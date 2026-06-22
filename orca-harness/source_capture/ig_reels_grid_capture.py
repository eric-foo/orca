"""Live browser capture for IG public `/reels/` grid observations.

The parser in ``ig_reels_grid`` stays pure and network-free. This module owns
the bounded browser substrate needed by the optimized runner: one public reels
page load, no hover/click/item fan-out, DOM media-anchor extraction, and passive
JSON response preservation.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass, field
from importlib import import_module
from pathlib import Path
from typing import TypeAlias
from urllib.parse import urlparse

from harness_utils import utc_now_z
from source_capture.ig_reels_grid import (
    CLIPS_USER_JSON_METADATA,
    PROFILE_FEED_JSON_METADATA,
    WEB_PROFILE_INFO_JSON_METADATA,
    source_surface_from_url_or_path,
)
from source_capture.proxy_profiles import ProxyProfile

DEFAULT_IG_REELS_VIEWPORT_WIDTH = 1080
DEFAULT_IG_REELS_VIEWPORT_HEIGHT = 1920
DEFAULT_IG_REELS_SETTLE_SECONDS = 2.5
DEFAULT_IG_REELS_TIMEOUT_SECONDS = 25.0
DEFAULT_IG_REELS_MAX_RESPONSE_BYTES = 5_000_000

_PRESERVED_RESPONSE_SURFACES = {
    CLIPS_USER_JSON_METADATA,
    WEB_PROFILE_INFO_JSON_METADATA,
    PROFILE_FEED_JSON_METADATA,
}
_HEAVY_RESOURCE_TYPES = {"image", "media", "font"}


@dataclass(frozen=True)
class IgReelsGridPassiveResponse:
    source_surface: str
    requested_url: str
    final_url: str
    status: int
    ok: bool
    body_text: str
    response_headers: dict[str, str]
    limitation_notes: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


@dataclass(frozen=True)
class IgReelsGridCaptureSuccess:
    requested_url: str
    final_url: str
    title: str | None
    visible_text: str
    dom_rows: list[dict[str, object]]
    passive_json_responses: list[IgReelsGridPassiveResponse]
    metadata: dict[str, object]
    warning_notes: list[str] = field(default_factory=list)
    limitation_notes: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class IgReelsGridCaptureFailure:
    requested_url: str
    failure_kind: str
    message: str
    final_url: str | None = None


IgReelsGridCaptureResult: TypeAlias = IgReelsGridCaptureSuccess | IgReelsGridCaptureFailure


def fetch_ig_reels_grid_capture(
    *,
    reels_url: str,
    profile_handle: str,
    timeout_seconds: float = DEFAULT_IG_REELS_TIMEOUT_SECONDS,
    viewport_width: int = DEFAULT_IG_REELS_VIEWPORT_WIDTH,
    viewport_height: int = DEFAULT_IG_REELS_VIEWPORT_HEIGHT,
    settle_seconds: float = DEFAULT_IG_REELS_SETTLE_SECONDS,
    max_response_bytes: int = DEFAULT_IG_REELS_MAX_RESPONSE_BYTES,
    max_rows: int = 12,
    block_heavy_assets: bool = True,
    proxy_profile: ProxyProfile | None = None,
    storage_state_path: Path | None = None,
    headless: bool = True,
    browser_channel: str | None = None,
) -> IgReelsGridCaptureResult:
    """Capture one bounded IG reels-grid page load.

    ``block_heavy_assets`` is a bandwidth control, not a stealth claim. It aborts
    images, media, and fonts only; scripts/XHR are left intact because they carry
    the observable page and JSON metadata.
    """

    try:
        sync_api = import_module("playwright.sync_api")
    except ModuleNotFoundError as exc:
        return IgReelsGridCaptureFailure(
            requested_url=reels_url,
            failure_kind="dependency_unavailable",
            message=(
                "Playwright is not installed. Install the browser optional dependency before "
                "running IG reels-grid capture."
            ),
        )

    timeout_ms = timeout_seconds * 1000
    started_at = utc_now_z()
    selected_responses: list[object] = []

    try:
        with sync_api.sync_playwright() as playwright:
            launch_kwargs: dict[str, object] = {}
            if proxy_profile is not None:
                launch_kwargs["proxy"] = _playwright_proxy_settings(proxy_profile)
            if browser_channel is not None:
                launch_kwargs["channel"] = browser_channel
            browser = playwright.chromium.launch(headless=headless, **launch_kwargs)
            try:
                context_kwargs: dict[str, object] = {
                    "viewport": {
                        "width": viewport_width,
                        "height": viewport_height,
                    }
                }
                if storage_state_path is not None:
                    context_kwargs["storage_state"] = str(storage_state_path)
                if proxy_profile is not None and proxy_profile.timezone is not None:
                    context_kwargs["timezone_id"] = proxy_profile.timezone
                if proxy_profile is not None and proxy_profile.locale is not None:
                    context_kwargs["locale"] = proxy_profile.locale
                context = browser.new_context(**context_kwargs)
                try:
                    page = context.new_page()
                    if block_heavy_assets:
                        page.route(
                            "**/*",
                            lambda route: route.abort()
                            if route.request.resource_type in _HEAVY_RESOURCE_TYPES
                            else route.continue_(),
                        )

                    page.on(
                        "response",
                        lambda response: selected_responses.append(response)
                        if _should_preserve_response(response.url)
                        else None,
                    )
                    page.goto(reels_url, wait_until="load", timeout=timeout_ms)
                    if settle_seconds > 0:
                        page.wait_for_timeout(settle_seconds * 1000)
                    try:
                        page.wait_for_selector('a[href*="/reel/"], a[href*="/p/"]', timeout=5000)
                    except Exception:
                        pass

                    visible_text = ""
                    warning_notes: list[str] = []
                    try:
                        visible_text = page.locator("body").inner_text(timeout=timeout_ms)
                    except Exception as exc:
                        warning_notes.append(f"ig_reels_grid visible_text extraction failed: {exc}")
                    dom_rows = page.evaluate(
                        _DOM_ROW_EXTRACT_SCRIPT,
                        {"profileHandle": profile_handle, "maxRows": max_rows},
                    )
                    passive_json_responses = _read_passive_responses(
                        selected_responses,
                        max_response_bytes=max_response_bytes,
                    )
                    final_url = page.url
                    title = page.title()
                    metadata = {
                        "requested_url": reels_url,
                        "final_url": final_url,
                        "capture_timestamp": started_at,
                        "timeout_seconds": timeout_seconds,
                        "settle_seconds": settle_seconds,
                        "headless": headless,
                        "browser_channel": browser_channel,
                        "viewport_width": viewport_width,
                        "viewport_height": viewport_height,
                        "storage_state_loaded": storage_state_path is not None,
                        "block_heavy_assets": block_heavy_assets,
                        "max_rows": max_rows,
                        "dom_row_count": len(dom_rows),
                        "passive_json_response_count": len(passive_json_responses),
                        **_proxy_metadata(proxy_profile),
                    }
                    if final_url != reels_url:
                        warning_notes.append(
                            f"ig_reels_grid landed at {final_url} from requested URL {reels_url}"
                        )
                    limitation_notes = [
                        note
                        for response in passive_json_responses
                        for note in response.limitation_notes
                    ]
                    return IgReelsGridCaptureSuccess(
                        requested_url=reels_url,
                        final_url=final_url,
                        title=title,
                        visible_text=visible_text,
                        dom_rows=dom_rows,
                        passive_json_responses=passive_json_responses,
                        metadata=metadata,
                        warning_notes=warning_notes,
                        limitation_notes=limitation_notes,
                    )
                finally:
                    context.close()
            finally:
                browser.close()
    except Exception as exc:  # noqa: BLE001 - failures are surfaced as capture artifacts.
        return IgReelsGridCaptureFailure(
            requested_url=reels_url,
            final_url=None,
            failure_kind="capture_failed",
            message=_capture_failure_message(exc, proxy_profile=proxy_profile),
        )


def _should_preserve_response(url: str) -> bool:
    return source_surface_from_url_or_path(url) in _PRESERVED_RESPONSE_SURFACES


def _read_passive_responses(
    responses: list[object],
    *,
    max_response_bytes: int,
) -> list[IgReelsGridPassiveResponse]:
    preserved: list[IgReelsGridPassiveResponse] = []
    seen: set[tuple[str, int]] = set()
    for response in responses:
        url = str(response.url)
        surface = source_surface_from_url_or_path(url)
        status = int(response.status)
        identity = (url, status)
        if identity in seen:
            continue
        seen.add(identity)
        headers = {
            str(key): str(value)
            for key, value in response.headers.items()
            if str(key).lower() not in {"set-cookie", "cookie"}
        }
        limitations: list[str] = []
        body_text = ""
        try:
            candidate = response.text()
        except Exception as exc:
            limitations.append(f"passive_json_body_unavailable: {type(exc).__name__}: {exc}")
        else:
            size = len(candidate.encode("utf-8"))
            if size > max_response_bytes:
                limitations.append(
                    f"passive_json_body_exceeded_cap: {size} > {max_response_bytes}; body omitted"
                )
            else:
                body_text = candidate
        preserved.append(
            IgReelsGridPassiveResponse(
                source_surface=surface,
                requested_url=url,
                final_url=str(response.url),
                status=status,
                ok=bool(response.ok),
                body_text=body_text,
                response_headers=headers,
                limitation_notes=limitations,
            )
        )
    return preserved


def _playwright_proxy_settings(proxy_profile: ProxyProfile) -> dict[str, str]:
    # Importing the generic adapter would expose a private helper; keep this copy
    # narrow and redacted at every packet boundary.
    from urllib.parse import unquote, urlunparse

    endpoint = proxy_profile.proxy_endpoint
    parsed = urlparse(endpoint)
    if not parsed.scheme or not parsed.hostname:
        return {"server": endpoint}

    host = parsed.hostname
    if ":" in host and not host.startswith("["):
        host = f"[{host}]"
    netloc = f"{host}:{parsed.port}" if parsed.port is not None else host
    server = urlunparse((parsed.scheme, netloc, "", "", "", ""))
    settings = {"server": server}
    if parsed.username is not None:
        settings["username"] = unquote(parsed.username)
    if parsed.password is not None:
        settings["password"] = unquote(parsed.password)
    return settings


def _proxy_metadata(proxy_profile: ProxyProfile | None) -> dict[str, object]:
    return {
        "proxy_used": proxy_profile is not None,
        "proxy_category": proxy_profile.proxy_category.value if proxy_profile is not None else None,
        "proxy_disclosure": "category_only" if proxy_profile is not None else "none",
        "proxy_endpoint_recorded": False,
        "proxy_exit_ip_recorded": False,
        "proxy_timezone": proxy_profile.timezone if proxy_profile is not None else None,
        "proxy_locale": proxy_profile.locale if proxy_profile is not None else None,
    }


def _capture_failure_message(error: Exception, *, proxy_profile: ProxyProfile | None) -> str:
    text = f"IG reels-grid capture failed: {type(error).__name__}: {error}"
    if proxy_profile is None:
        return text
    endpoint = proxy_profile.proxy_endpoint
    redacted = text.replace(endpoint, "[redacted-proxy-endpoint]")
    parsed = urlparse(endpoint)
    if parsed.username:
        redacted = redacted.replace(parsed.username, "[redacted-proxy-credential]")
    if parsed.password:
        redacted = redacted.replace(parsed.password, "[redacted-proxy-credential]")
    if parsed.hostname:
        redacted = redacted.replace(parsed.hostname, "[redacted-proxy-endpoint]")
    return redacted


_DOM_ROW_EXTRACT_SCRIPT = r"""
({profileHandle, maxRows}) => {
  const numericPattern = /^\d[\d,.]*(?:[KMB])?$/i;
  const numericFindPattern = /\d[\d,.]*(?:[KMB])?/gi;

  function numericTexts(text) {
    if (!text) return [];
    const values = text.match(numericFindPattern) || [];
    return values.filter((value) => numericPattern.test(value));
  }

  function leafNumericTexts(root) {
    const out = [];
    const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
    while (walker.nextNode()) {
      const text = (walker.currentNode.nodeValue || "").trim();
      if (numericPattern.test(text)) {
        out.push({ text });
      }
    }
    return out;
  }

  function pathFromHref(href) {
    try {
      return new URL(href, window.location.href).pathname;
    } catch (_error) {
      return href || "";
    }
  }

  function isMediaPath(path) {
    return path.includes("/reel/") || path.includes("/p/");
  }

  const handle = (profileHandle || "").toLowerCase();
  const rows = [];
  const seen = new Set();
  const anchors = Array.from(document.querySelectorAll("a[href]"));
  for (const anchor of anchors) {
    const href = anchor.href || anchor.getAttribute("href") || "";
    const path = pathFromHref(href);
    if (!isMediaPath(path)) continue;
    const parts = path.split("/").filter(Boolean);
    if (handle && parts[0] && !["p", "reel"].includes(parts[0]) && parts[0].toLowerCase() !== handle) {
      continue;
    }
    const rect = anchor.getBoundingClientRect();
    if (rect.width <= 0 || rect.height <= 0) continue;
    if (rect.bottom < 0 || rect.top > window.innerHeight) continue;
    const identity = path.replace(/\/$/, "");
    if (seen.has(identity)) continue;
    seen.add(identity);
    const visibleText = anchor.innerText || "";
    rows.push({
      href,
      path,
      visibleText,
      visibleNumericTexts: numericTexts(visibleText),
      leafNumericTexts: leafNumericTexts(anchor),
      rect: {
        x: rect.x,
        y: rect.y,
        width: rect.width,
        height: rect.height,
      },
    });
    if (rows.length >= maxRows) break;
  }
  return rows;
}
"""


__all__ = [
    "DEFAULT_IG_REELS_MAX_RESPONSE_BYTES",
    "DEFAULT_IG_REELS_SETTLE_SECONDS",
    "DEFAULT_IG_REELS_TIMEOUT_SECONDS",
    "DEFAULT_IG_REELS_VIEWPORT_HEIGHT",
    "DEFAULT_IG_REELS_VIEWPORT_WIDTH",
    "IgReelsGridCaptureFailure",
    "IgReelsGridCaptureResult",
    "IgReelsGridCaptureSuccess",
    "IgReelsGridPassiveResponse",
    "fetch_ig_reels_grid_capture",
]
