#!/usr/bin/env python3
"""Write an Adobe swatch exchange file (.ase) from a brand's colors.

Illustrator, Photoshop and InDesign load it from the Swatches panel, and a
Creative Cloud Library can save the colors from there. Standard library only.

Colors come from DESIGN.md's front matter, or from name=#hex pairs:

    python3 scripts/make_ase.py kit/brand-colors.ase --design DESIGN.md
    python3 scripts/make_ase.py kit/brand-colors.ase --group "Brand" "Navy=#1D2B3A" "Cream=#FAF7F2"

With --design, each color is named from its comment when the comment starts
with a name and a colon (primary: "#1D2B3A"  # Navy: all text), otherwise
from its token name. The file opens as one swatch group named after the brand.
"""
import argparse
import re
import struct
import sys

HEX = re.compile(r"^#?([0-9a-fA-F]{6})$")


def utf16(name):
    data = (name + "\0").encode("utf-16-be")
    return struct.pack(">H", len(data) // 2) + data


def block(kind, body):
    return struct.pack(">HI", kind, len(body)) + body


def color_block(name, hex6):
    r, g, b = (int(hex6[i:i + 2], 16) / 255 for i in (0, 2, 4))
    # model RGB, three big-endian floats, color type 2 (normal, not global or spot)
    return block(0x0001, utf16(name) + b"RGB " + struct.pack(">fffH", r, g, b, 2))


def write_ase(path, group, colors):
    blocks = [block(0xC001, utf16(group))] if group else []
    blocks += [color_block(n, h) for n, h in colors]
    if group:
        blocks.append(block(0xC002, b""))
    with open(path, "wb") as f:
        f.write(b"ASEF" + struct.pack(">HHI", 1, 0, len(blocks)) + b"".join(blocks))


def from_design(path):
    text = open(path, encoding="utf-8").read()
    front = text.split("---")[1] if text.startswith("---") else text
    name_m = re.search(r"^name:\s*(.+)$", front, re.M)
    colors, inside = [], False
    for line in front.splitlines():
        if re.match(r"^colors:\s*$", line):
            inside = True
            continue
        if inside and line and not line.startswith((" ", "\t")):
            break
        m = re.match(r'^\s+([\w-]+):\s*["\']?(#[0-9a-fA-F]{6})["\']?\s*(?:#\s*(.*))?$', line) if inside else None
        if m:
            token, hex_, comment = m.groups()
            label = token
            if comment and ":" in comment:
                label = comment.split(":", 1)[0].strip()
            colors.append((label, hex_))
    brand = name_m.group(1).strip().strip("\"'") if name_m else None
    return brand, colors


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("out", help="path for the .ase file")
    ap.add_argument("pairs", nargs="*", help='name=#hex, e.g. "Navy=#1D2B3A"')
    ap.add_argument("--design", help="read colors from this DESIGN.md")
    ap.add_argument("--group", help="swatch group name (defaults to the brand name in DESIGN.md)")
    a = ap.parse_intermixed_args()

    group, colors = (from_design(a.design) if a.design else (None, []))
    for p in a.pairs:
        if "=" not in p:
            sys.exit(f"Not a name=#hex pair: {p}")
        n, h = p.rsplit("=", 1)
        colors.append((n.strip(), h.strip()))
    clean = []
    for n, h in colors:
        m = HEX.match(h)
        if not m:
            sys.exit(f"Not a six-digit hex color: {n}={h}")
        clean.append((n, m.group(1).upper()))
    if not clean:
        sys.exit("No colors found. Pass --design DESIGN.md or name=#hex pairs.")
    write_ase(a.out, a.group or group, clean)
    print(f"Wrote {len(clean)} colors to {a.out}" + (f" in group '{a.group or group}'" if (a.group or group) else ""))
    for n, h in clean:
        print(f"  {n}: #{h}")


if __name__ == "__main__":
    main()
