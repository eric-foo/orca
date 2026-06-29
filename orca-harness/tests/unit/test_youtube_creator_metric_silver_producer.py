"""Unit tests for the YouTube creator-metric Silver Vault producer.

These run the producer against the REAL committed
``youtube_shorts_fragrance_creator_metric_seed_v0.json`` (Option 2 wraps the
committed seed, so no-drift is the strongest possible: the emitted numbers ARE
the committed, already-tested seed numbers) into a temp lake
(``DataLakeRoot.for_test`` -- no external lake drive). They assert the producer
emits Silver Vault-conformant records, reproduces ``content_hash`` independently,
obeys posture/value coupling, threads rollup -> observation lineage via
``derived_refs``, anchors observations to their per-Short packet and rollups to
their account id, and fails closed on a blank subject native_id.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pytest

from capture_spine.creator_profile_current.youtube_silver_metric_producer import (
    DEFAULT_YOUTUBE_SEED_PATH,
    METRIC_OBSERVATION_LANE,
    METRIC_OBSERVATION_PAYLOAD_KIND,
    METRIC_ROLLUP_LANE,
    METRIC_ROLLUP_PAYLOAD_KIND,
    YOUTUBE_SEED_WRAPPER_KEY,
    build_metric_observation_record,
    derive_youtube_creator_metric_silver_records_from_seed,
)
from data_lake.root import DataLakeRoot

EXPECTED_OBSERVATIONS = 196
EXPECTED_ROLLUPS = 30


def _content_hash(record: dict) -> str:
    """Independent re-implementation of the canonical content hash (catches a
    producer-side helper mistake instead of trusting it)."""
    canonical = dict(record)
    canonical.pop("content_hash", None)
    payload = json.dumps(
        canonical, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False
    )
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _committed_seed_document() -> dict:
    return json.loads(DEFAULT_YOUTUBE_SEED_PATH.read_text(encoding="utf-8-sig"))


def _run(tmp_path: Path):
    seed_document = _committed_seed_document()
    data_root = DataLakeRoot.for_test(tmp_path / "lake")
    result = derive_youtube_creator_metric_silver_records_from_seed(
        data_root=data_root, seed_document=seed_document
    )
    return result, seed_document[YOUTUBE_SEED_WRAPPER_KEY]


def test_producer_emits_conformant_metric_observation_records(tmp_path: Path) -> None:
    result, seed = _run(tmp_path)
    assert len(result.observation_records) == EXPECTED_OBSERVATIONS == len(seed["metric_observations"])

    seed_by_id = {o["metric_observation_id"]: o for o in seed["metric_observations"]}
    for record in result.observation_records:
        assert record["schema_version"] == "silver_vault_record_v0"
        assert record["record_kind"] == "observation"
        assert record["payload_kind"] == METRIC_OBSERVATION_PAYLOAD_KIND
        assert record["lane_namespace"] == METRIC_OBSERVATION_LANE
        assert record["content_hash_basis"] == "canonical_json_excluding_content_hash"
        assert record["source_family"] == "social_media"
        assert record["source_surface"] == "youtube_shorts"
        # content_hash reproduces independently from the record's own content.
        assert record["content_hash"] == f"sha256:{_content_hash(record)}"

        seed_obs = seed_by_id[record["provenance"]["seed_metric_observation_id"]]
        # Observation anchors to its own per-Short raw packet id (mirrors IG).
        assert record["raw_anchor"] == seed_obs["source_packet_id_or_none"]

        # raw_refs are honest YouTube provenance (no IG-style raw_anchor dict),
        # carrying sha256 + hash_basis per the Silver Vault raw_refs rule.
        raw_ref = record["raw_refs"][0]
        assert raw_ref["packet_id"] == seed_obs["source_packet_id_or_none"]
        assert raw_ref["source_pointer"] == seed_obs["source_pointer"]
        assert raw_ref["source_field"] == seed_obs["source_field"]
        assert raw_ref["sha256"] == seed_obs["source_watch_html_sha256_or_none"]
        assert raw_ref["hash_basis"] == "source_captured_watch_html_sha256"

        observation = record["payload"]["observation"]
        # Subject is the public content object keyed by stable ids only.
        subject_ref = observation["subject"]["ref"]
        assert observation["subject"]["ref_type"] == "entity_key"
        assert subject_ref["namespace"] == "youtube"
        assert subject_ref["kind"] == "public_content_object"
        assert subject_ref["native_id"] == seed_obs["content_id_or_none"]
        assert subject_ref["published_by_account_native_id"] == seed_obs["platform_subject_key"]
        assert subject_ref["orca_platform_account_id"] == seed_obs["platform_account_id"]

        posture = observation["metric_posture"]
        if posture["kind"] == "observed":
            assert isinstance(observation["metric_value"], (int, float))
            assert not isinstance(observation["metric_value"], bool)
            assert posture["reason_detail"] is None
        else:
            assert observation["metric_value"] is None
            assert posture["reason_detail"]


def test_observation_no_drift_against_committed_seed(tmp_path: Path) -> None:
    result, seed = _run(tmp_path)
    seed_by_id = {o["metric_observation_id"]: o for o in seed["metric_observations"]}
    for record in result.observation_records:
        seed_obs = seed_by_id[record["provenance"]["seed_metric_observation_id"]]
        observation = record["payload"]["observation"]
        # No-drift: the emitted number equals the committed seed observation.
        assert observation["metric_value"] == seed_obs["metric_value_or_none"]
        assert observation["metric_name"] == seed_obs["metric_name"]
        assert observation["unit"] == seed_obs["metric_unit"]


def test_observation_records_written_and_reload_with_stable_hash(tmp_path: Path) -> None:
    result, _ = _run(tmp_path)
    assert len(result.observation_paths) == len(result.observation_records) == EXPECTED_OBSERVATIONS
    # Spot-check the first/last 5 reload with a self-reproducing hash (full set is
    # already covered by the conformance test; this proves the bytes-on-disk path).
    sample = result.observation_records[:5] + result.observation_records[-5:]
    sample_paths = result.observation_paths[:5] + result.observation_paths[-5:]
    for record, path in zip(sample, sample_paths, strict=True):
        assert path.exists()
        on_disk = json.loads(path.read_text(encoding="utf-8"))
        assert on_disk["record_id"] == record["record_id"]
        assert on_disk["content_hash"] == f"sha256:{_content_hash(on_disk)}"


def test_rollup_records_lineage_and_no_drift(tmp_path: Path) -> None:
    result, seed = _run(tmp_path)
    assert len(result.rollup_records) == EXPECTED_ROLLUPS == len(seed["metric_rollups"])

    seed_by_id = {r["metric_rollup_id"]: r for r in seed["metric_rollups"]}
    observations_by_record_id = {r["record_id"]: r for r in result.observation_records}

    for rollup in result.rollup_records:
        assert rollup["record_kind"] == "observation"
        assert rollup["payload_kind"] == METRIC_ROLLUP_PAYLOAD_KIND
        assert rollup["lane_namespace"] == METRIC_ROLLUP_LANE
        assert rollup["content_hash"] == f"sha256:{_content_hash(rollup)}"

        seed_rollup = seed_by_id[rollup["provenance"]["seed_metric_rollup_id"]]
        # Rollup anchors to its platform account id (not a single packet).
        assert rollup["raw_anchor"] == seed_rollup["profile_subject_id"]

        payload = rollup["payload"]["observation"]
        # derived_refs point at the emitted observation records; hash matches.
        assert len(rollup["derived_refs"]) == len(seed_rollup["source_metric_observation_ids"])
        for edge in rollup["derived_refs"]:
            assert edge["edge_type"] == "derived_from_record"
            assert edge["lane_namespace"] == METRIC_OBSERVATION_LANE
            assert edge["content_hash"] == observations_by_record_id[edge["record_id"]]["content_hash"]

        # Mandatory derivation marker (not optional prose).
        assert payload["derivation"] == {
            "kind": "computed_metric_rollup",
            "source_record_ref_kind": "derived_refs",
            "metric_posture_semantics": "source_input_support_not_raw_aggregate_visibility",
            "calculation_recipe_version": seed_rollup["calculation_recipe_version"],
        }

        # No-drift: every rollup number equals the committed seed computation.
        assert payload["observation_count"] == seed_rollup["observation_count"]
        assert payload["view_count_min"] == seed_rollup["view_count_min"]
        assert payload["view_count_max"] == seed_rollup["view_count_max"]
        assert payload["sample_support"] == seed_rollup["sample_support"]
        assert payload["limitations"] == seed_rollup["limitations"]
        for name, seed_metric in seed_rollup["metric_rollups"].items():
            assert payload["metric_rollups"][name]["metric_value"] == seed_metric["value_or_none"]
            assert payload["metric_rollups"][name]["unit"] == seed_metric["metric_unit"]


def test_rollup_metric_posture_value_coupling(tmp_path: Path) -> None:
    result, _ = _run(tmp_path)
    saw_observed = False
    saw_non_observed = False
    for rollup in result.rollup_records:
        for metric in rollup["payload"]["observation"]["metric_rollups"].values():
            posture = metric["metric_posture"]
            if posture["kind"] == "observed":
                saw_observed = True
                assert isinstance(metric["metric_value"], (int, float))
                assert not isinstance(metric["metric_value"], bool)
                assert posture["reason_detail"] is None
            else:
                saw_non_observed = True
                assert metric["metric_value"] is None
                assert posture["reason_detail"]
    # The YouTube seed has both observed (average/median views) and non-observed
    # (engagement_rate/like/comment/cadence/velocity) rollup metrics.
    assert saw_observed and saw_non_observed


def test_observations_anchor_to_distinct_packets_rollups_to_accounts(tmp_path: Path) -> None:
    result, seed = _run(tmp_path)
    # Each observation anchors to its own distinct per-Short packet.
    obs_anchors = [r["raw_anchor"] for r in result.observation_records]
    assert len(set(obs_anchors)) == EXPECTED_OBSERVATIONS
    # Rollups anchor to the 30 distinct account ids.
    rollup_anchors = {r["raw_anchor"] for r in result.rollup_records}
    assert rollup_anchors == {r["profile_subject_id"] for r in seed["metric_rollups"]}
    assert len(rollup_anchors) == EXPECTED_ROLLUPS


def test_content_subject_missing_native_id_fails_closed() -> None:
    seed_document = _committed_seed_document()
    seed_obs = dict(seed_document[YOUTUBE_SEED_WRAPPER_KEY]["metric_observations"][0])
    seed_obs["content_id_or_none"] = None  # blank the content subject native_id
    with pytest.raises(ValueError, match="content subject requires a non-empty entity_key native_id"):
        build_metric_observation_record(seed_observation=seed_obs)


def test_observation_missing_source_packet_fails_closed() -> None:
    seed_document = _committed_seed_document()
    seed_obs = dict(seed_document[YOUTUBE_SEED_WRAPPER_KEY]["metric_observations"][0])
    seed_obs["source_packet_id_or_none"] = None  # remove the source anchor
    with pytest.raises(ValueError, match="lacks a source packet id"):
        build_metric_observation_record(seed_observation=seed_obs)
