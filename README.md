# Orca

Orca is a docs-first project/workspace at this stage. It is separate from `jb` and does not inherit `jb` project assumptions, lifecycle rules, validation rules, product policy, or artifact authority.

No software implementation exists yet. Do not create implementation directories, runtimes, packages, tests, or automation code until a later turn explicitly authorizes implementation.

Project-specific facts belong in `.agents/workflow-overlay/`. If a fact is not declared there or in an Orca-owned source document, treat it as `UNKNOWN - requires owner input`.

Reusable workflow skills are expected to come from a future `agent-workflow` canonical source and validated deployment copies. Orca must not rely on copied `jb` repo-local skills as reusable authority.

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
