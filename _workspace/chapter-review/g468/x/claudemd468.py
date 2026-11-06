#!/usr/bin/env python3
# Phase 468: CLAUDE.md: Book rules 8 (Korean words for chapter 12; its title waits), 11 (pitch-range built: Level 2 done;
# next Level 3), 15 (chapters 10 and 12 wait for the combined review); the log row.
import sys, re
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
def rep(a, b):
    global s
    if s.count(a) != 1: raise SystemExit('found %d: %s' % (s.count(a), a[:70]))
    s = s.replace(a, b)
rep("   call (recommended: 셈여림과 아티큘레이션; the standard spelling is 다이내믹).",
    "   call (recommended: 셈여림과 아티큘레이션; the standard spelling is 다이내믹). Chapter 12: 음높이, 음역, 낮은 음 / 가운데 음 /\n"
    "   높은 음, 현악기 / 목관 악기 / 금관 악기 / 타악기, 떨림, 헤르츠, 베이스 가수 (the voice; 더블베이스 the instrument); its\n"
    "   title Pitch, Hz & Range (음높이, 헤르츠와 음역) waits for her call (recommended: Pitch & Range, 음높이와 음역, since\n"
    "   hertz is one entry and an extra drill level).")
rep("tones, time-signatures, reading-steps, dynamics (Level 2; time-signatures, reading-steps and dynamics built in full in Phases\n   464, 466 and 467 under rule 15, then her item-by-item review);",
    "tones, time-signatures, reading-steps, dynamics, pitch-range (Level 2, done; time-signatures, reading-steps, dynamics and\n   pitch-range built in full in Phases 464, 466, 467 and 468 under rule 15, then her item-by-item review);")
rep("ledger-lines (Level 3, written early). Next: Level 2's pitch-range; then Level 3's\n   tempo, rhythm, scales, accidentals (a new chapter), piano-story; then Levels 4 and 5.",
    "ledger-lines (Level 3, written early). Next: Level 3's\n   tempo, rhythm, scales, accidentals (a new chapter), piano-story; then Levels 4 and 5.")
rep("   `<chapter key>-<item>` as before), made when she asks for it, instead of a page per chapter.",
    "   `<chapter key>-<item>` as before), made when she asks for it, instead of a page per chapter. Waiting for it: chapters 10\n"
    "   (dynamics) and 12 (pitch-range).")
ROW = """| 468 | 2026-10-14 | **Chapter 12, Pitch, Hz & Range, built in full (her 09:17 '계속 가줘 최종검토는 한꺼번에하게'; Book rules 14 and 15). Level 2 is done.** The Lesson Book (7 pages, dictionary entries: low (far left on the keys: the bottom of the bass staff and below), high (far right: the top of the treble staff and above), middle (middle C and the keys near it, from the G below to the F above); vibrate (big and long vibrate slowly and sound low), hertz (the A above middle C: 440 Hz); instrument family and the four families with how each makes its sound (the piano: a string instrument played like a drum); the violin family ('In one family, the bigger, the lower') and the voices; range, piccolo, the piano's range (88 keys, the lowest A to the highest C)), its screen lesson (five pads: spr-zone, spr-big, spr-fam, spr-ladder, spr-range), a 9-level drill on PITCH_RANGE_DRILL (low/middle/high on the keys, which sounds higher, which family, how it sounds, which can go lower, two by ear, Extras: each A doubles in hertz, which instrument can play a key), the Workbook (pages 2 to 7, the check-up A to F, 21 marks) and the Teacher copy (2 pages). New drawings: `SprInst` (13 instruments in navy line with a coral touch), `SprFiddle` (the violin family to scale, the double bass with sloping shoulders), `SprKeys88` (the 88 keys with a key, a range or dots), `SprKeysPart` (bare keys to draw on). Child-facing words name notes by letter only (no octave numbers); the drill and the Workbook keep to clear cases (low up to G2, middle G3 to F4, high from G5). Four fresh reviewers and a verifier (two rounds); fixed: vague low/high, English-only extra levels with untaught instruments, a Workbook task that needed an adult, PLAY tasks that repeated the book's At the piano, empty space, a cello icon no bigger than the violin, labels on staff lines, 'coral' for children (now orange), 'Woodwind and brass: blow' (now Strings: bow or pluck. Woodwind: blow. Brass: buzz. Percussion: hit.), the same Your turn on two pages, tested-but-untaught ranges, a blank Teacher answer, KO wording. No per-chapter review page: her combined final review comes later. Checks: wbcheck work, teacher, spread and lesson PASS in English and Korean; lbcheck 0/0. |
"""
m = re.search(r'^\| 467 \| [^\n]*\n', s, re.M)
if not m: raise SystemExit('row 467')
s = s[:m.end()] + ROW + s[m.end():]
open(p, 'w', encoding='utf-8').write(s); print('CLAUDE.md: rules 8, 11, 15; log row 468')
