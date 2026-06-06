"""ECR (Evidence Candidate Record) source-side package.

Realizes source-side rows of the ECR field schema ratified at 387b630
(``docs/product/core_spine_v0_data_and_cleaning_spine_boundary_v0.md``), one pure
per-slice deriver per row:

- SP-3 (pre-decision timing/cutoff): ``EcrTimingPosture`` +
  ``derive_timing_postures`` (M1 carry of the producer's closed ``cutoff_posture``).
- SP-2 (inspectability): ``EcrInspectabilityPosture`` +
  ``derive_inspectability_postures`` (M2 derived-read over the M1-carried
  ``PreservedFile.sha256`` integrity anchor and the slice locator).

Both are per-source-slice (single-grain), perform no I/O, mutate no input, bind no
``EvidenceUnit``, and make no JSG-01, scoring, or readiness claim.

Authorization provenance: each slice is built under explicit owner current-turn
authorization (a ``/fused`` implementation turn; option A of the ECR-gate
decision) -- slice-1 = SP-3, slice-2 = SP-2. ECR is a separately-gated boundary
(``.agents/workflow-overlay/safety-rules.md``): the remaining SP-1 / SP-6
derivers, any packet->EvidenceUnit binding, Cleaning, Judgment, and
commits/pushes each require their own separate authorization. JSG-01 stays
FROZEN.

There is no ``cutoff_posture -> pre_decision_status`` mapping or reconciliation
layer here: SP-3 and SP-4 are distinct conductor subpredicates, so the ECR is a
parallel record the frozen conductor reads, not a projection into EvidenceUnit.
"""
from ecr.deriver import derive_inspectability_postures, derive_timing_postures
from ecr.models import (
    EcrInspectabilityPosture,
    EcrTimingPosture,
    EcrTimingResidual,
    InspectabilityState,
)

__all__ = [
    "EcrInspectabilityPosture",
    "EcrTimingPosture",
    "EcrTimingResidual",
    "InspectabilityState",
    "derive_inspectability_postures",
    "derive_timing_postures",
]
