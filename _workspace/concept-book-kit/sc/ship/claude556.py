import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 551 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 552 | 2026-10-19 | **Accidentals lesson 3, the sharp, rebuilt in the template (her 15:34 'go to the sharp').** New hidden tool `ac-sharp` replaces the old 'The sharp' short tool as Home lesson 3. Whole picture: an arrow from each of C, D, F, G, A up to its black key, the black keys named above the keyboard (C♯ D♯ F♯ G♯ A♯); line 'Sharp (♯) = one half step up: the very next key to the right.' One by one: C, F, A, D, G, the line 'C♯ (C sharp): one half step above C.' Her turn: tap a white key, then press '♯ Sharp →'; E, B and black keys are met with a gentle line ('No black key right beside this one. Try another.'), so E♯ and B♯ wait for the 'one key, two names' lesson. One table (`AC_SIGN`) so the flat lesson is the mirror image. `TapKeyboard` gets a `top` room above the keys; names sit there. Source `patch555.py` + `patch556.py`; checked by me, no console errors. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
