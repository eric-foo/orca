# Canoo/Walmart Facilitator Ledger v0

```yaml
retrieval_header_version: 1
artifact_role: Research artifact
scope: Sealed facilitator-only ledger of actual public action, agreement terms, and post-window outcome evidence for the Canoo/Walmart case track.
use_when:
  - Creating a reveal readout after blind and owner-assisted judgments are sealed.
  - Checking actual-action and outcome source boundaries without exposing participant-facing material.
  - Preserving source provenance for Judgment Spine case learning.
authority_boundary: retrieval_only
open_next:
  - docs/research/judgment-spine/cases/canoo-walmart/pre_reveal_judgment_comparison_v0.md
  - docs/research/judgment-spine/cases/canoo-walmart/reveal_readout_v0.md
  - docs/research/judgment-spine/cases/canoo-walmart/outcome_calibration_v0.md
input_hashes:
  participant_packet_v0.md: E0191512B1A5AD292C023304321B6FD870B4C1CF591DDFF8708ACC69D5B3324F
  blind_judgments_v0.md: 2DF41433DCFACB31832CD51E65EC424888B7EB8955115D6949A35E8C7F2E8225
  owner_context_judgments_v0.md: A12BDC0416FC41502AB0B46B70338FF40FF118008D5D808C5E91BDD265E3B2E8
  pre_reveal_judgment_comparison_v0.md: 2AD850D94A29438D54491AA5EE72D8D79332E04F6C78E03BF960CF28BEEAEE80
stale_if:
  - New public action or outcome source materially changes the ledger.
  - Reveal readout or outcome calibration is created from sources not listed here.
  - Later source review finds a cited source unavailable, misdated, or materially misstated.
```

## Preflight

```yaml
orca_start_preflight:
  agents_read: yes
  overlay_read: yes
  source_pack: S0 plus sealed Canoo/Walmart judgment artifacts, pre-reveal comparison, and facilitator-only public actual-action and outcome source unit
  edit_permission: docs-write
  target_scope: Create facilitator-only ledger after blind and owner-assisted judgments were sealed.
  dirty_state_checked: yes
  blocked_if_missing: no
```

## Ledger Status

```yaml
facilitator_ledger_status: created_facilitator_only
participant_visibility: prohibited
blind_judgment_status: sealed_before_ledger
owner_context_judgment_status: sealed_before_ledger
pre_reveal_comparison_status: sealed_before_ledger
reveal_readout_status: not_created
outcome_calibration_status: not_created
judgment_quality_claim: not_proven
```

This artifact is spoiler material. Do not use any title, URL, quote, fact, agreement term, action record, implementation status, outcome fact, or inference from this ledger in participant-facing packets, prompts, summaries, or source lists.

## Source Ledger

| ID | Source | Date | Role | Ledger facts |
| --- | --- | --- | --- | --- |
| F-01 | Walmart corporate announcement: `https://corporate.walmart.com/news/2022/07/12/walmart-to-purchase-4-500-canoo-electric-delivery-vehicles-to-be-used-for-last-mile-deliveries-in-support-of-its-growing-ecommerce-business` | 2022-07-12 | Actual public action record | Walmart announced a definitive agreement to purchase 4,500 Canoo all-electric delivery vehicles, with an option to purchase up to 10,000 units; LDVs were expected to begin hitting the road in 2023, with advanced deliveries planned in Dallas-Fort Worth in the following weeks. |
| F-02 | Canoo Form 8-K: `https://www.sec.gov/Archives/edgar/data/1750153/000121390022038925/ea162764-8k_canooinc.htm` | 2022-07-12, reporting 2022-07-11 event | Definitive agreement and securities terms | Canoo Sales, LLC entered an EV Fleet Purchase Agreement with Walmart. Walmart agreed, subject to acceptance and performance criteria, to purchase at least 4,500 EVs, with an option to purchase up to an additional 5,500 EVs. The agreement had a five-year term unless earlier terminated, included Amazon-related exclusivity restrictions, acceptance criteria, termination rights, and a warrant for 61,160,011 Canoo common shares at $2.15 per share. |
| F-03 | Canoo Chapter 7 announcement: `https://www.globenewswire.com/news-release/2025/01/18/3011752/0/en/canoo-inc-announces-chapter-7-bankruptcy-filing.html` | 2025-01-17 | Post-window outcome source | Canoo announced a voluntary Chapter 7 bankruptcy filing, said a trustee would oversee liquidation, said it had agreements with Walmart and others, and stated that it would cease operations effective immediately. |

## Actual Action

The actual public action was a substantial retailer commitment to Canoo, not a pure deferment. Walmart publicly announced a definitive agreement to purchase 4,500 Canoo electric delivery vehicles with an option to purchase up to 10,000 units. Canoo's Form 8-K described the agreement as subject to acceptance and performance criteria and tied it to detailed commercial and securities terms.

This ledger does not establish actual Walmart fleet deployment volume, operational uptime, customer-route performance, or delivered-unit economics.

## Agreement And Risk Terms

The agreement combined commitment, optionality, and protection:

- minimum purchase agreement for at least 4,500 EVs, subject to acceptance and performance criteria;
- option to purchase up to an additional 5,500 EVs;
- five-year term unless earlier terminated;
- capped pricing for the first 10,000 Walmart EVs;
- acceptance criteria including reliability, warranties, vehicle design and components, delivery timeline, and ordering/process terms;
- Walmart termination rights for acceptance-criteria failures, convenience termination of the agreement on at least 30 days' written notice, and breach-related termination rights;
- Canoo restriction during the agreement term against specified Amazon-related EV sale, service, securities, or control-transfer arrangements;
- warrant issuance to Walmart for 61,160,011 Canoo common shares, with 15,290,003 shares immediately vested and the remainder tied to revenue from Walmart-related transactions until $300 million in net revenue.

## Outcome Context

Canoo later announced a voluntary Chapter 7 bankruptcy filing and immediate cessation of operations. This is terminal counterparty-risk evidence for the supplier, but it does not by itself establish every Walmart-specific operational consequence.

```yaml
walmart_delivery_performance: not_established_in_this_ledger
walmart_unit_acceptance_volume: not_established_in_this_ledger
retailer_operational_loss_or_gain: not_established_in_this_ledger
supplier_terminal_outcome: chapter_7_liquidation_announced
```

## Judgment Contrast Hooks

These hooks are for a later reveal readout. They are not the reveal readout and do not score either judgment.

| Judgment lane | Sealed position | Facilitator-side contrast hook |
| --- | --- | --- |
| Blind LLM contestant | Hybrid: narrow operational pilot plus option-heavy staged conditional commitment; no broader commercial commitment now. | Actual action moved beyond a narrow pilot into a definitive 4,500-vehicle purchase agreement with option and warrant structure. Some agreement terms resemble staged protection, but the scale and public commitment were materially larger than the blind recommendation. |
| Owner-assisted judgment | Do not proceed because risk is too high; monitor demand, policy, materials, imports, and tax-benefit signals for possible later reconsideration. | Canoo's later Chapter 7 liquidation is directionally relevant to the supplier-risk caution. It does not prove the owner-assisted judgment in a scoreable way until outcome calibration defines the comparison method and admissible evidence. |

## Non-Claims

- This ledger is not participant-facing.
- This ledger is not a reveal readout.
- This ledger is not outcome calibration.
- This ledger does not score the blind LLM contestant.
- This ledger does not score the owner-assisted judgment.
- This ledger does not prove Orca has judgment quality.
- This ledger does not prove Step A harness judgment quality.
- This ledger does not make Canoo/Walmart a scoreable v0.14 fixture.
- This ledger does not establish buyer validation, product readiness, commercial readiness, model-training readiness, or repeatability.
- TR/Casetext remains quarantined Step A plumbing only.

## Next Authorized Step

Create `docs/research/judgment-spine/cases/canoo-walmart/reveal_readout_v0.md` by comparing sealed judgments and the pre-reveal comparison against this facilitator ledger. Keep outcome calibration separate unless the next turn explicitly authorizes that artifact.

Required boundary: plumbing works only; not judgment quality
