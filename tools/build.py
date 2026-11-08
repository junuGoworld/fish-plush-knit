#!/usr/bin/env python3
"""Rebuild index.html (the fish plush page) from src/fish-plush.

The page is one self-contained HTML file: the template holds the UI, styles and
the simulation module; fishdraw (MIT, Lingdong Huang) is inlined where the
template says /*FISHDRAW*/.

Usage:  python3 tools/build.py
"""
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "src" / "fish-plush"
OUT = ROOT / "index.html"

RESET = ('<style>:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);'
         'padding-bottom:env(safe-area-inset-bottom,0px)}'
         'body{margin:0;font:14px/1.4 system-ui,sans-serif}img{max-width:100%}'
         '[hidden]{display:none!important}</style>')


def wrap(fragment: str) -> str:
    """Turn a page fragment (title/style first, then body markup) into a full document."""
    m = re.match(r"(\s*<title>.*?</style>\s*)", fragment, re.S)
    head, body = (m.group(1), fragment[m.end():]) if m else ("", fragment)
    return ("<!doctype html>\n<html lang=\"ko\">\n<head>\n<meta charset=\"utf-8\">\n"
            "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1,viewport-fit=cover\">\n"
            f"{RESET}\n{head.strip()}\n</head>\n<body>\n{body.strip()}\n</body>\n</html>\n")


def main() -> None:
    template = (SRC / "page.template.html").read_text(encoding="utf-8")
    fishdraw = (SRC / "fishdraw.vendored.js").read_text(encoding="utf-8")
    if "</script" in fishdraw:
        raise SystemExit("fishdraw source contains </script and cannot be inlined")
    if template.count("/*FISHDRAW*/") != 1:
        raise SystemExit("template must contain exactly one /*FISHDRAW*/ placeholder")
    OUT.write_text(wrap(template.replace("/*FISHDRAW*/", fishdraw)), encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)} ({OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
