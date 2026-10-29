#!/usr/bin/env python3
"""Build CV: the dashboard names a floor by its grade only (Sohyun 2026-10-29 14:24)."""
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def R(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (c, n, old[:100]); s = s.replace(old, new)
R('''const dhFloorName = (k) => { const f = DRILLS_HOUSE.floors[k]; return f ? "Floor " + (k + 1) + " · " + f.name : "—"; };''',
  '''const dhFloorName = (k) => { const f = DRILLS_HOUSE.floors[k]; return f ? f.name : "—"; };   // Build CV: the grade only''')
R(''': "Floor 1 · Beginner"}''', ''': "Beginner"}''')
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
