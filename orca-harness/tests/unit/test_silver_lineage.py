from __future__ import annotations

import pytest

from data_lake.silver_lineage import (
    SilverLineageError,
    build_silver_vault_record,
    derived_record_ref,
    is_full_source_backed,
    lineage_limitation,
    source_object_ref,
    validate_silver_vault_record,
)


def _source_object() -> dict:
    return source_object_ref(namespace="youtube", kind="transcript", native_id="vid12345678")


def _payload() -> dict:
    return {"video_id": "vid12345678", "mention_count": 1}


def _derived_ref() -> dict:
    return derived_record_ref(
        raw_anchor="AUDIOPACKET00000000000000",
        lane="transcript_asr",
        record_id="asr_small__1234567890abcdef",
        sha256="abc123",
        hash_basis="derived_record_marker_sha256",
        relation="consumed",
        record_set_completion_lane="transcript_asr__set",
    )


def test_build_record_populates_header_without_nested_silver_lineage() -> None:
    record = build_silver_vault_record(
        payload=_payload(),
        record_id="mentions_model__1234567890abcdef.json",
        raw_anchor="AUDIOPACKET00000000000000",
        lane_namespace="silver__cleaning__product_mentions",
        producer_id="test_producer",
        producer_schema_version="test_schema_v0",
        record_kind="observation",
        payload_kind="TranscriptProductMentionSet",
        producer_row_kind="transcript_product_mentions",
        source_surface="youtube_audio",
        source_object=_source_object(),
        observed_at=None,
        captured_at="2026-06-29T00:00:00Z",
        derived_refs=[_derived_ref()],
        require_full_source_backed=True,
    )

    assert "silver_lineage" not in record
    assert record["schema_version"] == "silver_vault_record_v0"
    assert record["derived_refs"][0]["record_id"] == "asr_small__1234567890abcdef"
    assert record["content_hash"].startswith("sha256:")
    validate_silver_vault_record(record, require_full_source_backed=True)


def test_derived_ref_requires_complete_projection_row_locator() -> None:
    with pytest.raises(SilverLineageError, match="row_locator"):
        derived_record_ref(
            raw_anchor="raw1",
            lane="projection_retail_pdp",
            record_id="projection.json",
            row_id="row-1",
        )


def test_missing_refs_require_explicit_limitation() -> None:
    with pytest.raises(SilverLineageError, match="raw_refs, derived_refs, or explicit"):
        build_silver_vault_record(
            payload=_payload(),
            record_id="mentions_model__1234567890abcdef.json",
            raw_anchor="AUDIOPACKET00000000000000",
            lane_namespace="silver__cleaning__product_mentions",
            producer_id="test_producer",
            producer_schema_version="test_schema_v0",
            record_kind="observation",
            payload_kind="TranscriptProductMentionSet",
            producer_row_kind="transcript_product_mentions",
            source_surface="youtube_audio",
            source_object=_source_object(),
            observed_at=None,
            captured_at=None,
        )


def test_limitations_only_record_is_valid_but_not_full_source_backed() -> None:
    record = build_silver_vault_record(
        payload=_payload(),
        record_id="mentions_model__1234567890abcdef.json",
        raw_anchor="RAWLESSSHORTCODE",
        lane_namespace="silver__capture__reel_transcript",
        producer_id="test_producer",
        producer_schema_version="test_schema_v0",
        record_kind="observation",
        payload_kind="ReelTranscriptObservation",
        producer_row_kind="ig_reel_transcript",
        source_surface="instagram_deep_capture",
        source_object=source_object_ref(
            namespace="instagram", kind="platform_content", native_id="RAWLESSSHORTCODE"
        ),
        observed_at=None,
        captured_at=None,
        lineage_limitations=[lineage_limitation("transient_source_not_persisted")],
    )

    assert not is_full_source_backed(record)
    validate_silver_vault_record(record)
    with pytest.raises(SilverLineageError, match="not eligible"):
        validate_silver_vault_record(record, require_full_source_backed=True)