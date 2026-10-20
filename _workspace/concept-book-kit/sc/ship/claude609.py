import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 595 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 596 | 2026-10-20 | **Scales drill: two extra chips removed.** Her call: \"D and B♭ signs\" (key-signature content, belongs to the Key signatures chapter) and \"My keys\" (the clock was unclear and it did not belong to any lesson) are removed from the Scales drill; \"More practice\" now holds only Listen. Removed from `SSC_LEVELS` only; the question code stays in the file and the Key signatures drill's own \"My keys\" is untouched. Opening the old level numbers 8 and 10 still gives no error. Built by `patch605.py` (`t609`). Checked in English and Korean. Local commit only, not pushed. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
