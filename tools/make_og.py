#!/usr/bin/env python3
"""Render assets/og.png (1200x630), the image shown when the hub link is shared.

Only needed when the preview text or design changes; the PNG itself is committed.

    pip install playwright        # plus a Chrome or Chromium it can launch
    python tools/make_og.py                       # uses Playwright's own browser
    python tools/make_og.py --chrome /usr/bin/google-chrome

The hub's three fonts are read from assets/fonts and embedded, so the image
matches the page. The map is the same Karnaugh map as the hero:
F = A xor B xor C xor D, rows AB and columns CD in Gray-code order.
"""
from __future__ import annotations

import argparse
import base64
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FONTS = ROOT / "assets" / "fonts"
OUT = ROOT / "assets" / "og.png"

GRAY = ["00", "01", "11", "10"]


def font_face(family: str, file: str, weight: int, style: str = "normal") -> str:
    data = base64.b64encode((FONTS / file).read_bytes()).decode()
    return (
        f"@font-face{{font-family:'{family}';font-weight:{weight};font-style:{style};"
        f"src:url(data:font/woff2;base64,{data}) format('woff2')}}"
    )


def kmap_cells() -> str:
    cells = []
    for r in range(4):
        for c in range(4):
            on = (r + c) % 2 == 1
            cells.append(f'<div class="cell{" on" if on else ""}">{1 if on else 0}</div>')
    return "".join(cells)


def build_html() -> str:
    faces = "".join(
        [
            font_face("Newsreader", "newsreader-latin-500-normal.woff2", 500),
            font_face("Newsreader", "newsreader-latin-400-italic.woff2", 400, "italic"),
            font_face("Plus Jakarta Sans", "plus-jakarta-sans-latin-500-normal.woff2", 500),
            font_face("Plus Jakarta Sans", "plus-jakarta-sans-latin-600-normal.woff2", 600),
            font_face("JetBrains Mono", "jetbrains-mono-latin-400-normal.woff2", 400),
        ]
    )
    cols = "".join(f"<span>{g}</span>" for g in GRAY)
    rows = "".join(f"<span>{g}</span>" for g in GRAY)
    return f"""<!doctype html><html lang="en"><meta charset="utf-8"><style>
{faces}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:1200px;height:630px;background:#0d0f17;color:#eef0f8;overflow:hidden}}
body{{font-family:'Plus Jakarta Sans','Noto Sans CJK KR','Noto Sans KR',sans-serif;position:relative}}
.frame{{position:absolute;inset:28px;border:1px solid #2a2f45;border-radius:22px}}
.left{{position:absolute;left:84px;top:84px;width:640px;bottom:84px;display:flex;flex-direction:column}}
.label{{font-family:'JetBrains Mono',monospace;font-size:19px;letter-spacing:.12em;text-transform:uppercase;color:#9097b2}}
h1{{margin-top:34px;font-family:'Newsreader',serif;font-weight:500;font-size:86px;line-height:1.04;letter-spacing:-.025em}}
h1 em{{font-style:italic;font-weight:400;color:#6cb0ff}}
.who{{margin-top:auto;font-size:27px;font-weight:600}}
.role{{margin-top:6px;font-size:21px;font-weight:500;color:#a9aec6}}
.url{{margin-top:22px;font-family:'JetBrains Mono',monospace;font-size:19px;color:#6cb0ff}}
.map{{position:absolute;right:92px;top:130px;width:352px}}
.cols{{display:grid;grid-template-columns:34px repeat(4,1fr);gap:10px;margin-bottom:8px;font-family:'JetBrains Mono',monospace;font-size:15px;color:#9097b2;text-align:center}}
.body{{display:grid;grid-template-columns:34px 1fr;gap:10px}}
.rows{{display:grid;grid-template-rows:repeat(4,1fr);gap:10px;font-family:'JetBrains Mono',monospace;font-size:15px;color:#9097b2}}
.rows span{{display:flex;align-items:center}}
.grid{{display:grid;grid-template-columns:repeat(4,1fr);grid-template-rows:repeat(4,1fr);gap:10px;aspect-ratio:1/1}}
.cell{{display:flex;align-items:center;justify-content:center;border-radius:11px;border:1px solid #2a2f45;background:#151826;font-family:'JetBrains Mono',monospace;font-size:24px;color:#9097b2}}
.cell.on{{background:#6cb0ff;border-color:#6cb0ff;color:#0d0f17;font-weight:500}}
.cap{{margin-top:22px;font-family:'JetBrains Mono',monospace;font-size:15px;line-height:1.5;color:#9097b2}}
</style>
<div class="frame"></div>
<div class="left">
  <div class="label">Structure Recognition Research Program</div>
  <h1>How do humans come to <em>see something new</em>?</h1>
  <div class="who">Jonghun Choi · 최종훈</div>
  <div class="role">Independent researcher · Inha Technical College</div>
  <div class="url">inha20.github.io/Research-Portfolio</div>
</div>
<div class="map">
  <div class="cols"><span></span>{cols}</div>
  <div class="body"><div class="rows">{rows}</div><div class="grid">{kmap_cells()}</div></div>
  <div class="cap">F = A ⊕ B ⊕ C ⊕ D on a Karnaugh map</div>
</div>
</html>"""


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--chrome", help="path to a Chrome/Chromium executable (default: Playwright's own)")
    args = ap.parse_args()
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        kw = {"executable_path": args.chrome} if args.chrome else {}
        browser = p.chromium.launch(args=["--no-sandbox"], **kw)
        page = browser.new_page(viewport={"width": 1200, "height": 630}, device_scale_factor=1)
        page.set_content(build_html(), wait_until="load")
        page.evaluate("document.fonts.ready")
        page.wait_for_timeout(200)
        page.screenshot(path=str(OUT), clip={"x": 0, "y": 0, "width": 1200, "height": 630})
        browser.close()
    print(f"wrote {OUT.relative_to(ROOT)} ({OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
