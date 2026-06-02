# Canoo/Walmart Participant-Safe Source Manifest Adapter Decision v0

```yaml
retrieval_header_version: 1
artifact_role: Research artifact
scope: Case-local source-manifest and ID-linking adapter decision for the Canoo/Walmart v0.14 fixture candidate.
use_when:
  - Checking which source-manifest fields may be shown to blind contestants.
  - Linking participant-visible aliases to facilitator-only fixture and source provenance.
  - Reviewing remaining gates before blind use, memorization probe, scoring, ledger freeze, or schema implementation.
authority_boundary: retrieval_only
input_hashes:
  fixture_authoring_receipt_v0.md: E2AFBEB0D8A9740015BE408D34D19F2A922E5887A9D34D807E63845CCF0B841A
  participant_packet_draft_v0.md: 059EE78287C0F667DD75568F3179EE8424D2FFCD42CCC2882C177F5A7C9C2FD6
  evidence_registry_draft_v0.md: 47BBA3BE55627FDE39B347A24E20779005B633B2143ACEE51625AE21460B47B1
  source_acquisition_receipt_v0.md: 621EA29B85C3D98936326E47012149582BF28F7B891EE3A810844D0B1CC5264C
  facilitator_ledger_draft_v0.md: B10C4B7A282CDB72D9320AB7E55FB9ECE7751CC10124A4415856115BE1D6AAC6
  blind_judgement_adapter_note_v0.md: B16206BB5859B61CF20C16112EF9AFE59972F0E4A6E73840241B9BFD6E45EB78
  post_patch_adversarial_recheck_v0.md: DEF486F288A43BB63647C72E4EF59A22FD6A155E38E3BE76FB28A06CE6675629
  source_manifest_adapter_adversarial_review_v0.md: 9C16EBCE0A4633B87CD179D9AA5CB17B8CB48DE56A7F83E25E5D9B651636C7BE
  source_manifest_adapter_post_patch_adversarial_recheck_v0.md: 6785B63D32EFF8266D517BFDB0FBA3F36B99BB1EE8638FBB10DD91B5CF08855D
hash_loop_boundary:
  fixture_authoring_receipt_v0.md_original_authoring_hash: DB80D5576553CFFEBEE86B987287AE8EC0A6CDB17FB6BAACEA7A5E4A970DD2B2
  fixture_authoring_receipt_v0.md_post_reconciliation_acceptance_hash: 32C99D992411CB88F536E4C9E6C706007454F731272F774397DAA95CC4B4F1E9
  fixture_authoring_receipt_v0.md_pre_source_acquisition_hash: E2AFBEB0D8A9740015BE408D34D19F2A922E5887A9D34D807E63845CCF0B841A
  rule: >
    The input_hashes entry pins the receipt state available before this
    source-acquisition status refresh. The receipt may separately pin this
    adapter's post-refresh hash after this update. Do not treat these hashes as
    a mutual final-state hash lock.
open_next:
  - docs/research/judgment-spine/harness/v0_14/fixtures/canoo_walmart_2022_v0_14/fixture_authoring_receipt_v0.md
  - docs/research/judgment-spine/harness/v0_14/fixtures/canoo_walmart_2022_v0_14/participant_packet_draft_v0.md
  - docs/research/judgment-spine/harness/v0_14/fixtures/canoo_walmart_2022_v0_14/evidence_registry_draft_v0.md
  - docs/research/judgment-spine/harness/v0_14/fixtures/canoo_walmart_2022_v0_14/source_acquisition_receipt_v0.md
  - docs/research/judgment-spine/harness/v0_14/fixtures/canoo_walmart_2022_v0_14/facilitator_ledger_draft_v0.md
stale_if:
  - Any input hash changes.
  - The participant-visible case alias changes.
  - Source IDs CW-P1 through CW-P7 are added, removed, renamed, or reclassified.
  - The v0.14 source-manifest, EvidenceUnit, BlindJudgement, or FacilitatorLedger protocol changes.
  - An adversarial review rejects or materially amends this adapter decision.
```

- Status: SOURCE_MANIFEST_ADAPTER_DECISION_ACCEPTED_FOR_NEXT_FIXTURE_STEP_NOT_BLIND_USE_READY
- Internal fixture ID: `canoo_walmart_2022_v0_14`
- Participant-visible case ID: `ev_last_mile_supplier_commitment_2022_v0_14`
- Adapter scope: case-local docs-only decision for participant display, facilitator provenance, and post-reveal audit linkage
- Fixture status after this decision: source bytes and retrieval timestamps are captured for CW-P1 through CW-P6; blind use, probe, scoring, ledger freeze, schema implementation, validation, proof-run, and lesson promotion remain blocked

## Source Context Receipt

```yaml
orca_start_preflight:
  agents_read: yes
  overlay_read: yes
  source_pack: custom S0 plus Canoo/Walmart fixture receipt, participant packet, evidence registry, facilitator ledger, blind adapter note, and post-patch recheck
  edit_permission: docs-write
  target_scope: Author a docs-only case-local source-manifest and participant-safe ID-linking adapter decision for the Canoo/Walmart v0.14 draft fixture pack.
  dirty_state_checked: yes
  blocked_if_missing: no
source_context_status: SOURCE_CONTEXT_READY
```

Dirty-state caveat: the fixture pack and related review reports are untracked in the current workspace, and multiple overlay files are modified. This artifact can support the accepted source-manifest decision basis for the next fixture step, but it does not prove validation, readiness, source-of-truth promotion, implementation authorization, probe-safety, score-readiness, product proof, or judgment quality.

## Decision Summary

Use a three-view source-manifest adapter for this case:

1. Participant-visible view: safe case alias, generic source IDs, participant-safe source aliases, and withheld pre-seal placeholders only; excluded-source metadata remains facilitator/internal before seal.
2. Facilitator/internal view: internal fixture ID, source-packet provenance, raw locators, source titles, source-byte hashes, retrieval timestamps, exclusion rationale, and spoiler controls.
3. Post-reveal audit view: the facilitator/internal view may be exposed only after the blind judgment is sealed or during a source-authorized review that is not participant-facing.

This is a case-local adapter decision, not a v0.14 schema change. If a later implementation needs these rules in the harness or schema, protocol/Pydantic reconciliation must happen in a separate authorized lane.

## Field Visibility Contract

| Field | Participant-visible before seal | Facilitator/internal before seal | Post-reveal audit | Rule |
| --- | --- | --- | --- | --- |
| `case_id` | `ev_last_mile_supplier_commitment_2022_v0_14` | Same alias plus internal mapping | Both alias and internal fixture ID | Participant output uses only the alias. |
| `internal_fixture_id` | Not shown | `canoo_walmart_2022_v0_14` | May be shown | Internal linkage only; never participant-facing before seal. |
| `source_id` | May show generic IDs CW-P1 through CW-P6 | Full internal source IDs CW-P1 through CW-P7 | May be shown | CW-P7 remains excluded from participant material. |
| `source` | Participant-safe alias only | Raw source locator and title in source packet or facilitator-only provenance | May be shown | Raw locators, titles, filenames, and URL-bearing source strings are not participant-facing before seal. |
| `source_role` | Not shown before seal | Full facilitator role and source packet row | May be shown | Showing role labels before seal requires a separate participant-facing source-authoring decision. |
| `retrieval_timestamp` | Withheld or placeholder only | Normalized internal value when available | May be shown | Not ready until normalized; never use timestamp as a readiness claim. |
| `hash` | Withheld or placeholder only | Source-byte hash when computed | May be shown | Source-byte hashes are audit provenance, not participant facts. |
| source titles | Not shown | Facilitator-only | May be shown | Titles can reveal parties or prime the answer. |
| raw URLs and file paths | Not shown | Facilitator-only | May be shown | Locators can reveal identity even when the body is anonymized. |
| agreement terms | Not shown | Facilitator/reveal only | May be shown after seal | Agreement terms are reveal material, not blind-input material. |
| outcome facts | Not shown | Facilitator/reveal only | May be shown after seal | Outcomes are calibration material, not blind-input material. |
| candidate labels and must-address items | Not shown | Facilitator-only | May be shown after seal or in review | Labels would prime scoring behavior. |

## Participant-Visible Manifest View

This is the only source-manifest shape this adapter allows before a blind contestant seals an answer. It is a display contract, not a frozen Pydantic instance. It must not include excluded-source metadata, source roles, raw locators, raw source titles, filenames, company names, agreement terms, outcome facts, facilitator labels, or reveal material.

```yaml
participant_visible_source_manifest:
  case_id: ev_last_mile_supplier_commitment_2022_v0_14
  internal_fixture_id: WITHHELD_BEFORE_SEAL
  sources:
    - source_id: CW-P1
      source: PARTICIPANT_SAFE_SOURCE_ALIAS_CW_P1_RAW_LOCATOR_WITHHELD
      retrieval_timestamp: WITHHELD_OR_PLACEHOLDER_BEFORE_SEAL
      hash: WITHHELD_OR_PLACEHOLDER_BEFORE_SEAL
    - source_id: CW-P2
      source: PARTICIPANT_SAFE_SOURCE_ALIAS_CW_P2_RAW_LOCATOR_WITHHELD
      retrieval_timestamp: WITHHELD_OR_PLACEHOLDER_BEFORE_SEAL
      hash: WITHHELD_OR_PLACEHOLDER_BEFORE_SEAL
    - source_id: CW-P3
      source: PARTICIPANT_SAFE_SOURCE_ALIAS_CW_P3_RAW_LOCATOR_WITHHELD
      retrieval_timestamp: WITHHELD_OR_PLACEHOLDER_BEFORE_SEAL
      hash: WITHHELD_OR_PLACEHOLDER_BEFORE_SEAL
    - source_id: CW-P4
      source: PARTICIPANT_SAFE_SOURCE_ALIAS_CW_P4_RAW_LOCATOR_WITHHELD
      retrieval_timestamp: WITHHELD_OR_PLACEHOLDER_BEFORE_SEAL
      hash: WITHHELD_OR_PLACEHOLDER_BEFORE_SEAL
    - source_id: CW-P5
      source: PARTICIPANT_SAFE_SOURCE_ALIAS_CW_P5_RAW_LOCATOR_WITHHELD
      retrieval_timestamp: WITHHELD_OR_PLACEHOLDER_BEFORE_SEAL
      hash: WITHHELD_OR_PLACEHOLDER_BEFORE_SEAL
    - source_id: CW-P6
      source: PARTICIPANT_SAFE_SOURCE_ALIAS_CW_P6_RAW_LOCATOR_WITHHELD
      retrieval_timestamp: WITHHELD_OR_PLACEHOLDER_BEFORE_SEAL
      hash: WITHHELD_OR_PLACEHOLDER_BEFORE_SEAL
```

Participant-visible source facts must come from the participant packet body, not from raw source locators. `WITHHELD_OR_PLACEHOLDER_BEFORE_SEAL` is the canonical pre-seal display token for withheld `retrieval_timestamp` and `hash` values. Legacy `TBD_*` draft markers, if encountered in an older packet revision, are internal draft markers and must be substituted with `WITHHELD_OR_PLACEHOLDER_BEFORE_SEAL` before any participant display. If the harness requires a schema-valid internal manifest, the participant renderer must redact or substitute participant-safe display values while preserving full facilitator-side provenance separately.

## Participant-Safe Alias Constraints

Participant-safe source aliases must stay opaque. A valid alias may include only the source ID and a generic withheld-locator marker such as `PARTICIPANT_SAFE_SOURCE_ALIAS_CW_P1_RAW_LOCATOR_WITHHELD`.

Participant-safe aliases must not include:

- company, product, counterparty, supplier, retailer, customer, or source-publisher names;
- source titles, filenames, URL fragments, domain names, CIKs, ticker symbols, or filing-accession identifiers;
- source type labels such as annual results release, quarterly filing, media report, reservation announcement, or strategy note;
- event, agreement, volume, warrant, bankruptcy, liquidation, restriction, termination, delivery, or outcome terms;
- content-role labels that reveal financial distress, funding uncertainty, launch burden, alternative-supplier evidence, or any other scoring-relevant emphasis.

If a future participant-facing packet needs richer source descriptions, that requires a separate source-authoring decision and adversarial review before blind use.

## Facilitator/Internal Linkage View

This view is allowed only for facilitator-side fixture authoring, review, provenance verification, and post-seal audit. It is not participant-facing.

```yaml
internal_linkage_view:
  internal_fixture_id: canoo_walmart_2022_v0_14
  participant_visible_case_id: ev_last_mile_supplier_commitment_2022_v0_14
  participant_visible_case_id_status: draft_alias_not_blind_run_accepted
  source_provenance_location: docs/research/judgment-spine/cases/canoo-walmart/source_packet_v0.md
  source_manifest_location: docs/research/judgment-spine/harness/v0_14/fixtures/canoo_walmart_2022_v0_14/evidence_registry_draft_v0.md
  source_id_policy:
    CW-P1: facilitator_only_raw_locator_in_source_packet
    CW-P2: facilitator_only_raw_locator_in_source_packet
    CW-P3: facilitator_only_raw_locator_in_source_packet
    CW-P4: facilitator_only_raw_locator_in_source_packet
    CW-P5: facilitator_only_raw_locator_in_source_packet
    CW-P6: facilitator_only_raw_locator_in_source_packet
    CW-P7: excluded_from_participant_material_pending_separate_source_authoring_decision
  excluded_before_seal:
    - source_id: CW-P7
      participant_visibility: facilitator_internal_only_not_contestant_visible_before_seal
      reason: excluded_from_participant_material_pending_separate_source_authoring_decision
  source_byte_hash_status: complete_current_or_owner_supplied_capture_cw_p1_through_cw_p6
  retrieval_timestamp_status: complete_normalized_current_or_owner_supplied_capture_cw_p1_through_cw_p6
```

The adapter intentionally does not duplicate raw locators here. Current source
acquisition captured CW-P1 through CW-P5 from live public web bytes and CW-P6
from an owner-supplied local SEC filing capture, with hashes and retrieval
timestamps stored in the evidence registry. Keep participant display redacted
until the judgment is sealed.

## Post-Reveal Audit View

After a blind answer is sealed, or inside a read-only review lane that is not participant-facing, the audit view may join:

- participant-visible case alias;
- internal fixture ID;
- CW-P1 through CW-P7 source packet provenance;
- source-byte hashes and retrieval timestamps when computed;
- evidence-unit mapping;
- facilitator ledger labels;
- reveal and outcome-calibration material.

This post-reveal view is for auditability and calibration only. It is not a retroactive cleanliness claim for the blind run.

## Excluded And Deferred Source Handling

```yaml
excluded_or_deferred_sources:
  - source_id: CW-P7
    participant_visibility: facilitator_internal_only_not_contestant_visible_before_seal
    status: requires_separate_source_authoring_decision_before_any_participant_use
  - field: source_byte_hashes
    participant_visibility: withheld_before_seal
    status: complete_internal_provenance_field_cw_p1_through_cw_p6_captured
  - field: normalized_retrieval_timestamps
    participant_visibility: withheld_before_seal
    status: complete_internal_provenance_field_cw_p1_through_cw_p6_captured
```

If any excluded or deferred item becomes necessary for the participant-facing packet, the packet must be rebuilt or reviewed as a new participant-facing source-authoring decision. Do not silently add raw locators, titles, filenames, or company-identifying source hints to the participant view.

## Receipt Linkage Rule

The fixture receipt may link to this adapter decision as an accepted docs-only source-manifest decision basis for the next fixture step after the accepted post-patch recheck. That linkage does not change blind-use, probe, scoring, ledger-freeze, schema implementation, validation, proof-run, product-proof, or judgment-quality status.

Receipt wording should preserve:

- `DRAFT_FIXTURE_PACK_BLOCKED_BEFORE_SCORING`;
- `patched_draft_only_not_accepted_not_validated_not_score_ready`;
- source-byte hashes and retrieval timestamps captured for CW-P1 through CW-P6;
- participant packet not blind-use-ready;
- no model run, memorization probe, score, ledger freeze, validation, product proof, or lesson promotion.
- adapter hash should be pinned in the receipt only with a hash-loop boundary, because receipt and adapter updates intentionally do not form a mutual final-state hash lock.

## Validation Recipe For This Adapter

Implementation-time checks should be targeted and failure-capable:

1. Confirm the participant-visible packet section does not include company names, internal fixture ID, raw URLs, file paths, agreement terms, outcome facts, facilitator labels, or reveal material.
2. Confirm participant-visible manifest values use only the case alias, CW-P1 through CW-P6 source IDs, `PARTICIPANT_SAFE_SOURCE_ALIAS_*_RAW_LOCATOR_WITHHELD` strings, and `WITHHELD_OR_PLACEHOLDER_BEFORE_SEAL` placeholders.
3. Confirm CW-P7 and all excluded-source metadata remain excluded from participant-facing material.
4. Confirm internal fixture ID linkage appears only in facilitator/internal or retrieval-only sections.
5. Run a consistency scan for the participant-visible alias and internal fixture ID across touched artifacts.
6. Run whitespace validation and capture hashes for touched files.

Passing these checks would only support "adapter authored and locally checked." It would not prove blind-use readiness, probe safety, scoring readiness, validation, product proof, or judgment quality.

## Source-Read Ledger

| Source | Why read | Status |
| --- | --- | --- |
| `AGENTS.md` | Orca project operating boundary and docs-only default. | Supplied/read in current task. |
| `.agents/workflow-overlay/README.md` | Overlay entrypoint and binding rule. | Read. |
| `.agents/workflow-overlay/source-of-truth.md` | Source hierarchy, conflict rules, doctrine-change propagation. | Read; modified in workspace. |
| `.agents/workflow-overlay/source-loading.md` | Start-preflight and bounded source-loading rules. | Read; modified in workspace. |
| `.agents/workflow-overlay/artifact-roles.md` | Research artifact role and permissions. | Read; modified in workspace. |
| `.agents/workflow-overlay/retrieval-metadata.md` | Retrieval header contract. | Read. |
| `.agents/workflow-overlay/validation-gates.md` | Claim discipline and dirty-state boundary. | Read; modified in workspace. |
| `fixture_authoring_receipt_v0.md` | Current fixture status, IDs, blockers, and patch receipt. | Read; untracked. |
| `participant_packet_draft_v0.md` | Participant-facing packet and manifest surface. | Read; untracked. |
| `evidence_registry_draft_v0.md` | Source IDs, source manifest draft, excluded source handling, and completed CW-P1 through CW-P6 source acquisition status. | Read; untracked; hash refreshed after source acquisition. |
| `source_acquisition_receipt_v0.md` | Current live source-byte capture receipt for CW-P1 through CW-P5 and owner-supplied CW-P6 source capture. | Read; untracked. |
| `facilitator_ledger_draft_v0.md` | Facilitator-only leakage, spoiler, and freeze blockers. | Read; untracked. |
| `blind_judgement_adapter_note_v0.md` | Existing BlindJudgement adapter caveats and ID boundary. | Read; untracked. |
| `canoo_walmart_v0_14_draft_fixture_pack_post_patch_adversarial_recheck_v0.md` | Latest DFP closure and residual risk surface. | Read; untracked. |
| `canoo_walmart_source_manifest_adapter_decision_adversarial_artifact_review_v0.md` | SM-01 through SM-06 findings used for the targeted patch. | Read; untracked. |
| `canoo_walmart_source_manifest_adapter_decision_post_patch_adversarial_recheck_v0.md` | Accepted recheck closing SM-01 through SM-06 before owner acceptance housekeeping. | Read; untracked. |

## Non-Claims

- Not a fixture admission decision.
- Not participant-packet readiness.
- Not a schema implementation.
- Not historical archive source-byte proof.
- Not memorization-probe pass.
- Not a blind model run.
- Not scoring readiness.
- Not ledger freeze.
- Not validation.
- Not product proof.
- Not judgment-quality proof.

Required boundary: plumbing works only; not judgment quality.
