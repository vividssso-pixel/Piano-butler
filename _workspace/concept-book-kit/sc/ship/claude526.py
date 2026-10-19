import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 524 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 525 | 2026-10-19 | **Minor lesson: minus and plus, and a middle speed (her 13:22 note).** Your turn: the left and right arrows are replaced by a minus and a plus button under the staff (one less or one more sharp or flat, with the count between them; the ends are disabled), so the direction is no longer confused with left and right. Animation speed set between the two earlier versions: first step after 0.6 s, then one per second; the half step up in the major rule after 0.7 s. Source `patch526.py`; checked by me, EN and KO, no console errors. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
