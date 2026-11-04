import sys, io, re
hist = sys.argv[1]
h = io.open(hist, encoding='utf-8').read().split('\n')
rows = [i for i, l in enumerate(h) if re.match(r'^\| \d+ \|', l)]
n = max(int(h[i].split('|')[1]) for i in rows) + 1
h.insert(rows[-1] + 1, "| {n} | 2026-11-04 | **Page 1's song shows its fingers; stems at full length (chat window, her 13:31 to 13:32).** Her 13:31 'the finger numbers have to be on page 1's song too': the tune on page 1 has the right hand's fingers above it, in Hot Cross Buns and in Mary (engrave default sing jobs fing). Her 13:32 'stems not too short, in Hot Cross Buns' first score': a lettered head's stem not on a beam now runs a full length (700) from where the head moved to; a beamed one stays on its beam. The lettered heads are drawn before the fingers are placed, and the fingers read the line's height before anything moves, so they clear the longer stems. |".format(n=n))
io.open(hist, "w", encoding="utf-8").write("\n".join(h)); print("row", n)
