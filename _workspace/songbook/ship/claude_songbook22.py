import sys, io, re
hist = sys.argv[1]
h = io.open(hist, encoding='utf-8').read().split('\n')
rows = [i for i, l in enumerate(h) if re.match(r'^\| \d+ \|', l)]
n = max(int(h[i].split('|')[1]) for i in rows) + 1
h.insert(rows[-1] + 1, f"| {n} | 2026-11-04 | **The song Lesson Book: Lesson 1 with its quavers, black keys with 4 3 2 (chat window, her 11:51: 'One a penny, two a penny' is quavers and that is the fun; on the black keys the fingers are 2 3 4, introduced first, leading down to C D E; 'or just introduce quavers early, nothing says they must come late').** My view, taken: keep Hot Cross Buns first and bring the quavers in by sound, in her own words from the drills, walk and run-ning (two quick notes in one beat; say pen-ny, count 1 +). Built: the third bar in quavers, beamed in twos (the engraver beams quavers now), counted 1 + 2 + 3 + 4 +; the note box shows 'crotchet: walk', 'two quavers: run-ning' and the minim; the running bar on a line of its own so its notes keep their room (lines 2 bars, 1 bar, 1 bar, scaled to one note size); letter boxes as wide as each note's room allows, never touching. Play it: the three black keys from the top with 4 3 2, then slide down to E D C with 3 2 1, then the left hand (1 2 3). Lesson 5 rebuilt with the same engraver, unchanged. |")
io.open(hist, 'w', encoding='utf-8').write('\n'.join(h)); print('row', n)
