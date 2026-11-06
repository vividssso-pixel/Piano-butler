#!/usr/bin/env python3
# Phase 434 in CLAUDE.md: the Phase row.   python3 claudemd434.py <CLAUDE.md>
import sys
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
if '| 434 | 2026-10-12 |' in s: raise SystemExit('CLAUDE.md: row 434 already there')
row = """| 434 | 2026-10-12 | **Chapter 7 draft v2: the half step and the whole step.** Her 09:30 'other ideas than best friend? and teach that these are the same as half step / whole step', then 09:35 '너 추천대로 가자 말이 되게 서로 연결되는게 좋으니' -- of four options (half step / whole step; next-door neighbour / two doors down; chess squares; best friend), the one where the names themselves say it: a semitone is a HALF STEP (반음 = 반 걸음), the very next key; a tone is a WHOLE STEP (온음 = 온 걸음), two half steps, one key in between. Both pairs of English names are taught (semitone and tone in Australian and British books, half step and whole step in American books); chapter 3's letter steps are whole or half (C to C: whole, whole, half, whole, whole, whole, half); 'as close as a best friend' stays as one phrase on page 2. Pages 1-5 redrawn and rewritten (tn434.jsx in _workspace/chapter-review/g434/x; still a draft build, drills.src.html unchanged): footprints where a step lands (coral half, navy whole), 'half' over each small hop and 'a whole step' over the arc, the half-step walk (C to C = 12 half steps), 'Half or whole?' pairs, sharp/flat = up/down a half step. Review pack v2 (Claude outputs/Chapter-07-review-v2-Tones-Semitones.pdf): B1 settled; B2, B4, B5, B8-B11 reworded for the step; A4 noted. Checks: lbcheck tones 0 overflow en/ko. |
"""
i = s.index('| 433 | 2026-10-12 |'); j = s.index('\n', i) + 1
s = s[:j] + row + s[j:]
open(p, 'w', encoding='utf-8').write(s); print('CLAUDE.md ok')
