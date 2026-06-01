# Adversarial Artifact Review — Source Observability Scalability Note v0

```yaml
retrieval_header_version: 1
artifact_role: Adversarial artifact review report
scope: Read-only adversarial review of orca-harness/docs/source_observability_scalability_note.md for safe use as local harness context before a health cleanup lane.
use_when:
  - Deciding whether the scalability note is safe to use as context for a health cleanup lane.
  - Checking whether the note's dry-run lifecycle guidance and boundary claims are consistent with controlling source authorities.
authority_boundary: retrieval_only
```

## Commission

- **Review target**: `orca-harness/docs/source_observability_scalability_note.md`
- **Purpose**: Determine whether the note is safe to use as local harness context before a later repo-health cleanup lane.
- **Expected HEAD**: `27cae7b`
- **Expected SHA256**: `874B3B67BB4B5AE3967D8154647B6EBF7289B20BD854E86AD2056A1B86AF9D23`
- **Commissioning lane**: Adversarial artifact review
- **Output path**: `docs/review-outputs/adversarial-artifact-reviews/source_observability_scalability_note_adversarial_artifact_review_v0.md`

## Source Preflight

### Workspace And Git State

- Repository: `C:\Users\vmon7\Desktop\projects\orca`
- Branch: `main`
- Observed HEAD: `27cae7b` — matches expected HEAD.
- Dirty-state allowance: broad dirty tree is allowed per commission; target note is untracked; `orca-harness/README.md` is modified but unrelated unless the note conflicts with it; `orca-harness/reports/` is entirely untracked with no tracked files.

### Hash Verification

- **Observed SHA256**: `874B3B67BB4B5AE3967D8154647B6EBF7289B20BD854E86AD2056A1B86AF9D23`
- **Expected SHA256**: `874B3B67BB4B5AE3967D8154647B6EBF7289B20BD854E86AD2056A1B86AF9D23`
- **Result**: HASH MATCH — review proceeds.

### Output Mode

- Output mode: `filesystem-output`
- Required output path: `docs/review-outputs/adversarial-artifact-reviews/source_observability_scalability_note_adversarial_artifact_review_v0.md`
- Directory exists: confirmed.

### Skill Invocations

- `workflow-deep-thinking` invoked before framing failure modes — confirmed.
- `workflow-adversarial-artifact-review` invoked after source readiness — confirmed.
- Both skills available and invoked in required order.

### Source-Read Ledger

| Source | Status | Role in this review |
|--------|--------|---------------------|
| `AGENTS.md` | tracked, clean | Agent operating rules; blast-radius authority for doctrine-change propagation |
| `.agents/workflow-overlay/README.md` | modified | Overlay entrypoint; binding rule |
| `.agents/workflow-overlay/source-of-truth.md` | modified | Source hierarchy; doctrine-change propagation contract; Source-Family Promotion Rule |
| `.agents/workflow-overlay/review-lanes.md` | modified | Review lane authority; adversarial artifact review requirements |
| `.agents/workflow-overlay/validation-gates.md` | modified | Validation gates including propagation receipt requirement |
| `.agents/workflow-overlay/safety-rules.md` | modified | Scope discipline |
| `docs/decisions/data_capture_spine_source_observability_local_support_implementation_scoping_authorization_v0.md` | untracked | Controlling local support authorization |
| `docs/product/data_capture_spine_source_observability_requirements_scoping_v0.md` | untracked | Candidate requirements; source-family framing |
| `docs/product/core_spine_v0_data_capture_spine_obligation_contract_v0.md` | modified | Controlling Data Capture obligation contract; Source-Family Promotion Rule |
| `docs/product/core_spine_v0_data_and_cleaning_spine_boundary_v0.md` | modified | Controlling Data Capture/Cleaning/Judgment boundary; Source-Family Promotion Rule |
| `orca-harness/source_observability/models.py` | untracked | Current field names and model structure |
| `orca-harness/source_observability/checker.py` | untracked | Current limitation type enumeration; check logic |
| `orca-harness/runners/run_source_observability_report.py` | untracked | Report output structure; NON_CLAIMS; record_summaries invariant |
| `orca-harness/docs/source_observability_operator_records.md` | untracked | Operator-facing records guide |
| `orca-harness/docs/source_observability_operator_records_template.yaml` | untracked | Operator-facing template |
| `orca-harness/README.md` | modified | Harness-level boundary statements; consistency check surface |

All overlay sources are modified but are relied on as advisory authority under the dirty-state allowance. No strict source-of-truth promotion or validation claim depends on these sources being clean; the review uses them only as boundary context.

### Lane Collision Check

- Target is a non-code harness documentation note, not implementation, code, tests, or runtime.
- Review purpose is source-backed adversarial critique of the note as pre-cleanup context.
- No collision with implementation review, postmortem review, or prompt orchestration lanes.
- Lane: **adversarial artifact review** — confirmed, no collision.

### Review Scope

**In scope**: Whether the note is safe to use as local harness context before a health cleanup lane, per the 12 adversarial questions.

**Excluded scope**: Implementation review of `checker.py`, `models.py`, or the runner; fixture acceptance; product-doctrine acceptance; source-access authorization; health cleanup execution; ECR design; Cleaning or Judgment design.

---

## Reviewer Deep-Thinking Summary

Before findings: identified the actual failure mode space as five candidate threat vectors:

1. **Doctrine leak**: the note claiming to be harness-local while smuggling a new product rule.
2. **Propagation escape**: the note changing a lifecycle boundary without a receipt.
3. **Boundary inversion**: the note asserting authority over controlling sources rather than subordinating to them.
4. **Cleanup pre-authorization**: the dry-run lifecycle section providing advance scope for a cleanup action before authorization exists.
5. **Fake-pass path**: a clean report being readable as a validation pass.

All five were tested against source evidence. The note does not trigger any of the five threat vectors at blocker level. Two advisory issues were found, both wording/clarity matters that can travel without preventing cleanup lane use.

---

## Findings

### Phase 1 — Correctness

#### AR-01 — Advisory: Non-Claims Section Does Not Explicitly Disclaim Cleanup Authorization Or Reports-Tree Policy

- **Finding ID**: AR-01
- **Severity**: Advisory/minor
- **Phase**: Correctness
- **Location anchor**: Note, section "Non-Claims" (final section)
- **Source evidence**: The commission context is specifically that this note will be used as context for a later health cleanup lane. The note's "Dry-Run Output Lifecycle" section contains substantive guidance about what cleanup should NOT do (bless, delete, move, or ignore the whole `orca-harness/reports/` tree) and what it COULD target if authorized (specific file patterns). This guidance is conditional and advisory, but a health cleanup agent reading the note without full source context might not see an explicit disclaimer in the non-claims section that the note does not constitute cleanup authorization.
- **Artifact evidence**: The non-claims section reads: "This note is not validation, readiness, fixture acceptance, source-of-truth promotion, source acquisition, archive retrieval, media preservation, browser automation, ECR receipt, Cleaning output, Judgment output, source-quality scoring, buyer proof, or commercial-readiness evidence." None of these entries address health cleanup authorization or reports-tree policy.
- **Body language**: The body contains adequate conditional language: "If later cleanup or `.gitignore` work is authorized..." and "The broader untracked `orca-harness/reports/` state is a repo-health issue, not part of this note's local support scope." These body statements are correct.
- **Requirement**: AGENTS.md: "Preserve real failure visibility; never create fake success paths." The non-claims section is the first surface a cleanup agent may check for boundary claims. Omitting the cleanup non-claim is not a fake success, but it is a boundary-visibility gap for the specific downstream use case.
- **Impact**: A health cleanup agent reading the non-claims section without reading the full body may not see an explicit disclaimer that the note does not authorize cleanup, `.gitignore` entries, or reports-tree policy. The body language is adequate; the non-claims section is weaker than the body.
- **Must be patched before health cleanup**: No. Body language in "Dry-Run Output Lifecycle" is explicit and correct. The missing entry is a clarity improvement, not a safety blocker.
- **Minimum closure condition**: Non-claims section includes at least one entry such as "not health cleanup authorization, not `.gitignore` or file-pattern policy, not reports-tree policy."
- **Next authorized action**: Owner decision on whether to patch the non-claims section before health cleanup lane begins. Advisory only; patch authorization is a separate step.
- **`patch_queue_entry` authorized**: No — this review is read-only. Advisory direction only.
- **Strict claims**: Not proven; this review does not grant patch authority.

---

#### AR-02 — Advisory: Dry-Run Lifecycle Section Pre-Scopes Cleanup File Patterns Without Labeling Guidance As Illustrative

- **Finding ID**: AR-02
- **Severity**: Advisory/minor
- **Phase**: Correctness
- **Location anchor**: Note, section "Dry-Run Output Lifecycle," paragraph beginning "If later cleanup or `.gitignore` work is authorized..."
- **Source evidence**: The authorization document (`data_capture_spine_source_observability_local_support_implementation_scoping_authorization_v0.md`) does not authorize cleanup scoping or `.gitignore` planning. The note's purpose is to describe scalability of the local helper. The dry-run lifecycle section correctly conditions its guidance on future authorization ("if later cleanup...is authorized"), but it names specific file patterns: `*_dry_run.yaml` and `*_dry_run.json`.
- **Artifact evidence**: "If later cleanup or `.gitignore` work is authorized, target specific dry-run file patterns such as source-observability `*_dry_run.yaml` and `*_dry_run.json`, not the entire `orca-harness/reports/` tree." The phrase "such as" before the patterns makes the guidance illustrative rather than prescriptive. The conditional "if later cleanup...is authorized" preserves the authorization gate.
- **Concern**: The word "target" in "target specific dry-run file patterns" is mildly imperative. A cleanup agent reading this note as context might read the pattern specification as implicit pre-scoping rather than illustrative guidance. The note does not explicitly label this as an example or note that the actual patterns must be confirmed against the actual file naming in `orca-harness/reports/source_observability/` at the time of cleanup.
- **Verification gap**: `orca-harness/reports/` is entirely untracked and has no tracked files (confirmed by `git ls-files -- orca-harness/reports`). The actual file naming convention used in any dry-run outputs is not confirmed by this review. If operators did not name files with the `_dry_run` suffix, the suggested patterns would not match.
- **Requirement**: AGENTS.md: "Every changed line must trace to the user request or required validation." The pattern specification traces to the note's scalability context, but the patterns are not verified against actual repo contents.
- **Impact**: Low. The conditional language ("if...authorized") and "such as" preserve the advisory nature. This is not a blocker. But a cleanup agent could treat the illustrative patterns as confirmed cleanup scope.
- **Must be patched before health cleanup**: No. The conditional and "such as" language is adequate. This is a wording hardening opportunity.
- **Minimum closure condition**: The dry-run lifecycle section either (a) explicitly labels the named file patterns as illustrative examples that must be confirmed against actual file contents before use, or (b) removes the specific pattern names in favor of a general description.
- **Next authorized action**: Owner decision on whether to harden the wording before the health cleanup lane reads this note. Advisory only.
- **`patch_queue_entry` authorized**: No.
- **Strict claims**: Not proven.

---

### Phase 2 — Friction

No friction findings. The note is appropriately concise. The sections are directly useful for health cleanup context. No redundant instructions, unclear routing, or unnecessary manual work identified within the health cleanup use case.

---

## Adversarial Question Disposition

| # | Question | Finding | Verdict |
|---|----------|---------|---------|
| 1 | Does the note accidentally introduce product doctrine? | No. Preamble explicitly claims harness-local status. All rules in the body apply existing boundaries locally. The extension/promotion rule restates the Source-Family Promotion Rule from the obligation contract and boundary document without changing it. | Clear |
| 2 | Does it require a direction_change_propagation receipt? | No. The note does not change any controlling source, obligation contract, or lifecycle boundary. It applies existing boundaries at the local helper level. No new durable rule is created that future agents would follow as doctrine. No-propagation posture is defensible. | Clear |
| 3 | Does it stay subordinate to the three controlling authorities? | Yes. The preamble explicitly declares subordination to all three: obligation contract, Data Capture/Cleaning/Judgment boundary, and local support authorization. Each section is consistent with those authorities. | Clear |
| 4 | Does it correctly preserve the local helper boundary? | Yes. The "Local Helper Boundary" section is a well-formed list matching the authorization document's "Forbidden Outputs." The not-extracted-source-truth claim is correct. The not-a-required-handoff-gate claim appears in both the preamble and the "Report Output Invariants" section. Human posture judgment is correctly preserved. | Clear |
| 5 | Does the source-slice record discipline match the anti-rollup and source-family promotion rules? | Yes. The anti-rollup guidance ("Do not collapse divergent states...") mirrors Obligation 10 of the obligation contract exactly. The extension/promotion rule ("at least two non-overlapping source families...or owner explicitly signs off on one specific invariant claim") matches the Source-Family Promotion Rule in both controlling sources word-for-word. | Clear |
| 6 | Does it preserve both report invariants: `record_summaries` and `non_claims`? | Yes. Both invariants are named and described in the "Report Output Invariants" section. Both are present in the runner implementation. The `record_summaries` invariant is described with the correct purpose (keeping operator posture records inspectable next to emitted limitation types). The `non_claims` invariant is described with the correct purpose (preventing reports from reading as validation/readiness). | Clear |
| 7 | Does the extension/promotion rule match the controlling source-family promotion rule, including the two non-overlapping source-family bar or owner signoff for one specific invariant? | Yes. The note's rule matches both the obligation contract (§ "Source-Family Promotion") and the boundary document (§ "Source-Family Promotion Rule") exactly. The owner-signoff specificity requirement ("attaches to the specific invariant, not a broad category") mirrors the contract's language. | Clear |
| 8 | Does the dry-run lifecycle section correctly target only dry-run YAML/JSON scratch outputs and avoid blessing, deleting, ignoring, or restructuring all of orca-harness/reports/? | Yes. The section explicitly prohibits ignoring, deleting, moving, or blessing the entire `orca-harness/reports/` directory. It correctly separates dry-run YAML (input) from dry-run JSON (output). The advisory pattern guidance is conditional. The `git ls-files` check confirms no files in `orca-harness/reports/` are tracked, which the section's protective language correctly assumes. | Clear with AR-02 advisory |
| 9 | Does the note accidentally start the later health cleanup? | No. No `.gitignore` entries are prescribed. No file moves are specified. No fixture policy is established. No reports-tree cleanup is executed. The dry-run lifecycle section is explicitly conditional ("if later cleanup...is authorized"). | Clear |
| 10 | Are there any stale field names or mismatches against current helper implementation? | No. All field names in the note (source language, visible source structure, archive body, media/layout, access, locator, cutoff, limitation notes) map to current `models.py` fields. Both report invariants (`record_summaries`, `non_claims`) are present in the runner. The `ObservablePosture` values referenced in the operator records guide match the `StrEnum` in `models.py`. | Clear |
| 11 | Are there any fake-success paths? | No. The note explicitly states: "A report with no emitted limitations is not a pass. It only means the supplied operator records did not expose limitations the helper knows how to flag." This is a strong, explicit anti-fake-success statement. The runner's `has_visible_limitations` field is a boolean data flag, not a pass verdict. `NON_CLAIMS` includes "not capture validation" and "not capture readiness." | Clear |
| 12 | Are there any missing non-claims that would be needed before health cleanup uses the note? | Yes — advisory. The non-claims section does not explicitly disclaim health cleanup authorization or reports-tree policy. Body language is adequate, but the non-claims section is the first surface a cleanup agent may check. See AR-01. | AR-01 advisory |

---

## Source-Boundary Spot Checks

**Does the note conflict with the modified orca-harness/README.md?**

The README says: "local source-observability support checks only, not source acquisition." The note says the helper must not "acquire sources." Consistent. The README's non-claim inventory matches the note's non-claims section. No conflict.

**Does the `record_summaries` implementation match the note's description?**

The runner calls `_record_summary(record)` which calls `record.model_dump(mode="json")`. This returns the full operator record as a JSON-compatible dict. The note says `record_summaries` keeps "each operator posture record...inspectable next to the emitted limitation types." The implementation is consistent: every field of every operator record appears in the summary, not just the limitation-triggering fields.

**Does the checker emit limitations for all non-preserved access postures?**

`_check_access_failure` fires for `INACCESSIBLE` and `FAILED` access postures. `NOT_ATTEMPTED` access posture is not in `ACCESS_FAILURE_POSTURES` and is not included in `_check_unnoted_non_preserved_postures`'s `checked_postures` set (which covers only the four source/archive/media/structure fields). This means `access_posture: not_attempted` without a limitation note produces no dedicated limitation, though the value remains visible in `record_summaries`. The note does not claim that all non-preserved access postures produce dedicated limitations; it says the helper should "expose" operator posture, which `record_summaries` fulfills. This implementation choice is consistent with the note's framing and does not constitute a stale field or a claim mismatch.

**Does `_check_unnoted_non_preserved_postures` short-circuit on any limitation note?**

Yes. If any limitation note is non-empty, the function returns `[]` for the whole record. This means a record with one limitation note and three non-preserved postures in the checked fields will not emit `unnoted_non_preserved_posture` for those fields. The note does not describe this behavior, but does not claim it either. The `record_summaries` invariant mitigates this: all posture values remain visible regardless. This is not a note-level finding.

---

## Verdict

```yaml
adversarial_review_verdict:
  target: orca-harness/docs/source_observability_scalability_note.md
  hash_verified: true
  observed_hash: 874B3B67BB4B5AE3967D8154647B6EBF7289B20BD854E86AD2056A1B86AF9D23
  verdict: safe_for_health_cleanup_context
  blocker_or_major_findings: 0
  advisory_findings: 2
  findings:
    - id: AR-01
      severity: advisory
      topic: Non-claims section missing explicit cleanup-scope disclaimers
      must_patch_before_cleanup: false
    - id: AR-02
      severity: advisory
      topic: Dry-run lifecycle pre-scopes file patterns without labeling guidance as illustrative
      must_patch_before_cleanup: false
  clean_adversarial_questions: 10 of 12 (two generate the above advisory findings)
  direction_change_propagation_required: false
  no_propagation_posture_defensible: true
  fake_success_paths: none
  stale_fields: none
  doctrine_drift: none
  cleanup_pre_authorization: none
```

The note is safe to use as local harness context before the health cleanup lane. No blocking or major issues were found. The two advisory findings are wording and clarity matters. Neither prevents cleanup lane use. The note correctly applies existing boundaries, does not introduce product doctrine, does not require a direction-change propagation receipt, does not create a required handoff gate, does not accidentally start cleanup, preserves both report invariants, and contains no fake-success paths or stale field names.

If the owner chooses to patch before cleanup lane use, the minimum changes are:
1. Add "not health cleanup authorization, not `.gitignore` or file-pattern policy, not reports-tree policy" to the non-claims section (AR-01).
2. Label the named file patterns in the dry-run lifecycle section as illustrative examples to be confirmed against actual file naming at cleanup time (AR-02).

Neither patch changes the note's scope, boundary claims, or any controlling source authority.

---

## Non-Claims

This review is not validation, readiness, fixture acceptance, implementation authorization, health cleanup execution, product-doctrine acceptance, source-access authorization, ECR design, Cleaning implementation, Judgment design, buyer proof, or commercial-readiness evidence.

Review findings are decision input only. They are not approval, validation, mandatory remediation, or executor-ready patch authority until separately accepted or authorized by the owner or a patch execution lane.
