import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 604 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 605 | 2026-10-21 | **Scale finder: clean key outlines, no scrolling, both hands on the staff.** Her feedback (2026-10-21): clean the keyboard borders, see everything at a glance without scrolling, and show both hands on the staff together (one octave is enough). `TapKeyboard` / `ScKeys` get an optional `clean` mode (thin quiet outlines, the colour only in the fill); the finder uses it. The 2-octave keyboards now fit the width (no sideways scroll). The staff behind \"Show on the staff\" is now the right hand on the treble staff over the left hand on the bass staff, one octave, with the key signature on both (key-signature notes green, signs coral; forms needing a double sharp still leave the staff out). Built by `patch614.py` (`t618`). Checked Bb major 2 octaves, all 24 keys with the staff open: no console errors. Local commit only, not pushed. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
