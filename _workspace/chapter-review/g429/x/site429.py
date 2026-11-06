#!/usr/bin/env python3
# Phase 429 on the site: 'ladder', not 'rung', on the chapter 4 and 6 guide pages; the ledger-lines page's drawings, worksheet
# picture (dotted guide lines, the lid) and printables picture redone.   python3 site429.py <repo root> <this x dir>
import sys, os, shutil, glob
root, x = sys.argv[1], sys.argv[2]
def cp(a, b): shutil.copyfile(os.path.join(x, a), os.path.join(root, b)); print('copy', b)
for f in sorted(glob.glob(os.path.join(x, 'svg', 'ledger-lines', '*.svg'))): cp(os.path.relpath(f, x), 'tools/lessons/svg/ledger-lines/' + os.path.basename(f))
cp('img/ledger-lines-worksheet.jpg', 'lessons/img/ledger-lines-worksheet.jpg')
cp('img/wb-ledger-lines.jpg', 'printables/img/wb-ledger-lines.jpg')
def edit(rel, pairs):
    p = os.path.join(root, rel); s = open(p, encoding='utf-8').read()
    for a, b in pairs:
        if s.count(a) != 1: raise SystemExit(rel + ': ' + a[:70] + ' found %d' % s.count(a))
        s = s.replace(a, b)
    open(p, 'w', encoding='utf-8').write(s); print('words', rel)
edit('tools/lessons/src/staff.html', [("Clara's middle C is written on a little ladder rung of its own", "Clara's middle C is written on a little ladder of its own")])
edit('tools/lessons/src/ledger-lines.html', [
    ('ledger lines &mdash; are the rungs of a ladder that lets them climb out', 'ledger lines &mdash; are little ladders that let them climb out'),
    ('counting the rungs wrong, reading a note', 'counting the ledger lines wrong, reading a note'),
    ('first count out from the staff &mdash; line, space, rung &mdash; and then', 'first count out from the staff &mdash; line, space, ladder &mdash; and then'),
    ('<section id="rung">\n  <h2>A rung for one note</h2>', '<section id="ladder">\n  <h2>A little ladder for one note</h2>'),
    ("in this book it is Princess Clara's rung.", "in this book it is Princess Clara's ladder."),
    ('with <b>no gaps</b> back to the staff &mdash; and never one more than the note needs.</p>', 'with <b>no gaps</b> back to the staff &mdash; and never one more than the note needs: a note in a space gets <b>no lid</b> on top.</p>'),
    ('Then rung 1 carries <b>A</b>, the next space <b>B</b>, and rung 2 carries', 'Then ladder 1 carries <b>A</b>, the next space <b>B</b>, and ladder 2 carries'),
    ('up to rung 3: <b>E</b>.', 'up to ladder 3: <b>E</b>.'),
    ('rung 1 carries <b>E</b>, the next space <b>D</b>, and rung 2 carries', 'ladder 1 carries <b>E</b>, the next space <b>D</b>, and ladder 2 carries'),
    ('down to rung 3: <b>A</b>.', 'down to ladder 3: <b>A</b>.'),
    ('The rungs between the two staves are borrowed. The A on rung 2 under the treble staff', 'The ladders between the two staves are borrowed. The A on ladder 2 under the treble staff'),
    ('the E on rung 2 over the bass staff', 'the E on ladder 2 over the bass staff'),
    ('Middle C sits on one rung, seen from either staff.', 'Middle C sits on one ladder, seen from either staff.'),
    ('<b>Sea C</b> on two rungs under the bass staff', '<b>Sea C</b> on two ladders under the bass staff'),
    ('<b>Clara\'s C</b> (middle C) on its rung,', '<b>Clara\'s C</b> (middle C) on its ladder,'),
    ('<b>Sky C</b> on two rungs over the treble staff', '<b>Sky C</b> on two ladders over the treble staff'),
    ('<div><h3>The rungs</h3><ul>', '<div><h3>The ladders</h3><ul>'),
    ('<li>I can read the rungs between the staves, both ways</li>', '<li>I can read the ladders between the staves, both ways</li>'),
    ('<h3>Draw the rungs</h3>', '<h3>Draw the ladders</h3>'),
    ('then draw the ledger lines seven notes need (some need none), and write how many lines each of seven notes on a big staff needs', 'then draw the ledger lines seven notes need on dotted guide lines (some need none), and count how many each of seven notes on a big staff needs'),
    ('alt="Worksheet page: circle a tick or a cross for neat and untidy ledger lines, draw the ledger lines seven notes need, and write how many each note needs."', 'alt="Worksheet page: circle a tick or a cross for neat and untidy ledger lines, draw the ledger lines seven notes need on dotted guide lines, and count how many each note needs."'),
    ('Draw only as many as the note needs: a note just above or below the staff needs none.</p>', 'Draw only as many as the note needs: a note just above or below the staff needs none, and a note in a space gets no extra line on top, like a lid.</p>'),
    ])
