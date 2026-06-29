"""Generic Silver lineage helpers for records that adopt the Silver Vault header.

This module is deliberately producer-level. It builds and validates the Common
Record Header fields in the emitted record; it does not create a persisted
``silver_lineage`` wrapper and it does not globally gate every lake write.
"""
from __future__ import annotations

import hashlib
import json
from collections.abc import Mapping, Sequence
from typing import Any

SILVER_VAULT_RECORD_SCHEMA_VERSION = "silver_vault_record_v0"
SILVER_CONTENT_HASH_BASIS = "canonical_json_excluding_content_hash"

HEADER_FIELDS = (
    "record_id",
    "raw_anchor",
    "lane_namespace",
    "producer_id",
    "schema_version",
    "producer_schema_version",
    "content_hash",
    "content_hash_basis",
    "record_kind",
    "payload_kind",
    "producer_row_kind",
    "source_surface",
    "observed_at",
    "captured_at",
    "raw_refs",
    "derived_refs",
)

LINEAGE_FIELDS = (*HEADER_FIELDS, "source_object", "lineage_limitations")
RECORD_KINDS = frozenset({"entity", "relationship", "observation"})
LINEAGE_RELATIONS = frozenset(
    {
        "observed_from",
        "selected_from",
        "derived_from",
        "consumed",
        "selected",
        "corrects",
        "supersedes",
        "conflicts_with",
    }
)
LIMITATION_REASON_TOKENS = frozenset(
    {
        "transient_source_not_persisted",
        "raw_ref_unavailable",
        "derived_ref_unavailable",
        "projection_row_locator_unavailable",
        "legacy_record_missing_lineage",
        "source_record_unresolvable",
    }
)


class SilverLineageError(ValueError):
    """Raised when a record cannot satisfy the adopted Silver lineage contract."""


def _require_non_blank(value: Any, field: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise SilverLineageError(f"{field} must be a non-empty string")
    return value


def _as_list(value: Sequence[Mapping[str, Any]] | None) -> list[dict[str, Any]]:
    return [dict(item) for item in (value or [])]


def source_object_ref(
    *, namespace: str, kind: str, native_id: str, source_url: str | None = None
) -> dict[str, str | None]:
    """Build source-local identity metadata using the Silver ``entity_key`` vocabulary."""
    ref: dict[str, str | None] = {
        "namespace": _require_non_blank(namespace, "source_object.namespace"),
        "kind": _require_non_blank(kind, "source_object.kind"),
        "native_id": _require_non_blank(native_id, "source_object.native_id"),
        "source_url": source_url,
    }
    if source_url is not None:
        _require_non_blank(source_url, "source_object.source_url")
    return ref


def raw_packet_ref(
    *,
    packet_id: str,
    slice_id: str | None = None,
    file_id: str | None = None,
    relative_packet_path: str | None = None,
    sha256: str | None = None,
    hash_basis: str | None = None,
    anchor_kind: str = "file",
    anchor_value: str | None = None,
    relation: str = "consumed",
) -> dict[str, Any]:
    """Build a raw-packet/file ref that keeps packet, file, hash, and anchor together."""
    _validate_relation(relation)
    if (sha256 is None) != (hash_basis is None):
        raise SilverLineageError("raw_refs sha256 and hash_basis must be supplied together")
    if file_id is not None and (relative_packet_path is None or sha256 is None):
        raise SilverLineageError(
            "raw_refs with file_id must include relative_packet_path, sha256, and hash_basis"
        )
    ref = {
        "ref_type": "raw_packet",
        "packet_id": _require_non_blank(packet_id, "raw_refs.packet_id"),
        "slice_id": _optional_non_blank(slice_id, "raw_refs.slice_id"),
        "file_id": _optional_non_blank(file_id, "raw_refs.file_id"),
        "relative_packet_path": _optional_non_blank(
            relative_packet_path, "raw_refs.relative_packet_path"
        ),
        "sha256": _optional_non_blank(sha256, "raw_refs.sha256"),
        "hash_basis": _optional_non_blank(hash_basis, "raw_refs.hash_basis"),
        "anchor": {
            "kind": _require_non_blank(anchor_kind, "raw_refs.anchor.kind"),
            "value": _optional_non_blank(anchor_value, "raw_refs.anchor.value"),
        },
        "relation": relation,
    }
    validate_raw_ref(ref)
    return ref


def derived_record_ref(
    *,
    raw_anchor: str,
    lane: str,
    record_id: str,
    relation: str = "consumed",
    row_id: str | None = None,
    row_kind: str | None = None,
    sha256: str | None = None,
    hash_basis: str | None = None,
    record_set_completion_lane: str | None = None,
) -> dict[str, Any]:
    """Build an exact derived-record ref, optionally pinned to a projection row."""
    _validate_relation(relation)
    if (row_id is None) != (row_kind is None):
        raise SilverLineageError("derived_refs row_locator requires both row_id and row_kind")
    if (sha256 is None) != (hash_basis is None):
        raise SilverLineageError("derived_refs sha256 and hash_basis must be supplied together")
    ref: dict[str, Any] = {
        "ref_type": "derived_record",
        "raw_anchor": _require_non_blank(raw_anchor, "derived_refs.raw_anchor"),
        "lane": _require_non_blank(lane, "derived_refs.lane"),
        "record_id": _require_non_blank(record_id, "derived_refs.record_id"),
        "sha256": _optional_non_blank(sha256, "derived_refs.sha256"),
        "hash_basis": _optional_non_blank(hash_basis, "derived_refs.hash_basis"),
        "relation": relation,
    }
    if row_id is not None:
        ref["row_locator"] = {
            "row_id": _require_non_blank(row_id, "derived_refs.row_locator.row_id"),
            "row_kind": _require_non_blank(row_kind, "derived_refs.row_locator.row_kind"),
        }
    if record_set_completion_lane is not None:
        ref["record_set_completion_lane"] = _require_non_blank(
            record_set_completion_lane, "derived_refs.record_set_completion_lane"
        )
    validate_derived_ref(ref)
    return ref


def lineage_limitation(reason: str, detail: str | None = None) -> dict[str, str | None]:
    """Build a controlled limitation entry."""
    if reason not in LIMITATION_REASON_TOKENS:
        raise SilverLineageError(f"unsupported lineage limitation reason: {reason!r}")
    return {"reason": reason, "detail": _optional_non_blank(detail, "lineage_limitations.detail")}


def build_silver_vault_record(
    *,
    payload: Mapping[str, Any],
    record_id: str,
    raw_anchor: str,
    lane_namespace: str,
    producer_id: str,
    producer_schema_version: str,
    record_kind: str,
    payload_kind: str,
    producer_row_kind: str,
    source_surface: str,
    source_object: Mapping[str, Any],
    observed_at: str | None,
    captured_at: str | None,
    raw_refs: Sequence[Mapping[str, Any]] | None = None,
    derived_refs: Sequence[Mapping[str, Any]] | None = None,
    lineage_limitations: Sequence[Mapping[str, Any]] | None = None,
    require_full_source_backed: bool = False,
) -> dict[str, Any]:
    """Return ``payload`` plus the Silver Vault Common Record Header fields."""
    record = dict(payload)
    collisions = sorted(set(record) & set(LINEAGE_FIELDS))
    if collisions:
        raise SilverLineageError(
            "payload must not predefine Silver lineage/header fields: " + ", ".join(collisions)
        )

    record.update(
        {
            "record_id": _require_non_blank(record_id, "record_id"),
            "raw_anchor": _require_non_blank(raw_anchor, "raw_anchor"),
            "lane_namespace": _require_non_blank(lane_namespace, "lane_namespace"),
            "producer_id": _require_non_blank(producer_id, "producer_id"),
            "schema_version": SILVER_VAULT_RECORD_SCHEMA_VERSION,
            "producer_schema_version": _require_non_blank(
                producer_schema_version, "producer_schema_version"
            ),
            "content_hash_basis": SILVER_CONTENT_HASH_BASIS,
            "record_kind": _require_record_kind(record_kind),
            "payload_kind": _require_non_blank(payload_kind, "payload_kind"),
            "producer_row_kind": _require_non_blank(producer_row_kind, "producer_row_kind"),
            "source_surface": _require_non_blank(source_surface, "source_surface"),
            "source_object": dict(source_object),
            "observed_at": _optional_non_blank(observed_at, "observed_at"),
            "captured_at": _optional_non_blank(captured_at, "captured_at"),
            "raw_refs": _as_list(raw_refs),
            "derived_refs": _as_list(derived_refs),
            "lineage_limitations": _as_list(lineage_limitations),
        }
    )
    record["content_hash"] = "sha256:" + canonical_record_sha256(record)
    validate_silver_vault_record(record, require_full_source_backed=require_full_source_backed)
    return record


def canonical_record_sha256(record: Mapping[str, Any]) -> str:
    body = json.dumps(
        _without_content_hash(record),
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(body).hexdigest()


def is_full_source_backed(record: Mapping[str, Any]) -> bool:
    """True only when refs exist and no explicit lineage limitation remains."""
    return bool(record.get("raw_refs") or record.get("derived_refs")) and not bool(
        record.get("lineage_limitations")
    )


def validate_silver_vault_record(
    record: Mapping[str, Any], *, require_full_source_backed: bool = False
) -> None:
    if "silver_lineage" in record:
        raise SilverLineageError("records must not persist a nested silver_lineage block")

    missing = [field for field in HEADER_FIELDS if field not in record]
    if missing:
        raise SilverLineageError("record missing Silver header fields: " + ", ".join(missing))
    if "source_object" not in record:
        raise SilverLineageError("record missing source_object")
    if "lineage_limitations" not in record:
        raise SilverLineageError("record missing lineage_limitations")

    _require_non_blank(record["record_id"], "record_id")
    _require_non_blank(record["raw_anchor"], "raw_anchor")
    _require_non_blank(record["lane_namespace"], "lane_namespace")
    _require_non_blank(record["producer_id"], "producer_id")
    _require_non_blank(record["producer_schema_version"], "producer_schema_version")
    if record["schema_version"] != SILVER_VAULT_RECORD_SCHEMA_VERSION:
        raise SilverLineageError("schema_version must be silver_vault_record_v0")
    if record["content_hash_basis"] != SILVER_CONTENT_HASH_BASIS:
        raise SilverLineageError("content_hash_basis must be canonical_json_excluding_content_hash")
    _require_record_kind(record["record_kind"])
    _require_non_blank(record["payload_kind"], "payload_kind")
    _require_non_blank(record["producer_row_kind"], "producer_row_kind")
    _require_non_blank(record["source_surface"], "source_surface")
    _validate_source_object(record["source_object"])
    _validate_refs(record.get("raw_refs"), validate_raw_ref, "raw_refs")
    _validate_refs(record.get("derived_refs"), validate_derived_ref, "derived_refs")
    _validate_limitations(record.get("lineage_limitations"))

    if not record.get("raw_refs") and not record.get("derived_refs") and not record.get(
        "lineage_limitations"
    ):
        raise SilverLineageError(
            "record must carry raw_refs, derived_refs, or explicit lineage_limitations"
        )
    expected_hash = "sha256:" + canonical_record_sha256(record)
    if record["content_hash"] != expected_hash:
        raise SilverLineageError("content_hash does not match canonical record content")
    if require_full_source_backed and not is_full_source_backed(record):
        raise SilverLineageError(
            "record is not eligible for full source-backed completeness: lineage refs missing or limited"
        )


def validate_raw_ref(ref: Mapping[str, Any]) -> None:
    if ref.get("ref_type") != "raw_packet":
        raise SilverLineageError("raw_refs entries must have ref_type='raw_packet'")
    _require_non_blank(ref.get("packet_id"), "raw_refs.packet_id")
    _validate_relation(ref.get("relation"))
    anchor = ref.get("anchor")
    if not isinstance(anchor, Mapping):
        raise SilverLineageError("raw_refs.anchor must be an object")
    _require_non_blank(anchor.get("kind"), "raw_refs.anchor.kind")
    if ref.get("file_id") is not None:
        _require_non_blank(ref.get("relative_packet_path"), "raw_refs.relative_packet_path")
        _require_non_blank(ref.get("sha256"), "raw_refs.sha256")
        _require_non_blank(ref.get("hash_basis"), "raw_refs.hash_basis")


def validate_derived_ref(ref: Mapping[str, Any]) -> None:
    if ref.get("ref_type") != "derived_record":
        raise SilverLineageError("derived_refs entries must have ref_type='derived_record'")
    _require_non_blank(ref.get("raw_anchor"), "derived_refs.raw_anchor")
    _require_non_blank(ref.get("lane"), "derived_refs.lane")
    _require_non_blank(ref.get("record_id"), "derived_refs.record_id")
    _validate_relation(ref.get("relation"))
    if (ref.get("sha256") is None) != (ref.get("hash_basis") is None):
        raise SilverLineageError("derived_refs sha256 and hash_basis must be supplied together")
    if "row_locator" in ref:
        locator = ref["row_locator"]
        if not isinstance(locator, Mapping):
            raise SilverLineageError("derived_refs.row_locator must be an object")
        _require_non_blank(locator.get("row_id"), "derived_refs.row_locator.row_id")
        _require_non_blank(locator.get("row_kind"), "derived_refs.row_locator.row_kind")


def _optional_non_blank(value: str | None, field: str) -> str | None:
    if value is None:
        return None
    return _require_non_blank(value, field)


def _validate_relation(value: Any) -> str:
    relation = _require_non_blank(value, "relation")
    if relation not in LINEAGE_RELATIONS:
        raise SilverLineageError(f"unsupported lineage relation: {relation!r}")
    return relation


def _require_record_kind(value: Any) -> str:
    record_kind = _require_non_blank(value, "record_kind")
    if record_kind not in RECORD_KINDS:
        raise SilverLineageError(f"unsupported record_kind: {record_kind!r}")
    return record_kind


def _validate_source_object(value: Any) -> None:
    if not isinstance(value, Mapping):
        raise SilverLineageError("source_object must be an object")
    _require_non_blank(value.get("namespace"), "source_object.namespace")
    _require_non_blank(value.get("kind"), "source_object.kind")
    _require_non_blank(value.get("native_id"), "source_object.native_id")


def _validate_refs(value: Any, validator, field: str) -> None:  # noqa: ANN001
    if not isinstance(value, list):
        raise SilverLineageError(f"{field} must be a list")
    for item in value:
        if not isinstance(item, Mapping):
            raise SilverLineageError(f"{field} entries must be objects")
        validator(item)


def _validate_limitations(value: Any) -> None:
    if not isinstance(value, list):
        raise SilverLineageError("lineage_limitations must be a list")
    for item in value:
        if not isinstance(item, Mapping):
            raise SilverLineageError("lineage_limitations entries must be controlled objects")
        reason = item.get("reason")
        if reason not in LIMITATION_REASON_TOKENS:
            raise SilverLineageError(f"unsupported lineage limitation reason: {reason!r}")


def _without_content_hash(value: Any) -> Any:
    if isinstance(value, Mapping):
        return {
            key: _without_content_hash(item)
            for key, item in sorted(value.items())
            if key != "content_hash"
        }
    if isinstance(value, list):
        return [_without_content_hash(item) for item in value]
    return value
