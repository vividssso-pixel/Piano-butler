# Piano Butler AI — Project Instructions

## Role
You are the **"Piano Butler AI,"** a world-class Orchestrator and Creative Strategist for the *Piano Butler* project. You are an expert in:
- The **2026 AMEB Piano Syllabus** (Comprehensive Piano & Piano for Leisure)
- Piano pedagogy and music theory
- UI/UX design for music education applications

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
│   └── G8/
│       ├── data_abrsm_g8.js         ← ABRSM G8 (45 pieces: A:16, B:15, C:14)
│       └── piano-repertoire_abrsm_g8.html
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

## Build Status — Last updated 2026-05-02

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

### Known Issues / Watch Points (as of 2026-05-02)
- `from_week` column: run `NOTIFY pgrst, 'reload schema';` in Supabase SQL if saves fail silently
- Drag cross-column: uses `grid.scrollWidth` (not `rect.width`) for `totalColW` — if layout changes, re-check `hitTest`
- `isExamStudent()` reads `s.examDate` — if examDate not loaded from `extra`, exam section won't open in edit modal

---

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

### Build Status — Last updated 2026-05-05 (evening)

| # | Feature | Status |
|---|---------|--------|
| 1–32 | All previously completed features | ✅ Done (see Phases 1–11) |
| 33 | For You recommendation engine | ✅ Done (Phase 12) |
| 34 | Composer Wikipedia links on index.html | ✅ Done (Phase 12) |
| 35 | 🎓 Diploma filter bug fix | ✅ Done (Phase 12) |
| 36 | G5 corpus bug fix (168 missing pieces) | ✅ Done (Phase 12) |

### Pending Work (priority order for next session)

| # | Task | Priority | Notes |
|---|------|----------|-------|
| 1 | payments.html — lesson fee management | High | Per-student fee, invoice PDF, paid/unpaid toggle. For Teacher Dashboard only. |
| 2 | Google Search Console — submit sitemap | Quick win | Go to search.google.com/search-console → add sitemap.xml URL → verify |
| 3 | Ad integration | Medium | Google AdSense application, or direct piano brand deals. Requires traffic first. |
| 4 | Design unification | Medium | All grade pages have slightly different styling. Deferred — not blocking. |
| 5 | ABRSM Diploma | Low | Needs PDF from abrsm.org (ARSM / DipABRSM / LRSM / FRSM). User to download first. |

### Known Issues (as of 2026-05-05)
- None active. All bugs from today's audit session resolved and deployed.

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

### Known Issues (as of 2026-05-06 morning)
- Logo button click fix deployed (commit 9277762) — awaiting user confirmation
- CertP grid layout fixed to `grid-cols-3` — awaiting user confirmation after push
- **Pending user action:** run `git push origin main` from Terminal to deploy Phase 14 fixes

---

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

### Build Status — Last updated 2026-05-08

| # | Feature | Status |
|---|---------|--------|
| 1–35 | All previously completed features | ✅ Done (Phases 1–19) |
| 36 | Local-first list system (AddToListModal + MyListsPanel) | ✅ Done (Phase 21) |
| 37 | Google-style minimal homepage | ✅ Done (Phase 22) |

### Pending Work (priority order for next session)

| # | Task | Priority | Notes |
|---|------|----------|-------|
| 1 | payments.html — lesson fee management | High | Per-student fee, invoice PDF, paid/unpaid toggle. Teacher Dashboard only. |
| 2 | Google Search Console — submit sitemap | Quick win | search.google.com/search-console → add sitemap.xml URL |
| 3 | Ad integration | Medium | Google AdSense or direct piano brand deals. Requires traffic first. |
| 4 | Design unification | Medium | All grade pages have slightly different styling. Deferred. |
| 5 | ABRSM Diploma — ARSM / DipABRSM | Low | PDFs not yet available. User to download from abrsm.org when ready. |

### Known Issues (as of 2026-05-08)
- None active.

---

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

### Known Issues (as of 2026-05-10)
- None active. All design changes deployed.

---

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

### Known Issues (as of 2026-05-10 evening)
- None active. Search is responsive.

---

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

### Build Status — Last updated 2026-05-13 (evening)

| # | Feature | Status |
|---|---------|--------|
| 1–40 | All previously completed features (Phases 1–26) | ✅ Done |
| 41 | Multi-token AND search + focus field search | ✅ Done (Phase 27) |
| 42 | Syllabus badge on piece cards | ✅ Done (Phase 27) |
| 43 | Autocomplete era/nationality/focus hints | ✅ Done (Phase 27) |
| 44 | AMEB data audit — ERA/FOCUS/NAT corrections | ✅ Done (Phase 27) |

### Pending Work (priority order for next session)

| # | Task | Priority | Notes |
|---|------|----------|-------|
| 1 | G8 Leisure BEETHOVEN Andante duplicate | Quick fix | Check Piano for Leisure G8 PDF — is Andante in both S4 and S1? If not, remove one. |
| 2 | ABRSM data audit | High | Run same automated audit (ERA/FOCUS/NAT/duplicate) across all 9 ABRSM grade files. |
| 3 | Trinity data audit | High | Run same automated audit across all 9 Trinity grade files. |
| 4 | C — sitewide UX review | High | Open live site, use it as a real teacher would, note friction points. |
| 5 | Teaching Lists upgrade | High | Ordered sequence, per-piece teacher notes, grade range tag, improved share view. |
| 6 | Google Search Console — submit sitemap | Quick win | search.google.com/search-console → add sitemap.xml URL → verify. |
| 7 | Ad integration | Medium | Google AdSense or direct piano brand deals. Requires traffic first. |
| 8 | ABRSM Diploma — ARSM / DipABRSM | Low | PDFs not yet available. |

### Known Issues (as of 2026-05-13 evening)
- ⚠️ G8 Leisure: BEETHOVEN Andante appears in both S4 (index 1) and S1 (index 24) — pending PDF verification before removal.

---

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

### Build Status — Last updated 2026-05-13 (Phase 29)

| # | Feature | Status |
|---|---------|--------|
| 1–44 | All previously completed features (Phases 1–27) | ✅ Done |
| 45 | Trinity Diploma — ATCL repertoire | ✅ Done (Phase 28) |
| 46 | Trinity Diploma — LTCL repertoire | ✅ Done (Phase 28) |
| 47 | Trinity Diploma — FTCL repertoire | ✅ Done (Phase 28) |
| 48 | index.html Trinity Diploma integration | ✅ Done (Phase 28) |
| 49 | Repertoire Recommender — recommend.html | ✅ Done (Phase 29) |
| 50 | Recommender — YouTube in-page modal | ✅ Done (Phase 29) |
| 51 | Recommender — Free discovery mode (no syllabus/grade) | ✅ Done (Phase 29) |
| 52 | index.html — 🎹 Recommend button in header | ✅ Done (Phase 29) |

---

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

### Pending Work (priority order for next session)

| # | Task | Priority | Notes |
|---|------|----------|-------|
| 1 | G8 Leisure BEETHOVEN Andante duplicate | Quick fix | Check Piano for Leisure G8 PDF — is Andante in both S4 and S1? If not, remove one. |
| 2 | Recommender UX polish | High | Test with real students. Possible improvements: show which syllabus/grade each result is from, add "exclude this piece" button, show more results with scroll. |
| 3 | ABRSM data audit | High | Run automated audit (ERA/FOCUS/NAT/duplicate) across all 9 ABRSM grade files. |
| 4 | Trinity data audit | High | Run same audit across all 9 Trinity grade files + 3 diploma files. |
| 5 | Teaching Lists upgrade | High | Ordered sequence, per-piece teacher notes, grade range tag, improved share view. |
| 6 | Google Search Console — submit sitemap | Quick win | search.google.com/search-console → add sitemap.xml URL → verify. |
| 7 | Ad integration | Medium | Google AdSense or direct piano brand deals. Requires traffic first. |
| 8 | payments.html — teacher fee management | Low | Per-student fee, invoice PDF, paid/unpaid toggle. |

### Known Issues (as of 2026-05-13 Phase 29)
- ⚠️ G8 Leisure: BEETHOVEN Andante appears in both S4 (index 1) and S1 (index 24) — pending PDF verification before removal.
- Trinity Diploma data parsed from PDF text extraction — some multi-line title entries may have minor formatting differences. Spot-check against source PDF if needed.
- recommend.html Free discovery: returns pieces from all syllabuses mixed — could optionally add a syllabus filter in future.

---

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

### Build Status — Last updated 2026-05-14

| # | Feature | Status |
|---|---------|--------|
| 1–52 | All previously completed features (Phases 1–29) | ✅ Done |
| 53 | Piano Diagnosis MVP — diagnose.html | ✅ Done (Phase 30) |
| 54 | 🔬 Diagnose button in index.html nav | ✅ Done (Phase 30) |

### Pending Work (priority order for next session)

| # | Task | Priority | Notes |
|---|------|----------|-------|
| 1 | Stripe + jsPDF for $4 full report | High | Stripe Checkout (hosted, no backend) + jsPDF or browser print-to-PDF. Unlock full PDF on payment. |
| 2 | connect.html — teacher/course matching | High | Shows matched teachers + courses based on diagnosis result stored in localStorage. Start with 3–5 teachers Sohyun knows. |
| 3 | G8 Leisure BEETHOVEN Andante duplicate | Quick fix | Check Piano for Leisure G8 PDF — is Andante in both S4 and S1? If not, remove one. |
| 4 | ABRSM data audit | Medium | ERA/FOCUS/NAT/duplicate check across all 9 ABRSM grade files. |
| 5 | Trinity data audit | Medium | Same audit across all 9 Trinity grade files + 3 diploma files. |
| 6 | Teaching Lists upgrade | Medium | Ordered sequence, per-piece teacher notes, grade range tag, improved share view. |
| 7 | Google Search Console — submit sitemap | Quick win | search.google.com/search-console → add sitemap.xml URL → verify. |
| 8 | Ad integration | Low | Google AdSense or direct piano brand deals. Requires traffic first. |

### Known Issues (as of 2026-05-14)
- ⚠️ G8 Leisure: BEETHOVEN Andante appears in both S4 (index 1) and S1 (index 24) — pending PDF verification before removal.
- Trinity Diploma data: some multi-line title entries may have minor formatting differences — spot-check against source PDF if needed.
- diagnose.html $4 report CTA: currently a coming-soon modal with waitlist email. Stripe integration pending.

---

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

### Build Status — Last updated 2026-05-15 (Phase 34)

| # | Feature | Status |
|---|---------|--------|
| 1–57 | All previously completed features (Phases 1–31) | ✅ Done |
| 58 | Composer name normalisation — all 42 data files | ✅ Done (Phase 33) |
| 59 | Data quality audit — ERA/FOCUS/NAT/duplicates | ✅ Done (Phase 33) |
| 60 | COMPOSER_LINKS canonical keys — 16 HTML files | ✅ Done (Phase 33) |
| 61 | diagnose.html — gapFactor bug fix + corpus fallback | ✅ Done (Phase 34) |
| 62 | diagnose.html — jsPDF in-browser report generator | ✅ Done (Phase 34) |
| 63 | diagnose.html — FullReportModal with PDF download + Gumroad link | ✅ Done (Phase 34) |

### Pending Work (priority order for next session)

| # | Task | Priority | Notes |
|---|------|----------|-------|
| 1 | Gumroad product setup | First thing | Create product at gumroad.com, upload sample PDF, replace `GUMROAD_URL` in diagnose.html, push to main. |
| 2 | connect.html — add real teacher info | High | Replace placeholder with real photo, real booking link, real price. |
| 3 | Google Search Console — submit sitemap | Quick win | search.google.com/search-console → add sitemap.xml URL → verify. |
| 4 | Ad integration | Low | After traffic grows. |

### Known Issues (as of 2026-05-15)
- `GUMROAD_URL` in diagnose.html is a placeholder — must be replaced with real Gumroad link before promoting publicly.
- jsPDF radar chart uses `doc.moveTo/lineTo` which may not be available in all jsPDF 2.5.1 builds — test in browser, fallback to simple score text if lines don't render.
- connect.html teacher cards: placeholder data only.
- connect.html teacher cards: placeholder data only. Real teacher info needed before promoting publicly.

---

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

### Build Status — Last updated 2026-05-18

| # | Feature | Status |
|---|---------|--------|
| 1–67 | All previously completed features | ✅ Done |
| 68 | diagnose.html — returner domain-based redesign | ✅ Done (Phase 36) |
| 69 | diagnose.html — beginner preference flow | ✅ Done (Phase 36) |

### Pending Work (next session)

| # | Task | Priority |
|---|------|----------|
| 1 | connect.html dark theme | Medium — still light theme |
| 2 | recommend.html dark theme | Medium — still light theme |
| 3 | YouTube API key referrer restriction | High — set in Google Cloud Console |
| 4 | Google Search Console — submit sitemap | Quick win |
| 5 | Ad integration | Low — after traffic |

---

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

### Build Status — Last updated 2026-05-18

| # | Feature | Status |
|---|---------|--------|
| 1–69 | All previously completed features (Phases 1–36) | ✅ Done |
| 70 | List/Group filter tabs in search results | ✅ Done (Phase 37) |
| 71 | admin-search.html — full-featured admin search | ✅ Done (Phase 37) |
| 72 | index.html — search-first homepage, dark theme, tool cards | ✅ Done (Phase 37) |
| 73 | Dark theme — connect.html + recommend.html + diagnose.html | ✅ Done (Phase 37) |
| 74 | recommend.html — simplified 4-step flow | ✅ Done (Phase 38) |
| 75 | recommend.html — Safari compatibility (color-mix, optional chaining, ErrorBoundary) | ✅ Done (Phase 38) |

### Pending Work (priority order for next session)

| # | Task | Priority | Notes |
|---|------|----------|-------|
| 1 | YouTube API key — referrer restriction | High | Set allowed referrers to `thepianobutler.com/*` in Google Cloud Console → Credentials → API key restrictions. Currently unrestricted. |
| 2 | Gumroad product setup | High | Create product at gumroad.com → upload sample PDF from diagnose.html → replace `GUMROAD_URL` constant in diagnose.html → push to main. |
| 3 | connect.html — real teacher info | High | Replace placeholder teacher cards with real photo, booking link, and price. |
| 4 | Google Search Console — submit sitemap | Quick win | search.google.com/search-console → add sitemap.xml URL → verify. |
| 5 | Sitewide UX review | Medium | Open live site at thepianobutler.com, use as a real teacher/student. Note friction. |
| 6 | Ad integration | Low | Google AdSense application or direct piano brand deals. Requires traffic first. |
| 7 | ABRSM Diploma — ARSM / DipABRSM | Low | PDFs not yet available from abrsm.org. |

### Known Issues (as of 2026-05-18)
- `GUMROAD_URL` in diagnose.html is a placeholder — must be replaced with real Gumroad link before promoting publicly.
- connect.html: placeholder teacher cards — real info needed before public promotion.
- YouTube API key (`[REDACTED-OLD]`) is unrestricted — add referrer restriction in Google Cloud Console.
- jsPDF radar chart in diagnose.html: uses `doc.moveTo/lineTo` — verify renders correctly in browser before selling reports.

---

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

### Build Status — Last updated 2026-05-21

| # | Feature | Status |
|---|---------|--------|
| 1–75 | All previously completed features (Phases 1–39) | ✅ Done |
| 76 | YouTube API key referrer restriction verified | ✅ Done (Phase 40) |
| 77 | ABRSM data audit + 31 focus fixes | ✅ Done (Phase 40) |
| 78 | Trinity data audit — all clean | ✅ Done (Phase 40) |
| 79 | List A/B/C/D badge on search results | ✅ Done (Phase 40) |
| 80 | Compact piece cards + 1-column layout | ✅ Done (Phase 40) |
| 81 | Sidebar filter restored | ✅ Done (Phase 40) |
| 82 | Safari blank screen fix — inset:0 removed sitewide | ✅ Done (Phase 41) |
| 83 | Supabase script removed from index.html | ✅ Done (Phase 41) |

### Pending Work (priority order for next session)

| # | Task | Priority | Notes |
|---|------|----------|-------|
| 1 | Google Search Console — submit sitemap | Quick win | search.google.com/search-console → add sitemap.xml URL → verify |
| 2 | Sitewide UX review — continue | High | index.html search UX, recommend.html, diagnose.html flows |
| 3 | connect.html — real teacher info | Medium | Replace placeholder cards with real photo, booking link, price |
| 4 | Gumroad product setup | Medium | Booked for after traffic grows — not urgent |
| 5 | Ad integration | Low | After traffic grows |
| 6 | ABRSM Diploma — ARSM / DipABRSM | Low | PDFs not yet available |

### Known Issues (as of 2026-05-22)
- `GUMROAD_URL` in diagnose.html is a placeholder — not urgent until traffic grows.
- connect.html: placeholder teacher cards.
- jsPDF radar chart: verify renders correctly before promoting $4 report.
- teacher-dashboard.html still has `inset:0` — not public-facing, low priority.

---

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

### Build Status — Last updated 2026-05-22

| # | Feature | Status |
|---|---------|--------|
| 1–83 | All previously completed features (Phases 1–41) | ✅ Done |
| 84 | Safari blank screen — CDN migration to cdnjs (pinned versions) | ✅ Done (Phase 42) |
| 85 | Safari blank screen — manual Babel compile trigger | ✅ Done (Phase 42) |
| 86 | Curly quote Babel compile error fix | ✅ Done (Phase 42) |

### Pending Work (priority order for next session)

| # | Task | Priority | Notes |
|---|------|----------|-------|
| 1 | Verify Safari fix on device | Immediate | Open thepianobutler.com in Safari private tab and confirm app renders |
| 2 | Google Search Console — submit sitemap | Quick win | search.google.com/search-console → add sitemap.xml URL → verify |
| 3 | Sitewide UX review | High | index.html search UX, recommend.html, diagnose.html flows |
| 4 | connect.html — real teacher info | Medium | Replace placeholder cards with real photo, booking link, price |
| 5 | Gumroad product setup | Medium | After traffic grows |
| 6 | Ad integration | Low | After traffic grows |
| 7 | ABRSM Diploma — ARSM / DipABRSM | Low | PDFs not yet available |

---

### Phase 39 Updates (2026-05-18 — diagnose.html UX fixes + security)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Landing cards — directly clickable | `diagnose.html` | 🌱 / 🔄 preview cards replaced with proper `<button>` elements. Click goes directly to correct flow — no intermediate background question. 🌱 → `beginner_quiz` immediately. 🔄 → `quiz` at phase 1 (Purpose), skipping phase 0. "Start →" single button removed. |
| 2 | ShareResultButton component | `diagnose.html` | New component added. "🔗 Share my result" button appears at bottom of both result screens (returner + beginner). Encodes result to base64 URL param (`?result=…`). Uses `navigator.share` on mobile, clipboard copy on desktop. Shows "✓ Link copied!" confirmation for 2.5s. |
| 3 | SharedResultView component | `diagnose.html` | Read-only result page rendered when `?result=` URL param detected on load. Shows returner result (levelLabel + overallPct + weak areas) or beginner profile (profile name + genre + timeline + teacherFormat). CTAs: "Take my own diagnosis" + "Find a teacher". No login required to view. |
| 4 | YouTube API key rotated — security | All 21 HTML files | Old key `[REDACTED-OLD]` exposed in GitHub history (GitGuardian alert). New key `[REDACTED]` applied across all 21 HTML files. Old key deleted from Google Cloud Console. New key restricted to `thepianobutler.com/*` + `www.thepianobutler.com/*` referrers. |

### Build Status — Last updated 2026-05-18

| # | Feature | Status |
|---|---------|--------|
| 1–75 | All previously completed features (Phases 1–38) | ✅ Done |
| 76 | diagnose.html — clickable landing cards (direct flow entry) | ✅ Done (Phase 39) |
| 77 | diagnose.html — share result link (URL-encoded, no login) | ✅ Done (Phase 39) |
| 78 | YouTube API key rotation — all 21 HTML files | ✅ Done (Phase 39) |

### Pending Work (priority order for next session)

| # | Task | Priority | Notes |
|---|------|----------|-------|
| 1 | Gumroad product setup | High | Create product at gumroad.com → complete diagnose quiz → download PDF → upload as product → replace `GUMROAD_URL` in diagnose.html → push to main. |
| 2 | connect.html — real teacher info | High | Replace placeholder teacher cards with real photo, booking link, and price. |
| 3 | Google Search Console — submit sitemap | Quick win | search.google.com/search-console → add sitemap.xml URL → verify. |
| 4 | Sitewide UX review | Medium | Open thepianobutler.com as a real teacher/student. Note friction. |
| 5 | Ad integration | Low | Google AdSense or direct piano brand deals. Requires traffic first. |
| 6 | ABRSM Diploma — ARSM / DipABRSM | Low | PDFs not yet available from abrsm.org. |

### Known Issues (as of 2026-05-18)
- `GUMROAD_URL` in diagnose.html is a placeholder — must be replaced with real Gumroad link before promoting publicly.
- connect.html: placeholder teacher cards — real info needed before public promotion.
- jsPDF radar chart in diagnose.html: uses `doc.moveTo/lineTo` — verify renders correctly in browser before selling reports.

---

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

### Build Status — Last updated 2026-05-25

| # | Feature | Status |
|---|---------|--------|
| 1–86 | All previously completed features (Phases 1–42) | ✅ Done |
| 87 | diagnose.html — 8-question single flow, clear results, cdnjs CDN | ✅ Done (Phase 43) |
| 88 | recommend.html — 2-step wizard, actionable result cards, cdnjs CDN | ✅ Done (Phase 43) |

### Pending Work (priority order for next session)

| # | Task | Priority | Notes |
|---|------|----------|-------|
| 1 | Push to main (git push origin main) | Immediate | Deploy Phase 43 changes live |
| 2 | Google Search Console — submit sitemap | Quick win | search.google.com/search-console → add sitemap.xml URL → verify |
| 3 | connect.html — real teacher info | Medium | Replace placeholder cards with real photo, booking link, price |
| 4 | Sitewide UX review | Medium | Open thepianobutler.com, use as real teacher/student, note friction |
| 5 | Ad integration | Low | Google AdSense or direct piano brand deals — after traffic grows |
| 6 | ABRSM Diploma — ARSM / DipABRSM | Low | PDFs not yet available from abrsm.org |

### Known Issues (as of 2026-05-25)
- connect.html: placeholder teacher cards — real info needed before public promotion.
- Gumroad: no longer used in diagnose.html (jsPDF/Gumroad flow removed in Phase 43 simplification).

---

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

### Build Status — Last updated 2026-05-25 (Phase 44)

| # | Feature | Status |
|---|---------|--------|
| 1–88 | All previously completed features (Phases 1–43) | ✅ Done |
| 89 | Homepage — two entry cards (Search vs Diagnose) | ✅ Done (Phase 44) |
| 90 | Search card → direct full-screen transition with autoFocus | ✅ Done (Phase 44) |
| 91 | diagnose.html — Tailwind removed, black text fixed | ✅ Done (Phase 44) |
| 92 | diagnose.html — SVG radar chart (4-axis polygon) | ✅ Done (Phase 44) |

### Pending Work (priority order for next session)

| # | Task | Priority | Notes |
|---|------|----------|-------|
| 1 | Sitewide UX review | High | Open thepianobutler.com, use as real teacher/student, note friction points |
| 2 | Google Search Console — submit sitemap | Quick win | search.google.com/search-console → add sitemap.xml URL → verify |
| 3 | connect.html — real teacher info | Medium | Replace placeholder cards with real photo, booking link, price |
| 4 | Ad integration | Low | Google AdSense or direct piano brand deals — after traffic grows |
| 5 | ABRSM Diploma — ARSM / DipABRSM | Low | PDFs not yet available from abrsm.org |

### Known Issues (as of 2026-05-25 Phase 44)
- connect.html: placeholder teacher cards — real info needed before public promotion.
- Git sandbox HEAD.lock: sandbox cannot write HEAD.lock — user must run `rm HEAD.lock && git commit && git push` in Terminal when commits fail.

---

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

### Build Status — Last updated 2026-05-27

| # | Feature | Status |
|---|---------|--------|
| 1–92 | All previously completed features (Phases 1–44) | ✅ Done |
| 93 | Random Pick — Listen + Score buttons | ✅ Done (Phase 45) |
| 94 | Random Pick — YouTube opens above modal, stays open after close | ✅ Done (Phase 45) |
| 95 | Footer independence disclaimer | ✅ Done (Phase 45) |
| 96 | Admin password removed from public repo | ✅ Done (Phase 45) |
| 97 | Site title — Exam & Repertoire Search | ✅ Done (Phase 45) |

### Pending Work (priority order for next session)

| # | Task | Priority | Notes |
|---|------|----------|-------|
| 1 | Google Search Console — submit sitemap | First | search.google.com/search-console → add thepianobutler.com → submit sitemap.xml |
| 2 | SheetMusicPlus affiliate | High | Once approved → replace Score button Google search URLs with affiliate links |
| 3 | recommend.html | Medium | Still modified/uncommitted — review and either clean up or discard changes |
| 4 | Ad integration | Low | Google AdSense — after traffic grows |
| 5 | ABRSM Diploma — ARSM / DipABRSM | Low | PDFs not yet available |

### Known Issues (as of 2026-05-28)
- connect.html: placeholder teacher cards — not promoted publicly.
- Git sandbox HEAD.lock: user must run `rm .git/HEAD.lock` in Terminal if git commit fails.

---

### Phase 48 Updates (2026-06-01 — SEO: noscript fallback + keywords)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Search Console status check | — | 2 pages indexed, 37 not indexed (35 "Discovered – currently not indexed", 1 "Crawled – currently not indexed", 1 canonical). All normal 4 days after sitemap submission. ABRSM G5 identified as the crawled-but-not-indexed page — root cause: React/JS rendering invisible to Google crawler. |
| 2 | `<noscript>` static HTML fallback — all 35 grade pages | All `piano-repertoire_*.html` files | Python + Node script extracted piece data (inline or from companion `data_*.js`) and injected a full static piece list inside `<noscript>` tags before `</body>`. Google crawler now sees all pieces without executing JavaScript. Commit `fb46e91`. |
| 3 | SEO keywords — AMusA, LMusA | `AMusA/piano-repertoire_amusa.html`, `LMusA/piano-repertoire_lmusa.html` | `<meta name="keywords">` tag was missing. Added 5 grade-specific keywords each. Commit `c1e684c`. |
| 4 | SEO keywords — Trinity Initial–G8 | All 9 `Trinity/*/piano-repertoire_trinity_*.html` files | Keywords expanded from 3 generic → 5 grade-specific (e.g. "Trinity College London piano Grade 5", "Trinity piano Grade 5 2023", "piano exam pieces grade 5", etc.). Commit `c1e684c`. |

### Build Status — Last updated 2026-06-01 (Phase 48)

| # | Feature | Status |
|---|---------|--------|
| 1–102 | All previously completed features (Phases 1–47) | ✅ Done |
| 103 | `<noscript>` static HTML fallback — all 35 grade pages | ✅ Done (Phase 48) |
| 104 | SEO keywords — AMusA, LMusA added | ✅ Done (Phase 48) |
| 105 | SEO keywords — Trinity Initial–G8 expanded | ✅ Done (Phase 48) |

### Pending Work (priority order for next session)

| # | Task | Priority | Notes |
|---|------|----------|-------|
| 1 | Sitewide UX review | High | Open thepianobutler.com as real teacher/student, note friction points |
| 2 | Search Console — re-check in 1 week | Quick check | Verify "Discovered" pages moving to indexed. URL Inspection → Request Indexing on ABRSM G5. |
| 3 | Affiliate signup | Deferred | Trigger: Search Console clicks ≥ 500 |
| 4 | Login revival | Deferred | Trigger: Search Console visitors ≥ 1,000 |
| 5 | connect.html — real teacher info | Deferred | When Sohyun ready to take referrals |
| 6 | ABRSM Diploma — ARSM / DipABRSM | Low | PDFs not yet available |

### Known Issues (as of 2026-06-01)
- connect.html: placeholder teacher cards — not promoted publicly.
- Git sandbox HEAD.lock: user must run `rm .git/HEAD.lock` in Terminal if git commit fails.

---

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

### Build Status — Last updated 2026-06-08

| # | Feature | Status |
|---|---------|--------|
| 1–109 | All previously completed features (Phases 1–49) | ✅ Done |
| 110 | Mobile UX — responsive font/padding/iframe fixes | ✅ Done (Phase 50) |
| 111 | Mobile grade filter in filter strip | ✅ Done (Phase 50) |
| 112 | `?q=` URL param — cross-page search links working | ✅ Done (Phase 50) |
| 113 | Contact button style upgrade | ✅ Done (Phase 50) |
| 114 | Random Pick Trinity + Enter key autocomplete fix | ✅ Done (Phase 50) |

### Pending Work (priority order for next session)

| # | Task | Priority | Notes |
|---|------|----------|-------|
| 1 | Search Console — re-check indexing | Quick check (Jun 13+) | Verify "Discovered" pages moving to indexed. ABRSM G5 validation in progress. |
| 2 | Affiliate signup | Deferred | Trigger: Search Console clicks ≥ 500 |
| 3 | Login revival | Deferred | Trigger: Search Console visitors ≥ 1,000 |
| 4 | connect.html — real teacher info | Deferred | When Sohyun ready to take referrals |
| 5 | ABRSM Diploma — ARSM / DipABRSM | Low | PDFs not yet available |

### Known Issues (as of 2026-06-08)
- connect.html: placeholder teacher cards — not promoted publicly.
- Supabase free tier auto-pauses after 7 days inactivity — restore manually from dashboard as needed.
- Git sandbox HEAD.lock: run `rm .git/HEAD.lock` + `rm .git/index.lock` in Terminal if git commit fails.

---

### Phase 51 Updates (2026-06-09 — Search Console audit + AdSense setup)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Search Console indexing audit | — | Checked URL Inspection for key pages. index.html ✅, G5 ✅, G3 ✅, G1 ✅, ABRSM G5 ✅ — all already indexed. Trinity G5 was "Discovered – not indexed" → Request Indexing submitted. Trinity G1, G8 already indexed. |
| 2 | Google AdSense account created | — | New AdSense account created with vividssso@gmail.com. Site: thepianobutler.com. Country: Australia. Payment profile: Clara Sohyun Park, 79 Burwood Road, Concord NSW 2137. |
| 3 | AdSense script added to index.html | `index.html` | `<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6523454944716812" crossorigin="anonymous"></script>` added to `<head>`. Commit `86a3287`. |
| 4 | AdSense site verified | Google AdSense | Site ownership confirmed. "사이트가 확인되었습니다" ✅. Google review in progress — approval typically takes days to 2 weeks. |

### Build Status — Last updated 2026-06-09

| # | Feature | Status |
|---|---------|--------|
| 1–114 | All previously completed features (Phases 1–50) | ✅ Done |
| 115 | Google AdSense — account created + script added + site verified | ✅ Done (Phase 51) |
| 116 | Search Console — Trinity G5 Request Indexing submitted | ✅ Done (Phase 51) |

### Pending Work (priority order for next session)

| # | Task | Priority | Notes |
|---|------|----------|-------|
| 1 | AdSense approval check | Quick check (Jun 13+) | Check AdSense dashboard for approval status. Once approved, ads go live automatically. |
| 2 | Search Console — re-check indexing | Quick check (Jun 13+) | Verify remaining "Discovered" pages moving to indexed. |
| 3 | Community sharing for traffic | Medium | Share thepianobutler.com in piano teacher Facebook groups, Reddit r/piano, r/pianolearning. Fast way to get initial traffic. |
| 4 | Affiliate signup (Sheet Music Plus) | Deferred | Trigger: Search Console clicks ≥ 500. Try again — previous attempt failed. |
| 5 | Login revival | Deferred | Trigger: Search Console visitors ≥ 1,000 |
| 6 | connect.html — real teacher info | Deferred | When Sohyun ready to take referrals |
| 7 | ABRSM Diploma — ARSM / DipABRSM | Low | PDFs not yet available |

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

### Build Status — Last updated 2026-06-10

| # | Feature | Status |
|---|---------|--------|
| 1–115 | All previously completed features (Phases 1–51) | ✅ Done |
| 116 | index.html noscript static fallback + Schema.org | ✅ Done (Phase 52) |
| 117 | Recommender syllabus filter (3-step) | ✅ Done (Phase 52) |
| 118 | Random Pick syllabus filter | ✅ Done (Phase 52) |
| 119 | Recommend result cards full details | ✅ Done (Phase 52) |
| 120 | Prelim → Preliminary user-facing labels | ✅ Done (Phase 52) |

### Phase 53 Updates (2026-06-10 — strategy session)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Traffic strategy research | — | Researched promotion channels: MTA NSW/VIC/QLD/SA/WA (email), Piano World Teachers Forum, ABRSM Teachers Forum, TopMusic.co. Decision: defer active promotion — SEO organic growth preferred. |
| 2 | Passive income strategy confirmed | — | Priority order: (1) AdSense auto-approval → (2) Sheet Music Plus affiliate at 500 clicks → (3) Gumroad PDF at 1,000 visitors. No active promotion for now — waiting for SEO to compound. |

### Pending Work (priority order for next session)

| # | Task | Priority | Notes |
|---|------|----------|-------|
| 1 | Search Console — re-check indexing (Jun 17+) | Quick check | Verify indexed pages increasing from 2. Request Indexing on index.html if not yet done. |
| 2 | AdSense approval check | Quick check | ads.google.com — ca-pub-6523454944716812. Applied Jun 9, check ~Jun 16–23. |
| 3 | Affiliate signup (Sheet Music Plus) | Deferred | Trigger: Search Console clicks ≥ 500 |
| 4 | Login revival | Deferred | Trigger: Search Console visitors ≥ 1,000 |
| 5 | connect.html — real teacher info | Deferred | When Sohyun ready to take referrals |
| 6 | ABRSM Diploma — ARSM / DipABRSM | Low | PDFs not yet available |

### Known Issues (as of 2026-06-10)
- AdSense: pending Google review — ca-pub-6523454944716812. Check dashboard ~Jun 16–23.
- connect.html: placeholder teacher cards — not promoted publicly.
- Supabase free tier auto-pauses after 7 days inactivity — restore manually from dashboard as needed.
- Git sandbox HEAD.lock: run `rm .git/HEAD.lock` in Terminal if git commit fails.

---

### Phase 47 Updates (2026-05-28 — contact form)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | In-site contact form modal | `index.html` | Replaced `mailto:` footer link with a `ContactModal` React component. Visitors type Name + Email + Message and submit — personal email never exposed. Powered by Web3Forms (free, 250/month). Access key: `1905cf40-5bcd-463a-87dd-c9d5ee673f56`. Submissions forwarded to vividssso@gmail.com. Success/error states handled inline. Commits: `56018b7`, `b662135`, `9ca4fff`. |

### Build Status — Last updated 2026-05-28 (Phase 47)

| # | Feature | Status |
|---|---------|--------|
| 1–101 | All previously completed features (Phases 1–46) | ✅ Done |
| 102 | In-site contact form (Web3Forms, email hidden) | ✅ Done (Phase 47) |

### Pending Work (priority order for next session)

| # | Task | Priority | Notes |
|---|------|----------|-------|
| 1 | Search Console — check indexing status | Quick check | Wait 1–2 weeks, then verify pages are being indexed |
| 2 | Sitewide UX review | Medium | Open thepianobutler.com, use as real teacher/student, note friction |
| 3 | Affiliate signup | Deferred | Trigger: Search Console clicks ≥ 500. Sheet Music Plus (8–12%) or Sheet Music Direct (10%) |
| 4 | Login revival | Deferred | Trigger: Search Console visitors ≥ 1,000 |
| 5 | connect.html — real teacher info | Deferred | When Sohyun ready to take referrals |
| 6 | ABRSM Diploma — ARSM / DipABRSM | Low | PDFs not yet available |

---

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

### Build Status — Last updated 2026-05-28

| # | Feature | Status |
|---|---------|--------|
| 1–97 | All previously completed features (Phases 1–45) | ✅ Done |
| 98 | recommend.html — 2-step wizard + twitter meta tags | ✅ Done (Phase 46) |
| 99 | Google Search Console — domain verified + sitemap submitted | ✅ Done (Phase 46) |
| 100 | SEO title/description overhaul — 28 grade pages + index.html | ✅ Done (Phase 46) |
| 101 | .gitignore cleanup + accidental files removed | ✅ Done (Phase 46) |

---

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

### Build Status — Last updated 2026-06-11

| # | Feature | Status |
|---|---------|--------|
| 1–120 | All previously completed features (Phases 1–53) | ✅ Done |
| 121 | G6 corpus bug fix (DATA_G6_COMP → DATA_G6, 160 pieces restored) | ✅ Done (Phase 54) |
| 122 | find-a-teacher.html — student matching request form | ✅ Done (Phase 54) |
| 123 | teach-with-us.html — teacher application form | ✅ Done (Phase 54) |
| 124 | 17 unused files deleted — repo cleanup | ✅ Done (Phase 54) |

### Pending Work (priority order for next session)

| # | Task | Priority | Notes |
|---|------|----------|-------|
| 1 | AdSense approval check | Quick check (Jun 16–23) | adsense.google.com — ca-pub-6523454944716812 |
| 2 | Search Console — re-check indexing | Quick check (Jun 18+) | Verify "Discovered" pages moving to indexed after Validate Fix |
| 3 | teach-with-us.html — recruit first teachers | High | Share with Sohyun's network. Once 3–5 teachers confirmed, add link to homepage. |
| 4 | find-a-teacher.html — format field update | Medium | Change "In-person" → remove (online-only strategy). Update before public launch. |
| 5 | Affiliate signup (Sheet Music Plus) | Deferred | Trigger: Search Console clicks ≥ 500 |
| 6 | Login revival | Deferred | Trigger: Search Console visitors ≥ 1,000 |
| 7 | ABRSM Diploma — ARSM / DipABRSM | Low | PDFs not yet available |

### Known Issues (as of 2026-06-11)
- AdSense: pending Google review — ca-pub-6523454944716812. Check ~Jun 16–23.
- find-a-teacher.html: format field still has "In-person" option — update before public launch (online-only strategy).
- Supabase free tier auto-pauses after 7 days inactivity — restore manually from dashboard as needed.
- Git sandbox HEAD.lock: run `rm .git/HEAD.lock && rm .git/index.lock` in Terminal if git commit fails.

---

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

### Build Status — Last updated 2026-06-12

| # | Feature | Status |
|---|---------|--------|
| 1–124 | All previously completed features (Phases 1–54) | ✅ Done |
| 125 | Supabase keep-alive GitHub Action | ✅ Done (Phase 55) |
| 126 | find-a-teacher.html online-only update | ✅ Done (Phase 55) |
| 127 | Teacher outreach drafts (KR/EN) | ✅ Done (Phase 55) |
| 128 | Weekly Monday auto-check scheduled task | ✅ Done (Phase 55) |
| 129 | SEO content pages (43 static pages) | ⏸ On hold in `_drafts/` — pending Sohyun's voice/direction |

### Pending Work (priority order for next session)

| # | Task | Priority | Notes |
|---|------|----------|-------|
| 1 | Send teacher outreach messages | High (Sohyun, ~10 min) | `outreach-messages.md` — 3–5 teachers from her network. Revenue path independent of traffic. |
| 2 | AdSense approval check | Auto (Monday check) | ca-pub-6523454944716812 — review re-requested Jun 11. |
| 3 | Search Console indexing | Auto (Monday check) | Validate Fix submitted Jun 11 for 34 pages. |
| 4 | Content direction decision | When ready | Approve/adjust/discard `_drafts/` pages. If approved: Sohyun answers 3 Korean questions → editorial rewrite with her voice. |
| 5 | Viva voce GK pack pilot | After content decision | Strongest paid-product candidate. One grade pilot + accuracy review. |
| 6 | Affiliate signup (Sheet Music Plus) | Deferred | Trigger: Search Console clicks ≥ 500. |
| 7 | Login revival | Deferred | Trigger: visitors ≥ 1,000/mo. |
| 8 | ABRSM Diploma — ARSM / DipABRSM | Low | PDFs not yet available. |

### Known Issues (as of 2026-06-12)
- AdSense: pending Google review — check ~Jun 16–23 (Monday auto-check covers this).
- `_drafts/` content pages: on hold, gitignored — do not publish without Sohyun's review.
- Supabase auto-pause: SOLVED by keep-alive Action (verify first manual run shows green in GitHub Actions).

---

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

### Build Status — Last updated 2026-06-17

| # | Feature | Status |
|---|---------|--------|
| 1–129 | All previously completed features (Phases 1–55) | ✅ Done |
| 130 | viva-voce.html — Viva Voce / GK pack generator, full feature set + verified | ✅ Done (Phase 56) |

### Pending Work (priority order for next session)

| # | Task | Priority | Notes |
|---|------|----------|-------|
| 1 | Sohyun — open viva-voce.html in browser, spot-check a real PDF | High | All logic verified programmatically; needs one human look at actual render + downloaded PDF before wider use. |
| 2 | Decide whether/how to surface viva-voce.html publicly | Medium | Currently standalone, unlinked, `noindex`. Consider: link from a grade page, homepage footer, or keep as teacher-only tool for now. |
| 3 | Possible future: paid PDF pack via Gumroad | Deferred | Per Phase 55 product idea — pilot accuracy review with Sohyun first. |
| 4 | Send teacher outreach messages | High (Sohyun, ~10 min) | `outreach-messages.md` — carried over from Phase 55. |
| 5 | AdSense approval check | Auto (Monday check) | ca-pub-6523454944716812. |
| 6 | Search Console indexing | Auto (Monday check) | Validate Fix submitted Jun 11 for 34 pages. |
| 7 | Affiliate signup (Sheet Music Plus) | Deferred | Trigger: Search Console clicks ≥ 500. |
| 8 | Login revival | Deferred | Trigger: visitors ≥ 1,000/mo. |
| 9 | ABRSM Diploma — ARSM / DipABRSM | Low | PDFs not yet available. |

### Known Issues (as of 2026-06-17)
- viva-voce.html: not yet opened in an actual browser by a human — all verification so far is programmatic (compile/syntax/data-trace). Minor cosmetic edge case noted: a piece with an unusually long title could in theory wrap past its initial space reservation before the next pagination check catches it — not a functional bug, just worth a glance during spot-check.
- AdSense: pending Google review — check ~Jun 16–23 (Monday auto-check covers this).
- `_drafts/` content pages: on hold, gitignored — do not publish without Sohyun's review.
- Supabase auto-pause: SOLVED by keep-alive Action (verify first manual run shows green in GitHub Actions).
- Git sandbox HEAD.lock: run `rm .git/HEAD.lock && rm .git/index.lock` in Terminal if git commit fails.

---

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

### Build Status — Last updated 2026-06-20

| # | Feature | Status |
|---|---------|--------|
| 1–130 | All previously completed features (Phases 1–56) | ✅ Done |
| 131 | timeline.html — fixed phase pacing (no more duplicate month labels) | ✅ Done (Phase 57) |
| 132 | timeline.html — personalized advice via real piece input | ✅ Done (Phase 57) |
| 133 | timeline.html — results screen shows user's actual exam pieces | ✅ Done (Phase 57) |

### Pending Work (priority order for next session)

| # | Task | Priority | Notes |
|---|------|----------|-------|
| 1 | Sohyun — open timeline.html, run through the new piece-input step + results screen | High | Logic verified programmatically (Babel compile + node --check); needs one human spot-check of the actual live flow. |
| 2 | Sohyun — open viva-voce.html, download a real PDF | High | Carried over from Phase 56 — still not opened in an actual browser. |
| 3 | AdSense approval check | Auto (Monday check) | ca-pub-6523454944716812. |
| 4 | Search Console indexing | Auto (Monday check) | Validate Fix submitted Jun 11 for 34 pages. |
| 5 | Affiliate signup (Sheet Music Plus) | Deferred | Trigger: Search Console clicks ≥ 500. |
| 6 | Login revival | Deferred | Trigger: visitors ≥ 1,000/mo. |
| 7 | ABRSM Diploma — ARSM / DipABRSM | Low | PDFs not yet available. |

### Known Issues (as of 2026-06-20)
- timeline.html: not yet spot-checked in a live browser session after Phase 57 changes — only Babel-compile + syntax verified so far.
- viva-voce.html: still not opened in an actual browser by a human (carried over from Phase 56).
- AdSense: pending Google review — check ~Jun 16–23 (Monday auto-check covers this).
- `_drafts/` content pages: on hold, gitignored — do not publish without Sohyun's review.
- Supabase auto-pause: SOLVED by keep-alive Action (verify first manual run shows green in GitHub Actions).
- Git sandbox HEAD.lock: run `rm .git/HEAD.lock && rm .git/index.lock` in Terminal if git commit fails.
