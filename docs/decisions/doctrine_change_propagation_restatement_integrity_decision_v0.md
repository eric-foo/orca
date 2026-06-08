# Doctrine Change Propagation: Restatement-Integrity Decision v0

```yaml
retrieval_header_version: 1
artifact_role: Workflow doctrine decision
scope: Adds a restatement-integrity rule and an additive-only stale-language-search tightening to Orca's Doctrine Change Propagation Contract.
use_when:
  - Propagating a doctrine change into more than one surface and deciding whether to restate or reference it.
  - Deciding whether stale_language_search may be not_run for a given change.
  - Changing the Doctrine Change Propagation Contract and needing the controlling decision.
authority_boundary: retrieval_only
open_next:
  - .agents/workflow-overlay/source-of-truth.md
stale_if:
  - The Doctrine Change Propagation Contract owner text in source-of-truth.md is amended, narrowed, or superseded.
  - A later owner decision rejects or replaces the restatement-integrity rule or the additive-only stale-skip.
```

## Status And Decision

Status: `DOCTRINE_CHANGE_PROPAGATION_RESTATEMENT_INTEGRITY_DECIDED_V0` (accepted, owner-authorized).

Owner instruction basis: authorized in-session through the ORCA propagation-doctrine
completeness port handoff — port scope "Rule 1 + Rule 3", landing "dedicated change".

Decision: Orca's Doctrine Change Propagation Contract now (1) requires a
propagated restatement to stay faithful to the controlling source's strength —
it must not soften, narrow, or silently fork the controlling rule, and where the
same wording would otherwise be copied across surfaces it should point at the
single controlling source rather than duplicate it — and (2) allows
`stale_language_search` to be `not_run` only for a purely additive change; an
edit or supersede must run it.

This is a workflow-governance (`workflow_authority`) doctrine change. It is not
validation, readiness, review authority, implementation authorization, or source
promotion. The controlling, authoritative rule text lives solely in
`.agents/workflow-overlay/source-of-truth.md` (Doctrine Change Propagation
Contract); this record references it and does not own it.

## What Changed And Why

Orca's prior contract reliably required updating the controlling source and
checking downstream surfaces for stale doctrine, but had two narrow gaps:

- **No restatement-integrity rule.** The contract told an agent to find stale
  downstream language but never stated the standard that language is measured
  against: a downstream restatement must preserve the controlling rule's
  strength and must not silently fork it. Orca already practices
  reference-over-copy at the top level (`AGENTS.md` requires surfaces "not
  duplicate, fork, weaken, or override" Orca rules and to "load the owning
  overlay file instead of duplicating the rule here"), but that principle was
  not codified inside the propagation contract. This change codifies it there.
- **Stale-skip was not additive-restricted.** The receipt schema allowed
  `stale_language_search: not_run + why` for any change. An edit or supersede
  could therefore skip the stale search with only a stated reason. The schema
  now restricts `not_run` to a purely additive change.

The third candidate from the source port — owner sets for every governed
doctrine class — was evaluated and **not applied**, because Orca does not have
the gap it fixes. Orca's contract is already class-uniform: every one of its
seven trigger classes resolves the same way (update the controlling source for
that doctrine, check downstream surfaces), with no single privileged class and
no class left without a propagation surface. There is no owner hole to close.

## Provenance

This is a cross-repo port of a completeness change first made in a separate
repo (`jb`), carried in via a cold handoff packet. Per the packet's
confirm-don't-trust load contract, the two source commits were re-verified
before relying on them: the source overlay change and its decision record were
read at their commits and matched the inlined rule text. Only the
domain-agnostic shape was ported. The source repo's bindings — its owner-artifact
lists, route-family names, product-doctrine specifics, and class naming — were
deliberately excluded; none appear in Orca's contract or in this record. The
source repo's decision record is external precedent only and carries no Orca
authority.

## Honest Sizing

A completeness-and-consistency change to existing doctrine, not a new system.
Rule (1) is an additive paragraph; rule (2) is a one-line tightening of the
receipt-schema comment. Nothing in the prior contract — trigger vocabulary,
receipt or blocker schema, related_triggers grammar, inline-evidence rule, or
the propagation blocker — is removed or weakened. The owner text stays solely in
`source-of-truth.md`; every other surface references it. The change self-applies
the doctrine it edits: its own `direction_change_propagation` receipt is recorded
inline in `source-of-truth.md`, and because the edit is not purely additive the
`stale_language_search` was run, finding the receipt schema single-homed and no
conflicting downstream language.

## Files Changed

- `.agents/workflow-overlay/source-of-truth.md` — Doctrine Change Propagation
  Contract: added the restatement-integrity paragraph and the additive-only
  `stale_language_search` hint; appended the self-applied DCP receipt.
- This decision record.

## Non-Claims

- not validation
- not readiness
- not review authority
- not implementation authorization
- not source promotion
- not a skill, registry, automation, or broad template sweep
