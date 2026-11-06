#!/usr/bin/env python3
# Phase 478: CLAUDE.md: rule 11 (chords built in the macro-first frame; next composers), rule 15 (22 waits for the combined
# review), the log row.
import sys, re
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
def one(a, b):
    global s
    if s.count(a) != 1: raise SystemExit('not found once: ' + a[:60])
    s = s.replace(a, b)
one("Level 4: key-signatures (Phase 474), signs (Phase 475), intervals (Phase 477). Next", "Level 4: key-signatures (Phase 474), signs (Phase 475), intervals (Phase 477), chords (Phase 478). Next")
m = re.search(r"Next chords the same way \(a triad one shape in all 12 keys, then the student's I IV V\);\s+composers, melody; then Level 5\.", s)
if not m: raise SystemExit('rule 11 tail')
s = s[:m.start()] + ("Phase 478 built chords (22) the same way: page 1 is the chord clock\n"
    "   (chapter 16's twelve-key clock with the major triad one triangle, 4 + 3 half steps, turned to any key); the screen\n"
    "   lesson ends with I, IV and V in the student's keys; Workbook page 7 is I IV V I in any key. Next composers, melody;\n"
    "   then Level 5.") + s[m.end():]
one("(key-signatures), 20 (signs) and 21 (intervals).", "(key-signatures), 20 (signs), 21 (intervals) and 22 (chords).")
ROW = """| 478 | 2026-10-17 | **Chapter 22, Chords, built in full in the macro-first frame (her 02:05 '1.2.3. 다동의해', step 3).** The fourth room of Level 4, replacing the 2025 chapter (Phase 117). **Lesson Book** (chbook478.jsx; patch478.py wires it): p1 the chord clock (chapter 16's twelve keys round a circle; the major triad one triangle, root coral, 4 and 3 half steps written on its sides; in print a dashed copy turned to D with an arrow) beside C E G on the staff (root, 3rd, 5th); p2 stack a triad (skip a letter; all lines or all spaces, on either staff; root, root position / 기본 위치); p3 major and minor (a major 3rd, 4 half steps, then 3; minor 3 + 4; the 3rd moves; white keys C F G major, D E A minor; the 3rd coral on the staff and the keys); p4 the tonic triad (C G D F major with key signatures; Roman numeral I); p5 I, IV and V (primary triads; tonic, subdominant, dominant; C and G major); p6 both hands (blocked and broken; RH 1 3 5, LH 5 3 1; bass staff); p7 My five checks. `ChxStaff` (block or broken chords, side words fanned 16 apart, key signatures (bass at x 56), bars, an arrow between places), `ChxKeys` (half steps counted in the keys), `ChxRing`; a triad whose top note would sit above the first ledger line goes down an octave. Korean: 3화음, 근음 / 3음 / 5음, 장3화음 / 단3화음, 으뜸화음, 버금딸림화음, 딸림화음, 주요 3화음, 펼친 화음 (분산화음), 반 걸음 N개 (never 'N 반 걸음'), 1번 / 3번 / 5번 음 (chapter 16's word). **Screen lesson** pads: the clock (tap a key, major or minor), stack (white keys), major or minor (counts), the tonic triad (C G D F, B♭ a screen extra), I IV V (▶ I IV V I), blocked or broken; the extra end step 'My chords' is I IV V in the student's keys (default C G D F). **Drill** 9 levels: 1 stack a triad (letters), 2 name the root, 3 major or minor, 4 write it (tap, or ▲ ▼ and +, then Check; wrong notes red, the right triad green beside), 5 listening: major or minor (screen only), 6 the bass staff, 7 tonic triads: which key, 8 I, IV or V in the student's keys, 9 extra: spell I, IV and V; roots from a shuffled bag. **Workbook** p2–p6, p7 I IV V I in any key (ALL YEAR row), p8 check-up (A root, B draw the triad, C major or minor, D I, IV or V with key signatures; 12 marks); **Teacher copy** 2 pages. Toolbox: chx-clock, chx-stack ('Stack a triad'), chx-mm, chx-tonic, chx-145, chx-hands; the older tools' words follow the chapter (no cake or snowman; 장3화음, 3음, half step; the old triad-stack is 'Root, 3rd, 5th'). Shared fixes: `STEPS_TOTAL_NOW = { chords: 6 }` (an old synced total of 8 no longer keeps chords 'started'); `STEP_EXTRA` (the screen lesson's extra last step is not counted in chapters 16, 19, 21, 22). printables.html: the chapter 22 card's words (the image waits for her combined review). Reviewed by four strict reviewers (theory 20, Korean 24, design 25, code 10 findings; 3 blockers, all fixed) and a verifier (its 2 new blockers and the rest fixed). For her: 근음 or 밑음; reading I IV V as '1도 화음' (left out: chapter 21's 1도 is the unison); the older Major-or-minor tool's face picture. Waits for her combined review. |
"""
m = re.search(r'^\| 477 \| [^\n]*\n', s, re.M)
if not m: raise SystemExit('row 477')
s = s[:m.end()] + ROW + s[m.end():]
open(p, 'w', encoding='utf-8').write(s); print('CLAUDE.md: rules 11, 15; log row 478')
