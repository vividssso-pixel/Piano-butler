"""Notes: chords root first, a picture in the first line (her 4 Nov 09:25)."""
import sys, io, re
hist = sys.argv[1]
h = io.open(hist, encoding='utf-8').read().split('\n')
rows = [i for i, l in enumerate(h) if re.match(r'^\| \d+ \|', l)]
n = max(int(h[i].split('|')[1]) for i in rows) + 1
h.insert(rows[-1] + 1, f"| {n} | 2026-11-04 | **The song Lesson Book: chords built from the root (chat window, her 09:25: for a very beginner, the root first and one note at a time; a picture by 2 or 3 notes, only one line; root position heads touching).** The sample's Ways 2 to 4 now stack the chord: Way 2 just the root, finger 5, all bar (C; the hand moves down to G for G), Way 3 root and fifth on beats 1 and 3 (C G; G D), Way 4 the whole chord in root position (C E G; G B D, fingers 5 3 1). The moving bass (5 1 3 1) is gone from this lesson. In the first line of Ways 3 and 4 the when-dots are pictures of the chord: its notes stacked a third a head apart, so a root-position chord's heads touch, a dashed ring where the third is still to come; the second line keeps plain dots. The left-hand keyboards run G to G, the fingers taken from the pattern. Move it in G: Ways 1 to 3 only (the D chord's third is F sharp). |")
io.open(hist, 'w', encoding='utf-8').write('\n'.join(h)); print('row', n)
