import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 564 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 565 | 2026-10-19 | **Accidentals lesson 10, accidental or key signature? (the contrast card from the agreed plan).** New hidden tool `ac-cmp` ('Accidental or key signature?' / 임시표와 조표) is Home lesson 10, built on the same staff-and-band engine as lesson 6 (copied into `AcCmp`, data-driven `AC_CMP`). Example 1, an accidental: F♯ G F | F, the band on one space until the bar line, the next bar plain. Example 2, a key signature: F♯ written once at the start, bands on both F lines (low space and high top line) across the bar line to the end, 'Every octave too', 'The bar line does not stop it'. Her turn mixes both (seven questions, the reason after each answer). Wording is her `ACC_EXAMPLES` (accidental lasts to the end of the bar; a key signature covers every octave; the natural/new-bar interplay is left to the Key signatures concept). Source `patch570.py`; checked by me, no console errors. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
