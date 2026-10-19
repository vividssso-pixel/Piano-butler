import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 562 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 563 | 2026-10-19 | **Accidentals lesson 9, double sharp and double flat (her 20:25: 'double sharps and flats belong in this category').** New hidden tool `ac-double` ('Double sharp, double flat' / 겹샵, 겹플랫) is Home lesson 9, after 'One key, two names'. Whole picture: F𝄪 to G and B𝄫 to A as two half-step arrows (navy then coral, the same as the whole step in lesson 2), 'Double sharp = two half steps up. Double flat = two half steps down. Just like a whole step.' One by one: C𝄪=D, E𝄪=F♯, F𝄪=G, A𝄪=B, D𝄫=C, F𝄫=E♭, G𝄫=F, B𝄫=A (all from her `ALL_NAMES` table). Her turn: tap the key for a double-sharp or double-flat name. Glyphs use `MUSIC_FONT`. Lesson 8 now also names the term 'enharmonic' / 딸이름한소리(이명동음), her wording from the chromatic tool. Source `patch568.py`; checked by me, no console errors. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
