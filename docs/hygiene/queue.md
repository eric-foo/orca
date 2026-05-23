# Orca Hygiene Queue

```yaml
retrieval_header_version: 1
artifact_role: Hygiene queue
scope: Triage queue for parked or temporary Orca docs-first material.
use_when:
  - Deciding whether parked material should be promoted, moved, archived, or deleted.
  - Checking unresolved docs-first folder or artifact drift.
authority_boundary: retrieval_only
```

Use this queue for temporary or parked docs-first material that needs later
triage. Queue entries are non-canonical routing records. They do not prove
validation, approval, readiness, product proof, lifecycle completion,
source-of-truth status, or edit permission.

Each retained item should include created date, source or owner/source lane when
inferable, current location, reason retained, non-canonical boundary, promotion
destination when known, review or removal condition, `review_by` or
`expires_on`, and status.

| ID | Created | Source / Owner Lane | Current Location | Reason Retained | Non-Canonical Boundary | Promote To | Review Or Removal Condition | Review By / Expires On | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ORCA-HYGIENE-001 | Unknown; logged before 2026-05-24 | Current working tree folder drift | `docs/prompts/hygiene-queue/` | Folder exists with parked precompact prompt material but is not listed as an accepted prompt-family folder in the overlay. | Not an accepted Orca prompt-family folder; not Orca authority. | `docs/hygiene/`, an accepted `docs/prompts/` child folder, or overlay-maintenance update | Decide whether to move the material, promote a prompt-family folder, or archive it as scratch. | `review_by: 2026-06-07` | Open |
