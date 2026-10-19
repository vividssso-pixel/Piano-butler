import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 526 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 527 | 2026-10-19 | **Minor lesson: only the arrival is strong, and more air (her 13:29 and 13:30 notes).** New keyboard mark 'pass' (pale, navy words, also on black keys): the major key and the keys the three half steps pass through are pale; only the arrival (the minor key) is strong coral. Same in Your turn (the major you found goes pale once you find the minor). Spacing on the Your turn screen: more room around the group buttons, the minus / plus row and the keyboard, and above the Back button. Sources `patch528.py`, `patch529.py`; checked by me, EN and KO, no console errors. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
