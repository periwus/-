"""유튜브 자동 업로드 (YouTube Data API v3, OAuth).

준비물: Google Cloud 콘솔에서 만든 OAuth 클라이언트(데스크톱 앱) JSON → client_secret.json
처음 한 번 브라우저로 로그인하면 token.json에 저장되어 이후엔 자동입니다.
"""
from __future__ import annotations

import json
import re
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

SCOPES = [
    "https://www.googleapis.com/auth/youtube.upload",
    "https://www.googleapis.com/auth/youtube.force-ssl",  # 댓글 작성용
]
KST = timezone(timedelta(hours=9))
CATEGORIES = {"people": "22", "howto": "26", "entertainment": "24"}


# ------------------------------------------------------------------ 인증
def get_service(client_secret: Path, token: Path):
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build

    creds = None
    if token.exists():
        creds = Credentials.from_authorized_user_file(str(token), SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not client_secret.exists():
                raise FileNotFoundError(
                    f"{client_secret} 가 없습니다. README의 '유튜브 업로드 준비'를 따라 OAuth 클라이언트 JSON을 받아 두세요.")
            flow = InstalledAppFlow.from_client_secrets_file(str(client_secret), SCOPES)
            creds = flow.run_local_server(port=0, prompt="consent")  # 브라우저가 열립니다
        token.write_text(creds.to_json(), encoding="utf-8")
    return build("youtube", "v3", credentials=creds, cache_discovery=False)


# ------------------------------------------------------------------ 메타데이터 정리
def _clean(s: str) -> str:
    return s.replace("<", "").replace(">", "")  # 유튜브는 제목/설명에 < > 금지


def build_body(meta: dict, privacy: str, publish_at: datetime | None, category: str,
               synthetic: bool, paid_promo: bool) -> dict:
    title = _clean(meta["title"]).strip()
    if "#shorts" not in title.lower() and len(title) <= 92:
        title += " #shorts"
    title = title[:100]
    desc = _clean(meta["description"]).encode("utf-8")[:4900].decode("utf-8", "ignore")
    tags, total = [], 0
    for t in meta.get("tags", []):
        t = _clean(t.lstrip("#")).strip()
        if t and total + len(t) + 1 <= 450:
            tags.append(t)
            total += len(t) + 1
    status = {
        "privacyStatus": "private" if publish_at else privacy,
        "selfDeclaredMadeForKids": False,
        "containsSyntheticMedia": synthetic,
    }
    if publish_at:
        status["publishAt"] = publish_at.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    body = {
        "snippet": {"title": title, "description": desc, "tags": tags,
                    "categoryId": CATEGORIES.get(category, category), "defaultLanguage": "ko"},
        "status": status,
    }
    if paid_promo:
        body["paidProductPlacementDetails"] = {"hasPaidProductPlacement": True}
    return body


def parse_time(s: str) -> datetime:
    """'2026-12-01 18:00' (한국시간) 또는 ISO 형식."""
    try:
        dt = datetime.fromisoformat(s)
    except ValueError:
        raise ValueError(f"시간 형식 오류: {s} (예: 2026-12-01 18:00)")
    return dt if dt.tzinfo else dt.replace(tzinfo=KST)


def parse_interval(s: str) -> timedelta:
    m = re.fullmatch(r"(\d+)\s*([hm])", s.strip().lower())
    if not m:
        raise ValueError(f"간격 형식 오류: {s} (예: 3h, 90m)")
    n = int(m.group(1))
    return timedelta(hours=n) if m.group(2) == "h" else timedelta(minutes=n)


# ------------------------------------------------------------------ 업로드
def _insert(yt, body: dict, video: Path):
    from googleapiclient.errors import HttpError
    from googleapiclient.http import MediaFileUpload

    parts = ",".join(body.keys())
    media = MediaFileUpload(str(video), mimetype="video/mp4", chunksize=8 * 1024 * 1024, resumable=True)
    req = yt.videos().insert(part=parts, body=body, media_body=media, notifySubscribers=True)
    resp, retries = None, 0
    while resp is None:
        try:
            status, resp = req.next_chunk()
            if status:
                print(f"    업로드 {int(status.progress() * 100)}%")
        except HttpError as e:
            if e.resp.status in (500, 502, 503, 504) and retries < 5:
                retries += 1
                time.sleep(2 ** retries)
                continue
            raise
    return resp


def upload_folder(yt, folder: Path, *, privacy="private", publish_at=None, category="people",
                  synthetic=False, paid_promo=None, thumbnail=False, comment=True, force=False) -> dict | None:
    from googleapiclient.errors import HttpError

    meta_file, result_file = folder / "upload.json", folder / "upload_result.json"
    if not meta_file.exists():
        print(f"  - 건너뜀(upload.json 없음): {folder}")
        return None
    if result_file.exists() and not force:
        r = json.loads(result_file.read_text(encoding="utf-8"))
        print(f"  - 이미 업로드됨: {folder.name} → https://youtu.be/{r['video_id']} (다시 올리려면 --force)")
        return {**r, "skipped": True}
    meta = json.loads(meta_file.read_text(encoding="utf-8"))
    video = folder / meta["video"]
    if paid_promo is None:
        paid_promo = bool(meta.get("affiliate"))  # 제휴 링크면 유료 광고 포함 표시

    body = build_body(meta, privacy, publish_at, category, synthetic, paid_promo)
    print(f"▲ {meta['title'][:50]} ({body['status']['privacyStatus']}"
          f"{', 예약 ' + publish_at.strftime('%m/%d %H:%M') if publish_at else ''})")
    try:
        resp = _insert(yt, body, video)
    except HttpError as e:
        if "paidProductPlacementDetails" in body and e.resp.status == 400:
            print("    ! 유료 광고 표시 필드 거부 → 빼고 다시 시도 (Studio에서 직접 체크하세요)")
            body.pop("paidProductPlacementDetails")
            paid_promo = False
            resp = _insert(yt, body, video)
        else:
            raise
    vid = resp["id"]
    result = {"video_id": vid, "url": f"https://youtu.be/{vid}", "title": body["snippet"]["title"],
              "privacy": body["status"]["privacyStatus"], "publish_at": body["status"].get("publishAt"),
              "paid_promotion_flag": paid_promo, "uploaded_at": datetime.now(KST).isoformat(timespec="seconds"),
              "comment_posted": False, "thumbnail_set": False}

    if thumbnail and (folder / "thumbnail.jpg").exists():
        try:
            from googleapiclient.http import MediaFileUpload
            yt.thumbnails().set(videoId=vid, media_body=MediaFileUpload(str(folder / "thumbnail.jpg"))).execute()
            result["thumbnail_set"] = True
        except HttpError as e:
            print(f"    ! 썸네일 설정 실패 (채널 인증 필요 등): {e.resp.status}")

    result_file.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    if comment and meta.get("pinned_comment"):
        post_comment(yt, folder)
        result = json.loads(result_file.read_text(encoding="utf-8"))
    print(f"    ✔ {result['url']}")
    return result


def post_comment(yt, folder: Path) -> bool:
    """구매 링크 댓글 작성. (API로는 '고정'이 안 되니 Studio에서 고정하세요)"""
    from googleapiclient.errors import HttpError

    result_file = folder / "upload_result.json"
    r = json.loads(result_file.read_text(encoding="utf-8"))
    if r.get("comment_posted"):
        return True
    meta = json.loads((folder / "upload.json").read_text(encoding="utf-8"))
    try:
        yt.commentThreads().insert(part="snippet", body={"snippet": {
            "videoId": r["video_id"],
            "topLevelComment": {"snippet": {"textOriginal": meta["pinned_comment"]}},
        }}).execute()
        r["comment_posted"] = True
        print("    ✔ 링크 댓글 작성 (Studio에서 '고정'을 눌러주세요)")
    except HttpError as e:
        print(f"    ! 댓글 작성 실패({e.resp.status}): 비공개·예약 영상은 공개 후 "
              f"'python upload.py {folder.parent} --comments-only' 로 다시 시도하세요")
    result_file.write_text(json.dumps(r, ensure_ascii=False, indent=2), encoding="utf-8")
    return r["comment_posted"]


def find_folders(path: Path) -> list[Path]:
    if (path / "upload.json").exists():
        return [path]
    return sorted(p.parent for p in path.glob("*/upload.json"))


# ------------------------------------------------------------------ CLI 공용 옵션
def add_args(ap):
    g = ap.add_argument_group("유튜브 업로드")
    g.add_argument("--privacy", choices=["private", "unlisted", "public"], default="private",
                   help="공개 범위 (기본: private 비공개)")
    g.add_argument("--publish-at", help="예약 공개 시각, 한국시간 (예: '2026-12-01 18:00')")
    g.add_argument("--interval", default="3h", help="여러 개 예약 시 간격 (기본 3h)")
    g.add_argument("--category", default="people", help="people | howto | entertainment | 카테고리 ID")
    g.add_argument("--synthetic", action="store_true", help="'변경되거나 합성된 콘텐츠' 표시")
    g.add_argument("--no-paid-promo", action="store_true", help="제휴 링크여도 '유료 광고 포함' 표시 안 함")
    g.add_argument("--thumbnail", action="store_true", help="썸네일도 업로드 (채널 인증 필요)")
    g.add_argument("--no-comment", action="store_true", help="링크 댓글 작성 안 함")
    g.add_argument("--force", action="store_true", help="이미 올린 영상도 다시 업로드")
    g.add_argument("--client-secret", type=Path, default=Path("client_secret.json"))
    g.add_argument("--token", type=Path, default=Path("token.json"))


def upload_many(folders: list[Path], a) -> tuple[int, int]:
    """(새로 올린 수, 실패 수)를 반환. 이미 올린 폴더는 건너뛴다."""
    yt = get_service(a.client_secret, a.token)
    when = parse_time(a.publish_at) if a.publish_at else None
    if when and when < datetime.now(KST) + timedelta(minutes=15):
        raise ValueError("예약 시각은 지금부터 15분 이후여야 합니다.")
    step = parse_interval(a.interval)
    ok = fail = 0
    for f in folders:
        try:
            r = upload_folder(yt, f, privacy=a.privacy, publish_at=when, category=a.category,
                              synthetic=a.synthetic, paid_promo=False if a.no_paid_promo else None,
                              thumbnail=a.thumbnail, comment=not a.no_comment, force=a.force)
            if r and not r.get("skipped"):
                ok += 1
                if when and r.get("publish_at"):
                    when += step
        except Exception as e:
            fail += 1
            print(f"  ✘ {f.name}: {e}")
            if "quota" in str(e).lower():
                print("  ! 일일 할당량 초과 → 내일 다시 실행하면 남은 것만 올라갑니다.")
                break
    return ok, fail
