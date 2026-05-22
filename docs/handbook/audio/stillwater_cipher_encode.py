#!/usr/bin/env python3
"""
Stillwater no-key cipher encoder.

Pipeline:
1. Clean message: uppercase A-Z only, J becomes I.
2. Encode using a standard 5x5 Polybius/Bifid-style coordinate mix.
3. Apply a fixed "tide route" transposition.

This script is intentionally no-key:
- No password.
- No keyword alphabet.
- No secret phrase.
- The difficulty comes from identifying the method.

Example:
    python stillwater_cipher_encode.py "THE ROOM BELOW THE SWITCHBOARD OPENS AT LOW TIDE"

With Morse-friendly output:
    python stillwater_cipher_encode.py "THE ROOM BELOW THE SWITCHBOARD OPENS AT LOW TIDE" --group 5
"""

from __future__ import annotations

import argparse
import string

# Fixed non-secret route values.
# 7 ties naturally to the Codicology extension.
# Change it only if you also change your lore hints.
TIDE_WIDTH = 7


ALPHABET_36 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
GRID_SIZE = 6
TIDE_WIDTH = 7

def clean_text(text: str) -> str:
    cleaned = []

    for char in text.upper():
        if char in ALPHABET_36:
            cleaned.append(char)

    return "".join(cleaned)


def build_polybius_maps():
    to_coords = {}
    to_symbol = {}

    for index, symbol in enumerate(ALPHABET_36):
        row = index // GRID_SIZE + 1
        col = index % GRID_SIZE + 1
        to_coords[symbol] = (row, col)
        to_symbol[(row, col)] = symbol

    return to_coords, to_symbol


def bifid_encode(cleaned: str, period: int = 5) -> str:
    """
    Standard Bifid-style encoding with the normal alphabet square.

    For each block:
    - Convert letters to row/column coordinates.
    - Write all row numbers, then all column numbers.
    - Read the coordinate stream back as pairs.
    - Convert pairs back to letters.
    """
    to_coords, to_letter = build_polybius_maps()
    output = []

    for start in range(0, len(cleaned), period):
        block = cleaned[start:start + period]

        rows = []
        cols = []

        for letter in block:
            row, col = to_coords[letter]
            rows.append(row)
            cols.append(col)

        mixed = rows + cols

        for i in range(0, len(mixed), 2):
            pair = (mixed[i], mixed[i + 1])
            output.append(to_letter[pair])

    return "".join(output)


def tide_route_encode(text: str, width: int = TIDE_WIDTH) -> str:
    """
    Fixed route transposition.

    Write the text left-to-right in rows of width 7.
    Read columns left-to-right.
    Even columns read top-to-bottom.
    Odd columns read bottom-to-top.

    This creates a wave/tide pattern without needing a key.
    """
    if width <= 1:
        return text

    rows = [text[i:i + width] for i in range(0, len(text), width)]
    output = []

    for col in range(width):
        column_chars = []

        for row in rows:
            if col < len(row):
                column_chars.append(row[col])

        if col % 2 == 0:
            output.extend(column_chars)
        else:
            output.extend(reversed(column_chars))

    return "".join(output)


def stillwater_encode(message: str, bifid_period: int = 5, route_width: int = TIDE_WIDTH) -> str:
    cleaned = clean_text(message)
    first_pass = bifid_encode(cleaned, period=bifid_period)
    second_pass = tide_route_encode(first_pass, width=route_width)
    return second_pass


def group_text(text: str, group_size: int) -> str:
    if group_size <= 0:
        return text

    return " ".join(text[i:i + group_size] for i in range(0, len(text), group_size))


def show_grid() -> str:
    rows = []

    for i in range(0, len(ALPHABET_25), GRID_SIZE):
        rows.append(" ".join(ALPHABET_25[i:i + GRID_SIZE]))

    return "\n".join(rows)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Encode text using the no-key Stillwater Bifid + tide-route cipher."
    )

    parser.add_argument("message", help="Plaintext message to encode")
    parser.add_argument("--period", type=int, default=5, help="Bifid period. Default: 5")
    parser.add_argument("--width", type=int, default=TIDE_WIDTH, help="Route width. Default: 7")
    parser.add_argument("--group", type=int, default=5, help="Ciphertext grouping size. Default: 5")
    parser.add_argument("--no-group", action="store_true", help="Print ciphertext without spaces")
    parser.add_argument("--show-grid", action="store_true", help="Print the 5x5 alphabet grid")

    args = parser.parse_args()

    if args.period < 1:
        raise SystemExit("--period must be at least 1")

    if args.width < 1:
        raise SystemExit("--width must be at least 1")

    cleaned = clean_text(args.message)
    bifid = bifid_encode(cleaned, period=args.period)
    final = tide_route_encode(bifid, width=args.width)

    if args.show_grid:
        print("5x5 grid:")
        print(show_grid())
        print()

    print(f"cleaned:    {cleaned}")
    print(f"bifid:      {group_text(bifid, args.group)}")
    print(f"ciphertext: {final if args.no_group else group_text(final, args.group)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
