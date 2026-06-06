"""ECR (Evidence Candidate Record) source-side models -- SP-3 timing slice.

Slice-1 of the ECR source-side field schema ratified in
``docs/product/core_spine_v0_data_and_cleaning_spine_boundary_v0.md`` (387b630).
This module realizes ONLY the SP-3 row (source-side pre-decision timing/cutoff
posture) of the four-field schema. SP-1 / SP-2 / SP-6 rows are deferred and may
be added later without reshaping these models.

Design constraints (do not relax without explicit owner authorization):

- M1 carry, no coining: the cutoff vocabulary is single-sourced from
  ``source_capture.models.CUTOFF_POSTURE_VALUES`` and the residual status from
  ``source_capture.models.VisibleFactStatus``. This module declares no parallel
  posture vocabulary (validation-gates.md: "enumerate once; reference it").
- Derived source-side posture only. It does NOT bind ``EvidenceUnit``, map to
  ``pre_decision_status``, or make any JSG-01, scoring, or readiness claim.
"""
from __future__ import annotations

from pydantic import model_validator

from schemas.case_models import StrictModel
from source_capture.models import CUTOFF_POSTURE_VALUES, VisibleFactStatus

# A residual exists exactly when the producer did NOT assert a KNOWN cutoff
# posture; KNOWN is excluded because a known value is carried (M1), never
# recorded as a residual. Derived from the single-sourced VisibleFactStatus so
# no status vocabulary is re-declared here.
RESIDUAL_TIMING_STATUSES = frozenset(VisibleFactStatus) - {VisibleFactStatus.KNOWN}


class EcrTimingResidual(StrictModel):
    """Named residual (M3) for a slice whose cutoff posture is not KNOWN.

    Carries the producer's own non-known ``VisibleFact`` status and reason
    verbatim; it coins no posture vocabulary of its own.
    """

    status: VisibleFactStatus
    reason: str

    @model_validator(mode="after")
    def validate_residual(self) -> "EcrTimingResidual":
        if self.status not in RESIDUAL_TIMING_STATUSES:
            allowed = ", ".join(sorted(s.value for s in RESIDUAL_TIMING_STATUSES))
            raise ValueError(
                f"EcrTimingResidual.status must be a non-known VisibleFactStatus "
                f"({{{allowed}}}); got {self.status.value!r}. A KNOWN cutoff posture "
                f"is carried (M1), not recorded as a residual."
            )
        if not self.reason.strip():
            raise ValueError("EcrTimingResidual.reason must be non-empty.")
        return self


class EcrTimingPosture(StrictModel):
    """SP-3 source-side timing posture derived for one source slice.

    Exactly one of ``carried_cutoff_posture`` / ``residual`` is set:

    - ``carried_cutoff_posture``: an M1 carry of the slice's KNOWN
      ``cutoff_posture`` value, validated against the single-sourced
      ``CUTOFF_POSTURE_VALUES``. The SP-3 subpredicate clears only when this
      value is ``"pre_cutoff"``.
    - ``residual``: a named M3 residual when the producer did not assert a KNOWN
      cutoff posture. Never clears.

    ``clears_pre_cutoff`` is a stored field (not computed) so the record
    round-trips through YAML cleanly under ``extra="forbid"``; the validator
    binds it to ``True`` iff the carried value is ``"pre_cutoff"``.
    """

    slice_id: str
    carried_cutoff_posture: str | None = None
    residual: EcrTimingResidual | None = None
    clears_pre_cutoff: bool

    @model_validator(mode="after")
    def validate_posture(self) -> "EcrTimingPosture":
        has_carried = self.carried_cutoff_posture is not None
        has_residual = self.residual is not None
        if has_carried == has_residual:
            raise ValueError(
                "EcrTimingPosture requires exactly one of "
                "{carried_cutoff_posture, residual} to be set."
            )
        if has_carried and self.carried_cutoff_posture not in CUTOFF_POSTURE_VALUES:
            allowed = ", ".join(sorted(CUTOFF_POSTURE_VALUES))
            raise ValueError(
                f"carried_cutoff_posture must be one of {{{allowed}}} "
                f"(source_capture CUTOFF_POSTURE_VALUES, single-sourced); got "
                f"{self.carried_cutoff_posture!r}."
            )
        expected_clears = self.carried_cutoff_posture == "pre_cutoff"
        if self.clears_pre_cutoff != expected_clears:
            raise ValueError(
                "clears_pre_cutoff must be True iff carried_cutoff_posture == "
                f"'pre_cutoff'; got clears_pre_cutoff={self.clears_pre_cutoff} with "
                f"carried_cutoff_posture={self.carried_cutoff_posture!r}."
            )
        return self
