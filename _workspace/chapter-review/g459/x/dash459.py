#!/usr/bin/env python3
# Phase 459: the teacher dashboard's chapter list uses chapter 7's new name.
import sys
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
a = '{ id: "whole-staff", label: "The Whole Staff" }'
if s.count(a) != 1: raise SystemExit('teacher-dashboard: found %d' % s.count(a))
s = s.replace(a, '{ id: "whole-staff", label: "Line and Space Names" }')
open(p, 'w', encoding='utf-8').write(s); print('teacher-dashboard.html: chapter 7 renamed')
