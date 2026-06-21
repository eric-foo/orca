```yaml
retrieval_header_version: 1
artifact_role: capture recon finding + proposed capability spec (non-authorizing)
scope: >
  Instagram profile-grid DOM engagement recon and capture contract for low-interaction
  creator monitoring. Records the 2026-06-21 no-hover hidden-DOM finding for a public
  reels grid and stabilizes what a downstream implementation must preserve before
  optimizing for DOM extraction instead of per-item page visits.
use_when:
  - Scoping an IG creator-monitoring route that captures views, likes, and comment counts from profile grids.
  - Deciding whether hover, per-item clicks, OCR, or computer-use interaction is needed for surface engagement.
  - Checking how engagement observations must be keyed so later captures survive new posts and grid-index shifts.
authority_boundary: retrieval_only
open_next:
  - orca/product/spines/capture/core/source_families/social_media/instagram/ig_capture_findings_consolidated_v0.md
  - orca/product/spines/capture/core/source_families/social_media/instagram/ig_reel_viewcount_capture_feasibility_recon_v0.md
  - orca/product/spines/capture/core/source_capture_toolbox/source_capture_playbook_v0.md
  - orca/product/spines/capture/core/source_capture_toolbox/capture_recon_index_v0.md
stale_if:
  - IG profile/reels grid media anchors stop carrying hidden numeric engagement leaves before hover.
  - A fresh logged-out/proxy probe contradicts the existing-Chrome finding.
  - Static post grid probing shows a materially different DOM contract.
  - A runner implementation supersedes this proposed extraction contract.
status: RECON_PARTIAL_GO_NO_HOVER_REELS_DOM__SPEC_COMPLETE_READY_FOR_SCOPING__STATIC_POSTS_PROXY_AND_SCALE_OPEN
```

# IG Profile-Grid DOM Engagement Recon And Spec (v0)

## Source context

```yaml
orca_start_preflight:
  agents_read: yes
  overlay_read: yes
  source_pack: custom S0 + capture-method + IG source-family target docs
  edit_permission: docs-write
  target_scope: IG-only source-family report/spec for no-hover profile-grid engagement extraction
  dirty_state_checked: yes
  isolation: new worktree branch codex/ig-grid-dom-engagement-spec-writable because the main workspace was dirty and .codex worktrees are read-only here
  blocked_if_missing:
    - current user redirect to IG grid DOM optimization
    - no-hover DOM probe sample pack
    - source_capture_playbook_v0.md
    - capture_recon_index_v0.md
```

Spec status: `SPEC_COMPLETE_READY_FOR_SCOPING`.

This is a capture recon finding plus a behavior contract. It is not a runner implementation, not
validation, not buyer proof, not bot classification, and not a claim that the route is undetectable.
It records a narrow but useful fact: on one existing Chrome Instagram reels grid, the DOM already
carried visible view counts plus hidden like/comment counts before hover.

## Probe finding

Probe target: `https://www.instagram.com/vanzzcoser/reels/`.

Captured sample: local ignored diagnostic artifacts under
`orca-harness/_test_runs/ig_non_hover_dom_pack_20260622_1/`.

Observed facts:

- Existing normal Chrome tab, not a runner packet and not a proven logged-out/proxy context.
- Mouse moved off-grid; no tile hover, click, reload, scroll, cookie read, storage read, or profile inspection during the no-hover check.
- The first compact visible-text pack found only rendered reel view counts in `anchor.innerText`.
- The deeper no-hover check inspected hidden leaf text and parsed `66/66` visible reel anchors.
- Extraction rule that worked: `views = rendered media-anchor innerText`; `likes/comments = first two hidden leaf numeric descendant texts, excluding the rendered view count`.
- Records can be keyed by media path/shortcode, not by grid index.

Sample rows from the corrected no-hover hidden-DOM pack:

| Shortcode | Path | Views | Likes | Comments |
| --- | --- | --- | --- | --- |
| `C7dGMB_hY3n` | `/vanzzcoser/reel/C7dGMB_hY3n/` | `1.4M` | `73.5K` | `536` |
| `DZz48C2hkI5` | `/vanzzcoser/reel/DZz48C2hkI5/` | `152K` | `10.3K` | `23` |
| `DZx0y8jBw-q` | `/vanzzcoser/reel/DZx0y8jBw-q/` | `71.9K` | `5,463` | `18` |
| `DZQsRFmTkUx` | `/vanzzcoser/reel/DZQsRFmTkUx/` | `27.4K` | `2,283` | `0` |
| `DWTJZkogcus` | `/vanzzcoser/reel/DWTJZkogcus/` | `1.8M` | `69.2K` | `852` |

## Required behavior

The profile-grid engagement extractor must, given an explicit IG creator handle or profile-grid URL,
load the public profile/reels grid in a browser context and extract surface engagement from media
anchors without hover or per-item page visits by default.

For each observed media anchor, it must emit a stable media identity (`shortcode` and permalink path),
observed grid position, content kind when derivable from the path, rendered view-count text when
present, hidden no-hover like-count text when present, hidden no-hover comment-count text when
present, pinned-marker evidence when present, parse status, and evidence locator.

The extractor must key repeat observations by `shortcode` or permalink path. Grid index is only an
observation of page order at capture time and must not be used as identity.

The default route is direct navigation from an already-known handle roster or URL list, then DOM
extraction. Instagram search, creator-click navigation, OCR, hover loops, and per-item opens are
fallback/calibration actions, not the steady-state collection path.

## Non-goals

- Capturing comment text, commenter identities, or bot/paid-comment classifications.
- Solving private profiles, login-gated material, CAPTCHA, password automation, raw cookies, raw storage-state paths, Chrome profile import, proxy rotation, or anti-detect browser work.
- Claiming invisibility, stealth, or immunity from IG behavioral/rate detection.
- Capturing media bytes or full captions from the grid.
- Replacing the existing per-item route where full caption/date/comment text is required.
- Treating the existing Chrome diagnostic as a proven logged-out proxy result.
- Assuming static posts expose reel-style view counts.
- Expanding beyond Instagram.

## Interfaces / contracts

Minimum input:

- `profile_handle` or exact IG profile/reels URL.
- `capture_context_label`, for example `existing_chrome_diagnostic`, `headed_logged_out_browser`, or a future runner route label.
- `capture_timestamp_utc`.
- Browser-route metadata that is safe to record: viewport, URL, route label, and whether hover/click/scroll occurred.

Minimum output per media observation:

```yaml
media_observation:
  platform: instagram
  source_profile:
  capture_timestamp_utc:
  capture_context_label:
  profile_grid_url:
  grid_index_observed:
  kind: reel | post | unknown
  shortcode:
  permalink_path:
  pinned_marker_present: true | false | unknown
  rendered_anchor_text:
  views_text:
  likes_text:
  comments_text:
  hidden_leaf_numeric_texts:
  extraction_mode: no_hover_dom | hover_dom | item_page | ocr | unknown
  parse_status:
  evidence_locator:
  limitations:
```

Required parse statuses:

- `parsed_no_hover_grid_engagement`: views/likes/comments parsed from no-hover grid DOM.
- `views_only_no_hidden_engagement`: visible views found but no hidden like/comment leaves found.
- `hidden_engagement_only_no_visible_views`: hidden likes/comments found, visible views absent.
- `ambiguous_hidden_numeric`: more or fewer hidden numeric leaves than the extraction rule can safely map.
- `static_post_contract_unverified`: static post behavior not yet pinned.
- `access_failed_visible_block`: visible page is login wall, interstitial, or block shell.
- `route_not_verified`: route context cannot support the claim being made.

Class names must not be treated as stable. The extractor should use media-anchor paths,
source-visible text, leaf text, and nearby icon/label semantics where available. If a future
implementation uses CSS selectors, selector failure must produce a visible parse status rather than
a silent empty result.

## Acceptance criteria

- A fresh no-hover probe against a public reels grid returns one record per visible media anchor and
  reports parsed versus unparsed rows without silent drops.
- For the current observed sample shape, rows equivalent to the sample above parse as views, likes,
  and comments keyed to shortcode/permalink.
- Returning to the same creator after new posts appear still joins old observations by shortcode,
  not by grid position.
- A manual hover/DevTools spot check on a small sample confirms the no-hover hidden values match the
  values IG displays on hover.
- A main-grid/static-post probe records whether static posts expose hidden no-hover likes/comments
  and whether views are absent by content type.
- The output records route context honestly: existing Chrome diagnostic, logged-out proxy, sessioned,
  runner packet, or other route must not be collapsed into one generic "IG capture" label.
- No output includes cookies, storage-state JSON, proxy credentials, exit IP, raw browser profile
  paths, or other local secrets.
- If the page shows a visible login wall or interstitial, the result is `access_failed_visible_block`
  or equivalent, not an empty successful capture.

## Operational recommendation

Use scripted DOM extraction as the default, not computer-use OCR. Computer use is useful for
attended calibration or manual navigation when a page state must be inspected, but it is the wrong
steady-state reader: it consumes more tokens, introduces UI event noise, and makes the extraction
less reproducible.

The efficient steady-state loop is:

1. Start from a prepared handle/profile URL roster.
2. Navigate directly to the profile or `/reels/` URL.
3. Let the page settle under a bounded, recorded route.
4. Extract media-anchor DOM records.
5. Store one observation set keyed by shortcode.
6. Move to the next explicit creator only if cadence and block checks remain clean.

This reduces interaction count and latency. It does not prove lower detection risk. Detection risk
still sits mainly in profile navigations, request cadence, IP/account/session reputation, and any
browser-route fingerprint; this spec only removes unnecessary hover/click/OCR work.

## Open questions

- Static posts: do their media anchors carry hidden like/comment leaves before hover, and do they
  intentionally omit view counts on the main grid?
- Fresh route: does the same hidden-DOM contract hold in a fresh logged-out browser/proxy context,
  separate from the existing Chrome tab?
- Viewport and zoom: what viewport gives the best stable grid density without changing DOM shape or
  making text parsing ambiguous?
- Scale/cadence: what creator-count and spacing remain clean over repeated monitoring windows?
- Persistence format: should this become a runner-side packet, a local monitoring view, or a
  projection attached to existing IG call packets? Scoping can defer this because the behavior
  contract above fixes the media observation shape.

## Downstream handoff

```yaml
spec_handoff:
  status: SPEC_COMPLETE_READY_FOR_SCOPING
  required_behavior:
    - Extract Instagram profile-grid surface engagement from media-anchor DOM without hover by default.
    - Emit media observations keyed by shortcode/permalink, including route context and parse status.
    - Prefer direct profile/reels navigation from a roster over IG search/click/OCR loops.
  non_goals:
    - comment text capture
    - bot classification
    - private/auth-gated capture
    - anti-detect/proxy-rotation/CAPTCHA work
    - stealth or undetectability claims
    - media-byte capture
  interfaces_contracts:
    - input profile_handle_or_url + safe route metadata
    - output media_observation records with shortcode/permalink identity
    - explicit parse_status for partial/blocked/ambiguous cases
    - no cookies, storage state, proxy credentials, exit IP, or raw browser profile paths in output
  acceptance_criteria:
    - fresh no-hover reels-grid probe parses visible media anchors or reports visible parse failures
    - manual hover/DevTools spot check matches no-hover hidden values on sample rows
    - static post behavior is probed and labeled separately
    - repeat captures join by shortcode after grid order changes
  deferred_open_questions:
    - static post DOM contract
    - fresh logged-out/proxy parity
    - viewport/zoom density
    - sustained cadence ceiling
    - final persistence surface
  review_timing_advisory:
    adversarial_review: recommended
    highest_value_checkpoint: after_artifact_pre_implementation
    review_target: this spec plus the first extractor implementation route
    why_this_checkpoint: >
      The route is tempting to overclaim as undetectable or general across IG. A review should
      check that implementation preserves route honesty, parse-status visibility, and non-goals.
  scoping_may_rely_on:
    - Reels-grid no-hover engagement is feasible on the observed existing-Chrome sample.
    - The first implementation should optimize around DOM records, not OCR or per-item clicks.
    - The implementation must keep static posts, fresh proxy/logged-out parity, and cadence as open residuals.
```

## Non-claims

Not validation, readiness, source-quality proof, fixture admission, commercial authorization, legal
advice, stealth guidance, or a completed runner. The evidence is one existing-Chrome reels-grid
diagnostic sample plus a behavior spec for the next implementation/scoping lane.