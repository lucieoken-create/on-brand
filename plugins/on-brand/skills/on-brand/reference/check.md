# Check: does this piece fit the system?

The person shares something (an image, a PDF, a screenshot, a page) and wants to know whether it fits their brand. Read DESIGN.md, PRODUCT.md and the matching format file first.

## What to look for

Go through these in order and note only real problems:

1. **Colors.** Any color not in the tokens? Is the accent overused or used on the wrong things? Do the shares roughly match DESIGN.md?
2. **Type.** Fonts other than the two in the system? Headline and body sizes in the right relationship? Case matches the copy rules?
3. **Contrast.** Any text that's hard to read against its background? Run `scripts/contrast.py` on sampled colors if you can; otherwise estimate and say so.
4. **Shape and space.** Corners, borders and shadows match? Crowded where the brand is roomy, or the other way round?
5. **Copy.** Over the word limit for the format? Banned words or punctuation? Business name written correctly? Facts in the caption that belong there?
6. **Never do.** Anything from the Do's and Don'ts list?
7. **AI defaults.** Emoji in headings, gradient blobs, generic rounded cards, stock phrases, a look that doesn't match their other pieces.

## How to report

A short list, most important first, each with what's wrong, where, and the fix:

> 1. The headline is 11 words; your limit on images is six. Try "20% off, this Saturday only."
> 2. The pink in the corner isn't in your palette. Swap it for the coral, or drop it.
> 3. Looks good: the type, the spacing, the photo style.

Keep it to five items or fewer. If more is wrong, say the piece needs a rebuild and offer to remake it with `make`.

End by asking them to make the last call: "Does it feel like you?" A checklist can pass work that still feels off, and they'll know.

Also run the piece against `reference/principles.md`, and report those findings the same way, each with the rule it falls under and what to change. Where the person's system and a principle disagree, the system wins and the principle is not a finding.
