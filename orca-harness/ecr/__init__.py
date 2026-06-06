"""ECR (Evidence Candidate Record) source-side package.

Slice-1 realizes the SP-3 (pre-decision timing/cutoff) row of the ECR
source-side field schema ratified at 387b630
(docs/product/core_spine_v0_data_and_cleaning_spine_boundary_v0.md).

Authorization provenance: built under explicit owner current-turn authorization
(a ``/fused`` implementation turn; option A of the ECR-gate decision), bounded to
slice-1 -- the SP-3 timing model + pure deriver + unit tests. ECR is a
separately-gated boundary (``.agents/workflow-overlay/safety-rules.md``):
slice-2 (EvidenceUnit binding, cutoff_posture -> pre_decision_status mapping,
the reconciliation rules, provenance marker), Cleaning, Judgment, and
commits/pushes each require their own separate authorization. JSG-01 stays
FROZEN.
"""
from ecr.deriver import derive_timing_postures
from ecr.models import EcrTimingPosture, EcrTimingResidual

__all__ = [
    "EcrTimingPosture",
    "EcrTimingResidual",
    "derive_timing_postures",
]
