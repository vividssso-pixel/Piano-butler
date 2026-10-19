import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 505 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 506 | 2026-10-19 | **Sharp order: 7th note sounds at the key it lights (her 11:14 note).** B♯, the 7th sharp, lights the C above B on the keyboard but played the middle C. The order screen's Say the order and + now play that high C (same key index as the lit key). Source `patch506.py`; checked by me, EN and KO, no console errors. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
