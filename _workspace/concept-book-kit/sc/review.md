# Review of t486 Scale finder (independent)

Scripts and screenshots: /home/claude/pbtest/sc/review/ (r1.js spelling dump, r2.js layout audit, r5.js t485 vs t486 text diff, r6.js stamps, r8.js typed queries).

## Verdicts
1 THEORY: spelling, pattern, raised notes, twins, hidden fingers PASS; degree names FAIL (F1), melodic descent not told (F2).
2 KOREAN: 2 findings (F4, F5), rest PASS.
3 LAYOUT: no sideways scroll in any state at 320/390 EN/KO (PASS); findings F6-F10.
4 NOTHING ELSE BROKE: PASS with notes. Chapter 16 and 19 lessons identical text EN/KO; modes, build-major, minor-forms, major-fingering, minor-fingering, build-minor, degree-names, ssc-*, major-shape old links render identical text; no page errors anywhere; stamps share pb_scale_stamps_v1 both ways (seeded C:RH, G:HT, m:A:LH, m:F#:HT show ticked in new section, 2/36 major, 2/36 minor; a new stamp in the section wrote "m:E:RH" to the same key). Toolbox: Scales and keys 24 -> 14, Playing scales and chords 5 -> 2 (scale-finder stays in both through TOOL_ALSO_IN); consistent with the 13 hidden tools. Concept book and cb-p-scales only differ where intended (see F11).

## Theory detail (all 12 minor keys x 3 forms x 1 and 2 octaves, 72 states, via the UI)
- Spelling correct everywhere, each letter once; twins correct: F#/Gb has no Gb row (theory-only), G#/Ab natural G# A# B C# D# E F# G# and Ab Bb Cb Db Eb Fb Gb Ab; harmonic F##/G; melodic E# F##/F G; Bb/A# melodic G A / F## G##; D#/Eb harmonic C##/D, melodic B# C##/C D. Typed queries (a# minor, gb minor, db minor, ab minor, eb minor) land on the right chip.
- Coral: harmonic = 7th only; melodic = 6th and 7th; natural none. Correct.
- Pattern: natural TSTTSTT, harmonic TSTTST+SS, melodic TSTTTTS (up), major TTSTTTS. Correct.
- Hidden fingers: exactly F# melodic, C# melodic, G# natural (both octaves, both hands) and the message appears. Matches brief. G#/Ab melodic and every other state show fingers.
- Melodic heard down as natural: yes in code (playScaleNotes down offsets).

## Findings

### F1 must-fix. Natural minor taught with "leading note"
Where: Degree names panel, minor, natural form. Reproduce: ?teacher=1&tool=scale-finder, Minor, natural minor, Degree names. Shows "7 leading note B♭" (C natural minor), likewise Korean "7 이끎음 B♭". In natural minor the 7th is a whole tone below the tonic, so it is the subtonic (서브토닉 / 버금으뜸음...), not a leading note; a leading note is a semitone below. A child learning from this gets a wrong exam answer. Same panel shows "leading note" for melodic (right) and harmonic (right). Fix: for natural show "subtonic" (and a Korean term in the app's usage), or drop the name for natural 7th.

### F2 should-fix. Melodic "coming down as natural minor" is only heard, never said
Where: melodic form, all keys. The title line, step row ("going up") and notes show only the ascending form; the Hear button silently plays the natural minor down. Nothing tells the child (or the teacher) that it comes down natural. Add a short line such as "coming down: natural minor" (EN/KO), ideally with the descending notes.

### F3 should-fix. Hidden-finger state leaves an empty keyboard and stale help text
Where: F# melodic, C# melodic, G# natural (320/390, EN/KO), shots: /home/claude/pbtest/sc/review/s-en-320-Fs-melodic.png. The two keyboards render with no coloured keys at all, so the scale's notes are not shown on the keys, the 1-2-3 / 1-2-3-4 / start-end legend stays under blank keyboards, and the intro line above still says "Numbers are fingers; the coloured groups start on the thumb". The warning is in alarm red (var(--bad)) like an error. Suggest keeping the notes lit (without finger numbers/group colours), hiding the legend, and a neutral colour. Also "Practise it from your book" assumes a book; fine for Sohyun but check.

### F4 should-fix. Korean "음 이름" for Degree names collides with note names
Where: Degree names chip. The app already uses 음 이름 / 음이름 for note names (C D E; many lesson strings) and calls the old tool "음계 이름". A Korean student will read the chip as note names. Use "음계 이름" or "도수 이름" (the app uses 도수 elsewhere) to match.

### F5 minor. Korean "스텝" vs the app's "걸음"
STEPS label is 스텝; the app teaches steps as 걸음 (26 uses, 장음계의 걸음). Use 걸음 for consistency. Also new strings write 화성 단음계 / 가락 단음계 with a space while scaleTitle, build-minor and several lessons write 화성단음계 / 가락단음계 (5 unspaced uses); the app already mixes, but pick one. Other new strings (단조, 자연/화성/가락 단음계, 온음/반음, 올린 7음, 올라갈 때 올린 6음과 7음, 직접 만들기, 손가락 번호 패턴, 도장, 선법, 으뜸음 list) are natural and consistent. At 320 none of the labels wraps awkwardly; the Korean 가락 단음계 line under the title wraps over two lines ("올라갈 때 올린 6음과 7음: A B") which is acceptable.

### F6 should-fix. Top control row overflows the card at 320
Where: Major | Minor | 1 oct | 2 oct row, 320 px. Card is 246 px wide; "2 oct" ends at 254 px (EN) and "2옥타브" at 265 px (KO), so the last chip is clipped by the card edge (shot m-en-320-Stamps.png, s-ko-320-*). At 390 it fits. t485 was worse (318/307), so not a regression, but the row now has room if the octave chips wrap or the spacer is removed.

### F7 should-fix. Tap targets in the new controls are small
Heights at 320 and 390: "Degree names" chip 21 px (EN) / 23 px (KO), section chips 26 px EN / 28 px KO, form chips about 24 px, Major/Minor 24-26 px, key chips 24 px, all below 40 px. Existing chips share the 24 px size, but the new Degree names switch (21 px, next to the step row) is the smallest and is meant for children.

### F8 minor. Step row reads as "number then its step"
Where: STEPS row (4 columns at 320). The T/S pill sits after the number, so "6 [T+S] 7" can be read as 6 being the T+S. At 320 the pills are tightly packed to the next number in the harmonic row. It is also above the keyboards, not under the keys as the degree numbers are described to be. Consider putting pills between numbers on a line or a small gap.

### F9 minor. Nested boxes carry their own ribbons and titles
Where: Build it, Fingering patterns, Modes sections. Each opens a full box with its own orange "TRY IT" ribbon, own title ("Build it yourself", "The seven modes") and long intro paragraph inside the Scale finder card, so two TRY IT ribbons and two titles on screen (shot M-en-320-Modes.png). Modes ignores the selected key (starts at parent major C). Build it in minor always builds the harmonic minor ("Build a harmonic minor" text) whatever form chip is on; Build it chips wrap to 44 px high rows at 320. Section heights are long on a phone (Stamps 36 cards = about 18 rows).

### F10 minor. Stamps heading wraps awkwardly at 320
"SCALE CARDS: STAMP EACH [0/36] ONE WHEN IT'S SOLID" - the counter sits in the middle of the sentence (shot m-en-320-Stamps.png). The two-column grid itself fits with no overflow.

### F11 minor. Concept book repeats "Scale finder"
Where: ?book=concept&ch=p-scales and ?tool=cb-p-scales, "Practise in steps". The First, Then and Later steps now each show a single "Scale finder" chip, three times in total (Further already had it). Fine as a design, but the three steps then differ only by the key letters; consider a different label per step. Kit link ?kit=scale-finder,ssc-steps,ssc-g still lists the hidden tools (intended).

### F12 minor. Theory-only box disappears for natural and melodic
Where: F#/C# (and A#/G#) in natural and melodic. The dashed "G♭ minor, only on paper" box and its note appear only for harmonic, so switching form makes it vanish without a word. Unlikely to confuse; mention only. Also the intro text ("Type a scale... Numbers are fingers") and the form chips do not use aria-pressed (section chips do).

## Counts
must-fix 1, should-fix 6 (F2, F3, F4, F6, F7 and F5 only if the Korean terms are to be unified; F5 itself is minor), minor 6.
Strict count: must-fix 1 (F1); should-fix 5 (F2, F3, F4, F6, F7); minor 6 (F5, F8, F9, F10, F11, F12).
