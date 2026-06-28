# Fragrance Purchase-Review Retailer Recon v0

```yaml
artifact_role: Capture recon / route pin
scope: Single-fixture source-capture recon for niche fragrance retailer PDP purchase-review surfaces.
use_when:
  - Capturing purchase reviews from fragrance-specialist retailers.
  - Deciding whether to use Direct HTTP or CloakBrowser before downstream review integrity analysis.
  - Explaining why a sampled retailer is GO, PARTIAL, or not yet pinned for row-level review capture.
authority_boundary: Retrieval-only. This artifact does not score review integrity, infer sentiment, normalize products, or certify source-wide completeness.
open_next:
  - orca/product/spines/capture/core/source_capture_toolbox/source_capture_playbook_v0.md
  - orca/product/spines/capture/core/source_capture_toolbox/capture_recon_index_v0.md
  - orca-harness/docs/source_capture_agent_runbook.md
stale_if:
  - Retailer review vendor, PDP template, or anti-bot posture changes materially.
  - CloakBrowser or Direct HTTP packet schema changes.
  - A second fixture contradicts the sampled verdict below.
```

## Boundary

This is a capture-routing artifact. It records observed source-access posture,
working runner/rung, substrate location, and a pinned recipe for the current
fragrance purchase-review lane.

In scope:

- Public niche fragrance retailer PDPs selected by the owner: Luckyscent /
  Scent Bar, Twisted Lily, ZGO Perfumery, Indigo Perfumery, and Ministry of
  Scent.
- Review-row substrate visibility: body text, rating, date, reviewer/verified
  buyer labels, source-app labels, and product/variant context where source-visible.
- Runner choice and minimum observed flags.

Out of scope:

- Reddit, community, forum, editorial, and CSB-style lanes.
- Brand DTC sources except on-demand follow-up.
- Any bypass of authentication, CAPTCHA, Cloudflare challenge, paid account, or
  private review portal.
- Review quality, demand inference, review fraud scoring, or cleaning/ECR claims.

## Route

- Cynefin route: complicated with a complex access edge.
- Bottleneck: source-access and substrate uncertainty per retailer.
- Riskiest assumption: fragrance-specialist retailers expose review bodies on
  public PDP pages, not only aggregate counts or vendor-widget shells.
- Stop/pivot condition: auth/CAPTCHA/private gate, or no review-row substrate on
  a sampled PDP after one bounded Direct HTTP plus rendered re-probe.
- Isolation: worktree branch `codex/fragrance-purchase-review-probes`.

## Probe Inputs

| Retailer | Sampled PDP |
| --- | --- |
| Luckyscent / Scent Bar | `https://www.luckyscent.com/products/memoirs-of-a-trespasser-by-imaginary-authors` |
| Twisted Lily | `https://twistedlily.com/products/essential-parfums-discovery-set-1` |
| ZGO Perfumery | `https://zgoperfumery.com/products/diptyque-orpheon-eau-de-parfum` |
| Indigo Perfumery | `https://indigoperfumery.com/products/memoirs-of-a-trespasser` |
| Ministry of Scent | `https://ministryofscent.com/products/memoirs-of-a-trespasser` |

## Observed Verdicts

| Retailer | Direct HTTP observation | Rendered observation | Verdict | Route pin |
| --- | --- | --- | --- | --- |
| Luckyscent / Scent Bar | HTTP 200 PDP body preserved. Static HTML exposed aggregate JSON-LD review substrate (`ratingValue: 3.71`, `reviewCount: 14`) and review anchors, but no review-body rows. | CloakBrowser render plus progressive scroll exposed row-level review text and metadata: sampled DOM/text showed 10 review bodies, titles, dates, reviewer names, country labels, variant labels, `data-verified-buyer`, and store-invitation labels. | `GO_ROW_LEVEL_RENDERED` | CloakBrowser packet with `--settle-seconds 5 --scroll-step-px 500 --scroll-passes 4`. |
| Twisted Lily | HTTP 200 PDP body preserved. Static HTML exposed Shopify/vendor review config and aggregate count substrate, but not usable row text. | CloakBrowser render plus progressive scroll exposed row-level review text and metadata: sampled visible text showed 6 reviews, rating summary, reviewer names, dates, verified labels, locations, and Shop App labels. | `GO_ROW_LEVEL_RENDERED` | CloakBrowser packet with `--settle-seconds 5 --scroll-step-px 500 --scroll-passes 4`. Variant URL normalization may append `?variant=...`; record actual final URL. |
| ZGO Perfumery | HTTP 200 PDP body preserved. Static HTML exposed Yotpo/widget config with sampled product count/rating at zero, but no review rows. | CloakBrowser preserved the rendered PDP shell, but sampled page still had no visible review rows or customer-review section text. | `PARTIAL_SAMPLED_EMPTY` | Keep a PDP shell packet. Do not claim row-level capture until another product fixture exposes rows. |
| Indigo Perfumery | Direct HTTP failed before packet write with local certificate verification error: `CERTIFICATE_VERIFY_FAILED`. | CloakBrowser preserved the rendered PDP shell and `CUSTOMER REVIEW` / `shopify-product-reviews` container posture, but sampled page had no visible review rows. | `PARTIAL_SAMPLED_EMPTY` | Use CloakBrowser for access. Do not claim row-level capture until another product fixture exposes rows. |
| Ministry of Scent | HTTP 200 PDP body preserved. Static HTML exposed Judge.me review rows directly, including `jdgm-rev__body`, titles, verified-buyer labels, dates, product title, review source labels, and thumbs counts. | Not needed for the sampled fixture. | `GO_ROW_LEVEL_DIRECT_HTTP` | Direct HTTP packet is sufficient first rung. Escalate to CloakBrowser only if a later product uses lazy-loaded rows. |

## Recipe Notes

1. Start with Direct HTTP when the page body is the target. For this lane, Direct
   HTTP is enough for Ministry of Scent and useful for detecting aggregate-only
   substrates on Luckyscent, Twisted Lily, and ZGO.
2. Escalate to CloakBrowser for rendered review widgets. For Luckyscent and
   Twisted Lily, the working sampled recipe is a rendered packet with
   `--settle-seconds 5 --scroll-step-px 500 --scroll-passes 4`.
3. Treat ZGO and Indigo as sampled partials, not source-wide failures. The
   sampled PDPs preserved product/review-widget shells but did not expose row
   bodies. A second product fixture with known reviews is required before a
   row-level GO/NO-GO claim.
4. Keep `--recapture-relationship` to an accepted enum such as `supplement`.
   Prose in that field fails runner validation and is an operator error, not a
   source-access fact.
5. Clear `ORCA_DATA_ROOT` for scratch probes when an explicit `--output` path is
   intended. The Direct HTTP runner honors the environment data root ahead of
   the supplied scratch output path.

## Non-Claims

- This recon does not say the five retailers are the best sources for review
  quality. It says which sampled retailer PDP surfaces can currently be captured
  with enough row-level purchase-review data for downstream integrity and
  pain/pleasure-point analysis.
- This recon does not certify broad retailer coverage. It pins the observed
  route for one sampled PDP per retailer.
- This recon does not authorize scaled scraping or any challenge bypass.