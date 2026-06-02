# Participant Packet v0: Last-Mile EV Fleet Supplier Commitment

```yaml
retrieval_header_version: 1
artifact_role: Research artifact
scope: Anonymized zero-spoiler participant packet for a last-mile EV fleet supplier commitment decision.
use_when:
  - Capturing a blind judgment before any reveal, facilitator ledger, or outcome calibration.
  - Testing whether a participant can reason from pre-decision public evidence without source locator leakage.
  - Preserving the Step A plumbing-only boundary while moving into judgment-quality case work.
authority_boundary: retrieval_only
input_hashes:
  pre_cutoff_source_packet: 6E2BC0894A36C08B0712C8FE045DF812D3A8857E525CA4412832866FF405E473
  safety_receipt: 284CB7EE77AF1D9F2325317528DC0E1404AD2978AE99B10D8FBB3722BE5B9A67
  adversarial_review_report: B1FF4E08EA2449836946D323F5DCFE13479F1F708095437A5256C7D324A7CE99
stale_if:
  - The pre-cutoff source packet changes.
  - The safety receipt changes.
  - A later review finds participant-facing leakage or over-priming.
  - A blind judgment is captured after reveal material has been shown.
```

## Internal Handling Receipt

```yaml
orca_start_preflight:
  agents_read: yes
  overlay_read: yes
  source_pack: custom S1 plus pre-cutoff source packet, safety receipt, adversarial review report, and product-proof zero-spoiler rules
  edit_permission: docs-write
  target_scope: Create an anonymized participant packet after adversarial review accepted source-packet use with friction.
  dirty_state_checked: yes
  blocked_if_missing: no
```

```yaml
participant_packet_status: candidate_for_blind_judgment_capture
source_boundary: pre-decision public evidence only
blind_judgment_status: not_sealed
facilitator_ledger_status: not_created
harness_status: not_admitted
review_consumed:
  recommendation: accept_with_friction
  major_items_addressed:
    - AR-01: Balanced prose weight across retailer demand, supplier promise, supplier risk, alternatives, and decision structure.
    - AR-02: Optional independent financial-risk media source excluded from participant-facing content.
  hygiene_items_addressed:
    - AR-03: Alternative-supplier quantity generalized to a substantial reservation.
    - AR-04: Source manifest table, row structure, and source codes excluded.
    - AR-05: Official filing locator and company identifier excluded.
```

Handling rule: show the participant only the section between `Participant-Facing Packet Starts` and `Participant-Facing Packet Ends`. Do not show file paths, source locators, source tables, review notes, facilitator notes, case folders, or any reveal material.

## Participant-Facing Packet Starts

### Role

You are advising the leadership team of a large U.S. retailer in mid-2022. The retailer is deciding whether, when, and how strongly to commit to an early-stage electric delivery-vehicle supplier for last-mile operations.

Your job is to make the best decision from the facts available at this point. Do not search for the case, source material, company names, or later developments before answering.

### Decision Question

Should the retailer make a significant commitment to this early-stage electric delivery-vehicle supplier now?

Choose the strongest recommendation you can support:

- Hold or defer pending stronger production evidence.
- Run a narrow operational pilot.
- Make a staged conditional commitment tied to production, funding, and delivery milestones.
- Create an option-heavy commercial structure that preserves upside but limits dependence.
- Make a broader commercial commitment now.

You may also propose a hybrid structure if the facts support it.

### What You Know

The retailer has a real last-mile delivery problem to solve. It is scaling a home-delivery service several-fold, adding thousands of delivery drivers, and trying to use its store footprint, delivery density, and logistics network as a competitive advantage.

The retailer also has a long-term zero-emissions logistics ambition. Electric delivery vehicles fit the retailer's public operating direction, especially for shorter routes, dense delivery areas, and use cases where charging and dispatch patterns can be controlled. The retailer has some relevant charging and facilities infrastructure, but its own transportation framing favors pilots, use-case fit, and different vehicle answers for different operating needs.

The target supplier offers a differentiated EV platform and business-vehicle concept. Before this decision point, it reported vehicle testing, platform and battery development, facility progress, preorders, multiple U.S. operating locations, and spending plans tied to launch and production work. The supplier is more than a concept deck, but it has not proven volume production.

The supplier also has material counterparty risk. Its cash balance fell substantially over the most recent reporting period, and recent quarterly loss and operating cash use were each above $100 million. The supplier disclosed funding and runway uncertainty under accounting rules. Its ability to deliver depends on capital access, manufacturing execution, burn-rate control, and credible production milestones.

The retailer appears to have alternatives. Another commercial EV delivery-vehicle supplier with incumbent backing had already announced a substantial reservation with the same retailer and had early activity with a major logistics customer. That does not prove the alternative is better or sufficient for every route, but it means the decision is not simply "this supplier or no EV delivery fleet."

### Decision Tensions

- EV delivery demand is credible, but supplier selection is separable from the EV strategy.
- The target supplier has product and option value, but not proven volume execution.
- A retailer commitment could help secure supply, influence design, and create strategic upside, but it could also increase dependence on an undercapitalized supplier.
- A public or large commitment could improve the supplier's credibility, but it could also transfer reputational and execution risk to the retailer.
- Alternatives exist, but they may not satisfy every route, configuration, timing, or strategic-control need.
- The best answer may be a staged structure rather than a simple yes or no.

### Your Blind Judgment

Answer in this structure:

1. Recommendation: choose one of hold/defer, narrow pilot, staged conditional commitment, option-heavy structure, broader commitment, or hybrid.
2. Rationale: explain the three strongest reasons for your recommendation.
3. Conditions: name the production, funding, operating, legal, or commercial safeguards you would require.
4. Risk posture: state the biggest risk you are accepting and the biggest risk you are avoiding.
5. Disconfirming evidence: name the evidence that would most change your recommendation.
6. Confidence: low, medium, or high, with one sentence explaining why.

Seal your answer before seeing any reveal or facilitator material.

## Participant-Facing Packet Ends

## Internal Non-Claims

- No buyer validation.
- No willingness-to-pay proof.
- No repeatability proof.
- No product readiness.
- No feature readiness.
- No implementation readiness.
- No commercial readiness.
- No model-training readiness.
- No fine-tuning readiness.
- No sealed blind judgment.
- No facilitator ledger.
- No scoreable fixture.
- No Judgment Spine validation.
- No proof that Step A plumbing demonstrates judgment quality.

## Next Authorized Step

Capture the owner's or participant's blind judgment against only the participant-facing packet section, then write the sealed judgment artifact before any reveal, facilitator ledger, or outcome calibration.

Required boundary: plumbing works only; not judgment quality.
