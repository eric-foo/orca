# Single-Acquisition Screened Capture Probe Spec v0

```yaml
retrieval_header_version: 1
artifact_role: Workflow specification
scope: >
  Specifies the target joint scanning/capture probe posture: one bounded public
  acquisition per URL, in-memory screening, explicit commit-or-discard, and
  capture packet commit only after a promotion gate passes.
use_when:
  - Choosing the default posture for an uncertain public page or venue that may be worth capture.
  - Scoping the build that combines screening evaluation with capture commit discipline.
  - Explaining how scanning evidence should feed a focused capture probe without double-visiting the same URL.
authority_boundary: retrieval_only
open_next:
  - docs/workflows/screening_read_service_build_receipt_v0.md
  - docs/workflows/screening_read_reusable_findings_v0.md
  - docs/decisions/screening_reddit_read_route_decision_v0.md
  - docs/decisions/data_capture_spine_source_access_tooling_build_authorization_v0.md
  - orca/product/spines/capture/core/source_capture_toolbox/source_capture_playbook_v0.md
  - orca/product/spines/foundation/vertical_exploration/orca_vertical_exploration_guide_v0.md
branch_or_commit: codex/screening-read-service-build @ 96cfb3b8687e1ed2aaec8d881031d1c549eff097 at spec start
stale_if:
  - The screening-read service boundary changes.
  - The Source Capture Packet commit lifecycle or packet core contract changes.
  - The source-access boundary, public-only posture, or no-standing-crawler rule changes.
  - A later decision implements or supersedes single-acquisition delayed commit.
```

## Start Preflight

```text
orca_start_preflight:
  agents_read: yes
  overlay_read: yes
  source_pack: custom
  edit_permission: docs-write
  target_scope: workflow spec for a joint scanning/capture probe posture; no code, no runtime execution, no capture run
  dirty_state_checked: yes
  blocked_if_missing: source-access build authorization, screening-read receipt, capture playbook, route decision
```

## Status

Status: `TARGET_SPEC_PENDING_IMPLEMENTATION`.

This is a workflow specification and routing target. It is not implemented by
the current screening-read build, does not authorize a live probe, does not
grant network approval, and does not make any Source Capture Packet, ECR,
Cleaning, Judgment, validation, readiness, or source-quality claim.

## Direct Answer

The intended default for uncertain public source/venue probes is not pure
screening and not capture-by-vibe. It is a **single-acquisition screened capture
probe**:

```text
plan_bounded_probe
  -> entitlement_gate
  -> ephemeral_acquire_once_per_url
  -> screen_and_extract_in_memory
  -> gate_decision
      -> discard_screen_light_only
      -> commit_same_acquired_artifact_as_capture_packet
```

The reason is site-count minimization. If the same URL is first screened and
then fetched again for capture, Orca pays twice in latency, block risk, page
state drift, and source attention. For challenge-walled or rate-sensitive sites,
the second visit can be the thing that kills the run.

The key reframing:

**Capture is the durable commit state, not the act of fetching.**

Before commit, acquisition is ephemeral and in memory. It may be used to decide
whether the page is worth preserving, but it must not write raw body, DOM,
screenshot, packet, manifest, ECR, Cleaning, Judgment, or source artifact.
After commit, the same acquired artifact enters the normal Source Capture Packet
path with provenance and limitations.

## What This Combines

This is deliberately a joint scanning/capture posture.

Scanning contributes:

- the source/venue question;
- the frontier choice and bounded probe set;
- the fields needed to decide whether the page is useful;
- the candidate/venue-potential interpretation;
- the negative set and screen-light receipt.

Capture contributes:

- the entitlement and access-control discipline;
- the acquisition route and anti-block/browser rung;
- the packet commit boundary;
- the no-ECR/no-Cleaning/no-Judgment separation;
- the receipt of what was preserved and why.

The orchestrator owns the transition:

- walkers do not call screening-read or capture entries directly;
- no standing service, crawler, scheduler, monitor, dashboard, or production
  runtime is created;
- every probe has a declared source unit, question, cap, gate policy, and stop
  condition;
- promotion to packet commit is explicit, testable, and recorded.

## Default Postures

| Situation | Default posture | Why |
| --- | --- | --- |
| Quick venue exploration where no durable evidence is likely needed | Pure screening read | Lowest cost; no packet or raw artifact. |
| Uncertain public page/venue where evidence may be valuable and repeat visits are costly | Single-acquisition screened capture probe | One visit per URL; discard or commit the same acquisition. |
| Adapter/rung cannot yet preserve an ephemeral artifact through the commit gate | Screen-gated separate capture fallback | Keeps boundaries correct while accepting a second visit as a named residual. |
| Source is already admitted/high-confidence, volatile, or the task starts with a durable evidence need | Direct capture | Screening would only add delay and risk drift. |
| Broad discovery, standing watch, site-wide walking, or feed monitoring | Not allowed by this spec | Violates the bounded source unit and no-standing-runtime rules. |

The current implemented `screening_read(...)` and `screening_browser_read(...)`
remain pure screening entries. They are not silently upgraded to capture. A
future build should add a separate orchestrator entry for this probe posture,
rather than hiding packet side effects inside the screening entry.

## Probe Unit

A probe unit is a bounded source/venue question, not an open crawl. It must
declare all of these before any acquisition:

- `probe_id`;
- source family or venue;
- operator question;
- allowed route family;
- public entitlement posture;
- candidate URL set or listing seed;
- maximum URL count;
- maximum captures;
- required extracted fields;
- gate policy version;
- stop condition.

The normal venue-probe shape is:

```text
listing_or_search_page: 1
candidate_detail_pages: top N from targeted row-local extraction
optional_control_or_near_miss: 0 or 1
```

Each URL gets one `url_key` and one acquisition attempt under the declared
route, unless a retry is explicitly part of the route's human-rate error
handling. The same URL must not be fetched once for screening and then fetched
again for the same gate decision.

## Gate Contract

The gate is not "feels okay." It is explicit criteria over the ephemeral
screened result.

Minimum gate fields:

- bounded dispatch: non-empty `probe_id`, source/venue id, source URL, question,
  route, cap, and gate policy version;
- public entitlement: logged-out public or legitimately entitled public-view
  access only; no private, auth-gated, paywalled, cross-account, stolen-cookie,
  or access-control bypass;
- access result: successful fetch/render, non-empty visible text or body, no
  login shell, no `BLOCK_SHELL`, no access-block reason;
- content class: declared class is eligible for this probe; `content_unverified`
  may be eligible but must not become a source-verification claim;
- required extraction: targeted fields declared before acquisition are present,
  row-local, canonicalized where needed, and range-sane;
- evidence need: the page would materially improve a candidate, venue-potential
  assessment, source-quality pass, or later capture recipe;
- side-effect check: packet, manifest, raw artifact, screenshot artifact, ECR,
  Cleaning, and Judgment writes are zero before the gate passes.

Gate outcomes:

- `discard`: keep only allowed screen-light metadata or the calling screen's
  normal provenance row; discard raw source artifact from memory.
- `commit_packet`: commit the same acquired artifact into the normal Source
  Capture Packet path, with `triggered_by_screening=true`, the gate policy
  version, and gate reasons.
- `fallback_capture_required`: the page looks valuable, but this route cannot
  single-acquisition commit yet; invoke a separate capture run only if the
  orchestrator accepts the named double-visit residual.
- `stop_blocked_or_gated`: do not escalate past the source-access boundary.

## State Machine

```text
probe_planned
  -> entitlement_gate
      -> refused_not_public_or_not_entitled
      -> ephemeral_acquire
          -> screen_evaluate
              -> discard
                  -> screen_light_receipt_only
              -> commit_authorized
                  -> packet_committed
              -> fallback_capture_required
                  -> separate_capture_invoked
              -> blocked_or_shell
                  -> screen_light_access_note_only
```

Invariants:

- `packet_committed` is unreachable without `commit_authorized`.
- `commit_authorized` is unreachable without a gate policy version and reasons.
- `screen_light_receipt_only` must not contain raw body, DOM, screenshot, packet
  path, manifest, ECR fields, Cleaning fields, Judgment fields, or source score.
- `separate_capture_invoked` must declare that it is a second visit and why the
  single-acquisition path was unavailable.

## Venue-Potential Receipt

The probe should return a screen-light venue-potential receipt so the capture
lane does not stop after one lucky or unlucky page.

Receipt fields:

- probe id, source family, venue, bounded question, route, cap, and gate policy
  version;
- for each URL: URL key, final URL, status, byte count or visible-text length,
  content class, block-shell/access state, extracted candidate fields, gate
  outcome, and packet pointer only when committed;
- aggregate: productive URL count, committed packet count, discard count,
  blocked count, signal density, observed access cost, rate/backoff notes,
  recommended next action.

Recommended next actions:

- `ignore_or_no_go`: no productive public signal inside the cap;
- `try_later_or_archive`: live access unstable but source may matter;
- `recipe_card_candidate`: route worked and should become a reusable capture
  recipe after a dedicated capture pass;
- `probe_more_bounded`: enough signal density to justify another declared probe;
- `direct_capture_candidate`: future runs may skip screening for this source
  class under declared admission criteria.

This receipt is not ECR, Cleaning, Judgment, source-quality scoring, fixture
admission, source completeness proof, or buyer proof.

## Why This Beats The Alternatives

Compared with pure screening, this keeps the cheap evaluation step but avoids
the common double-read when the same page becomes worth preserving.

Compared with direct capture, this avoids filling scratch packets with junk and
requires the gate to prove why a page deserves durable preservation.

Compared with screen-gated separate capture, this avoids the second visit and
the page-state drift between screen and capture.

Compared with boundary-collapse capture, this preserves auditability. No
screening entry silently writes packets. The commit boundary is a real state
transition with tests.

Compared with "one subagent captures one page and stops," this gives the
orchestrator a bounded venue-probe set and a venue-potential receipt. The output
can say "this venue has enough signal density to probe more" instead of treating
one page as the whole site.

## Example

Old way:

1. A scanning lane screens a public fragrance forum page through a browser rung.
2. The page looks promising.
3. A capture lane later opens the same URL again to make a packet.
4. The second open hits a stricter interstitial or returns a changed page.

New target:

1. The orchestrator declares a bounded fragrance-forum probe: one listing page,
   top three row-local candidate detail URLs, maximum two packet commits.
2. Capture-owned acquisition renders each URL once, in memory.
3. Screening-owned evaluation runs over visible text and targeted row-local
   extraction.
4. The gate commits the same acquired artifact for the one detail page that
   carries the required source-native signal and discards the rest.
5. The venue-potential receipt says the forum deserves another bounded probe,
   rather than pretending one captured URL proves venue quality.

## Accepted Residuals

| Residual | Why accepted now | Risk | Upgrade trigger |
| --- | --- | --- | --- |
| No implementation exists yet for delayed commit | Current branch proved pure screening reads, not commit semantics | Agents may fall back to double-read screen-gated capture | Build is commissioned, or duplicate visits become recurring blocker/cost |
| Some adapters may not expose a reusable in-memory artifact | Keeps the spec honest across HTTP and browser routes | Valuable pages still need second visit fallback | A route is used often enough to warrant an ephemeral artifact interface |
| The venue-potential receipt is screen-light only | Avoids hidden capture and ECR-like derived records | It may omit source nuance that only a packet would preserve | Repeated "interesting but discarded" receipts force a lower gate threshold or direct capture rule |
| Gate criteria may reject useful subtle pages | Targeted fields beat vague semantic scoring for first build | False negatives in exploratory screens | Manual override count becomes material and reviewable |
| No standing venue memory is introduced | Preserves the rejected registry/monitor boundary | Productive venues may need repeated bounded probes | Promote-on-reuse or a later source-card decision fires |
| Crash before commit loses the ephemeral artifact | No packet existed yet, so loss is preferable to hidden durability | A valuable page can disappear between runs | Crash-before-commit frequency or volatility becomes material |

## Build Requirements Before Implementation

A later build prompt must not target `screening_read(...)` directly as the
packet-writing entry. It should add a separate orchestrator-invoked entry, for
example `screened_capture_probe(...)`, that composes existing adapters and
packet commit code while keeping the commit gate explicit.

Minimum implementation requirements:

- no packet/manifest/raw artifact/ECR writes before gate pass;
- one acquisition per URL for the same probe decision;
- commit uses the same bytes/rendered artifact that screening evaluated;
- discard path leaves no source artifact behind;
- crash-before-commit leaves no packet or manifest;
- commit is idempotent or fails visibly on repeated commit attempt;
- fallback separate capture declares the second visit and accepted residual;
- human-rate, public-only, no-auth-bypass, no standing service;
- no walker-direct invocation.

## Test Requirements

Required contract tests:

- entitlement gate refuses private/auth/login/access-controlled URLs before
  acquisition;
- no durable source artifacts before gate pass, including crash and exception
  paths;
- discard path writes no packet, manifest, raw body, screenshot, ECR, Cleaning,
  or Judgment artifact;
- commit path writes exactly one packet from the same acquired artifact hash or
  route-native identity;
- no double-fetch for a URL inside one probe decision;
- fallback path records the second-visit residual;
- block-shell is classified on visible text for browser routes;
- structured extraction uses row-local locators and range sanity;
- probe caps stop listing and detail expansion;
- venue-potential receipt never contains raw source body/DOM/screenshot for
  discarded URLs;
- direct capture exceptions require declared admission/high-confidence criteria.

## Non-Claims

This spec is not validation, readiness, implementation authorization, network
approval, legal sufficiency, source completeness proof, source-quality scoring,
fixture admission, source-of-truth promotion, production runtime, broad crawler
authorization, ECR, Cleaning, Judgment, buyer proof, or commercial fetch
permission.

## Direction Change Propagation

```yaml
direction_change_propagation:
  doctrine_changed: >
    Orca adds a target default for uncertain public source/venue probes:
    single-acquisition screened capture, where scanning owns the bounded
    question/evaluation, capture owns acquisition/commit discipline, and one
    public acquisition is either explicitly committed as a packet or discarded.
  trigger: workflow_authority
  related_triggers:
    - architecture_doctrine
    - lifecycle_boundary
    - output_authority
  controlling_sources_updated:
    - docs/workflows/single_acquisition_screened_capture_probe_spec_v0.md
    - docs/workflows/data_capture_spine_consolidation_map_v0.md
    - docs/workflows/orca_repo_map_v0.md
    - orca/product/spines/capture/core/source_capture_toolbox/README.md
    - docs/prompts/deep-thinking/screening_capture_hybrid_mgt_strategy_prompt_v0.md
  downstream_surfaces_checked:
    - AGENTS.md
    - .agents/workflow-overlay/README.md
    - .agents/workflow-overlay/source-loading.md
    - .agents/workflow-overlay/source-of-truth.md
    - docs/decisions/screening_reddit_read_route_decision_v0.md
    - docs/workflows/screening_read_service_build_receipt_v0.md
    - docs/workflows/screening_read_reusable_findings_v0.md
    - docs/decisions/data_capture_spine_source_access_tooling_build_authorization_v0.md
    - orca/product/spines/capture/core/source_capture_toolbox/source_capture_playbook_v0.md
    - orca/product/spines/foundation/vertical_exploration/orca_vertical_exploration_guide_v0.md
  intentionally_not_updated:
    - path: docs/decisions/screening_reddit_read_route_decision_v0.md
      reason: >
        It records the implemented pure screening-read route. This spec does
        not change `screening_read(...)`; it defines a future separate probe
        posture.
    - path: docs/workflows/screening_read_service_build_receipt_v0.md
      reason: >
        The build receipt must stay faithful to current implementation:
        screening entries remain no-packet/no-ECR.
    - path: .agents/workflow-overlay/source-loading.md
      reason: >
        Source-loading already routes capture-spine activity through the Data
        Capture submap and capture playbook; the submap is updated rather than
        adding another read-pack rule.
    - path: orca/product/spines/capture/core/source_capture_toolbox/source_capture_playbook_v0.md
      reason: >
        The capture method still owns route diagnosis and packet-grade capture.
        This spec composes with that method but does not amend route catalog or
        risk posture.
    - path: orca/product/spines/foundation/vertical_exploration/orca_vertical_exploration_guide_v0.md
      reason: >
        Walker prompts remain screening-only and walker-direct capture remains
        forbidden. The orchestrator/capture side is routed through the maps and
        this spec.
  stale_language_search: >
    rg -n "screen-gated capture|single-read delayed|delayed-commit|single-acquisition|screening_capture_hybrid|capture if it feels okay"
    docs/workflows docs/prompts orca/product/spines/capture/core/source_capture_toolbox/README.md
    orca/product/spines/foundation/vertical_exploration/orca_vertical_exploration_guide_v0.md
    .agents/workflow-overlay/source-loading.md
  stale_language_search_result: >
    Executed 2026-06-21 after the spec patch. Remaining hits are the new spec
    itself and the historical ChatGPT strategy prompt. The prompt now carries a
    supersession note and `superseded_by` pointer to this spec, so its older
    "screen-gated now / delayed commit later" starting hypothesis is no longer
    live guidance.
  non_claims:
    - not validation
    - not readiness
    - not implementation authorization
    - not network approval
    - not Source Capture Packet output by screening_read
    - not ECR, Cleaning, or Judgment design
```
