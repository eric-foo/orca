from __future__ import annotations

from pathlib import Path

import pytest

from data_lake.root import DataLakeRoot, DataLakeRootError, LoadedRawPacket
from harness_utils import generate_ulid
from source_capture.models import known_fact
from source_capture.writer import write_local_source_capture_packet


def _capture(root: DataLakeRoot, tmp_path: Path, body: bytes):
    # A committed raw packet in the lake. Any family works; the loader is
    # spine-agnostic. The capture path is the one already on main (data_root seam).
    src = tmp_path / "blob.bin"
    src.write_bytes(body)
    return write_local_source_capture_packet(
        data_root=root,
        input_files=[src],
        source_family="reddit",
        source_surface="s",
        source_locator=known_fact("https://example.com/x"),
        decision_question="q",
        capture_context="loader test",
    )


def test_load_raw_packet_returns_verified_bodies(tmp_path: Path) -> None:
    # The read half: find raw by key, verify the seal, hand back bytes by file_id.
    root = DataLakeRoot.for_test(tmp_path / "orca-data")
    body = b"AAAAAAAAAAAAAAAA"
    pid = _capture(root, tmp_path, body).packet.packet_id

    loaded = root.load_raw_packet(pid)
    assert isinstance(loaded, LoadedRawPacket)
    assert loaded.container == root.path / "raw" / pid
    assert loaded.manifest["packet_id"] == pid
    assert list(loaded.bodies.values()) == [body]
    # bodies are keyed exactly by the manifest's preserved-file ids
    assert set(loaded.bodies) == {pf["file_id"] for pf in loaded.manifest["preserved_files"]}


def test_load_raw_packet_detects_sha256_tampering(tmp_path: Path) -> None:
    # Same length, different content -> size check passes, sha256 check catches it.
    root = DataLakeRoot.for_test(tmp_path / "orca-data")
    pid = _capture(root, tmp_path, b"AAAAAAAAAAAAAAAA").packet.packet_id

    container = root.find_packet(pid)
    assert container is not None
    next((container / "raw").iterdir()).write_bytes(b"AAAAAAAAAAAAAAAB")

    with pytest.raises(DataLakeRootError):
        root.load_raw_packet(pid)


def test_load_raw_packet_detects_missing_file(tmp_path: Path) -> None:
    root = DataLakeRoot.for_test(tmp_path / "orca-data")
    pid = _capture(root, tmp_path, b"some bytes").packet.packet_id

    container = root.find_packet(pid)
    assert container is not None
    next((container / "raw").iterdir()).unlink()

    with pytest.raises(DataLakeRootError):
        root.load_raw_packet(pid)


def test_load_raw_packet_unknown_key_fails_closed(tmp_path: Path) -> None:
    root = DataLakeRoot.for_test(tmp_path / "orca-data")
    with pytest.raises(DataLakeRootError):
        root.load_raw_packet(generate_ulid())
