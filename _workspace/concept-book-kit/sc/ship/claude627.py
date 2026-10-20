import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 613 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 614 | 2026-10-21 | **Scale finder: clock hand instead of a turning ring; the staff follows the playback.** Her ideas (2026-10-21): keep the circle of fifths but, like a clock, let the writing stand still and a hand move; and when playing up and down, the staff should move with the keyboard. The two rings (major outside, relative minor inside) no longer turn; a coral capsule with a pointer, the hand, glides round to the chosen pair (animated, shortest way). During up and down the sounding note is marked on both staves with a coral ring that glides from note to note (works for 2 octaves too: the second octave is shown on the same one-octave staff). New staff option `ringGlide` in `SkgStaff`. Built by `patch624.py` (`t627`). Checked E-flat major, staff on, playback: no console errors. Local commit only, not pushed. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
