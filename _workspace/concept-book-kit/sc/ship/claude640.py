import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 626 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 627 | 2026-10-22 | **Keys and staff section 1: her lesson characters and sea/sky taken out; plain wording for children and adults.** Her note (2026-10-22 07:17): the characters (Clara, the Dog, the Exit, the Front door, Grandma, the Apple garden, the Back door) and the other chapter phrases are words she uses in her own lessons; adults must be able to use this too, so Claude recreates the wording. Now every white key is described only by where it sits in its house: C the left door, D inside, E the right door; F the left door, G inside (first), A inside (second), B the right door; low and high are plain (left sounds low, right sounds high); middle C is 'the C in the middle of the keyboard'. Her turn: tap the letter; which letter is the marked key (choices from that house); tap the white key that is 'the left door of the small house' etc. Houses (small house = 2 black keys, big house = 3) stay as agreed earlier. Built by `patch634.py` (+ `kq.jsx`) (`t641`). Opened the five lessons at 390 px in English and Korean: no console errors. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
