```yaml
retrieval_header_version: 1
artifact_role: Review-output record (cross-vendor code review + home-model adjudication + same-vendor recheck)
scope: >
  Durable audit record of the adversarial CODE review of LinkedIn live-adapter
  slice 3a (LiveAccessEnvelope contract record + validator). Captures the
  cross-vendor findings, the home-model adjudication (accept/modify/reject +
  source verification + the patch), and the same-vendor closure recheck.
  Advisory throughout; not a verdict.
authority_boundary: retrieval_only
reviewed_artifact: capture_spine/linkedin_live_adapter/{models,validation,__init__}.py + tests/unit/test_linkedin_live_adapter.py
input_bundle: docs/review-outputs/linkedin_live_adapter_slice3a_v0_no_repo_review_bundle.zip (contains the PRE-patch code GPT-5.5 reviewed)
implements: docs/product/data_capture_spine_linkedin_live_layer_architecture_v0.md (ADR §8 slice 3a)
provenance:
  authored_by: anthropic/claude-opus-4.x
  reviewed_by: openai/gpt-5.5 (advisory, no-repo; ran the included tests: 13 passed pre-patch)
  same_vendor_recheck: anthropic/sonnet (clean)
  de_correlation_bar: cross_vendor_discovery
```

# LinkedIn live-adapter slice 3a — Cross-Vendor Code Review + Adjudication (v0)

## Outcome
2 findings (both major); **2/2 accepted + patched**; same-vendor recheck **clean**; **69 passed** (15 adapter + 54 core, no regression). The reviewer also confirmed the core gate solid: no hollow tests, no truthiness bypass, no forbidden-field bypass, one-way-import isolation holds, no runtime, smallest-complete holds.

## Findings + adjudication

| # | Sev | Finding (GPT-5.5) | Adjudication (CA) | Fix |
|---|-----|-------------------|-------------------|-----|
| F1 | major | `_is_negated` accepts a syntactically-negated, semantically-positive claim (`"not only live access; it also authorizes it"`) as disclaiming a hard-stop category — a fake-success path | **ACCEPT** (verified by probe) | `_is_negated` now requires a leading `not `/`no ` AND rejects expansive/reversal markers (`only, merely, also, "as well", "but ", however, except`); loose mid-string `" not "` branch removed. Residual (multi-clause inversion) documented; canonical-allowlist deferred. |
| F2 | major | POC-risk consistency is one-way (`autonomous ⟹ flag`); ADR §8 says `⟺`, so `attended_manual + flag=True` passes | **ACCEPT** (verified) | Added the reverse predicate (`flag=True ⟹ autonomous`, else `poc_risk_mode_overattested`) — now genuinely iff, no POC over-attestation on the manual mode. |

Two new negative tests added (`test_reversal_negation_does_not_satisfy_category_raises`, `test_poc_flag_on_manual_mode_raises`).

## Same-vendor recheck (Sonnet)
Both `closed`. All 11 default non_claims still pass the new marker filter (no false-positive); all four iff quadrants enforced + tested; no new issue introduced. Noted `"except"` as a theoretical over-rejection marker — CA kept it as fail-closed-correct (an exception-carved disclaimer is not a clean hard-stop disclaimer; no default trips it). Verdict: clean.

## Follow-up (out of slice scope)
Slice-2 `linkedin_graph_frontier/validation.py` `_is_negated` shares the F1 reversal weakness. NOT fixed here (core; separate ask) — spawned as a follow-up task. Apply the same tightening + a negative test there.

## Boundary
Advisory only. Not approval, validation, readiness, live-runner, or commercial authorization. Claim made: "the slice-3a module + its tests pass" (69 passed). The accepted contract is the ADR §8; this record is the slice's review provenance.
```
