#!/usr/bin/env python3
# Phase 438: CLAUDE.md -- book rule 9's townhouse: no lamps, pictures without frames, the dome in your room; the log row.
import sys, re
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
def sub(pat, rep):
    global s
    s, n = re.subn(pat, rep, s)
    if n != 1: raise SystemExit('%d x %s' % (n, pat[:60]))
sub(r'every floor with its own wallpaper, floor and lamp \(lamps lit coral with a soft glow\), NO STAIRS', "every floor with its own wallpaper and floor, NO LAMPS (Phase 438, '조명들 다 빼주고'), NO STAIRS")
sub(r"each chapter's picture in a cut-in-corner frame(\s+)hung on cords;", r"each chapter's picture on the wall with NO FRAME\1(Phase 438) and your room's picture under a wide glass dome on a little table instead of Clara;")
ROW = """| 438 | 2026-10-12 | **The house: no frames, no lamps, the glass dome in your room.** Room objects shown at 12:53 (A frame, B glass dome, C window, D oval medallion, E fireplace) and at 13:17 her own idea F, no frame; her 14:45 '유리돔 빼고 쓰자. 대신 조명들 다 빼주고, 클릭될 때 클라라 안보여도 되고 대신에 유리돔을 보여주게 ... 유리돔 옆으로 좀 더 넓게'. patch438.py: thPic draws the picture alone (0.8, all the same ink; grey only on the guides' page for rooms without a guide); thDome draws your room's picture under a wide dome (R 28, a coral knob) on a little round table -- it replaces the pawn as the map's figure; the floor lamps, the hall's sconces and the lanterns by the steps and all their glow are gone; a floor's names may go down to 12.5 to stay on one line. Guides: the front page's house and sharing picture redrawn, index rebuilt. Book rule 9 updated. Checks: house438test (5 widths, en/ko) 63/63 (dome inside your room, no glow), tn437test 11/11, house436base 72/72. |
"""
m = re.search(r'^\| 437 \| [^\n]*\n', s, re.M)
if not m: raise SystemExit('row 437')
s = s[:m.end()] + ROW + s[m.end():]
open(p, 'w', encoding='utf-8').write(s); print('CLAUDE.md: rule 9, log row 438')
