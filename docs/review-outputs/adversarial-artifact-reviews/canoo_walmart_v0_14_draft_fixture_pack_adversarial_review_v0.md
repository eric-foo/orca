# Canoo/Walmart v0.14 Draft Fixture Pack Adversarial Review v0

```yaml
retrieval_header_version: 1
artifact_role: Review report
scope: Adversarial artifact review of the Canoo/Walmart v0.14 draft fixture pack and bounded discovery pointers.
use_when:
  - Deciding whether the draft fixture pack can proceed to owner-authorized patching or remains blocked by artifact defects.
  - Checking whether FA-01 through FA-09 were correctly consumed without silent conversion.
  - Checking participant-packet leakage, EvidenceUnit field correctness, facilitator-ledger schema mapping, and blind-judgment adapter boundaries.
authority_boundary: retrieval_only
input_hashes:
  fixture_authoring_receipt_v0.md: 8D83BE764BE5BE34127C53FEB94FFF4191CE936524023C1A17EAFB7ED29ACF40
  participant_packet_draft_v0.md: 66A24DF645E1D6592C4F95B30395AAECBAF1B4F126BB6B6E0A7B776B6ECCD997
  evidence_registry_draft_v0.md: 79C22D86FEC835E9FB72682E57FB8F8FB99C382998D5596C0C76BF545478B093
  facilitator_ledger_draft_v0.md: 10E42DEE1B97F11874919E2F59FCD86D9E3ECF6D82100E6CE25D7BF9D5EFD313
  blind_judgement_adapter_note_v0.md: 2B7E0C6438F528736AC634C5ABDCD4C442383F896814A669009898A0CC36660B
  harness_v0_14_index.md: 3453D75546286B7755726076489C8550CB9AD60B53D02AADD1D5B57BE78BE769
  manifest_v0.md: 78B6821DDB9A38382199AEB218E4E68FABB434FDC631B0BA8C1CEC0D635E05F5
  case_index.md: 989D3764DB3965E7867B9B3B66F0D5AAB10FBEBA942865D5F6B5449476D0E13E
  adversarial_artifact_review_v0.md: 17188D11F4C151103CC746328D02F0DFC94FCF3AAD3F39714A510CEDBA5A60AA
  fixture_admission_review_v0.md: D81BA050852B6844D3F76D6F840C51A9538E1E4A3628B504C0820821E850D933
stale_if:
  - Any input hash changes.
  - v0.14 harness spec is superseded by a later version.
  - Any FA finding is accepted, patched, or retired by an authorized lane.
  - The draft fixture pack is patched by an owner-authorized pass.
```

---

## 1. Review Target and Purpose

**Review target:** Canoo/Walmart v0.14 draft fixture pack:
- `docs/research/judgment-spine/harness/v0_14/fixtures/canoo_walmart_2022_v0_14/fixture_authoring_receipt_v0.md`
- `docs/research/judgment-spine/harness/v0_14/fixtures/canoo_walmart_2022_v0_14/participant_packet_draft_v0.md`
- `docs/research/judgment-spine/harness/v0_14/fixtures/canoo_walmart_2022_v0_14/evidence_registry_draft_v0.md`
- `docs/research/judgment-spine/harness/v0_14/fixtures/canoo_walmart_2022_v0_14/facilitator_ledger_draft_v0.md`
- `docs/research/judgment-spine/harness/v0_14/fixtures/canoo_walmart_2022_v0_14/blind_judgement_adapter_note_v0.md`

**Bounded discovery-pointer targets:**
- `docs/research/judgment-spine/cases/canoo-walmart/case_index.md`
- `docs/research/judgment-spine/harness/v0_14/index.md`
- `docs/research/judgment-spine/manifest_v0.md`

**Pre-authoring review source:**
- `docs/review-outputs/adversarial-artifact-reviews/canoo_walmart_fixture_admission_scoring_readiness_adversarial_artifact_review_v0.md`

**Review purpose:** Adversarially verify that the draft fixture pack correctly consumes FA-01 through FA-09, preserves `DRAFT_FIXTURE_PACK_BLOCKED_BEFORE_SCORING`, maintains zero-spoiler participant-packet discipline, handles source-manifest aliasing as a blocker rather than a completed solution, produces schema-honest EvidenceUnit and FacilitatorLedger draft shapes, separates Pydantic fields from protocol metadata, keeps the adapter note non-scoreable, and keeps discovery pointers narrow and non-authorizing.

**Review lane:** Adversarial artifact review (read-only).
**Output mode:** `review-report` / `filesystem-output`
**Reviewer edit permission:** Read-only for all reviewed artifacts; docs-write for this report only.
**Patch queue:** Not authorized in this lane.

---

## 2. Source Context Status

```yaml
source_context_status: SOURCE_CONTEXT_READY
hash_verification:
  fixture_authoring_receipt_v0.md: EXACT_MATCH
  participant_packet_draft_v0.md: EXACT_MATCH
  evidence_registry_draft_v0.md: EXACT_MATCH
  facilitator_ledger_draft_v0.md: EXACT_MATCH
  blind_judgement_adapter_note_v0.md: EXACT_MATCH
  harness_v0_14_index.md: EXACT_MATCH
  manifest_v0.md: EXACT_MATCH
  case_index.md: EXACT_MATCH
  adversarial_artifact_review_v0.md: EXACT_MATCH
  fixture_admission_review_v0.md: EXACT_MATCH
```

All 10 verified target hashes match exactly. No hash mismatch. Dirty-state allowance applies to all reviewed artifacts (untracked); advisory findings proceed from visible artifact text.

---

## 3. Deep-Thinking and Adversarial-Review Invocation Status

```yaml
workflow_deep_thinking:
  reference_load: completed
  apply_status: applied
  application: framed_5_boundary_failure_modes_below

workflow_adversarial_artifact_review:
  reference_load: completed
  apply_status: applied
  application: applied_to_loaded_source_context_post_source_context_ready
```

### Deep-Thinking: Boundary Failure Mode Frame

Before listing findings, five failure modes were framed and governed the adversarial verification pass.

**FM-A: Over-claiming draft status** — Did any artifact imply scoring readiness, validation, fixture admission, clean blind-run status, memorization-probe pass, or implementation authorization that does not exist? The most dangerous form is a subtle signal (e.g., a status field that doesn't include NOT_FROZEN, a non-claims section that omits a key claim, or a discovery pointer that states the fixture is ready rather than blocked).

**FM-B: Silent FA finding conversion** — Did the draft pack absorb FA-01 through FA-09 as "work done" rather than "work defined"? A finding is silently converted when it disappears from blockers, is listed as resolved, or the artifact shows a completed field where the finding said a blocker existed.

**FM-C: Participant-facing leakage** — Does the participant packet body section (the section between the markers) contain any company name, source URL, source title, source filename, actual agreement term, post-cutoff fact, outcome, calibration content, candidate band input, or must-address item? Does the YAML frontmatter introduce any company-name or identity leakage that would be visible to a harness runner or contestant?

**FM-D: Schema shape defects** — Do the EvidenceUnit, FacilitatorLedger, and BlindJudgement draft shapes correctly map to v0.14 Pydantic schema fields, or do they invent patterns (multi-source IDs, placeholder strings in typed fields, extra protocol-only fields in Pydantic objects) that would mislead a later implementation-scoping or scoring-readiness lane?

**FM-E: Adapter note non-comparability** — Does the blind-judgment adapter note preserve the ladder-level ambiguity (3 vs. 4), avoid claiming a frozen ladder level, avoid treating the user-supplied narrative as a valid harness-executable `BlindJudgement`, and avoid implying that owner acceptance of the legacy adapter path has occurred?

**Adversarial verification pass outcome:** FM-D is present and produces two major findings (DFP-01, DFP-02) and two minor findings (DFP-03, DFP-04). FM-A and FM-B are not present — the pack correctly preserves blocked status and correctly absorbs all nine FA findings as work-still-required. FM-C is substantially absent (participant-facing body is clean), with a design concern in the YAML frontmatter captured under DFP-01. FM-E is not present — the adapter note correctly preserves non-comparability.

---

## 4. Source-Read Ledger

| Source | Why read | Status | Decision it supports |
|---|---|---|---|
| `AGENTS.md` | Project authority | Modified | Agent operating boundary; no-jb rule |
| `.agents/workflow-overlay/README.md` | Overlay entrypoint | Modified | Overlay wins for project facts |
| `.agents/workflow-overlay/source-of-truth.md` | Source hierarchy | Modified | Advisory findings boundary; strict claims not proven |
| `.agents/workflow-overlay/source-loading.md` | Source-loading budgets | Modified | Dirty-state allowance rule |
| `.agents/workflow-overlay/artifact-roles.md` | Research artifact and review report roles | Modified | Role permission for draft pack and this report |
| `.agents/workflow-overlay/review-lanes.md` | Adversarial review lane definition | Modified | Lane scope, severity labels, non-patch constraint |
| `.agents/workflow-overlay/prompt-orchestration.md` | Output mode and review prompt rules | Modified | review-report mode; YAML-only after durable write |
| `.agents/workflow-overlay/communication-style.md` | Courier YAML shape | Modified | review_summary shape |
| `.agents/workflow-overlay/validation-gates.md` | Zero-spoiler backtest gate | Modified | Leakage discipline; claim discipline |
| `.agents/workflow-overlay/retrieval-metadata.md` | Retrieval header contract | Clean | Header format check |
| `.agents/workflow-overlay/template-registry.md` | Template registry | Untracked | adversarial-artifact-review template binding |
| `.agents/workflow-overlay/product-proof.md` | Zero-spoiler backtest behavior, non-claims | Untracked | Zero-spoiler gate; non-claims discipline |
| `docs/prompts/templates/review/adversarial_artifact_review_v0.md` | Review template | Modified; hash verified | Template compliance |
| `fixture_admission_review_v0.md` | Prior review; FA-01 through FA-09 | Untracked; hash verified | FA finding set; what the authoring lane was asked to produce |
| `fixture_authoring_receipt_v0.md` | Primary draft pack target | Untracked; hash verified | Status, hard blockers, consumed-findings receipt |
| `participant_packet_draft_v0.md` | Primary draft pack target | Untracked; hash verified | Zero-spoiler check; YAML frontmatter schema check; use boundary |
| `evidence_registry_draft_v0.md` | Primary draft pack target | Untracked; hash verified | EvidenceUnit field correctness; CW-P7 exclusion; hash status |
| `facilitator_ledger_draft_v0.md` | Primary draft pack target | Untracked; hash verified | Pydantic vs protocol separation; band input validity; underreach_observability; freeze blockers |
| `blind_judgement_adapter_note_v0.md` | Primary draft pack target | Untracked; hash verified | Adapter non-comparability; ladder-level ambiguity; scoring blocker |
| `case_index.md` | Discovery pointer target | Untracked; hash verified | Narrowness; status accuracy |
| `harness/v0_14/index.md` | Discovery pointer target | Untracked; hash verified | Narrowness; non-authorization |
| `manifest_v0.md` | Discovery pointer target | Untracked; hash verified | Narrowness; Canoo/Walmart status accuracy |
| `source_packet_v0.md` | Case-folder source substrate | Untracked | CW-P7 exclusion check; EvidenceUnit source mapping |
| `participant_packet_v0.md` | Case-folder prior participant packet | Untracked | Participant-facing body comparison; source-manifest history |
| `blind_judgments_v0.md` | Case-folder blind judgment | Untracked | Adapter note accuracy; cleanliness caveat |
| `facilitator_ledger_v0.md` | Case-folder facilitator ledger | Untracked | Spoiler inventory completeness; outcome gap preservation |
| `outcome_calibration_v0.md` | Case-folder outcome calibration | Untracked | Underreach_observability rationale; split-axis learning preservation |
| `pydantic_schema_reference.md` | v0.14 Pydantic schema contracts | Untracked | EvidenceUnit, FacilitatorLedger, BlindJudgement, BandInputs field verification |
| `band_input_labeling_rubric.md` | v0.14 labeling rubric | Untracked | Band input enum validity; workflow requirements |
| `judgement_case_construction_protocol.md` | v0.14 case construction protocol | Untracked | Required fields; protocol vs Pydantic discrepancy |
| `blind_judgement_schema_and_harness_protocol.md` | v0.14 blind judgment protocol | Untracked | Adapter non-comparability; ladder-level mapping |
| `memorization_probe_protocol.md` | v0.14 probe protocol | Untracked | Probe requirement and blocking behavior |
| `action_band_mapping_table_numbers.md` | v0.14 numeric mapping constants | Untracked | Band floor calculation for underreach_observability rationale |
| `action_band_mapping_executable_spec.md` | v0.14 mapping spec | Untracked | Derivation function interface |
| `scorer_formula_spec.md` | v0.14 scorer formulas | Untracked | Underreach primary gate; evidence ID check specs |
| `failure_event_log_spec.md` | v0.14 failure event schema | Untracked | Failure event non-claim discipline |

**Dirty-state note:** All Orca overlay authority sources are modified. All reviewed draft pack artifacts, case-folder sources, and v0.14 harness spec files are untracked. Advisory findings proceed from visible artifact text. Strict claims about validation, readiness, acceptance, or source-of-truth status remain `not proven` because controlling sources are modified or untracked.

---

## 5. Findings

### DFP-01 — Case ID Contains Company Names in Participant Packet Frontmatter

**Priority:** Major
**Phase:** Correctness
**Location:** `participant_packet_draft_v0.md` — YAML frontmatter, `case_id` field

**Issue:** The `case_id: canoo_walmart_2022_v0_14` in the participant packet's YAML frontmatter directly names Canoo and Walmart. The v0.14 `judgement_case_construction_protocol.md` requires `case_id` in the participant packet frontmatter. If a harness runner passes the full participant packet file (including frontmatter) to a contestant, the `case_id` value immediately identifies the real-world companies, allowing the contestant to search for the actual agreement and later outcome before submitting a judgment.

This is separate from the source-manifest alias problem already documented as a blocking concern in the receipt and packet draft. The source-manifest conflict prevents URL and title leakage; the case_id problem allows company-identity leakage from the frontmatter field that the spec requires to be present.

**Evidence:**
- `participant_packet_draft_v0.md` frontmatter: `case_id: canoo_walmart_2022_v0_14`
- `judgement_case_construction_protocol.md` — Participant Packet Must Include: `case_id`
- `blind_judgement_schema_and_harness_protocol.md` — `blind_judgement` output requires `case_id`, implying the contestant receives or knows the case_id
- `memorization_probe_protocol.md` — probe input includes `public_identifiers_if_any` and `decision_question`; the probe is designed to handle known-fame risk, but it runs before the blind run; if the case_id is shown in the participant packet, the contestant already has the identifiers
- The receipt and participant packet draft acknowledge a source-manifest leakage conflict but do not separately flag the case_id as a leakage vector

**Impact:** If a later implementation or fixture-use lane passes the full YAML frontmatter to a blind contestant, the `canoo_walmart` string in the case_id immediately breaks anonymization and contaminates the blind judgment. The `PARTICIPANT_PACKET_DRAFT_NOT_BLIND_USE_READY` status partially mitigates this, but the design gap must be explicitly documented for a later fixture patch or implementation-scoping lane.

The `forbidden_information_notice` and the `use_boundary` that says to show only the participant-facing section provide partial mitigation, but neither solves the problem at the protocol level. A harness runner following the v0.14 spec literally (which requires `case_id` in frontmatter and uses it to link to the facilitator ledger) would expose company names to contestants.

**Minimum closure condition:** Before this fixture can be used for blind contestant runs, one of these must be true: (a) the v0.14 harness protocol defines a mechanism for using a non-identifying case ID in contestant-visible context (e.g., a run-scoped alias like `case_run_001`) while using the full `canoo_walmart_2022_v0_14` ID internally for ledger linking; or (b) the owner explicitly accepts a non-blind fixture mode where contestants are told the case identity in advance (and scoring is not claimed as blind). Neither path is currently accepted by an authorized Orca decision.

**Next authorized action:** Advisory finding. Owner decides whether to add a `contestant_visible_case_id` alias field to the participant packet design, require an abstracted run-wrapper, or accept non-blind fixture mode before any blind contestant run is authorized.

**Recommended direction:** Add a separate non-identifying `contestant_visible_case_id` field to the participant packet frontmatter design (e.g., `fleet_ev_commitment_2022_case_001`) that is distinct from the internal `case_id` used for ledger linking. Update the fixture spec to define when each is used. Do not execute this patch until an authorized fixture patch lane accepts it.

---

### DFP-02 — Multi-Source EvidenceUnit Pattern Not Defined in v0.14 Schema

**Priority:** Major
**Phase:** Correctness
**Location:** `evidence_registry_draft_v0.md` — CW-E02, CW-E04, CW-E05, CW-E06

**Issue:** Four of the six draft evidence units use compound source IDs and compound source aliases that do not conform to the v0.14 `EvidenceUnit` schema. The schema defines `source_id: str` (singular) and `source: str` (singular). The draft uses:
- CW-E02: `source_id: CW-P1_CW-P3`, `source: PARTICIPANT_SAFE_SOURCE_ALIAS_CW_P1_CW_P3_RAW_LOCATORS_WITHHELD`
- CW-E04: `source_id: CW-P4_CW-P5`, `source: PARTICIPANT_SAFE_SOURCE_ALIAS_CW_P4_CW_P5_RAW_LOCATORS_WITHHELD`
- CW-E05: `source_id: CW-P4_CW-P5_CW-P6`, `source: PARTICIPANT_SAFE_SOURCE_ALIAS_CW_P4_CW_P5_CW_P6_RAW_LOCATORS_WITHHELD`
- CW-E06: `source_id: CW-P4_CW-P5`, `source: PARTICIPANT_SAFE_SOURCE_ALIAS_CW_P4_CW_P5_RAW_LOCATORS_WITHHELD`

The v0.14 spec does not define a multi-source EvidenceUnit pattern. Each EvidenceUnit is expected to map to a single `source_id` and `source`. The compound ID approach is a workaround for evidence that synthesizes facts from multiple sources, but it would fail Pydantic validation if the schema enforces single-source semantics (e.g., by cross-referencing against a source registry).

**Evidence:**
- `pydantic_schema_reference.md` — `class EvidenceUnit(BaseModel): source_id: str; source: str` — both singular
- `judgement_case_construction_protocol.md` — `evidence_unit: source: [singular]; source_type: [singular]`
- The draft uses `TBD_SOURCE_BYTE_HASHES` (plural) for multi-source units, signaling that the hash model is also unresolved for compound-source evidence
- Only CW-E01 and CW-E03 have clean single-source mappings

**Impact:** A later implementation-scoping lane building the EvidenceUnit registry would encounter a schema gap: four of six evidence units need either splitting into per-source units or a spec extension for multi-source evidence. Without resolution, the scorer's `evidence_id_presence_pass` check cannot validate evidence citations cleanly, because the evidence IDs cited in a `BlindJudgement` (e.g., `CW-E04`) would need to resolve to a single source record, but the draft maps CW-E04 to two sources.

**Minimum closure condition:** Before the evidence registry can be frozen, either (a) each draft evidence unit must be split into per-source units (CW-E04a from CW-P4 and CW-E04b from CW-P5), which may change evidence ID assignments in the facilitator ledger and adapter note; or (b) the v0.14 spec must be extended to define a multi-source EvidenceUnit pattern with a compound-hash rule. Neither resolution is currently accepted.

**Next authorized action:** Advisory finding. Owner decides whether to split evidence units by source or to request a spec extension before the evidence registry freeze pass.

**Recommended direction:** Splitting evidence units by source is the simpler path and avoids spec changes. The facilitator ledger and adapter note would need corresponding evidence ID updates. Do not execute this change until an authorized fixture patch lane accepts it.

---

### DFP-03 — `committed_at: NOT_COMMITTED` Is Not a Valid ISO-8601 Timestamp

**Priority:** Minor
**Phase:** Correctness
**Location:** `facilitator_ledger_draft_v0.md` — Direct Pydantic FacilitatorLedger Draft Fields, `committed_at`

**Issue:** The `FacilitatorLedger` Pydantic schema requires `committed_at: str  # ISO-8601 UTC, Z suffix`. The draft sets `committed_at: NOT_COMMITTED`. This is not a valid ISO-8601 timestamp and would cause a Pydantic validation error if the ledger YAML is parsed against the schema.

**Evidence:**
- `pydantic_schema_reference.md` — `committed_at: str  # ISO-8601 UTC, Z suffix`
- `facilitator_ledger_draft_v0.md` — `committed_at: NOT_COMMITTED`

**Impact:** A later implementation-scoping or fixture-patch lane that attempts to validate the draft ledger YAML against the Pydantic schema would fail on `committed_at` schema validation. This is expected for a draft, but the failure should be explicit so the implementation lane knows the field needs a valid timestamp at freeze time, not just a content value.

The current `ledger_freeze_hash: NOT_COMPUTED` blocker is correctly stated, but `committed_at: NOT_COMMITTED` adds a separate schema-validity failure that would need to be resolved independently (a commit timestamp must be set at ledger freeze time, not just any ISO-8601 string).

**Minimum closure condition:** Before the ledger is frozen, `committed_at` must be set to a valid ISO-8601 UTC timestamp with Z suffix (e.g., `2026-06-01T00:00:00Z`) at the moment of ledger freeze.

**Next authorized action:** Advisory finding. Ledger freeze pass must assign a valid ISO-8601 timestamp. No immediate action required in the draft lane.

---

### DFP-04 — Protocol/Pydantic Schema Discrepancy for `case_family`, `decision_shape`, and `evidence_unit_ids` in `must_address_items` Is Unresolved and Not Surfaced as an Implementation Blocker

**Priority:** Minor
**Phase:** Friction
**Location:** `facilitator_ledger_draft_v0.md` — Protocol Fixture Metadata section; Must-Address Items table

**Issue:** Two discrepancies between the case construction protocol and the Pydantic schema reference are present but not explicitly surfaced as implementation blockers in the draft pack.

1. `case_family` and `decision_shape`: The `judgement_case_construction_protocol.md` includes these as required `facilitator_ledger` fields; the `pydantic_schema_reference.md` `FacilitatorLedger` class does not include them. The draft correctly classifies them as `CANDIDATE_PROTOCOL_METADATA` with status `NOT_DIRECT_PYDANTIC_FIELD`, but does not state that this discrepancy must be resolved before implementation can produce a schema-valid ledger.

2. `evidence_unit_ids` in `must_address_items`: The `judgement_case_construction_protocol.md` includes `evidence_unit_ids` in must_address_items; the `pydantic_schema_reference.md` `MustAddressItem` class has only `must_address_item_id: str` and `description: str`. The draft's must-address table includes evidence unit references (CW-E01, CW-E02, etc.) but the candidate items are `CANDIDATE_ONLY`, and the discrepancy is not named.

**Evidence:**
- `judgement_case_construction_protocol.md` — `facilitator_ledger: case_family: ...; decision_shape: ...`
- `pydantic_schema_reference.md` — `class FacilitatorLedger(BaseModel)` — no `case_family` or `decision_shape` fields
- `judgement_case_construction_protocol.md` — `must_address_items: - must_address_item_id: ...; description: ...; evidence_unit_ids: ...`
- `pydantic_schema_reference.md` — `class MustAddressItem(BaseModel): must_address_item_id: str; description: str` — no `evidence_unit_ids`
- `facilitator_ledger_draft_v0.md` — correctly separates but does not name the discrepancy as a blocker

**Impact:** A later implementation-scoping lane building from the draft ledger would encounter ambiguity about which fields belong in the schema-validated `FacilitatorLedger` object versus protocol-only metadata that lives in run configuration or adjacent artifacts. This could result in implementation code that silently drops `case_family` and `decision_shape`, or that includes them in the Pydantic object and fails validation, or that treats `evidence_unit_ids` in must_address_items as required when the Pydantic schema doesn't enforce it.

**Minimum closure condition:** Before implementation of the FacilitatorLedger schema, the spec discrepancy must be resolved: either update the Pydantic schema to include `case_family`, `decision_shape`, and `evidence_unit_ids` in the relevant objects, or document that these are protocol-only metadata fields that live outside the schema-validated ledger object. Resolution must be in an accepted harness spec update, not just in a local fixture.

**Next authorized action:** Advisory finding. Owner decides whether to resolve via a targeted v0.14 spec patch (adding fields to the Pydantic schema) or via a protocol-only metadata adapter. Resolution is required before harness implementation, not before fixture-patch review.

---

### DFP-05 — `underreach_observability` Rationale Lacks Evidence Unit ID Citations

**Priority:** Minor
**Phase:** Friction
**Location:** `facilitator_ledger_draft_v0.md` — Underreach Observability section; Direct Pydantic FacilitatorLedger Draft Fields

**Issue:** The `underreach_observability.present: false` declaration (required by FA-05) gives a rationale that references "option-value and opportunity-cost evidence" and "the reviewed record" without citing specific evidence unit IDs. The `judgement_case_construction_protocol.md` shows that `underreach_observability` can include `evidence_unit_ids`. The rationale is advisory-quality but not evidence-unit-anchored.

**Evidence:**
- `facilitator_ledger_draft_v0.md` — `underreach_observability: notes: > "The case has some option-value and opportunity-cost evidence, but the reviewed record does not establish a primary underreach failure."`
- `judgement_case_construction_protocol.md` — `underreach_observability: evidence_unit_ids:` (field shown as available)
- The Pydantic `UnderreachObservability` class does not include `evidence_unit_ids`, but the protocol schema does — which also reflects the DFP-04 discrepancy

**Impact:** Without specific evidence unit citations, the underreach_observability rationale is not source-bound at the same level as the evidence registry. A second-labeler or later fixture-patch reviewer would need to re-derive the rationale from the case evidence rather than being able to trace it to specific units. This is a friction issue for the second-label audit, not a correctness blocker.

**Minimum closure condition:** Before the ledger is frozen, the `underreach_observability` notes should identify which evidence units (CW-E03, CW-E05, CW-E06 are candidates given the alternative-supplier evidence, counterparty risk evidence, and launch burden evidence) support the `present: false` determination. The specific units supporting "no primary underreach failure" vs. "some option-value and opportunity-cost pressure" should be named.

**Next authorized action:** Advisory finding. Ledger freeze pass should add evidence unit IDs to the underreach_observability record. No immediate action required in the draft lane.

---

## 6. Non-Findings

The following were reviewed adversarially and found not to create defects in the draft fixture pack.

**`DRAFT_FIXTURE_PACK_BLOCKED_BEFORE_SCORING` status preserved:** All five artifacts consistently carry the blocked status. The receipt uses `DRAFT_FIXTURE_PACK_BLOCKED_BEFORE_SCORING`; the participant packet draft uses `PARTICIPANT_PACKET_DRAFT_NOT_BLIND_USE_READY`; the evidence registry uses `EVIDENCE_REGISTRY_DRAFT_NOT_FROZEN`; the facilitator ledger uses `FACILITATOR_LEDGER_DRAFT_NOT_FROZEN`; the adapter note uses `BLIND_JUDGEMENT_ADAPTER_NOTE_ONLY`. No artifact implies readiness, admission, or scoreability. Non-finding confirmed.

**FA-01 through FA-09 consumed without silent conversion:** All nine admission-review findings are present in the consumed_findings receipt and are reflected as still-open work in the hard blockers list. FA-01 (BlindJudgement schema): adapter note correctly says `clean_for_scoring: false` and `Harness-executable BlindJudgement created: no`. FA-02 (FacilitatorLedger format): ledger correctly says `frozen_band_inputs: NOT_FROZEN` and `ledger_freeze_hash: NOT_COMPUTED`. FA-03 (participant packet frontmatter): frontmatter is drafted but `participant_packet_hash: NOT_COMPUTED`. FA-04 (EvidenceUnit registry): registry exists as a draft, not frozen, with `registry_freeze_hash: NOT_COMPUTED`. FA-05 (underreach_observability): `present: false` declared as candidate. FA-06 (cleanliness): `strict_cleanliness_claim: user_supplied_not_independently_verified` preserved throughout. FA-07 (outcome gaps): spoiler inventory and leakage audit notes preserve the gaps. FA-08 (rubric use): receipt method_sequence records `band_input_labeling_rubric_read_before_ledger_draft: yes`. FA-09 (pricing-cap): acknowledged as not used as decisive scoring evidence. Non-finding confirmed.

**Participant-facing body is clean:** The section between `Participant-Facing Packet Starts` and `Participant-Facing Packet Ends` in the participant packet draft contains no company names (Canoo, Walmart), no source URLs, no source titles, no source filenames, no actual agreement terms (4,500 vehicles, warrants, termination rights), no post-cutoff outcome facts (Chapter 7), no reveal readout content, no outcome calibration content, no candidate band inputs, no must-address items, and no scoring hints. The wording closely matches the clean participant packet from `cases/canoo-walmart/participant_packet_v0.md`, with appropriate additions for the v0.14 role frame and frontmatter. Non-finding confirmed.

**CW-P7 correctly excluded:** The evidence registry excludes CW-P7 with documented reason ("Optional independent media coverage carries source-title and identifier priming risk from the source-packet safety review"). Core financial-risk facts traceable to CW-P4, CW-P5, or CW-P6 are included; facts traceable only to CW-P7 are not. The participant packet draft does not reference CW-P7. Non-finding confirmed.

**All 14 band input values are valid v0.14 enum values:** Every candidate value in the band inputs review table maps to a valid literal in the v0.14 `BandInputs` schema:
- `evidence_strength: moderate` ✓ (none/weak/moderate/strong)
- `evidence_independence: partially_independent` ✓ (correlated/partially_independent/independent)
- `reversibility_feasibility: medium` ✓ (low/medium/high)
- `reversibility_cost: high` ✓ (low/medium/high/ruinous)
- `authority: partial` ✓ (absent/partial/full)
- `authority_acquisition_cost: medium` ✓ (low/medium/high/impossible)
- `capability: partial` ✓ (absent/partial/full)
- `capability_build_cost: high` ✓ (low/medium/high/impossible)
- `loss_shape: asymmetric_down` ✓ (symmetric/asymmetric_down/ruinous_tail/unknown)
- `opportunity_cost: moderate` ✓ (none/low/moderate/severe)
- `information_decay: slow` ✓ (none/slow/fast/expiring)
- `option_value: moderate` ✓ (none/low/moderate/high)
- `upside_shape: asymmetric_up` ✓ (none/symmetric/asymmetric_up/convex/once_only_window)
- `urgency: low` ✓ (none/low/medium/critical)

All 14 are valid. All are marked `CANDIDATE_UNFROZEN`. Non-finding confirmed.

**`underreach_observability.present: false` complies with the Pydantic schema:** The `UnderreachObservability` model has `present: bool`, `basis: Optional[Literal[...]] = None`, `notes: Optional[str] = None`. With `present: false`, `basis: null` is a valid `None` value for the Optional field. Non-finding confirmed (the rationale quality is flagged separately as DFP-05).

**Adapter note preserves ladder-level ambiguity and non-scoreable status:** The adapter note states `ladder_level_candidate_primary: 4` and `ladder_level_candidate_alternate: 3` and explicitly says "This split must be resolved before any scoring." The mapping is inside a `candidate_blind_judgement_mapping` block explicitly labeled "a review aid only. It must not be treated as a schema-valid BlindJudgement." `clean_for_scoring: false` is set. Non-finding confirmed.

**Discovery pointers are narrow and non-authorizing:**
- `case_index.md` says "Docs-only v0.14 fixture-authoring pack; blocked before scoring" and explicitly says "Do not infer that a scoreable fixture, clean harness-format model run, v0.14 scoring admission, or product-proof artifact exists." Non-finding confirmed.
- `harness/v0_14/index.md` says "Draft fixture pack; blocked before scoring; does not authorize implementation, probe execution, model runs, validation, scoring, proof, product proof, or lesson promotion." Non-finding confirmed.
- `manifest_v0.md` says "Draft docs-only fixture pack; blocked before scoring and not probe-safe, blind-run-clean, or score-ready." Non-finding confirmed.

**Pydantic vs protocol field separation is correctly implemented:** The draft ledger clearly separates "Direct Pydantic FacilitatorLedger Draft Fields" from "Protocol Fixture Metadata." `case_family`, `decision_shape`, `memorization_probe_required`, and `known_fame_risk` are in the protocol section with status flags (`CANDIDATE_PROTOCOL_METADATA`, `PROTOCOL_LEAKAGE_INPUT_NOT_DIRECT_PYDANTIC_FIELD`). The spec discrepancy is present but not a violation by the draft. Non-finding confirmed (the spec discrepancy is flagged separately as DFP-04).

**Source-manifest conflict is treated as a blocker, not a completed solution:** The receipt explicitly states: "Raw v0.14 source-manifest fields are a current conflict for this anonymized case because raw URLs and titles would identify the retailer, supplier, and decision. A later packet-authoring pass must choose either a participant-safe source-manifest adapter or an explicit non-blind fixture mode before blind contestant use." The participant packet draft uses `PARTICIPANT_SAFE_SOURCE_ALIAS_CW_P1_RAW_LOCATOR_WITHHELD` as a placeholder, not as a completed schema value. Non-finding confirmed.

**Walmart-specific outcome gaps preserved:** The leakage audit notes and spoiler inventory correctly list: deployment volume, accepted units, route performance, uptime, termination-right exercise, financial exposure at bankruptcy, and protective-term effectiveness as not established. The facilitator ledger draft references these gaps from the narrative facilitator ledger. Non-finding confirmed.

**No implementation, runtime, model run, probe execution, scoring, or proof authorization implied:** Every artifact and every cross-reference in the receipt explicitly states: "not authorized." Non-finding confirmed.

**Candidate must-address items are facilitator-only and not in participant-facing body:** MA-CW-01 through MA-CW-05 appear only in the facilitator ledger draft and the adapter note's `must_address_items_covered_candidate` section. The participant packet body does not contain any must-address items or hints. Non-finding confirmed.

**EvidenceUnit `pre_decision_status` values are justified by source dates:**
- CW-P1 (2022-01-05), CW-P2 (2022-01-05), CW-P3 (2022-06-08), CW-P4 (2022-02-28), CW-P5 (2022-05-10), CW-P6 (2022-05-10) — all precede the July 2022 cutoff. `verified_pre_decision` is the correct label for all. Non-finding confirmed.

---

## 7. Strict-Only Blockers and Not-Proven Boundaries

- Whether the v0.14 case construction protocol and Pydantic schema can be reconciled without breaking the deterministic scoring guarantee: `not proven` — the DFP-04 discrepancy exists in the imported spec; this review did not change the spec.
- Whether a `contestant_visible_case_id` alias mechanism is compatible with the v0.14 harness protocol without breaking ledger linkage: `not proven` — no accepted spec extension exists.
- Whether splitting compound-source EvidenceUnits (CW-E02, CW-E04, CW-E05, CW-E06) would change any candidate band input label: `not proven` — splitting would produce more granular evidence IDs but should not change the evidence summaries; the band input label analysis used evidence-level content, not source-level atomicity.
- Whether the `band_input_labeling_rubric.md` rubric definitions, when applied by a second labeler, would disagree with more than three of the 14 candidate inputs: `not proven` — the rubric was read and used for the draft, but no second-label audit has been performed.
- Strict validation, readiness, acceptance, source-of-truth status, or fixture admission for the draft pack: `not proven` — controlling overlay sources are modified or untracked; all advisory findings only.
- Whether the memorization probe would pass for any specific model family given the `known_fame_risk: unresolved_moderate_to_elevated` flag: `not proven` — no probe has been run.

---

## 8. Review-Use Boundary

This is a read-only review. Findings, non-findings, and not-proven boundaries are decision input only.

They are not approval, validation, mandatory remediation, patch authority, product proof, fixture admission, probe pass, score-readiness, implementation authorization, lesson promotion, or lifecycle completion.

The `accept_with_friction` recommendation below is a reviewer recommendation under the commission and criteria defined in this review. It does not grant patch authority, implementation permission, fixture readiness, or execution authorization. A separately authorized owner-decision or fixture-patch lane must accept findings before any patch is executed.

**Required boundary: plumbing works only; not judgment quality.**

---

## 9. Next Authorized Step

The draft fixture pack correctly executes the admitted fixture-authoring move. The two major findings (DFP-01, DFP-02) identify real schema and design issues that must be resolved before blind use or implementation, but neither prevents the pack from serving its current purpose: documenting fixture-authoring surfaces, preserving blocked-before-scoring status, and providing a bounded basis for later patching.

**Recommended next step:** Owner reviews findings DFP-01 and DFP-02 and decides whether to authorize a fixture-patch lane to address them. DFP-01 (case_id company names) requires a protocol-level decision about contestant-visible identifiers. DFP-02 (multi-source EvidenceUnit) requires a decision between splitting units or extending the spec.

Minor findings DFP-03, DFP-04, and DFP-05 can be addressed during the ledger freeze pass without a separate patch authorization.

The next authorized step is NOT: implementation, probe execution, model runs, scoring, validation, proof-run, product-proof, or lesson promotion.

---

## Findings Summary

| ID | Priority | Phase | Location | One-line summary |
|---|---|---|---|---|
| DFP-01 | Major | Correctness | `participant_packet_draft_v0.md` — `case_id` frontmatter field | `case_id: canoo_walmart_2022_v0_14` contains company names; identity leakage if full frontmatter shown to contestants. |
| DFP-02 | Major | Correctness | `evidence_registry_draft_v0.md` — CW-E02, CW-E04, CW-E05, CW-E06 | Compound source IDs (`CW-P1_CW-P3`, etc.) not defined in v0.14 EvidenceUnit schema; will require splitting or spec extension. |
| DFP-03 | Minor | Correctness | `facilitator_ledger_draft_v0.md` — `committed_at` | `NOT_COMMITTED` is not a valid ISO-8601 UTC timestamp; would fail Pydantic validation at freeze time. |
| DFP-04 | Minor | Friction | `facilitator_ledger_draft_v0.md` — protocol metadata / must_address_items | `case_family`, `decision_shape`, `evidence_unit_ids` in must_address_items: protocol/Pydantic discrepancy unresolved and not flagged as implementation blocker. |
| DFP-05 | Minor | Friction | `facilitator_ledger_draft_v0.md` — `underreach_observability` | Rationale cites "reviewed record" without naming specific evidence unit IDs; gap for second-label audit. |

**Blocking findings (per severity label authority):** None. Severity labels are finding-priority labels only; they do not create approval, rejection, readiness, validation, or mandatory remediation authority.
**Advisory findings:** DFP-01 through DFP-05.
**Prior findings remediated:** FA-01 through FA-09 (admission review findings) are correctly consumed as still-open work items, not resolved.
