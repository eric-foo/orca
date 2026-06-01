from __future__ import annotations

import ast
from pathlib import Path


FORBIDDEN_IMPORT_ROOTS = {
    "aiohttp",
    "bs4",
    "httpx",
    "playwright",
    "requests",
    "scrapy",
    "selenium",
    "socket",
    "urllib",
}


def test_source_observability_helper_has_no_runtime_acquisition_imports() -> None:
    project_root = Path(__file__).resolve().parents[2]
    target_paths = sorted((project_root / "source_observability").glob("*.py")) + [
        project_root / "runners" / "run_source_observability_report.py"
    ]

    assert target_paths, "source_observability helper package must exist"

    for path in target_paths:
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported_roots = {alias.name.split(".")[0] for alias in node.names}
                assert not imported_roots & FORBIDDEN_IMPORT_ROOTS, f"Forbidden import in {path}"
            if isinstance(node, ast.ImportFrom) and node.module:
                imported_root = node.module.split(".")[0]
                assert imported_root not in FORBIDDEN_IMPORT_ROOTS, f"Forbidden import in {path}"
