#!/usr/bin/env python3
# Phase 467: printables.html: the chapter 10 Workbook card shows the new book's page 4 (hairpins), with its words.
import sys
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
def rep(a, b):
    global s
    if s.count(a) != 1: raise SystemExit('found %d: %s' % (s.count(a), a[:80]))
    s = s.replace(a, b)
OLD = 'Dynamics are the volume knob: how loud or soft. Articulation is how each note is played -- bouncy, smooth, poked or leaned on.'
NEW = 'How loud or soft to play, from pp to f, and the hairpins for getting louder and softer. Then legato and staccato, and the slur beside the tie.'
rep('alt="Workbook page from the Dynamics &amp; Articulation chapter: Soft to loud · What does it mean? · A story in dynamics"', 'alt="Workbook page from the Dynamics &amp; Articulation chapter: Louder or softer? · Draw the hairpin · Mark it, then play it"')
rep('<p>' + OLD + '</p>', '<p>' + NEW + '</p>')
rep('<p class="parts"><b>On this page:</b> Soft to loud · What does it mean? · A story in dynamics</p>', '<p class="parts"><b>On this page:</b> Louder or softer? · Draw the hairpin · Mark it, then play it</p>')
rep('"description": "' + OLD + '"', '"description": "' + NEW + '"')
open(p, 'w', encoding='utf-8').write(s); print('printables.html: the chapter 10 card')
