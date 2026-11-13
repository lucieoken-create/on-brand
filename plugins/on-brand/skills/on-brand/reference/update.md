# Update: change a decision or add a rule

Systems drift when new decisions live only in one chat. This mode folds them back into the files.

1. **Find where it belongs.** A look decision (color, type, shape, layout) goes in DESIGN.md and tokens.css. A why, audience or copy decision goes in PRODUCT.md. A rule for one kind of piece goes in that file in `formats/`. A "never" goes in Do's and Don'ts.
2. **Confirm the wording** with the person in one line before changing anything.
3. **Change the source first,** then anything that depends on it: a new color changes DESIGN.md's tokens and prose, tokens.css, and any format file that names colors.
4. **Re-check contrast** if a color changed.
5. **Log it.** Add a dated line under a "Changes" heading at the very end of DESIGN.md: `- 2026-11-20: added sage #8FA68E as a second background for seasonal posts.`
6. **Spec updates** (a platform changed a size): change the table in the format file, set its "Specs last checked" date to today, and log it the same way.
7. **Edit mode setting:** if they say "always make it editable", "ask me each time" or "stop offering", change the `Edit mode:` line in the brand's SKILL.md to `always`, `ask` or `never` and tell them.
8. **Deliver the updated files** the same way as `write`. In claude.ai, if Claude offers to save the changes to the skill (a card in the chat), accept it. If it doesn't, download the updated folder as a zip and upload it again to replace the old version.
