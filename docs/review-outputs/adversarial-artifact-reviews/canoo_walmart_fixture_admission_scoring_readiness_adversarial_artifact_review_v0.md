# Canoo/Walmart Fixture-Admission Scoring-Readiness Adversarial Artifact Review v0

```yaml
retrieval_header_version: 1
artifact_role: Review report
scope: Adversarial fixture-admission and scoring-readiness review for the Canoo/Walmart case track against the v0.14 Judgment Harness spec.
use_when:
  - Deciding whether the Canoo/Walmart case should proceed to v0.14 fixture authoring, remain qualitative-only, or block on a targeted source gap.
  - Checking the structural gap between existing narrative case artifacts and v0.14 harness schema requirements before fixture work begins.
authority_boundary: retrieval_only
input_hashes:
  case_index.md: D32B41BCF15B9DF879FE40CE91B87859E7AE679F662278A6B19FF4A407B53906
  participant_packet_v0.md: E0191512B1A5AD292C023304321B6FD870B4C1CF591DDFF8708ACC69D5B3324F
  blind_judgments_v0.md: 2DF41433DCFACB31832CD51E65EC424888B7EB8955115D6949A35E8C7F2E8225
  owner_context_judgments_v0.md: A12BDC0416FC41502AB0B46B70338FF40FF118008D5D808C5E91BDD265E3B2E8
  pre_reveal_judgment_comparison_v0.md: 2AD850D94A29438D54491AA5EE72D8D79332E04F6C78E03BF960CF28BEEAEE80
  facilitator_ledger_v0.md: 6356C45D8E9B75732DB3D146EABFFCE4AD2775BCDD23D0205E26A46222FCE739
  reveal_readout_v0.md: 927DB2F16D3D9DF9EBB9DF20F6A35F00659C7C671EEC8ADAF4104BD7535C3A7E
  outcome_calibration_v0.md: 8E5766B11F80D716ACFB376E8227A9C610BBB906949AF65C9C1791A070C0A2F0
  calibration_gate_adversarial_review_v0.md: 31362147A8557C0698A23A9D902AA5FFC71D8B973813F89DF9157D38ED0980EE
  harness_v0_14_index.md: 7038B2443E9EC96723A98359899A8975E0E42A5B45E8DFFD886EE393E3445C4F
  action_band_mapping_table_numbers.md: E6CFDF0ABCB529E93A2B9D933EBC3BA1A43B7D9DC915AC52E742815722442374
  action_band_mapping_executable_spec.md: EEB90B6B5C5F8279AF0CA5F582F5E72BEDB3071779CCE32F8539638D2E22D018
  scorer_formula_spec.md: 99FDC48F5C537D2E8AD28CEA8AC5CC20964D18130E19D4C9816AC075208CD8E3
  pydantic_schema_reference.md: CFFC7BCAC179B752B9A77204ECA6A6399D30DD7CB6B2C52533E3EC0FDC031D8D
stale_if:
  - Any input hash changes.
  - v0.14 harness spec is superseded by a later version.
  - New public evidence establishes Walmart vehicle acceptance volume, termination-right exercise, or financial exposure at Canoo's bankruptcy.
  - A fixture authoring receipt is created that supersedes this admission gate.
```

---

## Start Preflight

```yaml
orca_start_preflight:
  agents_read: yes
  overlay_read: yes
  source_pack: >
    S0 overlay plus S4 explicitly named case artifacts, v0.14 harness spec files,
    and prior calibration-gate adversarial review. No bulk folder reads. No web
    research. No TR/Casetext material. No Reddit/attention-lens material.
  edit_permission: read-only for all reviewed artifacts; docs-write for this report only
  target_scope: >
    Fixture-admission and scoring-readiness review for Canoo/Walmart against
    v0.14 harness spec. Return exactly one verdict: admit_to_fixture_authoring,
    keep_qualitative_only, or block_for_source_gap.
  dirty_state_checked: yes
  blocked_if_missing: no
```

**Workspace:** `C:\Users\vmon7\Desktop\projects\orca`  
**Branch / HEAD:** `main` / `a2aebdd` (expected HEAD verified exact match)  
**Review lane:** Adversarial artifact review  
**Output mode:** `review-report` / `filesystem-output`  
**Edit permission:** Read-only for reviewed artifacts; docs-write for this report only  
**Patch queue:** Not authorized in this lane  

**Hash verification:** All 14 pinned hashes verified against filesystem. No mismatch.  

**Dirty-state note:** All Orca overlay authority sources are modified (uncommitted) per workspace git status. All case and harness target artifacts are untracked. Advisory review findings may proceed from visible artifact text; strict claims about validation, readiness, or source-of-truth status remain `not proven` because controlling sources are modified or untracked. The untracked state of case artifacts is treated as claim-discipline context, not readiness proof.

---

## Authority and Source Bindings

**Authority read sources:**
- `AGENTS.md` — project authority boundaries; modified
- `.agents/workflow-overlay/README.md` — overlay entrypoint and binding rule; modified
- `.agents/workflow-overlay/source-of-truth.md` — source hierarchy and doctrine propagation contract; modified
- `.agents/workflow-overlay/source-loading.md` — source-loading budgets and dirty-state note; modified
- `.agents/workflow-overlay/artifact-roles.md` — research artifact and review report role bindings; modified
- `.agents/workflow-overlay/review-lanes.md` — adversarial artifact review lane definition; modified
- `.agents/workflow-overlay/prompt-orchestration.md` — output mode and review prompt rules; modified
- `.agents/workflow-overlay/communication-style.md` — courier YAML shape; modified
- `.agents/workflow-overlay/validation-gates.md` — zero-spoiler gate, product proof gates; modified
- `.agents/workflow-overlay/product-proof.md` — zero-spoiler backtest behavior and non-claims; untracked

**Case read sources (all untracked):**
- `docs/research/judgment-spine/cases/canoo-walmart/case_index.md`
- `docs/research/judgment-spine/cases/canoo-walmart/participant_packet_v0.md`
- `docs/research/judgment-spine/cases/canoo-walmart/blind_judgments_v0.md`
- `docs/research/judgment-spine/cases/canoo-walmart/owner_context_judgments_v0.md`
- `docs/research/judgment-spine/cases/canoo-walmart/pre_reveal_judgment_comparison_v0.md`
- `docs/research/judgment-spine/cases/canoo-walmart/facilitator_ledger_v0.md`
- `docs/research/judgment-spine/cases/canoo-walmart/reveal_readout_v0.md`
- `docs/research/judgment-spine/cases/canoo-walmart/outcome_calibration_v0.md`
- `docs/review-outputs/adversarial-artifact-reviews/canoo_walmart_reveal_readout_calibration_gate_adversarial_artifact_review_v0.md`

**Harness read sources (all untracked):**
- `docs/research/judgment-spine/harness/v0_14/index.md`
- `docs/research/judgment-spine/harness/v0_14/action_band_mapping_table_numbers.md`
- `docs/research/judgment-spine/harness/v0_14/action_band_mapping_executable_spec.md`
- `docs/research/judgment-spine/harness/v0_14/scorer_formula_spec.md`
- `docs/research/judgment-spine/harness/v0_14/pydantic_schema_reference.md`

**Sources available, not read (not decision-bearing for this admission question):**
- `docs/research/judgment-spine/harness/v0_14/band_input_labeling_rubric.md` — advisory gap; not in required reads; see FA-08 below
- `docs/research/judgment-spine/harness/v0_14/judgement_case_construction_protocol.md` — advisory gap
- `docs/research/judgment-spine/cases/canoo-walmart/case_track_preflight_v0.md` — not required; case_index summarizes
- `docs/research/judgment-spine/harness/v0_14/case_to_v0_14_bridge_foundation_v0.md` — advisory gap; see not-proven boundary below

---

## Method Sequence Record

```yaml
method_sequence:
  reference_load_workflow_deep_thinking: applied_as_failure_mode_framing_before_source_loading
  reference_load_workflow_adversarial_artifact_review: applied_as_review_methodology
  source_load: completed_all_required_reads
  hash_verification: all_14_hashes_verified_exact_match
  source_context_status: SOURCE_CONTEXT_READY
  apply_deep_thinking: framed_6_admissibility_failure_modes_below
  apply_adversarial_artifact_review: applied_to_loaded_source_context
```

---

## Fixture-Admission Verdict

```yaml
fixture_admission_verdict: admit_to_fixture_authoring
```

**Decisive reason:** The Canoo/Walmart case is bandable, the input path was sealed before reveal, the established outcome evidence is sufficient for honest band labeling from pre-decision evidence, and the missing outcome evidence (Walmart deployment volume, termination-right exercise, financial exposure at bankruptcy) can be represented as `not_established` annotations inside the fixture without creating artificial scoring. The scoring fairness tension — that the v0.14 band floor mechanics will place the owner-assisted no-proceed posture under-band — is manageable within v0.14's own structure via `underreach_observability.present: false`, which converts that under-band result from a primary failure to an advisory finding and preserves split-axis learning.

The structural deficits identified in findings FA-01 through FA-05 are not missing evidence. They are the artifact-authoring work that fixture authoring means: converting existing narrative case artifacts into v0.14 schema-format objects. These deficits do not prevent admission; they constitute the fixture authoring program.

---

## Deep-Thinking: Admissibility Failure Mode Frame

Six failure modes were framed before findings were listed. This framing governed the adversarial verification pass.

**FM-1: Input path contamination** — Was the blind judgment captured before any reveal, agreement, or outcome material was shown? A contaminated blind judgment would make scoring meaningless because the contestant's answer would reflect knowledge of the outcome.

**FM-2: False-binary bandability** — Do the decision options in the participant packet map to the action ladder in a way that forces a single obviously correct answer, or do they allow meaningful spread across the band? A false binary makes the scoring a trivial test rather than a judgment evaluation.

**FM-3: Scoring asymmetry / hidden winner selection** — Do the v0.14 band mechanics, when applied honestly to the pre-decision evidence, produce a band that systematically favors one judgment posture regardless of the case's split-axis learning? If the mechanics create a hidden winner before the fixture author declares one, the case's learning value is undermined.

**FM-4: Outcome evidence insufficiency** — Are the missing post-decision evidence items (Walmart operational outcomes, financial exposure, termination-right exercise) material enough to make band labeling speculative, or can honest band inputs be derived from the pre-decision evidence without them?

**FM-5: Harness schema gap** — Do the existing narrative case artifacts contain the structural elements (frontmatter, evidence registries, frozen enum inputs, harness-format judgment records) required for the v0.14 harness to execute? Gaps here are fixture authoring requirements, not evidence gaps.

**FM-6: Reproducibility gap** — Could a second scorer apply the same admission logic without relying on intuition, informal calibration, or outcome knowledge? Reproducibility depends on frozen inputs and a transparent band derivation, not on interpretive prose.

The adversarial verification pass found: FM-3 and FM-5 are materially present and produce findings. FM-1 is present with cleanliness caveats that remain unverified. FM-4 is present as an advisory gap that does not block admission. FM-2 is absent (bandability is confirmed). FM-6 is achievable with frozen inputs.

---

## Findings (Ordered by Severity)

### FA-01 — Blind Judgment Not in Harness-Executable Format

**Severity:** Critical  
**Location:** `docs/research/judgment-spine/cases/canoo-walmart/blind_judgments_v0.md` — full artifact  
**Issue:** The artifact captures a user-pasted narrative judgment from "a separate blind LLM thread." It is not a v0.14 `BlindJudgement` schema object. It lacks every required harness field.  
**Evidence:** The v0.14 `BlindJudgement` schema (pydantic_schema_reference.md) requires: `case_id`, `contestant_id`, `run_id`, `model_id`, `model_family`, `prompt_hash`, `temperature`, `seed_if_supported`, `harness_version`, `judgement_class` (one of `recommend/abstain/wait/escalate/irreducible_uncertainty`), `decision_shape`, `recommended_action` with `ladder_level` (integer 0–8), `evidence_used` with `claim_role` and `evidence_unit_ids`, and `must_address_items_covered`. The current artifact has none of these fields. It has a narrative recommendation ("Hybrid: create an option-heavy staged conditional commitment, beginning with a narrow operational pilot") but no `ladder_level` integer and no `evidence_unit_ids`.  
**Impact:** The v0.14 harness scorer cannot operate on the current artifact. `ScoringResult` requires `blind_judgement_hash` pointing to a valid `BlindJudgement` object. The evidence ID checks (`evidence_id_presence_pass`, `load_bearing_claim_citation_pass`, `must_address_coverage_pass`) would fail immediately against an artifact with no evidence registry bindings.  
**Minimum closure condition:** A valid v0.14 `BlindJudgement` object must exist for at least one contestant for this case before fixture scoring can proceed. The existing narrative judgment may inform the expected reasoning but is not a substitute for a harness-format record.  
**Next authorized action:** Fixture authoring work item. The narrative judgment artifact is not patched by this review. Owner decides whether to produce a new harness-run judgment by running the v0.14 participant packet through the harness protocol, or to retain the current artifact as qualitative context only and begin fresh with a harness-format run.

---

### FA-02 — Facilitator Ledger Not in v0.14 FacilitatorLedger Schema Format

**Severity:** Critical  
**Location:** `docs/research/judgment-spine/cases/canoo-walmart/facilitator_ledger_v0.md` — full artifact  
**Issue:** The artifact is a narrative research ledger recording public action, agreement terms, and outcome context. It does not contain the v0.14 `FacilitatorLedger` schema fields required to drive the harness scorer.  
**Evidence:** The v0.14 `FacilitatorLedger` schema (pydantic_schema_reference.md) requires: `case_id`, `batch_id`, `labeling_rubric_version`, `mapping_table_version_pin: "v0_14_mvp"`, `frozen_band_inputs` (all 14 `BandInputs` enum fields), `must_address_items` (list of `MustAddressItem`), `underreach_observability` (with `present: bool`), `committed_at` (ISO-8601 UTC), and `ledger_freeze_hash` (SHA256 of canonical YAML dump). The current narrative ledger has none of these fields. It has a rich source ledger, agreement terms, and outcome context, but no frozen enum inputs, no labeling rubric version pin, and no harness-format hash.  
**Impact:** The v0.14 scorer requires `facilitator_ledger_hash` in `ScoringResult`. The `derive_action_band` function requires `BandInputs` from the frozen facilitator ledger. The mapping version mismatch check (`ledger.mapping_table_version_pin != MAPPING_TABLE_VERSION`) would fail immediately. No harness scoring can proceed without a v0.14-format facilitator ledger.  
**Minimum closure condition:** A valid v0.14 `FacilitatorLedger` object with all required fields, authored using `band_input_labeling_rubric.md`, must exist before fixture scoring can proceed. The narrative ledger remains authoritative for source provenance and agreement term text; it is the input to the labeling process, not a substitute for the labeling output.  
**Next authorized action:** Fixture authoring work item. The existing narrative ledger is read-only in this review. Owner decides whether to commission a v0.14 facilitator ledger labeling pass using the existing narrative ledger as the source substrate.

---

### FA-03 — Participant Packet Lacks v0.14 YAML Frontmatter

**Severity:** Critical  
**Location:** `docs/research/judgment-spine/cases/canoo-walmart/participant_packet_v0.md` — document header  
**Issue:** The v0.14 pydantic schema requires participant packets to begin with YAML frontmatter containing harness-required fields. The current packet has an internal handling receipt but not the harness-required frontmatter structure.  
**Evidence:** The v0.14 pydantic_schema_reference.md specifies that `participant_packet.md` must begin with YAML frontmatter including `case_id`, `decision_question`, `decision_date_or_cutoff`, `role_frame`, `authority_constraints`, `capability_constraints`, `permitted_assumptions`, `forbidden_information_notice`, and `source_manifest` with per-source entries containing `source_id`, `source`, `retrieval_timestamp`, and `hash`. The current packet begins with a retrieval header followed by an `orca_start_preflight` receipt. There is no `case_id` field, no `decision_date_or_cutoff`, no `authority_constraints`, no `capability_constraints`, no `permitted_assumptions`, no `forbidden_information_notice`, and no `source_manifest` with evidence unit IDs.  
**Impact:** A harness runner producing a `BlindJudgement` must reference `participant_packet_hash`, which ties the judgment to a specific packet version. More critically, the `source_manifest` in the frontmatter drives `evidence_unit_ids` population in the judgment. Without the frontmatter, the evidence registry cannot be constructed from the packet alone, and the `evidence_id_presence_pass` check in the scorer would have no reference registry to validate against.  
**Minimum closure condition:** The participant packet must be extended with the required YAML frontmatter, or a new harness-format participant packet must be authored from the existing clean pre-cutoff content. The frontmatter addition must preserve zero-spoiler integrity (no post-cutoff facts, no outcome material, no actual action details).  
**Next authorized action:** Fixture authoring work item. The existing packet content is read-only in this review. The frontmatter can be added without changing the participant-facing body section, but must be treated as a version bump requiring a new hash.

---

### FA-04 — Evidence Registry (EvidenceUnit Objects) Does Not Exist

**Severity:** Critical  
**Location:** Case track folder — no evidence registry artifact exists  
**Issue:** The v0.14 harness scoring requires `evidence_unit_ids` in `BlindJudgement.evidence_used` referencing a case evidence registry of `EvidenceUnit` objects. No such registry exists for the Canoo/Walmart case track.  
**Evidence:** The v0.14 `EvidenceUnit` schema requires `evidence_id`, `source_id`, `source`, `timestamp`, `retrieval_timestamp`, `hash`, `pre_decision_status` (one of `verified_pre_decision / uncertain_timestamp / excluded`), `pre_decision_basis`, and `summary`. The scorer's `evidence_id_presence_pass` check fails if any `evidence_unit_id` cited in the blind judgment is missing from the case evidence registry. The `pre_decision_status_pass` check fails if any cited evidence has `pre_decision_status: excluded`. The `load_bearing_claim_citation_pass` check fails if a `load_bearing` claim has no `evidence_unit_ids`. The current case track has a narrative source packet (`source_packet_v0.md`, not read in this review but listed in case_index) and a narrative participant packet, but no structured `EvidenceUnit` registry.  
**Impact:** Without an evidence registry, neither the `evidence_id_presence_pass` check nor the `load_bearing_claim_citation_pass` check can be run. These are Phase 1 scoring checks, not optional. A blind judgment produced without evidence unit references would fail the scorer's evidence ID checks.  
**Minimum closure condition:** An evidence registry of `EvidenceUnit` objects must be constructed from the existing source packet and participant packet content, with each unit assigned `pre_decision_status: verified_pre_decision` or `uncertain_timestamp` based on sourcing, before the harness scorer can execute.  
**Next authorized action:** Fixture authoring work item. Owner decides whether to construct the evidence registry as part of the v0.14 participant packet frontmatter (source_manifest) or as a separate registry artifact. Zero-spoiler rules apply: the evidence registry must not include post-cutoff sources, actual-action records, or outcome evidence.

---

### FA-05 — Scoring Fairness Tension: Band Floor Mechanics Will Place No-Proceed Under-Band

**Severity:** Major  
**Location:** Structural — interaction between pre-decision evidence labels and v0.14 floor mechanics  
**Issue:** Honest pre-decision labeling of this case will produce action pressure floors that prevent the owner-assisted no-proceed posture (action ladder level 0–1) from being within the band, creating a systematic scoring asymmetry between the two judgment lanes even though the outcome calibration established split-axis learning with no single winner.  
**Evidence:** The v0.14 band floor mechanics work as follows. Floor pressures from `opportunity_cost`, `information_decay`, `option_value`, `upside_shape`, and `urgency` are taken as the maximum; then floor dampeners from `evidence_strength`, `loss_shape`, `authority`, and `capability` cap the floor downward. For this case: (a) `option_value` is at least `moderate` (the target supplier offered a differentiated EV platform and first-mover fleet option value — the participant packet explicitly discusses this); under the table, `option_value: moderate` contributes a floor of 3. (b) `opportunity_cost` is at least `low` to `moderate` given the retailer's scaling home-delivery service and competitors already moving on EV fleet reservations. Under the table, `opportunity_cost: moderate` contributes a floor of 3. Even with a `loss_shape: ruinous_tail` dampener (floor_cap = 3), the dampened_floor is `min(3, 3) = 3`. "Hold" (level 0) or "watch" (level 1) would be under-band regardless of other inputs. The owner-assisted judgment, which recommended not proceeding and monitoring external signals, maps to approximately level 0–1. The blind LLM judgment, which recommended a narrow pilot plus option structure, maps to approximately level 3–4 (test/option) and would be in-band. The reveal readout and outcome calibration both establish that the owner-assisted no-proceed posture was directionally aligned with Canoo's terminal counterparty outcome, and that the case is `split_axis_learning` with `single_winner: no`.  
**Impact:** If not managed explicitly, the v0.14 scorer would produce `under_band: true` and `underreach_primary: true` for the owner-assisted posture if `underreach_observability.present: true` in the facilitator ledger, which would score it as a primary failure even though the outcome calibration established its value. This would constitute hidden winner selection — the blind LLM's approach would be scored as in-band and the owner-assisted approach as a primary failure, baked into the band mechanics without the fixture author explicitly declaring that choice.  
**Minimum closure condition:** The v0.14 facilitator ledger for this case must declare `underreach_observability.present: false` with a documented basis, converting any under-band results to advisory (non-primary) findings. The fixture authoring notes must explicitly state that the case's split-axis learning requires treating under-band results as advisory, not primary failures, and must document the reasoning that honest band labeling yields a floor ≥ 3 while the case's calibrated learning includes the no-proceed posture as a valid alternative. This is not a falsification of band inputs; it is the correct use of the `underreach_observability` field for a case where the observability of underreach harm is not established.  
**Next authorized action:** Fixture authoring design decision. The facilitator ledger author must address this before the ledger is frozen. Owner decides whether this constraint is acceptable for fixture admission or whether it changes the admission verdict. This review's verdict is that it is acceptable and manageable, not that it is resolved.

---

### FA-06 — Blind Judgment Cleanliness Not Independently Verified

**Severity:** Major  
**Location:** `docs/research/judgment-spine/cases/canoo-walmart/blind_judgments_v0.md` — capture receipt  
**Issue:** The blind LLM judgment is `user_supplied_not_independently_verified`. The separation between the blind judgment thread and any reveal, outcome, or agreement material cannot be confirmed from the artifact alone.  
**Evidence:** The capture receipt states: `capture_method: user_pasted_from_separate_blind_llm_thread`, `exposure_declaration_user_supplied: no_reveal_seen`, `strict_cleanliness_claim: user_supplied_not_independently_verified`. There is no harness-generated `run_id`, no `prompt_hash`, no `temperature` record, and no `seed_if_supported` value. The exposure declaration is user-supplied, not mechanically enforced by the harness.  
**Impact:** For fixture scoring purposes, this is a cleanliness caveat that must be carried in fixture metadata. A harness-produced blind judgment would resolve this because the harness protocol mechanically controls exposure. The current artifact's cleanliness claim rests entirely on user attestation. If the user's separate LLM thread had any pre-loaded context about Canoo, Walmart, or EV fleet decisions, the judgment could be contaminated. The contamination risk is unverifiable from the artifact.  
**Minimum closure condition:** The fixture metadata and scoring output must carry the `strict_cleanliness_claim: user_supplied_not_independently_verified` caveat. For a production-quality fixture, a new harness-format blind run should replace or supplement this judgment. The current judgment can be retained as Judgment 001 with the cleanliness caveat attached.  
**Next authorized action:** Fixture authoring design decision. Owner decides whether to accept the cleanliness caveat for the initial fixture run or to require a fresh harness-format judgment run before the fixture is used for scoring conclusions.

---

### FA-07 — Missing Outcome Evidence (Deployment, Acceptance, Financial Exposure)

**Severity:** Minor  
**Location:** `docs/research/judgment-spine/cases/canoo-walmart/facilitator_ledger_v0.md` — Outcome Context; `docs/research/judgment-spine/cases/canoo-walmart/outcome_calibration_v0.md` — Established Reveal Inputs  
**Issue:** Walmart fleet deployment volume, unit acceptance volume, termination-right exercise, and financial exposure outstanding at Canoo's bankruptcy are not established in any reviewed artifact.  
**Evidence:** The facilitator ledger explicitly records: `walmart_delivery_performance: not_established_in_this_ledger`, `walmart_unit_acceptance_volume: not_established_in_this_ledger`, `retailer_operational_loss_or_gain: not_established_in_this_ledger`. The outcome calibration repeats these gaps: "Whether Walmart exercised termination rights," "Whether Walmart had any deposits, prepayments, or financial exposure outstanding at the time of the bankruptcy filing," and "Whether actual protective terms worked in practice" are all listed as unestablished.  
**Impact:** Minor for band input labeling, which draws from pre-decision evidence. The missing outcome evidence does not change whether the case is bandable or what the pre-decision band inputs should be. It does create uncertainty about whether the blind LLM's protective-term conditions (no take-or-pay exposure, deposits/escrow, termination remedies) actually mapped to terms that worked in practice. If the fixture eventually attempts outcome-level band label verification, these gaps would block that verification. For fixture admission purposes, the gaps should be represented as `not_established` in outcome context annotations, not filled with inferences.  
**Minimum closure condition:** The v0.14 facilitator ledger must annotate these outcome gaps as `not_established` rather than leaving them implicit. The outcome calibration's treatment of these gaps as explicit unknowns (already present) must be preserved in the harness-format ledger's `leakage_audit_notes` or `spoiler_inventory` fields.  
**Next authorized action:** Advisory finding. No targeted source check is required before fixture admission. If the owner wants to close these gaps for calibration completeness, a targeted search for public records of Walmart's Canoo vehicle acceptance status and any bankruptcy-related claims would be the appropriate route, but that is outside the scope of this review and is not a precondition for fixture authoring.

---

### FA-08 — band_input_labeling_rubric.md Not Read in This Review

**Severity:** Minor (Advisory Gap)  
**Location:** `docs/research/judgment-spine/harness/v0_14/band_input_labeling_rubric.md` — not in required reads, not read  
**Issue:** The rubric that governs how facilitators assign frozen band enum inputs is the controlling authority for whether specific inputs (e.g., `loss_shape: ruinous_tail` vs. `asymmetric_down`, `option_value: moderate` vs. `high`) can be assigned to this case. This review's analysis of the band floor mechanics (FA-05) relied on plausible input values derived from the participant packet, not from the rubric's definitions and tiebreaker rules.  
**Evidence:** The `action_band_mapping_executable_spec.md` states: "All inputs are frozen in the facilitator ledger using `band_input_labeling_rubric.md`." The `FacilitatorLedger` schema requires `labeling_rubric_version`. The harness index lists `band_input_labeling_rubric.md` as reading order position 8, describing it as "how ledger inputs are frozen." The rubric was not in the required read list for this review and was not read.  
**Impact:** If the rubric defines tiebreaker rules or label-assignment criteria that would change key inputs for this case — particularly `loss_shape`, `option_value`, `opportunity_cost`, and `reversibility_cost` — the band floor analysis in FA-05 could be imprecise. The finding direction (floor ≥ 3 from honest labeling) is unlikely to change because the case's characteristics strongly support moderate option value and moderate opportunity cost, but the exact band width and conflict-escalate conditions could shift.  
**Minimum closure condition:** The fixture author must consult `band_input_labeling_rubric.md` when labeling band inputs for this case and must document whether the rubric changes any of the key inputs analyzed in FA-05. This is an advisory finding for this review, not a blocker for admission.  
**Next authorized action:** Advisory finding. The fixture authoring process must include a rubric read before inputs are frozen.

---

### FA-09 — Pricing-Cap Source-Anchoring Gap (Inherited from Prior Review AR-04)

**Severity:** Minor  
**Location:** `docs/research/judgment-spine/cases/canoo-walmart/facilitator_ledger_v0.md` — Agreement And Risk Terms  
**Issue:** The "capped pricing for the first 10,000 Walmart EVs" claim lacks a source row citation. This was flagged as AR-04 in the prior calibration-gate adversarial review and was not patched.  
**Evidence:** The facilitator ledger lists "capped pricing for the first 10,000 Walmart EVs" in the Agreement And Risk Terms section without attribution to a specific source row (F-01, F-02, or F-03). The prior calibration-gate review noted this gap and recommended either source row attribution or exclusion from calibration mapping.  
**Impact:** Minor for admission. For fixture authoring, if the v0.14 facilitator ledger includes agreement term text in `must_address_items` or `spoiler_inventory`, an unsourced term creates a provenance gap. If fixture scoring attempts to credit whether the blind LLM's protective conditions (which included "capped pricing" adjacents like "no take-or-pay exposure") mapped to actual deal terms, an unanchored term distorts that mapping.  
**Minimum closure condition:** Before the pricing-cap claim is included in any v0.14 harness-format facilitator ledger must_address or spoiler field, it must be attributed to a specific source row or excluded.  
**Next authorized action:** Advisory finding. Owner may resolve this during facilitator ledger authoring.

---

## Non-Findings

The following were reviewed adversarially and found not to create admissibility problems:

**Bandability:** The decision space is encodable without forcing a false binary. The participant packet offers a range of options (hold/defer, narrow pilot, staged conditional commitment, option-heavy structure, broader commitment, hybrid) that map coherently to v0.14 action ladder levels 0–8. The spectrum from hold (0) through commit (8) is accessible without forcing a single correct answer. Fixture-authoring can assign a band that spans multiple levels. Non-finding confirmed.

**Zero-spoiler input path integrity:** The blind judgment was sealed before the facilitator ledger was created. The pre-reveal comparison confirms `comparison_status: pre_reveal_comparison_sealed` with `facilitator_ledger_status: not_created` and `reveal_readout_status: not_created` at comparison creation time. The case_index confirms the creation order. The facilitator ledger records `blind_judgment_status: sealed_before_ledger` and `owner_context_judgment_status: sealed_before_ledger`. Lane separation is intact. The zero-spoiler gate is not violated. Non-finding confirmed.

**Prior calibration-gate review findings adequately consumed:** The outcome calibration (`outcome_calibration_v0.md`) explicitly addresses all six findings (AR-01 through AR-06) from the calibration-gate adversarial review. Frame pre-selection is mitigated by declaring the calibration frame before using the readout's interpretive sections. Asymmetric contrast-hook burden is mitigated by applying the same evidentiary rule to both lanes. The outcome evidence gaps are explicitly preserved in the calibration's unestablished list. Stale status fields are mitigated by routing to case_index for current inventory. The prior review's `accept_with_friction` recommendation was consumed appropriately. Non-finding confirmed.

**TR/Casetext contamination:** No TR/Casetext material appears in any case artifact or harness spec. Both the facilitator ledger and outcome calibration maintain the quarantine: "TR/Casetext remains quarantined Step A plumbing only." No judgment-quality claim derives from TR/Casetext plumbing. Non-finding confirmed.

**Reddit/attention-lens material:** No social-signal, attention-lens, or Reddit-sourced material appears in any reviewed artifact. Non-finding confirmed.

**Outcome sufficiency for band label derivation:** The established outcome evidence — Walmart's definitive 4,500-vehicle purchase agreement (with option to 10,000) and Canoo's later Chapter 7 bankruptcy — is sufficient for the outcome context sections of the fixture. The missing evidence (deployment volume, financial exposure, termination-right exercise) does not prevent honest band input labeling from pre-decision evidence. Pre-decision band inputs draw from the participant packet's evidence, not from post-decision outcomes. Non-finding confirmed.

**Participant packet content cleanliness:** The participant packet's body section is anonymized and free of company names, filing identifiers, source locators, and actual action records. The source packet adversarial review was completed before the participant packet was authored. The handling receipt records major and hygiene items addressed. The zero-spoiler backtest gate is satisfied for the participant-facing body. Non-finding confirmed (caveat: the frontmatter deficit in FA-03 is a structural gap, not a content cleanliness issue).

**Case index inventory accuracy:** The case_index correctly lists all existing artifacts and explicitly states "No required Canoo/Walmart reveal-sequence artifact is currently missing from this index." The case_index is the canonical inventory for current-state navigation. Non-finding confirmed.

---

## Not-Proven Boundaries

- Whether `band_input_labeling_rubric.md` defines label-assignment criteria that would materially change the floor analysis in FA-05: `not proven` — rubric not read in this review.
- Whether `case_to_v0_14_bridge_foundation_v0.md` contains pre-existing guidance that changes fixture authoring requirements for this case: `not proven` — not read in this review.
- Whether targeted source research on Walmart's vehicle acceptance status and financial exposure at Canoo's bankruptcy would change fixture admissibility: `not proven` — assessed as unlikely to change bandability or admission verdict, but not verified.
- Whether the owner-assisted judgment (`owner_context_judgments_v0.md`) would map to a valid v0.14 `BlindJudgement` schema after harness formatting: `not proven` — the owner-assisted judgment lacks `judgement_class`, `ladder_level`, and `evidence_used` structure. It may require a separate fixture contestant entry or may be treated as qualitative context only.
- Whether the blind LLM's "Hybrid: option-heavy staged conditional commitment beginning with narrow operational pilot" maps to ladder level 3, 4, or a split between them: `not proven` — the fixture author must assign this via the rubric-labeled band and the `judgement_class_ladder_mapping` schema.
- Strict validation, readiness, or source-of-truth status for any reviewed artifact: `not proven` — controlling overlay sources are modified or untracked; advisory findings only apply.
- Whether the cited source URLs in `facilitator_ledger_v0.md` (F-01, F-02, F-03) are currently live and their content matches the ledger summaries: `not proven` — no live retrieval performed.

---

## Source-Read Ledger (Compact)

| Source | Why read | Status | Decision it supports |
|---|---|---|---|
| AGENTS.md | Project authority | Modified | Agent operating boundary; no-jb rule |
| Overlay README | Binding rule | Modified | Overlay wins for Orca project facts |
| source-of-truth.md | Source hierarchy | Modified | Advisory findings boundary; strict claims blocked |
| source-loading.md | Source-pack tiers; dirty-state note | Modified | S4 pack selection |
| artifact-roles.md | Research artifact and review report roles | Modified | Role permission for case artifacts and this report |
| review-lanes.md | Adversarial review lane definition | Modified | Lane scope, severity labels, non-patch constraint |
| prompt-orchestration.md | Output mode, review prompt rules | Modified | review-report mode; YAML-only after durable write |
| communication-style.md | Courier YAML shape | Modified | review_summary shape |
| validation-gates.md | Zero-spoiler backtest gate | Modified | Lane separation gate; cleanliness discipline |
| product-proof.md | Zero-spoiler backtest behavior, non-claims | Untracked | Facilitator/participant lane separation |
| case_index.md | Case inventory | Untracked; hash verified | Artifact existence state; use boundary |
| participant_packet_v0.md | Primary admission target | Untracked; hash verified | Cleanliness, frontmatter, decision space check |
| blind_judgments_v0.md | Primary admission target | Untracked; hash verified | Input path integrity; harness format check |
| owner_context_judgments_v0.md | Primary admission target | Untracked; hash verified | Input path integrity; lane label check |
| pre_reveal_judgment_comparison_v0.md | Comparison before reveal | Untracked; hash verified | Pre-reveal seal state; judgment contrast |
| facilitator_ledger_v0.md | Primary admission target | Untracked; hash verified | Outcome evidence; agreement terms; harness format check |
| reveal_readout_v0.md | Primary admission target | Untracked; hash verified | Calibration frame; lane separation |
| outcome_calibration_v0.md | Primary admission target | Untracked; hash verified | Split-axis learning; scoring fairness; evidence gaps |
| calibration_gate_adversarial_review_v0.md | Prior review | Untracked; hash verified | Prior friction consumed; inherited findings |
| harness/v0_14/index.md | Harness spec navigation | Untracked; hash verified | Spec scope; code-ready gate |
| action_band_mapping_table_numbers.md | Band floor/ceiling constants | Untracked; hash verified | FA-05 floor analysis |
| action_band_mapping_executable_spec.md | Band function interface | Untracked; hash verified | FA-01, FA-02, FA-04 harness format requirements |
| scorer_formula_spec.md | Scorer formulas | Untracked; hash verified | FA-05 underreach_primary formula; evidence ID checks |
| pydantic_schema_reference.md | Schema contracts | Untracked; hash verified | FA-01 through FA-04 schema gap identification |

---

## Findings Summary

| ID | Severity | Location | One-line summary |
|---|---|---|---|
| FA-01 | Critical | `blind_judgments_v0.md` | Narrative judgment; no harness-format BlindJudgement schema fields (model_id, run_id, ladder_level, evidence_unit_ids). |
| FA-02 | Critical | `facilitator_ledger_v0.md` | Narrative research ledger; no v0.14 FacilitatorLedger schema fields (frozen_band_inputs, labeling_rubric_version, ledger_freeze_hash). |
| FA-03 | Critical | `participant_packet_v0.md` | Missing v0.14 YAML frontmatter (case_id, decision_date_or_cutoff, source_manifest with evidence_unit_ids). |
| FA-04 | Critical | Case track folder — no EvidenceUnit registry | No EvidenceUnit registry exists; evidence_id_presence_pass and load_bearing_claim_citation_pass would fail immediately. |
| FA-05 | Major | Structural — band floor mechanics | Honest pre-decision labeling will produce floor ≥ 3; owner-assisted no-proceed posture (level 0–1) will be under-band; must be managed via underreach_observability.present: false to preserve split-axis learning. |
| FA-06 | Major | `blind_judgments_v0.md` — capture receipt | Blind judgment cleanliness is user_supplied_not_independently_verified; no mechanical enforcement of separation. |
| FA-07 | Minor | `facilitator_ledger_v0.md`, `outcome_calibration_v0.md` | Missing outcome evidence (deployment volume, financial exposure, termination-right exercise); not a band-labeling blocker; must be annotated as not_established. |
| FA-08 | Minor (advisory gap) | `harness/v0_14/band_input_labeling_rubric.md` — not read | Rubric not read in this review; FA-05 floor analysis used plausible pre-decision inputs, not rubric definitions. |
| FA-09 | Minor | `facilitator_ledger_v0.md` — Agreement And Risk Terms | Pricing-cap claim lacks source row citation (inherited from prior AR-04). |

**Blocking findings (per severity label authority):** None. Severity labels are finding-priority labels only. The four Critical findings are fixture authoring requirements, not evidence gaps that block admission.  
**Advisory findings:** FA-01 through FA-09.  
**Prior findings remediated:** AR-01 through AR-06 from the calibration-gate review were addressed by outcome_calibration_v0.md.

---

## Review-Use Boundary

This review is read-only. Findings are decision input for the authorized decision-maker only. They are not approval, validation, mandatory remediation, patch authority, product proof, judgment-quality proof, fixture admission authority, fixture readiness proof, scoring authorization, or lifecycle completion.

The fixture-admission verdict (`admit_to_fixture_authoring`) is a reviewer recommendation under the commission and criteria defined in this review. It is not a grant of implementation authority, proof that the case has judgment quality, proof that any model is calibrated, proof that the harness is validated, proof that Orca has product readiness, or proof that the Step A plumbing demonstrates judgment quality.

**Required closeout boundary: plumbing works only; not judgment quality.**

---

## Next Authorized Step

Commence v0.14 facilitator ledger authoring for the Canoo/Walmart case using `band_input_labeling_rubric.md` as the controlling label-assignment authority. The four critical findings (FA-01 through FA-04) define the required authoring outputs: a v0.14 FacilitatorLedger schema object with frozen_band_inputs, an EvidenceUnit registry constructed from the existing source packet, a v0.14 participant packet with required YAML frontmatter, and a harness-format BlindJudgement produced by running the updated packet through the harness protocol. The major scoring fairness finding (FA-05) must be addressed by declaring `underreach_observability.present: false` with documented basis in the facilitator ledger before the ledger is frozen.
