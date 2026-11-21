#!/usr/bin/env python3
"""Entry program for make.fun news-image-20261120.

Copies the bundled front-page image (entry.png, sitting next to this
file in the repository) to the output directory as entry.png.
Standard library only, no network, fully deterministic: the same
bytes in, the same bytes out, on every run.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(OUT_DIR, "entry.png")


def main():
    if not os.path.isfile(SRC):
        raise SystemExit(f"missing bundled image: {SRC}")
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, DST)
    if os.path.getsize(DST) != os.path.getsize(SRC):
        raise SystemExit("output size mismatch after copy")


if __name__ == "__main__":
    main()
