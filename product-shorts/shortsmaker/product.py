"""상품 정보 불러오기: JSON / CSV / 상품 페이지 URL(og 태그)."""
from __future__ import annotations

import csv
import json
import re
from dataclasses import dataclass, field, asdict
from pathlib import Path
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"


@dataclass
class Product:
    name: str
    price: str = ""                 # "19,900"
    original_price: str = ""        # 할인 전 가격(선택)
    features: list[str] = field(default_factory=list)
    images: list[str] = field(default_factory=list)   # 로컬 경로 또는 URL
    link: str = ""                  # 구매/제휴 링크
    pain: str = ""                  # 고객이 겪는 불편 ("욕실 물때")
    target: str = ""                # 타깃 ("자취생")
    cta: str = "고정댓글 링크에서 확인하세요"
    description: str = ""
    affiliate: bool | None = None   # None이면 링크로 자동 판단(쿠팡)

    @property
    def is_affiliate(self) -> bool:
        if self.affiliate is not None:
            return self.affiliate
        return "coupang" in self.link or "link.coupang" in self.link

    def discount_rate(self) -> int | None:
        p, o = _num(self.price), _num(self.original_price)
        if p and o and o > p:
            return round((o - p) / o * 100)
        return None

    def to_dict(self) -> dict:
        return asdict(self)


def _num(s: str) -> int | None:
    d = re.sub(r"[^\d]", "", s or "")
    return int(d) if d else None


def _split(v) -> list[str]:
    if isinstance(v, list):
        return [str(x).strip() for x in v if str(x).strip()]
    return [x.strip() for x in str(v or "").split("|") if x.strip()]


def from_dict(d: dict, base_dir: Path | None = None) -> Product:
    known = Product.__dataclass_fields__.keys()
    data = {k: v for k, v in d.items() if k in known}
    data["features"] = _split(d.get("features"))
    imgs = _split(d.get("images"))
    if base_dir:
        imgs = [i if i.startswith("http") or Path(i).is_absolute() else str(base_dir / i) for i in imgs]
    data["images"] = imgs
    for k in ("price", "original_price"):
        if data.get(k) not in (None, ""):
            n = _num(str(data[k]))
            data[k] = f"{n:,}" if n is not None else str(data[k])   # 9900 → 9,900
    if isinstance(data.get("affiliate"), str):
        data["affiliate"] = data["affiliate"].lower() in ("1", "true", "y", "yes")
    return Product(**data)


def load_products(path: str) -> list[Product]:
    p = Path(path)
    if p.suffix.lower() == ".csv":
        with p.open(encoding="utf-8-sig") as f:
            return [from_dict(row, p.parent) for row in csv.DictReader(f) if row.get("name")]
    raw = json.loads(p.read_text(encoding="utf-8"))
    items = raw if isinstance(raw, list) else [raw]
    return [from_dict(x, p.parent) for x in items]


def from_url(url: str) -> Product:
    """상품 페이지의 og 메타 태그로 이름·이미지·가격을 채운다.
    쇼핑몰에 따라 봇 차단으로 실패할 수 있으니 그땐 JSON으로 직접 입력하세요."""
    r = requests.get(url, headers={"User-Agent": UA, "Accept-Language": "ko-KR"}, timeout=20)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")

    def meta(*names):
        for n in names:
            t = soup.find("meta", attrs={"property": n}) or soup.find("meta", attrs={"name": n})
            if t and t.get("content"):
                return t["content"].strip()
        return ""

    name = meta("og:title", "twitter:title") or (soup.title.string.strip() if soup.title else "상품")
    desc = meta("og:description", "description")
    price = meta("product:price:amount", "og:price:amount")
    imgs = [urljoin(url, m["content"]) for m in soup.find_all("meta", attrs={"property": "og:image"}) if m.get("content")]
    return Product(name=name, price=price, images=imgs, link=url, description=desc)
