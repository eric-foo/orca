# CSB Scanning Artifact Checker CI Diff Gate Delegated Adversarial Code Review Prompt v0

```yaml
retrieval_header_version: 1
artifact_role: Review prompt
scope: >
  Filed route-out prompt for de-correlated adversarial implementation/code review
  of the CSB-first scanning artifact checker CI diff gate.
use_when:
  - Commissioning an independent reviewer to inspect PR #367's checker, tests, CI wiring, and scanning-doc contract updates.
  - Checking the prompt source, target revision, output binding, and de-correlation receipt for this review.
authority_boundary: retrieval_only
open_next:
  - .agents/workflow-overlay/prompt-orchestration.md
  - .agents/workflow-overlay/review-lanes.md
  - .agents/workflow-overlay/delegated-review-patch.md
  - .agents/workflow-overlay/source-loading.md
implementation_under_review: c4cc9e3e3cb0a6f1b647575fd18e12d0cc9950d1..aa331e53c13830a0e698c4af60980dd7aa0f09d0
prompt_carrier_note: >
  This prompt may be committed after the implementation commit. The implementation
  target under review ends at aa331e53c13830a0e698c4af60980dd7aa0f09d0; prompt-only
  carrier commits do not change the implementation target unless they modify the
  named target files.
stale_if:
  - Any named implementation target file changes after aa331e53c13830a0e698c4af60980dd7aa0f09d0 and before review.
  - The review-output destination already exists and the operator has not authorized a new version.
  - The receiving actor cannot inspect the named worktree or target commit in place.
```

## Orca Prompt Preflight

- Output mode: file-write review prompt; receiver output mode is `review-report` to `docs/review-outputs/csb_scanning_artifact_checker_ci_diff_gate_adversarial_code_review_v0.md`.
- Template kind: review. Orca-local `repo-code-review` template kind is unbound, so this uses the generic prompt-orchestrator review frame plus Orca overlay bindings.
- Edit permission, targets, branch: reviewer is read-only. Target worktree is `C:\Users\vmon7\Desktop\projects\orca\worktrees\scanning-artifact-enforcement-next`, branch `codex/scanning-artifact-enforcement-next`, implementation range `c4cc9e3e3cb0a6f1b647575fd18e12d0cc9950d1..aa331e53c13830a0e698c4af60980dd7aa0f09d0`. Dirty state allowed only for this prompt artifact or later prompt-carrier commits that do not touch target files.
- Reviews: findings-first. This is advisory implementation/code review unless a later Orca binding grants formal implementation-review authority. Do not emit formal PASS, readiness, mandatory remediation, or patch queue.
- Doctrine change: none intended by this prompt. It routes a review of a prior implementation change; it does not alter scanning, CSB, prompt, review, validation, Capture, Judgment, or product doctrine.
- Destinations: this prompt is the input artifact; the receiver writes the full report to `docs/review-outputs/csb_scanning_artifact_checker_ci_diff_gate_adversarial_code_review_v0.md`.

## Commission

Run an adversarial implementation/code review of PR #367's CSB-first scanning artifact checker CI diff gate. The implementation commit under review is `aa331e53c13830a0e698c4af60980dd7aa0f09d0` on branch `codex/scanning-artifact-enforcement-next`, with base `c4cc9e3e3cb0a6f1b647575fd18e12d0cc9950d1`.

This prompt was prepared after an explicit `workflow-delegated-review-patch` invocation, but the target is a multi-file implementation/code/CI diff. Per Orca `.agents/workflow-overlay/delegated-review-patch.md`, do not force this into the single-artifact delegated review-and-patch convention. Route it through implementation/code review instead. The reviewer is read-only and must not patch source files.

Review purpose:

1. Independently attack whether the new `check_csb_scanning_artifact.py --changed` / `--diff BASE` modes correctly detect changed CSB-first scanning artifacts without false-passing artifacts that should be gated.
2. Verify whether CI now protects changed `docs/research/*.md` CSB-first scan artifacts with the checker, without creating noisy or unsafe repo-wide failures.
3. Inspect tests and scanning doc updates for mismatch, stale doctrine, overclaiming, or false confidence.
4. Scan only the touched implementation scope for patch-caused or newly visible blocker/major issues. Minor findings are allowed, but do not widen into unrelated CSB, Capture, Judgment, crawler, research, product-proof, or runtime implementation review.

## Actor And De-Correlation Receipt

- author_home_model_family: OpenAI / GPT-family Codex, recorded from the authoring lane.
- controller_model_family: `operator_to_fill`; must be a different upstream vendor / model lineage from OpenAI to claim cross-vendor discovery.
- current_receiving_actor_role: controller.
- dispatch_mode: external-controller-courier.
- de_correlation_status: `operator_to_fill`; if controller model family is missing or same-vendor, return advisory findings only and do not claim cross-vendor discovery or no-new-seam.
- no runtime model recommendation is made by this prompt.

## Source-Gated Method Contract

1. REFERENCE-LOAD `workflow-deep-thinking` and `workflow-code-review` if available in your environment. Do not APPLY them yet.
2. Read the required Orca authority and target sources below.
3. Declare `SOURCE_CONTEXT_READY` or `SOURCE_CONTEXT_INCOMPLETE` with missing sources, conflicts, unavailable tools, and any target-file drift.
4. Only after source readiness, APPLY deep-thinking to frame material failure modes, then APPLY workflow-code-review to produce findings-first implementation/code review.
5. If `workflow-code-review` is unavailable, use its zero-config findings-only advisory semantics from the prompt text below, but mark strict review claims `NOT_CLAIMED`.

## Required Reads

Read these authority and boundary files first:

- `AGENTS.md`
- `.agents/workflow-overlay/README.md`
- `.agents/workflow-overlay/source-loading.md`
- `.agents/workflow-overlay/prompt-orchestration.md`
- `.agents/workflow-overlay/review-lanes.md`
- `.agents/workflow-overlay/delegated-review-patch.md`
- `.agents/workflow-overlay/validation-gates.md`
- `.agents/workflow-overlay/safety-rules.md`
- `.agents/workflow-overlay/source-of-truth.md`

Then read the review target:

- `.agents/hooks/check_csb_scanning_artifact.py`
- `.github/workflows/ci.yml`
- `orca-harness/tests/unit/test_csb_scanning_artifact_validator.py`
- `orca/product/spines/scanning/README.md`
- `docs/workflows/orca_repo_map_v0.md`

Read adjacent implementation and doctrine context as needed, but do not widen the review target:

- `orca/product/spines/scanning/scan_core/orca_scanning_intelligent_walk_mgt_operating_model_v0.md`
- `docs/research/orca_discovery_candidate_scan_imaginary_authors_core_satellite_csb_v0.md` if present in the worktree, as an example CSB-first scan artifact shape
- `docs/research/orca_discovery_candidate_scan_imaginary_authors_broad_scout_deep_scan_v0.md` if present in the worktree, as an example post-CSB scanning artifact shape
- adjacent tests or fixtures under `orca-harness/tests/fixtures/csb_scanning_artifacts/`

## Target Diff And Dirty-State Allowance

Implementation target range:

```text
c4cc9e3e3cb0a6f1b647575fd18e12d0cc9950d1..aa331e53c13830a0e698c4af60980dd7aa0f09d0
```

Observed target files in that range:

```text
M .agents/hooks/check_csb_scanning_artifact.py
M .github/workflows/ci.yml
M docs/workflows/orca_repo_map_v0.md
M orca-harness/tests/unit/test_csb_scanning_artifact_validator.py
M orca/product/spines/scanning/README.md
```

Use this command shape as the reviewed implementation diff:

```powershell
git diff c4cc9e3e3cb0a6f1b647575fd18e12d0cc9950d1..aa331e53c13830a0e698c4af60980dd7aa0f09d0 -- .agents/hooks/check_csb_scanning_artifact.py .github/workflows/ci.yml docs/workflows/orca_repo_map_v0.md orca-harness/tests/unit/test_csb_scanning_artifact_validator.py orca/product/spines/scanning/README.md
```

If the branch contains a later prompt-only commit, verify whether the five target files above still match `aa331e53c13830a0e698c4af60980dd7aa0f09d0`. If they changed, report `SOURCE_CONTEXT_INCOMPLETE` or review the newer target only if the operator explicitly authorizes that retarget.

## Validation Evidence To Inspect

The author observed these checks after the implementation commit:

```powershell
python -B .agents\hooks\check_csb_scanning_artifact.py --selftest
python -B .agents\hooks\check_csb_scanning_artifact.py --changed --strict
python -B .agents\hooks\check_csb_scanning_artifact.py --diff origin/main --strict
python -B -m pytest -q -p no:cacheprovider tests\unit\test_commission_signal_board_output_validator.py tests\unit\test_csb_scanning_artifact_validator.py
python -B -m pytest -q -p no:cacheprovider
git diff --check
python -B .agents\hooks\check_retrieval_header.py --changed
python -B .agents\hooks\check_repo_map_freshness.py --changed
python -B .agents\hooks\check_map_links.py --strict
python -B .agents\hooks\check_placement.py --check
python -c "import pathlib,yaml; yaml.safe_load(pathlib.Path('.github/workflows/ci.yml').read_text()); print('ci yaml ok')"
```

Observed validation notes:

- `--selftest` exited 0 and printed `SELFTEST OK`.
- `--changed --strict` and `--diff origin/main --strict` exited 0 with `check_csb_scanning_artifact: no changed CSB-first scan artifacts detected`.
- Targeted pytest and full `orca-harness` pytest exited 0; full pytest had 3 skipped tests and an existing `PytestUnknownMarkWarning` for `pytest.mark.integration`.
- `git diff --check`, retrieval-header check, repo-map freshness, strict map-links, placement check, and CI YAML parse exited 0. `check_placement.py --check` printed existing repo-wide advisory placement/root noise unrelated to this patch.
- PR #367 CI readback showed `orca-harness-tests` completed successfully.

Because this implementation introduces or materially changes a validation hook/checker and CI gate, independently smoke-run the new or changed command under a child-scoped 30-second timeout before any full/repeated validation run:

```powershell
python -B .agents\hooks\check_csb_scanning_artifact.py --diff origin/main --strict
```

If the smoke probe times out, stop and return `VALIDATION_HOOK_TIMEOUT` with command, cwd, touched files, and observed process state. Do not invoke the same hung command again. If the smoke probe passes, run the normal validation commands you judge necessary. If you do not rerun a validation command, report that command as author-supplied and not independently revalidated.

Do not run live scanning, crawler behavior, capture, outreach, network source access, public web research, API/dashboard code, storage/Data Lake operations, product-proof checks, or Judgment readiness checks.

## Review Scope

Attack these questions:

- Does `--changed` correctly identify changed `docs/research/*.md` artifacts that look like CSB-first scan artifacts, including staged and unstaged changes, without requiring users to pass explicit paths?
- Does `--diff BASE` correctly identify changed scan artifacts in CI when run as `python .agents/hooks/check_csb_scanning_artifact.py --diff origin/main --strict`?
- Does auto-detection require enough CSB-first markers to avoid gating unrelated research artifacts, while not being so strict that real CSB-first scan artifacts bypass the checker?
- Do explicit path validations remain unchanged or at least not weakened by the new changed/diff discovery modes?
- Does the checker fail closed on malformed YAML, missing intake, missing broad-scout accounting, missing observations, missing closeout, capture-route overclaims, recency-as-proof overclaims, and graph-weight overclaims?
- Does the implementation avoid the prior false-pass patterns: null/empty `closeout_state`, broad-scout-return text-anywhere loopholes, missing section tests, empty broad-scout body, and duplicate `invalid_capture_route_binding_state` emission?
- Does the CI step run from a checkout state where `origin/main` exists and means the intended base branch? If not, does the command fail visibly rather than silently skipping validation?
- Could the CI step create false failures on PRs that do not touch scanning artifacts, or false passes on PRs that do?
- Are test fixtures and unit tests sufficient for changed-file detection boundaries, explicit path behavior, bad artifact shapes, and count/accounting checks?
- Does the scanning README accurately describe the gate as receipt-shape / lane-boundary enforcement only, without claiming candidate quality validation, proof, readiness, approval, or runtime scanning correctness?
- Does the repo-map update accurately classify the hook as portable plus CI diff-scoped without overclaiming source-of-truth promotion or validation coverage?
- Does any wording imply the checker authorizes Capture, binds capture routes, proves demand, validates candidate promotion, or replaces scan-core doctrine?
- Does the patch preserve Windows path behavior and repo-root execution behavior?

## Intended Enforcement Closure Check

Treat these enforcement goals as claims to verify, not accepted truth:

- E-01 changed-file discovery: `--changed` and `--diff BASE` find changed CSB-first scan artifacts by file path and marker shape.
- E-02 CI gate wiring: PR CI runs the checker against `origin/main` in strict diff mode.
- E-03 preservation of explicit validation: existing explicit path and selftest validation still works.
- E-04 scan-lane doctrine alignment: docs frame the checker as mechanical receipt enforcement, not quality proof, capture authorization, or candidate readiness.

For each, report one of:

- `closed`: implementation and tests now cover the failure mode.
- `partially_closed`: some protection exists but a material variant remains.
- `not_closed`: the original failure mode remains.
- `not_assessed`: source or environment prevented assessment.

If `partially_closed` or `not_closed`, include evidence and a minimum closure condition.

## Strict-Claim Boundary

This review must not claim formal implementation-review authority, readiness, acceptance, validation, or pass/fail verdict unless Orca overlay authority is supplied separately. Use findings-only advisory review. Do not emit `patch_queue_entry`; do not edit source files; do not commit, push, PR, merge, or run live scanning/capture.

If you find no blocker or major issue, say so and state residual risks or validation gaps. If you find an issue, findings lead the report and must include:

- finding id
- severity as `blocker`, `major`, or `minor` for prioritization only, not formal Orca verdict authority
- target file and stable line/anchor
- evidence from the implementation
- authority or evidence basis
- concrete impact
- minimum closure condition
- next authorized action
- validation expectation

## Output Contract

Write the full review report to:

`docs/review-outputs/csb_scanning_artifact_checker_ci_diff_gate_adversarial_code_review_v0.md`

The report must include:

- `reviewed_by: operator_to_fill`
- `authored_by: openai-gpt-5-codex`
- `de_correlation_bar: cross_vendor_discovery | same_vendor_sanity | self_fallback`
- `same_vendor_rationale:` required if `de_correlation_bar` is `same_vendor_sanity`
- source-read ledger
- `SOURCE_CONTEXT_READY` or `SOURCE_CONTEXT_INCOMPLETE`
- findings first
- open questions and residual risk
- validation commands run, skipped, or blocked
- intended enforcement closure check for E-01 through E-04
- review-use boundary: findings are decision input only, not approval, validation, mandatory remediation, or executor-ready patch authority until separately accepted or authorized

After writing the report, fresh-read the written report path and return compact courier YAML in chat:

```yaml
review_summary:
  status: completed | blocked | failed
  report_path: docs/review-outputs/csb_scanning_artifact_checker_ci_diff_gate_adversarial_code_review_v0.md
  recommendation: accept | accept_with_friction | patch_before_merge | needs_architecture_pass | blocked
  reviewed_by: operator_to_fill
  authored_by: openai-gpt-5-codex
  de_correlation_bar: cross_vendor_discovery | same_vendor_sanity | self_fallback
  summary: ""
  findings_count: 0
  blocking_findings: []
  advisory_findings: []
  next_action: ""
```

Review findings are decision input only; they are not approval, validation, mandatory remediation, readiness, or executor-ready patch authority until the Chief Architect separately accepts or authorizes them.
