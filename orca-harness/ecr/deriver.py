"""ECR SP-3 source-side timing deriver (slice-1).

A pure M1 carry of each source slice's already-closed ``cutoff_posture`` into an
``EcrTimingPosture``. It coins no vocabulary, performs no I/O, does not mutate
the input packet, binds no ``EvidenceUnit``, and makes no JSG-01, scoring, or
readiness claim. The packet->EvidenceUnit binding and the
``cutoff_posture -> pre_decision_status`` mapping are deliberately out of scope
(slice-2).
"""
from __future__ import annotations

import re

from ecr.models import (
    EcrInspectabilityPosture,
    EcrTimingPosture,
    EcrTimingResidual,
    InspectabilityState,
)
from source_capture.models import SourceCapturePacket, VisibleFactStatus


def derive_timing_postures(packet: SourceCapturePacket) -> list[EcrTimingPosture]:
    """Derive the SP-3 timing posture for each source slice, in slice order.

    For each slice, the slice's ``timing.cutoff_posture`` (a ``VisibleFact``) is
    either M1-carried verbatim when its status is KNOWN (clearing only on
    ``"pre_cutoff"``) or recorded as a named residual when the status is not
    KNOWN, preserving the producer's status and reason. One posture is returned
    per source slice.
    """
    postures: list[EcrTimingPosture] = []
    for source_slice in packet.source_slices:
        fact = source_slice.timing.cutoff_posture
        if fact.status == VisibleFactStatus.KNOWN:
            postures.append(
                EcrTimingPosture(
                    slice_id=source_slice.slice_id,
                    carried_cutoff_posture=fact.value,
                    clears_pre_cutoff=fact.value == "pre_cutoff",
                )
            )
        else:
            postures.append(
                EcrTimingPosture(
                    slice_id=source_slice.slice_id,
                    residual=EcrTimingResidual(status=fact.status, reason=fact.reason),
                    clears_pre_cutoff=False,
                )
            )
    return postures


_SHA256_HEX = re.compile(r"\A[0-9a-fA-F]{64}\Z")
_PLACEHOLDER_SHA256 = "0" * 64


def _is_verifiable_sha256(value: str) -> bool:
    """D-C: a non-placeholder sha256 is 64 hex chars (case-insensitive) and not
    the all-zero sentinel.

    The producer schema does not constrain ``sha256`` shape, so the deriver must
    make this discrimination -- a hash-shaped placeholder is not verifiability.
    """
    return bool(_SHA256_HEX.match(value)) and value.lower() != _PLACEHOLDER_SHA256


def derive_inspectability_postures(
    packet: SourceCapturePacket,
) -> list[EcrInspectabilityPosture]:
    """Derive the SP-2 inspectability posture for each source slice, in slice order.

    Per slice, fail-closed "all referenced files must verify":

    - ``inspectable_verifiable`` (clears) iff the slice references >=1 preserved
      file AND every referenced file has a non-placeholder sha256.
    - ``inspectable_reference_only`` (does not clear) when something is pointable
      but not fully verifiable: referenced files exist but not all verify, or no
      files are referenced yet the slice locator is KNOWN.
    - ``not_inspectable`` (does not clear) when nothing is inspectable: no
      referenced files and the locator is not KNOWN.

    Pure: no I/O, no packet mutation, no ``EvidenceUnit`` binding. The integrity
    hash is read by reference and recomputed elsewhere, never trusted here. One
    posture is returned per source slice.
    """
    files_by_id = {pf.file_id: pf for pf in packet.preserved_files}
    postures: list[EcrInspectabilityPosture] = []
    for source_slice in packet.source_slices:
        referenced = [
            files_by_id[file_id]
            for file_id in source_slice.preserved_file_ids
            if file_id in files_by_id
        ]
        unverifiable = [pf for pf in referenced if not _is_verifiable_sha256(pf.sha256)]
        locator_known = source_slice.locator.status == VisibleFactStatus.KNOWN

        if referenced and not unverifiable:
            postures.append(
                EcrInspectabilityPosture(
                    slice_id=source_slice.slice_id,
                    state=InspectabilityState.INSPECTABLE_VERIFIABLE,
                    clears_inspectable=True,
                )
            )
        elif referenced or locator_known:
            if referenced:
                bad = ", ".join(sorted(pf.file_id for pf in unverifiable))
                reason = (
                    f"referenced preserved file(s) with placeholder or invalid "
                    f"sha256: {bad}; bytes are held but integrity is not verifiable."
                )
            else:
                reason = (
                    "no preserved file referenced; slice locator is known "
                    "(reference only)."
                )
            postures.append(
                EcrInspectabilityPosture(
                    slice_id=source_slice.slice_id,
                    state=InspectabilityState.INSPECTABLE_REFERENCE_ONLY,
                    clears_inspectable=False,
                    reason=reason,
                )
            )
        else:
            postures.append(
                EcrInspectabilityPosture(
                    slice_id=source_slice.slice_id,
                    state=InspectabilityState.NOT_INSPECTABLE,
                    clears_inspectable=False,
                    reason="no preserved file referenced and slice locator is not known.",
                )
            )
    return postures
