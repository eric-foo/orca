# Fragrance Purchase-Review Site Registry v0

```yaml
retrieval_header_version: 1
artifact_role: Capture source registry / current operating surface
scope: Current operating registry for the fragrance purchase-review Retail/PDP lane: which sites are in the v0 capture set, which are rescue-only, and which route to use.
use_when:
  - Selecting fragrance purchase-review PDP sources for row-level capture.
  - Checking the current route/status for Luckyscent, Twisted Lily, Ministry of Scent, ZGO, or Indigo.
  - Distinguishing the current operating set from the historical recon evidence ledger.
authority_boundary: retrieval_only; no live capture, adapter build, scraping scale, ECR, Cleaning, Judgment, or source-quality scoring authority.
open_next:
  - orca/product/spines/capture/core/source_families/retail_pdp/fragrance_purchase_review_row_contract_v0.md
  - orca/product/spines/capture/core/source_families/retail_pdp/fragrance_purchase_review_retailer_recon_v0.md
  - orca/product/spines/capture/core/source_capture_toolbox/source_capture_playbook_v0.md
  - orca/product/spines/capture/core/source_capture_toolbox/capture_recon_index_v0.md
stale_if:
  - A later probe changes any source route, status, or row-level verdict below.
  - A primary source stops exposing review rows under the pinned route.
  - ZGO or Indigo is re-probed with a known-reviewed SKU and moves into or out of primary status.
  - The review-row contract changes the minimum fields needed for v0 capture.
```

## Decision

Yes: this lane should have a site registry. It should not replace the recon index.

- `capture_recon_index_v0.md` is the evidence ledger: what has been probed, where
  the detailed card lives, and what verdict was reported.
- This registry is the current operating surface: what to use now, what route to
  run, what is excluded from the v0 capture set, and what must be true before a
  source changes status.

This avoids treating a long recon index as a runbook. The registry is the thin
source-of-current-truth; recon remains the proof behind it.

## Current Capture Set

Status: `FRAGRANCE_PURCHASE_REVIEW_SET_V0_LOCKED`.

Primary row-level capture set for the first pilot:

1. Ministry of Scent
2. Luckyscent / Scent Bar
3. Twisted Lily

Rescue queue, not in the first row-capture set:

1. ZGO Perfumery
2. Indigo Perfumery

The reason is not brand quality. The reason is row substrate. The first three
sampled sources exposed usable row-level purchase-review bodies. ZGO and Indigo
sampled PDPs preserved PDP/review-widget shells but did not expose review bodies
after Direct HTTP, anti_blocking_http rung 1, curl_cffi rung 2 diagnostic, and
CloakBrowser checks.

## Registry

| Source ID | Site | Current status | Route pin | Sampled fixture | Row substrate | Use now | Required next fact to change status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `fragrance_retail_ministry_of_scent` | Ministry of Scent | `LOCKED_PRIMARY_V0` | Direct HTTP first; CloakBrowser only if rows disappear or lazy-load appears. | `https://ministryofscent.com/products/memoirs-of-a-trespasser` | Static HTML exposed Judge.me row bodies (`jdgm-rev__body`) plus verified/source-app/product metadata. | Use as the cheapest row-capture source. | Re-probe if Judge.me markup or PDP template changes. |
| `fragrance_retail_luckyscent` | Luckyscent / Scent Bar | `LOCKED_PRIMARY_V0` | Direct HTTP aggregate control, then CloakBrowser with `--settle-seconds 5 --scroll-step-px 500 --scroll-passes 4` for rows. | `https://www.luckyscent.com/products/memoirs-of-a-trespasser-by-imaginary-authors` | Rendered review rows exposed body text, dates, reviewer labels, country, variant, verified/store-invitation labels. | Use for rendered row capture. | Re-probe if render+scroll stops loading row bodies or only aggregate JSON remains. |
| `fragrance_retail_twisted_lily` | Twisted Lily | `LOCKED_PRIMARY_V0` | Direct HTTP aggregate/config control, then CloakBrowser with `--settle-seconds 5 --scroll-step-px 500 --scroll-passes 4` for rows. Record final variant URL when Shopify normalizes it. | `https://twistedlily.com/products/essential-parfums-discovery-set-1` | Rendered review rows exposed body text, rating summary, reviewer names, dates, verified/location labels, and Shop App labels. | Use for rendered row capture. | Re-probe if rendered rows become config-only or variant routing changes target product binding. |
| `fragrance_retail_zgo` | ZGO Perfumery | `RESCUE_QUEUE_KNOWN_REVIEWED_SKU_REQUIRED` | Keep PDP shell packet only; do not run row extraction on sampled fixture. | `https://zgoperfumery.com/products/diptyque-orpheon-eau-de-parfum` | Sampled product exposed Yotpo/widget config and zero-count review substrate, but no row bodies. | Do not use in first row-capture set. | A known-reviewed SKU must expose review row bodies under bounded re-probe. |
| `fragrance_retail_indigo` | Indigo Perfumery | `RESCUE_QUEUE_KNOWN_REVIEWED_SKU_REQUIRED` | CloakBrowser for page access; Direct HTTP and anti_blocking_http hit local certificate verification failure in this environment. | `https://indigoperfumery.com/products/memoirs-of-a-trespasser` | Sampled product exposed review container posture, but no row bodies. curl_cffi reached HTTP 200 but still no rows. | Do not use in first row-capture set. | A known-reviewed SKU must expose review row bodies under bounded re-probe. |

## Promotion Rule

A source enters `LOCKED_PRIMARY_V0` only when a sampled public PDP exposes actual
review row bodies, not only aggregate counts, review-widget configuration, CSS,
empty containers, or zero-count widget state. The row must be capturable into
`candidate_fragrance_review_row_v0` with raw source anchors and per-field
residuals.

A source stays in rescue status when the only preserved evidence is a PDP shell,
review container, aggregate count, widget script/config, or empty/no-review
state. A second product fixture is allowed only when there is a new fact that it
is known to have reviews.

## Route Policy

Do not blindly climb every rung on every run. Use the pinned cheapest route that
preserved row bodies for that source, with Direct HTTP as a cheap control where
useful.

Run intermediate rungs again only when the failure signature points to that
hypothesis:

| Symptom | Recheck route |
| --- | --- |
| Static page returns aggregate/config only, but rendered widget likely holds rows | CloakBrowser render+scroll. |
| Direct HTTP fails or changes with UA/header-sensitive behavior | `anti_blocking_http` rung 1. |
| Passive TLS/JA3 fingerprint wall suspected and no JS/render dependency is evident | `curl_cffi` rung 2, once a packeted runner exists or as a clearly marked diagnostic. |
| Rendered route returns shell/no rows | Known-reviewed-SKU re-probe before source-wide NO-GO. |

For this lane, rung 1 and the ad hoc rung 2 diagnostic did not unlock ZGO or
Indigo. That is why they remain rescue-only.

## Pilot Unit

The first pilot should capture one row-producing PDP per primary source and emit
packet-local candidate rows under
`fragrance_purchase_review_row_contract_v0.md`.

Pilot success is not source-wide coverage. It is only proof that the three-source
v0 set can produce review rows with body text, provenance, product binding,
source-visible metadata, and explicit residuals.

## Non-Claims

- Not a claim that the three primary sources are the best fragrance sources.
- Not a source-wide completeness claim for any retailer.
- Not a durable Attachment Record implementation plan.
- Not ECR, Cleaning, Judgment, pain/pleasure labeling, review integrity scoring,
  or buyer proof.
- Not authorization for scaled scraping, auth bypass, challenge solving, or a
  standing crawler.