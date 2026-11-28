"""상품 1개 → 쇼츠 1편 (영상, 썸네일, 대본, 업로드 문구)."""
from __future__ import annotations

import json
import re
from pathlib import Path

from PIL import Image

from . import render, tts
from .product import Product
from .script import Script, make_script

COUPANG_NOTICE = "이 포스팅은 쿠팡 파트너스 활동의 일환으로, 이에 따른 일정액의 수수료를 제공받습니다."


def slug(s: str) -> str:
    s = re.sub(r"[^\w가-힣]+", "_", s).strip("_")
    return s[:40] or "product"


def pinned_comment(p: Product) -> str:
    pin = f"👉 {p.name} 구매 링크: {p.link}" if p.link else f"👉 {p.name} 정보는 프로필 링크에서!"
    if p.is_affiliate:
        pin += f"\n({COUPANG_NOTICE})"
    return pin


def full_description(p: Product, s: Script) -> str:
    lines = [s.description.strip()]
    if p.link:
        lines += ["", f"👉 구매 링크: {p.link}"]
    if p.is_affiliate:
        lines += ["", COUPANG_NOTICE]
    lines += ["", " ".join(s.hashtags)]
    return "\n".join(lines)


def upload_meta(p: Product, s: Script, video: Path) -> dict:
    """upload.py가 읽는 업로드 정보."""
    return {"title": s.title, "description": full_description(p, s), "tags": s.hashtags,
            "pinned_comment": pinned_comment(p), "affiliate": p.is_affiliate,
            "video": video.name, "thumbnail": "thumbnail.jpg"}


def upload_text(p: Product, s: Script) -> str:
    desc = s.description.strip()
    lines = [f"[제목]\n{s.title}", "", "[설명]", desc]
    if p.link:
        lines += ["", f"👉 구매 링크: {p.link}"]
    if p.is_affiliate:
        lines += ["", COUPANG_NOTICE]
    lines += ["", " ".join(s.hashtags), "", "[고정 댓글]"]
    pin = f"👉 {p.name} 구매 링크: {p.link}" if p.link else f"👉 {p.name} 정보는 프로필 링크에서!"
    if p.is_affiliate:
        pin += f"\n({COUPANG_NOTICE})"
    lines.append(pin)
    return "\n".join(lines) + "\n"


def make_short(p: Product, out_root: Path, font: str, *, ai="auto", model="claude-opus-5-5", style="",
               voice="sunhi", rate="+12%", tts_engine="edge", bgm: Path | None = None,
               bgm_volume=0.12, script_file: Path | None = None, clip_volume: float = 0.0) -> Path:
    out = out_root / slug(p.name)
    work = out / "work"
    work.mkdir(parents=True, exist_ok=True)
    print(f"▶ {p.name}")

    # 1) 대본 (기존 script.json을 고쳐 다시 렌더링할 수도 있음)
    if script_file and script_file.exists():
        script, src = Script.from_dict(json.loads(script_file.read_text(encoding="utf-8"))), "file"
    else:
        script, src = make_script(p, ai, model, style)
    (out / "script.json").write_text(json.dumps(script.to_dict(), ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"  · 대본: {src}, 장면 {len(script.scenes)}개")

    # 2) 이미지
    media = render.fetch_media(p.images, p.clips, work)
    badge_text = None
    dr = p.discount_rate()
    if dr:
        badge_text = f"{dr}% 할인 중"

    parts, total, voiced = [], 0.0, True
    for i, sc in enumerate(script.scenes):
        m = media[sc.image % len(media)]
        canvas = work / f"canvas_{sc.image % len(media)}.png"
        if m.kind == "image" and not canvas.exists():
            render.scene_canvas(m.image).save(canvas)

        # 자막 레이어
        layer = Image.new("RGBA", (render.W, render.H), (0, 0, 0, 0))
        if sc.kind == "hook":
            layer.alpha_composite(render.caption_png(sc.caption, font, 96, 1430))
        elif sc.kind == "price":
            layer.alpha_composite(render.caption_png(sc.caption, font, 104, 1450))
        else:
            layer.alpha_composite(render.caption_png(sc.caption, font, 78, 1480))
        if badge_text and sc.kind != "hook":
            layer.alpha_composite(render.badge_png(badge_text, font))
        ov = work / f"overlay_{i}.png"
        layer.save(ov)

        # 음성
        audio, dur, ok = tts.synth(sc.narration, work / f"voice_{i}.mp3", voice, rate, tts_engine)
        voiced &= ok
        dur += 0.25  # 장면 사이 숨 고르기
        part = work / f"scene_{i}.mp4"
        if m.kind == "video":
            render.render_clip_scene(m, ov, audio, dur, part, clip_volume)
        else:
            render.render_scene(canvas, ov, audio, dur, part, zoom_in=(i % 2 == 0), idx=i)
        parts.append(part)
        total += dur
        print(f"  · 장면 {i + 1}/{len(script.scenes)} [{sc.kind}] {dur:.1f}s")

    video = out / f"{slug(p.name)}.mp4"
    render.concat(parts, video, bgm, bgm_volume)

    # 썸네일
    thumb = render.scene_canvas(media[0].frame(), scale=1).convert("RGBA")
    first = script.scenes[0].caption
    thumb.alpha_composite(render.caption_png(first, font, 116, 1560))
    thumb.convert("RGB").save(out / "thumbnail.jpg", quality=92)

    (out / "upload.txt").write_text(upload_text(p, script), encoding="utf-8")
    (out / "upload.json").write_text(json.dumps(upload_meta(p, script, video), ensure_ascii=False, indent=2),
                                     encoding="utf-8")
    print(f"  ✔ {video}  ({total:.1f}초{'' if voiced else ', 무음: TTS 연결 실패'})")
    if total > 60:
        print("  ! 60초를 넘었습니다. 쇼츠는 짧을수록 유리하니 기능 수를 줄여보세요.")
    return video
