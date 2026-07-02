"""Consumption seam v0: shared derived-lane pickup/acknowledgement helper.

Contract: ``orca/product/spines/data_lake/authority/core_spine_v0_data_lake_consumption_seam_contract_v0.md``.
Every derived lane discovers committed Bronze work and acknowledges completion
the same tested way:

- **Pickup is by-key** over committed availability (storage contract
  authority); no queue, event, or ``indexes/derived_retrieval`` view is ever
  consulted (view-independence — the conformance suite enforces it).
- **Obligation fingerprint**: the consumer computes a cheap canonical-JSON
  snapshot of the inputs its processing depends on; its sha256 is the
  fingerprint. An anchor is picked up unless an ack with the CURRENT
  fingerprint exists, so obligation growth (a late-arriving input record)
  re-surfaces the anchor automatically.
- **Acks are lane-owned completion facts**: append-only create-only records
  under ``acknowledgements/`` written through ``DataLakeRoot.append_record``
  (write-boundary enforcement). The ack namespace MUST be a lane name already
  declared in ``lane_registry.LANE_ROLES`` — the CI-guarded lane map is the
  single name authority; no second registry.
- **Fail toward re-verification, never fake-done**: an unreadable ack is
  treated as absent (the anchor re-surfaces); an ack is only written by the
  consumer with completion evidence in hand.

This module sits in the base ``data_lake`` layer beside ``lane_registry`` and
imports no producer code. It adds NO behavior to ``DataLakeRoot``, the
catalog, or availability — it is lane-side infrastructure consuming public
surfaces only.
"""
from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Iterator

from data_lake.canonical_json import canonical_record_bytes
from data_lake.lane_registry import LANE_ROLES

ACK_SCHEMA_VERSION = 1
_ACK_SUBTREE = "acknowledgements"
# record_id budget: "ack_" + 24 hex chars stays far inside the lake's safe-segment limit.
_ACK_ID_HEX_LEN = 24


class ConsumptionSeamError(ValueError):
    """A seam-contract violation (bad namespace, malformed obligation, missing evidence)."""


def validate_ack_namespace(ack_namespace: str) -> str:
    """An ack namespace must be a lane name declared in ``lane_registry.LANE_ROLES``."""
    if ack_namespace not in LANE_ROLES:
        raise ConsumptionSeamError(
            f"ack namespace {ack_namespace!r} is not a lane declared in lane_registry.LANE_ROLES; "
            "register the lane there first (the lane map is the single name authority)"
        )
    return ack_namespace


def obligation_fingerprint(obligation: Any) -> str:
    """sha256 over the obligation's canonical persisted bytes (key-sorted, so
    dict ordering never changes the fingerprint)."""
    try:
        return hashlib.sha256(canonical_record_bytes(obligation)).hexdigest()
    except (TypeError, ValueError) as exc:
        raise ConsumptionSeamError(f"obligation is not canonical-JSON serializable: {exc}") from exc


def ack_record_id(fingerprint: str) -> str:
    """Deterministic ack record id for one obligation fingerprint. Completing the
    same obligation twice collides on create and hard-fails visibly."""
    return f"ack_{fingerprint[:_ACK_ID_HEX_LEN]}"


def append_ack(
    root,
    *,
    raw_anchor: str,
    ack_namespace: str,
    obligation: Any,
    evidence: list[dict],
    generated_at: str | None = None,
) -> Path:
    """Append the lane-owned completion fact for ``obligation`` at ``raw_anchor``.

    ``evidence`` must carry the refs proving completion (record ids /
    completion markers / hashes) — an ack without evidence is refused: the ack
    asserts the lane met its obligation, so it must say how that is checkable.
    Create-only: acknowledging an already-acknowledged obligation raises from
    the lake write boundary rather than overwriting history.
    """
    validate_ack_namespace(ack_namespace)
    if not evidence:
        raise ConsumptionSeamError(
            f"refusing ack for {raw_anchor!r}/{ack_namespace!r} without completion evidence"
        )
    fingerprint = obligation_fingerprint(obligation)
    body = {
        "ack_schema_version": ACK_SCHEMA_VERSION,
        "record_kind": "acknowledgement",
        "ack_namespace": ack_namespace,
        "raw_anchor": raw_anchor,
        "obligation_fingerprint": fingerprint,
        "obligation": obligation,
        "evidence": evidence,
        "generated_at": generated_at or datetime.now(timezone.utc).isoformat(),
    }
    return root.append_record(
        subtree=_ACK_SUBTREE,
        raw_anchor=raw_anchor,
        lane=ack_namespace,
        record_id=ack_record_id(fingerprint),
        data=canonical_record_bytes(body),
    )


def _parse_ack(path: Path) -> dict | None:
    """A well-formed ack record, or ``None``. Corrupt/unreadable acks are treated
    as ABSENT for pickup decisions — the safe direction is re-verification,
    never fake-done; integrity diagnosis belongs to the lake doctor."""
    try:
        data = json.loads(path.read_bytes().decode("utf-8"))
    except (OSError, ValueError):
        return None
    if not isinstance(data, dict) or data.get("record_kind") != "acknowledgement":
        return None
    if not isinstance(data.get("obligation_fingerprint"), str):
        return None
    return data


def find_acks(root, *, raw_anchor: str, ack_namespace: str) -> list[dict]:
    """All well-formed ack records for one anchor + namespace (append-only history)."""
    validate_ack_namespace(ack_namespace)
    lane_dir = root.lane_dir(subtree=_ACK_SUBTREE, raw_anchor=raw_anchor, lane=ack_namespace)
    if not lane_dir.is_dir():
        return []
    acks: list[dict] = []
    for record_file in sorted(lane_dir.iterdir()):
        if not record_file.is_file():
            continue
        ack = _parse_ack(record_file)
        if ack is not None:
            acks.append(ack)
    return acks


def is_acknowledged(root, *, raw_anchor: str, ack_namespace: str, obligation: Any) -> bool:
    """True iff an ack for exactly this obligation fingerprint exists and parses.

    Fast path: the deterministic record id makes this one existence check; the
    body is still parsed and its fingerprint field verified so a truncated or
    tampered file never counts as done.
    """
    validate_ack_namespace(ack_namespace)
    fingerprint = obligation_fingerprint(obligation)
    target = root.record_path(
        subtree=_ACK_SUBTREE,
        raw_anchor=raw_anchor,
        lane=ack_namespace,
        record_id=ack_record_id(fingerprint),
    )
    if not target.is_file():
        return False
    ack = _parse_ack(target)
    return ack is not None and ack.get("obligation_fingerprint") == fingerprint


@dataclass(frozen=True)
class PickupItem:
    """One unit of undone work: the anchor, the obligation snapshot the consumer
    computed for it, and that snapshot's fingerprint (pass both to ``append_ack``
    after completing the work)."""

    raw_anchor: str
    obligation: Any
    fingerprint: str


def pickup(
    root,
    *,
    ack_namespace: str,
    obligation_fn: Callable[[str], Any],
    source_family: str | None = None,
) -> Iterator[PickupItem]:
    """Yield committed anchors whose current obligation is not yet acknowledged.

    ``obligation_fn(raw_anchor)`` must be CHEAP (no raw-body loading/re-hashing):
    it snapshots the inputs the consumer's processing depends on. Heavy packet
    loading belongs to the consumer's processing of the yielded items only.

    Always by-key reconcile: every committed anchor is enumerated and compared;
    there is no incremental shortcut that could silently miss late-arriving
    work, and no view is consulted.
    """
    validate_ack_namespace(ack_namespace)
    for raw_anchor in root.list_available(source_family=source_family):
        obligation = obligation_fn(raw_anchor)
        if is_acknowledged(
            root, raw_anchor=raw_anchor, ack_namespace=ack_namespace, obligation=obligation
        ):
            continue
        yield PickupItem(
            raw_anchor=raw_anchor,
            obligation=obligation,
            fingerprint=obligation_fingerprint(obligation),
        )


def iter_all_acks(root) -> Iterator[tuple[str, str, dict]]:
    """Walk the whole acknowledgements tree, yielding ``(raw_anchor, namespace,
    ack)`` for every well-formed ack record.

    Read-only walk of the contract-pinned grammar
    ``acknowledgements/<anchor_shard>/<raw-anchor>/<ack-namespace>/<ack-record-id>``
    (derived-layout contract); used by the rebuild runner to build the
    ``undone`` view. Corrupt records are skipped per the fail-toward-
    re-verification rule.
    """
    ack_root = root.path / _ACK_SUBTREE
    if not ack_root.is_dir():
        return
    for shard_dir in sorted(p for p in ack_root.iterdir() if p.is_dir()):
        for anchor_dir in sorted(p for p in shard_dir.iterdir() if p.is_dir()):
            for namespace_dir in sorted(p for p in anchor_dir.iterdir() if p.is_dir()):
                for record_file in sorted(p for p in namespace_dir.iterdir() if p.is_file()):
                    ack = _parse_ack(record_file)
                    if ack is not None:
                        yield anchor_dir.name, namespace_dir.name, ack


__all__ = [
    "ACK_SCHEMA_VERSION",
    "ConsumptionSeamError",
    "PickupItem",
    "ack_record_id",
    "append_ack",
    "find_acks",
    "is_acknowledged",
    "iter_all_acks",
    "obligation_fingerprint",
    "pickup",
    "validate_ack_namespace",
]
