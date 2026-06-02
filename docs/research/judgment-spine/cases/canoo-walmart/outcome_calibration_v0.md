# Canoo/Walmart Outcome Calibration v0

```yaml
retrieval_header_version: 1
artifact_role: Research artifact
scope: Outcome calibration for the Canoo/Walmart case track after sealed judgments, facilitator ledger, reveal readout, and calibration-gate adversarial review.
use_when:
  - Reading the calibrated case learning after reveal.
  - Checking how the blind LLM and owner-assisted judgments compare without turning the case into validation.
  - Preserving the calibration frame before any later fixture, scoring, or lesson-promotion work.
authority_boundary: retrieval_only
open_next:
  - docs/research/judgment-spine/cases/canoo-walmart/case_index.md
  - docs/review-outputs/adversarial-artifact-reviews/canoo_walmart_reveal_readout_calibration_gate_adversarial_artifact_review_v0.md
  - docs/research/judgment-spine/cases/canoo-walmart/reveal_readout_v0.md
input_hashes:
  participant_packet_v0.md: E0191512B1A5AD292C023304321B6FD870B4C1CF591DDFF8708ACC69D5B3324F
  blind_judgments_v0.md: 2DF41433DCFACB31832CD51E65EC424888B7EB8955115D6949A35E8C7F2E8225
  owner_context_judgments_v0.md: A12BDC0416FC41502AB0B46B70338FF40FF118008D5D808C5E91BDD265E3B2E8
  pre_reveal_judgment_comparison_v0.md: 2AD850D94A29438D54491AA5EE72D8D79332E04F6C78E03BF960CF28BEEAEE80
  facilitator_ledger_v0.md: 6356C45D8E9B75732DB3D146EABFFCE4AD2775BCDD23D0205E26A46222FCE739
  reveal_readout_v0.md: 927DB2F16D3D9DF9EBB9DF20F6A35F00659C7C671EEC8ADAF4104BD7535C3A7E
  calibration_gate_adversarial_review_v0.md: 31362147A8557C0698A23A9D902AA5FFC71D8B973813F89DF9157D38ED0980EE
stale_if:
  - Any input hash changes.
  - New public evidence establishes Walmart delivery performance, unit acceptance volume, termination-right exercise, financial exposure at bankruptcy, or operational harm/gain.
  - A later scoreable fixture, rubric, or model-run artifact supersedes this qualitative calibration.
```

## Preflight

```yaml
orca_start_preflight:
  agents_read: yes
  overlay_read: yes
  source_pack: S4 explicitly named case artifacts plus calibration-gate adversarial review
  edit_permission: docs-write
  target_scope: Create qualitative outcome calibration without scoring, validation, or judgment-quality proof claims.
  dirty_state_checked: yes
  blocked_if_missing: no
```

## Calibration Status

```yaml
outcome_calibration_status: created_qualitative_only
calibration_frame: combined_decision_quality_alignment
calibration_axes:
  - actual_action_alignment
  - later_outcome_alignment
  - decision_quality_under_uncertainty
score_status: not_scored
winner_status: no_single_winner
judgment_quality_claim: not_proven
participant_visibility: prohibited
```

## Frame Selection

This calibration uses `combined_decision_quality_alignment`.

The frame is selected before applying the reveal readout's interpretive sections as calibration evidence. The reveal readout is treated as a source to check, not as authority for the calibration question.

The calibration does not ask only "who matched Walmart's actual action?" and does not ask only "who matched Canoo's later failure?" Either single-axis frame would overclaim. The usable decision-quality question is:

> Which sealed judgment gave the better pre-reveal decision stance under uncertainty, separating strategic EV option value from supplier-dependence risk while preserving claim discipline?

The answer is axis-split, not a single winner.

## Review Friction Applied

The calibration-gate adversarial review returned `accept_with_friction`. This artifact carries that friction forward as constraints:

| Review finding | Calibration handling |
| --- | --- |
| AR-01: Calibration-frame pre-selection | The calibration frame is declared here before using the readout's Core Contrast as evidence. |
| AR-02: Asymmetric contrast-hook burden | Both judgment lanes are evaluated under the same evidentiary rule: directional support is not proof, and structural resemblance is not score. |
| AR-03: Conditional vs. unconditional advantage | Both lane advantages are conditional on the selected calibration axis. |
| AR-04: Pricing-cap source anchoring gap | The pricing-cap term is not used as decisive calibration evidence unless later source-anchored. |
| AR-05: Unflagged operational evidence gaps | This calibration explicitly treats Walmart termination-right exercise and financial exposure at bankruptcy as unestablished. |
| AR-06: Stale pre-reveal status fields | Current inventory comes from `case_index.md`, not from creation-time status fields in the pre-reveal artifact. |

## Established Reveal Inputs

The established reveal inputs are narrow:

- Walmart publicly announced a definitive agreement to purchase 4,500 Canoo electric delivery vehicles, with an option to purchase up to 10,000 units.
- Canoo's Form 8-K described acceptance and performance criteria, termination rights, Amazon-related restrictions, and a warrant issued to Walmart.
- Canoo later announced a voluntary Chapter 7 bankruptcy filing and immediate cessation of operations.

The following remain unestablished in the reviewed artifacts:

- Walmart fleet deployment volume.
- Walmart unit acceptance volume.
- Route uptime or route-level performance.
- Operational harm, operational gain, or delivered-unit economics.
- Whether Walmart exercised termination rights.
- Whether Walmart had deposits, prepayments, or other financial exposure outstanding at bankruptcy.
- Whether the actual protective terms worked in practice.

## Axis Calibration

| Axis | Blind LLM contestant | Owner-assisted judgment | Calibration read |
| --- | --- | --- | --- |
| Actual-action alignment | Partial. It recommended a narrow protected pilot/option structure, not the larger 4,500-vehicle public commitment. It did, however, name optionality, milestones, non-exclusivity, deposits, publicity control, production proof, delivery remedies, uptime/service, charging fit, and route pilot evidence. | Low. It recommended not proceeding now and waiting for external EV-support signals, while Walmart did proceed with a substantial definitive agreement. | The blind LLM is closer to the actual deal shape, but not to the scale. This is action-alignment only, not proof of better judgment. |
| Later-outcome alignment | Partial. It identified funding/runway, production proof, and uptime/service as major conditions. It still preserved an engagement path whose protective effectiveness is not established in the reviewed evidence. | Stronger at top-level risk posture. It judged supplier risk too high and preferred no proceed unless conditions changed; Canoo's later Chapter 7 outcome supports the supplier-risk concern. | The owner-assisted judgment is closer to the later supplier-risk outcome. This is outcome-alignment only, not a complete decision-quality score. |
| Decision quality under uncertainty | Strong on transaction design and disconfirming-evidence discipline. Weakness: it may preserve too much exposure if the buyer can avoid the supplier entirely and alternatives exist. | Strong on avoiding existential counterparty exposure. Weakness: it gives less detailed deal design, diligence conditions, and option-preservation structure. | The case calibrates to a split lesson: engagement design and exposure avoidance are distinct capabilities. Neither lane alone proves judgment quality. |

## Calibration Result

```yaml
blind_llm_calibration: partially_supported_on_structure_and_conditions_not_vindicated
owner_assisted_calibration: directionally_supported_on_supplier_risk_not_scoreable_proof
case_learning: split_axis_learning
single_winner: no
judgment_spine_validation: not_proven
```

The blind LLM contestant was useful because it converted uncertainty into a staged, option-heavy, condition-rich operating answer. It was not vindicated, because the later supplier outcome makes any engagement path suspect unless protective terms demonstrably prevented harm, and that evidence is absent.

The owner-assisted judgment was useful because it made the supplier-dependence risk central and avoided exposure to a counterparty that later liquidated. It was not a complete calibration winner, because it did not match the actual action and provided less transactional specificity for a buyer that still wanted to preserve EV option value.

The best calibrated lesson is not "the LLM won" or "the owner won." The lesson is that this case separates two dimensions:

- When the buyer's strategic option value requires engagement, the blind LLM's safeguard discipline is the stronger working form.
- When the buyer can avoid exposure to the supplier, the owner-assisted no-proceed posture is better aligned with the later terminal counterparty outcome.

## Method Learning

This case is useful because it forced the Judgment Spine to distinguish action alignment from outcome alignment. A retailer's actual commitment does not prove that commitment was the right call, and the supplier's later failure does not prove every protected engagement path was wrong.

For future case tracks, preserve these requirements:

- Capture the calibration frame before using a reveal readout's interpretive sections.
- Track actual-action alignment and later-outcome alignment separately.
- Require evidence that protective terms worked before crediting them as successful risk control.
- Do not treat more detailed deal design as better judgment when the stronger answer may be no exposure.
- Do not treat no-proceed as better judgment when the decision context requires option preservation.

## Non-Claims

- No fixture score.
- No model run.
- No buyer validation.
- No willingness-to-pay proof.
- No repeatability proof.
- No product readiness.
- No feature readiness.
- No implementation readiness.
- No commercial readiness.
- No model-training readiness.
- No Judgment Spine validation.
- No proof that Step A plumbing demonstrates judgment quality.
- No proof that TR/Casetext plumbing demonstrates judgment quality.
- No proof that the blind LLM judgment was independently clean.
- No proof that the owner-assisted judgment was a clean blind judgment.

## Next Authorized Step

Use this artifact as a qualitative case-learning input only. If the owner wants the case to become a scoreable v0.14 fixture, run a separate fixture-admission or scoring-readiness route that starts from the calibration frame and explicitly handles the missing Walmart-specific operational evidence.

Required boundary: plumbing works only; not judgment quality
