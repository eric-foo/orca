# Project Authority

## Identity

- Project/workspace: Orca
- Stage: docs-first bootstrap
- Relationship to `jb`: separate workspace; no inherited project authority
- Product/domain purpose: UNKNOWN - requires owner input
- Target users/operators: UNKNOWN - requires owner input
- Implementation status: no software implementation authorized

## Authority Boundary

Orca owns its project-specific facts, artifact folders, review lanes, validation gates, output contracts, and safety rules. Reusable workflow skills may be used only when they defer project facts to this overlay or fail visibly when the overlay is incomplete.

## Forbidden Drift

- Do not import `jb` project-specific assumptions as Orca authority.
- Do not turn migration notes into Orca product requirements.
- Do not create implementation scope from unknown project facts.
- Do not treat installed skills or copied skills as canonical workflow-kernel source.
