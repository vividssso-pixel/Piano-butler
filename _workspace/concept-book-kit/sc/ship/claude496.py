import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 495 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 496 | 2026-10-19 | **Key finder opens on all seven (her 09:09).** Steps 1 and 2 now start on 7♯ / 7♭, so 'Say the order' plays the whole order instead of the first three. One-line change (`patch496.py`), checked by me: the staff shows all seven, the words all lit, no console errors. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
