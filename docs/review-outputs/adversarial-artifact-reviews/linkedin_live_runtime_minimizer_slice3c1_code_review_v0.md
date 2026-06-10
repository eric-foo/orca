```yaml
retrieval_header_version: 1
artifact_role: Review-output record (two-round cross-vendor code review + home-model adjudication)
scope: >
  Durable audit record of the adversarial CODE review of slice 3c-1 -- the no-live
  read-time minimizer (linkedin_live_runtime) + the completion of the §6.2 observation
  gate it relies on (validate_live_observation). Two cross-vendor rounds (v0, v1); no
  same-vendor recheck (skipped per calibration -- home model verified instead).
  Advisory throughout; not a verdict.
authority_boundary: retrieval_only
reviewed_artifact: capture_spine/linkedin_live_runtime/{minimizer,__init__}.py + capture_spine/linkedin_live_adapter/validation.py (validate_live_observation) + tests/unit/{test_linkedin_live_runtime,test_linkedin_live_adapter}.py
input_bundles:
  - docs/review-outputs/linkedin_live_runtime_minimizer_slice3c1_v0_no_repo_review_bundle.zip (blob 51a0e9b2; PRE-fold)
  - docs/review-outputs/linkedin_live_runtime_minimizer_slice3c1_v1_no_repo_review_bundle.zip (blob 3b0a099a; the fold)
implements: docs/product/data_capture_spine_linkedin_live_layer_architecture_v0.md (§6.2 minimization boundary; slice 3c-1 = the no-live runtime half)
provenance:
  authored_by: anthropic/claude-opus-4.x
  reviewed_by: openai/gpt-5.5 (advisory, no-repo; two rounds; ran the bundles -- 7 then 58 passed)
  same_vendor_recheck: not_run (skipped per calibration -- the v1 fix is a 2-line completeness patch that itself came from a cross-vendor finding; home model verified field coverage from source instead)
  de_correlation_bar: cross_vendor_discovery
```

# LinkedIn live-runtime minimizer slice 3c-1 — Cross-Vendor Code Review + Adjudication (v0)

## What 3c-1 is
The NO-LIVE half of the live runtime: a pure `raw_capture (over-captured field bag) ->
minimized LiveObservation` transform (`minimize_capture_to_observation`), default-deny
(carry only named fields; force the boundary flags safe), validating its output against
the §6.2 observation gate. Fixtures only; no browser, no LinkedIn access. The live
fetcher (3c-2) stays behind the legal/ToS gate.

## Outcome
Two cross-vendor rounds, all findings accepted + closed; **125 lane tests pass** (no
same-vendor recheck -- skipped per calibration; home model verified instead). The fix
was folded into the observation gate (the durable home), so it hardens both the
minimizer and the 3b-2 projection (both run the gate).

| Round | # | Sev | Finding (GPT-5.5) | Adjudication + fix |
|-------|---|-----|-------------------|--------------------|
| v0 | F1 | major | Carried-but-unchecked smuggle: the minimizer carries every LiveObservation field, but `validate_live_observation` only capped 5 free-text + 2 influence fields -- `minimization_rule`, `observed_source_surface`, `person_data_minimized`, the ids, `provenance_timestamp`, `exclusions` could carry content | **ACCEPT (verified).** **Folded into the gate** (not band-aided in the minimizer): closed-enum (source_surface / minimization_rule / person_data_minimized), safe-id (3 ids), ISO-UTC timestamp shape; minimizer forces `exclusions` safe. |
| v1 | F1 | major | `exclusions` still carried-but-unchecked **at the gate** for direct (non-minimizer) callers -- the fold's completeness claim was incomplete | **ACCEPT (verified).** Gate now rejects non-empty `exclusions` (allows empty/missing). Closes the path for any caller, not only the minimizer. |
| v1 | F2 | minor | Timestamp regex was `Z`-only, false-rejecting legitimate UTC `+00:00` (e.g. `datetime.isoformat()`) | **ACCEPT (verified).** Regex now accepts `Z` or `+00:00`; still rejects non-UTC offsets (`+05:00`) and prose. |

## Home-model adjudication notes
- The v0 fix was deliberately placed at `validate_live_observation` (the observation
  contract), not duplicated in the minimizer -- this is the second time that gate was
  found incomplete (3b-2 F1 was the influence fields), so it was completed
  systematically. The minimizer keeps only the minimization-specific `exclusions` drop.
- v1 F1 was the home model's own over-claim ("complete gate") caught by the reviewer:
  `exclusions` was handled only at the minimizer, not the gate. Now closed at the gate.
- `exclusions` is forced empty at the gate; a future structured exclusion receipt would
  need its own bounded validation there (recorded residual).
- The v1 patch was applied externally on the shared worktree; the home model verified
  the applied result (correct checks, pinned tests sound, 125 pass).

## Home-model verification (no same-vendor recheck)
No separate Sonnet recheck was run -- skipped per the calibration for a 2-line
completeness patch that itself came from a cross-vendor finding. Instead the home model
verified against source: every carried `LiveObservation` field falls into a guarded
bucket (closed-enum / capped / influence-guarded / safe-id / timestamp-shaped /
boundary-flag-False / forced-empty / schema-fixed) -- no carried field is unprotected;
the timestamp regex accepts `Z` and `+00:00` (and fractional seconds) and rejects
non-UTC offsets like `+05:00` and prose; `exclusions` rejects non-empty and allows
empty/missing (the `.to_dict()` `[]` path). Full lane: 125 pass, no regression.

## Boundary
Advisory only. Not approval / validation / readiness / live-runner / commercial
authorization. Claim: "module + tests pass" (125 lane). The gate now structurally
forbids carried free narrative; small content inside a capped free-text field remains
the slice-3c *runtime* read-time-minimization concern, not this contract gate. The live
fetcher (3c-2) stays behind the legal/ToS hard gate.
