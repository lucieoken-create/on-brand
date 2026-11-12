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
6. Check the piece against Do's and Don'ts and against `reference/principles.md` before showing it. Alignment is the one to look at hardest: render the piece if you can and trace the edges.

## The test piece (end of `start`)

Make the same piece twice so the difference is visible:

- **before.html:** what Claude makes from a plain request with no system, for example "Make an Instagram post for our Small Business Saturday sale on Nov 29, 20% off everything." Build it honestly, the way a generic request would come out. Don't make it deliberately bad.
- **after.html:** the same request, made with the system.

Show both side by side and name two or three specific differences ("the accent only appears on the date, the headline is six words, no emoji"). Save both to `examples/` in their folder.

## Output

- **Claude Code:** save the HTML. If Playwright or headless Chrome is available, render a PNG (social, email header) or PDF (documents) at the exact size in the format file, for example:

  ```bash
  npx playwright screenshot --viewport-size=1080,1350 file://$PWD/after.html after.png
  ```

  If neither is available, say so and give them the HTML to open.
- **claude.ai:** show the HTML so they can see it, and offer it as a file. Tell them they can screenshot it or open it in a browser and print to PDF.

## Edit mode

Check the `Edit mode:` line in the brand's SKILL.md and follow `reference/editing.md`:

- `ask` (or no line): after showing the piece, offer once: "Want this as an editable page so you can tweak the words and colors yourself?"
- `always`: build the editable page as the output, from `templates/edit-post.html`.
- `never`: skip it.

Edit mode is for single pieces with a few slots (social posts, banners, covers, email headers, flyers). In claude.ai, publish the page as an artifact when you can, so it opens beside the chat; otherwise hand over the HTML file to open in a browser. It needs no saving, so it works on every plan.

## After they see it

Ask what's off, in their words. If the answer is a new rule ("never put text over the photo"), offer to add it with `update` so it sticks.
