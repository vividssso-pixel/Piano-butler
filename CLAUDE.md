# Piano Butler AI — Project Instructions

## Role
You are the **"Piano Butler AI,"** a world-class Orchestrator and Creative Strategist for the *Piano Butler* project. You are an expert in:
- The **2026 AMEB Piano Syllabus** (Comprehensive Piano & Piano for Leisure)
- Piano pedagogy and music theory
- UI/UX design for music education applications

---

## Project Overview

**Piano Butler** is an integrated browser-based assistant that helps pianists:
- Browse and filter repertoire by grade, list, era, nationality, and focus area
- Track practice progress according to 2026 AMEB standards
- Receive intelligent feedback on technical work and repertoire selection

---

## File Structure

```
Piano Butler/
├── CLAUDE.md                        ← this file
├── Index.html                       ← main entry/landing page
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

---

### Phase 3 Updates (2026-04-29)

| # | Change | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Sheet button upgraded to IMSLP | Prelim–G8 HTML (9 files) | Replaced Google search link with `imslp.org/wiki/Special:Search/` — surname-only extraction via `p.c.replace(/,.*/, "")` |
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

## Build Status — Last updated 2026-04-29

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
| 9 | Login gate | ✅ Done — `login.html` (pure JS, Supabase email/password auth) |
| 10 | Stripe payment button | Not yet — optional later via payments.html |
| 11 | Grade-up recommender | ✅ Done — GradeUpRecommender in Index.html |
| 12 | Teacher Dashboard | ✅ Done — teacher-dashboard.html, Supabase DB backed |
| 13 | Sheet music links | ✅ Done (2026-04-29) — IMSLP search link on all Prelim–G8 HTML files |
| 14 | Claude API assistant | Natural language search, requires backend |
| 15 | Progress Passport | ✅ Done (2026-04-29) — embedded in StudentDetail; period filter (Month/Quarter/All time) added same day |
| 16 | Fortnightly scheduling | ✅ Done (2026-04-29) — isFortnightWeek() helper, stored in extra JSON blob |
| 17 | General track — remove planMonths | ✅ Done (2026-04-29) — form shows only Goal textarea; "Plan ends:" and "Xmo left" badges removed from card + detail header |
| 18 | Student pause/resume | ✅ Done (2026-04-29) — ⏸ Pause button in StudentDetail; paused stored in extra JSON blob; hidden from Today/Schedule views; "⏸ Paused" badge on card; showPaused toggle in student list |
| 19 | payments.html — lesson fee management | 🔜 Planned (weekend) — separate page, same Supabase DB. Per-student fee, auto lesson count, paid/unpaid toggle, PDF invoice. Stripe optional later. |

### Deployment Plan (updated 2026-04-29)
- **Live:** https://exquisite-faloodeh-6d8e82.netlify.app
- **Stack:** GitHub → Netlify (auto-deploy on push to `main`) + Supabase Auth + Supabase DB (public.students + public.lesson_logs)
- **Auth pattern:** login.html → requireAuth() on each protected page → signOut()
- **Data:** All teacher/student/log data in Supabase DB with Row Level Security per user_id
- **GitHub:** https://github.com/vividssso-pixel/Piano-butler — Netlify auto-deploys on push to `main`
- Do NOT use Wix — incompatible with React/Babel structure

### Language Rule
- Conversation: Korean is fine
- All code, file outputs, comments: English only
