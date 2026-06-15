# Handoff Packet — CA Coordination of the Demand-Durability Capture-Spine Rollout

```yaml
retrieval_header_version: 1
artifact_role: Cold cross-lane handoff packet (Chief-Architect coordination transfer; continuation artifact, not readiness evidence)
scope: Transfer the Chief-Architect coordination of the demand-durability capture-spine rollout to a fresh CA/coordinating thread.
authority_boundary: retrieval_only
```

## Load Contract

- packet_version: v0
- mode: max
- created_at: 2026-06-15
- created_by_lane: capture-spine Chief-Architect coordinating thread (provenance only; not an authority claim)
- workspace: C:\Users\vmon7\Desktop\projects\orca
- handoff_path: docs/prompts/handoffs/demand_durability_capture_spine_ca_coordination_handoff_v0.md
- expected_branch: a fresh worktree/branch off `origin/main` for any repo-changing follow-up (NOT the hot home branch `ecr-sp3-timing-deriver-slice1`)
- expected_head: `origin/main` was `10f370ed` at handoff; it moves fast (owner merges aggressively) — re-fetch.
- expected_dirty_state_including_handoff_file: this packet is newly created under tracked `docs/prompts/handoffs/` → untracked until committed on its lane.
- load_rule: **confirm-don't-trust** — re-verify every load-bearing fact (PR merge states, main HEAD, filenames) before acting; sender claims are hypotheses, not authority. The owner merges and renames aggressively mid-flow.

## Goal Handoff

- long_term_goal: a trustworthy demand-durability substrate for Orca's beauty-vertical demand-read — capture that does not silently lie about comparability, coverage, tampering, or sampling gaps — **without capture ever scoring or judging demand (INV-1)**.
- anchor_goal: **coordinate the demand-durability capture-spine rollout** from its current state (fully designed + hardened + handed-off + authorized, all merged on `main`) to a **running real commissioned series** — by driving the authorized builds (step 2 writer → step 3 scheduler) and, later, the deferred series-diff (Element 3).
- success_signal: the authorized fresh lanes build step 2 (the durability-series writer) then step 3 (the cadence runner/scheduler); a real commissioned series runs per the pilot protocol; series-diff (Element 3) follows once observations accrue; every step lands via a per-lane PR the owner merges, INV-1 preserved throughout.

## Open Decision / Fork

- decision: **the next coordination move now that the whole rollout is merged.**
  - options: (A) dispatch/route the **step-2 writer build** now to a fresh authorized lane (per the merged step-2 handoff); (B) wait for the owner to dispatch; (C) first do a cosmetic terminology pass (`proxy`→`indicator`) on the merged handoff docs.
  - already constrained / off the table: builds run in fresh lanes carrying the **bounded steps-2+3 authorization** (do not build in this coordinating thread); **landing to `main` stays owner-gated**; step 3 depends on step 2; series-diff Element 3 stays deferred.
  - trade-offs: (A) unblocks step 3 soonest; (B) owner-paced; (C) cosmetic only — the handoffs carry 0 stale *path* refs, so this is hygiene, not correctness.
  - owner of the call: the owner + the fresh CA.
  - recommendation: **(A) dispatch step 2 next** (it gates step 3); treat the terminology pass as optional. Also weigh the adjacent open capture-spine lanes below.
- adjacent open capture-spine lanes the CA may also weigh (NOT part of this rollout): **#94** `capture-publisher-history-ph-fixes` (still OPEN — the long-running publisher-history PH-01/02 fix from the #89-merged-ahead saga); **#112** `standing-capture-corpus-intake-contract`. Confirm their states before acting.

## Drift Guard

- **INV-1** (the load-bearing invariant): capture records observed facts + their limits, never weights, scores, ranks, or a durable-vs-hollow demand verdict. Everything in this rollout is bound by it.
- **no-gate-defeat**: anti-bot (honest/anti-blocking UA) OK; **STOP at any auth / CAPTCHA / Cloudflare *challenge***, record + re-probe (probe-then-pin). Never defeat a gate.
- **Commissioned capture only** (Ob.1): series are bounded + tied to a Decision Frame; never standing/opportunistic crawling.
- **Additive-optional schema** (the hardening): durability fields default unset; **no `SOURCE_CAPTURE_MANIFEST_VERSION` bump**; never break back-compat.
- **Series-diff (Element 3) is DEFERRED**: a cross-packet record needing an extracted-value extractor; when built it diffs EXTRACTED values (raw `PreservedFile.sha256` is only a coarse inspect-flag — distillation binding A1c). Do not build it as part of steps 2/3.
- **Bounded authorization**: the granted build authorization covers **steps 2 and 3 only** — NOT broader capture-spine work (no ECR/Cleaning/Judgment derivers, no source-quality scoring).
- **Confirm-don't-trust / cross-lane drift**: the owner merges + renames aggressively mid-flow. This rollout was twice bitten — **#89/#93** (a thing merged *ahead of* its in-flight fix) and **#106/#116** (files renamed `demand_proxy_*`→`demand_durability_indicator_*` between authoring and merge, creating dangling refs). Always re-verify current `main` filenames/PR-states before referencing or claiming.

## Inherited Context (does NOT flow to a new lane)

### Source-loading state to re-establish (follows overlay doctrine)

- overlay source-loading policy: `.agents/workflow-overlay/source-loading.md` (read `.agents/workflow-overlay/README.md` first, per AGENTS.md).
- targets to enter the ladder: the two build handoffs `docs/prompts/handoffs/demand_durability_series_writer_step2_handoff_v0.md` + `docs/prompts/handoffs/demand_durability_cadence_runner_step3_handoff_v0.md`; `docs/product/data_capture_spine/demand_durability_capture_pilot_v0.md` (§3 protocol + hardening targets); `orca-harness/source_capture/models.py` (hardened fields); `docs/product/data_capture_spine/core_spine_v0_data_capture_spine_obligation_contract_v0.md` (Ob.1, Ob.17); `docs/decisions/distillation_binding_data_capture_v0.md` (A1c).
- already loaded (weak orientation, freshness-marked; not authority): this packet's claims (sender verified at `origin/main 10f370ed`, all rollout PRs merged, main green).
- must load first: the two build handoffs + the pilot spec §3, before dispatching builds.
- load rule: receiver re-runs progressive source loading per overlay; the packet's loaded-set only seeds the ladder.

### Earlier-decided concepts and behaviors (inline gist + verify pointer)

- **Hardening landed (Elements 1/2/4 + Ob.17, additive-optional)**: the Capture Envelope now carries the durability fields as first-class optional schema. Decided in: `orca-harness/source_capture/models.py` + obligation contract Ob.17 (PR #113). Compare: `models.py` grep `intended_cadence`; reread-required. Verify before: any build that sets the fields.
- **Pilot proved the machinery on live data** (SdJ Bum Bum Cream, obs1+obs2): the per-observation protocol the builds automate. Decided in: `docs/product/data_capture_spine/demand_durability_capture_pilot_v0.md` (PR #108) §2–3. Compare: reread-required.
- **Distill A1c — series-diff-on-extracted-values** (Element 3 deferred; diff extracted values, raw hash = inspect-flag): Decided in `docs/decisions/distillation_binding_data_capture_v0.md` A1c (PR #107). Compare: grep `series-diff-on-extracted-values`; reread-required.
- **Bounded build authorization for steps 2+3** (owner, 2026-06-15): carried in the two build handoffs via the AGENTS.md accepted-handoff path. Verify in the handoff docs' "Build Authorization" sections.
- **Rename `demand_proxy_*` → `demand_durability_indicator_*`** (PR #106): the four indicator profiles + framing docs. Always use the NEW names. Verify: `git ls-tree origin/main docs/product/data_capture_spine/ | grep demand_durability_indicator`.

## Active Objective

Coordinate the demand-durability capture-spine rollout's remaining phases — the authorized step-2 (writer) and step-3 (scheduler) builds, then the first real commissioned series, then (later) series-diff Element 3 — from a fully-merged, green `main` baseline. Design, hardening, distillation, and both build handoffs are done and merged; nothing is mid-flight or broken.

## Exact Next Authorized Action

1. **Confirm-don't-trust**: `git fetch origin main`; confirm the rollout PRs (#107/#108/#113/#114/#115/#117) are MERGED and `main` is green (`check_map_links --strict` OK) — expected, but re-verify (owner moves fast).
2. Decide the next coordination move (Open Decision; recommend dispatch step 2).
3. **Dispatch the step-2 writer build** to a fresh authorized lane, pointing it at `docs/prompts/handoffs/demand_durability_series_writer_step2_handoff_v0.md` (it carries the bounded authorization). Optionally render a courier prompt via `workflow-prompt-orchestrator`.
4. After step 2 lands, **dispatch step 3** (`demand_durability_cadence_runner_step3_handoff_v0.md`).
5. **Commission the first real series** (owner picks SKU/source + Decision Frame; the pilot used Sol de Janeiro Bum Bum Cream via `direct_http`).
6. Later, separate lane: **series-diff Element 3** (with the A1c extracted-value anchor).

This coordinating thread does not itself build (it dispatches + adjudicates); builds happen in the authorized fresh lanes.

## Authority And Source Ledger

- Repository instructions: `AGENTS.md` + `.agents/workflow-overlay/` (read overlay `README.md` first).
- Overlay authority: source-loading; dev-workflow / per-lane PR (`docs/decisions/dev_workflow_ci_branch_protection_doctrine_v0.md`); safety / no-gate-defeat + commissioning (`.agents/workflow-overlay/safety-rules.md`, obligation contract Ob.1); delegated-review-patch + review-lanes (for any review steps).
- User constraints: token-conscious; wants real steps done; confirm-don't-trust; owner merges aggressively; bounded build authorization granted for steps 2+3 only; series-diff deferred.
- Source-read ledger (all on `origin/main 10f370ed`):
  - `docs/prompts/handoffs/demand_durability_series_writer_step2_handoff_v0.md` — Role: step-2 build handoff (carries bounded auth). Load-bearing: **yes**. Compare: `reread-required`. Reuse: dispatch from it.
  - `docs/prompts/handoffs/demand_durability_cadence_runner_step3_handoff_v0.md` — Role: step-3 build handoff (depends on step 2). Load-bearing: **yes**. Compare: `reread-required`.
  - `docs/product/data_capture_spine/demand_durability_capture_pilot_v0.md` — Role: protocol §3 + hardening targets. Load-bearing: **yes**. Compare: `reread-required`.
  - `orca-harness/source_capture/models.py` — Role: hardened durability fields. Load-bearing: **yes**. Compare: grep `intended_cadence` / `session_visibility_pin`; `reread-required`.
  - `docs/product/data_capture_spine/core_spine_v0_data_capture_spine_obligation_contract_v0.md` — Role: Ob.1 commissioning + Ob.17 durability obligation. Load-bearing: **yes**. Compare: grep `Demand-Durability Series Facts`.
  - `docs/decisions/distillation_binding_data_capture_v0.md` — Role: A1c series-diff cell (deferred). Load-bearing: no. Compare: `reread-required`.
  - the four `demand_durability_indicator_*_capture_profile_v0.md` — Role: the indicator capture profiles (renamed by #106). Load-bearing: no (context). Compare: `git ls-tree origin/main docs/product/data_capture_spine/`.
- Source gaps: the step-2 writer + step-3 scheduler are unbuilt (handed off).
- Strict-only blockers: none on `main` (it is green); the builds need their bounded authorization (granted in the handoffs) + the owner's per-lane merges.
- Not-proven boundaries: no real over-time series has run; series-diff (Element 3) unbuilt; the writer/scheduler unbuilt.

## Current Task State

- Completed (merged on `origin/main 10f370ed`): demand-read taxonomy/spec → live pilot proof (#108) → distill A1c (#107) → hardening Elements 1/2/4 + Ob.17 (#113) → step-2 build handoff (#114) → step-3 build handoff (#115) → stale-ref fixes (#117 + #116). `main` green.
- Partially completed: the rollout's BUILD phase — steps 2 and 3 handed off + authorized but NOT yet built.
- Broken or uncertain: none in the demand-durability rollout. Adjacent capture-spine lanes #94 (PH fix) + #112 (standing-capture intake) are OPEN and separate — confirm their states.

## Workspace State

- Branch: receiver creates a fresh worktree/branch off `origin/main` for any repo-changing follow-up.
- Head: `origin/main 10f370ed` at handoff (moves; re-fetch).
- Dirty/untracked before handoff: the home thread (`ecr-sp3-timing-deriver-slice1`) carries unrelated untracked files; do not work there.
- Dirty/untracked after writing this handoff file: + this file (untracked under `docs/prompts/handoffs/` until committed on its lane).
- Target files/artifacts: dispatching reads the two build handoffs; no source edits in the coordination lane itself.
- Related worktrees/branches: many merged rollout lanes are prunable (hardening/pilot/distill/handoffs/fix). Several stale worktrees exist under `.claude/worktrees/` + `orca-worktrees/` (owner hygiene).

## Frozen Decisions

- Hardening = additive-optional, no manifest bump (#113). Consequence: builds SET the fields; don't reshape the schema.
- Series-diff Element 3 deferred (#107 A1c). Consequence: not built in steps 2/3.
- Bounded build authorization = steps 2+3 only (owner, 2026-06-15). Consequence: build those two without re-asking; nothing broader; main owner-gated.
- INV-1 + commissioned-only (Ob.1). Consequence: facts-not-verdicts; bounded series.
- `demand_proxy_*` renamed → `demand_durability_indicator_*` (#106). Consequence: always use the new names.

## Mutable Questions

- Step-3 scheduler mechanism (operator-triggered per-slot [recommended] vs cron-bounded vs queue) — in the step-3 handoff.
- First commissioned SKU/source set + Decision Frame for the real series — owner input.
- When to build series-diff Element 3 — after enough observations accrue.
- Whether to do the cosmetic `proxy`→`indicator` terminology pass on the merged handoff docs.
- Whether/when to drive the adjacent capture-spine lanes (#94 PH fix, #112 standing-capture).

## Superseded / Dangerous-To-Reuse Context

- **`demand_proxy_*` filenames** — superseded by `demand_durability_indicator_*` (#106). Referencing the old names creates dangling links (the exact red-main bug #117/#116 fixed). Current replacement: the `demand_durability_indicator_*` names.
- **Pilot's "pins in `capture_context`"** — superseded by the hardened first-class schema fields (#113). Don't copy the stopgap.
- **"Scopes, does not authorize" (default handoff posture)** — superseded for steps 2+3 by the owner's bounded Build Authorization (in both build handoffs).
- **Older precompact/handoff packets from this arc** — superseded by this coordination handoff as the latest continuation anchor for the rollout.

## Commands And Verification Evidence

- Confirm rollout merged + main green:
  ```bash
  git fetch origin main && git log origin/main --oneline -8
  cd orca-harness && ../.agents/hooks/check_map_links.py --strict   # via the venv python
  ```
  Result at handoff: all rollout PRs MERGED; `check_map_links --strict: OK (0 findings)`; `origin/main 10f370ed`. Re-run target: the receiver confirms before dispatching.
- Offline suite (the green gate for any build):
  ```bash
  cd orca-harness && .venv/Scripts/python.exe -m pytest -q
  ```
  Baseline at the hardening merge: 861 passed, 2 skipped.

## Blockers And Risks

- Blocker: none on `main`. The builds need their (granted) bounded authorization + the owner's per-lane merges.
- Risk: cross-lane drift (owner merges/renames fast) — re-verify PR states + filenames before acting (the #89/#93 and #106/#116 lessons).
- Risk: a step-3 scheduler drifting toward standing capture — keep it bounded to the commissioned series' `slot_count`.

## Confirm-Don't-Trust Load Checklist

- Re-verify before acting: (1) rollout PRs #107/#108/#113/#114/#115/#117 MERGED; (2) `main` green (`check_map_links --strict` OK); (3) `origin/main` HEAD (≥ `10f370ed`); (4) the two build handoffs present + their bounded Build Authorization intact; (5) the `demand_durability_indicator_*` filenames current.
- Load outcomes: `REUSE` after all re-verify; `STALE_REREAD_REQUIRED` if `main` moved (expected — refresh); `BLOCKED_DRIFT` if a claimed-merged PR isn't merged or `main` is red.
- Reread on drift: the two build handoffs, the pilot spec §3, `models.py`, obligation contract Ob.1/Ob.17.

## Do Not Forget

- The rollout is **fully merged + main green** through hardening + both build handoffs; the remaining work is the **authorized builds (steps 2→3)** then a **real series**, then series-diff Element 3.
- **Owner merges/renames aggressively** — re-verify PR states + current filenames before every actionable claim (the #89/#93 + #106/#116 lessons).
- Build authorization is **bounded to steps 2+3**; landing to `main` stays owner-gated; **INV-1** and **commissioned-only** are non-negotiable.
