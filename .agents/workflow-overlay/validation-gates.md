# Validation Gates

Validation must be able to fail. Missing evidence is not a pass.

## Current Gates

- Required Orca files exist before claiming bootstrap completion.
- No software implementation directories are present unless explicitly authorized.
- `AGENTS.md` and overlay files do not encode `jb` project-specific authority as Orca rules.
- Source hashes for migration-governance inputs are recorded in `docs/workflows/orca_bootstrap_record.md`.
- Resolver-visible skill-name snapshots are recorded before any skill adoption or promotion work.
- Git status is reported when this workspace is a Git repo.

## Future Gates

- Orca independence dry run: UNKNOWN - requires owner input.
- Product/domain validation: UNKNOWN - requires owner input.
- Runtime or integration validation: UNKNOWN - requires owner input.
