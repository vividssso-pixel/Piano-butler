import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 581 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 582 | 2026-10-20 | **Scales lesson 9: all twelve keys (`sc-all`).** One pattern T T S T T T S, twelve start notes. Whole picture (C major on the keyboard with arrows and the T/S pills), then one by one in three screens: white-key starts (C G D A E F B), black-key starts (B♭ E♭ A♭ D♭ G♭), all twelve; on each screen tapping a key chip slides the same pattern onto that start note (arrows, note names, pills, root plays). Her turn: pick any of the twelve and tap its eight notes in order; a wrong key says it is wrong and names the step to take (whole or half step up). No new music facts, only the pattern and spellings already in `SCALES`. Home p-scale lessons now 1-9; next 10 chromatic scale, 11 the minors, then the drill chips. Korean wording is mine, unverified. Built by `patch588.py` (`t590`). Checked in English and Korean, round completes, no errors. Local commit only, not pushed. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
