# Design review r1: concept book "Scales and keys" (print and screen)

Reviewer: print and screen design. Tools: the content harness, scripts in `cb/review/r1/design/`
(`meas.js` print, `screen2.js` screen, `ladder2.js`, `rem320.js`, `tbox.js`, `words2.js`, `fix4.js`,
`say4.js`). Print = `?book=concept&ch=p-scales`, 900 px wide, A4 page 794 x 1123 px (1 px = 0.75 pt).
Screen = `?teacher=1&tool=cb-p-scales` at 390 and 320 px, dsf 1.5, English and Korean.

**Build checked.** Every finding is marked:
- **N** = re-measured on the new 9-page build (`a3/drills.t485.html` 22:57:52, `cb/cbscales.jsx`
  22:57:37, 419 lines: p6 Minor scales, p7 Other scales, p8 the ladder, p9 the checks).
- **O** = measured on the old 8-page build (22:29, `cbscales.r0.jsx`) only. I use O only where the
  component's code is the same in both builds.

Finished books used as the yardstick: chapter 16 (`?book=lesson&ch=scales`) and 19
(`?book=lesson&ch=key-signatures`). They have no content text under 11 px, a picture clearance of
14-15 px to the frame's inner line, and 113-185 words a page.

---

## Blockers

**B1 (N). On screen, the ladder's tool names are dead text.**
- Where: screen step 7 "Practise in steps" (print p8). `cbToolLink` in `cbscales.jsx` lines 112-114.
- What is wrong: all 23 tool names are `<span>`s with no `href`, for example `SPAN 151x19` "The major
  scale's steps". They show as grey words run together. A child cannot tap them, and nothing shows
  that they are tools. The cause is that `cbToolLink` checks `lbScreen()`, but `cbScalesPages` runs
  while `CbScalesLearn` renders, which is outside the `LbScreenCtx` provider (the provider wraps only
  the head and each `LbScreenPage`). So `lbScreen()` returns false.
- Fix: pass the page's own flag.
  `const cbToolLink = (id, scr) => ...` and `scr ? tools.map(id => cbToolLink(id, true)) : ...`.
  On screen, draw each tool as a chip: `minHeight:44`, `padding:'8px 14px'`, `fontSize:14`,
  `fontWeight:800`, `border:'1.5px solid var(--navy-line)'`, `background:'#fff'`,
  `color:'var(--navy)'`, `whiteSpace:'normal'`, gap 8. The current `.chip` class has a beige border
  (#e9e2d2), so set the border inline. Check: `document.querySelectorAll('.cb-ladder a[href*="tool="]').length === 23`.

**B2 (N). Print p4 (English): the frame line strikes through the caption.**
- Where: p4 Key signatures, `CbSigs` (line 154). The caption reads "key: the major key whose key
  signature ends at the sign above it".
- What is wrong: the picture box's inner frame line runs through the caption text. The ink ends 7 px
  below the line (clearBot = -7). The "Sharps:" heading is 7 px from the top line. Korean fits, but
  only with 8 px.
- Fix: in `CbSigs`, change the print width `maxWidth: scr ? 272 : 246` to `scr ? 272 : 220`, and
  change the "key" label in the name row from `fontSize="7.5"` to `"8.5"`. Simulated: 246 gives -7 px,
  232 gives 9 px, 226 gives 12 px (EN). At 220 you get about 15 px top and bottom, and the smallest
  drawing text stays near 10 px. Target: at least 14 px in EN and KO.

**B3 (N). Screen at 320 px: the REMEMBER text runs out of its band.**
- Where: every step's REMEMBER band (`LbRemember`). The worst case is step 4: "From C: clockwise one
  more sharp, anticlockwise one more flat."
- What is wrong: the text column is 84 px wide, so it holds one or two words a line. "Anticlockwise"
  is 114 px wide, so it ends at x 311 while the band ends at 283: a 28 px spill.
- Fix: in `LbRemember`, under 420 px of width, use `flexWrap:'wrap'`. Put the cameo and the
  "REMEMBER" label on the first row and the text below it at `flex:'1 1 100%'`. Add
  `overflowWrap:'anywhere'` as a safety. This is a shared component, so fix it there and check
  chapters 16 and 19 at 320 px too.

**B4 (N). The p6 and p7 clock labels cannot be read on paper or on a phone.**
- Where: `CbShapeFig` → `KeyRing` (`plain`, `pat`), on p6 (3 clocks) and p7 (3 clocks).
- What is wrong:
  - Print p6: black-key labels are 6.0 px (4.5 pt), stacked on two lines ("C♯/D♭"); white-key
    letters are 7.5 px (5.6 pt).
  - Print p7: black-key labels are 8.0 px (6.0 pt).
  - Screen still clocks: black-key labels are 6.8 px at 390 and 6.5 px at 320.
  - The finished books have nothing under 11 px. A 4.5 pt two-line label cannot be read.
- Fix:
  - p6: `CbShapeFig` print `maxWidth` 150 → 196 (3 x 196 + 2 x 18 = 624 px, inside the 632 px inner
    box). Give `KeyRing` an option `o.only` (the scale's own note names) and an option `o.labFs: 26`
    (viewBox units). Label only the notes of the scale, in its own spelling (A B C D E F G♯). Leave
    the other sectors unlabelled; their shading already shows black or white. At 196 px, 26 units is
    about 14 px (10.6 pt).
  - p7: label the same way.
  - Screen: the stills go (see M6), and the pads' clock gets the same `only` labels.

## Must fix

**M1 (N). Print p7: the picture is half empty, and it leaves out the G♭ pentatonic that the page asks for.**
- Where: p7 Other scales, `figs(['major','penta','chrom'], true)`.
- What is wrong: the ink fills 0.47 of the picture's height, with 142 px empty above and 131 px empty
  below (rule 6: no empty middles). At the piano step 2 says "Play G♭ major pentatonic: it is the five
  black keys", but the picture does not show it.
- Fix: a 2 x 2 grid: `gridTemplateColumns:'1fr 1fr'`, `gap:'10px 40px'`, `CbShapeFig` maxWidth 190,
  `LbPic h={520}`. Top row: C major | C major pentatonic. Bottom row: G♭ major pentatonic (black keys)
  | Chromatic, from C. To add it: `{ id:'penta', at:'Gb' }` → `<CbShapeFig sh={penta} k="Gb"/>`. Use
  the B4 labels. Target: ink fill of at least 0.8 and at least 14 px of clearance.

**M2 (N). Coral marks the tonic, which does not need attention.**
- Where: p2 (`SscKeys` circles 1 and 8 filled coral; `SscStaff` notes 1 and 8 and the word "tonic"
  in coral) and p3 (D major circles 1 and 8 coral). The same pattern is in the online pads.
- What is wrong: the house rule is coral only for what needs attention (half steps, sharps and
  flats). On p3, coral now means two different things in one picture: the tonic (1, 8) and the needed
  sharps (F♯, C♯ on 3 and 7).
- Fix: give `SscKeys` an option `o.tonicInk = PEN_N`, used instead of the hard-coded coral for d0 and
  d7 when `nums` is set. On p2's `SscStaff`, set `tonic: false` and keep `tonicLabel` in navy. Coral
  is then left only for "half" and the brackets on p2, and for F♯ and C♯ on p3.

**M3 (N). Content text in print is under 11 px.**
- p1 and p2: the clock's degree numbers are 8.3 / 8.0 px (6.2 / 6.0 pt) in grey #6d6f9c.
  Fix: `KeyRing` number fontSize 12 → 17 units, colour `PEN_N`. Also widen p1's two rings
  `maxWidth` 250 → 290 (the 620 grid still fits; the picture box is 680). That gives about 13.7 px.
- p3: "whole" / "half" under the D keys are 8.5 px (6.4 pt), and the finger and degree numbers are
  9.6 px.
  Fix: `SscKeys` step-word fontSize 12 → 16 units. For the keyboard, change the grid from
  `'0.9fr 1.25fr'` to `'1.05fr 1.1fr'` and the keys' `maxWidth` from 300 to 340, so that "whole" is
  about 12 px. Re-check that the 15-row table still fits.
- p4: the sign numbers 1-7 use #a3a5c2. That colour is off the palette and too pale (about 2.4:1 on
  white).
  Fix: `KSStaff` numbers `fill` → `#6d6f9c` (navy-soft), fontSize 8.5 → 9.5 units.

**M4 (N). Too many words on a page (rule 7: one idea a page, nothing extra).**
- What is wrong: words a page are p1 229, p2 209, p3 362 (including the 135 table cells), p4 271,
  p5 240, p6 308, p7 182, p8 247, p9 115. Chapter 16 has 113-185 and chapter 19 has 117-168.
- Fix (at most three entries a page):
  - p6: drop the entries "T+S" (the harmonic picture already writes T+S) and "which key?" (that one
    can go in the Teacher copy).
  - p3: drop "same keys, two names" (p5's "circle of fifths" entry already names B/C♭, F♯/G♭, C♯/D♭).
  - p4: drop At the piano step 3 (staff-paper drawing belongs in the Workbook).
  - p5: in the "a 5th" entry, delete the last sentence: "Degree 5 of a scale has another name, the
    dominant."
  These cuts also give B2 its room.

**M5 (N). p2 shows one idea three times, and the clock repeats itself.**
- Where: p2. The grid is `'1.55fr 1fr'`: keys (maxWidth 470), staff, and `KeyRing` (270).
- What is wrong: there are three drawings for one rule. The C major clock is the same picture as
  p1's left ring and p7's first clock. Chapter 16's p2 is a single keyboard about 590 px wide.
- Fix: remove the `KeyRing` from p2 and use one column. Keys `maxWidth` 470 → 600 and `H` 180 → 210.
  Put the staff under it at the same width. The step words then grow to about 13 px.

**M6 (N). On screen, the picture and the pad show the same thing twice.**
- p2: the still keyboard, then the `SscPad` keyboard.
- p5: the paper circle of fifths, then the old "Circle of fifths" tool. That is a second circle in a
  different design: a beige ring #f8f3e6, minor keys inside, coral "sharps ↻" next to a navy
  "↺ flats".
- p6 and p7: three still clocks (226 px each, stacked), then the shapes pad with the same clock and
  the same three chips. That is four clocks. Step 5 is 2,725 px tall at 390.
- Fix:
  - p2, p6, p7: `live(still, comp)` → `<LbLive still={still} live={comp}/>`, so the screen shows the
    pad only. This removes about 1,200 px from steps 5 and 6.
  - p5: replace `cbTool('circle-fifths')` with a pad in the book's own style. Take the right half of
    `CbKeyPad`: `FifthsRing` with `onPick` (twins on), the `KSStaff`, and the key line. Do not show the
    still as well.

**M7 (N). The older tools inside the book do not match it and overflow at 320.**
- build-major (p3):
  - It uses a beige background #f5f0e4, near-black keys #1d1c22 and #c9c0aa text.
  - Its key chips are 30-37 x 24 px.
  - At 320, the T, S and Restart buttons sit outside the tool's box (boxOver at 320 in EN and KO).
- sharps-order (p4):
  - It has no try-box frame, so it floats without one.
  - Its clef toggles are 58-64 x 23 px.
- circle-fifths (p5): see M6.
- Fix: these are shared tools, so add a book-mode prop.
  - For each: wrap it in `<div className="try-box" style={actBox}>`, use `#fff` and
    `var(--navy-line)` instead of the beige fills, and make the chips `minHeight:44`.
  - build-major: give the T / S / Restart row `flexWrap:'wrap'` and the keyboard `width:'100%'`.

**M8 (N). Tap targets a child uses are under 44 px.**
- Shapes-pad chips: 40 px tall (`CbShapesPad`, line 97). Fix: `minHeight:44`.
- SscPad "▶ Listen" and "▶ Tap it": 93 x 40 and 89 x 40. Fix: 44.
- "Done" tick boxes (`LbTick`): 24 x 24, 14 of them. "Got it ✓": 75 x 29.
  Fix (shared): a 44 x 44 hit area round the 24 px box (padding 10).
- FiveChecks buttons: 73-79 x 34 (KO 61 x 34). Fix: `minHeight:44`, `minWidth:64`.
- Toolbox card Open / Print at 390: 71 x 40 and 67 x 40. Fix: `minHeight:44` (`CbCard`, lines 415-416).
- The build-major and sharps-order items are covered in M7.

**M9 (N). Screen: the shape chips stack one per row.**
- Where: `CbShapesPad` chips at 390, for example "Natural minor", "Harmonic minor", "Melodic minor".
- What is wrong: each chip sits on its own row, centred. The result is a ragged column 120 px high
  above the clock.
- Fix: `display:'grid'`, `gridTemplateColumns:'repeat(3,1fr)'`, `gap:6`; chips `fontSize:13`,
  `padding:'6px 4px'`, `minHeight:44`, `whiteSpace:'normal'`, `lineHeight:1.15`.

**M10 (O, `CbKeyPad` code unchanged). The opener's key pad is taller than a phone screen.**
- What is wrong: the pad is 1,005-1,022 px tall at 390 (the viewport is 860) and 871-909 px at 320.
  The two rings stack, so the child taps a key and the result is off screen. At 320, the fifths ring's
  sector chord is 39 px and the clock's is 43 px, so the tap targets are under 44.
- Fix: under 560 px, add a two-chip toggle "Clock | Circle" (minHeight 44) and show one ring at a
  time at `maxWidth:300`, with the note row, the staff and the key line under it. Target: the pad at
  700 px or less.

**M11 (N). Print p8 ladder: separators hang at line ends, and the Later row looks unfinished.**
- What is wrong: a "·" is left at the end of a line: "F major and its B♭ ·", "Relative minor ·",
  "Three kinds of minor ·". The Later row has no coins, while the other three rows do.
- Fix:
  - Render each tool as `<span style={{whiteSpace:'nowrap'}}>{j ? '· ' : ''}{name}</span>`, so the
    separator stays with the name that follows it.
  - Later row: in place of coins, a small `FifthsRing` (o.paper, all filled, maxWidth 64) labelled
    "all 15 keys".
- Asked: is the ladder stretched on purpose? Yes: the rows have `flex:'1 0 auto'` and fill the page
  evenly. That is right. Keep it.

## Minor

**m1 (N). Opener, English: the fourth line leaves "keys in order." alone under the drop cap.**
Replacement, tested: it fits in 3 lines beside the drop cap at 19 px.
> Every major scale follows **one rule**: whole, whole, half, whole, whole, whole, half, from any
> note. Its sharps or flats are its **key signature**. The **circle of fifths** puts the twelve keys
> in order.

Korean is already 3 lines. No change.

**m2 (N). Print p5: the ring leaves bands at the top and bottom.** The ink fills 0.72, with 62 px
above and 64 px below. Fix: `FifthsRing` `maxWidth` 340 → 380 and the grid → `'1.3fr 1fr'`.

**m3 (N). Coral is used for arrows.** The p5 legend arrows ↻ ↺ ↓ are coral at 22 px, and so is the
"→" in p9's "C → Am" icon. Fix: `PEN_N` for all of them. Coral stays for half steps and signs.

**m4 (N). Korean flats are spaced and cramped.**
- The coins and the tool line show "B ♭" with a fallback glyph and a gap (p8 coin "B♭", "F장조와 B ♭").
- On p4 the key-name row "F B♭E♭A♭D♭G♭C♭" runs together.
- Fix: set ♭ and ♯ through `sscSx` / `MUSIC_FONT` in `coin()` and in the `CbSigs` name `<text>`
  (as a `<tspan fontFamily={MUSIC_FONT}>`), and change the name spacing from `56 + i * 15` to
  `54 + i * 16`.

**m5 (N). p1's circle of fifths has no twins, but p5's has them.** On p1, D♭ stands alone at 5♭ and
B alone at 5♯. Fix: `twins: true` on p1's `FifthsRing` too, so the two pages agree.

**m6 (N). p3: the D-major column is under-filled.** There are about 90 px of empty space above the
heading and below the caption. This is folded into the M3 grid change (`'1.05fr 1.1fr'`, keys 340).

**m7 (N). p7: the chromatic ring is all coral.** Twelve coral segments read as one alarm. The rule
allows it, since every step is a half step, but it is loud. Option: a navy polygon, with the caption
"12 half steps" in coral.

**m8 (O, code unchanged). Screen head: the title appears twice.** There is a "SCALES AND KEYS"
kicker over the h2 "Scales and keys". Fix: drop the kicker in `CbScalesLearn`'s head, or set the h2
to the book name only.

**m9 (N). Screen at 390: the search button covers content.** The floating search button covers the
pad title "Other shapes, the same clock" and its TRY IT tag on steps 5 and 6, and part of the Later
row's text on step 7. Fix (shared): `padding-bottom: 72px` on the page, and
`scroll-padding-bottom`, or a smaller button inside books.

**m10 (N). Toolbox card at 900.**
- What is wrong: the card's left edge is at x 139, the group header at 132 and the tool descriptions
  at 146: three left edges. It is also the only bordered box in a list of staff-line headers (1.5 px
  navy border).
- Fix: `margin:'8px 14px 2px'` (left edge 146); border `1px solid var(--navy-line)`; buttons
  `minHeight:44` (M8).
- At 390 the card is 346 x 119 and its buttons drop to a second row. That is fine.

**m11 (N). At 320 in English, the page scrolls 27 px sideways.** The teacher header row "TEACHER
VIEW · Dashboard" ends at x 347. The student view and Korean have 0 px. Fix (shared header):
`flexWrap:'wrap'` on that row.

**m12 (O, code unchanged). Key pad at 320: "G♭" touches its note box.** The note boxes are about
31 px wide. Fix: below 360 px, `fontSize` 15 → 13 and `maxWidth` 42 → 38, with `flexWrap:'wrap'`.

**m13 (O, code unchanged). "Fingering →" takes the child out of the book.** The scale finder's back
button then reads "← Toolbox". Fix: add `&from=cb-p-scales` and have the finder show "← Scales and
keys", or open it in place as a tool.

---

## Measurements (new build unless marked)

| Page | Picture box | Ink fill (V) | Clearance top/bottom (px) | Smallest content text | Words |
|---|---|---|---|---|---|
| p1 | 680x401 | 0.77 | 44 / 44 | clock numbers 8.3 px / 6.2 pt | 229 |
| p2 | 680x421 | 0.88 (KO 0.82) | 21 / 27 | clock numbers 8.0 px / 6.0 pt | 209 |
| p3 | 680x402 | 0.87 (KO 0.82) | 26 / 22 | "whole/half" 8.5 px / 6.4 pt | 362 |
| p4 | 680x410 | 0.99 | 11 / **-7** (KO 12 / 10) | "key" 10.8 px | 271 |
| p5 | 680x468 | 0.72 | 62 / 64 | ring labels 11.7 px | 240 |
| p6 | 680x306 | 0.76 | 38 / 30 | black-key labels **6.0 px / 4.5 pt** | 308 |
| p7 | 680x541 | **0.47** | **142 / 131** | black-key labels 8.0 px / 6.0 pt | 182 |
| p8 | none | none | none | "TOOLS" 10 px (label) | 247 |
| p9 | none | none | none | "Not yet" 9.5 px (label) | 115 |

The pages also share these results:
- Overflow is 0 on all 9 pages in both languages, and nothing is clipped inside its SVG.
- The only text overlaps are the kicker and title pairs (house style) and false hits from the tall
  boxes of music-font signs.

Screen, new build:

| | EN 390 | EN 320 | KO 390 | KO 320 |
|---|---|---|---|---|
| Sideways scroll | 0 | **27 px** (teacher header) | 0 | 0 |
| Page height | 17,518 | 20,210 | 16,874 | 19,792 |
| Tallest step | 2,725 (Minor scales) | 3,081 | 2,633 | 3,097 |

- For comparison, chapters 16 and 19 are about 10,600 px tall at 390 (old build).
- Ring sector chord and depth: at 390 the key pad's clock is 57/64 and its fifths ring 51/85; at 320
  they are 43/49 and 39/65. The shapes pad is 50/57 at 390 and 36/41 at 320.
- Smallest screen SVG text:
  - at 390: still clock labels 6.8 px, "whole/half" 7.7 px, "tonic" 7.9 px;
  - at 320: 5.4-6.5 px in places, and a KO "도" label 3.9 px inside an embedded tool.

## Counts

4 blockers (B1-B4), 11 must fix (M1-M11), 13 minor (m1-m13).
