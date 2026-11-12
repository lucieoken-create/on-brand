# on-brand

A Claude skill that turns your brand into a design system Claude follows, then makes on-brand social posts, emails, decks, PDFs and web pages from it.

> **Status: in testing.** This is a working draft (0.1.0). I'm running it on my own brand now, and the first tagged release comes after that. Expect changes, and tell me what breaks.

I'm Lucie Oken. I run [hijinx](https://hijinx.studio), and everything I make with AI starts from one design system: my site, my decks, my social posts, even my business card. AI makes things fast, but without a system everything looks like everyone else's. This skill is the process I used, packaged so you can do it for your own brand.

## What it does

1. **Pull.** It looks at what your brand already has: your website, a brand guide PDF, screenshots, or a design file from another tool. It tells you what it found and how sure it is about each value.
2. **Decide.** It asks you up to ten questions, one at a time, about the things no tool can see: who it's for, what each color is for, what your brand would never do, and how much text belongs on an image.
3. **Make.** It writes your system and makes a test post, once without the system and once with it, so you can see the difference. After that, ask for social posts and banners, email headers, slides, PDFs and flyers, or a web page, and they follow your rules. Anything else visual works too; it just doesn't have its own rules file yet.

## How this differs from Claude Design

Claude can already design things and hold a design system for you, right in a chat. on-brand works alongside that. The differences:

- **It asks before it builds.** Pulling colors and fonts from your files is the easy half. The half that makes work look like yours is judgment: what each color is for, what you'd never do, how many words belong on an image. on-brand gets that from you in about ten questions and writes it down.
- **It's made for marketing pieces.** Posts, banners, email headers, flyers and decks, with platform sizes and safe zones it keeps current.
- **The files are yours.** Two plain text files you can read, edit and take anywhere: Claude Code, another AI tool, a designer, or Claude's own design system setup.
- **It runs on a free plan.**

## Edit what it makes

Any single piece (a post, a banner, a flyer) can come back as an editable page. Change the words, switch between your own brand colors, pick a shape, download. Every option on the page is already in your system, so you can't knock it off-brand by exploring. You choose whether that happens every time, only when you say yes, or never. It doesn't save anything, so it works on every Claude plan.

## What you get

A folder for your brand. The two files that matter most:

- **DESIGN.md:** how your brand looks. Colors and their jobs, type, spacing, shapes, and your never-list. It uses the open [DESIGN.md format](https://github.com/google-labs-code/design.md) from Google Labs, so it also works with Claude's own design tools, impeccable, Stitch and others.
- **PRODUCT.md:** who it's for, why it looks the way it does, and your copy rules.

Plus size and layout rules for the things you make most, and a small skill file so Claude loads your system on its own. Social platforms change their sizes often, so your social rules carry the date they were last checked, and Claude looks up the current specs when they're out of date. The files are yours. They work even without this skill: attach them to any chat and most of the job is done.

## Three ways to use it

**1. Claude Code.** Start Claude Code in Terminal (`claude`), then run:

```
/plugin marketplace add lucieoken-create/on-brand
/plugin install on-brand@on-brand
```

This is the most precise route: it reads your site's code for exact colors and fonts.

**2. Upload it to claude.ai.** Coming with the first release, once testing is done: a single `on-brand.zip` on the [releases page](https://github.com/lucieoken-create/on-brand/releases). Until then, use route 1 or 3. When the zip is there: in claude.ai, go to Customize, then Skills, click +, then Create skill, then Upload a skill, and choose the zip. Skills work on every plan, as long as "Code execution and file creation" is on in Settings, then Capabilities. A skill you upload to claude.ai also loads in Claude Code when you sign in with the same account.

**3. No install.** Copy the prompts in [start-prompt.md](start-prompt.md) into a new chat. You get the same interview and the same two files, without installing anything. Use this if your company account doesn't allow custom skills.

## Use it

Once it's installed, say:

```
Use on-brand to set up my brand. My website is example.com.
```

In claude.ai, attach screenshots of your site or a brand guide PDF instead of a link. Claude can read the words on a page from a link, but not its colors and fonts.

After setup:

```
Use my brand system to make an Instagram post for our holiday open house, Saturday Dec 6, 2 to 6pm.
```

```
Check this flyer against my brand system.
```

## Using it for your website

Your design system works for your site too, in three ways:

- **Hand it to your website tool.** If you build with Lovable, Claude Code or another AI builder, give it your DESIGN.md and `tokens.css` so the site follows the same rules as your posts.
- **Set up a site builder.** On Squarespace, Wix, Shopify or Webflow, ask Claude to turn your system into that builder's color, font and spacing settings.
- **Make one page or one part of a page.** A landing page for an event, a link-in-bio page, or a single section such as a signup block, a pricing table or a header.

It doesn't build or manage a whole site. For that, use your system with a tool made for it; [impeccable](https://github.com/pbakaus/impeccable) is a good one if you work in code.

## Where I look

Two of the interview questions are hard to answer cold: what your brand should feel like, and what it would never do. It helps to look at a lot of good work first and notice what you're drawn to. I keep a public list of the places I go for that, with the design skills and references I use most: [Where I look: inspo and resources for AI-assisted design](https://hijinx-studio.notion.site/design-resources).

## Good to know

- **Some values are estimates.** Colors read from screenshots shift, and fonts can only be matched by eye. The skill marks these. Swap in exact values from your brand files when you can.
- **Use it on your own brand,** or a client's with permission. Point it at someone else's site and it treats it as inspiration and writes an original system. It won't copy another brand's logo or exact look.
- **Fonts:** it uses Google Fonts or font files you own, and tells you which. If your site uses a paid font, it suggests a free stand-in and labels it.
- **It covers copy rules, not your whole voice.** Word limits, case, punctuation and banned words, yes. For how you sound in longer writing, pair it with a voice or writing-style skill.

## Updates

This repo is the source of truth. When I update the skill, the version number and changes are listed below. Claude Code users get updates through the plugin; claude.ai users download the new zip and upload it again. Your own DESIGN.md and PRODUCT.md never change when the skill does.

**0.1.0** (November 2026): working draft, in testing. Not yet released.

## What's next

- **Now:** the design system and pieces made from it.
- **Now, new:** edit mode, described above.
- **Later:** a brand studio. One page with your brand guide (logos, colors, type, which file to use where) and a place to make new pieces from a few starting layouts. The rules for building one are already in [`reference/editing.md`](plugins/on-brand/skills/on-brand/reference/editing.md), so you can ask Claude to try it today; a tested version comes in a later release.

## Credits

on-brand stands on other people's work:

- The [DESIGN.md format](https://github.com/google-labs-code/design.md) from Google Labs (Apache 2.0).
- [impeccable](https://github.com/pbakaus/impeccable) by Paul Bakaus, for the idea of keeping strategy (PRODUCT.md) separate from visuals (DESIGN.md). If you build websites, use it.
- [jezweb's design-system skill](https://github.com/jezweb/claude-skills), for the order to look for colors and fonts in a site's code, and for checking the result with a test piece.
- Anthropic's skill-creator, which I used to build and test this.

No text from these projects is copied here.

## License

MIT. Use it, change it, share it.
