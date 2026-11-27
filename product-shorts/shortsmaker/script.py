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
HOOKS = [
    "아직도 {pain} 때문에 고생하세요?",
    "{target} 이거 모르면 진짜 손해예요",
    "이거 하나로 {pain} 끝났습니다",
    "솔직히 {price}원에 이게 된다고요?",
    "요즘 {target} 사이에서 난리 난 물건",
]


def template_script(p: Product, seed: int | None = None) -> Script:
    rnd = random.Random(seed if seed is not None else p.name)
    n_img = max(1, len(p.images))
    pain = p.pain or "매일 하는 이 불편함"
    target = p.target or "자취생"
    hooks = [h for h in HOOKS if ("{price}" not in h or p.price)]
    hook = rnd.choice(hooks).format(pain=pain, target=target, price=p.price)

    scenes = [Scene("hook", hook, _emph(hook, [pain, target, p.price]), 0)]
    if p.pain:
        t = f"매번 {p.pain}, 진짜 스트레스잖아요."
        scenes.append(Scene("problem", t, f"매번 **{p.pain}**…", 1 % n_img))
    scenes.append(Scene("feature", f"그래서 찾은 게 바로 {p.name}입니다.", f"그래서 찾은 **{_short(p.name)}**", 0))
    for i, f in enumerate(p.features[:4]):
        lead = ["첫째,", "둘째,", "셋째,", "그리고"][i]
        scenes.append(Scene("feature", f"{lead} {f}.", f"{f}", (i + 1) % n_img))
    if p.price:
        dr = p.discount_rate()
        if dr:
            t = f"정가 {p.original_price}원인데 지금은 {dr}% 할인해서 {p.price}원이에요."
            c = f"~~{p.original_price}원~~\n**{dr}% 할인 {p.price}원**"
        else:
            t = f"가격도 {p.price}원이면 충분해요."
            c = f"단돈 **{p.price}원**"
        scenes.append(Scene("price", t, c, 0))
    scenes.append(Scene("cta", f"자세한 건 {p.cta}.", f"**{p.cta}**", 0))

    title = f"{hook} | {_short(p.name)}"[:95]
    tags = ["#쇼츠", "#추천템", "#꿀템", f"#{_tag(p.name)}"] + ([f"#{_tag(target)}템"] if target else [])
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
SYSTEM = """너는 조회수 높은 한국 상품 쇼츠(유튜브 쇼츠·릴스·틱톡) 대본 작가다.
규칙:
- 전체 낭독 25~40초. 장면 5~8개, 장면당 낭독 1~2문장(짧고 구어체).
- 1장면은 첫 3초 후킹: 불편 공감, 반전, 가격 충격, 타깃 호명 중 하나.
- 흐름: hook → problem(선택) → feature(제품 소개+핵심 기능 2~4개) → price(가격이 있으면) → cta.
- caption은 화면 자막: 12자 안팎 한두 줄, 핵심 단어는 **두 별표**로 감싼다. 할인 전 가격은 ~~물결~~로 감싸면 취소선이 된다. 줄바꿈은 \\n. 이모지·특수기호(✔↓👇 등)는 쓰지 마라.
- 상품 정보에 없는 효능·수치·후기·인증을 지어내지 마라. 과장 광고 표현(최고, 100%, 완치 등) 금지.
- image는 0부터 시작하는 상품 이미지 번호(이미지 개수 미만).
- title은 60자 이내 후킹 제목, hashtags는 5~8개(#포함), description은 2~4줄 상품 설명."""

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
    info = {k: v for k, v in p.to_dict().items() if k not in ("images", "affiliate") and v}
    info["image_count"] = max(1, len(p.images))
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
    n = max(1, len(p.images))
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
