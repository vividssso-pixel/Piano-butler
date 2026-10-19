import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 545 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 546 | 2026-10-19 | **Key signatures: a new first card, 'What a key signature does' (her 15:12 note).** A sign in the key signature counts for every note of that letter, in every octave. Screen 1 shows G major's F sharp on a short row of notes and lights every F one by one; screen 2 (her turn) lets her pick G, D, F or B flat major and see which notes take the sign. It is Home lesson 1 of Key signatures, so the lessons are now 1 to 7 and the drill chips shift by one (sharp order 2, flat order 3, major sharps 4, major flats 5, both 4+5, relative minor 6, last note 7). The accidentals contrast (one note, until the bar line) comes with the Accidentals bar-line lesson. Source `patch549.py`; checked by me in English, no console errors. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
