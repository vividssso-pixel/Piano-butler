import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 580 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 581 | 2026-10-20 | **Feedback wording reverted (her call, 13:02).** Row 580's \"Almost!\" wording is undone: a wrong answer says plainly that it was wrong (\"Not that key.\", \"Not quite.\", \"그 건반이 아니에요.\") and then always gives the guide to the right one; the right answer says \"Yes.\" / \"맞아요.\" again. Rule kept: every wrong-answer line is a plain no plus a pointer. Content is `t587` again (built as `t589`). Local commit only, not pushed. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
