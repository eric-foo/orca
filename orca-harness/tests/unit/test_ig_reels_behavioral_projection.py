from __future__ import annotations

import pytest

from source_capture.ig_reels_behavioral_projection import (
    IG_REELS_BEHAVIORAL_PROJECTION_METHOD,
    project_ig_reels_behavioral_item,
)


_SHORTCODE = "DaA8n7EhqTR"


def _grid_row(**overrides):
    row = {
        "row_id": "grid-packet-1:ig_reels_grid_00:view_count",
        "raw_ref": {"packet_id": "grid-packet-1", "slice_id": "ig_reels_grid_00"},
        "content_shortcode": _SHORTCODE,
        "metric": "view_count",
        "posture": "observed",
        "value": 1200,
        "chosen_source_surface": "clips/user",
        "source_surface_count_candidates": [
            {"source_surface": "clips/user", "value": 1200},
            {"source_surface": "dom_grid_engagement", "value": 900, "raw_text": "900"},
        ],
        "join_status": "joined_by_shortcode",
        "selection_limitations": ["likes_hidden"],
        "capture_time": "2026-06-29T00:00:00Z",
        "source_visible_fields": {"media_product_type": "clips"},
        "residuals": [],
    }
    row.update(overrides)
    return row


def _comment_set(**overrides):
    row = {
        "reel_shortcode": _SHORTCODE,
        "record_id": "deepcap_1.json",
        "generated_at": "2026-06-29T00:01:00Z",
        "comment_count": 1,
        "comments": [{"comment_id": "c1", "author_username": "zoe", "text": "works"}],
        "media_provenance": {"audio_handle_used": True, "media_host": "x.fbcdn.net"},
    }
    row.update(overrides)
    return row


def _audio_transcript(**overrides):
    row = {
        "video_id": _SHORTCODE,
        "shortcode": _SHORTCODE,
        "record_id": "asr_small__abc123",
        "platform": "instagram",
        "posture": "transcribed",
        "cue_count": 1,
        "cues": [{"start_ms": 0, "end_ms": 90, "text": "hello"}],
        "provenance": {
            "source_packet_id": "audio-packet-1",
            "source_file_id": "audio-file-1",
            "source_sha256": "abc123",
        },
        "retrieval_time_utc": "2026-06-29T00:02:00Z",
    }
    row.update(overrides)
    return row


def _deep_transcript(**overrides):
    row = {
        "reel_shortcode": _SHORTCODE,
        "record_id": "deepcap_1.json",
        "generated_at": "2026-06-29T00:01:00Z",
        "transcript_posture": "ok",
        "cue_count": 1,
        "cues": [{"start_ms": 0, "end_ms": 90, "text": "hello"}],
        "media_provenance": {"audio_handle_used": True, "media_host": "x.fbcdn.net"},
    }
    row.update(overrides)
    return row


def test_projects_complete_audio_backed_ig_behavior_record() -> None:
    projection = project_ig_reels_behavioral_item(
        platform_item_id=_SHORTCODE,
        grid_rows=[_grid_row()],
        comment_sets=[_comment_set()],
        standalone_audio_transcript_records=[_audio_transcript()],
        extraction_results=[
            {
                "anchor": "audio-packet-1",
                "video_id": _SHORTCODE,
                "status": "extracted",
                "path": "derived/audio-packet-1/product_mentions/r1",
            }
        ],
    )

    assert projection["projection_method"] == IG_REELS_BEHAVIORAL_PROJECTION_METHOD
    assert projection["platform_item_id"] == _SHORTCODE
    assert projection["candidate"]["ranking_basis"] == "views_then_engagement"
    assert projection["candidate"]["limitations"] == ["likes_hidden"]
    assert projection["comments"]["posture"] == "captured"
    assert projection["transcript"]["source_count"] == 1
    assert projection["transcript"]["sources"][0]["source_route"] == "standalone_audio_packet"
    assert projection["transcript"]["sources"][0]["extraction_status"] == "extracted"
    assert projection["transcript"]["canonical_source"]["source_route"] == "standalone_audio_packet"
    assert projection["behavioral_completeness"] == {
        "status": "complete",
        "complete": True,
        "residuals": [],
    }
    assert projection["persistence_correlation"]["grid_packet_ids"] == ["grid-packet-1"]
    assert projection["persistence_correlation"]["audio_packet_ids"] == ["audio-packet-1"]
    assert projection["persistence_correlation"]["extraction_record_paths"] == [
        "derived/audio-packet-1/product_mentions/r1"
    ]


def test_deep_capture_transcript_is_visible_but_residualized_until_feed_adapter_exists() -> None:
    projection = project_ig_reels_behavioral_item(
        platform_item_id=_SHORTCODE,
        grid_rows=[_grid_row()],
        comment_sets=[_comment_set()],
        standalone_audio_transcript_records=[_audio_transcript()],
        deep_capture_transcript_records=[_deep_transcript()],
        extraction_results=[{"anchor": "audio-packet-1", "video_id": _SHORTCODE, "status": "extracted"}],
    )

    deep_source = [
        source
        for source in projection["transcript"]["sources"]
        if source["source_route"] == "deep_capture_render_audio"
    ][0]
    assert deep_source["posture"] == "transcribed"
    assert deep_source["extraction_eligible"] is False
    assert deep_source["non_eligible_reason"] == "deep_capture_not_in_extraction_feed"
    assert deep_source["extraction_status"] == "not_extraction_eligible"
    assert projection["transcript"]["canonical_source"]["source_route"] == "deep_capture_render_audio"
    assert projection["behavioral_completeness"]["status"] == "complete_with_residuals"
    assert projection["behavioral_completeness"]["complete"] is False
    assert (
        "ig_transcript_source_not_extraction_eligible:"
        f"{_SHORTCODE}:asr:deepcap_1.json"
    ) in projection["behavioral_completeness"]["residuals"]


def test_failed_extraction_stays_visible_and_blocks_complete_claim() -> None:
    projection = project_ig_reels_behavioral_item(
        platform_item_id=_SHORTCODE,
        standalone_audio_transcript_records=[_audio_transcript()],
        extraction_results=[
            {
                "anchor": "audio-packet-1",
                "video_id": _SHORTCODE,
                "status": "failed",
                "error": "RuntimeError: bad extraction",
            }
        ],
    )

    assert projection["extraction"]["rollup"]["status"] == "failed"
    assert projection["behavioral_completeness"]["complete"] is False
    assert projection["extraction"]["source_statuses"][0]["extraction_error"] == "RuntimeError: bad extraction"
    assert (
        "ig_transcript_extraction_failed:audio-packet-1:asr:asr_small__abc123"
    ) in projection["behavioral_completeness"]["residuals"]
    assert f"ig_grid_candidate_absent:{_SHORTCODE}" in projection["behavioral_completeness"]["residuals"]
    assert f"ig_comments_not_attempted:{_SHORTCODE}" in projection["behavioral_completeness"]["residuals"]


def test_mismatched_transcript_source_is_residualized_and_ignored() -> None:
    projection = project_ig_reels_behavioral_item(
        platform_item_id=_SHORTCODE,
        standalone_audio_transcript_records=[_audio_transcript(video_id="OtherShort")],
    )

    assert projection["transcript"]["source_count"] == 0
    assert projection["extraction"]["rollup"]["status"] == "no_extraction_eligible_sources"
    assert "ig_transcript_source_shortcode_mismatch:OtherShort" in projection["behavioral_completeness"]["residuals"]


def test_canonical_standalone_audio_prefers_latest_capture_time() -> None:
    projection = project_ig_reels_behavioral_item(
        platform_item_id=_SHORTCODE,
        standalone_audio_transcript_records=[
            _audio_transcript(
                record_id="asr_old",
                retrieval_time_utc="2026-06-29T00:01:00Z",
                provenance={"source_packet_id": "audio-old"},
            ),
            _audio_transcript(
                record_id="asr_new",
                retrieval_time_utc="2026-06-29T00:03:00Z",
                provenance={"source_packet_id": "audio-new"},
            ),
        ],
        extraction_results=[
            {"anchor": "audio-old", "video_id": _SHORTCODE, "status": "extracted"},
            {"anchor": "audio-new", "video_id": _SHORTCODE, "status": "extracted"},
        ],
    )

    assert projection["transcript"]["canonical_source"]["transcript_anchor"] == "audio-new"
    assert projection["behavioral_completeness"]["status"] == "complete"


def test_requires_platform_item_id() -> None:
    with pytest.raises(ValueError, match="platform_item_id is required"):
        project_ig_reels_behavioral_item(platform_item_id=" ")
