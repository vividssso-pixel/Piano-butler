import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 558 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 559 | 2026-10-19 | **Signs in a bar: two more examples (her 16:18, 'other examples too; the drill will do more').** The lesson now has three little bars, each with its own whole picture and walk, 'Example n / 3', and an 'Another example →' button at the end of each walk: (1) F♯ G F F-up B♭ B♮ | F; (2) E♭ A E E-up | E, a flat on the bottom line; (3) C♯ D C C♮ C | C, a sharp ended by a natural, the natural lasting to the bar line (her `ACC_EXAMPLES` wording). Her turn mixes all three examples (first question of each, then the second of each, ...) with the reason after each answer. Source `patch564.py` (data-driven `AC_BARS`); checked by me, no console errors. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
