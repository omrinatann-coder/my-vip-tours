#!/usr/bin/env python3
"""Static site generator for my-vip-tours.com. No dependencies (Python 3.9+).

    python3 build.py            # writes dist/
    python3 build.py --serve    # build, then serve dist/ on http://127.0.0.1:8080

Hebrew pages keep the original URLs (/ben-gurion-airport-transfers), English
pages are under /en/... . Each page is written as <path>.html and nginx serves
/<path> with `try_files $uri $uri.html`, so URLs have no extension or slash.
"""
import hashlib
import html
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CONTENT = ROOT / "content"
DIST = ROOT / "dist"
sys.path.insert(0, str(CONTENT))

import business as B  # noqa: E402
from articles import ARTICLES  # noqa: E402
from services import SERVICES  # noqa: E402

E = html.escape
REVIEWS = json.loads((CONTENT / "reviews.json").read_text(encoding="utf-8"))
TOURS = json.loads((CONTENT / "tours.json").read_text(encoding="utf-8"))
FAQ = json.loads((CONTENT / "faq.json").read_text(encoding="utf-8"))
FLEET = {v["id"]: v for v in B.FLEET}
SVC = {s["slug"]: s for s in SERVICES}
ART = {a["slug"]: a for a in ARTICLES}

CSS = (ROOT / "assets" / "style.css").read_text(encoding="utf-8")
JS_BYTES = (ROOT / "assets" / "site.js").read_bytes()
JS_URL = "/assets/site.js?v=" + hashlib.sha256(JS_BYTES).hexdigest()[:10]

ICONS = {
    "plane": '<path d="M21 16v-2l-8-5V3.5a1.5 1.5 0 0 0-3 0V9l-8 5v2l8-2.5V19l-2 1.5V22l3.5-1 3.5 1v-1.5L13 19v-5.5z"/>',
    "driver": '<circle cx="12" cy="7" r="4"/><path d="M4 21c0-4.4 3.6-8 8-8s8 3.6 8 8z"/>',
    "map": '<path d="M9 3 3 5v16l6-2 6 2 6-2V3l-6 2zm0 2.2 6 2v11.6l-6-2z"/>',
    "car": '<path d="M5 11l1.5-4.5A2 2 0 0 1 8.4 5h7.2a2 2 0 0 1 1.9 1.5L19 11a2 2 0 0 1 2 2v4h-2v2h-3v-2H8v2H5v-2H3v-4a2 2 0 0 1 2-2zm2.1 0h9.8l-1-3H8.1zM6.5 15a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3zm11 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3z"/>',
    "access": '<circle cx="12" cy="4" r="2"/><path d="M11 7h2v5h4v2h-6zM9.5 9.3A6 6 0 1 0 17 17.5l-1.6-1.2A4 4 0 1 1 10.3 11z"/>',
    "family": '<circle cx="7" cy="5" r="2.5"/><circle cx="17" cy="5" r="2.5"/><circle cx="12" cy="11" r="2"/><path d="M3 21v-7a4 4 0 0 1 8 0v7zm10 0v-7a4 4 0 0 1 8 0v7zm-3 0v-4a2 2 0 0 1 4 0v4z"/>',
    "bus": '<path d="M5 3h14a2 2 0 0 1 2 2v12h-1v2h-3v-2H7v2H4v-2H3V5a2 2 0 0 1 2-2zm0 3v5h14V6zm2 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3zm10 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3z"/>',
    "event": '<path d="M7 2v2H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2h-2V2h-2v2H9V2zM5 9h14v11H5zm7 2 1.2 2.6 2.8.3-2.1 1.9.6 2.8-2.5-1.5-2.5 1.5.6-2.8L8 13.9l2.8-.3z"/>',
    "phone": '<path d="M6.6 10.8a15 15 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/>',
    "wa": '<path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm5.3 14.1c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .2-3.3-.7-2.8-1.1-4.5-3.9-4.7-4.1-.1-.2-1.1-1.5-1.1-2.8s.7-2 1-2.3c.2-.3.5-.3.7-.3h.5c.2 0 .4 0 .6.5l.9 2.1c.1.2.1.3 0 .5l-.3.5-.4.4c-.1.1-.3.3-.1.6.2.3.8 1.3 1.7 2.1 1.2 1 2.1 1.3 2.4 1.5.3.1.5.1.6-.1l.9-1c.2-.3.4-.2.6-.1l2 1c.3.1.5.2.5.3.1.1.1.6-.1 1.2z"/>',
    "star": '<path d="m12 2 3.1 6.3 6.9 1-5 4.9 1.2 6.8L12 17.8 5.8 21l1.2-6.8-5-4.9 6.9-1z"/>',
}


def icon(name, cls="ic"):
    return f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true" focusable="false">{ICONS[name]}</svg>'


def url(lang, path=""):
    """Site-relative URL of a page. path '' is the home page."""
    if lang == B.DEFAULT_LANG:
        return "/" + path
    return f"/{lang}" + (f"/{path}" if path else "")


def t(lang, key):
    return B.UI[lang][key]


def loc(item, lang):
    """Item's text in `lang`, falling back to the other language."""
    return item.get(lang) or item.get("he") or item.get("en")


def has_faq():
    return bool(FAQ)


def nav_items(lang):
    items = [("", t(lang, "home")), ("fleet", t(lang, "fleet")),
             ("israel-private-tours", t(lang, "tours")), ("articles", t(lang, "articles"))]
    if has_faq():
        items.append(("faq", t(lang, "faq")))
    return items


def jsonld(obj):
    return ('<script type="application/ld+json">'
            + json.dumps(obj, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
            + "</script>")


def business_ld(lang):
    ld = {
        "@context": "https://schema.org", "@type": "LocalBusiness",
        "@id": B.SITE_URL + "/#business", "name": B.BRAND, "url": B.SITE_URL + url(lang),
        "telephone": B.PHONE_INTL, "areaServed": {"@type": "Country", "name": "Israel"},
        "description": t(lang, "tagline"),
    }
    if REVIEWS:
        ratings = [r["rating"] for r in REVIEWS if r.get("rating")]
        if ratings:
            ld["aggregateRating"] = {"@type": "AggregateRating",
                                     "ratingValue": round(sum(ratings) / len(ratings), 1),
                                     "reviewCount": len(ratings), "bestRating": 5}
    return ld


def breadcrumb_ld(lang, crumbs):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": name,
                                 "item": B.SITE_URL + href} for i, (name, href) in enumerate(crumbs)]}


def faq_ld(items, lang):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": loc(f, lang)["q"],
                            "acceptedAnswer": {"@type": "Answer", "text": loc(f, lang)["a"]}}
                           for f in items]}


# ---------------------------------------------------------------- layout

def layout(lang, path, title, desc, main, ld=(), alt_exists=True, og_type="website"):
    other = "en" if lang == "he" else "he"
    d = "rtl" if lang == "he" else "ltr"
    canon = B.SITE_URL + url(lang, path)
    alts = ""
    if alt_exists:
        alts = "".join(f'<link rel="alternate" hreflang="{l}" href="{B.SITE_URL}{url(l, path)}">' for l in B.LANGS)
        alts += f'<link rel="alternate" hreflang="x-default" href="{B.SITE_URL}{url(B.DEFAULT_LANG, path)}">'
    nav = "".join(
        f'<a href="{url(lang, p)}"{" aria-current=page" if p == path else ""}>{E(n)}</a>'
        for p, n in nav_items(lang))
    svc_links = "".join(f'<a href="{url(lang, s["slug"])}">{E(s[lang]["nav"])}</a>' for s in SERVICES)
    switch = url(other, path) if alt_exists else url(other)
    lds = "".join(jsonld(x) for x in (business_ld(lang), *ld))
    wa = f"https://wa.me/{B.WHATSAPP}"
    return f"""<!doctype html>
<html lang="{lang}" dir="{d}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<script>document.documentElement.className="js"</script>
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<link rel="canonical" href="{canon}">
{alts}
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{B.BRAND}">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:locale" content="{"he_IL" if lang == "he" else "en_US"}">
<meta name="theme-color" content="#0f1b2d">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<style>{CSS}</style>
{lds}
</head>
<body>
<a class="skip" href="#main">{t(lang, "skip")}</a>
<header class="top">
 <div class="wrap bar">
  <a class="logo" href="{url(lang)}">Tour <b>VIP</b></a>
  <button class="burger" type="button" aria-expanded="false" aria-controls="nav" aria-label="{t(lang, "menu")}"><span></span></button>
  <nav class="nav" id="nav">{nav}<details class="sub"><summary>{t(lang, "services")}</summary><div>{svc_links}</div></details>
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
  <div><a class="logo" href="{url(lang)}">Tour <b>VIP</b></a><p>{E(t(lang, "tagline"))}</p>
   <p><a href="tel:{B.PHONE_INTL}" dir="ltr">{B.PHONE_DISPLAY}</a></p></div>
  <div><h2>{t(lang, "services")}</h2>{svc_links}</div>
  <div><h2>{t(lang, "contact")}</h2><a href="{wa}">{t(lang, "whatsapp")}</a>
   <a href="tel:{B.PHONE_INTL}">{t(lang, "call")}</a>
   {"".join(f'<a href="{url(lang, p)}">{E(n)}</a>' for p, n in nav_items(lang)[1:])}</div>
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
    opts = "".join(
        f'<option value="{E(s[lang]["nav"])}"{" selected" if s["slug"] == path else ""}>{E(s[lang]["nav"])}</option>'
        for s in SERVICES)
    veh = f'<option value="">{t(lang, "f_vehicle_any")}</option>' + "".join(
        f'<option>{E(v[lang]["name"])}</option>' for v in B.FLEET)

    def field(name, key, typ="text", req=False, extra=""):
        r = " required" if req else ""
        star = ' <span aria-hidden="true">*</span>' if req else ""
        return (f'<label><span>{t(lang, key)}{star}</span>'
                f'<input name="{name}" type="{typ}"{r}{extra}></label>')

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
    cards = []
    for v in vs:
        seats = f'{v["seats"]} {t(lang, "seats")}' if v["seats"] else t(lang, "seats_ask")
        cards.append(f'<li class="card"><b class="seats">{E(seats)}</b><h3>{E(v[lang]["name"])}</h3>'
                     f'<p>{E(v[lang]["desc"])}</p></li>')
    return f'<ul class="cards">{"".join(cards)}</ul>'


def service_cards(lang, exclude=None):
    out = []
    for s in SERVICES:
        if s["slug"] == exclude:
            continue
        x = s[lang]
        out.append(f'<li class="card svc"><a href="{url(lang, s["slug"])}">{icon(s["icon"], "ic big")}'
                   f'<h3>{E(x["nav"])}</h3><p>{E(x["lead"])}</p></a></li>')
    return f'<ul class="cards">{"".join(out)}</ul>'


def review_block(lang, limit=None):
    if not REVIEWS:
        return ""
    items = []
    for r in REVIEWS[:limit] if limit else REVIEWS:
        stars = int(r.get("rating") or 0)
        rl = r.get("lang", lang)
        rd = "rtl" if rl == "he" else "ltr"
        meta = " · ".join(E(str(x)) for x in (r.get("source"), r.get("date")) if x)
        items.append(
            f'<li class="card review" lang="{rl}" dir="{rd}">'
            + (f'<div class="stars" role="img" aria-label="{stars}/5">{icon("star") * stars}</div>' if stars else "")
            + f'<blockquote>{E(r["text"])}</blockquote><p class="who">{E(r["name"])}'
            + (f' <small>{meta}</small>' if meta else "") + "</p></li>")
    return (f'<section class="wrap sec"><h2>{t(lang, "reviews_title")}</h2>'
            f'<ul class="cards">{"".join(items)}</ul></section>')


def faq_list(lang, items):
    return "".join(
        f'<details class="qa"><summary>{E(loc(f, lang)["q"])}</summary><p>{E(loc(f, lang)["a"])}</p></details>'
        for f in items)


def tour_block(lang):
    if not TOURS:
        return ""
    cards = []
    for tr in TOURS:
        x = loc(tr, lang)
        meta = "".join(f'<li><b>{t(lang, k)}:</b> {E(x[k])}</li>' for k in ("duration", "price") if x.get(k))
        cards.append(f'<li class="card tour" id="{E(tr["slug"])}"><h3>{E(x["name"])}</h3>'
                     + (f'<ul class="meta">{meta}</ul>' if meta else "")
                     + f'<p>{E(x.get("desc", ""))}</p></li>')
    return (f'<section class="sec"><h2>{t(lang, "tours_title")}</h2>'
            f'<ul class="cards">{"".join(cards)}</ul></section>')


def article_cards(lang, slugs=None):
    arts = [ART[s] for s in slugs] if slugs else ARTICLES
    return '<ul class="cards">' + "".join(
        f'<li class="card"><a href="{url(lang, "articles/" + a["slug"])}"><h3>{E(a[lang]["title"])}</h3>'
        f'<p>{E(a[lang]["desc"])}</p><span class="more">{t(lang, "read_more")}</span></a></li>'
        for a in arts) + "</ul>"


def crumbs_html(crumbs):
    return ('<nav class="crumbs" aria-label="breadcrumb"><ol>'
            + "".join(f'<li><a href="{h}">{E(n)}</a></li>' for n, h in crumbs[:-1])
            + f'<li aria-current="page">{E(crumbs[-1][0])}</li></ol></nav>')


def hero(lang, h1, lead, small=False):
    wa = f"https://wa.me/{B.WHATSAPP}"
    return f"""<section class="hero{" small" if small else ""}"><div class="wrap">
<h1>{E(h1)}</h1><p class="lead">{E(lead)}</p>
<div class="ctas"><a class="btn" href="#book">{t(lang, "book")}</a>
<a class="btn ghost" href="{wa}">{icon("wa")} {t(lang, "whatsapp")}</a>
<a class="btn ghost" href="tel:{B.PHONE_INTL}" dir="ltr">{icon("phone")} {B.PHONE_DISPLAY}</a></div>
</div></section>"""


# ---------------------------------------------------------------- pages

PAGES = {}  # path -> (lang, html)


def emit(lang, path, page):
    PAGES[url(lang, path)] = page


def home(lang):
    h1 = t(lang, "tagline")
    lead = ("מונית, ואן, מיניבוס, אוטובוס ורכב ממוגן, עם נהג, לכל מקום בארץ. מזמינים בוואטסאפ ומקבלים אישור ומחיר."
            if lang == "he" else
            "Taxi, van, minibus, coach or armored vehicle, with a driver, anywhere in Israel. Book on WhatsApp and get a confirmation and price.")
    title = ("Tour VIP | הסעות לנתב\"ג, נהג צמוד, מיניבוסים וסיורים פרטיים בישראל" if lang == "he"
             else "Tour VIP | Airport Transfers, Private Drivers, Minibuses & Private Tours in Israel")
    desc = ("הסעות לנתב\"ג, נהג צמוד, סיורים פרטיים והסעות לאירועים בכל הארץ. צי של מוניות, ואנים, מיניבוסים 16-22, אוטובוסים 35-60 ורכבים ממוגנים. 054-283-1111."
            if lang == "he" else
            "Ben Gurion Airport transfers, private drivers, private tours and event transportation across Israel. Taxis, vans, 16-22 seat minibuses, 35-60 seat coaches and armored vehicles.")
    main = (hero(lang, h1, lead)
            + f'<section class="wrap sec"><h2>{t(lang, "services")}</h2>{service_cards(lang)}</section>'
            + f'<section class="wrap sec"><h2>{t(lang, "fleet")}</h2>{fleet_cards(lang)}</section>'
            + review_block(lang, 6)
            + f'<section class="wrap sec"><h2>{t(lang, "articles")}</h2>{article_cards(lang, [a["slug"] for a in ARTICLES[:3]])}</section>')
    emit(lang, "", layout(lang, "", title, desc, main))


def service(lang, s):
    x = s[lang]
    path = s["slug"]
    crumbs = [(t(lang, "home"), url(lang)), (x["nav"], url(lang, path))]
    faqs = [f for f in FAQ if path in f.get("pages", [])]
    ld = [breadcrumb_ld(lang, crumbs),
          {"@context": "https://schema.org", "@type": "Service", "name": x["nav"], "description": x["desc"],
           "serviceType": x["nav"], "areaServed": {"@type": "Country", "name": "Israel"},
           "provider": {"@id": B.SITE_URL + "/#business"}, "url": B.SITE_URL + url(lang, path)}]
    if faqs:
        ld.append(faq_ld(faqs, lang))
    main = (hero(lang, x["h1"], x["lead"], small=True)
            + f'<div class="wrap">{crumbs_html(crumbs)}<article class="prose">{x["body"]}</article>'
            + (tour_block(lang) if path == "israel-private-tours" else "")
            + f'<section class="sec"><h2>{t(lang, "suitable")}</h2>{fleet_cards(lang, s["vehicles"])}</section>'
            + (f'<section class="sec"><h2>{t(lang, "faq_title")}</h2>{faq_list(lang, faqs)}</section>' if faqs else "")
            + f'<section class="sec"><h2>{t(lang, "articles")}</h2>{article_cards(lang, s["articles"])}</section>'
            + f'<section class="sec"><h2>{t(lang, "all_services")}</h2>{service_cards(lang, exclude=path)}</section></div>')
    emit(lang, path, layout(lang, path, x["title"], x["desc"], main, ld))


def fleet_page(lang):
    title = "הצי שלנו: מוניות, ואנים, מיניבוסים, אוטובוסים ורכבים ממוגנים | Tour VIP" if lang == "he" else \
        "Our Fleet: Taxis, Vans, Minibuses, Coaches & Armored Vehicles | Tour VIP"
    desc = "מונית 4 מקומות, ואן 6 ו-7, מיניבוס 16, 19 ו-22, אוטובוס 35, 50 ו-60 מקומות ורכבים ממוגנים, עם נהג." if lang == "he" else \
        "4-seat taxi, 6 and 7 seat vans, 16, 19 and 22 seat minibuses, 35, 50 and 60 seat coaches and armored vehicles, all with a driver."
    crumbs = [(t(lang, "home"), url(lang)), (t(lang, "fleet"), url(lang, "fleet"))]
    lead = "לכל גודל קבוצה יש רכב: מנסיעה של זוג ועד הסעה של 60 נוסעים ברכב אחד." if lang == "he" else \
        "A vehicle for every group size: from a ride for two to 60 passengers in one coach."
    main = (hero(lang, t(lang, "fleet"), lead, small=True)
            + f'<div class="wrap">{crumbs_html(crumbs)}<section class="sec">{fleet_cards(lang)}</section>'
            + f'<section class="sec"><h2>{t(lang, "articles")}</h2>{article_cards(lang, ["choosing-vehicle-size"])}</section></div>')
    emit(lang, "fleet", layout(lang, "fleet", title, desc, main, [breadcrumb_ld(lang, crumbs)]))


def articles_index(lang):
    title = "מאמרים ומדריכים: הסעות, נתב\"ג וטיולים בישראל | Tour VIP" if lang == "he" else \
        "Articles & Guides: Transfers, Ben Gurion Airport and Touring Israel | Tour VIP"
    desc = "מדריכים מעשיים להזמנת הסעות, נסיעות לנתב\"ג, אירועים, טיולים משפחתיים ונסיעות נגישות בישראל." if lang == "he" else \
        "Practical guides to booking transfers, Ben Gurion Airport rides, events, family trips and accessible rides in Israel."
    crumbs = [(t(lang, "home"), url(lang)), (t(lang, "articles"), url(lang, "articles"))]
    main = (hero(lang, t(lang, "articles"), desc, small=True)
            + f'<div class="wrap">{crumbs_html(crumbs)}<section class="sec">{article_cards(lang)}</section></div>')
    emit(lang, "articles", layout(lang, "articles", title, desc, main, [breadcrumb_ld(lang, crumbs)]))


def article(lang, a):
    x = a[lang]
    path = "articles/" + a["slug"]
    s = SVC[a["service"]]
    crumbs = [(t(lang, "home"), url(lang)), (t(lang, "articles"), url(lang, "articles")), (x["title"], url(lang, path))]
    ld = [breadcrumb_ld(lang, crumbs),
          {"@context": "https://schema.org", "@type": "Article", "headline": x["title"], "description": x["desc"],
           "inLanguage": lang, "datePublished": a["date"], "dateModified": a.get("modified", a["date"]),
           "mainEntityOfPage": B.SITE_URL + url(lang, path),
           "author": {"@type": "Organization", "name": B.BRAND, "url": B.SITE_URL},
           "publisher": {"@id": B.SITE_URL + "/#business"}}]
    others = [o["slug"] for o in ARTICLES if o["slug"] != a["slug"]][:3]
    main = (f'<div class="wrap">{crumbs_html(crumbs)}<article class="prose art"><h1>{E(x["title"])}</h1>'
            f'<p class="date">{t(lang, "updated")}: <time datetime="{a.get("modified", a["date"])}">{a.get("modified", a["date"])}</time></p>'
            f'{x["body"]}<p class="cta-line"><a class="btn" href="{url(lang, s["slug"])}">{E(s[lang]["nav"])}</a></p></article>'
            f'<section class="sec"><h2>{t(lang, "related")}</h2>{article_cards(lang, others)}</section></div>')
    emit(lang, path, layout(lang, path, f'{x["title"]} | {B.BRAND}', x["desc"], main, ld, og_type="article"))


def faq_page(lang):
    title = f'{t(lang, "faq_title")} | {B.BRAND}'
    desc = ("תשובות לשאלות נפוצות על הסעות לנתב\"ג, נהג צמוד, סיורים פרטיים, הסעות לאירועים והזמנה בוואטסאפ." if lang == "he"
            else "Answers to common questions about airport transfers, private drivers, private tours, event transportation and booking on WhatsApp.")
    crumbs = [(t(lang, "home"), url(lang)), (t(lang, "faq"), url(lang, "faq"))]
    main = (hero(lang, t(lang, "faq_title"), desc, small=True)
            + f'<div class="wrap">{crumbs_html(crumbs)}<section class="sec">{faq_list(lang, FAQ)}</section></div>')
    emit(lang, "faq", layout(lang, "faq", title, desc, main, [breadcrumb_ld(lang, crumbs), faq_ld(FAQ, lang)]))


def not_found():
    lang = B.DEFAULT_LANG
    main = (hero(lang, t(lang, "not_found"), t(lang, "not_found_text"), small=True)
            + f'<div class="wrap"><section class="sec">{service_cards(lang)}</section></div>')
    page = layout(lang, "404", f'{t(lang, "not_found")} | {B.BRAND}', t(lang, "not_found_text"), main, alt_exists=False)
    return page.replace('<link rel="canonical"', '<meta name="robots" content="noindex"><link rel="canonical"', 1)


# ---------------------------------------------------------------- output

def validate():
    seen = set()
    for s in SERVICES:
        assert s["slug"] not in seen, s["slug"]
        seen.add(s["slug"])
        for v in s["vehicles"]:
            assert v in FLEET, (s["slug"], v)
        for a in s["articles"]:
            assert a in ART, (s["slug"], a)
    for a in ARTICLES:
        assert a["service"] in SVC, a["slug"]
    for r in REVIEWS:
        assert r.get("name") and r.get("text"), f"review needs name and text: {r}"
        assert r.get("rating") in (None, 1, 2, 3, 4, 5), f"rating must be 1-5: {r}"
    for tr in TOURS:
        assert tr.get("slug") and loc(tr, "he").get("name"), f"tour needs slug and name: {tr}"
    for f in FAQ:
        assert loc(f, "he").get("q") and loc(f, "he").get("a"), f"faq needs q and a: {f}"
        for p in f.get("pages", []):
            assert p in SVC, f"faq page {p} is not a service slug"


def build():
    validate()
    PAGES.clear()
    for lang in B.LANGS:
        home(lang)
        for s in SERVICES:
            service(lang, s)
        fleet_page(lang)
        articles_index(lang)
        for a in ARTICLES:
            article(lang, a)
        if has_faq():
            faq_page(lang)

    if DIST.exists():
        shutil.rmtree(DIST)
    (DIST / "assets").mkdir(parents=True)
    for path, page in PAGES.items():
        f = DIST / ("index.html" if path == "/" else path.lstrip("/") + ".html")
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(page, encoding="utf-8")
    (DIST / "404.html").write_text(not_found(), encoding="utf-8")
    (DIST / "assets" / "site.js").write_bytes(JS_BYTES)
    shutil.copy(ROOT / "assets" / "favicon.svg", DIST / "favicon.svg")

    # sitemap with hreflang alternates
    rows = []
    for path in PAGES:
        lang = "en" if path == "/en" or path.startswith("/en/") else "he"
        bare = path[len("/en"):].lstrip("/") if lang == "en" else path.lstrip("/")
        alts = "".join(f'<xhtml:link rel="alternate" hreflang="{l}" href="{B.SITE_URL}{url(l, bare)}"/>'
                       for l in B.LANGS)
        rows.append(f"<url><loc>{B.SITE_URL}{path}</loc>{alts}</url>")
    (DIST / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
        + "\n".join(rows) + "\n</urlset>\n", encoding="utf-8")
    (DIST / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {B.SITE_URL}/sitemap.xml\n", encoding="utf-8")
    print(f"built {len(PAGES)} pages -> {DIST}")


if __name__ == "__main__":
    build()
    if "--serve" in sys.argv:
        import http.server
        import functools

        class H(http.server.SimpleHTTPRequestHandler):
            def send_head(self):  # mimic nginx: try $uri, then $uri.html, else 404.html
                p = self.path.split("?")[0]
                f = DIST / p.lstrip("/")
                if p != "/" and not f.is_file() and (DIST / (p.lstrip("/") + ".html")).is_file():
                    self.path = p + ".html"
                elif p != "/" and not f.is_file():
                    self.path = "/404.html"
                return super().send_head()

        http.server.ThreadingHTTPServer(("127.0.0.1", 8080), functools.partial(H, directory=str(DIST))).serve_forever()
