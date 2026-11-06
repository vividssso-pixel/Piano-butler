#!/usr/bin/env python3
# Phase 465: her 2026-10-14 06:42 '응 스케일 너 추천대로가자': a 'more-scales' room on Level 5, after Styles
# (off the map until its chapter exists, like accidentals); Korean bar line is 세로줄 everywhere (10 left as 마디줄).
import sys
src, out = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    if s.count(a) != n: raise SystemExit('found %d (want %d): %s' % (s.count(a), n, a[:70]))
    s = s.replace(a, b)
rep("  { ids: ['form', 'terms', 'styles'], en: ['Level 5',",
    "  { ids: ['form', 'terms', 'styles', 'more-scales'], en: ['Level 5',")
rep("// a room waits off the map until its chapter exists (accidentals)",
    "// a room waits off the map until its chapter exists (accidentals; more-scales: pentatonic, blues, whole-tone, the modes)")
rep('마디줄', '세로줄', 10)
open(out, 'w', encoding='utf-8').write(s); print('ok')
