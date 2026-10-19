import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 533 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 534 | 2026-10-19 | **A right answer waits; the circle shows the grand staff (her 14:13 note).** Every drill in lesson mode: after a right answer the screen stays 2 seconds (it was 0.7) and a Next button is there to go on sooner (game mode unchanged). Lesson 6, Circle view: the key signature is drawn on the grand staff (treble over bass, joined by a brace). Source `patch536.py`; checked by me, EN and KO, no console errors. Note: the longer wait is in the shared drill engine, so it applies to all drills. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
