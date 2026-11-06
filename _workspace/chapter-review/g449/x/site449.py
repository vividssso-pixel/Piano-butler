#!/usr/bin/env python3
# Phase 449 on the site: the ledger-lines guide page names its five Cs low C, bass C, middle C, treble C, high C, and its
# three drawings with C labels are re-exported from the book.
#   python3 site449.py <repo root> <this x dir>
import sys, os, shutil, glob
root, x = sys.argv[1], sys.argv[2]
p = os.path.join(root, 'tools/lessons/src/ledger-lines.html'); s = open(p, encoding='utf-8').read()
def rep(a, b):
    global s
    if s.count(a) != 1: raise SystemExit('ledger-lines.html: found %d: %s' % (s.count(a), a[:70]))
    s = s.replace(a, b)
rep("ladder 2 carries <b>C</b> &mdash; <b>Sky C</b>.", "ladder 2 carries <b>C</b> &mdash; <b>high C</b>.")
rep("ladder 2 carries <b>C</b> &mdash; <b>Sea C</b>.", "ladder 2 carries <b>C</b> &mdash; <b>low C</b>.")
rep("<b>Sea C</b> on two ladders under the bass staff, <b>Kingsland C</b> in the bass staff's second space, <b>Clara's C</b> (middle C) on its ladder, <b>Queensland C</b> in the treble staff's third space, and <b>Sky C</b> on two ladders over the treble staff.",
    "<b>low C</b> on two ladders under the bass staff, <b>bass C</b> in the bass staff's second space, <b>middle C</b> on its ladder, <b>treble C</b> in the treble staff's third space, and <b>high C</b> on two ladders over the treble staff.")
rep("the Cs meet in pairs: Queensland C on Kingsland C &mdash; and now <b>Sky C on Sea C</b>,", "the Cs meet in pairs: treble C on bass C &mdash; and now <b>high C on low C</b>,")
rep("a step or a skip from Sea C, Clara's C or Sky C.</p>", "a step or a skip from low C, middle C or high C.</p>")
rep("Sea C with Sky C, Kingsland C with Queensland C, both thumbs on Clara's C;", "low C with high C, bass C with treble C, both thumbs on middle C;")
rep("a step or a skip from Sky C and Sea C,", "a step or a skip from high C and low C,")
rep("such as the C two ledger lines above the treble staff and the C two ledger lines below the bass staff,", "such as high C, two ledger lines above the treble staff, and low C, two ledger lines below the bass staff,")
for w in ['Sea C', 'Sky C', 'Kingsland C', 'Queensland C', "Clara's C"]:
    if w in s: raise SystemExit('left: ' + w)
open(p, 'w', encoding='utf-8').write(s); print('tools/lessons/src/ledger-lines.html: the five Cs renamed')
for f in sorted(glob.glob(os.path.join(x, 'svg', '*', '*.svg'))):
    rel = os.path.relpath(f, os.path.join(x, 'svg')); shutil.copyfile(f, os.path.join(root, 'tools/lessons/svg', rel)); print('copy tools/lessons/svg/' + rel)
