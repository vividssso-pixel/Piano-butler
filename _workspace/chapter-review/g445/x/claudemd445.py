#!/usr/bin/env python3
# Phase 445: CLAUDE.md -- the log row.
import sys, re
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
ROW = """| 445 | 2026-10-12 | **Chapter 11's guide page; one colon a sentence; the guides' previous/next in path order.** (1) lessons/tones-and-semitones.html (--final, no dashes at all): 'From the teacher' = her G1 (14:52: E F and B C are half steps all by themselves, shown first, then the idea) and G2 (who is your nearest neighbour? the very next key); no parents' tip (her G3: nothing for parents); sections half step, whole step, the white half steps (W W H W W W H = the major scale's recipe), sharp and flat with the hidden attic and 'a sharp or a flat is not always a black key', sharps and flats on the staff, my five checks, the worksheet (Workbook page 3: H or W from C and from A, circle every E F and B C; lessons/img/tones-worksheet.jpg), the drill, five questions; drawings = the book's own (guide445svg.js, svg/tones/). Room 11 lit on the guides' front page (house redrawn with the rooms counted from the bottom, sharing picture, 'Open rooms' card), sitemap, the printables card (page 3, the new words, Chapter 11). Every guide's previous/next now follows the path's numbers (first-steps -> 3 Pulse & Counting; note-names 3 / 5 Notes & Rests; staff 5 / 7 The Whole Staff; ledger-lines 14 Rhythm Patterns / 16 Scales; tones 10 / 12). (2) patch444c.py: sentences the dash rewrite left with two colons in the finished books read again with one (C hop, Landmark hop, the check-up line, the hand staff, chapter 11's pages 2 and 3, en and ko). Open: the older guide pages still use em dashes (asked). |
"""
m = re.search(r'^\| 444 \| [^\n]*\n', s, re.M)
if not m: raise SystemExit('row 444')
s = s[:m.end()] + ROW + s[m.end():]
open(p, 'w', encoding='utf-8').write(s); print('CLAUDE.md: log row 445')
