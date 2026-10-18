import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 496 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 497 | 2026-10-19 | **'Say the order' lights the keys (her 09:10: the zigzag she teaches in lessons).** In the Key finder's sharps and flats steps, each note of the order lights on the keyboard as it sounds and stays lit as a trail (the newest one strongest); picking another count or tapping the answer clears it. One small change in `KfFind` (`patch497.py`), checked by me with screenshots mid-run and at the end for sharps and flats, no console errors. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
