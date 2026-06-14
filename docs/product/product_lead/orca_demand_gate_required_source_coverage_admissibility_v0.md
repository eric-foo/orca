# Orca Demand-Gate Required-Source-Coverage Admissibility Model v0

```yaml
retrieval_header_version: 1
artifact_role: Product artifact (criteria decision — source-coverage admissibility dimension for the live Demand-Substrate Hard Gate; owner-ratified 2026-06-14)
scope: >
  Defines the required-source-coverage admissibility model for the live
  Demand-Substrate Hard Gate and its gate-run commission criteria: the required
  demand-source-family set, the tier rule resolving Seam 1 (when >=2 independent
  origins unlock material action), the "insufficient coverage = no material
  judgment" rule, the consciously-accepted origin-starvation consequence, a
  hard-walled backtest carve-out, and the Seam 2 (insufficient-input vs fail)
  clarification. Criteria only — qualitative / LLM-in-session; NOT a scoring
  engine and NOT the sourcing build.
use_when:
  - Deciding whether a candidate's demand-source coverage suffices, and at which tier, before or during a gate-run.
  - Reading or amending how the Demand-Substrate Hard Gate gates the material-action tier on source-family coverage.
authority_boundary: retrieval_only
status: OWNER_RATIFIED_2026-06-14 (material-action-only gating; >=2-of-3 required families) — criteria only; not validation/readiness/buyer-proof/gate-clearance
open_next:
  - docs/product/product_lead/orca_buyer_proof_packet_v0.md            # Demand-Substrate Hard Gate (controlling gate logic)
  - docs/product/product_lead/orca_demand_gate_run_commission_criteria_v0.md  # how the gate is run
  - docs/product/product_lead/orca_demand_gate_definition_closures_proposal_v0.md  # ratified P2/P3/P4 (NOT reopened)
```

## Status And Ratification

Owner-ratified in-thread 2026-06-14 (two-question sign-off):

1. Coverage-insufficiency gates the **material-action tier only** — the gate keeps
   rendering hold / low-commitment reads on a single sourced demand family.
2. The required coverage threshold is **>=2 of the 3** named demand-source families.

This artifact encodes those decisions and is the controlling source for the
gate's **source-coverage admissibility** dimension. The live gate, the gate-run
commission criteria, and the discovery brief reference it.

It is a **ratified criteria decision** — not validation, readiness, buyer proof,
or gate clearance for any candidate. It is **not a scoring engine** (weighting
stays qualitative / LLM-in-session) and **not the sourcing build** (it DEFINES
required coverage; it does not implement review / search / social sourcing).

## Why This Exists (the seam it closes)

The live gate (re-derived 2026-06-12; P2/P3/P4 amendments applied 2026-06-14)
sets independence as **de-correlation by origination** and verb-tiers the
ceiling: one independent origin -> hold / low-commitment; >=2 converging
independent origins -> material action. A 10-case blind dry-run surfaced an
ambiguity (**Seam 1**) the gate text does not resolve: must the ">=2 independent
origins" required for material action come from >=2 distinct **source-families**
(review-surface / forums-community / search-interest), or can >=2 de-correlated
**origination lineages within one family** suffice? In the dry-run, the only case
to reach material action (a consumer subreddit + a separate professional forum)
did so solely under the within-one-family reading. This model resolves it.

(The dry-run used fabricated fixtures and is orientation only — never buyer proof.)

## The Two Axes (the load-bearing distinction)

Resolving Seam 1 by redefining a per-candidate "independent origin" to require
distinct families would contradict ratified **P2** ("independence is
de-correlation by origination, **not a raw venue count**"), which this lane must
not reopen. The resolution therefore lives on a **separate axis** from P2:

- **Axis 1 — per-candidate origin de-correlation (P2; LIVE; UNCHANGED here).**
  Within one candidate's evidence, independent origins are counted by origination
  lineage (no shared origination ancestry; laundered / shared-origination copies
  collapse to one). Two de-correlated lineages may sit inside one family. This is
  ratified and is not touched.
- **Axis 2 — source-coverage admissibility (NEW; this model).** How many of the
  required demand-source families are even **sourced** (have a maintained venue
  card-set able to produce provenance-noted demand signal), plus the requirement
  that a **material**-tier read's converging origins **span >=2 sourced families**.
  This is where "we need all these sources, else no judgment" lives, and it is
  what this model adds.

The owner's robustness intent and Seam 1 are both satisfied on Axis 2 **without
altering P2's per-candidate counting on Axis 1**.

## Required Demand-Source-Family Set

The required set is the three named **G1 demand families**:

1. review-surface
2. forums / community
3. search-interest

Retail presence is **G4 org-motion corroboration** (already excluded from the G1
origin count; unchanged). "**Sourced**" means the family has a maintained venue
card-set able to yield provenance-noted demand signal for the candidate's
category; building those card-sets is a **capture-lane** decision, out of scope
here. **Today only forums / community is sourced**; review-surface and
search-interest are owner-owned **unsourced gaps**.

## Seam 1 Resolution + Coverage-Admissibility Tier Rule (material-action only)

- **Hold / low-commitment tier — admissible on ONE sourced required family.**
  Unchanged from the live gate's "single clean origin -> hold (ceiling cap, not
  gate failure)." Within-family de-correlated lineages (Axis 1) strengthen the
  single-family read and may raise confidence within this tier, but do **not** by
  themselves unlock material action.
- **Material-action tier — admissible only when BOTH hold:**
  - (a) **Coverage prerequisite:** >=2 of the 3 required demand families are
    **sourced**; AND
  - (b) **Cross-family convergence:** the candidate shows >=2 converging
    independent origins (Axis 1 de-correlation) that **span >=2 of those sourced
    families**.

  Two de-correlated lineages inside a single family satisfy Axis 1 but **fail
  (b)** — they share that family's manipulation surface (e.g., coordinated
  cross-thread astroturf), which is exactly what a material / irreversible
  commitment on a manipulable substrate must not rest on. This **resolves Seam 1
  against the within-one-family reading for the material tier**, while leaving the
  hold tier and P2's general counting untouched.
- **Floor unchanged.** The G2 gradeable-costly-behavior floor (>=1 gradeable
  instance in >=1 qualifying family) and the divergence defeater are prerequisites
  at every tier and are not changed by this model.

This **formalizes how to require coverage** — the openness P2 deliberately left
at "enough independent origins for the commitment claimed" — and does not reopen
P2 / P3 / P4 or re-decide whether to have verb-tiering.

## Insufficient Coverage = No Material Judgment

When the coverage prerequisite (a) is not met — fewer than 2 required demand
families sourced — the gate is **inadmissible for the material-action tier**: it
must **not** return `admit @ material-action` for any candidate, no matter how
strong the within-family evidence. The verdict is **capped at hold** (`admit @
hold` when the floor + named owner + consequence hold, else `hold`). This is:

- **not `fail`** — the candidate's substrate may be perfectly real; the limit is
  the gate's sourcing maturity, not the candidate; and
- **not `insufficient-input`** — that verdict is about a specific scan missing
  required fields (see Seam 2), not about source-family coverage.

It is a **ceiling cap by source-coverage**, recorded with a one-line basis
("material ceiling capped: only N<2 required demand families sourced"). The
existing verdict set `{admit @ <ceiling>, hold, fail, insufficient-input}` is
unchanged; coverage-insufficiency caps the ceiling within it.

## Origin-Starvation Consequence (named and consciously accepted)

Direct consequence of the ratified rule: **until a 2nd required demand family is
sourced, the gate cannot render a material-action verdict for ANY candidate** —
every material / irreversible allocation call is dark, and the best attainable
verdict is hold. This is the deliberate price of robustness on a manipulable
substrate (a material call must survive across >=2 independent families, which is
uncheckable while only one family is sourced). It is **accepted, not a defect**.
The gate **remains productive at the hold tier now**. Lifting the starvation is a
**capture-lane** action (source a 2nd required family), never a per-candidate or
per-proof stretch.

## Backtest Carve-Out (hard-walled; anti-leak)

A backtest / historical replay MAY relax the coverage prerequisite **only** when
archives genuinely cannot supply >=2 families for the period under study, and
only under ALL of:

- it runs at **`product_learning` tier** (method calibration), never
  `buyer_proof`, and never emits a live `admit`;
- the coverage gap is **documented** inline (which families were unavailable and
  why — a best-available-substrate note);
- it **never lowers the live bar**: a live gate-run with <2 sourced families still
  caps at hold regardless of any backtest relaxation;
- the relaxation is **logged and hard-walled** — it cannot propagate into a live
  gate-run, a discovery slot, or any buyer-facing claim.

The carve-out exists so method-learning can proceed on thin historical substrate
**without ever creating a fake-success live path**. A backtest "material" finding
on relaxed coverage is a method observation, not live admissibility.

## Seam 2 Clarification (insufficient-input vs fail)

Folded into the gate-run for crispness:

- A costly-behavior claim **present but lacking the provenance / gradeability
  fields** needed to assess it (cannot judge attributability-to-buyer-action,
  direction + rough magnitude, or corroborability) -> **`insufficient-input`**:
  the scan must add provenance; the gate does not guess.
- **`fail`** is reserved for when gradeability **can** be assessed and the floor
  is genuinely not met: no costly-behavior instance at all, attention /
  engagement-only signal, the divergence defeater triggers, or signal only via an
  out-of-bounds / absurd-risk route.

That is: "cannot assess" (insufficient-input) is distinct from "assessed and
floor not cleared" (fail).

## Relationship to Ratified P2 / P3 / P4 (not reopened)

- **P2 (independence):** unchanged. Per-candidate independence stays
  de-correlation-by-origination ("not a raw venue count"). This model adds a
  material-tier cross-family-convergence requirement on Axis 2; it does not
  convert the general independence test into a venue count and does not change the
  hold tier.
- **P3 (venue-family binding):** unchanged. The required set is the same named G1
  families; retail stays G4 corroboration.
- **P4 (costly-behavior floor):** unchanged. The gradeable floor is a prerequisite
  at every tier.

## Claim-Tier Classification

Design / criteria-tier `product_lead` decision. Makes no proof, readiness,
validation, scoring, fixture, blind-use, or judgment-quality claim. Per
`.agents/workflow-overlay/product-proof.md` and the evidence-ladder, the
`closeout_state` for any such claim is `no_durable_evidence`.

## Non-Claims

- Criteria only; owner-ratified as a decision, not validation, readiness, buyer
  proof, or gate clearance for any candidate.
- Not a scoring / weighting engine; weighting stays qualitative / LLM-in-session.
- Not the sourcing build; defines required coverage, does not implement sourcing.
- Does not reopen ratified P2 / P3 / P4; does not restate the gate (it adds one
  dimension and references the gate).
- An `admit` under this model is memo-admissibility at a ceiling, nothing more.

## Direction Change Propagation

```yaml
direction_change_propagation:
  doctrine_changed: >
    The Demand-Substrate Hard Gate gains a source-coverage admissibility
    dimension: the material-action tier is admissible only when >=2 of the 3
    required demand-source families are sourced AND the candidate's >=2 converging
    independent origins span >=2 of those sourced families; a single sourced
    family caps every read at hold / low-commitment (origin starvation,
    consciously accepted). Insufficient coverage caps the ceiling (not fail, not
    insufficient-input). Per-candidate origination de-correlation (P2) and the G2
    floor are unchanged. A hard-walled product_learning backtest carve-out may
    relax coverage on genuinely-unavailable archives without lowering the live
    bar. Seam 2 clarified: present-but-ungradeable -> insufficient-input;
    assessed-and-floor-not-met -> fail. Owner-ratified 2026-06-14
    (material-action-only; >=2-of-3).
  trigger: product_doctrine
  controlling_sources_updated:
    - docs/product/product_lead/orca_demand_gate_required_source_coverage_admissibility_v0.md
    - docs/product/product_lead/orca_buyer_proof_packet_v0.md
    - docs/product/product_lead/orca_demand_gate_run_commission_criteria_v0.md
    - docs/product/product_lead/orca_discovery_consumer_demand_target_selection_brief_v0.md
  downstream_surfaces_checked:
    - docs/product/product_lead/orca_demand_gate_definition_closures_proposal_v0.md
    - docs/product/product_lead/orca_demand_read_taxonomy_v0.md
    - docs/workflows/orca_repo_map_v0.md
    - .agents/workflow-overlay/source-loading.md
    - AGENTS.md
  intentionally_not_updated:
    - path: docs/product/product_lead/orca_demand_gate_definition_closures_proposal_v0.md
      reason: >
        Ratified P2/P3/P4 encoding; this model adds a separate coverage axis and
        must not reopen it. Cited as the unchanged per-candidate authority, not
        edited.
    - path: docs/product/product_lead/orca_demand_read_taxonomy_v0.md
      reason: >
        Retail = org-motion classification is unchanged by this model (coverage
        concerns the G1 demand families, not the G4 retail classification). No
        edit owed; cite only.
    - path: >
        the six surfaces flagged in the buyer-proof packet's 2026-06-14 apply
        receipt (charter, offer-hypothesis x2, taxonomy-adjudication, prior
        revision packet, paper-check prompt)
      reason: >
        They carry the OLD "at least two venue families" count — a prior, separate
        reconcile target. They carry no source-coverage admissibility language, so
        they are not residuals for THIS change.
    - path: AGENTS.md and the overlay
      reason: >
        Product doctrine routes through docs/product/product_lead; no root or
        overlay rule changes.
  stale_language_search: >
    rg -li "source-coverage admissibility|required-source-coverage|origin
    starvation|spanning ≥2 sourced|cross-family convergence" docs
  stale_language_search_result: >
    Executed 2026-06-14 after this change (a replacement edit touching the live
    gate's material tier — required, not purely additive). The source-coverage
    terms appear only in the five touched files: the new model, the buyer-proof
    packet (gate), the gate-run commission criteria, the discovery brief, and the
    repo map. The ratified P2/P3/P4 encoding in
    orca_demand_gate_definition_closures_proposal_v0.md is unchanged and
    intentionally retains the Axis-1 verb-tiering wording (≥2 converging origins →
    material) without the coverage qualifier — it is the per-candidate authority
    this model layers on, deliberately not reopened. No other live instrument
    restates the material tier as coverage-independent. The six surfaces flagged
    in the packet's 2026-06-14 apply (charter, offer-hypothesis ×2,
    taxonomy-adjudication, prior revision packet, paper-check prompt) carry the
    older "venue families" count — a separate prior reconcile — and gained no
    coverage language here.
  non_claims:
    - not validation
    - not readiness
    - not buyer proof
    - not gate clearance
    - not a scoring engine
    - not the sourcing build
```
