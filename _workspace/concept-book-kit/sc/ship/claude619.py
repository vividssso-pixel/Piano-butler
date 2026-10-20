import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 605 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 606 | 2026-10-21 | **Scale finder: finger numbers inside the keys, the old finder's blue and green.** Her question and request (2026-10-21): are finger numbers inside the keys clearer when both hands are shown, and use the old design's colours. Recommendation taken: inside the key, because a number floating above a black key can be read as belonging to a neighbouring white key, and it sits right beside the note name. `ScKeys` gets `inKey` (numbers drawn in the key, coral, above the note name); `TapKeyboard` gets `nameCol` and two mark styles `seg3` (blue `#93d0f5`) and `seg4` (green `#98e6ab`), the same `SEGMENT_COLORS` as the old finder, also used for the legend. Built by `patch615.py` (`t619`). Checked Bb major, 2 octaves, both hands, staff open: no console errors. Local commit only, not pushed. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
