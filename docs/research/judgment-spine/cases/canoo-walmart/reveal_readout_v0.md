# Canoo/Walmart Reveal Readout v0

```yaml
retrieval_header_version: 1
artifact_role: Research artifact
scope: Post-reveal qualitative readout comparing sealed Canoo/Walmart judgments against the facilitator ledger.
use_when:
  - Reading the first post-reveal comparison after blind and owner-assisted judgments were sealed.
  - Preparing outcome calibration without treating this readout as a score.
  - Checking what the actual public action and later supplier outcome imply under claim discipline.
authority_boundary: retrieval_only
open_next:
  - docs/research/judgment-spine/cases/canoo-walmart/pre_reveal_judgment_comparison_v0.md
  - docs/research/judgment-spine/cases/canoo-walmart/facilitator_ledger_v0.md
  - docs/research/judgment-spine/cases/canoo-walmart/outcome_calibration_v0.md
input_hashes:
  participant_packet_v0.md: E0191512B1A5AD292C023304321B6FD870B4C1CF591DDFF8708ACC69D5B3324F
  blind_judgments_v0.md: 2DF41433DCFACB31832CD51E65EC424888B7EB8955115D6949A35E8C7F2E8225
  owner_context_judgments_v0.md: A12BDC0416FC41502AB0B46B70338FF40FF118008D5D808C5E91BDD265E3B2E8
  pre_reveal_judgment_comparison_v0.md: 2AD850D94A29438D54491AA5EE72D8D79332E04F6C78E03BF960CF28BEEAEE80
  facilitator_ledger_v0.md: 6356C45D8E9B75732DB3D146EABFFCE4AD2775BCDD23D0205E26A46222FCE739
stale_if:
  - The facilitator ledger changes.
  - Either sealed judgment artifact changes.
  - Outcome calibration is created and supersedes this qualitative-only readout for scoring or lesson extraction.
```

## Preflight

```yaml
orca_start_preflight:
  agents_read: yes
  overlay_read: yes
  source_pack: S0 plus pre-reveal comparison and facilitator ledger
  edit_permission: docs-write
  target_scope: Create first post-reveal readout while preserving score and outcome-calibration boundaries.
  dirty_state_checked: yes
  blocked_if_missing: no
```

## Readout Status

```yaml
reveal_readout_status: created_qualitative_only
facilitator_ledger_status: consumed_for_reveal
blind_judgment_status: sealed_before_reveal
owner_context_judgment_status: sealed_before_reveal
outcome_calibration_status: not_created
score_status: not_scored
judgment_quality_claim: not_proven
participant_visibility: prohibited
```

This readout is facilitator-side spoiler material. It may compare sealed judgments to actual public action and later supplier outcome, but it must not be reused as participant input, a fixture score, validation, or model-quality proof.

## Reveal Facts

The facilitator ledger reveals two distinct fact layers:

1. Actual action: Walmart publicly announced a definitive agreement to purchase 4,500 Canoo electric delivery vehicles, with an option to purchase up to 10,000 units.
2. Later supplier outcome: Canoo later announced a voluntary Chapter 7 bankruptcy filing and said it would cease operations effective immediately.

The agreement also contained protective and strategic terms: acceptance and performance criteria, a five-year term unless earlier terminated, pricing caps for the first 10,000 Walmart EVs, Walmart termination rights, Amazon-related exclusivity restrictions, and a warrant issued to Walmart.

This readout does not establish actual Walmart fleet deployment volume, unit acceptance volume, route uptime, operational losses, operational gains, or delivered-unit economics.

## Core Contrast

The case has a sharp split between action alignment and outcome alignment.

Actual action favored a substantial commitment with option and protection. Later outcome favored extreme caution about supplier solvency and production execution.

That means a naive reveal would be misleading. "Walmart did the deal" is not proof that commitment was right. "Canoo failed" is not by itself proof that every protected pilot would have been wrong. The usable learning is narrower: which judgment better separated strategic EV option value from supplier-dependence risk before the reveal?

## Judgment Readout

| Judgment lane | Sealed recommendation | Action-level readout | Outcome-level readout | Discipline note |
| --- | --- | --- | --- | --- |
| Blind LLM contestant | Hybrid: create an option-heavy staged conditional commitment, beginning with a narrow operational pilot; no broader commercial commitment now. | Partially aligned on structure, not scale. The actual agreement did use option/protection logic, but it was far larger and more public than a narrow pilot. | Directionally aligned on supplier-risk concern. The judgment named funding/runway risk, production proof, and uptime/service as conditions; Canoo's later Chapter 7 filing makes those concerns central. | Stronger than a simple proceed recommendation because it resisted broad dependence, but still needs calibration on whether even a narrow pilot-option structure accepted too much counterparty exposure. |
| Owner-assisted judgment | Do not proceed now; monitor demand, policy, materials/imports, tax benefits, and other external EV-support signals for possible later reconsideration. | Not aligned with the actual action, because Walmart did proceed with a substantial definitive agreement. | Directionally aligned with the later supplier failure. The high-risk/no-proceed posture fits the terminal counterparty outcome better than a commitment posture. | Strong risk call, but less transactional detail. Calibration should not over-reward it unless the scoring frame values avoiding supplier exposure over preserving EV option value. |

## First-Pass Interpretation

The blind LLM contestant appears better at naming a structured-deal shape: optionality, milestones, non-exclusivity, route pilot proof, financing thresholds, delivery remedies, safety, service, uptime, and charging fit.

The owner-assisted judgment appears better at the top-level risk posture if the target question is "should the buyer expose itself to this supplier now?" Canoo's later liquidation makes the owner-assisted caution directionally compelling.

The actual Walmart agreement sits between those positions. It was not pure deferment, and it was not a naive full-send purchase. It was a substantial public commitment wrapped in option, acceptance, termination, and warrant terms.

## Calibration Questions

Outcome calibration should answer these before any score or lesson is promoted:

- Is the benchmark the actual retailer action, the later supplier outcome, or a combined decision-quality frame?
- Should a protected pilot-option answer be rewarded for preserving strategic upside or penalized for accepting exposure to a supplier that later liquidated?
- Should the owner-assisted no-proceed answer be rewarded for avoiding terminal supplier risk even though it missed the actual action and gave fewer deal-design specifics?
- How much should Walmart's apparent contractual protections reduce the penalty for proceeding?
- Does the missing Walmart-specific deployment record block any claim about operational harm or benefit?

## Non-Claims

- No outcome calibration.
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
- TR/Casetext remains quarantined Step A plumbing only.

## Next Authorized Step

Create `docs/research/judgment-spine/cases/canoo-walmart/outcome_calibration_v0.md` only after choosing whether the calibration frame scores actual-action alignment, later-outcome alignment, or combined decision-quality alignment.

Required boundary: plumbing works only; not judgment quality
