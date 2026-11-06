#!/usr/bin/env python3
# Phase 446: CLAUDE.md -- rule 9 brought up to date (Phases 442-443), and the log row.
import sys, re
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
def rep(a, b):
    global s
    if s.count(a) != 1: raise SystemExit('found %d: %s' % (s.count(a), a[:80]))
    s = s.replace(a, b)
rep("for the rest of the session the house shows straight away.", "inside one page load the house then shows straight away, and every page load opens on the hall again (Phase 442); a floor's rooms are counted from the bottom left (1 2 3 below, 4 5 6 above, Phase 442).")
rep("five practice days take the pawn (Clara, or the linked student's own) across the board", "five practice days take the pawn (the linked student's own; 'My week' without a name, Phase 443) across the board")
ROW = """| 446 | 2026-10-12 | **Chapter 3 (Pulse & Counting) started: Lesson Book draft v1 + review pack.** After her 15:54 '다음으로 넘어가자' and 16:17 '이거 하고 다음순서', the next book in path order (C9). Built on her own words ('Music has a heartbeat: the pulse. It keeps going, steady, even when the notes stop.'), the level plan's scope for room 3 (a steady beat, counting out loud, the beat and the rhythm are not the same; strong and weak beats wait for room 8, note values for room 5) and the cast of chapters 1-2; no letter names (chapter 4 comes after). 7 pages (pl446book.jsx, draft only, drills.src.html unchanged): 1 the heart and two rows of steady beat circles, 'the same gap every time' · 2 A steady beat: footprints walking right, steady (a tick) and not steady (a cross), the sister walking · 3 Count out loud: the brother says 1, 2, 3, 4!, a counting ring with 4 back to 1 · 4 When the notes stop: play on 1 and 2, count only on 3 and 4 (dashed circles), the hearts go on · 5 Beat or rhythm?: bird (one sound) and tur-tle (two) over four beats, light-house too (새, 거-북, 등-대) · 6 The pulse in your fingers: a new finger on each beat on the 4th small house, the big house next to it, the 3rd small house for the left hand; finger numbers in coral circles (LbTune gets an optional coral look), the count in plain numbers · 7 My five checks. A fresh reviewer's fixes are in (no quaver by the bird; set hand, finger and house in every task; feet that walk; 'lift your hand', 'just above the key'; the 1 navy, not a strong beat; Korean wording). Review pack Claude outputs/Chapter-03-Pulse-review-v1.pdf (11 pages): G1-G3 for the guide page, A1-A6 (today: six tool steps, strong/weak beats, note values, bars, 'Hot Cross Buns', a drill that tests note values and bars, a pre-rules Workbook), B1-B11 with recommendations (B3 no 'slower', B4 strong/weak to room 8, B5 only 1 2 3 4, B6 silent beats before rests, B7 the cast's words, B9 a 5-level drill, B10 Workbook W1-W5, B11 on screen). Checks: lbcheck pulse 0/0 en and ko. |
"""
m = re.search(r'^\| 445 \| [^\n]*\n', s, re.M)
if not m: raise SystemExit('row 445')
s = s[:m.end()] + ROW + s[m.end():]
open(p, 'w', encoding='utf-8').write(s); print('CLAUDE.md: rule 9, log row 446')
