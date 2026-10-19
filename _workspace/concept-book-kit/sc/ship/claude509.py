import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 508 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 509 | 2026-10-19 | **Your turn: tap on the staff or on the keys (her 11:27 note).** In step 3 of the sharp and flat order the next sign can be placed by tapping its line or space on the staff, or its key on the keyboard; the two can be mixed. A wrong staff tap shows a faint red sign where she tapped for a moment. `KSStaff` gains optional `onPick` and `ghostPos` (other users unchanged). Source `patch509.py`; checked by me, EN and KO, staff and key taps, no console errors. Note: staff taps need the exact step, about 6 px at phone width. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
