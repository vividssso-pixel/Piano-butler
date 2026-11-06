#!/usr/bin/env python3
# Phase 455: CLAUDE.md: the log row, and Book rule 11 (pulse is done).
import sys, re
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
ROW = """| 455 | 2026-10-13 | **Chapter 3, Pulse & Counting: the Lesson Book, finished (Level 1).** Her 'b 전부 추천대로' with G1 (her two pulse faults: not keeping the count steady; playing the first beat and starting the count late), G2 (walk, running; + for 'and', rule 12) and G3 (no parents' tip). patch455.py on Phase 446's draft: B1 pictures (heart, beat circles, footprints); B2 'pulse' in the title and opener only, 'beat' everywhere else (박); B3 no faster or slower anywhere (gaps that change: shorter, longer, a stop); B4 strong and weak beats moved to Time signatures; B5 1 2 3 4 only; B6 silent beats dashed, no rest names; B7 bird / tur-tle / light-house (새 / 거-북 / 등-대); B8 finger numbers in coral circles (LbTune coral); B9 a 5-level tapped drill on the audio clock (steady or not; tap along; keep it going on your own; count inside, tap one beat; tap the beat, not the words; scored against the scheduled beat + output latency, tested with timed key presses); B10 Workbook pages 2-6 (set tasks: footprint trails, number the beats, the counting snake, count every beat, fix the count, one dot for each sound, words from dots, which finger on the beat, read the keys) and the paper check-up (A-E, 20 marks); B11 the online lesson is the book on screen (PlSteadyPad, PlCountRing, PlSilentBeats, PlWordsBeat, PlFingerBeat). Teacher copy: answers, both faults in the watch-fors, a 'walk, then run' box; chapter numbers via bkChapterNo. Toolbox: the pulse room's tools are the book's moving parts (count-ring, silent-beats, finger-beat new; beat-or-rhythm now PlWordsBeat); beat-groups and beat-target moved to Time signatures, count-aloud to Notes and rests, each added as the LAST step of those lessons so no step link moves. Fixes on the way: the spread for tones (and now pulse) pairs each workbook page with its own lesson page (tones was one page off; LB_PAGE_FNS); a tapped drill has no printed worksheet (noPrint). Checked: lbcheck, wbcheck, PLAY space under 35 px, all 126 printed books fit (en, ko), ch1/fitko/sf/ws/ll/tn tests, phone width 360-390, and a fresh reviewer against the Book rules (two rounds, all answers verified). Next: the pulse guide page (G1, G2), then note-values. |
"""
m = re.search(r'^\| 454 \| [^\n]*\n', s, re.M)
if not m: raise SystemExit('row 454')
s = s[:m.end()] + ROW + s[m.end():]
a = "Done: posture-hands, first-steps, note-names, staff (Level 1);"
if s.count(a) != 1: raise SystemExit('rule 11 done')
s = s.replace(a, "Done: posture-hands, first-steps, note-names, staff, pulse (Level 1);")
m = re.search(r"Next: Level 1's pulse \(draft v1, Phase 446, waiting for her answers to G1-G3\s+and B1-B11\) and note-values;", s)
if not m: raise SystemExit('rule 11 next')
s = s[:m.start()] + "Next: Level 1's note-values;" + s[m.end():]
open(p, 'w', encoding='utf-8').write(s); print('CLAUDE.md: log row 455, rule 11')
