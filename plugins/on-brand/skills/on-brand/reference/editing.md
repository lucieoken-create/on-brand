# Editing: pieces the person can tweak themselves

Read this before building an editable piece (edit mode) or anything bigger, like a brand studio. It holds the rules that make an editor usable by someone who is not a designer, and that keep every edit inside the brand.

## Edit mode in one paragraph

A finished piece comes back as one page with the piece on one side and a short panel of controls on the other. The person changes the words, picks between the brand's own options, and downloads the result. Nothing is saved anywhere, so it works on every Claude plan. Start from `templates/edit-post.html`.

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

**7. Shapes re-lay out. They never crop.** If the editor offers more than one size, each size is laid out again from the spec. Platform safe zones are drawn as a guide the person can switch on, shown in the preview only and never in the download.

**8. Always a way back.** A "Start over" button returns the piece to how Claude made it. It takes two clicks, and the button says so after the first. If the editor has parts (slides, scenes), each part gets its own reset too.

**9. Say what's happening in plain words.** One status line. "Ready", "Downloading", "This view blocked the download. Right-click the picture and save it." Every failure message says what to do next.

**The editor itself is plain and tidy.** The page around the piece is neutral: grey, white and one dark text color, in a system font. It carries nobody's brand, on-brand's included, so the only brand on screen is the person's own piece. Plain is still designed: controls line up on one grid, boxes in a row share a height, labels don't wrap awkwardly, and nothing overlaps or leaves a ragged gap when the window is resized. People who care about design notice a sloppy editor and trust the output less.

**10. Self-contained.** One HTML file, no outside scripts, stylesheets, fonts or images, since published pages can't load them. Fonts the brand owns or Google Fonts files are embedded as base64 when the files are on hand; otherwise the editor uses the fallback named in tokens.css and says so in a note. Photos come from the person's own upload and stay in their browser.

**11. Don't depend on saving.** Saving edits between visits needs storage that is not on every plan. Edit mode works without it: edit, download, done. If you keep a draft in browser storage as a convenience, wrap it in try/catch and never promise it will be there.

**12. Check it like a product.** Before handing it over: click every control, type a long headline and a blank one, try each shape, download once and open the file, and drag the window from wide to narrow, checking at several widths that rows of buttons stay even and nothing is cut off. Fix what breaks before the person finds it.

## Building one from the template

1. Copy `templates/edit-post.html`.
2. Fill `BRAND`: the pairings (name, background, text, accent) from DESIGN.md, the display and body font stacks, the headline word limit and footer text from PRODUCT.md.
3. Fill `START`, the spec for this piece, with the words and choices Claude made.
4. If the layout in DESIGN.md differs from the template's (centered, photo-led, a rule under the eyebrow), change `render` to match. Keep it one function.
5. Run the checks in rule 12.

## Going further: a brand studio

A studio is the same idea at full size: a page with the brand guide (logos to download, colors, type, which file to use where) and a "make something" side that turns a headline and details into several layouts to pick from and edit. It is planned as a later release of on-brand.

If someone asks for one now, build it from these rules plus four more:

- **Starting points and copies.** Ship a few starting layouts. Editing happens on a copy ("Duplicate"), so a starting point is always there to return to, and copies are named by the person.
- **Versions need storage.** Saved versions only work where the page can keep data (paid plans today). Say that up front, and keep the download path working without it.
- **Assets are a library, not uploads each time.** Logos, marks, patterns and approved photos sit in a rail and are placed by clicking, each with a note on where it may be used.
- **Budget for testing.** A studio is a small app. One pass will produce something simpler than a hand-tuned one, and it gets good through rounds of use and fixes. Tell the person that before starting.
