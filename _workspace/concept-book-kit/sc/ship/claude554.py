import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 550 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 551 | 2026-10-19 | **Whole step shown as two half steps (her 15:31 note).** In the whole step lesson every move is two arrows through the key between: the first navy, the second coral a moment later, the key between and the start pale, the arrival strong, three notes sounding in turn. Whole picture: the chain of whole steps drawn as navy-coral pairs. The example lines now say 'one half step to the black key, one more to D: a whole step', the her-turn line 'From F, a whole step (two half steps) up.', and the picture line 'Whole step (tone) = two half steps.' Arrows take an optional colour and delay. Source `patch554.py`; checked by me, no console errors. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
