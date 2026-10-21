import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 624 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 625 | 2026-10-22 | **Keys and staff section 1: white at first, no black-key names, no staff.** Her notes (2026-10-22): the keyboard should start plain white before the animation so it can be seen; no staff button in these lessons; no black-key names yet. Two houses and Every key has its place now start on a white keyboard: the four houses build up one at a time (roof drops, keys colour, letters appear), the close-ups start white and colour a moment later, the letters light up from white. The 'Show on the staff' button is gone from all of section 1 (the staff starts in section 2). `ScKeys` got an optional `plain` flag (letters above the keys stay, the black-key names C♯/D♭ and the white-key letters are left off), used by the section 1 keyboards. Built by `patch634.py` (+ `kq.jsx`) (`t639`). Opened five lessons at 390 px in English and Korean, plus the animation frames: no console errors. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
