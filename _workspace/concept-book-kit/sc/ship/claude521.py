import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 520 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 521 | 2026-10-19 | **Numbers above the signs in the Major key lessons (her 13:06 note).** The rule screen and the 'What key has N?' screen number every sharp (flat) on the staff, first to last, and the one that is circled (or found) is highlighted in the number row. Source `patch521.py` (one-line changes using the existing `numbers` option of `KSStaff`); checked by me, EN and KO, no console errors. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
