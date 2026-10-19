import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 504 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 505 | 2026-10-19 | **Key finder: add/remove one accidental at a time; circle of fifths moved out (her 11:07 note).** On the order screen a row of [−] [▶ Say the order] [+] adds or removes one sharp (flat); the staff, numbers, words and zigzag follow, and + plays the new note. The Sharps/Flats chips are gone: Next goes sharp order → flat order (Back returns). The Explore buttons are removed from both finders and the circle-of-fifths step is out of the Key finder, so it is four steps again (orders, find the major, find the minor, before a piece); the concept book is ten pages. The circle stays as its own Toolbox tool. Source `patch505.py`; checked by me at 390, EN and KO, print pages without overflow, no console errors. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
