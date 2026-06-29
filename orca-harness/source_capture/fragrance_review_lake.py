"""Fragrance review widget-response lake tee + projection.

Two thin, capture-lane units that mirror the ratified Retail/PDP lake pilot
(``source_capture/retail_pdp_projection.py``):

- ``write_fragrance_review_capture_packet`` tees the EXACT raw review
  widget-response bytes (``body_text.encode("utf-8")``) into the Data Lake as
  write-once ``PreservedFile`` bodies -- one preserved file per review-bearing
  widget response, one slice per PDP. It carries only capture metadata in the
  manifest; no coverage/selection field ever enters a preserved body.
- ``project_fragrance_review_into_lake`` reads a committed raw packet by key
  (hash-verified via ``DataLakeRoot.load_raw_packet``), decodes the preserved
  widget bodies, builds the focused review coverage projection from them, and
  appends it as an append-only derived record under
  ``derived/<packet_id>/projection_fragrance_review/<record_id>.json``.

Claim ceiling (deliberate): this preserves raw widget-response bytes and
re-derives a view from them. It is NOT a durable, typed Attachment Record. The
typed AR entry (source_family / payload-kind / schema-version / replay-pins /
posture + per-attachment discovery) stays data-lake-lane-owned, and it must be
able to reference or supersede these preserved bodies WITHOUT inheriting the
positional ``file_id`` or any staging-path semantics. Named residual: operator
``widget_route`` / ``source_id`` are NOT round-tripped through the preserved
bodies -- the projection re-derives ``source_site`` / ``source_id`` from the
manifest ``product_url``; rich provenance belongs to that future AR entry.

This module is import-clean for the no-runtime-imports source-capture contract
(it never imports a network module; ``urllib.parse`` is permitted).
"""
from __future__ import annotations

import json
from datetime import date
from pathlib import Path
from typing import TYPE_CHECKING, Any, Mapping, Sequence
from urllib.parse import urlparse

from harness_utils import generate_ulid, utc_now_z
from source_capture.fragrance_review_coverage import (
    FragranceReviewCoverageReceipt,
    build_fragrance_review_coverage,
)
from source_capture.models import (
    PacketTiming,
    SourceCaptureSlice,
    known_fact,
    not_applicable,
    not_attempted,
    unknown_with_reason,
)
from source_capture.packet_assembly import stage_and_write_packet, staged_file_id_map

if TYPE_CHECKING:
    from data_lake.root import DataLakeRoot
    from source_capture.fragrance_rendered_widget_companion import FragranceWidgetResponseCapture
    from source_capture.models import PacketWriteResult


FRAGRANCE_REVIEW_SOURCE_FAMILY = "fragrance_review"
FRAGRANCE_REVIEW_SOURCE_SURFACE = "rendered_widget_review"

# Append-only derived lane namespace for the fragrance review coverage projection.
PROJECTION_FRAGRANCE_REVIEW_LANE = "projection_fragrance_review"

# Review-bearing widget response kinds whose bodies carry parseable review rows.
# Mirrors fragrance_rendered_widget_companion._REVIEW_RESPONSE_KINDS.
_REVIEW_RESPONSE_KINDS = frozenset({"judgeme_reviews_for_widget", "yotpo_v3_reviews"})

FRAGRANCE_REVIEW_LAKE_NON_CLAIMS = [
    "not source acquisition",
    "not source-wide review coverage",
    "not durable Attachment Records",
    "not ECR, Cleaning, Judgment, pain/pleasure labeling, or review-integrity scoring",
]


class FragranceReviewLakeInputError(ValueError):
    """A tee/projection input cannot be preserved or projected honestly."""


def write_fragrance_review_capture_packet(
    *,
    output_directory: Path | None = None,
    data_root: "DataLakeRoot | None" = None,
    widget_responses: Sequence["FragranceWidgetResponseCapture"],
    product_url: str,
    source_family: str = FRAGRANCE_REVIEW_SOURCE_FAMILY,
    source_surface: str = FRAGRANCE_REVIEW_SOURCE_SURFACE,
    decision_question: str = "fragrance review demand evidence",
    capture_context: str = "fragrance rendered-widget review-response bytes preserved into the lake",
    session_id: str | None = None,
    warnings: Sequence[str] | None = None,
    limitations: Sequence[str] | None = None,
) -> "PacketWriteResult":
    """Tee the EXACT raw review widget-response bytes into a Source Capture Packet.

    Each review-bearing widget response (``response_kind`` in the review kinds
    AND a non-empty ``body_text``) becomes one preserved raw body, staged as
    ``body_text.encode("utf-8")`` so the writer's recomputed sha256 equals the
    capture-time ``body_sha256`` (``hash_basis="raw_stored_bytes"``). One slice
    references those bodies in order. No coverage/selection field is staged.

    Block-don't-fake: if no review-bearing response carries a body, raise rather
    than write an empty/contaminated packet.
    """
    review_responses = [
        response
        for response in widget_responses
        if getattr(response, "response_kind", None) in _REVIEW_RESPONSE_KINDS
        and getattr(response, "body_text", None)
    ]
    if not review_responses:
        raise FragranceReviewLakeInputError(
            "no review-bearing widget responses with body_text to preserve; block-don't-fake"
        )

    staged_artifacts: list[tuple[str, bytes]] = []
    for index, response in enumerate(review_responses, start=1):
        body_text = response.body_text or ""
        filename = f"{index:02d}_widget_response_{response.response_kind}.json"
        staged_artifacts.append((filename, body_text.encode("utf-8")))
    file_ids = staged_file_id_map(staged_artifacts)

    locator = known_fact(product_url)
    timing = PacketTiming(
        source_publication_or_event=unknown_with_reason(
            "fragrance review tee did not infer source publication or event timing"
        ),
        source_edit_or_version=unknown_with_reason(
            "fragrance review tee did not infer source edit or version timing"
        ),
        capture_time=known_fact(utc_now_z()),
        recapture_time=not_applicable("fragrance review tee does not model an earlier capture by default"),
        cutoff_posture=unknown_with_reason("fragrance review tee did not receive cutoff posture metadata"),
    )
    access_posture = known_fact("rendered_widget_review_response_tee")
    archive_posture = not_attempted(
        "fragrance review tee preserves widget responses only and does not query archive or history services"
    )
    media_posture = not_attempted(
        "fragrance review tee preserves widget JSON responses only and does not fetch linked media assets"
    )
    recapture_posture = not_applicable("no prior source capture packet was supplied for this fragrance review tee")

    packet_warnings = list(warnings or [])
    packet_limitations = list(limitations or [])
    source_slice = SourceCaptureSlice(
        slice_id="slice_01",
        locator=locator,
        timing=timing,
        access_posture=access_posture,
        archive_history_posture=archive_posture,
        media_modality_posture=media_posture,
        re_capture_relationship=recapture_posture,
        limitations=packet_limitations,
        warning_notes=packet_warnings,
        preserved_file_ids=[file_ids[filename] for filename, _content in staged_artifacts],
    )

    return stage_and_write_packet(
        output_directory=output_directory,
        data_root=data_root,
        staged_artifacts=staged_artifacts,
        source_slices=[source_slice],
        source_family=source_family,
        source_surface=source_surface,
        source_locator=locator,
        decision_question=decision_question,
        capture_context=capture_context,
        session_identity=session_id,
        access_posture=access_posture,
        archive_history_posture=archive_posture,
        media_modality_posture=media_posture,
        re_capture_relationship=recapture_posture,
        source_publication_or_event=timing.source_publication_or_event,
        source_edit_or_version=timing.source_edit_or_version,
        cutoff_posture=timing.cutoff_posture,
        recapture_time=timing.recapture_time,
        warnings=packet_warnings,
        limitations=packet_limitations,
        receipt_summary=(
            f"Fragrance review widget-response tee with {len(staged_artifacts)} preserved raw widget response(s)."
        ),
        receipt_non_claims=FRAGRANCE_REVIEW_LAKE_NON_CLAIMS,
    )


def project_fragrance_review_into_lake(
    *,
    data_root: "DataLakeRoot",
    packet_id: str,
    record_id: str | None = None,
    as_of_date: date | None = None,
) -> tuple[FragranceReviewCoverageReceipt, Path]:
    """Project a committed raw fragrance-review packet into a derived coverage record.

    Reads the raw packet by key (``DataLakeRoot.load_raw_packet`` -- fail-closed
    re-hash), decodes each preserved widget body in manifest order, builds the
    focused review coverage projection from those bytes, and appends it at
    ``derived/<packet_id>/projection_fragrance_review/<record_id>.json``
    (append-only; re-derive = new sibling). Adds no capture, fetch, Cleaning,
    ECR, or Judgment. Returns the coverage receipt and the derived record path.

    Determinism: selection depends on ``as_of_date`` (the coverage builder
    defaults to ``date.today()``); pass a pinned ``as_of_date`` for a
    byte-identical re-derivation from the same committed bytes.

    Named residual (typed-AR-owned): operator ``widget_route`` / ``source_id``
    are not preserved in the raw bodies, so ``source_site`` / ``source_id`` are
    re-derived from the manifest ``product_url`` and ``widget_route`` is empty.
    """
    loaded = data_root.load_raw_packet(packet_id)
    manifest = loaded.manifest

    product_url = _manifest_source_locator_value(manifest) or ""
    source_site = urlparse(product_url).netloc or product_url or packet_id
    source_id = source_site

    ordered_bodies: list[str] = []
    for preserved in _manifest_preserved_files(manifest):
        file_id = preserved.get("file_id")
        if not isinstance(file_id, str) or file_id not in loaded.bodies:
            raise FragranceReviewLakeInputError(
                f"committed packet {packet_id} is missing a verified body for preserved file {file_id!r}"
            )
        ordered_bodies.append(loaded.bodies[file_id].decode("utf-8"))

    receipt = build_fragrance_review_coverage(
        widget_responses=ordered_bodies,
        source_id=source_id,
        source_site=source_site,
        product_url=product_url,
        widget_route={},
        as_of_date=as_of_date,
    )

    record = record_id if record_id is not None else generate_ulid()
    data = (f"{json.dumps(receipt.model_dump(mode='json'), indent=2, sort_keys=True)}\n").encode("utf-8")
    derived_path = data_root.append_record(
        subtree="derived",
        raw_anchor=packet_id,
        lane=PROJECTION_FRAGRANCE_REVIEW_LANE,
        record_id=f"{record}.json",
        data=data,
    )
    return receipt, derived_path


def _manifest_source_locator_value(manifest: Mapping[str, Any]) -> str | None:
    locator = manifest.get("source_locator")
    if isinstance(locator, Mapping) and locator.get("status") == "known":
        value = locator.get("value")
        return value if isinstance(value, str) and value else None
    return None


def _manifest_preserved_files(manifest: Mapping[str, Any]) -> list[Mapping[str, Any]]:
    preserved = manifest.get("preserved_files")
    if not isinstance(preserved, list) or not preserved:
        raise FragranceReviewLakeInputError("committed raw manifest has no preserved_files to project")
    files: list[Mapping[str, Any]] = []
    for entry in preserved:
        if not isinstance(entry, Mapping):
            raise FragranceReviewLakeInputError("committed raw manifest preserved_files entry is not an object")
        files.append(entry)
    return files


__all__ = [
    "FRAGRANCE_REVIEW_LAKE_NON_CLAIMS",
    "FRAGRANCE_REVIEW_SOURCE_FAMILY",
    "FRAGRANCE_REVIEW_SOURCE_SURFACE",
    "PROJECTION_FRAGRANCE_REVIEW_LANE",
    "FragranceReviewLakeInputError",
    "project_fragrance_review_into_lake",
    "write_fragrance_review_capture_packet",
]
