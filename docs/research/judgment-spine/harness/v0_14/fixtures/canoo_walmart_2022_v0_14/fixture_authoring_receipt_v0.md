# Canoo/Walmart v0.14 Fixture Authoring Receipt v0

```yaml
retrieval_header_version: 1
artifact_role: Research artifact
scope: Receipt for the docs-only Canoo/Walmart v0.14 draft fixture pack.
use_when:
  - Checking what was authored in the draft Canoo/Walmart v0.14 fixture pack.
  - Verifying blocked-before-scoring status before any later review or patch.
  - Finding hard gates for participant packet, evidence registry, facilitator ledger, and blind-judgment adaptation.
authority_boundary: retrieval_only
input_hashes:
  source_packet_v0.md: 6E2BC0894A36C08B0712C8FE045DF812D3A8857E525CA4412832866FF405E473
  safety_receipt_v0.md: 284CB7EE77AF1D9F2325317528DC0E1404AD2978AE99B10D8FBB3722BE5B9A67
  participant_packet_v0.md: E0191512B1A5AD292C023304321B6FD870B4C1CF591DDFF8708ACC69D5B3324F
  blind_judgments_v0.md: 2DF41433DCFACB31832CD51E65EC424888B7EB8955115D6949A35E8C7F2E8225
  owner_context_judgments_v0.md: A12BDC0416FC41502AB0B46B70338FF40FF118008D5D808C5E91BDD265E3B2E8
  pre_reveal_judgment_comparison_v0.md: 2AD850D94A29438D54491AA5EE72D8D79332E04F6C78E03BF960CF28BEEAEE80
  facilitator_ledger_v0.md: 6356C45D8E9B75732DB3D146EABFFCE4AD2775BCDD23D0205E26A46222FCE739
  reveal_readout_v0.md: 927DB2F16D3D9DF9EBB9DF20F6A35F00659C7C671EEC8ADAF4104BD7535C3A7E
  outcome_calibration_v0.md: 8E5766B11F80D716ACFB376E8227A9C610BBB906949AF65C9C1791A070C0A2F0
  fixture_admission_review_v0.md: D81BA050852B6844D3F76D6F840C51A9538E1E4A3628B504C0820821E850D933
  pydantic_schema_reference.md: CFFC7BCAC179B752B9A77204ECA6A6399D30DD7CB6B2C52533E3EC0FDC031D8D
  band_input_labeling_rubric.md: 0CE6E9584F4F1C4716559A654870AF43EBED3E5D53D3279AB658993B7DE1C2AE
  judgement_case_construction_protocol.md: FDEA14A1767D135A8DD56AF073AF0E5E3206B945FB9E603F597491D795889C71
  blind_judgement_schema_and_harness_protocol.md: ED80A0C0D7EC2252E5FC07EC175CFAD3FEE5F3D1F4527812A7813E2C5EE85EE4
  draft_fixture_pack_adversarial_review_v0.md: 016BD1DF23F0ABDCB0146109E51379D1DA27E77773F8DEFA29790D118161D73F
  participant_packet_draft_v0.md: 059EE78287C0F667DD75568F3179EE8424D2FFCD42CCC2882C177F5A7C9C2FD6
  evidence_registry_draft_v0.md: 47BBA3BE55627FDE39B347A24E20779005B633B2143ACEE51625AE21460B47B1
  blind_judgement_adapter_note_v0.md: 3F1D3EDDB1D5F1DD2C3871F6BF4EC97913D8A5930EEFC96DF23D8727D04AAE6B
  source_acquisition_receipt_v0.md: 621EA29B85C3D98936326E47012149582BF28F7B891EE3A810844D0B1CC5264C
  source_manifest_participant_safe_adapter_decision_v0.md: 39E92DB6C9D86C1BB18857069CF0507065C4460A15B3293359611875B3DB2E32
  protocol_pydantic_reconciliation_decision_v0.md: FA33293C4A774DC947DB836DEFBE1D9B3CE87A3DDEEFBE2E2C7529BD25BD879B
  protocol_pydantic_reconciliation_decision_adversarial_review_v0.md: 54AFA84BA368F05CF9D2E1358D5CCD6F21B9FAF3F747847B0205C825ABCEBB4F
  protocol_pydantic_reconciliation_decision_post_patch_adversarial_recheck_v0.md: 6C884828AFCC75BB8B6D286A36D544E522C39EF3A2C2B3760B71E19AB3EF6CF2
  whole_fixture_hygiene_adversarial_review_v0.md: 41595CB8D431DC3F0D95C816F38D7241E2C4702301775152D3BFBD7586C7CBA0
  whole_fixture_hygiene_post_patch_adversarial_recheck_v0.md: 0F09A0C6065234F05383D1B3D98D0A0E1053E80695CFDFE587F0DE5D5A8DDB0F
open_next:
  - docs/research/judgment-spine/harness/v0_14/pydantic_schema_reference.md
  - docs/research/judgment-spine/harness/v0_14/band_input_labeling_rubric.md
  - docs/research/judgment-spine/harness/v0_14/judgement_case_construction_protocol.md
  - docs/research/judgment-spine/harness/v0_14/blind_judgement_schema_and_harness_protocol.md
  - docs/research/judgment-spine/harness/v0_14/fixtures/canoo_walmart_2022_v0_14/blind_judgement_adapter_note_v0.md
  - docs/research/judgment-spine/harness/v0_14/fixtures/canoo_walmart_2022_v0_14/protocol_pydantic_reconciliation_decision_v0.md
```

- Status: DRAFT_FIXTURE_PACK_BLOCKED_BEFORE_SCORING
- Artifact type: docs-only draft fixture pack receipt
- Draft fixture root: `docs/research/judgment-spine/harness/v0_14/fixtures/canoo_walmart_2022_v0_14/`
- Implementation, runtime, package, test, automation, model run, memorization-probe execution, scoring execution, validation execution, proof-run, product-proof, lesson-promotion, commit, push, or PR authorized: no
- Strict readiness, validation, acceptance, source-of-truth promotion, probe-safety, score-readiness, harness superiority, product-proof, or lesson-promotion claims: not proven

## Source Context Receipt

```yaml
orca_start_preflight:
  agents_read: yes
  overlay_read: yes
  source_pack: custom S1 plus Canoo/Walmart case artifacts, fixture-admission review, and v0.14 schemas/protocols
  edit_permission: docs-write
  target_scope: Create the docs-only Canoo/Walmart v0.14 draft fixture pack and narrow discovery pointers only.
  dirty_state_checked: yes
  blocked_if_missing: no
source_context_status: SOURCE_CONTEXT_READY
method_sequence:
  overlay_read_before_project_work: yes
  fixture_admission_review_consumed: yes
  band_input_labeling_rubric_read_before_ledger_draft: yes
```

Repository state caveat: this pack was authored in a workspace with existing dirty or untracked Judgment Spine state. These sources were used for this bounded draft pack, but dirty or untracked state does not prove acceptance, validation, readiness, source-of-truth promotion, implementation authorization, probe-safety, score-readiness, product proof, or harness superiority.

## Goal Fit

The pack fits the current Judgment Spine frontier by moving Canoo/Walmart from qualitative case learning toward fixture authoring surfaces without treating the qualitative case as scored proof.

The pack does not answer whether the blind LLM, owner-assisted judgment, or Orca has judgment quality. It only exposes the fields and blockers needed before a later review can decide whether this case can become a v0.14 scoring fixture.

## Canonical Draft Case ID

```yaml
internal_fixture_id: canoo_walmart_2022_v0_14
participant_visible_case_id: ev_last_mile_supplier_commitment_2022_v0_14
case_id_status: internal_fixture_id_frozen_for_this_docs_only_draft_pack
participant_visible_case_id_status: draft_alias_not_blind_run_accepted
format_basis: lowercase filesystem-safe slug with digits and underscores only
non_claim: These ID values are draft-pack consistency only; they are not fixture admission, probe pass, score-readiness, validation, source-of-truth promotion, or an accepted harness ID-linking adapter.
```

## Draft Fixture Pack Inventory

| Artifact | Path | Status |
| --- | --- | --- |
| Fixture authoring receipt | `docs/research/judgment-spine/harness/v0_14/fixtures/canoo_walmart_2022_v0_14/fixture_authoring_receipt_v0.md` | Created; this file |
| Participant packet draft | `docs/research/judgment-spine/harness/v0_14/fixtures/canoo_walmart_2022_v0_14/participant_packet_draft_v0.md` | Created; frontmatter draft only; not blind-use-ready; participant provenance placeholders preserved |
| Evidence registry draft | `docs/research/judgment-spine/harness/v0_14/fixtures/canoo_walmart_2022_v0_14/evidence_registry_draft_v0.md` | Created; source hashes and retrieval timestamps captured for CW-P1 through CW-P6 |
| Facilitator ledger draft | `docs/research/judgment-spine/harness/v0_14/fixtures/canoo_walmart_2022_v0_14/facilitator_ledger_draft_v0.md` | Created; ledger not frozen; labels candidate only |
| Blind judgement adapter note | `docs/research/judgment-spine/harness/v0_14/fixtures/canoo_walmart_2022_v0_14/blind_judgement_adapter_note_v0.md` | Created; adapter/blocker note plus docs-only blind-use entry contract; not harness-executable |
| Source-manifest participant-safe adapter decision | `docs/research/judgment-spine/harness/v0_14/fixtures/canoo_walmart_2022_v0_14/source_manifest_participant_safe_adapter_decision_v0.md` | Accepted docs-only decision basis for next fixture step; not blind-use-ready |
| Source acquisition receipt | `docs/research/judgment-spine/harness/v0_14/fixtures/canoo_walmart_2022_v0_14/source_acquisition_receipt_v0.md` | Current live source-byte capture for CW-P1 through CW-P5 plus owner-supplied CW-P6 SEC filing capture |

## Fixture Admission Review Receipt

```yaml
review_report: docs/review-outputs/adversarial-artifact-reviews/canoo_walmart_fixture_admission_scoring_readiness_adversarial_artifact_review_v0.md
review_report_hash: D81BA050852B6844D3F76D6F840C51A9538E1E4A3628B504C0820821E850D933
recommendation: accept_with_friction
fixture_admission_verdict: admit_to_fixture_authoring
consumed_findings:
  FA-01: Blind judgment not in harness-executable BlindJudgement schema format.
  FA-02: Facilitator ledger not in v0.14 FacilitatorLedger schema format.
  FA-03: Participant packet missing v0.14 YAML frontmatter.
  FA-04: No EvidenceUnit registry exists for this case track.
  FA-05: Band floor mechanics will place no-proceed under-band; declare underreach_observability.present false before ledger freeze.
  FA-06: Blind judgment cleanliness is user_supplied_not_independently_verified.
  FA-07: Missing outcome evidence must be annotated as not_established.
  FA-08: band_input_labeling_rubric.md must be used before ledger drafting.
  FA-09: Pricing-cap claim lacks source-row citation and is not used as decisive scoring evidence here.
post_authoring_status: draft_only_not_accepted_not_validated_not_score_ready
```

## Draft Fixture Pack Review Patch Receipt

```yaml
review_report: docs/review-outputs/adversarial-artifact-reviews/canoo_walmart_v0_14_draft_fixture_pack_adversarial_review_v0.md
review_report_hash: 016BD1DF23F0ABDCB0146109E51379D1DA27E77773F8DEFA29790D118161D73F
owner_authorization: patch DFP-01 and DFP-02, with DFP-03 through DFP-05 cleaned up while touching the same files
patched_findings:
  DFP-01: participant packet frontmatter case_id changed to non-identifying alias; internal fixture ID preserved outside participant-visible frontmatter.
  DFP-02: compound-source EvidenceUnits split into single-source draft units; ledger and adapter candidate references remapped.
  DFP-03: NOT_COMMITTED removed from draft schema block; committed_at is now a freeze-required field outside the draft instance.
  DFP-04: protocol/Pydantic field-placement discrepancy now named as an implementation and freeze blocker.
  DFP-05: underreach_observability rationale now cites candidate evidence unit IDs.
post_patch_status: patched_draft_only_not_accepted_not_validated_not_score_ready
```

## Source-Manifest Adapter Decision Receipt

```yaml
adapter_decision_artifact: docs/research/judgment-spine/harness/v0_14/fixtures/canoo_walmart_2022_v0_14/source_manifest_participant_safe_adapter_decision_v0.md
adapter_decision_review_report: docs/review-outputs/adversarial-artifact-reviews/canoo_walmart_source_manifest_adapter_decision_adversarial_artifact_review_v0.md
adapter_decision_review_report_hash: 9C16EBCE0A4633B87CD179D9AA5CB17B8CB48DE56A7F83E25E5D9B651636C7BE
adapter_decision_post_patch_recheck_report: docs/review-outputs/adversarial-artifact-reviews/canoo_walmart_source_manifest_adapter_decision_post_patch_adversarial_recheck_v0.md
adapter_decision_post_patch_recheck_report_hash: 6785B63D32EFF8266D517BFDB0FBA3F36B99BB1EE8638FBB10DD91B5CF08855D
adapter_decision_reviewed_hash: 285B4B8509CFFF166617D5F1414DE211177C38D06D8B93CAF8266AF9100D04F3
adapter_decision_current_hygiene_hash: 39E92DB6C9D86C1BB18857069CF0507065C4460A15B3293359611875B3DB2E32
adapter_decision_hash_pin_scope: current_hash_pinned_after_completed_source_acquisition_status_refresh
adapter_decision_status: accepted_for_next_fixture_step_not_blind_use_ready
owner_acceptance_basis: current_turn_authorized_acceptance_housekeeping_after_accept_recheck
decision_shape:
  participant_visible_view: safe case alias plus source IDs CW-P1 through CW-P6, participant-safe source aliases, and withheld pre-seal placeholders only; no excluded-source metadata or source roles
  facilitator_internal_view: internal fixture ID, raw locators, titles, source-byte hashes for CW-P1 through CW-P6, retrieval timestamps for CW-P1 through CW-P6, exclusion rationale, and spoiler controls
  post_reveal_audit_view: facilitator/internal provenance may be joined after the blind answer is sealed or inside a non-participant-facing review lane
fixture_status_after_adapter_decision: patched_draft_only_not_accepted_not_validated_not_score_ready
non_claim: Adapter authoring does not prove participant-packet readiness, probe safety, scoring readiness, validation, fixture admission, product proof, or judgment quality.
```

Targeted patch receipt:

```yaml
patched_review_findings:
  SM-01: adapter receipt input hash to be refreshed after this receipt patch; stale self-reference acknowledged and resolved by final hash update in the adapter decision
  SM-02: participant packet and adapter now use WITHHELD_OR_PLACEHOLDER_BEFORE_SEAL as the canonical pre-seal display token for withheld hash and retrieval timestamp values
  SM-03: excluded_before_seal metadata moved out of the participant-visible manifest and marked facilitator/internal only before seal
  SM-04: receipt records that adapter hash pinning is deferred until post-patch recheck or owner acceptance to avoid a reciprocal hash loop
  SM-05: source_role is not shown before seal unless a separate participant-facing source-authoring decision authorizes it
  SM-06: participant-safe alias constraints now define positive opacity requirements and prohibited alias content
```

Acceptance housekeeping receipt:

```yaml
accepted_recheck_recommendation: accept
accepted_recheck_report_hash: 6785B63D32EFF8266D517BFDB0FBA3F36B99BB1EE8638FBB10DD91B5CF08855D
adapter_reviewed_hash_pinned_in_receipt: 285B4B8509CFFF166617D5F1414DE211177C38D06D8B93CAF8266AF9100D04F3
hash_loop_boundary: >
  The receipt pins the adapter's current post-hygiene hash. The adapter
  separately pins the receipt hash available before this hygiene patch. Do not
  treat these two hashes as a mutual final-state hash lock.
adapter_acceptance_scope: source_manifest_decision_basis_for_next_fixture_step_only
still_blocked:
  - blind use
  - memorization probe execution
  - model runs
  - scoring
  - ledger freeze
  - schema implementation
  - validation
  - proof-run
  - product proof
  - judgment-quality claim
```

## Protocol/Pydantic Reconciliation Decision Receipt

```yaml
reconciliation_decision_artifact: docs/research/judgment-spine/harness/v0_14/fixtures/canoo_walmart_2022_v0_14/protocol_pydantic_reconciliation_decision_v0.md
reconciliation_decision_hash: FA33293C4A774DC947DB836DEFBE1D9B3CE87A3DDEEFBE2E2C7529BD25BD879B
reconciliation_decision_review_report: docs/review-outputs/adversarial-artifact-reviews/canoo_walmart_protocol_pydantic_reconciliation_decision_adversarial_review_v0.md
reconciliation_decision_review_report_hash: 54AFA84BA368F05CF9D2E1358D5CCD6F21B9FAF3F747847B0205C825ABCEBB4F
reconciliation_decision_post_patch_recheck_report: docs/review-outputs/adversarial-artifact-reviews/canoo_walmart_protocol_pydantic_reconciliation_decision_post_patch_adversarial_recheck_v0.md
reconciliation_decision_post_patch_recheck_report_hash: 6C884828AFCC75BB8B6D286A36D544E522C39EF3A2C2B3760B71E19AB3EF6CF2
accepted_recheck_recommendation: accept
closed_findings:
  - RD-01: receipt hash refresh plus documented hash-loop boundary
  - RD-02: underreach_observability.evidence_unit_ids protocol/Pydantic mismatch addressed outside current Pydantic object
  - RD-03: decision_shape injection ambiguity removed and contestant-output autonomy preserved
blast_radius_result: no blocker or major patch-caused regression found
protocol_pydantic_reconciliation_decision_status: accepted_for_next_fixture_step_not_schema_implementation_ready_source_acquisition_status_refreshed
acceptance_scope: docs_only_field_placement_decision_basis_for_next_fixture_step_only
still_blocked:
  - schema implementation
  - ledger freeze
  - blind use
  - memorization probe execution
  - model runs
  - scoring
  - validation
  - proof-run
  - product proof
  - judgment-quality claim
non_claim: Reconciliation decision acceptance does not prove schema implementation readiness, ledger-freeze readiness, blind-use readiness, scoring readiness, validation, product proof, or judgment quality.
```

## Whole Fixture Hygiene Patch Receipt

```yaml
whole_fixture_hygiene_review_report: docs/review-outputs/adversarial-artifact-reviews/canoo_walmart_v0_14_fixture_hygiene_adversarial_review_v0.md
whole_fixture_hygiene_review_report_hash: 41595CB8D431DC3F0D95C816F38D7241E2C4702301775152D3BFBD7586C7CBA0
whole_fixture_hygiene_post_patch_recheck_report: docs/review-outputs/adversarial-artifact-reviews/canoo_walmart_v0_14_fixture_hygiene_post_patch_adversarial_recheck_v0.md
whole_fixture_hygiene_post_patch_recheck_report_hash: 0F09A0C6065234F05383D1B3D98D0A0E1053E80695CFDFE587F0DE5D5A8DDB0F
review_recommendation: patch_before_acceptance
post_patch_recheck_recommendation: accept
owner_authorization: current_turn_authorized_narrow_docs_only_hygiene_patch_after_accepting_findings_as_decision_input
patched_findings:
  HF-01: protocol/Pydantic decision status refreshed to accepted docs-only next-step basis while preserving no-readiness boundaries
  HF-02: source-manifest adapter receipt hash relationship and accepted recheck provenance refreshed with hash-loop boundary
  HF-03: participant packet blockers distinguish closed DFP/source-manifest hygiene gates from remaining blind-use gates
closed_findings:
  - HF-01
  - HF-02
  - HF-03
blast_radius_result: no blocker or major patch-caused regression found
post_patch_status: hygiene_patch_rechecked_and_accepted_not_validated_not_score_ready
whole_fixture_hygiene_status: accepted_docs_only_hygiene_not_readiness
still_blocked:
  - schema implementation
  - ledger freeze
  - blind use
  - memorization probe execution
  - model runs
  - scoring
  - validation
  - proof-run
  - product proof
  - judgment-quality claim
non_claim: Hygiene acceptance does not prove blind-use readiness, scoring readiness, schema implementation readiness, validation, product proof, or judgment quality.
```

## Source Acquisition Receipt

```yaml
source_acquisition_receipt: docs/research/judgment-spine/harness/v0_14/fixtures/canoo_walmart_2022_v0_14/source_acquisition_receipt_v0.md
source_acquisition_receipt_hash: 621EA29B85C3D98936326E47012149582BF28F7B891EE3A810844D0B1CC5264C
source_acquisition_status: complete_current_live_or_owner_supplied_capture_not_historical_archive
captured_source_ids:
  - CW-P1
  - CW-P2
  - CW-P3
  - CW-P4
  - CW-P5
  - CW-P6
blocked_source_ids: []
evidence_registry_hash_after_source_acquisition: 47BBA3BE55627FDE39B347A24E20779005B633B2143ACEE51625AE21460B47B1
participant_packet_hash_after_placeholder_preservation: 059EE78287C0F667DD75568F3179EE8424D2FFCD42CCC2882C177F5A7C9C2FD6
source_manifest_adapter_hash_after_source_status_refresh: 39E92DB6C9D86C1BB18857069CF0507065C4460A15B3293359611875B3DB2E32
protocol_pydantic_decision_hash_after_source_status_refresh: FA33293C4A774DC947DB836DEFBE1D9B3CE87A3DDEEFBE2E2C7529BD25BD879B
non_claim: Source acquisition does not prove participant-packet readiness, blind-use readiness, scoring readiness, ledger-freeze readiness, validation, product proof, or judgment quality.
```

## Blind-Use Entry Contract Receipt

```yaml
blind_judgement_adapter_note: docs/research/judgment-spine/harness/v0_14/fixtures/canoo_walmart_2022_v0_14/blind_judgement_adapter_note_v0.md
blind_judgement_adapter_note_hash: 3F1D3EDDB1D5F1DD2C3871F6BF4EC97913D8A5930EEFC96DF23D8727D04AAE6B
entry_contract_status: docs_only_gate_contract_not_executed
smallest_complete_intervention: >
  The existing blind-adapter note now carries the entry contract because it
  already owned the blind-judgement blocker. No new standalone artifact was
  created.
target_model_family_status: OWNER_DECISION_REQUIRED
memorization_probe_status: not_run_not_authorized
blind_run_status: not_run_not_authorized
non_claim: Entry-contract authoring does not prove probe safety, blind-use readiness, scoring readiness, validation, product proof, or judgment quality.
```

## Hard Blockers Before Scoring

- Participant packet frontmatter: drafted with a participant-visible non-identifying case alias and canonical withheld pre-seal placeholders, and the case-local source-manifest adapter decision is accepted as the source-manifest decision basis for the next fixture step, but the packet is still not blind-use-ready because the adapter has not been implemented in a harness/rendering path and downstream gates remain unresolved.
- Clean participant packet hash for fixture use: not computed; draft remains editable.
- Source-byte hashes: captured for CW-P1 through CW-P5 from current live public web bytes and CW-P6 from owner-supplied local SEC filing bytes; CW-P7 remains excluded from the participant packet.
- Retrieval timestamps: normalized for CW-P1 through CW-P5 current capture and CW-P6 owner-supplied local file timestamp.
- Evidence registry freeze: not performed; single-source draft EvidenceUnits exist, but registry freeze and cross-artifact ID remapping remain unresolved.
- Facilitator ledger freeze: not performed; `ledger_freeze_hash` is `NOT_COMPUTED` and `committed_at` must be set at freeze time as a valid ISO-8601 UTC timestamp with Z suffix.
- Frozen band inputs: not frozen; all labels remain candidate or unfrozen.
- Second-label audit: not performed.
- Must-address items: candidate only; not frozen.
- `underreach_observability.present`: candidate false as required by FA-05 and now evidence-unit-anchored, but not frozen.
- Protocol/Pydantic field placement: accepted as a docs-only decision basis for `case_family`, `decision_shape`, must-address evidence-unit references, and underreach-observability evidence-unit references; schema implementation, ledger freeze, and scoring traceability sign-off remain blocked.
- Blind-use entry contract: authored docs-only in `blind_judgement_adapter_note_v0.md`, but target model family remains owner-required before any meaningful memorization probe or clean blind-run preflight.
- BlindJudgement schema instance: not created; the current blind LLM answer is narrative, user-supplied, and missing run metadata.
- Blind judgment cleanliness: user-supplied and not independently verified.
- Memorization probe: not run for any model family; Canoo/Walmart known-fame risk remains unresolved.
- Walmart-specific outcome gaps: deployment volume, accepted units, uptime, termination-right exercise, financial exposure at bankruptcy, and protective-term effectiveness remain not established.
- Mapping and scoring: not run; no action band, scoring result, case report, or failure event exists.

## Leakage And Memorization Gates

The participant draft uses only pre-cutoff packet-safe evidence summaries and intentionally does not expose raw source URLs, source titles, source filenames, company names, agreement terms, actual action, outcome facts, facilitator labels, calibration text, candidate band inputs, or must-address items in the participant-facing section.

Raw v0.14 source-manifest fields are a leakage conflict for this anonymized case because raw URLs and titles would identify the retailer, supplier, and decision. The participant packet now uses a non-identifying `case_id` alias and withheld pre-seal placeholders, and `source_manifest_participant_safe_adapter_decision_v0.md` defines an accepted three-view adapter for the next fixture-step decision basis, but blind contestant use still requires a later harness/rendering path or explicit non-blind fixture mode plus all downstream gates.

Canoo/Walmart is a real, public, named case with unresolved memorization risk. A memorization probe must run before any target model family sees the participant packet. Probe `fail` rejects or quarantines the contestant-case pair for that model family. Probe `ambiguous` quarantines until operator review. Probe `pass` is model-family scoped and still does not prove no memorization.

## Not-Proven Boundaries

This draft pack does not prove:

- Judgment Spine validation;
- v0.14 harness validation;
- case admission;
- participant-packet cleanliness for blind use;
- blind judgment cleanliness;
- memorization-probe pass;
- scoring readiness;
- implementation readiness;
- source-of-truth promotion;
- acceptance or approval;
- buyer validation;
- product readiness;
- feature readiness;
- commercial readiness;
- model-training readiness;
- harness superiority;
- memory compounding;
- lesson transfer or lesson promotion.

## Source-Read Ledger

| Source | Why read |
| --- | --- |
| `AGENTS.md` and `.agents/workflow-overlay/README.md` | Workspace and overlay authority. |
| `.agents/workflow-overlay/source-loading.md`, `artifact-roles.md`, and `retrieval-metadata.md` | Source budget, artifact roles, and retrieval metadata. |
| `docs/research/judgment-spine/harness/v0_14/index.md` | v0.14 spec index and source-of-truth roles. |
| v0.14 schema and protocol files | Participant packet, EvidenceUnit, FacilitatorLedger, band input, BlindJudgement, and case-construction controls. |
| `docs/review-outputs/adversarial-artifact-reviews/canoo_walmart_fixture_admission_scoring_readiness_adversarial_artifact_review_v0.md` | Fixture-admission recommendation and friction findings. |
| `docs/research/judgment-spine/cases/canoo-walmart/source_packet_v0.md` | Pre-cutoff evidence units and participant-safe source substrate. |
| `docs/research/judgment-spine/harness/v0_14/fixtures/canoo_walmart_2022_v0_14/source_acquisition_receipt_v0.md` | Current live source-byte capture receipt for CW-P1 through CW-P5 and owner-supplied CW-P6 source capture. |
| `docs/research/judgment-spine/cases/canoo-walmart/participant_packet_v0.md` | Existing anonymized participant packet and source leakage handling. |
| `docs/research/judgment-spine/cases/canoo-walmart/blind_judgments_v0.md` | User-supplied blind LLM answer and cleanliness caveat. |
| `docs/research/judgment-spine/cases/canoo-walmart/facilitator_ledger_v0.md` | Facilitator-only actual action, agreement terms, and outcome gaps. |
| `docs/research/judgment-spine/cases/canoo-walmart/outcome_calibration_v0.md` | Qualitative split-axis calibration and non-claim boundaries. |

Sources deliberately not used for participant-facing content: facilitator ledger, reveal readout, outcome calibration, actual agreement terms, post-cutoff outcome facts, candidate band inputs, must-address items, review findings, source URLs, source titles, source filenames, and company names.

## Next Authorized Step

The next authorized step is an owner-directed target-model-family decision for the docs-only blind-use entry contract. Do not route directly to blind use, probe execution, model runs, scoring, ledger freeze, schema implementation, validation, proof-run, product-proof, lesson promotion, or harness-superiority claims.

## Protocol/Pydantic Reconciliation Decision Linkage

- `docs/research/judgment-spine/harness/v0_14/fixtures/canoo_walmart_2022_v0_14/protocol_pydantic_reconciliation_decision_v0.md`: accepted as a docs-only field-placement decision basis for the next fixture step after post-patch adversarial recheck; not schema implementation readiness, ledger-freeze readiness, blind-use readiness, validation, scoring evidence, or judgment-quality evidence.

Required boundary: plumbing works only; not judgment quality.
