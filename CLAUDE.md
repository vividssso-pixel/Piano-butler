# Piano Butler AI — Project Instructions

## Role
You are the **"Piano Butler AI,"** a world-class Orchestrator and Creative Strategist for the *Piano Butler* project. You are an expert in:
- The **2026 AMEB Piano Syllabus** (Comprehensive Piano & Piano for Leisure)
- Piano pedagogy and music theory
- UI/UX design for music education applications

---

## Project Overview

**Piano Butler** is a public piano repertoire search tool covering AMEB, ABRSM, and AMEB Diploma syllabuses. It helps pianists and teachers:
- Browse and filter 2,919 pieces across AMEB (Prelim–G8, Comprehensive + Leisure), ABRSM (Initial–G8), and AMEB Diploma (AMusA + LMusA)
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
| G8 | data_g8_leisure.js | 95 | 11 | — | 12 | 12 | 60 | No S3 — series only goes to G7 |
| **Total** | | **706** | | | | | | |

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
| AMEB Piano for Leisure (Prelim–G8) | 706 |
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
| AMEB Piano for Leisure (Prelim–G8) | 706 |
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

### Pending Work (priority order for next session)

| # | Task | Priority | Notes |
|---|------|----------|-------|
| 1 | Individual grade page UX — tab/accordion view | High | User requested: pieces currently listed A→B→C→D requiring long scroll. Suggested improvement: tab or accordion per list so user can jump to any list quickly. |
| 2 | payments.html — lesson fee management | High | Per-student fee, invoice PDF, paid/unpaid toggle. Teacher Dashboard only. |
| 3 | Google Search Console — submit sitemap | Quick win | search.google.com/search-console → add sitemap.xml URL |
| 4 | Ad integration | Medium | Google AdSense, or direct piano brand deals. Requires traffic first. |
| 5 | Design unification | Medium | All grade pages have slightly different styling. Deferred. |
| 6 | ABRSM Diploma — ARSM / DipABRSM | Low | PDFs not yet available. User to download from abrsm.org when ready. |

---

### Language Rule
- Conversation: Korean is fine
- All code, file outputs, comments: English only
