#!/usr/bin/env python3
"""만들어 둔 쇼츠를 유튜브에 올린다.

  python upload.py output                          # output 안의 안 올린 영상 전부 (비공개)
  python upload.py output/상품폴더 --privacy public
  python upload.py output --publish-at "2026-12-01 18:00" --interval 3h   # 3시간 간격 예약
  python upload.py output --comments-only          # 공개된 뒤 링크 댓글만 달기
"""
import argparse
import sys
from pathlib import Path

from shortsmaker import youtube


def main():
    ap = argparse.ArgumentParser(description="쇼츠 유튜브 업로드")
    ap.add_argument("path", type=Path, help="output 폴더 또는 상품 폴더")
    ap.add_argument("--comments-only", action="store_true", help="업로드된 영상에 못 단 링크 댓글만 작성")
    youtube.add_args(ap)
    a = ap.parse_args()

    folders = youtube.find_folders(a.path)
    if not folders:
        sys.exit(f"{a.path} 에 upload.json이 있는 폴더가 없습니다. 먼저 shorts.py로 영상을 만드세요.")

    if a.comments_only:
        try:
            yt = youtube.get_service(a.client_secret, a.token)
        except FileNotFoundError as e:
            sys.exit(f"오류: {e}")
        for f in folders:
            if (f / "upload_result.json").exists():
                youtube.post_comment(yt, f)
        return

    try:
        ok, fail = youtube.upload_many(folders, a)
    except (ValueError, FileNotFoundError) as e:
        sys.exit(f"오류: {e}")
    print(f"\n업로드 {ok}개, 실패 {fail}개")
    sys.exit(1 if fail and not ok else 0)


if __name__ == "__main__":
    main()
