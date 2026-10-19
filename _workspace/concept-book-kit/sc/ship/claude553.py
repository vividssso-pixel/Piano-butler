import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 549 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 550 | 2026-10-19 | **Half and whole step arrows drawn on the keys (her 15:26 note: from the letter C on the key up to the black key).** The arrows no longer float above the keyboard: each starts at the letter of a white key (or the middle of a black key) and ends on the next key, so C goes up-right to the black key, E goes sideways to F, a black key goes down to the next white letter. Navy with a white halo so they read on white, coral and black keys. `TapKeyboard` gets an `overlay` prop. The whole picture of the half step is now a zigzag over the keys. Source `patch553.py`; checked by me, no console errors. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
