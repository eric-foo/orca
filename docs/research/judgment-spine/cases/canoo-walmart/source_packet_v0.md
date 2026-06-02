# Canoo Walmart Source Packet v0

```yaml
retrieval_header_version: 1
artifact_role: Research artifact
scope: Clean pre-cutoff source packet substrate for the Canoo/Walmart Judgment Spine case track.
use_when:
  - Building or reviewing a zero-spoiler participant packet for Canoo/Walmart.
  - Checking which pre-cutoff evidence can support the blind decision frame.
  - Keeping agreement-announcement, agreement-filing, post-cutoff, and outcome material out of participant-facing work.
authority_boundary: retrieval_only
open_next:
  - docs/research/judgment-spine/cases/canoo-walmart/safety_receipt_v0.md
  - docs/research/judgment-spine/cases/canoo-walmart/case_track_preflight_v0.md
  - .agents/workflow-overlay/product-proof.md
stale_if:
  - A later owner decision changes the cutoff or decision question.
  - Any participant-facing packet includes excluded public-action, filing, post-cutoff, or outcome material.
  - A later source audit finds that a source listed as pre-cutoff was published or materially modified after the recommended cutoff.
```

## Preflight Receipt

```yaml
orca_start_preflight:
  agents_read: yes
  overlay_read: yes
  source_pack: custom S1 plus Canoo/Walmart preflight, product-proof zero-spoiler rules, and one public pre-cutoff source-loading unit
  edit_permission: docs-write
  target_scope: Create the clean pre-cutoff Canoo/Walmart source packet and paired safety receipt.
  dirty_state_checked: yes
  blocked_if_missing: no
```

Repository state note: workspace state was already dirty and included untracked Judgment Spine and harness artifacts before this packet was written. This packet supports the next case-track step only; it is not validation, readiness, source-of-truth promotion, implementation authorization, score-readiness, product proof, or judgment quality.

## Status

```yaml
packet_status: source_packet_candidate
cutoff_policy: recommended_pre_announcement_cutoff
recommended_cutoff: before the July 2022 public-action announcement
participant_packet_ready: no
safety_receipt: docs/research/judgment-spine/cases/canoo-walmart/safety_receipt_v0.md
adversarial_review_required_before_participant_packet: yes
```

## Decision Frame

A large retailer is evaluating whether, when, and how strongly to commit to a novel electric last-mile delivery-vehicle supplier. The strategic pressure is real: the retailer is scaling home delivery, wants lower-emissions logistics, and has enough density and infrastructure to make electric delivery vehicles plausible. The counterpressure is also real: the target supplier is early-stage, pre-revenue, capital-intensive, not yet at volume production, and dependent on external funding and execution.

Candidate blind question:

```text
Should the retailer make a significant commitment to this early-stage electric delivery-vehicle supplier for last-mile operations now, and if so should the commitment be a narrow pilot, a staged conditional order, an option-heavy agreement, a broader commercial commitment, or a hold/defer pending stronger supplier-production evidence?
```

## Participant-Safe Source Manifest

These sources are intended as clean pre-cutoff source substrate. Do not treat the URLs, titles, or summaries as final participant-packet text until the safety receipt and adversarial review pass.

| ID | Source | Date | Source type | Participant use |
| --- | --- | --- | --- | --- |
| CW-P1 | Walmart InHome expansion announcement, `https://corporate.walmart.com/news/2022/01/05/walmart-to-expand-inhome-delivery-reaching-30-million-u-s-homes-in-2022` | 2022-01-05 | Retailer official source | Allowed after participant-packet wording pass |
| CW-P2 | BrightDrop/Walmart EV van reservation announcement, `https://news.gm.com/home.detail.html/Pages/news/us/en/2022/jan/ces/0105-brightdrop.html` | 2022-01-05 | Alternative supplier / incumbent-backed EV benchmark | Allowed after participant-packet wording pass |
| CW-P3 | Walmart transportation emissions strategy note, `https://corporate.walmart.com/news/2022/06/08/zero-sum-how-walmart-transportation-is-working-to-reduce-emissions-now-and-in-the-future` | 2022-06-08 | Retailer official source | Allowed after participant-packet wording pass |
| CW-P4 | Canoo FY2021 results release, `https://www.prnewswire.com/news-releases/canoo-inc-announces-fourth-quarter-and-fiscal-year-2021-results-301492051.html` | 2022-02-28 | Supplier financial and operating disclosure | Allowed after participant-packet wording pass |
| CW-P5 | Canoo Q1 2022 results release, `https://www.prnewswire.com/news-releases/canoo-inc-announces-first-quarter-2022-results-301544386.html` | 2022-05-10 | Supplier financial and operating disclosure | Allowed after participant-packet wording pass |
| CW-P6 | Canoo Form 10-Q filing detail for period ended 2022-03-31, `https://www.sec.gov/Archives/edgar/data/1750153/000162828022013637/0001628280-22-013637-index.html` | 2022-05-10 | Official SEC filing index | Allowed only as source-verification pointer; participant packet should paraphrase from audited source review, not expose SEC navigation noise |
| CW-P7 | Independent pre-cutoff Canoo financial-risk coverage, `https://www.caranddriver.com/news/a39967402/canoo-ev-startup-financial-trouble/` | 2022-05 | Independent media context | Optional; use only if review confirms title and framing do not over-prime the blind participant |

## Evidence Units

### CW-E01: Retailer Last-Mile Expansion Pressure

Source IDs: CW-P1.

The retailer planned to expand InHome delivery from 6 million households to 30 million U.S. households by the end of 2022. It planned to hire more than 3,000 associate delivery drivers and build a 100% all-electric delivery-van fleet to support that service. The service fits a broader last-mile strategy using store density, delivery speed, sustainability, and third-party delivery capabilities.

Decision relevance: demand-side pressure for delivery vehicles is credible. A fleet decision is not cosmetic if the service expansion and driver hiring are real.

Uncertainty preserved: source does not prove which supplier should be selected, how many vehicles are needed, or how much supplier risk should be accepted.

### CW-E02: Retailer Infrastructure And Electrification Fit

Source IDs: CW-P1, CW-P3.

The retailer had a stated goal to operate a zero-emissions logistics fleet by 2040 and already reported EV-charging infrastructure across stores and clubs. Its June 2022 transportation note framed electric vehicles as attractive for yard operations, lighter-weight hauls, and day deliveries around 200 miles, while also emphasizing that different vehicle classes may need different fuel types and that pilot learning matters.

Decision relevance: electric delivery vehicles are strategically aligned with the retailer's logistics and sustainability direction, but the retailer's own framing favors testing and fit-by-use-case rather than one broad EV answer.

Uncertainty preserved: the source packet does not prove the target supplier's product is the best operational fit.

### CW-E03: Alternative Supplier Benchmark Exists

Source IDs: CW-P2.

An incumbent-backed EV commercial-vehicle supplier announced that the retailer had reserved 5,000 electric delivery vans for the same broad last-mile and zero-emissions fleet context. The supplier also had FedEx commercial-vehicle activity and reported initial delivery or pilot evidence before the Canoo cutoff.

Decision relevance: the retailer had at least one visible alternative path for electric delivery vans. This changes the decision from "EV delivery vehicles or nothing" into "which supplier mix, staging, and risk posture is justified."

Uncertainty preserved: the alternative benchmark does not prove the alternative is superior, available on the needed timeline, or sufficient for all delivery use cases.

### CW-E04: Supplier Product And Production Promise

Source IDs: CW-P4, CW-P5.

The target supplier represented itself as developing modular electric vehicles for consumer and business applications, with operating locations across several U.S. states. It reported manufacturing-facility progress, platform/battery development progress, preorders, gamma vehicles, winter testing, and expected spending tied to launch and production work.

Decision relevance: the supplier was not merely a slide-deck idea; there were disclosed assets, vehicles, tests, and operating plans that could make a staged commitment worth examining.

Uncertainty preserved: gamma builds, preorders, and management claims are not volume-production proof.

### CW-E05: Supplier Liquidity And Going-Concern Risk

Source IDs: CW-P4, CW-P5, CW-P6, CW-P7.

The supplier reported $224.7 million of cash and cash equivalents at 2021 year-end and $104.9 million at March 31, 2022. It reported a $125.4 million Q1 2022 net loss, $120.3 million of net cash used in operating activities, and a going-concern warning tied to funding timing and accounting rules. Independent pre-cutoff coverage also treated the cash position and production funding risk as material.

Decision relevance: counterparty risk is central. A broad commitment may help the supplier's credibility but may also expose the retailer to production, delivery, supplier-dependency, and public-signal risk.

Uncertainty preserved: liquidity risk does not automatically mean "do not engage"; it may argue for staged commitments, options, strict conditions, or supplier-diversification.

### CW-E06: Spending And Launch Burden

Source IDs: CW-P4, CW-P5.

The supplier disclosed large operating and capital-expenditure expectations around the relevant period. Q1 2022 outlook expected operating expenses excluding stock-based compensation and depreciation of $95 million to $115 million and capital expenditures of $85 million to $105 million for Q2 2022.

Decision relevance: even if the product promise is attractive, the supplier's path to delivery depends on capital access, manufacturing execution, and burn-rate management.

Uncertainty preserved: the source packet does not compute a runway or production-probability estimate; that belongs in facilitator labeling and blind judgment.

## Decision Tensions To Preserve

- EV delivery fleet need is credible, but supplier selection is separable from EV strategy.
- The target supplier has differentiated product and option value, but not proven volume execution.
- A retailer commitment could create strategic option value, but it could also subsidize counterparty risk.
- Alternative supplier evidence means a hold/defer or diversified supplier approach may be live, not merely conservative.
- Public signaling can help a supplier but can also lock the retailer into reputational exposure.
- The right answer may be a staged, conditional, option-heavy structure rather than yes/no.

## Participant-Packet Build Notes

For a later participant packet:

- Include only pre-cutoff facts from this packet after safety review.
- Preserve uncertainty rather than implying what the retailer actually did.
- Do not disclose post-cutoff public-action terms, public-action existence, later implementation or non-implementation facts, financing effects after the cutoff, later adverse events, or outcome.
- Do not include source URLs, titles, snippets, or filenames if they reveal the actual action or later outcome.
- Reword source titles into neutral source labels where needed.

## Current Gaps

- No participant-safe prose packet has been authored.
- No source-byte hashes or canonical evidence-unit hashes have been computed.
- No facilitator ledger or band-input labels exist.
- No sealed blind judgment exists.
- No adversarial review has checked whether this packet over-primes supplier-risk or leaks the later decision path.
- No harness admission or scoring is authorized.

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
- No complete participant packet.
- No safety-reviewed participant source list.
- No sealed blind judgment.
- No facilitator ledger.
- No scoreable v0.14 fixture.
- No Judgment Spine validation.
- No proof that Step A plumbing demonstrates judgment quality.

## Next Authorized Step

Run a docs-only adversarial artifact review of `source_packet_v0.md` plus `safety_receipt_v0.md` before creating `participant_packet_v0.md`.

Required boundary: plumbing works only; not judgment quality.
