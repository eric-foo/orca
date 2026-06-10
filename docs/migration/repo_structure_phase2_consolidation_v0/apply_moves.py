#!/usr/bin/env python3
"""Phase-2 consolidation: docs/product flat files -> bound lane subfolders.

Manifest-driven, reversible, dry-run-first. Owned by
docs/decisions/orca_repo_structure_binding_v0.md (binding) and
docs/migration/repo_structure_phase2_consolidation_v0/runbook.md (procedure).

DESIGN INVARIANTS
  - The manifest (moves_manifest.csv) is the single source for apply/reverse.
  - Moved files' CONTENT is never edited by --apply: content-hash pins held by
    other lanes' records survive the move. Path pins are covered by the
    moved-paths index this script writes.
  - Path references are rewritten ONLY in LIVE navigation/authority surfaces
    (see LIVE_REWRITE_SURFACES). Historical records (decisions, reviews,
    receipts, prompts, research) are never rewritten; the index covers them.
  - Intra-product references (inside the moved files themselves) are NOT
    rewritten by default; --rewrite-product-internal enables it and prints a
    hash-pin warning. Default off.
  - --apply refuses to run on a dirty tree unless --waive-dirty-tree is given
    (runbook precondition: clean commit checkpoint or explicit owner waiver).

MODES
  apply_moves.py --generate     scan flat docs/product/*.md, write the manifest
  apply_moves.py --scan-refs    write reference_inventory.md (live vs historical)
  apply_moves.py --dry-run      validate manifest against the tree, print plan (default)
  apply_moves.py --apply        execute moves + live rewrites + index + map update
  apply_moves.py --reverse      undo the moves recorded in the manifest

Not validation, readiness, or authority. After --apply, run
  python .agents/hooks/check_placement.py --strict
and follow the runbook's post-apply checklist.
"""
from __future__ import annotations

import argparse
import csv
import re
import subprocess
import sys
from pathlib import Path

PKG = Path(__file__).resolve().parent
ROOT = PKG.parents[2]
PRODUCT = "docs/product"
MANIFEST = PKG / "moves_manifest.csv"
INVENTORY = PKG / "reference_inventory.md"
INDEX = PKG / "moved_paths_index.md"
MAP_FILE = ROOT / "repo-structure.yaml"

# Lane assignment, ordered: first match wins (most-specific token first).
LANE_RULES = (
    ("data_capture_spine", lambda n: "data_capture" in n or n.startswith("source_capture_packet")),
    ("judgment_spine", lambda n: "judgment_spine" in n or n.startswith("jsg01") or n.startswith("judgment_quality")),
    ("signal_content", lambda n: "signal_content" in n),
    ("ecr", lambda n: n.startswith("ecr_")),
    ("product_lead", lambda n: n.startswith("orca_") and re.search(
        r"product_lead|discovery|offer|buyer|icp|pricing|product_proof", n) is not None),
    ("core_spine", lambda n: n.startswith("core_spine") or n.startswith("orca_backtest_specimen")
        or n.startswith("orca_memorization")),
)

# LIVE surfaces: navigation + authority + reusable templates. Rewritten on apply.
LIVE_REWRITE_SURFACES = (
    ".agents/workflow-overlay/",
    ".agents/hooks/",
    "docs/README.md",
    "docs/STRUCTURE.md",
    "docs/workflows/orca_repo_map_v0.md",
    "docs/workflows/data_capture_spine_consolidation_map_v0.md",
    "docs/research/judgment-spine/judgment_spine_consolidation_map_v0.md",
    "docs/product/README.md",
    "docs/prompts/templates/",
    "repo-structure.yaml",
)
# Never scanned at all.
SCAN_EXCLUDE = (".git/", ".codex/", "docs/_inbox/", "docs/migration/repo_structure_phase2_consolidation_v0/")
TEXT_SUFFIXES = {".md", ".yaml", ".yml", ".py", ".json", ".txt", ".toml"}


def assign_lane(name: str) -> str | None:
    for lane, rule in LANE_RULES:
        if rule(name):
            return lane
    return None


def git(args: list[str]) -> tuple[int, str]:
    res = subprocess.run(["git", "-C", str(ROOT)] + args, capture_output=True, text=True)
    return res.returncode, (res.stdout or "") + (res.stderr or "")


def tracked_status(rel: str) -> str:
    code, out = git(["ls-files", "--error-unmatch", rel])
    return "tracked" if code == 0 else "untracked"


def generate() -> int:
    src = ROOT / PRODUCT
    rows, unassigned = [], []
    for p in sorted(src.glob("*.md")):
        if p.name == "README.md":
            continue
        lane = assign_lane(p.name)
        rel = f"{PRODUCT}/{p.name}"
        if lane is None:
            unassigned.append(rel)
            continue
        rows.append({"old_path": rel, "new_path": f"{PRODUCT}/{lane}/{p.name}",
                     "lane": lane, "tracked": tracked_status(rel)})
    with MANIFEST.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["old_path", "new_path", "lane", "tracked"])
        w.writeheader()
        w.writerows(rows)
    by_lane: dict[str, int] = {}
    for r in rows:
        by_lane[r["lane"]] = by_lane.get(r["lane"], 0) + 1
    print(f"manifest written: {MANIFEST.relative_to(ROOT).as_posix()} ({len(rows)} moves)")
    for lane, n in sorted(by_lane.items()):
        print(f"  {lane:22s} {n}")
    print(f"  {'(stays flat)':22s} {len(unassigned)}  {', '.join(Path(u).name for u in unassigned) or ''}")
    return 0


def load_manifest() -> list[dict]:
    with MANIFEST.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def iter_scan_files():
    for p in ROOT.rglob("*"):
        if not p.is_file() or p.suffix.lower() not in TEXT_SUFFIXES:
            continue
        rel = p.relative_to(ROOT).as_posix()
        if any(rel.startswith(x) for x in SCAN_EXCLUDE):
            continue
        yield rel, p


def is_live(rel: str) -> bool:
    return any(rel == s or rel.startswith(s) for s in LIVE_REWRITE_SURFACES)


def scan_refs(rows: list[dict]) -> dict:
    """Return {referencing_rel: {"class": live|historical|moved_set, "hits": n}}."""
    old_paths = [r["old_path"] for r in rows]
    moved_set = set(old_paths)
    pat = re.compile("|".join(re.escape(o) for o in old_paths))
    out: dict[str, dict] = {}
    for rel, p in iter_scan_files():
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        hits = len(pat.findall(text))
        if not hits:
            continue
        cls = "moved_set" if rel in moved_set else ("live" if is_live(rel) else "historical")
        out[rel] = {"class": cls, "hits": hits}
    return out


def write_inventory(refs: dict) -> None:
    lines = [
        "# Phase-2 Reference Inventory (generated)",
        "",
        "Classes: `live` = rewritten by --apply; `historical` = never rewritten,",
        "covered by moved_paths_index.md; `moved_set` = references inside the moved",
        "files themselves - rewritten only under --rewrite-product-internal",
        "(default OFF; content edits change file hashes - check hash pins first).",
        "",
        "| Referencing file | Class | Old-path hits |",
        "| --- | --- | --- |",
    ]
    for rel in sorted(refs, key=lambda r: (refs[r]["class"], r)):
        lines.append(f"| `{rel}` | {refs[rel]['class']} | {refs[rel]['hits']} |")
    by_cls: dict[str, int] = {}
    for v in refs.values():
        by_cls[v["class"]] = by_cls.get(v["class"], 0) + 1
    lines += ["", f"Totals: {by_cls}"]
    INVENTORY.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"inventory written: {INVENTORY.relative_to(ROOT).as_posix()}  {by_cls}")


def dirty_tree_lines() -> list[str]:
    code, out = git(["status", "--porcelain"])
    if code != 0:
        return ["<git status failed>"]
    return [l for l in out.splitlines() if l.strip()]


def dry_run(rows: list[dict]) -> int:
    problems = []
    targets = set()
    for r in rows:
        if not (ROOT / r["old_path"]).is_file():
            problems.append(f"source missing: {r['old_path']}")
        if (ROOT / r["new_path"]).exists():
            problems.append(f"target already exists: {r['new_path']}")
        if r["new_path"] in targets:
            problems.append(f"target collision: {r['new_path']}")
        targets.add(r["new_path"])
    refs = scan_refs(rows)
    write_inventory(refs)
    by_lane: dict[str, int] = {}
    for r in rows:
        by_lane[r["lane"]] = by_lane.get(r["lane"], 0) + 1
    print(f"\nDRY RUN: {len(rows)} moves -> {len(by_lane)} lanes {by_lane}")
    print(f"tracked: {sum(1 for r in rows if r['tracked'] == 'tracked')}, "
          f"untracked: {sum(1 for r in rows if r['tracked'] == 'untracked')}")
    live = [r for r, v in refs.items() if v["class"] == "live"]
    print(f"live surfaces to rewrite: {len(live)}")
    for rel in sorted(live):
        print(f"  rewrite: {rel} ({refs[rel]['hits']} hit(s))")
    print(f"historical referencing files (indexed, not rewritten): "
          f"{sum(1 for v in refs.values() if v['class'] == 'historical')}")
    print(f"moved-set internal referencing files (flag-gated): "
          f"{sum(1 for v in refs.values() if v['class'] == 'moved_set')}")
    dirty = dirty_tree_lines()
    print(f"worktree dirty lines: {len(dirty)} (apply requires clean tree or --waive-dirty-tree)")
    if problems:
        print("\nPROBLEMS:")
        for x in problems:
            print(f"  {x}")
        return 1
    print("dry run OK: manifest is applicable")
    return 0


def rewrite_text(text: str, mapping: dict) -> tuple[str, int]:
    n = 0
    for old, new in mapping.items():
        if old in text:
            n += text.count(old)
            text = text.replace(old, new)
    return text, n


def update_map_after_apply() -> bool:
    """Drop the flat-product tolerance; flip planned lanes to current."""
    try:
        text = MAP_FILE.read_text(encoding="utf-8")
    except OSError:
        return False
    ok = False
    lines = []
    for line in text.splitlines(keepends=True):
        if line.strip().startswith('- "docs/product/*.md"'):
            ok = True
            continue  # tolerance retired by this apply
        lines.append(line.replace("status: planned", "status: current")
                     if "status: planned" in line else line)
    if ok:
        MAP_FILE.write_text("".join(lines), encoding="utf-8")
    return ok


def apply(rows: list[dict], waive_dirty: bool, rewrite_internal: bool) -> int:
    dirty = dirty_tree_lines()
    if dirty and not waive_dirty:
        print(f"REFUSED: worktree has {len(dirty)} dirty line(s); commit a checkpoint first "
              "or pass --waive-dirty-tree (runbook precondition).")
        return 1
    if dry_run(rows) != 0:
        print("REFUSED: dry run found problems.")
        return 1
    mapping = {r["old_path"]: r["new_path"] for r in rows}
    # 1) moves (content untouched)
    for r in rows:
        src, dst = ROOT / r["old_path"], ROOT / r["new_path"]
        dst.parent.mkdir(parents=True, exist_ok=True)
        if r["tracked"] == "tracked":
            code, out = git(["mv", r["old_path"], r["new_path"]])
            if code != 0:
                print(f"ABORT at {r['old_path']}: git mv failed: {out.strip()}")
                return 1
        else:
            src.rename(dst)
    print(f"moved {len(rows)} file(s)")
    # 2) live-surface rewrites
    rewritten = 0
    for rel, p in iter_scan_files():
        if not is_live(rel):
            continue
        try:
            text = p.read_text(encoding="utf-8")
        except OSError:
            continue
        new_text, n = rewrite_text(text, mapping)
        if n:
            p.write_text(new_text, encoding="utf-8")
            rewritten += n
            print(f"  rewrote {n:3d} ref(s): {rel}")
    print(f"live references rewritten: {rewritten}")
    # 3) optional internal pass
    if rewrite_internal:
        print("WARNING: rewriting INSIDE moved files changes their content hashes; "
              "verify no hash pin covers them before relying on pinned records.")
        n_int = 0
        for r in rows:
            p = ROOT / r["new_path"]
            try:
                text = p.read_text(encoding="utf-8")
            except OSError:
                continue
            new_text, n = rewrite_text(text, mapping)
            if n:
                p.write_text(new_text, encoding="utf-8")
                n_int += n
        print(f"moved-set internal references rewritten: {n_int}")
    # 4) moved-paths index
    lines = ["# Moved Paths Index - Phase-2 product consolidation (generated)",
             "",
             "Historical records reference old paths by design; resolve them here.",
             "", "| Old path | New path |", "| --- | --- |"]
    lines += [f"| `{r['old_path']}` | `{r['new_path']}` |" for r in rows]
    INDEX.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"index written: {INDEX.relative_to(ROOT).as_posix()}")
    # 5) machine map update
    print("map tolerance retired + lanes flipped to current"
          if update_map_after_apply() else
          "WARNING: map tolerance line not found - update repo-structure.yaml by hand")
    print("\nNEXT (runbook): check_placement --strict; repo-map freshness --changed; "
          "review diff; commit per shared-file discipline.")
    return 0


def reverse(rows: list[dict]) -> int:
    n = 0
    for r in rows:
        src, dst = ROOT / r["new_path"], ROOT / r["old_path"]
        if not src.is_file():
            continue
        if r["tracked"] == "tracked":
            code, out = git(["mv", r["new_path"], r["old_path"]])
            if code != 0:
                print(f"reverse failed at {r['new_path']}: {out.strip()}")
                return 1
        else:
            dst.parent.mkdir(parents=True, exist_ok=True)
            src.rename(dst)
        n += 1
    print(f"reversed {n} move(s). NOTE: live-surface rewrites and the map update are "
          "content edits - revert those via git (they are not reversed here).")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--generate", action="store_true")
    g.add_argument("--scan-refs", action="store_true")
    g.add_argument("--dry-run", action="store_true")
    g.add_argument("--apply", action="store_true")
    g.add_argument("--reverse", action="store_true")
    ap.add_argument("--waive-dirty-tree", action="store_true")
    ap.add_argument("--rewrite-product-internal", action="store_true")
    a = ap.parse_args()
    if a.generate:
        return generate()
    rows = load_manifest()
    if a.scan_refs:
        write_inventory(scan_refs(rows))
        return 0
    if a.apply:
        return apply(rows, a.waive_dirty_tree, a.rewrite_product_internal)
    if a.reverse:
        return reverse(rows)
    return dry_run(rows)


if __name__ == "__main__":
    sys.exit(main())
