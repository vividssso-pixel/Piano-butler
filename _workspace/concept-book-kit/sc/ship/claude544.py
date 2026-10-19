import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 540 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 541 | 2026-10-19 | **Drill numbers follow the Home lessons; All 15 renamed (her 14:42 note).** Key signatures drill chips carry the number of the Home lesson they practise: 1 Sharp order, 2 Flat order, 3 Major: sharps, 4 Major: flats, 3+4 Major: sharp + flat (was All 15: the mixed review of lessons 3 and 4), 5 Relative minor, 6 Last note (lesson 6, the circle of fifths, has the last-bar guide). Source `patch544.py`; checked by me, EN and KO, no console errors. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
