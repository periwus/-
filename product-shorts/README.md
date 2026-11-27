# 상품쇼츠 자동화 (product-shorts)

상품 정보(JSON/CSV/상품 URL)만 넣으면 **9:16 세로 쇼츠 영상 + 썸네일 + 업로드 문구**를 한 번에 만들어 주는 프로그램입니다.
쿠팡파트너스·스마트스토어 상품 홍보 쇼츠를 여러 개 연속으로 뽑는 용도입니다.

```
상품 정보 → ① 대본(후킹→불편→기능→가격→CTA) → ② AI 음성(무료) → ③ 이미지 줌 + 자막 합성 → ④ mp4 / 썸네일 / 업로드 문구
```

## 참고한 오픈소스

| 프로젝트 | 가져온 아이디어 |
|---|---|
| [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) (★14만+, MIT) | 대본 → edge-tts 음성 → 자막 → 영상 합성 파이프라인 구조, 무료 edge-tts 사용 |
| 쿠팡파트너스 쇼핑쇼츠 노하우 글들 | 첫 3초 후킹, 1080×1920 규격, 자막 + CTA, 파트너스 고지 문구 |

코드는 상품쇼츠에 맞게 새로 작성했습니다. 스톡 영상 대신 **상품 사진에 줌 연출**을 넣고, **가격, 할인율(취소선), 할인 배지**를 강조합니다.

## 설치

1. Python 3.10 이상
2. **ffmpeg** 설치 후 PATH에 등록
   - Windows: `winget install ffmpeg`
   - macOS: `brew install ffmpeg`
3. 패키지 설치
   ```bash
   pip install -r requirements.txt
   ```
처음 실행할 때 자막 폰트(Black Han Sans, OFL 무료 라이선스)를 자동으로 내려받습니다.

## 사용법

```bash
# 1) 상품 1개 (JSON)
python shorts.py examples/product.json

# 2) 여러 상품 한 번에 (CSV, 한 줄에 상품 하나)
python shorts.py examples/products.csv

# 3) 상품 페이지 URL로 (og 태그에서 이름·이미지·가격 자동 추출)
python shorts.py --url "https://상품페이지주소" --features "기능1|기능2|기능3" --link "https://link.coupang.com/a/xxxx"

# 배경음악, 남자 목소리, 빠르게
python shorts.py examples/product.json --bgm music.mp3 --voice injoon --rate "+20%"
```

결과는 `output/<상품명>/` 폴더에 생깁니다.

| 파일 | 내용 |
|---|---|
| `<상품명>.mp4` | 1080×1920, 30fps 완성 영상 (보통 25~40초) |
| `thumbnail.jpg` | 후킹 문구가 들어간 썸네일 |
| `upload.txt` | 제목, 설명, 해시태그, 고정 댓글 (쿠팡 링크면 **파트너스 고지 문구 자동 삽입**) |
| `upload.json` | 유튜브 자동 업로드에 쓰는 정보 |
| `script.json` | 장면별 대본. 고친 뒤 `--script`로 다시 렌더링할 수 있습니다 |

### 대본 고쳐서 다시 만들기
```bash
# output/.../script.json 의 narration(읽는 말)과 caption(자막)을 고친 뒤
python shorts.py examples/product.json --script output/뿌리는_욕실_물때_클리너_500ml/script.json
```
자막에서 `**강조**`는 노란색, `~~15,900원~~`은 취소선으로 표시됩니다.

## 상품 입력 형식

```json
{
  "name": "뿌리는 욕실 물때 클리너 500ml",
  "price": "9,900",
  "original_price": "15,900",          // 넣으면 할인율 배지와 취소선 가격이 자동으로 들어갑니다
  "features": ["뿌리고 10분 두면 물때가 녹아요", "솔질 없이 물로 헹구기만"],
  "images": ["images/1.jpg", "https://.../2.jpg"],
  "link": "https://link.coupang.com/a/xxxx",
  "pain": "욕실 물때 청소",            // 후킹·공감 장면에 쓰입니다
  "target": "자취생",
  "cta": "고정댓글 링크에서 확인하세요"
}
```
CSV에서는 `features`와 `images`를 `|`로 구분합니다 (`examples/products.csv` 참고).

## AI 대본 (선택)

`ANTHROPIC_API_KEY` 환경변수가 있으면 Claude가 상품에 맞춰 대본, 제목, 해시태그를 씁니다. 없으면 내장 템플릿(후킹 문구 5종 랜덤)으로 만듭니다.

```bash
export ANTHROPIC_API_KEY=sk-ant-...     # Windows: set ANTHROPIC_API_KEY=...
python shorts.py examples/product.json --style "20대 친구한테 말하듯, 유머 있게"
```
- `--ai off`: 항상 템플릿 사용, `--ai on`: Claude만 사용 (실패하면 중단)
- 프롬프트에 "상품 정보에 없는 효능이나 후기를 지어내지 말 것", "과장 광고 표현 금지"가 들어 있습니다.

## 옵션 전체

| 옵션 | 설명 |
|---|---|
| `--voice` | `sunhi`(여, 기본), `injoon`(남), `hyunsu`, 또는 edge-tts 음성 이름 |
| `--rate` | 말 속도 (기본 `+12%`) |
| `--bgm`, `--bgm-volume` | 배경음악 파일, 볼륨 (기본 0.12) |
| `--tts none` | 음성 없이 자막만 (테스트용) |
| `--font` | 자막 폰트 직접 지정 (.ttf) |
| `-o` | 결과 폴더 |
| `--upload` | 만든 뒤 바로 유튜브 업로드 (아래 업로드 옵션 모두 사용 가능) |

## 유튜브 자동 업로드

### 1. 처음 한 번만: 업로드 권한 준비 (약 10분)
1. [Google Cloud 콘솔](https://console.cloud.google.com/)에서 새 프로젝트를 만듭니다.
2. **API 및 서비스 → 라이브러리**에서 `YouTube Data API v3`를 찾아 **사용**을 누릅니다.
3. **OAuth 동의 화면**: 유형은 *외부*, 앱 이름과 이메일을 넣고, **테스트 사용자**에 업로드할 유튜브 채널의 구글 계정을 추가합니다.
4. **사용자 인증 정보 → 사용자 인증 정보 만들기 → OAuth 클라이언트 ID**에서 유형을 **데스크톱 앱**으로 고릅니다. 만든 뒤 JSON을 내려받아 `product-shorts/client_secret.json`으로 저장합니다.
5. 처음 업로드할 때 브라우저가 열리면 채널 계정으로 로그인해 허용합니다. 그 뒤로는 `token.json`이 저장돼 자동으로 로그인됩니다.

> `client_secret.json`과 `token.json`은 비밀번호와 같습니다. `.gitignore`에 들어 있으니 깃허브나 남에게 올리지 마세요.

### 2. 업로드하기
```bash
# 만들고 바로 업로드 (기본: 비공개)
python shorts.py examples/products.csv --upload

# 이미 만든 영상 올리기 (output 안에서 아직 안 올린 것만)
python upload.py output

# 12/1 저녁 6시부터 3시간 간격으로 예약 공개
python upload.py output --publish-at "2026-12-01 18:00" --interval 3h

# 바로 전체 공개
python upload.py output --privacy public
```

자동으로 처리되는 것:
- 제목에 `#shorts` 추가, 설명란(구매 링크, 파트너스 고지, 해시태그), 태그, 아동용 아님 설정
- 쿠팡 링크면 **'유료 광고 포함'** 표시 (`--no-paid-promo`로 끌 수 있음)
- 구매 링크 **댓글 작성**. API로는 댓글을 고정할 수 없어서, Studio에서 **고정**을 눌러야 합니다.
- 올린 영상은 `upload_result.json`에 기록돼서 다시 실행해도 **중복 업로드되지 않습니다**.

비공개·예약 영상에는 댓글이 안 달릴 수 있습니다. 공개된 뒤에 아래 명령으로 링크 댓글만 다시 달면 됩니다.
```bash
python upload.py output --comments-only
```

### 꼭 알아둘 제한
- **감사(audit) 전에는 비공개로만 올라갑니다.** 2020년 7월 28일 이후 만든 API 프로젝트는 Google의 검토를 통과하기 전까지 업로드한 영상이 모두 비공개로 고정됩니다. `--privacy public`이나 예약을 해도 마찬가지입니다. 방법은 두 가지입니다.
  - Studio에서 직접 공개로 바꾸기 (업로드까지는 자동)
  - [YouTube API 감사·할당량 신청서](https://support.google.com/youtube/contact/yt_api_form)를 제출해 검토 받기
- **하루 업로드 개수 제한(할당량)**: 프로젝트마다 하루 사용량이 정해져 있습니다. 현재 값은 Google Cloud 콘솔의 **API → 할당량** 화면에서 확인하세요. 초과하면 프로그램이 멈추고, 다음 날 다시 실행하면 남은 영상만 올라갑니다.
- **썸네일**: `--thumbnail`로 올릴 수 있지만 채널 인증(전화번호)이 필요하고, 쇼츠 피드에서는 안 보일 수 있습니다.
- **같은 영상을 너무 많이 올리면** 스팸 정책에 걸릴 수 있습니다. 상품마다 대본과 이미지를 다르게 하세요.

## 주의사항

- **쿠팡파트너스**: 링크가 쿠팡이면 설명란과 고정 댓글에 대가성 고지 문구를 자동으로 넣습니다. 지우지 마세요.
- **상품 이미지 저작권**: 판매처 이미지 사용 조건을 확인하세요. 직접 찍은 사진이 가장 안전합니다.
- **배경음악**: YouTube 오디오 보관함 같은 저작권 무료 음원을 쓰세요.
- **URL 추출**: 쿠팡처럼 봇을 막는 쇼핑몰은 `--url`이 실패할 수 있습니다. 그럴 때는 JSON으로 직접 입력하세요.
- **TTS 실패**: edge-tts는 인터넷 연결이 필요합니다. 연결이 안 되면 자동으로 무음으로 바뀌고 콘솔에 안내가 나옵니다.

## 폴더 구조

```
product-shorts/
├── shorts.py              # 실행 파일 (CLI)
├── upload.py              # 만든 영상 유튜브 업로드
├── shortsmaker/
│   ├── product.py         # JSON/CSV/URL 상품 불러오기
│   ├── script.py          # 대본 생성 (템플릿 + Claude)
│   ├── tts.py             # edge-tts 음성
│   ├── render.py          # 장면 그리기, 자막, ffmpeg 합성
│   ├── pipeline.py        # 전체 흐름, 썸네일, 업로드 문구
│   ├── youtube.py         # 유튜브 업로드 (OAuth, 예약, 댓글)
│   └── fonts.py           # 한글 폰트 자동 준비
└── examples/              # 예시 상품 + 샘플 이미지
```

## 다음에 붙이면 좋은 것
- 인스타그램 릴스 / 틱톡 업로드
- 상품 영상 클립(mp4) 입력 지원
- 단어 단위 자막 싱크 (edge-tts WordBoundary 활용)
