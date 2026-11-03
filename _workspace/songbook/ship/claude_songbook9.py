"""Notes: root only, Move it out, the materials on page 1 (her 4 Nov 10:16)."""
import sys, io, re
hist = sys.argv[1]
h = io.open(hist, encoding='utf-8').read().split('\n')
rows = [i for i, l in enumerate(h) if re.match(r'^\| \d+ \|', l)]
n = max(int(h[i].split('|')[1]) for i in rows) + 1
h.insert(rows[-1] + 1, f"| {n} | 2026-11-04 | **The song Lesson Book: root only, no transposing yet, the materials shown (chat window, her 10:16).** Move it to G is out of the sample (later; it looked too much). The chords: no root position yet, the root only, so the ways grow by rhythm: Way 2 hold the root (C with 5, G with 1, in C position), Way 3 the root on beats 1 and 3, Way 4 on every beat; the rows show only finger numbers and hold lines (no chord pictures). The position keyboard moved into Listen and sing, with steps and the one skip (E up to G, in which bar?). Page 1 now shows what the song is made of before the rhythm lines: the time (4/4: four beats in a bar, a crotchet a beat) and the note values with beat dots. Three pages. My proposal for the book: root only first (rhythm ladders), then the two ends of the hand (5 and 1 together), then the whole chord with a one-line rule and a picture, the last in late Level 0 or Level ½. |")
io.open(hist, 'w', encoding='utf-8').write('\n'.join(h)); print('row', n)
