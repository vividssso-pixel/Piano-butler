import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 538 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 539 | 2026-10-19 | **Feedback under the question; the link button says Copy link (her 14:38 and 14:39 notes).** Key signatures drill: the Correct / Not quite line now sits directly under the question text, then the staff picture, then the buttons (was between the picture and the buttons). The drill's share button reads 'Copy link' (KO 링크 복사) instead of 'Copy link for a student' (all drills; the kit's 'Copy student link' is unchanged). Sources `patch541.py`, `patch542.py`; checked by me, EN and KO, no console errors. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
