# Adversarial Review Prompt: Orca Chat-Output Contract Post-Patch Diff

```yaml
retrieval_header_version: 1
artifact_role: Review prompt
scope: Read-only adversarial review prompt for the completed Orca chat-output contract Phase 1/2 patch set.
use_when:
  - Reviewing the actual post-patch diff for Orca human-summary / agent-detail / courier-YAML output topology.
  - Checking whether Phase 1 overlay and Phase 2 template edits resolved the accepted review friction without new contract drift.
authority_boundary: retrieval_only
open_next:
  - .agents/workflow-overlay/communication-style.md
  - .agents/workflow-overlay/prompt-orchestration.md
  - .agents/workflow-overlay/validation-gates.md
  - docs/prompts/templates/shared/orca_prompt_behavior_contract_v0.md
  - docs/prompts/templates/review/adversarial_artifact_review_v0.md
branch_or_commit: main @ fedafb7d60713020e1e628dbf0f484d79501c8d7
downstream_consumers:
  - docs/review-outputs/adversarial-artifact-reviews/orca_chat_output_contract_post_patch_adversarial_review_v0.md
stale_if: Any target file changes, chat-output contract ownership changes, or review-report output-mode contract changes before review is run.
```

- Prompt type: Review prompt
- Requested reviewer model: model-neutral; use a capable reasoning model
- Output mode: review-report
- Edit permission: read-only
- Workspace: `C:\Users\vmon7\Desktop\projects\orca`
- Expected branch: `main`
- Expected HEAD at prompt preparation: `fedafb7d60713020e1e628dbf0f484d79501c8d7`
- Dirty-state allowance: dirty state allowed. The workspace has broad unrelated
  dirty docs/product/research files. Review only the target files listed below
  plus the required overlay sources. Treat the untracked Phase 2 reusable
  template files as in-scope target artifacts, not as unrelated dirty state.
- Report destination:
  - `docs/review-outputs/adversarial-artifact-reviews/orca_chat_output_contract_post_patch_adversarial_review_v0.md`

## Objective

Run one read-only adversarial artifact review of the completed Orca
chat-output contract Phase 1/2 patch set.

The review should answer whether the actual patch set correctly establishes
this topology:

- decision-bearing chat starts with human-readable prose;
- agent-readable detail is separate and does not replace the human decision;
- courier YAML remains compact and last unless a stage-native exception
  applies;
- `review-report` YAML-only chat remains valid only after successful durable
  report write;
- `paste-ready-chat` is classified without becoming a loophole for machine-only
  Chief Architect, planning, scoping, phase-gate, or routing decisions;
- `file-write` post-artifact receipts remain compact when the durable artifact
  carries the human value;
- research/evidence tables remain task-native structured artifacts;
- the patch does not add ritual YAML fields or explicit `non_claims` keys
  merely for process metrics.

Do not patch files, prepare a patch queue, run validation gates, stage, commit,
push, or claim readiness.

## Required Skill Invocation

Use `workflow-deep-thinking` first.

Then use `workflow-adversarial-artifact-review`.

The deep-thinking step should frame the topology risk: a general
human-summary-first rule can improve CA/planning readability, but if it is not
bounded by output-mode exceptions it can silently contradict `review-report`,
`paste-ready-chat`, task-native research tables, and compact artifact receipts.

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

Review these Phase 1 overlay targets:

- `.agents/workflow-overlay/communication-style.md`
- `.agents/workflow-overlay/prompt-orchestration.md`
- `.agents/workflow-overlay/validation-gates.md`

Review these Phase 2 reusable template targets:

- `docs/prompts/templates/shared/orca_prompt_behavior_contract_v0.md`
- `docs/prompts/templates/_generic/gpt_5_5_general_prompt_v0.md`
- `docs/prompts/templates/research/o3_evidence_only_research_lane_v0.md`
- `docs/prompts/templates/research/gpt_5_5_evidence_synthesis_v0.md`
- `docs/prompts/templates/wrappers/thin_wrapper_v0.md`
- `docs/prompts/templates/review/adversarial_artifact_review_v0.md`

Use for review context, not as patch authority:

- `docs/prompts/reviews/orca_chat_output_contract_phase_plan_adversarial_review_prompt_v0.md`
- `docs/review-outputs/adversarial-artifact-reviews/orca_chat_output_contract_phase_plan_adversarial_review_v0.md`
- `docs/prompts/hygiene-queue/precompact_orca_chat_output_contract.md`

Also check:

- `git status --short --branch`
- `git diff -- .agents/workflow-overlay/communication-style.md .agents/workflow-overlay/prompt-orchestration.md .agents/workflow-overlay/validation-gates.md docs/prompts/templates/review/adversarial_artifact_review_v0.md`
- `git status --short -- docs/prompts/templates/shared/orca_prompt_behavior_contract_v0.md docs/prompts/templates/_generic/gpt_5_5_general_prompt_v0.md docs/prompts/templates/research/o3_evidence_only_research_lane_v0.md docs/prompts/templates/research/gpt_5_5_evidence_synthesis_v0.md docs/prompts/templates/wrappers/thin_wrapper_v0.md`
- `rg -n "Chat Output Topology|Output-mode exceptions|review-report|paste-ready-chat|file-write|human-summary|agent-detail|courier-YAML|task-native|structured table|non_claims|files_edited|validation_run|readiness_claimed" .agents/workflow-overlay docs/prompts/templates`

If the workspace is not `C:\Users\vmon7\Desktop\projects\orca`, the target
sources are inaccessible, or the reviewer cannot distinguish target files from
unrelated dirty work, return a blocked result instead of reviewing a substitute
checkout or reconstructed copy.

## Accepted Prior Review Friction To Recheck

The phase-plan adversarial review returned `accept_with_friction` with these
non-blocking findings. Check whether the patch set resolves them or leaves
residual risk:

- AR-01: STEP-01 needed an exceptions pointer in `communication-style.md`.
- AR-02: `paste-ready-chat` was used in template metadata but not listed in
  `prompt-orchestration.md` output modes.
- AR-03: Phase 2 needed to exclude already-correct active `review-report`
  prompts from broad sync.
- AF-01: Phase 1 needed to guard against implicit contradiction between the
  general rule and the exception.
- AF-02: New validation gate needed to be collision-focused, not a ritual key
  checklist.
- AF-03: Research templates have structured output shapes that could conflict
  with naive human-summary-first patching.
- AF-04: Shared behavior compactness guidance needed scoping to field presence,
  not YAML-only output.

## Review Scope

Review only these risks:

- Owner topology: `communication-style.md` owns the general chat shape and exact
  courier YAML shapes; `prompt-orchestration.md` owns output-mode exceptions;
  `validation-gates.md` owns the collision gate.
- Exception adjacency: `communication-style.md` points readers to
  `prompt-orchestration.md` for output-mode exceptions, especially
  `review-report`.
- `review-report` preservation: YAML-only chat remains tied to successful
  durable report writes; failed writes still use `review_location:
  chat_only_current_thread`, no `report_path`, and human-readable routing
  detail.
- `paste-ready-chat` classification: the mode is formalized without allowing
  CA/planning/scoping/phase-gate decisions to become machine-only prompt bodies.
- `file-write` receipts: compact path/hash/status receipts remain valid only
  when the durable artifact carries the human-readable value.
- Research templates: evidence-only tables and structured synthesis outputs
  remain task-native and are not naively forced into verbose closeouts.
- Template propagation: reusable templates inherit the owner rule narrowly and
  do not broad-sync already-correct active review-report prompts or stale
  one-offs.
- Process-key restraint: no extra courier keys, explicit `non_claims` YAML
  fields, or `files_edited` / `validation_run` / `readiness_claimed` keys are
  added merely to satisfy process metrics.
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
- Chat-output topology gate checked from
  `.agents/workflow-overlay/validation-gates.md`.
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

`docs/review-outputs/adversarial-artifact-reviews/orca_chat_output_contract_post_patch_adversarial_review_v0.md`

This prompt uses `review-report` output mode. The human-readable review value
belongs in the durable report above. Chat YAML is courier output only and is
valid only after that report has been successfully written.

The report must contain:

1. Review target and source-read ledger.
2. Git status and target dirty-state classification.
3. Scope and excluded scope.
4. Prior friction remediation assessment.
5. Contract-topology decision assessment.
6. Correctness findings first.
7. Friction findings only if material.
8. Not-proven boundaries.
9. Blockers or no-blocking-finding statement.
10. Next authorized step.
11. Review-use boundary.

Finding format:

- `AR-01`: one-sentence finding title.
- Location: file and stable section heading or search key.
- Evidence: quote or short paraphrase from the artifact.
- Why it matters: concrete effect on chat-output topology, phase safety, review
  routing, or future prompt safety.
- Next action: advisory only; no patch execution.

If there are no blocking findings, say so directly. Do not claim the patch set
is approved, accepted, validated, workflow-ready, merge-safe, product-ready,
resolver-ready, implementation-ready, installed, deployed, or committed.

Findings are decision input for the Chief Architect. They are not mandatory
remediation unless separately accepted and authorized.

After successfully writing the report, return only this compact YAML summary in
chat:

```yaml
review_summary:
  status: completed
  report_path: docs/review-outputs/adversarial-artifact-reviews/orca_chat_output_contract_post_patch_adversarial_review_v0.md
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
  summary: "Failed to write required report to docs/review-outputs/adversarial-artifact-reviews/orca_chat_output_contract_post_patch_adversarial_review_v0.md."
  findings_count: 0
  blocking_findings: []
  advisory_findings: []
  prior_findings_remediated: []
  next_action: "Resolve the report write failure, then rerun the review-report prompt."
```

Include enough brief human-readable failure detail to route the write failure.
Do not add extra YAML keys.
