import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 679 |')]
assert len(idx) == 1
rows = [
"| 680 | 2026-10-26 | **Workbooks for the three new Grades 2-3 rooms (Build AN).** Built on row 679, the way Build AI made them (row 675): pages 2 to 6 face the Lesson Book's steps (try it with an example, your turn this week, play), page 7 is the check-up on paper, and each teacher's copy gains every answer and the scoring (4 marks a part, pass 3+, go back to the step's page). Scales Further (ScfWorkbook, ScfPaperCheck, SCF_WB): the thumb's two letters, where the thumbs meet, the melodic minor written up and down, mirror twins Y or N, chromatic fingers. Intervals and Chords Further (H3Workbook, H3PaperCheck, H3_WB): name the interval, the degree names, I/IV/V and their first inversions, which voice, perfect or plagal. Rhythm Further (R2Workbook, R2PaperCheck, R2_WB; check lines chkA and chkB, four bars): counts under the notes in boxes, how many, beats in a bar, simple or compound. Every answer is computed from the room's own data. Small changes for the paper: ScfStrip legend optional, ScfCmKb finger-circle size and a bare form, the Rhythm teacher's copy two lines across. Tests wbshot.js (all pages, no overflow), chsweep, booksweep, reg674. |",
]
for r in reversed(rows): lines.insert(idx[0] + 1, r)
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
