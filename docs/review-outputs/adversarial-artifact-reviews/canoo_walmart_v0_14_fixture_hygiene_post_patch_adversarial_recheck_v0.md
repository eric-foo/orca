# Canoo/Walmart v0.14 Fixture Hygiene Post-Patch Adversarial Recheck v0

```yaml
retrieval_header_version: 1
artifact_role: Review report
scope: Bounded post-hygiene adversarial recheck for HF-01/HF-02/HF-03 closure and patch-caused regression check in the Canoo/Walmart v0.14 docs-only fixture pack.
use_when:
  - Verifying that the whole-fixture hygiene patch closed HF-01, HF-02, and HF-03 without introducing blocker or major regression.
  - Routing the next authorized step after hygiene acceptance.
authority_boundary: retrieval_only
```

```yaml
review_summary:
  status: completed
  report_path: docs/review-outputs/adversarial-artifact-reviews/canoo_walmart_v0_14_fixture_hygiene_post_patch_adversarial_recheck_v0.md
  recommendation: accept
  summary: "HF-01, HF-02, and HF-03 are closed; no blocker or major patch-caused regression was found in the touched patch scope or directly dependent hash/status surfaces."
  findings_count: 0
  blocking_findings: []
  advisory_findings: []
  prior_findings_remediated:
    - HF-01
    - HF-02
    - HF-03
  blast_radius_result: "no blocker or major patch-caused regression found"
  next_action: "Owner may accept whole-fixture hygiene and record the accepted recheck hash in the fixture authoring receipt; do not route to blind use, probe execution, scoring, schema implementation, ledger freeze, validation, proof-run, product proof, or judgment-quality claims."
```

---

## 1. Commission

Run a read-only bounded post-hygiene adversarial recheck of the Canoo/Walmart v0.14 docs-only fixture pack.

This is a patch recheck, not a full fixture review. Scope is limited to:

1. Whether HF-01, HF-02, and HF-03 from the whole-fixture hygiene review are closed.
2. Whether the hygiene patch introduced any blocker or major regression inside the touched patch scope or directly dependent hash/status surfaces.

This review did not assess scoring readiness, schema implementation readiness, blind-use readiness, validation, case judgment quality, Canoo/Walmart outcome interpretation, model memorization, or schema design. No fixture source files were edited. The only write is this report.

Required boundary: plumbing works only; not judgment quality.

---

## 2. Target

Primary post-hygiene patched sources:

- `docs/research/judgment-spine/harness/v0_14/fixtures/canoo_walmart_2022_v0_14/fixture_authoring_receipt_v0.md`
- `docs/research/judgment-spine/harness/v0_14/fixtures/canoo_walmart_2022_v0_14/protocol_pydantic_reconciliation_decision_v0.md`
- `docs/research/judgment-spine/harness/v0_14/fixtures/canoo_walmart_2022_v0_14/source_manifest_participant_safe_adapter_decision_v0.md`
- `docs/research/judgment-spine/harness/v0_14/fixtures/canoo_walmart_2022_v0_14/participant_packet_draft_v0.md`

Prior hygiene review being rechecked:

- `docs/review-outputs/adversarial-artifact-reviews/canoo_walmart_v0_14_fixture_hygiene_adversarial_review_v0.md`

Accepted prior recheck reports consulted for provenance:

- `docs/review-outputs/adversarial-artifact-reviews/canoo_walmart_v0_14_draft_fixture_pack_post_patch_adversarial_recheck_v0.md`
- `docs/review-outputs/adversarial-artifact-reviews/canoo_walmart_source_manifest_adapter_decision_post_patch_adversarial_recheck_v0.md`
- `docs/review-outputs/adversarial-artifact-reviews/canoo_walmart_protocol_pydantic_reconciliation_decision_post_patch_adversarial_recheck_v0.md`

Report output path (pre-write collision check: clear):

- `docs/review-outputs/adversarial-artifact-reviews/canoo_walmart_v0_14_fixture_hygiene_post_patch_adversarial_recheck_v0.md`

---

## 3. Authority and Source Context

```yaml
orca_start_preflight:
  agents_read: yes
  overlay_read: yes
  source_pack: custom S4 review — required overlay authorities, four pinned post-hygiene fixture artifacts, one hygiene review report, and three accepted prior recheck reports
  edit_permission: read-only reviewed artifacts; docs-write for this report only
  target_scope: bounded HF-01/HF-02/HF-03 closure check and patch-caused regression scan only
  dirty_state_checked: yes
  blocked_if_missing: no
source_context_status: SOURCE_CONTEXT_READY
workspace_state:
  expected_branch: main
  actual_branch: main
  expected_head: a2aebdd
  actual_head: a2aebdd
  worktree_dirty: yes
  dirty_state_note: >
    Multiple overlay files and many docs are modified or untracked. The fixture
    directory is untracked. This review proceeds from user-pinned source hashes
    only. Dirty overlay state and untracked fixture state are source-ledger
    caveats, not validation or readiness evidence.
method_sequence:
  workflow_deep_thinking_reference_loaded: yes
  workflow_adversarial_artifact_review_reference_loaded: yes
  methods_applied_only_after_source_context_ready: yes
dirty_state_boundary: >
  The Canoo/Walmart fixture directory is currently untracked/dirty. That is allowed
  for this bounded recheck only because the prompt pins exact source hashes. Dirty
  state is not validation, readiness, acceptance, score-readiness, blind-use
  readiness, source-of-truth promotion, or judgment-quality evidence.
```

Authority reads completed before source loading:

- `AGENTS.md`
- `.agents/workflow-overlay/README.md`
- `.agents/workflow-overlay/source-loading.md`
- `.agents/workflow-overlay/prompt-orchestration.md`
- `.agents/workflow-overlay/review-lanes.md`
- `.agents/workflow-overlay/communication-style.md`

Methods reference-loaded before source loading:

- `workflow-deep-thinking` (reference only; not applied until SOURCE_CONTEXT_READY)
- `workflow-adversarial-artifact-review` (reference only; not applied until SOURCE_CONTEXT_READY)

---

## 4. Hash Verification Table

All hashes computed with SHA-256 from on-disk bytes at expected workspace paths.

### Primary Post-Hygiene Patched Sources

| Source | Required Hash | Computed Hash | Result |
| --- | --- | --- | --- |
| `fixture_authoring_receipt_v0.md` | `AC4B916927E5AE39FD13FAC453693A05193F7FD78DD83594FA2F1342F98E2C44` | `AC4B916927E5AE39FD13FAC453693A05193F7FD78DD83594FA2F1342F98E2C44` | **matched** |
| `protocol_pydantic_reconciliation_decision_v0.md` | `5109052BBB38B62E4A787E57FAC257797043E752EFF940B8304401996A434AF1` | `5109052BBB38B62E4A787E57FAC257797043E752EFF940B8304401996A434AF1` | **matched** |
| `source_manifest_participant_safe_adapter_decision_v0.md` | `D6A0421094A41A19F938714F63A76E50AE94DAA92A2952DFE308A2C3458CCABD` | `D6A0421094A41A19F938714F63A76E50AE94DAA92A2952DFE308A2C3458CCABD` | **matched** |
| `participant_packet_draft_v0.md` | `EBA60C529ACBBA07324983FCAA5A48F268454A93F39C0F5D755DB9DCBB068CFB` | `EBA60C529ACBBA07324983FCAA5A48F268454A93F39C0F5D755DB9DCBB068CFB` | **matched** |

### Prior Hygiene Review Being Rechecked

| Source | Required Hash | Computed Hash | Result |
| --- | --- | --- | --- |
| `canoo_walmart_v0_14_fixture_hygiene_adversarial_review_v0.md` | `41595CB8D431DC3F0D95C816F38D7241E2C4702301775152D3BFBD7586C7CBA0` | `41595CB8D431DC3F0D95C816F38D7241E2C4702301775152D3BFBD7586C7CBA0` | **matched** |

### Accepted Prior Recheck Reports

| Source | Required Hash | Computed Hash | Result |
| --- | --- | --- | --- |
| `canoo_walmart_v0_14_draft_fixture_pack_post_patch_adversarial_recheck_v0.md` | `DEF486F288A43BB63647C72E4EF59A22FD6A155E38E3BE76FB28A06CE6675629` | `DEF486F288A43BB63647C72E4EF59A22FD6A155E38E3BE76FB28A06CE6675629` | **matched** |
| `canoo_walmart_source_manifest_adapter_decision_post_patch_adversarial_recheck_v0.md` | `6785B63D32EFF8266D517BFDB0FBA3F36B99BB1EE8638FBB10DD91B5CF08855D` | `6785B63D32EFF8266D517BFDB0FBA3F36B99BB1EE8638FBB10DD91B5CF08855D` | **matched** |
| `canoo_walmart_protocol_pydantic_reconciliation_decision_post_patch_adversarial_recheck_v0.md` | `6C884828AFCC75BB8B6D286A36D544E522C39EF3A2C2B3760B71E19AB3EF6CF2` | `6C884828AFCC75BB8B6D286A36D544E522C39EF3A2C2B3760B71E19AB3EF6CF2` | **matched** |

All 8 required source hashes matched. SOURCE_CONTEXT_READY declared.

---

## 5. HF-01/HF-02/HF-03 Closure Findings

### HF-01 — Protocol/Pydantic decision artifact stale-status contradiction

**Finding from prior review:** The decision artifact still said "Decision-basis status: pending review; not owner-accepted" and "post-patch adversarial recheck and owner acceptance not completed" while the receipt and accepted recheck already showed an accepted docs-only decision basis.

**Post-patch state in `protocol_pydantic_reconciliation_decision_v0.md`:**

The status block now reads:
- "Status: accepted docs-only field-placement decision basis for next fixture step."
- "Decision-basis status: accepted after post-patch adversarial recheck and owner-directed receipt housekeeping; not schema implementation ready, not ledger-freeze ready, not blind-use ready, and not score-ready."

The `input_hashes` section now pins both the accepted post-patch recheck report (`protocol_pydantic_reconciliation_decision_post_patch_adversarial_recheck_v0.md: 6C884828...`) and the post-reconciliation-acceptance receipt hash (`fixture_authoring_receipt_v0.md: 32C99D99...`). The hash `6C884828...` matches the verified recheck report hash. ✓

The `remaining_blockers` section no longer lists "post-patch adversarial recheck and owner acceptance not completed." It now correctly lists "whole-fixture hygiene acceptance not completed after this status-refresh patch," which refers to the current post-hygiene recheck, not the previously-completed protocol/Pydantic recheck. ✓

The "Next authorized step" correctly routes to: "Run a bounded post-hygiene recheck for HF-01 closure and patch-caused regressions before whole-fixture hygiene acceptance." This is a forward-pointing statement about the current recheck, not a backward reference to an uncompleted prior step. ✓

No-readiness boundaries are preserved throughout: "not schema implementation ready, not ledger-freeze ready, not blind-use ready, and not score-ready" plus the full non-claims section covering schema implementation, ledger freeze, scoring readiness, blind-use readiness, validation, and judgment-quality claims. ✓

The `hash_loop_boundary` section is present and explains the one-cycle authoring sequence:
- `fixture_authoring_receipt_v0.md_pre_linkage_authoring_hash: DB80D5576553CFFEBEE86B987287AE8EC0A6CDB17FB6BAACEA7A5E4A970DD2B2`
- `fixture_authoring_receipt_v0.md_post_reconciliation_acceptance_hash: 32C99D992411CB88F536E4C9E6C706007454F731272F774397DAA95CC4B4F1E9`
- Rule documents that the input_hashes entry pins the pre-final-hygiene-patch receipt state. ✓

**HF-01 closure verdict: CLOSED.** All four closure criteria satisfied:
1. No longer says review or owner acceptance are pending. ✓
2. No longer lists post-patch adversarial recheck / owner acceptance as incomplete. ✓
3. Presents the decision as accepted only as a docs-only field-placement basis for the next fixture step. ✓
4. Preserves all no-readiness boundaries. ✓

---

### HF-02 — Source-manifest adapter stale receipt hash and missing accepted recheck pin

**Finding from prior review:** The adapter's `input_hashes` still pinned `fixture_authoring_receipt_v0.md: DB80D557...` (the stale original authoring hash), and the accepted post-patch recheck hash was present only in the source-read ledger, not in `input_hashes`. No explicit hash-loop boundary was documented.

**Post-patch state in `source_manifest_participant_safe_adapter_decision_v0.md`:**

The `input_hashes` section now pins:
- `fixture_authoring_receipt_v0.md: 32C99D992411CB88F536E4C9E6C706007454F731272F774397DAA95CC4B4F1E9` — the post-reconciliation-acceptance receipt hash, replacing the stale `DB80D557...` original authoring hash. ✓
- `source_manifest_adapter_post_patch_adversarial_recheck_v0.md: 6785B63D32EFF8266D517BFDB0FBA3F36B99BB1EE8638FBB10DD91B5CF08855D` — the accepted recheck is now in durable `input_hashes`, not only in the source-read ledger. ✓ Hash matches verified recheck. ✓

The `hash_loop_boundary` section is now present:
- `fixture_authoring_receipt_v0.md_original_authoring_hash: DB80D5576553CFFEBEE86B987287AE8EC0A6CDB17FB6BAACEA7A5E4A970DD2B2` (retained for auditability)
- `fixture_authoring_receipt_v0.md_post_reconciliation_acceptance_hash: 32C99D992411CB88F536E4C9E6C706007454F731272F774397DAA95CC4B4F1E9`
- Rule: "The input_hashes entry pins the receipt state available before this source-manifest hygiene patch. The receipt may separately pin this adapter's post-hygiene hash after this update. Do not treat these hashes as a mutual final-state hash lock." ✓

The expected post-hygiene one-cycle loop is coherent: the adapter (D6A042...) pins the receipt at its pre-final-hygiene-patch state (32C99D99...), and the receipt (AC4B91...) pins the adapter's post-hygiene hash (D6A042...). Both sides document this loop explicitly. The receipt's `hash_loop_boundary` confirms: "The receipt pins the adapter's current post-hygiene hash. The adapter separately pins the receipt hash available before this hygiene patch. Do not treat these two hashes as a mutual final-state hash lock." ✓

Source-manifest adapter status remains `SOURCE_MANIFEST_ADAPTER_DECISION_ACCEPTED_FOR_NEXT_FIXTURE_STEP_NOT_BLIND_USE_READY`. No blind-use readiness, probe, scoring, ledger-freeze, schema implementation, validation, proof-run, or lesson-promotion claims introduced. ✓

**HF-02 closure verdict: CLOSED.** All four closure criteria satisfied:
1. No longer pins stale `DB80D557...` as the live receipt hash; now pins `32C99D99...`. ✓
2. Accepted source-manifest post-patch recheck hash is pinned in `input_hashes`, not only in the source-read ledger. ✓
3. Hash-loop boundary is explicitly documented, identifying which hash is current, which is historical, and that the loop is a one-cycle authoring artifact. ✓
4. Source-manifest adapter status preserved as docs-only next-step basis, not blind-use readiness. ✓

---

### HF-03 — Participant packet blocker list stale relative to accepted recheck state

**Finding from prior review:** The packet's blocker list still said "This draft has not been adversarially re-reviewed after the DFP-01 participant-visible case ID patch" and "A participant-safe source-manifest adapter or explicit non-blind fixture mode must be accepted before use," routing operators to a gate that had already been closed.

**Post-patch state in `participant_packet_draft_v0.md`:**

The "Draft Blockers Before Blind Use" section now reads:

1. "Raw v0.14 source-manifest URLs, titles, and filenames are withheld because they reveal company identity and source context."
2. "The participant-visible `case_id` is a non-identifying alias; internal fixture linkage to `canoo_walmart_2022_v0_14` still needs an authorized harness/rendering path before any blind run."
3. "The docs-only participant-safe source-manifest adapter decision is accepted for the next fixture step, but it is not a harness implementation and does not make this packet blind-use-ready."
4. "Source-byte hashes and retrieval timestamps remain unresolved."
5. "DFP-01 through DFP-05 were closed by post-patch adversarial recheck; blind use still requires a clean participant packet hash, harness/rendering linkage, memorization probe, and downstream fixture gates."
6. "Memorization probe has not been run for any target model family."

The stale DFP-01-not-re-reviewed language is gone. ✓
The stale "adapter must be accepted before use" language is gone and replaced with "adapter decision is accepted for the next fixture step, but it is not a harness implementation and does not make this packet blind-use-ready." ✓
DFP-01 through DFP-05 are correctly labeled as closed. ✓
Remaining blind-use blockers are preserved and precisely named:
- harness/rendering linkage ✓
- clean participant packet hash ✓
- source-byte hashes ✓
- retrieval timestamps ✓
- memorization probe ✓
- downstream fixture gates ✓

The distinction between closed hygiene gates and still-open blind-use gates is explicit in blocker 5: "DFP-01 through DFP-05 were closed by post-patch adversarial recheck; blind use still requires..." ✓

**HF-03 closure verdict: CLOSED.** All four closure criteria satisfied:
1. No longer says the DFP-01 patch has not been adversarially re-reviewed. ✓
2. No longer says a participant-safe source-manifest adapter decision still needs acceptance as if that gate is open. ✓
3. Distinguishes closed hygiene gates from still-open blind-use gates. ✓
4. Preserves all remaining blind-use blockers by name. ✓

---

## 6. Bounded Blast-Radius Findings

Scan limited to the touched patch scope (four primary fixture artifacts) and directly dependent hash/status surfaces.

### New stale live hashes caused by the hygiene patch

**Documented one-cycle hash loop — not a stale-hash defect.**

The hygiene patch updated the adapter (now D6A042...) and the reconciliation decision (5109052...) before updating the receipt (now AC4B91...). As a result:

- The adapter pins `fixture_authoring_receipt_v0.md: 32C99D99...` — the receipt's pre-final-hygiene-patch hash, not the current hash `AC4B91...`.
- The reconciliation decision pins `fixture_authoring_receipt_v0.md: 32C99D99...` — same intermediate hash.
- The receipt pins both the adapter's post-hygiene hash `D6A042...` and the reconciliation decision's post-hygiene hash `5109052...`, both of which are current. ✓

Both the adapter and the reconciliation decision have explicit `hash_loop_boundary` sections documenting this one-cycle authoring sequence. The receipt's `hash_loop_boundary` mirrors the explanation from the receipt side. The loop is consistently documented in all three artifacts and carries no contradictory claims.

No undocumented stale live hash was found. ✓

### Receipt/header hash loops — undocumented or contradictory

No undocumented loop found. The three cross-referenced hash relationships (adapter↔receipt, reconciliation-decision↔receipt) are each documented with consistent boundary language on both sides. No artifact claims its own hash as final-state-locked or uses cross-hash references to imply a validation status. ✓

### Accidental readiness, validation, or claim upgrade

No accidental readiness claim introduced. All four primary artifacts preserve their pre-patch no-readiness posture:
- Receipt: "DRAFT_FIXTURE_PACK_BLOCKED_BEFORE_SCORING"; `post_patch_status: hygiene_patch_applied_pending_post_patch_recheck_not_validated_not_score_ready` ✓
- Reconciliation decision: "not schema implementation ready, not ledger-freeze ready, not blind-use ready, and not score-ready" ✓
- Source-manifest adapter: "SOURCE_MANIFEST_ADAPTER_DECISION_ACCEPTED_FOR_NEXT_FIXTURE_STEP_NOT_BLIND_USE_READY"; fixture status still blocked before blind use, probe, scoring, ledger freeze, schema implementation, validation, proof-run, or lesson promotion ✓
- Participant packet: "PARTICIPANT_PACKET_DRAFT_NOT_BLIND_USE_READY" ✓

### Participant-facing leakage introduced by blocker text or source-manifest changes

No new participant-facing leakage found. The participant packet's frontmatter and participant-facing body remain unchanged from the prior accepted DFP post-patch state. The updated blocker text is in the non-participant-facing section after "Participant-Facing Packet Ends." Source-manifest entries continue to use only `PARTICIPANT_SAFE_SOURCE_ALIAS_CW_P*_RAW_LOCATOR_WITHHELD` and `WITHHELD_OR_PLACEHOLDER_BEFORE_SEAL` placeholders. ✓

### Collapse of distinct acceptance scopes

No scope collapse found. DFP recheck, source-manifest adapter decision, protocol/Pydantic reconciliation decision, and whole-fixture hygiene review remain conceptually separate and are labeled separately in the receipt. No artifact conflates these into a single acceptance surface. ✓

### Next-authorized-step drift toward runtime work

No drift found. The receipt's next authorized step is: "The next authorized step is a bounded post-hygiene adversarial recheck for HF-01 through HF-03 closure and patch-caused regressions." Exclusions are explicit: "Do not route directly to blind use, probe execution, model runs, scoring, ledger freeze, schema implementation, validation, proof-run, product-proof, lesson promotion, or harness-superiority claims." ✓

The reconciliation decision's next authorized step routes to the current recheck before whole-fixture hygiene acceptance. ✓

---

## 7. Non-Findings and Preserved Boundaries

**No overclaim on HF closure.** The patch correctly resolves the three stale-status and stale-hash defects without asserting that hygiene closure constitutes acceptance, validation, readiness, scoring, blind-use authorization, or judgment-quality evidence. The receipt's `post_patch_status` is correctly "pending_post_patch_recheck_not_validated_not_score_ready" — the hygiene patch itself does not claim to have completed the post-hygiene recheck.

**No score-readiness, blind-use readiness, schema implementation readiness, or ledger-freeze readiness claim** was found in any of the four primary artifacts. The extensive "still_blocked" lists in the receipt, reconciliation decision, and adapter are unchanged and accurate.

**No participant-packet cleanliness claim.** The participant packet hash for fixture use remains `NOT_COMPUTED` in the receipt. ✓

**No harness implementation claim.** The adapter is labeled as a docs-only decision basis. No artifact claims the harness has been implemented or that the participant-visible source-manifest has been rendered through a harness path. ✓

**No judgment-quality, proof-run, product-proof, or lesson-promotion claim** was found anywhere in the patched scope. ✓

**Hard blockers from the receipt remain intact and enumerated:**
- Clean participant packet hash: not computed
- Source-byte hashes: missing for CW-P1 through CW-P6; CW-P7 excluded
- Retrieval timestamps: not normalized
- Evidence registry freeze: not performed
- Facilitator ledger freeze: not performed
- Frozen band inputs: not frozen
- Second-label audit: not performed
- BlindJudgement schema instance: not created
- Blind judgment cleanliness: user-supplied, not independently verified
- Memorization probe: not run for any model family
- Walmart-specific outcome gaps: remain not established
- Mapping and scoring: not run

**No unrelated source expansion.** The blast-radius scan did not open the evidence registry, facilitator ledger, blind judgment adapter note, or unrelated Judgment Spine harness files. Those remain available-not-read for this bounded recheck. ✓

---

## 8. Recommendation

**accept**

Rationale: All three hygiene findings are closed. The hygiene patch introduced no blocker or major regression in the touched patch scope or directly dependent hash/status surfaces. The one-cycle hash loop between the adapter/reconciliation-decision and the receipt is coherent, documented on both sides, and correctly labeled as a non-final-state-lock. No-readiness, no-validation, and no-blind-use-readiness boundaries are preserved throughout. A new reviewer can verify the current source state, see accepted decision/recheck/hash-linkage status consistently across the receipt, reconciliation decision, source-manifest adapter, and participant packet, and return this bounded hygiene verdict without reopening scoring, schema implementation, blind use, validation, or case judgment.

This `accept` recommendation applies to the HF-01/HF-02/HF-03 closure check only. It does not mean blind-use readiness, scoring readiness, schema implementation readiness, ledger-freeze readiness, validation, product proof, or judgment quality.

---

## 9. Next Authorized Action

Owner may record this recheck as the accepted whole-fixture hygiene post-patch recheck in the fixture authoring receipt and close the hygiene acceptance gate. The receipt should be updated to reflect:
- `whole_fixture_hygiene_post_patch_recheck_report` path and hash for this report.
- `whole_fixture_hygiene_acceptance_status: accepted_for_next_fixture_step_pending_commit`.
- `post_patch_status` revised from "pending_post_patch_recheck" to the accepted state.

After that receipt update, the next authorized fixture-authoring step is owner-directed selection of which remaining hard blocker to address next (e.g., source-byte hash computation, retrieval timestamp normalization, memorization probe commissioning). Do not route to blind use, probe execution, model runs, scoring, schema implementation, ledger freeze, validation, proof-run, product proof, or judgment-quality claims.

---

## 10. Required Closeout Boundary

These review findings are decision input only. They are not approval, validation, mandatory remediation, readiness, or executor-ready patch authority until separately accepted or authorized.

Required closeout boundary: **plumbing works only; not judgment quality.**

---

## Source-Read Ledger

| Source | Why read | Status |
| --- | --- | --- |
| `AGENTS.md` | Workspace and overlay authority. | Supplied in current task. |
| `.agents/workflow-overlay/README.md` | Overlay entrypoint and binding rule. | Read. |
| `.agents/workflow-overlay/source-loading.md` | Source budget, start-preflight rules. | Read; modified in workspace (source-ledger caveat). |
| `.agents/workflow-overlay/prompt-orchestration.md` | Source-gated method contract, output-mode rules. | Read; modified in workspace (source-ledger caveat). |
| `.agents/workflow-overlay/review-lanes.md` | Review lane authority and restrictions. | Read; modified in workspace (source-ledger caveat). |
| `.agents/workflow-overlay/communication-style.md` | Review summary shape and courier YAML. | Read; modified in workspace (source-ledger caveat). |
| `fixture_authoring_receipt_v0.md` | Primary patched source; receipt linkage, hash relationships, next authorized step. | Read; untracked; hash matched. |
| `protocol_pydantic_reconciliation_decision_v0.md` | HF-01 closure target; status, hash pins, no-readiness boundaries. | Read; untracked; hash matched. |
| `source_manifest_participant_safe_adapter_decision_v0.md` | HF-02 closure target; input_hashes, hash_loop_boundary, accepted recheck pin. | Read; untracked; hash matched. |
| `participant_packet_draft_v0.md` | HF-03 closure target; blocker list, participant-facing content. | Read; untracked; hash matched. |
| `canoo_walmart_v0_14_fixture_hygiene_adversarial_review_v0.md` | Prior hygiene review; HF-01/HF-02/HF-03 original findings and closure criteria. | Read; hash matched. |
| `canoo_walmart_v0_14_draft_fixture_pack_post_patch_adversarial_recheck_v0.md` | Accepted DFP post-patch recheck; DFP closure provenance. | Hash matched; not re-read in full (prior accepted state). |
| `canoo_walmart_source_manifest_adapter_decision_post_patch_adversarial_recheck_v0.md` | Accepted source-manifest recheck; SM-01 through SM-06 closure provenance. | Hash matched; not re-read in full (prior accepted state). |
| `canoo_walmart_protocol_pydantic_reconciliation_decision_post_patch_adversarial_recheck_v0.md` | Accepted reconciliation decision recheck; RD-01 through RD-03 closure provenance. | Hash matched; not re-read in full (prior accepted state). |

Sources available not read for this bounded recheck:
- `evidence_registry_draft_v0.md` — not in HF-01/HF-02/HF-03 closure scope; not touched by hygiene patch.
- `facilitator_ledger_draft_v0.md` — same.
- `blind_judgement_adapter_note_v0.md` — same.
- All v0.14 schema/protocol reference files — not touched by hygiene patch.
- All case folder sources — not touched by hygiene patch.
