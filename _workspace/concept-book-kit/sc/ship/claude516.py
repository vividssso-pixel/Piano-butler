import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 515 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 516 | 2026-10-19 | **Major key: three examples, the half step on the staff, flats on their own (her 11:55 note).** The rule screen now runs three examples (3, 5 and 2 sharps/flats; Another one, then Try it). On the staff, step 2 draws the key note after the signature with a half-step arrow (sharps) or on the flat itself (flats). The Learn list is now six lessons: Sharp order, Flat order, Major key: sharps, Major key: flats, Minor key, Before a piece; each of the two major-key lessons is its own tool (`kf-msharp`, `kf-mflat`), the old combined `kf-major` stays hidden. `KSStaff` gains optional `tonicPos`, `tonicFrom`, `tallBox`. Source `patch516.py`; checked by me, EN and KO, no console errors. Note: the staff arrow is my drawing (a small curve with a half-step label); examples 3, 5 and 2 are my choice. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
