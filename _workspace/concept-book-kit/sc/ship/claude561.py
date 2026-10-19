import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 556 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 557 | 2026-10-19 | **Accidentals lesson 6, signs in a bar (her 16:02: 'show how sharp, flat and natural apply in a bar').** New hidden tool `ac-bar` ('Signs in a bar' / 마디 안의 임시표) is Home lesson 6; the old 'How long an accidental lasts' (`accidental-bar`) is out of the list (tool kept). Whole picture: one treble staff, bar 1 F♯ G F B♭ B♮, bar line, bar 2 F, the altered notes in coral with their names under them; 'A ♯ or ♭ lasts until the bar line. A ♮ cancels it. A new bar starts plain.' One by one: each note appears, plays, and its key lights on the keyboard below, with a line (a sign only changes its own note; still F♯ with no sign; the natural cancels the flat; the bar line ends the sharp). Her turn: a '?' note on the staff, she taps the key it plays; 'Another →'. Facts are the ones in her `ACC_EXAMPLES` lines (lasts to the bar line, natural cancels, new bar plain). Source `patch562.py`; checked by me, no console errors. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
