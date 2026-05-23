# Orca Repo Map v0

```yaml
retrieval_header_version: 1
artifact_role: Repository map
scope: Compact navigation map for Orca source loading and prompt setup.
use_when:
  - Choosing a bounded source pack before a CA prompt, review prompt, or product artifact.
  - Orienting a new thread without bulk-loading the repository.
  - Deciding which product, prompt, review, research, or workflow files are adjacent to a task.
authority_boundary: retrieval_only
open_next:
  - .agents/workflow-overlay/source-loading.md
  - .agents/workflow-overlay/source-of-truth.md
stale_if:
  - New top-level docs folders are added.
  - Core Spine, Data Spine, Cleaning Spine, Judgment Spine, offer, proof, or prompt families are materially reorganized.
  - A later repo-map artifact supersedes this file.
```

- Status: PROPOSED_MAP
- Artifact type: Workflow navigation artifact
- Scope: Repo navigation and source-pack selection
- Refreshed: 2026-05-23
- Implementation authorized: no

## How To Use This Map

Use this map to choose files. Do not treat it as product authority.

For source precedence, open `.agents/workflow-overlay/source-of-truth.md`.
For source-loading budgets, open `.agents/workflow-overlay/source-loading.md`.
For artifact retrievability, body-opening shape, stale/recheck patterns, and
temporary-artifact anti-rot guidance, open
`docs/workflows/artifact_retrievability_guide.md`.

## Top-Level Structure

| Path | Role |
| --- | --- |
| `AGENTS.md` | Workspace instructions and Orca project operating constraints. |
| `.agents/workflow-overlay/` | Orca overlay authority for project facts, folders, source rules, prompt rules, validation, safety, and review lanes. |
| `docs/decisions/` | Decision records. |
| `docs/product/` | Product contracts, Core Spine artifacts, proof plans, source/evidence standards, offer, buyer-proof, and decision artifacts. |
| `docs/prompts/` | Prompt artifacts, wrappers, reruns, reviews, and local templates. |
| `docs/research/` | Research artifacts and consulting-judgment corpus material. |
| `docs/review-inputs/` | Prepared review inputs. |
| `docs/review-outputs/` | Review reports and adversarial artifact reviews. |
| `docs/workflows/` | Workflow records, operational notes, and repo maps. |
| `docs/migration/` | Import and migration records. |
| `docs/hygiene/` | Triage and cleanup queues. |
| `docs/_inbox/` | Non-authoritative scratch and parked material. |

## Overlay Files

| Path | Use for |
| --- | --- |
| `.agents/workflow-overlay/README.md` | Overlay entrypoint and binding rule. |
| `.agents/workflow-overlay/project-authority.md` | Project identity, stage, and forbidden drift. |
| `.agents/workflow-overlay/source-of-truth.md` | Source precedence and conflict rules. |
| `.agents/workflow-overlay/source-loading.md` | Read packs, context budgets, and prompt source capsules. |
| `.agents/workflow-overlay/artifact-folders.md` | Accepted artifact folders and folder rules. |
| `.agents/workflow-overlay/artifact-roles.md` | Artifact role bindings and permissions. |
| `.agents/workflow-overlay/retrieval-metadata.md` | Retrieval-header contract. |
| `.agents/workflow-overlay/prompt-orchestration.md` | Prompt artifact, wrapper, preflight, and rerun rules. |
| `.agents/workflow-overlay/template-registry.md` | Orca-local prompt template registry. |
| `.agents/workflow-overlay/product-proof.md` | Buyer-proof semantics and non-claims. |
| `.agents/workflow-overlay/communication-style.md` | Orca response style. |
| `.agents/workflow-overlay/validation-gates.md` | Validation gate expectations. |
| `.agents/workflow-overlay/review-lanes.md` | Review lane rules. |
| `.agents/workflow-overlay/safety-rules.md` | Safety and forbidden drift. |
| `.agents/workflow-overlay/skill-adoption.md` | Skill source and adoption status. |

## Workflow Navigation Files

| Path | Use for |
| --- | --- |
| `docs/workflows/artifact_retrievability_guide.md` | Operational guidance for durable artifact headers, body-opening source surfaces, stale/recheck patterns, repo-map/index treatment, report-only retrieval checks, and hygiene anti-rot. |
| `docs/workflows/orca_repo_map_v0.md` | Compact navigation map for bounded source-pack selection and prompt setup. |

## Product Anchor Files

Use these before broad product architecture or CA setup:

| Path | Use for |
| --- | --- |
| `docs/decisions/turn_08_product_thesis_v0.md` | Orca thesis, value proposition, strategic center, broad product boundary. |
| `docs/product/orca_offer_hypothesis_v0.md` | Offer hypothesis, buyer-facing language, first proof offer, ICP boundary. |
| `docs/product/orca_buyer_proof_packet_v0.md` | First buyer-proof packet, proof gates, pull signals, kill/graduation criteria. |
| `docs/product/orca_product_lead_first_icp_wedge_decision_v0.md` | Selected first ICP wedge and decision-family focus. |
| `docs/product/orca_product_proof_lead_charter_v0.md` | Product proof lead role and proof execution boundary. |

## Core Spine Files

| Path | Use for |
| --- | --- |
| `docs/product/core_spine_v0_product_contract.md` | Core Spine product contract and eight primitives. |
| `docs/product/core_spine_v0_information_production_foundation_v0.md` | Manual information-production foundation and Evidence Unit standard. |
| `docs/product/core_spine_v0_data_and_cleaning_spine_boundary_v0.md` | Data/Cleaning/Judgment boundary and Evidence Candidate Record setup context. |
| `docs/product/engagement_logic_registry_v0.md` | Signal-use and engagement interpretation registry. |
| `docs/product/core_spine_v0_proof_protocol_v0.md` | Core proof protocol. |
| `docs/product/core_spine_v0_proof_input_selection_v0.md` | Proof input-selection rules. |
| `docs/product/core_spine_v0_proof_packet_preflight_v0.md` | Proof packet preflight. |
| `docs/product/core_spine_v0_proof_case_selection_brief_v0.md` | Proof case-selection brief. |

## Method Validation And Replay Files

Use only when method-validation history, replay evidence, or case-frame locks
are directly relevant. Do not include by default in Data Spine CA prompts.

Key files:

- `docs/product/core_spine_v0_method_validation_replay_packet_v0.md`
- `docs/product/core_spine_v0_method_validation_rubric_v0.md`
- `docs/product/core_spine_v0_method_validation_case_locks_v0.md`
- `docs/product/core_spine_v0_method_validation_case_frame_locks_v0.md`
- `docs/product/core_spine_v0_method_validation_case_frame_lock_contract_v0.md`
- `docs/product/core_spine_v0_method_validation_mv01_intercom_zendesk_replay_v0.md`
- `docs/product/core_spine_v0_method_validation_mv03_stack_overflow_chatgpt_replay_v0.md`
- `docs/product/core_spine_v0_method_validation_mv04_unity_runtime_fee_replay_v0.md`
- `docs/product/core_spine_v0_method_validation_mv05_reddit_api_pricing_replay_v0.md`
- `docs/product/core_spine_v0_method_validation_mv09_thomson_reuters_casetext_replay_v0.md`

## First Proof And Discovery Files

Use for customer discovery, target selection, first proof packet prep, or live
proof readiness questions.

Key files:

- `docs/product/core_spine_v0_first_proof_packet_preparation_v0.md`
- `docs/product/core_spine_v0_first_proof_run_charter_v0.md`
- `docs/product/core_spine_v0_first_proof_run_locks_v0.md`
- `docs/product/core_spine_v0_first_proof_run_packet_v0.md`
- `docs/product/core_spine_v0_first_proof_run_jb_client0_slice_v0.md`
- `docs/product/core_spine_v0_first_proof_run_bt204_backtest_slice_v0.md`
- `docs/product/core_spine_v0_first_proof_run_sh01_shadow_slice_v0.md`
- `docs/product/orca_discovery_batch_0_target_selection_brief_v0.md`
- `docs/product/orca_discovery_batch_0_qualification_prep_sentry_clerk_v0.md`
- `docs/product/orca_discovery_batch_0_candidate_context_scan_v0.md`

## Backtest Specimens

Use when the task is specifically about historical cutoff discipline or the
Unity runtime-fee specimen:

- `docs/product/orca_backtest_specimen_unity_runtime_fee_source_packet_v0.md`
- `docs/product/orca_backtest_specimen_memo_unity_runtime_fee_at_cutoff_v0.md`
- `docs/product/orca_backtest_specimen_unity_runtime_fee_outcome_calibration_v0.md`

## Prompt Families

| Path | Use for |
| --- | --- |
| `docs/prompts/product-planning/` | Product planning prompt drafts. |
| `docs/prompts/feature-planning/` | Feature planning prompt drafts. |
| `docs/prompts/deep-thinking/` | Deep reasoning prompt drafts. |
| `docs/prompts/handoffs/` | Handoff prompt drafts. |
| `docs/prompts/reviews/` | Review prompts. |
| `docs/prompts/reruns/` | Rerun prompts. |
| `docs/prompts/patches/` | Patch prompts. |
| `docs/prompts/wrappers/` | Thin wrapper prompts. |
| `docs/prompts/templates/` | Local prompt templates. |
| `docs/prompts/hygiene-queue/` | Current drift/parking area; not listed as an accepted prompt-family folder in the overlay. |

## Research And Review Areas

| Path | Use for |
| --- | --- |
| `docs/research/consulting-judgment-corpus/` | Consulting-judgment corpus, prompts, lane outputs, synthesis, candidate screens, backtestability, and reject patterns. |
| `docs/review-outputs/adversarial-artifact-reviews/` | Adversarial artifact review reports. |
| `docs/review-outputs/method-validation/` | Method-validation review outputs. |
| `docs/review-outputs/proof/` | Proof review outputs. |

## Inbox Warning

`docs/_inbox/` is non-authoritative. It currently contains contaminated
method-validation replay outputs and compacted-run material. Do not read or
promote those files unless the task explicitly concerns contamination,
recovery, hygiene, or comparison against canonical promoted files.

## Recommended Read Packs

### Data Spine Setup CA

Start with:

- `docs/decisions/turn_08_product_thesis_v0.md`: thesis, value proposition,
  strategic center, and current theory sections.
- `docs/product/orca_offer_hypothesis_v0.md`: core offer hypothesis,
  mechanism, fit diagnostic, and non-claims sections.
- `docs/product/orca_buyer_proof_packet_v0.md`: proof standard, target buyer,
  signal surface, disqualifiers, and not-build boundaries.
- `docs/product/core_spine_v0_data_and_cleaning_spine_boundary_v0.md`:
  purpose, decision, layer rules, and future ECR/Evidence Unit boundaries.
- `docs/product/core_spine_v0_product_contract.md`: product bet, core rule,
  frozen primitives, and explicit non-goals only.
- `docs/product/core_spine_v0_information_production_foundation_v0.md`:
  Evidence Unit standard and boundary rules only.

Do not read these files in full by default. Use targeted sections and expand
only when a concrete source gap could change the Data Spine CA prompt.

Exclude by default:

- method-validation replays;
- first proof run packets;
- review outputs;
- research corpus;
- `docs/_inbox/`.

### Offer Or Buyer Proof Work

Start with:

- `docs/decisions/turn_08_product_thesis_v0.md`
- `docs/product/orca_offer_hypothesis_v0.md`
- `docs/product/orca_buyer_proof_packet_v0.md`
- `docs/product/orca_product_lead_first_icp_wedge_decision_v0.md`
- `.agents/workflow-overlay/product-proof.md`

### Core Spine Evidence Standard Work

Start with:

- `docs/product/core_spine_v0_product_contract.md`
- `docs/product/core_spine_v0_information_production_foundation_v0.md`
- `docs/product/engagement_logic_registry_v0.md`
- nearest boundary or proof artifact named by the request.

### Prompt Or Review Prompt Work

Start with:

- `.agents/workflow-overlay/prompt-orchestration.md`
- `.agents/workflow-overlay/template-registry.md`
- relevant prompt template under `docs/prompts/templates/`
- the target source artifact being prompted or reviewed.

## New Thread Guidance

Use a new thread or compact handoff when the next task needs more than one
recommended read pack, more than six full artifacts, or both repo-map refresh
and CA prompt drafting. The handoff should cite this map, the source-loading
overlay, the target read pack, and the files excluded by default.

## Not-Proven Boundaries

This map does not prove acceptance, validation, readiness, buyer pull,
implementation authorization, source correctness, or freshness of every listed
artifact. Check the target artifact, retrieval header, and current `git status`
before strict claims.
