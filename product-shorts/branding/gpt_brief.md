# 채널 전환 확정안 (ChatGPT 이미지용)

대상 채널: 기존 「격투기명장면」 → 상품 쇼츠 채널로 전환

## ✅ 실제 적용 결과 (2026-11-28)

| 항목 | 적용 내용 |
|---|---|
| 이름 | **살림픽** |
| 핸들 | **@살림픽tv** (@salimpick, @salimpick.kr, @살림픽, salimpick_tv는 이미 사용 중) |
| 채널 ID | `UCgS9CvAWlfMSvVi4Jkn4Bnw` |
| 예전 영상 | 격투기 쇼츠 2개 비공개 (삭제 안 함) |
| 아이콘 | 빨간 굵은 한글 스티커 글자 "살림픽" + 노란 체크 (ChatGPT 생성) |
| 배너 | 밝은 바탕 가운데에 "오늘 살림, 딱 맞는 픽 / 살림픽 / 겨울템·주방·청소·생활꿀템" + 담요·머그·분무기·바구니 3D 아이콘 (ChatGPT 생성, 글자 확인, 모바일 안전 영역 안) |
| 스타일을 바꾼 이유 | 아래 2번의 노랑·남색 플랫 안은 "촌스럽다"는 의견이 있어서, 잘되는 살림 채널(살림로그, 살림남)처럼 밝은 바탕과 3D 아이콘 스타일로 바꿨어요 |
| 소개글 | 아래 문구에서 "직접 사서 써 본"을 "직접 찾아보고 고른"으로 바꿔 적용 |
| 프로필 링크 | 아직 비어 있음 (쿠팡 링크를 만든 뒤 1~5번 추가) |
| 남은 일 | 쿠팡 파트너스 '내 정보'에 채널 주소 등록, 프로필 링크 1~5번 추가 |

> 아래 2번의 노랑·남색 프롬프트는 쓰지 않았어요. 기록용으로만 남겨 둡니다.

## 1. 채널 이름 · 핸들 · 소개글

| | 이름 | 핸들 후보 (순서대로 시도) |
|---|---|---|
| ⭐ 추천 | **살림픽** | @salimpick → @salimpick.kr → @살림픽 |
| 2 | 꿀템한입 | @kkultem.hanip → @꿀템한입 |
| 3 | 살림한컷 | @salimhancut → @살림한컷 |

- 추천 이유: 3글자라 짧고 발음이 쉬워요. '살림'은 겨울 외풍템부터 사계절 생활용품까지 다 담을 수 있어요. 과장되거나 낚시처럼 들리는 느낌도 없어요.
- 이름과 핸들은 14일 동안 2번까지만 바꿀 수 있어요. **핸들이 비어 있는지 먼저 확인한 뒤**, 이름과 핸들을 한 번에 바꾸세요.
- 아이콘과 배너에는 이름을 넣지 않아요(아래 2번). 그래서 다른 이름을 골라도 그림은 그대로 쓸 수 있어요.

### 채널 소개글 (그대로 붙여넣기)

```
직접 사서 써 본 생활용품을 짧게 소개하는 살림픽입니다.

겨울 외풍·보온템부터 집에서 매일 쓰는 살림템까지,
설치하고 쓰는 모습을 그대로 보여드려요.

📌 상품 링크: 채널 상단 '링크'에서 영상 속 번호를 찾아 주세요.
📌 가격은 영상을 올린 날 기준이라 바뀔 수 있어요.

이 채널은 쿠팡 파트너스 활동의 일환으로, 이에 따른 일정액의 수수료를 제공받습니다.
```

- 업로드 일정은 실제로 지킬 수 있을 때만 넣으세요. 넣는다면 "매주 ○요일" 같은 형식이 좋아요.
- '직접 사서 써 본'은 실제로 사서 찍은 영상만 올린다는 전제의 문구예요. 판매처 사진만으로 영상을 만든다면 이 문구는 빼세요.

## 2. ChatGPT용 영어 프롬프트

### 결정 사항
- **아이콘:** 글자 없이 심볼만 넣어요. 48픽셀로 줄어들어도 알아볼 수 있어야 하기 때문이에요.
- **배너:** 그림 안에 글자를 **넣지 않아요.** 이미지 생성 AI는 한글 글자를 자주 틀리게 그려요. 채널 이름이 필요하면 아래 명령으로 정확한 폰트로 따로 얹어요. 그래서 배너 그림은 가운데를 비워 두게 했어요.
- **색:** 노랑 `#FFD400`과 남색 `#161B2D`. 쇼츠 자막의 강조색과 같은 조합이에요.
- **크기:** ChatGPT는 정해진 비율로만 그려요. 아이콘은 1024×1024, 배너는 1536×1024(가로형)로 받은 뒤 아래 명령으로 유튜브 규격에 맞춰요.

### 아이콘 프롬프트

```
Create a square 1024x1024 YouTube channel profile icon.
Flat vector style, bold and simple, no text, no letters, no numbers, no logos.
Solid warm yellow background (#FFD400) filling the entire canvas.
In the center, a single dark navy (#161B2D) shopping bag with a short rounded handle,
and a thick yellow check mark cut out of the front of the bag.
The bag should occupy about 55% of the canvas width, perfectly centered,
with generous empty space on all sides because the icon will be cropped to a circle.
Thick shapes, rounded corners, no thin lines, no small details, no gradients, no shadows.
It must stay clearly recognizable when shrunk to 48x48 pixels.
```

### 배너 프롬프트

```
Create a wide landscape image, 1536x1024, to be used as a YouTube channel banner.
Absolutely no text, no letters, no numbers, no logos, no brand names, no people.
Background: solid dark navy (#161B2D) with very subtle diagonal stripes in a slightly lighter navy,
plain and calm across the whole image.

All important content must sit inside ONE central horizontal band:
the band is about 60% of the image width and only about 25% of the image height,
exactly centered both horizontally and vertically.
Keep the top 37% and bottom 37% of the image plain background only.

Inside that band, place small flat-vector illustrations of cozy winter home items
with warm yellow (#FFD400) and soft white accents:
on the LEFT side: a window covered with clear insulation film with a zipper, and a padded door curtain;
on the RIGHT side: a small dome-shaped bed warming tent, a pair of knit knee warmers, and a steaming mug.
Leave the CENTER third of the band completely empty (plain navy) so a channel name can be added later.
Friendly, clean, minimal shapes with rounded corners, consistent line weight, no clutter.
```

- 다시 생성할 때는 "Keep everything else the same, but …"로 시작해서 고칠 부분만 말하세요.
- 확인할 것: 그림에 글자가 생기지 않았는지, 상단 37%와 하단 37%가 비어 있는지.

### 받은 그림을 유튜브 규격으로 맞추기

```bash
# 아이콘 → 800x800, 배너 → 2560x1440 (가운데를 기준으로 자르고 크기 조정)
python branding/make_branding.py --icon-src 받은아이콘.png --banner-bg 받은배너.png

# 배너 가운데 빈자리에 한글 채널 이름 얹기 (권장)
python branding/make_branding.py --banner-bg 받은배너.png --banner-text --name "살림픽"
```
`branding/output/`에 결과가 생겨요.

| 파일 | 용도 |
|---|---|
| `gpt_icon_800.png` | 업로드용 아이콘 |
| `gpt_icon_800_preview_circle.png` | 원형으로 잘렸을 때 모습 |
| `gpt_icon_800_preview_48px.png` | 작게 줄였을 때 알아볼 수 있는지 확인 |
| `gpt_banner_2560x1440.jpg` | 업로드용 배너 |
| `gpt_banner_2560x1440_safe_area_check.png` | 초록 상자 안에 핵심 요소가 다 들어갔는지 확인 |

## 3. 프로필 링크 (채널 → 맞춤설정 → 기본 정보 → 링크)

쇼츠 설명란과 댓글의 링크는 눌리지 않아요. 그래서 상품 링크는 채널 프로필 링크에 번호로 걸고, 영상 끝에서 "프로필 링크 N번"이라고 안내해요.

| 링크 제목 | URL |
|---|---|
| 1번 지퍼형 창문 방풍비닐 (쿠팡 파트너스) | 쿠팡 파트너스 링크 |
| 2번 현관 방한 커튼 (쿠팡 파트너스) | 〃 |
| 3번 침대 난방 텐트 (쿠팡 파트너스) | 〃 |
| 4번 무릎 기모 워머 (쿠팡 파트너스) | 〃 |
| 5번 기모 스타킹 (쿠팡 파트너스) | 〃 |

- **번호 규칙:** 번호는 상품마다 고정하고, 한 번 쓴 번호는 다른 상품에 다시 쓰지 마세요. 예전 영상이 "3번"이라고 안내하고 있기 때문이에요.
- **보이는 순서:** 첫 번째 링크만 채널 이름 아래에 보여요. 가장 최근에 올린 상품을 맨 위로 올리세요.
- **개수 제한:** 링크는 최대 14개까지 넣을 수 있어요. 넘치면 링크 모음 페이지 하나로 바꾸는 걸 그때 같이 정해요.
- **5번 상품:** 스노우체인을 찍을 수 있으면 5번을 '케이블타이 스노우체인'으로 바꾸세요.
- **대가성 고지:** 링크 제목의 "(쿠팡 파트너스)"는 짧은 고지예요. 전체 고지 문구는 소개글과 각 영상 설명란에 이미 들어 있어요.
- **쿠팡 파트너스 등록:** 쿠팡 파트너스의 '내 정보'에 이 채널 주소를 등록해야 해요.
