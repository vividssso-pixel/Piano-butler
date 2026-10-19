import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 523 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 524 | 2026-10-19 | **Slower half-step animation (her 13:17 note).** The three half steps down now come one every 1.5 seconds (first after 0.8 s), the half step up in the major rule after 1 s, and the notes ring longer. Source `patch525.py`; checked by me, no console errors. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
