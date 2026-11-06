# Rewrite without the double dash "--"

The Piano Butler app (a piano lesson app for children aged about 8 to adults, English + Korean) used " -- " as a dash
in its text. The teacher who owns it asked: remove every "--" a reader sees, and rewrite the sentence with ordinary
punctuation instead. Your job: one JSON file of items in, one JSON file of replacements out.

## Input

A JSON array. Each item: `id`, `kind` (StringLiteral | JSXText | TemplateElement), `raw` (the EXACT source text of
that string as it stands in the JSX file, quotes included for a StringLiteral), `before` and `after` (the source just
around it on the same line, for context only -- often the other half of a t('English', '한국어') pair, or the pieces of a
string joined with +).

## Output

A JSON array with one object per input item, same order:
- `{"id": 12, "raw": "<the new raw text>"}` -- a drop-in replacement for the exact `raw` slice, or
- `{"id": 12, "skip": "why"}` -- only when the "--" is not prose (see "Leave alone").

Write it with the Write tool to the output path you were given. It must be valid JSON (escape backslashes and double
quotes inside JSON strings properly). Before writing, check your array has exactly as many entries as the input.

## How to rewrite

1. Replace each prose "--" with the punctuation that reads most naturally:
   - `:` when what follows explains, names, lists, gives the example or the result.
     "A semitone is a half step -- to the very next key." -> "A semitone is a half step: to the very next key."
   - `,` for a light pause or an apposition.
     "Play C, then C sharp -- a half step up." -> "Play C, then C sharp, a half step up." (or ": a half step up")
   - `.` (capitalise the next word in English) when what follows is a new thought or a new instruction.
     "Tap a key -- then listen." -> "Tap a key. Then listen."
   - A pair of dashes around an aside -> two commas, or parentheses.
     "The black keys -- two and three -- make houses." -> "The black keys, two and three, make houses."
   - A range written with a dash ("Grades 1 -- 4", "1700 -- 1750") -> "Grades 1 to 4", "1700 to 1750" (Korean: "1~4급", "1700~1750년" style, or "부터 ... 까지").
   - Two groups in a short label list ("Clara · Dog · Exit -- Front door · Grandma") -> separate the groups with " / ".
2. Never use an em dash, an en dash, a single hyphen or "—" / "–" as the replacement. Avoid semicolons (prefer a full stop).
3. No two colons in one sentence: if the sentence already has a colon, use a full stop or a comma instead.
4. Change NOTHING else. Same words, same spelling (British/Australian English), same HTML/JSX entities, same escapes
   (`\'`, `\n`, ` `...), same quote characters around a StringLiteral, same leading/trailing spaces and newlines.
   Only the dash and, where needed, the space before it and the capital letter after a new full stop.
5. A piece of a longer sentence (a string joined with + to other strings): keep it joinable. If the piece starts with
   " -- ", start it with the new punctuation and one space (": ", ", ", ". "). If it ends with " -- ", end it with the
   punctuation and one space. Look at `before`/`after` to see what it joins.
6. Korean: the same rules, Korean punctuation as the app already uses (`:`, `,`, `.`). Prefer `:` or `,` so you do not
   have to change verb endings; if you split with `.`, the part before must still end like a sentence (요/다 ending) --
   you may add the smallest ending needed, nothing more.
7. Read both languages of a t('...', '...') pair if you have them both: keep them parallel.
8. Keep it valid: a StringLiteral stays one valid JS string literal with the same quotes (an apostrophe inside a
   '...' string stays escaped as \'); a TemplateElement must not gain a backtick or "${"; a JSXText must not gain
   "{", "}", "<" or ">".

## Leave alone (skip)

- Music or counting notation where "--" means something (a held beat "1 2 3 --", "C -- -- D" as sounds), ASCII arrows
  ("-->"), code, CSS, URLs, data keys, regular expressions, and any "--" that is not a dash between words.
- If you are unsure, prefer rewriting prose; skip only real notation.

## Voice

Short, warm, clear sentences for a child and a parent; no new words, no new ideas, no rewording beyond the punctuation.
