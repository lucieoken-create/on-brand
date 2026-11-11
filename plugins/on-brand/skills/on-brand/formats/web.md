# Web pages

Starter rules for a landing page, a single page, or a small site section. Fill in the brand-specific lines when writing a system. These are for pages built as HTML and CSS, by Claude or in Claude Code. If the person uses a site builder (Squarespace, Wix, Shopify, Webflow), use the same rules to set that builder's colors, fonts and spacing instead of writing code.

## Build on the tokens

- Link or paste `tokens.css` and use its variables for every color, font, size and space. No raw hex codes or one-off sizes in the page.
- Load fonts from Google Fonts or the person's own files, with fallbacks named in the tokens.

## Layout

- Design for phones first, then widen. Check at about 390px (phone), 768px (tablet) and 1280px (laptop).
- Body text at 16 to 18px with a line length of about 60 to 75 characters. Headlines can scale with the screen; body text shouldn't shrink on phones.
- Spacing from the scale in DESIGN.md only.
- {{Their layout habits: left-aligned or centered, roomy or dense, how sections are separated.}}

## A landing page, top to bottom

1. A headline that says what it is and who it's for, a short supporting line, and one main button.
2. What they get or why it matters: three to five points, not more.
3. Proof: a quote, a logo row, an example or a number, if the person has real ones. Never invent any.
4. Details: when, where, how much, how it works.
5. The same main button again, then a small footer with contact and links.

One main action per page. Secondary actions are text links, not more buttons.

## Words

- Button text says what happens: "Save my spot", "Book a call". Never "Click here" or "Submit".
- {{Their copy rules from PRODUCT.md: case, banned words, how the business name is written.}}

## Accessible by default

- Text and background pairs that pass contrast in DESIGN.md (4.5:1 for body text).
- Real headings in order (one h1, then h2s), alt text on images that carry meaning, visible focus outlines on links and buttons, and buttons as real `<button>` or `<a>` elements.
- Motion only if DESIGN.md allows it, and none for people who've turned motion off (`prefers-reduced-motion`).

## Before handing over

Open the page at phone and laptop widths and look at it. Check every link works, nothing overflows sideways on a phone, and the page has a real `<title>` and a short description for when it's shared.
