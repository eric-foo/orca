# Source Observability Helper — Blast-Radius Recheck v0

```yaml
retrieval_header_version: 1
artifact_role: Review report
scope: >
  Bounded recheck of the source-observability helper patch.
  Checks only whether F-01 through F-04 are closed and whether the
  source_structure_required expansion and Slot 1/2/3 usage test
  introduced any new blocker or major issue.
use_when:
  - Checking whether the patch is safe for bounded continued use of the helper.
  - Confirming finding closure before owner acts on next step.
authority_boundary: retrieval_only
reviewed_artifacts:
  - orca-harness/source_observability/models.py
  - orca-harness/source_observability/checker.py
  - orca-harness/tests/unit/test_source_observability_checker.py
  - orca-harness/tests/unit/test_source_observability_pressure_test_usage.py
  - orca-harness/tests/contract/test_source_observability_no_runtime_imports.py
prior_review_report: docs/review-outputs/source_observability_helper_adversarial_implementation_review_v0.md
prior_review_sha256: 2CAE38395A6738E302E2706BB38F2470C5E6065308FDDE1AECD0AF9C13AD676D
review_method: >
  workflow-deep-thinking closure-risk framing (reference-loaded) followed by
  workflow-code-review in bounded recheck posture (reference-loaded, applied inline)
review_posture: adversarial bounded recheck
output_mode: filesystem-output
required_output_path: docs/review-outputs/source_observability_helper_blast_radius_recheck_v0.md
patch_queue_authorized: false
```

---

## Recommendation (Top)

**`safe_for_continued_use_with_advisory_carry`**

F-01, F-03, and F-04 are fully closed. F-02 is closed for the `access_posture`
case (the explicit example in the finding); the same double-reporting pattern
persists for `source_language_posture`, `archive_body_posture`, `media_posture`,
and is carried into the new `source_structure_posture` expansion. This residual
is advisory-level, unchanged from original F-02's severity, and does not block
continued use or invalidate any other closure.

The `source_structure_required` / `_check_source_structure` expansion is
in-scope, backward-compatible, correctly implemented, and resolves the prior F-07
informational gap. The Slot 1/2/3 usage test is well-scoped, boundary-compliant,
and does not introduce validation, readiness, acquisition, or downstream scope.

No boundary violation found. No new blocker or major finding introduced.

---

## Method Sequence

```text
Step 1: AGENTS.md read                              — done
Step 2: .agents/workflow-overlay/README.md read     — done
Step 3: workflow-deep-thinking REFERENCE-LOADED     — active from prior review turn
Step 4: workflow-code-review REFERENCE-LOADED       — active from prior review turn
Step 5: SOURCE-LOAD prior review + all target files — done; all hashes verified
Step 6: SOURCE_CONTEXT_READY declared               — done
Step 7: workflow-deep-thinking APPLIED (closure-risk framing);
        workflow-code-review APPLIED (bounded recheck posture) — done
Step 8: durable recheck report written              — this artifact
```

---

## Preflight

```yaml
orca_start_preflight:
  agents_read: yes
  overlay_read: yes
  source_pack: custom bounded source-observability helper recheck
  edit_permission: read-only review; recheck report write only
  target_scope:
    - F-01 through F-04 closure
    - source_structure_required expansion
    - Slot 1/2/3 pressure-test usage test
  dirty_state_checked: yes
  blocked_if_missing: none missing
```

Expected branch `main` and HEAD `fb7f1a1` confirmed.
Target helper files and prior review report are untracked; reviewed in place
after hash verification.

---

## Hash Verification

| File | Expected SHA256 | Match |
| --- | --- | --- |
| `source_observability_helper_adversarial_implementation_review_v0.md` | `2CAE38395A6738E302E2706BB38F2470C5E6065308FDDE1AECD0AF9C13AD676D` | YES |
| `orca-harness/source_observability/models.py` | `5F43DA731E01EDC142BDDDB86367ABA0AB461CCF7369721C8389E1B4FAC3A3CA` | YES |
| `orca-harness/source_observability/checker.py` | `077B49618B67D1D9CF4CA1E8E5D754C27F69B44043CE3C304C945733831B3A8A` | YES |
| `orca-harness/tests/unit/test_source_observability_checker.py` | `AD259CD921876A00BE33313D66CBA6FFA36FC923E1EF11338E7ED13C4F432581` | YES |
| `orca-harness/tests/unit/test_source_observability_pressure_test_usage.py` | `4662BD07EE266DED8B527335681F54AB868A8DD10A12F568E96F65433E4DA769` | YES |
| `orca-harness/tests/contract/test_source_observability_no_runtime_imports.py` | `1E0D7F985C11C0C0B08111EAF5A75B59B12090C95C118F9FD8FC110240CEBD99` | YES |

`HASH_VERIFICATION: ALL PASSED`

---

## Source-Read Ledger

| Source | Role in this recheck |
| --- | --- |
| Prior review report (v0) | Baseline — F-01 through F-04 closure criteria and minimum closure conditions |
| `source_observability/checker.py` (patched) | F-01 guard fix; F-02 `checked_postures` change; new `_check_source_structure` |
| `source_observability/models.py` (patched) | `source_structure_required` field; `source_structure_not_preserved` type |
| `test_source_observability_checker.py` (patched) | F-01, F-02, F-04 new test coverage |
| `test_source_observability_pressure_test_usage.py` (new) | Slot 1/2/3 usage test scope and correctness |
| `test_source_observability_no_runtime_imports.py` (patched) | F-03 urllib root-based fix |

---

## Closure Risk Framing — `workflow-deep-thinking` Applied

Seven risks framed before assessing closure:

**R-1 — F-01 fix may replace one falsy check with another.**
`any(note.strip() for note in record.limitation_notes)` must handle `[]`, `[""]`,
`["  "]`, `["actual note"]`, and mixed lists correctly. Checked below.

**R-2 — F-02 fix may address only `access_posture` while the broader closure
condition (all dedicated-check fields) remains unmet.**
Original F-02 explicitly named `source_language_posture` and `media_posture` as
additional cases. Checked below.

**R-3 — The `source_structure` expansion may reproduce the F-02 double-reporting
pattern for `source_structure_posture`.**
If `_check_source_structure` fires for a field still in `checked_postures`, the
same advisory-level double-report recurs. Checked below.

**R-4 — F-03 fix may miss the `ImportFrom` form or introduce a regression by
removing `FORBIDDEN_IMPORT_MODULES`.**
The prior `FORBIDDEN_IMPORT_MODULES = {"urllib.request"}` check is removed.
Checked below.

**R-5 — F-04 test may not correctly target the `posture=PRESERVED, count=0`
boundary condition.**
The test must use the precise combination that makes the check fire while
`posture` claims preserved. Checked below.

**R-6 — Usage test may express pressure-test lessons in a way that introduces
validation, readiness, or downstream scope.**
Checked below.

**R-7 — Expansion may introduce acquisition imports or ECR/schema scope that
slips past the contract test.**
Checked below.

---

## F-01 Closure Assessment

**Status: `closed`**

**Patch — `checker.py:129`:**

```python
if any(note.strip() for note in record.limitation_notes):
    return []
```

**Behavioral verification:**

```
limitation_notes=[]          → any([]) is False → guard not triggered → check fires ✓
limitation_notes=[""]        → "".strip()="" (falsy) → any([""]) is False → check fires ✓  (F-01 fixed)
limitation_notes=["  "]      → "  ".strip()="" → any(["  "]) is False → check fires ✓  (whitespace handled)
limitation_notes=["note"]    → "note".strip() truthy → any(True) is True → early-return ✓  (correctly silenced)
limitation_notes=["","note"] → any(["","note".strip()]) → any([False,True]) = True → early-return ✓
```

The fix correctly distinguishes empty lists, whitespace-only lists, and non-empty-content lists.

**Covering test:** `test_blank_limitation_note_does_not_silence_unnoted_postures`
(`test_source_observability_checker.py:99–111`):

```python
result = run_source_observability_checks(
    [_record(source_language_posture=ObservablePosture.PARAPHRASED, limitation_notes=[""])]
)
assert [limitation.limitation_type for limitation in result.limitations] == ["unnoted_non_preserved_posture"]
```

Trace: `any(["".strip()])` = `any([""])` = `False` → unnoted check proceeds →
`source_language_posture=PARAPHRASED` in `NON_PRESERVED_POSTURES` → emits limitation. ✓

Red-green proof: before the fix, `bool([""])` is `True` → early-return `[]` → test would
fail (no limitation). After the fix, test passes. ✓

**F-01: closed.** Minimum closure condition met.

---

## F-02 Closure Assessment

**Status: `closed` for `access_posture`; advisory carry for remaining fields**

**What was fixed:** `access_posture` removed from `checked_postures` in
`_check_unnoted_non_preserved_postures` (`checker.py:132–137`):

```python
checked_postures = {
    "source_language_posture": record.source_language_posture,
    "source_structure_posture": record.source_structure_posture,
    "archive_body_posture": record.archive_body_posture,
    "media_posture": record.media_posture,
}
```

`access_posture` is absent. `_check_access_failure` has sole ownership of
access-posture classification.

**Covering test:** `test_access_failure_is_not_double_reported_as_unnoted_posture`
(`test_source_observability_checker.py:114–126`):

```python
result = run_source_observability_checks(
    [_record(access_posture=ObservablePosture.FAILED, limitation_notes=[])]
)
assert [limitation.limitation_type for limitation in result.limitations] == ["access_failure_visible"]
```

Trace: `_check_access_failure` fires → `access_failure_visible`. `_check_unnoted_non_preserved_postures`:
default postures are PRESERVED or NOT_APPLICABLE; `access_posture` not in `checked_postures`. Result
is exactly `["access_failure_visible"]`. ✓

Red-green proof: before the fix, `access_posture=FAILED` was in `checked_postures` → would have
also emitted `unnoted_non_preserved_posture` → assertion `["access_failure_visible"]` would fail. ✓

**What remains unaddressed (advisory carry):**

The original F-02 finding named three additional double-reporting cases beyond `access_posture`:

1. `source_language_posture` when `source_language_anchor_required=True`, posture non-preserved, `limitation_notes=[]`
2. `media_posture` when `media_required=True`, posture non-preserved, `limitation_notes=[]`
3. `archive_body_posture` when `archive_body_expected=True`, posture non-preserved, `limitation_notes=[]`

All three fields remain in `checked_postures`. Concrete trace for case 1:

```
Record: source_language_anchor_required=True, source_language_posture=PARAPHRASED,
        source_language_anchor_count=0, limitation_notes=[]

_check_source_language:    anchor_required=True, posture≠PRESERVED → fires → source_language_anchor_missing
_check_unnoted_non_preserved_postures:
  any([]) is False → scans checked_postures:
    source_language_posture=PARAPHRASED (in NON_PRESERVED) → fires → unnoted_non_preserved_posture

Result: two limitations for one posture state. No test asserts this is or is not intended.
```

The minimum closure condition from the prior review was: "exclude posture fields already covered
by dedicated checks from the unnoted scan." This was applied to `access_posture` only.

Additionally, the new `source_structure_posture` expansion (see below) introduces a fourth
unaddressed instance of the same pattern.

**Severity:** Advisory carry — same level as original F-02. Does not block use. Does not
invalidate F-01, F-03, F-04 closure. Does not constitute a new independent finding.

**F-02: closed for `access_posture`. Advisory carry persists for remaining fields.**

---

## F-03 Closure Assessment

**Status: `closed`**

**Patch — `test_source_observability_no_runtime_imports.py:7–17`:**

```python
FORBIDDEN_IMPORT_ROOTS = {
    "aiohttp", "bs4", "httpx", "playwright", "requests",
    "scrapy", "selenium", "socket", "urllib",
}
```

`FORBIDDEN_IMPORT_MODULES` removed entirely. The check for `ast.ImportFrom` nodes
is now:

```python
imported_root = node.module.split(".")[0]
assert imported_root not in FORBIDDEN_IMPORT_ROOTS
```

**Verification for all urllib import forms:**

| Import form | `imported_root` | Caught? |
| --- | --- | --- |
| `import urllib.request` | `urllib` | YES |
| `from urllib.request import urlopen` | `urllib` | YES |
| `from urllib import request` (prior gap) | `urllib` | YES |

**Regression check for `FORBIDDEN_IMPORT_MODULES` removal:**

The only entry in the removed set was `"urllib.request"`. The `ast.Import` check
used `{alias.name for alias in node.names} & FORBIDDEN_IMPORT_MODULES` to catch
`import urllib.request` via full module name. The new root-based check catches
`import urllib.request` via `imported_root = "urllib"`. The removal of the module-level
check introduces no gap.

**F-03: closed.** The `from urllib import request` gap is addressed. The F-08
informational limitation (dynamic imports not caught by static AST scan) is
pre-existing, unchanged, and remains informational.

---

## F-04 Closure Assessment

**Status: `closed`**

**Covering test:** `test_preserved_language_without_anchor_count_is_still_limited_when_required`
(`test_source_observability_checker.py:137–149`):

```python
result = run_source_observability_checks(
    [_record(source_language_anchor_count=0, source_language_anchor_required=True)]
)
assert [limitation.limitation_type for limitation in result.limitations] == ["source_language_anchor_missing"]
```

Default `_record` has `source_language_posture=PRESERVED`. With `anchor_count=0,
anchor_required=True`:

```
_check_source_language: anchor_required=True; posture==PRESERVED but count=0
  → NOT(PRESERVED AND count>0) → fires → source_language_anchor_missing

_check_unnoted_non_preserved_postures:
  source_language_posture=PRESERVED → not in NON_PRESERVED → no limitation
  (all other defaults also PRESERVED/NOT_APPLICABLE)

Result: ["source_language_anchor_missing"] ✓
```

Red-green proof: if the `and record.source_language_anchor_count > 0` condition were
removed from `_check_source_language`, the check would early-return for `posture=PRESERVED`
regardless of count — this test would fail. The test correctly guards the boundary. ✓

**F-04: closed.** Minimum closure condition met.

---

## Expansion Assessment: `source_structure_required` / `_check_source_structure`

**Result: no new blocker or major issue. One advisory carry (F-02 pattern).**

**Model change:**

`source_structure_required: bool = False` added to `SourceObservabilityRecord`
(`models.py:34`). Safe default: existing records that omit the field use `False`
(Pydantic uses the field default when the key is absent; `StrictModel` `extra="forbid"`
does not reject missing-with-default fields). ✓

`"source_structure_not_preserved"` added to `SourceObservabilityLimitation.limitation_type`
Literal (`models.py:45`). Additive only; no existing serialized types affected. ✓

`_record()` test factory does not include `source_structure_required` in its default
`values` dict. All prior tests that call `_record()` without an override use the model
default `False`. `_check_source_structure` therefore returns `[]` in all prior tests.
Prior test results are unaffected. ✓

**Checker function:**

```python
def _check_source_structure(record: SourceObservabilityRecord) -> list[SourceObservabilityLimitation]:
    if not record.source_structure_required or record.source_structure_posture == ObservablePosture.PRESERVED:
        return []
    return [SourceObservabilityLimitation(
        record_id=record.record_id,
        source_ref=record.source_ref,
        limitation_type="source_structure_not_preserved",
        posture=record.source_structure_posture,
        detail="Visible source structure is required but not visibly preserved.",
    )]
```

Logic is correct and mirrors `_check_media` exactly. Fires when
`source_structure_required=True` AND posture is not PRESERVED. The binary
required/preserved pattern is appropriate for RQ-01 structure-preservation
(no anchor-count layer needed). ✓

**Boundary check:** no acquisition path, no ECR/Cleaning/Judgment vocabulary,
no schema or storage design. Expansion is within the authorized slice. ✓

**F-07 resolution:** The prior F-07 informational finding noted the asymmetry
that `source_structure_posture` had no dedicated checker rule while
`source_language_posture` did. This expansion closes that asymmetry. ✓

**Advisory carry — F-02 pattern for `source_structure_posture`:**

`source_structure_posture` is in `checked_postures` AND is now also handled by
`_check_source_structure`. When `source_structure_required=True`, posture is
non-preserved, and `limitation_notes=[]`, both functions fire:

```
_check_source_structure  → source_structure_not_preserved
_check_unnoted_non_preserved_postures → unnoted_non_preserved_posture for source_structure_posture
```

Two limitations for one posture state. This is the same advisory-level pattern
as the unresolved F-02 cases. No test asserts that this is or is not intended.

The usage test avoids this because all SLOT records with non-preserved
`source_structure_posture` include non-empty `limitation_notes`, silencing
the unnoted check. The carry does not surface in any existing test.

**This carry is advisory, pre-existing in pattern, and does not constitute a
new independent finding or blocker.**

---

## Usage Test Assessment: `test_helper_expresses_first_pressure_test_batch_lessons`

**Status: correctly scoped, no boundary violation.**

**Scope verification:**

| Concern | Evidence | Verdict |
| --- | --- | --- |
| Source acquisition | `source_ref` values use abstract `slot{N}://` URIs, not real URLs | No acquisition |
| Source content exposure | `limitation_notes` contain generic posture descriptions only | No exposure |
| Quality scoring | Test asserts limitation types only; no score fields or quality labels | No scoring |
| ECR/Cleaning/Judgment boundary | No fields, functions, or assertions reference downstream layers | No violation |
| Readiness claim | No `has_visible_limitations` assertion as a gate; types only | No readiness claim |

**Limitation type traces:**

SLOT1-MI-BIWS: `anchor_required=True, anchor_count=0` → `source_language_anchor_missing` |
`source_structure_required=True, posture=PARAPHRASED` → `source_structure_not_preserved` |
`media_required=True, posture=NOT_ATTEMPTED` → `media_not_preserved` |
`archive_body_expected=True, posture=NOT_ATTEMPTED` → `archive_body_not_retrieved` |
`access_posture=PRESERVED` → no access check fires |
`limitation_notes` non-empty → unnoted check silenced.
Expected: 4 limitations. ✓

SLOT2-TEAL: `archive_body_expected=True, posture=FAILED` → `archive_body_not_retrieved` |
`access_posture=FAILED, locator=True, cutoff=True` → `access_failure_visible` |
`source_language_anchor_required=False` (default), `source_structure_required=False` (default) → no structure/language fires |
`limitation_notes` non-empty → unnoted check silenced.
Expected: 2 limitations; `archive_body_not_retrieved` before `access_failure_visible`
(call order: `_check_archive_body` before `_check_access_failure`). ✓

SLOT3-REDDIT-WSO: `anchor_required=True, posture=PRESERVED, anchor_count=4` → no language limitation |
`source_structure_required=False` (default) → no structure check fires |
`media_required=True, posture=POINTER_ONLY` → `media_not_preserved` |
`archive_body_expected=True, posture=NOT_ATTEMPTED` → `archive_body_not_retrieved` |
`access_posture=PRESERVED` → no access check |
`limitation_notes` non-empty → unnoted check silenced.
Expected: 2 limitations. ✓

**Final assertion strength:**

```python
assert "unnoted_non_preserved_posture" not in {
    limitation.limitation_type for limitation in result.limitations
}
```

This is a correct structural assertion: all three records have non-empty, non-whitespace
`limitation_notes`, so `_check_unnoted_non_preserved_postures` correctly returns `[]`
for all. The assertion documents that this was deliberate. ✓

---

## Validation Evidence Consistency

Reported: "focused source-observability tests: 10 passed; full harness suite: 35 passed."

**Test count trace:**

- `test_source_observability_checker.py`: 8 tests
  (5 pre-existing + 3 new: `test_blank_*`, `test_access_failure_is_not_*`, `test_preserved_language_without_*`)
- `test_source_observability_pressure_test_usage.py`: 1 test (new)
- `test_source_observability_no_runtime_imports.py`: 1 test (patched but same count)

Total focused: 10. ✓

Full harness: prior 31 + 4 new = 35. ✓

Validation evidence is consistent with source read.

---

## Recheck Questions — Responses

**Q1. Is F-01 closed?**
Yes. `any(note.strip() for note in ...)` correctly rejects empty strings and whitespace-only
strings. Covered by a red-green discriminating test.

**Q2. Is F-02 closed?**
Closed for `access_posture`. Advisory carry: the same double-reporting pattern persists
for `source_language_posture`, `archive_body_posture`, `media_posture`, and is introduced
for `source_structure_posture` by the expansion. No test asserts intended behavior for
these remaining cases.

**Q3. Is F-03 closed enough for this helper's no-runtime-acquisition boundary?**
Yes. Adding `"urllib"` to `FORBIDDEN_IMPORT_ROOTS` catches all urllib import forms,
including `from urllib import request`. Removing `FORBIDDEN_IMPORT_MODULES` creates no
regression. The contract now correctly guarantees "no static urllib import."

**Q4. Is F-04 closed?**
Yes. The test covers the exact `posture=PRESERVED, anchor_count=0, anchor_required=True`
boundary and asserts the limitation fires. Red-green proof holds.

**Q5. Did the new `source_structure_required` / `_check_source_structure` addition introduce
any blocker or major problem?**
No. The function is correctly implemented, in-scope, backward-compatible, and addresses
prior F-07 informational gap. One advisory carry (same F-02 pattern for
`source_structure_posture`) is noted; not a new blocker.

**Q6. Does the Slot 1/2/3 usage test correctly express pressure-test lessons without turning
them into source acquisition, validation, scoring, ECR, Cleaning, Judgment, schema, or
source-access policy?**
Yes. Records use abstract identifiers and posture classifications only. No forbidden
vocabulary, no readiness or validation claims. The `"unnoted_non_preserved_posture" not in
{...}` assertion is a well-scoped structural correctness check.

**Q7. Do the reported validations plausibly cover the touched scope?**
Yes. Test counts match source read. Prior test behavior is unaffected by the expansion.
New tests directly cover F-01, F-02 (`access_posture` case), F-04, the expansion path
via the usage test, and the no-runtime-acquisition contract.

---

## Finding Summary

| Finding | Closure status |
| --- | --- |
| F-01 major | **CLOSED** — `any(note.strip())` guard correct; blank-note test added |
| F-02 advisory | **CLOSED (access_posture)** — removed from `checked_postures`; non-double-report test added. Advisory carry: `source_language_posture`, `archive_body_posture`, `media_posture`, and new `source_structure_posture` retain the same pattern. |
| F-03 advisory | **CLOSED** — `"urllib"` in `FORBIDDEN_IMPORT_ROOTS`; all urllib import forms caught |
| F-04 advisory | **CLOSED** — `PRESERVED + anchor_count=0 + required=True` boundary test added |

**New findings from expansion and recheck:**

| ID | Severity | Description |
| --- | --- | --- |
| F-02-carry | Advisory | `source_structure_posture` added to both `_check_source_structure` (dedicated) and `checked_postures` (unnoted scan). When `source_structure_required=True`, posture non-preserved, `limitation_notes=[]`, both checks fire. Consistent with unresolved pre-existing F-02 pattern. Usage test avoids via non-empty notes. Does not invalidate closure. |

**New blockers or majors: none.**

---

## Non-Claims

This recheck is not:
- validation of the source-observability helper
- readiness claim for any downstream use
- approval, sign-off, or acceptance
- mandatory remediation instruction
- patch authority
- ECR, Cleaning, Judgment, or source-access implementation authorization
- source-of-truth promotion
- full review rerun

Findings are decision input only. The F-02 advisory carry is open; it is not
mandatory remediation unless separately accepted and authorized.
