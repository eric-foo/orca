# Adversarial Review Prompt: Orca Review-Report Contract Topology

```yaml
retrieval_header_version: 1
artifact_role: Review prompt
scope: Read-only adversarial review prompt for Orca review-report contract topology patches.
use_when:
  - Reviewing the saved-report exception and courier YAML contract for Orca review-report prompts.
  - Checking whether Phase 1 and Phase 2 prompt-policy patches preserve artifact-vs-courier boundaries.
authority_boundary: retrieval_only
open_next:
  - .agents/workflow-overlay/prompt-orchestration.md
  - .agents/workflow-overlay/communication-style.md
  - .agents/workflow-overlay/validation-gates.md
branch_or_commit: main @ 3bf5c45cfa6879ae65c8f822eff9c185dcba8b3c
input_hashes:
  .agents/workflow-overlay/prompt-orchestration.md: 9A5846F379C6FD635DAFF96544C2D15CB31ABE5FC425DD9D7BA0F3DD84B2CFA8
  .agents/workflow-overlay/communication-style.md: D429215695118D49D9B2551731B3A7DEB3E054B2D11C58CCABAE19D37503A5F8
  .agents/workflow-overlay/validation-gates.md: 5906ACFAB33F93C951E550A643D8345E8FD4295F4957CF6C33C64C41A95DF956
  docs/prompts/templates/review/adversarial_artifact_review_v0.md: 3476A7D0F1E2FDCE2EE76594615111FEE822BCDFC3B9E8B9E1884D1C16CE6E9C
  docs/prompts/reviews/core_spine_v0_proof_packet_preparation_adversarial_review_gpt55_prompt_v0.md: AFB4CEE573ADCB2F244C9733D8F0CF107DD0304CCF1B5529D30F9F4FB002C4A9
  docs/prompts/reviews/core_spine_v0_method_validation_case_frame_locks_adversarial_review_gpt54_prompt_v0.md: 316B96BC95DA06CE598E354A8456F78DDD5571900C4270B7F5C715AD27820F42
downstream_consumers:
  - docs/review-outputs/adversarial-artifact-reviews/orca_review_report_contract_topology_adversarial_review_v0.md
stale_if: Any input hash changes, review-report output-mode contract changes, or active review prompt surface changes before review is run.
```

- Prompt type: Review prompt
- Requested reviewer model: model-neutral; use a capable reasoning model
- Output mode: review-report
- Edit permission: read-only
- Workspace: `C:\Users\vmon7\Desktop\projects\orca`
- Expected branch: `main`
- Expected HEAD at prompt preparation: `3bf5c45cfa6879ae65c8f822eff9c185dcba8b3c`
- Dirty-state allowance: dirty state allowed; modified and untracked Orca docs,
  prompts, overlay files, and review-output folders may be present
- Report destination:
  - `docs/review-outputs/adversarial-artifact-reviews/orca_review_report_contract_topology_adversarial_review_v0.md`

## Objective

Run one read-only adversarial artifact review of the Orca review-report
contract-topology patches.

The review should answer whether the Phase 1 overlay patches and Phase 2
active prompt/template patches correctly preserve this contract:

- the durable human-readable report is the review artifact;
- chat YAML is courier output only;
- YAML-only chat is valid for `review-report` only after a successful durable
  report write;
- failed durable report writes fail loud with `status: failed`,
  `recommendation: blocked`, no `report_path`, the failed path named, and enough
  human-readable routing detail;
- exact YAML schema stays owned by `communication-style.md`;
- validity and write-failure behavior stay owned by `prompt-orchestration.md`;
- stale one-off prompts are queued for hygiene rather than broad-synced.

Do not patch files, prepare a patch queue, run validation gates, stage, commit,
push, or claim readiness.

## Required Skill Invocation

Use `workflow-deep-thinking` first.

Then use `workflow-adversarial-artifact-review`.

The deep-thinking step should frame the topology risk: locally correct durable
reports and locally correct courier YAML can still contradict each other if the
saved-report exception and failed-write behavior are not adjacent to the owning
output-mode rule.

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

Then read the patch targets:

- `.agents/workflow-overlay/prompt-orchestration.md`
- `.agents/workflow-overlay/communication-style.md`
- `.agents/workflow-overlay/validation-gates.md`
- `docs/prompts/templates/review/adversarial_artifact_review_v0.md`
- `docs/prompts/reviews/core_spine_v0_proof_packet_preparation_adversarial_review_gpt55_prompt_v0.md`
- `docs/prompts/reviews/core_spine_v0_method_validation_case_frame_locks_adversarial_review_gpt54_prompt_v0.md`

Read for continuity only, not authority:

- `docs/prompts/hygiene-queue/precompact_orca_review_report_contract_topology.md`

Also check:

- `git status --short --branch`
- `git diff -- .agents/workflow-overlay/prompt-orchestration.md .agents/workflow-overlay/communication-style.md .agents/workflow-overlay/validation-gates.md docs/prompts/templates/review/adversarial_artifact_review_v0.md docs/prompts/reviews/core_spine_v0_proof_packet_preparation_adversarial_review_gpt55_prompt_v0.md docs/prompts/reviews/core_spine_v0_method_validation_case_frame_locks_adversarial_review_gpt54_prompt_v0.md`
- `rg -n "review-report|review_summary|report_path|review_location|chat_only_current_thread|status: failed|recommendation: blocked|substitute report|substitute artifact|extra YAML keys" .agents/workflow-overlay docs/prompts/templates/review docs/prompts/reviews`

If the workspace is not `C:\Users\vmon7\Desktop\projects\orca`, the target
files are inaccessible, or any pinned input hash differs, return a blocked
result instead of reviewing a substitute checkout or reconstructed copy.

## Review Scope

Review only these risks:

- Contract ownership: `prompt-orchestration.md` owns `review-report` validity,
  saved-report prerequisite, and write-failure behavior.
- Schema ownership: `communication-style.md` owns the exact `review_summary`
  YAML shape and forbidden extra keys.
- Artifact-vs-courier boundary: human-readable review detail belongs in the
  durable report, not chat YAML.
- YAML-only validity: `review-report` YAML-only chat is allowed only after
  successful durable report write.
- Failed-write behavior: failed durable writes use `status: failed`,
  `recommendation: blocked`, `review_location: chat_only_current_thread`, no
  `report_path`, failed path named, and enough human-readable routing detail.
- Active surface coverage: the active adversarial review template and two
  active `review-report` prompts align with the overlay contract.
- Stale one-off handling: one-off or checkpoint language is not broad-synced
  into fake authority.
- Retrieval metadata boundary: retrieval headers remain retrieval-only and do
  not imply authority, validation proof, approval, readiness, lifecycle
  completion, deployment/install/resolver status, edit permission, or source-of-
  truth promotion.
- Leakage: no `jb` project policy, GAP/CV Engine paths, lifecycle mechanics,
  validation habits, or handoff rules are imported into Orca authority.
- Non-claims: the patches do not claim validation, approval, readiness, merge
  safety, product readiness, resolver behavior, installation, deployment, or
  implementation completion.

After correctness findings, note friction only if it could cause a future
reviewer or Chief Architect thread to misroute the contract.

## Excluded Scope

Do not review Orca product strategy, proof quality, buyer proof, customer
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

`docs/review-outputs/adversarial-artifact-reviews/orca_review_report_contract_topology_adversarial_review_v0.md`

This prompt uses `review-report` output mode. The human-readable review value
belongs in the durable report above. Chat YAML is courier output only and is
valid only after that report has been successfully written.

The report must contain:

1. Review target and source-read ledger.
2. Git status and dirty sources relied on.
3. Scope and excluded scope.
4. Contract-topology decision assessment.
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
- Why it matters: concrete effect on contract topology, review routing, or
  future prompt safety.
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
  report_path: docs/review-outputs/adversarial-artifact-reviews/orca_review_report_contract_topology_adversarial_review_v0.md
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
  summary: "Failed to write required report to docs/review-outputs/adversarial-artifact-reviews/orca_review_report_contract_topology_adversarial_review_v0.md."
  findings_count: 0
  blocking_findings: []
  advisory_findings: []
  prior_findings_remediated: []
  next_action: "Resolve the report write failure, then rerun the review-report prompt."
```

Include enough brief human-readable failure detail to route the write failure.
Do not add extra YAML keys.
