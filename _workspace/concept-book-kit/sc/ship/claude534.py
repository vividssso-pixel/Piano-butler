import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 531 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 532 | 2026-10-19 | **Home drill is the drill only; sharp order and flat order are separate checks (her 14:06 note).** A drill opened from the Home (teacher view) no longer shows the old Learn tab, the previous / next chapter arrows, 'Builds on' or 'Next on your path': just Back to the concept and the drill. (The old chapter pages are still in Chapters and Toolbox.) Key signatures drill: the order check is split into Sharp order and Flat order; levels now read Sharp order, Flat order, Major: sharps, Major: flats, All 15, Relative minor, Last note, then More practice. Source `patch534.py`; checked by me, EN and KO, no console errors. Open: whether the twelve-keys circle picture goes into lesson 6 (I suggest a List / Circle toggle, not a second picture on the same screen). |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
