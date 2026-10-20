import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 588 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 589 | 2026-10-20 | **Fingering and colours on the staff screens.** Lesson 9 (all twelve keys) now shows both hands' fingering for the chosen key (the same two-row grid as lesson 8, moving with the ▶ Up and down animation). On the staves, notes that come from the key signature are green (the key signature itself too) and accidentals are coral, with a small legend; applies to lesson 11 and to the staves in lessons 9 and 2. Lesson 11's \"Your turn\" also shows the D-minor staff with its key signature, each note appearing as she taps it, in the matching colours. New staff options `hl2`, `underAlt`, `signHl2` (second colour #2e8a6e). Built by `patch596.py`, `patch597.py`, `patch598.py` (`t602`). Checked in English and Korean, no console errors. Local commit only, not pushed. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
