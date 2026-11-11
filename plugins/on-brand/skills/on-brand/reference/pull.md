# Pull: get what the brand already has

Goal: a list of what the brand already uses (colors, fonts, corner style, spacing feel, imagery, logo), each with a source and a confidence tag. This feeds the interview. It is not the finished system.

## 1. Ask what they have

One question, with options:

> What can you share so I can see your brand as it is today? Any of these works: your website address, a brand guide PDF, a few screenshots (your homepage, one inner page, and how it looks on a phone), your logo, or a design file from another tool like a DESIGN.md. Or nothing yet, and we'll build it from questions.

Also ask, in the same message if it fits: "Is this your own brand, or a client's?" If it's neither, follow the "whose brand" rule in SKILL.md.

## 2. Use the best method available

Try them in this order and stop when you have enough. Tell the person in one line which method you used.

### a. An existing system file or brand guide (any environment)

- **DESIGN.md, design tokens, a CSS file, a Figma or Claude Design export:** read it, map it to the DESIGN.md schema, and keep their names and wording. Tag values **exact**.
- **Brand guide PDF:** read the text for hex, RGB or CMYK values, font names, logo rules and usage notes. Values printed in the guide are **exact**. Colors you can only see in images are **estimated**. CMYK-only colors: convert to hex and tag **estimated**, since the conversion depends on the printer profile.

### b. A website, with a shell and network (Claude Code, Codex)

Run:

```bash
python3 scripts/extract_site.py https://example.com --pages 3
```

It fetches the homepage and up to two inner pages it finds in the navigation, follows linked stylesheets, and prints JSON with: CSS custom properties, colors by how often they appear and where (text, background, border), font families, Google Fonts links, font sizes, corner radii, theme color, and logo and social-image URLs. Values from it are **exact**.

Read it with judgment:

- The most frequent colors are usually the background, body text and one accent. Brand colors are often in custom properties with names like `--primary`, `--brand` or `--accent`.
- Ignore colors that only appear in third-party embeds, cookie banners or code highlighting.
- If the site is built with Tailwind or a site builder (Squarespace, Wix, Webflow, Shopify), the CSS is huge and generic. Lean on custom properties and the colors that appear most on headings, buttons and links. Say the result needs a closer look.
- If the script can't reach the site (blocked, needs JavaScript, error), say so and move to method c or d.

You can also run it on a saved HTML file: `python3 scripts/extract_site.py path/to/page.html`.

### c. A browser tool (Claude in Chrome or similar)

Open the homepage. Take a screenshot at desktop width and at phone width (about 390px). Read computed styles with JavaScript for `body`, `h1`, `h2`, `a`, `button` and the main navigation: `color`, `background-color`, `font-family`, `font-size`, `font-weight`, `letter-spacing`, `border-radius`. Tag values **read from page**.

### d. Screenshots only (claude.ai without network, or no site code)

A pasted link in claude.ai usually gives you the words on a page, not its styles, so ask for screenshots instead. From the images, estimate:

- the background, text and accent colors (give hex values)
- whether headings are serif or sans serif, heavy or light, tight or loose; name the nearest Google Font
- corners (square, slightly rounded, pill), borders, shadows
- photography, illustration, or neither; light or dark; busy or calm

Tag everything **estimated** and say why: screenshots shift colors, and fonts can only be matched by eye.

## 3. Check consistency

If you have more than one page or screenshot, compare them. If they disagree, use the homepage as the source and note the differences. If they disagree a lot, ask which page feels most like the brand.

## 4. Report back

Show a short, plain summary, not raw JSON:

> Here's what I found on your site (read from the code, so these are exact):
> - Colors: deep navy #1D2B3A for text, warm white #FAF7F2 background, coral #E8664A on buttons and links
> - Type: Fraunces for headlines, Inter for everything else
> - Shape: slightly rounded corners (6px), no shadows
> - Imagery: product photos on plain backgrounds
> - Logo: found at /logo.svg
>
> A couple of things to confirm in the next step: there's also a sage green (#8FA68E) on the about page only. Is that part of the brand?

Then move to `reference/decide.md`. If the person only asked for `pull`, offer to write the findings as a starter DESIGN.md with every value marked by confidence.
