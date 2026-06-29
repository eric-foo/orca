from __future__ import annotations

import hashlib
import json
from datetime import date
from pathlib import Path

import pytest

from data_lake.root import DataLakeRoot, DataLakeRootError, raw_shard
from source_capture.fragrance_rendered_widget_companion import FragranceWidgetResponseCapture
from source_capture.fragrance_review_lake import (
    PROJECTION_FRAGRANCE_REVIEW_LANE,
    project_fragrance_review_into_lake,
    write_fragrance_review_capture_packet,
)

# Pinned so the projection's recency-based selection is deterministic across
# re-derivations (build_fragrance_review_coverage otherwise defaults to today()).
_AS_OF = date(2026, 6, 30)
_PRODUCT_URL = "https://examplefragrance.example/products/synthetic-eau"

# A minimal, fully SYNTHETIC Yotpo-v3-shaped widget response. No captured PII
# lives on-tree; bottomline + pagination make build_fragrance_review_coverage
# treat the row as a yotpo_v3_review and yield a non-trivial projection.
_WIDGET_BODY = json.dumps(
    {
        "reviews": [
            {
                "id": 90001,
                "content": "Synthetic test review body for the lake tee pilot fixture.",
                "score": 5,
                "created_at": "2026-05-01T00:00:00Z",
                "verified_buyer": True,
            }
        ],
        "bottomline": {"totalReview": 1, "averageScore": 5.0},
        "pagination": {"page": 1, "perPage": 10, "total": 1},
    },
    sort_keys=True,
)

# Fields that only ever belong to the derived coverage projection -- never to a
# preserved raw widget body or the raw manifest.
_CONTAMINATION_TOKENS = (
    "selected_for_reader",
    "selection_reasons",
    "coverage_method",
    "candidate_review_key",
)


def _synthetic_widget_response() -> FragranceWidgetResponseCapture:
    body = _WIDGET_BODY
    return FragranceWidgetResponseCapture(
        response_index=1,
        response_origin="render_passive",
        response_kind="yotpo_v3_reviews",
        requested_url="https://api-cdn.yotpo.com/v3/storefront/store/SYN/product/SYN/reviews",
        final_url="https://api-cdn.yotpo.com/v3/storefront/store/SYN/product/SYN/reviews",
        status=200,
        ok=True,
        body_sha256=hashlib.sha256(body.encode("utf-8")).hexdigest(),
        body_byte_count=len(body.encode("utf-8")),
        body_text=body,
    )


def _capture(root: DataLakeRoot) -> tuple[object, FragranceWidgetResponseCapture]:
    response = _synthetic_widget_response()
    result = write_fragrance_review_capture_packet(
        data_root=root,
        widget_responses=[response],
        product_url=_PRODUCT_URL,
    )
    return result, response


def test_exact_bytes_hash_equivalence_capture_equals_stored(tmp_path: Path) -> None:
    # (a) The capture-time hash of the widget body equals the hash the lake
    # recomputes from the committed preserved body -- exact bytes, end to end.
    root = DataLakeRoot.for_test(tmp_path / "orca-data")
    result, response = _capture(root)
    pid = result.packet.packet_id

    capture_hash = response.body_sha256

    loaded = root.load_raw_packet(pid)
    assert len(loaded.bodies) == 1
    ((_file_id, stored_bytes),) = loaded.bodies.items()
    stored_body_hash = hashlib.sha256(stored_bytes).hexdigest()
    manifest_pf = loaded.manifest["preserved_files"][0]

    assert capture_hash == stored_body_hash
    assert manifest_pf["sha256"] == capture_hash
    assert manifest_pf["hash_basis"] == "raw_stored_bytes"
    # the preserved body is exactly the UTF-8 encoding of the captured body_text
    assert stored_bytes == response.body_text.encode("utf-8")


def test_re_derive_appends_a_sibling_not_overwrite(tmp_path: Path) -> None:
    # (b) Re-derive = new sibling record (append-only), never an overwrite.
    root = DataLakeRoot.for_test(tmp_path / "orca-data")
    result, _ = _capture(root)
    pid = result.packet.packet_id

    _, first = project_fragrance_review_into_lake(data_root=root, packet_id=pid, as_of_date=_AS_OF)
    _, second = project_fragrance_review_into_lake(data_root=root, packet_id=pid, as_of_date=_AS_OF)

    lane_dir = root.path / "derived" / raw_shard(pid) / pid / PROJECTION_FRAGRANCE_REVIEW_LANE
    assert first != second
    assert sorted(p.name for p in lane_dir.glob("*.json")) == sorted([first.name, second.name])
    assert len(list(lane_dir.glob("*.json"))) == 2


def test_packet_grained_rebuild_is_byte_identical(tmp_path: Path) -> None:
    # (c) The projection is a pure function of the committed bytes (+ pinned
    # as_of_date): a fresh derivation is byte-identical, and packet-grained
    # availability rebuilds from committed raw alone without changing.
    root = DataLakeRoot.for_test(tmp_path / "orca-data")
    result, _ = _capture(root)
    pid = result.packet.packet_id

    _, first = project_fragrance_review_into_lake(
        data_root=root, packet_id=pid, record_id="rec1", as_of_date=_AS_OF
    )
    first_bytes = first.read_bytes()
    _, second = project_fragrance_review_into_lake(
        data_root=root, packet_id=pid, record_id="rec2", as_of_date=_AS_OF
    )
    assert second.read_bytes() == first_bytes

    before = root.read_availability(pid)
    assert root.rebuild_availability() == 1
    assert root.read_availability(pid) == before

    # the raw is untouched: a fresh verified read still succeeds
    assert root.load_raw_packet(pid).manifest["packet_id"] == pid

    # explicit record id is create-only (append-only guard observable)
    with pytest.raises(DataLakeRootError):
        project_fragrance_review_into_lake(data_root=root, packet_id=pid, record_id="rec1", as_of_date=_AS_OF)


def test_contamination_guard_raw_bodies_carry_only_raw_widget_responses(tmp_path: Path) -> None:
    # (d) Preserved bodies + manifest carry ONLY raw widget responses; all
    # coverage/selection fields live only in the derived projection.
    root = DataLakeRoot.for_test(tmp_path / "orca-data")
    result, response = _capture(root)
    pid = result.packet.packet_id

    loaded = root.load_raw_packet(pid)
    ((_file_id, stored_bytes),) = loaded.bodies.items()
    parsed = json.loads(stored_bytes)
    assert isinstance(parsed, dict) and "reviews" in parsed
    assert stored_bytes == response.body_text.encode("utf-8")

    body_text = stored_bytes.decode("utf-8")
    manifest_text = json.dumps(loaded.manifest, sort_keys=True)
    for token in _CONTAMINATION_TOKENS:
        assert token not in body_text, f"raw body leaked projection field: {token}"
        assert token not in manifest_text, f"raw manifest leaked projection field: {token}"

    # the split proven the other way: the derived record DOES carry the
    # coverage/selection fields.
    receipt, derived_path = project_fragrance_review_into_lake(
        data_root=root, packet_id=pid, as_of_date=_AS_OF
    )
    derived_text = derived_path.read_text(encoding="utf-8")
    assert "coverage_method" in derived_text
    assert "selected_for_reader" in derived_text
    assert receipt.coverage_summary.total_rows >= 1
