#!/usr/bin/env python3
# Phase 464: teacher-dashboard.html: the two renamed chapters in the 'For the student' chapter list.
import sys
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
for a, b in [('{ id: "staff", label: "Reading the Staff" },', '{ id: "staff", label: "The Staff & the Two Clefs" },'),
             ('{ id: "composers", label: "Famous Composers" },', '{ id: "composers", label: "Composers" },')]:
    if s.count(a) != 1: raise SystemExit('found %d: %s' % (s.count(a), a))
    s = s.replace(a, b)
open(p, 'w', encoding='utf-8').write(s); print('teacher-dashboard.html: chapters 6 and 22 renamed')
