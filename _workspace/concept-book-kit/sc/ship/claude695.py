import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 670 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 671 | 2026-10-26 | **Theory follows Theory of Music (Build AF-1; decision board call 5, changed 10:23).** Built on row 670. Sohyun's students sit Theory of Music, not Music Craft (the Grade 6 practical needs a Grade 2 theory pass: Theory of Music, Musicianship or Music Craft), so the theory standard is now Theory of Music; Music Craft is reference only, and aural, general knowledge and technique follow the practical syllabus. Technique is comparable, not a copy of the exam lists: rooms teach the skill each scale group and exercise is for; the exam's pieces stay in the book. Row 670 moved three Home lessons to Grades 2-3 on Music Craft Grade 3; in Theory of Music the inversion of intervals is Grade 4 and chromatic intervals Grade 5, so 'Turn it upside down', 'The tritone' and 'Diminished and augmented' carry the Grade 4 mark again (the exact floor waits for board call 9). 'Question or answer phrase?' and 'Sequences' stay on Grades 2-3. Only HOME_FLOOR changes. Files: drills.html, drills.src.html, _workspace/concept-book-kit/sc/patch695.py. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
