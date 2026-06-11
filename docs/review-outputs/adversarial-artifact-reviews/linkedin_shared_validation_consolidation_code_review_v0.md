```yaml
retrieval_header_version: 1
artifact_role: Review-output record (cross-vendor code review + home-model adjudication + same-vendor recheck)
scope: >
  Durable audit record of the adversarial CODE review of the LinkedIn-lane
  validation-helper consolidation (extract shared_validation.py; reconcile the
  drifted non_claims check + excluded-basis markers to the stronger/superset
  form; close slice-1 F4). Advisory throughout; not a verdict.
authority_boundary: retrieval_only
reviewed_artifact: >
  capture_spine/linkedin_lane/shared_validation.py (new) + the retrofitted
  validators (linkedin_lane/validation.py + __init__.py,
  linkedin_graph_frontier/validation.py, linkedin_live_adapter/validation.py) +
  tests/unit/test_linkedin_lane.py
input_bundle: docs/review-outputs/linkedin_shared_validation_consolidation_v0_no_repo_review_bundle.zip (PRE-fix code GPT-5.5 reviewed)
provenance:
  authored_by: anthropic/claude-opus-4.x
  reviewed_by: openai/gpt-5.5 (advisory, no-repo; reconstructed the package + ran tests: 72 passed pre-fix)
  same_vendor_recheck: anthropic/sonnet (clean)
  de_correlation_bar: cross_vendor_discovery
```

# LinkedIn shared-validation consolidation — Cross-Vendor Code Review + Adjudication (v0)

## Outcome
4 findings (3 major, 1 minor). The reviewer confirmed the **extraction is sound** (imports acyclic; slice-1 negatives non-hollow; 72 pass). Adjudication: **2 fixed in-scope (F3, F4), 2 accepted-valid-but-pre-existing (F1, F2) → follow-ups.** Same-vendor recheck of the fixes: **clean. 73 pass.**

| # | Sev | Finding | Adjudication | Disposition |
|---|-----|---------|--------------|-------------|
| F3 | major | Shared `is_negated` reversal markers over-broad — a benign `"not live access; only planning"` wrongly failed (false-positive) | **ACCEPT** — real bug in the new shared logic | **Fixed:** detect reversal by leading construction (`not only`/`not merely`/`not just`/`no mere`), not substring-anywhere. Demonstrated reversal still caught; benign compound passes. Guard test added. Residual (`not X but Y` mid-clause) documented + recheck-judged acceptable for this declared-posture field. |
| F4 | minor | 2 forbidden-field tests hollow — `reject_unknown_keys` fired before the walk, so they raised on unknown-key not forbidden-walk | **ACCEPT** (pre-existing, in a touched file) | **Fixed:** the 2 tests now nest the forbidden field under an allowed container, genuinely exercising the recursive walk. |
| F1 | major | `validate_run_envelope` never checks `schema_version` / closed enums (dataclass hints unenforced) → bogus `method_mode`/`candidate_classes` pass | **ACCEPT as valid, PRE-EXISTING** — the consolidation didn't touch RunEnvelope's enum-checking (behavior-preserving); not a refactor defect | **Follow-up** `task_0fc25eb2` (scope: separate hardening + tests). |
| F2 | major | `validate_graph_frontier_register` allowlists the inner wrapper but ignores unknown TOP-LEVEL sibling keys | **ACCEPT as valid, PRE-EXISTING** — predates the refactor (structure unchanged) | **Follow-up** `task_4f9e268a`. |

## Same-vendor recheck (Sonnet)
F3 + F4 both `closed`; defaults all still pass; no new issue introduced; the `not X but Y` / `definitely not X` lexical residuals are acceptable for a declared-posture, operator-controlled field (not an execution gate; the required-category + allowlist checks still catch missing/hollow non_claims). Verdict: clean.

## Boundary
Advisory only. Not approval, validation, readiness, live-runner, or commercial authorization. Claim: "the modules + their tests pass" (73 passed). This record is the consolidation's review provenance; F1/F2 remain open follow-ups.
```
