#!/usr/bin/env python3
"""유튜브 채널 아이콘·배너 만들기 (쇼츠 영상과 같은 폰트·색으로 통일)

  python branding/make_branding.py
  python branding/make_branding.py --name "살림픽" --slogan "1만원대 생활 꿀템, 30초면 끝" --sub "매일 저녁 7시 새 쇼츠"
"""
import argparse
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from shortsmaker.fonts import find_font  # noqa: E402

YELLOW = (255, 212, 0)
NAVY = (22, 27, 45)
NAVY2 = (36, 44, 72)
WHITE = (255, 255, 255)
RED = (255, 59, 48)


def fit_font(path, text, max_w, max_h, start=400):
    size = start
    while size > 10:
        f = ImageFont.truetype(path, size)
        l, t, r, b = f.getbbox(text)
        if r - l <= max_w and b - t <= max_h:
            return f
        size -= 4
    return ImageFont.truetype(path, 10)


def draw_center(d, cx, cy, text, font, fill, stroke=0, stroke_fill=None):
    l, t, r, b = font.getbbox(text)
    d.text((cx - (r - l) / 2 - l, cy - (b - t) / 2 - t), text, font=font, fill=fill,
           stroke_width=stroke, stroke_fill=stroke_fill)


def bag(d, cx, cy, s, color, check=NAVY):
    """쇼핑백 + 체크 표시 아이콘 (s = 가방 폭)."""
    w, h = s, s * 0.9
    x0, y0 = cx - w / 2, cy - h / 2 + s * 0.12
    d.arc([cx - s * 0.22, y0 - s * 0.28, cx + s * 0.22, y0 + s * 0.16], 180, 360, fill=color, width=int(s * 0.07))
    d.rounded_rectangle([x0, y0, x0 + w, y0 + h], radius=int(s * 0.12), fill=color)
    lw = int(s * 0.09)
    pts = [(cx - s * 0.2, y0 + h * 0.52), (cx - s * 0.04, y0 + h * 0.68), (cx + s * 0.24, y0 + h * 0.34)]
    d.line(pts, fill=check, width=lw, joint="curve")
    for p in (pts[0], pts[-1]):
        d.ellipse([p[0] - lw / 2, p[1] - lw / 2, p[0] + lw / 2, p[1] + lw / 2], fill=check)


def make_icon(name, font_path, out: Path, size=800):
    im = Image.new("RGB", (size, size), YELLOW)
    d = ImageDraw.Draw(im)
    # 원형으로 잘려 보이므로 중요한 요소는 가운데 70% 안에
    bag(d, size / 2, size * 0.36, size * 0.34, NAVY, check=YELLOW)
    f = fit_font(font_path, name, size * 0.66, size * 0.2, 220)
    draw_center(d, size / 2, size * 0.72, name, f, NAVY)
    im.save(out, quality=95)
    # 원형 미리보기
    prev = im.copy().convert("RGBA")
    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).ellipse([0, 0, size, size], fill=255)
    prev.putalpha(mask)
    prev.save(out.with_name(out.stem + "_preview_circle.png"))


def make_banner(name, slogan, sub, font_path, out: Path):
    W, H = 2560, 1440
    SW, SH = 1546, 423   # 모든 기기에서 보이는 안전 영역 (가운데)
    im = Image.new("RGB", (W, H), NAVY)
    d = ImageDraw.Draw(im)
    # TV·PC에서만 보이는 바깥 영역: 은은한 패턴
    for i in range(-H, W, 120):
        d.line([(i, 0), (i + H, H)], fill=NAVY2, width=28)
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(glow).ellipse([W / 2 - 900, H / 2 - 320, W / 2 + 900, H / 2 + 320], fill=(255, 212, 0, 40))
    im.paste(glow.filter(ImageFilter.GaussianBlur(120)), (0, 0), glow.filter(ImageFilter.GaussianBlur(120)))
    d = ImageDraw.Draw(im)

    x0, y0 = (W - SW) / 2, (H - SH) / 2
    # 왼쪽: 아이콘 배지
    bs = SH * 0.78
    bx, by = x0 + bs / 2 + 10, H / 2
    d.rounded_rectangle([bx - bs / 2, by - bs / 2, bx + bs / 2, by + bs / 2], radius=int(bs * 0.22), fill=YELLOW)
    bag(d, bx, by - bs * 0.04, bs * 0.5, NAVY, check=YELLOW)
    # 오른쪽: 이름 / 슬로건 / 업로드 안내
    tx = bx + bs / 2 + 60
    tw = x0 + SW - tx
    fn = fit_font(font_path, name, tw, SH * 0.42, 260)
    l, t, r, b = fn.getbbox(name)
    d.text((tx - l, y0 + 18 - t), name, font=fn, fill=YELLOW)
    fs = fit_font(font_path, slogan, tw, SH * 0.2, 90)
    l2, t2, r2, b2 = fs.getbbox(slogan)
    ys = y0 + 18 + (b - t) + 34
    d.text((tx - l2, ys - t2), slogan, font=fs, fill=WHITE)
    if sub:
        fsub = ImageFont.truetype(font_path, 50)
        l3, t3, r3, b3 = fsub.getbbox(sub)
        yb = ys + (b2 - t2) + 34
        d.rounded_rectangle([tx, yb, tx + (r3 - l3) + 56, yb + (b3 - t3) + 34], radius=40, fill=RED)
        d.text((tx + 28 - l3, yb + 17 - t3), sub, font=fsub, fill=WHITE)
    im.save(out, quality=92)
    # 안전 영역 확인용
    chk = im.copy()
    ImageDraw.Draw(chk).rectangle([x0, y0, x0 + SW, y0 + SH], outline=(0, 255, 120), width=6)
    chk.resize((1280, 720)).save(out.with_name(out.stem + "_safe_area_check.png"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--name", default="살림픽")
    ap.add_argument("--slogan", default="1만원대 생활 꿀템, 30초면 끝")
    ap.add_argument("--sub", default="매일 저녁 7시 새 쇼츠")
    ap.add_argument("--font")
    ap.add_argument("-o", "--out", default=str(Path(__file__).resolve().parent / "output"))
    a = ap.parse_args()
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    font = find_font(a.font)
    make_icon(a.name, font, out / "channel_icon_800.png")
    make_banner(a.name, a.slogan, a.sub, font, out / "channel_banner_2560x1440.jpg")
    print(f"완료 → {out}")


if __name__ == "__main__":
    main()
