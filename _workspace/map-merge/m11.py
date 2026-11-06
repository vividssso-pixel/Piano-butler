# The Map: the "My week" pawn board is gone from the House page (her 'this is not needed any more', 1 Nov):
# practice days live on the student's Today page and on the teacher's dashboard.
import sys
p = sys.argv[1]; h = open(p, encoding='utf-8').read()
o = "  const week = useMemo(() => compact ? null : weekSvg({ days: practiceDays(), today, name }), [sig]);"
if h.count(o) != 1: raise SystemExit('anchor')
h = h.replace(o, "  const week = null;   // m11: the pawn board left the Map (weekSvg kept for later use)")
open(p, 'w', encoding='utf-8').write(h); print('m11 ok')
