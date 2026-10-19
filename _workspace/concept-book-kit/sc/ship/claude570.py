import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 565 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 566 | 2026-10-19 | **Accidentals Home shows only the ten new lessons (her 22:16: leftovers should not be visible on the Home at all).** The old Home entries `chromatic`, `sac-bar`, `sac-line`, `sac-tune`, `accidental-cards`, `sharp-flat` are off the `p-clock` lesson list (the tools stay in the code and the Toolbox until she decides; chromatic goes to the scales concept later). Home now reads: 1 Half step, 2 Whole step, 3 Sharp, 4 Flat, 5 Natural, 6 Rules for sharps, flats and naturals, 7 Play it, 8 One key two names, 9 Double sharp and double flat, 10 Accidental or key signature, then 'Start the drill'. Source `patch571.py`; checked by me, no console errors. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
