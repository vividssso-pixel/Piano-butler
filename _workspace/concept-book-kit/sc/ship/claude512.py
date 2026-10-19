import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 511 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 512 | 2026-10-19 | **Flat order zigzags like the sharps (her 11:39 note).** The flat-order keyboard gets one extra B at its left end (C♭ is the B below C), so the seven dots alternate high and low in a clean zigzag; C♭ is labelled on that key and F♭ on E, and both sound at those keys (the low B sounds below the keyboard's C). `TapKeyboard` gains optional `extraB`. Tapping that B in Your turn counts as C♭. Source `patch512.py`; checked by me, EN and KO, no console errors. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
