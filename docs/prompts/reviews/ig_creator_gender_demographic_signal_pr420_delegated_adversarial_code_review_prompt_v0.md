# IG Creator-Gender Demographic Signal PR 420 Delegated Adversarial Code Review Prompt v0

```yaml
retrieval_header_version: 1
artifact_role: Orca review prompt (delegated/adversarial code review route-out)
scope: >
  De-correlated adversarial implementation/code review prompt for PR 420's
  creator-gender demographic signal slice. This is a route-out from the
  provisional delegated-review-patch convention because the target is a
  multi-file implementation/code diff, not a single high-stakes authored
  artifact, and no separate patch-execution commission is bound.
use_when:
  - Launching an independent, de-correlated review of PR 420 before merge.
  - Checking the sensitive inferred-demographic minimization posture, product-cue
    circularity handling, and hard-label-unrepresentable invariant.
  - Reconstructing why PR 420 still needs a visible delegated review artifact.
authority_boundary: retrieval_only
open_next:
  - .agents/workflow-overlay/delegated-review-patch.md
  - .agents/workflow-overlay/review-lanes.md
  - .agents/workflow-overlay/prompt-orchestration.md
  - .agents/workflow-overlay/source-loading.md
  - docs/decisions/ig_creator_gender_demographic_signal_lane_scope_defer_v0.md
input_hashes:
  creator_gender_models_py: E6ADF199B24033CC29B16696FDD51BAF060F9A894E747E455798CC1741D0184B
  creator_gender_fusion_py: 53CF273DD68A78CBD849E9FD4C4B510B988EAD699429DE20C21BB6210C74A938
  test_creator_gender_fusion_py: 1DA6DB1EB27CB41A7FD3740504805BA48818DAC65209DF62AE9FF14DDE2D0E8A
  scope_defer_decision_md: 3AA9E1EBACF0370F7FB3556BE6CF9592638113405CB6F61F5E837DD75293C353
branch_or_commit:
  branch: claude/ig-creator-gender-demographic
  reviewed_code_head: 26cf707f777db1682f13b1f8b5fa17a9eb3e9263
  pr: 420
stale_if:
  - Any target implementation, test, or scope decision file hash differs from input_hashes.
  - PR 420 is rebased/amended so reviewed_code_head is not an ancestor of the current branch.
  - Orca delegated-review, review-lane, prompt-orchestration, source-loading, or validation-gate authority changes.
  - A durable PR 420 delegated review report already exists and supersedes this prompt.
```

## Prompt Status

Status: `READY_FOR_DELEGATED_ADVERSARIAL_CODE_REVIEW_PROMPT_WITH_RECEIPT_GATE`.

This prompt does not run the review. It does not patch code, validate PR 420,
approve merge, or claim the prior delegated review occurred. It files a durable
route-out prompt so an independent receiving lane can inspect PR 420 directly
and write a review report.

The current PR head commit message claims a home-model adjudication of a
de-correlated GPT-family review, but PR 420 has no GitHub review/comments and no
repo-visible prompt or review report was found for this PR before this prompt
was authored. Treat that as context to verify, not as proof that delegated
review is complete.

## Orca Prompt Preflight

```yaml
orca_start_preflight:
  agents_read: yes
  overlay_read: yes
  source_pack: custom S0 plus PR 420 target files and scope decision
  edit_permission: read-only for downstream reviewer
  target_scope: PR 420 creator-gender demographic signal code slice
  dirty_state_checked: yes
  blocked_if_missing: AGENTS.md, overlay README, review-lanes, delegated-review-patch, prompt-orchestration, target files
output_mode:
  prompt_artifact: file-write
  downstream_output: review-report
template_kind: review
edit_permission:
  downstream_reviewer: read-only
  patch_authority: not bound
prompt_artifact_path: docs/prompts/reviews/ig_creator_gender_demographic_signal_pr420_delegated_adversarial_code_review_prompt_v0.md
downstream_report_path: docs/review-outputs/ig_creator_gender_demographic_signal_pr420_delegated_adversarial_code_review_v0.md
```

## Launch Prompt

````text
You are the controller for a delegated, de-correlated adversarial code review
of Orca PR 420.

This is NOT a runtime model recommendation. De-correlation is a who-constraint
for review coverage measurement, not a claim that one model is better. Do not
add a Recommended model block, do not rank runtime models, and do not treat this
prompt as model routing.

This is also NOT a delegated review-and-patch commission. The target is a
multi-file implementation/code diff, and no separate patch-execution commission
is bound. Your role is read-only adversarial implementation/code review. Do not
edit, stage, commit, push, or open a PR.

## Actor / Model-Family Receipt Gate

Before reading implementation sources, complete this receipt with actual
operator/tooling facts:

```yaml
actor_model_family_receipt:
  authored_by: operator_to_fill
  reviewed_by: operator_to_fill
  author_home_model_family: operator_to_fill
  controller_model_family: operator_to_fill
  current_receiving_actor_role: controller
  dispatch_mode: external-controller-courier
  de_correlation_bar: cross_vendor_discovery | same_vendor_sanity | self_fallback
  de_correlation_status: satisfied | blocked
  same_vendor_rationale: required_if_same_vendor_sanity
```

Repo-visible orientation only: branch name `claude/ig-creator-gender-demographic`
suggests a Claude-family authoring lane, and the current head commit message
claims a GPT-family review was adjudicated. Those are not enough to fabricate
exact provenance. If the operator cannot supply the receipt, record
`unrecorded` for factual provenance fields and block any strict cross-vendor
discovery claim.

If `controller_model_family` is missing, same-family as `author_home_model_family`,
ambiguous, or still a placeholder, stop before review and return
`BLOCKED_DECORRELATION_RECEIPT_MISSING` or `BLOCKED_CONTROLLER_NOT_DECORRELATED`.

If `current_receiving_actor_role` is `controller`, proceed as the controller
after the receipt is satisfied. Do not launch a replacement controller and do
not spawn recursive or unrelated subagents.

## Review Target

Repository:
- `C:\Users\vmon7\Desktop\projects\orca`

PR:
- GitHub PR: `https://github.com/eric-foo/orca/pull/420`
- Branch: `claude/ig-creator-gender-demographic`
- Reviewed code head: `26cf707f777db1682f13b1f8b5fa17a9eb3e9263`

Target files:
- `orca-harness/schemas/creator_gender_models.py`
- `orca-harness/scoring/creator_gender_fusion.py`
- `orca-harness/tests/unit/test_creator_gender_fusion.py`
- `docs/decisions/ig_creator_gender_demographic_signal_lane_scope_defer_v0.md`

Required durable review report path:
- `docs/review-outputs/ig_creator_gender_demographic_signal_pr420_delegated_adversarial_code_review_v0.md`

Dirty-state allowance:
- The reviewed code target is pinned at `26cf707f777db1682f13b1f8b5fa17a9eb3e9263`.
- This prompt may exist in a later prompt-only carrier commit on the same branch. If the target file hashes match the header above and `26cf707f777db1682f13b1f8b5fa17a9eb3e9263` is an ancestor of the current branch, the target is still valid.
- Any target file change from the hashes in this prompt is `BLOCKED_TARGET_STALE`.
- Unrelated dirty or untracked files are out of scope. Do not inspect them unless one narrow adjacent read is necessary to understand a target finding.
- Do not create, clone, request, or switch worktrees. Read the current working tree in place.

## Required Authority Sources

Read and follow:
- `AGENTS.md`
- `.agents/workflow-overlay/README.md`
- `.agents/workflow-overlay/decision-routing.md`
- `.agents/workflow-overlay/delegated-review-patch.md`
- `.agents/workflow-overlay/source-of-truth.md`
- `.agents/workflow-overlay/source-loading.md`
- `.agents/workflow-overlay/review-lanes.md`
- `.agents/workflow-overlay/prompt-orchestration.md`
- `.agents/workflow-overlay/validation-gates.md`
- `.agents/workflow-overlay/safety-rules.md`

Then read the target files listed above. Use the following adjacent sources only
if needed for a material finding:
- `orca-harness/scoring/audience_fusion.py`
- `orca-harness/scoring/product_fusion.py`
- `orca-harness/tests/contract/test_no_llm_imports.py`
- `docs/decisions/product_verdict_fusion_calibration_surface_v0.md`
- `orca-harness/cleaning/transcript_product_extractor.py`

Do not bulk-load unrelated capture, cleaning, judgment, research corpus, data
lake, review-output history, prompt history, `_inbox`, or other product files
unless a directly material target issue cannot be assessed without one narrow
adjacent read.

## Source-Gated Method Contract

REFERENCE-LOAD:
- `workflow-delegated-review-patch`
- `workflow-deep-thinking`
- `workflow-code-review`

Do not APPLY these methods before source readiness. SOURCE-LOAD the required
sources and declare `SOURCE_CONTEXT_READY` or `SOURCE_CONTEXT_INCOMPLETE`.

After source readiness, APPLY:
1. `workflow-delegated-review-patch` only to enforce receipt, role, scope,
   citation, escalation, and Chief Architect adjudication boundaries. Do not
   convert this read-only code review into a patch-authorized commission.
2. `workflow-deep-thinking` to frame sensitive-demographic failure modes,
   circularity paths, authorization conflicts, and fake-pass tests.
3. `workflow-code-review` to produce findings.

If `workflow-code-review` is unavailable, unresolved, or cannot be applied
after source readiness, return `BLOCKED_REVIEW_LANE_UNAVAILABLE` with the
reason and do not emit strict review claims. Do not silently emulate the review
lane inline.

## Cynefin Routing

Run Orca Cynefin routing before review.

Expected routing:
- Smallest complete outcome: review PR 420's creator-gender deterministic slice
  for sensitive inferred-demographic minimization failures, product-cue
  circularity, hard-label back doors, no-LLM boundary breaches, and source
  authority conflicts.
- Regime: complicated, with a review-authority wrinkle.
- Decomposition: risk-first implementation/code review over a small target
  slice, with the scope decision checked as governing context.
- Current bottleneck: proving that the code cannot emit or smuggle a hard
  creator-gender label, commenter gender, product-stance circularity, or
  unauthorized build claim while still preserving auditable soft-lean evidence.
- Riskiest assumption: tests pass because they exercise the intended happy path
  and recent review fixes, rather than because forbidden demographic payloads,
  product-cue circularity, and authorization overclaims are mechanically blocked.
- Stop or pivot condition: if the correct fix requires changing the lane scope,
  authorization status, minimization doctrine, product-stance architecture,
  cleaning inference design, data-lake persistence, or gender x stance join
  policy, return `NEEDS_ARCHITECTURE_PASS` / design-level finding and do not
  patch.
- Allowed next move: read-only adversarial code review and durable report.
- Disallowed next move: source edits, patch queues, implementation, live data
  reads, capture/backfill runs, cleaning inference work, product-stance join
  work, data-lake changes, or PR merge/approval claims.

## Review Criteria

Review material failures first:

- Hard-label unrepresentability: no top-level categorical `gender` field, no
  nested `gender`, `commenter_gender`, or equivalent categorical payload can
  hide in provenance, model construction, model copying, assignment, evidence
  ids, basis text, or fusion output.
- Sensitive-demographic minimization: the schema stores only soft signed lean,
  confidence, cue kind, short basis, and typed provenance; it does not smuggle
  transcript, commenter identity, profile, user metadata, or broad free-text
  payloads.
- Basis bound: `basis` is length-bounded and non-empty without becoming too
  thin for auditability.
- No commenter gender: neither schema nor tests imply per-commenter gender.
- Binary-axis residual: non-binary/outside-axis handling is named as abstention
  residual, not forced into male/female or silently erased as solved.
- Product-cue circularity: `product_marketed_gender` cannot decide or offset a
  creator-gender lean used later for gender x product-stance cuts. Retaining the
  cue kind must not create decisive fusion or evidence citation leakage.
- Evidence ids: only contributing, non-circular cues are cited as evidence.
- Single-creator guard: cross-creator signals cannot be fused into one lean.
- Empty, weak, neutral, zero-confidence, zero-weight, and contested signals
  abstain honestly.
- Numeric discipline: lean and confidence reject non-finite and out-of-range
  values, including unsafe construction or copy/update paths.
- No-LLM boundary: `schemas/` and `scoring/` remain deterministic and do not
  import OpenAI, Anthropic, LiteLLM, LangChain, HTTP, browser, or agent runtime
  dependencies.
- Calibration claim boundary: constants are explicitly uncalibrated v0 and not
  copied as a proven audience/product prior.
- Source authority conflict: the scope decision says `SCOPE_CAPTURED -
  DEFERRED - NOT_AUTHORIZED`, while PR 420 body says this is an authorized first
  slice. If no current owner authorization source supersedes the deferral, flag
  the conflict as a design/lifecycle issue. Do not infer authorization from the
  PR body alone.
- PR metadata drift: the PR body observed before this prompt still described
  product cue weight `0.3` and `17/17` tests, while current code/commit message
  describe product cue weight `0.0` and `19/19` tests. Flag misleading PR
  metadata if it remains true.
- Undocumented prior review claim: current head commit claims a GPT-family
  de-correlated review found F1/F2 and was adjudicated. Check whether there is a
  durable prompt/report or review record. If not, record the gap and do not
  treat that prior review as completed evidence.
- Test coverage: tests should fail on hard-label top-level and nested
  provenance attempts, overlong basis, non-finite values, product-cue decisive
  fusion, product-cue offsetting, multiple creators, blank ids, empty input, and
  no-LLM import violations.

Also check ordinary implementation quality where it affects the target:
- stable pydantic behavior under the repo's pydantic version;
- no fragile equality or rounding behavior that turns near-floor signals into
  misleading confidence;
- deterministic evidence ordering;
- import paths compatible with existing harness conventions;
- no hidden dependency on wall-clock time in tests.

## Output Contract

Write the full review report to:
- `docs/review-outputs/ig_creator_gender_demographic_signal_pr420_delegated_adversarial_code_review_v0.md`

Report structure:
1. Commission, lane binding, and actor/model-family receipt.
2. Source context status: `SOURCE_CONTEXT_READY` or `SOURCE_CONTEXT_INCOMPLETE`.
3. Cynefin routing result.
4. Provenance and de-correlation fields: `reviewed_by`, `authored_by`,
   `author_home_model_family`, `controller_model_family`,
   `de_correlation_bar`, `same_vendor_rationale` when applicable,
   `review_access_mode`, and `review_target_commit`.
5. Findings first, ordered by severity: critical, major, minor.
6. For each finding: location, issue, evidence, impact,
   `minimum_closure_condition`, `next_authorized_action`, and whether it is
   source-editable under this commission (`no` unless separately authorized).
7. Validation run status, including exact commands run or explicit not-run
   status.
8. Off-scope flags and design-level findings.
9. Controller verdict and residual-risk note.
10. CA adjudication packet.
11. Review-use boundary.

Do not emit `patch_queue_entry`; this review has no patch authority. Remediation
direction may state required end states, not executor-ready edits.

Suggested validation, if the source context is ready and local environment
supports it:

```powershell
Set-Location orca-harness
$env:PYTHONDONTWRITEBYTECODE = "1"
python -m pytest -p no:cacheprovider --no-header -q tests/unit/test_creator_gender_fusion.py tests/contract/test_no_llm_imports.py
```

If validation is not run, state why. Do not run network, live capture, data-lake,
cleaning inference, backfill, browser, or external service commands.

CA adjudication packet:
- state that findings, citations, validation evidence, and verdict are decision
  input only, not premises to inherit;
- list any source-authority conflict separately from patch-level code defects;
- list any closure conditions that require owner decision, rerun, PR metadata
  update, implementation patch authorization, or architecture pass;
- do not claim merge readiness, validation proof, owner acceptance, or that a
  delegated review has been completed until the report exists and the Chief
  Architect adjudicates it.

If no issues are found, say so clearly and name residual risks/test gaps.

After writing the report, return a compact chat summary with:
- report path;
- de-correlation receipt status;
- findings count by severity;
- validation evidence;
- strict claims explicitly not made;
- next action for Chief Architect adjudication.

Review-use boundary:
This delegated adversarial code review result is decision input only. It is not
approval, validation proof, merge readiness, mandatory remediation, product
proof, demographic-signal authorization, capture/backfill authorization, or
permission to keep any future patch without Chief Architect adjudication.
````
