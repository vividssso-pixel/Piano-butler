import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 600 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 601 | 2026-10-21 | **Scales lesson 12: the seven modes.** Her call (2026-10-21): modes become a lesson of the Scales concept. New `ScModes` (`sc-modes`, registered in `HOME_LIVE['p-scale'].lessons`, `TOOL_CONCEPT`, Home tryLine now \"Twelve short lessons\"). Same lesson style: all (C major's notes, the seven names) → one by one (each mode on the keyboard with its start note named, both ends marked; parent major chips C, G, D, F, B♭; staff behind a button with the parent key signature in green; ▶ Hear it) → her turn (play a mode on C's white keys; a wrong key says so plainly and names the next note). Every musical fact (formula, mood, example) comes unchanged from the existing `MODES` table, nothing new from memory. The old hidden `modes` tool and its component stay until the chapter rebuild. Built by `patch610.py` (`t614`). Checked English and Korean through all screens: no console errors. Local commit only, not pushed. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
