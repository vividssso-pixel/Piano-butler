#!/usr/bin/env python3
# Phase 430 in CLAUDE.md: the Phase row.   python3 claudemd430.py <CLAUDE.md>
import sys
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
if '| 430 | 2026-10-12 |' in s: raise SystemExit('CLAUDE.md: row 430 already there')
row = """| 430 | 2026-10-12 | **No frame round the pictures online.** Her 00:58 screenshot: in every chapter on the web the thin cut-in-corner frame (VicCutFrame, inside each LbPic picture box) sat crooked, bigger than its white box and spilling out right and below. Cause: on screens >= 900px .pb-main has zoom 1.12, and the frame measured its box with getBoundingClientRect (zoomed px) but drew in the box's own px -- 12% too big. 12 of 12 pictures on wide screens (phones were fine). Fix: on screen (lbScreen) LbPic draws the plain box with no frame; the printed books keep the frame, now measured with the computed width/height (zoom-proof; same pixels as before at 100%). Checks: kit/frame430.js -- online 24 pictures (390 and 1280 px, chapters 1-6), 0 frames, 0 spill; kit/frame430p.js -- printed Lesson Books 36 pictures, all framed and inside the box, also with the page zoomed 1.12; ll429test 82/82, ws419 45, sf405 22, ch1 21, ch2 21, ch3 35, no-song 24, lbcheck chapters 1-6 0 overflow en/ko. Prepared, not applied (her decision waits): today's rabbit butler centred in its frame; four new butler concepts (engraved, bow-tie mark, monocle, seal) -- she liked none of them, a new direction comes from her references. |
"""
i = s.index('| 429 | 2026-10-11 |'); j = s.index('\n', i) + 1
s = s[:j] + row + s[j:]
open(p, 'w', encoding='utf-8').write(s); print('CLAUDE.md ok')
