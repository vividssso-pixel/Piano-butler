#!/usr/bin/env python3
# Phase 472: printables.html: chapter 17, Accidentals, joins the map, so every card from The Piano's Story on moves up one
# (the numbers follow PATH_STAGES, as bkChapterNo; Phase 464's way); the chapter 17 Workbook card (its page 4); 26 pages.
import sys, re
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
ORDER = ['posture-hands', 'first-steps', 'pulse', 'note-names', 'note-values', 'staff',
         'whole-staff', 'time-signatures', 'reading-steps', 'dynamics', 'tones', 'pitch-range',
         'tempo', 'rhythm', 'ledger-lines', 'scales', 'accidentals', 'piano-story',
         'key-signatures', 'signs', 'intervals', 'chords', 'composers', 'melody',
         'form', 'terms', 'styles']
NO = {c: i + 1 for i, c in enumerate(ORDER)}
CUT = {'staff-mat': 'staff', 'cards-notes': 'staff', 'note-bars': 'note-values', 'cards-rhythm': 'note-values',
       'tempo-race': 'tempo', 'scale-slider': 'scales', 'fifths-wheel': 'key-signatures', 'chord-cake': 'chords',
       'chord-loop': 'chords', 'song-builder': 'form', 'cards-terms': 'terms', 'composer-cards': 'composers',
       'cards-elements': 'styles'}
def rep(a, b, n=1):
    global s
    if s.count(a) != n: raise SystemExit('found %d (want %d): %s' % (s.count(a), n, a[:80]))
    s = s.replace(a, b)
# 1. the chapter 17 Workbook card, after Scales
WORDS = 'An accidental is a sharp, flat or natural written just before a note. It lasts until the bar line, for its own line or space only.'
PARTS = 'Circle the changed notes · Write the names · Play it'
URL = 'drills.html?book=work&ch=accidentals&lang=en&pages=3'
CARD = '''        <article class="card wb" id="wb-accidentals">
          <a class="sheet" href="%s" target="_blank" rel="noopener" aria-label="Open the Accidentals sample page to print">
            <img src="printables/img/wb-accidentals.jpg" width="440" height="622" loading="lazy" alt="Workbook page from the Accidentals chapter: %s">
          </a>
          <div class="txt">
            <div class="topic">Chapter 17</div>
            <h3>Accidentals</h3>
            <p>%s</p>
            <p class="parts"><b>On this page:</b> %s</p>
            <div class="foot"><span class="meta">1 A4 page</span><a class="btn" href="%s" target="_blank" rel="noopener">Print this page</a></div>
          </div>
        </article>
''' % (URL, PARTS, WORDS, PARTS, URL)
rep('        <article class="card wb" id="wb-key-signatures">', CARD + '        <article class="card wb" id="wb-key-signatures">')
LD_AFTER = '"image": "https://thepianobutler.com/printables/img/wb-scales.jpg", "url": "https://thepianobutler.com/drills.html?book=work&ch=scales&lang=en&pages=3", "learningResourceType": "Worksheet", "isAccessibleForFree": true}'
rep(LD_AFTER, LD_AFTER + ', {"@type": "CreativeWork", "name": "Accidentals worksheet", "description": "' + WORDS + '", "image": "https://thepianobutler.com/printables/img/wb-accidentals.jpg", "url": "https://thepianobutler.com/' + URL + '", "learningResourceType": "Worksheet", "isAccessibleForFree": true}')
# 2. 26 worksheet pages
rep('board games and 25 worksheet pages.', 'board games and 26 worksheet pages.', 4)
rep('<a href="#worksheets">Worksheet pages (25)</a>', '<a href="#worksheets">Worksheet pages (26)</a>')
rep('one free page from each of the 25 workbook chapters', 'one free page from each of the 26 workbook chapters')
# 3. every card's number
seen = []
def card(m):
    kind, cid, body = m.group(1), m.group(2), m.group(3)
    ch = cid[3:] if kind == 'wb' else CUT.get(cid[4:])
    if ch is None: return m.group(0)
    if ch not in NO: raise SystemExit('no number for ' + cid)
    seen.append(cid)
    body2, n = re.subn(r'<div class="topic">Chapter \d+', '<div class="topic">Chapter %d' % NO[ch], body, count=1)
    if n != 1: raise SystemExit('no topic in ' + cid)
    return m.group(0).replace(body, body2)
s = re.sub(r'<article class="card (wb|cut)" id="([^"]+)">(.*?)</article>', card, s, flags=re.S)
if len(seen) != 39: raise SystemExit('cards numbered: %d' % len(seen))
open(p, 'w', encoding='utf-8').write(s); print('printables.html: %d cards numbered by the map; the chapter 17 card; 26 pages' % len(seen))
