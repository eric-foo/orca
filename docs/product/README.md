# Orca Product Docs

Use this folder for docs-first product artifacts: Core Spine contracts, satellite notes, evidence standards, source maps, product proof plans, decision artifacts, memo substrates, evidence appendices, and executive-deck shape drafts.

Artifacts are organized by lane subfolder per
`docs/decisions/orca_repo_structure_binding_v0.md`: `core_spine/`,
`data_capture_spine/`, `judgment_spine/`, `signal_content/`, `ecr/`,
`product_lead/`, and `source_capture_toolbox/`. New product artifacts go in the
matching lane; pre-move paths in historical records resolve via
`docs/migration/repo_structure_phase2_consolidation_v0/moved_paths_index.md`.

Keep the Core + Satellite split explicit:

- Core Spine: market-agnostic evidence mechanics.
- Satellites: decision-specific and domain-specific context.

For Judgment Spine claim boundaries, use
`judgment_spine/judgment_spine_evidence_ladder_architecture_v0.md` to distinguish
Product-Learning, Buyer-Proof, and Judgment-Quality evidence before making
proof, validation, scoring, fixture-admission, or readiness claims.

For Source Capture Armory planning, use
`source_capture_toolbox/README.md` as the product-facing entrypoint. New
Source Capture Armory product docs should live under
`docs/product/source_capture_toolbox/` unless a later migration decision moves
existing controlling artifacts. Existing Data Capture source-access decisions,
method plans, and obligation contracts now live under `data_capture_spine/`
(moved by the Phase-2 consolidation) and are indexed from the armory README and
the moved-paths index.

Do not treat Client 0 `jb` material as core product authority unless a product artifact explicitly promotes the concept as generalizable.
