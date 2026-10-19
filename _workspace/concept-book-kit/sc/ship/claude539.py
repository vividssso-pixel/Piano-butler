import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 536 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 537 | 2026-10-19 | **Key signatures drill: the extras sorted (her 14:23 note).** Coral note and Accidentals leave this drill (they belong to the Accidentals concept's drill when that is rebuilt); Listen leaves (it does not find a key; an 'is it major or minor by ear' idea is parked for the minor / aural side); My keys leaves (it overlaps the main levels); the bass staff is no longer its own level: it is mixed into Major: sharps, Major: flats, All 15 and Relative minor (about a third of the questions are on the bass staff). The drill is now Sharp order, Flat order, Major: sharps, Major: flats, All 15, Relative minor, Last note, and More practice: Which notes?, Written right. The removed questions stay in the code for their own concepts. Source `patch539.py`; checked by me, no console errors. Note: the book's page-6 drill text and workbook still describe the old ten levels (book rework). |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
