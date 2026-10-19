import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 544 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 545 | 2026-10-19 | **Accidentals, lesson 1 rebuilt in the key signatures template: the half step (her 15:09 note).** New hidden tool `ac-half` replaces the old 'Tone or semitone' as Home lesson 1. Screens: the whole picture (every key joined to its next key by an arc, one octave with the B below and the C above), then five examples one at a time (C up to a black key; E to F; D down; a black key up to a white one; B to C) with the start pale and only the arrival strong, then her turn (tap any key: its two neighbours light with arcs). White keys named, black keys not (the sharp and flat names come in lessons 2 and 3). Old lessons 2 to 13 unchanged until rebuilt. Source `patch548.py`; checked by me in English, no console errors. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
