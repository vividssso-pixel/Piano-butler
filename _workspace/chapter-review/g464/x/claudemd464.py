#!/usr/bin/env python3
# Phase 464: CLAUDE.md: Book rules 8 (two chapter names), 11 (time-signatures built), 13 (the more-scales question),
# 15 (where her review marks are kept); the log row.
import sys, re
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
def rep(a, b):
    global s
    if s.count(a) != 1: raise SystemExit('found %d: %s' % (s.count(a), a[:70]))
    s = s.replace(a, b)
rep("the lesson's words sit straight under the page title.\n",
    "the lesson's words sit straight under the page title. Chapter names (her 2026-10-14 00:36 '6번,23번만 바꾸자'):\n"
    "   chapter 6 is 'The Staff & the Two Clefs' / '오선과 두 음자리표' (once 'Reading the Staff'), and the composers chapter\n"
    "   'Composers' / '작곡가' (once 'Famous Composers'); the ids and the guide pages' search titles stay.\n")
rep("tones (Level 2);\n   ledger-lines (Level 3, written early). Next: Level 2's time-signatures (draft v1 in Phase 461; all as recommended, her 2026-10-13 23:51, built in full under rule 15), reading-steps, dynamics, pitch-range;",
    "tones, time-signatures (Level 2; time-signatures built in full in Phase 464 under rule 15, then her item-by-item review);\n   ledger-lines (Level 3, written early). Next: Level 2's reading-steps, dynamics, pitch-range;")
rep("Scales: pentatonic (named), whole-tone, blues.",
    "Scales: pentatonic (named), whole-tone, blues. More scales (her 2026-10-14 00:36 '스케일은 장단음계 빼고 다른 모드나 블루스\n"
    "   스케일같은건 챕터 더 만들거야? 아니면 하나로 다 넣으면 너무 많나'): recommended ONE new room on Level 5 beside Styles, 'More Scales:\n"
    "   Pentatonic, Blues, Whole-tone & Modes' / '여러 가지 음계'; the chromatic scale stays in chapter 11; waiting for her answer.")
rep("   decide: strategy, money, anything sent outside, deleting, AdSense.\n",
    "   decide: strategy, money, anything sent outside, deleting, AdSense. The review page is a private artifact; its `db`\n"
    "   collection `verdicts` keeps her marks, one document per item (`<chapter key>-<item>`: `v` 'ok' or 'change', `note`).\n"
    "   Read them with ArtifactData `list` when she says she has finished, then fix every Change. Chapter 8's page:\n"
    "   https://claude.ai/artifact/J4QaR5BUxDJoWRbE8fFPjB (keys `ts8-...`).\n")
ROW = """| 464 | 2026-10-14 | **Chapter 8, Time Signatures, built in full (Book rules 14 and 15).** The Lesson Book (7 pages; dictionary entries with `LbDefs`: bar line, bar, double bar line, repeat sign; time signature, top number, bottom number, C; strong, medium and weak beat; crotchet, minim and semibreve rest; tie; a page 7 of five checks shown at the piano), its screen lesson (five tools: ts-bars, ts-numbers, ts-strong, ts-build, ts-tie; the tap pads hold each note; Build a bar refuses what ABRSM and AMEB mark wrong), the drill (10 levels: beats in a bar, the bar line, tap the strong beat, rests on the staff, fill the bar, ties, then whole-bar rests, the bottom number, compound time and simple / compound / irregular, each named with its grades), the Workbook (pages 2 to 7, the check-up A to E) and the Teacher copy (2 pages); staves drawn by `tsRaw` / `TsStaff`. Four fresh reviewers (teaching, theory against AMEB and ABRSM, a child's reading, print and screen) and a verifier; every valid point fixed (clipped staves, hearts over boxes, bar lines touching heads, the tie's curve, level 6's answer always second, the words). Grouping, duplets and regroup move to the Rhythm chapter's toolbox. Korean 마디선 is now 세로줄. Her 00:36: chapter 6 is 'The Staff & the Two Clefs' / '오선과 두 음자리표', the composers chapter 'Composers' / '작곡가' (drills, printables, teacher dashboard). The Korean drop capital takes the page's own font. printables.html: every card's chapter number now follows the map (most were still from the old order); the chapter 8 card shows the new Workbook page 4. Her item-by-item review: https://claude.ai/artifact/J4QaR5BUxDJoWRbE8fFPjB (37 items, G1 to G3 as my guesses). Known, in that review: two check-up staves under 5 mm (A 3.9, E 3.2; the page is full). Checks: wbcheck work, teacher, spread and lesson PASS in English and Korean; lbcheck 0/0 for time-signatures and staff. |
"""
m = re.search(r'^\| 463 \| [^\n]*\n', s, re.M)
if not m: raise SystemExit('row 463')
s = s[:m.end()] + ROW + s[m.end():]
open(p, 'w', encoding='utf-8').write(s); print('CLAUDE.md: rules 8, 11, 13, 15; log row 464')
