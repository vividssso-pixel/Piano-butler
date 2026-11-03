import sys, io, re
hist = sys.argv[1]
h = io.open(hist, encoding='utf-8').read().split('\n')
rows = [i for i, l in enumerate(h) if re.match(r'^\| \d+ \|', l)]
n = max(int(h[i].split('|')[1]) for i in rows) + 1
h.insert(rows[-1] + 1, f"| {n} | 2026-11-04 | **The song Lesson Book: a part to a page, no teacher part (chat window, her 10:34 to 10:36).** 10:34: the C position keyboard with steps and the skip moved above the tune in Listen and sing (and the 'middle C' label no longer clipped). 10:35 'only the root showing in the chords; balance each page': 10:36 'take the teacher part out' -- the duet's full chords were what showed more than the root, so it is out of the book (its data stays for the play-along page, which still offers it). The pages balanced, a part to each: 1 Say and clap (the time, the notes, the rhythm lines), 2 Listen and sing (the position, the tune a little larger with a box under every note, the QR), 3 Play it four ways (the legend, the one score with its root rows, Play together for two players, the Check). |")
io.open(hist, 'w', encoding='utf-8').write('\n'.join(h)); print('row', n)
