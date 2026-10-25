import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 664 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 665 | 2026-10-26 | **Listen and Sing follows the syllabus; board names out of the drill labels (Build AA; the syllabus check of 26 Oct, her 'line it up with the syllabus').** Built on row 664. Chapter 6 checked against the Prelim aural tests: (1) Keep the beat: simple I and V chord passages in two or three beats a bar, slow (60), moderate (84) or quick (108), two quiet bars in the middle, the tapping carries on (meter and speed chips; the Home lesson cycles them). (2) Higher or lower: two notes at least a third apart, never the same, two choices everywhere (the drill's level 1 is now 'Higher or lower?'). (3) Sing it back: three, five or six one-beat notes, with a 'Note by note' mode that plays the phrase again one note at a time. Book texts, teacher notes and the five checks follow. Four time-signature drill labels no longer name an exam board (a student sees them). Regression: lessons 242, drills 37, errors 0. Files: drills.html, drills.src.html, _workspace/concept-book-kit/sc/patch689.py (+ lsx.jsx, lsh.jsx, lsx686.jsx, lsh686.jsx). |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
