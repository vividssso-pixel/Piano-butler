# Phase 485 review brief: the first concept book, "Scales and keys"

## What this is
Piano Butler (drills.html) is a piano teacher's app (Sohyun, Sydney; lessons in English and Korean; ages about 8 to adult).
On 2026-10-17 she decided a new foundation (CLAUDE.md rule 16, in `/home/claude/pbtest/cb/CLAUDE.md` lines 468-485):
everything sits in five areas and 13 concepts; **each concept is taught whole, once** ("not one scale, then another: teach
the concept and apply it to all at once"), then practised in steps (First / Then / Further / Later) that differ by student.
Exams (AMEB first, then ABRSM) are laid over later. A Lesson Book becomes a short **concept book**: the rule, the whole map,
how to use the tools, a check. This is the FIRST concept book and the model for the other twelve, so it must be right.

The concept "Scales and keys" (area Pitch) gathers what chapters 16 (Scales: C, G, F major) and 19 (Key Signatures) teach
one key at a time. Fingering and playing are in another concept (Technique: Playing scales and chords), so this book only
points there.

## The book (8 A4 pages, English and Korean)
1 opener (the rule; the keyboard clock and the circle of fifths; contents; "by the end, you can") · 2 The major scale ·
3 Any key (D major worked; all 13 major scales in a table, circle order) · 4 Key signatures (all seven sharps and flats,
treble and bass, the key under each sign) · 5 The circle of fifths · 6 Minor and other scales (six shapes on the same
clock: C major; A natural, harmonic, melodic minor; C pentatonic; chromatic) · 7 Practise in steps (the ladder, each step's
keys and the Toolbox tools to use) · 8 My five checks.
On screen the same pages are one lesson (opener + 7 steps), each with a working pad or an existing Toolbox tool beside its
picture (opener: "One key, all at once"; p2 the C major pad; p3 Build a major scale; p4 Order of sharps; p5 Circle of
fifths; p6 "Other shapes, the same clock"; p8 the five checks, saved). The Toolbox's "Scales and keys" group shows a card
"The concept book" (Open / Print). Workbook and drill for the concept come AFTER she approves this model (not in scope).

## Files
- Source of the new code: `/home/claude/pbtest/cb/cbscales.jsx`; the patch: `/home/claude/pbtest/cb/patch485.py`
  (also changes the shared KeyRing clock: `o.pat` shapes; LbPage `head`; the print route; the Toolbox card).
- Built page: `/home/claude/pbtest/a3/drills.t485.html` (full source after the patch: `/home/claude/pbtest/cb/t485.src.html`).
- Screenshots: `/home/claude/pbtest/cb/shots/` (cb-en-N.png, cb-ko-N.png = print pages 1-8; step-en-N.png / step-ko-N.png =
  screen steps on a 390 px phone; pad-*.png; toolbox-card-*.png).
- The house rules for books: `/home/claude/pbtest/cb/CLAUDE.md` lines 256-485 (rules 1-16: Lesson Book spine, nothing twice,
  set tasks, fill the page, balance and reading, words and cast, the Victorian look: navy + coral + green only, dictionary
  style, etc.). Earlier finished books to compare with: chapter 16 (`?book=lesson&ch=scales`) and 19 (`?book=lesson&ch=key-signatures`).
- A browser harness: `const { start } = require('/home/claude/pbtest/kit/contentharness'); const H = await start('drills.t485.html');
  const p = await H.open({ path: '?book=concept&ch=p-scales&lang=ko', w: 900, h: 1300 });` returns a Playwright page
  (`p._errs` = page errors; `await p.context().close(); await H.close();`). Screen version: `path: '?teacher=1&tool=cb-p-scales'`
  with `w: 390, h: 860, lang: 'ko', dsf: 1.5`. Toolbox: `?teacher=1&view=toolbox`. Run node scripts from `/home/claude/pbtest/kit`
  or with absolute requires. Put any scripts you write in your own folder under `/home/claude/pbtest/cb/review/r1/`.

## How to report
Be strict and concrete. Do not edit project files. Write your report to the file named in your task, with findings numbered
B1.. (blockers: wrong, broken, misleading), M1.. (must fix), m1.. (minor). For each: where (page, element, line), what is
wrong, and the exact fix you propose (exact replacement text for wording; Korean in Korean). Then reply with a one-paragraph
summary and the counts.
