# CSB Scanning Broad-Scout Recency Default Enforcement Adversarial Code Review v0

```yaml
retrieval_header_version: 1
artifact_role: Review output
scope: >
  Adversarial mixed code/docs review of the CSB recency row-shape enforcement
  patch at commit 28d896c79100db1159c5b0cdf9d897e4734397f0.
use_when:
  - Chief Architect adjudication of this review's findings.
  - Deciding whether the CSB enforcement patch is ready to land.
authority_boundary: retrieval_only
reviewed_by: claude-sonnet-4-6
authored_by: openai-gpt-5-codex
de_correlation_bar: cross_vendor_discovery
same_vendor_rationale: not_applicable
```

---

## Review Provenance

- **reviewed_by**: `claude-sonnet-4-6` (Anthropic / Claude family)
- **authored_by**: `openai-gpt-5-codex` (OpenAI / GPT family — recorded from prompt commission)
- **de_correlation_bar**: `cross_vendor_discovery` — reviewer vendor (Anthropic) differs from author vendor (OpenAI). Satisfies the cross-vendor discovery bar; no-new-seam claim is available to the CA upon adjudication.
- **implementation_under_review**: `28d896c79100db1159c5b0cdf9d897e4734397f0`
- **review_prompt**: `docs/prompts/reviews/csb_scanning_broad_scout_recency_default_enforcement_adversarial_code_review_prompt_v0.md`
- **report_path**: `docs/review-outputs/csb_scanning_broad_scout_recency_default_enforcement_adversarial_code_review_v0.md`

---

## Source-Read Ledger

| Source | Role | Freshness | State |
| --- | --- | --- | --- |
| `AGENTS.md` | Orca kernel authority | in context from session start | clean |
| `.agents/workflow-overlay/README.md` | Overlay entry point | read this session | clean |
| `.agents/workflow-overlay/review-lanes.md` | Review lane authority | read this session | clean |
| `.agents/workflow-overlay/delegated-review-patch.md` | De-correlation authority | read this session | clean |
| `.agents/workflow-overlay/validation-gates.md` | Validation gate authority | read this session | clean |
| `.agents/workflow-overlay/safety-rules.md` | Safety authority | read this session | clean |
| `docs/decisions/overlay_enforcement_placement_classification_v0.md` | Enforcement placement authority | read this session | clean |
| `.agents/hooks/check_commission_signal_board_output.py` | Primary target | read this session at HEAD (matches impl commit) | clean |
| `orca-harness/tests/unit/test_commission_signal_board_output_validator.py` | Primary target | read this session at HEAD | clean |
| All 10 fixture files (`commission_signal_board_outputs/`) | Primary target | read via diff + direct read of 2 representative fixtures | clean |
| `orca/product/spines/commission_signal_board/prompts/orca_commission_signal_board_prompt_structure_v0.md` | Primary target | read this session at HEAD | clean |
| `orca/product/spines/commission_signal_board/workflows/commission_signal_board_playbook_v0.md` | Primary target | read this session at HEAD | clean |
| `orca/product/spines/commission_signal_board/authority/orca_commission_signal_board_prompt_structure_rules_v0.md` | Primary target | read this session at HEAD | clean |
| `orca/product/spines/scanning/README.md` | Adjacent doctrine (leakage check) | read this session | clean |
| `orca/product/spines/scanning/scan_core/orca_scanning_intelligent_walk_mgt_operating_model_v0.md` | Adjacent doctrine (leakage check) | read partial (first 100 lines for vocabulary/boundary check) | clean |
| Capture playbook + Judgment machinery arch | Adjacent doctrine (leakage check) | NOT directly read — relied on DCP claim and prior review | unverified |
| `git show --stat --patch` diff of `28d896c` | Implementation diff | obtained this session | verified |
| Target file drift check (`git log 28d896c..HEAD -- [target files]`) | Stability gate | ran this session — result: empty (no drift) | verified |

**Gaps noted:** `orca/product/spines/capture/core/source_capture_toolbox/source_capture_playbook_v0.md` and `orca/product/spines/judgment/demand_read/core/judgment_spine_demand_read_machinery_architecture_v0.md` were not read directly. The prompt's DCP asserts these carry their own DCP receipts for the recency propagation and that a prior adversarial review (commit `5a861ffe docs: record recency propagation review`, which predates the implementation commit) found no cross-spine leakage. This reviewer cannot independently verify that claim from the sources read. Finding AR-04 records this.

---

## SOURCE_CONTEXT_READY

Target files at HEAD match the implementation commit (`28d896c`). Zero commits after the implementation commit touched any named target file. Later commits on branch are prompt-carrier commits only. All primary target sources and critical authority files are read. Source context is READY with the gap noted above (Capture/Judgment adjacent sources unread).

---

## Deep-Thinking Discipline

Applied before findings. Hidden assumptions and bypass paths interrogated:

1. **The central risk in enforcement-placement patches is manufacturing false confidence**: a checker that passes on invalid inputs while docs claim it catches them. Specifically attacked: can the new enum validation be bypassed via normalization artifacts, column ordering, or missing-column paths that don't reach the enum check?

2. **The non-proof boundary is the hardest to maintain**: recency/currentness wording that leaks from "attention routing" into anything resembling proof, demand classification, graph weight, or readiness is structurally seductive because the concepts are adjacent. Specifically attacked every doc surface for these slippages.

3. **Test coverage gaps are more dangerous than code gaps**: the checker could be correct while a missing test masks a silent regression path. Specifically traced which failure modes are proven by which tests vs. which rely only on code inspection and the selftest.

4. **DCP completeness is a claim, not an observation**: the stale-language search results are author-asserted. Independently checked the scanning spine surfaces; Capture/Judgment surfaces remain unverified by this reviewer.

5. **`recency_priority` row_purpose is a new vocabulary term** not present in prior versions — specifically checked whether its semantics and boundaries are clearly defined to avoid agents treating recency as a priority gate.

---

## Trigger Gate

- `workflow-adversarial-artifact-review` explicitly named in the commission prompt's method contract: TRIGGERED.
- `workflow-code-review` applied to checker, tests, and fixture changes: TRIGGERED.
- Mixed target (code + docs): routing confirmed per commission prompt's explicit instruction to use both skills. Lane collision handled: code review covers `.py` and `.txt` fixture files; adversarial artifact review covers `.md` doctrine surfaces.

---

## Lane Collision Result

No collision. The commission prompt explicitly routes mixed target as `workflow-code-review` for checker/tests/fixtures and `workflow-adversarial-artifact-review` for prompt/playbook/adjudication docs. Reviewer is read-only. No patch execution.

---

## Findings (Correctness First, Then Friction)

### Phase 1 — Correctness Findings

#### AR-01 (minor · correctness) — Explicit enum failure tests exist only for `recency_status` and `recency_attention`; `row_purpose`, `graph_role`, and `graph_weight_hint` lack dedicated mutation tests

**Location**: `orca-harness/tests/unit/test_commission_signal_board_output_validator.py` · `test_signal_board_validates_recency_vocab`; fixture directory.

**Evidence**: The two new shape tests are:
- `test_signal_board_requires_recency_columns` — strips `" | Recency status | Recency attention |"` from the header; asserts `missing_required_row_columns` fires.
- `test_signal_board_validates_recency_vocab` — replaces `recent | high` with `too_new | proof`; asserts `invalid_recency_status` and `invalid_recency_attention` fire.

No parallel tests exist for:
- Stripping `row_purpose`, `graph_role`, or `graph_weight_hint` columns from the header.
- Injecting invalid values for `row_purpose`, `graph_role`, or `graph_weight_hint`.

None of the 7 bad fixtures exercise an invalid `row_purpose`, `graph_role`, or `graph_weight_hint` value.

**Strongest defense**: The checker code is demonstrably correct — `_validate_signal_row_vocab` calls `_validate_vocab_field` for all five new fields symmetrically, and `REQUIRED_ROW_COLUMNS` lists all five. The selftest passes all fixtures, including the valid ones that exercise all new columns. The valid-fixture parametrized tests run `validate_text` on all three valid fixtures, which do contain all required columns and valid values; a silent regression that drops any of the three would surface as a selftest failure rather than a test-suite failure. The review's implicit question — "would the code catch it?" — is answered yes.

**Why the defense is incomplete**: The test suite provides no red-green proof that the three additional new fields (beyond recency) fail when violated. If a future author mutates `_validate_signal_row_vocab` to omit one of the five fields (e.g., removes `graph_role` check), no test fails unless the selftest is also run. The selftest requires human invocation and is not in the pytest suite directly (it is tested via the pytest parametrization of valid fixtures, but those don't directly mutate the new fields). A regression in `graph_role` enum checking would only show up if a valid fixture were mutated to have an invalid `graph_role` in a future edit — which is not guaranteed.

**Impact**: The enforcement gap is in testing completeness only, not in code behavior. The code enforces all five fields. The risk is silent regression if `_validate_signal_row_vocab` is modified later.

**minimum_closure_condition**: Two additional tests (or an additional parametrize block): one that strips a `row_purpose` or `graph_role` or `graph_weight_hint` column and asserts `missing_required_row_columns`; one that injects an invalid value for `row_purpose` (e.g., `"not_a_purpose"`) and asserts `invalid_row_purpose`.

**next_authorized_action**: Advisory only. CA may accept this gap as acceptable for current testing posture (the selftest + implicit valid-fixture tests provide partial coverage) or commission a follow-up test patch. Not a blocker for acceptance.

**patch_queue_entry**: Not authorized (advisory lane, not patch-queue lane).

---

#### AR-02 (minor · correctness) — Adjudication packet's Graph-Light Contract field taxonomy omits `recency_priority` from `row_purpose` values

**Location**: `orca/product/spines/commission_signal_board/authority/orca_commission_signal_board_prompt_structure_rules_v0.md` · "Graph-Light Contract" section · field schema YAML block.

**Evidence**: The adjudication packet's proposed field taxonomy lists:
```yaml
row_purpose: chronology | source_route | signal_unit | contradiction | gap | classifier_handoff
```
(six values, no `recency_priority`)

The durable CSB prompt lists:
```yaml
row_purpose: chronology | source_route | signal_unit | contradiction | gap | classifier_handoff | recency_priority
```
(seven values, includes `recency_priority`)

The checker `VALID_ROW_PURPOSES` includes `recency_priority`.

The patch to the adjudication packet was limited to the "Current prompt amendment" paragraph — it did not update the field taxonomy block.

**Strongest defense**: The adjudication packet is a decision-prep artifact, not a prompt or checker. Its field taxonomy was a proposed schema at the time of authoring; the durable CSB prompt (authored separately through prompt-orchestration) is the canonical field vocabulary source. The adjudication packet's own "Adjudication" section now says "the durable CSB prompt now records recency/currentness as source-route attention metadata," implicitly acknowledging that the prompt supersedes the adjudication packet's proposed schema. The CA adjudicating this packet knows the prompt is authoritative.

**Why the defense is incomplete**: An agent reading the adjudication packet without immediately cross-referencing the prompt could believe `recency_priority` is not a valid row purpose, or that the six-value list is the complete canon. This creates a documentation inconsistency that is detectable and avoidable. The adjudication packet's field taxonomy is not retired or clearly labeled as superseded.

**Impact**: Low. The operational surface where an agent is told to use the adjudication packet's field taxonomy (not the prompt's) is narrow. But the inconsistency is unnecessary and could cause confusion in a cold-read.

**minimum_closure_condition**: Either (a) update the adjudication packet's field taxonomy block to add `recency_priority` to the `row_purpose` values, or (b) add a note in the adjudication packet's field taxonomy section that the durable CSB prompt is the canonical vocabulary source.

**next_authorized_action**: Advisory only. CA may choose to close this in a subsequent docs-hygiene commit or accept the inconsistency as acceptable given the adjudication packet's non-authoritative role. Not a blocker.

**patch_queue_entry**: Not authorized.

---

#### AR-03 (minor · correctness) — `recency_priority` row_purpose is accepted by the checker but not explained in the prompt body's Section 4 rules

**Location**: `orca/product/spines/commission_signal_board/prompts/orca_commission_signal_board_prompt_structure_v0.md` · "### 4. Signal Board Rows" · Rules sub-section.

**Evidence**: The Section 4 rules block contains:
```
- Use `recency_attention: high` for same-strength newer/current signals that
  should receive more downstream scan attention than older context; this does
  not make the row proof, demand classification, or graph weight.
```

This explains how to use `recency_attention: high`. But the rules block contains no instruction on when to use `row_purpose: recency_priority` vs. `row_purpose: signal_unit` with `recency_attention: high`. The field vocabulary section defines the value but does not distinguish when a row's purpose is `recency_priority` rather than `signal_unit`.

**Strongest defense**: The vocabulary definition is present in the Field Vocabulary section (`row_purpose records why this row exists inside the board`). The values are enumerated. An agent authoring a board that uses `recency_priority` as a row purpose would not be blocked by the checker. The value is legitimately distinct from `signal_unit` — it represents a row whose primary function is recency routing rather than signal contribution — and an author can infer this.

**Why the defense is incomplete**: The inference is non-obvious. A board agent could reasonably use `row_purpose: signal_unit` everywhere and never use `recency_priority`, or could misuse `recency_priority` as a shorthand for "important new source." Without guidance on the distinction, the value is under-described and risks being either ignored or overused.

**Impact**: Low. The checker accepts both values. The risk is authoring confusion, not a failure mode in the checker or docs accuracy.

**minimum_closure_condition**: A clarifying sentence in the Section 4 rules block stating when `row_purpose: recency_priority` should be used vs. `signal_unit` with `recency_attention: high`. For example: "Use `row_purpose: recency_priority` only for rows whose board role is specifically to flag a recency routing priority — not for ordinary signal rows that happen to have `recency_attention: high`."

**next_authorized_action**: Advisory only. CA may add this clarification in a subsequent prompt update or accept the current vocabulary as sufficient. Not a blocker.

**patch_queue_entry**: Not authorized.

---

### Phase 2 — Friction Findings

No material friction findings. The checker is minimal and single-purpose. The tests are proportionate to the change. The DCP receipts are scoped correctly. The playbook's "What A Pass Means" section is clear and accurate. No avoidable process bloat identified.

---

## Not-Assessed Finding

#### AR-04 — Cross-spine leakage into Capture and Judgment surfaces not directly verified

**Evidence**: The CSB prompt's DCP `stale_language_search_result` asserts: "Capture and Judgment surfaces carry their own DCP receipts for the same propagation, and the follow-up adversarial review ran a cross-spine leakage search with no proof, scoring, route-binding, or gate-clearance leakage found."

This reviewer did not read `orca/product/spines/capture/core/source_capture_toolbox/source_capture_playbook_v0.md` or `orca/product/spines/judgment/demand_read/core/judgment_spine_demand_read_machinery_architecture_v0.md` directly. The claim relies on a prior adversarial review (commit `5a861ffe docs: record recency propagation review`, chronologically before the implementation commit) and on those surfaces' own DCP receipts.

**Scanning spine check (completed)**: The scanning README and MGT operating model were read. They correctly keep recency as "attention and relevance weight" without any proof, gate-clearance, or Capture route-binding claim. No leakage found in scanning surfaces directly read.

**Status**: `not_assessed` for Capture and Judgment — source limitation, not a code defect.

**minimum_closure_condition for not_assessed**: CA verifies that `source_capture_playbook_v0.md` and `judgment_spine_demand_read_machinery_architecture_v0.md` carry DCP receipts acknowledging the recency attention propagation, and that neither leaks recency values into proof, scoring, Capture route binding, or gate clearance.

**next_authorized_action**: CA spot-check the two files' DCP receipt sections. If the prior review's record is locatable and readable, its findings on those surfaces satisfy this gap.

---

## Enforcement Goal Closure Assessment

| Goal | Status | Evidence | Notes |
| --- | --- | --- | --- |
| **E-01** — row-shape burden reduction: required Section 4 recency/current-state and graph-light fields enforced before mechanical handoff-safety can be claimed | `closed` | `REQUIRED_ROW_COLUMNS` now includes `row_purpose`, `recency_status`, `recency_attention`, `graph_role`, `graph_weight_hint`. Missing any column produces `missing_required_row_columns`. All three valid fixtures carry all required columns and pass. `test_signal_board_requires_recency_columns` proves the header check fires when recency columns are stripped. | |
| **E-02** — enum burden reduction: invalid vocabulary for required Section 4 fields fails deterministically | `closed` | `_validate_signal_row_vocab` calls `_validate_vocab_field` for all five new fields using closed enum sets. `test_signal_board_validates_recency_vocab` proves invalid `recency_status` and `recency_attention` produce findings. All seven bad fixtures carry valid recency/graph vocab and still fail for their intended handoff-layer reasons. | AR-01 notes the test coverage gap for `row_purpose`/`graph_role`/`graph_weight_hint` enum mutations; the code is correct and the selftest passes, so the goal is closed at the code level with a test-coverage advisory. |
| **E-03** — non-proof boundary: checker-pass language strictly shape-only | `closed` | CSB prompt: "A validator pass means only that the handoff rows are mechanically eligible under the board's own row table and that Section 4 carries the required recency/current-state attention fields. It is not evidence truth, demand classification, retrieval completion, buyer proof, validation, readiness, attention correctness, or client-facing approval." Playbook: "A pass does not mean: ... recency/current-state attention values prove demand or evidence strength." Adjudication packet: "the attention is not buyer proof, demand classification, classifier mapping, evidence weighting, or graph weight." No proof, scoring, or graph-weight language found in checker code. Scanning spine independently keeps recency as attention weight, not proof. | |
| **E-04** — scope boundary: validator remains manual/local | `closed` | Playbook: "Current enforcement posture: manual/local checker. Not CI, not pre-commit, not a write hook." DCP receipt explicitly explains why `validation-gates.md` was not updated. Prompt body: "Before claiming a full board is mechanically safe for classifier handoff, save the exact board output to a temporary or bound artifact file and run: [command]" — describing manual invocation only. | |

---

## Validation Commands

Validation was **not independently rerun** by this reviewer. Author-supplied evidence only:

**Checker selftest (author-supplied)**:
```powershell
python -B .agents\hooks\check_commission_signal_board_output.py --selftest
```
Observed (author-reported):
```
PASS valid_empty_backtest_output.txt
PASS valid_source_backed_backtest_output.txt
PASS valid_source_backed_forward_output.txt
SELFTEST OK
```

**Unit suite (author-supplied)**:
```powershell
python -B -m pytest -q -p no:cacheprovider tests\unit\test_commission_signal_board_output_validator.py
```
Observed (author-reported):
```
..............                                                           [100%]
```

This reviewer independently confirmed code logic correctness by reading the full checker source and test source. The code paths for each new field are symmetric and correct. Author-supplied validation evidence is plausible given the code structure but is not independently verified.

---

## Residual Risk

1. **Test coverage regression path** (AR-01): A future edit to `_validate_signal_row_vocab` that silently drops one of the three under-tested fields (`row_purpose`, `graph_role`, `graph_weight_hint`) would not be caught by the unit test suite without a self-test run. Low probability; mitigable by adding the suggested tests.

2. **Adjudication packet taxonomy inconsistency** (AR-02): An agent that reads the adjudication packet as the field vocabulary authority may not include `recency_priority` as a valid `row_purpose`. The impact is limited because the prompt is the operational document and the adjudication packet is a decision-prep record.

3. **Capture/Judgment leakage unverified** (AR-04): This reviewer cannot certify that no recency/currentness wording leaked into Capture or Judgment surfaces. The prior review and DCP receipts are the current evidence; CA spot-check is the recommended closure path.

4. **`_normalize_vocab` could accept hyphenated variants**: Values like `"current-state"` normalize to `"current_state"` and pass. This is intentional and correct, not a bug. Documenting as a residual to record that the normalization is deliberate, not an oversight.

---

## Review-Use Boundary

This is a **read-only advisory review**. Findings are decision input for the Chief Architect only. They are not:
- mandatory remediation
- formal PASS or FAIL on the patch
- validation, readiness, or approval
- executor-ready patch authority

The three minor findings (AR-01, AR-02, AR-03) are all correctable in a subsequent commit and none blocks acceptance at the CA's discretion. AR-04 is a source-limitation note, not a defect finding.

---

## DELEGATED_ARTIFACT_REVIEW_RETURN_FOR_HOME_MODEL

```text
DELEGATED_ARTIFACT_REVIEW_RETURN_FOR_HOME_MODEL

Original commission: adversarial mixed code/docs review of the CSB recency
row-shape enforcement patch, commit 28d896c79100db1159c5b0cdf9d897e4734397f0.
Commissioned from workflow-delegated-review-patch route-out.

Reviewer: claude-sonnet-4-6 (Anthropic / Claude family)
Author family: OpenAI / GPT family (Codex)
De-correlation bar: cross_vendor_discovery (satisfied)

Target files reviewed:
  .agents/hooks/check_commission_signal_board_output.py
  orca-harness/tests/unit/test_commission_signal_board_output_validator.py
  orca-harness/tests/fixtures/commission_signal_board_outputs/ (all 10 fixtures)
  orca/product/spines/commission_signal_board/prompts/orca_commission_signal_board_prompt_structure_v0.md
  orca/product/spines/commission_signal_board/workflows/commission_signal_board_playbook_v0.md
  orca/product/spines/commission_signal_board/authority/orca_commission_signal_board_prompt_structure_rules_v0.md

Enforcement goals:
  E-01 (row-shape burden reduction): CLOSED
  E-02 (enum burden reduction): CLOSED (code correct; test coverage gap advisory, see AR-01)
  E-03 (non-proof boundary): CLOSED
  E-04 (scope boundary / manual-local): CLOSED

Findings:
  AR-01 (minor): No dedicated mutation tests for row_purpose, graph_role, graph_weight_hint enum failures.
    Code is correct. Risk: silent regression if _validate_signal_row_vocab is later modified.
    Closure: add 2 targeted mutation tests.
  AR-02 (minor): Adjudication packet's Graph-Light Contract field taxonomy omits recency_priority
    from row_purpose values. Prompt and checker are authoritative and correct.
    Closure: add recency_priority to adjudication packet's taxonomy block or add superseded note.
  AR-03 (minor): recency_priority row_purpose value undefined in Section 4 rules.
    Not a correctness issue; authoring clarity gap.
    Closure: one clarifying sentence in Section 4 rules block.
  AR-04 (not_assessed): Capture/Judgment leakage not directly read. DCP claims prior review cleared.
    Closure: CA spot-check DCP receipts in those two files.

Reviewer verdict: ACCEPT_WITH_FRICTION — implementation is correct, E-01 through E-04 are closed,
three minor advisory findings remain, none blocking. CA adjudicates which if any to close before landing.

Residual risk: test coverage regression path (low), adjudication packet taxonomy inconsistency (low),
unverified Capture/Judgment leakage (unknown — prior review evidence only).

No patch queue (advisory lane; reviewer is read-only).
```
