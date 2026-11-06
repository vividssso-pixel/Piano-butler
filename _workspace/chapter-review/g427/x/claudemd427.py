#!/usr/bin/env python3
# Phase 427: CLAUDE.md row -- chapter 6's Lesson Book draft v1 and review pack.   python3 claudemd427.py <repo root>
import sys, os
p = os.path.join(sys.argv[1], 'CLAUDE.md'); s = open(p, encoding='utf-8').read()
lines = s.split('\n')
i = [k for k, l in enumerate(lines) if l.startswith('| 426 |')]
if len(i) != 1: raise SystemExit('row 426 found %d' % len(i))
if any(l.startswith('| 427 |') for l in lines): raise SystemExit('row 427 already there')
row = ("| 427 | 2026-10-10 | **Chapter 6 (Ledger Lines) started: Lesson Book draft v1 + review pack.** After her '응' (18:27) to 'next is chapter 6, the one we paused'. "
  "Built on her standing decisions: Clara's ladder rung (chapter 4) gets its real name, ledger line; Queensland and Kingsland (chapter 5); the bird's sky and the turtle's sea (chapter 2) for up and down; "
  "chapter 5's three Cs grow to five (Sea C C2, Kingsland C, Clara's C, Queensland C, Sky C C6); AMEB checked (Music Craft Prelim: one ledger line below the treble; Grade 1: one above and below both staves; "
  "Grade 2: up to three; Theory Grade 1 two, Grade 2 three; 'leger' and 'ledger' both accepted). Draft 7 pages (_workspace/chapter-review/g427/x/ll427.jsx + apply427.py; a draft build only, "
  "drills.src.html unchanged): the ladders out of both lands; Clara's rung is a ledger line (draw it a little wider than the note, the same distance apart, no gaps, never one too many: one tick, three crosses); "
  "Up into the sky (F, G, then A C E on rungs 1-3); Down into the sea (G, F, then E C A on rungs 1-3); Between the lands (borrowed rungs: A on rung 2 under Queensland = Kingsland's top line, "
  "E on rung 2 over Kingsland = Queensland's bottom line, Clara's C one rung from both); Five Cs (every ledger note in the book is a step or a skip from Sea C, Clara's C or Sky C); My five checks. "
  "A fresh-eyes reviewer checked every note, ledger count and rung label en+ko (all correct); its fixes are in (the 'nearest C' rule made exact, 'a little wider', the no-gap cross, rung 2 wording, "
  "Korean 한 걸음 not 한 칸). Review pack Claude outputs/Chapter-06-review-v1-Ledger-Lines.pdf (12 pages): G1-G3 guide questions; A1-A8 on today's chapter 6 (not the book on screen, "
  "treble/bass/middle C names, twelve notes in four lists, drill level 1 mixes everything, the screen's moving parts don't fit the pages, the Phase 298 Workbook/Teacher copy, the old blue picture, "
  "'In this chapter' left in English in every Korean book); B1-B9 with recommendations (name, sky/sea ladder, Sky C/Sea C, three rungs, drop the four lists, keep Between the lands, 7 drill levels, "
  "Workbook W1-W6, minimal opener). |")
lines.insert(i[0] + 1, row)
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('row 427 added')
