"""한글 폰트 찾기. 없으면 Google Fonts(OFL)에서 자동 다운로드."""
from __future__ import annotations

import os
from pathlib import Path

import requests

CACHE_DIR = Path(os.environ.get("SHORTS_CACHE", Path.home() / ".cache" / "product-shorts"))

# 굵은 디스플레이 폰트(쇼츠 자막용). OFL 라이선스로 상업적 사용 가능.
DOWNLOADS = {
    "BlackHanSans-Regular.ttf": "https://raw.githubusercontent.com/google/fonts/main/ofl/blackhansans/BlackHanSans-Regular.ttf",
}

SYSTEM_CANDIDATES = [
    "C:/Windows/Fonts/malgunbd.ttf",                      # Windows 맑은 고딕 Bold
    "/System/Library/Fonts/AppleSDGothicNeo.ttc",         # macOS
    "/usr/share/fonts/truetype/nanum/NanumGothicExtraBold.ttf",
    "/usr/share/fonts/truetype/nanum/NanumGothicBold.ttf",
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Black.ttc",
]


def _download(name: str, url: str) -> Path | None:
    dest = CACHE_DIR / name
    if dest.exists() and dest.stat().st_size > 10_000:
        return dest
    try:
        CACHE_DIR.mkdir(parents=True, exist_ok=True)
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        if not r.content[:4] in (b"\x00\x01\x00\x00", b"OTTO", b"true", b"ttcf"):
            return None
        dest.write_bytes(r.content)
        return dest
    except Exception:
        return None


def find_font(user_font: str | None = None) -> str:
    if user_font:
        if not Path(user_font).exists():
            raise FileNotFoundError(f"폰트 파일이 없습니다: {user_font}")
        return user_font
    for name, url in DOWNLOADS.items():
        p = _download(name, url)
        if p:
            return str(p)
    for c in SYSTEM_CANDIDATES:
        if Path(c).exists():
            return c
    raise RuntimeError("한글 폰트를 찾지 못했습니다. --font 로 .ttf 경로를 지정하세요.")
