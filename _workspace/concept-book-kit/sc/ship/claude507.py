import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 506 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 507 | 2026-10-19 | **Order screen: whole order first, then one by one (her 11:17 note).** The first scene of the sharp (and flat) order is the full staff with all seven and their numbers, the sentence, and one button, One by one. The next page has the minus / Say the order / plus stepper and the keyboard, with Back to the overview. Splitting the Key and Scale finders into their own chapter is left for her review of the Home list. Source `patch507.py`; checked by me, EN and KO, no console errors. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
