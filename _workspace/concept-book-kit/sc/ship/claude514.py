import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 513 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 514 | 2026-10-19 | **Find the major key: the rule comes first (her 11:48 note).** On the Sharps and the Flats rule screens of Find the major key, the one-line rule (the key is a half step above the last sharp; the second-to-last flat) now sits right under the title, before the staff, keyboard and result. My reading of her garbled note; easy to undo. Source `patch514.py`; checked by me, EN and KO, no console errors. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
