#!/usr/bin/env python3
"""Check that the hub never scrolls sideways, at every width from 320 to 1600 px.

    pip install playwright        # plus a Chrome or Chromium it can launch
    python tools/check_layout.py
    python tools/check_layout.py --chrome /usr/bin/google-chrome --step 5

Serves this folder on a local port, opens index.html and 404.html at each width in
both color schemes, and exits with status 1 if any width overflows.
A width that lies between two layouts is the usual culprit, so the step is small.
"""
from __future__ import annotations

import argparse
import functools
import http.server
import sys
import threading
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class Handler(http.server.SimpleHTTPRequestHandler):
    """Serves the folder quietly. 404.html links its assets under /Research-Portfolio/
    (the address on GitHub Pages), so that prefix is mapped back to the folder."""

    def translate_path(self, path: str) -> str:
        if path.startswith("/Research-Portfolio/"):
            path = path[len("/Research-Portfolio"):]
        return super().translate_path(path)

    def log_message(self, *args, **kwargs) -> None:
        pass


def serve() -> http.server.ThreadingHTTPServer:
    handler = functools.partial(Handler, directory=str(ROOT))
    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--chrome", help="path to a Chrome/Chromium executable (default: Playwright's own)")
    ap.add_argument("--step", type=int, default=10, help="width step in px (default 10)")
    args = ap.parse_args()
    from playwright.sync_api import sync_playwright

    server = serve()
    base = f"http://127.0.0.1:{server.server_address[1]}/"
    bad: list[str] = []
    with sync_playwright() as p:
        kw = {"executable_path": args.chrome} if args.chrome else {}
        browser = p.chromium.launch(args=["--no-sandbox"], **kw)
        for page_name in ("index.html", "404.html"):
            for scheme in ("dark", "light"):
                ctx = browser.new_context(viewport={"width": 1440, "height": 800}, color_scheme=scheme)
                page = ctx.new_page()
                page.goto(base + page_name, wait_until="networkidle")
                for width in range(320, 1601, args.step):
                    page.set_viewport_size({"width": width, "height": 800})
                    page.wait_for_timeout(15)
                    scroll_w, client_w = page.evaluate(
                        "[document.documentElement.scrollWidth, document.documentElement.clientWidth]"
                    )
                    if scroll_w > client_w:
                        bad.append(f"{page_name} {scheme} at {width}px: content is {scroll_w}px wide")
                ctx.close()
        browser.close()
    server.shutdown()
    if bad:
        print("\n".join(bad))
        return 1
    print(f"no sideways scrolling from 320 to 1600 px (step {args.step}), both pages, both color schemes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
