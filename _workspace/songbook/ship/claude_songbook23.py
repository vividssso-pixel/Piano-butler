import sys, io, re
hist = sys.argv[1]
h = io.open(hist, encoding='utf-8').read().split('\n')
rows = [i for i, l in enumerate(h) if re.match(r'^\| \d+ \|', l)]
n = max(int(h[i].split('|')[1]) for i in rows) + 1
h.insert(rows[-1] + 1, f"| {n} | 2026-11-04 | **The song Lesson Book: Hot Cross Buns in 2/4, eight bars (chat window, her 11:59: split it into 2/4 as 8 bars? and the music always reaching the right edge).** Done: two beats a bar (count 1 2), the running bars four quavers each, four bars to a line, both lines full width; no line shorter than the measure. Rule for every lesson from now: lines of equal length that end at the right margin, the bars split so they come out even. |")
io.open(hist, 'w', encoding='utf-8').write('\n'.join(h)); print('row', n)
