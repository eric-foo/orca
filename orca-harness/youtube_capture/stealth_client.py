#!/usr/bin/env python3
"""Stealth HTTP client for the YouTube scratch capture (gitignored).

Makes the capture's network traffic resemble real Chrome (TLS + HTTP/2 + headers via curl_cffi
"impersonate") instead of stdlib Python, to reduce anti-bot detectability when capturing PUBLIC
data at volume. ANONYMOUS ONLY: a persistent Session carries anonymous cookies (CONSENT /
visitor_data) across requests; NO account login, NO po_token (no JS engine). Optional proxy is
read from env (YT_PROXY / HTTPS_PROXY) only — never hardcoded, no proxy creds in code/logs.
Falls back to plain urllib (more detectable) if curl_cffi is unavailable.

Owner-authorized: public data only, SG-legal non-criminal use, Orca source-access posture
(anti-detect/fingerprint config accepted-risk). It accesses nothing gated; a costume, not a lockpick.
Public read-only. NOT committed (under _scratch/).

Accepted residuals (Mini God Tier lens — named, not hidden):
  - po_token NOT minted -> escalate that request to a real browser (CloakBrowser) if a surface enforces it.
  - residential proxies NOT configured (single IP) -> env hook present but unused/untested.
  - first request is cookieless until the Session seeds cookies (no explicit warmup).
  - TLS/JA3 verification RUN (owner-run 2026-06-21): curl_cffi(chrome) JA3=bc54cda9.../JA4=t13d1516h2_ over HTTP/2,
    distinct from stdlib urllib JA3=a1ebe7f9.../JA4=t13d1713h1_ HTTP/1.1 -> fingerprint confirmed Chrome-class and
    coherent (Mac-Chrome UA+TLS+h2 as a set). Residual: Chrome-class, NOT proven byte-identical to a live Chrome build (version drift).
  - cannot see YouTube's actual detector -> "not blocked != undetected".
"""
import os, urllib.request

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
_PROXY = os.environ.get("YT_PROXY") or os.environ.get("HTTPS_PROXY")  # none today; residential = future

try:
    from curl_cffi import requests as _cr
    _session = _cr.Session(impersonate="chrome")
    if _PROXY:
        _session.proxies = {"http": _PROXY, "https": _PROXY}
    BACKEND = "curl_cffi:chrome" + (" +proxy" if _PROXY else "")

    def http_get(url, data=None):
        if data is not None:
            r = _session.post(url, data=data, headers={"Content-Type": "application/json"}, timeout=30)
        else:
            r = _session.get(url, timeout=30)
        return r.status_code, r.url, r.content

except Exception:  # curl_cffi missing -> degraded (more detectable) stdlib fallback
    BACKEND = "urllib_fallback"

    def http_get(url, data=None):
        h = {"User-Agent": UA, "Accept-Language": "en-US,en;q=0.9"}
        if data is not None:
            h["Content-Type"] = "application/json"
        r = urllib.request.urlopen(urllib.request.Request(url, data=data, headers=h), timeout=30)
        return r.getcode(), r.geturl(), r.read()


# Code-enforced: never run the detectable fallback silently at volume.
STEALTH_OK = BACKEND.startswith("curl_cffi")
if not STEALTH_OK:
    import sys as _sys
    print("WARNING [stealth_client]: curl_cffi unavailable -> urllib fallback; on-the-wire fingerprint is "
          "DETECTABLE as Python. Install curl_cffi before capturing at volume.", file=_sys.stderr)
