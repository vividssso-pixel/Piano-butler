#!/usr/bin/env python3
# Phase 464 (b): printables.html's structured data says what the cards say: the two new names, the new words.
import sys, json, re
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
def rep(a, b):
    global s
    if s.count(a) != 1: raise SystemExit('found %d: %s' % (s.count(a), a[:70]))
    s = s.replace(a, b)
rep('"name": "Reading the Staff worksheet", "description": "The staff is a harbour map: the Queen\'s treble staff on the north shore, the King\'s bass staff on the south shore, and middle C is the bridge to the CBD."',
    '"name": "The Staff & the Two Clefs worksheet", "description": "The five lines, the treble clef and the bass clef: the Queen sings high, the King sings low. Lines and spaces first: skewers and sandwiches."')
rep('"name": "Famous Composers worksheet"', '"name": "Composers worksheet"')
rep('"name": "Time Signatures worksheet", "description": "A bar is a lunch box. The top number says how many pieces fit in it; the bottom number says what size each piece is."',
    '"name": "Time Signatures worksheet", "description": "Music is divided into bars, and the time signature at the start says how to count them. Feel the strong beat, fill a bar with notes and rests, and hold a tie across the bar line."')
m = re.search(r'<script type="application/ld\+json">(.*?)</script>', s, re.S); json.loads(m.group(1))
open(p, 'w', encoding='utf-8').write(s); print('printables.html: structured data matches the cards')
