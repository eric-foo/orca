# Artifact Roles

This file binds reusable artifact-role mechanics to Orca-owned paths. Generic workflow methods may request these roles, but Orca owns the concrete permissions, destinations, freshness checks, and validation evidence.

## Role Bindings

| Role | Authoritative source or destination | Read / write permission | Freshness marker | Paired artifacts | Validation evidence |
| --- | --- | --- | --- | --- | --- |
| Orca overlay authority | `.agents/workflow-overlay/` | Read for all Orca work; write only for explicit overlay maintenance | File contents plus git status | `AGENTS.md` | Source list and changed overlay files |
| Product thesis authority | `docs/decisions/turn_08_product_thesis_v0.md` | Read for planning; write only when explicitly updating the thesis | Decision ID, status, date, and hash when pinned | Product and feature planning prompts | Source list and decision status |
| Full prompt artifact | `docs/prompts/` or a typed child folder under it | Read/write docs-only prompt drafts | File path, version suffix, source list, and optional hash | Thin wrapper, review input, rerun prompt | Prompt validation gate result |
| Thin wrapper prompt | `docs/prompts/wrappers/` | Read/write docs-only wrapper drafts | Referenced full prompt path and hash or revision | Full prompt artifact | Wrapper-delta check |
| Planning handoff prompt | `docs/prompts/handoffs/` | Read/write docs-only handoff prompts | Work unit ID, target source revision, and output mode | Feature plan, implementation handoff, review input | Preflight check and validation plan |
| Review prompt | `docs/prompts/reviews/` or `docs/review-inputs/` | Read/write review requests; reviewers are read-only unless explicitly assigned patch execution | Source paths, hashes or revisions, and review lane | Review report | Review-lane and source-hash check |
| Rerun or patch prompt | `docs/prompts/reruns/` or `docs/prompts/patches/` | Read/write docs-only retry or patch prompts | Prior artifact path, prior hash or revision, frozen fields, mutable fields | Prior artifact, patch queue, review report | Rerun economy check |
| Review report | `docs/review-outputs/` | Read/write reviewer reports and verdicts | Reviewed artifact path and revision | Review prompt, patch queue | Verdict and findings list |
| Patch queue | `docs/review-inputs/` or `docs/workflows/` | Read/write ordered patch candidates; source changes require separate execution authority | Stable unit IDs and target files | Rerun prompt, review report, implementation handoff | Residual-work and validation-gate mapping |
| Workflow record | `docs/workflows/` | Read/write Orca workflow records | Date, source list, and hashes when material | Prompt artifacts, decisions, validation notes | Gate evidence and residuals |
| Product artifact | `docs/product/` | Read/write docs-only product contracts, product proof plans, evidence standards, source maps, satellite notes, and decision-memo shape drafts | File path, version suffix, source list, and decision status when applicable | Product planning prompts, feature planning prompts, decision records | Product artifact impact classification and source list |
| Hygiene queue | `docs/hygiene/` | Read/write docs-only triage queues and cleanup notes | Queue item ID, status, and target destination | Inbox material, prompt artifacts, product artifacts, workflow records | Triage status and promotion or disposal note |
| Inbox scratch | `docs/_inbox/` | Read/write temporary docs-only scratch; not authoritative | Creation note or queue item ID when retained | Hygiene queue | Promotion, archive, deletion, or `not authority` note |

## Protected Roles

- External workflow source under `C:\Users\vmon7\Desktop\projects\agent-workflow\` is read-only from Orca work unless a later turn explicitly authorizes workflow-kernel source changes.
- Installed global, user-level, plugin, and project-local skills are deployment copies or tools, not Orca project authority.
- `jb` project rules, paths, handoffs, GAP/CV Engine policy, lifecycle mechanics, and repo-local skills are not Orca artifact roles.
- Material in `docs/_inbox/` is not Orca authority until promoted into an accepted docs folder or overlay file.

## Failure States

- `BLOCKED_UNBOUND_ARTIFACT_ROLE`: a prompt or workflow references a role not listed here or in another accepted Orca overlay file.
- `BLOCKED_ROLE_PERMISSION`: requested work exceeds the role permission.
- `BLOCKED_ROLE_DRIFT`: a role points to stale, missing, or conflicting evidence.
