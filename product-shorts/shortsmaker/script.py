"""쇼츠 대본 생성.
- ANTHROPIC_API_KEY(또는 ant 로그인)가 있으면 Claude가 상품에 맞춰 작성
- 없으면 검증된 상품쇼츠 구조(후킹→불편→기능→가격→CTA) 템플릿으로 작성
"""
from __future__ import annotations

import json
import os
import random
from dataclasses import dataclass, asdict

from .product import Product


@dataclass
class Scene:
    kind: str          # hook | problem | feature | price | cta
    narration: str     # TTS로 읽을 문장
    caption: str       # 화면 자막 (**강조**는 노란색)
    image: int = 0     # 사용할 상품 이미지 번호


@dataclass
class Script:
    title: str
    scenes: list[Scene]
    hashtags: list[str]
    description: str

    def to_dict(self):
        return {"title": self.title, "hashtags": self.hashtags, "description": self.description,
                "scenes": [asdict(s) for s in self.scenes]}

    @classmethod
    def from_dict(cls, d):
        return cls(d["title"], [Scene(**s) for s in d["scenes"]], d.get("hashtags", []), d.get("description", ""))


# ---------------------------------------------------------------- 템플릿 대본
# 원칙: 불편한 상황으로 시작, 낚시·과장 문구 금지, 15~25초, 영상마다 문장 구성이 달라지게.
HOOKS_PAIN = [
    "{pain} 때문에 고민이라면 보세요",
    "{pain}, 이렇게 해결할 수 있어요",
    "{pain} 신경 쓰이는 집이라면",
    "겨울마다 {pain} 겪는 집이라면",
]
HOOKS_TARGET = ["{target}{iramyeon} 한 번쯤 겪는 {pain}"]
HOOKS_PLAIN = ["{short} 실제로 쓰는 모습이에요", "{short}, 어떻게 쓰는지 보여드릴게요"]
CONNECT = [["", "그리고 ", "또 "], ["", "게다가 ", "마지막으로 "], ["", "", ""]]
SEASON_WORDS = ("외풍", "결로", "추위", "난방", "보온", "방한", "냉기", "웃풍", "우풍", "성에")


def _has_batchim(word: str) -> bool:
    ch = word.strip()[-1:] if word.strip() else ""
    return bool(ch) and "가" <= ch <= "힣" and (ord(ch) - 0xAC00) % 28 != 0


def _josa(word: str, with_b: str, without_b: str) -> str:
    return word + (with_b if _has_batchim(word) else without_b)


def template_script(p: Product, seed: int | None = None) -> Script:
    rnd = random.Random(seed if seed is not None else p.name)
    n = max(1, len(p.media))
    short = _short(p.name)
    pain, target = p.pain.strip(), p.target.strip()

    if pain:
        pool = list(HOOKS_PAIN)
        if not any(w in pain for w in SEASON_WORDS):
            pool.remove("겨울마다 {pain} 겪는 집이라면")
        if target:
            pool += HOOKS_TARGET
        hook = rnd.choice(pool).format(pain=pain, target=target, short=short,
                                       iramyeon="이라면" if _has_batchim(target) else "라면")
    else:
        hook = rnd.choice(HOOKS_PLAIN).format(short=short)
    scenes = [Scene("hook", hook, _emph(hook, [pain, short]), 0)]

    # 사용 장면: 장점 최대 3개, 첫 장면에서 제품 이름을 함께 말한다
    conn = rnd.choice(CONNECT)
    for i, f in enumerate(p.features[:3]):
        if i == 0:
            t = f"{_josa(short, '은', '는')} {f}."
            c = f"**{short}**\n{f}"
        else:
            t = f"{conn[i]}{f}."
            c = f
        scenes.append(Scene("feature", t, c, (i + 1) % n))

    # 마무리: 가격 + 프로필 링크 안내를 한 장면에
    cta = p.cta_text
    cta_say = f"제품 정보는 {cta}에 있어요." if cta.startswith("프로필 링크") else f"{cta}."
    if p.price:
        dr = p.discount_rate()
        if dr:
            t = f"지금 {dr}% 할인해서 {p.price}원이에요. {cta_say}"
            c = f"~~{p.original_price}원~~ **{p.price}원**\n{_emph(cta, [cta])}"
        else:
            t = f"가격은 {p.price}원이에요. {cta_say}"
            c = f"**{p.price}원**\n{cta}"
        scenes.append(Scene("price", t, c, 0))
    else:
        scenes.append(Scene("cta", cta_say, f"**{cta}**", 0))

    title = f"{hook} | {short}"[:95]
    tags = ["#살림템", "#생활꿀템", f"#{_tag(p.name)}"] + ([f"#{_tag(target)}템"] if target else [])
    desc = f"{p.name}\n" + "".join(f"- {f}\n" for f in p.features)
    return Script(title, scenes, tags, desc)


def _short(name: str, n: int = 14) -> str:
    """긴 상품명은 단어 단위로 줄인다 (용량·수량 표기 등 뒤쪽을 생략)."""
    if len(name) <= n:
        return name
    out = ""
    for w in name.split():
        if len((out + " " + w).strip()) > n:
            break
        out = (out + " " + w).strip()
    return out or name[:n]


def _tag(s: str) -> str:
    return "".join(ch for ch in s if ch.isalnum())[:15]


def _emph(text: str, words: list[str]) -> str:
    for w in words:
        if w and w in text:
            return text.replace(w, f"**{w}**", 1)
    return text


# ---------------------------------------------------------------- Claude 대본
SYSTEM = """너는 한국 생활용품 쇼츠(유튜브 쇼츠·릴스) 대본 작가다. 채널은 YPP 심사에서
'오해 소지가 있는 제목'과 '반복 콘텐츠'로 거절된 적이 있으니 정직하고 영상마다 다르게 쓴다.
규칙:
- 전체 낭독 15~25초. 장면 4~5개, 장면당 낭독 1문장(짧은 구어체).
- 1장면(hook)은 시청자가 겪는 불편한 상황으로 시작한다. 예: "창문 틈으로 찬바람 들어오는 집이라면".
- 흐름: hook → feature 2~3개(첫 feature에서 제품 이름을 말함) → price(가격이 있으면) 또는 cta.
- 마지막 장면 낭독은 반드시 cta_text를 안내한다. 예: "제품 정보는 프로필 링크 3번에 있어요."
  설명란·댓글 링크로 안내하지 마라(쇼츠에서는 눌리지 않는다).
- caption은 화면 자막: 12자 안팎 한두 줄, 핵심 단어는 **두 별표**로 감싼다. 할인 전 가격은 ~~물결~~로 감싸면 취소선이 된다. 줄바꿈은 \\n. 이모지·특수기호(✔↓👇 등)는 쓰지 마라.
- 금지: 상품 정보에 없는 효능·수치·후기·인증·사연, "보일러보다 따뜻", "난방비 X% 절약", "이거 모르면 손해",
  "난리 난", "역대급", "최고", "100%" 같은 과장·낚시 표현, 가격 충격형 후킹.
- image는 0부터 시작하는 소재 번호(media 목록 길이 미만). media에서 "video"는 상품 영상 클립이니
  후킹·사용 장면에 우선 배치하고, 가격·CTA 장면에는 "image"를 쓰는 편이 좋다.
- title은 영상 내용과 정확히 맞는 50자 이내 제목(낚시 금지), hashtags는 4~6개(#포함), description은 2~4줄 상품 설명."""


SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "required": ["title", "scenes", "hashtags", "description"],
    "properties": {
        "title": {"type": "string"},
        "description": {"type": "string"},
        "hashtags": {"type": "array", "items": {"type": "string"}},
        "scenes": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": ["kind", "narration", "caption", "image"],
                "properties": {
                    "kind": {"type": "string", "enum": ["hook", "problem", "feature", "price", "cta"]},
                    "narration": {"type": "string"},
                    "caption": {"type": "string"},
                    "image": {"type": "integer"},
                },
            },
        },
    },
}


def ai_script(p: Product, model: str = "claude-opus-5-5", style: str = "") -> Script:
    import anthropic

    client = anthropic.Anthropic()
    info = {k: v for k, v in p.to_dict().items() if k not in ("images", "clips", "affiliate") and v}
    info["cta_text"] = p.cta_text
    info["media"] = ["video" if i < len(p.clips) else "image" for i in range(max(1, len(p.media)))]
    prompt = "다음 상품으로 쇼츠 대본을 써줘.\n" + json.dumps(info, ensure_ascii=False, indent=2)
    if style:
        prompt += f"\n\n추가 요청: {style}"
    resp = client.beta.messages.create(
        model=model,
        max_tokens=16000,
        betas=["server-side-fallback-2026-07-01"],
        fallbacks="default",
        system=SYSTEM,
        output_config={"effort": "low", "format": {"type": "json_schema", "schema": SCHEMA}},
        messages=[{"role": "user", "content": prompt}],
    )
    if resp.stop_reason == "refusal":
        raise RuntimeError("Claude가 이 상품 대본 작성을 거절했습니다.")
    text = "".join(b.text for b in resp.content if b.type == "text")
    s = Script.from_dict(json.loads(text))
    n = max(1, len(p.media))
    for sc in s.scenes:
        sc.image = min(max(sc.image, 0), n - 1)
    return s


def has_claude_credentials() -> bool:
    return bool(os.environ.get("ANTHROPIC_API_KEY") or os.environ.get("ANTHROPIC_AUTH_TOKEN"))


def make_script(p: Product, use_ai: str = "auto", model: str = "claude-opus-5-5", style: str = "") -> tuple[Script, str]:
    if use_ai == "on" or (use_ai == "auto" and has_claude_credentials()):
        try:
            return ai_script(p, model, style), "claude"
        except Exception as e:  # 네트워크/키 문제 시 템플릿으로 계속
            if use_ai == "on":
                raise
            print(f"  ! Claude 대본 실패 → 템플릿 사용 ({type(e).__name__}: {e})")
    return template_script(p), "template"
