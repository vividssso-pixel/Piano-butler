import sys, io, re
hist = sys.argv[1]
h = io.open(hist, encoding='utf-8').read().split('\n')
rows = [i for i, l in enumerate(h) if re.match(r'^\| \d+ \|', l)]
n = max(int(h[i].split('|')[1]) for i in rows) + 1
h.insert(rows[-1] + 1, "| {n} | 2026-11-04 | **The position keyboard shows one octave, C to B (chat window, her 13:35).** Her 13:35 'the position only needs to go this far' (to B): kb() draws seven white keys by default (SONG.kb_whites to change), keys the same size as before, set at the left of its column. Lessons 1 and 4 rebuilt. |".format(n=n))
io.open(hist, "w", encoding="utf-8").write("\n".join(h)); print("row", n)
