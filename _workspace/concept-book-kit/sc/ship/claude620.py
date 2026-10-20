import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 606 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 607 | 2026-10-21 | **Scale finder: spacing, a ring round each thumb, finger numbers on the staff.** Her request (2026-10-21): keep the finger numbers well clear of the black keys, ring the 1 every time the thumb comes in, and put the finger numbers on the staff too. `TapKeyboard` `numIn`: the number sits low in the key (baseline 104, size 17), the note name under it, and a coral ring round every 1 (white ring on a black key). `sskRaw` gets `ring1` (finger numbers above the notes, a circle only round the 1); the finder's staves pass `fingers` for the one-octave fingering of both hands (none where the harmonic fingering is not shown). Built by `patch616.py` (`t620`). Checked Bb major 2 octaves with the staff open: no console errors. Local commit only, not pushed. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
