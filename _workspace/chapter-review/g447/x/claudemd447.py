#!/usr/bin/env python3
# Phase 447: CLAUDE.md -- the log row.
import sys, re
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
ROW = """| 447 | 2026-10-12 | **The clefs sit on their lines.** Her 18:15 (practising the drills with students): '높은음자리표 낮은음 자리표가 딱 g나 f 자리에 맞지 않는것들이 있던데 검토해서 고쳐줘'. Every clef is ClefGlyph, which scans the glyph's ink on a canvas and fits it between two marks on the staff; the marks were guesses, and the treble's two pads were swapped (comment 1.3 over / 1.6 under, code 1.6 / 1.3), so EVERY treble curl sat 0.26 of a space above the G line; the bass sat 0.05 high and a little small; the alto was squeezed into 2.6 spaces. patch447.py: the marks come from Noto Music's own geometry (its staff glyph U+1D11A: lines at 12/256/500/744/988, a space of 244; the G clef curls round 256; the F clef's dots at 534.5 and 754.5, one space of 220 apart, the F line between them; the C clef centred on 500), less the scan's 0.04-space trim: treble top 38 + 14.63 / bottom 30 + 16.35, bass top 26 + 1.96 / 26 + 34.35, alto 32 + 0.98 / 24 + 0.9. Measured on every page that shows a clef (kit/clefcheck.js: maps the font's own G/F/C line through each clef's transform onto the staff it sits on): 26 drill pages and the lesson, Workbook and Teacher books of chapters 6, 7, 11 and 15, 306 clefs, every one 0.00 spaces off (before: treble -0.26, bass -0.05). The guide pages' drawings with clefs (reading-the-staff, ledger-lines, tones) and the ledger-lines worksheet pictures re-exported; guides rebuilt --final. Checks: lbcheck and wbcheck for chapters 6, 7, 11, 15 pass; sf405 22, ws419 45, ll444 82, tn444 16, ch3app397 35, ll431 24. |
"""
m = re.search(r'^\| 446 \| [^\n]*\n', s, re.M)
if not m: raise SystemExit('row 446')
s = s[:m.end()] + ROW + s[m.end():]
open(p, 'w', encoding='utf-8').write(s); print('CLAUDE.md: log row 447')
