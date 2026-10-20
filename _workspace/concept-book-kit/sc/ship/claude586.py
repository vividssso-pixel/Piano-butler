import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 577 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 578 | 2026-10-20 | **Scales fingering strips: B (right hand) and F (left hand) join the standard row; digits no longer clump (her call, 12:48).** In the white-key lessons the standard B on the right hand and the standard F on the left hand are shown in the same row as C G D A E, leaving only the one odd key (F right hand, B left hand) marked ≠. In every strip and in the both-hands lesson each finger number now sits in its own column under its note instead of a spaced-out block of digits. Built as `t586` (edit of `t585`). Checked in English, no errors. Local commit only, not pushed. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
