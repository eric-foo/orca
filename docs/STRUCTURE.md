# Orca Docs Structure

This file is a quick usage guide for future agents. The Orca overlay in `.agents/workflow-overlay/` remains the authority if anything here conflicts with it.

## Rule Of Thumb

Keep Orca docs-first. Do not create implementation folders, runtimes, packages, tests, scrapers, or automation unless a later turn explicitly authorizes implementation.

## Core Folders

- `docs/decisions/`: accepted or proposed decision records.
- `docs/product/`: product contracts, Core Spine notes, satellite notes, evidence standards, source maps, proof plans, and decision-memo shape drafts.
- `docs/prompts/`: reusable prompt artifacts and typed prompt families.
- `docs/review-inputs/`: artifacts prepared for review.
- `docs/review-outputs/`: reviewer reports and verdicts.
- `docs/workflows/`: workflow records, validation notes, and operational records.
- `docs/migration/`: migration and import planning records.
- `docs/hygiene/`: triage queues and cleanup notes.
- `docs/_inbox/`: temporary holding area for untriaged prompts, notes, imports, and scratch material.

## Core And Satellite Product Work

Use `docs/product/` for the Core + Satellite model:

- Core Spine artifacts define market-agnostic evidence mechanics.
- Satellite artifacts define decision-specific and domain-specific context.
- Client 0 `jb` material is a satellite proof case, not the product center.

Do not promote `jb`-specific assumptions into core unless a product artifact explicitly argues why the concept generalizes.

## Inbox And Hygiene

`docs/_inbox/` is not authoritative. Material placed there must be promoted, archived, deleted, or left explicitly parked through `docs/hygiene/queue.md` when it matters.

Use this promotion rule:

- product truth -> `docs/product/` or `docs/decisions/`
- prompt artifact -> `docs/prompts/`
- workflow record -> `docs/workflows/`
- review input or output -> `docs/review-inputs/` or `docs/review-outputs/`
- migration/import note -> `docs/migration/`

If an item is useful but unresolved, keep it in `_inbox/` and add a hygiene queue entry.
