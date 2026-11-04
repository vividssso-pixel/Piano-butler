import sys, io, re
hist = sys.argv[1]
h = io.open(hist, encoding='utf-8').read().split('\n')
rows = [i for i, l in enumerate(h) if re.match(r'^\| \d+ \|', l)]
n = max(int(h[i].split('|')[1]) for i in rows) + 1
h.insert(rows[-1] + 1, f"| {n} | 2026-11-04 | **The song Lesson Book: Lesson 1 is Hot Cross Buns (chat window, her 11:03: the time signature can come later; Rain, Rain needs its A for 'come again another day', so it goes later with a new position; Hot Cross Buns first, the simplest).** Lesson 1 rebuilt from buns.json: a London street cry, written down in 1733 (Wikipedia); E D C, three heights around one line (above, on, below) before the staff; page 1 'The beat' (count 1 2 3 4, what a bar is) and crotchet and minim, no time signature; page 2 the hand (thumb on middle C, 2 and 3 on D and E) and steps down; page 3 Hello, piano and Play it on the three black keys first (fingers 3 2 1; the same steps, so it sounds right), then on E D C, then the left hand. 'One a penny, two a penny' in crotchets, as most piano books print it. A shorter last line keeps the same note size (widths). The order proposed: 1 Hot Cross Buns, 2 Au clair de la lune, 3 Going Home, 4 Rain, Rain (the whole song, thumb on E: E G A), then 5 Mary on. Rain, Rain's draft (rain.json) kept for lesson 4. |")
io.open(hist, 'w', encoding='utf-8').write('\n'.join(h)); print('row', n)
