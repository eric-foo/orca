from __future__ import annotations

import importlib.util
from pathlib import Path
import sys

import pytest

REPO_ROOT = Path(__file__).resolve().parents[3]
VALIDATOR_PATH = REPO_ROOT / ".agents" / "hooks" / "check_commission_signal_board_output.py"
FIXTURE_DIR = REPO_ROOT / "orca-harness" / "tests" / "fixtures" / "commission_signal_board_outputs"


def _load_validator():
    spec = importlib.util.spec_from_file_location("check_commission_signal_board_output", VALIDATOR_PATH)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


validator = _load_validator()


@pytest.mark.parametrize(
    "fixture_name",
    [
        "valid_empty_backtest_output.txt",
        "valid_source_backed_backtest_output.txt",
    ],
)
def test_valid_commission_signal_board_outputs_pass(fixture_name: str) -> None:
    findings = validator.validate_text((FIXTURE_DIR / fixture_name).read_text(encoding="utf-8"))
    assert findings == []


@pytest.mark.parametrize(
    ("fixture_name", "expected_code"),
    [
        ("bad_uncertain_cutoff_in_handoff_output.txt", "handoff_row_cutoff_invalid"),
        ("bad_aeo_future_info_in_handoff_output.txt", "handoff_row_aeo_visibility"),
        ("bad_to_retrieve_in_handoff_output.txt", "handoff_row_not_source_backed"),
    ],
)
def test_invalid_commission_signal_board_outputs_fail(fixture_name: str, expected_code: str) -> None:
    findings = validator.validate_text((FIXTURE_DIR / fixture_name).read_text(encoding="utf-8"))
    assert findings
    assert expected_code in {finding.code for finding in findings}


def test_handoff_row_must_exist_in_signal_board_rows() -> None:
    text = (FIXTURE_DIR / "valid_source_backed_backtest_output.txt").read_text(encoding="utf-8")
    text = text.replace("    - SBR-001", "    - SBR-999", 1)

    findings = validator.validate_text(text)

    assert "handoff_row_unknown" in {finding.code for finding in findings}
