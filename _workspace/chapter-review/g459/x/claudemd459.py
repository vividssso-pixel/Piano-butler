#!/usr/bin/env python3
# Phase 459: CLAUDE.md: the log row; Book rules 7, 8 and 11.
import sys, re
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
def rep(a, b):
    global s
    if s.count(a) != 1: raise SystemExit('found %d: %s' % (s.count(a), a[:60]))
    s = s.replace(a, b)
rep("Every explanation short and plain, nothing extra (her 2026-10-13 20:45 '다 심플하게 설명해줘 군더더기 없이').",
    "Every explanation short and plain, nothing extra (her 2026-10-13 20:45 '다 심플하게 설명해줘 군더더기 없이'; 20:57 '모든 챕터에 적용해줘': done for the eight finished books and their guide pages in Phase 459): one fact a sentence, no warm-up words, nothing the picture or the title already says.")
rep("bird's sky over Queensland and down into the turtle's sea under Kingsland ('ladder 1, ladder 2')",
    "bird's sky over the treble staff and down into the turtle's sea under the bass staff ('ladder 1, ladder 2')")
rep("treble staff is Queensland and the bass staff Kingsland from chapter 5;",
    "two staves go by their REAL NAMES (her 2026-10-13 20:58 '퀸즈랜드 킹스랜드 좋은데 진짜 이름으로 불러야지 treble clef, bass clef'; Phase 459): every title, label, button, check row, drill level and teacher line says treble clef / bass clef (높은음자리표 / 낮은음자리표), or the treble staff / bass staff (높은음자리표 오선 / 낮은음자리표 오선) for a place on the page; 'Clef check', never 'Crown check'; 'between the staves', never 'between the lands'; Queensland and Kingsland are said ONCE, in chapter 7's opener, as the staves' other names;")
rep("PATH_STAGES order. Done: posture-hands, first-steps, note-names, staff, pulse (Level 1); whole-staff, tones (Level 2);",
    "PATH_STAGES order. Done: posture-hands, first-steps, note-names, staff, pulse (Level 1); whole-staff (named 'Line and Space Names' / '줄과 칸 이름' since Phase 459, her 20:58 '라인 칸 전체 이름 익히는거라 이름 바꿔야할 듯'; the id stays), tones (Level 2);")
ROW = """| 459 | 2026-10-13 | **Short and plain in every finished book; real names for the staves; chapter 7 renamed.** Her 20:57 '짧고 군더더기 없이 ... 모든 챕터에 적용해줘' and 20:58 '퀸즈랜드 킹스랜드 좋은데 진짜 이름으로 불러야지 treble clef, bass clef, 챕터 이름도 그렇고 그리고 이 챕터 이름이 whole staff가 아니라 라인 칸 전체 이름 익히는거라 이름 바꿔야할 듯'. (1) Short and plain: eight agents, one per chapter (posture-hands, first-steps, pulse, note-names, staff, whole-staff, tones, ledger-lines), proposed exact replacements for every LbSay, step and long line, en and ko, and for the guide pages' body text (not the teacher's notes): about a fifth shorter, every fact, task and cast member kept (_workspace/chapter-review/g459: BRIEF.md, the eight JSON files, apply460a.py); one check-up sentence for every book ('Show each one at the piano. Colour a circle: not yet, nearly, or got it!'); chapter 1's six warm-up cards shortened (book and Toolbox); the last long dashes in these books gone; note-names' 'make up a word of your own' gone (Book rule 3). (2) Real names (patch460b/c.py): titles, labels, buttons, check rows, drill levels ('Clef check: treble or bass?', 'Treble clef: every line and space', 'One ladder: treble clef', 'Between the staves'), Workbook how-lines (circle 'treble' or 'bass' instead of Q or K), Teacher copies and the ledger guide say treble clef / bass clef or the treble / bass staff; chapter 7's opener: 'The treble staff is on top. Its other name is Queensland, the Queen's land.'; its picture's watermark reads TREBLE CLEF / BASS CLEF. (3) Chapter 7 is 'Line and Space Names' / '줄과 칸 이름' (book, app, drill, Workbook header, house rooms, the staff guide's next link, the teacher dashboard). (4) A fresh reviewer read every changed line; its 26 points applied (patch460d.py: which Cs meet in the fold, space 1 in each clef, Korean particles and verbs, 'from the bottom', a label that ran out of its box, 오선 wherever the English says staff). Guides rebuilt --final (all seven + the index's house); worksheet images unchanged (pixel-identical). Checks: fitall 126 paths 0 overflow; lbcheck eight chapters 0/0 en and ko; ws460test 45, ll431test460 24, ll444test460 82, tn444test 16, sf405test 22, ch1app460 21 pass, 0 fail (the 460 tests replace 419/449/376 where the words changed). |
"""
m = re.search(r'^\| 458 \| [^\n]*\n', s, re.M)
if not m: raise SystemExit('row 458')
s = s[:m.end()] + ROW + s[m.end():]
open(p, 'w', encoding='utf-8').write(s); print('CLAUDE.md: log row 459, rules 7, 8, 11')
