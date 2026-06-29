# IG Deep Capture Transcript Extraction Adversarial Code Review Prompt v0

```yaml
retrieval_header_version: 1
artifact_role: Review prompt
scope: >
  Filed route-out prompt for de-correlated adversarial implementation/code
  review of the IG deep-capture transcript extraction patch: making completed
  per-reel deep-capture transcript records feed product extraction and
  behavioral projection without hidden skips or source-key ambiguity.
use_when:
  - Commissioning a bounded review of branch codex/ig-deep-capture-transcript-extraction before owner merge.
  - Checking whether deep-capture transcript records now behave like extraction-eligible transcript records without forcing shared IG/YT acquisition machinery.
authority_boundary: retrieval_only
open_next:
  - .agents/workflow-overlay/delegated-review-patch.md
  - .agents/workflow-overlay/review-lanes.md
  - .agents/workflow-overlay/prompt-orchestration.md
  - .agents/workflow-overlay/source-loading.md
source_repo: https://github.com/eric-foo/orca
source_branch: codex/ig-deep-capture-transcript-extraction
source_base: origin/main at 32e2d888f07ce345abadd521dca0dff9db93e264
source_head: e5a5765408461ba42fa7b3eef850b9ef953497f6
target_blob_ids:
  orca-harness/cleaning/transcript_product_extractor.py: 86c3a35d7b7f6f9d8822d2b3b33d7df801792e7f
  orca-harness/cleaning/transcript_product_lake.py: a6a27b13fbda95aaefe268d2b8a214f736af22cd
  orca-harness/runners/run_ig_reels_product_extract.py: 97af6d4fab63af27282148c24102baac3063fb01
  orca-harness/source_capture/ig_reels_behavioral_lake.py: 7ee1d6c06ff7781c2111206c57b01a13c9871e19
  orca-harness/source_capture/ig_reels_behavioral_projection.py: 8737eeffac33c3542294e25e93774cc315d3e006
  orca-harness/tests/unit/test_ig_reels_behavioral_lake.py: 347880ce9fc095e428d2ad2d3bad4274f2d79a91
  orca-harness/tests/unit/test_ig_reels_behavioral_projection.py: ef560060d5c4b961791b23fd67b34f412d870028
  orca-harness/tests/unit/test_ig_reels_product_extract.py: 31bd803b69a65e0620e97c23a22a5edb75141853
  orca-harness/tests/unit/test_transcript_product_lake.py: 3913ddbb0c1dd8feb422954a6e442b7014960868
intended_report_path: docs/review-outputs/ig_deep_capture_transcript_extraction_advisory_code_review_v0.md
stale_if:
  - Branch codex/ig-deep-capture-transcript-extraction head differs from e5a5765408461ba42fa7b3eef850b9ef953497f6.
  - origin/main base for the review differs from 32e2d888f07ce345abadd521dca0dff9db93e264 and the reviewer cannot explain whether the diff still applies.
  - Any target blob id differs from the values above.
  - The receiver cannot inspect the pinned source branch/worktree and diff directly.
```

## Prompt Preflight

preflight_defaults: `docs/prompts/templates/shared/orca_preflight_defaults_v0.md` v0 - constants bound; deltas stated below.

```yaml
orca_start_preflight:
  agents_read: yes_supplied_in_current_task_context
  overlay_read: yes_loaded_by_dispatcher
  source_pack: custom_ig_deep_capture_transcript_extraction_code_diff
  repo_map_decision: targeted_route_checked
  repo_map_reason: >
    `docs/prompts/reviews/`, `docs/review-outputs/`, `orca-harness/runners/`,
    `orca-harness/cleaning/`, `orca-harness/source_capture/`, and
    `orca-harness/tests/` are already map-reachable for this prompt and patch
    scope.
  edit_permission: read-only
  target_scope:
    implementation_targets:
      - C:\Users\vmon7\Desktop\projects\orca\worktrees\ig-deep-capture-transcript-extraction\orca-harness\cleaning\transcript_product_extractor.py
      - C:\Users\vmon7\Desktop\projects\orca\worktrees\ig-deep-capture-transcript-extraction\orca-harness\cleaning\transcript_product_lake.py
      - C:\Users\vmon7\Desktop\projects\orca\worktrees\ig-deep-capture-transcript-extraction\orca-harness\runners\run_ig_reels_product_extract.py
      - C:\Users\vmon7\Desktop\projects\orca\worktrees\ig-deep-capture-transcript-extraction\orca-harness\source_capture\ig_reels_behavioral_lake.py
      - C:\Users\vmon7\Desktop\projects\orca\worktrees\ig-deep-capture-transcript-extraction\orca-harness\source_capture\ig_reels_behavioral_projection.py
      - C:\Users\vmon7\Desktop\projects\orca\worktrees\ig-deep-capture-transcript-extraction\orca-harness\tests\unit\test_ig_reels_behavioral_lake.py
      - C:\Users\vmon7\Desktop\projects\orca\worktrees\ig-deep-capture-transcript-extraction\orca-harness\tests\unit\test_ig_reels_behavioral_projection.py
      - C:\Users\vmon7\Desktop\projects\orca\worktrees\ig-deep-capture-transcript-extraction\orca-harness\tests\unit\test_ig_reels_product_extract.py
      - C:\Users\vmon7\Desktop\projects\orca\worktrees\ig-deep-capture-transcript-extraction\orca-harness\tests\unit\test_transcript_product_lake.py
    context_only:
      - C:\Users\vmon7\Desktop\projects\orca\worktrees\ig-deep-capture-transcript-extraction\orca-harness\source_capture\ig_reels_deep_capture.py
      - C:\Users\vmon7\Desktop\projects\orca\worktrees\ig-deep-capture-transcript-extraction\orca-harness\source_capture\ig_reels_deep_capture_lake.py
      - C:\Users\vmon7\Desktop\projects\orca\worktrees\ig-deep-capture-transcript-extraction\orca-harness\source_capture\ig_reels_behavioral_projection.py
      - C:\Users\vmon7\Desktop\projects\orca\worktrees\ig-deep-capture-transcript-extraction\orca-harness\source_capture\ig_reels_behavioral_lake.py
      - C:\Users\vmon7\Desktop\projects\orca\worktrees\ig-deep-capture-transcript-extraction\orca-harness\runners\run_youtube_caption_product_extract.py
      - C:\Users\vmon7\Desktop\projects\orca\worktrees\ig-deep-capture-transcript-extraction\orca-harness\runners\run_transcript_product_extract.py
      - C:\Users\vmon7\Desktop\projects\orca\worktrees\ig-deep-capture-transcript-extraction\orca-harness\tests\unit\test_youtube_caption_product_extract.py
      - C:\Users\vmon7\Desktop\projects\orca\worktrees\ig-deep-capture-transcript-extraction\orca-harness\tests\unit\test_transcript_product_extractor.py
      - C:\Users\vmon7\Desktop\projects\orca\worktrees\ig-deep-capture-transcript-extraction\orca-harness\tests\contract\test_no_llm_imports.py
  excluded_from_review_target:
    - this prompt artifact
    - shared IG/YT/TikTok capture-core architecture
    - YouTube acquisition changes or live YouTube probing
    - Instagram live capture execution or source-system access
    - Cleaning product ontology quality beyond source identity and idempotence
    - Judgment, creator ledger, scheduler, dashboard, buyer-proof, or production-runtime claims
  dirty_state_checked: yes_by_dispatcher_before_prompt_write
  branch_or_commit_reference: >
    branch codex/ig-deep-capture-transcript-extraction,
    implementation commit e5a5765408461ba42fa7b3eef850b9ef953497f6,
    base origin/main 32e2d888f07ce345abadd521dca0dff9db93e264.
    If this prompt or a review report is later committed on another branch,
    exclude those artifacts from implementation findings.
  controlling_source_state: >
    Dispatcher observed the implementation worktree clean at
    e5a5765408461ba42fa7b3eef850b9ef953497f6 before this prompt artifact was filed.
    Strict readiness, approval, and formal pass claims are not authorized by this prompt.
  output_mode: file-write
  prompt_artifact_path: C:\Users\vmon7\Desktop\projects\orca\worktrees\ig-deep-capture-review-prompt\docs\prompts\reviews\ig_deep_capture_transcript_extraction_adversarial_code_review_prompt_v0.md
  delivery_copy: paste-ready-chat copy may be used after this filed prompt artifact exists
  reviewer_output_mode: filesystem-output_preferred
  required_review_report_path: C:\Users\vmon7\Desktop\projects\orca\worktrees\ig-deep-capture-review-prompt\docs\review-outputs\ig_deep_capture_transcript_extraction_advisory_code_review_v0.md
  doctrine_change_decision: no doctrine change requested; review prompt only
  isolation_decision: read-only review; do not create or switch branches/worktrees unless required only to inspect the pinned branch
  validation_gates:
    - inspect the source diff against the IG/YT transcript extraction parity objective
    - optionally rerun the focused pytest commands if repo execution is available
  blocked_if_missing:
    - reviewer cannot open the pinned implementation worktree, branch, or commit
    - reviewer cannot inspect the exact changed files and adjacent transcript/product-extraction context
    - reviewer cannot distinguish deep-capture transcript extraction eligibility from acquisition-method unification
```

## Commission

Run a read-only adversarial code review of branch `codex/ig-deep-capture-transcript-extraction` at commit `e5a5765408461ba42fa7b3eef850b9ef953497f6`.

The review target is the implementation code and tests listed above. The purpose is to find blocker or major correctness, scope, validation, boundary, idempotence, or false-confidence issues in the patch that makes IG per-reel deep-capture transcript records feed product extraction and behavioral projection.

This prompt is routed from an explicit `workflow-delegated-review-patch` request, but the target is a multi-file implementation/code diff. Per `.agents/workflow-overlay/delegated-review-patch.md`, do not stretch the provisional single-artifact review-and-patch convention. Route through adversarial implementation/code review instead. No patch execution, patch queue, formal verdict, readiness claim, runtime model recommendation, or no-new-seam claim is authorized.

De-correlation is a who-constraint, not a runtime model recommendation. The author/home family is OpenAI/Codex GPT-5, recorded from the authoring lane. The operator should route this to a different upstream vendor/model-lineage reviewer if claiming `cross_vendor_discovery`; otherwise record the lower bar actually used in the output provenance fields. Unknown or undisclosed reviewer lineage cannot satisfy cross-vendor de-correlation.

Fitness reference:

- Goal: when IG per-reel deep capture already spent the request and produced a transcript record, the product-extraction runner should extract from that record using the same idempotent path as other transcript inputs, and behavioral projection should make unextracted deep-capture transcripts visible enough to block a clean `complete`.
- Non-goal: do not require IG and YouTube to use the same acquisition method, priority ladder, packet shape, browser flow, or live capture route. This patch is transcript-feed/identity/projection parity only.
- Done looks like: the review identifies whether completed deep-capture transcript records are discovered, source-keyed, extracted exactly once, carried into the lake/projection, and tested without weakening existing standalone audio or YouTube transcript extraction behavior.

## Method Order

REFERENCE-LOAD these methods first. Do not APPLY them yet:

- `workflow-deep-thinking`
- `workflow-code-review`

Then SOURCE-LOAD the target files and context-only files listed in preflight. Declare either `SOURCE_CONTEXT_READY` or `SOURCE_CONTEXT_INCOMPLETE` with missing sources and material gaps. Only after that declaration, APPLY `workflow-deep-thinking` to frame material failure modes, then APPLY `workflow-code-review` for findings-first review.

If `workflow-code-review` is unavailable, unresolved, or cannot be applied, return `BLOCKED_REVIEW_LANE_UNAVAILABLE` with the reason and do not emit strict review claims.

## Required Reads

Read these first:

- `AGENTS.md`
- `.agents/workflow-overlay/README.md`
- `.agents/workflow-overlay/source-loading.md`
- `.agents/workflow-overlay/prompt-orchestration.md`
- `.agents/workflow-overlay/review-lanes.md`
- `.agents/workflow-overlay/delegated-review-patch.md`
- `.agents/workflow-overlay/safety-rules.md`

Then inspect the pinned source:

```powershell
git -C C:\Users\vmon7\Desktop\projects\orca\worktrees\ig-deep-capture-transcript-extraction status --short --branch
git -C C:\Users\vmon7\Desktop\projects\orca\worktrees\ig-deep-capture-transcript-extraction rev-parse HEAD
git -C C:\Users\vmon7\Desktop\projects\orca\worktrees\ig-deep-capture-transcript-extraction rev-parse origin/main
git -C C:\Users\vmon7\Desktop\projects\orca\worktrees\ig-deep-capture-transcript-extraction diff --stat origin/main..HEAD
git -C C:\Users\vmon7\Desktop\projects\orca\worktrees\ig-deep-capture-transcript-extraction diff origin/main..HEAD -- orca-harness/cleaning/transcript_product_extractor.py orca-harness/cleaning/transcript_product_lake.py orca-harness/runners/run_ig_reels_product_extract.py orca-harness/source_capture/ig_reels_behavioral_lake.py orca-harness/source_capture/ig_reels_behavioral_projection.py orca-harness/tests/unit/test_ig_reels_behavioral_lake.py orca-harness/tests/unit/test_ig_reels_behavioral_projection.py orca-harness/tests/unit/test_ig_reels_product_extract.py orca-harness/tests/unit/test_transcript_product_lake.py
git -C C:\Users\vmon7\Desktop\projects\orca\worktrees\ig-deep-capture-transcript-extraction ls-tree e5a5765408461ba42fa7b3eef850b9ef953497f6 -- orca-harness/cleaning/transcript_product_extractor.py orca-harness/cleaning/transcript_product_lake.py orca-harness/runners/run_ig_reels_product_extract.py orca-harness/source_capture/ig_reels_behavioral_lake.py orca-harness/source_capture/ig_reels_behavioral_projection.py orca-harness/tests/unit/test_ig_reels_behavioral_lake.py orca-harness/tests/unit/test_ig_reels_behavioral_projection.py orca-harness/tests/unit/test_ig_reels_product_extract.py orca-harness/tests/unit/test_transcript_product_lake.py
```

Read adjacent context as needed, but do not widen the target:

- `orca-harness/source_capture/ig_reels_deep_capture.py`
- `orca-harness/source_capture/ig_reels_deep_capture_lake.py`
- `orca-harness/runners/run_youtube_caption_product_extract.py`
- `orca-harness/runners/run_transcript_product_extract.py`
- `orca-harness/tests/unit/test_youtube_caption_product_extract.py`
- `orca-harness/tests/unit/test_transcript_product_extractor.py`
- `orca-harness/tests/contract/test_no_llm_imports.py`

## Review Axes To Attack

Focus on blocker/major correctness and review-confidence failures:

- Whether `run_ig_reels_product_extract.py` genuinely discovers completed deep-capture transcript record sets and does not silently skip a valid per-reel transcript because only standalone audio transcript lanes were scanned before.
- Whether deep-capture transcript records are filtered to the intended completed transcript shape, not every deep-capture packet or failed/missing transcript posture.
- Whether `transcript_source_key`, `source_route`, and `asr_record_id` are exact enough to disambiguate multiple transcript records for the same reel and prevent accidental de-duplication or false idempotence.
- Whether `mentions_record_id` remains backward compatible for existing transcript inputs while using the optional exact source key when present.
- Whether product extraction results persist the source identity fields without making those fields required for older YouTube or standalone transcript flows.
- Whether `ig_reels_behavioral_lake.py` ingests product extraction results with enough source identity for behavioral projection to correlate extraction with the exact deep-capture transcript record.
- Whether `ig_reels_behavioral_projection.py` treats deep-capture transcript records as extraction-feed-eligible, blocks clean `complete` when such a transcript is unextracted, and becomes complete when the exact-key product extraction record exists.
- Whether projection does not hide acquisition failure states, failed ASR, missing transcript posture, or source mismatch behind a product-extraction success from a different source.
- Whether the code preserves the no-LLM runner boundary and does not import live browser, network, Cleaning ontology expansion, Judgment, dashboard, or creator-ledger machinery into the projection path.
- Whether tests prove load-bearing behavior rather than only asserting the implementation's chosen helper names: deep-capture discovery, exact source key idempotence, projection residuals, lake adapter propagation, and no regression for YT/shared transcript extraction.
- Whether any claim of shared IG/YT capture-core unification, acquisition parity, data-lake propagation doctrine, live capture completeness, or creator-ledger readiness is implied without authority.

## Validation Evidence To Inspect

Dispatcher-observed focused validation after the patch:

```powershell
cd C:\Users\vmon7\Desktop\projects\orca\worktrees\ig-deep-capture-transcript-extraction
$env:PYTHONDONTWRITEBYTECODE=1; python -m pytest -p no:cacheprovider -q --basetemp .pytest_tmp_ig_deep_capture_extract orca-harness/tests/unit/test_ig_reels_product_extract.py orca-harness/tests/unit/test_ig_reels_behavioral_projection.py orca-harness/tests/unit/test_ig_reels_behavioral_lake.py orca-harness/tests/unit/test_transcript_product_lake.py
```

Observed result in the implementation turn: `48 passed`.

Dispatcher-observed no-LLM contract validation:

```powershell
cd C:\Users\vmon7\Desktop\projects\orca\worktrees\ig-deep-capture-transcript-extraction
$env:PYTHONDONTWRITEBYTECODE=1; python -m pytest -p no:cacheprovider -q --basetemp .pytest_tmp_ig_deep_capture_contract orca-harness/tests/contract/test_no_llm_imports.py
```

Observed result in the implementation turn: `1 passed`.

Dispatcher-observed shared/YT smoke validation:

```powershell
cd C:\Users\vmon7\Desktop\projects\orca\worktrees\ig-deep-capture-transcript-extraction
$env:PYTHONDONTWRITEBYTECODE=1; python -m pytest -p no:cacheprovider -q --basetemp .pytest_tmp_ig_deep_capture_shared orca-harness/tests/unit/test_transcript_product_extractor.py orca-harness/tests/unit/test_youtube_caption_product_extract.py orca-harness/tests/unit/test_youtube_behavioral_projection.py
```

Observed result in the implementation turn: `54 passed`.

Treat these as evidence to inspect, not as a formal validation claim. If you have repo execution access, rerun the focused pytest commands and report the observed result. If you cannot run them, report `validation_not_run` and review from source.

## Output Contract

Preferred reviewer output is a durable report at:

`C:\Users\vmon7\Desktop\projects\orca\worktrees\ig-deep-capture-review-prompt\docs\review-outputs\ig_deep_capture_transcript_extraction_advisory_code_review_v0.md`

If filesystem write is unavailable, return the same findings-first report in chat and set `review_location: chat_only_current_thread`. Do not claim chat is equivalent to a missing durable report.

Report findings first, ordered by materiality. Each finding must include:

- `finding_id`
- commissioned target and purpose
- file and line or stable structural anchor
- implementation evidence
- authority or evidence basis
- correctness, validation, runtime, or review-confidence impact
- `minimum_closure_condition`
- `next_authorized_action`
- verification expectation
- whether `patch_queue_entry` is authorized: always `no` for this prompt

Also include:

- source-read ledger
- `SOURCE_CONTEXT_READY` or `SOURCE_CONTEXT_INCOMPLETE`
- strict-only blockers and `not proven` boundaries
- validation run status
- open questions
- residual risk
- review-use boundary: findings are decision input only; they are not approval, validation, readiness, mandatory remediation, or executor-ready patch authority until separately accepted or authorized

Use these provenance fields in the durable report or chat output:

```yaml
reviewed_by: operator_or_reviewer_to_fill_or_unrecorded
authored_by: OpenAI/Codex GPT-5
de_correlation_bar: cross_vendor_discovery | same_vendor_sanity | self_fallback | unrecorded
same_vendor_rationale: not_applicable_unless_same_vendor_sanity_is_claimed
target_branch: codex/ig-deep-capture-transcript-extraction
target_commit: e5a5765408461ba42fa7b3eef850b9ef953497f6
base_commit: 32e2d888f07ce345abadd521dca0dff9db93e264
reviewer_verdict: NOT_CLAIMED
```

Do not fabricate model identity. Do not recommend, prescribe, rank, or imply runtime model choice.

After writing the report, return only a compact summary plus:

```yaml
review_courier:
  output_mode: filesystem-output
  report_path: docs/review-outputs/ig_deep_capture_transcript_extraction_advisory_code_review_v0.md
  commission: adversarial implementation/code review of IG deep-capture transcript extraction patch
  target_branch: codex/ig-deep-capture-transcript-extraction
  target_commit: e5a5765408461ba42fa7b3eef850b9ef953497f6
  target:
    - orca-harness/cleaning/transcript_product_extractor.py
    - orca-harness/cleaning/transcript_product_lake.py
    - orca-harness/runners/run_ig_reels_product_extract.py
    - orca-harness/source_capture/ig_reels_behavioral_lake.py
    - orca-harness/source_capture/ig_reels_behavioral_projection.py
    - orca-harness/tests/unit/test_ig_reels_behavioral_lake.py
    - orca-harness/tests/unit/test_ig_reels_behavioral_projection.py
    - orca-harness/tests/unit/test_ig_reels_product_extract.py
    - orca-harness/tests/unit/test_transcript_product_lake.py
  authority: advisory implementation/code review; formal review verdict NOT_CLAIMED
  decision_criteria: deep-capture transcript feed completeness, exact source identity, idempotence, projection failure visibility, boundary hygiene, offline test adequacy
  evidence_summary: <short source-backed summary>
  finding_ids: []
  minimum_closure_conditions: []
  next_authorized_action: home model adjudicates findings before keeping or landing the branch
  non_claims:
    - not approval
    - not validation
    - not readiness
    - not patch authority
    - not live capture execution
```

For this prompt, `proposed patch`, `diff`, `exact requested edits`, formal verdict, severity authority, readiness, approval, validation pass/fail, and patch queue are `NOT_CLAIMED` unless a later owner instruction binds them.
