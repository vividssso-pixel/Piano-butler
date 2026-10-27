import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 704 |')]
assert len(idx) == 1
rows = [
"| 705 | 2026-10-27 | **A shorter house (Build BM; her 22:21, 'the house is too long too').** On phones and narrow screens up to four rooms a row, balanced with the fuller rows at the bottom (13 rooms 4 3 3 3; seven 4 3; eight 4 4; four in one row): 14 rows instead of 19. Each room lower: the name, a smaller picture, the chair rail and the floor; the empty wainscot panels go; your room's dome scaled to fit. Phone 2,370 to 1,490 px; a narrow desktop column 3,250 to 2,050. The wide house and the printed colouring page keep their layout. Source patch732.py. chsweep 46 chapters 0 errors, booksweep 0 errors, regression 332 lessons, 54 drills, 0 errors. Local commit only, not pushed. |",
]
for r in reversed(rows): lines.insert(idx[0] + 1, r)
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
