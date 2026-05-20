# Prompt Orchestration

This file defines Orca's lightweight prompt-orchestration layer. It is docs-first and binds reusable mechanics from `agent-workflow` to Orca-owned paths without importing `jb` project policy.

## Source Boundary

Reusable mechanics may come from `agent-workflow` source documents and queue records:

- prompt artifact creation and thin-wrapper prompts;
- worktree preflight and hash pins;
- explicit output mode;
- source hierarchy and hard constraints;
- required checks, verdicts, and rerun economy.

Orca-specific facts, product constraints, artifact paths, review lanes, validation gates, and safety rules must come from `AGENTS.md`, this overlay, or accepted Orca docs named in `.agents/workflow-overlay/source-of-truth.md`.

`prompt_orchestrator.yaml`, `product-ultraplan.yaml`, and `feature-ultraplan.yaml` are non-executable queue records unless later accepted source creates real workflow-kernel skills and Orca validates adoption. Do not create `SKILL.md`, install skills, or copy `jb` templates from Orca prompt-orchestration work.

## Supported Prompt Families

| Family | Purpose | Default artifact destination | Default output mode |
| --- | --- | --- | --- |
| Product planning | Frame product bets, evidence standards, kill criteria, and handoff boundaries | `docs/prompts/product-planning/` | `chat-only` or `file-write` |
| Feature planning | Turn an accepted product bet into evidence-producing capability plans | `docs/prompts/feature-planning/` | `chat-only` or `file-write` |
| Deep reasoning | Compare options, downgrade weak candidates, preserve assumptions, and recommend | `docs/prompts/deep-thinking/` | `chat-only` |
| Implementation handoff | Prepare a source-changing unit after implementation is explicitly authorized | `docs/prompts/handoffs/` | `file-write` |
| Review | Ask a read-only or patch-authorized reviewer to inspect artifacts | `docs/prompts/reviews/` or `docs/review-inputs/` | `review-report` |
| Rerun or patch | Retry an unresolved finding without reopening settled decisions | `docs/prompts/reruns/` or `docs/prompts/patches/` | `patch-queue` |

Typed child folders under `docs/prompts/` may be created when the first prompt of that family is authored. Until implementation is explicitly authorized, source-changing handoff prompts must target documentation or overlay work only.

## Full Prompt Versus Thin Wrapper

A full prompt is the durable artifact. It must include:

- objective and intended decision;
- Orca source hierarchy and required reads;
- source paths plus hashes or revisions when stability matters;
- hard constraints and forbidden imports;
- output mode and exact output contract;
- target artifact roles and write permissions;
- validation gates and required verdicts;
- assumptions, unknowns, and blocked conditions.

A thin wrapper is a short invocation of a full prompt. It must include:

- referenced full prompt path and hash or revision;
- workspace path, branch or revision, and dirty-state allowance;
- target files or directories;
- output mode and edit permission;
- only the delta needed for this run.

Thin wrappers must not restate or fork project policy. If policy changes are needed, update the full prompt or overlay first.

## Review Prompt Defaults

All Orca review prompts must explicitly trigger `workflow-deep-thinking`
before the relevant review skill, such as `workflow-adversarial-artifact-review`
or `workflow-code-review`.

The deep-thinking step should frame the boundary problem, failure modes, and
decision criteria before findings are listed. It does not widen the review
scope, authorize patching, or turn a narrow review into product planning.

Review prompts should still return the requested review output shape. Deep
thinking improves the reviewer’s risk framing; the final answer remains a
review report with findings, non-findings, not-proven boundaries, and next
authorized step.

## Required Preflight Fields

Every repo-aware Orca prompt must state:

- workspace path or repository identifier;
- expected branch, detached revision, or commit hash when source stability matters;
- dirty-state allowance and whether untracked files are in scope;
- target files or directories;
- source hierarchy for the task;
- edit permission: `read-only`, `patch-only`, or `docs-write`;
- output mode: `chat-only`, `file-write`, `review-report`, or `patch-queue`;
- required validation gates and where evidence is recorded;
- external source boundary, including the rule that `agent-workflow` is read-only reusable source and `jb` is not Orca authority.

Rerun and patch prompts must also name the prior artifact, prior hash or revision, frozen decisions, mutable fields, and unresolved finding being retried.

## Output Modes

- `chat-only`: return analysis, options, recommendations, and blocked assumptions without writing files.
- `file-write`: write only authorized Orca documentation or overlay files; report changed files and validation evidence.
- `review-report`: perform read-only review unless a patch-execution lane is explicitly assigned; write reports under `docs/review-outputs/` when requested.
- `patch-queue`: produce stable patch units, target files, authority basis, and validation gates. Applying patches requires separate execution authority.

## Prompt Validation Gates

Before using a generated Orca prompt, apply these gates:

1. Overlay authority loaded: `AGENTS.md` and `.agents/workflow-overlay/README.md` were read.
2. Artifact roles bound: every prompt role maps to `.agents/workflow-overlay/artifact-roles.md` or another accepted overlay file.
3. Source resolution clean: agent-workflow material is source guidance only; installed skills are deployment copies; `jb` project policy is not imported.
4. Worktree preflight present: workspace, revision, dirty-state allowance, target scope, and edit permission are explicit when repository state matters.
5. Output mode explicit: exactly one output mode is named, with write destination and report destination if applicable.
6. Required checks named: validation gates can fail and include pass, fail, blocked, and not-run semantics.
7. Rerun economy satisfied: retry prompts preserve frozen decisions and avoid scope reset.

## Prompt Verdicts

- `PASS`: all required prompt gates are satisfied.
- `PASS_WITH_WARNINGS`: prompt may be used, but named assumptions or unknowns must travel with it.
- `BLOCKED`: required authority, role binding, source, or preflight data is missing.
- `FAILED`: the prompt violates a hard constraint, imports forbidden policy, or changes output mode without authority.

## Anti-Import Rules

- Do not copy `jb` prompt templates, skill files, GAP/CV Engine policy, compiler paths, handoff rules, product-lead rules, or repo-local lifecycle mechanics.
- Do not claim `workflow-product-ultraplan`, `workflow-feature-ultraplan`, or `workflow-prompt-orchestrator` are executable unless a real `agent-workflow` `SKILL.md` exists and Orca source-resolution/adoption checks pass.
- Generic layout ideas may be reused only after binding to Orca paths, artifact roles, output modes, and validation gates.
