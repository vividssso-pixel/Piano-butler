import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 507 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 508 | 2026-10-19 | **Order screens in three steps, sharps and flats each (her 11:22 note).** For the sharp order, then the flat order: (1) all seven on the staff with one button; (2) One by one starts with an empty staff and plus adds a sharp (flat) at a time with the zigzag, minus removes, Say the order plays all seven; (3) Your turn: she taps the keys in order (Tap sharp 1 ... 7), a wrong key flashes an outline, the sentence stays visible as a guide, and Next appears after the seventh. Source `patch508.py`; checked by me, EN and KO, full walk with wrong and right taps, no console errors. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
