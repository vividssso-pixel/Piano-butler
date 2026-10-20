import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 596 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 597 | 2026-10-20 | **Scales drill titles show both names for black-key scales.** Question titles read \"C♯ / D♭ major\" (Korean \"C♯ / D♭장조 음계\"), like the keyboard, for D♭, E♭, G♭, A♭ and B♭ (sharp name first for the flats' enharmonic partner). White-key scales are unchanged. New `SSC_BOTH`, `sscTitleName`; `sscScaleName` uses them. Built by `patch606.py` (`t610`). Checked in English and Korean on the build-any-key level, no console errors. Local commit only, not pushed. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
