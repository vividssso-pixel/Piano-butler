#!/usr/bin/env python3
# Phase 465: CLAUDE.md: Book rules 10 and 13 (the More Scales room, her 06:42); rule 8 (bar line in Korean); the log row.
import sys, re
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
def rep(a, b):
    global s
    if s.count(a) != 1: raise SystemExit('found %d: %s' % (s.count(a), a[:70]))
    s = s.replace(a, b)
rep("(27 once Accidentals, room 17 on Level 3, has its chapter; until then it stays off the map).",
    "(27 once Accidentals, room 17 on Level 3, has its chapter; until then it stays off the map; likewise More Scales,\n"
    "   `more-scales`, the last room on Level 5 after Styles, so no chapter number moves when it comes).")
rep("Scales: pentatonic (named), whole-tone, blues. More scales (her 2026-10-14 00:36 '스케일은 장단음계 빼고 다른 모드나 블루스\n"
    "   스케일같은건 챕터 더 만들거야? 아니면 하나로 다 넣으면 너무 많나'): recommended ONE new room on Level 5 beside Styles, 'More Scales:\n"
    "   Pentatonic, Blues, Whole-tone & Modes' / '여러 가지 음계'; the chromatic scale stays in chapter 11; waiting for her answer.",
    "Scales: the pentatonic, whole-tone and blues scales and the modes get a room of their own (her 2026-10-14\n"
    "   00:36 '스케일은 장단음계 빼고 다른 모드나 블루스 스케일같은건 챕터 더 만들거야?', then 06:42 '응 스케일 너 추천대로가자'): More\n"
    "   Scales / 여러 가지 음계 (`more-scales`; the book's subtitle Pentatonic, Blues, Whole-tone & Modes), the last room on\n"
    "   Level 5, after Styles; the Scales room keeps major and minor; the chromatic scale stays in chapter 11.")
rep("Skewer, not kebab (Korean 꼬치);",
    "A bar line is 세로줄 in Korean everywhere (never 마디선 or 마디줄; Phases 464, 465). Skewer, not kebab (Korean 꼬치);")
ROW = """| 465 | 2026-10-14 | **More Scales gets its room (her 06:42 '응 스케일 너 추천대로가자').** `PATH_STAGES` Level 5 lists `more-scales` after Styles; like accidentals it stays off the map until its chapter exists, and it is numbered last so no chapter number moves. Book rules 10 and 13 say where the pentatonic, whole-tone and blues scales and the modes go. Korean: the last ten 마디줄 (the accidentals tools and the Level 2 line on the map) are 세로줄, as chapter 8 defines the bar line. The review board (artifact WPcDbn32yCFzyYTYcFCzTF) now shows the five levels, the current names and the two rooms to come. |
"""
m = re.search(r'^\| 464 \| [^\n]*\n', s, re.M)
if not m: raise SystemExit('row 464')
s = s[:m.end()] + ROW + s[m.end():]
open(p, 'w', encoding='utf-8').write(s); print('CLAUDE.md: rules 8, 10, 13; log row 465')
