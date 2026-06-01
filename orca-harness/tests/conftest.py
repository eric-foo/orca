from __future__ import annotations

import shutil
import sys
import uuid
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
CASE_ID = "tr_casetext_2023_v0_14"

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


def _copy_ignore(_directory: str, names: list[str]) -> set[str]:
    ignored: set[str] = set()
    for name in names:
        if name in {"_test_runs", ".pytest_cache", "pytest_tmp"}:
            ignored.add(name)
        if (
            name.startswith("pytest_run_")
            or name.startswith("pytest-cache-files-")
            or name.startswith("pytest_tmp")
            or (name.startswith("pytest_") and name.endswith("_tmp"))
        ):
            ignored.add(name)
    return ignored


def _reset_copied_outputs(project_root: Path) -> None:
    case_dir = project_root / "cases" / "plumbing" / CASE_ID
    scores_dir = case_dir / "scores"
    if scores_dir.exists():
        shutil.rmtree(scores_dir)

    report_dir = project_root / "reports" / "plumbing" / CASE_ID
    if report_dir.exists():
        shutil.rmtree(report_dir)

    failure_log = project_root / "memory" / "logs" / "failure_events.yaml"
    if failure_log.exists():
        failure_log.unlink()


@pytest.fixture
def copied_project() -> Path:
    scratch_root = PROJECT_ROOT / "_test_runs"
    scratch_root.mkdir(exist_ok=True)
    destination = scratch_root / f"run_{uuid.uuid4().hex}"
    shutil.copytree(PROJECT_ROOT, destination, ignore=_copy_ignore)
    _reset_copied_outputs(destination)
    try:
        yield destination
    finally:
        shutil.rmtree(destination)


@pytest.fixture
def copied_case_dir(copied_project: Path) -> Path:
    return copied_project / "cases" / "plumbing" / CASE_ID
