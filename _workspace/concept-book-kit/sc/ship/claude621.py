import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 607 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 608 | 2026-10-21 | **Scale finder: white lines between the coloured keys.** Her idea (2026-10-21): white instead of grey between the keys. In `TapKeyboard` `clean` mode a coloured key now has a white 2.5 outline (so neighbours are split by a white line), an uncoloured key keeps the faint grey outline so it does not vanish on the cream page. Built by `patch617.py` (`t621`). Checked Bb major 2 octaves: no console errors. Local commit only, not pushed. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
