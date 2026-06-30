# YouTube Behavioral Measurement Corpus Receipt v0

```yaml
retrieval_header_version: 1
artifact_role: Workflow receipt
scope: Canonical F-lake YouTube behavioral measurement corpus after expanding beyond the initial two-video proof.
use_when:
  - Checking whether YouTube behavioral evidence is statistically measurable.
  - Distinguishing caption-route source/caption coverage from full behavioral completion.
  - Recovering the current YouTube canonical F-lake corpus counts after the 2026-06-30 expansion run.
open_next:
  - docs/workflows/ig_youtube_behavioral_e2e_closeout_receipt_v0.md
  - docs/workflows/youtube_behavioral_contract_from_merged_main_v0.md
  - orca-harness/runners/run_source_capture_youtube_watch_packet.py
  - orca-harness/runners/run_source_capture_youtube_caption_packet.py
  - orca-harness/runners/run_source_capture_youtube_asr_packet.py
  - orca-harness/youtube_capture/behavioral_projection.py
stale_if:
  - YouTube packets, transcript packets, or product-mention records are added to or removed from F:/orca-data-lake.
  - The YouTube behavioral projection, transcript discovery, product-extraction, or source-lineage semantics change.
  - A later YouTube measurement receipt supersedes this corpus.
authority_boundary: retrieval_only
```

## Short Answer

The corpus is now large enough to measure the **YouTube caption-route source/caption layer**,
but it is still not large enough to statistically claim **full behavioral completeness**.

Observed canonical `F:/orca-data-lake` state:

```text
YOUTUBE_PACKET_COUNT 62
YOUTUBE_VIDEO_COUNT 32
SURFACE_COMBOS
youtube_captions+youtube_watch_metadata_comments 30
youtube_watch_metadata_comments 2
PROJECTION_STATUS_COUNTS
complete 2
no_extraction_eligible_sources 2
not_attempted 28
YOUTUBE_PRODUCT_RECORDS 2
```

Interpretation:

- Caption-route source/caption coverage is measurable at `n=30`: every item in that cell has both
  `youtube_watch_metadata_comments` and `youtube_captions` packets.
- Full behavioral completion is only `2/32` over the observed YouTube video set, because only two
  videos have source-backed product-mention records. The other 28 caption-ready videos are
  `not_attempted` at product extraction.
- ASR/no-caption fallback is not measurable: the attempted ASR seed wrote a watch packet, but audio
  download failed and the caption probe reported the video as removed/unavailable.
- The seed is a fragrance YouTube Shorts seed, not a random platform sample; do not generalize to all
  YouTube or all creator content.

## Corpus Build

The expansion used the existing YouTube Shorts fragrance seed as the candidate source and targeted
30 caption-route videos with both watch metadata/comments and caption transcript packets.

Starting state before this pass:

```text
START_WATCH 2 ['VOGZUccarFc', 'ljZ7_JHXNdw']
START_CAPTION 2 ['VOGZUccarFc', 'ljZ7_JHXNdw']
START_COMPLETE 2 ['VOGZUccarFc', 'ljZ7_JHXNdw']
```

Batch result:

```text
FINAL_WATCH 31
FINAL_CAPTION 30
FINAL_COMPLETE 30
RESULT_COUNTS {"attempts": 30, "caption_failed": 2, "caption_ok": 28, "watch_failed": 1, "watch_ok": 29}
```

Additional ASR-route probe:

```text
as7hye0qgYc watch packet: wrote F:/orca-data-lake/raw/f69/01KWBPYB766MZ89C2D23VCS0DN
as7hye0qgYc ASR audio download: failed with "audio download failed"
as7hye0qgYc caption probe: failed with "Video unavailable. This video has been removed by the uploader"
```

Failed/residual candidates observed during corpus construction:

| Video id | Route expectation | Observed result | Interpretation |
| --- | --- | --- | --- |
| `-V7MN2IWMpA` | caption | runner invocation failed with argparse rc=2 for both watch and caption | Batch invocation edge for leading-dash video ids; not a source-route result. Use `--video-id=-V7MN2IWMpA` or patch a batch helper before retrying. |
| `JcwT5rvhXIc` | caption | watch packet wrote; caption failed as removed by uploader | Current-source unavailability; contributes watch-only/no-transcript case, not caption-route success. |
| `as7hye0qgYc` | ASR | watch packet wrote; ASR audio download failed; caption probe says removed by uploader | ASR/no-caption stratum remains unmeasured and needs replacement candidates. |

Complete caption-route video ids:

```text
17mhHUkRLvg, 1K9ej-6aP6g, 5QDcTenklxg, 5e4y5yNagRI, 6k8ebJw50tU, 7S40eU8FDCY, Fd-aChpt_Ss, FqTrOZbh_DE, JMmEIv_oG4o, Ln1LUflj8d0, MN3AI-mrPWk, Tb-_V-JVNfk, Uj4bVTM6dm8, VOGZUccarFc, WEqUWKA4FUI, WcSRnnwSAJM, XDscn2sgW3w, _Gp2AmN74E8, bPJCH9iQUhI, ekaQONEC2ys, hfyoVdOAYt4, jo03W7cBwBM, ljZ7_JHXNdw, rmDwkTrzNxo, sy-rczzFrYg, uaCSynFfPpc, vl-QUTwtneY, vtwo-iaOszA, xK8bmugSpgQ, xZ6vd9fyBbw
```

Watch-only video ids:

```text
JcwT5rvhXIc, as7hye0qgYc
```

## Product Extraction Boundary

No provider extraction was available during this pass:

```text
OPENAI_API_KEY_SET False
ANTHROPIC_API_KEY_SET False
ORCA_PRODUCT_EXTRACT_PROVIDER <unset>
ORCA_PRODUCT_EXTRACT_MODEL <unset>
```

The only YouTube product-mention records currently present for this corpus are the two earlier
explicitly labeled operator records:

| Video id | Anchor | Record id | Status | Mentions | Backend |
| --- | --- | --- | --- | ---: | --- |
| `VOGZUccarFc` | `01KWBNSQ9VS2GBHYM2XZKF9CYV` | `mentions_codex_operator_manual_v0__6ae6f45ebdbc94db.json` | `extracted` | 10 | `codex_operator_manual_current_thread` |
| `ljZ7_JHXNdw` | `01KWBNRPGW6CQ021CWCSTNFJF0` | `mentions_codex_operator_manual_v0__49f6b5ed7347c215.json` | `extracted` | 2 | `codex_operator_manual_current_thread` |

This means the current `not_attempted` count is an extraction-run gap, not evidence that captions are
missing or non-extractable.

## Projection Matrix

| Video id | Surfaces | Status | Sources | Eligible | Complete sources | Caption cues | Extraction statuses |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- |
| `17mhHUkRLvg` | `youtube_captions+youtube_watch_metadata_comments` | `not_attempted` | 1 | 1 | 0 | 101 | `not_attempted` |
| `1K9ej-6aP6g` | `youtube_captions+youtube_watch_metadata_comments` | `not_attempted` | 1 | 1 | 0 | 65 | `not_attempted` |
| `5QDcTenklxg` | `youtube_captions+youtube_watch_metadata_comments` | `not_attempted` | 1 | 1 | 0 | 85 | `not_attempted` |
| `5e4y5yNagRI` | `youtube_captions+youtube_watch_metadata_comments` | `not_attempted` | 1 | 1 | 0 | 13 | `not_attempted` |
| `6k8ebJw50tU` | `youtube_captions+youtube_watch_metadata_comments` | `not_attempted` | 1 | 1 | 0 | 27 | `not_attempted` |
| `7S40eU8FDCY` | `youtube_captions+youtube_watch_metadata_comments` | `not_attempted` | 1 | 1 | 0 | 43 | `not_attempted` |
| `Fd-aChpt_Ss` | `youtube_captions+youtube_watch_metadata_comments` | `not_attempted` | 1 | 1 | 0 | 31 | `not_attempted` |
| `FqTrOZbh_DE` | `youtube_captions+youtube_watch_metadata_comments` | `not_attempted` | 1 | 1 | 0 | 29 | `not_attempted` |
| `JMmEIv_oG4o` | `youtube_captions+youtube_watch_metadata_comments` | `not_attempted` | 1 | 1 | 0 | 47 | `not_attempted` |
| `JcwT5rvhXIc` | `youtube_watch_metadata_comments` | `no_extraction_eligible_sources` | 0 | 0 | 0 | 0 | `` |
| `Ln1LUflj8d0` | `youtube_captions+youtube_watch_metadata_comments` | `not_attempted` | 1 | 1 | 0 | 89 | `not_attempted` |
| `MN3AI-mrPWk` | `youtube_captions+youtube_watch_metadata_comments` | `not_attempted` | 1 | 1 | 0 | 31 | `not_attempted` |
| `Tb-_V-JVNfk` | `youtube_captions+youtube_watch_metadata_comments` | `not_attempted` | 1 | 1 | 0 | 53 | `not_attempted` |
| `Uj4bVTM6dm8` | `youtube_captions+youtube_watch_metadata_comments` | `not_attempted` | 1 | 1 | 0 | 53 | `not_attempted` |
| `VOGZUccarFc` | `youtube_captions+youtube_watch_metadata_comments` | `complete` | 1 | 1 | 1 | 29 | `extracted` |
| `WEqUWKA4FUI` | `youtube_captions+youtube_watch_metadata_comments` | `not_attempted` | 1 | 1 | 0 | 63 | `not_attempted` |
| `WcSRnnwSAJM` | `youtube_captions+youtube_watch_metadata_comments` | `not_attempted` | 1 | 1 | 0 | 49 | `not_attempted` |
| `XDscn2sgW3w` | `youtube_captions+youtube_watch_metadata_comments` | `not_attempted` | 1 | 1 | 0 | 45 | `not_attempted` |
| `_Gp2AmN74E8` | `youtube_captions+youtube_watch_metadata_comments` | `not_attempted` | 1 | 1 | 0 | 47 | `not_attempted` |
| `as7hye0qgYc` | `youtube_watch_metadata_comments` | `no_extraction_eligible_sources` | 0 | 0 | 0 | 0 | `` |
| `bPJCH9iQUhI` | `youtube_captions+youtube_watch_metadata_comments` | `not_attempted` | 1 | 1 | 0 | 55 | `not_attempted` |
| `ekaQONEC2ys` | `youtube_captions+youtube_watch_metadata_comments` | `not_attempted` | 1 | 1 | 0 | 93 | `not_attempted` |
| `hfyoVdOAYt4` | `youtube_captions+youtube_watch_metadata_comments` | `not_attempted` | 1 | 1 | 0 | 17 | `not_attempted` |
| `jo03W7cBwBM` | `youtube_captions+youtube_watch_metadata_comments` | `not_attempted` | 1 | 1 | 0 | 35 | `not_attempted` |
| `ljZ7_JHXNdw` | `youtube_captions+youtube_watch_metadata_comments` | `complete` | 1 | 1 | 1 | 37 | `extracted` |
| `rmDwkTrzNxo` | `youtube_captions+youtube_watch_metadata_comments` | `not_attempted` | 1 | 1 | 0 | 105 | `not_attempted` |
| `sy-rczzFrYg` | `youtube_captions+youtube_watch_metadata_comments` | `not_attempted` | 1 | 1 | 0 | 47 | `not_attempted` |
| `uaCSynFfPpc` | `youtube_captions+youtube_watch_metadata_comments` | `not_attempted` | 1 | 1 | 0 | 75 | `not_attempted` |
| `vl-QUTwtneY` | `youtube_captions+youtube_watch_metadata_comments` | `not_attempted` | 1 | 1 | 0 | 61 | `not_attempted` |
| `vtwo-iaOszA` | `youtube_captions+youtube_watch_metadata_comments` | `not_attempted` | 1 | 1 | 0 | 55 | `not_attempted` |
| `xK8bmugSpgQ` | `youtube_captions+youtube_watch_metadata_comments` | `not_attempted` | 1 | 1 | 0 | 43 | `not_attempted` |
| `xZ6vd9fyBbw` | `youtube_captions+youtube_watch_metadata_comments` | `not_attempted` | 1 | 1 | 0 | 113 | `not_attempted` |

## Claim Levels

| Claim | Status | Basis |
| --- | --- | --- |
| YouTube caption-route source/caption corpus is statistically measurable | observed | 30 videos with both watch metadata/comments and caption transcript packets |
| YouTube caption-route full behavioral completion is statistically measurable | not yet | only 2 of 30 caption-ready videos have product-mention records |
| YouTube ASR/no-caption route is statistically measurable | not observed | attempted ASR seed is currently unavailable; no complete ASR transcript packet observed |
| YouTube platform-wide behavioral completeness is statistically measurable | not proven | corpus is seed-biased and missing ASR/provider-extraction coverage |
| IG/YT platform-wide behavioral completeness is proven | not proven | IG residuals remain and YouTube full-path corpus is incomplete |

## Next Non-Admin Steps

1. Run product extraction for the 28 `not_attempted` caption-ready YouTube transcripts, either with
   a provider API configuration or an explicitly accepted operator/Codex extraction batch. Keep the
   backend label honest.
2. Replace the stale ASR seed with reachable ASR/no-caption candidates and capture at least 5, ideally
   10, complete ASR transcript cases before claiming fallback-route measurement.
3. Fix or wrap batch invocation for leading-dash YouTube ids before retrying `-V7MN2IWMpA`.
4. Rerun this receipt after extraction and ASR expansion; only then set a behavioral-completeness
   threshold such as per-route completion rate and residual ceilings.

## Non-Claims

- Not full YouTube behavioral completeness.
- Not ASR/no-caption fallback validation.
- Not live provider-API extraction.
- Not random or platform-wide YouTube measurement.
- Not shared IG/YT core, production readiness, scheduler behavior, Judgment, or gold verdict.
