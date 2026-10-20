import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 574 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 575 | 2026-10-20 | **Scales lesson 6: starting on a black key (`sc-black`, `ScBlack`).** Six screens: B♭ major right hand (the thumb only ever plays white keys: C and F), then E♭, A♭ and D♭ (thumbs again on C and F), the left hand (one shape for all four: 3-2-1, 4-3-2-1, 3), and G♭ / F♯ (three black keys in a row, fingers 2-3-4, thumbs on C♭ (B) and F). Her turn: pick B♭ E♭ A♭ D♭ G♭ and a hand, tap the keys where the thumb goes (both), a wrong black key says the thumb only ever plays white keys, a wrong white key says it is not a thumb key; when both are found the whole fingering appears. Colouring as in lesson 4 (3-group coral, 4-group blue, everything else plain); a negative length in `SC_LENS` marks a plain group; `scIdx` now reads the root from `SCALES[key].rootPc` so G♭ works. Facts and finger numbers only from her `SCALE_PATTERNS` text and `SCALES[key].octaves[1]`. Home `p-scale` lists lessons 1-6. Korean wording is mine, unverified. Built by `patch581.py` (`t581`). Checked in English (all five keys, both hands) and Korean, no errors. Local commit only, not pushed. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
