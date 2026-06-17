# Judgment Level 1 Product-Learning Core Minimum v0

```yaml
retrieval_header_version: 1
artifact_role: Judgment Spine product artifact (Level 1 product-learning core minimum)
scope: >
  Defines the reusable market-agnostic Level 1 product-learning minimum that
  satellites must consume before they fill domain-specific case, source,
  evidence, weighting, forecast, decision, reveal, lesson, or receipt slots.
use_when:
  - Deciding what core Judgment pieces a Level 1 satellite may rely on.
  - Checking which Level 1 pieces are still missing or blocked before case admission or run planning.
  - Preventing fragrance or another satellite from owning claim tiers, gate semantics, run authorization, scoring, or proof claims.
open_next:
  - docs/product/judgment_spine/judgment_current_state_and_decomposition_v0.md
  - docs/product/judgment_spine/judgment_spine_evidence_ladder_architecture_v0.md
  - docs/product/judgment_spine/judgment_quality_promotion_operating_model_v0.md
  - docs/product/judgment_spine/judgment_spine_gate_ownership_map_v0.md
  - docs/research/judgment-spine/judgment_spine_machinery_build_state_gap_map_v0.md
  - docs/product/judgment_spine/fragrance_level1_product_learning_satellite_skeleton_v0.md
branch_or_commit: >
  Authored on dependent branch codex/judgment-level1-core-minimum based on
  PR #230 head dec37f13cd63a8e683aafeca7851f700e1f0c064.
stale_if:
  - PR #230 changes before landing and this dependent branch is not rebased and reread.
  - The evidence ladder changes claim tiers, closeout states, receipt minima, or promotion gates.
  - The conductor changes its no-authority invariant, by-hand cap, JSG routing, or run authorization boundary.
  - The gate ownership map changes JSG ownership, receipt ownership, or blocked-claim boundaries.
  - The build-state gap map changes blind-execution, real-run, JSG-01 binding, source/evidence binding, or case-finder status.
  - A Level 1 satellite admits a named case, completes a product-learning receipt, or receives source-capture/run/scoring authorization.
authority_boundary: retrieval_only
```

## Status

This is a docs-only product-learning core-minimum artifact. It names the
minimum reusable Level 1 surface that satellites should consume by pointer. It
does not run a case, admit a case, authorize source capture, authorize model
execution, authorize scoring, or promote any claim.

Claim cap for this artifact: `unreceipted_product_learning_context`.

This artifact depends on PR #230 landing first. If PR #230 changes before this
dependent lane lands, rebase or recreate the dependency, then rerun the source
load against the new PR head before using this artifact.

## Source-Loading Surface

Purpose: give future Level 1 satellites a compact market-agnostic checklist for
what must live in Judgment core and what may be filled by a domain satellite.

Use when:

- starting a Level 1 satellite after current-state/decomposition;
- checking whether a satellite can move from organizer slots toward case
  admission or product-learning receipt work;
- reviewing whether a satellite is trying to own core Judgment semantics.

Do not use for:

- claim-tier definitions or closeout vocabulary;
- JSG gate semantics, predicate changes, or run lifecycle changes;
- source-capture authority, packet-grade evidence capture, or ECR/Cleaning work;
- named-case admission, run authorization, model execution, scoring, buyer
  proof, validation, fixture admission, readiness, or judgment-quality claims.

Authority boundary: this artifact routes to the owner sources. If it disagrees
with the evidence ladder, conductor, gate ownership map, build-state gap map,
source-capture owners, or a case-specific accepted artifact, the owner source
wins and this artifact is stale for that point.

Recheck recipe:

1. Confirm the branch still descends from the intended PR #230 head or a landed
   descendant.
2. Open the Judgment consolidation map first.
3. Open the evidence ladder for claim caps and receipt minima.
4. Open the conductor for routing, no-authority discipline, by-hand cap, and run
   lifecycle.
5. Open the gate ownership map for gate owners and blocked-claim boundaries.
6. Open the build-state gap map before any built-vs-gap or run-executability
   claim.
7. Open the relevant satellite artifact before saying what a satellite has
   already filled.

## Core Minimum

The Level 1 product-learning core minimum is the smallest reusable Judgment
surface a satellite must be able to point at before it treats its domain fields
as more than organizer slots.

It is not the entire Judgment core. It is not a harness build plan. It is not a
case runner. It is the minimum reusable contract that keeps a Level 1 satellite
from inflating its case, source, forecast, decision, reveal, lesson, or receipt
fields into stronger claims.

| Core piece | Owner source | Minimum Level 1 role | Satellite may fill | Satellite must not own |
| --- | --- | --- | --- | --- |
| Claim cap and closeout vocabulary | Evidence ladder | Classify the surface as product-learning context, completed product-learning evidence, or a lower/blocked state by owner vocabulary | A case-specific classification or receipt pointer | Claim tiers, closeout states, promotion gates |
| Product-learning receipt minimum | Evidence ladder | Provide the minimum fields for completed product-learning evidence | Case ID, prompt/answer handle, owner readback, product/friction signals, non-claims | Buyer-proof or judgment-quality receipt fields |
| Gate route and no-authority discipline | Conductor | Keep JSG-01 through JSG-10 as owner-routed gates and prevent the conductor or satellite from self-clearing gates | Pointers to case-specific receipts when they exist | Gate predicates, run lifecycle semantics, model/run/scoring authorization |
| Gate ownership and blocked-claim boundaries | Gate ownership map | Identify who owns each JSG receipt and which stronger claims are blocked if missing | Case-specific missing-gate notes | Gate ownership or receipt semantics |
| Build/run executability state | Build-state gap map | Separate built plumbing from missing execution/case-finder/run surfaces | A case-specific gap note after reread | Readiness, validation, or run-executability claims |
| Case admission boundary | Current-state/decomposition plus satellite casebook frame | Require a separate named-case admission record before a candidate becomes admitted | Domain case ID, cutoff, source families, outcome label plan, benchmark policy | Fixture admission, run authorization, or source-capture authority |
| Source/evidence boundary | Source-capture owners plus JSG-01 owners by pointer | Keep source family hints and evidence packet plans separate from source authority | Candidate venues, source-family notes, provenance plan, held/prohibited sources | Capture authority, source-family admission, ECR clearance, packet validity |
| Qualitative demand read | Current-state C0-C4 pointers, especially C1/C2/C3 owner surfaces | Keep allow, qualitative weighting, and verdict/action ceiling market-agnostic | Domain signal IDs, qualitative direction, caveats, no-row handling, action examples mapped onto owner vocabulary | Numeric weights, formulas, scores, new action vocabulary |
| Forecast/reveal/lesson loop | Current-state decomposition, JSG-08 owner contract, near/far learning surfaces by pointer | Treat forecasts and reveals as learning inputs, not proof of judgment quality | Forecast field, measurement window, reveal comparison, candidate lessons | Calibration, proof, validated lessons, or outcome-as-score claims |
| Non-claims and promotion guard | Evidence ladder, conductor, gate map | Keep every Level 1 artifact capped until receipts and gates exist | Domain-specific non-claims and blocker notes | Buyer proof, product proof, readiness, scoring authorization, judgment-quality evidence |

## What Current Judgment Already Provides

The current source-loaded Judgment surface provides these reusable core pieces:

- The evidence ladder owns claim tiers, closeout states, weakest-cleared-gate
  discipline, and minimum receipt fields.
- The conductor owns routing through JSG-01 to JSG-10, the no-authority
  invariant, the route-don't-restate rule, run lifecycle labels, and the
  by-hand cap.
- The gate ownership map owns gate-owner routing and names which stronger
  claims are blocked when required gate receipts are missing.
- The build-state gap map records the current built-vs-gap inventory: scoring,
  memorization probe, schemas/reports/tests, ECR derivers, SP-5 finalizer, and
  JSG-01 binding are recorded there as built; blind-judgment contestant
  execution under proven isolation, an authorized real non-synthetic run, and
  the case-finder remain recorded gaps.
- The current-state/decomposition artifact owns the core/satellite split and
  keeps fragrance as a satellite, not the core.
- The fragrance satellite skeleton and casebook frame reserve domain slots but
  do not admit named cases or authorize execution.

## What Remains Missing Or Blocked

These are blockers for treating any Level 1 satellite case as run-ready or
proof-bearing:

- No named Level 1 fragrance case is admitted by the current fragrance artifacts.
- No satellite has a case-specific captured evidence packet or source-capture
  authority by this artifact.
- No authorized real non-synthetic run is recorded by this artifact.
- Blind-judgment contestant execution under proven isolation remains a recorded
  gap in the build-state gap map.
- No completed Level 1 `product_learning_receipt` exists for any fragrance case
  in this lane.
- No buyer-proof receipt or judgment-quality receipt exists for this Level 1
  slice.
- PR #230 must land or be otherwise incorporated before this dependent branch is
  treated as mainline-reachable.

Missing evidence is a cap, not a pass. A satellite may use the gaps to plan the
next docs-only slice, but it must not convert them into readiness, validation,
proof, or run authority.

## Satellite Fill Contract

A Level 1 satellite may fill only domain-specific instances:

- casebook candidates and later named-case admission records;
- domain source-family notes and source-plan fields;
- case-specific evidence references and provenance notes;
- C1/C2/C3 domain reads that preserve owner vocabulary and caveats;
- forecast, decision, reveal, evaluation, and lesson fields as learning inputs;
- product-learning receipt fields when the minimum receipt can be satisfied;
- domain-specific non-claims and blocker notes.

A Level 1 satellite must not fill or redefine:

- claim tiers, closeout states, promotion gates, or receipt minima;
- JSG gate semantics, predicates, ownership, or run lifecycle states;
- no-tools, memorization-probe, sealed-output, scoring, or reveal/calibration
  gate-clearance rules;
- source-capture authority or ECR/Cleaning handoff obligations;
- numeric weighting, scoring, formulas, or deterministic apply rules;
- C3 action vocabulary beyond mapping domain examples onto the owner vocabulary;
- buyer-proof, product-proof, readiness, validation, fixture-admission,
  scoring, blind-use, run authorization, or judgment-quality claims.

## Minimum Per-Case Progression

Use this as a Level 1 progression checklist, not as execution authorization.

| State | Minimum durable artifact | Strongest claim before next state |
| --- | --- | --- |
| Candidate | Candidate screen, queue, or casebook row | Product-learning context only |
| Admitted for Level 1 attempt | Named-case admission record with all admission-minimum fields | Case admitted for learning setup only; no capture/run authority |
| Source/evidence plan bounded | Source/evidence plan that points to source-capture owners and names prohibited/held sources | Product-learning planning context only |
| Evidence packet available | Captured packet or evidence object admitted by the owning source/capture/JSG-01 route | At most the owner-cleared source/evidence state; no run claim by itself |
| Qualitative read and decision sealed | C1/C2/C3 trace and forecast/decision record sealed before reveal when evaluation is intended | Product-learning process context unless receipt completed |
| Reveal/eval recorded | Outcome/reveal comparison under the JSG-08 owner boundary | Learning input; not calibration or judgment-quality by itself |
| Product-learning receipt complete | Evidence-ladder `product_learning_receipt` minimum fields complete | Completed product-learning evidence only |

Any state that lacks its named durable artifact remains at the weaker prior
state or `unknown`.

## Claim Classification

```yaml
judgment_spine_claim_classification:
  evaluated_claim_surface: judgment_level1_product_learning_core_minimum_v0
  source_quality_state: >
    docs-only market-agnostic core-minimum artifact derived from the current
    Judgment source pack and dependent on PR #230 head dec37f13.
  execution_quality_state: >
    no admitted case, no captured case-specific evidence packet, no sealed
    answer, no model execution, no scoring, no reveal comparison, and no
    completed product-learning receipt.
  closeout_state: unreceipted_product_learning_context
  claim_cap: product-learning context only
  weakest_missing_or_failed_gate:
    - no case-specific product_learning_receipt
    - no admitted named Level 1 case by this artifact
    - no source-capture authority or captured evidence packet by this artifact
    - no authorized real run by this artifact
    - no buyer_proof_receipt
    - no judgment_quality_receipt
  receipt_artifact_or_gap: >
    This artifact is setup context. Future per-case product-learning receipts
    remain required before completed product-learning evidence can be claimed.
  non_claims:
    - not validation
    - not readiness
    - not buyer proof
    - not product proof
    - not source-capture authority
    - not run authorization
    - not scoring authorization
    - not fixture admission
    - not judgment-quality evidence
```

## Next Docs-Only Moves

After this core minimum is map-reachable and PR #230 is accounted for, the next
useful docs-only moves are:

1. Admit-attempt packet for the first named fragrance case, still with no source
   capture or run authorization.
2. Fragrance source/evidence plan that points to source-capture owners rather
   than claiming source authority.
3. Per-case product-learning receipt template or first receipt only after a
   named case and evidence plan are bounded.

Do not broaden the fragrance skeleton before the case admission and source
boundary blockers are resolved.

## Non-Claims

This artifact is not validation, readiness, buyer proof, product proof,
judgment-quality evidence, source-capture authority, prompt approval, run
authorization, scoring authorization, fixture admission, accepted benchmark,
completed product-learning evidence, owner adoption of any fragrance case, or
proof that a Level 1 satellite works.

It does not change the evidence ladder, conductor, gate ownership map,
build-state gap map, source-capture owners, or fragrance satellite artifacts. It
only names the minimum core surface a satellite must consume without claim
inflation.

## Direction Change Propagation

```yaml
direction_change_propagation:
  doctrine_changed: >
    Level 1 product-learning satellites now have a reusable Judgment core-minimum
    product organization layer: before a satellite fills domain-specific case,
    source, evidence, weighting, forecast, decision, reveal, lesson, or receipt
    slots as more than organizer context, it must consume the market-agnostic
    core pieces named here by pointer. This changes product-learning routing for
    Level 1 satellites only; it does not change claim tiers, closeout states,
    conductor routing, JSG gate ownership, source-capture authority, scoring,
    run authorization, buyer proof, readiness, or judgment-quality evidence.
  trigger: product_doctrine
  related_triggers:
    - architecture_doctrine
  controlling_sources_updated:
    - docs/product/judgment_spine/judgment_level1_product_learning_core_minimum_v0.md
    - docs/product/judgment_spine/judgment_current_state_and_decomposition_v0.md
    - docs/research/judgment-spine/judgment_spine_consolidation_map_v0.md
    - docs/workflows/orca_repo_map_v0.md
  downstream_surfaces_checked:
    - AGENTS.md
    - .agents/workflow-overlay/README.md
    - .agents/workflow-overlay/source-of-truth.md
    - .agents/workflow-overlay/source-loading.md
    - .agents/workflow-overlay/decision-routing.md
    - .agents/workflow-overlay/validation-gates.md
    - docs/product/judgment_spine/judgment_spine_evidence_ladder_architecture_v0.md
    - docs/product/judgment_spine/judgment_quality_promotion_operating_model_v0.md
    - docs/product/judgment_spine/judgment_spine_gate_ownership_map_v0.md
    - docs/research/judgment-spine/judgment_spine_machinery_build_state_gap_map_v0.md
    - docs/product/judgment_spine/fragrance_level1_product_learning_satellite_skeleton_v0.md
    - docs/product/judgment_spine/fragrance_level1_casebook_admission_frame_v0.md
    - docs/product/judgment_spine/fragrance_level1_named_case_candidate_screen_v0.md
  intentionally_not_updated:
    - path: docs/product/judgment_spine/judgment_spine_evidence_ladder_architecture_v0.md
      reason: >
        Claim tiers, closeout states, promotion gates, and receipt minima are
        unchanged and are consumed by pointer.
    - path: docs/product/judgment_spine/judgment_quality_promotion_operating_model_v0.md
      reason: >
        Conductor routing, no-authority discipline, by-hand cap, and run
        lifecycle states are unchanged and are consumed by pointer.
    - path: docs/product/judgment_spine/judgment_spine_gate_ownership_map_v0.md
      reason: >
        JSG gate ownership and blocked-claim boundaries are unchanged and are
        consumed by pointer.
    - path: docs/research/judgment-spine/judgment_spine_machinery_build_state_gap_map_v0.md
      reason: >
        Built-vs-gap state is unchanged; this artifact only points to that map
        before any run-executability claim.
    - path: docs/product/judgment_spine/fragrance_level1_product_learning_satellite_skeleton_v0.md
      reason: >
        The fragrance satellite remains a domain organizer. The core-minimum
        artifact sits above it and does not change its slots.
    - path: docs/product/judgment_spine/fragrance_level1_casebook_admission_frame_v0.md
      reason: >
        The casebook admission frame remains the owner of the 25-slot shape and
        named-case admission minimum. No named case is admitted here.
    - path: docs/product/judgment_spine/fragrance_level1_named_case_candidate_screen_v0.md
      reason: >
        Candidate ranking remains unchanged. This artifact does not select or
        admit a named case.
  stale_language_search: >
    rg -n "Level 1 product-learning continuation handoff|judgment_level1_product_learning_core_minimum_handoff_v0|Level 1 product-learning core minimum|core-minimum docs slice"
    docs/product/judgment_spine docs/research/judgment-spine docs/workflows/orca_repo_map_v0.md
  stale_language_search_result: >
    Executed 2026-06-17 after the patch. The old specific handoff pointer and
    "core-minimum docs slice" wording no longer appear in live Judgment route
    surfaces. Hits are the new repo-map route, the consolidation-map route and
    section, the current-state route, and this new artifact.
  non_claims:
    - not validation
    - not readiness
    - not buyer proof
    - not product proof
    - not source-capture authority
    - not implementation authorization
    - not run authorization
    - not scoring authorization
    - not fixture admission
    - not judgment-quality evidence
```

## Source-Read Ledger

- Current user instruction: continue from `codex/judgement-lane` at
  `dec37f13cd63a8e683aafeca7851f700e1f0c064`; create or reset dependent
  branch; rerun confirm-don't-trust; do not merge or close PR #230.
- `AGENTS.md`
- `.agents/workflow-overlay/README.md`
- `.agents/workflow-overlay/source-of-truth.md`
- `.agents/workflow-overlay/source-loading.md`
- `.agents/workflow-overlay/decision-routing.md`
- `.agents/workflow-overlay/retrieval-metadata.md`
- `.agents/workflow-overlay/artifact-folders.md`
- `.agents/workflow-overlay/validation-gates.md`
- `docs/workflows/artifact_retrievability_guide.md`
- `docs/workflows/orca_repo_map_v0.md`
- `docs/research/judgment-spine/judgment_spine_consolidation_map_v0.md`
- `docs/research/judgment-spine/judgment_spine_machinery_build_state_gap_map_v0.md`
- `docs/product/judgment_spine/judgment_current_state_and_decomposition_v0.md`
- `docs/product/judgment_spine/judgment_quality_promotion_operating_model_v0.md`
- `docs/product/judgment_spine/judgment_spine_evidence_ladder_architecture_v0.md`
- `docs/product/judgment_spine/judgment_spine_gate_ownership_map_v0.md`
- `docs/product/judgment_spine/fragrance_level1_product_learning_satellite_skeleton_v0.md`
- `docs/product/judgment_spine/fragrance_level1_casebook_admission_frame_v0.md`
- `docs/product/judgment_spine/fragrance_level1_named_case_candidate_screen_v0.md`
