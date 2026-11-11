# Write: the system folder

Write only after the person approves the summary from `decide`.

## The folder

Name it `<brand-slug>-design/`, for example `low-tide-goods-design/`.

```
<brand>-design/
  SKILL.md          from templates/system-SKILL.md: tells Claude to read the system before making anything
  DESIGN.md         from templates/DESIGN.md: how the brand looks
  PRODUCT.md        from templates/PRODUCT.md: who it's for, why, copy rules
  formats/          only the formats they chose, copied from this skill's formats/ and filled in
  tokens.css        from templates/tokens.css: the same tokens as CSS variables
  AGENTS.md         from templates/AGENTS.md: points Codex and other tools at the files
  assets/           logo and image files they provided
  examples/         the test piece from make: before.html, after.html (and PNGs if rendered)
```

## Filling in the templates

- **DESIGN.md** follows the Google Labs DESIGN.md format: YAML tokens at the top, then the sections in this order: Overview, Colors, Typography, Layout, Elevation & Depth, Shapes, Components, Do's and Don'ts. Leave out sections that don't apply and list them under `omitted` in the front matter with a reason. Name colors by their job (`primary`, `secondary`, `tertiary`, `neutral`, plus plain names like `surface` or `accent` if needed) and describe each one's use in the prose. The person's refusals go in Do's and Don'ts, in their own words where possible, plus the AI-default list from the template.
- **PRODUCT.md** is strategy only: no hex codes, no font names. Who it's for, the feeling, the point of view, the reasoning rules, the voice line and the copy rules.
- **formats/** files: copy the starter rules for each chosen format (social, email, slides, documents, web) and fill in the brand-specific parts (which colors go where, headline size in their font, word limits from their copy answers). Delete starter lines that conflict with their decisions. Keep the "Keep the specs current" section and the "Specs last checked" date in social.md; if you checked specs during setup, set the date to today.
- **tokens.css**: one variable per token, same names as DESIGN.md.
- **SKILL.md**: set `name` to `<brand-slug>-design` and the description to "Use for anything visual made for <Brand>: social posts, flyers, slides, documents and web pages."
- Mark any value still **estimated** with a short comment so they can fix it later.

## Checks before handing over

1. Run `python3 scripts/contrast.py` on every text and background pair in the tokens. Fix or flag failures.
2. If a shell with Node is available, run `npx @google/design.md lint DESIGN.md` and fix errors. If it isn't, skip it silently.
3. Search the files for anything left from the templates (double curly braces) and for hex codes that aren't in the tokens.
4. Read DESIGN.md and PRODUCT.md once as the person would. Cut anything a non-designer wouldn't understand.

## Delivering

- **Claude Code:** write the folder where the person asked, or next to their project. Offer to install it as a personal skill by copying it to `~/.claude/skills/<brand>-design/`.
- **claude.ai:** create the files, zip the folder (the folder name must match the `name` in its SKILL.md), and give them the zip. Tell them how to use it, in this order of ease:
  1. Upload the zip as a skill: Customize > Skills > + > Create skill > Upload a skill. Then Claude uses it automatically.
  2. Or add DESIGN.md and PRODUCT.md to a Claude Project's files, and do brand work inside that Project.
  3. Or attach the two files to any chat when making something.
- **No code tools:** print DESIGN.md and PRODUCT.md as two separate text blocks and tell them to save each as a file with that exact name.

Then go to `reference/make.md` and make the test piece.
