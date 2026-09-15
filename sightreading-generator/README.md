# Piano Butler — Sight-Reading Generator

A working prototype of the feature described in the build spec: a teacher
picks a grade, clicks **Generate**, and gets an original,
procedurally-generated sight-reading excerpt rendered as sheet music (PNG
preview + PDF download), with a **Regenerate** button and a **Save to
Mission Bank** button.

> **2026-09-03 correction:** an earlier version of this app also had a
> separate, manually-curated **Explorer Bank** library page. It was retired
> on 2026-09-03 — it ended up doing the same job as Mission Bank ("a place
> to save pieces"), just for manually-typed-in repertoire instead of
> generated excerpts, so the two were folded into one rather than keeping
> two overlapping "saved pieces" concepts (see the comment at the top of
> `server/server.js`). **This README described Explorer Bank as still live
> and flagged its admin form as unauthenticated — that's now stale; the
> feature and its routes don't exist in the current code at all**, so
> there's no unauthenticated admin endpoint to fix here.

This is greenfield — there was no existing Piano Butler codebase to build
into, so this is a self-contained Node/Express app implementing the full
spec end to end.

## What's implemented

- **Difficulty mapping** (`server/generator/gradeParams.js`): the grade →
  parameter table from the spec (bars, note values, keys, time signatures,
  hand-position span, max leap size/count), covering Preliminary through
  Grade 8, with Clara Music aliases (Spark/Ember/Flame/Blaze/Beacon).
- **Rule-based generation engine** (`server/generator/`):
  - `rhythm.js` fills each bar exactly from the grade's allowed note values.
  - `scales.js` builds a correctly-spelled diatonic scale for the chosen key
    so the melody walks by scale degree (always in-key).
  - `melody.js` is a constrained random walk: stepwise motion weighted
    higher than leaps, clamped to a hand-position window, with a per-grade
    cap on leaps larger than a 3rd.
  - `bass.js` generates a simple left-hand accompaniment (root/fifth or
    triad patterns) from the harmony implied by each bar's melody, using a
    steady quarter-note pulse so it never reads harder than the melody.
  - `index.js` assembles it all into a LilyPond (`.ly`) source string.
- **Compilation** (`server/lilypondCompiler.js`): LilyPond → PDF → PNG
  (via `pdftoppm`), matching the spec's step 7.
- **API** (`server/server.js`): `POST /api/generate-sightreading`, plus
  Mission Bank (`POST/GET/DELETE /api/mission-bank`, per-item `.pdf`/`.png`/
  `.mp3` fetch routes) — it stores the `.ly` source so items can be
  regenerated/edited later. No Explorer Bank routes exist (retired
  2026-09-03, see note above).
- **Frontend** (`client/public/`): a no-build-step vanilla HTML/CSS/JS app
  — `/sight-reading-generator` and `/mission-bank` pages.

This was tested end-to-end: every grade × hands × realm combination (27
total) generates and compiles without error, and output was visually
checked at several grades for correct clef/register/key/time-signature
rendering.

## Running it

Requires Node.js, and LilyPond + `pdftoppm` (from `poppler-utils`) on the
system PATH.

```bash
# one-time setup (Debian/Ubuntu example)
sudo apt-get install -y lilypond poppler-utils

npm install
npm start
```

Then open:
- http://localhost:3000/sight-reading-generator
- http://localhost:3000/mission-bank

Verified working 2026-09-10: `npm start`, then `GET /api/grades` and
`POST /api/generate-sightreading` both round-trip correctly and produce a
real rendered PNG under `server/output/` — this is a live, running app,
not just source that's never been exercised end to end.

## Grade difficulty reference (Preliminary–8)

This table is the live ground truth read directly out of
`server/generator/gradeParams.js` (AMEB-style grading, 2026-09-10). It's
meant to travel with the code into the main Piano Butler project once this
sight-reading review is finished, so a teacher can sanity-check the whole
ladder in one place without reading the source.

| Grade | Bars | Time signatures | Keys | Melodic span | Max leap | Hands |
|---|---|---|---|---|---|---|
| Preliminary | 4 | 4/4, 2/4 | C, G major | 5 scale degrees | 3rd (1 per excerpt) | progressive (RH/LH alternate by section) |
| Grade 1 | 4–6 | 4/4, 2/4, 3/4 | C, F, D, G, B♭ major | 6 scale degrees | 3rd (2 per excerpt) | alternating |
| Grade 2 | 4–8 | 4/4, 3/4, 2/4 | F, G, B♭, D, E♭ major | 7 scale degrees | 4th (3 per excerpt) | alternating |
| Grade 3 | 8 | 4/4, 3/4, 2/4 | C, G, E♭, A, B♭, D major | 7 scale degrees | 4th (3 per excerpt) | mixed (RH/LH swap mid-excerpt) |
| Grade 4 | 8 | 4/4, 3/4, 2/2, 6/8 | B♭, A♭, E, A, E♭, D, G, F major | 8 scale degrees | 5th (4 per excerpt) | together |
| Grade 5 | 7–15 | 4/4, 3/4, 2/4, 6/8, 9/8 | D, A, E♭, B♭ major; E minor; G major; F♯ minor; C♯ minor; G♯ minor; B♭ minor; D♭ major | 9 scale degrees | 6th (5 per excerpt) | together |
| Grade 6 | 12–20 | 4/4, 3/4, 2/2, 6/8 | G, A, B♭, F major; G, D minor | 10 scale degrees | 7th (6 per excerpt) | together |
| Grade 7 | 14–22 | 4/4, 2/2, 3/2, 3/4, 5/4, 2/4 | F, D, B♭, A major; A minor | 11 scale degrees | 7th (6 per excerpt) | together |
| Grade 8 | 15–24 | 3/4, 4/4, 2/4, 9/8 | D♭ major; B♭ minor; A♭ major; F minor; E♭, B♭, E, A, D major; B minor | 12 scale degrees | 8th (7 per excerpt) | together |

Companion visual version (color-coded ladder with per-grade "what's
confirmed vs. deferred" callouts) is published as a Claude Artifact —
ask whoever last worked on this file for the link, or regenerate it from
this same table if it's gone stale.

## Recent musicality improvements (2026-09-10 pass)

These were added on top of the original prototype engine described above,
all within each grade's already-calibrated rhythm/key/range vocabulary —
no new note values or techniques were introduced per grade, only smarter
choices among the ones already confirmed against the AMEB books:

- **Phrase-arc melodic contour** (`melody.js`): the right hand no longer
  picks up/down by a flat coin flip. Each generated line gets a randomized
  "arc peak" position (30–70% of the way through), and the up/down
  probability is biased toward that peak, producing a natural rise-then-
  fall shape instead of a random walk. Applies to every grade and every
  hands mode, since it lives in the shared `pickMove`/`generateMelody`
  path all of them call.
- **Functional harmony bias** (`bass.js`): `chooseChordRoot` now nudges
  toward real tonal motion — IV→V and V→I are given a small scoring bonus
  over other legal chord choices — without overriding a chord clearly
  implied by the bar's melody notes.
- **Half cadence** (`bass.js`): excerpts of 6+ bars get a soft "comma" —
  a bonus toward landing on V at the excerpt's phrase midpoint — distinct
  from the pre-existing hard-forced tonic landing on the final bar. Gives
  longer excerpts (mainly Grade 5+) an audible two-part phrase shape
  instead of one long unbroken line.
- **Beam-grouping fix** (`index.js`, `forceQuaverBeamPairs`): manual beam
  forcing (used for 2/4 and 3/4 time) was grouping by blind pairs-of-2,
  which mis-beamed runs of 4 sixteenth notes (split into two unrelated
  2-note beams) and triplets (only 2 of 3 notes beamed). Rewritten to
  group by beat offset and to leave triplets to LilyPond's own default
  auto-beaming inside `\tuplet 3/2 { ... }`. Purely a notation-rendering
  fix — no change to what notes/rhythms get generated.
- **"Style" dropdown removed from the UI** (not a musicality change, but
  related cleanup): the waltz/minuet/march/etc. presets are hidden from
  the Generator page for now since they weren't fleshed out enough to be
  worth the extra control. The backend (`opts.feel` in
  `generator/index.js`) still fully supports them, so a more detailed
  style picker can come back later without an API change.

## Notes / next steps for a teacher to review

- **Difficulty ranges are a starting point**, exactly as the spec says —
  tune `server/generator/gradeParams.js` after trying it with real
  students.
- The left-hand accompaniment logic is still fundamentally simple
  (I/IV/V root/fifth or broken patterns) — the 2026-09-10 pass above adds
  functional-harmony and half-cadence *tendencies* on top of that base,
  it doesn't rewrite the voicing/register logic itself. Still worth a
  pass by a piano teacher on voicing/register choices, especially at the
  higher grades where the left hand could reasonably do more (e.g. actual
  broken-chord figuration variety, occasional passing tones).
- Grades 5–8 are the newest and least classroom-tested part of the
  ladder — the parameter ranges above came from a book-calibration pass,
  but they haven't had the same amount of real-student mileage as
  Preliminary–4.
- Storage is flat JSON files on disk (`storage/mission-bank/`) — fine for
  a prototype; swap for a real database before multi-user production use.
  (`storage/explorer-bank/` still exists on disk as an empty leftover
  directory from before the 2026-09-03 retirement; nothing in the code
  reads or writes it, safe to delete.)
- No auth on `POST /api/mission-bank` or `DELETE /api/mission-bank/:id` —
  anyone who can reach the server can save or delete Mission Bank items.
  Add access control before deploying somewhere public.
- Out of scope for this pass, per the spec: MIDI playback, AI-based
  melody generation, difficulty auto-detection from student performance
  history.
- **Deployment**: this is a stateful Node/Express server that shells out
  to LilyPond + `pdftoppm` and writes files to local disk
  (`server/output/`, `storage/`) — it needs a real host with a
  persistent filesystem (or the storage/output paths pointed at object
  storage), not a static host. It won't run on something like GitHub
  Pages as-is.
