---
name: on-brand
description: Turns a brand into a design system Claude follows (DESIGN.md and PRODUCT.md) from a site, brand guide or screenshots, then makes on-brand social posts, emails, decks, PDFs and web pages.
---

# on-brand

Most AI-made marketing looks the same because the AI has nothing to go on. on-brand fixes that in three steps: **pull** what the brand already has, **decide** what only the person can decide, then **make** things that follow it: social posts and banners, email headers, slides, PDFs and flyers, web pages, and anything else visual.

The person using this is usually not a designer and often not technical. Write to them in plain words, one question at a time, and never make them read a file to answer a question.

## What it produces

A folder called `<brand>-design/` holding two files that matter most:

- `DESIGN.md`: how the brand looks. Colors, type, spacing, shapes, and what it never does. Written in the open DESIGN.md format from Google Labs, so it also works in Claude Design, impeccable, Stitch and other tools.
- `PRODUCT.md`: who it's for, the point of view, why each choice was made, and the copy rules. Named so impeccable can read it too.

Plus format rules for the pieces they make most, a small SKILL.md so Claude loads the system automatically, and a test piece showing the difference. The files belong to the person. They work even without this skill: attaching them to any chat does most of the job.

## Pick the mode

Read the request and pick one. If it's unclear and no system exists yet, start with `start`.

| The person wants to | Mode | Read |
| --- | --- | --- |
| Set up their brand from scratch or from a site | `start` | `reference/pull.md`, `reference/decide.md`, `reference/write.md`, then `reference/make.md` for the test piece |
| Only extract a system from a site, guide or screenshots | `pull` | `reference/pull.md` |
| Make a social post, email, deck, PDF, flyer or web page with an existing system | `make` | `reference/make.md` and the matching file in `formats/` (social, email, slides, documents, web) |
| Check whether a piece fits the system | `check` | `reference/check.md` |
| Change a decision or add a new rule | `update` | `reference/update.md` |

If the person attaches a DESIGN.md or PRODUCT.md (or the folder), the system exists: go straight to `make`, `check` or `update`.

## Where this is running

Work out the environment once and pick methods to match. Don't ask the person what environment they're in.

- **Claude Code or another agent with a shell and network:** you can run `scripts/extract_site.py` on a URL, save files to disk, and render HTML to PNG or PDF.
- **claude.ai:** you can run scripts in a sandbox that usually can't reach outside websites, and you can read attached PDFs and images. Ask for screenshots or a brand PDF instead of fetching the site, and deliver files as downloads (a zip for the folder).
- **No code tools at all:** run the interview in chat and write DESIGN.md and PRODUCT.md as text blocks the person copies and saves.

## Specs change

Platform sizes and safe zones change. The social format file carries the date its specs were last checked and the steps to refresh them. Follow them before making social pieces, banners or platform headers.

## Rules that apply in every mode

- **Never invent brand facts.** If something is unknown, ask, or leave it out and say so. Every extracted value carries how sure you are: exact, read from page, or estimated.
- **Confirm before writing.** Show a one-screen summary of decisions and wait for a yes or changes.
- **Check contrast** on every text and background pair with `scripts/contrast.py` when you can run code (4.5:1 for body text, 3:1 for large headlines). Flag failures and suggest the nearest passing shade from their palette. Without code, estimate and say it's an estimate.
- **Only use fonts they're allowed to use:** Google Fonts, or files they own. Say which is which. If their site uses a paid font they haven't licensed for other uses, suggest the closest Google Font and label it as a stand-in.
- **Whose brand is it?** Their own or a client's with permission is fine. For anyone else's site, treat it as reference: describe the feel and write an original system. Never copy another brand's logo, artwork, or exact palette and type pairing.
- **Don't let AI defaults creep in.** No emoji in headings, no gradient blobs, no rounded cards everywhere just because, no stock phrases ("unlock", "elevate", "seamless"), no new colors outside the system.
- **Keep it short.** DESIGN.md under about 250 lines, PRODUCT.md under about 120. A non-designer should be able to read both in ten minutes.

## Voice

This skill covers copy rules tied to layout: how many words go on an image, what goes in a caption, case, punctuation and banned words. It is not a full voice guide. If the person has a voice or writing-style skill, follow it for longer copy and say so. If they want one, suggest building it separately.
