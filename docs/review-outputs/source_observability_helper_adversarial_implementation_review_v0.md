# Source Observability Helper — Adversarial Implementation Review v0

```yaml
retrieval_header_version: 1
artifact_role: Implementation review report
scope: >
  Read-only adversarial implementation review of the new local
  source_observability helper in orca-harness. Tests whether the
  implementation matches the authorized slice (local support/check only;
  no acquisition; no ECR/Cleaning/Judgment/schema design; no validation
  claims; visible limitations only).
use_when:
  - Deciding whether the helper may be used as a local support check input.
  - Checking whether the authorized scope was respected before owner action.
authority_boundary: retrieval_only
review_mode: strict_formal
output_mode: filesystem-output
required_output_path: docs/review-outputs/source_observability_helper_adversarial_implementation_review_v0.md
commissioned_by: adversarial-implementation-review-prompt-2026-06-01
review_posture: adversarial
patch_queue_authorized: false
```

---

## Recommendation (Top)

**`advisory_pass_with_one_major_finding`**

The implementation is locally deterministic, contains no acquisition imports,
and does not cross into ECR, Cleaning, Judgment, schema/storage design, or
readiness/validation claims. The authorized scope boundary is respected.

One major correctness finding (F-01) creates a false-pass path in the
`_check_unnoted_non_preserved_postures` check. Three advisory findings weaken
test coverage and introduce a double-reporting behavior. Five informational
findings cover naming precision and model invariant gaps.

No boundary violation was found. F-01 is the only finding that can suppress
a limitation that the checker is designed to emit.

---

## Method Sequence

```text
Step 1: AGENTS.md read                           — done
Step 2: .agents/workflow-overlay/README.md read  — done
Step 3: workflow-deep-thinking REFERENCE-LOADED  — done
Step 4: workflow-code-review REFERENCE-LOADED    — done
Step 5: SOURCE-LOAD target implementation files  — done
Step 6: SOURCE_CONTEXT_READY declared            — done
Step 7: deep-thinking applied (failure-mode framing);
        code review applied (adversarial posture) — done
Step 8: findings written first (below)           — done
```

---

## Preflight

```yaml
orca_start_preflight:
  agents_read: yes
  overlay_read: yes
  source_pack: custom source-observability implementation review
  edit_permission: read-only review; report write only
  target_scope:
    - orca-harness/source_observability/
    - orca-harness/tests/unit/test_source_observability_checker.py
    - orca-harness/tests/contract/test_source_observability_no_runtime_imports.py
    - orca-harness/README.md
  dirty_state_checked: yes
  blocked_if_missing: none missing
```

Expected branch `main` and HEAD `fb7f1a1` confirmed.
Dirty-state allowance applied: target implementation files are untracked;
reviewed in place after hash verification.

---

## Hash Verification

All review target and source-basis file hashes verified before review:

| File | Expected SHA256 | Match |
| --- | --- | --- |
| `orca-harness/README.md` | `E2048915...03A908` | YES |
| `orca-harness/source_observability/__init__.py` | `6FBB62B3...B56339` | YES |
| `orca-harness/source_observability/models.py` | `1B81DA2F...E775F` | YES |
| `orca-harness/source_observability/checker.py` | `5F1C840F...05746` | YES |
| `orca-harness/tests/unit/test_source_observability_checker.py` | `0F3024D6...F23F6C` | YES |
| `orca-harness/tests/contract/test_source_observability_no_runtime_imports.py` | `9F9C55D3...17DA` | YES |
| `docs/product/data_capture_spine_source_observability_requirements_scoping_v0.md` | `B242238D...55625` | YES |
| `docs/product/data_capture_spine_pressure_test_all_slot_synthesis_v0.md` | `A0021F1E...FB0E5` | YES |
| `docs/review-outputs/adversarial-artifact-reviews/data_capture_spine_pressure_test_all_slot_synthesis_blast_radius_recheck_v0.md` | `46FE7128...CC68D` | YES |

`HASH_VERIFICATION: ALL PASSED`

Additional context reads (not in preflight, read for authority verification):
- `orca-harness/schemas/case_models.py` — read to verify `StrictModel` definition
- `orca-harness/tests/conftest.py` — read for test infrastructure context
- `orca-harness/tests/contract/test_no_llm_imports.py` — read for contract-test pattern context

---

## Source-Read Ledger

| Source | Role in this review |
| --- | --- |
| `source_observability/checker.py` | Primary review target — checker logic |
| `source_observability/models.py` | Primary review target — model definitions and posture vocabulary |
| `source_observability/__init__.py` | Review target — boundary check |
| `tests/unit/test_source_observability_checker.py` | Test coverage review |
| `tests/contract/test_source_observability_no_runtime_imports.py` | Contract boundary review |
| `orca-harness/README.md` | Boundary wording review |
| `schemas/case_models.py` | Authority verification for `StrictModel` definition |
| `data_capture_spine_source_observability_requirements_scoping_v0.md` | Source authority for RQ-01 through RQ-05 |
| `data_capture_spine_pressure_test_all_slot_synthesis_v0.md` | Source authority for cross-slot pressure context |
| `blast_radius_recheck_v0.md` | Source authority for review lineage |

---

## Scope Review

**Authorized slice:**
- Local source-observability support/check helper only
- No source acquisition
- No runtime, browser, API, scraper, or archive retrieval
- No ECR, Cleaning, Judgment, schema/storage, or source-access policy design
- No validation or readiness claims
- Reports visible limitations only

**Scope verdict:** Implementation stays within the authorized slice. No boundary violation found.

**Boundary checks passed:**
- `checker.py` imports only from `source_observability.models` — no runtime acquisition path
- `models.py` imports only from `pydantic`, `typing`, `enum`, and `schemas.case_models` — all standard
- `schemas.case_models.StrictModel` is `BaseModel` with `extra="forbid"` — no acquisition, no downstream scope
- `__init__.py` is empty except for a docstring
- No model name implies quality score, readiness, ECR, Cleaning, Judgment, or validation
- README explicitly states: "does not fetch sources, retrieve archives, automate browsers, call APIs, score source quality, validate Data Capture, or authorize downstream ECR, Cleaning, or Judgment behavior"

---

## Findings

### F-01 — Empty-string limitation_notes creates false-pass path in `_check_unnoted_non_preserved_postures`

```yaml
finding_id: F-01
severity: major
target: orca-harness/source_observability/checker.py
location: checker.py line 114
```

**Evidence:**

```python
def _check_unnoted_non_preserved_postures(
    record: SourceObservabilityRecord,
) -> list[SourceObservabilityLimitation]:
    if record.limitation_notes:   # line 114
        return []
```

The guard uses Python's truthiness of a list. `bool([])` is `False` (check fires), but
`bool([""])` is `True` (check silenced). A record with `limitation_notes=[""]` — a list
containing one empty string — passes the guard and returns `[]` even when multiple
non-preserved postures are present and genuinely unnoted.

The `SourceObservabilityRecord` model definition (`models.py:36`) declares
`limitation_notes: list[str] = Field(default_factory=list)` with no validator
requiring non-empty string items. An empty string is valid input and
`model_validate({"limitation_notes": [""]})` succeeds.

**Authority basis:** The purpose of `_check_unnoted_non_preserved_postures` is to surface
non-preserved postures that have not been documented with a limitation note. An empty
string is not a limitation note — it carries no information. The check's semantics
require that at least one non-empty note be present before silencing, but the
implementation silences on any non-empty list regardless of item content.

**Impact:** Any record constructed with `limitation_notes=[""]` will produce no
`unnoted_non_preserved_posture` limitations even if every posture field is
non-preserved. This is a false-pass path: the checker reports no unnoted limitation
where multiple unnoted limitations should appear.

**No test covers this path.** The unit tests use either `limitation_notes=[]` (fires)
or `limitation_notes=["...non-empty string..."]` (correctly silenced). The
empty-string case is not exercised.

```yaml
minimum_closure_condition: >
  The guard condition must distinguish an empty list from a list containing
  only empty strings. Acceptable approaches: validate non-empty string items
  in the model (reject ""), or change the guard to check for at least one
  non-empty note (e.g., `if any(record.limitation_notes)`), or use a
  field validator that strips and rejects empty strings. The fix must be
  covered by a test that passes [""] and expects unnoted limitations to fire.
next_authorized_action: >
  Decision input only. No patch authority in this review. Owner or authorized
  implementer must assess and apply a fix.
verification_expectation: >
  Red-green: a test with limitation_notes=[""] and at least one non-preserved
  posture should fail (produce no limitations) before fix, pass (produce
  correct unnoted limitations) after fix.
patch_queue_entry: not authorized
```

---

### F-02 — Double-reporting when access-failure posture coincides with empty `limitation_notes`

```yaml
finding_id: F-02
severity: advisory
target: orca-harness/source_observability/checker.py
location: checker.py lines 87-134 (interaction between _check_access_failure and _check_unnoted_non_preserved_postures)
```

**Evidence:**

When a record has `access_posture ∈ {INACCESSIBLE, FAILED}` AND `limitation_notes == []`:

1. `_check_access_failure` (lines 87-108) emits either `access_failure_visible` or
   `access_failure_context_missing` based on locator/cutoff visibility.
2. `_check_unnoted_non_preserved_postures` (lines 111-134) also emits
   `unnoted_non_preserved_posture` for `access_posture` because it is in
   `NON_PRESERVED_POSTURES` and `limitation_notes` is empty.

The same posture state generates two distinct limitation entries from two different
check functions. The same double-emission applies to:
- `source_language_posture` when `source_language_anchor_required=True` and posture
  is non-preserved and `limitation_notes == []`
- `media_posture` when `media_required=True` and posture is non-preserved and
  `limitation_notes == []`

**Authority basis:** The unnoted-posture check is designed to surface postures that
have not been noted elsewhere. When `_check_access_failure` already emits a
limitation for `access_posture`, the posture is not "unnoted" — it has been explicitly
processed by a dedicated check. The current logic is blind to whether a dedicated
check already fired; it gates only on `limitation_notes`.

**Impact:** Misleading limitation counts. A record with one access-failure state
and no limitation notes produces two limitation entries for the same underlying
posture. Consumers iterating `result.limitations` will see both an
`access_failure_*` entry and an `unnoted_non_preserved_posture` entry for the same
field, which overstates the distinct problem count.

No test covers the `access_posture ∈ ACCESS_FAILURE_POSTURES, limitation_notes=[]`
case, so this behavior is unverified.

```yaml
minimum_closure_condition: >
  The unnoted-posture check should not double-report posture fields already
  handled by a dedicated check. Acceptable approaches: exclude posture
  fields already covered by dedicated checks from the unnoted scan, or
  require a test that explicitly asserts the double-report case is or is not
  intended behavior.
next_authorized_action: decision input only
verification_expectation: >
  A test with access_posture=INACCESSIBLE, limitation_notes=[], locator_visible=True,
  cutoff_visible=True should clarify whether the expected output is one
  (access_failure_visible) or two (access_failure_visible + unnoted_non_preserved_posture)
  limitations for access_posture.
patch_queue_entry: not authorized
```

---

### F-03 — Contract test misses the `from urllib import request` import form

```yaml
finding_id: F-03
severity: advisory
target: orca-harness/tests/contract/test_source_observability_no_runtime_imports.py
location: lines 37-40
```

**Evidence:**

The contract test bans:

```python
FORBIDDEN_IMPORT_ROOTS = {"aiohttp", "bs4", "httpx", "playwright", "requests", "scrapy", "selenium", "socket"}
FORBIDDEN_IMPORT_MODULES = {"urllib.request"}
```

For `ast.ImportFrom` nodes, the check is:

```python
imported_root = node.module.split(".")[0]
assert imported_root not in FORBIDDEN_IMPORT_ROOTS
assert node.module not in FORBIDDEN_IMPORT_MODULES
```

The import `from urllib import request` produces `node.module = "urllib"`. This node:
- `imported_root = "urllib"` — not in `FORBIDDEN_IMPORT_ROOTS` → passes
- `node.module = "urllib"` — not in `FORBIDDEN_IMPORT_MODULES` (which has `"urllib.request"`) → passes

`from urllib import request` gives full access to `urllib.request.urlopen()`,
`urllib.request.urlretrieve()`, and related HTTP functions. The ban's intent
(block `urllib.request`) is not enforced for this import form.

The sibling contract test `test_no_llm_imports.py` uses the same pattern and has
the same structural gap.

**Impact:** The contract test does not guarantee "no runtime acquisition via urllib.request."
A future author writing `from urllib import request` would pass the test undetected.

```yaml
minimum_closure_condition: >
  Either add "urllib" to FORBIDDEN_IMPORT_ROOTS (which catches all urllib imports,
  including any non-acquisition submodules — acceptable for this helper's narrow
  scope), or add an explicit check for ImportFrom nodes where module="urllib" and
  any alias.name is "request". Must be covered by a test that verifies the new
  form is caught.
next_authorized_action: decision input only
verification_expectation: >
  A test that constructs a synthetic AST with `from urllib import request` and
  runs the contract checker against it should fail before fix and pass after fix.
patch_queue_entry: not authorized
```

---

### F-04 — No test for `source_language_anchor_required=True, posture=PRESERVED, anchor_count=0`

```yaml
finding_id: F-04
severity: advisory
target: orca-harness/tests/unit/test_source_observability_checker.py
location: test coverage gap
```

**Evidence:**

`_check_source_language` (checker.py lines 43-56) fires if:

```python
if not record.source_language_anchor_required:
    return []
if record.source_language_posture == ObservablePosture.PRESERVED and record.source_language_anchor_count > 0:
    return []
return [SourceObservabilityLimitation(...)]
```

The condition `posture == PRESERVED AND count > 0` implies both must hold for a
non-limitation result. The case `posture=PRESERVED, count=0` is the
"claimed preserved but no visible anchors" state — it should fire a limitation
(and does), but no test covers it.

The existing tests exercise:
- `posture=POINTER_ONLY, count=0, anchor_required=True` → fires (in the combined test)
- `posture=PRESERVED, count=2, anchor_required=True` → no limitation (happy path)

The gap case `posture=PRESERVED, count=0` is the boundary where the posture
self-reports as preserved but the count contradicts it. If the condition were
accidentally simplified to `posture == PRESERVED`, this case would become
a silent false-pass.

```yaml
minimum_closure_condition: >
  A unit test should explicitly cover posture=PRESERVED, anchor_count=0,
  source_language_anchor_required=True and assert that a
  source_language_anchor_missing limitation is emitted.
next_authorized_action: decision input only
verification_expectation: >
  The test fails (no limitation emitted) if the count check is accidentally
  dropped, and passes with the current implementation.
patch_queue_entry: not authorized
```

---

### F-05 — `has_visible_limitations=False` may be read as "no source limitations exist"

```yaml
finding_id: F-05
severity: informational
target: orca-harness/source_observability/models.py
location: models.py lines 59-61
```

**Evidence:**

```python
@property
def has_visible_limitations(self) -> bool:
    return bool(self.limitations)
```

`has_visible_limitations = False` when `self.limitations == []`. The property is
checker-scoped: it means "no limitations visible to this checker were found."
It cannot mean "no limitations exist" because the checker only reports what is
locally observable from the provided records.

The property name does not encode the "visible to this checker" qualifier. A caller
testing `not result.has_visible_limitations` and concluding "the source is clean"
or "the source is ready" would be making a false-success assumption beyond the
helper's semantics.

The README non-claims section correctly bounds this, but the model property itself
has no inline qualifier.

```yaml
minimum_closure_condition: >
  Informational only. No correctness bug. If the property remains, a docstring
  or rename to `has_checker_visible_limitations` would tighten the semantics.
  Not a required closure for current scope.
next_authorized_action: decision input only; no patch required for this finding
patch_queue_entry: not authorized
```

---

### F-06 — `access_failure_visible` limitation type name implies acceptability

```yaml
finding_id: F-06
severity: informational
target: orca-harness/source_observability/models.py
location: models.py line 47
```

**Evidence:**

```python
limitation_type: Literal[
    "source_language_anchor_missing",
    "media_not_preserved",
    "archive_body_not_retrieved",
    "access_failure_visible",
    "access_failure_context_missing",
    "unnoted_non_preserved_posture",
]
```

`"access_failure_visible"` uses "visible" to mean "the failure has locator and
cutoff context." The contrast with `"access_failure_context_missing"` could lead
consumer code to treat `access_failure_visible` as "accounted for and OK" while
treating `access_failure_context_missing` as the actionable gap.

Both types are `SourceObservabilityLimitation` entries in `result.limitations`.
Both represent access failures; neither is a success or a clean state. The naming
hierarchy suggests a quality gradient that doesn't exist in the model semantics.

The checker detail string for this type reads: "Access failure is visible with
locator and cutoff context." — which is accurate, but the type name alone could
encourage misuse.

```yaml
minimum_closure_condition: >
  Informational only. No correctness bug. Renaming to
  "access_failure_context_present" or "access_failure_located" would
  remove the acceptability implication. Not a required closure for current scope.
next_authorized_action: decision input only; no patch required for this finding
patch_queue_entry: not authorized
```

---

### F-07 — `source_structure_posture` has no dedicated checker rule

```yaml
finding_id: F-07
severity: informational
target: orca-harness/source_observability/checker.py
location: checker.py — coverage gap for source_structure_posture
```

**Evidence:**

The model captures `source_structure_posture: ObservablePosture` as a first-class
field, mapping to the RQ-01 structure-preservation obligation. The checker defines
dedicated functions for:

- source language (`_check_source_language`)
- media (`_check_media`)
- archive body (`_check_archive_body`)
- access failure (`_check_access_failure`)

No `_check_source_structure()` exists. Structure posture is only surfaced through
`_check_unnoted_non_preserved_postures` if `limitation_notes` is empty.

RQ-01 treats language and structure as peer obligations: "Capture records whether
the source language is preserved..." and "Capture records whether visible source
structure is preserved..." The checker makes language anchor-checkable
(via `source_language_anchor_required`) but has no parallel structure-specific
trigger (no `source_structure_anchor_required` or equivalent).

**Impact:** Structure posture is visible in the record but no checker rule enforces
or flags structure-specific conditions. If a caller marks `source_structure_posture`
as non-preserved but does include a limitation note (for any reason), the structure
gap is silently passed over.

This may be intentional for the current RQ scope (requirements scoping does not
mandate a structure-checker rule at v0), but the asymmetry between model field
coverage and checker rule coverage is notable.

```yaml
minimum_closure_condition: >
  Informational only. No current requirement mandates a structure-specific check.
  If a later requirements pass adds a structure-anchor requirement parallel to
  source_language_anchor_required, this gap would become a correctness issue.
  Document the gap as a known limitation if the structure field is expected to
  gain a dedicated rule.
next_authorized_action: decision input only; no patch required for this finding
patch_queue_entry: not authorized
```

---

### F-08 — Contract test cannot catch dynamic imports

```yaml
finding_id: F-08
severity: informational
target: orca-harness/tests/contract/test_source_observability_no_runtime_imports.py
location: lines 29-40
```

**Evidence:**

The test uses `ast.walk()` to find `ast.Import` and `ast.ImportFrom` nodes. This
correctly catches all static import statements at any scope depth (top-level,
inside functions, inside conditionals). It does not check for:

- `importlib.import_module("requests")`
- `__import__("requests")`
- `exec("import requests")`

No dynamic imports are present in the current implementation. The practical risk
is low. But the test's implicit guarantee is "no static import of forbidden modules"
not "no runtime acquisition possible."

```yaml
minimum_closure_condition: >
  Informational only. No dynamic imports exist. The gap matters only if future
  development introduces dynamic import patterns. Acceptable as-is for a helper
  of this scope.
next_authorized_action: decision input only; no patch required for this finding
patch_queue_entry: not authorized
```

---

### F-09 — No cross-field validation for `archive_body_expected=True` combined with `posture=NOT_APPLICABLE`

```yaml
finding_id: F-09
severity: informational
target: orca-harness/source_observability/models.py and checker.py
location: models.py line 34 (archive_body_expected), checker.py lines 73-84
```

**Evidence:**

`_check_archive_body` fires a limitation when `archive_body_expected=True` AND
`archive_body_posture != PRESERVED`. `NOT_APPLICABLE` is not `PRESERVED`, so
a record with `archive_body_expected=True, archive_body_posture=NOT_APPLICABLE`
triggers `archive_body_not_retrieved` with detail "Archive body content is expected
but not visibly retrieved."

`NOT_APPLICABLE` semantically means the field does not apply to this source type.
The combination `expected=True` + `NOT_APPLICABLE` is self-contradictory: if
archive body is expected, the posture cannot correctly be NOT_APPLICABLE.

The model does not validate this cross-field consistency. The checker emits a
technically correct limitation (the posture is non-preserved) but the limitation
detail is misleading — it implies retrieval was attempted and failed, while the
posture says the field is inapplicable.

The same contradiction applies to `media_required=True` + `media_posture=NOT_APPLICABLE`.

```yaml
minimum_closure_condition: >
  Informational only. No current test exercises this contradiction. A model
  validator could reject the combination, or the checker could detect and
  emit a clearer limitation type. Not a required closure for current scope.
next_authorized_action: decision input only; no patch required for this finding
patch_queue_entry: not authorized
```

---

## Boundary Violation Scan

| Authorized restriction | Evidence checked | Violation? |
| --- | --- | --- |
| No source acquisition | All imports in `source_observability/*.py` checked; only `pydantic`, `enum`, `typing`, `schemas.case_models` | None |
| No runtime/browser/API/scraper | Contract test AST scan + manual read; no network imports | None |
| No ECR/Cleaning/Judgment design | Model and function names reviewed; no downstream-layer vocabulary | None |
| No schema/storage design | No database, serialization, or storage imports or field definitions | None |
| No validation or readiness claims | `has_visible_limitations` is checker-scoped; no "pass/ready/valid" claim found | None |
| Reports visible limitations only | All checker outputs are `SourceObservabilityLimitation` entries; no quality scores | None |
| README boundary correct | README explicitly names all forbidden behaviors | None |

**Boundary verdict: no boundary violation found.**

---

## Review Questions — Responses

**Q1. Does the helper remain local and deterministic, with no acquisition/runtime behavior?**

Yes. All imports are local project modules or standard library/pydantic. The
contract test correctly blocks the known acquisition library roots. F-03 is a
gap in one urllib import form, but no urllib import is present in the current code.

**Q2. Does any model or checker name imply validation, readiness, scoring, source quality, or downstream Judgment?**

No names imply those downstream semantics. F-05 notes that `has_visible_limitations=False`
could be misread as a clean state, but this is a naming precision concern, not a
true scope claim in the model or checker logic.

**Q3. Are the posture values complete enough for RQ-01 through RQ-05 without overbuilding?**

The seven values (PRESERVED, PARAPHRASED, POINTER_ONLY, INACCESSIBLE, FAILED,
NOT_ATTEMPTED, NOT_APPLICABLE) cover the vocabulary described in RQ-01 through
RQ-05. No extra states are introduced. One minor gap: RQ-02 mentions "unavailable"
as a distinct concept — INACCESSIBLE is a reasonable mapping, and the
`ACCESS_FAILURE_POSTURES` set covers both INACCESSIBLE and FAILED, which is
appropriate.

**Q4. Does `_check_unnoted_non_preserved_postures` create noisy or misleading limitations?**

Yes — in two ways:

1. F-01: it can be silenced by empty strings in `limitation_notes`, creating a
   false-pass.
2. F-02: when a dedicated check has already fired for a posture field (e.g.,
   `access_posture` via `_check_access_failure`), the unnoted check can also fire
   for the same field if `limitation_notes` is empty, producing double-reported
   limitations.

**Q5. Does the access-failure logic preserve visible limitation semantics without treating failure as success?**

Yes — both `access_failure_visible` and `access_failure_context_missing` are
limitation entries in `result.limitations`. Neither is a success state. F-06
is a naming precision note, not a semantic error: both types are failures.

**Q6. Are tests strong enough to catch regression into runtime acquisition, schema design, or fake-pass behavior?**

The contract test (F-03) has one import-form gap for `from urllib import request`.
The unit tests have an anchor-count boundary gap (F-04) and do not cover the
F-01 empty-string false-pass or the F-02 double-reporting case.

The posture vocabulary boundary test (`test_posture_values_are_bounded`) is
correctly narrow and effective for its stated purpose.

**Q7. Does README wording correctly bound this as support/checking only?**

Yes. The README explicitly names all forbidden behaviors (no acquisition, no
archive retrieval, no browser/API, no source quality scoring, no validation,
no ECR/Cleaning/Judgment authorization). The boundary description is accurate.

---

## Findings Summary Table

| ID | Severity | Location | Issue |
| --- | --- | --- | --- |
| F-01 | **Major** | `checker.py:114` | Empty-string in `limitation_notes` silences unnoted-posture check; false-pass path |
| F-02 | Advisory | `checker.py:87-134` | Double-reporting: dedicated check + unnoted check both fire for same posture when `limitation_notes=[]` |
| F-03 | Advisory | `test_no_runtime_imports.py:37-40` | Contract test misses `from urllib import request` import form |
| F-04 | Advisory | `test_source_observability_checker.py` | No test for `anchor_required=True, posture=PRESERVED, anchor_count=0` boundary |
| F-05 | Informational | `models.py:59-61` | `has_visible_limitations=False` could be read as "source clean" |
| F-06 | Informational | `models.py:47` | `access_failure_visible` type name implies acceptability |
| F-07 | Informational | `checker.py` — gap | `source_structure_posture` has no dedicated checker rule |
| F-08 | Informational | `test_no_runtime_imports.py:29-40` | Contract test cannot catch dynamic imports |
| F-09 | Informational | `models.py:34`, `checker.py:73-84` | No cross-field validation for `archive_body_expected=True` + `posture=NOT_APPLICABLE` |

**Total findings: 9 (1 major, 3 advisory, 5 informational)**
**Boundary violations: 0**

---

## Validation Evidence Reported by Implementer

Per the review commission, the implementer reported:
- Targeted tests (6 tests): passed in 0.33s
- Full harness suite (31 tests): passed in 4.50s
- Direct trailing-whitespace scan over touched files: no hits

This review treats that evidence as consistent with the source read. The passing
test results do not contradict the findings: F-01, F-02, F-04 are gaps in test
coverage, not failures of existing tests.

---

## Non-Claims

This review is not:
- validation of the source-observability helper
- readiness claim for any downstream use
- approval or sign-off for production use
- Data Capture Spine validation
- mandatory remediation instruction
- patch authority
- ECR, Cleaning, or Judgment design input
- source-of-truth promotion
- source-access method authorization

Findings are decision input only. Patch execution requires separate owner
authorization.

---

## Minimum Closure Conditions Summary

| Finding | Minimum closure condition |
| --- | --- |
| F-01 | Fix empty-string false-pass in `limitation_notes` guard; cover with test |
| F-02 | Clarify intended double-reporting behavior; add test asserting expected count |
| F-03 | Add `from urllib import request` to contract-test coverage |
| F-04 | Add test for `anchor_required=True, posture=PRESERVED, anchor_count=0` |
| F-05 | Informational — no required closure; naming improvement optional |
| F-06 | Informational — no required closure; naming improvement optional |
| F-07 | Informational — no required closure; note as known gap if structure rule planned |
| F-08 | Informational — no required closure |
| F-09 | Informational — no required closure; model validator optional |
