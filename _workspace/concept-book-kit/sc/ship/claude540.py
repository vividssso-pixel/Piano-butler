import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 537 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 538 | 2026-10-19 | **Right / not quite sits between the question and the buttons (her 14:33 note).** In the Key signatures drill (lesson mode) the 'Correct!' / 'Not quite: it was ...' line now appears right under the question and above the answer buttons (a little bigger); Next sits below the buttons. Other drills keep the line under the buttons: a drill opts in with `feedbackAbove` (the shared `DrillFeedback` line and an `fbAbove` prop on its question component, which uses display: contents and order). Game mode unchanged. Source `patch540.py`; checked by me, EN and KO, no console errors. Open: whether to do the same in every drill as each concept is rebuilt. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
