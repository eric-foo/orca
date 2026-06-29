from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

import pytest

from cleaning import CleaningPacket
from cleaning.fragrantica import build_fragrantica_cleaning_packet
from cleaning.fragrantica_lake import (
    FRAGRANTICA_CLEANING_LANE,
    FRAGRANTICA_CLEANING_RECORD_SCHEMA_VERSION,
    derive_fragrantica_cleaning_into_lake,
    fragrantica_cleaning_record_payload,
)
from data_lake.root import DataLakeRoot, DataLakeRootError, raw_shard
from source_capture.fragrantica_projection import build_fragrantica_projection
from source_capture.models import (
    PacketTiming,
    SourceCapturePacket,
    SourceCaptureSlice,
    known_fact,
    not_applicable,
    not_attempted,
    unknown_with_reason,
)
from source_capture.writer import write_local_source_capture_packet


_CAPTURE_TIME = "2026-06-28T18:57:58Z"


def test_derives_fragrantica_cleaning_packet_into_derived_record(tmp_path: Path) -> None:
    root = DataLakeRoot.for_test(tmp_path / "orca-data")
    packet_id = _commit_fragrantica_packet(root, tmp_path)

    cleaning_packet, derived_path = derive_fragrantica_cleaning_into_lake(
        data_root=root,
        packet_id=packet_id,
    )

    assert derived_path.parent == root.path / "derived" / raw_shard(packet_id) / packet_id / FRAGRANTICA_CLEANING_LANE
    assert derived_path.suffix == ".json"
    assert derived_path.is_file()

    record = json.loads(derived_path.read_text(encoding="utf-8"))
    assert record["record_id"] == derived_path.name
    assert record["raw_anchor"] == packet_id
    assert record["lane_namespace"] == FRAGRANTICA_CLEANING_LANE
    assert record["schema_version"] == "silver_vault_record_v0"
    assert record["producer_schema_version"] == FRAGRANTICA_CLEANING_RECORD_SCHEMA_VERSION
    assert record["record_kind"] == "observation"
    assert record["payload_kind"] == "FragranticaCleaningPacket"
    assert record["source_family"] == "fragrance_native_database"
    assert record["source_surface"] == "fragrantica_product_page_direct_http"
    assert isinstance(record["observed_at"], str)
    assert record["observed_at"].endswith("Z")
    assert record["captured_at"] == record["observed_at"]
    assert record["content_hash"] == f"sha256:{_content_hash(record)}"
    assert record["content_hash_basis"] == "canonical_json_excluding_content_hash"
    assert record["raw_refs"]
    assert {ref["packet_id"] for ref in record["raw_refs"]} == {packet_id}
    assert {ref["file_id"] for ref in record["raw_refs"]} == {"file_01"}
    assert all(ref["sha256"] and ref["hash_basis"] == "raw_stored_bytes" for ref in record["raw_refs"])

    assert record["payload"]["handle_count"] == len(cleaning_packet.handles)
    assert record["payload"]["transform_entry_count"] == len(cleaning_packet.transform_ledger)
    round_tripped = CleaningPacket.model_validate(record["payload"]["cleaning_packet"])
    assert len(round_tripped.handles) == len(cleaning_packet.handles)
    assert len(round_tripped.transform_ledger) == len(cleaning_packet.transform_ledger)
    assert {
        handle.ecr_ref.status
        for handle in round_tripped.handles
        if handle.ecr_ref is not None
    } == {"by_convention_not_existence_checked"}


def test_fragrantica_cleaning_record_rejects_unknown_capture_time(tmp_path: Path) -> None:
    root = DataLakeRoot.for_test(tmp_path / "orca-data")
    packet_id = _commit_fragrantica_packet(root, tmp_path)
    loaded = root.load_raw_packet(packet_id)
    packet = SourceCapturePacket.model_validate(loaded.manifest)
    packet = packet.model_copy(
        update={
            "timing": packet.timing.model_copy(
                update={"capture_time": unknown_with_reason("fixture hides capture time")}
            )
        }
    )
    projection = build_fragrantica_projection(
        packet=packet,
        raw_file_bytes_by_file_id=loaded.bodies,
    )
    cleaning_packet = build_fragrantica_cleaning_packet(projection)

    with pytest.raises(ValueError, match="known capture_time"):
        fragrantica_cleaning_record_payload(
            packet=packet,
            cleaning_packet=cleaning_packet,
            record_id="rec.json",
        )


def test_fragrantica_cleaning_record_preserves_current_window_residuals(tmp_path: Path) -> None:
    root = DataLakeRoot.for_test(tmp_path / "orca-data")
    packet_id = _commit_fragrantica_packet(root, tmp_path)

    _, derived_path = derive_fragrantica_cleaning_into_lake(data_root=root, packet_id=packet_id)

    record = json.loads(derived_path.read_text(encoding="utf-8"))
    coverage = record["coverage"]
    assert coverage["current_window_only"] is True
    assert coverage["full_archive_captured"] is False
    assert "full_review_archive_not_captured_login_prompt_present" in coverage["residuals"]
    assert "inspect_raw_before_archive_completeness_claim" in coverage["raw_pull_triggers"]
    assert "not_judgment" in record["non_claims"]
    assert "not_demand_signal" in record["non_claims"]
    assert "not_sentiment_analysis" in record["non_claims"]


def test_fragrantica_cleaning_re_derive_appends_sibling_not_overwrite(tmp_path: Path) -> None:
    root = DataLakeRoot.for_test(tmp_path / "orca-data")
    packet_id = _commit_fragrantica_packet(root, tmp_path)

    _, first = derive_fragrantica_cleaning_into_lake(data_root=root, packet_id=packet_id)
    _, second = derive_fragrantica_cleaning_into_lake(data_root=root, packet_id=packet_id)

    lane_dir = root.path / "derived" / raw_shard(packet_id) / packet_id / FRAGRANTICA_CLEANING_LANE
    assert first != second
    assert len(list(lane_dir.glob("*.json"))) == 2


def test_fragrantica_cleaning_explicit_record_id_is_create_only(tmp_path: Path) -> None:
    root = DataLakeRoot.for_test(tmp_path / "orca-data")
    packet_id = _commit_fragrantica_packet(root, tmp_path)

    _, first = derive_fragrantica_cleaning_into_lake(
        data_root=root,
        packet_id=packet_id,
        record_id="rec1",
    )
    with pytest.raises(DataLakeRootError):
        derive_fragrantica_cleaning_into_lake(
            data_root=root,
            packet_id=packet_id,
            record_id="rec1",
        )
    assert first.read_text(encoding="utf-8")


def _commit_fragrantica_packet(root: DataLakeRoot, tmp_path: Path) -> str:
    body_path = tmp_path / "http_response_body.bin"
    body_path.write_text(_html(), encoding="utf-8")
    metadata_path = tmp_path / "http_response_metadata.json"
    metadata_path.write_text('{"status": 200}\n', encoding="utf-8")

    timing = PacketTiming(
        source_publication_or_event=unknown_with_reason("fixture does not supply source event timing"),
        source_edit_or_version=unknown_with_reason("fixture does not supply edit timing"),
        capture_time=known_fact(_CAPTURE_TIME),
        recapture_time=not_applicable("first capture"),
        cutoff_posture=unknown_with_reason("test fixture has no decision cutoff"),
    )
    source_slice = SourceCaptureSlice(
        slice_id="slice_01",
        locator=known_fact(
            "https://www.fragrantica.com/perfume/Maison-Francis-Kurkdjian/Baccarat-Rouge-540-33519.html"
        ),
        timing=timing,
        access_posture=known_fact("direct HTTP fixture supplied"),
        archive_history_posture=not_attempted("archive not queried"),
        media_modality_posture=not_attempted("linked media not fetched"),
        re_capture_relationship=not_applicable("first capture"),
        limitations=[],
        warning_notes=[],
        preserved_file_ids=["file_01", "file_02"],
    )
    result = write_local_source_capture_packet(
        data_root=root,
        input_files=[body_path, metadata_path],
        source_family="fragrance_native_database",
        source_surface="fragrantica_product_page_direct_http",
        source_locator=known_fact(
            "https://www.fragrantica.com/perfume/Maison-Francis-Kurkdjian/Baccarat-Rouge-540-33519.html"
        ),
        decision_question="test Fragrantica Cleaning into lake",
        capture_context="fragrantica cleaning lake pilot",
        source_slices=[source_slice],
    )
    return result.packet.packet_id


def _html() -> str:
    return """
    <html><head>
      <link rel="canonical" href="https://www.fragrantica.com/perfume/Maison-Francis-Kurkdjian/Baccarat-Rouge-540-33519.html"/>
      <title>Baccarat Rouge 540 Maison Francis Kurkdjian perfume</title>
    </head><body>
      <div id="perfume-description-content" itemprop="description">
        <p><b>Baccarat Rouge 540</b> by <b>Maison Francis Kurkdjian</b> is a fragrance. Baccarat Rouge 540 was launched in 2015.</p>
      </div>
      <p itemprop="aggregateRating"><span itemprop="ratingValue">3.76</span><span itemprop="bestRating">5</span><span itemprop="ratingCount" content="28808">28,808</span></p>
      <span>Reviews (<span>3.9K</span>)</span>
      <button data-tab="all-reviews" data-active="true">All reviews by date</button>
      <div class="review-tab-panel" id="all-reviews">
        <div id="parent3090334" class="cell tw-review-card tw-gradient-rose" itemprop="review" itemscope>
          <user-perfume-votes-new :perfume-votes="{&quot;rating&quot;:5,&quot;winter&quot;:0,&quot;spring&quot;:0,&quot;summer&quot;:0,&quot;autumn&quot;:0,&quot;day&quot;:0,&quot;night&quot;:0,&quot;longevity&quot;:3,&quot;sillage&quot;:2,&quot;gender&quot;:&quot;female_unisex&quot;,&quot;relation&quot;:&quot;have&quot;}"></user-perfume-votes-new>
          <meta itemprop="name" content="Rimazy"/>
          <span itemprop="datePublished" content="2026-06-25">06/25/26 18:41</span>
          <div id="review_3090334"><p>This perfume died young.</p></div>
          <vote-buttons-new initial-status="neutral" item-id="33519" comment-id="3090334" vote-for="perfumeReview"></vote-buttons-new>
          <share-new path="/perfume/Maison-Francis-Kurkdjian/Baccarat-Rouge-540-33519.html?ccid=3090334#focus-zone"></share-new>
        </div>
        <reviews-infinity-new :perfume-id="33519" sentiment="all" :is-logged="false" login-url="/board/login.php"
          :lang-strings="{&quot;loginPromptMessage&quot;:&quot;Sign in to access the full review archive&quot;}">
        </reviews-infinity-new>
      </div>
    </body></html>
    """


def _content_hash(record: dict[str, Any]) -> str:
    canonical = dict(record)
    canonical.pop("content_hash", None)
    return hashlib.sha256(
        json.dumps(
            canonical,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
            allow_nan=False,
        ).encode("utf-8")
    ).hexdigest()