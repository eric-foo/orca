from __future__ import annotations

import ast
from datetime import UTC, datetime, timedelta
import json
from pathlib import Path

import pytest

from runners import run_source_capture_ig_calls_batch as batch
from source_capture.auth_state import AuthenticatedSessionMode


NOW = datetime(2026, 6, 21, 0, 0, tzinfo=UTC)


def _slot(slot_id: str, handle: str) -> batch.IgCallsBatchSlot:
    return batch.IgCallsBatchSlot(
        slot_id=slot_id,
        profile_url=f"https://www.instagram.com/{handle}/",
        handle=handle,
    )


def _write_manifest(packet_dir: Path, limitations: list[str] | None = None) -> None:
    packet_dir.mkdir(parents=True, exist_ok=True)
    (packet_dir / "manifest.json").write_text(
        f"{json.dumps({'limitations': limitations or []}, indent=2)}\n",
        encoding="utf-8",
        newline="\n",
    )


def _read_json(path: Path | str) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def test_load_slots_accepts_handles_and_profile_urls(tmp_path: Path) -> None:
    profile_list = tmp_path / "profiles.json"
    profile_list.write_text(
        json.dumps(
            [
                "@jeremyfragrance",
                {
                    "slot_id": "curly",
                    "profile_url": "https://www.instagram.com/curlyscents/",
                },
            ]
        ),
        encoding="utf-8",
    )

    slots = batch.load_slots(profile_list)

    assert slots == [
        batch.IgCallsBatchSlot(
            slot_id="slot_001",
            profile_url="https://www.instagram.com/jeremyfragrance/",
            handle="jeremyfragrance",
        ),
        batch.IgCallsBatchSlot(
            slot_id="curly",
            profile_url="https://www.instagram.com/curlyscents/",
            handle="curlyscents",
        ),
    ]


@pytest.mark.parametrize(
    "payload",
    [
        [{"slot_id": "post", "profile_url": "https://www.instagram.com/p/ABC/"}],
        [{"slot_id": "../escape", "handle": "hyram"}],
    ],
)
def test_load_slots_rejects_non_profile_targets_and_path_slots(tmp_path: Path, payload: list[dict]) -> None:
    profile_list = tmp_path / "profiles.json"
    profile_list.write_text(json.dumps(payload), encoding="utf-8")

    with pytest.raises(ValueError):
        batch.load_slots(profile_list)


def test_batch_runner_rejects_duplicate_direct_slot_ids(tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="duplicate slot_id"):
        batch.run_source_capture_ig_calls_batch(
            slots=[_slot("dup", "hyram"), _slot("dup", "curlyscents")],
            output_root=tmp_path / "out",
            decision_question="Which creator calls are visible?",
            cooldown_ledger_path=tmp_path / "cooldown.json",
            now_fn=lambda: NOW,
        )


def test_batch_runner_wraps_per_handle_runner_and_records_summary(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    calls: list[dict] = []
    sleeps: list[float] = []

    def fake_packet_runner(**kwargs):
        calls.append(kwargs)
        _write_manifest(kwargs["output_directory"])
        return 0, "packet-ok"

    monkeypatch.setattr(batch, "run_source_capture_ig_calls_packet", fake_packet_runner)

    exit_code, message = batch.run_source_capture_ig_calls_batch(
        slots=[_slot("hyram", "hyram"), _slot("curly", "curlyscents")],
        output_root=tmp_path / "out",
        decision_question="Which creator calls are visible?",
        inter_profile_delay_seconds=0,
        cadence_random_seed=700,
        auth_state_label="ig-free",
        auth_session_mode=AuthenticatedSessionMode.FREE_ACCOUNT_CREATED,
        cooldown_ledger_path=tmp_path / "cooldown.json",
        now_fn=lambda: NOW,
        sleep_fn=sleeps.append,
    )

    summary = _read_json(message)
    assert exit_code == 0
    assert [call["profile_url"] for call in calls] == [
        "https://www.instagram.com/hyram/",
        "https://www.instagram.com/curlyscents/",
    ]
    assert [call["cadence_random_seed"] for call in calls] == [700, 701]
    assert calls[0]["auth_state_label"] == "ig-free"
    assert calls[0]["auth_session_mode"] == AuthenticatedSessionMode.FREE_ACCOUNT_CREATED
    assert "batch_runner_no_discovery" in calls[0]["limitations"]
    assert sleeps == []
    assert summary["status"] == "completed"
    assert summary["attempted_count"] == 2
    assert summary["packet_success_count"] == 2
    assert summary["circuit_break_count"] == 0
    assert summary["auth_state_loaded"] is True
    assert summary["auth_state_path_recorded"] is False
    assert not (tmp_path / "cooldown.json").exists()


def test_batch_runner_stops_on_exit_code_circuit_break_and_writes_cooldown(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    calls: list[str] = []
    cooldown_ledger = tmp_path / "cooldown.json"

    def fake_packet_runner(**kwargs):
        calls.append(kwargs["profile_url"])
        return batch.IG_CIRCUIT_BREAK_EXIT_CODE, "redirected_to_login"

    monkeypatch.setattr(batch, "run_source_capture_ig_calls_packet", fake_packet_runner)

    exit_code, message = batch.run_source_capture_ig_calls_batch(
        slots=[_slot("hyram", "hyram"), _slot("curly", "curlyscents")],
        output_root=tmp_path / "out",
        decision_question="Which creator calls are visible?",
        inter_profile_delay_seconds=0,
        cooldown_ledger_path=cooldown_ledger,
        now_fn=lambda: NOW,
    )

    summary = _read_json(message)
    ledger = _read_json(cooldown_ledger)
    assert exit_code == batch.IG_CIRCUIT_BREAK_EXIT_CODE
    assert calls == ["https://www.instagram.com/hyram/"]
    assert summary["status"] == "stopped_circuit_break"
    assert summary["attempted_count"] == 1
    assert summary["results"][0]["circuit_break_detected"] is True
    assert ledger["trigger_handle"] == "hyram"
    assert ledger["trigger_reason"] == "redirected_to_login"
    assert ledger["cooldown_seconds"] == batch.DEFAULT_COOLDOWN_SECONDS


def test_batch_runner_stops_on_manifest_circuit_break_when_child_exits_zero(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    calls: list[str] = []
    cooldown_ledger = tmp_path / "cooldown.json"

    def fake_packet_runner(**kwargs):
        calls.append(kwargs["profile_url"])
        _write_manifest(
            kwargs["output_directory"],
            [
                "ig_circuit_break_recommended:web_profile_info_401; "
                "stop batch and cool down before next profile"
            ],
        )
        return 0, "packet-ok-with-limitation"

    monkeypatch.setattr(batch, "run_source_capture_ig_calls_packet", fake_packet_runner)

    exit_code, message = batch.run_source_capture_ig_calls_batch(
        slots=[_slot("hyram", "hyram"), _slot("curly", "curlyscents")],
        output_root=tmp_path / "out",
        decision_question="Which creator calls are visible?",
        inter_profile_delay_seconds=0,
        cooldown_ledger_path=cooldown_ledger,
        now_fn=lambda: NOW,
    )

    summary = _read_json(message)
    ledger = _read_json(cooldown_ledger)
    assert exit_code == batch.IG_CIRCUIT_BREAK_EXIT_CODE
    assert calls == ["https://www.instagram.com/hyram/"]
    assert summary["status"] == "stopped_circuit_break"
    assert summary["packet_success_count"] == 1
    assert summary["results"][0]["packet_written"] is True
    assert summary["results"][0]["circuit_break_reason"].startswith("ig_circuit_break_recommended")
    assert ledger["trigger_handle"] == "hyram"


def test_batch_runner_refuses_active_cooldown_unless_ignored(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    cooldown_ledger = tmp_path / "cooldown.json"
    cooldown_ledger.write_text(
        json.dumps(
            {
                "runner": "ig_calls_batch",
                "cooldown_until": (NOW + timedelta(minutes=30)).isoformat().replace("+00:00", "Z"),
            }
        ),
        encoding="utf-8",
    )
    calls: list[str] = []

    def fake_packet_runner(**kwargs):
        calls.append(kwargs["profile_url"])
        _write_manifest(kwargs["output_directory"])
        return 0, "packet-ok"

    monkeypatch.setattr(batch, "run_source_capture_ig_calls_packet", fake_packet_runner)

    exit_code, message = batch.run_source_capture_ig_calls_batch(
        slots=[_slot("hyram", "hyram")],
        output_root=tmp_path / "blocked",
        decision_question="Which creator calls are visible?",
        cooldown_ledger_path=cooldown_ledger,
        now_fn=lambda: NOW,
    )

    blocked_summary = _read_json(message)
    assert exit_code == batch.IG_CALLS_BATCH_EXIT_CODE_COOLDOWN_ACTIVE
    assert calls == []
    assert blocked_summary["status"] == "cooldown_active"
    assert blocked_summary["attempted_count"] == 0

    exit_code, message = batch.run_source_capture_ig_calls_batch(
        slots=[_slot("hyram", "hyram")],
        output_root=tmp_path / "ignored",
        decision_question="Which creator calls are visible?",
        cooldown_ledger_path=cooldown_ledger,
        ignore_cooldown=True,
        now_fn=lambda: NOW,
    )

    ignored_summary = _read_json(message)
    assert exit_code == 0
    assert calls == ["https://www.instagram.com/hyram/"]
    assert ignored_summary["status"] == "completed"


def test_batch_runner_has_no_hidden_network_browser_or_proxy_imports() -> None:
    runner_path = Path(__file__).resolve().parents[2] / "runners" / "run_source_capture_ig_calls_batch.py"
    tree = ast.parse(runner_path.read_text(encoding="utf-8"))
    imported_modules: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported_modules.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported_modules.add(node.module)

    forbidden = {
        "aiohttp",
        "archivebox",
        "cloakbrowser",
        "httpx",
        "patchright",
        "playwright",
        "praw",
        "requests",
        "scrapy",
        "selenium",
        "socket",
        "source_capture.proxy_profiles",
        "webbrowser",
    }
    bad_imports = sorted(
        module
        for module in imported_modules
        for forbidden_module in forbidden
        if module == forbidden_module or module.startswith(f"{forbidden_module}.")
    )
    assert bad_imports == []
