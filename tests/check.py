#!/usr/bin/env python3
"""Checks dist/ after a build:
- every URL of the old Base44 site is a page or redirects to one,
- internal links resolve, each page has one h1, a title and a description,
- hreflang links are mutual, sitemap entries exist, no duplicate titles/descriptions.

    python3 build.py && python3 tests/check.py
"""
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

DIST = Path(__file__).resolve().parent.parent / "dist"

# The page list from the Base44 export (16 Nov 2026). /blog/:id is checked via redirects.map.
OLD_URLS = """/ /AdminPanel /ConfirmBooking /Home /ServiceAreas /monit-yerushalayim-natbag /monit-tel-aviv-natbag
/monit-yerushalayim-tel-aviv /hasaot-chasuna /hasaot-bar-mitzva /minibus-hashara /nahag-prati /siur-yerushalayim
/tiyul-yam-hamelach /tiyul-galil /tiyul-eilat /hasaot-iruvim /rechavim-memugnay-yeri /rechavei-yukra /hasaot-meforsamim
/ben-gurion-airport-transfers /private-driver-israel /private-transportation-israel /israel-private-tours
/israel-family-transportation /19-passenger-minibus-israel /accessible-transportation /hasaot-menatbag
/israel-transportation-services /vip-transportation-israel /hasaot-beisrael /blog /hasaot-haifa /hasaot-beer-sheva
/hasaot-netanya /hasaot-ashdod /hasaot-rishon-lezion /hasaot-petah-tikva /hasaot-yerushalayim /hasaot-tel-aviv
/israel-vip-transportation-miami /israel-vip-transportation-new-york /israel-vip-transportation-canada
/israel-vip-transportation-russia""".split()
OLD_BLOG_POSTS = 53

REDIRECTS = dict(line.rstrip(";").split(" ") for line in (DIST / "redirects.map").read_text().splitlines() if line)


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
        self.links, self.meta, self.alts, self.h1, self.ids, self.title, self._t = [], {}, {}, 0, set(), "", False

    def handle_starttag(self, tag, a):
        a = dict(a)
        if "id" in a:
            self.ids.add(a["id"])
        if tag in ("a", "link", "script") and (a.get("href") or a.get("src")):
            if a.get("rel") not in ("canonical", "alternate"):
                self.links.append(a.get("href") or a.get("src"))
        if tag == "meta" and a.get("name"):
            self.meta[a["name"]] = a.get("content")
        if tag == "link" and a.get("rel") == "canonical":
            self.meta["canonical"] = a["href"]
        if tag == "link" and a.get("rel") == "alternate":
            self.alts[a["hreflang"]] = a["href"].replace("https://my-vip-tours.com", "") or "/"
        if tag == "html":
            self.meta["lang"] = a.get("lang")
        self.h1 += tag == "h1"
        self._t = tag == "title"

    def handle_data(self, d):
        if self._t:
            self.title += d

    def handle_endtag(self, tag):
        self._t = False


errors = []
for u in OLD_URLS:
    if not resolve(u) and not (u in REDIRECTS and resolve(REDIRECTS[u])):
        errors.append(f"old URL {u} is neither a page nor a working redirect")
blog_ok = sum(1 for k, v in REDIRECTS.items() if k.startswith("/blog/") and resolve(v))
blog_ok += sum(1 for f in (DIST / "blog").glob("*.html") if re.fullmatch(r"[0-9a-f]{24}\.html", f.name))
if blog_ok != OLD_BLOG_POSTS:
    errors.append(f"{blog_ok} of {OLD_BLOG_POSTS} old blog posts are covered")
for old, new in REDIRECTS.items():
    if resolve(old):
        errors.append(f"{old} is a page and also redirects")
    if not resolve(new):
        errors.append(f"redirect {old} -> {new}: target missing")

pages, titles, descs = {}, {}, {}
for f in DIST.rglob("*.html"):
    rel = "/" + str(f.relative_to(DIST))
    url = "/" if rel == "/index.html" else rel[:-5]
    p = P()
    p.feed(f.read_text(encoding="utf-8"))
    pages[url] = p
    for link in p.links:
        if link.startswith("#"):
            if link[1:] and link[1:] not in p.ids:
                errors.append(f"{url}: anchor {link} not on page")
        elif link.startswith("/") and not link.startswith("//") and not resolve(link):
            errors.append(f"{url}: broken link {link}" + (" (goes through a redirect)" if link in REDIRECTS else ""))
    if f.name == "404.html":
        continue
    if p.h1 != 1:
        errors.append(f"{url}: {p.h1} h1 tags")
    if not 10 <= len(p.title) <= 110:
        errors.append(f"{url}: title length {len(p.title)}")
    d = p.meta.get("description") or ""
    if not 50 <= len(d) <= 200:
        errors.append(f"{url}: description length {len(d)}")
    if p.meta.get("canonical", "").replace("https://my-vip-tours.com", "") not in (url, "/" if url == "/" else None):
        errors.append(f"{url}: canonical {p.meta.get('canonical')}")
    titles.setdefault(p.title, []).append(url)
    descs.setdefault(d, []).append(url)

for url, p in pages.items():
    if not p.alts:
        continue
    lang = p.meta["lang"]
    if p.alts.get(lang) != url or set(p.alts) != {"he", "en", "x-default"}:
        errors.append(f"{url}: bad hreflang {p.alts}")
        continue
    other = p.alts["en" if lang == "he" else "he"]
    q = pages.get(other)
    if not q or q.alts.get(lang) != url:
        errors.append(f"{url}: hreflang partner {other} does not link back")

errors += [f"duplicate title on {v}" for v in titles.values() if len(v) > 1]
errors += [f"duplicate description on {v}" for v in descs.values() if len(v) > 1]
sm = (DIST / "sitemap.xml").read_text(encoding="utf-8")
locs = re.findall(r"<loc>https://my-vip-tours.com([^<]*)</loc>", sm)
for loc in locs:
    if not resolve(loc or "/"):
        errors.append(f"sitemap lists missing {loc}")
if len(locs) != len(pages) - 1:
    errors.append(f"sitemap has {len(locs)} URLs, site has {len(pages) - 1} pages")

print("\n".join(errors) or f"OK: {len(pages)} html files, {len(REDIRECTS)} redirects, all {len(OLD_URLS)} old URLs + {OLD_BLOG_POSTS} old posts covered")
sys.exit(1 if errors else 0)
