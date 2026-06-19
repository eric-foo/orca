```yaml
retrieval_header_version: 1
artifact_role: Orca migration note
scope: >
  Phase-2 W3a deletion + ontology proposal for the judgment spine area
  (orca/product/spines/judgment/, 25 files). Evidence-backed deletion
  candidates and ontology/doc-term findings for owner adjudication only.
  EXECUTE NOTHING from this artifact.
use_when:
  - Adjudicating judgment-area deletion candidates in the Phase-2 bloat-cut fan-out.
  - Reviewing ontology drift or new-term candidates in judgment spine documents.
authority_boundary: retrieval_only
open_next:
  - docs/migration/orca_second_pass_consolidation_plan_v0.md
stale_if:
  - The deletion register is updated with executed records for these targets, or the
    judgment spine files are renamed/superseded beyond what is described here.
```

# Phase-2 W3a Proposal — judgment

## Summary

- **Files scanned:** 25 (all files under `orca/product/spines/judgment/`)
- **Deletion candidates:** 0 high / 3 medium / 1 low
- **Ontology / doc-term findings:** 1 (NEW-TERM-CANDIDATE: `FailureEvent`)

---

## A. Deletion candidates

### Candidate 1

```yaml
- targets:
    - orca/product/spines/judgment/conductor/conductor_construction_integrity_probe_addendum_proposal_v0.md
  evidence:
    reverse_ref_check: >
      Inbound refs found:
        docs/migration/spine_first_untagged_file_inventory_v0.md:73 (inventory record)
        docs/migration/spine_first_target_move_table_v0.md:180 (inventory record)
        docs/migration/repo_structure_spine_first_v0/moved_paths_index.md:147 (inventory record)
        docs/hygiene/handoff_orgmotion_beautypie_r5_propagation_v0.md:104 (says "do not cite")
        docs/decisions/judgment_spine_backtest_batch1_ledger_declaration_v0.md:200 (historical DCP context)
        docs/review-outputs/adversarial-artifact-reviews/conductor_construction_integrity_probe_addendum_adversarial_review_v0.md
          (multiple lines — this review artifact targets v0 as its reviewed subject; deleting v0
          leaves the review artifact without a resolvable target; owner should decide whether the
          review artifact is also deleted or whether v0 is retained as review history)
      0 refs from orca/product/ (live doctrine) or .agents/.
      The migration inventory refs are historical. The handoff ref explicitly marks it "do not cite".
      The batch1 ledger ref is historical DCP context only.
      The adversarial review ref is the principal inbound dependency; see semantic_delta.
    successor: orca/product/spines/judgment/conductor/conductor_construction_integrity_probe_addendum_v1.md
    semantic_delta: >
      v0 contains the three original proposed rules (invocation expectation, outcome-blind
      construction, JSG-05 probe refinement) that were superseded by a NEEDS_ARCHITECTURE_PASS
      finding. v1 supersedes with a requirements-and-routed-out shape that resolved AR-01/02/03.
      The substantive content migrated to v1. What remains unique in v0 is the as-authored design
      that was found architecturally blocked — preserved in git and cited by the adversarial review
      artifact as its reviewed subject. Meaning preserved: all requirements and resolutions are in
      v1. Meaning lost on deletion: the review artifact's subject becomes unresolvable (though git
      history retains it); the blocked design rationale is git-recoverable but no longer browsable.
    rollback: >
      git revert <executing merge sha>  — or recover via:
      git show HEAD:orca/product/spines/judgment/conductor/conductor_construction_integrity_probe_addendum_proposal_v0.md
  confidence: medium
  rationale: >
    superseded-by-v1. v0 body self-declares "SUPERSEDED 2026-06-12 by the
    conductor_construction_integrity_probe_addendum_v1.md". v1 open_next cites it as
    "superseded; review history only". Principal inbound dependency is the adversarial review
    artifact (which itself may be deletable alongside v0; owner to adjudicate as a pair).
```

### Candidate 2

```yaml
- targets:
    - orca/product/spines/judgment/demand_read/c2_weighting/judgment_spine_c2_qualitative_read_feasibility_probe_v0.md
  evidence:
    reverse_ref_check: >
      Inbound refs found:
        orca/product/spines/judgment/demand_read/c2_weighting/judgment_spine_c2_qualitative_read_feasibility_probe_v1.md:18
          (open_next provenance pointer — "v0 probe + its graded-weak result (provenance)"; not live doctrine)
        docs/migration/repo_structure_spine_first_v0/moved_paths_index.md:160 (inventory record)
        docs/prompts/handoffs/judgment_spine_c2_read_contract_continuation_handoff_v0.md:123
          (historical handoff record)
      0 refs from orca/product/ live doctrine or .agents/.
      The v1 open_next ref is a provenance pointer only, not a dependency that blocks deletion.
    successor: orca/product/spines/judgment/demand_read/c2_weighting/judgment_spine_c2_qualitative_read_feasibility_probe_v1.md
    semantic_delta: >
      v0 contains the original Pair-alpha/beta feasibility probe with author-produced reads that a
      cross-vendor grader judged "F3 but probe_soundness: rigged_or_weak" (AR-01: cases too clean,
      AR-02: pre-registration not external, AR-03: bad reads were strawmen). The probe structure and
      grading rubric migrated to v1 with stronger cases. v0's unique content is the graded-weak
      provenance trail showing why v1 was needed. All active probe content is in v1 and v2.
      Meaning preserved: probe design, rubric, and failure-mode taxonomy are in v1/v2.
      Meaning lost on deletion: the graded-weak provenance trail is git-recoverable but no longer
      directly browsable.
    rollback: >
      git revert <executing merge sha>  — or recover via git show HEAD:<path>
  confidence: medium
  rationale: >
    superseded-by-v1. v1 body explicitly states it "supersedes v0 after a cross-vendor grading
    judged v0 weak". v1 open_next cites v0 as "the v0 probe + its graded-weak result (provenance)".
    v0 is retained only as provenance; no live doctrine depends on it.
```

### Candidate 3

```yaml
- targets:
    - orca/product/spines/judgment/demand_read/c2_weighting/judgment_spine_c2_qualitative_read_feasibility_probe_v1.md
  evidence:
    reverse_ref_check: >
      Inbound refs found:
        orca/product/spines/judgment/demand_read/c2_weighting/judgment_spine_c2_qualitative_read_feasibility_probe_v2.md:18
          (open_next provenance pointer — "v1 + its graded result (provenance)"; not live doctrine)
        docs/migration/repo_structure_spine_first_v0/moved_paths_index.md:161 (inventory record)
      0 refs from orca/product/ live doctrine or .agents/.
      The v2 open_next ref is a provenance pointer only.
    successor: orca/product/spines/judgment/demand_read/c2_weighting/judgment_spine_c2_qualitative_read_feasibility_probe_v2.md
    semantic_delta: >
      v1 contains the pre-registered Cases + Pairs alpha/beta/gamma + four failure modes
      (F1/F2/F4/F3) + external pre-registration structure. v2 supersedes with blind
      author-independent reads (AR-01 against v1: author-synchronized consistency test was
      "illusory"). v1's unique content is the graded result and the bad-read answer key inline that
      v2 moved to a hidden adjudication key. All active probe content is in v2.
      Meaning preserved: probe design and rubric are in v2. Meaning lost: the v1 graded result and
      inline answer key are git-recoverable but no longer directly browsable.
    rollback: >
      git revert <executing merge sha>  — or recover via git show HEAD:<path>
  confidence: medium
  rationale: >
    superseded-by-v2. v2 body states "v2 answers the two findings a cross-vendor (OpenAI GPT-5)
    grading raised against v1". v2 open_next cites v1 as "v1 + its graded result (provenance)".
    v1 is retained only as provenance; no live doctrine depends on it.
```

### Candidate 4

```yaml
- targets:
    - orca/product/spines/judgment/demand_read/c2_weighting/judgment_spine_c2_rule3_reground_phase_a_classification_finding_v0.md
  evidence:
    reverse_ref_check: >
      Inbound refs found:
        docs/migration/spine_first_target_move_table_v0.md:190 (inventory record)
        docs/migration/search_demand_signal_migration_inventory_v0.md:117 (inventory record)
        docs/migration/repo_structure_spine_first_v0/moved_paths_index.md:163 (inventory record)
        docs/migration/repo_structure_search_lane_v0/reference_inventory.md:38 (inventory record)
      0 refs from orca/product/ live doctrine or .agents/.
      All refs are migration inventory records only; none are live doctrine consumption.
    successor: orca/product/spines/judgment/demand_read/c2_weighting/judgment_spine_c2_ledger_read_contract_v0.md
    semantic_delta: >
      This finding's sole purpose was to recommend that Rule 3 from the sender artifact be
      classified as PATCH and folded into c2_ledger_read_contract_v0.md. That fold was executed:
      c2_ledger_read_contract_v0.md DCP (2026-06-15) records "Rule 3 — Risk-State Weighting Across
      Evidentiary States (folded 2026-06-15)". The two-axis re-grounding rationale (which mechanism
      classes are C2 caps vs C3 transient verdicts) migrated into the c2 contract.
      What remains unique in this finding: the cross-lane drift signal about the c3 architecture
      stale "hollow" reference (noted as out-of-scope to edit in the finding itself), and the
      Phase A provenance trail.
      Meaning preserved: the Rule 3 fold outcome is in c2_ledger_read_contract_v0.md.
      Meaning lost: the two-axis re-grounding design rationale is git-recoverable but no longer
      directly browsable; the out-of-scope c3 drift signal is not captured elsewhere.
    rollback: >
      git revert <executing merge sha>  — or recover via git show HEAD:<path>
  confidence: low
  rationale: >
    obsolete — its sole purpose was to recommend the Rule 3 fold; that fold was executed
    2026-06-15 per the DCP in c2_ledger_read_contract_v0.md. However, the two-axis
    re-grounding design rationale retained in this finding has provenance value, and the
    c3 drift signal was never resolved. Conservative; owner adjudication required.
```

---

## B. Ontology / doc-term findings

### Finding 1 — NEW-TERM-CANDIDATE: `FailureEvent`

- **Term:** `FailureEvent`
- **Classification:** NEW-TERM-CANDIDATE per `check_doc_terms.py` logic (>=2 CamelCase humps; head noun `Event` IS an ontology head noun, inherited from `DecisionEvent`)
- **Not in SSOT:** neither in canonical types nor in runtime aliases (`ontology.yaml`)
- **Locations:**
  - `orca/product/spines/judgment/conductor/judgment_spine_gate_ownership_map_v0.md:131`
  - `orca/product/spines/judgment/conductor/judgment_spine_gate_ownership_map_v0.md:312`
  - `orca/product/spines/judgment/conductor/judgment_quality_promotion_operating_model_v0.md:215` (and nearby occurrences in the same file)
- **Context:** Refers to `orca-harness/schemas/scoring_models.py:FailureEvent` — a scoring/harness runtime class used within JSG-07 gate descriptions. It is not an ontology domain type and does not belong to the `decision:` namespace.
- **Proposed read-only fix (owner adjudication):** At first occurrence in each file, add a clarifying inline parenthetical — e.g., `FailureEvent (harness runtime class: scoring_models.py; not an ontology DecisionEvent-namespace type)` — to distinguish it from the ontology `Event` head-noun family. No rename is needed; the term correctly names the harness concept. Owner to decide whether to register it as a non-ontology alias in the SSOT or to annotate in place.
