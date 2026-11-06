#!/usr/bin/env python3
# Phase 409: the Workbook lost its copy of the opener, so "Print this page" links shift one page back;
# chapter 4's sample worksheet is the new big-staff page 1; printables.html's chapter numbers follow the
# 26-chapter order (Phase 402 had missed them).
#   python3 guide409.py <repo root>
import sys, os, re
root = sys.argv[1]
def edit(rel, pairs):
    p = os.path.join(root, rel); s = open(p, encoding='utf-8').read()
    for a, b, n in pairs:
        c = s.count(a)
        if c != n: raise SystemExit('%s: %r expected %d, got %d' % (rel, a[:70], n, c))
        s = s.replace(a, b)
    open(p, 'w', encoding='utf-8').write(s); print('ok', rel)
    return s

edit('tools/lessons/src/posture-hands.html', [('ch=posture-hands&amp;lang=en&amp;pages=2', 'ch=posture-hands&amp;lang=en&amp;pages=1', 2)])
edit('tools/lessons/src/first-steps.html', [('ch=first-steps&amp;lang=en&amp;pages=3', 'ch=first-steps&amp;lang=en&amp;pages=2', 2)])
edit('tools/lessons/src/note-names.html', [('ch=note-names&amp;lang=en&amp;pages=5', 'ch=note-names&amp;lang=en&amp;pages=4', 2)])
edit('tools/lessons/src/staff.html', [
    ('ch=staff&amp;lang=en&amp;pages=2', 'ch=staff&amp;lang=en&amp;pages=1', 2),
    ('<p>Kebab or sandwich: write L or S for ten notes, then sort six more onto the kebab plate and the sandwich plate. One A4 page.</p>',
     '<p>Kebab or sandwich: write L or S for ten notes on two big staves, then cook your own -- three kebabs on the kebab plate, three sandwiches on the sandwich plate. One A4 page.</p>', 1),
    ('alt="Worksheet page: write L or S for line and space notes, then sort six notes onto the kebab plate and the sandwich plate."',
     'alt="Worksheet page: write L or S under line and space notes on two big staves, then draw kebabs and sandwiches on two plates."', 1)])

# printables.html: chapters 1-3 one page back; chapter 4 = the new page 1; chapter numbers in map order
order = ["posture-hands", "first-steps", "note-names", "staff", "whole-staff", "ledger-lines", "tones", "pulse", "note-values", "time-signatures", "rhythm", "reading-steps", "tempo", "intervals", "scales", "key-signatures", "chords", "melody", "form", "dynamics", "signs", "terms", "piano-story", "composers", "pitch-range", "styles"]
p = os.path.join(root, 'printables.html'); s = open(p, encoding='utf-8').read()
for ch in ['posture-hands', 'first-steps', 'note-names']:
    a = 'book=work&ch=%s&lang=en&pages=3' % ch
    n = s.count(a)
    if n < 2: raise SystemExit('printables %s links: %d' % (ch, n))
    s = s.replace(a, 'book=work&ch=%s&lang=en&pages=2' % ch)
a = 'book=work&ch=staff&lang=en&pages=3'
if s.count(a) < 2: raise SystemExit('printables staff links')
s = s.replace(a, 'book=work&ch=staff&lang=en&pages=1')
pairs = [
    ('alt="Workbook page from the Reading the Staff chapter: Line or space? · Line or space? On your own · Draw a note face"',
     'alt="Workbook page from the Reading the Staff chapter: Line or space? · Your turn · Kebab plate, sandwich plate"'),
    ("<p>The staff is a harbour map: the Queen&#x27;s treble staff on the north shore, the King&#x27;s bass staff on the south shore, and middle C is the bridge to the CBD.</p>",
     "<p>Meet the royal family of the keys: the King sings low, the Queen sings high, and Princess Clara lives on middle C. Lines and spaces first -- kebabs and sandwiches.</p>"),
    ('<p class="parts"><b>On this page:</b> Line or space? · Line or space? On your own · Draw a note face</p>',
     '<p class="parts"><b>On this page:</b> Line or space? · Your turn · Kebab plate, sandwich plate</p>'),
]
for a, b in pairs:
    if s.count(a) != 1: raise SystemExit('printables staff text: %r' % a[:60])
    s = s.replace(a, b)
# each workbook card's "Chapter N" follows the map (26 chapters since Phase 402)
def fix(m):
    cid = m.group(1); body = m.group(2)
    if cid not in order: return m.group(0)
    return '<article class="card wb" id="wb-%s">%s' % (cid, re.sub(r'<div class="topic">Chapter \d+</div>', '<div class="topic">Chapter %d</div>' % (order.index(cid) + 1), body, count=1))
s, nfix = re.subn(r'<article class="card wb" id="wb-([a-z-]+)">(.*?)</article>', lambda m: fix(m) + '</article>', s, flags=re.S)
open(p, 'w', encoding='utf-8').write(s); print('ok printables.html, cards', nfix)
