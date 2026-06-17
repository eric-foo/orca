# IG Capture Spine Candidate File Inventory v0

```yaml
retrieval_header_version: 1
artifact_role: Migration inventory - candidate file marking
scope: >
  Marks files related to the IG source-capture / operating-envelope lane and
  classifies likely buckets under the proposed spine-first Capture/IG workspace.
use_when:
  - Planning a future migration of IG source-capture artifacts toward the
    proposed spine-first workspace structure.
  - Separating direct Capture/IG lane files from shared Capture infrastructure
    and global repo maps.
authority_boundary: retrieval_only
open_next:
  - docs/decisions/orca_repo_structure_binding_v0.md
  - docs/product/source_capture_toolbox/ig_at_scale_operating_envelope_v0.md
stale_if:
  - A later accepted repo-structure decision changes the target spine layout.
  - Any listed file is moved, deleted, renamed, or superseded.
  - The IG operating-envelope lane adds more source, runner, test, or report files.
```

- Status: CANDIDATE_INVENTORY_ONLY.
- Current binding: the active repo structure is still `docs/` plus `orca-harness/`.
- Proposal source read from external worktree:
  `C:/Users/vmon7/Desktop/projects/orca/.codex/worktrees/commission-spine-structure/docs/decisions/orca_spine_first_workspace_structure_proposal_v0.md`.
- Non-claims: not migration authorization, not a moved-path index, not validation,
  not readiness, not a claim that `orca/product/spines/capture/` is accepted.

## Target Interpretation

The proposal names the product spine root as:

```text
orca/product/spines/capture/
```

This inventory uses `spines/capture/IG` as an inferred sub-area inside that
Capture spine, not as a new top-level `capturespine/IG` root. A likely
migration shape would keep role folders first inside the Capture spine, with
`IG/` as a subfolder where needed:

```text
orca/product/spines/capture/
  authority/IG/
  decisions/IG/
  prompts/IG/
  workflows/IG/
  research/IG/
  reports/IG/
  harness/IG/
  tests/IG/
  migrations/IG/
```

## Direct Capture/IG Product Docs

These are directly IG-owned source-capture, operating-envelope, discovery,
creator-momentum, or wind-caller artifacts.

| Current path | Candidate bucket | Mark |
| --- | --- | --- |
| `docs/product/source_capture_toolbox/ig_at_scale_operating_envelope_v0.md` | `authority/IG/` | MOVE_CAPTURE_IG_HIGH |
| `docs/product/source_capture_toolbox/ig_logged_out_sustainability_probe_plan_v0.md` | `workflows/IG/` | MOVE_CAPTURE_IG_HIGH |
| `docs/product/source_capture_toolbox/ig_r_probe_results_v0.md` | `research/IG/` | MOVE_CAPTURE_IG_HIGH |
| `docs/product/source_capture_toolbox/ig_capture_rate_findings_report_v0.md` | `reports/IG/` | MOVE_CAPTURE_IG_HIGH |
| `docs/product/source_capture_toolbox/ig_capture_findings_consolidated_v0.md` | `reports/IG/` | MOVE_CAPTURE_IG_HIGH |
| `docs/product/source_capture_toolbox/ig_sustained_cadence_r_probe_design_v0.md` | `workflows/IG/` | MOVE_CAPTURE_IG_HIGH |
| `docs/product/source_capture_toolbox/ig_capture_shape_contract_spec_v0.md` | `authority/IG/` | MOVE_CAPTURE_IG_HIGH |
| `docs/product/source_capture_toolbox/ig_creator_discovery_spec_v0.md` | `authority/IG/` | MOVE_CAPTURE_IG_HIGH |
| `docs/product/source_capture_toolbox/ig_creator_discovery_suggested_accounts_recon_v0.md` | `research/IG/` | MOVE_CAPTURE_IG_HIGH |
| `docs/product/source_capture_toolbox/ig_creator_roster_frontier_ledger_spec_v0.md` | `authority/IG/` | MOVE_CAPTURE_IG_HIGH |
| `docs/product/source_capture_toolbox/ig_reel_viewcount_capture_feasibility_recon_v0.md` | `research/IG/` | MOVE_CAPTURE_IG_HIGH |
| `docs/product/source_capture_toolbox/ig_wind_caller_calls_capture_build_architecture_v0.md` | `authority/IG/` or `harness/IG/` | MOVE_CAPTURE_IG_MEDIUM |
| `docs/product/source_capture_toolbox/ig_wind_caller_capture_feasibility_recon_v0.md` | `research/IG/` | MOVE_CAPTURE_IG_HIGH |
| `docs/product/data_capture_spine/orca_creator_momentum_pipeline_architecture_v0.md` | `authority/IG/` | MOVE_CAPTURE_IG_HIGH |

## Adjacent IG-Core / Monitoring Docs

These are IG-heavy, but they also define cross-data-type, monitoring, or
creator-momentum core boundaries. They should not be dumped into IG just because
they mention IG.

| Current path | Candidate bucket | Mark |
| --- | --- | --- |
| `docs/product/data_capture_spine/orca_creator_monitoring_policy_architecture_v0.md` | `authority/monitoring/` under Capture, with an `IG/` profile pointer | CAPTURE_SHARED_HIGH |
| `docs/product/data_capture_spine/orca_capture_projection_storage_spine_architecture_v0.md` | `authority/shared/` under Capture, not IG-only | CAPTURE_SHARED_HIGH |
| `docs/product/data_capture_spine/source_capture_packet_schema_evolution_architecture_v0.md` | `authority/shared/` under Capture | CAPTURE_SHARED_HIGH |
| `docs/decisions/wind_caller_calibration_carveout_v0.md` | `decisions/social_creator_capture/`, not IG-only | CAPTURE_SHARED_HIGH |
| `docs/research/creator_momentum_data_landscape_v0.md` | `research/shared/` under Capture | CAPTURE_SHARED_HIGH |

## IG Prompt / Handoff Artifacts

| Current path | Candidate bucket | Mark |
| --- | --- | --- |
| `docs/prompts/handoffs/ig_capture_rate_at_scale_operating_envelope_handoff_v0.md` | `prompts/IG/handoffs/` | MOVE_CAPTURE_IG_HIGH |
| `docs/hygiene/ig_creator_momentum_lane_handoff_v0.md` | `workflows/IG/` or `archive/IG/` if treated as historical continuation | MOVE_CAPTURE_IG_MEDIUM |

Historical external worktree artifact observed during this lane, not a current
workspace file:

| Current path | Candidate bucket | Mark |
| --- | --- | --- |
| `C:/Users/vmon7/Desktop/projects/orca/.codex/worktrees/ig-capture-operating-envelope-successor-main/docs/prompts/handoffs/ig_capture_operating_envelope_successor_main_handoff_v0.md` | `prompts/IG/handoffs/` if deliberately preserved | HISTORICAL_EXTERNAL_DO_NOT_PORT_BLINDLY |

## IG Harness Code

Executable code should remain in `orca-harness/` until a separate code-root
migration is accepted. Under the spine-first proposal, the Capture workspace
would hold harness notes, schemas, runner pointers, or migration indexes rather
than silently moving Python packages.

| Current path | Candidate bucket | Mark |
| --- | --- | --- |
| `orca-harness/runners/run_source_capture_ig_calls_packet.py` | `harness/IG/` pointer or design note | HARNESS_POINTER_CAPTURE_IG_HIGH |
| `orca-harness/runners/run_ig_creator_momentum_projection.py` | `harness/IG/` pointer or design note | HARNESS_POINTER_CAPTURE_IG_HIGH |
| `orca-harness/runners/run_ig_operating_envelope_stage.py` | `harness/IG/` pointer or design note | HARNESS_POINTER_CAPTURE_IG_HIGH |
| `orca-harness/source_capture/ig_calls_parse.py` | `harness/IG/` pointer or schema note | HARNESS_POINTER_CAPTURE_IG_HIGH |
| `orca-harness/source_capture/ig_momentum_harvest.py` | `harness/IG/` pointer or adapter note | HARNESS_POINTER_CAPTURE_IG_HIGH |
| `orca-harness/source_capture/ig_projection.py` | `harness/IG/` pointer or projection note | HARNESS_POINTER_CAPTURE_IG_HIGH |

Shared dependency, not IG-owned:

| Current path | Candidate bucket | Mark |
| --- | --- | --- |
| `orca-harness/source_capture/__init__.py` | shared harness package export | SHARED_DEPENDENCY_DO_NOT_MOVE_AS_IG |
| `orca-harness/source_capture/cadence.py` | shared capture cadence utility | SHARED_DEPENDENCY_DO_NOT_MOVE_AS_IG |
| `orca-harness/source_capture/models.py` | shared Source Capture Packet models | SHARED_DEPENDENCY_DO_NOT_MOVE_AS_IG |
| `orca-harness/source_capture/packet_assembly.py` | shared packet assembly | SHARED_DEPENDENCY_DO_NOT_MOVE_AS_IG |
| `orca-harness/source_capture/packet_inspection.py` | shared packet inspection | SHARED_DEPENDENCY_DO_NOT_MOVE_AS_IG |
| `orca-harness/source_capture/writer.py` | shared packet writer | SHARED_DEPENDENCY_DO_NOT_MOVE_AS_IG |
| `orca-harness/source_capture/adapters/browser_snapshot.py` | shared browser snapshot adapter used by IG runner | SHARED_DEPENDENCY_DO_NOT_MOVE_AS_IG |
| `orca-harness/source_capture/proxy_profiles.py` | shared proxy profile support used by IG runner | SHARED_DEPENDENCY_DO_NOT_MOVE_AS_IG |

## IG Tests

Executable tests should remain in `orca-harness/tests/` unless a separate
code/test-root migration is accepted. A future Capture spine can carry pointers
or test-plan documentation under `tests/IG/`.

| Current path | Candidate bucket | Mark |
| --- | --- | --- |
| `orca-harness/tests/unit/test_ig_calls_parse.py` | `tests/IG/` pointer or test plan | TEST_POINTER_CAPTURE_IG_HIGH |
| `orca-harness/tests/unit/test_ig_momentum_harvest.py` | `tests/IG/` pointer or test plan | TEST_POINTER_CAPTURE_IG_HIGH |
| `orca-harness/tests/unit/test_source_capture_ig_calls_packet.py` | `tests/IG/` pointer or test plan | TEST_POINTER_CAPTURE_IG_HIGH |
| `orca-harness/tests/unit/test_source_capture_ig_projection.py` | `tests/IG/` pointer or test plan | TEST_POINTER_CAPTURE_IG_HIGH |
| `orca-harness/tests/unit/test_ig_operating_envelope_stage.py` | `tests/IG/` pointer or test plan | TEST_POINTER_CAPTURE_IG_HIGH |

## Generated Local Run Artifacts

These are evidence/run outputs, not source documents. Do not move raw run trees
by default. If preserved, retain a human-readable summary or moved-path pointer
under `reports/IG/` and keep raw generated payloads out of source migration
unless an explicit fixture-retention decision says otherwise.

| Current path | Candidate bucket | Mark |
| --- | --- | --- |
| `orca-harness/_test_runs/ig_current_egress_recovery_20260617_hyram_768x1024_max4/` | `reports/IG/` summary pointer only | GENERATED_DO_NOT_MOVE_BY_DEFAULT |
| `orca-harness/_test_runs/ig_stage1_current_egress_logged_out_768x1024_max12_20260617_162730/` | `reports/IG/` summary pointer only | GENERATED_DO_NOT_MOVE_BY_DEFAULT |

Representative generated leaves under those roots include per-handle
`manifest.json`, `receipt.md`, `raw/*.json`, and `_projection/*.json`. This
inventory marks the run roots plus leaf patterns instead of enumerating every
generated payload file.

## Global / Shared References To Update If Migration Happens

These files are not Capture/IG-owned, but a future migration must update their
references or moved-path indexes.

| Current path | Why not IG-owned | Mark |
| --- | --- | --- |
| `docs/workflows/data_capture_spine_consolidation_map_v0.md` | global Data Capture navigation map | GLOBAL_REFERENCE_UPDATE_ONLY |
| `docs/workflows/orca_repo_map_v0.md` | repo-wide map | GLOBAL_REFERENCE_UPDATE_ONLY |
| `docs/product/source_capture_toolbox/source_capture_playbook_v0.md` | shared capture method playbook | CAPTURE_SHARED_REFERENCE_UPDATE_ONLY |
| `docs/product/source_capture_toolbox/capture_recon_index_v0.md` | shared recon index across sources | CAPTURE_SHARED_REFERENCE_UPDATE_ONLY |
| `docs/product/source_capture_toolbox/source_capture_packet_fixture_admission_criteria_v0.md` | shared packet fixture policy | CAPTURE_SHARED_REFERENCE_UPDATE_ONLY |
| `docs/product/source_capture_toolbox/pipe_block_wall_escalation_v0.md` | shared block/wall escalation concept | CAPTURE_SHARED_REFERENCE_UPDATE_ONLY |
| `docs/product/source_capture_toolbox/source_capture_anti_block_ladder_usage_guide_v0.md` | shared anti-block usage guide | CAPTURE_SHARED_REFERENCE_UPDATE_ONLY |
| `docs/product/source_capture_toolbox/weapon_anti_block_http_ladder_v0.md` | shared source-capture weapon | CAPTURE_SHARED_REFERENCE_UPDATE_ONLY |
| `docs/product/source_capture_toolbox/cloakbrowser_local_setup_probe_receipt_v0.md` | shared CloakBrowser setup evidence | CAPTURE_SHARED_REFERENCE_UPDATE_ONLY |
| `docs/product/source_capture_toolbox/cloakbrowser_packet_runner_architecture_v0.md` | shared CloakBrowser runner architecture | CAPTURE_SHARED_REFERENCE_UPDATE_ONLY |
| `docs/product/source_capture_toolbox/cloakbrowser_packet_runner_architecture_independent_pass_v0.md` | shared CloakBrowser review/pass artifact | CAPTURE_SHARED_REFERENCE_UPDATE_ONLY |

## Current Worktree Notes

- `orca-harness/runners/run_ig_operating_envelope_stage.py` and
  `orca-harness/tests/unit/test_ig_operating_envelope_stage.py` are present in
  the current worktree as uncommitted added files at inventory time.
- The first 5.3 sidecar inventory attempt failed because the requested model was
  over quota; a later 5.3 retry also failed after spawn. A 5.4 read-only audit
  completed and its source-backed additions / bucket corrections are integrated.
