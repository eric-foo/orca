"""Persist Fragrantica Cleaning output into the Data Lake.

The verified read half lives on ``DataLakeRoot``. This adapter reads a committed
Fragrantica raw packet by key, rebuilds the mechanical Fragrantica projection,
builds the source-family Cleaning packet, and appends one lane-owned derived
record at ``derived/<anchor_shard>/<packet_id>/cleaning_fragrantica/<record_id>.json``.

Boundary: this persists Cleaning ledger output only. It does not write lake core
fields, change raw, decide sentiment, infer demand, bind Evidence Units, or make
Judgment claims.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import TYPE_CHECKING, Any

from cleaning.fragrantica import build_fragrantica_cleaning_packet
from cleaning.models import CLEANING_CORE_VERSION, REQUIRED_NON_CLAIMS, CleaningPacket
from harness_utils import generate_ulid
from source_capture.fragrantica_projection import (
    FRAGRANTICA_PROJECTION_CERTIFICATION,
    FRAGRANTICA_PROJECTION_METHOD,
    FRAGRANTICA_PROJECTION_VERSION,
    build_fragrantica_projection,
)
from source_capture.models import SourceCapturePacket, VisibleFactStatus

if TYPE_CHECKING:
    from data_lake.root import DataLakeRoot


FRAGRANTICA_CLEANING_LANE = "cleaning_fragrantica"
FRAGRANTICA_CLEANING_RECORD_SCHEMA_VERSION = "fragrantica_cleaning_packet_record_v0"
SILVER_VAULT_RECORD_SCHEMA_VERSION = "silver_vault_record_v0"
_CONTENT_HASH_BASIS = "canonical_json_excluding_content_hash"
_PRODUCER_ID = "orca-harness.cleaning.fragrantica_lake.derive_fragrantica_cleaning_into_lake"


def derive_fragrantica_cleaning_into_lake(
    *,
    data_root: "DataLakeRoot",
    packet_id: str,
    record_id: str | None = None,
) -> tuple[CleaningPacket, Path]:
    """Build and append the Fragrantica Cleaning packet for a committed raw packet.

    Re-derive = a fresh sibling record. A caller-supplied ``record_id`` is still
    create-only through ``DataLakeRoot.append_record``.
    """
    loaded = data_root.load_raw_packet(packet_id)
    packet = SourceCapturePacket.model_validate(loaded.manifest)
    projection = build_fragrantica_projection(
        packet=packet,
        raw_file_bytes_by_file_id=loaded.bodies,
    )
    cleaning_packet = build_fragrantica_cleaning_packet(projection)

    record = record_id if record_id is not None else generate_ulid()
    record_name = f"{record}.json"
    payload = fragrantica_cleaning_record_payload(
        packet=packet,
        cleaning_packet=cleaning_packet,
        record_id=record_name,
    )
    path = data_root.append_record(
        subtree="derived",
        raw_anchor=packet_id,
        lane=FRAGRANTICA_CLEANING_LANE,
        record_id=record_name,
        data=_json_bytes(payload),
    )
    return cleaning_packet, path


def fragrantica_cleaning_record_payload(
    *,
    packet: SourceCapturePacket,
    cleaning_packet: CleaningPacket,
    record_id: str,
) -> dict[str, Any]:
    """Return the Silver-compatible record payload before lake append."""
    capture_time = _known_capture_time(packet)
    record: dict[str, Any] = {
        "record_id": record_id,
        "raw_anchor": packet.packet_id,
        "lane_namespace": FRAGRANTICA_CLEANING_LANE,
        "producer_id": _PRODUCER_ID,
        "schema_version": SILVER_VAULT_RECORD_SCHEMA_VERSION,
        "producer_schema_version": FRAGRANTICA_CLEANING_RECORD_SCHEMA_VERSION,
        "content_hash": "",
        "content_hash_basis": _CONTENT_HASH_BASIS,
        "record_kind": "observation",
        "payload_kind": "FragranticaCleaningPacket",
        "producer_row_kind": "fragrantica_cleaning_packet",
        "source_family": packet.source_family,
        "source_surface": packet.source_surface,
        "observed_at": capture_time,
        "captured_at": capture_time,
        "raw_refs": _raw_refs(cleaning_packet),
        "derived_refs": [],
        "coverage": _coverage(cleaning_packet),
        "payload": {
            "cleaning_core_version": CLEANING_CORE_VERSION,
            "projection_method": FRAGRANTICA_PROJECTION_METHOD,
            "projection_version": FRAGRANTICA_PROJECTION_VERSION,
            "projection_certification": FRAGRANTICA_PROJECTION_CERTIFICATION,
            "handle_count": len(cleaning_packet.handles),
            "transform_entry_count": len(cleaning_packet.transform_ledger),
            "cleaning_packet": cleaning_packet.model_dump(mode="json"),
        },
        "non_claims": sorted(
            {
                *REQUIRED_NON_CLAIMS,
                "not_archive_completeness",
                "not_demand_signal",
                "not_evidence_unit_binding",
                "not_judgment",
                "not_sentiment_analysis",
            }
        ),
    }
    record["content_hash"] = f"sha256:{_content_hash(record)}"
    return record


def _known_capture_time(packet: SourceCapturePacket) -> str:
    if packet.timing.capture_time.status != VisibleFactStatus.KNOWN or not packet.timing.capture_time.value:
        raise ValueError(
            "Fragrantica Cleaning observation records require a known capture_time "
            "for observed_at and captured_at."
        )
    return packet.timing.capture_time.value


def _coverage(cleaning_packet: CleaningPacket) -> dict[str, Any]:
    residuals = sorted(
        {
            residual
            for handle in cleaning_packet.handles
            for residual in handle.residuals
        }
    )
    return {
        "basis": "fragrantica_current_window_cleaning_packet",
        "current_window_only": True,
        "full_archive_captured": False,
        "handle_count": len(cleaning_packet.handles),
        "transform_entry_count": len(cleaning_packet.transform_ledger),
        "residuals": residuals,
        "raw_pull_triggers": sorted(
            {
                trigger
                for handle in cleaning_packet.handles
                for trigger in handle.raw_pull_triggers
            }
        ),
    }


def _raw_refs(cleaning_packet: CleaningPacket) -> list[dict[str, str | None]]:
    refs: dict[tuple[str | None, ...], dict[str, str | None]] = {}
    for handle in cleaning_packet.handles:
        anchor = handle.raw_anchor
        key = (
            anchor.packet_id,
            anchor.slice_id,
            anchor.file_id,
            anchor.relative_packet_path,
            anchor.sha256,
            anchor.hash_basis,
        )
        refs[key] = {
            "packet_id": anchor.packet_id,
            "slice_id": anchor.slice_id,
            "file_id": anchor.file_id,
            "relative_packet_path": anchor.relative_packet_path,
            "sha256": anchor.sha256,
            "hash_basis": anchor.hash_basis,
        }
    return [refs[key] for key in sorted(refs)]


def _content_hash(record: dict[str, Any]) -> str:
    canonical = dict(record)
    canonical.pop("content_hash", None)
    return hashlib.sha256(_canonical_json_bytes(canonical)).hexdigest()


def _canonical_json_bytes(value: Any) -> bytes:
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    ).encode("utf-8")


def _json_bytes(value: Any) -> bytes:
    return (
        json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False)
        + "\n"
    ).encode("utf-8")


__all__ = [
    "FRAGRANTICA_CLEANING_LANE",
    "FRAGRANTICA_CLEANING_RECORD_SCHEMA_VERSION",
    "derive_fragrantica_cleaning_into_lake",
    "fragrantica_cleaning_record_payload",
]
