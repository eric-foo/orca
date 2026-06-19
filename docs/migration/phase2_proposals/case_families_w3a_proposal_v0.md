```yaml
retrieval_header_version: 1
artifact_role: Orca migration note
scope: >
  Phase-2 W3a proposal for the case_families area (orca/product/case_families/):
  bloat/deletion candidates with full deletion-evidence records and
  ontology/doc-term findings against the SSOT.
use_when:
  - Owner adjudicating Phase-2 deletion candidates for the case_families area
    (product_learning/other_verticals/ + product_learning/fragrance/).
  - Reviewing ontology/doc-term drift findings for case-families files before
    a Phase-3 ratchet.
authority_boundary: retrieval_only
open_next:
  - docs/migration/orca_second_pass_consolidation_plan_v0.md
stale_if:
  - Any case_families file is moved, renamed, or deleted after this proposal is
    written (inbound ref counts and successor paths change).
  - The owner resolves untagged decisions U-CF1 / U-CF2 / U-CF3 (may change
    sub-folder placement, not deletion status).
  - A new MV replay packet is produced that explicitly absorbs interim slices
    (would open deletion questions currently rated conservative-keep).
```

# Phase-2 W3a Proposal — case_families

## Summary

Files scanned: 24 (all `.md`; 1 in `fragrance/`, 23 in `other_verticals/`)
Deletion candidates: 0 high / 1 medium / 2 low
Ontology findings: 0 new-term candidates; 0 deprecated/aliased misuses; corpus is clean

## A. Deletion candidates

### Candidate 1 (medium confidence): `core_spine_v0_proof_case_selection_brief_v0.md`

```yaml
targets:
  - orca/product/case_families/product_learning/other_verticals/core_spine_v0_proof_case_selection_brief_v0.md
evidence:
  reverse_ref_check: >
    Grep of orca/product/, docs/, .agents/ for `proof_case_selection_brief`:
    - docs/migration/spine_first_target_move_table_v0.md:248 — migration table (historical, groups it with discovery corpus)
    - docs/migration/repo_structure_spine_first_v0/moved_paths_index.md:60 — migration provenance record
    - docs/workflows/orca_repo_map_v0.md:545 — live repo map EXPLICITLY notes:
      "Early proof case-selection brief; status BLOCKED_OWNER_CANDIDATES_NEEDED.
       For current case/backtest selection see the heavyweight discovery pass
       (…discovery_results_v0.md and …results_part_2_v0.md), which produced the
       candidates the brief was blocked on."
    - orca/product/case_families/product_learning/other_verticals/core_spine_v0_heavyweight_proof_case_discovery_charter_v0.md:44
      — names it in source-basis list (historical citation; not a runtime dependency)
    The repo map itself declares this file superseded by the discovery results.
    No live spine, product contract, or decision record depends on its content.
    Handling needed: update/remove repo-map entry (docs/workflows/orca_repo_map_v0.md:545)
    at execution time.
  successor: >
    orca/product/case_families/product_learning/other_verticals/core_spine_v0_heavyweight_proof_case_discovery_results_v0.md
    and
    orca/product/case_families/product_learning/other_verticals/core_spine_v0_heavyweight_proof_case_discovery_results_part_2_v0.md
    — together these produced the candidates the brief was blocked on.
    For register entry use the primary successor only:
    orca/product/case_families/product_learning/other_verticals/core_spine_v0_heavyweight_proof_case_discovery_results_v0.md
  semantic_delta: >
    The brief records BLOCKED_OWNER_CANDIDATES_NEEDED status and defines
    selection rules that were subsequently operationalized in the discovery
    charter and results artifacts. Its selection-rule content is a proper
    subset of the charter (which is the fuller operative document). No unique
    evidence, recommendation, or decision lives in this brief that is not
    recorded or superseded in the discovery corpus. Loss: the intermediate
    blocked-state record; preserved in git history.
  rollback: git revert <executing merge sha>
```

confidence: medium
rationale: superseded-by-discovery-corpus; repo map explicitly flags it as historical; status is permanently BLOCKED

---

### Candidate 2 (low confidence): `core_spine_v0_heavyweight_proof_case_discovery_charter_v0.md`

```yaml
targets:
  - orca/product/case_families/product_learning/other_verticals/core_spine_v0_heavyweight_proof_case_discovery_charter_v0.md
evidence:
  reverse_ref_check: >
    Grep of orca/product/, docs/, .agents/ for `heavyweight_proof_case_discovery_charter`:
    - docs/migration/spine_first_target_move_table_v0.md:248 — migration table
      (groups it with discovery corpus as `direct_move`; no deletion signal)
    - docs/migration/repo_structure_spine_first_v0/moved_paths_index.md:45 — migration provenance
    - docs/workflows/orca_repo_map_v0.md (not found in explicit entry — grouped under discovery corpus listing)
    - orca/product/case_families/product_learning/other_verticals/core_spine_v0_heavyweight_proof_case_discovery_results_v0.md:50
      — results artifact names it in source-basis list (historical citation)
    - orca/product/case_families/product_learning/other_verticals/core_spine_v0_heavyweight_proof_case_discovery_results_part_2_v0.md:47
      — same pattern
    No live spine, product-contract, or active decision depends on this charter
    for current authority. The results artifacts absorbed its boundary rules.
    Handling needed: none beyond execution; cited only as historical source-basis.
  successor: >
    orca/product/case_families/product_learning/other_verticals/core_spine_v0_heavyweight_proof_case_discovery_results_v0.md
    — the operative corpus that this charter authorized.
  semantic_delta: >
    The charter defines the authorization boundary, stop criteria, forbidden
    activities, and eligibility fields for the discovery pass. That content is
    absorbed into the results artifacts' source-basis declarations and
    boundary-actually-used sections. Unique content: the explicit forbidden-activity
    list and stop-criteria list. These are not referenced by any live product
    artifact. Loss is the pre-authorization governance record; fully recoverable
    from git. Rated low because the charter carries more unique boundary-setting
    content than the brief, and two live results artifacts cite it as their
    source-basis — a marginal active-citation case.
  rollback: git revert <executing merge sha>
```

confidence: low
rationale: superseded-by-results; boundary content absorbed; no live dependency; cited only as historical source-basis in the results artifacts themselves. Conservative keep is also defensible — charter + results form a natural governance pair.

---

### Candidate 3 (low confidence): `core_spine_v0_first_proof_packet_preparation_v0.md`

```yaml
targets:
  - orca/product/case_families/product_learning/other_verticals/core_spine_v0_first_proof_packet_preparation_v0.md
evidence:
  reverse_ref_check: >
    Grep of orca/product/, docs/, .agents/ for `first_proof_packet_preparation`:
    - docs/migration/spine_first_target_move_table_v0.md:246 — migration table
      (groups it with first-proof-run corpus as `direct_move`)
    - docs/migration/repo_structure_spine_first_v0/moved_paths_index.md:38 — migration provenance
    - docs/workflows/orca_repo_map_v0.md:587 — live repo map listing (no supersession note)
    - orca/product/case_families/product_learning/other_verticals/core_spine_v0_first_proof_run_charter_v0.md:22
      — charter names it in source-basis list at artifact creation time
    - orca/product/case_families/product_learning/other_verticals/core_spine_v0_heavyweight_proof_case_discovery_charter_v0.md:47
      — discovery charter names it in source-basis
    No live spine or product contract loads this as current authority.
    Handling needed: none; cited only as historical source-basis.
  successor: >
    orca/product/case_families/product_learning/other_verticals/core_spine_v0_first_proof_run_charter_v0.md
    — the charter supersedes the preparation artifact by providing the full
    authorized proof-run scope including all elements the preparation defined.
  semantic_delta: >
    The preparation artifact converts the proof-packet preflight into a bounded
    preparation structure and records a readiness checklist. The charter that
    followed it covers the same scope more fully (proof question, authorized work,
    allowed outputs, stop criteria, backtest lock sequence, result states). The
    preparation article's unique content is the "proof execution blockers" section
    and the preparation-state checklist — both are time-bound records of a gating
    step that has since passed (proof was executed and packet produced). Loss is
    the intermediate preparation state; recoverable from git.
    Rated low because the repo map still lists it without a supersession note,
    and the proof lifecycle flow (preparation -> charter -> execution -> packet)
    may be worth preserving as a documentation audit trail.
  rollback: git revert <executing merge sha>
```

confidence: low
rationale: superseded-by-charter; preparation-gate content is time-bound and absorbed by the charter; no live product authority dependency. Conservative keep is defensible — forms part of the proof lifecycle audit trail.

---

### Files verified as NOT deletion candidates

The following files were fully reviewed and rejected as deletion candidates; each carries active corpus value or live inbound dependencies:

**core_spine_v0_first_proof_run_packet_v0.md** — the synthesis and primary result of the first proof run; heavily cited in the repo map and referenced as the method-proof record; no successor absorbs it.

**core_spine_v0_first_proof_run_charter_v0.md** — the authorization instrument for the proof run; successor of the preparation artifact; cited in the discovery charter source-basis and repo map.

**core_spine_v0_first_proof_run_locks_v0.md** — pre-evidence lock record; cited in discovery charter and repo map; contains the shadow-satellite and backtest lock records needed for the proof audit trail.

**core_spine_v0_first_proof_run_jb_client0_slice_v0.md**, **…sh01_shadow_slice_v0.md**, **…bt204_backtest_slice_v0.md** — the three primary evidence corpora that feed the proof-run packet. The packet synthesized FROM them; it does not absorb them. The packet (line 17-19) explicitly lists them as its source basis. A synthesis does not make the primary corpora bloat: the packet cannot be independently verified without the slices.

**core_spine_v0_method_validation_case_locks_v0.md**, **…case_frame_lock_contract_v0.md**, **…case_frame_locks_v0.md** — the three-layer validation lock sequence (identity → contract → frame locks). Each layer is distinct; together they constitute the pre-replay discipline record for MV-01 through MV-09. No layer absorbs another.

**core_spine_v0_method_validation_mv01_…replay_v0.md** through **mv09_…replay_v0.md** (5 files) — the five individual case replay artifacts. The replay packet synthesizes their compact receipts; the full case artifacts remain the primary evidence and are independent audit records. The packet explicitly does NOT re-audit source ledgers from these files (replay_packet line 122).

**core_spine_v0_method_validation_replay_packet_v0.md** — cross-case packet synthesis from the five sealed receipts; the top-level summary; cited in the repo map as the entry point for the MV corpus.

**core_spine_v0_heavyweight_proof_case_discovery_results_v0.md** — operative discovery results (shadow candidates + backtest candidates); named in the repo map as the reference for current case selection; successor of the brief.

**core_spine_v0_heavyweight_proof_case_discovery_results_part_2_v0.md** — complementary backtest-candidate refresh pass; not a replacement of part_1 but an additive backtest-domain discovery artifact.

**core_spine_v0_proof_case_selection_brief_v0.md** — flagged as deletion candidate (medium, above).

**orca_backtest_specimen_unity_runtime_fee_source_packet_v0.md**, **…memo_unity_runtime_fee_at_cutoff_v0.md**, **…outcome_calibration_v0.md** — tight three-file backtest specimen family; the calibration cites the memo's SHA256; the memo cites the packet's SHA256. Cross-SHA integrity chain makes these indivisible; all three carry unique content at different lifecycle phases. Not bloat.

**consumer_demand_candidate_pool_handoff_v0.md** — dated one-shot beauty discovery handoff with a retrieval header declaring stale_if conditions; inbound ref check: cited in the migration table as pending an owner ruling (U-CF3: `case_families/fragrance` vs `satellites/beauty`). Not deletion-eligible; placement question only.

## B. Ontology / doc-term findings

**Clean.**

Systematic check against SSOT (`orca/product/spines/foundation/ontology/ontology.yaml`):

1. CamelCase distinctive tokens (>=2 humps, head noun in SSOT ontology head-noun set) were searched across all 24 files in `orca/product/case_families/`. No tokens matching the pattern `[A-Z][a-z]+(Vector|Caller|Packet|Unit|Event|Reading|Memo|Case)` appear in this corpus. The corpus uses Core Spine primitives as space-separated prose phrases (`Evidence Unit`, `Signal Integrity`, `Action Ceiling`, `Decision Frame`, etc.), which are explicitly excluded from the doc-term checker's CamelCase matching discipline.

2. SSOT canonical types (`TrendVector`, `WindCaller`, `CapturePacket`, `EvidenceUnit`, `DecisionEvent`, `TrendVector`, `Case`, `Outcome`, etc.) do not appear as CamelCase tokens in this corpus — they appear only as prose descriptions in the correct space-separated form.

3. No deprecated aliases, no non-SSOT coinages with ontology head-nouns, and no new-term candidates were found.

4. The `consumer_demand_candidate_pool_handoff_v0.md` uses `claim_tier` values (`product_learning`, `buyer_proof`, `judgment_quality`) consistently with the SSOT dimension definition (`ontology.yaml:123`).

**No ontology findings requiring action.**
