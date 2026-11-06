#!/usr/bin/env python3
# Phase 472: teacher-dashboard.html: chapter 17, Accidentals, in the 'For the student' chapter list, after Scales.
import sys
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
a = '  { id: "scales", label: "Scales" },\n'
if s.count(a) != 1: raise SystemExit('found %d: %s' % (s.count(a), a))
s = s.replace(a, a + '  { id: "accidentals", label: "Accidentals" },\n')
open(p, 'w', encoding='utf-8').write(s); print('teacher-dashboard.html: accidentals added')
