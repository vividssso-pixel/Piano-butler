# Short and plain: one chapter's Lesson Book (and guide page)

The author (Sohyun, a piano teacher) asked, for every chapter: "다 심플하게 설명해줘 군더더기 없이" (explain everything simply, nothing extra). Her model sentence, from the new chapter 5:
  "A crotchet has a filled head and a stem. It lasts one beat. Walk: one step on each beat. Its other name is a quarter note."
Short sentences. One fact each. No warm-up words, no repeating what the picture or the title already says, no asides, no "the closest key there is"-style restatements.

## Your job
Propose shorter wording for ONE chapter, as exact string replacements. DO NOT edit the source files. Write your result to the JSON path you are given.

Source: /home/claude/pbtest/g460/base.src.html (one big JSX file). Your chapter's pages are one function (name and start line given to you); it ends where the next top-level function starts. Inside it, shorten:
- every LbSay paragraph (both the Korean `LANG === 'ko' ? <>...</>` branch and the English branch),
- every LbPiano step (Korean and English lists),
- every LbRemember line, LbTune `how` text, the opener's "By the end, you can" lines and the five check rows' text, if they are wordy.
Leave alone: titles and kickers (t('Step 1'...), page titles), table-of-contents rows, picture drawing code and its numbers, aria labels (the long picture descriptions passed to pic(...)), any code, ids, keys, storeKey, component names.

If a guide page is given: /home/claude/pbtest/g460/guide/<file>.html is the public web page for the same chapter (HTML). Shorten its body paragraphs (<p>, <li>) the same way. Leave the <!--meta--> JSON, headings, links, {{svg:...}} and {{beats:...}} markers, the FAQ questions (h3) and the nav/footer alone. FAQ answers may be shortened but must still answer the question. The teacher's note (<aside class="note">) is the author's own words: do NOT change it.

## Rules (the author's Book rules)
- Keep every fact, every set task detail (which hand, which finger, which key or house, how many times), the cast and metaphors (the Queen and King, Queensland/Kingsland, the small house and big house, the bird's sky and turtle's sea, Clara, the rabbit butler, the hidden attic, ladders/ledger lines, the five Cs' names, etc.). Shorter, never different.
- Korean must be just as short and natural; keep Korean and English saying the same thing.
- A second name: "Its other name is ..." / "다른 이름은 ...". Never say whose books use it.
- No double dash "--" and no long dash. At most one colon in a sentence.
- Keep <b>...</b> on the key words; keep JSX valid: every tag you open you close, `{...}` expressions untouched (e.g. {C4}, {A('B2', ...)}, {chP}, {t(...)} calls inside text stay exactly as they are).
- Don't shorten a sentence that is already short. Aim for roughly a third shorter overall, mostly by cutting filler.

## Output
JSON: {"chapter": "<id>", "book": [{"old": "...", "new": "..."}, ...], "guide": [{"old": "...", "new": "..."}, ...]}
- Each "old" must be an exact substring of the file and occur EXACTLY ONCE in the whole file (base.src.html for "book", the guide file for "guide"). Make "old" a whole LbSay inner branch or a whole step, long enough to be unique.
- Before finishing, verify with a short Python script: load the file, check each old occurs exactly once, apply all replacements to a copy in memory, and check the count of '<b>' equals the count of '</b>' inside each new string. Report any failures and fix them.
- Finally reply with a short summary: how many replacements, the before/after character count of the replaced text, and 2 example before/after pairs.
