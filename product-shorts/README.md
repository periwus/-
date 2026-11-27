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
├── shortsmaker/
│   ├── product.py         # JSON/CSV/URL 상품 불러오기
│   ├── script.py          # 대본 생성 (템플릿 + Claude)
│   ├── tts.py             # edge-tts 음성
│   ├── render.py          # 장면 그리기, 자막, ffmpeg 합성
│   ├── pipeline.py        # 전체 흐름, 썸네일, 업로드 문구
│   └── fonts.py           # 한글 폰트 자동 준비
└── examples/              # 예시 상품 + 샘플 이미지
```

## 다음에 붙이면 좋은 것
- 유튜브 업로드 API로 자동 업로드 (OAuth 설정 필요)
- 상품 영상 클립(mp4) 입력 지원
- 단어 단위 자막 싱크 (edge-tts WordBoundary 활용)
