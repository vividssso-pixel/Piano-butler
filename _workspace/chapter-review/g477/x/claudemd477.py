#!/usr/bin/env python3
# Phase 477: CLAUDE.md: rule 11 (intervals built in the macro-first frame; next chords), rule 15 (21 waits for the
# combined review), the log row.
import sys, re
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
def one(a, b):
    global s
    if s.count(a) != 1: raise SystemExit('not found once: ' + a[:60])
    s = s.replace(a, b)
one("Level 4: key-signatures (Phase 474), signs (Phase 475). Next", "Level 4: key-signatures (Phase 474), signs (Phase 475), intervals (Phase 477). Next")
m = re.search(r"Then intervals and chords built the same way \(a triad one shape in all 12 keys, then the\s+student's I IV V\); composers, melody; then Level 5\.", s)
if not m: raise SystemExit('rule 11 tail')
s = s[:m.start()] + ("Phase 477 built intervals (21) in the same frame: the Lesson\n"
    "   Book's first page is the interval ladder (every interval from one note, a 2nd to an octave, counted on the keys);\n"
    "   the screen lesson ends with the ladder in the student's keys, with major and perfect (an extra step); Workbook page\n"
    "   7 is the ladder in any key. Next chords the same way (a triad one shape in all 12 keys, then the student's I IV V);\n"
    "   composers, melody; then Level 5.") + s[m.end():]
one("(key-signatures) and 20 (signs).", "(key-signatures), 20 (signs) and 21 (intervals).")
ROW = """| 477 | 2026-10-17 | **Chapter 21, Intervals, built in full in the macro-first frame (her 02:05 '1.2.3. 다동의해', step 3).** The third room of Level 4, replacing the 2025 chapter (Phases 105/116). **Lesson Book** (ivbook477.jsx; patch477.py wires it): p1 the interval ladder (C to every note up to the octave, harmonic, the keys counted 1 to 8 under it); p2 counting (both notes count, the lower is 1; unison); p3 2nd to 5th in the hand (C position: thumb and finger n make an nth); p4 6th, 7th and octave (odd: line to line or space to space; even: line to space or space to line); p5 melodic and harmonic (a harmonic 2nd side by side, touching, the lower on the left; going down counted from the lower note: D down to B is a 3rd); p6 above the tonic in G major with its key signature (2 3 6 7 major, 4 5 8 perfect); p7 My five checks. `IvxStaff` (pairs: melodic, harmonic, falling, count ladders; o.key draws a key signature and drops signs the key gives; o.bars) and `IvxKeys` (numbers over white keys, or [n, 'sharp'] over a black key). **Screen lesson** pads: the ladder (C G D F chips, tap to hear, ▶ All), Count it, In the hand (C or G position), 6th 7th or octave, Melodic or harmonic, Above the tonic; the extra end step 'My intervals' is the ladder in the student's keys (dashboard keys, default C G D F) with major and perfect. **Drill** 9 levels: 1 count it, 2 together too, 3 in C or G position, 4 write it (tap the staff or ▲ ▼, then Check; wrong red, right green; on paper 'Draw the note'), 5 melodic or harmonic, 6 the bass staff, 7 listening (2nd 3rd 5th octave; screen only), 8 above the tonic in the student's keys, 9 extra: major or perfect; about a third of melodic questions fall. **Workbook** p2–p6 facing the book pages, p7 the ladder in any key (a fresh copy per key, an ALL YEAR row of twelve keys), p8 the check-up on paper (A number, B draw the note above, C melodic or harmonic, D major or perfect above the tonic with the key signature; 12 marks); **Teacher copy** 2 pages (answers, watch-fors, what to say, AMEB/ABRSM placement). Toolbox: ivx-ladder, ivx-count, ivx-hand, ivx-big, ivx-mh, ivx-tonic; Korean tool names follow the chapter (자리, 음이름, 음계). Shared fix: `BoardTrack` returns null under ?print=1, so the printed drill worksheets of chapters 19, 20 and 21 drop the game board (12 boards had made 7 pages). printables.html: the chapter 21 card's words (the image waits for her combined review). Reviewed by four strict reviewers (theory 26, Korean 35, design 32, code 11 findings; 13 blockers, all fixed) and a verifier (9 partly fixed, 18 new, no blockers; all fixed but two). Not changed: the TRY IT badge in Korean (her open question from Phase 476), the older interval-ruler tool's 6 px overflow at 320 px (toolbox pass), SacKeys white-key notches (shared). Waits for her combined review. |
"""
m = re.search(r'^\| 476 \| [^\n]*\n', s, re.M)
if not m: raise SystemExit('row 476')
s = s[:m.end()] + ROW + s[m.end():]
open(p, 'w', encoding='utf-8').write(s); print('CLAUDE.md: rules 11, 15; log row 477')
