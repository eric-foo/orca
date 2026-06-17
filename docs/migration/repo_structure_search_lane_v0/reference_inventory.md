# Search-lane Reference Inventory (v0)

Hand-verified pre-apply (worker sweep, this session) and re-scanned by
`apply_moves.py --dry-run` at apply time. Classes: `live` = rewritten by
`--apply`; `historical` = kept, resolved via `moved_paths_index.md`;
`moved_set` = inside a moved file (rewritten where the reference is a full old
path).

Move-set (4): see `moves_manifest.csv`.

## Full-path references that `--apply` rewrites (old path -> new search/ path)

| Referencing file | Class | References | Lines |
| --- | --- | --- | --- |
| `docs/product/data_capture_spine/demand_durability_indicator_capture_deconfliction_note_v0.md` | live (stays) | search-interest capture profile (file 4) | 21, 134 |
| `docs/product/data_capture_spine/demand_search_interest_sourcing_and_gate_delta_spec_v0.md` | moved_set (file 3) | search-interest capture profile (file 4), `open_next:` full path | 21 |

## NOT rewritten (by design)

- AEO report -> evidence JSON: the `"<evidence>.json (same folder)"` note is a
  bare filename; both files move into `docs/product/search/` together, so it
  stays correct.
- Bare-filename mentions of the capture profile inside the #228 spec (lines 46,
  121): filename-only, resolve regardless of folder.

## Coverage notes

- No references found in the repo map (`docs/workflows/orca_repo_map_v0.md`),
  `docs/STRUCTURE.md`, `docs/product/README.md`,
  `.agents/workflow-overlay/artifact-folders.md`,
  `.agents/workflow-overlay/source-loading.md`, or `repo-structure.yaml`.
- The #228 source-class spec (file 3) and the AEO files (1, 2) carry no inbound
  references beyond the rows above.
- No inbound content-hash pin covers any of the four moved files (file 3 has
  zero inbound references; file 4 is referenced by path, not hash), so rewriting
  the one `moved_set` internal reference is hash-safe.
- `apply_moves.py --dry-run` re-scans the live tree at apply time. If a
  concurrent lane has added a new full-path reference by then, it is reported and
  rewritten; if a reference appears that is outside this inventory, surface it for
  reconciliation per the lock's stop condition rather than auto-trusting it.
