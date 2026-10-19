import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 509 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 510 | 2026-10-19 | **Learn is five separate lessons (her 11:31 and 11:32 notes: 5장 전부).** In Scales and keys on the Home, Learn now opens a list of five numbered cards: Sharp order, Flat order, Find the major key, Find the minor key, Before a piece. Each is its own hidden tool (`kf-sharps`, `kf-flats`, `kf-major`, `kf-minor`, `kf-piece`) that shows one lesson with no number tabs and no three-pill chain, only Back and Next; the Back link returns to the Learn list. `KeyFinder` takes an `only` prop; the four-step Key finder tool and the printed book are unchanged. Source `patch510.py`; checked by me, EN and KO, all five lessons open, no console errors. Not done yet: a final Done button inside a lesson (the top Back link leaves it). |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
