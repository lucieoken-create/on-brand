#!/usr/bin/env python3
"""Extract the visual design from a website or a saved HTML file.

Part of the on-brand skill. Standard library only, so it runs anywhere Python 3.8+ does.

    python3 extract_site.py https://example.com --pages 3
    python3 extract_site.py path/to/index.html

Prints JSON: custom properties, colors by frequency and context, fonts, Google Fonts,
font sizes, corner radii, the styles on key elements (body, headings, links, buttons),
shadows, theme color, logo and social-image candidates, image folders that look like an
illustration library, and notes about anything that limits the result. Values come from the CSS, so they're exact, but a page that builds its
styles with JavaScript will show less than a browser would.
"""

import argparse
import colorsys
import json
import os
import re
import sys
from collections import Counter, defaultdict
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse, parse_qs
from urllib.request import Request, urlopen

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36 on-brand/0.1"
MAX_BYTES = 3_000_000
MAX_STYLESHEETS = 20
TIMEOUT = 15

KEY_SELECTORS = ["html", "body", "h1", "h2", "h3", "p", "a", "button", ".button", ".btn", "nav", "header", "footer"]
KEY_PROPS = ["color", "background", "background-color", "font-family", "font-size", "font-weight",
             "letter-spacing", "line-height", "text-transform", "border-radius"]
GENERATORS = ["squarespace", "wix", "webflow", "shopify", "wordpress", "framer", "ghost", "hubspot", "showit", "carrd"]

HEX_RE = re.compile(r"#(?:[0-9a-fA-F]{8}|[0-9a-fA-F]{6}|[0-9a-fA-F]{4}|[0-9a-fA-F]{3})\b")
FUNC_RE = re.compile(r"\b(rgba?|hsla?)\(\s*([^)]+)\)", re.I)
VAR_RE = re.compile(r"var\(\s*(--[\w-]+)")
CUSTOM_PROP_RE = re.compile(r"(--[\w-]+)\s*:\s*([^;{}]+)")
RULE_RE = re.compile(r"([^{}]+)\{([^{}]*)\}")
IMPORT_RE = re.compile(r"@import\s+(?:url\()?\s*['\"]?([^'\")\s;]+)", re.I)
FONT_FACE_RE = re.compile(r"@font-face\s*\{([^}]*)\}", re.I)
COMMENT_RE = re.compile(r"/\*.*?\*/", re.S)


# ---------- fetching ----------

def is_url(s):
    return urlparse(s).scheme in ("http", "https")


def fetch(src, base_dir=None):
    """Return (text, error). src is a URL or a local path."""
    try:
        if is_url(src):
            req = Request(src, headers={"User-Agent": UA, "Accept": "text/html,text/css,*/*"})
            with urlopen(req, timeout=TIMEOUT) as r:
                raw = r.read(MAX_BYTES)
                charset = r.headers.get_content_charset() or "utf-8"
            return raw.decode(charset, errors="replace"), None
        path = src if os.path.isabs(src) or base_dir is None else os.path.join(base_dir, src)
        path = path.split("?")[0].split("#")[0]
        with open(path, "rb") as f:
            return f.read(MAX_BYTES).decode("utf-8", errors="replace"), None
    except Exception as e:  # network blocked, 403, missing file, etc.
        return None, f"{src}: {type(e).__name__}: {e}"


def norm_url(u):
    """Normalize a page URL so https://site.com and https://site.com/ count as one page."""
    if not is_url(u):
        return u
    p = urlparse(u.split("#")[0])
    path = p.path.rstrip("/") or ""
    q = ("?" + p.query) if p.query else ""
    return f"{p.scheme.lower()}://{p.netloc.lower()}{path}{q}"


def image_path(src):
    """Return the real image path, unwrapping Next.js /_next/image?url=... links."""
    if "/_next/image" in src:
        inner = parse_qs(urlparse(src).query).get("url", [""])[0]
        if inner:
            return inner
    return src


def resolve(ref, base, base_dir):
    if is_url(base):
        return urljoin(base, ref)
    if is_url(ref):
        return ref
    if ref.startswith("/"):
        return os.path.join(base_dir, ref.lstrip("/"))
    return os.path.normpath(os.path.join(os.path.dirname(base) if base_dir is None else base_dir, ref))


# ---------- HTML ----------

class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stylesheets, self.style_blocks, self.inline_styles = [], [], []
        self.theme_color, self.og_image, self.generator = None, None, None
        self.icons, self.logos, self.nav_links, self.google_fonts = [], [], [], []
        self.class_samples = []
        self.images, self.logo_elements = [], []
        self._in_style = False
        self._style_buf = []
        self._nav_depth = 0

    def handle_starttag(self, tag, attrs):
        a = {k.lower(): (v or "") for k, v in attrs}
        rel = a.get("rel", "").lower()
        if tag == "link" and "stylesheet" in rel and a.get("href"):
            self.stylesheets.append(a["href"])
            if "fonts.googleapis.com" in a["href"]:
                self.google_fonts.append(a["href"])
        elif tag == "link" and "icon" in rel and a.get("href"):
            self.icons.append(a["href"])
        elif tag == "link" and "fonts.googleapis.com" in a.get("href", ""):
            self.google_fonts.append(a["href"])
        elif tag == "meta":
            name = (a.get("name") or a.get("property") or "").lower()
            if name == "theme-color":
                self.theme_color = a.get("content")
            elif name in ("og:image", "twitter:image") and not self.og_image:
                self.og_image = a.get("content")
            elif name == "generator":
                self.generator = a.get("content")
        elif tag == "style":
            self._in_style, self._style_buf = True, []
        elif tag in ("nav", "header"):
            self._nav_depth += 1
        if tag == "a" and self._nav_depth and a.get("href"):
            self.nav_links.append(a["href"])
        if tag == "img" and a.get("src"):
            self.images.append(image_path(a["src"]))
        blob = " ".join([a.get("src", ""), a.get("alt", ""), a.get("class", ""), a.get("id", ""),
                         a.get("aria-label", "")]).lower()
        if "logo" in blob:
            if tag == "img" and a.get("src"):
                self.logos.append(a["src"])
            elif len(self.logo_elements) < 6:
                self.logo_elements.append(f"<{tag}> with 'logo' in its attributes (likely an inline SVG or a wordmark set in type)")
        if a.get("style"):
            self.inline_styles.append(a["style"])
        if a.get("class") and len(self.class_samples) < 400:
            self.class_samples.append(a["class"])

    def handle_endtag(self, tag):
        if tag == "style" and self._in_style:
            self.style_blocks.append("".join(self._style_buf))
            self._in_style = False
        elif tag in ("nav", "header") and self._nav_depth:
            self._nav_depth -= 1

    def handle_data(self, data):
        if self._in_style:
            self._style_buf.append(data)


# ---------- colors ----------

NAMED = {"white": "#ffffff", "black": "#000000"}


def to_hex(value):
    """Normalize a CSS color string to (#rrggbb, alpha) or None."""
    v = value.strip().lower()
    if v in NAMED:
        return NAMED[v], 1.0
    if v.startswith("#"):
        h = v[1:]
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        alpha = int(h[6:8], 16) / 255 if len(h) == 8 else 1.0
        return "#" + h[:6], round(alpha, 2)
    m = FUNC_RE.match(v)
    if not m:
        return None
    kind, args = m.group(1).lower(), re.split(r"[\s,/]+", m.group(2).strip())
    args = [x for x in args if x]
    try:
        if kind.startswith("rgb"):
            nums = []
            for x in args[:3]:
                nums.append(round(float(x[:-1]) * 2.55) if x.endswith("%") else round(float(x)))
            alpha = args[3] if len(args) > 3 else "1"
        else:
            hdeg = float(args[0].replace("deg", ""))
            s = float(args[1].rstrip("%")) / 100
            lum = float(args[2].rstrip("%")) / 100
            r, g, b = colorsys.hls_to_rgb((hdeg % 360) / 360, lum, s)
            nums = [round(r * 255), round(g * 255), round(b * 255)]
            alpha = args[3] if len(args) > 3 else "1"
        a = float(alpha[:-1]) / 100 if alpha.endswith("%") else float(alpha)
        nums = [max(0, min(255, n)) for n in nums]
        return "#%02x%02x%02x" % tuple(nums), round(a, 2)
    except (ValueError, IndexError):
        return None


def colors_in(text):
    found = [m.group(0) for m in HEX_RE.finditer(text)]
    found += [m.group(0) for m in FUNC_RE.finditer(text)]
    for word in re.findall(r"\b(white|black)\b", text.lower()):
        found.append(word)
    out = []
    for c in found:
        h = to_hex(c)
        if h:
            out.append(h)
    return out


def context_of(prop):
    p = prop.lower()
    if p == "color":
        return "text"
    if p.startswith("background"):
        return "background"
    if p.startswith("border") or p.startswith("outline"):
        return "border"
    if p in ("fill", "stroke"):
        return "icon"
    if "shadow" in p:
        return "shadow"
    return "other"


def shadow_kind(value):
    """Classify a shadow as hard offset (no blur), soft (blurred) or ring/other."""
    v = re.sub(r"(rgba?|hsla?|var)\([^)]*\)", "", value.lower())
    lengths = re.findall(r"-?[\d.]+(?:px|rem|em)?", v)
    nums = []
    for x in lengths[:3]:
        try:
            nums.append(float(re.sub(r"[a-z]+$", "", x)))
        except ValueError:
            pass
    if len(nums) >= 2 and (nums[0] or nums[1]):
        blur = nums[2] if len(nums) >= 3 else 0
        return "hard offset (no blur)" if blur == 0 else "soft (blurred)"
    return "ring or other"


# ---------- CSS ----------

def split_decls(body):
    decls = []
    for part in body.split(";"):
        if ":" in part:
            k, v = part.split(":", 1)
            decls.append((k.strip().lower(), v.strip()))
    return decls


def first_family(value):
    fam = value.split(",")[0].strip().strip("'\"")
    return fam


class CssStats:
    def __init__(self):
        self.custom = {}
        self.custom_uses = defaultdict(Counter)
        self.colors = defaultdict(lambda: {"count": 0, "contexts": Counter(), "alpha": set()})
        self.fonts = Counter()
        self.font_faces = set()
        self.sizes = Counter()
        self.radii = Counter()
        self.shadows = Counter()
        self.key = defaultdict(dict)
        self.tailwind = False

    def add_color(self, hexa, ctx, n=1):
        hx, alpha = hexa
        c = self.colors[hx]
        c["count"] += n
        c["contexts"][ctx] += n
        if alpha < 1:
            c["alpha"].add(alpha)

    def feed(self, css, inline=False):
        css = COMMENT_RE.sub("", css)
        if "--tw-" in css:
            self.tailwind = True
        for m in FONT_FACE_RE.finditer(css):
            for k, v in split_decls(m.group(1)):
                if k == "font-family":
                    self.font_faces.add(first_family(v))
        for name, value in CUSTOM_PROP_RE.findall(css):
            value = value.strip()
            if name not in self.custom:
                self.custom[name] = value
        blocks = [("[inline]", css)] if inline else RULE_RE.findall(css)
        for selector, body in blocks:
            selector = selector.strip().split("@")[-1] if "@" in selector else selector.strip()
            for prop, value in split_decls(body):
                if prop.startswith("--"):
                    continue
                ctx = context_of(prop)
                for h in colors_in(value):
                    self.add_color(h, ctx)
                for var in VAR_RE.findall(value):
                    self.custom_uses[var][ctx] += 1
                if prop == "font-family":
                    fam = first_family(value)
                    if fam and not fam.startswith("var("):
                        self.fonts[fam] += 1
                    for var in VAR_RE.findall(value):
                        self.custom_uses[var]["font"] += 1
                elif prop == "font":
                    fm = re.search(r"\d(?:px|rem|em|pt)?(?:/[\d.]+\w*)?\s+(.+)$", value)
                    if fm:
                        self.fonts[first_family(fm.group(1))] += 1
                if prop == "font-size":
                    self.sizes[value] += 1
                if prop == "border-radius":
                    self.radii[value] += 1
                if (prop in ("box-shadow", "text-shadow") and value.strip().lower() not in ("none", "0", "initial", "inherit", "unset")
                        and not value.strip().startswith("var(--tw-")):  # skip Tailwind's ring plumbing
                    self.shadows[value.strip()] += 1
                if not inline:
                    for sel in (s.strip() for s in selector.split(",")):
                        if sel in KEY_SELECTORS and prop in KEY_PROPS:
                            self.key[sel][prop] = value

    def deref(self, value, depth=0):
        """Replace var(--x, fallback) with the custom property's value, a few levels deep."""
        if depth > 6 or "var(" not in value:
            return value
        def sub(m):
            name, fallback = m.group(1), (m.group(2) or "").strip()
            return self.custom.get(name, fallback or m.group(0))
        out = re.sub(r"var\(\s*(--[\w-]+)\s*(?:,\s*([^()]*))?\)", sub, value)
        return out if out == value else self.deref(out, depth + 1)

    def resolve_custom_colors(self):
        """Count colors referenced through var(--x) so brand variables show up in the ranking."""
        for name, uses in self.custom_uses.items():
            val = self.custom.get(name, "")
            hx = to_hex(val) if val else None
            if hx:
                for ctx, n in uses.items():
                    if ctx != "font":
                        self.add_color(hx, ctx, n)


def collect_css(page_src, parser, base_dir, errors, seen):
    sheets = []
    for href in parser.stylesheets:
        if "fonts.googleapis.com" in href:
            continue
        sheets.append(resolve(href, page_src, base_dir))
    texts = []
    while sheets and len(seen) < MAX_STYLESHEETS:
        s = sheets.pop(0)
        if s in seen:
            continue
        seen.add(s)
        text, err = fetch(s, None)
        if err:
            errors.append(err)
            continue
        texts.append(text)
        for imp in IMPORT_RE.findall(text):
            if "fonts.googleapis.com" in imp:
                parser.google_fonts.append(imp)
            else:
                sheets.append(resolve(imp, s, None if is_url(s) else os.path.dirname(s)))
    return texts


def google_families(links):
    fams = set()
    for link in links:
        qs = parse_qs(urlparse(link).query)
        for fam in qs.get("family", []):
            for part in fam.split("|"):
                fams.add(part.split(":")[0].replace("+", " "))
    return sorted(fams)


# ---------- main ----------

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("source", help="A URL (https://...) or a path to a saved HTML file")
    ap.add_argument("--pages", type=int, default=3, help="How many same-site pages to read, homepage included (URLs only)")
    args = ap.parse_args()

    src = args.source
    base_dir = None if is_url(src) else os.path.dirname(os.path.abspath(src))
    errors, notes, pages_read, seen_sheets = [], [], [], set()
    stats = CssStats()
    agg = PageParser()

    queue = [norm_url(src) if is_url(src) else os.path.abspath(src)]
    visited = set()
    while queue and len(pages_read) < max(1, args.pages):
        page = queue.pop(0)
        if page in visited:
            continue
        visited.add(page)
        html, err = fetch(page, None)
        if err:
            errors.append(err)
            continue
        pages_read.append(page)
        p = PageParser()
        p.feed(html)
        for block in p.style_blocks:
            stats.feed(block)
        for inline in p.inline_styles:
            stats.feed(inline, inline=True)
        for text in collect_css(page, p, base_dir, errors, seen_sheets):
            stats.feed(text)
        # merge page findings
        agg.theme_color = agg.theme_color or p.theme_color
        agg.og_image = agg.og_image or (p.og_image and resolve(p.og_image, page, base_dir))
        agg.generator = agg.generator or p.generator
        agg.icons += [resolve(i, page, base_dir) for i in p.icons]
        agg.logos += [resolve(i, page, base_dir) for i in p.logos]
        agg.google_fonts += p.google_fonts
        agg.class_samples += p.class_samples
        agg.images += [resolve(i, page, base_dir) for i in p.images]
        agg.logo_elements += p.logo_elements
        if is_url(src):
            host = urlparse(src).netloc
            for href in p.nav_links:
                full = norm_url(urljoin(page, href))
                u = urlparse(full)
                if u.netloc == host and full not in visited and not re.search(r"\.(pdf|jpg|png|zip)$", u.path, re.I):
                    queue.append(full)

    if not pages_read:
        print(json.dumps({"source": src, "error": "Couldn't read the page.", "errors": errors,
                          "next_step": "Ask for screenshots or a brand guide PDF instead."}, indent=2))
        sys.exit(1)

    stats.resolve_custom_colors()

    # notes on things that limit the result
    gen = (agg.generator or "").lower()
    builder = next((g for g in GENERATORS if g in gen), None)
    if builder:
        notes.append(f"Built with {builder.title()}: much of the CSS is the platform's, not the brand's. Trust custom properties and the colors on headings, links and buttons over raw frequency.")
    utility_hits = sum(1 for c in agg.class_samples if re.search(r"\b(?:bg|text|px|py|mt|mb|flex|grid)-", c))
    if stats.tailwind or utility_hits > 40:
        notes.append("Looks like Tailwind or a utility-class framework: many colors are framework defaults. Lean on custom properties and the key elements.")
    if len(stats.colors) < 3:
        notes.append("Very few colors found. The page may build its styles with JavaScript; screenshots or a browser tool will show more.")
    if errors:
        notes.append(f"{len(errors)} file(s) couldn't be read; see errors.")
    if stats.font_faces and not agg.google_fonts:
        notes.append("Fonts are self-hosted (see font_face_families). Many self-hosted fonts are Google Fonts loaded from the site's own server; check fonts.google.com before treating one as paid.")
    if not agg.logos:
        notes.append("No logo image found. Check social_image and icons: the logo may be an inline SVG or a wordmark set in type.")

    custom_colors = {k: v for k, v in stats.custom.items() if to_hex(v)}
    custom_fonts = {k: stats.deref(v) for k, v in stats.custom.items()
                    if re.search(r"font|family|typeface", k, re.I) and not to_hex(v)}
    custom_other = {k: v for k, v in stats.custom.items()
                    if re.search(r"radius|space|spacing|gap|size|tracking|leading", k, re.I)}

    colors = sorted(stats.colors.items(), key=lambda kv: -kv[1]["count"])[:24]

    folders = defaultdict(set)
    for img in dict.fromkeys(agg.images):
        path = urlparse(img).path if is_url(img) else img
        folder = os.path.dirname(path)
        if folder and not folder.startswith("/_next"):
            folders[folder].add(os.path.basename(path))
    image_folders = {f: sorted(names) for f, names in sorted(folders.items(), key=lambda kv: -len(kv[1])) if len(names) >= 3}
    result = {
        "source": src,
        "method": "code (exact values)",
        "pages_read": pages_read,
        "stylesheets_read": len(seen_sheets),
        "generator": agg.generator,
        "theme_color": agg.theme_color,
        "custom_properties": {
            "colors": dict(list(custom_colors.items())[:40]),
            "fonts": dict(list(custom_fonts.items())[:15]),
            "shape_and_space": dict(list(custom_other.items())[:25]),
        },
        "colors_by_frequency": [
            {"hex": hx, "count": c["count"], "used_for": dict(c["contexts"].most_common()),
             **({"also_with_alpha": sorted(c["alpha"])} if c["alpha"] else {})}
            for hx, c in colors
        ],
        "fonts": {
            "declared_families": dict(stats.fonts.most_common(10)),
            "font_face_families": sorted(stats.font_faces),
            "google_fonts": google_families(agg.google_fonts),
        },
        "font_sizes": dict(stats.sizes.most_common(12)),
        "corner_radii": dict(stats.radii.most_common(8)),
        "shadows": [{"value": v, "count": n, "kind": shadow_kind(v)} for v, n in stats.shadows.most_common(8)],
        "key_elements": {k: {p: stats.deref(v) for p, v in props.items()} for k, props in stats.key.items() if props},
        "logo_candidates": list(dict.fromkeys(agg.logos))[:6] or list(dict.fromkeys(agg.logo_elements))[:3],
        "image_folders": dict(list(image_folders.items())[:5]),
        "icons": list(dict.fromkeys(agg.icons))[:4],
        "social_image": agg.og_image,
        "notes": notes,
        "errors": errors[:10],
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
