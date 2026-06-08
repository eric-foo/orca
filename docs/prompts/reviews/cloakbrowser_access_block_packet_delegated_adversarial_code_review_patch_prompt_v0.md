# CloakBrowser Access-Block Packet Delegated Adversarial Code Review-And-Patch Prompt v0

## Commission

You are the de-correlated controller for a bounded adversarial code review-and-patch pass. The author/home model family is OpenAI/Codex. The controller must be a different vendor or family. This is a who-constraint, not a model recommendation.

Your task is to review and, only if needed, patch the CloakBrowser access-block packet preservation change. Your output is decision input for CA adjudication; it is not approval, readiness, or auto-keep authority.

## Required Method Sequence

1. Read this prompt.
2. REFERENCE-LOAD `workflow-deep-thinking`.
3. REFERENCE-LOAD `workflow-code-review`.
4. Do not APPLY either method yet.
5. SOURCE-LOAD the target files and required context below.
6. Declare `SOURCE_CONTEXT_READY` or `SOURCE_CONTEXT_INCOMPLETE`.
7. APPLY `workflow-deep-thinking` to frame the highest-risk failure modes.
8. APPLY `workflow-code-review` to review the implementation.
9. If a bounded fix is needed, patch only the submitted scope.
10. Fresh-read the changed target files and rerun the required validation.
11. Return findings first, then patch summary, diff, validation evidence, residual risk, and verdict.

## Source Context

Required reads:

- `AGENTS.md`
- `.agents/workflow-overlay/README.md`
- `.agents/workflow-overlay/decision-routing.md`
- `.agents/workflow-overlay/review-lanes.md`
- `.agents/workflow-overlay/delegated-review-patch.md`
- `docs/product/source_capture_toolbox/README.md`
- `orca-harness/docs/source_capture_agent_runbook.md`
- `orca-harness/source_capture/adapters/cloakbrowser_snapshot.py`
- `orca-harness/runners/run_source_capture_cloakbrowser_packet.py`
- `orca-harness/tests/unit/test_source_capture_cloakbrowser_snapshot.py`
- `orca-harness/tests/contract/test_source_capture_cloakbrowser_snapshot_contract.py`

Optional context if needed:

- `orca-harness/source_capture/adapters/direct_http.py`
- `orca-harness/runners/run_source_capture_http_packet.py`
- `orca-harness/tests/unit/test_source_capture_direct_http.py`

## Observed Implementation Context

The previous CloakBrowser path connected through Decodo successfully for `https://example.com/`, proving the proxy profile and CloakBrowser launch path could work for a neutral target. The Reddit guarded run still failed with:

```text
cloakbrowser_access_blocked: CloakBrowser snapshot reached an access-block/interstitial page instead of source content: reddit_network_security_block
```

The failure was diagnosed as target-side access blocking after navigation, not proxy authentication failure. Before this patch, the adapter had already rendered DOM/text/screenshot for the block page, but returned `CloakBrowserSnapshotFailureKind.ACCESS_BLOCKED`; the runner then exited without writing a packet. That made CloakBrowser less inspectable than Direct HTTP, which already writes packets for HTTP `403 Blocked` responses and marks them `access_failed`.

The current patch changes the behavior so rendered access-block pages become packetable `CloakBrowserSnapshotSuccess` values with:

- `access_block_reason: str | None`;
- metadata fields `access_blocked` and `access_block_reason`;
- a limitation beginning with `access_failed`;
- runner access posture beginning with `cloakbrowser_snapshot access_failed with access block ...`;
- a receipt summary that says source content was not captured.

This is packet preservation, not access success. The reviewer should be hostile to any wording, exit semantics, metadata, or test shape that could let a blocked Reddit interstitial become a usable source-content claim.

Validation observed before this review commission:

```powershell
$env:PYTHONDONTWRITEBYTECODE=1; python -m pytest -p no:cacheprovider -q --basetemp orca-harness\_pytest_tmp_cloakbrowser_patch orca-harness\tests\unit\test_source_capture_cloakbrowser_snapshot.py
```

Observed output:

```text
.............................                                            [100%]
```

```powershell
$env:PYTHONDONTWRITEBYTECODE=1; python -m pytest -p no:cacheprovider -q --basetemp orca-harness\_pytest_tmp_cloakbrowser_contract orca-harness\tests\contract\test_source_capture_cloakbrowser_snapshot_contract.py
```

Observed output:

```text
...                                                                      [100%]
```

## Review Target

Editable scope:

- `orca-harness/source_capture/adapters/cloakbrowser_snapshot.py`
- `orca-harness/runners/run_source_capture_cloakbrowser_packet.py`
- `orca-harness/tests/unit/test_source_capture_cloakbrowser_snapshot.py`
- `orca-harness/tests/contract/test_source_capture_cloakbrowser_snapshot_contract.py`

Read-only context:

- all other files.

Do not edit:

- live capture outputs under `orca-harness/_test_runs/`;
- proxy profile files or credentials;
- Reddit parser, consolidation, quality, candidate intake, monitoring, crawler, archive, or commercial API code;
- product docs or prompt artifacts outside this prompt;
- unrelated packet schema or source-quality code.

## Review Questions

Find material bugs, false-success paths, or provenance drift in the current patch. Focus especially on:

1. Whether a rendered Reddit access-block page now always writes an inspectable packet without hiding that source content was not captured.
2. Whether exit code `0` for packet-written blocked captures is consistent with runner semantics and cannot be misread as source-content success by nearby code or operators.
3. Whether the new `access_block_reason` field and metadata stay non-secret-bearing and do not create schema drift that breaks existing success paths.
4. Whether access-block artifacts are size-capped before packet writing and still clean up staging files on metadata/write failure.
5. Whether receipt summary, access posture, limitations, and non-claims are strong enough to prevent downstream consolidation, quality, ECR, Cleaning, Judgment, buyer-proof, or commercial-use claims.
6. Whether the tests would fail under the old behavior and prove the new blocked-packet behavior without live network access.
7. Whether any off-scope design issue should be returned as `NEEDS_ARCHITECTURE_PASS` instead of patched.

## Patch Boundary

If you patch, keep it to the editable scope. Patch only defects that materially affect access-block packet preservation, false-success prevention, provenance, or directly adjacent tests.

If the correct fix requires changing packet schema doctrine, source-quality vocabulary, Reddit consolidation behavior, archive fallback policy, proxy profile policy, live CloakBrowser launch strategy, or commercial API routing, return `NEEDS_ARCHITECTURE_PASS` or an off-scope finding instead of patching those files.

## Required Validation

Run this exact focused slice after any patch, or state why it could not be run:

```powershell
$env:PYTHONDONTWRITEBYTECODE=1; python -m pytest -p no:cacheprovider -q --basetemp orca-harness\_pytest_tmp_cloakbrowser_review orca-harness\tests\unit\test_source_capture_cloakbrowser_snapshot.py orca-harness\tests\contract\test_source_capture_cloakbrowser_snapshot_contract.py
```

Do not perform live Reddit network access. Do not spend proxy traffic.

## Output Path

Write the review result to:

`docs/review-outputs/cloakbrowser_access_block_packet_delegated_adversarial_code_review_patch_v0.md`

## Output Contract

Return:

1. `SOURCE_CONTEXT_READY` or `SOURCE_CONTEXT_INCOMPLETE`.
2. Findings first, ordered by severity.
3. For each finding: affected file/line, evidence, risk, minimum closure condition, and whether you patched it.
4. Patch summary, if any.
5. Unified diff.
6. Validation command and observed output, or not-run reason.
7. Residual risk.
8. Verdict: `PATCHED_FOR_CA_ADJUDICATION`, `NO_PATCH_NEEDED_FOR_CA_ADJUDICATION`, `NEEDS_ARCHITECTURE_PASS`, or `BLOCKED`.

Reminder: your diff and verdict are claims to adjudicate, not premises to inherit. CA/home model decides what is kept.
