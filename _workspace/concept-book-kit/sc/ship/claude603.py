import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 589 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 590 | 2026-10-20 | **Keyboard first, staff on request.** Her feedback: a staff appearing suddenly on a learning screen confuses a beginner. Lesson 11's one-by-one screens are keyboard first again (the three minor scales on the keys, with the ▶ Up and down animation); a \"Write it on the staff\" button then reveals the two staves with the key signature and the green/coral colours (text changes to the key-signature wording). Lessons 9 and 2 likewise: the staff sits behind the same button. The staff in \"Your turn\" (lesson 11) stays, as she liked it. New `ScStaffBtn`. Built by `patch599.py` (`t603`). Checked in English and Korean, no console errors. Local commit only, not pushed. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
