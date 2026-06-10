"""Rung-1.5 price-payload capture runner (browser-free).

Closes the JS-hydrated SPA "displayed price is an empty shell" gap by recovering
displayed pricing INFORMATION (tiers + amounts + effective/settling signal) from
the structured payloads a rung-1 capture already preserves -- the React Router
hydration turbo-stream in the page HTML (tier structure + price tokens) joined,
by token, with the static ``prices`` object compiled into a linked JS module
asset (per-currency amounts). No headless browser; no hand-parsing of rendered
HTML; structured-payload parse only.

It runs OVER the existing rung-1 path: the same ``fetch_anti_blocking_http_capture``
adapter and ``block_shell`` guard used by ``run_source_capture_antiblock_http_packet``.
Every fetched body is block-shell-classified and a 200 is never trusted as
content. The "certified content" claim is an explicit interpretation-layer
discriminator over that recorded provenance (``certify_extraction``) -- it does
NOT weaken ``block_shell``.

The prices JS chunk is discovered by CONTENT ANCHOR (``prices:{"chatgpt.``)
across the page's module-preload list, never by asset hash, so it survives
redeploys. Discovery is bounded by a chunk-count and byte budget; if the payload
is not located, the run fails visibly (no fake success).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Sequence
from urllib.parse import urljoin, urlparse

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
)
from source_capture.adapters import (
    AntiBlockingHttpCaptureFailure,
    fetch_anti_blocking_http_capture,
)
from source_capture.block_shell import classify_capture_body
from source_capture.packet_assembly import stage_and_write_packet, staged_file_id_map
from source_capture.price_payload_extraction import (
    PRICES_ANCHOR,
    certify_extraction,
    chunk_contains_prices,
    decode_react_router_stream,
    extract_announcement_effective_date,
    extract_prices_object,
    extract_tier_structure,
    extract_token_list,
    join_tiers_with_amounts,
)
import re

DEFAULT_PAGE_URL = "https://chatgpt.com/pricing/"
DEFAULT_ANNOUNCEMENT_URL = "https://openai.com/index/introducing-chatgpt-pro/"

PRICE_PAYLOAD_NON_CLAIMS = [
    "browser-free: no headless browser, no rendered-DOM capture, no JS execution",
    "structured-payload parse only: no hand-parsing of rendered HTML text",
    "does not weaken block_shell; each fetched body keeps its block-shell class",
    "not the honest direct_http baseline",
    "not TLS/JA3 fingerprint impersonation; not proxy/session; not anti-detect",
    "not API SDK use; not archive retrieval; not media preservation",
    "amounts are the source-published list prices in minor currency units; not a "
    "quote, not tax-inclusive, not a personalized/checkout price",
    "displayed amount can vary by region/currency; USD selected unless overridden",
    "not ECR design; not Cleaning implementation; not Judgment scoring; not buyer proof",
]

_MODULEPRELOAD_RE = re.compile(
    r'<link[^>]+(?:rel="modulepreload"|as="script")[^>]*href="([^"]+)"'
)


def _sha256(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def _rung1_fetch(url: str, *, timeout: float, max_bytes: int):
    """One rung-1 fetch + block_shell classification. Returns (success, classification)."""
    result = fetch_anti_blocking_http_capture(url=url, timeout_seconds=timeout, max_bytes=max_bytes)
    if isinstance(result, AntiBlockingHttpCaptureFailure):
        return result, None
    classification = classify_capture_body(
        status=result.status, headers=result.response_headers, body=result.body
    )
    return result, classification


def _chunk_urls(page_html: str, base_url: str) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []
    for href in _MODULEPRELOAD_RE.findall(page_html):
        absolute = urljoin(base_url, href)
        if absolute not in seen:
            seen.add(absolute)
            ordered.append(absolute)
    return ordered


def _discover_prices_chunk(chunk_urls, *, timeout, max_chunks, byte_budget):
    """Fetch chunks (rung-1) in order, stop at the first carrying the prices anchor.

    Returns (url, success_result, classification, scanned_log) or raises ValueError.
    """
    scanned: list[dict] = []
    spent = 0
    for url in chunk_urls[:max_chunks]:
        success, classification = _rung1_fetch(url, timeout=timeout, max_bytes=12_000_000)
        if isinstance(success, AntiBlockingHttpCaptureFailure):
            scanned.append({"url": url, "status": "fetch_failed", "detail": success.message})
            continue
        spent += len(success.body)
        text = success.body.decode("utf-8", "replace")
        has = chunk_contains_prices(text)
        scanned.append({
            "url": url, "status": success.status, "bytes": len(success.body),
            "block_shell": classification.classification.value if classification else None,
            "has_prices_anchor": has,
        })
        if has:
            return url, success, classification, scanned
        if spent > byte_budget:
            raise ValueError(
                f"prices payload not found within byte budget ({byte_budget}); "
                f"scanned {len(scanned)} chunks"
            )
    raise ValueError(
        f"prices payload anchor {PRICES_ANCHOR.pattern!r} not found in "
        f"{len(scanned)} scanned module-preload chunks"
    )


def _resolved_tiers_to_json(resolved_tiers, currency: str) -> list[dict]:
    out = []
    for rt in resolved_tiers:
        out.append({
            "name": rt.name,
            "display_order": rt.display_order,
            "static_price": rt.static_price,
            "prices": [
                {
                    "price_token": rp.price_token,
                    "price_header": rp.price_header,
                    "descriptor": rp.descriptor,
                    "label": rp.label,
                    "currency": currency,
                    "amount_minor_units": rp.amount_minor,
                    "amount_display": rp.amount_display,
                    "token_updated_at": rp.token_updated_at,
                    "resolved": rp.resolved,
                }
                for rp in rt.prices
            ],
        })
    return out


def run_price_payload_capture(
    *,
    page_url: str,
    announcement_url: str | None,
    currency: str,
    output_directory: Path,
    decision_question: str,
    capture_context: str,
    operator_category: str,
    session_id: str | None,
    timeout_seconds: float,
    max_chunks: int,
    chunk_byte_budget: int,
) -> tuple[int, str]:
    capture_ts = None

    # --- 1. page (structure) over rung-1 -----------------------------------
    page_res, page_cls = _rung1_fetch(page_url, timeout=timeout_seconds, max_bytes=12_000_000)
    if isinstance(page_res, AntiBlockingHttpCaptureFailure):
        return 3, f"page fetch failed: {page_res.message}"
    capture_ts = page_res.metadata["capture_timestamp"]
    page_html = page_res.body.decode("utf-8", "replace")
    base_url = page_res.final_url

    # --- 2. discover + fetch prices chunk (amounts) over rung-1 ------------
    chunk_urls = _chunk_urls(page_html, base_url)
    if not chunk_urls:
        return 3, "no module-preload chunks found in page; cannot locate prices payload"
    try:
        chunk_url, chunk_res, chunk_cls, scan_log = _discover_prices_chunk(
            chunk_urls, timeout=timeout_seconds,
            max_chunks=max_chunks, byte_budget=chunk_byte_budget,
        )
    except ValueError as exc:
        return 3, str(exc)
    chunk_text = chunk_res.body.decode("utf-8", "replace")

    # --- 3. structured extraction (pure) -----------------------------------
    try:
        root = decode_react_router_stream(page_html)
        tiers = extract_tier_structure(root)
        prices = extract_prices_object(chunk_text)
        token_list = extract_token_list(chunk_text)
        resolved = join_tiers_with_amounts(tiers, prices, currency=currency)
    except ValueError as exc:
        return 3, f"structured extraction failed: {exc}"

    verdict = certify_extraction(
        page_block_class=page_cls.classification.value, page_status=page_res.status,
        page_block_signal=page_cls.signal,
        chunk_block_class=chunk_cls.classification.value, chunk_status=chunk_res.status,
        chunk_block_signal=chunk_cls.signal,
        token_list=token_list, prices=prices, resolved_tiers=resolved, currency=currency,
    )

    # --- 4. effective/settling signals -------------------------------------
    announcement_body = None
    announcement_cls = None
    pro_effective_date = None
    if announcement_url:
        ann_res, announcement_cls = _rung1_fetch(
            announcement_url, timeout=timeout_seconds, max_bytes=12_000_000
        )
        if not isinstance(ann_res, AntiBlockingHttpCaptureFailure):
            announcement_body = ann_res.body
            pro_effective_date = extract_announcement_effective_date(
                ann_res.body.decode("utf-8", "replace")
            )

    team_settling = sorted({
        rp.token_updated_at
        for rt in resolved for rp in rt.prices
        if rp.price_token.endswith(".2026") and rp.token_updated_at
    })
    effective_signals = {
        "page_native_forward_effective_date_string": None,
        "page_native_note": (
            "chatgpt.com/pricing does not publish a forward human effective-date "
            "string; a price change is encoded as versioned tokens (e.g. '.2026') "
            "plus per-entry CMS updatedAt timestamps."
        ),
        "team_business_2026_settled_at": {
            "value": team_settling,
            "source": "chatgpt.com/pricing react-router turbo-stream: prices[].updatedAt for .2026 tokens",
            "meaning": "publish/last-settled timestamp of the displayed (.2026) Business/Team price entries",
        },
        "pro_tier_effective_date": {
            "value": pro_effective_date,
            "source": (f"{announcement_url} (Next.js RSC publicationDateText)"
                       if announcement_url else None),
            "meaning": "date the ChatGPT Pro paid tier was introduced (when that price took effect)",
        },
    }

    coverage_instrumentation = {
        "wedge_source_set_signal": "Build for OpenAI; instrument for the set.",
        "per_source": [
            {
                "source": "openai_chatgpt_consumer_pricing",
                "locator": page_url,
                "framework": "React Router v7 (Remix successor)",
                "structure_location": "embedded HTML turbo-stream (window.__reactRouterContext)",
                "amount_location": "static prices object in a linked JS module asset",
                "rung15_extractable_browser_free": True,
            },
            {
                "source": "openai_api_pricing",
                "locator": "https://developers.openai.com/api/docs/pricing",
                "framework": "Astro v6 (static site generation)",
                "amount_location": "server-rendered directly in HTML (e.g. $20/$25 present in rung-1 body)",
                "rung15_extractable_browser_free": True,
                "note": "different extraction path: server-rendered amounts (recon signal, not built here)",
            },
            {
                "source": "openai_pricing_announcement",
                "locator": DEFAULT_ANNOUNCEMENT_URL,
                "framework": "Next.js (App Router RSC)",
                "amount_location": "self.__next_f RSC stream chunks (structured); carries publicationDate",
                "rung15_extractable_browser_free": True,
            },
        ],
        "currency_coverage": {
            "selected": currency,
            "available_currencies_per_token": {
                tk: len(cur) for tk, cur in sorted(prices.items())
            },
            "note": "the JS-module prices object carries per-currency amounts; "
                    "region-localized displayed price is a token x currency lookup",
        },
    }

    extraction = {
        "schema": "rung15_price_payload_extraction_v0",
        "method": "react_router_turbostream(structure) + js_module_prices_object(amounts), joined by priceToken",
        "browser_free": True,
        "source_surface": "openai_chatgpt_pricing",
        "page_url": page_url,
        "page_final_url": base_url,
        "prices_payload_url": chunk_url,
        "prices_payload_discovery": "by content anchor 'prices:{\"chatgpt.', not by asset hash",
        "currency": currency,
        "captured_at": capture_ts,
        "tiers": _resolved_tiers_to_json(resolved, currency),
        "price_token_amounts_usd": {
            tk: prices[tk].get(currency) for tk in token_list if tk in prices
        },
        "effective_signals": effective_signals,
        "coverage_instrumentation": coverage_instrumentation,
        "certification": verdict.as_dict(),
    }

    extraction_metadata = {
        "schema": "rung15_price_payload_capture_metadata_v0",
        "rung1_method": "anti_blocking_http header_complete_stdlib (same path as run_source_capture_antiblock_http_packet)",
        "page": {
            "requested_url": page_res.requested_url, "final_url": base_url,
            "status": page_res.status, "content_type": page_res.metadata.get("content_type"),
            "byte_count": len(page_res.body), "sha256": _sha256(page_res.body),
            "block_shell": page_cls.classification.value,
            "block_shell_signal": page_cls.signal,
        },
        "prices_chunk": {
            "url": chunk_url, "status": chunk_res.status,
            "content_type": chunk_res.metadata.get("content_type"),
            "byte_count": len(chunk_res.body), "sha256": _sha256(chunk_res.body),
            "block_shell": chunk_cls.classification.value,
            "module_preload_chunks_seen": len(chunk_urls),
            "chunk_scan_log": scan_log,
        },
        "announcement": (
            {
                "url": announcement_url,
                "block_shell": announcement_cls.classification.value if announcement_cls else None,
                "byte_count": len(announcement_body) if announcement_body else None,
                "sha256": _sha256(announcement_body) if announcement_body else None,
                "pro_effective_date_text": pro_effective_date,
            }
            if announcement_url else None
        ),
        "capture_timestamp": capture_ts,
    }

    # --- 5. assemble packet -------------------------------------------------
    artifacts: list[tuple[str, bytes]] = [
        ("rung15_pricing_page_body.bin", page_res.body),
        ("rung15_prices_payload_chunk.js", chunk_res.body),
        ("rung15_price_extraction.json",
         (json.dumps(extraction, indent=2, ensure_ascii=False) + "\n").encode("utf-8")),
        ("rung15_extraction_metadata.json",
         (json.dumps(extraction_metadata, indent=2, ensure_ascii=False) + "\n").encode("utf-8")),
        ("rung15_certification.json",
         (json.dumps(verdict.as_dict(), indent=2, ensure_ascii=False) + "\n").encode("utf-8")),
    ]
    if announcement_body is not None:
        artifacts.append(("rung15_announcement_body.bin", announcement_body))
    file_ids = staged_file_id_map(artifacts)

    if verdict.certified:
        access_posture = known_fact(
            "rung-1.5 payload extraction: displayed pricing tiers + amounts recovered "
            "browser-free from structured payloads (HTML turbo-stream structure + "
            "JS-module prices object amounts) and CONTENT-CERTIFIED via interpretation-layer "
            f"discriminator rung15_price_payload_v0 (all checks passed; "
            f"{verdict.priced_tier_count} tiers priced). Per-body block_shell stays "
            "content_unverified and is NOT weakened."
        )
        capture_limitations: list[str] = []
    else:
        failed = [c.name for c in verdict.checks if not c.passed]
        access_posture = known_fact(
            "rung-1.5 payload extraction did NOT certify content: discriminator "
            f"rung15_price_payload_v0 failed checks {failed}. Structured payloads preserved; "
            "displayed amounts not certified."
        )
        capture_limitations = [
            f"content_certification_failed: rung15_price_payload_v0 checks {failed}"
        ]

    cert_state = "certified" if verdict.certified else "uncertified"
    mode_changes = [
        f"anti_blocking_http_profile:{page_res.impersonation_profile}",
        "rung15_price_payload_extraction:react_router_turbostream+js_module_prices",
        f"block_shell_page:{page_cls.classification.value}",
        f"block_shell_prices_chunk:{chunk_cls.classification.value}",
        f"content_certification:{cert_state}",
    ]

    timing = PacketTiming(
        source_publication_or_event=unknown_with_reason(
            "rung-1.5 extractor did not infer a single source publication timestamp; "
            "per-tier effective/settling signals are recorded in the extraction artifact"
        ),
        source_edit_or_version=known_fact(
            "displayed price entries carry CMS updatedAt timestamps and versioned tokens "
            "(e.g. .2026); see rung15_price_extraction.json effective_signals"
        ),
        capture_time=known_fact(str(capture_ts)),
        recapture_time=not_applicable("no earlier capture supplied"),
        cutoff_posture=unknown_with_reason("cutoff posture metadata not supplied"),
    )
    archive_posture = not_attempted("rung-1.5 extractor does not query archive or history services")
    media_posture = not_attempted("rung-1.5 extractor preserves response payloads; no linked media fetch")
    recapture_posture = not_applicable("no prior source capture packet supplied")

    page_files = [
        file_ids["rung15_pricing_page_body.bin"],
        file_ids["rung15_price_extraction.json"],
        file_ids["rung15_extraction_metadata.json"],
        file_ids["rung15_certification.json"],
    ]
    slices = [
        SourceCaptureSlice(
            slice_id="slice_01_pricing_page_structure",
            locator=known_fact(base_url),
            timing=timing,
            access_posture=access_posture,
            archive_history_posture=archive_posture,
            media_modality_posture=media_posture,
            re_capture_relationship=recapture_posture,
            limitations=capture_limitations,
            warning_notes=list(page_res.warning_notes),
            preserved_file_ids=page_files,
        ),
        SourceCaptureSlice(
            slice_id="slice_02_prices_payload_chunk",
            locator=known_fact(chunk_url),
            timing=timing,
            access_posture=known_fact(
                f"prices amounts payload (static JS module asset); HTTP {chunk_res.status}; "
                f"block_shell={chunk_cls.classification.value}; discovered by content anchor"
            ),
            archive_history_posture=archive_posture,
            media_modality_posture=media_posture,
            re_capture_relationship=recapture_posture,
            limitations=[],
            warning_notes=list(chunk_res.warning_notes),
            preserved_file_ids=[file_ids["rung15_prices_payload_chunk.js"]],
        ),
    ]
    if announcement_body is not None:
        slices.append(SourceCaptureSlice(
            slice_id="slice_03_pro_effective_date_announcement",
            locator=known_fact(announcement_url),
            timing=timing,
            access_posture=known_fact(
                "ChatGPT Pro effective-date companion source (Next.js RSC); "
                f"block_shell={announcement_cls.classification.value}; "
                f"publicationDate={pro_effective_date!r}"
            ),
            archive_history_posture=archive_posture,
            media_modality_posture=media_posture,
            re_capture_relationship=recapture_posture,
            limitations=[],
            warning_notes=[],
            preserved_file_ids=[file_ids["rung15_announcement_body.bin"]],
        ))

    result = stage_and_write_packet(
        output_directory=output_directory,
        staged_artifacts=artifacts,
        source_slices=slices,
        source_family="vendor_pricing_page",
        source_surface="openai_chatgpt_pricing_rung15",
        source_locator=known_fact(page_url),
        decision_question=decision_question,
        capture_context=capture_context,
        actor_audience_context=unknown_with_reason(
            "actor/audience context not supplied to the rung-1.5 extractor"
        ),
        capture_mode=CaptureModeCategory.STRUCTURED_ACCESS,
        operator_category=operator_category,
        session_identity=session_id,
        visible_mode_changes=mode_changes,
        source_publication_or_event=timing.source_publication_or_event,
        source_edit_or_version=timing.source_edit_or_version,
        cutoff_posture=timing.cutoff_posture,
        recapture_time=timing.recapture_time,
        access_posture=access_posture,
        archive_history_posture=archive_posture,
        media_modality_posture=media_posture,
        re_capture_relationship=recapture_posture,
        warnings=list(page_res.warning_notes),
        limitations=capture_limitations,
        receipt_summary=(
            f"rung-1.5 price-payload capture for openai_chatgpt_pricing: "
            f"{verdict.priced_tier_count} priced tiers recovered browser-free "
            f"(structure=react-router turbo-stream, amounts=JS-module prices object); "
            f"content_certification={cert_state}; block_shell per body content_unverified."
        ),
        receipt_non_claims=PRICE_PAYLOAD_NON_CLAIMS,
    )
    status = 0 if verdict.certified else 4
    return status, result.output_directory


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description=(
            "Rung-1.5 browser-free price-payload capture: recover displayed pricing "
            "tiers + amounts + effective/settling signal from a JS-hydrated SPA pricing "
            "page via structured-payload extraction over the rung-1 anti-block HTTP path."
        )
    )
    p.add_argument("--url", default=DEFAULT_PAGE_URL)
    p.add_argument("--announcement-url", default=DEFAULT_ANNOUNCEMENT_URL,
                   help="effective-date companion source; pass '' to skip")
    p.add_argument("--currency", default="usd")
    p.add_argument("--output", type=Path, required=True)
    p.add_argument("--decision-question",
                   default="OpenAI ChatGPT consumer pricing tiers + amounts + effective date")
    p.add_argument("--capture-context",
                   default="Orca pricing-wedge proof case C; rung-1.5 payload-extraction sub-lane")
    p.add_argument("--operator-category", default="rung15_price_payload_cli_operator")
    p.add_argument("--session-id", default=None)
    p.add_argument("--timeout-seconds", type=float, default=25.0)
    p.add_argument("--max-chunks", type=int, default=20)
    p.add_argument("--chunk-byte-budget", type=int, default=20_000_000)
    return p


def main(argv: Sequence[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)
    announcement_url = args.announcement_url or None
    try:
        exit_code, message = run_price_payload_capture(
            page_url=args.url,
            announcement_url=announcement_url,
            currency=args.currency.lower(),
            output_directory=args.output,
            decision_question=args.decision_question,
            capture_context=args.capture_context,
            operator_category=args.operator_category,
            session_id=args.session_id,
            timeout_seconds=args.timeout_seconds,
            max_chunks=args.max_chunks,
            chunk_byte_budget=args.chunk_byte_budget,
        )
    except ValueError as exc:
        parser.exit(status=2, message=f"rung-1.5 price-payload capture failed: {exc}\n")
    except Exception as exc:  # noqa: BLE001 - surface any failure as exit 3
        parser.exit(status=3, message=f"rung-1.5 price-payload capture failed: {exc}\n")

    print(message)
    if exit_code == 0:
        print("content_certification: certified")
    elif exit_code == 4:
        print("content_certification: UNCERTIFIED (packet written; see certification artifact)")
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
