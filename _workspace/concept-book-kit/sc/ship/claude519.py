import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 518 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 519 | 2026-10-19 | **'Second last' and the one-flat case (her 13:00 note).** English now says 'second last' instead of 'second-to-last' (shorter, and the usual Australian wording); Korean unchanged. The flat rule examples are now 3 flats, 5 flats, then 1 flat: with one flat there is no second last, so that example just shows F major (no circle, no steps). Source `patch519.py`; checked by me, EN and KO, no console errors. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
