# Review Lanes

## Current Lanes

- Artifact review: read-only review of docs, decisions, prompts, and migration artifacts. Reviewers may write reports only under `docs/review-outputs/` unless a prompt authorizes a different Orca-owned report path.
- Patch or integration execution: applies accepted documentation patches inside Orca and reports changed files plus validation.
- Workflow-kernel adoption review: deferred until `agent-workflow` canonical source exists and a later turn authorizes adoption or shadow validation.

## Rules

- Reviewer threads are source-read-only unless explicitly assigned patch execution.
- Executor threads must not report success without file and validation evidence.
- Installed global `review`, implementation/code review, and artifact review remain separate lanes until Orca accepts more specific routing.
- Model lanes and output contracts: UNKNOWN - requires owner input.
