import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 554 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 555 | 2026-10-19 | **Accidentals lesson 4, the flat, rebuilt in the template (her 'next').** New hidden tool `ac-flat` replaces the old 'The flat' short tool as Home lesson 4: the mirror of the sharp from the same `AC_SIGN` table. Whole picture: arrows to the left from all seven white keys, labelled D♭ E♭ G♭ A♭ B♭ and, to the white keys, C♭ (the B below) and F♭ (E). One by one order D, C, E, F, G, A, B; C♭ and F♭ read 'C♭ (C flat) = the white key B. Flats are not always black keys.' Her turn: tap a white key, then tap its flat on the keyboard. Source `patch559.py`; checked by me, no console errors. C♭ = B and F♭ = E come from her own SharpFlatMover text. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
