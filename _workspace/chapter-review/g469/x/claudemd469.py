#!/usr/bin/env python3
# Phase 469: CLAUDE.md: Book rules 8 (Korean words for chapter 13; its title waits), 11 (tempo built; next rhythm), 15
# (chapter 13 waits for the combined review too); the log row.
import sys, re
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
def rep(a, b):
    global s
    if s.count(a) != 1: raise SystemExit('found %d: %s' % (s.count(a), a[:70]))
    s = s.replace(a, b)
rep("   hertz is one entry and an extra drill level).",
    "   hertz is one entry and an extra drill level). Chapter 13: 빠르기(템포) and 빠르기말 (never 템포 단어), 메트로놈 표시, 미리 세기\n"
    "   (its other name 예비박), 꾸준하게, 서두르기, 처지기 (never 끌기: it reads as 끄다 and chapter 8's 끌다), 똑딱 소리, a tempo\n"
    "   본디 빠르기로; its title Tempo Race / 템포 경주 waits for her call (recommended: Tempo / 빠르기: a race means faster wins, but\n"
    "   the chapter ends on 'no rushing').")
rep("   ledger-lines (Level 3, written early). Next: Level 3's\n   tempo, rhythm, scales, accidentals (a new chapter), piano-story; then Levels 4 and 5.",
    "   ledger-lines (Level 3, written early), tempo (Level 3, built in full in Phase 469 under rule 15). Next: Level 3's\n   rhythm, scales, accidentals (a new chapter), piano-story; then Levels 4 and 5.")
rep("   (dynamics) and 12 (pitch-range).", "   (dynamics), 12 (pitch-range) and 13 (tempo).")
ROW = """| 469 | 2026-10-14 | **Chapter 13, Tempo Race, built in full (her 09:17 '계속 가줘 최종검토는 한꺼번에하게'; Book rules 14 and 15). The first room of Level 3.** The Lesson Book (7 pages, dictionary entries: tempo (Italian for 'time'), slow, fast; Adagio, Andante, Moderato, Allegro with their Italian glosses; tempo word, count-in (its other name 예비박); metronome (slide the weight down: faster), metronome mark (♩ = 60: 60 crotchet beats in a minute); steady tempo, rushing, dragging), its screen lesson (five pads: stm-sf, stm-words, stm-read, stm-metro with a sound switch that keeps the beat going, stm-steady that times eight taps alone), a 9-level drill on TEMPO_DRILL in the book's order (ear slow/fast, meanings, the faster word, slow to fast, ear words, find the tempo word on a page of music, metronome marks and what ♩ = 60 means, ear steady/rushing/dragging, an Extra level for rit., accel., a tempo and Presto) keeping the race track, the Workbook (pages 2 to 7, the check-up A to F, 18 marks) and the Teacher copy (2 pages, with pronunciation and the metronome spans). The four words sound at 70, 90, 110 and 140 (six seconds hold exactly 7, 9, 11 and 14 beats); slow and fast on page 2 at 60 and 120, as its ruler of seconds. Each piece title keeps one tempo word everywhere (STM_PIECES). New drawings: `StmMetronome` (scale 40 to 208 with the words beside it), `StmMark` and `stmMm` (the crotchet mark in drawings and on the text's baseline), `StmMiniPage` (a page of music: title, composer, tempo word, metronome mark, dynamic). Four fresh reviewers and two verifier rounds; fixed: dotted minims drawn without their dot, a steady-tempo check that could not be judged (now the metronome's sound off, then on), 끌기 read as 끄다 (now 처지기), 빠르기 defined with itself, a tempo glossed as Tempo primo, the drill out of the book's order and only recognition, tempo taken for loudness not taught, ♩ = 60 never asked, 'tick' meaning two things, alternating answers, titles paired with different words, the tempo word touching the clef, small tap targets on the music pages, 'Allegro' cut on phones, the ♩ glyph tiny and raised, a clipped metronome, words to circle too close, empty frames and PLAY boxes. No per-chapter review page: her combined final review comes later. Checks: wbcheck work, teacher, spread and lesson PASS in English and Korean; lbcheck 0/0. |
"""
m = re.search(r'^\| 468 \| [^\n]*\n', s, re.M)
if not m: raise SystemExit('row 468')
s = s[:m.end()] + ROW + s[m.end():]
open(p, 'w', encoding='utf-8').write(s); print('CLAUDE.md: rules 8, 11, 15; log row 469')
