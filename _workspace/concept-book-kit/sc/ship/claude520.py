import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 519 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 520 | 2026-10-19 | **Same keyboard in the order and the key screens (her 13:02 note).** The Major key rule screen and the 'What key has N?' screen now use the keyboard of the orders: sharps get the extra C on the right, flats the extra B on the left, and C♭ major (7 flats) lights that low B like the order screen does. Source `patch520.py`; checked by me, EN and KO, no console errors. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
