#!/usr/bin/env python3
# Phase 464: printables.html: every card's chapter number follows the map (PATH_STAGES order, as bkChapterNo);
# chapter 6 and 22 under their new names; the chapter 8 Workbook card for the new book.
import sys, re
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
ORDER = ['posture-hands', 'first-steps', 'pulse', 'note-names', 'note-values', 'staff',
         'whole-staff', 'time-signatures', 'reading-steps', 'dynamics', 'tones', 'pitch-range',
         'tempo', 'rhythm', 'ledger-lines', 'scales', 'piano-story',          # accidentals: off the map until it has a chapter
         'key-signatures', 'signs', 'intervals', 'chords', 'composers', 'melody',
         'form', 'terms', 'styles']
NO = {c: i + 1 for i, c in enumerate(ORDER)}
CUT = {'staff-mat': 'staff', 'cards-notes': 'staff', 'note-bars': 'note-values', 'cards-rhythm': 'note-values',
       'tempo-race': 'tempo', 'scale-slider': 'scales', 'fifths-wheel': 'key-signatures', 'chord-cake': 'chords',
       'chord-loop': 'chords', 'song-builder': 'form', 'cards-terms': 'terms', 'composer-cards': 'composers',
       'cards-elements': 'styles'}
NAME = {'staff': ('Reading the Staff', 'The Staff &amp; the Two Clefs'), 'composers': ('Famous Composers', 'Composers')}
def rep(a, b, n=1):
    global s
    if s.count(a) != n: raise SystemExit('found %d (want %d): %s' % (s.count(a), n, a[:80]))
    s = s.replace(a, b)
# 1. the two new names (cards, links' labels, picture descriptions)
for old, new in NAME.values():
    rep('the ' + old + ' sample page', 'the ' + new + ' sample page')
    rep('the ' + old + ' chapter', 'the ' + new + ' chapter')
    rep('<h3>' + old + '</h3>', '<h3>' + new + '</h3>')
    s = s.replace('· ' + old + '</div>', '· ' + new + '</div>')
# 2. the chapter 8 card: the new book's page 4 (pages=3: the Workbook's third sheet)
rep('<img src="printables/img/wb-time-signatures.jpg" width="440" height="622" loading="lazy" alt="Workbook page from the Time Signatures chapter: Read the two numbers · Which time signature fits? · Be the conductor">',
    '<img src="printables/img/wb-time-signatures.jpg" width="440" height="622" loading="lazy" alt="Workbook page from the Time Signatures chapter: Colour the strong beats · More strong beats · Count it, then play it">')
rep('<p>A bar is a lunch box. The top number says how many pieces fit in it; the bottom number says what size each piece is.</p>\n            <p class="parts"><b>On this page:</b> Read the two numbers · Which time signature fits? · Be the conductor</p>',
    '<p>Music is divided into bars, and the time signature at the start says how to count them. Feel the strong beat, fill a bar with notes and rests, and hold a tie across the bar line.</p>\n            <p class="parts"><b>On this page:</b> Colour the strong beats · More strong beats · Count it, then play it</p>')
# the staff card's words (no double dash; the clefs by their real names)
rep('<p>Meet the royal family of the keys: the King sings low, the Queen sings high, and Clara lives on middle C. Lines and spaces first -- skewers and sandwiches.</p>',
    '<p>The five lines, the treble clef and the bass clef: the Queen sings high, the King sings low. Lines and spaces first: skewers and sandwiches.</p>')
# 3. every card's number
seen = []
def card(m):
    kind, cid, body = m.group(1), m.group(2), m.group(3)
    ch = cid[3:] if kind == 'wb' else CUT.get(cid[4:])
    if ch is None: return m.group(0)                      # a card for every chapter
    if ch not in NO: raise SystemExit('no number for ' + cid)
    seen.append(cid)
    body2, n = re.subn(r'<div class="topic">Chapter \d+', '<div class="topic">Chapter %d' % NO[ch], body, count=1)
    if n != 1: raise SystemExit('no topic in ' + cid)
    return m.group(0).replace(body, body2)
s = re.sub(r'<article class="card (wb|cut)" id="([^"]+)">(.*?)</article>', card, s, flags=re.S)
if len(seen) != 38: raise SystemExit('cards numbered: %d' % len(seen))
if '--' in re.sub(r'<!--.*?-->|<style.*?</style>|<script.*?</script>', '', s, flags=re.S).split('<body', 1)[-1]:
    print('note: a double dash is still in the page text')
open(p, 'w', encoding='utf-8').write(s); print('printables.html: %d cards numbered by the map; chapters 6, 8, 22' % len(seen))
