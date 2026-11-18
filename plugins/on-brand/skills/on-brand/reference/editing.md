# Editing: pieces the person can tweak themselves

Read this before building an editable piece (edit mode) or anything bigger, like a brand studio. It holds the rules that make an editor usable by someone who is not a designer, and that keep every edit inside the brand.

## Edit mode in one paragraph

A finished piece comes back as one page with the piece on one side and a short panel of controls on the other. The person changes the words, picks between the brand's own options, and downloads the result. Nothing is saved anywhere, so it works on every Claude plan (in claude.ai it needs "Code execution and file creation" turned on). Start from the brand's own `templates/edit-post.html`: if it was filled in during setup, most of the work is done.

## When to build one

The brand's own SKILL.md carries a line: `Edit mode: ask`, `always` or `never`.

- `ask` (the default): after showing a piece, offer once in one line: "Want this as an editable page so you can tweak the words and colors yourself?" Build it only on a yes.
- `always`: every piece comes back editable. No question.
- `never`: don't build one and don't offer.

If they answer the offer with "always" or "stop asking", change the line in the brand's SKILL.md and say so. An editable page costs more to make than a plain one, so say that once if they ask about usage.

Edit mode fits single pieces with a few slots: social posts, banners, event covers, email headers, flyers. For decks, long documents and web pages, offer plain changes in chat instead.

## The rules

**Start from the output.** Before building any controls, look at the finished piece and list what a person would reasonably want to change: a word, the date, which color leads, the photo, the shape. Every item on that list gets a control. Anything nobody would change gets none. After building, go down the list again and confirm each change can be made from the panel.

**1. The piece is data.** Everything that can change lives in one `spec` object: the words, the color pairing, the size step, the shape, the photo. The page never edits its own layout directly. A control changes the spec, and the spec is drawn again.

**2. One renderer.** A single `render(ctx, spec)` function draws the piece. The preview calls it, and the download calls the same function at full size. What they see is what they get, because there is no second code path to drift.

**3. Controls are named choices, never free values.** No color picker, no font menu, no pixel fields. Offer the pairings DESIGN.md allows ("Navy on cream", "Cream on navy"), a size stepper with a floor and a ceiling, left or center, photo on or off. Every option on the panel is already on-brand, so the person can't break the system by exploring.

**One control per thing.** If two things can be wanted separately, they get separate controls: photo on or off is not tied to the color pairing, and the footer can be hidden without hiding the label. A single switch that turns two things off together is the most common complaint about a first-pass editor. Use a switch for on or off, a row of buttons for a choice between a few, and a stepper for more or less.

**4. Only offer pairings that pass.** Run every text and background pairing through `scripts/contrast.py` before it goes in the editor. A pairing that fails for body text is left out, or kept for large headlines only and labeled that way.

**5. Write the brand's refusals into the code.** If PRODUCT.md says headlines are six words or fewer, the editor counts words and shows a plain note when the line runs long. If the script font never goes in capitals, the control isn't there. Limits belong in the editor, with the reason in a short note, so the person learns the rule while using it.

**6. Words first.** Order the panel the way people edit: the words, then the look, then the shape, then download. Label fields by what they are in the piece ("Headline", "The date", "Footer, right"), in the person's vocabulary, never by element or variable name.

**7. Shapes re-lay out. They never crop.** If the editor offers more than one size, each size is laid out again from the spec, with its own values where one layout doesn't fit all: a shorter photo and a smaller headline on a square, a bigger photo filling the middle of a Story. Platform safe zones are drawn as a guide the person can switch on, shown in the preview only and never in the download. When the words run into the footer or out of the safe zone, show a plain note saying what to do ("Cut a few words, make the headline smaller or turn off the photo"). Render every shape with the longest likely words before handing it over.

**8. Always a way back.** A "Start over" button returns the piece to how Claude made it. It takes two clicks, and the button says so after the first. If the editor has parts (slides, scenes), each part gets its own reset too.

**9. Say what's happening in plain words.** One status line. "Ready", "Downloading", "This view blocked the download. Right-click the picture and save it." Every failure message says what to do next.

**Downloads work inside an artifact and outside it.** A claude.ai artifact blocks a plain download link. Published as an artifact, the page needs the `downloads` capability: declare it when publishing (`downloads: true`), then in the page `claude.use('downloads')` resolves to an object whose `save({ filename, data })` offers the file; the person confirms, and may decline. `use()` resolves `null` where the capability isn't there, such as a file opened in a browser, and then the page falls back to a plain download link. The template does both. Never promise the save happened until it resolves.

**The editor itself is plain and tidy.** The page around the piece is neutral: grey, white and one dark text color, in a system font. It carries nobody's brand, on-brand's included, so the only brand on screen is the person's own piece. Plain is still designed: controls line up on one grid, boxes in a row share a height, labels don't wrap awkwardly, and nothing overlaps or leaves a ragged gap when the window is resized. People who care about design notice a sloppy editor and trust the output less.

**10. Self-contained.** One HTML file, no outside scripts, stylesheets, fonts or images, since published pages can't load them. Fonts the brand owns or Google Fonts files are embedded as base64 when the files are on hand (`assets/fonts/`); otherwise the editor uses the fallback named in tokens.css and says so in a note. Marks and a starter photo can be embedded too. Photos the person uploads stay in their browser.

Embedding adds up: fonts, a logo in three colors and a photo can pass half a megabyte. Embed only the weights the editor uses, shrink images to the largest size they're drawn at (a logo drawn 280px wide doesn't need a 2000px file), and save photos as JPEG. Keep one copy of the editor in the brand folder.

**11. Don't depend on saving.** Saving edits between visits needs storage that is not on every plan. Edit mode works without it: edit, download, done. If you keep a draft in browser storage as a convenience, wrap it in try/catch and never promise it will be there.

**12. Check it like a product.** Before handing it over: click every control, type a long headline and a blank one, try each shape, download once and open the file, and drag the window from wide to narrow, checking at several widths that rows of buttons stay even and nothing is cut off. Fix what breaks before the person finds it.

## Building one from the template

1. Copy `templates/edit-post.html`.
2. Fill `BRAND`: the pairings from DESIGN.md (name, background, text, and the tag and mark colors for each background), the display, body and label font stacks, the word limits and the never-list from PRODUCT.md.
3. **The mark and the tag.** If the brand has a logo or a signature mark, embed the files (one per color the pairings need) in `MARKS` and keep the mark control: each mark the brand allows, plus "None". If it has only a logo, offer logo or none. If its pieces carry a date or time tag, keep the tag; if not, delete the tag field and leave the highlighted fact in the accent color.
4. Fill `START`, the spec for this piece, with the words and choices Claude made.
5. Set each shape's values in `SHAPES` (photo height, headline scale, mark size) and check the safe zones against `formats/social.md`. If the layout in DESIGN.md differs from the template's (centered, photo-led, a rule under the label), change `render` to match. Keep it one function.
6. Run the checks in rule 12.

## Going further: a brand studio

A studio is the same idea at full size: a page with the brand guide (logos to download, colors, type, which file to use where) and a "make something" side that turns a headline and details into several layouts to pick from and edit. It is planned as a later release of on-brand.

If someone asks for one now, build it from these rules plus four more:

- **Starting points and copies.** Ship a few starting layouts. Editing happens on a copy ("Duplicate"), so a starting point is always there to return to, and copies are named by the person.
- **Versions need storage.** Saved versions only work where the page can keep data (paid plans today). Say that up front, and keep the download path working without it.
- **Assets are a library, not uploads each time.** Logos, marks, patterns and approved photos sit in a rail and are placed by clicking, each with a note on where it may be used.
- **Budget for testing.** A studio is a small app. One pass will produce something simpler than a hand-tuned one, and it gets good through rounds of use and fixes. Tell the person that before starting.
