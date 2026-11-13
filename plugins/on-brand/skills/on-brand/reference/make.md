# Make: marketing pieces from the system

## Before you start

Read DESIGN.md, PRODUCT.md, `reference/principles.md` and the matching file in `formats/` (social, email, slides, documents or web). If the person hasn't got a system yet, offer `start` first. If they only want something quick, make it and say it would look more like them with a system.

**Something with no format file** (a business card, a Substack header, a podcast cover, a sticker): make it from DESIGN.md and PRODUCT.md, and look up the current size and safe zones for that platform or medium if you can search the web. If they'll make it again, offer to add a format file for it with `update`.

Ask only what you need: what the piece is for, the words or facts it must include (date, price, link), and where it's going. Never invent facts like prices, dates or addresses. Leave a clearly marked gap and ask.

## Building it

1. **Check the specs first** for social posts, banners, event covers and platform headers: follow "Keep the specs current" in the brand's `formats/social.md` (or the email file for platform headers). Stale or missing specs get looked up before you build, not after.
2. Start from the template in `templates/` that matches (`social-post.html` for social, `flyer.html` for documents). For email, slides and web, build from the rules in the format file.
3. Link the tokens: paste the contents of `tokens.css` into the page's `<style>`, and load the fonts named in DESIGN.md (Google Fonts link, or their own files from `assets/`).
4. Write the copy to the copy rules in PRODUCT.md and the word limits in the format file. Headline first. If the copy doesn't fit the limits, cut words; don't shrink the type.
5. Use only colors from the tokens. Respect the shares in DESIGN.md (an accent used everywhere stops being an accent).
6. Check the piece against Do's and Don'ts and against `reference/principles.md` before showing it. Alignment, type hierarchy and pixel precision are the ones to look at hardest: render the piece if you can, trace the edges, and check it again at phone size.

## Illustrations, patterns and art files

Raster art (ASCII art, line drawings, scanned textures) behaves differently from type and color blocks:

- **Show it big enough to read at the size it'll be seen.** Fine detail shrunk down turns into grey texture. If it doesn't fit, give it more room rather than shrinking or cropping it.
- **Watch thin strokes on color.** Light or semi-transparent strokes mix with the color behind them; on a color close to the art's opposite they turn muddy grey. Put light art on a neutral or matching background, or redraw it in an exact brand color: in HTML, use the image as a CSS mask over a solid fill (`background: var(--color-primary); mask: url(art.png) center / contain no-repeat`).
- **Align by the drawing, not the file.** Image files often have empty margins. Line up what you can see.
- **Sit inside or run off on purpose.** Art sits fully inside its space by default. Running it off an edge is a choice, and it never stops awkwardly mid-canvas.

## Render before you write a rule

When a new visual rule comes up (a treatment, a size, a way to place art), make it and look at it before writing it into the system. Rules written from a guess ("use the file as it is") often look different once rendered.

## The test piece (end of `start`)

Make the same piece twice so the difference is visible:

- **before.html:** what Claude makes from a plain request with no system, for example "Make an Instagram post for our Small Business Saturday sale on Nov 29, 20% off everything." Build it honestly, the way a generic request would come out. Don't make it deliberately bad.
- **after.html:** the same request, made with the system.

Show both side by side and name two or three specific differences ("the accent only appears on the date, the headline is six words, no emoji"). Save both to `examples/` in their folder.

## Output

- **Claude Code or Codex:** save the HTML. Render a PNG (social, email header) or PDF (documents) at the exact size in the format file, and look at it before showing it. Playwright works if it's installed:

  ```bash
  npx playwright screenshot --viewport-size=1080,1350 file://$PWD/after.html after.png
  ```

  Without Playwright, use a Chrome or Chromium that's already on the machine, in headless mode (no install needed):

  ```bash
  # Mac: "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"   Linux: chromium or google-chrome   Windows: chrome.exe
  CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
  "$CHROME" --headless=new --hide-scrollbars --force-device-scale-factor=1 --allow-file-access-from-files \
    --window-size=1080,1350 --virtual-time-budget=8000 --screenshot="$PWD/after.png" "file://$PWD/after.html"
  ```

  `--virtual-time-budget` gives web fonts time to load; `--allow-file-access-from-files` lets local images load when they're used as CSS masks. For a PDF, use `--print-to-pdf=after.pdf` instead of `--screenshot`. If nothing can render, say so and give them the HTML to open.
- **claude.ai:** show the HTML so they can see it, and offer it as a file. Tell them they can screenshot it or open it in a browser and print to PDF.

## Edit mode

Check the `Edit mode:` line in the brand's SKILL.md and follow `reference/editing.md`:

- `ask` (or no line): after showing the piece, offer once: "Want this as an editable page so you can tweak the words and colors yourself?"
- `always`: build the editable page as the output, from `templates/edit-post.html`.
- `never`: skip it.

Edit mode is for single pieces with a few slots (social posts, banners, covers, email headers, flyers). In claude.ai, publish the page as an artifact when you can, so it opens beside the chat; otherwise hand over the HTML file to open in a browser. It needs no saving, so it works on every plan.

## After they see it

Ask what's off, in their words. If the answer is a new rule ("never put text over the photo"), offer to add it with `update` so it sticks.

Also ask: "Do you have a piece that gets this right?" The most useful examples often come up here, once the person can see what's missing, rather than at the start. Read anything they share the same way as in `reference/pull.md` (step 3), then update the system.

At the end of `start`, this round is part of setup: pull, interview, write, the test piece, then one round of "what's off?" and `update`. That round is where the rules that matter most usually show up.

## The handover

After that round, setup is done. Say so, and hand the system over as its own skill:

1. **Install it** where they work, after checking the name is still free:
   - **Claude Code:** copy the folder to `~/.claude/skills/<folder name>/` (all their projects) or the project's `.claude/skills/` (this project only). Ask which.
   - **Codex:** copy it to their Codex skills folder, or keep it in the repo; the `AGENTS.md` inside points Codex at the files.
   - **claude.ai:** zip the folder (the folder name must match the `name` in its SKILL.md) and walk them through uploading it: Customize > Skills > + > Create skill > Upload a skill.
   - **No code tools:** they already have DESIGN.md and PRODUCT.md as text; tell them to keep both together and attach them when making things.
2. **Tell them, in a few lines,** what changes now:
   > Your brand system is set up and installed as its own skill, `<name>`. From here, you don't need on-brand: ask for what you want ("Make a LinkedIn post for our workshop on Dec 6") and your skill handles it. When something looks off, say so, and it writes the fix into your files so it holds next time. The files are yours, and they work in Claude, Codex and other tools that read them. Come back to on-brand to set up another brand or a client, or for a bigger rework.
3. **Suggest keeping a copy** somewhere they control (a Drive folder, a Git repo) as the source of truth, since an installed skill is a copy.
