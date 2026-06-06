"""ECR SP-3 source-side timing deriver (slice-1).

A pure M1 carry of each source slice's already-closed ``cutoff_posture`` into an
``EcrTimingPosture``. It coins no vocabulary, performs no I/O, does not mutate
the input packet, binds no ``EvidenceUnit``, and makes no JSG-01, scoring, or
readiness claim. The packet->EvidenceUnit binding and the
``cutoff_posture -> pre_decision_status`` mapping are deliberately out of scope
(slice-2).
"""
from __future__ import annotations

from ecr.models import EcrTimingPosture, EcrTimingResidual
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
