# Write: the system folder

Write only after the person approves the summary from `decide`.

## The folder

Name it `<brand-slug>-design/`, for example `low-tide-goods-design/`. Before writing, check that the name isn't taken: look for an existing folder or skill with the same name (in Claude Code, `~/.claude/skills/` and the project's `.claude/skills/`; in Codex, its skills folder; in claude.ai, ask whether they already have a skill for this brand). If it is, suggest another name, like `<brand-slug>-brand-system`, and say why. Two skills with one name means the wrong one loads.

```
<brand>-design/
  SKILL.md          from templates/system-SKILL.md: how to make, check and update with this system
  DESIGN.md         from templates/DESIGN.md: how the brand looks
  PRODUCT.md        from templates/PRODUCT.md: who it's for, why, copy rules
  formats/          only the formats they chose, copied from this skill's formats/ and filled in
  tokens.css        from templates/tokens.css: the same tokens as CSS variables
  AGENTS.md         from templates/AGENTS.md: points Codex and other tools at the files
  reference/
    principles.md   copied from this skill: the checks every piece goes through
    editing.md      copied from this skill: rules for editable pieces
    voice.md        only if they have a voice or brand context doc: a copy of it
  templates/
    edit-post.html  from this skill's starter, filled in for this brand if they'll edit pieces (see below)
  scripts/
    contrast.py     copied from this skill: the contrast checker
    make_ase.py     copied from this skill: writes the Adobe swatch file
  kit/              for people and other tools (see below)
    brand-guide.html  from templates/brand-guide.html: the one-page visual guide (and brand-guide.pdf if rendered)
    brand-kit.md    from templates/brand-kit.md: colors, fonts, logos and setup steps
    brand-colors.ase  from scripts/make_ase.py: the palette as an Adobe swatch file
  assets/           logo and image files they provided, and any versions you made from them
    fonts/          the font files and their licenses, when you can get them (see below)
  examples/         the test piece from make: before.html, after.html (and PNGs if rendered)
```

**The folder has to work without on-brand.** After setup, the brand's own skill is what people use to make things and to update the rules, in Claude, Codex or anything else that reads skills or `AGENTS.md`. That's why the principles, the editing rules, the contrast script and the update steps (in its SKILL.md) travel with it. Copy those files as they are; their paths match this skill's, so links inside them still work.

**Nothing in it points outside it.** The skill gets used in other projects, other chats and other tools, where a doc in one Claude Project or a file on one computer isn't there. If they have a voice doc or brand context doc, copy what lasts into the folder: the copy rules into PRODUCT.md, and the whole doc as `reference/voice.md` if they want it to travel (then fill in the voice line in SKILL.md). Things that change week to week (dates, offers, events) stay out; the skill asks for them when making a piece.

**Each file lives in one place.** Don't copy the editor into `examples/` as well as `templates/`; with fonts and images embedded it can weigh close to a megabyte. Keep it in `templates/` only.

### Assets you make

If you make versions they didn't send (a white logo from a colored one, a mark cut out of the logo, a divider), render each one on every background it'll sit on and look at it before saving. Cut-outs leave stray bits behind, and thin strokes vanish on some backgrounds. Name the files by color (`logo-white.png`), note in `assets/` which are originals and which you made, and save an SVG as well when the shape is simple enough to trace.

### Fonts

Put the brand's font files in `assets/fonts/` with their licenses, so pieces render the same anywhere, including offline and in the editor. Google Fonts are free to ship this way. If Google Fonts is blocked (common in sandboxes), the same fonts come from npm: `npm install @fontsource/<font-name>` gives `.woff2` files and the license under `node_modules/@fontsource/<font-name>/`. Copy only the weights the system uses. Paid fonts never go in the folder unless the person says their license allows it.

### The visual guide

Everyone gets `kit/brand-guide.html`, filled in from `templates/brand-guide.html`: the brand on one page, for the person to look at and to send to a designer, a printer or someone new. DESIGN.md is for tools; this is for people. It shows:

- the name and logo (or stand-in wordmark, labeled) and who it's for
- each color with its name, hex, job and share, and the passing text pairs set in those colors
- the fonts set on real words from the practice piece, as headline, subhead, body and label, with family, weight, source and license
- corners, shadows and room
- each logo file on the background it goes on
- the test piece and the second format, as images
- the never-list, and anything still open

Write it after the test piece, so "In use" has real pieces in it, and update it after the round of feedback. Embed the fonts and images so it works as a single file. Render it and look at it like any other piece. Where you can, also save it as `kit/brand-guide.pdf` (see Output in `reference/make.md`). If they're stopping with a guide instead of a skill (see "A guide can be the finish" in `reference/decide.md`), this is their main deliverable.

### The kit for other tools

Everyone gets the rest of `kit/` too, so the brand travels to the tools they already use:

- **`kit/brand-kit.md`** from `templates/brand-kit.md`: each color with its hex, RGB and job, the passing text pairs, the fonts and where to get them, the logo files and which background each goes on, and steps for Canva and Adobe. Keep the plan limits in it: Canva's free Brand Kit holds only a few colors, and Adobe Express brand kits need Premium. Cut the Canva or Adobe section only if they said they never use that tool.
- **`kit/brand-colors.ase`**: run `python3 scripts/make_ase.py kit/brand-colors.ase --design DESIGN.md`. Illustrator, Photoshop and InDesign load it from the Swatches panel. Name colors in DESIGN.md's comments the way the person names them (`# Navy: all text`), so the swatches carry their names.

### The editor, filled in for the brand

If they'll use editable pieces (`Edit mode: always` or `ask`), fill in `templates/edit-post.html` for their brand now, during setup, following `reference/editing.md`: their color pairings, fonts embedded, their mark and tag if they have them, word limits and refusals, and a layout for each shape. Then making an editable piece later only means changing the words. Mention editable pieces in the skill's `description` so it's clear the skill offers them. With `never`, copy the starter as it is, so it's there if they change their mind.

## Filling in the templates

- **DESIGN.md** follows the Google Labs DESIGN.md format: YAML tokens at the top, then the sections in this order: Overview, Colors, Typography, Layout, Elevation & Depth, Shapes, Components, Do's and Don'ts. Leave out sections that don't apply and list them under `omitted` in the front matter with a reason. Name colors by their job (`primary`, `secondary`, `tertiary`, `neutral`, plus plain names like `surface` or `accent` if needed) and describe each one's use in the prose. The person's refusals go in Do's and Don'ts, in their own words where possible, plus the AI-default list from the template.
- **PRODUCT.md** is strategy only: no hex codes, no font names. Who it's for, the feeling, the point of view, the reasoning rules, the voice line and the copy rules.
- **Exceptions by output** from question 8 go in the matching format file, not in DESIGN.md: "photos are fine in slides", "chartreuse fills whole slides". DESIGN.md holds the rules that are true everywhere.
- **Formats they want later:** don't write a file yet, even if one came up in the interview. List them under "Where it shows up" in PRODUCT.md marked "(later)", and mention them in SKILL.md so the system knows to work from DESIGN.md and PRODUCT.md for those. The brand skill's own rule adds a format file the first time they make one again.
- **Print:** if they'll print, add a color table to the documents file with hex, RGB and CMYK for each color. Mark CMYK as a starting point to confirm with the printer, since it comes from a formula, not their printer, and add a line about asking for a Pantone match for anything printed in volume.
- **Text in template slots:** the starter templates put small text (labels, footers, the highlighted fact) in a color slot. Before using one, check each slot's color against the passing pairs in DESIGN.md. If a palette's secondary or accent fails as small text, use the text color there, or put the fact in a block of the accent with readable text on it.
- **formats/** files: copy the starter rules for each chosen format (social, email, slides, documents, web) and fill in the brand-specific parts (which colors go where, headline size in their font, word limits from their copy answers). Delete starter lines that conflict with their decisions. Keep the "Keep the specs current" section and the "Specs last checked" date in social.md; if you checked specs during setup, set the date to today.
- **tokens.css**: one variable per token, same names as DESIGN.md.
- **SKILL.md**: set `name` to the folder name (`<brand-slug>-design`, or the alternative if that was taken), fill in the brand name, list the kinds of pieces they make in the `description`, and set `Delivery:` and `Edit mode:` from their answer. Keep the "Keeping this system current" section as it is.
- Mark any value still **estimated** with a short comment so they can fix it later.

## Checks before handing over

1. Run `python3 scripts/contrast.py` on every text and background pair in the tokens. Fix or flag failures.
2. If a shell with Node is available, run `npx @google/design.md lint DESIGN.md` and fix errors. If Node isn't there, skip it silently. If the command is blocked (no network, or a permission setting stops the install), say so once in the handover and move on. A warning about the `omitted` list is expected: the linter currently flags any section listed there. Keep the list, since it tells other tools a section was left out on purpose.
3. Search the files for anything left from the templates (double curly braces), for hex codes that aren't in the tokens, and for anything that points outside the folder (a Claude Project doc, a path on their computer). Every stand-in (a borrowed photo, a placeholder wordmark) is labeled as one.
4. Read DESIGN.md and PRODUCT.md once as the person would. Cut anything a non-designer wouldn't understand.

## Delivering

Write the folder now, so the test piece can use it. Installing it as a skill is part of the handover at the end of setup (see "The handover" in `reference/make.md`).

- **Claude Code:** write the folder where the person asked, or next to their project.
- **Codex:** write the folder in the repo they're working in, or where they asked.
- **claude.ai:** create the files, zip the folder (the folder name must match the `name` in its SKILL.md), and give them the zip. Tell them how to use it, in this order of ease:
  1. Upload the zip as a skill: Customize > Skills > + > Create skill > Upload a skill. Then Claude uses it automatically.
  2. Or add DESIGN.md and PRODUCT.md to a Claude Project's files, and do brand work inside that Project.
  3. Or attach the two files to any chat when making something.
- **No code tools:** print DESIGN.md and PRODUCT.md as two separate text blocks and tell them to save each as a file with that exact name.

Then go to `reference/make.md` and make the test piece. Setup isn't finished at the test piece: it ends after one round of feedback (see "After they see it" in make.md).
