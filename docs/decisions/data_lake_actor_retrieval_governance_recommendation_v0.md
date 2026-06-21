# Data Lake Actor-Retrieval Governance Recommendation v0

```yaml
retrieval_header_version: 1
artifact_role: Owner-policy recommendation (PENDING owner adjudication; not adopted)
scope: >
  Recommended access, audit, retention, and identifier-scope guardrails for on-demand
  actor/commenter/reviewer timing retrieval in the Data Lake indexes/derived_retrieval
  lane, keeping it non-dossier per the medallion gold-readiness contract.
  Recommendation only; the owner (with legal/privacy review) adjudicates; the
  derived_retrieval lane stays blocked until adoption.
use_when:
  - Owner adjudication of actor-retrieval guardrails before any derived_retrieval build.
  - Checking whether a proposed retrieval surface stays non-dossier.
open_next:
  - orca/product/spines/data_lake/authority/core_spine_v0_data_lake_medallion_gold_readiness_contract_v0.md
  - orca/product/spines/data_lake/authority/core_spine_v0_data_lake_physicality_location_contract_v0.md
stale_if:
  - The owner adopts, amends, or rejects this recommendation.
  - The medallion gold-readiness contract changes the actor-timing-retrieval boundary.
authority_boundary: retrieval_only
```

## Status

`RECOMMENDATION_PENDING_OWNER_ADJUDICATION`. Addresses Physicality Location Contract
blocker 6 (actor-related access/audit/retention + identifier scopes) as a
**recommendation only**.

This is NOT an adopted policy, NOT legal advice, NOT validation/readiness, and NOT
implementation authorization. The `indexes/derived_retrieval` actor-retrieval lane
stays blocked until the owner — with legal/privacy review — adopts guardrail wording.
Produced by an external blocker-resolution lane and adjudicated as faithful to the
medallion contract's Actor Timing Retrieval boundary.

## Recommended Guardrails (for owner adjudication)

- **Access:** internal decision workflows only; every invocation carries a bound,
  registered decision question (from an owner-approved enumeration); no freeform "show
  everything"; one exact identifier per call; no public/anonymous path.
- **Audit:** write-before-return (a failed audit write blocks the retrieval); log
  caller, decision question, identifier scope, time window, profile/version, result
  row count, cache-hit, timestamp, and an elevated-volume flag; append-only,
  immutable, retained beyond result caches.
- **Retention:** result caches expire at a short owner-set TTL (recommended <= 30
  days, 7 preferred), measured from derivation (not last access); on-demand deletion
  required; no migration/export into any durable actor store; audit logs outlive
  caches. Underlying raw stays intact and rebuildable — reconstruction on demand is
  not "retention" of an actor history.
- **Identifier scope:** exact public identifier + single source-family namespace +
  bounded observation window only; no cross-namespace/cross-platform join; explicit
  rejections — cross-platform identity merge, canonical/legal person identity, device
  fingerprint, retrieval anchored on a risk score or prior label. New namespaces
  require an explicit owner decision.
- **Dossier hard stops (no override):** (1) no bound decision question -> fail; (2)
  scope beyond single-namespace exact-identifier -> fail; (3) no write path from
  results to a profile store, actor database, or adverse-action/outreach surface; (4)
  no unbounded-TTL cache; (5) no build on the derived_retrieval path before owner
  adoption.
- **Forbidden outputs (per medallion):** persistent all-history actor profile; "show
  everything this person did"; cross-platform identity merge; actor risk score;
  bot/fake/paid/coordinated label; credibility/exclusion recommendation;
  adverse-action/outreach surface.

## Owner Decisions Required (only the owner can make these)

1. Legal/privacy clearance (PDPA at minimum; GDPR applicability if EU-facing) — with counsel.
2. The permitted decision-question enumeration.
3. Result-cache TTL value and audit-log retention duration.
4. Elevated-volume threshold for flagging.
5. Whether to adopt the full MGT guardrail set or the SCI floor.
6. Formal adoption of guardrail wording (the adoption act itself).

Until 1-6 are decided, the `derived_retrieval` actor-retrieval lane remains blocked.

## Accepted Residuals (recommendation-level, MGT)

- Automated TTL deletion not yet built (no caches exist until the lane is built;
  trigger: lane build makes automated TTL mandatory).
- Anomaly detection procedural, not automated (trigger: volume exceeds owner threshold).
- Cross-namespace enforcement procedural until a query layer exists (trigger:
  query-layer design makes it a structural pre-execution check).
- New-namespace onboarding process not yet formalized (trigger: before a second namespace).

## Non-Claims

Not an adopted policy, not legal advice, not validation/readiness, not implementation
authorization. Does not clear PDPA/GDPR or any privacy regime. Does not authorize
bypassing legal/privacy review. Governs only actor timing retrieval in the
`derived_retrieval` lane; not the full statement of Orca data governance.
