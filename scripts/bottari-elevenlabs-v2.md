# 「보따리」 v2 — 일레븐랩스 캐릭터 목소리 · 대사

## 작업 순서
1. **목소리 만들기:** 일레븐랩스 Voice Design에서 캐릭터마다 목소리를 만들어 저장합니다. 설명과 시험 문장은 아래에 있습니다.
2. **대사 소리 만들기:** Text to Speech(Eleven v3)에서 컷마다 해당 캐릭터 목소리를 골라 대사를 넣고, 파일을 컷 번호로 저장합니다. 예: `C25_순자.mp3`
3. **편집에서 맞추기:** 영상의 원래 소리를 끄고 일레븐랩스 대사를 얹습니다. 입 모양이 어긋나면 립싱크 도구로 맞춥니다.

## 1. 캐릭터 목소리 설계 (Voice Design)
설명은 영어로 넣고, 시험 문장은 그 인물의 대사로 넣습니다. 3개씩 나오면 가장 자연스러운 것을 저장하세요. 저장할 이름은 `보따리_순자`처럼 정합니다.

### 순자 (68, 어머니)
설명
```
A Korean woman in her late 60s, native Korean speaker with a standard Seoul accent. Warm, low, slightly husky voice of a mother who ran a market restaurant for decades. Calm, unhurried and dignified, never loud. Speaks plainly with quiet strength and a hint of dry humor. Natural conversational pace, clear studio recording, no background noise.
```
시험 문장
```
김밥이야. 사돈어른들 드시라고. [pause] 아까도 말하려는데 네가 못 하게 하더라.
```

### 민호 (36, 아들)
설명
```
A Korean man in his mid 30s, native Korean speaker with a standard Seoul accent. Clear mid-range office-worker voice, a little tense and self-conscious. Speaks quickly when embarrassed, softens and hesitates when guilty. Natural conversational pace, clear studio recording, no background noise.
```
시험 문장
```
[irritated, under breath] 엄마, 그 보따리 차에 두고 오라니까요. [pause] [quietly] …엄마, 내가 들게.
```

### 지은 (32, 예비 며느리)
설명
```
A Korean woman in her early 30s, native Korean speaker with a standard Seoul accent. Bright, soft and sincere voice, gentle and warm, slightly playful. Sounds kind without being sugary. Natural conversational pace, clear studio recording, no background noise.
```
시험 문장
```
어머님, 아침에 싸 오신 거예요? [laughs softly] 아니요. 저 아침도 못 먹었어요.
```

### 정숙 (61, 예비 사돈 어머니)
설명
```
A Korean woman in her early 60s, native Korean speaker with a polished upper-class Seoul accent. Smooth, refined, slightly nasal voice. Sounds polite and sweet on the surface but condescending underneath. Becomes shrill and flustered when surprised. Natural conversational pace, clear studio recording, no background noise.
```
시험 문장
```
[sweetly] 예단은 하지 마세요. 형편에 무리하실 것 없잖아요. [flustered] 시장에 가게 하신다고…
```

### 강 회장 (64, 예비 사돈 아버지)
설명
```
A Korean man in his mid 60s, native Korean speaker with a standard Seoul accent. Deep, gravelly authoritative voice of a company chairman, but anxious and hurried under pressure. Natural conversational pace, clear studio recording, no background noise.
```
시험 문장
```
늦었습니다. 이 호텔 대표님 뵙기로 해서요. [nervous] 아직. 오늘은 꼭 뵈어야 하는데.
```

### 박 지배인 (52, 호텔 총지배인)
설명
```
A Korean man in his early 50s, native Korean speaker with a standard Seoul accent. Calm, polite, well-trained hotel service voice, clear and respectful, medium-low pitch. Natural conversational pace, clear studio recording, no background noise.
```
시험 문장
```
대표님, 말씀하신 차 준비됐습니다.
```

## 2. 컷별 대사 (Eleven v3 감정 표시 포함)
대괄호 [ ] 안은 읽지 않고 말투로만 반영됩니다. C09, C16은 대사가 없어서 뺐습니다.

| 컷 | 목소리 | 넣을 문장 |
|---|---|---|
| C01 | 민호 | `[irritated, under breath] 엄마, 그 보따리 차에 두고 오라니까요.` |
| C02 | 순자 | `[warmly] 김밥이야. 사돈어른들 드시라고.` |
| C03 | 민호 | `[embarrassed, whispering] 여기 호텔이에요. 창피하게 진짜.` |
| C04 | 지은 | `[kindly] 어머님, 여기 두세요.` |
| C05 | 정숙 | `[politely, condescending] 어머, 직접 싸 오셨어요? 여기 음식 다 나오는데.` |
| C06 | 정숙 | `[casually] 어머님은 무슨 일 하세요?` |
| C07 | 순자 | `[modestly] 저는 시장에서…` |
| C08 | 민호 | `[quickly, cutting in] 작은 가게 하세요. 지금은 거의 쉬시고요.` |
| C10 | 정숙 | `[pitying] 아, 장사하셨구나.` |
| C11 | 정숙 | `[sweetly] 예단은 하지 마세요. 형편에 무리하실 것 없잖아요.` |
| C12 | 순자 | `[calmly] 마음 써 주셔서 고맙네요.` |
| C13 | 지은 | `[curious, warm] 어머님, 아침에 싸 오신 거예요?` |
| C14 | 순자 | `[a little shy] 응. 식었지?` |
| C15 | 지은 | `[mouth half full, bright] 아니요. 저 아침도 못 먹었어요.` |
| C17 | 정숙 | `[scolding, low voice] 지은아, 손으로 그게 뭐니.` |
| C18 | 강 회장 | `[slightly out of breath] 늦었습니다. 이 호텔 대표님 뵙기로 해서요.` |
| C19 | 정숙 | `[eager] 만났어요?` |
| C20 | 강 회장 | `[tense, low] 아직. 오늘은 꼭 뵈어야 하는데.` |
| C21 | 박 지배인 | `[respectfully] 대표님, 말씀하신 차 준비됐습니다.` |
| C22 | 강 회장 | `[stunned] …대표님이세요?` |
| C23 | 민호 | `[stunned whisper] 엄마가?` |
| C24 | 정숙 | `[flustered, trailing off] 시장에 가게 하신다고…` |
| C25 | 순자 | `[plainly, calm] 네. 국밥 팔아서 번 돈이에요.` |
| C26 | 강 회장 | `[nervous] 투자 건은 제가 따로…` |
| C27 | 순자 | `[politely but firmly] 그 얘기는 회사에서 하시죠.` |
| C28 | 순자 | `[pause] [softly, warm] 오늘은 애들 보러 왔어요.` |
| C29 | 민호 | `[hesitant] 엄마, 나한테는 왜…` |
| C30 | 순자 | `[quietly, no blame] 아까도 말하려는데 네가 못 하게 하더라.` |
| C31 | 지은 | `[gently, a little shy] 어머님, 이거 제가 가져가도 되죠?` |
| C32 | 순자 | `[warmly] 그럼.` |
| C33 | 민호 | `[quietly, sincere] …엄마, 내가 들게.` |
| C34 | 순자 | `[lightly, everyday motherly tone] 기울이지 마. 김밥 쏟아진다.` |

## 3. 설정 추천 (Eleven v3)
- 안정성(Stability): **Natural**. 너무 들쑥날쑥하면 Robust로 올립니다.
- 같은 문장을 2~3번 만들어 가장 자연스러운 것을 고릅니다.
- 짧은 대사("그럼.", "엄마가?")는 어색하게 늘어지기 쉬우니, 앞뒤 무음을 편집에서 잘라 씁니다.

## 4. 영상과 맞추는 법
- **이미 만든 영상이 있으면:** 영상 소리를 끄고 일레븐랩스 대사를 얹습니다. 대사 길이가 영상 속 입 움직임과 비슷하면 그대로 쓰고, 많이 어긋나는 컷만 립싱크 도구로 맞춥니다.
- **앞으로 만들 영상:** 영상 프롬프트의 대사 부분은 그대로 둡니다. 입 모양이 대사에 맞게 움직여야 나중에 목소리만 바꿔도 덜 어색합니다.
