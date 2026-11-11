---
name: {{brand-slug}}-design
description: Use for anything visual made for {{Brand}}: social posts, flyers, slides, documents and web pages. Holds the brand's colors, type, layout rules, copy rules and what it never does.
---

# {{Brand}} design system

Before making anything visual for {{Brand}}, read these files in this order:

1. `DESIGN.md` for how it looks: colors and their jobs, type, layout, shapes, and the Do's and Don'ts.
2. `PRODUCT.md` for who it's for, why it looks this way, and the copy rules.
3. The file in `formats/` that matches what you're making. For social posts, banners and event covers, check the "Specs last checked" date in `formats/social.md` first and refresh the specs if they're stale. For anything without a format file, work from DESIGN.md and PRODUCT.md and look up the current size for that platform.

Use `tokens.css` for exact values in HTML. Use only the fonts and colors defined there. Logo and image files are in `assets/`.

Never invent facts (prices, dates, addresses) for a piece. Ask.

If a new decision comes up while working ("never put text over the photo"), suggest adding it to the right file so it sticks.
