import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 514 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 515 | 2026-10-19 | **Find the major key rule, unfolded in two steps (her 11:50 note).** The Sharps rule screen now says 1. circle the last sharp (a ring on the staff, the key it names lit on the keyboard), then Next: 2. go up one half step (the key lights, 3 sharps = A major appears; the A key sounds). The Flats rule screen does the same with the second-to-last flat (that flat is the key; one flat is F). `KSStaff` gains optional `ring`. Back returns to step 1. Source `patch515.py`; checked by me, EN and KO, no console errors. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
