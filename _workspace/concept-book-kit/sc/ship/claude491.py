import sys
p = sys.argv[1]
s = open(p, encoding='utf-8').read()
lines = s.split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 490 |')]
assert len(idx) == 1, 'row490'
row = ("| 491 | 2026-10-19 | **The dice board under every quiz is gone; ten steps and one token instead (her 2026-10-19 01:07: '이건 없애자, 대신 체스처럼 10문제씩이니까 움직이는게 보이는건 좋은 것 같아').** "
"The 24-square board (dice, D.C./D.S./Fine rules, a segno glyph that showed as an empty box) is replaced in `BoardTrack`/`useBoard` by a row of ten small steps, one per question; a coral token moves one step after each answer, the step turns navy for a right answer and soft coral for a wrong one, and after the tenth it starts again. "
"Same names, so all ~25 quiz types changed at once; the print pages still hide it; an aria-label says 'Question 4 of 10, 1 right so far'. The 'Game board rule' line in Beat and time is removed. Game mode (its own start screen) was not touched. Source `patch491.py`. Small change, checked by me alone (no theory touched): both languages at 390 and 320, no scroll, no errors. "
"**Open for her:** whether wrong answers should also move the token (now they do, in coral); nothing else. |")
lines.insert(idx[0] + 1, row)
open(p, 'w', encoding='utf-8').write('\n'.join(lines))
print('ok')
