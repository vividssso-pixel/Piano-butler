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

**Push hold note -- resolved (2026-09-22):** the 2026-09-20 hold is over. Sohyun renewed her
expired GitHub token and pushed everything in one go on 2026-09-22 (`0492fb4..f3349cb`), including
the button/design commits that were held back. There is no standing push hold right now -- go back
to the normal rule: commit locally as usual, never `git push` (that's still always Sohyun's call
from her own Terminal), and just mention once per session if there's anything committed but
unpushed.

**drills.html is now a COMPILED file (Phase 327).** Never edit `drills.html` by hand. The source is
`drills.src.html`; after editing it run `node tools/precompile.js` (it writes `drills.html`). Details in the
section "drills.html: source and compiled page" below.

Be specific and honest, not just reassuring. If something is stalling, say it's stalling — and
say what the next concrete action is.

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
| `drills.html` | **The page the site serves.** Same page with the code already compiled in `<script id="app-js">`, no babel-standalone. Loads in about half a second. Starts with a `GENERATED by precompile.js` comment. |
| `tools/precompile.js` | `node tools/precompile.js` (or `node tools/precompile.js <in> <out>`) reads `drills.src.html` and writes `drills.html`. Uses `@babel/standalone` if installed, otherwise `@babel/core` + `@babel/preset-react` (both are in this repo's `node_modules`). Always the classic runtime (`React.createElement`): the page loads React from a CDN script, so a `jsx-runtime` / `jsxDEV` import would break it, and the script refuses to write such output. |

**Rule: edit `drills.src.html`, then run `node tools/precompile.js`, then commit BOTH files.** Never edit `drills.html` directly: the next precompile would overwrite the change. The verification bar is unchanged: check `drills.html` in a real browser (`?book=...` pages, a chapter, a tool), in both languages.

The printed books and the Cut-outs are generated from the same file (`?book=lesson|work|teacher|cutouts`). The build chain that produces the source (patch scripts, `book.jsx`, `cutouts.jsx`) lives in the cloud workspace; the latest copy is `_workspace/book-build-2026-10-06b.tar.gz` (untracked backup; `STATE.md` inside it explains the chain).

---

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

## Project History & Reference (Phases 7–23)

*(Renamed 2026-07-21 — this was originally titled "Build Status", but it's actually a mix of
early build-status snapshots, the Phase 7–23 changelog, and reference material that's never
duplicated elsewhere: Supabase schema, deployment plan, helper functions, ABRSM architecture.
Kept as-is for that reference value. For current status, see "Current Status" at the end of
this file.)*

### Completed Features (Index.html)
| # | Feature | Status |
|---|---------|--------|
| 1 | Focus picker (FOCUS_GROUPS) | ✅ Done |
| 2 | Similar pieces (getSimilar scoring) | ✅ Done |
| 3 | My Interests panel (localStorage) | ✅ Done |
| 4 | Exam Readiness (List A/B/C check) | ✅ Done |
| 5 | Era Balance Advisor | ✅ Done |
| 6 | Nationality filter + NAT_LIST | ✅ Done |
| 7 | Mobile Responsive QA | ✅ Done |

### Mobile QA Changes Applied (2026-04-23)
- All grade HTML pages (Prelim–G8) + Index.html:
  - Button rows → `flex flex-col gap-2` + `flex flex-wrap gap-1.5` (no overflow on small screens)
  - Page headers → `flex flex-wrap items-start justify-between gap-3`
  - Viewport meta → added `viewport-fit=cover` (iOS safe area)
- Index.html stats row → `flex flex-wrap gap-2` with responsive padding

### Remaining Build Order
| # | Feature | Notes |
|---|---------|-------|
| 9 | Login gate | ✅ Done — Magic Link only (`signInWithOtp`), no password. Triggered only on ★ Save. |
| 10 | Stripe payment button | 🔜 Optional later via payments.html |
| 11 | Grade-up recommender | ✅ Done — GradeUpRecommender in index.html |
| 12 | Teacher Dashboard | ✅ Done — teacher-dashboard.html, Supabase DB backed. Deprioritized for public launch. |
| 13 | Sheet music links | ✅ Done (2026-04-29) — Google "sheet music" search on all Prelim–G8 HTML files + index.html |
| 14 | Claude API assistant | 🔜 Natural language search, requires backend |
| 15 | Progress Passport | ✅ Done (2026-04-29) — embedded in StudentDetail; period filter added |
| 16 | Fortnightly scheduling | ✅ Done (2026-04-29) — isFortnightWeek() helper |
| 17 | General track — remove planMonths | ✅ Done (2026-04-29) |
| 18 | Student pause/resume | ✅ Done (2026-04-29, enhanced 2026-04-30) |
| 19 | payments.html — lesson fee management | 🔜 Planned — per-student fee, invoice PDF, paid/unpaid toggle |
| 20 | Schedule week navigation | ✅ Done (2026-04-30) |
| 21 | Schedule calendar UX polish | ✅ Done (2026-04-30, further improved 2026-05-01) |
| 22 | Schedule reschedule (weekly override + permanent) | ✅ Done (2026-05-01, drag improved 2026-05-02) |
| 23 | Exam track refactor + flexible exam type | ✅ Done (2026-05-02) |
| 24 | Override revert UX (RevertConfirmPopover) | ✅ Done (2026-05-02) |
| 25 | ABRSM syllabus integration | ✅ Done (2026-05-04) — Initial–G8, 411 pieces, toggle on index.html, 182 title corrections |
| 26 | index.html public rewrite + Magic Link | ✅ Done (2026-05-04) — fully public, no login wall, 2,510-piece unified corpus |
| 27 | Auto-deploy GitHub Action | ✅ Done (2026-05-04) — push to main → auto-syncs gh-pages |
| 28 | SEO meta tags | ✅ Done (2026-05-05) — Open Graph, Twitter Card, canonical, keywords, robots |
| 29 | ABRSM missing pieces recovery (411→433) | ✅ Done (2026-05-05) — all 9 grades at 48 pieces; G5 List C has 17 per PDF |
| 30 | AMEB Diploma — AMusA repertoire | ✅ Done (2026-05-05) — 161 pieces, data_amusa.js + piano-repertoire_amusa.html |
| 31 | AMEB Diploma — LMusA repertoire | ✅ Done (2026-05-05) — 226 pieces, data_lmusa.js + piano-repertoire_lmusa.html |
| 32 | index.html diploma integration | ✅ Done (2026-05-05) — DIPLOMA_META, GradeGrid cards, corpus, sidebar filter |
| 33 | Admin piece-count page | 🔜 Password-protected internal page, owner-only |
| 31 | Ad integration | 🔜 Google AdSense / affiliate / direct piano brand deals |

### Deployment Plan (updated 2026-05-05)
- **Live:** https://vividssso-pixel.github.io/Piano-butler/
- **Stack:** GitHub Pages (auto-deploy via GitHub Actions on push to `main`) + Supabase Auth + Supabase DB (public.students + public.lesson_logs)
- **Deploy:** push to `main` → GitHub Actions → force-pushes to `gh-pages` branch → live in ~1 min
- **Auth pattern:** login.html → requireAuth() on each protected page → signOut()
- **Data:** All teacher/student/log data in Supabase DB with Row Level Security per user_id
- **GitHub:** https://github.com/vividssso-pixel/Piano-butler
- ⚠️ Netlify (https://exquisite-faloodeh-6d8e82.netlify.app) is NO LONGER USED — GitHub Pages only
- Do NOT use Wix — incompatible with React/Babel structure

### Supabase Schema (current as of 2026-05-02)

**`public.students` columns:**
```
id, user_id, name, grade, track, exam_date, plan_months, lesson_dur,
lesson_day, lesson_time, lesson_day2, lesson_time2,   ← lesson_day2/time2 added 2026-05-02
start_phase, created_at, extra (jsonb)
```

**`extra` jsonb blob fields (teacher-dashboard.html):**
```
startDate, grade, examType, lessonDuration2, customDuration, customDuration2,
lessonsPerWeek, termGoal, level, startingPhase,
paused, pausedAt, pauseUntil, pauseUndecided,
frequency (e.g. "fortnightly")
```

**`public.lesson_logs` columns:**
```
id, user_id, student_id, date, type, notes, sections (jsonb), created_at
```

**`public.lesson_overrides` columns:**
```
id, user_id, student_id, week_key (date, nullable), from_week (date, nullable),
slot_idx (int), day (text), time (text), created_at
```
- `week_key` set → single-week override; `from_week` set → permanent from that week
- Never both NULL — `saveOverride` guard enforces this
- After adding `from_week`: run `NOTIFY pgrst, 'reload schema';` in Supabase SQL editor

### Key Helper Functions (teacher-dashboard.html)

| Function | Purpose |
|----------|---------|
| `isExamStudent(s)` | `!!(s && s.examDate)` — replaces `track==="exam"` |
| `rowToStudent(r)` | DB row → React state; reads `extra` JSON first for `startDate`, `grade`, etc. |
| `studentToRow(f, userId)` | React form state → DB row; writes `startDate`/`grade` into `extra` blob |
| `getEffectiveOverride(studentId, slotIdx, weekKey)` | Priority: exact week match → latest `from/` override ≤ weekKey |
| `getWeekKey(offset)` | ISO Monday date for a given weekOffset |
| `isFortnightWeek(startDate, offset)` | Returns true if this week is an "on" week for fortnightly students |
| `fmtTime(t)` | `"14:00"` → `"2:00 PM"` |
| `hitTest(cx, cy)` | Pure DOM: maps viewport coords → `{ day, time, dayIdx, colW, rect, scrollLeft }` |
| `saveOverride({ weekKey, fromWeek, studentId, slotIdx, day, time, skip })` | Upserts to `lesson_overrides` Supabase table |
| `deleteOverride(key)` | Deletes override row by its local state key |

### Override Key Format

| Key format | Meaning |
|------------|---------|
| `"<isoMonday>/<studentId>/<slotIdx>"` | Single-week override (exact week_key match) |
| `"from/<isoMonday>/<studentId>/<slotIdx>"` | Permanent from that week onwards |

### Phase 7 Updates (2026-05-04)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | ABRSM syllabus added — Initial through Grade 8 | `ABRSM/` folder (18 new files) | 411 pieces initially extracted from official *ABRSM Piano 2025 & 2026* PDF via pdfplumber word-bbox parsing; recovered to 433 in Phase 9 (2026-05-05). Each grade has `data_abrsm_gX.js` + `piano-repertoire_abrsm_gX.html` (self-contained React 18 + Tailwind). ABRSM purple theme (`#7c3aed`). Features: List A/B/C tabs, Era chips, Nationality dropdown, search, YouTube + Google Sheet links, Wikipedia COMPOSER_LINKS. Back-link `../../Index.html`. |
| 2 | AMEB/ABRSM syllabus toggle on Index.html | `Index.html` | New `SyllabusGrid` React component (line ~189) replaces static AMEB-only grade grid. 🇦🇺 AMEB / 🇬🇧 ABRSM tab toggle. AMEB renders existing `GradeCard` components; ABRSM renders 9 violet-accented cards (Initial–G8) with List A/B/C chips. Fixes prior IIFE-based `React.useState` hook violation. |
| 3 | ABRSM title quality pass | All `data_abrsm_*.js` + `piano-repertoire_abrsm_*.html` (18 files) | 182 title corrections applied across all 9 grades: trailing `(from)` restored, truncated `Op./No./Vol.` numbers completed, spurious `Piano` word insertions removed, composer-name leakage into titles cleared, duplicate `Piano Piano` collapsed. All verified against PDF. |

### ABRSM Piece Counts (2026-05-05 — fully recovered)

| Grade | File | Total | List A | List B | List C |
|-------|------|-------|--------|--------|--------|
| Initial | data_abrsm_initial.js | 48 | 16 | 16 | 16 |
| G1 | data_abrsm_g1.js | 48 | 16 | 16 | 16 |
| G2 | data_abrsm_g2.js | 48 | 16 | 16 | 16 |
| G3 | data_abrsm_g3.js | 48 | 16 | 16 | 16 |
| G4 | data_abrsm_g4.js | 48 | 16 | 16 | 16 |
| G5 | data_abrsm_g5.js | 49 | 16 | 16 | 17 |  ← List C legitimately has 17 per PDF |
| G6 | data_abrsm_g6.js | 48 | 16 | 16 | 16 |
| G7 | data_abrsm_g7.js | 48 | 16 | 16 | 16 |
| G8 | data_abrsm_g8.js | 48 | 16 | 16 | 16 |
| **Total** | | **433** | | | | ← recovery complete (2026-05-05) |

### ABRSM Data Architecture

Each `data_abrsm_gX.js` follows the same schema as AMEB data but without `s` (series) or `key` fields:

```javascript
const DATA_ABRSM_G1 = [
  {
    "l": "A",              // List: A / B / C
    "c": "HANDEL",         // Composer — SURNAME, Firstname format
    "t": "Fireworks Minuet (from Music for the Royal Fireworks)",
    "nat": "German",       // Nationality
    "era": "Baroque",      // Era: Baroque / Classical / Romantic / Modern / Contemporary
    "focus": ["Baroque style", "Dance character", "Keyboard clarity"]  // exactly 3 keywords
  },
  ...
];
```

### ABRSM HTML App Architecture

Each `piano-repertoire_abrsm_gX.html` is a **self-contained single-file app**:
- React 18 + Babel + Tailwind CSS (CDN) — same stack as AMEB pages
- Data embedded **inline** (no external JS file needed)
- ABRSM violet theme: `#7c3aed`
- `nats` computed via `useMemo` from data (dynamic nationality list)
- Back-link: `../../Index.html`
- `COMPOSER_LINKS` object with Wikipedia URLs

### Remaining TODO (ABRSM)
| # | Task | Priority |
|---|------|----------|
| 1 | Recover missing 21 pieces (411 → 432) | Medium — PDF page-boundary parsing edge cases |
| 2 | payments.html — lesson fee management page | High |
| 3 | GitHub push → Netlify deploy | Done (2026-05-04) |

---

### Phase 8 Updates (2026-05-04 — same day, evening session)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | index.html complete rewrite — public access | `index.html` | Removed `requireAuth()` entirely. Page is now fully public — no login wall. Supabase client inlined (no longer depends on auth.js). `buildCorpus()` merges AMEB (2,099) + ABRSM (411) = **2,510 searchable pieces**, each tagged with `_syllabus: "AMEB"` or `_syllabus: "ABRSM"`. |
| 2 | Magic Link login modal | `index.html` | New `LoginModal` component — email only, no password. Uses `_sb.auth.signInWithOtp({ email, options: { emailRedirectTo: window.location.href } })`. Shows "Check your email ✉️" confirmation after send. Triggered only when user clicks ★ Save without a session. |
| 3 | Session-aware auth state | `index.html` | `useEffect` checks `_sb.auth.getSession()` on load. `onAuthStateChange` listens for Magic Link callback. `user` state drives Save button behaviour site-wide. |
| 4 | Save button (login-gated) | `index.html` | ★ button on each piece card. If no session → opens LoginModal. If logged in → saves to localStorage (`pb_interests_v2`) and optionally Supabase. |
| 5 | Sidebar filters | `index.html` | Left sidebar with: Syllabus (AMEB / ABRSM chips), Era chips, Grade dropdown, Nationality dropdown. All filters update search corpus in real time. |
| 6 | Minimal GradeGrid component | `index.html` | Clean grade cards — no piece counts shown publicly. AMEB/ABRSM toggle preserved. Piece counts moved to internal admin view (planned). |
| 7 | Branding cleaned up | `login.html`, `home.html` | Removed all "2026 AMEB" references. Updated to "Piano Repertoire · Exam & Studio" and "AMEB & ABRSM Piano Syllabus" — covers all major piano syllabuses. |
| 8 | 404 fix — case sensitivity | `home.html`, `teacher-dashboard.html`, `teacher-plan.html`, all 9 ABRSM HTML files | GitHub Pages (Linux) is case-sensitive. Fixed all `href="Index.html"` → `href="index.html"` across 11 files using grep + sed. |
| 9 | Auto-deploy GitHub Action | `.github/workflows/deploy.yml` | Created workflow: on push to `main` → `git push origin HEAD:gh-pages --force`. GitHub Actions bot pushes directly. Personal Access Token needed `workflow` scope (user enabled this). Now: `git push origin main` alone deploys the site. |
| 10 | Deployment pipeline confirmed live | Netlify + GitHub | Live URL: https://exquisite-faloodeh-6d8e82.netlify.app — public, no login wall. GitHub: https://github.com/vividssso-pixel/Piano-butler — auto-deploys on push to `main`. |

### Business Strategy Decision (2026-05-04)

**Pivot confirmed:** Piano Butler is now a **public repertoire search tool**, not a teacher-gated app.

| Pillar | Decision |
|--------|----------|
| Access model | Fully public — no login wall on index.html |
| Monetization | Ads: piano brands, sheet music publishers, lesson platform referrals |
| Login use | Magic Link only — triggered when saving pieces (low friction) |
| Teacher Dashboard | Deprioritized — kept in codebase but not promoted publicly |
| User acquisition | SEO + word of mouth — search "AMEB piano repertoire", "ABRSM grade 5 pieces" etc. |
| Revenue timeline | Gather users first → ads once traffic grows → Stripe optional later |

### index.html Architecture (as of Phase 8)

```
index.html (fully public, no requireAuth)
├── Supabase client (inline — not auth.js)
├── buildCorpus()           — merges AMEB + ABRSM, tags _syllabus field
├── useVideoModal()         — YouTube in-page modal hook
├── LoginModal              — Magic Link email form, no password
├── PieceRow                — piece card with ★ Save (login-gated)
├── GradeGrid               — AMEB/ABRSM tab toggle, clean grade cards
├── Sidebar                 — Syllabus / Era / Grade / Nationality filters
└── App
    ├── useEffect: _sb.auth.getSession() → setUser
    ├── onAuthStateChange subscription
    └── renders: <Sidebar> + <SearchBar> + <PieceRow list>
```

### Upcoming Next Steps (priority order)

| # | Task | Notes |
|---|------|-------|
| 1 | Test Magic Link end-to-end | Open site in incognito → click ★ → enter email → check inbox → verify session |
| 2 | SEO meta tags on index.html | `<meta name="description">`, Open Graph tags for social sharing |
| 3 | Admin piece-count page | Separate password-protected page showing grade-by-grade counts (for owner only) |
| 4 | ABRSM missing 21 pieces recovery | Manual audit of 9 grades against PDF — G2 missing 3, G3–G8 each missing 1–3 |
| 5 | Ad integration planning | Research: Google AdSense, Musicnotes affiliate, piano brand direct deals |
| 6 | payments.html — teacher fee tracking | Per-student lesson fee, invoice PDF, paid/unpaid toggle |

### Phase 11 Updates (2026-05-05)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | sitemap.xml — diploma pages added | `sitemap.xml` | AMusA + LMusA pages added (priority 0.8, monthly) |
| 2 | robots.txt — admin page blocked | `robots.txt` | `Disallow: /admin-counts.html` added |
| 3 | Admin piece-count page | `admin-counts.html` | Password-protected React dashboard. Shows live piece counts from all loaded data files. Grand Total card + per-syllabus subtotals. SectionTable with list badges + ✓ OK / ⚠ MISSING status. Expected vs Actual panel compares live counts to CLAUDE.md targets — red highlight on mismatch. `noindex` meta tag. |
| 4 | SEO keywords expanded | `index.html` | Added: AMusA repertoire, LMusA repertoire, AMEB diploma piano, ABRSM diploma piano, piano exam pieces Australia, piano syllabus search |
| 5 | Back-link added to all AMEB grade pages | `Prelim–G8/piano-repertoire_*.html` (9 files) | `← Piano Butler` link (`../index.html`) injected into header of all 9 AMEB Comprehensive/Leisure grade pages. ABRSM pages already had back-links. |
| 6 | ABRSM Diploma task logged | Task #7 | Pending — requires ABRSM Diploma PDF (ARSM / DipABRSM / LRSM / FRSM). User to download from abrsm.org → Performance Diplomas. |

---

### Phase 12 Updates (2026-05-05 — evening session)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Full system audit | All files | Ran complete audit of bugs found during user testing session. |
| 2 | G5 corpus silent bug fix | `index.html` | `GRADE_META` referenced `DATA_G5_1` but `G5/data_g5_1.js` exports `DATA_G5`. Result: 168 G5 pieces were silently absent from all search results. Fixed by correcting the variable reference to `DATA_G5`. |
| 3 | Footer piece count corrected | `index.html` | Footer showed stale "2,510" (pre-diploma count). Updated to "2,919 pieces". |
| 4 | admin-counts.html expected count fix | `admin-counts.html` | Expected Comprehensive count was `2099 - leisureTotal` (evaluated dynamically to wrong value). Fixed to hardcoded `1393`. |
| 5 | SEO meta tags — all 18 grade pages | `Prelim–G8/piano-repertoire_*.html` (9 files) + `ABRSM/*/piano-repertoire_abrsm_*.html` (9 files) | Added `<meta name="keywords">` and `<meta name="description">` to all 18 grade HTML pages via Python batch script. Descriptions include piece counts, syllabus name, and grade number. |
| 6 | Composer Wikipedia links restored on index.html | `index.html` | index.html was rebuilt without `COMPOSER_LINKS`. Extracted 414-entry object from grade pages and added to index.html. Both `PieceRow` and `ForYouPanel` `MiniCard` composer names now always render as clickable links with Wikipedia search fallback: `COMPOSER_LINKS[p.c] \|\| wikipedia search URL`. |
| 7 | Save button — login gate removed | `index.html` | ★ Save button no longer requires login. Any user can save pieces to localStorage without signing in. Login modal only shown if user manually clicks "Sign in" in the header. |
| 8 | interests state sync | `index.html` | `saveInterests()` now dispatches `window.dispatchEvent(new Event("pb_interests_changed"))`. App-level `interests` state has a `useEffect` listener that syncs via `loadInterests()` whenever PieceRow updates localStorage. ForYouPanel now reacts in real time. |
| 9 | focus field saved in interests | `index.html` | `focus: p.focus\|\|[]` added to interests object when saving a piece — required for ForYouPanel recommendation scoring. |
| 10 | For You recommendation engine | `index.html` | `getRecommendations(interests, corpus, count=5)` function added. Two modes: **More like this** (scores by era match, nationality match, focus tag overlap) and **Broaden your repertoire** (scores by least-listened era, unseen nationality, novel focus tags). Shuffled corpus for variety on each render. `ForYouPanel` component renders both sections below GradeGrid on homepage (only visible when `interests.length > 0`). |
| 11 | 🎓 Diploma filter — empty results bug fix | `index.html` | Clicking "🎓 Diploma" in sidebar showed "No pieces found". Root cause: `gradeFilter` retained previous value (e.g. `"G1"`) when switching syllabus. Diploma pieces have `_gradeKey: "AMusA"\|"LMusA"` — so grade filter blocked all results. Fix: syllabus filter buttons now also call `setGradeFilter("All")`. Deployed 2026-05-05. |

---

### Phase 13 Updates (2026-05-05 — late night)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | AMEB Leisure filter added to sidebar | `index.html` | Syllabus filter now has 5 options: All / 🇦🇺 AMEB Comprehensive / 🎵 AMEB Leisure / 🇬🇧 ABRSM / 🎓 Diploma. Previously Leisure pieces were in the corpus (`_type:"Leisure"`) but had no way to be filtered separately. Filter logic updated: `"AMEB"` → `_syllabus==="AMEB" && _type==="General"` only; `"AMEB Leisure"` → `_syllabus==="AMEB" && _type==="Leisure"` only. Each filter has its own accent colour (Leisure = `#0891b2`). Syllabus filter buttons also reset `gradeFilter` to "All" on click. |

---

---

### Phase 14 Updates (2026-05-06 — morning session)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | CertP (Certificate of Performance) added | `CertP/data_certp.js`, `CertP/piano-repertoire_certp.html` | 128 pieces (A:28, B:27, C:33, D:40) from 2026 AMEB Piano Syllabus pp.76–77. Teal gradient header (`#0f4c75` → `#0f766e`). Exam banner: Level 2, 45-min exam, 25–35 min programme, one work from each of Lists A/B/C/D. All pieces have exactly 3 focus keywords, nat, era fields. Verified with node count script. |
| 2 | index.html — CertP integrated | `index.html` | Script tag added: `<script src="CertP/data_certp.js"></script>`. CertP added first in `DIPLOMA_META` array (key:"CertP", accent:"#0f766e", bg:"#f0fdfa", examCode:"Level 2", program:"25–35 min"). Piece count updated 2,919 → 3,047 in all 4 meta/og/twitter tags. |
| 3 | Series badge added to search results | `index.html` | `PieceRow` now shows a series badge between List and Era badges when `p.s` field exists. Badge only appears on pieces that have a series code (AMEB Grade 1–8 pieces). CertP, Diploma, and ABRSM pieces have no `s` field → no badge shown. Colour-coded: S19=blue, S18=indigo, S17=violet, AustAnth=yellow, Manual=grey, Leisure S1–S4=green. IIFE pattern used inside JSX. |
| 4 | Logo button — home navigation | `index.html` | "Piano Butler" logo in top-left changed from `<div>` to `<button onClick={handleClear}>` with explicit `style={{background:"none",border:"none",padding:0,cursor:"pointer",position:"relative",zIndex:40}}`. Clicking resets all filters and returns to homepage. |
| 5 | admin-counts.html — CertP integrated | `admin-counts.html` | Script tag + DIPLOMA array entry added for CertP. Expected counts updated: AMEB Diploma + CertP total → 515, Grand Total → 3,047. |
| 6 | sitemap.xml — CertP page added | `sitemap.xml` | CertP URL added: `https://vividssso-pixel.github.io/Piano-butler/CertP/piano-repertoire_certp.html` (priority 0.8, monthly). |
| 7 | Diploma grid layout fix | `index.html` | `grid-cols-2` → `grid-cols-3` for Diploma Level cards. All three diploma cards (CertP, AMusA, LMusA) now appear in a single row. |

### CertP Repertoire — Verified Piece Counts

| List | Count | Character |
|------|-------|-----------|
| A | 28 | Studies & Baroque/Early — Scarlatti, Bach WTC, Cramer, Czerny, Handel, Hensel, Liszt, Moscheles, Moszkowski, Rameau, Schumann C., Shostakovich |
| B | 27 | Classical Sonatas/Suites — CPE Bach, JC Bach, JS Bach BWV814, Beethoven, Clementi, Haydn, Hummel, Méhul, Mozart, Poulenc, Sculthorpe, Sutherland |
| C | 33 | Romantic — Arensky, Bridge, Chopin x9, Fauré, Grieg, Hensel x5, Hill, Liszt x2, Mendelssohn, Rachmaninoff x4, Schubert, Schumann R. x4, Skryabin x2, Tchaikovsky |
| D | 40 | Modern/Contemporary — Albéniz x3, Bailey, Bartók x2, Benjamin, Boulanger, Chua, Copland x2, Debussy x6, Durham, Falla, Ginastera x2, Gould, Handel A., Holland x2, Kabalevsky, Khachaturian, Prokofiev x2, Ravel, Schoenberg, Sitsky, Stravinsky x2, Sutherland M., Villa-Lobos x5 |
| **Total** | **128** | |

### Updated Piece Count Totals (as of Phase 14)

| Syllabus | Count |
|----------|-------|
| AMEB Comprehensive (Prelim–G8) | 1,393 |
| AMEB Piano for Leisure (Prelim–G8) | 705 |
| AMEB Diploma — CertP | 128 |
| AMEB Diploma — AMusA | 161 |
| AMEB Diploma — LMusA | 226 |
| ABRSM Initial–G8 | 433 |
| **Grand Total** | **3,047** |

### File Structure Update

```
Piano Butler/
├── CertP/                           ← NEW (Phase 14)
│   ├── data_certp.js                ← CertP Diploma (128 pieces: A:28, B:27, C:33, D:40)
│   └── piano-repertoire_certp.html  ← Self-contained React app, teal theme
```

### Phase 15 Updates (2026-05-07)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | ABRSM LRSM diploma repertoire | `ABRSM/Diploma/data_abrsm_lrsm.js`, `ABRSM/Diploma/piano-repertoire_abrsm_lrsm.html` | 139 entries from *Piano LRSM Repertoire [7 Nov 2023] FINAL.pdf*. Open pool format (no lists). ABRSM violet theme (`#7c3aed`). Era/Nationality filters, search, YT + Sheet links, Wikipedia COMPOSER_LINKS. Back-link to index.html. |
| 2 | ABRSM FRSM diploma repertoire | `ABRSM/Diploma/data_abrsm_frsm.js`, `ABRSM/Diploma/piano-repertoire_abrsm_frsm.html` | 97 entries from *Piano FRSM Repertoire [7 Nov 2023] FINAL.pdf*. Same open pool pattern. Deeper purple theme (`#4c1d95`). |
| 3 | index.html — LRSM & FRSM integration | `index.html` | Script tags added. `DIPLOMA_META` gains LRSM + FRSM entries (`_syllabus:"ABRSM Diploma"`). Sidebar filter gains "🎓 ABRSM Diploma" option. GradeGrid Diploma section shows LRSM/FRSM cards under ABRSM tab. Filter logic updated with `ABRSM Diploma` case. Piece count 3,047 → 3,283. Footer updated. |
| 4 | sitemap.xml | `sitemap.xml` | LRSM + FRSM pages added (priority 0.8, monthly). |
| 5 | admin-counts.html | `admin-counts.html` | Script tags + DIPLOMA array entries added for LRSM + FRSM. Grand Total expected updated to 3,283. ABRSM Diploma row (236) added to Expected vs Actual panel. |
| 6 | CLAUDE.md | `CLAUDE.md` | Phase 15 logged. File structure, piece counts, and pending work updated. |

### ABRSM Diploma Piece Counts (Phase 15)

| Diploma | File | Total | Format | Valid from |
|---------|------|-------|--------|------------|
| LRSM | data_abrsm_lrsm.js | 139 | Open pool | Nov 2023 |
| FRSM | data_abrsm_frsm.js | 97 | Open pool | Nov 2023 |
| **Total** | | **236** | | |

> Note: ARSM and DipABRSM PDFs not yet available. LRSM + FRSM only for now.

### Updated Piece Count Totals (as of Phase 15)

| Syllabus | Count |
|----------|-------|
| AMEB Comprehensive (Prelim–G8) | 1,393 |
| AMEB Piano for Leisure (Prelim–G8) | 705 |
| AMEB Diploma — CertP | 128 |
| AMEB Diploma — AMusA | 161 |
| AMEB Diploma — LMusA | 226 |
| ABRSM Initial–G8 | 433 |
| ABRSM Diploma — LRSM | 139 |
| ABRSM Diploma — FRSM | 97 |
| **Grand Total** | **3,283** |

### File Structure Update (Phase 15)

```
ABRSM/
└── Diploma/                          ← NEW (Phase 15)
    ├── data_abrsm_lrsm.js            ← LRSM (139 entries)
    ├── piano-repertoire_abrsm_lrsm.html
    ├── data_abrsm_frsm.js            ← FRSM (97 entries)
    └── piano-repertoire_abrsm_frsm.html
```

### Phase 16 Updates (2026-05-07 — afternoon)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Coloured list tabs with piece counts — all AMEB grade pages | `Prelim–G8/piano-repertoire_*.html` (9 files) | `tabColors` object covers A/B/C/D/Collab/S1/S2/S3/S4/Manual. Each tab button shows list label + piece count as two-line display. Comprehensive tabs: A=blue, B=indigo, C=violet, D=purple, Collab=pink. Leisure series tabs: S4=teal, S3=cyan, S2=sky, S1=green, Manual=slate. |

### Phase 17 Updates (2026-05-07 — evening)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Instant search (keystroke-triggered) | `index.html` | Removed Enter-key requirement for text queries. `onChange` directly activates results via `searchActive = query.trim() \|\| ...`. Empty query clears `searchTriggered`. |
| 2 | Autocomplete suggestions dropdown | `index.html` | `autoSuggestions` useMemo fires when query ≥ 2 chars. Returns up to 8 results: 4 composer matches + 4 title matches from full corpus. Dark dropdown anchored to search input. `composer` badge (indigo) / `title` badge (cyan). Click on suggestion fills query + triggers results. Closes on blur (150ms delay for click handling). |
| 3 | Quick search chips on homepage | `index.html` | 14 chips below GradeGrid: Chopin, Bach, Debussy, Beethoven, Romantic, Baroque, Australian, Contemporary, French, Russian, Sonatina, Waltz, Mazurka, Nocturne. Era chips set `eraFilter`; name chips set `query`. All trigger results instantly. |
| 4 | Active filter pills in results header | `index.html` | When results are active, shows colour-coded pill badges for current query + each active filter. "clear filters" link appears next to result count when any filter is active. |
| 5 | Smart "no results" UI | `index.html` | Shows query name in message, "Clear all filters" button if any filter active, and 6 suggested composer name chips (Chopin, Bach, Beethoven, Debussy, Schubert, Brahms). |
| 6 | Search placeholder updated | `index.html` | Changed to "Search composer, title, nationality…" to communicate search scope. |

### Phase 18 Updates (2026-05-07 — night)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Smart query parser (`parseQuery`) | `index.html` | Extracts grade / era / nationality / syllabus signals from free text before keyword search. Maps: GRADE_MAP (prelim/g1–g8/amusa/lmusa/certp/lrsm/frsm), ERA_MAP (baroque/classical/romantic/modern/contemporary + aliases), NAT_MAP (australian/french/german/russian/english etc.), SYLLABUS_MAP (ameb/abrsm/diploma etc.). Multi-word patterns matched longest-first. |
| 2 | Multi-token AND matching | `index.html` | Query split into tokens after signal extraction. Every token must match at least one field (title, composer, nationality, era, **or focus array**). Previously single string `.includes()` — now all tokens must hit, e.g. "bach minuet" returns only Bach pieces with "Minuet" in title. |
| 3 | Focus field search | `index.html` | `p.focus` array now included in token matching. Queries like "finger independence", "voicing", "pedalling" now return relevant results. |
| 4 | Fuzzy composer matching (Levenshtein ≤ 1) | `index.html` | Each token checked against all known composer surnames. Typos like "Chopn", "Debussi", "Beetoven" auto-corrected before search. Distance threshold = 1 edit. |
| 5 | Auto-detected signal pills | `index.html` | When `parseQuery` extracts grade/era/nat/syllabus from query text, dashed-border hint pills appear in results header (e.g. `↳ Romantic`, `↳ G5`, `↳ French`) — distinct from solid sidebar filter pills. |
| 6 | Effective filter merging | `index.html` | `effEra/effGrade/effNat/effSyllabus` — sidebar filter takes priority; parsed signal used as fallback. Allows "grade 5 romantic" to work even when sidebar is on "All". |

### Phase 19 Updates (2026-05-07 — night)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | `repertoire_lists` + `list_pieces` Supabase tables | Supabase SQL | `repertoire_lists`: id, user_id, name, is_public, share_token (auto-generated 10-char), created_at. `list_pieces`: id, list_id, composer, title, grade, syllabus, era, nat, added_at. RLS: owner full access; public can read is_public=true lists + their pieces. |
| 2 | `ListModal` component | `index.html` | Dark modal: shows user's existing lists + create-new-list input. "+ Add" button per list → inserts into list_pieces. "✓ Added" confirmation. Triggered by "+ List" button on PieceRow. |
| 3 | `MyListsPage` component | `index.html` | Full modal panel: list of user's lists → click to drill into pieces. "🔗 Share link" copies `?list=<token>` URL to clipboard. Per-piece ✕ remove button. Delete list button. |
| 4 | `SharedListPage` inline view | `index.html` | Reads `?list=<token>` URL param on load. Fetches public list + pieces from Supabase. Renders full-page shareable list (no login needed). ▶ YouTube button per piece. "Explore 3,283 pieces on Piano Butler →" CTA at bottom. |
| 5 | "+ List" button on PieceRow | `index.html` | Indigo button next to ★ Save. Opens LoginModal if not logged in; opens ListModal if logged in. |
| 6 | "📋 My Lists" nav button | `index.html` | Shown in header when user is logged in. Opens MyListsPage modal. |
| 7 | Login gate for list features | `index.html` | handleAddToList() checks user state — triggers Magic Link modal if not signed in. Core mechanism for email collection. |

### Supabase Schema Update (Phase 19)

```sql
-- New tables added 2026-05-07
CREATE TABLE public.repertoire_lists (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id uuid REFERENCES auth.users(id) ON DELETE CASCADE,
  name text NOT NULL,
  description text,
  is_public boolean DEFAULT true,
  share_token text UNIQUE DEFAULT substr(md5(random()::text), 1, 10),
  created_at timestamptz DEFAULT now()
);
CREATE TABLE public.list_pieces (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  list_id uuid REFERENCES public.repertoire_lists(id) ON DELETE CASCADE,
  composer text, title text, grade text, syllabus text, era text, nat text,
  added_at timestamptz DEFAULT now()
);
-- RLS: owner full, public read on is_public=true
```

### Phase 20 Updates (2026-05-08 — morning)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Search UX redesign — minimal aesthetic | `index.html` | White background, border-based piece rows (no shadows), simplified nav, `.prompt-card` / `.sidebar-label` / `.filter-btn` CSS classes. |
| 2 | Guided discovery prompts | `index.html` | "What are you looking for?" section with 8 scenario cards above grade grid. |
| 3 | PieceRow redesign | `index.html` | Star button top-right, cleaner badges, minimal action buttons (Listen / Score / + List). |

### Phase 21 Updates (2026-05-08)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Local-first list system | `index.html` | `LISTS_KEY = "pb_lists_v1"` in localStorage. Helpers: `loadLists`, `saveLists`, `createLocalList`, `addPieceToList`, `removePieceFromList`, `deleteList`, `updateList`. Custom event `pb_lists_changed` for sync. |
| 2 | `LIST_TYPES` — 4 categories | `index.html` | Student (indigo), Concert (teal), Exam (amber), General (slate). |
| 3 | `AddToListModal` (replaces `ListModal`) | `index.html` | No login required. Existing local lists with type badges, inline create form (name + type + description). One-action "Create & add". |
| 4 | `MyListsPanel` (replaces `MyListsPage`) | `index.html` | Slide-in right panel. Lists grouped by type. Detail view, inline edit, Print/PDF export, Share via base64 URL (`?locallist=…`), delete, remove pieces. Login upsell for sync/share upgrade. |
| 5 | Login gate removed from list creation | `index.html` | `handleAddToList()` no longer requires login — any visitor can create lists locally. |
| 6 | "My Lists" nav button always visible | `index.html` | Shown for all users. `data-signin` on Sign in button for upsell targeting. |

### Phase 22 Updates (2026-05-08)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Google-style minimal homepage | `index.html` | Pre-search screen: logo + subtitle + large centered search bar + 8 quiet hint chips + bottom links. Grade grid, prompt cards, ForYouPanel all removed. |
| 2 | Nav hidden on homepage | `index.html` | Top nav only renders when `searchActive === true`. Clean blank canvas until user searches. |
| 3 | Sidebar hidden on homepage | `index.html` | Filter sidebar and mobile filter strip only appear in results mode. |
| 4 | Large search bar with glow | `index.html` | `borderRadius:28`, `fontSize:15`, indigo glow on focus. Autocomplete preserved. |
| 5 | Hint chips — minimal | `index.html` | 8 chips (Chopin, Bach, Romantic, Australian, Grade 5, Diploma, ABRSM, Debussy). Grey default, indigo hover, no fill. |

### Language Rule
- Conversation: Korean is fine
- All code, file outputs, comments: English only

---

### Phase 23 Updates (2026-05-10 — design session)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Reverted Google-style homepage | `index.html` | Restored Phase 21 version (grade grid visible on load). Google-style blank canvas felt too empty — grade grid gives immediate context. |
| 2 | Grade card redesign | `index.html` | 3-col grid, fixed 80px height, left color bar per grade accent, subtle color background (`accent + "0d"`), text bottom-aligned. |
| 3 | Hero search bar on homepage | `index.html` | Large search input (15px, padding 14px, border-radius 14px) placed above grade grid. Nav search bar hidden (`invisible`) on homepage — only appears in results mode. |
| 4 | PieceRow simplified | `index.html` | Removed focus chips entirely. Badges smaller (9px). Inline layout (text left, star right). Buttons smaller (10px). Card style changed to borderless with bottom divider. |
| 5 | Sidebar cleanup | `index.html` | Reduced section spacing, smaller label font, "Filters" header instead of "FILTER". |
| 6 | Removed guided discovery prompts | `index.html` | 8 prompt cards removed — clutter without clear value. |
| 7 | Removed popular search chips | `index.html` | Chips below grade grid removed — cleaner homepage. |

---

## Product Direction (decided 2026-05-10)

### Core insight
Piano Butler's "can't live without" feature is **curated teaching lists** — not just search.

The problem piano teachers actually have:
> "Finding pieces that are technically achievable, sound impressive, and that students will enjoy" — this relies entirely on years of personal experience and memory.

### The real value
**Sohyun's teaching philosophy in action:**
- Start with pieces that have clear technical goals AND student appeal (Wild Chase → Going Baroque → Malagueña)
- Build momentum through small wins and a sense of accomplishment
- Piece selection IS the curriculum — wrong piece = student quits

### Product evolution path

**Stage 1 — Teaching Lists (next session)**
Upgrade My Lists → Teaching Lists:
- Ordered sequence (drag to reorder, numbered)
- Per-piece teacher note ("focus on legato, 2-week goal")
- Grade range tag on the list ("Prelim–G2")
- Share link shows order + notes (currently notes are lost on share)

**Stage 2 — Sohyun's curated lists (after Stage 1)**
- Build 3–5 real teaching sequences from Sohyun's experience
- Show as "Featured Lists" on homepage
- First-time visitors immediately understand the value

**Stage 3 — Community (when traffic grows)**
- Other teachers can publish their lists publicly
- Homepage shows curated feed of teacher lists
- Becomes a living resource, not just a database

### Why this works
- Sohyun uses it herself → honest feedback loop
- Teacher's curated list = value for students too (pass knowledge down)
- Community of lists = reason to come back, reason to share

### Next session action items
1. Try creating a real list in My Lists (Wild Chase → Going Baroque → Malagueña)
2. Note exactly what's missing/annoying in the current UI
3. Build: ordered list + per-piece notes + improved share view
4. Design: homepage "Featured Lists" section

### Phase 24 Updates (2026-05-10 — search performance session)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Removed Levenshtein fuzzy matching | `index.html` | `parseQuery` + `FUZZY_COMPOSERS` + Levenshtein distance function fully removed. Was rebuilding composer surname list and running edit-distance on every keystroke — major lag source. |
| 2 | Replaced parseQuery with simple includes | `index.html` | Results filtering now uses single `string.includes(q)` against title, composer, nat, era. No tokenization, no signal detection. Much faster. |
| 3 | Decoupled input display from search filtering | `index.html` | Added `searchQuery` state (separate from `query`). `query` updates instantly on every keystroke (input feels responsive). `searchQuery` updates after 200ms idle via useEffect debounce. `searchActive`, `results` useMemo both depend on `searchQuery` — filtering never runs mid-keystroke. Root cause of English lag: every keystroke triggered `searchActive=true` via `query.trim()`, which fired 3,283-piece filter. Fixed by tying `searchActive` to `searchQuery` instead. |
| 4 | Single search bar | `index.html` | Removed nav search bar (duplicate). Now one search bar always visible above grade grid. No page-transition animation — results appear inline below search bar. Grade grid hidden only while results are active. |
| 5 | Removed screen transition | `index.html` | Previous design had home→results layout switch that felt slow. Now grade grid stays in place; results replace it in-line with no React re-layout. |

### Search Architecture (as of Phase 24)

```
query state        → input value (instant, every keystroke)
searchQuery state  → debounced 200ms → drives results + searchActive
results useMemo    → depends on [searchQuery, eraFilter, gradeFilter, natFilter, syllabusFilter, searchActive]
                   → simple includes() match on title/composer/nat/era
autoSuggestions    → depends on [query] — fires on keystroke for dropdown
```

### Phase 25 Updates (2026-05-13 — Trinity integration)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Trinity College London syllabus added — Initial through Grade 8 | `Trinity/` folder (18 new files) | 516 pieces scraped from trinitycollege.com 2023 syllabus. Each grade has `data_trinity_gX.js` + `piano-repertoire_trinity_gX.html` (self-contained React 18 + Tailwind). Trinity crimson theme (`#b91c1c`). Initial–G5: flat open pool (no groups). G6–G8: Group A (Baroque/Classical/early) + Group B (Romantic/Contemporary) filter tabs. Features: Era chips, Nationality dropdown, search, YouTube + Google Sheet links, Wikipedia COMPOSER_LINKS. Back-link to index.html. |
| 2 | index.html — Trinity integration | `index.html` | Script tags for all 9 Trinity data files. `TRINITY_META` array. `buildCorpus()` now includes Trinity tagged `_syllabus:"Trinity"`. GradeGrid gains "Trinity" tab (crimson cards, links to HTML pages). Sidebar filter + mobile strip gains `🇬🇧 Trinity` option. syllabusFilter logic updated. syllabusColor updated. Piece count 3,283 → 3,799 across all meta/og/twitter/footer tags. |
| 3 | sitemap.xml — Trinity pages added | `sitemap.xml` | All 9 Trinity URLs added (priority 0.8, monthly). |
| 4 | admin-counts.html — Trinity integrated | `admin-counts.html` | Script tags + `TRINITY` array + `SectionTable` + grand total + Expected vs Actual row (expected 516). Grand Total target updated 3,283 → 3,799. |
| 5 | CLAUDE.md updated | `CLAUDE.md` | Phase 25 logged. Project overview, piece counts, file structure, pending work all updated. |

### Trinity Piece Counts (Phase 25)

| Grade | File | Total | Format |
|-------|------|-------|--------|
| Initial | data_trinity_initial.js | 56 | Open pool |
| Grade 1 | data_trinity_g1.js | 57 | Open pool |
| Grade 2 | data_trinity_g2.js | 56 | Open pool |
| Grade 3 | data_trinity_g3.js | 57 | Open pool |
| Grade 4 | data_trinity_g4.js | 56 | Open pool |
| Grade 5 | data_trinity_g5.js | 58 | Open pool |
| Grade 6 | data_trinity_g6.js | 59 | Group A: 24, Group B: 35 |
| Grade 7 | data_trinity_g7.js | 58 | Group A: 23, Group B: 35 |
| Grade 8 | data_trinity_g8.js | 59 | Group A: 25, Group B: 34 |
| **Total** | | **516** | |

### Updated Piece Count Totals (as of Phase 25)

| Syllabus | Count |
|----------|-------|
| AMEB Comprehensive (Prelim–G8) | 1,393 |
| AMEB Piano for Leisure (Prelim–G8) | 705 |
| AMEB Diploma — CertP | 128 |
| AMEB Diploma — AMusA | 161 |
| AMEB Diploma — LMusA | 226 |
| ABRSM Initial–G8 | 433 |
| ABRSM Diploma — LRSM | 139 |
| ABRSM Diploma — FRSM | 97 |
| Trinity College London Initial–G8 | 516 |
| **Grand Total** | **3,799** |

### File Structure Update (Phase 25)

```
Trinity/                              ← NEW (Phase 25)
├── Initial/
│   ├── data_trinity_initial.js       ← 56 pieces
│   └── piano-repertoire_trinity_initial.html
├── G1/ … G5/                         ← same pattern, flat pool
├── G6/
│   ├── data_trinity_g6.js            ← 59 pieces (Group A: 24, Group B: 35)
│   └── piano-repertoire_trinity_g6.html  ← Group A/B tab filter
├── G7/
│   ├── data_trinity_g7.js            ← 58 pieces (Group A: 23, Group B: 35)
│   └── piano-repertoire_trinity_g7.html
└── G8/
    ├── data_trinity_g8.js            ← 59 pieces (Group A: 25, Group B: 34)
    └── piano-repertoire_trinity_g8.html
```

---

### Phase 26 Updates (2026-05-13 — bug fixes + UX)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Series badge added to search results | `index.html` | `PieceRow` now renders a series badge when `p.s` field exists. Manual=slate, S19=blue, S18=indigo, S17=violet, AustAnth=yellow, S1–S4=green. IIFE pattern inside JSX. Commit `9ac7b1d`. |
| 2 | Trinity grade filter bug fix | `index.html` | Grade filter was always showing AMEB keys (Prelim/G1–G8). Selecting Trinity syllabus now renders Trinity grade keys (TInitial, TG1–TG8). `gradeKeys` useMemo + `gradeLabel()` helper added. Commit `d102429`. |
| 3 | Syllabus filter emoji/flag icons | `index.html` | All syllabus filter labels now have icons: 🇦🇺 AMEB Comprehensive, 🎵 AMEB Leisure, 🇬🇧 ABRSM, 🎓 AMEB Diploma, 🎓 ABRSM Diploma, 🇬🇧 Trinity. Applied to sidebar + mobile panel. Commit `f06fd35`. |

### Phase 27 Updates (2026-05-13 — search UX + data audit session)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Multi-token AND search | `index.html` | Query split into tokens on whitespace. Every token must match at least one field (title, composer, nat, era, focus). Previously single-string includes — `"bach minuet"` returned 0 results. Now returns correctly. |
| 2 | focus field included in search | `index.html` | `p.focus` array now joined and searched per token. Queries like `"finger independence"`, `"voicing"` now return results. |
| 3 | Syllabus badge on piece cards | `index.html` | `syllabusBadge` computed per piece. Always-visible coloured pill before Grade badge: AMEB=indigo, ABRSM=violet, Trinity=crimson, AMEB Leisure=cyan, AMEB Diploma=teal, ABRSM Diploma=deep purple. |
| 4 | Autocomplete — era/nationality/focus hints | `index.html` | `autoSuggestions` useMemo extended to include era (🕰️), nationality (🌍), focus (🎯) matches in addition to composer (🎼) and title (🎵). Priority order: era > composer > nationality > title > focus, cap 8. Badge colour per type. |
| 5 | AMEB data audit — ERA fixes | `G5/data_g5_1.js`, `G5/data_g5_leisure.js`, `G6/data_g6_leisure.js` | 23 invalid era values corrected: `"Classical-Romantic"` → `"Classical"`, `"Modern-Jazz"` / `"Contemporary-Jazz"` → `"Modern"` / `"Contemporary"`, `"Modern-Contemporary"` → `"Contemporary"`, `"Traditional"` → `"Contemporary"` / `"Modern"` / `"Romantic"` as appropriate. |
| 6 | AMEB data audit — FOCUS fixes | `G5/data_g5_leisure.js`, `G6/data_g6_leisure.js` | 166 pieces with 2-item focus arrays fixed: 3rd pedagogical keyword added to all 78 G5 Leisure + all 88 G6 Leisure pieces. |
| 7 | AMEB data audit — NAT fix | `G4/data_g4_leisure.js` | ANONYMOUS - Allegro: `nat: ""` → `"Unknown"`. |
| 8 | ERA nat fix — Traditional folk pieces | `G6/data_g6_leisure.js` | Go tell it on the mountains: `nat: "Traditional"` → `"American"`. Danny boy: `nat: "Traditional"` → `"Irish"`. |

### AMEB Data Audit Status (2026-05-13)

| Check | Result |
|-------|--------|
| Piece counts (all 18 files) | ✅ All match CLAUDE.md targets exactly |
| ERA validity | ✅ All 2,099 pieces have valid era |
| FOCUS length = 3 | ✅ All 2,099 pieces have exactly 3 focus keywords |
| NAT not empty | ✅ All pieces have nationality |
| Duplicates | ⚠️ 1 pending: G8 Leisure BEETHOVEN Andante appears in S4 and S1 — needs PDF verification |

### Phase 28 Updates (2026-05-13 — Trinity Diploma integration)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Trinity ATCL diploma repertoire | `Trinity/Diploma/data_trinity_atcl.js`, `Trinity/Diploma/piano-repertoire_trinity_atcl.html` | 241 works from official *Trinity Piano Diploma Repertoire List 2026* PDF (trinitycollege.com/resource?id=8546). Open pool format. Crimson-dark gradient header. Era/Nationality filters, search, YT + Sheet links, Wikipedia COMPOSER_LINKS. |
| 2 | Trinity LTCL diploma repertoire | `Trinity/Diploma/data_trinity_ltcl.js`, `Trinity/Diploma/piano-repertoire_trinity_ltcl.html` | 306 works. Same open pool pattern. Purple-crimson gradient. |
| 3 | Trinity FTCL diploma repertoire | `Trinity/Diploma/data_trinity_ftcl.js`, `Trinity/Diploma/piano-repertoire_trinity_ftcl.html` | 155 works. Deep purple header. FTCL note: concertos permitted (with second piano). |
| 4 | index.html — Trinity Diploma integration | `index.html` | `TRINITY_DIPLOMA_META` array added. Script tags for all 3 diploma JS files. `buildCorpus()` includes Trinity Diploma tagged `_syllabus:"Trinity Diploma"`. GradeGrid Trinity tab shows ATCL/LTCL/FTCL diploma cards. Sidebar + mobile strip gain `🎓 Trinity Diploma` filter. syllabusBadge + syllabusColor updated. Piece count updated 3,799 → 4,500. |
| 5 | admin-counts.html | `admin-counts.html` | Script tags + `TRINITY_DIPLOMA` array + `SectionTable` + grand total + Expected vs Actual row (702 total). Grand Total target updated 3,799 → 4,501. |
| 6 | sitemap.xml | `sitemap.xml` | 3 Trinity Diploma URLs added (priority 0.8, monthly). |
| 7 | CLAUDE.md | `CLAUDE.md` | Phase 28 logged. Project overview, piece counts, file structure, pending work updated. |

### Trinity Diploma Piece Counts (Phase 28)

| Diploma | File | Total | Format | Performance |
|---------|------|-------|--------|-------------|
| ATCL | data_trinity_atcl.js | 241 | Open pool | 32–38 min |
| LTCL | data_trinity_ltcl.js | 306 | Open pool | 37–43 min |
| FTCL | data_trinity_ftcl.js | 155 | Open pool | 42–48 min |
| **Total** | | **702** | | |

> Source: [Trinity Piano Diploma Repertoire List 2026](https://www.trinitycollege.com/resource?id=8546). Own-choice programmes must be pre-approved by Trinity.

### Updated Piece Count Totals (as of Phase 28)

| Syllabus | Count |
|----------|-------|
| AMEB Comprehensive (Prelim–G8) | 1,393 |
| AMEB Piano for Leisure (Prelim–G8) | 705 |
| AMEB Diploma — CertP | 128 |
| AMEB Diploma — AMusA | 161 |
| AMEB Diploma — LMusA | 226 |
| ABRSM Initial–G8 | 433 |
| ABRSM Diploma — LRSM | 139 |
| ABRSM Diploma — FRSM | 97 |
| Trinity College London Initial–G8 | 516 |
| Trinity Diploma — ATCL | 241 |
| Trinity Diploma — LTCL | 306 |
| Trinity Diploma — FTCL | 155 |
| **Grand Total** | **4,500** |

### File Structure Update (Phase 28)

```
Trinity/
└── Diploma/                                    ← NEW (Phase 28)
    ├── data_trinity_atcl.js                    ← ATCL (241 works)
    ├── piano-repertoire_trinity_atcl.html
    ├── data_trinity_ltcl.js                    ← LTCL (306 works)
    ├── piano-repertoire_trinity_ltcl.html
    ├── data_trinity_ftcl.js                    ← FTCL (155 works)
    └── piano-repertoire_trinity_ftcl.html
```

### Phase 29 Updates (2026-05-13 — Recommender session)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Repertoire Recommender page created | `recommend.html` | Self-contained React 18 + Tailwind app. 6-step form wizard: mode → syllabus → grade → combo type → character → era → nationality → results. Scoring engine: era match (+30), character focus keyword match (+25), nationality preference (+20), random variety (+15). Era diversity + nationality diversity bonus in `pickDiverse()`. |
| 2 | Two recommendation modes | `recommend.html` | **Exam mode**: filters corpus by syllabus + grade, picks one piece per list (A/B/C/D). **Free discovery**: searches all 4,500 pieces, no syllabus/grade constraint. |
| 3 | YouTube in-page modal | `recommend.html` | ▶ Listen button opens YouTube video inside a dark overlay modal — same pattern as index.html. Uses YouTube Data API v3 for video search. |
| 4 | 🎹 Recommend button in header | `index.html` | Indigo pill button added to top nav, links to recommend.html. |
| 5 | Free mode step routing fix | `recommend.html` | Free discovery jumps step 0→3 (skips syllabus/grade steps 1+2). `mode === 'exam'` guard on step 1 and step 2 render blocks. `nextStep()` helper handles branching. |

### recommend.html Architecture

```
recommend.html
├── buildCorpus()          — loads all 4,500 pieces from all data files
├── scorepiece(p, prefs)   — scores each piece by era/character/nationality match
├── pickDiverse(scored, n) — picks n pieces with era+nationality diversity bonus
├── generateCombination()  — exam mode: filters by syllabus+grade, picks by list (A/B/C/D)
├── generateFreeMode()     — free mode: scores entire corpus, picks diverse set
├── useVideoModal()        — YouTube Data API v3 search → in-page iframe modal
├── ResultCard             — piece card with list badge, era, reasons, focus tags, ▶ Listen, ♩ Score
└── App (6-step wizard)
    ├── Step 0: mode picker (Exam / Free discovery)
    ├── Step 1: syllabus — AMEB / ABRSM / Trinity [exam mode only]
    ├── Step 2: grade — Prelim–G8 / Diploma [exam mode only]
    ├── Step 3: programme type — Exam 3/4 pieces or Lesson 4/6 pieces
    ├── Step 4: student personality — Technical / Expressive / Playful / Balanced
    ├── Step 5: era preference — Baroque / Classical / Romantic / Modern / Contemporary
    ├── Step 6: nationality diversity — Any / Varied / Western / Australian
    └── Step 7: results — scored combination + 🔀 regenerate
```

### Phase 30 Updates (2026-05-14 — Diagnosis System MVP)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Piano Diagnosis MVP | `diagnose.html` | Self-contained React 18 + Tailwind page. 16 plain-language questions across 4 domains (Ear, Sight-reading, Technique, Theory). 4 questions per domain, scored Always/Usually/Sometimes/Rarely → 4/3/2/1. Score bands: 13–16 Strong, 8–12 Developing, 4–7 Needs work. |
| 2 | SVG radar chart | `diagnose.html` | Pure SVG 4-axis diamond polygon. Grid rings at 25/50/75/100%. Data polygon filled indigo. Score labels per axis. No Chart.js dependency. |
| 3 | Repertoire matching engine | `diagnose.html` | `pickPieces(domain, band, count)` filters live 4,500-piece corpus by domain weakness. Ear → Baroque/Classical + melodic focus tags. Sight → Baroque/Classical + rhythm/pulse tags. Technique → étude/finger/articulation/pedal focus tags. Theory → Bach/Haydn/Mozart/Beethoven + Baroque/Classical era. Era diversity bonus in selection loop. |
| 4 | Weakness explanation cards | `diagnose.html` | `WEAKNESS_TIPS` object — per-domain: what it means, quick fix, piece type rationale. Shown for bottom 2 domains only. |
| 5 | Estimated level (by-product) | `diagnose.html` | `estimatedLevel(scores)` maps average score → Beginner/Prelim through Diploma/Advanced. Shown as secondary info in results header, not as primary framing. |
| 6 | Coming Soon modal | `diagnose.html` | "$4 Full Report" CTA opens modal with waitlist mailto link (`vividssso@gmail.com`). Placeholder for future Stripe + jsPDF integration. |
| 7 | 🔬 Diagnose button in nav | `index.html` | Amber pill button added to top nav, left of 🎹 Recommend. Links to `diagnose.html`. |
| 8 | ErrorBoundary | `diagnose.html` | `class ErrorBoundary` wraps `<App/>` — shows error + stack trace on crash instead of blank screen. |

### diagnose.html Architecture

```
diagnose.html
├── buildCorpus()          — loads all 4,500 pieces (same as recommend.html)
├── DOMAINS (4)            — Ear / Sight-reading / Technique / Theory
├── QUESTIONS (16)         — 4 per domain, plain language, with hint
├── OPTIONS (4)            — Always(4) / Usually(3) / Sometimes(2) / Rarely(1)
├── scoreDomain()          — sums answers for a domain
├── bandFor(score)         — Strong / Developing / Needs work
├── estimatedLevel(scores) — average → grade range string
├── pickPieces(domain, n)  — corpus filter + era diversity selection
├── RadarChart             — pure SVG 4-axis polygon
├── PieceCard              — piece card with composer Wikipedia link + focus tags
├── ComingSoonModal        — $4 report waitlist CTA
├── DomainCard             — intro screen domain cards
├── WEAKNESS_TIPS          — per-domain explanations + quick fix advice
└── App (5 screens)
    ├── landing            — gradient hero, "Start the diagnosis →"
    ├── intro              — 4 domain cards, "Begin 16 questions →"
    ├── quiz               — question cards, auto-advance, progress dots, go back
    ├── processing         — spin animation, 5 sequential messages
    └── results            — radar chart + band grid + weakness cards + piece recs + CTAs
```

### Quiz Question Design

| Domain | Q# | Theme |
|--------|-----|-------|
| Ear | 1 | Melodic memory — can you hum a tune back? |
| Ear | 2 | Chord quality — major vs minor by ear |
| Ear | 3 | Error detection — noticing wrong notes |
| Ear | 4 | Playing by ear — finding a melody without music |
| Sight-reading | 1 | Rhythm reading — tapping before playing |
| Sight-reading | 2 | Pulse maintenance — no stopping |
| Sight-reading | 3 | Key signature recognition |
| Sight-reading | 4 | Both hands together from a new page |
| Technique | 1 | Scale fluency — even, in tempo, hands together |
| Technique | 2 | Dynamic control — piano/forte in the right places |
| Technique | 3 | Articulation — staccato/legato switching |
| Technique | 4 | Pedalling — clean vs muddy |
| Theory | 1 | Time signature — reading and understanding |
| Theory | 2 | Harmonic resolution — feeling a phrase "land" |
| Theory | 3 | Formal structure — identifying sections and repeats |
| Theory | 4 | Theory-aided learning — using structure to memorise |

### Business Model Integration (Phase 30)

| Stage | Feature | Status |
|-------|---------|--------|
| Stage 1 | Free diagnosis (radar + weakness + recs) | ✅ Live |
| Stage 2 | $4 Full PDF report (roadmap + teacher match) | 🔜 Stripe + jsPDF needed |
| Stage 3 | Teacher matching page (`connect.html`) | 🔜 Planned |
| Stage 4 | Course/affiliate connections | 🔜 After traffic grows |

### Phase 31 Updates (2026-05-14 — evening session)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Teacher Dashboard removed from public nav | `index.html` | `teacher-dashboard.html` link removed from header. File kept in codebase but no longer promoted publicly. Product direction confirmed: Piano Butler = public repertoire search + diagnosis + connection hub (not a studio management app). |
| 2 | connect.html — teacher/course matching page | `connect.html` | New self-contained React 18 + Tailwind page. Reads `pb_diagnosis_v1` from localStorage. **Teachers tab**: cards sorted by match % against weak domains, match bar, domain badges. **Courses & Apps tab**: Piano Marvel, Musicarta, Lessonface, Musicnotes, Simply Piano — each scored against weak domains. "Apply to be listed" CTA for teacher acquisition. Affiliate disclosure note. |
| 3 | diagnose.html → connect.html wired | `diagnose.html` | Diagnosis result saved to `localStorage('pb_diagnosis_v1')`. Results CTA gains "👩‍🏫 Find a teacher" button (green) → connect.html. |
| 4 | diagnose.html — purpose-first full redesign | `diagnose.html` | Complete rewrite. Target audience narrowed to **returning players** (people who learned before and want to come back). New flow: Landing ("You used to play piano. Where are you now?") → Step 1: Purpose (5 options) → Step 2: Gap (4 options) → Step 3: Memory test (4 questions) → Step 4: Hands readiness (4 questions) → Processing → Results. |
| 5 | Result engine — purpose × gap × score | `diagnose.html` | `computeResult()` combines purpose + gap + memScore + handScore → levelKey (Prelim / G1-G2 / G2-G3 / G4-G5) + personalised headline/message/nextStep per purpose + retention score breakdown (theory memory / physical readiness / overall %) + weak areas list + purpose-filtered corpus picks. |
| 6 | sitemap.xml updated | `sitemap.xml` | diagnose.html (priority 0.9), connect.html (priority 0.9), recommend.html (priority 0.8) added. |

### Product Direction (confirmed 2026-05-14)

| Decision | Detail |
|----------|--------|
| Teacher Dashboard | Removed from public nav. File preserved. Not promoted. |
| Target user | Returning adult pianists — people who learned before and want to come back |
| Piano Butler role | **Middleperson** — diagnosis → connection → commission. Not a content creator. |
| Revenue model | $4 full report (Stripe pending) + teacher referral commission + course affiliate |
| Content strategy | No curriculum creation, no course filming, no ongoing content pressure |

### connect.html Architecture

```
connect.html
├── TEACHERS[]         — teacher cards with strengths[] per domain
├── PLATFORMS[]        — course/app cards with strengths[] per domain
├── matchScore()       — % of user's weak domains covered by item
├── TeacherCard        — avatar, match %, match bar, domain badges, booking CTA
├── PlatformCard       — logo, match %, domain badges, affiliate link
└── App
    ├── useEffect      — reads pb_diagnosis_v1 from localStorage
    ├── weakDomains    — bottom 2 domains from scores
    ├── Teachers tab   — sorted by match score
    └── Courses tab    — sorted by match score + affiliate note
```

### diagnose.html Architecture (Phase 31 — redesigned)

```
diagnose.html (purpose-first, returning player focused)
├── PURPOSES (5)       — child / self / exam / hobby / perform
├── GAPS (4)           — recent / few / decade / long
├── MEMORY_QUESTIONS (4) — note reading, time sig, piece memory, notation reading
├── HANDS_QUESTIONS (4)  — finger readiness, hands together, previous level, mindset
├── computeResult()    — purpose × gap × memScore × handScore → full profile
│   ├── levelKey       — Prelim / G1-G2 / G2-G3 / G4-G5
│   ├── pmsg           — purpose-specific headline + msg + nextStep
│   ├── memWeak[]      — specific theory gaps
│   ├── handsWeak[]    — specific physical gaps
│   └── pieces[]       — 5 corpus picks filtered by purpose + level
└── Results screen
    ├── Purpose message card (headline + msg + next step callout)
    ├── Retention score (theory memory / physical readiness / overall %)
    ├── Brush up on (weak areas list)
    ├── Piece recommendations (5 pieces)
    └── CTAs: Find a teacher → connect.html / Full report $4 (modal)
```

### Phase 33 Updates (2026-05-15 — data quality session)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Composer name normalisation | All 42 `data_*.js` files | 1,641 fixes across all data files. Standard: `SURNAME, Initials` format (e.g. `BEETHOVEN, L.`, `BACH, J.S.`). Fixed: bare surnames, Title Case, Unicode encoding errors (BARTÓK, BURGMÜLLER etc.), RACHMANINOV→RACHMANINOFF, SKRYABIN→SCRIABIN, trailing dots removed. |
| 2 | G8 Leisure BEETHOVEN duplicate removed | `G8/data_g8_leisure.js` | BEETHOVEN Andante appeared in both S4 and S1. PDF confirmed S4 only — removed from S1. Count: 95→94. Leisure total: 706→705. Grand total: 4,501→4,500. |
| 3 | LE COUPPEY fix | `Prelim/data_prelim.js`, `Prelim/data_prelim_leisure.js`, `G2/data_g2.js` | `COUPPEY, F. Le.` → `LE COUPPEY, F.` (correct surname format). |
| 4 | MARTÍNEZ trailing dot removed | `G6/data_g6_comp.js`, `G6/data_g6.js` | `MARTÍNEZ, M. von.` → `MARTÍNEZ, M. von`. |
| 5 | MARTÍNEZ bare surname fixed | `ABRSM/G8/data_abrsm_g8.js` | `MARTÍNEZ` → `MARTÍNEZ, M. von`. |
| 6 | NAT standardisation | `G6/data_g6_comp.js`, `G6/data_g6_leisure.js`, `G5/data_g5_leisure.js` | `Australian-British`→`Australian` (GRAINGER), `Swedish/British`→`Swedish` (ANDERSSON/ULVAEUS), `British-NZ`→`British` (NORTON, C.). |
| 7 | Piece count 4,501→4,500 | `index.html`, `diagnose.html`, `recommend.html`, `admin-counts.html` | All public-facing counts updated to 4,500. |
| 8 | COMPOSER_LINKS canonical keys added | 16 HTML files | 727 new canonical-format keys added to COMPOSER_LINKS objects across all ABRSM, LMusA, AMusA, Trinity Diploma HTML files. Keys now match normalised `p.c` values so Wikipedia links work correctly. |
| 9 | data_g6.js deprecated | `G6/data_g6.js` | Added deprecation warning comment. File is an old skeleton (no nat/era/focus, 159 pieces, exports MASTER_DATA). Not referenced by any live page — `data_g6_comp.js` is authoritative. |
| 10 | sitemap.xml lastmod updated | `sitemap.xml` | All `<lastmod>` dates updated to `2026-05-15`. |

### Phase 34 Updates (2026-05-15 — diagnose.html audit + PDF report)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | `gapFactor` bug fix | `diagnose.html` | `gapFactor` was computed but never applied to the level calculation — gap had zero effect on results. Fixed: `gapPenalty = round((1-gapFactor)*8)`, `adjustedTotal = max(0, total-gapPenalty)`. Level thresholds now use `adjustedTotal`. "More than 10 years" gap now meaningfully lowers the recommended starting level. |
| 2 | Corpus filter fallback | `diagnose.html` | `child` and `perform` purpose filters were too narrow — could return 0 pieces on some grade ranges (focus keywords like "dramatic" or "dance" are rare). Refactored to `filteredPool` with fallback: if `filteredPool.length < 8`, use the full grade pool. |
| 3 | Modal redesign — FullReportModal | `diagnose.html` | `ComingSoonModal` (waitlist email) replaced with `FullReportModal`. Shows purpose + level, 4-item report contents, "Download PDF" button (in-browser jsPDF), and Gumroad $4 link. `gap` prop threaded through. |
| 4 | jsPDF in-browser report generator | `diagnose.html` | `generatePDFReport(result, purpose, gap)` function added (243 lines). Generates 2-page A4 PDF: Page 1 — cover + goal section + next step callout + retention score boxes + radar chart (SVG-style pure jsPDF lines) + weak areas. Page 2 — 4-week practice roadmap (colour-coded week blocks) + 10 recommended pieces + teacher CTA. CDN: `cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js`. |
| 5 | `adjustedTotal` in result object | `diagnose.html` | `adjustedTotal` now returned from `computeResult()` and used in results screen `totalPct` calculation — overall % now reflects gap penalty. |
| 6 | Revenue model updated | `diagnose.html` | Strategy: generate PDF free in browser → user sees value → "Get the full version — $4" Gumroad link in modal. `GUMROAD_URL` constant at top — replace once Gumroad product is created. |

### diagnose.html Architecture (Phase 34 — updated)

```
diagnose.html
├── jsPDF CDN (2.5.1)
├── buildCorpus()          — Prelim–G5 AMEB/ABRSM/Trinity (early grades)
├── PURPOSES (5)           — child / self / exam / hobby / perform
├── GAPS (4)               — recent / few / decade / long
├── MEMORY_QUESTIONS (4)   — note reading, time sig, piece memory, notation
├── HANDS_QUESTIONS (4)    — finger readiness, hands together, prev level, mindset
├── GUMROAD_URL            — ← replace with real link once product created
├── generatePDFReport()    — 2-page A4 jsPDF: cover + radar + roadmap + pieces
├── computeResult()        — purpose × gap(adjusted) × memScore × handScore
│   ├── gapPenalty         — (1-gapFactor)*8 subtracted from total
│   ├── adjustedTotal      — gap-penalised total (0-24), drives levelKey
│   ├── filteredPool       — purpose-filtered corpus with <8 fallback
│   └── pieces[]           — 5 diverse corpus picks
├── FullReportModal        — download button (jsPDF) + Gumroad $4 link
└── Results screen
    ├── Purpose message card
    ├── Retention scores (memScore/12, handScore/12, adjustedTotal%)
    ├── Things to brush up on
    ├── Piece recommendations (5)
    └── CTAs: Find a teacher / Full report $4 modal
```

### Revenue Path (Gumroad)

| Step | Action |
|------|--------|
| 1 | Go to gumroad.com → create product "Piano Butler Full Report — $4" |
| 2 | Generate a sample PDF using diagnose.html (complete the quiz → Download) |
| 3 | Upload that PDF as the Gumroad product file |
| 4 | Copy the Gumroad product URL → replace `GUMROAD_URL` in diagnose.html |
| 5 | Push to main → live |

### Phase 35 Updates (2026-05-15 — domain + onboarding session)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Domain migrated to thepianobutler.com | `CNAME`, `index.html`, `sitemap.xml`, `robots.txt`, `diagnose.html`, `connect.html` | All domain references updated from `pianobutler.com` → `thepianobutler.com`. CNAME file updated. Namecheap DNS configured (4× A records + CNAME → vividssso-pixel.github.io). GitHub Pages custom domain set + DNS check successful + Enforce HTTPS enabled. Supabase Site URL + Redirect URLs updated. |
| 2 | 2-step onboarding LoginModal | `index.html` | Step 1: name input + role selector (Student 🎹 / Teacher 👩‍🏫 / Hobby player 🎵 / Parent 👨‍👧). Step 2: personalised greeting + email input. Name/role saved to `localStorage` (`pb_user_name`, `pb_user_role`) and Supabase `user_metadata` on auth. Progress dots in header. |
| 3 | Supabase Magic Link email template | Supabase dashboard | Subject: "🎹 Your Piano Butler sign-in link". Body: branded HTML email with Piano Butler header, gradient CTA button, footer with thepianobutler.com link. |
| 4 | Dark theme redesign — Claude-inspired | `index.html` | Full dark aesthetic: `#1a1a1a` body, `#e8e3dc` text, `#d4956a` orange accent, Inter font. Nav, sidebar, grade cards, piece rows, search bar, modals, autocomplete all updated. Grade cards: dark bg + subtle accent border. Search input: dark with orange focus glow. Star/save: orange. All filter states use warm orange instead of indigo. |

### Phase 36 Updates (2026-05-18 — diagnosis redesign)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | diagnose.html — full redesign (returner flow) | `diagnose.html` | Replaced 8-question flat quiz with domain-based skill assessment. 16 questions across 4 domains (Technique/Ear/Theory/Sight-Reading), 4 per domain scored 0–3. Results: SVG radar chart, score bars per domain, weak/strong analysis, 8-week personalised roadmap (accordion), 6 corpus-matched piece recommendations. |
| 2 | diagnose.html — beginner flow added | `diagnose.html` | Separate branch for first-time learners. 8 preference questions: genre, dream piece, goal, practice time, timeline, teacher format preference, instrument access, learning style. Result: learner profile card (The Planner / Explorer / Achiever / Thinker), teaching direction note, instrument advice, "what to tell your teacher" summary, 4 starter pieces to listen to. localStorage key: `pb_beginner_v1`. |
| 3 | Landing page updated | `diagnose.html` | New landing copy: "Where are you on your piano journey?" — two-path preview cards (🌱 First-time / 🔄 Returning). |

### diagnose.html Architecture (Phase 36 — dual flow)

```
diagnose.html
├── buildCorpus()              — loads AMEB/ABRSM/Trinity early grades
├── DOMAINS (4)                — Technique / Ear / Theory / Sight-Reading, 4 questions each
├── BACKGROUNDS (2)            — returner / beginner (determines flow branch)
├── PURPOSES (4)               — hobby / exam / perform / teach (returner only)
├── BEGINNER_QUESTIONS (8)     — genre, dream, goal, practice, timeline, teacher, instrument, style
│
├── computeResult()            — returner: domain scores → level + roadmap + recs
├── computeBeginnerResult()    — beginner: answers → learner profile + teaching direction + recs
│
├── RadarChart                 — pure SVG, 4-axis polygon, colour-coded by score
├── ScoreBar                   — per-domain progress bar with ✓/△/! indicator
├── PieceCard                  — piece card with era badge + focus chips
├── BeginnerResults            — beginner result screen component
│
└── App (screens)
    ├── landing                — two-path preview + Start button
    ├── quiz (returner)        — phase 0: background, phase 1: purpose, phases 2–5: domains
    ├── beginner_quiz          — 8 questions, single/multi-select, step dots
    ├── processing             — spin animation (returner only)
    ├── results                — radar + score bars + weak/strong + roadmap + pieces
    └── beginner_results       — profile card + teaching direction + "tell your teacher" + pieces
```

### Phase 37 Updates (2026-05-17 — index.html overhaul + new files)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | List/Group filter tabs in search results | `index.html` | `listFilter` state added (All/A/B/C/D/S1–S4/Manual/Group A/Group B). Dynamic tabs appear only when results contain 2+ distinct list values. Each tab shows piece count, colour-coded by list type. `preListResults` useMemo computes pre-filter set for tab counts. `listFilter` pill in results header; resets on syllabus change. All clear/back buttons reset `listFilter`. |
| 2 | Role-picker homepage redesign | `index.html` | Major rewrite: homepage presents two role-based entry paths (Teacher / Student/Self-learner). Each path leads to a tailored grade picker and filtered search. `activeSyllabus` state drives AMEB/ABRSM/Trinity grade grid tabs. |
| 3 | Diploma + AMEB Leisure in teacher grade picker | `index.html` | Grade picker for teacher flow expanded to include Diploma levels (CertP, AMusA, LMusA, LRSM, FRSM, ATCL, LTCL, FTCL) and AMEB Leisure grades (Prelim–G8). |
| 4 | admin-search.html — full-featured admin search | `admin-search.html` | New file (`noindex, nofollow`). Password-gated (sessionStorage). Full corpus search with all filters: syllabus, era, grade, nationality, list (A/B/C/D), text. Lists functionality (AddToListModal, MyListsPanel, ShareListModal). Supabase auth + favourites. Full piece cards with ▶ Listen, Score, ★ Save, + List buttons. |
| 5 | robots.txt — admin-search.html blocked | `robots.txt` | `Disallow: /admin-search.html` added. |
| 6 | Search-first homepage (second iteration) | `index.html` | Further simplified: single search bar always visible, grade grid removed from homepage, tool cards (Recommend + Diagnose) shown below hint chips, stats footer with "Full search ↗" link. Dark theme throughout. |
| 7 | UX iterations — homepage tool cards | `index.html` | Multiple passes: tool cards removed → hint chips expanded → tool cards restored → syllabus filter chips removed → final: hint chips + 2 tool cards (🎹 Recommend, 🔬 Diagnose). |
| 8 | 2-col results grid | `index.html` | Results changed to `repeat(auto-fill,minmax(340px,1fr))` — 2 columns on desktop. Bigger titles (17px, 800 weight). List/Diploma badges removed from piece cards (cleaner). Butler-tone copy in results count and no-results messages. |
| 9 | Dark theme — connect.html, diagnose.html, recommend.html | `connect.html`, `diagnose.html`, `recommend.html` | All three pages updated to match index.html dark aesthetic: `#1a1a1a` bg, `#e8e3dc` text, `#d4956a` orange accent. Dark cards, dark nav, dark modals. |

### Phase 38 Updates (2026-05-17 — recommend.html redesign + Safari fixes)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | recommend.html — simplified 4-step flow | `recommend.html` | Full redesign. Previous 6-step wizard replaced with cleaner flow: **Step 0** character (Expressive/Technical/Playful/Balanced/Adventurous) → **Step 1** level (Beginner/Early/Intermediate/Advanced/Diploma) → **Step 2** era preference (multi-select chips, optional) → **Step 3** exam optional (Yes/No → if Yes: syllabus + grade). Results generated from scoring engine. |
| 2 | recommend.html — scoring engine update | `recommend.html` | `scorepiece()` updated: character keyword match (+25 per hit), era match (+30), grade range match (+20), random variety seed (+10). `pickDiverse()` selects pieces with era and nationality diversity bonus. `CHAR_WORDS` expanded per character type. `LEVEL_GRADE_KEYS` maps level → `_gradeKey` array. |
| 3 | recommend.html — Safari compatibility fixes | `recommend.html` | Three separate fixes: (1) `color-mix()` CSS function removed → replaced with static hex; (2) TypeScript `as any` casts removed from JSX (Babel standalone rejects them); (3) optional chaining `?.` → explicit null checks; (4) `ErrorBoundary` class component added to catch render crashes. |
| 4 | recommend.html — progress bar + step dots | `recommend.html` | `progress-fill` CSS bar advances through 4 steps (0–3). 4 step dots below progress bar (done = orange filled, active = scaled). Back button appears from step 1 onward. "Generate" button only on final step. |

### index.html Architecture (as of Phase 37)

```
index.html (minimal public search — dark theme)
├── buildCorpus()           — 4,500 pieces from all data files
├── searchCorpus()          — multi-token AND search (title/composer/nat/era/focus)
├── useVideoModal()         — YouTube Data API v3 in-page modal
├── VideoModal              — dark overlay iframe
├── PieceCard               — piece card: syllabus badge, era tag, title, composer Wikipedia link, ▶ Listen, Score
├── HINT_CHIPS (12)         — Chopin, Bach, Debussy, Baroque, Romantic, Australian, Waltz, Sonatina…
├── SYLLABUS_BADGE          — colour mapping for all 6 syllabus types
├── ERAS / ERA_TAG_CLASS    — 5 eras, CSS class per era
└── App
    ├── query / searchQuery — debounced 200ms (input instant, filter delayed)
    ├── eraFilter           — era chip filter
    ├── gradeFilter         — grade chip filter (shown only when searching)
    ├── syllabusFilter      — All / AMEB / Leisure / ABRSM / Trinity (no UI — available in state)
    ├── isSearching         — true when any filter or query active
    ├── results             — filtered corpus, max 60
    ├── suggestions         — autocomplete (composer + title, max 8)
    ├── Homepage (not searching): hint chips + 2 tool cards + stats footer
    └── Results: count + grid of PieceCard
```

### admin-search.html Architecture

```
admin-search.html (password-gated, noindex)
├── Password gate           — sessionStorage('pb_admin_auth')
├── Full buildCorpus()      — all 4,500 pieces
├── Full filter set         — syllabus + era + grade + nationality + list (A/B/C/D)
├── listFilter tabs         — dynamic tabs from result set
├── AddToListModal          — local-first list creation
├── MyListsPanel            — slide-in panel, share/export/delete
├── Supabase auth           — Magic Link, session-aware
├── Full PieceRow           — ★ Save + + List + ▶ Listen + Score
└── GradeGrid               — AMEB/ABRSM/Trinity tab toggle + grade cards
```

### recommend.html Architecture (as of Phase 38)

```
recommend.html (dark theme, 4-step wizard)
├── buildCorpus()           — all 4,500 pieces
├── CHARACTERS (5)          — Expressive / Technical / Playful / Balanced / Adventurous
├── LEVELS (5)              — Beginner / Early / Intermediate / Advanced / Diploma
├── CHAR_WORDS              — keyword arrays per character (used in scorepiece)
├── LEVEL_GRADE_KEYS        — level → _gradeKey array (corpus filter)
├── scorepiece(p, prefs)    — scores each piece by character/era/grade match
├── pickDiverse(scored, n)  — picks n pieces with era + nationality diversity
├── ErrorBoundary           — crash-safe wrapper
└── App (5 screens: 0–3 + results)
    ├── Step 0: character picker (5 cards)
    ├── Step 1: level picker (5 options)
    ├── Step 2: era preference (multi-select chips, optional)
    ├── Step 3: exam optional (Yes/No → syllabus + grade if Yes)
    └── Results: scored combination, regenerate button, YouTube modal
```

### Phase 40 Updates (2026-05-21 — data audit + UX polish)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | YouTube API key referrer restriction verified | Google Cloud Console | Confirmed `https://thepianobutler.com/*` and `https://www.thepianobutler.com/*` both registered. New key `AIzaSyAUydn17tJCoduix-iv7f7bKfXweIrR6Mg` active across all 22 HTML files. ✅ |
| 2 | Full data audit — ABRSM (433 pieces) | All 9 `data_abrsm_*.js` files | ERA/FOCUS/NAT/duplicate check. Found 31 pieces with duplicate focus keyword (`"Formal structure"` repeated). All fixed with pedagogically appropriate 3rd keywords per piece. ✅ |
| 3 | Full data audit — Trinity (1,565 pieces) | All 12 Trinity data files | ERA/FOCUS/NAT/duplicate check. All clean. Trinity Initial–G5 = open pool (no `l` field, uses no grouping). Trinity G6–G8 = `grp: "A"|"B"`. ✅ |
| 4 | List A/B/C/D badge added to search results | `index.html` | `PieceCard` now shows List badge: A=blue, B=indigo, C=violet, D=purple. Trinity G6–G8 shows Group A/B badge (green). Open-pool pieces (Trinity Initial–G5, all Diploma) show no list badge. |
| 5 | Search results → 1-column layout | `index.html` | `gridTemplateColumns` changed from `repeat(auto-fill,minmax(340px,1fr))` → `1fr`. Results now display as single full-width column. |
| 6 | Piece cards — compact layout | `index.html` | Card padding reduced (22px → 12px 16px). Title + Composer + Listen/Score buttons on same row. Focus tags displayed inline below composer. Container maxWidth 900 → 1100. |
| 7 | Era chips removed from homepage | `index.html` | Baroque/Classical/Romantic/Modern/Contemporary chips removed from below search bar. Era filter still available in sidebar during search. |
| 8 | Sidebar filter restored | `index.html` | Left sidebar with Syllabus / Grade / Era sections reintroduced for search results view. Replaces the two-row filter bar (seg-bar + grade chips). Sidebar only visible when `isSearching`. |
| 9 | ANZCA evaluated and declined | — | 2025-27 ANZCA Piano Syllabus PDF reviewed. Data structure is book-based (not piece-based) — incompatible with Piano Butler's per-piece architecture. Decision: do not add ANZCA. |
| 10 | Product direction confirmed | — | Piano Butler = exam syllabus search tool only. No open repertoire additions. Focus: deepen existing syllabuses, improve UX, grow traffic before monetisation. |

### Phase 41 Updates (2026-05-21 — Safari compatibility fix)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | `inset:0` → `top/right/bottom/left:0` | 23 HTML files | `inset` CSS shorthand not supported in Safari <14.1. Replaced across all public pages: index.html, diagnose.html, recommend.html, Prelim–G8 (9 files), ABRSM Initial–G8 (9 files), AMusA, LMusA, CertP, ABRSM LRSM/FRSM. |
| 2 | `min(800px,95vw)` → `width:95vw; max-width:800px` | `index.html` | CSS `min()` function replaced with equivalent max-width pattern for broader Safari compatibility. |
| 3 | Supabase script removed from index.html | `index.html` | Supabase JS library (500KB) was loaded but completely unused on index.html — auth/login code was removed in Phase 8. Removed to reduce load time and eliminate potential Safari init errors. |

### Phase 42 Updates (2026-05-22 — Safari blank screen root cause fix)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | CDN migration — React + ReactDOM | `index.html` | `unpkg.com/react@18` (unversioned, unstable on mobile) → `cdnjs.cloudflare.com/ajax/libs/react/18.2.0` (pinned, fast). Same for react-dom. Added `crossorigin="anonymous"`. |
| 2 | CDN migration — Babel Standalone | `index.html` | `unpkg.com/@babel/standalone` (unversioned = ~8MB latest) → `cdnjs.cloudflare.com/ajax/libs/babel-standalone/7.23.3` (pinned, smaller). Root cause of Safari blank screen: unpkg was serving a huge Babel build that timed out or exhausted memory on mobile Safari before the app could mount. |
| 3 | Manual Babel compile trigger | `index.html` | Changed `<script type="text/babel">` → `<script id="app-jsx" type="text/jsx-raw">` (non-standard type prevents Babel auto-run). Added inline bootstrap `<script>` that waits for `DOMContentLoaded`, checks `typeof Babel !== 'undefined'` (retries every 50ms if not ready), then calls `Babel.transform()` manually before appending compiled script to DOM. Includes `try/catch` that renders error message in `#root` on compile failure. |
| 4 | Curly quote fix | `index.html` | Smart/curly quotes (`"` `"`) present in a JSX string literal caused Babel compile error: `Unexpected character '"' (571:70)`. Replaced all curly quotes with straight ASCII quotes throughout the file via Python script. |

### index.html CDN Stack (as of Phase 42)

| Library | Old CDN | New CDN | Version |
|---------|---------|---------|---------|
| React | unpkg.com (unversioned) | cdnjs.cloudflare.com | 18.2.0 (pinned) |
| ReactDOM | unpkg.com (unversioned) | cdnjs.cloudflare.com | 18.2.0 (pinned) |
| Babel Standalone | unpkg.com (unversioned, ~8MB) | cdnjs.cloudflare.com | 7.23.3 (pinned) |
| Tailwind CSS | cdn.tailwindcss.com | cdn.tailwindcss.com | latest (unchanged) |

### Phase 39 Updates (2026-05-18 — diagnose.html UX fixes + security)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Landing cards — directly clickable | `diagnose.html` | 🌱 / 🔄 preview cards replaced with proper `<button>` elements. Click goes directly to correct flow — no intermediate background question. 🌱 → `beginner_quiz` immediately. 🔄 → `quiz` at phase 1 (Purpose), skipping phase 0. "Start →" single button removed. |
| 2 | ShareResultButton component | `diagnose.html` | New component added. "🔗 Share my result" button appears at bottom of both result screens (returner + beginner). Encodes result to base64 URL param (`?result=…`). Uses `navigator.share` on mobile, clipboard copy on desktop. Shows "✓ Link copied!" confirmation for 2.5s. |
| 3 | SharedResultView component | `diagnose.html` | Read-only result page rendered when `?result=` URL param detected on load. Shows returner result (levelLabel + overallPct + weak areas) or beginner profile (profile name + genre + timeline + teacherFormat). CTAs: "Take my own diagnosis" + "Find a teacher". No login required to view. |
| 4 | YouTube API key rotated — security | All 21 HTML files | Old key `[REDACTED-OLD]` exposed in GitHub history (GitGuardian alert). New key `[REDACTED]` applied across all 21 HTML files. Old key deleted from Google Cloud Console. New key restricted to `thepianobutler.com/*` + `www.thepianobutler.com/*` referrers. |

### Phase 43 Updates (2026-05-25 — diagnose.html + recommend.html UX overhaul)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | diagnose.html — full rewrite, 8 questions | `diagnose.html` | Replaced complex dual-flow (beginner/returner, 16 questions) with a single clean 8-question flow (2 per domain). Domains: Technique 🎹, Ear Training 👂, Theory 📖, Sight-Reading 🎵. Results: score bars per domain with Strong/Developing/Focus here bands, top 2 weak domains with DOMAIN_TIPS (title + 3 actionable tips + next step), 4 corpus-matched pieces with Listen/Score/Find in Piano Butler buttons, strength callout card, CTAs to recommend.html and index.html. CDN migrated to cdnjs pinned (React 18.2.0, Babel 7.23.3) with manual Babel compile trigger. No Gumroad/jsPDF dependency — removed. |
| 2 | recommend.html — rewrite (Phase 42 session) | `recommend.html` | Reduced from 4-step wizard to 2-step (level → style+era → results). Result cards have 3 action buttons: Listen, Score, Find in Piano Butler (links to index.html with search query). CDN migrated to cdnjs pinned versions. |

### diagnose.html Architecture (as of Phase 43)

```
diagnose.html (single flow, 8 questions)
├── buildCorpus()              — AMEB Prelim-G5 + ABRSM Initial-G4 + Trinity Initial-G4
├── DOMAINS (4)                — Technique / Ear / Theory / Sight-Reading, 2 questions each
├── ALL_QUESTIONS (8)          — flat array from DOMAINS
├── DOMAIN_TIPS                — per-domain: title + 3 tips + nextStep
├── computeResult(answers)     — domain scores (0-6 each), weakest x2, strongest, levelLabel, pieces x4
│   ├── levelLabel             — Preliminary / Grade 1-2 / Grade 2-4 / Grade 4-5+ (from totalScore 0-24)
│   ├── weakFocusTags          — union of weak domain focusTags (used to score corpus)
│   └── pieces                 — 4 corpus picks with era + composer diversity
├── DomainResult               — score bar + Strong/Developing/Focus band
├── TipCard                    — per-domain tip card from DOMAIN_TIPS
├── PieceCard                  — Listen + Score + Find in Piano Butler action links
└── App screens
    ├── landing                — 4 domain preview cards + Start button
    ├── quiz                   — question card with 4 options, Back/Next, progress bar
    └── results                — level label + score bars + focus tips + piece recs + strength callout + CTAs
```

### Phase 44 Updates (2026-05-25 — homepage UX: two entry points)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Homepage redesign — two equal entry cards | `index.html` | Replaced search bar + TOOLS section with two side-by-side cards: 🔍 "I know what I'm looking for" (Search) and 🎹 "I'm not sure where to start" (Diagnose). Both cards equal size, same border style. Clicking Search card → transitions directly to full search screen. Clicking Diagnose card → navigates to diagnose.html. |
| 2 | `showSearchInput` state added | `index.html` | `const [showSearchInput, setShowSearchInput] = useState(false)`. `isSearching` updated to `!!(showSearchInput \|\| searchQuery.trim() \|\| ...)`. `clearAll()` resets `showSearchInput` to false. |
| 3 | Direct search screen transition | `index.html` | Search card click calls `setShowSearchInput(true)` only — no inline input expansion. `isSearching` becomes true → full search layout renders. Search input has `autoFocus`. |
| 4 | Tailwind removed from diagnose.html | `diagnose.html` | Tailwind CDN (`cdn.tailwindcss.com`) was overriding inline styles with black text on `<a>`, `<button>`, `<ul>/<li>`. Removed entirely. Added explicit CSS reset in `<style>`: `a { color: inherit; }`, `button { font-family: inherit; }`, `ul,ol { margin:0; padding:0; list-style:none; }`. TipCard uses `listStyle:'disc'` inline on ul. |
| 5 | SVG radar chart added to diagnose.html | `diagnose.html` | Pure SVG 4-axis diamond polygon. Grid rings at 33/66/100%. Data polygon filled orange. Colored domain dots at each axis endpoint. Domain icon + label outside each axis. Bug fix: `axisEnds` stores `{ ds: ds }` objects; accessed as `a.ds.domain.color` (not `a.domain.domain.color`). |
| 6 | CDN stack standardised — diagnose.html | `diagnose.html` | React 18.2.0 + Babel 7.23.3 pinned on cdnjs. Manual Babel compile trigger: `DOMContentLoaded` → check `typeof Babel !== 'undefined'` (retry 50ms) → `Babel.transform()` → append script. `try/catch` renders error in `#root` on compile failure. |

### diagnose.html Architecture (as of Phase 44 — final)

```
diagnose.html
├── No Tailwind — explicit CSS reset only
├── CDN: React 18.2.0 + Babel 7.23.3 (cdnjs, pinned), manual compile trigger
├── buildCorpus()              — AMEB Prelim–G5 + ABRSM Initial–G4 + Trinity Initial–G4
├── DOMAINS (4)                — Technique 🎹 / Ear 👂 / Theory 📖 / Sight-Reading 🎵
│   each has: label, icon, color, bgColor, focusTags[], questions[2]
├── ALL_QUESTIONS (8)          — flat array from DOMAINS
├── DOMAIN_TIPS                — per domain: title + tips[3] + nextStep
├── computeResult(answers)     — domainScores[], ranked[], weakest[2], strongest, levelLabel, pieces[4]
├── RadarChart                 — pure SVG, polar→XY: (cx + r*cos(rad), cy + r*sin(rad))
│   axisEnds: [{ds: {domain, score, pct}}, ...], accessed as a.ds.domain.color
├── ScoreBar, DomainResult, TipCard, PieceCard
├── ErrorBoundary
└── App screens: landing → quiz → results
```

### index.html Homepage Architecture (as of Phase 44)

```
index.html homepage (not isSearching):
├── Nav (Piano Butler title + nav buttons: Recommend / Diagnose / Sign in)
├── Hero text ("The piano repertoire you've been looking for.")
├── Two entry cards (flex row, equal width):
│   ├── Search card (onClick → setShowSearchInput(true))
│   └── Diagnose card (href="diagnose.html")
└── Stats line ("4,500+ pieces · AMEB · ABRSM · Trinity · Diploma")

index.html results (isSearching = true):
├── Nav visible
├── Search input (autoFocus when entering from Search card)
├── Sidebar (Syllabus / Grade / Era filters)
├── Results grid (1-column, compact PieceCard rows)
└── clearAll() → resets showSearchInput + all filters → returns to homepage
```

### Phase 45 Updates (2026-05-27 — Random Pick polish + security + title)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Random Pick — Listen + Score buttons | `index.html` | Each result card now has ▶ Listen (YouTube modal) and ♩ Score (Google sheet music search) buttons. |
| 2 | Random Pick — YouTube z-index fix | `index.html` | `.yt-modal-bg` z-index raised 100→200. Random Pick stays open; YouTube floats above it. Closing YouTube returns to Random Pick with all cards intact. `onClose()` removed from Listen button. |
| 3 | Footer disclaimer expanded | `index.html` | Single-line "Not affiliated" → two-line independence statement: "Piano Butler is an independent repertoire reference tool. Syllabus information is sourced from publicly available AMEB, ABRSM, and Trinity syllabuses. Piano Butler is not affiliated with or endorsed by AMEB, ABRSM, or Trinity College London." |
| 4 | Security — admin password removed from public files | `CLAUDE.md` | `pianobutler2026` password text removed from CLAUDE.md (3 occurrences). Admin files still exist but password no longer exposed in public GitHub repo. |
| 5 | Admin link removed from footer | `index.html` | "Full search ↗" link to admin-search.html removed from homepage footer. robots.txt disallow still in place. |
| 6 | Site title updated | `index.html` | `Piano Butler — Piano Exam Pieces` → `Piano Butler — Exam & Repertoire Search` across title, og:title, twitter:title. |

### Product Direction (confirmed 2026-05-27)
- Goal: clean, functional site → SEO traffic → simple monetisation
- Priority order: Google Search Console → SheetMusicPlus affiliate → AdSense (when traffic grows)
- Diagnose/Recommend: deprioritised, not linked from nav
- connect.html: placeholder only, not promoted

### Phase 48 Updates (2026-06-01 — SEO: noscript fallback + keywords)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Search Console status check | — | 2 pages indexed, 37 not indexed (35 "Discovered – currently not indexed", 1 "Crawled – currently not indexed", 1 canonical). All normal 4 days after sitemap submission. ABRSM G5 identified as the crawled-but-not-indexed page — root cause: React/JS rendering invisible to Google crawler. |
| 2 | `<noscript>` static HTML fallback — all 35 grade pages | All `piano-repertoire_*.html` files | Python + Node script extracted piece data (inline or from companion `data_*.js`) and injected a full static piece list inside `<noscript>` tags before `</body>`. Google crawler now sees all pieces without executing JavaScript. Commit `fb46e91`. |
| 3 | SEO keywords — AMusA, LMusA | `AMusA/piano-repertoire_amusa.html`, `LMusA/piano-repertoire_lmusa.html` | `<meta name="keywords">` tag was missing. Added 5 grade-specific keywords each. Commit `c1e684c`. |
| 4 | SEO keywords — Trinity Initial–G8 | All 9 `Trinity/*/piano-repertoire_trinity_*.html` files | Keywords expanded from 3 generic → 5 grade-specific (e.g. "Trinity College London piano Grade 5", "Trinity piano Grade 5 2023", "piano exam pieces grade 5", etc.). Commit `c1e684c`. |

### Phase 49 Updates (2026-06-03 — UX bug fixes)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Supabase project restored | Supabase dashboard | Project auto-paused after 7 days of inactivity (free tier). Restored manually. Teacher dashboard functional again. To prevent recurrence: use dashboard weekly or upgrade to Pro ($25/mo). |
| 2 | Trinity grade filter bug fix | `index.html` | Sidebar Grade section was always showing AMEB keys (Prelim/G1–G8). When Trinity syllabus selected, now shows Trinity keys (TInitial/TG1–TG8). `TRINITY_GRADE_KEYS` constant added. `isDiploma` check hides Grade section entirely for Diploma syllabuses. |
| 3 | Diploma sidebar filter added | `index.html` | SYLLABUS_FILTERS expanded: added AMEB Diploma, ABRSM Diploma, Trinity Diploma. Diploma pieces were in corpus but had no way to be filtered in sidebar. |
| 4 | Title truncation removed | `index.html` | `whiteSpace:'nowrap'` + `textOverflow:'ellipsis'` removed from PieceCard title. Long titles now wrap fully. |
| 5 | Random Pick — Trinity included | `index.html` | Pool filter was `_syllabus === 'AMEB' \|\| _syllabus === 'ABRSM'` only. Added `\|\| _syllabus === 'Trinity'`. |
| 6 | "Surprise me" card copy fix | `index.html` | Description said "Filter by List (A/B/C/D) or era" — List filter doesn't exist in Random Pick modal. Corrected to "Pick a grade and get one piece from each era — Baroque through Contemporary." |
| 7 | Nav kept minimal | `index.html` | Recommend/Diagnose buttons not restored to nav — intentional decision to keep homepage simple. Diagnose exposure deferred pending further development. Recommend accessible via direct URL only for now. |

### Phase 50 Updates (2026-06-08 — SEO + mobile UX + cross-page search)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Search Console — ABRSM G5 Validate Fix submitted | Google Search Console | Clicked "Validate Fix" on "Crawled – currently not indexed" ABRSM G5 page. Validation started 06/06/2026. |
| 2 | Search Console — 6× Request Indexing | Google Search Console | Manually requested indexing for: G5, G1, ABRSM G1, Trinity G1, G3, ABRSM G3. |
| 3 | Mobile UX improvements | `index.html` | CSS media query `@media (max-width:640px)` expanded: `.hero-title` font-size 42→28px, `.hero-subtitle` 15→13px, `.entry-card` padding 28px 24px→20px 16px, `.entry-card-title` 18→15px, `.yt-iframe` height 450→220px, `.main-pad` padding reduced. Class names added to matching JSX elements. |
| 4 | Mobile grade filter added to filter strip | `index.html` | Previously mobile strip had Syllabus + Era chips only. Now includes Grade chips (AMEB: Prelim–G8; Trinity: TInitial–TG8; hidden for Diploma). Dynamically rendered with TRINITY_GRADE_KEYS / GRADE_KEYS. |
| 5 | `?q=` URL param support | `index.html` | `_initQ` reads `URLSearchParams(window.location.search).get('q')` on init. `query` + `searchQuery` both initialised to `_initQ`. `showSearchInput` initialised to `!!_initQ`. "Find in Piano Butler" buttons in `diagnose.html` and `recommend.html` now correctly trigger search on landing. |
| 6 | Contact button style upgrade | `index.html` | Footer contact link upgraded from plain text underline → bordered pill button (white bg, `#e0d8d0` border, rounded-8, hover orange). |
| 7 | Random Pick Trinity inclusion fix | `index.html` | Pool filter now includes Trinity-keyed pieces (`TInitial`, `TG1`–`TG8`) via `trinityKey` mapping. |
| 8 | Enter key closes autocomplete | `index.html` | `onKeyDown` handler added to search input: `if (e.key === 'Enter') setShowSuggestions(false)`. |

### Phase 51 Updates (2026-06-09 — Search Console audit + AdSense setup)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Search Console indexing audit | — | Checked URL Inspection for key pages. index.html ✅, G5 ✅, G3 ✅, G1 ✅, ABRSM G5 ✅ — all already indexed. Trinity G5 was "Discovered – not indexed" → Request Indexing submitted. Trinity G1, G8 already indexed. |
| 2 | Google AdSense account created | — | New AdSense account created with vividssso@gmail.com. Site: thepianobutler.com. Country: Australia. Payment profile: Clara Sohyun Park, 79 Burwood Road, Concord NSW 2137. |
| 3 | AdSense script added to index.html | `index.html` | `<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6523454944716812" crossorigin="anonymous"></script>` added to `<head>`. Commit `86a3287`. |
| 4 | AdSense site verified | Google AdSense | Site ownership confirmed. "사이트가 확인되었습니다" ✅. Google review in progress — approval typically takes days to 2 weeks. |

### Phase 52 Updates (2026-06-10 — SEO + UX polish)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | SEO audit — root cause identified | `index.html` | Google이 JS 없이 index.html을 보면 `<div id="root"></div>` 하나만 보이는 문제 발견. 37개 페이지 중 2개만 인덱스된 원인. |
| 2 | `<noscript>` static fallback added | `index.html` | AMEB/ABRSM/Trinity 각 grade별 샘플 곡 + 모든 grade 헤더 (27개) + Diploma 링크 + 설명 텍스트. Google이 JS 없이도 콘텐츠를 읽을 수 있음. Commit `92ef293`. |
| 3 | Schema.org JSON-LD added | `index.html` | `WebSite` + `SearchAction` (sitelinks searchbox 자격) + `ItemList` (27개 grade 페이지 구조화). Commit `92ef293`. |
| 4 | Recommender syllabus filter | `recommend.html` | Step 0 추가: 🌐 Any / 🇦🇺 AMEB only / 🇬🇧 ABRSM only / 🎓 Trinity only. 3-step 플로우 (syllabus → level → style). Commit `7c83584`. |
| 5 | Random Pick syllabus filter | `index.html` | Syllabus 선택 행 추가 (Any / AMEB / ABRSM / Trinity). Grade 선택 위에 배치. 설명 텍스트도 동적으로 변경. Commit `396de63`. |
| 6 | Recommend result cards — full details | `recommend.html` | Series (S19/S18/S17/Manual/AustAnth/S1–S4), List A/B/C/D, Group A/B, Nationality, Key, Focus tags 모두 표시. 색상 구분 배지. Commit `5f40a44`. |
| 7 | Prelim → Preliminary (user-facing labels) | `index.html`, `recommend.html` | GRADE_LABEL_MAP, GRADE_OPTIONS label, buildCorpus grade label 모두 수정. 내부 key ('Prelim')는 유지. Commit `24530fd`. |

### Phase 53 Updates (2026-06-10 — strategy session)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Traffic strategy research | — | Researched promotion channels: MTA NSW/VIC/QLD/SA/WA (email), Piano World Teachers Forum, ABRSM Teachers Forum, TopMusic.co. Decision: defer active promotion — SEO organic growth preferred. |
| 2 | Passive income strategy confirmed | — | Priority order: (1) AdSense auto-approval → (2) Sheet Music Plus affiliate at 500 clicks → (3) Gumroad PDF at 1,000 visitors. No active promotion for now — waiting for SEO to compound. |

### Phase 47 Updates (2026-05-28 — contact form)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | In-site contact form modal | `index.html` | Replaced `mailto:` footer link with a `ContactModal` React component. Visitors type Name + Email + Message and submit — personal email never exposed. Powered by Web3Forms (free, 250/month). Access key: `1905cf40-5bcd-463a-87dd-c9d5ee673f56`. Submissions forwarded to vividssso@gmail.com. Success/error states handled inline. Commits: `56018b7`, `b662135`, `9ca4fff`. |

### Phase 46 Updates (2026-05-28 — SEO + housekeeping)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | recommend.html — 2-step wizard committed | `recommend.html` | Uncommitted Phase 43 changes finalised. CDN migrated to cdnjs pinned (React 18.2.0, Babel 7.23.3). Manual Babel compile trigger. 4-step → 2-step flow (level → style+era → results). `dramatic` character added. Missing `twitter:title` + `twitter:description` meta tags added. Commit `5a6d577`. |
| 2 | Google Search Console — domain verified | Google Search Console | `https://thepianobutler.com` verified via HTML tag method. `<meta name="google-site-verification">` added to index.html. Commit `e963922`. |
| 3 | sitemap.xml submitted | Google Search Console | `https://thepianobutler.com/sitemap.xml` submitted. Status "Couldn't fetch" initially — normal, Google will crawl within days. |
| 4 | SEO — title + description overhaul (28 pages) | All AMEB/ABRSM/Trinity grade HTML files + index.html | Keyword-rich titles: `"AMEB Grade 5 Piano Pieces 2026 \| Piano Butler"`, `"ABRSM Grade 5 Piano Pieces 2025 & 2026 \| Piano Butler"`, `"Trinity College Piano Grade 5 Pieces 2023 \| Piano Butler"`. Descriptions include piece counts and filter features. index.html og/twitter tags updated to match. Commit `5099a62`. |
| 5 | .gitignore — accidental files cleaned | `.gitignore`, repo | `Anzca/`, `Piano Butler — Lesson Video Plan.md`, `main` accidentally committed in SEO commit. Removed from Git tracking, added to .gitignore. Commit `5159fe4`. |
| 6 | CLAUDE.md — deferred features reminder table | `CLAUDE.md` | Added table of features to revive at traffic milestones: Login revival (≥1,000 visitors), Affiliate links (≥500 clicks), Gumroad PDF, connect.html real teacher info. Commit `dc9cfad`. |
| 7 | Affiliate research completed | — | Compared Sheet Music Plus (8–12%, 30-day cookie) vs Sheet Music Direct (10% fixed) vs Musicnotes (5%). Decision: defer until Search Console clicks ≥ 500. Sheet Music Plus preferred at scale; Sheet Music Direct better at low volume. |

## Deferred Features — Remind When Ready

| Feature | Trigger to remind | Notes |
|---------|------------------|-------|
| **Login revival** (Magic Link + Supabase) | Monthly Search Console visitors ≥ 1,000 | index.html had Supabase + LoginModal removed in Phase 41. auth.js + login.html still exist. Reinstate takes ~1–2h. Remind Sohyun when traffic hits this threshold. |
| **Affiliate links** (Sheet Music Plus or Direct) | Monthly Search Console clicks ≥ 500 | Score button currently links to Google search. Replace with affiliate URL once approved. Sheet Music Plus = 8–12%, Sheet Music Direct = 10% fixed. |
| **Gumroad $4 PDF report** | After affiliate is live | diagnose.html has jsPDF generator ready. Just needs Gumroad product URL + replace GUMROAD_URL constant. |
| **connect.html — real teacher info** | When Sohyun is ready to take referrals | Add real photo, booking link, price. Currently placeholder only. |
| **hello@thepianobutler.com 이메일** | Monthly visitors ≥ 1,000 | Namecheap 이메일 포워딩으로 설정 (월 몇 달러). vividssso@gmail.com으로 받을 수 있음. footer Contact 링크 주소도 함께 교체. |
| **find-a-teacher.html + teach-with-us.html** | When Sohyun is ready to recruit teachers | Both pages built and tested. Add links to homepage footer when ready to go public. |

---

### Phase 54 Updates (2026-06-11 — UX audit + teacher matching + file cleanup)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | AdSense review re-requested | Google AdSense | adsense.google.com — "검토 요청" clicked again. Account: ca-pub-6523454944716812. Applied Jun 9. Check ~Jun 16–23. |
| 2 | Search Console Validate Fix submitted | Google Search Console | 34 pages "Discovered – currently not indexed". Clicked "Validate Fix" to prompt re-crawl. |
| 3 | Supabase restored | Supabase dashboard | Project auto-paused (free tier, 7 days inactivity). Restored manually. Status: Healthy ✅. Teacher dashboard functional again. |
| 4 | G6 corpus bug fixed | `index.html` | `buildCorpus()` referenced `DATA_G6_COMP` but `G6/data_g6_comp.js` exports `DATA_G6`. Variable was always `undefined` → 160 G6 pieces silently absent from all search results. Footer showed "4,340 pieces" instead of 4,500. Fixed: `typeof DATA_G6_COMP` → `typeof DATA_G6`. Verified with node count script: total = 4,500 ✅. |
| 5 | find-a-teacher.html created | `find-a-teacher.html` | New page — student teacher-matching request form. 4-step wizard: About you (name, email, age, phone) → Goals (level chips + goal chips) → Preferences (location, format, frequency, budget) → Summary + Submit. Web3Forms submission to vividssso@gmail.com. Success screen. NOT linked from homepage — hidden pending review. |
| 6 | teach-with-us.html created | `teach-with-us.html` | New page — teacher application form. Fields: name, email, location, timezone chips, levels multi-chips, syllabuses multi-chips, availability multi-chips, experience, rate, bio. 3 perk cards: Online only / Pre-matched / Free to join. Web3Forms submission. NOT linked from homepage — hidden pending review. |
| 7 | Strategic direction — online-only matching | — | Decision: Piano Butler teacher matching will be **online-only** (no in-person). Removes geographic constraints, lower operational complexity, aligns with digital-native user base. find-a-teacher.html still has "In-person" option in format field — update when launching publicly. |
| 8 | Supply-first strategy confirmed | — | Build teacher supply (teach-with-us.html) before promoting student demand (find-a-teacher.html). Recruit teachers via Sohyun's network and piano teacher communities first. |
| 9 | 17 unused files deleted | Multiple | Deleted session logs, old auth files, unused pages (home.html, auth.js, login.html, payments.html, teacher-plan.html, connect-stripe.html, stripe-webhook.js, test-*.html, etc.). Files no longer used since public pivot (Phase 8). Committed and pushed. |
| 10 | Teacher pages hidden from homepage | `index.html` | find-a-teacher and teach-with-us footer links removed (Contact us remains). Pages accessible via direct URL only until ready for public launch. |

### New Files (Phase 54)

```
Piano Butler/
├── find-a-teacher.html    ← Student teacher-matching request (hidden from nav)
└── teach-with-us.html     ← Teacher application form (hidden from nav)
```

### find-a-teacher.html Architecture

```
find-a-teacher.html (4-step wizard)
├── Step 0: About you — name, email, age (optional), phone (optional)
├── Step 1: Your goals — level chips + goal multi-chips (AMEB/ABRSM/Trinity exam, Hobby, Adult returner, Performance, Not sure)
├── Step 2: Preferences — location, format chips (In-person/Online/Either), frequency chips, budget chips
├── Step 3: Summary card + submit → Web3Forms → vividssso@gmail.com
└── Success screen
```

### teach-with-us.html Architecture

```
teach-with-us.html (single-page form)
├── Perk cards: Online only / Pre-matched / Free to join
├── Your details: name, email, location, timezone chips
├── What you teach: levels multi-chips, syllabuses multi-chips, availability multi-chips
├── About you: experience, rate, bio textarea
└── Submit → Web3Forms → vividssso@gmail.com (subject: "New Teacher Application — Piano Butler")
```

### Phase 55 Updates (2026-06-12 — automation + content experiment)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Supabase keep-alive GitHub Action | `.github/workflows/supabase-keepalive.yml` | Cron pings Supabase REST API (`students?select=id&limit=1` with public anon key) every Mon & Thu 22:00 UTC + manual `workflow_dispatch`. Free-tier auto-pause permanently solved — no more manual dashboard restores. Deployed commit `bd67b99`. |
| 2 | find-a-teacher.html — online-only | `find-a-teacher.html` | "In-person" format chip removed per online-only strategy. `format` hardcoded to `'Online'`, validation updated, Location field relabelled "Location / timezone" with hint "All Piano Butler lessons are online". Ready for public launch. Deployed `bd67b99`. |
| 3 | Teacher outreach message drafts | `outreach-messages.md` (gitignored) | Copy-paste-ready recruitment messages: KR casual, KR polite, EN, + 1-week follow-up. Target: 3–5 founding teachers via Sohyun's network → then add teach-with-us link to homepage. |
| 4 | Weekly Monday auto-check (Cowork scheduled task) | Cowork `piano-butler-monday-check` | Runs Mondays 9:05am local: site health fetch, AdSense approval status, Search Console indexing progress. Briefs only when action needed. |
| 5 | SEO content experiment — ON HOLD | `_drafts/` (gitignored) | Generated 43 static pages: 3 guides (choosing AMEB pieces / board comparison / adult returners), 28 composer pages + hub (every piece per composer across all syllabuses, from live data), 9 grade comparison pages (AMEB vs ABRSM vs Trinity per grade), exam FAQ (FAQPage schema), best-G4-pieces article. Sohyun verdict: content feels generic/AI-ish — needs her real teaching voice before publishing. All index.html/sitemap.xml integrations reverted; site unchanged. Generator script preserved in session outputs (`gen_pages.js`). |

### Content Direction (pending decision as of 2026-06-12)
- Drafts live in `_drafts/` — restorable in minutes if direction is approved.
- Agreed fix if revived: data/reference pages (composer tables, grade comparisons) keep minimal factual intros; editorial articles wait for Sohyun's 5-min Korean voice-memo answers (favourite/overrated G4 pieces, her selection criteria, real student-rescue stories) → rewritten with byline "by Sohyun Park" (E-E-A-T).
- Explicitly NOT a blog — one-time evergreen reference pages, no recurring writing commitment.
- Viva voce / General Knowledge product idea raised: per-piece fact sheets (composer, era, form, Italian terms) as free web pages + paid printable PDF pack per grade on Gumroad ($4–7). Pilot one grade with Sohyun's accuracy review before scaling.

### Phase 56 Updates (2026-06-17 — viva-voce.html built + verified)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Viva Voce / General Knowledge pack generator built | `viva-voce.html` | New self-contained React 18 + Tailwind-free page (cdnjs-pinned React 18.2.0 / Babel 7.23.3, manual compile trigger — same pattern as Phase 42 fix). Teacher picks Grade (Prelim–G8, CertP, AMusA, LMusA) → Series (S19/S18/S17/Manual/AustAnth, dynamic per grade) → pieces (checkboxes, select-all/clear) → Generate → client-side jsPDF download. No backend, no login. |
| 2 | `buildPieceQA(piece, override)` rules engine | `viva-voce.html` | Generates per-piece "story" (🎼 Meet the Composer / 🕰️ Time Machine / 🎨 Colors / 🧱 How the Music is Built) + Q&A pairs, following actual AMEB GK exam rules (≥1 Q per List piece, 6–10 total, key changes only at clear-cut points, form from allowed list, period + timeframe, style tied to period). All content built from existing corpus fields (`c`,`t`,`nat`,`era`,`key`,`focus`) — no sheet-music content reproduced. |
| 3 | Tone — playful, not stiff | `viva-voce.html` | Per Sohyun's direction ("딱딱한 해석 보단 재밌게 풀어서 설명"): composer intro, era "time machine" narrative, key "color" framing, form "building blocks" framing — all written conversationally, not textbook-dry. |
| 4 | "NEEDS VERIFICATION" flagging — copyright/accuracy safeguard | `viva-voce.html` | Anything not confirmable from corpus metadata alone (modulation bar/destination key, key when corpus says "Variable", one concrete period-style feature actually present in the piece) is flagged amber and labelled "NEEDS VERIFICATION" with an instruction to check the real score — never guessed. Verified via direct data trace against real G5 S19 corpus pieces: flags appear correctly when data is missing, disappear correctly when a teacher override is supplied. |
| 5 | Optional accuracy-boost panel per piece | `viva-voce.html` | Teachers can expand a panel per selected piece to manually enter `modulation` (bar + destination key), `form` (override auto-inferred form), and `styleExample` (one concrete stylistic detail) — these override the corresponding NEEDS VERIFICATION flag in both the on-screen preview and the generated PDF. |
| 6 | Optional score image upload per piece | `viva-voce.html` | Per Sohyun's request ("악보를 올리면 더 자세하게 만들수 있는 툴... 4곡 정도 뽑는거니까"): teachers can attach a photo/scan of the score per piece via FileReader → base64 data URL, stored in React state only (no server upload, no automated image analysis). Embedded into the generated PDF as a "Reference score page (uploaded by teacher — for your own cross-checking only)" image block via jsPDF `addImage`, with try/catch fallback if embedding fails. |
| 7 | PDF generation — `generatePDF()` | `viva-voce.html` | jsPDF 2.5.1, A4, orange cover band + "Before you start" + bold NEEDS VERIFICATION warning note, then per piece: Part 1 (Key Points to Remember — story items) + Part 2 (Expected Q&A) + optional score image, then General reminders (`CORE_QA`) at the end. Pagination via `ensure(space)` called before every block (header, each story item, each QA item, image) — verified no block can be written without first reserving space, so nothing clips across a page break. |
| 8 | Full verification pass | `viva-voce.html` | (a) Babel-compiled output passed `node --check` syntax validation; (b) full manual code review of override-merging, state-keying (`composer+'|'+title` consistent across `selected`/`overrides`/`generatePDF`), and corpus-loading; (c) explicitly checked `buildCorpus()`'s `typeof DATA_GX` references against actual `const` export names in all 12 loaded data files — confirmed NO repeat of the Phase 12 (`DATA_G5_1`) / Phase 54 (`DATA_G6_COMP`) silent-data-loss bug; (d) concrete data trace of `buildPieceQA` against real G5 S19 pieces (17 found), both with and without overrides — output confirmed correct and well-formed. |
| 9 | Not yet linked from homepage | `index.html` | `viva-voce.html` is a standalone page (`noindex, follow`), not yet linked from nav/footer. Sohyun to open and spot-check in a real browser before deciding whether/how to surface it publicly. |

### viva-voce.html Architecture

```
viva-voce.html
├── CDN: React 18.2.0 + ReactDOM 18.2.0 + Babel 7.23.3 (cdnjs pinned) + jsPDF 2.5.1
├── Manual Babel compile trigger — two raw blocks: #app-jsx (engine) + #app-main (App)
├── ERA_TIMEFRAME / ERA_STYLE_FEATURES / ERA_TIME_MACHINE / ALLOWED_FORMS / KEY_VIBES
├── inferForm(piece) / keyVibe(key)         — heuristic inference from focus/title/key text
├── buildPieceQA(piece, override)           — story[] + qa[], NEEDS VERIFICATION flags
├── CORE_QA                                  — general exam-format reminder
├── buildCorpus()                            — Prelim–G8 + CertP + AMusA + LMusA (12 data files)
├── generatePDF(gradeLabel, seriesLabel, pieces, overrides) — jsPDF cover + per-piece pages + image embed
└── App()
    ├── state: grade, series, selected{}, overrides{}, showBoost{}, generating
    ├── gradePieces / seriesOptions / visiblePieces / selectedPieces (useMemo)
    ├── toggle / selectAll / clearAll
    ├── setOverrideField / handleScoreUpload (FileReader→base64) / removeScoreUpload / toggleBoost
    └── handleGenerate → generatePDF()
```

### Phase 57 Updates (2026-06-20 — timeline.html quality pass)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Phase pacing fixed — `allocatePhases()` | `timeline.html` | Replaced ratio-based `getPhase()` (caused duplicate phase labels on short timelines, e.g. July/August both "Development & Technique") with an explicit month-count-based allocator. Hard-coded phase sequences for 1–6 total months; proportional allocation with guaranteed minimum 1 month/phase for 7+ months. Exam month always last. |
| 2 | Phase split — Technical Foundation / Musical Shaping | `timeline.html` | Old single "Development" phase split into `technical` (cyan) and `musical` (purple) sub-phases in `PHASE_META`, each with distinct `MONTH_FOCUS` text — addresses visually identical consecutive months. |
| 3 | Personalized advice text — `fillTemplate()` | `timeline.html` | `MONTH_FOCUS` strings now use `{grade}`/`{syllabus}`/`{piece1–4}` placeholders, substituted with the student's actual grade/syllabus/pieces. Falls back to generic phrasing ("your first piece") when pieces aren't supplied — fully backward compatible. |
| 4 | New Step 4 — real exam piece input | `timeline.html` | New `PieceInput` component + `searchGradePieces()` helper. Student can search/select up to 4 actual exam pieces (autocomplete against CORPUS, filtered by chosen syllabus + grade) or skip. Inserted between exam-date and readiness-quiz steps — flow is now 6 steps (was 5). |
| 5 | Results screen — "Your exam pieces" section | `timeline.html` | When pieces were supplied, a dedicated card section shows them above the repertoire sample; the random `pickRepertoire()` sample is relabeled "More repertoire ideas for this grade" (supplementary) instead of being the only repertoire shown. |
| 6 | Verification | — | Extracted and Babel-compiled (`@babel/standalone`, React preset) the full `#app-jsx` script block, then ran `node --check` on the compiled output — confirmed syntactically valid before deploy. |
| 7 | Deployed | `timeline.html` | Commit `050377b` pushed to `main` by user from Terminal — live via GitHub Pages auto-deploy. |

### Phase 58 Updates (2026-07-19 — privacy policy deploy + June backlog cleanup)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Discovered uncommitted Jun 24 session work | — | Working tree contained an entire uncommitted session from 2026-06-24: new `about.html` + `privacy.html`, footer links in `index.html`, sitemap entries, a timeline.html overflow-text fix, and the Phase 57 CLAUDE.md log itself. None of it had been deployed — meaning the site had NO privacy policy while AdSense review was pending, a likely cause of the month-long approval delay. |
| 2 | Critical pre-deploy verification pass | `index.html`, `timeline.html`, `sitemap.xml`, `about.html`, `privacy.html` | Babel-compiled both JSX blocks + `node --check` (passed); sitemap XML validated; all internal links resolved; timeline overflow-suffix logic simulation confirmed no consecutive duplicate month text. Found 2 real errors: about.html claimed "4 exam boards" (actually 3 — AMEB/ABRSM/Trinity), and about.html linked to `teach-with-us.html`, which is strategically hidden until founding teachers are recruited (Phase 54 decision). |
| 3 | Minimal privacy-only configuration (Sohyun's decision) | `privacy.html`, `index.html`, `sitemap.xml`, `about.html` (deleted) | Sohyun opted for the minimum required footprint: `about.html` deleted entirely (footer link + sitemap entry removed); `privacy.html` trimmed from 8 sections to the 4 that matter — (1) Information we collect, (2) Cookies and advertising incl. Google AdSense third-party-cookie disclosure + adssettings.google.com opt-out (the AdSense-mandated wording), (3) Third-party services (AdSense/YouTube/Web3Forms/GitHub Pages), (4) Contact. "Last updated" set to 19 July 2026. |
| 4 | Deployed | commits `6f93f2b` + `3c32931` | Pushed to `main` by Sohyun from Terminal (050377b..3c32931). Verified live: privacy.html renders correctly at thepianobutler.com/privacy.html, index.html footer shows Privacy Policy button, timeline overflow fix live. |
| 5 | timeline.html overflow-text fix (from Jun 24, now live) | `timeline.html` | `OVERFLOW_SUFFIXES` cycle appended once a phase's MONTH_FOCUS strings run out — long timelines (17+ months) no longer show the exact same paragraph two months running. |
| 6 | Chrome extension never connected this session | — | AdSense dashboard check, Search Console check, and live browser spot-checks of timeline/viva-voce could NOT be done — Claude-in-Chrome extension unreachable throughout. All carried over to next session. |


### Phase 59 Updates (2026-07-21 — blank-page bug hunt, Search Console recovery, viva-voce PDF fix)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Root cause of AdSense rejection corrected | — | Previous assumption (missing privacy policy) was wrong. Live-diagnosed via Chrome: 14 of ~39 public pages (G5, G6 comprehensive, Trinity Initial–G8 × 9, Trinity Diploma ATCL/LTCL/FTCL × 3) were rendering as fully blank white pages for every visitor — almost certainly the real cause of both the AdSense "no content" rejection and the Search Console indexing stall. |
| 2 | G5/G6 bug fixed | `G5/piano-repertoire_g5.html`, `G6/piano-repertoire_g6.html` | A single missing comma inside the `COMPOSER_LINKS` object broke the entire ~76,000-character inline `<script>` block silently — a syntax error in a classic script kills the whole tag with no hoisting and no partial execution. Fixed, verified with `node --check` and a live render (41 pieces in List A rendering correctly). |
| 3 | Trinity Diploma bug fixed (3 files) | `Trinity/Diploma/piano-repertoire_trinity_{atcl,ftcl,ltcl}.html` | Every curly brace in the `<style>` block and the JSX script block had been doubled at some point — including already-correct `style={{...}}` becoming `style={{{{...}}}}`. Fixed via regex "halving" (each `{`/`}` run replaced with half its length) applied separately to the style and script spans, using `git show HEAD:<path>` to recover clean source since the sandbox can't `git checkout`. |
| 4 | Trinity Initial–G8 bug fixed (9 files) | `Trinity/{Initial,G1..G8}/piano-repertoire_trinity_*.html` | Every `style={...}` JSX attribute (25 per file) was missing its inner object-literal brace — `style={maxWidth:900,...}` instead of `style={{maxWidth:900,...}}`. Fixed via regex `style=\{([^{}]*)\}` → `style={{\1}}` per file (pre-existing correct `style={{` instances on G6–G8 were correctly skipped). |
| 5 | Full 41-file regression audit | all public HTML pages | Automated `node --check` (plain JS) + `@babel/core` transform (JSX) pass across every public page — matches the actual browser rendering pipeline rather than guessing. Confirmed no other page has this class of bug, and separately ruled out a second bug class (runtime variable-name mismatches, à la Phase 12/54's `DATA_G5_1` / `DATA_G6_COMP` silent-data-loss bugs) on `index.html`, `diagnose.html`, `recommend.html`, and the remaining un-indexed pages. |
| 6 | Search Console access restored | Google account vividssso@gmail.com | The account had zero registered Search Console properties despite full, working AdSense access on the same account — genuinely had no prior verification on file. Added a second `google-site-verification` meta tag to `index.html` (kept the original) and re-verified via the HTML-tag method. |
| 7 | Re-indexing requested — 19 of 23 target URLs | Search Console URL Inspection | Submitted: G5, G6, all 3 Trinity Diploma pages, all 9 Trinity Initial–G8 pages, ABRSM LRSM, ABRSM G2/G4/G6/G7, and G8 comprehensive. Hit Google's daily indexing-request quota after 19 submissions — LMusA, `diagnose.html`, and `recommend.html` are still queued; resume when the daily quota resets. |
| 8 | `timeline.html` live-tested end to end — no bugs found | `timeline.html` | First-ever live spot-check (previously unverified since Phase 57). Full flow confirmed working: syllabus → grade → exam date → the newer piece-search step (autocomplete correctly filters by grade + syllabus) → readiness quiz → 18-month plan. Also confirmed the Phase 57 duplicate-month-text fix works live — `OVERFLOW_SUFFIXES` correctly varies repeated phase text instead of showing two identical paragraphs back to back. |
| 9 | `viva-voce.html` live-tested — real bug found (caught by Sohyun) | `viva-voce.html` | First-ever live spot-check (previously unverified since Phase 56). Sohyun spotted it from a real generated-PDF screenshot: the 🎼🕰️🎨🧱 emoji in story-section labels were rendering as garbled bytes ("Ø<ß¼") because jsPDF's built-in Helvetica font only supports WinAnsiEncoding, not emoji — and that same broken character was also corrupting jsPDF's character-width table for the rest of that line, which is what caused the visible letter-stretching and right-edge text cutoff in the same screenshot. |
| 10 | `viva-voce.html` fix deployed | `viva-voce.html` | Removed emoji from the 4 hard-coded story labels (`Meet the Composer` / `Time Machine` / `Colors` / `How the Music is Built`). Added a `stripEmojiForPDF()` safety net inside `wrapText()` so any future emoji — hard-coded or typed by a teacher into an accuracy-boost field — can't reintroduce this bug. Verified via Babel compile + `node --check` + a direct Node.js trace of `buildPieceQA()` output (confirmed zero non-ASCII characters in the labels), then re-verified live on the redeployed site: clean PDF regeneration, no console errors. |
| 11 | Confirmed `viva-voce.html` / `timeline.html` are pre-launch prototypes | — | Neither is linked from site nav or footer, and both are `noindex`. `viva-voce.html`'s AMEB-only scope is intentional, not a gap — "General Knowledge" (viva voce) is specifically an AMEB Comprehensive Piano syllabus exam component; ABRSM and Trinity don't have the same requirement. |
| 12 | Monday scheduled task rewritten | Cowork scheduled task `piano-butler-monday-check` | Updated with the 2026-07-21 baseline (20/39 indexed, 14 clicks/2mo), an explicit instruction not to click AdSense "request review" until indexing recovers, and a mandatory "partner recommendation" section that forces one concrete next action every week instead of a passive status dump. |
| 13 | CLAUDE.md restructured | `CLAUDE.md` | Removed 73 duplicate "Build Status" / "Pending Work" / "Known Issues" sections scattered across Phases 1–58 (~690 lines of redundant, frequently stale copies) and replaced them with one consolidated, accurate "Current Status" section at the end of this file. Added a "Top Priority — Read This First" section near the top per Sohyun's explicit instruction to keep surfacing critical, revenue-focused points every session. |

---

### Phase 60 Updates (2026-07-22 — find-a-teacher.html pricing + timeline.html real curriculum)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Final 3 re-indexing requests submitted | Search Console URL Inspection | LMusA, `diagnose.html`, `recommend.html` — the 3 URLs still queued from Phase 59's daily-quota cutoff. All 23/23 target pages now resubmitted for re-crawl. |
| 2 | find-a-teacher.html — pricing + payment CTA added | `find-a-teacher.html` | Per Sohyun's decision (AskUserQuestion: $25 AUD, Stripe Payment Link): added a `$25 AUD · one-off session · online` hero badge, a price line in the step-4 summary card, and a post-submit payment prompt. `STRIPE_PAYMENT_LINK` constant left empty with a TODO comment — until Sohyun creates the real Stripe Payment Link and supplies the URL, the button shows "we'll email you a payment link" instead of a dead link. Verified via Babel compile + `node --check`. |
| 3 | AMEB Technical Work syllabus data extracted | `AMEB Syllabus/technical pre-4 list.pdf`, `AMEB Syllabus/technical 5-8 list.pdf` | Both PDFs are scanned/image-based (no text layer) — rasterized via `pdftoppm` and read visually, page by page, Preliminary through Grade 8. Transcription cross-checked against each grade's own item-numbering range (e.g. Grade 6 = "6.1–6.23" = 23 items) as an accuracy check — all 9 grades matched exactly. |
| 4 | `data_technical_ameb.js` created | `data_technical_ameb.js` (new, root level) | Structured data: per grade (Prelim–G8), the named Technical Exercises (code + pedagogical purpose + piece names) and every scale/arpeggio/chord-progression requirement section, verbatim from the syllabus. AMEB only — ABRSM/Trinity have different technical requirements, and AMEB Diploma grades (CertP/AMusA/LMusA) have no fixed technical-exercise list in this format. |
| 5 | `timeline.html` — real curriculum content | `timeline.html` | Per Sohyun's request to make the timeline "실라버스를 포괄해서... 커리큘럼자체로" (cover the syllabus, become a real curriculum) rather than generic template phrases. Added `getTechnicalWork(syllabus, gradeKey)` (returns real data for AMEB Prelim–G8, `null` otherwise) and `buildTechnicalFocusLines(tech)`, which replace the generic `MONTH_FOCUS.technical` template text with grade-specific paragraphs naming the actual required exercises and scales. Also added a new "Technical Work Checklist" card block on the results screen showing the full exercise list and every scale/arpeggio section for the chosen grade, straight from the syllabus. Scoped to AMEB only for this pass (ABRSM/Trinity/sight-reading data intentionally deferred, per this session's scope-discipline agreement). |
| 6 | Verification | — | Babel-compiled the full `#app-jsx` block + `node --check` on the output (both clean); separately traced `getTechnicalWork()`/`buildTechnicalFocusLines()` in isolation for two different grade shapes (G5 — has a plain "Scales" section; G7 — has no "Scales" section, starts with "Abbreviated grand scale format", tests the fallback path) and confirmed correct output for both, plus confirmed `null` fallback for ABRSM/Trinity/Diploma grades. |
| 7 | Live-tested end to end post-deploy — confirmed working, one caching gotcha found | `timeline.html` | First live run (AMEB → Grade 5 → 17-month date → skip pieces → quiz → results) initially showed the OLD generic text — `typeof DATA_TECHNICAL_AMEB` was `undefined` in that tab even though a cache-busted `fetch()` of the live HTML confirmed the new `<script src="data_technical_ameb.js">` tag and code were correctly deployed. Root cause: browser/CDN cache serving a stale pre-deploy version of `timeline.html` to a tab that was opened moments before the push finished propagating — not a code bug. A hard reload (`?v=2` cache-bust) picked up the new version correctly: Nov 2026 through Jan 2027 month cards showed the real Grade 5 exercise/scale text (5A/5B/5C, full scale list, arpeggios), and the new "Grade 5 Technical Work Checklist" card rendered all exercise + scale/arpeggio sections correctly. Zero console errors throughout. |

---

### Phase 61 Updates (2026-07-22 — timeline.html restricted to AMEB only)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Syllabus picker removed | `timeline.html` | Per Sohyun's explicit decision: she has taught and personally sat AMEB exams, not ABRSM/Trinity, and didn't want the planner implying expertise it doesn't have — especially since the ABRSM/Trinity path only ever showed generic template text (no real technical-work data exists for those boards). Step 0 (syllabus picker) removed entirely; the wizard now starts directly on grade selection. `SYLLABUS = 'AMEB'` is now a fixed constant, not a state value. |
| 2 | Wizard renumbered 5 steps → 4 | `timeline.html` | Screens: 0=grade, 1=exam date, 2=pieces, 3=quiz, 4=results (was 0=syllabus…5=results). All `screen===N` checks, the progress bar percentages, "Step X of Y" header text, and Back/Next navigation targets updated and re-verified. |
| 3 | ABRSM/Trinity data removed from this page | `timeline.html` | All 20 ABRSM/Trinity `<script src=...>` tags and their `buildCorpus()` push() calls removed — this page no longer loads or references ABRSM/Trinity data at all (full multi-syllabus search remains unaffected on `index.html`). `GRADE_OPTIONS_BY_SYLLABUS` (3-syllabus map) replaced with a flat `GRADE_OPTIONS` array (AMEB's 12 grades: Prelim–G8, CertP, AMusA, LMusA). Unused `SYLLABUSES` array and `GRADE_ORDER` constant deleted. |
| 4 | Copy updated to be explicit about scope | `timeline.html` | Title/meta tags changed to "AMEB Exam Timeline". Grade-step heading changed to "Which AMEB grade are you sitting?" with a subtitle "Built for the AMEB Piano syllabus — Preliminary through Diploma." |
| 5 | Verification | — | Babel-compiled the `#app-jsx` block + `node --check` (clean); grepped for any leftover `DATA_ABRSM`/`DATA_TRINITY`/`SYLLABUSES` references (none found); confirmed `GRADE_OPTIONS` still lists all 12 correct AMEB grade keys. |
| 6 | Scope decision — Sight-Reading/GK stay generic | — | Asked Sohyun whether Sight-Reading and General Knowledge/Aural requirements should get the same real-data treatment as Technical Work. Her call: unlike scales/arpeggios (discrete, enumerable items), sight-reading and aural requirements aren't cleanly itemizable per grade the same way — general prep guidance is the right level for those, not a checklist. `MONTH_FOCUS` phase text for sight-reading/GK stays as generic reminders; only Technical Work gets real per-grade syllabus data. Not a "todo, do later" — this is the intended final shape. |
| 7 | Month-card technical text shortened | `timeline.html` | Sohyun feedback from real screenshots: the Sep/Oct 2026-style month cards were an unreadable wall of text (full exercise purposes + full comma-separated scale lists crammed into prose). `buildTechnicalFocusLines()` rewritten to name only the exercise codes and point to the Technical Work Checklist card below for full detail — removes duplication, each month card now 1-2 short sentences. |
| 8 | Technical Work Checklist card restyled as chips | `timeline.html` | The checklist's scale/arpeggio sections were a single dense `·`-joined paragraph. Rewritten as one consolidated card with internal section dividers, each scale/arpeggio item rendered as an individual pill/chip (`flex-wrap`) instead of run-on text — verified against real Grade 5 data (41+33+38+48+8 = 168 pieces, all accounted for). |
| 9 | Browsable piece picker added (no typing required) | `timeline.html` | Sohyun feedback: typing exact piece titles is effort. Added `browseGradePieces(syllabus, gradeKey)` — groups the grade's exam repertoire (Leisure excluded) by List A/B/C/D, sorted by composer. `PieceInput`'s suggestion panel now always shows something: the browsable grouped list by default, or live search results once the user types. Panel is a fixed-height (280px) scrollable box so it doesn't blow out page length. |
| 10 | Live-tested post-deploy — all three fixes confirmed working | `timeline.html` | Full run: AMEB → Grade 5 → date → pieces step showed "LIST A" sticky-header browse panel with real Grade 5 pieces, tapped one in without typing, filled the slot and auto-advanced correctly → quiz → results. Nov/Dec 2026 month cards showed the new short technical text (2 sentences, points to checklist) instead of the old wall of text. Technical Work Checklist rendered as one card with chip-pill scale/arpeggio items. Selected piece correctly appeared in the July/Aug month text and the "Your exam pieces" card. Zero console errors. |

---

### Phase 62 Updates (2026-07-22 — every phase specific + weekly breakdowns + density)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Sohyun feedback on results page ("이렇게만은 좀 부족하게 느껴지는데") | — | Asked via `AskUserQuestion` (multi-select) what specifically felt lacking. Answer: (a) other phases should be as specific as Technical, (b) month-level is too coarse — week-level plans needed too, (c) page looks visually sparse for the amount of studying required. All three addressed this session. |
| 2 | Piece slots now store full piece objects, not display strings | `timeline.html` | `PieceInput.choose()` now sets `pieces[slot] = p` (the whole corpus object) instead of a formatted string, so `.era`/`.focus`/`.c`/`.t`/`.l` survive into the results screen and into `buildTimeline()`. `anyFilled` / slot display / `App()`'s `userPieces` all updated accordingly (`pieces.filter(Boolean)` instead of `.filter(p=>p&&p.trim())`). |
| 3 | Every phase now has a real checklist builder, not just Technical | `timeline.html` | New per-phase functions — `foundationChecklist`, `technicalChecklist` (replaces the old `buildTechnicalFocusLines`), `musicalChecklist`, `consolidationChecklist`, `polishChecklist`, `examChecklist` — each returns 1–3 concrete checklist items for the given month-in-phase. `musicalChecklist` and `foundationChecklist` reference the student's actual chosen pieces by name when supplied; `musicalChecklist` specifically pulls each piece's existing `focus` keywords (already curated in the corpus, 3 per piece) and a new `ERA_MUSICAL_TIPS` dictionary (Baroque/Classical/Romantic/Modern/Contemporary — separate, shorter copy from `viva-voce.html`'s era content, which serves a different purpose) to generate era-appropriate shaping cues per piece. `technicalChecklist` still uses the real `data_technical_ameb.js` exercise/scale data, now shaped as short checklist bullets instead of paragraphs; falls back to a clear "no fixed technical list at Diploma level" message for CertP/AMusA/LMusA. |
| 4 | `MONTH_FOCUS` lead sentences shortened, piece-placeholders removed | `timeline.html` | The old `{piece1}`–`{piece4}` template substitution inside `MONTH_FOCUS` strings is gone — piece-specific detail now lives entirely in the new checklists (avoids duplicating the same piece name in both the lead sentence and the checklist below it). `fillTemplate()` simplified to just `{grade}`/`{syllabus}` substitution. |
| 5 | Week-by-week breakdown added to every month | `timeline.html` | New `WEEKLY_TEMPLATES` — one array of exactly 4 week-level lines per phase (same 4 for every month within that phase, since the month-to-month progression is already carried by the lead sentence + checklist). `buildMonthContent()` now returns `{ lead, checklist, weekly }` per month; `MonthCard` renders `weekly` behind a collapsible "▸ Week by week" toggle (per-card local state) so the page gains real week-level structure without forcing every month open by default. |
| 6 | Visual density — checklist bullets + chip-style badges | `timeline.html` | `MonthCard` now renders the lead sentence, then a checkmark (✓) bullet list for the checklist (phase-coloured checkmarks), then the collapsible weekly block — three distinct visual layers per month instead of one paragraph. The "Your exam pieces" card was upgraded to show era badge + full focus-tag chips per piece (previously just plain text), using the piece-object data now retained from step 2. |
| 7 | Verification | — | Babel-compiled the full `#app-jsx` block with the browser's actual transform settings (classic runtime, matching `Babel.transform(src,{presets:['react']})`) + `node --check` on the output (both clean). Built a Node logic-test harness (stubbed `React`, loaded real `data_technical_ameb.js` + `G5/data_g5_1.js`) and directly exercised `buildTimeline()`/`buildMonthContent()`/each checklist builder against real Grade 5 corpus pieces: confirmed correct, era/focus-aware checklist output both with and without user-supplied pieces; confirmed the AMusA (Diploma, no technical data) fallback message; confirmed short (2-month) and long (20-month) timelines don't crash and correctly cap at each checklist's last stage via `Math.min`; grepped the source to confirm no leftover references to the old `buildTechnicalFocusLines`/`techFocusLines`. |
| 8 | Live-tested end to end post-deploy — confirmed working | `timeline.html` | Commit `545ccc6` pushed by Sohyun, deploy confirmed via cache-busted origin fetch before navigating. Full run: AMEB → Grade 5 → 17-month date → searched/browsed 2 real pieces (Arne Gigue via browse list, Chopin Polonaise via search) → readiness quiz → results. Confirmed live: Foundation months show piece-specific checklist items ("Hands-separate read-through: Gigue 2nd mvt..., Polonaise..."), Technical Foundation months name the real exercise codes (5A/5B/5C), Musical Shaping correctly generates era-specific shaping tips per piece (Baroque piece → "even touch, light pedal..."; Romantic piece → "singing tone, purposeful rubato..."), Consolidation/Polish reference the pieces and technical codes too. "▸ Week by week" toggle expands/collapses correctly showing 4 week rows. "Your exam pieces" card shows era badge + real focus-tag chips per piece (Triplets/Clarity/Compound time; Polonaise/Nobility/Dance character). Technical Work Checklist card renders correctly. Zero console errors throughout. |

---

### Phase 63 Updates (2026-07-23 — AdSense audit: found the real blocker)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | outreach-messages.md checked | — | Still unsent. No change since Phase 55. Flagged again as the highest-leverage idle lever. |
| 2 | Git/deploy state checked | — | Working tree was clean, nothing uncommitted since Phase 62 — all prior work already pushed and logged. |
| 3 | Search Console live-checked | Google Search Console | Still 20/39 indexed — unchanged from the 2026-07-21 baseline. Data shown was last updated 2026-07-10, i.e. it does **not yet reflect** the July 21 blank-page fixes or the 23 re-indexing requests submitted since — too early to read anything into the flat number. Total clicks: 15 (was 14) — essentially flat. Not-indexed breakdown: 16 "Discovered — currently not indexed", 2 "Crawled — currently not indexed", 1 duplicate/alternate-canonical page. |
| 4 | **AdSense site status live-checked — found a real, concrete blocker** | Google AdSense → Sites | Site row for thepianobutler.com shows 승인 상태 (approval status): **주의 필요** (needs attention), reason given: "Google ads served on screens without publisher content, low-value content" — dated **2026-06-21**, i.e. this predates the July 21 blank-page-bug fixes entirely and may already be stale, but has not been refreshed since. Separately and more concretely: **Ads.txt 상태 (ads.txt status) showed 찾을 수 없음 — "not found."** The site had no `ads.txt` file at all. This is an unambiguous, independently-fixable technical gap (distinct from the "low-value content" flag, which may just be a stale artifact of the pre-fix blank pages). |
| 5 | Policy Center checked | Google AdSense → Policy Center | "현재 정책 위반 문제 없음" — no active policy violations on the account right now. This is reassuring: the site-level "주의 필요" tag is most likely a stale snapshot from before the July 21 fixes, not a live, current violation. |
| 6 | Payment info checked (view only — not touched) | Google AdSense → Payments | Still shows "1개/2개" — payment info has not been completed. **This requires Sohyun personally** — entering bank/address details is outside what Claude can do (financial-credentials policy). Genuinely blocks getting paid even after approval, independent of the content/indexing questions. |
| 7 | `ads.txt` created and committed | `ads.txt` (new, repo root) | `google.com, pub-6523454944716812, DIRECT, f08c47fec0942fa0` — the standard required line for a direct AdSense publisher, using the exact `pub-` ID confirmed from the live `adsbygoogle.js` script tag in `index.html`. Committed locally (`18544d9`) but **not yet pushed** — per the standing git-sandbox limitation, Sohyun needs to run `git push` from her own Terminal. |
| 8 | CLAUDE.md restructured — Current Status section updated | `CLAUDE.md` | Revenue-critical status table and pending-work list below updated to reflect today's findings. File Structure section (top of doc) refreshed — see #9. |
| 9 | File Structure section refreshed | `CLAUDE.md` | The section near the top of this doc was stale since before Trinity/CertP/diploma expansion. Updated to reflect the current top-level layout (see "File Structure" near the top). |

---

### Phase 64 Updates (2026-07-27 — traffic inflection confirmed, butler.html rescued, diploma-page CTR fix)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | `ads.txt` confirmed live | `thepianobutler.com/ads.txt` | Fetched directly — serving correctly (`google.com, pub-6523454944716812, DIRECT, f08c47fec0942fa0`). Commit `18544d9` had already been pushed (0 commits ahead/behind `origin/main`) — the Phase 63 note that it was "not yet pushed" is now stale. AdSense's Ads.txt column still reads 찾을 수 없음 in the dashboard, but its last-updated timestamp is 2026-06-21 — over a month stale, predates the fix entirely. Not yet re-crawled, not a real problem. |
| 2 | **Search Console — real traffic inflection found** | Google Search Console | Last 7 days (Jul 18–24): 12 clicks / 770 impressions — that's 46% of all clicks and 50% of all impressions in the entire trailing 3-month window, in one week. Weekly impressions went from a ~100/week baseline to 770, and the daily chart was still climbing on the last day, not peaking. Timing lines up exactly with the July 21 blank-page fixes going live and getting re-crawled. 35 distinct pages now earn impressions (vs. 20 in the stale indexing report). |
| 3 | Traffic source identified — diploma pages, not grade pages | — | Top impression pages this week: Trinity ATCL (108 impr, 0 clicks), ABRSM LRSM (97 impr, 1 click), ABRSM G2 (52 impr, 1 click), Trinity LTCL (45 impr, 1 click), ABRSM G4 (37 impr), Trinity G7 (22 impr). Top queries: `lrsm piano repertoire list`, `atcl piano syllabus 2026`, `trinity atcl piano syllabus 2026` — low-competition diploma-syllabus searches nobody else has indexed as a browsable list. This is the site's actual current moat, not the grade pages the SEO effort has mostly focused on to date. |
| 4 | Bottleneck identified: CTR, not indexing | — | Trinity ATCL at 108 impressions / 0 clicks and avg. position ~15–18 means it's ranking (page 2) but the title/snippet isn't earning the click. This is now the highest-leverage lever available — cheaper and faster than waiting on further indexing recovery. |
| 5 | Diploma page `<title>`/`<meta description>` rewritten for CTR | `ABRSM/Diploma/piano-repertoire_abrsm_{lrsm,frsm}.html`, `Trinity/Diploma/piano-repertoire_trinity_{atcl,ltcl,ftcl}.html` | Rewrote to match actual query phrasing found in Search Console and lead with the concrete piece count, e.g. `"ATCL Piano Diploma Syllabus 2026 — Full Repertoire List (241 Works) | Piano Butler"`. See table below for the full before/after. |
| 6 | **Rescued uncommitted local work — `butler.html`** | `butler.html`, `butler-engine.js`, `butler-engine.test.js`, `data_aural_ameb.js`, `serve-butler.py`, `Open Piano Butler.command` (all new) | Found sitting untracked in the folder, undocumented anywhere in this file, with no prior mention in chat history. Turned out to be a real, finished feature: a daily practice-rotation companion covering AMEB technical work + aural + sight-reading + viva voce coverage, least-recently-practiced-first scheduling, exam lockdown mode (last 8 weeks serves one item per area instead of rotating), and per-student exclusion switches for Leisure/untaught/exempt items. `butler-engine.js` is pure logic (no DOM) with a 67-assertion test suite (`node butler-engine.test.js`) traced against real Grade 5 syllabus data — all 67 pass. Terminal history showed Sohyun had already built and run it herself via `Open Piano Butler.command` on 2026-07-26 21:56, so it was already spot-checked live in a real browser before this session found it — not a repeat of the Phase 12/54/58 blank-page pattern. Committed (`57e7f5f`) so it can't be silently lost; not yet pushed (Sohyun pushes from her own Terminal), not yet linked from any public page, not yet decided whether it's a private teacher tool or a public feature. |
| 7 | Verification | — | `node butler-engine.test.js` → 67 passed, 0 failed, confirmed before committing. New diploma-page meta tags checked with `node --check` (N/A — HTML, not JS) and manual diff review; confirmed each title is unique across the 5 files (no duplicate-title regression). |

### butler.html Architecture

```
butler.html (private/undecided-scope local tool, noindex — not yet linked publicly)
├── data_technical_ameb.js   — existing file, AMEB technical exercises + scales/arpeggios Prelim-G8
├── data_aural_ameb.js       — NEW: AMEB aural test requirements Prelim-G8 (Manual of Syllabuses §21)
├── butler-engine.js         — pure rotation/coverage logic, no DOM, usable from node or browser
│   ├── AREAS                — aural / sightread / viva (drillable) + theory / gk (manual-only, no engine support)
│   ├── coverageKeys()       — flattens a grade's technical exercises + scale sections + aural tests + other areas into one list
│   ├── stalestFirst()       — the whole scheduling rule: never-practiced first, then least-recently-practiced
│   ├── planFor()            — pinned daily technical picks (2/day) + weekly area rotation (aural/sightread/viva, no area repeats back-to-back)
│   ├── examLocked()         — inside 8 weeks of the exam date, serves one item per area instead of rotating
│   └── isExcluded()/toggleExcluded() — per-student switches for Leisure/untaught/exempt items; excluded items leave both the rotation and the coverage denominator
├── butler-engine.test.js    — 67 assertions, run via `node butler-engine.test.js`, traced against real G5 data
└── serve-butler.py + "Open Piano Butler.command" — no-cache local dev server + double-click launcher (port 8899)
```

### Diploma Page Title/Meta Rewrites (Phase 64)

| Page | Old title (generic) | New title (query-matched, count-led) |
|------|---------|-------|
| ABRSM LRSM | ABRSM LRSM Diploma Piano Repertoire \| Piano Butler | LRSM Piano Repertoire List 2023 — 139 Diploma Works \| Piano Butler |
| ABRSM FRSM | ABRSM FRSM Diploma Piano Repertoire \| Piano Butler | FRSM Piano Repertoire List 2023 — 97 Diploma Works \| Piano Butler |
| Trinity ATCL | Trinity ATCL Diploma Piano Repertoire \| Piano Butler | ATCL Piano Diploma Syllabus 2026 — Full Repertoire List (241 Works) \| Piano Butler |
| Trinity LTCL | Trinity LTCL Diploma Piano Repertoire \| Piano Butler | LTCL Piano Diploma Syllabus 2026 — Full Repertoire List (306 Works) \| Piano Butler |
| Trinity FTCL | Trinity FTCL Diploma Piano Repertoire \| Piano Butler | FTCL Piano Diploma Syllabus 2026 — Full Repertoire List (155 Works) \| Piano Butler |

Rationale: Search Console's actual top queries for these pages are `lrsm piano repertoire list`, `atcl piano syllabus 2026`, `trinity atcl piano syllabus 2026` — phrase-matching the query in the title, and leading with the concrete work count (something a generic "browse our diploma repertoire" competitor snippet won't have), is the standard high-leverage CTR fix when a page already ranks but isn't clicked.

---

### Phase 65 Updates (2026-07-27 — full-site audit: syntax, canonical tags, data integrity, live spot-check)

Requested by Sohyun as a genuine full sweep after Phase 64's targeted fixes, not just a repeat of "what changed today." Four separate checks, each automated rather than sampled by hand, plus a live-browser pass:

| # | Check | Method | Result |
|---|-------|--------|--------|
| 1 | Inline-script syntax audit, all 47 public/gated HTML pages | Wrote a Node script (`@babel/core`, `runtime:'classic'` to match the site's actual in-browser Babel Standalone config — same method as Phase 59/62) that extracts every non-`src` `<script>` block per page and compiles it. Two false positives in the tool itself were found and fixed mid-run: (a) Babel's default automatic JSX runtime injects an ES `import` that a plain `vm.Script` check then rejects — fixed by forcing `runtime:'classic'`; (b) `<script type="application/ld+json">` blocks aren't JS and were wrongly run through the JS compiler — fixed by checking those with `JSON.parse` instead. | **0 real errors across all 47 pages.** No repeat of the Phase 12/54/58/59 blank-page bug class. |
| 2 | `index.html` data-loading cross-check | Extracted every `typeof X` guard in `index.html` and every actual `const NAME =` export across all 44 loaded `data_*.js` files, then diffed the two sets programmatically (rather than eyeballing one file at a time, which is exactly how Phase 12's `DATA_G5_1` and Phase 54's `DATA_G6_COMP` mismatches went unnoticed for weeks). | **All 44 match.** No silent-data-loss bug present anywhere in `index.html` right now. |
| 3 | Canonical tag audit, all 47 pages | Regex-extracted `<title>`, `<meta description>`, `<link rel=canonical>`, `<meta robots>` from every page; checked for missing tags, stale `vividssso-pixel.github.io` URLs, and duplicate titles. | Confirmed the exact scope of the gap flagged in Phase 64: **27 grade pages (all 9 AMEB + all 9 ABRSM + all 9 Trinity) had no canonical tag at all**, plus `recommend.html` (not previously flagged). **Fixed all 28** — added self-referencing `https://thepianobutler.com/<path>` canonical tags, matching the existing pattern on `index.html`/`diagnose.html`/the diploma pages. No duplicate titles found anywhere on the site. |
| 4 | Data integrity re-check, all 44 `data_*.js` files (4,500 pieces) | Loaded every file in a Node `vm` sandbox, summed piece counts per file against the exact numbers in this file's own "Verified Piece Counts" tables, and scanned every piece for invalid `era`, `focus` arrays not exactly length 3, and empty `nat`. | **All 44 files match their documented count exactly** (grand total 4,500, incl. G6 Comprehensive's inline-only 160). **0 invalid era, 0 malformed focus arrays, 0 empty nationality** across all 4,500 pieces — the Phase 27/33/40 data-quality fixes have held. |
| 5 | Live browser spot-check (real thepianobutler.com, not local files) | Navigated to `index.html`, `G5`, `ABRSM/Diploma/LRSM`, `Trinity/G7`, `Trinity/Diploma/ATCL`, `diagnose.html`, `recommend.html`, `timeline.html`, `viva-voce.html` and read both rendered content and the browser console. | **All render correctly with real content, zero console errors.** (Live pages still show pre-Phase-64/65 titles since none of today's 3 commits have been pushed yet — expected, not a bug.) |
| 6 | Documentation-drift bug found | While building the file list for this audit, `connect.html` — still referenced in this file's own Pending Work as an existing deferred feature — turned out **not to exist on disk at all**, almost certainly removed in Phase 54's "17 unused files deleted" cleanup without updating the reference. Corrected below. | Pending Work item removed/corrected. |

**What this audit does NOT cover** (scope boundary, stated plainly rather than implied): the `_drafts/` content-experiment pages (intentionally on hold since Phase 55, excluded here on purpose), a re-verification of every individual piece's title/composer/era against the source syllabus PDFs (last done piecemeal across Phases 1–40), and Supabase/teacher-dashboard functional testing (no Supabase-dependent flow was exercised this session).

---

### Phase 66 Updates (2026-08-03 — live Search Console review, AMEB-first strategy, internal linking)

Live session in Google Search Console (Chrome connected, account vividssso@gmail.com) rather than reading stale exported numbers — first time this was done interactively rather than via scheduled-task screenshots.

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Search Console indexing — confirmed recovery | — | 35/40 pages indexed (up from the 20/39 baseline). The 5 not-indexed: 1 alternate-canonical (`index.html` vs. root `/`, expected/fine), 1 "discovered — not indexed" (`privacy.html`, low priority), 3 "crawled — currently not indexed": **G3, G4 (AMEB Comprehensive), and ABRSM G5**. |
| 2 | Traffic snapshot (3-month) | — | 38 clicks / 3.36k impressions, avg CTR 1.1%, avg position 17.3. Top query: `lrsm piano repertoire list` (126 impr / 1 click). Country breakdown: **Australia #1 by clicks (17 of 38, ~45%), 662 impressions**; UK #2 by impressions (560) but only 3 clicks — UK impressions are diploma-page-driven but converting poorly, Australia converts well. |
| 3 | Strategic decision — AMEB-first (Sohyun's call) | — | Sohyun directed: prioritize AMEB (Prelim–G8 + CertP/AMusA/LMusA) over ABRSM/Trinity going forward, since AMEB is the dominant board in Australia (confirmed by the country data above) and matches her own teaching background. This also happens to be where the 2 stuck-indexing pages (G3, G4) live, so priority and problem overlap. |
| 4 | G3, G4 re-indexing requested | — | URL Inspection confirmed both pages' canonical tags **are** live and correct (self-referencing, `meta-robots: index, follow` — the Phase 65 fix did ship). Search Console just hadn't re-crawled since 2026-06-07. Re-indexing requested for both via URL Inspection on 2026-08-03. |
| 5 | Diploma-page exam-syllabus content — considered, declined | — | Raised as a possible next step (LRSM/FRSM/ATCL/LTCL/FTCL pages currently have zero exam-requirement context, just a bare repertoire list) but Sohyun correctly pushed back: Piano Butler is a **search tool**, not a syllabus-content site — reproducing official exam requirements duplicates the official boards' own pages and adds an ongoing maintenance burden outside the site's positioning. Not implemented. If revisited later, the lighter-weight version is a single outbound link to the official ABRSM/Trinity syllabus page rather than reproducing the requirements. |
| 6 | AMEB grade-to-grade internal nav links — added to all 12 pages | `Prelim/piano-repertoire_prelim.html`, `G1–G8/piano-repertoire_gX.html`, `CertP/piano-repertoire_certp.html`, `AMusA/piano-repertoire_amusa.html`, `LMusA/piano-repertoire_lmusa.html` | Each page now has a horizontally-scrollable pill-strip nav ("AMEB grades: Prelim · G1 · G2 · … · LMusA") near the header, linking to all 11 other AMEB pages with the current page highlighted. Purely internal navigation/structured-data-adjacent SEO — not new editorial content, consistent with the "search tool, not content site" scope Sohyun confirmed in this same session. Comprehensive pages (Prelim–G8, indigo theme) got the strip inserted right after `</header>`; the 3 dark-header diploma pages (CertP teal, AMusA/LMusA purple) got it inserted between the header gradient block and the sticky filter bar, styled to match each page's own accent colour. |
| 7 | Verification | — | All 12 files' `<script type="text/babel">` blocks compiled via `@babel/core` `transformSync` with `runtime:'classic'` (matching the site's actual in-browser Babel Standalone config, same method as Phase 59/62/65) + a `new Function()` syntax check on the compiled output — **0 errors across all 12 files** before committing, given this project's history of blank-page bugs from bad JSX edits (Phase 12/54/58/59). |
| 8 | Committed and deployed | commit `ea87edb` | Committed locally, Sohyun ran `git push` from her Terminal, GitHub Actions deployed to `gh-pages`. **Live-verified in Chrome** (not just assumed from the commit): both `G3/piano-repertoire_g3.html` and `AMusA/piano-repertoire_amusa.html` render the new nav strip correctly, current page correctly highlighted, zero visual/console issues. |
| 9 | Monday scheduled task upgraded to a daily pulse check | Cowork scheduled task `piano-butler-monday-check` (task ID unchanged, cadence and prompt changed) | Per Sohyun's request for closer/"real-time" monitoring. Honest caveat given to her: true real-time isn't possible (Search Console data itself lags 2–3 days, and scheduled tasks only run while the app is open) — landed on a **daily 9am short pulse check** instead, instructed to say "no change" tersely on quiet days rather than manufacture false signal, and to escalate clearly the moment Australia clicks, G3/G4 indexing, or the 5 retitled diploma pages' CTR actually move. Full new baseline (35/40 indexed, 38 clicks/3.36k impr 3-month, Australia country breakdown, G3/G4 reindex pending, nav-links deployed) written into the task prompt so tomorrow's run has correct context without needing this file. |

---

### Phase 67 Updates (2026-08-13 — AdSense root cause found, ABRSM data repair, homepage content grid)

Started as a routine daily pulse check; the AdSense finding turned it into a build session.

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | **AdSense flag is no longer stale — and it's diagnosable** | Google AdSense → Sites | The site row still reads 주의 필요 ("ads served on screens without publisher content, low-value content"), but its **last-updated stamp is now 2026-08-08** (was 2026-06-21). Google re-assessed *after* the July 21 blank-page fixes and the verdict stood. The previous "wait for the stale flag to refresh" plan has resolved, and it resolved against us. Ads.txt separately flipped to **승인됨** — that gap is closed. Policy Center still shows zero active violations. |
| 2 | **Root cause identified: the ad script was on the thinnest page on the site, and nowhere else** | `index.html` (was the only match) | `grep -rl adsbygoogle --include="*.html"` returned exactly one file. Two consequences: (a) the one ad-bearing page renders a logo, one subtitle line, three cards and a footer — about 70 visible words, a literal match for "screens without publisher content"; (b) every page that actually earns traffic (LRSM 708 impressions, Trinity ATCL 417, G5 242, G3 168) carried no ad slot at all and could never earn revenue even after approval. |
| 3 | **Rendered homepage linked to nothing** | `index.html` | The `<noscript>` fallback is full of links to all 35 repertoire pages, but the *rendered* DOM — what Googlebot sees after executing the JS — linked only to Contact and Privacy. Content pages were reachable via `sitemap.xml` alone. Plausible contributor to the recurring "crawled – currently not indexed" stalls despite correct canonical tags. |
| 4 | `GradeDirectory` component added | `index.html` | New `SYLLABUS_PAGES` constant (3 boards × all pages, with piece counts) plus a `GradeDirectory` component rendered below the entry cards on the homepage. **35 real `<a href>` links**, grouped by board, each with its piece count. Adds ~200 visible words of genuine content and gives crawlers a path to every content page. Render-tested with `react-dom/server` (not just compiled): 35 anchors emitted, all 35 targets confirmed to exist on disk. |
| 5 | Ad unit added to all 35 content pages | all `piano-repertoire_*.html` | AdSense loader in `<head>` + one responsive display unit **below the repertoire list** (placement chosen by Sohyun via AskUserQuestion). Injected after the app root in static HTML, so no JSX was touched — zero blank-page risk. The unit is **inert until `PB_AD_SLOT` is filled in**: with an empty slot the script returns early, appends nothing, and requests nothing. |
| 6 | **ABRSM inline data was stale — pages rendered fewer pieces than they claimed** | all 9 `ABRSM/*/piano-repertoire_abrsm_*.html` | Found while opening the files for the title cleanup. The inline `const DATA_ABRSM_*` arrays pre-dated **both** the Phase 9 piece recovery **and** the Phase 33 composer normalisation: pages rendered **42–47 pieces while their own meta descriptions and noscript blocks said 48**, with pre-normalisation composer names (`MOZART` not `MOZART, W.A.`). Same bug class as Phase 12/54 — authoritative `.js` updated, downstream copy not. Inline arrays and noscript blocks are now regenerated from the `.js` files; all three layers verified byte-identical. |
| 7 | ABRSM title repair — composer-name leakage | all 9 `data_abrsm_*.js` | 54 titles had the composer's own name injected by the original Phase 7 PDF extraction — e.g. `Allegro (1st movt from Sonata in E, Op. 14 No. 1) Beethoven: Beethoven: Beethoven`, `Csardas Carse`, `Rondo in F, K. 15hh Core Mozart`. Removed by matching each piece's own composer surname (both the trailing form and the mid-title `Surname:` form). 3 apparent remainders are false positives — `Jazz Preludes Wolf-temperiertes Klavier 2` really is the book title. |
| 8 | ABRSM title repair — 21 catalogue numbers restored **from the PDF, not guessed** | all 9 `data_abrsm_*.js` | Titles ending in a dangling reference (`Melody in F, Op.`, `Sonata in C, Kp.`, `Invention No. 14 in B flat, BWV`) had lost their numbers. Extracted the syllabus PDF with `pdftotext` and read each one off directly: Op. 190 No. 27, Kp. 513, BWV 785, BWV 814, BWV 826, HWV 437, K. 487, K. 7, D. 145 No. 6, S. 172, Op. 92 No. 2, Op. 36 No. 13, Op. 100 No. 15, and so on. **The PDF also corrected one of my own assumptions** — I was about to write Carse's *Progressive Pieces for Pianists*; the syllabus says *Progressive Duets for Pianists, Book 1*. |
| 9 | ABRSM title repair — publisher/page bleed | all 9 `data_abrsm_*.js` | 13 titles had absorbed the following edition line from the PDF layout (`Pp. 24–27 from Ben Crosland: Cool Beans!, Vol. 1 (Editions Musica Ferrum)` → `... Pp. Vol. 1) (Editions)`). All 13 verified against the PDF and truncated to the real title. |
| 10 | ABRSM title repair — lost accidentals | all 9 `data_abrsm_*.js` | The original extraction dropped ♭/♯ glyphs, leaving `Sonata in E-` and `Romanze in F+`. 10 flats and 1 sharp restored via a note-letter-anchored pattern (`\b[A-G]-` followed by punctuation/end only, so hyphenated words are untouched). |
| 11 | ABRSM nationality placeholders | all 9 `data_abrsm_*.js` | 135 pieces carried `nat: "International"`, which broke the nationality filter for a fifth of the ABRSM corpus. Resolved 117 from a hand-checked composer map (Chaminade → French, Moszkowski → Polish, Joplin → American, Hisaishi → Japanese, Guastavino → Argentine, P. E. Wolf → Hungarian, …). **The remaining 18 were deliberately left alone**: multi-songwriter pop credits (`ANDERSON-LOPEZ, Kristen & Robert`, `ROMAN, Capaldi, Kohn, Kelleher, Barnes &`) plus `ANON.` and `ATTRIB.`, where a single nationality would be a fabrication. |
| 12 | Verification | — | (a) All **105 inline script blocks across 48 HTML files** extracted and compiled with `@babel/core` using `runtime:'classic'` — matching the site's own in-browser Babel Standalone config — then instantiated via `new vm.Script`; JSON-LD blocks checked with `JSON.parse` rather than the JS compiler. **0 errors.** (b) Full corpus recount: **still exactly 4,500**. (c) ABRSM `.js` ↔ inline HTML ↔ noscript parity: byte-identical across all 9 grades. (d) `GradeDirectory` render-tested with `react-dom/server`. (e) Post-fix data scan: composer-in-title 54→3 (all false positives), dangling catalogue refs 21→0, publisher bleed 13→0, `nat=International` 135→18, focus arrays ≠3 → 0, invalid era → 0. |
| 13 | Committed | commit `0e9029c` | 45 files. **Not yet pushed** — Sohyun runs `git push` from her own Terminal. |
| 14 | Pre-existing uncommitted work left untouched | `diagnose.html`, `.gitignore`, `practice-challenge.html`, 2 `.docx` files | Found in the working tree at session start, from a session not logged here (same recurring pattern as Phase 58 and Phase 64). `diagnose.html` has a large uncommitted rewrite (−308/+41 lines) and there is a new untracked `practice-challenge.html`. **Deliberately not staged** — not reviewed, not mine to commit. Sohyun should decide whether to keep or discard. |
| 15 | Search Console re-index requests | — | The "crawled – not indexed" set has *changed membership*: G3 and G4 are out (G3 is now the #2 page at 6 clicks / 168 impressions). New members: **LMusA, ABRSM G5, ABRSM G8**. Requested re-indexing for ABRSM G5 and G8 — both last crawled *before* the Phase 65 canonical fix shipped (22 Jul and 11 Jun), and URL Inspection confirmed the canonical tag is live on them now. LMusA left alone: it is already earning 6 clicks, so its status is most likely report lag. |
| 16 | Documentation drift noted | `CLAUDE.md` | The live site is a **light theme**; this file still describes the Phase 35/37 dark theme (`#1a1a1a` background). Also `connect.html`, corrected in Phase 65, remains referenced in older phase sections. Not rewritten here — flagged for a future consolidation pass. |

### Traffic snapshot (2026-08-13, live from Search Console)

| Metric | 2026-08-03 | 2026-08-13 |
|---|---|---|
| Clicks (3-month) | 38 | **53** |
| Impressions (3-month) | 3.36k | **4.59k** |
| Avg CTR / position | 1.1% / 17.3 | 1.2% / 16.5 |
| Australia | 17 clicks / 662 impr | **25 clicks / 1,004 impr** |
| UK | 3 clicks / 560 impr | 5 clicks / 687 impr |
| Indexed | 35 / 40 | 35 / 40 (report last refreshed 8 Aug) |

Top pages: ABRSM LRSM (6 clicks / 708 impr), G3 (6 / 168), LMusA (6 / 97), G5 (4 / 242), G1 (3 / 87), ABRSM FRSM (3 / 81), Trinity ATCL (2 / 417). Australia is now ~47% of all clicks — the AMEB-first pivot is being confirmed by the data.

---

### Phase 68 Updates (2026-08-14 — SECURITY INCIDENT, service design doc, score-reader, practice puzzle)

#### ⚠️ 1. Malware incident — read this first

**What happened.** While researching PDF→MusicXML conversion, Claude cited `audiveris.com` as a
source without verifying it was the official project. **It is not** — the real Audiveris lives at
`github.com/Audiveris/audiveris`. `audiveris.com` is an impersonation site that served a
base64-obfuscated `curl … | zsh` command. Sohyun copied it from Claude's own Sources list and ran
it at 17:12.

**Confirmed compromise.** Identified as a **ClickFix campaign delivering an AMOS-family
infostealer** — the file-name and behaviour match Microsoft's published IoCs exactly (`curl -o
/tmp/helper` → `chmod +x` → execute). Payload found at `/private/tmp/helper`, 330,592 bytes,
timestamped 17:12. A fake macOS password dialog appeared and **the login password was entered**,
so the login keychain, browser-stored passwords, session cookies, wallets and Notes must all be
treated as exfiltrated.

**What was checked and found clean.** `/Library/LaunchAgents`, `/Library/LaunchDaemons`,
`~/Library/LaunchAgents` (Zoom/Google/Grammarly only, directory mtimes all pre-date the incident),
login items (empty), `/var/tmp`, `~/Downloads`, running processes (`ps aux` showed only Claude,
Spotify, Grammarly and Apple system helpers). `ChatGPT.app` was verified genuine via `codesign`
(Developer ID: OpenAI OpCo, LLC). **No persistence was installed** — consistent with a run-once
stealer.

**Remediation.** `helper` hashed (`daf57240a9216e6dd9ea0550c999eeded344ebf262cd457d4a2f043af044072d`)
and deleted; machine rebooted. Gmail: all devices signed out except her phone. **Remaining account
work was still outstanding when the session ended — see Known issues.**

**Rules adopted.** (a) Never paste a `curl … | zsh` / `| bash` command from any site — legitimate
software ships an installer. (b) Claude must verify that any install/download link is the official
repository before citing it.

#### 2. Service design document — `Piano-Butler-Service-Design.docx` (new)

Session opened with "이 프로젝트에 내가 뭘 코어로 반영하고 싶은지 찾고 싶어". Investigation of the
repo (including gitignored files) found the answer was already written but invisible: the voice in
`challenge-welcome-guide.md`, `outreach-messages.md` and the uncommitted `diagnose.html` rewrite is
one consistent character — *notices you, never grades you, lowers the bar, has taste*. **Piano
Butler is a voice; the tools are what it carries.** 7-page doc covers: the value ("a butler who
remembers you"), nine design rules drawn from Sohyun's own writing (R8/R9 were taken from comments
inside `butler-engine.js`), the 부담 question resolved by separating arrival from expectation, one
engine / four profiles (verified: `butler-engine.js` is `{grade, examDate, coverage, excluded}`,
67/67 tests pass), the four system layers, and a staged arrival plan.

#### 3. `score-reader.html` (new) — MusicXML information layer

Reads a MusicXML file with plain `DOMParser` (no notation rendered, so it stays clear of
reproduction) and reports key, time signature, note names, rhythm, dynamics, articulations,
ornaments and range — per bar and as six pivoted **study sheets** (rhythm / note names / intervals
/ dynamics / articulation / signs and words), each printable. 79-term dictionary written in the
butler's voice. Auto-detects OMR-produced files by reading `<software>` and flags everything as a
draft.

Two real bugs found by cross-checking against `music21`:
- Key reported as **E major** for a piece in **C♯ minor** — the file gives a signature but no
  `<mode>`, and the code silently assumed major. Now shows both with a "worth checking" note.
- **73 bars counted where music21 counts 75** — measure number `0` appears three times (pickup
  bars) and keying by printed number merged distinct bars. Now keyed by position.
- Rhythm counts differed by 6 from music21; investigation showed **the parser was right** —
  music21 absorbs padding rests in incomplete bars. Rests are now labelled separately.

#### 4. `puzzle.html` (new) — practice puzzle, rebuilt three times

Evolved as the real requirement surfaced. Final form: **photograph the score → drag a box round the
bars → mark it up → attach the demo clip → send both to the student.**

| Round | Source | Why it changed |
|---|---|---|
| 1 | MusicXML + Verovio | Exact bar numbers, but Sohyun has PDFs, not MusicXML |
| 2 | PDF via PDF.js | Realised the viewer never needs to *understand* the notes — only crop a picture. No OMR, no server |
| 3 | **Photo via camera** | "레슨 때마다 신속하게해야하니까" — opening a PDF mid-lesson is too slow. Photo is now the primary entry; PDF remains for home prep |

Features: freehand annotation (pencil / red / highlighter, undo, clear) stored in crop-relative
coordinates; a one-line note; **seams** — the join between two pieces is its own practisable item,
and two pieces only count as joined once the seam is learned; a **practice log** (not yet / got it /
comfortable, one entry per day, "learned" derives from the *last* entry so it decays honestly);
image export that renders bars + markings + note and hands it to the phone's share sheet; and
video/audio attachment shared together with the score image.

Bugs caught in verification:
- **Verovio silently renders the entire score when a measure range is out of bounds** (requesting
  bars 76–76 of a 75-bar piece returned all 536 notes). Ranges are now clamped; verified across
  five edge cases.
- Auto-detection of staff systems was attempted and **abandoned on evidence** — gaps within a
  system (20–24 px) and between systems (20–33 px) are indistinguishable, so it would have cut
  wrongly on some scores. Manual drag is both reliable and what Sohyun originally described.

Architecture notes: clips are session-only (video is far too large for browser storage, and the
workflow is film → attach → send → done); progress is keyed to a sampled hash of the file bytes +
name; v1 saved data still loads; the layout is two columns with the page pinned on the left so
cutting never costs a scroll.

#### 5. Competitive research

`digitalScore` and `forScore` cover score cropping and annotation. `Practice Space` ($9.99/mo),
`Better Practice` and `My Music Staff` all do teacher→student assignments with video, annotated
sheet music and progress dashboards. **Tonara — the best-known player — shut down in December
2023.**

The category is crowded, but every competitor is a **platform**: teacher signs up, student signs
up, both migrate. Piano Butler's approach requires **no account from the student at all** — it
rides the WhatsApp channel that already works. Sohyun's own words explain why that matters: "애들이
그정도의 열정은 없지". The seam concept was not found in any competitor. Nothing here is a business
case yet; it is a strong case for a tool she uses herself.

#### 6. Not committed

Everything from this session is **untracked**. Also still uncommitted from earlier sessions:
`diagnose.html` (−308/+41), `practice-challenge.html`, `.gitignore`, and the two 30-day-challenge
`.docx` files. Nothing was staged or pushed — and the GitHub token should be rotated before any
push (see Known issues).

---

### Phase 69 Updates (2026-08-17 — puzzle.html: voluntary-practice game framing)

Sohyun asked for a shift in framing for `puzzle.html`: game-like, exploratory, with nothing that
forces or grades practice. Two additions, both built on the existing `pieces`/`seams`/log data —
no new storage format, no schema change.

| # | Change | Detail |
|---|--------|--------|
| 1 | `Trail` component — "the route so far" | A row of numbered circular nodes (one per cut piece), connected by short lines. Node fill reflects the *last* log entry only (grey = not yet touched, amber = got it, green = comfortable) — same honest-decay logic as `isLearned()`/`sinceText()`, not a permanent badge. The line between two nodes turns green only once that specific seam is marked done. Every node is clickable at any time — nothing is locked or sequenced, matching the "autonomy over gating" direction from the earlier brainstorm. Rendered inside the existing "Your pieces" card, above the thumbnail strip. |
| 2 | "Surprise me" suggestion card | Shown whenever 2+ pieces exist. Idle state: one line ("Not sure what to open today? No pressure either way — just a place to start.") plus a single button. Pressed: picks a piece at random — weighted toward pieces not yet marked comfortable, falling back to the full set if everything is — and shows a small preview with three equal-weight actions: **Open it** / **Show me another** / **Not today**. Declining costs nothing and is offered as a real option, not a dismiss-only "×". |
| 3 | Deliberately excluded | No streak counter, no points, no comparison between pieces or between students, no daily requirement, no red/warning state for time gaps — consistent with the project's existing progress-tracking design principle (documented earlier for the practice log) of showing gaps as neutral information rather than failure. |
| 4 | Verification | Extracted `#app-jsx`, compiled with `@babel/core` (`runtime:'classic'`, matching the page's own in-browser Babel Standalone config) + `new Function()` on the output — compiles clean. Separately traced the `Trail` state-classification and the `Surprise me` weighted-random selection logic against 4 mock pieces (comfortable / got-it / never-touched / not-yet) in a standalone Node script — confirmed: comfortable pieces are excluded from the random pool, the pool correctly falls back to the full set when everything is already comfortable, and seam-line coloring only lights up for the exact pair that was marked done. |
| 5 | Not committed | Same as the rest of this session's `puzzle.html` work — sitting in the working tree, not staged. |

---

### Phase 70 Updates (2026-09-02 — piece-card design unification + SEO step-by-step pass)

Continuation of the design-unification task started in a prior session (ABRSM style confirmed
as the base standard for all 33 grade/diploma pages), plus a full step-by-step SEO pass Sohyun
asked to work through in order.

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Piece-card redesign completed — Trinity diploma pages | `Trinity/Diploma/piano-repertoire_trinity_{atcl,ltcl,ftcl}.html` | Converted to the same unified card pattern already applied to AMEB (9) and Trinity grade pages (9) in the prior session: box-card container (`background:#fff, borderRadius:12, boxShadow`), badges-then-composer-then-title-then-focus-tags ordering, icon-only YouTube/sheet-music buttons top-right. Completes all 33 target pages (AMEB 12 + Trinity 12 + the ABRSM reference itself needing no change). Verified via Babel `transformSync` (classic JSX runtime) + `new Function()` syntax check across all 21 edited files (9 AMEB + 9 Trinity grade + 3 Trinity diploma) — 0 errors. Committed `c900b95`, pushed by Sohyun, live-verified in Chrome on G3 and Trinity Initial. |
| 2 | CTR fixes — 3 lowest-performing high-impression pages | `Trinity/Diploma/piano-repertoire_trinity_atcl.html`, `ABRSM/G4/piano-repertoire_abrsm_g4.html`, `ABRSM/G8/piano-repertoire_abrsm_g8.html` | Identified via Search Console pages breakdown: ATCL (1,065 impr / 10 clicks, 0.94% CTR), ABRSM G4 (377 impr / 5 clicks, 1.3%), ABRSM G8 (561 impr / 9 clicks, 1.6%) — all well below the site's best-performing diploma pages (LRSM 2.05% CTR). Retitled all three to lead with "Piano Repertoire List" (matching the LRSM/FRSM winning pattern) instead of "Piano Diploma Syllabus" / "Piano Pieces", and added piece counts to titles. |
| 3 | Two stale-crawl pages re-submitted for indexing | `ABRSM/G1`, `AMusA` | Confirmed via Search Console's "페이지 색인 생성" report — both "크롤링됨, 현재 색인이 생성되지 않음" (last crawled 2026-07-01 and 2026-06-19 respectively, both well over a month stale). Both showed stale/missing canonical-URL data in the last-known crawl (AMusA's crawl even showed the pre-domain-migration `vividssso-pixel.github.io` canonical, though the live file itself already has the correct `thepianobutler.com` canonical) — confirmed this is Google simply not having re-crawled since earlier fixes, not a live bug. Requested re-indexing for both via URL Inspection's live-test flow. Third not-yet-indexed page (`privacy.html`) left alone — already flagged low priority. |
| 4 | Cross-syllabus internal linking extended to ABRSM + Trinity | All 9 ABRSM grade pages (Initial–G8), all 9 Trinity grade pages (Initial–G8), 3 Trinity diploma pages (ATCL/LTCL/FTCL), 2 ABRSM diploma pages (LRSM/FRSM) — 23 files total | Extends the Phase 66 AMEB-only internal-linking work to the other two syllabuses. Each page now carries a small "Also see [related AMEB page]" pill link in its header: ABRSM/Trinity Initial→AMEB Prelim, G1–G8→AMEB G1–G8, Trinity diploma (ATCL/LTCL/FTCL)→AMEB CertP, ABRSM LRSM→AMEB AMusA, ABRSM FRSM→AMEB LMusA. Applied via targeted Python string-replacement scripts anchored on verified-identical surrounding JSX (not blind sed across assumed-uniform files — each file's header structure was grepped and confirmed byte-identical before batch editing, learning from a prior session's mistake where AMEB G5–G8 turned out to have per-file variants). Verified via the same Babel compile + `new Function()` sweep across all 23 files — 0 errors. Committed `164f753` (combined with #2 above), not yet pushed as of this log entry — Sohyun to run `git push`. |
| 5 | Hong Kong traffic investigated | Search Console, country filter = Hong Kong | 18 clicks / 699 impressions / 2.6% CTR / avg position **8.2** — notably better average position than the site-wide 14.3, meaning HK traffic is landing on pages that already rank well. Top HK queries are exclusively diploma-syllabus terms: `atcl piano syllabus 2026` (2/101), `lrsm piano syllabus` (1/65), `lrsm piano repertoire list` (1/24), `frsm piano repertoire list` (1/8) — zero AMEB or Trinity *grade*-level queries appear in the Hong Kong breakdown at all. Reading: Hong Kong is a well-known strong market for ABRSM/Trinity diploma-level piano study, and this new country entrant is being driven entirely by the same diploma pages (LRSM/FRSM/ATCL) already identified as the site's main traffic engine — not a new content gap, just the existing diploma-page strength reaching a new geography. |
| 6 | Traffic snapshot at start of session (3-month, live) | Search Console | 186 clicks / 10.3k impressions / 1.8% CTR / avg position 14.3 — up sharply from the 2026-08-17 baseline (63 clicks / 5.26k impressions). Top pages unchanged in character: ABRSM LRSM (42 clicks/2,044 impr) still dominant, followed by ABRSM FRSM (19/303), LMusA (16/371), G3 (12/441 — AMEB's best performer), Trinity ATCL (10/1,065). Australia remains #1 by clicks (67/2,488, ~36% of all clicks), UK #2 (22/1,644), Hong Kong newly #3 (18/699). Indexed pages 36/40 (up from 35/40 on 8/17). |

---

### Phase 71 Updates (2026-09-15 — stickiness brainstorm → local-first Lists rebuilt on Random Pick)

Sohyun asked for the best 5 feature ideas to make the site something people keep coming back to
(current traffic is mostly one-shot "look up the list, leave" repertoire searches). Landed on
reviving the Phase 21 local-list concept (removed from `index.html` during later homepage
rewrites) as the fastest lever, scoped first onto the existing Random Pick tool.

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Local-first Lists rebuilt from scratch | `index.html` | The Phase 21 `pb_lists_v1` localStorage list system no longer existed anywhere in `index.html` — removed at some point during the Phase 22/37/44 homepage rewrites without being carried forward. Rebuilt: `loadLists()`/`saveLists()`/`pieceKey()`/`createLocalList()`/`addPieceToList()`/`removePieceFromList()`/`deleteList()` — same no-login, browser-only design as the original (Sohyun confirmed this is fine at current traffic; Deferred Features table's "login revival ≥1,000 visitors/mo" trigger still hasn't fired). `saveLists()` dispatches a `pb_lists_changed` window event so open panels/nav stay in sync without prop-drilling. |
| 2 | `AddToListModal` + `MyListsPanel` components (new) | `index.html` | `AddToListModal`: shows existing lists with one-tap "+ Add" (dedupes by composer+title), plus an inline create-new-list field. `MyListsPanel`: slide-in right panel, list of lists → drill into a list → Listen/Score/Remove per piece, delete-list with confirm. Both styled to match the site's current light theme (not the Phase 35 dark theme these components originally shipped in — that theme is no longer live, see Phase 67 #16 documentation-drift note). |
| 3 | Random Pick — click-to-expand detail | `index.html`, `RandomPickModal` | Piece cards were previously flat (era badge, grade, title, composer, Listen/Score only) despite the corpus already carrying nationality, key, list/series code, and 3 focus keywords per piece. Clicking a card now toggles an inline expand (▼/▲) showing that existing metadata as inline text + focus-tag chips, without navigating away from the modal — chosen over "click → go to the grade page" specifically to keep the Random Pick flow uninterrupted. |
| 4 | Random Pick — "+ List" button | `index.html`, `RandomPickModal` | Added next to Listen/Score. Opens `AddToListModal` for that piece. Fixed one event-bubbling bug during build: `AddToListModal`'s own backdrop-click-to-close was bubbling up through the React tree to `RandomPickModal`'s backdrop handler too, closing the whole Random Pick modal underneath it — fixed with `e.stopPropagation()` on `AddToListModal`'s outer click handler. |
| 5 | "📋 My Lists" nav button | `index.html`, `App` | Added to the header, right-aligned. Only renders once `hasLists` is true (checked on mount + kept live via the `pb_lists_changed` listener) — avoids showing an empty-state button to every first-time visitor. |
| 6 | Verification | — | All 4 inline `<script>` blocks (JS + JSX + the one JSON-LD block) in `index.html` extracted and compiled with `@babel/core transformSync`, `runtime:'classic'` (matching the page's actual `Babel.transform(..., {presets:['react']})` in-browser call) + `new Function()` on the output — 0 errors. Separately traced the list helpers in an isolated Node script with a stubbed `localStorage`/`window`: confirmed dedup-on-re-add, remove, empty-name→"Untitled list" fallback, and delete all behave correctly. Not yet live-tested in a real browser this session — flag for Sohyun to spot-check before treating this as done, per this project's standing "a built tool isn't a working tool until opened in a real browser" rule. |
| 7 | Committed, not pushed | commit pending | Only `index.html` and this `CLAUDE.md` entry staged — several other files were already modified/untracked in the working tree at session start (`admin-counts.html`, `admin-search.html`, `.gitignore`, `.github/workflows/supabase-keepalive.yml`, plus untracked `puzzle.html`, `score-reader.html`, `practice-challenge.html`, `sightreading-generator/`, and Word docs) and were deliberately left unstaged — not reviewed this session, not mine to commit, same policy as Phase 67 #14. Sohyun runs `git push` from her own Terminal as always. |

---

### Phase 72 Updates (2026-09-15 — director-mode session: git audit, live spot-checks, confirm() bug fix, AdSense/Search Console refresh)

First session run under the new "Piano Butler Director" operating skill (Sohyun: she decides,
Claude runs the session). Opened with a full `git status` / `git log` audit rather than assuming
CLAUDE.md's own phase log was current — it wasn't.

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Documentation-drift found: 3 undocumented, already-pushed feature sessions | — | `git log` showed 8 commits after Phase 71's own commit that CLAUDE.md never logged: Google Analytics 4 added site-wide (`617818e`), a full **Sight-Reading Generator** built and deployed (`9f7dd95`/`8cfee38`/`8181462` — a separate Node/Express + LilyPond/FluidSynth/ffmpeg service on Render, `sightreading-generator/`, linked from the homepage as a 4th entry card), and two same-day Render reliability fixes (`eaabcde`/`04806cc` — LilyPond version pin + longer compile timeout for Render's free-tier CPU). All were already pushed (`git status` showed local == `origin/main`, no push needed) but never reached this file's phase log. |
| 2 | Live-verified: Phase 71's Random Pick + Lists work | `thepianobutler.com` (live) | Phase 71 was logged as "not yet live-tested" — now confirmed working end to end via Claude in Chrome: Random Pick modal opens, "Shuffle again" generates 5 era-diverse picks, click-to-expand shows nationality/list/series/focus chips correctly, "+ List" opens `AddToListModal`, created a list, piece added, "📋 My Lists" nav button appeared correctly (only after a list exists), and `MyListsPanel` correctly showed the new list. Zero console errors throughout. |
| 3 | Live-verified: Sight-Reading Generator (external Render service) | `sightreading-generator` (piano-butler-sightreading.onrender.com) | Not previously spot-checked live. Clicked Generate for Preliminary: took roughly 40–50 seconds (Render free-tier cold start + LilyPond compile — matches the same-day timeout-fix commits), then produced a correct notation image (G major, 4/4, 4 bars, one hand), working audio playback, a real `Download PDF` link, and `Share`/`Regenerate` buttons. Zero console errors. **The long silent wait with no progress indicator or "this can take up to a minute" copy is a real UX risk** given this project's history of users (and Sohyun) assuming a quiet screen means something is broken — see Decisions Needed. |
| 4 | **Bug found and fixed: native `confirm()` dialog in `MyListsPanel`** | `index.html` | Clicking "Delete" on a list in the My Lists panel called `window.confirm(...)`, which froze the Chrome-automation session for several tool calls (browser-native dialogs block the page entirely) — the exact failure mode this project's own browser-automation guidance warns about, and a UX pattern the project moved away from years ago elsewhere (Phase 6 replaced `confirm()` popups in `teacher-dashboard.html` with proper in-page modals). Replaced with an inline "Delete? [Delete] [Cancel]" affordance using a new `confirmDeleteId` state — no native dialog, consistent with the rest of the site. Verified via `@babel/core` `transformSync` (`runtime:'classic'`, matching the page's own in-browser Babel Standalone call) + `new Function()` on the compiled output — 0 errors. **Not yet live-tested** — the fix is committed but not pushed, so it isn't on the live site yet; needs a live click-through after Sohyun pushes, per this project's own "not a working tool until opened in a real browser" rule. |
| 5 | `AGENTS.md` found — an undocumented, drifting mirror of this file | `AGENTS.md` (untracked, new) | A near-complete copy of `CLAUDE.md` (2,366 vs 2,416 lines, 138 diff lines) with `CLAUDE.md`→`AGENTS.md` and one `Claude API`→`Codex API` substitution — the naming convention a different AI coding tool (OpenAI Codex, or similar) reads instead of `CLAUDE.md`. Nobody has kept it in sync since whenever it was created; it's several phases stale. Not committed — this is a real decision, not something to act on unilaterally (see Decisions Needed). |
| 6 | Admin password-gate changes reviewed and committed | `admin-counts.html`, `admin-search.html` | Found sitting uncommitted since 2026-09-14: both admin pages had a client-side password prompt (`sessionStorage` + a hardcoded password) added/restored — `admin-search.html`'s previous gate pointed at `login.html`, which no longer exists (deleted in the Phase 54 cleanup), so the page had been completely unreachable by anyone, Sohyun included, until this fix. Reviewed the diff line by line — it's a straightforward soft-protection restore, already labeled in its own code comment as "not true security" (client-side JS is always viewable via View Source regardless of password, so this only deters casual/search-engine access, which is exactly what `noindex` + this gate are meant to do together). Committed as-is. |
| 7 | Search Console — real numbers pulled live (not from a stale export) | Google Search Console, logged in as vividssso@gmail.com | 3-month (Jun 13 – Sep 12): **319 clicks / 15.2k impressions**, avg CTR **2.1%**, avg position **12.4** — a further jump from Phase 70's 186 clicks/10.3k impressions two weeks ago, and CTR/position both improved too (was 1.8%/14.3). **Indexed pages now 38/40** (was 36/40 on 9/2), only 2 not-indexed. Top queries unchanged in character — all diploma-syllabus long-tail (`lrsm piano repertoire list` 17/575, `frsm piano repertoire list` 13/148, `atcl piano syllabus 2026` 3/203). |
| 8 | **AdSense — the "주의 필요" (needs attention) flag is gone** | Google AdSense → Sites, logged in live | The site's 승인 상태 (approval status) column now reads **준비 중** ("in progress/preparing") with an empty 상태 세부정보 (status detail) field — not the 주의 필요 / "low-value content" flag that had stood since 2026-06-21 and was last confirmed present (and stale) as recently as Phase 67 (2026-08-13). Last-updated timestamp on this row: **2026-09-09**. Ads.txt status still reads 승인됨 (approved, unchanged). This reads as real forward movement — the site has moved out of the flagged state into an active/pending review state — but "준비 중" is not itself an approval; see Decisions Needed for the recommended next step. |
| 9 | Verification | — | `node --check`-equivalent compile pass on `index.html`'s single inline script block (`@babel/core transformSync`, `runtime:'classic'`) — 0 errors, confirmed before committing. `git log`/`git status` re-checked after all commits this session to confirm nothing was left in a half-committed state. |
| 10 | Committed, not pushed | commits pending | `index.html` (confirm() fix), `admin-counts.html`, `admin-search.html`, `.gitignore`, `.github/workflows/supabase-keepalive.yml` (daily Supabase keep-alive, already reviewed and explained in its own commit message from 2026-08-17), and this `CLAUDE.md` entry. `AGENTS.md`, the two 30-Day-Challenge `.docx` files, `Piano-Butler-Service-Design.docx`, `Satie-Gnossienne1-Decode-Worksheet.docx`, `practice-challenge.html`, `puzzle.html`, `score-reader.html`, and `sample-score-chopin-mazurka.musicxml` were deliberately left unstaged — not reviewed this session, not mine to commit, same standing policy as Phase 67 #14 / Phase 71 #7. Sohyun runs `git push` from her own Terminal as always. |

---

### Phase 73 Updates (2026-09-15 — same-day: Sight-Reading Generator cold-start fix, folder cleanup)

Same director session, continued. Sohyun reported live: opening the Sight-Reading Generator
sometimes shows Render's own branded "waking up" loading page (not Piano Butler's) before the
tool works at all, and the whole thing takes too long — asked whether to fix it or pull it down
and re-launch later.

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Diagnosed live | `sightreading-generator` (Render) | Reproduced it directly: navigating cold shows Render's own ASCII-art "APPLICATION LOADING" splash for ~10-15s (this is Render's free-tier edge, not Piano Butler's code — nothing in this repo can suppress it), then the real app loads and a Generate click takes another ~30-40s (LilyPond + FluidSynth compiling on a slow free-tier CPU — genuine work, not a hang). Ran it twice end to end: both times it completed successfully with a correct excerpt, audio, and PDF — **the feature itself is not broken**, it's Render's free-tier cold-start behavior plus real compile time, which reads as "failing" to a first-time visitor because a stranger's branding flashes on what should be Piano Butler's site. |
| 2 | Recommendation given (not a pull-it-down situation) | — | Told Sohyun: this doesn't need taking the feature down and relaunching — that costs a redeploy cycle for a problem with a known, free, standard fix. Recommended a keep-alive ping (same pattern already used for Supabase in this repo) instead. |
| 3 | Render Keep-Alive GitHub Action added | `.github/workflows/render-keepalive.yml` (new) | Pings the Sight-Reading Generator every 10 minutes — comfortably inside Render's free-tier ~15-minute sleep window — so most real visitors land on an already-warm instance instead of triggering a cold start. Modeled directly on the existing `supabase-keepalive.yml`. Logs a GitHub Actions warning if the ping ever returns a non-2xx/3xx status. **Will not run until this is pushed** (GitHub Actions only executes from the pushed repo, not local commits). |
| 4 | "This can take up to a minute" loading copy | `sightreading-generator/client/public/app.js`, `.../style.css` | The spinner shown during generation now includes a small muted note under "Engraving your excerpt…" so a genuinely-working-but-slow generation doesn't read as frozen. This does not fix the Render splash screen itself (that appears before the app's own JS even runs) — only softens the compile-time wait once the app is up. Verified with `node --check` (plain JS, not JSX). **Not yet live** — this is a separate Render service with its own deploy; it picks up the change whenever Sohyun pushes and Render redeploys. |
| 5 | Honest limits of this fix | — | The keep-alive does not *guarantee* zero cold starts — a scheduled Render redeploy, a burst of traffic, or GitHub Actions running a few minutes late can still let the instance sleep. If Sohyun keeps seeing the Render splash screen after this is live for a few days, the next real fix is Render's paid Starter plan (~$7/mo) which removes sleep entirely — a cost decision for her, not something to switch to unilaterally. |
| 6 | Folder cleanup (from earlier in this same session) | filesystem only, no git impact | Per Sohyun's request, moved loose, never-git-tracked personal files at the project root into `_workspace/` (`docs/`, `lesson-tools/`, `challenge-idea/` subfolders) — 4 `.docx` files, a build-tracker `.xlsx`, a sample `.musicxml`, `puzzle.html`, `score-reader.html`, `practice-challenge.html`, `challenge-welcome-guide.md`, `outreach-messages.md`. Confirmed via `git status` that none of these were ever tracked, so this has zero effect on GitHub or the live site. `AGENTS.md` (an untracked, stale Codex-oriented mirror of this file) was deleted outright per Sohyun's instruction, after confirming no file referenced it. `butler.html` and its companion files were deliberately left at the root, pending Sohyun's decision on Pending Work item — recommended to her as "keep private, don't build it out further" but not yet confirmed. |
| 7 | Verification | — | `node --check` on `app.js` (clean). `git status` re-confirmed after each change to keep the "what's tracked vs. not" picture accurate before committing. |
| 8 | Committed, not pushed | commit pending | `.github/workflows/render-keepalive.yml`, `sightreading-generator/client/public/app.js`, `sightreading-generator/client/public/style.css`. Sohyun pushes from her own Terminal as always — both the keep-alive Action and the loading-copy fix are inert until then. |

### Phase 74 Updates (2026-09-15 — same-day: Sight-Reading Generator JSON-parse error diagnosed + fixed, butler.html decision closed)

Same director session, continued again. Sohyun then sent two screenshots of a *different* error
from the cold-start splash already addressed in Phase 73: a red banner reading "Couldn't generate
an excerpt: Unexpected token '<', \"<!DOCTYPE \"... is not valid JSON".

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Diagnosed live | `sightreading-generator/client/public/app.js`, Render | `generate()` did `if (!res.ok) throw new Error((await res.json()).error ...)` — when Render's proxy answers a request with its own HTML error page (typically right at the edge of a cold start, before/while the Node process finishes binding the port) instead of the app's JSON, `res.json()` itself throws a generic "Unexpected token '<'... is not valid JSON" parse error, which was then shown to the user verbatim. Reproduced the real request live in Chrome: a cold `POST /api/generate-sightreading` took ~50s and *did* succeed once fully warm — confirming the failure window is specifically the boot/race moment, not the generation logic itself. |
| 2 | Retry + friendly-message fix | `sightreading-generator/client/public/app.js` | Added `isGatewayStyleError()` to recognize this exact failure signature, and `requestExcerpt()` as a reusable single-attempt helper. `generate()` now retries once automatically after a 4s pause when it hits this signature, and only falls back to a friendly "the generator is still waking up, please wait a few seconds and click Generate again" message if the retry also fails — the raw JS parse error is never shown to a real user anymore. A genuine generation failure (e.g. a real 500 with a JSON error body) still surfaces its real message unchanged. |
| 3 | Verification | — | `node --check app.js` passes. Live-reproduced a cold generate end-to-end in Chrome (network tab confirmed `pending` → `200` over ~50s) to confirm the underlying request path still works correctly under the new code path. Not yet feasible to force the exact HTML-error-body race on demand (it depends on Render's boot timing), so the retry path itself is verified by code review + syntax check rather than a live repro of the failure — flagged here rather than overstated as fully live-tested. |
| 4 | Committed | `37c1aa5` | "Phase 74: retry + friendly message for sight-reading gateway-style JSON parse errors". Not yet pushed — Sohyun pushes from her own Terminal as always. |
| 5 | `butler.html` decision closed | none (decision only) | Sohyun confirmed (2026-09-15): keep `butler.html` private for now, per Claude's recommendation — not built out into a public feature. Pending Work item removed; Known Issues line updated to reflect the decision instead of listing it as undecided. |

### Phase 75 Updates (2026-09-15 — same-day: sight-reading generation speed — lazy hands-view previews + LilyPond warm-up)

Sohyun asked directly: "초견 뜨는 시간을 줄일 방법은 없어?" (is there a way to cut the sight-reading
generation time?) — a step further than Phase 73/74's cold-start mitigations, about the actual
per-generate compute time.

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Diagnosed the real time sink | `server/lilypondCompiler.js`, `server/server.js` | Read the actual compile pipeline. Two real, code-fixable causes found (on top of the already-addressed cold-start/sleep issue): (a) every single generate call pre-rendered BOTH hands-view preview images (treble-only, bass-only) in addition to the 'both hands' view actually shown first — 3x the LilyPond+pdftoppm+compose work per click, even though most visitors never touch that toggle; (b) LilyPond builds its font cache on its very first invocation in a fresh container, which the code's own existing comment already documented as able to take 20-30s+ alone on Render's free 0.1-CPU instance — the render-keepalive.yml Action (Phase 73) stops an already-warm instance from sleeping, but does nothing for the moment right after a fresh deploy/restart. |
| 2 | Made hands-view previews lazy | `server/lilypondCompiler.js` (new `renderLazyView`), `server/server.js` (new `POST /api/sightreading-view` route), `client/public/app.js` | `compileExcerpt` now only builds the 'both hands' preview up front. Right-hand/left-hand previews render on demand the first time a visitor actually clicks that toggle (client already has the treble/bass `.ly` source text from the original response, so no new server-side state is needed), and are cached client-side per excerpt so toggling back and forth doesn't re-request. Cuts real per-generate compute for the large majority of visitors who never touch the toggle. |
| 3 | LilyPond font-cache warm-up at boot | `server/lilypondCompiler.js` (new `warmUp`), `server/server.js` | Fire-and-forget call right after `app.listen()` that primes the font cache once when the server boots, so it isn't the very first real visitor who pays that 20-30s+ cost after every fresh deploy/restart. Free, no cost decision needed. |
| 4 | Verification | — | `node --check` passes on all three touched files. **Could not run this end-to-end locally** — this dev machine has ffmpeg/pdftoppm/python3 but no `lilypond`/`fluidsynth` binaries (only present in the Docker image Render actually builds), consistent with this project's standing note that this app is only really testable on the deployed Render instance. Needs a live spot-check (both the lazy toggle and a rough before/after timing sense) once Sohyun pushes and Render redeploys. |
| 5 | Committed, not pushed | `9180f3d` | "Phase 75: speed up sight-reading generation — lazy hands-view previews + LilyPond warm-up". |
| 6 | Honest ceiling on this fix | — | These are real, meaningful, zero-cost wins, but the underlying LilyPond/FluidSynth compile work on a 0.1-CPU free instance is still inherently slow — a first-generate-after-idle can still take tens of seconds. The one remaining lever that would make a large, guaranteed difference is Render's paid plan (Starter, ~$7/mo: real CPU allocation, no sleep at all) — a cost decision left to Sohyun, not something to switch to unilaterally. |

### Phase 76 Updates (2026-09-15 — same-day: Piano Butler-branded loading page replaces Render's own wake-up splash)

Sohyun sent a screenshot: the raw Render "WELCOME TO RENDER" wake-up splash was still showing to
visitors, despite the Phase 73 keep-alive Action.

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Diagnosed why keep-alive wasn't enough | GitHub Actions API | Checked `render-keepalive.yml`'s actual run history via the GitHub API: it IS active and both runs so far succeeded, but only fired twice — ~3 hours apart, then 52 minutes apart — nowhere near the configured `*/10 * * * *`. This is a known GitHub Actions limitation: sub-hourly cron schedules are frequently delayed or coalesced on lower-traffic repos. Not something fixable by editing the workflow file further -- the keep-alive helps but can't be trusted alone to prevent every cold start. |
| 2 | Piano Butler-branded loading page | `sight-reading-loading.html` (new, noindex) | index.html's "Practice sight-reading" card now opens this page instead of the raw Render URL directly. It shows Piano Butler's own spinner/copy and polls a new health route every ~1.8s in the background, only redirecting to the real generator once that app (not Render's placeholder) actually answers. A warm instance is barely noticeable; a cold one now shows Piano Butler's own wait instead of a stranger's splash. Falls back to a manual "open it directly" link after 90s rather than spinning forever. |
| 3 | New CORS-open health route | `sightreading-generator/server/server.js` | `GET /api/health` returns `{ ok: true, ts }` with `Access-Control-Allow-Origin: *` -- needed since the loading page lives on thepianobutler.com (GitHub Pages) polling a different origin (onrender.com). Render's own splash answers every route while the app is still booting but never returns this exact JSON shape, which is what lets the loading page tell the two apart. No sensitive data on this route, so open CORS is fine. |
| 4 | `index.html` link updated | `index.html` | `onClick` now opens `sight-reading-loading.html` instead of `https://piano-butler-sightreading.onrender.com` directly. |
| 5 | Verification | — | `node --check` on `server.js`; HTML parses cleanly; Babel-compiled `index.html`'s inline script block per this project's standard method — all pass. **Not yet live-tested** — the new `/api/health` route doesn't exist on Render until this is pushed and redeployed. |
| 6 | Committed, not pushed | `2324278` | "Phase 76: Piano Butler-branded loading page masks Render's own wake-up splash". |
| 7 | **Live-verified after push** | — | Pushed by Sohyun (`f3d6578`); GitHub Pages redeployed and Render redeployed successfully. Confirmed live: `/api/health` returns real JSON; `sight-reading-loading.html` correctly detected the already-warm instance and redirected straight through in ~2s; generated a fresh Grade 3 excerpt; clicked "Right hand" and confirmed the lazy `/api/sightreading-view` call fires only on that click and renders correctly. Everything in Phase 75/76 works as designed. |

### Phase 77 Updates (2026-09-15 — same-day: sight-reading generation, round 3 — header-image caching + audio moved off the critical path)

Sohyun again: "최대한 시간 줄이는 방법 찾아줘 아직도 너무 오래걸리는데" (find the biggest way to cut the
time, it's still too slow) — went back into the compile pipeline for anything left after Phase 75.

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Header-image caching | `sightreading-generator/server/lilypondCompiler.js` | The title/subtitle header image was re-rendered via its own LilyPond process on every single generate, even though the title text never changes and the subtitle is one of a small fixed set of "<grade> — <realm>" combinations. Added an in-memory cache (PNG bytes, keyed by title+subtitle) inside the running server process -- after the first request for a given grade/realm combo, every later one skips that LilyPond call entirely (each invocation carries its own ~1-2s fixed startup cost, documented in this file's existing timeout comment, on top of real render time). Cache resets on redeploy/restart, which is fine -- it just warms back up on the first few requests. |
| 2 | Audio moved off the critical path | `sightreading-generator/server/lilypondCompiler.js`, `server.js`, `client/public/app.js` | fluidsynth reloads the ENTIRE General MIDI soundfont from disk into memory on every single invocation -- there's no way to keep it warm across separate process launches -- which alone can cost real seconds on Render's slow free-tier disk/CPU. That was previously part of what a visitor waited through before ever seeing their notation. `compileExcerpt` now returns as soon as the PDF/PNG are ready; audio renders in the background afterward. The response carries `audioPending` + the mp3's eventual URL; a new `pollForAudio()` in `app.js` checks every 1.5s (scoped to the exact excerpt via a `data-mp3-url` guard so a stale poll from a since-regenerated excerpt can never attach the wrong audio) and swaps in the real player once it's ready. Visible notation now shows up without waiting on audio at all. |
| 3 | Verification | — | `node --check` passes on all three touched files. **Not live-tested** — same standing limitation as Phase 75/76 (no lilypond/fluidsynth on this dev machine). Needs a live check after push + redeploy: confirm the header cache never bleeds stale text across different grades, and that the audio player actually appears a moment after the notation via polling. |
| 4 | Committed, not pushed | `470e554` | "Phase 77: two more speed wins — cache rendered header images, defer audio off the critical path". |
| 6 | **Live-verified after push** | — | Pushed by Sohyun (`93c7860`); Render redeployed. Generated a fresh Grade 3 excerpt on the newly-redeployed (cold, empty header-cache) instance — notation appeared with the audio player slot showing "Rendering audio…", then a few `HEAD` polls (a couple of transient 503s right after redeploy, expected) before the real player swapped in and played correctly (confirmed audio actually plays, 0:13 total). Header cache and deferred-audio polling both work as designed. |
| 5 | Honest ceiling, restated | — | These three rounds (Phase 75/76/77) remove essentially every avoidable overhead this code controls. What's left — the actual LilyPond engraving + font rendering of real music — is genuine work on a CPU-starved 0.1-vCPU free instance, and will still take several real seconds on a cold or heavily-loaded piece. The only remaining lever that changes that floor is Render's paid Starter plan (~$7/mo, real CPU, no sleep) — already tracked in Pending Work as Sohyun's cost decision, not something to switch to unilaterally. |

### Phase 78 Updates (2026-09-15 — same-day: sight-reading generation, round 4 — the full-page PDF compile also moved off the critical path)

Sohyun asked once more, explicitly for a free option this time ("무료로 시간 단축하는 방법을 찾아줘").
Found the biggest remaining item.

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Found the real remaining bottleneck | `sightreading-generator/server/lilypondCompiler.js` | `compileExcerpt` raced the full-page (uncropped) PDF compile against the cropped preview build via `Promise.all` -- "parallel" in name, but the response still waited for BOTH, so every single generate was gated on TWO separate LilyPond compiles of the same music. The preview build never actually reads from the full-page PDF at all (it compiles straight from `lySource` itself, independently, at its own crop) -- the full compile is only needed for the Download PDF button and as the .midi source for audio, neither of which a visitor needs before they can see and start reading their excerpt. |
| 2 | Full-page PDF compile deferred | `lilypondCompiler.js`, `server.js`, `client/public/app.js` | `compileExcerpt` now returns as soon as the ONE compile the visible preview needs is done; the full-page compile runs in the background afterward, and audio (already backgrounded in Phase 77) now runs after THAT finishes instead of racing it. Response carries a new `pdfPending` alongside `audioPending`. `app.js`'s new `pollForPdf` mirrors `pollForAudio`: shows "Preparing PDF…" and disables Share until the real file exists, then swaps in the working Download link and re-enables Share automatically. |
| 3 | Net effect | — | The response now depends on a single LilyPond invocation (on top of the header, which is cached as of Phase 77) instead of two. Combined with Phase 75-77, this removes essentially every avoidable compile/overhead this code controls -- what's left is genuine LilyPond engraving work on a 0.1-vCPU free instance. |
| 4 | Verification | — | `node --check` passes on all three touched files. **Not live-tested** — same standing limitation as Phase 75-77 (no lilypond/fluidsynth on this dev machine). Needs a live check after push + redeploy: confirm Download PDF and Share correctly wait for `pdfPending` to clear (rather than 404ing) and then work normally. |
| 5 | Committed, not pushed | `585a8cf` | "Phase 78: cut the critical path to a single LilyPond compile — defer the full-page PDF too". |
| 6 | **Live-verified after push** | — | Pushed by Sohyun (`14dfe02`); Render redeployed. Generated a fresh Preliminary excerpt on the newly-redeployed instance -- notation appeared, and by the time of the follow-up screenshot both "Download PDF" (a real working link, confirmed via element inspection) and the audio player had already resolved from their pending placeholders. Deferred PDF + audio both work correctly end to end. |

### Phase 79 Updates (2026-09-15 — found and fixed why the "optimized" generator still failed live)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Root-caused a live "Couldn't generate an excerpt: generation failed" failure Sohyun asked about ("꽤 오래걸리지 않아?") | `sightreading-generator/client/public/app.js` | A direct debug `fetch()` to the live endpoint took **75 seconds** and still succeeded (200 OK) -- confirming the request itself is still genuinely slow even after Phases 75-78's optimizations, and that on a slower attempt Render's own proxy can time out mid-compile and hand back a non-JSON (HTML) error body. |
| 2 | Fixed a real regression: the gateway-timeout retry added in Phase 74 had been silently defeated | `sightreading-generator/client/public/app.js` (`requestExcerpt`, `isGatewayStyleError`) | `requestExcerpt()`'s `!res.ok` branch was swallowing the JSON-parse failure from a non-JSON error body inside its own `try/catch` and replacing it with the generic string `"generation failed"` -- so `isGatewayStyleError()` in `generate()` never saw the `SyntaxError` it was written to detect, and the Phase 74 retry never fired. Now a non-JSON error body (or any 5xx) is tagged `err.isGatewayError = true` and correctly triggers the existing retry + friendly "still waking up" messaging instead of a dead-end error. |
| 3 | Made the retry more resilient to how slow this actually is | `sightreading-generator/client/public/app.js` (`generate`) | One retry (4s pause) wasn't always enough given 75s+ real compile times observed live. Now retries up to twice more (4s, then 8s pause) before giving up, and the final failure message was reworded to reflect that this is a "taking unusually long" wake-up, not a broken feature. |
| 4 | Honest status: generation time itself has NOT been reduced to consistently under Render free-tier's proxy timeout window | -- | Phases 75-78 removed genuinely redundant work (eager unused previews, blocking audio, blocking full-PDF compile, repeat header renders) and did measurably cut the *critical-path* LilyPond work from 2 compiles to 1. But on Render's free 0.1 vCPU tier, a cold or unlucky compile can still take 40-75+ seconds end to end, which is beyond what client-side or LilyPond-side optimization alone can fix for free. The only further lever for consistently-fast generation is a paid Render plan (more CPU) -- a cost decision for Sohyun, already tracked in Pending Work. |

**Live-verified after push** (2026-09-16): Sohyun pushed both commits (`4e07b74`, `48bcd69`); Render redeployed. Confirmed the deployed `/app.js` actually contains the fix (`isGatewayError` present, old `serverMsg = 'generation failed'` swallow-bug gone, `RETRY_DELAYS_MS` present). Clicked Generate fresh on a Preliminary excerpt: took about 40 seconds and succeeded outright this time -- notation, PDF link, and audio player all rendered ready with no placeholder/pending state. Did not happen to hit a gateway-timeout on this run to observe the retry UI itself, but the underlying bug (retry being silently defeated) is fixed and deployed either way.

### Phase 80 Updates (2026-09-16 — background-refilled excerpt pool, "instant" Generate)

Sohyun asked "다른 방법은?" (other ways to cut the wait, for free) after Phase 79's honest answer
that the remaining wait is a genuine LilyPond-compile cost on Render's free 0.1 vCPU, not
something client-side alone could fix further. Two ideas were proposed; she approved both,
starting with the more reliable free keep-alive (see Decisions needed) and this pool.

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Added a small background-refilled "warm pool" of pre-compiled excerpts | `sightreading-generator/server/excerptPool.js` (new) | The generator page always requests the exact same fixed shape (`realm: 'reading'`, `hands: 'auto'`, no `feel`) — only `grade` varies (confirmed in `client/public/app.js`: `REALM` is hardcoded and the old Style/"feel" picker was disabled). So instead of compiling fresh live on every click, keep up to 2 already-compiled excerpts ready per grade (9 grades), topped up one at a time in the background whenever no real visitor request is in flight, and hand one out instantly on a hit. A miss (pool empty — e.g. right after boot, or a burst of clicks) falls straight through to the same live-compile path as before; nothing about the non-pooled path changed. |
| 2 | Wired the pool into the generate route | `sightreading-generator/server/server.js` | `POST /api/generate-sightreading` now checks `excerptPool.isPoolableRequest(...)` first and serves `excerptPool.takeFromPool(grade)` when available; a custom `feel`/non-default `hands`/`realm` (not currently reachable from this page's UI, but supported by the API) always bypasses the pool. Added `markLiveRequestStart/End()` around the live-compile path so the background refill loop can detect real traffic and step aside rather than competing with it for the one weak CPU. `excerptPool.refillLoop(OUTPUT_DIR)` is kicked off fire-and-forget at the bottom of `app.listen(...)`, alongside the existing `warmUp()`. |
| 3 | Scope/tradeoff, stated plainly | -- | This does NOT make any single compile faster — it moves the wait to idle time between visitors instead of onto the visitor's own click. On a freshly booted (or freshly woken) instance, the pool starts empty and fills gradually (roughly one excerpt every ~10-40s+ per grade), so the very first visitors after a cold start still get the old live-compile wait; only once the pool has filled do subsequent Generate clicks become near-instant. Pairs directly with the Decisions-needed item below (a more reliable free keep-alive) — the more consistently the instance stays awake, the more consistently the pool stays full. |

**Live-verified after push** (2026-09-16): Sohyun pushed (`8541171`, `eeea8ea`, `998d552`) and separately
finished setting up a real free keep-alive (UptimeRobot, 5-min interval, confirmed Up/100%) for the
Decisions-needed item below. Tested Generate live right after the redeploy: it took over 50s and
actually surfaced Phase 79's new friendly retry UI ("Still warming up — trying again…") and, after
exhausting retries, its friendly failure message — confirming Phase 79's fix works exactly as
designed. BUT this also caught a real, unintended regression from Phase 80 itself: the excerpt
pool's background refill loop was running fully concurrently with this live request (both are
separate LilyPond child processes competing for the same 0.1 vCPU), making the wait *worse* than
before the pool existed, not better. Root cause: nothing serialized "background refill compile" and
"live request compile" — excerptPool's own `liveRequestsInFlight` counter only stopped a *new*
background compile from *starting* once a live request was already in flight; it did nothing about
a background compile already underway when the live request arrived, or about other overlaps (e.g.
warmUp() racing the first refill).

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 4 | Added a fairness gate so only one compile runs at a time, live-priority | `sightreading-generator/server/compileGate.js` (new), `server.js`, `excerptPool.js` | `runGated(task, priority)` queues every LilyPond-driving unit of work (a live generate, a lazy hands-view render, a background pool refill, boot-time warm-up) through a single-slot queue; `'live'` priority jumps ahead of any queued `'background'` work. Stated limit: it cannot preempt a job that has *already started* — a click landing the instant a background compile begins still waits for it — and it doesn't reach into compileExcerpt's own fire-and-forget follow-up work (deferred PDF/audio from Phases 77/78), which can still overlap with a next gated job. It does stop the specific compounding case this live test caught: two full preview compiles actively racing for the CPU at once. |

**Live-verified (gate fix)**: Sohyun pushed (`9d76a89`, `24f73e9`); confirmed redeployed and
healthy (health check OK, `app.js` fix present). While checking on it, Sohyun forwarded a Render
"server failure — Exited with status 1" email, which turned out to be a real, serious bug, not a
benign redeploy artifact — see #5.

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 5 | **Critical fix**: a failed background PDF compile could crash the whole server, not just one request | `sightreading-generator/server/lilypondCompiler.js` | Sohyun forwarded Render's crash email; her screenshot of the actual Render dashboard logs showed the smoking gun: an uncaught `Error: lilypond failed: ... /app/server/output/<id>.ly` stack trace ending in the Node process re-announcing "running at http://localhost:10000" — i.e. the process died and Render auto-restarted it. Root cause: `compileExcerpt`'s `fullCompilePromise` (the deferred full-page PDF compile added in Phase 78) is only ever `await`ed later — in the rare fallback branch, or inside a background IIFE further down — so if it rejects before either of those await points is reached, Node sees no attached handler at the end of that microtask turn, fires `unhandledRejection`, and (Node 15+ default behavior, confirmed running Node 20.20.2 from the logs) **crashes the entire process** — taking down every visitor currently being served, not just the one excerpt whose PDF compile happened to fail. This has almost certainly existed since Phase 78 shipped, just hadn't been caught live before. Fix: attach a no-op `.catch(() => {})` to `fullCompilePromise` immediately at creation so Node marks the rejection "handled" right away; the real error handling (logging, fallback raster, etc.) is unaffected since a promise can have more than one `.then`/`.catch` consumer. Audited the rest of the file for the same pattern (`grep .then(` ) — this was the only bare, non-immediately-awaited promise in it. |

**Live-verified (crash fix)**: Sohyun pushed (`04ea904`, `0b830bc`); confirmed redeployed. Ran a
fresh Preliminary Generate end to end: notation, PDF download link, and audio all resolved
correctly with no error, and `/api/health` stayed healthy throughout with no crash/restart gap.
Did not force-trigger an actual full-page-compile failure to directly prove the crash can no
longer happen (that would mean deliberately overloading the live production service, which was
correctly blocked as a workload-interference risk when attempted) — confidence here rests on the
code-level fix being correct (the exact unhandled-rejection pattern Node crashes on), not on
having reproduced the original crash and shown it no longer occurs. Sohyun should keep an eye on
Render's email/logs for any further "Exited with status 1" alerts as normal usage continues.

### Phase 81 Updates (2026-09-17 — Sight-Reading Generator: SEO landing page)

Sohyun asked whether the Sight-Reading Generator had moved the needle on traffic. Live check
(Search Console + GA4) showed no — the tool is only reachable via a homepage click, so it can't
show up as organic search traffic, and it didn't appear in GA4's top-7 pages by views over the
last 28 days either. She asked to fix that.

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | New indexable landing page | `sight-reading.html` (new) | Plain static HTML (no React/JSX — avoids the Babel-compile risk class entirely for a page this simple), matching the site's light theme. Real crawlable content: what the tool does, the 9 AMEB grades covered, an FAQ block, and CTA buttons — targets `AMEB sight reading generator`, `free piano sight reading exercises`, `sight reading exercises by grade` and similar long-tail terms, following the same "phrase-match the query, lead with something concrete" pattern that worked for the diploma-page CTR fixes (Phase 64/70). Carries the same `<title>`/description/canonical/OG/Twitter/keywords tag set as other indexed pages, the site's GA4 tag, and the standard ad-unit snippet (same `PB_AD_SLOT`, matching the pattern used on all 35 other content pages). |
| 2 | Homepage entry card now routes through it | `index.html` | "Practice sight-reading" card's `onClick` changed from `window.open('sight-reading-loading.html', '_blank')` to `window.location.href = 'sight-reading.html'` — same-tab navigation to a real page instead of popping the loading/redirect screen directly, matching how the "Plan for an exam" card links to `timeline.html`. `sight-reading-loading.html` itself is unchanged and stays `noindex` — it's a pure redirect/wait screen with no content, correctly excluded from search; the new page's own CTA buttons link to it to continue the existing warm-up flow. |
| 3 | Added to sitemap | `sitemap.xml` | `sight-reading.html` added, priority 0.9 (matching `diagnose.html`/`recommend.html`'s tool-page priority), monthly changefreq. |
| 4 | Verification | — | `index.html`'s inline script block re-compiled via `@babel/core transformSync` (`runtime:'classic'`) + `new Function()` — 0 errors. `sight-reading.html`'s two inline `<script>` blocks (gtag init + ad-unit loader) checked with `new Function()` as plain JS — 0 errors. Confirmed the file has a matching DOCTYPE/closing tag. **Not yet live-tested** — not pushed this session, so nothing to spot-check live yet; flag for a live click-through (homepage card → `sight-reading.html` → Generate button → loading page → tool) once Sohyun pushes, per this project's standing "not a working tool until opened in a real browser" rule. |
| 5 | Committed, not pushed | `4cfff82` | "Add SEO landing page for the Sight-Reading Generator (sight-reading.html), wire homepage card + sitemap to it". Once live, will need a Search Console "request indexing" pass like every other new page has gotten (see Phase 59/60/64/70 pattern) — results won't show for at least a few days after that. |

### Phase 82 Updates (2026-09-17 — sight-reading.html CTA revert + timeline.html generic mode)

Two small follow-ups from Sohyun after Phase 81 shipped the `sight-reading.html` SEO landing page.

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Reverted the Generate CTA to skip the loading-page detour | `sight-reading.html` | Sohyun's call: the two "Generate an excerpt →" buttons now link straight to `https://piano-butler-sightreading.onrender.com/sight-reading-generator` again instead of `sight-reading-loading.html` (the Phase 76 branded health-check/wait page). `sight-reading-loading.html` itself is untouched and is now effectively orphaned from the live click path (`index.html`'s card routes through `sight-reading.html` now, per Phase 81 #2) — left in place, not deleted, since she didn't ask for that. Committed as `336edfa`. |
| 2 | New generic "performance countdown" mode, alongside the existing AMEB flow | `timeline.html` | Sohyun asked to broaden the AMEB-only exam timeline tool so it's also useful for an HSC performance or a plain school concert — without touching the AMEB-specific logic (Phase 61's Reference Integrity restriction stands: no fabricated syllabus claims for exams Sohyun hasn't sat). Implemented her preferred option: a new "What are you preparing for?" screen up front routes to either the untouched AMEB flow or a new generic flow — free-text performance label instead of a grade picker, typed piece titles instead of the CORPUS search/browse (`GenericPieceInput`, new), and the same month-by-month engine (`buildTimeline`/`MONTH_FOCUS`/`WEEKLY_TEMPLATES`/`allocatePhases` — already syllabus-agnostic, no changes needed) with a separate `READINESS_QUESTIONS_GENERIC` array so the quiz doesn't say "General Knowledge" or "this grade's scales" to a non-AMEB user. Two small shared-code fixes made along the way so the generic mode reads correctly (and improve the AMEB Diploma-grade case too, which already hit the same `tech === null` path): `technicalChecklist`'s no-data fallback no longer cites "AMEB's fixed technical-exercise list" (that line now just says to work through scales/exercises with a teacher); `foundationChecklist` now only tells the student to "skim the Technical Work Checklist below" when that section actually exists on the page (a real bug — this line unconditionally referenced a heading that isn't rendered for Diploma grades or the new generic mode). The results screen hides the AMEB-only Technical Work Checklist and sample-repertoire sections entirely for generic mode (both already conditionally rendered — no JSX changes needed there). Committed as `55816fa`. |
| 3 | Verification | — | JSX parse-checked with `@babel/parser` (jsx plugin) after every edit. Live browser verification hit a real constraint worth recording: neither Claude in Chrome (the desktop's real browser) nor the built-in Browser pane could reach a locally-run dev server for this not-yet-deployed page — Claude in Chrome resolved `localhost` to the isolated Linux VM this session's shell runs in, not the Mac Chrome is actually running on (so nothing was listening), and the built-in Browser pane explicitly doesn't support a local dev server on its surface at all. Worked around it by running the actual compiled app in a real headless Chromium *inside the cloud workspace* (Playwright, already preinstalled there) — the org's egress policy blocks the cdnjs CDN this page normally loads React/ReactDOM/Babel from, so those three files were swapped for local `npm`-installed copies for the test run only (the real file on Sohyun's machine still points at cdnjs, untouched). Full generic-mode flow driven end to end (mode pick → name → date → pieces → quiz → results): correct label substitution throughout, no AMEB-only copy leaking through, Technical Work Checklist/repertoire sections correctly absent, checklist correctly referencing the typed test piece. Full AMEB flow re-run as a regression check (grade picker, date, piece browse/search, quiz, results) — confirmed unchanged and still working. Zero unexpected console errors (only the expected 404s for AMEB data files not present in the trimmed test copy). |
| 4 | Committed, not pushed | `336edfa`, `55816fa` | Both ready for Sohyun to push from her Terminal. |

### Phase 83 Updates (2026-09-17 — homepage sight-reading card skips the landing page)

Sohyun sent screenshots showing her expectation: clicking the "Practice sight-reading" card on
the homepage should land straight in the actual generator, one click, matching how it worked
before Phase 81. It took a couple of exchanges to pin down -- she was actually seeing that already
work correctly on `sight-reading.html`'s own CTA button (Phase 82's fix), but the homepage
entry card itself still routed through `sight-reading.html` first (Phase 81 #2), requiring a
second click.

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Homepage card links straight to the generator again | `index.html` | The "Practice sight-reading" entry card's `onClick` changed from `window.location.href = 'sight-reading.html'` to `window.location.href = 'https://piano-butler-sightreading.onrender.com/sight-reading-generator'`. `sight-reading.html` itself is untouched and stays live/indexed for organic search traffic landing on it directly from Google -- only the homepage's own click-through path changed. Verified with `@babel/core transformSync` (`runtime:'classic'`) + `new Function()` on the inline script -- 0 errors. Committed as `43e52f8`, not yet pushed. |
| 2 | Note on concurrent editing | -- | Hit a real (not stale) git lock contention while committing this -- another session was actively committing to this same repo at the same time (`ea7b4f9`, "Unify Sight-Reading Generator design with Ink & Brass", landed on `sightreading-generator/client/public/*` and `sight-reading.html` mid-way through this session's own commit attempts). Waited for `ps aux` to show no running git process and the working tree to settle before removing the resulting stale lock files and retrying -- did not touch any of the other session's in-flight files. Worth keeping in mind: this repo can have more than one Claude session working in it concurrently now (a "design room" session appears to exist alongside this Director session). |

### Phase 84 Updates (2026-09-17 — timeline.html mode-choice button generalized)

Sohyun saw the new mode-choice screen (Phase 81/82's "What are you preparing for?") and asked
not to lead with "AMEB" on the entry button. Asked her directly whether she wanted the label
generalized only, or the underlying AMEB grade/technical-work/repertoire data actually broadened
to other syllabuses (ABRSM/Trinity) inside that option -- she confirmed label only, keeping the
Phase 61 Reference Integrity restriction (AMEB-only, since that's the syllabus she's personally
taught/sat) fully intact.

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Button title generalized | `timeline.html` | The mode-choice button's title changed from "AMEB Piano exam" to "Piano exam". Its description line underneath is unchanged ("Grade-specific plan using the real AMEB syllabus — technical work and repertoire included.") so the page stays honest about what's actually inside once picked. No other AMEB-specific copy or logic touched. Verified via `@babel/parser` (jsx plugin) -- 0 errors. Committed as `21214f4`, not yet pushed. |

### Phase 85 Updates (2026-09-17 — Sight-Reading Generator header logo now links home)

Sohyun sent screenshots of the generator app noting the "Piano Butler" logo/button in the
header didn't do anything when clicked -- she expected it to go back to the homepage.

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Header brand mark is now a real link | `sightreading-generator/client/public/index.html`, `.../style.css` | The header's "Piano Butler" mark was a plain `<div class="brand">` -- never a link, so clicking it did nothing. Changed it to `<a class="brand" href="https://thepianobutler.com/index.html">` (absolute URL, since this app is hosted on a separate Render domain, not thepianobutler.com itself). Added `color: inherit; text-decoration: none; cursor: pointer;` to `.brand` in `style.css` so it keeps its existing look instead of turning into a plain blue underlined link. Verified both files are still well-formed (diff reviewed line by line). Committed as `1e214e3`, on top of a concurrent commit from another session (`5f3e8e1`, unrelated font/layout fixes to the same app) -- confirmed via `git diff` that neither commit touched the other's changes. |

### Phase 86 Updates (2026-09-17 — timeline.html: free-text label + focus-area checklist replaces AMEB grade picker)

Sohyun sent screenshots of `timeline.html`'s AMEB grade-picker screen and asked to drop grade
selection entirely -- exams differ, this tool isn't AMEB-only, and she isn't going to input every
board's full syllabus data. Her direction after a clarifying round: since she won't be entering
detailed syllabus info herself, let users type what they're preparing for and check off which
areas they need (pieces, technical work, sight-reading, theory), and build a general time-
management strategy from that -- not syllabus-specific content. She explicitly delegated the
concrete design ("너 생각은 좀 구체적으로").

This is a genuine reversal of Phase 61's "AMEB-only, real syllabus data" restriction and Phase
84's "label-only" generalization -- treated as a strategic/scope decision and escalated via
`AskUserQuestion` before building, per this session's standing contract.

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Head/meta tags and Phase 61 comment generalized | `timeline.html` | Title, meta description, OG/Twitter tags no longer mention AMEB or grades -- now describe the tool as "Enter your exam or performance date and pick what you need to prepare... to get an instant month-by-month practice timeline." The old Phase 61 comment explaining the AMEB-only restriction was rewritten to document Phase 86's reasoning: Reference Integrity is now kept intact by making **no** board-specific claims at all (rather than restricting detailed claims to AMEB), so genuinely no syllabus data is fabricated for any board. AMEB-specific helpers/components/data (`getTechnicalWork`, `PieceInput`, `pickRepertoire`, `GRADE_OPTIONS`, the `AMEB_*` data script tags) are left in place, unused, in case a syllabus-specific mode is wanted again later. |
| 2 | Checklist-builder engine threaded with a `focus` parameter | `timeline.html` | `foundationChecklist`, `technicalChecklist`, `musicalChecklist`, `consolidationChecklist`, `polishChecklist`, `examChecklist`, `buildMonthContent`, `buildTimeline` all now accept `focus = {pieces, technical, sightread, theory}` and filter their bullet lines by selected area, falling back to a generic line (e.g. "Keep working steadily toward your goal this month.") rather than ever rendering an empty checklist. `technicalChecklist` shows "Not a focus area for you this time..." when technical work wasn't selected, matching the pattern live-verified below. |
| 3 | `App()` state model and full render tree rebuilt | `timeline.html` | Removed `mode`, `gradeKey`, `gradeLabel`, `repertoire` state entirely. Added `focus` state (all four areas default `false`) and `anyFocus`/`effectiveGradeLabel`/`userPieces`/`quizQuestions` derived values. The old three-screen step 0 (mode choice -> AMEB grade grid -> generic name entry) is now a single screen: a free-text "What are you preparing for?" label input, followed by "What do you need to prepare?" with four toggle buttons (Repertoire/pieces, Technical work, Sight-reading, Theory), with Next disabled until at least one is selected. The date step's Next button now skips straight to the quiz (screen 3) when "pieces" wasn't selected, instead of always visiting the pieces step. The quiz only asks questions matching selected focus areas (`READINESS_QUESTIONS_GENERIC`, ids matching the `focus` keys), and a raw score is rescaled (`4 + ((raw - qCount)/(qCount*3))*12`) onto the same 4..16 range `allocatePhases()` expects regardless of how many questions were actually asked. Two now-impossible JSX blocks referencing deleted state (`technicalWork`, `repertoire`, `gradeLabel` -- the AMEB Technical Work Checklist card and "more repertoire" link) were deleted outright rather than left to throw `ReferenceError`s. |
| 4 | Wording bug caught during live testing | `timeline.html` | `MONTH_FOCUS.exam`'s line read "...rest well before the {grade} exam." -- harmless when `{grade}` was always a controlled AMEB string like "Grade 4", but now that `{grade}` is the user's free-text label (which the placeholder itself suggests should contain the word "exam", e.g. "Grade 4 piano exam"), this produced a visible "...before the Grade 4 piano exam exam." Fixed to drop the trailing "exam.", matching the equivalent line already used elsewhere in the file (`Trust the preparation — rest well before ${grade}`). Would not have been caught without the live run below. |
| 5 | Verification | — | JSX parse-checked with `@babel/parser` (jsx plugin) and full-compile-checked with `@babel/core transformSync` (`preset-react`, `runtime:'classic'`) + `new Function()` -- 0 errors. Grepped the compiled `App()` body for every removed variable (`mode`, `gradeKey`, `gradeLabel`, `repertoire`, `technicalWork`, `isGeneric`, `SYLLABUS`) to confirm zero leftover live references (only two harmless code-comment mentions of "mode" remained). Live-tested end to end in headless Chromium inside the cloud workspace (React 18 + Babel-standalone **7.23.3 pinned to match the production `<script>` tag** -- an earlier attempt with the latest npm-installed Babel-standalone (8.0.5) produced a false failure, since its `preset-react` now defaults to the automatic JSX runtime and emits an `import` statement that breaks a classic `<script>` tag; pinning the version confirmed this was a test-harness artifact, not a real bug). Three full flows driven end to end: (a) pieces+sight-reading focus with a typed piece -- correct plan, correct piece name threaded through every month, quiz asked only the 2 matching questions, exam-month wording fix confirmed live; (b) technical+theory focus with no pieces selected -- confirmed the pieces step is skipped entirely and the quiz asks only the 2 matching questions; (c) Next button correctly stays disabled on step 0 until at least one focus area is toggled on. Zero console/page errors across all three runs (only expected 404s for AMEB data files intentionally absent from the trimmed offline test copy, and blocked font/analytics network calls). |
| 6 | Committed, not pushed | `21423a5` | Ready for Sohyun to push from her Terminal. |

### Phase 87 Updates (2026-09-17 — homepage: exam-year notation removed)

Second half of the same request that produced Phase 86. Sohyun confirmed the location directly
when asked ("네, 홈페이지의 시험 연도 표기 (추천)") -- the homepage's board mentions ("AMEB Piano
2026", "ABRSM Piano 2025 & 2026", "Trinity Piano 2023") shouldn't carry a syllabus year, since
it's implementation detail that needs manual upkeep every year regardless.

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Year suffix stripped from every board mention | `index.html` | Removed "2026"/"2025 & 2026"/"2023" from: the 3 meta description variants (`description`, `og:description`, `twitter:description`), all 27 BreadcrumbList structured-data `ListItem` names, the 3 `SYLLABUS_PAGES` board-card labels (`AMEB Piano`, `ABRSM Piano`, `Trinity College London Piano`), and 5 body-copy headings/paragraphs in the no-JS fallback content. Board names themselves (AMEB/ABRSM/Trinity) are untouched -- these remain functionally necessary since they're how the search tool's results are labeled/filtered, and Sohyun's confirmed request was specifically about the year notation, not the board names. |
| 2 | Verification | — | JSX parse + Babel compile check (`@babel/parser` jsx plugin + `@babel/core transformSync`) on the inline `app-jsx` script -- 0 errors. Regex-swept for any leftover `(AMEB|ABRSM|Trinity)...20XX` pattern near a board mention after the edit -- none found. |
| 3 | Scope note | — | Sohyun's original message also mentioned "exam piece" wording and de-emphasizing specific board names more broadly, in the context of the same screenshots (`timeline.html` + homepage). That's already satisfied for `timeline.html` by Phase 86's rewrite, which no longer references any board name at all. Left `index.html`'s AMEB/ABRSM/Trinity result badges untouched -- those are core functional labels for a live search tool (not decorative copy), and she didn't confirm that broader scope when asked directly; revisit if she asks for it explicitly. |
| 4 | Committed, not pushed | `12276c9` | Ready for Sohyun to push from her Terminal. |

### Phase 88 Updates (2026-09-17 — timeline.html: local progress tracking + email backup)

Sohyun asked whether the results screen could actually track progress (it couldn't -- the
"Save & track progress" button only opened a waitlist modal). Walked through the options: local
device-only tracking (fast, no backend, matches the site's existing local-first pattern) vs.
Supabase/Magic-Link tracking (real cross-device sync, matches `teacher-dashboard.html`'s existing
infra, but much bigger build) vs. real recurring reminder emails (needs a scheduler + email API --
biggest build of all). She confirmed: local tracking, plus something better than local-only for
portability -- landed on local checkboxes + a one-time "email me a copy" backup button, since a
scheduled/recurring reminder email would need real backend infrastructure to build.

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Checklist items are now real, persisted checkboxes | `timeline.html` | Each checklist line in a month card is now a `☐`/`☑` toggle. Toggling saves immediately to `localStorage['pb_timeline_v1']`, keyed by month + item index -- same "local-first" pattern already used by `index.html`'s `pb_lists_v1`/`pb_interests_v2` (no login, no Supabase, nothing leaves the device). |
| 2 | Plan auto-saves on generation, silently restores on reload | `timeline.html` | The full set of inputs needed to rebuild the exact same plan (label, exam date, pieces, focus, and the scaled readiness score -- `buildTimeline()` needs all of these, not just the rendered result) is saved the moment a plan is generated. On page load, a saved plan is silently restored straight into the results screen with checked items intact, unless its exam date has already passed (then it's discarded rather than shown, since `buildTimeline()` can't produce a timeline for a past date anyway). "Start over" clears the saved plan. |
| 3 | Current month highlighted, past months dimmed | `timeline.html` | Added a "THIS MONTH" badge on the month matching today's date. `MonthCard`'s `isPast` prop existed already but was hardcoded to `false` (dead) -- now wired to the real month comparison, so past months actually dim as originally intended. |
| 4 | "Save & track progress" replaced with a real "Email me this plan" button | `timeline.html` | The old button opened `LoginPrompt`, a waitlist modal promising "tracking is coming soon" -- now inaccurate and misleading, so removed entirely (component deleted, not left as dead code, since its copy actively contradicts the new reality). Replaced with a `mailto:` link containing a plaintext month-by-month summary (capped at ~1800 characters, since mailto bodies can silently truncate in some mail clients well before that) -- a zero-backend way for a user to keep a portable copy outside this browser. A small note under the results header now says progress saves automatically on this device. |
| 5 | Real process-safety catch: the Phase 86 exam-wording fix had never actually landed | `timeline.html` | While live-testing this feature, the same "...before the Grade 4 piano exam exam." wording bug reappeared -- turned out the Phase 86 session's fix was applied only to a staged test copy of the file (`/mnt/user-data/uploads/...`) and never to the real file, even though the Phase 86 commit message claimed it was fixed. Confirmed via `git show HEAD:timeline.html` that the committed version still had the bug. Applied the one-line fix for real this time, directly to the file about to be committed, and diffed it against the already-verified test copy to confirm they now matched exactly before committing. Worth remembering: always verify a fix landed in the actual device file, not a staging/test copy, before trusting a commit message that says it's fixed. |
| 6 | Verification | — | JSX parse + Babel compile check -- 0 errors. Live-tested end to end in headless Chromium: generating a plan auto-saves to `localStorage`; toggling a checkbox persists immediately; reloading the page (fresh tab, same browser storage) silently resumes into the results screen with checked state intact; "Start over" clears the saved state; the "THIS MONTH" badge appears on the correct month; the mailto href decodes to a correctly-formatted, non-truncated plan summary with the exam-wording fix confirmed present in the actual generated output. |
| 7 | Note on concurrent editing | — | Hit real (not stale) git lock contention twice while committing this -- another session was actively committing `dca5597`/`15cd067` ("Homepage: drop/broaden exam board names from hero tagline", both on `index.html`) to this same repo mid-way through this session's own commit attempt. Waited for `ps aux` to show no running git process and the commit log to stabilize before clearing the resulting stale lock files and retrying -- confirmed via `git show --stat` that neither of the other session's commits touched `timeline.html`. |
| 8 | Pushed and live-verified 2026-09-17 | `c0e8c15` | Sohyun pushed all of Phase 84-88 (`ab1a973`..`0492fb4`, plus another session's unrelated `dca5597`/`15cd067` hero-tagline commits in between) from her Terminal. Live-verified directly on thepianobutler.com via Claude in Chrome: the free-text label + focus-area screen renders correctly with no AMEB grade picker; the pieces step correctly appears (since "pieces" was selected) and the readiness quiz correctly asked only the one matching question; the results screen shows the "THIS MONTH" badge, real checkboxes, the exact exam-wording fix confirmed live ("...rest well before Grade 5 piano exam." -- no duplicate), and the new saved-progress note + "Email me this plan" button; toggling a checkbox and reloading the page correctly resumed straight into the results screen with the checked state intact; "Start over" correctly cleared it back to a fresh screen 0; the mailto href decoded cleanly with no wording bug. Also spot-checked the Sight-Reading Generator's header logo (Phase 85) -- confirmed it's a real link to the homepage. All of Phase 84-88 is now confirmed working on the live site, not just in this session's local tests. |

### Phase 89 Updates (2026-09-18 — drills.html: new "Practice Drills" toolbox, first drill built)

Multi-turn brainstorm, not a single request: Sohyun described a grocery-catalog-sticker-inspired
gamification/rewards idea (virtual room decoration, credits, possibly real-world rewards) and
asked for more lightweight "촉진제" (catalyst) feature ideas usable casually during a lesson. This
evolved into a distinct, smaller concept she confirmed first: rather than a fixed linear
progression, an open-ended "drill toolbox" of quick, on-demand mini-exercises for skills students
repeatedly struggle with (note reading, rhythm, key signatures, intervals, etc.), with randomized
content so a drill doesn't go stale on repeat use. From her own teaching practice she described two
concrete drills -- (1) fast rhythm/beat "chunking" recognition for sight-reading, and (2) a reverse
letter-naming / interval call-and-response exercise she already does live with students (teacher
says a letter, student says the next one per a chosen interval and direction, alternating turns --
e.g. "3rd down": C→A→F→D...). She explicitly confirmed building the interval/letter-chain drill
first, "진짜 심플하게" (really simple): screen shows a letter, student says the next one according
to the interval relationship, with different behavior for ascending vs. descending.

This was handled as pure ideation across several turns -- proposing grounded options, asking
clarifying questions, not building anything -- until Sohyun gave an explicit, narrowly-scoped
confirmation for this one specific drill.

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | New page: `drills.html` | `drills.html` (new) | Standalone, `noindex, follow` page matching `timeline.html`'s boilerplate pattern exactly (favicon, meta tags, React 18.2.0 + Babel-standalone 7.23.3 via cdnjs, Google Fonts Inter, gtag). Built as a `DRILLS` registry (`[{id, label, render}]`) with a chip-based picker in `App()`, so future drills (rhythm chunking, key signatures, interval distance, keyboard↔note-name matching -- all raised in the brainstorm but not yet built) can be added as additional registry entries without restructuring the page. |
| 2 | First drill: Letter Chain | `drills.html` | Digitizes only the setup/answer-checking side of Sohyun's existing spoken exercise -- it doesn't replace the live back-and-forth, it removes the mental-arithmetic burden of computing the next letter. Direction (Ascending/Descending) and interval (2nd–8ve, traditional inclusive counting) are chip-selected; a large letter display shows the current letter; a single "Show answer"/"Next →" button reveals then advances through `nextLetter(current, intervalSize, direction)`; a running history trail and "New starting note" reset button are included. Interval math verified against Sohyun's own worked example (3rd descending: mathematically equivalent to her stated C→A→F→D pattern). |
| 3 | Brand palette reused, no new colors introduced | `drills.html` | Loaded the confirmed Ink & Brass palette via the `piano-butler-designer` skill (`--bg:#f8edd4`, `--text:#241f1a`, `--muted:#a49b8f`, `--border:#e8dcc0`, `--brass:#a8823f` used only for the revealed-answer text) rather than re-deriving colors, consistent with `timeline.html`. |
| 4 | Discoverability: no homepage entry point added | `drills.html` | Left unlisted/direct-URL-only for now, same as `timeline.html`'s original launch pattern -- this is a teacher-facing lesson tool Sohyun would likely bookmark directly rather than something that needs homepage promotion, similar to `teacher-dashboard.html`'s deprioritized status. Not explicitly confirmed with her; tracked below as a pending decision rather than assumed. |
| 5 | Verification | — | JSX parse-checked with `@babel/parser` (jsx plugin) and full-compile-checked with `@babel/core transformSync` (`preset-react`, `runtime:'classic'`) + `new Function()` on the local test copy -- 0 errors. Full Playwright live-interaction test in headless Chromium (React 18 + Babel-standalone 7.23.3 pinned to match production) confirmed: default Ascending+2nd produces the correct forward chain (C→D→E→F→G); Descending+3rd produces a chain independently checked against a locally-computed reference function across 6 rounds, all correct, matching Sohyun's own example pattern; "New starting note" correctly resets history to a single letter with no arrow; zero console/page errors throughout. Per this project's own Phase 86 lesson (a fix verified only against a staging copy, not the real device file, was wrongly trusted), the actual device file was re-staged and re-run through the same parse+compile check after being written, and diffed byte-for-byte against the already-tested local copy to confirm they matched exactly before committing. |
| 6 | Committed, not pushed | `29502ef` | Ready for Sohyun to push from her Terminal. |

### Phase 90 Updates (2026-09-19 — Scale Fingering drill: all 15 major keys, key-signature staff notation, dual view mode)

Direct continuation of Phase 89's drill toolbox. Sohyun asked for a second drill (`ScaleFingeringDrill`
inside `drills.html`) built earlier this same arc: pick any major key, see both hands' fingering
overlaid on an on-screen keyboard. It shipped with only C/G/A filled in and a single view grouped
by "fingering family" (which black-key cluster a scale's black keys fall into). This session filled
in the remaining 12 keys and made several rounds of corrections against Sohyun's own review, per an
explicit workflow shift she requested mid-session: "일단 표준 너가 다 넣고 틀린걸 내가 잡아낼게" (fill
in a best-effort standard for everything, she'll flag what's wrong) -- a deliberate exception to this
project's usual Reference Integrity discipline of verifying every data point against the AMEB PDF
before shipping, scoped to just this one sub-task.

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Key-signature staff notation | `drills.html` (`KeySigStaff`) | Added a real SVG treble-clef staff (5 lines + clef glyph + sharp/flat symbols in correct order and position) to the "by key signature" view, so a key's actual staff notation shows next to its keyboard fingering. `SHARP_ORDER`/`FLAT_ORDER` and `SHARP_POS`/`FLAT_POS` position maps cross-checked against the real AMEB PDF's "Key signatures of relative major and minor keys" page (printed p.10 / PDF p.3) -- exact match. |
| 2 | Dual view mode, key-signature view now default | `drills.html` | Added a toggle between "By key signature" (circle-of-fifths order, sharps 0-7 then flats 1-7) and "By fingering family" (the original grouping). Per Sohyun's request ("키 시그니쳐 그룹이 첫번째 보이게 먼저 하자"), key-signature is now the default and listed first. |
| 3 | All 15 major keys filled in | `drills.html` (`SCALES`) | D and E added via the plain standard formula (same shape as C/G/A). F major added from Sohyun's own dictated fingering (RH 1234/123/1234/123/4, LH 5/4321/321/4321/321 for 2 octaves) -- matches AMEB Grade 1 p.27 (1.4), which the scan itself was too low-resolution to transcribe confidently. B/Cb major's LH corrected by Sohyun directly (4321/4321/321/4321). Bb/Eb/Ab/Db/C# use a general black-root-key RH rule Sohyun specified: start on finger 2, whichever note is the first white key reached gets the thumb, then repeat the standard [1,2,3,1,2,3,4] unit -- confirmed to exactly match the real AMEB Bb major scan (Grade 2 p.37, 2.4). |
| 4 | F#/Gb major given its own explicit fingering | `drills.html` (`SCALES['F#']`, `SCALES.Gb`) | The generic black-root rule from #3 turned out wrong for F#/Gb specifically: F# has three consecutive black keys per octave (F#-G#-A#) rather than Bb's black-white-white shape, so the fixed unit misplaced fingers. Sohyun caught this from a live screenshot and dictated the correct fingering directly: RH 234/123/1234/123(/2 for the 2nd octave), LH 4321/321(/4321/321/4 for the 2nd octave). Verified by hand-deriving F#'s full pitch-class sequence and confirming her digits land the thumb only on the scale's two white notes per octave (B and E#/F) exactly where she said. Still an open question whether C#/Db, Eb, Ab also have similar exceptions the generic formula gets wrong -- flagged for Sohyun to check as she reviews the rest. |
| 5 | 1-octave versions for every key | `drills.html` | Previously only 2-octave fingering existed for the newer keys. Added a matching 1-octave entry for all 15 keys (e.g. F major's 1-octave RH correctly ends on finger 5 since its top note is white, instead of continuing into a would-be 2nd octave). |
| 6 | Keyboard SVG clipping fix | `drills.html` (`ScaleKeyboard`) | A leading black key (on black-root scales) or a trailing black key was being cut off at the SVG boundary. Fixed by widening the viewBox by one black-key-width, split evenly on both sides: `viewBox={(-blackW/2)+' 0 '+(whiteCount*whiteW+blackW)+' '+whiteH}`. Confirmed via Playwright screenshot of F# major showing no more clipping. |
| 7 | Removed per-entry "Source: ..." UI text | `drills.html` | Sohyun asked for the citation footer removed from the live view (kept only as code comments for internal tracking, since Reference Integrity still matters for future edits -- just not shown to her while she's reviewing quickly). |
| 8 | Verification | — | Babel parse + full-compile check (`@babel/parser` + `@babel/core transformSync`, `preset-react`, `runtime:'classic'`, then `new Function()`) on both `drills.html` and its mirrored Artifact-tool copy -- 0 errors both times. Playwright screenshots in headless Chromium of F# major (1-octave and 2-octave, both hands) confirmed the corrected RH/LH sequences render exactly as Sohyun specified, digit for digit. The device file was re-staged after being written and MD5-diffed against the already-verified working copy (`d5e9f5a664db3cc5f3f17a6da884ffc0`) to confirm an exact match before committing, per this project's standing lesson about trusting a staging copy over the real device file. |
| 9 | Committed, not pushed | `cbf9e3b` | Ready for Sohyun to push from her Terminal. |

### Phase 91 Updates (2026-09-22 -- YouTube "Listen" button relevance fix)

Sohyun flagged (with a screenshot) that clicking "Listen" on the AMEB Grade 7 Manual-list piece
"Sky dive samba" (R. KEANE) played a completely unrelated YouTube Shorts clip (an Ed Sheeran/Lewis
Capaldi friendship video from Warner Music Canada), and noted this happens occasionally on other
pieces too ("이거 클릭했는데 상관없는 유투브 뜨고 이런것도 간혹 있더라구").

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Root cause confirmed | `index.html` (`useVideoModal`) | The Listen button did a live YouTube Data API v3 search (`composer surname + title + "piano"`) and blindly embedded the #1 raw result with `maxResults=1` and zero relevance checking. Reproduced live via Claude-in-Chrome on the real site, then replicated the exact API call in-page (to use the referrer-restricted key) with `maxResults=5`: for "Sky dive samba" the top 3 real results are all genuinely unrelated content -- this is a YouTube search-relevance failure for obscure/niche pieces, not a data or logic bug elsewhere in the app. |
| 2 | Fix: keyword-overlap relevance filter | `index.html` (`useVideoModal`, new `ytKeywords`/`pickBestYtMatch` helpers) | Now fetches the top 5 candidates instead of 1. Each candidate's YouTube title is scored against the piece's own title (stopword-filtered keyword overlap, e.g. "sky"/"dive"/"samba") plus a small bonus for composer-surname match. A candidate is only accepted if it clears roughly 50% keyword overlap with the piece title; otherwise the modal falls back to the existing "No video found" state instead of embedding a wrong video. |
| 3 | Verification | -- | Babel `transformSync` (`preset-react`, `runtime:'classic'`) + `new Function()` syntax check passed on the full `app-jsx` block. Live-verified via Claude-in-Chrome, replicating the app's exact query logic in-page against the real YouTube API for two cases: the reported bad case ("Sky dive samba" -> now correctly returns no match, previously showed the Ed Sheeran clip) and a well-known piece ("Chopin Nocturne Op.9 No.2" -> still correctly matches the right video, confirming the fix doesn't break legitimate matches). |
| 4 | Committed, not pushed | `6659b7e` | Ready for Sohyun to push from her Terminal. |

### Phase 92 Updates (2026-09-22 -- admin-search.html hang, G5 data-file question)

Follow-up on the two items flagged (not yet acted on) at the end of Phase 91. Sohyun said to go
ahead and resolve both.

| # | Item | Resolution | Detail |
|---|------|-----------|--------|
| 1 | `admin-search.html` hangs indefinitely on load | **Fixed** | Root cause: the password gate called `window.prompt()`, a native blocking browser dialog. A native dialog freezes the page's JS thread entirely until a human answers it, and isn't visible to browser-automation screenshots (they only capture the page's own rendered content, not native browser chrome). Reproduced live via Claude-in-Chrome: the page showed as an endless blank screen and the JS thread was fully frozen (even a trivial `1+1` eval timed out) -- this is almost certainly what Sohyun saw too, whether or not the native dialog was visibly registering for her. Fixed by replacing `window.prompt()` with a plain in-page HTML form (`#pbAdminGate`, a fixed full-screen overlay) that never blocks JS -- same password and `sessionStorage` key as before. Verified via Babel/`new Function()` syntax check, and via an isolated Playwright test of the extracted gate markup covering all 4 cases (fresh load never blocks JS; wrong password shows an inline error and doesn't crash; correct password removes the overlay, reveals the app, and sets `sessionStorage`; a returning session skips the gate instantly on reload). Committed as `b55d69e`, not pushed. |
| 2 | `G5/data_g5.js` vs `G5/data_g5_1.js` | **Not a bug -- already self-documented** | Opening `data_g5.js` shows it already carries its own header: `"DEPRECATED -- This is an old skeleton file... Use data_g5_1.js (DATA_G5) as the authoritative Grade 5 Comprehensive data source... kept for reference only and is NOT used by any HTML page."` Confirmed via `grep` across every `.html` file that only `data_g5_1.js` is ever `<script>`-included -- `data_g5.js` is inert. Git history shows both files already existed at this repo's very first commit, so whatever the original reason for keeping the old skeleton was, it predates this project's tracked history and was a deliberate decision by someone (labeled "kept for reference," not an oversight). Left untouched -- did not delete or move it, since removing a file explicitly marked "kept for reference" without being asked crosses this project's standing rule against deleting data Claude didn't create itself. No code or data change made. |

### Phase 93 Updates (2026-09-22 -- admin-counts.html rebuilt into Sohyun's piece-count dashboard)

Sohyun wants a real working dashboard for tracking piece counts across syllabuses/editions as the
catalogue grows (more exam boards, and older AMEB syllabus editions kept alongside 2026 since
AMEB allows some older-syllabus pieces as exam "extra" selections even under the current
syllabus). `admin-counts.html` already existed and is almost exactly this -- a per-syllabus,
per-grade piece-count table with an Expected-vs-Actual check against this file's own targets --
but it turned out to be completely unusable.

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Same `window.prompt()` hang as `admin-search.html` | `admin-counts.html` | Identical bug, identical fix: replaced with the same in-page `#pbAdminGate` HTML form. |
| 2 | Dead second gate removed | `admin-counts.html` | Past the password gate, a `LoginGate` component required a Supabase login session and redirected to `login.html` if absent -- but `login.html` was deleted in an earlier cleanup, so this always redirected to a dead page. Removed `LoginGate` entirely (the password gate is this page's real access control) and the now-pointless unconditional `supabase.createClient()` call with it, which was also a latent crash risk: it threw if the Supabase CDN script was ever slow/blocked, for a client the page didn't even use anymore. |
| 3 | Real data bug found while verifying: Grade 5 always showed 0 / MISSING | `admin-counts.html` | The code checked `typeof DATA_G5_1 !== "undefined"`, but `G5/data_g5_1.js` declares `const DATA_G5 = [...]` -- the `_1` is only in the filename, not the variable name. Every Grade 5 lookup silently fell through to an empty array. This exactly accounted for the dashboard's 168-piece gap from the true total (4,332 vs. 4,500 -- 168 is exactly G5's piece count). Fixed the variable name. |
| 4 | Verification | -- | CDN libraries (unpkg/jsdelivr/Tailwind) aren't reachable from this sandbox, so real React/ReactDOM/Babel-standalone builds were pulled from the npm registry and used to run a full Playwright test against a local copy with all real grade/syllabus data files staged in -- not just a syntax check. Confirmed: fresh load never blocks JS; wrong password shows an inline error and stays gated; correct password actually mounts the React dashboard (checked via real rendered DOM content, not raw script text); no redirect to the dead `login.html`; and after the Grade 5 fix, Grand Total reads exactly 4,500 with 0 MISSING rows, matching every row of the page's own Expected-vs-Actual table. |
| 5 | Committed, not pushed | `62ac7d9` | Ready for Sohyun to push from her Terminal. |

**Roadmap discussion, not yet built:** Sohyun is considering adding other exam boards (RCM, LCM,
etc. -- looked at pianosyllabus.com as a reference, which covers ~14 boards, tracks multiple
syllabus editions per board, and cross-references the same piece's grade across boards) and older
AMEB syllabus editions alongside 2026. Advised: new boards fit the current architecture cleanly
(same pattern as AMEB/ABRSM/Trinity coexisting today) and are lower-risk to add; older editions
are lower priority to consider carefully first since (a) the Reference-Integrity verification
burden scales with data volume and this project has already hit real data-accuracy issues at the
current size, and (b) meaningfully cross-referencing "same piece, different board/edition" (the
part of pianosyllabus.com that's actually valuable, not just row count) would need a canonical
piece-identity field (e.g. a catalog number like BWV/Op.) that the current schema doesn't have --
worth adding deliberately if/when this expansion happens, rather than bolting on after the fact.
No schema or data changes made yet; this is queued for whenever Sohyun decides the concrete scope.

**Follow-up same day:** Sohyun spotted "AMEB Leisure 705 != 706" on the live dashboard right after
this shipped. Checked -- the data (705) was already correct; the dashboard's own hardcoded target
was stale. Phase 33 (2026-05-15) had legitimately fixed a real duplicate (BEETHOVEN's Andante in
both S4 and S1 of G8 Leisure, PDF confirmed S4 only) and dropped the true count 706->705, but this
dashboard's comparison target was never updated to match at the time. Fixed the target to 705 with
a code comment explaining the history, committed as `4cb8ea3`, not pushed. Lesson for next time a
mismatch shows up here: check whether the *data* is wrong or whether it's the *target* that's
stale -- this file has now had one of each.



### Phase 94 Updates (2026-09-23 -- drills.html: shared drill engine + Note Names concept set)

Direction agreed with Sohyun this session (her words, summarized): extend `drills.html` into a
"shared game engine + per-drill question generator" structure. Every concept is a SET of an
infographic and a drill that share the same music data. The user is Sohyun (teacher), and she must
be able to share a link with a student. A drill + difficulty opens directly from URL parameters; no
login, records saved on the device. Two modes: Lesson and Game (pixel). First drill: keyboard <->
note-name matching; next: key signatures (infographic + drill). Homepage entry point: still on hold
(Pending #14 stays open, now explicitly her call to hold).

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Shared `DrillEngine` | `drills.html` | Music-agnostic engine. A concept supplies `levels`, `generate(level, prev)`, `check(q, ans)`, `answerLabel(q)`, a `Question` component and a `Learn` component. **Lesson mode**: 10 questions, no timer, a correct answer auto-advances, a wrong one shows the answer and waits for "Next" so the teacher can talk it through, then a score / best summary. **Game (pixel) mode**: Press Start 2P font, ink panel with brass pixel border, PRESS START title screen, 3 lives, per-question countdown bar (per-level seconds), +10 per hit plus streak bonus (+2 per streak step, capped at +10), GAME OVER screen with best. Records: `localStorage['pb_drill_records_v1']`, keyed `drill|level|mode` -> `{plays, best, lastAt, history (last 20)}`, all wrapped in try/catch. |
| 2 | Concept 1: Note Names | `drills.html` (`PC_INFO`, `TapKeyboard`, `NoteNamesLearn`, `NoteNameQuestion`, `NOTE_NAMES_DRILL`) | `PC_INFO` (12 pitch classes, white/black, sharp+flat names) is the single data source for both the Learn infographic and the drill. Learn: 1-octave labelled keyboard with C-D-E / F-G-A-B groups tinted by their 2- and 3-black-key groups, plus 4 short tips (C left of the 2 blacks, F left of the 3 blacks, only A-G, sharp = right / flat = left). Drill levels: L1 white keys, name the highlighted key (A-G buttons, physical A-G keys also work); L2 white keys, tap the named key; L3 two octaves, both directions; L4 black keys too (12 choices shown as "C♯ / D♭", name-to-key prompts randomly use the sharp or the flat spelling, any octave counts). Never asks the same pitch class twice in a row. |
| 3 | URL state + student link | `drills.html` (`readUrlState`, `App`, `ShareLink`) | `?drill=<id>&tab=learn\|drill&level=<n>&mode=lesson\|game&lock=1`. The URL is kept in sync via `history.replaceState`. Unknown drill / level falls back to defaults. "Copy link for a student" (clipboard, falls back to a selectable text box, never a native dialog) builds a `lock=1` link: the drill picker and level/mode controls are hidden and the header shows just the drill's name; the Learn tab stays available to the student. |
| 4 | Registry | `drills.html` (`DRILLS`) | Now accepts both shapes: `{id,label,render}` (Letter Chain, Scale Fingering, both unchanged) and `{id,label,concept}`. Note Names is listed first and is the default drill. |
| 5 | Verification | -- | `@babel/core transformSync` (`preset-react`, `runtime:'classic'`) + `new Function()` on the device file: 0 errors. cdnjs is blocked from the sandbox, so React 18.2.0 / ReactDOM / Babel-standalone 7.23.3 were pulled from npm and served to a full Playwright run (390px phone viewport) against the exact device file (MD5 `e77a36ca…` matched before commit). Confirmed: Learn renders, and "Start the drill" switches tab + URL; a full 10-question lesson with one deliberate wrong answer (Next button shown, red/green marking correct) ends at 9/10 and writes the record; the A-G keyboard shortcut works; a locked game link (`level=2&mode=game&lock=1`) hides the chips, runs PRESS START, 3 correct answers score 36 with STREAK x3, a miss marks the tapped key red and the answer green, timeouts drain the remaining lives, and GAME OVER saves the record; Level 4 correctly offers sharp/flat choices and 2-octave keys; Letter Chain and Scale Fingering still render; bogus params fall back cleanly; zero page/console errors. The pixel font itself couldn't load in the sandbox (Google Fonts blocked), so the pixel look still needs a real-browser look after push. |
| 6 | Committed, not pushed | `7072051` | Ready for Sohyun to push from her Terminal. |

Also this session: live-verified the Phase 71 `MyListsPanel` inline-delete fix on the real site
(first click shows "Delete? [Delete] [Cancel]", no native `confirm()` fired, second click removes
the list from both the UI and `localStorage`; Sohyun's existing "Test List" untouched). Committed
the pending CLAUDE.md note on the 2026-09-19 AdSense rejection / wait-for-traffic decision as
`84aec74`.

### Phase 95 Updates (2026-09-23 -- drills.html: Tempo Race concept set)

Sohyun shared photos of two commercial classroom teaching aids (numbered scale cards; tempo-term
"cars" on a rainbow racetrack) and asked about drills built per chapter in that spirit. Agreed to
borrow the CONCEPTS only -- no artwork, characters or card designs reproduced. She chose to start
with the smallest one ("제일 적은것부터"): Tempo Race with the 7 core terms.

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | `TEMPO_DRILL` concept on the Phase 94 engine | `drills.html` (`TEMPO_TERMS`, `TempoLearn`, `TempoQuestion`, `RaceTrack`, `playClicks`) | 7 terms Adagio -> Presto shared by Learn and Drill. Meanings are standard textbook glosses; BPM ranges shown as "about" (sources disagree); Andantino treated as a little faster than Andante (modern convention, historically ambiguous). Learn: slow-to-fast lanes, tap a term to hear its beat (Web Audio metronome, no files). Levels: L1 term -> meaning, L2 which is faster, L3 order 4 slow -> fast (with Undo), L4 listen to the beat and pick (distractors >= 30 bpm from the answer). An original simple race-track bar moves the car one step per correct answer in both modes. Engine now passes `stats` ({correct, asked, streak}) to every Question. |
| 2 | Verification | -- | Babel compile + `new Function()`: 0 errors. Playwright (390px) against the exact device file (MD5 `f46bb9b7…` matched): Learn plays/marks the tapped term; L1 full 10-question lesson with one deliberate miss ends 9/10; L2 x3 correct; L3 Undo works, correct order passes, a swapped order fails with the right order shown; L4 in locked game mode plays, marks miss/answer, reaches GAME OVER; Note Names regression OK; zero page/console errors. |
| 3 | Preview artifact refreshed | claude.ai artifact Dycfqwb9UUvGYyq7qiv6po | Sohyun's review copy of drills.html (was still the Phase 90 version) republished with Note Names + Tempo Race. gtag removed in the preview; URL-parameter student links only work on the real site. |
| 4 | Committed, not pushed | `9c4d331` | Ready for Sohyun to push from her Terminal. |

### Phase 96 Updates (2026-09-23 -- drills.html: Notes & Rests, Rhythm Cards, Key Signatures)

Sohyun shared two more classroom-aid photos (a note/rest board game with symbol/name/beat cards and
+ − = cards; numbered rhythm cards) and said "일단 전체 다 넣어서 만들어줘" -- build all of them.
Concept only again, no product artwork. Naming: British first with American alongside (the
recommended option; she didn't object). She also confirmed Andantino = a little faster than Andante.

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Font-free notation drawing | `drills.html` (`NoteShape`, `RestShape`, `Glyph`, `RhythmSVG`) | SVG heads/stems/flags/dots, rests drawn as shapes, beams per beat with secondary beams and stubs, triplet "3". No music font needed (Noto Music is loaded only for the clef and segno glyphs). |
| 2 | Notes & Rests concept | `drills.html` (`NOTE_VALUES`, `NOTEVAL_DRILL`, `useBoard`, `BoardTrack`) | Learn: note-value tree (1 semibreve → 16 semiquavers, matching rests, beats) + "a dot adds half again". Levels: name the note, how many beats (rests and dotted too), matching rest, add two values, finish a 4/4 bar (exactly one choice fits -- generator verified over 300 runs). Board game in both modes: correct answer rolls 1-3; D.C. -> start and D.S. -> segno, each once per lap; Fine ends the lap. |
| 3 | Rhythm Cards concept | `drills.html` (`RCELLS`, `RHYTHM_TIERS`, `RHYTHM_DECK`, `RHYTHM_DRILL`) | 40 one-bar 4/4 cards from a fixed seed (card numbers are stable), 5 sets: crotchet/minim/semibreve/rests → quaver pairs → quaver rests, dotted crotchets, syncopation → semiquavers → triplets & dotted quavers. Built from beat cells so beaming is always by beat. Learn shows counting (1 e & a, trip-let, rests in brackets) and plays any card with a count-in. Drill mixes "listen and pick the card" with "tap along": 4-click count-in, taps via Space or a big pad, scored against the audio clock (tolerance min(140 ms, 45% of the smallest gap), no extra taps). |
| 4 | Key Signatures concept | `drills.html` (`KEY_SIGS`, `KSStaff`, `KEYSIG_DRILL`) | Learn: order of sharps/flats on the staff, three rules (sharps: up a semitone from the last sharp; flats: second-last flat; relative minor = 6th degree), all 15 keys selectable with major/minor names. Levels: staff -> major (up to 4), major -> count, staff -> major (all 15), staff -> relative minor, order of sharps/flats. Staff positions reuse the Phase 90 PDF-checked maps. |
| 5 | Chapter order | `drills.html` (`DRILLS`) | Note Names, Notes & Rests, Rhythm Cards, Key Signatures, Tempo Race, then Letter Chain and Scale Fingering. |
| 6 | Bug caught in screenshots | `drills.html` | "whole note note" (American name doubled) in the Learn tree and name choices -- fixed before commit. |
| 7 | Verification | -- | Babel compile + `new Function()`: 0 errors. Node run of the data layer: 40 cards, 8 per set, every card sums to exactly 4 beats; 300 rounds of every generator with no duplicate choices, answer always present, "finish the bar" always has exactly one right choice. Playwright (390px) on the exact device file (MD5 `372a7028…` matched): all three Learn pages render; every Notes & Rests and Key Signatures level answers and gives feedback; board moves in game mode; rhythm tap-along with taps on the audio clock scored 10/10 = Correct, and one tap 300 ms late scored 2/3 + 1 extra = wrong; listen question renders; old drills still load; zero page/console errors. Tap feel on a real phone (touch latency) still needs a real-device check. |
| 8 | Preview artifact refreshed | claude.ai artifact Dycfqwb9UUvGYyq7qiv6po | Now shows all five concept sets. |
| 9 | Committed, not pushed | `14ea06c` | Ready for Sohyun to push from her Terminal. |

### Phase 97 Updates (2026-09-23 -- Scales chapter rebuilt, Letter Chain into Note Names, black-key fingerings fixed)

Sohyun pushed Phases 94-96 (`440adca..7aeaaff`). Then asked me to rethink her scale idea (the
Scale Fingering tool + the numbered scale-card photo) "in an efficient way" and to fold Letter
Chain into Note Names (A-G forwards is easy; backwards and skipping inside the 7 letters isn't).

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | **Real data bug fixed from the AMEB books** | `drills.html` (`SCALES`) | Before building, read the black-key-start scales off the AMEB Piano Technical Work books: B♭ (Level 1 p.37, 2.4), E♭ (p.48, 3.4), A♭ (p.59, 4.5), D♭ (Level 2 p.20, 5.4). The generic formula was wrong for E♭/A♭/D♭ RH (it put the thumb on a black key) and for all four LH (it used the mirrored 54321 shape; the books give 3214 3213 ...). Replaced with the printed fingerings; C♯ uses D♭'s (same keys). A data check confirms no thumb lands on a black key in any of the 15 keys, both octave lengths. This closes Pending #15. `blackRootEntry`/`rhPatternBlackRoot` removed. |
| 2 | Scales concept (replaces the Scale Fingering tab) | `drills.html` (`SCALES_DRILL`, `ScalesLearn`, `ScalePath`, `ScaleTapKeyboard`, `spellScale`, `fingerNotes`) | Design idea: the thumb tucks after 3 and after 4, so finger 4 plays once per octave -- one landmark per scale instead of 8 numbers. Learn: a table of RH/LH finger-4 notes for 12 keys (computed from `SCALES` 2-octave data, end notes skipped) with the shortcut "every flat key F→G♭: RH 4 on B♭; B♭ E♭ A♭ D♭ start LH on 3"; 36 stamp cards (12 keys × RH/LH/hands together, localStorage `pb_scale_stamps_v1`, card-deck numbering 1-1…12-3, grouped by shared fingering); the existing fingering viewer (now controlled by the table/cards, key-signature view only) with a computed Landmarks box instead of the black-cluster "family" note. Drill: L1 which finger (C G D A E), L2 tap where finger 4 goes, L3 tap every thumb note (then Check), L4 which finger (all 12). |
| 3 | Letter Chain folded into Note Names | `drills.html` (`LetterCircle`, `LetterStepQuestion`, `genLetterQuestion`) | Learn gets tip 5 (letters go round in a circle), a letter-circle diagram and the original spoken Letter Chain tool. Drill gets L5 "next letter up or down" and L6 "jumps 3rd to octave, up or down" (A-G keyboard keys work; feedback shows both keys). |
| 4 | Registry | `drills.html` | Chapters: Note Names, Notes & Rests, Rhythm Cards, Key Signatures, Scales, Tempo Race. Old `?drill=letter-chain` and `?drill=scale-fingering` links redirect. |
| 5 | Verification | -- | Babel compile + `new Function()`: 0 errors. Node data run: spelled scales and landmarks printed for all 12 keys and checked by eye (e.g. E♭: RH 4 B♭, thumbs F & C; LH 4 A♭, thumbs G & D). Playwright on the exact device file (MD5 matched): aliases redirect; Letter Chain works inside Learn; L5 and L6 full 10-question runs with keyboard answers (9/10 with one deliberate miss); Scales Learn table/stamp/landmark box; all 4 Scales levels answer and mark correctly; zero page/console errors. |
| 6 | Pushed and live-verified | `d6e3a4a`, `c4f6ee5` | Sohyun pushed (`7aeaaff..f8d1690`). Live on thepianobutler.com: Scales tab with the landmark table, E♭ data matches the book (RH 212341231234123, LH 321432132143213), old `?drill=letter-chain` link lands on Note Names with the letter circle and chain, zero console errors. Phase 94-96 also spot-checked live: pixel font loads, locked student link hides the picker. |
| 7 | Follow-up: patterns instead of the finger-4 table | `drills.html` (`ScalePatterns`, `FingerGroups`, `SCALE_PATTERNS`) | Sohyun: the finger-4 table was hard to follow -- "패턴으로 설명해주는게 낫지 않아?". Replaced with five pattern cards: 1 standard (C G D A E), 2 F (RH swaps), 3 B (LH swaps), 4 black-key starts B♭ E♭ A♭ D♭ (thumbs only on white keys; RH thumbs on C and F; one LH shape), 5 G♭/F♯. Finger rows are drawn from `SCALES` (one octave), split at the thumb into group-of-3 / group-of-4 boxes in the keyboard's colours, finger 5 and lead-in notes shown plain, note names under each finger. Viewer box renamed "Where the thumbs and finger 4 go". Babel check 0 errors; Playwright screenshot reviewed on the exact device file; no page errors. Committed, not pushed. |

### Phase 98 Updates (2026-09-23 -- minor scales, harmonic minor first)

Sohyun: add a minor group, and decide how to introduce natural / harmonic / melodic minor --
harmonic minor comes up most, so lead with it.

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Harmonic minor data from the AMEB books | `drills.html` (`MINOR_2OCT`, `MINOR_SCALES`) | Read every key off the Technical Work books: A P.3 (1 octave only; standard shape), E 1.3, D 1.6, B 2.3, G 2.6, F♯ 3.3, C 3.6, C♯ 4.3, F 4.7 (Level 1); G♯ 5.2, B♭ 5.5, D♯ 6.2 (Level 2). 1-octave = first octave of the printed 2-octave fingering (RH finishes on 5 where it would carry on with the thumb, as in Prelim A minor). No thumb on a black key in any key. |
| 2 | Honest limit found and handled | `drills.html` (`MinorViewer`) | Checking the data showed the harmonic fingers do NOT transfer to every other form: F♯ and C♯ melodic (raised 6th) and G♯ natural (lowered 7th) would put a thumb on a black key. The viewer therefore shows finger numbers for natural/melodic only when there is no clash (matches what the books print for E, D, G, C, F, B, F♯/C♯ natural, G♯/B♭/D♯ melodic) and otherwise says "the fingers change for this form -- practise it from your book". |
| 3 | Minor Learn | `drills.html` (`MinorFormsCard`, `MINOR_PATTERNS`, `ScalePatterns mode`, `ScalePath keys/prefix`) | Major/Minor switch at the top of Scales Learn. "Three kinds of minor" on A minor with gold changed notes: natural (relative major's notes), harmonic -- "the one you'll play most" (raised 7th both ways; the 3-semitone F-G♯ step), melodic (raise 6th & 7th going up, natural coming down), then "learn the harmonic fingering first". Five minor patterns: standard (A E D G C), F (RH swaps), B (LH swaps), F♯/C♯/G♯ (one RH shape; C♯/G♯ LH = flat-major LH; F♯ LH starts on 4), B♭/D♯ (both hands start on 2). 36 minor stamp cards (`m:` prefix). Viewer: 12 keys × 3 forms × 1/2 octaves, spelled notes with changed notes in gold (double sharps shown as ♯♯). |
| 4 | Drill | `drills.html` (`SCALE_LEVELS` 5-6) | L5 harmonic minor: which finger; L6 tap the raised 7th (scale dots hidden so the answer isn't given away). |
| 5 | Verification | -- | Babel compile 0 errors; Node data run printed spelled harmonic minors + 1-octave fingers for all 12 and the thumb-on-black check; Playwright on the exact device file: Minor switch, C♯ melodic shows the clash message, C♯ harmonic shows the AMEB line, A natural "same fingers", minor stamps saved as `m:` ids, L5/L6 answer correctly, major pattern labels intact, zero page errors. |
| 6 | Committed, not pushed | see git log | Ready for Sohyun to push. |

### Phase 99 Updates (2026-09-23 -- drills curriculum order, Tones & Semitones, scale step patterns)

Sohyun asked for a curriculum order covering TTSTTTS, intervals (with tones/semitones) and chords,
then approved all three recommendations: (1) reorder chapters, (2) build Tones & Semitones + scale
shape next, (3) chords will show Roman numerals AND letter names (AMEB theory uses numerals).

**Agreed curriculum (main path, all "count the semitones"):** 1 Note Names (+ letter chain) →
2 Tones & Semitones → 3 Scales (shape TTSTTTS, then fingering; minor forms with step patterns) →
4 Key Signatures (derived from the shape) → 5 Intervals (number by letters, then quality by
semitones; major/perfect from the tonic first) → 6 Chords (stacked 3rds; major 4+3, minor 3+4;
I IV V with numerals + letters; inversions/arpeggios; V7). Side track any time: Notes & Rests,
Rhythm Cards, Tempo Race. Intervals and chords are NOT built yet -- check the AMEB theory syllabus
for grade placement when building them.

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Tones & Semitones chapter | `drills.html` (`TONES_DRILL`, `TonesLearn`, `StepExplorer`) | Learn: 4 tips + tap-any-two-keys explorer. Drill: L1 tone or semitone, L2 tap a tone/semitone up/down from a white key (3-octave keyboard), L3 enharmonic other name (incl. E♯/F, B♯/C, C♭/B, F♭/E). |
| 2 | Scale shape | `drills.html` (`STEP_PATTERNS`, `StepStrip`, `MajorShapeCard`) | Major Learn opens with T T S T T T S on C (semitone steps gold) and "why G major needs F♯". Minor forms card shows step strips (natural T S T T S T T, harmonic T S T T S T+S S, melodic up T S T T T T S). Drill L7/L8: build a major / harmonic minor by tapping each note up from the tonic (a wrong key ends the question and shows the scale). Data check: every pattern equals the offsets in `SCALES`/`minorOffsets`. |
| 3 | Key Signatures tip | `drills.html` | "Where the sharps and flats come from" (D major needs F♯ and C♯ to keep the shape). |
| 4 | Picker grouped | `drills.html` (`DRILLS` `track`) | "Step by step" numbered 1-4, then "Rhythm & terms -- any time". |
| 5 | Verification | -- | Babel 0 errors; Node pattern/offset check; Playwright on the exact device file (MD5 matched): grouped chips, explorer E→F = 1 semitone, all Tones levels answer, L7 A major and L8 E harmonic minor built correctly = Correct, a wrong second key ends with the full scale shown, zero page errors. |
| 6 | Committed, not pushed | see git log | |

### Phase 100 Updates (2026-09-23 -- full basics curriculum plan, Time Signatures chapter)

Sohyun: this can be both a curriculum and a site of moving, fun music teaching tools -- put in all
the basics, decide the order (keyboard first or staff first), and add topics one at a time
starting with time signatures.

**Decided order (three tracks, shown grouped in the picker):**
- **Pitch** -- keyboard first (hands-on, instant), then the staff tied straight back to the
  keyboard: 1 Note Names ✓ → 2 **Reading the Staff** (treble/bass clef, lines & spaces, landmark
  notes, ledger lines, grand staff ↔ keyboard) -- the biggest remaining gap → 3 Tones & Semitones ✓
  → 4 Scales ✓ → 5 Key Signatures ✓ → 6 Intervals → 7 Chords (numerals + letters).
- **Rhythm** -- 1 Notes & Rests ✓ → 2 Time Signatures ✓ (this phase) → 3 Rhythm Cards ✓ (later:
  3/4 and 6/8 cards) → ties, dots, triplets as they come up.
- **Reading the music** -- 1 Tempo Race ✓ → Dynamics (pp–ff, cresc./dim.) → Articulation
  (staccato, legato, accent, tenuto) → Signs (repeats, D.C./D.S./Fine, fermata, 8va).
Build next in this order: ~~Reading the Staff~~ (Phase 101), ~~Dynamics & Articulation~~ (Phase 102), Signs, Intervals, Chords.
Check the AMEB theory syllabus for grade placement when building Intervals/Chords.

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Time Signatures chapter | `drills.html` (`TIME_SIGS`, `TSig`, `playTimeSig`, `fillBar`, `TIMESIG_DRILL`) | Learn: top number = beats per bar, bottom = beat note (4 crotchet, 2 minim, 8 quaver); simple 2/4 3/4 4/4 2/2 3/8 and compound 6/8 9/8 12/8, each with "N × beat glyph", a one-line use, and tap-to-hear with the strong beat accented. Drill: L1 meaning, L2 which signature fits a drawn bar (only one of 2/4 3/4 4/4 3/8 fits; dotted quavers left out for readable bars), L3 listen 2/3/4 beats, L4 how many beats you feel (6/8 → 2). |
| 2 | Picker in three tracks | `drills.html` (`DRILLS` `track`) | Pitch / Rhythm / Reading the music, numbered within each. |
| 3 | Verification | -- | Babel 0 errors; 400 rounds per level: answer always present, no duplicate choices, "fits" bars sum exactly and only one signature fits; Playwright on the exact device file: groups render, Learn tap-to-hear, all 4 levels answer; zero page errors. |

### Phase 101 Updates (2026-09-23 -- Reading the Staff chapter)

Next item on the Phase 100 plan. Pitch track is now 1 Note Names → 2 Reading the Staff → 3 Tones &
Semitones → 4 Scales → 5 Key Signatures.

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Staff drawing | `drills.html` (`StaffView`, `dY`, `ledgersFor`, `CLEFS`, `GRAND_GAP`) | Positions as d = octave×7 + letter (middle C = 28); treble lines E4 G4 B4 D5 F5, bass lines G2 B2 D3 F3 A3 (checked in Node). Grand staff draws the bass staff 20px lower so the two read as separate staves; ledger lines computed per staff. Clefs are Noto Music glyphs (already loaded from Google Fonts) -- position calibrated in the sandbox with a fallback font, so **the clef placement needs a look on a real phone**. |
| 2 | Learn | `drills.html` (`StaffLearn`, `StaffExplorer`, `StaffLetters`, `LANDMARKS`) | Tips (two staves one piano; each line/space is the next letter; read from landmarks; ledger lines), an explorer (7 landmark buttons + 3-octave keyboard C3–B5; tapping a white key moves the note), treble and bass lines/spaces drawn with letters (lines black, spaces gold) and the usual rhymes. |
| 3 | Drill | `drills.html` (`STAFF_DRILL`) | L1 treble (D4–G5), L2 bass (F2–B3), L3 both clefs incl. ledger lines (A3–C6 treble, C2–E4 bass), L4 find the exact key (C3–B5). Naming levels accept A–G keys; feedback shows the key. |
| 4 | Verification | -- | Babel 0 errors; Node: line names, middle C = key 12, ledger sets; Playwright on the exact device file: each level answered 10/10 by reading the drawn note's position and pressing/tapping the matching letter/key (so the drawing and the answer agree), explorer tap E4 → "E (E4)", zero page errors. |
| 5 | Follow-up: clef bug + Sohyun's fold idea | `drills.html` (`ClefGlyph`, `FoldStaff`, `LedgerMirror`) | Live check showed the clefs misplaced: the page's `* { font-family }` rule overrides SVG `fontFamily` attributes, so the Noto Music glyphs never loaded. Fixed with inline style + ink measured on a canvas and scaled into a fixed staff box (verified with Noto Music and with a fallback font). Sohyun's decalcomania idea: fold the grand staff at middle C (mirror d → 56−d; treble C↔bass C, high C↔low C, G line↔F line highlighted) with a fold animation (reduced-motion aware), plus "the gap is really one missing line" (treble A with 2 ledger lines = bass top line A). Her rhymes: Every Good Boy Deserves **Fun**; bass lines **Great Big Dragon Flies Away**. Staff drill re-run 10/10 on every level. |
| 6 | Follow-up: middle C + clef story | `drills.html` (`ClefStory`, `FoldStaff`, `LedgerMirror`) | Sohyun asked for middle C to be visible in both diagrams (now a black note on the fold, "its own mirror", and on both the treble-side and bass-side ledger line in the gap diagram) and a clef story, plausible but not childish: the treble clef began as a letter G and grew into a spiral that closes on the second line -- the Queen's home; the bass clef began as an F, the King lives on the fourth line with the two dots as guards above and below. Ties to the fold: G is five notes above middle C, F five below. |

### Phase 102 Updates (2026-09-23 -- Dynamics & Articulation chapter)

Reading-the-music track: 1 Tempo Race → 2 Dynamics & Articulation.

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Learn | `drills.html` (`DYNAMICS`, `CHANGES`, `ARTICS`, `DynLearn`, `ArticBar`, `playDyn/playChange/playArtic`) | pp p mp mf f ff (bold italic, growing size, tap to hear at that volume; "p = piano, f = forte, m = mezzo"), cresc./dim. hairpins, sfz, fp (each playable), and six articulations drawn on a bar of crotchets -- staccato, legato (slur), accent, tenuto, staccatissimo, fermata -- each playable. |
| 2 | Drill | `drills.html` (`DYN_DRILL`) | L1 dynamic → meaning, L2 which is louder, L3 volume-change signs, L4 name the articulation marking, L5 listen: getting louder / softer / staccato / legato. |
| 3 | Verification | -- | Babel 0 errors; 400 rounds per level (answer present, no duplicates); Playwright on the exact device file: Learn plays, all 5 levels answer, zero page errors. |

**Follow-up (2026-09-24): key signature drawing fixed.** Sohyun spotted that key signatures looked wrong. Real data bug: `FLAT_POS` had G♭ and F♭ above the staff (G5, F5) -- standard engraving is G4 (2nd line) and F4 (1st space); the Phase 90 note claiming a PDF match was wrong for these two. Sharps (F5 C5 G5 D5 A4 E5 B4) were correct. Accidentals are now drawn shapes (`SharpShape`, `FlatShape`) centred on their line/space, clefs use the fitted `ClefGlyph`, and the order of sharps/flats is shown on both clefs (bass = same shape a 3rd lower; bass F♭ in the space below the staff). `KeySigStaff` (Scale Fingering) now reuses `KSStaff`. Checked by screenshot, every accidental against its line/space.

### Phase 103 -- Key Signatures: hands-on round (order, place-it, circle of fifths)
Sohyun: flats looked broken; number the accidentals; animate adding them one by one; introduce the circle of fifths; add creative touch-it activities so it sticks.
- `FlatShape` redrawn as one closed, filled bowl on a stem (bowl centred on its line/space) -- no more gap.
- `KSStaff` gains `numbers` (1..n above each accidental, newest in red).
- `OrderBuilder` (sharps and flats): − One off / + Next one / ▶ Play auto-adds every 850 ms; treble/bass toggle; names light up; live "n♯ = X major / y minor". Mnemonic line between them (Father Charles Goes Down And Ends Battle / reversed).
- `PlaceIt`: tap the line/space for sharp/flat #n; a wrong tap shows a red ghost plus "That's E -- try again"; counts misses.
- `CircleOfFifths`: 12 tappable slots, relative minors inside (follow the chosen enharmonic), enharmonic chips (B/C♭, F♯/G♭, D♭/C♯), numbered staff, "Walk the sharps" C→…→C♯ and "Walk the flats" C→…→C♭ animations (sequence verified in Playwright).
- Drill Level 6 "Circle of fifths: next key round" (one step clockwise/anticlockwise; generator fuzzed 300x).

### Phase 104 -- Note Names: hands-on round
Sohyun: give every chapter key-signature-style activities, starting from chapter 1. Four new activities in the Note Names Learn tab, each after the rule it teaches (keys now play a tone when tapped via `playKey`):
- `FindAll`: pick a letter, tap all three on a 3-octave keyboard against the clock; best times per letter in localStorage `pb_findall_v1`; the group tint appears when done.
- `NameReveal`: ▶ Play / + Next key -- letters land on the white keys one by one across two octaves; the restart at A is flagged in red ("After G the letters start again at A!").
- `SharpFlatMover`: tap a white key, push ♭ left / ♯ right; an animated arc shows the move; E♯/B♯/C♭/F♭ explain the white-key landing.
- `LetterWalker` (replaces the static LetterCircle picture): start letter, up/down, 2nd–8ve, Go -- a ring hops round the circle numbering 1, 2, 3... (start counts as 1).
- `TapKeyboard` gains a `names` prop (per-key labels, fade in) and a fill transition. CSS `@keyframes drawArc`.
- Follow-up (Sohyun): counting 2nds..octaves belongs in the Intervals chapter, not here. Tip 5 is now "Up is right, down is left" with `UpDownWalk` (Step down / Step up one white key, arc animation, letter trail, G→A and A→G wraps flagged, "Hide names" mode so the student says the letter first). `LetterWalker` is kept in the file, unused, for the Intervals chapter (plan: interval number by letter-counting first, then quality -- major 6th etc.).
- Follow-up 2 (Sohyun): sharps/flats belong with Tones & Semitones. The Note Names tip about black-key names and `SharpFlatMover` moved to TonesLearn (after StepExplorer); the mover now speaks in semitones ("B♯ is one semitone up -- a white key, the same sound as C") and tapping a black key only plays it. TonesLearn opens with two name cards: Semitone (S) = half step, Tone (T) = whole step; StepExplorer says "1 semitone (half step)" / "2 semitones = 1 tone (whole step)". Note Names drill Level 4 (black keys) still exists -- revisit if Sohyun wants it moved too.

### Phase 105 -- Intervals chapter (pitch track #6)
Sohyun asked for Intervals before Signs. Placement from the 2026 AMEB Manual: Music Craft Prelim = M3/m3, P4, P5, P8 by number; Grade 1 = all diatonic by number; Grade 2 = major/minor 2, 3, 6, 7 + perfect 1, 4, 5, 8 and consonant/dissonant; Grade 3 = inversions + A4/d5 (not built yet). Theory of Music Grade 1 = number above the tonic, Grade 2 = number + quality. Musicianship Grade 1 aural = major vs minor 3rd.
- Model: note = { d, acc } (d = staff diatonic number, middle C 28). Helpers ivMidi/ivName/ivNum/ivQuality/ivBuild/ivLong, playIv (melodic then harmonic). `IntervalStaff` draws a single staff with spread notes, sharps/flats, ledger lines, optional counting "ladder" and tap rows.
- Learn: (1) number -- `IntervalRuler` (tap the staff above a bottom note; red 1-2-3 stairs climb; line/space rule for odd vs even numbers) + `LetterWalker` (moved here from Note Names); (2) quality -- `SemitoneCounter` (bottom note, number, minor/major; "Count the semitones" numbers each key on the keyboard, table of semitone sizes); (3) `MajorScaleIntervals` shortcut (C G D A F B♭ E♭; tonic sounds with each degree, labels M2 M3 P4 P5 M6 M7 P8); (4) `IntervalEar` (all 11 from C, consonant/dissonant, song hooks: Jaws, Happy Birthday, Greensleeves, Oh When the Saints, Here Comes the Bride, Twinkle Twinkle, My Bonnie, Somewhere, Over the Rainbow).
- Drill levels: 1 number treble, 2 number treble+bass, 3 m3/M3/P4/P5/P8, 4 above the tonic in major keys (C G D A E F B♭ E♭ A♭), 5 any of the 11 (treble+bass), 6 build it on the keyboard, 7 by ear (m3/M3/P4/P5/P8). Bottom notes natural (except tonics) so answers need at most one accidental. Generator fuzzed 2000x per level: 0 fallbacks, 0 mismatches.
- `TapKeyboard` `names` now also labels black keys.
- Next here: inversions and A4/d5 (Grade 3), then Chords.

### Phase 106 -- Reading the Staff: hands-on round
Continuing Sohyun's "activities in every chapter, in curriculum order". New in StaffLearn (shared `StaffFrame` = single or grand staff with tappable line/space rows; `GlideNote` animates a notehead between positions; `dMidiKey(d)` maps staff positions to `playKey`):
- `StaffClimb`: step up/down one line/space at a time on the grand staff (C2..C6), note glides, keyboard mirrors it, "on a line / in a space", letter trail; crossing middle C moves between staves. Tapping a white key moves the note there.
- `MnemonicStaff` (replaces the two static StaffLetters pictures): treble/bass x lines/spaces; tap each line/space (or ▶ Play) and the rhyme builds word by word (Every Good Boy Deserves Fun / FACE / Great Big Dragon Flies Away / All Cows Eat Grass).
- `LandmarkHop`: guess a random gold note (A-G); then the nearest landmark appears and a marker hops step by step to the note with letters; running score.
- `WriteTheNote`: a letter is shown, tap where it goes (treble C4-A5 / bass E2-C4); wrong tap = red note + "That's G -- try again"; right = green plus faint copies an octave away; streak counter.
- StaffExplorer kept (landmark chips + keyboard) right before LandmarkHop.

### Phase 107 -- Scales: build it yourself
`ScaleBuilder` (major under MajorShapeCard; harmonic minor under MinorFormsCard): pick a tonic (major C G D A F B♭ E♭ / minor A E D G C B), then press T / S (and T+S for harmonic minor) for each step; correct steps light the key with its spelled name and play it, a wrong step flashes the key it would land on in red ("Not a semitone here"), two misses in a row reveal the pattern. Finish: the spelled scale plus the key-signature link (G major needs F♯ -- that's its key signature) or, for minor, why the raised 7th is written in.

### Phase 108 -- Notes & Rests: hands-on round
Shared helpers: `playItems(items, bpm, onStep)` (tone per note, rests silent, soft beat clicks, step callback), `usePlayer()`, `BeatRow` (each note/rest drawn in a box whose width is proportional to its length, dashed beat lines, a duration bar under each, current item lit while playing).
- `SplitTree` (after the value tree): start with one semibreve; tap a note to split it into two of the next value, or switch to "note ↔ rest"; the bar never changes length; running sum ("2 crotchets + 1 crotchet rest + 2 quavers = 4 beats"); ♪ Play the bar.
- `FillTheBar` (after "A dot adds half again"): 2/4, 3/4, 4/4; palette of semibreve, dotted minim, minim, dotted crotchet, crotchet, quaver and their rests; overfilling shows the extra in red ("Too long -- that makes 6 beats in a 3-beat bar") and removes it; a full bar plays itself; Undo / Play / Clear.

### Phase 109 -- Time Signatures: hands-on round
- `BeatPulse` ("Count along"): 2/4, 3/4, 4/4, 6/8; ▶ Start loops the pulse with lights (strong beat biggest and red, 6/8's second beat medium) and ONE/two/three words; ■ Stop.
- `BarLineBuilder` ("Put in the bar lines" -- the AMEB written task): three bars of 2/4, 3/4 or 4/4 from `fillBar` with no bar lines; tap the gap where each bar is full; a wrong gap flashes red with "that bar only has 1½ beats so far"; final double bar; New line.
- `RegroupQuavers` ("Same notes, different beat"): six quavers beamed 2+2+2 (3/4) or 3+3 (6/8), labelled beat 1/2/3, played with the matching accents.
- `fmtBeats` now says "½ beat" / "1 beat" (singular up to one beat).

### Phase 110 -- Rhythm Cards: make your own card
`RhythmComposer` (end of RhythmLearn): choose Set 1-5 (unlocks the same RCELLS building blocks the 40 cards use), tap blocks to fill one 4/4 bar (progress bar; blocks that would overflow are disabled), the card renders with RhythmCard and shows counts once full; ♪ Play (count-in + rhythm), ↻ Loop / ■ Stop, ↶ Undo, Surprise me (random full bar from the set's blocks).

### Phase 111 -- Tempo Race: metronome and speed changes
- `MetronomeDial`: slider 40-208 bpm, a drawn metronome whose arm swings in time (weight slides down as it gets faster, like a real one), the matching tempo word (`termForBpm` = nearest demo tempo) and its lane colour; ▶ Start/■ Stop clicks; "Tap" measures the user's own tempo from the last taps.
- `SpeedChange`: rit., rall., accel., a tempo -- twelve beats played with the tempo changing, dots spaced by real time light up as they sound.

### Phase 112 -- Dynamics & Articulation: hands-on round
- `DynOrder` ("Line them up"): the six dynamics shuffled; tap softest to loudest (each plays at its volume), bars grow as you go, wrong tap flashes red ("very loud comes later"), slip count.
- `HairpinMaker` ("Draw a hairpin"): pick start and end dynamics; the hairpin draws itself while eight notes ramp in volume; labels crescendo/diminuendo.

### Phase 113 -- Reading the Staff fixes from Sohyun's review
1. Middle C shown in both places: `StaffClimb` draws middle C under the treble staff AND above the bass staff (solid = the one you arrived at -- from above = treble/RH, from below = bass/LH; the other dashed), boxed labels, "same key ↕", and "Middle C" toggles between them. `StaffExplorer` shows both (labels treble / bass) when Middle C is picked.
2. `ClefHome` animation in ClefStory: "♛ Take the Queen home" -- a crown spirals down the treble clef's curl onto the G line and glides to the note, the G line turns gold, G sounds. "♚ Take the King home" -- the crown walks in along the F line to the clef, the two guards (dots) get red rings, F line gold. Dot/curl positions measured from Noto Music (curl centre x~24, dots x~35 at F-line ±4.6).
3. `BoxLabel` (text on a filled box): FoldStaff's "middle C" and "fold" now sit ON the dashed fold line in boxes; LedgerMirror's "middle C" and "A = bass staff top line" labels boxed so lines don't run through them.
4. Open question to Sohyun: ledger lines -- expand inside Reading the Staff or split into its own chapter? (recommended: own chapter, graded by AMEB ledger-line limits).

### Phase 113b -- Queen/King crowns land exactly in the clefs
Sohyun: crowns must sit inside the clef on their line, look different, and the King must pass between his guards. `ClefHome` rewritten: glyph ink measured at 4x (Noto Music as ClefGlyph scales it) -- treble curl's inner hole centre x 21 on the G line; bass dots centred x 34.2 at y 125 / 134 (gap 127.2-132); pocket inside the bass clef on the F line centre x 21. The camera zooms onto the clef (viewBox 70 wide), the `QueenCrown` (tiara, pearls, pink jewel) spirals two turns into the curl and sits on the G line; the `KingCrown` (red cap, square points, cross) walks in along the F line, straight through the gap between the two dots (red rings when he passes), into the clef; then the camera pulls back to a 175-wide view (whole clef + note + letter) with the line gold and the note sounding. Crowns are vertically centred on the line so the King fits the guards' gap.

### Phase 114 -- Lesson steps layout + accidentals
Sohyun: introduce sharp/flat/natural ("accidentals") in Tones & Semitones, and make every chapter's Learn page read as small steps in learning order, clearly set apart.
- New shared layout: `Lesson` (title, intro, a map of numbered coloured step pills -- tap to jump -- and "n of N steps done"), `Step` (big coloured number, "STEP n OF N", title, coloured rail, "Got it ✓" ticks it off, folds it and opens/scrolls to the next; saved per chapter in localStorage `pb_lesson_steps_v1`; tap the header to reopen), `Rule` (key fact: white box with the step's colour on the left; every chapter's local `tip()` now renders a Rule), `.try-box` CSS adds a dark "TRY IT" tag to every hands-on box. `STEP_COLORS` = blue, green, brass, red, purple, teal, orange.
- Steps per chapter: Note Names 4 (black-key map / seven letters / up and down / letter chain), Reading the Staff 6 (two staves two clefs -- ClefStory moved here / line-space / rhymes / landmarks / middle C and ledger lines / write them), Tones 2 (semitones and tones / accidentals), Scales 5 each for major and minor (tabs above the lesson), Key Signatures 6 (order of sharps / order of flats / place them / name the key / circle of fifths / all 15), Intervals 4, Notes & Rests 4, Time Signatures 3, Rhythm Cards 2, Tempo 3, Dynamics 3.
- Accidentals step: `AccidentalCards` (♯ raises, ♭ lowers, ♮ cancels), `SharpFlatMover` gains "♮ natural" (arc back to the plain key), Rules for placement and "lasts until the bar line", `AccidentalBar` (F♯, F still ♯, F♮, | F -- and B♭, A, B still ♭, | B; tap notes or play the bar, keyboard shows the key actually sounding), `NaturalShape` drawn to match SharpShape/FlatShape.

### Phase 115 -- Ledger Lines chapter (pitch track #3, after Reading the Staff)
Sohyun agreed ledger lines need their own chapter with more examples. AMEB placement: Music Craft Prelim = one ledger line below treble (middle C); Grade 1 = one above/below both staves; Grade 2 = up to three; Theory of Music Grade 1 = two.
- Learn (Lesson, 4 steps): "What a ledger line is" (`LedgerClimb`: step off either staff, ledger lines appear, "C -- on ledger line 2 above"); "Ledger lines skip a letter" (`LedgerLandmarks`: the notes ON the 1st-3rd ledger lines -- treble above A C E, below C A F; bass above C E G, below E C A -- played and shown); "Borrowed from the other staff" (`LedgerTwins`: B3 A3 G3 F3 under the treble = bass staff notes, D4 E4 F4 G4 over the bass = treble staff notes, side by side + keyboard; `staffPlace()` names the line/space); "Write them" (`LedgerWrite`: "A above the treble staff" -- tap the right line/space, wrong tap shown red).
- Drill (`LEDGER_DRILL`, reuses StaffQuestion): L1 one ledger line, L2 two, L3 three (both clefs, above and below, incl. the spaces beyond), L4 find the exact key. Generator fuzzed 1000x per level: never exceeds the level's ledger count; keyboard answers always on the 3-octave keyboard.
- `ledgerDesc(clef, d)` describes any position ("in the space just above the staff", "on ledger line 2 below", "above ledger line 1").

### Phase 116 -- Signs chapter (reading track #3)
- Learn (Lesson, 4 steps): Repeat signs, D.C./D.S./Fine/Coda, Ties and slurs, 8va and 8vb.
- `RoadMap` + `RoadStrip`: six maps (Repeat, Repeat part, 1st & 2nd time, D.C. al Fine, D.S. al Fine, D.C. al Coda) drawn with real repeat bar lines/dots, 1./2. brackets, 𝄋, 𝄌, To Coda, Fine and jump words. ▶ Watch: a highlight travels the bars in playing order (each bar has its own pitch so repeats are audible) while the order builds underneath; Your turn: tap the bars in order, a wrong bar flashes with "look at the signs at the end of bar n". Orders hand-written and checked: 12341234 / 123234 / 123124 / 123412 / 1234523 / 12341256.
- `TieOrSlur` (same pitch = tie, different = slur; tie plays one long note, slur two joined notes), `CurvePair` draws stems/curve by the standard rule (stems up + curve under below the middle line, stems down + curve over from it).
- `OttavaDemo`: written C D E F in the treble; as written / 8va / 8vb with the dashed bracket; keyboard shows the keys actually played.
- Drill: L1 what does this sign mean (11 signs; meanings don't contain the sign's name), L2 tie or slur, L3 road map playing order (correct + 3 typical mistakes). Fuzzed 500x per level.
- Still to do in this area: Intervals Grade 3 add-on (inversions, A4/d5), Chords.

### Phase 117 -- Chords chapter (pitch track #8)
AMEB (2026 Manual): Music Craft Prelim = tonic triad I of C/G/F (treble, root); Grade 1 = I (i) and V root position, both staves, grade keys (C G D F B♭, A E D G harmonic minor); Grade 2 = I ii IV V root + 1st inversion, Roman numerals/figured bass; Grade 3 = all inversions, dim and aug. Musicianship Grade 2 aural = major/minor triads. Theory of Music Grade 3 = primary triads + first inversions.
- Model reuses the interval notes {d, acc}: `scaleNotes(key, minor)` (starts G3-F4), `triadOn`, `triadQuality`, `romanFor` (capitals major, small minor, ° dim, + aug), `playChord` (arpeggio then block), `ChordStaff` (stacked semibreve chords, staggered accidentals, labels, highlight).
- Learn (5 steps): `TriadStacker` (root/+3rd/+5th, R-3-5 on the keys, snowman), `MajorMinorFlip` (only the middle note moves; semitone counts), `KeyChords` (a triad on every degree in C G D F B♭ / Am Em Dm Gm harmonic -- verified: major I ii iii IV V vi vii°, harmonic minor i ii° III+ iv V VI vii°), `PrimaryTriads` (I IV V cards with letters and roles, play I-IV-V-I, scale notes light up), `InversionFlip` (root / 1st / 2nd, bottom-note colour, 5/3 a, 6/3 b, 6/4 c).
- Drill: L1 tonic triads (C G F D B♭), L2 I/IV/V in a key (treble or bass), L3 major or minor (seen), L4 by ear, L5 build it (tap 3 keys), L6 root/1st/2nd inversion. Fuzzed 800x per level.

### Phase 118 -- Toolbox: every activity as a stand-alone mini tool
Sohyun's guiding idea: teaching aids cut into mini tools a teacher can pull out mid-lesson. `TOOLS` registers all 47 hands-on activities (id, chapter, title, blurb). New top switch "Chapters | Toolbox"; the Toolbox lists tools grouped by chapter (chapter colours) with search; a tool opens alone (`?tool=<id>`), with "Learn the whole chapter →" and "Copy student link" (`?tool=<id>&lock=1` shows only that tool, header = tool name). `?view=tools` opens the list. All 47 tool URLs load with zero errors. RULE going forward: every new activity must work stand-alone and be added to TOOLS.

### Phase 119 -- Intervals Grade 3 add-on + cadences
- Intervals step 5 "Inversions and the tritone": `IntervalInverter` (bottom note up an octave; numbers add to 9; M↔m, A↔d, P stays) and `TritoneTool` (F-B augmented 4th vs B-F diminished 5th, 6 semitones counted on the keys). Drill L8 "Invert it", L9 "Any interval incl. A4/d5" (`IV_LIST3`). Fuzzed 1500x.
- Chords step 6 "Cadences": `CadencePlayer` -- perfect (authentic) V-I, plagal IV-I, imperfect (half) ?-V, interrupted (deceptive) V-vi, each as a 4-chord phrase in any of the chord keys; `voiceProgression` voices the upper three notes as close as possible to the previous chord over a root bass (C: G C E / A C F / G B D / G C E). Drill L7 "By ear: which cadence?".
- Toolbox now has 50 tools (+ invert-interval, tritone, cadences). Git: `gc.auto` set to 0 in this repo after an auto-gc left undeletable .lock files (removed with delete permission 2026-09-25).

### Phase 120 -- Lesson Path / Toolbox / Practice + beginner stages 1-4 + theory and practice tools
Sohyun's direction (2026-09-25): connect student and piano first, then pulse, then reading (rhythm and notes together); make the site a lesson curriculum, a teaching-aid toolbox and a practice solution. She counts "1 and 2 and".
- Navigation: top switch **Lesson Path | Toolbox | Practice** (replaces Chapters | Toolbox). Lesson Path = `STAGES` (1 Me and the piano; 2 Pulse and rhythm; 3 Reading begins; 4 Five-finger positions; 5 Theory Prelim-G3) with chapter rows, `GRADE_TAGS` pills and ✓ steps-done counts; a chapter opens with "← Lesson Path", the stage name and ‹ › to the previous/next chapter. Practice = `PRACTICE_IDS` tools. URLs: `?view=path|tools|practice`, `?drill=` still opens a chapter, `?tool=` a tool. `DRILLS` reordered by stage (18 chapters).
- New chapters: `first-steps` Me and the Piano (FingerNumbers + `HandPic` game, HighLowGame high/low + loud/soft, KeyHouses small house (2) / big house (3) with roofs drawn over the groups + C D E / F G A B modes, BlackKeySong Hot Cross Buns / Mary Had a Little Lamb on the black keys, watch + your turn; drill finger / high-low / loud-soft / house). `pulse` Pulse & Counting (SteadyBeat heartbeat + tap-along early/late feedback, CountAloud "1 and 2 and" lit as it plays, RhythmComposer; drill beats / which bar). `reading-steps` Steps & Skips (StepSkip, MiniTune C-position tunes incl. Ode to Joy with fingers + counts + your turn; drill up/down/same, step/skip/same, name the next note). `five-finger` Five-Finger Positions (FivePosition C, G, middle C, F positions, both hands, fingers on keys and staff; drill which finger).
- Theory: `DegreeNames` (Scales, new step: tonic ... leading note, hear against the tonic), `Transposer` (Key Signatures, new step: tune in C, degrees shown, transpose to G F D B♭ A E♭, reveal answer).
- Practice tools: PracticeTimer (5-30 min ring + bell), PracticeDice (12 practice tasks), PerfectCounter (3/5/7/10 in a row beads), SightReadCards (fresh 2-bar tune: steps / steps+skips / new positions; counts; check by ear).
- Shared: `MelodyStaff` (real rhythm: crotchet, minim, dotted, quaver flag, semibreve; bar lines, 4/4, fingers, names, "1 and 2 and" counts with held counts in grey) and `playMelody`.
- 65 tools, 18 chapters: every chapter, drill level 1-3 and tool URL loads with zero errors.
- Awaiting Sohyun's review of the new beginner stages before changes.

### Phase 121 -- Piano sound + spoken count option
Sohyun: plain tones can't show articulation, dynamics sound thin; offer a spoken "1 2 3 4" count.
- `blip(..., 'triangle')` (every musical note in drills.html) now plays `pianoNote`: sampled grand piano from `audio/piano/` (22 mp3s, ~600 KB, lazy-loaded on first sound; source tonejs-instruments piano, MIT -- see audio/README.md), nearest sample pitch-shifted, velocity from the old volume with a velocity-dependent low-pass (pp dark, ff bright; offline render check: ff ≈ 6x pp RMS), damper release after the note length (so staccato/legato differ). Synth-piano fallback before samples load / if missing.
- Count: `beatTick()` replaces the beat clicks in the metronome, rhythm cards count-in, Notes & Rests playback, time-signature demos, Count along, Steady beat, Count it (+ "and"), Tempo race clicks. `SoundSettings` row under the top switch: Sound Piano | Simple, Count Click | Voice 1 2 3 4 (localStorage `pb_sound_v1`). Voice = recorded files `audio/count/1..8.mp3, and.mp3` if Sohyun adds them (sample-accurate), else the device speech voice (en-AU preferred), scheduled ~70 ms early.
- Idea for Sohyun: record her own voice counting 1-8 and "and" -> drop into audio/count/.

### Phase 122 -- Musical Terms chapter + Echo the tune
- `terms` chapter (Stage 5, tag G1–G4): `TERMS` = 91 AMEB Theory of Music terms, Grades 1-4, with the Manual's own meanings (string-playing terms left out). `TermCards` (grade + category filter, quiz mode hides meanings, ♪ plays the same 8-note phrase at that speed / volume / touch -- `playTerm`: tempo terms at a bpm, accel./rit./rall./stringendo ramps, a tempo/più/meno mosso sudden changes, cresc./dim./morendo/calando ramps, fp, sfz, staccato/legato/mezzo staccato lengths, rubato). Lesson: one step per grade. Drill: G1, ≤G2, ≤G3, ≤G4 term→meaning, and meaning→term (≤G3); distractors never share the answer's meaning. Fuzzed 600x per level.
- `EchoTune` (Steps & Skips step 3 + Practice): hear a 3/4/5-note tune starting on C in C position, play it back on the keys.
- 19 chapters, 67 tools: all chapter/drill/tool URLs load with zero errors.

### Phase 123 -- Terms: string terms, pronunciation, metronome for speed words, Musicianship lists
Sohyun: string-playing terms are in the exam too; let students hear how to say the Italian; speed words should sound like a metronome.
- Added the 5 Grade 4 string terms (sul ponticello, sul tasto, tremolo, pizzicato, arco; new category Strings) -> 96 terms.
- `PRON` respelling for every term (stressed syllable in capitals, e.g. aht-cheh-leh-RAHN-doh), shown as "say: ..." on each card; tapping it (or "Say it" after a drill answer) speaks the word with the device's Italian voice (`speakTerm`, it-IT; French voice for Main droite/gauche; M.M. read as "Maelzel's metronome").
- `playTerm`: Speed and Changing speed terms now play metronome clicks (steady, ramped, sudden change, rubato); tremolo = rapid repeated note; pizzicato/arco short/long.
- `TermCards` toggle Theory of Music | Musicianship (`MUSICIANSHIP_TERMS`, Grades 1-3 from the Manual's Musicianship section).

### Phase 124 -- three more mini tools (2026-09-26)

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | Relative minor tool | `drills.html` `RelativeMinor`, Key Signatures "Name the key" step + TOOLS `relative-minor` | Pick a key; animated walk down 3 semitones on the keyboard (or up, minor → major), key signature shown, letter check (3 letters → which kind of that letter), and the 6th-note shortcut. Plays the major then minor chord. |
| 2 | Term match (memory pairs) | `TermMatch`, Terms chapter new step "Match them up" + TOOLS `term-match` | Grade 1-4, 4/6/8 pairs; no two pairs share a meaning. Term cards speak themselves (toggle), matched pairs play `playTerm`. |
| 3 | Which touch? / How loud? | `TouchEar`, Dynamics new step "Train your ear" + TOOLS `touch-ear` | Listening game on the sampled piano: 3 or 5 touches (staccato, legato, accent, tenuto, staccatissimo) or p/mf/f and pp-ff with an mf reference button; answer reveals the notation (`ArticBar` / `DynMark`), score + streak. |
| 4 | Stale comment fixed | TERMS | Grade 4 comment no longer says string terms are left out. |
| 5 | Verification | -- | Babel compile in Playwright; all 70 tool URLs and 19 chapters load with zero page errors; screenshots of each new tool checked. Fixed a crash when switching Touch → Loudness with an answer showing (state now reset in the click handler). |
| 6 | Git hygiene | `.git` | Removed stale HEAD.lock / maintenance.lock / tmp_obj files left by background maintenance after e4a5e43; set `maintenance.auto false` (plus `gc.auto 0`). |

### Phase 125 -- timing: taps, metronome, count voice and piano now line up (2026-09-26)

Sohyun's feedback: taps had to be early to count as on time; metronome, spoken count and piano didn't quite line up; and a question about counting "1 2 3 4" first vs "1 and 2 and" from the start.

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | Steady beat rebuilt on the audio clock | `SteadyBeat` | Was `setInterval` (drifts later every beat) + a `click` handler (fires on button *release*, ~100 ms late) + no speaker-latency allowance, so every tap scored late. Now: look-ahead scheduler on `AudioContext` time, `onPointerDown` + space bar, tap compared with scheduled time + `outLatency(ctx)`; hearts light when the sound is heard; a crisp click edge on the heartbeat; last 8 taps shown as dots; verdict from the last 4 taps. Playwright: taps exactly on the heard beat → "Right on the beat!", 180 ms early → "A little early". |
| 2 | Piano samples start on their attack | `onsetOf`, `pianoNote` | mp3 files carry ~27 ms of silence at the front; measured at decode and skipped (`src.start(t, offset)`). |
| 3 | Real recorded count voice, sample-accurate | `audio/count/*.wav`, `sayCount`, `loadCount` | The device speech voice can't be scheduled (100-300 ms random delay) -- that was the main mismatch. Added 9 generated voice files (Kokoro-82M, `af_heart`); `sayCount` lines up each word's vowel (measured with `onsetOf(buf, 0.4)`) with the beat, and cuts the previous word when counts come fast. Loader tries `.wav` then `.mp3`. Offline-render check: click 0 ms, piano +5 ms, voice vowel -6..+3 ms from the beat. |
| 4 | Count it: "1 2 3 4" or "1 and 2 and" | `CountAloud`, Pulse chapter | Toggle, default "1 2 3 4"; Quavers forces "1 and 2 and" (with a one-line why). Step renamed "Count out loud"; chapter intro now says "1 2 3 4 -- and once quavers arrive, 1 and 2 and". Pending Sohyun's call on which default she wants. |
| 5 | Verification | -- | All 70 tool URLs and 19 chapters load with zero page errors. |

### Phase 126 -- "Sit and shape your hands" broken down into four visual steps (2026-09-26)

Sohyun: break the first step down, show it visually -- wrist height, open elbows, knuckle hand shape held while the whole arm moves -- with exercises, and make it systematically checkable.

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | Set up the stool | `SitCheck`, `SeatedFigure`, `sitPose`, `FrontArms`; TOOLS `sit-check` | Side-view figure at an upright piano; Height and Distance sliders + 5 presets (just right / too low / too high / too close / too far). The arm is a 2-joint reach to the keys, so the body really follows the stool. Live checks: feet flat, forearm level with the keys (slope -7..12°), elbows just in front of the body, arms not stretched -- each ✗ says what to change. Front view: elbow-gap slider (squashed / open, a fist's width / chicken wings). |
| 2 | The hand shape | `HandShape`, `HandSide`, `HAND_POSES`; TOOLS `hand-shape` | One finger on a key from the side, drawn tip → nail joint → middle → knuckle → wrist → forearm. Good shape + 5 faults (flat fingers, knuckles collapsed, nail joint caving in, wrist dropped, wrist too high), animated between; knuckle / wrist / tip markers turn red when wrong; each fault has what you see + the fix (pointing to the exercise). |
| 3 | Move with the whole arm | `ArmExercises` + `ExRagDoll`, `ExBridge`, `ExGlide`, `ExWings`, `ExBalloon`, `ExDrop`; TOOLS `arm-moves` (also Practice) | Six looping animations: rag doll, knuckle bridge (fingers 1-5 lift, knuckle line stays), arm glide (top view, same hand shape carried C to C, elbow leads), elbow wings, wrist balloon, arm drop. Steps + "watch for" + rep dots (+1/−1), saved in `pb_arm_ex_v1`. |
| 4 | Posture check | `PostureChecklist`; TOOLS `posture-check` (also Practice) | 17 points in 4 groups (Sitting, Arms, Hands, Moving); tap = ✓, again = "work on it"; progress bar; "Save today's check" keeps the last 8 checks (`pb_posture_v1`) with a mini history bar and the items to work on. |
| 5 | Chapter | `FirstStepsLearn` | Step 1 became 4 steps (Sit at the piano, The hand shape, Move with the whole arm, Posture check); chapter now 8 steps. Lesson "Got it" marks are stored by step index, so earlier marks in this chapter shift by 3 (only affects anyone who had ticked them). |
| 6 | Verification | -- | All 74 tool URLs and 19 chapters load with zero page errors; screenshots of every preset, fault and exercise checked at phone width. |

### Phase 127 -- posture fixes + new Stage 6 "Know your instrument" (2026-09-26)

Sohyun's feedback on Phase 126: (1) wrist should sit a little higher; (2) the knuckle-bridge picture invites lifting fingers -- show it another way; (3) arm glide: body and arm too close, unnatural; (4) purpose/use of the posture checklist unclear. New request: piano info -- Cristofori, clavichord/harpsichord and their effect on Baroque playing (non legato), an era summary (composers later), and pitch in Hz with the piano's range vs other instruments.

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | Wrist higher | `HAND_POSES.good` [80,55,24,-3,-2] | Wrist nearly as high as the knuckles, level with the forearm; text updated; wrist check window adjusted. |
| 2 | Knuckle bridge redrawn | `ExBridge` | Fingertips never leave the keys: one key at a time is pressed to the bottom and held while an arrow shows arm weight arriving through the knuckle; ✓ Right / ✗ Wrong toggle shows the knuckle giving way. Steps + "watch for" rewritten (no lifting). |
| 3 | Arm glide re-laid out | `ExGlide` | Player sits well back (top view: shoulders + head), longer arm, left arm in the lap, elbow label with halo; caption "sitting back -- room for the arm to travel". |
| 4 | Posture check made purposeful | `PostureChecklist`, `POSTURE_LIST` | "How to use it" (when, how, what happens next); every item now maps to the tool/exercise that fixes it -- marking "work on it" shows "→ Practise: … open". |
| 5 | Chapter "The piano's story" | `PianoStoryLearn`, drill `piano-story` | Before the piano: `KeyboardAncestors` (clavichord / harpsichord / piano, animated key mechanism -- tangent, jack+quill, hammer with escapement; "press" slider shows the harpsichord stays the same loudness; clavichord Bebung; synthesized `harpsiNote`, `clavNote`). Non legato: `TouchLengths` (legato / non legato / staccato bars + sound, piano or harpsichord). `PianoTimeline` (1400s → 1700 Cristofori → 1720s survivors → Silbermann/Bach → fortepiano → Érard 1821 → iron frame 1825/1843, Steinway 1859 → 88 keys 1880s → digital). `ErasTimeline` (Baroque / Classical / Romantic / 20th c.: keyboard, traits, "playing it today", representative composers, ♪ a few bars in each style). Drill: 27 fact questions in 3 levels + mixed. |
| 6 | Chapter "Pitch, Hz and range" | `PitchRangeLearn`, drill `pitch-range` | `HzExplorer` (A0-C8 slider, wave drawing, octave-doubling chips, hearing range, piano vs pure tone). `RangeChart` (typical ranges of 23 instruments/voices laid over the 88 keys with an Hz ruler; tap to hear lowest/highest; "Piano through history": Cristofori 1720 C2-C6, Mozart F1-G6, Beethoven's Broadwood C1-C7, modern A0-C8). Drill: octave Hz, which goes lowest, who can play this note. |
| 7 | Stage 6 | `STAGES`, `GRADE_TAGS`, `DRILLS`, TOOLS (+6) | "Know your instrument", tagged General knowledge. Composer pages per era still to come (Sohyun: later). |
| 8 | Verification | -- | All 80 tool URLs and 21 chapters load with zero page errors; generators fuzzed (0 bad questions); screenshots checked. |

### Phase 128 -- new metronome sound, choice of click and voice (2026-09-26)

Sohyun: change the metronome sound -- it sounds shaky ("떨려").

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | Woodblock click | `metroClick`, `noiseBuf`, `beatTick` | Every metronome/count click now goes through `metroClick`: a short band-passed noise burst + a pitched body, like a woodblock (accent 2000 Hz, others 1450 Hz, ~50 ms). The Steady beat's 110 Hz sine "heartbeat" (the most likely source of the buzz on small speakers) and the square-wave clicks are gone. Also routed: `playClicks`, speed-term metronome in `playTerm`, 6/8 weak pulses. |
| 2 | Choice of click | `SoundSettings`, `SOUND.click` | Woodblock (default) / Tick (a short high mechanical tick) / Beep (the old sine beep). Picking one plays four clicks. |
| 3 | Voice count: no click underneath, choice of voice | `beatTick`, `SOUND.voice`, `loadCount`, `reloadCount` | Voice mode no longer layers a click under the spoken number (two sounds a few ms apart can sound like a flam). Three voices: Female (US) = `audio/count/` (af_heart), Female (UK) = `audio/count/emma/`, Male = `audio/count/michael/`; picking one reloads and says "1 2 3 4". |
| 4 | Verification | -- | Offline render: every click style starts exactly on the beat (beep +4 ms); both new voices load (9 words) and line up; 80 tools / 21 chapters load with zero page errors. |

### Phase 129 -- full metronome + "Tap the right beat" game (2026-09-26)

Sohyun: grow the metronome -- split a beat into triplets, choose time signatures in more detail -- and a timing game like "tap on beat N".

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | Metronome rebuilt | `MetronomeDial`, `METERS`, `SUBS`, `meterGrid` (Tempo chapter + TOOLS `metronome`) | Audio-clock look-ahead scheduler (was `setInterval`). Time signatures 2/4 3/4 4/4 5/4 2/2 3/8, compound 6/8 9/8 12/8, irregular 5/8 (2+3, 3+2) and 7/8 (2+2+3, 3+2+2, 2+3+2). Split each beat: beats only / quavers / triplets / semiquavers (compound: dotted beats / quavers / semiquavers). Three click levels (bar / beat / split, via `metroClick` accent 2/1/0). The bar is drawn as dots with counts ("1 trip let", "1 e & a", 6/8 quavers "1-6", 7/8 "1 2 | 1 2 | 1 2 3") lit when heard. ±1/±5 buttons, 30-240, speed unit named (crotchets, dotted crotchets, quavers…), TSig shown. Voice mode speaks beat numbers (and "and" for quavers). |
| 2 | Tap the right beat | `BeatTarget`, `btRound` (Pulse chapter new step 2 + TOOLS `beat-target`, also in Practice) | 1 bar count-in, 2 bars to play; tap only where told. Levels: one beat / two beats / the "and" / silent bars (clicks stop after the count-in). 2/4 3/4 4/4, three speeds. Target circles ringed; each tap flashes green/red; result: hits, extra taps, average early/late ms; perfect-round counter. Scored on the audio clock with speaker latency, pointerdown + space bar. Playwright: exact taps on every level → "Perfect!". |
| 3 | Verification | -- | 81 tools / 21 chapters load with zero page errors. |

### Phase 130 -- 6/8 counted 1 2 3 4 5 6; "8 on the bottom: everything doubles" (2026-09-26)

Sohyun: count 6/8 as 1 2 3 4 5 6, also in the Time Signatures lessons; teach that with the quaver as the beat a crotchet is 2 beats -- the values double.

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | New lesson step "When the quaver is the beat" | `BeatDoubler`, `DOUBLE_ROWS`, `EIGHT_BARS` (Time Signatures step 3 + TOOLS `beat-doubler`) | Rule: 8 on the bottom -> quaver = 1 beat, crotchet 2, dotted crotchet 3, minim 4, dotted minim 6. "4 on the bottom / 8 on the bottom" toggle re-numbers five note cards (½ 1 1½ 2 3 -> 1 2 3 4 6, "× 2 -- everything doubles"). Then four 6/8 bars counted 1-6 (bold = note starts, grey = held), played with the count lit (voice mode says 1-6). |
| 2 | 6/8 counted in quavers everywhere | `TIME_SIGS` text, `BeatPulse` (1 2 3 4 5 6, voice), `RegroupQuavers` ("1 2 3 · 4 5 6"), `TimeSigLearn` rows ("6 × quaver beats, in groups of 3") and Compound step text (1 and 4 strongest; groups of three = dotted crotchets = compound duple when fast) | |
| 3 | Drill | `TIMESIG_LEVELS`, `genTimeSigQuestion`, `TimeSigQuestion` | Meaning: 6/8 = "6 quaver beats". New level 4 "In 8 time, how many beats is it?" (3/8, 6/8, 9/8, 12/8 × quaver/crotchet/dotted crotchet/minim/dotted minim). Level 5 is now "Simple or compound?" (simple/compound × duple/triple/quadruple). |
| 4 | Metronome | `meterGrid` (cmode), `MetronomeDial` | 6/8, 9/8, 12/8 default to "Every quaver: 1 2 3 4 5 6" (speed in quavers, 1 and 4 accented, split into semiquavers optional); "In dotted crotchets (fast)" keeps the old behaviour. |
| 5 | Tap the right beat | `BeatTarget` | 6/8 option: six quaver beats counted 1-6 (the "and" level hidden). |
| 6 | Verification | -- | 82 tools / 21 chapters load with zero page errors; time-signature generators fuzzed, 0 bad questions. |

### Phase 131 -- Toolbox reorganised: by skill, filters, "My student…", student kits (2026-09-26)

Sohyun: tools should be grab-and-go; chapter names like "Me and the piano" don't say "posture"; every student is different, so what categories?

Decision (Claude): three ways in, because a teacher arrives at the Toolbox with three different questions -- "what area?", "what's wrong with this student?", "what does THIS student need?".

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | 12 skill categories instead of chapters | `TOOL_CATS`, `TOOL_META` (every tool: category, level range, kinds) | Posture & hands · Finding notes on the keys · Reading notes · Pulse & counting · Rhythm & note values · Touch & expression · Ear & listening · Scales & keys · Intervals & chords · Signs & terms · Practice helpers · About music. Each has a one-line "when" hint and a colour; colour jump-chips at the top scroll to a category. Chapters (Lesson Path) are unchanged -- the Toolbox no longer mirrors them. |
| 2 | Filters | `Toolbox` | Level (Beginner / Preliminary / Grade 1–2 / Grade 3–4, by range) and kind (Show & explain / Student does it / Listening / Written theory / Home practice); search now also matches category names and hints; count + Clear filters. Cards show level and ♪ / home tags. |
| 3 | "My student…" problem finder | `PROBLEMS` (18) | e.g. "…flat fingers or collapsing knuckles" -> hand shape, arm exercises, posture check; "…counts up from C to read every note" -> landmarks, hop, rhymes, climb; "…is confused by 6/8"; "…plays everything at one volume"; "…has a theory exam coming"; "…doesn't practise at home". |
| 4 | Student kits | `loadKits`/`saveKits` (`pb_kits_v1`), `KitView`, App `view=kit` (`?kit=a,b,c&kn=Name`) | ☆ on any tool adds it to the selected kit ("+ New kit", named per student). Open the kit in the lesson, or "Copy student link" -> the student sees only their tools (locked, header = kit name, ← Kit back button). |
| 5 | Clearer titles | TOOLS | Parenthetical hints where a title was cryptic: (black keys), (clefs), (grand staff), (perfect reps), (copy by ear), (repeats, D.C., D.S.), (count an interval), (intervals), (speed changes), (time signatures), (note values). ToolView header now shows the category. |
| 6 | Verification | -- | All 82 tools have metadata; problem finder ids valid; kit create/star/open/locked student link/back tested in Playwright; 82 tools / 21 chapters load with zero page errors. |

### Phase 132 -- Lesson plan by strands (no fixed order) + teacher / student views (2026-09-26)

Sohyun: in the first lessons milestones 1-4 all go in together, a little at a time -- crotchets, posture and hand shape, note names, or the black-key groups first. And a link shows everything; teacher and student views should be separate.

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | Teacher "Lesson plan" | `PlanView`, `STRANDS`, `SKILLS` (36), `START_MIXES`, `EXAM_LADDER` | Five strands side by side: Body & hands, Keys & note names, Pulse & rhythm, Ear & expression, Reading -- ordered small "can do" steps inside each, no order between them. Per student (students = the Toolbox kits, now with `done`): tick what they can do, NEXT tag on the first gap in each strand. "A first mix for…" presets (Young 5-7, Beginner 8-12, Teen/adult, Transfer, Exam) mark START steps and fill "Today's mix" -> open those tools now, or add them to the student's kit. Each step links its tools. Exam ladder (Prelim / G1-2 / G3-4 chapters), Anytime (piano story, pitch), "All chapters" link. |
| 2 | Chapters regrouped by topic, not stages | `STAGES` | Piano basics · Rhythm & counting · Reading music · Sound, signs & terms · Theory: scales, keys & chords · Know your instrument. "Stage n" numbering removed. `first-steps` renamed "Posture, Hands & Black Keys". |
| 3 | Teacher / student views | `initialMode`, `UI_TEACHER`, `TeacherOnly`, App | Student view is the default: tabs Learn + Practice only; no Toolbox, kits, plan, share buttons or teacher notes (e.g. Posture check "How to use it"). Teacher view: `?teacher=1` once (remembered on that device; `?teacher=0` turns it off), tabs Lesson plan + Toolbox + Practice, "See the student view" preview with a back banner. Student links (lock=1) always show the student view. Not a password lock -- keeps the student's screen clean. |
| 4 | Verification | -- | Playwright: student tabs = Learn/Practice; teacher plan: add student, preset, ticks, today's mix -> tools, all chapters -> chapter -> back, tool -> "← Lesson plan", student preview; 82 tools / 21 chapters load with zero page errors. |

Teacher link for Sohyun: https://thepianobutler.com/drills.html?teacher=1 (bookmark once per device).

### Phase 133 -- Students tab: add, name, edit, notes, delete (2026-09-26)

Sohyun: students need their own section -- write their names, edit or delete them. (Her screenshot showed "Student 1 / Student 2": browser prompt() is blocked inside the preview, so names fell back to defaults.)

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | Students tab (teacher view) | `StudentsView`, App `view=students`, tabs now Plan · Students · Toolbox · Practice | Add a student (name, "starts as" group = one of the first mixes, notes), per-student card: group + start date, notes, progress bar coloured by strand (x/36 steps), kit size; Lesson plan (opens the plan on that student), Open kit, Student link, Edit (inline form), Delete (inline two-step confirm). |
| 2 | No more prompt()/confirm() | `AddName` inline field used in Plan and Toolbox; Toolbox "Delete" replaced by "Manage students" | Works inside embedded previews and on phones. |
| 3 | One selected student everywhere | `WHO_KEY` (`pb_who_v1`), `loadWho`/`saveWho`, student ids (`newStudentObj`; old kits get ids on load) | Plan, Toolbox and Students share the current student; choosing a student in the Plan sets its first mix from the student's group; the student's notes show under the picker. |
| 4 | Verification | -- | Playwright: add two students with group and notes, edit a name, delete with confirm/cancel, open plan for a student, inline add in the plan, kits list in the Toolbox; 82 tools / 21 chapters load with zero page errors. |

### Phase 134 -- readability pass: bigger text, stronger contrast, less clutter (2026-09-26)

Sohyun: everything is small and hard to take in at a glance -- make the important things stand out.

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | Font floor raised everywhere | all inline `fontSize` in JSX (511 values) | 9.5→11, 10→11.5, 10.5→12, 11→12, 11.5→12.5, 12→13, 12.5→13.5, 13→14, 13.5→14.5, 14→15 (15+ unchanged; pixel-game sizes 8/9 and SVG text untouched). Tool titles (`actTitle`) 17px/900, tool notes (`actNote`) 14px darker; tool boxes get more padding. |
| 2 | Contrast | CSS | `--muted` #a49b8f -> #7a7064 (grey text was ~2.6:1, now ~4.8:1); inactive chips #5a5248; ghost buttons 14px/800 #4a4239; body 16px. |
| 3 | Wider column, bigger on desktop | `.pb-main` | Column 480 -> 600px; at 900px+ the column is scaled ×1.12 (`zoom`) so the iMac view isn't tiny. |
| 4 | Less on screen | `SoundSettings`, header | Sound settings fold into one line ("♪ Sound: Piano · Woodblock click -- change"), opening a panel with Done. Header compact and aligned with the column: "← Piano Butler", title, and in teacher view a small "TEACHER VIEW · Student view" on the right. Plan, Toolbox and beat-game intros shortened. |
| 5 | Verification | -- | Screens checked at phone and desktop width (learn, plan, students, toolbox, metronome, beat game, chapter, drill, hand shape); student-management test; 82 tools / 21 chapters load with zero page errors. |

### Phase 135 -- scale finder + fingering display fix, visible tap targets, book plan (2026-09-26)

Sohyun: (1) every scale should be searchable; in B-flat major the RH starting 2 isn't part of the pattern so it should look plain, and black keys tinted blue/green hide that e.g. F# starts on three black keys -- double-check every scale's numbers; (2) activities like ledger-line writing give no guide where to tap -- audit all activities so the purpose and the action are clear; (3) plan the course as printable PDFs / a book series, online + offline.

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | Scale finder | `ScaleFinder`, `parseScaleQuery`, `PENDING_SCALE`; TOOLS `scale-finder`; Scales chapter step "Look up any scale"; Toolbox search | Type "bb", "B flat", "e flat major", "f#m", "c minor" (or tap a key): key signature, notes (raised 7th for harmonic minor), both hands on the keyboard (1/2 octaves), legend, hear it up and down. Typing a scale in the Toolbox search shows a direct "E♭ major scale ›" card. |
| 2 | Fingering display | `segmentsStartAt1`, `ScaleKeyboard` | RH notes before the first thumb (Bb/Eb start on 2, Ab/Db on 2-3, F# on 2-3-4) are a lead-in: uncoloured. Black keys always stay black; their group shows as a coloured outline + stripe, number in white -- runs of black keys are visible again. Applies to every scale keyboard (finder, fingering drill, minor viewer). |
| 3 | Fingering audit | SCALES, MINOR_2OCT | Programmatic check of all 15 majors + 12 harmonic minors, 1 and 2 octaves: array lengths match, no thumb on a black key, no finger 5 mid-scale -- all pass. Compared with standard fingerings: all majors match. Two points flagged for Sohyun to confirm against her books, **both closed 2026-09-27**: F# major 1-octave RH 234/123/12, LH 4321/321/2 -- confirmed correct exactly as coded, no change; G# harmonic minor 1-octave LH corrected to 321/4321/2 (top note finger 2, not the mechanical carry-over 3) -- see Phase 137. |
| 4 | Visible tap targets | `StaffFrame` (`guideX`), `LedgerWrite`, `WriteTheNote`, `PlaceIt` | Every tappable line/space shows a small dot; ledger positions show dotted ledger lines; a ghost note (or ghost sharp/flat) follows the pointer. Ledger writing got a purpose line and a step-by-step hint ("count line, space, line… then tap where F goes"). Place-it hit area widened. |
| 5 | Activity audit | all 83 tools | Screenshot sheet review of every tool at phone width; remaining tools already state purpose + action. |
| 6 | Book plan | Claude Doc "Piano Butler Books: Print & Online Plan" | 7-book series (Me and the Piano, Reading Begins, Hands on the Move, Theory Ladder Prelim-G1 and G2-4, Teacher Guide, Know Your Instrument), TOCs mapped to step codes, spread design with QR to tools, online/offline use, production (print view -> PDF builder), phased plan. |

Phase 136 -- filling the theory gaps (book plan: "fill everything in first"). Five new stand-alone tools, each in TOOLS + TOOL_META and in its chapter's Learn:
- `count-more` (CountHarder, Note values chapter): dotted crotchet+quaver, semiquavers "1 e & a", quaver+2 semis, dotted quaver+semi, triplets "1-trip-let", syncopation. New `BeamRow` renderer (beams, secondary beams, triplet 3, dots) with a time-aligned count row; play highlights note and syllable.
- `grouping` (GroupingGame, Time signatures): "which bar is beamed right?" for 2/4, 3/4, 4/4 (never across the middle), 6/8 (threes), with the rule after each answer.
- `ornaments` (Signs): trill, upper/lower mordent, turn, acciaccatura, appoggiatura -- written vs played staff, play plain and ornamented.
- `pedal` (PedalDemo, Dynamics): no pedal / held (blur) / legato pedalling, bracket with notches, Ped. and star, una corda / tre corde / sostenuto.
- `chromatic` (ChromaticScale, Tones): sharps up, flats down, RH/LH fingering (3 on black, 2 on F&C RH / E&B LH, lowest note thumb), start on C-A, tap any key for all its enharmonic names incl. double sharps/flats.
Regression: 88 tools / 21 drills, no errors.

Phase 137 -- fingering corrections from Sohyun's books, staff basics, anacrusis (book-plan gap fill continues). Regression: 91 tools / 21 drills, no errors.
- Fingering fixes (both confirmed by Sohyun directly, 2026-09-27): F# major 1-octave (RH 234/123/12, LH 4321/321/2) checked against the already-coded data -- exact match, no change needed, closes the Phase 97 open question. G# harmonic minor 1-octave LH corrected to 321/4321/2 (`MINOR_SCALES['G#'].octaves[1].LH` overridden after the generic 2-octave-derived build; the 2-octave fingering is unchanged).
- `staff-basics` (StaffBasics, new first step of the Staff chapter): the one explanation the site never actually gave -- 5 lines + 4 spaces, counted bottom-up, notes sit on a line or in a space never between. Tap-to-hear on both.
- `anacrusis` (AnacrusisDemo, Rhythm chapter): pickup/upbeat bars -- three worked examples (3/4, 4/4, 2/4) showing the incomplete first bar and the shortened last bar adding up to one full bar, with a bracket highlight and play-through.
- `minor-forms`: the existing "Three kinds of minor" (natural/harmonic/melodic) content was Learn-only -- registered it as its own stand-alone Toolbox tool too, per the standing "every activity in TOOLS" rule.
- Book-plan doc: corrected the Content Coverage table -- melodic minor, scale degree names, transposition and chord inversions were already built (Phase 98/103/108ish) and wrongly listed as missing; only anacrusis and the staff explanation were real gaps, both closed this phase. Student books confirmed staying at 3 thin volumes (Sohyun answered the doc comment).

Phase 138 -- two teacher-reported gaps, fixed live. Regression: 92 tools / 21 drills, no errors.
- Scale finder: the black-key-root chip row showed both spellings for F#/Gb, C#/Db and B/Cb, but only "Ab" for the G#/Ab pitch class (major mode) and only "G#m" for it in minor mode -- looked broken by comparison, flagged by Sohyun directly. There genuinely is no separate "G# major" or "Ab minor" scale to add (both would need an 8-sharp/7-flat signature nobody uses), so the fix is a label, not new data: that one chip now reads "A♭ · G♯" (major) / "G♯m · A♭m" (minor), `scaleChipLabel()`. The other 8 black-key-root chips are unchanged.
- `clef-basics` (ClefBasics, new -- first in the Staff chapter's "Two staves, two clefs" step, and its own Toolbox tool): what treble and bass clef actually mean in practice -- two staves because the piano's range doesn't fit one, treble = higher notes/usually right hand, bass = lower notes/usually left hand, grand staff joined at middle C, tap to hear either register. The existing Queen/King naming story (ClefStory) was real content but was standing in as the ONLY clef explanation; it's now clearly framed as "by the way, why they're called that" underneath this, per Sohyun's note that the practical explanation was missing and the Queen/King bit is secondary.
- Verification note: the first clef-basics layout had the bass clef's dots colliding with the middle-C marker (both drawn near the same x) -- caught on the screenshot pass before committing, moved the middle-C notehead to its own ledger position clear of both clefs.

Phase 139 -- next two items off the book-plan Content Coverage table. Regression: 94 tools / 21 drills, no errors.
- `flash-cards` (FlashCards, Staff chapter, after Landmark Hop): fast note-ID drill with no scaffolding -- no landmark to count from, no ledger lines, just the letter as fast as it's recognised, with a running streak/best-streak and rolling average response time. Framed explicitly as the next stage after Landmark Hop ("from reasoning to recognition").
- `grace-write` (GraceWrite, Signs chapter, after Ornaments): the missing write-it-yourself half of the ornaments tool (Phase 136 only showed written vs played) -- tap where the small grace note goes, acciaccatura (with slash) or appoggiatura, checked against the target.
- Verified live: flash-cards' right/wrong colouring and streak counter, and grace-write's tap-then-check flow (including its wrong-answer state), both screenshotted mid-interaction, not just at rest.

Phase 140 -- rest grouping and duplets, next off the Content Coverage table. Regression: 96 tools / 21 drills, no errors.
- `rest-grouping` (RestGrouping, Note values chapter, after Fill the bar): the one universally-taught rest-writing rule -- a single rest must never span across the middle of a 4/4 bar (hide beat 3) -- shown as a right/wrong pair of identical-sounding bars, both playable, with the point made explicit that this is a writing convention only (rests are silent either way). Deliberately narrow in scope: only the one rule every syllabus agrees on, not a fabricated exhaustive rest-grouping ruleset -- broader rest-grouping conventions vary enough by source that they need Sohyun's books before being asserted as quiz answers.
- `duplets` (DupletDemo, Time signatures chapter, after Grouping notes/GroupingGame): 2 equal notes in the time of 3 in compound time, the mirror of a triplet -- toggle between the normal 3-quaver beat and the bracketed "2" duplet, both playable so the timing difference is audible, not just visual.
- `BeamRow` (the shared beamed-notation renderer from Phase 136) extended: a tuplet bracket can now show "2" (`dup: true`) as well as "3" (`tri: true`), and a `noDot: true` flag on an event suppresses the automatic augmentation-dot the renderer would otherwise draw for a q=1.5 duration -- needed because a duplet's notes are an untied odd duration, not a dotted note.

Phase 141 -- complete-the-melody ending, next off the Content Coverage table. Regression: 97 tools / 21 drills, no errors.
- `complete-melody` (CompleteMelody, Reading steps chapter, after Echo the tune): a short scale-shaped tune (C, G, or F major) climbs up and back down but stops one note short of home -- three candidate endings, all playable, so the resolution is heard, not just read. Correct answer is always the tonic ("settles -- home"); wrong answers are a step-short-of-home (still wants to fall) and a leap that breaks the stepwise shape. Verified live via screenshots: at-rest render (ghost end-note + C/E/A buttons), wrong-answer path (red colouring on the final note, "Listen again" explanation, no Next button), correct-answer path (green colouring, "Yes --" explanation, "Next tune ->" button appears).

Phase 142 -- Alto clef + Print/PDF worksheets, closing out the Content Coverage table's two remaining items. Regression: 98 tools / 21 drills, no errors.
- `alto-clef` (AltoClef, Staff chapter, after Clef Basics; also its own Toolbox tool): a third clef, always centred on middle C (what viola reads) -- geometric fact, not AMEB-specific data, so no PDF check needed. Added `alto: { lines: [24,26,28,30,32], low: 24, high: 32 }` to `CLEFS` and a matching `CLEF_GLYPH` entry (Noto Music C-clef glyph 𝄡); `StaffFrame`'s clef-specific line-bounds logic (previously only handled 'bass'/'treble', silently defaulting to treble's bounds for anything else) fixed to also handle 'alto' explicitly. `StaffView` needed zero changes -- it was already fully generic across any `CLEFS` key. New "A third clef" step added to `StaffLearn`'s Lesson.
- Print / PDF worksheets (`?print=1&drill=<id>&level=<n>&n=<count>`): reuses the browser's own Print dialog ("Save as PDF") rather than adding a jsPDF dependency -- deliberately lower-risk, and each worksheet renders every question through the concept's own `Question` component (locked, unanswered), so a worksheet always matches what the live drill actually asks, not a separately-maintained copy. `PrintLink` (a small "🖨 Print worksheet" link next to the existing Share link, teacher view only) and `PrintWorksheet` (the full printable page: header + date, Name/Score blanks, N numbered questions, a bottom Answer Key grid from `concept.answerLabel(q)`, and a graceful "no printable worksheet for this activity yet" fallback for any future non-concept, render-based drill) added. `useMemo` added to the React hooks import for this. A `Root()` wrapper component now checks `?print=1` before ever rendering `<App/>` -- chosen specifically over an early-return inside `App()` itself, which would have called `useState` conditionally and violated React's Rules of Hooks; `Root()` means `App()`'s hooks are never invoked at all in print mode, avoiding the risk entirely (self-caught during this phase, not a live bug).
- Verification: `test48.js` (98 tools / 21 drills via `?tool=`/`?drill=` URLs) passed both times, but doesn't exercise `?print=1` at all -- separately screenshot-tested the print path directly: a keyboard-tap-based concept (`note-names`, Level 2, 6 questions) rendered correctly locked/unanswered with no crash; a staff-notation-based concept (`intervals`, Level 1, 4 questions) also rendered correctly; and an invalid/unknown `drill` id correctly showed the "no printable worksheet" fallback instead of erroring. All three via real headless-Chromium screenshots, not just a syntax check.

Phase 143 -- Lesson plan: branching-pace content + glanceable layout. Sohyun described a real first-lesson pattern (young/slow students: posture -> black-key groups -> if still slow, a black-key song -> crotchet/minim rhythm, done; quick learners: black-key groups -> also the white keys around them -> rhythm covering semibreve/minim/crotchet together) and said the Lesson Path screen felt scattered and forced scrolling to see all 5 strand categories. Asked her to prioritize: she chose content first, then layout (deferred a third option -- a live branching-decision engine that would auto-suggest the next step based on "fast/slow" taps -- for a later phase).
- `black-white-neighbours` (BlackWhiteNeighbours, First Steps chapter step 9 "Ready for more? The white neighbours", also its own Toolbox tool): the "quick learner" branch off the black-key houses -- an original 12-note walk up and back down the big house (F#/G#/A#) touching the white key right after each black key, watch-then-your-turn like the existing black-key songs. Deliberately an original pattern, not a named tune, so nothing is reproduced. New `k2b` SKILLS entry ("(quick learners) the white key beside each black one") added to the Keys & note names strand, available for a teacher to tick manually -- not yet auto-suggested by pace, since the branching-logic engine itself was deferred.
- `PlanView` (Lesson plan) rebuilt around a persistent overview row: all 5 strands shown at once as small tappable chips (color, done-count, name) so every category is visible without scrolling, instead of 5 fully-expanded cards stacked vertically. Only one strand's full step list is open at a time (accordion) -- tapping a different strand's chip swaps it instantly, and a "Next in <strand>: <step>" line updates right under the overview row so the very next thing to do is visible without opening anything. Defaults to the strand with the current student's next incomplete step (both on load and when switching students via the STUDENT chip row), so returning to a student's plan lands somewhere useful rather than always on strand 1.
- Verification: Babel-compiled the app-jsx script (@babel/standalone, matching the page's own in-browser compile) + `new Function()` on the output -- 0 errors. Live-tested in headless Chromium: the new tool's Watch/Your-turn flow (correct-key taps advance and mark green, matching the existing BlackKeySong pattern); the new Lesson step renders in the First Steps chapter in the right position; the Lesson plan overview row renders all 5 strands with no scroll needed at phone width; clicking a different strand chip swaps the open accordion section and updates the "Next in..." line; adding a student and ticking updates the overview counts live.
- Not yet: the branching decision engine (real-time "fast/slow" -> different next-step suggestion) Sohyun deprioritized this session -- next candidate for a future phase once she's seen this round live.

Phase 144 -- Notes & Rests: rest content deepened, name correspondence, whole-bar rest, matching tool. Sohyun's request (verbatim): "참 rest에 관해서도 내용 보충해줘 그리고 음이름이랑 rest 이름이 같으니까 외우기 쉽게 semibreve, whole bar rest의 용도도 따로 설명해주고 거기에 맞게 음이름이랑 매칭하는 것도 만들면 좋겠다" -- more rest content, explicitly teach that note names and rest names are the same (easier to memorise), explain the semibreve/whole-bar-rest usage separately, and build a matching activity pairing note names to rest names.
- `NoteRestNaming` (new Learn step "Same name for the note and the rest", right after "The note-value tree"): the existing `nvItem` data already ties a note and its rest together by a shared `v.id` root -- this makes that fact explicit and playable. Each of the 5 note values shown as a note-glyph/rest-glyph pair with "same name" between them; tapping the note plays it, tapping the rest plays silence for the same length (a click marks where it ends) so the equivalence is heard, not just read.
- `WholeBarRest` (new Learn step "The whole-bar rest", after "Writing rests correctly"): explains the convention distinct from the rest's normal literal 4-beat duration -- a semibreve rest is also used to mean "rest this whole bar," whatever the bar actually holds. Shown concretely across three time signatures (4/4 = 4 beats, 3/4 = 3 beats, 2/4 = 2 beats), each with a ♪ Count it button so the different real lengths behind the same symbol are audible, plus a closing line clarifying a semibreve rest away from a whole empty bar still means its literal 4 beats.
- `NoteRestMatch` (new Learn step "Match note names to rest names", after the whole-bar-rest step): a memory-pairs matching game adapted from the Phase 124 `TermMatch` pattern -- cards are drawn from `NOTE_VALUES` (3/4/5 pairs, selectable), one card per pair shows the note glyph, the other the rest glyph, matched by shared name; a correct match plays the note's pitch.
- All three registered as stand-alone tools in `TOOLS` (+ `TOOL_META`, category `rhythm`) per the Phase 118 rule: `note-rest-naming`, `whole-bar-rest`, `note-rest-match` -- each opens independently via `?tool=<id>`.
- Verification: Babel-compiled the `#app-jsx` script (`@babel/standalone` 7.23.3, pinned to match the page's own in-browser CDN version) + `new Function()` on the output -- 0 errors. Live Playwright test in headless Chromium (React 18.2.0 / ReactDOM 18.2.0 / Babel-standalone 7.23.3 via local npm copies, served locally since cdnjs is blocked from this sandbox): all three new Lesson steps render in the Notes & Rests chapter (now 9 steps) with correct text and no page errors; interacted with each -- tapped a note/rest pair in the naming step, played a "Count it" bar in the whole-bar-rest step, and flipped two cards in the matching game -- zero console/page errors throughout; each of the three `?tool=<id>` URLs also loads standalone with zero errors, confirmed separately.

Phase 145 -- Korean localization: i18n infrastructure + language toggle + Notes & Rests chapter translated. Sohyun's request (verbatim): "이거 혹시 한국어 번역으로도 볼 수 있을까? 언어 선택 있으면 좋을 듯 일단 엄마한테 보여줄거라, 엄마도 한국에서 학원을 해서 엄마한테 써보라고 해볼거거든" -- a Korean translation option / language selector, ahead of showing the app to her mother (who runs a piano academy in Korea). Given the huge scope (drills.html is 800KB+, 90+ tools, 21+ chapters, zero prior i18n), escalated via `AskUserQuestion` with three options (translate one chapter now + infra / UI chrome only / everything). Sohyun's explicit choice: "전체 다 번역 (시간이 걸려도 괜찮음)" -- translate everything, accepting it as a multi-session effort. This phase is the first installment.
- i18n architecture: a module-level `LANG` variable (persisted to `localStorage['pb_lang_v1']`) and a `t(en, ko)` helper, mirroring the existing `UI_TEACHER` global-mutable-variable pattern already used in this codebase. `App()` holds `const [lang, setLang] = useState(LANG); LANG = lang;` (written once per render, same pattern as `UI_TEACHER = T;`) -- because `App()` re-renders its entire descendant tree on any state change (no component in this file is memoized), flipping `lang` cascades a full re-render and every `t()` call anywhere in the tree picks up the new value with no prop-drilling needed.
- Language toggle: a small "한국어"/"EN" chip added to the header next to the existing "← Piano Butler" link, calls `toggleLang()` which flips `lang` and persists it.
- Translated this phase: the header (back link, page title fallback "Practice Drills", TEACHER VIEW/Student view badge), the top nav tabs (Plan/Students/Toolbox/Practice and Learn/Practice), the "← Back"/"← Learn" back button, the shared `Lesson`/`Step` chrome used by every chapter ("Step n of N", "Got it ✓"/"Done ✓", "n of N steps done", the default "Start the drill →" label), `SoundSettings`' compact summary line and its expanded panel, and the full Notes & Rests chapter (Lesson title/intro, all 9 step titles, the note-value tree row labels, the dotted-notes box, the fill-the-bar caption, and the three Phase 144 components `NoteRestNaming`/`WholeBarRest`/`NoteRestMatch` in full).
- Not yet translated (flagged honestly, not silently skipped): the ~90 individual tool components' own internal text and the ~20 other chapters' Learn content/drill questions are still English-only -- older sub-widgets reused inside the Notes & Rests chapter itself (`SplitTree`, `FillTheBar`, `RestGrouping`) also still show English body copy, since they're shared components used across many chapters and translating them is separate follow-up work, not part of this pass.
- Verification: Babel-compiled the `#app-jsx` script (`@babel/standalone` 7.23.3, pinned to match the page's own in-browser CDN version) + `new Function()` on the output -- 0 errors. Live Playwright test in headless Chromium (React 18.2.0 / ReactDOM 18.2.0 / Babel-standalone 7.23.3 via local npm copies, served locally since cdnjs is blocked from this sandbox): loaded the Notes & Rests chapter, clicked the language toggle, confirmed the header, nav, and all 9 step titles + body text switched to Korean correctly (screenshot reviewed), confirmed the toggle button itself flips between "한국어"/"EN", zero console/page errors (aside from expected blocked-external-domain noise).

Phase 146 -- Korean localization continued: First Steps + Note Names chapters, LANG/t() moved to fix a real bug. Sohyun's direction: "일단 기본적으로 배워야하는 것부터 차근차근 해줘 음이름 리듬 자세 등등 너가 우선순위정해서 알려주고 진행해" -- do the basics first (note names, rhythm, posture...), Claude to set the priority order and proceed. Proposed and started on this order: (1) Posture/Hands/Black keys, (2) Note Names, (3) Pulse & Counting, (4) Notes & Rests [done, Phase 145], (5) Time Signatures, (6) Rhythm Cards, (7) Reading the Staff, (8) Five-Finger Positions, then theory chapters.
- **Real bug caught and fixed before it shipped**: an early attempt to translate `FS_LEVELS`' level labels (a module-level `const` array, evaluated once when the script first loads, not inside a component render) called `t()` at that top-level evaluation point -- but `LANG`/`t()` were declared much later in the file (near `UI_TEACHER`, past line 11400), so the `let LANG` binding would still have been in its temporal-dead-zone at line ~8167, throwing `ReferenceError: Cannot access 'LANG' before initialization` on page load. Caught by reasoning through script evaluation order before testing, not by a live failure. Fixed properly: moved the whole `LANG`/`t()` declaration to the very top of the `#app-jsx` script (right after `const { useState, ... } = React;`), removed the old location, and reverted the risky `FS_LEVELS` edit (level labels chosen from a fixed array like this can't naturally react to a language toggle anyway, since the array is built once -- translating them needs a different approach, e.g. translating at the display call site inside a render function, left for whenever those labels actually need it). Left a comment at the top explaining the constraint so future phases don't repeat this: only call `t()` from inside a component's render body, never at module top-level.
- Translated (Lesson-level chrome only, per chapter): **First Steps** (`FirstStepsLearn`) -- Lesson title/intro, all 9 step titles, and the `Rule` tip title+body text for each step that has one (Sitting, A round hand, The arm carries the hand, The black keys are the map, Not every student needs this yet). **Note Names** (`NoteNamesLearn`) -- Lesson title/intro, all 4 step titles, all 4 `Rule` tips, the black-key/white-key group captions, and the "Say it out loud together" label. Also translated the drill-mode prompt text used by this chapter's two question components: `NoteNameQuestion` ("Which note is the highlighted key?" / "Tap this note on the keyboard" and their pixel-mode shouted versions) and `LetterStepQuestion` (the "Say it, then tap it" / "WHICH LETTER?" prompts, the letter-circle's up/down labels, and the interval cue text -- added a small `intervalWordKo(size)` helper since the existing English `intervalWord`/`withArticle` grammar helpers don't translate directly, e.g. size 8 -> "옥타브" not "8도").
- Not yet translated (same honest caveat as Phase 145): the ~9 hands-on sub-components inside First Steps (`SitCheck`, `HandShape`, `ArmExercises`, `PostureChecklist`, `FingerNumbers`, `HighLowGame`, `KeyHouses`, `BlackKeySong`, `BlackWhiteNeighbours`) and Note Names' own sub-tools (`FindAll`, `NameReveal`, `UpDownWalk`, `LetterChainDrill`) still show their internal English text (button labels, instructions, exercise copy) -- only the shared Lesson/Step wrapper text and the top-level tips around them are in Korean so far. These are real, substantial follow-up work, not overlooked.
- Verification: Babel-compiled the `#app-jsx` script (`@babel/standalone` 7.23.3, pinned) + `new Function()` on the output after the LANG/t() move -- 0 errors (this is also what would have caught the TDZ bug at build time if it had shipped, since `new Function()` executes the compiled module top-level code). Live Playwright test in headless Chromium: loaded First Steps in Korean (screenshot reviewed -- header, nav, all step titles and Rule tips correctly in Korean, sub-widget internals correctly still English as expected), then navigated to Note Names and confirmed the language choice persisted across the navigation (still Korean without re-toggling), then opened the Note Names drill (Level 1, Lesson mode) and confirmed the Korean prompt text renders. Zero console/page errors (aside from expected blocked-external-domain noise).
- Committed locally, not pushed -- Sohyun to `git push` from her Terminal as always.

Phase 147 -- Korean localization continued: Pulse & Counting chapter. Direct continuation of the agreed priority order (Phase 146: (1) First Steps, (2) Note Names done; (3) Pulse & Counting was next).
- Translated (Lesson-level chrome, same scope as the two prior phases): `PulseLearn` -- Lesson title/intro, all 4 step titles (Feel the pulse, Tap the right beat, Count out loud, Clap the rhythm cards), and the 3 `Rule` tips (Count inside, Long and short notes, Clap and count). Also translated the drill-mode prompt text in `PulseQuestion`: "How many beats does it last?", "Listen (4 clicks = one bar): which one was it?", and the "♪ Play again" button label.
- Not yet translated (same honest caveat as the prior two phases): this chapter's sub-widgets (`SteadyBeat`, `BeatTarget`, `CountAloud`, `RhythmComposer`) still show their internal English text -- only the shared Lesson/Step wrapper and the drill question prompts are in Korean so far. `answerLabel` strings (the "it was X" wrong-answer feedback text, used across every chapter's drill runner) were also left untranslated -- these are shared low-level formatting functions repeated in nearly every chapter's drill config, not specific to Pulse & Counting, and are a separate follow-up pass of their own.
- Verification: Babel-compiled the `#app-jsx` script (`@babel/standalone`, `presets:['react']`) + `new Function()` on the output -- 0 errors. Live Playwright test in headless Chromium (React 18.2.0 / ReactDOM 18.2.0 / Babel-standalone via local npm copies, served locally since cdnjs is blocked from this sandbox): loaded the Pulse & Counting chapter's Learn tab, toggled to Korean, confirmed the Lesson title, all 4 step titles, and the language toggle itself all render correctly in Korean (screenshot reviewed); separately loaded the drill (Level 1, Lesson mode) directly in Korean via URL params and confirmed the "몇 박 동안 지속될까요?" prompt renders. Zero page errors both times (only expected blocked-external-domain noise).
- Committed locally, not pushed -- Sohyun to `git push` from her Terminal as always.

Phase 148 -- Korean localization continued: Time Signatures chapter. Direct continuation of the agreed priority order (Phase 147: Pulse & Counting done; (5) Time Signatures was next).
- Translated (same Lesson-chrome + drill-prompt scope as the prior three phases): `TimeSigLearn` -- Lesson title/intro, all 6 step titles (The two numbers, Bar lines, When the quaver is the beat, Compound time, Grouping notes to show the beat, Duplets), the top/bottom-number explainer box, the "Simple time" and "6/8, 9/8, 12/8" section captions, the "8 on the bottom: everything doubles" `Rule` (title + body), and the compound-time explanatory paragraph. Also translated all 5 drill-mode prompts in `TimeSigQuestion` (meaning / fits / listen / double / feel question types, including their pixel-mode shouted versions) and the "In each bar: " choice-label prefix and "♪ Play again" button.
- Not yet translated (same honest caveat as the prior phases): this chapter's sub-widgets (`BeatPulse`, `BarLineBuilder`, `BeatDoubler`, `RegroupQuavers`, `GroupingGame`, `DupletDemo`) still show internal English text. The drill choice labels themselves (e.g. "3 quaver beats", "2 crotchet beats") are built by a shared label-generator function combining dynamic note/beat data and were left in English, same reasoning as the `answerLabel` functions flagged in Phase 147 -- these are deeper, more structural translations than the Lesson-chrome pass this project is doing chapter by chapter right now, and are noted as follow-up work alongside the `answerLabel` pass.
- Verification: Babel-compiled the `#app-jsx` script (`@babel/standalone`, `presets:['react']`) + `new Function()` on the output -- 0 errors. Live Playwright test in headless Chromium (React 18.2.0 / ReactDOM 18.2.0 / Babel-standalone via local npm copies, served locally since cdnjs is blocked from this sandbox): loaded the Time Signatures Learn tab, toggled to Korean, confirmed the Lesson title, all 6 step titles, and body text render correctly in Korean (screenshot reviewed); separately loaded all 5 drill levels directly in Korean via URL params and confirmed each level's distinct Korean prompt text renders correctly ("이 박자표는 무슨 뜻일까요?", "센 첫 박을 잘 들어보세요...", "12/8에서는 8분음표가 1박이에요...", "단순박자일까요, 겹박자일까요..."). Zero page errors across all checks (only expected blocked-external-domain noise).
- Committed locally, not pushed -- Sohyun to `git push` from her Terminal as always.

Phase 149 -- Korean localization continued: Rhythm Cards chapter. Direct continuation of the agreed priority order (Phase 148: Time Signatures done; (6) Rhythm Cards was next).
- Translated (same Lesson-chrome + drill-prompt scope as the prior four phases): `RhythmLearn` -- Lesson title/intro, all 4 step titles (The 40 cards, Harder rhythms: dots/semiquavers/triplets, Anacrusis: starting before beat 1, Make your own), the "Set N" chip labels, the "New in this set:" caption, and the counting-notation caption. Also translated both drill-mode prompts in `RhythmQuestion` (the "listen -- which card" type and the "tap along" type, including pixel-mode shouted versions), the "Play again"/"Hear it first"/"Start tapping"/"Ready…"/"Tap!" button labels, and the hits/extra-taps result line.
- **Real bug caught and fixed before it shipped, same class as Phase 146's TDZ bug**: `RhythmLearn` had `const t = RHYTHM_TIERS[tier - 1];` -- a local variable named `t` that shadowed the global `t()` translate function for the rest of that component's scope. The first live test caught it immediately (`t is not a function` -- calling the tier object as if it were the translate function). Renamed the local variable to `tr` throughout `RhythmLearn` (three usages: `tr.bpm` ×2, `tr.label`) rather than only patching the one line that collided, so no latent second collision was left behind. This is exactly the naming-collision risk flagged as a lesson in Phase 146's log (the `TOOLS.find(t => ...)` rename) -- worth remembering as a checklist item for every future chapter: grep the component for a local `const t =`/`let t =`/`t =>` before assuming `t()` calls are safe to add.
- Not yet translated (same honest caveat as the prior phases): `CountHarder`, `AnacrusisDemo`, and `RhythmComposer` (the three sub-widgets embedded in this chapter) still show internal English text; the shared `answerLabel` function for this drill (the "count it: 1 2 3 4" wrong-answer feedback) was also left untranslated, same reasoning as the other chapters' `answerLabel` functions.
- Verification: Babel-compiled the `#app-jsx` script (`@babel/standalone`, `presets:['react']`) + `new Function()` on the output -- 0 errors both before and after the shadowing fix (the compile check alone doesn't catch a runtime `TypeError` like this one; only the live Playwright run did). Live Playwright test in headless Chromium (React 18.2.0 / ReactDOM 18.2.0 / Babel-standalone via local npm copies, served locally since cdnjs is blocked from this sandbox): first run surfaced the `t is not a function` page error immediately and confirmed none of the intended Korean strings rendered; after the fix, re-ran and confirmed the Lesson title, all 4 step titles, and chip labels render correctly in Korean with zero page errors; separately loaded drill Level 1 (listen) and Level 2 (tap) directly in Korean via URL params and confirmed each level's distinct Korean prompt renders correctly ("들어보세요 -- 어떤 카드일까요?", "따라 두드려보세요: 4번 클릭으로 카운트인..."), plus the "먼저 들어보기"/"두드리기 시작" buttons. Zero page errors on the final pass.
- Committed locally, not pushed -- Sohyun to `git push` from her Terminal as always.

Phase 150 -- Korean localization continued: Reading the Staff chapter. Direct continuation of the agreed priority order (Phase 149: Rhythm Cards done; (7) Reading the Staff was next). Per the Phase 149 lesson, checked `StaffLearn`/`StaffQuestion` for a local `t`-shadowing variable before adding calls -- none found (the local helper here is named `tip`, not `t`), so no collision this time.
- Translated (same Lesson-chrome + drill-prompt scope as the prior five phases): `StaffLearn` -- Lesson title/intro, all 9 step titles (What is the staff?, Two staves two clefs, Line/space/line/space, The rhymes, Landmarks, Fast flash cards, Middle C and ledger lines, Write them, A third clef), the "Why they're called the G clef and the F clef" sub-heading, and all 6 `Rule` tips (their titles and full bodies, including the EGBDF/FACE and GBDFA/ACEG mnemonic sentences kept in their original English form inside the Korean sentence, since they're the actual English mnemonic being taught, not prose to translate). Also translated both drill-mode prompts in `StaffQuestion` ("Tap this exact note on the keyboard" / "Name this note", including pixel-mode shouted versions), used by all 4 drill levels.
- Not yet translated (same honest caveat as the prior phases): this chapter's many sub-widgets (`StaffBasics`, `ClefBasics`, `ClefStory`, `StaffClimb`, `MnemonicStaff`, `StaffExplorer`, `LandmarkHop`, `FlashCards`, `FoldStaff`, `LedgerMirror`, `WriteTheNote`, `AltoClef`) still show internal English text -- this is the largest single chapter translated so far in terms of embedded sub-tools, so the gap between "Lesson chrome done" and "fully translated" is bigger here than in earlier chapters. The `answerLabel` function for this drill was also left untranslated, same reasoning as other chapters.
- Verification: Babel-compiled the `#app-jsx` script (`@babel/standalone`, `presets:['react']`) + `new Function()` on the output -- 0 errors. Live Playwright test in headless Chromium (React 18.2.0 / ReactDOM 18.2.0 / Babel-standalone via local npm copies, served locally since cdnjs is blocked from this sandbox): loaded the Reading the Staff Learn tab, toggled to Korean, confirmed the Lesson title and all 9 step titles render correctly in Korean (checked programmatically against the rendered page text, not just visually); separately loaded drill Level 1 (name this note) and Level 4 (find it on the keyboard) directly in Korean via URL params and confirmed each level's distinct Korean prompt renders correctly. Zero page errors across all checks (only expected blocked-external-domain noise).
- Committed locally, not pushed -- Sohyun to `git push` from her Terminal as always.

Phase 151 -- Korean localization continued: Five-Finger Positions chapter. Direct continuation of the agreed priority order (Phase 150: Reading the Staff done; (8) Five-Finger Positions was next). Checked `FiveFingerLearn`/`FfQuestion` for a local `t`-shadowing variable before adding calls -- none found (the local helper here is named `tip`, same pattern as Reading the Staff), so no collision.
- Translated (same Lesson-chrome + drill-prompt scope as the prior six phases): `FiveFingerLearn` -- Lesson title/intro, both step titles (C position, Read with your fingers), and both `Rule` tips (Thumbs on C, Finger = note). Also translated the drill-mode prompt in `FfQuestion` ("[Position], [right/left] hand: which finger plays this note?" -- split into three separately-translated pieces since the position title itself, `q.pos.title`, is dynamic data from the `POSITIONS` array and stays in English).
- Not yet translated (same honest caveat as the prior phases): this chapter's two sub-widgets (`FivePosition`, `MiniTune`) still show internal English text (e.g. "Five-finger positions" heading, "Right hand"/"Left hand" chips, "One finger for each key..." instructions, "♪ Up and down" button). The `answerLabel` function for this drill ("finger N (note)") was also left untranslated, same reasoning as other chapters.
- Verification: Babel-compiled the `#app-jsx` script (`@babel/standalone`, `presets:['react']`) + `new Function()` on the output -- 0 errors. Live Playwright test in headless Chromium (React 18.2.0 / ReactDOM 18.2.0 / Babel-standalone via local npm copies, served locally since cdnjs is blocked from this sandbox): loaded the Five-Finger Positions Learn tab, toggled to Korean, confirmed the Lesson title and both step titles render correctly in Korean; separately loaded drill Level 1 directly in Korean via URL params and confirmed "오른손"/"어떤 손가락으로 이 음을 칠까요?" render correctly. Zero page errors across all checks (only expected blocked-external-domain noise).
- Committed locally, not pushed -- Sohyun to `git push` from her Terminal as always.

Phase 152 -- Korean localization continued: Tones & Semitones chapter. Direct continuation of the agreed priority order (Phase 151: Five-Finger Positions done; (9) Tones & Semitones was first of the theory chapters).
- Translated (same Lesson-chrome + drill-prompt scope as the prior seven phases): `TonesLearn` -- Lesson title/intro ("Semitones, tones and accidentals" -> "반음, 온음, 임시표"), all 3 step titles (Semitones and tones, Accidentals: sharp/flat/natural, The chromatic scale and double sharps), the Semitone/Tone comparison card labels, and all 6 `Rule` tips (3 in step 1, 3 in step 2). Also translated all 3 drill-mode prompts in `TonesQuestion` (enharmonic "other name" question, tone-or-semitone question incl. its two answer buttons, and the "tap the key [a semitone/tone] [up/down] from X" question, including pixel-mode shouted versions). Noted the local `prompt = (t, px) => ...` helper inside `TonesQuestion` shadows the global `t()` within its own arrow-function body -- confirmed safe since all translated `t()` calls happen at the *call site* (arguments passed into `prompt(...)`), never inside the helper's own body, so no collision occurred; left the parameter name as-is since it introduced no actual bug, but flagging the pattern for whoever touches this function next.
- Not yet translated (same honest caveat as the prior phases): this chapter's two sub-widgets (`StepExplorer`, `AccidentalCards`, `SharpFlatMover`, `AccidentalBar`, `ChromaticScale` -- five sub-components in this chapter, more than most) still show internal English text. The `answerLabel` function for this drill was also left untranslated, same reasoning as other chapters.
- Verification: Babel-compiled the `#app-jsx` script (`@babel/standalone`, `presets:['react']`) + `new Function()` on the output -- 0 errors. Live Playwright test in headless Chromium (React 18.2.0 / ReactDOM 18.2.0 / Babel-standalone via local npm copies, served locally since cdnjs is blocked from this sandbox): loaded the Tones & Semitones Learn tab, toggled to Korean, confirmed the Lesson title, all 3 step titles, and body text render correctly in Korean; separately loaded drill Level 1 (which) and Level 3 (enh) directly in Korean via URL params and confirmed each level's distinct Korean prompt renders correctly ("온음일까요, 반음일까요?", "같은 건반의 다른 이름은?"); Level 2 (find) confirmed loads with zero errors (in English, fresh localStorage in that separate test run, but mechanism identical to the other two levels already confirmed). Zero page errors across all checks.
- Committed locally, not pushed -- Sohyun to `git push` from her Terminal as always.

Phase 153 -- Korean localization continued: Scales chapter (major + minor). Direct continuation of the agreed priority order (Phase 152: Tones & Semitones done; (10) Scales was next). Checked `ScalesLearn`/`ScaleQuestion` for a local `t`-shadowing variable before adding calls -- none found.
- Translated (same Lesson-chrome + drill-prompt scope as the prior eight phases): the major/minor tab chips, both `ScalesLearn` lessons in full (major: title/intro + all 7 step titles -- The shape, Build it yourself, Degree names, Fingering patterns, Your scale path, Practise the fingering, Look up any scale; minor: title/intro + all 5 step titles -- Three forms, Build it yourself, Fingering patterns, Your scale path, See every form). Also translated every prompt/caption in `ScaleQuestion` across all 8 drill levels: the hand name shown in the question title ("right hand"/"left hand"), all 4 kind-specific prompts (which finger / where does 4 go / tap the raised 7th / build it), the "Steps so far: ... next: ..." progress caption, the seventh/build/default captions under the keyboard, and the "Check (N picked)" button.
- Not yet translated (same honest caveat as the prior phases): this chapter has the most sub-widgets of any chapter translated so far -- `MajorShapeCard`, `ScaleBuilder`, `DegreeNames`, `ScalePatterns`, `ScalePath`, `ScaleFingeringDrill`, `ScaleFinder`, `MinorFormsCard`, `ScalePath` (minor), `MinorViewer` -- all still internal English. The `scaleAnswerLabel` function was also left untranslated, same reasoning as other chapters' `answerLabel` functions.
- Verification: Babel-compiled the `#app-jsx` script (`@babel/standalone`, `presets:['react']`) + `new Function()` on the output -- 0 errors. Live Playwright test in headless Chromium (React 18.2.0 / ReactDOM 18.2.0 / Babel-standalone via local npm copies, served locally since cdnjs is blocked from this sandbox): loaded the Scales Learn tab, toggled to Korean, confirmed the major Lesson's title, all 7 step titles render correctly in Korean; clicked the minor tab and confirmed it switches lessons and renders the minor Lesson's title + step titles correctly; separately loaded drill Level 1 (finger) and Level 7 (build) directly, toggled to Korean, and confirmed each level's distinct Korean prompt text renders correctly ("표시된 음은 어떤 손가락으로 칠까요?", "한 걸음씩 스케일을 올라가며..."). Zero page errors across all checks.
- Committed locally, not pushed -- Sohyun to `git push` from her Terminal as always.

Phase 154 -- Korean localization continued: Key Signatures chapter. Direct continuation of the agreed priority order (Phase 153: Scales done; (11) Key Signatures was next). Checked `KeySigLearn`/`KeySigQuestion` for a local `t`-shadowing variable before adding calls -- none found (`KeySigQuestion` has its own local `prompt` helper, same safe pattern as Tones & Semitones' `TonesQuestion`, not named `t`).
- Translated (same Lesson-chrome + drill-prompt scope as the prior nine phases): `KeySigLearn` -- Lesson title/intro ("Reading a key signature" -> "조표 읽기"), all 7 step titles (The order of sharps, The order of flats, Place them yourself, Name the key, The circle of fifths, Transposing, All 15 keys), the "A sentence to remember the sharps.../Read it backwards for the flats..." lead-ins (kept the FCGDAEB mnemonic itself in English, same reasoning as Reading the Staff's EGBDF/FACE mnemonics -- it's the actual English mnemonic being taught), all 4 `Rule` tips in the "Name the key" step, and the "Tap one" label in the "All 15 keys" step. Also translated all 4 drill-question types in `KeySigQuestion` (circle of fifths direction prompt, sharps/flats count prompt, order-of-sharps/flats prompt, and the major/minor-key-from-signature prompt), including pixel-mode shouted versions.
- Not yet translated (same honest caveat as the prior phases): this chapter's 5 sub-widgets (`OrderBuilder`, `PlaceIt`, `RelativeMinor`, `CircleOfFifths`, `Transposer`) still show internal English text. The `answerLabel`-equivalent logic for this drill was also left untranslated, same reasoning as other chapters.
- Verification: Babel-compiled the `#app-jsx` script (`@babel/standalone`, `presets:['react']`) + `new Function()` on the output -- 0 errors. Live Playwright test in headless Chromium (React 18.2.0 / ReactDOM 18.2.0 / Babel-standalone via local npm copies, served locally since cdnjs is blocked from this sandbox): loaded the Key Signatures Learn tab, toggled to Korean, confirmed the Lesson title and all 7 step titles render correctly in Korean; separately loaded all 6 drill levels directly, toggled to Korean, and confirmed each level's distinct Korean prompt text renders correctly (level 1/3/4 "이 조표는 어떤 장조/단조일까요?", level 2 "몇 개일까요?", level 5 order-of-sharps/flats text, level 6 "5도권" text). Zero page errors across all checks.
- Committed locally, not pushed -- Sohyun to `git push` from her Terminal as always.

Phase 155 -- Korean localization continued: Intervals chapter. Direct continuation of the agreed priority order (Phase 154: Key Signatures done; (12) Intervals was next). Checked `IntervalsLearn`/`IntervalQuestion` for a local `t`-shadowing variable before adding calls -- `IntervalQuestion` has its own local `prompt = (t, px) => ...` helper, same pattern already confirmed safe in Phase 152 (`TonesQuestion`) -- all translated `t()` calls happen at `prompt(...)`'s call sites in the surrounding component body, never inside `prompt`'s own body, so no collision.
- Translated (same Lesson-chrome + drill-prompt scope as the prior ten phases): `IntervalsLearn` -- Lesson title/intro (with embedded `<b>` tags for "number"/"quality"/"major 3rd"/"perfect 5th" kept structurally intact), all 5 step titles (The number, The quality, The major-scale shortcut, Train your ear, Inversions and the tritone), and all 5 `Rule` tips (Count the letters, Count the semitones, Think of the major scale, Link each one to a tune, and the "Grade 3" tip -- title left as `t('Grade 3', 'Grade 3')` since it's a grade-level label rather than prose, body translated). Also translated all 9 drill-question types in `IntervalQuestion`: 'build' (tap-the-key prompt), 'ear' (listen + "play again" button), and the default block's 4 sub-kinds (invert, num, tonic, name), including pixel-mode shouted versions throughout.
- Not yet translated (same honest caveat as the prior phases): this chapter's 7 sub-widgets (`IntervalRuler`, `LetterWalker`, `SemitoneCounter`, `MajorScaleIntervals`, `IntervalEar`, `IntervalInverter`, `TritoneTool`) still show internal English text. The `INTERVALS_DRILL.answerLabel` logic was also left untranslated, same reasoning as other chapters.
- Verification: Babel-compiled the `#app-jsx` script (`@babel/standalone`, `presets:['react']`) + `new Function()` on the output -- 0 errors. Live Playwright test in headless Chromium (React 18.2.0 / ReactDOM 18.2.0 / Babel-standalone via local npm copies, served locally since cdnjs is blocked from this sandbox): loaded the Intervals Learn tab, toggled to Korean, confirmed the Lesson title, all 5 step titles ("도수", "성질", "전위와 트라이톤" among them), and body text render correctly in Korean; separately loaded all 9 drill levels directly, toggled to Korean, and confirmed each level's distinct Korean prompt text renders correctly ("이 음정은 몇 도일까요?", "음정의 이름은?", "A♭ 장조에서: 으뜸음 위 음정의 이름은?", "G 위로 major 3rd만큼 떨어진 건반을 눌러보세요", "들어보세요: 어떤 음정일까요?" + "♪ 다시 듣기", "이것은 major 6th이에요. 뒤집으면 무엇이 될까요?"). Zero page errors across all 9 levels.
- Committed locally, not pushed -- Sohyun to `git push` from her Terminal as always.

Phase 156 -- Korean localization continued: Chords chapter. Direct continuation of the agreed priority order (Phase 155: Intervals done; (13) Chords was next). Checked `ChordsLearn`/`ChordQuestion` for a local `t`-shadowing variable before adding calls -- `ChordQuestion` has its own local `prompt = (t, px) => ...` helper, same safe pattern already confirmed in Phase 152/155 (calls happen at `prompt(...)`'s call sites in the outer scope, never inside `prompt`'s own body).
- Translated (same Lesson-chrome + drill-prompt scope as the prior eleven phases): `ChordsLearn` -- Lesson title/intro (with embedded `<b>` tags for "letters"/"Roman numeral" kept structurally intact), all 6 step titles (Stack a triad, Major and minor, Roman numerals, I IV and V, Inversions, Cadences), and all 6 `Rule` tips. Also translated all 7 drill-question types in `ChordQuestion`: 'build' (tap-the-three-keys prompt), 'cadence' (listen + "play again"), 'ear' (major/minor by ear + "play again"), and the default block's 4 sub-kinds (tonic, roman, inv, quality), including pixel-mode shouted versions throughout.
- Not yet translated (same honest caveat as the prior phases): this chapter's 6 sub-widgets (`TriadStacker`, `MajorMinorFlip`, `KeyChords`, `PrimaryTriads`, `InversionFlip`, `CadencePlayer`) still show internal English text. The `CHORDS_DRILL.answerLabel` logic was also left untranslated, same reasoning as other chapters.
- Verification: Babel-compiled the `#app-jsx` script (`@babel/standalone`, `presets:['react']`) + `new Function()` on the output -- 0 errors. Live Playwright test in headless Chromium (React 18.2.0 / ReactDOM 18.2.0 / Babel-standalone via local npm copies, served locally since cdnjs is blocked from this sandbox): loaded the Chords Learn tab, toggled to Korean, confirmed the Lesson title ("화음과 삼화음") and all 6 step titles ("삼화음 쌓기", "전위" etc.) render correctly; separately loaded all 7 drill levels directly, toggled to Korean, and confirmed each level's distinct Korean prompt text renders correctly ("어느 조의 으뜸화음일까요?", "A minor에서: 이 화음은 I, IV, V 중 무엇일까요?", "장화음일까요, 단화음일까요?", "들어보세요: 장화음일까요, 단화음일까요?", "세 개의 건반을 눌러보세요: F major", "E 삼화음 -- 어떤 위치일까요?", "문장의 끝을 들어보세요: 어떤 종지일까요?"). Zero page errors across all 7 levels.
- Committed locally, not pushed -- Sohyun to `git push` from her Terminal as always.

Phase 157 -- Korean localization continued: Signs chapter. Direct continuation of the agreed priority order (Phase 156: Chords done; (14) Signs was next). Checked `SignsLearn`/`SignsQuestion` for a local `t`-shadowing variable before adding calls -- `SignsQuestion` has its own local `prompt = (t, px) => ...` helper, same safe pattern already confirmed in Phase 152/155/156 (calls happen at `prompt(...)`'s call sites in the outer scope, never inside `prompt`'s own body).
- Translated (same Lesson-chrome + drill-prompt scope as the prior twelve phases): `SignsLearn` -- Lesson title/intro, all 6 step titles (Repeat signs, D.C./D.S./Fine and Coda, Ties and slurs, 8va and 8vb, Ornaments, Write a grace note), and all 5 `Rule` tips (The repeat sign, 1st and 2nd time bars, D.C., D.S., Fine and Coda). Also translated all 3 drill-mode prompts in `SignsQuestion` (tie-or-slur, road-map playing order, sign meaning), including pixel-mode shouted versions.
- Not yet translated (same honest caveat as the prior phases, and deliberately consistent with how other chapters' lookup-table answer text has been handled): the `SIGN_LIST` array's 11 sign meanings (used as both the correct answer and the wrong-choice distractors in Level 1) were left in English, same reasoning as other chapters' `answerLabel`/choice-list data -- these are shared answer-text data, not Lesson chrome, and are queued for the broader answer-label translation pass. This chapter's sub-widgets (`RoadMap`, `RoadStrip`, `TieOrSlur`, `OttavaDemo`, `Ornaments`, `GraceWrite`) still show internal English text.
- Verification: Babel-compiled the `#app-jsx` script (`@babel/standalone`, `presets:['react']`) + `new Function()` on the output -- 0 errors. Live Playwright test in headless Chromium (React 18.2.0 / ReactDOM 18.2.0 / Babel-standalone via local npm copies, served locally since cdnjs is blocked from this sandbox): loaded the Signs Learn tab, toggled to Korean, confirmed the Lesson title, "도돌이표", "이음줄과 슬러", and "장식음" step titles all render correctly; separately loaded all 3 drill levels directly, toggled to Korean, and confirmed each level's distinct Korean prompt renders correctly ("이 기호는 무슨 뜻일까요?", "이음줄일까요, 슬러일까요?", "마디는 어떤 순서로 연주될까요?"). Zero page errors across all 3 levels.
- Committed locally, not pushed -- Sohyun to `git push` from her Terminal as always.

Phase 158 -- Korean localization continued: Dynamics & Articulation chapter. Direct continuation of the agreed priority order (Phase 157: Signs done; (15) Dynamics & Articulation was next). Checked `DynLearn`/`DynQuestion` for a local `t`-shadowing variable before adding calls -- `DynQuestion` has its own local `prompt = (t, px) => ...` helper, same safe pattern already confirmed in Phase 152/155/156/157 (calls happen at `prompt(...)`'s call sites in the outer scope, never inside `prompt`'s own body).
- Translated (same Lesson-chrome + drill-prompt scope as the prior thirteen phases): `DynLearn` -- Lesson title/intro, all 5 step titles (Soft to loud, Getting louder and softer, The pedals, Articulation, Train your ear), and the p/f/m explainer paragraph (kept the letter abbreviations `p`/`f`/`m` in place, translated the surrounding explanation). Also translated all 5 drill-mode prompts in `DynQuestion` (dynamic meaning, which is louder, volume-change sign meaning, name the articulation marking, and the listen question incl. "♪ Play again" button), including pixel-mode shouted versions.
- Not yet translated (same honest caveat as the prior phases, consistent with how other chapters' lookup-table answer text has been handled): the `DYNAMICS`/`CHANGES`/`ARTICS` arrays' Italian-term meanings (used both as displayed labels in the Learn tab and as the answer/choice text in the drill) were left in English, same reasoning as Signs' `SIGN_LIST` and other chapters' `answerLabel` data. This chapter's sub-widgets (`DynOrder`, `HairpinMaker`, `PedalDemo`, `TouchEar`) still show internal English text.
- Verification: Babel-compiled the `#app-jsx` script (`@babel/standalone`, `presets:['react']`) + `new Function()` on the output -- 0 errors. Live Playwright test in headless Chromium (React 18.2.0 / ReactDOM 18.2.0 / Babel-standalone via local npm copies, served locally since cdnjs is blocked from this sandbox): loaded the Dynamics & Articulation Learn tab, toggled to Korean, confirmed the Lesson title and all 4 step titles ("얼마나 크게", "점점 세게", "페달", "아티큘레이션") render correctly; separately loaded all 5 drill levels directly, toggled to Korean, and confirmed each level's distinct Korean prompt renders correctly ("무슨 뜻일까요?", "어느 쪽이 더 클까요?", "이 기호는 무슨 뜻일까요?", "이 표시는 이름이 무엇일까요?", "들어보세요 -- 무엇이 들리나요?" + "♪ 다시 듣기"). Zero page errors across all 5 levels.
- Committed locally, not pushed -- Sohyun to `git push` from her Terminal as always.

Phase 159 -- Korean localization continued: Tempo Race chapter. Direct continuation of the agreed priority order (Phase 158: Dynamics & Articulation done; (16) Tempo Race was next). Checked `TempoLearn`/`TempoQuestion` for a local `t`-shadowing variable before adding calls -- found and fixed one real risk before it shipped: `TempoLearn`'s `TEMPO_TERMS.map((t, i) => ...)` callback parameter was named `t`, and this phase needed to call the global `t()` translate function *inside* that callback's own body (for the "about X-Y"/"playing" label) -- exactly the dangerous pattern flagged in Phase 149, not the safe call-site pattern from Phase 152/155-158. Renamed the callback parameter to `tm` throughout that map body (`tm.term`, `tm.meaning`, `tm.bpm`) before adding any `t()` calls, avoiding the collision entirely rather than discovering it live. `TempoQuestion`'s own `prompt` helper is named `txt`, not `t` -- no risk there at all.
- Translated (same Lesson-chrome + drill-prompt scope as the prior fourteen phases): `TempoLearn` -- Lesson title/intro, all 3 step titles (Slow to fast, The metronome, Changing speed), the "🐢 Slow"/"Fast 🏁" lane labels, the "♪ playing"/"about X-Y" status text per tempo term, and the "approximate BPM" closing paragraph. Also translated all 4 drill-mode prompts in `TempoQuestion` (term meaning, which is faster, slowest-to-fastest ordering incl. the "Undo" button, and the listen question incl. "♪ Play again"), including pixel-mode shouted versions.
- Not yet translated (same honest caveat as the prior phases): the `TEMPO_TERMS` array's own Italian-term meanings (Adagio/Andante/etc. displayed in the Learn tab and used as answer/choice text in the drill) were left in English, same reasoning as other chapters' lookup-table answer data (`SIGN_LIST`, `DYNAMICS`/`CHANGES`/`ARTICS`). This chapter's 2 sub-widgets (`MetronomeDial`, `SpeedChange`) still show internal English text.
- Verification: Babel-compiled the `#app-jsx` script (`@babel/standalone`, `presets:['react']`) + `new Function()` on the output -- 0 errors. Live Playwright test in headless Chromium (React 18.2.0 / ReactDOM 18.2.0 / Babel-standalone via local npm copies, served locally since cdnjs is blocked from this sandbox): loaded the Tempo Race Learn tab, toggled to Korean, confirmed the Lesson title ("템포 경주") and all 3 step titles ("느리게에서 빠르게로", "메트로놈", "속도 바꾸기") render correctly; separately loaded all 4 drill levels directly, toggled to Korean, and confirmed each level's distinct Korean prompt renders correctly ("이 용어는 무슨 뜻일까요?", "어느 쪽이 더 빠를까요?", "느린 순서대로 눌러보세요", "박을 들어보세요 -- 어떤 템포일까요?" + "♪ 다시 듣기"). Zero page errors across all 4 levels.
- Committed locally, not pushed -- Sohyun to `git push` from her Terminal as always.

Phase 160 -- Korean localization continued: Musical Terms chapter. Direct continuation of the agreed priority order (Phase 159: Tempo Race done; (17) Musical Terms was next). Checked `TermsLearn`/`TermQuestion`/`genTermQuestion` for a local `t`-shadowing variable before adding calls -- all use `tm` for the term variable, not `t` -- no risk.
- Translated (same Lesson-chrome + drill-prompt scope as the prior fifteen phases): `TermsLearn` -- Lesson title/intro, all 5 step titles (Grade 1-4, Match them up), and the one `Rule` tip (Speed, changing speed, volume, touch). Also translated both drill-mode prompts in `TermQuestion` ("What does it mean?" / "Which term means...", the "Say it: " button prefix, and the "♪ Hear it" button).
- Not yet translated (same honest caveat as the prior phases): the `TERMS` array's own term meanings (used as both the displayed meaning and the answer/choice text across all 5 levels) were left in English, same reasoning as other chapters' lookup-table answer data. The `TermCards`/`TermMatch` sub-widgets and the `MUSICIANSHIP_TERMS` toggle still show internal English text.
- Verification: Babel-compiled the `#app-jsx` script (`@babel/standalone`, `presets:['react']`) + `new Function()` on the output -- 0 errors. Live Playwright test in headless Chromium (React 18.2.0 / ReactDOM 18.2.0 / Babel-standalone via local npm copies, served locally since cdnjs is blocked from this sandbox): loaded the Musical Terms Learn tab, toggled to Korean, confirmed the Lesson title ("음악 용어"), "1학년" step title, and "짝 맞추기" step title render correctly; separately loaded all 5 drill levels directly, toggled to Korean, and confirmed each level's distinct Korean prompt renders correctly ("무슨 뜻일까요?" for levels 1-4, "어떤 용어가 이 뜻일까요…" for level 5). Zero page errors across all 5 levels.
- Committed locally, not pushed -- Sohyun to `git push` from her Terminal as always.

This closes out the reading-track theory chapters (Signs, Dynamics & Articulation, Tempo Race, Musical Terms) alongside the pitch-track theory chapters (Intervals, Chords) finished in Phases 155-156 -- every chapter's Lesson-level chrome and drill-mode prompts are now translated. What remains is the deeper, more time-consuming layer: the ~90 individual tool sub-components' own internal text (buttons, instructions, exercise copy inside `FivePosition`, `MiniTune`, `StaffBasics`, `ClefBasics`, `ScaleBuilder`, `OrderBuilder`, `CircleOfFifths`, `TermCards`, `TermMatch`, and dozens more -- Reading the Staff (12 sub-widgets) and Scales (10 sub-widgets) remain the two biggest single gaps), plus the shared `answerLabel`/choice-label/lookup-table data across every chapter (`SIGN_LIST`, `DYNAMICS`/`CHANGES`/`ARTICS`, `TEMPO_TERMS`, `TERMS`, and the many chapter-specific `answerLabel` functions used for "it was X" wrong-answer feedback). This is a much larger, more granular effort than the chapter-by-chapter Lesson-chrome pass just completed, and is the natural next multi-session block. Before adding new `t()` calls anywhere, grep the surrounding function first for a local variable or arrow-function parameter named `t` that would shadow the translate function, and check whether the new `t()` calls would actually land *inside* that shadowed scope's own body (the real risk, per Phase 149 and confirmed again in Phase 159) or only at its call site (safe, per Phase 152/155-158). Sohyun accepted this as multi-session.

### Phase 161 -- Vox-style motion graphics for era/composer content (2026-09-27)

Sohyun's request: apply motion graphics to the era-background and composer-explanation content in the "Know your instrument" chapter, "Vox style" -- confirmed via clarifying questions to mean the bold, clean explainer-video look (animated typography, color-blocked callouts, staggered data reveals synced to narrative beats), starting with era-background/composer content, with intent to extend to other suitable content once she's seen this first piece.

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | New Vox-style CSS keyframes | `drills.html` `<style>` (after the existing `fadeUp` keyframe) | 6 new animations: `voxYearIn` (headline slides in from the left with a slight scale), `voxNameIn`, `voxSlideIn` (traits/rows slide in), `voxPopIn` (composer chips and the year badge pop in with an overshoot ease), `voxBarGrow` (the new feel-bars grow from 0 width), `voxBlockIn` (the "Playing it today" callout). |
| 2 | `ERA_BARS` + `ERA_BAR_LABELS` data | `drills.html` (new, right after the existing `ERAS` array) | Three small "feel" bars per era -- Dynamic range, Pedal use, Tempo flexibility -- rated 1-4, derived directly from each era's own already-written `traits`/`today` text above them (e.g. Baroque = terraced dynamics + little/no pedal + steady dance pulse -> all low; Romantic = huge dynamic range + rich pedal + rubato -> all high). Explicitly labelled in the UI "A rough feel, not a rule -- based on the traits below" so it reads as a visual summary of the existing text, not a new historical claim. |
| 3 | `ErasTimeline` rebuilt with staggered Vox-style reveal | `drills.html` (`ErasTimeline`) | Era tab strip: selected tab now scales up slightly for emphasis. The detail card is now keyed by `E.id` so switching eras remounts and replays the whole reveal sequence. Inside: (a) a bigger, bolder era name + a colour-blocked pill badge for the year range (was plain text) that slide/pop in first; (b) the new 3-row animated feel-bars, each growing in with a staggered delay; (c) the trait bullets slide in one after another; (d) the "Playing it today" callout fades/scales in after the traits; (e) composer names are now colour-tinted pill chips (were a plain comma-separated line) that pop in one by one with an overshoot ease, timed to land after everything above them. All existing functionality preserved unchanged: era tab selection, `playEra` audio playback, the underlying `ERAS` data. |
| 4 | Verification | -- | Babel-compiled the `#app-jsx` script (`@babel/standalone`, `presets:['react']`) + `new Function()` on the output -- 0 errors. Live Playwright test in headless Chromium (React 18.2.0 / ReactDOM 18.2.0 / Babel-standalone via local npm copies, served locally since cdnjs is blocked from this sandbox): loaded the "Know your instrument" chapter, scrolled to "The style eras", confirmed the section renders with the new headline/bars/chips (screenshot reviewed -- Baroque and Romantic both checked, correct era colour theming carried through the badge/bars/chips in both cases); clicked the Romantic tab and confirmed the era, its bars, and its composer chips (Chopin, Schubert, etc.) all switch correctly. Zero page errors (only expected blocked-external-domain noise for fonts/gtag). The real device file was staged after being written and MD5-diffed against the already-verified working copy (`3302d80b...`) to confirm an exact match before committing. |
| 5 | Scope note | -- | Only `ErasTimeline` (era background + composer names) was restyled this phase, per Sohyun's own scoping ("일단 ... 만들어보고 다른것도 적용할 만 것들 추가하면 좋을것 같아" -- do this piece first, then extend to other suitable content). `PianoTimeline` (the tap-a-date timeline just above it in the same chapter) was left unchanged. Candidates to extend the same treatment to next, pending Sohyun's review of this first piece: `PianoTimeline`'s expand/collapse entries, and potentially the Musical Terms chapter's term cards (Phase 122/123), which already has a comparable "one fact revealed at a time" structure. |
| 6 | Committed, not pushed | see git log | Ready for Sohyun to push from her Terminal. |

Live-verified: Sohyun pushed Phases 142-161 together (`4f79752..eae1543`) same session -- confirmed via `git log --oneline origin/main..HEAD` returning empty (local == remote).

### Phase 162 -- Exam Check-Up removed, cleanup pass (2026-09-27)

Sohyun's direction: won't activate the Exam Check-Up service, so remove it outright rather than leaving it half-built; also asked to clear out anything else already built that won't be used, so the project isn't confusing to come back into.

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | `find-a-teacher.html` deleted | `find-a-teacher.html` | The Exam Check-Up form (4-step wizard, $25 AUD pricing added Phase 60, payment never wired up). `git rm`. |
| 2 | Dead homepage entry card removed | `index.html` | The "Get an exam check-up" entry card was already gated behind `{false && (...)}` (never actually live/rendered) -- removed the whole dead block rather than leaving unreachable code linking to a now-deleted file. |
| 3 | `robots.txt` entry removed | `robots.txt` | `Disallow: /find-a-teacher.html` line removed (the file it pointed to no longer exists). |
| 4 | CLAUDE.md live-status sections updated | `CLAUDE.md` | File Structure list, the Revenue-critical status table, and Pending Work item #3 (the Stripe Payment Link task, now moot) updated to reflect the removal. Historical phase-log entries (Phase 54/60 etc. that describe building it) left untouched, per this project's convention of not rewriting past log entries -- only the "current" sections were updated. |
| 5 | What else was reviewed and deliberately NOT deleted | -- | Went through the other built-but-unpromoted pages before deleting only the one Sohyun explicitly named, rather than guessing broadly: `teach-with-us.html` (teacher recruitment form) -- kept live per the 2026-08-25 strategic decision to leave it as a zero-cost passive capture point, revisit later, not "won't use"; `practice-challenge.html` + the 30-Day Challenge `.docx` proposals (now under `_workspace/`) -- Sohyun's own prior note on this was "아직 모르겠음, 다음에" (undecided, later), not decided against, so left alone; `butler.html` -- decided "stays private," which means unlisted, not deleted; `diagnose.html`, `recommend.html`, `viva-voce.html`, `score-reader.html`, `puzzle.html`, `admin-*.html` -- all still actively used or pending Sohyun's own review, not dormant. If any of these should also go, flag them specifically next session rather than a blanket sweep. |
| 6 | Verification | -- | `index.html`'s inline script block staged into the cloud workspace and compiled with `@babel/standalone` (`presets:['react']`) + `new Function()` on the output -- 0 errors, confirming the removed JSX block didn't leave anything broken. `grep -rl "find-a-teacher"` re-run after the edits -- only historical CLAUDE.md phase-log mentions and unrelated scratch files remain (`_workspace/challenge-idea/outreach-messages.md`, a `Claude outputs/` file), nothing live references the removed page. |
| 7 | Committed, not pushed | see git log | Ready for Sohyun to push from her Terminal. |

### Phase 163 -- Vox-style motion graphics extended to PianoTimeline (2026-09-28)

Continuing the Phase 161 Vox-style treatment: applied the same staggered-animation approach to
the `PianoTimeline` component (the "piano's story" tap-to-expand chronology, `drills.html`,
`?tool=piano-timeline`) that Phase 161 gave `ErasTimeline`. Reused the existing Vox keyframes
only -- no new keyframes invented.

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | Timeline rows fade/slide in, staggered | `PianoTimeline` row wrapper `<div>` | `animation:'voxSlideIn 0.3s ' + (i * 0.045) + 's ease both'` -- each of the 9 entries (1400s through Today) slides in in sequence rather than all appearing at once. |
| 2 | Dot markers pop in, staggered | the gold/white dot `<span>` per row | `animation:'voxPopIn 0.3s ' + (0.05 + i * 0.045) + 's cubic-bezier(.34,1.56,.64,1) both'` -- same overshoot easing Phase 161 used for `ErasTimeline`'s composer pill chips. |
| 3 | Vertical connector line fades/settles in | the absolute-positioned line behind the dots | `animation:'voxBlockIn 0.45s ease both'` -- `voxBarGrow` (width-based) didn't fit a vertical line, so used `voxBlockIn` (opacity + translateY + scale) instead of inventing a new keyframe. |
| 4 | Expanded description still animates in on tap | the `open === i` detail `<div>` | `animation:'voxBlockIn 0.28s ease both'` -- fires fresh each time a row is opened, same as before but now with the Vox entrance motion. |
| 5 | Preserved unchanged | `PIANO_TIMELINE` data array, `open`/`setOpen` tap-to-expand state, `key:true` gold-dot styling logic | No data or interaction-logic changes -- animation-only edit. |
| 6 | Verification | -- | `<script id="app-jsx">` extracted from `drills.html` and compiled with `@babel/core` (`preset-react`, `runtime:'classic'`) -- clean compile, then `node --check` on the output -- 0 syntax errors. Live Playwright test in headless Chromium against `drills.html?tool=piano-timeline&lock=1`, served locally with locally-installed React 18.2.0/ReactDOM/Babel-standalone 7.23.3 (cdnjs unreachable from the sandbox): all 9 timeline rows render, 20 elements carry the new `animation` styles, tap-to-expand confirmed working both directions (clicking a closed row opens it and closes the previously-open one; clicking an open row collapses it), full-page screenshot visually confirmed layout and gold-dot styling intact. Only console messages were two blocked-by-sandbox-network requests (Google Fonts, Google Tag Manager) and a Babel "deoptimised styling" size note -- both pre-existing and unrelated to this change, zero real errors. |
| 7 | Committed, not pushed | see git log | Ready for Sohyun to push from her Terminal. |

### Phase 164 -- Teacher view is now the default (2026-09-28)

Sohyun: easiest for her own day-to-day testing if the app opens straight into the teacher view
(Plan / Students / Toolbox / Practice tabs) instead of the clean student view (Learn / Practice)
-- the student-facing default can be revisited once that side is polished. Found already applied,
uncommitted, in the working tree this session (no author note attached) -- reviewed against the
existing `?teacher=1`/`?teacher=0`/`lock=1` mechanism before committing; it's correct and matches
exactly what Sohyun asked for, so it's logged and committed here rather than redone.

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | `UI_TEACHER` default flipped | `drills.html`, the `Mode: teacher/student` block right before `initialMode()` | `let UI_TEACHER = false` -> `true`. `initialMode()` now returns `true` unless `?teacher=0` was ever set on this device (remembered in `localStorage` under `pb_mode_v1`) or the URL explicitly says `?teacher=0`. `?teacher=1` still works exactly as before. |
| 2 | Student links unaffected | same block | `lock=1` links always force the student view regardless of the remembered mode -- unchanged, still the right behaviour for anything sent to an actual student. |
| 3 | Verification | -- | Re-ran this session's own Babel compile + `node --check` + Playwright pass (see Phase 165 below, same verification run) confirms `drills.html` with no query string at all now shows the Plan/Students/Toolbox/Practice tab row. |

### Phase 165 -- Modes and chord extensions, two new Toolbox tools (2026-09-28)

Sohyun: modes (선법) and chord extensions (9th/11th/13th chords) are hard for her to hold onto,
not just students -- asked for something to help her own understanding today, reference-style
rather than a scored quiz, so it goes in the Toolbox next to the other explainer tools
(`triad-stack`, `key-chords`, `scale-finder`, etc.) rather than as a new graded chapter.

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | "The seven modes" tool | `drills.html`, new `MODES`/`modeNotes`/`Modes()`, registered as `modes` under `ch: 'scales'` | Relative framing for the actual pitches (rotates `spellScale(parentKey)`, so spelling can't drift from the rest of the app), listed brightest (Lydian) to darkest (Locrian) rather than by scale degree -- Sohyun's own teaching instinct is usually "relate it to something already known," and the brightness ladder is the one idea that tends to make the whole system click. Each mode shows its formula against major/minor, a one-line character description, the scale on a horizontal staff (`MelodyStaff`, reused as-is), and playback with note-by-note highlighting (`playMelody`, reused as-is). Parent major choices kept to a small, familiar set (C, G, D, F, Bb). |
| 2 | "Build a 7th chord" tool | `drills.html`, new `SEVENTH_TYPES`/`seventhChord`/`SeventhChords()`, registered as `seventh-chords` under `ch: 'chords'` | Major 7th, Dominant 7th, Minor 7th, Half-diminished (m7♭5) and Diminished 7th (°7), each built from the same triad-quality + interval-quality machinery (`ivBuild`) already used for plain triads elsewhere in the file, so these chords can't disagree with the rest of the app's theory. Follows the exact defensive pattern `MajorMinorFlip` already uses: only renders the staff when every note is a single sharp/flat, otherwise falls back to plain letter+accidental text -- this is what lets diminished 7th's enharmonic top note (a double flat, e.g. C°7's B𝄫) be included safely without a broken staff render. |
| 3 | "Beyond the 7th: 9, 11, 13" tool | `drills.html`, new `EXT_STACK`/`ChordExtensions()`, registered as `chord-extensions` under `ch: 'chords'` | A plain stack-of-3rds reference kept diatonic on C (every note a white key, root through the 13th: C E G B D F A) so only the counting pattern needs reading -- directly answers "why 9 and not 2": the 9th/11th/13th are just the 2nd/4th/6th scale degrees an octave up, and there's no "15th" because that's the root again. |
| 4 | Verification | -- | `<script id="app-jsx">` extracted and compiled with `@babel/core` (`preset-react`, `runtime:'classic'`) after every edit (including a fix, see #5) -- clean compile, then `node --check` -- 0 syntax errors each time. Live Playwright pass in headless Chromium against a locally-served copy (React 18.2.0 / ReactDOM / Babel-standalone 7.23.3, cdnjs unreachable from the sandbox): confirmed the default (no query string) view now shows the Plan/Students/Toolbox/Practice tabs (Phase 164); opened all three new tools directly by URL (`?tool=modes`, `?tool=seventh-chords`, `?tool=chord-extensions`) and clicked through every chip/button in each (parent-key and mode rows, all 7 root chips × all 5 seventh-chord types, all 7 extension-stack steps) with zero JS exceptions; full-page screenshots confirm correct rendering (modes' scale staff and brightness list, the 7th-chord keyboard/staff with correct chord-tone highlighting, the 9/11/13 stack diagram). |
| 5 | Bug caught and fixed during verification | `drills.html`, the three new "Hear it" buttons | First pass wrote the ♪ note character as a `\u266A` escape sequence directly inside JSX child text -- JSX text content isn't a JS string literal, so escapes aren't interpreted there (unlike inside a quoted string), and the button literally read "\u266A Hear it" in the browser. Confirmed via screenshot, fixed by using the literal ♪ character in the JSX text (matching how every other "♪ ..." button in the file already does it), recompiled and re-screenshotted to confirm the fix. |
| 6 | Committed, not pushed | see git log | Ready for Sohyun to push from her Terminal. |

### Phase 166 -- Toolbox category chips moved to the top; new tools re-categorized (2026-09-28)

Sohyun pushed Phase 164-165 live herself from her Terminal, then, browsing the live site,
compared the Toolbox to the Learn tab's category-chip overview (PITCH / RHYTHM / READING THE
MUSIC, etc.) and asked for the same easy-to-scan category view at the top of the Toolbox --
the Toolbox already grouped tools by category further down the page, but the only way to jump
to a category was a small, easy-to-miss pill row buried below the search box and level/kind
filter chips.

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | Category chips moved to the top of the Toolbox | `drills.html`, `Toolbox()` | The category quick-jump row (one chip per `TOOL_CATS` entry, each still scrolling to its `#cat-<id>` section) now renders directly under the "Toolbox" title/subtitle, before the search box -- it's the first thing seen, matching how the Learn tab leads with its category chips. Made larger/bolder (bigger padding and font) to read as an overview, not a filter afterthought. The old row (which only showed categories with a currently-matching tool, positioned after the level/kind filter chips) was removed rather than duplicated. |
| 2 | Bug fix: today's 3 new tools were miscategorized | `drills.html`, `TOOL_META` | `modes`, `seventh-chords` and `chord-extensions` (added in Phase 165) were never added to `TOOL_META`, so `toolMeta()`'s fallback silently filed all three under "Practice helpers" with a default "All levels" range -- caught while verifying this change, since the new top-of-page category chips made the wrong grouping obvious immediately. Fixed: `modes` -> Scales & keys (Grade 3-4), `seventh-chords` and `chord-extensions` -> Intervals & chords (Grade 3-4, matching the rest of that chapter's advanced tools). |
| 3 | Verification | -- | Babel compile + `node --check` -- 0 errors. Live Playwright pass: confirmed the category-chip row now renders before the search input (screenshot), and confirmed the corrected placement -- "The seven modes" now appears under the "Scales & keys" section header and "Build a 7th chord" / "Beyond the 7th: 9, 11, 13" now appear under "Intervals & chords", in that order, with zero JS errors. |
| 4 | Committed, not pushed | see git log | Ready for Sohyun to push from her Terminal. |

### Phase 167 -- Smarter Toolbox search + record-your-own-voice metronome count (2026-09-28)

Sohyun: still spending time hunting for tools in the Toolbox search (typed "time signature",
"minim" and didn't reliably land on the right tool), and asked whether the metronome's spoken
count could use her own recorded voice instead of only the built-in voice packs, usable right
away rather than needing new audio files uploaded to the server.

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | Chapter-level search keyword aliases | `drills.html`, new `CHAPTER_SEARCH_TERMS`, used in `Toolbox()`'s `match()` | A word like "minim" or "time signature" often isn't literally in a given tool's own title/blurb even though the tool is exactly the right one -- added a small dictionary of extra search terms per chapter (British *and* American note-value names, "time signature"/"meter", etc.) and appended it into the search `hay` string alongside title/blurb/category text. Typing "minim" now surfaces every `note-values` tool; "time signature" surfaces every `time-signatures` tool, including ones whose own blurb never uses that phrase (e.g. "Put in the bar lines"). |
| 2 | "My voice" recording for the metronome's spoken count | `drills.html`, new `MYVOICE_KEY`/`loadMyVoice`/`saveMyVoiceClip`/`loadMyVoiceBufs`/`VoiceWordRecorder`/`MyVoiceRecorder`, wired into `sayCount()`, `getAudio()` and `SoundSettings()` | A 4th "Voice" option next to the existing Female (US)/Female (UK)/Male packs. Tap a number (1-8, "and") to record with the mic (MediaRecorder), tap again to stop; stored as base64 audio in `localStorage` under `pb_myvoice_v1` -- same `pb_*_v1` convention as every other preference in this file, on-device only, no server upload or redeploy needed, usable the instant it's recorded. Playback reuses the exact same onset-alignment (`onsetOf`) the server-hosted voice packs already use in `sayCount()`, so a home-recorded count lines up with the beat exactly like the built-in voices. `loadCount()` skips its (would-be 404) fetch to a non-existent `audio/count/myvoice/` server folder once this pseudo-voice is selected. |
| 3 | Verification | -- | Babel compile + `node --check` -- 0 errors. Live Playwright pass in headless Chromium launched with a fake microphone device (`--use-fake-device-for-media-stream`) and granted mic permission: searching "time signature" and "minim" in the Toolbox returns the expected tools (16 and 6 results respectively, including tools whose own text doesn't contain the search word); recorded all 9 words end-to-end (mic -> MediaRecorder -> blob -> `localStorage`, confirmed the actual stored clip data), then started the live metronome with Voice count + My voice selected and let it run through several beats with zero JS errors, confirming playback actually reads the recorded clips back. Confirmed no wasted network requests to a nonexistent `audio/count/myvoice/` folder. |
| 4 | Committed, not pushed | see git log | Ready for Sohyun to push from her Terminal. |

### Phase 168 -- Always-on "Find a tool" search, reachable from any screen (2026-09-28)

Sohyun: even after Phase 167's smarter search, she still had to drill down several screens deep
to reach a specific tool -- e.g. open a chapter, open the posture checklist, tap a checklist row's
chip -- just to get to "Set up the stool". She asked for the search itself to be redesigned so a
12-year-old could find any tool immediately, from anywhere in the app, not only from inside the
Toolbox tab.

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | Small floating "find" button (🔎), visible on every teacher-mode screen | `drills.html`, new `FindButton`, rendered in `App()` right after the header, above the tab switcher | Fixed bottom-right, so it's reachable mid-checklist, mid-lesson-plan, or on a tool page -- no need to first navigate back to the Toolbox tab. |
| 2 | Full-screen search overlay: one big input, instantly-tappable results, no filters to learn first | `drills.html`, new `FindOverlay` | Empty state shows the 12 topic chips as a browse fallback; typing shows up to 40 matching tools as large rows (title + one-line blurb + color dot); tapping a row jumps straight to that tool and closes the overlay. |
| 3 | Search logic unified | `drills.html`, new `toolHay(t)` / `toolMatches(t, words)`, used by both `FindOverlay` and the existing Toolbox tab's own search box | The Phase 167 `CHAPTER_SEARCH_TERMS` aliases ("time signature", "minim", etc.) now work identically everywhere a tool can be searched for, not just inside the Toolbox tab. Refactor only -- the Toolbox tab's own search box behaves the same as before, re-verified below. |
| 4 | Verification | -- | Babel compile + `node --check` (0 errors). Live Playwright pass: opened the app, navigated into the Plan tab (a screen away from Toolbox), confirmed the 🔎 button is visible there too, opened the overlay, searched "stool" and confirmed "Set up the stool" was the only result and tapping it landed directly on that tool; searched "minim" and got the same 6 tools as the Toolbox tab's own search; re-ran the Toolbox tab's own search box with "time signature" to confirm the shared-code refactor didn't regress it (still 16 tools, matching Phase 167). Zero console/page errors in any of these. |
| 5 | Committed, not pushed | see git log | Ready for Sohyun to push from her Terminal. |

### Phase 169 -- "Whole chapter" jump from every search result (2026-09-28)

Sohyun: after Phase 168's find overlay, a search hit still only opened the one small tool --
there was no way to also see the whole chapter around it, the way tapping a chip in the Exam
ladder opens that chapter's full step-by-step lesson. She wanted that same one-tap access
directly from search results, in both the Toolbox tab's own search and the new find overlay.

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | "Whole chapter: <name> ->" button on every tool result card | `drills.html`, `ToolCard` (now takes an `onChapter` prop), used by the Toolbox tab's category grid, its Student-kit tool list, and `KitView` | Only shown when the tool actually belongs to a chapter (same check `ToolView`'s existing "Learn the whole chapter" link already used). Restructured the card so this is a second, separate button rather than a click target nested inside the card's main button. |
| 2 | Same jump inside the Phase 168 find overlay | `drills.html`, `FindOverlay` | Each result row now shows the same "Whole chapter" button under it when applicable. |
| 3 | Shared navigation helper | `drills.html`, `App()`'s new `jumpToChapter(id)` | Closes the find overlay if open, then opens that chapter's full Learn view (same place "Learn the whole chapter" already goes to from inside a single tool). |
| 4 | Caught my own shadowing bug before shipping | `ToolCard` | Its `t` prop (the tool object) shadows the app's global `t(en, ko)` translator, so the new chapter-button label was switched to read `LANG` directly instead of calling `t()`, which would have thrown. |
| 5 | Verification | -- | Babel compile + `node --check` (0 errors). Live Playwright pass: searched "major" in the Toolbox tab, clicked a result's "Whole chapter: Intervals ->" and landed on the full Intervals chapter; searched "minim" in the find overlay, clicked its "Whole chapter: Notes & Rests ->" and landed on the full 8-step Notes & Rests chapter. Zero console/page errors either time. |
| 6 | Committed, not pushed | see git log | Ready for Sohyun to push from her Terminal. |

### Phase 170 -- One "Whole chapter" link per chapter group, not per card (2026-09-28)

Sohyun: Phase 169's "Whole chapter" button, repeated on every single result card, looked
"정신없게" (overwhelming/cluttered) -- most cards in the same category or search result already
share the same chapter, so the same button was repeating over and over. She asked for it to sit
once at the top of each chapter's group instead, the way the Exam ladder shows one heading per
grade with its chips underneath.

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | New `ChapterGroups` helper: groups a list of tools by the chapter they belong to (`t.ch`) and renders one "Whole chapter: <name> ->" link above each group's card grid | `drills.html`, new `ChapterGroups` component | `ToolCard` itself went back to having no chapter button at all (reverted the Phase 169 per-card button) -- it's a plain card again. |
| 2 | Applied everywhere tool grids are shown | `Toolbox`'s per-category grid, its Student-kit tool list, `KitView` | All three now render through `ChapterGroups` instead of a flat `.map` of `ToolCard`. |
| 3 | Same grouping in the find overlay | `FindOverlay` | Search results are grouped by chapter with one header per group above its rows, instead of a button under every single row. |
| 4 | Verification | -- | Babel compile + `node --check` (0 errors). Live Playwright pass: confirmed the Posture & Hands category now shows one "Whole chapter" link per chapter (2 groups: "Posture, Hands & Black Keys" and "Five-Finger Positions") instead of one per card; searched "chord" in the find overlay and confirmed results split into "The Piano's Story" / "Intervals" / "Chords" / "Dynamics & Articulation" groups, each with one header; clicked a header and landed on that chapter's full Learn view; re-ran the student-kit star/add flow (add a student, star two tools) and confirmed the kit panel still groups and displays correctly. Zero console/page errors. |
| 5 | Committed, not pushed | see git log | Ready for Sohyun to push from her Terminal. |

### Phase 171 -- Toolbox visual pass: calmer, less "조잡한" (cluttered) look (2026-09-28)

Sohyun: even after Phases 168-170's search/navigation fixes, the Toolbox tab overall still
looked too cluttered ("조잡해 보여"). The root cause: the 12 TOOL_CATS colors (already used as
informational category coding, same idea as the site's era/syllabus badges per the
piano-butler-designer brand skill) were being used THREE times at once on one screen -- as solid
-fill button backgrounds, as saturated all-caps section headings, and as card left-borders --
which reads as a wall of competing hues rather than a coherent page. Brought this in line with
the confirmed "Ink & Brass" system (ink for interactive chrome, category color as a quiet
identifier only, brass reserved for one special action) instead of re-deriving a new palette.

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | Category "jump" chips: solid saturated fill -> outlined pill with a small color dot + ink text | `drills.html`, new `.cat-pill`/`.cat-dot` CSS classes, used in the Toolbox tab's top row and the find overlay's empty-state topic chips | Category color still there as a quick visual anchor, just no longer shouting as a full-color button. |
| 2 | Category section headings: bold all-caps text in the category's own saturated color -> ink heading + small color dot + thin bottom rule | `drills.html`, Toolbox's per-category `<div>` | This was the single biggest source of the "rainbow wall" scrolling down the tab -- 12 different hues as page headings, one after another. |
| 3 | "Whole chapter" links (Phase 169/170): inconsistent colors (category color in the Toolbox tab, hardcoded brass in the find overlay) -> one shared `.chapter-link` brass pill everywhere | `drills.html`, `ChapterGroups` and `FindOverlay` | Matches the brand rule that brass marks one special action consistently, not a different color per context. |
| 4 | Tool cards: harder 4px color bar + flat look -> slimmer 3px bar, soft card shadow, more padding/line-height, larger gap between cards | `drills.html`, `ToolCard` | Small but repeated 30+ times per scroll, so it compounds -- matches the design skill's note that a repeated-card page needs to be tested at full-page density, not as a single swatch. |
| 5 | Search input: browser-default blue focus ring -> ink focus ring matching the rest of the site's interactive chrome | `drills.html`, new `.search-input` CSS class, used by the Toolbox tab's search box | The find overlay's own search box keeps its brass border/ring on purpose (it's the one "special" global action, per the brand rule that brass marks something singular). |
| 6 | Verification | -- | Babel compile + `node --check` (0 errors). Live Playwright pass: re-ran the category-pill jump, the inline Toolbox search + star-to-kit flow, and a "Whole chapter" jump -- all still work exactly as before, just restyled. Zero console/page errors. |
| 7 | Committed, not pushed | see git log | Ready for Sohyun to push from her Terminal. |

### Phase 172 -- Merged Plan + Toolbox into one tab; Practice/Students pushed later (2026-09-28)

Sohyun: didn't see why Plan and Toolbox needed to be two separate tabs -- they're really one
workflow (pick a student, then find a tool for them) -- and asked for them to be merged and
"professionally" arranged, with Practice and the Students tab pushed later in the tab order.

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | Tab bar: 4 tabs (Plan, Students, Toolbox, Practice) -> 3 (Plan, Practice, Students) | `App()`'s tab array | The standalone "Toolbox" tab is gone; its content now lives inside Plan. |
| 2 | Toolbox appended to the bottom of the Plan screen | `PlanView`, new "ALL TOOLS" section divider + `<Toolbox .../>` | Kept Plan's existing top-to-bottom order (student picker -> first mix -> today's mix -> progress -> exam ladder) and added the full searchable/browsable tool library underneath, rather than interleaving everything into a new order -- lower-risk and still answers "why do I need a separate tab for this." |
| 3 | `Toolbox` is now a controlled component: no more independent copy of "current student" | `Toolbox` (removed its own `kits`/`kitIdx` state and its "Student kits" builder card entirely), `PlanView` (now owns `star()`/`copyKit()`, passes `kit`/`onStar` down) | Before this, Plan and Toolbox each loaded their own copy of the same underlying student-kit data on mount -- fine when they were separate tabs (each remount re-synced), but showing both on one screen at once could have let them drift out of sync (e.g. switching student at the top not updating which kit "☆" stars into, lower down). One shared state now; starring a tool anywhere on the page updates the same "Open <student>'s kit" panel at the top. |
| 4 | "Open kit" / "Copy student link" buttons moved from Toolbox's old panel to Plan's top card | `PlanView` | Same actions, now next to the student picker they act on instead of a second card further down. |
| 5 | Back-navigation fixed for the merged structure | `App()`: find-overlay jump and the kit-view back button now target `view:'path'` (Plan) instead of the now-removed standalone Toolbox destination | A stray old bookmark with `?view=tools` still renders something reasonable (falls through to Practice) rather than erroring. |
| 6 | Verification | -- | Babel compile + `node --check` (0 errors). Live Playwright pass: confirmed the new 3-tab bar (Plan/Practice/Students); added a student, starred a tool from the bottom toolbox section, and confirmed the top "Open <name>'s kit" button updated to show it (same state, no desync); opened a tool from the merged toolbox and from the global find overlay and confirmed both back-buttons correctly return to "Lesson plan"; opened a kit and confirmed its "← Plan" back button returns correctly; confirmed Practice and Students tabs still render. Zero console/page errors. |
| 7 | Committed, not pushed | see git log | Ready for Sohyun to push from her Terminal. |

### Phase 173 -- Modes/Chord Extensions pedagogy pass + Plan/Toolbox search-first layout (2026-09-28)

Sohyun: wanted Modes and Chord Extensions made understandable for a 12-year-old before moving on
to translation, with hands-on activity filled in wherever a tool was just informational, tool
order checked pedagogically, and -- in the merged Plan/Toolbox screen from Phase 172 -- the search
reachable at the very top, questioning whether Lesson Plan needed to compete with it for space.

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | Modes: kid-friendly "stops on a loop" analogy + hands-on tap keyboard | `Modes()` | Kept the existing brightest-to-darkest explanation but added a concrete anchor: "Ionian starts the ride at C, Dorian starts the same loop at D." Added a `TapKeyboard` below the staff/Hear-it button marking the mode's 8 notes (labelled 1-8) so a student can play it themselves instead of only auto-listening -- previously the only interaction was clicking buttons and pressing play. Bilingual (EN/KO). |
| 2 | Chord Extensions: "stacking donuts past the octave" analogy + hands-on tap keyboard | `ChordExtensions()` | Same fix, same reasoning -- this was the one tool in the Chords chapter with no way to physically try the notes (7th Chords already had one). Added a marked `TapKeyboard` for the current stack. Bilingual (EN/KO). |
| 3 | Reordered Scales & Keys tool group | `TOOLS` array | "The seven modes" (`TOOL_META` already flags it level 3, the most advanced scales tool) was listed *before* Build a major scale, Build a harmonic minor and Scale finder -- backwards for a student meeting modes for the first time. Moved it to render after all three. Chords group's order (basic triads -> 7th chords -> extensions) was already correct, left unchanged. |
| 4 | PlanView: search moved to the top, Lesson Plan collapsed | `PlanView` | Reordered the screen: a compact student switcher, then the full `<Toolbox/>` (search + category browse), now render first -- reachable the instant the tab opens. The strand progress tracker (today's mix, strand tracker, Exam ladder, Anytime, All chapters) is kept, since it's real curriculum-progress data with no other home, but now sits behind a "Lesson plan ▾" toggle, closed by default, instead of pushing the tool library down the page. |
| 5 | Verification | -- | Babel compile (`@babel/standalone`) + `node --check` (0 errors). Live Playwright pass: confirmed the search input renders near the top of the Plan tab (well above the tool category list) and the Lesson Plan section is absent from the DOM until the toggle is clicked, then reappears on toggle; confirmed "The seven modes" now renders after Build a major/minor scale within Scales & Keys; opened both Modes and Chord Extensions, confirmed their new `TapKeyboard`s render and respond to a tap with zero console/page errors; re-ran the Modes tool with the Korean toggle on and confirmed the new analogy text and tap-keyboard label render correctly in Korean. |
| 6 | Committed, not pushed | see git log | Ready for Sohyun to push from her Terminal. |

### Phase 174 -- Fix Modes ordering confusion + add real-music examples per mode (2026-09-28)

Sohyun, right after Phase 173's Modes redesign: "아이오니안 먼저 아니야? 아직도 헷갈려 예시가 좀 필요할
것 같아" -- the brightness-order list put Lydian (a name she'd never heard) before Ionian (the
ordinary major scale she already knows), which read as a mistake, and the mood-word descriptions
alone ("bluesy, folky") weren't concrete enough to make each mode click.

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | Ionian visually anchored as the list's pivot | `Modes()` | Kept the brightness-ladder order itself (a real, deliberate teaching choice from Phase 165 -- each neighbour differs by exactly one note) but now gives Ionian a gold border + "★ you know this one" badge, with explicit "↑ BRIGHTER THAN THE MAJOR SCALE" / "↓ DARKER THAN THE MAJOR SCALE" headers splitting the list above and below it -- its middle position now reads as intentional, not backwards. |
| 2 | Intro text states the pivot directly | `Modes()` | Now says outright: "Ionian IS the ordinary major scale you already know -- it's the middle of this list on purpose." |
| 3 | Real-world "Sounds like: ..." example per mode | `MODES` array (new `exEn`/`exKo` fields), shown in the detail box | One concrete line per mode -- nursery rhymes for Ionian, classic rock riffs for Mixolydian, flamenco guitar for Phrygian, a few tense horror-score seconds for Locrian, etc. -- updates with the selected mode. Bilingual. |
| 4 | Verification | -- | Babel compile + `node --check` (0 errors). Live Playwright pass in both languages: confirmed the brighter/darker headers and Ionian badge render, confirmed the example line updates on selecting a different mode (tested Locrian), confirmed Korean renders with no mangled characters. Caught and fixed a real mistake during this pass: a first draft hand-typed `\uXXXX` escapes for the new Korean strings and mistyped one (`\ubaham` -- not valid hex), which would have thrown a JS syntax error; switched to literal Korean text (the convention the rest of the file already uses) before committing. |
| 5 | Committed, not pushed | see git log | Ready for Sohyun to push from her Terminal, along with Phase 173. |

### Phase 175 -- Switch Modes to scale-degree order (2026-09-28)

Sohyun, a second time, on Phase 174's brightness-anchored list: "이게 왜 이순서야 아이오니안, 도리안
이순서로가야하는거아냐?" -- the brightness-ladder order (each neighbour differs by one note -- a real
theory idea from Phase 165) kept reading as wrong no matter how clearly Ionian's position was
explained/badged. Rather than patch the explanation a third time, switched to what she actually
expects, which is also the far more standard way modes are taught.

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | Reordered `MODES` to scale-degree order | `MODES` array | Ionian, Dorian, Phrygian, Lydian, Mixolydian, Aeolian, Locrian -- built on the major scale's 1st note, then 2nd, then 3rd... Each mode's `start` field already *is* its scale-degree index (0-based), so this is just the array sorted by `start`; no other data changed. |
| 2 | Ordinal badge replaces brighter/darker headers | `Modes()` | Each row now shows "1st / 2nd / 3rd..." instead of Phase 174's "↑ brighter" / "↓ darker" group headers, which described an order the list no longer uses. Ionian keeps its "★ you know this one" star, now naturally the first row instead of needing a pivot position explained. |
| 3 | Intro text restated | `Modes()` | Now says the actual organizing idea directly: "starting on the 1st note of the major scale gives Ionian... the 2nd note gives Dorian... up to the 7th, Locrian." |
| 4 | Kept from Phase 173/174 | -- | The per-mode "Sounds like: ..." real-music example and the hands-on tap keyboard are unchanged -- only the ordering/framing changed. |
| 5 | Verification | -- | Babel compile + `node --check` (0 errors). Live Playwright pass in both languages: confirmed the 7 rows render in exact scale-degree order (1st Ionian through 7th Locrian), confirmed Ionian's badge, confirmed selecting a different mode (Dorian) still updates the staff/keyboard/example with zero console errors. |
| 6 | Committed, not pushed | see git log | Ready for Sohyun to push from her Terminal, along with Phases 173-174. |

### Phase 176 -- Friendlier, analogy-driven explanations across the Chords chapter (2026-09-28)

Sohyun: "코드, 7화음, 익스텐션도, 건반화성 페다고지 교수님처럼 친절하게 잘 설명해줘 머리 뽀개지지
않게" -- wanted every tool in the Chords chapter explained as simply and memorably as the Modes
rework (Phases 173-175), with analogies rather than dry theory language.

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | Rewrote intro text with concrete analogies, bilingual (EN/KO), in all 6 remaining Chords tools | `TriadStacker`, `MajorMinorFlip`, `KeyChords`, `PrimaryTriads`, `InversionFlip`, `CadencePlayer` | Stack a triad = 3-layer cake / snowman. Major or minor = a face (smile vs. the same face with the corners of the mouth down). A triad on every note = a family photo of seven siblings built the same recipe, plus a new highlighted memory-tip box ("I, IV, V are the big siblings; ii, iii, vi are the middle ones; vii° is the odd one out"). Primary triads I/IV/V = home / stepping out for a walk / standing at the door itching to go back in. Inversions = three friends holding hands, whoever's at the front walks to the back. Cadences = sharpened the existing punctuation analogy (period / hymn's "Amen" / comma / plot twist). |
| 2 | Real bug caught and fixed, same class flagged in Phase 146/149/159 | `MajorMinorFlip` | Had a local `const t = [...]` (the triad array) shadowing the global `t(en, ko)` translator -- the new bilingual calls would have thrown "t is not a function." Live Playwright caught it immediately on first open. Renamed the local variable to `tri` throughout (5 usages), not just the call sites. Audited the other five tools for the same risk before shipping: `KeyChords`/`PrimaryTriads` do have `.map((t, i) => ...)` callbacks with a `t` parameter, but confirmed safe -- the new `t()` calls sit in the component body above those callbacks, not inside their arrow-function bodies. |
| 3 | Verification | -- | Babel compile + `node --check` (0 errors). Live Playwright pass opened all 8 Chords-chapter tools (the 6 rewritten here plus 7th Chords/Beyond the 7th from Phase 173, spot-checked for regressions) with zero console/page errors, in both English and Korean. |
| 4 | Committed, not pushed | see git log | Ready for Sohyun to push, along with Phases 173-175. |

### Phase 177 -- Visual-first pedagogy: icon badges + reactive illustrations for Chords (2026-09-28)

Sohyun, after seeing the visual-guide-ideas mockup: "응 단순하게 셋 다 같이 가게. 그리고 코드 뿐만이
아니라 모든 챕터가 설명이 많은 것보다 시각적으로 딱 이해가기 쉽게 만드는게 먼저 우선순위야." --
combine all 3 mockup concepts, and treat "show, don't just explain, with fun/memorable elements
everywhere" as the standing top priority for every remaining chapter, not just Chords. This phase
implements all 3 concepts in the Chords chapter as the first rollout; the wider rollout is tracked
as its own pending item below.

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | Icon badges on the Toolbox list | `TOOL_ICON` lookup (new, before `ToolCard`), wired into `ToolCard` | Small inline SVGs for all 8 "Intervals & chords" tools: stacked colored blocks for Stack a triad, a smiley/frown face for Major or minor, a family-of-circles for Chords in a key, a house for I/IV/V, three linked circles for Inversions, a "." "," glyph for Cadences, stacked bars for 7th chords, dots-on-a-line for Extensions. Cards without an icon render exactly as before (conditional padding/gap). |
| 2 | Reactive face | `MajorMinorFlip()` | A face SVG above the root-chip row whose mouth path morphs between a smile (major) and a frown (minor) on toggle, colored via `Q_COL`, with a CSS transition on both `d` and `stroke`. |
| 3 | Reactive building cake | `TriadStacker()` | A 3-layer cake SVG above the `ChordStaff` whose layers fade/scale in as the root, 3rd, and 5th are added (`n` state), with a brass "cherry" circle appearing once the triad is complete at `n===3`. |
| 4 | Static leading icons | `KeyChords`, `PrimaryTriads`, `InversionFlip`, `CadencePlayer` | Small SVGs added to each tool's own `actTitle` line so the icon appears both in the Toolbox list and again inside the opened tool. |
| 5 | Verification | -- | Babel compile + `node --check` on the extracted app script (0 errors). Live headless-Chromium Playwright pass: confirmed all 8 icon badges render in the Toolbox list; opened Stack a triad and stepped through +Add the 3rd/+Add the 5th, confirming the cake layers fade/scale in correctly and the triad quality readout updates; opened Major or minor chord and toggled Major -> Minor, confirming the face's mouth path morphs from smile to frown with zero console/page errors; opened Chords in a key, I/IV/V, Inversions, and Cadences and confirmed the new static icons render without layout breakage; re-ran the triad-stacking and Major/minor tools in Korean, confirming the existing bilingual `actNote` text and new SVG text labels render correctly with zero errors. No `t()`-shadowing issues introduced (the well-documented recurring bug class from Phases 146/149/159/176) -- none of the new icon or illustration code references the translator inside a shadowed scope. |
| 6 | Committed, not pushed | see git log | Ready for Sohyun to push, along with Phases 173-176. |

### Phase 178 -- Visual-first pedagogy rollout to Intervals (2026-09-28)

Continuing the standing priority from Phase 177 (see Pending work #19): applying the same
icon-badge + reactive-illustration treatment to the next chapter in curriculum order.

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | Icon badges on the Toolbox list | `TOOL_ICON` (7 new entries) | A ladder (lines/spaces) for Interval ruler, dots-on-a-ring for Hop round the letters (echoing `LetterWalker`'s own circular hop visual), two piano keys with a connecting arc for Count the semitones, an ascending staircase for the major-scale shortcut, a stylized ear with sound waves for Hear the intervals, two linked dots for Invert an interval, and a violet zigzag "tension" line between two dots for The tritone (violet matching the existing diminished-chord color used elsewhere in the file). |
| 2 | Reactive flip diagram | `IntervalInverter` | A small two-dot SVG above the staff whose dots swap vertical position and color when the interval is inverted, so the visual literally shows "the bottom note moves to the top." |
| 3 | Reactive tension line | `TritoneTool` | A zigzag line between the two note dots that redraws when toggling between the augmented 4th and diminished 5th spellings. |
| 4 | Reactive step-meter | `SemitoneCounter` | A row of brass squares above the keyboard that fills in one at a time as semitones are counted, reusing the component's existing `step`/`s` state -- no new state added. |
| 5 | Static leading icons | `IntervalRuler`, `MajorScaleIntervals`, `IntervalEar` | Same pattern as Phase 177's static-icon tools. |
| 6 | Real bug caught and fixed before commit | `IntervalInverter` | First draft had the reactive dot diagram's vertical positions backwards -- the bottom note's dot was drawn above the top note's dot (and vice versa after flipping), contradicting the actual staff rendering directly below it. Caught by comparing the live screenshot against the `IntervalStaff` colors/positions, not just by re-reading the code. Fixed by swapping the `cy` formulas so the dot diagram's up/down layout always matches the staff. |
| 7 | Verification | -- | Babel compile + `node --check` (0 errors). Live Playwright pass: all 7 icon badges confirmed rendering; Invert an interval opened and flipped, confirming the (fixed) reactive diagram matches the staff in both states; The tritone opened and toggled between both spellings with zero console errors; Count the semitones run through a full auto-count cycle, confirming all 4 step-meter squares fill for C-E (major 3rd); the three static-icon tools opened with no layout issues; Invert an interval and The tritone re-checked in Korean, zero errors (these three components don't yet use the bilingual `t()` helper -- translation backlog, unchanged here -- so no shadowing risk applies). |
| 8 | Committed, not pushed | see git log | Ready for Sohyun to push, along with Phase 177 and earlier. |

### Phase 179 -- Group articulation (tie/slur, staccato, legato) with legato-first order (2026-09-28)

Sohyun: "타이 슬러, 스타카토, 레가토 이런 아티큘레이션으로 한 곳에 묶여야 될 것 같기도 한데 이거
섹션을 좀 잘 고려해서 넣자. 처음에 배울때부터나는 레가토 개념 기본으로 깔고 가져가거든, 좀 나중에
스타카토 들어가고" -- these three articulation concepts were scattered across three different
Toolbox chapters, and the built-in ordering put staccato before legato, backwards from how she
actually teaches it.

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | Regrouped into one chapter | `touch-lengths` (`ch: 'piano-story'` -> `'dynamics'`), `tie-slur` (`ch: 'signs'` -> `'dynamics'`) | All 6 touch/dynamics tools (Line up the dynamics, Which touch?/How loud?, The sustain pedal, Draw a hairpin, Legato/non legato/staccato, Tie or slur?) now list together under one "Whole chapter: Dynamics & Articulation" heading in the Toolbox -- that chapter's existing label already names articulation, so this is its natural home, not a new chapter. `piano-story` (now keyboard-ancestors, piano-timeline, eras) and `signs` (now road-map, grace-write, ornaments, ottava) both stay coherent without it. |
| 2 | Legato-first ordering | `ARTICS` array, `EAR_TOUCH` option lists | `ARTICS` reordered to Legato, Tenuto, Accent, Staccato, Staccatissimo, Fermata -- this drives the Dynamics lesson's Articulation step, its quiz level, and the touch/ear listening game, so the change propagates everywhere articulation is taught or tested. |
| 3 | Tie/slur pulled into the lesson itself | `DynLearn`'s "Articulation" `Step` | Added a short explainer ("a slur is what legato looks like on the page...") plus `<TieOrSlur/>` directly below the Legato-first list, so the connection is made inside the guided Learn flow, not just via the Toolbox filter. |
| 4 | Visual-first pass on the regrouped chapter | `TOOL_ICON` (6 new entries), 5 static `actTitle` icons | Ascending bars for Line up the dynamics, a crescendo wedge for Draw a hairpin, a pedal glyph for The sustain pedal, a slur-vs-staccato-dot contrast icon for Legato/non legato/staccato, a curve-over-two-dots icon for Tie or slur?, an ear+note icon for Which touch?/How loud? (badge only -- its actTitle toggles between two labels, so no fixed static icon). |
| 5 | Bonus bug caught live | `TOOL_META` (8 entries: count-more, grouping, rest-grouping, duplets, grace-write, alto-clef, ornaments, chromatic, pedal) | All had `hi: 4`, but the level-display arrays (`LO`/`HI` in `ToolCard`) only have indices 0-3 -- silently rendered as "G1-undefined" on the card. Fixed all 8 to `hi: 3`; confirmed live (the sustain-pedal card now correctly shows "G1-G4"). |
| 6 | Verification | -- | Babel compile + `node --check` (0 errors). Live Playwright pass: confirmed the regrouped Toolbox listing; opened the Dynamics lesson directly (`?drill=dynamics&tab=learn`) and confirmed Legato-first ordering plus the embedded Tie-or-slur tool render correctly; confirmed the "G1-undefined" bug is fixed; zero console/page errors throughout. |
| 7 | Committed, not pushed | see git log | Ready for Sohyun to push, along with Phases 177-178. |

### Phase 180 -- Bigger, more literal icons (fixing Phase 177-179's icon pass) (2026-09-28)

Sohyun, looking at the Interval ruler card specifically: "이것의 용도를 아직 잘 모르겠어. 시각화
버튼에 해주니 좋은데 아이콘들이 더 컸으면 좋겠고, 시각적인걸 교육적으로 풀어내는 방법을 찾으라는
말이야." Two real problems with the icon work so far: too small to read at a glance, and a few icons
leaned on an abstract or punny metaphor instead of directly showing what the tool teaches.

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | Bigger everywhere | `ToolCard` badge container (26x26 -> 40x40, inner svg 22 -> 34), all 12 static `actTitle` icons (unified to 28x28, was an inconsistent 20x20/24x24 mix left over from doing 3 chapters separately) | viewBox stayed `0 0 24 24` throughout, so every existing icon just scales up cleanly -- no path redrawing needed for the 18 icons that were already clear enough to keep. |
| 2 | Interval ruler icon redesigned | `TOOL_ICON['interval-ruler']` and its actTitle instance | Was an unlabeled ladder shape with no obvious connection to the tool. Now a vertical line with an ink dot (bottom note) and a brass dot (top note), with tick marks between -- directly depicts "measure the gap, count the steps," which is literally the tool's job. |
| 3 | Cadences icon redesigned | `TOOL_ICON['cadences']` and its actTitle instance | Was a bare ".," text glyph -- a stretch metaphor for "punctuation" that didn't read as intended. Now a real double barline (thin + thick line), the actual notation symbol students already know means "the end." |
| 4 | Inversions icon redesigned | `TOOL_ICON['inversions']` and its actTitle instance | Was three static circles on a flat line. Now the same three circles with a curved, arrowed line from the bottom circle arcing up and over to the top -- directly shows "move the bottom note to the top," the tool's own description, instead of just implying "these three notes are related." |
| 5 | Verification | -- | Babel compile + `node --check` (0 errors). Live Playwright pass across Intervals and Chords at the new sizes: confirmed no layout breakage, confirmed via cropped screenshots that the interval-ruler, cadences, and inversions icons now read as literal depictions rather than abstract shapes, zero console/page errors. |
| 6 | Design principle updated | `piano-butler-designer` skill (proposed) | Recorded as refined guidance for the remaining chapters (Signs & terms next): icons must be sized generously, not decoratively small, and must directly depict the tool's own mechanism or the real notation symbol it teaches -- never an abstract or punny metaphor that needs its own explanation. |
| 7 | Committed, not pushed | see git log | Ready for Sohyun to push, along with Phases 177-179. |

### Phase 181 -- New chapter: Melody & Phrasing (2026-09-28)

Sohyun shared the table of contents of a reference book, "Help Your Kids with Music -- A Unique
Step-by-Step Visual Guide" (PDF placed in the Piano Butler folder), and asked for a concise
gap-analysis of drills.html against it (skipping the book's Ch.7, Instruments and Voices), then to
start filling in what's missing, beginning with whichever new chapter she picked.

**Gap analysis (reported to Sohyun in chat, not duplicated in full here):** the book's Ch.1-3, 5, 9
map onto drills.html's existing 21 chapters reasonably well (with some sub-topics thinner than the
book -- relative minor/circle of fifths/modulation, cadences/chord symbols, etc., left for later).
Three of the book's chapters have **no drills.html equivalent at all**: Ch.4 Melody, Ch.6 Form,
Ch.8 Styles & Genres. Sohyun chose Melody first.

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | New chapter `melody` | `DRILLS` (new entry), `MELODY_DRILL` concept object | Dynamics/articulation/pedal/ties are also part of the book's Melody chapter but were already covered by the existing `dynamics` chapter (Phase 179), so this chapter covers only the genuinely new content: what a tune is (rhythm + pitch), phrase marks, question-and-answer phrases, and sequences. |
| 2 | 4-step Lesson | `MelodyLearn`, `TuneAnatomy`, `PhraseBreath`, `QuestionAnswer`, `SequenceStepper` | Reuses `MelodyStaff` (built for Phase 141's "Complete the melody") for real notation rather than inventing a new renderer. `TuneAnatomy` toggles "Twinkle Twinkle" between rhythm-only (same pitch, real durations), pitch-only (real pitches, uniform durations, no time signature or bar lines -- a literal match to the book's own illustration), and both together. `PhraseBreath` plays each of two phrases and fades in a comma at the phrase-mark's end once playback finishes. `QuestionAnswer` plays a 3-note lead-in plus a varying ending (scale degree 1 = answer/resolved, 2/4/5/7 = question/unstable) and checks the student's guess. `SequenceStepper` reveals a 2-note motif transposed up a step, up to 3 times, with the staff visibly growing as each repetition is revealed. |
| 3 | Matching 4-kind quiz | `MELODY_LEVELS`, `genMelodyQuestion`, `MelodyQuestion` | Same generate/check/Question contract as every other chapter's concept object; verified live through all 4 levels including right/wrong feedback text. |
| 4 | 4 new Toolbox tools, built to the Phase 180 standard from the start | `TOOLS` (`ch: 'melody'`), `TOOL_ICON` (34px badges + 28px actTitle icons), `TOOL_META`, new `TOOL_CATS` entry ("Melody & phrasing"), `CHAPTER_SEARCH_TERMS`, `GRADE_TAGS`, `STAGES` (added to "Reading music") | No later size/clarity correction pass needed this time -- icons sized generously from the start and each depicts its own tool's mechanism: a phrase-mark arc over three notes, a dashed circle+"?" vs. solid circle+check for unstable/stable phrase endings, and a climbing staircase of note pairs for sequences (matching the tool's own on-screen visual). |
| 5 | Verification | -- | Babel compile + `node --check` (0 errors). Live Playwright pass: all 4 Toolbox tools opened and interacted with (mode toggles, phrase playback + breath-mark reveal, question/answer guess with feedback, sequence reveal), the full 4-step lesson page, and the drill quiz through several questions with right/wrong feedback -- zero console/page errors throughout. |
| 6 | Committed, not pushed | see git log | Ready for Sohyun to push, along with Phases 177-180. |

### Phase 182 -- New posture tool: Arm Weight & Alignment (2026-09-28)

Sohyun shared the complete source of a self-authored standalone tool ("Technic.html" -- a
biomechanical arm/wrist/finger alignment visualizer with inverse-kinematics rendering) and asked
for it to be ported into drills.html, in the appropriate posture-related place -- ahead of
continuing the reference-book gap-fill (Form / Styles & Genres, still undecided, see Pending #20).

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | Ported IK arm-pose logic 1:1 | `calcElbowIK`, `computeArmPose`, `armDiagnosis` (new `function` declarations, hoisted -- placed before `const TOOLS = [` since only referenced at render time, avoiding the Phase 181 TDZ mistake) | `computeArmPose` clamps seating distance and wrist height from mouse/touch position, derives elbow position via law-of-cosines IK and finger-arch factor from wrist height, and classifies elbow state (tucked / reaching / free) and wrist state (high / collapsed / good). `armDiagnosis` maps every state combination to bilingual diagnosis text, colors, and title, reusing the Ink & Brass palette (`--good`/`--bad`/`--brass`). |
| 2 | New component `ArmAlignment` | before `const TOOLS = [` | Renders a dark, responsive `viewBox="0 0 900 560"` SVG (torso, keyboard, weight-vector paths, arm bones, finger bones, joints, all driven by the diagnosis) with a semi-transparent status-panel overlay. Adds mouse *and* touch support (the original vanilla-JS tool was mouse-only). |
| 3 | Wired into First Steps lesson | `FirstStepsLearn` -- new `<Step title="Feel the arm weight">` inserted immediately after the existing "Move with the whole arm" step | Chosen as the most thematically exact existing posture location; confirmed via live Playwright screenshot that it renders correctly embedded between "Move with the whole arm" and "Posture check". |
| 4 | New Toolbox tool | `TOOLS` (`id: 'arm-alignment', ch: 'first-steps'`), `TOOL_ICON` (34px badge, literal elbow/wrist bend path), `TOOL_META` (`['body', 0, 3, 'show']`) | Follows the Phase 180 icon standard (generously sized, depicts the tool's own mechanism -- a bent arm path with two joint dots -- rather than an abstract metaphor). |
| 5 | New skill-checklist entry | `SKILLS` -- `['b7', 'body', 'Feels arm weight sink through a relaxed wrist into the key', ['arm-alignment']]` | Separate "can-do" progress taxonomy from `TOOL_CATS`; this is the first tool wired to a `SKILLS` entry this session. |
| 6 | Verification | -- | Babel compile + `node --check` (0 errors). Live Playwright pass: opened the tool directly and moved the pointer through four distinct diagram states (good alignment, wrist too high, wrist collapsed, elbow tucked -- seating too close), confirming diagnosis text/colors update correctly each time with zero console/page errors; separately opened the First Steps guided lesson and confirmed the new "Feel the arm weight" step renders correctly in place. Screenshots visually spot-checked for all 4 states plus the full lesson page. |
| 7 | Committed, not pushed | commit `853bdfc` | Ready for Sohyun to push, along with Phases 177-181. |

### Phase 183 -- New chapter: Musical Form (2026-09-28)

Sohyun said "proceed in order" (following the Director report's recommendation), resuming the
reference-book gap-fill thread that paused for Phase 182's arm-alignment tool. Built the second
of the three entirely-missing chapters: Ch.6 Form.

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | New chapter `form` | `DRILLS` (new entry), `FORM_DRILL` concept object | Repeats/D.C./D.S./Coda/Fine are already covered in depth by the `signs` chapter (Phase 116), so this chapter skips the book's "Repeats" section entirely and covers only the genuinely new content: how a piece is organized into sections -- binary (AB), ternary (ABA), rondo (ABACA) -- telling a repeated section from a new one by ear, and spotting the returning refrain in a rondo. Counterpoint (rounds/canons/fugues), theme and variations, ostinati/loops/riffs, breaks and fills, and full orchestral forms (symphony/sonata/concerto movements) are more advanced theory/analysis topics, deliberately left for a possible later, deeper chapter -- the same scoping call made for dynamics/articulation in the Melody chapter (Phase 181). |
| 2 | 4-step Lesson | `FormLearn`, `FormShapes`, `SameOrNewSection`, `RondoRefrain`, `BinaryTernarySpot` | Three short *original* motifs (A = home/stable, B = away/unstable, C = second rondo episode, lower register) double as both the audio and the "sections" students compare in every tool -- written fresh rather than reproducing the book's own melodic examples or diagrams. `FormShapes` toggles between binary/ternary/rondo block diagrams (tap a letter to hear it, or play the whole shape). `SameOrNewSection` and `BinaryTernarySpot` are ear-training games (is the next section a repeat or new material; did the opening tune return). `RondoRefrain` is a progressive reveal-and-guess game through the full ABACA sequence. |
| 3 | Matching 4-kind quiz | `FORM_LEVELS`, `genFormQuestion`, `FormQuestion` | Same generate/check/Question contract as every other chapter; verified live through all 4 levels including right/wrong feedback text (e.g. a wrong "Ternary" guess on a rondo example correctly showed "Not quite -- it was Rondo (ABACA)"). |
| 4 | 4 new Toolbox tools, Phase 180 icon standard | `TOOLS` (`ch: 'form'`), `TOOL_ICON` (34px badges + 28px actTitle icons), `TOOL_META`, new `TOOL_CATS` entry ("Musical form"), `CHAPTER_SEARCH_TERMS`, `GRADE_TAGS`, `STAGES` (added to "Reading music", alongside `melody`) | Icons depict their own tool literally: three colored A-B-A blocks for Form Shapes, two overlapping circles (a comparison/Venn shape) for Same-or-New, a loop arrow with "A" for Rondo Refrain, and two stacked rows of 2-vs-3 blocks for Binary/Ternary Spot. |
| 5 | Verification | -- | Babel compile + `node --check` (0 errors). Live Playwright pass: all 4 Toolbox tools opened and interacted with (shape toggling + playback, same/new guess with feedback, full rondo reveal through all 5 blocks, binary/ternary guess with feedback), the full 4-step lesson page, and the drill quiz through several questions with right/wrong feedback -- zero console/page errors throughout. Screenshots visually spot-checked for every tool state plus the full lesson page. |
| 6 | Committed, not pushed | commit `cc8e8e1` | Ready for Sohyun to push, along with Phases 177-182. |

### Phase 184 -- New chapter: Styles & Genres, final book gap-fill chapter (2026-09-28)

Sohyun's "proceed in order" continued straight into the last of the three entirely-missing
chapters from the reference-book gap analysis (item #20): Ch.8 Styles and Genres.

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | New chapter `styles` | `DRILLS` (new entry), `STYLES_DRILL` concept object | Deliberately scoped down from the book's full chapter. The four period sub-sections (Baroque, Classical, Romantic, Modern) are already covered at a glance by `piano-story`'s `eras` tool, so they're not repeated here -- doing so would duplicate rather than deepen (flagged from the start of item #20). Real audio identification of folk/jazz/pop recordings was ruled out: the app has no licensed audio library for that, and fabricating "genre-typical" synthesized audio would be misleading rather than educational. What's left, genuine, and buildable: musical texture (monophony/homophony/polyphony), and the defining conceptual traits that separate folk, classical, jazz & blues, and popular music. |
| 2 | 3-step Lesson | `StylesLearn`, `TextureTypes`, `TextureSpotter`, `GenreTraits` | The texture demo is *real* audio, not faked -- `playHomophony` uses `blip()`/the pattern from the existing `playChord` to sound a genuine sustained triad simultaneously under the melody, and `playPolyphony` schedules two independently-timed voices (a canon-like second entrance) so the ear actually hears two interweaving lines, not sequential notes relabeled. All three reuse `FORM_MOTIF` (from the Form chapter, Phase 183) as the same raw tune treated three ways, so the comparison is apples-to-apples. `GenreTraits` is a definitional reference (four style families and what sets each apart), not an audio quiz, since no genre-authentic audio exists in the app. |
| 3 | Matching 3-kind quiz | `STYLES_LEVELS`, `genStylesQuestion`, `StylesQuestion` | Same generate/check/Question contract as every other chapter; level 2 ("Listen and identify") reuses the same real audio playback as the Texture Spotter tool. Verified live through all 3 levels including right/wrong feedback text. |
| 4 | 3 new Toolbox tools, Phase 180 icon standard | `TOOLS` (`ch: 'styles'`), `TOOL_ICON` (34px badges + 28px actTitle icons), `TOOL_META`, new `TOOL_CATS` entry ("Styles & genres"), `CHAPTER_SEARCH_TERMS`, `GRADE_TAGS`, `STAGES` (added to "Know your instrument", alongside `piano-story`/`pitch-range`) | Icons depict their own tool literally: four layered horizontal lines of different lengths/colors for Texture Types (matching the tool's own header icon), an ear-like circle-and-curve for Texture Spotter, and four colored squares for Genre Traits. |
| 5 | Verification | -- | Babel compile + `node --check` (0 errors). Live Playwright pass: all 3 Toolbox tools opened and interacted with (texture switching with real differentiated audio, spotter guess with feedback, genre trait browsing), the full 3-step lesson page, and the drill quiz through several questions with right/wrong feedback -- zero console/page errors throughout. Screenshots visually spot-checked for every tool state plus the full lesson page and drill quiz. |
| 6 | Committed, not pushed | commit `b454163` | Ready for Sohyun to push, along with Phases 177-183. |

**Item #20 (reference-book gap-fill) is now complete** -- all three entirely-missing chapters
(Melody, Form, Styles & Genres) are built and verified. The book's thinner sub-topics noted at the
start of item #20 (relative minor/circle of fifths depth, modulation/transposition depth,
cadences/chord-symbols/harmonizing-a-melody depth) remain a lower-priority follow-up, not started.

### Phase 185 -- Consolidate Toolbox filter pills to match the reference book's chapters (2026-09-28)

Sohyun looked at the Toolbox's category pill list (15 pills) and said it was too fragmented to
scan at a glance, giving a concrete example: "Pulse & counting" and "Rhythm & note values" should
just be one "Rhythm" pill. She asked for the whole list reorganized around the reference book's
own chapter names (the same book already used for the Melody/Form/Styles & Genres chapters this
session).

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | 15 pills -> 13 | `TOOL_CATS` | `keys` (Finding notes on the keys) + `reading` (Reading notes) merged into a new `pitch` category, "Pitch" (book Ch.1). `beat` (Pulse & counting) merged into `rhythm`, "Rhythm" (book Ch.2) -- the example Sohyun gave. The 6 interval-identification tools moved out of `harmony` into `scales`, renamed "Intervals, Scales & Keys" (book Ch.3); `harmony` now holds only chord/cadence tools, renamed "Chords & Harmony" (book Ch.5). `melody`/`form`/`styles` renamed to their exact book titles: "Melody", "Form", "Styles & Genres" (dropping the app's own descriptive suffixes). |
| 2 | Kept as-is | `body`, `expression`, `ear`, `words`, `practice`, `about` | These have no equivalent chapter in the reference book (posture, ear training, practice helpers, etc. are the app's own pedagogy, not book content) -- folding them into a book chapter would misrepresent what the book covers, so they stayed separate. |
| 3 | Reassignment | `TOOL_META` | Every tool id previously tagged `keys`, `reading`, or `beat` retagged to `pitch` or `rhythm`; the 6 interval tools retagged from `harmony` to `scales`. All lookups (`toolMeta`, `TOOL_CATS.find`, pill rendering, the search overlay) are driven dynamically off the single `TOOL_CATS` array, so nothing else needed to change. |
| 4 | Verification | -- | Babel compile + `node --check` (0 errors). Live Playwright pass on the Toolbox: confirmed all 13 pills render with the intended labels ("Pitch", "Rhythm", "Intervals, Scales & Keys", "Chords & Harmony", "Melody", "Form", "Styles & Genres", plus the 6 unchanged pedagogy pills), clicked several to confirm filtering still works -- zero console/page errors. Screenshot-checked the pill row visually for the cleaner 4-row layout. |
| 5 | Committed, not pushed | commit `84a1854` | Ready for Sohyun to push, along with Phases 177-184. |

### Phase 186 -- Illustrated-content direction, pilot on First Steps chapter (2026-09-29)

After a dedicated design conversation (3 rounds of mockups, references: an "onto z" watering-can
collage card, a London Jazz Festival poster, and two Pinterest mood-boards of mid-century flat
collage illustration), Sohyun confirmed a new illustration direction for drills.html content --
recorded in full in the `piano-butler-designer` skill (palette, scope, composition principle).
She then said to roll it out "ONE BY ONE FROM THE FIRST ONE" rather than picking a pilot chapter
of convenience -- so this phase applies it to `first-steps` ("Posture, Hands & Black Keys"),
DRILLS[0], exactly as it sits in chapter order.

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | Chapter hero illustration | `FirstStepsHero` (new component), wired into `FirstStepsLearn`'s `<Lesson head={...}>` slot | Depicts the chapter's own "small house, big house" black-key analogy literally -- a 2-key cluster and a 3-key cluster drawn as roof shapes, cream fill on a slate-blue ground (the color assigned to `pitch`-track chapters per the skill's rollout plan), rust "windows" standing in for the black keys themselves, one mustard accent circle. Not a generic decoration -- the same metaphor already in the chapter's own text (Phase 186 read that text before designing the image, rather than inventing an unrelated visual). |
| 2 | 9 new Toolbox badge icons | `TOOL_ICON`: `sit-check`, `hand-shape`, `arm-moves`, `posture-check`, `finger-numbers`, `high-low`, `key-houses`, `black-key-song`, `black-white-neighbours` | These 9 first-steps tools had no badge icon before this phase (only `arm-alignment` did) -- ToolCard degrades gracefully with no icon, so this was purely additive, no risk to existing cards. Each new badge is a self-contained colored square (same slate/cream/rust/mustard palette as the hero) depicting its own tool's mechanism literally, per the existing icon-literalism rule: a stool with a height arrow for Set up the stool, a knuckle-bridge arc for The hand shape, a sweep arc for Move with the whole arm, a checklist for Posture check, a numbered fingertip for Finger numbers, paired up/down chevrons for High, low, loud and soft, a small/big roof pair for Small house big house, a note over a black key for Your first song, and a black key beside an outlined white key for Black keys, white neighbours. |
| 3 | Scope respected | -- | Nothing outside `drills.html` content touched. Buttons, nav, tabs, category-pill colors all stay ink/brass exactly as before -- verified by diff (`git diff --stat` showed only `drills.html`, 51 insertions). |
| 4 | Verification | -- | Babel compile + `node --check` (0 errors). Live Playwright pass: opened the full First Steps chapter end to end (hero renders correctly, all 10 lesson steps scroll with no breakage), then searched up and screenshotted each of the 9 newly-iconified tool cards individually in the Toolbox to confirm every badge renders legibly at its real 40px size, not just in isolation. Zero console/page errors throughout. |
| 5 | Committed, not pushed | commit `cef6c7b` | Ready for Sohyun to push, along with Phases 177-185. |

While this phase was in progress, Sohyun sent a follow-up reaction to an earlier mockup round
(the bolder, more saturated "poster" palette from round 2 of the design conversation, not the
quieter round-3 palette that was actually confirmed and shipped here): she said she also likes
that more colorful version and wants the eventual full set of chapters to feel like a "gallery" --
varied, colorful, something people want to keep looking through. This doesn't contradict what
shipped this phase (the confirmed palette already varies by chapter/track -- dusty rose, forest,
rust, slate, mustard -- so a gallery effect builds naturally as more chapters ship), but it's worth
her explicit steer once a few more chapters are live and she can see them side by side: whether to
stay within the round-3 quieter family for consistency, or let later chapters lean toward round
2's higher-saturation end of the same palette for more variety. Not a blocker -- noted here so it
isn't lost, and to revisit once she's seen a handful of chapters together.

### Phase 187 -- Illustrated-content direction, chapter 2: Note Names (2026-09-29)

Continuing "ONE BY ONE FROM THE FIRST ONE" -- second chapter in `DRILLS` order.

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | Chapter hero illustration | `NoteNamesHero` (new component), wired into `NoteNamesLearn`'s `<Lesson head={...}>` slot | A ring of the 7 letters A-G on the same slate-blue ground assigned to `pitch`-track chapters, with C highlighted in mustard -- reuses the chapter's own "seven letters, A to G, then loop back" idea, and deliberately echoes `LetterCircle` (the existing in-tool ring diagram inside the Letter Chain drill) rather than inventing an unrelated image. |
| 2 | 4 new Toolbox badge icons | `TOOL_ICON`: `find-every`, `name-reveal`, `step-updown`, `letter-chain` | None had icons before. Each depicts its own tool literally: a magnifying glass over a "C" for Find every C, a letter tile dropping onto a key for Name them in order, paired up/down arrows for Step up step down, three linked circles for Letter chain. |
| 3 | Caught and fixed before commit | `NoteNamesHero` | First version clipped the ring (C and G cut off at the bottom of the frame) -- the first live screenshot showed it immediately, fixed by widening the viewBox and re-centering before re-verifying and committing. Left in the log as a reminder that a first screenshot of a new hero illustration is not optional, even for a "just geometry" SVG. |
| 4 | Verification | -- | Babel compile + `node --check` (0 errors) on both the clipped and corrected version. Live Playwright pass on the corrected version: full chapter opened top to bottom, all 4 new tool cards searched up and screenshotted individually in the Toolbox. Zero console/page errors. |
| 5 | Committed, not pushed | commit `350e2dc` | Ready for Sohyun to push, along with Phases 177-186. |

### Phase 188 -- Illustrated-content direction, chapter 3: Pulse & Counting (2026-09-29)

Continuing "ONE BY ONE FROM THE FIRST ONE" -- third chapter in `DRILLS` order.

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | Chapter hero illustration | `PulseHero` (new component), wired into `PulseLearn`'s `<Lesson head={...}>` slot | A heartbeat/ECG-style pulse line on the dusty-rose ground assigned to `rhythm`-track chapters, two beats marked as peaks (one mustard, one rust). Directly literal -- `SteadyBeat`'s own blurb already calls it "a heartbeat pulse to tap along with," so the illustration draws that heartbeat rather than inventing a separate metaphor. |
| 2 | 3 new Toolbox badge icons | `TOOL_ICON`: `steady-beat`, `beat-target`, `count-aloud` | None had icons before. A small pulse-line echo of the hero for Steady Beat, a bullseye with a beat number at center for Tap the right beat, a speech bubble reading "1 2" for Count it out loud. |
| 3 | Verification | -- | Babel compile + `node --check` (0 errors). Live Playwright pass: full chapter opened top to bottom, both remaining new tool cards searched up and screenshotted individually in the Toolbox. Zero console/page errors. |
| 4 | Committed, not pushed | commit `b5b2bab` | Ready for Sohyun to push, along with Phases 177-187. |

### Phase 189 -- Illustrated-content direction, chapter 4: Notes & Rests (2026-09-29)

Continuing "ONE BY ONE FROM THE FIRST ONE" -- fourth chapter in `DRILLS` order.

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | Chapter hero illustration | `NoteValHero` (new component), wired into `NoteValLearn`'s `<Lesson head={...}>` slot | A binary split-tree on the dusty-rose ground shared with `pulse` (both `rhythm`-track): one whole block halving into two, then four. Directly depicts the chapter's own intro text ("every note splits into two of the next one down") and the `split-it` tool's own name. |
| 2 | 6 new Toolbox badge icons | `TOOL_ICON`: `split-it`, `note-rest-naming`, `rest-grouping`, `whole-bar-rest`, `note-rest-match`, `fill-bar` | None had icons before. Each literal to its own tool: a splitting block for Split the notes, a note glyph "=" a rest glyph for Same name note or rest, three beat dots with the middle one accented for the beat-3 rule in Writing rests correctly, a hanging rest under a line for The whole-bar rest, two paired swatches for the memory-match game, a partly-filled bar outline for Fill the bar. |
| 3 | Verification | -- | Babel compile + `node --check` (0 errors). Live Playwright pass: full chapter opened top to bottom (8 steps, no breakage), 5 of the 6 new tool cards searched up and screenshotted individually in the Toolbox. Zero console/page errors. |
| 4 | Committed, not pushed | commit `f33f143` | Ready for Sohyun to push, along with Phases 177-188. |

### Phase 190 -- Brighten illustrated-content palette + composition polish (2026-09-29)

Sohyun shared a second set of references (a fruit still life, several travel-poster style
illustrations, a watch/picnic pairing) and gave two concrete notes: this brightness level is fine
(brighter than the round-3 palette actually shipped in Phases 186-189), and the illustrations
should be better balanced and "cute but sophisticated" (귀여우면서 세련되게), not just flat color
fills. This is an evolution of the confirmed direction, not a reversal of it -- same system (one
ground color per track, one confident object, generous space), retuned brighter and with more
finishing detail.

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | Brightened palette, file-wide | Every illustration hex used in Phases 186-189 | `#4a6a84`->`#3a7bc4` (pitch ground, slate->sky blue), `#d9a9a0`->`#e2735a` (rhythm ground, dusty rose->coral), `#f4ede0`->`#f7f0e0` (cream, warmed slightly), `#b25c3f`->`#c96b3f` (rust accent), `#d9a441`->`#e8b93a` (mustard accent), plus their ink/detail pairs. Before replacing, verified every occurrence of each old hex traced back to this session's own additions (none pre-existed elsewhere in the 13,000+ line file), so a global find-and-replace was safe as a pure recolor with no risk to unrelated code. |
| 2 | Ink outline strokes added | `FirstStepsHero`, `NoteNamesHero`, `PulseHero`, `NoteValHero` | The references' "sophisticated" quality comes partly from a clean thin outline on flat shapes, not just flat fills -- added `stroke="#241f1a"` to the cream shapes in all 4 already-shipped heroes. |
| 3 | Composition rebalanced | `FirstStepsHero` | The original had the sun isolated top-right with nothing to counterweight it. Added a small 3-circle cloud cluster on the left and grew the canvas so the two houses read bigger and more centered -- the earlier version felt a little empty. |
| 4 | Verification | -- | Babel compile + `node --check` (0 errors). Live Playwright pass: reopened all 4 already-shipped chapters fresh and screenshotted each hero at its new brighter palette. Zero console/page errors across all four. |
| 5 | Committed, not pushed | commit `d194a18` | Ready for Sohyun to push, along with Phases 177-189. |

The `piano-butler-designer` skill's illustrated-content palette table needs updating to match (a
follow-up skill proposal, not a silent edit) -- the confirmed hexes recorded there from the Phase
185 design conversation are now superseded by these brighter ones for any *new* chapter work going
forward.

### Phase 191 -- Illustrated-content direction, chapter 5: Rhythm Cards (2026-09-29)

Continuing "ONE BY ONE FROM THE FIRST ONE" -- fifth chapter in `DRILLS` order.

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | Chapter hero illustration | `RhythmCardsHero` (new component), wired into `RhythmLearn`'s `<Lesson head={...}>` slot | A fanned deck of 3 outlined rhythm cards on the coral rhythm-track ground, each with a distinct note-stem pattern -- literal to the chapter's own "40 one-bar rhythms" card-deck concept. Deliberately a different composition from the other rhythm-track heroes already shipped (a heartbeat line for Pulse, a split-tree for Notes & Rests), so chapters sharing a ground color still look distinct from each other. |
| 2 | 3 new Toolbox badge icons | `TOOL_ICON`: `anacrusis`, `count-more`, `make-card` | None had icons before. A partial pickup note leading into a full one for Anacrusis, subdivided beat ticks for Count harder rhythms, a card with a pencil corner for Make a rhythm card. |
| 3 | Verification | -- | Babel compile + `node --check` (0 errors). Live Playwright pass: full chapter opened top to bottom, both remaining new tool cards searched up and screenshotted individually. Zero console/page errors. |
| 4 | Committed, not pushed | commit `1d07936` | Ready for Sohyun to push, along with Phases 177-190. |

### Phase 192 -- Illustrated-content direction, chapter 6: Reading the Staff (2026-09-29)

Continuing "ONE BY ONE FROM THE FIRST ONE" -- sixth chapter in `DRILLS` order (5 of 24 done before this one). Also the first chapter shipped entirely in the Phase 190 brightened palette from the start (no separate recolor pass needed).

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | Chapter hero illustration | `StaffHero` (new component), wired into `StaffLearn`'s `<Lesson head={...}>` slot | 5-line staff on the sky-blue pitch-track ground, with mustard circles marking notes on a line and a cream ellipse marking a note in a space -- reuses `StaffBasics`' own existing circle/ellipse coding for lines/spaces rather than inventing a new one. A simple ink-outline treble-clef swirl in cream is the secondary balancing element on the left. |
| 2 | 11 new Toolbox badge icons | `TOOL_ICON`: `staff-basics`, `clef-basics`, `clef-story`, `staff-climb`, `rhymes`, `landmarks`, `flash-cards`, `landmark-hop`, `fold`, `write-note`, `alto-clef` | All 11 tools in the chapter iconified in one pass (per the "scatter everywhere" rule, not just the flagship tool). Each depicts the tool's own literal mechanism: a staff + circle for What is the staff?, simplified G/F clef marks for Treble/bass clef, a crown for "The Queen and the King", an ascending staircase for Climb the staff, a speech-bubble for the EGBDF rhymes, a numbered flag planted on the staff for Landmark notes, a card for flash cards, a hop arc between two notes for Hop from a landmark, a mirrored fold at middle C for Fold at middle C, a pencil drawing a dashed note for Write it on the staff, and a C-clef bracket for Alto clef. |
| 3 | Verification | -- | Babel compile + `node --check` (0 errors). Live Playwright pass: full chapter opened top to bottom, all 11 tool cards searched up individually and screenshotted together in the Toolbox list -- all icons confirmed legible against the sky-blue badge background. Zero console/page errors. |
| 4 | Committed, not pushed | commit `308bdd2` | Ready for Sohyun to push, along with Phases 177-191. |

### Phase 193 -- Illustrated-content direction, chapter 7: Ledger Lines (2026-09-29)

Continuing "ONE BY ONE FROM THE FIRST ONE" -- seventh chapter in `DRILLS` order (6 of 24 done before this one).

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | Chapter hero illustration | `LedgerHero` (new component), wired into `LedgerLearn`'s `<Lesson head={...}>` slot | Sky-blue pitch-track ground: a five-line staff with short ledger lines stepping out above and below, each carrying a note -- literal to the chapter's own "walk off the staff" framing (its first Step). Same mustard-circle/cream-ellipse note coding as `StaffHero`, giving the two staff-related chapters a visually related but not identical pair. |
| 2 | 4 new Toolbox badge icons | `TOOL_ICON`: `ledger-walk`, `ledger-landmarks`, `ledger-twins`, `ledger-write` | One per tool in the chapter. Lines stepping out with notes for Walk off the staff; ACE/CAF letters beside short lines for Notes on ledger lines; two staff lines linked by a dashed connector for Same note, other staff; a dashed note + pencil corner for Write with ledger lines. |
| 3 | Verification | -- | Babel compile + `node --check` (0 errors). Live Playwright pass: full chapter opened top to bottom, all 3 remaining new tool cards searched up individually. A broad-match search screenshot also confirmed all 6 previously shipped chapters' icons still render correctly alongside these new ones. Zero console/page errors. |
| 4 | Committed, not pushed | commit `31d451c` | Ready for Sohyun to push, along with Phases 177-192. |

### Phases 194-198 -- Illustrated-content direction: DRILLS-order correction and backfill (2026-09-29)

Discovered while starting what I'd labeled "chapter 7" (Ledger Lines, Phase 193): the true `DRILLS` array order is first-steps, note-names, pulse, note-values, rhythm, staff, **reading-steps, five-finger, time-signatures, tempo, dynamics**, ledger-lines, tones, scales... -- five chapters (Steps & Skips, Five-Finger Positions, Time Signatures, Tempo Race, Dynamics & Articulation) sit between Reading the Staff and Ledger Lines and were skipped over by mistake. Ledger Lines itself (Phase 193) is fine as shipped, just built out of the strict "one by one" order. Backfilled the five skipped chapters in true DRILLS order before continuing past Ledger Lines, so the rollout is now caught up through chapter 11 with no gaps.

| Phase | Chapter (DRILLS position) | Hero | Icons | Notes |
|---|---|---|---|---|
| 194 | Steps & Skips (7, pitch/sky-blue) | `ReadingStepsHero` -- 3 notes climbing the staff, a step then a bigger skip | `step-skip`, `mini-tune`, `complete-melody`, `echo` | Commit `7a5acdb` |
| 195 | Five-Finger Positions (8, pitch/sky-blue) | `FiveFingerHero` -- 5 keys, 5 numbered fingers, thumb in mustard | `five-positions` | Commit `cca13ad` |
| 196 | Time Signatures (9, rhythm/coral) | `TimeSigHero` -- big 3/4 beside one barred bar of 3 beat dots | `count-along`, `bar-lines`, `beat-doubler`, `grouping`, `duplets`, `regroup` | Commit `9d120c1` |
| 197 | Tempo Race (10, **reading** -- new track) | `TempoHero` -- 3 race lanes sparse-to-dense, turtle + checkered flag | `metronome`, `speed-change` | Commit `e465e96`. First chapter on the "reading" track -- introduced a new ground color, **dusty teal `#3f9e94`**, distinct from pitch's sky blue and rhythm's coral, same Phase 190 brightness family. Flagging this color choice for Sohyun in case she'd rather use something else; it's one systematic hex, trivial to swap. |
| 198 | Dynamics & Articulation (11, reading/teal) | `DynamicsHero` -- one crescendo hairpin, soft dot to loud dot | 6 tools recolored (`dyn-order`, `hairpin`, `pedal`, `touch-lengths`, `tie-slur`, `touch-ear`) from their pre-existing Phase 179 `var(--brass)`-style icons onto the new teal rounded-square badge, for gallery consistency | Commit `2f2a737` |

Each phase verified individually: Babel compile + `node --check` (0 errors every time), live Playwright pass opening the full chapter plus every new/changed tool card via search, 0 console/page errors throughout. Committed, not pushed -- ready for Sohyun to push along with everything since Phase 177.

Chapters 1-11 of 24 are now fully done in true DRILLS order. Next up: chapter 12 (Ledger Lines) is already done (Phase 193) -- continue from chapter 13 (Tones & Semitones) onward.

### Phase 199 -- Illustrated-content direction, chapter 13: Semitones & Tones (2026-09-29)

Continuing normally through `DRILLS` order (chapter 12, Ledger Lines, already shipped in Phase 193; the chapter 7-11 backfill finished in Phase 198).

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | Chapter hero illustration | `TonesHero` (new component), wired into `TonesLearn`'s `<Lesson head={...}>` slot | Sky-blue pitch-track ground: a short keyboard strip with C-D (a whole step, black key between) highlighted cream and E-F (a half step, no black key between) highlighted mustard, each under a small "T"/"S" arc -- literally the chapter's own "S (1 key) / T (2 keys)" framing. First draft mistakenly drew a black key between the E-F pair -- caught on the first screenshot, fixed before committing (another "always screenshot before calling it done" catch). |
| 2 | 4 new Toolbox badge icons | `TOOL_ICON`: `tone-semitone`, `sharp-flat`, `chromatic`, `accidental-bar` | A small keyboard segment matching the hero; a sharp sign with a bend arrow; five alternating light/mustard keys; a barred bar with a sharp curling toward a note. |
| 3 | Verification | -- | Babel compile + `node --check` (0 errors). Live Playwright pass: full chapter opened top to bottom, all 4 new tool cards searched up and screenshotted. Zero console/page errors. |
| 4 | Committed, not pushed | commit `d031320` | Ready for Sohyun to push, along with everything since Phase 177. |

Chapters 1-13 of 24 now done in true DRILLS order (12 shipped Phase 193, out of strict sequence but fine as-is). Next: chapter 14 (Scales).

### Phase 200 -- Illustrated-content direction, chapter 14: Scales (2026-09-29)

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | Chapter hero illustration | `ScalesHero` (new component), wired into both `ScalesLearn` branches via `head={<>{scalesHero}{tabs}</>}` | Sky-blue pitch-track ground: a full 8-note run climbing evenly in one smooth line, tonic (1st/8th degree) in mustard -- "one shape builds every major scale". The `scales` DRILLS entry is actually two toggled Lessons (major/minor, existing `head={tabs}` precedent) -- the hero is built once and shown above the tabs on both, so it persists across the toggle. Deliberately a longer, smoother climb than Steps & Skips' shorter step-vs-skip contrast so the two pitch-track heroes don't read as repeats of each other. |
| 2 | 6 new Toolbox badge icons | `TOOL_ICON`: `minor-forms`, `degree-names`, `scale-finder`, `build-major`, `build-minor`, `modes` | Three overlaid scale-shape outlines for the minor forms; a dot row with the tonic labelled "1"; a magnifying glass; a rising line to a peak (kinked lower for the minor's raised 7th); a bar chart of increasing note-counts for the seven modes. |
| 3 | Verification | -- | Babel compile + `node --check` (0 errors). Live Playwright pass: chapter opened, switched between the major and minor tabs (hero confirmed present and correct in both), broad Toolbox search screenshot confirming all 6 new icons. Zero console/page errors. |
| 4 | Committed, not pushed | commit `44814c0` | Ready for Sohyun to push, along with everything since Phase 177. |

Chapters 1-14 of 24 now done. Next: chapter 15 (Key Signatures).

### Phase 201 -- Illustrated-content direction, chapter 15: Key Signatures (2026-09-29)

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | Chapter hero illustration | `KeySigHero` (new component), wired into `KeySigLearn`'s `<Lesson head={...}>` slot | Sky-blue pitch-track ground: a staff with 4 sharps arriving left to right, each under its own numbered badge, the newest (4th) in mustard -- "sharps and flats always arrive in the same order... numbered", reusing the chapter's own OrderBuilder framing. |
| 2 | 6 new Toolbox badge icons | `TOOL_ICON`: `transpose`, `sharps-order`, `flats-order`, `place-it`, `relative-minor`, `circle-fifths` | Two parallel melodic contours (one shifted) for Transpose; a row of accidental glyphs fading in with the newest highlighted for the sharps/flats order tools, matching the hero; staff lines with a placed sharp and a dashed target ring for Place the key signature; two linked note-dots labelled "-3" for Relative minor; twelve dots around a ring for Circle of fifths. |
| 3 | Verification | -- | Babel compile + `node --check` (0 errors). Live Playwright pass: full chapter opened top to bottom, broad Toolbox search screenshot confirming all 6 new icons plus every previously shipped chapter's icons render correctly together. Zero console/page errors. |
| 4 | Committed, not pushed | commit `2c19d1e` | Ready for Sohyun to push, along with everything since Phase 177. |

Chapters 1-15 of 24 now done. Next: chapter 16 (Intervals) -- note this chapter was already iconified in Phase 178, before this hero-illustration rollout existed, so it likely just needs a hero + a palette-consistency check on its existing icons, similar to what Dynamics needed in Phase 198.

### Phase 202 -- Illustrated-content direction, chapter 16: Intervals (2026-09-29)

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | Chapter hero illustration | `IntervalsHero` (new component), wired into `IntervalsLearn`'s `<Lesson head={...}>` slot | Sky-blue pitch-track ground: a vertical ruler between two notes with each rung numbered 1-4 -- reusing the chapter's own IntervalRuler tool as its emblem, "every interval has a number (count the letters)" from the chapter's own intro. |
| 2 | Recolored 7 pre-existing icons | `TOOL_ICON`: `interval-ruler`, `letter-hop`, `semitone-counter`, `scale-intervals`, `interval-ear`, `invert-interval`, `tritone` | These had icons from Phase 178, before this rollout's rounded-square badge style existed. Recolored all 7 onto the sky-blue badge for gallery consistency, same treatment as Dynamics & Articulation got in Phase 198. |
| 3 | Verification | -- | Babel compile + `node --check` (0 errors). Live Playwright pass: full chapter opened top to bottom, broad Toolbox search screenshot confirming all 7 recolored icons render correctly alongside every previously shipped chapter. Zero console/page errors. |
| 4 | Committed, not pushed | commit `59eeb93` | Ready for Sohyun to push, along with everything since Phase 177. |

Chapters 1-16 of 24 now done. Next: chapter 17 (Chords) -- also iconified pre-rollout (Phase 177), so expect the same hero-plus-recolor treatment.

### Phase 203 -- Illustrated-content direction, chapter 17: Chords (2026-09-29)

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | Chapter hero illustration | `ChordsHero` (new component), wired into `ChordsLearn`'s `<Lesson head={...}>` slot | Sky-blue pitch-track ground: a "snowman" triad -- three note-heads stacked in 3rds on a staff, root at the bottom in mustard -- reusing the chapter's own TriadStacker nickname ("the snowman") for root/3rd/5th. |
| 2 | Recolored 8 pre-existing icons | `TOOL_ICON`: `triad-stack`, `major-minor`, `key-chords`, `primary-triads`, `inversions`, `cadences`, `seventh-chords`, `chord-extensions` | Had icons from Phase 177, before this rollout's badge style existed. `major-minor` and `key-chords` keep their existing `Q_COL` quality colors (major/minor/diminished), which carry real meaning elsewhere in the app -- only added the sky-blue badge background around them. The other 6 moved fully onto the cream/mustard/ink palette. |
| 3 | Verification | -- | Babel compile + `node --check` (0 errors). Live Playwright pass: full chapter opened top to bottom, broad Toolbox search screenshot confirming all 8 recolored icons render correctly with Q_COL colors intact. Zero console/page errors. |
| 4 | Committed, not pushed | commit `b1ad6e9` | Ready for Sohyun to push, along with everything since Phase 177. |

Chapters 1-17 of 24 now done. Next: chapter 18 (signs, reading track).

### Phase 204 -- Illustrated-content direction, chapter 18: Signs (2026-09-29)

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | Chapter hero illustration | `SignsHero` (new component), wired into `SignsLearn`'s `<Lesson head={...}>` slot | Teal reading-track ground: a repeat sign (thin + thick barline, two dots) with a curved arrow looping back to the start -- directly reusing the chapter's own intro framing ("Music is read like a road map -- these are the road signs") and its own Road Map tool's core idea. |
| 2 | New icons for 4 tools (chapter had none before this rollout) | `TOOL_ICON`: `road-map`, `grace-write`, `ornaments`, `ottava` | Each depicts that tool's own literal notation symbol/mechanism: road-map = a fork in a road with a loop-back arrow; grace-write = a small grace note beside a full-size main note; ornaments = "tr" plus a wavy trill line; ottava = an "8" over a dashed octave line with a leap arrow, next to a note. All on the teal badge, cream/mustard/ink content, per the established sizing standard (34x34 badge). |
| 3 | Verification | -- | Babel compile + `node --check` (0 errors). Live Playwright pass: full chapter opened top to bottom, plus individual card screenshots for all 4 tools (road map, grace note, ornaments, 8va), and a Korean-language pass. Zero console/page errors throughout. |
| 4 | Committed, not pushed | commit `7c35e2d` | Ready for Sohyun to push, along with everything since Phase 177. |

Chapters 1-19 of 24 now done. Next: chapter 20 (piano-story, reading track).

### Phase 205 -- Illustrated-content direction, chapter 19: Musical Terms (2026-09-29)

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | Chapter hero illustration | `TermsHero` (new component), wired into `TermsLearn`'s `<Lesson head={...}>` slot | Teal reading-track ground: a small stack of flashcards, the front card showing an italic term ("mf" / mezzo-forte) -- literal to the chapter's own TermCards format and its "Italian words in the music, grade by grade" intro. |
| 2 | New icons for 2 tools (chapter had none before this rollout) | `TOOL_ICON`: `term-cards`, `term-match` | term-cards = a single flashcard with an italic term, matching the hero. term-match = a face-up term card ("p") beside a face-down card-back (X pattern), with a checkmark above -- depicting the actual memory-pairs mechanic (find the matching card). First draft of term-match tried spelling out the translated word ("soft") on the second card; it clipped/overlapped at icon size, caught on a cropped close-up screenshot and redesigned to the face-up/face-down pair instead -- another case for close-up verification, not just full-page. |
| 3 | Verification | -- | Babel compile + `node --check` (0 errors). Live Playwright pass (EN + KO): full chapter opened top to bottom, Toolbox search screenshot, plus a 6x cropped close-up of both new icons to confirm legibility after the term-match redesign. Zero console/page errors. |
| 4 | Committed, not pushed | commit `a4a9cc0` | Ready for Sohyun to push, along with everything since Phase 177. |

Chapters 1-20 of 24 now done. Next: chapter 21 (pitch-range, pitch track).

### Phase 206 -- Illustrated-content direction, chapter 20: The Piano's Story (2026-09-29)

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | Chapter hero illustration | `PianoStoryHero` (new component), wired into `PianoStoryLearn`'s `<Lesson head={...}>` slot | Teal reading-track ground: a 3-stop timeline (1700 Cristofori -> 1800s cast-iron frame -> Today, 88 keys) -- literal to the chapter's own PianoTimeline tool and its "Cristofori 1700 to the 88-key grand" blurb. |
| 2 | New icons for 3 tools (chapter had none before this rollout) | `TOOL_ICON`: `keyboard-ancestors`, `piano-timeline`, `eras` | keyboard-ancestors = a string with a plectrum, a tangent and a hammer above it, literally the 3 mechanisms the tool itself compares (pluck / press / strike). piano-timeline = a small keyboard over a 3-stop timeline, echoing the hero. eras = a 4-segment color-block strip standing in for the chapter's 4 style eras (Baroque/Classical/Romantic/20th-century). |
| 3 | Verification | -- | Babel compile + `node --check` (0 errors). Live Playwright pass: full chapter opened top to bottom (had to search "Cristofori", not "piano timeline", to surface the whole-chapter link -- noted for next time), broad "piano" Toolbox search screenshot, plus 6x cropped close-ups of all 3 new icons. Zero console/page errors. |
| 4 | Committed, not pushed | commit `31862ee` | Ready for Sohyun to push, along with everything since Phase 177. |

Chapters 1-21 of 24 now done. Next: chapter 22 (melody, reading track).

### Phase 207 -- Illustrated-content direction, chapter 21: Pitch, Hz & Range (2026-09-29)

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | Chapter hero illustration | `PitchRangeHero` (new component), wired into `PitchRangeLearn`'s `<Lesson head={...}>` slot | Sky-blue pitch-track ground (first pitch-track chapter since chapter 17, Chords): a sound wave whose frequency visibly compresses left to right (a chirp, built from a quadratic phase curve, not just a uniform wave), literal to the chapter's own "faster = higher" rule in its Vibrations and Hertz step, with a slice of piano keys along the bottom for the range half of the chapter. |
| 2 | New icons for 2 tools (chapter had none before this rollout) | `TOOL_ICON`: `hz-explorer`, `range-chart` | hz-explorer = a wave compressing from cream/low to mustard/high, echoing the hero. range-chart = a keyboard strip with a highlighted mustard band showing an instrument/voice's range across the keys. |
| 3 | Verification | -- | Babel compile + `node --check` (0 errors). Live Playwright pass: full chapter opened top to bottom, "range" Toolbox search screenshot, plus 6x cropped close-ups of both new icons. Zero console/page errors. |
| 4 | Committed, not pushed | commit `43db14d` | Ready for Sohyun to push, along with everything since Phase 177. |

Chapters 1-22 of 24 now done. Next: chapter 23 (form, reading track).

### Phase 208 -- Illustrated-content direction, chapter 22: Melody & Phrasing (2026-09-29)

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | Chapter hero illustration | `MelodyHero` (new component), wired into `MelodyLearn`'s `<Lesson head={...}>` slot | Teal reading-track ground: a rising melodic contour -- notes at varying heights (pitch) spaced at varying intervals (rhythm), connected by a line -- literal to the chapter's own "Rhythm + pitch = a tune" framing and its own TuneAnatomy step. |
| 2 | Recolored 4 pre-existing icons | `TOOL_ICON`: `tune-anatomy`, `phrase-marks`, `question-answer`, `melody-sequence` | Had icons from before this rollout existed (no badge background, `var(--brass)`/mixed hues). `question-answer` keeps the app's own good/bad semantic colors (green checkmark for the resolved "answer", red "?" for the unstable "question") -- only added the teal badge background. The other 3 moved fully onto the cream/mustard/ink palette. |
| 3 | Verification | -- | Babel compile + `node --check` (0 errors). Live Playwright pass: full chapter opened top to bottom, "phrase" Toolbox search screenshot confirming all 4 recolored icons render correctly (question-answer's semantic colors intact). Zero console/page errors. |
| 4 | Committed, not pushed | commit `b263a73` | Ready for Sohyun to push, along with everything since Phase 177. |

Chapters 1-23 of 24 now done. Next: chapter 24, the last one (styles, "about" track -- needs a ground color decided, per the established pattern for a new track).

### Phase 209 -- Illustrated-content direction, chapter 23: Musical Form (2026-09-29)

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | Chapter hero illustration | `FormHero` (new component), wired into `FormLearn`'s `<Lesson head={...}>` slot | Teal reading-track ground: an A-B-A ternary-form layout, three labeled blocks -- literal to the chapter's own "letters like A and B" framing and its ternary-form content. |
| 2 | Recolored 4 pre-existing icons | `TOOL_ICON`: `form-shapes`, `same-or-new`, `rondo-refrain`, `binary-ternary-spot` | Had icons from before this rollout existed (no badge background, `var(--brass)`/mixed hues). None carried semantic meaning worth preserving (unlike Phase 208's question-answer) -- all 4 moved fully onto the cream/mustard/ink palette on the teal badge. |
| 3 | Verification | -- | Babel compile + `node --check` (0 errors). Live Playwright pass: full chapter opened top to bottom, "section" Toolbox search screenshot confirming all 4 recolored icons render correctly. Zero console/page errors. |
| 4 | Committed, not pushed | commit `3ab3a49` | Ready for Sohyun to push, along with everything since Phase 177. |

All 24 of 24 chapters now done -- the illustrated-content rollout (started Phase 176) is
complete. Every chapter has a hero illustration wired into its `<Lesson head={...}>` slot, and
every tool in the app has a `TOOL_ICON` entry on its track's colored badge (pitch sky-blue
#3a7bc4, rhythm coral #e2735a, reading teal #3f9e94, about sage-green #6b9b5e). Any future new
chapter or tool should follow this same pattern from the start rather than needing a follow-up
pass.

### Phase 210 -- Illustrated-content direction, chapter 24 (final): Styles & Genres (2026-09-29)

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | New track ground color | "about" track = sage green `#6b9b5e` | The 4th and last track color needed. Matches the brightness family of the existing three (pitch sky-blue `#3a7bc4`, rhythm coral `#e2735a`, reading teal `#3f9e94`). Flagged to Sohyun for awareness/veto before use, the same way teal was introduced and flagged for the reading track in Phase 197 -- she confirmed with "응". |
| 2 | Chapter hero illustration | `StylesHero` (new component), wired into `StylesLearn`'s `<Lesson head={...}>` slot | Sage-green ground: the chapter's own three textures side by side -- a single line (mono), a melody over chord blocks (homo), two interwoven lines (poly) -- literal to its own TextureTypes step. |
| 3 | Recolored 3 pre-existing icons | `TOOL_ICON`: `texture-types`, `texture-spotter`, `genre-traits` | Had icons from before this rollout existed (no badge background, `var(--brass)`/mixed hues). texture-types echoes the hero's own line language; texture-spotter is an "ear" listening ring; genre-traits is a 4-quadrant swatch grid for the 4 style families. No semantic colors needed preserving -- all moved fully onto the cream/mustard/ink palette on the new sage badge. |
| 4 | Verification | -- | Babel compile + `node --check` (0 errors). Live Playwright pass: full chapter opened top to bottom, "texture" Toolbox search screenshot confirming all 3 recolored icons and the new sage-green filter chip render correctly. Zero console/page errors. |
| 5 | Committed, not pushed | commit `9e55fad` | Ready for Sohyun to push, along with everything since Phase 177. |

**All 24 of 24 chapters are now done.** The illustrated-content rollout that began at Phase 176
(Sohyun's direction: "시각적으로 딱 이해가기 쉽게 만드는게 먼저 우선순위야") is complete: every
chapter has a hero illustration, and every tool in the app has a `TOOL_ICON` badge on its track's
color. Any new chapter or tool added later should get this treatment from the start.

### Phase 211 -- "All chapters" screen becomes a visual gallery (2026-09-29)

Sohyun's request mid-session, with a reference screenshot: a wallpaper-picker-style photo grid on
her phone, asking whether drills.html's chapter picker could work the same way. Since all 24
chapters now have hero illustrations (Phase 210 finished the rollout), this was directly
buildable with existing assets.

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | Grouping check before building | -- | She asked how to efficiently re-review/reset the chapter grouping first. Checked `STAGES` programmatically: all 24 `DRILLS` ids appear exactly once across its 6 groups, no gaps or duplicates -- so no re-grouping was actually needed, and the existing groups (Piano basics / Rhythm & counting / Reading music / Sound, signs & terms / Theory / Know your instrument) were reused as-is. |
| 2 | New `HERO_MAP` constant | Right above `LessonPath` | Maps each of the 24 chapter ids to its hero component (`'first-steps': () => <FirstStepsHero/>`, etc.), including the shared `ScalesHero` for the `scales` id (used by both its major/minor sub-lessons). |
| 3 | `LessonPath` rewritten | The "All chapters" screen | Each chapter row is now a full-width tappable card: the chapter's own hero illustration on top, then title / progress checkmark / grade tag / chevron below -- replacing the old plain text-row buttons. Single column, not a multi-column grid like the reference photo, because the heroes are wide 600x160 banners; a portrait grid would have shrunk them to illegible slivers. Same `STAGES` section headers/blurbs/colors as before. |
| 4 | Verification | -- | Babel compile + `node --check` (0 errors). Live Playwright pass: loaded the gallery directly (`?view=chapters`), scrolled top to bottom across all 6 stage groups (screenshots confirm every hero renders correctly as a thumbnail), clicked a card (Five-Finger Positions) and confirmed it opened that chapter's own lesson, plus a Korean-language pass. Zero console/page errors throughout. |
| 5 | Committed, not pushed | commit `7e7185f` | Ready for Sohyun to push, along with everything since Phase 177. |

### Phase 212 -- Split "Posture & Hand Shape" out of First Steps; fixed arm-alignment style and wrist bug (2026-09-29)

Sohyun's review of First Steps with 5 screenshots: steps 1-6 (sitting, hand shape, arm exercises,
arm weight, posture check, finger numbers) are what a student needs to know about their own body
before touching the keyboard; steps 7-10 (high/low, black-key houses, first song, white
neighbours) are keyboard-pattern content -- two different kinds of learning sharing one chapter.
She asked to split posture out first, and separately flagged the arm-alignment tool as visually
inconsistent with the rest of the chapter and hiding its own wrist point behind text.

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | New chapter: Posture & Hand Shape (`posture-hands`) | `DRILLS`, `STAGES` ("Piano basics" group), `GRADE_TAGS`, `CHAPTER_SEARCH_TERMS`, new `PostureHandsLearn` component | The 6 posture/hand-shape/finger-number `<Step>` blocks moved out of `FirstStepsLearn` verbatim. The 6 matching `TOOLS` entries (`sit-check`, `hand-shape`, `arm-moves`, `posture-check`, `finger-numbers`, `arm-alignment`) had their `ch:` field reassigned from `first-steps` to `posture-hands`. Its own quiz level (finger numbers) split out of `FS_LEVELS` into a new `POSTURE_LEVELS`/`POSTURE_HANDS_DRILL`, sharing the existing `genFsQuestion`/`FsQuestion`. No `HERO_MAP` entry yet -- left as a text-only gallery card on purpose, since Sohyun said she'll decide the remaining regrouping (steps 7-10, and the notation-reading group after that) next rather than guessing at hero artwork now. |
| 2 | First Steps trimmed | `FirstStepsLearn`, `FS_LEVELS`, `FIRST_STEPS_DRILL` | Now just the 4 keyboard-pattern steps (high/low loud/soft, small/big house, first song, white neighbours), retitled "The keyboard and your first song" / "건반과 첫 곡". Keeps its existing hero illustration (two black-key "houses"), which now matches its trimmed content even more directly than before. Quiz trimmed to its 3 remaining levels, renumbered. |
| 3 | `ArmAlignment` ("Feel the arm weight") restyled | Same component | Was a dark (`#241f1a`) abstract skeletal-diagram style, visually inconsistent with the flat illustrated-character look used everywhere else in this chapter (`HandSide`/`FrontArms`: cream background, blue-body torso, skin-tone head/limb joints). Rebuilt on a light background with the same body/limb visual language and color roles (`POS_SKIN`/`POS_SKIN_EDGE`, blue torso/upper-arm, tan forearm) so it now reads as the same "character" as `SitCheck`/`HandShape`/`ArmExercises`. |
| 4 | Fixed: wrist hidden behind text | Same component | The diagnostic panel was `position:absolute` over the top-right of the diagram; since the tracked wrist point can move into that exact region (e.g. the "wrist too high" state), it could end up completely hidden behind the tooltip box -- confirmed directly in Sohyun's screenshot. Moved the diagnosis panel out of the overlay entirely into a normal-flow card below the diagram, so no cursor position can ever cover a joint again. |
| 5 | Confirmed, no change made | "Set up the stool" (`SitCheck`) | Sohyun's "2 screenshots overlap" note was about the tool already being one step with two tabs (Side view / Front view covering genuinely different checks), not a request to merge or delete anything -- it already counts as a single entry in the new grouping, so nothing needed to change here. |
| 6 | Verification | -- | Babel compile + `node --check` (0 errors). Live Playwright pass: gallery render (both chapters appear as separate cards, correct hero placement), opened the new Posture & Hand Shape chapter (6 steps, 0/6 done -- confirms a clean split with no leftover progress bleed), opened the trimmed First Steps chapter (4 steps, 0/4 done), moved the cursor over the arm-alignment diagram to multiple positions confirming the wrist joint and label stay visible and joints recolor correctly, plus a Korean-language load. Zero console/page errors throughout. |
| 7 | Committed, not pushed | commit `694c163` | Ready for Sohyun to push, along with everything since Phase 177. |

**Same-day addendum (commit `df2ea71`):** Sohyun compared the new arm-alignment diagram against SitCheck's front-view tool side by side -- the shoulder joint floated visibly off the torso silhouette (should sit on its edge), no separate head was needed, and the two tools now read as the same picture despite checking different things. Replaced the filled torso + head circle with a single thick line from a hip point to the shoulder (the same line-based side-view grammar `SeatedFigure` already uses in SitCheck's own side tab, rather than `FrontArms`' front-facing blob) plus a small stool seat -- the shoulder is now the line's own endpoint (can't float away) and the diagram reads unambiguously as a side view, distinct from the front-view tool. Re-verified: Babel compile + `node --check` + live Playwright pass, zero errors.

### Phase 214 -- Split Finger Numbers into its own chapter (2026-09-30)

Sohyun's continued reorganization of the beginner sequence: teach finger numbers as its own
standalone step, positioned between pure posture/hand-shape drills and the upcoming hand/clef
assignment + keyboard-pattern content, rather than bundling it into the posture chapter.

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | New chapter: Finger Numbers (`finger-numbers`) | `DRILLS`, `STAGES` ("Piano basics" group, between `posture-hands` and `first-steps`), `GRADE_TAGS`, `CHAPTER_SEARCH_TERMS`, new `FingerNumbersLearn` component and `FINGER_NUMBERS_DRILL` concept | One Learn step (the `FingerNumbers` tool) and its own quiz (the "which finger?" question, moved out of the posture-hands drill, sharing the existing `genFsQuestion`/`FsQuestion`). The `finger-numbers` `TOOLS` entry's `ch:` field now points here instead of `posture-hands`. |
| 2 | Posture & Hand Shape trimmed further | `PostureHandsLearn`, `DRILLS` | Down to its 5 remaining steps (sit, hand shape, arm exercises, arm weight, posture check) -- none of which have quiz-testable content of their own (same as before this chapter existed: the original combined First Steps chapter never quizzed on posture either). Rather than leave an empty or orphaned "which finger?" quiz tab pointing at content no longer in this chapter's Learn page, its `DRILLS` entry now uses the app's own `render` fallback (`concept ? <ConceptView/> : active.render()`) instead of `concept` -- this path already existed in `App`'s routing but had never been exercised by any chapter before. Verified live before shipping: the chapter now shows no Learn/Drill tab bar at all, just its 5 steps, with zero console errors. |
| 3 | Recovered a stray uncommitted draft found mid-session | -- | A prior, uncommitted attempt at this same split was found sitting on disk (id `hand-fingers`, and it had left `posture-hands` still pointing at the finger-number quiz even though the Learn step had moved out -- the exact orphaned-quiz problem row 2 above avoids). Diffed it, kept one good line from its lesson intro copy (the "put finger 2 on D" example), and replaced it with this fully tested version rather than trying to merge two divergent implementations in place. |
| 4 | Verification | -- | Babel compile + `node --check` (0 errors). Live Playwright pass: gallery (both chapters as separate cards, correct order), the concept-less Posture & Hand Shape page (confirmed 0 Drill-tab buttons present, 0 errors), the new Finger Numbers chapter's Learn and Drill tabs (quiz questions, print worksheet, share link all present and working), and the trimmed First Steps chapter. Zero console/page errors throughout. |
| 5 | Committed, not pushed | commit `a0f8358` | Ready for Sohyun to push, along with everything since Phase 177. |


### Phase 215 -- Getting Started track: Hands & Clefs chapter, redesigned finger illustrations (2026-09-30)

Sohyun's strategic call on the beginner-onboarding sequence: rather than filing posture, finger
numbers, hand/clef assignment and the black-key map under the pitch-track "Piano basics" group
(alongside note names and five-finger positions, which are genuinely pitch-reading content), pull
the whole onboarding sequence into its own leading category -- since real lesson order for a fast
learner can vary a lot after this point (straight to note names and white keys, or to the staff, or
to time signatures), while this initial sequence is fixed for everyone. Recommended and Sohyun
confirmed a new pink "Getting Started" track. Also requested in the same message: build the new
hand/clef chapter, redesign the finger illustration to look like an actual hand, give each finger a
character/nickname, and explain the finger 3/4 tendon connection.

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | New 5th track: "Getting Started" (pink) | New leading `STAGES` group (`n: 0`), recolored `FirstStepsHero` + 3 new Hero components (`PostureHandsHero`, `FingerNumbersHero`, `HandClefsHero`), 3 `DRILLS` entries' `track` changed from `'pitch'` to `'start'`, `TOOL_ICON` badges for all `posture-hands`/`finger-numbers`/`first-steps` tools recolored from pitch-blue `#3a7bc4` to the new pink `#c1517c` | Group contains, in lesson order: Posture & Hand Shape, Finger Numbers, Hands & Clefs, Black Keys & Your First Song. "Piano basics" (`n: 1`) trimmed down to just Note Names and Five-Finger Positions, with an updated blurb. Palette: `#c1517c` background / `#a8395f` accent, chosen from Sohyun's own two suggestions (reuse pitch-blue, or pink) -- picked pink since it's now a visually distinct 5th track rather than a shade of the pitch track it's separating from. |
| 2 | New chapter: Hands & Clefs (`hand-clefs`) | `DRILLS`, `STAGES`, `GRADE_TAGS`, `CHAPTER_SEARCH_TERMS`, `TOOLS` (`hand-clef-match`), `TOOL_ICON`, `HERO_MAP`; new `HandClefsLearn`/`HandClefMatch`/`HandClefQuestion`/`genHandClefQuestion`/`HAND_CLEFS_DRILL` | Teaches "the top staff (treble clef) is usually the right hand, the bottom staff (bass clef) is usually the left hand" via the Grand Staff, reusing the existing `StaffView({clef:'grand', spread, notes})` renderer and referencing the pre-existing Queen-of-G/King-of-F clef-story characters by name (full story stays in the later, deeper `staff` chapter -- not duplicated here). Quiz is a single-level "which hand plays this clef?" question, sharing the app's existing `choice-btn`/`pixel-choice` question-rendering conventions. |
| 3 | `HandPic` redesigned | Same component (used by the standalone Finger Numbers tool and by `FsQuestion`'s finger-quiz rendering, so both call sites improved together) | First pass (skin-tone-adjacent cream fill, low-contrast strokes) read too washed out against the white card background and, worse, had a real bug: both hands' thumbs, rotated toward the center to look anatomically correct, swung into the shared middle and merged into one blob when the two hands sat only 10px apart in the standalone tool's side-by-side legend. Fixed by: warmer/more-saturated skin-tone fill (`#f6d7ae`) with a darker visible stroke (`#c9884f`), richer gold highlight for the "lit" finger (`#f6c343`), darker ink for the finger-number digits (`#4a2e15`, always legible now instead of only when highlighted), reduced thumb rotation (22° instead of 30°), and widened the gap between the two `HandPic`s in the Finger Numbers tool's legend (10px to 34px) so the thumbs read as reaching toward each other without overlapping. |
| 4 | Finger characters + tendon explanation | New `FINGER_NAMES` array, new `TendonLink` component, `FingerNumbers()` tool updated | Each finger now has a bilingual nickname shown as a chip legend and above the hand diagram: Captain Thumb/대장 엄지, Pointer/가리키미, Tall Middle/가운데 장군, Shy Ring/수줍은 넷째, Baby Pinky/막내 새끼. A new "Why is finger 4 the tricky one?" panel with a small `TendonLink` illustration (two finger shapes joined by a curved tendon line) explains that fingers 3 and 4 share a tendon under the skin, so lifting 4 alone naturally tugs on 3 -- framed as normal anatomy, not a mistake, that just needs patient practice. |
| 5 | Fixed a Korean-string bug found during this round's own verification | `FingerNumbers()`'s current-question label | The English/Korean string was built by concatenating fragments (`{hand} {"hand, finger"} {f}`), which is fine in English but rendered as "오른손 손, 1" in Korean (the word for "hand" doubled, and the number placed before its counter word instead of after). Switched to two full `LANG === 'ko' ? ... : ...` branches with correct Korean word order instead of fragment concatenation: "오른손 1번 손가락". |
| 6 | Verification | -- | Babel compile (`@babel/standalone`, React preset) + `node --check` (0 errors) on the full file. Live Playwright pass: gallery (new "Getting Started" pink group renders first with all 4 cards in the right order), Hands & Clefs chapter's Learn tab (staff diagram, Play button) and Drill tab (answered a question, correct feedback state), Finger Numbers Learn tab (redesigned hand diagram, character chips, tendon panel), played the "Show me finger..." game and tapped a finger on the redesigned `HandPic` to confirm `onTap`/`marks` still work, confirmed the quiz-embedded `HandPic` (inside `FsQuestion`) still renders with 0 errors, confirmed Posture & Hand Shape still has 0 Drill-tab buttons (unaffected by the `render`-fallback path from Phase 214), and a full Korean-language pass (toggled the actual 한국어 button, not just a URL param) on both new/changed chapters -- caught and fixed the finger/hand string bug in item 5 this way. Zero console/page errors throughout. |
| 7 | Committed, not pushed | commit `14215f0` | Ready for Sohyun to push, along with everything since Phase 177. |


### Phase 216 -- Default language always English, ignore stale localStorage preference (2026-09-30)

Sohyun: "디폴트는 영어로 보여야해" (the default must show in English) -- opening a fresh copy of
`drills.html` (the file sent to her in this session's chat) loaded in Korean instead of English.

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | Root cause | `LANG`/`LANG_KEY` init (top of file) | The initial language was read from `localStorage.getItem('pb_lang_v1')`, set by whichever language the 한국어/EN toggle button was last clicked to. Under a browser's shared `file://` origin (all local files opened directly, not through a server, generally share one `file://` storage bucket per browser), a Korean toggle click during this session's own live-testing on the Mac could carry over silently to a freshly-sent copy of the file -- not a per-file preference, a per-browser one. |
| 2 | Fix | Same `LANG` init, `toggleLang()` in `App()` | `LANG` now always starts `'en'`, unconditionally -- the `localStorage.getItem` read removed entirely. `toggleLang()` still flips the current visit's language via `setLang()`, but no longer writes to `localStorage` (dead write otherwise, since nothing reads it back anymore). |
| 3 | Verification | -- | Babel compile + `node --check` (0 errors). Live Playwright pass that specifically reproduces Sohyun's scenario: set `pb_lang_v1='ko'` in `localStorage` first (simulating a prior Korean toggle click), then reload -- toggle button correctly reads "한국어" (confirming the page is in English), not "EN". Clicked the toggle to confirm Korean still works mid-session, then reloaded again and confirmed it returned to English (no persistence), all with 0 console errors. |
| 4 | Committed, not pushed | commit `7324e57` | Ready for Sohyun to push, along with everything since Phase 177. |


### Phase 217 -- Natural thumb shape, Posture chapter reordered big-to-small, new finger-facts step (2026-09-30)

Sohyun compared the redesigned `HandPic` against a reference hand illustration (wikiHow's "Names
of Each Finger") and flagged the thumb specifically as looking wrong -- also asked to reorder
Posture & Hand Shape from big body parts to small ones (stool -> whole-arm movement -> hand shape
-> individual fingers), with a new short step giving fingers 2/3/4 quick, fun anatomical facts.

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | Thumb redesigned | `HandPic` | The thumb was literally the same rounded-rect finger capsule used for fingers 2-5, just shorter and rotated -- next to a reference illustration this read as a floating, disconnected blob rather than an actual thumb. Replaced with its own tapered `<path>` (a wide, rounded base that flares directly out of the palm outline, narrowing to a smaller rounded pad at the tip -- the actual shape of a thumb, not a finger), rotated about its own base point (which sits right on the palm's edge) rather than a distant pivot, so the join to the palm has no visible gap at any rotation angle. Tuned iteratively against live screenshots: first pass still showed a small gap (rotated base swinging slightly below the palm's flat bottom edge), fixed by moving the pivot further into the palm interior and reducing rotation to 32°. |
| 2 | Posture & Hand Shape reordered | `PostureHandsLearn` | Was: sit, hand shape, whole-arm movement, arm weight, posture check. Now, big body part to small: sit at the piano (stool/space) -> move with the whole arm -> feel the arm weight (both arm-related steps now sit together) -> the hand shape -> **Meet your fingers** (new) -> posture check (kept as the final wrap-up review, unchanged). |
| 3 | New step: Meet your fingers | New `FingerFriends` component, reusing `HandPic` and the existing `TendonLink` | A short, playful intro to individual finger character -- deliberately lighter than the full `FingerNumbers` tool (naming/numbering practice stays in its own later chapter): finger 2 "Pointer" (the one already used for pointing, naturally quick and independent), finger 3 "Tall Middle" (longest and strongest, naturally the best balance), finger 4 "Shy Ring" (tied to finger 3 by a tendon *and* works closely with 5 too -- the hardest to move alone, needs a little extra patience). Reuses the same `TendonLink` illustration already built for the Finger Numbers chapter rather than duplicating it. |
| 4 | Verification | -- | Babel compile + `node --check` (0 errors). Live Playwright pass: confirmed the new step order renders correctly top to bottom, expanded "Meet your fingers" and screenshotted the redesigned thumb both isolated (cropped) and in context, confirmed the chapter still has 0 Drill-tab buttons (concept-less, unaffected by the reorder), a Korean-language pass on the reordered chapter, and confirmed the quiz-embedded `HandPic` inside `FsQuestion` (Finger Numbers chapter's Drill tab, rendered at a larger 170px size) still renders the new thumb correctly with 0 errors. |
| 5 | Committed, not pushed | commit `5d048ed` | Ready for Sohyun to push, along with everything since Phase 177. |

### Phase 218 -- ArmAlignment iPad touch fix + icon cleanup, finger-anatomy step redesigned as a callout diagram (2026-09-30)

Sohyun reported Step 3 (Feel the arm weight) worked fine on the computer but the wrist didn't
move when touched on her iPad, flagged that this step alone has an icon before its title unlike
every other step, and -- after sharing a Gray's-Anatomy-style reference page ("The Problem of
Developing Equal Skills with All Fingers") a second time -- asked for the "Meet your fingers" step
to be redesigned in that labeled-diagram style, adapted to the site's own visual language.

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | iPad touch bug fixed | `ArmAlignment` | Root cause: React attaches `onTouchMove`/`onTouchStart` synthetic handlers as passive by default, so the existing `e.preventDefault()` inside the touch handler silently no-opped on iPad Safari -- the touch-drag gesture could be swallowed as a page scroll before reaching the handler, even with `touchAction:'none'` set on the container. Fixed by replacing the separate `onMouseMove`/`onTouchMove`/`onTouchStart` handler trio with a single unified `onPointerMove`/`onPointerDown` pair (Pointer Events aren't subject to the same passive-listener limitation and are the standard cross-device fix for exactly this class of bug). |
| 2 | Icon removed from title | `ArmAlignment` | This was the only step in the whole chapter with an inline SVG icon before its title text (`<svg>` line-drawing + two dots, added at some earlier phase and never applied elsewhere). Removed it so the title uses the same plain `actTitle` div as every other step. |
| 3 | "Meet your fingers" redesigned as a labeled callout diagram | New `FingerAnatomyDiagram` component, `FingerFriends` rewritten to use it | Replaced the plain picture-plus-bullets layout with a Gray's-Anatomy-style diagram: the Phase 217 `HandPic` hand/thumb artwork redrawn at a larger scale inside a single `<g transform="translate(...) scale(...)">` (so all the original 0-120/0-150 coordinate math, including the tapered-thumb fix, carries over unchanged), with six label boxes (plain HTML, for normal CSS text wrapping) connected by dashed leader lines to computed fingertip anchor points -- including the thumb tip, whose position is computed via the same rotation math used to draw it, so the leader line always lands exactly on the drawn tip. Facts updated to match the reference page: finger 5 is the smallest and weakest; finger 4 is the least independent and is tendon-bound to *both* neighbors (3 and 5, not just 3 as the Phase 217 version said); fingers 2 and 3 are the most agile and strongest; the thumb's muscles pull it toward the palm, which is why a clean downward strike feels awkward. First layout pass had the "finger 4" callout box overlapping the pinky finger's shaft -- fixed by moving that box higher, clear of both fingertips, and re-verified with a fresh screenshot. |
| 4 | Verification | -- | Babel compile (`@babel/standalone`, React preset) + `node --check` (0 errors). Live Playwright pass: desktop mouse-drag on `ArmAlignment` still moves the wrist marker; a separate pass using Playwright's iPad Pro 11 device emulation + real `touchscreen.tap()` calls confirmed touch taps on the diagram now move the wrist marker (previously the whole point of the bug); confirmed the title div has zero `<svg>` children (icon fully removed) via both a DOM check and a screenshot matching the other steps' plain style; screenshotted the new finger-anatomy diagram in both English and Korean (Korean text wraps to 3 lines in the label boxes with no overflow or clipping); a short regression pass across four other chapters plus the Finger Numbers Drill tab (which still uses the unrelated, unchanged `TendonLink` component) confirmed nothing else broke. Zero console/page errors throughout. |
| 5 | Committed, not pushed | commit `c7c31a5` | Ready for Sohyun to push, along with everything since Phase 177. |

### Phase 219 -- First-steps chapter: blue sky, teacher note removed from student view, "white neighbours" step dropped (2026-09-30)

Sohyun flagged three things on the "The keyboard and your first song" chapter: the hero banner's
sky should be blue (it draws clouds and a sun, but used the track's pink brand color), a
teacher-facing pacing note ("Not every student needs this yet...") was visible to students, and
Step 4 ("Ready for more? The white neighbours") should go.

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | Blue sky in the hero banner | `FirstStepsHero` | This is the only "Getting Started" hero banner that literally depicts an outdoor scene (clouds, sun, houses), so the track's pink brand color read as a wrong sky color rather than an abstract accent. Changed just this banner's background rect to a sky blue (`#6fa3cf`); the other three hero banners in the same track (posture, finger numbers, hand clefs) keep the pink brand color since they're not literal sky scenes. |
| 2 & 3 | Teacher-facing pacing note removed, Step 4 dropped | `FirstStepsLearn` | Sohyun's point: a note written for the teacher ("Not every student needs this yet -- some are ready to go further, others need more time...") was rendering directly in the student-facing lesson flow. Since that note lived only inside Step 4 ("Ready for more? The white neighbours"), removing the step removed the note with it. The chapter now ends at Step 3 ("Your first song"). The underlying tool (`BlackWhiteNeighbours`) and its Toolbox/search entry are left in place -- a quick learner can still find it -- only the forced step in the guided lesson flow is gone. Teacher-only commentary belongs in a separate teacher manual going forward, not in-lesson notes visible to students; flag any other spot like this if it comes up. |
| 4 | Verification | -- | Babel compile + `node --check` (0 errors). Live Playwright pass: confirmed the step count dropped from 4 to 3 ("0 of 3 steps done"), confirmed both the removed step's title and the teacher note text are gone from the rendered page in English and Korean, screenshotted the hero banner to confirm the sky reads blue, a short regression pass across the other three "Getting Started" chapters (posture-hands, finger-numbers, hand-clefs) found nothing broken, and confirmed the separate, chapter-agnostic Practice tab (a different, unrelated tool list) still renders with 0 errors. |
| 5 | Committed, not pushed | commit `3c74ad1` | Ready for Sohyun to push, along with everything since Phase 177. |

### Phase 220 -- Posture & Hand Shape gets a Drill tab: spot the stool / hand fault (2026-09-30)

Sohyun asked to continue the practice-drills work (drills.html). Nothing was queued, so the
session picked the one Getting Started chapter with no Drill tab: Posture & Hand Shape. Sohyun
confirmed this choice.

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | New two-level drill for `posture-hands` | New `POSTURE_LEVELS`, `POSTURE_SIT`, `POSTURE_HAND`, `genPostureQuestion`, `PostureQuestion`, `POSTURE_HANDS_DRILL`; `DRILLS` entry switched from `render:` to `concept:`; `PostureHandsLearn({ onStart })` + `onStart` passed to its `Lesson` | Level 1 "Is the stool set up right?" shows the existing `SeatedFigure` in one of five presets (`SIT_PRESETS`) and asks Just right / too low / too high / too close / too far. Level 2 "Spot the hand-shape fault" shows the existing `HandSide` (labels hidden so the green/red markers don't give the answer away) in one of six `HAND_POSES` and asks which fault it is. Both levels work in Lesson and Game (pixel) mode, print worksheet and share link (all via the standard `concept` contract). After an answer, a one-line "why + fix" appears in English or Korean. |
| 2 | Visual-first | -- | Every question is a picture, not a paragraph. No new illustrations were needed: both figures are reused from the Learn steps, so the drill tests exactly what the lesson shows. |
| 3 | Verification | -- | Babel compile (`@babel/core`, React preset, classic runtime) + `node --check`: 0 errors. Live Playwright pass (Chromium, React/Babel served locally because the sandbox blocks the CDN): Level 1 and 2 render, a wrong answer shows red/green plus the explanation and a Next button, Korean toggle relabels all choices and the explanation, Game mode renders the pixel labels without overflow, the Learn tab now shows "Start the drill" and Learn/Drill tabs. 0 console/page errors (only the known Babel 500KB note). |
| 4 | Not covered | -- | The 17-point posture checklist and arm-exercise tools are unchanged. First-steps, finger-numbers and hand-clefs already had drills. |

### Phase 221 -- Toolbox categories become in-place accordion bars, reordered (2026-09-30)

Sohyun: category chips/sections looked mismatched; wanted long bars that open downward on the same page, order settled first, colour/design unification later.

| # | Change | Where | Notes |
|---|--------|-------|-------|
| 1 | Accordion bars | `Toolbox` | Removed the scroll-jump chip row. Each `TOOL_CATS` entry is a full-width bar (dot, name, hint, count, chevron) that opens its tools in place (`openCats` state); search/level/kind/problem filters auto-open matching categories. |
| 2 | Category order | `TOOL_CATS` | Now teaching order: Posture & hands, Pitch, Rhythm, Intervals/Scales/Keys, Chords, Melody, Form, Touch & expression, Signs & terms, Ear, Styles, About music, Practice helpers. |
| 3 | Deferred | -- | Colour/design unification (TOOL_CATS dots vs track-coloured icon badges vs legacy plain icons e.g. arm-alignment) left for later, as Sohyun asked. |
| 4 | Verification | -- | Babel compile + node --check clean; Playwright: 13 bars, open/close works, search auto-opens, no page errors. |

### Phase 222 -- Letter Chain moved to Intervals; housekeeping decisions (2026-09-30)

| # | Change | Notes |
|---|--------|-------|
| 1 | Letter chain (spoken next-letter game) moved from Note Names to Intervals | New step sits after "The number" (it practises counting 2nd..octave by letters). Tool `letter-chain` now `ch: intervals`, category Intervals/Scales/Keys. Note Names lesson is now 3 steps. Old `?drill=letter-chain` links redirect to Intervals. |
| 2 | Note Names drill Level 4 (black keys) stays | Keyboard-based naming belongs in the Pitch track; the sharp/flat/natural meaning is taught in Tones & Semitones. |
| 3 | Interval song hooks: swap approved, NOT done | Need Sohyun's 3-4 tunes (opening interval unverified from memory, so none guessed). |
| 4 | Prototype pages shelved | movement-lab.html, piano-body-atlas.html, piano-posture-detail.html, pasted-kinematic-viewer.svg stay untracked and unlinked as reference only; fold into Posture chapter only if a specific need arises. **Sohyun deleted all four on 2026-10-06** (the app's own `sit-check` "Set up the stool" already covers bench distance and reach). |
| 5 | Rhythm Cards tap timing | Still needs a real-phone check (Pending #17). |

### Phase 223 -- Finger Numbers merged into Posture & Hand Shape (2026-09-30)
- Sohyun: shelve Rhythm Cards tap-timing (still needs a real-phone check, Pending #17), tidy categories in order, fold Finger Numbers into Posture & Hand Shape after step 5.
- `drills.html`: Posture & Hand Shape now has 7 steps (new step 6 "Finger numbers" with the `<FingerNumbers/>` tool, before "Posture check") and 3 drill levels (level 3 "Which finger?" reuses `genFsQuestion`/`FsQuestion`, dispatched by `kind`).
- Removed the standalone `finger-numbers` chapter (DRILLS, STAGES, GRADE_TAGS, HERO_MAP, search terms, `FingerNumbersLearn`, `FINGER_NUMBERS_DRILL`, `FingerNumbersHero`). Toolbox tool `finger-numbers` kept, now `ch: 'posture-hands'`; old `?drill=finger-numbers` links alias to posture-hands.
- Verified: Babel + `new Function()` compile, live Chromium load of posture-hands / old drill link / tool link, level 3 quiz, Korean step title; zero page errors.

### Phase 224 -- Toolbox tools as inline list rows (2026-09-30)
- Sohyun: category groups collapsing is right, but the tools inside should be long list bars that open in place, not a 2-column card grid that navigates away.
- `drills.html`: new `ToolRow` (full-width row: icon, title, blurb, level, star, chevron). Clicking expands the tool right under the row (one open per group); a "Learn the whole chapter" button sits inside the expanded panel. The per-group "Whole chapter" banner is hidden in the Toolbox (`ChapterGroups inline`). Student kit view uses the same rows (added right after); the global search overlay was already a row list.
- Verified: Babel + `new Function()`, live Chromium: category expands, row opens with URL unchanged, EN/KO toggle, zero page errors.

### Phase 225 -- One category system for teacher and student views (2026-09-30)
- Sohyun found the teacher Plan/Toolbox (13 skill categories) and the student Learn / All chapters page (7 learning-path stages) grouped the same chapters differently. Decision: use the Toolbox categories everywhere (option A, which also covers matching names/colours).
- `drills.html`: `CHAPTER_CAT` maps each of the 26 chapters to a `TOOL_CATS` id; `LessonPath` (student Learn + teacher All chapters) now groups by category with the category name, blurb and colour; empty categories (Ear, Practice helpers) are hidden; the chapter page header shows the category and its prev/next arrows follow category order. `STAGES` still exists for legacy data only.
- Toolbox: every chapter group now starts with a full-width "View full page: <chapter> →" row.
- Follow-up (same day): Five-Finger Positions moved into Intervals, Scales & Keys as the warm-up before Scales (order: Tones, Five-finger, Scales, Key signatures, Intervals; its Toolbox tool re-categorised to match). Hand & Clefs stays under Pitch. Posture & hands now holds only Posture & Hand Shape.
- Split (same day, Sohyun: too many in one group): "Intervals, Scales & Keys" (23 tools) became **Tones & Intervals** (10 tools; chapters Tones, Intervals) and **Scales & Keys** (13 tools; chapters Five-finger warm-up, Scales, Key signatures). New category id `tones`.
- Pitch split (same day, approved): **Piano keys & note names** (`keys`, 7 tools; chapters Hand & Clefs, First Steps, Note Names) and **Reading the staff** (`pitch`, 20 tools; chapters Staff, Reading Steps, Ledger Lines). Rhythm (19 tools) audited: see report -- chapter merges pending her decision.
- Polish (2026-10-01): tool "Name them in order" renamed "The seven note-name letters" (heading "The seven note-name letters, A to G"); Arm weight & alignment icon given the same pink badge as its Posture & hands siblings (it was the only bare icon). Wider colour/design unification waits for Sohyun's new references.
- Pilot (2026-10-01): Sohyun shared new references (flat mid-century cut-paper posters, wide bright palette: sky blue, forest green, mustard, tomato, pink, cobalt, teal, cream). The six Posture & hands tool icons were redrawn as a pilot with a different ground colour each (no outlines); tools inside a chapter group now follow that chapter's step order (`CHAPTER_TOOL_ORDER`, so far only posture-hands). If she approves, roll the varied palette out to all icons/heroes and set step order for the other chapters; the older per-track palette in the designer skill would then be superseded.
- Gallery rows (2026-10-01, approved palette): Toolbox tool rows now lead with a full-bleed 150px illustration panel (`.tool-art`, 104px on phones) instead of a 40px badge; card is 14px-rounded with overflow hidden, category left border dropped. The six Posture & hands illustrations were redrawn as richer scenes in the approved varied palette. Roll-out to the remaining ~95 icons and 26 chapter heroes is queued, one category at a time.
- Small-group tidy (2026-10-01, Sohyun approved): Hands & Clefs chapter + "Which hand plays this staff?" moved into **Posture & hands** (left/right hand is a first-lesson topic); Melody + Form merged into **Melody & Form** (8 tools); Styles & Genres + About music merged into **General knowledge** (8 tools; matches the existing GRADE_TAGS wording); "Tie or slur?" moved to Signs & terms. Now 11 categories with tools. Rhythm-group questions (Pulse vs Time Signatures, Tempo tool split across Rhythm/Expression, Rhythm Cards placement) still open.
- Rhythm (2026-10-01, Sohyun approved): Pulse stays its own chapter; Rhythm group order is Pulse, Note Values, Time Signatures, Rhythm Patterns, Tempo; chapter "Rhythm Cards" renamed **Rhythm Patterns**. Open: move the "rit. and accel." tool (Tempo chapter, currently in Touch & expression) into Rhythm next to the Metronome -- she didn't understand the question, explained in plain words, awaiting reply.
- Content-depth audit (2026-10-01, Sohyun wants a "music playground": manipulatives, playful metaphors, punchier explanations, more activities): thinnest chapters by steps/levels/tools/text are Hands & Clefs (1 step, 1 level, 1 tool), First Steps, Tempo, Five-Finger, Melody, Form, Styles, Pitch & Range; Musical Terms is 7k characters of text with a single picture. Recommended order: enrich content first, then the design phase, so art is drawn once.
- Five-Finger Positions folded into **Steps & Skips** (Sohyun, 2026-10-01): the chapter is gone; its lesson is now step 5 "Five-finger positions" of Steps & Skips, its quiz is Steps & Skips levels 4-6 (dispatch by `kind: 'ff'`), tool `five-positions` is now `ch: 'reading-steps'`, cat Reading the staff; old `?drill=five-finger` links alias to reading-steps. "rit. and accel." moved to **Signs & terms** (tool `ch: 'terms'`; Sohyun's call). Scales & Keys is now 12 tools.
- Content pass 1 -- Hands & Clefs (2026-10-01): 1 step -> 3 steps (Grand Staff; new "Split the keyboard" tap-a-key activity with the two-houses-and-a-doorbell metaphor, middle C = shared note; new "Spot the clef" costume toggle: treble curls round G, bass dots round F) and 1 -> 3 quiz levels (clef->hand, treble or bass?, which hand plays this note?). Components `HandSplit`, `ClefCostume`.
- **Sohyun's teaching voice (2026-10-01) -- use for all new explanations:** (1) *Best-friend distance*: she asks students "who is your best friend?" (closest person, by psychological distance) and shows "if you are this key, your best friend is here". Semitone = your very best friend (the very next key); tone = a friend of a friend (one person in between). (2) *Queen and King*: treble clef = the Queen (high voice, usually right hand, curl around G); bass clef = the King (low voice, usually left hand, two dots around F). (3) *Middle C = the Sydney CBD* connecting the two (a light touch, not essential). (4) She sometimes uses her own name, *Clara*, as the example character. Built so far: `BestFriends` (Tones & Semitones), `HandSplit` Queen/King/CBD wording (Hands & Clefs).
- Next (Sohyun approved: content before design, thinnest chapters first, in order): Hands & Clefs, Tempo, Musical Terms, Melody & Form, Styles; then the design phase (Pending #0).
- Verified: Babel + `new Function()`, live Chromium student Learn, chapter header, teacher All chapters, Toolbox rows; zero page errors.

- **Phase 227 (2026-10-01) -- Five-finger positions in all 12 keys; simple sight-reading counts; Toolbox order = chapter step order.** `POSITIONS` is now generated from `FF_ROOTS` (C, D♭, D, E♭, E, F, F♯, G, A♭, A, B♭, B; major shape tone-tone-semitone-tone; each note carries its own `acc`); Middle C position removed. Right hand sits above middle C; left-hand G/A/B roots drop an octave (tool keyboard base C2 for LH, C3 for RH) so the hand stays below middle C. Quiz levels 4-6 of Steps & Skips draw from all 12 (answer labels show ♯/♭); `MelodyStaff` name row now shows accidentals. `TapKeyboard`: finger numbers no longer overlap the letter labels (number sits above the letter). Sight-reading card level 3 = "any of 12 keys"; counts are simple `1 2 3 4` (`counts="simple"`, no "and", held beats just dimmed). `CHAPTER_TOOL_ORDER` now covers every chapter, generated from each Learn function's step order. Verified: Babel compile, live Playwright (EN), spellings of all 12 positions, 300 generated questions per ff level, zero page errors.

- **Phase 228 (2026-10-01) -- Reading the Staff restructure.** "What is the staff?" markers spread out (no overlap). "The rhymes" is now step 2 (right after lines and spaces, so notes get letter names straight away). Landmarks and "Middle C and ledger lines" merged: the middle-C fold (`FoldStaff`) now sits in a collapsible panel inside the Landmarks step (chapter is 8 steps). `LedgerMirror` ("The gap is really one missing line") moved to the Ledger Lines chapter, step 3. `CHAPTER_TOOL_ORDER` staff updated. Verified: Babel compile, live Playwright, zero errors.

- **Phase 229 (2026-10-01) -- Category split.** "Reading the staff" is now two categories: **Reading the staff** (Reading the Staff + Ledger Lines) and **Steps, skips & sight-reading** (`steps`; Steps & Skips chapter, with step-skip, mini-tune, five-positions, complete-melody, sight-reading tools). Tool order fixed for the Landmarks step: the fold-at-middle-C tool now sits directly at the top (the collapsible wrapper of Phase 228 was removed). 14 categories now.

- **Phase 230 (2026-10-01) -- Rests tool becomes a sound demo.** `RestGrouping` (Note Values) rewritten: tap each beat of a 4/4 bar to make it a note or a rest; Play runs a pulse click through the silence so the next note lands on time; presets; a toggle shows "two crotchet rests" vs "one minim rest" over beats 2-3 (sounds identical, only the writing differs). Tool retitled "Rests: counted, but silent". Also: Hands & Clefs "Which hand plays this staff?" moved after the Queen/King step (Phase 229+). Open decision: split Rhythm category into 3 (Beat & tempo / Note values / Time signatures & patterns).

- **Phase 231 (2026-10-01) -- Rhythm regrouped; Pulse joins the reading group.** Category `steps` renamed **"Reading tunes: pitch + rhythm"** and now holds Pulse & Counting (steady-beat, beat-target, count-aloud) + Steps & Skips (8 tools). Rhythm split into three categories: **Note values & rests** (`rnotes`, 6), **Time signatures & rhythm patterns** (`rtime`, 9: Time Signatures then Rhythm Patterns), **Tempo** (`rtempo`, 1). Note Values intro points back to Pulse & Counting. Sight-reading cards got an icon (Phase 230+). 16 categories total. Verified: Babel compile, live load, per-category tool counts.

- **Phase 232 (2026-10-01) -- Category tidy.** "Reading tunes: pitch + rhythm" (`steps`) keeps 4 tools (Read a tiny tune, Complete the melody, Five-finger positions, Sight-reading cards). **Pulse & counting** is its own category (`rpulse`, before Note values & rests, Time signatures & patterns, Tempo). "Step, skip or same?" moved to the Intervals chapter/Tones & Intervals category (also shown at the start of the Intervals lesson, step 1; still used in Steps & Skips lesson). 8va/8vb moved to Signs & terms. 17 categories.

- **Phase 233 (2026-10-01) -- Tempo chapter tools.** "The tempo race" (Slow to fast lanes) is now a standalone Toolbox tool (`tempo-race`, component `TempoLanes`, new icon). `speed-change` ("rit. and accel.") moved from Terms to Tempo, so there is no duplicate (Terms keeps term-cards + term-match). Tempo lesson steps reordered: Slow to fast → Changing speed → The metronome. Tempo category now has 3 tools. Fixed order in `CHAPTER_TOOL_ORDER`.

- **Phase 234 (2026-10-01) -- Metronome voice.** `SoundSettings` (click/voice/My voice) is now embedded in the Metronome tool. My-voice recording is now take-then-keep: record a count word, listen (▶), press ✓ to save (localStorage, device only) or ✕ to discard; nothing is saved until ✓. Verified with a fake microphone in headless Chromium (draft not stored until Keep). Not a shared/built-in voice: clips stay on that device; making it a built-in voice for all students would need audio files in audio/count/.

- **Phase 235 (2026-10-01) -- Several recorded voices per device.** My-voice storage upgraded to `pb_myvoice_v2` = `{active, profiles:{id:{name, clips}}}` (auto-migrates the old single voice into "My voice"). The recorder panel (in the Metronome / Sound settings) has voice chips (name · clips recorded/9), "+ Add a voice", rename, delete (two-step). Switching a voice switches what the count says, live. **Per-student login plan:** each profile has a plain id, so an account can map to a profile id and clips can later move from localStorage to Supabase (e.g. a `student_voices` table + storage bucket) without changing the UI or `sayCount`. Verified in headless Chromium with a fake mic: migration, add, record, switch, persist across reload.

- **Phase 236 (2026-10-01) -- Tones & semitones moved forward; accidental examples with key signatures.** Category split: **Tones & semitones** (`tones`, 4 tools) now sits right after Reading the staff and before Pulse & counting; **Intervals** (`intervals`, 7 tools incl. Step/skip/same) sits before Scales & keys. `AccidentalBar` ("How long an accidental lasts") grew from 2 to 6 examples: Sharp, Flat, **G major (♯)** and **F major (♭)** (key signature drawn on the staff; key-signature accidental, natural cancelling it, bar line restoring it), **A visitor in the key** (C♯ in G major), **Other octave** (accidental only affects the same pitch). Staff widens for longer bars. Order now: Posture · Piano keys & note names · Reading the staff · Tones & semitones · Pulse · Note values · Time signatures & patterns · Reading tunes · Tempo · Intervals · Scales & keys · Chords · Melody & form · ... 18 categories.

- **Phase 237 (2026-10-01) -- Metronome also in Practice helpers.** New `TOOL_ALSO_IN` map lets a tool appear in a second Toolbox category without moving its home: `metronome` stays in Tempo and is listed first in Practice helpers (4 tools). It was already on the Practice page (`PRACTICE_IDS`).

- **Phase 238 (2026-10-01) -- Count along: accents + more time signatures.** `BeatPulse` now covers 2/4, 3/4, 4/4, 2/2, 5/4 (local `BEAT_EXTRA`, not in `TIME_SIGS`), 3/8, 6/8, 9/8, 12/8. Accent marks (>) over strong/medium beats, light sizes by stress, a Strong/medium/weak caption, compound time grouped in threes, tempo per note value. Verified: Babel compile + Playwright all signatures, 0 page errors.

- **Phase 239 (2026-10-01) -- Same name, note or rest: more rows.** Added demisemiquaver (new 3-flag note + 3-dot rest glyphs in `NoteShape`/`RestShape`) and dotted minim/crotchet/quaver notes and rests (rest dots drawn in `Glyph`), with beat counts shown on dotted rows. Verified by compile + Playwright screenshot.

- **Phase 240 (2026-10-01) -- Rhythm activities: Dot lab + dotted/demisemi quiz.** New tool `dot-lab` (ch note-values, also a lesson step): pick value, note/rest, dot on/off, beat-ruler bar with brass dot part, beat-tick playback (rests silent). Notes & Rests drill: demisemiquaver now in name/beats/rest/sum/fill via quiz-only pools (`QZ_*`), new Level 6 'Dotted notes & dotted rests' (dotted note -> dotted rest, plain-rest trap). `fmtBeats` handles eighths. Verified by compile + Playwright, 0 errors.

- **Phase 241 (2026-10-01) -- Beams + two rhythm games (Notes & rests).** New tools: `beam-apples` ('One beat = one apple': Apple SVG cut into halves/quarters = beamed quavers/semiquavers, beam on/off, plus a 4-beat 'slice a bar' with playback; uses `Apple`, `BeatNotes`, `playBeatPattern`), `fix-the-bar` (tap symbols until 4/4 adds up; many answers accepted), `heard-bar` (hear sound/silence per beat, pick the written bar). All also lesson steps in Notes & rests and in CHAPTER_TOOL_ORDER. Verified by compile + Playwright screenshots, 0 errors.

- **Phase 242 (2026-10-01) -- Note/rest naming: beats on every row, full dotted set.** Every row shows its beat count; dotted rows now run semibreve to semiquaver, in the same order as the plain ones.

- **Phase 243 (2026-10-01) -- Whole-bar rest merged into 'Same name, note or rest'.** `WholeBarRest` became `WholeBarRestBody`, shown under the naming table; separate tool `whole-bar-rest` and its lesson step removed (TOOLS, TOOL_META, CHAPTER_TOOL_ORDER, icon).

- **Phase 244 (2026-10-01) -- Beams in MelodyStaff + bar-lines in 9 time signatures.** `MelodyStaff` now beams quavers that share a beat (group stem direction by majority, flat beam, viewBox grows to fit) instead of lone flags, so all Reading-tunes tools/tunes show real beaming. `BarLineBuilder` offers 2/4, 3/4, 4/4, 2/2, 5/4 (local `BEAT_EXTRA`), 3/8, 6/8, 9/8, 12/8 (8-bottom bars use the small pool; 9/8 and 12/8 show 2 bars); `fillBar` allows up to 8 items for the small pool. Verified compile + Playwright, 0 errors.

- **Phase 245 (2026-10-01) -- Time signatures: 2/2 halving, common/cut time, grouping bug, tuplet lanes.** (1) `BeatDoubler` renamed 'The bottom number changes the beat': chips 2/4/8 on the bottom; 2 halves every value and counts a 2/2 bar as '1 & 2 &' (new `TWO_BARS`). (2) New tool `common-cut` (`CommonCutTime`, `CommonCutSign`): C = 4/4, cut time = 2/2, also a lesson step. (3) BUG FIX in 'Group the quavers' (`makeGroupingQ`): options could look identical (patterns with no beamable pairs) because the check compared raw group labels, not the visible beam structure; now compares beam structure (25x4 trials, 0 identical). (4) `DupletDemo` rebuilt as 'One beat, cut up different ways': all lanes stacked on one shared beat (compound: 1, 3, duplet 2, quadruplet 4, 6; simple: 1, 2, triplet 3, 4, quintuplet 5, sextuplet 6) with fraction labels and darker guide lines where lanes coincide. Verified compile + Playwright, 0 errors.

- **Phase 246 (2026-10-02) -- Lesson/Toolbox audit: no more lesson-only content.** Scripted audit of every `*Learn` function's steps against TOOLS found 16 pieces visible only inside the full lesson. Each is now its own Toolbox tool (and the lesson step reuses the same component): `time-sig-numbers` + `compound-time` (via `TimeSigNumbers`/`CompoundTimeList`/`useTimeSigRows`), `note-value-tree`, `dotted-notes`, `rhythm-cards-all` (`RhythmCardsBrowser`), `all-keys` (`KeySigAllKeys`), `major-shape`, `major-fingering` (`MajorFingeringSet`: patterns+path+drill), `minor-fingering` (`MinorFingeringSet`: patterns+path+viewer), `dc-ds-coda` (`SignsDCDS`), `grand-staff` (`GrandStaffIntro`), `hand-split`, `clef-costume`, `finger-friends`, `best-friends`, `accidental-cards`. CHAPTER_TOOL_ORDER updated to match lesson step order; icons borrowed from sibling tools via an alias loop (redraw in the design phase). Audit method: parse Step blocks per Learn function, list JSX components, compare with TOOLS `C:` components. Verified: compile, every new tool loads, 9 affected lessons render, 0 page errors.

- **Phase 247 (2026-10-02) -- Toolbox tools carry their own explanations; bar-line types; tuplet lanes simple-first; Time Signatures category split.** (1) 51 generated `Expl...` wrappers so the lesson-step Rule text shows above each tool in the Toolbox (where the lesson interleaves Rule + tool). (2) `BarLineIntro`/`BarLinesFull`: bar line, double bar, final bar, start/end repeat drawn as glyphs, with the 'Put in the bar lines' game under it. (3) Duplets/tuplet lanes: Simple beat (crotchet) is now the default tab; the big beats 1,2,3,4 are drawn as blue lines with a legend (tan = where lanes line up, red bracket = tuplet) so they are not confused with tuplet brackets. (4) New category `rrhythm` 'Compound time & rhythm patterns' split from `rtime` 'Time signatures' (basic); CAT_CHAPTER_ORDER rtime:['time-signatures'], rrhythm:['rhythm']. Icons borrowed until the design phase. Verified: compile, screenshots of bar-lines/duplets/triad tools, tool sweep.

- **Phase 248 (2026-10-02) -- Bar-line tool chips below title; neutral example name; reverse audit.** Time-signature chips in 'Put in the bar lines' now sit under the title (phone-friendly). Removed the 'Clara' example from the Finger Friends tool text (Sohyun undecided between Piano Butler / Clara Music branding -- keep examples neutral, no recurring named character). Reverse audit (tools whose component appears in no lesson step): only practice-page tools plus `black-white-neighbours`, `modes`, `seventh-chords`, `chord-extensions` -- advanced extras, left as tool-only. Pending her check: tuplet naming ('5 in the time of 4') and the blue beat-line reading.

- **Phase 249 (2026-10-02) -- Toolbox layout: art on categories, thin tool rows.** Category headers now carry a 64px illustration (`CAT_ART` map borrows a representative tool icon; real chapter heroes come in the design phase) and tool rows under them are slim one-line rows (48px icon, title + one-line blurb with ellipsis, level tag right, hidden on phones). Verified by screenshot at 700px; no page errors.

- **Phase 261 (2026-10-02) -- Note-value tree redrawn as a true tree**: each level is a bar cut into 1/2/4/8/16 equal boxes; every box shows the note, the matching rest under it, and its beat count under that (4 beats ... ¼), with "N pieces = one semibreve" per row. Checked at 700px and 390px.

- **Phase 260 (2026-10-02) -- Notes & Rests re-sequenced again (lesson + Toolbox) per Sohyun**: values/names/rests -> Rests: counted but silent -> Note↔rest match -> Split the notes -> One beat = one apple -> Dotted notes -> Dot lab -> Fix the bar -> Fill the bar -> Which bar did you hear. Also fixed a real intermittent crash in `makeBrokenBar` (Fix the bar): when the remainder was smaller than any note (e.g. after a dotted quaver) `pick([])` returned undefined and `.beats` threw; now breaks and retries. Verified with 5000 generator runs, 0 errors.

- **Phase 259 (2026-10-02) -- Merged "The note-value tree" and "Same name, note or rest" into one tool** "Note values, names & rests" (`NoteValuesTool`, chips: Splitting tree | Names, rests & dots). Old id note-rest-naming stays reachable by link but hidden from the list. Lesson steps unchanged. Notes & Rests = 10 rows.

- **Phase 258 (2026-10-02) -- Notes & Rests reordered by level and teaching logic, lesson and Toolbox together.** New order: note-value tree, same name (note/rest), note↔rest match, one beat = one apple (beams), split it, dotted notes, dot lab, fix the bar, which bar did you hear, fill the bar, writing rests correctly (G1+). Dot lab level raised from Beginner–Prelim to Prelim–G2 (it needs dotted notes first). Verified: lesson shows steps 1-11 in this order, Toolbox shows the same order, no errors.

- **Phase 257 (2026-10-02) -- New Toolbox category "Writing notes & ledger lines" (id `ledger`) right after Reading the staff**, holding the 6 tools separately: write-note, alto-clef, ledger-walk, ledger-landmarks, ledger-twins, ledger-write (an earlier bundle-into-one-tool attempt was a misreading and was reverted). `ledger-lines` chapter now maps to this category in the Learn path too. Reading the staff = 9 tools. Verified by rendering both categories; no errors.

- **Phase 256 (2026-10-02) -- Hands & Clefs chapter removed from the app** at Sohyun's request (confusing alongside its tools): unregistered from DRILLS, STAGES, level map, hero map, CHAPTER_CAT, CAT_CHAPTER_ORDER and search keywords. Code (HandClefsLearn, HAND_CLEFS_DRILL, HandSplit, ClefCostume, GrandStaffIntro) is left in the file, unreachable, so it can be restored by re-adding those registrations. An old ?drill=hand-clefs link now just opens the home screen. Verified: compile, home, Learn, Practice, neighbouring lessons, no errors.

- **Phase 255 (2026-10-02) -- Toolbox order = lesson order.** Scripted audit (parse each *Learn function, map components to TOOLS, compare with CHAPTER_TOOL_ORDER) across all 24 chapters: fixed staff (fold before landmarks), tones (tone-semitone first, accidental-cards before sharp-flat), note-values (dotted-notes before beam-apples). Also the Toolbox now orders the chapter groups inside a category by lesson-path order (`chapterOrder` in ChapterGroups; rrhythm shows Time Signatures group before Rhythm Patterns). Tools with no lesson step (seventh-chords, chord-extensions, touch-lengths, black-white-neighbours) sit at the end of their chapter. Verified by expanding every category and reading the rendered order.

- **Phase 254 (2026-10-02) -- Merged "Best friends: semitones" into "Tone or semitone"** (one tool, two chips: Count the steps | Best friends; `ToneSemitoneTool`; best-friends tool entry removed). Lesson steps unchanged.

- **Phase 253 (2026-10-02) -- Removed 4 Hands & Clefs tools from the Toolbox** (grand-staff, hand-split, hand-clef-match, clef-costume) at Sohyun's request ("for now"). The Hands & Clefs lesson and practice drill are untouched; the components (GrandStaffIntro, HandSplit, ClefCostume, hand-clef-match icon) remain in the file so tools can be restored by re-adding TOOLS entries.

- **Phase 252 (2026-10-02) -- Grand Staff tool shows the staff picture; Sydney CBD removed (neutral wording); middle C marked blue on the Split-the-keyboard keyboard.**

- **Phase 251 (2026-10-02) -- Toolbox tool rows are icon-free text lists** (title + one-line blurb, level tag right, category-colour left bar; category headers keep their art).

- **Phase 250 (2026-10-02) -- Simple/Compound merged into one tool.** The Toolbox tool 'The two numbers' now has a Simple time / Compound time toggle (the separate `compound-time` tool is removed from TOOLS, meta, icon alias and chapter order). Simple list now also shows 3/2 and 5/4 alongside 2/4, 3/4, 4/4, 2/2, 3/8 (`BEAT_EXTRA` gained 3/2); level widened to Beginner-G4. Lesson step 'Compound time' unchanged. Verified: compile, both screenshots, lesson page loads, 0 errors.

| 262 | 2026-10-02 | **Design phase stage 1 (Toolbox):** Sohyun chose the "staff look" (navy #26296b + coral #e4572e, five-line staff headers with the title knocked out, Playfair Display titles, note-head bullets). drills.html: new tokens `--navy/--coral/--navy-soft/--navy-line`, Playfair font link, `.stf-head/.stf-title/.stf-count` CSS, Toolbox topic header and ToolRow restyled (level now inline after the blurb, no card boxes). Verified: Babel compile + Playwright at 390px and 1000px, no page errors. Mockups: Design artifact "Toolbox Header Options" (rows V3/V6). Not yet rolled out: page background/other screens, home, tool pages, student view. |

| 263 | 2026-10-02 | **Design phase stage 2 (global colours):** drills.html palette switched file-wide from ink/brass/buttercream to navy #26296b / coral #e4572e / paper #f6f4ef (brass #a8823f -> coral, ink #241f1a -> navy, borders -> #dcdcea, muted browns -> #6d6f9c); h1-h3 use Playfair Display. Old illustration icons got the same swap (their brass accents are now coral) and are still to be redrawn. Verified: Babel compile, 390/1000px screenshots, 139-tool sweep with 0 errors. Still old-style: tool-page layouts, student view, home layout, tab bar, curve motif. |

| 264 | 2026-10-02 | **Design phase stage 3 (Learn + Practice lists):** the student Learn / teacher All-chapters screen no longer shows the big hero-picture cards; each topic is a staff-line header with slim chapter rows (note bullet, title, grade tag, tick count). Practice tab is a slim list too. New shared components `NoteBullet`, `StaffHead`, `PageIntro`, `SlimRow`; narrow-phone title size via media query. Chapter hero art (HERO_MAP) is now unused on these lists but still used inside chapter pages -- to be restyled or dropped next. Verified: Babel compile + 390px screenshots. |

| 265 | 2026-10-02 | **Design phase stage 4 (lesson pages):** `Lesson` component restyled -- no card box, 30px serif chapter title, staff-line divider, step chips and steps alternate navy/coral (`STEP_COLORS` now 2 colours), step titles in Playfair, quiet left rule. The per-chapter `head` hero pictures are no longer rendered (Hero components kept in file for a later redraw; `HERO_MAP` unused). Verified: Babel compile + 390px screenshot of Reading the staff lesson, no page errors. Not yet: inner tool/panel colours (e.g. pink 'Try it' panels), student view layout, tab bar. |

| 266 | 2026-10-02 | **Design phase stage 5 (tabs + activity panels):** top Plan/Practice/Students (student: Learn/Practice) switch is now serif text tabs with a coral underline; `actBox` (the 'Try it' panel) is white with a thin navy-line border and soft shadow instead of the pink fill. Verified: Babel compile + 390px screenshot. Still to do: bottom tab bar/staff motif and curve (not used in app), student home 'Keep going' resume card (needs progress logic), redraw of chapter heroes (optional), full 139-tool sweep after the colour work. |

| 267 | 2026-10-02 | **Design phase stage 6 (full sweep, Sohyun: change everything design-related without waiting):** ~1,290 remaining hard-coded colours mapped to the staff theme -- illustration cream -> #fbfaf6, mustard -> ochre #e9a83a family, good green -> #2e8a6e, bad red -> #c8361b, sky/blue -> #3b4fa8 family, teal -> #2b8c8c, browns -> navy neutrals, beige tints/borders -> navy tints; brass/buttercream rgba too. All `TOOL_CATS` colours -> coral. Buttons are pills (primary navy, ghost navy-line), search is a navy pill, `.chapter-link` is an underlined coral text link, cards get navy-line border + soft shadow, TRY IT tag coral, lesson Learn/Drill switch is two pills. Black piano keys are now navy (deliberate, matches the two-colour look -- revert to near-black if it reads oddly). Verified: Babel compile, 139-tool sweep 0 errors, screenshots of 12 illustrated tools + Toolbox/Practice/Students/drill. |

| 268 | 2026-10-02 | **Design phase stage 7 (chrome):** top header bar now sits on paper with a five-line staff band along its bottom edge; Find button uses an inline SVG magnifier instead of the emoji. Verified: Babel compile, 390/1000px screenshots. Design phase rollout (Pending #0) is now applied across drills.html; remaining optional items: redraw chapter hero art in the staff style, student 'Keep going' resume card. |

| 269 | 2026-10-02 | **Paper colour warmed:** Sohyun found the grey paper (#f6f4ef) too cold and wanted natural manuscript-paper ivory. drills.html `--bg` -> #f6f0e1, `--surface` -> #fffdf8, `--border` -> #e4dcc8; the cool navy-tint neutrals (#f4f3ee, #efeef5, #f1f1f8, #ecebf3, #e6e6ef, #dcdcea, #d4d4e4, #c9c9dc, #c4c4d6) and the illustration cream (#fbfaf6) moved to matching warm ivory tints. Navy/coral unchanged. Verified: Babel compile + 390px screenshots. |

| 270 | 2026-10-02 | **Staff theme across the whole site (Sohyun: change the entire Piano Butler design to this theme, no approval needed).** (a) drills.html paper brightened again to #faf6ec (Sohyun: ivory looked a little old) with matching tints; navy black keys kept (her call). (b) 45 public pages + piano-butler-logo.svg themed with one idempotent script (`_workspace`-free; kept in session scratchpad as theme.py): ink -> navy #26296b, brass/terracotta -> coral #e4572e, buttercream/greys -> ivory #faf6ec + warm/navy neutrals, cool slate/gray hexes -> navy-leaning neutrals; a Tailwind config override remaps the `slate`/`gray` classes on Tailwind pages; Playfair Display injected for h1-h3. Repertoire pages: each board's colour was its page chrome -> now navy for all interactive parts, and the board colour survives only as the title marker bar (AMEB #8a2f4a, ABRSM #3b4a6b, Trinity #1e4d2b) and on the home page grade-group borders. Era / list / syllabus badge colours untouched (informational). index.html: ivory sticky header with a staff band, serif wordmark, the four emoji card icons replaced by navy/coral line icons. privacy.html converted from its dark page to ivory/navy. Not touched (internal): admin-counts, admin-search, teacher-dashboard, butler.html. Verified: all 45 pages load with no page errors in headless Chromium (Tailwind built locally to preview); screenshots of home, every page type at 390/1200px; device files checksum-identical to the verified copy. |

| 271 | 2026-10-02 | **Decorative emoji -> line icons (site).** 26 public pages: diagnose (hero + Technique/Ear/Theory/Sight-reading domain icons), recommend (six playing-style icons; syllabus choices now a board-colour dot instead of flags), teach-with-us (perks, success, Apply button), sight-reading (What it does), index (Random Pick, Shuffle, My Lists, syllabus pills -- the 'X only' sentence now reads the key so it never prints [object Object]), viva-voce buttons, repertoire pages (Searching, General/Leisure tabs, empty state, 'Also see AMEB', diploma info list). Icons are 24px-grid navy line drawings with a coral accent, sized in em so they scale with the text. Symbols (sharps, flats, ticks, crosses) kept. Verified: 45-page headless sweep, 0 page errors; screenshots of each changed page type; device files checksum-identical to the verified copy. |

| 272 | 2026-10-02 | **Chapter pictures redrawn as staff drawings.** New `ChapterArt` + `STAFF_ART` in drills.html: one wide navy/coral drawing per chapter on the same five-line staff band (viewBox 360x100), shown under each lesson title in place of the plain staff divider. Each shows its own idea literally: arched hand over keys, black-key groups of 2 and 3, A-G alphabet looping back, four even beats, semibreve = 2 minims = 4 crotchets, a rhythm card counted 1 2& 3 4, line notes vs space notes, steps vs skips, ledger lines with middle C, 4/4 with two bars, metronome + Adagio/Allegro/Presto, p < f with staccato and legato, a repeat sign with a loop-back arrow, Italian terms, semitone vs tone on keys, the C major scale C to C, the order of sharps F C G D (drawn as lines), C up to G = 5th, triads C G F, clavichord/harpsichord/piano, low vs high waves, a phrase arc, A B A, three textures. Treble clef reuses the app's measured `ClefGlyph` scaled to the 4px staff. Fix: the Scales lesson's Major/Minor switch had been hidden since Phase 265 (it lived in the `head` prop alongside the hero); `head` now carries only that switch and is rendered again, and the 23 old `head={<XHero/>}` props were removed. Verified: Babel compile; all 24 chapter pages screenshotted at 390px with Noto Music/Playfair loaded locally, no page errors; 139-tool sweep 0 errors; device file checksum-identical to the verified copy. |

| 273 | 2026-10-02 | **Korean for the redesign strings.** drills.html: Learn / All chapters / Practice page titles and intros, 'Practice tools', every label in the 24 chapter drawings (줄/칸, 반음/온음, 가운데 도, 5도, 클라비코드/하프시코드/피아노, ...), the lesson Learn/Drill switch (배우기/드릴) and the student-preview banner now go through t(). Terms follow the app's existing Korean (반음, 온음, 가운데 도, 줄과 칸, 건너뛰기, 프레이즈, 선율, 5도). Note: category names/blurbs (TOOL_CATS) and chapter labels (DRILLS) were English-only before the redesign and still are -- part of the existing translation backlog. Verified: compile + KO screenshots of Learn and a lesson page. |

| 274 | 2026-10-02 | **Screen audit after the redesign.** Clicked through screens not covered before: home search results, Random Pick (before/after picking), Contact pop-up, Recommend steps 2-3 and results, Timeline step 2, Diagnose questions and results, Viva Voce grade picker, sight-reading loading page; drills Find overlay (with a search), Students add form, a drill before/after a wrong answer, pixel game start, Plan with the add-student field. Only fix needed: the home page Contact pop-up was still a dark (#1e1e1e) panel -- now ivory/white with navy text, warm inputs and a navy pill Send button (index.html). Diagnose's per-domain chart colours and the era/list badges are informational and were left as they are. No page errors anywhere. |

| 275 | 2026-10-02 | **Student 'Keep going' card.** drills.html: the App remembers the last chapter opened (`pb_last_chapter_v1` in localStorage, try/catch, only ids in CHAPTER_CAT), and the student Learn page opens with a card -- coral 'KEEP GOING' label, the chapter name in serif, 'n steps done' (or 'Pick up where you left off'), navy Resume pill -- above the topic list. Hidden for teachers and when nothing has been opened yet. Korean included (이어서 하기 / 이어하기). Verified: compile; headless run: fresh visit shows no card, open Reading the Staff -> Got it -> back shows 'Reading the Staff, 1 step done', Resume reopens the lesson; no page errors. |

| 276 | 2026-10-02 | **Korean topic and chapter names.** drills.html: `CAT_KO` (20 topic names + one-line descriptions) and `CHAPTER_KO` (24 chapter names). `TOOL_CATS[].name/when` and `DRILLS[].label` (chapters only) are now getters that follow LANG, with English kept as `nameEn/whenEn/labelEn`; tool search reads both languages. Terms match the app's existing Korean (다이나믹, 이음줄, 여린내기, 보통박자와 얼라 브레베, 알토음자리표, 손가락 번호, 스케일, 튠, 시퀀스, 케이던스, 텍스처, 템포 경주); 덧줄 newly introduced for ledger lines. Tool titles/blurbs remain English-only (existing backlog). Verified: compile, KO screenshots of Plan/Toolbox, Learn and a lesson, 139-tool sweep 0 errors, device checksum-identical. |

| 277 | 2026-10-02 | **Korean tool titles and blurbs.** drills.html: `TOOL_KO` gives all 133 tools a Korean title and one-line blurb (TOOLS[].title/blurb are now LANG-aware getters; English kept as titleEn/blurbEn; search reads both). Toolbox filter chips (모든 레벨 / 입문 / 모든 종류 / 보여 주며 설명 / 학생이 직접 / 듣기 / 이론 쓰기 / 집에서 연습; exam level names Preliminary and Grade x-y kept as in the syllabus), the search placeholder, '+ 학생', '추가', 'My student...' (우리 학생은... / 눈에 띄는 것을 골라요), '+ 학생 추가' and the empty-students note. Standard Korean theory terms used: 으뜸음/윗으뜸음/이끔음, 자연·화성·가락 단음계, 나란한조, 딴이름한소리, 5도권, 근음, 전위, 정격·변격·반·거짓 종지, 댐퍼 페달, 아차카투라/아포자투라, 2잇단음표/셋잇단음표, 여린내기(못갖춘마디), 홑박자/겹박자. A leftover brown (#8f6216) on the chosen 'My student' problem is now coral. Still English: PROBLEMS list items and most in-tool explanation text. Verified: compile, KO screenshots, 139-tool sweep 0 errors, device checksum-identical. |

| 278 | 2026-10-02 | **Korean 'My student...' list.** drills.html: `PROBLEMS_KO` (18 entries, same order as PROBLEMS) + `probLabel(i)` used in the picker and the chosen line. Verified: compile, device checksum-identical. |

| 279 | 2026-10-02 | **Tempo chapter content pass (approved order: content before design, thinnest first -- Tempo next).** Tempo lesson 3 -> 6 steps, three new tools (Toolbox `rtempo`, Korean included): **What is tempo?** (`TempoWalk`, tool `tempo-walk`): walk / jog / sprint stick figures play 88 / 132 / 184 bpm (Andante / Allegro / Presto, inside the app's own TEMPO_TERMS ranges) with a dot pulsing at that speed. **Tap your own tempo** (`TapTempo`, `tap-tempo`): averages the last taps into bpm and lights the matching words on a tempo ruler built from TEMPO_TERMS. **Same tune, different tempo** (`SameTuneTempo`, `same-tune-tempo`): Twinkle Twinkle (traditional) at Adagio 70 / Moderato 112 / Presto 184 with note bars lighting up, then a mystery-tempo quiz (slow / medium / fast). Tempo lanes recoloured navy-blue -> coral, the turtle/flag emoji removed. CHAPTER_TOOL_ORDER tempo updated; order audit clean. Verified: compile, Playwright interaction run (gait tap, 5 taps -> 108 bpm, mystery quiz feedback), 136-tool sweep 0 errors, device checksum-identical. Next in the approved order: Musical Terms, Melody & Form, Styles. |

| 280 | 2026-10-02 | **Musical Terms content pass.** Two new hands-on steps/tools built on the existing TERMS data (no new facts): **Four families** (`TermSort`, `term-sort`, first step): a term card, four bins with navy/coral icons -- Speed, Changing speed, Loud and soft, Mood and touch (= TERMS[].cat Speed / Changing speed / Volume / Other); answer reveals the AMEB meaning and plays the term; grade filter 1-4; modifier, road-map, which-hand, pedal and catalogue words (Sempre, Poco, Molto, Senza, Assai, Quasi, Non troppo, Subito, Dal segno, Da capo al fine, Attacca, M.D./M.G., Opus, Loco, M.M., Una corda, Tre corde, Ad libitum) are left out of the sort. **Little words, big changes** (`TermMixer`, `term-mixer`, after Grade 2): Molto / Assai / Poco / Non troppo / Sempre with Allegro, Adagio, Crescendo, Diminuendo, Forte, Legato, Staccato; shows both AMEB meanings and plays plain vs changed (molto/assai exaggerate the playback, poco/non troppo soften it, sempre explained as 'keep doing it'). Korean fix: Terms step titles said 학년 (school year) -> 1급-4급, intro 학년별로 -> 급수별로. Verified: compile, interaction screenshots, 138-tool sweep 0 errors, order audit clean, device checksum-identical. Next in order: Melody & Form, Styles. |
| 281 | 2026-10-02 | **Melody & Form content pass ("make your own").** Two new hands-on steps/tools, no new music facts beyond the existing chapters: **Draw a tune** (`MelodyContour`, `draw-tune`, 2nd Melody step): tap the staff to move 8 notes between C4 and C5, play it, and the tool names its shape (rising / falling / arch / valley / wave / all one note) and says whether it ends on C (sounds finished) or not; Arch/Rising/Valley/Wave presets; treble clef reuses `ClefGlyph`. **Build your own form** (`FormBuilder`, `form-builder`, 2nd Form step): A/B/C blocks (up to 7), Play/Undo/Clear, plays through the existing `playFormSeq`, and names AB/AABB as binary, ABA as ternary, ABACA-style as rondo (otherwise "your own shape"). Form colour C changed purple → teal `#2b8c8c` to sit with the staff palette. Korean for both (letter names stay C, matching the rest of the app); Undo/Clear moved beside Play so nothing wraps at phone width. Verified: Babel compile, 390px screenshots EN + KO, full tool sweep 140 tools 0 errors, lesson/toolbox order audit clean, device md5 = container. |
| 282 | 2026-10-02 | **Styles & Genres content pass.** Visual-first upgrade of the thinnest chapter, facts sourced from *Help Your Kids with Music* (`_pb_refextract/full.txt`): **Textures** now draw the exact notes the synth plays as a piano roll (tune; + held chords; + second voice entering 2 beats later) with a moving playhead (`TexturePicture`); **Which texture is this?** reveals that picture after you answer, locks after one guess, keeps a score. **What makes each style different?** gets one picture per family (folk: tune passed ear to ear; classical: written score page; jazz & blues: even eighths played long-short; popular: verse/chorus/verse/same chorus). New **Straight or swing?** (`SwingFeel`, `swing-feel`; book p.40: written in even eighth-note pairs, played long-short "as if in triplets"): same written bar, played-length blocks that stretch 1:1 → 2:1 with gold triplet dots, plays with a soft click, plus an ear test. New **The 12-bar blues** (`TwelveBarBlues`, `twelve-bar-blues`; book p.220: I-I-I-I / IV-IV-I-I / V-IV-I-I, in C = C, F, G, V only in bar 9): colour-coded 12-bar grid, play-through with a moving bar highlight and Stop, tap a bar to hear its chord, and a **Fill the gaps** game (3 bars blanked, always one of the IV/V bars; tap ? to cycle I/IV/V, Check marks ✕). **Korean bug fixed:** `TEXTURE_TYPES` and `GENRE_TRAITS` called `t()` at module level, so their labels stayed English after switching to 한국어 -- now getters (a Babel scan confirms no other module-level `t()` calls remain). Verified: Babel compile, 390px screenshots EN + KO (incl. a played-through 12-bar and a checked gaps round), Styles practice level 3, full tool sweep 142 tools 0 errors, order audit clean, device md5 = container. |
| 283 | 2026-10-02 | **Pitch & Range content pass** (was the thinnest chapter, 2 tools). Three new steps/tools, facts from *Help Your Kids with Music* p.14-16 and p.175 (faster vibration = higher; shorter or tighter string = higher, longer or looser = lower; smaller instruments and xylophone bars play higher; an octave up vibrates exactly twice as fast; the half-string vibration = the octave in the harmonic series): **Shorter, tighter, higher** (`StringLab`, `string-lab`): a G3 string (the violin's lowest, from the app's RANGES) with a finger slider, Whole/¾/Half presets, Loose/Normal/Tight, pluck (harpsichord pluck sound) with a wobble that's faster for higher notes; shows note + Hz (¾ length = C4, half = G4). **Big is low, small is high** (`SizePitch`, `size-pitch`): an 8-bar xylophone, big to small, tap or run up/down; then "which of the violin family plays higher?" -- two instruments drawn to rough scale, answer, then hear each one's lowest open string (G3/C3/C2/E1 from RANGES). **The octave ladder** (`OctaveLadder`, `octave-ladder`): A2-A6 as bars drawn to scale (110-1760 Hz), one number hidden, 3 choices (the trap answers add instead of double). All bilingual. Verified: Babel compile, 390px screenshots EN + KO, full tool sweep 145 tools 0 errors, order audit clean, device md5 = container. |
| 284 | 2026-10-02 | **Pulse content pass.** Two new steps/tools between "Feel the pulse" and "Tap the right beat", facts from *Help Your Kids with Music* p.24-25 (the beat is the steady background that keeps going through long notes; beats are felt in groups of 2, 3 or 4 with the 1s stronger; 2s like a march, 4s most common esp. in pop): **Beat or rhythm?** (`BeatOrRhythm`, `beat-or-rhythm`): "Hot Cross Buns" (traditional) drawn as two lanes -- the tune's note blocks (height = pitch) over 16 beat hearts -- "Listen to both" lights them as they play; then pick tap the beat or tap the rhythm, 4-click count-in, tap button or space bar (audio-clock timing with output-latency correction, like SteadyBeat), and the lanes mark every hit/miss plus a one-line lesson (the beat kept going through long notes; the rhythm stopped and got busy). **Strong and weak beats** (`BeatGroups`, `beat-groups`): in 2s/3s/4s, a big navy "pat" circle for the 1 and small coral "clap" circles, low drum + accented click on the 1, lights in time; ear test (2s, 3s or 4s?) with score. Bilingual. Verified: Babel compile, 390px screenshots EN + KO including a scripted tap run (13/16 with 3 deliberate skips), full tool sweep 147 tools 0 errors, order audit clean, device md5 = container. |
| 285 | 2026-10-02 | **The Piano's Story: "Inside the piano"** (`PianoAction`, `piano-action`, new step after "Cristofori and after"). Facts from *Help Your Kids with Music* p.180-181 (press a key: the hammer strikes the strings and a felt damper lifts; let go: the damper returns and stops them; the sustaining pedal lifts all dampers; una corda moves the hammers sideways so they strike only one of the two or three strings; the middle pedal sustains only certain pitches; grand strings horizontal, upright vertical). A side-view diagram of key (lever on its balance rail), push rod, hammer on its shank, damper and steel string: hold the key (button or tap the diagram) and the key tips, the hammer strikes and drops back, the damper lifts and the string wobbles and fades; let go and the damper drops and the sound stops instantly (own synth voice so the damper can cut it). Right-pedal toggle keeps the dampers up so the note rings after release; left-pedal (una corda) toggle slides the hammer in a top-view inset from 3 strings to 1 and the note gets softer and darker. Status line explains each state. Bilingual. Verified: Babel compile, 390px screenshots EN + KO (rest, key held, pedal-held release, una corda), full tool sweep 148 tools 0 errors, order audit clean, device md5 = container. |
| 286 | 2026-10-02 | **Korean pass: The Piano's Story, Pitch & Range, and the shared drill chrome.** (1) **The Piano's Story** fully bilingual: `ANCESTORS`, `TOUCHES`, `PIANO_TIMELINE`, `ERAS` string fields became getters (`get name() { return t(...) }`, era traits/composers swap whole arrays; new `short` era name for the era bar), Mechanism labels, KeyboardAncestors/TouchLengths/PianoTimeline/ErasTimeline UI text, the three tips, lesson title/intro/step titles, and the drill question bank (`STORY_QS_KO`, same order as `STORY_QS`; `genStoryQuestion` picks by index and uses the Korean row when 한국어 is on). Composer names in Korean transliteration (바흐, 헨델, 스카를라티...); era names 바로크/고전주의/낭만주의/20세기. (2) **Pitch & Range**: HzExplorer and RangeChart text, tips, lesson; instrument/voice/history names via `RANGE_KO` + `rangeName()` (English name stays the id). (3) **Drill chrome** (lesson mode; pixel game mode deliberately stays English arcade style): question counter, correct count, Correct!/Not quite/Time's up, Next, Finished/best/Go again, Level chips, Lesson/Game mode, student link, worksheet link. (4) **Every drill level name** (119 labels across 28 drills, incl. rhythm-card tiers) via `LEVEL_KO` + `lvName()`. Korean grade terms: 예비급 (Prelim), N급. Babel scan: still no module-level `t()` calls. Korean sweep: English-only lines 294 → 259 (Piano's Story and Pitch & Range now 0). Known limit: a question already on screen when you switch language stays in the old language until the next question. Verified: Babel compile, KO screenshots of all 6 original tools + a Korean piano-story drill round, full tool sweep 148 tools 0 errors, order audit clean, device md5 = container. |
| 287 | 2026-10-02 | **Korean pass: Scales chapter.** Fingering patterns (`SCALE_PATTERNS`/`MINOR_PATTERNS` title+text as getters, row labels via `PAT_ROW_KO`), ScaleFingeringDrill, ScalePath (scale cards: 오른손/왼손/양손, kept on one line), MinorFormsCard (자연/화성/가락 단음계; `MINOR_FORMS` labels as getters), MinorViewer, ScaleFinder (typing still takes English names like "F# minor"), MajorShapeCard, ScaleBuilder (incl. the right object particle 스케일을/단음계를), DegreeNames (으뜸음, 윗으뜸음, 가온음, 버금딸림음, 딸림음, 버금가온음, 이끎음 via `DEGREE_NAMES_KO`/`DEGREE_WHY_KO`), Modes (Korean name + Latin in brackets, formula and mood via new `nameKo`/`formulaKo`/`moodKo`). Also the Toolbox row's "Learn the whole chapter →" and student-link buttons (that code shadows `t` with the tool object, so it uses `LANG` directly). Verified: Babel compile, Korean full-page screenshots of all Scales tools, full tool sweep 148 tools 0 errors, order audit clean, device md5 = container. |
| 288 | 2026-10-02 | **First Steps content pass.** Two new steps/tools: **The whole piano** (`WholePiano`, `whole-piano`): all 88 keys, count the 2- and 3-black-key groups ("houses") after a guess (5 / 7 / 10), the lone A♯0 at the bottom, and a middle-C mode. **Black-key jam** (`BlackKeyJam`, `black-key-jam`): a two-chord bass loop to improvise over on the black keys only. Toolbox order = lesson order (CHAPTER_TOOL_ORDER first-steps). Korean for the chapter's tools and drill. Verified: compile, t288.js interaction test, EN/KO screenshots. |
| 289 | 2026-10-02 | **Reading tunes content pass.** **Hear it, find it** (`HearFind`, `hear-find`, step after Echo): "Which tune?" (hear 4 notes, pick the written tune of three that differ in shape) and "Spot the change" (a 2-bar tune plays with one note moved by a step or a skip; tap it; the answer shows what was heard). C position, crotchets in 4/4. Whole chapter now in Korean; MelodyStaff counts "1 앤 2 앤" in Korean. Verified: t289.js, screenshots. |
| 290 | 2026-10-02 | **Colour words, palette and emoji.** Instructions that name a colour now match what is drawn (orange/주황색 for coral marks, "shaded", the gold part of the dot bar, tuplet label); ScaleTapKeyboard uses MARK_STYLE; the ✂ emoji is now a `PrintIcon` SVG. |
| 291 | 2026-10-02 | **Korean pass, part 1:** Ledger Lines, Posture & Hand Shape, Musical Terms (`TERM_MEANING_KO`, all 96 AMEB meanings, kept distinct so quiz choices never repeat), Staff, Dynamics, Time Signatures (`TS_USE_KO`, `UNIT_KO`), Intervals (`IV_QWORD_KO`), Key Signatures. `fmtBeats` says N박; BoxLabel widths count Hangul. |
| 292 | 2026-10-03 | **Korean pass, part 2 -- backlog closed.** Note Values (`NV_KO`; `nvItem().uk` is now a LANG-aware getter, `ukEn` keeps the English), Rhythm (Count harder rhythms, anacrusis = 못갖춘마디/여린내기, Make your own card), Tones (accidental cards/bar, push-a-key, chromatic scale), Signs (road map, 8va, ornaments, grace notes), Note Names, Chords (triads, Roman numerals, primary triads, inversions, cadences, 7th chords, extensions), Pulse, Tempo (meanings, speed changes, metronome), Melody/Form/Dynamics/Time-signature/Pitch & Range drill answers, the practice tools (dice, timer, 5 in a row, sight-reading cards) and the back buttons. Drill answers stay English keys and are shown through display mappers (`chordLabel`/`chordName`, `tsLabel`, `tieSlurName`, `chKo` + `CHOICE_KO`, `q.show` + `rangeName`), so answer checking is unchanged. **Accuracy fixes to earlier Korean:** solfège replaced by letter names per the standing decision (도♯ → C♯, 레장조 → D장조, 시단조 → B단조, 미♭장조 → E♭장조, "도 레 미 파 솔" → C D E F G; "가운데 도" kept as the term); tie = 붙임줄 and slur = 이음줄 (both had been 이음줄); cadences = 완전종지 / 변격종지 / 반종지 / 위종지 (Imperfect had been 불완전, Interrupted 반종지); inversions unified to 근음 위치 / 제1전위 / 제2전위. Verified: new KO scanners in the sandbox (`engall.js` every lesson, `engdall.js` + `mixed.js` every drill level, `engtools.js` all 151 tools) leave only Italian terms, pronunciation guides, counting syllables, English mnemonics and song titles; sw.js sweep (151 tools + 24 chapters, EN and KO): 0 errors. |
| 293 | 2026-10-03 | **Black-key songs: Korean title.** In Korean mode "Mary Had a Little Lamb" shows as **떴다 떴다 비행기** (the same melody Korean children know: E D C D E E E ...); "Hot Cross Buns" shows as 핫 크로스 번. Song chips use a `chip` getter instead of slicing the English title. Sohyun approved 2026-10-03. Verified: compile, KO screenshot. |
| 294 | 2026-10-03 | **Do Re Mi beside the letter names (Sohyun's decision A).** Fixed do -- C is always 도/Do in every key (C♯ = 도♯, B♭ = 시♭). Korean mode always shows it; English mode only when a teacher taps the new **Do Re Mi** chip in the header (teacher view; remembered per device in `pb_solfa_v1`), because Australian classrooms often use movable do. Helpers `solfaOn()`, `solfa(n)`, `withSolfa(text)` and `<NoteName n/>` (letter with its syllable under it). Shown on keyboard letter labels (`TapKeyboard`), the note-name, staff, ledger-line and steps-and-skips drills (choices and answers), the letter-step drill, Find every C, the letter chain and `MelodyStaff` note names. Verified: compile, KO/EN screenshots. |
| 295 | 2026-10-03 | **Printed books: Lesson Book + Workbook (Sohyun: paper first, basics first; a chapter test that checks every concept evenly; the whole thing should work as physical books).** New print routes in drills.html: `?book=lesson&ch=<id>\|all&lang=en\|ko` renders a chapter's own Learn page for A4 (global `BOOK` flag: `Lesson`/`Step` switch to a paper layout, action buttons and the TRY IT tag hidden, page numbers and running head from `@page` margin boxes, chapter QR code to the app). `?book=work&ch=staff&lang=..` renders fixed A4 workbook pages. **Sample built: Reading the Staff workbook, 10 pages** -- opener (concept checklist tied to lesson steps, warm-up, QR), line-or-space, which-is-higher, name 15 treble / 15 bass notes (letters spread evenly so every note gets practised), note words + write-your-own, find middle C, join landmarks, write the notes, At the piano (7-day ticks, practice minutes, parent/teacher sign-off, teacher's note, sticker/stamp space, QR to the drill), a **chapter check-up** (20 marks, 5 concepts weighted evenly, a per-concept score row with pass mark and "review lesson step N, exercise M"), and answers. Every item comes from a seeded generator (`withSeed`), so reprints and answer keys never drift. `PaperStaff` draws compact staves (semibreve heads, wider grand-staff gap for middle C). QR codes come from qrcode-generator (MIT, inlined as a plain script). `?lang=ko` link parameter added. PDFs made with headless Chromium: fonts embedded, Hangul in a Korean font (`<html lang>` set). Sandbox note: the test harness was serving the font CSS in place of the font files, so every earlier screenshot used fallback fonts -- fixed. Verified: compile, page-overflow check on every workbook page, PDFs inspected page by page in EN and KO, full sweep 0 errors. |
| 295b | 2026-10-03 | **Scale finder fixes (Sohyun).** Every black-key chip shows both names (F♯ · G♭, C♯ · D♭, B♭ · A♯, E♭ · D♯, A♭ · G♯, D♭ · C♯, G♭ · F♯, B · C♭; the minor chips likewise via `CHIP_ALSO`). F major RH 1 octave now ends on finger 4 (1-2-3-4 1-2-3-4), per Sohyun; F harmonic minor 1-octave still ends on 5 (not asked). Verified: rendered close-up. Commit `7b4cec1`. |
| 296 | 2026-10-03 | **Printed books v2 -- built for 1:1 lessons + homework (Sohyun's decisions).** Workbook pages now follow one lesson step each and have three parts: TOGETHER (done in the lesson, first item a worked EXAMPLE in coral), AT HOME (same task alone, ~10 min) and PLAY (a puzzle or something to create -- Sohyun: "the most important part"). Each page has a homework strip (Lesson step, Set, Due, minutes) and a How-did-it-feel face row; the book opens with "How each page works" and a My homework log (date, pages, done, checked, sticker). Reading the Staff sample, 11 pp: note face (line/space), secret message (DAD FED A BEE), the King's F maze, note ladder, join landmarks, fold-the-staff at middle C (treble C meets bass C, treble G meets bass F), make-your-own flash cards + beat-your-record, compose your first tune, Piano detective week, check-up whose review column points at lesson step + workbook page, chapter badge. Answers moved to a separate **Teacher copy** (`?book=teacher&ch=staff`): answers per page, "Watch for" (common mistakes) and "If stuck, try saying" (Queen/King voice). **Lesson Book:** `bookExtras(id)` per step adds NEW SIGN symbol cards (big symbol, name, Means, Play -- staff, treble/bass clef, grand staff, middle C, alto clef), a coral REMEMBER line, and swaps tools that print empty for paper pictures (`PaperRhymes`, `PaperLandmarks`, `PaperFlash`, `PaperDrawHow`); chip buttons hidden in print. English only for now (Korean book decided last). Book split agreed (see Pending 0d). Verified: compile, overflow check every page, all pages inspected, sweep. |
| 297 | 2026-10-03 | **Books: balanced layout + Note Names + Notes & Rests (Sohyun: "balance the alignment, keep going, make music study fun"; chapter order as proposed).** Layout: every workbook page is a flex column -- the PLAY box grows to fill the rest of the page and centres its content, so pages end level; full grid rows; shared page parts for every chapter (`WbOpener`, `WbLog`, `WbPiano`, `CheckHead`, `CheckTable`, `PaperKeys` paper keyboard, `LetterRow`, `LetterRing`). **Note Names** workbook (8 pp): find C/F by the black keys, name dotted keys, black-key houses colouring, missing letters, music word search, up/down steps, treasure hunt on the keyboard, backwards/skipping chains, draw the 7-letter star (A C E G B D F), piano detective, 20-mark check-up (5 concepts). **Notes & Rests** workbook (9 pp): name + count notes, grow the note tree, draw the matching rest, join note to rest, cut-out note/rest Pairs game, how-many-fit equations, crack the code (sums spell PIANO), dotted notes, note dominoes, is-the-bar-full, finish the bar, compose a rhythm, check-up. Teacher copies for both (answers, watch for, if stuck). Lesson Book extras: Note Names paper pictures (every C and F, alphabet wrap, up/down arrows, letter rings); Notes & Rests NEW SIGN cards (semibreve, minim, crotchet, quaver, semiquaver, crotchet rest, beam, dotted minim, dotted crotchet), REMEMBER line on all 11 steps, paper swaps for the match game, split tree, fill-the-bar and the listening step (QR). Verified: compile, overflow check every page (flex children no longer shrink, so overflow is caught), every page inspected, sweep. |
| 298 | 2026-10-03 | **Books: Time Signatures + Ledger Lines** (workbook, teacher copy, lesson-book extras -- same Together / At home / Play pattern). **Time Signatures** (8 pp): read the two numbers, which time signature fits, be the conductor (trace 2/3/4 patterns), C and ¢, draw the bar lines, body-percussion band in 3/4, the quaver as the beat (6/8), time-signature riddles, simple or compound, beam the quavers, word rhythms in 6/8, check-up. Lesson Book NEW SIGN cards: time signature, common time, cut time, bar line, double bar line, final bar line, 6/8; REMEMBER on all 7 steps. **Ledger Lines** (8 pp): one ledger line, rocket launch (draw notes up the ledger lines to the moon), ledger lines skip a letter (A C E / E C A stacks), two and three ledger lines, ledger-line code (ACE, BAG, EGG), same note on the other staff, write it on the bass staff, twin hunt, write ledger notes, a tune in outer space, check-up. Lesson Book: ledger-line card + REMEMBER lines. Verified: compile, overflow check, every page inspected, sweep. |
| 299 | 2026-10-03 | **Books: Intervals + Key Signatures** (workbook, teacher copy, lesson-book extras). **Intervals** (8 pp): the number on the staff, frog jumps on lily pads (count the letters), count the semitones on a keyboard (major/minor/perfect table), happy or sad (major vs minor 3rd + a tiny story), name it from C, write the top note (major-scale shortcut, with sharps/flats), song detective (Twinkle = P5, Here Comes the Bride = P4, Saints = M3, Jaws = m2, Over the Rainbow = octave -- titles only), inversions, the magic number 9, check-up. Lesson Book: REMEMBER lines; the ear-training step swapped for a QR. **Key Signatures** (7 pp): finish the order of sharps/flats, which sharps or flats, my own silly sentence for F C G D A E B, write the key signature (treble and bass), key-signature Pairs cards, name the key + relative minor, the circle-of-fifths clock, check-up. Lesson Book: NEW SIGN cards (sharp, flat), the two order-builders swapped for a printed "all seven" picture, REMEMBER on all 7 steps. Verified: compile, overflow check, every page inspected, sweep. |
| 300 | 2026-10-03 | **Books: First Steps (+ legato early) + Pulse & Counting.** **First Steps** (9 pp, pre-readers, all on the keyboard): which is higher (star it), sound pictures (high/low x loud/soft), draw the roofs on the black-key houses, colour and count houses, who lives here?, count houses on a full 88-key piano (+ the lonely A♯0), lowest/highest key animals, finger numbers on the big house, Hot Cross Buns in finger numbers (4 3 2...), **legato introduced here** (Sohyun teaches it from the start): "smooth as honey" honey-pot line + play the song legato; echo game, write your own black-key tune, design the cover, check-up (incl. "which line is legato?"). Lesson Book: the first song printed (keyboard + finger numbers), NEW SIGN card for legato on the first-song step, the jam step swapped for a QR, REMEMBER lines. **Pulse & Counting** (8 pp): steady or not (clock, rain, heartbeat...), heartbeat hunt at home, strong and weak beats (big/small circles), pat-and-clap, invent a 4-beat dance move, count it out loud with held counts in brackets and "&" for quavers, fruit-salad rhythms (pear / ap-ple / plu-um / wa-ter-mel-on), clap the cards, make your own rhythm cards, rhythm chain game, check-up. Lesson Book: REMEMBER lines, card builder swapped for a QR. Verified: compile, overflow check, every page inspected, sweep. |
| 301 | 2026-10-03 | **Books: Posture & Hand Shape + Rhythm (Book 1 complete).** **Posture** (7 pp): good sitting yes/no, sitting and arm-weight statements, draw yourself at the piano, which finger (HandPic), hand-shape yes/no, trace your hands and number them, posture checklist + 7-day posture chart, the finger family (name and draw each finger), check-up (incl. left/right hand + finger number). **Rhythm** (8 pp): count the cards (held counts in brackets, "&"), rhythm bingo, harder rhythms (dotted crotchet-quaver "1 (2) &", semiquavers "1 e & a", triplets "1 trip-let" with a printed 3-bracket), animal rhythms (CAT / ti-ger / el-e-phant / hip-po-pot-a), anacrusis with counts and pick-up beats, pick-up words, clap it back, compose a 4-bar rhythm, rhythm comic, check-up. Lesson Book REMEMBER lines; the rhythm composer swapped for a QR. Book 1 (First Steps, Posture, Note Names, Pulse, Note Values, Rhythm, Time Signatures) now has workbook + teacher copy + lesson-book extras for every chapter. Verified: compile, overflow, every page inspected, sweep. |
| 302 | 2026-10-03 | **Books 2-3: nine more chapters (workbook + teacher copy + lesson-book extras).** Steps & Skips (reading-steps), Dynamics & Articulation, Signs, Tempo Race, Musical Terms, Melody & Phrasing, Tones & Semitones, Scales (major + minor), Chords. New paper activities: sequences with a dashed "third group" box and dotted group dividers, finish-the-tune boxes, rope-bridge ties + build-your-own bridge, ornament-spotting tally, heartbeat tempo ruler (Largo 40-60 ... Presto 168-200, as in the app), term charades with blank cards, little-word/big-word bank for "bossy instructions", chromatic caterpillars (up with sharps, down with flats), snowman-chord guide, three-chord songs (end on I / end on V), story-ending cadences incl. plagal. Lesson Book: QR swaps for every sound-only tool (Echo the tune, Hear it find it, Line them up, Tap tempo, Same tune, Changing speed, Metronome, Term match, Build a scale, Scale path) and a paper "best friend" keyboard; Scales Lesson Book now prints the Minor lesson too (new page); REMEMBER lines no longer orphan onto a new page (break-before: avoid). Scales workbook labels the minor page "Minor scales lesson, step 1-2". Verified: compile, overflow 0 on all 27 PDFs, every page inspected, sweep. |
| 303 | 2026-10-03 | **Book 4 start: Musical Form + Styles & Genres (eras, textures) -- workbook, teacher copy, lesson-book extras.** Form (8 pp): name the shape (binary/ternary/rondo block strips, AABB = binary), same-or-new phrase pairs + labelling rows (letters by music, not position), rondo trains with missing carriages, binary-or-ternary phrase rows (AB, AABB, ABA), PLAY: build your own piece (A + B, play AB/ABA/ABACA), Twinkle's secret shape (ABA), body-percussion rondo, form detective table for their own pieces. Styles (8 pp): textures as piano-roll pictures + scenario cards, Be the texture (Row Row Row solo / with a C chord / as a round); style eras page (timeline + era clues from the app's ERAS data + composers; goes with The Piano's Story lesson step 5, new step label "story N"), Time-travel your tune; style families (folk/classical/jazz & blues/popular clues) + straight-vs-swing block rows, Swing your name; 12-bar blues gaps in C, the blues in G (letters), write your own AAB blues verse + improvise on C Eb F G Bb. Lesson Book: paper Form shapes, Textures (the app's TexturePicture), Genre cards, Swing picture; QR swaps for the listening tools. Sohyun confirmed the app's tempo bands for the tempo ruler. Verified: compile, overflow 0 on all 6 PDFs, pages inspected, sweep 0 problems. |
| 304 | 2026-10-04 | **New drills.html chapter: Famous Composers (`composers`, 25th chapter, "about" track, stage 6 after The Piano's Story).** Sohyun: a chapter showing famous composers against the background of their era, plus each composer's own characteristics. 5 Learn steps / Toolbox tools: **Step into each era** (`era-worlds` -- an illustrated scene per era + where music was heard, who paid the composer, the keyboard, what else was new in the world), **Who lived when?** (`composer-time-machine` -- lifespan bars 1660-2020 over era bands, a year slider + "Travel through time" animation, the age each composer turns that year, 7 dated moments e.g. 1685 three births, 1781 Mozart v Clementi), **Meet the composers** (`composer-cards` -- 22 composers: Vivaldi, Bach, Handel, Scarlatti, Haydn, Mozart, Clementi, Beethoven, Schubert, Chopin, R. Schumann, Clara Schumann, Liszt, Brahms, Tchaikovsky, Debussy, Joplin, Bartok, Prokofiev, Gershwin, Kabalevsky, Sculthorpe; each with a literal emblem, famous pieces, musical fingerprint, fun fact, a piece to play, and a sound), **Who am I?** (`who-am-i` -- 4 clues, 4..1 points), **Name that tune** (`name-that-tune` -- spinning record). Drill: 5 levels (Which era? / Who am I? / Name that tune / Who was born first? / mixed); printed worksheets turn listening questions into "Who wrote ...?". Sounds: 12 real openings (Bach Prelude in C, Vivaldi Spring, Hallelujah, Haydn Surprise with the ff chord in bar 16, Eine kleine Nachtmusik, Clementi Op. 36/1, Fur Elise, Ode to Joy, Chopin Op. 9/2, Wild Horseman, Brahms Lullaby, The Entertainer) checked note by note against Mutopia/published editions; other composers get short sketches clearly labelled "made up for this app, not a real piece" (Sculthorpe: none). Facts independently web-checked (12 corrections applied, e.g. Joseph II not "Emperor of Austria" in 1781, Haydn denied the wake-up story, Vivaldi/Bartok/Bach/Liszt claims softened; Beethoven and Debussy shown as era bridges). Era ids/colours reuse ERAS. Verified: compile, EN+KO screenshots of every tool and all 5 drill levels, 43 sounds played without errors, Korean audit 0 English lines, sweep. Note: chapter numbers after The Piano's Story shift by one (Styles is now 25) -- the paused books will pick this up when rebuilt. TOOL_ICON badges added but no current view shows TOOL_ICON. |
| 305 | 2026-10-04 | **Start-here guide + Famous Composers redrawn and widened (Sohyun: friends testing the app didn't know where to start or what to press; the composer pages didn't match the app's look; eras "as detailed as possible -- Impressionism, Nationalism and so on"; the Nutcracker; home-page link only at publishing time).** (1) **"Start here" guide** at the top of the teacher **Plan** tab and the student **Learn** tab (`StartGuide`): how the app works in 3 numbered steps (open a chapter -> do the drill -> press Next), one big button ("Start at the beginning" / "Keep going: X" / "Next on your path: X"), and **the whole path** in 7 stages (Getting started, Reading notes, Rhythm, Reading tunes, Theory, Making music, Know the music) with every chapter as a chip (navy ✓ finished, coral dot started, coral outline = next) and a YOU ARE HERE marker. Collapses to a one-line bar (remembered in `pb_guide_v1`). Path order = `TOOL_CATS` order, the same as the Learn list and the ‹ › chapter arrows. Each `Lesson` now records its step count (`pb_steps_total_v1`) so a chapter counts as finished when every step is ticked. Every chapter page ends with a **"Next on your path"** card (`PathNext`: stage message, button to the next chapter, "See the whole path"). The student "Keep going" card is folded into the guide. (2) **Famous Composers chapter redrawn in the staff look** (navy + coral on white/paper only; the era colours and gold are gone): 46 line-drawing composer emblems, a staff-line scene per period, staff-style chips/tags. (3) **Widened**: 6 periods (Renaissance, Baroque, Classical, Romantic, Modern 1900-1950, Contemporary 1950-today) with "what it sounds like" for each; **11 movements** in a new **Movements** tool/step (`movement-map`: First Viennese School, Nationalism, Late Romanticism, Impressionism, Ragtime/jazz/American, Twelve-tone (Second Viennese School), Neoclassicism, Experimental, Minimalism, Film/TV/game, Australian voices -- each with what, listen for, why it happened, composers, a sound); **24 more composers** (46 total: Palestrina, Byrd, Pachelbel, Couperin, Mendelssohn, Smetana, Mussorgsky, Dvořák, Grieg, Rimsky-Korsakov, Saint-Saëns, Rachmaninoff, Satie, Ravel, Schoenberg, Stravinsky, Copland, Shostakovich, Cage, Reich, Glass, Pärt, John Williams, Hisaishi); time machine 1500-today with living composers and a period filter; **30 real tunes** in Name that tune (new: the Nutcracker's Sugar Plum Fairy, Pachelbel's Canon, Wedding March, Marche militaire, Promenade, Largo, Morning Mood, Mountain King, Bumblebee, Rachmaninoff's Prelude, Gymnopédie, Rondo alla Turca, Beethoven 5, Minute Waltz, Liebestraum, Hungarian Dance 5, Clair de lune); composers still in copyright get original "in the style of" sketches only, labelled as made up; Cage gets a 15-second listening countdown. Drill levels: Which era? / Which movement? / Who am I? / Name that tune / Who was born first? / Everything mixed. All new facts and melodies checked against outside sources by separate agents (corrections applied: Petrucci 1501 = first printed polyphony, Mendelssohn's 1829 Bach revival in Berlin, Byrd/Tallis wording, Rimsky's voyage, Satie not Impressionist, vienna2 dates, etc.). **Not linked from the home page yet -- Sohyun wants to polish first and link it at publishing time.** Verified: compile, EN/KO screenshots of every tool, the guide (new / with progress / collapsed / student) and every drill level, every sound button played, full sweep. |
| 306 | 2026-10-05 | **Books, pass 1 of 4 -- structure (Sohyun: "mostly activities; the practice-check pages go, I'll make those separately; everything connected to what's online; a how-to-use guide").** Four reviewers read all 165 workbook pages + 5 Lesson Book chapters; the full critique is the doc "Piano Butler books: conductor's review" (claude.ai artifact 9a3784be). Decisions Sohyun delegated: keep the check-up (its "go back to" table moves to the Teacher copy); the layered cake for chords; the new metaphors stay; untaught items out of the basics chapters ("bonus" from Rhythm on); start now. This pass, applied centrally to all 22 chapters by `patch306.py` on `book.jsx` (`book.pre306.jsx` = backup; new pieces in `p306/book306.jsx`): (1) the "My homework" log page and the "Piano detective / minutes practised / teacher's note / sticker" page are gone from every chapter; (2) page 2 is now **the chapter's map** (`WbMap`): the four-stop route (Lesson Book step -> Workbook page -> app -> check-up), a step-by-page table with Done boxes, the piano missions (tick once per lesson), the drill's levels with "best __/10" boxes and a QR to the drill; (3) every lesson page's strip (`WbTop`) now has a **QR straight to that lesson step online** (`?drill=X&step=N` scrolls the app to the step -- added in patch305.py) plus "drill level __ best __/10"; the Name line is gone; (4) the opener lost the repeated "How each page works" and points to the map; (5) the student check-up table is Score / Pass mark / Passed, the "go back to Lesson step N, page P" mapping is printed in the Teacher copy's check-up block (`TcBlock goBack`); (6) **front matter** `?book=work&ch=front`: "How this book works" (the route, the three parts, the strip explained with a sample, Learn vs Drill in the app, the whole 7-stage path = the app's Start-here guide on paper) + one homework log for the whole book. Check-up pages moved up one; teacher-copy page refs adjusted. Verified: compile, all 23 workbook routes rendered page by page, 0 overflow (staff p7 1px), teacher copy spot-checked. Next: pass 2 (the 18 verified errors + draw-on staff sizes), pass 3 (draw the metaphors, 10 PLAY replacements), pass 4 (Lesson Book print curation). |
| 307 | 2026-10-05 | **Books, pass 2 of 4 -- the verified errors.** Three fixers worked in isolated copies of the build (`mk_sandbox.sh`), each confirming every reported problem at zoom before touching it (two reports were misreads: ledger-lines p5 and the chords B-D-F item were correct) and re-rendering after; diffs merged into `book.jsx` (`book.pre307.jsx` = backup). Shared rhythm renderer (`BeatRow`/`RestShape` reassigned for the book): notes sit at the start of their beat span, quaver pairs and semiquaver groups are **beamed**, triplets beamed with a 3, minim/semibreve rests drawn on a visible line, over-full bars spill past a bar line in coral. Per chapter: posture (test hands without finger numbers or L/R labels, upright thumb "1", hand-trace boxes 117 mm, "collapses" reworded); first steps (check-up legato item rewritten to taught words, two-row 88-key keyboard, "right-hand one (the highest)"); note names ("4 steps up" with a worked hop, numbered boxes); staff (middle-C hunt corrected: every C on its own ledger line, half on each staff; named items kept inside the five lines; fold page photocopy note; secret-message staves 3 per row); ledger lines (headings honest about the beside-the-staff spaces, 1st/2nd/3rd labels beside their notes); steps & skips (the shape puzzle now draws a real mountain/valley/stairs/roller-coaster; arrow boxes; bigger staves); tones (accidentals tested across a bar line, four different check-up signs, bigger key dots, "either name is right"); pulse (unambiguous steady/not items, dotted minim and semiquavers removed, quaver rule in TOGETHER, pear/ap-ple/pluuum); note values (semiquavers and dotted quavers removed, rest sentence corrected, dominoes shuffled, one clear draw task); time signatures (one wording: six quaver counts, two beats you feel; "use 4 on the bottom"; beam-the-quavers item prints bare stems); rhythm (semiquavers/triplets as BONUS, hip-po-pot-a, clap-back boxes, short last bar note); tempo (six words = six animals, ruler ranges touch, "very slow and wide", big metronome crotchet); form (rondo lettering follows the next-letter rule everywhere, clipped item fixed, pairs 3 per row); intervals (letters under the keys, "letters first, then semitones", pads on a keyboard strip, step 5 strip); scales (Broken staircase replaces the star-chart log, staircase template, step 7 shown app-only); key signatures (bass-clef rule corrected with a D major picture, relative minor = 3 semitones with keys, F major exception, bigger pairs cards); terms (mosso, SHORT FORMS box, rall. in the check-up, A tempo answer line, photocopy note); melody (numbering, 4+1 marks, 3 per row); dynamics (fermata defined, pedal answer line, concept steps match the app); signs (To Coda rule, two new 8va questions); styles ("in this simple blues", texture legend, Debussy/Bartók). All draw-on staves at 3 per row except the ledger-lines and dynamics check-ups (page capacity). Verified: compile, all 23 workbook routes re-rendered, 0 overflow, teacher copies rendered, merged pages spot-checked. Next: pass 3 (draw the metaphors + 10 PLAY replacements), pass 4 (Lesson Book curation). |
| 308 | 2026-10-05 | **Books, pass 3 chunk 1 of 4 -- the metaphors drawn into the first six chapters** (Sohyun: visual beats reading; everyday, metaphorical, fun; her own metaphors first). `WbOpener` gained a `hero` prop; new two-colour (navy/coral) SVG components live in book.jsx. Posture & Hand Shape: the 12 yes/no sentences are now 12 drawings of a kid at the piano to tick or cross (front of chair, sofa lean, feet flat, shoulders up, elbows, puppet string to a cloud, squashed elbows, swinging feet, whole arm, squeezing, heavy arm, locked wrist); hand shapes as pictures (ball, flat, tip, bending tip, thumb as a tipped boat, stiff wrist); PLAY = spot the 5 differences; check-up in pictures. Black Keys & First Song: bear at the low end, bird at the high end on every keyboard; little/big houses; the lone bottom black key under a kennel; overlapping footprints (legato) vs hopping raindrops (staccato); PLAY "Bear or bird?". Note Names: the two houses with front doors on C and F replace "C sits just left of the 2 black keys"; the A-G Ferris wheel for "after G, back at A"; a 3-step staircase for up/down; PLAY "Lost letters". Reading the Staff: opener = Sydney Harbour map (north shore = the Queen's treble staff, south shore = the King's bass staff, middle C = the Harbour Bridge to the CBD); kebab (line note) vs sandwich (space note); Queen on her G line and King with two guards on F on the clef pages and in the maze; PLAY "Beat your record" log replaced by seeded Note bingo. Ledger Lines: ladder with clipped-on rungs + the rocket; stepping stones for "skip a letter"; the bridge picture for "same place, two addresses". Tones & Semitones: two keys holding hands (best friend) and the go-between trio (friend of a friend), the houses with "no fence" at E-F and B-C, up/down/eraser icons for sharp/flat/natural, a "Hi, I'm C#, also known as Db" name badge, a 12-step chromatic staircase. Verified: compile, all 23 routes 0 overflow, teacher copies fit, pages inspected. Next chunks: Rhythm group (pulse, note values, time signatures, rhythm, steps & skips, tempo), Theory, Making music + Know the music; then pass 4 (Lesson Book). |
| 309 | 2026-10-05 | **Books, pass 3 chunk 2 -- metaphors drawn into the Rhythm group and Reading tunes.** Pulse & Counting: heart/ECG hero (hearts only ever mean the beat), the 12 steady/not-steady items as drawn icons to circle, BIG-step/little-step footprints for strong and weak beats, a "still singing" sound tail for 1 (2) and two kids sharing one seat for a quaver pair, pizza slices by the fruit words, the Rhythm-chain log replaced by a 12-square board game. Notes & Rests: the cake hero (one cake, then cut in 2, 4, 8, an empty plate with the rest beside each), "Cut the cake" PLAY, minim rest = a hat on line 3 and semibreve rest = a bat hanging from line 4, the dot = a scoop and a half, "Roll a bar" dice game. Time Signatures: the lunch box (top number = how many pieces, bottom = what size piece), train carriages for bar lines, bananas in bunches of 2 vs 3, marching LEFT-right vs skipping STRAW-ber-ry. Rhythm Patterns: cards riding on a heartbeat line, one beat box cut 2/3/4 ways with CAT/ti-ger/el-e-phant/hip-po-pot-a, the runner's run-up for the pick-up bar, a balloon for held beats, "Pick-up song hunt" (answers in the teacher copy). Steps & Skips: staircase beside the staff with middle C on its own CBD platform, the hand on C-G, odd-one-out and finger-code puzzles, 8 note slots + a dice composer. Tempo Race: the six animals racing past a speed-limit sign, animal icons to match, the car with accelerator/brake/back-to-the-sign, heartbeat rulers for you and a parent or pet. Verified: compile, all 23 routes 0 overflow, teacher copies fit. |
| 310 | 2026-10-06 | **Books, pass 3 chunk 3 -- metaphors drawn into the Theory chapters.** Intervals: opener = a tape measure laid across the keyboard (count the letters for the number, the best-friend steps for the quality), a frog that counts the key it sits on as 1, a ruler of semitones with the interval names hanging off it, happy/sad faces on C-E vs C-E♭, a see-saw for inversions (3 + 6 = 9), and PLAY "Inversion dominoes" replacing the magic-9 joining (the chain was brute-force checked: it has solutions and the teacher answer is valid). Scales: opener = a staircase standing on a keyboard (BIG step = tone = skip a key, tiny step = semitone = the very next key, T T S T T T S); harmonic minor drawn as the same staircase with one giant 3-semitone step (the "creaky stair"). Key Signatures: opener = a line-up of kids (F C G D A E B for sharps, the same line turned round for flats; D major = the first two kids step forward) and a house-rules sign on the door for "write it once, it covers the whole piece". Chords: opener = a 3-layer cake = a snowman (the app's name for it) = a stack on the staff; "slide the cake's middle layer down one key" tied to the Intervals happy/sad faces; home / garden / gate (I / IV / V) fills the empty slots on the Roman-numeral page; inversions = the same cake with its layers shuffled; PLAY "Punctuation detective" (perfect = full stop, plagal = Amen, imperfect = comma, interrupted = surprise) replaces "Story endings", answers in the teacher copy. Page fixes: Intervals pages 3-5 and Chords page 6 re-fitted. Verified: compile, the four chapters and their teacher copies 0 overflow, pages inspected at zoom. Remaining pass 3: chunk 4 = melody, dynamics, signs, terms, form, styles; then pass 4 (Lesson Book). |
| 311 | 2026-10-06 | **Books, pass 3 chunk 4a -- metaphors drawn into Melody, Dynamics and Signs.** Melody & Phrasing: opener = four shape pictures (rising = stairs, falling = a slide, arch = the Harbour Bridge, valley = a hammock) that the note-head lines are matched to; question/answer phrases drawn as two speech bubbles (a question hangs in the air, an answer lands back home on C); sequences drawn as the same footprints one stair higher each time. Dynamics & Articulation: opener = a six-step volume ladder with everyday voices (a whisper, library voice, dinner-table chat, classroom talk, playground shout, thunder!) plus an articulation strip (staccato = bounce, legato = glide, accent = poke, tenuto = lean); hairpins drawn as megaphones that open up or close down. Signs: opener = road signs (repeat = roundabout, D.C./D.S. = U-turn, To Coda = exit ramp, Fine = chequered flag) and the tie as a rope vs the slur as a rainbow; 8va/8vb boxes get lift icons; the ornament page's tally cards are replaced by ornament cards (glyph, picture, "sounds like ..." and four circles to fill in). Page fixes: Melody pages 3-5 and Signs page 4 re-fitted after the new leads; slur caption on the Signs opener no longer clips. Verified: compile 0 errors, the three workbooks and their teacher copies 0 overflow, pages inspected at zoom. Remaining pass 3: chunk 4b = terms, form, styles; then pass 4 (Lesson Book print curation). |
| 312 | 2026-10-06 | **Teacher home split into separate tabs; Lesson plan removed (Sohyun: the guide, the all-chapters/Toolbox list and the Lesson plan were all crammed on one page; the bottom Lesson plan is not needed).** Teacher tabs are now Guide | Chapters | Toolbox | Practice | Students (student tabs unchanged: Learn | Practice). Guide = the "Start here" guide on its own page, always expanded (no hide button; students keep the collapsible version on Learn). Chapters = the existing All chapters page, now a tab. Toolbox = student switcher + search + categories, with its own title and one-line intro. The Lesson plan block (today's mix, strand tracker, exam ladder, anytime chapters) was removed from the UI, and the places that pointed to it were re-pointed: Students page (text, "Toolbox" button instead of "Lesson plan", step-progress bar replaced by a "n in kit" line, "STARTS AS" chips removed from the form), kit/tool back buttons, deep link ?view=toolbox. Chapters opened from a tab return to that tab. Kit data (kits/who) is untouched; old per-student step ticks stay in localStorage unused. The old code is in git history (Phase 311 and earlier) if the plan is ever wanted back. Also decided: Korean is for the online translation only -- no Korean printed books for now. Source: patch312.py (applied after patch305.py). Verified: compile 0 errors, tab and back-button flows in a real browser (guide, chapters, toolbox, tool, kit, students), Korean labels, student view unchanged, 360px and 420px widths. |
| 313 | 2026-10-06 | **Books, pass 3 chunk 4b -- metaphors drawn into Musical Terms, Musical Form and Styles (pass 3 now complete for every chapter).** Musical Terms: opener = four everyday dials for the four families (speed = speedometer "How fast?", changing speed = brake and accelerator pedals "Faster or slower?", volume = volume knob "How loud?", other = a luggage tag "What mood or touch?"), with the line that Italian is music's language like pizza and espresso; the same icons sit in the four family boxes on the Four families page; Little words page gets three dials (poco allegro / allegro / molto allegro) so "little words turn the dial". Musical Form: one metaphor for every form = a train (opener: binary, ternary and rondo as three trains on rails, blurb now "a piece is a train, each section is a carriage"); the Form detective review table is replaced by three train-depot rows (write the piece, colour one carriage per section, name the form). Styles & Genres: the tick-list PLAY is replaced by a Time-travel passport (a card per era with a sound-shape picture -- terraced dots, neat arches, a flowing wave, mist plus spikes -- a stamp circle and a star); swing page gets a walking vs skipping lead (straight = walking, swing = skipping); small spacing trims so the page still fits. Source: patch313.py + p313/art313.jsx. Verified: compile 0 errors, the three workbooks and their teacher copies 0 overflow, pages inspected at zoom, online app and tab flows unchanged. Remaining: pass 4 (Lesson Book print curation), the quaver-on-& tweak in BeatRow, a sw.js full-site sweep after Phases 306-313. |
| 314 | 2026-10-06 | **Books, pass 4 chunk 1 -- Lesson Book print curation begins.** A `LessonFix` wrapper (Lesson Book only) rewrites screen-only wording on the printed page: about 60 rules turn "tap / press / hear" sentences into paper wording (clap, count, look, circle), hide counters (0/6 done, 0/17 ✓, 0/0, Score) and the "Space bar" line, and keep the clef-story heading with its card; short steps (<= 500 px) are kept on one page, long ones flow. Paper versions replace empty tool states: Pulse (Beat or rhythm? with the Hot Cross Buns picture, Clap the right beat with coral-ring rows), Form steps 2-5 (build-your-own boxes, same-or-new pairs and letter row, rondo trains, two-or-three phrases, one worked example each, QR kept as a small extra). Staff: the blank "The staff" card is gone, "the theory papers" now says AMEB theory papers, and the alto clef step is a footnote ("Beyond the piano"). Pulse also gains the shapes of crotchet/minim/dotted minim/semibreve and a plain explanation of "72 beats a minute"; Form notes that A A B B is still binary. `Step` in the book build supports `foot`; `SymbolCards` use 4 columns when there are 4 cards. The online app is unchanged. Source: `book.jsx` (patch314.py + p314/lessonfix314.jsx; book.pre314.jsx = backup). Still to do in pass 4: time-signatures, rhythm, reading-steps, tempo, intervals, scales, key-signatures, chords, tones, melody, dynamics, signs, terms, styles, piano-story, pitch-range, composers (tool states, untaught items, the "Grade 3" step title). |
| 315 | 2026-10-06 | **Books, pass 4 chunk 2 -- Lesson Book paper versions for Tempo, Key signatures, The piano's story and Famous composers.** Tempo: "Tap your own tempo" becomes "Find your own tempo" (clap for 15 seconds, count, x 4, with a fill-in line; QR kept as an extra) and the stray "dot pulses" line is hidden. Key signatures: "All 15 keys" is a printed table of every major key with its number of sharps or flats and its relative minor (the "Tap one" label and the "show the answer" wording are gone). Piano's story: the three keyboards are a side-by-side card set (clavichord, harpsichord, piano, with the mechanism drawings), the style eras are four printed era cards, and the "Press / Tap a date" lines are reworded; each step gets a Remember line. Composers: the time-machine wording is reworded and the Who am I? / Name that tune games become QR exercises (the chapter is still not linked from index.html; the printed version shows only the first era and first composer card, a known limit). Source: `book.jsx` (p315/paper315.jsx applied in place; book.pre315.jsx = backup). The online app is unchanged. Still to do in pass 4: intervals, terms, note-names, time-signatures, scales, tones, melody, chords, dynamics, signs, styles, pitch-range, reading-steps, rhythm (tool states, untaught items). |
| 316 | 2026-10-06 | **Books, pass 4 chunk 3 -- Lesson Book paper versions for Intervals, Musical terms and Note names.** Terms: "Four families" and "Little words" become printed tables, the ♪ say-it buttons are hidden, and a "Two traps" box (rit. = ritardando or ritenuto; mosso = "moved") closes the Grade 2 list. Intervals: the semitone-and-tone Rule (best friend / friend of a friend) is added to step 2, the "Grade 3" heading is now "Turn it upside down", and the screen-only inversion and tritone tools get compact paper versions (two staves side by side, no animated widgets), which removes the page that held a lone Remember line. Note names: black-key sharp/flat labels are hidden with an explanatory note, and an octave note is added. `build296.py` now supports `{x.add}` after the step children. Checks: build 0 errors; workbooks for the three chapters 0 overflow; `chk314.js` shows the online app unchanged. Known and accepted: Terms Grade 2 list splits across pages 3-4. Not pushed. | `drills.html`, `CLAUDE.md` |
| 317 | 2026-10-06 | **Interval ruler shows the line/space pattern for every interval; Scales has one fingering tool instead of two.** Intervals: under the ruler staff a new strip lists 2nd to 8ve above the chosen bottom note, each with a tiny line-or-space picture of the bottom and top note and the word stay (odd: line to line, space to space) or swap (even: line to space); tapping a cell moves the top note there. Scales (major lesson): the "Practise the fingering" step is removed because it duplicated the Scale finder; the finder is now the last step (6 of 6), still follows the key picked in the pattern and scale-path steps, and carries the AMEB-books fingering note. Black-key and enharmonic scales (F♯/G♭, C♯/D♭, B/C♭ major; G♯/A♭, D♯/E♭, B♭/A♯ harmonic minor) show BOTH key signatures and both note spellings; when the other spelling exists only on paper (B♭, E♭, A♭ major; F♯, C♯ minor) a short note explains why (double sharps/flats). One chip per pair in the finder. The Toolbox card "Major scale fingering" no longer repeats the drill; the unused `ScaleFingeringDrill` is deleted. Build: new `patch317.py` in the chain after `patch312.py`. Lesson Book/workbook: scales WbMap now 6 steps, last Remember line merged. Checks: 0 build errors, live browser pass EN+KO, workbooks 0 overflow, online app unchanged elsewhere. Not pushed. | `drills.html`, `CLAUDE.md` |
| 318 | 2026-10-06 | **No exam board is named anywhere a student or teacher can read it (Sohyun's rule: keep the drills general; "comparable for ..." exam notes can be added later).** Removed every visible AMEB mention from `drills.html` (EN + KO): the fingering captions in the Scale finder and the harmonic-minor viewer, the Terms lesson intro ("meanings the AMEB accepts"), the Term cards and Theory category blurbs, and three Lesson Book / workbook / teacher-copy notes. Term cards no longer show the "Theory of Music / Musicianship" paper switch (the full Theory list stays; the Musicianship list data is kept in the code for later). Grade/Preliminary level labels were left as they are (flagged to Sohyun). Code comments that record where the data came from are unchanged. New `patch318.py` in the build chain after `patch317.py`. Checks: 0 build errors, 0 non-comment AMEB lines, live pass EN + KO, workbooks 0 overflow. Not pushed. | `drills.html`, `CLAUDE.md` |
| 319 | 2026-10-06 | **Books, pass 4 chunk 4a -- Lesson Book paper versions for Time signatures, Scales and Tones.** Time signatures: the screen-only "hear" labels and the "0 of 2 bar lines" counter are hidden. Tones: "How long does an accidental last?" is now a printed, numbered example (a sharp then a natural, and a G major key signature) instead of an unlit keyboard; "pick any two keys" becomes "count the semitones from C to E"; the empty "Start on" label is hidden and the "names of one key" line is rewritten for paper. Scales: the Scale finder step prints as a QR plus a "Same keys, two names" page (F♯/G♭, C♯/D♭, B/C♭ major and G♯/A♭, D♯/E♭, A♯/B♭ minor, each with both key signatures); "See every form" becomes a QR card. The Scales Lesson Book drops from 11 to 8 pages. `paperFix` now lets a step marked `data-flow` break across pages. Checks: build 0 errors; workbooks and teacher copies 0 overflow; `chk314.js` shows the online app unchanged. Not pushed. | `drills.html`, `CLAUDE.md` |
| 320 | 2026-10-06 | **Pass 4 chunk 4b: Melody + Chords paper versions + Valley preset fix.** Lesson Book only; the online tools are unchanged except one bug fix. Melody (4 → 3 pages): *Draw a tune* prints the five tune shapes (rising, falling, arch, valley, wave) as dotted-contour cards with the ending note in coral and a QR to the real tool; *Phrase marks* prints solid brass arcs with the breath comma; *Question or answer* prints all six endings (4 questions, 2 answers) with note names and a QR; *Sequences* prints all three repetitions with brackets and coral starting notes. Chords (6 pages, unchanged): *Stack a triad* prints the cake and the staff growing root → 3rd → 5th, the C-E-G keyboard and line/space examples (E-G-B, F-A-C); *Inversions* prints all three positions with staff and keyboard in rows. The Cadences step now stays together on one page (new `keep` flag on a step: `data-keep` section attribute). App fix: the *Valley* preset in Draw a tune was classed as a wave by its own shape rule (rose past the low note then dipped); it is now a true valley (`33 31 29 28 29 31 32 34`), EN+KO verified live. Workbook/teacher copies 0 overflow; chk314 ok. Build chain gains `patch320b.py` (after patch318); `patch320.py` edits `book.jsx` once from `book.pre320.jsx`. |
| 321 | 2026-10-06 | **Pass 4 chunk 4c-1: Dynamics + Signs paper versions.** Lesson Book only; online app unchanged. Dynamics (4 pages): *Hairpins* prints four worked examples (p<f, f>p, pp<mf, ff>mp) with the crescendo/diminuendo wording; *The sustain pedal* prints all three ways (no pedal, held, changed with each chord) as chord timelines with the Ped. line; *Articulation* no longer repeats Staccato and Accent (the two big cards) in the list below, which now lists Legato, Tenuto, Staccatissimo and Fermata; Tie-or-slur becomes a QR game and the Articulation step is kept together on one page. Signs (5 pages): *Follow the road map* prints all six maps (repeat, repeat part, 1st/2nd time, D.C. al Fine, D.S. al Fine, D.C. al Coda) with the play order under each; *8va and 8vb* prints both (it showed only 8va); *Ornaments* prints all six (trill, upper and lower mordent, turn, acciaccatura, appoggiatura) as written/played pairs; Tie-or-slur becomes a QR game (the Tie and Slur cards above already show both). Workbook/teacher copies 0 overflow; chk314 ok; QR targets `tool=tie-slur` etc. open. Sources `p321/paper321.jsx` + `patch321.py` (edits `book.jsx` once from `book.pre321.jsx`, not in the chain). |
| 322 | 2026-10-06 | **Pass 4 chunk 4c-2: Pitch, Hz and range paper version.** Lesson Book only; online app unchanged. Chapter 24 now prints in 4 pages (it was 6). *How high is a note?* prints three waves (A3 220, A4 440, A5 880 Hz) over the same slice of time so the doubling can be counted; *Shorter, tighter, higher* prints the string lab as five stacked states (whole, 3/4, half, loose, tight) with the vibrating part marked and the note and Hz beside each; *Big is low, small is high* prints the xylophone plus the whole violin family in size order with each lowest open string (the online one is a two-instrument guessing game); *The octave ladder* prints all five A's to scale with a x2 label on each; *Who plays where?* is one compact chart (keyboards, strings, woodwind, brass, voices, piano history) kept together on one page. Built from p322/paper322.jsx via patch322.py (not in the build chain). Workbook and teacher copy have no pages for this chapter (same as before). Build 0 errors, chk314 ok. |
| 323 | 2026-10-06 | **Pass 4 chunk 4c-3: Reading steps + Rhythm paper versions (closes pass 4 chunk 4c).** Lesson Book only; online app unchanged. Reading steps (5 pages): *Step, skip or same?* prints all five moves (same, step up, step down, skip up, skip down) as a two-note staff plus a key strip and a how-to-tell card, replacing the single giant keyboard; *Read a tiny tune* prints all four tunes (Walking up, Step and repeat, Skipping, Ode to Joy) with fingers and counts and a thumb-on-C hand strip, with no blank keyboard; *Complete the melody* prints the three endings (C home, E not yet, A a leap) with the verdict beside each; steps 2, 5 and 6 are kept together on one page. Rhythm (3 pages, was 4): *The 40 cards* prints all of Set 1 in two columns plus two sample cards from each of Sets 2-5 and a note that all 40 are in the app; *Count harder rhythms* prints all seven bars (dotted, two dotted pairs, semiquavers, quaver + 2 semiquavers, dotted quaver + semiquaver, triplets, syncopation) with their counts, flowing across the page break. Built from p323/paper323.jsx via patch323.py (not in the build chain). Workbook and teacher copy 0 overflow, chk314 ok, build 0 errors. |
| 324 | 2026-10-06 | **Scale finder: the paper-only twin's key signature is drawn too; clipped signatures fixed.** Sohyun's request (A♭ · G♯ showed only the flats): every black-key scale now shows both signatures. A♭ · G♯, B♭ · A♯ and E♭ · D♯ major, and the F♯ and C♯ harmonic minors, get a second dashed card marked "only on paper" with the real signature (G♯ major 8♯, A♯ major 10♯, D♯ major 9♯, G♭ minor 9♭, D♭ minor 8♭) drawn with double sharps (x) or double flats, plus that scale's note names (F♯♯ ...), and the explanation now says how many sharps/flats it needs and which are doubled (EN + KO). New helpers `theoryKey()` / `fmtTheory()` spell any key on paper; `KSStaff` now accepts a count of 8-10 (first count-7 signs double, via `DoubleSharpShape` and a paired flat). Also fixed: the 7-accidental twin cards (C♯ / D♭, B / C♭) were clipped at the card edge, online and in the Lesson Book (the old paper cards drew every signature at width 92, so anything past three accidentals was cut off). Lesson Book Scales step 6 now draws all 11 pairs (6 twin cards + the 5 paper-only keys), still 8 pages; pitch-range range chart edge widened by 3 units. Online change is a build-chain patch (patch324.py, edits drills.pre296.html, in the chain after patch320b.py); the book change is patch324c.py (from book.pre324.jsx, not in the chain). New check script clipchk.js flags any SVG whose drawn content leaves its own viewBox. Build 0 errors, chk314 ok, workbook/teacher 0 overflow. |
| 325 | 2026-10-06 | **Toolbox gets a Books shelf.** Sohyun asked where to find the books and wanted them viewable on their own in the Toolbox. The printed books used to exist only behind hidden `?book=` web addresses. The teacher Toolbox now has two tabs, Activities | Books. Books lists all 25 chapters in path order (the seven Lesson Book stages) with a Lesson Book, Workbook and Teacher copy button each (a dashed grey pill where a chapter has none yet: The Piano's Story, Famous Composers, Pitch/Hz/Range have the Lesson Book only), plus whole-set buttons (all Lesson Books, Workbook front pages, all Workbooks, all Teacher copies). Each opens in a new tab on the paper layout, which has its own Print / Save as PDF button; links always ask for `lang=en` (books are English only, the shelf itself is EN/KO; `?view=toolbox&books=1&sec=books` opens it directly). **Public (Sohyun OK, 2026-10-06):** `BOOKS_PUBLIC = true`, so the Books tab shows for every visitor of `drills.html` (the Toolbox is in the teacher view, which is the default). Nothing on the main site links to `drills.html` books yet and Famous Composers stays unlinked from `index.html`; the `?book=` pages are still reachable only through drills.html. To hide the tab again set `BOOKS_PUBLIC = false` in `patch325.py` (then it shows only on a device that opened `?books=1`, or on a copy opened from the Mac). Source: `patch325.py` (in the build chain after patch324). Verified: Babel/script check 0 errors, EN + KO + 430 px + 960 px screenshots, all 73 links present, four links clicked and opened (Lesson Book, Workbook, Teacher copy, front pages), full EN+KO sweep earlier the same day (157 tools, 25 chapters, 0 problems) covers the rest. |
| 326 | 2026-10-06 | **Housekeeping.** `.gitignore` now keeps the reference book PDF (*Help Your Kids with Music*) and `_pb_refextract/` (the text extracted from it) out of git for good. The four shelved posture prototypes (movement-lab, piano-body-atlas, piano-posture-detail, pasted-kinematic-viewer) were deleted by Sohyun. Build sources for the books and app (patch scripts, `book.jsx`, notes) saved as `_workspace/book-build-2026-10-06.tar.gz` (untracked, they otherwise live only in the temporary cloud workspace). Cleaned by Claude with Sohyun's OK (2026-10-06, folder 1022 MB -> 817 MB): deleted `sightreading-generator/_to_delete/` (205 MB of regenerable sight-reading output, one test record, an old sample; nothing referenced it), the empty stray file `main`, and 10 leftover git `tmp_` garbage files. Still open for Sohyun: run `git gc` in her own Terminal (the .git folder is 377 MB because ~10,000 objects are stored loose), and decide about old brand mockups in `Claude outputs/` (kept). Rule learned: never amend a commit that `origin/main` already has (Phase 325 was amended after Sohyun had pushed it and had to be rebuilt as 325b). |
| 327 | 2026-10-06 | **Faster loading, Cut-outs, posture tracing page, clipping fixes.** (1) *Faster loading:* `drills.html` is now precompiled (see the section "drills.html: source and compiled page"): first screen in about 0.4-0.7 s instead of about 6 s on the same machine; `drills.src.html` is the editable source and `tools/precompile.js` builds the served page. The full tool/chapter sweep (157 tools, 25 chapters, English and Korean) passes with 0 problems on the compiled page; the page compiled with this repo's own `@babel/core` was also smoke-tested and behaves the same. (2) *Cut-outs* (new, printable manipulatives, English only, A4): open from Toolbox > Books > Cut-outs or `?book=cutouts&ch=<set>|all&lang=en`. Six sets, 16 pages: **Note-value bars** `note-bars` (2 pages: strips at true scale, 1 beat = 44 mm, so a 4/4 bar is 176 mm; semibreve to semiquaver, the rests, dotted pieces drawn as note + half, a 4/4 bar mat, Try-this boxes); **Scale slider** `scale-slider` (2 pages: a two-octave keyboard strip where every key is 7 mm wide, so 1 key = 1 semitone and 2 keys = 1 tone; sliders for major, natural/harmonic/melodic minor, five-finger major/minor, major/minor/diminished/augmented triads, an interval ruler, and two blank sliders for the student's own pattern); **Staff mat and tokens** `staff-mat` (2 pages: grand staff plus a 3-bar treble staff with 9.5 mm line spacing, Queen/King captions; round 9 mm tokens: 36 note heads, A-G letters x4, sharps/flats/naturals, ledger-line strips); **Note flashcards** `cards-notes` (4 pages: treble middle C to G5 and bass E2 to B3, 12 cards each; staff on the front, letter + mini keyboard on the back), **Rhythm flashcards** `cards-rhythm` (2 pages, 12 notes/rests/dotted), **Term flashcards** `cards-terms` (4 pages, 24 terms read from the app's own `TERMS` data: speed, changing speed, volume, legato/staccato). Flashcards are double-sided: print the FRONTS page, then print the BACKS page on the other side, flip on the long edge (the back page lists each row right-to-left so every back lands behind its front; each card has a small number on both sides). Code: `cutouts.jsx` spliced into `book.jsx` by `patch327.py`; registry `CUTOUTS` / `CUTOUT_LIST`. Terms cards name no exam board. Still to build (not asked for yet): circle-of-fifths wheel, chord cake / flip cards, practice dice and tracker, Tempo Race board, era cards (hold until publishing). Still to do: a pilot print test with 3-5 students (needs a printer). (3) *Posture & Hand Shape workbook:* "Trace your hands" now has a page of its own with two boxes about 180 mm tall (a real hand needs about 150 mm); the workbook is 7 pages, the teacher copy 2 pages, the check-up is page 7. The ledger-line and dynamics check-ups were deliberately left at 4 per row (3 per row split the groups of four into 3 + 1 and overflowed the page). (4) *Print-set proof:* every Lesson Book chapter (25, 126 pages), Workbook (22, 149 pages) and Teacher copy (22, 44 pages) rendered to PDF with no errors and no page overflow. The SVG clipping check found four drawings cut off at the right edge, fixed: the third carriage of the Time Signatures train, the last hopping foot in First Steps, "A-CHOO!" in Pulse, the "1" in the Note Values ice-cream label. |
| 328 | 2026-10-07 | **Cut-outs: four more sets (10 sets, 26 pages).** Open from Toolbox > Books > Cut-outs or `?book=cutouts&ch=<set>|all&lang=en`. **Circle-of-fifths wheel** `fifths-wheel` (2 pages: a 150 mm wheel with major keys on the outer ring, relative minors in the middle and the number of sharps or flats inside, all read from the app's own `CIRCLE` and `KEY_SIGS` tables; plus a turning disc with a 3-key mouth to fasten over the wheel with a paper fastener, and order-of-sharps / order-of-flats tiles); **Chord cake** `chord-cake` (2 pages: the seven white-key triads as loose root / 3rd / 5th layers in the app's chord-layer colours plus a blank cake to write on; then layers as thick as the gap they stand for, 4 keys = major 3rd and 3 keys = minor 3rd, with a vertical keyboard ruler at 7 mm per key and the four triad recipes); **Practice dice and week tracker** `practice-dice` (3 pages: two cut-and-fold dice with glue tabs, "play it" = Queen's hand / King's hand / hands together / Adagio / forte / piano and "before you play" = clap the rhythm / say the note names / count out loud / tap the pulse / find the key signature / sit tall, feet flat; a Mon-Sun tracker with star stickers); **Tempo Race board game** `tempo-race` (3 pages: a 30-square snake board with accelerando and rallentando squares; 16 speed cards from the app's seven `TEMPO_TERMS`, move 1 for Adagio up to 7 for Presto, plus two blank; four cars; rules and an answer key). English only, no exam board named. Verified: overflow check 0 for every set and for the 26-page combined PDF, clip check clean, sweep of 157 tools and 25 chapters with 0 problems, compiled page first screen about 0.4 s. Committed locally, not pushed. |
| 329 | 2026-10-07 | **Teacher login restored (Phase 0 of student links + progress tracking).** `login.html` and `auth.js` had been deleted in the Phase 54 cleanup (commit `1bccbd5`) while `teacher-dashboard.html` still loads `auth.js` and calls `requireAuth()`, so by file evidence the dashboard could not start. Both files recovered from `1bccbd5^`. Changes to the old `login.html`: success and already-signed-in redirects now go to `teacher-dashboard.html` (the old target `home.html` no longer exists); title and button say teacher sign-in; `noindex, nofollow` added; new "Email me a sign-in link instead" button (Magic Link, `shouldCreateUser:false` so a stranger cannot create an account from this page). The original email + password sign-in is unchanged and is what the teacher account used before. `auth.js` is the original (Supabase client + `requireAuth()` + `signOut()`; only the public anon key). **Verified in a real headless Chromium against a local copy with the Supabase auth and REST calls stubbed** (no live Supabase from the sandbox): dashboard with no session redirects to `login.html`; empty-email and refused-address errors show; link-sent message shows; password sign-in lands on the dashboard and mounts the React root; Sign out returns to `login.html`; inline scripts pass `node --check`. Live check 2026-10-07: Sohyun signed in through the emailed sign-in link on the pushed site and the dashboard opened (she does not remember the old password; the account has no way to set one yet, and she chose to stay with sign-in links only). Design for the rest (student links, progress sync, Passport, This week): `_workspace/student-login-sync-design-v2-simple.md`. `drills.html` and `drills.src.html` untouched. |
| 330 | 2026-10-07 | **Student links, step A1: SQL for `student_links` (not yet run).** Decided with Sohyun 2026-10-07: simple first, no chapter lock, students see all chapters, a personal secret link per student (no username/password), progress saved per student so it follows them across devices, teacher sees progress in the dashboard later; sign-in stays Magic Link only. New file `migrations/2026-10-07_phaseA1_student-links.sql`: table `student_links` (student_id, teacher_id, display_name, token, active, created_at, revoked_at; one link per student; token at least 32 characters), RLS so a teacher can only create/read/update/delete links for her own students, and `pb_student_info(token)`, a security-definer function that returns only `{name}` for an active link and null otherwise. Anonymous users cannot read the table. The `id` type of `students` is detected (uuid or bigint) because it is not documented. Tested in an in-memory Postgres (PGlite) with simulated roles and RLS: 44 checks passed for both id types (cross-teacher isolation, forged teacher_id, short/wrong/paused/regenerated tokens, cascade delete, idempotent re-run); the test script is `_workspace/sql-tests/phaseA1-sqltest.mjs`. NOT tested against the real Supabase project: Sohyun runs the file once in the Supabase SQL editor. Next: A2 dashboard "Create student link" (copy, pause, regenerate), A3 drills opens a student link. `drills.html` untouched. |
| 331 | 2026-10-07 | **Teacher login and dashboard restyled to match the drills.** Sohyun asked for the same look as the drills before building student links. `login.html` rewritten: the drills' cream page (`#faf6ec`), cream card with a navy hairline border, the bowtie mark (navy strokes, coral knot, same as the drills favicon), Playfair Display title, five thin navy staff lines under the header, navy primary button, outlined pill for the sign-in-link button, no emoji; Inter body. `teacher-dashboard.html` kept its layout and logic and only changed colours and fonts: the Tailwind indigo and slate palette is remapped to the drills' navy, muted navy and cream (235 inline hex values remapped by script, plus an override block for the Tailwind `slate`/`indigo` classes with `!important`, plus `rgba(99,102,241,..)` to navy); headings use Playfair Display, body Inter (Pretendard stays as the Korean fallback); cards use the drills' surface, 1.5px navy hairline and soft shadow. Red, green, amber, teal and violet stay as they are because they carry meaning (absent, on track, check, lesson types). Verified in headless Chromium against a local copy (Tailwind CSS generated with the v3 CLI from the file, Inter and Playfair served locally, Supabase calls stubbed, three fake students): login (desktop, mobile, error and link-sent states), dashboard Today, Students, Schedule and a student's detail page all read correctly, JSX compiles, sign-in and sign-out flow still passes, no page errors. Not checked: Add student / Log lesson modals and the PDF/Excel export look (colour only, no logic changed). `drills.html` untouched. |
| 332 | 2026-10-07 | **Student link panel in the teacher dashboard (step A2).** `teacher-dashboard.html` student detail page gets a "Student link" card between the header card and "This month" (`StudentLinkPanel`, hidden when printing). With no link yet: a name field (defaults to the student's first word, max 40, this is the only name the student ever sees) and "Create student link". With a link: Active/Paused badge, the read-only link `<site>/drills.html#k=<token>` with "Copy link", "Pause link" / "Resume link" (sets `active` and `revoked_at`), "New link" (two-step confirm, old link stops working), "Rename", and a line saying anyone with the link can open that student's record. The token is 27 random bytes from `crypto.getRandomValues`, base64url, so 36 characters (the table requires 32 or more), and sits in the URL fragment so it is not sent to any server or Referer. All reads and writes go through the teacher's own signed-in session and the RLS policies from Phase 330 (`student_links`); no keys, no Edge Function, no new data about the student beyond the display name. Verified in headless Chromium against a stubbed in-memory `student_links` that enforces the same checks (token length, name length, one link per student): create (empty name refused), link format, copy to clipboard, pause, resume, new link (cancel keeps the old token, confirm changes it), rename, second student has its own panel, panel fits a 390px screen, no page errors. The panel also says that trying a link on her own computer switches that browser to the student view, and that `?teacher=1` on the drills address switches back (see Phase 333). Note: the dashboard's top bar already overflows sideways on phones (same before this change); not touched. Not yet checked live: needs the push, then Sohyun opens a student and creates a link. The drills do not read the link yet (step A3). `drills.html` untouched. |
| 333 | 2026-10-07 | **The drills open a student link (step A3).** A visitor who opens `drills.html#k=<token>` now sees "Hi, <first name>!" and a "Not me" button in a slim card under the header (Korean: "<name> 님, 안녕하세요!" / "내가 아니에요"). Code in `drills.src.html` just before `readUrlState`: `linkTokenFromHash` (accepts only 32-64 chars of A-Z a-z 0-9 - _), `loadStoredLink` / `saveStoredLink` / `forgetStudentLink` (localStorage `pb_link_token_v1` and `pb_link_name_v1`), `fetchStudentInfo` (plain `fetch` POST to `/rest/v1/rpc/pb_student_info` with the public anon key, 8 s timeout, no supabase-js), and `<StudentBanner/>` inside `App` only. States: valid -> name; unknown or paused token -> "This link isn't active. Ask your teacher for a new one. You can keep practicing." + Remove (a fresh bad link is not remembered; an already remembered one is kept, in case the teacher resumes it); network or server trouble -> "Couldn't reach your link just now..." (a remembered name still shows, so a tablet with no wifi still says Hi); a server error is never shown as "link not active". Nothing runs without a token: a visitor with no link makes no request, stores nothing, and the page DOM is identical to the old build (checked old vs new, English and Korean, four routes, seeded random). `?book=` and `?print=1` routes never reach `App`, so they never call the database. The URL sync effect now keeps `location.hash` (before it dropped it), so refresh, bookmarks and Add to Home Screen keep the link; the fragment is never sent to a server and the token never appears in a request URL. A student link also opens the clean student view and remembers it, like `?teacher=0` (the drills default to the teacher view); `?teacher=1` wins, so Sohyun can test a link on her own computer and get back. Opening another student's link on the same device switches to that student (step B adds the shared-tablet data rule). Built with `tools/precompile.js` using @babel/standalone 7.29.9, the version that reproduces the committed `drills.html` byte-for-byte (the Babel in the repo's own `node_modules` is version 8 and writes a different but equivalent file; use 7.25-7.29 so diffs stay small). Verified in headless Chromium with the database stubbed: valid link, remember across visits, Not me (clears storage and fragment, stays in student view), Korean, paused link, offline, server error, malformed or script-like tokens ignored, print routes silent, 320px width, no page errors, first render time unchanged (median 183 ms old, 169 ms new). Not yet checked live: needs the push and one real link from the dashboard. Nothing is saved or synced yet (step B). |
| 334 | 2026-10-07 | **Teacher dashboard shows which account is signed in.** Sohyun found that opening `login.html` signs her straight in (the saved session sends her on to the dashboard, as designed) and asked for some sign of who is signed in, so it is not confusing later. `teacher-dashboard.html` header now shows "Signed in as <email>" in small muted text under the title (the email comes from the session already loaded by `requireAuth()`; no new request; one line, cut with an ellipsis if long; hidden when printing), and the Sign out button's tooltip names the account ("Sign out of <email>"). `login.html` is unchanged: it still goes straight to the dashboard when a session exists. Verified in headless Chromium against the same stubbed Supabase as Phase 332 (20 checks, no page errors); the phone-width overflow of the top bar is exactly what it was before (572px wide in a 390px screen, not made worse). Not yet checked live. `drills.html` untouched. |
| 335 | 2026-10-07 | **Simpler Add / Edit student form in the teacher dashboard.** Sohyun asked for just name, age, and for exam students only the grade; she cannot remember when each student started, so that question goes. `StudentModal` in `teacher-dashboard.html` now asks: Student name, Age (optional, 1-99, saved in the `extra` blob so no database change), Exam (two buttons: "No exam" / "Preparing for an exam"), and only when exam is chosen a Grade dropdown (Preliminary to Grade 8; an older free-text grade such as "Beginner" stays selectable so editing never loses it) plus an optional Exam date (kept on purpose: the countdown, the D-days badge and the monthly plan all key off the exam date, and a student with no exam date is treated as a general student). Lesson duration, frequency and day/time stay (the Schedule and Today tabs need them). Removed from the form: Grade / Level free text, Goal, Exam type (this also removes the exam-board names that were in its placeholder), Current preparation stage (the plan already spreads its phases over the months left to the exam; new students start at Foundation) and "Lessons started with me". New students get start date = today. Fortnightly students instead get "Which week is a lesson week? This week / Next week", because the lesson weeks are counted from the start date: the choice moves the start date by 7 days (so an existing student's plan start is not reset). Existing students keep everything they had (old goal, stage, exam type, start date are not deleted, just no longer editable here). The student card and the student page show "Age N" before the grade. Switching back to "No exam" clears the exam date. Verified in headless Chromium with a stubbed database (32 checks): empty form, exam student, no-exam student, age bounds, fortnightly this/next week, editing an exam student keeps start date, exam date, grade and goal, editing a student with a free-text grade, form fits a 390px screen, no page errors. Not yet checked live. Not changed: the bulk Import schedule and the PDF/Excel exports (they still list whatever a student has). |
| 336 | 2026-10-07 | **Music Lab (new page `music-lab.html`): load a score, pick bars, practise slowly with a live beat and note names.** Sohyun had been prototyping this in a ChatGPT site (Stages 1-4: upload MusicXML/MXL, draw the score, metadata, bar selection, play/loop/tempo/metronome) and asked to build it here instead (the ChatGPT prototype needs a ChatGPT sign-in, so it was not opened -- rebuilt from her stage list). Decisions from Sohyun: scores are uploaded by her (IMSLP public-domain editions, no bundled copyrighted AMEB pieces), tried with her own students first, opened to everyone only once it works. So: `noindex, follow`, not linked from anywhere, not in the sitemap. (1) *Score:* OpenSheetMusicDisplay 1.9.9 (BSD-3) draws it; **self-hosted in `lib/opensheetmusicdisplay.min.js` + `lib/opensheetmusicdisplay.LICENSE.txt` because cdnjs does not carry OSMD** (checked: 404, search returns 0); no CDN dependency, nothing uploaded, files stay in the browser. Accepts .musicxml/.xml/.mxl (zip detected by its PK header; text must start with `<`, otherwise OSMD would treat the string as a URL and fetch it). (2) *Info:* title, composer, key (read from the first bar's key instruction, because this OSMD build has no `ActiveKeySignature`; shows 'F major or D minor' when the file gives no mode), time signature(s), written tempo (or 'assumed 90'), bar count. (3) *Bars:* tap a bar to start, tap another to end (same bar twice = one bar); coral boxes drawn from OSMD's own bar geometry; Clear selection; none selected = whole piece. (4) *Playback:* Web Audio piano-ish synth (triangle + two sine overtones), look-ahead scheduler; Play / Pause / Resume / Stop, Loop (gapless wrap), Metronome (compound time clicks per dotted beat), Count-in (one bar), tempo 30-130 percent of written with a live BPM label; pick-up bars handled (beat counted from the end of a nominal bar); ties joined into one long note; grace notes skipped. (5) *Live beat + note names (the Stage 5 Sohyun asked for):* bottom dock shows the bar number, beat dots (strong beat navy), and the note names sounding right now per staff (Upper/Lower for a piano, part names otherwise), as Letters / Do Re Mi / Both; Back / Next steps one cursor position at a time (and plays that note); cursor is coral; A- / A+ resizes the score. **Repeats:** OSMD's cursor walks the PERFORMED order (repeat signs unfolded, written time jumps backwards). The model keeps each written bar once (skips the second pass until time moves past the furthest bar recorded) and moves the cursor by OSMD's raw step index; the page plays the score as written, repeat signs are NOT played twice (footer says so). Playing repeats/voltas/D.C. is the obvious next feature. **Verified:** inline script `node --check`; headless Chromium with the real OSMD against a generated 12-bar two-staff test score (A-flat major, 2/4, tie across a barline, rest, chord, repeat) and its zipped .mxl: 44/44 checks (metadata, no duplicated notes, tie length, bar clicks and highlight, exact range in quarter notes, scheduled frequencies, beat dots and bar number advancing, pause/resume/stop, loop pass length 3.69 s at 130 percent, count-in then strong-click-first at 0.6 s spacing, Do Re Mi / Both names, step, play-to-end, cursor inside bar 9 after the repeat, bad file -> friendly error and recovery, zoom, 390 px phone with no horizontal overflow, zero page errors). Also loaded real public-domain scores from the OSMD test set without errors: Joplin 'Elite Syncopations' (88 bars) and 'The Entertainer' (92), Schumann Dichterliebe (pick-up bar, voice + piano), Beethoven An die ferne Geliebte (file starts with a BOM), Bach Air (4 staves), Schubert An die Musik; each loads in about 0.5-2.4 s and plays. **Not verified:** actual sound (headless browser; only the scheduled oscillator frequencies/times were checked), a real iPhone/iPad (the silent switch can mute Web Audio; hint in the footer), and Sohyun's own Maple Leaf Rag .mxl. Ask her to open it on the iPad with that file. Files: `music-lab.html`, `lib/opensheetmusicdisplay.min.js`, `lib/opensheetmusicdisplay.LICENSE.txt`. Test files stayed outside the repo (cloud scratch). **Follow-up (same day): note names can now be written ON the score** — two chips, "Top staff · RH" (coral, above the upper staff) and "Bottom staff · LH" (navy, below the lower staff); one row per system placed clear of stems/beams, works with Letters / Do Re Mi / Both and zoom; OSMD system spacing is widened only while names are on so rows of adjacent systems do not collide. Verified headless: label counts equal note events (demo 22+17, The Entertainer 1572=1572), 44/44 suite, zero page errors, 390px phone no overflow. Known cosmetic: on dense first systems the top row can touch a tempo/title text. |
| 337 | 2026-10-07 | **Student "Today" page, homework from lesson logs, and a daily practice check (step B1).** Sohyun (2026-10-07) wanted a student who opens their link to see what to do today first (homework and current pieces, which she logs at lessons) and wanted to see in the dashboard whether the student practised. **SQL (not yet run):** `migrations/2026-10-07_phaseB1_student-today.sql` adds table `practice_checkins` (student_id, day, minutes 1-600; row level security: the teacher can read and delete their own students' rows, anon has no table access) and functions `pb_student_today(token)` (name, the latest non-absent lesson's `homework` text and date, last 3 weeks of check-ins), `pb_checkin(token, day, minutes)` (upsert; the day must be within 2 days of the server date) and `pb_uncheck(token, day)`, plus helper `pb_safe_jsonb`. Only the homework text is ever returned from a lesson log, never notes, mood or ratings. The homework is stored in the existing `lesson_logs.extra` JSON (no column change). **Dashboard (`teacher-dashboard.html`):** Log lesson gets a "For the student" box (one item per line, "Copy from notes" button; the Notes box stays private), saved as `extra.homework` and shown in the lesson history; the Student link card gets "Daily practice" (14 dots, this week's days and minutes, last practised), reading `practice_checkins` and hidden silently until the SQL is run; the card text no longer promises progress sync. **Drills (`drills.src.html`, rebuilt `drills.html`):** `fetchStudentInfo` now sits on a generic `pbRpc`; a `useStudentLink()` hook is shared by the banner and the new Today tab, which is the first tab for a linked student (a link in the address, or one remembered on the device, lands on `?view=today`; an explicit `view=`, `drill=`, `tool=`, `kit=`, `lock=1` or `?teacher=1` wins; "Not me" or an inactive link goes back to Learn). `TodayView`: date, homework card (ticks are this device's own memory, `pb_today_ticks_v1`, keyed by a token prefix; the teacher does not see them), big "I practised today" button with optional 5/10/20/30+ minutes and Undo (the student's own local date; an error line if saving fails; no offline queue), Monday-first week dots, days this week and days in a row, a Keep going card (last chapter, Continue, All chapters), a reload when the tab comes back after 30 s, and the last answer cached per token (`pb_today_cache_v1`) so the page opens offline. English and Korean strings for everything. A visitor with no link sees a DOM identical to before (tested), and print routes make no database call. Tests: 76 SQL (PGlite), 22 dashboard Phase 337, 20 dashboard link panel, 32 student form, 44 drills link, 70 Today; `drills.html` rebuilt with Babel 7.29.9. Not done yet: sharing homework ticks with the teacher, and progress sync (step B proper). Committed locally, not pushed. |
| 338 | 2026-10-07 | **Simpler Log lesson window: every section is a short numbered list.** Sohyun (2026-10-07) found the old window heavy and asked for repertoire as separate items numbered 1 to 8, with technical work and the other sections addable the same way. `LogModal` in `teacher-dashboard.html` now has five lists (Repertoire, Technical work, Sight-reading & aural, General knowledge, For the student), one input per row with a number, a "+ Add" button (up to 8 rows, 12 for "For the student"), a × to remove a row, Enter to add a row below (and focus it), Backspace on an empty row to remove it. Each row grows with its text, so nothing is hidden on a phone. Repertoire rows have one circle that cycles red, yellow, green, none (the old traffic light, now per piece). The row of tag buttons (HS, HT, Slow practice, ...) is gone. "+ From repertoire" copies the piece names (no ratings) into "For the student". Notes is now "Notes (private)" with its Copy button, and "Copy from notes" is removed. The new-log reminder shows the last lesson's "For the student" text, or its notes if there is none. **No database change:** each list is saved as lines in the same text columns (`repertoire`, `technical`, `sr_aural`, `general_k`; `extra.homework`); a rating is a leading 🔴🟡🟢 on the line, as before. Old logs open as rows by line, with the old single rating on the first row, nothing is cut off (a 10-line log opens with 10 rows), and saving an old log unchanged writes exactly the same text. Blank rows are dropped. Tests: 47 (dashboard Phase 337/338), 20 link panel, 32 student form. Committed locally, not pushed. |
| 339 | 2026-10-07 | **Homework lines can open a chapter or a practice activity.** Sohyun asked how the drill chapters connect to the student's page besides the lesson log; decided with her (2026-10-07): in the Log lesson window, "For the student" gets a "+ Chapter / activity" button (picker with the 25 chapters in path order and the 15 practice activities, e.g. Practice dice, Posture check, Metronome). A picked row is a normal line the teacher can retitle ("Scales, step 3"); it is stored as the same text with a mark at the end, `Scales, step 3 [chapter:scales]` or `Practice dice [tool:practice-dice]`, in `lesson_logs.extra.homework` (no SQL change; the SQL already returns the text). The lesson history shows "↗" instead of the mark. **Drills:** the Today page strips the mark and gives that row an "Open →" button (KO "열기 →"); a chapter id or tool id the drills do not have is shown as plain text with no button; an empty label falls back to the chapter / tool name. Opening goes to the chapter (`?drill=`) or the tool (`?tool=`, Practice view) and its back button says "← Today" (KO "← 오늘") and returns to Today; the memory of where you came from (`st.from`) is cleared by the tabs and only applies to the same chapter or tool, so Learn and Practice behave as before. The dashboard list `DRILL_LINKS` is a copy of the drills' chapter and activity ids and names (it was generated from the built drills page with the helper script used in testing); **when a chapter or practice activity is added to the drills, add it to `DRILL_LINKS` in `teacher-dashboard.html` too** (until then it just is not in the picker, and nothing breaks). Tests: 65 dashboard (picker list is checked against the built drills page), 86 Today, 44 drills link, 20 link panel, 32 student form. Not done yet: automatic "done in the app" ticks and the teacher seeing chapter steps (progress sync, step B proper). Committed locally, not pushed. |
| 340 | 2026-10-07 | **Log lesson without Sight-reading and General knowledge; a way back to Today.** Sohyun (2026-10-07) wanted the Log lesson window as simple as possible: Sight-reading & aural and General knowledge are no longer lists in the form, she writes them in Notes (the Notes box is now 3 rows with a placeholder that names them). Nothing already logged is lost: when a log being edited already has text in `sr_aural` or `general_k`, those two lists still appear (one item per line) and save unchanged, and the lesson history still shows them; the database columns and the Excel export are untouched. Because the form no longer asks for them, the lesson guide in `teacher-dashboard.html` no longer raises "Sight-reading & Aural missing" and "General Knowledge not recorded" alerts. **Drills:** a student with a link now gets a "← Today" button (KO "← 오늘") at the top of the Learn list and the Practice list, because "All chapters →" from Today had no obvious way back (the Today tab is only at the top of the page). A chapter opened from the Learn list still goes back to "← Learn". No link: no change (DOM identical, tested). Tests: 71 dashboard, 95 Today, 44 drills link, 20 link panel, 32 student form. Committed locally, not pushed. |
| 341 | 2026-10-07 | **The lesson log's Repertoire shows on the student's Today page as "Pieces you're working on".** Sohyun (2026-10-07) asked how a repertoire she adds relates to the student's Today page and chose to show it automatically. New SQL `migrations/2026-10-07_phaseB2_student-today-pieces.sql` (run once in the Supabase SQL editor after B1; safe to run again): the helper `pb_pieces_json` takes the latest lesson log that is not an absence and has a non-empty Repertoire, one piece per line, with the leading red/yellow/green rating mark removed (at most 12 pieces, 120 characters each), and `pb_student_today` now also returns `pieces`. Ratings, notes, mood and technical work still never leave the database; the text of a Repertoire row IS shown to the student, so the dashboard hint says so and private remarks belong in Notes. A lesson log with an empty Repertoire leaves the previous list in place. **Drills:** a new card on Today between the homework card and the practice card (music-note rows, names only, not tickable; EN "Pieces you're working on" / KO "지금 연습 중인 곡", with a small note that the teacher updates it at lessons); the saved copy keeps the pieces for offline use; an older database without `pieces` simply shows no card. **Dashboard:** the "+ From repertoire" button is removed (redundant now), and the Repertoire hint, the "For the student" hint and the student-link card say what the student sees. Tests: 111 SQL (PGlite, both id/date/extra type variants), 29 pieces card, 95 Today, 44 drills link, 71 dashboard, 20 link panel, 32 student form. Committed locally, not pushed; the SQL is still to be run. |
| 342 | 2026-10-07 | **Progress Passport no longer shows Sight-reading / General knowledge when nothing was logged.** Sohyun (2026-10-07) still saw "SR & Aural 0%" and "General Knowledge 0%" bars after Phase 340 removed those two lists from the Log lesson window: they were in the Progress Passport (student page), which counts how many lessons have each section filled. Fix in `teacher-dashboard.html` only: the "GK covered" tile is gone (three tiles remain: Attendance, Lessons logged, Lesson streak) and the SR & Aural / General Knowledge coverage bars show only when at least one lesson in the selected period still has text in that section (old logs), so nothing with data is hidden. Left on purpose and asked about: the "This month" time chips (Repertoire / Technical / SR/Aural / GK minutes) are a lesson-time plan, not logged data. Tests: 8 new Passport checks (fail on the Phase 341 file, pass on this one), plus 71 dashboard, 20 link panel, 32 student form. Committed locally, not pushed. |
| 343 | 2026-10-07 | **"This month" card shows only the Repertoire time.** Sohyun (2026-10-07), asked about the lesson-time chips on the student page (Repertoire / Technical / SR/Aural / GK minutes), chose to remove all but Repertoire to keep things simple. `teacher-dashboard.html` only: the card now shows one chip (e.g. "Repertoire 25m" for a 45-minute lesson). The plan data itself (`getAlloc`) and the Excel plan export columns are unchanged. Open question to Sohyun: whether to also drop the "Technical work" list from Log lesson (scales are in the drills: chapter 14 "Scales", group "Scales & Keys", plus the Scale finder tool; the "+ Chapter / activity" picker can give the student an Open button for it), handled like Sight-reading / General knowledge (old logs keep their text). Tests: 3 new chip checks (fail on the Phase 342 file, pass on this one), plus the Passport checks, 71 dashboard, 20 link panel, 32 student form. Committed locally, not pushed. |
| 344 | 2026-10-07 | **Log lesson without "Technical work".** Sohyun (2026-10-07) answered yes: scales are in the drills (chapter 14 "Scales", group "Scales & Keys", and the "+ Chapter / activity" picker gives the student an Open button), and anything else technical can go in Notes or "For the student". Same handling as Sight-reading / General knowledge (Phase 340): the Technical list shows only when the log being edited already has Technical text (saved unchanged, still in the history and the Excel export). The Log lesson window is now Repertoire, For the student, Notes. Also in `teacher-dashboard.html`: the lesson guide no longer raises "Technical work hasn't been recorded for 2+ weeks", the "all sections covered" praise now reads "repertoire recorded at every recent lesson", the unreachable 30-minute-lesson tip is removed, and the Progress Passport shows the Technical bar only when a lesson in the period still has Technical text. The plan data (`getAlloc`) and the Excel plan export are unchanged. Note for tests: `document.body.textContent` includes the page's own source (in-browser Babel), so text checks use `innerText`. Tests: 6 new Passport/guide checks (fail on the Phase 343 file, pass on this one), 72 dashboard, 20 link panel, 32 student form. Committed locally, not pushed. |
| 345 | 2026-10-07 | **Progress sync, step 1 of 3: the database (SQL only).** Sohyun (2026-10-07) said go. New file `migrations/2026-10-07_phaseB3_progress-sync.sql` (run once in the Supabase SQL editor, name it "B3 progress sync"; safe to run again; needs A1 and B1): tables `progress_store` (student_id, store, value jsonb, rev, updated_at; stores = records, stamps, lesson_steps, steps_total, posture, arm_ex, last_chapter) and `practice_log` (one row per drill play: at, drill, level, mode, score, correct, total; unique per student/at/drill/level/mode), both with row level security (the teacher can select and delete the rows of their own students; nobody else; no anon access). Students use three SECURITY DEFINER functions with the secret token: `pb_get(token)` -> {ref, name, stores:{store:{value,rev}}, server_time} (ref = a stable 16-character code from md5 of the student id, the same after the link is regenerated, used to tell one child from another on a shared device); `pb_save(token, store, value, base_rev)` saves only when base_rev equals the stored revision, otherwise returns {ok:false, reason:'conflict', rev, value} (base_rev 0 = never saved; a cleared store answers rev 0 so the device starts again); `pb_log(token, rows)` adds up to 50 plays at a time, skips bad rows and duplicates, refuses past 20,000 rows per student. Limits: records 300,000 characters, other stores 60,000; last_chapter is a string up to 60 characters. Nothing personal is stored (no name, email, age, voice). Lesson: in PL/pgSQL an IF condition ends at the first THEN, so a CASE...THEN inside an IF condition breaks the function; compute it into a variable first. Tests: 140 PGlite checks (both students.id types): token isolation, conflicts, validation, limits, teacher-only access, regenerate and pause, cascade delete. Not yet run in Supabase; the drills do not use it yet (step 2 = the sync engine in the drills, step 3 = the dashboard progress view). Committed locally, not pushed. |
| 346 | 2026-10-07 | **Music Lab: "Play repeats".** New chip in the dock (shown only when the score has repeat signs). Off by default, so a chosen bar range still plays once as before. On: the page follows the repeat signs and first/second endings as written, joined gaplessly (same scheduler path as Loop). A chosen range only repeats if it includes the bar where the repeat jump happens (bars 1-4 of a piece repeating 1-8 play once; bars 7-8 play twice). Built from the OSMD cursor walk (performed order) split into segments wherever the written time jumps. Verified headless: repeats test (notes on = 2x off, pause/resume across the jump, no errors), 44/44 main suite, on-score names suite, segments on Joplin Entertainer / Elite Syncopations (voltas), Bach Air, Schubert. Not verified: real sound on iPad. |
| 347 | 2026-10-07 | **Progress sync, step 2 of 3: the sync engine in the drills.** Sohyun (2026-10-07) said go. (Numbered 347 because another session took 346 for Music Lab.) Only runs on a device that holds a student link; a visitor without one gets no request, no wrapped storage and no extra keys (tested: DOM identical to before, first render unchanged, print routes never call the database). The 7 progress stores (`pb_drill_records_v1`, `pb_scale_stamps_v1`, `pb_lesson_steps_v1`, `pb_steps_total_v1`, `pb_posture_v1`, `pb_arm_ex_v1`, `pb_last_chapter_v1`) follow the student between devices through `pb_get` / `pb_save` (revision numbers) and every finished drill play is added to the practice log with `pb_log` (queued on the device, sent in chunks of 50). A write to one of those keys is noticed by a small hook on `localStorage.setItem/removeItem` (installed only once a link exists) which marks the store dirty and pushes ~3 s later, when the page is hidden, and when the connection returns; marks and the log queue live in `localStorage` so a failure is retried. On a conflict the two copies are merged (records: plays/best/lastAt = larger, history = union by time, last 20; stamps and lesson steps = union; steps per chapter and arm exercises = larger; posture marks = union, history by day last 8; last chapter = this device) and pushed again. First time a link meets a device that already has practice and no owner tag (`pb_sync_owner_v1` = the student's `ref`), a card asks once: "Add the practice on this device to <name>'s saved progress?" (Yes = merge, plays add up; No = this device's practice goes to a backup copy `pb_sync_backup_v1` and the saved progress is used). Another child's link on the same device never merges: the first child's practice is pushed, then the synced keys, the sync bookkeeping and the Today page's own memory are cleared (if that push fails the child is asked "Leave anyway / Stay", and a backup copy is kept); a new link for the same child (same `ref`) changes nothing. "Not me" does the same push-then-clear; "Remove" on an inactive link keeps the practice. While a chapter or tool is open nothing is rewritten under the student (pulls wait until they leave it, then the page content is rebuilt once). If the database functions are missing (SQL 345 not run) every call answers 404 and the engine stays silent: no prompt, no line, and "Not me" keeps the practice as it always did. Today shows one quiet line ("Your progress is saved ✓" / "Not saved yet. We'll save it when you're online."). `pbRpc` now also returns the HTTP status. Verified in Chromium with a pretend database and several pretend devices (`sync346test.js`, 103 checks: two devices, conflicts, import yes/no, same-child new link, child switch, Not me, offline queue + Leave anyway/Stay, chapter-open deferral, a real played lesson reaching the log, Korean + 390 px layout) plus all earlier drills suites. Not verified: the real database (needs SQL 345 run first). Dashboard progress view is step 3. |
| 348 | 2026-10-07 | **Progress sync, step 3 of 3: the dashboard shows a linked student's drill progress.** Sohyun (2026-10-07) said go. `teacher-dashboard.html`: under the Daily practice strip in the Student link panel, a new "Drill progress" section (only for a student who has a link) reads `progress_store` and `practice_log` with the teacher's own login (RLS: own students only; the log read is the last 60 days, 500 rows; nothing is ever written from the dashboard). It shows: 14 day bars of drill sessions, this week's sessions/days, last 14 days, last drill practice, the 8 latest sessions (date and time, chapter name, level, Lesson/Game, result 8/10 or points), a collapsible best-scores table (per drill level: best, plays, last date), chapter steps done as chips (ticked/total), scale stamps (major n/36, minor n/36 with a collapsible grid of RH/LH/HT dots), and one line for the last posture check and arm-exercise reps. "Delete drill progress" (two clicks: confirm text "cannot be undone") deletes this student's rows in both tables with the teacher's own delete policies; the student's device then clears its own copy the next time it connects unless they practised meanwhile. If the tables are not there yet (SQL 345 not run) the section is hidden silently. The Student link panel text now mentions the drill record and warns that anything practised through the link is saved to the student's progress, so the teacher should use it only to look, in a private window. Verified in Chromium with a pretend database (`d348test.js`: no section before a link, empty state, full data, Leo never sees Mia's rows, delete cancel/confirm, tables missing, wording, no sideways scroll added) and the earlier dashboard suite. Not verified: the real database. Ideas not built: a teacher "look only" link that never syncs; showing this on the Today/Passport tab. |
| 349 | 2026-10-07 | **Dashboard: Student link, Daily practice and Drill progress are three separate cards.** Sohyun (2026-10-07), after seeing the live Drill progress (the sync works end to end on the real database: a played lesson showed up in Recent sessions): "it does not fit the Piano Butler design, make it clearly separated and easy to see". `teacher-dashboard.html` only. The one long panel is now three cards in the dashboard's own look (card + 4px left accent + heading row with icon, title and pill, big-number tiles like the Progress Passport): Student link (navy; the two warnings are now two coloured notice boxes "Keep it private" and "Trying it yourself"), Daily practice (green; tiles This week / Last 14 days / Last check-in, then a block with the 14 circles and the day number under each), Drill progress (coral; tiles This week / Last 14 days / Last drill / Scale stamps, then separate white blocks: Sessions bar chart with counts, Recent sessions table with result pills (green 8+/10, amber 5-7, red below; game = points), Best scores table (first 8, "Show all" for the rest), Chapter steps done as small cards with a progress bar, Scale stamps as chips with RH/LH/HT dots (major and minor), Posture and arm exercises, and a "Student data" footer with the two-click delete). Tile rows use inline `auto-fit` grids so they wrap on a phone and do not depend on Tailwind classes. Same data, same queries, same test ids; `d344full.js` and `d348test.js` now read the tiles instead of one sentence. Verified in Chromium at 1280 px and 390 px (no sideways scroll added) plus the earlier dashboard suites. |
| 350 | 2026-10-07 | **Scales chapter: the Scale finder first, the stamps last.** Sohyun (2026-10-07): "show the Scale finder first in the Scales chapter, then the fingering, and the check at the very end". Major scales now: Find any scale (Scale finder) -> Fingering patterns -> The shape -> Build it yourself -> Degree names -> Stamp your scales (the scale cards). Minor scales: See every form (the minor viewer: every key, its notes and fingering) -> Fingering patterns -> Three forms -> Build it yourself -> Stamp your scales. Both intros rewritten to match (EN + KO). `Lesson` gained an optional `storeAs={n}` on a `Step`: the step's "Got it" tick is stored under n (its old position), so the ticks students already made (now synced to the database) stay on the same steps after a reorder, and the printed Lesson Book keeps each step's paper extras (`bookExtras(id)[storeAs]`). Use `storeAs` whenever steps of an existing lesson are reordered. Verified in Chromium (`t350test.js`: both orders, old ticks follow their steps, a new tick is stored under the old index, Korean names, the scales Lesson Book renders) plus the earlier drills suites (logged-out DOM identical, first render unchanged, sync 103/103). |
| 351 | 2026-10-07 | **Dashboard student page in the drills' look: navy and coral only.** Sohyun (2026-10-07): the colours "feel mixed with the old design"; the current design is "only navy and coral, clean and modern"; she chose "the whole student page". `teacher-dashboard.html`, student page only (other dashboard pages unchanged): every section now starts with the drills' staff-line head (`.stf-head`, five thin navy lines with the title knocked out, copied from drills.html; `SecHead({title,right})`, right side for a pill, a count or "+ Log lesson") and sits in a plain card: Student link, Daily practice, Drill progress, This month, Teaching guide, Progress Passport, Makeup schedule, Lesson history, Full plan. Removed: emoji (link, calendar, piano, clipboard, makeup, pause, absent), the rainbow side/top stripes and phase colours (header, This month, guide, Passport, makeup, plan). Colours: navy `#26296b` for text, numbers, bars and pills (`navyPill` = `#ecebf5` on navy); coral `#e4572e` / `#c0431f` on `#fbe3da` (`coralPill`) only for attention (Paused, Absent, overdue, low results, "← now", delete, warnings); green stays only on the Daily practice "practised" circles. Avatar = navy circle with Playfair initials. Drill results: navy pill, coral when under half right. Scale stamp dots coral (as in the student page clock). Also fixed: "undefined× per week" when lessons per week is empty (now blank), and Drill progress "Chapter steps done" now counts lessons whose ids extend the chapter id (Scales = `scales-major` + `scales-minor`). Tests updated for the new structure (titles are outside the cards: `d351test.js`, `a2test344_351.js`); all dashboard suites pass; screenshots at 1280 px and 390 px. |
| 352 | 2026-10-07 | **One page for a linked student, and the music map (every chapter on one sheet).** Sohyun (2026-10-07), over several rounds of mockups: the student link should be "just one page" with a few practice tools; the general Learn explainer is not for students; scales and an overall map by default; "only navy and coral, clean and modern"; the map should look "like a mind map", "all on one sheet", and above all "don't lose the minimalism: too much information blurs what to look at" (a standing principle for everything). drills.src.html: (1) **StudentHome** replaces the tabs for a student with a link (no Today/Learn/Practice tabs): `TodayView` (with a small 3-step "how it works" strip: read what your teacher wrote, practise at the piano, tap I practised today; the Keep going card is gone, `compact`), then **My practice tools** (exactly posture-check, practice-timer, practice-dice, perfect-counter, metronome, each with its own small navy line + coral accent icon on a coral-tint tile, one line each), **My scales** = the **scale clock** (`ScaleClock`: 12 keys round a clock in circle-of-fifths order, C at the top, sharps to the right, flats to the left, the key signature beside each; three stamp dots per key = RH/LH/HT, a full key turns navy; Major/Minor; tap a key and stamp below; it reads and writes the same `pb_scale_stamps_v1` ids as the chapter's scale cards ("C:RH", "m:E:HT"), so both agree and the stamps sync; "See the fingering ->" opens the Scale finder tool on that key via `PENDING_SCALE`), and **My music map**. (2) **MusicMap**: one root "My music map · n of 25 done", the 7 PATH_STAGES branching from it (tree connectors), and each stage's chapters as small chips with a short name only (`CH_SHORT`, EN + KO): navy = done, coral ring = you are here (the last chapter if unfinished, else the first unfinished), a coral dot = started; no pictures, no descriptions, no step counts on the map (they live inside the chapter). Chapter progress counts lessons whose ids extend the chapter id (`chapterSteps`: Scales = scales-major + scales-minor). The same map is the Learn page (student view) and the teacher's Chapters tab ("unify everything"); the old long LessonPath list is no longer shown (the function stays). (3) The scale cards' note says "Stamps are saved with your progress" when a link exists. Mockups tried and dropped on the way: cheat-sheet cards with a picture per chapter, a radial overview with 25 dots and long branches of cards (too much). Tests: `t352test.js` (the Today suite rewritten for one page), `t352extra.js` (27: tools, clock, finger link, map states, teacher Chapters, Korean, stamps note), `p352test.js`, `a3test352.js` (logged-out DOM identical, first render unchanged), sync 103/103, t350 12/12. Korean is in but English came first (her priority); she still wants to check the Korean wording. |
| 353 | 2026-10-08 | **The music map drawn as a classic mind map.** Sohyun (2026-10-07, late): "the feel of a classic mind map, branching out round from the middle". `MusicMap` (drills.src.html) is now one SVG drawing (viewBox 480 x 556, scales to the width; about 11 px text on a 390 px phone, one screen): a navy centre circle ("My music map", n/25 done), thick curved main branches out to the 7 stages, clockwise from the top right (1-4 down the right side, 5-7 up the left side, so both sides balance), each stage a numbered circle + its Playfair name, and thin curved twigs to its chapters as pills with the short name only (navy = done, coral outline = you are here, coral dot = started). Pill widths are measured with the page font (canvas `measureText`, redone once `document.fonts.ready`). Each chapter is a `role="button"` group reachable by keyboard (Enter/Space); a transparent row-high rectangle enlarges the tap target. SVG text that must be Playfair uses an inline style, because the drills' global `* { font-family: Inter }` rule beats SVG font-family attributes. Same data, same states and the same three places as 352 (Learn, teacher Chapters, the student page). Verified: `t352test.js`, `t352extra.js` (now 28, incl. keyboard-reachable chapters and "one drawing, no pictures, no step counts"), `p352test.js`, `a3test352.js` (logged-out DOM identical, first render unchanged), sync 103/103, t350 12/12; screenshots at 390 px (EN, KO) and 1024 px. |
| 354 | 2026-10-08 | **The music map as one winding road.** Sohyun found the Phase 353 mind map unpleasant ("too many tentacles") and asked for something more sensual, sharing four editorial references (a typographic word map, sweeping hand-drawn curves with tiny figures, a winding road with big red circles, circles filling with red). `MusicMap` (drills.src.html, inside the Phase 352 block) is now one thin navy road that passes through 7 big circles (the 7 `PATH_STAGES`). Each circle fills with coral water as its chapters are done (a started chapter counts half; the water has a soft wavy top and rises once on load, skipped with reduced motion); a finished stage is a full coral circle. A tiny navy figure stands on the water in the stage you are in. Beside each circle: `01` + the stage name (Playfair) and its chapters as plain words (bold navy with a check = done, coral underlined = you are here, navy = started, faded = not yet); tapping a word opens that chapter, tapping a circle opens the stage's next chapter. The road ends in a final barline and *Fine*. Two drawings of the same road: phones get it winding down the page (circles left/right, words beside them); wider than 560px it runs in two rows like a board game (1-4 left to right, a U-turn, 5-7 back to Fine) so the whole map fits on one computer screen. Page title is now "My music map" (teacher: "Music map") instead of a second "Learn"; the count reads "2 of 25 chapters done". Test hooks kept (`music-map`, `map-count`, `[data-chapter]` buttons with `data-status`, 7 `[data-map-stage]`); new `data-here`, `data-fill`, `data-stage-circle`, `map-figure`, `data-layout`. Tests: new G block in t352extra (no words touching each other or a circle at 320/390/768/1024/1440px, fits one screen on a computer, fill levels, one figure, Enter on a circle, finished stage, reduced motion, Korean) plus the Today, sync (103), Scales and first-screen suites all pass; first render unchanged. |
| 355 | 2026-10-08 | **Dashboard: "today" is the teacher's own day, also in the morning.** Found while checking the dashboard at 00:37 Sydney time: `todayStr()`, `currentMonthStr()` and the Schedule's week keys used `toISOString()` (UTC). In Sydney UTC is still "yesterday" until 10-11am, so in the morning a new lesson log was dated the day before, Today did not show a lesson logged that morning as logged, and a lesson moved in the morning was saved under the Sunday before the week (`week_key`/`from_week`), so in the afternoon the move vanished from the calendar. teacher-dashboard.html now has `ymdLocal()` (the browser's own calendar day) for today, the month, week keys (Monday) and the plan helpers, and `normWeekKey()` reads any old Sunday key as the Monday after it when the overrides load (a row saved with the right Monday key wins over an old Sunday one), so moves saved before the fix show again. No SQL. New `tools/date355test.js` (pretend Supabase, clock fixed at 8:30am and 3pm Sydney): Today date, a morning log shows Logged, old Sunday-keyed "this week" and "from this week" moves show on the right day, a new move saves Monday 2026-10-05, a new log is dated 2026-10-08; it fails on the old file (4 failures) and passes now. The older dashboard tests had lessons hard-coded on Wednesday (the day they were written), so they now put the lessons on whatever day they run; d351test_month 2a/2c/3a and d348test 2e fail the same way on the old file (date-dependent test data), not caused by this. |
| 356 | 2026-10-08 | **Teacher dashboard in the drills' look: header, Today, Schedule, student cards.** Sohyun: the dashboard's Today and calendar were still the old design. teacher-dashboard.html only (no SQL). Header: "← Piano Butler", "Teacher Dashboard" in Playfair, quiet pill actions (Import schedule, Export ▾, + Add student, Sign out -- no teal, no emoji), three thin navy staff lines, then Playfair tabs with a coral underline (`role=tab`, `aria-selected`); on phones the header is not sticky and "Import schedule" shortens to "Import" so the four actions fit one line. **Today** is a running order (`TodayView` rewritten): times on the left, a thin line with one dot per lesson (open navy ring = to come, coral = the next lesson still to finish, green with a tick = logged, coral ring = absent and the name struck through, dashed = paused), the name (opens the student) and "Grade, phase, exam in N days", "+ Log lesson" / "Absent" or the logged/absent actions on the right (below on phones). The line under the date counts "3 lessons today, 1 logged, 1 absent, 1 paused". A day off shows a whole-bar rest on a little staff and "Next lesson: Tomorrow, 10:00 AM, Ruby Han". **Schedule**: round ← → arrows around "This week" (Playfair) and its dates; day headings with the weekday small and the date in Playfair, today in coral with a coral bar and a faint coral column; a coral "now" line across today; lesson blocks are navy on lilac-grey paper (logged = green bar and ✓, absent = coral bar and struck name, moved = dashed navy outline and "moved", paused / off week = dashed and faded); the per-weekday colours (`DAY_COLOR`) are gone. The week scrolls sideways as one piece (headings with the grid) with the hours stuck on the left, and on a narrow screen it opens at today (before, the headings and the grid scrolled separately and phones had a 227px sideways scroll). Reschedule / skip / revert / new-lesson windows: same navy, coral for removing, no emoji. Colours: `PHASE_META` is now a navy ramp that deepens through the plan (foundation light ... polish dark) with the exam phase coral; one avatar colour for all grades; student cards, the exam banner, the paused filter, the Absent/Makeup window and the Pause window use navy/coral (green only for "On track"/logged). Lesson-log rating dots and mood faces are unchanged (they are saved data). New `tools/dashharness.js` (pretend Supabase with a fixed clock) and `tools/dash356test.js` (37 checks incl. an automatic colour check that every colour on Today, Schedule and Students is paper, navy, coral or green; keyboard tabs; dragging a lesson still opens Reschedule; phone layout). The old suites pass (d344full 72, d351test, formtest 32, a2test 20, date355test 14); d348test 2e fails the same way as on the old file (date-dependent test data). |
| 357 | 2026-10-08 | **"My rhythms" on the student's page.** Sohyun asked earlier for the basic rhythms to be part of every student's page; this is the rhythm card next to the scale clock (order now: My practice tools, My scales, My rhythms, My music map). `RhythmSheet` (drills.src.html, Phase 352 block, new file `a3/rhythm357.jsx` read by `patch352p.js`): one card with two chips. **Note values**: the note tree -- 1 semibreve / 2 minims / 4 crotchets / 8 quavers (beamed in pairs) / 16 semiquavers (beamed in fours), each row one 4-beat bar, the count of notes on the left, faint lines from each note to the two it splits into -- plus the two dotted notes as chips (dotted minim = 3 beats, dotted crotchet = 1½). **Time signatures**: 2/4, 3/4, 4/4, 6/8 as stacked Playfair numbers and one bar of beat dots (strong beat coral, 6/8 in two groups of three). Tapping a row plays it (`playItems` for notes, a new `rsPlayMeter` click with accents for time signatures), highlights it in coral and shows its name (British first, US name after: "Crotchets ... (quarter notes)"), what it is, and how to count it ("1 & 2 & 3 & 4 &", "1 (2) 3 (4)", "1 e & a" ...) with the counted word lighting up as it plays; then "I can clap it" / "I can count it" stamps it. 11 stamps, saved in the scale-stamp store with an `r:` prefix (`r:crotchet`, `r:.minim`, `r:6/8`), so they already follow a linked student between devices -- no new store, no SQL; the scale clock and the dashboard's scale counts ignore them. Dashboard (teacher-dashboard.html): a "Rhythm stamps" block under Scale stamps on the student's drill progress (n of 11, stamped ones coral). Tests: t352extra H1-H18 (section and order, 7 rows / 4 rows, tap plays and names, counting lights up, stamp saved with scale stamps and synced, scale clock unaffected, Enter on a row, dotted crotchet, 6/8, second tap removes, Korean, no sideways scroll at 320/390) and d348test 2r; all drills suites pass (sync 103, Today, Scales, first render unchanged ~0.3-0.4 s); d348test 2e is the old date-dependent failure. |
| 358 | 2026-10-08 | **Styles chapter: "Two hands, four ways" (parallel, similar, contrary, oblique motion).** From Sohyun's cheat sheets (the musical-textures one) -- the drills had textures but nothing on how two lines move against each other, which a piano student meets in every hands-together scale. Sohyun chose to add new content inside the existing chapters, so the music map keeps its 25 chapters. New step 3 of the Styles chapter, `MotionTypes` (code in `a3/motion358.jsx`, added by the new `a3/patchcontent.js`, which runs after `patch352p.js` and writes `drills.src.t358.html`): both hands on one picture, the right hand on top in navy and the left hand below in coral, one dot per note, dashed lines between the hands showing the gap. Parallel keeps the gap (octaves), similar moves the same way with the gap changing, contrary spreads out and back (a contrary-motion C scale), oblique holds the left hand on G. Tap a way to hear it (piano, both hands, the dots and gap line light up note by note); "Ear test: which way?" plays one with the picture hidden and keeps a score. Kid-level wording, the usual term in brackets in Korean (평행 진행, 동방향 진행, 반진행, 사진행) -- for Sohyun to check. The old steps keep their ticks (`storeAs` 2, 3, 4; the new step stores under 5). On paper (`?book=lesson&ch=styles`) all four pictures print in a 2 x 2 grid with their one-line meanings. New `tools/contentharness.js` and `tools/t358test.js` (M1-M14: step order and kept ticks, gap shapes for each way, oblique left hand still, plays, ear test answered right, Korean at 320px, no sideways scroll, Lesson Book renders with no database call); all drills suites pass. |

## Current Status (as of 2026-08-17, traffic/indexing/AdSense numbers refreshed 2026-09-15 — see Phase 72)

> **Latest (2026-10-04, Phases 247-304):** Phase 304: new online chapter Famous Composers (era backgrounds, time machine, 22 composer cards with fingerprints and sounds, Who am I?, Name that tune). Books paused by Sohyun to be reviewed as a whole. Phase 303: Book 4 started -- Musical Form and Styles & Genres (eras, textures, swing, blues). Phase 302: Books 2-3 -- nine chapters (Steps & Skips, Dynamics, Signs, Tempo, Terms, Melody, Tones, Scales, Chords). Phase 301: Posture and Rhythm books -- Book 1 complete. Phase 300: First Steps (legato introduced early) and Pulse books. Phase 299: Intervals and Key Signatures books. Phase 298: Time Signatures and Ledger Lines books. Phase 297: book pages balanced, plus Note Names and Notes & Rests (workbook, teacher copy, lesson-book extras). Phase 296: printed books rebuilt for 1:1 lessons -- Together / At home / Play pages with worked examples, homework strip and log, a separate Teacher copy, and NEW SIGN symbol cards + REMEMBER lines in the Lesson Book (Reading the Staff sample, English). Phases 294-295: Do Re Mi next to letter names (always in Korean, teacher switch in English) and the first printed-book pages (Reading the Staff workbook sample with a per-concept check-up, plus an auto-generated Lesson Book layout for every chapter). drills.html and all 45 public site pages now use the **staff look** -- navy `#26296b`, coral `#e4572e`, ivory paper `#faf6ec`, Playfair Display headings, five-line staff headers, note-head bullets, staff-line chapter drawings (see the piano-butler-designer skill and Pending #0). Site emoji are line icons; favicon, logo SVG and og-image.png redone; contact pop-up light. drills.html also got: Korean for topic/chapter names and the new UI strings, a student "Keep going" card, the Scales major/minor switch restored; content passes added hands-on tools to Tempo, Musical Terms, Melody, Form, Styles, Pitch & Range, Pulse and The Piano’s Story (Phases 279-285); Korean for those two English-only chapters, every drill’s level names and the drill screen (Phase 286), and the whole Scales chapter (Phase 287). Phases 288-292: First Steps and Reading tunes content passes (Whole piano, Black-key jam, Hear it find it), colour words fixed, and the Korean backlog closed for every chapter, drill and tool, with accuracy fixes to earlier Korean (letter names not solfège, 붙임줄/이음줄, cadence names). Everything verified headlessly (45 pages, 151 tools, 24 chapter pages, 0 errors) but **not yet live**: 25+ local commits await Sohyun's `git push` (last pushed: `a1c488b`).


*This section replaces the many duplicate "Build Status / Pending Work / Known Issues" blocks
that used to repeat after almost every phase above (removed in Phase 59 for readability) — this
is the single current source of truth. The phase-by-phase history above is preserved for
technical context: bug root-causes, schema decisions, architecture notes.*

### Build status
All features listed across Phases 1–58 are built and were live prior to 2026-07-21. That session
confirmed live, via direct browser testing: `timeline.html` (full 6-step flow, no bugs at the
time) and `viva-voce.html` (one real bug found and fixed — PDF generation confirmed clean). All
41 public HTML pages passed a syntax/JSX regression audit on 2026-07-21 — no known blank-page or
silent-JS-error bugs remain as of that audit. This session (Phase 60, 2026-07-22) added real
AMEB syllabus content to `timeline.html`'s technical-work phase and a checklist card, and added
pricing UI to `find-a-teacher.html`. `timeline.html`'s new curriculum content was verified via
Babel compile + `node --check` + logic trace, then live-tested post-deploy on the real site —
confirmed working correctly (see Phase 60 #7 above). `find-a-teacher.html`'s pricing UI was
verified programmatically but not yet live-tested in a browser this session. Phase 61 (same day)
restricted `timeline.html` to AMEB only, per Sohyun's decision — she hasn't personally sat
ABRSM/Trinity exams, and the ABRSM/Trinity path only ever showed generic (non-syllabus-specific)
text anyway. Sight-reading/GK were confirmed to intentionally stay generic — Sohyun's call is
that they aren't cleanly itemizable per grade the way scales/arpeggios are. Same session, based
on Sohyun's real-screenshot feedback: shortened the dense month-card technical text, restyled
the Technical Work Checklist as scannable chips, and added a no-typing browsable piece picker.
Phase 62 (same day, next round of feedback): every phase (not just Technical) now generates a
real per-month checklist — Foundation and Musical Shaping use the student's actual chosen pieces
plus their existing curated `focus` tags and a new era-tip dictionary when pieces are supplied;
every month also got a collapsible week-by-week breakdown (4 beats per phase) and denser
checkmark/chip-style visual structure instead of a single paragraph. Verified via Babel compile
+ `node --check` + a direct Node logic trace against real Grade 5 data, then live-tested end to
end post-deploy (real pieces selected via both browse and search, era-tip generation confirmed
correct for Baroque and Romantic pieces, weekly toggle confirmed working, zero console errors) —
see Phase 62 #8 above.

### Revenue-critical status

| Lever | Status | What's blocking it |
|---|---|---|
| Organic traffic | **Still climbing, live-checked 2026-09-15.** 3-month totals (Jun 13–Sep 12): **319 clicks / 15.2k impressions**, avg CTR **2.1%**, avg position **12.4** — up from 186/10.3k (9/2) and 63/5.26k (8/17). Top queries unchanged in character, all diploma long-tail: `lrsm piano repertoire list` (17/575), `frsm piano repertoire list` (13/148), `atcl piano syllabus 2026` (3/203). | Nothing blocking — genuinely climbing, not flat. |
| AdSense (ca-pub-6523454944716812) | **UPDATE 2026-09-23: rejected again on 2026-09-19 (주의 필요, low-value content). Sohyun decided to wait for traffic — see Pending Work #6.** Earlier note: **The 주의 필요 (needs attention) flag is gone, live-checked 2026-09-15.** Site row now reads **준비 중** ("in progress/preparing"), status detail blank, last updated 2026-09-09 — a real change from the 주의 필요/"low-value content" flag that had stood since 06-21 and was still present (though stale) as of Phase 67 (08-13). Ads.txt still 승인됨 (approved). | 준비 중 is Google actively re-assessing, not an approval yet — worth Sohyun checking back in a few days rather than requesting re-review immediately; if it's still 준비 중 after ~1–2 weeks with no change, that's the moment to consider a manual nudge. |
| Payment info | **Now shows complete** — AdSense onboarding screen (checked live 2026-08-17) shows "지급: 프로필 작성이 완료되었습니다" with a green check, vs. the "1 of 2 steps" note from earlier sessions. | Worth Sohyun double-checking there's no residual step (e.g. a bank verification email) — but nothing currently blocking on this front from what's visible in the dashboard. |
| Ad units on content pages | **Confirmed LIVE 2026-08-17.** Directly inspected the rendered G5 page: `<ins class="adsbygoogle">` present with `data-ad-slot="5406851832"` and `data-adsbygoogle-status="done"` — the unit is real and serving, not a placeholder. | Nothing blocking. Account isn't approved yet, so no earnings dashboard is visible regardless of whether ads are technically serving. |
| Search Console indexing | **38/40 indexed as of 2026-09-15** (was 36/40 on 9/2), only 2 pages not indexed. | Nothing blocking — moving in the right direction. |
| Teacher outreach | **Closed — Sohyun's decision (2026-08-17): not sending it.** No longer a pending item. | N/A — settled, not a blocker. |
| ABRSM data quality | Repaired 2026-08-13 (Phase 67): 54 leaked composer names, 21 missing catalogue numbers, 13 publisher fragments, 11 lost accidentals, 117 placeholder nationalities, inline-HTML/`.js` parity restored. **Confirmed pushed and live 2026-08-17.** | Nothing blocking. |
| Exam Check-Up service | **Removed (Phase 162, 2026-09-27) — Sohyun decided not to activate it.** `find-a-teacher.html` deleted, its dead homepage entry card removed, robots.txt entry removed. | N/A — closed. |
| `butler.html` practice-tracker | Built, tested (67/67), committed (`57e7f5f`), pushed as of 2026-07-27 | **Sohyun decision needed.** Not yet linked anywhere, scope (private tool vs. public feature) still undecided. |
| AMEB internal linking | **Done, deployed, live-verified 2026-08-03 and re-confirmed live 2026-08-17** (commit `ea87edb`). All 12 AMEB pages (Prelim–G8, CertP, AMusA, LMusA) cross-link via a grade-nav strip; homepage also carries a 35-link `GradeDirectory` (Phase 67). | Nothing blocking — effect on crawl/indexing signals will take time to show. |
| Random Pick + local Lists (Phase 71) | **Live-verified 2026-09-15** end to end (create list, add piece, My Lists panel) — confirmed working, no console errors. One real bug found in the same feature and fixed same session (see Sight-reading generator + Lists confirm() bug row below). | Nothing blocking -- the `window.confirm()` fix is pushed and **live-verified 2026-09-23** (inline Delete?/Cancel, no native dialog). |
| Sight-Reading Generator (external Render service) | **Live-verified 2026-09-15** — generates a correct, grade-matched excerpt with notation, audio, and a working PDF download. Built and deployed in an undocumented prior session; this is its first appearance in this file. Takes ~40–50 seconds per generation (Render free-tier cold start + LilyPond compile) with only a static "Engraving your excerpt…" message and no time estimate. | Not blocking, but worth a small UX fix: add "this can take up to a minute" copy so a slow-but-working generation doesn't read as broken, given this project's history with exactly that kind of silent-looks-broken bug. |

### Idea map — consolidating what's scattered across files (2026-08-17)

Sohyun asked to consolidate before organizing further — several files turned out to be pieces of
the *same* idea, built in sessions not logged here, and never connected back to each other. This
section is the single place to look instead of re-discovering it file by file. **No priority
decision has been made** (Sohyun: "아직 모르겠음, 다음에") — this is a map, not a plan.

**Cluster 1 — the 30-Day Challenge, a plan half-executed.** `30-Day-Challenge-Community-Proposal.docx`
(+ Korean twin, both 2026-08-05) is a real strategic proposal, not a stray note: a paid,
subscription-style accountability community for adult returning pianists, deliberately hosted as
a "hidden sub-brand" on thepianobutler.com — same unlinked-page pattern as `find-a-teacher.html`.
It explicitly designs the build to **reuse existing engines** — `diagnose.html`'s "returning
player" flow as the front door, the AMEB Leisure corpus (no exam pressure), and **`butler.html`'s
rotation logic as the daily-mission engine**. It also names two decisions as required *before*
building: (A) proof-of-completion format (checkbox vs. photo/video), (B) platform (Discord vs. a
custom Supabase dashboard). What actually got built (2026-08-05 to 08-10, also undocumented until
now): `practice-challenge.html` (a real, working signup landing page — pilot free, Web3Forms
signup, `PILOT_MODE` flag, empty `STRIPE_PAYMENT_LINK` waiting for pilot validation) and a local,
uncommitted rewrite of `diagnose.html` scoped to AMEB Leisure only with softer question wording,
bridging to the challenge page via a `?level=` param. **What's still missing**: decisions A and B
were never made, and the mission content in `practice-challenge.html` is hard-coded example text —
`butler.html`'s rotation logic was never actually wired in. This is a stalled mid-build, not a
finished, dormant feature.

**Cluster 2 — Sohyun's own lesson-time toolkit, unrelated to the Challenge.** `puzzle.html`,
`score-reader.html`, `viva-voce.html`, and `butler.html` (in its original, standalone framing) all
serve a different purpose: things Sohyun uses herself to prepare for or run a lesson, not a
packaged product sold to strangers. These don't need to be merged with each other or with Cluster
1 — they're already distinct tools for distinct moments (crop/annotate/send a score during a
lesson; extract study info from a MusicXML file; generate a General Knowledge PDF pack; track
daily technical/aural/sight-reading rotation for a student). `butler.html` is the one file that
sits in both clusters — its rotation engine was *proposed for reuse* in Cluster 1 but was built and
tested as a private per-student tool in Cluster 2's spirit. That double-appearance is exactly why
it's been stuck undecided since Phase 64.

**Cluster 3 — two competing "second income stream" ideas sitting side by side, unresolved.**
Exam Check-Up (`find-a-teacher.html`, $25 one-off, 1:1, needs only a Stripe link to go live) and
the 30-Day Challenge (Cluster 1, pilot-free, group/subscription, still missing two build decisions)
are both aimed at the same slot — a paid offer beyond ad revenue — and neither has been chosen
over the other. This is most likely the actual source of the scattered feeling: not too many
tools, but two unresolved plans quietly competing for the same next step. Revisit when ready;
no need to decide both at once, and no harm in leaving both parked exactly as they are.

### Strategic direction — teacher directory/marketplace (decided 2026-08-25)

Sohyun asked directly: should Piano Butler move toward a teacher-matching/directory model
(MusicTeachers.com-style — teachers self-list profiles/ads, parents search and contact directly,
no curation from Sohyun) instead of, or alongside, the search-tool + personalization-tools
direction? Full reasoning given to her, decision below.

**Why not now:** this is a two-sided marketplace, a structurally different business from either
the search tool or the curated 1:1 matching in `find-a-teacher.html`. A directory only has value
to searchers once it has real supply — tens to hundreds of teacher listings, not the 3–5 founding
teachers `outreach-messages.md` was scoped for. Sohyun has already declined to send that outreach
(2026-08-17) — a directory model needs *more* supply to be useful, not less, so it's a taller
order than the thing already parked. Search intent is also unproven and unrelated to current
traffic: every query in Search Console today is repertoire/syllabus lookup ("lrsm piano
repertoire list"), never "piano teacher near me" — none of the current SEO asset transfers.
Established directories (MusicTeachers.com and similar) already own that keyword territory,
including competing against Google's local pack/Maps listings — a much harder fight than the
low-competition diploma-page long-tail Piano Butler actually won (Phase 64).

**The one angle worth keeping alive:** a generic directory competing head-on with MusicTeachers.com
is a bad bet, but a **syllabus-specific angle — "find an AMEB/ABRSM/Trinity-experienced teacher"**
— is a real differentiator generic directories don't have, and it's the one version that actually
builds on Piano Butler's existing data/traffic instead of starting a second business from zero.

**Decision:** not now — revisit once the site has meaningfully more scale/traffic (rough trigger:
same order of magnitude as the existing "login revival ≥1,000 visitors/mo" threshold — no need to
pick an exact number today). Until then, keep it alive at zero ongoing cost rather than shelving
it completely: `teach-with-us.html` stays live and unpromoted (not linked from nav) so any organic
teacher interest is still captured passively; no active recruitment, no build work, no new pages.
When revisited, build the AMEB/ABRSM/Trinity-specific angle, not a generic directory clone.

### Pending work (priority order)

| # | Task | Priority | Notes |
|---|------|----------|-------|
| 0 | **DESIGN PHASE -- staff look, ROLLED OUT 2026-10-02 (Phases 262-268)** | Done; optional follow-ups -- Sohyun | Direction changed 2026-10-02: Sohyun dropped the cut-paper multi-colour illustration direction and chose a two-colour "staff look" (navy #26296b, coral #e4572e, paper (ivory #f6f0e1 since Phase 269), Playfair Display headings, five-line staff headers, note-head bullets), inspired by a staff-line jazz-festival poster she shared. Mockups: Design artifact "Toolbox Header Options" (claude.ai/artifact/UNbMf8WyRj41uTyjdxYyAd). Applied across all of drills.html. Chapter heroes redrawn as staff drawings (Phase 272). Optional next: student 'Keep going' card, decide whether navy black keys stay. thepianobutler.com itself is still ink/brass -- extending the look there is a separate decision (piano-butler-designer skill also still describes ink/brass + cut-paper; update it if she confirms). |
| 0a | **Push, then live-check the staff theme** | Quick -- Sohyun | After `git push`: open thepianobutler.com and drills.html on a real phone and desktop. Check (1) Playfair headings and the Noto Music treble clef in the chapter drawings actually load (sandbox could only test with local font copies), (2) header staff band and sticky header on scroll, (3) home Contact pop-up, Random Pick, search results, (4) a repertoire page per board (title marker bar keeps AMEB maroon / ABRSM slate / Trinity green), (5) drills Korean mode, (6) share a link somewhere to see the new og-image (social caches may take time). |
| 0b | ~~Open tool-overlap merges~~ | Closed -- Sohyun 2026-10-03: not important, leave as is | Possible merges with chips: sharps-order + flats-order (same OrderBuilder), build-major + build-minor (ScaleBuilder), road-map + dc-ds-coda, major-shape + build-major, clef-basics + clef-story, count-along + time-sig-numbers, accidental-cards + sharp-flat. Claude's recommendation: merge 1-7. Also: 7th-chord/extension tools as optional Chords steps? Where should "Which bar did you hear?" live? |
| 0c | ~~Korean backlog in drills.html~~ | Done (Phases 286-292) -- one open choice for Sohyun | Every lesson, drill level and tool is now Korean in 한국어 mode. Left in English on purpose: Italian terms, pronunciation guides, counting syllables (1 e & a, trip-let), song titles, Roman numerals, and the English mnemonics (Every Good Boy..., FACE, Father Charles...). Decided 2026-10-03: keep the English mnemonics; Sohyun proposed adding fixed-do solfège (도레미 / Do Re Mi) alongside letter names in both languages -- scope and the English default still to settle (Korea uses fixed do = C; Australian school music often uses movable do). A question already on screen when 한국어 is pressed stays English until 다음 (answers are generated per question). |
| 0d | **Printed books: Lesson Book + Workbook + Teacher copy** (Phases 295-296) | Top -- Sohyun reviews the v2 sample | Decided 2026-10-03: English only (updated 2026-10-06: Korean is for the online translation only -- no Korean books for now); separate Teacher copy (not answers in the back); every workbook page = Together / At home / Play, with fun and creative activities on every page (Sohyun's top priority); homework flow = set in the lesson, done at home, checked next lesson with the teacher copy + sticker; symbol cards for every new sign in the Lesson Book; minimal but catchable at a glance. **Book split (agreed as a start):** Book 1 First steps & rhythm (First Steps, posture, Note Names, Pulse, Note Values, Rhythm, Time Signatures -- and **legato introduced early here**, Sohyun teaches it from the start); Book 2 Reading music (Five-Finger Positions, Reading the Staff, Ledger Lines, Dynamics & Articulation, Signs, Tempo, Musical Terms, **Melody & Phrasing**); Book 3 Scales, keys & chords (Tones & Semitones, Scales, Key Signatures, Intervals, Chords); Book 4 later -- Form, Pitch & Range, The Piano's Story, Styles/eras (core first). Built so far (Phases 296-299): Reading the Staff, Note Names, Notes & Rests, Time Signatures, Ledger Lines, Intervals, Key Signatures -- the whole "basics first" list. Also built (Phases 300-301): First Steps (legato on the first song), Pulse, Posture, Rhythm -- Book 1 complete. Also built (Phase 302): Steps & Skips (five-finger positions), Dynamics & Articulation, Signs, Tempo, Musical Terms, Melody & Phrasing, Tones & Semitones, Scales (major + minor), Chords -- Books 1-3 now complete except Hand & Clefs. Also built (Phase 303): Musical Form, Styles & Genres (incl. the style eras page). **Paused 2026-10-04 (Sohyun): review the whole book set together before building more.** Next: Book 4 rest (The Piano's Story, Pitch & Range) if wanted; Hand & Clefs; per-chapter print curation (remaining "tap" wording). Open: printing route. |
| 0e | **Cut-outs: pilot print test** (Phase 327-328) | Medium -- Sohyun (printer) | Ten Cut-out sets (26 pages) are built and live in Toolbox > Books > Cut-outs. Next: print them on a real printer with 3-5 students (check the 7 mm keyboard keys and 9 mm tokens are easy to handle, that two-sided flip-on-long-edge lines up the flashcard backs, that the fifths disc turns neatly on a paper fastener, and that the dice fold and glue cleanly on card). Remaining idea: era cards (hold until publishing). Famous Composers stays unlinked from index.html until publishing. |
| 0f | **Student links + progress tracking** (Phase 329 onward) | Top -- Sohyun answers, then build | Design v2 (simple first) is in `_workspace/student-login-sync-design-v2-simple.md`. Phase 0 (teacher login restored) is committed locally; after pushing, test a real sign-in at thepianobutler.com/login.html. Next: Phase A (SQL for Sohyun to run in the Supabase SQL editor, dashboard "Create student link", drills opens a student link), then B (sync + practice log), then C (Passport + This week). No chapter lock (decided 2026-10-07), voice recordings stay local. Before real students' data goes live Sohyun decides: privacy.html wording, parent consent, Supabase region, backups (free tier has none). **Status 2026-10-07:** Phase 0 and A are done and live (329-335); B1 = the Today page, homework from lesson logs, the daily practice check and chapter links (337-340; its SQL has been run) and B2 = the pieces she is working on shown on Today (341; SQL run) are live. B3 = progress sync is in progress: step 1 (SQL, 345: `migrations/2026-10-07_phaseB3_progress-sync.sql`, still to be run), step 2 = the sync engine in the drills (347, done, tested against a pretend database), step 3 = the dashboard progress view (348, done). All three steps are built and tested against pretend databases; they need SQL 345 run in Supabase to go live; then C. |
| 0g | **Music Lab (`music-lab.html`) -- try it with real students** (Phase 336) | Top -- Sohyun tests | Built and committed, unlinked + noindex. Sohyun: open it on the iPad with her Maple Leaf Rag .mxl (IMSLP/MuseScore public-domain scores only), check the sound, the bar-tap selection, loop + slow tempo, and the live beat/note names with a student for 2-4 weeks. Next features if it earns it: play repeats/voltas/D.C. (OSMD's cursor already walks performed order; the page currently keeps each bar once), a small public-domain library she curates, saving a student's chosen bars/tempo to their link. Do NOT add recording/grading before it is used in lessons. |
| 1 | Revisit: should `sight-reading.html` auto-redirect to the generator? | Medium — Sohyun | 2026-09-17: built and committed an auto-redirect version (Sohyun had asked for it), then she said she didn't like the result and asked to shelve it for now and revise later -- reverted locally (`81b724d`/`f4551b9`), never pushed, so the live site was never affected. `sight-reading.html` is back to its original static SEO landing page. Revisit when she's ready to say what she wants it to do/look like instead. |
| 2 | Decide what `AGENTS.md` is for | Medium — Sohyun | Found 2026-09-15: an untracked, stale (138-line-diff) mirror of this file, apparently read by a different AI coding tool (naming convention + one "Codex API" substitution suggest OpenAI Codex or similar). Decide: keep it and have future sessions maintain both in sync, or delete it if it's a stray leftover from a one-off experiment. |
| 4 | Re-check diploma-page CTR after re-crawl | Medium | 5 diploma pages retitled 2026-07-27 for CTR — still awaiting re-crawl to show effect. |
| 5 | Sohyun — glance at a real downloaded viva-voce PDF | Quick — deferred by Sohyun since 2026-07-23 | Sample already generated live, zero console errors. Just needs her eyes on it. |
| 6 | AdSense — WAIT for traffic (Sohyun's decision, 2026-09-23) | Parked | Re-reviewed 2026-09-19 and rejected again: 주의 필요, "가치가 별로 없는 콘텐츠" (low-value content) — Google's three tests are unique value, ongoing curation, and real user interest. Likely main factor: traffic (~4 clicks/day). Sohyun chose to change nothing and wait for traffic to grow rather than add teacher's notes now. Do NOT tick "문제를 수정했음" / request review, and don't nag about it. Revisit when 3-month clicks roughly double (~750+). If revived, the recommended fix is short teacher's notes in Sohyun's own voice on the top 5 pages (LRSM, FRSM, ATCL, LMusA, AMEB G3). Also check the AdSense banner saying payment info still needs adding. |
| 7 | Consider Render's paid Starter plan (~$7/mo) for the Sight-Reading Generator | Low — cost decision, Sohyun | Removes free-tier sleep entirely and gives real CPU (vs. today's 0.1 vCPU) — the one remaining lever that would meaningfully cut generation time further after Phase 73/74/75's free fixes. Only worth it if cold starts/slowness are still bothering visitors after those land. |
| 8 | Affiliate signup (Sheet Music Plus) | Deferred | Trigger: Search Console clicks ≥ 500 (now at 319, 3-month). |
| 9 | Login revival | Deferred | Trigger: visitors ≥ 1,000/mo. |
| 10 | ABRSM Diploma — ARSM / DipABRSM | Low | PDFs not yet available. |
| 11 | Rebuild `connect.html` if teacher referrals are revived | Deferred | File no longer exists (removed in Phase 54 cleanup) — would need rebuilding from scratch. |
| 12 | Diploma pages (LRSM/FRSM/ATCL/LTCL/FTCL) — outbound link to official syllabus | Low, optional | Raised and consciously declined as full content 2026-08-03 (out of "search tool" scope) — if revisited, keep it to a single link out, not reproduced requirements. |
| 14 | Should `drills.html` get a homepage entry point? | On hold -- Sohyun (2026-09-23: hold for now) | Built 2026-09-18 (Phase 89) as an unlisted, direct-URL-only teacher tool, same pattern as `timeline.html`'s original launch and `teacher-dashboard.html`'s deprioritized status -- reasoning: a lesson-side tool a teacher bookmarks directly probably doesn't need homepage discoverability, but this wasn't explicitly confirmed with Sohyun. Decide: keep unlisted, or add a link (e.g. from the homepage or a teacher-facing page). |
| 13 | Add AMEB Series 16 and earlier repertoire (Prelim–G8) | Low — whenever time permits, Sohyun to add pieces incrementally | Raised 2026-09-15 to broaden repertoire choice. Sohyun has an old physical syllabus/grade book she's checking for full piece lists — current syllabus PDF only covers S19/S18/S17 (Series 16 and earlier pieces are **not currently exam-valid** unless they also appear on the Manual List, per live web research this session). Sohyun's direction: show both — keep the current-valid search as-is, and add legacy/reference-only pieces with a clear badge/filter separating them (not mixed in with exam-eligible results). Build as incremental, grade-by-grade additions from her source material — cross-check each against her real syllabus before adding (no memory-only entries, per Reference Integrity rule), tag with a new `legacy:true`-style field or a series code (e.g. `S16`, `S15`) distinct from current codes, and add a "Legacy / reference only — not on the current exam list" badge in the UI. |
| 15 | ~~Verify remaining DRAFT black-root scale fingerings~~ | Done (Phase 97) | B♭, E♭, A♭, D♭ read off the AMEB books and fixed; C♯ = D♭. Sohyun may still eyeball them in the Scales tab. |
| 16 | drills.html chapters built (Phases 94-105) | Done -- review | Sohyun to try every chapter in the preview and flag anything off. Latest (2026-09-24): Key Signatures hands-on round (103), Note Names activities (104), sharps/flats + half/whole step moved to Tones & Semitones, new Intervals chapter (105). |
| 18 | drills.html -- open questions for Sohyun (asked 2026-09-24) | (c) closed 2026-10-03: interval song hooks not important, keep as is | (a) Note Names "Letter chain" (2nd-8ve chips): keep in Note Names or move to Intervals? (b) Note Names drill Level 4 "Black keys too (sharps & flats)": keep or move to Tones & Semitones? (c) Interval song hooks (Jaws, Happy Birthday, Greensleeves, Oh When the Saints, Here Comes the Bride, Twinkle Twinkle, My Bonnie, Somewhere, Over the Rainbow) -- swap for tunes Australian students know? |
| 19 | drills.html -- STANDING PRIORITY (updated 2026-09-28, supersedes the row below): visual-first pedagogy, every chapter | Top | Sohyun (2026-09-28): "설명이 많은 것보다 시각적으로 딱 이해가기 쉽게 만드는게 먼저 우선순위야. 많은 설명보다 보여주는게 더 받아들여지는게 빨라. 재밌는 요소들이 곳곳에 많이 깔려있어야해." Every chapter should lead with a visual/interactive element (an icon badge in the Toolbox list, a reactive illustration that responds to the tool's own state) rather than leaning on text explanation alone, with fun/memorable touches scattered throughout so child students retain it -- **ahead of, not just alongside, further prose rewrites or the remaining Korean translation backlog.** Recorded as a standing design principle in the `piano-butler-designer` skill (see its "Visual-first pedagogy" section) so future sessions don't need this restated. Phase 177 (2026-09-28) did the first rollout -- Chords chapter: `TOOL_ICON` badges on all 8 tool cards, a reactive smile/frown face in Major or minor chord, a reactive building-cake in Stack a triad, static icons on 4 more tools. Phase 178 (2026-09-28) did the second rollout -- Intervals chapter: 7 `TOOL_ICON` badges, a reactive flip-diagram in Invert an interval, a reactive tension-line in The tritone, a reactive step-meter in Count the semitones, static icons on 3 more tools. Phase 179 (2026-09-28) regrouped tie-slur and legato/non-legato/staccato into the Dynamics & Articulation chapter (they were scattered across 3 different chapters), put legato before staccato throughout per Sohyun's teaching order, and gave that regrouped chapter's 6 tools the same icon-badge treatment. **Next chapter to do this for, in curriculum order:** Signs & terms (now: road-map, grace-write, ornaments, ottava, plus term-match/term-cards in the separate Musical Terms chapter -- check the current tool set in the Toolbox before starting) -- then continue down the remaining curriculum order applying the same treatment, chapter by chapter, as its own multi-session effort rather than attempting all remaining chapters at once. |
| 19b | drills.html -- remaining content-coverage plan (curriculum order, pre-existing) | Next, after 19 | Sohyun's direction (2026-09-24): give every chapter key-signature-style hands-on, animated activities, going in curriculum order (Note Names done; Tones & Semitones partly -- has StepExplorer + SharpFlatMover; Reading the Staff done (Phase 106); Scales done (Phase 107); Notes & Rests done (Phase 108); Time Signatures done (Phase 109); Rhythm Cards done (Phase 110); Tempo Race (111) and Dynamics (112) done -- every existing chapter now has a hands-on round). New chapters still to build: Signs (repeats, D.C./D.S./Fine, 8va, ties vs slurs), Intervals Grade 3 add-on (inversions, A4/d5), then Chords (Roman numerals + letter names; check AMEB grade placement first -- Music Craft Prelim = tonic triad I in C/G/F, Grade 1 = I and V; **Chords chapter's hands-on content itself is done as of Phase 173-177** -- this line now just tracks Signs/Intervals-add-on). |
| 20 | drills.html -- reference-book gap-fill against "Help Your Kids with Music" | ✅ Done (2026-09-28, Phase 184) | Sohyun placed a reference book PDF ("Help Your Kids with Music -- A Unique Step-by-Step Visual Guide") in the Piano Butler folder and asked for a chapter-by-chapter gap check against it, skipping its Ch.7 (Instruments and Voices). Existing chapters covered the book's Ch.1-3/5/9 reasonably well. **All three entirely-missing chapters are now built:** Ch.4 Melody (Phase 181, `melody`), Ch.6 Form (Phase 183, `form`), Ch.8 Styles & Genres (Phase 184, `styles` -- scoped to texture and style-family traits; the book's period sub-sections were deliberately skipped since `piano-story`'s `eras` tool already covers them). Remaining lower-priority follow-up, not started: some sub-topics are thinner than the book (relative minor, circle of fifths, modulation/transposition depth, cadences/chord symbols/harmonizing-a-melody depth). |
| 17 | Tap-along timing on a real phone (Rhythm Cards) | Quick -- after Sohyun pushes `7072051` | Especially Game (pixel) mode: the Press Start 2P font could not load in the sandbox test. Also try a `lock=1` student link on a phone. |


| 13 | Fixed: pool filled grades one at a time instead of round-robin | `sightreading-generator/server/excerptPool.js` | Sohyun caught this live: Preliminary was fast right after boot, but switching to Grade 6 right after still meant a full wait. Root cause: the refill loop always picked the FIRST grade (in fixed prelim..grade8 order) still under target, so a grade near the end of that list got zero attention until every grade ahead of it was fully filled to `TARGET_PER_GRADE` (2) -- right after a cold boot that could be 5+ grades × 2 builds before Grade 6 got even one. Now it always picks whichever grade currently has the smallest pool, so every grade reaches its first pooled item before any grade gets a second. |

**Live-verified**: Sohyun pushed (`77880c9`, `da09835`); confirmed redeployed. Switched straight
to Grade 6 (without touching Preliminary first) and it came back in ~3 seconds with full notation
rendered — the exact case Sohyun caught failing before this fix. Round-robin fill confirmed working.

*Removed from this list 2026-09-17 (fifth pass): live-verifying Phase 82's `sight-reading.html` CTA revert and `timeline.html` generic mode (done -- Sohyun pushed all four commits; confirmed live: sight-reading.html's Generate button now opens the generator directly, and timeline.html's new mode-choice screen correctly routes to both the untouched AMEB flow -- grade picker, real piece browse/search, Grade 3 Technical Work Checklist and sample repertoire all confirmed unchanged -- and the new generic performance flow end to end, with no AMEB-specific copy leaking into the generic mode's quiz or checklist). *Removed from this list 2026-09-16 (fourth pass): the "diagnose.html rewrite + practice-challenge.html" decision -- Sohyun said discard it, but checking found nothing to discard: `diagnose.html` is tracked and clean (already committed in a later, real commit chain -- `a6c7277`/`26c3134`/`617818e`), and `practice-challenge.html` doesn't exist in the working tree at all. This pending item had gone stale since whenever those were actually resolved; no action needed. Also removed 2026-09-16 (third pass): live-verifying Phase 80's round-robin pool fix (done -- switching straight to Grade 6 came back in ~3s). Also removed 2026-09-16 (second pass): live-verifying Phase 80's crash fix (done -- confirmed redeployed, a full Generate cycle succeeded end to end with no crash, health check stayed continuously up). Also removed 2026-09-16: setting up a reliable free keep-alive ping (done — Sohyun set up UptimeRobot, 5-min interval, confirmed Up/100%). live-verifying Phase 79's gateway-retry fix (done -- confirmed deployed and a fresh Generate succeeded live). Removed 2026-09-15: Search Console indexing monitoring (was flat, now climbing —
folded into the Revenue-critical table instead of its own pending-work line); pushing this
session's commits (done — confirmed via `git rev-list --left-right --count origin/main...HEAD`
returning `0 0`); the sight-reading "may take a minute" loading message (done, Phase 73); deciding
`butler.html`'s scope (done, Phase 74 — stays private); live-verifying Phase 75/76's sight-reading
speed and loading-page changes (done, confirmed live 2026-09-15 — see Phase 76 #7). Removed 2026-08-17:
`git push` the Phase 67 commit, create the AdSense ad unit + set `PB_AD_SLOT`, and complete AdSense
payment info — all three confirmed done via direct live-site/dashboard checks that session. Teacher
outreach also removed — Sohyun has decided not to send it; see Known issues and the Top Priority
section for the standing note.*

### Known issues

- 🔴 **SECURITY — credential rotation from the 2026-08-14 malware incident is partly done.**
  The machine was clean as of 8/14 (payload deleted, no persistence, verified), but the login
  keychain and browser cookies were exfiltrated. **GitHub personal access token rotated
  2026-08-17**: old `piano-butler` classic token (no expiration, last used within 3 months —
  plausibly the one exposed) deleted, new `piano-butler` classic token generated with the same
  `repo`+`workflow` scopes and a hard 1-year expiration (2027-08-17), done live in Sohyun's own
  authenticated GitHub session via browser automation with her present and approving each step.
  It's still unconfirmed whether the Phase 67 push (`0e9029c`, confirmed live 8/17) happened
  before or after this rotation — low residual risk now that the old token is deleted either way.
  **Still outstanding, all from her phone, not the Mac**: Gmail password (confirm it was actually
  changed, not just signed out) · GitHub account password itself (only the token was rotated, not
  the password) · bank and card · Namecheap · Apple ID · Supabase · AdSense · Anthropic. Also
  worth enabling 2FA on GitHub if not already on, and checking GitHub account security log for
  any unfamiliar sign-ins during the exposure window.
- **Never paste a `curl … | zsh` or `| bash` command from a website**, and Claude must verify that
  any install link is the official repository before citing it. That is what caused the incident:
  a Sources list in Claude's own reply pointed at `audiveris.com`, an impersonation of the real
  project at `github.com/Audiveris/audiveris`.
- **Teacher outreach — closed, not a gap.** Sohyun decided 2026-08-17 not to send
  `outreach-messages.md`. Do not flag this again.
- **The AdSense dashboard flag is stale relative to the live site, not the other way around.**
  As of 2026-08-17 the dashboard still shows 주의 필요 / Ads.txt 찾을 수 없음, last refreshed
  2026-08-08 — but the actual fix (ad units + homepage content) has been live since sometime
  between 8/13 and 8/17, confirmed by direct inspection. The dashboard just hasn't re-crawled yet.
  Don't request re-review until it does.
- **Recurring pattern: uncommitted work sitting in the working tree between sessions.** Hit again at Phase 67 (`diagnose.html`, `practice-challenge.html`), as in Phase 58 and Phase 64. Worth running `git status` at the start of every session.
- **Recurring pattern: authoritative `.js` updated, inline HTML copy not.** Phase 12 (`DATA_G5_1`), Phase 54 (`DATA_G6_COMP`), and now Phase 67 (all 9 ABRSM pages rendering 42–47 of 48 pieces). Any page that embeds data inline needs an explicit parity check, not an assumption.
- drills.html Korean mode: a drill question that was already on screen when 한국어 is tapped stays English until the next question (choices are generated per question). By design, low impact.
- `butler.html`: built, tested, and pushed. **Decided 2026-09-15: stays private** — not linked or promoted as a public feature.
- Diploma pages (LRSM/FRSM/ATCL/LTCL/FTCL) intentionally have no exam-requirement content (performance duration, own-choice rules, etc.) — this is a deliberate scope decision (2026-08-03), not a gap to fill. Piano Butler is a search tool, not a syllabus-content site.
- Supabase free tier auto-pauses after 7 days of inactivity — mitigated by the `supabase-keepalive.yml` GitHub Action (runs Mon & Thu).
- Git sandbox: `rm -f .git/index.lock .git/HEAD.lock` may fail with "Operation not permitted" — call `allow_cowork_file_delete` on the lock file path first, then retry. The actual `git push` must always be run by Sohyun from her own Terminal (the sandbox has no push credentials).
- Scheduled task `piano-butler-monday-check` now runs **daily at 9am** (upgraded 2026-08-03 from weekly) with a rewritten prompt containing the current baseline — despite the taskId still saying "monday-check," it is no longer weekly-only.
