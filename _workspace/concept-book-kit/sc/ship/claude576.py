import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 570 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 571 | 2026-10-19 | **Scales lesson 2: the same pattern from any note (`sc-same`, `ScSame`).** Eight story screens: G major (start G, T T S T T, the pattern wants a whole step from E, F is only a half step, so F♯; F♯ to G a half step), then F major (T T, the pattern wants a half step from A, B is a whole step, so B♭; then T T T S). Then her turn: eight start keys (G D A E F B♭ E♭ A♭), the line names the next step (whole or half), she taps the key; note names come from her `spellScale`, so D major shows F♯ and C♯. Facts only from her `MajorShapeCard` text (G: the 6th-to-7th step must be a tone, so F becomes F♯) and the key signatures she already has (F: B♭). New `ScKeys` (a two-octave board cropped to one scale with the arrow overlay) and a `vx` crop prop on `TapKeyboard`. Home `p-scale` lists lessons 1-2. Korean wording is mine, unverified. Built by `patch576.py` (`t576`). Checked in English and Korean, D major played to the end, no errors. Local commit only, not pushed. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
