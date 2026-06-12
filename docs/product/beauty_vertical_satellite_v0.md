# Beauty Vertical Satellite Doctrine v0 — Slice 1

```yaml
retrieval_header_version: 1
artifact_role: Product satellite doctrine artifact (beauty vertical)
scope: >
  Slice-1 satellite vocabulary for the beauty/personal-care vertical:
  decision-family context, demand-semantics signal rows mapped onto the
  existing SCR signal_family / family_detail seam, a distortion-manifestation
  taxonomy held as satellite-grade Signal Integrity candidates, categorical
  source-family notes, and a promotion ledger under the Source-Family
  Promotion Rule. Bounded by the Core-vs-Satellite contract; redefines no
  core invariant.
use_when:
  - Reading or authoring beauty-vertical demand-signal or distortion vocabulary.
  - Filling SCR family_detail values or proposing Signal Use / Signal Integrity
    candidate rows for a beauty case.
  - Checking which beauty rules are satellite-grade versus core-promotion
    candidates.
authority_boundary: retrieval_only
open_next:
  - docs/product/core_spine/core_spine_v0_data_and_cleaning_spine_boundary_v0.md
  - docs/product/signal_content/core_spine_v0_signal_content_record_architecture_v0.md
stale_if:
  - The SignalFamily enum or the family_detail seam changes
    (orca-harness/signal_content/models.py or the SCR architecture direction).
  - The core Signal Integrity or Signal Use registries are built (all candidate
    rows below must re-map onto the real registry shapes).
  - The Core-vs-Satellite contract or Source-Family Promotion Rule in the
    boundary doc changes.
  - Any ledger row below is promoted or rejected by a later owner decision.
```

## Status And Claim Cap

`AUTHORED_SATELLITE_SLICE_1` — claim cap: **product-learning**. Authoring this
vocabulary proves nothing about judgment quality, signal quality, readiness,
validation, or buyer proof. Every row below is candidate doctrine for the
beauty satellite; nothing here is core promotion, registry design, schema, or
implementation authorization.

## Authorization Basis

Owner word 2026-06-12 (ECR lane thread): "perhaps let's work on beauty tuning
next. we will want to own the ontology probably." and "okay route for it,
prompt out for beauty satellite." — executed via
`docs/prompts/handoffs/beauty_vertical_satellite_slice1_authoring_handoff_prompt_v0.md`.
ECR stays vertical-agnostic; beauty ontology lives here (satellite) and, later,
in the SCR authored-interpretation lane. Documentation only.

## Contract Consumed

This satellite operates inside the Core-vs-Satellite contract
(`docs/product/core_spine/core_spine_v0_data_and_cleaning_spine_boundary_v0.md`,
"Core Vs Satellite" + "Source-Family Promotion Rule"). It owns only the
satellite surfaces named there: buyer context, decision owner, consequence,
decision-family language, competitor set, source-family relevance and blind
spots, source-family access notes and capture-feasibility constraints,
costly-behavior examples, and satellite-specific Signal Use rows. It must not
— and does not — redefine capture provenance, admissibility, cutoff
discipline, preservation discipline, integrity effects, cleaning traceability,
Action Ceilings, memo/appendix discipline, or non-claims.

The content seam consumed is the as-ratified SCR direction
(`docs/product/signal_content/core_spine_v0_signal_content_record_architecture_v0.md`)
and its as-built v0 model (`orca-harness/signal_content/models.py`, read-only):
four closed wedge-agnostic `SignalFamily` members plus
`RESIDUAL_FAMILY_UNRESOLVED`; vertical richness rides `family_detail` values,
never new spine columns; an unresolved family degrades to the residual rather
than being forced. The core **Signal Integrity registry and Signal Use
Classification registry shapes are reserved and unbuilt**; this satellite
consumes that boundary and proposes candidate *contents* only — it designs no
core registry shape.

Promotion-tag vocabulary used throughout (per the Source-Family Promotion
Rule): `source-invariant-core-candidate` / `source-family-adapted-satellite` /
`unresolved-candidate`.

## 1. Decision-Family Context

Satellite-owned context surfaces (not promotion-bearing rules). Product anchor:
the ratified consumer-demand thesis
(`docs/decisions/orca_product_thesis_consumer_demand_v0.md` — thesis,
value-proposition, central-read, and vertical-doctrine sections). Beauty/
personal-care is the proof vertical: substrate-rich (reviews, Reddit/forums,
trackers, trade press), entity hierarchies tractable, US-market first.

**Buyer context and decision owners.** Operator side first (indie/DTC beauty
operator door per the thesis buyer ladder): founder, brand GM, CMO, head of
sales/wholesale committing real allocation before internal data is conclusive.
Investor side later: consumer seed/VC screens, then PE/family-office diligence
underwriting whether observed demand is durable or manufactured.

**Consequence.** Capital committed ahead of conclusive internal data:
inventory working capital on a trending SKU, retailer slotting and launch
commitments, promo budget, acquisition price. The cost of acting on hollow
demand (viral spike, gifted-creator wave, stuffed reviews) is the loss this
vertical's read exists to prevent.

**Decision-family language** (beauty decision families this satellite serves;
labels are satellite vocabulary, not core terms):

| ID | Decision family | Typical owner | The live question |
| --- | --- | --- | --- |
| DF-B1 | Inventory / replenishment commitment | Operator (founder/GM) | Is this SKU's spike durable enough to buy deep against? |
| DF-B2 | Retail-channel expansion timing | Operator (sales/wholesale) | Is demand pull strong enough to survive a Sephora/Ulta/Target/Amazon commitment? |
| DF-B3 | Launch / category-extension timing | Operator (founder/CMO) | Does adjacent-category demand exist beyond our current buyers' politeness? |
| DF-B4 | Pricing / promo posture under competitor moves | Operator (GM/pricing) | Is the competitor's repricing biting our demand, or only their narrative? |
| DF-B5 | Defend-vs-harvest under viral competitor entry | Operator (founder/GM) | Is the entrant's demand real switching or rented attention? |
| DF-B6 | Demand-durability underwriting | Investor (screen/diligence) | Is the brand's growth durable demand or manufactured momentum? |

**Competitor-set framing.** In beauty the competitor set is category-and-claim
defined, not price-tier alone: clinical/derm-led, clean/ingredient-led,
masstige color, prestige skincare, TikTok-native, professional/salon. Three
satellite framings matter: (a) brand-vs-parent — reads roll up entity-resolved
brand→parent (a conglomerate can fund a hollow push longer than an indie);
(b) the **dupe set is a first-class competitor** — private-label and explicit
"dupes" compete on the same demand, and dupe discourse is itself a demand
signal about the original; (c) channel-defined sub-sets — a salon-exclusive
brand and a TikTok Shop brand may share a category but not a buyer decision.

**Industry constraints** (context for interpretation, not capture rules):
short trend half-life and seasonal/gifting cycles compress decision windows;
ingredient/claims regulation (FTC-calibrated integrity flags per the thesis)
bounds what brands may assert; retailer gatekeeping cycles quantize DF-B2;
PR-gifting and sampling culture make incentive-bearing content structurally
common rather than exceptional — which is why the distortion taxonomy in
section 3 is load-bearing for every family above.

## 2. Demand-Semantics Signal Rows

Owner seed list (verbatim, 2026-06-12): *attention, search, review velocity,
retail presence, switching, repurchase, workaround, complaint, community
pressure, channel movement.* Each seed is mapped onto the existing SCR seam
below — carrier `SignalFamily` member plus candidate `family_detail` values —
or explicitly residualized. Grain discipline is consumed from the SCR
direction: one record = one observed event/claim from one source slice; any
cross-source or cross-capture aggregate is Judgment-owned and never a record
field; `decision_relevance` stays a mechanical shape-derived tag. The
`family_detail` values below are candidate satellite payload vocabulary for
the (currently empty) `FamilyDetailBase` extension slot — no code change is
made or implied by listing them.

### Seed-to-Seam Mapping

| Rule | Seed | Carrier `signal_family` | Candidate `family_detail` value | Single-slice observable (what carries) | Judgment-owned remainder (what does not) | Tag |
| --- | --- | --- | --- | --- | --- | --- |
| R-DS1 | attention | `DEMAND_REACTION` | `attention_resonance` | One captured mention/creator-pickup/view-count state about the subject | Aggregate attention trends; any durable-vs-hollow read | source-family-adapted-satellite |
| R-DS2 | search | `DEMAND_REACTION` | `search_interest_state` | One captured search-interest panel state (the panel's own claim, for a query, over a window) | Interest→demand inference; cross-window trend reads | source-family-adapted-satellite |
| R-DS3 | review velocity | `DEMAND_REACTION` | `review_flow_state` | Review count/rating state visible on the captured slice; a `delta` only when the slice itself shows before/after | Computed velocity across captures/sources (a Judgment aggregate, never a field) | source-family-adapted-satellite |
| R-DS4a | retail presence (event) | `TRIGGER_TIMING_EVENT` | `retail_distribution_event` | Subject newly stocked/delisted/expanded at a named retailer | Whether the placement evidences demand | source-family-adapted-satellite |
| R-DS4b | retail presence (competitor act) | `COMPETITOR_PRICE_PACKAGING_MOVE` | `distribution_change` | A competitor's observed distribution/packaging/price change | Threat assessment; DF-B4/B5 reads | source-family-adapted-satellite |
| R-DS4c | retail presence (availability state) | **none — residualize** | — (`RESIDUAL_FAMILY_UNRESOLVED` today) | In-stock/out-of-stock/low-stock state on a captured listing | Sell-out-as-demand inference | unresolved-candidate (see CNF-1) |
| R-DS5 | switching | `DEMAND_REACTION` | `switching_report` | First-person switch report ("ditched X for Y"), direction carried by `reaction.direction` | Switching-rate aggregates; competitive damage reads | source-family-adapted-satellite |
| R-DS6 | repurchase | `DEMAND_REACTION` | `repurchase_report` | First-person repurchase/replenishment report ("third bottle") | Retention/repeat-rate aggregates | source-family-adapted-satellite |
| R-DS7 | workaround | `DEMAND_REACTION` | `workaround_report` | Effortful substitute-seeking: DIY dupe recipes, stockpiling before discontinuation, cross-border/gray-market sourcing, decanting against a packaging change | Whether workarounds evidence durable unmet demand | source-family-adapted-satellite |
| R-DS8 | complaint | `DEMAND_REACTION` | `complaint_churn_report` | Return/irritation/reformulation-backlash/"stopped working" report (negative `reaction.direction`) | Churn inference; counterevidence weighting (exclusion stays Judgment-owned) | source-family-adapted-satellite |
| R-DS9 | community pressure | `DEMAND_REACTION` | `community_pressure` | A collective durable-buyer-pressure act: restock petition, shade-range demand, bring-back campaign, discontinued-SKU megathread | Sustained-past-trigger persistence read | source-family-adapted-satellite |
| R-DS10a | channel movement (buyer report) | `DEMAND_REACTION` | `channel_switch_report` | First-person where-I-buy-it-now report | Channel-mix shift aggregates | source-family-adapted-satellite |
| R-DS10b | channel movement (brand/retailer act) | `TRIGGER_TIMING_EVENT` | `channel_event` | Subject enters/exits a channel (TikTok Shop launch, salon-exclusivity end); a competitor's same act maps via R-DS4b | What the move means for demand | source-family-adapted-satellite |

Costly-behavior examples (satellite-owned per Core Vs Satellite): R-DS5,
R-DS6, R-DS7, and R-DS9 are this vertical's canonical costly behaviors —
payment, switching, workarounds, durable buyer pressure. R-DS1 and R-DS2 are
attention/resonance class by the frozen core rule (engagement volume alone
never carries a Commit); that rule is consumed from the thesis, not authored
here.

### Candidate New Family (explicitly unpromoted)

- **CNF-1 `retail_availability_state`** — tag: **unresolved-candidate**. An
  availability state on a captured retail listing (out-of-stock, low-stock,
  waitlist) is not honestly a demand *reaction* (mapping it to
  `DEMAND_REACTION` would smuggle the sell-out-equals-demand inference into a
  mechanical carrier), not a competitor move, and not a dated trigger event.
  Today such a slice **degrades to `RESIDUAL_FAMILY_UNRESOLVED`** exactly as
  the enum design intends. Promotion to a fifth `SignalFamily` member is an
  additive enum change that is a separate owner-gated act requiring either
  survival across two non-overlapping source families or an explicit owner
  exception — neither is claimed here.

### Candidate Satellite Signal Use Rows

The Signal Use Classification **registry shape is core-reserved and unbuilt**;
graded Signal Use, Decision Strength, and Action Ceiling stay Judgment-owned.
The rows below are candidate satellite *contents* for that future registry,
held at a categorical level (signal kind → proposed use posture → integrity
dependency). They bind nothing until the core registry exists and Judgment
adopts them.

| Rule | Signal kind (from mapping above) | Proposed use posture (candidate) | Integrity dependency | Tag |
| --- | --- | --- | --- | --- |
| SU-B1 | Switching / repurchase / workaround reports (R-DS5/6/7) | Candidate decide-supporting demand evidence | Only with incentive/coordination flags clear (section 3) | source-family-adapted-satellite |
| SU-B2 | Attention / search states (R-DS1/2) | Attention/resonance class only; never sufficient alone for a Commit-tier verb | Platform-artifact and paid-amplification exposure is the default assumption, not the exception | source-family-adapted-satellite |
| SU-B3 | Review-flow states (R-DS3) | Confirm-only at best while stuffing-suspect flags are unresolved | Review-stuffing and incentive markers (D3/D4) | source-family-adapted-satellite |
| SU-B4 | Community-pressure events (R-DS9) | Candidate durable-demand corroborator when pressure persists past its trigger | Coordination check (organic collective vs brand-seeded campaign, D2) | source-family-adapted-satellite |
| SU-B5 | Complaint/churn reports (R-DS8) | Counterevidence channel — carried into the read, never dropped upstream (capture/cleaning may not exclude; exclusion is Judgment's) | Incentive check (competitor-seeded complaint waves exist in beauty) | source-family-adapted-satellite |

## 3. Distortion-Manifestation Taxonomy

Owner seed list (verbatim, 2026-06-12): *paid amplification,
copied/coordinated content, incentive bias, review stuffing, trend-chasing,
platform artifact, affiliate contamination.*

The core Signal Integrity vocabulary this satellite maps onto — per the thesis
value proposition — is *artificial-amplification risk*, *incentive
distortion*, *copied/coordinated*. The core **Signal Integrity registry shape
and the Integrity Effect Rule are core-owned; the registry is reserved and
unbuilt.** Everything below is a satellite-grade candidate manifestation
vocabulary: what each distortion *looks like* per beauty-relevant source
family, so a future Judgment-owned registry can consume it. No integrity
effect, discount, or exclusion semantics are defined here.

Beauty-relevant source families used below: **review sites** (retailer and
standalone review surfaces), **forums/Reddit**, **social/video**
(TikTok/IG/YouTube), **retail listings** (PDP state: price, badges, rank,
availability).

| Rule | Seed distortion | Core label mapped | Manifestations per source family (satellite-grade) | Tag |
| --- | --- | --- | --- | --- |
| R-DM1 | Paid amplification | artificial-amplification risk | Social/video: boosted posts and Spark-Ads-style placements indistinguishable from organic in capture; synchronized creator waves at launch. Retail listings: sponsored search rank captured as organic-looking placement. Forums: undisclosed sponsored AMAs/posts. Review sites: paid review-collection drives. | source-family-adapted-satellite |
| R-DM2 | Copied/coordinated content | copied/coordinated | Forums/Reddit: astroturf accounts with template phrasing; vendor-managed discount threads (already a named example in the core promotion rule). Social/video: caption/script reuse across unaffiliated-looking accounts. Review sites: near-identical review text across products or profiles. | source-family-adapted-satellite |
| R-DM3 | Incentive bias | incentive distortion | Review sites: "received free for honest review," rebate-card-in-box reviews. Social/video: PR-box/gifted-creator content (disclosed or not). Forums: brand-affiliated mods or seeded "routines." Retail listings: incentivized-review badges and sweepstakes programs. | source-family-adapted-satellite |
| R-DM4 | Review stuffing | artificial-amplification risk + incentive distortion (compound) | Review sites/retail listings: burst-shaped arrival of near-duplicate five-star reviews at launch or after a viral event; rating distribution snapping bimodal; review count outrunning plausible buyer base. | source-family-adapted-satellite |
| R-DM5 | Trend-chasing | **no clean core label — candidate `organic_herding_inflation`** | Social/video: sound/format herding where creators chase a trend for reach, inflating mention counts without buyer intent; copycat "dupe of X" content waves. Forums: bandwagon threads recycling the same claim. Distinct from R-DM1/R-DM2: no artificial actor and no coordination — the inflation is organic incentive-following. The durable-vs-hollow consequence is Judgment's; only the manifestation marker is satellite. | unresolved-candidate |
| R-DM6 | Platform artifact | **partially artificial-amplification; candidate `platform_mechanics_artifact`** | Review sites: cross-retailer review syndication (same review legitimately republished — see R-DH1). Retail listings: "bestseller"/"trending" badges driven by paid placement or category-tree quirks; counterfeit/gray-market sellers consolidated onto one listing polluting its review pool (beauty-specific and common). Social/video: algorithmic redistribution spikes unrelated to demand. Forums: repost bots, mod removals deleting context. | unresolved-candidate |
| R-DM7 | Affiliate contamination | incentive distortion (sub-kind) | Social/video: LTK/storefront links, TikTok Shop commission content. Forums/Reddit: link-laden "routine" posts and comment-section affiliate drops. Review sites: reviewer profiles funneling to affiliate blogs. Retail listings: affiliate-driven Q&A seeding. | source-family-adapted-satellite |

### Satellite Disambiguation Heuristics

- **R-DH1 — syndication is not coordination** (review sites): identical review
  text appearing across retailer properties is, by default, platform
  syndication (R-DM6), not copied/coordinated content (R-DM2). Treating
  syndication as coordination would manufacture false integrity flags at scale
  in beauty, where retailer syndication networks are standard. Tag:
  **source-family-adapted-satellite** (review-sites family only; promotion
  would require survival in a second non-overlapping family).
- **R-DH2 — gifted-wave is incentive, not coordination** (social/video): a
  synchronized burst of creator content following a PR-box drop manifests
  *incentive distortion* (R-DM3) even though its shape resembles coordination
  (R-DM2); the actors are independent but identically incentivized. Tag:
  **source-family-adapted-satellite**.
- **R-DH3 — disclosure markers are capture-visible observables** (cross-family):
  explicit incentive-disclosure tokens — "gifted," "#ad," "affiliate link,"
  retailer incentivized-review badges — are observable in the captured source
  itself and manifest in at least two non-overlapping source families (review
  sites; social/video). Tag: **source-invariant-core-candidate** — declared,
  not promoted; see PC-1 in the ledger.

## 4. Source-Family Notes (Categorical Only)

Relevance, blind spots, and capture-feasibility constraints at a categorical
level. No capture plans, no source inventory, no scraper design; capture
method, access boundaries, and anti-blocking posture stay owned by the Data
Capture Spine lane and its existing decisions — this section consumes that
boundary and adds vertical context only.

- **Review sites.** Relevance: the densest costly-behavior text (verified
  purchase, repurchase, switching language) and ground zero for R-DM3/R-DM4.
  Blind spots: post-purchase only (no funnel top); syndication duplicates
  (R-DH1); platform-side review suppression/removal invisible at capture;
  incentivized-program skew. Feasibility constraints (categorical): listing
  and review state is volatile, so the core timing/cutoff discipline carries
  the load — consumed, not redefined.
- **Forums/Reddit.** Relevance: richest workaround/switching/complaint texture
  (R-DS5/7/8) and earliest community-pressure signals (R-DS9); the thesis's
  subtle-decision class (quiet reformulations, silent SKU kills) surfaces here
  before trade-press laundering. Blind spots: demographic skew; small-n
  enthusiast bias; deletion/edit decay; vendor-managed-thread astroturf
  (R-DM2). Feasibility constraints (categorical): existing Reddit capture
  ordering and boundaries apply unchanged.
- **Social/video.** Relevance: earliest attention/trigger signals (R-DS1,
  R-DS10b) and the primary habitat of R-DM1/R-DM3/R-DM5/R-DM7. Blind spots:
  paid/organic indistinguishability at capture (the defining limitation —
  manufactured-vs-organic separation is forward/live with cross-signal
  consistency as a partial flag, per the thesis); ephemerality; algorithm
  opacity (R-DM6). Feasibility constraints (categorical): media-heavy capture
  and platform anti-automation friction; governed by Data Capture lane
  decisions, not this doc.
- **Retail listings.** Relevance: distribution events and competitor moves
  (R-DS4a/4b), price/packaging state, and the residualized availability state
  (CNF-1). Blind spots: badge/rank mechanics are platform artifacts (R-DM6);
  counterfeit-seller review pollution; bundle/dupe listing confusion.
  Feasibility constraints (categorical): high-churn page state → timing/cutoff
  discipline again carries the load.
- **Search-interest surfaces** (supporting family for R-DS2). Relevance:
  funnel-propagation reads (search → reviews → retail per the central read).
  Blind spot: panels are aggregate-by-construction — the slice is an
  indicator state, never a costly behavior; it can route and corroborate but
  not carry commit-tier demand claims (SU-B2).

## 5. Promotion Ledger

Every authored rule in this doc, tagged per the Source-Family Promotion Rule.
Context surfaces (section 1) carry no promotion-bearing rules. Restated core
rules (costly-behavior-over-engagement, exclusion-is-Judgment's,
timing/cutoff discipline) are consumed citations, not authored rules, and do
not appear in this ledger.

| Rule ID | Short name | Tag |
| --- | --- | --- |
| R-DS1 | attention → DEMAND_REACTION / attention_resonance | source-family-adapted-satellite |
| R-DS2 | search → DEMAND_REACTION / search_interest_state | source-family-adapted-satellite |
| R-DS3 | review velocity → DEMAND_REACTION / review_flow_state (single-slice only) | source-family-adapted-satellite |
| R-DS4a | retail distribution event → TRIGGER_TIMING_EVENT | source-family-adapted-satellite |
| R-DS4b | competitor distribution move → COMPETITOR_PRICE_PACKAGING_MOVE | source-family-adapted-satellite |
| R-DS4c | availability state → residualize today | unresolved-candidate |
| R-DS5 | switching report → DEMAND_REACTION / switching_report | source-family-adapted-satellite |
| R-DS6 | repurchase report → DEMAND_REACTION / repurchase_report | source-family-adapted-satellite |
| R-DS7 | workaround report → DEMAND_REACTION / workaround_report | source-family-adapted-satellite |
| R-DS8 | complaint → DEMAND_REACTION / complaint_churn_report | source-family-adapted-satellite |
| R-DS9 | community pressure → DEMAND_REACTION / community_pressure | source-family-adapted-satellite |
| R-DS10a | buyer channel-switch report → DEMAND_REACTION / channel_switch_report | source-family-adapted-satellite |
| R-DS10b | brand/retailer channel event → TRIGGER_TIMING_EVENT / channel_event | source-family-adapted-satellite |
| CNF-1 | candidate fifth family: retail_availability_state | unresolved-candidate |
| SU-B1 | costly-behavior reports as candidate decide-support | source-family-adapted-satellite |
| SU-B2 | attention/search as resonance-only use posture | source-family-adapted-satellite |
| SU-B3 | stuffing-suspect review flow as confirm-only | source-family-adapted-satellite |
| SU-B4 | persistent community pressure as durable-demand corroborator | source-family-adapted-satellite |
| SU-B5 | complaints as carried counterevidence channel | source-family-adapted-satellite |
| R-DM1 | paid amplification manifestations | source-family-adapted-satellite |
| R-DM2 | copied/coordinated manifestations | source-family-adapted-satellite |
| R-DM3 | incentive-bias manifestations | source-family-adapted-satellite |
| R-DM4 | review-stuffing compound manifestations | source-family-adapted-satellite |
| R-DM5 | trend-chasing → candidate organic_herding_inflation label | unresolved-candidate |
| R-DM6 | platform artifact → candidate platform_mechanics_artifact label | unresolved-candidate |
| R-DM7 | affiliate contamination manifestations | source-family-adapted-satellite |
| R-DH1 | syndication-is-not-coordination disambiguation | source-family-adapted-satellite |
| R-DH2 | gifted-wave-is-incentive disambiguation | source-family-adapted-satellite |
| R-DH3 | disclosure markers as capture-visible observables | source-invariant-core-candidate |

### Named Future Two-Family Promotion Candidate

- **PC-1 — disclosed-incentive-marker observation (from R-DH3).** The rule
  "explicit incentive-disclosure tokens present in the captured source are an
  integrity-relevant observable feeding incentive-distortion labeling" already
  manifests in two non-overlapping source families (review sites;
  social/video) and is plausibly source-invariant. It is the owner-actionable
  promotion candidate from this slice: a future owner decision could promote
  it into the core Signal Integrity vocabulary after the two-family comparison
  is actually run (this doc asserts the candidacy, not the survival). Until
  then it remains satellite-held under its core-candidate tag.

No other row is proposed for promotion. CNF-1, R-DM5, and R-DM6 are
unresolved candidates that stay satellite-held (or residualized) pending
either a second-family comparison or an explicit owner exception.

## 6. Non-Claims

- Not validation, readiness, acceptance, buyer proof, or judgment-quality
  evidence. Claim cap is product-learning; authoring vocabulary proves nothing
  about signal quality or judgment quality.
- Not core promotion: no `SignalFamily` enum change, no new spine column, no
  Signal Integrity or Signal Use core registry design — the registry shapes
  remain core-reserved and unbuilt; this doc proposes candidate contents only.
- Not Evidence Unit architecture work (owner-reserved), not JSG gate work, not
  ECR/SCR deriver or schema change, not capture plans, not a source inventory,
  not scraper or anti-blocking design, not implementation authorization of any
  kind.
- Not a second satellite, not ontology code, not beauty case fixtures.
- Zero-spoiler discipline honored: no Beauty Pie capture or sourcing informs
  this doc; sealed outcome artifacts were not opened.
- The `family_detail` values listed are candidate vocabulary for the empty v0
  extension slot; nothing here asserts they are adopted, typed, or built.

## Direction Change Propagation

```yaml
direction_change_propagation:
  doctrine_changed: >
    Orca gains its first vertical satellite doctrine artifact: beauty-vertical
    decision-family context, demand-semantics signal rows mapped onto the
    existing SCR signal_family / family_detail seam (one explicitly unpromoted
    candidate family residualized), a distortion-manifestation taxonomy held
    as satellite-grade Signal Integrity candidates, categorical source-family
    notes, and a promotion ledger with one named two-family promotion
    candidate — all bounded by the Core-vs-Satellite contract; no core
    invariant, enum, registry shape, or layer rule is changed.
  trigger: product_doctrine
  related_triggers: []
  controlling_sources_updated:
    - docs/product/beauty_vertical_satellite_v0.md
  downstream_surfaces_checked:
    - path: docs/product/core_spine/core_spine_v0_data_and_cleaning_spine_boundary_v0.md
      note: "Satellite operates inside its Core Vs Satellite + promotion-rule contract, which already anticipates satellites-before-core; no edit required."
    - path: docs/product/signal_content/core_spine_v0_signal_content_record_architecture_v0.md
      note: "family_detail seam consumed exactly as designed (vertical richness in values, no new columns); no edit required."
    - path: orca-harness/signal_content/models.py
      note: "Read-only check: SignalFamily unchanged; candidate families correctly degrade to RESIDUAL_FAMILY_UNRESOLVED."
    - path: docs/workflows/ecr_spine_submap_v0.md
      note: "No stale_if condition triggered: no new derived-record kind, no discipline change; no edit required."
    - path: AGENTS.md
      note: "No global behavior or routing rule changed; no edit required."
    - path: .agents/workflow-overlay/README.md
      note: "No overlay authority changed; no edit required."
  intentionally_not_updated:
    - path: docs/workflows/orca_repo_map_v0.md
      reason: >
        Coordinator-owned routing surface; registering the new satellite row is
        flagged for the coordinator (this lane's edit permission is
        single-target docs-write). Until registered, this doc is reachable via
        docs/product/ placement rules and the handoff prompt's stale_if pointer.
  stale_language_search: >
    not_run — purely additive new artifact; no existing rule is re-worded,
    superseded, or forked by this change.
  non_claims:
    - "not validation"
    - "not readiness"
    - "not core promotion or registry design"
    - "not implementation authorization"
```
