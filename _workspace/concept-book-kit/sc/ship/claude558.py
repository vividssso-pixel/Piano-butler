import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 553 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 554 | 2026-10-19 | **Sharp lesson 'Your turn' taps the keys; one name for the link button (her 15:49).** In her turn the student taps a white key, then taps the sharp key itself on the keyboard (no button); a wrong key gets 'Not that one. Where is the sharp of C?'; tapping another white key starts again. Works for E and B (the sharp is the white F or C). Every copy-link button now reads 'Copy link' / '링크 복사' (teacher bar, class list, kit). Source `patch558.py`; checked by me, no console errors. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
