from __future__ import annotations

import json
from pathlib import Path

import pytest

from runners.run_edgar_headcount import (
    EdgarHeadcountRunFailure,
    main,
    run_edgar_headcount_capture,
    run_edgar_headcount_history_capture,
)
from source_capture.adapters.direct_http import DirectHttpCaptureSuccess
from source_capture.company_aggregate.observation_log import read_observation_log

UA = "Orca research probe (research@orca.local)"

SUBMISSIONS = {
    "cik": 320193,
    "filings": {
        "recent": {
            "form": ["10-Q", "10-K", "8-K"],
            "accessionNumber": ["acc-q", "0000320193-23-000106", "acc-8k"],
            "primaryDocument": ["q.htm", "aapl-20230930.htm", "8k.htm"],
            "reportDate": ["2023-06-30", "2023-09-30", "2023-10-01"],
            "filingDate": ["2023-07-15", "2023-11-03", "2023-10-20"],
        },
        "files": [],
    },
}
FILING_HTML = b"<html>... As of fiscal year-end we had approximately 161,000 full-time employees ...</html>"

NO_10K = {
    "filings": {
        "recent": {
            "form": ["10-Q"],
            "accessionNumber": ["q"],
            "primaryDocument": ["q.htm"],
            "reportDate": ["2023-06-30"],
            "filingDate": ["2023-07-15"],
        },
        "files": [],
    }
}


def _ok(url: str, body: bytes) -> DirectHttpCaptureSuccess:
    return DirectHttpCaptureSuccess(
        requested_url=url, final_url=url, status=200, reason="OK",
        metadata={"status": 200, "byte_count": len(body)}, body=body, warning_notes=[], limitation_notes=[],
    )


class _StubFetch:
    """Dispatches on URL: the submissions API returns JSON, the Archives doc returns the filing."""

    def __init__(self, submissions: dict = SUBMISSIONS, filing_html: bytes = FILING_HTML) -> None:
        self.submissions = submissions
        self.filing_html = filing_html
        self.calls: list[str] = []

    def __call__(self, *, url, timeout_seconds, max_bytes, user_agent):
        self.calls.append(url)
        if "data.sec.gov/submissions" in url:
            return _ok(url, json.dumps(self.submissions).encode("utf-8"))
        return _ok(url, self.filing_html)


def _run(tmp_path: Path, *, fetch: _StubFetch, packet_suffix: str = ""):
    return run_edgar_headcount_capture(
        cik="320193",
        user_agent=UA,
        packet_output_directory=tmp_path / f"pkt{packet_suffix}",
        observation_log_path=tmp_path / "obs_log.yaml",
        decision_question="beauty net-adds backtest",
        fetch=fetch,
    )


def test_end_to_end_discovers_captures_derives_and_projects(tmp_path):
    stub = _StubFetch()
    result = _run(tmp_path, fetch=stub)

    # discovery supplied the real filing_date + period (closing the capture-adapter gap)
    assert result.discovery.filing_date == "2023-11-03"
    assert result.discovery.period_of_report == "2023-09-30"

    # the observation carries the discovered filing_date, not a sentinel
    assert result.observation.employee_count_int == 161000
    assert result.observation.filing_date == "2023-11-03"

    # the projection is a filer-level UNRESOLVED trend with one point
    assert len(result.projections) == 1
    projection = result.projections[0]
    assert projection.resolution_state == "unresolved"
    assert projection.entity_key is None
    assert projection.provisional_filer_key == "sec_edgar:CIK0000320193"
    assert [p.employee_count_int for p in projection.points] == [161000]

    # it actually went to the submissions API first, then the Archives document
    assert any("data.sec.gov/submissions" in url for url in stub.calls)
    assert any("www.sec.gov/Archives" in url for url in stub.calls)

    # the observation was persisted append-only
    assert len(read_observation_log(tmp_path / "obs_log.yaml")) == 1


def test_second_run_appends_to_the_log_and_collapses_identical(tmp_path):
    _run(tmp_path, fetch=_StubFetch(), packet_suffix="1")
    result = _run(tmp_path, fetch=_StubFetch(), packet_suffix="2")
    # two readings of the same filing now in the log -> collapse to one point with two refs
    assert len(read_observation_log(tmp_path / "obs_log.yaml")) == 2
    point = result.projections[0].points[0]
    assert point.point_state == "single"
    assert len(point.observation_refs) == 2


def test_discovery_failure_raises_run_failure(tmp_path):
    with pytest.raises(EdgarHeadcountRunFailure) as excinfo:
        _run(tmp_path, fetch=_StubFetch(submissions=NO_10K))
    assert excinfo.value.code == "discovery_failed"


# ---- multi-period history capture: the organizational-movement series (offline) ----

SUBMISSIONS_MULTIYEAR = {
    "filings": {
        "recent": {
            "form": ["10-K", "10-Q", "10-K", "10-K"],
            "accessionNumber": ["acc-2021", "acc-q", "acc-2023", "acc-2022"],
            "primaryDocument": ["fy2021.htm", "q.htm", "fy2023.htm", "fy2022.htm"],
            "reportDate": ["2021-09-25", "2023-06-30", "2023-09-30", "2022-09-24"],
            "filingDate": ["2021-10-29", "2023-07-15", "2023-11-03", "2022-10-28"],
        },
        "files": [],
    },
}
# one distinct headcount per fiscal year -> a real trend the projection must surface in order
FILINGS_BY_DOC = {
    "fy2021.htm": b"<html>... As of fiscal year-end we had approximately 154,000 full-time employees ...</html>",
    "fy2022.htm": b"<html>... As of fiscal year-end we had approximately 164,000 full-time employees ...</html>",
    "fy2023.htm": b"<html>... As of fiscal year-end we had approximately 161,000 full-time employees ...</html>",
}


class _MultiYearStubFetch:
    """Submissions URL -> the multi-year JSON; each Archives doc URL -> that year's filing body."""

    def __init__(self) -> None:
        self.calls: list[str] = []

    def __call__(self, *, url, timeout_seconds, max_bytes, user_agent):
        self.calls.append(url)
        if "data.sec.gov/submissions" in url:
            return _ok(url, json.dumps(SUBMISSIONS_MULTIYEAR).encode("utf-8"))
        for doc, body in FILINGS_BY_DOC.items():
            if doc in url:
                return _ok(url, body)
        raise AssertionError(f"unexpected fetch url: {url}")


def test_history_capture_yields_multi_year_movement_series(tmp_path):
    stub = _MultiYearStubFetch()
    result = run_edgar_headcount_history_capture(
        cik="320193",
        user_agent=UA,
        packet_output_directory=tmp_path / "pkts",
        observation_log_path=tmp_path / "log.yaml",
        decision_question="organizational movement: headcount trajectory",
        fetch=stub,
    )

    # three 10-Ks captured (the 10-Q ignored); each its own packet, all appended to one log
    assert len(result.observations) == 3
    assert len(read_observation_log(tmp_path / "log.yaml")) == 3
    assert len({d for d in result.packet_output_directories}) == 3  # no packet collisions

    # the projection is a single filer-level UNRESOLVED lane with an ordered, multi-point trend
    assert len(result.projections) == 1
    projection = result.projections[0]
    assert projection.resolution_state == "unresolved"
    assert projection.entity_key is None
    points = projection.points
    assert [p.period_of_report for p in points] == ["2021-09-25", "2022-09-24", "2023-09-30"]
    # the movement signal: 154k -> 164k -> 161k, oldest to newest
    assert [p.employee_count_int for p in points] == [154000, 164000, 161000]


def test_history_capture_limit_keeps_most_recent(tmp_path):
    result = run_edgar_headcount_history_capture(
        cik="320193",
        user_agent=UA,
        packet_output_directory=tmp_path / "pkts",
        observation_log_path=tmp_path / "log.yaml",
        decision_question="organizational movement",
        limit=2,
        fetch=_MultiYearStubFetch(),
    )
    points = result.projections[0].points
    # only the two most recent fiscal years captured
    assert [p.period_of_report for p in points] == ["2022-09-24", "2023-09-30"]
    assert [p.employee_count_int for p in points] == [164000, 161000]


def test_history_capture_no_10k_raises(tmp_path):
    with pytest.raises(EdgarHeadcountRunFailure) as excinfo:
        run_edgar_headcount_history_capture(
            cik="320193",
            user_agent=UA,
            packet_output_directory=tmp_path / "pkts",
            observation_log_path=tmp_path / "log.yaml",
            decision_question="organizational movement",
            fetch=_StubFetch(submissions=NO_10K),
        )
    assert excinfo.value.code == "discovery_failed"


# ---- the CLI exit-code convention (offline, stubbed transport) ----

def _argv(tmp_path: Path) -> list[str]:
    return [
        "--cik", "320193",
        "--user-agent", UA,
        "--packet-output-directory", str(tmp_path / "pkt"),
        "--observation-log", str(tmp_path / "log.yaml"),
        "--decision-question", "beauty net-adds backtest",
    ]


def test_main_exit_0_on_success(tmp_path):
    assert main(_argv(tmp_path), fetch=_StubFetch()) == 0
    assert (tmp_path / "pkt" / "manifest.json").exists()
    assert (tmp_path / "log.yaml").exists()


def test_main_exit_3_on_discovery_failure(tmp_path):
    assert main(_argv(tmp_path), fetch=_StubFetch(submissions=NO_10K)) == 3


def test_main_exit_2_on_bad_cik(tmp_path):
    argv = _argv(tmp_path)
    argv[argv.index("--cik") + 1] = "not-a-cik"
    with pytest.raises(SystemExit) as excinfo:
        main(argv, fetch=_StubFetch())
    assert excinfo.value.code == 2
