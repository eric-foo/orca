# Orca Offer Hypothesis v0

```yaml
retrieval_header_version: 1
artifact_role: Product artifact
scope: Revised Orca offer hypothesis aligned to the value proposition, selected first ICP wedge, product docs, and owner feedback that the buyer-facing artifact is an executive decision deck.
use_when:
  - Preparing Orca customer-discovery framing or buyer-facing offer language.
  - Checking whether offer language preserves Orca product-proof boundaries.
  - Comparing future ICP, commercial-frame, or deliverable-shape decisions against this hypothesis.
authority_boundary: retrieval_only
open_next:
  - docs/decisions/turn_08_product_thesis_v0.md
  - docs/product/core_spine_v0_product_contract.md
  - docs/product/core_spine_v0_information_production_foundation_v0.md
  - docs/decisions/orca_icp_wedge_pricing_first_v0.md  # current wedge authority (supersedes orca_product_lead_first_icp_wedge_decision_v0.md below)
  - docs/product/orca_product_lead_first_icp_wedge_decision_v0.md  # superseded — reread-required; see pricing-first record above
  - docs/product/orca_buyer_proof_packet_v0.md
  - docs/product/orca_product_proof_lead_charter_v0.md
  - docs/review-outputs/adversarial-artifact-reviews/orca_offer_hypothesis_v0_narrow_adversarial_review.md
  - docs/review-outputs/adversarial-artifact-reviews/orca_ai_exposed_icp_refinement_adversarial_review_v0.md
  - .agents/workflow-overlay/product-proof.md
input_hashes:
  - path: docs/decisions/turn_08_product_thesis_v0.md
    sha256: 822653A241CF84675A3F07F695BA0ED3BFACC230F7F13AA47A4649B5DB2CD7E6
  - path: docs/product/core_spine_v0_product_contract.md
    sha256: 6D1876BE75E3ACAD349479E2CD584E869EB7A9B1C1C40F98E8C9234005EAB17E
  - path: docs/product/core_spine_v0_information_production_foundation_v0.md
    sha256: 8C0A784F80C577D725CE4D71BDED7F15B502F61B545DF5158B18352C351F7767
  - path: docs/product/orca_product_lead_first_icp_wedge_decision_v0.md
    sha256: B570672CD7F31B2D78F9DC5E851C3AEDA7030A56ECF2CDC6733E0191ED3DDC23
  - path: docs/product/orca_buyer_proof_packet_v0.md
    sha256: ECDCD4BFC626295D486189F063CA8429EA2F324BD71151C9D28A52683927A224
  - path: docs/product/orca_product_proof_lead_charter_v0.md
    sha256: 731E4349AA931613D393DFC64B05F410E098D40F86D1C26A11BD31A1E2852322
  - path: docs/review-outputs/adversarial-artifact-reviews/orca_offer_hypothesis_v0_narrow_adversarial_review.md
    sha256: 26CC2DC631AD550234BDB6904640616109F76CC3F5DAC90F490ED76B524D40A6
  - path: docs/review-outputs/adversarial-artifact-reviews/orca_ai_exposed_icp_refinement_adversarial_review_v0.md
    sha256: 648864959A13143F9C0C4DF5A8553D5F4BD0D7608FF09ADE6632938D748CADBA
  - path: .agents/workflow-overlay/product-proof.md
    sha256: 0EB8A11DAA2A2BE1FC7F610AAA48004D97200A18D11679F9C8D45731EED61F21
  - path: C:\Users\vmon7\Desktop\projects\orca nonrepo\offer_creation_handbook_saas_consulting.md
    sha256: A9505B589ECFC3D9BCBA587E342AFEC2DF6EFC804B9248976ABFCFD09A7595EF
```

## Status

Status: `PROVISIONAL_LOCK_OFFER_HYPOTHESIS_V0`.

This artifact defines the provisionally locked offer hypothesis for now. It is
not a hard lock, accepted commercial offer, buyer validation,
willingness-to-pay proof, repeatability proof, product readiness, feature
readiness, implementation readiness, or commercial readiness.

## Pricing-First Refinement (2026-06-08)

This artifact's first-proof framing is REFINED by the owner-locked pricing-first
direction. Controlling wedge authority:
`docs/decisions/orca_icp_wedge_pricing_first_v0.md` (the pinned `input_hashes` /
v0 ICP-wedge references below are superseded by it — reread-required). Deltas:

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
    - .agents/workflow-overlay/product-proof.md      # buyer-proof semantics unchanged
  non_claims:
    - not validation
    - not willingness-to-pay
    - not readiness
    - not ICP proven
```

The substantive content below (the broad offer, value proposition, decision
families, deck framing, and all non-claims) has been SURGICALLY ALIGNED to this
refinement and is unchanged in substance. (Proof standard, evaluation rubric, and
kill/graduation criteria live in the buyer-proof packet and charter, not in this
offer doc.)

## Source Use

Controlling Orca sources:

- `docs/decisions/turn_08_product_thesis_v0.md`
- `docs/product/core_spine_v0_product_contract.md`
- `docs/product/core_spine_v0_information_production_foundation_v0.md`
- `docs/decisions/orca_icp_wedge_pricing_first_v0.md` — current wedge authority
- `docs/product/orca_product_lead_first_icp_wedge_decision_v0.md` — superseded by pricing-first record above; reread-required
- `docs/product/orca_buyer_proof_packet_v0.md`
- `docs/product/orca_product_proof_lead_charter_v0.md`
- `.agents/workflow-overlay/product-proof.md`

Reference heuristic:

- `C:\Users\vmon7\Desktop\projects\orca nonrepo\offer_creation_handbook_saas_consulting.md`

The offer-creation handbook is useful for structure: specific buyer, expensive
problem, credible mechanism, economic upside, and repeatable delivery terms. It
does not override Orca source hierarchy, product-proof gates, buyer-proof
non-claims, or docs-first limits.

## Product-Doc Sync Note

The existing product docs distinguish internal proof substrate from buyer-facing
packaging:

- The decision memo plus evidence appendix is the internal reasoning substrate,
  proof gate, and backtest artifact.
- The executive-grade decision deck is the premium buyer-facing artifact,
  derived from that substrate.

This offer hypothesis should therefore lead with the executive deck externally.
It should not front a memo in buyer meetings. Internally, the memo and evidence
appendix still exist so the deck cannot become presentation theater.

The selected first ICP wedge and the patched product-proof docs now constrain
the first proof offer. This artifact should preserve the broader Orca value
proposition while making the first offer surface specific enough for buyer
qualification.

## Deep-Thinking Judgment

The earlier offer was too narrow and too proof-operator-facing. It over-indexed
on post-revenue B2B SaaS, API, data-product, pricing, and packaging contexts,
then made the memo feel like the offer.

That was the wrong front door for the value proposition.

Post-ICP update: that judgment should not be read as anti-specificity. It was a
guard against shrinking the whole value proposition too early. The selected ICP
wedge now belongs in the first proof offer because the offer needs a buyer,
decision trigger, and disqualifier set that can be tested in market.

The stronger offer is broader at the top and stricter underneath:

- broad enough for foundational strategic and hyper-competitive decisions;
- open to pre-revenue or post-revenue companies when they face a real decision
  with enough public or external signal;
- buyer-facing as an executive-grade decision deck with a decision matrix;
- internally disciplined by memo, evidence appendix, and source-backed
  inference;
- not a dashboard, market-monitoring feed, source dump, or free strategy deck.

The only place to push back hard: "greatest" cannot mean unconstrained upside
or whatever story feels most exciting. Orca can sell the greatest
evidence-supported decision, not the greatest unsupported bet. Otherwise the
offer breaks the signal-quality judgment that makes Orca valuable.

## Offer Name

Working buyer-facing name: `Strategic Decision Evidence Deck`.

Alternate names to test:

- `Foundational Decision Evidence Deck`
- `Hyper-Competitive Decision Deck`
- `Public-Signal Strategic Decision Deck`
- `Strategic Decision Matrix And Evidence Deck`

Current recommendation: use `Strategic Decision Evidence Deck` for the buyer
surface because the value proposition is a deck, not a memo. Keep "sprint" as
an internal or commercial packaging question for a later Commercial Frame CA.

## Core Offer Hypothesis

Orca turns messy, noisy, and contradictory public market signals into
executive-grade decision decks for foundational strategic and hyper-competitive
decisions, helping leaders decide whether to accelerate, narrow, delay, defend,
or reframe before budget, runway, launch focus, or strategic commitment is
spent.

The engine and spine is outside-in competitive & market intelligence; pricing
is its first application — the competitive decision with the cleanest public
substrate and the highest decision density.

For a company facing a consequential strategic decision before internal data is
conclusive, Orca gathers, cleans, classifies, source-backs, and constrains
public customer, user, buyer, competitor, partner, community, and ecosystem
signals into a decision deck and decision matrix.

The deck helps the decision owner identify the greatest evidence-supported
decision path: the strongest move, delay, defense, narrowing, reframing, or
test that the visible evidence can support without overclaiming.

First proof offer layer:

For B2B SaaS teams making a first-time AI-monetization or
competitor-triggered repricing/repackaging decision, where the competitor-
pricing substrate is publicly rich (pricing pages, changelogs, filings,
earnings) and the firm is flying blind, Orca offers a public-signal decision
artifact backed by a memo and evidence appendix, surfaced as a decision matrix
or executive deck when the substrate passes the proof gates, to help the
decision owner narrow, phase, defend, delay, or reframe before committing
budget, roadmap, pricing, packaging, or GTM motion. Developer-facing SaaS is
a strong sub-instance of this beachhead; the wedge frame is cross-sector-open.
The decision family (pricing, packaging, API, billing, usage, add-on,
monetization) is unchanged.

This first proof offer does not make the AI-monetization slice the permanent
ICP. It is the bounded market-facing test of the broader offer.

## Buyer-Facing Draft

Orca turns messy, noisy, and contradictory public market signals into
executive-grade decision decks for foundational strategic and hyper-competitive
decisions, helping leaders decide whether to accelerate, narrow, delay, defend,
or reframe before budget, runway, launch focus, or strategic commitment is
spent.

Most teams either ignore public signals until backlash appears, or overreact to
loud anecdotes, scattered posts, competitor narratives, and noisy community
feedback. Orca gathers, cleans, classifies, source-backs, and constrains those
signals into decision evidence, so the team can see the greatest
evidence-supported path: what to move on, what to delay, what to defend, what
to narrow, and what to reframe.

The buyer-facing deliverable is an executive-grade decision deck with a
decision matrix, evidence-backed options, tradeoffs, risks, and explicit
uncertainty. Internally, the deck is built from a memo-like reasoning substrate
and evidence appendix, but the meeting artifact is the deck.

For the first proof lane, this buyer-facing language should be introduced only
inside the selected wedge: B2B SaaS teams making a first-time AI-monetization
or competitor-triggered repricing/repackaging decision, where the competitor-
pricing substrate is publicly rich and the firm is flying blind, with a live
30-90 day pricing, packaging, API, billing, usage, add-on, or monetization
decision. Developer-facing SaaS is a strong sub-instance; the frame is
cross-sector-open.

## ICP Status

The first proof ICP wedge is selected, not proven.

Selected first proof ICP / wedge:

B2B SaaS companies making a first-time AI-monetization or competitor-triggered
repricing/repackaging decision, where the competitor-pricing substrate is
publicly rich (pricing pages, changelogs, filings, earnings) and the firm is
flying blind, with a live 30-90 day pricing, packaging, API, billing, usage,
add-on, or monetization decision where clean, decision-grade public substrate
(competitor price/packaging signal; reviews are confirmatory-only and flagged)
can change a decision-risk memo, decision matrix, or executive decision deck.
Developer-facing SaaS is a strong sub-instance; the wedge frame is
cross-sector-open.

This updates the first proof offer, not the permanent company-wide value
proposition. The broader Orca value proposition can still apply to other
foundational strategic and hyper-competitive decisions later, but they are out
of the first proof offer unless a later accepted Orca decision replaces this
wedge.

Buyer / sponsor types for the first proof offer:

- VP Product, GM, pricing or packaging lead, growth or strategy lead, product
  marketing lead, platform/product lead, or founder/operator directly
  accountable for the live decision.
- Decision owner or budget-accountable lead who can participate in readback.

Qualifying conditions for the first proof offer:

- B2B SaaS context where the company is making a first-time AI-monetization
  or competitor-triggered repricing/repackaging decision (developer-facing SaaS
  is a strong sub-instance; the frame is cross-sector-open).
- Competitor-pricing substrate is publicly rich (pricing pages, changelogs,
  filings, earnings) and the firm is flying blind.
- Live 30-90 day pricing, packaging, API, billing, usage, add-on, or
  monetization decision.
- Concrete consequence if wrong: churn, customer backlash, delayed revenue
  capture, launch waste, developer trust loss, sales-enablement cost,
  positioning damage, competitive-response misfire, or overbroad package
  commitment.
- Clean, decision-grade public substrate (competitor price/packaging signal;
  reviews are confirmatory-only and flagged as biased/FTC-polluted/
  interview-gated).
- Buyer is willing to evaluate whether public-signal evidence can affect the
  decision after method, evidence quality, examples, numbers, case logic,
  memo, or deck are explained.
- Buyer agrees to decision-artifact readback before memo, deck, or paid
  production is treated as meaningful pull.

AI exposure is a trigger/context-ordering hypothesis only. It is not a buyer
filter, proof claim, or standalone decision family. `venture-backed`,
`AI-native`, and `AI-adjacent` are neither qualifiers nor disqualifiers.
Standalone trust, competitive-positioning, agent-workflow, or AI cost-structure
questions qualify only when they resolve into pricing, packaging, API, billing,
usage, add-on, or monetization.

Do not treat this selected wedge as buyer validation, willingness-to-pay proof,
repeatability proof, product readiness, commercial readiness, or permanent ICP
lock.

## Decision Families

The broad Orca offer can later cover foundational strategic and
hyper-competitive decisions, including:

- product roadmap bets;
- positioning shifts;
- pricing, packaging, and monetization;
- category entry;
- competitor narrative response;
- growth-channel prioritization;
- buyer-objection remediation;
- launch sequencing;
- founder or investor allocation decisions where public market evidence can
  change the decision.

The first proof offer is narrower:

- pricing;
- packaging;
- API access or API monetization;
- billing model or billing transition;
- usage limits, usage-based monetization, overage, or quota decisions;
- add-on monetization, including AI add-ons;
- beta-to-paid, bundle-versus-add-on, package migration, grandfathering,
  segment-exemption, or developer/customer communication decisions tied to the
  above.

This preserves the broader offer boundary while avoiding a vague "we do
strategy" position. The first proof decision must be specific enough to build a
memo, evidence appendix, decision matrix, and if justified an executive deck
against.

## Expensive Problem

The buyer is making a high-stakes decision before internal data is conclusive,
while public signals are visible but messy, contradictory, and easy to misuse.

This is especially painful when the company is pre-revenue, entering a new
category, reacting to a competitor, choosing a wedge, or making a strategic
commitment before enough internal customer behavior exists.

The expensive failure modes are:

- Overreacting to loud but low-quality public complaints.
- Underreacting to early market, trust, pricing, positioning, or ecosystem
  signals.
- Committing budget, runway, launch focus, or brand credibility to the wrong
  strategic path.
- Copying a competitor move without knowing which public objections or buyer
  beliefs matter.
- Delaying a good move because public evidence is noisy and untrusted.
- Treating public signals as generic research instead of constrained decision
  evidence.

## Mechanism

Most companies trying to use public signals for strategic decisions make one of
two mistakes: they either treat public noise as anecdotal and ignore it, or
they turn it into dashboards, sentiment summaries, and source dumps that still
do not tell a decision owner what to do.

The problem is that public signals are not evidence until they are gathered,
cleaned, deduplicated, source-backed, classified, and constrained by what they
can actually support.

Orca uses a manual decision-evidence process:

1. Bind one strategic decision question, owner or owner-context, deadline, and
   consequence.
2. Identify relevant public and external signal families.
3. Gather, clean, deduplicate, and source-back the evidence.
4. Classify signal quality, audience fit, uncertainty, and visible artificial
   amplification risk where applicable.
5. Map buyer, user, competitor, partner, community, or ecosystem objection
   patterns.
6. Separate valid decision evidence from source volume, praise, noise, and
   overclaim.
7. Build an executive decision deck and matrix that states the greatest
   evidence-supported path and what would change the answer.

The mechanism is not "AI research," "social listening," or "more sources." The
mechanism is source-backed signal-quality judgment plus evidence-constrained
decision design.

## Buyer-Facing Deliverable

Primary buyer-facing deliverable:

- Executive-grade strategic decision deck.

Required deck components:

- decision question;
- strategic context and stakes;
- decision matrix;
- recommended path and alternatives;
- what public signals can and cannot support;
- source-backed signal synthesis;
- buyer, user, competitor, partner, community, or ecosystem objection patterns;
- risks and tradeoffs by option;
- what would change the recommendation;
- evidence appendix or source appendix;
- explicit non-claims.

Internal production substrate:

- memo-like reasoning substrate;
- evidence appendix;
- source-backed signal-quality notes;
- uncertainty and boundary notes.

The buyer does not need to receive or be fronted with the internal memo. The
deck is the meeting artifact.

## Commercial Frame Status

Commercial frame is not locked.

A separate Chief Architect run should decide pricing, packaging, duration,
payment terms, and whether the offer is sold as a sprint, deck, advisory
package, or another paid container.

Current commercial boundary:

- No unpaid custom deck production.
- No free source expansion after a buyer asks for "more sources."
- No free "send me the deck" path when the deck would require custom work.
- Paid-first is acceptable and likely necessary before bespoke evidence work.
- Exact price, duration, scope, refund terms, and expansion terms are
  `UNKNOWN - requires owner input`.

## Fit Diagnostic

A candidate qualifies for the broad offer hypothesis only if the answer is yes
to all required fields:

1. Is there a foundational strategic or hyper-competitive decision?
2. Does the decision have material consequence for budget, runway, launch
   focus, positioning, competitive response, growth, category entry, or
   allocation?
3. Is internal data incomplete, lagging, unavailable, or not enough by itself?
4. Are public or external signals visible enough to gather, inspect, and
   constrain?
5. Is there a decision owner, founder, operator, investor, or budget-adjacent
   stakeholder who can use the deck?
6. Is the buyer willing to pay or enter a paid-first commercial path before
   custom deck production?
7. Is the buyer willing to evaluate whether public-signal evidence can affect
   the decision after the method, evidence quality, examples, numbers, case
   logic, deck, or decision artifact are explained?

Disqualify or reframe if:

- The buyer wants unpaid generic research, unpaid source volume, dashboards, or
  monitoring before any paid decision use.
- There is no specific strategic decision.
- The work requires private/internal data before public-signal evidence can
  matter.
- The buyer states public signals cannot affect the decision regardless of
  evidence quality, examples, numbers, mechanism, case logic, or proof
  experience.

Initial skepticism is not a disqualifier. It is `trust_objection` unless it
becomes categorical `trust_refusal`.

For the first proof offer, add these stricter gates:

1. Is the company making a first-time AI-monetization or competitor-triggered
   repricing/repackaging decision (the AI-monetization slice is the beachhead;
   developer-facing SaaS is a strong sub-instance; frame is cross-sector-open)?
2. Is the competitor-pricing substrate publicly rich — pricing pages,
   changelogs, filings, or earnings available and decision-grade?
3. Is the live decision within 30-90 days?
4. Is the decision specifically pricing, packaging, API, billing, usage,
   add-on, or monetization?
5. Is there a named decision owner or budget-accountable lead?
6. Is clean, decision-grade public substrate (competitor price/packaging
   signal) available to support an inspectable decision artifact? (Reviews
   are confirmatory-only and flagged — not the differentiated read.)
7. Is AI exposure, if present, only a trigger/context signal rather than the
   qualification basis?

If any first proof gate fails, do not stretch the first proof offer around the
candidate. Record the gap and either disqualify, hold for clarification, or
defer to a later broader-offer test.

## Offer Audit Against Handbook

Specific buyer:

- Locked only for the first proof offer. The first buyer wedge is B2B SaaS
  companies making a first-time AI-monetization or competitor-triggered
  repricing/repackaging decision (competitor-pricing substrate publicly rich;
  firm flying blind), with a named owner of a live pricing, packaging, API,
  billing, usage, add-on, or monetization decision. Developer-facing SaaS is
  a strong sub-instance; the frame is cross-sector-open. This is not a
  permanent ICP lock.

Specific problem:

- Pass as hypothesis: expensive strategic uncertainty before a foundational or
  hyper-competitive decision, especially when internal data is incomplete and
  public signals are noisy.

Specific mechanism:

- Pass as hypothesis: gather, clean, deduplicate, source-back, classify,
  constrain, and convert public signals into a deck and decision matrix.

Economic upside:

- Plausible but not proven: better allocation, fewer false moves, faster
  confident commitment, avoided strategic misallocation, and stronger
  competitive response. No buyer validation, willingness-to-pay proof, ROI
  proof, or paid conversion exists yet.

Scalable delivery:

- Partially proven: internal memo substrate plus deck/matrix packaging is
  repeatable in theory. Repeatability is not proven until multiple buyers or
  decision owners use the artifact in comparable decision families.

## Pull Signals To Test

Count as stronger pull:

- Buyer brings a real strategic decision and deadline.
- Buyer names stakes, owner, budget, runway, launch, retention, GTM, category,
  or competitive consequence.
- Buyer asks for paid custom deck production.
- Buyer requests the deck for internal decision circulation tied to the live
  decision.
- Buyer asks for more sources inside a paid scope, or pays for a deeper source
  expansion.
- Buyer schedules a readback with decision or budget-adjacent stakeholders.
- Buyer uses or forwards the deck internally.
- Buyer asks for a second decision artifact, budget-owner meeting, vendor
  setup, LOI, procurement path, or urgent referral to another live decision
  owner.

Do not count as strong pull by itself:

- Praise.
- Curiosity.
- Free "send me the deck" interest with no payment path.
- Free requests for more sources.
- Requests for dashboards or market monitoring before decision use.
- Interest from someone with no path to a decision owner or paid sponsor.

## Non-Claims

This artifact does not prove:

- Buyer validation.
- Willingness to pay.
- Paid pilot conversion.
- Repeatable demand.
- Procurement feasibility.
- ROI.
- Product readiness.
- Feature readiness.
- Implementation readiness.
- Commercial readiness.
- Core Spine v0 validation.

It does not authorize software implementation, source systems, dashboards,
collection pipelines, source maps, data-spine design, automation, tests,
packages, feature planning, product-bet planning, commits, pushes, PRs, or
readiness claims.

## Recommendation

Use this revised offer hypothesis as the buyer-facing direction: Orca sells an
executive-grade strategic decision deck and matrix built from public-signal
evidence for foundational strategic and hyper-competitive decisions.

Use the selected ICP wedge as the first proof offer surface: B2B SaaS teams
making a first-time AI-monetization or competitor-triggered repricing/
repackaging decision (competitor-pricing substrate publicly rich; firm flying
blind), with a live 30-90 day pricing, packaging, API, billing, usage, add-on,
or monetization decision. Developer-facing SaaS is a strong sub-instance; the
frame is cross-sector-open.

Do not narrow the entire Orca value proposition to this wedge. The wedge is the
first market-facing proof container, chosen because it is specific enough to
test buyer pull and broad enough to matter if it works.

This recommendation now aligns with the current first proof lane in
`docs/product/orca_buyer_proof_packet_v0.md`,
`docs/product/orca_product_proof_lead_charter_v0.md`, and
`docs/decisions/orca_icp_wedge_pricing_first_v0.md` (current wedge authority;
`docs/product/orca_product_lead_first_icp_wedge_decision_v0.md` is superseded
— reread-required).

Do not front a memo as the offer. Keep the memo-like reasoning substrate and
evidence appendix internal so the deck remains credible, inspectable, and
source-backed.

Do not decide the commercial frame inside this artifact. Run a separate
Commercial Frame CA for price, paid-first structure, duration, scope, and
expansion terms.
