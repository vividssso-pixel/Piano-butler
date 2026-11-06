#!/usr/bin/env python3
# Phase 461: CLAUDE.md: the log row; Book rule 11.
import sys, re
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
def rep(a, b):
    global s
    if s.count(a) != 1: raise SystemExit('found %d: %s' % (s.count(a), a[:60]))
    s = s.replace(a, b)
rep("Next: Level 2's time-signatures,", "Next: Level 2's time-signatures (draft v1, Phase 461, waiting for her answers to B1-B12 and G1-G3),")
ROW = """| 461 | 2026-10-13 | **Chapter 8 (Time Signatures) started: Lesson Book draft v1 + review pack.** Her 23:21 '다음 진행해줘': the first room of Level 2 in path order (Book rule 11). Built on the level plan's scope for room 8 (bar lines, the double bar line and the repeat sign; 2/4 3/4 4/4; strong and weak beats; filling a bar; rests on the staff; a tie across the bar line; 6/8 and cut time for the drill's higher levels) and on chapters 5 and 6. The first book that writes rhythms on the staff: every note on G, line 2 of the treble clef, right hand finger 3 (tsRaw draws notes, rests, ties, bar lines, the double bar line, the repeat sign and time signatures inside SfStaff; each staff ends at its last bar line, one scale a page). Draft (tsbook461.jsx in _workspace/chapter-review/g461; drills.src.html unchanged, apply461.py builds a draft): 1 two bars of 4/4 with the time signature, a bar line and the double bar line named; 2 Bars and bar lines, 'Its other name is a measure', the repeat sign; 3 The two numbers, 2/4 3/4 4/4 with the top number in coral, and C, 'Its other name is common time'; 4 Strong and weak beats, big and small hearts, 4/4 strong weak medium weak, pat the 1 and clap the rest; 5 Fill the bar, the crotchet rest in the middle, the minim rest on line 3, the semibreve rest from line 4, a whole bar of silence in 4/4; 6 The tie across the bar line, the beat after it lighter; 7 My five checks. A fresh reviewer's 17 points applied (the dot in the space, the tie under the heads, labels, set tasks, one fact a sentence, 끝세로줄). Claude outputs/Chapter-08-Time-Signatures-review-v1.pdf (11 pages: summary and G1-G3, A today's chapter 8, B1-B12 with recommendations, the 7 pages, today's lesson and Workbook). Checks: lbcheck 0/0 en and ko. |
"""
m = re.search(r'^\| 460 \| [^\n]*\n', s, re.M)
if not m: raise SystemExit('row 460')
s = s[:m.end()] + ROW + s[m.end():]
open(p, 'w', encoding='utf-8').write(s); print('CLAUDE.md: log row 461, rule 11')
