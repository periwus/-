# 예제: 경비실 할아버지의 진짜 명함 (Veo 3 / Flow 버전)

원본 대본(씨댄스 30초 한 번 생성용)을 Veo 3의 8초 × 4클립 구조로 바꾼 완성 예시.

---

## 1단계. 대본 (원본 요약)

**제목:** 경비실 할아버지의 진짜 명함

**스토리 한 줄 요약:** 아파트 경비원 최 할아버지는 날마다 입주민 김 사장의 갑질을 묵묵히 견딘다.
그런데 김 사장이 석 달째 월세를 밀린 세입자이고, 최 할아버지가 그 건물 주인이라는 사실이 드러나며 판세가 뒤집힌다.

구간: 0~3초 훅(컵 던지기) / 3~12초 갈등(촬영하며 조롱) / 12~22초 절정(무릎 → 등기부등본) / 22~30초 마무리(짐 빼세요).

---

## 1-B. 8초 클립 배치표

| 클립 | 구간 | 원본 구간 | 장소·구도 | 대사 (약 음절 수) |
|---|---|---|---|---|
| 1 | 0~8초 | 0~3 훅 + 3~12 앞부분 | 경비실 앞 주차장, 김 사장 어깨 너머로 할아버지 | 김: "야! 할아버지, 이거 주워! 당장!" / 김: "경비 주제에 눈 똑바로 뜨네?" (24) |
| 2 | 8~16초 | 3~12 뒷부분 + 12~22 앞부분 | 같은 장소, 미디엄 투샷 → 할아버지 쪽으로 천천히 | 김: "관리소장한테 한마디면 끝이야. 무릎 꿇고 사과해." (21) |
| 3 | 16~24초 | 12~22 절정 | 할아버지 클로즈업 → 봉투 꺼내 건넴 | 최: "무릎 꿇을 사람은 김 사장님 같은데요." (16) |
| (인서트) | 편집 삽입 1.5초 | 12~22 화면 전환 | 등기부등본·내용증명 클로즈업 정지 이미지 | 없음 |
| 4 | 24~32초 | 22~30 마무리 | 김 사장 얼굴 → 할아버지 퇴장 | 최: "다음 달 말까지 짐 빼세요. 커피는 본인이 치우시고요." (22) |

**대사 조정 (원본 → 수정본)**

| 원문 | 수정본 | 이유 |
|---|---|---|
| "야! 할아버지, 이거 주워! 지금 당장 무릎 꿇고!" | "야! 할아버지, 이거 주워! 당장!" | 무릎 요구는 클립 2로 넘겨 고조 단계를 만듦 |
| "뭘 봐요? 경비 주제에 눈 똑바로 뜨고. 관리소장한테 한마디면 할아버지 끝이야." | 클립 1 "경비 주제에 눈 똑바로 뜨네?" + 클립 2 "관리소장한테 한마디면 끝이야." | 한 클립 35음절 제한 |
| "이 주차 자리 내 차 좀 옮겨놔. 그리고 무릎 꿇고 사과해." | "무릎 꿇고 사과해." | 주차 요구는 삭제, 핵심 요구만 유지 |
| "다음 달 말까지 짐 빼세요. 아, 그리고 그 커피는 본인이 치우시고요." | "다음 달 말까지 짐 빼세요. 커피는 본인이 치우시고요." | 음절 축소 |
| "커피값은 관리비에 넣어 놓을게요." | 삭제 (원하면 편집에서 엔딩 직전 음성만 추가) | 8초 안에 들어가지 않음 |

> 4클립 합계 32초 → 편집에서 각 클립 앞뒤를 다듬어 30초로 맞춘다.

---

## 캐릭터 앵커 (모든 프롬프트에 글자 그대로 반복)

- **최 할아버지 (A):** `a Korean man in his early 70s with short thin grey hair, deep wrinkles, a calm dignified face, silver wire-rimmed glasses, wearing a navy blue security guard uniform jacket with a white name badge on the chest and a navy cap`
- **김 사장 (B):** `a Korean man in his mid 40s with slicked-back black hair, a sharp arrogant face, wearing a black designer polo shirt and a gold wristwatch, holding a smartphone`
- **동료 경비 (C):** `a Korean man in his 60s in the same navy blue security guard uniform without a cap`
- **장소:** `the outdoor parking lot of a Korean apartment complex in the morning, in front of a small guard booth with a sliding glass window, a black luxury sedan parked nearby`

---

## 2단계. 이미지 프롬프트

### 키프레임 (클립 1 시작 프레임)

**장면 설명:** 아침 아파트 주차장 경비실 앞. 화면 앞쪽에 김 사장이 등을 3/4쯤 보인 채 빈 커피컵을 쥔 손을 치켜들고 있다.
화면 중앙 뒤쪽에 최 할아버지가 정면에 가깝게 서서, 모욕을 참는 굳은 얼굴로 김 사장을 바라본다. 옆에 검은 외제차.

**구도를 고른 이유:** 가해자의 손과 피해자의 얼굴을 한 화면에 담아 첫 프레임만으로 갈등이 읽히고, 주인공 얼굴·의상이 정면으로 고정된다.

```
Vertical 9:16 photorealistic still frame from a Korean TV drama, cinematic morning light, shallow depth of field.
Scene: the outdoor parking lot of a Korean apartment complex in the morning, in front of a small guard booth with a sliding glass window, a black luxury sedan parked nearby.
Main character, center background, almost facing the camera: a Korean man in his early 70s with short thin grey hair, deep wrinkles, a calm dignified face, silver wire-rimmed glasses, wearing a navy blue security guard uniform jacket with a white name badge on the chest and a navy cap.
His face is clearly visible; jaw tight, lips pressed together, eyes steady, quietly holding back humiliation. He stands upright with hands at his sides.
Foreground left, back three-quarter view, slightly out of focus: a Korean man in his mid 40s with slicked-back black hair, a sharp arrogant face, wearing a black designer polo shirt and a gold wristwatch, raising an empty paper coffee cup in his right hand, about to throw it on the ground.
Composition: over-the-shoulder medium shot at eye level, the guard framed between the foreground man's arm and the sedan. The moment right before the throw.
Style: realistic Korean drama, natural skin texture, 35mm lens look.
No text, no subtitles, no captions, no logos, no watermark.
```

### 인물 레퍼런스 시트

```
Character reference image, vertical 9:16, photorealistic.
A Korean man in his early 70s with short thin grey hair, deep wrinkles, a calm dignified face, silver wire-rimmed glasses, wearing a navy blue security guard uniform jacket with a white name badge on the chest and a navy cap.
Front-facing upper body, neutral expression, standing straight, plain light grey studio background, soft even lighting.
No text, no logos, no watermark.
```

```
Character reference image, vertical 9:16, photorealistic.
A Korean man in his mid 40s with slicked-back black hair, a sharp arrogant face, wearing a black designer polo shirt and a gold wristwatch, holding a smartphone.
Front-facing upper body, neutral expression, standing straight, plain light grey studio background, soft even lighting.
No text, no logos, no watermark.
```

### 반전 인서트 (편집에서 클립 3 뒤에 1.5초 삽입)

```
Vertical 9:16 photorealistic close-up insert shot.
An elderly man's wrinkled hand in a navy uniform sleeve holding an official Korean property registration certificate on top of a lease contract and a formal notice letter.
The owner field of the certificate shows the Korean name "최○○" in large clear print; all other text is small and softly blurred.
Shallow depth of field, morning daylight, realistic paper texture.
No watermark, no subtitles.
```
> 이름이 뭉개지면 편집에서 "소유자: 최○○", "월세 3개월 연체 내용증명" 그래픽을 1초 이상 얹는다.

---

## 3단계. Veo 3 클립 프롬프트

### 클립 1 (0~8초) — 훅

| 동작 | 표정 | 카메라 | 대사 |
|---|---|---|---|
| 김 사장이 컵을 바닥에 던짐 → 할아버지가 말없이 허리 굽혀 주움 → 김 사장이 휴대폰으로 촬영 | 김: 비웃음 / 최: 무표정, 눈만 내리깔기 | 고정 → 느린 줌인 | 김 2줄 |

```
Vertical 9:16, photorealistic Korean TV drama, 8 seconds, continuous shot.
Setting: the outdoor parking lot of a Korean apartment complex in the morning, in front of a small guard booth with a sliding glass window, a black luxury sedan parked nearby.
Characters:
- Guard: a Korean man in his early 70s with short thin grey hair, deep wrinkles, a calm dignified face, silver wire-rimmed glasses, wearing a navy blue security guard uniform jacket with a white name badge on the chest and a navy cap.
- Resident: a Korean man in his mid 40s with slicked-back black hair, a sharp arrogant face, wearing a black designer polo shirt and a gold wristwatch, holding a smartphone.

[0-3s] The resident throws the empty paper coffee cup onto the asphalt; it bounces at the guard's feet. Camera: static over-the-shoulder.
The resident shouts in Korean, angry and rude: "야! 할아버지, 이거 주워! 당장!"

[3-8s] The guard silently bends down and picks up the cup, eyes lowered, face expressionless. The resident raises his smartphone to film him and sneers. Camera: slow push-in toward the guard.
The resident says in Korean, sneering: "경비 주제에 눈 똑바로 뜨네?"

Keep the faces and outfits exactly the same as the start frame.
Audio: No background music. Only Korean dialogue and natural ambient sound: a plastic cup bouncing on asphalt, light wind, a distant car passing.
No subtitles, no captions, no on-screen text, no watermark.
```

**Flow 설정 메모**
- 모드: Frames to Video
- 시작 프레임: 키프레임
- 레퍼런스: 없음 (시작 프레임으로 충분)
- 비율 9:16 · 8초 · 생성 개수 1
- 확인: 첫 대사가 김 사장 입에서 나오는지, 컵 소리

### 클립 2 (8~16초) — 갈등 고조

| 동작 | 표정 | 카메라 | 대사 |
|---|---|---|---|
| 김 사장이 손가락질하며 무릎 요구 → 할아버지 짧은 한숨 → 동료 경비가 고개 저음 → 할아버지가 천천히 무릎을 굽히기 시작 | 김: 의기양양 / 최: 체념한 듯 침착 / 동료: 안타까움 | 미디엄 투샷 → 할아버지 쪽 느린 팬 | 김 1줄 |

```
Continue the same scene in the same parking lot. Vertical 9:16, photorealistic Korean TV drama, 8 seconds.
Characters:
- Guard: a Korean man in his early 70s with short thin grey hair, deep wrinkles, a calm dignified face, silver wire-rimmed glasses, wearing a navy blue security guard uniform jacket with a white name badge on the chest and a navy cap, holding the crushed paper cup.
- Resident: a Korean man in his mid 40s with slicked-back black hair, a sharp arrogant face, wearing a black designer polo shirt and a gold wristwatch, holding a smartphone.
- Colleague: a Korean man in his 60s in the same navy blue security guard uniform without a cap, standing at the guard booth door.

[0-4s] Medium two-shot. The resident points at the ground with his phone still recording, smug.
The resident says in Korean, arrogant and loud: "관리소장한테 한마디면 끝이야. 무릎 꿇고 사과해."

[4-8s] The guard lets out a short quiet sigh. In the background the colleague slowly shakes his head. The guard begins to bend one knee very slowly, his right hand moving toward the inside of his jacket. Camera: slow pan and push-in toward the guard.

Same faces and outfits as before.
Audio: No background music. Only Korean dialogue and natural ambient sound: a quiet sigh, light wind, fabric rustling.
No subtitles, no captions, no on-screen text, no watermark.
```

**Flow 설정 메모**
- 모드: Extend (클립 1에 이어서) — 경계가 튀면 클립 1 마지막 프레임으로 Frames to Video
- 레퍼런스: 동료 경비가 새로 등장하므로 Ingredients를 쓸 경우 인물 시트 A·B 추가
- 비율 9:16 · 8초 · 생성 개수 1
- 확인: 동료 경비가 대사를 하지 않는지, 마지막 프레임이 "무릎 굽히며 안주머니로 손" 상태인지

### 클립 3 (16~24초) — 반전

| 동작 | 표정 | 카메라 | 대사 |
|---|---|---|---|
| 무릎을 굽히던 할아버지가 멈추고 안주머니에서 서류 봉투를 꺼내며 일어섬 → 봉투를 내밀며 말함 → 김 사장이 받아 들여다봄 | 최: 처음으로 눈을 들어 똑바로 봄, 차분 / 김: 비웃음 → 당황 | 할아버지 클로즈업으로 푸시인 → 김 사장 리액션 | 최 1줄 |

```
Continue the same scene. Vertical 9:16, photorealistic Korean TV drama, 8 seconds.
Characters:
- Guard: a Korean man in his early 70s with short thin grey hair, deep wrinkles, a calm dignified face, silver wire-rimmed glasses, wearing a navy blue security guard uniform jacket with a white name badge on the chest and a navy cap.
- Resident: a Korean man in his mid 40s with slicked-back black hair, a sharp arrogant face, wearing a black designer polo shirt and a gold wristwatch, holding a smartphone.

[0-4s] Close-up on the guard. He stops halfway down, pulls a brown document envelope from the inside pocket of his uniform, and stands up straight. For the first time he looks directly into the resident's eyes, calm and firm. Camera: slow push-in to a close-up of his face.
The guard says in Korean, in a calm low voice, without raising it: "무릎 꿇을 사람은 김 사장님 같은데요."

[4-8s] He hands over the envelope. The resident takes out the papers and looks down at them; his smirk freezes and fades. Camera: cut to a medium close-up of the resident's reaction. The papers show no legible text.

Same faces and outfits as before.
Audio: No background music. Only Korean dialogue and natural ambient sound: paper sliding out of an envelope, pages flipping.
No subtitles, no captions, no on-screen text, no watermark.
```

**Flow 설정 메모**
- 모드: Extend, 또는 클립 2 마지막 프레임으로 Frames to Video
- 레퍼런스: 얼굴이 흔들리면 Ingredients에 인물 시트 A·B
- 확인: 할아버지 목소리가 낮고 차분한지, 서류에 엉뚱한 글자가 크게 찍히지 않았는지
- 편집: 이 클립 뒤에 반전 인서트 이미지 1.5초

### 클립 4 (24~32초) — 마무리

| 동작 | 표정 | 카메라 | 대사 |
|---|---|---|---|
| 김 사장 얼굴이 하얗게 질리고 휴대폰이 손에서 미끄러져 떨어짐 → 할아버지가 내용증명 한 장을 차 보닛에 톡 내려놓고 말함 → 돌아서 경비실로 들어가 문을 닫음 | 김: 창백, 입 벌어짐 / 최: 담담 | 김 사장 클로즈업 → 할아버지 뒷모습 따라가는 느린 팬 | 최 1줄 |

```
Continue the same scene. Vertical 9:16, photorealistic Korean TV drama, 8 seconds.
Characters:
- Guard: a Korean man in his early 70s with short thin grey hair, deep wrinkles, a calm dignified face, silver wire-rimmed glasses, wearing a navy blue security guard uniform jacket with a white name badge on the chest and a navy cap.
- Resident: a Korean man in his mid 40s with slicked-back black hair, a sharp arrogant face, wearing a black designer polo shirt and a gold wristwatch.

[0-3s] Close-up of the resident: his face goes pale, mouth slightly open; his smartphone slips from his hand and clatters on the asphalt. Camera: static close-up.

[3-6s] The guard calmly taps a single sheet of paper down on the hood of the black sedan.
The guard says in Korean, calm and dry: "다음 달 말까지 짐 빼세요. 커피는 본인이 치우시고요."

[6-8s] The guard turns and walks back into the guard booth; the sliding door closes behind him. The resident stands frozen. Camera: slow pan following the guard, ending on the frozen resident in the foreground.

Same faces and outfits as before.
Audio: No background music. Only Korean dialogue and natural ambient sound: a phone hitting asphalt, paper tapping on a car hood, footsteps, a sliding door closing.
No subtitles, no captions, no on-screen text, no watermark.
```

**Flow 설정 메모**
- 모드: Extend, 또는 클립 3 마지막 프레임으로 Frames to Video
- 비율 9:16 · 8초 · 생성 개수 1
- 확인: 대사 두 문장이 잘리지 않는지 (잘리면 "커피는 본인이 치우세요."로 줄여 재생성)

---

## 편집 체크리스트

- [ ] 클립 1~4 이어붙이고 32초 → 30초로 다듬기
- [ ] 클립 3 뒤에 반전 인서트 1.5초 (이름 "최○○"이 1초 이상 정확히 보이게, 필요하면 그래픽으로 덮기)
- [ ] 편집 자막: 0초 "70대 경비원한테 무릎 꿇으라는 입주민" / 클립 2 "매일 아침 이 장면을 참고 있었습니다" / 인서트 "이 건물 주인, 사실은 경비 아저씨였습니다"
- [ ] 엔딩 카드: "갑질은 대부분 자기 집 주인이 누군지 모를 때 일어납니다"
- [ ] 음향: 컵 떨어지는 소리로 시작, 반전에서 종이 넘기는 소리 강조
- [ ] 발음이 나쁜 대사는 자막으로 보완하거나 해당 클립만 재생성
