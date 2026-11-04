import sys, io, re
hist = sys.argv[1]
h = io.open(hist, encoding='utf-8').read().split('\n')
rows = [i for i, l in enumerate(h) if re.match(r'^\| \d+ \|', l)]
n = max(int(h[i].split('|')[1]) for i in rows) + 1
h.insert(rows[-1] + 1, "| {n} | 2026-11-04 | **The song Lesson Book: Rain, Rain's left hand shown in the tune itself (chat window, her 12:45).** Her 12:45 '1. take this out; 2. here just show the stems down so they know the left hand plays the 2': the Both hands panel on page 3 is gone; on page 2 (Listen and sing) the 2s (A sharp) have their stems down at full length and the words sit a little lower to clear them (verse translate 480 with job option mix); the page's how-to line says a stem down means the left hand. Page 3 keeps the keyboard, the two set tasks and the check. |".format(n=n))
io.open(hist, "w", encoding="utf-8").write("\n".join(h)); print("row", n)
