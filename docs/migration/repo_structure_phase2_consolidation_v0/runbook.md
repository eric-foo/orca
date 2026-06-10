# Phase-2 Consolidation Runbook - docs/product by-lane move

```yaml
retrieval_header_version: 1
artifact_role: Orca migration record
scope: >
  Owner runbook for applying the prepared Phase-2 consolidation: docs/product
  flat files into bound lane subfolders, plus the deferred activations from the
  repo-structure binding (placement hook wiring, harness scratch config).
use_when:
  - Executing or reviewing the Phase-2 product consolidation.
  - Wiring the EP-04 placement hook or applying the harness scratch config.
authority_boundary: retrieval_only
open_next:
  - docs/decisions/orca_repo_structure_binding_v0.md
  - docs/migration/repo_structure_phase2_consolidation_v0/moves_manifest.csv
  - docs/migration/repo_structure_phase2_consolidation_v0/reference_inventory.md
stale_if:
  - The apply has run (this runbook then documents history, not pending work).
  - moves_manifest.csv is regenerated after docs/product changes.
```

## What this applies

99 file moves: `docs/product/*.md` flat files into the six bound lanes
(`core_spine/` 32, `data_capture_spine/` 48, `judgment_spine/` 8,
`product_lead/` 7, `signal_content/` 2, `ecr/` 2). One residual stays flat by
design (`engagement_logic_registry_v0.md`). 82 tracked files move via `git mv`
(history preserved); 17 untracked files move on the filesystem. Moved files'
content is NOT edited (content-hash pins in other lanes' records survive).
Path references are rewritten only in the 10 live navigation/authority
surfaces named in `reference_inventory.md`; the 591 historical referencing
files keep their original path text and resolve via `moved_paths_index.md`
(written by the apply). Validated by dry-run 2026-06-11 (exit 0, zero
collisions).

## PRECONDITION GATE (do not skip)

1. Review and commit (or deliberately exclude) the current worktree state so
   the tree is clean - the apply REFUSES on a dirty tree. This is the rollback
   checkpoint: after it, `git reset`/`git checkout` can undo everything the
   apply does to tracked files. The 17 untracked moves are reversed by
   `--reverse`.
   - Tonight's binding work (new + edited files, claim inventory in the
     closeout) should be part of that checkpoint commit(s).
   - Shared files edited tonight (`.claude/settings.json` was NOT edited;
     `docs/workflows/orca_repo_map_v0.md` WAS) follow the commit-once-whole
     discipline: `git commit --only -- docs/workflows/orca_repo_map_v0.md`.
2. Only if you accept reduced rollback safety, `--waive-dirty-tree` overrides
   the gate. Not recommended.

## Apply sequence

```text
cd <repo root>
python docs/migration/repo_structure_phase2_consolidation_v0/apply_moves.py --dry-run   # re-validate
python docs/migration/repo_structure_phase2_consolidation_v0/apply_moves.py --apply
python .agents/hooks/check_placement.py --strict          # expect exit 0
python .agents/hooks/check_repo_map_freshness.py --changed # advisory; map rows already rewritten
git diff --stat                                            # review scope: moves + 10 live surfaces + map
```

Then commit per shared-file discipline (repo map and overlay files
explicit-path first), with `repo-map-ack: phase-2 product consolidation` in
the commit message if the freshness strict gate is used.

Optional second pass: `--rewrite-product-internal` rewrites old paths inside
the moved files themselves (91 files hold such references). This EDITS CONTENT
and changes file hashes - verify no hash pin covers a file before running it
(see `docs/hygiene/queue.md` ORCA-HYGIENE-002/004/005 for known pins).
Default: leave off; the index covers resolution.

Rollback: `--reverse` restores all 99 paths (git mv back / filesystem move
back); content edits to live surfaces and the machine map revert via git from
the checkpoint.

## Deferred activations bundled with this runbook

1. **Placement hook wiring (owner action; was permission-denied for the
   agent as self-modification).** Add beside the two existing PostToolUse
   hooks in `.claude/settings.json`:

   ```json
   { "type": "command", "command": "python .agents/hooks/check_placement.py --hook", "timeout": 10 }
   ```

   Restart the session afterward (hooks load at session start).

2. **Harness scratch consolidation.** Apply
   `harness_scratch_config_snippet.toml` to `orca-harness/pyproject.toml`
   AFTER the other lane's dirty `pyproject.toml`/`README.md` changes are
   committed (do not entangle). Then add `orca-harness/_scratch/` to
   `.gitignore` and delete the now-redundant top-level pytest cache dirs at
   will (they regenerate under `_scratch/`).

## Non-claims

Not validation, readiness, or product proof. The apply changes placement and
navigation surfaces only; no artifact's authority, content (default mode), or
acceptance state changes. A green `--strict` run after apply is placement
shape, not correctness.
