"""Data Lake physical root: resolver, per-root identity marker, directory
skeleton, and the deterministic write-boundary guard.

Implements the foundation slice of the adopted decision contracts:

- physicality location: one operator-configured external data root
  (``ORCA_DATA_ROOT``) that resolves OUTSIDE the repo working tree; fail-closed.
- write-boundary enforcement: a single deterministic writer; write-once raw;
  append-only derived/ack; per-root UUID marker; atomic create-only writes.
- raw admission + key grammar: ``packet_id`` is an opaque Crockford-26 handle;
  raw container is ``raw/<packet_id>/`` at packet depth.
- derived layout: ``derived/<raw-anchor>/<lane>/<record-id>`` and the split
  ``indexes/availability`` (content-free) vs ``indexes/derived_retrieval``
  (rebuildable, non-authoritative; created empty, population build-deferred).

This module is filesystem-incumbent and selects no storage engine,
serialization, or queue.
"""
from __future__ import annotations

import json
import os
import re
from pathlib import Path

from harness_utils import generate_ulid, utc_now_z

ROOT_MARKER_FILENAME = ".orca-data-root"
ROOT_MARKER_CONTRACT_VERSION = "v0"

# v0 logical directory grammar. ``indexes/`` is split into a content-free
# availability subslot and a rebuildable, non-authoritative derived_retrieval
# subslot (created empty here; population is governance-gated/build-deferred).
LAKE_SUBDIRECTORIES: tuple[str, ...] = (
    "raw",
    "attachments",
    "derived",
    "acknowledgements",
    "indexes/availability",
    "indexes/derived_retrieval",
)

# packet_id grammar: incumbent Crockford base32, 26 chars (harness generate_ulid).
_CROCKFORD_26 = re.compile(r"^[0123456789ABCDEFGHJKMNPQRSTVWXYZ]{26}$")
# Conservative, collision-safe, traversal-proof path segments for raw anchors,
# lane namespaces, and record ids.
_SAFE_SEGMENT = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,127}$")

_APPENDABLE_SUBTREES = ("derived", "acknowledgements")


class DataLakeRootError(Exception):
    """Fail-closed error. Raised instead of writing to an unsafe or unverified
    location; the caller must surface it, never silently fall back."""


def _detect_repo_root(start: Path) -> Path | None:
    start = start.resolve()
    for candidate in (start, *start.parents):
        if (candidate / ".git").exists():
            return candidate
    return None


# The Orca repo working tree, detected from this module's location. The data
# root must resolve OUTSIDE it.
_ORCA_REPO_ROOT = _detect_repo_root(Path(__file__))


def _is_inside_repo(path: Path, repo_root: Path | None) -> bool:
    if repo_root is None:
        return False
    try:
        path.resolve().relative_to(repo_root.resolve())
        return True
    except ValueError:
        return False


def _validate_packet_id(packet_id: str) -> str:
    if not _CROCKFORD_26.match(packet_id):
        raise DataLakeRootError(
            f"invalid packet_id (expected Crockford base32, 26 chars): {packet_id!r}"
        )
    return packet_id


def _validate_segment(name: str, *, role: str) -> str:
    if name in {".", ".."} or not _SAFE_SEGMENT.match(name):
        raise DataLakeRootError(f"invalid {role} path segment: {name!r}")
    return name


def _read_marker(root: Path) -> dict:
    marker = root / ROOT_MARKER_FILENAME
    if not marker.is_file():
        raise DataLakeRootError(
            f"missing root marker {ROOT_MARKER_FILENAME!r}; not an initialized Orca data root: {root}"
        )
    try:
        data = json.loads(marker.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise DataLakeRootError(f"unreadable root marker at {marker}: {exc}") from exc
    if not isinstance(data, dict) or "root_uuid" not in data or "contract_version" not in data:
        raise DataLakeRootError(f"malformed root marker at {marker}")
    return data


def _write_marker(root: Path, *, root_uuid: str, label: str | None) -> None:
    payload = {
        "root_uuid": root_uuid,
        "contract_version": ROOT_MARKER_CONTRACT_VERSION,
        "label": label,
        "created_at": utc_now_z(),
    }
    (root / ROOT_MARKER_FILENAME).write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


def _atomic_create(target: Path, data: bytes) -> None:
    """Create-only + crash-atomic publish: refuse if the target exists
    (write-once / append-only), write a sibling temp file, fsync, then
    atomically rename into place."""
    if target.exists():
        raise DataLakeRootError(f"refusing to overwrite existing record (create-only): {target}")
    target.parent.mkdir(parents=True, exist_ok=True)
    tmp = target.parent / f".{target.name}.{generate_ulid()}.tmp"
    try:
        with open(tmp, "xb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        if target.exists():  # create-only re-check before publish
            raise DataLakeRootError(
                f"refusing to overwrite existing record (create-only): {target}"
            )
        os.replace(tmp, target)
    finally:
        try:
            tmp.unlink()
        except FileNotFoundError:
            pass


def _production_candidate(
    *, explicit: str | os.PathLike[str] | None, env: dict[str, str], config_path: Path | None
) -> str | None:
    """Production precedence only: explicit/per-run -> ORCA_DATA_ROOT env ->
    optional config file. A test root is never part of this chain."""
    if explicit is not None:
        return str(explicit)
    env_value = env.get("ORCA_DATA_ROOT")
    if env_value:
        return env_value
    if config_path is not None and config_path.is_file():
        try:
            config = json.loads(config_path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            return None
        value = config.get("data_root") if isinstance(config, dict) else None
        if value:
            return str(value)
    return None


class DataLakeRoot:
    """A resolved, verified Orca data-lake root. Construct via ``resolve``,
    ``initialize``, or ``for_test`` — never trust a bare path."""

    def __init__(self, path: Path, *, _verified: bool) -> None:
        if not _verified:
            raise DataLakeRootError("construct DataLakeRoot via resolve()/initialize()/for_test()")
        self._path = path

    @property
    def path(self) -> Path:
        return self._path

    @property
    def root_uuid(self) -> str:
        return _read_marker(self._path)["root_uuid"]

    # -- construction -------------------------------------------------------

    @classmethod
    def resolve(
        cls,
        *,
        explicit: str | os.PathLike[str] | None = None,
        env: dict[str, str] | None = None,
        config_path: Path | None = None,
        expected_uuid: str | None = None,
        repo_root: Path | None = _ORCA_REPO_ROOT,
    ) -> "DataLakeRoot":
        """Resolve the production data root, fail-closed. A test root is NEVER
        part of this chain (use ``for_test``). Refuses to write when the root is
        unset, relative, inside the repo, absent/unmounted, not a directory,
        missing/mismatched its marker, or not writable."""
        env = os.environ if env is None else env
        candidate = _production_candidate(explicit=explicit, env=env, config_path=config_path)
        if candidate is None:
            raise DataLakeRootError(
                "ORCA_DATA_ROOT is unset/unresolvable (no explicit root, env var, or config); "
                "refusing to write (fail-closed)."
            )
        path = Path(candidate)
        if not path.is_absolute():
            raise DataLakeRootError(f"data root must be an absolute path: {path}")
        if _is_inside_repo(path, repo_root):
            raise DataLakeRootError(f"data root must resolve OUTSIDE the repo working tree: {path}")
        if not path.exists():
            raise DataLakeRootError(
                f"data root does not exist / not mounted (removable media absent?): {path}"
            )
        if not path.is_dir():
            raise DataLakeRootError(f"data root is not a directory: {path}")
        marker = _read_marker(path)  # raises if missing/malformed
        if expected_uuid is not None and marker["root_uuid"] != expected_uuid:
            raise DataLakeRootError(
                "root marker identity mismatch (drive letter may have been reassigned): "
                f"expected {expected_uuid}, found {marker['root_uuid']}"
            )
        if not os.access(path, os.W_OK):
            raise DataLakeRootError(f"data root is not writable: {path}")
        return cls(path, _verified=True)

    @classmethod
    def initialize(
        cls,
        path: str | os.PathLike[str],
        *,
        label: str | None = None,
        root_uuid: str | None = None,
        repo_root: Path | None = _ORCA_REPO_ROOT,
    ) -> "DataLakeRoot":
        """Create (or verify) the root: marker + directory skeleton. Idempotent
        when a well-formed marker already exists; refuses to claim a non-empty
        directory that lacks a marker."""
        path = Path(path)
        if not path.is_absolute():
            raise DataLakeRootError(f"data root must be an absolute path: {path}")
        if _is_inside_repo(path, repo_root):
            raise DataLakeRootError(f"data root must be OUTSIDE the repo working tree: {path}")
        return cls._init_at(path, label=label, root_uuid=root_uuid)

    @classmethod
    def for_test(cls, path: str | os.PathLike[str], *, label: str = "test") -> "DataLakeRoot":
        """TEST-MODE ONLY. Initializes a root at ``path`` bypassing the
        outside-repo guard (tests use temp dirs that live inside the repo).
        Never reachable from production ``resolve``."""
        return cls._init_at(Path(path), label=label, root_uuid=None)

    @classmethod
    def _init_at(cls, path: Path, *, label: str | None, root_uuid: str | None) -> "DataLakeRoot":
        marker = path / ROOT_MARKER_FILENAME
        if path.exists():
            if not path.is_dir():
                raise DataLakeRootError(f"data root path is not a directory: {path}")
            if marker.is_file():
                _read_marker(path)  # verify the existing marker is well-formed
            elif any(path.iterdir()):
                raise DataLakeRootError(
                    f"refusing to initialize a non-empty directory that lacks a root marker: {path}"
                )
            else:
                _write_marker(path, root_uuid=root_uuid or generate_ulid(), label=label)
        else:
            path.mkdir(parents=True, exist_ok=False)
            _write_marker(path, root_uuid=root_uuid or generate_ulid(), label=label)
        for sub in LAKE_SUBDIRECTORIES:
            (path / sub).mkdir(parents=True, exist_ok=True)
        return cls(path, _verified=True)

    # -- guarded writes -----------------------------------------------------

    def _within(self, *parts: str) -> Path:
        target = self._path.joinpath(*parts).resolve()
        try:
            target.relative_to(self._path.resolve())
        except ValueError as exc:
            raise DataLakeRootError(f"refusing path escape outside the data root: {target}") from exc
        return target

    def allocate_raw_packet_dir(self, packet_id: str) -> Path:
        """Create the write-once raw packet container ``raw/<packet_id>/`` and
        return it. Create-only: fails if it already exists."""
        _validate_packet_id(packet_id)
        container = self._within("raw", packet_id)
        (self._path / "raw").mkdir(parents=True, exist_ok=True)
        try:
            container.mkdir(parents=False, exist_ok=False)
        except FileExistsError as exc:
            raise DataLakeRootError(
                f"raw packet container already exists (write-once): {container}"
            ) from exc
        return container

    def append_record(
        self, *, subtree: str, raw_anchor: str, lane: str, record_id: str, data: bytes
    ) -> Path:
        """Append-only create of a derived or acknowledgement record at
        ``<subtree>/<raw_anchor>/<lane>/<record_id>``. Refuses overwrite."""
        if subtree not in _APPENDABLE_SUBTREES:
            raise DataLakeRootError(
                f"append_record subtree must be one of {_APPENDABLE_SUBTREES}: {subtree!r}"
            )
        _validate_segment(raw_anchor, role="raw_anchor")
        _validate_segment(lane, role="lane")
        _validate_segment(record_id, role="record_id")
        target = self._within(subtree, raw_anchor, lane, record_id)
        _atomic_create(target, data)
        return target
