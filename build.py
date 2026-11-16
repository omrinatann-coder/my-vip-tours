#!/usr/bin/env python3
"""Static site generator for my-vip-tours.com. No dependencies (Python 3.9+).

    python3 build.py            # writes dist/
    python3 build.py --serve    # build, then serve dist/ on http://127.0.0.1:8080

Every URL keeps the language it had on the old site (content/pages.py).
Each page is written as <path>.html; nginx serves /<path> with
`try_files $uri $uri.html`, so URLs have no extension and no trailing slash.
Old URLs without a page are 301-redirected via dist/redirects.map (nginx map).
"""
import hashlib
import html
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CONTENT = ROOT / "content"
DIST = ROOT / "dist"
sys.path.insert(0, str(CONTENT))

import business as B  # noqa: E402
from articles import ARTICLES  # noqa: E402
from legacy import KEPT_ARTICLES, REDIRECTS  # noqa: E402
from pages import PAGES as CONTENT_PAGES  # noqa: E402

E = html.escape
REVIEWS = json.loads((CONTENT / "reviews.json").read_text(encoding="utf-8"))
TOURS = json.loads((CONTENT / "tours.json").read_text(encoding="utf-8"))
FAQ = [f for f in json.loads((CONTENT / "faq.json").read_text(encoding="utf-8")) if not f.get("hidden")]
FLEET = {v["id"]: v for v in B.FLEET}

CSS = (ROOT / "assets" / "style.css").read_text(encoding="utf-8")
JS_BYTES = (ROOT / "assets" / "site.js").read_bytes()
JS_URL = "/assets/site.js?v=" + hashlib.sha256(JS_BYTES).hexdigest()[:10]

# articles.py `service` slug -> page in each language
ARTICLE_SERVICE = {
    "ben-gurion-airport-transfers": {"he": "/hasaot-menatbag", "en": "/ben-gurion-airport-transfers"},
    "private-transportation-israel": {"he": "/hasaot-beisrael", "en": "/private-transportation-israel"},
    "hasaot-iruvim": {"he": "/hasaot-iruvim", "en": "/en/event-transportation"},
    "israel-private-tours": {"he": "/siurim-pratiyim", "en": "/israel-private-tours"},
    "israel-family-transportation": {"he": "/hasaot-beisrael", "en": "/israel-family-transportation"},
    "accessible-transportation": {"he": "/accessible-transportation", "en": "/en/accessible-transportation"},
}

ICONS = {
    "plane": '<path d="M21 16v-2l-8-5V3.5a1.5 1.5 0 0 0-3 0V9l-8 5v2l8-2.5V19l-2 1.5V22l3.5-1 3.5 1v-1.5L13 19v-5.5z"/>',
    "phone": '<path d="M6.6 10.8a15 15 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/>',
    "wa": '<path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm5.3 14.1c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .2-3.3-.7-2.8-1.1-4.5-3.9-4.7-4.1-.1-.2-1.1-1.5-1.1-2.8s.7-2 1-2.3c.2-.3.5-.3.7-.3h.5c.2 0 .4 0 .6.5l.9 2.1c.1.2.1.3 0 .5l-.3.5-.4.4c-.1.1-.3.3-.1.6.2.3.8 1.3 1.7 2.1 1.2 1 2.1 1.3 2.4 1.5.3.1.5.1.6-.1l.9-1c.2-.3.4-.2.6-.1l2 1c.3.1.5.2.5.3.1.1.1.6-.1 1.2z"/>',
    "star": '<path d="m12 2 3.1 6.3 6.9 1-5 4.9 1.2 6.8L12 17.8 5.8 21l1.2-6.8-5-4.9 6.9-1z"/>',
    "pin": '<path d="M12 2a7 7 0 0 0-7 7c0 5 7 13 7 13s7-8 7-13a7 7 0 0 0-7-7zm0 9.5A2.5 2.5 0 1 1 12 6.5a2.5 2.5 0 0 1 0 5z"/>',
    "clock": '<path fill-rule="evenodd" d="M12 2a10 10 0 1 1 0 20 10 10 0 0 1 0-20zm0 2a8 8 0 1 0 0 16 8 8 0 0 0 0-16zm-1 3h2v5.4l3.5 2.1-1 1.7L11 13.6z"/>',
    "user": '<path d="M12 12a5 5 0 1 0 0-10 5 5 0 0 0 0 10zm0 2c-4.4 0-8 2.2-8 5v3h16v-3c0-2.8-3.6-5-8-5z"/>',
    "bus": '<path d="M4 16c0 .9.4 1.7 1 2.2V20a1 1 0 0 0 1 1h1a1 1 0 0 0 1-1v-1h8v1a1 1 0 0 0 1 1h1a1 1 0 0 0 1-1v-1.8c.6-.5 1-1.3 1-2.2V6c0-3.5-3.6-4-8-4S4 2.5 4 6zm3.5 1a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zm9 0a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zM18 11H6V6h12z"/>',
}

IMG_DIR = ROOT / "assets" / "img"


def photo(name, alt, fallback_icon):
    """Card photo from assets/img/<name>.(webp|jpg|jpeg|png); dark placeholder with an icon if it is missing."""
    for ext in ("webp", "jpg", "jpeg", "png"):
        if (IMG_DIR / f"{name}.{ext}").exists():
            return (f'<img src="/assets/img/{name}.{ext}" alt="{E(alt)}" loading="lazy" decoding="async"'
                    ' width="800" height="500">')
    return f'<span class="ph-icon">{icon(fallback_icon)}</span>'


def icon(name, cls="ic"):
    return f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true" focusable="false">{ICONS[name]}</svg>'


def t(lang, key):
    return B.UI[lang][key]


def home_of(lang):
    return "/" if lang == "he" else "/en"


def jsonld(obj):
    return ('<script type="application/ld+json">'
            + json.dumps(obj, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
            + "</script>")


def business_ld(lang):
    return {"@context": "https://schema.org", "@type": "LocalBusiness", "@id": B.SITE_URL + "/#business",
            "name": B.BRAND, "url": B.SITE_URL + home_of(lang), "telephone": [B.PHONE_INTL, B.PHONE2_INTL],
            "areaServed": {"@type": "Country", "name": "Israel"}, "description": t(lang, "tagline")}


def breadcrumb_ld(crumbs):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": B.SITE_URL + h}
                                for i, (n, h) in enumerate(crumbs)]}


def faq_ld(items):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": f["q"],
                            "acceptedAnswer": {"@type": "Answer", "text": f["a"]}} for f in items]}


# ---------------------------------------------------------------- site registry

SITE = {}   # path -> page dict (lang, nav, lead, ...), filled by register()


def register(p):
    assert p["path"] not in SITE, f"duplicate page {p['path']}"
    SITE[p["path"]] = p


def pages_in(lang, *groups):
    return [p for p in CONTENT_PAGES if p["lang"] == lang and p["group"] in groups]


def nav_html(lang, current):
    def link(path, name):
        cur = " aria-current=page" if path == current else ""
        return f'<a href="{path}"{cur}>{E(name)}</a>'

    def drop(label, items):
        return (f'<details class="sub"><summary>{label}</summary><div>'
                + "".join(link(p["path"], p["nav"]) for p in items) + "</div></details>")

    if lang == "he":
        services = pages_in("he", "service", "route", "vip")
        tours = pages_in("he", "tour")
    else:
        services = pages_in("en", "service")
        tours = pages_in("en", "tour") or [SITE["/israel-private-tours"]]
    return (link(home_of(lang), t(lang, "home")) + drop(t(lang, "services"), services)
            + drop(t(lang, "tours"), tours)
            + link("/fleet" if lang == "he" else "/en/fleet", t(lang, "fleet"))
            + link("/blog" if lang == "he" else "/en/blog", t(lang, "articles")))


def footer_cols(lang):
    def col(title, items):
        return f'<div><h2>{E(title)}</h2>' + "".join(f'<a href="{p["path"]}">{E(p["nav"])}</a>' for p in items) + "</div>"
    if lang == "he":
        return (col(t(lang, "services"), pages_in("he", "service", "vip"))
                + col(t(lang, "tours"), pages_in("he", "tour"))
                + col(t(lang, "cities"), pages_in("he", "route", "city")))
    return (col(t(lang, "services"), pages_in("en", "service"))
            + col(t(lang, "travelers"), pages_in("en", "diaspora")))


# ---------------------------------------------------------------- layout

def layout(p, main, ld=(), og_type="website", noindex=False):
    lang, path = p["lang"], p["path"]
    other = "en" if lang == "he" else "he"
    d = "rtl" if lang == "he" else "ltr"
    canon = B.SITE_URL + path
    alt = p.get("alt")
    alts = ""
    if alt and not noindex:
        he_url = path if lang == "he" else alt
        alts = (f'<link rel="alternate" hreflang="{lang}" href="{B.SITE_URL}{path}">'
                f'<link rel="alternate" hreflang="{other}" href="{B.SITE_URL}{alt}">'
                f'<link rel="alternate" hreflang="x-default" href="{B.SITE_URL}{he_url}">')
    switch = alt or home_of(other)
    lds = "".join(jsonld(x) for x in (business_ld(lang), *ld))
    wa = f"https://wa.me/{B.WHATSAPP}"
    robots = '<meta name="robots" content="noindex">\n' if noindex else ""
    return f"""<!doctype html>
<html lang="{lang}" dir="{d}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<script>document.documentElement.className="js"</script>
<title>{E(p["title"])}</title>
<meta name="description" content="{E(p["desc"])}">
{robots}<link rel="canonical" href="{canon}">
{alts}
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{B.BRAND}">
<meta property="og:title" content="{E(p["title"])}">
<meta property="og:description" content="{E(p["desc"])}">
<meta property="og:url" content="{canon}">
<meta property="og:locale" content="{"he_IL" if lang == "he" else "en_US"}">
<meta name="theme-color" content="#111827">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<style>{CSS}</style>
{lds}
</head>
<body>
<a class="skip" href="#main">{t(lang, "skip")}</a>
<header class="top">
 <div class="wrap bar">
  <a class="logo" href="{home_of(lang)}">Tour <b>VIP</b></a>
  <button class="burger" type="button" aria-expanded="false" aria-controls="nav" aria-label="{t(lang, "menu")}"><span></span></button>
  <nav class="nav" id="nav">{nav_html(lang, path)}
   <a class="lang" href="{switch}" hreflang="{other}" lang="{other}">{t(lang, "other_lang")}</a></nav>
  <a class="btn btn-sm" href="#book">{t(lang, "book")}</a>
 </div>
</header>
<main id="main">
{main}
{booking_section(lang, path)}
</main>
<footer class="foot">
 <div class="wrap cols">
  <div><a class="logo" href="{home_of(lang)}">Tour <b>VIP</b></a><p>{E(t(lang, "tagline"))}</p>
   <p><a href="tel:{B.PHONE_INTL}" dir="ltr">{B.PHONE_DISPLAY}</a><a href="tel:{B.PHONE2_INTL}" dir="ltr">{B.PHONE2_DISPLAY}</a>
   <a href="{wa}">{t(lang, "whatsapp")}</a></p></div>
  {footer_cols(lang)}
 </div>
 <p class="wrap copy">© {B.BRAND}. {t(lang, "rights")}.</p>
</footer>
<div class="fab">
 <a class="fab-wa" href="{wa}" aria-label="{t(lang, "whatsapp")}">{icon("wa")}</a>
 <a class="fab-call" href="tel:{B.PHONE_INTL}" aria-label="{t(lang, "call")} {B.PHONE_DISPLAY}">{icon("phone")}</a>
</div>
<script src="{JS_URL}" defer></script>
</body>
</html>
"""


def booking_section(lang, path):
    groups = ("service", "route", "tour", "vip") if lang == "he" else ("service", "tour")
    opts = "".join(
        f'<option value="{E(p["nav"])}"{" selected" if p["path"] == path else ""}>{E(p["nav"])}</option>'
        for p in pages_in(lang, *groups))
    veh = f'<option value="">{t(lang, "f_vehicle_any")}</option>' + "".join(
        f'<option>{E(v[lang]["name"])}</option>' for v in B.FLEET)

    def field(name, key, typ="text", req=False, extra=""):
        r = " required" if req else ""
        star = ' <span aria-hidden="true">*</span>' if req else ""
        return f'<label><span>{t(lang, key)}{star}</span><input name="{name}" type="{typ}"{r}{extra}></label>'

    return f"""<section class="book" id="book" aria-labelledby="book-h">
 <div class="wrap">
 <h2 id="book-h">{t(lang, "book_title")}</h2>
 <p>{t(lang, "book_lead")}</p>
 <form id="booking" data-wa="{B.WHATSAPP}" data-intro="{E(t(lang, "wa_intro"))}" novalidate>
  <div class="grid">
   {field("name", "f_name", req=True, extra=' autocomplete="name"')}
   {field("phone", "f_phone", "tel", True, ' autocomplete="tel" dir="ltr"')}
   <label><span>{t(lang, "f_service")}</span><select name="service">{opts}</select></label>
   <label><span>{t(lang, "f_vehicle")}</span><select name="vehicle">{veh}</select></label>
   {field("date", "f_date", "date", True)}
   {field("time", "f_time", "time", True)}
   {field("from", "f_from", req=True)}
   {field("to", "f_to", req=True)}
   {field("pax", "f_pax", "number", True, ' min="1" max="500" inputmode="numeric"')}
   {field("bags", "f_bags", "number", extra=' min="0" max="500" inputmode="numeric"')}
   {field("flight", "f_flight", extra=' dir="ltr"')}
   <label class="check"><input name="return" type="checkbox"> <span>{t(lang, "f_return")}</span></label>
   <label class="wide"><span>{t(lang, "f_notes")}</span><textarea name="notes" rows="3"></textarea></label>
  </div>
  <p class="err" role="alert" hidden data-msg="{t(lang, "f_required")}"></p>
  <button class="btn" type="submit">{icon("wa")} {t(lang, "f_submit")}</button>
  <noscript><p>{t(lang, "noscript")} <a href="https://wa.me/{B.WHATSAPP}">wa.me/{B.WHATSAPP}</a></p></noscript>
 </form>
 </div>
</section>"""


# ---------------------------------------------------------------- blocks

def fleet_cards(lang, ids=None):
    vs = [FLEET[i] for i in ids] if ids else B.FLEET
    out = []
    for v in vs:
        seats = f'{v["seats"]} {t(lang, "seats")}' if v["seats"] else t(lang, "seats_ask")
        out.append(f'<li class="pcard"><div class="ph">{photo("fleet-" + v["id"], v[lang]["name"], "bus")}'
                   f'<div class="cap"><h3>{E(v[lang]["name"])}</h3><span>{icon("user")} {E(seats)}</span></div></div>'
                   f'<p class="pbody">{E(v[lang]["desc"])}</p></li>')
    return f'<ul class="cards pcards">{"".join(out)}</ul>'


def page_cards(paths):
    out = []
    for path in paths:
        p = SITE[path]
        out.append(f'<li class="card"><a href="{path}"><h3>{E(p["nav"])}</h3><p>{E(p["lead"])}</p>'
                   f'<span class="more">{t(p["lang"], "read_more")}</span></a></li>')
    return f'<ul class="cards">{"".join(out)}</ul>'


def review_block(lang, limit=None):
    items = []
    for r in REVIEWS:
        text = r.get(f"text_{lang}")
        if not text:
            continue
        name = r.get(f"name_{lang}") or r["name_he"]
        label = r.get(f"tour_{lang}") or ""
        meta = " · ".join(E(x) for x in (label, r.get("date") if lang == "he" else "") if x)
        stars = int(r.get("rating") or 0)
        items.append(f'<li class="card review"><div class="stars" role="img" aria-label="{stars}/5">{icon("star") * stars}</div>'
                     f'<blockquote>{E(text)}</blockquote><p class="who">{E(name)}'
                     + (f' <small>{meta}</small>' if meta else "") + "</p></li>")
    if not items:
        return ""
    return (f'<section class="wrap sec"><h2>{t(lang, "reviews_title")}</h2>'
            f'<ul class="cards">{"".join(items[:limit] if limit else items)}</ul></section>')


def faq_block(path):
    items = [f for f in FAQ if f["page"] == path]
    if not items:
        return "", None
    lang = SITE[path]["lang"]
    body = "".join(f'<details class="qa"><summary>{E(f["q"])}</summary><p>{E(f["a"])}</p></details>' for f in items)
    return f'<section class="sec"><h2>{t(lang, "faq_title")}</h2>{body}</section>', faq_ld(items)


ROUTES_HE = [("/hasaot-yerushalayim", "ירושלים"), ("/hasaot-tel-aviv", "תל אביב"), ("/hasaot-haifa", "חיפה"),
             ("/hasaot-netanya", "נתניה"), ("/hasaot-beer-sheva", "באר שבע"), ("/hasaot-ashdod", "אשדוד"),
             ("/hasaot-rishon-lezion", "ראשון לציון"), ("/hasaot-petah-tikva", "פתח תקווה")]


def routes_block(lang):
    """Dark airport-routes band, as on the Base44 home page. Hebrew only: the city pages are in Hebrew."""
    if lang != "he":
        return ""
    pills = "".join(f'<a class="pill" href="{h}">{E(n)}</a>' for h, n in ROUTES_HE)
    return (f'<section class="routes"><div class="wrap"><span class="tile">{icon("plane")}</span>'
            '<h2>הסעות מנתב"ג</h2><p>איסוף מנתב"ג לכל עיר בארץ, 24/7, עם מעקב אחרי הטיסה.</p>'
            f'<nav class="pills" aria-label="הסעות לפי עיר">{pills}</nav>'
            '<a class="btn" href="/hasaot-menatbag">לכל ההסעות מנתב"ג</a></div></section>')


def tour_block(lang):
    cards = []
    for tr in TOURS:
        name = tr[f"name_{lang}"]
        hl = "".join(f"<li>{icon('pin')} {E(h)}</li>" for h in tr[f"highlights_{lang}"])
        link = tr.get("page_he") if lang == "he" else ""
        title = f'<a href="{link}">{E(name)}</a>' if link else E(name)
        cards.append(f'<li class="pcard tour" id="tour-{E(tr["id"])}"><div class="ph">{photo("tour-" + tr["id"], name, "pin")}'
                     f'<div class="cap"><h3>{title}</h3><span>{icon("clock")} {E(tr[f"duration_{lang}"])}</span></div></div>'
                     f'<div class="pbody"><ul class="pins">{hl}</ul><a class="btn go" href="#book">{t(lang, "book")}</a></div></li>')
    return (f'<section class="sec c"><h2>{t(lang, "tours_title")}</h2>'
            f'<ul class="cards pcards">{"".join(cards)}</ul></section>')


def crumbs_html(crumbs):
    return ('<nav class="crumbs" aria-label="breadcrumb"><ol>'
            + "".join(f'<li><a href="{h}">{E(n)}</a></li>' for n, h in crumbs[:-1])
            + f'<li aria-current="page">{E(crumbs[-1][0])}</li></ol></nav>')


def hero(lang, h1, lead, small=False):
    return f"""<section class="hero{" small" if small else ""}"><div class="wrap">
<h1>{E(h1)}</h1><p class="lead">{E(lead)}</p>
<div class="ctas"><a class="btn" href="#book">{t(lang, "book")}</a>
<a class="btn wa" href="https://wa.me/{B.WHATSAPP}">{icon("wa")} {t(lang, "whatsapp")}</a>
<a class="btn tel" href="tel:{B.PHONE_INTL}" dir="ltr">{icon("phone")} {B.PHONE_DISPLAY}</a></div>
</div></section>"""


def md(text):
    """Tiny Markdown subset used by the kept blog article: #, ##, -, **bold**, [links](/x)."""
    out, para, items = [], [], []

    def inline(s):
        s = E(s, quote=False)
        s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
        return re.sub(r"\[([^\]]+)\]\((/[^)\s]*)\)", r'<a href="\2">\1</a>', s)

    def flush():
        if para:
            out.append(f"<p>{inline(' '.join(para))}</p>")
            para.clear()
        if items:
            out.append("<ul>" + "".join(f"<li>{inline(i)}</li>" for i in items) + "</ul>")
            items.clear()

    for line in text.splitlines():
        s = line.strip()
        if not s:
            flush()
        elif s.startswith("# "):
            flush()  # the page already has the title as <h1>
        elif s.startswith("## "):
            flush()
            out.append(f"<h2>{inline(s[3:])}</h2>")
        elif s.startswith("- "):
            if para:
                flush()
            items.append(s[2:])
        else:
            para.append(s)
    flush()
    return "\n".join(out)


# ---------------------------------------------------------------- pages

OUT = {}  # path -> html


def content_page(p):
    path, lang = p["path"], p["lang"]
    crumbs = [(t(lang, "home"), home_of(lang)), (p["nav"], path)]
    faq_html, fld = faq_block(path)
    ld = [breadcrumb_ld(crumbs),
          {"@context": "https://schema.org", "@type": "Service", "name": p["nav"], "description": p["desc"],
           "serviceType": p["nav"], "areaServed": {"@type": "Country", "name": "Israel"},
           "provider": {"@id": B.SITE_URL + "/#business"}, "url": B.SITE_URL + path}]
    if fld:
        ld.append(fld)
    related = [r for r in p.get("related", []) if r != path]
    main = (hero(lang, p["h1"], p["lead"], small=True)
            + f'<div class="wrap">{crumbs_html(crumbs)}<article class="prose">{p["body"]}</article>'
            + (tour_block(lang) if p.get("tours") else "")
            + f'<section class="sec"><h2>{t(lang, "suitable")}</h2>{fleet_cards(lang, p["vehicles"])}</section>'
            + faq_html
            + (f'<section class="sec"><h2>{t(lang, "articles")}</h2>{page_cards(p["articles"])}</section>' if p.get("articles") else "")
            + (f'<section class="sec"><h2>{t(lang, "all_services")}</h2>{page_cards(related)}</section>' if related else "")
            + "</div>")
    OUT[path] = layout(p, main, ld)


def home(lang):
    path = home_of(lang)
    p = SITE[path]
    faq_html, fld = faq_block(path)
    if lang == "he":
        featured = ["/hasaot-menatbag", "/nahag-prati", "/siurim-pratiyim", "/hasaot-beisrael", "/hasaot-iruvim",
                    "/minibus-hashara", "/accessible-transportation", "/rechavei-yukra", "/rechavim-memugnay-yeri"]
        arts = ["/blog/6ade3177ac824cd0a53548ab", "/blog/ben-gurion-transfer-guide", "/blog/choosing-vehicle-size"]
    else:
        featured = ["/ben-gurion-airport-transfers", "/private-driver-israel", "/israel-private-tours",
                    "/private-transportation-israel", "/israel-family-transportation", "/19-passenger-minibus-israel",
                    "/vip-transportation-israel", "/en/event-transportation", "/en/accessible-transportation"]
        arts = ["/en/blog/ben-gurion-transfer-guide", "/en/blog/choosing-vehicle-size", "/en/blog/private-day-tours-from-tel-aviv"]
    banner = ""
    if (ROOT / "assets" / "img" / "hero-banner.webp").exists():
        alt = "TOUR VIP — הסעות, טיולים ושירותי VIP בכל רחבי ישראל" if lang == "he" else "TOUR VIP — transfers, tours and VIP services across Israel"
        banner = (f'<div class="banner"><img src="/assets/img/hero-banner.webp" alt="{E(alt)}" '
                  'width="1536" height="1024" fetchpriority="high"></div>')
    main = (banner + hero(lang, p["h1"], p["lead"])
            + f'<section class="wrap sec c"><h2>{t(lang, "services")}</h2>{page_cards(featured)}</section>'
            + f'<div class="wrap">{tour_block(lang)}</div>'
            + f'<section class="wrap sec c"><h2>{t(lang, "fleet")}</h2>{fleet_cards(lang)}</section>'
            + routes_block(lang)
            + review_block(lang)
            + (f'<div class="wrap">{faq_html}</div>' if faq_html else "")
            + f'<section class="wrap sec"><h2>{t(lang, "articles")}</h2>{page_cards(arts)}</section>')
    OUT[path] = layout(p, main, [fld] if fld else [])


def fleet_page(p):
    lang = p["lang"]
    crumbs = [(t(lang, "home"), home_of(lang)), (p["nav"], p["path"])]
    art = "/blog/choosing-vehicle-size" if lang == "he" else "/en/blog/choosing-vehicle-size"
    main = (hero(lang, p["h1"], p["lead"], small=True)
            + f'<div class="wrap">{crumbs_html(crumbs)}<section class="sec">{fleet_cards(lang)}</section>'
            + f'<section class="sec"><h2>{t(lang, "articles")}</h2>{page_cards([art])}</section></div>')
    OUT[p["path"]] = layout(p, main, [breadcrumb_ld(crumbs)])


def blog_index(p, posts):
    lang = p["lang"]
    crumbs = [(t(lang, "home"), home_of(lang)), (p["nav"], p["path"])]
    main = (hero(lang, p["h1"], p["lead"], small=True)
            + f'<div class="wrap">{crumbs_html(crumbs)}<section class="sec">{page_cards(posts)}</section></div>')
    OUT[p["path"]] = layout(p, main, [breadcrumb_ld(crumbs)])


def article_page(p, body_html, date, service_path, others):
    lang, path = p["lang"], p["path"]
    blog = "/blog" if lang == "he" else "/en/blog"
    crumbs = [(t(lang, "home"), home_of(lang)), (t(lang, "articles"), blog), (p["h1"], path)]
    ld = [breadcrumb_ld(crumbs),
          {"@context": "https://schema.org", "@type": "Article", "headline": p["h1"], "description": p["desc"],
           "inLanguage": lang, "datePublished": date, "dateModified": date, "mainEntityOfPage": B.SITE_URL + path,
           "author": {"@type": "Organization", "name": B.BRAND, "url": B.SITE_URL},
           "publisher": {"@id": B.SITE_URL + "/#business"}}]
    svc = SITE[service_path]
    main = (f'<div class="wrap">{crumbs_html(crumbs)}<article class="prose art"><h1>{E(p["h1"])}</h1>'
            f'<p class="date">{t(lang, "updated")}: <time datetime="{date}">{date}</time></p>'
            f'{body_html}<p class="cta-line"><a class="btn" href="{service_path}">{E(svc["nav"])}</a></p></article>'
            f'<section class="sec"><h2>{t(lang, "related")}</h2>{page_cards(others)}</section></div>')
    OUT[path] = layout(p, main, ld, og_type="article")


def special_pages():
    """Home, fleet and blog pages: (path, lang, alt, nav, title, desc, h1, lead)."""
    he_home_title = 'Tour VIP | הסעות לנתב"ג, נהג צמוד, מיניבוסים וסיורים פרטיים בישראל'
    rows = [
        ("/", "he", "/en", t("he", "home"), he_home_title,
         'הסעות לנתב"ג, נהג צמוד, סיורים פרטיים והסעות לאירועים בכל הארץ. מוניות, ואנים, מיניבוסים 16-22, אוטובוסים 35-60 ורכבים ממוגנים. 24/7. 054-283-1111.',
         t("he", "tagline"), "מונית, ואן, מיניבוס, אוטובוס ורכב ממוגן, עם נהג, לכל מקום בארץ, 24/7. מזמינים בוואטסאפ ומקבלים אישור ומחיר."),
        ("/en", "en", "/", t("en", "home"), "Tour VIP | Airport Transfers, Private Drivers, Minibuses & Private Tours in Israel",
         "Ben Gurion Airport transfers, private drivers, private tours and event transportation across Israel. Taxis, vans, 16-22 seat minibuses, 35-60 seat coaches and armored vehicles. 24/7.",
         t("en", "tagline"), "Taxi, van, minibus, coach or armored vehicle, with a driver, anywhere in Israel, 24/7. Book on WhatsApp and get a confirmation and price."),
        ("/fleet", "he", "/en/fleet", t("he", "fleet"), "הצי שלנו: מוניות, ואנים, מיניבוסים, אוטובוסים ורכבים ממוגנים | Tour VIP",
         "מונית 4 מקומות, ואן 6 ו-7, מיניבוס 16, 19 ו-22, אוטובוס 35, 50 ו-60 מקומות ורכבים ממוגנים, עם נהג.",
         t("he", "fleet"), "לכל גודל קבוצה יש רכב: מנסיעה של זוג ועד הסעה של 60 נוסעים ברכב אחד."),
        ("/en/fleet", "en", "/fleet", t("en", "fleet"), "Our Fleet: Taxis, Vans, Minibuses, Coaches & Armored Vehicles | Tour VIP",
         "4-seat taxi, 6 and 7 seat vans, 16, 19 and 22 seat minibuses, 35, 50 and 60 seat coaches and armored vehicles, all with a driver.",
         t("en", "fleet"), "A vehicle for every group size: from a ride for two to 60 passengers in one coach."),
        ("/blog", "he", "/en/blog", t("he", "articles"), 'מאמרים ומדריכים: הסעות, נתב"ג וטיולים בישראל | Tour VIP',
         'מדריכים מעשיים להזמנת הסעות, נסיעות לנתב"ג, אירועים, טיולים משפחתיים ונסיעות נגישות בישראל.',
         t("he", "articles"), 'מדריכים מעשיים להזמנת הסעות, נסיעות לנתב"ג, אירועים, טיולים ונסיעות נגישות.'),
        ("/en/blog", "en", "/blog", t("en", "articles"), "Articles & Guides: Transfers, Ben Gurion Airport and Touring Israel | Tour VIP",
         "Practical guides to booking transfers, Ben Gurion Airport rides, events, family trips and accessible rides in Israel.",
         t("en", "articles"), "Practical guides to booking transfers, airport rides, events, family trips and accessible rides."),
    ]
    return [{"path": r[0], "lang": r[1], "alt": r[2], "nav": r[3], "title": r[4], "desc": r[5], "h1": r[6], "lead": r[7],
             "group": "special"} for r in rows]


def build_pages():
    SITE.clear()
    OUT.clear()
    for p in CONTENT_PAGES:
        register(p)
    for p in special_pages():
        register(p)
    articles = []  # (page dict, body html, date, service path)
    for a in ARTICLES:
        for lang in ("he", "en"):
            x = a[lang]
            path = f"/blog/{a['slug']}" if lang == "he" else f"/en/blog/{a['slug']}"
            alt = f"/en/blog/{a['slug']}" if lang == "he" else f"/blog/{a['slug']}"
            p = {"path": path, "lang": lang, "alt": alt, "nav": x["title"], "title": f'{x["title"]} | {B.BRAND}',
                 "desc": x["desc"], "h1": x["title"], "lead": x["desc"], "group": "article"}
            register(p)
            svc = ARTICLE_SERVICE[a["service"]][lang] if "service" in a else a[f"service_{lang}"]
            articles.append((p, x["body"], a.get("modified", a["date"]), svc))
    for k in KEPT_ARTICLES:
        p = {"path": k["path"], "lang": k["lang"], "alt": None, "nav": k["title"], "title": f'{k["title"]} | {B.BRAND}',
             "desc": k["desc"], "h1": k["title"], "lead": k["desc"], "group": "article"}
        register(p)
        articles.append((p, md(k["markdown"]), k["date"], k["service"]))

    for p in CONTENT_PAGES:
        content_page(p)
    home("he")
    home("en")
    fleet_page(SITE["/fleet"])
    fleet_page(SITE["/en/fleet"])
    articles.sort(key=lambda a: a[2], reverse=True)  # newest first
    for lang, blog in (("he", "/blog"), ("en", "/en/blog")):
        posts = [a[0]["path"] for a in articles if a[0]["lang"] == lang]
        blog_index(SITE[blog], posts)
        for p, body, date, svc in articles:
            if p["lang"] == lang:
                article_page(p, body, date, svc, [x for x in posts if x != p["path"]][:3])


def not_found():
    p = {"path": "/404", "lang": "he", "alt": None, "title": f'{t("he", "not_found")} | {B.BRAND}',
         "desc": t("he", "not_found_text")}
    main = (hero("he", t("he", "not_found"), t("he", "not_found_text"), small=True)
            + f'<div class="wrap"><section class="sec">{page_cards(["/hasaot-menatbag", "/nahag-prati", "/hasaot-beisrael", "/ben-gurion-airport-transfers", "/private-driver-israel", "/israel-private-tours"])}</section></div>')
    return layout(p, main, noindex=True)


# ---------------------------------------------------------------- output

def validate():
    for p in SITE.values():
        alt = p.get("alt")
        if alt:
            assert alt in SITE, f"{p['path']}: alt {alt} is not a page"
            assert SITE[alt].get("alt") == p["path"], f"{p['path']} <-> {alt} alt links are not mutual"
            assert SITE[alt]["lang"] != p["lang"], f"{p['path']} and {alt} have the same language"
        for r in p.get("related", []) + p.get("articles", []):
            assert r in SITE, f"{p['path']}: link to unknown page {r}"
            assert SITE[r]["lang"] == p["lang"], f"{p['path']}: related {r} is in another language"
        for v in p.get("vehicles", []):
            assert v in FLEET, f"{p['path']}: unknown vehicle {v}"
    for f in FAQ:
        assert f["page"] in SITE, f"FAQ for unknown page {f['page']}"
    for old, new in REDIRECTS.items():
        assert old not in SITE, f"{old} is both a page and a redirect"
        assert new in SITE, f"redirect {old} -> {new}: target is not a page"
    for tr in TOURS:
        assert not tr.get("page_he") or tr["page_he"] in SITE, tr["id"]


def build():
    build_pages()
    validate()
    if DIST.exists():
        shutil.rmtree(DIST)
    (DIST / "assets").mkdir(parents=True)
    for path, page in OUT.items():
        f = DIST / ("index.html" if path == "/" else path.lstrip("/") + ".html")
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(page, encoding="utf-8")
    (DIST / "404.html").write_text(not_found(), encoding="utf-8")
    (DIST / "assets" / "site.js").write_bytes(JS_BYTES)
    shutil.copy(ROOT / "assets" / "favicon.svg", DIST / "favicon.svg")
    if (ROOT / "assets" / "img").is_dir():
        shutil.copytree(ROOT / "assets" / "img", DIST / "assets" / "img")
    # nginx `map $uri $redirect_to { include .../redirects.map; }`
    (DIST / "redirects.map").write_text("".join(f"{o} {n};\n" for o, n in sorted(REDIRECTS.items())), encoding="utf-8")

    rows = []
    for path in sorted(OUT):
        p = SITE[path]
        alts = ""
        if p.get("alt"):
            alts = (f'<xhtml:link rel="alternate" hreflang="{p["lang"]}" href="{B.SITE_URL}{path}"/>'
                    f'<xhtml:link rel="alternate" hreflang="{SITE[p["alt"]]["lang"]}" href="{B.SITE_URL}{p["alt"]}"/>')
        rows.append(f"<url><loc>{B.SITE_URL}{path}</loc>{alts}</url>")
    (DIST / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
        + "\n".join(rows) + "\n</urlset>\n", encoding="utf-8")
    (DIST / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {B.SITE_URL}/sitemap.xml\n", encoding="utf-8")
    print(f"built {len(OUT)} pages, {len(REDIRECTS)} redirects -> {DIST}")


if __name__ == "__main__":
    build()
    if "--serve" in sys.argv:
        import functools
        import http.server

        class H(http.server.SimpleHTTPRequestHandler):
            def send_head(self):  # mimic nginx: redirects, then $uri, $uri.html, 404.html
                p = self.path.split("?")[0]
                if p in REDIRECTS:
                    self.send_response(301)
                    self.send_header("Location", REDIRECTS[p])
                    self.end_headers()
                    return None
                f = DIST / p.lstrip("/")
                if p != "/" and not f.is_file():
                    self.path = p + ".html" if (DIST / (p.lstrip("/") + ".html")).is_file() else "/404.html"
                return super().send_head()

        http.server.ThreadingHTTPServer(("127.0.0.1", 8080), functools.partial(H, directory=str(DIST))).serve_forever()
