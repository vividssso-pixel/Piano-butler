#!/usr/bin/env python3
# Phase 469: printables.html: the chapter 13 Workbook card shows the new book's page 4 (reading the tempo), with its words.
import sys
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
def rep(a, b):
    global s
    if s.count(a) != 1: raise SystemExit('found %d: %s' % (s.count(a), a[:80]))
    s = s.replace(a, b)
OLD = 'Tempo is how fast the beat goes. Italian words are the speed signs -- from a slow snail to a racing cheetah.'
NEW = 'Tempo is how fast the beat goes. Slow and fast; Adagio, Andante, Moderato and Allegro; reading the tempo word; the metronome; keeping a steady tempo.'
rep('alt="Workbook page from the Tempo Race chapter: The tempo race · Who goes at this speed? · Walk like the animals"', 'alt="Workbook page from the Tempo Race chapter: Find the tempo word · Which word fits? · Count in, then play"')
rep('<p>' + OLD + '</p>', '<p>' + NEW + '</p>')
rep('<p class="parts"><b>On this page:</b> The tempo race · Who goes at this speed? · Walk like the animals</p>', '<p class="parts"><b>On this page:</b> Find the tempo word · Which word fits? · Count in, then play</p>')
rep('"name": "Tempo Race worksheet", "description": "' + OLD + '"', '"name": "Tempo Race worksheet", "description": "' + NEW + '"')
open(p, 'w', encoding='utf-8').write(s); print('printables.html: the chapter 13 card')
