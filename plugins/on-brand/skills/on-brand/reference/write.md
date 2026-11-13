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
  templates/
    edit-post.html  copied from this skill: the editable-piece starter
  scripts/
    contrast.py     copied from this skill: the contrast checker
  assets/           logo and image files they provided
  examples/         the test piece from make: before.html, after.html (and PNGs if rendered)
```

**The folder has to work without on-brand.** After setup, the brand's own skill is what people use to make things and to update the rules, in Claude, Codex or anything else that reads skills or `AGENTS.md`. That's why the principles, the editing rules, the contrast script and the update steps (in its SKILL.md) travel with it. Copy those files as they are; their paths match this skill's, so links inside them still work.

## Filling in the templates

- **DESIGN.md** follows the Google Labs DESIGN.md format: YAML tokens at the top, then the sections in this order: Overview, Colors, Typography, Layout, Elevation & Depth, Shapes, Components, Do's and Don'ts. Leave out sections that don't apply and list them under `omitted` in the front matter with a reason. Name colors by their job (`primary`, `secondary`, `tertiary`, `neutral`, plus plain names like `surface` or `accent` if needed) and describe each one's use in the prose. The person's refusals go in Do's and Don'ts, in their own words where possible, plus the AI-default list from the template.
- **PRODUCT.md** is strategy only: no hex codes, no font names. Who it's for, the feeling, the point of view, the reasoning rules, the voice line and the copy rules.
- **Exceptions by output** from question 8 go in the matching format file, not in DESIGN.md: "photos are fine in slides", "chartreuse fills whole slides". DESIGN.md holds the rules that are true everywhere.
- **Formats they want later:** don't write a file yet. List them under "Where it shows up" in PRODUCT.md marked "(later)", and mention them in SKILL.md so the system knows to work from DESIGN.md and PRODUCT.md for those.
- **formats/** files: copy the starter rules for each chosen format (social, email, slides, documents, web) and fill in the brand-specific parts (which colors go where, headline size in their font, word limits from their copy answers). Delete starter lines that conflict with their decisions. Keep the "Keep the specs current" section and the "Specs last checked" date in social.md; if you checked specs during setup, set the date to today.
- **tokens.css**: one variable per token, same names as DESIGN.md.
- **SKILL.md**: set `name` to the folder name (`<brand-slug>-design`, or the alternative if that was taken) and fill in the brand name. Keep the "Keeping this system current" section as it is.
- Mark any value still **estimated** with a short comment so they can fix it later.

## Checks before handing over

1. Run `python3 scripts/contrast.py` on every text and background pair in the tokens. Fix or flag failures.
2. If a shell with Node is available, run `npx @google/design.md lint DESIGN.md` and fix errors. If Node isn't there, skip it silently. If the command is blocked (no network, or a permission setting stops the install), say so once in the handover and move on.
3. Search the files for anything left from the templates (double curly braces) and for hex codes that aren't in the tokens.
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
