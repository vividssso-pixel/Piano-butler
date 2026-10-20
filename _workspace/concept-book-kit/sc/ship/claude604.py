import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 590 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 591 | 2026-10-20 | **Show the way up, then clear it to come down.** In the Your-turn screens that go up and down (lessons 2, 9 and 11), when she taps the top note the whole way up stays on screen with the line \"That is the way up: look at the pattern. Then we come back down.\" (and, in lesson 11, the full staff). Taps are ignored there; a \"Come down →\" button then clears the colours and the way down starts with only the top note. New state `go`, `pat` in `ScSame`, `ScAll`, `ScMinor`. Built by `patch600.py` (`t604`). Checked in English and Korean, no console errors. Local commit only, not pushed. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
