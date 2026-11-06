#!/usr/bin/env python3
# Phase 460: the printables card for chapter 5 shows the new Workbook's page 4.
import sys
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
def rep(a, b):
    global s
    if s.count(a) != 1: raise SystemExit('printables: found %d: %s' % (s.count(a), a[:60]))
    s = s.replace(a, b)
rep('alt="Workbook page from the Notes &amp; Rests chapter: Name it, count it · Name and count on your own · Cut the cake">',
    'alt="Workbook page from the Notes &amp; Rests chapter: How many beats? · Draw the sound lines · Count it, then play it">')
rep("""            <div class="topic">Chapter 9</div>
            <h3>Notes &amp; Rests</h3>
            <p>A semibreve is a whole cake: 4 beats. Cut it in half for minims, in quarters for crotchets, in eighths for quavers -- and every note has a rest the same size.</p>
            <p class="parts"><b>On this page:</b> Name it, count it · Name and count on your own · Cut the cake</p>""",
    """            <div class="topic">Chapter 5</div>
            <h3>Notes &amp; Rests</h3>
            <p>Every note lasts a number of beats, and its shape tells you how many: a crotchet 1, a minim 2, a dotted minim 3, a semibreve 4. A rest is a silence you count.</p>
            <p class="parts"><b>On this page:</b> How many beats? · Draw the sound lines · Count it, then play it</p>""")
open(p, 'w', encoding='utf-8').write(s); print('printables.html: chapter 5 card')
