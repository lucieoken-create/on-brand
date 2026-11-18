# on-brand without installing anything

Two prompts. The first sets up your brand system in one chat. The second uses it whenever you make something. They work in Claude, and in most other AI chat tools.

The questions come from the on-brand skill's interview (`plugins/on-brand/skills/on-brand/reference/decide.md`). If that file changes, update this prompt to match.

## 1. Set up your brand system

Start a new chat. Attach what you have: screenshots of your website (homepage, one inner page, and how it looks on your phone) or your current brand guide PDF, plus three to five recent things you've made that feel most like you now (a post, a deck, a PDF), and your logo. Skip older work; it carries old decisions. Haven't made much yet? Attach what you have instead: a palette you picked, photos of your shop or packaging, a few mood pictures, a brand you like the look of. Nothing is fine too. Then paste this:

```
I want to set up a simple design system for my brand so that everything you make for me looks like me. Please work through this with me in three parts.

PART 1: LOOK AT WHAT I HAVE
Look at anything I've attached. Tell me in plain words what you see: the colors (give hex codes, including lighter shades used for borders or small text), the fonts or the closest Google Fonts, how rounded the corners are, any shadows (none, soft and blurry, or solid offset blocks), how roomy or busy it feels, and the kind of images. From the things I've made, tell me the habits you see: how much text sits on an image, where each color shows up, what repeats. Say which values you read exactly (from a brand guide) and which you're estimating from images. Then ask me once which of my files can appear in my pieces and which are just for the feel, and ask what one thing I want to make soon, so you can try choices out on it. If I didn't attach anything, ask me for three to five things I like the look of (anything: a café, a book cover, a sign), tell me what you see in each, and ask which parts I like.

PART 2: ASK ME QUESTIONS, ONE AT A TIME
Ask one question, wait for my answer, then ask the next. Start each one with its number and what it decides (for example, "Question 3 of 10: type"). If I've already answered something, skip it. For each one, suggest an answer based on what you saw so I can just react, and if your suggestion goes against something you saw, say so. Use plain words and describe what things look like rather than using design terms; if you can show me options side by side, on the thing I want to make, do. Fonts must be real fonts I can install, labeled with their names. Once I pick a version, change one thing at a time from that version. No more than ten questions:
1. Who am I making things for, and what should they feel in the first three seconds? Where does my business name come from?
2. Which color does most of the work, which is the background, and which accents are saved for important things (one or two, each with a job)? Roughly how much of each? Do I have names for these colors? If I don't want a loud accent, how should the one important thing stand out?
3. One font for headlines and one for everything else. Keep what I have, or change?
4. Square corners or rounded? Lots of breathing room, or packed? Shadows: none, soft, or solid offset blocks? Do I make Reels, Stories or GIFs?
5. What would never appear in my brand? Push me for at least five specifics.
6. What logo, photos or patterns do I have, and anything I should never use? Is there a meaning in my logo?
7. When something I make looks off, what's usually the reason?
8. What do I make most: social posts or banners, email newsletters, slides, PDFs like proposals or guides, flyers, web pages? Then: do these rules hold for everything I make, or are there exceptions (for example, slides louder than my website)? Will I print anything? How do I want pieces handed to me: an image, a PowerPoint or Word file, or a file to finish in Canva or Adobe?
9. How much text goes on an image (for example, a headline of six words or fewer, four or five short phrases at most)? What goes on the image and what goes in the caption? Sentence case or title case?
10. Any words, punctuation or habits that should never show up? How is my business name written? How do I write my web address, email and handles on a piece? How do I write prices, dates and calls to action?

Before Part 3, show me a one-screen summary of every decision and check that text colors are readable on their backgrounds. A color I love that's too light for text can stay as a fill or background. List only what's really still open. Wait for my OK.

PART 3: WRITE MY TWO FILES
Write two files as separate code blocks I can copy and save with these exact names.

DESIGN.md (how my brand looks): start with YAML front matter between --- lines with: version: alpha, name, description, colors (primary, secondary, tertiary, neutral as hex codes), typography (display, body and label, each with fontFamily, fontSize, fontWeight, lineHeight, letterSpacing), rounded, spacing. Then these sections in order: ## Overview, ## Colors (each color's job), ## Typography, ## Layout, ## Shapes, ## Components, ## Do's and Don'ts (my never-list in my words, plus: no colors outside the palette, no emoji in headlines, no gradient blobs, no stock phrases like "unlock" or "elevate"). Mark any estimated value.

PRODUCT.md (who it's for and why): no hex codes or font names. Sections: ## Who it's for, ## The feeling, ## Point of view, ## Why it looks this way, ## When something looks off, ## Where it shows up, ## Voice (three words), ## Copy on the page (business name, headline case and word limit, what goes on images vs captions, how prices, dates and calls to action are written, never-list).

Keep both short enough to read in ten minutes. Then make one test: the thing I said I want to make (or a social post for something real in my business), as an image or HTML, following both files exactly. Leave out designing a logo, illustrations or animation; list them as still open.
```

## 2. Use it every time you make something

Save the two files somewhere you'll find them. Then either add them to a Claude Project and do your brand work there, or start a new chat, attach both files, and paste:

```
Attached are my DESIGN.md and PRODUCT.md. Follow them exactly for everything you make in this chat: only my colors and fonts, my copy rules and word limits, and nothing from my Do's and Don'ts. If something I ask for would break a rule, tell me before you make it. Never invent facts like prices or dates; ask me.

Here's what I need: [describe the post, flyer or slide, with the date, price and link it should include]
```

If a new rule comes up ("never put text over the photo"), ask Claude to add it to the right file and save the updated version.
