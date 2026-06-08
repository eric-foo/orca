# Orca Product Proof Lead Charter v0

```yaml
retrieval_header_version: 1
artifact_role: Product artifact
scope: Bounded charter for the Orca Product Proof Lead and first buyer-proof lane.
use_when:
  - Setting up Orca buyer-proof work before feature planning.
  - Checking Product Proof Lead ownership, exclusions, and graduation rules.
authority_boundary: retrieval_only
open_next:
  - .agents/workflow-overlay/product-proof.md
  - docs/product/orca_product_lead_first_icp_wedge_decision_v0.md
  - docs/product/orca_buyer_proof_packet_v0.md
  - docs/decisions/turn_08_product_thesis_v0.md
input_hashes:
  - path: docs/decisions/turn_08_product_thesis_v0.md
    sha256: 822653A241CF84675A3F07F695BA0ED3BFACC230F7F13AA47A4649B5DB2CD7E6
  - path: docs/product/core_spine_v0_method_validation_replay_packet_v0.md
    sha256: 8CB2D592D49C1C10DD5DD91A070D2800AF61DFDFC67D7C56A404A75F2EEA2161
  - path: docs/product/orca_product_lead_first_icp_wedge_decision_v0.md
    sha256: B570672CD7F31B2D78F9DC5E851C3AEDA7030A56ECF2CDC6733E0191ED3DDC23
  - path: docs/review-outputs/adversarial-artifact-reviews/orca_ai_exposed_icp_refinement_adversarial_review_v0.md
    sha256: 648864959A13143F9C0C4DF5A8553D5F4BD0D7608FF09ADE6632938D748CADBA
```

## Status And Boundary

Status: `PROPOSED_PRODUCT_PROOF_CHARTER_V0`

Product planning verdict: `NEEDS_CUSTOMER_DISCOVERY`.

Readiness verdict: `ready for product-fit testing`; not buyer-validated, not feature-ready, not implementation-ready, and not commercially ready.

This charter defines a bounded Orca Product Proof Lead. It is not a full Product Lead role. It does not own roadmap, feature planning, implementation, product readiness, commercial readiness, or validation claims.

This artifact is docs-first only. It does not authorize software implementation, automation, packages, tests, dashboards, source maps, data-spine designs, commits, pushes, PRs, collection pipelines, or feature planning.

## Pricing-First Refinement (2026-06-08)

This charter's first-proof framing is REFINED by the owner-locked pricing-first
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
  biased / FTC-polluted / interview-gated). Read "enough public signal" below as
  "clean, decision-grade substrate."
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

The substantive content below (role purpose, ownership, exclusions, first proof
lane, pull standard, kill and graduation criteria, and all non-claims) is
SURGICALLY ALIGNED to the refinement. Proof standard, rubric, kill/graduation
criteria, non-claims, manual/docs-first boundary, pull standard, trust handling,
commercial path, and all not-proven boundaries are UNCHANGED.

## Source Basis

- Current owner instruction for Orca product-proof planning.
- `AGENTS.md` and `.agents/workflow-overlay/` authority, especially product artifact write permission under `docs/product/`.
- `docs/decisions/turn_08_product_thesis_v0.md`, which frames Orca as an outside-in strategic intelligence system for public market signals and allocation decisions.
- `docs/product/orca_product_lead_first_icp_wedge_decision_v0.md`, which selects the first proof lane and binds AI exposure as trigger/context ordering only.
- `docs/review-outputs/adversarial-artifact-reviews/orca_ai_exposed_icp_refinement_adversarial_review_v0.md`, which rejects AI buyer-attribute filters and standalone AI/trust/competitive-positioning decision-family expansion.
- `docs/product/core_spine_v0_method_validation_replay_packet_v0.md`, accepted only as bounded method signal, not validation, buyer validation, feature readiness, implementation readiness, or commercial readiness.
- Advisory `workflow-product-ultraplan` standard lanes: directional, adversarial, and grounding. These were advisory inputs only, not verdicts or readiness proof.

No public web research was used. Archived contaminated replay outputs were not read.

## Role Purpose

The Orca Product Proof Lead owns the buyer-proof loop for one narrow question:

Can a real decision owner at a B2B SaaS company making a first-time
AI-monetization or competitor-triggered repricing/repackaging decision — where
the competitor-pricing substrate is publicly rich and the firm is flying blind
— use an Orca decision artifact to reduce allocation risk before committing
budget to a live pricing, packaging, API, billing, usage, add-on, or
monetization decision, after Orca cleans, classifies, source-backs, and
constrains messy, noisy, and contradictory public market signals into
inspectable decision evidence?

The engine for this work is outside-in competitive and market intelligence;
pricing is its first application — the competitive decision with the cleanest
public substrate. Developer-facing SaaS is a strong sub-instance of this
beachhead, not the defining qualifier; the wedge frame is cross-sector-open.

The minimum viable artifact is a manual decision memo plus evidence appendix. The premium buyer-facing artifact is an executive-grade decision deck derived from that memo and appendix. The first commercial next-step hypothesis is a fixed-scope paid decision sprint, not validated commercial readiness.

The role exists to convert bounded method signal into buyer-proof learning without prematurely turning Orca into a product organization, software system, dashboard, deck shop, research factory, or implementation program.

## What The Product Proof Lead Owns

1. Buyer-proof design for the first external proof loop.
2. Selection of one target buyer segment and one live decision family for the proof.
3. Qualification of live decision triggers before memo production.
4. The manual Orca decision memo, evidence appendix, and optional executive deck shape used in the proof.
5. The proof evaluation rubric, including pull, weak signal, kill, and graduation criteria.
6. Source cleanliness, uncertainty framing, action-ceiling discipline, and explicit non-claims inside proof artifacts.
7. Buyer readback questions that test decision use, risk reduction, trust, and commercial next step.
8. Proof notes that distinguish buyer behavior from praise.
9. Recommendations to kill, reframe, continue discovery, or graduate the proof.
10. Boundary enforcement against roadmap, feature, implementation, validation, and commercial-readiness leakage.

## What Remains Outside The Role

The Product Proof Lead does not own:

- Orca roadmap.
- Product readiness.
- Feature planning or feature readiness.
- Implementation planning or implementation readiness.
- Software architecture, runtimes, packages, tests, dashboards, source maps, data-spine designs, source systems, collection pipelines, automations, scoring engines, or generalized tooling.
- Commercial readiness, sales operations, final pricing, packaging, procurement operations, or revenue ownership.
- Claims that Core Spine v0 is validated, accepted, predictive, buyer-validated, feature-ready, implementation-ready, or commercially ready.
- Broad AI strategy, standalone trust work, standalone competitive-positioning
  work, agent-workflow design, or AI cost-structure analysis unless it presents
  as a qualified pricing, packaging, API, billing, usage, add-on, or
  monetization decision.
- Broad market research, generic social listening, person-level dossiers, outreach lists, data-broker activity, manipulation, fake reviews, botting, or deceptive competitive tactics.
- Revalidation of the accepted method replay packet or use of archived contaminated replay outputs.

## First Proof Lane

Recommended first buyer segment:

B2B SaaS companies making a first-time AI-monetization or
competitor-triggered repricing/repackaging decision, where the
competitor-pricing substrate is publicly rich and the firm is flying blind.
Developer-facing SaaS is a strong sub-instance; the wedge frame is
cross-sector-open. Targets must have a live 30-90 day pricing, packaging,
API, billing, usage, add-on, or monetization decision.

Targets must have a clean, decision-grade public substrate to support a
meaningful memo — competitor price/packaging signal (pricing pages,
changelogs, filings, earnings). User reviews are confirmatory-only and
flagged: independently shown biased (J-curve self-selection), FTC-polluted
(16 CFR 465), and interview-gated. A qualified target must also have a named
decision owner who can identify a concrete budget, launch, retention,
revenue-capture, customer-backlash, or sales-enablement consequence.

If results are mixed, diagnose pricing, packaging, API, billing, usage,
add-on, and monetization sub-types separately before treating the decision
family as repeatable or non-repeatable.

Recommended decision owner:

VP Product, GM, pricing or packaging lead, growth or strategy lead, product marketing lead, or founder/operator directly accountable for the budgeted decision.

Recommended first decision family:

Pricing, packaging, API, billing, usage-based monetization, AI add-on
monetization, package migration, beta-to-paid transition, bundle versus add-on
framing, grandfathering, segment exemptions, or developer/customer
communication around those changes, where a false broad commit could create
backlash, churn, positioning damage, wasted launch spend, support or
sales-enablement cost, competitive-response misfire, or delayed capture of a
real opportunity.

AI exposure is trigger and candidate-context ordering only. AI feature
bundling, AI add-on monetization, AI cost-structure-driven repricing, and
AI-native competitor packaging moves count only when they resolve into the
first decision family above. Buyer attributes such as `venture-backed`,
`AI-native`, or `AI-adjacent` are neither qualifiers nor disqualifiers.

Selected product promise:

Orca reduces allocation risk before budget is committed by turning messy public market signals into a clean, source-backed, inspectable, and bounded decision artifact that identifies safer action ceilings such as hold, narrow, segment, phase, exempt, grandfather, message, test, upgrade, downgrade, or reframe.

Manual proof artifact:

A concise public-signal pricing/package/billing decision risk memo plus
evidence appendix, produced manually for one qualified live decision. The memo
is the reasoning substrate and minimum proof artifact; it must not depend on a
dashboard, source system, collection pipeline, source map, automation, or
generalized data spine.

Premium artifact:

An executive-grade decision deck may be produced only after the memo and evidence appendix pass the same gates. The deck must be derived from the memo and appendix, preserve uncertainty and action-ceiling discipline, and serve qualified internal decision circulation rather than generic presentation interest.

The Product Proof Lead or designated operator produces the proof memo and, only if justified, the executive deck. The proof artifact should fit a bounded manual session under the accepted scope. If it materially exceeds that scope, classify the result as consulting-risk evidence and record it in the batch notes.

Core/satellite/bespoke boundary:

- Core is the repeatable decision spine.
- Satellites adapt the spine to buyer, industry, decision family, competitor set, and source families.
- Bespoke work is allowed only as bounded final adaptation. Overage or repeated custom work remains consulting-risk evidence unless tied to a repeatable decision family.

## Public-Signal Trust Handling

Use `.agents/workflow-overlay/product-proof.md` for trust-objection semantics.

Classify public-signal trust state as:

- `trust_open`: buyer already sees public signals as potentially relevant.
- `trust_objection`: buyer is skeptical but willing to evaluate evidence quality, examples, numbers, mechanism, case logic, proof memo, or decision artifact.
- `trust_refusal`: buyer states public signals cannot affect the decision regardless of evidence quality, examples, numbers, mechanism, case logic, or proof experience.

Only `trust_refusal` disqualifies or blocks memo production on public-signal trust grounds. `trust_objection` is proof material: capture it, test it, and read it back.

## Pull Standard

Buyer pull means observable budget-adjacent behavior, not approval language.

Strong pull includes one or more of:

- A real decision owner brings a live decision with timing, stakes, and budget consequence.
- The buyer gives context and asks for a memo by a decision deadline.
- The buyer schedules a readback with the decision owner or budget-adjacent stakeholders.
- The memo changes, narrows, delays, accelerates, or de-risks the allocation decision.
- The buyer circulates or uses the memo in an internal decision process.
- A qualified decision owner requests an executive deck for internal decision circulation tied to the live decision.
- The buyer asks for a second decision artifact, deeper cut, fixed-scope paid decision sprint, vendor setup, LOI, budget-owner meeting, procurement path, referral to another decision owner, or equivalent commercial next step.

Paid-decision-sprint-level pull means at least one commercial next-step signal: payment offer, fixed-scope sprint sponsorship, LOI, vendor/procurement path, budget-owner meeting, or referral to another live decision owner with stated urgency. Memo usefulness or deck interest alone is not enough.

Evidence of decision-judgment pull includes the buyer naming a specific action the memo helped avoid, narrow, reframe, sequence, or defend; asking for a second decision artifact in a different decision context; asking for an executive deck for internal decision circulation tied to a qualified live decision; or bringing a budget owner / decision owner into the next conversation. Requests only for more sources, deeper research, deck polish, or custom analysis on the same topic are not enough.

Weak or non-pull includes:

- Praise, curiosity, or "interesting" feedback without a live decision.
- Requests for a generic report, dashboard, data feed, or source volume rather than decision-risk reduction.
- Generic deck interest detached from a qualified live decision and internal decision use.
- A desire for free advice without internal decision use.
- Interest that cannot name a decision owner, timing, allocation risk, or commercial next step.

## Commercial Path Boundary

The first offer hypothesis is a fixed-scope paid decision sprint around one
qualified live decision and one bounded decision artifact. It is not proof of
willingness to pay, repeatability, or commercial readiness.

A retainer comes later only after recurring decision cadence and observable
buyer pull. Repeated ad hoc custom work without a repeatable decision family is
consulting-risk evidence, not graduation evidence.

## Kill Criteria

Kill or materially reframe the proof if the first qualified proof batch shows any of the following:

- Fewer than two qualified decision owners have live decisions in the selected segment and decision family.
- Buyers treat the memo as generic research rather than decision-risk reduction.
- No delivered memo changes or sharpens a real allocation decision.
- Buyers will not use or circulate the memo in the decision process.
- Buyers show `trust_refusal`, or the proof memo fails to move a `trust_objection` enough for public-signal evidence, source cleanliness, and uncertainty boundaries to affect the decision.
- Value depends on bespoke consulting labor with no repeatable decision pattern.
- No buyer requests a fixed-scope paid decision sprint or equivalent commercial next step after useful memo feedback.
- The memo requires software, dashboards, collection pipelines, source maps, automation, or private/internal data to be credible.

A single strong candidate may justify a follow-up conversation, but not graduation or proof-boundary acceptance.

## Graduation Criteria

Graduate to product-bet planning only if the proof produces all of the following:

- Repeat means: At least two independent qualified decision owners in the same buyer segment and decision family produce Grade A or Grade B results, without reusing the same buyer or same internal decision.
- At least two qualified decision owners use a manual Orca memo in a live allocation decision.
- At least one buyer shows fixed-scope paid-decision-sprint-level pull or equivalent commercial commitment.
- The memo plus evidence appendix format remains sufficient without software, dashboards, source systems, source maps, or automation.
- Any executive deck layer is derived from the memo and appendix and does not become bespoke presentation consulting.
- The buyer values Orca's decision judgment and action-ceiling discipline, not merely custom research labor.
- The non-claims remain intact: no buyer validation, feature readiness, implementation readiness, or commercial readiness is asserted.

Feature planning remains later than product-bet planning. It may be considered only after accepted product proof evidence, explicit owner authorization, and a bounded feature-planning turn. This charter does not route to feature planning.

## Next Docs-First Product Work

Customer discovery may proceed as docs-first product-fit testing under this charter after owner acceptance of the proof boundary.

First memo production may proceed only for a named qualified buyer with a live
30-90 day pricing, packaging, API, billing, usage, add-on, or monetization
trigger, using the manual proof artifact in
`docs/product/orca_buyer_proof_packet_v0.md`. Executive deck production may
proceed only after the memo and evidence appendix pass the same gates and the
deck is tied to a qualified live decision use.

No implementation, automation, source-system design, data-spine design, dashboard design, source-map design, commits, pushes, PRs, or feature planning may proceed from this charter.

## Not-Proven Boundaries

This charter does not prove:

- Buyer validation.
- External willingness to pay.
- Repeatable demand.
- Procurement feasibility.
- ROI.
- Retention, renewal, or expansion.
- Product readiness.
- Feature readiness.
- Implementation readiness.
- Commercial readiness.
- Core Spine v0 validation.
- Source-system feasibility, data rights, or runtime feasibility.
