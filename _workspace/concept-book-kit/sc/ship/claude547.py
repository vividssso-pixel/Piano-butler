import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 543 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 544 | 2026-10-19 | **Concept renamed: Accidentals (her 15:07 note).** The Home concept `p-clock` is now 'Accidentals' (ko 임시표) with the line 'Sharps, flats and naturals' (ko 샵, 플랫, 내추럴) under it; the drill and the lesson kickers use the new name. The Toolbox group takes the same name. Source `patch547.py`; checked by me in English and Korean, no console errors. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
