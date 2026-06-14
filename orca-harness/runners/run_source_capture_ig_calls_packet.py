"""Bounded, logged-out IG wind-caller CALLS capture -> Source Capture Packet.

Composes existing primitives (no new auth/session path, no secrets):
- browser_snapshot (headless, LOGGED-OUT; scroll to enumerate the profile grid),
- ig_calls_parse (og:description -> caption/likes/comments/date/#ad; permalinks),
- cadence.bounded_jitter (human-mimicking variable gaps between item visits),
- writer.write_local_source_capture_packet (one packet: profile slice + N call slices).

Substrate basis: the recon + 2026-06-14 headless probe found IG serves the call
signal (caption + engagement) in the post/reel page og:description to a browser,
LOGGED-OUT. This runner therefore needs no session. Reel view/play counts (media
GraphQL) and any session-only depth are OUT of scope here (deferred).

Bounded by the wind-caller carve-out: attended, human-mimicking cadence, no
standing/scheduled crawler, per-run item cap. This is one bounded capture unit
(one named account's recent calls), launched by an operator; there is no
scheduler entrypoint.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path
from typing import Callable, Sequence

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from source_capture import (
    CaptureModeCategory,
    PacketTiming,
    SourceCaptureSlice,
    known_fact,
    not_applicable,
    not_attempted,
    unknown_with_reason,
    write_local_source_capture_packet,
)
from source_capture.adapters import BrowserSnapshotFailure, fetch_browser_snapshot_capture
from source_capture.adapters.browser_snapshot import (
    DEFAULT_MAX_ARTIFACT_BYTES,
    DEFAULT_TIMEOUT_SECONDS,
    DEFAULT_VIEWPORT_HEIGHT,
    DEFAULT_VIEWPORT_WIDTH,
)
from source_capture.cadence import build_cadence_plan
from source_capture.ig_calls_parse import (
    extract_item_permalinks,
    extract_meta_content,
    parse_ig_og_description,
    parse_ig_profile_og,
)

IG_CALLS_NON_CLAIMS = [
    "not content sufficiency proof",
    "not login or session capture",
    "not stored profile or cookie use",
    "not anti-detect behavior",
    "not proxy or session injection",
    "not CAPTCHA solving",
    "not crawler or scheduled monitoring",
    "not full-history backfill",
    "not reel view-count capture",
    "not media byte preservation",
    "not API SDK use",
    "not ECR design",
    "not Cleaning implementation",
    "not Judgment scoring",
    "not buyer proof",
    "not commercial-readiness logic",
]

DEFAULT_MAX_ITEMS = 12
DEFAULT_PROFILE_SCROLL_PASSES = 3
DEFAULT_CADENCE_WINDOW_SECONDS = 900.0
DEFAULT_CADENCE_MIN_GAP_SECONDS = 8.0
DEFAULT_CADENCE_MAX_GAP_SECONDS = 45.0


def _detect_ig_block(*, final_url: str, title: str | None, visible_text: str, rendered_dom: str) -> str | None:
    """Return a block reason if the page is an access/anti-bot wall, else None.

    Logged-out IG shows "Log in"/"Sign up" while still serving the og:description,
    so those alone are NOT a block. Only a login redirect, a 429 interstitial, or
    an explicit network-security block count.
    """
    final_low = final_url.lower()
    if "/accounts/login" in final_low:
        return "redirected_to_login"
    probe = f"{title or ''}\n{visible_text[:3000]}\n{rendered_dom[:3000]}".lower()
    if "please wait a few minutes before you try again" in probe:
        return "rate_limited_429_interstitial"
    if "you've been blocked" in probe or "you have been blocked" in probe:
        return "network_security_block"
    return None


def _capture_one(url: str, *, scroll_passes: int, timeout_seconds: float, viewport_width: int,
                 viewport_height: int, max_artifact_bytes: int):
    return fetch_browser_snapshot_capture(
        url=url,
        timeout_seconds=timeout_seconds,
        wait_until="load",
        viewport_width=viewport_width,
        viewport_height=viewport_height,
        max_artifact_bytes=max_artifact_bytes,
        scroll_passes=scroll_passes,
    )


def run_source_capture_ig_calls_packet(
    *,
    profile_url: str,
    output_directory: Path,
    decision_question: str,
    max_items: int = DEFAULT_MAX_ITEMS,
    profile_scroll_passes: int = DEFAULT_PROFILE_SCROLL_PASSES,
    cadence_window_seconds: float = DEFAULT_CADENCE_WINDOW_SECONDS,
    cadence_min_gap_seconds: float = DEFAULT_CADENCE_MIN_GAP_SECONDS,
    cadence_max_gap_seconds: float = DEFAULT_CADENCE_MAX_GAP_SECONDS,
    cadence_random_seed: int | None = None,
    timeout_seconds: float = DEFAULT_TIMEOUT_SECONDS,
    viewport_width: int = DEFAULT_VIEWPORT_WIDTH,
    viewport_height: int = DEFAULT_VIEWPORT_HEIGHT,
    max_artifact_bytes: int = DEFAULT_MAX_ARTIFACT_BYTES,
    capture_context: str = "logged-out IG wind-caller calls capture (no session); one bounded account, recent calls",
    operator_category: str = "ig_calls_browser_snapshot_cli_operator",
    session_id: str | None = None,
    warnings: Sequence[str] = (),
    limitations: Sequence[str] = (),
    sleep_fn: Callable[[float], None] = time.sleep,
) -> tuple[int, str]:
    if max_items <= 0:
        raise ValueError("max_items must be greater than zero")

    profile = _capture_one(
        profile_url, scroll_passes=profile_scroll_passes, timeout_seconds=timeout_seconds,
        viewport_width=viewport_width, viewport_height=viewport_height, max_artifact_bytes=max_artifact_bytes,
    )
    if isinstance(profile, BrowserSnapshotFailure):
        return 3, f"profile capture failed: {profile.message}"
    block = _detect_ig_block(
        final_url=profile.final_url, title=profile.title,
        visible_text=profile.visible_text, rendered_dom=profile.rendered_dom,
    )
    if block is not None:
        return 3, f"profile access-blocked ({block}); recorded NO-GO, no packet written"

    permalinks = extract_item_permalinks(profile.rendered_dom)[:max_items]
    if not permalinks:
        return 3, "no /p/ or /reel/ permalinks enumerated from the profile grid"

    profile_og = extract_meta_content(profile.rendered_dom, "og:description")
    profile_stats = parse_ig_profile_og(profile_og) if profile_og else None
    capture_timestamp = str(profile.metadata["capture_timestamp"])

    # Human-mimicking gaps between the per-item visits (auditable, deterministic per seed).
    cadence = build_cadence_plan(
        slot_count=len(permalinks),
        mode="bounded_jitter",
        delay_seconds=0.0,
        window_seconds=cadence_window_seconds,
        min_gap_seconds=cadence_min_gap_seconds,
        max_gap_seconds=cadence_max_gap_seconds,
        random_seed=cadence_random_seed,
    )

    item_records: list[dict] = []
    for index, url in enumerate(permalinks):
        if index > 0:
            sleep_fn(cadence.planned_waits_seconds[index - 1])
        item = _capture_one(
            url, scroll_passes=0, timeout_seconds=timeout_seconds, viewport_width=viewport_width,
            viewport_height=viewport_height, max_artifact_bytes=max_artifact_bytes,
        )
        if isinstance(item, BrowserSnapshotFailure):
            item_records.append({"url": url, "status": "capture_failed", "message": item.message})
            continue
        item_block = _detect_ig_block(
            final_url=item.final_url, title=item.title,
            visible_text=item.visible_text, rendered_dom=item.rendered_dom,
        )
        if item_block is not None:
            item_records.append({"url": item.final_url, "status": "access_blocked", "block_reason": item_block})
            continue
        og = extract_meta_content(item.rendered_dom, "og:description")
        if not og:
            item_records.append({"url": item.final_url, "status": "no_signal",
                                 "message": "no og:description on item page"})
            continue
        parsed = parse_ig_og_description(og)
        item_records.append({
            "url": item.final_url,
            "status": "captured",
            "caption": parsed.caption,
            "likes": parsed.likes,
            "comments": parsed.comments,
            "date": parsed.date,
            "is_ad": parsed.is_ad,
            "caption_truncated": parsed.truncated,
            "raw_og": parsed.raw_og,
        })

    return _write_packet(
        profile_url=profile.requested_url,
        profile_final_url=profile.final_url,
        profile_stats=profile_stats,
        permalink_count=len(permalinks),
        capture_timestamp=capture_timestamp,
        cadence_summary=cadence.to_dict(),
        item_records=item_records,
        output_directory=output_directory,
        decision_question=decision_question,
        capture_context=capture_context,
        operator_category=operator_category,
        session_id=session_id,
        warnings=list(warnings),
        limitations=list(limitations),
    )


def _slice_postures():
    access = known_fact(
        "ig_logged_out_browser_snapshot; public og:description; content sufficiency not asserted"
    )
    archive = not_attempted("IG calls runner does not query archive or history services")
    media = known_fact(
        "og:description caption + engagement text preserved; reel view-counts and media bytes are out of scope"
    )
    recapture = not_applicable("no prior source capture packet was supplied for this IG calls capture")
    return access, archive, media, recapture


def _write_packet(
    *,
    profile_url: str,
    profile_final_url: str,
    profile_stats,
    permalink_count: int,
    capture_timestamp: str,
    cadence_summary: dict,
    item_records: list[dict],
    output_directory: Path,
    decision_question: str,
    capture_context: str,
    operator_category: str,
    session_id: str | None,
    warnings: list[str],
    limitations: list[str],
) -> tuple[int, str]:
    access, archive, media, recapture = _slice_postures()
    staging_parent = output_directory.parent
    staging_parent.mkdir(parents=True, exist_ok=True)

    captured_count = sum(1 for r in item_records if r["status"] == "captured")
    stats_dict = (
        {"followers": profile_stats.followers, "following": profile_stats.following, "posts": profile_stats.posts}
        if profile_stats is not None
        else None
    )
    profile_payload = {
        "profile_url": profile_final_url,
        "stats": stats_dict,
        "permalinks_enumerated": permalink_count,
        "cadence_plan": cadence_summary,
    }

    # One staged file per slice: file_01 = profile, file_02.. = each item.
    staged: list[tuple[Path, dict]] = [(staging_parent / "ig_profile.json", profile_payload)]
    for i, record in enumerate(item_records, start=1):
        staged.append((staging_parent / f"ig_call_{i:02d}.json", record))

    if any(path.exists() for path, _ in staged):
        raise ValueError("IG calls staging files already exist in the output parent; clear them before rerunning")

    written: list[Path] = []
    try:
        for path, payload in staged:
            path.write_text(
                json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
                encoding="utf-8",
                newline="\n",
            )
            written.append(path)

        def _timing(publication) -> PacketTiming:
            return PacketTiming(
                source_publication_or_event=publication,
                source_edit_or_version=unknown_with_reason("IG calls runner did not infer source edit/version timing"),
                capture_time=known_fact(capture_timestamp),
                recapture_time=not_applicable("IG calls packet does not model an earlier capture by default"),
                cutoff_posture=unknown_with_reason("IG calls runner did not receive cutoff posture metadata"),
            )

        profile_timing = _timing(
            unknown_with_reason("profile slice is the enumeration source, not a dated post")
        )
        slices = [
            SourceCaptureSlice(
                slice_id="ig_profile_00",
                locator=known_fact(profile_final_url),
                timing=profile_timing,
                access_posture=access,
                archive_history_posture=archive,
                media_modality_posture=media,
                re_capture_relationship=recapture,
                limitations=[],
                warning_notes=[],
                preserved_file_ids=["file_01"],
            )
        ]
        for i, record in enumerate(item_records, start=1):
            date = record.get("date")
            publication = known_fact(date) if date else unknown_with_reason(
                f"item {record['status']}: no post date parsed"
            )
            slice_limitations: list[str] = []
            if record["status"] != "captured":
                slice_limitations.append(f"item_not_captured: {record['status']}")
            elif record.get("caption_truncated"):
                slice_limitations.append(
                    "caption_truncated_in_og: long caption may be cut at IG's og cap; rendered caption DOM not yet captured"
                )
            slices.append(
                SourceCaptureSlice(
                    slice_id=f"ig_call_{i:02d}",
                    locator=known_fact(record["url"]),
                    timing=_timing(publication),
                    access_posture=access,
                    archive_history_posture=archive,
                    media_modality_posture=media,
                    re_capture_relationship=recapture,
                    limitations=slice_limitations,
                    warning_notes=[],
                    preserved_file_ids=[f"file_{i + 1:02d}"],
                )
            )

        run_limitations = list(limitations)
        if captured_count < len(item_records):
            run_limitations.append(
                f"partial_capture: {captured_count}/{len(item_records)} items yielded a call signal"
            )

        result = write_local_source_capture_packet(
            output_directory=output_directory,
            input_files=written,
            source_family="instagram_creator",
            source_surface="ig_calls_browser_snapshot",
            source_locator=known_fact(profile_url),
            decision_question=decision_question,
            capture_context=capture_context,
            actor_audience_context=known_fact(
                "public-figure creator public profile; logged-out capture; internal wind-caller calibration"
            ),
            capture_mode=CaptureModeCategory.AUTOMATED_EXTRACTION,
            operator_category=operator_category,
            session_identity=session_id,
            visible_mode_changes=[f"ig_calls_logged_out_capture:items={len(item_records)}:captured={captured_count}"],
            source_publication_or_event=profile_timing.source_publication_or_event,
            source_edit_or_version=profile_timing.source_edit_or_version,
            cutoff_posture=profile_timing.cutoff_posture,
            recapture_time=profile_timing.recapture_time,
            access_posture=access,
            archive_history_posture=archive,
            media_modality_posture=media,
            re_capture_relationship=recapture,
            source_slices=slices,
            warnings=list(warnings),
            limitations=run_limitations,
            receipt_summary=(
                f"IG calls packet for {profile_final_url}: {captured_count} of {len(item_records)} "
                "enumerated items yielded a logged-out call signal (caption + engagement)."
            ),
            receipt_non_claims=IG_CALLS_NON_CLAIMS,
        )
    finally:
        for path in written:
            try:
                path.unlink()
            except FileNotFoundError:
                pass
    return 0, result.output_directory


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Capture one IG creator's recent CALLS (logged-out) into a Source Capture Packet."
    )
    parser.add_argument("--profile-url", required=True)
    parser.add_argument("--decision-question", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--max-items", type=int, default=DEFAULT_MAX_ITEMS)
    parser.add_argument("--profile-scroll-passes", type=int, default=DEFAULT_PROFILE_SCROLL_PASSES)
    parser.add_argument("--cadence-window-seconds", type=float, default=DEFAULT_CADENCE_WINDOW_SECONDS)
    parser.add_argument("--cadence-min-gap-seconds", type=float, default=DEFAULT_CADENCE_MIN_GAP_SECONDS)
    parser.add_argument("--cadence-max-gap-seconds", type=float, default=DEFAULT_CADENCE_MAX_GAP_SECONDS)
    parser.add_argument("--cadence-random-seed", type=int, default=None)
    parser.add_argument("--timeout-seconds", type=float, default=DEFAULT_TIMEOUT_SECONDS)
    parser.add_argument("--max-artifact-bytes", type=int, default=DEFAULT_MAX_ARTIFACT_BYTES)
    parser.add_argument("--session-id", default=None)
    parser.add_argument("--warning", action="append", default=[])
    parser.add_argument("--limitation", action="append", default=[])
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)
    try:
        exit_code, message = run_source_capture_ig_calls_packet(
            profile_url=args.profile_url,
            output_directory=args.output,
            decision_question=args.decision_question,
            max_items=args.max_items,
            profile_scroll_passes=args.profile_scroll_passes,
            cadence_window_seconds=args.cadence_window_seconds,
            cadence_min_gap_seconds=args.cadence_min_gap_seconds,
            cadence_max_gap_seconds=args.cadence_max_gap_seconds,
            cadence_random_seed=args.cadence_random_seed,
            timeout_seconds=args.timeout_seconds,
            max_artifact_bytes=args.max_artifact_bytes,
            session_id=args.session_id,
            warnings=args.warning,
            limitations=args.limitation,
        )
    except ValueError as exc:
        parser.exit(status=2, message=f"source capture ig calls failed: {exc}\n")
    except Exception as exc:  # noqa: BLE001 - surface any failure visibly with a nonzero exit
        parser.exit(status=3, message=f"source capture ig calls failed: {exc}\n")

    if exit_code == 0:
        print(message)
        return 0
    parser.exit(status=exit_code, message=f"source capture ig calls failed: {message}\n")
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
