import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 703 |')]
assert len(idx) == 1
rows = [
"| 704 | 2026-10-27 | **Smaller rooms on screen: one step open at a time (Build BL; her 20:17, 'the size of each room').** A room's page held every step open at once (Melody 12,500 px tall on a phone). Now only the first step not yet ticked is open; the others show as their title line. Got it ✓ folds the step and opens the next; a step's title or its pill in the map opens that one and folds the rest. Phone heights: Melody 12,500 to 3,900 px, Time signatures 9,500 to 3,300, Chords 9,900 to 3,900, Rhythm 9,300 to 3,500. Nothing removed; the books unchanged. Source patch731.py. chsweep 46 chapters 0 errors, booksweep 0 errors, regression 332 lessons, 54 drills, 0 errors. Local commit only, not pushed. |",
]
for r in reversed(rows): lines.insert(idx[0] + 1, r)
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
