# Search-lane Migration Runbook

```yaml
retrieval_header_version: 1
artifact_role: Orca migration record
scope: >
  Owner runbook for applying the search-lane migration: physically move the 4
  search-primary docs into docs/product/search/ and rewrite the small live
  reference set. Bound by docs/decisions/orca_search_product_lane_binding_v0.md.
use_when:
  - Executing or reviewing the search-lane physical move.
authority_boundary: retrieval_only
open_next:
  - docs/decisions/orca_search_product_lane_binding_v0.md
  - docs/migration/repo_structure_search_lane_v0/moves_manifest.csv
  - docs/migration/repo_structure_search_lane_v0/reference_inventory.md
stale_if:
  - The apply has run (this runbook then documents history, not pending work).
  - moves_manifest.csv changes.
```

## What this applies

4 tracked file moves into `docs/product/search/` (the AEO probe + its evidence
JSON, the search/AEO source-class spec, and the search-interest capture profile)
plus ~3 live reference-line rewrites (see `reference_inventory.md`). Moved files'
content is not edited except the one `moved_set` internal full-path reference
(the #228 spec's `open_next:` pointer to the capture profile); no inbound
content-hash pin covers any of the four files. The apply also flips
`repo-structure.yaml` `search` status `planned` -> `current`.

## PRECONDITION GATE (do not skip)

1. **Owner-coordinated freeze of `data_capture_spine`.** This is the move's only
   contended lane (files 3 and 4 plus the deconfliction-note edit live there, and
   the demand/durability lanes are active). The agent cannot enforce this freeze;
   the owner coordinates one of: (a) let the active `data_capture_spine` lanes
   merge to main, then apply on a quiesced base; (b) pause those lanes for the
   apply window; or (c) accept that git rename-detection auto-resolves most
   their-edit + our-rename merges and hand-resolve the rest. The AEO pair
   (files 1 and 2, `source_capture_toolbox/`) is low-contention.
2. **Clean commit checkpoint.** Commit (or deliberately exclude) the worktree so
   the tree is clean - `--apply` REFUSES on a dirty tree. This is the rollback
   checkpoint. `--waive-dirty-tree` overrides only if you accept reduced rollback
   safety (not recommended).

## Apply sequence

```text
cd <this search-lane worktree root>
python docs/migration/repo_structure_search_lane_v0/apply_moves.py --dry-run   # expect exit 0
python docs/migration/repo_structure_search_lane_v0/apply_moves.py --apply
python .agents/hooks/check_placement.py --strict                               # expect exit 0
# reference-resolution: no stale old-path hits should remain in LIVE docs
git grep -n "source_capture_toolbox/aeo_capture_feasibility_probe_phase0_v0\|data_capture_spine/demand_search_interest_sourcing_and_gate_delta_spec_v0.md\|data_capture_spine/demand_durability_indicator_search_interest_capture_profile_v0.md" -- docs ":!docs/decisions" ":!docs/review-inputs" ":!docs/review-outputs" ":!docs/prompts" ":!docs/research" ":!docs/hygiene" ":!docs/migration"
git diff --stat
```

Then commit (4 renames + the rewritten references + the status flip +
`moved_paths_index.md`).

## Validation

- `--dry-run` exit 0 (sources exist, targets free, no collision).
- `check_placement.py --strict` exit 0 (placement shape; the search lane is
  recognized via `repo-structure.yaml` `product_lanes`).
- reference-resolution grep above returns nothing (historical records keep old
  paths by design and resolve via `moved_paths_index.md`).
- `git log --follow` on a moved file shows history preserved (git mv).

A green check is placement shape only - not validation, readiness, or product
proof.

## Rollback

`python docs/migration/repo_structure_search_lane_v0/apply_moves.py --reverse`
restores the 4 paths (git mv back). The live-reference rewrites and the status
flip are content edits - revert them via git from the checkpoint (they are not
undone by `--reverse`).

## Non-claims

Not validation, readiness, or product proof. The apply changes placement and a
small reference set only; no artifact's authority, content (beyond the one
internal reference line), or acceptance state changes.
