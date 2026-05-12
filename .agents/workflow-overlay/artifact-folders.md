# Artifact Folders

## Accepted Folders

- `docs/decisions/`: Orca decision records.
- `docs/prompts/`: Orca prompt artifacts.
- `docs/review-inputs/`: artifacts prepared for review.
- `docs/review-outputs/`: reviewer reports and verdicts.
- `docs/workflows/`: workflow records owned by Orca.
- `docs/migration/`: migration and import queue records.

## Rules

- Keep docs-first artifacts under `docs/` unless a later Orca decision creates a narrower folder.
- Do not create implementation folders such as `src`, `app`, `packages`, `tests`, or automation runtimes until explicitly authorized.
- Do not copy or move material from external reference folders unless a later turn explicitly authorizes the import.
