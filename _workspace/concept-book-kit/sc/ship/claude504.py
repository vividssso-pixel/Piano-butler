import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 503 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 504 | 2026-10-19 | **Black keys show both names (her 'yes' at 10:10).** In the Scale finder's black-key step the chips read C♯/D♭, D♯/E♭, F♯/G♭, G♯/A♭, A♯/B♭; the keyboard keeps the scale's own spelling. A grey line under the keyboard says when the same keys are also a real key with another name: D♭ = C♯ major (7 sharps) and F♯ = G♭ major (6 flats), taken from the existing key-signature data; the other three have no real twin, so no line (no theory from memory). Source `patch504.py`; checked by me at 390 EN and 320 KO, no overflow, no console errors. **Sound:** she thinks her own setting differs; parked for later. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
