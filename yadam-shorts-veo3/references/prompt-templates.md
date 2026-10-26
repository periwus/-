# 프롬프트 템플릿

`< >` 부분만 바꿔 쓴다.

---

## 1단계 출력 형식 (대본)

```
<대본 제목>

스토리 한 줄 요약:
<누가, 어떤 갑질을 참다가, 무엇이 드러나 판세가 뒤집히는지 1~2문장>

[0~3초] 훅
화면: <첫 동작>
<인물>(<말투>): "<대사>"
자막(편집용): "<훅 자막>"

[3~12초] 갈등 고조
화면: <주인공이 참는 동작 / 가해자의 조롱>
<인물>: "<대사>"
연출: <표정, 목격자 반응>

[12~22초] 절정·반전
화면: <반전 직전 동작 → 증거 공개>
<주인공>: "<반전 대사>"
화면 전환: <증거 클로즈업 — 핵심 글자 1초 이상>

[22~30초] 반전 마무리
화면: <가해자 표정 붕괴>
<주인공>(<동작>): "<펀치라인>"
엔딩 카드 자막(편집용): "<교훈 한 줄>"

[제작 메모]
- 반전 핵심 컷:
- 주인공 톤:
- 음향 포인트:
```

## 1-B 출력 형식 (8초 클립 배치표)

| 클립 | 구간 | 원본 대본 구간 | 장소·구도 | 대사 (음절 수) |
|---|---|---|---|---|
| 1 | 0~8초 | 0~3초 훅 + 갈등 시작 | | |
| 2 | 8~16초 | 갈등 고조 | | |
| 3 | 16~24초 | 절정·반전 | | |
| 4 | 24~32초 | 반전 마무리 | | |

대사를 줄였다면 아래 표를 함께 준다.

| 원문 | 수정본 | 이유 |
|---|---|---|

---

## 2단계 — 키프레임 (Flow 이미지 생성 / Gemini 나노바나나)

```
Vertical 9:16 photorealistic still frame from a Korean TV drama, cinematic lighting, shallow depth of field.
Scene: <장소, 시간대, 날씨>.
Main character: <캐릭터 앵커 문장 — 나이, 얼굴, 머리, 안경, 의상, 색>.
His face is clearly visible, almost facing the camera, <표정 — e.g. holding back humiliation, jaw tight, eyes lowered>.
Body pose: <동작 직전의 자세 — e.g. just about to bend down>.
Other character: <상대역 묘사, 위치 — e.g. in the foreground, back three-quarter view, pointing at the floor>.
Props: <훅에 필요한 소품>.
Composition: <샷 크기, 카메라 높이, 인물 배치>. The moment right before the action starts.
Style: realistic Korean drama, natural skin texture, 35mm lens look.
No text, no subtitles, no captions, no logos, no watermark.
```

## 2단계 — 인물 레퍼런스 시트

```
Character reference image, vertical 9:16, photorealistic.
<캐릭터 앵커 문장>.
Front-facing upper body, neutral expression, standing straight, plain light grey studio background, soft even lighting.
Same outfit as described, every detail clearly visible.
No text, no logos, no watermark.
```

## 2단계 — 반전 인서트 (서류·소품)

```
Vertical 9:16 photorealistic close-up insert shot.
<손과 소품 묘사 — e.g. an elderly man's wrinkled hand holding an official Korean property registration document>.
<글자 지시 — e.g. The owner field shows the Korean name "최○○" in large clear print; the rest of the text is small and blurred.>
Shallow depth of field, warm indoor light, realistic paper texture.
No watermark, no subtitles.
```
> 글자가 뭉개지면 편집에서 그래픽으로 덮는다.

---

## 3단계 — Veo 3 클립 프롬프트

```
Vertical 9:16, photorealistic Korean TV drama, 8 seconds, continuous shot.
Setting: <장소 — 클립 1이 아니거나 새 장소면 구체적으로>.
Characters:
- <A 캐릭터 앵커 문장>
- <B 캐릭터 앵커 문장>

[0-<n>s] <동작>. <표정>. Camera: <고정 / slow push-in / pan left / handheld>.
<B> says in Korean, <말투>: "<대사>"

[<n>-8s] <동작>. <표정 변화>. Camera: <움직임>.
<A> says in Korean, <말투>: "<대사>"

Keep the faces and outfits exactly the same as the reference / start frame.
Audio: No background music. Only Korean dialogue and natural ambient sound: <현장음>.
No subtitles, no captions, no on-screen text, no watermark.
```

### Flow 설정 메모 (클립마다 붙이기)

```
- 모드: <Frames to Video / Ingredients to Video / Extend>
- 시작 프레임: <키프레임 / 클립 N 마지막 프레임 / 없음>
- 레퍼런스(Ingredients): <인물 시트 A, B / 없음>
- 비율: 9:16 · 길이: 8초 · 생성 개수: 1
- 확인할 점: <입 모양, 화자, 글자 등>
```

### Extend용 짧은 프롬프트

Extend는 직전 장면을 이어받으므로 인물 소개를 줄이고 "다음에 일어나는 일"만 쓴다.

```
Continue the same shot. <동작>. Camera: <움직임>.
<인물> says in Korean, <말투>: "<대사>"
Same characters, same outfits. No background music, only dialogue and ambient sound: <현장음>.
No subtitles, no on-screen text.
```
