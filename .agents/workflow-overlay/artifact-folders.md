# Artifact Folders

```yaml
retrieval_header_version: 1
artifact_role: Orca overlay authority
scope: Accepted Orca artifact folders and folder rules.
use_when:
  - Deciding where Orca artifacts belong.
  - Checking whether a folder is authoritative, scratch, or forbidden.
authority_boundary: retrieval_only
```

## Accepted Folders

- `docs/decisions/`: Orca decision records.
- `docs/prompts/`: Orca prompt artifacts.
- `docs/prompts/product-planning/`: product planning prompt drafts.
- `docs/prompts/feature-planning/`: feature planning prompt drafts.
- `docs/prompts/deep-thinking/`: deep reasoning prompt drafts.
- `docs/prompts/handoffs/`: implementation handoff prompt drafts.
- `docs/prompts/reviews/`: review prompt drafts.
- `docs/prompts/reruns/`: rerun prompt drafts.
- `docs/prompts/patches/`: patch prompt drafts.
- `docs/prompts/wrappers/`: thin wrapper prompts that reference full prompt artifacts.
- `docs/prompts/templates/`: Orca-local prompt templates and template README files, subordinate to `.agents/workflow-overlay/template-registry.md`.
- `docs/review-inputs/`: artifacts prepared for review.
- `docs/review-outputs/`: reviewer findings reports and overlay-bound verdicts.
- `docs/review-outputs/adversarial-artifact-reviews/`: adversarial artifact review reports.
- `docs/workflows/`: workflow records, repo maps, validation notes, and operational records owned by Orca.
- `docs/migration/`: migration and import queue records.
- `docs/product/`: product contracts, product proof plans, core-spine notes, satellite notes, evidence standards, source maps, decision artifacts, memo substrates, evidence appendices, and executive-deck shape drafts.
- `docs/product/source_capture_toolbox/`: product-facing Source Capture Armory design notes, scoped specs, and gap notes. Existing controlling Data Capture source-access decisions, method plans, and obligation contracts remain at their historical paths unless a later migration decision moves them.
- `docs/product/` lane subfolders (`core_spine/`, `data_capture_spine/`, `judgment_spine/`, `signal_content/`, `ecr/`, `product_lead/`): the bound second-level axis for product artifacts per `docs/decisions/orca_repo_structure_binding_v0.md`. New product artifacts use the matching lane; files matching no lane may stay at `docs/product/` root. Existing flat files move only via the Phase-2 migration package, not ad hoc.
- `repo-structure.yaml` (repo root): the machine structure map - router only, consumed by `.agents/hooks/check_placement.py` and agents for navigation. It declares homes and never states rules; this overlay file remains the placement authority and wins on conflict.
- `docs/research/`: public/source research artifacts, evidence-only lane outputs, synthesis reports, candidate screens, and reject-pattern maps that support Orca product or proof work without becoming product authority by default.
- `docs/research/judgment-spine/harness/v0_14/smoke_tests/`: Judgment Harness v0.14 no-case smoke-test receipts and operator provenance records. Artifacts in this folder are plumbing evidence only and do not become real-case probe, validation, fixture-admission, product-proof, or judgment-quality evidence by location.
- `docs/hygiene/`: triage queues and cleanup notes for Orca artifacts.
- `docs/_inbox/`: non-authoritative temporary holding area for scratch prompts, notes, imports, and untriaged material.
- `.agents/skills/`: Orca-local accepted/candidate workflow skill source (for example, `orca-product-lead`), governed by `.agents/workflow-overlay/skill-adoption.md`. Orca-local only; this is NOT plugin, user-level, installed, or external skill source, and living here does not deploy, activate, or make a skill resolver-visible.

## Rules

- Keep durable Orca artifacts under `docs/` unless a later Orca decision creates a narrower folder.
- Full prompt artifacts and thin wrappers must follow `.agents/workflow-overlay/prompt-orchestration.md`.
- New or materially touched durable human-authored workflow artifacts must
  follow `.agents/workflow-overlay/retrieval-metadata.md` unless that contract
  excludes the artifact class.
- Treat `docs/_inbox/` as scratch only. Nothing in `_inbox` is Orca authority until promoted into an accepted docs folder or overlay file.
- Track parked or temporary material through `docs/hygiene/queue.md` when it may need promotion, review, archiving, or deletion.
- Keep product artifacts in `docs/product/` unless they are accepted decision records, prompt artifacts, workflow records, review artifacts, or migration records.
- Keep research artifacts in `docs/research/` when the primary purpose is source discovery, corpus qualification, evidence gathering, candidate screening, or rejected-source mapping. Promote research conclusions into `docs/product/` or `docs/decisions/` only through a later accepted product or decision artifact.
- Do not create implementation folders such as `src`, `app`, `packages`, `tests`, or automation runtimes until explicitly authorized.
- Orca-local workflow skills live only under `.agents/skills/` and are governed by `.agents/workflow-overlay/skill-adoption.md`; acceptance there is a local freeze, not deployment, and must not edit plugin, user-level, installed, or external skill source.
- Do not copy or move material from external reference folders unless a later turn explicitly authorizes the import.
- Placement is checked at the write boundary by `.agents/hooks/check_placement.py` (EP-04, advisory; `--strict` commit/CI mode available), which reads `repo-structure.yaml` as its only rule source. A passing check is placement shape only - never validation, readiness, or authority. Parameters and invariants: `docs/decisions/orca_repo_structure_binding_v0.md`.

## Direction Change Propagation - Source Capture Armory Product Folder

```yaml
direction_change_propagation:
  doctrine_changed: "The Source Capture Armory product-doc folder convention is now bound in the overlay folder authority while existing controlling Data Capture source-access documents remain at their historical paths."
  trigger: output_authority
  controlling_sources_updated:
    - ".agents/workflow-overlay/artifact-folders.md"
    - "docs/product/source_capture_toolbox/README.md"
    - "docs/product/README.md"
  downstream_surfaces_checked:
    - "AGENTS.md"
    - ".agents/workflow-overlay/README.md"
    - ".agents/workflow-overlay/source-of-truth.md"
    - ".agents/workflow-overlay/source-loading.md"
    - "docs/workflows/orca_repo_map_v0.md"
    - "docs/decisions/data_capture_spine_source_access_tooling_build_authorization_v0.md"
    - "docs/product/data_capture_spine/data_capture_source_access_method_plan_v0.md"
  intentionally_not_updated:
    - path: ".agents/workflow-overlay/artifact-roles.md"
      reason: "The existing Product artifact role covers Source Capture Armory design notes and scoped specs; this patch binds folder routing, not a new artifact role."
    - path: "docs/product/data_capture_spine/data_capture_source_access_boundary_decision_v0.md"
      reason: "Source-access boundary permission and hard stops did not change."
    - path: "docs/product/data_capture_spine/core_spine_v0_data_capture_spine_obligation_contract_v0.md"
      reason: "Data Capture obligations did not change."
  stale_language_search: "rg -n \"source_capture_toolbox|Source Capture Armory\" .agents/workflow-overlay/artifact-folders.md docs/product/README.md docs/product/source_capture_toolbox/README.md .agents/workflow-overlay/source-loading.md docs/workflows/orca_repo_map_v0.md docs/decisions/data_capture_spine_source_access_tooling_build_authorization_v0.md docs/product/data_capture_spine/data_capture_source_access_method_plan_v0.md"
  non_claims:
    - "not validation"
    - "not readiness"
    - "not implementation authorization"
    - "not source-access boundary amendment"
    - "not ECR, Cleaning, or Judgment design"
```

## Direction Change Propagation - No-Case Smoke Tests Folder

```yaml
direction_change_propagation:
  doctrine_changed: >
    The Judgment Harness v0.14 now has a narrow accepted folder for no-case
    smoke-test receipts and operator provenance records, with a permanent
    plumbing-only/non-gate-clearing boundary.
  trigger: output_authority
  controlling_sources_updated:
    - .agents/workflow-overlay/artifact-folders.md
  downstream_surfaces_checked:
    - AGENTS.md
    - .agents/workflow-overlay/README.md
    - .agents/workflow-overlay/source-of-truth.md
    - .agents/workflow-overlay/source-loading.md
    - docs/research/judgment-spine/harness/v0_14/no_case_smoke_test_authorization_checklist_v0.md
    - docs/decisions/no_case_smoke_test_authorization_pending_parameters_v0.md
    - docs/review-outputs/adversarial-artifact-reviews/no_case_smoke_test_authorization_pending_parameters_adversarial_artifact_review_v0.md
  intentionally_not_updated:
    - path: .agents/workflow-overlay/artifact-roles.md
      reason: >
        Existing Research artifact and Workflow record roles already cover the
        receipt/provenance distinction; this patch only binds a narrower folder.
    - path: docs/research/judgment-spine/harness/v0_14/no_case_smoke_test_authorization_checklist_v0.md
      reason: >
        The checklist already requires exact receipt/provenance paths and keeps
        smoke artifacts non-gate-clearing; no semantic update is required.
  stale_language_search: >
    rg -n "smoke_tests|no-case smoke|SMOKE_NOCASE_|gate-clearing|fixture admission|judgment-quality"
    .agents/workflow-overlay/artifact-folders.md
    docs/research/judgment-spine/harness/v0_14/no_case_smoke_test_authorization_checklist_v0.md
    docs/decisions/no_case_smoke_test_authorization_pending_parameters_v0.md
  non_claims:
    - not validation
    - not readiness
    - not live-call authorization
    - not fixture admission
    - not judgment-quality proof
```

## Direction Change Propagation - Orca-Local Skill Folder

```yaml
direction_change_propagation:
  doctrine_changed: >
    `.agents/skills/` is now a bound Orca-local accepted/candidate workflow-skill
    source folder, and the first Orca-local skill (`orca-product-lead`) is
    accepted/frozen. Acceptance is a local freeze only — not deployment,
    activation, or resolver-visibility.
  trigger: output_authority
  controlling_sources_updated:
    - .agents/workflow-overlay/artifact-folders.md
    - .agents/workflow-overlay/skill-adoption.md
    - .agents/skills/orca-product-lead/SKILL.md
  downstream_surfaces_checked:
    - AGENTS.md                                      # grep: no skill/folder reference; skill rules already defer to overlay; no change
    - .agents/workflow-overlay/README.md             # grep: no reference; no change
    - .agents/workflow-overlay/source-of-truth.md    # grep: no reference; skill is not an authority source (it defers)
    - .agents/workflow-overlay/project-authority.md  # grep: no reference; skill is explicitly non-authority
  stale_language_search: 'rg -n "orca-product-lead|\.agents/skills|no accepted Orca-local" . (run 2026-06-08; only skill-adoption.md carried the stale "no accepted" status, now fixed)'
  intentionally_not_updated:
    - path: .agents/workflow-overlay/skill-adoption.md (Known Snapshots, 2026-05-24 line)
      reason: dated historical observation, true as of its date.
    - path: docs/workflows/orca_pricing_first_doc_cascade_proposal_v0.md
      reason: historical proposal record (row 7 deferral); current acceptance state now lives in skill-adoption.md; the proposal is not retro-edited.
    - path: docs/product/product_lead/orca_product_lead_first_icp_wedge_decision_v0.md
      reason: already-superseded historical record; its supersede banner governs.
    - path: docs/decisions/orca_icp_wedge_convergence_break_in_first_v0.md
      reason: already-superseded historical record; its supersede banner governs.
    - path: docs/prompts/product-planning/orca_product_lead_ca_first_icp_wedge_prompt_v0.md
      reason: historical generator prompt; records a then-open question, not current state.
    - path: docs/prompts/handoffs/jb_prompt_path_assignment_ca_settlement_prompt_v0.md
      reason: jb-scoped non-Orca lane; its "do not edit .agents/skills" guardrail is not stale.
  non_claims:
    - not deployment
    - not activation
    - not resolver-visibility
    - not validation
    - not readiness
```

## Direction Change Propagation - Repo Structure Binding v0

```yaml
direction_change_propagation:
  doctrine_changed: >
    Orca adopts the agent-first repo-structure invariant core as Orca-owned
    doctrine via docs/decisions/orca_repo_structure_binding_v0.md, binds the
    docs/product/ by-lane second axis and root machine map repo-structure.yaml
    (router-only), and authorizes the EP-04 placement substrate
    (.agents/hooks/check_placement.py, advisory write-boundary + --strict
    commit/CI mode). Forward-only; the docs/product flat-file consolidation is
    packaged under docs/migration/repo_structure_phase2_consolidation_v0/ and
    is not executed by this change.
  trigger: output_authority
  related_triggers:
    - workflow_authority
  controlling_sources_updated:
    - .agents/workflow-overlay/artifact-folders.md
    - docs/decisions/orca_repo_structure_binding_v0.md
    - repo-structure.yaml
  downstream_surfaces_checked:
    - AGENTS.md                                      # no structure facts; defers to overlay; no change
    - .agents/workflow-overlay/README.md             # section ownership unchanged; no change
    - .agents/workflow-overlay/source-of-truth.md    # hierarchy/propagation mechanics unchanged; receipt inline here per contract
    - .agents/workflow-overlay/source-loading.md     # read packs reference unchanged paths until Phase-2 apply
    - .agents/workflow-overlay/validation-gates.md   # Enforcement Placement principle already present and generic
    - docs/workflows/orca_repo_map_v0.md             # updated in this change set (Active Hooks + root map entry)
    - docs/STRUCTURE.md
  intentionally_not_updated:
    - path: .agents/workflow-overlay/source-of-truth.md
      reason: shared commit-once-whole file; hierarchy unchanged; DCP contract stores receipts inline in the changed artifact.
    - path: docs/STRUCTURE.md
      reason: narrative tier per the binding's surface tiering; gains lane detail when the Phase-2 move applies, not before.
    - path: .agents/workflow-overlay/validation-gates.md
      reason: the principle is already bound there; the EP-04 instance is recorded in the EP classification decision update and the repo map Active Hooks note.
  stale_language_search: 'rg -n "repo-structure.yaml|check_placement|orca_repo_structure_binding" .agents/workflow-overlay docs/STRUCTURE.md docs/workflows/orca_repo_map_v0.md AGENTS.md (run at closeout; expected hits only in this change set)'
  non_claims:
    - not validation
    - not readiness
    - not a commit, push, or branch action
    - not execution of the Phase-2 move
    - hook wiring not live until session restart
```
