"""Tier-1 ideal-audience fusion: CE-invariant + counterfactual tests (Slice A).

Verifies the code-enforced invariants (CE3-CE12) the spec requires fusion to
guarantee, plus the three cheap counterfactual smoke tests from the route.
All synthetic evidence; no LLM, no network.
"""

from __future__ import annotations

import pytest
from pydantic import ValidationError

from schemas.audience_inference_models import (
    UNKNOWN_LABEL,
    EvidenceRecord,
    IdealAudienceProfile,
    ModalityFamily,
    OutputField,
    SupportBand,
)
from scoring.audience_fusion import MultipleCreatorsError, fuse_profile


def _ev(
    evidence_id: str = "E1",
    *,
    field: OutputField = OutputField.SEGMENT,
    modality: ModalityFamily = ModalityFamily.TEXT,
    label: str = "aspirational_beauty",
    vote: float = 1.0,
    base: float = 1.0,
    conf: float = 1.0,
    authored: bool = True,
    negation: bool = False,
    cluster: str | None = None,
    pillar: str | None = None,
    creator: str = "c1",
    post: str = "p1",
    source: str = "caption:p1:span",
) -> EvidenceRecord:
    return EvidenceRecord(
        evidence_id=evidence_id,
        creator_id=creator,
        platform="instagram",
        post_id=post,
        pillar_label=pillar,
        signal_id="T1",
        modality=modality,
        target_field=field,
        label=label,
        vote=vote,
        base_reliability=base,
        extractor_confidence=conf,
        creator_authored=authored,
        possible_negation_or_irony=negation,
        creative_cluster_id=cluster,
        source_pointer=source,
    )


def _field(profile: IdealAudienceProfile, field: OutputField, pillar_idx: int = 0):
    pillar = profile.ideal_audience_profiles[pillar_idx]
    return next(fr for fr in pillar.field_results if fr.field == field)


# --- CE10: actual_audience is never estimated ------------------------------


def test_actual_audience_always_not_estimated() -> None:
    profile = fuse_profile([_ev()], generated_at="2026-06-23T00:00:00Z")
    assert profile.actual_audience == "not_estimated"


def test_schema_rejects_actual_audience_claim() -> None:
    with pytest.raises(ValidationError):
        IdealAudienceProfile(
            creator_id="c1",
            actual_audience="estimated",  # type: ignore[arg-type]
            fusion_config_version="0.1",
            generated_at="2026-06-23T00:00:00Z",
        )


# --- CE9: every evidence item must carry a source pointer ------------------


@pytest.mark.parametrize("bad", ["", "   "])
def test_ce9_source_pointer_required(bad: str) -> None:
    with pytest.raises(ValidationError):
        _ev(source=bad)


# --- CE6: abstention on thin or contested evidence -------------------------


def test_ce6_thin_evidence_abstains() -> None:
    profile = fuse_profile([_ev(base=0.5, conf=0.3)], generated_at="t")
    seg = _field(profile, OutputField.SEGMENT)
    assert seg.support_band == SupportBand.ABSTAIN
    assert seg.label == UNKNOWN_LABEL
    assert "default:segment" in profile.abstentions


def test_ce6_contested_margin_abstains() -> None:
    evidence = [
        _ev("EX", label="luxury_buyer", vote=1.0),
        _ev("EY", label="value_seeker", vote=1.0),
    ]
    profile = fuse_profile(evidence, generated_at="t")
    seg = _field(profile, OutputField.SEGMENT)
    assert seg.support_band == SupportBand.ABSTAIN
    assert seg.label == UNKNOWN_LABEL


# --- CE8: divergent pillars are not merged ---------------------------------


def test_ce8_pillars_not_merged() -> None:
    evidence = [
        _ev("EB", label="aspirational_beauty", pillar="consumer_beauty"),
        _ev("EP", label="professional_stylist", pillar="pro_education"),
    ]
    profile = fuse_profile(evidence, generated_at="t")
    assert len(profile.ideal_audience_profiles) == 2
    labels = {_field(profile, OutputField.SEGMENT, i).label for i in range(2)}
    assert labels == {"aspirational_beauty", "professional_stylist"}


# --- CE12: a decided field carries its evidence ids ------------------------


def test_ce12_decided_field_has_evidence_ids() -> None:
    profile = fuse_profile([_ev("E42", label="aspirational_beauty")], generated_at="t")
    seg = _field(profile, OutputField.SEGMENT)
    assert seg.label == "aspirational_beauty"
    assert seg.evidence_ids == ["E42"]


# --- CE3: aggregate comments cannot drive a field ---------------------------


def test_ce3_comment_only_abstains() -> None:
    profile = fuse_profile(
        [_ev(modality=ModalityFamily.COMMENT, vote=1.0)], generated_at="t"
    )
    seg = _field(profile, OutputField.SEGMENT)
    assert seg.support_band == SupportBand.ABSTAIN


# --- CE5: one modality family cannot dominate beyond its cap ---------------


def test_ce5_single_modality_capped() -> None:
    evidence = [_ev(f"E{i}", label="aspirational_beauty") for i in range(5)]
    profile = fuse_profile(evidence, generated_at="t")
    seg = _field(profile, OutputField.SEGMENT)
    # Five strong text votes still cannot reach HIGH alone (text cap binds).
    assert seg.support_band == SupportBand.LOW
    assert seg.label == "aspirational_beauty"


# --- CE4: creator-authored outweighs implicit -----------------------------


def test_ce4_creator_authored_outweighs_implicit() -> None:
    evidence = [
        _ev("EA", label="authored_target", vote=0.25, authored=True),
        _ev("EB", label="implicit_target", vote=0.25, authored=False),
    ]
    profile = fuse_profile(evidence, generated_at="t")
    seg = _field(profile, OutputField.SEGMENT)
    assert seg.label == "authored_target"


# --- Counterfactual smoke tests -------------------------------------------


def test_counterfactual_flip_segment_signal() -> None:
    a = fuse_profile([_ev(label="aspirational_beauty")], generated_at="t")
    b = fuse_profile([_ev(label="performance_fitness")], generated_at="t")
    assert _field(a, OutputField.SEGMENT).label == "aspirational_beauty"
    assert _field(b, OutputField.SEGMENT).label == "performance_fitness"


def test_counterfactual_strip_cta_purchase_intent_abstains() -> None:
    # Only a segment signal; nothing votes purchase_intent -> it abstains.
    profile = fuse_profile([_ev(field=OutputField.SEGMENT)], generated_at="t")
    intent = _field(profile, OutputField.PURCHASE_INTENT)
    assert intent.support_band == SupportBand.ABSTAIN
    assert "default:purchase_intent" in profile.abstentions


def test_counterfactual_oneoff_campaign_does_not_flip() -> None:
    established = [
        _ev("A1", label="aspirational_beauty", modality=ModalityFamily.TEXT),
        _ev("A2", label="aspirational_beauty", modality=ModalityFamily.STRUCTURAL),
    ]
    oneoff = [
        _ev(f"B{i}", label="budget_shopper", modality=ModalityFamily.COMMERCIAL, cluster="camp1")
        for i in range(3)
    ]
    profile = fuse_profile(established + oneoff, generated_at="t")
    seg = _field(profile, OutputField.SEGMENT)
    assert seg.label == "aspirational_beauty"


# --- Guards ----------------------------------------------------------------


def test_multiple_creators_rejected() -> None:
    with pytest.raises(MultipleCreatorsError):
        fuse_profile([_ev("E1", creator="c1"), _ev("E2", creator="c2")], generated_at="t")


def test_empty_evidence_rejected() -> None:
    with pytest.raises(ValueError):
        fuse_profile([], generated_at="t")
