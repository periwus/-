"""나레이션 음성. edge-tts(무료 MS 한국어 음성) 사용, 실패 시 무음으로 대체."""
from __future__ import annotations

import asyncio
import os
import re
import subprocess
from pathlib import Path

VOICES = {
    "sunhi": "ko-KR-SunHiNeural",     # 여성, 밝음 (기본)
    "injoon": "ko-KR-InJoonNeural",   # 남성
    "hyunsu": "ko-KR-HyunsuMultilingualNeural",
}


def probe_duration(path: Path) -> float:
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)],
        capture_output=True, text=True, check=True,
    ).stdout.strip()
    return float(out)


def _clean(text: str) -> str:
    text = re.sub(r"[*~]+", "", text)
    return text.replace("✔", "").replace("👇", "").strip()


async def _edge(text: str, voice: str, rate: str, out: Path):
    import edge_tts

    proxy = os.environ.get("HTTPS_PROXY") or os.environ.get("https_proxy")
    comm = edge_tts.Communicate(text, voice, rate=rate, proxy=proxy)
    await comm.save(str(out))


def silent(duration: float, out: Path) -> Path:
    subprocess.run(
        ["ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo",
         "-t", f"{duration:.2f}", "-c:a", "libmp3lame", "-q:a", "6", str(out)],
        check=True,
    )
    return out


_EDGE_DOWN = False


def synth(text: str, out: Path, voice: str = "sunhi", rate: str = "+12%", engine: str = "edge") -> tuple[Path, float, bool]:
    """음성 파일을 만들고 (경로, 길이초, 실제음성여부)를 반환."""
    global _EDGE_DOWN
    text = _clean(text)
    if engine == "edge" and not _EDGE_DOWN:
        try:
            asyncio.run(_edge(text, VOICES.get(voice, voice), rate, out))
            if out.exists() and out.stat().st_size > 1000:
                return out, probe_duration(out), True
        except Exception as e:
            _EDGE_DOWN = True  # 한 번 실패하면 이후 장면은 바로 무음 처리
            print(f"  ! TTS 연결 실패 → 이후 무음으로 대체 ({type(e).__name__}: {e})")
    # 무음 대체: 글자 수로 읽는 시간 추정 (약 7자/초)
    dur = max(1.8, len(text) / 7.0 + 0.4)
    return silent(dur, out), dur, False
