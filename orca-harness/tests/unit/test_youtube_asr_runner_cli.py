from __future__ import annotations

from pathlib import Path

from data_lake import root as root_module
from runners import run_source_capture_youtube_asr_packet as runner

_LEADING_DASH_VIDEO_ID = "-V7MN2IWMpA"


def test_youtube_asr_runner_accepts_leading_dash_video_id(monkeypatch, tmp_path: Path) -> None:
    resolved_root = object()

    class FakeDataLakeRoot:
        @staticmethod
        def resolve(*, explicit):
            assert explicit == str(tmp_path / "lake")
            return resolved_root

    def fake_download(video_id: str):
        assert video_id == _LEADING_DASH_VIDEO_ID
        return b"audio", "webm"

    def fake_write_asr_transcript(**kwargs):
        assert kwargs["video_id"] == _LEADING_DASH_VIDEO_ID
        assert kwargs["audio_bytes"] == b"audio"
        assert kwargs["audio_ext"] == "webm"
        assert kwargs["data_root"] is resolved_root
        return 0, "derived/path"

    monkeypatch.setattr(root_module, "DataLakeRoot", FakeDataLakeRoot)
    monkeypatch.setattr(runner, "download_audio", fake_download)
    monkeypatch.setattr(runner, "write_asr_transcript", fake_write_asr_transcript)

    assert runner.main(["--video-id", _LEADING_DASH_VIDEO_ID, "--data-root", str(tmp_path / "lake")]) == 0
