# Demand-Durability Multi-Retailer Live-Capture Verdicts + Measured-ToS Posture v0

```yaml
retrieval_header_version: 1
artifact_role: Capture recon verdicts + measured-ToS posture record (observed facts + limits; non-authorizing; INV-1)
scope: >
  Records the per-retailer LIVE-capture verdicts for the demand-durability multi-retailer rendered
  capture: Amazon recon (GO/PARTIAL/NO-GO), and Sephora + Ulta bounded single-SKU verification through
  the cadence runner via the merged rendered (CloakBrowser) writer. Captures each retailer's measured-ToS
  posture, as-served storefront/locale pins, the rendered method used, and honest limitations. Observed
  facts + limits only -- no demand verdict, no scoring, no durable-vs-hollow judgment (INV-1).
authority_boundary: retrieval_only
use_when:
  - Checking whether/which retailers were live-verified for the demand-durability series and how.
  - Reading the measured-ToS posture + as-served storefront per retailer.
  - Deciding the US-storefront geo path before any production series.
open_next:
  - docs/product/data_capture_spine/demand_durability_multi_retailer_rendered_capture_spec_v0.md   # the binding spec
  - docs/prompts/handoffs/demand_durability_multiretailer_live_capture_commission_handoff_v0.md     # the commission
  - docs/product/source_capture_toolbox/capture_recon_index_v0.md                                   # recon index (append a row)
  - docs/product/source_capture_toolbox/source_capture_playbook_v0.md                               # the method
  - orca-harness/runners/run_source_capture_durability_series.py                                    # the cadence runner
  - docs/product/data_capture_spine/data_capture_source_access_boundary_decision_v0.md              # the boundary
stale_if:
  - A retailer's verdict (GO/PARTIAL/NO-GO) changes or is re-probed.
  - The source-access boundary decision changes hard stops or the measured-ToS posture.
  - The cadence runner's writer-invocation seam changes, or a proxy passthrough is added to the runner.
  - A US-geo egress path that Amazon does not bot-wall is established (would reopen the Amazon US verdict).
```

## What this is — and is not

A record of **observed live-capture facts + honest limits** from the commissioned live half of the
demand-durability multi-retailer rendered capture. It is **non-authorizing**: not validation, not
readiness, not commercial-scale capture, not a demand verdict, not ECR/Cleaning/Judgment, and no
source-quality scoring or durable-vs-hollow judgment (INV-1). Verdicts are what the live probes
observed on **2026-06-15**, not a settled capability claim.

## Provenance

- **Commission:** `docs/prompts/handoffs/demand_durability_multiretailer_live_capture_commission_handoff_v0.md` (owner-authorized 2026-06-15). Landing to `main` stays owner-gated.
- **Lane:** branch `demand-durability-live-capture-v0` off `origin/main @ 7d7cacdc`.
- **Consumed (not re-implemented):** the merged rendered-capture wiring — PR #146 (`dfdc9816`): cadence runner `run-slot --writer cloakbrowser` selector + `--writer-arg` knob passthrough + the CloakBrowser writer's Ob.17 durability flags. Confirmed present on `origin/main` before building.
- **Runtime:** CloakBrowser `0.3.31` (Chromium), local venv. All fetches human-rate, single-SKU, bare path (no proxy) per the owner's geo decision below.
- **Evidence:** scratch capture packets under gitignored `orca-harness/_test_runs/dd_live/` (recon controls + the two observed durability series). Series-grade packets are bounded verification artifacts, not a production series.

## Cross-cutting finding — egress geo determines storefront

The executing host egresses from a **Singapore-geolocated IP**. This is the load-bearing context for
every "US storefront" question and was discovered during Amazon recon (amazon.com served `SGD` +
`Deliver to Singapore`). The commission's "US storefront (owner default)" is therefore **not** what a
bare fetch yields for a geo-localizing retailer. Per-retailer effect:

- **Amazon** geo-localizes by requester IP → bare fetch = **Singapore storefront**. US needs US egress.
- **Sephora** (`sephora.com`) is US-only (SG is a separate `sephora.sg`) → serves **US/USD** regardless of egress.
- **Ulta** (`ulta.com`) is US-only → serves **US/USD** regardless of egress.

**Owner decision (2026-06-15):** resolve via the Decodo US proxy → on test, Amazon **bot-walled** the
available Decodo residential exit (see Amazon below); owner then directed **verify Sephora/Ulta on the
bare path, record as-served pins**. US-storefront pinning for geo-localizing retailers (Amazon) is a
**deferred, gated** decision (a cleaner US residential/ISP exit + a runner proxy passthrough — neither
exists today).

## Per-retailer verdicts

| Retailer | Verdict | Method (rung) | As-served storefront | Substrate captured |
|---|---|---|---|---|
| **Sephora** | **GO** (verified) | cadence runner → CloakBrowser, progressive scroll (`--scroll-step-px=350`) + settle | US / USD | Bazaarvoice reviews (lazy-load fired) + price |
| **Ulta** | **GO** (verified, **substitute SKU**) | cadence runner → CloakBrowser (settle) | US / USD | `__APOLLO_STATE__` embedded JSON (`productId`/`listPrice`/`salePrice`/`sku`) + price + availability |
| **Amazon** | **GO** substrate reachability (bare); **NO-GO** US-storefront via Orca's own (proxy) path | rung-0 `direct_http` (control); CloakBrowser+proxy (escalation) | Singapore / SGD (bare); US unreached | Full server-rendered PDP (bare); **bot wall** (proxied) |

### Sephora = GO (verified)

- **Method:** `init` series + `run-slot --slot 0 --writer cloakbrowser --writer-arg=--scroll-step-px=350 --writer-arg=--settle-seconds=2`. Bare `direct_http` returned **HTTP 403** (bot wall) — the rendered CloakBrowser path passed it legitimately (no gate defeated; recon Pattern 1: "blocked" was a hypothesis, resolved by the rendered route).
- **Substrate:** 1.39 MB rendered DOM; **Bazaarvoice reviews loaded** by progressive scroll (review-count anchors present); price substrate present (multiple USD values incl. `$38.00`).
- **Packet:** valid Ob.17 durability observation; slot 0 = **observed**; series complete (1 observed / 0 un-observed). `series_id` `sephora_laneige_lipmask_berry_us_v0`; `intended_cadence` set; locale/currency/variant pins recorded.
- **As-served pins:** locale `en-US`, currency `USD`, variant `Berry, 2.5g (P446304)`.
- **Measured-ToS:** public PDP, no login; honest anti-blocking (rendered browser, human-rate, single SKU) under the source-access boundary. Bare anti-bot 403 present; rendered path passed without defeating a gate.
- **Limits:** single slot ≠ sustained-cadence capability; observed price/review **values** are as-served, **not** authenticated or attributed to the primary product line-item in this verification (container ≠ content authenticity, two-axis bar); one SKU.

### Ulta = GO (verified, substitute SKU)

- **SKU divergence (honest):** Ulta does **not** carry the cross-retailer SKU (LANEIGE Lip Sleeping Mask) — three web searches + a live Ulta own-search probe (`ulta.com/search?Ntt=laneige lip sleeping mask`) returned **no Laneige result**. Ulta's rendered seam was verified on a confirmed in-catalog substitute: **ULTA Beauty Collection — Night Shift Overnight Lip Mask** (`pimprod2046225`, `sku=2620759`), same category. The same-SKU comparability shape is therefore **not** achieved across all three (Sephora + Amazon share the Laneige SKU; Ulta uses a substitute).
- **Method:** `init` + `run-slot --slot 0 --writer cloakbrowser --writer-arg=--settle-seconds=3`.
- **Substrate:** 1.46 MB DOM; **0 block markers**; `window.__APOLLO_STATE__` present with `productId` (×24), `listPrice`, `salePrice`, `price`, `sku` — the recon'd embedded-JSON substrate; price `$12.00`; availability "In stock".
- **Packet:** valid Ob.17 durability observation; slot 0 = **observed**; series complete. `series_id` `ulta_nightshift_overnight_lipmask_us_v0`; pins recorded.
- **As-served pins:** locale `en-US`, currency `USD`, variant = the Night Shift substitute SKU.
- **Measured-ToS:** public PDP, no login; rendered human-rate single-SKU capture under the boundary.
- **Limits:** substitute SKU breaks same-SKU comparability; single slot ≠ sustained cadence; observed values as-served, not authenticated.

### Amazon = GO substrate reachability (bare, SG) / NO-GO US-storefront via Orca's own path

- **Bare `direct_http` (rung-0 control): GO substrate, SG storefront.** HTTP 200, 2.18 MB, **0 block markers** on a single human-rate `urllib` GET. Price/availability/reviews are **server-rendered into the initial HTML** — checkable anchors: `<span class="a-offscreen">S$30.76</span>` / `S$33.32`, `Currently unavailable.`, `34,282 ratings`, ASIN `B07XXPHQZK` ×170, buybox markers. **No rendered/CloakBrowser path needed for Amazon** — a series would use `--writer direct_http` (the default), unlike Sephora/Ulta.
- **As-served storefront = Singapore:** `"currencyOfPreference" value="SGD"`, prices only in `S$`, `Deliver to Singapore` (marketplaceId `ATVPDKIKX0DER` = amazon.com US marketplace serving an SG-geolocated session).
- **CloakBrowser + Decodo residential proxy (US-geo escalation): NO-GO.** Amazon served its **"Click the button below to continue shopping"** bot-mitigation interstitial (5.5 KB, no substrate) at the PDP URL. **STOPPED at the gate** — not defeated (the commission's hard constraint; CloakBrowser does not solve challenges).
- **Verdict:** substrate reachability **GO** (bare path, SG); commissioned **US-storefront series = NO-GO via Orca's own (proxy) path** — the available Decodo rotating-residential exit is bot-walled by Amazon. This matches the commission's anticipation: *Amazon's ToS is the most restrictive on automation; commercial / US scale routes through a licensed provider, not Orca's own path.*
- **Measured-ToS:** Amazon's ToS is the most restrictive on automation; the bare read was a single human-rate public fetch under the owner's accepted pre-commercial risk posture. Commercial/US-scale Amazon capture routes through a provider.
- **Limits:** one human-rate fetch ≠ a settled **series** capability (Amazon rate/pattern/IP detection over a cadence is unproven); container ≠ price authenticity; "Currently unavailable" is the SG-session state; a clean US exit Amazon does not flag was not available.

## Structural findings (for the owner / downstream lanes)

1. **The cadence runner cannot pass a proxy to the writer — by deliberate design.** The `run-slot --writer-arg` allowlist (`_WRITER_ARG_KNOB_ALLOWLIST`) rejects proxy flags, and `run-slot` has no proxy argument (PR #146 intentionally excluded proxy — "an owner decision, not a per-slot knob"). A US-pinned **series through the runner** for a geo-localizing retailer would require adding a proxy passthrough to the runner — a change to just-merged, cross-vendor-reviewed code that reverses that intent. Not done in this lane; surfaced for an owner decision.
2. **CloakBrowser block-detection misses Amazon's "Continue shopping" interstitial → false-success risk.** The proxied Amazon capture recorded `access_block_reason: null` and a SUCCESS access posture for the bot interstitial. Through `run_slot`, that would record the gate as an **observed** durability slot (false success), violating gap≠no-change for Amazon-via-proxy. Out of this lane's scope (existing merged code); flagged as a background task for `cloakbrowser_snapshot.py` block-detection hardening + a regression test, routed through delegated cross-vendor review.

## Acceptance-signal status (per the spec)

- **Sephora:** ✅ valid Ob.17 packet via the runner→writer seam; ToS posture + verdict recorded; one-series-per-retailer; no gate defeated.
- **Ulta:** ✅ valid Ob.17 packet via the seam (substitute SKU, divergence recorded); same as above.
- **Amazon:** honest **NO-GO for the US-storefront series via Orca's own path** (recorded, not forced) — `gap ≠ no-change` honored: the Amazon proxy bot-wall was **not** recorded as a series observation (no Amazon series was init/run; recon only).
- **One-series-per-retailer shape** held; **no gate defeated**; **additive** (no schema change, no `SOURCE_CAPTURE_MANIFEST_VERSION` bump, no runner state-model change, no per-retailer adapter, no new writer code).

## Non-claims

Not validation, not readiness, not commercial-scale capture, not a demand verdict, not source-quality
scoring, not a durable-vs-hollow judgment, not ECR/Cleaning/Judgment. The rendered-capture wiring's
correctness is PR #146's concern (reviewed cross-vendor); this record proves the live path within the
source-access boundary on 2026-06-15, with the limits above traveling visibly.
