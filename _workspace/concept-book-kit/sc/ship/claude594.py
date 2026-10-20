import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 584 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 585 | 2026-10-20 | **The way back down is checked too (her ask, 13:32).** In her turns of lesson 2 (same pattern), 9 (all twelve keys), 11 (three kinds of minor) and 10 (chromatic fingering) the scale now continues down after the top note: the student taps the same keys coming down (14 taps for a major or minor scale; 25 for the chromatic scale, where the names switch to flats on the way down and the lowest note takes the thumb again). Step pills grow to 14 (T/S, T+S) and arrows go both ways. Melodic minor comes down as the natural minor (her card): at the top the line says so, and tapping F♯ or G♯ on the way down gets \"Not that key. Coming down, the melodic minor plays the natural minor: G, not G♯.\" Harmonic minor comes down on the same notes as up. New helper `scStepWord`. Built by `patch591.py` (`t594`). Checked in English and Korean for all four lessons, melodic wrong-key message checked, no errors. Local commit only, not pushed. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
