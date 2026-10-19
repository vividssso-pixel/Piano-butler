import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 528 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 529 | 2026-10-19 | **Before you play the piece: a table of every key signature (her 13:41 note).** The old one-key-at-a-time screen (with left and right arrows) is replaced by a table: Signature, Major, Minor side by side, with Sharp keys / Flat keys buttons (C and 0 in both); tap a row to select it. Under it, a small last-bar picture and the guide: same signature, two keys; look at the last bar, the note it ends on (or its chord) is the key, with the two endings spelled out for the selected row (Ends on A -> A major / Ends on F sharp -> F sharp minor). Play its scale and Back kept. Source `patch531.py`; checked by me, EN and KO, no console errors. Note: the 'last note or its chord decides the key' rule is stated in her own words (13:41), not checked against a syllabus; the Korean wording is mine. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
