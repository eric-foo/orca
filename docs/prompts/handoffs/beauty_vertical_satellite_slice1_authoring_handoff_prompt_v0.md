# Beauty Vertical Satellite Doc — Slice 1 Authoring Handoff Prompt v0

```yaml
retrieval_header_version: 1
artifact_role: Prompt artifact (handoff family; documentation-only lane)
scope: >
  Commission one bounded lane to author slice 1 of the Orca beauty vertical
  SATELLITE doctrine doc — decision-family context, demand-semantics signal
  rows, distortion-manifestation taxonomy, promotion ledger, non-claims —
  under the Core-vs-Satellite contract. Doc-only; no code, no captures, no
  core-vocabulary promotion.
use_when:
  - Executing the beauty satellite slice-1 authoring lane.
  - Checking what that lane may produce and must not touch.
authority_boundary: retrieval_only
open_next:
  - docs/product/core_spine/core_spine_v0_data_and_cleaning_spine_boundary_v0.md
  - docs/product/signal_content/core_spine_v0_signal_content_record_architecture_v0.md
stale_if:
  - The slice-1 satellite doc lands (this prompt is consumed).
  - The Core-vs-Satellite contract or Source-Family Promotion Rule in the
    boundary doc changes.
```

## Authorization Basis (record, verbatim intent)

Owner word 2026-06-12 (ECR lane thread): "perhaps let's work on beauty tuning
next. we will want to own the ontology probably." and "okay route for it,
prompt out for beauty satellite." Earlier in the same thread the owner accepted
the deep-think recommendation that ECR stays vertical-agnostic and beauty
ontology routes to a satellite doc + the SCR authored-interpretation lane.
This authorizes documentation work only; no implementation authorization is
conveyed or implied.

## Goal Handoff

```yaml
goal_handoff:
  anchor_goal: >
    Own the beauty-vertical ontology as Orca satellite doctrine: a versioned
    vocabulary of beauty demand-signal kinds and distortion manifestations
    that feeds the SCR signal_family / family_detail seam and the
    Judgment-owned Signal Integrity / Signal Use registries, without
    redefining any core invariant.
  success_signal: >
    The slice-1 satellite doc is landed at the bound path with: every authored
    rule tagged source-invariant-core-candidate / source-family-adapted-satellite
    / unresolved-candidate per the Source-Family Promotion Rule; both owner
    seed lists mapped onto existing seams (or explicitly residualized); explicit
    non-claims; a direction_change_propagation receipt; and at least one named
    future two-family promotion candidate the owner could act on.
```

```yaml
thread_operating_target_continuity:
  carried_forward: no
  reason: no_visible_active_target
  changed_from_input: no
  lifecycle_status: none_active
  if_changed_reason:
```

(The prior ECR-lane operating target was consumed at the JSG-01 unfreeze
closeout; this is a new workstream.)

## Cynefin Routing (run 2026-06-12 in the authoring thread)

Regime: Complicated — the satellite contract, SCR seam, and promotion rule are
ratified and readable; satellite-before-core is explicitly authorized doctrine.
Decomposition: layer-based (contract → vocabulary → seams → lifecycle).
Riskiest assumption: beauty vocabulary can be authored at satellite grade from
general vertical knowledge + already-landed material, without new captures and
without the unbuilt core Signal Use registry. Stop-or-pivot: if authoring
cannot proceed without inventing the core Signal Integrity / Signal Use
registry shape, STOP and route a core-shape owner decision instead of bloating
the satellite. Re-run the router per
`.agents/workflow-overlay/decision-routing.md` only if scope drifts from this
commission.

## Preflight

Record `orca_start_preflight` on intake (owner:
`.agents/workflow-overlay/source-loading.md`):

- `agents_read` / `overlay_read`: must be `yes` in the receiving thread before
  authoring.
- `source_pack`: custom (the bounded pack below).
- `repo_map_decision: not_needed`; `repo_map_reason`: the source pack is fully
  named by this prompt; the ECR spine submap is included as the one-hop front
  door.
- Workspace: `C:\Users\vmon7\Desktop\projects\orca`.
- Isolation (decide and state before editing, per `AGENTS.md`): default is a
  worktree off `main` (writing work alongside active lanes on a dirty shared
  base); the owner may instead say to use the current shared branch
  (`ecr-sp3-timing-deriver-slice1` pattern). Do not start on a base whose
  isolation was not stated.
- Dirty-state allowance: other lanes' modified/untracked files exist on the
  shared branch; never commit, revert, or clean them. Untracked files are out
  of scope except the one new satellite doc.
- Controlling-source state at authoring time (verified 2026-06-12 at
  `de14a3b`): the four pinned sources below were git-clean. Re-verify on
  intake; report drift instead of silently proceeding.
- Doctrine change: YES — a new satellite product doctrine artifact. Closeout
  must carry a `direction_change_propagation` receipt (or named blocker) per
  `.agents/workflow-overlay/source-of-truth.md`, trigger `product_doctrine`
  (architecture-adjacent surfaces checked as the contract requires).
- Target file (exactly one new doc): `docs/product/beauty_vertical_satellite_v0.md`.
  Placement basis: `.agents/workflow-overlay/artifact-folders.md` — the bound
  product lane subfolders do not include a satellite lane, and "files matching
  no lane may stay at `docs/product/` root." Binding a dedicated satellite lane
  folder is a separate owner placement decision; do not create new folders.
- Edit permission: docs-write, this target only (plus the DCP receipt inline in
  the new doc).
- Output mode: `file-write`.
- External boundary: external workflow source is read-only; `jb` is not Orca
  authority.

## Source Pack (bounded)

SOURCE-LOAD the following, then declare `SOURCE_CONTEXT_READY` (or
`SOURCE_CONTEXT_INCOMPLETE` with the named gap) before authoring. Targeted
sections, not full files, except where marked:

1. `docs/product/core_spine/core_spine_v0_data_and_cleaning_spine_boundary_v0.md`
   — sections: Decision (layer table), Layer Rules, Inclusion State Rule,
   Core Vs Satellite, Source-Family Promotion Rule. This is the controlling
   contract for what a satellite may own.
2. `docs/product/signal_content/core_spine_v0_signal_content_record_architecture_v0.md`
   — full (short). The SCR direction: carrier, `signal_family` /
   `family_detail` seam, two-family promotion inheritance.
3. `orca-harness/signal_content/models.py` — read-only; `SignalFamily`,
   `DecisionRelevance`, the family/residual discipline. Code is the as-built
   seam; the contract wins on conflict.
4. `docs/workflows/ecr_spine_submap_v0.md` — orientation front door only.
5. `docs/decisions/orca_product_thesis_consumer_demand_v0.md` — thesis /
   value-proposition sections only (product anchor for decision-family
   context).
6. Optional, only if decision-family context needs it:
   `docs/product/product_lead/orca_buyer_proof_packet_v0.md` — target buyer +
   disqualifiers sections.

Excluded by default: all review outputs, research corpus bulk, proof-run
packets, all prompts, method-validation history, and the entire Beauty Pie
Phase-4 capture lane's material. Never open
`docs/research/orgmotion_beautypie_sealed_outcome_facilitator_only_v0.md` or
any `*sealed_outcome_facilitator_only*` artifact under any circumstance.

## Owner Seed Vocabulary (verbatim, 2026-06-12)

Treat as owner-supplied candidate vocabulary to structure and tag — not as
ratified semantics:

> Signal-integrity layer — label distortion: paid amplification,
> copied/coordinated content, incentive bias, review stuffing, trend-chasing,
> platform artifact, affiliate contamination.
>
> Demand-semantics layer — classify signal type: attention, search, review
> velocity, retail presence, switching, repurchase, workaround, complaint,
> community pressure, channel movement.

## Commission — Slice 1 Only

Author `docs/product/beauty_vertical_satellite_v0.md` with a retrieval header
and these sections:

1. **Decision-family context** — buyer context, decision owner, consequence,
   decision-family language, competitor-set framing for the beauty vertical
   (satellite-owned surfaces per Core Vs Satellite).
2. **Demand-semantics signal rows** — map each seed signal type onto the SCR
   seam: which of the four existing `SignalFamily` members (plus
   `family_detail` values) carries it; where a candidate NEW family would be
   needed, record it as an explicitly unpromoted candidate that degrades to
   `RESIDUAL_FAMILY_UNRESOLVED` today. Add candidate satellite Signal Use rows
   (registry shape consumed from the boundary doc, not designed here).
3. **Distortion-manifestation taxonomy** — what each seed distortion looks
   like per beauty-relevant source family (review sites, forums/Reddit,
   social/video, retail listings), mapped to the Judgment-owned Signal
   Integrity vocabulary as satellite-grade candidates. Name explicitly that
   the core Signal Integrity registry shape is reserved/unbuilt; consume the
   boundary, never design core.
4. **Source-family notes** — relevance, blind spots, and capture-feasibility
   constraints at a categorical level only (no capture plans, no source
   inventory, no scraper design).
5. **Promotion ledger** — every authored rule tagged
   `source-invariant-core-candidate` / `source-family-adapted-satellite` /
   `unresolved-candidate` per the Source-Family Promotion Rule, with at least
   one named future two-family promotion candidate.
6. **Non-claims.**

## Hard Constraints

- The satellite must not redefine capture provenance, admissibility, cutoff
  discipline, preservation discipline, integrity effects, cleaning
  traceability, Action Ceilings, memo/appendix discipline, or non-claims
  (boundary doc, Core Vs Satellite).
- Doc-only lane: no code edits anywhere (no `SignalFamily` enum change —
  promotion is a separate owner-gated act), no captures, no runners, no live
  LLM/raw-API calls, no case fixtures.
- Zero-spoiler discipline is absolute: no Beauty Pie capture or ad-hoc Beauty
  Pie sourcing (the outcome-clean Phase-4 lane owns it); sealed outcome
  artifacts stay sealed.
- Claim cap: product-learning. Authoring vocabulary proves nothing about
  judgment quality, signal quality, readiness, or buyer proof.
- Smallest complete intervention: slice 1 only — no ontology code, no schema,
  no beauty case fixtures, no SCR deriver changes, no second satellite.

## Output Mode And Contract

`file-write`. Write exactly one new doc at the bound target path. Closeout per
`.agents/workflow-overlay/prompt-orchestration.md` file-write rules: headed
human summary first (recommendation, boundaries, next authorized step), then
the path/SHA256/status receipt, plus the `direction_change_propagation`
receipt. Commit only the new doc on the stated isolation; verify the landed
file with a fresh read before any written/committed claim.

## Validation Gates

- `orca_start_preflight` recorded on intake; pinned-source re-verification
  (drift → report and stop, never silently proceed).
- `SOURCE_CONTEXT_READY` declared before any authoring (APPLY gate per the
  Source-Gated Method Contract).
- Retrieval header uses literal `authority_boundary: retrieval_only` (hook
  compatibility); placement check passes as shape-only evidence.
- DCP receipt present at closeout, or strict completion claims are blocked.
- Verifying read of the landed file shown for the lifecycle claim.

## Non-Claims

Authoring this satellite is not validation, readiness, acceptance, core
promotion, Evidence Unit architecture work, JSG gate work, Signal Integrity /
Signal Use core registry design, or implementation authorization. Template
note: no project handoff template is registered; this prompt mirrors the
accepted prior handoff structure plus the prompt-orchestration full-prompt
contract.

Prompt verdict at authoring: PASS_WITH_WARNINGS — warnings: (1) model lane
unbound (warning-only; no model routing requested); (2) satellite home
defaults to `docs/product/` root under the no-matching-lane rule; binding a
dedicated satellite lane folder remains an open owner placement option;
(3) isolation is an owner choice between the `AGENTS.md` worktree default and
the established shared-branch pattern — the receiving lane must state the
choice before editing.
