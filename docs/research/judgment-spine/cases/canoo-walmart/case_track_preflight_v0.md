# Canoo Walmart Case Track Preflight v0

```yaml
retrieval_header_version: 1
artifact_role: Research artifact
scope: Zero-spoiler preflight for whether the Canoo/Walmart candidate can proceed as the next Judgment Spine case track.
use_when:
  - Deciding whether to build a clean pre-cutoff source packet or participant packet for Canoo/Walmart.
  - Checking source sufficiency and leakage boundaries before any blind judgment.
  - Preserving Step A plumbing-only claim discipline while starting the next case track.
authority_boundary: retrieval_only
open_next:
  - .agents/workflow-overlay/product-proof.md
  - docs/research/judgment-spine/README.md
  - docs/research/judgment-spine/harness/v0_14/judgement_case_construction_protocol.md
  - docs/research/judgment-spine/cases/canoo-walmart/case_index.md
stale_if:
  - A later owner decision changes the selected case, cutoff, or zero-spoiler policy.
  - A participant-facing packet is created from agreement-announcement, agreement-filing, post-cutoff, or outcome sources.
  - Step A plumbing-only boundaries are reopened or upgraded into judgment-quality claims.
```

## Preflight Receipt

```yaml
orca_start_preflight:
  agents_read: yes
  overlay_read: yes
  source_pack: custom S1 plus Judgment Spine parent, product-proof zero-spoiler rules, v0.14 case-construction protocol, Packing-to-Harness interface, and one public source-loading unit
  edit_permission: docs-write
  target_scope: Initialize Canoo/Walmart as the next docs-only Judgment Spine case track after owner accepted Step A as plumbing only.
  dirty_state_checked: yes
  blocked_if_missing: no
```

Repository state note: `git status --short --branch` showed `main...origin/main [ahead 19]`, modified Orca overlay and docs files, and many untracked docs plus `orca-harness/` before this file was written. This preflight may route the next case-track artifact, but dirty or untracked state does not prove acceptance, validation, readiness, source-of-truth promotion, implementation authorization, score-readiness, product proof, or judgment quality.

Owner boundary consumed: Step A is accepted only as plumbing. TR/Casetext remains quarantined plumbing-grade and cannot support a judgment-quality claim.

## Status

```yaml
case_track_status: initialized_preflight
recommendation: GO_TIER_0_CANDIDATE_WITH_SOURCE_PACKET_REQUIRED
source_packet_status: created_after_preflight
safety_receipt_status: created_after_preflight
participant_packet_status: blocked_pending_adversarial_review
blind_judgment_status: not_sealed
facilitator_ledger_status: not_created
harness_status: not_admitted
source_context_status: SOURCE_CONTEXT_READY_FOR_PREFLIGHT_ONLY
```

## Spoiler-Safe Case Identity

- candidate_label: Canoo/Walmart last-mile EV fleet commitment
- decision_family: strategic supplier selection, fleet electrification, startup counterparty risk, last-mile economics, exclusivity, and option-value discipline
- decision_owner_hypothesis: Walmart U.S. last-mile, innovation and automation, fleet/procurement, finance, sustainability, legal, and executive risk owners
- spoiler_state: preflight only; no blind judgment has been sealed
- participant-safe frame: a large retailer is evaluating whether, when, and how strongly to commit to a novel electric last-mile vehicle supplier as part of a fast-growing delivery strategy, balancing sustainability, delivery economics, operational fit, supplier maturity, capital/funding risk, delivery-timeline risk, competitive positioning, and option value.

Do not use agreement-announcement titles, agreement-filing titles, post-cutoff source titles, snippets, URLs, filenames, actual decision terms, later implementation facts, or outcome material in participant-facing packets.

## Candidate Decision Question

Should the retailer make a significant commitment to an early-stage electric delivery-vehicle supplier for last-mile operations now, and if so should the commitment be a narrow pilot, a staged conditional order, an option-heavy agreement, a broader commercial commitment, or a hold/defer pending stronger supplier-production evidence?

## Candidate Cutoff Options

Recommended cutoff: immediately before the July 2022 definitive agreement announcement. This appears to be the strongest blind-judgment setup because it tests the owner decision before the public action is known while still allowing source depth on the retailer's delivery strategy, fleet-electrification goals, supplier risks, production maturity, capital constraints, and alternative EV-fleet options.

Alternative cutoff A: before the retailer's early-2022 last-mile expansion and EV fleet planning became public. This is cleaner but likely too source-thin for a strong participant packet.

Alternative cutoff B: after the definitive agreement announcement but before delivery, production, or later outcome information. This should be avoided for first blind use unless the question is reframed as post-signature risk management, because the actual commitment decision would already be revealed.

Alternative cutoff C: any date after later implementation or outcome facts become public. This is facilitator-only calibration territory and must not be used for the blind decision packet.

## Clean Pre-Cutoff Source-Family Inventory

Participant-safe source families appear available for the recommended cutoff:

- retailer last-mile and delivery-service strategy before the agreement announcement;
- retailer sustainability and fleet-electrification goals before the agreement announcement;
- public supplier financial filings and earnings materials before the agreement announcement;
- supplier production, manufacturing, product-readiness, preorder, and commercialization claims available before the agreement announcement;
- independent pre-cutoff business and industry coverage of the supplier's cash, manufacturing, governance, and production-timing risks;
- independent pre-cutoff context on alternative electric delivery-vehicle suppliers and retailer fleet options;
- public economics or operating constraints for last-mile delivery sufficient to reason about fleet fit, delivery density, and operational option value.

Source families to exclude from participant-facing packets:

- the July 2022 agreement announcement;
- agreement filings, warrant terms, exclusivity terms, termination rights, or purchase-order details;
- post-cutoff company filings, press releases, articles, implementation facts, delivery facts, bankruptcy or liquidation facts, and outcome discussion;
- source titles, URLs, snippets, or filenames that leak the actual action or later outcome.

## Facilitator-Only Source Availability Status

The following statuses confirm availability only. They are not participant-facing content.

| Source class | Status | Participant use |
| --- | --- | --- |
| Clean pre-cutoff retailer delivery-strategy evidence | available | allowed after cutoff filtering and title/URL sanitization |
| Clean pre-cutoff supplier financial-risk evidence | available | allowed after cutoff filtering and title/URL sanitization |
| Clean pre-cutoff supplier production and vehicle-fit evidence | available | allowed after cutoff filtering and title/URL sanitization |
| Clean pre-cutoff alternative-supplier and EV-fleet context | available | allowed after cutoff filtering and title/URL sanitization |
| Actual public agreement/action records | available | sealed facilitator-only |
| Agreement terms and warrant/exclusivity filings | available | sealed facilitator-only |
| Independent post-window outcome evidence | available | sealed facilitator-only |
| Leakage-free participant source list | not yet built | must be created with safety receipt |

## Facilitator-Only Public Sources Opened

These links were opened to test source availability for this preflight. They are not a participant source list and must not be pasted into participant-facing material before a blind judgment is sealed.

| Source | Date | Preflight use |
| --- | --- | --- |
| Walmart corporate announcement on InHome expansion and electric delivery vans: `https://corporate.walmart.com/news/2022/01/05/walmart-to-expand-inhome-delivery-reaching-30-million-u-s-homes-in-2022` | 2022-01-05 | Pre-cutoff retailer delivery-strategy source family |
| Canoo Q1 2022 results release via PRNewswire: `https://www.prnewswire.com/news-releases/canoo-inc-announces-first-quarter-2022-results-301544386.html` | 2022-05-10 | Pre-cutoff supplier financial and production-risk source family |
| SEC filing detail page for Canoo Form 10-Q accession `0001628280-22-013637`: `https://www.sec.gov/Archives/edgar/data/1750153/000162828022013637/0001628280-22-013637-index.html` | 2022-05-10 | Official pre-cutoff financial filing availability |
| Walmart corporate announcement of the Canoo agreement: `https://corporate.walmart.com/news/2022/07/12/walmart-to-purchase-4-500-canoo-electric-delivery-vehicles-to-be-used-for-last-mile-deliveries-in-support-of-its-growing-ecommerce-business` | 2022-07-12 | Sealed actual-action source; not participant-facing for recommended cutoff |
| Canoo Form 8-K on the EV Fleet Purchase Agreement: `https://www.sec.gov/Archives/edgar/data/1750153/000121390022038925/ea162764-8k_canooinc.htm` | 2022-07-12 | Sealed agreement-terms source; not participant-facing for recommended cutoff |
| Canoo Chapter 7 bankruptcy filing announcement: `https://www.globenewswire.com/news-release/2025/01/18/3011752/0/en/canoo-inc-announces-chapter-7-bankruptcy-filing.html` | 2025-01-17 | Sealed post-window outcome source availability |

## Learnability Tier Assessment

classification: `GO_TIER_0_CANDIDATE_WITH_SOURCE_PACKET_REQUIRED`

Rationale: the case appears to have a real decision owner, a clean pre-announcement cutoff, material tradeoffs, visible pre-cutoff public evidence, startup counterparty risk, operational/economic stakes, alternative supplier context, and sealed actual-action and outcome sources for later calibration. It is not Tier 0-ready until a clean pre-cutoff source packet, participant packet, safety receipt, and sealed blind judgment exist.

## Source Sufficiency Assessment

| Dimension | Assessment | Preflight note |
| --- | --- | --- |
| Decision reconstructability | strong | The decision can be framed as commit/pilot/stage/defer a supplier relationship under uncertainty. |
| Economics and operations | moderate to strong | Retailer delivery-density and fleet-electrification context appears available; detailed unit economics still need source-packet work. |
| Counterparty and production risk | strong | Pre-cutoff supplier financial and manufacturing-risk evidence appears available. |
| Trust, psychology, or strategic pressure | strong | Sustainability goals, last-mile competition, supplier credibility, and option value are decision-relevant. |
| Timing and irreversibility | moderate to strong | A staged commitment can preserve optionality, but exclusivity, supplier dependency, warrant economics, and public signaling are facilitator-only until reveal. |
| Owner/incentive clarity | strong | Retailer operations, sustainability, finance, legal/procurement, and innovation owners can be mapped cleanly. |
| Independent action or outcome availability | available | Sealed facilitator-only sources appear sufficient for later reveal and calibration. |
| Leakage risk | high but manageable | Agreement and outcome sources are highly contaminating, but a pre-announcement cutoff can keep them sealed. |

## Recommendation

Proceed with Canoo/Walmart as the next Judgment Spine case track, but only through the source-packet step first.

The immediate next artifact should be a clean pre-cutoff `source_packet_v0.md` plus a paired `safety_receipt_v0.md`. It should use the recommended cutoff and exclude all agreement-announcement, agreement-filing, post-cutoff, and outcome material from participant-facing sections. The source packet may contain a facilitator-only appendix only if it is clearly separated and never consumed by the participant packet before blind judgment.

Do not create a harness fixture, facilitator ledger, blind judgment, scoring result, or outcome calibration until the source packet and safety receipt pass a zero-spoiler readback.

## Hold Or No-Go Change Conditions

Downgrade to `HOLD_TIER_1_CANDIDATE` if a clean pre-cutoff source packet cannot reconstruct supplier financial risk, production maturity, vehicle-fit, retailer delivery strategy, and alternative supplier context without leaking the actual agreement.

Downgrade to `NO_GO_FOR_BLIND_USE` if the only usable source path requires agreement-announcement titles, post-cutoff agreement filings, bankruptcy/outcome sources, or articles whose titles/snippets reveal the actual decision or later outcome.

## Non-Claims

- No buyer validation.
- No willingness-to-pay proof.
- No repeatability proof.
- No product readiness.
- No feature readiness.
- No implementation readiness.
- No commercial readiness.
- No model-training readiness.
- No fine-tuning readiness.
- Source packet exists only as a pre-cutoff source substrate candidate; it is not participant-ready.
- No participant packet.
- No safety receipt.
- No sealed blind judgment.
- No facilitator ledger.
- No scoreable v0.14 fixture.
- No Judgment Spine validation.
- No proof that Step A plumbing demonstrates judgment quality.
- No claim that Canoo/Walmart is safe for participant use yet.

## Next Authorized Step

Run a docs-only adversarial artifact review of `docs/research/judgment-spine/cases/canoo-walmart/source_packet_v0.md` and `docs/research/judgment-spine/cases/canoo-walmart/safety_receipt_v0.md` before any participant packet is authored.

Required boundary: plumbing works only; not judgment quality.
