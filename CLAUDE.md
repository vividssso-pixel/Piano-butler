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
├── find-a-teacher.html               ← student → teacher matching request form (hidden from nav)
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
Build next in this order: ~~Reading the Staff~~ (Phase 101), Dynamics & Articulation, Signs, Intervals, Chords.
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

## Current Status (as of 2026-08-17, traffic/indexing/AdSense numbers refreshed 2026-09-15 — see Phase 72)

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
| Exam Check-Up service (`find-a-teacher.html`) | Form + pricing UI live, payment not wired up | **Sohyun action required.** Needs a real Stripe Payment Link pasted into the `STRIPE_PAYMENT_LINK` constant. |
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
| 1 | Revisit: should `sight-reading.html` auto-redirect to the generator? | Medium — Sohyun | 2026-09-17: built and committed an auto-redirect version (Sohyun had asked for it), then she said she didn't like the result and asked to shelve it for now and revise later -- reverted locally (`81b724d`/`f4551b9`), never pushed, so the live site was never affected. `sight-reading.html` is back to its original static SEO landing page. Revisit when she's ready to say what she wants it to do/look like instead. |
| 2 | Decide what `AGENTS.md` is for | Medium — Sohyun | Found 2026-09-15: an untracked, stale (138-line-diff) mirror of this file, apparently read by a different AI coding tool (naming convention + one "Codex API" substitution suggest OpenAI Codex or similar). Decide: keep it and have future sessions maintain both in sync, or delete it if it's a stray leftover from a one-off experiment. |
| 3 | Create the Stripe Payment Link for Exam Check-Up | High — Sohyun | $25 AUD one-time product → paste the link into `STRIPE_PAYMENT_LINK` in `find-a-teacher.html`. |
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
| 16 | drills.html chapters built (Phases 94-97) | Done -- review | Sohyun to try Note Names (letter levels), Notes & Rests, Rhythm Cards, Key Signatures, Scales, Tempo Race and flag anything off. |
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
- `butler.html`: built, tested, and pushed. **Decided 2026-09-15: stays private** — not linked or promoted as a public feature.
- Diploma pages (LRSM/FRSM/ATCL/LTCL/FTCL) intentionally have no exam-requirement content (performance duration, own-choice rules, etc.) — this is a deliberate scope decision (2026-08-03), not a gap to fill. Piano Butler is a search tool, not a syllabus-content site.
- Supabase free tier auto-pauses after 7 days of inactivity — mitigated by the `supabase-keepalive.yml` GitHub Action (runs Mon & Thu).
- Git sandbox: `rm -f .git/index.lock .git/HEAD.lock` may fail with "Operation not permitted" — call `allow_cowork_file_delete` on the lock file path first, then retry. The actual `git push` must always be run by Sohyun from her own Terminal (the sandbox has no push credentials).
- Scheduled task `piano-butler-monday-check` now runs **daily at 9am** (upgraded 2026-08-03 from weekly) with a rewritten prompt containing the current baseline — despite the taskId still saying "monday-check," it is no longer weekly-only.
