#!/usr/bin/env python3
# Phase 475: printables.html: the chapter 20 (Signs) Workbook card shows the rebuilt Workbook's page 4 (D.C. al Fine: write
# the order, write Fine, play it); its words and the JSON-LD follow the new chapter.
import sys
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    if s.count(a) != n: raise SystemExit('found %d (want %d): %s' % (s.count(a), n, a[:80]))
    s = s.replace(a, b)
WORDS = 'Signs show the road through the music: which bars to play again, where to go back to, where to stop, and which note to hold. Repeat signs, 1st and 2nd time bars, D.C. and D.S. al Fine, and the pause.'
rep('Signs are the music&#x27;s road signs: go round again, make a U-turn, take the exit, stop at the finish line -- or add a little sparkle.', WORDS)   # the card
rep("Signs are the music's road signs: go round again, make a U-turn, take the exit, stop at the finish line -- or add a little sparkle.", WORDS)       # the JSON-LD
rep('Follow the road map · Which way now? · Design a road map', 'Write the order · Write Fine · Play it', 2)   # the alt text and the parts line
if 'printables/img/wb-signs.jpg' not in s: raise SystemExit('card missing')
open(p, 'w', encoding='utf-8').write(s); print('printables.html: the chapter 20 card (page 4, its words and parts)')
