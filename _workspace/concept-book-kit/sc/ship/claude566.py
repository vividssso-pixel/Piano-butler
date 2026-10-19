import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 561 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 562 | 2026-10-19 | **Accidentals lesson 8, one key, two names (agreed plan, 20:21).** New hidden tool `ac-two` ('One key, two names' / 한 건반, 두 이름) is Home lesson 8, after 'Play it'. Whole picture: every black key with a coral arrow from the white key on its left (the sharp name) and a blue arrow from the one on its right (the flat name), the two names stacked above it (coral over blue). One by one: C♯/D♭, D♯/E♭, F♯/G♭, G♯/A♭, A♯/B♭, then the white keys: F is also E♯, C is also B♯, E is also F♭, B is also C♭. Her turn: 'Tap the key for G♭'; a wrong key gets 'G♭ is one half step below G'; the answer shows 'G♭ = F♯'. `AcKeys` names may now be a [sharp, flat] pair drawn as two coloured lines. E♯ = F, B♯ = C, C♭ = B, F♭ = E from her own `SharpFlatMover` text. Source `patch567.py`; checked by me, no console errors. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
