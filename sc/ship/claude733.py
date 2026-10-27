import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 705 |')]
assert len(idx) == 1
rows = [
"| 706 | 2026-10-27 | **What is inside a room, and a shorter house again (Build BN; her 23:15, 'I can't tell what is in a room above Beginner').** Tapping a room on the house now brings up a card (through a portal, fixed at the bottom of the screen): the room's full name (Keys 5 is Keys and Intervals, Grade 5), its floor, how many steps are done, and INSIDE: its steps by title, taken from the room's own Lesson Book (LB_PAGE_FNS, the opener and the check-up left out; roomSteps, cached per language), done steps ticked in green. Go in, or the same room again, opens it; the tapped room is scrolled above the card. The hint under the house: Tap a room to see what is inside. The compact house again shorter: rooms 45 high, the picture 0.44, the floor plaque 22, a lower roof and turrets: phone 1,490 to 1,330 px (2,370 two builds ago), a narrow desktop column 2,050 to 1,820. Source patch733.py; test bn733.js. chsweep 46 chapters 0 errors, booksweep 0 errors, regression 332 lessons, 54 drills, 0 errors. Local commit only, not pushed. |",
]
for r in reversed(rows): lines.insert(idx[0] + 1, r)
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
