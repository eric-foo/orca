"""Schemas for the IG creator-gender demographic signal (Pass 1 silver + Pass 2 fusion output).

A SOFT, confidence-weighted creator-gender LEAN — never a hard categorical label. Sibling to
product/audience inference (do NOT fold into product-stance). The agent-in-the-loop inference
that POPULATES `CreatorGenderSignal` (cleaning/ zone) and the gender x product-stance join are
DEFERRED; this file is the deterministic contract the no-LLM fusion (`scoring/creator_gender_fusion.py`)
consumes.

Minimization posture (owner-decided): store ONLY a signed soft lean + confidence + the cue + a
short verbatim basis + inferred provenance. There is deliberately NO categorical gender field, so
a hard label is UNREPRESENTABLE; no commenter gender is stored. Binary male-vs-female axis;
non-binary creators are an accepted residual handled by abstention (lean ~0 / low confidence),
never a forced label.

Scope/intent: docs/decisions/ig_creator_gender_demographic_signal_lane_scope_defer_v0.md.
"""

from __future__ import annotations

import math
from enum import StrEnum
from typing import Any, Mapping, Self

from pydantic import ConfigDict, Field, field_validator, model_validator

from schemas.case_models import StrictModel


class GenderCueKind(StrEnum):
    """How a per-reel gender lean was cued, so the fusion can weight cues by trust.

    `self_presentation` is the trusted, circularity-free spine (explicit first-person/self-
    reference). `product_marketed_gender` is a NOISY proxy held to a low weight: it risks
    circularity with the downstream gender x product-stance cut (inferring gender from the
    products reviewed, then cutting product-stance by gender) and cross-gender reviewing is common.
    """

    SELF_PRESENTATION = "self_presentation"
    PRODUCT_MARKETED_GENDER = "product_marketed_gender"


class CreatorGenderModel(StrictModel):
    """Strict base (mirrors ProductMentionModel): forbid extras, validate on assignment, and route
    unsafe construction back through validation so the soft-lean invariants cannot be skipped."""

    model_config = ConfigDict(extra="forbid", populate_by_name=True, validate_assignment=True)

    @classmethod
    def model_construct(cls, _fields_set: set[str] | None = None, **values: Any) -> Self:
        return cls.model_validate(values)

    def model_copy(self, *, update: Mapping[str, Any] | None = None, deep: bool = False) -> Self:
        data = self.model_dump(mode="python")
        if update:
            data.update(update)
        return type(self).model_validate(data)


class CreatorGenderSignal(CreatorGenderModel):
    """One per-reel creator-gender lean cue (Pass 1, silver).

    What the DEFERRED agent-in-the-loop cleaning inference will produce per reel. `gender_lean`
    is a signed SOFT lean in [-1, 1] (convention: negative = female-leaning, positive =
    male-leaning, ~0 = neutral / insufficient). There is NO categorical gender field, so a hard
    label is unrepresentable. `basis` is a short verbatim self-presentation (or product-mix) cue,
    kept for auditability; `provenance` marks the read inferred.
    """

    creator_id: str
    signal_id: str
    reel_ref: str
    gender_lean: float = Field(ge=-1.0, le=1.0)
    confidence: float = Field(ge=0.0, le=1.0)
    cue_kind: GenderCueKind
    basis: str
    provenance: dict = Field(default_factory=dict)

    @field_validator("creator_id", "signal_id", "reel_ref", "basis")
    @classmethod
    def _required_non_empty(cls, value: str) -> str:
        if not value or not value.strip():
            raise ValueError("field must be non-empty")
        return value

    @model_validator(mode="after")
    def _finite(self) -> Self:
        # NaN/Inf slip past pydantic ge/le (comparison-based); reject them so a non-finite lean or
        # confidence cannot persist (mirrors StatedRating / ProductMention finite discipline).
        if not (math.isfinite(self.gender_lean) and math.isfinite(self.confidence)):
            raise ValueError("gender_lean and confidence must be finite")
        return self


class CreatorGenderLean(CreatorGenderModel):
    """The fused creator-level gender lean (Pass 2 output) — deterministic, evidence-cited, SOFT.

    `gender_lean` is the signed soft lean in [-1, 1]; `confidence` is the squashed signal strength
    in [0, 1]. `abstained` True means the net signal was too weak/contested to call: `gender_lean`
    is reported 0.0 while `confidence` retains the sub-floor strength for audit. NO categorical
    label. UNCALIBRATED v0 (see `scoring/creator_gender_fusion.py`).
    """

    creator_id: str
    gender_lean: float = Field(ge=-1.0, le=1.0)
    confidence: float = Field(ge=0.0, le=1.0)
    abstained: bool
    evidence_ids: list[str] = Field(default_factory=list)
    fusion_config_version: str
    generated_at: str
    provenance: dict = Field(default_factory=dict)

    @field_validator("creator_id", "fusion_config_version", "generated_at")
    @classmethod
    def _required_non_empty(cls, value: str) -> str:
        if not value or not value.strip():
            raise ValueError("field must be non-empty")
        return value

    @model_validator(mode="after")
    def _finite(self) -> Self:
        if not (math.isfinite(self.gender_lean) and math.isfinite(self.confidence)):
            raise ValueError("gender_lean and confidence must be finite")
        return self
