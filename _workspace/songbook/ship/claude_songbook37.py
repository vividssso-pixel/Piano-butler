import sys, io, re
hist = sys.argv[1]
h = io.open(hist, encoding='utf-8').read().split('\n')
rows = [i for i, l in enumerate(h) if re.match(r'^\| \d+ \|', l)]
n = max(int(h[i].split('|')[1]) for i in rows) + 1
h.insert(rows[-1] + 1, "| {n} | 2026-11-04 | **Hot Cross Buns: room round the big lettered notes; two quavers' beat as a dot cut in half (chat window, her 13:22 to 13:23).** Her 13:22 'not so close to the bar lines; space them out nicely': lines with lettered heads get Verovio note and bar-line margins (leftMarginNote 2, rightMarginNote 1.5, leftMarginBarLine 1.5, rightMarginBarLine 2; every other job resets them, since the toolkit keeps options between jobs), the quavers spread a little more (spacingNonLinear 0.35 on page 1), and page 3's lines respaced to fit. Her 13:23 'two quavers should show the circle cut in half': in the note-values box the quaver pair's one beat is now one coral dot in two halves. |".format(n=n))
io.open(hist, "w", encoding="utf-8").write("\n".join(h)); print("row", n)
