```yaml
retrieval_header_version: 1
artifact_role: capture recon finding (non-authorizing)
scope: >
  First IG (Instagram) capture-feasibility recon for the creator-momentum /
  wind-caller lane. Records, for the owner's OWN account first, whether and at
  which rung the wind-caller signal (public "calls" = post captions + public
  stats) is capturable via an attended, logged-in, human-mimicking automated
  session, and whether Social Blade (free) covers the stats series. Locks the IG
  capture architecture's open rung / substrate / self-capture-vs-buy choices.
use_when:
  - Choosing the IG capture rung, substrate, or self-capture-vs-buy split.
  - Checking whether IG already has a worked recon before re-probing.
  - Onboarding the IG wind-caller calibration capture path.
authority_boundary: retrieval_only
open_next:
  - docs/product/source_capture_toolbox/capture_recon_index_v0.md
  - docs/decisions/wind_caller_calibration_carveout_v0.md
  - docs/product/source_capture_toolbox/source_capture_playbook_v0.md
stale_if:
  - IG changes its profile/post substrate (og:description meta, web_profile_info API shape).
  - The owner moves to commercial scale (triggers licensed/bought-data posture for stats — non-negotiable per the carve-out).
  - A harness-native authenticated-browser capability is built (would re-open the "calls self-capture is human-driven only" residual).
  - Tier-2 (audience-graph / cross-platform stitching) is later activated under its own gate.
status: RECON_COMPLETE_DEMONSTRATED_GO
```

# IG Wind-Caller Capture-Feasibility Recon (v0)

## What this is — and is not

This is a **capture recon finding**: a real, bounded, attended probe of whether the IG
wind-caller signal is capturable, at which rung, where it lives, and what to buy vs.
self-capture. It closes the recon index's IG gap (previously "Instagram has no
technical recon at all").

It is **non-authorizing**. It is not validation, readiness, buyer proof, commercial
authorization, Tier-2 activation, or a doctrine change. It records a finding; where a
finding implies a posture change, it is surfaced, not made. Verbatim personal caption
text was viewed live for the demonstration but is **not retained** here
(retention-minimal, internal-only, per the carve-out).

## Verdict (headline)

**GO (demonstrated) — at the attended logged-in own-account browser rung**, with a clean
self-capture-vs-buy split:

- **Calls (verbatim post captions + dated engagement) = SELF-CAPTURE** first-party, via the
  attended logged-in own-account browser. This is the moat signal. **Demonstrated live.**
- **Public stats (follower / following / post counts; and the historical series) = BUY** the
  series from Social Blade (free tier carries it; second-hand is acceptable per the carve-out).
  Current-snapshot stats also come **free alongside the calls** (carried in the same profile
  `og:description` meta), so only the *historical time-series* genuinely needs Social Blade.

`direct_http` (the cheapest rung) is **NO-GO for the signal**; a session-bearing browser is
the working rung. Full per-rung verdicts below.

## Posture / authorization (confirmed on entry)

- Controlling carve-out: `docs/decisions/wind_caller_calibration_carveout_v0.md`, **as amended
  by PR #73** — confirmed **MERGED** (merge commit `5ea1241`, merged 2026-06-13; the recon
  worktree is pinned to that commit). The amendment permits **attended automated** capture at a
  **human-mimicking (variable / ADHD-like) cadence** — not uniform machine-rate, not
  high-throughput, not continuous/24-7; no standing or scheduled crawler.
- This probe is the **owner's OWN account** (`@foo_yu_quan`) — the owner's own data, attended,
  logged into IG by the owner (the agent did not and may not enter credentials).
- Bounded: ≤5 accounts, pre-commercial, internal calibration only, US-first. Tier-2 (audience
  graph / cross-platform stitching) NOT activated. Tier-3 exclusions untouched.
- Risk-posture line (`source_capture_playbook_v0.md`): public content is in scope even against
  ToS; **the auth gate is the hard line — own entitled access only.** The own-account logged-in
  read is exactly own-entitled access; no auth gate was defeated.

## Source-gated method (preflight + SOURCE_CONTEXT_READY)

`orca_start_preflight`: AGENTS.md + overlay `README.md` + `source-loading.md` read in task
context. Worktree off fresh `origin/main` (`5ea1241`), pinned at start. Edit permission:
docs-write (finding + index row). Runtime: bounded live IG capture on the owner's own account.
No new committed adapter code.

Sources reference-loaded: `source_capture_playbook_v0.md` (the 6 cross-cutting patterns +
Step-0/1/2/3 method + Risk posture), `capture_recon_index_v0.md`.
Sources source-loaded: the carve-out (merge state confirmed via `gh`),
`source_capture/adapters/direct_http.py`, `source_capture/screening_reddit_read.py` (the
screen-light entitlement-gate pattern), `source_capture/adapters/cloakbrowser_snapshot.py`.

**`SOURCE_CONTEXT_READY`** — with two resolved naming gaps: the commission named the playbook
`capture_investigation_playbook_v0.md` (actual: `source_capture_playbook_v0.md`) and placed
`screening_reddit_read.py` under `adapters/` (actual: one level up at
`source_capture/screening_reddit_read.py`). Both located and read; no content gap.

## Step 0 — Entitlement / access-control gate

| Route | Classification | Disposition |
|---|---|---|
| IG logged-out web (HTML + profile) | publicly-viewable-but-ToS-restricted | in scope (Risk posture; human-rate) |
| IG internal `web_profile_info` API, cookieless | publicly-viewable surface, bot/rate-gated | in scope; gated by session, not auth |
| IG logged-IN **own** account | authenticated — **own entitled access** | in scope (own data; owner logged in) |
| Social Blade free tier | publicly-viewable | in scope (free, second-hand) |

No auth gate was defeated. The owner logged into their own IG; the agent drove the
already-authenticated session.

## Step 1 — Substrate (where the signal lives)

- **Public stats (counts):** carried in the profile page `og:description` meta tag
  (`"<N> Followers, <M> Following, <K> Posts — …(@handle)"`) **and** in IG's internal
  `web_profile_info` JSON API (`edge_followed_by.count`, `edge_follow.count`,
  `edge_owner_to_timeline_media.count`). The API **no longer carries the post nodes** — counts
  only (observed: `recentPosts: []` even on a 200 logged-in response).
- **Calls (verbatim captions + dated engagement):** carried per-post in the **post page**
  `og:description` / `og:title` meta (`"<likes> likes, <comments> comments - <handle> on
  <date>: \"<caption>\""`). Post permalinks (`/<handle>/p/<shortcode>/`) are enumerable from the
  profile DOM.
- **NOT in the initial logged-out stdlib HTML:** a bare `direct_http` GET returns a ~595 KB JS
  shell with **no** `og:description`, **no** embedded stats/calls — IG serves the meta-tag'd /
  hydrated content only to a browser-like session.

## Step 2 — The probe ladder (receipts; cheapest-first)

Cadence across all live steps: **attended, variable, human-speed** — a handful of bounded
navigations with multi-second settles, one profile, one API call, one post page. No crawler,
no scheduler, no bulk enumeration. Consistent with the amended carve-out.

| Rung | Target | Status / bytes | Signal present? | Verdict |
|---|---|---|---|---|
| **direct_http** (stdlib, cookieless, browser UA) | `instagram.com/instagram/` HTML | **200**, ~595 KB | No stats meta, no embedded calls (only `props`/`csrftoken`/`challenge` markers) | **NO-GO for signal** (reaches shell, not signal) |
| **direct_http** (cookieless) | `web_profile_info` API (±`x-ig-app-id`) | **429** Too Many Requests (both variants) | n/a — bot/rate-gated cookieless | **NO-GO cookieless** (needs a session) |
| **real browser, logged-OUT** (guest session) | `instagram.com/instagram/` | rendered | **Stats render** (header + `og:description`); post grid renders but **caption depth login-walled** by the signup modal | **PARTIAL** (stats GO; calls walled) |
| **real browser, logged-IN own account** | `instagram.com/foo_yu_quan/` profile | rendered, **no login modal** | Stats in header + `og:description`; post permalinks enumerable | **GO** |
| **real browser, logged-IN own account** | `web_profile_info` API (same-origin fetch, session cookies + app-id) | **200** JSON | Structured stats (followers 186, following 267, posts 3, `is_private:false`); **no post nodes** | **GO (stats only)** |
| **real browser, logged-IN own account** | own post page `/p/<shortcode>/` | rendered, no login modal | **Verbatim caption present** in `og:description`/`og:title` (caption len ≈ 95 chars; likes/comments/date present) | **GO (calls)** |

The 429-cookieless → 200-logged-in contrast on the **same endpoint** is the clean proof that the
block was a session/bot gate (Pattern 1: "blocked is a hypothesis"), not an auth wall and not a
true NO-GO.

## Step 3 — Social Blade (free-tier) commodity coverage

`socialblade.com/instagram/user/instagram` via `direct_http` (logged-out): **HTTP 200, ~80 KB**,
**no Cloudflare/challenge wall**. Markers present: `Followers`, `engagement` (×20), `rank`,
`Daily`, `Future Projections`, charting. → The free tier **carries the stats series surface**
(follower / engagement / rank / daily, with projections). Known limitations: full historical
depth + export are **premium-gated**; data is **second-hand** (aggregated) — so **verbatim call
text must still come first-party**, never from Social Blade (carve-out requirement).
**Verdict: GO (stats commodity, free tier).**

## Step 4 — The decision (locks the architecture's open choices)

- **Rung:** a **session-bearing browser** is the working rung. For the **calls** (moat), that is
  the **attended logged-in own-account browser** (own entitled access). `direct_http` is NO-GO for
  the signal; the logged-out browser is PARTIAL (stats only).
- **Substrate:** **stats** = profile `og:description` meta + `web_profile_info` JSON (counts only);
  **calls** = per-post page `og:description`/`og:title` meta (verbatim caption + dated engagement).
- **Self-capture-vs-buy:** **SELF-CAPTURE the calls** first-party (logged-in own account);
  **BUY the stats time-series** from Social Blade free (current-snapshot stats are free alongside
  the calls; only the historical series needs Social Blade). This is the "self-capture the moat,
  buy the commodity" thesis, instantiated for IG.

## Load-bearing finding for the build lane (STOP — not built here)

The harness's existing browser adapter (`cloakbrowser_snapshot.py`) launches **`headless=True`**
with **`profile_persistence: none`** and **`storage_state_loaded: False`** — it carries **no
session / no login**. It therefore **cannot perform the logged-in own-account calls capture** that
this recon demonstrated via the human-driven browser. Operationalizing the calls self-capture
**inside the harness** (so it is not human-driven each time) requires a **new authenticated /
persistent-context browser capability** (own-session storage-state load, attended, human-mimicking
cadence). That is **new committed adapter code → a separate authorized build**, explicitly out of
scope for this recon. Recorded as a finding, **not built here.**

Until that capability exists: IG calls self-capture is **human-driven (attended browser) only**;
the harness can already do the Social Blade stats fetch at the `direct_http` rung today.

## Cross-cutting patterns confirmed (recon index spine)

1. **"Blocked" is a hypothesis** — the cookieless 429 was a session gate, not NO-GO (200 once
   logged in). 2. **Locate substrate first** — stats vs. calls live in *different* substrates;
   `web_profile_info` no longer carries posts. 4. **Entitlement gate first** — logged-out is ToS-
   in-scope; own-account is own-entitled; no auth gate defeated. 5. **PARTIAL/NO-GO are first-class**
   — direct_http NO-GO-for-signal and logged-out-browser PARTIAL are honest, useful diagnoses.

## Limitations / residuals / non-claims

- **Single own account, single session.** Demonstrated on `@foo_yu_quan` (3 posts). Behavior on a
  larger creator account (pagination of the posts feed beyond the profile DOM's first tranche) is
  **not probed** — the per-post `og:description` substrate is expected to hold, but post
  *enumeration* past the initial grid uses a separate paginated query, **not demonstrated here**.
- **Third-party wind-caller accounts NOT probed.** #73 is merged (third-party would be permitted),
  but this recon was scoped own-account-first per the commission; third-party capture is a separate
  bounded step.
- **Harness-native logged-in capture NOT built** (see the build-lane finding above).
- **Stats historical series** depth from Social Blade free is **premium-limited**; verbatim call
  text must stay first-party.
- Not validation / readiness / buyer-proof / commercial authorization / Tier-2 activation / a
  doctrine change. A green fetch is not the gate — this recorded verdict is.

## Next authorized step (candidate, not authorized here)

A bounded, separately-authorized build to add a harness authenticated-browser capability (own
session storage-state, attended, human-mimicking) so the calls self-capture is harness-native;
and/or a first **third-party** wind-caller own-rung probe under the merged carve-out. Both require
their own authorization.
```
