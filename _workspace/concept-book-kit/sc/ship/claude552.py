import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 548 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 549 | 2026-10-19 | **No line starts with the article 'A' in the half and whole step lessons (her 15:25 note: it read like the note name A).** 'A half step (semitone) is...' is now 'Half step (semitone) = the very next key.', 'A whole step (tone) is...' is 'Whole step (tone) = two half steps: skip one key.', and 'D. A whole step.' is 'to D: a whole step.' The arrows of Phase 548 were already shared by both lessons (one arrow component). Source `patch552.py`; checked by me, no console errors. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
