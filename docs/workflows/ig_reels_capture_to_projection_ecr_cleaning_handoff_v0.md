```yaml
retrieval_header_version: 1
artifact_role: Workflow handoff packet
scope: >
  Cold-reader handoff from the Instagram public /reels/ capture lane to downstream
  Projection, Evidence Candidate Record, Cleaning, and future TikTok/YouTube social
  source-family lanes. Records continuation state and lane boundaries only.
use_when:
  - Continuing IG reels-grid downstream projection/ECR/Cleaning work.
  - Starting TikTok or YouTube source-family probes using generic DOM plus passive JSON lessons.
  - Checking which code-enforceable items belong outside the capture runner.
authority_boundary: retrieval_only
open_next:
  - orca/product/spines/capture/core/source_families/social_media/instagram/ig_profile_grid_dom_engagement_recon_and_spec_v0.md
  - orca/product/shared/projection_doctrine/core_spine_v0_projection_doctrine_v0.md
  - docs/workflows/ecr_spine_submap_v0.md
  - orca/product/spines/foundation/product_contract/core_spine_v0_data_and_cleaning_spine_boundary_v0.md
stale_if:
  - IG reels-grid runner or parser changes row identity, source surfaces, or candidate preservation.
  - Projection doctrine changes mechanical-only, no-salience, or loss-ledger rules.
  - ECR/SCR carry-or-residualize discipline changes.
  - Cleaning gains owner-authorized semantic classification authority.
  - TikTok or YouTube probes supersede the generic social learning capsule.
```

# Handoff Packet

## Load Contract

- packet_version: workflow-handoff-v1
- mode: max
- created_at: 2026-06-22T20:30:03.9869610+08:00
- created_by_lane: Codex IG public reels capture closeout lane; provenance only, not authority
- workspace: `C:\Users\vmon7\Desktop\projects\orca`
- handoff_path: `docs/workflows/ig_reels_capture_to_projection_ecr_cleaning_handoff_v0.md`
- expected_branch: `main`
- expected_head: `b3072a0b`
- expected_dirty_state_including_handoff_file: dirty working tree; this handoff file is expected to be untracked after creation; receiver must rerun `git status --short --branch`
- load_rule: confirm-don't-trust; re-verify every load-bearing fact against its compare target before acting; sender claims are hypotheses, not authority

## Goal Handoff

- long_term_goal: Build Orca social-source capture and downstream evidence plumbing that can monitor public creator/content traction without confusing raw capture, Projection, ECR, Cleaning, or Judgment responsibilities.
- anchor_goal: Route IG reels-grid learnings into the correct lanes: Projection gets mechanical source-view enforcement, ECR gets by-key receipt/integrity/content boundaries, Cleaning gets non-destructive normalization mechanics, and TikTok/YouTube lanes get generic probe lessons without inheriting IG-specific selectors or endpoints.
- success_signal: A cold downstream lane can re-open the named sources and continue only its lane's bounded work without re-learning the IG DOM/JSON findings or smuggling ad/sponsorship/demand/integrity judgment into capture, projection, ECR, or Cleaning.

## Open Decision / Fork

- decision: Whether to implement items 1-3 as one Projection-first slice or as parallel Projection, ECR, and Cleaning slices.
  - options: Projection-first adapter and tests; or parallel lane plans before code.
  - already constrained / off the table: no ad, sponsorship, bot, paid-comment, demand, credibility, integrity, Decision Strength, or Action Ceiling conclusions in Projection, ECR, Cleaning, or Capture; no IG selectors/endpoints/count semantics copied into TikTok/YouTube.
  - trade-offs: Projection-first protects the row contract fastest; parallel planning reduces lane-mismatch risk but adds coordination latency.
  - owner of the call: current Orca owner / current receiving lane user instruction.
  - recommendation and why: Projection-first, then ECR/Cleaning consumption checks. Items 1-3 are most directly enforced at the projection row boundary.

## Drift Guard

- Static/reels separation remains Capture-owned. Projection/Cleaning consume declared `source_surface`; they do not decide whether static is captured or mix static rows into reels traction.
- Projection is mechanical and source-visible only. It may carry captions, timestamps, counts, source surfaces, row identity, and mechanical mention counts; it must not decide meaning.
- ECR/SCR references by key and carries/residualizes; it does not author meaning from capture prose or merge projection fields into posture fields.
- Cleaning may normalize and cluster mechanically, but sponsorship, credibility, artificial-amplification, exclusion, demand, and action-support effects stay Judgment-owned.
- TikTok/YouTube reuse the generic method only, not IG-specific implementation details.

## Inherited Context (does NOT flow to a new lane)

### Source-loading state to re-establish

- overlay source-loading policy: `.agents/workflow-overlay/source-loading.md`
- targets to enter the ladder:
  - `orca/product/spines/capture/core/source_families/social_media/instagram/ig_profile_grid_dom_engagement_recon_and_spec_v0.md`
  - `orca/product/shared/projection_doctrine/core_spine_v0_projection_doctrine_v0.md`
  - `docs/workflows/ecr_spine_submap_v0.md`
  - `orca/product/spines/foundation/product_contract/core_spine_v0_data_and_cleaning_spine_boundary_v0.md`
  - `orca-harness/runners/run_source_capture_ig_reels_grid_packet.py`
  - `orca-harness/source_capture/ig_reels_grid.py`
  - `orca-harness/source_capture/ig_reels_grid_capture.py`
- already loaded, weak orientation only: AGENTS, overlay README, source-loading, artifact-folders, decision-routing, IG spec, projection doctrine, ECR submap, Data/Cleaning boundary, and relevant IG runner/parser/test files were read on 2026-06-22.
- must load first before strict/actionable steps: AGENTS.md, overlay README, source-loading, this packet, IG spec, and the owner source for the receiving lane.
- load rule: receiver re-runs progressive source loading per overlay; this packet's loaded-set only seeds the ladder.

### Earlier-decided concepts and behaviors

- IG steady-state public monitoring default is one `/reels/` page load with no hover, click, OCR, item-page fan-out, comment-text capture, or media-byte preservation.
  - verify pointer: IG spec, SHA256 `A200F56527CEA2FDF4F289913C32C5BCD65B9FE7ECDB5A5C343FFA8D11B20D32`.
- Projection may carry raw counts, captions, timestamps, labels, and baselines, but must not emit interpretation such as anomaly, independence, demand, credibility, or action labels.
  - verify pointer: Projection doctrine, SHA256 `BE22FD65CB9D6D31682D74847631C51E766D01BD0A86063B65585CC994F6CDC0`.
- ECR/SCR records are siblings over raw, reference by key, and follow carry-supplied-or-residualize; they never author interpretive values from packet prose.
  - verify pointer: ECR submap, SHA256 `B1F2BD6D10B05D53F22052349784B3C0802E47A8A155AC81E43CE9CCDD2494A1`.
- Cleaning owns non-destructive transformation mechanics only; Judgment owns credibility, exclusion, demand, integrity effect, Decision Strength, and Action Ceiling.
  - verify pointer: Data/Cleaning boundary, SHA256 `3D50EEA84071490B563A36ABE37F974654A820274EFD767FFB37FFAB05F2509D`.

## Active Objective

Transfer IG reels-grid capture closeout into downstream work without lane blur. Items 1-3 are downstream code-enforcement candidates; item 4 remains Capture-owned; TikTok/YouTube lanes inherit generic social-source capture method lessons only.

## Exact Next Authorized Action

1. Projection lane: source-load this packet, the IG spec, and the projection doctrine; scope or implement a bounded IG reels-grid projection adapter that emits only mechanical source-visible rows: raw refs, row identity, source surfaces, selected fields, join status, selection limitations, candidate disagreements, caption anchors, timestamps, and mechanical mention frequencies.
2. ECR lane: source-load this packet and `docs/workflows/ecr_spine_submap_v0.md`; decide whether existing ECR/SCR consumers need references to the projection row handle or whether packet/slice keys are sufficient. Do not merge projection fields into ECR posture fields.
3. Cleaning lane: source-load this packet and the Data/Cleaning boundary; define how caption/product/brand strings and repeated mention groups may be normalized or clustered without losing originals or deciding paid/sponsored/campaign meaning.
4. Capture lane: keep static/profile-grid comparison as a separate future source surface if implemented; enforce static `view_count = not_applicable` and do not mix static rows into the reels traction series.
5. TikTok/YouTube lanes: start with a source-family probe using the generic social DOM/JSON learning capsule below; do not reuse IG selectors, endpoints, JSON keys, or count semantics.

## Authority And Source Ledger

- Repository instructions: `AGENTS.md`, SHA256 `4296E7617D8B2675881780CD7BE0704A00DCB17ADF7758243008DE956070940B`, load-bearing yes.
- Overlay authority:
  - `.agents/workflow-overlay/README.md`, SHA256 `7A30709D6011BD3F6458E926570B7164B91C7F3BF8BAE7DBD5A612A08DE81FDA`.
  - `.agents/workflow-overlay/source-loading.md`, SHA256 `58994CA788F1754DEA49277750B64C592DE0A4B7B19DBF495CE675DDB9C08181`.
  - `.agents/workflow-overlay/artifact-folders.md`, SHA256 `42D4F554DAF4BE6F0A4A9BCBE3C67FD74EEFCC063FC72B03E53E11242EDC7AE9`.
  - `.agents/workflow-overlay/decision-routing.md`, SHA256 `8CA8069E20C5803A1B645921ABBD986656739C943ED0996572E26A4B9430092E`.
- Target source ledger:
  - IG spec: SHA256 `A200F56527CEA2FDF4F289913C32C5BCD65B9FE7ECDB5A5C343FFA8D11B20D32`, load-bearing yes, reread before capture/projection claims.
  - Projection doctrine: SHA256 `BE22FD65CB9D6D31682D74847631C51E766D01BD0A86063B65585CC994F6CDC0`, load-bearing yes, reread before projection implementation or review.
  - ECR submap: SHA256 `B1F2BD6D10B05D53F22052349784B3C0802E47A8A155AC81E43CE9CCDD2494A1`, load-bearing yes, reread before ECR/SCR changes.
  - Data/Cleaning boundary: SHA256 `3D50EEA84071490B563A36ABE37F974654A820274EFD767FFB37FFAB05F2509D`, load-bearing yes, reread before Cleaning or cross-layer claims.
  - IG runner: SHA256 `A3F78150DE056BEACE5B37B480325EBF20E4D048348709C8AD9A8E30F84ABA32`, load-bearing yes for current implementation state.
  - IG parser: SHA256 `C3515683AF50EC155D6D5D8F296C3CD1C30560BE6D1E57C89A0D7EF8E477CE36`, load-bearing yes for row/candidate shape.
  - IG browser capture: SHA256 `3DAAD7D7B77067810B4CD00F18AFB9B8D3AF28668F29E95E76C559BE5EC19964`, load-bearing yes for capture privacy and passive JSON mechanics.
  - Packet assembly: SHA256 `F959E874FED3E5EF35A5D79CD9B7732AB4362341D74B9E29C0BB8A99CE83F5AB`, load-bearing yes for lake staging claim.
  - Focused IG runner tests: SHA256 `A57AD8FB662AAFEA708AFDF8B615B787176028635EDC14FF0552487EA0814C78`, load-bearing yes for stated test coverage.
- Source gaps: no TikTok/YouTube probe was run; no downstream IG reels-grid projection adapter was implemented; ECR/Cleaning consumption of IG projection rows was not implemented or reviewed.
- Not-proven boundaries: no scaled monitoring durability/rate envelope; no platform-stability claim; no ad/sponsorship/bot/demand/credibility classification.

## Current Task State

- Completed:
  - IG public `/reels/` capture runner and parser exist in the working tree.
  - IG spec records runner binding, static comparison policy, and lane wrap-up boundary.
  - Focused runner tests passed after review fixes.
  - One proxy-backed live capture for `jeremyfragrance` was admitted to a temp data-lake root; treat it as a probe artifact, not production proof.
- Partially completed:
  - Projection requirements are identified but not implemented for reels-grid rows.
  - ECR/Cleaning consumption boundary is identified but not patched.
  - Generic TikTok/YouTube method transfer is recorded here but not validated by platform probes.
- Broken or uncertain:
  - IG DOM hidden numeric ordering remains behavioral and must be refreshed.
  - Passive JSON surfaces and fields remain behavioral; endpoint/key stability is not a correctness claim.
  - Static/profile-grid comparison is deferred.

## Workspace State

- Branch: `main`
- Head: `b3072a0b`
- Dirty or untracked state before handoff, observed by `git status --short --branch` on 2026-06-22:
  - modified: `docs/hygiene/ig_creator_momentum_lane_handoff_v0.md`, `docs/workflows/orca_repo_map_v0.md`, `orca-harness/runners/run_source_capture_ig_calls_packet.py`, `orca-harness/source_capture/packet_assembly.py`
  - untracked relevant IG/capture files: `orca-harness/runners/run_source_capture_ig_reels_grid_packet.py`, `orca-harness/source_capture/ig_reels_grid.py`, `orca-harness/source_capture/ig_reels_grid_capture.py`, `orca-harness/tests/unit/test_ig_reels_grid.py`, `orca-harness/tests/unit/test_source_capture_ig_reels_grid_packet.py`, `orca/product/spines/capture/core/source_families/social_media/instagram/ig_profile_grid_dom_engagement_recon_and_spec_v0.md`
  - other untracked material existed: `.codex/hooks/run_orca_guard.py`, `_scratch/`, several docs/hygiene, docs/prompts, docs/review-outputs, docs/workflows, and `worktrees/` entries. Do not revert or assume ownership.
  - warning observed: `orca-harness/.pytest_tmp/` permission denied during status.
- Dirty or untracked state after writing this handoff file:
  - expected additional line: `?? docs/workflows/ig_reels_capture_to_projection_ecr_cleaning_handoff_v0.md`.
  - receiver must re-run `git status --short --branch` before editing.

## Changed / Inspected / Tested Files

- `orca/product/spines/capture/core/source_families/social_media/instagram/ig_profile_grid_dom_engagement_recon_and_spec_v0.md`: untracked; IG capture spec and lane boundary; key sections are Runner Binding, Static Comparison Policy, and Lane Wrap-Up.
- `orca-harness/runners/run_source_capture_ig_reels_grid_packet.py`: untracked; optimized IG packet runner; enforces one target output, row-limitation roll-up, unknown missing timestamp, and omitted coverage window when timestamp absent.
- `orca-harness/source_capture/ig_reels_grid.py`: untracked; DOM row parser and passive JSON candidate join helper; joins by shortcode and preserves source surfaces.
- `orca-harness/source_capture/ig_reels_grid_capture.py`: untracked; browser capture and passive JSON handling; strips cookie/set-cookie and redacts proxy endpoint/credentials/exit IP.
- `orca-harness/source_capture/packet_assembly.py`: modified; packet assembly and lake-owned staging.
- `orca-harness/tests/unit/test_source_capture_ig_reels_grid_packet.py`: untracked; focused runner tests.

## Frozen Decisions

- Item 4, static/profile-grid separation, is Capture lane. Projection/Cleaning consume a declared source surface and must not decide capture mix.
- Projection may count repeated brand/product/caption mentions mechanically but must not classify ads or sponsorship.
- Cleaning may normalize entities and cluster repeated strings only as a non-destructive ledger with originals preserved.
- ECR/SCR does not absorb projection rows as authoritative truth; it references packet/projection keys and residualizes missing inputs.

## Mutable Questions

- What exact IG reels-grid projection row schema should be implemented first?
- Does ECR need an explicit projection-row-handle reference for IG social rows, or are packet/slice keys enough?
- How much Cleaning should normalize caption/product strings before Judgment?
- Which TikTok/YouTube public routes expose DOM counts, passive JSON metadata, captions, timestamps, and item IDs?

## Superseded / Dangerous-To-Reuse Context

- Do not use the old IG calls runner as steady-state. It remains calibration/fallback only; optimized steady-state is the `/reels/` page-load runner.
- Do not treat `is_paid_partnership=false`, empty sponsor users, or missing affiliate fields as proof of not-ad.
- Do not infer exact dates from grid order; pinned or mixed content can distort position.
- Do not assume bigger viewport or zoom is automatically better; record viewport/zoom/browser bucket as behavioral variables.

## Generic Social DOM/JSON Capture Learning Capsule

Use this as method transfer for TikTok and YouTube lanes. It is not a platform claim.

- Start with a public creator/channel listing surface a human can view without authentication, such as videos, shorts, reels, or uploads.
- First prove what is visible without item-page fan-out: visible count text, hidden DOM text, item permalinks, profile snapshot fields, route/block state.
- Treat rendered DOM and passive page-load JSON as separate source surfaces. Do not collapse them into one truth field.
- Join only by stable item identity: shortcode, video ID, canonical permalink path, or platform item ID. Never use grid index as identity across days.
- Preserve candidate values before selecting. If DOM count, passive JSON count, and profile-feed count disagree, emit candidates with `source_surface`, `capture_mode`, and limitation reason.
- Selection policy must be versioned and visible. A chosen `view_count`, `like_count`, or `comment_count` without source provenance is a bug for downstream evidence.
- Passive JSON may include more items than the visible grid because pages preload. Useful, but not guaranteed; record candidate count and overlap count.
- Bigger viewport can change passive JSON depth without changing visible DOM count; zoom/browser bucket can also change route behavior. Record viewport, zoom, and final URL.
- Strip cookies and `set-cookie` headers. Do not serialize proxy endpoint, credentials, exit IP, browser profile path, storage state, raw media bytes, or private session material into packets.
- Captions, hashtags, sounds, paid labels, affiliate fields, sponsor users, pinned markers, and product fields are source-visible candidates. They are not ad/sponsorship conclusions.
- Engagement counts are raw public traction inputs, not demand, credibility, integrity, or action signals by themselves.
- Repeated brand/product mentions are Projection/Cleaning mechanical signals: count them, normalize them, link originals, and defer meaning.
- Exact timestamps come from joined source data only. Do not extrapolate exact publish dates from position.
- Platform-specific lanes should discover their own source-surface vocabulary, for example `dom_grid_engagement`, `passive_page_json_metadata`, `player_or_initial_state_json`, `profile_json_metadata`, or `item_page_metadata`.
- Every source-family probe should return a route status even when blocked: final URL, login/challenge/interstitial markers, parsed item count, source-surface count, and limitations.

## Commands And Verification Evidence

- Command: `python -m py_compile runners\run_source_capture_ig_reels_grid_packet.py tests\unit\test_source_capture_ig_reels_grid_packet.py`
  - Result: passed on 2026-06-22 in `orca-harness`.
  - Re-run target: before claiming code still compiles after edits.
- Command: `python -m pytest tests\unit\test_source_capture_ig_reels_grid_packet.py -q`
  - Result: `5 passed` on 2026-06-22 in `orca-harness`.
  - Re-run target: before relying on focused runner behavior after edits.
- Command: `python -m pytest tests\unit\test_ig_reels_grid.py tests\unit\test_source_capture_ig_reels_grid_packet.py tests\unit\test_source_capture_ig_calls_packet.py tests\unit\test_run_source_capture_packet_lake.py -q`
  - Result: `32 passed` on 2026-06-22 in `orca-harness`.
  - Re-run target: before claiming broader IG/source-capture packet integration remains green.
- Command: `Get-FileHash -Algorithm SHA256 <source ledger files>`
  - Result: hashes recorded in Authority And Source Ledger.
  - Re-run target: receiver should rehash load-bearing sources before strict/actionable continuation.

## Blockers And Risks

- Downstream lane may overread this handoff as implementation authorization. The receiving lane must follow current user instruction and Orca implementation-authorization rules.
- Candidate mention frequency can look like ad classification. Use mechanical names like `caption_surface_mention_frequency`; ban conclusion names like `sponsored_ad_detected` outside Judgment.
- TikTok/YT lanes may copy IG-specific mechanics. Use the generic learning capsule, then prove each platform's route with its own probe.

## Confirm-Don't-Trust Load Checklist

- Load-bearing facts the receiver must re-verify before acting:
  - branch/head and dirty state;
  - IG spec lane boundary and hashes;
  - Projection doctrine mechanical-only/no-salience rules;
  - ECR submap carry-or-residualize/reference-never-merge rules;
  - Data/Cleaning boundary and Cleaning vs Judgment split;
  - runner/parser/test file contents if implementation continues;
  - test results if code changes are made.
- Compare target for each:
  - hashes in Authority And Source Ledger;
  - fresh `git status --short --branch`;
  - fresh `git rev-parse --short HEAD`;
  - rerun tests when code changes are relevant.
- Load outcomes and what each means:
  - `REUSE`: all load-bearing facts match; continue from Exact Next Authorized Action.
  - `PARTIAL_REUSE`: optional or non-load-bearing facts drifted; reuse verified lane boundaries and refresh the rest.
  - `STALE_REREAD_REQUIRED`: material source drifted but can be reread and re-derived.
  - `BLOCKED_DRIFT`: drift conflicts with scope, ownership, or dirty-state safety.
  - `BLOCKED_MISSING_PACKET`: this file is absent or unreadable.
  - `BLOCKED_UNVERIFIABLE`: a load-bearing claim lacks a compare target and cannot be re-derived.
- Sources that must be reread if drift is detected:
  - IG spec, Projection doctrine, ECR submap, Data/Cleaning boundary, and affected runner/parser/test files.

## Do Not Forget

Projection can count and carry; Cleaning can normalize and cluster mechanically; ECR can reference and residualize; Judgment decides what it means. Static comparison remains Capture-owned. TikTok/YouTube inherit the method, not the IG implementation.
