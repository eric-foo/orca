# Orca Buyer Proof Packet v0

```yaml
retrieval_header_version: 1
artifact_role: Product artifact
scope: First buyer-proof packet for testing Orca's public-signal decision artifact promise.
use_when:
  - Running customer discovery for Orca buyer proof.
  - Deciding whether first memo production, executive deck production, proof kill, or proof graduation may proceed.
authority_boundary: retrieval_only
open_next:
  - .agents/workflow-overlay/product-proof.md
  - docs/product/orca_product_lead_first_icp_wedge_decision_v0.md
  - docs/product/orca_product_proof_lead_charter_v0.md
  - docs/decisions/turn_08_product_thesis_v0.md
input_hashes:
  - path: docs/decisions/turn_08_product_thesis_v0.md
    sha256: 822653A241CF84675A3F07F695BA0ED3BFACC230F7F13AA47A4649B5DB2CD7E6
  - path: docs/product/core_spine_v0_method_validation_replay_packet_v0.md
    sha256: 8CB2D592D49C1C10DD5DD91A070D2800AF61DFDFC67D7C56A404A75F2EEA2161
  - path: docs/product/orca_product_lead_first_icp_wedge_decision_v0.md
    sha256: B570672CD7F31B2D78F9DC5E851C3AEDA7030A56ECF2CDC6733E0191ED3DDC23
    note: SUPERSEDED as wedge authority by docs/decisions/orca_icp_wedge_pricing_first_v0.md (reread-required)
  - path: docs/decisions/orca_icp_wedge_pricing_first_v0.md
    sha256: REREAD_REQUIRED
  - path: docs/review-outputs/adversarial-artifact-reviews/orca_ai_exposed_icp_refinement_adversarial_review_v0.md
    sha256: 648864959A13143F9C0C4DF5A8553D5F4BD0D7608FF09ADE6632938D748CADBA
```

## Status And Verdict

Status: `PROPOSED_BUYER_PROOF_PACKET_V0`

Product planning verdict: `NEEDS_CUSTOMER_DISCOVERY`.

Readiness verdict: `ready for product-fit testing`; not ready for product-bet planning until the graduation criteria in this packet are met and accepted.

Feature planning verdict: not ready. This packet does not route to feature planning.

## Pricing-First Refinement (2026-06-08)

This packet's first-proof framing is REFINED by the owner-locked pricing-first
direction. Controlling wedge authority:
`docs/decisions/orca_icp_wedge_pricing_first_v0.md` (the pinned `input_hashes` /
v0 ICP-wedge references are superseded by it — reread-required). Deltas:

- Engine/spine = outside-in COMPETITIVE & market intelligence; pricing is its
  first application (the competitive decision with the cleanest public substrate).
- First-proof BEACHHEAD re-scoped: from "developer-facing SaaS" (a stale,
  convenience-derived inheritance) to the AI-MONETIZATION SLICE — B2B SaaS making
  a first-time AI-monetization or competitor-triggered repricing/repackaging
  decision, where the competitor-pricing substrate is publicly rich and the firm
  is flying blind. Dev-facing SaaS is a strong sub-instance, not the defining
  qualifier. Wedge frame stays cross-sector-open. Decision family
  (pricing/packaging/monetization) is UNCHANGED.
- Beachhead RATIONALE (so this reads as a test instrument, not an arbitrary
  filter): the "first-time AI-monetization / flying-blind" qualifiers exist
  because that is where public signal can plausibly DECIDE the repricing move
  rather than merely CONFIRM it — the firm has no internal AI-pricing history to
  fall back on. Caveat the proof must test: in a first-time wave the
  competitor-price substrate is itself new/sparse, so "publicly rich" is not yet
  "clean/decision-grade." See the decision record.
- Servability HARD GATE: the differentiated read must sit on a CLEAN,
  decision-grade public substrate — competitor PRICE/packaging signal (pricing
  pages, changelogs, filings, earnings), NOT user reviews (independently shown
  biased / FTC-polluted / interview-gated). Read every "enough public signal" /
  "meaningful public signal" requirement below as "clean, decision-grade
  substrate."
- Open question (pending, NOT validated): does public signal DECIDE the repricing
  move or merely CONFIRM it — to be tested by two method-validation cases
  (pricing-repricing + clean-substrate displacement), no buyer contact.

```yaml
direction_change_propagation:
  doctrine_changed: First-proof framing refined to pricing-first / AI-monetization beachhead / outside-in competitive-intelligence engine / clean-substrate servability hard gate.
  trigger: product_doctrine
  controlling_sources_updated:
    - this artifact
  controlling_decision: docs/decisions/orca_icp_wedge_pricing_first_v0.md
  downstream_surfaces_checked:
    - docs/decisions/turn_08_product_thesis_v0.md   # consistent; no change (pricing within scope)
    - .agents/workflow-overlay/product-proof.md      # buyer-proof + trust semantics unchanged
  non_claims:
    - not validation
    - not willingness-to-pay
    - not readiness
    - not ICP proven
```

The substantive content below (proof standard, target buyer, rubric, kill and
graduation criteria, exclusions, and all non-claims) is SURGICALLY ALIGNED to
the refinement; proof standard, rubric, kill/graduation criteria, non-claims, and
all non-claim boundaries are unchanged in substance.

## Proof Standard

This packet tests one narrow first-proof claim:

A real decision owner at a B2B SaaS company making a first-time
AI-monetization or competitor-triggered repricing/repackaging decision —
where the competitor-pricing substrate is publicly rich and the firm is flying
blind — will use an Orca decision artifact to reduce allocation risk before
committing budget to a live pricing, packaging, API, billing, usage, add-on,
or monetization decision. Developer-facing SaaS is a strong sub-instance of
this AI-monetization slice; the wedge frame is cross-sector-open. The engine
is outside-in competitive & market intelligence; pricing is its first
application. Orca creates that artifact by cleaning, classifying,
source-backing, and constraining messy, noisy, and contradictory public market
signals into inspectable decision evidence.

Minimum viable artifact: a manual decision memo plus evidence appendix.

Premium buyer-facing artifact: an executive-grade decision deck derived from the memo and evidence appendix.

Commercial next-step hypothesis: a fixed-scope paid decision sprint or equivalent budget-adjacent commitment. This is a hypothesis to test, not validated commercial readiness.

The proof is manual and docs-first. It does not authorize software implementation, automation, source systems, dashboards, collection pipelines, source maps, data-spine designs, packages, tests, commits, pushes, PRs, or feature planning.

## Evidence Mode And Source Boundary

Profile: `standard`.

Subagents launched: 3.

Evidence mode: delegated advisory directional, adversarial, and grounding lanes. Each lane was advisory input only; none was a verdict, implementation authority, or proof of readiness.

Source mode: local Orca authority and repo-visible product artifacts only. No public web research was used. Archived contaminated replay outputs were not read.

## Target Buyer

Primary segment:

B2B SaaS companies making a first-time AI-monetization or
competitor-triggered repricing/repackaging decision, where the
competitor-pricing substrate is publicly rich (pricing pages, changelogs,
filings, earnings, visible public reaction) and the firm is flying blind (no
internal AI-pricing history or directly applicable precedent). Developer-facing
SaaS is a strong sub-instance; the wedge frame is cross-sector-open. A
qualified target must have a live pricing, packaging, API, billing, usage,
add-on, or monetization decision in the next 30-90 days.

Targets must have a clean, decision-grade public substrate — competitor
price/packaging signal (pricing pages, changelogs, filings, earnings) — to
support a differentiated decision memo. User reviews are confirmatory-only and
must be flagged as independently biased (J-curve self-selection) and
potentially polluted (FTC 16 CFR 465); they do not satisfy the hard gate.
Changelog or docs updates and visible ecosystem reaction are acceptable
supplementary signal where the competitor-price substrate anchors the read. A
qualified target must also have a named decision owner who can identify a
concrete budget, launch, retention, revenue-capture, customer-backlash, or
sales-enablement consequence.

If results are mixed, diagnose pricing, packaging, API, billing, usage,
add-on, and monetization sub-types separately before treating the decision
family as repeatable or non-repeatable.

Primary decision owner:

VP Product, GM, pricing or packaging lead, growth or strategy lead, product marketing lead, or founder/operator directly accountable for the decision.

Economic context:

The decision should have meaningful allocation risk: launch spend, pricing
change, packaging change, API monetization, billing transition, usage-based
monetization, add-on monetization, package migration, customer backlash risk,
churn risk, sales enablement cost, competitive response cost, or delayed
capture of a real opportunity.

Disqualifiers:

- No named decision owner.
- Budget-adjacent champion cannot surface a named decision owner for the memo step.
- No live 30-90 day pricing, packaging, API, billing, usage, add-on, or
  monetization decision.
- No budget or allocation consequence.
- Buyer wants only generic research, source volume, dashboard access, or a market-monitoring feed.
- Buyer requires private/internal data or automated collection before a manual public-signal memo can be useful.
- Categorical trust refusal: buyer says public-signal evidence cannot affect this decision regardless of evidence quality, explanation, examples, numbers, case logic, or proof memo.
- Buyer attributes such as `venture-backed`, `AI-native`, or `AI-adjacent`
  are neither qualifiers nor disqualifiers. They may be recorded as context,
  but cannot replace the decision owner, live decision, consequence,
  public-signal surface, paid-first condition, trust-refusal test, or
  consulting-risk test.

## Live Decision Trigger

The proof should start only when at least one of these triggers is present:

- A pricing, packaging, API, billing, usage, add-on, or monetization change is
  being planned or debated.
- A competitor or adjacent platform has changed pricing, packaging, API
  access, billing, usage, add-on, or monetization.
- An AI-triggered shift, such as AI feature bundling, AI add-on monetization,
  AI cost-structure-driven repricing, or an AI-native competitor packaging
  move, creates a pricing, packaging, API, billing, usage, add-on, or
  monetization decision.
- Public customer, developer, buyer, partner, or ecosystem reaction creates risk around a planned change.
- A launch, board, budget, strategy, or GTM decision deadline creates a near-term need to reduce allocation risk.

The trigger must be real enough that the buyer can say what decision is pending, who owns it, what budget or allocation is at stake, and when the decision must be made.

AI exposure is trigger and candidate-context ordering only. It is not a buyer
filter, not a wedge replacement, not buyer validation, not willingness-to-pay
proof, and not market-size or capital-density proof. Trust,
competitive-positioning, agent-workflow, and AI-cost-structure questions count
inside this packet only when they present as the first-wedge decision families
above.

## Orca Promise

Orca helps a decision owner reduce allocation risk before committing budget by turning messy public market signals into a clean, source-backed, inspectable, and bounded decision artifact.

For this first proof, the promise is not "Orca sets the correct price." The promise is narrower:

Orca can identify a safer action ceiling for a pricing, packaging, API,
billing, usage, add-on, or monetization decision, such as hold, narrow,
segment, phase, exempt, grandfather, message, test, upgrade, downgrade, or
reframe.

## Manual Proof Artifact

Artifact name: `Public-Signal Pricing/Package/Billing Decision Risk Memo`.

Minimum sufficient artifact:

A concise manual memo plus evidence appendix for one qualified live decision. The memo is the reasoning substrate and proof gate. It should be good enough for a buyer readback before any premium deck is produced.

Premium artifact:

An executive-grade decision deck may be produced only after the memo and evidence appendix pass the same proof gates. The deck must be derived from the memo and appendix, preserve uncertainty and action-ceiling discipline, and be suitable for internal decision circulation by the buyer.

The Product Proof Lead or designated operator produces the proof memo and, only if justified, the executive deck. The proof artifact should fit a bounded manual session under the accepted scope. If it materially exceeds that scope, classify the result as consulting-risk evidence and record it in the batch notes.

Core/satellite/bespoke boundary:

- Core is the repeatable decision spine.
- Satellites adapt the spine to buyer, industry, decision family, competitor set, and source families.
- Bespoke work is allowed only as bounded final adaptation. Overage or repeated custom work remains consulting-risk evidence unless it points to a repeatable decision family.

## Public-Signal Trust Handling

Use `.agents/workflow-overlay/product-proof.md` for trust-objection semantics.

Classify public-signal trust state as:

- `trust_open`: buyer already sees public signals as potentially relevant.
- `trust_objection`: buyer is skeptical but willing to evaluate evidence quality, examples, numbers, mechanism, case logic, proof memo, or decision artifact.
- `trust_refusal`: buyer states public signals cannot affect the decision regardless of evidence quality, examples, numbers, mechanism, case logic, or proof experience.

Only `trust_refusal` disqualifies or blocks memo production on public-signal trust grounds. `trust_objection` is proof material: capture it, test it, and read it back.

Recommended memo and evidence appendix shape:

1. Decision question and live trigger.
2. Decision owner, timing, and allocation risk.
3. Public-signal synthesis relevant to the decision.
4. Signal-quality caveats, including source cleanliness, audience fit, uncertainty, and artificial-amplification risk where visible.
5. Buyer, user, developer, partner, or ecosystem objection patterns.
6. Competitor or category movement relevant to the decision.
7. Valid action ceiling and unsafe overclaims.
8. Decision options: hold, narrow, segment, phase, exempt, grandfather, message, test, upgrade, downgrade, or reframe.
9. Evidence appendix with source links or citations.
10. Explicit non-claims.

Recommended executive deck shape, if the premium layer is produced:

1. Decision question and recommendation verb.
2. Executive action ceiling: accelerate, narrow, delay, defend, or reframe.
3. What public signals can and cannot support.
4. Source-backed signal synthesis.
5. Buyer, user, developer, partner, or ecosystem objection patterns.
6. Competitor or category movement relevant to the decision.
7. Options, risks, and decision deadline.
8. Evidence appendix pointer and explicit non-claims.

Intentionally manual:

- Source selection.
- Source reading.
- Evidence extraction.
- Signal-quality judgment.
- Memo writing.
- Buyer readback.
- Pull classification.

Deferred or excluded:

- Dashboards.
- Source systems.
- Collection pipelines.
- Source maps.
- Data-spine designs.
- Automated scoring.
- Generalized memo generation.
- CRM or sales automation.
- Feature planning.
- Implementation planning.

## Evaluation Rubric

Grade A: strong pull.

- Buyer has a named live decision with timing and allocation consequence.
- Buyer accepts the manual memo and evidence appendix as decision-relevant.
- The memo changes, narrows, delays, accelerates, defends, reframes, or de-risks the decision.
- Buyer uses or forwards the memo internally, or a qualified decision owner requests an executive deck for internal decision circulation tied to the live decision.
- Buyer asks for a fixed-scope paid decision sprint, second decision artifact, budget-owner meeting, vendor setup, LOI, procurement path, referral, or equivalent commercial next step.

Paid-decision-sprint-level pull means at least one commercial next-step signal: payment offer, fixed-scope sprint sponsorship, LOI, vendor/procurement path, budget-owner meeting, or referral to another live decision owner with stated urgency. Memo usefulness or deck interest alone is not enough.

Grade B: useful but not commercial pull.

- Buyer has a live decision and finds the memo useful.
- Memo sharpens the decision but does not produce a commercial next step.
- Buyer asks for more thinking, but not with budget-adjacent behavior.

Grade C: weak signal.

- Buyer praises the work but cannot name a decision use.
- Buyer treats the memo as market research.
- Buyer asks for more source volume, dashboards, or monitoring instead of decision-risk reduction.
- Buyer does not involve the actual decision owner.

Grade D: kill or reframe signal.

- No live decision exists.
- Buyer shows `trust_refusal`, or the proof memo fails to move a `trust_objection` enough for public-signal evidence to affect the decision.
- The memo cannot reduce allocation risk without private data or software.
- Buyer interest depends on bespoke consulting with no repeatable pattern.
- No fixed-scope paid decision sprint or equivalent commercial next step appears after useful feedback.

## Buyer Pull

Behavior that counts as pull:

- Buyer brings a real decision rather than responding to a hypothetical concept.
- Buyer gives decision context, timing, and stakes.
- Buyer requests delivery by a decision deadline.
- Buyer schedules a readback with decision or budget-adjacent stakeholders.
- Buyer uses the memo in the decision process.
- Buyer asks for a second memo, executive deck for internal decision circulation, or deeper cut on the same decision family.
- Buyer offers payment, pilot sponsorship, LOI, vendor setup, procurement path, budget-owner meeting, or a referral to another live decision owner.

Evidence of decision-judgment pull includes the buyer naming a specific action the memo helped avoid, narrow, reframe, sequence, or defend; asking for a second decision artifact in a different decision context; asking for an executive deck for internal decision circulation tied to a qualified live decision; or bringing a budget owner / decision owner into the next conversation. Requests only for more sources, deeper research, deck polish, or custom analysis on the same topic are not enough.

Behavior that does not count as pull:

- Compliments.
- Curiosity.
- Generic "send me the deck" interest detached from a qualified live decision and internal decision use.
- Requests for a dashboard before any decision use.
- Interest from someone without decision ownership or budget adjacency.
- Desire for generic research or source volume.
- Internal Client 0 method validation.

## Commercial Path Boundary

The first offer hypothesis is a fixed-scope paid decision sprint around one
qualified live decision and one bounded decision artifact. It is not proof of
willingness to pay, repeatability, or commercial readiness.

A retainer comes later only after recurring decision cadence and observable
buyer pull. Repeated ad hoc custom work without a repeatable decision family is
consulting-risk evidence, not graduation evidence.

## Suggested Proof Batch

Run a small manual proof batch before any product-bet or feature-planning claim:

1. Qualify 6-8 target decision owners, or budget-adjacent champions who can surface a named decision owner for the memo step.
2. Select up to 3 buyers with live pricing, packaging, API, billing, usage,
   add-on, or monetization decisions.
3. Produce one manual memo plus evidence appendix per selected buyer.
4. Produce an executive deck only when the memo and evidence appendix pass the same gates and the deck has a live decision-circulation use.
5. Run a live readback for each memo, and deck readback only if a deck is produced.
6. Record decision use, risk reduction, trust objections, commercial next step, and anti-pull.
7. Classify each result using the rubric above.

These numbers are planning defaults, not validation proof. They should be adjusted only if owner acceptance changes the proof batch.

The memo/readback stage requires a named decision owner or budget-accountable decision lead.

Suggested buyer readback questions:

- What action would this memo help you avoid, narrow, reframe, sequence, or defend?
- What would you do differently if this memo were in the decision packet?
- Would an executive deck help internal decision circulation, and if so who would use it for this live decision?
- Who owns the budget or accountability for this decision, and should they be in the readback?
- What commercial next step, if any, would be justified if another memo reached this bar?
- Which part felt like decision judgment rather than custom research labor?

## Kill Criteria

Kill or reframe the proof if any of these conditions hold after the first proof batch:

- Fewer than two qualified decision owners have live decisions in the selected segment and decision family.
- No delivered memo is used in a real allocation decision.
- Buyers consistently classify the memo as interesting research rather than decision support.
- Buyers show `trust_refusal`, or the proof memo fails to move `trust_objection` enough for the public-signal basis, source cleanliness, uncertainty framing, or action-ceiling discipline to affect the decision.
- Buyers require private/internal data, dashboards, source systems, collection pipelines, source maps, automation, or data-spine design before the memo can be useful.
- The strongest buyer ask is generic market monitoring, not allocation-risk reduction.
- No buyer shows fixed-scope paid-decision-sprint-level pull or equivalent commercial next step after useful memo feedback.
- The work only succeeds as bespoke consulting and does not repeat around a decision family.

A single strong candidate may justify a follow-up conversation, but not graduation or proof-boundary acceptance.

## Graduation Criteria

Graduate to product-bet planning only if all of the following are met and accepted:

- Repeat means: At least two independent qualified decision owners in the same buyer segment and decision family produce Grade A or Grade B results, without reusing the same buyer or same internal decision.
- At least two qualified decision owners use a manual Orca memo in a live allocation decision.
- At least one buyer shows fixed-scope paid-decision-sprint-level pull or equivalent commercial commitment.
- The memo plus evidence appendix format is repeatable enough to test again without building software.
- Any executive deck layer is derived from the memo and appendix and does not become bespoke presentation consulting.
- The strongest buyer value is Orca's decision judgment and action-ceiling discipline, not merely custom research labor.
- The proof does not require dashboards, source systems, collection pipelines, source maps, automation, or data-spine design.
- Non-claims remain intact.

Feature planning may be considered only after product-bet planning or equivalent owner-accepted proof evidence, plus a later explicit feature-planning authorization. This packet alone does not authorize feature planning.

## What Must Not Be Built Yet

Do not build:

- Source systems.
- Dashboards.
- Collection pipelines.
- Source maps.
- Data-spine designs.
- Scoring engines.
- Databases.
- APIs.
- Packages.
- Tests.
- Automation.
- CRM workflows.
- Generalized memo tooling.
- User interfaces.
- Feature plans.
- Implementation plans.

Do not create buyer-validation, feature-readiness, implementation-readiness, or commercial-readiness claims.

## Product Artifact Impact

Impact classification: `artifact-as-proof` and `artifact-required`.

This packet is required before first buyer proof because it binds the proof claim, target buyer, decision family, minimum memo artifact, evidence appendix, premium executive deck layer, rubric, kill criteria, graduation criteria, exclusions, and non-claims.

The later manual decision memo plus evidence appendix is the minimum artifact-as-proof. It should be produced only after a qualified buyer and live decision trigger are selected. The executive deck is buyer-facing packaging derived from that substrate, not separate proof by itself.

## Not-Proven Boundaries

This packet does not prove:

- Buyer validation.
- External willingness to pay.
- Paid pilot conversion.
- Repeatable demand.
- Procurement feasibility.
- Retention, renewal, or expansion.
- ROI.
- Product readiness.
- Feature readiness.
- Implementation readiness.
- Commercial readiness.
- Core Spine v0 validation.
- Source-system feasibility.
- Data rights.
- Runtime feasibility.

The accepted Core Spine v0 replay packet remains bounded method signal only.

## May Proceed

Customer discovery may proceed under this packet as docs-first product-fit testing after owner acceptance of the proof boundary.

First memo production may proceed only after a named qualified buyer and live decision trigger are selected. It must use a manual decision memo and evidence appendix as the minimum artifact. Executive deck production may proceed only after the memo and evidence appendix pass the same gates and the deck is tied to a qualified live decision use.

No product-bet planning, feature planning, implementation, source-system design, automation, commits, pushes, PRs, or commercial-readiness claim may proceed from this packet.

## Blockers

Authority blocker: none for writing these docs-first product artifacts under `docs/product/`.

Product fit gaps:

- No external buyer has been qualified yet.
- No live decision trigger has been selected yet.
- No manual memo has been produced or read back yet.
- No buyer pull, fixed-scope paid-decision-sprint intent, or equivalent commercial next step has been observed yet.
