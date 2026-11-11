# Documents: PDFs, one-pagers, flyers and posters

Starter rules. Fill in the brand-specific lines when writing a system. Two kinds of document need different rules: ones people read on a screen (proposals, guides, lead magnets, one-pagers sent by email) and ones that get printed (flyers, posters, handouts). Ask which it is if it isn't obvious.

## Sizes

| Piece | Size | Notes |
| --- | --- | --- |
| Screen PDF, one-pager, proposal or guide (US) | Letter, 8.5 × 11 in | Most people open these on a laptop; letter also prints cleanly if they do print. |
| Screen PDF elsewhere | A4, 210 × 297 mm | |
| Flyer (US) | Letter, or half-page 5.5 × 8.5 in | Half-page is good for counters and bags. |
| Flyer elsewhere | A4, or A5 148 × 210 mm | |
| Small poster | 11 × 17 in (tabloid) or A3 | For shop windows. |

- Keep all text at least 0.5 in (12 mm) from the edge.
- For print that runs color to the edge, add 0.125 in (3 mm) bleed on every side and tell the person to choose "print with bleed" at the print shop. A home printer can't print to the edge, so keep a white margin for anything printed at home.

## Type sizes

| | Screen PDF | Flyer or poster |
| --- | --- | --- |
| Title or headline | 28 to 40pt | 48 to 96pt on a letter flyer, readable from across a room |
| Section heads | 16 to 22pt | 24 to 36pt |
| Body | 10.5 to 12pt | 11 to 14pt |
| Smallest text | 8pt | 8pt |

Fixed sizes only in print and PDFs. Fluid web sizing (CSS `clamp()`) doesn't belong in a document.

## Structure

- **Screen PDFs:** title block, then sections with clear heads, short paragraphs and lists. One idea per section. A proposal or guide over two pages gets page numbers and the brand name in a small footer.
- **Flyers:** headline, the one fact that matters most (date, offer), where and when, and how to find out more. {{Their word limits.}} Anything longer belongs in a one-pager.
- **One-pagers:** a short intro, three to five points, and contact details.

## Color

On screen, colors behave as in DESIGN.md. In print they look darker and duller: avoid very pale text on white and dark text on dark colors. Large areas of dark color use a lot of ink on home printers, so keep big fills light for anything printed at home.

## Images, links and codes

- Photos at 300 dpi at printed size for print. A phone photo is usually fine at half-page size; a web image usually isn't.
- Screen PDFs: make links clickable and write out where they go. Print: use a QR code at least 0.8 in (2 cm) square, dark on light, with a few words saying where it goes.

## Making the file

Build as HTML with `@page` set to the size (see `templates/flyer.html`), then print to PDF. Before handing over:

- Open the PDF and check the fonts embedded (look at the headline).
- Check nothing sits closer than the margin to the edge, and no line ends with one stray word.
- Set the PDF's title to the document name, so it doesn't show "Untitled" in a browser tab.
