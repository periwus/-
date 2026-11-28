"""9:16 영상 렌더링 (Pillow로 장면 그림, ffmpeg로 줌·합성·인코딩)."""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
from dataclasses import dataclass
from io import BytesIO
from pathlib import Path

import requests
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps

W, H, FPS = 1080, 1920, 30
YELLOW = (255, 226, 38)
WHITE = (255, 255, 255)
GRAY = (190, 190, 190)


# ------------------------------------------------------------------ 이미지 준비
def fetch_images(srcs: list[str], work: Path, allow_empty: bool = False) -> list[Image.Image]:
    imgs = []
    for s in srcs:
        try:
            if s.startswith("http"):
                r = requests.get(s, timeout=30, headers={"User-Agent": "Mozilla/5.0"})
                r.raise_for_status()
                im = Image.open(BytesIO(r.content))
            else:
                im = Image.open(s)
            imgs.append(ImageOps.exif_transpose(im).convert("RGB"))
        except Exception as e:
            print(f"  ! 이미지 불러오기 실패: {s} ({e})")
    if not imgs and not allow_empty:
        imgs = [_placeholder()]
    return imgs


@dataclass
class Media:
    kind: str                      # "image" | "video"
    image: Image.Image | None = None
    path: Path | None = None       # video
    duration: float = 0.0
    width: int = 0
    height: int = 0
    has_audio: bool = False
    cursor: float = 0.0            # 다음 장면이 이어서 쓸 위치(초)

    def frame(self) -> Image.Image:
        """썸네일·미리보기용 대표 이미지."""
        if self.kind == "image":
            return self.image
        t = min(1.0, self.duration / 3)
        r = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t:.2f}", "-i", str(self.path), "-frames:v", "1",
                            "-f", "image2pipe", "-vcodec", "png", "-"], capture_output=True)
        return Image.open(BytesIO(r.stdout)).convert("RGB") if r.stdout else _placeholder()


def probe_video(path: Path) -> dict:
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                          "stream=codec_type,width,height:stream_tags=rotate:stream_side_data=rotation:format=duration",
                          "-of", "json", str(path)], capture_output=True, text=True, check=True).stdout
    info = json.loads(out)
    v = next((st for st in info.get("streams", []) if st.get("codec_type") == "video"), None)
    if not v:
        raise ValueError("영상 스트림이 없습니다")
    w, h = v.get("width", 0), v.get("height", 0)
    rot = abs(int(float(v.get("tags", {}).get("rotate", 0) or
                        next((d.get("rotation", 0) for d in v.get("side_data_list", [])), 0) or 0)))
    if rot in (90, 270):  # 휴대폰 세로 촬영 영상
        w, h = h, w
    return {"w": w, "h": h, "duration": float(info["format"]["duration"]),
            "audio": any(st.get("codec_type") == "audio" for st in info["streams"])}


def fetch_media(images: list[str], clips: list[str], work: Path) -> list[Media]:
    out: list[Media] = []
    for i, c in enumerate(clips):
        try:
            path = Path(c)
            if c.startswith("http"):
                path = work / f"clip_{i}{Path(c.split('?')[0]).suffix or '.mp4'}"
                if not path.exists():
                    with requests.get(c, timeout=60, stream=True, headers={"User-Agent": "Mozilla/5.0"}) as r:
                        r.raise_for_status()
                        with path.open("wb") as f:
                            for chunk in r.iter_content(1 << 20):
                                f.write(chunk)
            info = probe_video(path)
            if info["duration"] < 0.5:
                raise ValueError("너무 짧은 영상")
            out.append(Media("video", path=path, duration=info["duration"], width=info["w"],
                             height=info["h"], has_audio=info["audio"]))
        except Exception as e:
            print(f"  ! 클립 불러오기 실패: {c} ({e})")
    out += [Media("image", image=im) for im in fetch_images(images, work, allow_empty=bool(out))]
    return out or [Media("image", image=_placeholder())]


def _placeholder() -> Image.Image:
    im = Image.new("RGB", (1000, 1000), (40, 40, 48))
    ImageDraw.Draw(im).rectangle([200, 200, 800, 800], outline=(120, 120, 130), width=12)
    return im


def _cover(im: Image.Image, w: int, h: int) -> Image.Image:
    return ImageOps.fit(im, (w, h), Image.LANCZOS)


def scene_canvas(im: Image.Image, scale: int = 2) -> Image.Image:
    """흐린 배경 + 가운데 상품 이미지. 줌 연출을 위해 2배 크기로 만든다."""
    cw, ch = W * scale, H * scale
    bg = _cover(im, cw // 8, ch // 8).filter(ImageFilter.GaussianBlur(6)).resize((cw, ch), Image.LANCZOS)
    bg = Image.blend(bg, Image.new("RGB", bg.size, (0, 0, 0)), 0.45)
    r = min(cw * 0.90 / im.width, ch * 0.55 / im.height)   # 작은 이미지도 확대
    fg = im.resize((int(im.width * r), int(im.height * r)), Image.LANCZOS)
    x = (cw - fg.width) // 2
    y = int(ch * 0.40) - fg.height // 2
    shadow = Image.new("RGBA", (fg.width + 80, fg.height + 80), (0, 0, 0, 0))
    ImageDraw.Draw(shadow).rounded_rectangle([40, 40, fg.width + 40, fg.height + 40], 30, fill=(0, 0, 0, 150))
    bg.paste(shadow.filter(ImageFilter.GaussianBlur(25)), (x - 40, y - 20), shadow.filter(ImageFilter.GaussianBlur(25)))
    mask = Image.new("L", fg.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, fg.width, fg.height], 36, fill=255)
    bg.paste(fg, (x, y), mask)
    return bg


# ------------------------------------------------------------------ 자막 그리기
TOKEN = re.compile(r"(\*\*.+?\*\*|~~.+?~~)")


def _segments(line: str):
    for part in TOKEN.split(line):
        if not part:
            continue
        if part.startswith("**"):
            yield part[2:-2], YELLOW, False
        elif part.startswith("~~"):
            yield part[2:-2], GRAY, True
        else:
            yield part, WHITE, False


def _wrap(text: str, font: ImageFont.FreeTypeFont, max_w: int) -> list[str]:
    """강조 마커를 유지하면서 폭에 맞게 줄바꿈 (한글은 글자 단위)."""
    out = []
    for para in text.split("\n"):
        plain_len = lambda s: font.getlength(TOKEN.sub(lambda m: m.group(0)[2:-2], s))
        words, line = para.split(" "), ""
        for w in words:
            cand = (line + " " + w).strip()
            if plain_len(cand) <= max_w:
                line = cand
                continue
            if line:
                out.append(line)
            line = w
            while plain_len(line) > max_w:  # 아주 긴 단어는 강제로 자름
                cut = len(line)
                while cut > 1 and plain_len(line[:cut]) > max_w:
                    cut -= 1
                out.append(line[:cut])
                line = line[cut:]
        out.append(line)
    # 줄을 넘어간 강조 마커 보정
    fixed, carry = [], None
    for ln in out:
        if carry:
            ln = carry + ln
            carry = None
        for mk in ("**", "~~"):
            if ln.count(mk) % 2:
                ln += mk
                carry = mk
        fixed.append(ln)
    return [l for l in fixed if TOKEN.sub("", l).strip() or TOKEN.search(l)]


# 자막 폰트에 없을 수 있는 기호/이모지는 지운다 (빈 네모 방지)
_ALLOWED = re.compile(r"[^0-9A-Za-z가-힣ㄱ-ㅎㅏ-ㅣ\s.,!?%~*()+\-:'\"/&#·…]")


def clean_caption(text: str) -> str:
    text = text.replace("↓", " 할인 ").replace("→", " ")
    text = _ALLOWED.sub("", text)
    return re.sub(r"[ \t]+", " ", text).strip()


def caption_png(text: str, font_path: str, size: int, y_center: int, box: bool = True) -> Image.Image:
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    font = ImageFont.truetype(font_path, size)
    text = clean_caption(text)
    lines = _wrap(text, font, W - 140)
    lh = int(size * 1.28)
    total = lh * len(lines)
    y = y_center - total // 2
    d = ImageDraw.Draw(layer)
    if box and lines:
        widths = [font.getlength("".join(s for s, _, _ in _segments(l))) for l in lines]
        bw = max(widths) + 80
        d.rounded_rectangle([(W - bw) / 2, y - 30, (W + bw) / 2, y + total + 20], 28, fill=(0, 0, 0, 150))
    stroke = max(4, size // 12)
    for ln in lines:
        segs = list(_segments(ln))
        lw = sum(font.getlength(s) for s, _, _ in segs)
        x = (W - lw) / 2
        for s, color, strike in segs:
            d.text((x, y), s, font=font, fill=color, stroke_width=stroke, stroke_fill=(0, 0, 0))
            sw = font.getlength(s)
            if strike:
                my = y + size * 0.6
                d.line([x, my, x + sw, my], fill=(255, 70, 70), width=max(4, size // 14))
            x += sw
        y += lh
    return layer


def badge_png(text: str, font_path: str) -> Image.Image:
    """상단 고정 배지 (예: 상품명/할인율)."""
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    font = ImageFont.truetype(font_path, 54)
    tw = font.getlength(text)
    d = ImageDraw.Draw(layer)
    x0 = (W - tw) / 2 - 36
    d.rounded_rectangle([x0, 150, x0 + tw + 72, 250], 50, fill=(255, 59, 48, 235))
    d.text(((W - tw) / 2, 164), text, font=font, fill=WHITE)
    return layer


# ------------------------------------------------------------------ ffmpeg
def run(cmd: list[str]):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError("ffmpeg 실패:\n" + r.stderr[-2000:])


def render_scene(canvas: Path, overlay: Path, audio: Path, dur: float, out: Path, zoom_in: bool, idx: int):
    frames = max(1, int(dur * FPS))
    if zoom_in:
        z = f"min(1+0.10*on/{frames},1.10)"
    else:
        z = f"max(1.10-0.10*on/{frames},1.0)"
    vf = (
        f"[0:v]zoompan=z='{z}':d={frames}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
        f":s={W}x{H}:fps={FPS},format=yuv420p[bg];"
        f"[1:v]format=rgba,fade=t=in:st=0:d=0.15:alpha=1[ov];"
        f"[bg][ov]overlay=0:0:shortest=1,format=yuv420p[v]"
    )
    run([
        "ffmpeg", "-y", "-loglevel", "error",
        "-loop", "1", "-framerate", str(FPS), "-i", str(canvas),
        "-loop", "1", "-framerate", str(FPS), "-i", str(overlay),
        "-i", str(audio),
        "-filter_complex", vf, "-map", "[v]", "-map", "2:a",
        "-t", f"{dur:.3f}", "-r", str(FPS),
        "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "160k", "-ar", "44100", "-ac", "2",
        str(out),
    ])


def render_clip_scene(m: Media, overlay: Path, audio: Path, dur: float, out: Path, clip_volume: float = 0.0):
    """영상 클립 장면. 세로 영상은 화면을 꽉 채우고, 가로·정사각 영상은 흐린 배경 위에 얹는다.
    같은 클립을 여러 장면에서 쓰면 앞 장면이 끝난 지점부터 이어서 보여준다(끝나면 처음으로)."""
    start = m.cursor if m.cursor + 0.3 < m.duration else 0.0
    m.cursor = (start + dur) % m.duration
    vertical = m.height and m.width / m.height <= 0.7
    if vertical:
        v = (f"[0:v]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},"
             f"setsar=1,fps={FPS},format=yuv420p[bg];")
    else:
        fg_h = int(H * 0.55)
        v = (f"[0:v]fps={FPS},split[a][b];"
             f"[a]scale={W // 4}:{H // 4}:force_original_aspect_ratio=increase,crop={W // 4}:{H // 4},"
             f"boxblur=8:2,scale={W}:{H},eq=brightness=-0.18,setsar=1[blur];"
             f"[b]scale={W - 40}:{fg_h}:force_original_aspect_ratio=decrease,setsar=1[fg];"
             f"[blur][fg]overlay=(W-w)/2:{int(H * 0.40)}-h/2,format=yuv420p[bg];")
    v += "[1:v]format=rgba,fade=t=in:st=0:d=0.15:alpha=1[ov];[bg][ov]overlay=0:0:shortest=1,format=yuv420p[v]"
    if clip_volume > 0 and m.has_audio:
        a = (f";[0:a]volume={clip_volume},aformat=sample_rates=44100:channel_layouts=stereo[ca];"
             f"[2:a]aformat=sample_rates=44100:channel_layouts=stereo[na];"
             f"[na][ca]amix=inputs=2:duration=first:dropout_transition=0,volume=2[a]")
        amap = "[a]"
    else:
        a, amap = "", "2:a"
    run([
        "ffmpeg", "-y", "-loglevel", "error",
        "-stream_loop", "-1", "-ss", f"{start:.3f}", "-i", str(m.path),
        "-loop", "1", "-framerate", str(FPS), "-i", str(overlay),
        "-i", str(audio),
        "-filter_complex", v + a, "-map", "[v]", "-map", amap,
        "-t", f"{dur:.3f}", "-r", str(FPS),
        "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "160k", "-ar", "44100", "-ac", "2",
        str(out),
    ])


def concat(parts: list[Path], out: Path, bgm: Path | None, bgm_volume: float):
    lst = out.with_suffix(".txt")
    lst.write_text("".join(f"file '{p.resolve()}'\n" for p in parts), encoding="utf-8")
    joined = out.with_name(out.stem + "_nobgm.mp4")
    run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy", str(joined)])
    if not bgm:
        joined.replace(out)
        return
    run([
        "ffmpeg", "-y", "-loglevel", "error", "-i", str(joined), "-stream_loop", "-1", "-i", str(bgm),
        "-filter_complex",
        f"[1:a]volume={bgm_volume},aformat=sample_rates=44100:channel_layouts=stereo[m];"
        f"[0:a][m]amix=inputs=2:duration=first:dropout_transition=0,volume=2[a]",
        "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", str(out),
    ])
    joined.unlink(missing_ok=True)


def cache_key(*parts) -> str:
    return hashlib.md5("|".join(map(str, parts)).encode()).hexdigest()[:10]
