#!/usr/bin/env python3
"""Deletion-evidence check (Phase-2 deletion safety) -- REPORT MODE.

WHAT THIS DOES
  Reports any deletion of a GOVERNED artifact (one under `governed_roots` in the
  deletion-evidence register) that lacks a complete `executed` register record.
  The frozen rule: a governed-artifact deletion is central-adjudicated, two-phase,
  with no standing per-lane delete -- it carries a complete register record (the
  four evidence elements) and is executed only via a human-merged PR. This checker
  is the mechanical visibility for the report-mode phase.

  Report-mode (exit 0) now; the strict (exit 1) flip is Phase-3, per the
  frozen-predicate ratchet the other Orca gates use. Doctrine + register:
  docs/decisions/deletion_evidence_doctrine_v0.md /
  docs/decisions/deletion_evidence_register_v0.yaml.

HARD BOUNDARY
  Read-only. Fail-open ONLY for infrastructure gaps (no git, no PyYAML, missing
  register). A present register with a missing/incomplete record for a real
  deletion is a real finding (printed; exit 0 in report mode).

MODES
  check_deletion_evidence.py --report    report governed deletions lacking a record; exit 0
  check_deletion_evidence.py --check      alias for --report; exit 0
  check_deletion_evidence.py --selftest   pure-function cases; exit 0/1
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

REGISTER_REL = "docs/decisions/deletion_evidence_register_v0.yaml"
EVIDENCE_FIELDS = ("reverse_ref_check", "successor", "semantic_delta", "rollback")


def repo_root() -> Path:
    """Repo root, derived from this file's location (.agents/hooks/<this>)."""
    return Path(__file__).resolve().parents[2]


# ---------------------------------------------------------------------------
# Pure predicates (testable)
# ---------------------------------------------------------------------------

def record_is_complete(rec: object) -> bool:
    """True iff `rec` is a well-formed EXECUTED deletion record: phase `executed`,
    `targets` a non-empty list of path strings, and all four evidence fields
    present and non-empty."""
    if not isinstance(rec, dict) or rec.get("phase") != "executed":
        return False
    targets = rec.get("targets")
    if not isinstance(targets, list) or not targets:
        return False
    if not all(isinstance(t, str) and t.strip() for t in targets):
        return False
    ev = rec.get("evidence")
    if not isinstance(ev, dict):
        return False
    return all(isinstance(ev.get(f), str) and ev.get(f, "").strip() for f in EVIDENCE_FIELDS)


def covered_targets(register: object) -> set[str]:
    """Repo-relative paths covered by a complete `executed` record."""
    out: set[str] = set()
    if not isinstance(register, dict):
        return out
    for rec in register.get("deletions") or []:
        if record_is_complete(rec):
            out.update(t.strip() for t in rec["targets"])
    return out


def governed_roots(register: object) -> list[str]:
    """Declared governed roots (paths whose deletions require a record)."""
    roots = register.get("governed_roots") if isinstance(register, dict) else None
    return [r for r in (roots or []) if isinstance(r, str) and r.strip()]


def is_governed(path: str, roots: list[str]) -> bool:
    """True if `path` is at or under a governed root."""
    return any(path == r.rstrip("/") or path.startswith(r) for r in roots)


# ---------------------------------------------------------------------------
# Git deletion detection
# ---------------------------------------------------------------------------

def _git(root: Path, args: list[str]) -> list[str] | None:
    """Run a git command; return stripped non-empty stdout lines, or None on any
    git failure (an infra gap -> fail-open)."""
    try:
        out = subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True)
    except (FileNotFoundError, OSError):
        return None
    if out.returncode != 0:
        return None
    return [ln.strip() for ln in out.stdout.splitlines() if ln.strip()]


def deleted_paths(root: Path) -> list[str] | None:
    """Paths deleted in the diff against the base (origin/main, else HEAD~1).
    None on a git infra gap (fail-open); [] when there is no base / no deletion."""
    base = None
    for cand in ("origin/main", "HEAD~1"):
        if _git(root, ["rev-parse", "--verify", "--quiet", cand]) is not None:
            base = cand
            break
    if base is None:
        if _git(root, ["rev-parse", "--verify", "--quiet", "HEAD"]) is None:
            return None  # not a git repo / no HEAD -> infra gap
        return []        # a repo with no base to diff against -> nothing to report
    return _git(root, ["diff", "--diff-filter=D", "--name-only", "%s...HEAD" % base])


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------

def check_deletions(root: Path) -> tuple[list[str], str | None]:
    """Return (findings, skip_reason). Fail-open: a non-None skip_reason marks an
    infra gap and findings is []."""
    try:
        import yaml
    except Exception:
        return [], "PyYAML unavailable"
    reg_path = root / REGISTER_REL
    if not reg_path.is_file():
        return [], "register missing (%s)" % REGISTER_REL
    try:
        register = yaml.safe_load(reg_path.read_text(encoding="utf-8"))
    except Exception as exc:
        return ["register: cannot parse %s (%s)" % (REGISTER_REL, exc)], None
    roots = governed_roots(register)
    if not roots:
        return [], "no governed_roots declared in the register"
    deleted = deleted_paths(root)
    if deleted is None:
        return [], "git unavailable"
    covered = covered_targets(register)
    findings = [
        "governed artifact deleted without a complete `executed` register record: %s" % p
        for p in deleted
        if is_governed(p, roots) and p not in covered
    ]
    return findings, None


def run_report(root: Path) -> int:
    findings, skip = check_deletions(root)
    print("check_deletion_evidence --report (REPORT MODE, exit 0; strict flip is Phase-3):")
    if skip:
        print("  fail-open (infra gap): %s -- nothing to report" % skip)
        return 0
    if findings:
        print("  %d governed deletion(s) lacking a complete register record:" % len(findings))
        for f in findings:
            print("    " + f)
    else:
        print("  OK: no governed deletion lacks a register record (diff vs base)")
    return 0


# ---------------------------------------------------------------------------
# Selftest
# ---------------------------------------------------------------------------

def selftest() -> int:
    ok = True

    def check(label: str, got, exp):
        nonlocal ok
        status = "PASS" if got == exp else "FAIL"
        if got != exp:
            ok = False
        print("%s  %-46s got=%s" % (status, label, got))

    complete = {
        "phase": "executed",
        "targets": ["orca/product/x_v0.md"],
        "evidence": {f: "a non-empty narrative" for f in EVIDENCE_FIELDS},
    }
    check("complete executed record", record_is_complete(complete), True)
    check("phase proposed -> incomplete", record_is_complete({**complete, "phase": "proposed"}), False)
    check("missing evidence field", record_is_complete({**complete, "evidence": {"reverse_ref_check": "x"}}), False)
    check("empty targets", record_is_complete({**complete, "targets": []}), False)
    check("blank evidence value",
          record_is_complete({**complete, "evidence": {**complete["evidence"], "rollback": "  "}}), False)

    reg = {
        "governed_roots": ["orca/product/"],
        "deletions": [complete, {"phase": "proposed", "targets": ["orca/product/y.md"]}],
    }
    check("covered_targets (complete only)", covered_targets(reg), {"orca/product/x_v0.md"})
    check("governed_roots", governed_roots(reg), ["orca/product/"])
    check("is_governed inside root", is_governed("orca/product/a/b.md", ["orca/product/"]), True)
    check("is_governed outside root", is_governed("docs/decisions/z.md", ["orca/product/"]), False)

    print()
    print("SELFTEST", "OK" if ok else "FAILED")
    return 0 if ok else 1


def main(argv: list[str]) -> int:
    if "--selftest" in argv:
        return selftest()
    try:
        root = repo_root()
    except Exception as exc:
        sys.stderr.write("check_deletion_evidence: cannot determine repo root: %s\n" % exc)
        return 0
    if "--report" in argv or "--check" in argv:
        return run_report(root)
    print("Usage: check_deletion_evidence.py --report | --check | --selftest")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except Exception as exc:  # never hard-fail a report-mode advisory
        sys.stderr.write("check_deletion_evidence: internal error, allowing: %s\n" % exc)
        sys.exit(0)
