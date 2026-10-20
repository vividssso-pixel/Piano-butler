import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 567 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 568 | 2026-10-19 | **Accidentals drill: lessons 1 and 2 share two chips instead of four (her call, 22:29: merge the drill chips only; the two lessons stay separate).** Chip 1–2 \"Half or whole?\" now mixes the half-or-whole question with the white-neighbours question (E F, B C); chip 1–2 \"Play the step\" mixes half and whole steps, up and down, in one level. The old chips Play a half step / White neighbours / Play a whole step are gone from this drill (the old Tones drill keeps its own). Korean wording for the new chip (반음·온음 치기) is mine, unverified. Built by `patch573.py` (`t573`). Checked: both chips open in English and Korean with no errors; all four half/whole and up/down prompts appear. Local commit only, not pushed. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
