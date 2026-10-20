import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 587 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 588 | 2026-10-20 | **Staff and key signature in the scale lessons.** Lesson 11 (three kinds of minor) now uses D minor on the treble staff with its key signature (one flat, B♭), going up and coming down on two staves. Natural minor follows the key signature with no extra sign; the harmonic minor's raised 7th (C♯) and the melodic minor's raised 6th and 7th (B♮, C♯) are drawn in coral as accidentals beside the notes, and the text says they are not part of the key signature; the melodic minor coming down returns to the key signature. The ▶ Up and down animation rings the note on the staff, the try-it turn is in D minor. Lesson 9 (all twelve keys) shows the staff of the chosen key under the keyboard, key-signature notes in coral; lesson 2 shows the staff on the two complete-scale screens. New `ScStaffScale`, `scMinItems`, `SC_D0`. Built by `patch595.py` (`t599`). Checked in English and Korean, no console errors. Local commit only, not pushed. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
