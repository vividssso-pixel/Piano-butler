#!/usr/bin/env python3
# Phase 471: printables.html: the chapter 16 Workbook card shows the new book's page 4 (scale degrees), with its words.
import sys
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
def rep(a, b):
    global s
    if s.count(a) != 1: raise SystemExit('found %d: %s' % (s.count(a), a[:80]))
    s = s.replace(a, b)
OLD = 'A scale is a staircase. A big step (tone) skips a key, a tiny step (semitone) is the very next key. The same staircase -- T T S T T T S -- builds every major scale.'
NEW = 'A scale is notes in order, step by step, from one note to the same letter an octave away. The major scale’s steps, C major fingering, scale degrees, and G and F major.'
PARTS_OLD = 'Fingering for C major · G and F major · Find the wrong finger'
PARTS_NEW = 'Number the keys · Which degree? · Play the numbers'
rep('alt="Workbook page from the Scales chapter: ' + PARTS_OLD + '"', 'alt="Workbook page from the Scales chapter: ' + PARTS_NEW + '"')
rep('<p>' + OLD + '</p>', '<p>' + NEW + '</p>')
rep('<p class="parts"><b>On this page:</b> ' + PARTS_OLD + '</p>', '<p class="parts"><b>On this page:</b> ' + PARTS_NEW + '</p>')
rep('"name": "Scales worksheet", "description": "' + OLD + '"', '"name": "Scales worksheet", "description": "' + NEW + '"')
open(p, 'w', encoding='utf-8').write(s); print('printables.html: the chapter 16 card')
