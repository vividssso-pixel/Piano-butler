import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 502 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 503 | 2026-10-19 | **Key finder follows her teaching order (her 09:34).** Step 1 is only the orders: the sharp order, then the flat order (seven of each; chips to switch, 'Flat order →' to go on). Step 2 is the major key: a rule screen for sharps (a beat to breathe), then the count unfolding 1 to 7, then a rule screen for flats (their own rule), then 1 to 7. Step 3 minor, 4 circle, 5 before a piece (unchanged). The three pills now jump to steps 1 / 2 / 5. The concept book follows, eleven pages: the orders, sharps: the key, flats: the key, minor, circle, before a piece, three scale pages, checks. Source `patch503.py`. Checked by me in EN and KO: every phase by screenshot, the full walk through steps 1 and 2 to step 3, all eleven print pages with no overflow, no console errors. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
