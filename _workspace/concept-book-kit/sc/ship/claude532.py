import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 529 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 530 | 2026-10-19 | **Key signature table shows the staff (her 13:43 note).** In the Before you play the piece table the Signature column now draws the key signature on a small staff (treble clef with the sharps or flats) instead of the number, so each row reads: staff, major, minor. Source `patch532.py`; checked by me, EN and KO, no console errors. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
