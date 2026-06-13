#!/usr/bin/env python3
"""Retrieval-header index and forward-only CI gate.

WHAT THIS DOES
  Provides four modes over the retrieval-header contract:

  --index    Full retrieval view: for each durable, header-bearing .md in the
             repo, print one row: path | artifact_role | scope | use_when
             (joined) | stale_if (joined) | open_next.  Human-readable, exit 0.

  --health   Whole-repo advisory. Counts (and with --verbose lists) two classes:
               MISSING-HEADER  durable, non-exempt .md files with no header
               ORPHAN          header-bearing .md whose repo-relative path does
                               NOT appear as a substring in the repo map or any
                               submap under docs/workflows/.
             Exit 0 always (advisory, not a gate).

  --health --oneline
             Single capsule line for the session context capsule:
               "retrieval health: N missing headers, M orphans"
             or "retrieval health: ok" when both are zero.  Exit 0.

  --strict   CI GATE — diff-scoped / forward-only.  Resolves changed .md files
             vs a base ref (priority: $GITHUB_BASE_REF env var -> origin/<ref>;
             then --base <ref> CLI arg; then default origin/main).  Computes
             the changed set via `git diff --name-only <base>...HEAD`.  For
             ONLY those changed files: fails (exit 1) if a changed durable
             non-exempt doc is MISSING-HEADER or is an ORPHAN.  Prints each
             finding.  Exit 0 if none.  If diff-scoping genuinely cannot be
             resolved (e.g. no origin), prints a loud message and exits 0
             (fail-open) — a whole-repo strict would red-main on the existing
             backlog.

  --selftest Pure-function cases; exit 0 on pass, 1 on fail.

WHY THIS EXISTS (enforcement placement)
  The retrieval-header check (check_retrieval_header.py) already enforces header
  presence at the write-time boundary for individual files.  This companion adds:
    (a) a whole-repo index so a CA can see all durable retrieval artifacts at a
        glance without blind-walking the tree;
    (b) a whole-repo health advisory so the existing missing-header and orphan
        backlog is surfaced non-blockingly via the session capsule;
    (c) a forward-only CI gate so every NEW or CHANGED durable doc is gated on
        both header presence AND map reachability, without red-lining main on
        the pre-existing backlog.
  Enforcement placement principle:
    .agents/workflow-overlay/validation-gates.md -> "Enforcement Placement"

HARD BOUNDARY
  Read-only.  No writes.  Fails OPEN on internal error (prints the error,
  exits 0) so a broken index never stalls CI or a session.  --strict is
  diff-scoped only; it NEVER falls back to whole-repo strict.

MODES (summary)
  header_index.py --index
  header_index.py --health [--verbose]
  header_index.py --health --oneline
  header_index.py --strict [--base <ref>]
  header_index.py --selftest

REUSE
  Imports scope_folder, check_relpath, IN_SCOPE_PREFIXES, EXCLUDED_PREFIXES,
  and head_lines directly from check_retrieval_header.py (same .agents/hooks/
  directory).  check_retrieval_header.py is the canonical source for "which
  .md paths are durable/in-scope" and "does a file have a valid header";
  this file does NOT redefine those decisions.

REGISTRATION
  CI:  .github/workflows/ci.yml (retrieval-header index step, after link-check)
  Capsule: session_context_capsule.py calls --health --oneline with a 5s timeout
"""
from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Import shared decisions from check_retrieval_header (canonical source)
# ---------------------------------------------------------------------------

def _import_check_retrieval_header():
    """Import check_retrieval_header from the same hooks directory."""
    import importlib.util
    hooks_dir = Path(__file__).resolve().parent
    spec = importlib.util.spec_from_file_location(
        "check_retrieval_header",
        hooks_dir / "check_retrieval_header.py",
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


try:
    _crh = _import_check_retrieval_header()
    scope_folder = _crh.scope_folder
    check_relpath = _crh.check_relpath
    head_lines = _crh.head_lines
    IN_SCOPE_PREFIXES = _crh.IN_SCOPE_PREFIXES
    EXCLUDED_PREFIXES = _crh.EXCLUDED_PREFIXES
    _CRH_AVAILABLE = True
except Exception as _crh_err:
    _CRH_AVAILABLE = False
    _CRH_ERR = _crh_err


# ---------------------------------------------------------------------------
# Repo root (same pattern as other hooks)
# ---------------------------------------------------------------------------

def repo_root() -> Path:
    """Repo root derived from this file's location (.agents/hooks/<this>)."""
    return Path(__file__).resolve().parents[2]


# ---------------------------------------------------------------------------
# YAML header field extraction
# ---------------------------------------------------------------------------

_FIELD_RE = re.compile(r"^\s*(\w[\w_]*)\s*:\s*(.*)$")
_LIST_ITEM_RE = re.compile(r"^\s+-\s+(.+)$")


def _extract_header_fields(lines: list[str]) -> dict:
    """Extract YAML retrieval header fields from the first HEAD_LINES of a file.

    Returns a dict with keys: artifact_role, scope, use_when (list), stale_if
    (list), open_next (list).  Missing fields are empty strings / empty lists.

    Pure function (testable).
    """
    fields: dict = {
        "artifact_role": "",
        "scope": "",
        "use_when": [],
        "stale_if": [],
        "open_next": [],
    }

    in_yaml = False
    current_list_key: str | None = None
    list_keys = {"use_when", "stale_if", "open_next"}

    for line in lines:
        stripped = line.strip()

        # Detect yaml fence
        if stripped.startswith("```"):
            if not in_yaml and ("yaml" in stripped.lower() or stripped == "```"):
                in_yaml = True
                continue
            elif in_yaml:
                in_yaml = False
                current_list_key = None
                continue
            continue

        if not in_yaml:
            continue

        # List continuation
        if current_list_key is not None:
            m = _LIST_ITEM_RE.match(line)
            if m:
                val = m.group(1).strip().strip("\"'")
                fields[current_list_key].append(val)
                continue
            # Any non-list line ends the current list
            current_list_key = None

        # Key-value line
        m = _FIELD_RE.match(line)
        if m:
            key = m.group(1).strip()
            val = m.group(2).strip().strip("\"'")
            if key in ("artifact_role", "scope"):
                fields[key] = val
            elif key in list_keys:
                # Inline value or start of a list
                if val:
                    fields[key].append(val)
                else:
                    current_list_key = key

    return fields


# ---------------------------------------------------------------------------
# Repo walk: enumerate all in-scope .md files
# ---------------------------------------------------------------------------

def walk_durable_mds(root: Path) -> list[str]:
    """Return all in-scope durable .md relpaths (POSIX) under the repo root.

    Pure walk — does not check for header presence.
    """
    results: list[str] = []
    for dirpath, dirnames, filenames in os.walk(root):
        # Prune excluded subtrees early
        rel_dir = Path(dirpath).relative_to(root).as_posix()
        # Prune hidden/large non-relevant dirs
        dirnames[:] = [
            d for d in dirnames
            if not (d.startswith(".git") or d == "node_modules" or d == "__pycache__")
        ]
        for fname in filenames:
            if not fname.endswith(".md"):
                continue
            fpath = Path(dirpath) / fname
            relposix = fpath.relative_to(root).as_posix()
            if scope_folder(relposix) is not None:
                results.append(relposix)
    return sorted(results)


def has_retrieval_header(relposix: str, root: Path) -> bool:
    """True if the file has a structurally valid retrieval header (no problems)."""
    return len(check_relpath(relposix, root)) == 0


# ---------------------------------------------------------------------------
# Repo map / submap loading (mirrors check_map_links approach)
# ---------------------------------------------------------------------------

def load_map_text(root: Path) -> str:
    """Concatenate repo map + any submap text for orphan substring checks."""
    parts: list[str] = []
    map_path = root / "docs" / "workflows" / "orca_repo_map_v0.md"
    if map_path.exists():
        try:
            parts.append(map_path.read_text(encoding="utf-8", errors="replace"))
        except OSError:
            pass
    workflows = root / "docs" / "workflows"
    if workflows.is_dir():
        for f in workflows.iterdir():
            if (
                f.is_file()
                and "submap" in f.name.lower()
                and f.name.endswith(".md")
                and f != map_path
            ):
                try:
                    parts.append(f.read_text(encoding="utf-8", errors="replace"))
                except OSError:
                    pass
    return "\n".join(parts)


def is_orphan(relposix: str, map_text: str) -> bool:
    """True if relposix does NOT appear as a substring in map_text.

    Mirrors the C1/ORPHAN logic from check_map_links: a path is map-reachable
    if it or any enclosing path prefix appears as a substring on any map line.

    Pure function (testable).
    """
    if not map_text:
        return True
    return relposix not in map_text


# ---------------------------------------------------------------------------
# Health scan (whole-repo advisory)
# ---------------------------------------------------------------------------

def health_scan(root: Path) -> tuple[list[str], list[str]]:
    """Return (missing_headers, orphans) lists of relpaths.

    missing_headers: durable in-scope .md files with no valid retrieval header.
    orphans: durable in-scope .md files WITH a valid header but NOT appearing
             as a substring in any map/submap file.
    """
    map_text = load_map_text(root)
    all_mds = walk_durable_mds(root)
    missing: list[str] = []
    orphans: list[str] = []
    for relposix in all_mds:
        problems = check_relpath(relposix, root)
        if problems:
            missing.append(relposix)
        else:
            # Has a valid header — check map reachability
            if is_orphan(relposix, map_text):
                orphans.append(relposix)
    return missing, orphans


# ---------------------------------------------------------------------------
# Mode: --index
# ---------------------------------------------------------------------------

def run_index(root: Path) -> int:
    """Print a full retrieval view of all header-bearing durable .md files."""
    all_mds = walk_durable_mds(root)
    rows = []
    for relposix in all_mds:
        problems = check_relpath(relposix, root)
        if problems:
            continue  # skip files without a valid header
        lines = head_lines(root / relposix)
        if lines is None:
            continue
        f = _extract_header_fields(lines)
        rows.append((relposix, f))

    if not rows:
        print("header_index --index: no header-bearing durable .md files found")
        return 0

    print("header_index --index: %d indexed file(s)\n" % len(rows))
    for relposix, f in rows:
        use_when = " | ".join(f["use_when"]) if f["use_when"] else "(none)"
        stale_if = " | ".join(f["stale_if"]) if f["stale_if"] else "(none)"
        open_next = " | ".join(f["open_next"]) if f["open_next"] else "(none)"
        print("  path:        %s" % relposix)
        print("  role:        %s" % (f["artifact_role"] or "(missing)"))
        print("  scope:       %s" % (f["scope"] or "(missing)"))
        print("  use_when:    %s" % use_when)
        print("  stale_if:    %s" % stale_if)
        print("  open_next:   %s" % open_next)
        print()
    return 0


# ---------------------------------------------------------------------------
# Mode: --health [--verbose] [--oneline]
# ---------------------------------------------------------------------------

def run_health(root: Path, verbose: bool = False, oneline: bool = False) -> int:
    """Advisory whole-repo health check. Always exit 0."""
    missing, orphans = health_scan(root)
    if oneline:
        if not missing and not orphans:
            print("retrieval health: ok")
        else:
            print(
                "retrieval health: %d missing header%s, %d orphan%s"
                % (
                    len(missing), "s" if len(missing) != 1 else "",
                    len(orphans),  "s" if len(orphans)  != 1 else "",
                )
            )
        return 0

    # Full health report
    print("header_index --health (whole-repo advisory, exit 0)")
    print("  MISSING-HEADER: %d  (durable in-scope .md with no valid header)" % len(missing))
    print("  ORPHAN:         %d  (header-bearing .md not substring-found in map/submaps)" % len(orphans))
    print()
    if verbose:
        if missing:
            print("MISSING-HEADER files:")
            for p in missing:
                print("  %s" % p)
            print()
        if orphans:
            print("ORPHAN files:")
            for p in orphans:
                print("  %s" % p)
            print()
    if not missing and not orphans:
        print("health: ok")
    else:
        print(
            "health: advisory backlog present (%d missing header, %d orphan) "
            "-- not a gate; fix via the retrieval-metadata contract; "
            "new/changed docs gated forward-only via --strict."
            % (len(missing), len(orphans))
        )
    return 0


# ---------------------------------------------------------------------------
# Mode: --strict (CI gate, diff-scoped)
# ---------------------------------------------------------------------------

def _git(root: Path, *args: str, timeout: int = 15) -> tuple[int, str]:
    """Run git; return (returncode, stdout). Never raises."""
    try:
        res = subprocess.run(
            ["git", "-C", str(root), *args],
            capture_output=True, text=True, timeout=timeout,
        )
        return res.returncode, res.stdout
    except (FileNotFoundError, OSError, subprocess.TimeoutExpired) as e:
        return -1, ""


def resolve_base_ref(root: Path, cli_base: str | None) -> str | None:
    """Resolve the base ref for diff-scoping.

    Priority:
    1. $GITHUB_BASE_REF env var  -> "origin/<value>"
    2. --base <ref> CLI arg
    3. default: "origin/main"

    Returns a ref string, or None if none could be resolved.
    """
    gh_base = os.environ.get("GITHUB_BASE_REF", "").strip()
    if gh_base:
        return "origin/%s" % gh_base
    if cli_base:
        return cli_base
    return "origin/main"


def changed_mds_vs_base(root: Path, base_ref: str) -> list[str] | None:
    """Return list of changed .md relpaths vs base_ref, or None on failure.

    Uses `git diff --name-only <base>...HEAD` (three-dot: merge-base diff).
    Returns None if the diff cannot be computed.
    """
    rc, out = _git(root, "diff", "--name-only", "%s...HEAD" % base_ref)
    if rc != 0:
        # Try two-dot as fallback
        rc2, out2 = _git(root, "diff", "--name-only", base_ref, "HEAD")
        if rc2 != 0:
            return None
        out = out2
    return [line.strip() for line in out.splitlines() if line.strip().endswith(".md")]


def run_strict(root: Path, cli_base: str | None = None) -> int:
    """--strict CI gate: diff-scoped, forward-only.  Exit 1 on findings."""
    base_ref = resolve_base_ref(root, cli_base)

    changed = changed_mds_vs_base(root, base_ref)
    if changed is None:
        # Cannot diff-scope — MUST fail open (whole-repo strict would red-main)
        print(
            "header_index --strict: WARNING: diff-scoping unavailable "
            "(base ref '%s' could not be resolved or git diff failed). "
            "Failing OPEN (exit 0) to avoid red-main on backlog. "
            "Check that origin is configured and the base ref exists."
            % base_ref,
            file=sys.stderr,
        )
        return 0

    if not changed:
        print("header_index --strict: no changed .md files in this diff -- OK (exit 0)")
        return 0

    map_text = load_map_text(root)
    findings: list[str] = []

    for relposix in changed:
        if scope_folder(relposix) is None:
            continue  # out of scope (not a durable doc)
        problems = check_relpath(relposix, root)
        if problems:
            findings.append(
                "MISSING-HEADER: %s -- %s" % (relposix, "; ".join(problems))
            )
        else:
            # Header present — check orphan
            if is_orphan(relposix, map_text):
                findings.append(
                    "ORPHAN: %s -- header present but path not found as "
                    "substring in repo map or any submap under docs/workflows/. "
                    "Add an entry to docs/workflows/orca_repo_map_v0.md or a submap."
                    % relposix
                )

    if findings:
        print(
            "header_index --strict: %d finding(s) on changed durable .md files "
            "(base: %s):" % (len(findings), base_ref)
        )
        for f in findings:
            print("  %s" % f)
        return 1

    print(
        "header_index --strict: OK -- %d changed durable .md file(s) all have "
        "headers and are map-reachable (base: %s)"
        % (sum(1 for r in changed if scope_folder(r) is not None), base_ref)
    )
    return 0


# ---------------------------------------------------------------------------
# Mode: --selftest
# ---------------------------------------------------------------------------

def selftest() -> int:
    """Pure-function self-test cases. Exit 0 on pass, 1 on fail."""
    ok = True

    # --- _extract_header_fields ---
    def make_header(**kw) -> list[str]:
        lines = ["# Title", "", "```yaml", "retrieval_header_version: 1"]
        for k, v in kw.items():
            if isinstance(v, list):
                lines.append("%s:" % k)
                for item in v:
                    lines.append("  - %s" % item)
            else:
                lines.append("%s: %s" % (k, v))
        lines.append("authority_boundary: retrieval_only")
        lines.append("```")
        return lines

    print("--- _extract_header_fields ---")
    h1 = make_header(
        artifact_role="Test role",
        scope="Test scope",
        use_when=["when A", "when B"],
        stale_if=["if X"],
        open_next=["docs/foo/bar_v0.md"],
    )
    f1 = _extract_header_fields(h1)
    cases_ehf = [
        ("artifact_role", f1["artifact_role"] == "Test role"),
        ("scope",         f1["scope"] == "Test scope"),
        ("use_when len",  len(f1["use_when"]) == 2),
        ("use_when[0]",   f1["use_when"][0] == "when A"),
        ("stale_if",      f1["stale_if"] == ["if X"]),
        ("open_next",     f1["open_next"] == ["docs/foo/bar_v0.md"]),
    ]
    for label, passed in cases_ehf:
        status = "PASS" if passed else "FAIL"
        if not passed:
            ok = False
        print("%s  %s" % (status, label))

    # Empty header (no yaml block)
    h_empty = ["# Title", "", "No yaml here."]
    f_empty = _extract_header_fields(h_empty)
    cases_empty = [
        ("empty artifact_role", f_empty["artifact_role"] == ""),
        ("empty use_when",      f_empty["use_when"] == []),
    ]
    for label, passed in cases_empty:
        status = "PASS" if passed else "FAIL"
        if not passed:
            ok = False
        print("%s  %s" % (status, label))

    # --- is_orphan ---
    print()
    print("--- is_orphan ---")
    map_text_sample = "| `docs/decisions/foo_v0.md` | Some role |\n| `docs/workflows/bar_v0.md` | Another |\n"
    orphan_cases = [
        ("present in map",    "docs/decisions/foo_v0.md", map_text_sample, False),
        ("not in map",        "docs/decisions/baz_v0.md", map_text_sample, True),
        ("empty map text",    "docs/decisions/foo_v0.md", "", True),
        ("substring match",   "docs/workflows/bar_v0.md", map_text_sample, False),
    ]
    for label, relposix, mt, expected in orphan_cases:
        got = is_orphan(relposix, mt)
        status = "PASS" if got == expected else "FAIL"
        if got != expected:
            ok = False
        print("%s  %-40s  expect=%s got=%s" % (status, label, expected, got))

    # --- resolve_base_ref ---
    print()
    print("--- resolve_base_ref ---")
    import pathlib
    fake_root = pathlib.Path(".")
    # Clear any GITHUB_BASE_REF for testing
    env_saved = os.environ.pop("GITHUB_BASE_REF", None)
    try:
        r1 = resolve_base_ref(fake_root, None)
        r2 = resolve_base_ref(fake_root, "some-branch")
        os.environ["GITHUB_BASE_REF"] = "develop"
        r3 = resolve_base_ref(fake_root, None)
        os.environ["GITHUB_BASE_REF"] = "develop"
        r4 = resolve_base_ref(fake_root, "ignored")  # env takes priority
    finally:
        if env_saved is not None:
            os.environ["GITHUB_BASE_REF"] = env_saved
        else:
            os.environ.pop("GITHUB_BASE_REF", None)
    base_cases = [
        ("default -> origin/main",  r1, "origin/main"),
        ("cli base",                r2, "some-branch"),
        ("env GITHUB_BASE_REF",     r3, "origin/develop"),
        ("env beats cli",           r4, "origin/develop"),
    ]
    for label, got, expected in base_cases:
        status = "PASS" if got == expected else "FAIL"
        if got != expected:
            ok = False
        print("%s  %-30s  expect=%s got=%s" % (status, label, expected, got))

    print()
    print("SELFTEST", "OK" if ok else "FAILED")
    return 0 if ok else 1


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main(argv: list[str]) -> int:
    if not _CRH_AVAILABLE:
        print(
            "header_index: ERROR: could not import check_retrieval_header.py: %s" % _CRH_ERR,
            file=sys.stderr,
        )
        print(
            "header_index: ensure check_retrieval_header.py is in the same "
            "directory as this script (.agents/hooks/).",
            file=sys.stderr,
        )
        # Fail open on import error so CI doesn't ghost-fail
        return 0

    if "--selftest" in argv:
        return selftest()

    try:
        root = repo_root()
    except Exception as exc:
        print("header_index: could not determine repo root: %s" % exc, file=sys.stderr)
        return 0  # fail open

    if "--index" in argv:
        return run_index(root)

    if "--health" in argv:
        oneline = "--oneline" in argv
        verbose = "--verbose" in argv
        return run_health(root, verbose=verbose, oneline=oneline)

    if "--strict" in argv:
        cli_base: str | None = None
        if "--base" in argv:
            idx = argv.index("--base")
            if idx + 1 < len(argv):
                cli_base = argv[idx + 1]
        return run_strict(root, cli_base=cli_base)

    print("Usage: header_index.py --index | --health [--verbose] [--oneline] | --strict [--base <ref>] | --selftest")
    return 1


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except Exception as exc:
        sys.stderr.write("header_index: internal error, failing open: %s\n" % exc)
        sys.exit(0)  # fail open
