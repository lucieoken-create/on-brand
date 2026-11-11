# Email: newsletter headers and announcement emails

Starter rules. Fill in the brand-specific lines when writing a system. Email clients are fussier than web browsers, so these rules lean cautious.

## Header images

- 600px wide on screen. Export at 1200px wide so it stays sharp on phones, and keep it under about 250px tall at 600 wide.
- Words on the header at least 32px at 600 wide, and only a few of them: the newsletter name and the issue or event.
- One header style for the series, with the issue, date or event changing.
- If they send through a platform with a fixed header slot (Substack, Beehiiv, Mailchimp, Kit), check that platform's current header size before making one; they differ.

## The email itself

- Put the important words in live text, not in an image. Many inboxes block images until the reader allows them, and screen readers can't read them. Give every image short alt text.
- One column, about 600px wide. Short paragraphs. Body text 16px or larger.
- One main button in {{accent color}} with {{button text color}} text, written to the call-to-action style in PRODUCT.md. A second link can be plain text.
- Logo or business name in the header, small. Contact details and an unsubscribe line in the footer.
- Fonts: email clients often ignore web fonts, so name a safe fallback for each (for example Georgia for a serif, Arial for a sans serif) and check the email still looks like the brand in that fallback.

## Dark mode

Some inboxes flip colors in dark mode. Avoid a header that's mostly white with thin dark text; give it its own background color. Logos on a transparent background need a version that works on dark.

## Words

- Subject line under about 50 characters, saying what's inside. Preview text adds the next most useful detail.
- {{Their copy rules: case, banned words, how dates and prices are written.}}

## Making it

Build the header as an image (from the social template, at 1200 × the chosen height). Build the email as simple HTML with inline styles, or give the person the copy and header to drop into their email platform's editor, which is usually easier for them.
