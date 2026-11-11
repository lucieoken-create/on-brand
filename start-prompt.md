# on-brand without installing anything

Two prompts. The first sets up your brand system in one chat. The second uses it whenever you make something. They work in Claude, and in most other AI chat tools.

The questions come from the on-brand skill's interview (`plugins/on-brand/skills/on-brand/reference/decide.md`). If that file changes, update this prompt to match.

## 1. Set up your brand system

Start a new chat. Attach what you have: screenshots of your website (homepage, one inner page, and how it looks on your phone), a brand guide PDF, your logo. Nothing is fine too. Then paste this:

```
I want to set up a simple design system for my brand so that everything you make for me looks like me. Please work through this with me in three parts.

PART 1: LOOK AT WHAT I HAVE
Look at anything I've attached. Tell me in plain words what you see: the colors (give hex codes), the fonts or the closest Google Fonts, how rounded the corners are, how roomy or busy it feels, and the kind of images. Say which values you read exactly (from a brand guide) and which you're estimating from images. If I didn't attach anything, skip to Part 2.

PART 2: ASK ME QUESTIONS, ONE AT A TIME
Ask one question, wait for my answer, then ask the next. For each one, suggest an answer based on what you saw so I can just react. No more than ten questions:
1. Who am I making things for, and what should they feel in the first three seconds?
2. Which color does most of the work, which is the background, and which is the one accent saved for important things? Roughly how much of each?
3. One font for headlines and one for everything else. Keep what I have, or change?
4. Square corners or rounded? Lots of breathing room, or packed? Anything that moves?
5. What would never appear in my brand? Push me for at least five specifics.
6. What logo, photos or patterns do I have, and anything I should never use?
7. When something I make looks off, what's usually the reason?
8. What do I make most: social posts, flyers, one-pagers, slides, email headers?
9. How much text goes on an image (for example, a headline of six words or fewer, four or five short phrases at most)? What goes on the image and what goes in the caption? Sentence case or title case?
10. Any words, punctuation or habits that should never show up? How is my business name written? How do I write prices, dates and calls to action?

Before Part 3, show me a one-screen summary of every decision and check that text colors are readable on their backgrounds. Wait for my OK.

PART 3: WRITE MY TWO FILES
Write two files as separate code blocks I can copy and save with these exact names.

DESIGN.md (how my brand looks): start with YAML front matter between --- lines with: version: alpha, name, description, colors (primary, secondary, tertiary, neutral as hex codes), typography (display, body and label, each with fontFamily, fontSize, fontWeight, lineHeight, letterSpacing), rounded, spacing. Then these sections in order: ## Overview, ## Colors (each color's job), ## Typography, ## Layout, ## Shapes, ## Components, ## Do's and Don'ts (my never-list in my words, plus: no colors outside the palette, no emoji in headlines, no gradient blobs, no stock phrases like "unlock" or "elevate"). Mark any estimated value.

PRODUCT.md (who it's for and why): no hex codes or font names. Sections: ## Who it's for, ## The feeling, ## Point of view, ## Why it looks this way, ## When something looks off, ## Where it shows up, ## Voice (three words), ## Copy on the page (business name, headline case and word limit, what goes on images vs captions, how prices, dates and calls to action are written, never-list).

Keep both short enough to read in ten minutes. Then make one test: a social post for something real in my business, as an image or HTML, following both files exactly.
```

## 2. Use it every time you make something

Save the two files somewhere you'll find them. Then either add them to a Claude Project and do your brand work there, or start a new chat, attach both files, and paste:

```
Attached are my DESIGN.md and PRODUCT.md. Follow them exactly for everything you make in this chat: only my colors and fonts, my copy rules and word limits, and nothing from my Do's and Don'ts. If something I ask for would break a rule, tell me before you make it. Never invent facts like prices or dates; ask me.

Here's what I need: [describe the post, flyer or slide, with the date, price and link it should include]
```

If a new rule comes up ("never put text over the photo"), ask Claude to add it to the right file and save the updated version.
