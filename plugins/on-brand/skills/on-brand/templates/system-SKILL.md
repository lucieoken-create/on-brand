---
name: {{brand-slug}}-design
description: Use for anything visual made for {{Brand}}: social posts, flyers, slides, documents and web pages. Holds the brand's colors, type, layout rules, copy rules and what it never does, and keeps them current as feedback comes in.
---

# {{Brand}} design system

This is {{Brand}}'s own design system. It works on its own: making pieces, checking them and updating the rules all happen here, in any tool that reads skills or `AGENTS.md`.

## Before making anything

Read these files in this order:

1. `DESIGN.md` for how it looks: colors and their jobs, type, layout, shapes, and the Do's and Don'ts.
2. `PRODUCT.md` for who it's for, why it looks this way, and the copy rules.
3. The file in `formats/` that matches what you're making. For social posts, banners and event covers, check the "Specs last checked" date in `formats/social.md` first and refresh the specs if they're stale. For anything without a format file, work from DESIGN.md and PRODUCT.md and look up the current size for that platform.
4. `reference/principles.md`, the checks every piece goes through before it's shown.

Use `tokens.css` for exact values in HTML. Use only the fonts and colors defined there. Logo and image files are in `assets/`.

Never invent facts (prices, dates, addresses) for a piece. Ask.

## Before showing a piece

Render it if you can and look at it at full size and at the size it'll be seen. Check it against DESIGN.md's Do's and Don'ts and `reference/principles.md`: one thing leads, alignment (shared edges, even gaps, nothing nearly lined up), the fixed type sizes and weights, whole-pixel values. The brand's own rules win where they disagree with a principle.

After showing it, ask what's off. If they have a piece that already gets it right, ask to see it.

## Editable pieces

Edit mode: ask

(`ask`, `always` or `never`. This decides whether a finished piece also comes back as an editable page where the words and brand colors can be changed and the result downloaded. With `ask`, offer once after showing a piece. Build it from `templates/edit-post.html` following `reference/editing.md`.)

## Keeping this system current

Feedback goes into these files, so it holds next time. When a new decision comes up ("never put text over the photo", "the web address is always in capitals"):

1. **Find where it belongs.** A look decision (color, type, shape, layout) goes in DESIGN.md, and in tokens.css if it changes a value. A why, audience or copy decision goes in PRODUCT.md. A rule for one kind of piece goes in that file in `formats/`. A "never" goes in Do's and Don'ts.
2. **Confirm the wording** with the person in one line before changing anything.
3. **Change the source first,** then anything that depends on it: a new color changes DESIGN.md's tokens and prose, tokens.css, and any format file that names colors.
4. **Re-check contrast** if a color changed: `python3 scripts/contrast.py --text <text colors> --bg <background colors>`.
5. **Log it** with a dated line under "Changes" at the end of DESIGN.md.
6. **Visual rules get rendered before they're written.** Make the thing, look at it, then write the rule.
7. **Platform specs:** when a size changes, update the table in `formats/social.md` and its "Specs last checked" date.
8. **A new kind of piece** they'll make again (a podcast cover, a business card) gets its own file in `formats/`.

If this folder is uploaded to claude.ai as a skill, remind them to upload the updated folder again after changes, since uploaded skills don't update themselves.
