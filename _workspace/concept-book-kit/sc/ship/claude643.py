import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 628 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 629 | 2026-10-22 | **Keys and staff section 1: black keys stay black, keyboards bigger.** Her feedback (08:53-08:54): colours overlapped and hid the keys, and the keyboard pictures were too small. Now the group colours (coral for 2, blue for 3) tint only the white keys; black keys keep their own black (except in the Black keys lesson, where they are the subject). Keyboards render up to 560px wide (close-ups 380px+), with brackets and number rows sized to match. Also asked: show the Questions drills under the Scales and Key signatures Home concepts the same way as Keys and staff (to do next). |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
