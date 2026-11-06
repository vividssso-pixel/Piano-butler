#!/usr/bin/env python3
# Phase 475: CLAUDE.md: Book rules 8 (Korean words for chapter 20), 11 (signs built; next; her macro-first decision of
# 2026-10-17 02:05), 15 (chapter 20 waits for the combined review too); the log row.
import sys, re
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
def rep(a, b):
    global s
    if s.count(a) != 1: raise SystemExit('found %d: %s' % (s.count(a), a[:70]))
    s = s.replace(a, b)
rep("   it (a word joiner). Skewer, not kebab",
    "   it (a word joiner). Chapter 20: 도돌이표 (chapter 8's), 시작 도돌이표 / 끝 도돌이표 (끝세로줄 앞의 점 두 개), 1번 괄호 / 2번\n"
    "   괄호 (숫자 1이 적힌 괄호; never 괄호를 치다 for playing: 1번 괄호 마디를 쳐요), 겹세로줄 (two thin lines, under Fine), Fine\n"
    "   (피네, so Fine와 / Fine를), 다 카포 (첫머리부터), 달 세뇨, 세뇨, 늘임표 (other name 페르마타; 제 길이보다 더 길게 늘여요),\n"
    "   'N마디' for bar N, 그림 아래의 차례로 (never 차례대로 before a number string), 'N번 괄호' and 'D.C. al Fine' kept on one\n"
    "   line. Skewer, not kebab")
rep("   Phase 473): Level 3 is done. Level 4: key-signatures (Phase 474). Next: signs, intervals, chords, composers, melody\n"
    "   (PATH_STAGES order); then Level 5.",
    "   Phase 473): Level 3 is done. Level 4: key-signatures (Phase 474), signs (Phase 475). Next (her 2026-10-17 02:05\n"
    "   '1.2.3. 다동의해' to a macro-first plan: see the whole, then the parts): first a pass on scales (16) and key-signatures\n"
    "   (19): a 12-key map on the keyboard clock (a semitone a step; the scale clock reused) as the chapter's first page, the\n"
    "   steps zooming in, the map again at the end ('the keys I know' coloured); the teacher sets each student's keys in the\n"
    "   dashboard (default: the exam keys; all 12 possible) and the drills and pads use them; Workbook pages that work in any\n"
    "   key ('___ major'); keys learned in fingering groups (C G D A E share both hands' fingering); reading key signatures\n"
    "   stays step by step. Then intervals and chords built the same way (a triad one shape in all 12 keys, then the\n"
    "   student's I IV V); composers, melody; then Level 5.")
rep("   (dynamics), 12 (pitch-range), 13 (tempo), 14 (rhythm), 16 (scales), 17 (accidentals), 18 (piano-story) and 19\n"
    "   (key-signatures).",
    "   (dynamics), 12 (pitch-range), 13 (tempo), 14 (rhythm), 16 (scales), 17 (accidentals), 18 (piano-story), 19\n"
    "   (key-signatures) and 20 (signs).")
ROW = """| 475 | 2026-10-17 | **Chapter 20, Signs, built in full (her 09:17 '계속 가줘 최종검토는 한꺼번에하게'; Book rules 14 and 15). The second room of Level 4.** The level plan's scope (the tie and the slur stay in chapter 10; 8va, ornaments and al Coda in the toolbox): the road signs. The Lesson Book (7 pages, dictionary entries): the opener (the signs show the road: which bars to play again, where to go back to, where to stop, which note to hold; the six signs drawn, one whole note a bar); repeat signs (start and end; back to the start-repeat sign or to the beginning); 1st and 2nd time bars; D.C. al Fine (Fine said fee-nay, over two thin bar lines); D.S. al Fine (the segno on bar 2); the pause (over a note or rest, two examples with time boxes, in time and held); My five checks. Each road picture has its bar numbers and 'Play the bars in this order'. The road model: bars with their signs, one playing-order rule (`sgnOrder`: a repeat once, not after a D.C./D.S.; the 1st time bar skipped the second time and after a jump; Fine and To Coda after a jump). The screen lesson: a pad on pages 2 to 6 (▶ Listen lights each bar as it sounds and says why it jumps; ▶ Your turn: tap the bar numbers in order; page 6 over a note or a rest, with and without the pause). The segno, coda and pause are drawn as SVG (no music font needed). A 9-level drill (what each sign tells you; the order with repeat signs, 1st and 2nd time bars, D.C. al Fine, D.S. al Fine; how many bars; listening: played right or wrong; all the roads; extra: al Coda with its key line); no answer twice running; wrong options are real mistakes (no repeat, back to the beginning, the 1st time bar again, past Fine, D.S. to the beginning...). The Workbook (pages 2 to 6, one drawing task a page: repeat signs on the staff, the brackets, Fine, the segno, the pause; circle the pauses among ties and slurs; the check-up 8 marks) at about 3.3 mm a staff space (5-bar roads about 3.0 mm), and the Teacher copy (AMEB and ABRSM placement, how the signs are written, the road check in lessons). Four reviewers (theory, Korean, design, code QA) and a verifier (77 of 86 held; the rest and the new points fixed). Kept for her combined review: the exact ABRSM grade of the pause, repeat marks and volta brackets (the PDF's table could not be read reliably; the copy says 'by Grade 3'), 5-bar reading roads at about 3.0 mm, 다 카포 / 달 세뇨 spacing, the printed level-1 worksheet's coral sign (colour printing). Shared: chapter 8's bar-line tool says 시작 / 끝 도돌이표; chapter 10's list 'Pause (fermata)' / '늘임표 (페르마타)'; the chapter's grade tag G1–G2; 'Easier after' chapters 8 and 9; old lesson ticks ignored as in chapter 19 (`skgOldStep`). printables.html: the chapter 20 card shows Workbook page 4 with new words. Waits for her combined review. |
"""
m = re.search(r'^\| 474 \| [^\n]*\n', s, re.M)
if not m: raise SystemExit('row 474')
s = s[:m.end()] + ROW + s[m.end():]
open(p, 'w', encoding='utf-8').write(s); print('CLAUDE.md: rules 8, 11, 15; log row 475')
