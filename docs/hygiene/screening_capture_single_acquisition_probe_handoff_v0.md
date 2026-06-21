---
retrieval_header_version: 1
artifact_role: Cold cross-lane handoff packet (durable continuation artifact; NOT validation/readiness/governance)
scope: >
  Transfer the single-acquisition screened capture probe spec lane to a fresh
  agent or thread after the spec is written, so the receiver can re-verify the
  scanning/capture boundary and continue only the next authorized docs or build
  step.
use_when:
  - Continuing the screening/capture hybrid posture work cold after context clearing.
  - Reconstructing why single-acquisition delayed commit became the target default over pure screening, direct capture, or screen-gated separate capture.
authority_boundary: retrieval_only
open_next:
  - docs/workflows/single_acquisition_screened_capture_probe_spec_v0.md
  - docs/workflows/screening_read_service_build_receipt_v0.md
  - docs/decisions/screening_reddit_read_route_decision_v0.md
  - docs/decisions/data_capture_spine_source_access_tooling_build_authorization_v0.md
stale_if:
  - The spec lands in a later commit or is superseded.
  - The screening-read service API, packet commit lifecycle, or source-access boundary changes.
---

# Handoff Packet - Screening/Capture Single-Acquisition Probe

## Load Contract

- packet_version: v0
- mode: max
- created_at: 2026-06-21
- created_by_lane: Codex capture-spine CA in `codex/screening-read-service-build` (provenance only; not authority)
- workspace: `C:\Users\vmon7\Desktop\projects\orca\worktrees\screening-read-service-build`
- handoff_path: `docs/hygiene/screening_capture_single_acquisition_probe_handoff_v0.md`
- expected_branch: `codex/screening-read-service-build`
- expected_head: `96cfb3b8687e1ed2aaec8d881031d1c549eff097` at packet drafting; reread current HEAD before acting because this packet is written in the same docs patch.
- expected_dirty_state_including_handoff_file: this packet and `docs/workflows/single_acquisition_screened_capture_probe_spec_v0.md` are newly created in the same work unit; map/index files are modified to route to the spec; the historical ChatGPT strategy prompt is modified with a supersession note. Re-verify with `git status --short --branch`.
- load_rule: confirm-don't-trust; re-verify every load-bearing fact against its compare target before acting; sender claims are hypotheses, not authority.

## Goal Handoff

- long_term_goal: Give Orca a source-access posture that finds high-value public venues while minimizing repeated visits to the same site and preserving packet-grade evidence only when useful.
- anchor_goal: Stabilize and, if later authorized, build the single-acquisition screened capture probe: one bounded public acquisition per URL, in-memory screening, explicit commit-or-discard, no hidden packet/ECR side effects.
- success_signal: A clean agent can explain and continue from the written spec without confusing pure screening, direct capture, screen-gated fallback, or delayed-commit target posture.

## Open Decision / Fork

- decision: Whether to move from spec to implementation, and if so which version to build first.
  - options:
    - implement the target `screened_capture_probe(...)` delayed-commit path;
    - keep using pure screening plus screen-gated separate capture as fallback;
    - write an owner decision first if the default posture needs ratification beyond this workflow spec.
  - already constrained / off the table:
    - do not add packet side effects to `screening_read(...)`;
    - do not let walkers invoke capture/read entries directly;
    - do not build a standing crawler, scheduler, monitor, dashboard, or production runtime;
    - do not weaken public-only, entitlement-first, no-auth-bypass boundaries.
  - trade-offs:
    - delayed commit best minimizes site visits and page-state drift, but needs new commit/discard/idempotency tests;
    - screen-gated separate capture is simpler but double-visits the same URL;
    - direct capture is correct only for admitted/high-confidence durable evidence needs.
  - owner of the call: owner/CA for build authorization; implementation requires a later bounded build commission.
  - recommendation and why: adopt the spec as the target default for uncertain public source/venue probes; build delayed commit only when commissioned, with screen-gated separate capture as the interim fallback.

## Drift Guard

- Do not treat `screening_read(...)` as packet-writing. It remains pure screening by current build receipt.
  - why it matters: hidden capture side effects would erase the boundary the tests just proved.
  - what violating it would break: no-packet/no-ECR screening contract and auditability of the posture transition.
- Do not re-litigate "capture if it feels okay" as an acceptable gate. The spec replaces it with explicit criteria.
  - why it matters: vague promotion produces untestable over-collection.
  - what violating it would break: no-durable-before-gate and source-access accounting.
- Site-count minimization is load-bearing. The target default is single acquisition per URL for the same probe decision.
  - why it matters: repeat visits increase block/rate/interstitial risk and can change page state.
  - what violating it would break: the reason this spec supersedes the earlier "Tier 2 later" recommendation.
- A bounded venue probe may include a small listing plus detail set, but it is not broad crawling.
  - why it matters: one-page capture often under-samples a venue; site-wide walking over-corrects.
  - what violating it would break: human-rate, bounded-question, no-standing-runtime constraints.

## Inherited Context (does NOT flow to a new lane)

### Source-loading state to re-establish (follows overlay doctrine)

- overlay source-loading policy: `.agents/workflow-overlay/source-loading.md`; start with `AGENTS.md` and `.agents/workflow-overlay/README.md`.
- targets to enter the ladder:
  - `docs/workflows/single_acquisition_screened_capture_probe_spec_v0.md`;
  - `docs/workflows/screening_read_service_build_receipt_v0.md`;
  - `docs/workflows/screening_read_reusable_findings_v0.md`;
  - `docs/decisions/screening_reddit_read_route_decision_v0.md`;
  - `docs/decisions/data_capture_spine_source_access_tooling_build_authorization_v0.md`;
  - `orca/product/spines/capture/core/source_capture_toolbox/source_capture_playbook_v0.md`;
  - `orca/product/spines/foundation/vertical_exploration/orca_vertical_exploration_guide_v0.md`.
- already loaded (weak orientation, freshness-marked 2026-06-21; not authority): the sender read the sources above plus the ChatGPT strategy output bundle at `C:\Users\vmon7\.codex\attachments\22434f2a-c73a-4aa0-abcd-a45d1ea40171\pasted-text.txt`.
- must load first before strict or actionable steps: the new spec and the current implementation receipt.
- load rule: receiver re-runs progressive source loading per overlay; this packet only seeds the ladder.

### Earlier-decided concepts and behaviors (inline gist plus verify pointer)

- Pure screening-read entries are implemented and no-packet/no-ECR. Verify in `docs/workflows/screening_read_service_build_receipt_v0.md` before claiming current behavior.
- Browser/interstitial screening classifies `block_shell` on visible text, not full DOM. Verify in `docs/workflows/screening_read_reusable_findings_v0.md` before reusing the Cloudflare finding.
- The external ChatGPT strategy initially recommended Tier 1 screen-gated capture now and Tier 2 delayed commit later. The owner then made site-count minimization a core goal, which upgrades delayed commit from later optimization to target default. Verify against the new spec before repeating the older recommendation.
- Mini God Tier requires accepted residuals and is not validation/readiness. Verify in `docs/decisions/orca_mini_god_tier_doctrine_v0.md` if using the MGT label.

## Active Objective

Continue the screening/capture hybrid architecture from the written spec: make the single-acquisition delayed-commit posture clear, keep pure screening and capture boundaries intact, and only move to implementation after a fresh owner/build authorization.

## Exact Next Authorized Action

1. Re-verify the spec and current branch state.
2. If the next task is docs-only, update only routing or follow-on prompt material needed to make the spec discoverable.
3. If the next task is implementation, stop unless the current turn or an accepted handoff explicitly grants bounded implementation authority for a separate orchestrator entry such as `screened_capture_probe(...)`.
4. If implementation is authorized, start from the spec's test requirements: no durable source writes before gate, one acquisition per URL, commit same artifact, discard leaves no source artifact, and fallback separate capture records the double-visit residual.

## Authority And Source Ledger

- `AGENTS.md`
  - Role: root Orca project instructions and MGT trigger binding.
  - Load-bearing: yes.
  - Compare target: reread-required.
  - Last checked: 2026-06-21.
  - Reuse rule: reread before strict or source-changing claims.
- `.agents/workflow-overlay/README.md`
  - Role: overlay entrypoint.
  - Load-bearing: yes.
  - Compare target: reread-required.
  - Last checked: 2026-06-21.
  - Reuse rule: reread before strict or source-changing claims.
- `.agents/workflow-overlay/source-loading.md`
  - Role: source-loading, capture-spine read-pack pointer, and start preflight.
  - Load-bearing: yes.
  - Compare target: reread-required.
  - Last checked: 2026-06-21.
  - Reuse rule: reread before a prompt, handoff, docs-write, or build prompt.
- `docs/workflows/single_acquisition_screened_capture_probe_spec_v0.md`
  - Role: target spec being handed off.
  - Load-bearing: yes.
  - Compare target: reread-required until committed; after commit, use the commit blob.
  - Last checked: 2026-06-21.
  - Reuse rule: authoritative only as retrieval/workflow spec, not implementation or validation.
- `docs/workflows/screening_read_service_build_receipt_v0.md`
  - Role: current implementation receipt for pure screening-read entries.
  - Load-bearing: yes.
  - Compare target: HEAD `96cfb3b8687e1ed2aaec8d881031d1c549eff097` at packet drafting; reread-required after this patch.
  - Last checked: 2026-06-21.
  - Reuse rule: use for current behavior, not future delayed-commit behavior.
- `docs/decisions/data_capture_spine_source_access_tooling_build_authorization_v0.md`
  - Role: build authorization and source-access boundaries.
  - Load-bearing: yes.
  - Compare target: reread-required.
  - Last checked: 2026-06-21.
  - Reuse rule: reread before any implementation or live-source claim.
- `C:\Users\vmon7\.codex\attachments\22434f2a-c73a-4aa0-abcd-a45d1ea40171\pasted-text.txt`
  - Role: external strategy output orientation.
  - Load-bearing: no.
  - Compare target: local attachment path, bundle-only.
  - Last checked: 2026-06-21.
  - Reuse rule: orientation only; superseded by owner correction and the new spec for target default.
- Source gaps: exact implementation interface and packet commit API are not scoped yet.
- Strict-only blockers: implementation authority is absent for a build turn; this handoff is docs/continuation only.
- Not-proven boundaries: no delayed-commit code, runtime validation, live probe, packet output, or source-quality result exists.

## Current Task State

- Completed: pure screening-read service and browser wrapper were already built on this PR branch; reusable extraction findings were propagated; the hybrid strategy was externally adjudicated; this work writes the single-acquisition target spec, routes it through maps, and marks the older strategy prompt superseded.
- Partially completed: implementation is not started; exact orchestrator API and packet commit interface remain to be scoped.
- Broken or uncertain: no known broken source; the exact build cost of preserving route-native ephemeral artifacts is unknown.

## Workspace State

- Branch: `codex/screening-read-service-build`.
- Head at packet drafting: `96cfb3b8687e1ed2aaec8d881031d1c549eff097`.
- Dirty or untracked state before handoff work: clean.
- Dirty or untracked state after writing the handoff file: this handoff and the new spec are new files; map/index files plus the historical strategy prompt are modified. Re-verify with `git status --short --branch`.
- Target files or artifacts:
  - `docs/workflows/single_acquisition_screened_capture_probe_spec_v0.md`;
  - `docs/hygiene/screening_capture_single_acquisition_probe_handoff_v0.md`;
  - `docs/workflows/data_capture_spine_consolidation_map_v0.md`;
  - `docs/workflows/orca_repo_map_v0.md`;
  - `orca/product/spines/capture/core/source_capture_toolbox/README.md`;
  - `docs/prompts/deep-thinking/screening_capture_hybrid_mgt_strategy_prompt_v0.md`.
- Related branches or PRs: PR #324, branch `codex/screening-read-service-build`.

## Changed / Inspected / Tested Files

- `docs/workflows/single_acquisition_screened_capture_probe_spec_v0.md`
  - Status: new.
  - Role: workflow spec for single-acquisition screened capture.
  - Important observations: target default is delayed commit; screen-gated separate capture is fallback.
- `docs/hygiene/screening_capture_single_acquisition_probe_handoff_v0.md`
  - Status: new.
  - Role: cold handoff packet.
  - Important observations: single-consumption continuation artifact, not authority.
- `docs/workflows/data_capture_spine_consolidation_map_v0.md`
  - Status: modified for routing.
  - Role: Data Capture submap.
- `docs/workflows/orca_repo_map_v0.md`
  - Status: modified for routing.
  - Role: repo map/discoverability.
- `orca/product/spines/capture/core/source_capture_toolbox/README.md`
  - Status: modified for routing.
  - Role: Armory entrypoint.
- `docs/prompts/deep-thinking/screening_capture_hybrid_mgt_strategy_prompt_v0.md`
  - Status: modified with supersession note and `superseded_by` pointer.
  - Role: historical external-strategy prompt; no longer current target guidance.

## Frozen Decisions

- Decision: The target default for uncertain public page/venue probes is single-acquisition screened capture, not boundary-collapse capture and not pure screening as the ideal.
  - Evidence: owner stated minimizing site counts is a core goal; the spec records accepted residuals.
  - Consequence: a future build must preserve one acquisition per URL when possible and make commit explicit.
- Decision: `screening_read(...)` stays pure.
  - Evidence: current build receipt and route decision.
  - Consequence: future build should add a separate orchestrator entry or equivalent, not hide packet writes in screening.

## Mutable Questions

- Question: What exact API should carry an ephemeral acquisition into packet commit?
  - Why still mutable: no implementation scoped yet.
  - What would resolve it: bounded build scoping over current adapters and packet writer.
- Question: Which route families can support same-artifact delayed commit first?
  - Why still mutable: direct HTTP and browser routes differ in bytes/DOM/screenshot behavior.
  - What would resolve it: implementation scoping and route-specific tests.

## Superseded / Dangerous-To-Reuse Context

- Stale instruction, idea, artifact, or finding: "Tier 1 screen-gated capture now; Tier 2 delayed commit later" as the target default.
  - Why stale or dangerous: it underweights the later owner clarification that repeat site visits are a core risk.
  - Current replacement: single-acquisition delayed commit is the target default; screen-gated separate capture is fallback.
- Stale instruction, idea, artifact, or finding: "capture if it feels okay" or "ignore the boundary."
  - Why stale or dangerous: untestable gate and hidden durable side effects.
  - Current replacement: explicit gate with commit-or-discard state transition.

## Commands And Verification Evidence

- Command:
  ```powershell
  git status --short --branch
  ```
  Result:
  - Passed/failed/not run: run before edits.
  - Important output: branch `codex/screening-read-service-build...origin/codex/screening-read-service-build`, clean.
  - Re-run target so the receiver can confirm rather than trust: run again after loading this packet.
- Command:
  ```powershell
  git rev-parse HEAD
  ```
  Result:
  - Passed/failed/not run: run before edits.
  - Important output: `96cfb3b8687e1ed2aaec8d881031d1c549eff097`.
  - Re-run target so the receiver can confirm rather than trust: run again after loading this packet.

## Blockers And Risks

- Blocker or risk: implementation authority is not present in this handoff.
  - Evidence: current request was to write a spec and clear context.
  - Likely next action: get a bounded build commission before code changes.
- Blocker or risk: committing this packet can make its expected dirty-state text stale.
  - Evidence: the packet is authored during the same docs patch it describes.
  - Likely next action: receiver re-runs the confirm-don't-trust load protocol and treats dirty/head claims as hypotheses.

## Confirm-Don't-Trust Load Checklist

- Load-bearing facts the receiver must re-verify before acting:
  - current branch, HEAD, and dirty state;
  - existence and content of the new spec;
  - current screening-read implementation boundary;
  - source-access build authorization and hard stops;
  - whether any later commit superseded this packet.
- Compare target for each:
  - branch/head/status: `git status --short --branch` and `git rev-parse HEAD`;
  - spec and docs: reread named files;
  - implementation behavior: reread build receipt and, if building, current code/tests;
  - supersession: `rg -n "single-acquisition screened capture|screened_capture_probe|delayed commit" docs orca`.
- Load outcomes:
  - `REUSE`: all load-bearing facts re-verified; continue from Exact Next Authorized Action.
  - `PARTIAL_REUSE`: non-load-bearing orientation drifted; re-derive and continue.
  - `STALE_REREAD_REQUIRED`: head, spec, or implementation boundary drifted; reread before action.
  - `BLOCKED_DRIFT`: current user instruction or source boundary conflicts with this packet.
  - `BLOCKED_MISSING_PACKET`: this path is missing or unreadable.
  - `BLOCKED_UNVERIFIABLE`: a load-bearing claim cannot be re-derived.

## Do Not Forget

- The spec's point is minimizing repeat site visits without collapsing the audit boundary. If a future plan either double-fetches by default or hides packet writes in screening, it missed the core.
