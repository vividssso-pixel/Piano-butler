#!/usr/bin/env python3
# Phase 431 on the site: the ledger-lines guide page's opener and Five Cs drawings (Clara's C from both staves; the fold),
# its words on the fold, and the worksheet/printables pictures of chapters 4 and 6 (question numbers in the boxes).
#   python3 site431.py <repo root> <this x dir>
import sys, os, shutil, glob
root, x = sys.argv[1], sys.argv[2]
def cp(a, b): shutil.copyfile(os.path.join(x, a), os.path.join(root, b)); print('copy', b)
for f in sorted(glob.glob(os.path.join(x, 'svg', 'ledger-lines', '*.svg'))): cp(os.path.relpath(f, x), 'tools/lessons/svg/ledger-lines/' + os.path.basename(f))
cp('img/ledger-lines-worksheet.jpg', 'lessons/img/ledger-lines-worksheet.jpg')
cp('img/wb-ledger-lines.jpg', 'printables/img/wb-ledger-lines.jpg')
cp('img/reading-the-staff-worksheet.jpg', 'lessons/img/reading-the-staff-worksheet.jpg')
cp('img/wb-staff.jpg', 'printables/img/wb-staff.jpg')
def edit(rel, pairs):
    p = os.path.join(root, rel); s = open(p, encoding='utf-8').read()
    for a, b in pairs:
        if s.count(a) != 1: raise SystemExit(rel + ': ' + a[:70] + ' found %d' % s.count(a))
        s = s.replace(a, b)
    open(p, 'w', encoding='utf-8').write(s); print('words', rel)
edit('tools/lessons/src/ledger-lines.html', [
    ('"updated": "2026-10-11"', '"updated": "2026-10-12"'),
    ('Updated 11 October 2026</p>', 'Updated 12 October 2026</p>'),
    ("and <b>Sky C</b> on two ladders over the treble staff. Every ledger note in this chapter",
     "and <b>Sky C</b> on two ladders over the treble staff. Fold the grand staff in half at middle C, as in the chapter before, and the Cs meet in pairs: Queensland C on Kingsland C &mdash; and now <b>Sky C on Sea C</b>, two ledger lines up, two ledger lines down. Every ledger note in this chapter"),
    ("play the five Cs from the sea to the sky, naming each one; then the C hop",
     "play the five Cs from the sea to the sky, naming each one; then the fold partners &mdash; Sea C with Sky C, Kingsland C with Queensland C, both thumbs on Clara's C; then the C hop"),
    ])
