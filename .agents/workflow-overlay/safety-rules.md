# Safety Rules

## Project-Specific Safety

- Fail visibly when required Orca authority is missing.
- Do not substitute `jb` paths, product facts, lifecycle rules, or validation gates.
- Do not create software implementation while Orca is docs-first.
- Do not mutate external reference folders during import planning.
- Do not edit installed global skills, user-level skills, plugin cache files, or external workflow source unless a later turn explicitly authorizes it.
- Do not commit, push, configure remotes, create pull requests, or perform destructive cleanup unless explicitly authorized.

## Rollback Boundary

Rollback for this bootstrap is additive: remove the newly created Orca directory only with explicit user approval. No rollback step may edit `jb`, installed skills, user-level skills, plugin skills, or external reference folders.
