import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 594 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 595 | 2026-10-20 | **Home line for Scales matches the eleven lessons.** On Home the Scales concept lists its eleven lessons in order (shape, same pattern, degrees, white keys right and left, black keys right and left, both hands, all twelve keys, chromatic, minor); the line above them still said \"Three steps: white keys, black keys, all twelve\" and now reads \"Eleven short lessons: the shape, fingering, all twelve keys, the minor scales\" (Korean too). Built by `patch604.py` (`t608`). Local commit only, not pushed. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
