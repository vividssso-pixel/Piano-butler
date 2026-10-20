import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 578 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 579 | 2026-10-20 | **Scales lesson 8, her turn made easy for young children (her call, 12:54).** The left-hand fingers are asked in order from the left, one note at a time, with an orange box marking the current column across both rows; the group shapes (coral 3, blue 4) are always visible and only the digits are hidden (?), so the shape itself guides; one short line (\"Look at the left-hand row under the orange box\"); after a wrong tap the right finger gets a ring and the line says to tap the ringed finger. Names row placed explicitly so the highlight cannot shift it. Built as `t587`. Checked in English and Korean, round completes, no errors. Local commit only, not pushed. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
