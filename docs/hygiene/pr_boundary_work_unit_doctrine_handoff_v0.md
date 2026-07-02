# Handoff Packet

```yaml
retrieval_header_version: 1
artifact_role: Cold cross-lane handoff checkpoint
scope: >
  Commission packet for a fresh lane to encode the owner's 2026-07-02
  PR-boundary direction into the dev-workflow doctrine: PRs are cut per work
  unit; planning/scoping-only artifacts are not standalone PRs by default;
  the commissioning artifact (handoff packet or /fused invocation) decides at
  commissioning time whether to pre-grant bounded implementation authority
  (whole chain lands as one lane PR) or withhold it (deliberate mid-chain
  owner fork with split PRs); named exceptions where splitting stays correct.
use_when:
  - Starting the lane that folds the PR-boundary rule into the dev-workflow doctrine.
  - Checking what the owner actually directed about PR topology on 2026-07-02.
authority_boundary: retrieval_only
open_next:
  - docs/decisions/dev_workflow_ci_branch_protection_doctrine_v0.md
  - .agents/workflow-overlay/source-of-truth.md
stale_if:
  - The doctrine edit lands with its DCP receipt (this packet is then consumed history; delete it per the checkpoint lifecycle).
  - A later owner direction changes the PR-boundary rule.
```

## Load Contract

- packet_version: workflow-handoff max v0
- mode: max
- created_at: 2026-07-02
- created_by_lane: Anthropic/Claude session lane (Bronze full-GT post-ratification thread); provenance only, not authority
- workspace: receiver creates a fresh worktree or branch off `origin/main`
- handoff_path: `docs/hygiene/pr_boundary_work_unit_doctrine_handoff_v0.md`
- expected_branch: authored on `claude/pr-boundary-doctrine-handoff` off `origin/main` @ `0e8056fa`; receiver must verify this packet is on `origin/main` (`git ls-tree origin/main -- docs/hygiene/pr_boundary_work_unit_doctrine_handoff_v0.md`) before continuing
- expected_dirty_state_including_handoff_file: receiver's fresh worktree should be clean
- load_rule: confirm-don't-trust; re-verify every load-bearing fact against its compare target before acting; sender claims are hypotheses, not authority

## Goal Handoff

- long_term_goal: Orca lanes deliver owner-steerable work with minimal
  no-value ceremony (AGENTS.md Operating Economy): PR topology matches work
  units, so owner review/steer cycles are spent on real forks, not on
  artifact fragments.
- anchor_goal: Fold the owner's 2026-07-02 PR-boundary direction into
  `docs/decisions/dev_workflow_ci_branch_protection_doctrine_v0.md` (the
  per-lane PR flow owner) as a smallest complete edit with one
  `direction_change_propagation` receipt (trigger: `workflow_authority`) and
  actually-run stale-language searches. The rule to encode:
  1. A lane PR is cut per **work unit**, not per pipeline stage.
  2. A planning/scoping-only artifact is not a standalone PR by default; it
     rides with the work unit that produced it, or the chain continues when
     authority allows.
  3. The commissioning artifact (handoff packet or `/fused` invocation)
     decides the authority grant **at commissioning time**: pre-grant bounded
     implementation authority so the full scope→spec→implement→review chain
     is one work unit landing as one lane PR (owner steers at commissioning),
     or deliberately withhold it, making a mid-chain owner authorization fork
     the explicit work-unit boundary (split PRs). Withholding is a deliberate
     choice, not the default drift.
  4. Named exceptions where splitting stays correct even with pre-granted
     authority: (a) the earlier half carries shared-authority doctrine that
     other concurrent lanes need on `main` promptly (example: the Gate 1/2
     contract fold-in in PR #585); (b) authority is deliberately withheld for
     a mid-chain owner fork; (c) high-lock-in probe-first slicing per the
     Smallest Complete Intervention rule.
- success_signal:
  - core_success: the doctrine file states the rule in its own voice; the DCP
    receipt lands shape-valid (`python .agents/hooks/check_dcp_receipt.py
    --strict` green) with the stale-language search executed and reconciled
    against the doctrine's existing PR-cadence language; downstream surfaces
    checked (pointing, not forking).
  - boundary: no owner gate is weakened — landing to `main` stays
    human-gated, the protected-action guard is untouched, and pre-granting
    implementation authority remains an owner choice recorded in the
    commissioning artifact, never an agent default.

## Open Decision / Fork

- decision: exact placement and wording granularity inside the doctrine file.
  - options: a new subsection under the per-lane PR flow decision vs. amending
    the existing PR-cadence language in place.
  - already constrained: single-source the rule in the dev-workflow doctrine;
    other surfaces point at it (source-of-truth.md anti-fork rule).
  - owner of the call: receiving lane's judgment against the doctrine's
    current text; surface to owner only if the existing text materially
    conflicts with the direction quoted below.
  - recommendation: amend nearest to where the doctrine already discusses PR
    cadence/size (its prior receipts track "one focused PR|PR cadence"
    language — see ledger), so one home keeps owning the topic.
- decision: whether `.agents/workflow-overlay/prompt-orchestration.md` (the
  handoff/commissioning prompt-family owner) needs a one-line pointer telling
  commissioning artifacts to record the authority-grant decision.
  - recommendation: add the pointer only if the receiving lane's read shows
    commissioning artifacts have no existing field for it; keep the rule
    itself in the dev-workflow doctrine.

## Drift Guard

- Do not weaken any owner gate: human merge to `main`, the protected-action
  guard, and the per-lane/accepted-handoff authorization to open PRs stay
  exactly as the doctrine states them. This rule governs PR *topology*, not
  merge *authority*.
- Not a license for big-bang PRs: work units still follow the Smallest
  Complete Intervention rule; this rule only fixes where the PR boundary sits
  relative to the owner authorization fork.
- Do not edit `AGENTS.md` unless a real conflict is found — it already routes
  landing through the doctrine ("Land changes via the per-lane PR flow in
  docs/decisions/dev_workflow_ci_branch_protection_doctrine_v0.md").
- Do not edit the `workflow-handoff` or `fused` skill sources (external
  workflow-kernel candidates, not Orca authority); the Orca-side rule lives in
  Orca doctrine only.
- Do not re-litigate or retro-classify past PRs. PR #585 (scoping route +
  fold-in as its own PR, implementation split off) was correct under its
  commissioning packet: exception (a) applied to the fold-in half and the
  commissioning packet deliberately withheld implementation authority.
- Docs-only lane: doctrine text + receipt; no runtime, CI-config, or
  branch-protection changes.

## Inherited Context (does NOT flow to a new lane)

### Source-loading state to re-establish (follows overlay doctrine)

- overlay source-loading policy: `.agents/workflow-overlay/source-loading.md`;
  hierarchy and DCP receipt contract: `.agents/workflow-overlay/source-of-truth.md`.
- targets to enter the ladder: `AGENTS.md`; overlay README; then the ledger below.
- already loaded by sender (weak orientation, 2026-07-02; not authority):
  doctrine file headings and PR-cadence grep hits only; AGENTS.md and overlay
  in full (in the sender's thread — receiver rereads its own).
- must load first (before strict or actionable steps):
  `docs/decisions/dev_workflow_ci_branch_protection_doctrine_v0.md` in full —
  the sender NEVER read it in full; its existing decision text, item numbering,
  and prior receipts must come from a fresh read, not this packet.
- load rule: receiver re-runs progressive source loading per overlay; this
  packet's loaded-set only seeds the ladder.

### Earlier-decided concepts and behaviors (inline gist plus verify pointer)

- Owner direction (the doctrine change this lane encodes), stated 2026-07-02
  in the sender's thread, verbatim: "hold on - we should do PRs in terms of
  work unit no ? why we pring scope shouldnt we do it after whole fused chain ?
  e.g. implement and reviewed changed and agreed." followed by "let's hand off
  first so this one would be implemented for future - this behavior for
  PRing."
  - decided in: the sender's chat thread; this packet is the durable record.
  - compare target: user-stated, carried verbatim above | verify before: if
    the receiving lane finds the direction materially ambiguous against the
    doctrine's existing text, surface to the owner instead of guessing.
- Case study grounding the rule and exception (a): PR #585 landed Gate 1/2
  contract fold-in + a read-only scoping route as one PR, with implementation
  split behind an owner yes/no; the split was packet-mandated (authority
  withheld) and the fold-in half was shared-authority doctrine other lanes
  needed on `main` promptly.
  - decided in: PR #585, merged to `origin/main` as `0e8056fa`; route artifact
    `orca/product/spines/data_lake/workflows/core_spine_v0_data_lake_bronze_full_gt_physicalization_proof_scoping_route_v0.md`.
  - compare target: `git log -1 0e8056fa` + route file on `origin/main` | verify
    before: citing the case in doctrine text.
- Kernel rules this direction instantiates: Operating Economy (fewest ceremony
  steps per delivered unit, act-default on reversible work) and Smallest
  Complete Intervention (deliberate slicing only for lock-in/probe reasons).
  - decided in: `AGENTS.md` | compare target: reread-required | verify before:
    drafting the doctrine wording.

## Active Objective

Encode the PR-boundary-per-work-unit rule (with the commissioning-time
authority-grant decision and the three named exceptions) into the dev-workflow
doctrine with a shape-valid DCP receipt, and land it via one lane PR.

## Exact Next Authorized Action

1. Fresh worktree or branch off `origin/main`; verify this packet is on
   `origin/main`; run the overlay start preflight.
2. Read `docs/decisions/dev_workflow_ci_branch_protection_doctrine_v0.md` in
   full and the DCP contract in `.agents/workflow-overlay/source-of-truth.md`.
3. Draft the smallest complete doctrine edit stating rules 1-4 from the
   anchor_goal; reconcile with the doctrine's existing PR-cadence language
   (amend, don't duplicate).
4. Write one `direction_change_propagation` receipt (trigger:
   `workflow_authority`); run a stale-language search such as
   `rg -in "one focused PR|PR cadence|per-lane PR|work unit" AGENTS.md
   .agents/workflow-overlay/ docs/decisions/dev_workflow_ci_branch_protection_doctrine_v0.md`
   and record the result; check downstream surfaces (`AGENTS.md`,
   `.agents/workflow-overlay/prompt-orchestration.md`,
   `.agents/workflow-overlay/decision-routing.md`, repo map) — point, don't
   fork; run `python .agents/hooks/check_dcp_receipt.py --strict`.
5. Delete this packet in the same PR (checkpoint single-consumption); commit,
   push, open the lane PR; landing stays human-gated.
6. Stop conditions: existing doctrine text materially conflicts with the
   quoted owner direction → surface to owner; any edit that would touch merge
   authority, CI config, or branch protection → blocker, not a decision.

## Authority And Source Ledger

- Repository instructions: `AGENTS.md`; overlay README — Load-bearing: yes;
  reread-required.
- User constraints: owner directed the PR-boundary behavior 2026-07-02
  (verbatim quotes above); owner merged PR #585 the same day.
- Source-read ledger:
  - `docs/decisions/dev_workflow_ci_branch_protection_doctrine_v0.md`
    - Role: edit target; per-lane PR flow owner.
    - Load-bearing: yes.
    - Compare target: reread-required (sender read headings + grep hits only;
      known: prior receipts already searched "one focused PR|PR cadence",
      so compatible cadence language exists and must be reconciled).
    - Last checked: 2026-07-02 (headings/grep only).
    - Reuse rule: receiver reads in full before drafting.
  - `AGENTS.md`
    - Role: kernel; routes landing to the doctrine; owns Operating Economy + SCI.
    - Load-bearing: yes. Compare target: quoted routing line in Drift Guard;
      reread-required for full text. Last checked: 2026-07-02.
    - Reuse rule: check for conflicts; expect intentionally_not_updated.
  - `.agents/workflow-overlay/source-of-truth.md`
    - Role: DCP receipt contract (shape, two-inline cap, archive pointer).
    - Load-bearing: yes. Compare target: reread-required. Last checked: 2026-07-02.
    - Reuse rule: receipt must match its shape exactly.
- Source gaps: the doctrine file's full text (sender never read it); whether
  prompt-orchestration.md already carries a commissioning authority-grant field.
- Strict-only blockers: no CI, branch-protection, merge-authority, or
  AGENTS.md-kernel change may be made from this packet.

## Current Task State

- Completed: owner direction captured verbatim; case study (#585) landed on
  main; this packet authored.
- Not started: the doctrine edit, receipt, and lane PR — all receiver work.

## Workspace State

- Branch: authored on `claude/pr-boundary-doctrine-handoff` off `origin/main`
  @ `0e8056fa`; clean before this packet; this packet untracked after writing
  until committed.
- Receiver state: fresh worktree or branch off `origin/main`, clean.

## Frozen Decisions

- The rule targets the dev-workflow doctrine as its single home; other
  surfaces point. Consequence: no duplicated PR-topology rules across files.
- Landing to `main` stays human-gated; the protected-action guard stays as-is.
  Consequence: this rule changes topology, never authority.

## Mutable Questions

- Placement/wording inside the doctrine (receiver judgment against full text).
- Whether prompt-orchestration.md needs the one-line commissioning pointer.

## Superseded / Dangerous-To-Reuse Context

- The sender thread's inline explanation of PR #585's split: orientation only;
  the doctrine edit must cite the packet-mandated fork and exception (a), not
  reproduce chat reasoning.

## Commands And Verification Evidence

- Verify packet on main: `git ls-tree origin/main -- docs/hygiene/pr_boundary_work_unit_doctrine_handoff_v0.md`.
- Receipt gate after edits: `python .agents/hooks/check_dcp_receipt.py --strict`.

## Blockers And Risks

- Wording risk: the doctrine is a long, receipt-dense shared file; a careless
  edit could contradict its existing cadence/authority text. Mitigation: full
  fresh read first; smallest complete edit; one receipt.

## Confirm-Don't-Trust Load Checklist

- Re-verify before acting: packet on `origin/main`; doctrine file full read;
  AGENTS.md routing line; DCP contract shape.
- Load outcomes: REUSE (all verified) → continue at Exact Next Authorized
  Action step 2; STALE_REREAD_REQUIRED (doctrine moved) → reread then continue;
  BLOCKED_UNVERIFIABLE (packet absent on main) → stop, report to owner.

## Do Not Forget

The owner's direction is about WHERE the PR boundary sits, not about merging
authority or PR size: pre-granted authority → one chain, one PR; withheld
authority → the fork IS the boundary. Encode the exceptions with the rule, or
the rule will be misread as "never split."
