import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 592 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 593 | 2026-10-20 | **Black-key buttons show both names.** In the scale lessons the key buttons for the black keys (the D♭, E♭, G♭, A♭ and B♭ scales in lessons 2, 6, 7, 8 and 9) now carry two names, sharp above and flat below, like the keys on the keyboard (C♯ over D♭, and so on). New `scKeyBtn`, `SC_SH`. Built by `patch602.py` (`t606`). Checked in English and Korean, no console errors. Local commit only, not pushed. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
