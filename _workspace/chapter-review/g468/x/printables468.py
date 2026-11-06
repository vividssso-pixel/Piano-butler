#!/usr/bin/env python3
# Phase 468: printables.html: the chapter 12 Workbook card shows the new book's page 4 (the instrument families), with its words.
import sys
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
def rep(a, b):
    global s
    if s.count(a) != 1: raise SystemExit('found %d: %s' % (s.count(a), a[:80]))
    s = s.replace(a, b)
OLD = 'What makes a note high or low? Count vibrations, shorten strings, line up the violin family, climb the octave ladder, and find out where the piano sits among the instruments and voices.'
NEW = 'Low, middle and high on the keys and the staff, and why big sounds low. Then the four instrument families, the violin family from low to high, and the piano’s 88-key range.'
rep('alt="Workbook page from the Pitch, Hz &amp; Range chapter: Count the waves · Which string is higher? · Make a rubber-band guitar"', 'alt="Workbook page from the Pitch, Hz &amp; Range chapter: Which family? · How does it make its sound? · Play like them"')
rep('<p>' + OLD + '</p>', '<p>' + NEW + '</p>')
rep('<p class="parts"><b>On this page:</b> Count the waves · Which string is higher? · Make a rubber-band guitar</p>', '<p class="parts"><b>On this page:</b> Which family? · How does it make its sound? · Play like them</p>')
rep('"description": "' + OLD + '"', '"description": "' + NEW + '"')
open(p, 'w', encoding='utf-8').write(s); print('printables.html: the chapter 12 card')
