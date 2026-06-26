"""Offline tests for the FusionConfig surface + the calibration sensitivity harness.

All synthetic, no LLM, no network. Two jobs: (1) pin the uncalibrated default constants and
prove the config is actually wired through fusion (not ignored), and (2) verify the harness's
sweep / boundary / corroboration mechanics and the documented current-default behaviours
(single-witness bar, irony floor, saturation) the memo relies on.
"""
from __future__ import annotations

from dataclasses import fields, replace
from math import atanh

import pytest

from schemas.product_mention_models import (
    Concentration,
    ProductMention,
    TranscriptSource,
    Verdict,
)
from scoring.product_fusion import (
    DEFAULT_FUSION_CONFIG,
    FusionConfig,
    fuse_product_verdicts,
)
from scoring.product_fusion_sensitivity import (
    SWEEPABLE_KNOBS,
    boundary_scan,
    corroboration_curve,
    min_clearing_raw,
    render_boundary_scan,
    render_corroboration_curve,
    render_knob_sweep,
    sweep_knob,
)


def _mention(
    stance: float,
    conf: float,
    *,
    authored: bool = False,
    negated: bool = False,
    mid: str = "m",
    vid: str = "v",
) -> ProductMention:
    return ProductMention(
        mention_id=mid,
        video_id=vid,
        transcript_anchor=f"asr:{vid}",
        transcript_source=TranscriptSource.ASR,
        brand="brand",
        line="line",
        concentration=Concentration.UNKNOWN,
        stance_vote=stance,
        source_pointer="x",
        start_ms=0,
        end_ms=1,
        creator_authored=authored,
        possible_negation_or_irony=negated,
        extractor_confidence=conf,
    )


def _verdict(mentions: list[ProductMention], config: FusionConfig):
    vs = fuse_product_verdicts(mentions, creator_id="c", generated_at="t", config=config)
    return vs.verdicts[0]


# --- config: defaults are pinned + actually wired ---------------------------


def test_default_config_values_are_the_documented_constants() -> None:
    c = DEFAULT_FUSION_CONFIG
    assert (
        c.gain,
        c.material_min,
        c.creator_authored_mult,
        c.implicit_mult,
        c.negation_mult,
        c.dependence_exponent,
    ) == (2.0, 0.40, 1.0, 0.6, 0.3, 0.5)


def test_config_is_wired_not_ignored() -> None:
    # Same borderline mention (score ~0.345); only the abstain floor differs -> verdict flips.
    m = [_mention(0.5, 0.6, authored=False)]
    low = _verdict(m, replace(DEFAULT_FUSION_CONFIG, material_min=0.3))
    high = _verdict(m, replace(DEFAULT_FUSION_CONFIG, material_min=0.5))
    assert low.verdict == Verdict.POSITIVE
    assert high.verdict == Verdict.UNKNOWN
    assert low.uncalibrated_support_score == high.uncalibrated_support_score


def test_sweepable_knobs_match_config_fields() -> None:
    # If a knob is added to FusionConfig, the harness must sweep it too (keeps coverage complete).
    assert set(SWEEPABLE_KNOBS) == {f.name for f in fields(FusionConfig)}


# --- harness scalars + guards ----------------------------------------------


def test_min_clearing_raw_default_and_edges() -> None:
    assert min_clearing_raw() == pytest.approx(atanh(0.4) / 2.0)
    assert min_clearing_raw(replace(DEFAULT_FUSION_CONFIG, material_min=1.0)) == float("inf")
    assert min_clearing_raw(replace(DEFAULT_FUSION_CONFIG, material_min=0.0)) == 0.0


def test_sweep_knob_rejects_unknown_knob() -> None:
    with pytest.raises(ValueError):
        sweep_knob([_mention(1.0, 1.0, authored=True)], "not_a_knob", (0.1,))


def test_boundary_scan_rejects_unknown_archetype() -> None:
    with pytest.raises(ValueError):
        boundary_scan(archetype="nope")


def test_sweep_knob_is_deterministic_and_ordered() -> None:
    m = [_mention(1.0, 1.0, authored=True)]
    a = sweep_knob(m, "gain", (1.0, 2.0, 3.0))
    b = sweep_knob(m, "gain", (1.0, 2.0, 3.0))
    assert [p.value for p in a] == [1.0, 2.0, 3.0]
    assert a == b


# --- documented current-default behaviours (the memo's findings) -----------


def test_material_min_sweep_flips_at_default_floor() -> None:
    points = sweep_knob([_mention(0.5, 0.6, authored=False)], "material_min", (0.3, 0.4))
    by_value = {p.value: p.verdict for p in points}
    assert by_value[0.3] == Verdict.POSITIVE
    assert by_value[0.4] == Verdict.UNKNOWN


def test_single_authored_witness_decides_a_verdict() -> None:
    # Finding: one authored mention above the single-witness bar already decides a verdict.
    decides = boundary_scan(archetype="authored", stances=(0.3,), confidences=(1.0,))[0]
    abstains = boundary_scan(archetype="authored", stances=(0.2,), confidences=(1.0,))[0]
    assert decides.verdict == Verdict.POSITIVE
    assert abstains.verdict == Verdict.UNKNOWN


def test_irony_flag_alone_does_not_abstain_a_max_mention() -> None:
    # Finding: at negation_mult 0.3 the irony flag alone does NOT pull a max-stance/-confidence
    # mention below the floor; abstention still depends on the extractor lowering stance/conf.
    max_corner = boundary_scan(archetype="authored+irony", stances=(1.0,), confidences=(1.0,))[0]
    weaker = boundary_scan(archetype="authored+irony", stances=(1.0,), confidences=(0.7,))[0]
    assert max_corner.verdict == Verdict.POSITIVE
    assert weaker.verdict == Verdict.UNKNOWN


def test_corroboration_curve_saturates() -> None:
    # Finding: past the first strong mention the squashed score barely rises (near-binary).
    points = corroboration_curve((1, 2, 3, 5))
    scores = [p.support_score for p in points]
    assert scores[1] > scores[0]
    assert scores == sorted(scores)
    assert scores[2] == pytest.approx(scores[3], abs=1e-6)
    assert all(p.verdict == Verdict.POSITIVE for p in points)


# --- render helpers ---------------------------------------------------------


def test_render_helpers_produce_tables_and_handle_empty() -> None:
    ks = render_knob_sweep(sweep_knob([_mention(1.0, 1.0, authored=True)], "gain", (2.0,)))
    assert "gain" in ks and "verdict" in ks
    bs = render_boundary_scan(boundary_scan(archetype="authored", stances=(1.0,), confidences=(1.0,)))
    assert "authored" in bs and "conf 1" in bs
    cc = render_corroboration_curve(corroboration_curve((1, 2)))
    assert "mentions" in cc and "support" in cc
    assert render_knob_sweep([]) == "(empty sweep)"
    assert render_boundary_scan([]) == "(empty scan)"
    assert render_corroboration_curve([]) == "(empty curve)"
