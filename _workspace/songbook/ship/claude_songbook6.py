"""Notes: Ways 2-4 as lead sheets (her 4 Nov 09:21)."""
import sys, io, re
hist = sys.argv[1]
h = io.open(hist, encoding='utf-8').read().split('\n')
rows = [i for i, l in enumerate(h) if re.match(r'^\| \d+ \|', l)]
n = max(int(h[i].split('|')[1]) for i in rows) + 1
h.insert(rows[-1] + 1, f"| {n} | 2026-11-04 | **The song Lesson Book: the chords as a lead sheet (chat window, her 09:21: like the photo, show only when to play).** Ways 2 to 4 of the sample are no longer grand staves: one treble line with the chord letters above, and under each bar only the left hand's when (Way 2 the held note's finger and a grey line; Way 3 coral dots on beats 1 and 3; Way 4 a finger number a beat, 5 1 3 1 or 4 1 2 1), drawn from the same pattern data; beside each Way two small left-hand keyboards, C and G, the notes lit with their fingers. Why: the bass clef comes in lesson 8 (its room), chord letters are a real skill (lead sheets), and Move it changes only the letters. check.js requires the when rows. |")
io.open(hist, 'w', encoding='utf-8').write('\n'.join(h)); print('row', n)
