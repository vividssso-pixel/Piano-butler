import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 559 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 560 | 2026-10-19 | **Accidentals lessons 1-6: the explanation line now sits at the top, right under the title (her 16:23).** In `AcStep` (half step, whole step), `AcSign` (sharp, flat), `AcNatural` and `AcBar` the one line of text moves above the keyboard / staff in every view (whole picture, one by one, her turn), so it is read first and never scrolls out of sight under the keyboard. Source `patch565.py` (moves the line in 12 blocks); checked by me, no console errors. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
