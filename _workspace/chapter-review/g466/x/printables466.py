#!/usr/bin/env python3
# Phase 466: printables.html: the chapter 9 Workbook card shows the new book's page 4 (C position), with its words.
import sys
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
def rep(a, b):
    global s
    if s.count(a) != 1: raise SystemExit('found %d: %s' % (s.count(a), a[:80]))
    s = s.replace(a, b)
OLD = 'The staff is a staircase: does the next note step up a stair, skip one, or stand still?'
NEW = 'Read a tune by its moves: up, down or the same, a step or a skip. Then set each hand in C position and in G position, one finger for each note.'
rep('alt="Workbook page from the Steps &amp; Skips chapter: Step, skip or same? · Step, skip or same? On your own · What shape is this tune?"', 'alt="Workbook page from the Steps &amp; Skips chapter: Write the finger numbers · More finger numbers · Name it, then play it"')
rep('<p>' + OLD + '</p>', '<p>' + NEW + '</p>')
rep('<p class="parts"><b>On this page:</b> Step, skip or same? · Step, skip or same? On your own · What shape is this tune?</p>', '<p class="parts"><b>On this page:</b> Write the finger numbers · More finger numbers · Name it, then play it</p>')
rep('"description": "' + OLD + '"', '"description": "' + NEW + '"')
open(p, 'w', encoding='utf-8').write(s); print('printables.html: the chapter 9 card')
