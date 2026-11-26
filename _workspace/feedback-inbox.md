# Feedback inbox (from the overseeing window)

Her 26 Nov 2026 ("도서관창에서 볼 수 있게 실시간 피드백"): one window builds (the Library / Read & listen window), another checks
behind it and writes here. **The building window reads this file before every build**, fixes the open items it can,
ticks them (`[x]`, with the commit hash) and leaves items marked *Her call* until she answers on the board
(Curriculum Plan doc, tab 전체 지도). New feedback is added at the top of "Open", newest first.

## Audit checklist (for any reviewer)

For every new picture (first, middle and last frame) and page: music facts (British names: semibreve, minim, crotchet, quaver;
bar lines, rests, key and time signatures, scales, chords, terms); sound matches picture; house colours (navy #26296b and
coral #e4572e; green only for correct or practised; pink only for Clara); no overlapping or clipped text; spelling;
public-domain melodies only. Report only clear problems: file, what is wrong, the fix. Taste questions go under 'Her call'.

## Open

### Note Writer Books 2, 3, 4 (65 pages each), self-audit of 26 Nov (two fresh reviewers)

Fixed in this build (`_workspace/note-writer/`, not committed)
- [x] Write it: a letter could mean two octaves on one staff: every name once per row pool (new notes first; ledger notes in Book 3); answers unambiguous.
- [x] "C needs its own little line" was wrong outside middle C: now "notes above or below the staff need their ledger lines".
- [x] Odd one out was visual only: the pair is the same name in two octaves; in Book 4 the odd one is often the same letter with another sign (F against F sharp).
- [x] Frère Jacques fingering: G A G F E C = 4 5 4 3 2 1; repeated "right hand from middle C" removed.
- [x] Grand-staff tunes: a whole-bar rest on the staff with no notes.
- [x] Book 4: step/skip notes overlapped after the key signature (three boxes a row, room for signs); signs touched the clef or the note before (notes with a sign move right; two odd-one-out boxes a row); week 4 Which key lacked the new notes F sharp and B flat; the check-up drew a grand staff for a bass-only term (now one staff, right instruction).
- [x] Treble clef clipped at the top of a staff (all books); keyboards redrawn in proportion (white key about 3.6 times as long as wide).

Her call (do not change until she answers)
- [ ] Book 3 week 7 grand staves are close (3 spaces): treble A3 and bass C4 sit at the same height. Widen?
- [ ] Staggered name boxes under dense tune lines: OK for children?
- [ ] Hot Cross Buns quavers beamed in pairs (by beat) or in fours?
- [ ] Book 4: Ode to Joy in F appears in weeks 2 and 6; the naturals week tune (Hot Cross Buns in D) has no natural.

### Note Writer Book 1 (Term 1, 65 pages), self-audit of 26 Nov (a fresh reviewer, every page)

Fixed in this build (`_workspace/note-writer/`, not committed)
- [x] Time signatures sat half a space low (old-style figures) and touched the bass clef's dots: lining figures, centred, moved clear.
- [x] Notes ran into the clef in the step/skip and odd-one-out boxes; the treble clef stuck out of the box: clef and notes moved in, room above.
- [x] Grand staff Write it: F and G could not be told apart (two of each): a small clef in the box, the answers mark the staff; no same letter side by side.
- [x] Week 9 secret words had nothing left to do: BADGE added.
- [x] No brace on the grand staves: added.
- [x] Tune name boxes touched under dense bars: they take turns on two rows when a line is too tight for 10 mm boxes.
- [x] Empty areas (grand-staff Day 4 and Day 5): twelve step/skip pairs; rows spread to the foot; nothing overflows (fit.py measures every page).
- [x] "(C = 1, B" broke across lines: no-break spaces.
- [x] Step/skip boxes on the grand staff were different heights and overlapped: one height for all.

Her call (do not change until she answers)
- [ ] Rests in the empty staff of the both-staves tunes (weeks 7 to 9)?
- [ ] Games: odd one out in weeks 1, 3, 4, 6; secret words in weeks 2, 5, 7, 8, 9. Keep that balance?
- [ ] Day 4 on the grand staff is steps and skips only (12 pairs); weeks 1 to 6 also have 20 names. OK?

### Picture lesson, Pitch and Rhythm — self-audit of 27 Nov (72 pictures: first, middle and last frame; a fresh reviewer; sound not heard)

Fixed (3c80b45)
- [x] **LP-P6-1**: ledger lines were hidden behind the note; they now stick out both sides.
- [x] **LR-T3-2**: the caption named a dotted quaver that was not drawn; it is drawn now (three quarters of a beat).
- [x] Pale-key letters (LP-O1-0, P1-2, P2-2, P4-0, P9-0, P10-1, P10-3): navy on pale keys.
- [x] **LP-P7-1**: Clara is pink; the other children coral and navy. **LP-P9-1**: bottom captions larger and off the edge. **LR-T4-2**: beat numbers larger and clear of the sparks.
- [x] Colours: Pitch and Rhythm now follow navy and coral too (green and gold were used as category colours).

Should fix (looks) — open, next build
- [x] (a968203) **LP-P5-0**: the note A and its letter sit on the "treble G" label, which is written across the staff lines. Move the label clear.
- [x] (a968203) **LP-P6-2**: "below the treble" / "above the bass" are written across the staff lines.
- [x] (a968203) **LP-P7-0** (last): the bottom caption repeats the title and only one black key is lit. End with two neighbouring keys lit; drop one line.
- [x] (a968203) **LP-P8-0** (first): "♭ = next key left" and "♯ = next key right" collide in the top-left corner.
- [x] (a968203) **LR-T2-5** (last): the earlier staff and rest labels are still faintly visible behind the new picture.
- [x] (a968203) **LR-T5-1**: the coral weight does not stay on the pendulum rod as it swings.
- [ ] **D-crotchet, D-semibreve, D-semiquaver** (old demo page only): the word label is cut off by the first circle.

Her call
- [ ] **LP-P4-0**: "only Middle C sits between the two staves": B and D sit in that gap too. Safer: "Middle C sits on its own line between the two staves"?
- [ ] **LR-T1-7**: "one beam: quavers" is paired with just "two beams". Add ": semiquavers"?
- [ ] **LR-T12-1**: the caption says "the orange note"; elsewhere the colour is called coral.
- [ ] **LR-T3-0 / T3-1** and **LR-T2-5 / T2-6**: each pair shows almost the same picture. Keep both?

### Picture lesson, Bars and time to Before you play — self-audit of 26 Nov (119 pictures: first, middle and last frame; a fresh reviewer; sound not heard)

Fixed in this build
- [x] Pale-tinted keys lost their letters (LC-H2-0, H2-1, H6-0, H7-0, H8-0, H9-0, H9-1, M1-0, M2-0, M3-1, LE-S2-1, LS-L5-0): the letter is now navy on a pale key.
- [x] LC-H10-0, LC-H9-0: keyboard moved off the right edge. LC-M6-0: caption clear of the circle. LS-O8-0: long tile text made smaller. LS-G1-1: "look at how it moves".
- [x] LC-H4-0: in the A minor part the row shows minor-key numerals (i, iv, V).

Must fix (music facts)
- [x] (3b18ee1) **LB-T10-1** (Upbeats, last frame): the last bar is counted 1, 2 but holds one crotchet; the second seat is empty. Fill it (or show a rest) so 1 + 2 = 3 works, as in LB-T10-2.
- [x] (3b18ee1) **LB-T7-0** (Compound time, last frame): the row "count: 1 · · 2 · ·" does not line up with the bananas and stops after two beats. One mark under each banana, through all four beats, or cut the row.

Should fix (looks)
- [x] (3b18ee1) **LB-T10-0 / -1 / -2**: beat numbers 1 and 3 sit on the carriage wheels. Move them below the wheels.
- [x] (3b18ee1) **LB-T6-3**: the 4/4 → 3/4 on the small stave is tiny and the lines run through the digits. Enlarge.
- [x] (3b18ee1) **LB-T7-5**: the coral ring round the 8 cuts the bottom of the 6.
- [x] (3b18ee1) **LB-B3-2**: the D.S. arrow runs through "segno (the sign)" and "D.S. al Coda". Raise the arc.
- [x] (3b18ee1) **LE-E6-0**: the train ends touching the right edge. Stop it earlier.
- [x] (3b18ee1) **LE-E9-0**: "E: above" sits on the stave. Move it clear.
- [x] (3b18ee1) **LE-E5-5**: the navy shapes look clipped (tops of circles only); the metronome marks are very small.
- [x] (3b18ee1) **LE-S6-0 / LE-S6-1**: the 6 sits on the bottom edge and has no sharp/flat sign; outside labels are small.
- [x] (3b18ee1) **LE-O4-0**: the tile "Slowing down, speeding up" fills its box edge to edge.

Her call (do not change until she answers)
- [x] (a9014ca) **Colour in the picture lesson**: green, gold and purple are used as category colours in most new pictures too (bass notes, minor chords, left hand, form letters, periods, chord flavours). Same question as "Colour" below; one answer covers both. → Her 26 Nov: "색깔은 그 전이랑 같이" — navy and coral as before. All 119 lesson pictures re-rendered; green only on ticks.
- [x] (a9014ca) **LS-L5-0**: the octave song is named "Somewhere over the Rainbow" (1939). The clip plays only the two notes C to C, not the tune. Keep the title, or pick a public-domain octave song? → Her 26 Nov: OK, keep the title.
- [x] (a9014ca) **LB-T8-3**: "five-four: from Grade 5" — check against the syllabus. → Her 26 Nov: take the grade wording out. Line removed from the picture and from the lesson audio.
- [x] (a9014ca) **LB-B3-0**: the caption says "jump back at the sign" under a D.C. al Fine map with no segno; "the sign" may be misread. → Her 26 Nov: ok. Caption now "go back · stop at Fine · or jump to the Coda".
- [x] (a9014ca) **LB-T7-4**: title "feel two beats, on 1 and 4" but the numbers under the beats are 1 and 2. → Her 26 Nov: ok. Title now "feel two big beats in the bar".
- [x] (a9014ca) **LE-E3-7**: marcato wedges are drawn under the note heads; in print they normally sit above. → Her 26 Nov: ok. Marcato wedges now sit above the notes.

### Library picture books — audit of 26 Nov (82 pictures: first, middle and last frame of each; sound not yet heard)

Must fix (music facts)
- [x] (15b67d4) **R-bars** (Bars and time): a double bar line stands between bar 3 and bar 4. It should be a single bar line; the double (final) bar line only at the end.
- [x] (15b67d4) **R-rests** (Rhythm): the semibreve rest and the minim rest are drawn with no staff line, so they look the same. Draw them on a line: the semibreve rest hangs below it, the minim rest sits on it.
- [x] (15b67d4) **S-minor** (Scales and keys): the staircase is the harmonic minor (B natural, A♭–B a tone and a half) but the label says only "C minor". Either label it "C harmonic minor" or draw the natural minor (B♭).

Should fix (looks)
- [x] (15b67d4) **E3-a / E3-l / E3-s** (The kitchen, legato): the monkey-bars frame runs over the "Chef Pepe" name under the portrait.
- [x] (15b67d4) **E5-all** (The kitchen, tempo race): at the end the fast animals have wrapped back to the start, so you cannot see who arrived first. Stop each animal at the finish line.

Her call (do not change until she answers)
- [x] (a9014ca) **Colour**: yellow and green are used as category colours in F-form (A B C), F-texture (three lines), H-inv (C E G), H-seventh (the 7th), R-dots (the dot's beat), P-semi (tone) and L-nerves (captions). The house rule is navy + coral, green only for correct. Keep if this follows the Handbook's own colour code; otherwise navy and coral tints. → Her 26 Nov: navy and coral as before. F-form, F-texture, H-inv, H-seventh, R-dots, P-semi, L-nerves recoloured.
- [x] (a9014ca) **L-ears**: the octave example is "Somewhere over the Rainbow" (1939, still in copyright). Naming the title is fine; check that the picture or its clip does not play the melody, or choose a public-domain octave song. → Her 26 Nov: OK, keep the title (the clip plays only the two notes).

## Done

(none yet)
