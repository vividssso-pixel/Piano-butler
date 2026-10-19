import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 525 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 526 | 2026-10-19 | **Minor lesson: roomier Your turn, no Try row while learning (her 13:27 note).** The 'Try it: Sharps / Flats' row is removed from the learn screens (the last example still ends with Your turn, where the Sharp keys / Flat keys buttons are). On Your turn the group buttons and the minus / plus are smaller and spaced evenly, and the prompt line is shorter, so the screen is no longer cramped. Source `patch527.py`; checked by me, no console errors. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
