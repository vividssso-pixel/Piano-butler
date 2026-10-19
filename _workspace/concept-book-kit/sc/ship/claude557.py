import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 552 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 553 | 2026-10-19 | **Sharp lesson: a sharp is not always a black key (her 15:43 note).** `ac-sharp` no longer rejects E and B. All seven white keys now get an arrow: C D F G A to a black key, E to the white F and B to the white C, labelled E♯ and B♯ above the keys (staggered so labels do not collide). One by one order C, E, D, F, G, A, B; E and B examples read 'E♯ (E sharp) = the white key F. Sharps are not always black keys.' (E♯ = F and B♯ = C come from her own SharpFlatMover text.) Her turn: every white key works; the dead-end line is gone. Source `patch557.py`; checked by me, no console errors. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
