# Decide: the questions only the person can answer

Extraction shows how the brand looks today. It can't tell you what each color is for, what the brand would never do, or why. Those answers are what keep AI-made work from drifting back to generic, so this step matters most.

## How to ask

- **One question at a time.** Wait for the answer before the next one.
- **Lead with a suggestion** drawn from what `pull` found, so they react instead of starting cold: "Your buttons and links use the coral. Should coral be the one accent, used only for things people click?"
- **Check every suggestion against the pull before you offer it.** People accept most suggestions as written, so a wrong suggestion becomes a wrong rule. If a suggestion goes against something the pull found, say so in the question: "Your site uses a hard offset shadow on the headshot. Keep it, or should shadows be on the never-list?" Never suggest a rule the evidence contradicts without naming the evidence.
- **Plain words, and describe what things look like.** Say "the color for headlines", not "primary token"; "how rounded the corners are", not "border radius". Many people who care about design aren't designers, and design words get misread. When a word has more than one meaning, describe each one: "a soft, blurry shadow under a card" vs. "a solid block offset behind it, with no blur"; "art that runs off the edge of the page" instead of "bleed".
- **Accept short answers.** "Yes", "not that", "whatever you think" are fine. For "whatever you think", make the call, say what you chose and why, and move on.
- **Ten questions at most.** Skip any question the pull already answered with confidence; just confirm it in the summary.
- If there was nothing to pull (no site, no guide), ask the same questions with examples instead of suggestions, and offer two or three concrete options for colors and fonts.

## The questions

Ask in this order. The wording is a guide; adjust it to the person and what you found.

1. **Point of view.** "Who are you making things for, and what should they feel in the first three seconds of seeing one of your posts?" Suggest a main audience and a second one if the evidence points to both.
2. **Colors and their jobs.** Confirm every color found, including tints like border shades, hover colors and muted text: "These four lighter shades show up on borders and small text. Are they part of the system?" Then: "Which one should do most of the work, which is the background, and which are the accents that only show up for important things?" A brand can have one or two accents if each has its own job. Get a rough share for each, like mostly warm white, navy for text, coral rarely. Ask: "Do you have names for these colors?" and use their names in the files.
3. **Type.** "One font for headlines and one for everything else. Here's what your site uses. Keep them, or is there a reason they don't feel right?" Note why the fonts fit, in their words.
4. **Shape, space and motion.** "Square corners or rounded? Lots of breathing room, or packed with information? Shadows: none, soft and blurry, or solid offset blocks? Anything that moves?"
5. **Refusals.** "What would never appear in your brand? Colors, styles, words, kinds of photos, anything." Push gently for specifics: "Anything you've seen a competitor do that you'd never do?" This is the most important question. Aim for at least five items. Check each suggested item against the pull (see "How to ask").
6. **Assets.** "Do you have a logo file, photos you own, illustrations or patterns we should use? Where do you keep them? Anything we should never use, like an old logo?" If the pull found an illustration folder, show it and ask whether it's the full set.
7. **Reasoning.** "When something you've made looks off, what's usually the reason?" (Too busy, wrong color, looks cheap, looks like everyone else, nothing lines up.) The answer becomes a rule.
8. **Where it shows up.** "What do you make most often: social posts or banners, email newsletters, slides, PDFs like proposals or guides, flyers, web pages?" This decides which format files get written, and which platforms to note in the social file. Note anything they want to make later. Default to social posts and documents if they're unsure.
   Then ask straight away: **"Do these rules hold for everything you make, or are there exceptions?"** For example, slides that are louder than the website, photos allowed in decks but not on the site, a color that fills whole slides but only appears in small doses on posts. Write exceptions into the matching format file.
9. **Words on the page.** "How much text should go on an image? For example, a headline of six words or fewer and no more than four or five short phrases. What goes on the graphic, and what goes in the caption? Sentence case or title case for headlines?"
10. **Copy habits.** "Any words, punctuation or habits that should never show up? Exclamation points, emoji, ALL CAPS, certain buzzwords? How is your business name written? How do you write your web address, email and social handles on a piece (for example, in capitals)? How do you write prices, dates and calls to action?"

If they're stuck on question 1 or 5 (what it should feel like, what it would never do), that's normal. Suggest they look at work they like first, and point them to Lucie's public list of places to look: https://hijinx-studio.notion.site/design-resources. Offer to carry on with the other questions and come back.

Voice gets one line in PRODUCT.md (three words for how the brand sounds). If they want more than that, suggest a separate voice skill.

## Name the style

Most people can't name their style, and a name helps every tool that reads the files later. After question 7, offer two or three named styles that fit what you've seen, plus one look-alike to rule out, and let them react: "Your work reads as Swiss (grid, clean sans serif, lots of white space) with a terminal nod. The look-alike to avoid is vaporwave, which also uses classical busts and purple." Use names designers and AI tools already know. If none fits, describe it in a short phrase of their own ("terminal meets gallery"). Write the name into DESIGN.md's overview and the look-alike into Do's and Don'ts. For a longer list of style names, point to a reference like "50 Design Styles Every Designer Should Know for Better Prompting" (UX Planet), without copying from it.

## The summary

Before writing anything, show one screen that covers every decision, grouped: who it's for, colors with jobs and shares, type, shape and space, never do, assets, where it shows up (and any exceptions by output), copy rules. Mark anything still estimated, and anything based on a habit seen only once. Mark any contrast pair that fails.

End with: "Anything to change before I write your files?" Only move on to `reference/write.md` after a yes or their changes.
