# 원님 시리즈 1화 — 장면 이미지 프롬프트 (s03~s23)

`wonnim-tiger-midform.md` 본편 장면표의 이미지를 만드는 프롬프트다.
Google Flow 이미지 생성(나노바나나)이나 Gemini 앱에 붙여 넣는다. 받은 이미지는 `s03.png`처럼 장면 번호로 저장하고, 브루에서 장면별로 매칭한다.

## 사용법

1. **레퍼런스 3장을 먼저 만든다** (R1~R3). 이후 장면을 만들 때마다 해당 인물의 레퍼런스를 함께 첨부하면 얼굴과 의상이 유지된다.
2. 장면 프롬프트 앞에 **공통 스타일**을 붙인다. 아래 장면 프롬프트에는 이미 붙여 두었다.
3. 캡컷에서 줌·팬 효과를 넣으므로 **인물을 화면 가운데에 두고 여백을 넉넉하게** 잡았다. 줌인해도 잘리지 않는다.
4. 인트로 Veo 영상과 같은 인물 묘사 문장을 쓴다. 영상과 이미지 사이에서 인물이 바뀌어 보이지 않게 하기 위해서다.

## 복식 고증 메모

| 인물 | 기준 |
|---|---|
| 원님 (지방 수령, 당하관) | 푸른 계열 단령, 가슴에 **네모난** 학 흉배 한 마리, 흑사모, 각대. 둥근 흉배(보)는 왕실용이라 쓰지 않는다 |
| 이방 (아전) | 회색 도포, 흑립(갓). 관복은 입지 않는다 |
| 포졸 | 검은 전립(벙거지), 더그레(소매 없는 겉옷), 육모방망이 |
| 백성 | 흰 무명 한복, 상투에 망건 또는 수건, 짚신. 여인은 쪽머리 |
| 아이 | 댕기머리, 색동저고리(명절옷이지만 이야기 단서라 유지) |

> 더 세밀한 고증이 필요하면 `yadam-flow-prompts` 스킬 기준을 따른다.

## 공통 스타일

```
Vertical 9:16, cinematic photorealistic still from a Korean historical drama set in the Joseon dynasty, muted natural colors, soft film grain, subject centered with generous margins for slow zoom and pan.
No text, no subtitles, no captions, no logos, no watermark.
```

---

## 인물 레퍼런스

### R1 — 원님

```
Character reference image, vertical 9:16, photorealistic, Joseon dynasty.
A Korean magistrate of the Joseon dynasty in his early 30s, lean face, neat short beard, calm sharp eyes, wearing a deep navy official robe (dallyeong) with a square embroidered crane rank badge (hyungbae) on the chest, a black horn belt, and a black winged samo hat.
Front-facing upper body, neutral calm expression, plain light grey studio background, soft even lighting.
No text, no logos, no watermark.
```

### R2 — 호랑이

```
Reference image, vertical 9:16, photorealistic.
A huge old Korean Siberian tiger with thick orange and black fur and a torn scar on its left ear, sitting and facing the camera, calm dignified eyes.
Plain light grey studio background, soft even lighting, full body visible.
No text, no logos, no watermark.
```

### R3 — 이방

```
Character reference image, vertical 9:16, photorealistic, Joseon dynasty.
A plump Korean clerk in his 50s with narrow cunning eyes and a thin moustache, wearing a grey robe (dopo) and a black gat hat.
Front-facing upper body, slight forced smile, plain light grey studio background, soft even lighting.
No text, no logos, no watermark.
```

---

## 장면 프롬프트

### s03 — 고을 전경 · 첨부: 없음

```
Vertical 9:16, cinematic photorealistic still from a Korean historical drama set in the Joseon dynasty, muted natural colors, soft film grain, subject centered with generous margins for slow zoom and pan.
A small Joseon village of thatched-roof houses and a tiled-roof government office in a valley, surrounded by deep dark mountains, thick dawn mist rolling down the slopes, wide aerial view.
No text, no subtitles, no captions, no logos, no watermark.
```

### s04 — 원님 부임 · 첨부: R1

```
Vertical 9:16, cinematic photorealistic still from a Korean historical drama set in the Joseon dynasty, muted natural colors, soft film grain, subject centered with generous margins for slow zoom and pan.
The magistrate from the reference image, same face and same navy dallyeong robe, crane rank badge and samo hat, rides a brown horse through the village entrance on a dirt road, two constables in black jeonrip hats walking ahead.
On both sides, villagers in white cotton hanbok peek nervously through half-open wooden doors and stone walls, avoiding his eyes. Overcast morning.
No text, no subtitles, no captions, no logos, no watermark.
```

### s05 — 비어 있는 산길 · 첨부: 없음

```
Vertical 9:16, cinematic photorealistic still from a Korean historical drama set in the Joseon dynasty, muted natural colors, soft film grain, subject centered with generous margins for slow zoom and pan.
An empty narrow mountain path in a dark pine forest, a wooden A-frame carrier (jige) lying abandoned on its side, a single small straw sandal in the middle of the path, cold mist, eerie silence.
No text, no subtitles, no captions, no logos, no watermark.
```

### s06 — 주막의 소문 · 첨부: 없음

```
Vertical 9:16, cinematic photorealistic still from a Korean historical drama set in the Joseon dynasty, muted natural colors, soft film grain, subject centered with generous margins for slow zoom and pan.
Night inside a Joseon tavern (jumak), oil lamp light, three villagers in white hanbok leaning close and whispering with fearful faces over bowls of makgeolli.
Through the open door behind them, in the dark forest on the mountain, two glowing tiger eyes.
No text, no subtitles, no captions, no logos, no watermark.
```

### s07 — 이방의 건의 · 첨부: R1, R3

```
Vertical 9:16, cinematic photorealistic still from a Korean historical drama set in the Joseon dynasty, muted natural colors, soft film grain, subject centered with generous margins for slow zoom and pan.
Inside the wooden main hall of a Joseon county office, daylight through paper doors.
The magistrate from reference R1 sits behind a low wooden desk. The clerk from reference R3, same face, grey robe and black gat, bows deeply in front of him, presenting a folded paper document with both hands, a sly smile hidden from the magistrate.
No text, no subtitles, no captions, no logos, no watermark.
```

### s08 — 의심하는 원님 · 첨부: R1

```
Vertical 9:16, cinematic photorealistic still from a Korean historical drama set in the Joseon dynasty, muted natural colors, soft film grain, subject centered with generous margins for slow zoom and pan.
Close-up of the magistrate from the reference image, same face, samo hat and navy robe, brows slightly furrowed, eyes narrowed in doubt, looking off-camera to the side. Soft window light from the left, dark background.
No text, no subtitles, no captions, no logos, no watermark.
```

### s09 — 호랑이를 끌고 온 사냥꾼들 · 첨부: R2

```
Vertical 9:16, cinematic photorealistic still from a Korean historical drama set in the Joseon dynasty, muted natural colors, soft film grain, subject centered with generous margins for slow zoom and pan.
Pre-dawn, blue mist and orange torchlight. Five rugged Korean hunters in fur vests with bows on their backs drag the tiger from the reference image, bound with thick ropes, through the wooden gate of a Joseon government office. Villagers with torches crowd behind them.
No text, no subtitles, no captions, no logos, no watermark.
```

### s10 — 앞발을 살피는 원님 · 첨부: R1, R2

```
Vertical 9:16, cinematic photorealistic still from a Korean historical drama set in the Joseon dynasty, muted natural colors, soft film grain, subject centered with generous margins for slow zoom and pan.
In the torch-lit stone courtyard, the magistrate from reference R1 crouches down close to the bound tiger from reference R2, his robe touching the ground, carefully examining the tiger's front paw. The tiger lies still and watches him calmly. Constables in the background step back nervously.
No text, no subtitles, no captions, no logos, no watermark.
```

### s11 — 발톱에 걸린 색동 옷고름 · 첨부: R2

```
Vertical 9:16, cinematic photorealistic still, extreme close-up macro shot.
A huge tiger paw with thick orange fur and sharp claws resting on a grey stone floor. Caught on one claw is a small torn strip of a child's rainbow-striped saekdong ribbon, stained with brown mud, no blood. Warm torchlight, shallow depth of field.
No text, no subtitles, no captions, no logos, no watermark.
```

### s12 — 원님의 명령 · 첨부: R1

```
Vertical 9:16, cinematic photorealistic still from a Korean historical drama set in the Joseon dynasty, muted natural colors, soft film grain, subject centered with generous margins for slow zoom and pan.
The magistrate from the reference image stands up straight in the torch-lit courtyard, holding the small muddy rainbow ribbon in one hand, turning to give an order to a constable in a black jeonrip hat and a sleeveless deogeure vest, who bows. Low angle, serious mood.
No text, no subtitles, no captions, no logos, no watermark.
```

### s13 — "호랑이를 풀어라" · 첨부: R2

```
Vertical 9:16, cinematic photorealistic still from a Korean historical drama set in the Joseon dynasty, muted natural colors, soft film grain, subject centered with generous margins for slow zoom and pan.
A trembling constable in a black jeonrip hat cuts the thick ropes off the tiger from the reference image with a knife. The tiger slowly rises. Villagers in white hanbok stumble backward in terror, torches shaking, one woman covering her mouth.
No text, no subtitles, no captions, no logos, no watermark.
```

### s14 — 산길을 안내하는 호랑이 · 첨부: R1, R2

```
Vertical 9:16, cinematic photorealistic still from a Korean historical drama set in the Joseon dynasty, muted natural colors, soft film grain, subject centered with generous margins for slow zoom and pan.
A misty mountain path through tall pine trees, early morning. The tiger from reference R2 walks slowly uphill in front, looking back over its shoulder. Several steps behind follow the magistrate from reference R1 and three constables in black jeonrip hats holding wooden clubs, tense.
View from below, looking up the slope.
No text, no subtitles, no captions, no logos, no watermark.
```

### s15 — 절벽 아래 동굴 · 첨부: R2

```
Vertical 9:16, cinematic photorealistic still from a Korean historical drama set in the Joseon dynasty, muted natural colors, soft film grain, subject centered with generous margins for slow zoom and pan.
The dark entrance of a small cave at the foot of a tall rocky cliff, covered with moss and vines, mist around it. The tiger from the reference image stands still beside the entrance and turns its head back toward the camera.
No text, no subtitles, no captions, no logos, no watermark.
```

### s16 — 살아 있는 아이들 · 첨부: 없음

```
Vertical 9:16, cinematic photorealistic still from a Korean historical drama set in the Joseon dynasty, muted natural colors, soft film grain, subject centered with generous margins for slow zoom and pan.
Inside a rocky cave lit by a single torch from the entrance. Three Joseon children, ages about 6 to 10, with braided daenggi hair, dirty faces, wearing worn hanbok, one girl in a rainbow-striped saekdong jeogori with a torn ribbon, huddle together on a straw mat, alive and wide-eyed. Beside them lies a pile of wild game meat brought by an animal.
No text, no subtitles, no captions, no logos, no watermark.
```

### s17 — 원님 품의 아이 · 첨부: R1

```
Vertical 9:16, cinematic photorealistic still from a Korean historical drama set in the Joseon dynasty, muted natural colors, soft film grain, subject centered with generous margins for slow zoom and pan.
In the torch-lit cave, the magistrate from the reference image kneels and holds the youngest child, a small girl in a rainbow-striped saekdong jeogori with braided hair, who cries and clings to his navy robe. His face is gentle but grave.
No text, no subtitles, no captions, no logos, no watermark.
```

### s18 — 굳은 원님의 얼굴 · 첨부: R1

```
Vertical 9:16, cinematic photorealistic still from a Korean historical drama set in the Joseon dynasty, muted natural colors, soft film grain, subject centered with generous margins for slow zoom and pan.
Close-up of the magistrate from the reference image inside the dark cave, half his face lit by flickering torchlight, half in shadow, jaw set, eyes cold and focused as he realizes the truth.
No text, no subtitles, no captions, no logos, no watermark.
```

### s19 — 이방 집 하인의 표식과 산삼 자루 · 첨부: 없음

```
Vertical 9:16, cinematic photorealistic still from a Korean historical drama set in the Joseon dynasty, muted natural colors, soft film grain, subject centered with generous margins for slow zoom and pan.
At night in the back storeroom of a wealthy Joseon house, two servants in brown hanbok, each with the same small dark-blue cloth tag sewn on the collar, tie up straw sacks overflowing with wild ginseng roots. Oil lamp light, secretive mood.
No text, no subtitles, no captions, no logos, no watermark.
```

### s20 — 다시 열린 재판 · 첨부: R1, R3

```
Vertical 9:16, cinematic photorealistic still from a Korean historical drama set in the Joseon dynasty, muted natural colors, soft film grain, subject centered with generous margins for slow zoom and pan.
The stone courtyard of the government office in daylight. The magistrate from reference R1 stands on the raised wooden hall, pointing down firmly. Below him, the clerk from reference R3 kneels on the stone ground between two constables, his black gat knocked askew, face pale with fear. Villagers in white hanbok crowd around.
No text, no subtitles, no captions, no logos, no watermark.
```

### s21 — 무너진 이방 · 첨부: R3

```
Vertical 9:16, cinematic photorealistic still from a Korean historical drama set in the Joseon dynasty, muted natural colors, soft film grain, subject centered with generous margins for slow zoom and pan.
The clerk from the reference image prostrates himself with his forehead pressed to the stone ground, his gat fallen beside him. All around, angry villagers in white hanbok point at him and shout. Harsh midday light.
No text, no subtitles, no captions, no logos, no watermark.
```

### s22 — 고개 숙인 호랑이 · 첨부: R1, R2

```
Vertical 9:16, cinematic photorealistic still from a Korean historical drama set in the Joseon dynasty, muted natural colors, soft film grain, subject centered with generous margins for slow zoom and pan.
At the edge of a misty pine forest at dawn, the tiger from reference R2 stands at the treeline, turned back and bowing its head low. In the foreground, seen from behind, the magistrate from reference R1 stands alone watching it. Soft golden light through the fog, quiet and moving.
No text, no subtitles, no captions, no logos, no watermark.
```

### s23 — 3년 뒤, 끌려가는 원님 · 첨부: R1

```
Vertical 9:16, cinematic photorealistic still from a Korean historical drama set in the Joseon dynasty, muted natural colors, soft film grain, subject centered with generous margins for slow zoom and pan.
A dark night road under a full moon. The magistrate from the reference image, now with a slightly longer beard, without his samo hat, in a plain white prisoner's robe, hands bound with red rope, is led by royal guards with torches. In the far background, on a moonlit mountain ridge, the silhouette of a huge tiger.
No text, no subtitles, no captions, no logos, no watermark.
```

### s24 — 검은 화면

이미지를 만들지 않는다. 캡컷이나 브루에서 검은 배경에 "원님 시리즈 2화에서 계속"을 넣는다.

---

## 결과 확인 체크

- [ ] 원님 흉배가 **네모**인지 (둥글게 나오면 다시 생성)
- [ ] 원님 얼굴이 R1과 같은지. s04, s08, s17, s22는 특히 확인
- [ ] 호랑이 왼쪽 귀 흉터가 s09~s15, s22에서 유지되는지
- [ ] 이미지 안에 글자나 워터마크가 없는지
- [ ] s11 옷고름에 **피가 아니라 진흙**이 묻었는지 (이야기 단서)
