# Adversarial Review Prompt: Orca Chat-Output Contract Phase Plan

```yaml
retrieval_header_version: 1
artifact_role: Review prompt
scope: Read-only adversarial review prompt for the Orca chat-output contract phase plan before Phase 0 edits.
use_when:
  - Reviewing the proposed phase plan for Orca human-summary / agent-detail / courier-YAML output topology patches.
  - Checking whether the planned patches preserve the review-report saved-artifact exception.
authority_boundary: retrieval_only
open_next:
  - .agents/workflow-overlay/prompt-orchestration.md
  - .agents/workflow-overlay/communication-style.md
  - .agents/workflow-overlay/validation-gates.md
  - docs/prompts/templates/shared/orca_prompt_behavior_contract_v0.md
  - docs/prompts/templates/review/adversarial_artifact_review_v0.md
branch_or_commit: main @ fedafb7d60713020e1e628dbf0f484d79501c8d7
downstream_consumers:
  - docs/review-outputs/adversarial-artifact-reviews/orca_chat_output_contract_phase_plan_adversarial_review_v0.md
stale_if: The accepted route or phase plan changes, chat-output contract ownership changes, or review-report output-mode contract changes before review is run.
```

- Prompt type: Review prompt
- Requested reviewer model: model-neutral; use a capable reasoning model
- Output mode: review-report
- Edit permission: read-only
- Workspace: `C:\Users\vmon7\Desktop\projects\orca`
- Expected branch: `main`
- Expected HEAD at prompt preparation: `fedafb7d60713020e1e628dbf0f484d79501c8d7`
- Dirty-state allowance: dirty state allowed; modified and untracked Orca docs,
  prompts, overlay files, product artifacts, and review-output folders may be
  present. Do not clean, revert, stage, commit, push, or treat unrelated dirty
  files as review failure.
- Report destination:
  - `docs/review-outputs/adversarial-artifact-reviews/orca_chat_output_contract_phase_plan_adversarial_review_v0.md`

## Objective

Run one read-only adversarial artifact review of the proposed Orca
chat-output contract implementation route and phase plan before Phase 0 edits
begin.

The review should answer whether the plan is narrow, correctly phased, and
safe to use as the next docs-only patch route for Orca's chat-output topology:

- decision-bearing chat starts with human-readable prose;
- agent-detail sections carry machine-routable specifics without replacing the
  human decision narrative;
- courier YAML is compact and last;
- `review-report` remains the explicit saved-artifact exception where YAML-only
  chat is valid only after a successful durable report write;
- file-write artifact receipts remain distinct from decision-bearing chat and
  are not over-patched into verbose closeouts;
- prompt policy does not add ritual YAML keys or explicit `non_claims` blocks
  merely to satisfy process shape;
- stale one-off prompts and checkpoint records are deferred rather than
  broad-synced into fake authority.

Do not patch files, prepare a patch queue, run validation gates, stage, commit,
push, or claim readiness.

## Required Skill Invocation

Use `workflow-deep-thinking` first.

Then use `workflow-adversarial-artifact-review`.

The deep-thinking step should frame the boundary problem: Orca needs readable
decision chat for Chief Architect, planning, scoping, and phase-gate work while
preserving compact machine-routable state and the existing `review-report`
saved-report exception.

## Required Reads

Read first:

- `AGENTS.md`
- `.agents/workflow-overlay/README.md`
- `.agents/workflow-overlay/source-of-truth.md`
- `.agents/workflow-overlay/artifact-roles.md`
- `.agents/workflow-overlay/prompt-orchestration.md`
- `.agents/workflow-overlay/communication-style.md`
- `.agents/workflow-overlay/review-lanes.md`
- `.agents/workflow-overlay/validation-gates.md`
- `.agents/workflow-overlay/template-registry.md`
- `.agents/workflow-overlay/retrieval-metadata.md`
- `.agents/workflow-overlay/safety-rules.md`
- `docs/prompts/templates/shared/orca_prompt_behavior_contract_v0.md`
- `docs/prompts/templates/review/adversarial_artifact_review_v0.md`

Then inspect active reusable templates and active prompt families enough to
test the phase plan's target surface:

- `docs/prompts/templates/_generic/gpt_5_5_general_prompt_v0.md`
- `docs/prompts/templates/research/o3_evidence_only_research_lane_v0.md`
- `docs/prompts/templates/research/gpt_5_5_evidence_synthesis_v0.md`
- `docs/prompts/templates/wrappers/thin_wrapper_v0.md`
- `docs/prompts/templates/review/adversarial_artifact_review_v0.md`
- active prompts under `docs/prompts/product-planning/`
- active prompts under `docs/prompts/deep-thinking/`
- active prompts under `docs/prompts/wrappers/`
- active prompts under `docs/prompts/reruns/`
- active review prompts under `docs/prompts/reviews/`

Also check:

- `git status --short --branch`
- `rg -n "human summary|human-readable|agent detail|courier YAML|review-report|review_summary|report_path|review_location|Return only|Final Response|Output Contract|paste-ready-chat|file-write|chat-only|patch-queue" .agents/workflow-overlay docs/prompts`

If the workspace is not `C:\Users\vmon7\Desktop\projects\orca`, the target
sources are inaccessible, or the prompt cannot distinguish the embedded phase
plan from implementation authorization, return a blocked result instead of
reviewing a substitute checkout or reconstructed route.

## Review Target

Review this accepted non-executing route and phase-gate plan:

```text
Accepted problem:
Orca needs a chat-output topology rule for human-facing workflow outputs:
human summary first, agent detail second, compact courier YAML last. The rule
must preserve the review-report saved-artifact exception and avoid adding
process-only YAML keys or required non-claim blocks.

Accepted owner split:
- communication-style.md owns the general chat rendering rule.
- prompt-orchestration.md owns output-mode exceptions and write-failure behavior.
- validation-gates.md owns the collision checklist before closure.
- review-lanes.md owns review routing and report destinations.
- the shared prompt behavior contract should point to the overlay rule, not
  duplicate all policy.

Frozen decisions:
- Decision-bearing chat starts with human-readable prose.
- Agent detail follows only when useful.
- Courier YAML is compact and last.
- review-report YAML-only chat remains valid only after successful durable
  report write.
- Do not broad-patch stale one-offs or file-write receipt prompts merely
  because they are compact.
- Do not include an explicit non_claims YAML block such as files_edited,
  validation_run, or readiness_claimed unless a specific prompt contract
  requires it.

Implementation route:
STEP-01: Patch communication-style.md.
Intent: add the general chat-output topology: human summary first, agent
detail second, courier YAML last. Include the decision-bearing versus
artifact-receipt distinction.

STEP-02: Patch prompt-orchestration.md.
Intent: bind output-mode exceptions: review-report, file-write receipts,
paste-ready-chat, chat-only, and patch-queue. Keep write-failure behavior
owned here.

STEP-03: Patch validation-gates.md.
Intent: add a chat-output topology gate for prompt-policy and workflow patches
before closure.

STEP-04: Patch shared prompt behavior contract.
Intent: point prompt templates to the overlay-owned topology rule without
duplicating all policy text.

STEP-05: Patch active reusable templates only.
Intent: align generic, research, wrapper, and review templates where output
shape is open-ended or likely to spread the problem. Avoid stale one-offs and
already-valid post-artifact receipts.

Phase gate:
execution_shape: PHASED_REQUIRED

PHASE-0:
Dirty-state and ownership preflight.
Allowed changes: none.
Gate: read-only branch/status/target-file classification.
Stop on dirty target collision, unexpected owner conflict, or inability to
isolate intended Phase 1/2 files from unrelated dirty work.

PHASE-1:
Overlay contract owners.
Linked route steps: STEP-01 through STEP-03.
Allowed changes:
- .agents/workflow-overlay/communication-style.md
- .agents/workflow-overlay/prompt-orchestration.md
- .agents/workflow-overlay/validation-gates.md
Gate: targeted readback confirms the topology rule, output-mode exceptions,
and closure/collision gate are adjacent to their owning rules.
Stop if the saved-report exception becomes weaker or moves away from
review-report output-mode ownership.

PHASE-2:
Shared and reusable templates.
Linked route steps: STEP-04 and STEP-05.
Allowed changes:
- docs/prompts/templates/shared/orca_prompt_behavior_contract_v0.md
- active reusable templates under docs/prompts/templates/
Gate: targeted rg/readback confirms no weakened review-report exception, no
broad stale sync, and no required ritual non_claims YAML block.
Stop if template edits become a broad prompt rewrite or stale prompt sync.

Review timing:
Adversarial review before Phase 0 is recommended because the route changes
contract-bearing prompt/output policy and reusable templates. The review should
stress overcorrection, saved-report exception drift, and template propagation
risk.
```

## Review Scope

Review only these risks:

- Owner topology: the proposed owner map puts the general chat shape,
  output-mode exceptions, review routing, and closure gate in the right files.
- Phase boundaries: Phase 1 and Phase 2 are the smallest safe split and do not
  hide dependency, rollback, stale-source, or authority risk.
- Exception boundaries: `review-report` saved-report behavior remains explicit
  beside the output-mode rule and is not weakened by the general chat-output
  rule.
- Artifact-receipt distinction: compact file-write receipts and source-heavy
  checkpoints are not over-patched into verbose CA-style closeouts when a
  durable artifact carries the human value.
- Human-readable phase plans: future phase-gate or CA planning outputs should
  render the plan in prose, bullets, or tables instead of YAML-only structures.
- Process-key restraint: the route should not add explicit non-claim YAML keys
  or extra courier keys merely to satisfy process metrics.
- Active surface coverage: the chosen active template/prompt surfaces are
  sufficient for the first patch without broad-syncing stale one-offs.
- Retrieval metadata boundary: retrieval headers remain retrieval-only and do
  not imply authority, validation proof, approval, readiness, lifecycle
  completion, deployment/install/resolver status, edit permission, or
  source-of-truth promotion.
- Leakage: no `jb` project policy, GAP/CV Engine paths, lifecycle mechanics,
  validation habits, or handoff rules are imported into Orca authority.

After correctness findings, note friction only if it could cause a future
Chief Architect, implementer, prompt author, or reviewer to misroute the
contract.

## Excluded Scope

Do not review Orca product strategy, product proof, buyer proof, customer
discovery, Core Spine validation, method-validation case quality, or external
evidence.

Do not review implementation code, tests, runtime architecture, tooling,
automation, packages, install/deploy behavior, resolver behavior, or
workflow-kernel source.

Do not prepare a patch queue. Suggested remediation may be advisory prose only.

## Prompt Validation Gates

Before reviewing, check and record:

- Overlay authority loaded: `AGENTS.md` and `.agents/workflow-overlay/README.md`
  were read.
- Artifact roles bound: review prompt and review report roles map to
  `.agents/workflow-overlay/artifact-roles.md`.
- Source resolution clean: installed skills are runtime copies; `jb` project
  policy is not Orca authority.
- Worktree preflight present: workspace, branch, HEAD, dirty-state allowance,
  target files, edit permission, and report destination are explicit.
- Output mode explicit: exactly one output mode is named, `review-report`.
- Review-report topology gate checked from
  `.agents/workflow-overlay/validation-gates.md`.
- Retrieval metadata bounded: headers are retrieval-only and do not create
  authority, validation proof, approval, readiness, lifecycle completion,
  deployment/install/resolver status, edit permission, or source-of-truth
  promotion.
- Leakage gate: prompt artifacts do not copy `jb` templates, GAP/CV Engine
  paths, compiler paths, handoff rules, product-lead rules, or repo-local
  lifecycle mechanics.

## Output Contract

Write the durable review report to:

`docs/review-outputs/adversarial-artifact-reviews/orca_chat_output_contract_phase_plan_adversarial_review_v0.md`

This prompt uses `review-report` output mode. The human-readable review value
belongs in the durable report above. Chat YAML is courier output only and is
valid only after that report has been successfully written.

The report must contain:

1. Review target and source-read ledger.
2. Git status and dirty sources relied on.
3. Scope and excluded scope.
4. Phase-plan decision assessment.
5. Correctness findings first.
6. Friction findings only if material.
7. Not-proven boundaries.
8. Blockers or no-blocking-finding statement.
9. Next authorized step.
10. Review-use boundary.

Finding format:

- `AR-01`: one-sentence finding title.
- Location: file and stable section heading or search key.
- Evidence: quote or short paraphrase from the artifact.
- Why it matters: concrete effect on chat-output topology, phase safety, review
  routing, or future prompt safety.
- Next action: advisory only; no patch execution.

If there are no blocking findings, say so directly. Do not claim the phase
plan is approved, accepted, validated, workflow-ready, merge-safe,
product-ready, resolver-ready, implementation-ready, installed, deployed, or
committed.

Findings are decision input for the Chief Architect. They are not mandatory
remediation unless separately accepted and authorized.

After successfully writing the report, return only this compact YAML summary in
chat:

```yaml
review_summary:
  status: completed
  report_path: docs/review-outputs/adversarial-artifact-reviews/orca_chat_output_contract_phase_plan_adversarial_review_v0.md
  recommendation: accept | accept_with_friction | patch_before_acceptance | reject | blocked
  summary: "One sentence describing the review result."
  findings_count: 0
  blocking_findings: []
  advisory_findings: []
  prior_findings_remediated: []
  next_action: "One concrete next step"
```

If the required report cannot be written after review work starts, do not use
`report_path` and do not treat chat YAML as a substitute report. Return a
failed blocked summary in chat:

```yaml
review_summary:
  status: failed
  review_location: chat_only_current_thread
  recommendation: blocked
  summary: "Failed to write required report to docs/review-outputs/adversarial-artifact-reviews/orca_chat_output_contract_phase_plan_adversarial_review_v0.md."
  findings_count: 0
  blocking_findings: []
  advisory_findings: []
  prior_findings_remediated: []
  next_action: "Resolve the report write failure, then rerun the review-report prompt."
```

Include enough brief human-readable failure detail to route the write failure.
Do not add extra YAML keys.
