#!/usr/bin/env python3
# Phase 463: CLAUDE.md: Book rule 12 (the rhythm words; held taps); the log row.
import sys, re
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
def rep(a, b):
    global s
    if s.count(a) != 1: raise SystemExit('found %d: %s' % (s.count(a), a[:70]))
    s = s.replace(a, b)
rep("   starting the count too late.\n", """   starting the count too late. The rhythm words (her 2026-10-14 00:07 '이것도 다른 단어로 바꿔줘 walk running 아님 ta titi'):
   walk for one sound on a beat and run-ning for two, in English; in Korean 타 and 티-티, because a spoken word needs as
   many syllables as sounds (걷기 and 달리기 have two and three); never bird, tur-tle or light-house any more. A tapped
   note sounds for as long as the pad is held (her 00:12), like a key.
""")
ROW = """| 463 | 2026-10-14 | **Her late-night review, four fixes.** (1) 00:07: chapter 3's beat-or-rhythm words were still bird / tur-tle / light-house: now walk (one sound) and run-ning (two), Korean 타 and 티-티 (one syllable a sound; chapter 5's Korean labels 걷기 / 달리기 change to 타 / 티-티 too): the book's page 5 (footprints, one and two, instead of the bird and the turtle), the tool, the drill, the Workbook, the Teacher copy, the guide page (text and drawing). (2) 00:12: tapping a minim gave a short blip while listening held it: the tap pads now sound the note for as long as they are held (pointer or space bar down to up, up to a semibreve); blip and pianoNote return a release, PlPad has onRelease; chapter 5's pads say 'Hold each note'. (3) 00:14: the King's cross was cut off at the top of the chapter 6 clef intros: the pieces sit lower in their boxes, and the cross has a thinner bar and a clear top. (4) 00:15: chapter 6 page 3 showed skips only on lines and only going up: now two staves, steps up and down, and skips line to line and space to space, each up and back down; the bird's cloud no longer cut off; the tasks name their keys (C D E F G F E D C; C E G E C, D F A F D; Book rule 3). Guide drawings regenerated (kit/guide463svg.js). Checks: lbcheck 0/0 for staff, pulse, note-values in both languages. |
"""
m = re.search(r'^\| 462 \| [^\n]*\n', s, re.M)
if not m: raise SystemExit('row 462')
s = s[:m.end()] + ROW + s[m.end():]
open(p, 'w', encoding='utf-8').write(s); print('CLAUDE.md: rule 12; log row 463')
