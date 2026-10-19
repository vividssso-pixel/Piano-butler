import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 532 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 533 | 2026-10-19 | **Before you play the piece: List / Circle (her 14:10 note).** A List | Circle switch at the top of lesson 6. List (default) is the table; Circle is the circle of fifths with each key's relative minor inside, tap a key to see its key signature on the staff, and the line 'Clockwise: one more sharp, anticlockwise: one more flat'. The last-bar guide and Play its scale are shared. Source `patch535.py`; checked by me, EN and KO, no console errors. Note: the circle has twelve places, so the sharp spellings F sharp, C sharp major (and C flat) are reached from the List, not the Circle. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
