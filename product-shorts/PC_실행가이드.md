# PC 실행 가이드 (Windows)

명령은 모두 **PowerShell**에 복사해서 붙여넣으면 됩니다.

## 1단계: 프로그램 설치 (처음 한 번, 약 15분)

### ① Python 설치
1. [python.org/downloads](https://www.python.org/downloads/)에서 최신 버전을 내려받아 실행합니다.
2. 설치 첫 화면 아래의 **"Add python.exe to PATH"를 꼭 체크**하고 Install을 누릅니다.

### ② ffmpeg 설치 (영상 만드는 도구)
1. 시작 메뉴에서 **PowerShell**을 열고 아래를 입력합니다.
   ```powershell
   winget install Gyan.FFmpeg
   ```
2. 설치가 끝나면 **PowerShell 창을 닫았다가 새로 엽니다.** 그래야 ffmpeg가 인식됩니다.

### ③ 프로그램 내려받기
1. 브라우저에서 GitHub 저장소 `periwus/-`의 **`claude/amazing-ride-aatota` 브랜치**로 갑니다.
2. 초록색 **Code → Download ZIP**을 눌러 받고, 원하는 곳에 압축을 풉니다.

### ④ 필요한 부품 설치
1. 압축을 푼 폴더 안의 **`product-shorts` 폴더**를 탐색기로 엽니다.
2. **주소창에 `powershell`이라고 치고 Enter**를 누르면, 그 폴더에서 PowerShell이 열립니다.
3. 아래를 실행합니다.
   ```powershell
   py -m pip install -r requirements.txt
   ```

## 2단계: 예시로 시험 실행

```powershell
py shorts.py examples\product.json
```
- `output` 폴더에 영상, 썸네일, `upload.txt`가 생기면 성공입니다.
- **음성이 나오는지** 꼭 확인하세요. 개발 환경에서는 음성 서버가 막혀 있어 확인하지 못한 부분입니다.
- 첫 실행 때 자막 폰트를 자동으로 내려받느라 조금 걸립니다.

## 3단계: 내 상품으로 만들기

1. `product-shorts` 안에 `my` 폴더를 만들고, 직접 찍은 영상과 사진을 넣습니다.
2. 메모장으로 `my\방풍비닐.json`을 만들어 아래 내용을 붙여넣습니다. **장점(features)은 실제 상품 상세페이지에 적힌 내용으로 바꾸세요.**
   ```json
   {
     "name": "지퍼형 창문 방풍비닐",
     "price": "12,900",
     "features": ["지퍼로 열고 닫아 환기 가능", "양면테이프로 붙이는 방식"],
     "clips": ["붙이는장면.mp4", "지퍼여는장면.mp4"],
     "images": ["완성사진.jpg"],
     "link": "쿠팡 파트너스 링크",
     "link_no": "1",
     "pain": "창문 틈 찬바람",
     "target": "구축 아파트"
   }
   ```
3. 실행합니다.
   ```powershell
   py shorts.py my\방풍비닐.json
   ```
4. 대본을 고치고 싶으면 `output\지퍼형_창문_방풍비닐\script.json`을 메모장으로 고친 뒤 다시 실행합니다.
   ```powershell
   py shorts.py my\방풍비닐.json --script output\지퍼형_창문_방풍비닐\script.json
   ```

**팁**
- 엑셀로 CSV를 만들 때는 **"CSV UTF-8"** 형식으로 저장해야 한글이 안 깨집니다.
- 남자 목소리는 `--voice injoon`, 배경음악은 `--bgm 음악.mp3`를 붙입니다.
- `link_no`는 채널 프로필 링크 번호입니다. 상품마다 고정하고, 한 번 쓴 번호는 다시 쓰지 마세요.

## 4단계: 유튜브 업로드 준비 (처음 한 번, 약 10분)

1. [Google Cloud 콘솔](https://console.cloud.google.com/)에서 새 프로젝트를 만듭니다.
2. **API 및 서비스 → 라이브러리**에서 `YouTube Data API v3`를 찾아 **사용**을 누릅니다.
3. **OAuth 동의 화면**: 유형은 *외부*로 정하고, **테스트 사용자**에 살림픽 채널의 구글 계정을 추가합니다.
4. **사용자 인증 정보 → OAuth 클라이언트 ID → 데스크톱 앱**을 만들고, JSON을 받아 `product-shorts` 폴더에 **`client_secret.json`**이라는 이름으로 저장합니다.

> `client_secret.json`과 `token.json`은 비밀번호와 같습니다. 다른 사람에게 보내거나 인터넷에 올리지 마세요.

## 5단계: 업로드

```powershell
py upload.py output
```
1. 브라우저가 열리면 살림픽 채널의 계정으로 로그인합니다.
   - **"Google에서 확인하지 않은 앱"** 화면이 나오면 **고급 → (앱 이름)(으)로 이동**을 누릅니다. 내가 만든 앱이라 괜찮습니다.
2. 창에 **"업로드 채널: 살림픽 (UCgS9…)"**이 나오는지 확인합니다. 다른 채널이면 자동으로 멈춥니다.
3. 기본은 **비공개 업로드**입니다. 스튜디오에서 영상, 음성, 자막을 확인한 뒤 공개로 바꾸세요.
   - 감사를 받지 않은 API 프로젝트는 어차피 비공개로만 올라갑니다.
4. 예약 업로드는 이렇게 합니다.
   ```powershell
   py upload.py output --publish-at "2026-12-02 19:00"
   ```
5. 업로드한 뒤에는 `upload.txt`의 **[채널 프로필 링크에 넣을 것]**을 채널 프로필 링크에 추가합니다.

## 자주 막히는 곳

| 증상 | 해결 |
|---|---|
| `py`를 찾을 수 없음 | Python을 다시 설치하면서 PATH 체크하기 |
| `ffmpeg가 필요합니다` | PowerShell 창을 새로 열기. 그래도 안 되면 PC 재시작 |
| 음성 없이 "TTS 연결 실패" | 인터넷 연결이나 회사·학교 방화벽 확인 |
| 일주일쯤 뒤 업로드 로그인 오류 | `token.json`을 지우고 다시 실행해 로그인하기 |
| "정해 둔 채널이 아닙니다" | `token.json`을 지우고 살림픽 채널 계정으로 다시 로그인하기 |
| 한글이 깨진 CSV | 엑셀에서 "CSV UTF-8"로 다시 저장 |

'일주일 뒤 로그인 오류'는 Google OAuth 동의 화면이 '테스트' 상태여서 생기는 일입니다. 테스트 상태에서는 로그인이 7일마다 만료됩니다. 동의 화면을 '프로덕션'으로 바꾸면 덜 자주 풀립니다.

오류가 나면 PowerShell에 나온 메시지를 그대로 복사해서 Claude에게 보여 주세요.
