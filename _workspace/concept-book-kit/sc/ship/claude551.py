import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 547 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 548 | 2026-10-19 | **Half step and whole step lessons: straight arrows along the keys instead of arcs (her 15:23 note).** The move from one key to the next is a horizontal arrow drawn over the keyboard (to the right = up, to the left = down); in the whole picture a row of small arrows, in the examples and her turn one strong arrow that draws itself, arrowhead last. Source `patch551.py`; checked by me, no console errors. I read her note as 'show it with arrows, sideways along the keys'; to confirm with her. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
