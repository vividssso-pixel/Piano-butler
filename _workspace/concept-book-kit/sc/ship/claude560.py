import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 555 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 556 | 2026-10-19 | **Accidentals lesson 5, the natural, rebuilt in the template (her 'build it optimally, do not slot other things in first').** New hidden tool `ac-natural` is Home lesson 5, straight after the sharp and the flat; the old 'Cancel it' mover (`cl-natural`) is out of the list. Whole picture: F♯ back to F and B♭ back to B (one sharp, one flat), 'Natural (♮) = the plain white key again. It cancels a sharp or a flat.' One by one: F♯, B♭, C♯, E♭, G♯, A♭, each coming back to its plain white key. Her turn: the key with the sign is shown, she taps its natural; wrong key gets a gentle line; 'Another →' goes to the next. Staggered name labels so F♮ and F♯ do not collide. Source `patch560.py` + `patch561.py`; checked by me, no console errors. Next on the Home list: Play sharps and flats (staff), The natural (staff, old), then the rest, still to be rebuilt. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
