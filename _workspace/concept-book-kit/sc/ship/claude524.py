import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 522 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 523 | 2026-10-19 | **Half steps animate; try sharps or flats directly (her 13:12 and 13:14 notes).** Minor lesson: after Next the three half steps down light up one after another (1, 2, 3, with the note sounding), and the result line appears after the third. Major rule: the half step up arrives after a short beat. Her 13:14 note: the minor lesson has a 'Try it: Sharps / Flats' row under the buttons (no need to click through to the end), and the Your turn screen has Sharp keys / Flat keys buttons; the arrows stay inside the chosen group. Sources `patch523.py`, `patch524.py`; checked by me, EN and KO, no console errors. Sound not audible in the test environment. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
