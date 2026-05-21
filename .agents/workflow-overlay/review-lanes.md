# Review Lanes

## Current Lanes

- Artifact review: read-only review of docs, decisions, prompts, and migration artifacts. Reviewers may write reports only under `docs/review-outputs/` unless a prompt authorizes a different Orca-owned report path.
- Prompt review: read-only review of prompt artifacts, thin wrappers, source maps, output modes, and validation gates. Reports go under `docs/review-outputs/` unless the prompt names another Orca-owned report path.
- Patch-queue review: read-only review that produces ordered patch units. Applying those patches requires a separate patch or integration execution assignment.
- Patch or integration execution: applies accepted documentation patches inside Orca and reports changed files plus validation.
- Workflow-kernel adoption review: deferred until `agent-workflow` canonical source exists and a later turn authorizes adoption or shadow validation.

## Rules

- Reviewer threads are source-read-only unless explicitly assigned patch execution.
- Review prompts must explicitly trigger `workflow-deep-thinking` before the
  relevant review skill so the reviewer frames failure modes before listing
  findings. This does not expand review scope or authorize patching.
- Adversarial artifact review prompts should request the compact
  `review_summary` YAML shape from
  `.agents/workflow-overlay/communication-style.md` before detailed findings.
- Executor threads must not report success without file and validation evidence.
- Installed global `review`, implementation/code review, and artifact review remain separate lanes until Orca accepts more specific routing.
- Model lanes: UNKNOWN - requires owner input.
- Prompt output contracts are bound in `.agents/workflow-overlay/prompt-orchestration.md`.
