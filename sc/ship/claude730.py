import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 702 |')]
assert len(idx) == 1
rows = [
"| 703 | 2026-10-27 | **Things to make, batch 3 (Build BK; board call 25).** A tune from one interval (Intervals): choose a 2nd, 3rd, 4th, 5th or octave and build a tune of up to twelve notes hopping only by it, up or down, on the staff with its note names, then play it. Add a sharp or a flat (Accidentals): the first line of Ode to Joy on the staff; tap any note name to make it sharp, flat, then natural again; Every E flat; hear the colour change. One tune, four styles (Styles): Twinkle over a Baroque band (harpsichord, a moving bass), a Classical one (Alberti bass), a jazz one (swing, a walking bass, 7th chords) or a pop one (a chord on every beat); Tune off lets the child play the tune on top, the key to play lit. Transpose a tune (Key signatures) gains My tune: up to eight notes on C D E F G become the tune to move. Source patch730.py; test bk730.js. chsweep 46 chapters 0 errors, booksweep 0 errors, regression 332 lessons, 54 drills, 0 errors. Local commit only, not pushed. |",
]
for r in reversed(rows): lines.insert(idx[0] + 1, r)
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
