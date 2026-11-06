#!/usr/bin/env python3
# Phase 473: printables.html: the chapter 18 (The Piano's Story) Workbook card shows the rebuilt Workbook's page 4
# (inside the piano: name the parts, in order, hold and let go); its words and the JSON-LD follow the new chapter.
import sys
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    if s.count(a) != n: raise SystemExit('found %d (want %d): %s' % (s.count(a), n, a[:80]))
    s = s.replace(a, b)
OLD_WORDS = 'Before the piano there were the clavichord and the harpsichord. Meet the man who invented the piano, look inside it, and find out how each era’s keyboard shaped the way its music is played.'
WORDS = 'The piano is a keyboard instrument whose hammers strike its strings. The harpsichord and the clavichord, Cristofori’s first piano, the key, hammer, string and damper, the pedals, and grand and upright.'
OLD_PARTS = 'Pluck, press or strike? · Which keyboard? · Draw the touch'
PARTS = 'Name the parts · In order · Slowly, then hold and let go'
# the card (2 times the words: the card and the JSON-LD; 2 times the parts: the alt text and the parts line)
rep(OLD_WORDS, WORDS, 2)
rep(OLD_PARTS, PARTS, 2)
rep('aria-label="Open the The Piano’s Story sample page to print"', 'aria-label="Open The Piano’s Story sample page to print"')
rep('alt="Workbook page from the The Piano’s Story chapter: ', 'alt="Workbook page from The Piano’s Story chapter: ')
# the same slip on the chapter 6 card ("the The Staff")
rep('aria-label="Open the The Staff &amp; the Two Clefs sample page to print"', 'aria-label="Open The Staff &amp; the Two Clefs sample page to print"')
rep('alt="Workbook page from the The Staff &amp; the Two Clefs chapter: ', 'alt="Workbook page from The Staff &amp; the Two Clefs chapter: ')
if '<article class="card wb" id="wb-piano-story">' not in s or 'printables/img/wb-piano-story.jpg' not in s: raise SystemExit('card missing')
open(p, 'w', encoding='utf-8').write(s); print('printables.html: the chapter 18 card (page 4, its words and parts); no "the The" in alt texts')
