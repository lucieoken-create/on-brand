# Pull: get what the brand already has

Goal: a list of what the brand already uses (colors, fonts, corner style, spacing feel, shadows, imagery, logo, illustration library) and how it uses them, each with a source and a confidence tag. This feeds the interview. It is not the finished system.

## 1. Ask what they have

Ask this every time, even when the person has already given a website address. A site shows the brand's values; the things they've made show how those values get used, and that's where most rules come from.

> To get this right, I need two things:
>
> 1. **Where your brand is defined today.** Your website, your current brand guide, or a design file (like a DESIGN.md or a Figma file). Just the latest version.
> 2. **Three to five things you've made recently that feel most like you now.** Ideally one of each thing you make most: a social post, a deck, a PDF, an email. Skip anything from before your last refresh.
>
> Optional: one piece that feels off or out of date, so I know what to avoid. And if you keep logos, illustrations, patterns or fonts in a folder (Google Drive, Notion, Dropbox), point me to that folder and I'll use those files in what I make.
>
> Is this your own brand, or a client's?

If it's neither, follow the "whose brand" rule in SKILL.md. If they only give a website, carry on: the interview will have more guesses to confirm.

### Why small and recent

Ask for a few chosen pieces, not everything. Older work carries older decisions, and three years of posts averages the brand into something that isn't quite any version of it. Two kinds of input get different limits:

- **Examples to learn from** (posts, decks, documents): three to five, recent, chosen by the person. More only if they're from the same period and cover different formats.
- **Assets to use** (logos, illustrations, patterns, fonts they own): a whole folder is fine, as long as it's the current set. These get copied and used, not read for rules.

### Connected folders and pages

If the person points to Google Drive, Notion, Dropbox, Figma or another connected source, ask for one folder or page, never the whole account. List what's there, suggest the three to five pieces to read (newest first, one per format) and the asset files to copy, and let them confirm before reading. Don't crawl. If no connector is available, ask them to attach the files instead, with the same limits.

## 2. Use the best method available

Try them in this order and stop when you have enough. Tell the person in one line which method you used.

### a. An existing system file or brand guide (any environment)

- **DESIGN.md, design tokens, a CSS file, a Figma or Claude Design export:** read it, map it to the DESIGN.md schema, and keep their names and wording. Tag values **exact**.
- **Brand guide PDF:** read the text for hex, RGB or CMYK values, color names, font names, logo rules and usage notes. Values printed in the guide are **exact**. Colors you can only see in images are **estimated**. CMYK-only colors: convert to hex and tag **estimated**, since the conversion depends on the printer profile.

### b. A website, with a shell and network (Claude Code, Codex)

Run:

```bash
python3 scripts/extract_site.py https://example.com --pages 3
```

It fetches the homepage and up to two inner pages it finds in the navigation, follows linked stylesheets, and prints JSON with: CSS custom properties, colors by how often they appear and where (text, background, border, shadow), font families, Google Fonts, font sizes, corner radii, shadows, theme color, logo and social-image URLs, and image folders that look like an illustration library. Values from it are **exact**.

Read it with judgment:

- The most frequent colors are usually the background, body text and one accent. Brand colors are often in custom properties with names like `--primary`, `--brand` or `--accent`.
- **Keep every brand color you find, including tints** (border shades, hover colors, muted text, text-on-dark). Don't trim the palette to a tidy number; ask about each one in the interview.
- **Look at the shadows.** A brand with no shadows, soft blurred shadows, and hard offset shadows (solid, no blur) are three different looks. Note which one it is, and where it's used.
- Ignore colors that only appear in third-party embeds, cookie banners or code highlighting.
- If the site is built with Tailwind or a site builder (Squarespace, Wix, Webflow, Shopify), the CSS is huge and generic. Lean on custom properties and the colors that appear most on headings, buttons and links. Say the result needs a closer look.
- Fonts listed under `font_face_families` are self-hosted. Many are Google Fonts loaded from the site's own server, so check before calling a font paid.
- If `image_folders` shows a folder with several images (like `/illustrations/` or `/ascii/`), that's probably an illustration library. Look at a few of the images and ask about the set in the interview.
- If no logo is found, look at the social image (`social_image`) and the favicon; the logo is often a wordmark set in type.
- If the script can't reach the site (blocked, needs JavaScript, error), say so and move to method c or d.

You can also run it on a saved HTML file: `python3 scripts/extract_site.py path/to/page.html`.

### c. A browser tool (Claude in Chrome or similar)

Open the homepage. Take a screenshot at desktop width and at phone width (about 390px). Read computed styles with JavaScript for `body`, `h1`, `h2`, `a`, `button` and the main navigation: `color`, `background-color`, `font-family`, `font-size`, `font-weight`, `letter-spacing`, `border-radius`, `box-shadow`. Tag values **read from page**.

### d. Screenshots only (claude.ai without network, or no site code)

A pasted link in claude.ai usually gives you the words on a page, not its styles, so ask for screenshots instead. From the images, estimate:

- the background, text and accent colors (give hex values)
- whether headings are serif or sans serif, heavy or light, tight or loose; name the nearest Google Font
- corners (square, slightly rounded, pill), borders, shadows (none, soft, or hard offset)
- photography, illustration, or neither; light or dark; busy or calm

Tag everything **estimated** and say why: screenshots shift colors, and fonts can only be matched by eye.

## 3. Read the pieces they've made

This is where the "how" comes from. For each piece, note:

- **Words:** how much text sits on an image or slide, what goes in a caption, how headlines are written.
- **Layout:** where things line up, how much room there is, whether art sits inside its space or runs off an edge.
- **Color use:** which color fills whole slides or posts, which only appears in small doses, which marks a takeaway or a first step.
- **Recurring parts:** frames, labels, numbering, list markers, footers, panels, tags.
- **Photos and illustration:** what appears on which kind of piece.
- **Differences between outputs:** a deck can be louder than a website, a document quieter than a post.

**A habit seen once is a guess, not a rule.** Seen in two or more pieces, it's a pattern worth confirming. When pieces disagree, the newest wins by default; ask if it matters.

**Decks and PDFs:** if you can't see the pages (the file reader shows text only), render them to images first. `pdftoppm -png -r 72 deck.pdf page` works where poppler is installed; `python3 -m pip install pymupdf` gives a Python route; on a Mac without either, a short Swift script using PDFKit works. For a long deck, lay the pages out on a contact sheet (an HTML grid of the images, screenshotted) to see the whole thing at once, then look closer at the slides that matter.

Colors sampled from rendered PDFs or images shift slightly with color profiles. Tag them **estimated**; values from code or a brand guide win.

## 4. Check consistency

If you have more than one page or piece, compare them. If they disagree, use the homepage or the newest piece as the source and note the differences. If they disagree a lot, ask which feels most like the brand now.

## 5. Report back

Show a short, plain summary, not raw JSON:

> Here's what I found on your site (read from the code, so these are exact) and in the two decks you shared:
> - Colors: deep navy #1D2B3A for text, warm white #FAF7F2 background, coral #E8664A on buttons and links. Also two lighter shades on borders (#D9D4CC, #C2BBB0).
> - Type: Fraunces for headlines, Inter for everything else (both Google Fonts)
> - Shape: slightly rounded corners (6px), a hard offset shadow on buttons, no soft shadows
> - Imagery: product photos on plain backgrounds; a set of line illustrations in /illustrations/
> - Logo: found at /logo.svg
> - In your decks: coral fills whole section slides; takeaways sit in a pale band at the bottom
>
> A couple of things to confirm in the next step: there's also a sage green (#8FA68E) on the about page only. Is that part of the brand?

Then move to `reference/decide.md`. If the person only asked for `pull`, offer to write the findings as a starter DESIGN.md with every value marked by confidence.
