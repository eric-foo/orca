# Decision: Ground-Truth Check Before Absence / Build-State Claims (Kernel Rule)

```yaml
retrieval_header_version: 1
artifact_role: Decision record
scope: >
  Records the owner-approved addition of one sentence to the AGENTS.md Agent
  Behavior Kernel: absence and build-state claims that are load-bearing and
  cheaply checkable must be confirmed against the primary source before being
  reported. Carries the direction_change_propagation receipt for that kernel edit.
use_when:
  - Checking why the AGENTS.md observed-facts rule now explicitly covers absence/build-state claims.
  - Deciding whether the deferred overlay companion (source-loading.md ground-truth pointer) should be added.
authority_boundary: retrieval_only
status: LOCKED
decided: 2026-06-09
open_next:
  - AGENTS.md
  - .agents/workflow-overlay/source-loading.md
```

## Decision

Added one sentence to the AGENTS.md `Agent Behavior Kernel`, immediately after
the existing "Report only observed facts…" rule:

> Absence and build-state are claims, not defaults: a doc that says something is
> missing, deferred, superseded, or done is a secondary report, not an
> observation of that state — when such a claim is load-bearing and cheaply
> checkable, confirm it against the primary source (the code, commits, repo map,
> or owning lane) before reporting it.

This **extends** the existing observed-facts rule (whose "status" term already
implied this); it does not add a competing rule. It closes a trigger gap: the
rule read as applying to one's *own* writes/commits, so it did not fire when
reporting another lane's or artifact's build-state from a doc.

## Why

A recurring failure: reporting something as a gap from a doc's wording without
checking where it would actually live. Concretely (2026-06-09): JSG-01's
SP-1/2/3/6 derivers were reported as an unbuilt "gap" because the conductor's
JSG-01 row said the derivers were "deferred" — but they were in fact built and
committed in the ECR lane (`orca-harness/ecr/`, commits
`d857c58`/`51f4193`/`14490ce`/`6329d71`), and the repo map already reflected
their existence. The conductor doc was stale; trusting it nearly shipped a false
build backlog.

## Scope and narrowness

The trigger is the **conjunction**, kept narrow on purpose so it is not
"verify every doc claim": (a) about to assert existence / absence / build-state
("missing / deferred / built / done"); **and** (b) load-bearing — the reader
will act on it; **and** (c) sourced from a secondary description (a doc
describing code or another lane), especially under its own `stale_if`; **and**
(d) the primary check is cheap (a repo-map lookup, a `git log -- <dir>`, an
`ls`). When all hold, do the seconds-long check first. Trivial,
non-load-bearing, or "the doc owns the thing" → no check.

## Deferred (not done in this change)

The optional overlay companion — naming the repo map (`orca_repo_map_v0.md`) as
the cheapest first cross-lane check, and lane precompacts + the code tree as
deeper ground truth, in `.agents/workflow-overlay/source-loading.md` — is a
deferrable enhancement, **not** added here. The kernel sentence is complete on
its own (it names the primary sources). Add the overlay companion only if the
kernel sentence proves insufficient in practice.

## direction_change_propagation

```yaml
direction_change_propagation:
  doctrine_changed: >
    AGENTS.md Agent Behavior Kernel gains one sentence extending the
    "report only observed facts" rule to absence/build-state claims: a doc
    asserting something is missing/deferred/superseded/done is a secondary
    report, not an observation, and a load-bearing + cheaply-checkable such claim
    must be confirmed against the primary source (code, commits, repo map, owning
    lane) before reporting. Governs all lanes. Owner-approved 2026-06-09.
  trigger: architecture_doctrine
  related_triggers:
    - validation_philosophy
  controlling_sources_updated:
    - AGENTS.md
  downstream_surfaces_checked:
    - CLAUDE.md  # shim imports AGENTS.md; unchanged, no duplication
    - .agents/workflow-overlay/source-loading.md  # overlay companion deferred, not changed
    - .agents/workflow-overlay/decision-routing.md  # doctrine-change routing owner; no rule change here
  non_claims:
    - not a new competing rule (extends the existing observed-facts rule)
    - not implementation, validation, readiness, or deployment
    - the overlay companion (source-loading.md pointer) is not added
    - no lane's source hierarchy, review lane, or validation gate changed
```
