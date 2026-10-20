import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 591 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 592 | 2026-10-20 | **Which-minor drill moved to D minor, with staff questions.** The \"Which minor?\" questions (level 64) now use D minor like lesson 11 (the old A-minor wording, \"G♯\" and \"C major's white keys\" is replaced by D minor's key signature, B♭, and C♯), and the answer keyboard shows D minor. Three new questions show the up and down staves with the key signature and ask which minor it is (harmonic, melodic, natural); the staff stays on screen and the keyboard appears after the answer. Built by `patch601.py` (`t605`). Checked in English and Korean, no console errors. Local commit only, not pushed. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
