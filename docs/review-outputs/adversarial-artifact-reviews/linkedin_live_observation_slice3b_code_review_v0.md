```yaml
retrieval_header_version: 1
artifact_role: Review-output record (cross-vendor code review + home-model adjudication + same-vendor recheck)
scope: >
  Durable audit record of the adversarial CODE review of slice 3b -- the
  LiveObservation contract record + validate_live_observation (the §6.2
  minimization-boundary seam, no runtime, no projection). Advisory throughout;
  not a verdict.
authority_boundary: retrieval_only
reviewed_artifact: capture_spine/linkedin_live_adapter/{models,validation,__init__}.py (LiveObservation) + tests/unit/test_linkedin_live_adapter.py
input_bundle: docs/review-outputs/linkedin_live_observation_slice3b_v0_no_repo_review_bundle.zip (PRE-fix code GPT-5.5 reviewed)
implements: docs/product/data_capture_spine_linkedin_live_layer_architecture_v0.md (ADR §6.2 / §8 slice-3b)
provenance:
  authored_by: anthropic/claude-opus-4.x
  reviewed_by: openai/gpt-5.5 (advisory, no-repo; reconstructed the package, ran tests: 26 passed pre-fix)
  same_vendor_recheck: anthropic/sonnet (clean)
  de_correlation_bar: cross_vendor_discovery
```

# LinkedIn live-observation slice 3b — Cross-Vendor Code Review + Adjudication (v0)

## Outcome
4 findings (3 major, 1 minor). The reviewer confirmed the shape is narrow and the extraction sound, but caught that the §6.2 minimization claim was **overstated**. Adjudication: **4/4 accepted + patched.** Same-vendor recheck: **clean. 93 pass.**

| # | Sev | Finding (GPT-5.5) | Adjudication + fix |
|---|-----|-------------------|--------------------|
| F1 | major | Free-text allowed fields can carry forbidden *content* despite named-fields-only + flags + walk (the "cannot carry over-captured state" claim is overstated) | **ACCEPT** — softened the claim (3b is the *structural* boundary + length caps; full content minimization is the **3c runtime tape-test**); added length caps on the free-text fields. Honest residual: small forbidden content (an email in a basis field) is **3c's** job, not 3b's. |
| F2 | major | `person_data_minimized="no"` passed for person observations | **ACCEPT** — the observation IS the minimization seam, so person observations now require exactly `"yes"` (`"no"`/`"not_applicable"` raise `person_data_not_minimized`). |
| F3 | major | Posture is an unchecked `live_access_id` reference; the validator doesn't bind the `LiveAccessEnvelope` | **ACCEPT, deferred to 3b-2** — binding (matching ids/run_id + a validated envelope) IS the mint-path, deferred. Fixed the 3b-1 **overclaim**: `validate_live_observation` is the *shape* gate, not the full posture gate; not safe standalone. No binding function now. |
| F4 | minor | Tests miss the smuggling path + don't pin error codes | **ACCEPT** — added the over-capture + `"no"` negatives, both asserting `LinkedInLaneError.code`. |

## Same-vendor recheck (Sonnet)
All 4 `closed`; the 512-char cap does not false-positive on legitimate minimized values; the residual (3b structural + length, 3c content) is honestly scoped; the F3 honesty fix is accurate (no binding overclaim). The `person_data_minimized` dataclass default `"not_applicable"` is safe-by-design (the validator rejects it for persons). Verdict: clean.

## Boundary
Advisory only. Not approval/validation/readiness/live-runner/commercial authorization. Claim: "module + tests pass" (93). Two scoped deferrals remain by design: **full content-level read-time minimization = slice 3c** (the runtime tape-test); **observation↔envelope posture binding = slice 3b-2** (the mint-path).
```
