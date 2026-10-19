import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 521 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 522 | 2026-10-19 | **Find the minor key: learn, then try (her 13:08 note).** The minor lesson no longer shows major and minor at once. Learn: 1. find the major first (the signature and its major key), then 2. count 3 half steps down (the three keys numbered 1, 2, 3 on the keyboard, the minor lit), over three examples (A major to F sharp minor, B flat major to G minor, E major to C sharp minor); then Your turn: on any key signature (the arrows change it) she taps the major key, then, 3 half steps down, the minor key; a wrong key flashes. Source `patch522.py`; checked by me, EN and KO, no console errors. Note: Your turn taps on the keyboard only (no staff tap), and the 'Next' to Before a piece appears only in the four-step Key finder. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
