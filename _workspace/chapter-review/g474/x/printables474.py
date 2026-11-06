#!/usr/bin/env python3
# Phase 474: printables.html: the chapter 19 (Key Signatures) Workbook card shows the rebuilt Workbook's page 4 (F major:
# draw the key signature, find the key, play it); its words and the JSON-LD follow the new chapter.
import sys
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    if s.count(a) != n: raise SystemExit('found %d (want %d): %s' % (s.count(a), n, a[:80]))
    s = s.replace(a, b)
OLD_WORDS = 'Sharps and flats always join in the same order, like a line-up that never changes. Learn the line and every key falls out of it.'
WORDS = 'A key signature is the sharps or flats written just after the clef at the start of every line of music. It changes those notes for the whole piece. C, G, F, D and B♭ major, and the key signature beside an accidental.'
OLD_PARTS = 'Finish the order · Which sharps or flats? · My own silly sentence'
PARTS = 'Draw the key signature · Find the key · Play it'
rep(OLD_WORDS, WORDS, 2)    # the card and the JSON-LD
rep(OLD_PARTS, PARTS, 2)    # the alt text and the parts line
if 'printables/img/wb-key-signatures.jpg' not in s: raise SystemExit('card missing')
open(p, 'w', encoding='utf-8').write(s); print('printables.html: the chapter 19 card (page 4, its words and parts)')
