from __future__ import annotations

import json
from pathlib import Path

import pytest

from runners import run_fragrantica_mgt_capture as runner


_URL = "https://www.fragrantica.com/perfume/Chanel/Chanel-No-5-33519.html"


def _write_manifest(packet_dir: Path, *, packet_id: str, source_surface: str) -> None:
    packet_dir.mkdir(parents=True, exist_ok=True)
    (packet_dir / "manifest.json").write_text(
        json.dumps(
            {
                "packet_id": packet_id,
                "source_family": runner.SOURCE_FAMILY,
                "source_surface": source_surface,
            }
        ),
        encoding="utf-8",
    )


def test_fragrantica_mgt_capture_composes_three_packets_and_summary(tmp_path: Path) -> None:
    calls: list[dict[str, object]] = []

    def fake_http_runner(**kwargs: object) -> tuple[int, str]:
        calls.append(dict(kwargs))
        packet_dir = Path(kwargs["output_directory"])
        _write_manifest(
            packet_dir,
            packet_id="01KW0000000000000000000001",
            source_surface=str(kwargs["source_surface"]),
        )
        return 0, str(packet_dir)

    def fake_cloakbrowser_runner(**kwargs: object) -> tuple[int, str]:
        calls.append(dict(kwargs))
        packet_dir = Path(kwargs["output_directory"])
        packet_id = (
            "01KW0000000000000000000002"
            if kwargs["source_surface"] == runner.INITIAL_VIEWPORT_SURFACE
            else "01KW0000000000000000000003"
        )
        _write_manifest(
            packet_dir,
            packet_id=packet_id,
            source_surface=str(kwargs["source_surface"]),
        )
        return 0, str(packet_dir)

    output_root = tmp_path / "fragrantica_mgt_bundle"

    exit_code, message = runner.run_fragrantica_mgt_capture(
        url=_URL,
        output_root=output_root,
        http_runner=fake_http_runner,
        cloakbrowser_runner=fake_cloakbrowser_runner,
    )

    assert exit_code == 0
    summary_path = Path(message)
    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    assert summary["capture_profile"] == runner.CAPTURE_PROFILE
    assert summary["tier"] == "mini_god_tier"
    assert summary["source_family"] == runner.SOURCE_FAMILY
    assert summary["fragrantica_product_id"] == "33519"
    assert summary["packet_publication_mode"] == "local_output_bundle"
    assert summary["projection_status"] == "not_run; projection is a later lane over the raw packet evidence"
    assert summary["packet_roles"][runner.DIRECT_HTTP_SLOT]["packet_id"] == "01KW0000000000000000000001"
    assert summary["packet_roles"][runner.INITIAL_VIEWPORT_SLOT]["packet_id"] == "01KW0000000000000000000002"
    assert summary["packet_roles"][runner.DEEP_SCROLL_SLOT]["packet_id"] == "01KW0000000000000000000003"
    assert any("login-gated full review archive" in item for item in summary["accepted_residuals"])

    assert len(calls) == 3
    assert calls[0]["source_surface"] == runner.DIRECT_HTTP_SURFACE
    assert calls[0]["capture_mode"] == runner.CaptureModeCategory.STRUCTURED_ACCESS
    assert calls[0]["data_root"] is None
    assert calls[1]["source_surface"] == runner.INITIAL_VIEWPORT_SURFACE
    assert calls[1]["settle_seconds"] == runner.DEFAULT_INITIAL_SETTLE_SECONDS
    assert calls[1]["scroll_passes"] == 0
    assert calls[1]["scroll_step_px"] == 0
    assert calls[2]["source_surface"] == runner.DEEP_SCROLL_SURFACE
    assert calls[2]["settle_seconds"] == runner.DEFAULT_DEEP_SETTLE_SECONDS
    assert calls[2]["scroll_passes"] == runner.DEFAULT_DEEP_SCROLL_PASSES
    assert calls[2]["scroll_step_px"] == runner.DEFAULT_DEEP_SCROLL_STEP_PX
    assert calls[2]["block_heavy_assets"] is False


def test_preflight_does_not_create_output_root(tmp_path: Path, capsys) -> None:
    output_root = tmp_path / "preflight_bundle"

    exit_code = runner.main(
        [
            "--url",
            _URL,
            "--output-root",
            str(output_root),
            "--preflight-only",
        ]
    )

    captured = capsys.readouterr()
    assert exit_code == 0
    assert "no network capture attempted" in captured.out
    assert "product_id=33519" in captured.out
    assert not output_root.exists()


def test_nonempty_output_root_fails_before_capture(tmp_path: Path) -> None:
    output_root = tmp_path / "bundle"
    output_root.mkdir()
    (output_root / "existing.txt").write_text("do not overwrite", encoding="utf-8")

    with pytest.raises(ValueError, match="output root must be absent or empty"):
        runner.run_fragrantica_mgt_capture(
            url=_URL,
            output_root=output_root,
            http_runner=lambda **_kwargs: (0, "should-not-run"),
            cloakbrowser_runner=lambda **_kwargs: (0, "should-not-run"),
        )
