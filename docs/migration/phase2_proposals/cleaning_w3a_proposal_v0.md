```yaml
retrieval_header_version: 1
artifact_role: Orca migration note
scope: >
  Phase-2 W3a proposal for the cleaning area (orca/product/spines/cleaning/): bloat/deletion candidates with full deletion-evidence records and ontology/doc-term findings against the SSOT.
use_when:
  - Owner adjudicating Phase-2 deletion candidates for the cleaning spine.
  - Reviewing ontology/doc-term drift findings for cleaning-area files before a Phase-3 ratchet.
authority_boundary: retrieval_only
open_next:
  - docs/migration/orca_second_pass_consolidation_plan_v0.md
stale_if:
  - Any cleaning-area file is moved, renamed, or deleted after this proposal is written (inbound ref counts change).
```

# Phase-2 W3a Proposal — cleaning

## Summary

Files scanned: 3 (all `.md`)
Deletion candidates: 0 high / 0 medium / 0 low
Ontology findings: 3

## A. Deletion candidates

None — area is lean.

All three files in `orca/product/spines/cleaning/contracts/` carry live, unresolved inbound references from other governed areas and collectively form a tightly coupled contract set (readme → foundation; foundation → corroboration note; external consumers reference each independently). Evidence summary per file:

- `core_spine_v0_cleaning_spine_foundation_v0.md`: Inbound refs in `orca/product/spines/data_lake/workflows/core_spine_v0_data_lake_mechanics_map_v0.md:23,213`; `orca/product/spines/cleaning/contracts/core_spine_v0_cleaning_spine_readme_v0.md:13`; `docs/prompts/handoffs/cleaning_spine_foundation_architecture_planning_prompt_v0.md:16,84,130,194`; `docs/prompts/handoffs/cleaning_spine_foundation_architecture_planning_prompt_v1.md:16,26,96,142,205`; `docs/migration/spine_first_target_move_table_v0.md:98`; `docs/migration/repo_structure_spine_first_v0/moved_paths_index.md:33`. Status `FOUNDATION_DRAFT_FROM_PROJECTION_CANDIDATE` with owner directions OD-1/OD-4/OD-7 installed (2026-06-16). The primary authority document for the Cleaning Spine layer contract. Not a deletion candidate.

- `core_spine_v0_cleaning_spine_readme_v0.md`: Inbound refs in `docs/migration/spine_first_target_move_table_v0.md:99`; `docs/migration/repo_structure_spine_first_v0/moved_paths_index.md:34`. Status `PURPOSE_ENTRYPOINT`. Functions as the plain-language onboarding entry point that routes to the foundation; its `open_next` links the foundation as the load-bearing destination. 2 migration-record refs only (no live product/agent refs outside the file set), but the file is the stated entrypoint for implementation scoping and is small and non-redundant with the foundation. Not a deletion candidate.

- `core_spine_v0_corroboration_vs_amplification_discipline_v0.md`: Inbound refs in `orca/product/spines/cleaning/contracts/core_spine_v0_cleaning_spine_foundation_v0.md:18,79,96,399`; `docs/workflows/orca_repo_map_v0.md:539`; `docs/migration/spine_first_target_move_table_v0.md:100`; `docs/migration/repo_structure_spine_first_v0/moved_paths_index.md:35`; `docs/migration/repo_structure_phase2_consolidation_v0/reference_inventory.md:612`; `docs/migration/repo_structure_phase2_consolidation_v0/moved_paths_index.md:7`; `docs/decisions/distillation_binding_core_spine_proof_v0.md:84`; `docs/prompts/handoffs/cleaning_spine_foundation_architecture_planning_prompt_v0.md:20,198`; `docs/prompts/handoffs/cleaning_spine_foundation_architecture_planning_prompt_v1.md:20,209`; `docs/prompts/handoffs/cleaning_spine_projection_doctrine_handoff_prompt_v0.md:143`. Status `PROPOSED` (design note). The repo map (`orca_repo_map_v0.md:539`) calls it out as the Cleaning/Judgment dedup-vs-independence design note; the distillation binding cites it at a specific line (`distillation_binding_core_spine_proof_v0.md:84`). The foundation loads it as a blocked dependency at authoring. Not a deletion candidate.

## B. Ontology / doc-term findings

Compared cleaning-area vocabulary against `orca/product/spines/foundation/ontology/ontology.yaml` (SSOT). Canonical types and runtime aliases checked: `Vertical`, `Brand`, `Product`, `Venue`, `WindCaller`, `Call`, `Observation`, `TrendVector`, `DecisionEvent`, `Reading`, `Memo`, `Case`, `Outcome`, `CapturePacket`, `EvidenceUnit`, `Buyer`, `Org`; aliases `SourceCapturePacket`, `FacilitatorLedger`, `CaseReport`. Head nouns from multi-hump canonical types: `Caller`, `Event`, `Packet`, `Unit`, `Vector`.

**Finding 1 — `EvidenceUnit` appears in the foundation as a prose target noun, correctly absent as a schema field**

- Term: `EvidenceUnit`
- File:line: `core_spine_v0_cleaning_spine_foundation_v0.md` (prose): not present as CamelCase. The SSOT type `EvidenceUnit` is discussed via its snake-case components ("Evidence Candidate Record", "Evidence Unit", "cleaned evidence unit") throughout the foundation and corroboration note. The phrase "Evidence Unit" (two words, not CamelCase) appears in the foundation layer boundary table and non-claims sections; "Evidence Candidate Record" appears as an input boundary concept.
- SSOT status: `EvidenceUnit` is ADOPTED (`evidence` namespace). The two-word prose form "Evidence Unit" is not a CamelCase token; it does not trigger the doc-term checker's `>=2-hump` filter and is not a drift signal. "Evidence Candidate Record" is a pipeline concept, not an SSOT type; its use as a stage name is appropriate.
- Proposed fix (read-only note): None required. Authors should prefer `EvidenceUnit` (CamelCase, no space) when referring to the SSOT type in type-reference contexts rather than the spaced prose form, but this is a style alignment, not a violation. No rename or edit needed for the current foundation draft.

**Finding 2 — `CapturePacket` referenced as prose "capture packet" without CamelCase binding**

- Term: `CapturePacket` (SSOT ADOPTED, `packet` namespace); alias `SourceCapturePacket`
- File:line: `core_spine_v0_cleaning_spine_foundation_v0.md` (YAML illustrative schema block, line ~179): `raw_anchor: "<packet/slice/hash or modality-appropriate anchor>"` — uses lowercase "packet" as a descriptive term, not the SSOT type. The phrase "raw capture packet" and "projection packet" appear in prose without CamelCase.
- SSOT status: `CapturePacket` is ADOPTED. The lowercase uses are positional descriptors within an illustrative (non-binding) schema YAML example marked as `This is an illustrative contract, not a frozen runtime schema`. The foundation explicitly defers runtime schema naming.
- Proposed fix (read-only note): No rename required. When the cleaning runtime schema is authorized, references to capture inputs should use `CapturePacket` (CamelCase) or its alias `SourceCapturePacket` for type-name references to distinguish the SSOT type from informal "packet" usage. This is a future-binding note for the implementation-authorization phase, not a finding in the current draft.

**Finding 3 — "Projected Unit" used as a working label with explicit OD-7 deferral; not a SSOT drift candidate**

- Term: `ProjectedUnit` (would be a new-term candidate under the doc-term checker's head-noun rule: head noun `Unit` is an ontology head noun from `EvidenceUnit`); spelled as two words "Projected Unit" in the foundation.
- File:line: `core_spine_v0_cleaning_spine_foundation_v0.md` (OD-7 section, line ~349): `"Projected Unit" is a working label, not durable ontology`; also non-claims section line ~62: `Not final object naming for "Projected Unit", "Cleaned Unit", Evidence Candidate Record, or Evidence Unit.`
- SSOT status: Neither `ProjectedUnit` nor `CleanedUnit` appears in the SSOT. The foundation explicitly records OD-7: these are working labels only; this artifact does not promote them into canonical spine ontology. The two-word spelling avoids triggering the CamelCase checker.
- Proposed fix (read-only note): The current posture (explicit OD-7 deferral, two-word spelling) is correct. If a future artifact promotes "Projected Unit" to a CamelCase type name, it would become a new-term candidate requiring SSOT adjudication. No action needed on the current draft.
