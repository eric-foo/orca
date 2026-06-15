---
retrieval_header_version: 1
artifact_role: Cold handoff packet (durable; transfers the "lane-start auto-prune rule" lane to a fresh lane/agent that holds none of this thread's context)
scope: >
  Adopt an agent-side lane-start standing rule that prunes merged worktree/branch
  residue (git fetch --prune + remove [gone]-branch worktrees + delete [gone]
  branches) at each new lane's start — closing the cleanup half of the
  agent-fast-creation / human-gated-cleanup velocity mismatch. Owner-gated; lands
  via a per-lane PR off main. The merge half is already closed by the live
  auto-merge bot.
authority_boundary: retrieval_only
open_next:
  - docs/decisions/dev_workflow_ci_branch_protection_doctrine_v0.md
  - .agents/workflow-overlay/decision-routing.md
---

# Handoff Packet — Lane-Start Auto-Prune Rule

## Load Contract

- packet_version: v0
- mode: max
- created_at: 2026-06-15
- created_by_lane: lane-start-auto-prune-handoff-v0 (provenance only; not an authority claim)
- workspace: C:\Users\vmon7\Desktop\projects\orca (do the actual rule work in a FRESH worktree off origin/main)
- handoff_path: docs/hygiene/lane_start_auto_prune_rule_handoff_v0.md
- expected_branch: this packet is stored on lane `lane-start-auto-prune-handoff-v0`; the receiver opens a NEW lane off `origin/main` for the rule itself.
- expected_head: `origin/main` = `02e91e2` at packet creation. REREAD — this repo moves fast (~30 PRs/day, plus the auto-merge bot is now live), so the head will have moved.
- expected_dirty_state_including_handoff_file: this packet file is newly created + untracked on its lane until committed.
- load_rule: confirm-don't-trust; re-verify every load-bearing fact against its compare target before acting; sender claims are hypotheses, not authority.

## Goal Handoff

- long_term_goal: Self-maintaining dev workflow — sprawl never rebuilds; cleanup keeps pace with machine-speed lane creation.
- anchor_goal: Adopt an agent-side lane-start standing rule (git fetch --prune + remove any [gone]-branch worktree + delete the [gone] branch) at each new lane's start; zero new infra; owner-gated; lands via a lane PR.
- success_signal:
  - Core success:
    - owner-observable: rule documented in its owning surface + landed via PR; worktree count stays bounded without manual sweeps.
    - output_fit: a CONCRETE owner-gated rule (location, exact prune steps, safety guards: non-force remove only, exclude open-PR worktrees, never the seal or [ahead]-unpushed worktrees), not vague tidiness.
    - boundary: not the one-time sweep alone; not a force prune of dirty/open-PR worktrees; not throttling creation.
    - drift_cue: scope-creep into big automation; destructive-by-default prune; or slowing creation.
  - Secondary success signals:
    - Optional: wire `.github/scripts/lane-health-check.ps1` as a periodic backstop.
    - Composes with the live auto-merge bot (merge half already handled).

## Open Decision / Fork

- decision: WHERE the standing rule lives, and WHAT FORM it takes.
  - options:
    - (a) `AGENTS.md` kernel trigger — highest visibility, but the kernel is deliberately terse/global; a procedural git rule may be too operational for it.
    - (b) **`docs/decisions/dev_workflow_ci_branch_protection_doctrine_v0.md` as a new Decision item** — co-located with item 8 (lane-isolation early-detection detector) and item 9 (the auto-merge bot). Natural home; the rule is the cleanup complement to those two.
    - (c) `.agents/workflow-overlay/` (lane-isolation or decision-routing surface) — overlay-level behavioral rule.
    - form: agent-instruction-only (a standing behavioral rule the agent follows at lane start) vs ALSO wiring `.github/scripts/lane-health-check.ps1` to perform or prompt the prune.
  - already constrained / off the table: not a new always-on destructive automation; not a guard edit; not throttling lane creation; the one-time backlog sweep is already done (do not re-scope it as the deliverable).
  - trade-offs: (b)+instruction-only is smallest-complete and composes with the existing item-8 detector + item-9 bot; wiring the detector adds a periodic backstop but is more surface and risks a destructive script.
  - owner of the call: owner / architecture.
  - recommendation and why: **(b) doctrine Decision item + agent-instruction-only first**, detector-wiring as an explicitly optional follow-on. Smallest complete, co-located with the related items, zero new infra.

## Drift Guard

- non-force `git worktree remove` ONLY.
  - why it matters: non-force `remove` REFUSES a worktree with uncommitted/untracked content. That refusal is the load-bearing safety — it cannot discard unsaved work.
  - what violating it would break: `--force` would silently delete real uncommitted work.
- EXCLUDE open-PR worktrees from any prune.
  - why: removing a worktree on an open PR disrupts in-flight review/work.
  - what violating it would break: an active lane's checkout.
- NEVER prune the seal worktree or any `[ahead]`-with-unpushed-commits worktree.
  - the seal: `orca-seal-wt` [branch `pilot-seal-outcome`] holds the unpushed, firewalled Beauty-Pie sealed outcome. Pruning it discards the only copy AND its presence is outcome-sensitive. Do not prune it; do not read its sealed file.
  - `[ahead]` worktrees at packet time: `doctrine-harness-caveat`, `hooks-readme`, `judgment-spine-read-machinery-architecture-v0`, `ledger-c2-read-contract-v0` — each has unpushed unique commits. REREAD `git for-each-ref --format='%(refname:short) %(upstream:track)' refs/heads | rg ahead` for the current set.
- `[gone]` = merged via squash + `delete_branch_on_merge`, so `git branch -D` is normally safe — but glance for a closed-unmerged PR (its branch would also read `[gone]` while its work is NOT on main) before deleting.
- do NOT throttle lane creation; do NOT build heavy CI/automation; owner-gated; lands via a per-lane PR off main; the EP-03 guard (`.agents/hooks/guard_protected_actions.py`) is unchanged — this is a behavioral/doctrine rule, not a guard edit.

## Inherited Context (does NOT flow to a new lane)

### Source-loading state to re-establish (follows overlay doctrine)

- overlay source-loading policy: Orca overlay — read `AGENTS.md` then `.agents/workflow-overlay/README.md` first (per AGENTS.md); this is doctrine-changing, so run the Cynefin Routing Layer (`.agents/workflow-overlay/decision-routing.md`) before planning/editing.
- targets to enter the ladder: `docs/decisions/dev_workflow_ci_branch_protection_doctrine_v0.md` (items 5, 8, 9), `.github/scripts/lane-health-check.ps1`, `.agents/workflow-overlay/decision-routing.md`.
- already loaded (weak orientation, freshness-marked; NOT authority): this packet's claims, captured 2026-06-15 against `origin/main` @ `02e91e2`. Treat as hypotheses.
- must load first (before any strict or actionable step): the dev-workflow doctrine (to pick the home + match item-8/9 style) and the overlay README + decision-routing.
- load rule: receiver re-runs progressive source loading per the overlay; the packet's loaded-set only seeds the ladder.

### Earlier-decided concepts and behaviors (inline gist plus verify pointer)

- The auto-merge bot is LIVE (the MERGE half of the velocity mismatch).
  - gist: a CI-controlled GitHub Actions workflow merges PRs labeled `agent-automerge` when clean + green + up-to-date, one-per-run, squash; this auto-prune rule is its CLEANUP complement.
  - decided in: `.github/workflows/auto-merge.yml` + `docs/decisions/dev_workflow_ci_branch_protection_doctrine_v0.md` Decision item 9.
  - compare target: `gh pr view 97 --repo eric-foo/orca --json state` → MERGED (merged 2026-06-14T14:36Z); `git ls-tree origin/main .github/workflows/auto-merge.yml` exists.
  - verify before: relying on "merge half is handled."
- Squash-merge default + `delete_branch_on_merge` → a merged lane's remote branch auto-deletes, so its local branch reads `[gone]`.
  - decided in: dev-workflow doctrine items 4 and 5.
  - compare target: `gh api repos/eric-foo/orca --jq '{allow_squash_merge, delete_branch_on_merge}'` → both true.
  - verify before: treating `[gone]` as "safe to delete."
- Structure B′ (in-session guard self-merge) + the EP-03 guard are unchanged by this lane.
  - gist: the guard already allows an in-session agent to `gh pr merge` a CLEAN + green + `agent-automerge`-labeled PR; this lane does not touch the guard.
  - decided in: `docs/decisions/dev_workflow_ci_branch_protection_doctrine_v0.md` item 7; `.agents/hooks/guard_protected_actions.py`.
  - compare target: doctrine item 7 text; guard `--selftest`.
  - verify before: any claim about merge authority.

## Active Objective

Turn the proven manual lane-start prune into a documented, owner-gated standing rule so worktree/branch sprawl cannot rebuild — the cleanup complement to the now-live auto-merge bot.

## Exact Next Authorized Action

1. Run the Cynefin Routing Layer (`.agents/workflow-overlay/decision-routing.md`) — this is doctrine-changing.
2. Resolve the Open Decision with the owner: the rule's home (recommend (b) — a new Decision item in `docs/decisions/dev_workflow_ci_branch_protection_doctrine_v0.md`) and form (recommend agent-instruction-only first).
3. Draft the rule in the chosen surface: at each NEW lane's start, run `git fetch --prune origin`, then `git worktree remove` (non-force) any worktree whose branch is `[gone]` and has no open PR, then `git branch -D` those `[gone]` branches — with the Drift Guard exclusions stated inline.
4. Validation/stop: lands via a per-lane PR off main (squash). Owner CLI-merges (or labels `agent-automerge` for the bot). Do NOT execute a fresh destructive sweep as part of authoring (the backlog sweep is done); do NOT edit the guard.

## Authority And Source Ledger

- Repository instructions: `AGENTS.md` (+ `CLAUDE.md` shim) → `.agents/workflow-overlay/README.md`. Load-bearing: yes. reread-required.
- Overlay / doctrine: `docs/decisions/dev_workflow_ci_branch_protection_doctrine_v0.md` — per-lane PR off main, squash default (item 5), `delete_branch_on_merge` on (item 4), lane-isolation early-detection detector (item 8), auto-merge bot (item 9). Load-bearing: yes. Compare target: `git ls-tree origin/main docs/decisions/dev_workflow_ci_branch_protection_doctrine_v0.md`. reread-required (the doc grows fast).
- `.github/scripts/lane-health-check.ps1` — existing read-only worktree-sprawl WARN-at->4 detector; candidate wiring point if the owner chooses the detector form. Load-bearing: yes (for form (b)-with-wiring). Compare target: file exists on origin/main; reread before wiring.
- `.agents/workflow-overlay/decision-routing.md` — Cynefin router; doctrine-changing work routes here first. Load-bearing: yes. reread-required.
- User constraints: owner-gated; lands via lane PR; non-force prune only; never prune the seal/open-PR/[ahead] worktrees; do not throttle creation.
- Source gaps: none known at packet time.
- Strict-only blockers: none — this is an additive doctrine/behavioral rule, no validation gate to clear beyond CI on the lane PR.
- Not-proven boundaries: the rule is not yet written or accepted; the "stays bounded over time" outcome is unproven until the rule is live across several lanes.

## Current Task State

- Completed (this thread): the one-time backlog sweep (worktrees 53→29; 7 branches deleted by this thread + concurrent activity); the auto-merge bot built, cross-vendor reviewed/hardened, and LANDED (PR #97 merged) — the merge half.
- Partially completed: nothing for THIS lane — the auto-prune rule is not started (this packet is the intake).
- Broken or uncertain: nothing broken. The sweep proved the prune commands work; what remains is to make it a standing rule.

## Workspace State

- Branch: receiver opens a fresh lane off `origin/main`.
- Head: `origin/main` = `02e91e2` at packet creation (reread).
- Dirty/untracked before handoff: the primary checkout (`…/orca`) sits on `ecr-sp3-timing-deriver-slice1` with pre-existing untracked scratch — unrelated to this lane.
- Dirty/untracked after writing this file: this packet newly created + untracked on `lane-start-auto-prune-handoff-v0`.
- Target files or artifacts (the rule lane will likely touch ONE of): `docs/decisions/dev_workflow_ci_branch_protection_doctrine_v0.md` (recommended), or `AGENTS.md`, or an overlay file; optionally `.github/scripts/lane-health-check.ps1`.
- Related worktrees: do NOT prune `orca-seal-wt` [pilot-seal-outcome] or any `[ahead]` worktree.

## Frozen Decisions

- Decision: Automate the cleanup TAIL, not throttle creation.
  - Evidence: the velocity mismatch is agent-fast creation vs human-gated cleanup; the bot (item 9) closed the merge half.
  - Consequence: the rule fires at lane START (cleanup rides on the next creation), zero new infra.
- Decision: `git worktree remove` must be NON-FORCE.
  - Evidence: this thread's sweep — non-force refused every dirty worktree, protecting unsaved work.
  - Consequence: a dirty worktree is left for the owner, never force-discarded.
- Decision: a local git hook does NOT fit.
  - Evidence: PR merges are server-side, so a `post-merge` client hook never fires.
  - Consequence: the right shape is a lane-start agent rule (and/or a scheduled detector), not a git hook.

## Mutable Questions

- Question: home + form of the rule (see Open Decision).
  - Why still mutable: owner/architecture call.
  - What would resolve it: owner picks (a)/(b)/(c) and instruction-only vs wired.
- Question: should the rule also delete branch-only `[gone]` branches (no worktree), or only worktree-bound ones?
  - Why still mutable: scope choice; branch-only `[gone]` deletes are cheap but a separate step.
  - What would resolve it: owner preference; recommend including both (the sweep did).

## Superseded / Dangerous-To-Reuse Context

- Stale: any worktree/branch list in this packet or prior notes.
  - Why dangerous: the repo moves fast (the sweep itself saw 53→35→29 within one session); a stale list will name worktrees that no longer exist or miss new ones.
  - Current replacement: re-derive live with `git worktree list` + `git for-each-ref … | rg '\[gone\]'` and `gh pr list --state open` before any prune.

## Commands And Verification Evidence

- Proven prune commands (this thread, on Windows PowerShell / git):
  ```
  git fetch --prune origin
  git worktree remove "<absolute-worktree-path>"          # NON-force; refuses dirty
  git branch -D <gone-branch>                              # capital -D: squash-merge leaves branches non-ff
  ```
  Result:
  - Passed: 6 merged worktrees removed + 6 `[gone]` branches deleted cleanly this session; dirty worktrees correctly REFUSED (kept).
  - Re-run target so the receiver can confirm: `git worktree list | rg -c .` (count), `git for-each-ref --format='%(refname:short) %(upstream:track)' refs/heads | rg '\[gone\]'`, `gh pr list --repo eric-foo/orca --state open --json number,headRefName`.
- Auto-merge bot live:
  ```
  gh pr view 97 --repo eric-foo/orca --json state,mergedAt
  ```
  Result: MERGED, mergedAt 2026-06-14T14:36:46Z.

## Blockers And Risks

- Risk: pruning a worktree on an open PR, or the seal/[ahead] worktrees.
  - Evidence: open-PR + unpushed-work worktrees hold live/irreplaceable state.
  - Likely next action: the rule's exclusion clauses (Drift Guard) + non-force remove.
- Risk: deleting a `[gone]` branch from a CLOSED-unmerged PR (work not on main).
  - Evidence: a manually-deleted remote branch also reads `[gone]`.
  - Likely next action: glance `gh pr list --state all --head <branch>` for closed-unmerged before `-D`.
- Risk: scope-creep into a destructive always-on automation.
  - Evidence: the temptation to "just wire a cron that force-prunes."
  - Likely next action: hold to agent-instruction-only first; any automation is non-force + owner-gated.

## Confirm-Don't-Trust Load Checklist

- Re-verify before acting:
  - `origin/main` head (moved since `02e91e2`) — `git rev-parse origin/main`.
  - the dev-workflow doctrine's current item numbering/style (items 8, 9 present) — `git ls-tree origin/main` + read the file.
  - the auto-merge bot is live — `gh pr view 97` MERGED + `auto-merge.yml` on main.
  - live worktree/branch/open-PR state — the re-run targets above.
- Load outcomes: `REUSE` only after the doctrine surface + bot-live facts re-verify; `STALE_REREAD_REQUIRED` if the doctrine moved; `BLOCKED_UNVERIFIABLE` if a load-bearing source is missing.
- Sources that must be reread if drift detected: the dev-workflow doctrine, the overlay README, decision-routing.

## Do Not Forget

- The seal worktree (`orca-seal-wt` / `pilot-seal-outcome`) must NEVER be pruned and its sealed file NEVER read — outcome-blind is permanent.
- This is the CLEANUP half; the MERGE half (auto-merge bot) is already live — do not rebuild it.
