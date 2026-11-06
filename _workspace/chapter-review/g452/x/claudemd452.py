#!/usr/bin/env python3
# Phase 452: CLAUDE.md -- the log row.
import sys, re
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
ROW = """| 452 | 2026-10-12 | **The token page is full.** Her 22:46 '토큰 늘려주거나 다른걸로 채우던지' (451: the staff mat set's token page was half empty). patch452.py adds, under the ledger strips: 12 coral note tokens ('for the note you are finding'); the five landmark tokens (CutLandmarkToken: a navy letter in a coral ring, so they are not the coral-on-pink letter tokens), named under them bass C, the King's F, middle C, the Queen's G, treble C (Phase 449's names); time-signature tiles 2/4, 3/4, 4/4, two of each (CutTimeTile), exactly one staff tall (4 x CUT_GAP = 38 mm, measured equal to the mat's staff), to lay just after the clef on the tune staff; and a TRY THIS with three set tasks (the five landmarks on the grand staff; a coral token a step above and a skip below a landmark; a 3/4 tile and three tokens a bar, counting 1 2 3). The page fits (en, ko). |
"""
m = re.search(r'^\| 451 \| [^\n]*\n', s, re.M)
if not m: raise SystemExit('row 451')
s = s[:m.end()] + ROW + s[m.end():]
open(p, 'w', encoding='utf-8').write(s); print('CLAUDE.md: log row 452')
