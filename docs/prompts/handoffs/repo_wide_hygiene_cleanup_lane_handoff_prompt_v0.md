# Repo-Wide Hygiene Cleanup Lane — Handoff Prompt v0

```yaml
retrieval_header_version: 1
artifact_role: Planning handoff prompt (docs/prompts/handoffs/; cleanup-lane commission)
scope: >
  Commissions one bounded repo-wide hygiene cleanup lane: inventory the whole
  repo with the existing mechanical checkers plus targeted sweeps, classify
  every finding (mechanically-safe / queue-routed / owner-gated), execute ONLY
  the mechanically-safe docs-write class, write queue rows for the rest, and
  deliver an owner decision memo for deletions, branch/worktree pruning, and
  disposition questions. Carries the commissioning thread's verified
  orientation capsule (2026-06-11) so the lane does not rediscover the repo.
use_when:
  - Spinning up the repo cleanup lane in a fresh session (owner-couriered).
  - Checking what that lane may fix itself versus what it must route to the owner.
authority_boundary: retrieval_only
open_next:
  - docs/hygiene/queue.md                                   # the routing record this lane reads and extends
  - docs/decisions/orca_repo_structure_binding_v0.md        # placement parameters; Phase-2 applied 2026-06-11
  - .agents/workflow-overlay/artifact-folders.md            # placement authority
  - .agents/workflow-overlay/source-of-truth.md             # checkpoint lifecycle + DCP contract
stale_if:
  - The hygiene queue's open/settled row set changes materially (re-read it on intake; it is the live state, this prompt is the snapshot).
  - A repo-structure or artifact-folders change lands (re-anchor placement rules before fixing placement findings).
branch_or_commit: ecr-sp3-timing-deriver-slice1 @ 48c00ca at authoring (concurrent lanes commit freely; intake re-checks)
```

## Thread Operating Target

`Bring the repo to a clean, navigable, checker-passing state — dead pointers
fixed, stale language trued, debris classified — without disturbing live
lanes, sealed materials, or owner-settled decisions.`

```yaml
thread_operating_target_continuity:
  carried_forward: no
  reason: no_visible_active_target   # new lane; commissioned from a courier/cleaning thread
  changed_from_input: no
  lifecycle_status: active_from_this_commission
```

## Cynefin Routing

Commissioning classification (2026-06-11, per
`.agents/workflow-overlay/decision-routing.md`): regime **Mixed** —
mechanically-clear sweeps coexist with owner-gated dispositions and live-lane
hazards; decomposition **split and classify** (inventory → classes → bounded
apply). Bottleneck: telling debris from live concurrent-lane state. Riskiest
assumption: "stale-looking equals safe-to-touch" — several resolved-retain
decisions look like debris but are owner-settled. Re-run the router on intake.

## Preflight

```text
orca_start_preflight:
  agents_read: required on intake (fresh read)
  overlay_read: required on intake (.agents/workflow-overlay/README.md)
  source_pack: S1 map + the targeted reads in open_next + checker outputs
  edit_permission: docs-write (mechanically-safe class only; everything else routes)
  target_scope: repo-wide hygiene inventory + bounded safe fixes + queue rows + owner memo
  dirty_state_checked: required on intake (expect concurrent churn; census it, do not assume)
  blocked_if_missing: hygiene queue unreadable, or checker scripts absent
repo_map_decision: loaded
repo_map_reason: whole-repo navigation work; the map and its consolidation submaps are both inventory inputs and potential fix targets
doctrine_change: none authorized. Pointer/path/status-text fixes are not doctrine;
  any fix that would change a rule's MEANING in AGENTS.md or the overlay is
  owner-gated and routes to the memo (with a direction_change_propagation
  receipt owed by whoever applies it).
external_source_boundary: external workflow source read-only; jb is not Orca authority.
commits: ask the owner at lane start. Default: leave fixes uncommitted and list
  them; with owner word, use small grouped commits with explicit paths
  (git commit --only -- <paths>) and repo-map-ack tokens where the freshness
  hook asks.
```

## Orientation Capsule (verified by the commissioning thread, 2026-06-11)

Trust this over rediscovery, but verify pins on intake — the repo moves daily.

**Hygiene queue state** (`docs/hygiene/queue.md`): rows 001/002/004/005/008/009/011/012/013/014
are RESOLVED — rows 002/004/005 are owner-approved RETAIN-IN-PLACE decisions:
the v0_14 superseded spec versions, the 19 loose review-outputs files, and the
advisory/review-prompt placements are SETTLED. **Do not relitigate or "fix"
them.** Open rows: 003 (pass-2 checker adoption — owner decision, review_by
2026-06-12), 010 (three quarantined `docs/_inbox/` strays — owner disposition:
delete or promote), 006/007 (event-triggered, deliberately dormant — leave).

**Mechanical checkers that exist** (run these as Phase A, report mode first):
- `.agents/hooks/check_retrieval_header.py --strict` (EP-06; known gap:
  `.agents/workflow-overlay/safety-rules.md` lacks a header — previously left
  to the owner as forward-only; do not silently backfill headers on docs whose
  lane you cannot identify).
- `.agents/hooks/check_placement.py --strict` (EP-04; reads
  `repo-structure.yaml`; `_`-prefixed dirs and named generated patterns are
  excluded by design).
- `.agents/hooks/check_repo_map_freshness.py --strict`.

**Known debris and hazards:**
- `orca-harness/_test_runs/`: ~24 `run_*` directories, each a full copy of
  test scaffolding. Absent from `git status` (appears gitignored — confirm
  before claiming). Disk debris at most: disposal is an owner-memo
  recommendation, never a lane action.
- `_scratch/` (repo root): scratch by binding; contains a saved external
  webpage (`gijn_toolkit.html`). Leave; note in memo if aged.
- `docs/research/creator_momentum_data_landscape_v0.md`: appeared untracked
  MID-SESSION on 2026-06-11 — almost certainly a live lane's working file.
  Touch nothing about it unless it is still orphaned and aged at your intake.
- `docs/_inbox/`: `inbox.max_age_days: 30` is an advisory aging signal; spent
  precompact/handoff checkpoints are burn-after-consumption per
  source-of-truth's Checkpoint Artifacts section — a SPENT checkpoint found
  here is deletable-class, but route to the memo if you cannot prove it was
  consumed.
- Branch/worktree sprawl: ~17 local branches; `git branch` entries prefixed
  `+` are checked out in linked worktrees (live-lane indicators — at authoring:
  capture-archive-*, capture-cloak-*, capture-demand-projection,
  capture-probe-tiktok-demand, capture-rung15-*, capture-spine-bounded-*,
  codex/*, consumer-demand-probe, doctrine-harness-caveat, hooks-readme).
  Inventory with last-commit dates and merged-status; pruning is OWNER-GATED,
  one list in the memo, zero deletions by this lane.
- Stale-language class with proven instances: pre-Phase-2 flat
  `docs/product/<file>` references that should be by-lane
  (`docs/product/<lane>/<file>`). The judgment-spine manifest had nine
  (fixed 2026-06-11); sweep the rest of docs/ for the same class. Related:
  fired-but-unretired `stale_if` triggers, and `open_next` entries pointing at
  nonexistent paths (three were found pointing at files that had moved to
  `core_spine/`).

**Sealed-material skip rule (hard):** files marked facilitator-only / sealed
(e.g. `docs/research/orgmotion_beautypie_sealed_outcome_facilitator_only_v0.md`)
and batch-1 case-outcome material: read HEADERS only, never bodies; never
move, rename, excerpt, or quote them. This lane becomes outcome-aware the
moment it reads one — it must never be reused for batch-1 contestant or
recognition work regardless.

**Concurrent-lane rule (hard):** never commit, move, edit, or delete another
lane's uncommitted files; when ownership is unclear, the finding goes to the
memo, not your hands.

## Commission

**Phase A — Inventory (read-only).** Run the three checkers in report mode;
census `git status` untracked/modified by apparent lane; branch/worktree
inventory (last commit date, ahead/behind main, merged-status); `docs/_inbox/`
aging audit; dead-pointer sweep (`open_next`, `input_hashes` paths, inline
`docs/...` references that fail existence checks); stale-language sweep
(pre-Phase-2 flat product paths; "PROPOSED"/"pending" statuses contradicted by
the owning doc; fired `stale_if` triggers). Record every finding with path,
evidence, and proposed class.

**Phase B — Classify.** Three classes, every finding in exactly one:
1. `mechanically_safe` (docs-write, meaning-preserving): dead pointers to
   moved files, stale path text, statuses contradicted by their own primary
   source, retired triggers. Bar: the fix changes where a reader is routed or
   what state-text says, never what a rule means, and the owning lane is
   identifiable or the file is shared-routing (maps, queue, manifests).
2. `queue_routed`: real but not-now work — new ORCA-HYGIENE rows with
   created date, location, reason, boundary, promote-to, review condition,
   review_by.
3. `owner_gated`: ALL deletions, branch/worktree pruning, `_test_runs`
   disposal, inbox stray disposition (fold with row 010), header backfills on
   unowned docs, anything touching settled rows, sealed materials, or another
   lane's files.

**Phase C — Apply and report.** Execute class 1 only, each fix verified by
fresh read; append class-2 rows to the queue; write the cleanup report to
`docs/hygiene/repo_cleanup_pass_2026_06_v0.md` (findings table by class,
checker outputs summarized, fixes applied with verification evidence, the
owner memo as its final section: one decision list with per-item
recommendation and blast radius). Close with the headed human summary, then
path/hash/status receipts.

## Hard Constraints

- Zero deletions, zero `git branch -d/-D`, zero worktree removal, zero
  `git clean`, zero history rewriting — recommend only.
- Do not reopen owner-settled queue rows (001/002/004/005 retain decisions
  especially); do not act on dormant 006/007.
- Sealed-material skip rule and concurrent-lane rule above are absolute.
- Overlay/AGENTS.md edits: pointer-or-typo class only; anything
  meaning-bearing is owner-gated (+ DCP receipt owed by the applier).
- No implementation/runtime work; checker SCRIPTS are run, never edited.
- Stay smallest-complete: navigability fixes, not rewrites, restyling, or
  speculative reorganization; `_archive/` folders remain explicitly deferred.

## Output Mode And Contract

`file-write` (docs-write). Durable outputs: the cleanup report (path above),
queue-row appends, and the class-1 fixes themselves. The owner memo lives in
the report, not a separate decision file. New durable artifacts carry
retrieval headers per `.agents/workflow-overlay/retrieval-metadata.md`.

## Validation Gates

- `orca_start_preflight` recorded; checker runs recorded with their actual
  output (a checker that cannot run is a named blocker, not a skipped step).
- Every class-1 fix verified by fresh read with shown evidence; every claim of
  absence ("no other stale paths") backed by the search that proved it.
- Findings are hygiene/routing defects only — fixing them proves
  navigability, never validation, readiness, or acceptance.
- Prompt verdict at authoring: PASS_WITH_WARNINGS (warnings: repo state moves
  daily — the capsule is orientation, intake re-verifies; commit authority is
  deliberately unbound until the owner speaks at lane start).

## Non-Claims

Commissions one bounded hygiene pass. Not validation, not readiness, not a
reorganization mandate, not deletion/pruning authority, not doctrine change,
not a standing janitor role — the lane ends at its report. The orientation
capsule is the commissioning thread's verified snapshot, not a substitute for
the lane's own intake checks.
