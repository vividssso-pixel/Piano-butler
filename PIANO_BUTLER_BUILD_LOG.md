# Piano Butler — Complete Build Log
**Last updated:** 2026-04-27 (Session 8 wrap-up — next: Session 9 Beat Butler polish)
**Live URL:** https://vividssso-pixel.github.io/Piano-butler/login.html  
**Stack:** React 18 + Babel + Tailwind CSS (all CDN) · Supabase Auth + DB · GitHub Pages

---

## File Structure

```
Piano Butler/
├── CLAUDE.md                        — project instructions for AI
├── auth.js                          — Supabase client + requireAuth() + signOut()
├── login.html                       — login page (pure JS, no React)
├── home.html                        — post-login hub (2 cards)
├── import-schedule.html             — bulk student import page
├── teacher-dashboard.html           — teacher studio management app
├── Index.html                       — repertoire browser (all grades)
├── Prelim/
│   ├── data_prelim.js               — 93 pieces (Comprehensive)
│   ├── data_prelim_leisure.js       — 71 pieces (Leisure)
│   └── piano-repertoire_prelim.html
├── G1/ … G8/                        — same pattern per grade
└── AMEB Syllabus/                   — PDF source files (gitignored)
```

---

## Piece Counts — 2026 AMEB Syllabus (verified 2026-04-23)

### Comprehensive Piano
| Grade | Total | A | B | C | D | Other |
|-------|-------|---|---|---|---|-------|
| Prelim | 93 | 24 | 23 | 46 | — | — |
| G1 | 143 | 48 | 37 | 58 | — | — |
| G2 | 184 | 58 | 50 | 76 | — | — |
| G3 | 196 | 57 | 59 | 80 | — | — |
| G4 | 156 | 49 | 51 | 56 | — | — |
| G5 | 168 | 41 | 33 | 38 | 48 | Collab: 8 |
| G6 | 160 | 41 | 35 | 37 | 47 | — |
| G7 | 148 | 37 | 28 | 41 | 42 | — |
| G8 | 145 | 29 | 29 | 38 | 49 | — |
| **Total** | **1,393** | | | | | |

### Piano for Leisure
| Grade | Total | S4 | S3 | S2 | S1 | Manual |
|-------|-------|----|----|----|----|--------|
| Prelim | 71 | 12 | 11 | 12 | 12 | 24 |
| G1 | 70 | 12 | 11 | 10 | 11 | 26 |
| G2 | 64 | 12 | 11 | 11 | 12 | 18 |
| G3 | 68 | 12 | 11 | 9 | 13 | 23 |
| G4 | 80 | 12 | 11 | 11 | 11 | 35 |
| G5 | 78 | 12 | 11 | 13 | 12 | 30 |
| G6 | 88 | 12 | 12 | 11 | 12 | 41 |
| G7 | 92 | 12 | 9 | 14 | 12 | 45 |
| G8 | 95 | 11 | — | 12 | 12 | 60 |
| **Total** | **706** | | | | | |

**Grand Total: 2,099 pieces**

---

## Session Log — All Work Completed

---

### SESSION 1 — Syllabus Data Build (2026-04-13)

**Goal:** Build all grade data files and HTML apps from PDF syllabus.

#### Completed
- G1–G8 Comprehensive data files (`data_gX.js`) — all pieces with list, composer, title, nationality, era, key, focus (3 keywords)
- G1–G8 Leisure data files (`data_gX_leisure.js`)
- Prelim Comprehensive + Leisure data files
- All grade HTML apps (`piano-repertoire_gX.html`) — React + Tailwind, self-contained
- `Index.html` — main repertoire browser aggregating all grades

#### Data Bugs Fixed (Phase 1 Audit)
| # | Issue | File | Fix |
|---|-------|------|-----|
| 1 | SHCHEDRIN, SITSKY, VINE in wrong list (D instead of C) | data_g7.js | Moved to List C Manual |
| 2 | Same 3 pieces duplicated in C and D | piano-repertoire_g7.html | Removed from List D |
| 3 | BEATH, B. Contrasts missing from HTML List D | piano-repertoire_g7.html | Added |
| 4 | Debussy title missing English translation | piano-repertoire_g7.html | Fixed |
| 5 | BENDA sonatina wrong number (No 7 → No 13) | piano-repertoire_g7.html | Fixed |
| 6 | BURGMÜLLER title missing [Spinning song] | piano-repertoire_g7.html | Fixed |
| 7 | Tchaikovsky missing English translation | piano-repertoire_g7.html | Fixed |
| 8 | All 168 G5 focus arrays had only 2 keywords | data_g5_1.js | Third keyword added |
| 9 | data_g5.js — no nat/era/focus fields | data_g5.js | Marked deprecated |

---

### SESSION 2 — Index.html Feature Build (2026-04-23)

**Goal:** Add smart features to the main repertoire browser.

#### Completed
| Feature | Details |
|---------|---------|
| Focus picker (FOCUS_GROUPS) | Filter by pedagogical focus area |
| Similar pieces (getSimilar scoring) | Weighted match by era/nat/focus |
| My Interests panel | localStorage — saved pieces |
| Exam Readiness checker | Checks List A/B/C coverage |
| Era Balance Advisor | Warns if era mix is unbalanced |
| Nationality filter + NAT_LIST | Dropdown filter by composer nationality |
| Mobile Responsive QA | All grade pages Prelim–G8 + Index.html |

#### Mobile QA Changes (all grade pages + Index.html)
- Button rows → `flex flex-col gap-2` + `flex flex-wrap gap-1.5`
- Page headers → `flex flex-wrap items-start justify-between gap-3`
- Viewport meta → added `viewport-fit=cover`
- Index.html stats row → `flex flex-wrap gap-2` with responsive padding

#### Data Bugs Fixed (Phase 2 Audit)
| # | Issue | File | Fix |
|---|-------|------|-----|
| 1 | G5 Collab: Primo/Secondo tags missing on 6 pieces | piano-repertoire_g5.html | Tags added |
| 2 | G5 Manual: 13 titles abbreviated or missing attribution | piano-repertoire_g5.html | Full titles restored |

---

### SESSION 3 — Teacher Dashboard Build (2026-04-24)

**Goal:** Build teacher studio management tool (`teacher-dashboard.html`).

#### Features Built
| Feature | Details |
|---------|---------|
| Student list | Add / Edit / Delete students |
| Student modal | Name, grade, track (Exam/General), exam date, plan months, lesson duration (30/45/60/Custom), lesson day/time |
| Lesson log modal | Log repertoire, technical, SR/Aural, general knowledge, notes per lesson |
| Exam timeline (buildPlan) | Monthly plan from start → exam date with phase colours |
| General plan panel | Last lesson snapshot + focus pattern bar chart |
| Starting phase picker | Exam track only — pick which phase to start from |
| Schedule view | Students grouped by lesson day |
| Data storage | localStorage (pb_students, pb_logs) — pre-Supabase |

#### Bugs Fixed
| # | Bug | Fix |
|---|-----|-----|
| 1 | Full Plan not updating after student edit | Live lookup: `students.find(s=>s.id===selected.id)` |
| 2 | useMemo not recomputing after edit | Removed useMemo, call buildPlan() directly |
| 3 | Months truncated (4 of 8 shown) | Rewrote buildPlan — cursor first, phases second |
| 4 | startingPhase deleting early months | Clamp instead of filter |
| 5 | goalMonthsInput out of sync on Edit open | Sync on initialisation |
| 6 | Total months calculation wrong | Simple inclusive diff formula |

#### buildPlan Architecture
```
1. Compute endDate (examDate or startDate + planMonths)
2. Walk cursor from startDate → endDate, push one object per month
3. Assign phase to each month by ratio: i / total
4. Clamp: if assigned phase < startingPhase, use startingPhase
5. Map phase → focus text from MONTH_FOCUS lookup
```

---

### SESSION 4 — Auth + Hub + Supabase (2026-04-25 morning)

**Goal:** Real authentication, hub page, Supabase connection.

#### Completed
| Feature | Details |
|---------|---------|
| auth.js — Supabase auth | Real email+password auth via Supabase. requireAuth() + signOut() utility |
| login.html | Dedicated login page — pure JS, no React, email + password fields, show/hide toggle |
| home.html | Post-login hub with 2 cards: Repertoire Browser + Teacher Dashboard |
| Auth flow | login.html → home.html → Index.html or teacher-dashboard.html |
| Session persistence | Supabase client stores session in localStorage automatically |
| Supabase project | icefqxaccclwasnfzgnp.supabase.co — Oceania/Sydney, Nano tier |
| User account | vividssso@gmail.com created in Supabase Auth dashboard |

#### Auth Architecture (B안 — finalised)
```
login.html          — pure JS login form
    ↓ signInWithPassword()
home.html           — requireAuth() session check → hub
    ├── Index.html          — requireAuth() → Repertoire Browser
    └── teacher-dashboard.html  — requireAuth() → Teacher Dashboard
```

---

### SESSION 5 — Supabase DB Migration + Bulk Import (2026-04-25 afternoon)

**Goal:** Move all data from localStorage to Supabase DB. Import 57 students.

#### Completed
| Feature | Details |
|---------|---------|
| Supabase DB tables | public.students + public.lesson_logs |
| Row Level Security | Each teacher (user_id) sees only their own data |
| students table columns | id, user_id, name, grade, track, exam_date, plan_months, lesson_dur, lesson_day, lesson_time, start_phase, extra (JSON), created_at |
| lesson_logs table columns | id, user_id, student_id, date, repertoire, technical, sr_aural, general_k, notes, extra (JSON), created_at |
| rowToStudent() / studentToRow() | Field mapping between JS objects and DB rows |
| rowToLog() / logToRow() | Field mapping for lesson logs |
| extra (JSON) column | Stores additional fields not in core columns |
| import-schedule.html | Standalone bulk import page — inserted 57 students from schedule |
| Sign out button | Added to teacher-dashboard.html header |

#### Data Notes
- ALL data now in Supabase DB — no localStorage fallback
- extra column stores: mood, pieceRating, and any future fields
- 57 students successfully imported on 2026-04-25

---

### SESSION 6 — GitHub + Auto-deploy + Lesson Log UX (2026-04-25 evening / 2026-04-26)

**Goal:** GitHub → Netlify auto-deploy pipeline. Lesson log improvements. Schedule view.

#### GitHub Setup
- Repo created: github.com/[user]/Piano-butler
- .gitignore created — excludes AMEB Syllabus PDFs (180MB+), DS_Store, _admin/, index-designs/, session logs
- Fresh git init (PDFs were too large — had to rm -rf .git and reinitialise after .gitignore was in place)
- Netlify connected to GitHub repo → auto-deploy on every push
- Deploy command: `git add . && git commit -m "..." && git push`

#### Lesson Log — 5 New Features (all in LogModal)
| # | Feature | Details |
|---|---------|---------|
| 1 | Mood rating | 4 emoji buttons (😕😐🙂😀) — saved to extra.mood in Supabase |
| 2 | Traffic light piece rating | 🔴🟡🟢 tap to rate — saved to extra.pieceRating |
| 3 | Focus chip quick-insert | Tap chips to append text to repertoire/technical fields (HS, HT, Scales, etc.) |
| 4 | Copy homework button | One tap copies last lesson notes to clipboard |
| 5 | Last lesson hint | Shows previous log's notes as grey hint text at top of modal |

#### extra column in lesson_logs
- Already existed in Supabase schema — no migration needed
- rowToLog() updated to parse extra JSON for mood + pieceRating
- logToRow() updated to serialise mood + pieceRating into extra

#### Student List Filters
| Filter | Details |
|--------|---------|
| Search | Filter by student name (existing) |
| Grade dropdown | All / Prelim / G1 … G8 |
| Track toggle | All / Exam / General |
| Sort dropdown | Name / Grade / Exam date / Last log |
| Count badge | Shows filtered count |
| Clear button | Resets all filters |

All filters use useMemo — no extra DB calls.

#### Schedule View — Weekly Calendar Grid
- Rebuilt ScheduleView as time-axis weekly calendar
- 7 columns — Sunday through Saturday (always shown, even if empty)
- Sunday shown first (leftmost column)
- Time axis on left: 8:00 AM → 8:00 PM
- Student blocks positioned with absolute CSS (timeToY, durToH functions)
- Day colour coding — each weekday has distinct bg/border/text/grid colour
- Default tab changed from "students" to "schedule" — schedule loads first

#### DAYS_ORDER and DAY_COLOR
```js
const DAYS_ORDER = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"];
// Each day has: bg, border, text, grid colours
```

---

## Deployment State (as of 2026-04-26)

| Item | Status |
|------|--------|
| Live URL | https://exquisite-faloodeh-6d8e82.netlify.app |
| Hosting | Netlify (free tier) |
| Auth | Supabase email+password |
| Database | Supabase DB — students + lesson_logs tables |
| Auto-deploy | GitHub → Netlify (connected) |
| Data | 57 real students imported |

---

---

### SESSION 7 — 캘린더 기능 강화 + GitHub Pages 이전 (2026-04-26 오전)

**Goal:** 구글 캘린더 대체 기능 추가, 호스팅 이전

#### Today View (새 탭)
- 앱 첫 탭을 "Today"로 변경 (기존: Schedule)
- 오늘 요일에 해당하는 학생을 시간순으로 표시
- 각 학생 옆에 "+ Log lesson" / "Absent" 버튼 바로 노출
- 오늘 이미 로그 기록한 학생은 "✓ Logged" 뱃지 표시
- 레슨 없는 날은 "No lessons today — Enjoy your day off!" 표시

#### 결석 / 보강 기록 (AbsenceModal)
- Today 탭 + 캘린더 블록에 "Absent" 버튼 추가
- AbsenceModal: Absent / Makeup 선택, 날짜, 보강 날짜, 메모 입력
- lesson_logs의 extra JSON에 `type: "absent" | "makeup"` 저장
- rowToLog() / logToRow() 업데이트 — type, makeupDate 파싱
- 레슨 히스토리에서 "😔 Absent" / "🔄 Makeup" 뱃지로 표시

#### D-day 뱃지 (학생 카드)
- `daysUntilNext(dayName)` 헬퍼 추가 — 다음 요일까지 며칠인지 계산
- `daysUntilExam(examDate)` 헬퍼 추가
- 학생 카드 이름 아래에 두 가지 뱃지 표시:
  - "🎹 Today!" (오늘 레슨) / "Next: Mon in 2d" (다음 레슨)
  - "D-42" (시험까지) — 14일 이내 빨간색, 60일 이내 노란색
- Today view에도 D-day 뱃지 표시

#### 캘린더 블록 → 바로 액션
- ScheduleView 블록 안에 "+ Log" / "Absent" 버튼 직접 노출
- onLog / onAbsence prop 추가 — 클릭 시 바로 모달 오픈
- 기존: 블록 클릭 → 학생 디테일 이동 (3단계)
- 변경: 버튼 클릭 → LogModal / AbsenceModal 바로 오픈 (1단계)

#### 탭 구조 변경
- 탭 순서: Today → Students → Schedule
- 기본 탭: Today (앱 열면 오늘 레슨이 첫 화면)

#### 호스팅 이전 — Netlify → GitHub Pages
- **문제:** Netlify AI 에이전트 크레딧 300개 초과 → 사이트 전체 정지
- **원인:** GitHub 연결 후 매 push마다 Netlify 빌드 실행 → 크레딧 소모
- **해결:** GitHub 레포를 Public으로 변경 → GitHub Pages 활성화
- **새 URL:** https://vividssso-pixel.github.io/Piano-butler/login.html
- **Supabase URL Configuration 업데이트:**
  - Site URL: `https://vividssso-pixel.github.io`
  - Redirect URL: `https://vividssso-pixel.github.io/Piano-butler/home.html`
- Netlify는 삭제하지 않고 방치 (5월 24일 크레딧 리셋, 무료 플랜이라 비용 없음)
- 앞으로 배포: `git add . && git commit -m "..." && git push` → GitHub Pages 자동 반영

#### 전체 빌드 로그 문서 작성
- `PIANO_BUTLER_BUILD_LOG.md` 생성 — 세션 1~6 전체 누락 없이 기록

---

### SESSION 8 — Brand Identity & Logo (2026-04-27)

**Goal:** Finalise logo mark and establish Butler Suite visual identity.

#### Brand Decisions
| Item | Decision |
|------|---------|
| Logo concept | Pocket watch — staff lines on face, arrow hand, crown at top |
| Hand position | 10:30 — upper-left 45°, arrow tip stops inside circle |
| Staff lines | 5 lines ghost-faded, centre line passes through dot |
| Centre dot | Sits exactly on middle staff line, hand originates from dot edge |
| Tagline | "At your service, always on time." |
| Piano Butler hand | 10:30 — prepared, time to spare (one lesson length remaining) |
| Beat Butler hand | 12:00 — downbeat, this very moment, metronome straight up |
| Butler Suite concept | Same mark, same crown, same circle — hand angle = product identity |
| Exam board scope | Broadened beyond AMEB — tagline no longer exam-board specific |

#### Files Created
| File | Description |
|------|-------------|
| `piano-butler-logo.svg` | Final vector logo mark — watch, staff, arrow hand, wordmark |

#### Session 8 — Design decisions made, not yet applied
| Item | Status |
|------|--------|
| piano-butler-logo.svg | ✅ Final — watch mark, 10:30 hand, 5 staff lines, wordmark, tagline |
| beat-butler-logo.svg | ⚠️ Needs fix — staff lines currently vertical (should be horizontal, same as Piano Butler) |
| Centre dot colour | 🕐 Deferred — 3 options shown (black/black · black/red · black/gold). Decide next session |
| Colour system | 🕐 Deferred — Ebony/Ivory mono vs Navy/Gold premium |
| Typography system | 🕐 Deferred — serif wordmark + UI sans |
| Apply design to pages | 🕐 Deferred — login → home → dashboard order |

---

### SESSION 9 — Beat Butler Polish (next session)

**Goal:** Finish Beat Butler as the first fully "done" product in the Butler Suite.

#### Start here
1. **Fix beat-butler-logo.svg** — replace vertical beat lines with 5 horizontal staff lines (identical to piano-butler-logo.svg layout). Hand stays at 12:00, black.
2. **Centre dot colour decision** — confirm from 3 options: (a) both black, (b) Piano=black/Beat=red, (c) Piano=black/Beat=gold. Apply to both SVGs.
3. **Beat Butler branding** — update header wordmark in `Beat Butler/index.html` to match Butler Suite style (Georgia serif, letter-spacing, same tagline).
4. **Beat Butler logo in header** — embed SVG mark inline in the Beat Butler app header.
5. **Final check** — dark mode, mobile, BPM range, tap tempo, voice/record modes all working.

#### Beat Butler current state (as of 2026-04-27)
| Feature | Status |
|---------|--------|
| BPM slider + display | ✅ Done |
| Tap tempo (keyboard + button) | ✅ Done |
| Tempo name (Grave → Prestissimo) | ✅ Done |
| Time signature selector | ✅ Done |
| Subdivision selector | ✅ Done |
| Voice counting (TTS) | ✅ Done |
| Custom voice recording per beat | ✅ Done |
| Click sound mix toggle | ✅ Done |
| Dark / light mode toggle | ✅ Done |
| Colour accent swatches | ✅ Done |
| Mobile layout | ✅ Done |
| Logo / branding | ⚠️ Not applied — beat-butler-logo.svg exists but not embedded |
| Auth / login gate | ❌ Not yet — standalone app, no auth |
| Stripe / paywall | ❌ Not yet |

---

## Features Remaining (Not Yet Built)

| # | Feature | Priority |
|---|---------|---------|
| 1 | Beat Butler — logo fix + branding | 🔴 HIGH — do first (lightest lift, one product "done") |
| 2 | Centre dot colour decision | 🔴 HIGH — confirm then apply to both SVGs |
| 3 | Colour system | 🔴 HIGH — Ebony/Ivory mono or Navy/Gold premium |
| 4 | Typography system | 🔴 HIGH — serif wordmark + UI sans, define scale |
| 5 | Apply design to Piano Butler pages | 🟡 MED — login → home → dashboard order |
| 6 | Index.html — Stripe payment gate | 🟡 MED |
| 7 | Calendar extras | 🟡 MED — holiday blocks, monthly view, tuition, parent contacts |
| 8 | IMSLP sheet music links per piece | 🟡 MED |
| 9 | Teacher Dashboard — Polish pass | 🟡 MED — edge cases, UX improvements |
| 10 | Progress Passport | 🟢 LOW |
| 11 | Claude API assistant | 🟢 LOW — requires backend |
| 12 | Mobile UX phone test | 🟡 MED |

---

## Key Architecture Decisions

| Decision | Choice | Reason |
|----------|--------|--------|
| Auth pattern | B안 — login.html separate page | Cleaner than LoginGate component in every page |
| Data storage | Supabase DB (not localStorage) | localStorage = data loss risk, no multi-device |
| Hub page | home.html separate from Index.html | Extensible — add cards without touching Repertoire Browser |
| buildPlan | Cursor-first, phases-second | Eliminates rounding errors in month assignment |
| Deploy | Netlify + GitHub auto-deploy | No more manual drag & drop |
| Grade pages | Self-contained single HTML files | No server needed, works offline |

---

## Supabase Reference

| Item | Value |
|------|-------|
| Project URL | https://icefqxaccclwasnfzgnp.supabase.co |
| Region | ap-southeast-2 (Oceania/Sydney) |
| Tier | Nano |
| Auth user | vividssso@gmail.com |
| Tables | public.students, public.lesson_logs |
| RLS | Enabled — user_id filter on all rows |
