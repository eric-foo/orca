# Data Capture Harness Operating Model Architecture Prompt Adversarial Review Prompt v0

```yaml
retrieval_header_version: 1
artifact_role: Full prompt artifact
scope: Read-only adversarial review prompt for the Data Capture Harness operating-model architecture prompt structure and launch efficacy.
use_when:
  - Reviewing whether the operating-model architecture prompt is structurally fit to launch.
  - Stress-testing the prompt's three-subagent architecture-planning requirement, source-loading economy, output contract, and boundary discipline.
authority_boundary: retrieval_only
open_next:
  - docs/prompts/product-planning/data_capture_harness_operating_model_architecture_prompt_v0.md
  - .agents/workflow-overlay/prompt-orchestration.md
  - .agents/workflow-overlay/source-loading.md
  - .agents/workflow-overlay/template-registry.md
stale_if:
  - The target architecture prompt is materially revised or superseded.
  - Orca prompt-orchestration, source-loading, review-lane, or template-registry rules are materially revised.
```

- Prompt target: model-neutral adversarial artifact review lane.
- Output mode: `review-report`.
- Review report path: `docs/review-outputs/adversarial-artifact-reviews/data_capture_harness_operating_model_architecture_prompt_adversarial_review_v0.md`.
- Prompt artifact path: `docs/prompts/reviews/data_capture_harness_operating_model_architecture_prompt_adversarial_review_prompt_v0.md`.
- Created: 2026-05-28.
- Edit permission for reviewer: read-only.
- Patch execution authorized: no.
- Architecture execution authorized: no.
- Runtime/source-system design authorized: no.
- Source-of-truth promotion claimed: no.

## Paste-Ready Prompt

```text
<role>
You are performing a read-only adversarial artifact review for Orca.
</role>

<commission>
Review target:
`docs/prompts/product-planning/data_capture_harness_operating_model_architecture_prompt_v0.md`

Review purpose:
Determine whether the target prompt structure is high-efficacy enough to launch
the Data Capture Harness operating-model architecture lane, especially under
the owner's requirement that standard architecture planning use exactly three
advisory subagents: directional, adversarial, and grounding.

This review is about the prompt as a prompt artifact. Do not perform the
architecture planning lane, do not produce the operating-model architecture,
and do not patch the target prompt.
</commission>

<workspace_preflight>
Worktree: `C:\Users\vmon7\Desktop\projects\orca`
Expected branch: `main`
Expected HEAD: `b7627d3`

Dirty-state allowance:
- Dirty and untracked prompt/overlay sources are allowed for advisory review.
- The target prompt is currently untracked unless the launcher says otherwise.
- Modified or untracked sources may support advisory findings, but do not
  claim prompt readiness, validation, approval, acceptance, or source-of-truth
  promotion from dirty evidence alone.

Required output mode:
- `review-report`
- Write the durable report to:
  `docs/review-outputs/adversarial-artifact-reviews/data_capture_harness_operating_model_architecture_prompt_adversarial_review_v0.md`

If the report cannot be written, return `FAILED_REVIEW_OUTPUT_WRITE` and do not
treat chat output as the durable review artifact.
</workspace_preflight>

<required_method_sequence>
1. REFERENCE-LOAD `workflow-deep-thinking`.
2. REFERENCE-LOAD `workflow-adversarial-artifact-review`.
3. Do not APPLY either method yet. Before source readiness, use them only to
   prepare neutral source-reading questions.
4. SOURCE-LOAD the required Orca sources below.
5. Declare `SOURCE_CONTEXT_READY` or `SOURCE_CONTEXT_INCOMPLETE`.
6. Only after source readiness, APPLY `workflow-deep-thinking` to frame the
   boundary problem, hidden assumptions, prompt failure modes, and decision
   criteria.
7. Then APPLY `workflow-adversarial-artifact-review` to the target prompt.

If `workflow-adversarial-artifact-review` is unavailable, unresolved, or cannot
be applied after `SOURCE_CONTEXT_READY`, return a blocked or advisory-only
result. Do not emit formal verdicts, readiness claims, validation claims,
mandatory remediation, patch queues, executor-ready handoffs, or
alignment-complete claims.
</required_method_sequence>

<required_sources>
Control and overlay sources:
- `AGENTS.md`
- `.agents/workflow-overlay/README.md`
- `.agents/workflow-overlay/source-of-truth.md`
- `.agents/workflow-overlay/source-loading.md`
- `.agents/workflow-overlay/artifact-roles.md`
- `.agents/workflow-overlay/retrieval-metadata.md`
- `.agents/workflow-overlay/prompt-orchestration.md`
- `.agents/workflow-overlay/review-lanes.md`
- `.agents/workflow-overlay/communication-style.md`
- `.agents/workflow-overlay/template-registry.md`

Reusable method sources:
- `workflow-deep-thinking`
- `workflow-adversarial-artifact-review`
- `workflow-architecture-planning`
- `workflow-prompt-orchestrator`

Target and controlling prompt sources:
- `docs/prompts/product-planning/data_capture_harness_operating_model_architecture_prompt_v0.md`
- `docs/prompts/templates/review/adversarial_artifact_review_v0.md`
- `docs/prompts/templates/_generic/claude_opus_prompting_best_practices_v0.md`

Product-method context only as needed to test prompt fit:
- `docs/product/data_capture_obligation_baseline_decision_v0.md`
- `docs/product/data_capture_harness_product_goal_direction_signal_decision_v0.md`
- `docs/product/core_spine_v0_data_capture_spine_obligation_contract_v0.md`
</required_sources>

<review_questions>
Attack these questions first:

1. Does the prompt actually maximize the chance of a strong architecture output,
   or does its structure encourage template-filling, overbroad source loading,
   or premature target selection?
2. Does the prompt handle the three-subagent requirement correctly under the
   workflow-architecture-planning evidence-lane contract?
3. Does each delegated subagent have enough source context, source-readiness
   gating, and advisory-only boundary to avoid under-sourced architecture input?
4. Is the hard `BLOCKED_SUBAGENT_UNAVAILABLE` behavior correct for the likely
   launch environment, or should the prompt split into an agent-enabled
   architecture prompt and a plain-Opus wrapper with explicitly local
   perspectives?
5. Is the required source pack narrow enough for efficacy, or should it be
   reduced, staged, or converted into a source capsule to avoid context bloat?
6. Does the target artifact contract ask for the smallest complete architecture
   artifact, or does it overprescribe sections that may reduce synthesis
   quality?
7. Are method sequencing, output mode, write path, dirty-state allowance,
   non-claims, and no-implementation boundaries internally consistent?
8. Does the prompt leak into runtime/source-system design, ECR, Cleaning,
   Judgment, implementation scoping, validation, readiness, acceptance, or
   source-of-truth promotion?
</review_questions>

<finding_contract>
Report findings first, ordered by materiality.

For each finding include:
- finding id;
- phase: `correctness` or `friction`;
- severity: `critical`, `major`, or `minor` as finding-priority labels only;
- location or stable search key in the reviewed prompt;
- issue;
- evidence;
- impact on launch efficacy, source grounding, boundary control, or output
  usefulness;
- minimum_closure_condition;
- next_authorized_action.

Do not include `patch_queue_entry`. The review is read-only.
</finding_contract>

<allowed_recommendations>
Use exactly one advisory recommendation:
- `use_as_is`: no material prompt-structure issue found.
- `patch_before_launch`: prompt is usable after bounded prompt-structure patching.
- `split_before_launch`: launch-environment ambiguity means the prompt should
  be split into separate agent-enabled and plain-Opus prompt/wrapper paths
  before launch.
- `block_launch`: prompt has a correctness defect that makes launch unsafe or
  misleading under the current commission.

These recommendation labels are advisory review outputs only. They are not
approval, validation, readiness, owner acceptance, mandatory remediation, or
implementation authority.
</allowed_recommendations>

<output_contract>
Write the full review report to:
`docs/review-outputs/adversarial-artifact-reviews/data_capture_harness_operating_model_architecture_prompt_adversarial_review_v0.md`

The report must include:
- source-readiness declaration;
- source-read ledger;
- dirty/untracked source caveats;
- review boundary and excluded scope;
- findings;
- non-findings that matter;
- not-proven boundaries;
- advisory recommendation;
- smallest next authorized step.

After writing the report, return only a compact human summary plus courier YAML:

review_summary:
  status: completed
  report_path: docs/review-outputs/adversarial-artifact-reviews/data_capture_harness_operating_model_architecture_prompt_adversarial_review_v0.md
  recommendation: use_as_is | patch_before_launch | split_before_launch | block_launch
  summary: "..."
  findings_count: N
  blocking_findings: [...]
  advisory_findings: [...]
  next_action: "..."
</output_contract>

<review_use_boundary>
This is a read-only adversarial artifact review. Findings are decision input
for the owner or a separately authorized prompt-patching lane. They are not
approval, validation, readiness, buyer proof, mandatory remediation, patch
authority, architecture execution, or implementation authority.
</review_use_boundary>
```
