#!/usr/bin/env python3
# Phase 470: printables.html: the chapter 14 Workbook card shows the new book's page 4 (the dotted crotchet), with its words.
import sys
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
def rep(a, b):
    global s
    if s.count(a) != 1: raise SystemExit('found %d: %s' % (s.count(a), a[:80]))
    s = s.replace(a, b)
OLD = 'One-bar rhythms in 4/4, easiest first. The beat is your heartbeat -- count it out loud under every note!'
NEW = 'Rhythm is the pattern of long and short sounds and silences. Grouping quavers, a quaver alone, the dotted crotchet, starting before beat 1, and count, clap, play.'
PARTS_OLD = 'Count the cards · Count them on your own · Rhythm bingo'
PARTS_NEW = 'Count the dotted crotchet · Which note fills the gap? · Count it, then play it'
rep('alt="Workbook page from the Rhythm Patterns chapter: ' + PARTS_OLD + '"', 'alt="Workbook page from the Rhythm Patterns chapter: ' + PARTS_NEW + '"')
rep('<p>' + OLD + '</p>', '<p>' + NEW + '</p>')
rep('<p class="parts"><b>On this page:</b> ' + PARTS_OLD + '</p>', '<p class="parts"><b>On this page:</b> ' + PARTS_NEW + '</p>')
rep('"name": "Rhythm Patterns worksheet", "description": "' + OLD + '"', '"name": "Rhythm Patterns worksheet", "description": "' + NEW + '"')
open(p, 'w', encoding='utf-8').write(s); print('printables.html: the chapter 14 card')
