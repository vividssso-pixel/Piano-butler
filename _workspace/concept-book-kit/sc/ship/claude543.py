import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 539 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 540 | 2026-10-19 | **Drill chips are numbered in order (her 14:41 note).** In a drill whose levels have names, the main levels show their order as a small number before the name (1 Sharp order, 2 Flat order, 3 Major: sharps, 4 Major: flats, 5 All 15, 6 Relative minor, 7 Last note); the More practice chips have no number. Source `patch543.py`; checked by me, EN and KO, no console errors. Note: the drill numbers 1 to 7 are the drill's own order, not the Home lesson numbers (the drill adds All 15 and Last note). |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
