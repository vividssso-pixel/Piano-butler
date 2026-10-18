# Phase 485, round 1: what was done with each finding

Build after the fixes: `a3/drills.t485.html` (source `cb/cbscales.jsx`, `cb/patch485.py`). Pre-fix source: `cb/cbscales.r0.jsx`.
Structure change: the book is now 9 pages. Page 6 was too full for the new entries, so it split in two:
p6 Minor scales (natural, harmonic, melodic on the clock) and p7 Other scales (major, major pentatonic, chromatic).
The ladder is p8 and the five checks p9 (the checks still point at pages 2 to 6).

## Theory

| # | Finding | Done |
|---|---|---|
| B1 | "A scale's sharps or flats are its key signature" wrong for minors | Fixed: opener says "A major scale's"; p4 "The sharps or flats of a key"; p6 harmonic minor: the raised note is an accidental each time, never in the key signature |
| B2 | "a black key takes a sharp or flat" | Fixed, theory's wording: "When the steps need a note the plain letter does not give … That note can be a white key: F♯ major has E♯, played on F." |
| M1 | 'key' never defined; piano key vs musical key | Fixed: p3 entry **key** (the scale a piece uses, named after its tonic). Opener "from any note", "twelve major keys"; legend "same piano keys"; chromatic "every note, white and black"; pad "Tap a piano key on the clock, or a key on the circle" |
| M2 | 'five letters' gives B→F | Fixed: "On the circle every 5th is 7 half steps (a perfect 5th), so a 5th above B is F♯, not F". (The sentence naming the dominant was later cut for design M4.) |
| M3 | T+S undefined, two meanings | Fixed: p6 entry **T+S** (3 half steps; harmonic minor 6 to 7); p7 pentatonic entry says its T+S steps are skips. p2 **scale**: "A major or minor scale goes step by step, each letter once" |
| M4 | 13 rows; C♯ and C♭ missing | Fixed: 15 rows, twins together (B/C♭, F♯/G♭, C♯/D♭); p5 entry: three places have two names, so fifteen key signatures |
| M5 | direction words; enharmonic not named | Fixed: legends and REMEMBER "from C"; ringCap "from C"; p3 entry **same keys, two names** with "Its other name is enharmonic" (딴이름한소리) |
| M6 | one signature, two keys | Fixed: p4 "the major key"; p6 entry **which key?**; check 3 "name the major key" |
| M7 | 'raised' only with sharps | Fixed: harmonic "B♮ (B natural) in C minor"; melodic "(C minor: A♮ B♮)" |
| M8 | double sharp unexplained | Fixed: the shapes pad explains F𝄪 (letter built from the data); ladder 'Later' lists double sharps |
| M9 | tools don't match their words | Fixed: Then gets build-minor; Further gets minor-forms |
| M10 | ladder vs AMEB | Fixed: G minor in Then; C and G major pentatonic in Further (csx-penta tool there). The book names no exam board (Phase 318) |
| M11 | key signature: 'every line', 줄마다, time signature | Fixed (EN and KO): before the time signature; 오선마다 맨 앞 |
| M12 | whole/half never defined | Fixed: p2 first entry **half step, whole step** with semitone (S) and tone (T) as other names |
| m1 | major pentatonic | Fixed: 'Major pentatonic' / 장조 5음음계 everywhere |
| m2 | melodic down on paper; pad 'up:' | Fixed: figure has a "down:" line; pad prefixes the steps with "up:" |
| m3 | relative minor quick rule | Fixed: "three half steps below C" |
| m4 | the two circles disagree | Fixed: FifthsRing `o.twins` (p5 only) shows B/C♭ and D♭/C♯ with "5♯ 7♭", "5♭ 7♯". Chapter 19 unchanged (ring diff: same) |
| m5 | pad twin line only for G♭ | Fixed: B and D♭ too |
| m6 | p4 key row has no gloss | Fixed: caption under the signatures |
| m7 | why the naming rule works | Fixed: "(its degree 7)" |
| m8 | whole-tone and blues have no tool | Fixed: Later = fifteen signatures, double sharps, chromatic, modes |
| m9 | 반대 방향 | Fixed: 반시계 방향 |
| m10 | dashed T+S segment | Not done: optional; the T+S is named in the steps line and defined on p6 |
| m11 | leading note | Not done: optional, page room |
| m12 | write a key signature | Not in the book: the staff-paper step was removed for design M4 / teaching M2; writing key signatures waits for the Workbook |
| m13 | modes blurb stale | Fixed: "Ionian to Locrian: same notes, a new home note." (EN, KO) |
| m14 | 'whole piece' simplification | Kept, as chapter 19; for her |
| m15 | 5ths run off the keyboard | Fixed: "(or a 4th lower, to stay in the middle)" |
| For her | Technical Work order (A minor at Prelim) vs Music Craft; natural minor not examined | In the report to her |

## Korean

| # | Finding | Done |
|---|---|---|
| B1 | 줄마다, 유효해요 | Fixed (chapter 19's words) |
| B2 | sign parts from its syllable | Fixed: `cbNbKo` (word joiner after ♯♭♮, plus the rules below); used for X5, checks, pad line |
| M1 | 반대 방향 | Fixed: 반시계 방향 everywhere in the book |
| M2 | drop capital splits 모든; orphan 반 | Fixed: opener starts "한 가지 규칙으로"; last pair joined |
| M3 | ㄹ 수 있어요, 조 이름 | Fixed by `cbNbKo` |
| M4 | 온+반 breaks; lone last token | Fixed: word joiners inside 온+반 / T+S, last pair no-break; chromatic "반 걸음 12번" / "12 half steps" |
| M5 | 시계에서 조를 | Fixed: 건반을 |
| M6 | 조를 쳐요 | Fixed: 각 조의 으뜸음을 쳐요; step 2 has its verb |
| M7 | 음의 번호 circular, 음도 missing | Fixed |
| M8 | 한 걸음마다 반 걸음 | Fixed: 반 걸음씩 |
| M9 | tool names 스케일 | Fixed: 장음계 만들기, 화성단음계 만들기 |
| M10 | ladder labels | Fixed: 처음에 / 그다음에 / 더 나아가서 / 나중에 |
| M11 | 선생님이 | Fixed in both languages ("Pick a key", "Cover the key names"); p8 intro no longer assumes a teacher |
| M12 | 2~6쪽 on screen | Fixed: screen says 1~5단계 / steps 1 to 5 |
| m1 | 음이름 | Fixed |
| m2 | lone 반 | Fixed by `cbNbKo` |
| m3 | 코랄색, 요구해요 | Fixed: 산호색; 걸음을 맞추려면 이 두 음이 필요해요 |
| m4 | 장음계 def repeats | Fixed: one sentence (the other names are in the half/whole step entry) |
| m5 | quotes | Fixed |
| m6 | 어느 음에서나 | Fixed: title 어느 음에서나 장음계; the term became 조 (theory M1) |
| m7 | 같은 건반, 두 이름 | Fixed |
| m8 | 만든 조에 표시 | Fixed |
| m9 | 순서, 조 이름 wording | Fixed |
| m10 | 5권/5도 | Fixed |
| m11 | p6 colons | Fixed |
| m12 | 새로운 집 | Fixed |
| m13 | shape names | Fixed (C 반음계; labels from `sh.full`) |
| m14 | older tools: C 장조 / A 단조, 가단조 | Fixed in patch485.py (majName, minName, the order tool, minor-forms blurb) |
| m15 | pad title, note, bracket | Fixed |
| m16 | caption object | Fixed |
| m17 | check 2 fragment | Fixed |
| m18 | p7 rows, intro, panel | Fixed |
| m19 | coins legend | Fixed: a coin key above the ladder ("a major key", "a minor key") |
| m20 | 개념책 | Fixed (one word); 개념서 is for her |
| m21 | build-major tool: 1번째, 처음부 / 터, 이 필요해요 | Fixed (첫 번째 …; nowrap; "F♯ 음이 필요해요") |
| For her | 개념책 or 개념서; 자연 단음계 spacing app-wide | In the report to her |

Extra no-break rules added after a line-break dump of the new build: 이름 둘, 5도 위/아래, 샤프/플랫 + number, a quoted tool name.

## Design

| # | Finding | Done |
|---|---|---|
| B1 | Ladder tool names were dead text on screen | Fixed: `cbScalesPages(scr)` takes the page's own flag (lbScreen() is only valid inside the provider); on screen each tool is a 44 px chip `<a>` (navy-line border, white); 17 links in the ladder plus the Technique chip |
| B2 | p4 frame line through the caption | Fixed: `CbSigs` print maxWidth 220, "key" label 8.5; signs in a MUSIC_FONT tspan |
| B3 | REMEMBER text out of its band at 320 | Fixed in the shared `LbRemember`: under 400 px the row wraps and the text takes the full width (`overflow-wrap:anywhere`); chapters 16 and 19 checked at 320, no overflow |
| B4 | p6/p7 clock labels unreadable | Fixed: `KeyRing` `o.only` + `o.labFs` (the scale's own spelling, 24-26 units), p6 figures 196, p7 200 in a 2 x 2 grid; screen pads use the same labels; unlabelled keys get a faint letter (`ghost`) on screen |
| M1 | p7 half empty, no G♭ pentatonic | Fixed: 2 x 2 grid (major, major pentatonic, G♭ pentatonic, chromatic); fill 0.96 |
| M2 | Coral on the tonic | Fixed: `SscKeys`/`SscStaff` `tonicInk: PEN_N` on p2/p3 and in the p2 pad; coral is left for half steps and the needed sharps |
| M3 | Print text under 11 px | Fixed: ring numbers 17 units navy, p1 rings 290; p3 grid '1.05fr 1.1fr', keys 340, step words 13 (16 split the words onto two rows); `KSStaff` numbers 9.5, #6d6f9c |
| M4 | Too many words a page | Fixed: p3 "same keys, two names" moved to p5; p4 staff-paper step removed; p5 dominant sentence removed; p6 T+S folded into the harmonic-minor entry, "which key?" shortened |
| M5 | p2 shows one idea three times | Fixed: the clock is gone from p2; one column (keys maxWidth 420, H 150: wider spilled the page) with the staff under it |
| M6 | Picture and pad shown twice on screen | Fixed: p2, p6, p7 use `LbLive` (screen shows the pad only); p5's old circle tool replaced by `CbCirclePad` (the book's circle, twins and minors, staff, key line, clockwise/anticlockwise buttons) |
| M7 | Older tools inside the book do not match | Fixed: build-major white with navy-line borders, chips 44, buttons wrap; sharps-order wrapped in a try-box (`CB_BOXLESS`), clef chips 44 |
| M8 | Tap targets under 44 px | Fixed: shapes chips, SscPad Listen/Tap, RH/LH chips, `LbTick` (44 x 44 hit area), FiveChecks buttons, "Got it", Toolbox card buttons |
| M9 | Shape chips one per row | Fixed: 3-column grid, 13 px, wrap |
| M10 | Opener key pad taller than a phone | Fixed: under 560 px a "Clock / Circle" switch shows one ring at a time (maxWidth 300) |
| M11 | p8 separators at line ends; Later row bare | Fixed: separator kept with the next name (nowrap span); Later row has a small circle of fifths, "all 15 keys" |
| m1 | Opener: lone last line | Kept "twelve major keys" (theory M1 asked for "major"); the last pair "whole, half" is joined with a no-break space |
| m2 | p5 ring bands | Fixed: ring maxWidth 380, grid '1.3fr 1fr' |
| m3 | Coral arrows | Fixed: legend arrows and the C → Am icon navy |
| m4 | Korean flats spaced | Fixed: coins use `tnSign`; `CbSigs` key names draw the sign in a MUSIC_FONT tspan |
| m5 | p1 circle without twins | Fixed: `twins` on p1 too |
| m6 | p3 D-major column under-filled | Fixed with M3 |
| m7 | Chromatic ring all coral | Kept: every step of it is a half step, so coral is right by the house rule |
| m8 | Title twice on screen | Partly: the tool kicker is now "Pitch · Concept book" (was the title again); the h2 and the opener title remain |
| m9 | Search button covers content | Fixed (shared): `pb-main` bottom padding 92 px |
| m10 | Toolbox card edges | Fixed: margin '8px 14px 2px', 1 px navy-line border, buttons 44 |
| m11 | 27 px sideways scroll at 320 | Fixed (shared header): the right group wraps; the concept book scrolls 0 px at 320 |
| m12 | "G♭" touches its note box at 320 | Fixed: below 360 px boxes 13 px font, maxWidth 38, wrap |
| m13 | "Fingering →" leaves the book | Not done: in-app routing back to the book (also teach-code m4); the link now keeps the language and a student's lock |

## Teaching and code

| # | Finding | Done |
|---|---|---|
| B1 | Ladder tools are plain text on screen | Fixed (see design B1) |
| B2 | A student link's "Fingering →" opens the teacher view | Fixed: `cbHref` keeps `lang=ko` and `lock=1`; every in-book link uses it |
| M1 | p3 At the piano is a free task | Fixed: set tasks (G major from G with the steps, then F major from F; check each note against its row; next time D, then B♭ major); the table scrolls inside its box on screen |
| M2 | p4 asks for staff paper | Fixed: the step is removed |
| M3 | "Practise in steps" has no move-on rule | Fixed (proposal for her): "Start at First; go up a step when you can show checks 1 to 3 in every key of your step, without the book"; each "what" line names its page |
| M4 | Five checks assume every key | Fixed: "in the keys of your step (page 8 / step 7)" |
| M5 | The keyboard clock is never defined | Fixed: p1 caption is a definition ("one octave's twelve keys in a ring, each place clockwise a half step higher"); the pad note says the same |
| M6 | Minors never shown all at once | Fixed: the p5 circle shows every key's relative minor inside (`FifthsRing o.minors`) with a legend; the circle pad too |
| M7 | Scale table overlaps at 360 px | Fixed: screen table minWidth 300 inside a sideways-scroll box |
| M8 | p4 caption on the frame line | Fixed (see design B2) |
| m1 | Unknown concept book prints a blank page | Fixed: one line, EN and KO |
| m2 | p1 QR opens the teacher view | For her: the chapter books' QRs behave the same way |
| m3 | Two pads can play at once | Fixed: `cbUseOneSound` shares chapter 16's `SSC_STOP`, so any pad stops the last one |
| m4 | No way back to the book from a tool | Not done (routing; with design m13) |
| m5 | Dashboard can't see concept-book progress | For her |
| m6 | Print can make a Korean book; no shelf row | Print now always asks for `lang=en`; the shelf row waits for her (with the duplicate-tool clean-up) |
| m7 | Title three times | Partly (see design m8) |
| m8 | E♯ and B♯ with no help | Fixed: "(E♯ is played on F, B♯ on C)" |
| m9 | Technique note is plain text | Fixed: a chip to the scale finder on screen |
| m10 | Korean flat labels run together on p4 | Fixed (see design m4) |
| m11 | Small ring labels in print | Fixed (see design B4) |

## Round 2 (verifier, `../r2/verify.md`): 104 checked, 97 held

| # | Finding | Done |
|---|---|---|
| Theory M8 (Partly) | Later line pointed at a page with no double sharp | Fixed: "double sharps (G♯ minor’s F𝄪)" / "겹샤프(G♯단조의 F𝄪)" |
| Theory M2, m12 | Record wrong | Corrected above |
| Design M7 (Partly) | build-major beige chip borders, near-black keys | Fixed inside the book: `[data-cb-tool]` chips navy-line, black keys navy (the standalone tool is unchanged) |
| Design M10 (Partly) | Clock sectors 43 px at 320 | Ring takes the whole width and the pad's side padding is 4 px below 360 px; the sectors are 47 x 43 (the box is that narrow) |
| N1 | Screen table hid degree 7 and the count | Fixed: on screen the key column goes (degree 1 is the key, in serif), 13 px; nothing hidden at 320/360/390 |
| N2 | Got it! past its card at 320 | Fixed (shared): below 370 px the three buttons share the row (`fc-btns`); chapters 1, 16, 19 checked |
| N3 | Signs drop in coins and chips | Fixed: the letters sit in one inline span |
| N4 | Order-tool buttons wrap inside their pills | Fixed (shared): the row wraps, the labels do not (`ob-row`); all 44 px tall, one line |
| N5 | Language lost on Back and refresh | Fixed (shared): the address keeps `lang=ko` |
| N6 | p7 bottom lines near the frame | Fixed: figures 186, row gap 4; 26-27 px clear of the box |
| N7 | build-major plays over a pad | Fixed: a step stops the sounding pad (`SSC_STOP`) |
| N8 | Wide ♭ in Korean ring labels | Fixed (shared): ring signs in the music font (`pbAccT`, KeyRing labels, circle labels, counts, minors) |
| N9 | Awkward Korean sentence on p3 | Fixed: "걸음에 맞는 음이 원래 글자의 음과 다르면, …" |
| N10 | Screen drawing words under 11 px | Partly: p3 step words 17 on screen, circle counts 14, shapes-pad labels 30 under 360 px; the key pad's black-key labels and build-major's letters (older tool) left |
| N11 | Later ring letters unreadable | Fixed: `o.bare` draws no letters and is hidden from screen readers |
| N12 | Korean chips split inside the word | Fixed: 자연 / 단음계 break point |
| N13 | Lone last words | Fixed: "page 8", "step 7", "letter once" joined; short Korean brackets kept whole; p4 caption balanced |
| N14 | Twins show one minor | Fixed: all three twins show both minors (G♯m / A♭m, B♭m / A♯m) |
| N15 | English note runs split | Fixed: a run stays whole; a run of five or more may break once, in its middle (a whole run of seven pushed the tick out at 320) |
