# Company-Aggregate Forward-Signal — Architecture Decision (v0)

```yaml
retrieval_header_version: 1
artifact_role: Decision record
scope: >
  Owner-locked target architecture for the company headcount-aggregate forward-trend
  signal (org-motion net-adds realization): a source-agnostic signal core with
  official-first source adapters; the LinkedIn lane owns ONLY the company-page
  extraction adapter. Routes the sibling signal slice to the capture lane.
  Scope/architecture only; NOT a build authorization.
use_when:
  - The capture lane picks up the sibling company-aggregate signal slice.
  - Deciding the source for a company headcount-aggregate trend (official-first vs LinkedIn).
  - Scoping the LinkedIn company-aggregate extraction extension.
authority_boundary: retrieval_only
branch_or_commit: ecr-sp3-timing-deriver-slice1 (working tree dirty — shared/volatile; uncommitted)
stale_if:
  - The owner changes the official-first policy, the core/satellite split, or the posture recommendation.
  - The capture lane accepts/forks the sibling slice with a different boundary.
  - A build authorization supersedes this scope-only decision.
```

## Status

`SCOPE_ARCHITECTURE_DECISION_OWNER_LOCKED` (2026-06-11, in-thread). Not a build authorization, not validated, not source-of-truth promotion. A batch-local lock label, not an evidence-ladder claim tier.

## Decision (locked: AO-3)

The request was framed as "a LinkedIn signal." The locked architecture reframes it as a **source-agnostic company headcount-aggregate time series**, with sources as swappable adapters. LinkedIn is one adapter — the least-defensible one.

## Owner Locks (2026-06-11)

1. **AO-3** — split: source-agnostic signal core + source adapters; the LinkedIn lane owns only the LinkedIn extraction adapter.
2. **Official-first source policy** — Companies House (UK official annual employee count) and SEC EDGAR (US public) are preferred; **LinkedIn = fallback** for US-private / no-official-source only.
3. **Sibling slice routed to the capture lane** (Source Capture Armory / core-spine capture). **Not scoped or handled in this turn.**

## Core / Satellite Boundary

| Concern | Owner |
| --- | --- |
| Source-agnostic aggregate time-series record (entity-keyed; carries `source` + `capture-posture` tags) | Capture lane (sibling slice) |
| Periodic cadence, persistence, source-selection policy | Capture lane (sibling slice) |
| Companies House / SEC EDGAR adapters (official, preferred) | Capture lane (sibling slice) |
| LinkedIn company-page extraction (`numberOfEmployees` + size band + follower count) | **LinkedIn lane** (this lane) |

## This Lane's Piece

The LinkedIn company-aggregate **extraction adapter**: extend the existing `CompanySignal`/extractor (slice 3c-2b already pulls `display_name` + follower count) to also pull `numberOfEmployees` + size band. The JSON-LD `numberOfEmployees` integer was confirmed present in the company-page bytes (read-only probe, 2026-06-11). **Minimization verified** against the lane's `business_entity_only` rails: company aggregate only — no individuals, no follower/connection lists, no graphs, no profile/post content. **Ownable, but its build is NOT authorized by this record.**

## Posture (#1) — carried to the capture lane, not force-locked here

Periodic capture (the forward *trend*) is the high-lock-in axis. Recorded **recommendation**: the LinkedIn fallback runs **attended / low-frequency, posture-tagged — not a periodic-default scheduler**, preserving the legally-defensible long-term posture. This is the capture lane's build-time decision (it owns cadence); the owner may override then.

> Interpretation note: "yes — lock in" is read as locking AO-3 + official-first (LinkedIn = attended fallback; periodic NOT committed). It is **not** read as authorizing periodic/scheduled LinkedIn capture. If the owner meant to accept the periodic-LinkedIn lock-in for the US-private gap specifically, this section is the single line to flip.

## Beauty Pie #3 Reality Check

The forward LinkedIn trend does **not** serve Beauty Pie #3 — a *past UK* case whose net-adds proxy is **Companies House**, not a go-forward LinkedIn signal. This capability is **go-forward realization for future cases**; there is no urgency forcing the high-lock-in periodic-LinkedIn path now.

## Next

- Capture lane scopes the sibling company-aggregate slice (record shape, cadence, persistence, source-selection, official adapters) under the official-first policy + the attended-fallback posture recommendation. **Not in this turn.**
- This lane's LinkedIn extraction extension awaits its own bounded build authorization.

## Non-Claims

Scope/architecture only. No build or implementation authorized. Not validated, not ready, not buyer-proof. Does not bind the capture lane's eventual design beyond the owner-locked official-first policy and core/satellite split. Periodic/scheduled LinkedIn capture is **not** authorized by this record.
