import sys, io, re
hist = sys.argv[1]
h = io.open(hist, encoding='utf-8').read().split('\n')
rows = [i for i, l in enumerate(h) if re.match(r'^\| \d+ \|', l)]
n = max(int(h[i].split('|')[1]) for i in rows) + 1
h.insert(rows[-1] + 1, "| {n} | 2026-11-04 | **The song Lesson Book: Rain, Rain's position back above the tune (chat window, her 12:48).** Her 12:48 'the position has to show above the song's score': page 2 has its black-key keyboard again (L and R on each lit key) with a two-line note beside it, the tune spread a little wider (spacingLinear 0.55) and its heads a little bigger (hs 1.0) so four lines still fit. Her 12:48 'bars 9 to the end are completely different from the original; mix just these 3 notes close to the original': waiting for her tune for 'Little Johnny wants to play / Rain, rain, go away' (no text source found; Beth's Notes gives only the tone sets s-m and m-s-l). |".format(n=n))
io.open(hist, "w", encoding="utf-8").write("\n".join(h)); print("row", n)
