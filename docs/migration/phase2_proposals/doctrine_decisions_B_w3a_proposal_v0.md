---
retrieval_header_version: 1
artifact_role: Orca migration note
scope: >
  Phase-2 W3a deletion + ontology proposal for the B-half of docs/decisions/*.md
  (45 files, sorted alphabetically: ground_truth_check_before_absence_or_build_state_claims_v0.md
  through work_unit_fitness_reference_v0.md). Read-only scan; proposes for owner
  adjudication only. Executes nothing.
use_when:
  - Owner adjudicating Phase-2 deletion candidates in the docs/decisions/ B-half.
  - Running the ontology / doc-term pass over this file set.
authority_boundary: retrieval_only
open_next:
  - docs/migration/orca_second_pass_consolidation_plan_v0.md
stale_if:
  - Any proposed deletion is executed (register entry required + ungated human-review-only).
  - Ontology SSOT (ontology.yaml) changes (re-run the term scan).
---

# Phase-2 W3a Proposal — doctrine (docs/decisions B-half)

## Summary

**Files scanned:** 45 (the alphabetical second half of docs/decisions/*.md, indices 44–88 of 89 total)
**File range:** `ground_truth_check_before_absence_or_build_state_claims_v0.md` .. `work_unit_fitness_reference_v0.md`
**Scan date:** 2026-06-19
**Subagent:** doctrine/decisions-B (this file)

UNGATED REMINDER: every deletion candidate below is tagged **ungated: human-review-only at execute**.
docs/decisions/ is outside GOVERNED_ROOTS (`orca/product/`), so the deletion-evidence gate
(check_deletion_evidence.py) does NOT enforce it in CI. Any deletion here requires owner manual
review and a deletion-evidence register entry as a governance record. The governance audit trail
lives in these records; be extra conservative.

---

## A. Deletion candidates

### Candidate 1

```yaml
targets:
  - docs/decisions/turn_07_branch_casing.md
ungated: human-review-only at execute
evidence:
  reverse_ref_check: >
    grep -r "turn_07_branch_casing" (full repo): 0 inbound references found
    anywhere in the repo (docs/, .agents/, orca/, workflows, prompts, migration).
    orca_doctrine_index_v0.md does NOT list it. Safe to remove.
  successor: "none -- pure bloat"
  semantic_delta: >
    Records a single 2026-05-13 branch-casing decision (Main -> main) from
    before any commits. This is a bootstrap artifact that predates the decision
    framework; the branch has been named 'main' for months; the decision carries
    no forward-operating rule and is not referenced anywhere. Zero semantic loss
    on deletion — the fact is visible in git history itself.
  rollback: "git revert <executing merge sha>"
confidence: high
rationale: archived-receipt (bootstrap-era receipt, zero inbound refs, no forward rule)
```

### Candidate 2

```yaml
targets:
  - docs/decisions/orca_icp_wedge_convergence_break_in_first_v0.md
ungated: human-review-only at execute
evidence:
  reverse_ref_check: >
    grep -r "orca_icp_wedge_convergence_break_in_first_v0" (full repo): 9 inbound
    files found:
      docs/research/orgmotion_demand_signal_wedge_discovery_v0.md
      docs/research/orca_icp_redo_evidence_targets_v0.md
      docs/research/orca_wedge_alternatives_register_v0.md
      docs/prompts/product-planning/orca_break_in_verification_evidence_prompt_v0.md
      docs/migration/repo_structure_phase2_consolidation_v0/reference_inventory.md
      docs/hygiene/checkpoint_icp_convergence_lock.md
      docs/decisions/orca_icp_wedge_pricing_first_v0.md
      docs/decisions/orca_icp_wedge_consumer_demand_first_v0.md
      .agents/workflow-overlay/artifact-folders.md
    These refs are non-trivial: two active decision records (pricing_first, consumer_demand_first)
    reference it explicitly as a supersession anchor. Not safe to delete while these refs stand
    (resolving them is a separate human-adjudicated cascade, not handled here).
  successor: docs/decisions/orca_icp_wedge_pricing_first_v0.md (explicit superseder recorded in the file)
  semantic_delta: >
    The file is SUPERSEDED (2026-06-08) and carries a prominent banner. Its content
    is historical: the break-in-first direction that was reversed. It is referenced
    as a provenance anchor by two live decisions; semantic history would be lost for
    those refs if deleted without updating them first.
  rollback: "git revert <executing merge sha>"
confidence: low
rationale: >
  Superseded (archived-receipt) status favors eventual deletion, but 9 inbound refs
  including two live decision records prevent safe deletion now. DO NOT PROPOSE as
  a near-term delete. Flag for a future ref-cleanup pass only.
```

**Verdict on Candidate 2:** WITHDRAW from near-term deletion. Too many live inbound refs.
Retaining below as a low-confidence candidate for a future ref-cleanup pass only, not for
this Phase-2 execute wave.

### Candidate 3

```yaml
targets:
  - docs/decisions/turn_08_product_thesis_v0.md
ungated: human-review-only at execute
evidence:
  reverse_ref_check: >
    grep -r "turn_08_product_thesis_v0" (full repo): 49 inbound files found across
    docs/decisions/, orca/product/, docs/prompts/, docs/review-outputs/, docs/workflows/,
    .agents/workflow-overlay/. Includes:
      docs/decisions/orca_product_thesis_consumer_demand_v0.md (open_next + supersedes cite)
      docs/decisions/orca_icp_wedge_convergence_break_in_first_v0.md
      docs/decisions/orca_icp_wedge_consumer_demand_first_v0.md
      docs/decisions/wind_caller_calibration_carveout_v0.md
      .agents/workflow-overlay/project-authority.md
      .agents/workflow-overlay/artifact-roles.md
      plus 43 more files.
    Not safe to delete; still widely referenced as the v0 historical baseline.
  successor: docs/decisions/orca_product_thesis_consumer_demand_v0.md
  semantic_delta: >
    The file carries SUPERSEDED status and a clear banner; the controlling thesis is
    v1 (orca_product_thesis_consumer_demand_v0.md). However with 49 inbound refs
    including .agents/ overlay files, deletion would create widespread link rot.
  rollback: "git revert <executing merge sha>"
confidence: low
rationale: >
  Superseded (archived-receipt) status favors eventual deletion, but 49 inbound refs
  (including overlay-authority files) prevent safe deletion without a ref-cleanup pass.
  Do NOT propose for this execute wave. Future pass only.
```

**Verdict on Candidate 3:** WITHDRAW from near-term deletion. 49 inbound refs; unsafe without a prior ref-cleanup pass.

### Candidate 4 — orca_icp_wedge_pricing_first_v0.md

```yaml
targets:
  - docs/decisions/orca_icp_wedge_pricing_first_v0.md
ungated: human-review-only at execute
evidence:
  reverse_ref_check: >
    grep -r "orca_icp_wedge_pricing_first_v0" (full repo): 22 inbound files found
    including orca/product/ spines, docs/prompts/, docs/review-outputs/, and other
    docs/decisions/ files. Explicitly open_next'd by orca_icp_wedge_consumer_demand_first_v0.md
    and cited as a historical wedge chain anchor.
  successor: docs/decisions/orca_icp_wedge_consumer_demand_first_v0.md (explicit superseded_by field)
  semantic_delta: >
    SUPERSEDED (2026-06-12) with a prominent banner and an explicit superseded_by
    field. Retains historical method anchors (two RETRO SaaS dev cases). However
    22 inbound refs span active product spines and decision chain records that still
    open_next it as a chain anchor.
  rollback: "git revert <executing merge sha>"
confidence: low
rationale: >
  Superseded (archived-receipt). 22 inbound refs prevent safe deletion without a
  ref-cleanup pass. WITHDRAW from near-term deletion.
```

**Verdict on Candidate 4:** WITHDRAW from near-term deletion.

### Candidate 5 — orca_moat_judgment_quality_proof_path_decision_chain_v0.md

```yaml
targets:
  - docs/decisions/orca_moat_judgment_quality_proof_path_decision_chain_v0.md
ungated: human-review-only at execute
evidence:
  reverse_ref_check: >
    grep -r "orca_moat_judgment_quality_proof_path" (full repo): 4 inbound files found:
      orca/product/spines/foundation/vertical_exploration/orca_memorization_resistant_case_finder_frame_v0.md
      docs/research/judgment-spine/decide_vs_confirm_backtest_case_frame_template_v0.md
      docs/research/judgment-spine/decide_vs_confirm_case_discovery_results_v0.md
      docs/migration/repo_structure_phase2_consolidation_v0/reference_inventory.md
    Not listed in orca_doctrine_index_v0.md. No .agents/ references.
  successor: "none -- pure bloat"
  semantic_delta: >
    Status is "DECISION_CHAIN_CAPTURED_PENDING_OWNER_SIGNOFF" — explicitly a pending
    decision-prep artifact, not a locked/adopted record. Its own stale_if says it
    should be superseded when the chain is promoted into controlling product/harness
    sources. Has 4 inbound refs from research files and a migration inventory;
    those are primarily provenance reads, not authority links.
  rollback: "git revert <executing merge sha>"
confidence: low
rationale: >
  Status is PENDING_OWNER_SIGNOFF — not yet adopted or locked. This raises the
  question of whether it is stale-pending or still a live decision under development.
  With 4 inbound refs including research files that may depend on it as a sequencing
  anchor, and no clear adoption/rejection outcome recorded, this is borderline.
  CONSERVATIVE CALL: do not propose for deletion. The pending status without explicit
  rejection means the governance record may still be load-bearing; only the owner
  can determine if this was silently superseded by subsequent work. Flag for owner
  review only.
```

**Verdict on Candidate 5:** NO PROPOSAL — pending status + 4 inbound refs; owner-only determination.

### Candidate 6 — orca_consumer_demand_ratification_decision_memo_v0.md

```yaml
targets:
  - docs/decisions/orca_consumer_demand_ratification_decision_memo_v0.md
ungated: human-review-only at execute
evidence:
  reverse_ref_check: >
    grep -r "orca_consumer_demand_ratification_decision_memo" (full repo): 5 inbound files found:
      orca/product/spines/product_lead/icp_wedge/orca_icp_ratification_readiness_report_v0.md
      orca/product/spines/product_lead/icp_wedge/orca_ratification_day_runbook_v0.md
      docs/prompts/product-planning/consumer_demand_probe_stage1_feasibility_commission_prompt_v0.md
      docs/migration/search_demand_signal_migration_inventory_v0.md
      docs/decisions/orca_product_thesis_consumer_demand_v0.md (open_next cite)
  successor: >
    docs/decisions/orca_product_thesis_consumer_demand_v0.md — the thesis record
    records the owner's decisions from this memo inline and supersedes it as the
    live state; the memo itself says "DECIDED_2026-06-12" and its stale_if fired.
  semantic_delta: >
    Status "DECIDED_2026-06-12" means the memo is consumed. The thesis record
    contains the owner's verbatim words and all decision outcomes. However the 5
    inbound refs include active product-lead spine docs and a runbook that
    open_next it; those refs would break on deletion.
  rollback: "git revert <executing merge sha>"
confidence: low
rationale: >
  Consumed decision memo (archived-receipt). With 5 inbound refs including product
  spines, not safe to delete without a ref-cleanup. WITHDRAW from near-term deletion.
```

**Verdict on Candidate 6:** WITHDRAW from near-term deletion.

### Summary of A-section findings

The only HIGH-CONFIDENCE candidate without inbound refs is:

| File | Confidence | Action |
|---|---|---|
| `turn_07_branch_casing.md` | HIGH | PROPOSE for deletion (0 inbound refs, bootstrap-only receipt) |
| `orca_icp_wedge_convergence_break_in_first_v0.md` | LOW | WITHDRAW — 9 inbound refs |
| `turn_08_product_thesis_v0.md` | LOW | WITHDRAW — 49 inbound refs |
| `orca_icp_wedge_pricing_first_v0.md` | LOW | WITHDRAW — 22 inbound refs |
| `orca_moat_judgment_quality_proof_path_decision_chain_v0.md` | LOW | OWNER-ONLY — pending status |
| `orca_consumer_demand_ratification_decision_memo_v0.md` | LOW | WITHDRAW — 5 inbound refs |

All other files scanned: active, adopted, locked, or load-bearing records with no
clear supersession or duplication. Not proposed. The conservative stance is correct
for the governance audit trail.

### Formal deletion record for the one high-confidence candidate

```yaml
- targets: ["docs/decisions/turn_07_branch_casing.md"]
  ungated: human-review-only at execute
  evidence:
    reverse_ref_check: >
      Full-repo grep for "turn_07_branch_casing": 0 inbound references found in
      docs/, .agents/, orca/, docs/decisions/orca_doctrine_index_v0.md (not listed).
      Safe to remove — no downstream consumer.
    successor: "none -- pure bloat"
    semantic_delta: >
      Records a 2026-05-13 branch rename (Main -> main) before any commits.
      The branch has been 'main' for months; the decision has no forward-operating
      rule and is purely a bootstrap receipt. Zero semantic loss: git history records
      the rename authoritatively; this file adds nothing retrievable.
    rollback: "git revert <executing merge sha>"
```

---

## B. Ontology / doc-term findings

Scan scope: the 45 B-half docs/decisions/ files vs the SSOT
(`orca/product/spines/foundation/ontology/ontology.yaml`).

check_doc_terms.py scope is `orca/product/` (corpus only); docs/decisions/ is
outside that scope by design (these are decision records, not product corpus docs).
The ontology SSOT's `check_doc_terms.py` does not lint docs/decisions/ files.
Accordingly this section is a manual scan of CamelCase type-shaped vocabulary
appearing in the B-half files against the SSOT.

### SSOT canonical types (for reference)

From ontology.yaml `types` roster:
`Vertical`, `Brand`, `Product`, `Venue`, `WindCaller`, `Call`, `Observation`,
`TrendVector`, `DecisionEvent`, `Reading`, `Memo`, `Case`, `Outcome`,
`CapturePacket`, `EvidenceUnit`, `Buyer`, `Org`

Runtime aliases: `SourceCapturePacket` (-> CapturePacket), `FacilitatorLedger` (-> Case),
`CaseReport` (-> Case)

### Findings

**1. `SourceCapturePacket` — correct SSOT alias**

- Files: `judgment_spine_backtest_batch1_ledger_declaration_v0.md` (line ~169)
- Usage: "-> `SourceCapturePacket`" in the Amendment section
- Classification: KNOWN — runtime alias for CapturePacket, per ontology.yaml `runtime_bindings`
- Proposed fix: none (correct usage)

**2. `FacilitatorLedger` — correct SSOT alias**

- Files: `judgment_spine_backtest_batch2_band_ratification_v0.md` (table of freeze hashes)
- Usage: references to facilitator_ledger.yaml and `ledger_authors.second_labeler`
- Classification: KNOWN — runtime alias for Case, per ontology.yaml `runtime_bindings`
- Proposed fix: none (correct usage)

**3. `DecisionEvent` — correct SSOT canonical type**

- Files: `ontology_runtime_drift_check_contract_v0.md` references ontology.yaml types
- Classification: KNOWN
- Proposed fix: none

**4. `WindCaller` — correct SSOT canonical type**

- Files: `ingestible_beauty_screen1_ledger_v0.md`, `orca_icp_wedge_consumer_demand_first_v0.md`
- Usage: used in prose to describe "wind-caller" pattern; `WindCaller` as a type name in
  `ingestible_beauty_screen1_ledger_v0.md` ("REGULATOR-AS-WIND-CALLER", "RETAIL-GATEKEEPER-AS-VALIDATOR")
  — these are prose descriptions of NEW wind-caller subtypes, not SSOT type violations
- Classification: KNOWN (canonical type in prose context); the subtypes are role descriptions,
  not new type coinages
- Proposed fix: none

**5. `TrendVector` — correct SSOT canonical type**

- Files: `orca_icp_wedge_consumer_demand_first_v0.md`
- Classification: KNOWN
- Proposed fix: none

**6. New-term-candidate scan: NO non-SSOT ontology-shaped CamelCase coinages found**

Full-repo grep over the 45 B-half files for CamelCase patterns with ontology
head-nouns {Caller, Event, Packet, Unit, Vector} that are NOT in the SSOT:

- `DemandVector`, `SignalPacket`, `DemandPacket`, `TrendCaller`, `ObservationUnit`,
  `CaptureUnit`, `DemandUnit`, `CaptureVector`: 0 matches found across all 45 files.
- No new-term-candidates detected.

**7. Deprecated / aliased term check**

No deprecated or aliased terms found in the B-half decision files. The SSOT has no
`deprecated` field entries; `Buyer` and `Org` are `reserved` (not deprecated).
Their use in B-half files is in ontology-referencing contexts only, consistent with SSOT.

**8. Flag: "MGT name-drift decision 2026-06-19" citation in ontology.yaml**

The file `ontology_runtime_drift_check_contract_v0.md` (line ~183) records a governance
flag: "ontology.yaml's runtime_bindings comment cites an 'MGT name-drift decision
2026-06-19' that the review could not locate — a possible dangling citation to reconcile
separately." This is NOT a doc-term finding but a governance citation gap. The comment
in ontology.yaml at the CapturePacket `name_alias` entry reads:
"MGT name-drift decision 2026-06-19". Cross-referencing all B-half decision files:
no file titled "MGT name-drift decision" or containing that exact phrase was found.
This appears to be a forward-reference to `orca_repo_map_architecture_mgt_v0.md` (which
does record an owner-invoked MGT decision 2026-06-19) — but that record is about the
repo-map architecture, not about the CapturePacket name alias.

**Proposed read-only fix for flag:** Add a note to the consolidation plan that the
ontology.yaml `CapturePacket.name_alias` comment "MGT name-drift decision 2026-06-19"
should be reconciled against its source authority. If the intended source is
`orca_repo_map_architecture_mgt_v0.md`, the citation needs a path anchor. If the
intended source is a separate name-drift decision that does not yet exist, that
record should be authored or the comment should be updated to cite the existing
authority (e.g., this drift-check contract itself).

**Scope note:** This fix is a comment clarification in ontology.yaml, not a docs/decisions/
edit. The B-half subagent is read-only on everything except the proposal artifact.

### B-section verdict

**Ontology / doc-term findings: 1 governance citation gap flagged (non-blocking); all
type-name usages in the B-half files are either SSOT-canonical, SSOT-alias, or correct
prose-description usage. No non-SSOT coinages found. No deprecated terms found.**
