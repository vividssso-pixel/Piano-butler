# Phase 485, round 1: teaching and code review

Reviewer: piano teacher (teaching tomorrow from this book) and React/JS engineer, in one pass.

**Builds.** Every finding is marked:

- **N** = seen on the current build, `a3/drills.t485.html` (23:00:32), source `cb/cbscales.jsx` + `cb/patch485.py` (22:55).
- **O** = seen only on the older build (22:29, source `cb/cbscales.r0.jsx`); fixed in the current build.

The source is being edited while I write (`cbscales.jsx` was saved again at 23:22:02; no new build yet). Where I re-read that newer source, I say so. Line numbers move, so places are named by function and by the quoted text.

Counts: **2 blockers, 8 must fix, 11 minor** (all N). 12 more points were seen only on the older build (O) and are now fixed.

---

## Blockers

### B1 (N). On screen, the tools on "Practise in steps" are plain text, not links

- **Where:** `cbToolLink` and the ladder in `cbScalesPages` (page 8; on screen, step 7 "Practise in steps", `?tool=cb-p-scales`).
- **What is wrong:** `cbToolLink` decides between a link and plain text by calling `lbScreen()`, which is `React.useContext(LbScreenCtx)`. The ladder elements are built when `cbScalesPages(true)` runs inside `CbScalesLearn`. That is outside every `LbScreenCtx.Provider`, so `lbScreen()` returns `false` and every tool name renders as a grey `<span>`. Measured on the current build: the whole screen book has exactly **one** `a[href*="tool="]` (the key pad's "Fingering →") and **0** `a.chip`. All 17 ladder tools (4 + 5 + 5 + 3) cannot be opened, so the page that turns the concept into a practice plan cannot be used on screen. It also calls a hook inside `.map()` while elements are built, which breaks the rules of hooks (it only avoids a crash because the number of calls is the same on every render). The 23:22 source still has this code.
- **Fix:** pass the flag in; never call the hook here. One helper for every in-book link (it also fixes B2):

```js
// a link inside the screen book: keeps the language and a student link's lock
const cbHref = (q) => '?' + q + (LANG === 'ko' ? '&lang=ko' : '')
  + (new URLSearchParams(location.search).get('lock') === '1' ? '&lock=1' : '');
const cbToolLink = (id, scr) => { const tl = TOOLS.find(x => x.id === id); if (!tl) return null;
  return scr ? <a key={id} className="chip" href={cbHref('tool=' + id)} style={{textDecoration:'none',minHeight:40,display:'inline-flex',alignItems:'center',fontSize:13.5,whiteSpace:'normal',textAlign:'left'}}>{tl.title}</a>
    : <span key={id} style={{whiteSpace:'nowrap'}}>{tl.title}</span>; };
```

In the ladder, replace `{scr ? tools.map(cbToolLink) : tools.map((id, j) => <React.Fragment key={id}>{j ? <span style={{margin:'0 6px'}}>·</span> : null}{cbToolLink(id)}</React.Fragment>)}` with:

```js
{scr ? tools.map(id => cbToolLink(id, true)) : tools.map((id, j) => <React.Fragment key={id}>{j ? <span style={{margin:'0 6px'}}>·</span> : null}{cbToolLink(id, false)}</React.Fragment>)}
```

Test: the screen book must have 18 `a[href*="tool="]` (17 ladder links + Fingering), and the print must have none.

### B2 (N). A student link that taps "Fingering →" lands in the teacher view

- **Where:** `CbKeyPad`, the "Fingering →" link (`href={'?tool=scale-finder&key=' + … + (LANG === 'ko' ? '&lang=ko' : '')}`). Once B1 is fixed, the same applies to every ladder link.
- **What is wrong:** the link reloads the whole page without `lock=1`. Checked on the current build, starting from the student link `?tool=cb-p-scales&lock=1`:
  - on a device that never chose a mode, the next page is `?tool=scale-finder` in the **teacher view** (Chapters, Toolbox, Practice tabs, "TEACHER VIEW", "Copy student link");
  - on a device saved as student, the Toolbox and Practice tabs come back, so the lock is gone.

  A student who follows the teacher's link ends up in the teacher UI. The language is kept (`&lang=ko` checked), but the mode and lock are not. The 23:22 source still has this.
- **Fix:** `href={cbHref('tool=scale-finder&key=' + encodeURIComponent(sel))}`, using `cbHref` from B1. A locked student then sees only the scale finder, and the browser's back button returns to the book.

---

## Must fix

### M1 (N). Page 3 "At the piano" is a free task, and step 2 cannot be done on screen

- **Where:** page 3 "Any key" (screen step 2), `LbPiano`.
- **What is wrong:**
  1. "Pick a key." breaks rule 3 (set tasks, never "any"). A beginner who only knows C major gets no key to play.
  2. "…tick the key you built." On screen the table rows cannot be ticked. On paper, the task only works once a key has been picked.
- **Fix** (the keys are the "First" step of page 8):
  1. EN `'Play G major up from G with the steps, saying each note’s name. Then F major from F.'` · KO `'G에서 걸음대로 G장조 음계를 올라가며 음이름을 하나씩 말해요. 그다음 F에서 F장조 음계를 쳐요.'`
  2. EN `'Check each note against its row in the table. Next time: D major, then B♭ major.'` · KO `'표에서 그 조의 줄과 음을 하나씩 맞춰 봐요. 다음에는 D장조, 그다음 B♭장조를 쳐요.'`

### M2 (N). Page 4 asks for staff paper, which the book does not give

- **Where:** page 4 "Key signatures", `LbPiano` step 3: "On staff paper, draw G major’s and F major’s key signatures, on the treble staff and on the bass staff."
- **What is wrong:** there is no Workbook for this concept and no staff paper in the book, so the task needs something the book does not give.
- **Fix** (a task done on the page's own picture, with no new drawing; the facts match chapter 19):
  - EN `'On both staves above, point to G major’s F♯ and F major’s B♭, and say which line each sits on.'`
  - KO `'위의 두 오선에서 G장조의 F♯와 F장조의 B♭을 가리키고, 각각 어느 줄에 있는지 말해요.'`

  If drawing is wanted, the page itself needs two blank staves (check that the page still fits).

### M3 (N). "Practise in steps" does not say when to move on, or where each step's work is

- **Where:** page 8 (screen step 7), its `LbSay` and the third field of each `STEPS` row.
- **What is wrong:** "go up a step when its keys are easy" is not a rule a teacher or a child can check. The steps name tools, but not the book pages that teach them. A teacher with a C-major-only beginner has to work out alone which parts of pages 3 to 7 belong to "First".
- **Fix:**
  - **`LbSay`.** EN `'The rule is the same for every key; only how many keys changes. Start at First. Go up a step when you can show checks 1 to 3 (My five checks) in every key of your step, without the book.'` · KO `'규칙은 모든 조에서 같아요. 단계마다 조의 수만 달라요. ‘처음에’부터 시작해요. 그 단계의 모든 조에서 책을 보지 않고 확인 1~3(나의 다섯 가지 확인)을 보여 줄 수 있으면 다음 단계로 가요.'` The pass rule is my proposal and is for Sohyun to confirm.
  - **The `what` lines.** Page titles are used, so the references work both on paper and on screen:

| Step | EN | KO |
|---|---|---|
| First | `'Build each from the rule (Any key); say its sharps or flats (Key signatures).'` | `'규칙으로 하나씩 만들고(어느 음에서나 장음계), 샤프나 플랫을 말해요(조표).'` |
| Then | `'The order of sharps and flats (Key signatures); a major key’s relative minor, natural and harmonic (Minor scales).'` | `'샤프와 플랫의 순서(조표), 장조의 나란한조, 자연단음계와 화성단음계(단음계).'` |
| Further | `'The circle of fifths (The circle of fifths); placing a key signature (Key signatures); the melodic minor (Minor scales); the major pentatonic on C and G (Other scales).'` | `'5도권(5도권), 조표 자리 찾기(조표), 가락단음계(단음계), C와 G의 장조 5음음계(다른 음계).'` |
| Later | `'All fifteen key signatures (Any key, The circle of fifths); double sharps (Minor scales); the chromatic scale (Other scales); the modes.'` | `'조표 15개 전부(어느 음에서나 장음계, 5도권), 겹샤프(단음계), 반음계(다른 음계), 선법.'` |

### M4 (N). The five checks assume every key, but the ladder teaches a few keys at a time

- **Where:** page 9 "My five checks" (screen step 8), its `LbSay`.
- **What is wrong:** check 2 ("build a major scale from any note") and check 4 ("find a key on the circle of fifths") can never be "Got it!" for a student on the First step. Nothing ties the checks to the keys of the student's step, so a beginner sees two checks they cannot reach. Each check does match its page: 1 → p2, 2 → p3, 3 → p4, 4 → p5, 5 → p6. Page 7 has no check, which is acceptable.
- **Fix:**
  - **Print:** EN `'Show each one at the piano, on its page (2 to 6), in the keys of your step (page 8).'` · KO `'8쪽에서 내가 있는 단계의 조로, 2~6쪽을 하나씩 펴고 피아노 앞에서 보여 줘요.'`
  - **Screen:** EN `'Show each one at the piano, using steps 1 to 5, in the keys of your step (step 7).'` · KO `'7단계(단계별로 연습하기)에서 내가 있는 단계의 조로, 1~5단계를 하나씩 펴고 피아노 앞에서 보여 줘요.'`

### M5 (N). The keyboard clock is the book's main picture, and it is never defined

- **Where:** pages 1, 2, 6 and 7, the opener's pad, and the REMEMBER on page 7 ("…the same clock"). `LbDefs` on page 2 defines half step, scale, major scale and degree, but not the clock.
- **What is wrong:** rule 14 (like a dictionary). A child meeting the concept book first does not know that one place round the ring is one half step, or that C is at the top. The p1 caption assumes it ("one shape, turned to start on its key").
- **Fix:** add a first entry to page 2's `LbDefs`, then check the page still fits:
  - EN `[t('keyboard clock', '건반 시계'), X('The twelve keys of one octave in a ring, C at the top. Each place clockwise is a half step higher.', …)]`
  - KO `'한 옥타브의 열두 건반을 둥글게 놓은 거예요. 맨 위는 C예요. 시계 방향으로 한 칸이 반 걸음 위예요.'`

  (`KeyRing` puts key *i* at −90° + 30°·*i*, `KEY12[0]` = C, and the shape group is rotated to the key.)

### M6 (N). The minors are never shown "all keys at once"

- **Where:** page 6 "Minor scales".
- **What is wrong:** the majors get the whole map (the 15-row table on page 3, every signature on page 4, the circle on page 5). The minors get one figure each (A minor) and a pad that shows one key at a time. The book promises the concept "applied to all keys at once", and the ladder's Then and Further steps list nine minor keys, but no page shows which minor goes with which major.
- **Fix:** add one line under page 6's figures (or show the relative minors inside the page 5 circle):
  - EN `'Every major key has its relative minor, three half steps lower: C–Am, G–Em, D–Bm, A–F♯m, E–C♯m, B–G♯m, F♯–D♯m, D♭–B♭m, A♭–Fm, E♭–Cm, B♭–Gm, F–Dm.'`
  - KO `'장조마다 반 걸음 세 개 아래에 나란한조가 있어요: C–Am, G–Em, D–Bm, A–F♯m, E–C♯m, B–G♯m, F♯–D♯m, D♭–B♭m, A♭–Fm, E♭–Cm, B♭–Gm, F–Dm.'`

  Run both through `X()` so the signs keep to their letters.

### M7 (N). On phones 360 px wide or narrower, the scale table's notes overlap

- **Where:** `CbScaleTable` on screen (page 3, step 2), wrapped as `<div style={{minWidth:0}}><CbScaleTable hl="D"/></div>`.
- **What is wrong:** the table gets the viewport width minus about 158 px of nested padding (162 px at 320, 202 px at 360), so each of the seven note columns is about 11 to 17 px wide. Overlapping cell texts measured on the current build: **48 at 320 px, 35 at 340, 4 at 360**, 0 at 375 and 390. 360 px is a common Android width.
- **Fix:** let the table scroll sideways instead of squeezing.
  - In page 3: `<div style={{minWidth:0,overflowX:'auto'}}><CbScaleTable hl="D"/></div>`.
  - In `CbScaleTable`'s outer `style`, add `minWidth:scr ? 300 : 0`.
  - Re-run the overlap count at 320, 340 and 360.

### M8 (N). The page 4 caption runs along the picture frame's bottom line (English print)

- **Where:** page 4 "Key signatures", the caption under `CbSigs` ("key: the major key whose key signature ends at the sign above it"), inside `<LbPic h={392}>`.
- **What is wrong:** in the English Lesson Book the caption sits on the frame's double line, so a line runs through every letter (`review/r1/shots/new/crop-p4-cap.png`). The Korean caption is one line shorter and clears the frame (`crop-p4-cap-ko.png`).
- **Fix:** give the picture room, for example `<LbPic h={412}>`. If the page then overflows, move the caption out of `LbPic` so it sits directly under the picture box. Check the EN and KO prints afterwards.

---

## Minor

- **m1 (N). An unknown concept book prints a blank page.** `?book=concept&ch=zzz` gives an empty white page. **Fix:** in `BookRoot`, when `kind === 'concept'` and `!CONCEPT_BOOKS[ch]`, render one line: EN `'No concept book called “zzz”.'` · KO `'“zzz”라는 개념책이 없어요.'`
- **m2 (N). The page 1 QR opens the teacher view on a student's phone.** `bkLink('tool=cb-p-scales')` has no `lock=1`, and drills opens in the teacher view by default. The chapter books' QRs behave the same way, so this is for Sohyun. **Fix, if she wants it:** `bkLink('tool=cb-p-scales&lock=1')`.
- **m3 (N). Two pads can play at the same time.** `CbKeyPad` (opener) and `CbShapesPad` (pages 6 and 7) each stop only their own timers. Checked on the older build; the code is the same now. **Fix:** a module-level `let cbStopOther = null;`. Before each play, call `if (cbStopOther && cbStopOther !== stop) cbStopOther(); cbStopOther = stop;`. In the unmount cleanup, set `cbStopOther = null` if it is that pad's `stop`.
- **m4 (N). A teacher who opens a tool from the book cannot get back to the book in the app.** After "Fingering →", the tool's back button reads "← Toolbox" and goes to `?view=toolbox` (checked). Only the browser's back button returns to the book. **Fix:** route in the app, like `OPEN_CH`: a module hook `OPEN_TOOL = (id) => update({ tool: id, from: 'tool:cb-p-scales' })`, with the back button honouring `from`.
- **m5 (N). The teacher cannot see the concept book's progress.** Step ticks are saved under lesson id `cb-p-scales` in `pb_lesson_steps_v1`, which is synced. The dashboard's "Chapter steps done" only counts ids that extend a chapter id in `DRILL_LINKS.chapters`, so they never show. The five checks (`pb_five_cb_scales_v1:stage`) stay on the device, like every chapter's. **Fix (her call):** add a "Concept book: Scales and keys" row for `cb-p-scales` to the dashboard's list.
- **m6 (N). The Toolbox card's Print can print a Korean book; the Books shelf does not list the concept book.** `CbCard` adds `&lang=ko` to the Print link when the app is in Korean. The books are English only (Phases 312 and 325; the shelf always asks for `lang=en`). **Fix:** `const href = '?book=concept&ch=' + cid + '&lang=en';` (or keep Korean print, if Sohyun chooses that), and add a shelf row for the concept book.
- **m7 (N). The screen header says the title three times.** It reads "Concept book: Scales and keys", then "SCALES AND KEYS", then "Scales and keys". **Fix:** drop the `Lesson` title when the opener already shows it, or shorten the tool title to "Scales and keys".
- **m8 (N). Page 4, step 1 has beginners play E♯ and B♯ with no help.** **Fix:** append EN `' (E♯ is played on F, B♯ on C)'` · KO `'(E♯는 F 건반, B♯는 C 건반에서 쳐요)'`.
- **m9 (N). The page 8 note "…is in Technique: Playing scales and chords" is plain text on screen,** so there is no way to get there from the book. **Fix:** on screen, make it a link to that Toolbox group (or to `scale-finder` via `cbHref`).
- **m10 (N). Page 4's flat key labels run together in the Korean print** ("B♭E♭A♭D♭G♭C♭", `crop-p4-cap-ko.png`). The ♭ falls back to a wide CJK glyph inside the 15-unit spacing. **Fix:** draw the sign in its own tspan, for example `<tspan style={{fontFamily:MUSIC_FONT}}>♭</tspan>` (as `tnSign` does), or widen the step from 15 to 17 units.
- **m11 (N). The small rings on pages 6 and 7 have very small note labels in print** (three across the page). This may already be covered by the design pass. **Fix:** check at A4 print size; use two across with larger labels if they read under about 8 pt.

---

## Seen on the older build only (O): fixed in the current build

1. Page 3 said that a black key "takes a sharp or flat". Now it says "each letter once" and gives E♯ played on F.
2. Tasks said "your teacher". Now neutral.
3. The key signature was "on every line" / 줄마다. Now "at the start of every line of music, before the time signature" / 오선마다 맨 앞.
4. The 5th was defined as "five letters", which gives B→F. Now the 5th is a perfect 5th, 7 half steps, so B→F♯.
5. The table had 13 rows, without C♯ and C♭. Now 15 rows, with twin keys together.
6. T+S was used but never defined. Now defined on page 6.
7. Page 6 was overfull. It is split into page 6 (minors) and page 7 (other scales).
8. The whole-tone and blues shapes had no tool and no ladder step. Removed.
9. The ladder's tools did not match its words. Now Then has build-minor and Further has minor-forms.
10. The ladder's filled and outlined coins had no key. A coin key was added.
11. Screen page 9 said "pages 2 to 6". Now "steps 1 to 5".
12. The modes tool blurb read "Lydian to Locrian…" while the tool runs Ionian to Locrian. Now "Ionian to Locrian: same notes, a new home note." (`patch485.py`).

---

## Checked, no finding (current build unless marked)

- **`KeyRing` `o.pat`.** Every existing use renders exactly as before. I compared the DOM against the shipped `a3/drills.t484.html` on 12 routes, in English and Korean:
  - `?book=lesson&ch=scales` and `?book=lesson&ch=key-signatures`
  - `?book=work&ch=scales`
  - `?drill=scales&tab=learn`
  - `?drill=scales&tab=drill&level=10`
  - chapter 16 map pads

  Interactive checks (tapping keys, seeded random) also gave the same DOM. Algebra: with `PAT = PB_MAJOR`, `(PAT[j+1]−PAT[j]+12)%12===1` is true only for j = 2 and j = 6, the old `half`. `FifthsRing` without `o.twins` is identical (chapter 19 unchanged).
- **The pads in the harness.** 72 shape × key combinations (6 shapes × 12 keys) on both shapes pads, EN and KO. Each was checked against an independent speller and against the dots' angles on the ring: 0 wrong, 0 page errors, no throws for black-key tonics. Double sharps are spelled and explained correctly (for example "F𝄪 is F double sharp … played on the key G"). The key pad was tapped on every key of both rings.
- **Sound** stops when the same pad plays again and when the tool is left (checked on the older build; the cleanup code is unchanged).
- **React dev build** (React 18.3.1 development, warnings proven to be captured): 0 warnings on `?teacher=1&tool=cb-p-scales`, `?teacher=1&view=toolbox`, `?tool=cb-p-scales&lock=1`, `?book=lesson&ch=scales` and `?drill=scales&tab=learn`. No missing-key warnings.
- **Print route** `?book=concept&ch=p-scales`: 9 pages in EN and in KO, 0 overflow, no database calls.
- **`LbPage head`.** All other `LbPage` calls are unchanged (the DOM comparison of lesson books above).
- **Hidden tool.**
  - Not listed by the Toolbox search ("concept", "scales and keys", "cb-p", "the rule") or by the Find overlay.
  - `?tool=cb-p-scales&lock=1` opens the student view with no tabs.
  - Toolbox card: Open goes to `?tool=cb-p-scales`, and back goes to `?view=toolbox` (EN and KO).
- **`FiveChecks376` store key** `pb_five_cb_scales_v1:stage` does not collide with any other key.
- **`patch485.py`'s older-tool changes** render as intended in the Toolbox, chapter 16 and chapter 19: 장조 / 단조 with no space, 장음계 만들기, 첫 번째 걸음, F♯ 음이 필요해요, and the new modes blurb. They change shipped chapters' Korean, so they belong in her review.
- **320 px:** the only element wider than the page is the teacher header (한국어 · Do Re Mi · TEACHER VIEW · Dashboard, 347 px). That is the same on the shipped t484 (the scale finder there is 355 px), so it is outside this phase.

---

## Scripts and evidence

- **Scripts:** `cb/review/r1/scripts/`: ringdiff, ringdiff2, domdiff2, shapes3, cbprint2, cbmisc, lockescape, tbl320, widths, devchk, devwarn, final.
- **Screenshots:** `cb/review/r1/shots/new/` (current build) and `cb/review/r1/shots/` (older build).
