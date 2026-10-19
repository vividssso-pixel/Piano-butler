import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 510 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 511 | 2026-10-19 | **No separate Learn layer (her 11:37 note).** In Scales and keys the five lessons now sit straight on the concept page (1 to 5), followed by Try (6) and Check (7); the middle Learn list is gone. Back from a lesson returns to this page. Source `patch511.py`; checked by me, EN and KO, no console errors. My reading of her note: she meant the Learn category is redundant, so Try and Check stay as the last two rows. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
