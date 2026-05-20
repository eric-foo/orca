# Source Of Truth

## Current Source Hierarchy

1. Explicit user instruction for the current turn.
2. Orca `AGENTS.md`.
3. This overlay under `.agents/workflow-overlay/`.
4. Orca docs under `docs/`, when they do not conflict with the overlay.
5. Future accepted `agent-workflow` reusable workflow-kernel source for generic mechanics only.

## Conflict Rules

- Orca overlay wins for Orca project facts.
- Future `agent-workflow` source may own reusable workflow mechanics, not Orca facts.
- Installed global/user/plugin skills are runtime copies or external tools, not Orca project authority.
- If a required source is missing, report a visible failure and name the missing file or decision.

## Known Source Documents

- `README.md`: workspace entrypoint.
- `AGENTS.md`: agent operating instructions.
- `.agents/workflow-overlay/README.md`: overlay entrypoint.
- `.agents/workflow-overlay/artifact-roles.md`: Orca artifact role bindings for reusable workflow methods.
- `.agents/workflow-overlay/prompt-orchestration.md`: Orca prompt artifact, wrapper, preflight, output mode, validation, and rerun bindings.
- `.agents/workflow-overlay/communication-style.md`: Orca response style for Chief Architect sequencing, review closeouts, and prompt handoffs.
- `docs/STRUCTURE.md`: docs-folder usage guide for future agents; subordinate to this overlay if conflicts appear.
- `docs/workflows/orca_bootstrap_record.md`: Turn 6 bootstrap record.
- `docs/migration/import_queue.md`: read-only import queue state.
- `docs/decisions/turn_08_product_thesis_v0.md`: current Orca product thesis and value proposition.
- `docs/workflows/turn_08_workflow_bedrock_maximization.md`: docs-first maximization plan for `workflow-deep-thinking`, future `workflow-product-ultraplan`, and future `workflow-feature-ultraplan`.
