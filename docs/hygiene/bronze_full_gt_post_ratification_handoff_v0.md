# Handoff Packet

```yaml
retrieval_header_version: 1
artifact_role: Cold cross-lane handoff checkpoint
scope: >
  Continuation packet for the Bronze full-GT lane after both physicalization
  gates were owner-ratified on 2026-07-02: contract fold-in with DCP receipts,
  then the implementation-scoping route for the physicalization proof scope
  (A1 deterministic inventory gate plus the invariant-proof obligations),
  toward a defensible Bronze full-GT claim.
use_when:
  - Continuing the Bronze full-GT lane in a fresh thread after gate ratification.
  - Checking what ratification changed, what fold-in must do, and what still blocks a full-GT claim.
  - Checking the standing Gate 2 deferral triggers before any backend-adjacent step.
authority_boundary: retrieval_only
open_next:
  - orca/product/spines/data_lake/workflows/core_spine_v0_data_lake_bronze_full_gt_gate1_attachment_record_body_layout_adr_v0.md
  - orca/product/spines/data_lake/workflows/core_spine_v0_data_lake_bronze_full_gt_gate2_retention_lawful_erasure_posture_adr_v0.md
  - orca/product/spines/data_lake/authority/core_spine_v0_data_lake_attachment_record_implementation_contract_v0.md
stale_if:
  - Contract fold-in lands and the implementation-scoping route is accepted (this packet is then history).
  - Any Gate 2 revisit trigger (T1-T4) fires.
  - A later accepted authority supersedes either ratified ADR.
```

## Load Contract

- packet_version: workflow-handoff max v0
- mode: max
- created_at: 2026-07-02
- created_by_lane: Anthropic/Claude session lane (Gate ADR batch thread); provenance only, not authority
- workspace: receiver creates a FRESH worktree/branch off `origin/main`
- handoff_path: `docs/hygiene/bronze_full_gt_post_ratification_handoff_v0.md`
- expected_branch: authored on `claude/bronze-gate-ratification` pre-PR; receiver must verify this packet AND both ratification records are on `origin/main` (`git ls-tree origin/main -- <path>`; grep each ADR for `decision: ratified`) before continuing
- expected_dirty_state_including_handoff_file: receiver's fresh worktree should be clean
- load_rule: confirm-don't-trust; re-verify every load-bearing fact against its compare target before acting; sender claims are hypotheses, not authority

## Goal Handoff

- long_term_goal: Bronze from Mini God Tier (typed raw-truth retrievability, proven behavior) to defensible full God Tier - physical architecture deliberately decided, implemented, and proven - without storage convenience choosing architecture, hiding residuals, or weakening raw authority.
- anchor_goal: Execute the post-ratification chain in order: (1) contract fold-in - the AR implementation, Storage, and Physicality-Location contracts absorb the ratified Gate 1 relationship and point at the ratified Gate 2 deferral, each edit carrying its own direction_change_propagation receipt; (2) an accepted implementation-scoping route (workflow-implementation-scoping, read-only) for the physicalization proof scope: the A1 deterministic inventory gate plus deterministic proof of write-once raw, append-only derived/ack, read-by-key, hash verification, public AR body resolution, and index rebuild under the ratified packet-member relationship.
- success_signal:
  - core_success: Fold-in lands with shape-valid receipts and no contract still reads "layout undecided"; the scoping route exists with ordered STEP-* entries so the owner can grant bounded implementation authorization as a single yes/no.
  - boundary: Neither fold-in nor the route is implementation, validation, readiness, or a full-GT claim.
  - drift_cue: The lane is drifting if it starts runtime storage code before the owner authorizes the scoped route, opens a backend ADR without firing Gate 2 trigger T3, or starts third-proof work below the materially-different threshold.

## Open Decision / Fork

- decision: The physicalization brief's cross-vendor discovery residual (the brief has had two same-vendor GPT reviews plus cross-family Claude adjudication, never a non-OpenAI controller pass).
  - options: owner accepts it as a named residual at full-GT closeout; or commissions one non-OpenAI, non-Anthropic (e.g. Gemini-family) pass over the brief.
  - already constrained: the final full-GT closeout separately requires a de-correlated review over the FINAL contracts and code path (brief Full-GT Distance item 5), which could absorb this.
  - owner of the call: Owner. recommendation: fold it into the final full-GT de-correlated review commission rather than running a standalone pass now.
- decision: Bounded implementation authorization for the scoped route (only after the route exists). Owner-only; the route must present it as one yes/no.

## Drift Guard

- Gate 2's ratified deferral is standing doctrine: its claim ceiling caps all deletion/compliance language; its forbidden backend classes/operations bind every future storage step; any backend ADR fires trigger T3 and must re-ratify or replace the deferral first.
- G1-D external bodies stay locked behind Gate 2 PLUS a separate backend/physicalization ADR proving the storage invariants; Gate 2's deferral alone unlocks nothing.
- The attachments/ sidecar slot opens only through a future ADR on its named reopen trigger (a body that cannot land in its packet).
- Third-proof work only for a materially different raw-body/AR-join shape per the brief's threshold; the YouTube ambiguous-AR branch stays code-present/not-test-proven until pinned.
- No full-GT claim until the brief's Full-GT Distance items 3-5 close: implementation proves the invariants; materially-different third proof; final de-correlated review over contracts + code.
- Ratification is not implementation authorization. Fold-in is docs-write; everything runtime waits for the owner's route-level yes.

## Inherited Context (does NOT flow to a new lane)

### Source-loading state to re-establish (follows overlay doctrine)

- overlay source-loading policy: `.agents/workflow-overlay/source-loading.md`; hierarchy: `.agents/workflow-overlay/source-of-truth.md` (owns the DCP receipt contract fold-in must satisfy).
- targets to enter the ladder: `AGENTS.md`; overlay README; then the ledger below.
- already loaded by sender (weak orientation, 2026-07-02; not authority): both ADRs (authored+ratified this thread), AR implementation / storage / physicality / Silver Vault contracts, the brief, batch plan, B5 review report, two-family proof closeout.
- must load first (before strict or actionable steps): `.agents/workflow-overlay/source-of-truth.md` (DCP contract - sender never read it in full); the raw-admission + key grammar contract (owns the sharded raw grammar the ratified relationship sits under; sender never read it); both ratified ADRs fresh from main.
- load rule: receiver re-runs progressive source loading per overlay; this packet's loaded-set only seeds the ladder.

### Earlier-decided concepts and behaviors (inline gist plus verify pointer)

- Gate 1 ratified 2026-07-02: packet-member default body relationship; sidecar reserved; G1-D double-locked; eight outputs bound (body key, hash_basis=raw_stored_bytes, relationship, public surface, authority split, rebuild rule, zero-body-home-migration replay implication, rejected shapes).
  - decided in: `orca/product/spines/data_lake/workflows/core_spine_v0_data_lake_bronze_full_gt_gate1_attachment_record_body_layout_adr_v0.md`
  - compare target: `gate1_ratification.decision: ratified` present on origin/main | verify before: any fold-in or scoping claim.
- Gate 2 ratified 2026-07-02: explicit deferral with accepted-residual record (residual scope incl. public-web basis, claim ceiling, tombstone posture, forbidden backend classes/operations, triggers T1-T4).
  - decided in: `orca/product/spines/data_lake/workflows/core_spine_v0_data_lake_bronze_full_gt_gate2_retention_lawful_erasure_posture_adr_v0.md`
  - compare target: `gate2_ratification.decision: ratified` on origin/main | verify before: any retention/backend-adjacent step.
- B5 delegated review executed and adjudicated (discovery bar satisfied for both ADRs; brief at same-vendor sanity).
  - decided in: `docs/review-outputs/adversarial-artifact-reviews/core_spine_v0_data_lake_bronze_full_gt_gate_adr_batch_delegated_adversarial_review_patch_v0.md`
  - compare target: reread-required | verify before: any review-status claim.
- A2 (Manifest v2 vs packet-index serialization) stays gated on A1 (deterministic inventory); the old next-material-decisions packet holds the A1/A2 definitions.
  - decided in: `orca/product/spines/data_lake/workflows/core_spine_v0_data_lake_bronze_full_gt_next_material_decisions_v0.md` (historical but load-bearing for A1/A2 shape)
  - compare target: reread-required | verify before: scoping the inventory gate.
- The concurrent consumption-seam lane (pickup/ack helper, derived_retrieval rebuild, metrics policy) is separate and already launched; do not absorb it.
  - decided in: `docs/hygiene/data_lake_consumption_seam_scoping_handoff_v0.md`
  - compare target: reread-required | verify before: any scope overlap decision.

## Active Objective

Make Bronze full-GT real: land contract fold-in for the two ratified gates, then produce the accepted implementation-scoping route for the physicalization proof scope, ending at a single owner yes/no on bounded implementation.

## Exact Next Authorized Action

1. Fresh worktree off `origin/main`; verify this packet and both `decision: ratified` blocks are on main; run the overlay start preflight.
2. Read `.agents/workflow-overlay/source-of-truth.md` (DCP contract) and the raw-admission + key grammar contract in full.
3. Fold-in lane (docs-write): update the AR implementation contract (layout: packet-member selected per Gate 1 ADR; keep A2 serialization deferred), the storage contract (blocker-1 layout note; retention posture pointer to Gate 2 ADR), and the physicality contract ("Attachment physical home unfrozen" residual closes; footnote resolves to packet-member) - one lane PR, one DCP receipt per contract edit, stale-language searches actually run.
4. Then run `workflow-implementation-scoping` (read-only) for the proof scope: A1 deterministic inventory gate + the six invariant proofs, under the ratified relationship; route ends at the owner authorization fork.
5. Stop conditions: any step needing a backend choice (fires Gate 2 T3), a second body home, or a full-GT claim is a blocker, not a decision.

## Authority And Source Ledger

- Repository instructions: `AGENTS.md`; overlay README - Load-bearing: yes; reread-required.
- User constraints: owner ratified both gates 2026-07-02 in-session ("2 gates OK"); wants this lane continued to "make bronze GT"; seam lane runs concurrently elsewhere.
- Source-read ledger: the five pointer entries above plus (all Load-bearing: yes, reread-required, last checked 2026-07-02): the three authority contracts named in fold-in; the patched brief (historical framing; its stale_if has self-fired); the batch plan (historical, status BATCH_COMPLETE).
- Source gaps: source-of-truth.md and raw-admission contract unread by sender; exact fold-in wording is receiver's judgment against contract text.
- Strict-only blockers: no implementation, validation, readiness, backend, erasure-capability, or full-GT claim may be made from this packet.

## Current Task State

- Completed: gates framed (brief, PR #557, reviewed twice), ADR batch authored (PR #576), B5 review executed + adjudicated (PR #578), both gates owner-ratified with DCP receipts (this packet's lane PR).
- Not started: contract fold-in; implementation-scoping route; everything runtime.

## Workspace State

- Authored on branch `claude/bronze-gate-ratification` (pre-PR); this handoff file plus the two ratified ADRs and batch-plan sync land via that lane's PR.
- Receiver state: fresh worktree off `origin/main`, clean.

## Frozen Decisions

- Packet-member default body relationship (Gate 1, ratified). Consequence: fold-in states it as contract fact; implementations must reproduce it.
- Erasure deferred with bounded residual record (Gate 2, ratified). Consequence: claim ceiling and forbidden-backend rules bind all downstream work; T1-T4 are live tripwires.

## Mutable Questions

- Brief discovery residual: accept vs Gemini pass (owner; recommendation: fold into final full-GT review).
- Implementation authorization: granted only against the finished scoping route.
- Whether A1's inventory gate lands inside the first implementation slice or as its own slice (scoping decides).

## Superseded / Dangerous-To-Reuse Context

- The brief's Decision Request and option ledgers: superseded by the ratified ADRs; do not re-adjudicate options from the brief.
- The batch plan's sequencing (B1-B5): complete; do not re-run it.
- Any pre-ratification statement that "nothing is selected": stale - the two gates ARE now selected/deferred by ratified authority.

## Commands And Verification Evidence

- Verify ratification on main: `git grep -n "decision: ratified" origin/main -- "orca/product/spines/data_lake/workflows/core_spine_v0_data_lake_bronze_full_gt_gate*"` (expect both ADRs).
- Receipt shape gate (after fold-in edits): `python .agents/hooks/check_dcp_receipt.py --strict`.

## Blockers And Risks

- Fold-in wording risk: contracts are shared authority surfaces; a careless edit could widen scope. Mitigation: smallest complete edits, one receipt each, reread contract text first.
- The sender never read source-of-truth.md; the DCP contract details (receipt caps, archive pointer rules) must come from a fresh read, not this packet.

## Confirm-Don't-Trust Load Checklist

- Re-verify before acting: packet + both ratification blocks on main; ADR content matches the gists above (reread both in full); fold-in target contracts' current text; seam-lane handoff exists (scope boundary).
- Load outcomes: REUSE (all verified) -> continue at Exact Next Authorized Action step 2; STALE_REREAD_REQUIRED (contracts or ADRs moved) -> reread then continue; BLOCKED_UNVERIFIABLE (ratification blocks absent on main) -> stop, report to owner.

## Do Not Forget

Ratification closed the *decision* layer, not the *proof* layer: full GT still requires implementation proving the six invariants, a materially-different third proof, and a final de-correlated review over contracts plus code. Do not let "gates ratified" drift into "Bronze is full GT" in any artifact or chat.
