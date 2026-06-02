# Canoo/Walmart Protocol/Pydantic Reconciliation Decision Adversarial Review v0

```yaml
retrieval_header_version: 1
artifact_role: Adversarial artifact review report
scope: Read-only adversarial review of protocol_pydantic_reconciliation_decision_v0.md and its receipt linkage.
use_when:
  - Deciding whether the reconciliation decision is safe as a docs-only basis for the next fixture step.
  - Checking findings before any schema implementation, ledger freeze, blind use, scoring, probe execution, or validation claim.
authority_boundary: retrieval_only
```

---

## 1. Commission

Run a read-only adversarial artifact review of the Canoo/Walmart v0.14 Protocol/Pydantic reconciliation decision before any schema implementation, ledger freeze, blind use, scoring, probe execution, validation, or judgment-quality claim.

Review whether `protocol_pydantic_reconciliation_decision_v0.md`, plus its minimal receipt linkage in `fixture_authoring_receipt_v0.md`, is safe and coherent as a docs-only decision basis for the next fixture step.

This review is read-only. No source artifacts were edited. The report is the only authorized write output.

---

## 2. Target

Primary review targets:

- `docs/research/judgment-spine/harness/v0_14/fixtures/canoo_walmart_2022_v0_14/protocol_pydantic_reconciliation_decision_v0.md`
- `docs/research/judgment-spine/harness/v0_14/fixtures/canoo_walmart_2022_v0_14/fixture_authoring_receipt_v0.md` (receipt linkage only)

Supporting fixture files:

- `docs/research/judgment-spine/harness/v0_14/fixtures/canoo_walmart_2022_v0_14/participant_packet_draft_v0.md`
- `docs/research/judgment-spine/harness/v0_14/fixtures/canoo_walmart_2022_v0_14/source_manifest_participant_safe_adapter_decision_v0.md`
- `docs/research/judgment-spine/harness/v0_14/fixtures/canoo_walmart_2022_v0_14/facilitator_ledger_draft_v0.md`
- `docs/research/judgment-spine/harness/v0_14/fixtures/canoo_walmart_2022_v0_14/evidence_registry_draft_v0.md`

v0.14 controlling references:

- `docs/research/judgment-spine/harness/v0_14/pydantic_schema_reference.md`
- `docs/research/judgment-spine/harness/v0_14/judgement_case_construction_protocol.md`
- `docs/research/judgment-spine/harness/v0_14/blind_judgement_schema_and_harness_protocol.md`

Prior review context (available but not opened for this review; not needed for direct contradiction checks):

- `docs/review-outputs/adversarial-artifact-reviews/canoo_walmart_source_manifest_adapter_decision_post_patch_adversarial_recheck_v0.md`

---

## 3. Authority and Source Context

```yaml
orca_start_preflight:
  agents_read: yes
  overlay_read: yes
  source_pack: custom S0 plus Canoo/Walmart reconciliation targets and v0.14 schema/protocol references
  edit_permission: read-only-review-plus-report-write
  target_scope: Adversarial review of protocol_pydantic_reconciliation_decision_v0.md and receipt linkage only.
  dirty_state_checked: yes
  blocked_if_missing: yes
source_context_status: SOURCE_CONTEXT_READY
```

```yaml
workspace_state:
  branch: main
  head: a2aebdd8e04c627c5102e79eb324b24b3de35226
  expected_head: a2aebdd
  head_match: yes
  report_path_collision: none
  dirty_or_untracked_fixture_files: yes
  dirty_state_allowance: allowed_for_named_canoo_walmart_fixtures_and_report_path_only
```

```yaml
methods_applied:
  workflow_deep_thinking: applied_for_failure_mode_framing
  workflow_adversarial_artifact_review: applied_for_findings_and_recommendation
  source_gated_sequence: satisfied
```

Overlay files read: `AGENTS.md`, `.agents/workflow-overlay/README.md`, `.agents/workflow-overlay/source-of-truth.md`, `.agents/workflow-overlay/source-loading.md`, `.agents/workflow-overlay/prompt-orchestration.md`, `.agents/workflow-overlay/review-lanes.md`, `.agents/workflow-overlay/communication-style.md`.

---

## 4. Hash Verification Table

All hashes computed fresh from on-disk bytes using `certutil -hashfile ... SHA256`.

| File | Expected SHA256 | Computed SHA256 | Match |
| --- | --- | --- | --- |
| `protocol_pydantic_reconciliation_decision_v0.md` | `95082704A850ECBAB28461BC9E2150DC99E7B0EBB9B36B7DE0CFD485C2A3C4FA` | `95082704a850ecbab28461bc9e2150dc99e7b0ebb9b36b7de0cfd485c2a3c4fa` | YES |
| `fixture_authoring_receipt_v0.md` | `BD08CF4583EC8D6A874AA2A1EAE2D9BA0B9FC990A116DC3B4DE338EB0A14F1E6` | `bd08cf4583ec8d6a874aa2a1eae2d9ba0b9fc990a116dc3b4de338eb0a14f1e6` | YES |
| `participant_packet_draft_v0.md` | `3F9D10A743E10C5A464D5AD16866D700E9EFD5838FFC82BD5FE2B5905F174C61` | `3f9d10a743e10c5a464d5ad16866d700e9efd5838ffc82bd5fe2b5905f174c61` | YES |
| `source_manifest_participant_safe_adapter_decision_v0.md` | `B427AB9AC769838E990BC31B04CB2DE4E09CE226345D60AB06753DEDEB677D61` | `b427ab9ac769838e990bc31b04cb2de4e09ce226345d60ab06753dedeb677d61` | YES |
| `facilitator_ledger_draft_v0.md` | `B10C4B7A282CDB72D9320AB7E55FB9ECE7751CC10124A4415856115BE1D6AAC6` | `b10c4b7a282cdb72d9320ab7e55fb9ece7751cc10124a4415856115be1d6aac6` | YES |
| `evidence_registry_draft_v0.md` | `5F8BB241981D7FDB79F78E18BE07E7E52E68B447C51CFDAC688E234B09FC4078` | `5f8bb241981d7fdb79f78e18be07e7e52e68b447c51cfdac688e234b09fc4078` | YES |
| `pydantic_schema_reference.md` | `CFFC7BCAC179B752B9A77204ECA6A6399D30DD7CB6B2C52533E3EC0FDC031D8D` | `cffc7bcac179b752b9a77204eca6a6399d30dd7cb6b2c52533e3ec0fdc031d8d` | YES |
| `judgement_case_construction_protocol.md` | `FDEA14A1767D135A8DD56AF073AF0E5E3206B945FB9E603F597491D795889C71` | `fdea14a1767d135a8dd56af073af0e5e3206b945fb9e603f597491d795889c71` | YES |
| `blind_judgement_schema_and_harness_protocol.md` | `ED80A0C0D7EC2252E5FC07EC175CFAD3FEE5F3D1F4527812A7813E2C5EE85EE4` | `ed80a0c0d7ec2252e5fc07ec175cfad3fee5f3d1f4527812a7813e2c5ee85ee4` | YES |

All nine required hashes verified. No mismatch between on-disk state and commission-provided expected hashes.

---

## 5. Review Criteria Applied

Maximally adversarial within the commission-bound scope. Checked for:

1. False schema compatibility claims.
2. Hidden schema extension or implementation authorization.
3. Treating protocol metadata as current Pydantic fields.
4. Confusing `BlindJudgement.decision_shape` with current `FacilitatorLedger` storage.
5. Adding or implying `evidence_unit_ids` support inside current `MustAddressItem`.
6. Weak or missing traceability for must-address evidence references.
7. Participant-facing leakage from facilitator-only reconciliation metadata.
8. Receipt linkage that overstates acceptance, readiness, scoring status, or validation.
9. Any contradiction with the accepted source-manifest adapter boundary.
10. Any language converting a draft docs-only decision into ledger freeze, blind-use readiness, scoring readiness, validation, or judgment-quality evidence.

---

## 6. Failure Mode Framing (workflow-deep-thinking applied)

Before listing findings, four failure modes were framed:

**FM-1: Hash-loop integrity gap.** The reconciliation decision was authored before the fixture_authoring_receipt was updated to add the reconciliation linkage section. This creates a predictable one-way hash staleness: the decision pins the pre-linkage receipt hash, but the commission-verified receipt hash reflects the post-linkage state. Without a hash-loop boundary statement, a future integrity checker sees an unexplained mismatch and cannot distinguish authoring-sequence staleness from tampering.

**FM-2: Scope gap on a secondary protocol/Pydantic mismatch.** The v0.14 case-construction protocol lists `evidence_unit_ids` under `underreach_observability` as well as under `must_address_items`. The Pydantic `UnderreachObservability` object has no such field. The reconciliation decision correctly addresses `case_family`, `decision_shape`, and `MustAddressItem.evidence_unit_ids`, but does not address the `underreach_observability.evidence_unit_ids` protocol-to-Pydantic gap. A future ledger author following the protocol template could attempt to use the field.

**FM-3: decision_shape directionality ambiguity.** The reconciliation decision states `decision_shape` "may later populate BlindJudgement.decision_shape." This implies the facilitator metadata would flow into the contestant's output field. The actual relationship may be that the facilitator sets a case-characteristic value used for validation/comparison after the contestant independently selects their `decision_shape` in the blind judgment. The imprecise verb "populate" is directionally ambiguous.

**FM-4: Readiness escalation via receipt pointer.** The receipt linkage in `fixture_authoring_receipt_v0.md` says the reconciliation decision is "pending review; not readiness, validation, or scoring evidence." This is correctly scoped. The risk is that a future agent reads the receipt-to-decision pointer plus the receipt's "adapter_decision_status: accepted" (for the SM adapter, not the reconciliation decision) and conflates acceptance of the SM adapter with acceptance of the reconciliation decision. These are separate status entries with different scopes.

---

## 7. Findings

### RD-01 — Stale input hash for `fixture_authoring_receipt_v0.md` in the reconciliation decision

**Severity:** major

**Evidence:**

In `protocol_pydantic_reconciliation_decision_v0.md`, the `input_hashes` section (line 13) pins:
```
fixture_authoring_receipt_v0.md: DB80D5576553CFFEBEE86B987287AE8EC0A6CDB17FB6BAACEA7A5E4A970DD2B2
```

The commission-verified current SHA256 of `fixture_authoring_receipt_v0.md` is:
```
BD08CF4583EC8D6A874AA2A1EAE2D9BA0B9FC990A116DC3B4DE338EB0A14F1E6
```

These do not match. The reconciliation decision was authored when the receipt lacked the "Protocol/Pydantic Reconciliation Decision Linkage" section (lines 251–256 of the current receipt). After the reconciliation decision was authored, the receipt was updated to add that linkage pointer, changing the receipt's hash from `DB80D5576553...` to `BD08CF4583...`.

The reconciliation decision does not include a hash-loop boundary statement acknowledging the expected discrepancy. Compare: the receipt itself includes a `hash_loop_boundary` note (under the Acceptance Housekeeping Receipt) handling the SM-04 mutual-reference situation for the adapter/receipt loop. No equivalent acknowledgment exists for the reconciliation-decision/receipt loop.

**Why it matters:**

A future agent or reviewer performing integrity validation against the pinned input hashes will find a hard mismatch at the most prominent supporting artifact. Without documentation explaining why the mismatch is expected (authoring-sequence timing, not tampering), the mismatch cannot be distinguished from an integrity failure. This blocks clean hash-chain verification for the entire reconciliation decision.

**Minimum closure condition:**

The reconciliation decision must either:
(a) Refresh its input hash for `fixture_authoring_receipt_v0.md` from `DB80D5576553...` to `BD08CF4583...` and note in the `stale_if` or a hash-loop acknowledgment block that the receipt was subsequently updated to add the reconciliation linkage, with the review-verified hash recorded; or
(b) Add a hash-loop boundary statement similar to the receipt's `hash_loop_boundary` note, explicitly stating that the pinned hash `DB80D5576553...` reflects the pre-linkage receipt state and is expected to be stale after the receipt was updated.

Either approach must make the mismatch self-documenting so integrity checks can pass without requiring knowledge of authoring sequence.

**Next authorized action:** Owner decision on (a) vs (b); then a patch to the reconciliation decision. This review authorizes no edits to source artifacts.

---

### RD-02 — `underreach_observability.evidence_unit_ids` protocol/Pydantic mismatch not addressed

**Severity:** minor

**Evidence:**

The v0.14 case-construction protocol (`judgement_case_construction_protocol.md`, under "Facilitator Ledger Required Fields") lists:
```yaml
underreach_observability:
  present: true | false
  basis:
    - opportunity_cost
    - window_closure
    - information_decay
    - option_value_loss
    - other
  evidence_unit_ids:
```

The current Pydantic `UnderreachObservability` model (`pydantic_schema_reference.md`, lines 114–118) has:
```python
class UnderreachObservability(BaseModel):
    present: bool
    basis: Optional[Literal["opportunity_cost", "window_closure", "information_decay", "other"]] = None
    notes: Optional[str] = None
```

`evidence_unit_ids` is absent from the Pydantic model. This is the same class of protocol/Pydantic mismatch the reconciliation decision was commissioned to resolve, but for `underreach_observability.evidence_unit_ids` rather than `MustAddressItem.evidence_unit_ids`.

The reconciliation decision's stated scope is "resolve current placement for `case_family`, `decision_shape`, and must-address evidence-unit references." It does not claim to address `underreach_observability.evidence_unit_ids`. The facilitator_ledger_draft handles this implicitly by placing evidence references in the `notes` prose field rather than a structured field. The facilitator_ledger_draft's "Protocol/Pydantic Reconciliation Blocker" section also does not flag this mismatch.

The risk is that a future ledger author following the protocol template verbatim attempts to populate `evidence_unit_ids` under `underreach_observability` in the Pydantic object, encountering a schema error or silently treating it as unsupported.

**Why it matters:**

The facilitator_ledger_draft's implicit handling (prose notes only) is pragmatically correct, but the reconciliation decision does not provide explicit coverage. Without explicit coverage, the scope gap is not documented as an intentional boundary, and the implicit workaround could be lost in a subsequent authoring pass.

**Minimum closure condition:**

The reconciliation decision must either:
(a) Expand its scope to explicitly address `underreach_observability.evidence_unit_ids` using the same pattern as `MustAddressItem.evidence_unit_ids` (protocol traceability metadata, not a current Pydantic field); or
(b) Add an explicit out-of-scope statement noting that `underreach_observability.evidence_unit_ids` is similarly not in the current Pydantic `UnderreachObservability`, that the draft ledger handles it via prose notes, and that a future reconciliation step would be required before any schema implementation targets `underreach_observability.evidence_unit_ids`.

**Next authorized action:** Advisory direction to owner; does not block the next fixture step on its own.

---

### RD-03 — `decision_shape` flow directionality is ambiguous

**Severity:** minor

**Evidence:**

The reconciliation decision states (field placement contract table, row for `decision_shape`):

> "Protocol fixture metadata now; later blind input only after explicit freeze and authorized adaptation or rerun"

And in the Decision section (line 78):

> "`decision_shape` remains facilitator/protocol fixture metadata until it is explicitly frozen for the case. It may later populate `BlindJudgement.decision_shape`, but that future use is separate from current `FacilitatorLedger` shape and is not implemented here."

The verb "populate" implies the facilitator-held `decision_shape` value would be written into the contestant's `BlindJudgement.decision_shape` field — i.e., facilitator → contestant. However, the v0.14 protocol structure is that contestants produce `decision_shape` as part of their blind judgment output, and the facilitator's case-level `decision_shape` characterizes the expected case type for facilitator reference and later scoring/comparison. The direction is more likely: facilitator sets case-characteristic value; contestant independently produces their own value; scorer compares.

The reconciliation decision correctly defers the "blind adaptation" question ("that future use is separate from current FacilitatorLedger shape and is not implemented here"), so no false claim is made. The ambiguity does not affect the current docs-only decision. But "may later populate" could mislead a future adapter author into implementing a wrong one-way injection.

**Why it matters:**

If a future agent implementing the blind adapter interprets "populate" as "the harness fills in the contestant's `decision_shape` from the facilitator ledger," it would produce a non-blind run where the contestant's output is partially prefilled. This would be a harness integrity failure, not a docs failure.

**Minimum closure condition:**

The reconciliation decision should clarify the intended use of facilitator `decision_shape` relative to `BlindJudgement.decision_shape`: whether it is a case-type characterization used for post-run validation/comparison (not injection into the blind output), or whether it is intended to be provided to the contestant as part of the prompt (which would need its own participant-safety review). The clarification should be added before any blind adapter implementation is authorized.

**Next authorized action:** Advisory direction to owner; does not block the next fixture step on its own.

---

## 8. Non-Findings and Confirmed Boundaries

The following criteria were checked and found clean:

**No false schema compatibility claims.** The reconciliation decision accurately characterizes the current Pydantic schema:
- `FacilitatorLedger` does not expose `case_family` or `decision_shape` — confirmed against `pydantic_schema_reference.md` lines 119–133.
- `MustAddressItem` supports only `must_address_item_id` and `description` — confirmed against `pydantic_schema_reference.md` lines 110–112.
- `BlindJudgement` exposes `decision_shape: str` as a contestant output field — confirmed against `pydantic_schema_reference.md` lines 191–210.

**No hidden schema extension or implementation authorization.** The decision explicitly rejects schema extension ("Not authorized in this lane"), explicitly defers the adapter-layer option ("Deferred until after review and explicit authorization"), and states "No artifact in this lane should add an `evidence_unit_ids` field to the current `MustAddressItem` schema block."

**Protocol metadata correctly separated from current Pydantic fields.** `case_family`, `decision_shape`, and must-address evidence-unit references are each explicitly placed as "facilitator/protocol fixture metadata" or "separate protocol traceability mapping" — not as current Pydantic fields.

**`BlindJudgement.decision_shape` not confused with `FacilitatorLedger` storage.** The decision correctly identifies that `decision_shape` is absent from `FacilitatorLedger` and present only in `BlindJudgement` as a contestant output field. The ambiguity flagged in RD-03 is about directionality of future use, not about current placement. No current confusion exists.

**`evidence_unit_ids` not implied as a current `MustAddressItem` field.** The decision explicitly prohibits adding the field and explicitly treats the facilitator_ledger_draft's candidate table as protocol-level traceability only, not as proof of Pydantic support.

**Traceability for must-address evidence references is adequate for a docs-only decision.** The MA-CW-01 through MA-CW-05 candidate table in `facilitator_ledger_draft_v0.md` provides the named CW-E* references. The reconciliation decision's handling of this table as "protocol-level traceability metadata" correctly preserves the references without asserting Pydantic field support.

**No participant-facing leakage from facilitator-only reconciliation metadata.** The decision explicitly blocks participant-packet exposure of `case_family` and `decision_shape`. The impact table correctly marks `participant_packet_draft_v0.md` as requiring no edits. The participant packet's content (verified at its commission-checked hash) contains no facilitator metadata from this decision.

**Receipt linkage does not overstate acceptance, readiness, or scoring status.** The fixture_authoring_receipt's "Protocol/Pydantic Reconciliation Decision Linkage" section (lines 251–255 of the current receipt) characterizes the reconciliation decision as "created as a draft docs-only reconciliation decision; pending review; not readiness, validation, or scoring evidence." This is accurate.

**No contradiction with the accepted source-manifest adapter boundary.** The source-manifest adapter was accepted at `accepted_for_next_fixture_step_not_blind_use_ready` with SM-01 through SM-06 closed. The reconciliation decision's scope (protocol/Pydantic field placement for `case_family`, `decision_shape`, and must-address evidence references) does not intersect with or contradict the SM adapter's scope (participant visibility, source ID linking, and pre-seal placeholder handling). No contradiction found.

**No language converting draft decision into ledger freeze, blind-use readiness, or scoring readiness.** The decision explicitly states: "No schema implementation, ledger freeze, blind adaptation, scoring, or validation claim may proceed from this decision alone. Review and explicit acceptance are still required." The "Remaining blockers" section enumerates 8 explicit open blockers. The "Next authorized step" directs to review before any implementation or scoring action. All anti-escalation language is present and consistent.

---

## 9. Recommendation

```yaml
recommendation: patch_before_acceptance
blocking_findings:
  - id: RD-01
    severity: major
    title: "Stale input hash for fixture_authoring_receipt_v0.md — no hash-loop boundary statement"
advisory_findings:
  - id: RD-02
    severity: minor
    title: "underreach_observability.evidence_unit_ids protocol/Pydantic mismatch not addressed in scope"
  - id: RD-03
    severity: minor
    title: "decision_shape flow directionality ambiguous — 'may later populate' imprecise"
```

**Rationale:** The reconciliation decision is substantively sound. The protocol/Pydantic placement decisions for `case_family`, `decision_shape`, and `MustAddressItem.evidence_unit_ids` are correctly analyzed, correctly scoped as docs-only, and correctly blocked behind review and explicit acceptance. No false claims, no hidden implementation, no leakage, no readiness overstatement.

RD-01 is the single blocking finding. It is a traceability integrity issue, not a substantive content error. The stale hash is the predictable artifact of a mutual-reference loop between the reconciliation decision and the receipt. Because the receipt successfully handles an analogous loop (the SM-04 hash-loop boundary for the adapter/receipt mutual reference), the pattern for resolution is established. The fix is narrow: a hash-loop acknowledgment or hash refresh. The decision's substantive content does not change.

RD-02 and RD-03 are advisory. RD-02 should be addressed before a second reconciliation decision is needed to cover the same class of gap. RD-03 should be addressed before any blind adapter implementation is authorized.

---

## 10. Next Authorized Action

Patch the reconciliation decision to address RD-01 (hash-loop boundary statement or hash refresh with explanation). Advisory: also address RD-02 and RD-03 in the same patch to keep the reconciliation decision internally complete before it is accepted as a fixture step decision basis.

After the patch:
1. Run a post-patch recheck (equivalent to the SM adapter post-patch recheck pattern) to confirm RD-01 is closed.
2. Owner accepts the patched reconciliation decision.
3. Proceed to the next fixture step (not ledger freeze, not blind use, not scoring — only the next authorized fixture-authoring step as defined by the receipt's "Next Authorized Step" section).

Required boundary: plumbing works only; not judgment quality.

---

## 11. Source-Read Ledger

| Source | Why read | Sections targeted | Status |
| --- | --- | --- | --- |
| `AGENTS.md` | Workspace and overlay authority | Full (short file) | clean/tracked |
| `.agents/workflow-overlay/README.md` | Overlay entrypoint and binding rule | Full | modified/tracked |
| `.agents/workflow-overlay/source-of-truth.md` | Source hierarchy and conflict rules | Full | modified/tracked |
| `.agents/workflow-overlay/source-loading.md` | Source pack selection and budgets | Full | modified/tracked |
| `.agents/workflow-overlay/prompt-orchestration.md` | Review output mode and method sequence rules | Full | modified/tracked |
| `.agents/workflow-overlay/review-lanes.md` | Review lane authority and doctrine | Full | modified/tracked |
| `.agents/workflow-overlay/communication-style.md` | Courier YAML shape and review closeout | Full | modified/tracked |
| `protocol_pydantic_reconciliation_decision_v0.md` | Primary review target | Full | untracked |
| `fixture_authoring_receipt_v0.md` | Receipt linkage review | Full | untracked |
| `pydantic_schema_reference.md` | v0.14 controlling reference — Pydantic schema surface | Full | untracked |
| `judgement_case_construction_protocol.md` | v0.14 controlling reference — protocol field requirements | Full | untracked |
| `blind_judgement_schema_and_harness_protocol.md` | v0.14 controlling reference — BlindJudgement field structure | Full | untracked |
| `facilitator_ledger_draft_v0.md` | Supporting fixture — protocol metadata and candidate must-address table | Full | untracked |
| `participant_packet_draft_v0.md` | Supporting fixture — participant-facing surface check | Frontmatter only | untracked |
| `source_manifest_participant_safe_adapter_decision_v0.md` | Supporting fixture — SM adapter boundary | Header and decision summary | untracked |
| Prior SM post-patch recheck report | Prior review context | Not opened — no contradiction found requiring it | not read |

---

```yaml
review_non_claims:
  - "not validation"
  - "not readiness"
  - "not approval"
  - "not mandatory remediation"
  - "not executor-ready patch authority"
  - "not blind-use authorization"
  - "not scoring authorization"
  - "not judgment quality"
```

Required closeout boundary: plumbing works only; not judgment quality.
