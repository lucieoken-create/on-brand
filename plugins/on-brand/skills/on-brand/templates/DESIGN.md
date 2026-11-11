---
version: alpha
name: {{Brand}}
description: {{One line: the look in plain words, e.g. "Warm, coastal and uncluttered, with one coral accent."}}
colors:
  primary: "{{#hex}}"      # {{job, e.g. headlines and body text}}
  secondary: "{{#hex}}"    # {{job}}
  tertiary: "{{#hex}}"     # {{job, often the one accent}}
  neutral: "{{#hex}}"      # {{job, usually the background}}
  # Add plain-named colors only if they have their own job, e.g.:
  # surface: "#hex"        # panels and cards
typography:
  display:
    fontFamily: {{Headline font}}
    fontSize: {{48px}}
    fontWeight: {{600}}
    lineHeight: {{1.1}}
    letterSpacing: {{-0.02em}}
  body:
    fontFamily: {{Body font}}
    fontSize: {{17px}}
    fontWeight: {{400}}
    lineHeight: {{1.6}}
  label:
    fontFamily: {{Body or third font}}
    fontSize: {{13px}}
    fontWeight: {{500}}
    letterSpacing: {{0.08em}}
rounded:
  sm: {{0px}}
  md: {{0px}}
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 32px
  xl: 64px
components:
  button-primary:
    backgroundColor: "{colors.tertiary}"
    textColor: "{colors.neutral}"
    rounded: "{rounded.md}"
# omitted:
#   - section: elevation
#     reason: "No shadows in this brand"
---

<!-- Built with on-brand. Values marked "estimated" came from screenshots; check them against your real files when you can. -->

## Overview

{{Two or three sentences: who it's for, what they should feel in the first three seconds, and the look in plain words. Use the person's own words where possible.}}

## Colors

{{One line on the palette as a whole, including rough shares, e.g. "Mostly warm white, navy for all text, coral rarely and only for the one thing to act on."}}

- **Primary ({{#hex}}):** {{what it's for and where it never goes}}
- **Secondary ({{#hex}}):** {{job}}
- **Tertiary ({{#hex}}):** {{job}}
- **Neutral ({{#hex}}):** {{job}}

Text and background pairs that pass contrast: {{list}}. Pairs to avoid: {{list, or "none"}}.

## Typography

- **Headlines:** {{font}}, {{weight}}, {{feel, e.g. "tight and confident"}}. {{Google Font or licensed file}}.
- **Body:** {{font}}, {{weight}}. {{Why it fits.}}
- **Labels and small text:** {{font, size, case}}.

Headlines in {{sentence case / title case}}. {{Any other type rules: no all caps, no italics for emphasis, etc.}}

## Layout

{{Roomy or dense, how much margin, alignment habits (left-aligned, centered), grid notes. One short paragraph.}}

## Elevation & Depth

{{Shadows or none. If none, move this section to `omitted` in the front matter.}}

## Shapes

{{Corner style, borders, dividers, any signature shapes or patterns.}}

## Components

{{Only what they use: buttons, tags, photo frames, quote blocks. One line each.}}

## Do's and Don'ts

Do:
- {{rule from their answers}}
- {{rule}}

Don't:
- {{their refusals, in their words}}
- {{refusal}}
- Use colors outside this palette, or more than one accent in a piece.
- Put emoji in headlines, use gradient blobs or glossy effects, or round every corner by default.
- Use stock phrases like "unlock", "elevate", "seamless" or "take it to the next level".
