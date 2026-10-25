import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 671 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 672 | 2026-10-26 | **Theory of Music floor marks (Build AF-2).** Built on row 671. From the Theory of Music check (Grades 1-3, Manual of Syllabuses 2026): 'Transposing' (kf-trans) moves from Grades 2-3 to Prelim - Grade 1 (Theory of Music Grade 1 transposes a melody of up to four bars; its room, Key signatures, is already on that floor); 'Binary, ternary, and rondo' (form-shapes) and 'Rondo' (rondo-refrain) move from Grade 5 to Grades 2-3 (Theory of Music Grade 3: binary, ternary and rondo, marked AB, ABA, ABACA). Only HOME_FLOOR changes. Files: drills.html, drills.src.html, _workspace/concept-book-kit/sc/patch696.py. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
