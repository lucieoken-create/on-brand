#!/usr/bin/env python3
"""Check WCAG contrast between colors.

Part of the on-brand skill. Standard library only.

    python3 contrast.py "#1D2B3A" "#FAF7F2"          # one pair: text, then background
    python3 contrast.py --all "#1D2B3A" "#FAF7F2" "#E8664A" "#8FA68E"   # every pair
    python3 contrast.py --tokens tokens.css         # every pair of colors in a tokens file

Passing levels: 4.5:1 for body text, 3:1 for large text (about 24px+, or 19px+ bold) and for
icons and borders that matter. 7:1 is the stricter AAA level for body text.
"""

import argparse
import itertools
import re
import sys

HEX = re.compile(r"#(?:[0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b")


def norm(h):
    h = h.strip().lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    if not re.fullmatch(r"[0-9a-fA-F]{6}", h):
        raise ValueError(f"Not a hex color: #{h}")
    return "#" + h.upper()


def norm_safe(h):
    try:
        return norm(h)
    except ValueError:
        return None


def luminance(h):
    h = norm(h)[1:]
    chans = []
    for i in (0, 2, 4):
        c = int(h[i:i + 2], 16) / 255
        chans.append(c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4)
    r, g, b = chans
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(a, b):
    la, lb = luminance(a), luminance(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def verdict(r):
    if r >= 7:
        return "passes for all text (AAA)"
    if r >= 4.5:
        return "passes for body text"
    if r >= 3:
        return "large text and icons only"
    return "fails: don't use for text"


def tokens_from_css(path):
    named = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            m = re.search(r"(--[\w-]+)\s*:\s*(#[0-9a-fA-F]{3,6})\b", line)
            if m:
                named.append((m.group(1), norm(m.group(2))))
    return named


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("colors", nargs="*", help="Hex colors")
    ap.add_argument("--all", action="store_true", help="Check every pair of the colors given")
    ap.add_argument("--tokens", help="Path to a tokens.css file; checks every pair of its hex colors")
    args = ap.parse_args()

    if args.tokens:
        named = tokens_from_css(args.tokens)
    else:
        try:
            named = [(c, norm(c)) for c in args.colors]
        except ValueError as e:
            sys.exit(str(e))

    if len(named) < 2:
        sys.exit("Give at least two colors, or --tokens with a tokens.css file.")

    pairs = itertools.combinations(named, 2) if (args.all or args.tokens or len(named) > 2) else [tuple(named)]
    rows = sorted(((ratio(a[1], b[1]), a, b) for a, b in pairs), key=lambda r: -r[0])
    for r, a, b in rows:
        name_a = a[1] if norm_safe(a[0]) == a[1] else f"{a[0]} ({a[1]})"
        name_b = b[1] if norm_safe(b[0]) == b[1] else f"{b[0]} ({b[1]})"
        print(f"{r:5.2f}:1  {name_a} on {name_b}  {verdict(r)}")


if __name__ == "__main__":
    main()
