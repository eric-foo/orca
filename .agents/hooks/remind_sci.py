#!/usr/bin/env python3
"""Smallest-Complete-Intervention reminder hook (advisory, never blocks).

WHY THIS EXISTS
  The Smallest Complete Intervention (SCI) rule lives in AGENTS.md, near the top
  of a large instruction surface. Over a long session -- and especially while
  authoring durable artifacts, where scope creep is most tempting -- SCI can drift
  out of active context. This hook re-injects a short SCI pointer at the write
  boundary, right when an artifact is created or edited, so the rule stays
  top-of-mind at the moment it matters.

  The RULE is owned by AGENTS.md (-> "Smallest Complete Intervention"). This hook
  does NOT restate or change it; it carries a pointer. If the two ever disagree,
  AGENTS.md wins and this reminder is the stale party.

BOUNDARY
  Advisory only. Emits `additionalContext` and ALWAYS exits 0; it never blocks a
  write and makes no validation, readiness, or correctness claim. Forward-only and
  low-noise by design: it fires ONLY for writes under the durable artifact folders
  and stays silent for code, scratch, skill copies, and project config.

SCOPE (in: durable artifacts; out: code/scratch/config)
  In  : docs/{decisions,product,prompts,workflows,migration,hygiene,review-inputs,
        review-outputs}/, .agents/workflow-overlay/, orca/product/
  Out : anything containing _scratch; docs/_inbox/; .agents/skills/; .claude/;
        orca-harness/ (and any path not under an in-scope prefix, e.g. .agents/hooks/).

MODES
  remind_sci.py --hook       PostToolUse hook (reads stdin JSON); emit reminder; exit 0
  remind_sci.py --selftest   pure-function scope cases; exit 0/1
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

RULE_AUTHORITY = "AGENTS.md > Smallest Complete Intervention"

# Durable artifact folders whose creation/edit warrants the SCI nudge.
IN_SCOPE_PREFIXES = (
    "docs/decisions/",
    "docs/product/",
    "docs/prompts/",
    "docs/workflows/",
    "docs/migration/",
    "docs/hygiene/",
    "docs/review-inputs/",
    "docs/review-outputs/",
    ".agents/workflow-overlay/",
    "orca/product/",
)

# Subtrees excluded even under an in-scope prefix (scratch, skill copies, config, code).
EXCLUDED_PREFIXES = (
    "docs/_inbox/",
    ".agents/skills/",
    ".claude/",
    "orca-harness/",
)

REMINDER = (
    "SCI reminder (advisory, not blocking) -- a durable artifact was touched. Apply "
    "the Smallest Complete Intervention rule (%s): solve the actual request COMPLETELY "
    "with the NARROWEST sufficient scope. Every changed line must trace to the request "
    "or required validation. 'Complete' -> do not underfix just to shrink the diff; "
    "'Smallest' -> no unrelated cleanup, speculative abstractions, broad rewrites, or "
    "nice-to-have additions."
) % RULE_AUTHORITY


def repo_root() -> Path:
    """Repo root, derived from this file's location (.agents/hooks/<this>)."""
    return Path(__file__).resolve().parents[2]


def to_relposix(target: str, root: Path) -> str | None:
    """Repo-relative POSIX path for a target, or None if outside the repo."""
    p = Path(target)
    if p.is_absolute():
        try:
            return p.resolve().relative_to(root).as_posix()
        except (ValueError, OSError):
            return None
    s = Path(target).as_posix()
    return s[2:] if s.startswith("./") else s  # strip a literal leading "./"


def in_scope(relposix: str) -> bool:
    """True if this path is a durable artifact whose write warrants the SCI nudge.

    Pure function (testable). Exclusions win over inclusions; a path under no
    in-scope prefix is out of scope (so code under .agents/hooks/ stays silent).
    """
    if not relposix:
        return False
    if "_scratch" in relposix:
        return False
    if any(relposix.startswith(x) for x in EXCLUDED_PREFIXES):
        return False
    return any(relposix.startswith(x) for x in IN_SCOPE_PREFIXES)


def run_hook(root: Path) -> int:
    """PostToolUse hook: read the touched file from stdin JSON; if it is a durable
    artifact, emit the SCI reminder as additionalContext. Always exit 0."""
    try:
        data = json.loads(sys.stdin.read() or "{}")
        file_path = (data.get("tool_input") or {}).get("file_path")
    except (ValueError, AttributeError):
        return 0  # malformed payload -> stay silent, never block
    if not file_path:
        return 0
    rel = to_relposix(file_path, root)
    if rel is None or not in_scope(rel):
        return 0
    print(
        json.dumps(
            {
                "hookSpecificOutput": {
                    "hookEventName": "PostToolUse",
                    "additionalContext": "%s (touched: %s)" % (REMINDER, rel),
                }
            }
        )
    )
    return 0


def selftest() -> int:
    ok = True
    cases = [
        ("decision doc in scope", "docs/decisions/foo_v0.md", True),
        ("product artifact in scope", "orca/product/spines/x/y_v0.md", True),
        ("overlay in scope", ".agents/workflow-overlay/x.md", True),
        ("migration doc in scope", "docs/migration/plan_v0.md", True),
        ("harness code out of scope", "orca-harness/schemas/case_models.py", False),
        ("hook code out of scope", ".agents/hooks/remind_sci.py", False),
        ("scratch excluded", "docs/decisions/_scratch/tmp.md", False),
        ("inbox excluded", "docs/_inbox/note.md", False),
        ("project config excluded", ".claude/settings.json", False),
        ("repo-root file out of scope", "README.md", False),
        ("empty path", "", False),
    ]
    for label, rel, exp in cases:
        got = in_scope(rel)
        status = "PASS" if got == exp else "FAIL"
        if got != exp:
            ok = False
        print("%s  %-34s got=%s" % (status, label, got))
    print()
    print("SELFTEST", "OK" if ok else "FAILED")
    return 0 if ok else 1


def main(argv: list[str]) -> int:
    if "--selftest" in argv:
        return selftest()
    if "--hook" in argv:
        return run_hook(repo_root())
    print("Usage: remind_sci.py --hook | --selftest")
    return 0  # advisory tool: unknown args -> exit 0, never block


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except Exception as exc:  # never block a write on an internal error
        sys.stderr.write("remind_sci: internal error, allowing: %s\n" % exc)
        sys.exit(0)
