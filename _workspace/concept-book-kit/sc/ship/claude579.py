import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 572 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 573 | 2026-10-20 | **Scales lesson 4: the standard fingering (`sc-finger`, `ScFinger`); the hats over the degree numbers removed (her call, 11:35).** Lesson 3's numbers now print plainly (1 2 3 …), no hat (`patch578.py`). Lesson 4: whole picture (C major right hand, finger numbers over the keys, thumbs coral); seven steps (right hand: a group of 3, the thumb goes under, a group of 4, finger 5 on top; left hand: the mirror, 5 at the bottom, then 4 fingers, then 3); then G major to show the same fingers for all five keys (C G D A E); then her turn: choose the key (C G D A E) and the hand, a marked note comes up in random order and she presses the finger button 1-5 (wrong: \"Not that finger\"), eight notes per round. Facts only from her `SCALE_PATTERNS` text and the `SCALES[key].octaves[1]` finger arrays (RH 1 2 3 1 2 3 4 5, LH 5 4 3 2 1 3 2 1). Home `p-scale` lists lessons 1-4. Korean wording is mine, unverified. Built by `patch579.py` (`t579`). Checked in English and Korean, both hands played to the end, no errors. Local commit only, not pushed. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
