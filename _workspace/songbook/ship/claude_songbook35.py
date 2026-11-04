import sys, io, re
hist = sys.argv[1]
h = io.open(hist, encoding='utf-8').read().split('\n')
rows = [i for i, l in enumerate(h) if re.match(r'^\| \d+ \|', l)]
n = max(int(h[i].split('|')[1]) for i in rows) + 1
h.insert(rows[-1] + 1, "| {n} | 2026-11-04 | **The song Lesson Book: whole, part, whole -- 'Listen first' at the top of every lesson; the overview's PDF links fixed (chat window, her 12:58 to 13:09).** She asked whether a lesson should show the rhythm, pitch and anatomy first, then the song, then the lead sheet, or the song first and the activities after. Recommended whole-part-whole: hear the whole song first, take it apart (page 1 rhythm from its own words, page 2 position and pitch), put it together (page 3 play, then the chords). Her 13:09 'do that': page 1 now opens with a coral 'Listen first' box under the chips, a small QR and one line (scan, listen once, hum along the second time); its QR goes to the song's drills room (the ?room= deep link is still to build). Her 13:08 screenshot 'claude.ai is blocked': the overview's PDF links opened the artifact's frame on its own, which claude.ai refuses; now a page picture opens large inside the page and 'Save the PDF' saves the file (downloads capability). |".format(n=n))
io.open(hist, "w", encoding="utf-8").write("\n".join(h)); print("row", n)
