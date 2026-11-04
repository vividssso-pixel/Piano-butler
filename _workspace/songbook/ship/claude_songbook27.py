import sys, io, re
hist = sys.argv[1]
h = io.open(hist, encoding='utf-8').read().split('\n')
rows = [i for i, l in enumerate(h) if re.match(r'^\| \d+ \|', l)]
n = max(int(h[i].split('|')[1]) for i in rows) + 1
h.insert(rows[-1] + 1, f"| {n} | 2026-11-04 | **The song Lesson Book: Lesson 1's notes where the staff will put them; no black keys in it (chat window, her 12:07 to 12:11).** 12:07: the letter inside a bigger head (done: filled heads for crotchets and quavers, open for minims; one head size for the whole song, shrinking where notes are close so no two touch). 12:10: let the places hint at the staff: E on the line, D hanging just under it, C with a ledger through it like middle C (S.pre E 0, D -2, C -4 with heads twice the size; Verovio's ledger lines removed, one drawn for C); bar numbers lifted clear of the notes. 12:11: the black keys come out of Lesson 1 (it is the step onto C D E); a black-key song is to be chosen for before it. Play it is now the right hand (3 2 1) and the left hand (1 2 3). |")
io.open(hist, 'w', encoding='utf-8').write('\n'.join(h)); print('row', n)
