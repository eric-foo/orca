# Canoo/Walmart v0.14 Protocol/Pydantic Reconciliation Decision v0

```yaml
retrieval_header_version: 1
artifact_role: Research artifact
scope: Accepted docs-only decision for reconciling Canoo/Walmart v0.14 protocol field requirements against current Pydantic surfaces.
use_when:
  - Deciding where Canoo/Walmart v0.14 fixture metadata belongs before any schema implementation or ledger freeze.
  - Checking how `case_family`, `decision_shape`, must-address evidence references, and underreach-observability evidence references should be handled in the current draft fixture.
  - Checking the accepted docs-only field-placement basis before any blind run, scoring, or validation claim.
authority_boundary: retrieval_only
input_hashes:
  fixture_authoring_receipt_v0.md: E2AFBEB0D8A9740015BE408D34D19F2A922E5887A9D34D807E63845CCF0B841A
  source_manifest_participant_safe_adapter_decision_v0.md: 39E92DB6C9D86C1BB18857069CF0507065C4460A15B3293359611875B3DB2E32
  participant_packet_draft_v0.md: 059EE78287C0F667DD75568F3179EE8424D2FFCD42CCC2882C177F5A7C9C2FD6
  evidence_registry_draft_v0.md: 47BBA3BE55627FDE39B347A24E20779005B633B2143ACEE51625AE21460B47B1
  source_acquisition_receipt_v0.md: 621EA29B85C3D98936326E47012149582BF28F7B891EE3A810844D0B1CC5264C
  facilitator_ledger_draft_v0.md: B10C4B7A282CDB72D9320AB7E55FB9ECE7751CC10124A4415856115BE1D6AAC6
  pydantic_schema_reference.md: CFFC7BCAC179B752B9A77204ECA6A6399D30DD7CB6B2C52533E3EC0FDC031D8D
  judgement_case_construction_protocol.md: FDEA14A1767D135A8DD56AF073AF0E5E3206B945FB9E603F597491D795889C71
  blind_judgement_schema_and_harness_protocol.md: ED80A0C0D7EC2252E5FC07EC175CFAD3FEE5F3D1F4527812A7813E2C5EE85EE4
  protocol_pydantic_reconciliation_decision_adversarial_review_v0.md: 54AFA84BA368F05CF9D2E1358D5CCD6F21B9FAF3F747847B0205C825ABCEBB4F
  protocol_pydantic_reconciliation_decision_post_patch_adversarial_recheck_v0.md: 6C884828AFCC75BB8B6D286A36D544E522C39EF3A2C2B3760B71E19AB3EF6CF2
hash_loop_boundary:
  fixture_authoring_receipt_v0.md_pre_linkage_authoring_hash: DB80D5576553CFFEBEE86B987287AE8EC0A6CDB17FB6BAACEA7A5E4A970DD2B2
  fixture_authoring_receipt_v0.md_post_reconciliation_acceptance_hash: 32C99D992411CB88F536E4C9E6C706007454F731272F774397DAA95CC4B4F1E9
  fixture_authoring_receipt_v0.md_pre_source_acquisition_hash: E2AFBEB0D8A9740015BE408D34D19F2A922E5887A9D34D807E63845CCF0B841A
  rule: >
    The input_hashes entry pins the receipt state available before this
    source-acquisition status refresh. Earlier receipt hashes are retained only
    to document the one-cycle authoring sequence. The receipt may separately
    pin this artifact's post-refresh hash after this update; do not treat these
    hashes as a mutual final-state hash lock.
branch_or_commit: main@a2aebdd
open_next:
  - docs/research/judgment-spine/harness/v0_14/judgement_case_construction_protocol.md
  - docs/research/judgment-spine/harness/v0_14/pydantic_schema_reference.md
  - docs/research/judgment-spine/harness/v0_14/blind_judgement_schema_and_harness_protocol.md
  - docs/review-outputs/adversarial-artifact-reviews/
stale_if:
  - Any pinned input hash changes.
  - The v0.14 protocol or Pydantic reference changes field placement for `case_family`, `decision_shape`, `MustAddressItem`, or `UnderreachObservability`.
  - A later accepted review rejects or materially revises this decision.
```

## Status and scope

```yaml
orca_start_preflight:
  agents_read: yes
  overlay_read: yes
  source_pack: custom S0 plus Canoo/Walmart fixture files and v0.14 schema/protocol files
  edit_permission: docs-write
  target_scope: Author a docs-only protocol/Pydantic reconciliation decision for Canoo/Walmart v0.14 fixture fields.
  dirty_state_checked: yes
  blocked_if_missing: yes
source_context_status: SOURCE_CONTEXT_READY
```

- Status: accepted docs-only field-placement decision basis for next fixture step.
- Decision-basis status: accepted after post-patch adversarial recheck and owner-directed receipt housekeeping; not schema implementation ready, not ledger-freeze ready, not blind-use ready, and not score-ready.
- Scope: resolve current placement for `case_family`, `decision_shape`, must-address evidence-unit references, and underreach-observability evidence-unit references in the Canoo/Walmart v0.14 draft fixture.
- Non-claims: no schema implementation, no ledger freeze, no scoring readiness, no blind-use readiness, no validation, and no judgment-quality claim.

## Problem statement

The v0.14 case-construction protocol currently places `case_family`, `decision_shape`, `must_address_items[].evidence_unit_ids`, and `underreach_observability.evidence_unit_ids` inside the facilitator-side protocol shape. The current Pydantic reference does not mirror that placement:

- `FacilitatorLedger` does not expose `case_family` or `decision_shape`.
- `MustAddressItem` supports only `must_address_item_id` and `description`.
- `UnderreachObservability` supports `present`, optional `basis`, and optional `notes`; it does not expose `evidence_unit_ids`.
- `BlindJudgement` does expose `decision_shape`, but only as run-time blind-judgement input, not as current facilitator-ledger storage.

That mismatch blocks any honest attempt to claim schema implementation, ledger freeze, scoring readiness, or harness-executable blind adaptation for this fixture.

## Options compared

| Option | Advantages | Failure modes | Result |
| --- | --- | --- | --- |
| Keep fields as protocol-only fixture metadata outside direct Pydantic objects. | Smallest docs-only move. Preserves current v0.14 Pydantic surfaces. Avoids fake schema compliance. | Leaves a two-surface contract that later review or implementation must honor. | Chosen, with separate traceability mapping for must-address evidence references. |
| Extend or patch Pydantic schema now. | Aligns protocol and schema directly. | Not authorized in this lane. Would create implementation and doctrine movement, not a docs-only decision. | Rejected for this turn. |
| Build a case-local adapter layer that maps protocol metadata into current Pydantic objects. | Could preserve traceability and run compatibility later. | Implementation-shaped. Easy to overclaim a working adapter without accepted field contract. | Deferred until after review and explicit authorization. |
| Defer reconciliation and keep the fixture blocked. | Avoids premature placement choice. | Leaves the known blocker unresolved and does not unblock the next decision basis. | Rejected. |

Decisive criteria were: smallest complete docs-only intervention, no false schema compliance, preserved evidence traceability, and no hidden readiness claim.

## Decision

Use the smallest complete hybrid that preserves the current v0.14 Pydantic schema:

1. `case_family` remains facilitator/protocol fixture metadata for this draft. It is not inserted into the current `FacilitatorLedger` schema block.
2. `decision_shape` remains facilitator/protocol fixture metadata until it is explicitly frozen as a case-level characterization. It must not be injected into contestant `BlindJudgement.decision_shape`; any later blind adapter must either let the contestant supply that field independently or separately authorize participant-visible prompt exposure after participant-safety review.
3. `must_address_items` remain Pydantic-compatible direct items containing only `must_address_item_id` and `description`.
4. Must-address evidence-unit references remain case-local protocol traceability metadata in a separate mapping, not in the current `MustAddressItem` object.
5. Underreach-observability evidence-unit references remain case-local protocol traceability metadata or prose rationale, not in the current `UnderreachObservability` object.
6. No schema implementation, ledger freeze, blind adaptation, scoring, or validation claim may proceed from this decision alone. Separate authorization is still required for any runtime, schema, freeze, blind-use, probe, scoring, or validation work.

## Field placement contract

| Field | Current source of requirement | Current Pydantic support | Chosen placement | Participant visibility | Facilitator visibility | Blocks before |
| --- | --- | --- | --- | --- | --- | --- |
| `case_family` | `judgement_case_construction_protocol.md` facilitator ledger shape | None in current `FacilitatorLedger` | Protocol fixture metadata only | No participant-packet exposure required | Yes | Schema implementation, ledger freeze |
| `decision_shape` | `judgement_case_construction_protocol.md` facilitator ledger shape and `blind_judgement_schema_and_harness_protocol.md` blind input | Present in `BlindJudgement`; absent from `FacilitatorLedger` | Protocol fixture metadata now; later case-level comparison reference only after explicit freeze; not prefilled into blind output | No participant-packet exposure required | Yes | Blind adaptation, ledger freeze, scoring |
| `must_address_items[].must_address_item_id` | Protocol and current fixture draft | Present in `MustAddressItem` | Direct Pydantic field | No participant-packet exposure | Yes | Finalization before freeze |
| `must_address_items[].description` | Protocol and current fixture draft | Present in `MustAddressItem` | Direct Pydantic field | No participant-packet exposure | Yes | Finalization before freeze |
| `must_address_items` evidence-unit references (`MA-CW-*` -> `CW-E*`) | `judgement_case_construction_protocol.md` and facilitator ledger candidate table | Not present in current `MustAddressItem` | Separate protocol traceability mapping, outside current Pydantic object | No participant-packet exposure | Yes | Schema implementation, ledger freeze, scoring traceability sign-off |
| `underreach_observability.evidence_unit_ids` | `judgement_case_construction_protocol.md` underreach-observability shape and facilitator ledger rationale | Not present in current `UnderreachObservability` | Separate protocol traceability metadata or prose note, outside current Pydantic object | No participant-packet exposure | Yes | Schema implementation, ledger freeze, scoring traceability sign-off |

## Must-address evidence-unit reference handling

For this draft fixture:

- The canonical current `MustAddressItem` payload is only `must_address_item_id` plus `description`.
- `MA-CW-*` items may still reference `CW-E*` evidence units through a separate facilitator-side mapping table or equivalent protocol traceability note.
- The existing candidate table in `facilitator_ledger_draft_v0.md` is treated as protocol-level traceability metadata, not as proof that the current Pydantic `MustAddressItem` supports `evidence_unit_ids`.
- No artifact in this lane should add an `evidence_unit_ids` field to the current `MustAddressItem` schema block or describe that field as already schema-valid.
- Any future adapter or schema-extension work must start from this contract and must be explicitly authorized after review.

## Underreach observability evidence-unit reference handling

For this draft fixture:

- The canonical current `UnderreachObservability` payload is only `present`, optional `basis`, and optional `notes`.
- `underreach_observability.evidence_unit_ids` may still be used as protocol traceability metadata or prose rationale outside the current Pydantic object.
- The draft ledger's underreach evidence references are evidence-unit-anchored rationale only; they are not a frozen Pydantic field.
- No artifact in this lane should add an `evidence_unit_ids` field to the current `UnderreachObservability` schema block or describe that field as already schema-valid.
- Any future adapter or schema-extension work must explicitly reconcile this field before ledger freeze, scoring traceability sign-off, or schema implementation.

## Impact on existing fixture files

| File | Edit required now | Reason |
| --- | --- | --- |
| `facilitator_ledger_draft_v0.md` | No | It already preserves the blocker and candidate protocol metadata without pretending schema compliance. |
| `evidence_registry_draft_v0.md` | No | Evidence-unit inventory can remain unchanged; this decision only governs placement and traceability contract. |
| `blind_judgement_adapter_note_v0.md` | No | It already records that `decision_shape` freeze, evidence attachment, and must-address coverage remain unresolved for executable blind use. |
| `fixture_authoring_receipt_v0.md` | Yes, minimal linkage only | Record this decision as accepted for docs-only next-step use while preserving all no-readiness boundaries. |

## Remaining blockers

- ledger freeze not performed
- second-label audit not performed
- source-byte hashes and retrieval timestamps captured for CW-P1 through CW-P6, but the EvidenceUnit registry remains unfrozen
- memorization probe not run
- no BlindJudgement schema instance
- no scoring
- no validation
- no judgment-quality claim
- whole-fixture hygiene acceptance not completed after this status-refresh patch

## Validation checks performed

- Required source hash verification completed for the eight named source files; all matched the requested SHA256 values.
- `git diff --check` must pass on touched files for this authoring slice.
- Participant-facing packet change scan must confirm no `participant_packet_draft_v0.md` text was changed in this slice.
- Targeted language scan must confirm no schema implementation or scoring-ready claim was introduced by this decision or receipt linkage.

## Next authorized step

Run a bounded post-hygiene recheck for HF-01 closure and patch-caused regressions before whole-fixture hygiene acceptance. This artifact is accepted only as a docs-only field-placement decision basis for the next fixture step; it does not authorize schema implementation, ledger freeze, blind use, memorization-probe execution, scoring, validation, proof-run, product proof, or judgment-quality claims.
