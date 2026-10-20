import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 601 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 602 | 2026-10-21 | **Home, Pitch: the Scale finder is the last step of Scales; Modes is its own concept.** Her calls (2026-10-21): the Scale finder lives inside Home > Pitch > Scales, at the end (a shortcut to it will be made later); modes are a separate concept, built as a real lesson series, because moving a mode to another key needs its own teaching. `HOME_LIVE['p-scale']`: lessons 1-11, then the Try step with `scale-finder` (`tryLine` now describes the finder). New Home concept `p-modes` (Modes / 선법) after Scales (`HOME_VIRTUAL`, `HOME_LINE`, `HOME_LIVE['p-modes']`, lesson `sc-modes` moved there, its kicker reads Pitch · Modes); the \"Start the drill\" button only shows when a concept has a drill (`live.check`). Built by `patch611.py` (`t615`). Checked the Scales and Modes concept pages and the lesson route: no console errors. Local commit only, not pushed. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
