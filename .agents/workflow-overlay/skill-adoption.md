# Skill Adoption

## Current Status

- Orca has no local reusable workflow-kernel skill source.
- Orca has no accepted global skill shadow candidates.
- Orca has no same-name global skill promotions.
- Future reusable workflow skills must come from accepted `agent-workflow` canonical source and validated deployment copies.

## Adoption Rules

- Use shadow names before any same-name promotion.
- Re-check repo-local, installed global/system, user-level, plugin-contributed, and other resolver-visible skill names before adoption work.
- Record source path, source hash, overlay loaded, collision status, and rollback path for any adoption validation.
- Missing overlay authority must fail visibly when a reusable skill requires project facts.

## Known Turn 6 Snapshot

The Turn 6 resolver-visible skill snapshot is recorded in `docs/workflows/orca_bootstrap_record.md`.
