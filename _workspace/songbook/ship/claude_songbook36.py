import sys, io, re
hist = sys.argv[1]
h = io.open(hist, encoding='utf-8').read().split('\n')
rows = [i for i, l in enumerate(h) if re.match(r'^\| \d+ \|', l)]
n = max(int(h[i].split('|')[1]) for i in rows) + 1
h.insert(rows[-1] + 1, "| {n} | 2026-11-04 | **The song Lesson Book's pages now run whole, part, whole (chat window, her 13:13 to 13:15).** Her 13:13 'Listen is first, so shouldn't the score on page 2 come first, then the taking apart (the elements) on page 2, then the chords? And Lesson 1?' -- yes (13:15). Page 1 Listen and sing: title, chips, Listen first (QR), the position keyboard, the whole tune with its words; ticks Listened and pointed / Sang it with the words. Page 2 Take it apart: The rhythm (say and clap, the beat and the note values, counts) and The notes (the tune again with empty heads and a box under each to write its letter name; Mary on the staff, her skip question moved here). Page 3 Play it: Lesson 1 the right-hand and left-hand panels, no chords; the chords start on page 3 at Lesson 4 (Mary). One QR per lesson, on page 1. Generator: name jobs (engrave default name1/name2, buns name1/name2 with blank heads), boxes before the staff sit just under the heads, the default rhythm lines a little smaller (sl 0.4). |".format(n=n))
io.open(hist, "w", encoding="utf-8").write("\n".join(h)); print("row", n)
