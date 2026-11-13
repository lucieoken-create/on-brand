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

Plus size and layout rules for the things you make most, the checks every piece goes through, and a skill file that makes the whole folder your brand's own skill. Social platforms change their sizes often, so your social rules carry the date they were last checked, and Claude looks up the current specs when they're out of date. The files are yours. They work even without this skill: attach them to any chat and most of the job is done.

## After setup: your own skill

You use on-brand once per brand. What it hands you at the end is your brand's own skill, installed where you work:

1. **on-brand, once:** it looks at what you have, asks its questions, writes your files, makes a test piece, and takes one round of feedback.
2. **The handover:** your system is installed as its own skill (say, `low-tide-goods-design`).
3. **From then on, your skill:** ask for what you want ("Make a LinkedIn post for our workshop on Dec 6") without mentioning on-brand. When something looks off, say so, and your skill writes the fix into your files.

Your skill doesn't need on-brand to keep working. It carries its own checks and its own update steps, and it works in Claude, Codex, and other tools that read skills or `AGENTS.md`. Come back to on-brand to set up another brand or a client, or for a bigger rework.

## Four ways to use it

**1. Claude Code.** Start Claude Code in Terminal (`claude`), then run:

```
/plugin marketplace add lucieoken-create/on-brand
/plugin install on-brand@on-brand
```

This is the most precise route: it reads your site's code for exact colors and fonts.

**2. Upload it to claude.ai.** Coming with the first release, once testing is done: a single `on-brand.zip` on the [releases page](https://github.com/lucieoken-create/on-brand/releases). Until then, use route 1, 3 or 4. When the zip is there: in claude.ai, go to Customize, then Skills, click +, then Create skill, then Upload a skill, and choose the zip. Skills work on every plan, as long as "Code execution and file creation" is on in Settings, then Capabilities (newer layouts call it "Create and edit files"). On Enterprise, an owner has to turn on Skills for the organization first, and can turn off skills that members create. A skill you upload to claude.ai also loads in Claude Code when you sign in with the same account.

**3. Codex.** Copy the `plugins/on-brand/skills/on-brand` folder into your Codex skills folder (`~/.codex/skills/on-brand/`), or into the repo you're working in, and ask Codex to use on-brand. The scripts are plain Python, and the system it writes includes an `AGENTS.md` so Codex follows it afterwards. <!-- Check the current Codex skills path before release. -->

**4. No install.** Copy the prompts in [start-prompt.md](start-prompt.md) into a new chat. You get the same interview and the same two files, without installing anything. Use this if your company account doesn't allow custom skills.

## Use it

Once it's installed, say:

```
Use on-brand to set up my brand. My website is example.com.
```

In claude.ai, attach screenshots of your site or a brand guide PDF instead of a link. Claude can read the words on a page from a link, but not its colors and fonts.

## What to give it

Less than you'd think, as long as you choose it:

- **Where your brand is defined today:** your website, your current brand guide, or a design file. Just the latest version.
- **Three to five recent things you've made that feel most like you now,** ideally one of each thing you make most (a post, a deck, a PDF). Your site shows your colors and fonts; your work shows how you use them, and that's where most of the rules come from.
- **Optional:** one piece that feels off or out of date, so it knows what to avoid.
- **Your asset folder,** if you have one: logos, illustrations, patterns, fonts. If it's in Google Drive, Notion or Dropbox and that's connected, point it to the one folder; it'll list what's there and check with you before reading.

Skip the archive. Three years of posts or every version of your guidelines carries old decisions along with the current ones, and the system comes out blurrier for it.

## What to expect

One run gets your foundations right: your colors and what each one is for, your fonts, spacing and shapes, your never-list and your copy rules. It won't know what you've learned from making things: how your decks differ from your posts, the fix for a PDF that rendered badly, the layout you settled on after three rounds with a client. Those come from use. When something looks off, say so, and the skill writes the fix into your system so it holds next time. That's how it goes from a good start to yours.

When I tested it on my own brand, one afternoon matched the foundations of the design system I'd spent months refining. Most of what was missing were production details that only shipping real work teaches.

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

## What keeps it from looking like AI

The skill carries fourteen rules I check on everything I make, and it runs each piece against them before showing it to you: one thing leads, the accent color stays rare, the headline says something specific, decoration needs a job, alignment is deliberate, type has a fixed hierarchy, and everything is precise to the pixel. Alignment is the note I give most often on a first pass from any AI tool. The full list is in [`reference/principles.md`](plugins/on-brand/skills/on-brand/reference/principles.md). Your own system wins wherever it disagrees with mine.

## Where I look

Two of the interview questions are hard to answer cold: what your brand should feel like, and what it would never do. It helps to look at a lot of good work first and notice what you're drawn to. I keep a public list of the places I go for that, with the design skills and references I use most: [Where I look: inspo and resources for AI-assisted design](https://hijinx-studio.notion.site/design-resources).

## Good to know

- **Some values are estimates.** Colors read from screenshots shift, and fonts can only be matched by eye. The skill marks these. Swap in exact values from your brand files when you can.
- **Use it on your own brand,** or a client's with permission. Point it at someone else's site and it treats it as inspiration and writes an original system. It won't copy another brand's logo or exact look.
- **Fonts:** it uses Google Fonts or font files you own, and tells you which. If your site uses a paid font, it suggests a free stand-in and labels it.
- **Already have a skill for your brand?** It names your system `<brand>-design` and checks first that the name is free, so it won't overwrite or clash with a skill you've built. Run setup in a fresh project so the old skill doesn't fill in answers for you.
- **It covers copy rules, not your whole voice.** Word limits, case, punctuation and banned words, yes. For how you sound in longer writing, pair it with a voice or writing-style skill.

## Updates

This repo is the source of truth. When I update the skill, the version number and changes are listed below. Claude Code users get updates through the plugin; claude.ai users download the new zip and upload it again. Your own DESIGN.md and PRODUCT.md never change when the skill does.

**Unreleased** (November 2026), from the first full test run: asks for recent work and an asset folder, not just a website; checks its suggestions against what it found; asks whether rules change between outputs; asks for color names, every tint, and how your web address is written; offers style names to react to; two new rules (type hierarchy, pixel precision); a rule for illustrations on color; fixes to the site extractor (pages read twice, shadows, logo, self-hosted Google Fonts, illustration folders); headless Chrome and PDF rendering fallbacks; a name check before writing; setup now ends after one round of feedback and a handover that installs your brand's own skill; that skill now works without on-brand (it carries the principles, contrast checker, editing rules and update steps).

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
