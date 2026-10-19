import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 534 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 535 | 2026-10-19 | **Lesson 6 is the Circle of fifths (her 14:16 note).** 'Before a piece' is renamed 'Circle of fifths' (KO 5도권), blurb 'Every key in one circle, then the list.'; the screen opens on the Circle (grand staff, relative minors inside) and the List is the second view. The last-bar guide and Play its scale stay on both. Source `patch537.py`; checked by me, EN and KO, no console errors. Note: the old four-step Key finder tool keeps its own 'Before a piece' step name. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
