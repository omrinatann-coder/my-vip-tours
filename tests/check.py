#!/usr/bin/env python3
"""Checks dist/ after a build: old URLs exist, internal links resolve, SEO tags are present.

    python3 build.py && python3 tests/check.py
"""
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

DIST = Path(__file__).resolve().parent.parent / "dist"
OLD_URLS = ["/", "/ben-gurion-airport-transfers", "/private-driver-israel", "/israel-private-tours",
            "/private-transportation-israel", "/accessible-transportation", "/israel-family-transportation",
            "/19-passenger-minibus-israel", "/hasaot-iruvim"]


def resolve(path):
    path = path.split("#")[0].split("?")[0]
    if path == "/":
        return DIST / "index.html"
    for c in (DIST / path.lstrip("/"), DIST / (path.lstrip("/") + ".html")):
        if c.is_file():
            return c
    return None


class P(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self.meta, self.alts, self.h1, self.ids, self.title = [], {}, {}, 0, set(), ""
        self._t = False

    def handle_starttag(self, tag, a):
        a = dict(a)
        if "id" in a:
            self.ids.add(a["id"])
        if tag in ("a", "link", "script") and (a.get("href") or a.get("src")):
            self.links.append(a.get("href") or a.get("src"))
        if tag == "meta" and a.get("name"):
            self.meta[a["name"]] = a.get("content")
        if tag == "link" and a.get("rel") == "canonical":
            self.meta["canonical"] = a["href"]
        if tag == "link" and a.get("rel") == "alternate":
            self.alts[a["hreflang"]] = a["href"]
        if tag == "h1":
            self.h1 += 1
        self._t = tag == "title"

    def handle_data(self, d):
        if self._t:
            self.title += d

    def handle_endtag(self, tag):
        self._t = False


errors = []
for u in OLD_URLS + ["/en" + (u if u != "/" else "") for u in OLD_URLS]:
    if not resolve(u):
        errors.append(f"missing page {u}")

titles, descs = {}, {}
for f in DIST.rglob("*.html"):
    rel = "/" + str(f.relative_to(DIST))
    p = P()
    p.feed(f.read_text(encoding="utf-8"))
    for l in p.links:
        if l.startswith("#"):
            if l[1:] and l[1:] not in p.ids:
                errors.append(f"{rel}: anchor {l} not on page")
        elif l.startswith("/") and not l.startswith("//") and not resolve(l):
            errors.append(f"{rel}: broken link {l}")
    if f.name == "404.html":
        continue
    if p.h1 != 1:
        errors.append(f"{rel}: {p.h1} h1 tags")
    if not 10 <= len(p.title) <= 110:
        errors.append(f"{rel}: title length {len(p.title)}")
    d = p.meta.get("description") or ""
    if not 50 <= len(d) <= 200:
        errors.append(f"{rel}: description length {len(d)}")
    if set(p.alts) != {"he", "en", "x-default"}:
        errors.append(f"{rel}: hreflang {sorted(p.alts)}")
    canon = p.meta.get("canonical", "")
    if canon.endswith(".html") or (canon.endswith("/") and canon.count("/") > 3):
        errors.append(f"{rel}: bad canonical {canon}")
    titles.setdefault(p.title, []).append(rel)
    descs.setdefault(d, []).append(rel)

errors += [f"duplicate title on {v}" for v in titles.values() if len(v) > 1]
errors += [f"duplicate description on {v}" for v in descs.values() if len(v) > 1]
sm = (DIST / "sitemap.xml").read_text(encoding="utf-8")
for loc in re.findall(r"<loc>https://my-vip-tours.com([^<]*)</loc>", sm):
    if not resolve(loc or "/"):
        errors.append(f"sitemap lists missing {loc}")

print("\n".join(errors) or f"OK: {len(list(DIST.rglob('*.html')))} html files checked")
sys.exit(1 if errors else 0)
