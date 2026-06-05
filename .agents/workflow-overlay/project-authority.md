# Project Authority

## Identity

- Project/workspace: Orca
- Stage: docs-first bootstrap
- Relationship to `jb`: separate workspace; no inherited project authority
- Product/domain purpose: outside-in strategic intelligence system for public market signals and evidence-backed allocation decisions
- Target users/operators: companies and teams making product, positioning, pricing, growth, and competitive decisions; `jb` is the first internal Client 0 for method validation
- Implementation status: no software implementation authorized
- Current product thesis source: `docs/decisions/turn_08_product_thesis_v0.md`

## Authority Boundary

Orca owns its project-specific facts, artifact folders, review lanes, validation gates, output contracts, and safety rules. Reusable workflow skills may be used only when they defer project facts to this overlay or fail visibly when the overlay is incomplete.

## Forbidden Drift

- Do not import `jb` project-specific assumptions as Orca authority.
- Do not turn migration notes into Orca product requirements.
- Do not create implementation scope from unknown project facts.
- Do not treat installed skills or copied skills as canonical skill source.
