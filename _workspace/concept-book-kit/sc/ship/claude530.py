import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 527 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 528 | 2026-10-19 | **Relative minor: a major and a minor are one set (her 13:36 note).** The minor lesson is now titled 'Find the relative minor key' (KO: 나란한 단조 찾기) and opens with one picture: a key signature (3 sharps) with both of its keys lit on the keyboard, the line 'Every key signature has two keys: a major and its relative minor', and A major + F sharp minor. Next goes to step 1 (find the major), Back returns to it. Source `patch530.py`; checked by me, EN and KO, no console errors. Note: the Korean title uses the existing word for relative key (나란한); the Korean wording is unverified. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
