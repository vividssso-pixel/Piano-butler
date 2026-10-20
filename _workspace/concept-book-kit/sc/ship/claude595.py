import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 585 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 586 | 2026-10-20 | **Lesson 8 (both hands) goes down too (her yes, 13:36).** Her turn is now 15 steps: the left-hand finger for each column going up, then the same fingers backwards coming down (the left-hand digits are hidden again for the way down; \"Now come back down: the same fingers, backwards\"). Her rule applied here too: a wrong finger now says \"Not that finger.\" and points to the ringed finger (it said \"Almost!\"). Built as `t595`. Checked in English and Korean, the full 15-step round completes, no errors. Local commit only, not pushed. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
