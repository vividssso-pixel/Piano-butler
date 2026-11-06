#!/usr/bin/env python3
# Phase 466: CLAUDE.md: Book rules 8 (Korean words for a step and a tune; no curve between notes), 11 (reading-steps
# built), 15 (chapter 9's review page); the log row.
import sys, re
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
def rep(a, b):
    global s
    if s.count(a) != 1: raise SystemExit('found %d: %s' % (s.count(a), a[:70]))
    s = s.replace(a, b)
rep("A bar line is 세로줄 in Korean everywhere (never 마디선 or 마디줄; Phases 464, 465).",
    "A bar line is 세로줄 in Korean everywhere (never 마디선 or 마디줄; Phases 464, 465). A step is 한 걸음 and a tune 선율 (never 한 칸\n"
    "   or 튠; Phase 466); a move is said direction first: 위로 한 걸음, 아래로 건너뛰기; the chapter 9 title 차례가기와 건너뛰기 waits for\n"
    "   her call (recommended: 한 걸음과 건너뛰기). No curve between two notes but a tie (and, from chapter 10, a slur): a move is\n"
    "   marked with a straight bracket and its word.")
rep("tones, time-signatures (Level 2; time-signatures built in full in Phase 464 under rule 15, then her item-by-item review);",
    "tones, time-signatures, reading-steps (Level 2; time-signatures and reading-steps built in full in Phases 464 and 466 under\n   rule 15, then her item-by-item review);")
rep("ledger-lines (Level 3, written early). Next: Level 2's reading-steps, dynamics, pitch-range; then Level 3's",
    "ledger-lines (Level 3, written early). Next: Level 2's dynamics, pitch-range; then Level 3's")
rep("https://claude.ai/artifact/J4QaR5BUxDJoWRbE8fFPjB (keys `ts8-...`).",
    "https://claude.ai/artifact/J4QaR5BUxDJoWRbE8fFPjB (keys `ts8-...`); chapter 9's: https://claude.ai/artifact/4dCGVtL6SsPyfeakiZAzrS\n   (keys `ss9-...`).")
ROW = """| 466 | 2026-10-14 | **Chapter 9, Steps & Skips, built in full (her 06:54 '계속 가줘'; Book rules 14 and 15).** The Lesson Book (7 pages, dictionary entries: tune, up, down, same note; step and skip by letters, 'In C and G position, the next white key / jump over one white key', their other names a 2nd and a 3rd; five-finger position, C position, G position; sight-reading), its screen lesson (five pads: ssk-shape, ssk-step, ssk-cpos, ssk-gpos, ssk-read), a 9-level drill (up/down/same, step/skip/same, the next note, fingers in C and G position, two by ear, an Extra level of all twelve positions), the Workbook (pages 2 to 7, the check-up A to E, 32 marks) and the Teacher copy (2 pages); tunes drawn by `sskRaw` / `SskStaff` / `SskSystems`, positions by `SskPosPic` (each note over its key). Four fresh reviewers and a verifier; fixed: curves between notes (they read as ties) now straight brackets, step and skip defined by letters, the left hand in G position at the piano, Workbook page 6's first notes carry their finger (a note alone does not give the position), word boxes now words to circle, leaps and weak endings out of the tunes, the screen tools no longer give the answer, the drill's tunes numbered 1 2 3. Elsewhere: lit keys on every on-screen keyboard show their numbers and letters navy or white (MARK_STYLE text); MOVE_KO says 위로 한 걸음; this chapter's older tools say 한 걸음 and 선율; 'easier after' names chapters 7 and 8. Her review: https://claude.ai/artifact/4dCGVtL6SsPyfeakiZAzrS (36 items, G1 to G3 as my guesses, the Korean title as a call). Checks: wbcheck work, teacher, spread and lesson PASS in English and Korean; lbcheck 0/0. |
"""
m = re.search(r'^\| 465 \| [^\n]*\n', s, re.M)
if not m: raise SystemExit('row 465')
s = s[:m.end()] + ROW + s[m.end():]
open(p, 'w', encoding='utf-8').write(s); print('CLAUDE.md: rules 8, 11, 15; log row 466')
