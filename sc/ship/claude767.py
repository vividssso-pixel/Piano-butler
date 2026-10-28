import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 738 |')]
assert len(idx) == 1
assert not any(l.startswith('| 739 |') for l in lines)
rows = [
"| 739 | 2026-10-29 | **The book redo starts: fun first on paper, a prototype in chapter 2 (Build CT; her 23:58 'then let's start the Lesson Books'; the rule of 28 Oct 09:56: fun first, the How to Blitz way, its approach never its content).** An audit of the Beginner floor's books (13 Lesson Books of 6 to 8 pages, 12 Workbooks; ear prep has none by design) found them already short and pictured, with 'At the piano', 'Remember' and the Workbook's Try it / Your turn / Play; what the rule asks and they lack is the quick challenge with a streak and the small joke. Two components, print and online alike (the Lesson Book is the online lesson): LbChallenge (under 'At the piano': a streak of circles to colour, green, or three times to beat) and LbJoke (the butler's joke on the opener: the answer upside down in print, one tap online). Chapter 2 only, for her to judge before the other twelve: the joke 'Why do the piano keys never get lost? They always know which house they live in.'; the house race (time), the small-or-big-house call (5 in a row), middle C in 3 seconds (5 in a row), the roof walk with no gap and no bump (5 in a row). The paper floor checkpoints are next: the app's question components print as screen UI (pw767.js), so the checkpoint needs its own paper items in the books' style. Source patch767.py; tests ct767.js (no overflow in the Lesson Book, Workbook, spread and teacher copy; online in en and ko), bk767.js (the audit). |",
]
lines[idx[0] + 1:idx[0] + 1] = rows
open(p, 'w', encoding='utf-8').write('\n'.join(lines))
print('row 739 added')
