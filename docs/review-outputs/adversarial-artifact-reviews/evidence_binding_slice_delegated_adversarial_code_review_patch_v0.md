```yaml
retrieval_header_version: 1
artifact_role: delegated adversarial code review-and-patch report
authority_boundary: retrieval_only
reviewed_by: openai/gpt-5-codex
authored_by: anthropic/claude-fable-5
controller_model_family: OpenAI
author_home_model_family: Anthropic
de_correlation_bar: cross_vendor_discovery
commission: evidence_binding/ slice B build, ECR JSG-01 unfreeze
target_files:
  - orca-harness/evidence_binding/__init__.py
  - orca-harness/evidence_binding/models.py
  - orca-harness/evidence_binding/composer.py
  - orca-harness/tests/unit/test_evidence_binding.py
output_mode: review-report + working-tree patch + chat courier
```

```yaml
review_summary:
  strict_claim_boundary: decision_input_only_not_acceptance_or_readiness
  preflight:
    target_hash_pins: mismatch_observed_then_owner_authorized_current_live_baseline
    branch_observed: ecr-sp3-timing-deriver-slice1
    head_observed_before_patch: c3ff536
  source_context_ready: true
  critical_findings: 0
  major_findings: 2
  minor_findings: 0
  patch_status: applied_to_working_tree_only
  validation:
    red_check: "tests/unit/test_evidence_binding.py failed before model patch: 15 passed, 2 failed"
    focused_post_patch: "17 passed"
    full_post_patch: "712 passed, 1 skipped"
  verdict: patch_applied_for_home_model_adjudication
```

## Preflight

The original commission hash pins did not match two live target files. I stopped, reported `BLOCKED_PREFLIGHT_HASH_MISMATCH`, and then proceeded only after owner authorization in chat. The current live files were copied to `_scratch/delegated_review_evidence_binding/originals/` before patching and are the baseline for the diffs below.

Pre-patch hashes after owner authorization:

```text
8000EEDFFCF4E3EDABEC02DC30824FAAF94CC47313D0E6AFCA99FDB6706FA9AA  _scratch/delegated_review_evidence_binding/originals/__init__.py
6D8DAEC7438D4C3B80968F9B4606EB1A80F3A78E748434C5F632F18425783726  _scratch/delegated_review_evidence_binding/originals/models.py
CA3F428591DB63A9C54D2E348CF7CE2A4335BA010BD12C6A7655D0F1F6EFF3A0  _scratch/delegated_review_evidence_binding/originals/composer.py
7F4CB52577675A0B4ED2AFA63D6D8F96F027F8FB8988D159DDED59629BABA849  _scratch/delegated_review_evidence_binding/originals/test_evidence_binding.py
```

Post-patch hashes:

```text
8000EEDFFCF4E3EDABEC02DC30824FAAF94CC47313D0E6AFCA99FDB6706FA9AA  orca-harness/evidence_binding/__init__.py
02BE07BF9CB90E3F7227CF9D4EC0C8B4BA1BFB6037A5E039FE59E44A41BC7D90  orca-harness/evidence_binding/models.py
CA3F428591DB63A9C54D2E348CF7CE2A4335BA010BD12C6A7655D0F1F6EFF3A0  orca-harness/evidence_binding/composer.py
B11DBE84A4F74FEBE9A45860268907B80F34CD2C633F887126ABB0743284721B  orca-harness/tests/unit/test_evidence_binding.py
```

## Source Context

Source pack loaded: the four target files; `docs/product/ecr/ecr_consolidation_v0_jsg01_evidence_unit_binding_slice_plan_v0.md`; the JSG-01 ratification and reserved list in `docs/product/core_spine/core_spine_v0_data_and_cleaning_spine_boundary_v0.md`; `orca-harness/ecr/deriver.py`; `orca-harness/ecr/models.py`; `orca-harness/schemas/finalization_models.py`; `orca-harness/tests/unit/_ecr_builders.py`; `orca-harness/tests/unit/test_ecr_source_side_composition.py`; `orca-harness/source_capture/models.py`.

Material contract anchors:

- The slice plan binds "five reads and no more" at `docs/product/ecr/ecr_consolidation_v0_jsg01_evidence_unit_binding_slice_plan_v0.md:61` and says anything beyond those reads routes to owner memo at `:72`.
- The binding is three durable keys only, with no posture, receipt, content, or derived value stored on the binding at `docs/product/ecr/ecr_consolidation_v0_jsg01_evidence_unit_binding_slice_plan_v0.md:80-90`.
- The composer must carry full SP-2/SP-3 vectors with bound-row selection by exact key, not sibling promotion, at `docs/product/ecr/ecr_consolidation_v0_jsg01_evidence_unit_binding_slice_plan_v0.md:119-126`.
- The finalization read must carry the validate-only consumer verdict verbatim, including BLOCKED as a named state, at `docs/product/ecr/ecr_consolidation_v0_jsg01_evidence_unit_binding_slice_plan_v0.md:126-132`.
- The record must compute no aggregate verdict at `docs/product/ecr/ecr_consolidation_v0_jsg01_evidence_unit_binding_slice_plan_v0.md:135-140` and the ratification repeats "no aggregate verdict" at `docs/product/core_spine/core_spine_v0_data_and_cleaning_spine_boundary_v0.md:326-330`.
- Reserved surfaces remain full ECR/Evidence Unit architecture, canonical object name, D2/corroborated tier, SP-4 value policing, conductor edit, and JSG-01 unfreeze at `docs/product/core_spine/core_spine_v0_data_and_cleaning_spine_boundary_v0.md:346-349`.

## Findings

### MAJOR EB-01 - Duplicate non-bound slice rows could pass `Jsg01EvidenceRecord` validation

Location: `orca-harness/evidence_binding/models.py`, `Jsg01EvidenceRecord.validate_key_coherence`.

Issue: The live baseline required timing and inspectability vectors to align by `slice_id` and required the bound `evidence_slice_id` to appear exactly once, but did not reject duplicate non-bound `slice_id` rows. A crafted record could carry two rows for the same sibling slice while still passing alignment and bound-row checks.

Evidence: The added red test mutated both vectors so the third row duplicated `s_placeholder` while the bound row `s_clean` still appeared exactly once. Before the model patch, `tests/unit/test_evidence_binding.py` failed because this did not raise a `ValidationError`.

Impact: This weakens the "full per-slice vector" audit surface. A duplicate non-bound row can make the carried vector no longer represent one coherent row per slice, undercutting the no-hide/no-laundering guarantee even when the bound row itself is selected by exact key.

Minimum closure condition: `Jsg01EvidenceRecord` rejects duplicate carried `slice_id` rows after timing/inspectability alignment and before bound-row accessors are trusted.

Next authorized action: Keep or adjudicate the applied model validator and regression test; no architecture pass required.

### MAJOR EB-02 - Cleared finalization reads could carry a blank receipt id

Location: `orca-harness/evidence_binding/models.py`, `Jsg01FinalizationRead.validate_read`.

Issue: A manually constructed `Jsg01FinalizationRead` with `result=CLEARED`, a final status, and `current_receipt_id="   "` passed validation. The consumer's `FinalizationReceipt` model rejects blank receipt ids, but the binding model is also a public record type and must not allow a hand-built cleared read to smuggle an incoherent "surfaced" receipt id.

Evidence: The added red test constructed a cleared read with a whitespace receipt id. Before the model patch, `tests/unit/test_evidence_binding.py` failed because this did not raise a `ValidationError`.

Impact: This is a verbatim-carry honesty gap. A cleared read with a blank `current_receipt_id` claims provenance was carried while losing the receipt identity needed to audit the current finalization act.

Minimum closure condition: `Jsg01FinalizationRead` requires `current_receipt_id.strip()` on CLEARED reads while preserving the existing BLOCKED-with-no-values rule.

Next authorized action: Keep or adjudicate the applied model validator and regression test; no architecture pass required.

## Patch

Only `models.py` and `test_evidence_binding.py` changed after the owner-authorized baseline. `__init__.py` and `composer.py` hashes are unchanged.

```diff
diff --git "a/_scratch\\delegated_review_evidence_binding\\originals\\models.py" "b/orca-harness\\evidence_binding\\models.py"
index f252c42..52a916e 100644
--- "a/_scratch\\delegated_review_evidence_binding\\originals\\models.py"
+++ "b/orca-harness\\evidence_binding\\models.py"
@@ -89,6 +89,10 @@ class Jsg01FinalizationRead(StrictModel):
                 "a CLEARED finalization read must carry the consumer-surfaced "
                 "final_pre_decision_status and current_receipt_id"
             )
+        if cleared and not self.current_receipt_id.strip():
+            raise ValueError(
+                "a CLEARED finalization read current_receipt_id must be non-empty"
+            )
         if not cleared and has_value:
             raise ValueError(
                 "a BLOCKED finalization read must carry no final status or "
@@ -142,6 +146,11 @@ class Jsg01EvidenceRecord(StrictModel):
                 "timing and inspectability vectors must align 1:1 by slice_id "
                 f"and order; got {timing_ids} vs {inspect_ids}"
             )
+        if len(set(timing_ids)) != len(timing_ids):
+            raise ValueError(
+                "timing and inspectability vectors must not contain duplicate "
+                f"slice_id rows; got {timing_ids}"
+            )
         if timing_ids.count(self.evidence_slice_id) != 1:
             raise ValueError(
                 f"evidence_slice_id {self.evidence_slice_id!r} must match exactly "
```

```diff
diff --git "a/_scratch\\delegated_review_evidence_binding\\originals\\test_evidence_binding.py" "b/orca-harness\\tests\\unit\\test_evidence_binding.py"
index c2a8ad4..c04ee3d 100644
--- "a/_scratch\\delegated_review_evidence_binding\\originals\\test_evidence_binding.py"
+++ "b/orca-harness\\tests\\unit\\test_evidence_binding.py"
@@ -227,6 +227,13 @@ def test_finalization_read_populated_only_on_cleared():
             result=FinalizationProvenanceResult.CLEARED,
             reason="cleared without the surfaced values",
         )
+    with pytest.raises(ValidationError, match="current_receipt_id must be non-empty"):
+        Jsg01FinalizationRead(
+            result=FinalizationProvenanceResult.CLEARED,
+            reason="cleared with a blank receipt id",
+            final_pre_decision_status=PreDecisionStatus.VERIFIED_PRE_DECISION,
+            current_receipt_id="   ",
+        )
 
 
 def test_blank_binding_keys_rejected():
@@ -249,6 +256,12 @@ def test_record_key_coherence_validators_reject_mismatches():
     with pytest.raises(ValidationError, match="exactly one carried slice row"):
         Jsg01EvidenceRecord.model_validate(unbound)
 
+    duplicate_non_bound = record.model_dump()
+    duplicate_non_bound["timing"][2]["slice_id"] = "s_placeholder"
+    duplicate_non_bound["inspectability"][2]["slice_id"] = "s_placeholder"
+    with pytest.raises(ValidationError, match="must not contain duplicate slice_id"):
+        Jsg01EvidenceRecord.model_validate(duplicate_non_bound)
+
 
 def test_single_slice_packet_composes():
     packet = build_packet(
```

Per-change citations:

- The duplicate-slice validator closes EB-01 against the full-vector/no sibling-promotion contract at `docs/product/ecr/ecr_consolidation_v0_jsg01_evidence_unit_binding_slice_plan_v0.md:119-126` and the ratified no-hide language at `docs/product/core_spine/core_spine_v0_data_and_cleaning_spine_boundary_v0.md:326-330`.
- The blank receipt-id validator closes EB-02 against the verbatim finalization-carry contract at `docs/product/ecr/ecr_consolidation_v0_jsg01_evidence_unit_binding_slice_plan_v0.md:126-132` and the consumer's populated-only-on-CLEARED semantics in `orca-harness/schemas/finalization_models.py`.
- The tests are regression proofs for the two validator gaps and stay inside the commissioned test target.

## Validation

Red check before model patch:

```text
.venv\Scripts\python.exe -m pytest -q tests\unit\test_evidence_binding.py
15 passed, 2 failed
Failures:
- test_finalization_read_populated_only_on_cleared did not raise ValidationError
- test_record_key_coherence_validators_reject_mismatches did not raise ValidationError
```

Focused post-patch check:

```text
.venv\Scripts\python.exe -m pytest -q tests\unit\test_evidence_binding.py
17 passed
```

Required full post-patch gate:

```text
.venv\Scripts\python.exe -m pytest
712 passed, 1 skipped in 88.56s (0:01:28)
```

## Verdict

`patch_applied_for_home_model_adjudication`.

No critical finding, no `NEEDS_ARCHITECTURE_PASS`, and no off-scope code edits. The patch closes two validator-soundness gaps inside the commissioned scope. This report and diff are decision input only; they are not approval, readiness, JSG-01 unfreeze, or a lifecycle keep claim.

## Residual Risk

- `model_construct` or post-validation object mutation can still bypass Pydantic validators; this is a general Pydantic escape hatch, not a binding-specific public validation path.
- The first preflight hash pins did not match the live files. Owner authorization allowed proceeding from the current live baseline, but home-model adjudication should account for that drift explicitly.
- The patch does not add SP-4 value policing, D2/corroborated-tier logic, conductor edits, canonical object naming, or full ECR/Evidence Unit architecture; those remain reserved by contract.

## Off-Scope Flags

- Initial hash pin mismatch was observed and waived by owner authorization; it was not silently treated as a passing preflight.
- `orca-harness/ecr/`, `orca-harness/schemas/`, `orca-harness/source_capture/`, and product/contract docs were read-only and unchanged.
- No sealed outcome facilitator artifact was opened.
- No staging, commit, or push was performed.

## Courier

```yaml
DELEGATED_CODE_REVIEW_RETURN_FOR_HOME_MODEL:
  commission: "evidence_binding/ slice B build, ECR JSG-01 unfreeze"
  reviewed_by: "openai/gpt-5-codex"
  authored_by: "anthropic/claude-fable-5"
  de_correlation_bar: "cross_vendor_discovery"
  preflight_note: "original target hash pins mismatched for models.py and test_evidence_binding.py; owner authorized proceeding from current live baseline"
  changed_files:
    - "orca-harness/evidence_binding/models.py"
    - "orca-harness/tests/unit/test_evidence_binding.py"
  unchanged_target_files:
    - "orca-harness/evidence_binding/__init__.py"
    - "orca-harness/evidence_binding/composer.py"
  findings:
    - id: "EB-01"
      severity: "major"
      issue: "duplicate non-bound slice rows could pass Jsg01EvidenceRecord validation"
      closure: "validator now rejects duplicate carried slice_id rows; regression test added"
    - id: "EB-02"
      severity: "major"
      issue: "CLEARED finalization reads could carry a blank current_receipt_id"
      closure: "validator now rejects blank current_receipt_id on CLEARED reads; regression test added"
  validation:
    red_check: "15 passed, 2 failed before model patch"
    focused_post_patch: "17 passed"
    full_post_patch: "712 passed, 1 skipped"
  verdict: "patch_applied_for_home_model_adjudication"
  non_claims:
    - "not approval"
    - "not readiness"
    - "not JSG-01 unfreeze"
    - "not lifecycle keep claim"
```

## Home-Model Adjudication (anthropic/claude-fable-5, 2026-06-12)

- **EB-01 (duplicate non-bound slice rows): ACCEPTED verbatim.** Real validator
  gap — the original coherence check guarded only the bound `slice_id` count, so
  a hand-built record could carry duplicate sibling rows and corrupt the
  one-row-per-slice audit surface. The no-duplicates rejection is the correct
  minimal closure; the composer cannot produce duplicates from a valid packet,
  so this hardens exactly the hand-built/mutated-record path.
- **EB-02 (blank `current_receipt_id` on CLEARED): ACCEPTED verbatim.** Real
  verbatim-carry honesty gap (whitespace-only id passed the `None` check);
  closure mirrors the consumer model's non-empty enforcement.
- **Preflight hash-mismatch: adjudicated as pure line-ending drift.** The
  delegate's preserved baseline copies contain CRLF; normalizing them to LF
  reproduces the commission's authored pins byte-for-byte for both mismatched
  files (verified by the home model, output observed 2026-06-12). No
  substantive content drift existed; the owner's proceed-from-live-baseline
  authorization was sound and the recorded baseline is the authored content.
- **Validation observed at adjudication (home environment, repo config):**
  focused `17 passed`; full suite `712 passed, 1 skipped in 83.86s`.
- **Kept state:** both reviewer hunks kept; `__init__.py` / `composer.py`
  untouched at their authored hashes. Post-adjudication SHA256 = the
  post-patch hashes recorded above (re-verified fresh by the home model).
- **Residual accepted:** `model_construct` / post-validation mutation is a
  general Pydantic escape hatch, mitigated at the read boundary by validate-on-
  load; not a binding-specific defect.
- Boundary unchanged: decision input recorded, not validation or readiness;
  JSG-01 stays FROZEN; this record is the binding slice's review provenance.
