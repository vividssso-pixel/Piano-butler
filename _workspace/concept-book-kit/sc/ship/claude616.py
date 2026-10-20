import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 602 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 603 | 2026-10-21 | **Scale finder: fingering on two keyboards, one ring.** Her feedback (2026-10-21): the 1-2-3 / 1-2-3-4 colours must be on the keys as in the old finder, both hands as two keyboards one above the other, the staff behind a button (kept), and the circle of fifths design was not liked. Fingering is now the right-hand keyboard over the left-hand keyboard (`ScaleKeyboard`, coloured groups and a legend), for major and minor; where the harmonic fingering would put a thumb on a black key the note stays. The dial is one big ring of twelve (like the Home clock) whose Major / Minor chips swap its labels, so there are no tiny inner labels; the relative key is named in the centre. Still turns to put the chosen key in the window at the top. Built by `patch612.py` (`t616`). Checked major and minor, English: no console errors. Local commit only, not pushed. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
