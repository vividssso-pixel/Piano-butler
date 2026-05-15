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
| 3 | Admin piece-count page | `admin-counts.html` | Password-protected (`pianobutler2026`) React dashboard. Shows live piece counts from all loaded data files. Grand Total card + per-syllabus subtotals. SectionTable with list badges + ✓ OK / ⚠ MISSING status. Expected vs Actual panel compares live counts to CLAUDE.md targets — red highlight on mismatch. `noindex` meta tag. |
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

### Build Status — Last updated 2026-05-14 (evening)

| # | Feature | Status |
|---|---------|--------|
| 1–54 | All previously completed features (Phases 1–30) | ✅ Done |
| 55 | Teacher Dashboard removed from public nav | ✅ Done (Phase 31) |
| 56 | connect.html — teacher/course matching page | ✅ Done (Phase 31) |
| 57 | diagnose.html — purpose-first redesign for returning players | ✅ Done (Phase 31) |

### Pending Work (priority order for next session)

| # | Task | Priority | Notes |
|---|------|----------|-------|
| 1 | Test diagnose.html end-to-end | First thing | Go through all 5 purpose paths. Check piece recommendations make sense per purpose + level. Note any friction. |
| 2 | connect.html — add real teacher info | High | Replace Sohyun placeholder with real photo, real booking link, real price. Add 1–2 more real teachers if possible. |
| 3 | $4 Full Report — define content | High | Decide exactly what's in the report before building Stripe/jsPDF. Suggested: personalised level summary + 6-month plan outline + 10 piece list + teacher match. |
| 4 | $4 Full Report — Stripe + jsPDF | High | Stripe Checkout (hosted, no backend) → payment success → jsPDF generates PDF in browser. |
| 5 | G8 Leisure BEETHOVEN Andante duplicate | Quick fix | Check Piano for Leisure G8 PDF — is Andante in both S4 and S1? |
| 6 | ABRSM data audit | Medium | ERA/FOCUS/NAT/duplicate check across all 9 ABRSM grade files. |
| 7 | Google Search Console — submit sitemap | Quick win | search.google.com/search-console → add sitemap.xml URL → verify. |
| 8 | Ad integration | Low | After traffic grows. |

### Known Issues (as of 2026-05-14 evening)
- ⚠️ G8 Leisure: BEETHOVEN Andante duplicate — pending PDF verification.
- diagnose.html $4 report CTA: coming-soon modal with waitlist email. Stripe pending.
- connect.html teacher cards: placeholder data only. Real teacher info needed before promoting publicly.
