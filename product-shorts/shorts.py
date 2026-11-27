#!/usr/bin/env python3
"""상품쇼츠 자동 생성기

예)
  python shorts.py examples/product.json
  python shorts.py examples/products.csv --bgm music.mp3
  python shorts.py --url "https://상품페이지" --name "이름 덮어쓰기"
  python shorts.py examples/product.json --script output/xxx/script.json   # 대본 수정 후 재렌더
  python shorts.py examples/products.csv --upload --publish-at "2026-12-01 18:00"  # 만들고 예약 업로드
"""
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

from shortsmaker import fonts, youtube
from shortsmaker.pipeline import make_short
from shortsmaker.product import from_url, load_products


def main():
    ap = argparse.ArgumentParser(description="상품 정보로 9:16 쇼츠 영상을 자동 생성")
    ap.add_argument("input", nargs="?", help="상품 JSON 또는 CSV 파일")
    ap.add_argument("--url", help="상품 페이지 URL (og 태그로 이름·이미지·가격 추출)")
    ap.add_argument("--name", help="상품명 덮어쓰기 (--url과 함께)")
    ap.add_argument("--features", help="기능 목록, | 로 구분 (--url과 함께)")
    ap.add_argument("--link", help="제휴/구매 링크 덮어쓰기")
    ap.add_argument("-o", "--out", default="output", help="결과 폴더 (기본: output)")
    ap.add_argument("--ai", choices=["auto", "on", "off"], default="auto",
                    help="Claude 대본 사용 (auto: API 키 있으면 사용)")
    ap.add_argument("--model", default="claude-opus-5-5")
    ap.add_argument("--style", default="", help="대본 추가 요청 (예: '20대 말투, 유머러스하게')")
    ap.add_argument("--voice", default="sunhi", help="sunhi | injoon | hyunsu | edge-tts 음성 이름")
    ap.add_argument("--rate", default="+12%", help="말하기 속도 (예: +20%%)")
    ap.add_argument("--tts", choices=["edge", "none"], default="edge", help="none이면 무음(테스트용)")
    ap.add_argument("--bgm", type=Path, help="배경음악 파일 (저작권 free 음원 권장)")
    ap.add_argument("--bgm-volume", type=float, default=0.12)
    ap.add_argument("--font", help="자막 폰트 .ttf 경로")
    ap.add_argument("--script", type=Path, help="수정한 script.json으로 다시 렌더링")
    ap.add_argument("--upload", action="store_true", help="만든 뒤 바로 유튜브에 업로드 (upload.py와 같은 옵션)")
    youtube.add_args(ap)
    a = ap.parse_args()

    if not shutil.which("ffmpeg"):
        sys.exit("ffmpeg가 필요합니다. https://ffmpeg.org 에서 설치 후 PATH에 추가하세요.")

    if a.url:
        p = from_url(a.url)
        if a.name:
            p.name = a.name
        if a.features:
            p.features = [f.strip() for f in a.features.split("|") if f.strip()]
        products = [p]
    elif a.input:
        products = load_products(a.input)
    else:
        ap.error("상품 파일 또는 --url 이 필요합니다.")
    if a.link:
        for p in products:
            p.link = a.link

    font = fonts.find_font(a.font)
    out = Path(a.out)
    done, failed = [], []
    for p in products:
        try:
            done.append(make_short(
                p, out, font, ai=a.ai, model=a.model, style=a.style, voice=a.voice, rate=a.rate,
                tts_engine=a.tts, bgm=a.bgm, bgm_volume=a.bgm_volume,
                script_file=a.script if len(products) == 1 else None,
            ))
        except Exception as e:
            print(f"  ✘ {p.name}: {e}")
            failed.append(p.name)
    print(f"\n완료 {len(done)}개, 실패 {len(failed)}개 → {out.resolve()}")
    if a.upload and done:
        try:
            ok, fail = youtube.upload_many([v.parent for v in done], a)
            print(f"업로드 {ok}개, 실패 {fail}개")
        except (ValueError, FileNotFoundError) as e:
            sys.exit(f"업로드 오류: {e}\n(영상은 만들어졌으니 문제를 고친 뒤 'python upload.py {out}' 로 올리면 됩니다)")
    sys.exit(1 if failed and not done else 0)


if __name__ == "__main__":
    main()
