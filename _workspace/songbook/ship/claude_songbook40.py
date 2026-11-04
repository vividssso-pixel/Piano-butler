import sys, io, re
hist = sys.argv[1]
h = io.open(hist, encoding='utf-8').read().split('\n')
rows = [i for i, l in enumerate(h) if re.match(r'^\| \d+ \|', l)]
n = max(int(h[i].split('|')[1]) for i in rows) + 1
h.insert(rows[-1] + 1, "| {n} | 2026-11-04 | **Hot Cross Buns on fingers 2 3 4 (chat window, her 13:48).** Her: 'with three notes, fingers 2 3 4 are better, the left hand too; 1 and 5 later, when five notes come in -- they are harder.' Right hand 2 on middle C, 3 on D, 4 on E; left hand an octave lower, 4 on C, 3 on D, 2 on E. Changed: the fingers over the tune (pages 1 and 3), the keyboards, the chip (fingers 4 3 2), page 1's Your hand and page 3's note and panel labels. Thumbs and fifth fingers wait for the five-note songs. Also this hour: the tidy-up page (artifact HcWufUE82Di9LfqnHdk2Zy) lists everything made so far, 58 items, sorted into the Song Lesson Book, the dollhouse (drills floors) and the timeless Handbook/Workbook, each with Keep / Merge / Archive and her own choice saved; nothing moved yet. |".format(n=n))
io.open(hist, "w", encoding="utf-8").write("\n".join(h)); print("row", n)
