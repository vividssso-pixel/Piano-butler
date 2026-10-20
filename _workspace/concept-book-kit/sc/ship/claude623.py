import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 609 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 610 | 2026-10-21 | **Scale finder: back to the Scales lessons' coral and blue, stronger; up and down now waits for a button at every thumb.** Her decisions (2026-10-21): keep the coral (group of 3) and blue (group of 4) of the Scales lessons instead of the blue/green trial, and find a way to make the groups stand out; when playing up and down, stop at every thumb and go on only when she presses a button, so there is time to take it in. The finder's fingering keyboards now use a stronger coral (`#f6ac93`, black keys `#c0431f`) and blue (`#a3baf0`, black keys `#3b4fa8`) than the lesson pale fills, with navy numbers, the same white separators and thumb rings; legend swatches match. Up and down now plays to the next thumb, says whose thumb it is, and shows a \"Next\" button (\"다음\"); Stop ends it. Built by `patch619.py` (variant A) and `patch620.py` (`t623`). Checked in 1 and 2 octaves in the test run, Korean playback stops in order (RH, LH, LH top, LH, RH) and no console errors. Local commit only, not pushed. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
