"""Shared CLI helpers for YouTube capture runners."""
from __future__ import annotations

import re
from typing import Sequence

_YOUTUBE_VIDEO_ID = re.compile(r"[A-Za-z0-9_-]{11}")


def normalize_video_id_argv(argv: Sequence[str]) -> list[str]:
    """Allow ``--video-id -abc...`` without hiding ordinary argparse errors."""
    normalized: list[str] = []
    index = 0
    while index < len(argv):
        token = argv[index]
        if token == "--video-id" and index + 1 < len(argv):
            value = argv[index + 1]
            if value.startswith("-") and _YOUTUBE_VIDEO_ID.fullmatch(value):
                normalized.append(f"--video-id={value}")
                index += 2
                continue
        normalized.append(token)
        index += 1
    return normalized
