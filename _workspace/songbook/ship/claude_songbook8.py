"""Notes: the lesson re-ordered and cut to three pages (her 4 Nov 10:08)."""
import sys, io, re
hist = sys.argv[1]
h = io.open(hist, encoding='utf-8').read().split('\n')
rows = [i for i, l in enumerate(h) if re.match(r'^\| \d+ \|', l)]
n = max(int(h[i].split('|')[1]) for i in rows) + 1
h.insert(rows[-1] + 1, f"| {n} | 2026-11-04 | **The song Lesson Book: the lesson re-ordered and the repeats cut (chat window, her 10:08: say and clap first with the position, then listen and sing with the note boxes under it, then the chords in order; the same tune printed again and again is too much).** Now three A4 pages: 1 Say and clap (the rhythm lines and the C position keyboard); 2 Listen and sing (the tune with words, the letter boxes for bars 1 to 4 under the words, the QR); 3 Play it four ways: a legend of the four ways beside the left-hand C and G keyboards, then one score, the tune with right-hand fingers and chord letters and under it a numbered row for each of Ways 2 to 4 (chord pictures in the first line); Play together; 4 Move it to G (bars 1 to 4); 5 Check. The tune is printed three times and once in G, where it was printed eight times. The separate Read it part and its step-or-skip question are gone (the letter boxes moved under Listen and sing); the music is drawn a little larger (1750 units a line, not 2100). |")
io.open(hist, 'w', encoding='utf-8').write('\n'.join(h)); print('row', n)
