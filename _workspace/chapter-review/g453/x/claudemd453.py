#!/usr/bin/env python3
# Phase 453: CLAUDE.md -- her answers of 2026-10-13 13:22 as rules (Korean middle C, counting with +, the theory plan,
# the house later), and the log row.
import sys, re
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
def rep(a, b):
    global s
    if s.count(a) != 1: raise SystemExit('CLAUDE.md: found %d: %s' % (s.count(a), a[:70]))
    s = s.replace(a, b)
rep("Queensland and Kingsland are the idea, the two lands, never part of a C's name; no 'Sea C', 'Sky C' or 'Clara's C' any more);",
    "Queensland and Kingsland are the idea, the two lands, never part of a C's name; no 'Sea C', 'Sky C' or 'Clara's C' any more; middle C in Korean stays 가운데 도, not 가온 도: her 2026-10-13 '가운데 도가 아무래도 알기 편한듯');")
rep("""   tempo, rhythm, scales, accidentals (a new chapter), piano-story; then Levels 4 and 5.
""", """   tempo, rhythm, scales, accidentals (a new chapter), piano-story; then Levels 4 and 5.
12. **Counting is written with + for 'and'** (her 2026-10-13 G2: 'walk, running, 그러고 박자표에 맞게 박자세기 1 2 3 4,
   1+2+3+4+, 1e+a 2e+a ... +은 and 이야 내가 저렇게 표기해'). Beats: 1 2 3 4; quavers: 1 + 2 + 3 + 4 +; semiquavers:
   1 e + a 2 e + a, always as the time signature counts (2, 3 or 4 beats). In words the + is read 'and'. Her ways in to a
   steady beat: walking and running. Her two pulse faults (G1): not keeping the count steady; playing the first beat and
   starting the count too late.
13. **Theory still to come, room by room** (her 2026-10-13 '너 추천따를께 책바탕 기반으로', after the gap list of 2026-10-12
   against AMEB/ABRSM grades 1-5): each goes into its room's Lesson Book when that book is written, as a higher drill
   level when it belongs to a later grade. Note values: the breve, double dots. Time signatures: anacrusis (today a
   Rhythm tool), 2/8 4/8 4/2 6/4 9/4 12/4, irregular 5/8 7/8 7/4. Scales: pentatonic (named), whole-tone, blues. Intervals:
   compound intervals. Chords: the augmented triad, ii and vi, the cadential 6/4 (Ic), passing and auxiliary notes,
   recognising a modulation. Clefs: the tenor clef; transposing between clefs; transposing instruments and concert
   pitch. Terms: French and German terms. Form and styles: suite, minuet and trio, scherzo, theme and variations,
   recitative and aria; ostinato; canon and imitation; the orchestra's families and their clefs. A new room on Level 5,
   'Writing music' (음악 쓰기): rhythm to words and word stress, a melody from a rhythm or an opening, cadences and a
   harmonised melody in SATB. The house's floor-by-floor reveal is decided once every book is built ('일단 다 만들고
   정하자').
""")
ROW = """| 453 | 2026-10-13 | **Guide pages: no long dashes, short paragraphs; her answers as rules.** Her 13:22: '예전 가이드 페이지에 남은 긴 대시(—)를 지울지 응 지워줘 그리고 문단마다 읽기 쉽게'. All seven guide sources (index, first-steps, posture-hands, note-names, staff, ledger-lines, tones) rewritten by a separate agent and checked: 32 dashes gone (staff 14, ledger-lines 15, note-names 2, index 1), each rewritten with a colon, a comma, brackets or a full stop, never two colons in a sentence; 19 long paragraphs split into one idea each; no fact, name, link, drawing or id changed (a script compared tags, placeholders, links, ids and words); index lead 'On each floor, any room can come first.'; every page 'Updated 13 October 2026'; all rebuilt --final. Her other answers recorded: rule 8 (Korean middle C stays 가운데 도), new rule 12 (counting with +: 1 + 2 +, 1 e + a; walk and run; her two pulse faults), new rule 13 (the theory gaps, room by room, and a 'Writing music' room on Level 5; the house reveal after all books). Chapter 3: 'B 전부 추천대로', G1-G3 answered (next phase). |
"""
m = re.search(r'^\| 452 \| [^\n]*\n', s, re.M)
if not m: raise SystemExit('row 452')
s = s[:m.end()] + ROW + s[m.end():]
open(p, 'w', encoding='utf-8').write(s); print('CLAUDE.md: rules 8, 12, 13 and log row 453')
