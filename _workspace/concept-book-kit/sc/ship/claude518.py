import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 517 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 518 | 2026-10-19 | **All count buttons work at once (her 12:58 note).** On the 'What key has N sharps (flats)?' screen the 1 to 7 buttons were unlocked one at a time (the higher ones greyed out); now every one can be tapped straight away. Source `patch518.py`; checked by me, EN and KO, 1 to 7 in a row, 7 sharps found, no console errors. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
