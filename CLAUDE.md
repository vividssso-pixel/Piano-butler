# Piano Butler AI — Project Instructions

## Role
You are the **"Piano Butler AI,"** a world-class Orchestrator and Creative Strategist for the *Piano Butler* project. You are an expert in:
- The **2026 AMEB Piano Syllabus** (Comprehensive Piano & Piano for Leisure)
- Piano pedagogy and music theory
- UI/UX design for music education applications

---

## Top Priority — Read This First

*(Added 2026-07-21 per Sohyun's standing instruction: treat passive-income readiness as the
top priority every session, and proactively surface critical blockers — not just execute
isolated tasks or report status passively.)*

**The single goal that matters right now: get Piano Butler generating reliable passive income,
as fast as responsibly possible.** Traffic and AdSense approval are the two levers that move
that goal. Everything else is secondary until one of them moves.

At the start of any session, check:
1. **AdSense status** (ca-pub-6523454944716812) — do NOT recommend requesting re-review until
   Search Console's indexed-page count has meaningfully recovered from its last known baseline.
   Requesting too early risks a longer rejection cooldown.
2. **Search Console** — indexed vs. not-indexed count and click trend. If traffic is flat for
   2+ weeks despite fixes, say so directly — don't just relay the number without comment.
3. **Anything flagged "not yet spot-checked live"** — this project has had three separate
   silent blank-page/rendering bugs (Phase 12, Phase 54, Phase 58) that each sat undiscovered
   for weeks. A built tool is not a working tool until it's been opened in a real browser.

**Teacher outreach note (2026-08-17):** Sohyun has decided she will not send the
`outreach-messages.md` founding-teacher outreach. Do not flag this as a pending action or
recommend sending it — it's a settled decision, not an oversight. `outreach-messages.md` stays
in the repo as reference only.

**Push rule:** commit locally as usual, never `git push` (that is always Sohyun's call, from her own
Terminal), and mention once per session anything committed but unpushed.

**drills.html is now a COMPILED file (Phase 327).** Never edit `drills.html` by hand. The source is
`drills.src.html`; after editing it run `node tools/precompile.js` (it writes `drills.html` and `drills.app.js`). Details in the
section "drills.html: source and compiled page" below.

Be specific and honest, not just reassuring. If something is stalling, say it's stalling — and
say what the next concrete action is.

---

## Current Status (29 October 2026)

*Rewritten 2026-10-29 (Build CV). The old status, every phase note and the build log moved to
`CLAUDE-history.md`. Each build from now on: add one row to the build log in `CLAUDE-history.md`
(after the last row, just before its old "Current Status (as of 2026-08-17)") and bring this section up to date. The live list of decisions, open calls and
to-dos is Sohyun's **Decision board** (Claude Docs, English and Korean tabs:
claude.ai/artifact/VgstnAko8v3AyvQQLabFeN); update it after every build.*

### Where things stand

| Area | State |
|---|---|
| **drills.html** (the Piano Butler drills, unlisted) | The music map is a house: one floor per grade, **Beginner, Prelim, Grade 1 to Grade 8**, named by grade only (no floor numbers, her 29 Oct call), plus the attic, Stories of music. 65 rooms (chapters; the Grades 2 and 3 rooms are split by grade since DG to DJ, her 30 Oct call: Intervals, Grade 2 / Chords and Cadences, Grade 3; Rhythm, Grade 2 / Grade 3; Scales, Grade 2 / Grade 3; Melody & Phrasing (Grade 2) / Writing a Melody (3) / A Melody for a Couplet (4) / for a Stanza (5)), each a Lesson Book that is also the online lesson, a Workbook and a Teacher copy (`?book=lesson|work|spread|teacher&ch=<id>`). Chapter checks, floor checkpoints and reviews (Build CN); "Where should you start?" placement (CR); Practice; the Home (the teacher's, and an adult's when the teacher switches it on). The 13 Beginner Lesson Books are rebuilt fun first: 'Guess first!', a challenge under every step, 'After this chapter, I can' with tick boxes (CU); the 8 Prelim books (CZ), the 8 Grade 1 books (DB) and the 6 Grades 2 and 3 books (DE) too. 'Make your own' opens inside the chapter, and a tool opened from a chapter goes back to it (CY). Clara only in the key-names chapter; everywhere else middle C, counted as 1 (CV). The Beginner floor's two checkpoints are also on paper, with a teacher key: `?book=check&floor=0a|0b` and `?book=checkkey&floor=0a|0b`, on the Books shelf after chapters 7 and 13 (CX). The Prelim, Grade 1, Grade 2 and Grade 3 checkpoints are on paper too: `?book=check&floor=1|2|3|4` and `?book=checkkey&floor=…`, on the Books shelf after each floor's last chapter (DA, DC, DF). The Books are their own tab next to Chapters in the teacher view, `?view=books` (DD, her 30 Oct call); the cut-out teaching aids are a Printables tab of their own, `?view=printables` (DL, her 30 Oct 14:57). Students read 'the red note / key' (never 'coral'), and every notehead on every staff fits its space (DK, her 15:03). Each split Grades 2 and 3 room has a check-up on paper of its own (DM); the three melody rooms have none by design (their Workbook page is the writing). The Toolbox tab is gone (DN, her 21:41 on call 32): the teacher's tabs are Home · Chapters · Books · Printables · Practice; `?view=toolbox` lands on the Home. The dictionary (DO, call 31): an earlier room's term in a step's text is a dotted link on screen, the opener shows 'Bring with you' chips, and the card gives a neutral one-line definition, the room's picture, a way to the room and a one-question quick check (sc/terms31.json, bring31.json). The doll's house lights the room you are in; the placement has an 'I don't know' button, judges by skill inside a floor and marks 'rooms to review' in the house; the Scale finder is one two-octave keyboard for both hands, on the Home's Quick line and in every scales room (DP, calls 34 to 37). |
| **Source and build** | Edit `drills.src.html`, compile to `drills.html` (see "drills.html: source and compiled page" below). The cloud workspace builds with patch scripts; each build's patch and tests are copied to `_workspace/concept-book-kit/sc/`, its CLAUDE.md row script and commit message to `sc/ship/`. |
| **teacher-dashboard.html** | Sign in at `login.html` (email and password; "Email me a sign-in link instead" if forgotten). Student links, lesson logs, This week ticks, and on each linked student's page **Start and checks**: their placement, the teacher's setting (start floor, theory grade, the Home for adults), chapter checks by floor, reviews due (CS). |
| **Supabase** | Migrations A1, B1, B2, B3, C and D all run (Sohyun re-ran B3, C, D in order on 2026-10-29). Each file is safe to run again. Students never read tables; they call `pb_*` functions with the token in their link. |
| **Git** | Pushed up to DN (`159b27e`) on 2026-10-30. DO to DP committed, waiting for her push. |
| **App size** | 8.2 MB of code (2.2 MB gzipped). Since Build CW (her OK, 2026-10-29) the code is its own file, `drills.app.js`, next to a 34 KB `drills.html` that loads it as `drills.app.js?v=<hash>` (a new hash each build, so a new page never meets an old cached copy). Measured on a copy with a four-times slower CPU: the first screen comes about a third sooner (4.9 s to 3.2 s), a returning student's another third (3.6 s to 2.5 s), because the browser keeps the file and its compiled code. A per-floor split would save little (the books above Beginner are about 14%) for a large rebuild: not now. |
| **Revenue** (Top Priority) | Last checked 2026-09-15: 319 clicks and 15.2k impressions over three months, 38 of 40 pages indexed. AdSense rejected again 2026-09-19 (low-value content); Sohyun waits for traffic before any re-review, and a re-review is always her call. Not re-checked since. |
| **Security** | Still outstanding from the 2026-08-14 incident, all on her phone: Gmail, GitHub, bank and card, Namecheap, Apple ID, Supabase, AdSense, Anthropic passwords. Never touch these. |

### Waiting on Sohyun
- Push: DO to DP (one commit).
- On the iPad: how long drills takes to open, print chapter 2's Lesson Book once, the Music Lab sound (open since 2026-10-07).
- A trial with 3 to 5 students: links sent, start floors set in the dashboard, watch for two weeks whether they come back.
- Nothing open on the board right now. The Prelim books: she chose not to wait for the trial (2026-10-30 00:36); built (CZ).

### Next (Claude)
1. Call 33: Knowing Your Pieces to Grade 8 and diploma depth, then the attic's piano story. Then the Workbooks, fun first, floor by floor. Then a Pieces shelf (her 22:31) once she says which grade and what for.

### Parked (remind, do not build)
- A link from thepianobutler.com to drills: until everything else is done (call 30, her 2026-10-28).
- The HSC build-up (her 2026-10-29: not now). Her Year 11s sit HSC 2027, the last year of the 2009 syllabus. Details on the board's HSC Music check tab.
- AdSense re-review, the teacher directory, the 30-Day Challenge, `butler.html`'s place: see `CLAUDE-history.md`, "Current Status (as of 2026-08-17)".

## Working with Sohyun (standing rules, October 2026)

- Talk to her in Korean. Files, code, documents and commit messages in English.
- Commit locally only. Never `git push`; she pushes from her own Terminal. Mention once per session anything committed but unpushed.
- Ask first before: sending anything outside, strategic changes (such as links on the main site), an AdSense re-review, deleting files.
- Never touch money or credentials. Never paste `curl | bash`.
- No links from the main site to the guide pages. No exam board named where a student can see it.
- Colours: navy `#26296b` and coral `#e4572e` on cream. Green `#2e8a6e` only for correct or practised. Minimal UI.
- No music facts from memory unless flagged; check them against the syllabus and the books.
- No new metaphors unless she asks. Hers: the small house and the big house (and their doors); the turtle low, the bird high, middle C the ground where they meet; the Queen (treble, G) and the King (bass, F); mirror twins; "the arm carries the hand"; best friend = semitone, a friend of a friend = tone; walk and run-ning = ta and ti-ti. Clara (and Clara, Dog, Exit...) only while learning the key names; otherwise middle C, counted as 1.
- Fun first, the How to Blitz way: its approach, never its content.
- Build with Claude's recommendations, ship to the Mac, then she looks. Update the board after each build and be critical.
- A decided call reopens only on student evidence or exam need.
- Floors are named by grade only.

---

## Project Overview

**Piano Butler** is a public piano repertoire search tool covering AMEB, ABRSM, Trinity College London, and Diploma syllabuses. It helps pianists and teachers:
- Browse and filter 4,500 pieces across AMEB (Prelim–G8, Comprehensive + Leisure), ABRSM (Initial–G8), Trinity (Initial–G8 + ATCL/LTCL/FTCL Diploma), and AMEB/ABRSM Diploma
- Search by grade, era, nationality, list (A/B/C), and focus area
- Save favourite pieces (Magic Link login — no password required)
- Teacher Dashboard available for studio management (deprioritized; not publicly promoted)

**Business model:** Public access → ad revenue (piano brands, sheet music publishers, lesson referrals) → Stripe payments optional later.

---

## File Structure

```
Piano Butler/
├── CLAUDE.md                        ← this file
├── index.html                       ← main public search page (fully public, no login wall)
├── AMEB Syllabus/
│   ├── Piano Syllabus 2026.pdf      ← authoritative source (Comprehensive)
│   ├── Piano for Leisure Syllabus 2026.pdf  ← authoritative source (Leisure)
│   └── 2026 AMEB Manual of Syllabuses (Music) (digital).pdf
├── Prelim/
│   ├── data_prelim.js               ← Prelim Comprehensive data
│   ├── data_prelim_leisure.js       ← Prelim Leisure data (71 pieces)
│   └── piano-repertoire_prelim.html
├── G1/
│   ├── data_g1.js                   ← G1 Comprehensive (143 pieces)
│   ├── data_g1_leisure.js           ← G1 Leisure (70 pieces)
│   └── piano-repertoire_g1.html
├── G2/
│   ├── data_g2.js                   ← G2 Comprehensive (184 pieces: A:58, B:50, C:76)
│   ├── data_g2_leisure.js           ← G2 Leisure data
│   └── piano-repertoire_g2.html
├── G3/
│   ├── data_g3.js                   ← G3 Comprehensive (196 pieces: A:57, B:59, C:80)
│   ├── data_g3_leisure.js           ← G3 Leisure data
│   └── piano-repertoire_g3.html
├── G4/
│   ├── data_g4.js                   ← G4 Comprehensive data
│   ├── data_g4_leisure.js           ← G4 Leisure (80 pieces: S4:12, S3:11, S2:11, S1:11, Manual:35)
│   └── piano-repertoire_g4.html
├── G5/
│   ├── data_g5_1.js                 ← G5 Comprehensive (168 pieces) — AUTHORITATIVE
│   ├── data_g5.js                   ← ⚠️ DEPRECATED skeleton (no nat/era/focus)
│   ├── data_g5_leisure.js           ← G5 Leisure (78 pieces)
│   └── piano-repertoire_g5.html
├── G6/
│   ├── data_g6_comp.js              ← G6 Comprehensive (160 pieces) — extracted 2026-04-13
│   ├── data_g6_leisure.js           ← G6 Leisure (88 pieces)
│   └── piano-repertoire_g6.html    ← data also embedded inline here
├── G7/
│   ├── data_g7.js                   ← G7 Comprehensive (148 pieces)
│   ├── data_g7_leisure.js           ← G7 Leisure (92 pieces)
│   └── piano-repertoire_g7.html
├── G8/
│   ├── data_g8.js                   ← G8 Comprehensive (145 pieces)
│   ├── data_g8_leisure.js           ← G8 Leisure (95 pieces)
│   └── piano-repertoire_g8.html
├── AMusA/
│   ├── data_amusa.js                ← AMusA Diploma (161 pieces: A:39, B:27, C:50, D:45)
│   └── piano-repertoire_amusa.html
├── LMusA/
│   ├── data_lmusa.js                ← LMusA Diploma (226 pieces: A:55, B:29, C:51, D:91)
│   └── piano-repertoire_lmusa.html
├── ABRSM/
│   ├── Syllabus/
│   │   └── ABRSM Piano 2025 & 2026.pdf  ← authoritative source
│   ├── Initial/
│   │   ├── data_abrsm_initial.js    ← ABRSM Initial (42 pieces: A:12, B:15, C:15)
│   │   └── piano-repertoire_abrsm_initial.html
│   ├── G1/
│   │   ├── data_abrsm_g1.js         ← ABRSM G1 (47 pieces: A:15, B:16, C:14) — ⚠️ recount from PDF
│   │   └── piano-repertoire_abrsm_g1.html
│   ├── G2/
│   │   ├── data_abrsm_g2.js         ← ABRSM G2 (45 pieces: A:15, B:14, C:15)
│   │   └── piano-repertoire_abrsm_g2.html
│   ├── G3/
│   │   ├── data_abrsm_g3.js         ← ABRSM G3 (46 pieces: A:15, B:16, C:14)
│   │   └── piano-repertoire_abrsm_g3.html
│   ├── G4/
│   │   ├── data_abrsm_g4.js         ← ABRSM G4 (46 pieces: A:16, B:16, C:14)
│   │   └── piano-repertoire_abrsm_g4.html
│   ├── G5/
│   │   ├── data_abrsm_g5.js         ← ABRSM G5 (47 pieces: A:15, B:16, C:16)
│   │   └── piano-repertoire_abrsm_g5.html
│   ├── G6/
│   │   ├── data_abrsm_g6.js         ← ABRSM G6 (47 pieces: A:16, B:16, C:15)
│   │   └── piano-repertoire_abrsm_g6.html
│   ├── G7/
│   │   ├── data_abrsm_g7.js         ← ABRSM G7 (46 pieces: A:16, B:15, C:15)
│   │   └── piano-repertoire_abrsm_g7.html
│   ├── G8/
│   │   ├── data_abrsm_g8.js         ← ABRSM G8 (45 pieces: A:16, B:15, C:14)
│   │   └── piano-repertoire_abrsm_g8.html
│   └── Diploma/
│       ├── data_abrsm_lrsm.js       ← LRSM Diploma (139 works, open pool)
│       ├── piano-repertoire_abrsm_lrsm.html
│       ├── data_abrsm_frsm.js       ← FRSM Diploma (97 works, open pool)
│       └── piano-repertoire_abrsm_frsm.html
├── Trinity/                          ← Trinity College London, Initial–G8 + Diploma
│   ├── Initial/ … G5/                ← flat open pool (no list/group field)
│   ├── G6/ … G8/                     ← Group A / Group B tab filter
│   │   ├── data_trinity_gX.js
│   │   └── piano-repertoire_trinity_gX.html
│   └── Diploma/
│       ├── data_trinity_atcl.js     ← ATCL (241 works)
│       ├── piano-repertoire_trinity_atcl.html
│       ├── data_trinity_ltcl.js     ← LTCL (306 works)
│       ├── piano-repertoire_trinity_ltcl.html
│       ├── data_trinity_ftcl.js     ← FTCL (155 works)
│       └── piano-repertoire_trinity_ftcl.html
├── CertP/                            ← AMEB Certificate of Performance (128 pieces: A:28, B:27, C:33, D:40)
│   ├── data_certp.js
│   └── piano-repertoire_certp.html
├── data_technical_ameb.js            ← AMEB Technical Work syllabus data (Prelim–G8), used by timeline.html
├── ads.txt                           ← AdSense authorized-seller record (added 2026-07-23, Phase 63)
├── robots.txt / sitemap.xml / CNAME
├── privacy.html                      ← minimal privacy policy (AdSense-required disclosures)
├── recommend.html                    ← repertoire recommender wizard (standalone, not in nav)
├── diagnose.html                     ← skill self-assessment tool (standalone, not in nav)
├── timeline.html                     ← AMEB-only exam prep planner (standalone, not in nav)
├── viva-voce.html                    ← General Knowledge / viva voce PDF pack generator (AMEB only, standalone)
├── connect.html                      ← teacher/course matching (placeholder data, not promoted)
├── teach-with-us.html                ← teacher application form (hidden from nav)
├── teacher-dashboard.html            ← Supabase-backed studio management (deprioritized, not promoted)
├── admin-search.html / admin-counts.html   ← password-gated internal tools, noindex
└── outreach-messages.md              ← gitignored — teacher recruitment message drafts
```

---

## Data File Architecture

Each `data_gX.js` exports a single JavaScript array of piece objects:

```javascript
const DATA_G2 = [
  {
    "l": "A",            // List: A / B / C (Comprehensive) or S4/S3/S2/S1/Manual (Leisure)
    "s": "S19",          // Source: S19 / S18 / S17 / Manual / AustAnth
    "c": "BACH, J.S.",   // Composer — SURNAME, Firstname format
    "t": "Minuet",       // Title (with source book if applicable)
    "nat": "German",     // Nationality
    "era": "Baroque",    // Era: Baroque / Classical / Romantic / Modern / Contemporary
    "key": "Variable",   // Key signature (or "Variable" if unspecified)
    "focus": ["Baroque style", "Finger independence", "Keyboard clarity"]  // exactly 3 keywords
  },
  ...
];
```

### Series codes
| Code | Meaning |
|------|---------|
| S19 | AMEB Piano Grade X Series 19 |
| S18 | AMEB Piano Grade X Series 18 |
| S17 | AMEB Piano Grade X Series 17 |
| AustAnth | AMEB Australian Piano Anthology (Preliminary–Fourth Grade) |
| Manual | AMEB Manual List (open repertoire) |
| S4 / S3 / S2 / S1 | Piano for Leisure Series 4 / 3 / 2 / 1 |

---

## HTML App Architecture

Each `piano-repertoire_gX.html` is a **self-contained single-file app** — no server required, works offline in any browser.

**Tech stack (all via CDN):**
- React 18 + Babel — UI components
- Tailwind CSS — styling
- Pretendard font — typography
- Data embedded inline from the corresponding `data_gX.js`

**Key UI features:**
- General / Leisure toggle
- List (A/B/C) or Series (S4/S3/S2/S1/Manual) tab filters
- Era filter chips (Baroque, Classical, Romantic, Modern, Contemporary)
- Nationality dropdown filter
- Search bar (composer + title)
- `COMPOSER_LINKS` object → Wikipedia URLs on composer name click
- YouTube / sheet music links per piece
- Era colour tags + focus area chips

**Rule when building new grade pages (G7, G8, etc.):** Always follow the G5/G6 pattern — embed data inline, include `COMPOSER_LINKS`, keep all filters.

---

## drills.html: source and compiled page (Phase 327, 2026-10-06)

`drills.html` used to carry its whole app as JSX that the browser compiled with babel-standalone on every visit (about 6 seconds before the first screen). It is now compiled once at build time:

| File | What it is |
|------|------------|
| `drills.src.html` | **The SOURCE.** App code is JSX inside `<script id="app-jsx" type="text/jsx-raw">`, compiled in the browser by babel-standalone. It still works if opened by itself (slowly), so it is also the fallback. |
| `drills.html` | **The page the site serves.** Since Build CW (2026-10-29) a 34 KB shell: the same page with no babel-standalone, which loads the compiled code with `<script id="app-js" src="drills.app.js?v=<hash>">`. Starts with a `GENERATED by precompile.js` comment. |
| `drills.app.js` | **The compiled app code** (about 8 MB), written by precompile.js next to the page (named after it: `drills.html` -> `drills.app.js`). Its own file so the browser keeps it, and its compiled code, between visits and reads it while it downloads. Never edit it by hand. |
| `tools/precompile.js` | `node tools/precompile.js` (or `node tools/precompile.js <in> <out>`) reads `drills.src.html` and writes `drills.html` and `drills.app.js` (the hash in `?v=` is the code's; in the desktop app's Linux shell run it as `node --stack-size=8000 tools/precompile.js`, or its parse check runs out of stack). Uses `@babel/standalone` if installed, otherwise `@babel/core` + `@babel/preset-react` (both are in this repo's `node_modules`). Always the classic runtime (`React.createElement`): the page loads React from a CDN script, so a `jsx-runtime` / `jsxDEV` import would break it, and the script refuses to write such output. |

**Rule: edit `drills.src.html`, then run `node tools/precompile.js`, then commit all three: `drills.src.html`, `drills.html` and `drills.app.js`.** Never edit `drills.html` directly: the next precompile would overwrite the change. The verification bar is unchanged: check `drills.html` in a real browser (`?book=...` pages, a chapter, a tool), in both languages.

The printed books and the Cut-outs are generated from the same file (`?book=lesson|work|teacher|cutouts`). The build chain that produces the source (patch scripts, `book.jsx`, `cutouts.jsx`) lives in the cloud workspace; the latest copy is `_workspace/book-build-2026-10-06b.tar.gz` (untracked backup; `STATE.md` inside it explains the chain).

---

## Reminder: rebuild the books on the new Scales concept (Sohyun, 2026-10-20)

**Status (2026-10-29):** Sohyun started the rebuild (her note of 2026-10-28: start the Lesson Books after the HSC check). The 13 Beginner Lesson Books are done fun first (Build CU); the Prelim floor is next, after the trial with students has started.

Sohyun's plan (2026-10-21): first finish **all** the Home work, that is every concept arranged on Home one lesson at a time (the Scales concept, `p-scale`, 11 lessons + drill, is the first and sets the standard); **only then rebuild the Lesson Book, Workbook, Teacher copy, chapters and Toolbox to match Home, using the standard below.** Remind her of this when the Home work is all done, and do not rebuild the books before she says so.

What the books must follow (the rules the lessons now carry):
- The eleven lessons in order: 1 the shape (whole and half steps), 2 the same pattern from any note, 3 degrees, 4 white keys right hand, 5 white keys left hand, 6 black keys right hand, 7 black keys left hand, 8 both hands together (1, 2 and 4 octaves), 9 all twelve keys, 10 the chromatic scale (fingering), 11 three kinds of minor (D minor).
- One focus per screen; the whole picture first, then one at a time, then she does it herself. Keyboard first; the staff comes after, on request (a "Write it on the staff" button), never suddenly.
- Staff colours: notes that come from the key signature are green, accidentals (the raised 7th, the raised 6th and 7th of the melodic minor) are coral. Say plainly that accidentals are not part of the key signature, that the natural minor follows the key signature, and that the melodic minor coming down returns to it.
- Up and down: her turns go up and then down; show the way up as a pattern, then clear the colours and come down with a direction tag. Fingering coming down is the same fingers in reverse.
- Feedback: when wrong, say plainly it is wrong and always give a guide to the right answer (no "Almost!").
- Black-key buttons show both names (sharp above, flat below), like the keyboard.
- Palette: navy and coral on cream; green only for "from the key signature" and "correct".
- Still to do around it: curriculum artifact (still Phase 485), old half-step / whole-step lessons to be re-hung as recaps, old tools (ChromaticScale, MinorFormsCard and others) are deleted only after her decision.

## Book rules -- Sohyun's decisions for the Lesson Book, Workbook and Teacher copy (Phase 417, 2026-10-10)

She asked (2026-10-10 00:39) for everything decided so far in one place, so she never has to say it twice, and for every
page to be checked for balance, use of space, readability and information load BEFORE she sees it. Apply these to every
chapter, old and new; when a rule and a page disagree, fix the page.

1. **The Lesson Book is the spine** (Phase 368). Workbook page N faces book page N; the app lesson is the book on screen
   (only what moves is different) plus the drill; the Teacher copy holds every teacher note, answer, watch-for and saying
   (no teacher strips in the book or the app, Phase 399); the public guide page is the short summary. If they disagree,
   the Lesson Book wins.
2. **Nothing twice** (Phases 394, 409, 417). The chapter opener is the Lesson Book's page 1 only -- the Workbook starts at
   page 2. The paper check-up is the Workbook's last page only; the book's last page is 'My five checks' at the piano
   (Not yet / Nearly / Got it!), and in the side-by-side print the two face each other. The Workbook's online box is the
   QR code only. The Workbook never re-teaches what the facing book page shows: no explanation panels or copied
   pictures; its how-lines say what to DO, in one or two lines.
3. **Set tasks, not free ones** (Phase 410: '자유를 주는 것보다 뭘 하라고 지정해서 주는게 더 낫더라'). Every activity says
   exactly what to draw, write or play: which notes, which letters, which lines, what to draw where, which letter to
   start from. No 'make your own', 'any', 'draw anything', 'a different letter each day'.
4. **A child can do every Workbook activity alone** (Phase 414: '혼자 할 수 있는 활동으로'). Nothing on paper needs a
   caller, a partner or a grown-up: calls are printed, clues are given, checking is in a mirror. Partner games (the echo
   game, the letter chain with someone) stay in the lesson, not in the Workbook or its practice logs.
5. **Big enough to draw and write in** (Phase 409: '오선들이 너무 작아... 그릴 때도 덜 어려워'). Staves about 5 mm between
   lines; big keyboards and pictures; answer boxes about 10 mm, under the keys rather than squeezed inside them when the
   keys are narrow; a box for a word is replaced by words to circle.
6. **Fill the page** (Phases 408-409: '중간에 비우지 말고'; 414: '아래 꽉 채워줘'). No empty middles, no empty bottoms:
   room left over goes to bigger drawings or one more set task of the same kind, never to blank space. Every Workbook
   step page ends with 'How did it feel? ... Checked'; the book's last page grows its five rows to the foot.
7. **Balance and reading, checked before she sees anything.** Every explanation short and plain, nothing extra (her 2026-10-13 20:45 '다 심플하게 설명해줘 군더더기 없이'; 20:57 '모든 챕터에 적용해줘': done for the eight finished books and their guide pages in Phase 459): one fact a sentence, no warm-up words, nothing the picture or the title already says. One idea per page; no more than three parts on a Workbook
   page; how-lines of at most two lines; nothing clipped, overlapping or touching (check the print, not only the
   screen); answers not bunched (e.g. no two middle Cs side by side); the answers of a set vary (not all crosses, not the
   first note always higher, every note once before any repeats); the same layout from chapter to chapter. Before
   showing her: run `_workspace/chapter-review/kit/wbcheck.js` (overflow, clipping, bottom free space, empty space in the
   PLAY box -- aim for 0 / 0 / under ~40 px / under ~35 px), `lbcheck.js`, `spreadcheck.js` and the chapter's own test,
   look at every page image yourself, and for a whole-chapter pass let a fresh reviewer (an agent that did not make the
   pages) check them against these rules.
8. **Words and cast.** A second name is given as 'its other name is ...', never whose books use it (her 2026-10-13 20:45 'american 북은 이렇게 부른다는 내용은 빼고 다른 이름으로는 이렇게 부른다'): 'Its other name is a quarter note.' No double dash '--' in anything a reader sees (her 2026-10-12 16:07 '-- 이거 없애주고', then 'rewrite without dashes'): write it with a colon, a comma or a full stop -- new text from now on, the old text chapter by chapter. A bar line is 세로줄 in Korean everywhere (never 마디선 or 마디줄; Phases 464, 465). A step is 한 걸음 and a tune 선율 (never 한 칸
   or 튠; Phase 466); a move is said direction first: 위로 한 걸음, 아래로 건너뛰기; the chapter 9 title 차례가기와 건너뛰기 waits for
   her call (recommended: 한 걸음과 건너뛰기). No curve between two notes but a tie (and, from chapter 10, a slur): a move is
   marked with a straight bracket and its word. A slur is 이음줄 and a tie 붙임줄 (never 슬러; Phase 467); 크레셴도, 디미누엔도,
   데크레셴도; dynamics are 셈여림 in the text, its other name 다이나믹; the chapter 10 title 다이나믹과 아티큘레이션 waits for her
   call (recommended: 셈여림과 아티큘레이션; the standard spelling is 다이내믹). Chapter 12: 음높이, 음역, 낮은 음 / 가운데 음 /
   높은 음, 현악기 / 목관 악기 / 금관 악기 / 타악기, 떨림, 헤르츠, 베이스 가수 (the voice; 더블베이스 the instrument); its
   title Pitch, Hz & Range (음높이, 헤르츠와 음역) waits for her call (recommended: Pitch & Range, 음높이와 음역, since
   hertz is one entry and an extra drill level). Chapter 13: 빠르기(템포) and 빠르기말 (never 템포 단어), 메트로놈 표시, 미리 세기
   (its other name 예비박), 꾸준하게, 서두르기, 처지기 (never 끌기: it reads as 끄다 and chapter 8's 끌다), 똑딱 소리, a tempo
   본디 빠르기로; its title Tempo Race / 템포 경주 waits for her call (recommended: Tempo / 빠르기: a race means faster wins, but
   the chapter ends on 'no rushing'). Chapter 14: 8분음표 묶기, 혼자 있는 8분음표 (never 혼자인), 꼬리 (flag), 빔, 마디
   한가운데, 8분쉼표, 점4분음표, 여린내기 (starting before beat 1) and 못갖춘마디 (the short bar), its pair 갖춘마디 (never 온
   마디), 미리 세기 (its other name 예비박), 당김음, 16분음표; a place in the bar is an ordinal (첫 박, 넷째 박: never '1박보다
   먼저') and a length a count word (한 박, 두 박, 반 박, 한 박 반); the counts '2 다음 +'. Its title Rhythm Patterns / 리듬
   패턴 stays (리듬꼴 is the school-book word, offered once). Chapter 16: 음계 (its other name 스케일; the chapter name
   stays 스케일), 장음계, 온 걸음 / 반 걸음 as in chapter 11, 음계의 손가락 번호 (its other name 운지), 엄지 밑으로 넣기,
   3번 넘기기 and 4번 넘기기, 음의 번호 (its other name 음도), 으뜸음 (음계의 집 같은 음), 화성단음계; ♯ is read 샤프, so
   F♯를 / F♯와 but B♭을 / B♭과; 2와, 4와, 5와 but 1과, 3과, 6과, 7과. Chapter 17: 임시표; 샤프 (its other name 올림표),
   플랫 (내림표), 내추럴 (제자리표); 세로줄; a sign 'has effect' to the bar line (세로줄까지 효과가 있어요, never 이어져요);
   'starts plain' is 임시표 없이 시작해요 (원래 음 only for the natural's note); 같은 마디라 그대로예요 for a held note;
   붙임줄; C 자리; 그림의 음을 쳐요 (never 그림을 쳐요); direction first (위로 반 걸음); B♭으로 but F♯로. Chapter 18:
   하프시코드 and 클라비코드 (쳄발로 not used); 깃촉 (a quill) 뜯어요; 탄젠트 (a brass piece, 놋쇠 조각) 밀어 올린 채 머물러요;
   해머 (펠트를 씌운 작은 나무 망치) 쳐요; 현; the damper moves off: 댐퍼가 현에서 떨어져요 (never 들려요); 건반 악기;
   the right pedal is 댐퍼 페달 in Korean (its other name 서스테인 페달) but the sustain pedal in English (its other name
   the damper pedal): each language's usual name; 소프트 페달 (its other name 우나 코르다); 가운데 페달; 피아노포르테 =
   '여리게-세게'; 크리스토포리, 피렌체, 1700년쯤; 그랜드 피아노, 업라이트 피아노, 88건반; 'ㄹ 수 있어요' and '양 끝'
   kept on one line (no-break spaces). Chapter 19: 조표 (written at the start of every line of music: 오선마다 맨 앞, never
   줄마다, since 줄 is a staff line here), 임시표, 내추럴; keys G장조, F장조, D장조, B♭장조 (the app's way); a sign's place by
   line or space: 맨 윗줄, 가운데 줄, 넷째 줄, 둘째 줄, 맨 아랫줄, 셋째 칸, 맨 위 칸, 맨 아래 칸; 'Both are F: the F line' = '둘
   다 F 자리, F 줄이에요'; 이름이 같은 음 (every note of its letter); 조표대로, 다시 조표대로예요 (after the bar line);
   G장조 음계를 쳐요; 엄지 밑으로 넣기, 3번 넘기기; chapter references as (16챕터); a sign never parts from the syllable after
   it (a word joiner). Chapter 20: 도돌이표 (chapter 8's), 시작 도돌이표 / 끝 도돌이표 (끝세로줄 앞의 점 두 개), 1번 괄호 / 2번
   괄호 (숫자 1이 적힌 괄호; never 괄호를 치다 for playing: 1번 괄호 마디를 쳐요), 겹세로줄 (two thin lines, under Fine), Fine
   (피네, so Fine와 / Fine를), 다 카포 (첫머리부터), 달 세뇨, 세뇨, 늘임표 (other name 페르마타; 제 길이보다 더 길게 늘여요),
   'N마디' for bar N, 그림 아래의 차례로 (never 차례대로 before a number string), 'N번 괄호' and 'D.C. al Fine' kept on one
   line. Skewer, not kebab (Korean 꼬치); stool; tip joint; middle C is 'the left door of the 4th small
   house' (never 'just left of' it); its short line is Clara's little LADDER (사다리 발판; in English never 'rung' -- her 2026-10-11 22:22: a hard word)
   until the ledger-lines chapter, which names it a LEDGER LINE (덧줄; 'leger' accepted): little ladders up into the
   bird's sky over the treble staff and down into the turtle's sea under the bass staff ('ladder 1, ladder 2'), read from five Cs by their real names: low C, bass C, middle C, treble C, high C (낮은 도, 낮은음자리표 도, 가운데 도, 높은음자리표 도, 높은 도; Phase 449, her 2026-10-12 19:17 '퀸즈랜드, 킹스랜드는 아이디어고 ... middle c, treble c, bass c 그 위로는 high c low c': Queensland and Kingsland are the idea, the two lands, never part of a C's name; no 'Sea C', 'Sky C' or 'Clara's C' any more; middle C in Korean stays 가운데 도, not 가온 도: her 2026-10-13 '가운데 도가 아무래도 알기 편한듯'); the
   two staves go by their REAL NAMES (her 2026-10-13 20:58 '퀸즈랜드 킹스랜드 좋은데 진짜 이름으로 불러야지 treble clef, bass clef'; Phase 459): every title, label, button, check row, drill level and teacher line says treble clef / bass clef (높은음자리표 / 낮은음자리표), or the treble staff / bass staff (높은음자리표 오선 / 낮은음자리표 오선) for a place on the page; 'Clef check', never 'Crown check'; 'between the staves', never 'between the lands'; Queensland and Kingsland are said ONCE, in chapter 7's opener, as the staves' other names; the royals are Staunton CHESS PIECES, never
   faces (Phases 420, 424: '체스 테마 너무 좋다'): the King navy, the Queen coral, Clara a pink pawn with a tiara (a princess -- said ONCE, where she first appears, 'Clara, a little princess'; never 'Princess Clara' / '클라라 공주', her 2026-10-12 16:02; she is a character the student meets, never the student: the student is always 'you', the week board says 'My week' / '나의 일주일' when no name is linked)
   (pink is hers alone; a pawn that crosses the board becomes a queen); the King's dragon and cows are words only;
   the butler is the RABBIT (Phase 433, her 2026-10-12 08:34 '토끼로 바꿔줘 마스코트' -- after the fox of Phases 424-432 and
   four new concepts she turned down) and appears only as his oval portrait, centred in the oval, with a coral bow tie
   (the REMEMBER band, the map's hall, the welcomes) -- never as a full figure in a picture ('그냥 초상화에만 넣자'), except two: chapter 1's puppet (he holds the strings) and chapter 2's opener (he stands between the houses) -- her 2026-10-12 15:56 '이 두개 사진에 있던 토끼 돌려줘'; frames and props are straight; no songs inside the
   chapters (the song book comes after the review); the lesson's words sit straight under the page title. Chapter names (her 2026-10-14 00:36 '6번,23번만 바꾸자'):
   chapter 6 is 'The Staff & the Two Clefs' / '오선과 두 음자리표' (once 'Reading the Staff'), and the composers chapter
   'Composers' / '작곡가' (once 'Famous Composers'); the ids and the guide pages' search titles stay.

9. **The Victorian look** (Phases 424-426, her decisions of 2026-10-10). Colours: navy, coral and green only -- green
   is the check --, pink only for Clara, NO BEIGE anywhere (white paper; hairlines are navy at low opacity). The
   wainscoting is lines only: a cornice running head (thick line, thin line, dentils), white picture boxes with the
   cut-in-corner frame, 'At the piano' and PLAY as raised panels in lines, REMEMBER as the chair rail with the butler's
   portrait, a chequered floor at every page's foot with the page number on a plaque; step numbers and section letters
   on chess squares; a drop capital in a dark square and a chequered diamond under titles on openers; Playfair italic
   for subheads and numbers, spaced capitals for small labels. The chapter map is the TOWNHOUSE (Phase 426;
   her 17:30 '좋다 이렇게 정하자' after a street, a village, a château garden and a classical plan): one tall house cut
   open like a doll's house -- the hall at the foot (the rabbit butler's portrait, a pedimented front door), a floor per level, a
   room per chapter, every floor with its own wallpaper and floor, NO LAMPS (Phase 438, '조명들 다 빼주고'), NO STAIRS
   ('계단 빼고 층층이'); quoins, dentil cornices, panelled wainscot, each chapter's picture on the wall with NO FRAME
   (Phase 438) and your room's picture under a wide glass dome on a little table instead of Clara; a mansard in chequered slates, a pedimented dormer 'Piano Butler', two turrets with the King on the
   LEFT and the Queen on the RIGHT. Classical letters on the map: Cinzel capitals for floors, Cormorant Garamond for
   rooms (Inter and plain icons 'had no classicism'). The map opens on the hall; the door swings open and the house
   rises above the hall, anchored at the bottom; inside one page load the house then shows straight away, and every page load opens on the hall again (Phase 442); a floor's rooms are counted from the bottom left (1 2 3 below, 4 5 6 above, Phase 442). Above it
   the WEEK BOARD: five practice days take the pawn (the linked student's own; 'My week' without a name, Phase 443) across the board to become a
   queen. The Workbook colours in the wide house (one row of rooms per floor); the guides' front page shows it too. The room scene's piano is the parlour upright seen from the front; the
   grand piano waits for a concert room of its own. The openers' two lists ('In this chapter', 'By the end, you can') mark
   each row with a small coral diamond inside a navy one (`bkGoal`), never a tick box (her 2026-10-13 23:57: a box looks
   like something to tick; Phase 462). On a keyboard, a tapped key is solid coral, the keys that go with it pale coral
   inside one navy outline, the rest plain white; green only ever means 'correct' (her 23:56 on 'Whose house is this?').
10. **The path in five levels** (Phase 436; the level plan of Phase 435, her '좋아. 그렇게 해보자' and '너 의견에 맞춰가자',
   2026-10-11/12). The house has five floors: LEVEL 1-5 on the plaques, 'n층' in Korean, no floor names ('첫레슨이라도
   하지말고 ... 그냥 층'). `PATH_STAGES` lists each level's chapter ids; the chapters are numbered 1 to 27 in that order
   (Accidentals, room 17 on Level 3, joined the map with its chapter in Phase 472, and every chapter after it moved up one;
   More Scales, `more-scales`, the last room on Level 5 after Styles, stays off the map until it has its chapter, so no
   chapter number moves when it comes). Phase 479 (her 2026-10-17 09:42 '음악 용어 먼저 … 그다음 음악 형식 선율과 프레이즈'):
   Level 4 is key-signatures, signs, intervals, chords, terms (23), form (24); Level 5 is melody (25), composers (26),
   styles (27), more-scales; composers and styles will be built together on one timeline. Free order inside a
   floor; the rooms a chapter is easier after (`ROOM_AFTER`) are one gentle line at its top, never a lock. The books never
   type a chapter number: they use `bkChapterNo(id)`. Everything in a box is centred ('박스가 있거나 하는 건 다 가운데
   정렬'): the floor plaques, each room's number and name over its picture, the hall's words; one name size and one
   picture height on each floor.
11. **The Lesson Books are written floor by floor** (her 2026-10-12 19:18 '우리 층층히 바꿨잖아. 레벨별로': the order of
   finishing the Lesson Books follows the levels). Finish every chapter of a level before the next level; inside a level,
   PATH_STAGES order. Done: posture-hands, first-steps, note-names, staff, pulse, note-values (Level 1; note-values' guide page waits for her G1-G3); whole-staff (named 'Line and Space Names' / '줄과 칸 이름' since Phase 459, her 20:58 '라인 칸 전체 이름 익히는거라 이름 바꿔야할 듯'; the id stays), tones, time-signatures, reading-steps, dynamics, pitch-range (Level 2, done; time-signatures, reading-steps, dynamics and
   pitch-range built in full in Phases 464, 466, 467 and 468 under rule 15, then her item-by-item review);
   ledger-lines (Level 3, written early), tempo (Level 3, built in full in Phase 469 under rule 15), rhythm (Level 3,
   Phase 470), scales (Level 3, Phase 471), accidentals (Level 3, a new chapter, Phase 472), piano-story (Level 3,
   Phase 473): Level 3 is done. Level 4: key-signatures (Phase 474), signs (Phase 475), intervals (Phase 477), chords (Phase 478), terms (Phase 479), form (Phase 480): Level 4 is done. Level 5: melody (Phase 481), composers (Phase 482), styles (Phase 483). Next (her 2026-10-17 02:05
   '1.2.3. 다동의해' to a macro-first plan: see the whole, then the parts): Phase 476 built the pass on scales (16) and key-signatures
   (19): the Lesson Book's first page is a map of all twelve keys (16: the keyboard clock, a semitone a step, the major
   scale one shape that turns, its half steps coral; 19: the circle of fifths, the chapter's five filled), the screen
   lesson ends with it again (an extra step, not counted in the chapter's steps; 16: scale stamps per hand, the same
   store as Today's; 19: 'I can draw it and name it', stamps 'ks:<key>'); the teacher sets each student's keys in the
   dashboard (Log lesson › For the student › Keys: a first line [keys:C,G,D]; [keys:-] clears; default the chapter's
   exam keys; G♭ stands for F♯) and the maps and drill level 10 use them; Workbook page 7 works in any key ('___
   major', a fresh copy per key, the first copy's ring coloured all year); fingering groups (C G D A E; B; F; B♭ E♭ A♭
   D♭). Map colours: the piano's own; coral only the half steps (clock) or the key looked at (circle); navy marks are
   the student's. Phase 477 built intervals (21) in the same frame: the Lesson
   Book's first page is the interval ladder (every interval from one note, a 2nd to an octave, counted on the keys);
   the screen lesson ends with the ladder in the student's keys, with major and perfect (an extra step); Workbook page
   7 is the ladder in any key. Phase 478 built chords (22) the same way: page 1 is the chord clock
   (chapter 16's twelve-key clock with the major triad one triangle, 4 + 3 half steps, turned to any key); the screen
   lesson ends with I, IV and V in the student's keys; Workbook page 7 is I IV V I in any key. Phase 479 built terms (23) the same way: page 1 is the
   expression ladder (every word on one map by family: speed slow to fast, changing speed as rows of beats, loud and
   soft under a widening wedge, touch and character, the little words); the screen lesson ends with it again, the
   student ticking the words they know; Workbook page 7 is a term hunt in any piece. Phase 480 built form (24) the
   same way: page 1 is the map of a piece (rows zooming in: the piece, its sections A B A, six phrases, 24 bars grouped
   by 4 and 8, bar 1's four beats; on screen every part plays when tapped); the screen lesson ends with a piece the
   student builds from A and B sections (the first always A; it always ends on C); Workbook page 7 is any piece's map
   on a bar ruler. Phase 481 built melody (25) the same way: page 1 is the map of a tune (the tune and its line with
   its high point, the question and the answer, the eight bars with the motif and its repetition and sequences, bar 1's
   notes on a staff; on screen every part plays when tapped, the bars two by two on phones); the screen lesson ends with
   a tune the student builds (a motif, two bars from it, a last note: it ends like a question or like an answer);
   Workbook page 7 is any piece's melody. Phase 482 built composers (26) on the timeline of music that chapter 27
   shares (MusTimeline, mtl482: one axis, 1600 to today; rows periods, keyboards, composers, sound, styles; each chapter
   draws its own rows strongly, the others lightly): page 1 the whole timeline, a lane per composer in birth order;
   pages 2 to 5 one period each (its stretch of the timeline and a who's who); page 6 who lived when (a line down from
   one year); the screen lesson ends with four composers to tap in order of birth; Workbook page 7 is my composers (any
   piece: composer, years, period, keyboard). Phase 483 built styles (27) on the same timeline, its sound and styles
   rows drawn strongly and the composers faintly: page 1 the timeline (folk songs a dashed lane under everything);
   page 2 texture (one tune drawn three ways, every roll the same range and width); page 3 the sound of each period
   (its texture and three things to listen for; its own clips: Bach Invention No. 1, Mozart K. 545, Liszt Liebestraum
   No. 3, then Debussy and Hisaishi in their style); page 4 folk (the pentatonic scale is a major scale without its 4th
   and 7th notes); page 5 blues and jazz; page 6 pop (verse, chorus, bridge; C G Am F). More scales waits: the foundation (rule 16) folds it into Scales and keys. The big-map first pages for chapters 1-18
   come after her combined review.
12. **Counting is written with + for 'and'** (her 2026-10-13 G2: 'walk, running, 그러고 박자표에 맞게 박자세기 1 2 3 4,
   1+2+3+4+, 1e+a 2e+a ... +은 and 이야 내가 저렇게 표기해'). Beats: 1 2 3 4; quavers: 1 + 2 + 3 + 4 +; semiquavers:
   1 e + a 2 e + a, always as the time signature counts (2, 3 or 4 beats). In words the + is read 'and'. Her ways in to a
   steady beat: walking and running. Her two pulse faults (G1): not keeping the count steady; playing the first beat and
   starting the count too late. The rhythm words (her 2026-10-14 00:07 '이것도 다른 단어로 바꿔줘 walk running 아님 ta titi'):
   walk for one sound on a beat and run-ning for two, in English; in Korean 타 and 티-티, because a spoken word needs as
   many syllables as sounds (걷기 and 달리기 have two and three); never bird, tur-tle or light-house any more. A tapped
   note sounds for as long as the pad is held (her 00:12), like a key.
13. **Theory still to come, room by room** (her 2026-10-13 '너 추천따를께 책바탕 기반으로', after the gap list of 2026-10-12
   against AMEB/ABRSM grades 1-5): each goes into its room's Lesson Book when that book is written, as a higher drill
   level when it belongs to a later grade. Note values: the breve, double dots (the drill's level 9 since Phase 460). Time signatures: anacrusis (today a
   Rhythm tool), 2/8 4/8 4/2 6/4 9/4 12/4, irregular 5/8 7/8 7/4. Scales: the pentatonic, whole-tone and blues scales and the modes get a room of their own (her 2026-10-14
   00:36 '스케일은 장단음계 빼고 다른 모드나 블루스 스케일같은건 챕터 더 만들거야?', then 06:42 '응 스케일 너 추천대로가자'): More
   Scales / 여러 가지 음계 (`more-scales`; the book's subtitle Pentatonic, Blues, Whole-tone & Modes), the last room on
   Level 5, after Styles; the Scales room keeps major and minor; the chromatic scale stays in chapter 11. Intervals:
   compound intervals. Chords: the augmented triad, ii and vi, the cadential 6/4 (Ic), passing and auxiliary notes,
   recognising a modulation. Clefs: the tenor clef; transposing between clefs; transposing instruments and concert
   pitch. Terms: French and German terms. Form and styles: suite, minuet and trio, scherzo, theme and variations,
   recitative and aria; ostinato; canon and imitation; the orchestra's families and their clefs. A new room on Level 5,
   'Writing music' (음악 쓰기): rhythm to words and word stress, a melody from a rhythm or an opening, cadences and a
   harmonised melody in SATB. The house's floor-by-floor reveal is decided once every book is built ('일단 다 만들고
   정하자'). Legato and the slur (her 2026-10-13 23:56 '레가토를 공식적으로 설명해야할 것 같은데 어디서? 그리고 슬러는?'):
   legato, the touch, is defined where the student first plays notes one after another, chapter 2's 'Play on the
   patterns' (one dictionary line; the relay baton stays its REMEMBER), since legato is the default touch from day one
   (her 2026-09-28 '레가토 개념 기본으로 깔고 가져가거든, 좀 나중에 스타카토'); the slur, legato's sign, comes in chapter 10
   (dynamics and articulation) with staccato, after chapter 9 because a slur joins different notes, set beside chapter
   8's tie: the same curve, on the same note a tie, on different notes a slur. Chapter 8 teaches the tie only.
14. **Like a dictionary** (her 2026-10-13 23:51 '모든 설명을 사전처럼 깔끔하게. 군더더기 없이'). Every explanation reads like
   a dictionary entry: the term in bold first, then what it is in one short sentence; a page with several terms lists
   them as entries, one under another (`LbDefs`: **bar line** A line that divides the music into bars.). After the
   definition, at most one more fact a sentence: how long, where it sits, how to play it, its other name ('Its other
   name is a measure.'). No story, no warm-up, no 'let's', nothing the picture already shows. Tasks stay set tasks
   (rule 3). From chapter 8 on, then the finished books, chapter by chapter.
15. **Recommendations by default; strict reviewers; her final review item by item** (her 2026-10-13 23:51 '지금부터
   추천대로 다 가줘, 검토자 몇명이 까다롭게 나 대신 검수해서 레슨하기 쉽게 다 만들고 내가 최종 하나씩 검토할 수 있게 해줘').
   No more drafts that wait for her answers: each chapter is built in full (the Lesson Book, its screen lesson, the
   drill, the Workbook, the Teacher copy) with the recommendations. Then several fresh reviewers who did not make it
   check it hard, each from one side: easy to teach; the theory right against AMEB and ABRSM; easy for a child to read
   (rules 7, 8, 14); print and screen (fit, clipping, overlap, both languages). Every valid point is fixed, and only then
   does she see it: the final review page shows the chapter one item at a time, and she marks each OK or Change with a
   note. The G questions (what only her classroom knows) get my best guess, marked for that review. Still hers to
   decide: strategy, money, anything sent outside, deleting, AdSense. The review page is a private artifact; its `db`
   collection `verdicts` keeps her marks, one document per item (`<chapter key>-<item>`: `v` 'ok' or 'change', `note`).
   Read them with ArtifactData `list` when she says she has finished, then fix every Change. Chapter 8's page:
   https://claude.ai/artifact/J4QaR5BUxDJoWRbE8fFPjB (keys `ts8-...`); chapter 9's: https://claude.ai/artifact/4dCGVtL6SsPyfeakiZAzrS
   (keys `ss9-...`). From chapter 10 on (her 2026-10-14 09:17 '계속 가줘 최종검토는 한꺼번에하게') the chapters are built back
   to back, each with its reviewers and fixes, and she reviews them all at once: one combined review page (keys
   `<chapter key>-<item>` as before), made when she asks for it, instead of a page per chapter. Waiting for it: chapters 10
   (dynamics), 12 (pitch-range), 13 (tempo), 14 (rhythm), 16 (scales), 17 (accidentals), 18 (piano-story), 19
   (key-signatures), 20 (signs), 21 (intervals), 22 (chords), 23 (terms), 24 (form), 25 (melody), 26 (composers) and 27 (styles).
   **Review sized to the change** (her 2026-10-18 02:30 '1,2 응', after long sessions cost too much time and tokens). The full review above (four strict reviewers, then a verifier) is for a new chapter, a new concept book, or any change to a shared part (KeyRing, FifthsRing, the Lesson Book layout, the app shell). A small change (wording, one page, one tool's layout, a bug fix, one number) is checked by me alone: the build, the compile and syntax check, screenshots at 320 px and the print page in both languages, and a diff against the chapters that must not change; one fresh reviewer only when the change touches theory or Korean. A change to a shared part is never small. Her final review stays as it is. **One window, one job**: each job runs in its own new window, started with the prompt in `_workspace/concept-book-kit/HANDOFF.md`, and the window is closed when the job is done. The kit that builds and tests a concept book (source, patch, harness, measuring scripts, the reviewers' reports) is in `_workspace/concept-book-kit/` (untracked on purpose).
16. **The foundation: five areas, concept first** (her 2026-10-17 21:09 '스케일 하나 둘 설명하는게 아니라 개념알려주고 쫙
   다 적용시킬 수 있게 ... 나는 좀 거꾸로 하고싶어서'; 21:13 '이게 pitch 영역이면 그것만, 리듬 영역이면 그것만, 터치
   아티큘레이션, 테크닉에 스케일 코드 이런식으로'; 21:20 '시험지도는 당장 만들 필요는 없고 바탕 정리를 해놓는게 우선';
   21:32 '그렇게 하자. 이렇게 가는게 맞아 내 레슨 성격에 더 맞아'). Everything sits in five areas, each holding only its own
   kind of thing, 13 concepts in all: Pitch (keys and staff; semitones and accidentals; intervals; scales and keys;
   chords), Rhythm (beat and time), Touch and expression (touch; tempo and character), Technique (posture and hands; positions
   and finger numbers; playing scales and chords), Pieces (reading tunes; melody and form). The stories of music (the piano,
   composers, styles) and the practice helpers sit beside the five, not in them. Each concept is taught whole, once: one
   rule and the whole of it at once (all twelve major scales from one pattern, not C, then G, then F), then practised
   in steps (First, Then, Further, Later) that differ by student. Scales and chords are explained in Pitch and played in
   Technique. The Toolbox is the backbone: since Phase 484 `TOOL_AREAS`, `TOOL_CATS` (the 15 groups) and `TOOL_CONCEPT`
   put every tool under one concept, and tools that do the same job stay side by side until she chooses which to keep.
   A Lesson Book becomes a short concept book (the rule, the whole map, how to use the tools, a check); the Workbook and
   the drill follow the practice steps. Exams (AMEB first, then ABRSM) are laid over the foundation later, as routes
   through it; nothing is built for an exam yet. The plan and the inventory of every lesson step, Workbook page, drill
   level and tool under its concept: https://claude.ai/artifact/V29Y63iAxpApaCz9tx9s14. Order: the Toolbox grouped
   (Phase 484), then Scales and keys rebuilt as the model concept book (Phase 485: printed `?book=concept&ch=p-scales`,
   on screen the Toolbox's `cb-p-scales`, a card under Scales and keys), then the other concepts one by one, then the
   exams. The house of five levels (rule 10) and the 27 chapters stay as they are for now.

## Verified Piece Counts (2026 Syllabus)

> **Last audited: 2026-04-23** — All counts verified by running the bash count script against live files and cross-checked against the 2026 AMEB Piano Syllabus PDF.

### Comprehensive Piano

| Grade | File | Total | List A | List B | List C | List D | Other | Notes |
|-------|------|-------|--------|--------|--------|--------|-------|-------|
| Prelim | data_prelim.js | 93 | 24 | 23 | 46 | — | — | |
| G1 | data_g1.js | 143 | 48 | 37 | 58 | — | — | List C includes HOULIHAN Albatross |
| G2 | data_g2.js | 184 | 58 | 50 | 76 | — | — | |
| G3 | data_g3.js | 196 | 57 | 59 | 80 | — | — | |
| G4 | data_g4.js | 156 | 49 | 51 | 56 | — | — | |
| G5 | data_g5_1.js | 168 | 41 | 33 | 38 | 48 | Collab:8 | Embedded inline in HTML; `data_g5.js` is deprecated skeleton |
| G6 | piano-repertoire_g6.html | 160 | 41 | 35 | 37 | 47 | — | Data embedded inline in HTML only |
| G7 | data_g7.js + HTML | 148 | 37 | 28 | 41 | 42 | — | JS and HTML in sync as of 2026-04-13 |
| G8 | data_g8.js + HTML | 145 | 29 | 29 | 38 | 49 | — | JS and HTML match |
| **Total** | | **1,393** | | | | | | |

### Piano for Leisure

| Grade | File | Total | S4 | S3 | S2 | S1 | Manual | Notes |
|-------|------|-------|----|----|----|----|--------|-------|
| Prelim | data_prelim_leisure.js | 71 | 12 | 11 | 12 | 12 | 24 | |
| G1 | data_g1_leisure.js | 70 | 12 | 11 | 10 | 11 | 26 | Manual corrected (4 Prelim pieces removed) |
| G2 | data_g2_leisure.js | 64 | 12 | 11 | 11 | 12 | 18 | |
| G3 | data_g3_leisure.js | 68 | 12 | 11 | 9 | 13 | 23 | |
| G4 | data_g4_leisure.js | 80 | 12 | 11 | 11 | 11 | 35 | |
| G5 | data_g5_leisure.js | 78 | 12 | 11 | 13 | 12 | 30 | |
| G6 | data_g6_leisure.js | 88 | 12 | 12 | 11 | 12 | 41 | |
| G7 | data_g7_leisure.js | 92 | 12 | 9 | 14 | 12 | 45 | |
| G8 | data_g8_leisure.js | 94 | 11 | — | 12 | 11 | 60 | No S3 — series only goes to G7; BEETHOVEN Andante duplicate removed from S1 |
| **Total** | | **705** | | | | | | |

### Grand Total: 2,099 pieces across all grades and both syllabuses

### AMEB Diploma Repertoire

| Exam | Code | File | Total | List A | List B | List C | List D | Program |
|------|------|------|-------|--------|--------|--------|--------|---------|
| AMusA | 9950 | data_amusa.js | 161 | 39 | 27 | 50 | 45 | 25–40 min |
| LMusA | 9951 | data_lmusa.js | 226 | 55 | 29 | 51 | 91 | 35–50 min |
| **Total** | | | **387** | | | | | |

**Grand Total across all syllabuses: 2,919 pieces**
- AMEB Comprehensive + Leisure: 2,099
- ABRSM Initial–G8: 433
- AMEB Diploma (AMusA + LMusA): 387 — but note: open-pool format (candidates select from the list; pieces may appear in multiple lists)

---

### Phase 4 Updates (2026-04-30)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Piece count verification | All data_gX.js files | Bash count script confirmed 2,099 total pieces across 18 files — all match CLAUDE.md table exactly |
| 2 | Student card: "Lessons this month" badge | teacher-dashboard.html | Shows `N× this month` badge next to last lesson date. Counts only non-absent logs for current calendar month. |
| 3 | Sort: "Lessons this month" option | teacher-dashboard.html | New `monthcount` sort option added to student list dropdown — sorts by most lessons in current month first |
| 4 | ScheduleView: Absent button fix | teacher-dashboard.html | + Log / Absent buttons now only appear on today's slots (weekOffset=0, day=todayDay). Other days show no buttons. Already-logged slots show ✓ Logged; absent slots show 😔 Absent badge. |
| 5 | Paused students visible in calendar | teacher-dashboard.html | Removed `filter(s => !s.paused)` from ScheduleView and TodayView slot builders. Paused students shown dimmed (opacity 0.55, grayscale 40%) with ⏸ suffix on name. No Log/Absent buttons for paused slots. |
| 6 | showPaused default → true | teacher-dashboard.html | `useState(false)` → `useState(true)` — paused students visible in student list by default |
| 7 | Pause modal with date fields | teacher-dashboard.html | `PauseModal` component added — replaces `confirm()` dialog. Fields: Pause from (date, default today), Return date (date, optional), Undecided checkbox (disables return date, shows "TBD"). `pauseUntil` + `pauseUndecided` stored in `extra` JSON blob. Paused banner in StudentDetail shows return date or "Return date TBD". |
| 8 | ScheduleView: slot display tiers | teacher-dashboard.html | Three display tiers: tiny (<30px, name only), compact (30–44px, name + time), full (44px+, name + time + buttons). Removed Grade label from all calendar slots. |
| 9 | ScheduleView: day header shows total hours | teacher-dashboard.html | Each day column header now shows lesson count + total hours (e.g. `10 lessons / 9h 30m`). Zero-lesson days show count only. |
| 10 | ScheduleView: week navigation | teacher-dashboard.html | ← Prev / Next → buttons added above calendar. `weekOffset` state (0=this week). Label shows "This week" / "Next week" / "Last week" / date range. Today dot highlight and Log/Absent buttons only active at weekOffset=0. `isFortnightWeek()` updated to accept `weekOffset` param for correct fortnightly display across weeks. |
| 11 | Calendar background → white + coloured blocks | teacher-dashboard.html | Grid column backgrounds changed to white. Lesson blocks now filled with muted pastel per day colour (`blockBg`). `DAY_COLOR` extended with `blockBg` + `blockText` fields. + Log button uses `dc.border` background with white text. |
| 12 | Pastel colours refined | teacher-dashboard.html | DAY_COLOR palette tuned twice — first to low-saturation muted pastels, then slightly deepened for better day distinction while remaining easy on the eyes. |

---

### Phase 3 Updates (2026-04-29)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Sheet button → Google search | Prelim–G8 HTML (9 files) + Index.html | `google.com/search?q=` with composer surname + title + "sheet music". Originally set to IMSLP but reverted same day — IMSLP returns empty results too often. `imslpUrl()` helper and `PUBLIC_DOMAIN_ERAS` removed from Index.html; replaced with `sheetUrl()`. |
| 2 | COMPOSER_LINKS expanded | Prelim–G8 HTML (9 files) | 131–141 new Wikipedia URLs added per file (Brahms, Liszt, Rachmaninoff, Fauré, Ellington, Copland, Joplin, Saint-Saëns, Vaughan Williams, etc.) — 1,119 total entries injected |
| 3 | Progress Passport added | teacher-dashboard.html | New section inside `StudentDetail` (above Lesson History) — shows attendance rate, lesson streak, section coverage bars (Repertoire/Technical/SR/GK), List A/B/C mention scan, parent-facing summary. No Supabase schema changes required. |
| 4 | Absent ↔ Attended toggle added | teacher-dashboard.html | `markAttended()` function added — flips absent log to `type: "regular"` via Supabase update. Button appears on absent log cards in StudentDetail. |
| 5 | Makeup Schedule section added | teacher-dashboard.html | New card in StudentDetail (above Lesson History) — shows pending makeups from absent logs that have `makeupDate` set. Colour-coded: overdue (red), today (green), upcoming (grey). ✓ Done button marks makeup as attended. |
| 6 | Today view — student name clickable | teacher-dashboard.html | Avatar + name area in TodayView cards now navigates to StudentDetail on click (hover highlight added). ScheduleView calendar cards also wired with `onClick → onSelect`. |
| 7 | Today view — status-aware action buttons | teacher-dashboard.html | Replaced single Absent button with dynamic status system: pending → + Log lesson (primary) + Absent (quiet text), absent → 😔 badge + ✓ Attended + 📅 Set makeup + ↩ Undo, logged → ✓ Logged badge + Edit log. Card left-border colour reflects status. |
| 8 | Fortnightly lesson frequency | teacher-dashboard.html | Added "Fortnightly" option to lesson frequency selector. `isFortnightWeek(startDate)` helper calculates Monday-based week diff to show/dim off-weeks in ScheduleView. Stored in `extra` JSON blob — no schema migration needed. |
| 9 | planMonths removed for general track | teacher-dashboard.html | General track students no longer need a plan duration — form shows only Goal textarea. "Plan ends:" line and "Xmo left" badge hidden in StudentDetail header. Progress Passport unaffected (reads only from lesson_logs). |
| 10 | Progress Passport period filter | teacher-dashboard.html | Month / Quarter / All time toggle added to Passport header. `passportPeriod` state in `StudentDetail` filters `studentLogs` by date range before computing all stats, coverage bars, and parent summary. |
| 11 | Student pause/resume | teacher-dashboard.html | `pauseStudent()` / `resumeStudent()` functions added to App. `paused: true` + `pausedAt` stored in `extra` JSON blob. ⏸ Pause button in StudentDetail, paused banner shown. Card greyed out + "⏸ Paused" badge. Paused students excluded from TodayView and ScheduleView slots. `showPaused` toggle in student list filter bar. |
| 12 | "3mo left" badge removed from general track cards | teacher-dashboard.html | StudentCard top-right badge now only shows weeks countdown for exam track students. General track shows nothing. |

---

### Phase 2 Audit — Issues Found & Fixed (2026-04-23)

| # | Issue | File(s) | Fix Applied |
|---|-------|---------|-------------|
| 1 | G5 Collab: Primo/Secondo tags missing on 6 pieces | piano-repertoire_g5.html | Added [Primo or Secondo] / [Primo] / [Secondo] to Norwegian dance, Kindermarsch, Gartenmelodie, Conga, Mulga Bill, Petit poucet |
| 2 | G5 Manual: 13 titles abbreviated or missing source attribution | piano-repertoire_g5.html | Full titles restored: Czerny (School of Velocity), Kabalevsky ×2 (Allegro marcato / Allegro), Handel (Presto 4th mvt), Telemann (TWV 33:8), Shchedrin (Notebook for young people), Sitsky (No 108 & No 109), Chua (… or less), Bailey ×2 (Jazzin' around 4/5), Cornick ×2 (Blue piano), McCombe (Australian piano miniatures), Benjamin/Eagles (Australian Anthology) |

---

### Phase 1 Audit — Issues Found & Fixed (2026-04-13)

| # | Issue | File(s) | Fix Applied |
|---|-------|---------|-------------|
| 1 | SHCHEDRIN, SITSKY, VINE in wrong list (D instead of C) | data_g7.js | Moved to List C Manual — confirmed by PDF p.72 |
| 2 | Same 3 pieces duplicated in both C and D | piano-repertoire_g7.html | Removed from List D |
| 3 | BEATH, B. *Contrasts* missing from HTML List D | piano-repertoire_g7.html | Added — confirmed by PDF p.72 |
| 4 | Debussy title missing English translation | piano-repertoire_g7.html | Fixed to `[The girl with the flaxen hair]` |
| 5 | BENDA sonatina wrong number (No 7 → No 13) | piano-repertoire_g7.html | Fixed — confirmed by PDF p.71 |
| 6 | BURGMÜLLER title missing `[Spinning song]` | piano-repertoire_g7.html | Fixed to match JS and PDF |
| 7 | Tchaikovsky missing English translation in HTML | piano-repertoire_g7.html | Fixed to `[March: Song of the lark]` |
| 8 | All 168 G5 focus arrays had only 2 keywords | data_g5_1.js | Third keyword added to all 168 pieces |
| 9 | data_g5.js (SYLLABUS_DATA) — no nat/era/focus fields | data_g5.js | Marked deprecated with warning comment |

---

## Key Composer Facts (verified, do not change)

| Composer | Nationality | Note |
|----------|-------------|-------|
| CHUA, S. (Sonny Chua) | Australian | Born Malaysia, emigrated to Melbourne — NOT Singaporean |
| KUTNOWSKI, M. | Argentine | Do NOT tag focus as "Australian character" |
| CHAPPLE, B. | English | Do NOT tag focus as "Australian character" |
| NORTON, C. | English | Do NOT tag focus as "Australian character" |

---

## PDF Navigation Guide

The AMEB PDFs have a **page offset** — printed syllabus page numbers ≠ PDF file page numbers (offset ≈ 6 pages due to front matter).

**Formula:** PDF file page ≈ Printed page + 6

### Piano Syllabus 2026.pdf — grade page reference
| Grade | Printed pages | PDF file pages |
|-------|--------------|----------------|
| G1 | p.52–56 | ~34–36 |
| G2 | p.57–59 | ~35–37 |
| G3 | p.60–62 | ~38–40 |
| G4 | p.62–65 | ~40–43 |

### Piano for Leisure Syllabus 2026.pdf — grade page reference
| Grade | Printed pages | PDF file pages |
|-------|--------------|----------------|
| Prelim | p.89 | ~25 |
| G1 | p.90 | ~26 |
| G2 | p.91 | ~27 |
| G3 | p.92 | ~28 |
| G4 | p.94 | ~30 |

---

## Operational Guidelines

### Strategic Thinking
Before any edit, think step-by-step:
1. Verify the target count against the official PDF
2. Identify which section (List A/B/C, Series, Manual) needs the change
3. Check alphabetical ordering within the section
4. Update section header comments AND file total header

### Verifying Data After Every Edit
Always run this after modifying a data file:
```bash
node -e "
const fs = require('fs');
const content = fs.readFileSync('PATH/data_gX.js', 'utf8');
eval(content.replace('const DATA_GX', 'var DATA_GX'));
const byList = {};
DATA_GX.forEach(p => { byList[p.l] = (byList[p.l]||0)+1; });
console.log(byList);
console.log('Total:', DATA_GX.length);
"
```

### Editing Rules
- **Alphabetical order** within each section by composer surname
- **Section header comments** must reflect accurate piece count e.g. `// LIST A — Manual (46 pieces)`
- **Never remove a syllabus piece** without checking the PDF first
- **Focus arrays** must have exactly 3 pedagogical keywords
- **Never assign national identity keywords** (e.g. "Australian character") to non-Australian composers

### Tone & Style
Professional, encouraging, and highly organised — like a refined butler for a concert pianist.

### Format Excellence
- **Tables** for syllabus comparisons and piece counts
- **Markdown** for clear hierarchies
- **Mermaid.js** for practice flowcharts and system architecture

### Reference Integrity
Always cross-check the **2026 AMEB Piano Syllabus PDF** before adding or removing pieces. Never add pieces from memory alone.

---

## How the AI Can Help

| Task | Approach |
|------|----------|
| Syllabus data corrections | Read PDF → verify → edit data_gX.js → bash verify count |
| New grade HTML pages | Follow G5/G6 pattern — self-contained, embed data inline |
| Practice habit tools | Design flowcharts with Mermaid.js, AMEB-aligned session structures |
| Repertoire selection | Filter by grade, era, nationality, focus area from data arrays |
| Technical work tracking | Reference AMEB Technical Work requirements per grade |
| Sight-reading & Aural | Cross-reference syllabus Section III requirements per grade |

---

### Phase 5 Updates (2026-05-01)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Date numbers in schedule day headers | teacher-dashboard.html | Each day column (SUN–SAT) now shows the actual date number below the weekday label. Computed from `weekOffset` via `weekDates` map (ISO Monday anchor). Today's date shown larger + coloured; other days smaller + muted. Correct across Prev/Next week navigation. |
| 2 | Slot height bug fix (30-min slots) | teacher-dashboard.html | `lessonDuration` missing → `dur = undefined` → `height = NaN` → slot rendered as tiny (name only). Fixed with `safeDur` fallback: `(slot.dur && slot.dur > 0) ? slot.dur : 45`. |
| 3 | Calendar grid height expanded | teacher-dashboard.html | `SLOT_H` raised 56 → 60 → 80 px/hour. Results: 30-min = 40px (name+time visible), 45-min = 60px (name+time+buttons), 60-min = 80px (full). |
| 4 | Slot display tier logic simplified | teacher-dashboard.html | `isTiny = height < 28` (name only for <20min slots); `isCompact` removed — all non-tiny slots show name + time + buttons. `lineHeight: 1.2` added to prevent text clipping. |
| 5 | Weekly override system | teacher-dashboard.html | `weekOverrides` state: `{ "<isoMonday>/<studentId>/<slotIdx>": { day, time } }`. Slots rendered from override when present. Week key computed from `weekOffset`. Override indicator: purple dashed border + ↪ suffix on time. ✕ button to reset individual override. "↺ Reset moves" button in week header clears all overrides for current week. |
| 6 | Reschedule popover (replaces broken drag-and-drop modal) | teacher-dashboard.html | Drag-and-drop fully removed (caused blank screen due to browser drag event timing). Replaced with ✎ icon on each slot → click opens `ReschedulePopover` anchored next to the slot (fixed position, auto-flips left/right to stay in viewport). Popover contains: day picker (Sun–Sat tabs, original day highlighted), time editor (−1h/−15/direct input/+15/+1h coarse + −5/−1/+1/+5m fine nudge), live end-time display. Save buttons appear only when day or time has changed: 📅 This week only (stores to `weekOverrides`) / 🔁 Update regular schedule (Supabase `lesson_day`/`lesson_time` update + `setStudents`). Backdrop click closes popover. |
| 7 | `handlePermanentReschedule` in App | teacher-dashboard.html | New App-level async function. Updates `lesson_day`/`lesson_time` (slotIdx=1) or `lesson_day2`/`lesson_time2` (slotIdx=2) via Supabase. Reflects in `students` state and `selected` immediately. |
| 8 | Drag-and-drop — pure DOM approach | teacher-dashboard.html | Completely rewrote drag to avoid React render cycles. All drag visuals (clone div + ghost div) are `createElement`/`appendChild`/`remove` in pure DOM inside `onSlotMouseDown` closure — zero `setState` calls during mouse movement. Full-screen transparent overlay div captures all mouse events during drag. `data-override-key` attribute on each slot div allows direct `style.opacity` manipulation without React. `setActivePopover` called only once on mouseup after cleanup. |
| 9 | ReschedulePopover crash fix | teacher-dashboard.html | Root cause of all blank-screen crashes: `editTime` state was `null` on first render (useEffect runs after render, not before) → `timeToMins(null)` → `null.split(":")` → TypeError. Fixed by initialising `useState` directly from `activePopover` props instead of relying on useEffect, plus a `if (!editDay \|\| !editTime) return null` guard. |
| 10 | ErrorBoundary added | teacher-dashboard.html | `class ErrorBoundary extends React.Component` wraps `<App/>` in `ReactDOM.createRoot(...).render(...)`. Catches any future React render crash and displays the error message + stack trace on screen instead of a blank page. |

---

### Phase 6 Updates (2026-05-02)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | `startDate` persisting after edit | teacher-dashboard.html | `studentToRow` was silently dropping `startDate` (not written to any column). Fixed: `extraObj.startDate = startDate` explicitly added. `rowToStudent` reads `extra.startDate` first before falling back to `created_at`. |
| 2 | Save button always enabled | teacher-dashboard.html | `valid` check simplified to `f.name.trim().length > 0` — no longer requires `examDate` for exam track students. |
| 3 | Exam prep refactored as optional section | teacher-dashboard.html | Removed binary exam/general toggle. `isExamStudent(s)` helper: `!!(s && s.examDate)`. All 43 `track==="exam"` comparisons replaced. `StudentModal` rewritten with collapsible "Exam" accordion — only visible when expanded. `examType` field added (free text — supports AMEB, RCM, Trinity, ABRSM, etc.), stored in `extra` blob. |
| 4 | `lessonDuration2` for 2x-per-week students | teacher-dashboard.html | Second lesson duration field added to `StudentModal` when `lessonsPerWeek=2`. Stored in `extra` blob as `lessonDuration2`. `safeDur2` computed in `ScheduleView` with fallback to `lessonDuration`. |
| 5 | `lesson_day2` / `lesson_time2` DB columns | teacher-dashboard.html | Added via `ALTER TABLE students ADD COLUMN lesson_day2 text, ADD COLUMN lesson_time2 text`. `rowToStudent` and `studentToRow` updated to map these columns. `NOTIFY pgrst, 'reload schema'` run to clear PostgREST cache. |
| 6 | `lesson_overrides` table: `from_week` column | teacher-dashboard.html | `from_week date` column added to `lesson_overrides`. `saveOverride` guard added: rejects saves when both `from_week` and `week_key` are NULL. `onFromWeek` handler uses `fw = targetKey \|\| currentWeekKey` as null-safe fallback. |
| 7 | Override `from` key format | teacher-dashboard.html | "From this week onwards" overrides stored as `from/<isoMonday>/<studentId>/<slotIdx>`. `getEffectiveOverride()` checks exact week key first, then most-recent `from/` ≤ currentWeekKey. |
| 8 | `weekDates` Sunday anchor fix | teacher-dashboard.html | Previous formula gave SUN the following week's date (index off-by-one). Fixed with Sunday anchor: `sun.setDate(now.getDate() - nowDay + weekOffset * 7)` + `DAY_OFFSET` dict. `DAYS_ORDER = ["Sunday","Monday",...,"Saturday"]` (Sun-first). |
| 9 | `hitTest` cross-column drag fix | teacher-dashboard.html | `x` calculation corrected: `(cx - rect.left) + scrollLeft - TC`. `totalColW` now uses `grid.scrollWidth - TC` (full scroll width) instead of `rect.width` (visible only). `hitTest` returns `{ day, time, dayIdx, colW, rect, scrollLeft }` — `updateVisuals` uses `hit.colW` for ghost width. |
| 10 | Google Calendar-style drag-and-drop | teacher-dashboard.html | Pure DOM drag (no React setState during mousemove). Floating clone follows cursor, ghost shows drop target. Cross-column dragging works via fixed `hitTest`. On mouseup: opens `ReschedulePopover` at drop position with pre-filled day/time. |
| 11 | RevertConfirmPopover (new component) | teacher-dashboard.html | Clicking ✕ on an overridden (moved) slot opens 3-option revert menu: ↺ Revert this week only (masks from-override with exact-week original) / ↺↺ Revert from this week on (new from-override pointing to original) / ⚡ Revert all weeks (delete override entirely). |
| 12 | Skip button hidden on overridden slots | teacher-dashboard.html | Skip-btn ✕ (red, hover-visible) now only shows on non-overridden slots (`!slot.isOverridden`). Overridden slots show blue ✕ → RevertConfirmPopover. Eliminates two conflicting ✕ buttons on same block. |
| 13 | SkipConfirmPopover label improvements | teacher-dashboard.html | Clearer option labels: "Skip this week only" / "Skip from this week on" / "Remove this lesson slot" / "Delete student". Subtitles explain exactly what each option does. |

---

### Phase 10 Updates (2026-05-05)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | AMusA diploma repertoire | `AMusA/data_amusa.js`, `AMusA/piano-repertoire_amusa.html` | 161 pieces (A:39, B:27, C:50, D:45) from 2026 AMEB Manual of Syllabuses pp.79–80. Self-contained React 18 + Tailwind app, purple gradient header, exam requirements banner (Exam 9950, 25–40 min), List A/B/C/D tabs, Era chips, Nationality dropdown, Wikipedia COMPOSER_LINKS, YT + Sheet links. |
| 2 | LMusA diploma repertoire | `LMusA/data_lmusa.js`, `LMusA/piano-repertoire_lmusa.html` | 226 pieces (A:55, B:29, C:51, D:91) from 2026 AMEB Manual of Syllabuses pp.81–83. Same self-contained app pattern, deeper purple header (#3b0764), exam requirements banner (Exam 9951, 35–50 min, concert standard, 1 work from memory). |
| 3 | index.html — diploma integration | `index.html` | `DIPLOMA_META` array added. `buildCorpus()` now includes diploma data tagged `_syllabus:"AMEB Diploma"`. `GradeGrid` shows "Diploma Level" section under AMEB tab with direct links to AMusA/LMusA pages. Sidebar filter gains "🎓 Diploma" option. Piece count updated to 2,897. |
| 4 | CLAUDE.md updated | `CLAUDE.md` | File structure, project overview, grand total, and diploma piece count table all updated. |

---


## History and build log

Everything before 2026-10-29 that used to follow here (Project History, Product Direction, every phase note,
the deferred features, the build log rows 262-741 and the old Current Status with its Pending work table) is in
`CLAUDE-history.md`, unchanged. Read it for root causes, schema decisions and why a call was made. New build-log
rows go after its last row, just before the old Current Status.
