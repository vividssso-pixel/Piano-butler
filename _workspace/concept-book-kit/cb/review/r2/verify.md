# Phase 485, round 2: verification of the concept book "Scales and keys"

Build checked: `a3/drills.t485.html`, written 23:49:54. It already has page 7's four clock figures at 193 px.
I read the sources (`cb/cbscales.jsx`, `cb/patch485.py`) and edited none of them.
Every script and picture named here is in `cb/review/r2/` (scripts in `scripts/`, pictures in `shots/`).

## Summary

### Round 1 findings (Fixed or Partly in DISPOSITION.md)

| Side | Checked | Held | Partly | Not fixed | Regressed |
|:-|:-|:-|:-|:-|:-|
| Theory | 26 | 24 | 1 | 1 | 0 |
| Korean | 35 | 35 | 0 | 0 | 0 |
| Design | 25 | 22 | 3 | 0 | 0 |
| Teaching and code | 18 | 16 | 2 | 0 | 0 |
| **Total** | **104** | **97** | **6** | **1** | **0** |

The six Partly: theory M8, design M7, design M10, design m4, teaching M7, teaching m10 (the same fault as design m4).
The one Not fixed: theory m12. It is a conflict between reviewers, not a slip (see its row).

### New findings

| Severity | Count |
|:-|:-|
| Blocker | 0 |
| Must fix | 6 |
| Minor | 9 |

### Must fix, one line each

1. N1. On a phone (320 to 390 px) the scale table on screen step 2 hides degree 7 and the sharps/flats column, with no sign that it scrolls.
2. N2. At 320 px the "Got it!" button of every five-checks row runs past its card (34 px in English, 11 px in Korean).
3. N3. Sharps and flats in the coins and the tool chips drop below the letter; in F♯m and C♯m the sign hangs onto the coin's border (print and screen).
4. N4. The order-of-sharps buttons inside the book wrap inside their pills; in Korean at 320 px they stand one syllable a line, 115 px tall.
5. N5. The app drops `lang=ko` from the address, so Back from any linked tool (and a refresh) shows the book in English.
6. N6. Print page 7: the bottom row's step lines sit about 2.7 px (0.7 mm) above the frame's inner line, in English and Korean.

## How I checked

- Print: every page in English and Korean rendered to PNG (`shots/p-en-1..9.png`, `shots/p-ko-1..9.png`), and the PDF the browser makes (`shots/book-en.pdf`, `shots/book-ko.pdf`, rasterised as `shots/pdf-*.png`). Zoomed crops are `shots/z-*.png`.
- Fit: `scripts/k485.js` (no overflow on any of the 9 pages, both languages; `out-k485b.txt`). Smallest print text per page: `scripts/printtext.js` (`out-printtext.txt`).
- Screen: every step at 390 px in both languages, in 800 px pieces (`shots/c-en390-*.png`, `shots/c-ko390-*.png`); 320 px pieces for steps 2, 3 and 8 (`shots/c-*320-*.png`); 1024 px spot shots (`shots/w1024-*.png`). Checks for sideways scroll, small targets and things past their box: `scripts/screenchk.js` (`out-screenchk.txt`). SVG text sizes on screen: `scripts/svgtext.js` (`out-svgtext.txt`).
- Theory: the 15-row table, the circle with its minors, the three minor forms, the pentatonic and chromatic figures, both clefs' key signatures, and the pads' lines for B, D♭, G♭ and G♯ melodic minor (`out-padlines.txt`).
- Korean breaks: a dump of every printed and on-screen line (`shots/orig/print-lines.txt`, `screen-lines-390.txt`, `screen-lines-360.txt`) and a check that no sign ever parts from its letter or the syllable after it (`scripts/signbreak.js`, `out-signbreak.txt`).
- Shared parts, old build (t484) against new (t485): chapters 16 and 19, the posture and first-steps chapters, build-major, sharps-order, flats-order, at 320 and 390, both languages (`out-regress.txt`, `out-five.txt`). The two rings against chapter 16 and 19 drills: same in all six runs (`out-ringdiff.txt`).
- Sound: every audio source's start and stop time was recorded (`scripts/sound.js`, `sound2.js`, `sound4.js`; `out-sound.txt`, `out-sound2.txt`, `out-sound4.txt`).
- Links: language and lock kept, and the round trip with Back (`scripts/links2.js`, `out-links2.txt`).

## Verdicts on round 1

### Theory

| # | Verdict | Evidence |
|:-|:-|:-|
| B1 | Held | Opener: "Every major scale follows one rule … Its sharps or flats are its key signature." p4: "The sharps or flats of a key". p6 harmonic minor: "It is written as an accidental, never in the key signature." Korean the same (조표에는 넣지 않아요). |
| B2 | Held | p3 "each letter once": "That note can be a white key: F♯ major has E♯, played on F." Korean matches. |
| M1 | Held | p3 entry **key** (조). Opener "from any note", "twelve major keys". p5 "played on the same piano keys". p7 chromatic "Every note, white and black". Key pad note: "Tap a piano key on the clock, or a key on the circle" (`shots/w1024-en-top.png`). |
| M2 | Held | p5 "a 5th": "On the circle every 5th is 7 half steps (a perfect 5th), so a 5th above B is F♯, not F." Korean matches. Note: DISPOSITION says "dominant named". It is not: design M4 deleted that sentence. Nothing to fix in the book; correct the record. |
| M3 | Held | p6 harmonic minor: "Degree 6 to 7 is then T+S: a tone and a semitone, 3 half steps." p7 pentatonic: "Its T+S steps are skips over a letter: E to G, A to C." p2 scale: "A major or minor scale goes step by step, each letter once." |
| M4 | Held | 15 rows in circle order, twins side by side (B/C♭, F♯/G♭, C♯/D♭). Every note and every count checked, all right (`shots/w1024-en-step2.png`, `shots/c-en390-3-1.png`). p5 says "So there are fifteen key signatures." |
| M5 | Held | Legends start "Clockwise from C" and "Anticlockwise from C"; REMEMBER "From C: …". The entry "same keys, two names" ends "Its other name is enharmonic: one sound, two names." (moved to p5, as design M4 asked). Korean 딴이름한소리. |
| M6 | Held | p4 "the major key is a half step above the last sharp". p6 entry "which key?". Check 3 "name the major key from its key signature". |
| M7 | Held | p6: "B♮ (B natural) in C minor"; melodic "(A minor: F♯ G♯; C minor: A♮ B♮)" (`shots/p-en-6.png`). |
| M8 | Partly | Screen: the shapes pad explains F𝄪 when G♯ minor is picked ("F𝄪 is F double sharp: two half steps up from F, played on the key G. Each letter once, so it is not written G." `out-padlines.txt`). Print: the ladder's Later line says "double sharps (Minor scales)", but printed p6 never shows or names a double sharp. Fix: Later text EN `'All fifteen key signatures (The circle of fifths); double sharps (G♯ minor’s F𝄪); the chromatic scale (Other scales); the modes.'`, KO `'조표 15개 전부(5도권), 겹샤프(G♯단조의 F𝄪), 반음계(다른 음계), 선법.'` |
| M9 | Held | p8 Then tools end "Build a harmonic minor"; Further has "Three kinds of minor" (`shots/p-en-8.png`). |
| M10 | Held | Then: "D and B♭ major; A, E, D and G minor", coins include Gm. Further: "the major pentatonic on C and G (Other scales)" with the Five notes tool. |
| M11 | Held | EN "written after the clef at the start of every line of music, before the time signature". KO "오선마다 맨 앞, 음자리표 바로 뒤에, 박자표보다 먼저 적어요. 곡 끝까지, 모든 옥타브에서 효과가 있어요." |
| M12 | Held | p2's first entry is **half step, whole step**, with semitone (S) and tone (T) as other names. |
| m1 | Held | "Major pentatonic" / 장조 5음음계 on the chips, p7 and the figure titles. |
| m2 | Held | p6 figure has "down: A G F E D C B A"; the pad prefixes the steps with "up:" (`out-padlines.txt`). |
| m3 | Held | "three half steps below C". |
| m4 | Held | The circle shows B/C♭ with "5♯ 7♭" and D♭/C♯ with "5♭ 7♯" on p1 and p5. Chapter 19's ring is unchanged (`out-ringdiff.txt`: same in all six runs). |
| m5 | Held | Key pad: "B major: five sharps (F♯ C♯ G♯ D♯ A♯) · the same keys as C♭ major (7 flats)"; D♭ has "the same keys as C♯ major (7 sharps)". Korean too. |
| m6 | Held | Caption "key: the major key whose key signature ends at the sign above it". |
| m7 | Held | "(its degree 7)"; KO "마지막 샤프가 그 조의 7번 음이에요." |
| m8 | Held | Later lists key signatures, double sharps, chromatic, modes. No whole-tone or blues scale. |
| m9 | Held | 반시계 방향 on p5 (legend, At the piano 2, REMEMBER). |
| m12 | Not fixed | DISPOSITION says p4 has an At the piano step 3 (write G and F major's signatures on both staves). Printed p4 has two steps only. Design M4 and teaching M2 removed the staff-paper step. The book cannot both have and not have it. My view: keep it out of the book (rule 3, set tasks only, and no staff paper on the page) and put the writing task in the Workbook when it is built. Correct the DISPOSITION line. |
| m13 | Held | The modes blurb is "Ionian to Locrian: same notes, a new home note." (no "Lydian to Locrian" left in the build). |
| m15 | Held | "each a 5th higher (or a 4th lower, to stay in the middle)". |

### Korean

| # | Verdict | Evidence |
|:-|:-|:-|
| B1 | Held | 오선마다 맨 앞; 효과가 있어요. 유효해 appears nowhere in the build. |
| B2 | Held | `scripts/signbreak.js`: no sign parts from its letter or from the syllable after it, in print or on screen at 320, 360 and 390 px (`out-signbreak.txt`). |
| M1 | Held | 반시계 방향 in the book; 반대 방향 is not in the book (only in other chapters' tools). |
| M2 | Held | The drop capital is 한, a whole word (`shots/p-ko-1.png`). The last pair "온, 반" is joined. |
| M3 | Held | Print lines: "만들 수 있어요", "말할 수 있어요" and "조 이름" stay whole (`shots/orig/print-lines.txt`). |
| M4 | Held | p7 figure "온 온 온+반 온 온+반" on one line; chromatic "반 걸음 12번" (`shots/z-ko7-bottom.png`). |
| M5 | Held | Shapes pad: "모양을 고르고, 시계에서 건반을 눌러 그 음에서 시작해요." |
| M6 | Held | p5: "각 조의 으뜸음을 쳐요"; step 2 has its verb. |
| M7 | Held | "… 다른 이름은 음도예요." |
| M8 | Held | 반음계: "흰건반과 검은건반을 모두 반 걸음씩 가는 음계예요." |
| M9 | Held | Tool names 장음계 만들기, 화성단음계 만들기. |
| M10 | Held | 처음에 / 그다음에 / 더 나아가서 / 나중에. |
| M11 | Held | No 선생님 in `cbscales.jsx`. p3 and p4 steps are set tasks without a teacher. |
| M12 | Held | Screen check page: "7단계에서 내가 있는 단계의 조로, 1~5단계를 …". |
| m1 to m21 | Held (21) | Spot checks in the build: 음이름; 산호색 in the book (코랄색 only once, in another chapter); "조 하나를 한눈에"; "글자를 한 번씩 써서, 어느 음에서나 장음계를 만들 수 있어요" (m17); "샤프 넷, 플랫 넷까지의 장조와 그 나란한조" (m18); coin key "장조 / 단조" (m19); 개념책 one word (m20); "첫 번째 걸음" (m21); the order tool's "샤프 없음 = C장조 / A단조" and the minor-forms blurb "자연, 화성, 가락: A단조로 나란히 비교해요." (m14). The m8 sentence is gone with the old p3 steps. |

### Design

| # | Verdict | Evidence |
|:-|:-|:-|
| B1 | Held | 17 ladder chips plus "Fingering →" and the scale-finder chip are real links, 44 px tall, each keeping `lang=ko` and `lock=1`. (The signs inside them drop: see N3.) |
| B2 | Held | p4 caption sits about 30 px clear of the frame (`shots/z-en4-cap.png`). |
| B3 | Held | No REMEMBER band spills at 320 in the book or in chapters 16 and 19 (`out-regress.txt`, rem empty everywhere). |
| B4 | Held | Print p6 and p7 clocks label only the scale's notes, at 11 px or more (`out-printtext.txt`: nothing under 10.5 px in any picture of p1 to p7). On screen the shapes pad labels are 10.7 px at 390 (were 6.8) and 7.8 px at 320 (were 6.5): see N10. |
| M1 | Held | p7 is a 2 x 2 grid with G♭ major pentatonic; the picture fills 0.94 of its box (`out-k485b.txt`). Its bottom step lines are too close to the frame: see N6. |
| M2 | Held | Degrees 1 and 8 are navy on p2, p3 and the pad; coral is left for half steps and F♯, C♯ (`shots/w1024-en-step2.png`). |
| M3 | Held | Smallest content text in print is 10.5 to 10.9 px (p1 legend arrows, p3 step words 10.8, p7 flats 10.9). Only page furniture (running head 8.6, REMEMBER label 9.5, the not yet/nearly/got it labels 9.5) and the Later icon are smaller. |
| M4 | Held | p3 has two entries; p4 two steps; the dominant sentence is gone; "which key?" is short. |
| M5 | Held | p2 is one column: the keys, then the staff. |
| M6 | Held | p2, p6 and p7 show the pad only on screen; p5 uses the book's own circle pad. |
| M7 | Partly | Held: build-major chips are 44 px tall and wrap; sharps-order sits in a try-box; clef chips 44 px. Not held: build-major chips keep the beige border #e9e2d2 and its black keys are #1d1c22, not the book's navy (`scripts/bmcolors.js`). The order tool's three buttons wrap inside their pills (N4). Fix for the colours: give build-major a book-mode prop that sets chip `border:'1.5px solid ' + BK.line` and black-key fill `PEN_N`. |
| M8 | Held | Shapes chips, Listen, the tick boxes, the five-checks buttons (44 tall, 64 wide) and the Toolbox card's Open and Print (71 x 44, 67 x 44 at 390) all reach 44. The wider check buttons overflow at 320: see N2. |
| M9 | Held | Shape chips in a 3-column grid, 44 px. Korean labels split inside the word at 320 and 360: see N12. |
| M10 | Partly | The Clock / Circle switch works and one ring shows at a time. At 320 the clock's sectors are still 47 x 43 and 43 x 47 px, the same 43 px the round-1 finding asked to fix (`out-screenchk.txt`). Fix: below 360 px let the ring take the pad's full width (`maxWidth:'100%'` instead of 300) and drop the 6 px side padding of the pad, so a sector chord reaches 46 px. |
| M11 | Held | The separator now starts the next name ("· Name the key"); the Later row has the small circle and "all 15 keys" (`shots/p-en-8.png`). |
| m2 | Held | p5 ring 380 wide, grid '1.3fr 1fr'. |
| m3 | Held | Legend arrows and the C → Am icon are navy (`shots/p-en-5.png`, `shots/p-en-9.png`). |
| m4 | Partly | The gap is gone, but `tnSign` now sits inside an `inline-flex` box, so the sign drops below the letter (N3). In Korean print the ring labels still show a wide ♭ with a gap ("B ♭", "E ♭", "G ♭"; `shots/p-ko-1.png`, `shots/z-ko7-bottom.png`): see N8. |
| m5 | Held | p1's circle has the twins. |
| m6 | Held | Folded into M3. |
| m8 | Held | On screen the title shows once: kicker "Pitch · Concept book", then the h2 (`shots/c-en390-top-0.png`). Better than the "Partly" in DISPOSITION. |
| m9 | Held | Scrolled to the bottom at 390 and 900, nothing sits under the search button (`out-fabcard.txt`). |
| m10 | Held | Card buttons 44 px; card links ask for `lang=en`. |
| m11 | Held | The book scrolls 0 px sideways at 320 (old build 27 px; `out-regress.txt`). |
| m12 | Held | Below 360 the note boxes are 13 px, 38 wide, and wrap. |

### Teaching and code

| # | Verdict | Evidence |
|:-|:-|:-|
| B1 | Held | As design B1. |
| B2 | Held | Every in-book link carries `lang=ko` and `lock=1`. A student who follows "Fingering →" stays locked (no tabs) and reads Korean. The finder opens on the chosen key (G♭ opens "F♯ · G♭", D♭ opens "C♯ · D♭"). But Back loses the language: see N5. |
| M1 | Held | p3: "Play G major up from G with the steps, saying each note’s name. Then F major from F." and "Check each note against its row in the table. Next time: D major, then B♭ major." |
| M2 | Held | The staff-paper step is gone. |
| M3 | Held | p8: "Start at First; go up a step when you can show checks 1 to 3 in every key of your step, without the book." Each line names its page by title. |
| M4 | Held | p9 "in the keys of your step (page 8)"; screen "(step 7)". |
| M5 | Held | p1 caption: "one octave’s twelve keys in a ring … each place clockwise a half step higher"; the pad note says the same. |
| M6 | Held | p5 shows every relative minor inside the ring, with a legend line. (Twins show one minor name only: N14.) |
| M7 | Partly | The table no longer overlaps: it scrolls inside its box. But at 390, 360 and 320 the box hides 68, 98 and 138 px: the degree 7 column and the count column, with nothing to say it scrolls. See N1. |
| M8 | Held | As design B2. |
| m1 | Held | `?book=concept&ch=zzz` prints one line: "No concept book called “zzz”." / "“zzz”라는 개념책이 없어요." (`shots/zzz-en.png`, `shots/zzz-ko.png`). |
| m3 | Held | The pads stop each other (key pad, shapes pads, circle pad, chapter 16's pad) and stop when you leave (`out-sound.txt`, `out-sound2.txt`). One older tool inside the book does not join them: see N7. |
| m6 | Held | The card's Print link is `?book=concept&ch=p-scales&lang=en`. |
| m7 | Held | As design m8. |
| m8 | Held | "(E♯ is played on F, B♯ on C)". |
| m9 | Held | The Technique panel has a 44 px chip to the scale finder. |
| m10 | Partly | As design m4. |
| m11 | Held | As design B4. |

## New findings

### N1. Must fix. The scale table on screen hides its last columns
- **Where.** Screen step 2 "Any key" (print p3), the 15-row table. English and Korean. 320, 360 and 390 px.
- **What.** The table has `minWidth:300` inside a box with `overflowX:'auto'`. The box is 232 px wide at 390, 202 at 360 and 162 at 320, so 68, 98 and 138 px are hidden. At 390 the child sees degrees 1 to 6 only. G major's F♯, the note the row is there to show, and every count (1♯ … 7♭) are out of view. Nothing shows that the table scrolls. Step 2's At the piano asks the child to check each note against its row.
- **Evidence.** `out-screenchk.txt` (table hidden 138 / 98 / 68 px, 0 at 1024); `shots/c-en390-3-1.png`, `shots/c-ko390-3-1.png`.
- **Fix.** On screen drop the Key column (degree 1 is the key) and let the table fit:
  - In `CbScaleTable`: `const fs = scr ? 13 : 15;` and `const cols = scr ? 'repeat(7,minmax(0,1fr)) 30px' : '62px repeat(7,1fr) 50px';`
  - On screen, skip the header's 'Key' cell and each row's key cell; give the degree-1 cell `fontFamily:LB_SERIF, fontWeight:900`.
  - Style: `minWidth:0` (not 300). In p3: `overflowX:'visible'` on screen.
  - Check: at 320 every row's last cell's right edge is inside the box, and no cell's `scrollWidth` is larger than its `clientWidth`.

### N2. Must fix. "Got it!" runs past its card at 320
- **Where.** Screen step 8 "My five checks", every row. 320 px. English 34 px past the card, Korean 11 px.
- **What.** The three buttons are each at least 64 px wide with padding and do not wrap (`FiveChecks376` button box `flex:'0 0 auto'`). In this book the card is narrower than in chapters 16 and 19, which fit.
- **Evidence.** `out-five.txt` ("485. en 320 ?tool=cb-p-scales&lock=1 gotit right-past-row 34"; ko 11); `shots/c-en320-9-0.png`.
- **Fix** (shared, safe for the chapters that already fit): in `FiveChecks376` make the button box
  `{flex:'1 1 100%', display:'grid', gridTemplateColumns:'repeat(3,minmax(0,1fr))', gap:4, minWidth:0}`
  and each button `{minHeight:44, minWidth:0, padding:'4px 4px', display:'flex', flexDirection:'column', alignItems:'center', justifyContent:'center', lineHeight:1.1}` (icon above the word). Check chapters 1, 16 and 19 and this book at 320, 360 and 390.

### N3. Must fix. Sharps and flats drop below the letter in the coins and the tool chips
- **Where.** p8 ladder coins (print and screen step 7) and the on-screen tool chips ("G major and its F♯", "F major and its B♭"). English and Korean.
- **What.** `tnSign` uses `verticalAlign` and `lineHeight:0`, which only work in inline text. In `coin()` and in `cbToolLink` the parent is `display:'inline-flex'`, so the sign becomes a flex item: the vertical-align is ignored and the sign sits low. In F♯m and C♯m the ♯ hangs onto the coin's lower border (nothing may touch). E♭, A♭, B♭ flats sit like subscripts.
- **Evidence.** `shots/z-en8-coins.png` (B♭), `shots/z-ko8-coins.png` (E♭, A♭, F♯m, C♯m), `shots/c-en390-8-0.png` (chips and coins on screen).
- **Fix.** Keep the letters in one inline span inside the flex box:
  - `coin()`: `<span ...coin style...><span>{n[0]}{n.length > 1 ? tnSign(n[1] === '♯' ? '#' : 'b') : null}{m ? <span style={{fontFamily:'Inter, sans-serif',fontSize:'0.8em',fontWeight:800}}>m</span> : null}</span></span>`
  - `cbToolLink`: `<a ...>{<span>{cbSx(tl.title)}</span>}</a>`
  - Check the zoomed coins: the sign's bottom sits above the coin's inner edge with at least 2 px.

### N4. Must fix. The order-of-sharps buttons wrap inside their pills in the book
- **Where.** Screen step 3 "Key signatures", the embedded Order of sharps tool. 320, 360, 390 px.
- **What.** "− One off", "+ Next one", "▶ Play" each break inside the pill: 73 px tall in English at 320 to 390 ("− One / off", "▶ / Play"). In Korean at 320 they stand one syllable a line, 115 px tall ("하 / 나 / 빼 / 기", "재 / 생"); at 360 "재 / 생" still splits the word. The standalone tool is unchanged from t484 (56 to 60 px at 320), so this comes from the book's narrower try-box.
- **Evidence.** `out-kochips.txt`; `shots/sobtn-ko320.png`, `shots/c-en390-4-1.png`.
- **Fix.** In the order builder's button row (shared tool): row `flexWrap:'wrap', justifyContent:'center', gap:6`; each button `whiteSpace:'nowrap', wordBreak:'keep-all', flex:'0 1 auto', minHeight:44`. The row then wraps to two lines instead of the labels. Check the book and the standalone tool at 320, 360, 390 in both languages: each button one line, 44 to 48 px tall.

### N5. Must fix. The language is lost on Back and on refresh
- **Where.** Any link out of the book (ladder chips, "Fingering →", the scale finder chip), student and teacher. Korean.
- **What.** The links carry `lang=ko`, and the tool opens in Korean. But the app's address sync rebuilds the query without `lang`. The address of the book itself becomes `?tool=cb-p-scales&lock=1`. Browser Back then opens the book in English, and so does a refresh. A Korean child leaves the book for one tool and comes back to English.
- **Evidence.** `out-links2.txt`: fresh link `?tool=cb-p-scales&lock=1&lang=ko` becomes `?tool=cb-p-scales&lock=1`; after Back `{"ko":false,"en":true}`; the same for a teacher who switched to Korean.
- **Fix.** In the App's address-sync effect (the one ending `history.replaceState(null,'',location.pathname+'?'+p.toString()+location.hash)`), after `if(st.lock)p.set('lock','1');` add `if(lang==='ko')p.set('lang','ko');` and add `lang` to the effect's dependency list. Check: open the book in Korean, follow a chip, press Back: the book is still Korean; refresh: still Korean.

### N6. Must fix. Print page 7: the bottom step lines nearly touch the frame
- **Where.** Print p7 "Other scales", the bottom row of the 2 x 2 grid. English and Korean.
- **What.** After the 193 px change nothing is clipped, but the last lines ("T T T+S T T+S" and "12 half steps"; Korean "온 온 온+반 온 온+반" and "반 걸음 12번") end about 2.7 px (0.7 mm) above the frame's inner line. On paper they read as touching.
- **Evidence.** `shots/z-en7-bottom.png`, `shots/z-ko7-bottom.png` (and the PDF raster `shots/z-pdf-en7-bottom.png`, `shots/z-pdf-ko7-bottom.png`).
- **Fix.** The page has no free space left (`out-k485b.txt`: page 7 free 0), so make room inside the picture: set the four `CbShapeFig` figures to 186 px (the rings get about 7 px shorter in each row, which lifts the bottom row's text by about 14 px), or keep 193 px and cut the grid's row gap to 2 px and the space between each figure's title and its ring. Target: at least 10 px between the lowest text and the frame's inner line, page 7 still 0 overflow, ring labels still 11 px or more.

### N7. Minor. The build-major tool plays over a pad's scale
- **Where.** Screen step 2, the embedded Build it yourself tool.
- **What.** Press Listen on any pad, then T or S in build-major: its notes start at once while the pad's scale keeps playing (52 notes of the shapes pad still to come). The new pads stop each other and stop build-major, but build-major does not stop them. The order tool's Play makes no sound, so it is fine.
- **Evidence.** `out-sound4.txt`.
- **Fix.** In build-major's note player call the shared stop first: `if (typeof SSC_STOP === 'function') SSC_STOP();` (or register it with `cbUseOneSound`) before each note.

### N8. Minor. Korean print: the ring's ♭ is wide, with a gap
- **Where.** Korean print p1 and p5 (FifthsRing labels and counts: "B ♭", "E ♭", "1 ♭", "♭ 많아짐") and p6, p7 (KeyRing labels "G ♭"). Chapter 19 shares the ring.
- **What.** The sign is drawn in the Korean font, which has a wide ♭. English is tight. This may depend on the fonts of the machine, but CbSigs already fixed the same thing with the music font.
- **Evidence.** `shots/p-ko-1.png`, `shots/z-ko7-bottom.png`.
- **Fix.** In FifthsRing and KeyRing labels, draw ♯ and ♭ in a `<tspan fontFamily={MUSIC_FONT}>`, as `CbSigs` does. Re-run `out-ringdiff` (chapter 19 must stay the same apart from the glyph).

### N9. Minor. Korean p3: an awkward sentence
- **Where.** p3 "each letter once" (글자는 한 번씩), print and screen.
- **What.** "걸음을 맞추려면 원래 글자와 다른 음이 필요할 때, 그 글자에 샤프나 플랫을 붙여요." mixes "in order to" and "when".
- **Fix.** `'걸음에 맞는 음이 원래 글자의 음과 다르면, 그 글자에 샤프나 플랫을 붙여요.'`

### N10. Minor. Screen drawings: words under 11 px
- **Where.** Screen. Step words under the keys (step 1 pad and step 2 keys): 8.4 to 8.5 px at 390, 5.8 to 6.2 px at 320. Circle pad counts (0, 1♯ … 5♯ 7♭): 8.5 / 6.2 px. Shapes pad labels at 320: 7.8 px. Key pad black-key labels at 320: 8.9 px. Build-major letters 7.6 / 5.5 px (Korean 도 5.3 px).
- **Evidence.** `out-svgtext.txt`.
- **Fix.** On screen raise the drawing font sizes in viewBox units: `SscKeys` `stepFs` 16 → 22 when `lbScreen()`; FifthsRing count `fontSize` up by 40 percent when `o.scr`; KeyRing `labFs` 26 → 30 below 360 px. Target: 11 px or more at 390, 9 px or more at 320.

### N11. Minor. The Later row's small circle
- **Where.** p8 ladder, Later row (print and screen).
- **What.** The 38 px circle has `role="img"` and no name, and 12 letters at 1.5 to 2.1 px that nobody can read.
- **Evidence.** `out-printtext.txt` (p8: 1.5 to 2.1 px), `scripts/mini.js`.
- **Fix.** Draw it without letters (`o.bare` should drop the labels) and mark it `aria-hidden="true"`; the words "all 15 keys" sit beside it.

### N12. Minor. Korean shape chips break inside the word
- **Where.** Screen steps 5 and 6, shapes pad chips. Korean, 320 and 360 px.
- **What.** "자연단 / 음계" at 320 and "자연단음 / 계" at 360 (also 화성단음계, 가락단음계).
- **Evidence.** `shots/kochips-ko320.png`, `shots/orig/screen-lines-360.txt`.
- **Fix.** Give the Korean labels a set break point: render `자연<wbr/>단음계`, `화성<wbr/>단음계`, `가락<wbr/>단음계` with `wordBreak:'keep-all'`. Check 320 and 360: "자연 / 단음계" or one line.

### N13. Minor. Lone last words
- **Where and what.**
  - EN p9 intro: "(page / 8)." (`shots/p-en-9.png`). EN check 2 on p9: "once" alone on its line.
  - KO p8 Further text: "(다른 / 음계)." (`shots/orig/print-lines.txt`).
  - KO screen p4 caption at 360: "… 끝나는 / 장조".
- **Fix.** EN: write `page 8` and `letter once`. KO: in `cbNbKo` add `.replace(/\(([^()]{1,8}) ([^()]{1,8})\)/g, '($1 $2)')` (a short bracketed name stays whole). The p4 caption on screen: `textWrap:'balance'`.

### N14. Minor. Twin keys show one relative minor
- **Where.** p5 circle and the circle pad.
- **What.** B/C♭ shows G♯m only and D♭/C♯ shows B♭m only, while F♯/G♭ shows both D♯m and E♭m. The book says there are fifteen key signatures, so C♭ major's A♭m and C♯ major's A♯m are missing. All the minors shown are right.
- **Fix.** Show both names for all three twins (`FIFTHS_MINOR` B: G♯m / A♭m, D♭: B♭m / A♯m), small, as at the bottom; or show one name for all three and say so in the legend. The first keeps the circle consistent with "fifteen".

### N15. Minor. English note-name runs split across lines on screen
- **Where.** Screen step 3, At the piano 1, English: "F♯ C♯ / G♯ D♯ A♯ E♯ B♯" at 320 and "F♯ C♯ G♯ D♯ A♯ E♯ / B♯" at 390.
- **What.** Korean keeps note runs whole (`cbNbKo`), English does not.
- **Evidence.** `out-enorder.txt` (from `scripts/dbg-order.js`).
- **Fix.** Add the Korean rule to the English path used by `X` and `X5`: `.replace(/(?<![A-Za-z])([A-G][♯♭♮]?) (?=[A-G][♯♭♮]?(?![A-Za-z]))/g, '$1 ')`.

## Checks with no finding

- **Theory.** All 15 major scales in the table, spelled each letter once, with the right number of sharps or flats; the three twin pairs. The circle: 12 major keys in fifths order, counts 0 to 7 both ways, every relative minor right. Natural, harmonic and melodic minor on A (steps, half steps on the clocks, the way down). G♯ melodic minor on the pad: G♯ A♯ B C♯ D♯ E♯ F𝄪 up, natural minor down. Major pentatonic C D E G A, G A B D E, G♭ pentatonic = the five black keys. Chromatic = 12 half steps. Key signatures: the order F C G D A E B and B E A D G C F; all 28 sign positions on both clefs, checked by eye on p4. No exam board named.
- **Print fit.** All 9 pages fit in English and Korean, nothing over the page (`out-k485b.txt`), and the PDF matches the PNGs. The p4 caption is clear of the frame.
- **Screen.** No sideways scroll at 320, 360, 390 or 1024 in either language (`out-screenchk.txt`). The opener's Clock / Circle switch works. No page errors and no database calls in any run.
- **Shared parts.** Chapters 16 and 19 (`?drill=scales`, `?drill=key-signatures`): no change from t484 at 320 and 390 apart from the header, which no longer scrolls sideways at 320 (was 27 px). REMEMBER bands: no spill anywhere. Five-checks rows in chapters 16 and 19: fit, now 44 px tall. Build-major and order tools standalone: same as t484. Page header: wraps at 320. The two rings against both chapters' drills: same (`out-ringdiff.txt`). Posture and first-steps at 320: their 6 px and 1 px overflow are older than this phase (also in t484).
- **Links.** All 19 links out of the book keep `lang=ko` and `lock=1`; a locked student stays locked; the scale finder opens on the chosen key; the Toolbox card's Print link asks for English.
- **Sound.** One sound at a time among the book's pads and chapter 16's pad; every pad stops when you leave the book. The order tool's Play is silent.
- **Words.** No double dash in reader text; no teacher assumed; colours: navy, coral only for half steps, needed signs and "the key looked at"; green only on Got it!.
- **Not reported (environment).** Faint horizontal lines under long Korean titles in the sandbox PDF also appear in chapter 16's Korean book (t484) and come from the sandbox's fallback font.
