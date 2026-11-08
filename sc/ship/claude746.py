import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 718 |')]
assert len(idx) == 1
rows = [
"| 719 | 2026-10-28 | **Every room shows its thing to make (Build CA; her 07:02, 'where are the make-toys?').** Until now a room's make-toy lived only in the Toolbox tab and at the end of the room's Home group (five rooms also had it among the 'More in the toolbox' chips), so a child working in a room never met it. LessonMake: at the end of every room with a toy, under the last step and above Start the drill, a MAKE YOUR OWN card (coral kicker, the toy's name and one-line blurb, a coral ›) that opens the toy. It finds toys by their room (TOOLS ch, ids mk-…), so all twenty show (pulse, reading-steps, chords, dynamics, tempo, minor-scales, intervals, accidentals, styles and the eleven Grade 6 to 8 rooms) and later toys need no list; the toys leave the 'More in the toolbox' chips. Navy and coral, no icon. Source patch746.py; test make746.js (20 rooms, en and ko, a card in each). chsweep 57 chapters 0 errors. Local commit only, not pushed. |",
]
for r in reversed(rows): lines.insert(idx[0] + 1, r)
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
