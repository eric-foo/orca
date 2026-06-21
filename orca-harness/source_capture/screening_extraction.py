from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from html.parser import HTMLParser
from urllib.parse import urlparse


@dataclass(frozen=True)
class OldRedditThreadCandidate:
    thread_url: str
    subreddit: str
    title: str | None
    source_anchor_class: str
    submission_datetime: str | None
    submission_datetime_state: str
    submission_datetime_detail: str | None = None

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


def extract_screening_fields(
    *,
    url: str,
    body_text: str,
    old_reddit_submission_min_datetime: str | None = None,
    old_reddit_submission_max_datetime: str | None = None,
) -> dict[str, object]:
    """Return bounded screen-light extraction fields from already-read text.

    This intentionally returns only locator-style fields. It never returns raw
    HTML, comment bodies, post bodies, author/profile fields, packet metadata, or
    ECR/Cleaning/Judgment data.
    """
    fields: dict[str, object] = {
        "comments_marker_count": body_text.count("/comments/"),
    }
    if _looks_like_old_reddit_listing_or_search(url):
        candidates = extract_old_reddit_thread_candidates(
            body_text=body_text,
            submission_min_datetime=old_reddit_submission_min_datetime,
            submission_max_datetime=old_reddit_submission_max_datetime,
        )
        fields["old_reddit_thread_candidates"] = [candidate.to_dict() for candidate in candidates]
        fields["old_reddit_thread_candidate_count"] = len(candidates)
    return fields


def extract_old_reddit_thread_candidates(
    *,
    body_text: str,
    submission_min_datetime: str | None = None,
    submission_max_datetime: str | None = None,
) -> list[OldRedditThreadCandidate]:
    min_dt = _parse_optional_iso_datetime(submission_min_datetime)
    max_dt = _parse_optional_iso_datetime(submission_max_datetime)
    parser = _OldRedditThreadCandidateParser(submission_min_datetime=min_dt, submission_max_datetime=max_dt)
    parser.feed(body_text)
    parser.close()
    return parser.candidates


class _OldRedditThreadCandidateParser(HTMLParser):
    _VOID_TAGS = {
        "area",
        "base",
        "br",
        "col",
        "embed",
        "hr",
        "img",
        "input",
        "link",
        "meta",
        "param",
        "source",
        "track",
        "wbr",
    }

    def __init__(
        self,
        *,
        submission_min_datetime: datetime | None,
        submission_max_datetime: datetime | None,
    ) -> None:
        super().__init__(convert_charrefs=True)
        self.submission_min_datetime = submission_min_datetime
        self.submission_max_datetime = submission_max_datetime
        self.candidates: list[OldRedditThreadCandidate] = []
        self._seen_urls: set[str] = set()
        self._container_depth = 0
        self._container_href: str | None = None
        self._container_title: str | None = None
        self._container_anchor_class: str | None = None
        self._container_datetime: str | None = None
        self._current_anchor_href: str | None = None
        self._current_anchor_class: str | None = None
        self._current_anchor_parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr_map = {key: value or "" for key, value in attrs}
        class_tokens = set(attr_map.get("class", "").split())

        if self._container_depth:
            if tag not in self._VOID_TAGS:
                self._container_depth += 1
        elif tag in {"div", "article"} and _is_old_reddit_result_container(class_tokens):
            self._container_depth = 1
            self._container_href = None
            self._container_title = None
            self._container_anchor_class = None
            self._container_datetime = None

        if tag == "a":
            href = attr_map.get("href", "")
            anchor_class = _candidate_anchor_class(class_tokens)
            if anchor_class is not None and "/comments/" in href:
                self._current_anchor_href = href
                self._current_anchor_class = anchor_class
                self._current_anchor_parts = []
                return

        if tag == "time" and self._container_depth and self._container_datetime is None:
            if _is_submission_time_locator(class_tokens):
                datetime_value = attr_map.get("datetime", "").strip()
                if datetime_value:
                    self._container_datetime = datetime_value

    def handle_data(self, data: str) -> None:
        if self._current_anchor_href is not None:
            self._current_anchor_parts.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "a" and self._current_anchor_href is not None:
            title = " ".join("".join(self._current_anchor_parts).split()) or None
            if self._container_depth:
                self._container_href = self._current_anchor_href
                self._container_title = title
                self._container_anchor_class = self._current_anchor_class
            else:
                self._append_candidate(
                    href=self._current_anchor_href,
                    title=title,
                    anchor_class=self._current_anchor_class or "unknown",
                    submission_datetime=None,
                )
            self._current_anchor_href = None
            self._current_anchor_class = None
            self._current_anchor_parts = []
            return

        if self._container_depth and tag not in self._VOID_TAGS:
            self._container_depth -= 1
            if self._container_depth == 0:
                if self._container_href is not None:
                    self._append_candidate(
                        href=self._container_href,
                        title=self._container_title,
                        anchor_class=self._container_anchor_class or "unknown",
                        submission_datetime=self._container_datetime,
                    )
                self._container_href = None
                self._container_title = None
                self._container_anchor_class = None
                self._container_datetime = None

    def _append_candidate(
        self,
        *,
        href: str,
        title: str | None,
        anchor_class: str,
        submission_datetime: str | None,
    ) -> None:
        thread_url = _canonical_old_reddit_thread_url(href)
        if thread_url is None or thread_url in self._seen_urls:
            return
        subreddit = _subreddit_from_thread_url(thread_url)
        if subreddit is None:
            return

        state, normalized, detail = _classify_submission_datetime(
            submission_datetime,
            min_datetime=self.submission_min_datetime,
            max_datetime=self.submission_max_datetime,
        )
        self.candidates.append(
            OldRedditThreadCandidate(
                thread_url=thread_url,
                subreddit=subreddit,
                title=title,
                source_anchor_class=anchor_class,
                submission_datetime=normalized,
                submission_datetime_state=state,
                submission_datetime_detail=detail,
            )
        )
        self._seen_urls.add(thread_url)


def _is_old_reddit_result_container(class_tokens: set[str]) -> bool:
    return "thing" in class_tokens or "search-result" in class_tokens


def _candidate_anchor_class(class_tokens: set[str]) -> str | None:
    if "search-title" in class_tokens:
        return "search-title"
    if "title" in class_tokens:
        return "title"
    return None


def _is_submission_time_locator(class_tokens: set[str]) -> bool:
    return not class_tokens or "live-timestamp" in class_tokens


def _canonical_old_reddit_thread_url(href: str) -> str | None:
    stripped = href.strip()
    if stripped.startswith("/r/"):
        stripped = f"https://old.reddit.com{stripped}"
    if stripped.startswith("https://www.reddit.com/r/"):
        stripped = "https://old.reddit.com/r/" + stripped.split("https://www.reddit.com/r/", 1)[1]
    if not stripped.startswith("https://old.reddit.com/r/"):
        return None
    stripped = stripped.split("#", 1)[0].split("?", 1)[0]
    if "/comments/" not in stripped:
        return None
    if not stripped.endswith("/"):
        stripped += "/"
    return stripped


def _subreddit_from_thread_url(url: str) -> str | None:
    parsed = urlparse(url)
    parts = parsed.path.split("/")
    if len(parts) < 3 or parts[1] != "r" or not parts[2]:
        return None
    subreddit = parts[2]
    if not subreddit.replace("_", "").isalnum():
        return None
    return subreddit


def _looks_like_old_reddit_listing_or_search(url: str) -> bool:
    parsed = urlparse(url)
    host = (parsed.hostname or "").lower()
    if host not in {"old.reddit.com", "www.reddit.com"}:
        return False
    path = (parsed.path or "").rstrip("/")
    if "/comments/" in path:
        return False
    return path.startswith("/r/")


def _classify_submission_datetime(
    value: str | None,
    *,
    min_datetime: datetime | None,
    max_datetime: datetime | None,
) -> tuple[str, str | None, str | None]:
    if value is None:
        return "unknown_absent", None, "no targeted listing time element was found for this row"
    parsed = _parse_optional_iso_datetime(value)
    if parsed is None:
        return "invalid", None, f"could not parse submission datetime {value!r}"
    if min_datetime is not None and parsed < min_datetime:
        return (
            "out_of_range",
            _format_utc(parsed),
            f"submission datetime is before range minimum {_format_utc(min_datetime)}",
        )
    if max_datetime is not None and parsed > max_datetime:
        return (
            "out_of_range",
            _format_utc(parsed),
            f"submission datetime is after range maximum {_format_utc(max_datetime)}",
        )
    return "known", _format_utc(parsed), None


def _parse_optional_iso_datetime(value: str | None) -> datetime | None:
    if not value:
        return None
    text = value.strip()
    if text.endswith("Z"):
        text = f"{text[:-1]}+00:00"
    try:
        parsed = datetime.fromisoformat(text)
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=UTC)
    return parsed.astimezone(UTC).replace(microsecond=0)


def _format_utc(value: datetime) -> str:
    return value.astimezone(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


__all__ = [
    "OldRedditThreadCandidate",
    "extract_old_reddit_thread_candidates",
    "extract_screening_fields",
]
