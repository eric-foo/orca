```yaml
retrieval_header_version: 1
artifact_role: Review-output record (cross-vendor code review + home-model adjudication)
scope: >
  Durable audit record of the adversarial CODE review of slice 3c-2a -- the attended
  capture HARNESS (the no-live runner skeleton: the Fetcher seam, the legal-gate-as-code
  in run_live_capture, the caps + fetch->minimize->validate->project wiring). One
  cross-vendor round. Advisory; not a verdict.
authority_boundary: retrieval_only
reviewed_artifact: capture_spine/linkedin_live_runtime/{fetcher,runtime}.py (+ __init__ exports) + capture_spine/linkedin_live_adapter/validation.py (caps fold) + tests/unit/test_linkedin_live_runtime_capture.py
input_bundle: docs/review-outputs/linkedin_live_runtime_capture_harness_slice3c2a_v0_no_repo_review_bundle.zip (blob e538e251)
implements: docs/product/data_capture_spine_linkedin_live_layer_architecture_v0.md (slice 3c-2a = the no-live capture harness)
provenance:
  authored_by: anthropic/claude-opus-4.x
  reviewed_by: openai/gpt-5.5 (advisory, no-repo; ran the bundle -- 16 passed)
  same_vendor_recheck: not_run (skipped per calibration -- a ~9-line caps-validator fold from a cross-vendor finding; home model verified)
  de_correlation_bar: cross_vendor_discovery
```

# LinkedIn live-runtime capture harness slice 3c-2a — Cross-Vendor Code Review + Adjudication (v0)

## What 3c-2a is
The no-live attended-capture HARNESS: the runner skeleton + the legal-gate-as-code.
`run_live_capture` refuses to run without explicit owner authorization
(`live_run_authorized`) + owner-present + a valid posture envelope + run envelope; it
then drives the injected `Fetcher` per target, minimizes (3c-1), validates, and projects
(3b-2), capped. Authorization model: the `LiveAccessEnvelope` stays posture-only
(`execution_authorized=False`); the live-run authorization is a SEPARATE explicit owner
arg. Offline (StubFetcher); the real `BrowserFetcher` (3c-2b) is the only live part,
gated, not here.

## Outcome
1 finding (major). The reviewer confirmed the gate is before any fetch, uses strict
`is not True` checks, and every returned row flows through minimize + project (validate)
before append. **1/1 accepted + folded.** No same-vendor recheck (small fold,
home-model verified). **137 lane tests pass.**

| # | Sev | Finding (GPT-5.5) | Adjudication + fix |
|---|-----|-------------------|--------------------|
| F1 | major | Cap values not validated before summing: `_resolve_cap` did `sum(int(v) ...)`, and `validate_live_access_envelope` only checked caps is a non-empty Mapping -- so `{"max_profiles": "2"}`, `{True}`, `{-1, ...}` rode through `int()` coercion, weakening the "cannot widen declared caps" guarantee | **ACCEPT (verified).** **Folded into the envelope gate** (standing fold-default): `validate_live_access_envelope` now requires each cap value to be a non-negative int (rejecting bool/str/negative), each name a non-empty string, and a positive total (`invalid_cap`). The runtime adds a `max_captures` type-check (rejecting bool/non-int) and trusts the gate-validated caps. |

## Home-model adjudication notes
- Per the standing default the owner set (consumer-found upstream-validator gaps fold
  into the owning validator), the caps validation went to `validate_live_access_envelope`
  (re-opening committed slice-3a), not the runtime. The runtime keeps only the
  `max_captures` arg check.
- Verified no false-reject: legit caps (`{max_profiles:25, max_searches:10}`) pass; a
  zero total is rejected.

## Boundary
Advisory only. Not approval / validation / readiness / live-runner / commercial
authorization. Claim: "module + tests pass" (137 lane). The harness is no-live
(StubFetcher only). The real attended `BrowserFetcher` (3c-2b) -- the only part that
touches LinkedIn -- stays behind the legal/ToS gate and is owner-validated; the live
path is owner-accepted POC-risk (ToS-gray, NOT "legally defensible").
