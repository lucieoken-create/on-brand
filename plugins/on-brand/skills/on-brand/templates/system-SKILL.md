---
name: {{brand-slug}}-design
description: Use for anything visual made for {{Brand}}: {{the pieces they make, e.g. social posts, emails, flyers and slides}}{{, and returns single pieces as editable pages for light edits (words, photo, colors), if edit mode is on}}. Holds the brand's colors, type, layout rules, copy rules and what it never does, and keeps them current as feedback comes in.
---

# {{Brand}} design system

This is {{Brand}}'s own design system. It works on its own: making pieces, checking them and updating the rules all happen here, in any tool that reads skills or `AGENTS.md`.

It covers how {{Brand}} looks, plus the copy rules that affect graphics. {{If they have a voice doc: For longer copy (captions, email bodies), follow `reference/voice.md`.}}

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

## How pieces are delivered

Delivery: {{in their words, e.g. images for posts, PowerPoint for decks, or "whatever fits"}}

Hand every piece over the way this line says, unless the request asks for something else:

- **Image or PDF:** render it at the size in the format file and check it before showing.
- **PowerPoint or Word:** build the file with the tool's built-in PowerPoint or Word skill where there is one (claude.ai has them), or `python-pptx` / `python-docx` with a shell. Use the exact colors from `tokens.css` and the fonts from DESIGN.md, and follow the matching format file. Render or open it once to check before handing it over.
- **To finish in Canva or Adobe:** hand over a PDF or PowerPoint. Tell them once that Canva and Adobe Express open both as editable designs when uploaded. Their brand colors, fonts and logos for those tools are in `kit/`.

## Editable pieces

Edit mode: ask

(`ask`, `always` or `never`. This decides whether a finished piece also comes back as an editable page where the words and brand colors can be changed and the result downloaded. With `ask`, offer once after showing a piece. Build it from `templates/edit-post.html` following `reference/editing.md`. {{If the template was filled in during setup: It's already filled in with this brand's color pairings, fonts, marks and word limits; change the words in START, and render() only if the layout differs.}})

**The first time you build an editable page for someone,** explain it in a few plain lines. In claude.ai it's an artifact: a small web page in their Claude account that opens next to the chat. It works as a mini studio for this one piece: they can change the words, swap the photo, pick a color pairing or switch sizes, then download. Every option is on-brand. Nothing saves automatically, so they should download what they want to keep. Publish it with the `downloads` capability so the download button works. If the page doesn't appear, they need "Code execution and file creation" turned on in Settings > Capabilities (on Team and Enterprise, an owner turns it on in Organization settings).

**Where artifacts aren't available** (another AI tool, or the setting is off), hand over the editor as an .html file. Opened in any browser, it works fully, download included.

## Keeping this system current

Feedback goes into these files, so it holds next time. When a new decision comes up ("never put text over the photo", "the web address is always in capitals"):

Start by saying what's set now, in plain words ("Right now headlines are in the serif, in navy. What's changing?"), so someone changing one thing doesn't re-answer the rest. Then:

1. **Find where it belongs.** A look decision (color, type, shape, layout) goes in DESIGN.md, and in tokens.css if it changes a value. A why, audience or copy decision goes in PRODUCT.md. A rule for one kind of piece goes in that file in `formats/`. A "never" goes in Do's and Don'ts.
2. **Confirm the wording** with the person in one line before changing anything.
3. **Change the source first,** then anything that depends on it: a new color changes DESIGN.md's tokens and prose, tokens.css, and any format file that names colors.
4. **Re-check contrast** if a color changed: `python3 scripts/contrast.py --text <text colors> --bg <background colors>`.
5. **Log it** with a dated line under "Changes" at the end of DESIGN.md.
6. **Visual rules get rendered before they're written.** Make the thing, look at it, then write the rule.
7. **Platform specs:** when a size changes, update the table in `formats/social.md` and its "Specs last checked" date.
8. **A new kind of piece** they'll make again (a podcast cover, a business card) gets its own file in `formats/`.
9. **Changes apply from now on.** Never say pieces made before the change were updated. Offer to redo one if they want it.
10. **Keep the examples, the editor and the kit in step.** If a change affects what `examples/` shows (a new default mark, a new color), redo the example and its PNG, so it never shows an old rule. If it affects the editor (a pairing, a word limit, a mark), change `templates/edit-post.html` too. If a color, font or logo changes, update `kit/` (re-run `python3 scripts/make_ase.py kit/brand-colors.ase --design DESIGN.md` and the sheet) and tell them to update their Canva or Adobe brand kit.

In claude.ai, if Claude offers to save the changes to the skill (a card in the chat), accept it. If it doesn't, download the updated folder as a zip and upload it again to replace the old version.
