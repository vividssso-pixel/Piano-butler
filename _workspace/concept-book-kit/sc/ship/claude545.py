import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 541 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 542 | 2026-10-19 | **No 'LEVEL 11' in game mode (her 14:47 note).** In a drill whose levels have names, the game start screen no longer shows 'LEVEL n' (it was the internal number); the game bar shows the lesson number and name (e.g. '1 SHARP ORDER') instead of 'LV n', and the printed worksheet header shows just the level's name. Source `patch545.py`; checked by me, no console errors. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
