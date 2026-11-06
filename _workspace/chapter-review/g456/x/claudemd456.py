#!/usr/bin/env python3
# Phase 456: CLAUDE.md: the log row.
import sys, re
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
ROW = """| 456 | 2026-10-13 | **Chapter 3's guide page.** Her 18:22 '응 계속 가줘' after Phase 455. lessons/pulse-and-counting.html (--final, no dashes, one colon a sentence): her G1 in the teacher's note (the count that does not stay steady; the first note played before the count starts, so every number lands behind its beat) and G2 (walking first, running later; the count grows as the time signature counts, 1 2 3 4, 1 + 2 + 3 + 4 +, 1 e + a 2 e + a, the + read 'and'); no parents' tip (G3). The book's own six drawings (svg/pulse, guide456svg.js), the three finger rows in coral circles (build.py's new {{fingers:...}}, README), Workbook page 4 (count every beat, colour the beats you play, fix the count) as the worksheet (lessons/img/pulse-worksheet.jpg and printables/img/wb-pulse.jpg; the printables card now says chapter 3, no '--'). Room 3 open on the guides' house (house428gen.js; house.jpg remade), its card in Open rooms; keyboard-patterns and musical-alphabet now link to it; sitemap. Counts keep their spaces unbroken (&nbsp;). |
"""
m = re.search(r'^\| 455 \| [^\n]*\n', s, re.M)
if not m: raise SystemExit('row 455')
s = s[:m.end()] + ROW + s[m.end():]
open(p, 'w', encoding='utf-8').write(s); print('CLAUDE.md: log row 456')
