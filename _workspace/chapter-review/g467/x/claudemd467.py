#!/usr/bin/env python3
# Phase 467: CLAUDE.md: Book rules 8 (Korean words for a slur, a tie, crescendo; the chapter 10 title waits), 11 (dynamics
# built), 15 (her 09:17: chapters back to back, one combined final review later); the log row.
import sys, re
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
def rep(a, b):
    global s
    if s.count(a) != 1: raise SystemExit('found %d: %s' % (s.count(a), a[:70]))
    s = s.replace(a, b)
rep("   marked with a straight bracket and its word.",
    "   marked with a straight bracket and its word. A slur is 이음줄 and a tie 붙임줄 (never 슬러; Phase 467); 크레셴도, 디미누엔도,\n"
    "   데크레셴도; dynamics are 셈여림 in the text, its other name 다이나믹; the chapter 10 title 다이나믹과 아티큘레이션 waits for her\n"
    "   call (recommended: 셈여림과 아티큘레이션; the standard spelling is 다이내믹).")
rep("tones, time-signatures, reading-steps (Level 2; time-signatures and reading-steps built in full in Phases 464 and 466 under\n   rule 15, then her item-by-item review);",
    "tones, time-signatures, reading-steps, dynamics (Level 2; time-signatures, reading-steps and dynamics built in full in Phases\n   464, 466 and 467 under rule 15, then her item-by-item review);")
rep("ledger-lines (Level 3, written early). Next: Level 2's dynamics, pitch-range; then Level 3's",
    "ledger-lines (Level 3, written early). Next: Level 2's pitch-range; then Level 3's")
rep("   (keys `ss9-...`).",
    "   (keys `ss9-...`). From chapter 10 on (her 2026-10-14 09:17 '계속 가줘 최종검토는 한꺼번에하게') the chapters are built back\n"
    "   to back, each with its reviewers and fixes, and she reviews them all at once: one combined review page (keys\n"
    "   `<chapter key>-<item>` as before), made when she asks for it, instead of a page per chapter.")
ROW = """| 467 | 2026-10-14 | **Chapter 10, Dynamics & Articulation, built in full (her 09:17 '계속 가줘 최종검토는 한꺼번에하게'; Book rules 14 and 15).** The Lesson Book (7 pages, dictionary entries: dynamics, p, f; pp, mf ('m means medium. The same letter twice means very.'); hairpin, crescendo, diminuendo (other name decrescendo); articulation, legato (its sign the slur), staccato (a dot on the side away from the stem); slur (lift after the last note) beside the tie; how to make p and f at the piano), its screen lesson (five pads: sdy-pf, sdy-ladder, sdy-hair, sdy-touch, sdy-tie), a 9-level drill on DYN_DRILL (meanings, which is louder, hairpins and the words cresc./dim./decresc., legato or staccato, tie or slur, three by ear, an Extra level for mp and ff), the Workbook (pages 2 to 7, the check-up A to F, 18 marks) and the Teacher copy (2 pages). Marks drawn by `sdyMarks` / `SdyStaff` over chapter 9's `sskRaw`: dynamics centred under their notes, hairpins clear of the signs, staccato dots never on a line, slurs and ties on the head side and never along a staff line (a tie between line notes stays flat in the space), sound lines (legato touching across the bar, staccato short, a tie one line). Four fresh reviewers and a verifier; fixed: two tunes that were songs (Hänschen klein, Frère Jacques), 'Two letters mean very' (mf), legato lines broken at the bar, ties on a staff line, a Workbook PLAY that copied its book page, answers given away in the instructions, crowded words to circle and small write boxes, empty PLAY boxes (now two tunes each), the drill's words in level 3 and mp/ff alone in level 9, KO wording (위/아래 악보, 이음줄로 이은, 줄임말). Elsewhere: a slur is 이음줄 in the older strings; 크레셴도; `.choice-btn:hover` only where there is hover (a tapped answer looked chosen on phones); a semibreve's ledger line a little wider; 'easier after' names chapter 9. No per-chapter review page: her combined final review comes later. Checks: wbcheck work, teacher, spread and lesson PASS in English and Korean; lbcheck 0/0. |
"""
m = re.search(r'^\| 466 \| [^\n]*\n', s, re.M)
if not m: raise SystemExit('row 466')
s = s[:m.end()] + ROW + s[m.end():]
open(p, 'w', encoding='utf-8').write(s); print('CLAUDE.md: rules 8, 11, 15; log row 467')
