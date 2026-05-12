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
- `docs/workflows/orca_bootstrap_record.md`: Turn 6 bootstrap record.
- `docs/migration/import_queue.md`: read-only import queue state.
