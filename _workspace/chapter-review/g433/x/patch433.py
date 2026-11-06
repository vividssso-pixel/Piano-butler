#!/usr/bin/env python3
# Phase 433 (her 2026-10-12 00:53 "go back to the rabbit, and centre him", decided 08:34 "change the mascot to the rabbit"): the butler is the rabbit again, centred in his oval.   python3 patch430.py <drills.src.html> <rabbit430.uri.txt>
import sys
src, uri = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read(); enc = open(uri).read().strip()
i = s.index("const VIC_CAMEO = 'data:image/svg+xml,' + \""); j = s.index('";\n', i)
s = s[:i] + "const VIC_CAMEO = 'data:image/svg+xml,' + \"" + enc + s[j:]
for a, b in [("(the fox's portrait, the front door)", "(the rabbit butler's portrait, the front door)"),
             ("the hall -- the fox's portrait, a pedimented front door", "the hall -- the rabbit butler's portrait, a pedimented front door"),
             ("and the fox butler's portrait (coral bow tie).", "and the butler's portrait: the rabbit again (Phase 433), centred, coral bow tie."),
             ("is the chair rail with the fox butler's portrait;", "is the chair rail with the rabbit butler's portrait;")]:
    if s.count(a) != 1: raise SystemExit('comment ' + a + ': %d' % s.count(a))
    s = s.replace(a, b)
open(src, 'w', encoding='utf-8').write(s); print('patch433 ok')
