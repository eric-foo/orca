"""Driver + daemon-ready runner: offline integration tests over a `for_test` data lake.

No network, no credentials. Commits real caption / ASR transcripts into a temp lake, runs the
extractor through a fake transport, and asserts mentions land in the silver lane, that the
runner is idempotent (skip-if-done), and that the json3->cues parser preserves timing.
"""

from __future__ import annotations

import json
from typing import Any

import pytest

from cleaning.audience_extractor import RawApiProvider
from cleaning.transcript_product_extractor import TranscriptInput
from cleaning.transcript_product_lake import (
    PRODUCT_MENTIONS_LANE,
    PRODUCT_MENTIONS_SET_LANE,
    cues_from_json3,
    extract_products_into_lake,
    mentions_record_id,
)
from data_lake.root import DataLakeRoot
from runners.run_transcript_product_extract import find_transcripts, run_extraction
from source_capture.transcript.asr_packet import write_asr_transcript
from source_capture.transcript.youtube_captions import CaptionFetch
from source_capture.transcript.caption_packet import write_caption_packet

_ANCHOR = "ANCHORTEST0123456789ABCDEF"
_PROVIDER = RawApiProvider.ANTHROPIC_MESSAGES


def _cues() -> list[dict]:
    return [
        {"start_ms": 1000, "end_ms": 3000, "text": "Today I'm testing Dior Sauvage Elixir"},
        {"start_ms": 3000, "end_ms": 6000, "text": "and it is an absolute beast in the heat"},
    ]


def _item(**over: Any) -> dict[str, Any]:
    base = dict(
        brand="Dior", line="Sauvage Elixir", concentration="elixir", stance_vote=0.8,
        creator_authored=True, possible_negation_or_irony=False, extractor_confidence=0.9,
        source_pointer="absolute beast in the heat",
    )
    base.update(over)
    return base


def _anthropic(items: list[dict[str, Any]]) -> str:
    return json.dumps({"content": [{"type": "text", "text": json.dumps(items)}]})


class FakeTransport:
    def __init__(self, canned: str) -> None:
        self.canned = canned

    def post_json(self, url, headers, body, timeout_seconds):  # noqa: ANN001
        return self.canned


def _transcript() -> TranscriptInput:
    return TranscriptInput("vid12345678", _ANCHOR, "asr", _cues())


# --- json3 -> cues (timing preserved) ----------------------------------------


def test_cues_from_json3_preserves_timing_and_dedups() -> None:
    raw = json.dumps(
        {
            "events": [
                {"tStartMs": 1000, "dDurationMs": 2000, "segs": [{"utf8": "hello world"}]},
                {"tStartMs": 1000, "dDurationMs": 2000, "segs": [{"utf8": "hello world"}]},  # rolling dup
                {"tStartMs": 3000, "dDurationMs": 1500, "segs": [{"utf8": "second line"}]},
                {"segs": []},  # empty -> skipped
            ]
        }
    ).encode("utf-8")
    cues = cues_from_json3(raw)
    assert cues == [
        {"start_ms": 1000, "end_ms": 3000, "text": "hello world"},
        {"start_ms": 3000, "end_ms": 4500, "text": "second line"},
    ]


# --- driver: persists to the silver lane + write-once -------------------------


def test_driver_persists_to_silver_lane(tmp_path) -> None:
    data_root = DataLakeRoot.for_test(tmp_path / "lake")
    paths = extract_products_into_lake(
        data_root=data_root, transcript=_transcript(), transport=FakeTransport(_anthropic([_item()])),
        provider=_PROVIDER, model="test-model", api_key="k",
    )
    assert PRODUCT_MENTIONS_LANE in paths
    rid = mentions_record_id(_transcript(), "test-model")
    assert data_root.is_record_set_complete(
        subtree="derived", raw_anchor=_ANCHOR, record_id=rid, completion_lane=PRODUCT_MENTIONS_SET_LANE,
    )
    written = json.loads(paths[PRODUCT_MENTIONS_LANE].read_text(encoding="utf-8"))
    assert written["mention_count"] == 1
    assert written["mentions"][0]["start_ms"] == 3000  # CE5 timestamp from the cue


def test_driver_refuses_duplicate_write(tmp_path) -> None:
    data_root = DataLakeRoot.for_test(tmp_path / "lake")
    kw = dict(data_root=data_root, transcript=_transcript(), transport=FakeTransport(_anthropic([_item()])),
              provider=_PROVIDER, model="test-model", api_key="k")
    extract_products_into_lake(**kw)
    with pytest.raises(Exception):  # write-once: append_record_set refuses an existing set
        extract_products_into_lake(**kw)


# --- runner: ASR path, end-to-end + idempotent --------------------------------


def _commit_asr_transcript(data_root) -> None:
    write_asr_transcript(
        video_id="vid12345678", audio_bytes=b"fake-audio-bytes", audio_ext="m4a",
        transcribe_fn=lambda _path: ("transcribed", _cues(), {"tool": "faster-whisper", "model": "test"}),
        data_root=data_root,
    )


def test_runner_extracts_asr_transcript_then_skips_on_rerun(tmp_path) -> None:
    data_root = DataLakeRoot.for_test(tmp_path / "lake")
    _commit_asr_transcript(data_root)

    transport = FakeTransport(_anthropic([_item()]))
    first = run_extraction(data_root=data_root, transport=transport, provider=_PROVIDER, model="m", api_key="k")
    assert len(first) == 1
    assert first[0]["status"] == "extracted"
    assert first[0]["video_id"] == "vid12345678"

    # idempotent: a second pass finds the completed set and skips (does not re-extract).
    second = run_extraction(data_root=data_root, transport=transport, provider=_PROVIDER, model="m", api_key="k")
    assert len(second) == 1
    assert second[0]["status"] == "skipped_done"


# --- runner: caption path, end-to-end -----------------------------------------


def test_runner_extracts_caption_transcript(tmp_path) -> None:
    data_root = DataLakeRoot.for_test(tmp_path / "lake")
    json3 = json.dumps(
        {
            "events": [
                {"tStartMs": 1000, "dDurationMs": 2000, "segs": [{"utf8": "Today I'm testing Dior Sauvage Elixir"}]},
                {"tStartMs": 3000, "dDurationMs": 3000, "segs": [{"utf8": "and it is an absolute beast in the heat"}]},
            ]
        }
    ).encode("utf-8")
    cap = CaptionFetch(
        video_id="vid12345678", found=True, note="ok", lang="en", caption_kind="auto",
        json3_bytes=json3, flat_text="x", cue_count=2, title="T", channel_id="UC",
        publish_date_iso="2026-06-20", duration_s=42,
        tooling={"tool": "yt-dlp", "tool_version": "x", "client": "yt-dlp-default"},
    )
    write_caption_packet(cap, data_root=data_root, decision_question="Q")

    results = run_extraction(
        data_root=data_root, transport=FakeTransport(_anthropic([_item()])),
        provider=_PROVIDER, model="m", api_key="k",
    )
    assert len(results) == 1
    assert results[0]["status"] == "extracted"


def test_find_transcripts_empty_lake_is_empty(tmp_path) -> None:
    data_root = DataLakeRoot.for_test(tmp_path / "lake")
    assert find_transcripts(data_root) == []
