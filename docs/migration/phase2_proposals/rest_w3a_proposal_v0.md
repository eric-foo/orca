```yaml
retrieval_header_version: 1
artifact_role: Orca migration note
scope: >
  Phase-2 W3a deletion + ontology proposal for the "rest" area of orca/product/:
  everything except spines/, shared/, and case_families/ — covering satellites/
  (beauty + fragrance/judgment_level1) and the top-level README.md.
use_when:
  - Owner adjudicating Phase-2 deletion candidates for the rest/satellites area.
  - Reviewing ontology/doc-term findings for satellites + README before a Phase-3 strict gate.
authority_boundary: retrieval_only
open_next:
  - docs/migration/orca_second_pass_consolidation_plan_v0.md
stale_if:
  - Any satellite file is deleted, moved, or superseded after this proposal is written.
  - The ontology SSOT (ontology.yaml) adds or retires a type that would change findings here.
```

# Phase-2 W3a Proposal — rest

## Summary

**Area:** `orca/product/` excluding `spines/`, `shared/`, `case_families/`.

**Dirs scanned:**
- `orca/product/` (top-level — README.md only)
- `orca/product/satellites/beauty/`
- `orca/product/satellites/fragrance/judgment_level1/casebook_admission/`
- `orca/product/satellites/fragrance/judgment_level1/named_case_screens/`
- `orca/product/satellites/fragrance/judgment_level1/reconciliation/`
- `orca/product/satellites/fragrance/judgment_level1/satellite_skeleton/`

**No `ecr/` or `product_lead/` directories exist** under `orca/product/` (confirmed by glob).

**Files scanned (6 total):**
1. `orca/product/README.md`
2. `orca/product/satellites/beauty/beauty_venue_card_set_v0.md`
3. `orca/product/satellites/fragrance/judgment_level1/casebook_admission/fragrance_level1_casebook_admission_frame_v0.md`
4. `orca/product/satellites/fragrance/judgment_level1/named_case_screens/fragrance_level1_named_case_candidate_screen_v0.md`
5. `orca/product/satellites/fragrance/judgment_level1/reconciliation/fragrance_level1_product_learning_reconciliation_v0.md`
6. `orca/product/satellites/fragrance/judgment_level1/satellite_skeleton/fragrance_level1_product_learning_satellite_skeleton_v0.md`

---

## A. Deletion candidates

None — area is lean.

**Evidence summary per file:**

**File 1: `orca/product/README.md`**
- reverse_ref_check: 10+ inbound refs across `repo-structure.yaml`, `artifact-folders.md`, `check_placement.py`, multiple spines, migration index, consolidation plan, promotion decision, and shared engagement registry. It is the authoritative product-tree entry point.
- verdict: Keep. Active, multiply-referenced, non-bloat structure doc.

**File 2: `orca/product/satellites/beauty/beauty_venue_card_set_v0.md`**
- reverse_ref_check: 15+ inbound refs across `orca_repo_map_v0.md`, `orca_demand_scan_core_spec_v0.md`, `orca_vertical_exploration_guide_v0.md`, `beauty_venue_card_set_promotion_decision_v0.md`, `beauty_subtle_decision_screen3_ledger_v0.md`, `ingestible_beauty_screen1_ledger_v0.md`, `venue_basenotes_v0.md`, `orca_demand_read_taxonomy_v0.md`, all four fragrance satellite files, and `judgment_current_state_and_decomposition_v0.md`.
- verdict: Keep. This is the SOLE maintained beauty venue asset, owner-promoted with a hard 12-card cap. Highly referenced; no successor; not bloat.

**Files 3-6: fragrance/judgment_level1 cluster (4 files)**
- reverse_ref_check: All four files are multiply referenced from `judgment_current_state_and_decomposition_v0.md` (lines 23-26, 225-228, 250-253), `orca_spine_first_target_structure_binding_v0.md`, `spine_first_untagged_file_inventory_v0.md`, `spine_first_target_move_table_v0.md`, `moved_paths_index.md`, and the consolidation plan. The four files also mutually cross-reference each other as an intentional cluster.
- verdict: Keep. They form the current fragrance Level 1 product-learning cluster; they are the live, properly-placed, multiply-referenced artifacts for this satellite. No predecessor versions exist to clean up (all migrated from `docs/product/judgment_spine/` to these paths in the spine-first migration). No bloat pattern.

**Conclusion: 0 deletion candidates.** The area is the smallest possible set of active, correctly-placed satellite artifacts plus one structural README. No orphans, no superseded versions, no duplicates, no dead ends.

---

## B. Ontology / doc-term findings

**Scan method:** Multi-hump CamelCase token grep across all 6 files vs. SSOT canonical types (Vertical, Brand, Product, Venue, WindCaller, Call, Observation, TrendVector, DecisionEvent, Reading, Memo, Case, Outcome, CapturePacket, EvidenceUnit, Buyer, Org) and runtime aliases (SourceCapturePacket, FacilitatorLedger, CaseReport). Head nouns from multi-hump canonical: Caller, Vector, Event, Packet, Unit.

**Known SSOT terms observed in this area:** TrendVector (used by implication in `reading` / `action_ceiling` schema field names in satellite_skeleton), CapturePacket (referenced in schema field `packet_id`). No problematic usage — all occurrences are schema placeholder fields, not novel coinages.

**New-term candidates (ontology-shaped coinages NOT in SSOT):** None found.

All multi-hump CamelCase tokens in this area are:
- Proper venue/brand names: BeautyMatter, BeautyGuruChatter, AsianBeauty, SkincareAddiction, CaFleureBon (venue names in the card table — not ontology-shaped coinages; head nouns are Matter, Chatter, Beauty, Addiction, Bon — none are ontology head nouns).
- TikTok (proper noun, one hump ending in acronym shape — excluded by the checker's multi-hump rule).

No deprecated or aliased SSOT terms are used in drift-risk ways. The satellite files reference `SourceCapturePacket` and `FacilitatorLedger` only via pointer paths to the runtime files, not as coined type names.

**Verdict: Clean.** Zero new-term candidates. Zero deprecated/aliased-term drift. Zero SSOT conflicts.
