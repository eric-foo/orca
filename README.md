# Orca

Orca is separate from `jb` and does not inherit `jb` project assumptions, lifecycle rules, validation rules, product policy, or artifact authority.

Project-specific facts belong in `.agents/workflow-overlay/`. If a fact is not declared there or in an Orca-owned source document, treat it as `UNKNOWN - requires owner input`.

Explicitly invoked or resolver-loaded skills may provide task-local mechanics only; they are not Orca project authority.

## Current Authority

- Project overlay: `.agents/workflow-overlay/`
- Docs workspace: `docs/`
- Bootstrap record: `docs/workflows/orca_bootstrap_record.md`
- Migration import queue: `docs/migration/import_queue.md`

## Current Unknowns

- Orca product/domain purpose: UNKNOWN - requires owner input
- Orca implementation scope: UNKNOWN - requires owner input
- Orca runtime or automation stack: UNKNOWN - requires owner input
- Orca external integrations: UNKNOWN - requires owner input
