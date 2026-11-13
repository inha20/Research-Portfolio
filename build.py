#!/usr/bin/env python3
"""Build the research hub page from program.toml.

    python build.py                    write index.html and 404.html
    python build.py --check            exit 1 if the committed files are out of date
    python build.py --include-hidden   also render papers with show = false (for testing)
    python build.py --out DIR          write somewhere else (assets/ must sit next to it)

Needs Python 3.11 or newer. Standard library only.
"""
from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import re
import sys
import tomllib
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent
PAGES_BASE = "https://inha20.github.io/"
GITHUB_BASE = "https://github.com/inha20/"

STATUS = {
    "current": ("Current", "current"),
    "in-progress": ("In progress", "progress"),
    "archived": ("Archived", "archived"),
}
LANGS = {"ko": ("KO", "Korean"), "en": ("EN", "English")}
NUMBER_WORDS = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
NAV = [
    ("current", "Current"),
    ("map", "Map"),
    ("archive", "Archive"),
    ("genealogy", "Genealogy"),
    ("documents", "Documents"),
    ("about", "About"),
]

THEME_INIT = (
    "(function(){try{var t=localStorage.getItem('sr_theme');"
    "if(t!=='dark'&&t!=='light'){t=matchMedia('(prefers-color-scheme: light)').matches?'light':'dark'}"
    "document.documentElement.setAttribute('data-theme',t)}catch(e){}})();"
)


class BuildError(Exception):
    """Raised when program.toml is incomplete or inconsistent."""


def e(value) -> str:
    return html.escape(str(value), quote=True)


COMPOUND = re.compile(r"[\w₀-₉]+(?:[-–][\w₀-₉]+)+")


def nb(value) -> str:
    """Escape text and keep hyphenated compounds (Human-AI, multi-session) on one line."""
    return COMPOUND.sub(lambda m: f'<span class="nb">{m.group(0)}</span>', e(value))


# ---------------------------------------------------------------- loading

def load(include_hidden: bool) -> dict:
    with open(ROOT / "program.toml", "rb") as fh:
        data = tomllib.load(fh)
    for key in ("site", "person", "program", "layers", "papers", "genealogy", "docs", "beyond"):
        if key not in data:
            raise BuildError(f"program.toml: missing [{key}]")

    seen: set[int] = set()
    for p in data["papers"]:
        label = f"paper {p.get('id', '?')}"
        for key in ("id", "repo", "status", "role", "lang", "short", "title_en", "summary"):
            if key not in p:
                raise BuildError(f"{label}: missing '{key}'")
        if p["status"] not in STATUS:
            raise BuildError(f"{label}: status must be one of {', '.join(STATUS)}")
        if p["lang"] not in LANGS:
            raise BuildError(f"{label}: lang must be one of {', '.join(LANGS)}")
        if p["id"] in seen:
            raise BuildError(f"{label}: duplicate id")
        seen.add(p["id"])
        p.setdefault("show", True)
        p.setdefault("has_page", True)
        p.setdefault("tags", [])
        p.setdefault("title_ko", "")
        p.setdefault("version", "")
        p.setdefault("extra_links", [])
        for link in p["extra_links"]:
            for key in ("label", "path"):
                if key not in link:
                    raise BuildError(f"{label}: an extra_links entry is missing '{key}'")
        if p["extra_links"] and not p["has_page"]:
            raise BuildError(f"{label}: extra_links need has_page = true")
    for layer in data["layers"]:
        for pid in layer["papers"]:
            if pid not in seen:
                raise BuildError(f"layer '{layer['id']}': unknown paper id {pid}")
    for doc in data["docs"]:
        for key in ("badge", "title", "url", "lang", "desc"):
            if key not in doc:
                raise BuildError(f"doc '{doc.get('title', '?')}': missing '{key}'")
    for repo in data["beyond"].get("repos", []):
        for key in ("repo", "title", "lang", "desc"):
            if key not in repo:
                raise BuildError(f"beyond repo '{repo.get('repo', '?')}': missing '{key}'")

    data["papers"].sort(key=lambda p: p["id"])
    data["hidden"] = [p for p in data["papers"] if not p["show"]]
    if not include_hidden:
        data["papers"] = [p for p in data["papers"] if p["show"]]
    return data


# ---------------------------------------------------------------- small pieces

def paper_page(p: dict) -> str | None:
    return f"{PAGES_BASE}{p['repo']}/" if p["has_page"] else None


def paper_repo(p: dict) -> str:
    return f"{GITHUB_BASE}{p['repo']}"


def lang_chip(code: str, what: str = "Page") -> str:
    short, name = LANGS[code]
    return (
        f'<span class="chip chip--lang" title="{what} language: {name}">'
        f'<span aria-hidden="true">{short}</span><span class="sr-only">{what} language: {name}</span></span>'
    )


def status_chip(p: dict) -> str:
    label, cls = STATUS[p["status"]]
    if p["version"]:
        label += f" · {p['version']}"
    return f'<span class="chip chip--{cls}">{e(label)}</span>'


def ranges(numbers: list[int]) -> str:
    numbers = sorted(numbers)
    parts: list[str] = []
    start = prev = numbers[0]
    for n in numbers[1:] + [None]:  # type: ignore[list-item]
        if n is not None and n == prev + 1:
            prev = n
            continue
        parts.append(str(start) if start == prev else f"{start}–{prev}")
        if n is not None:
            start = prev = n
    return ", ".join(parts)


def section_head(eyebrow: str, title: str, title_id: str, intro: str = "") -> str:
    intro_html = f"<p>{nb(intro)}</p>" if intro else ""
    return (
        f'<div class="section-head"><span class="eyebrow">{e(eyebrow)}</span>'
        f'<h2 id="{title_id}">{e(title)}</h2>{intro_html}</div>'
    )


def ext_link(href: str, text: str, sr: str = "", arrow: str = "↗") -> str:
    sr_html = f'<span class="sr-only"> {e(sr)}</span>' if sr else ""
    return f'<a href="{e(href)}">{e(text)}{sr_html} <span aria-hidden="true">{arrow}</span></a>'


# ---------------------------------------------------------------- page chrome

def header(d: dict, full: bool = True) -> str:
    site, person = d["site"], d["person"]
    mark = "<i></i>" * 16
    nav = ""
    menu = ""
    if full:
        links = "".join(f'<a href="#{i}">{e(t)}</a>' for i, t in NAV)
        links += f'<a class="nav-gh" href="{e(person["github"])}">GitHub <span aria-hidden="true">↗</span></a>'
        nav = f'<nav class="nav-links" id="site-nav" aria-label="Sections">{links}</nav>'
        menu = (
            '<button class="icon-btn menu-btn" id="menu-btn" type="button" aria-label="Menu" '
            'aria-controls="site-nav" aria-expanded="false">'
            '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button>'
        )
    home = "#top" if full else site["url"]
    spacer = "" if full else '<span style="margin-left:auto"></span>'
    return f"""
<header class="site-header" id="site-header">
  <div class="container nav-inner">
    <a class="brand" href="{e(home)}"><span class="mark" aria-hidden="true">{mark}</span>
      <span>{e(site['brand'])}<small>Research hub</small></span></a>
    {nav}{spacer}
    <div class="nav-actions">
      <a class="gh-link" href="{e(person['github'])}">GitHub <span aria-hidden="true">↗</span></a>
      <button class="icon-btn theme-btn" id="theme-toggle" type="button" aria-label="Switch theme">
        <svg class="i-moon" viewBox="0 0 24 24" aria-hidden="true"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>
        <svg class="i-sun" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M4.93 19.07l1.41-1.41M17.66 6.34l1.41-1.41"/></svg>
      </button>
      {menu}
    </div>
  </div>
</header>"""


def footer(d: dict, today: dt.date) -> str:
    site, person = d["site"], d["person"]
    start = 2026
    years = f"{start}" if today.year <= start else f"{start}–{today.year}"
    session = next((x for x in d["docs"] if x["title"] == "SESSION_START.md"), None)
    session_link = f'<a href="{e(session["url"])}">For AI sessions: SESSION_START.md</a>' if session else ""
    return f"""
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <p><strong>{e(site['title'])}</strong><br>© {years} {e(person['name_en'])} (<span lang="ko">{e(person['name_ko'])}</span>)</p>
      <nav class="footer-links" aria-label="Footer">
        <a href="{e(person['github'])}">GitHub</a>
        <a href="{e(site['repo'])}">Source of this page</a>
        {session_link}
        <a href="mailto:{e(person['email'])}">Email</a>
      </nav>
    </div>
    <p class="footer-meta">Updated {today.isoformat()} · generated from program.toml by build.py</p>
  </div>
</footer>"""


def minify_css(css: str) -> str:
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    css = re.sub(r"\s+", " ", css)
    css = re.sub(r"\s*([{};,>])\s*", r"\1", css)
    return css.replace(";}", "}").strip()


def head(d: dict, css: str, *, title: str, canonical: str, base: str, robots: str = "") -> str:
    site, person = d["site"], d["person"]
    desc = site["description"]
    og_image = f"{site['url']}assets/og.png"
    og_alt = "The question “How do humans come to see something new?” beside a Karnaugh map checkerboard"
    ld = [
        {"@context": "https://schema.org", "@type": "WebSite", "name": site["title"], "url": site["url"], "inLanguage": "en"},
        {
            "@context": "https://schema.org", "@type": "Person", "name": person["name_en"],
            "alternateName": person["name_ko"], "url": site["url"], "sameAs": [person["github"]],
            "description": person["role_en"],
            "affiliation": {"@type": "CollegeOrUniversity", "name": "Inha Technical College"},
        },
    ]
    ld_json = json.dumps(ld, ensure_ascii=False).replace("</", "<\\/")
    robots_tag = f'<meta name="robots" content="{robots}">' if robots else ""
    return f"""<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="keywords" content="{e(', '.join(site['keywords']))}">
<meta name="author" content="{e(person['name_en'])}">
{robots_tag}
<link rel="canonical" href="{e(canonical)}">
<meta name="color-scheme" content="dark light">
<meta name="theme-color" media="(prefers-color-scheme: dark)" content="#0d0f17">
<meta name="theme-color" media="(prefers-color-scheme: light)" content="#fbfbf9">
<link rel="icon" href="{base}assets/favicon.svg" type="image/svg+xml">
<link rel="preload" href="{base}assets/fonts/plus-jakarta-sans-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{base}assets/fonts/newsreader-latin-500-normal.woff2" as="font" type="font/woff2" crossorigin>
<meta property="og:type" content="website">
<meta property="og:site_name" content="{e(site['title'])}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{e(canonical)}">
<meta property="og:locale" content="en_US">
<meta property="og:image" content="{e(og_image)}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{e(og_alt)}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(title)}">
<meta name="twitter:description" content="{e(desc)}">
<meta name="twitter:image" content="{e(og_image)}">
<script type="application/ld+json">{ld_json}</script>
<script>{THEME_INIT}</script>
<style>{css}</style>
</head>"""


# ---------------------------------------------------------------- sections

def kmap() -> str:
    """The four-variable XOR function on a Karnaugh map: the checkerboard the program began with."""
    gray = ["00", "01", "11", "10"]
    cells = ["<span></span>"] + [f'<span aria-hidden="true">{c}</span>' for c in gray]
    for r in gray:
        cells.append(f'<span aria-hidden="true">{r}</span>')
        for c in gray:
            v = (r + c).count("1") % 2
            on = " on" if v else ""
            cells.append(f'<span class="kmap-cell{on}" aria-hidden="true">{v}</span>')
    return (
        '<figure class="kmap"><div class="kmap-grid" role="img" '
        'aria-label="Karnaugh map of the four-variable XOR function: the ones form a checkerboard">'
        + "".join(cells)
        + "</div><figcaption>F = A ⊕ B ⊕ C ⊕ D on a Karnaugh map (rows AB, columns CD). "
        "The checkerboard where the program began.</figcaption></figure>"
    )


def hero(d: dict) -> str:
    person, program = d["person"], d["program"]
    papers = d["papers"]
    n_current = sum(1 for p in papers if p["status"] == "current")
    n_archived = sum(1 for p in papers if p["status"] == "archived")
    n_ko = sum(1 for p in papers if p["lang"] == "ko")
    question = e(program["question"]).replace("see something new", "<em>see something new</em>")
    facts = [
        f"{n_current} current paper{'s' if n_current != 1 else ''}",
        f"{n_archived} archived note{'s' if n_archived != 1 else ''}",
        f"{n_ko} of {len(papers)} paper pages are in Korean (marked KO)",
    ]
    facts_html = "".join(f"<span>{e(f)}</span>" for f in facts)
    return f"""
<section class="hero" aria-labelledby="hero-title">
  <div class="container hero-grid">
    <div>
      <p class="who"><strong>{e(person['name_en'])} · <span lang="ko">{e(person['name_ko'])}</span></strong>
        <span>{e(person['role_en'])}</span></p>
      <h1 id="hero-title">{question}</h1>
      <p class="lead">{e(program['lead'])}</p>
      <div class="cta">
        <a class="btn btn--primary" href="#current">Read the current papers <span aria-hidden="true">↓</span></a>
        <a class="btn" href="{e(person['github'])}">GitHub profile <span aria-hidden="true">↗</span></a>
      </div>
      <p class="facts">{facts_html}</p>
    </div>
    {kmap()}
  </div>
</section>"""


def split_title(title: str) -> tuple[str, str]:
    """Split "Main title: subtitle" for display; short or unusual titles stay whole."""
    head, sep, tail = title.partition(": ")
    if sep and len(head.split()) >= 3 and len(tail.split()) >= 3:
        return head, tail
    return title, ""


def paper_card(p: dict, compact: bool = False) -> str:
    page, repo = paper_page(p), paper_repo(p)
    cls = "card card--compact" if compact else "card card--current"
    main_title, sub_title = split_title(p["title_en"])
    sub_html = f'<p class="subtitle">{nb(sub_title)}</p>' if sub_title else ""
    ko = f'<p class="title-ko" lang="ko">{e(p["title_ko"])}</p>' if p["title_ko"] else ""
    tags = "".join(f"<li>{e(t)}</li>" for t in p["tags"])
    tags_html = f'<ul class="tags" aria-label="Topics">{tags}</ul>' if tags else ""
    links = []
    if page:
        verb = "Open the page" if compact else "Read the paper"
        links.append(ext_link(page, verb, sr=f"(Paper {p['id']})", arrow="→"))
        for extra in p["extra_links"]:
            links.append(ext_link(f"{page}{extra['path']}", extra["label"], sr=f"(Paper {p['id']})", arrow="→"))
    links.append(ext_link(repo, "GitHub", sr=f"repository of Paper {p['id']}"))
    return f"""
      <article class="{cls}" id="paper-{p['id']}">
        <div class="chips">
          <span class="chip chip--id">Paper {p['id']}</span>{status_chip(p)}{lang_chip(p['lang'], 'Page' if page else 'Repository')}<span class="chip">{e(p['role'])}</span>
        </div>
        <h3>{nb(main_title)}</h3>
        {sub_html}
        {ko}
        <p class="summary">{e(p['summary'])}</p>
        {tags_html}
        <div class="card-links">{''.join(links)}</div>
      </article>"""


def current_section(d: dict) -> str:
    current = [p for p in d["papers"] if p["status"] == "current"]
    progress = [p for p in d["papers"] if p["status"] == "in-progress"]
    if not current and not progress:
        return ""
    body = f'<div class="grid-2">{"".join(paper_card(p) for p in current)}</div>' if current else ""
    if progress:
        body += (
            '<h3 class="sub-title">In progress</h3>'
            f'<div class="grid-2">{"".join(paper_card(p, compact=True) for p in progress)}</div>'
        )
    note = '<p class="map-note">Pages marked KO are written in Korean. The Korean title sits under each English title.</p>'
    return f"""
<section class="section" id="current" aria-labelledby="current-title">
  <div class="container">
    {section_head("Current work", "Where to start", "current-title", d["program"]["current_intro"])}
    {body}
    {note}
  </div>
</section>"""


def map_section(d: dict) -> str:
    by_id = {p["id"]: p for p in d["papers"]}
    rows = []
    for layer in d["layers"]:
        chips = []
        for pid in layer["papers"]:
            p = by_id.get(pid)
            if not p:
                continue
            target = paper_page(p) or paper_repo(p)
            short, _ = LANGS[p["lang"]]
            chips.append(
                f'<a class="paper-link" href="{e(target)}"><b>P{p["id"]}</b> {e(p["short"])}'
                f'<span class="lang-tag" aria-hidden="true">{short}</span>'
                f'<span class="sr-only"> (page language: {LANGS[p["lang"]][1]})</span></a>'
            )
        if not chips:
            continue
        extra = " layer--synthesis" if layer["id"] == "synthesis" else ""
        rows.append(
            f'<div class="layer{extra}"><div><div class="layer-label">{e(layer["label"])}</div>'
            f'<h3>{nb(layer["title"])}</h3><p>{nb(layer["desc"])}</p></div>'
            f'<div class="layer-papers">{"".join(chips)}</div></div>'
        )
    joined = '<div class="map-arrow" aria-hidden="true">↓</div>'.join(rows)
    return f"""
<section class="section section--soft" id="map" aria-labelledby="map-title">
  <div class="container">
    {section_head("Program map", "How the papers fit together", "map-title", d["program"]["map_intro"])}
    <div class="map">{joined}</div>
    <p class="map-note">Dashed outlines mark archived papers.</p>
  </div>
</section>"""


def archive_section(d: dict) -> str:
    archived = [p for p in d["papers"] if p["status"] == "archived"]
    if not archived:
        return ""
    count = NUMBER_WORDS.get(len(archived), str(len(archived)))
    cards = "".join(paper_card(p, compact=True) for p in archived)
    return f"""
<section class="section" id="archive" aria-labelledby="archive-title">
  <div class="container">
    {section_head("Archive", f"Papers {ranges([p['id'] for p in archived])}", "archive-title", d["program"]["archive_note"])}
    <details class="archive" id="archive-list">
      <summary><span>Show the {count} archived papers</span><span class="hint">read-only since 2026-10-18</span></summary>
      <div class="archive-body"><div class="grid-3">{cards}</div></div>
    </details>
  </div>
</section>"""


def genealogy_section(d: dict) -> str:
    steps = d["genealogy"]
    items = []
    for i, step in enumerate(steps):
        cls = ' class="is-current"' if i == len(steps) - 1 else ""
        items.append(f'<li{cls}><h3>{nb(step["title"])}</h3><p>{nb(step["note"])}</p></li>')
    return f"""
<section class="section section--soft" id="genealogy" aria-labelledby="genealogy-title">
  <div class="container">
    {section_head("Concept genealogy", "How the ideas actually arrived", "genealogy-title",
                  "The real order of discovery, not a logical reconstruction.")}
    <ol class="timeline">{"".join(items)}</ol>
    <p class="threads">{e(d["program"]["threads"])}</p>
  </div>
</section>"""


def documents_section(d: dict) -> str:
    cards = []
    for doc in d["docs"]:
        cards.append(
            f'<article class="card card--compact card--stretch"><div class="chips"><span class="chip">{e(doc["badge"])}</span>'
            f'{lang_chip(doc["lang"], "Document")}</div>'
            f'<h3 class="doc-title"><a class="stretch" href="{e(doc["url"])}">{e(doc["title"])}</a></h3>'
            f'<p class="desc">{e(doc["desc"])}</p></article>'
        )
    return f"""
<section class="section" id="documents" aria-labelledby="documents-title">
  <div class="container">
    {section_head("Documents", "Where the program is recorded", "documents-title",
                  "The working documents behind the papers. They are rendered on GitHub.")}
    <div class="grid-2">{"".join(cards)}</div>
  </div>
</section>"""


def beyond_section(d: dict) -> str:
    beyond = d["beyond"]
    repos = beyond.get("repos", [])
    if not repos:
        return ""
    cards = []
    for r in repos:
        url = f"{GITHUB_BASE}{r['repo']}"
        cards.append(
            f'<article class="card card--compact card--stretch"><div class="chips"><span class="chip chip--repo">inha20/{e(r["repo"])}</span>'
            f'{lang_chip(r["lang"], "Repository")}</div>'
            f'<h3><a class="stretch" href="{e(url)}">{e(r["title"])}</a></h3><p class="desc">{e(r["desc"])}</p></article>'
        )
    return f"""
<section class="section section--soft" id="beyond" aria-labelledby="beyond-title">
  <div class="container">
    {section_head("Beyond the research", "Other work on this account", "beyond-title", beyond["intro"])}
    <div class="grid-3">{"".join(cards)}</div>
    <p class="map-note">{ext_link(beyond["all_url"], "See all repositories on GitHub")}</p>
  </div>
</section>"""


def about_section(d: dict) -> str:
    person, site = d["person"], d["site"]
    interests = "".join(f'<li class="chip">{e(i)}</li>' for i in person["interests"])
    keywords = " ".join(f"<li>{e(k)}</li>" for k in site["keywords"])
    session = next((x for x in d["docs"] if x["title"] == "SESSION_START.md"), None)
    session_row = (
        f'<dt>AI sessions</dt><dd><a href="{e(session["url"])}">SESSION_START.md</a></dd>' if session else ""
    )
    gh_label = urlparse(person["github"]).netloc + urlparse(person["github"]).path
    return f"""
<section class="section" id="about" aria-labelledby="about-title">
  <div class="container">
    {section_head("About", f"{person['name_en']} · {person['name_ko']}", "about-title")}
    <div class="about-grid">
      <div>
        <p>{e(person['bio'])}</p>
        <p class="muted">{e(person['method'])}</p>
        <div class="kw"><span class="eyebrow">Research interests</span><ul class="chips">{interests}</ul></div>
        <div class="kw"><span class="eyebrow">Keywords</span><ul class="kw-line">{keywords}</ul></div>
      </div>
      <aside class="contact" aria-label="Contact">
        <h3>Contact</h3>
        <dl>
          <dt>Email</dt><dd><a href="mailto:{e(person['email'])}">{e(person['email'])}</a></dd>
          <dt>GitHub</dt><dd><a href="{e(person['github'])}">{e(gh_label)}</a></dd>
          <dt>Role</dt><dd>{e(person['role_en'])}<br><span lang="ko">{e(person['role_ko'])}</span></dd>
          {session_row}
        </dl>
      </aside>
    </div>
  </div>
</section>"""


# ---------------------------------------------------------------- pages

def page(d: dict, css: str, js: str, today: dt.date) -> str:
    site, person = d["site"], d["person"]
    title = f"{site['title']} — {person['name_en']} ({person['name_ko']})"
    body = (
        header(d)
        + '<main id="main">'
        + hero(d)
        + current_section(d)
        + map_section(d)
        + archive_section(d)
        + genealogy_section(d)
        + documents_section(d)
        + beyond_section(d)
        + about_section(d)
        + "</main>"
        + footer(d, today)
    )
    return (
        '<!DOCTYPE html>\n<html lang="en">\n'
        + head(d, css, title=title, canonical=site["url"], base="")
        + '\n<body id="top">\n<a class="skip-link" href="#main">Skip to content</a>'
        + body
        + f"\n<script>{js}</script>\n</body>\n</html>\n"
    )


def not_found(d: dict, css: str, js: str, today: dt.date) -> str:
    site = d["site"]
    base = urlparse(site["url"]).path  # e.g. /Research-Portfolio/ — 404 pages can be served from any depth
    css = css.replace("url(assets/", f"url({base}assets/")
    title = f"Page not found — {site['title']}"
    body = (
        header(d, full=False).replace('href="assets/', f'href="{base}assets/')
        + '<main id="main"><div class="container"><div class="notfound"><span class="eyebrow">404</span>'
        "<h1>That page is not here.</h1>"
        "<p>The link may be old. The research hub has the current papers, the program map and the archive.</p>"
        f'<a class="btn btn--primary" href="{e(site["url"])}">Go to the research hub <span aria-hidden="true">→</span></a>'
        "</div></div></main>"
        + footer(d, today)
    )
    return (
        '<!DOCTYPE html>\n<html lang="en">\n'
        + head(d, css, title=title, canonical=site["url"], base=base, robots="noindex")
        + '\n<body id="top">\n<a class="skip-link" href="#main">Skip to content</a>'
        + body
        + f"\n<script>{js}</script>\n</body>\n</html>\n"
    )


def normalise(text: str) -> str:
    return re.sub(r"Updated \d{4}-\d{2}-\d{2}", "Updated DATE", text)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="exit 1 if the committed files are out of date")
    ap.add_argument("--include-hidden", action="store_true", help="also render papers with show = false")
    ap.add_argument("--out", type=Path, default=ROOT, help="output directory (default: this folder)")
    args = ap.parse_args()

    try:
        data = load(args.include_hidden)
    except (BuildError, OSError, tomllib.TOMLDecodeError) as err:
        print(f"error: {err}", file=sys.stderr)
        return 2

    css = minify_css((ROOT / "src" / "site.css").read_text(encoding="utf-8"))
    js = (ROOT / "src" / "site.js").read_text(encoding="utf-8").strip()
    today = dt.date.today()
    outputs = {
        "index.html": page(data, css, js, today),
        "404.html": not_found(data, css, js, today),
    }

    if args.check:
        stale = [
            name for name, text in outputs.items()
            if not (args.out / name).exists() or normalise((args.out / name).read_text(encoding="utf-8")) != normalise(text)
        ]
        if stale:
            print("out of date: " + ", ".join(stale) + " — run `python build.py` and commit the result", file=sys.stderr)
            return 1
        print("up to date")
        return 0

    args.out.mkdir(parents=True, exist_ok=True)
    for name, text in outputs.items():
        (args.out / name).write_text(text, encoding="utf-8")
        print(f"wrote {args.out / name} ({len(text.encode('utf-8')) / 1024:.1f} KB)")
    shown = data["papers"]
    print(
        f"{len(shown)} papers shown ({sum(p['status'] == 'current' for p in shown)} current, "
        f"{sum(p['status'] == 'archived' for p in shown)} archived), {len(data['hidden'])} hidden"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
