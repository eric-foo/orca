# SP-5 Finalization Producer Delegated Adversarial Code Review-and-Patch v0

```yaml
retrieval_header_version: 1
artifact_role: Delegated adversarial code review-and-patch report
scope: >
  Bounded review-and-patch pass for the SP-5 finalization producer slice:
  orca-harness/runners/run_finalization_receipt.py and
  orca-harness/tests/unit/test_run_finalization_receipt.py only.
reviewed_by: GPT-5 Codex / OpenAI
authored_by: anthropic/claude-fable-5
author_home_model_family: anthropic
controller_model_family: openai
de_correlation_bar: cross_vendor_discovery
source_context: SOURCE_CONTEXT_READY
output_mode: review-report + working-tree patch + paste-ready courier
authority_boundary: retrieval_only
review_use_boundary: >
  Decision input only. The home model adjudicates every change before anything
  is kept. No validation, readiness, approval, lifecycle, or JSG-01 unfreeze
  claim is made by this report.
```

```yaml
review_summary:
  status: PATCH_PROPOSED_FOR_HOME_MODEL_ADJUDICATION
  recommendation: keep_after_home_model_adjudicates_if_the_distinct_post_write_failure_path_is_accepted
  findings_count: 1
  blocking_findings: 0
  advisory_findings: 1
  summary: >
    One material failure-visibility issue was found and patched: a post-write
    verification failure was raised through the same pre-write refusal class and
    CLI prefix even though the appended receipt was retained for audit.
```

## Source Loading

Method sources reference-loaded:

- `workflow-deep-thinking` - resolvable.
- `workflow-code-review` - resolvable.

Commissioned source pack loaded:

1. `orca-harness/runners/run_finalization_receipt.py`
2. `orca-harness/tests/unit/test_run_finalization_receipt.py`
3. `orca-harness/schemas/finalization_models.py`
4. `docs/research/judgment-spine/sp5_finalization_receipt_spec_v0.md`
5. `docs/decisions/ar_01_pre_decision_status_finalizer_staffing_v0.md`
6. `orca-harness/harness_utils.py`
7. `orca-harness/schemas/case_models.py`
8. `orca-harness/tests/contract/test_no_llm_imports.py`
9. `orca-harness/tests/contract/test_finalization_models_contract.py`

Preflight target hashes matched the commission before editing:

```yaml
pre_patch_sha256:
  orca-harness/runners/run_finalization_receipt.py: CAF6C0FCDEBEB15720331560676D19B5547FCEA178E899DBC4C55022AC2D8517
  orca-harness/tests/unit/test_run_finalization_receipt.py: DD33920581F1563DCA7F305A9CBB54AED917CD436A2F14C8341CDF33A3174050
post_patch_sha256:
  orca-harness/runners/run_finalization_receipt.py: 3D12109EB39CDC2DFBAF5E8EA6DBA3A5AF44D1A4E27DABF11C735702452EBC1D
  orca-harness/tests/unit/test_run_finalization_receipt.py: 57789D572D43658A6D1B6AFF6AE58D9ED1F533A348E46262949BF2A5880F6DC6
```

## Findings

### F-01 - Major - Post-write verification failure was collapsed into the pre-write refusal path

severity: major

location:

- `orca-harness/runners/run_finalization_receipt.py:48`
- `orca-harness/runners/run_finalization_receipt.py:172`
- `orca-harness/runners/run_finalization_receipt.py:184`
- `orca-harness/runners/run_finalization_receipt.py:263`

issue:

The runner used `FinalizationActError` for a post-write verification failure.
That error class states the act was refused and nothing was written, and the CLI
rendered all such errors as `finalization act refused`. The post-write branch is
materially different: the receipt has already been appended, then the fresh-read
consumer failed to clear it.

evidence:

- `AGENTS.md:8` requires real failure visibility and no fake success paths.
- `orca-harness/runners/run_finalization_receipt.py:48` defined `FinalizationActError` as a refusal where nothing was written.
- `orca-harness/runners/run_finalization_receipt.py:172` performs the required fresh-read post-write verification.
- `orca-harness/runners/run_finalization_receipt.py:184` now raises `FinalizationPostWriteVerificationError`; before this patch, that branch raised `FinalizationActError`.
- `orca-harness/runners/run_finalization_receipt.py:263` and `:265` now split refusal from recorded-but-unverified CLI outcomes.
- `docs/research/judgment-spine/sp5_finalization_receipt_spec_v0.md:50` requires the consumer to block rather than repair or infer.
- `docs/research/judgment-spine/sp5_finalization_receipt_spec_v0.md:94` requires append-only retained-prior behavior.

impact:

Before the patch, a failure mode that wrote an audit record could be surfaced
through a "refused" path whose class docstring said nothing was written. That is
not a success false-positive, but it is a false refusal/no-write implication and
can mislead an operator or home-model adjudicator about the durable stream state.

minimum_closure_condition:

Post-write verification failure must have a distinct visible error path that
does not claim or imply the act was refused before writing. The CLI must render
that distinction, and tests must prove the audit record remains persisted.

next_authorized_action:

Home model adjudicates the proposed patch. No further source edits are
authorized by this report.

## Patch Summary

The patch:

- adds `FinalizationPostWriteVerificationError` for the post-write verification branch;
- changes the post-write verification failure raise site to use that class;
- changes `main()` to exit with status `3` and message `finalization act recorded but not verified` for that branch, while preserving status `2` and `finalization act refused` for pre-write refusals;
- adds two regression tests proving the direct API and in-process CLI path preserve the recorded-but-unverified distinction and keep the appended audit document visible.

## Per-Change Citation Map

```yaml
changes:
  - change: add FinalizationPostWriteVerificationError
    file: orca-harness/runners/run_finalization_receipt.py
    lines: [52]
    citations:
      - AGENTS.md:8
      - orca-harness/runners/run_finalization_receipt.py:48
      - orca-harness/runners/run_finalization_receipt.py:172
  - change: raise the distinct post-write error after fresh-read verification fails
    file: orca-harness/runners/run_finalization_receipt.py
    lines: [184]
    citations:
      - docs/research/judgment-spine/sp5_finalization_receipt_spec_v0.md:50
      - docs/research/judgment-spine/sp5_finalization_receipt_spec_v0.md:94
      - orca-harness/schemas/finalization_models.py:207
  - change: split CLI exit paths for refusal versus recorded-but-unverified
    file: orca-harness/runners/run_finalization_receipt.py
    lines: [263, 265]
    citations:
      - AGENTS.md:8
      - AGENTS.md:9
  - change: add regression tests for recorded-but-unverified behavior
    file: orca-harness/tests/unit/test_run_finalization_receipt.py
    lines: [174, 250]
    citations:
      - orca-harness/runners/run_finalization_receipt.py:172
      - orca-harness/runners/run_finalization_receipt.py:184
      - orca-harness/runners/run_finalization_receipt.py:265
```

## Unified Diffs

### `orca-harness/runners/run_finalization_receipt.py`

```diff
diff --git "a/_scratch\\delegated_review_sp5_producer\\originals\\run_finalization_receipt.py" "b/orca-harness\\runners\\run_finalization_receipt.py"
index 3bc92c1..351db08 100644
--- "a/_scratch\\delegated_review_sp5_producer\\originals\\run_finalization_receipt.py"
+++ "b/orca-harness\\runners\\run_finalization_receipt.py"
@@ -49,6 +49,10 @@ class FinalizationActError(ValueError):
     """A visible block: the finalization act was refused and nothing was written."""
 
 
+class FinalizationPostWriteVerificationError(RuntimeError):
+    """The receipt was appended, but the fresh-read consumer did not verify it."""
+
+
 def load_receipts(receipts_file: Path) -> list[FinalizationReceipt]:
     """Strictly load every receipt document from the append-only stream.
 
@@ -177,7 +181,7 @@ def perform_finalization_act(
         verdict.result is not FinalizationProvenanceResult.CLEARED
         or verdict.current_receipt_id != receipt.receipt_id
     ):
-        raise FinalizationActError(
+        raise FinalizationPostWriteVerificationError(
             f"post-write verification failed for receipt {receipt.receipt_id} "
             f"({verdict.result.value}: {verdict.reason}); the appended receipt "
             f"was retained for audit but the act is NOT verified."
@@ -258,6 +262,11 @@ def main(argv: Sequence[str] | None = None) -> int:
         )
     except FinalizationActError as exc:
         parser.exit(status=2, message=f"finalization act refused: {exc}\n")
+    except FinalizationPostWriteVerificationError as exc:
+        parser.exit(
+            status=3,
+            message=f"finalization act recorded but not verified: {exc}\n",
+        )
 
     print(f"receipt_id: {receipt.receipt_id}")
     print(f"evidence_id: {receipt.evidence_id}")
```

### `orca-harness/tests/unit/test_run_finalization_receipt.py`

```diff
diff --git "a/_scratch\\delegated_review_sp5_producer\\originals\\test_run_finalization_receipt.py" "b/orca-harness\\tests\\unit\\test_run_finalization_receipt.py"
index 7806343..28e1816 100644
--- "a/_scratch\\delegated_review_sp5_producer\\originals\\test_run_finalization_receipt.py"
+++ "b/orca-harness\\tests\\unit\\test_run_finalization_receipt.py"
@@ -6,9 +6,11 @@ from pathlib import Path
 
 import pytest
 
+import runners.run_finalization_receipt as runner
 from harness_utils import load_yaml_documents
 from runners.run_finalization_receipt import (
     FinalizationActError,
+    FinalizationPostWriteVerificationError,
     load_receipts,
     main,
     perform_finalization_act,
@@ -16,6 +18,7 @@ from runners.run_finalization_receipt import (
 from schemas.case_models import PreDecisionStatus
 from schemas.finalization_models import (
     FinalizationProvenanceResult,
+    FinalizationVerdict,
     evaluate_finalization_provenance,
 )
 
@@ -168,6 +171,29 @@ def test_malformed_existing_stream_blocks_and_is_not_repaired(tmp_path: Path) ->
     _assert_unchanged(receipts_file, before)
 
 
+def test_post_write_verification_failure_reports_recorded_not_refused(
+    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
+) -> None:
+    receipts_file = tmp_path / "receipts.yaml"
+
+    def blocked_verdict(**_kwargs) -> FinalizationVerdict:
+        return FinalizationVerdict(
+            result=FinalizationProvenanceResult.BLOCKED,
+            reason="forced verification failure",
+        )
+
+    monkeypatch.setattr(runner, "evaluate_finalization_provenance", blocked_verdict)
+
+    with pytest.raises(
+        FinalizationPostWriteVerificationError, match="retained for audit"
+    ):
+        _act(receipts_file)
+
+    documents = load_yaml_documents(receipts_file)
+    assert len(documents) == 1
+    assert documents[0]["evidence_id"] == "ev-1"
+
+
 # ---- CLI ----
 
 def _cli(receipts_file: Path, *extra: str) -> subprocess.CompletedProcess[str]:
@@ -221,6 +247,48 @@ def test_cli_refusal_exits_nonzero_with_visible_reason(tmp_path: Path) -> None:
     assert len(load_yaml_documents(receipts_file)) == 1
 
 
+def test_main_post_write_verification_failure_exits_distinct_status(
+    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
+) -> None:
+    receipts_file = tmp_path / "receipts.yaml"
+
+    def blocked_verdict(**_kwargs) -> FinalizationVerdict:
+        return FinalizationVerdict(
+            result=FinalizationProvenanceResult.BLOCKED,
+            reason="forced verification failure",
+        )
+
+    monkeypatch.setattr(runner, "evaluate_finalization_provenance", blocked_verdict)
+
+    with pytest.raises(SystemExit) as exc_info:
+        main(
+            [
+                "--receipts-file",
+                str(receipts_file),
+                "--evidence-id",
+                "ev-main-failed",
+                "--proposed-status",
+                "uncertain_timestamp",
+                "--proposed-basis",
+                "packing proposed value pending finalization",
+                "--final-status",
+                "verified_pre_decision",
+                "--finalizer-identity",
+                "operator:band_labeler_1",
+                "--judge-model-family",
+                JUDGE,
+                "--finalizer-model-family",
+                FINALIZER,
+            ]
+        )
+
+    captured = capsys.readouterr()
+    assert exc_info.value.code == 3
+    assert "recorded but not verified" in captured.err
+    assert "refused" not in captured.err
+    assert len(load_yaml_documents(receipts_file)) == 1
+
+
 def test_main_returns_zero_in_process(tmp_path: Path) -> None:
     receipts_file = tmp_path / "receipts.yaml"
     exit_code = main(
```

## Validation Evidence

Focused target:

```text
.venv\Scripts\python.exe -m pytest -p no:cacheprovider -o addopts= --basetemp C:\Users\vmon7\Desktop\projects\orca\_scratch\delegated_review_sp5_producer\pytest_tmp_focused_count tests\unit\test_run_finalization_receipt.py
collected 15 items
tests\unit\test_run_finalization_receipt.py ...............              [100%]
15 passed, 1 warning in 1.29s
```

Full suite:

```text
.venv\Scripts\python.exe -m pytest -p no:cacheprovider --basetemp C:\Users\vmon7\Desktop\projects\orca\_scratch\delegated_review_sp5_producer\pytest_full_tmp tests
694 passed, 1 skipped, 1 warning in 92.05s (0:01:32)
```

Validation caveat:

The repository-configured pytest temp/cache locations under
`orca-harness/_scratch` were access-denied in this environment before assertions
ran. The full suite was therefore run with cache disabled and an explicit
absolute `--basetemp` under the commissioned scratch directory. The suite result
above is the observed full-suite test result for the code; the temp-directory
access failure is an environment/sandbox artifact, not an assertion failure.

## Verdict

PATCH_PROPOSED_FOR_HOME_MODEL_ADJUDICATION.

The patch closes F-01 under the commissioned scope and leaves the rest of the
producer design unchanged. The home model must adjudicate the diff before it is
kept. This report is not validation, readiness, approval, acceptance, or
lifecycle completion. JSG-01 remains FROZEN regardless of this outcome.

## Residual Risk

No locking exists around the append-only stream. The current code is honest for
an operator-driven tool because it re-reads after append and refuses to verify if
another write leaves the new receipt non-current or consumer-blocked. It still
does not provide an atomic "current at return forever" guarantee under concurrent
writers. The minimum honest closure is to document that this producer is a
single-operator append tool unless a later architecture pass binds file locking
or transactional persistence. That is off-scope for this bounded patch.

## Off-Scope Flags

- No edits were made to `finalization_models.py`, specs, decisions, conductor
  docs, `ecr/`, boundary docs, or other lanes' files.
- No sealed facilitator-only artifacts were opened.
- No architecture pass was required.
- No commits, staging, or pushes were performed.

## Courier YAML

```yaml
delegated_code_review_return_for_home_model:
  commission: SP-5 Finalization Producer slice A, ECR JSG-01 unfreeze build
  reviewed_by: GPT-5 Codex / OpenAI
  authored_by: anthropic/claude-fable-5
  de_correlation_bar: cross_vendor_discovery
  source_context: SOURCE_CONTEXT_READY
  status: PATCH_PROPOSED_FOR_HOME_MODEL_ADJUDICATION
  report_path: docs/review-outputs/adversarial-artifact-reviews/sp5_finalization_producer_delegated_adversarial_code_review_patch_v0.md
  touched_files:
    - orca-harness/runners/run_finalization_receipt.py
    - orca-harness/tests/unit/test_run_finalization_receipt.py
  findings:
    - id: F-01
      severity: major
      summary: >
        Post-write verification failure was previously routed through the
        pre-write refusal/nothing-written error path.
      minimum_closure_condition: >
        Recorded-but-unverified must be visibly distinct from refused-before-write,
        and tests must prove the audit record remains persisted.
      closure_in_patch: proposed
  validation:
    focused: "15 passed, 1 warning in 1.29s"
    full_suite: "694 passed, 1 skipped, 1 warning in 92.05s"
    temp_caveat: >
      Repo-configured pytest temp/cache path was access-denied; validation used
      an explicit absolute basetemp and disabled pytest cache.
  verdict: >
    Decision input only. Home model adjudicates every change before keep. No
    validation, readiness, approval, lifecycle, or JSG-01 unfreeze claim.
```

## Home-Model Adjudication (anthropic/claude-fable-5, 2026-06-12)

- **F-01: ACCEPTED — all reviewer hunks kept verbatim** (distinct
  `FinalizationPostWriteVerificationError`, CLI exit 3 `recorded but not
  verified` split from exit 2 `refused`, both regression tests). The finding is
  real: the pre-patch code surfaced a persisted-receipt state through an error
  class and CLI prefix that claimed nothing was written.
- **Adjudication extension (CA-applied, completing F-01's own closure
  condition):** the post-write fresh read (`load_receipts`) could still raise
  the refused-shaped `FinalizationActError` AFTER the append — the same
  misreport class. Now re-raised as `FinalizationPostWriteVerificationError`
  (`run_finalization_receipt.py`, post-write try/except) with regression test
  `test_post_write_load_failure_reports_recorded_not_refused`.
- **Residual-risk note (no locking): ACCEPTED as the honest bound.** The
  producer is a single-operator append tool; transactional persistence is
  off-scope unless a later architecture pass binds it. Documented residual, no
  code change.
- **Temp-path caveat: adjudicated environmental.** The full suite runs green in
  the home environment under the repo-configured basetemp/cache
  (`_scratch/pytest_tmp`); no repo config change needed.
- **Validation observed at adjudication (home environment, repo config):**
  full suite `695 passed, 1 skipped in 81.14s`; focused producer file 16 tests
  green.
- **Kept state (post-adjudication SHA256):**
  - `orca-harness/runners/run_finalization_receipt.py`: `D946ED72E82FF6524319E657B01B731B2BE3407D285D957EC473419E4BFD2732`
  - `orca-harness/tests/unit/test_run_finalization_receipt.py`: `D6640380695257099F29C8E3F3B6C78CA147171C9360B0A43AAF5A846B9A4ECB`
- Boundary unchanged: not validation, readiness, or judgment-quality evidence;
  JSG-01 stays FROZEN; this record is the producer slice's review provenance.
