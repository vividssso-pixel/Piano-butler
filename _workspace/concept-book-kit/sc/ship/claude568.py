import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 563 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 564 | 2026-10-19 | **Accidentals lesson 6 renamed (her 22:07).** 'Signs in a bar' is now 'Rules for sharps, flats and naturals' / 샵, 플랫, 내추럴의 규칙 (tool title and the lesson's own title); blurb 'How long each sign lasts, and which notes it reaches.' Source `patch569.py`; checked by me, no console errors. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
