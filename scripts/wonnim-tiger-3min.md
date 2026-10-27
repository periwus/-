# 원님 시리즈 1화: 호랑이를 재판한 원님 (2분 50초 미드폼 쇼츠)

**스토리 한 줄 요약:** 아이를 물어 간 호랑이를 처형하라는 백성들 앞에서 새로 온 원님이 "재판하겠다"고 선언한다.
호랑이가 이끈 산속 동굴에서 사라진 아이들이 살아 돌아오고, 진짜 범인은 호랑이 소문으로 이득을 보던 이방으로 드러난다.

**제작 방식**
- **0~16초 인트로: Veo 3 영상 2클립.** 이야기에서 가장 강한 장면(관아 마당 호랑이 재판)을 맨 앞에 보여 준다.
- **16초~끝: 브루 나레이션 + 장면 이미지 + 캡컷 움직임 효과.**
- 브루 나레이션은 약 760음절이다. 보통 TTS 속도면 2분 20~30초가 나오니, 합계가 2분 59초를 넘지 않게 속도를 맞춘다.

---

## 등장인물 고정 묘사 (이미지·영상 공통)

| 인물 | 한국어 설명 | 프롬프트용 앵커 |
|---|---|---|
| 원님 | 30대 초반, 마른 얼굴, 단정한 수염, 침착한 눈빛, 남색 단령에 흑사모 | `a Korean magistrate of the Joseon dynasty in his early 30s, lean face, neat short beard, calm sharp eyes, wearing a deep navy official robe (dallyeong) with a round rank badge on the chest and a black winged samo hat` |
| 호랑이 | 크고 늙은 수컷 백두산 호랑이, 왼쪽 귀에 찢긴 흉터 | `a huge old Korean Siberian tiger with thick orange and black fur and a torn scar on its left ear` |
| 이방 | 50대, 살찐 얼굴, 가는 눈, 회색 도포, 갓 | `a plump Korean clerk in his 50s with narrow cunning eyes, wearing a grey robe and a black gat hat` |
| 사냥꾼 | 40대, 거친 수염, 털조끼, 활 | `a rugged Korean hunter in his 40s with a rough beard, a fur vest, carrying a bow` |

> 복식 고증을 더 세밀하게 하려면 `yadam-flow-prompts` 스킬로 레퍼런스 이미지를 먼저 만든다.

---

## PART 1. 인트로 — Veo 3 영상 (0~16초)

### 키프레임 (클립 1 시작 프레임)

```
Vertical 9:16 photorealistic still frame from a Korean historical drama, Joseon dynasty, pre-dawn blue light mixed with orange torchlight, light mist.
Scene: the stone courtyard of a Joseon county government office (gwana), a wooden hall with a raised floor in the background, villagers in white hanbok holding torches on both sides.
Center: a huge old Korean Siberian tiger with thick orange and black fur and a torn scar on its left ear, bound with thick ropes, lying low on the stone ground, its eyes calm, not aggressive.
Beside it, a rugged Korean hunter in his 40s with a rough beard, a fur vest, carrying a bow, pointing at the tiger.
Background, on the raised hall, seated: a Korean magistrate of the Joseon dynasty in his early 30s, lean face, neat short beard, calm sharp eyes, wearing a deep navy official robe (dallyeong) with a round rank badge on the chest and a black winged samo hat. His face is clearly visible, looking down at the tiger with a serious expression.
Composition: low-angle wide shot from behind the tiger's shoulder, tiger in the foreground, magistrate centered above. The moment right before the crowd starts shouting.
No text, no subtitles, no logos, no watermark.
```

### 클립 1 (0~8초) — 분노한 백성들

```
Vertical 9:16, photorealistic Korean historical drama, Joseon dynasty, 8 seconds, continuous shot.
Setting: the stone courtyard of a Joseon county government office before dawn, torchlight and mist, villagers in white hanbok holding torches.
Characters:
- Tiger: a huge old Korean Siberian tiger with thick orange and black fur and a torn scar on its left ear, bound with thick ropes.
- Hunter: a rugged Korean hunter in his 40s with a rough beard, a fur vest, carrying a bow.
- Magistrate: a Korean magistrate of the Joseon dynasty in his early 30s, lean face, neat short beard, calm sharp eyes, wearing a deep navy official robe (dallyeong) with a round rank badge and a black winged samo hat, seated on the raised hall.

[0-4s] The hunter steps forward and shouts toward the hall. The tiger stays low and still. Camera: static low angle.
The hunter shouts in Korean, furious: "사또! 이놈이 아이들을 물어 갔습니다!"

[4-8s] The villagers raise their torches and shout together. Torch flames flicker. Camera: slow push-in toward the tiger's face; the tiger slowly lifts its head.
The villagers shout in Korean, all together: "죽여라! 죽여라!"

Audio: No background music. Only Korean voices and ambient sound: crackling torches, crowd murmuring, the tiger's low breathing.
No subtitles, no captions, no on-screen text, no watermark.
```

### 클립 2 (8~16초) — 원님의 선언

```
Continue the same scene. Vertical 9:16, photorealistic Korean historical drama, 8 seconds.
Characters: same tiger, hunter and magistrate as before, same outfits.

[0-3s] The magistrate stands up on the raised hall and raises one hand. The crowd falls silent at once. Camera: low-angle medium shot of the magistrate.

[3-6s] Close-up of the tiger: it looks straight up at the magistrate; their eyes meet.

[6-8s] Close-up of the magistrate, calm and firm.
The magistrate says in Korean, in a low steady voice: "멈춰라. 이 호랑이는 재판을 받는다."

Audio: No background music. Only Korean dialogue and ambient sound: torches crackling, sudden silence, a soft tiger growl.
No subtitles, no captions, no on-screen text, no watermark.
```

**Flow 설정:** 클립 1은 키프레임을 시작 프레임으로 넣고 Frames to Video로 만든다. 클립 2는 Extend로 이어서 만든다. 둘 다 9:16, 8초, 생성 개수 1.

**편집:** 16초 지점에서 화면을 흰색으로 0.3초 번쩍이게 한 뒤, 제목 자막 **"호랑이를 재판한 원님"**을 1.5초 띄운다.

---

## PART 2. 본편 — 브루 나레이션 + 이미지 + 캡컷 효과 (16초~)

- 이미지 파일명은 `s03.png`부터 순서대로 붙인다. 브루에서 장면별로 매칭한다.
- **효과** 열은 캡컷 기준이다. 브루만 쓸 때는 이미지 애니메이션 중 확대·축소·이동으로 대신한다.
- ⏸ 표시는 0.5초 쉼, 🔔 표시는 다시 궁금증을 거는 문장(재후킹)이다.

| 장면 | 이미지 내용 | 나레이션 | 효과 |
|---|---|---|---|
| s03 | 깊은 산을 낀 고을 전경, 새벽 안개 | 옛날, 깊은 산을 낀 한 고을에 젊은 원님이 새로 부임했습니다. | 천천히 줌아웃 + 안개 오버레이 |
| s04 | 원님이 말을 타고 고을 입구에 들어섬, 백성들이 문틈으로 훔쳐봄 | 그런데 부임 첫날부터, 백성들은 원님의 눈을 피했습니다. | 좌→우 팬 |
| s05 | 텅 빈 산길, 버려진 지게와 짚신 한 짝 | 석 달 사이, 산에 오른 아이 셋이 감쪽같이 사라졌기 때문입니다. ⏸ | 느린 줌인 + 비네팅 |
| s06 | 주막에서 수군대는 사람들, 어둠 속 호랑이 눈 실루엣 | 사람들은 말했습니다. 산에 사람 잡아먹는 호랑이가 산다고. | 호랑이 눈 부분으로 줌인 + 화면 어둡게 |
| s07 | 관아 대청, 허리 숙인 이방이 원님에게 문서를 올림 | 이방이 원님에게 아뢰었습니다. "사또, 호랑이를 잡으려면 사냥꾼을 풀어야 합니다. 백성들에게 호랑이 세를 걷으시지요." | 고정 → 이방 얼굴로 살짝 줌인 |
| s08 | 원님의 클로즈업, 미간을 찌푸림 | 원님은 고개를 갸웃했습니다. 호랑이를 잡는데, 왜 백성의 돈이 필요하단 말인가. | 줌인 |
| s09 | 횃불 든 사냥꾼들이 밧줄로 호랑이를 끌고 관아로 들어옴 | 그리고 사흘 뒤 새벽, 사냥꾼들이 거대한 호랑이를 끌고 왔습니다. 바로 그날 아침, 원님이 재판을 선언한 것입니다. | 흔들림 효과 0.5초 + 횃불 불꽃 오버레이 |
| s10 | 호랑이 앞에 쪼그려 앉아 앞발을 들여다보는 원님 | 🔔 그런데 호랑이 앞에 다가간 원님은, 이상한 것을 발견합니다. ⏸ | 느린 줌인 |
| s11 | 호랑이 앞발 발톱에 걸린 색동 옷고름 한 조각, 진흙 묻음 | 호랑이 발톱에 걸린 것은 피 묻은 살점이 아니었습니다. 아이 저고리의 색동 옷고름. 그리고 피가 아니라, 진흙이었습니다. | 옷고름에 강한 줌인 + 플래시 전환 |
| s12 | 원님이 일어서며 포졸에게 명령 | 원님이 물었습니다. "아이들이 마지막으로 보인 곳이 어디냐." | 고정 |
| s13 | 밧줄을 풀어 주는 포졸, 놀라 뒷걸음치는 백성들 | 그리고 모두가 기겁할 명령을 내렸습니다. "호랑이를 풀어라." | 흔들림 효과 + 빠른 줌아웃 |
| s14 | 안개 낀 산길, 호랑이가 앞서고 원님과 포졸들이 뒤따름 | 호랑이는 달아나지 않았습니다. 마치 길을 안내하듯, 천천히 산으로 걸어 올라갔습니다. | 아래→위 팬 |
| s15 | 바위 절벽 아래 어두운 동굴 입구, 호랑이가 멈춰 돌아봄 | 🔔 한 시진을 걸어 호랑이가 멈춘 곳은, 절벽 아래 작은 동굴 앞이었습니다. ⏸ | 동굴 입구로 느린 줌인 + 화면 어둡게 |
| s16 | 동굴 안, 횃불에 비친 아이 셋이 웅크린 채 살아 있음, 옆에 산짐승 고기 | 동굴 안에는 사라졌던 아이 셋이, 살아 있었습니다. 곁에는 호랑이가 물어다 놓은 산짐승 고기가 쌓여 있었죠. | 플래시 전환 → 줌아웃 |
| s17 | 원님 품에 안겨 우는 가장 어린 아이 | 가장 어린 아이가 울며 말했습니다. "아저씨들이 우리를 산에 버렸어요. 호랑이가 우리를 여기로 데려왔어요." | 느린 줌인 |
| s18 | 원님의 굳은 얼굴, 횃불 그림자 | 🔔 원님이 물었습니다. "그 아저씨들, 누구였느냐." 아이는 떨리는 손으로, 옷깃에 달린 표식을 가리켰습니다. | 얼굴로 줌인 |
| s19 | 이방 집 하인들의 옷에 달린 같은 표식, 산삼이 가득 든 자루 | 그 표식은 이방 집 하인들의 것이었습니다. 이방은 아이들을 산에 버리고 호랑이 소문을 퍼뜨렸습니다. 사람들이 산에 못 오르는 사이 산삼밭을 독차지하고, 호랑이 세까지 챙기려 한 것이죠. | 좌→우 팬 + 표식에 줌인 |
| s20 | 다시 관아 마당, 무릎 꿇은 이방, 백성들 | 다시 열린 재판. 원님이 판결했습니다. "호랑이는 무죄다. 죄인은, 저기 있다." | 흔들림 효과 + 이방에게 빠른 줌인 |
| s21 | 이방이 땅에 이마를 박고 엎드림, 백성들이 손가락질 | 이방은 그 자리에서 무너졌고, 백성들의 분노는 호랑이가 아닌 이방에게 향했습니다. | 고정 + 비네팅 |
| s22 | 산 입구에서 호랑이가 떠나다 돌아보고 고개 숙임, 원님이 지켜봄 | 호랑이를 산으로 돌려보내던 날. 호랑이는 숲으로 들어가다 멈춰, 원님을 향해 고개를 숙였습니다. ⏸ | 아주 느린 줌아웃 + 안개 오버레이 |
| s23 | 3년 뒤 밤, 포박되어 끌려가는 원님, 멀리 산 능선 | 🔔 그리고 3년 뒤. 원님이 역적 누명을 쓰고 한양으로 끌려가던 밤. 산 너머에서, 그 울음소리가 들려왔습니다. | 화면 어둡게 → 흔들림 + 호랑이 포효 효과음 |
| s24 | 검은 화면 | 원님 시리즈 2화에서 계속됩니다. | 페이드아웃 |

---

## 편집 메모

- **배경음악:** Veo 클립은 배경음악 없이 만들고, 편집에서 국악풍 배경음악 하나를 인트로부터 끝까지 낮게 깐다. 1분이 넘는 쇼츠라 저작권 걸리는 음원은 쓰지 않는다.
- **효과음:** 호랑이 울음 (s09, s23), 횃불 타는 소리 (s09, s20), 종이·옷 스치는 소리 (s11).
- **자막:** 브루 자동 자막을 쓴다. 이방의 대사와 원님의 판결 대사는 글자를 크게 키운다.
- **이어 보기 장치:** 관련 동영상 링크는 원님 롱폼 또는 2화에 건다. 고정 댓글: "여러분이 원님이었다면 호랑이를 풀어 줄 수 있었을까요?"
- **30초 쇼츠 재활용:** Veo 클립 2개(16초) + s11 + s16 + s20에 압축 나레이션을 붙이면 30초 예고편이 된다. 이 예고편의 관련 동영상 링크는 이 3분 영상에 건다.
