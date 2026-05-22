#!/usr/bin/env python3
"""Local-only helper: extract the zero-width README payload for testing."""

from __future__ import annotations

import argparse
from pathlib import Path

ZERO = "\u200b"
ONE = "\u200c"


def decode_zero_width(source: str) -> str:
    bits = ["0" if char == ZERO else "1" for char in source if char in (ZERO, ONE)]
    if len(bits) % 8 != 0:
        raise ValueError(f"Hidden bit count is not byte-aligned: {len(bits)} bits")
    data = bytes(int("".join(bits[i:i + 8]), 2) for i in range(0, len(bits), 8))
    return data.decode("utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("readme", nargs="?", default="README.md")
    args = parser.parse_args()
    print(decode_zero_width(Path(args.readme).read_text(encoding="utf-8")))


if __name__ == "__main__":
    main()
