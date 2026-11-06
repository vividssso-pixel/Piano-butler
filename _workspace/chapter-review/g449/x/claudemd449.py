#!/usr/bin/env python3
# Phase 449: CLAUDE.md -- rule 8 (the five Cs' names), new rule 11 (Lesson Books floor by floor), the log row.
import sys, re
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
def rep(a, b):
    global s
    if s.count(a) != 1: raise SystemExit('CLAUDE.md: found %d: %s' % (s.count(a), a[:70]))
    s = s.replace(a, b)
rep("read from five Cs -- Sea C, Kingsland C, Clara's C, Queensland C, Sky C (Phase 428);",
    "read from five Cs by their real names: low C, bass C, middle C, treble C, high C (낮은 도, 낮은음자리표 도, 가운데 도, 높은음자리표 도, 높은 도; Phase 449, her 2026-10-12 19:17 '퀸즈랜드, 킹스랜드는 아이디어고 ... middle c, treble c, bass c 그 위로는 high c low c': Queensland and Kingsland are the idea, the two lands, never part of a C's name; no 'Sea C', 'Sky C' or 'Clara's C' any more);")
rep("""   정렬'): the floor plaques, each room's number and name over its picture, the hall's words; one name size and one
   picture height on each floor.
""", """   정렬'): the floor plaques, each room's number and name over its picture, the hall's words; one name size and one
   picture height on each floor.
11. **The Lesson Books are written floor by floor** (her 2026-10-12 19:18 '우리 층층히 바꿨잖아. 레벨별로': the order of
   finishing the Lesson Books follows the levels). Finish every chapter of a level before the next level; inside a level,
   PATH_STAGES order. Done: posture-hands, first-steps, note-names, staff (Level 1); whole-staff, tones (Level 2);
   ledger-lines (Level 3, written early). Next: Level 1's pulse (draft v1, Phase 446, waiting for her answers to G1-G3
   and B1-B11) and note-values; then Level 2's time-signatures, reading-steps, dynamics, pitch-range; then Level 3's
   tempo, rhythm, scales, accidentals (a new chapter), piano-story; then Levels 4 and 5.
""")
ROW = """| 449 | 2026-10-12 | **The five Cs by their real names; the Lesson Books floor by floor.** Her 19:17 '퀸즈랜드, 킹스랜드는 아이디어고 가온도 높은음자리표 도 낮은음 자리표 도는 middle c, treble c, bass c 그 위로는 high c low c 이렇게 정정해줘' and 19:18 (the Lesson Books in level order). patch449.js: Sea C -> low C (C2), Kingsland C -> bass C (C3), Clara's C -> middle C (C4), Queensland C -> treble C (C5), Sky C -> high C (C6); Korean 바다 C -> 낮은 도, 킹스랜드 C -> 낮은음자리표 도, 클라라의 C -> 가운데 도, 퀸즈랜드 C -> 높은음자리표 도, 하늘 C -> 높은 도 (the particles stay: C and 도 both end in a vowel). 135 English and 83 Korean places, each decided on and checked against its list: lower case in sentences and in the name tables (they sit beside 'the King's F'); a capital where a picture's label, a chip or a sentence starts (llCap for the five-C chips). The fold's label in chapters 6 and 7 is 'middle C' in both (chapter 6 said Clara's C). Queensland and Kingsland stay as the lands; the turtle's sea and the bird's sky stay as pictures. The ledger-lines guide page renamed (site449.py) and its three drawings with C labels (five-cs, sky, sea) re-exported; CLAUDE.md rule 8 says the names, new rule 11 the Lesson Book order. Tests: ll431test449 24 and ll444test449 82 (the old A3 'no middle C in chapter 6' and L2's 'no middle C' turned round), ws419 45, sf405 22, lbcheck and wbcheck for chapters 6, 7, 11, 15 pass, all 124 printed books fit. |
"""
m = re.search(r'^\| 448 \| [^\n]*\n', s, re.M)
if not m: raise SystemExit('row 448')
s = s[:m.end()] + ROW + s[m.end():]
open(p, 'w', encoding='utf-8').write(s); print('CLAUDE.md: rule 8, rule 11, log row 449')
