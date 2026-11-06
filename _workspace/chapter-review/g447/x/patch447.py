#!/usr/bin/env python3
# Phase 447: the clefs sit on their lines (her 2026-10-12 18:15: '높은음자리표 낮은음 자리표가 딱 g나 f 자리에 맞지 않는것들이').
# ClefGlyph fits each clef's ink between two marks on the staff. The marks were guesses: the treble's top and bottom
# pads were swapped (the comment said 1.3 above / 1.6 below, the code had 1.6 / 1.3), so the curl sat 0.26 of a space
# ABOVE the G line in every treble clef; the bass clef was 0.05 high and slightly small; the alto clef was squeezed into
# 2.6 spaces. The marks now come from the font itself (Noto Music, the page's music font, 1000 units an em):
#   its five-line staff glyph U+1D11A has lines at 12 / 256 / 500 / 744 / 988, a space of 244 units;
#   the G clef (ink -398 to 1334) curls round its second line, 256: top 1.418 spaces over the top line, bottom 1.680
#   under the bottom line;
#   the F clef (ink 101 to 900) has its dots at 534.5 and 754.5, one space (220 units) apart: the F line runs between
#   them (644.5), its top 0.161 of a space over the top line, its tail 3.470 spaces under the top line;
#   the C clef (ink -10 to 1012) is centred on the middle line, 0.098 over the top line, 0.090 under the bottom line.
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(a, b):
    global s
    if s.count(a) != 1: raise SystemExit('found %d: %s' % (s.count(a), a[:90]))
    s = s.replace(a, b)
rep("const CLEF_GLYPH = { treble: { ch: '𝄞', top: 38, topPad: 16, bottom: 30, bottomPad: 13 }, bass: { ch: '𝄢', top: 26, topPad: 1, bottom: 26, bottomPad: 31 }, alto: { ch: '𝄡', top: 28, topPad: 13, bottom: 28, bottomPad: 13 } };",
    "const CLEF_GLYPH = { treble: { ch: '𝄞', top: 38, topPad: 14.63, bottom: 30, bottomPad: 16.35 }, bass: { ch: '𝄢', top: 26, topPad: 1.96, bottom: 26, bottomPad: 34.35 }, alto: { ch: '𝄡', top: 32, topPad: 0.98, bottom: 24, bottomPad: 0.9 } };   // Phase 447: from the font's own geometry (see below)")
rep("""// treble from 1.3 spaces above the top line to 1.6 below the bottom line, bass from the top line
// down 3.1 spaces. That keeps the treble curl on G and the bass dots around F on any font.""",
"""// Phase 447 (her 2026-10-12 18:15: some clefs were off their G and F lines): the box comes from Noto Music's own
// geometry (its staff glyph U+1D11A: lines at 12/256/500/744/988 units, a space of 244). Treble: the curl round the
// second line (256), from 1.418 spaces over the top line to 1.680 under the bottom line. Bass: the F line between the
// dots (534.5 and 754.5, one space of 220 apart), from 0.161 over the top line to 3.470 under it. Alto: the whole staff,
// 0.098 over the top line to 0.090 under the bottom line. The ink scan (alpha > 60) trims the faint edge by about 0.04
// of a space, so the treble and bass boxes are lifted by that much (treble 14.63 / 16.35, bass 1.96 / 34.35). (Before: the treble's two pads were swapped, so every treble
// curl sat a quarter of a space above G.) Tested by measuring every clef on every page (clefcheck.js).""")
open(dst, 'w', encoding='utf-8').write(s); print('447 applied')
