# Handoff Packet — creator_profile_current lake cut-over (FINISH: make it lake-fed/fresh)

```yaml
retrieval_header_version: 1
artifact_role: Workflow handoff
scope: >
  Cold handoff to FINISH the creator_profile_current lake cut-over. The lake
  reading/selection/snapshot/producer machinery is built and merged, but the
  registry view is still SEED-FED: the live switch to lake-fed (Migration
  §4 produce-rollups+first-snapshot, §5 re-point materialize) plus freshness
  gate (§6), CI flip (§7), and YouTube fold-in (§8) are NOT done. Identity
  ledger is fenced; the IG creator set is now hyram/jeremyfragrance/milanscents.
use_when:
  - Continuing the creator_profile_current lake cut-over from a fresh lane.
  - Producing the first real-lake IG snapshot and re-pointing materialize.
  - Checking the cut-over's honest status (what is lake-backed vs still seed-fed).
authority_boundary: retrieval_only
open_next:
  - orca/product/spines/capture/core/source_families/social_media/creator_registry/creator_profile_current_lake_cutover_architecture_v0.md
  - orca-harness/capture_spine/creator_profile_current/materialize.py
  - orca-harness/capture_spine/creator_profile_current/silver_metric_snapshot.py
  - orca-harness/runners/run_creator_metric_rollup_snapshot.py
  - orca-harness/runners/run_creator_metric_rollup_producer.py
stale_if:
  - materialize.py re-points onto the snapshot (metric_snapshot_pointer appears) — §5 done, this handoff superseded.
  - The first real-lake snapshot is committed under .../instagram/.
```

## Load Contract

- packet_version: 1
- mode: max
- created_at: 2026-06-30 (cut-over implementation thread)
- created_by_lane: worktree `worktrees/creator-snapshot-runner` (re-branched across lanes); provenance only, not authority
- workspace: `C:\Users\vmon7\Desktop\projects\orca` (main repo). **Real lake is EXTERNAL** at `F:\orca-data-lake` via `ORCA_DATA_ROOT`.
- handoff_path: `docs/workflows/creator_profile_current_lake_cutover_handoff_v0.md`
- expected_branch: **start a FRESH worktree off `origin/main`** (do NOT reuse the sender's `worktrees/creator-snapshot-runner` — it is re-branched constantly)
- expected_head: `origin/main @ f90d72e3` at handoff time. RE-VERIFY: `git -C <repo> fetch origin && git rev-parse --short origin/main` — main moves fast.
- expected_dirty_state_including_handoff_file: this handoff doc is newly created on branch `creator-cutover-handoff` (untracked → committed there).
- load_rule: confirm-don't-trust; re-verify every load-bearing fact against its compare target before acting; sender claims are hypotheses, not authority.

## Goal Handoff

- long_term_goal: Make `creator_profile_current` a source-backed, self-refreshing creator-stats registry that stops going manually stale (eventual horizon: a queryable creator-intelligence surface — out of scope here).
- anchor_goal: **Finish the lake cut-over so the registry is LAKE-FED, not seed-fed** — complete Migration §4 (produce rollups into the real lake + first snapshot) and §5 (re-point `materialize` onto the snapshot), then §6 (freshness gate) / §7 (CI flip) / §8 (YouTube fold-in).
- success_signal: `materialize` reads the committed lake **snapshot** (not the seed) for IG; the view regenerates from lake rollups; CI verifies it deterministically **lake-free**; a freshness receipt + gate make drift non-silent. The IG view numbers MAY legitimately differ from the old seed — that is freshness, not a bug.

## Open Decision / Fork

- decision: **§4's "first snapshot vs seed" is an INSPECTION DIFF, not a hard equality gate.** Against the real lake, fresh captures legitimately differ from the stale hand-kept seed. Adapter correctness is ALREADY proven in CI by the temp-lake equivalence gate (PR #522, `test_ig_lake_path_rollups_equal_seed_builder_no_drift`). So §4 = generate the first real snapshot and **inspect** the seed→lake delta (investigate a large delta as freshness-vs-real-data-producer-bug), NOT assert `== seed`.
  - options: (a) §4 then §5 sequentially [recommended]; (b) additionally build the capture→produce→snapshot **coupling** (owner-accepted "B1": file-per-capture, publish-per-batch, with `rebuild_availability` made skippable in the coupled path) — bigger, can follow §5.
  - already constrained / off the table: the hardened-α ordering design is settled (don't re-litigate); the identity ledger is fenced (no further edits without owner direction); CI stays lake-free; no byte-equality-to-seed assertion.
  - trade-offs: doing §4 needs the real lake (operator box, `F:\` mounted) and writes durable append-only records; a fresh lane on CI / another box cannot run §4.
  - owner of the call: the owner/operator (durable lake writes + the seed→lake delta interpretation are owner-gated).
  - recommendation: merge #531 → §4 (produce 3 IG rollups + dry-run snapshot, inspect the delta) → §5 (re-point materialize) → §6/§7/§8. Treat the delta as freshness.

## Drift Guard

- **Identity ledger** (`.../creator_registry/creator_public_handle_linkage_ledger_v0.json`) is **FENCED** — do NOT edit it further without explicit owner direction. The milan-for-vanz swap (#531) was a one-off owner-directed exception, not license to keep changing the creator set.
- Do NOT re-litigate the **hardened-α ordering**: `selection_run_id` is owned by the snapshot run (`max(prior)+1`), NEVER a producer-clock field; STEP 1's `computed_at` guards are a load-bearing cross-check; the watermark is a content-hash set, not a clock.
- **missing ≠ zero**; CI **never** resolves the real lake; **determinism** (no wall-clock in generators — `snapshot_generated_at`/`generated_at_utc` are caller-supplied); the real lake is EXTERNAL (`F:\orca-data-lake`) and a fresh lane on a different box / CI will NOT have it.
- The "first snapshot == seed" idea is an **inspection diff**, NOT a hard gate (lake is legitimately fresher).
- IG capture is **login-walled when logged-out**. The working path uses the residential proxy `reddit-res-01`, whose store is in the **MAIN repo** `orca-harness/_proxy_profiles` (NOT in worktrees — pass `--proxy-root <main-repo>/orca-harness/_proxy_profiles`). Do NOT drive the authenticated `_auth_state` IG session autonomously (operator's logged-in account; ban risk).

## Inherited Context (does NOT flow to a new lane)

### Source-loading state to re-establish (follows overlay doctrine)

- overlay source-loading policy: read `.agents/workflow-overlay/README.md` FIRST (Orca overlay governs); `AGENTS.md` for triggers. (`repo-overlay-bound`.)
- targets to enter the ladder: the architecture doc (below) — sections **Migration (smallest-first) §4–§8**, **Two gates**, **Freshness mechanism (AR-02)**, **How materialize consumes it (AR-05)**, **Reversibility (AR-07)**.
- already loaded (weak orientation, freshness = `origin/main @ f90d72e3`; NOT authority): the merged modules + runners in the source ledger below.
- must load first (before strict/actionable steps): the architecture doc; `materialize.py` (the §5 re-point target); `validation.py` (the drill-back keys); `silver_metric_snapshot.py` (the generator the snapshot runner calls).
- load rule: re-run progressive source loading per the overlay; this packet's loaded-set only seeds the ladder.

### Earlier-decided concepts (inline gist + verify pointer)

- **Hardened-α ordering** — `selection_run_id` owned by the snapshot run.
  - decided in: `orca-harness/capture_spine/creator_profile_current/silver_metric_snapshot.py` (module docstring) + architecture doc "Latest-rollup-per-account (AR-04)". Verify before strict use.
- **Value-equal (NOT byte-equal) no-drift bridge** — snapshot rollups are value-equal to the seed; the VIEW is canonicalized (`sort_keys=True`, PR #524 merged) so source key-order can't change it.
  - decided in: architecture doc "No-drift bridge" (Recommended v0) + `materialize.dump_creator_profile_current_view`. The architecture doc was corrected from "byte-equal" → "value-equal" this lane.
- **The temp-lake equivalence gate IS the adapter-correctness proof**; the real-lake "== seed" is an inspection diff.
  - decided in: architecture doc §4 + `tests/unit/test_creator_metric_silver_snapshot.py::test_ig_lake_path_rollups_equal_seed_builder_no_drift` (PR #522, merged).
- **IG registry set is now hyram / jeremyfragrance / milanscents** (vanzzcoser removed).
  - decided in: PR #531 (OPEN, MERGEABLE — MUST MERGE before §4/§5). Verify: `gh pr view 531 -R eric-foo/orca --json state,mergeable`.

## Active Objective

Finish the lake cut-over so the registry is lake-fed/fresh: §4 (produce IG rollups into the real lake + first snapshot) → §5 (re-point `materialize`) → §6 (freshness gate) / §7 (CI flip) / §8 (YouTube fold-in).

## Exact Next Authorized Action

0. **Merge PR #531** (milan-for-vanz registry swap) first — else §4/§5 run on the stale vanzzcoser set. It is MERGEABLE (CI gate is the only wait).
1. **(§4 — REQUIRES the real lake at `F:\`)** Produce rollups for the 3 IG creators into the lake. First RE-READ `runners/run_creator_metric_rollup_producer.py` (its `--projection` contract: it consumes RAW grid projections `{packet_id, rows}`; the lake projection records below ARE feedable). Then run it once per the 3 projections (APPEND-ONLY, durable):
   - milan: `F:\orca-data-lake\derived\057\01KWC89MF50H39PEQRG9V53FYY\projection_ig_reels_grid\01KWC8A2KRT2E6CER7DS764BXZ.json` (captured+projected this lane via proxy)
   - hyram: `F:\orca-data-lake\derived\01KW9T4ESARHD545RRPGCWWY1P\projection_ig_reels_grid\01KW9TYBFCV1Y6K3FVRJAPANQ3.json`
   - jeremyfragrance: `F:\orca-data-lake\derived\01KW9T5SGKBYD8HRVP3154F4Y8\projection_ig_reels_grid\01KW9TYSZA4A4Z4XQXW91S0VVY.json`
   - `python -m runners.run_creator_metric_rollup_producer --projection <p1> --projection <p2> --projection <p3>`
2. **(§4)** `python -m runners.run_creator_metric_rollup_snapshot --platform instagram` (DRY-RUN default — writes nothing) → inspect per-account numbers vs the seed (expect a freshness delta). Then `--write` to commit the snapshot + selection manifest + freshness receipt (default paths under `.../social_media/instagram/`).
3. **(§5)** Re-point `materialize` onto the snapshot (per architecture doc "How materialize consumes it (AR-05)"):
   - rename the view's `source_drill_back` key `metric_seed_pointer` → `metric_snapshot_pointer` in `materialize.py`;
   - update `validation.py`: `_ALLOWED_SOURCE_DRILL_BACK_KEYS` + the `_validate_source_drill_back` field reference;
   - flip `_collect_metric_rollup_records` to read the snapshot's `metric_rollups` (not `seed["metric_rollups"]`) for IG; `source_inputs` seed→snapshot pointer/sha256;
   - update the view spec + static-view test; regenerate the view (now lake-fed); validate (`--check` + creator suite).
4. **(§6/§7/§8)** §6 `live_lake_freshness_gate` runner + write-time receipt gate + scheduled drift check (`pytest.skip` in CI); §7 flip CI test expected paths seed→snapshot; §8 YouTube fold-in (own snapshot/gates/seed-retirement, AR-06).

## Authority And Source Ledger

- Repository instructions: `AGENTS.md` (root) + `.agents/workflow-overlay/README.md` (read first). Per-lane PR flow: `docs/decisions/dev_workflow_ci_branch_protection_doctrine_v0.md`.
- User constraints: finish the cut-over (make it fresh/lake-fed); identity ledger stays fenced; don't drive the authenticated IG session; don't block on CI watch (push/PR and move on).
- Source-read ledger:
  - `orca/product/spines/capture/core/source_families/social_media/creator_registry/creator_profile_current_lake_cutover_architecture_v0.md`
    - Role: the cut-over contract (Migration §4–§8, gates, AR-02/05/07). Load-bearing: **yes**. Compare target: present on `origin/main @ f90d72e3` (`git ls-tree origin/main -- <path>`); contains "value-equal" (NOT "byte-equal"). Reuse rule: re-read before §4/§5.
  - `orca-harness/capture_spine/creator_profile_current/materialize.py`
    - Role: the §5 re-point TARGET (still seed-fed). Load-bearing: **yes**. Compare target: `git grep -c metric_snapshot_pointer origin/main -- <path>` == **0** (still `metric_seed_pointer`). Reuse rule: re-read; flipping this is §5.
  - `orca-harness/capture_spine/creator_profile_current/silver_metric_snapshot.py`
    - Role: pure snapshot generator the snapshot runner calls. Load-bearing: yes. Compare target: on main; `generate_creator_metric_rollup_snapshot(...)`. Reuse rule: re-read; do not change anchoring.
  - `orca-harness/runners/run_creator_metric_rollup_snapshot.py` (snapshot runner, PR #518), `run_creator_metric_rollup_producer.py` (producer runner, PR #526)
    - Role: §4 operator runners. Load-bearing: yes. Compare target: both on main (`git ls-tree origin/main:orca-harness/runners | grep creator_metric_rollup`). Reuse rule: re-read the producer's `--projection` raw-projection contract before running.
  - `orca-harness/capture_spine/creator_profile_current/validation.py`
    - Role: §5 also edits drill-back keys here. Load-bearing: yes. Compare target: `_ALLOWED_SOURCE_DRILL_BACK_KEYS`. Reuse rule: re-read at §5.
  - identity ledger / IG seed / view (`.../creator_registry/...ledger_v0.json`, `.../instagram/instagram_reels_creator_metric_seed_v0.json`, `.../creator_registry/creator_profile_current_view_v0.json`)
    - Role: current registry state. Load-bearing: yes. Compare target: after #531 merges, IG set = hyram/jeremyfragrance/milanscents. Reuse rule: ledger is FENCED.
- Source gaps: the seed's original IG source projections are NOT committed (only the lake derived projections referenced in the seed `source_inputs` exist, at the `F:\` paths above). A fresh box without `F:\` cannot reproduce the seed.
- Not-proven boundaries: the registry is NOT yet lake-fed; NOT a runtime/query service (its own non_claims disclaim "SQLite/data-lake physicalization", "dashboard readiness").

## Current Task State

- Completed / merged to `origin/main`: STEP 1 (selection), 2a (discovery), 2b (snapshot generator), 3 (snapshot runner) [#502/504/513/518]; #522 (no-drift equivalence gate); #524 (view canonicalize, `sort_keys=True`); #526 (producer runner — lake-population wiring).
- Partially completed: PR #531 (milan-for-vanz registry swap) — OPEN, MERGEABLE, must merge.
- Not done (the actual lake-fed switch): §4 (lake has **0 rollups**), §5 (materialize still seed-fed), §6, §7, §8.

## Workspace State

- Branch (this handoff): `creator-cutover-handoff` off `origin/main @ f90d72e3`.
- Real lake: `F:\orca-data-lake` (mounted on this operator box; `ORCA_DATA_ROOT` set). **IG: 3 raw packets captured + grid-projected** (hyram `01KW9T6R...`, jeremyfragrance `01KWA193...`, milanscents `01KWC89MF50H39PEQRG9V53FYY`); **0 `creator_metric_rollup_silver` rollups**; 64 YT packets. Compare target: `r.list_available(source_family='instagram_creator')` → 3; `derived rglob creator_metric_rollup_silver` → 0.
- Target files for §5: `materialize.py`, `validation.py`, the view spec + static-view test.
- Related: the sender's worktrees (`worktrees/creator-snapshot-runner` re-branched; others prunable) — do NOT reuse; start fresh off main.

## Changed / Inspected / Tested Files (this lane, for orientation)

- Merged: `runners/run_creator_metric_rollup_snapshot.py`, `runners/run_creator_metric_rollup_producer.py`, `capture_spine/creator_profile_current/silver_metric_snapshot.py` (+ reader/producers), `tests/unit/test_creator_metric_silver_snapshot.py` (equivalence gate), `materialize.py` (`dump_creator_profile_current_view` now `sort_keys=True`).
- Pending (#531): the ledger + IG seed + view (vanz→milan).

## Frozen Decisions

- Hardened-α ordering (selection_run_id owned by the snapshot run). Evidence: `silver_metric_snapshot.py` docstring + architecture AR-04. Consequence: do not re-litigate.
- Value-equal (not byte-equal) bridge + canonical view (#524). Evidence: architecture "No-drift bridge"; `dump_creator_profile_current_view`. Consequence: §4 inspects values, not bytes.
- Equivalence gate (#522) is the adapter proof; real-lake == seed is an inspection diff. Consequence: §4 does not hard-gate on seed equality.

## Mutable Questions

- When to build the capture→produce→snapshot **coupling** (B1) — during §4/§5 or after? What would resolve it: owner preference + whether per-batch publish is wanted now.
- Whether the seed is retired at §5 (IG) or kept as oracle until §8 (YT). What would resolve it: the architecture's seed-retirement rule (AR-06) + owner call.

## Superseded / Dangerous-To-Reuse Context

- The precompact restore packet at the sender's SCRATCHPAD (`...\scratchpad\creator_lake_cutover_precompact_v2.md`) — session-specific TEMP, NOT durable; a fresh lane must NOT rely on it. This handoff supersedes it.
- "byte-equal to seed" bridge wording — SUPERSEDED by **value-equal** (architecture doc corrected this lane).
- "first snapshot == seed" as a hard gate — SUPERSEDED by **inspection diff** (the temp-lake gate is the adapter proof).
- The earlier "2/3 IG creators / capture the missing one" framing — SUPERSEDED: the missing slot was cosplay (vanzzcoser), now swapped for fragrance (milanscents); all 3 IG are captured.

## Commands And Verification Evidence

- Validate (lake-free, matches CI):
  ```bash
  cd <repo>/orca-harness
  env -u ORCA_DATA_ROOT python -m pytest tests/unit/test_creator_metric_silver_*.py tests/unit/test_creator_profile_current_static_view.py -q
  env -u ORCA_DATA_ROOT python -m runners.run_creator_profile_current_materialize --check
  ```
  Result (at handoff): green, 1 operator-local skip; `--check` up to date. Re-run target so the receiver confirms rather than trusts.
- Confirm still seed-fed: `git grep -c metric_snapshot_pointer origin/main -- orca-harness/capture_spine/creator_profile_current/materialize.py` → 0.

## Blockers And Risks

- §4 requires the real lake (`F:\`) and writes durable append-only records — operator-gated; not runnable on CI / a fresh box without the lake.
- IG re-capture (if needed) is login-walled logged-out; needs the `reddit-res-01` proxy from the MAIN repo's `_proxy_profiles`.
- #531 unmerged → §4/§5 would run on the stale vanzzcoser set. Merge it first.
- Multiple view-touching changes have merged (#524) + are pending (#531); §5 also regenerates the view — expect to regenerate, not hand-merge.

## Confirm-Don't-Trust Load Checklist

- Re-verify before acting: `origin/main` HEAD (fetch); `materialize.py` still seed-fed (grep == 0); #531 mergeable/merged; lake IG packets == 3 and rollups == 0 (operator box only); the 3 lake projection paths still resolve.
- Load outcomes: `REUSE` only if all the above re-verify; `STALE_REREAD_REQUIRED` if main moved / §5 partly done; `BLOCKED_DRIFT` if the ledger was changed without owner direction; `BLOCKED_UNVERIFIABLE` if `F:\` lake is absent (a fresh box) — then §4 cannot run and the lane stops at "needs operator box".
- Sources to reread on drift: the architecture doc, `materialize.py`, the snapshot + producer runners.

## Do Not Forget

- The real lake is at `F:\orca-data-lake` on the OPERATOR box. A fresh lane on a different machine or CI will NOT have it — §4/§5's real-lake steps need it; verify before promising §4.
- **Merge #531 first** (milan in the registry).
- The proxy store is in the **MAIN repo** `orca-harness/_proxy_profiles`, not worktrees.
