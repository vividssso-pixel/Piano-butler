#!/usr/bin/env python3
# Phase 410: 'skewer', not 'kebab', on the chapter 4 guide page and its printables card
#   python3 guide410.py <repo root>
import sys, os
root = sys.argv[1]
def edit(rel, pairs):
    p = os.path.join(root, rel); s = open(p, encoding='utf-8').read()
    for a, b, n in pairs:
        c = s.count(a)
        if c != n: raise SystemExit('%s: %r expected %d, got %d' % (rel, a[:70], n, c))
        s = s.replace(a, b)
    open(p, 'w', encoding='utf-8').write(s); print('ok', rel)
edit('tools/lessons/src/staff.html', [
    ('the line runs straight through its middle, like a kebab &mdash;', 'the line runs straight through its middle, like a skewer &mdash;', 1),
    ('<p>Kebab or sandwich: write L or S for ten notes on two big staves, then cook your own -- three kebabs on the kebab plate, three sandwiches on the sandwich plate. One A4 page.</p>',
     '<p>Skewer or sandwich: write L or S for ten notes on two big staves, then cook -- skewers on lines 1, 3 and 5, sandwiches in spaces 1, 2 and 4. One A4 page.</p>', 1),
    ('then draw kebabs and sandwiches on two plates."', 'then draw skewers and sandwiches on two plates."', 1)])
edit('printables.html', [
    ('Lines and spaces first -- kebabs and sandwiches.</p>', 'Lines and spaces first -- skewers and sandwiches.</p>', 1),
    ('Line or space? · Your turn · Kebab plate, sandwich plate"', 'Line or space? · Your turn · Skewer plate, sandwich plate"', 1),
    ('<b>On this page:</b> Line or space? · Your turn · Kebab plate, sandwich plate</p>', '<b>On this page:</b> Line or space? · Your turn · Skewer plate, sandwich plate</p>', 1)])
