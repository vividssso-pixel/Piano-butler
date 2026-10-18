import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 501 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 502 | 2026-10-19 | **Sharps and flats open on the order, then unfold one by one (her 09:31).** Key finder steps 1 and 2 no longer start with 'What key has 7♯?'. They open on 'The order of sharps' (or flats): the staff with all seven, the sentence, 'Say the order' with the zigzag, one line, one Next. Then the count unfolds from 1: tap the last ♯ (or second-to-last ♭), see the key, 'One more ♯ →' up to 7, then Next; the later counts stay dim until reached; '← The order' goes back. Source `patch502.py`; checked by me in EN and KO with screenshots of each phase, no console errors. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
