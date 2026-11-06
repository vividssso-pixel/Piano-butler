#!/usr/bin/env python3
# Phase 402: 26 chapters -- the guide pages' "of 25" and the house page's counts, and the teacher dashboard's chapter links
#   python3 guide402.py <repo root>
import sys, os
root = sys.argv[1]
def edit(rel, pairs):
    p = os.path.join(root, rel); s = open(p, encoding='utf-8').read()
    for a, b, n in pairs:
        c = s.count(a)
        if c != n: raise SystemExit('%s: %r expected %d, got %d' % (rel, a, n, c))
        s = s.replace(a, b)
    open(p, 'w', encoding='utf-8').write(s); print('ok', rel)
edit('tools/lessons/src/posture-hands.html', [('Chapter 1 of 25', 'Chapter 1 of 26', 1)])
edit('tools/lessons/src/first-steps.html', [('Chapter 2 of 25', 'Chapter 2 of 26', 1)])
edit('tools/lessons/src/note-names.html', [('Chapter 3 of 25', 'Chapter 3 of 26', 1)])
edit('tools/lessons/src/index.html', [('"25 piano chapters for young beginners', '"26 piano chapters for young beginners', 1),
    ('<div class="kicker">25 chapters &middot; one room each</div>', '<div class="kicker">26 chapters &middot; one room each</div>', 1),
    ('<h2>All 25 chapters, on screen</h2>', '<h2>All 26 chapters, on screen</h2>', 1)])
edit('teacher-dashboard.html', [('  { id: "staff", label: "Reading the Staff" },\n', '  { id: "staff", label: "Reading the Staff" },\n  { id: "whole-staff", label: "The Whole Staff" },\n', 1)])
