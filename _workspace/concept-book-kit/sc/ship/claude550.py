import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 546 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 547 | 2026-10-19 | **Accidentals lessons 1 and 2: half step = semitone, whole step = tone (her 15:18 note).** Lesson 1 is titled 'Half step = semitone' (ko 반음 = semitone) and a new lesson 2 'Whole step = tone' (온음 = tone) follows it in the same shape: the whole picture (whole steps as a chain of arcs, C to D to E and so on), five examples one at a time (skip one key; black to black; down), then her turn. Her turn is clearer in both lessons: tap a key to stand on it (pale), then press 'Half step up' or 'Whole step up' / '... down'; only that one move is drawn, the arrival strong, with the line 'From F, a half step up.' (no more both neighbours at once). Home lessons are now ac-half, ac-whole, then the older ones. Source `patch550.py`; checked by me in English, no console errors. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
