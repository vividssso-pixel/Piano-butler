import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 569 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 570 | 2026-10-19 | **Scales concept (`p-scale`) started: lesson 1, the major scale pattern (her go, 23:41).** Plan of eight lessons: 1 the pattern T T S T T T S; 2 the same pattern from every note (G: F♯, F: B♭); 3 degree numbers and names; 4 fingering, the standard shape; 5 keys with other fingering; 6 all twelve keys; 7 the chromatic scale (moved from Accidentals); 8 three kinds of minor. Lesson 1 (`sc-shape`, `ScShape`, built on `AcKeys`): the whole picture (C major with the seven steps, whole = navy, half = coral, plus a T/S strip), one step at a time with sound, then her turn: the line names the next step (whole or half) and she taps the key. Facts only from her `MajorShapeCard` (T T S T T T S; the half steps between notes 3-4 and 7-8, E-F and B-C). Home `p-scale` now lists only this lesson (old Scale finder and Five notes stay in the Toolbox); the drill is still the old one and is rebuilt after the lessons. Korean wording is mine, unverified. Built by `patch575.py` (`t575`). Checked in English and Korean, no errors. Local commit only, not pushed. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
