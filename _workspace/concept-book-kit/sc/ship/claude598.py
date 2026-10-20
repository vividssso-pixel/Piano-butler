import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 586 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 587 | 2026-10-20 | **Scales drill rebuilt to match the eleven lessons.** Main chips, each carrying its lesson number: 1 Whole or half?, 1 Where is the half step?, 1–2 Build the scale, 3 Which degree?, 3 Name the note, 4–8 Which finger? (new `finger12`: any of the twelve keys, either hand, on the lessons' own keyboard, the coral key, fingers shown with rings after the answer), 9 Build any key (new `build12`: tap the eight notes of any of the twelve major scales), 10 Chromatic fingers (new `chrom`: which finger on a key of the chromatic scale from C, either hand), 11 Which minor? (new `minform`: five questions from her card, answer shown on the A-minor keyboard), 11 The raised 7th. More practice: Listen, D and B♭ signs, My keys. The old white-keys-only \"Which finger?\" is replaced by the all-keys one. New `genScNew`, `ScDrillQ`, `SC_MINQ`; levels 61–64 are new numbers, 1/2/3/5/6/9 and the extras keep theirs, so saved progress stays. Built by `patch594.py` (`t598`). Checked in English and Korean: every new chip opens, answers and moves on, build-any-key completes, no errors. Local commit only, not pushed. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
