import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 568 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 569 | 2026-10-19 | **Accidentals drill: \"Find the key\" and \"On the staff\" merged into one chip (3–4) (her call, 23:30: merge only what works together).** The chip now mixes two ways of showing the same task, a note named in words and a note drawn on the staff, both answered by tapping the key. Chips 3–5 Name the sign and 5 The natural stay separate (recognition; a different idea), as do the three lesson-6 chips. The drill now has 13 main chips plus 3 in More practice. Built by `patch574.py` (`t574`). Checked: chip list in English and Korean, both question types appear, no errors. Local commit only, not pushed. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
