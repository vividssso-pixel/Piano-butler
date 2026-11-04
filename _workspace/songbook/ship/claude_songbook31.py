import sys, io, re
hist = sys.argv[1]
h = io.open(hist, encoding='utf-8').read().split('\n')
rows = [i for i, l in enumerate(h) if re.match(r'^\| \d+ \|', l)]
n = max(int(h[i].split('|')[1]) for i in rows) + 1
h.insert(rows[-1] + 1, "| {n} | 2026-11-04 | **The song Lesson Book: Lesson 1 Rain, Rain is played with the hands mixed; Hot Cross Buns keeps a right-hand and a left-hand panel; the end bar fixed (chat window, her 12:33 to 12:42).** Her 12:34 'show the right hand and the left hand separately': page 3 (Play it) of the early lessons now draws each hand in a panel of its own (navy R, coral L). Her 12:41-12:42 'the end bar line looks odd; 2 is played by the left hand, so stems down; in this one the hands are not taken separately, they mix': Rain, Rain is one 'Both hands' panel -- the left hand's 2 on A sharp (the top of the three), the right hand's 3 and 4 on C sharp and D sharp (the two); a left-hand note's stem points down at full length (S.hand, job option mix); two set tasks fill the page (Which hand?, Hands only); the checks are Slowly / In time. Before the staff the end bar's thick stroke now reaches as far as its thin one. Her 12:41 on length: both songs stay as they are (a concept summary, not the full versions). |".format(n=n))
io.open(hist, "w", encoding="utf-8").write("\n".join(h)); print("row", n)
