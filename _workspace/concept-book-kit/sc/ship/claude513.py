import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 512 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 513 | 2026-10-19 | **Home: Key signatures and Scales are two concepts (her 11:42 notes).** On the Home, Pitch lists Key signatures (the five lessons, then Drill) and Scales (Try = the Scale finder, then Drill) instead of one Scales and keys. The T/S pattern card is removed. The last row is called Drill and opens the chapter drill (key-signatures / scales). Home-only split: `HOME_VIRTUAL`, `homeCats`, `homeCatById`; the Toolbox keeps its single Scales and keys group, and old `concept=p-scales` links land on the Pitch list. Source `patch513.py`; checked by me, EN and KO, no console errors. Not done: the Scale finder's three steps are still one tool; the circle of fifths and the old More practice tools are no longer linked from the Home (still in the Toolbox). |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
