import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 611 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 612 | 2026-10-21 | **Scale finder: one control for the relative key.** Her idea (2026-10-21): the \"Relative major/minor\" button does the same as the Major/Minor chips (they already move to the relative key on the same circle position), so remove the button and put a small \"relative\" mark between the Major and Minor chips. The button is gone; the chip row is now `← ♭ | Major ⇄ relative Minor | ♯ →`. The line \"Its relative minor is ...\" stays. Built by `patch622.py` (`t625`). Checked E-flat minor to Major gives G-flat major, no console errors. Local commit only, not pushed. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
