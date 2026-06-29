# Fragrantica ECR Source-Side Adversarial Code Review Prompt v0

```yaml
retrieval_header_version: 1
artifact_role: Review prompt
scope: >
  Filed route-out prompt for adversarial implementation/code review of the
  Fragrantica source-side ECR structure and replayed data-lake materialization.
use_when:
  - Commissioning an independent reviewer to inspect the ECR-first Fragrantica lane before Cleaning or assumption-gate work.
  - Checking whether the generic ECR source-side posture set is correctly used over Fragrantica capture packets.
authority_boundary: retrieval_only
open_next:
  - .agents/workflow-overlay/prompt-orchestration.md
  - .agents/workflow-overlay/review-lanes.md
  - .agents/workflow-overlay/delegated-review-patch.md
  - .agents/workflow-overlay/source-loading.md
branch_or_commit: codex/fragrantica-ecr-review-prompt at b2e0d638b903989713b69523d1dfe7c0ebb13202; includes PR #445 merge 0de4618acf3c694d8e85ebd40a28fdb8cbd42bb3
stale_if:
  - Any target ECR or Fragrantica projection source file changes after this prompt is filed.
  - The worktree branch or HEAD differs from the pinned branch/head below.
  - The Fragrantica replayed raw/projection/ECR data-lake records are superseded by a newer replay.
  - The review-output destination already exists and the operator has not authorized a new version.
```

## Orca Prompt Preflight

- Output mode: file-write review prompt; receiver output mode is filesystem-output to `docs/review-outputs/fragrantica_ecr_source_side_adversarial_code_review_v0.md`.
- Template kind: review; Orca-local implementation/code-review template is unbound, so this uses the generic prompt-orchestrator review frame plus Orca overlay bindings. The current user explicitly requested `workflow-delegated-review-patch` for ECR first.
- Edit permission, targets, branch: reviewer is read-only. Target repo/worktree is `C:\Users\vmon7\Desktop\projects\orca\worktrees\fragrantica-ecr-review-prompt`, branch `codex/fragrantica-ecr-review-prompt`, HEAD `b2e0d638b903989713b69523d1dfe7c0ebb13202`, dirty state expected clean except the filed prompt artifact if reviewing before it is merged.
- Reviews: findings-first. This is advisory implementation/code review unless a later Orca binding grants formal implementation-review authority. Do not emit formal PASS, readiness, assumption-gate clearance, mandatory remediation, or patch queue.
- Doctrine change: none intended. This prompt routes a review; it does not alter ECR, Capture, Projection, Cleaning, prompt, review, or data-lake doctrine.
- Destinations: this prompt is the input artifact; the receiver writes the full report to `docs/review-outputs/fragrantica_ecr_source_side_adversarial_code_review_v0.md`.

## Commission

Run an adversarial implementation/code review of the Fragrantica source-side ECR decision and replayed materialization before any Cleaning or assumption-gate work proceeds.

This prompt was prepared after an explicit `workflow-delegated-review-patch` invocation, but the target is not a single high-stakes authored artifact. It is a multi-file implementation plus materialized data-lake lane. Per `.agents/workflow-overlay/delegated-review-patch.md`, do not force it into the single-artifact delegated review-and-patch convention. Route it through implementation/code review instead.

The review purpose is to find blocker or major correctness, scope, traceability, data-lake, validation, or false-confidence issues in the ECR-first handling for Fragrantica. The review must specifically attack whether the existing generic source-side ECR sibling set is the right structure for Fragrantica capture packets and whether the replayed materialization honestly preserves residuals instead of overclaiming clearance.

## Actor And De-Correlation Receipt

- author_home_model_family: OpenAI / GPT-family Codex, recorded from the current authoring lane.
- controller_model_family: `operator_to_fill`; must be a different upstream vendor/model lineage to claim cross-vendor discovery.
- current_receiving_actor_role: controller.
- dispatch_mode: external-controller-courier.
- de_correlation_status: `operator_to_fill`; if controller model family is missing or same-vendor, return advisory findings only and do not claim cross-vendor discovery or no-new-issue confidence.
- no runtime model recommendation is made by this prompt.

## Source-Gated Method Contract

1. REFERENCE-LOAD `workflow-deep-thinking` and `workflow-code-review` if available in your environment. Do not APPLY them yet.
2. Read the required Orca authority, target repo sources, and data-lake records below.
3. Declare `SOURCE_CONTEXT_READY` or `SOURCE_CONTEXT_INCOMPLETE` with missing sources, conflicts, and unavailable tools.
4. Only after source readiness, APPLY deep-thinking to frame material failure modes, then APPLY workflow-code-review to produce findings-first implementation/code review.
5. If `workflow-code-review` is unavailable, use its zero-config findings-only advisory semantics from this prompt text, but mark strict review claims `NOT_CLAIMED`.
6. If the external data lake at `F:\orca-data-lake` is unavailable, do not substitute the author summary for direct inspection. Mark materialized-lake review as `SOURCE_CONTEXT_INCOMPLETE` and continue only with the repo-source portion.

## Required Reads

Read these first:

- `AGENTS.md`
- `.agents/workflow-overlay/README.md`
- `.agents/workflow-overlay/source-loading.md`
- `.agents/workflow-overlay/prompt-orchestration.md`
- `.agents/workflow-overlay/review-lanes.md`
- `.agents/workflow-overlay/delegated-review-patch.md`
- `.agents/workflow-overlay/safety-rules.md`
- `docs/workflows/ecr_spine_submap_v0.md`
- `orca/product/spines/ecr/evidence_candidate_record/ecr_consolidation_v0_frame_source_visibility_slice_architecture_plan_v0.md`
- `orca/product/spines/ecr/evidence_candidate_record/ecr_consolidation_v0_sp1_sp2_sp3_source_side_slice_plan_v0.md`
- `orca/product/spines/judgment/source_side_receipts/jsg01_sp6_source_visibility_derivation_architecture_plan_v0.md`

Then read the implementation target:

- `orca-harness/ecr/models.py`
- `orca-harness/ecr/deriver.py`
- `orca-harness/ecr/lake.py`
- `orca-harness/tests/test_ecr_lake_pilot.py`
- `orca-harness/tests/unit/test_ecr_models.py`
- `orca-harness/tests/unit/test_ecr_identity_deriver.py`
- `orca-harness/tests/unit/test_ecr_inspectability_deriver.py`
- `orca-harness/tests/unit/test_ecr_timing_deriver.py`
- `orca-harness/tests/unit/test_ecr_source_visibility_deriver.py`
- `orca-harness/tests/unit/test_ecr_source_side_composition.py`

Read Fragrantica producer context only to the extent needed to verify the ECR input boundary and sibling projection relationship:

- `orca-harness/source_capture/fragrantica_projection.py`
- `orca-harness/runners/run_fragrantica_projection.py`
- `orca-harness/tests/unit/test_fragrantica_projection.py`
- `orca-harness/tests/unit/test_fragrantica_cleaning_projection_integration.py`
- `orca-harness/tests/test_fragrantica_projection_lake_pilot.py`

Do not widen into Cleaning design unless a target ECR finding cannot be explained without a direct Cleaning boundary source. If you need that source, state why before using it.

## Replayed Data-Lake Records To Inspect

The author reported a fresh Fragrantica projection replay and then ECR materialization over the same six raw packets. Treat these paths as inspection targets, not trusted proof.

Projection records reported by author:

- Baccarat Rouge 540: `F:\orca-data-lake\derived\930\01KW7SGXRZHFTS372X391Z8GHV\projection_fragrantica\01KW99HJVCCJQ5KNKY41MCKNJN.json`
- Sauvage: `F:\orca-data-lake\derived\601\01KW7YH647ARXFSM4E126JXHDS\projection_fragrantica\01KW99HKBJ7KBWWTF8J4KQ0NJS.json`
- Bleu de Chanel: `F:\orca-data-lake\derived\d60\01KW7YHQF051NVAYC7M4MW0B5H\projection_fragrantica\01KW99HKMC76JSY5DXBKKWABJR.json`
- Santal 33: `F:\orca-data-lake\derived\dee\01KW7YJ6KEHFWKMSX83ZSDVQ8K\projection_fragrantica\01KW99HKYKQHY1XGVFRBBXPVAM.json`
- Cloud: `F:\orca-data-lake\derived\3a1\01KW7YJP09YG806007ZQFEDZSA\projection_fragrantica\01KW99HME469C4H8GXMMQ4FJXC.json`
- Black Opium: `F:\orca-data-lake\derived\904\01KW7YKTPPNVV5F763351SHME3\projection_fragrantica\01KW99HMQTGRGX3EKSNK2A8CQQ.json`

ECR materialized record sets reported by author:

- Baccarat Rouge 540 raw `01KW7SGXRZHFTS372X391Z8GHV`, ECR record id `01KW99PN5N8H6MDJ0D9PJ2BFV6`
  - `F:\orca-data-lake\derived\930\01KW7SGXRZHFTS372X391Z8GHV\ecr_identity\01KW99PN5N8H6MDJ0D9PJ2BFV6.json`
  - `F:\orca-data-lake\derived\930\01KW7SGXRZHFTS372X391Z8GHV\ecr_inspectability\01KW99PN5N8H6MDJ0D9PJ2BFV6.json`
  - `F:\orca-data-lake\derived\930\01KW7SGXRZHFTS372X391Z8GHV\ecr_timing\01KW99PN5N8H6MDJ0D9PJ2BFV6.json`
  - `F:\orca-data-lake\derived\930\01KW7SGXRZHFTS372X391Z8GHV\ecr_source_visibility\01KW99PN5N8H6MDJ0D9PJ2BFV6.json`
  - `F:\orca-data-lake\derived\930\01KW7SGXRZHFTS372X391Z8GHV\ecr_set\01KW99PN5N8H6MDJ0D9PJ2BFV6.json`
- Sauvage raw `01KW7YH647ARXFSM4E126JXHDS`, ECR record id `01KW99PN7FBNQGH3Y37ZAKXY8K`
- Bleu de Chanel raw `01KW7YHQF051NVAYC7M4MW0B5H`, ECR record id `01KW99PND2EYW9H6C0JQ4FTK5X`
- Santal 33 raw `01KW7YJ6KEHFWKMSX83ZSDVQ8K`, ECR record id `01KW99PNEWQCFG808WAJSDPC7P`
- Cloud raw `01KW7YJP09YG806007ZQFEDZSA`, ECR record id `01KW99PNG3XDQF60BXKGVJTRA8`
- Black Opium raw `01KW7YKTPPNVV5F763351SHME3`, ECR record id `01KW99PNJGB4AAQK8G74FN0F3J`

For the five abbreviated ECR sets, inspect the same five sibling lanes under:

- `F:\orca-data-lake\derived\601\01KW7YH647ARXFSM4E126JXHDS\`
- `F:\orca-data-lake\derived\d60\01KW7YHQF051NVAYC7M4MW0B5H\`
- `F:\orca-data-lake\derived\dee\01KW7YJ6KEHFWKMSX83ZSDVQ8K\`
- `F:\orca-data-lake\derived\3a1\01KW7YJP09YG806007ZQFEDZSA\`
- `F:\orca-data-lake\derived\904\01KW7YKTPPNVV5F763351SHME3\`

For each packet, verify:

- the projection and all four ECR postures are siblings under the same raw packet key, not merged;
- the `ecr_set` marker references exactly four member lanes and member record hashes;
- `ecr_identity` and `ecr_inspectability` clear only when supported by raw packet fields;
- `ecr_timing` preserves a residual such as `unknown_with_reason` and does not clear when capture cutoff cannot be proven;
- `ecr_source_visibility` preserves `current_capture_only` or equivalent non-clearing posture and does not claim archive coverage;
- projection residuals for accords, notes pyramid, and similarity surfaces remain projection residuals, not ECR inputs or ECR clearance blockers.

If raw-packet files are needed to verify the bucket/hash/key relationship, derive the raw path from the ECR/projection metadata and inspect the frozen raw packet directly. Do not infer from filenames alone.

## Validation Evidence To Inspect

The author reported these focused tests passed after replay:

```powershell
python -m pytest -p no:cacheprovider --no-header --no-summary -q orca-harness\tests\test_ecr_lake_pilot.py orca-harness\tests\unit\test_ecr_identity_deriver.py orca-harness\tests\unit\test_ecr_inspectability_deriver.py orca-harness\tests\unit\test_ecr_timing_deriver.py orca-harness\tests\unit\test_ecr_source_visibility_deriver.py
```

Reported result: `49 passed`.

```powershell
python -m pytest -p no:cacheprovider --no-header --no-summary -q orca-harness\tests\unit\test_fragrantica_projection.py orca-harness\tests\unit\test_fragrantica_cleaning_projection_integration.py orca-harness\tests\test_fragrantica_projection_lake_pilot.py
```

Reported result: `10 passed`.

You may rerun read-only tests or checks if your environment permits. If you do not rerun them, report validation as author-supplied and not independently revalidated.

## Review Scope

Attack these questions:

- Does the generic ECR source-side posture set (`ecr_identity`, `ecr_inspectability`, `ecr_timing`, `ecr_source_visibility`, plus `ecr_set`) correctly fit Fragrantica capture packets without inventing a Fragrantica-specific ECR schema?
- Does the implementation keep ECR as integrity/provenance posture over raw packet evidence, not content extraction or review-sentiment projection?
- Are Fragrantica projection outputs and ECR postures true siblings under the same raw packet key in the derived lake?
- Does any code path accidentally use projection rows, review text, accords, notes, similarity data, or Cleaning-derived content to satisfy ECR source-side fields?
- Are the non-clearing timing and source-visibility residuals honest and visible, or is anything overclaiming freshness, archive coverage, historical completeness, review-window finality, or validation readiness?
- Does the materialization preserve append-only derived records with hashes and member references, without mutating raw packets or overwriting prior projections?
- Do tests cover the Fragrantica raw-packet shape through the generic ECR derivers, not only generic fixtures detached from real Fragrantica packet structure?
- Is the reported replay enough to support "ECR structure is acceptable to review next" while still not supporting assumption-gate, Cleaning readiness, Judgment readiness, buyer proof, or live capture coverage claims?
- Are there hidden path-containment, Windows path, bucket-key, record-id, hash, or stale-record risks in `derive_ecr_into_lake` when applied to these packets?

## Strict-Claim Boundary

This review must not claim formal implementation-review authority, readiness, acceptance, validation, assumption-gate clearance, or pass/fail verdict unless Orca overlay authority is supplied separately. Use findings-only advisory review. Do not emit `patch_queue_entry`; do not edit source files; do not commit, push, PR, run live capture, replay projection, replay ECR, or start Cleaning.

If you find no blocker or major issue, say so and state residual risks or validation gaps. If you find an issue, findings lead the report and must include:

- finding id
- severity as `blocker`, `major`, or `minor` for prioritization only, not formal Orca verdict authority
- target file and stable line/anchor
- evidence from the implementation or materialized record
- authority or evidence basis
- concrete impact
- minimum closure condition
- next authorized action
- validation expectation

## Output Contract

Write the full review report to:

`docs/review-outputs/fragrantica_ecr_source_side_adversarial_code_review_v0.md`

The report must include:

- `reviewed_by: operator_to_fill`
- `authored_by: gpt-family-codex`
- `de_correlation_bar: cross_vendor_discovery | same_vendor_sanity | self_fallback`
- `same_vendor_rationale:` required if `de_correlation_bar` is `same_vendor_sanity`
- source-read ledger
- `SOURCE_CONTEXT_READY` or `SOURCE_CONTEXT_INCOMPLETE`
- findings first
- open questions and residual risk
- validation evidence inspected and validation not-run gaps
- review-use boundary: findings are decision input only, not approval, validation, assumption-gate clearance, mandatory remediation, or executor-ready patch authority until separately accepted or authorized

After writing the report, return only a compact summary plus:

```yaml
review_courier:
  output_mode: filesystem-output
  report_path: docs/review-outputs/fragrantica_ecr_source_side_adversarial_code_review_v0.md
  commission: adversarial implementation/code review of Fragrantica source-side ECR structure and replayed lake materialization
  target:
    - orca-harness/ecr/models.py
    - orca-harness/ecr/deriver.py
    - orca-harness/ecr/lake.py
    - orca-harness/tests/test_ecr_lake_pilot.py
    - orca-harness/tests/unit/test_ecr_*.py
    - orca-harness/source_capture/fragrantica_projection.py as adjacent producer context only
    - F:\orca-data-lake\derived Fragrantica projection/ECR sibling records listed in the prompt
  authority: advisory implementation/code review; formal review verdict NOT_CLAIMED
  decision_criteria: generic ECR sibling structure, raw-packet keying, residual honesty, data-lake materialization integrity, Fragrantica boundary control
  evidence_summary: <short source-backed summary>
  reviewer_verdict: NOT_CLAIMED
  finding_ids: []
  minimum_closure_conditions: []
  next_authorized_action: home model adjudicates findings before assumption-gate, Cleaning, or fused implementation work
  non_claims:
    - not approval
    - not validation
    - not readiness
    - not assumption-gate clearance
    - not patch authority
    - not live capture execution
    - not Cleaning design
    - not Judgment or buyer proof
```
