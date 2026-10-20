import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 583 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 584 | 2026-10-20 | **Chromatic lesson: fingering instead of semitone tapping (her call, 13:29).** The whole picture now shows the 7 white keys and the 5 black keys put in between in another colour (orange), \"all twelve, one half step at a time\". Her turn is the fingering: choose right or left hand and, for the 13 keys from C to C in order, press the finger (1-5); the answered keys turn green and show their finger (staggered rows, ring on every thumb). A wrong finger says so and gives the rule (every black key 3; the lowest note the thumb; F and C right hand / E and B left hand finger 2; other white keys the thumb). Built as `t593` (edit of `t592`). Checked in English and Korean, both hands complete, no errors. Local commit only, not pushed. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
