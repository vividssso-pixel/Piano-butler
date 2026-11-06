#!/usr/bin/env python3
# Phase 470: CLAUDE.md: Book rules 8 (Korean words for chapter 14), 11 (rhythm built; next scales), 15 (chapter 14 waits
# for the combined review too); the log row.
import sys, re
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
def rep(a, b):
    global s
    if s.count(a) != 1: raise SystemExit('found %d: %s' % (s.count(a), a[:70]))
    s = s.replace(a, b)
rep("   the chapter ends on 'no rushing').",
    "   the chapter ends on 'no rushing'). Chapter 14: 8분음표 묶기, 혼자 있는 8분음표 (never 혼자인), 꼬리 (flag), 빔, 마디\n"
    "   한가운데, 8분쉼표, 점4분음표, 여린내기 (starting before beat 1) and 못갖춘마디 (the short bar), its pair 갖춘마디 (never 온\n"
    "   마디), 미리 세기 (its other name 예비박), 당김음, 16분음표; a place in the bar is an ordinal (첫 박, 넷째 박: never '1박보다\n"
    "   먼저') and a length a count word (한 박, 두 박, 반 박, 한 박 반); the counts '2 다음 +'. Its title Rhythm Patterns / 리듬\n"
    "   패턴 stays (리듬꼴 is the school-book word, offered once).")
rep("   ledger-lines (Level 3, written early), tempo (Level 3, built in full in Phase 469 under rule 15). Next: Level 3's\n   rhythm, scales, accidentals (a new chapter), piano-story; then Levels 4 and 5.",
    "   ledger-lines (Level 3, written early), tempo (Level 3, built in full in Phase 469 under rule 15), rhythm (Level 3,\n   Phase 470). Next: Level 3's scales, accidentals (a new chapter), piano-story; then Levels 4 and 5.")
rep("   (dynamics), 12 (pitch-range) and 13 (tempo).", "   (dynamics), 12 (pitch-range), 13 (tempo) and 14 (rhythm).")
ROW = """| 470 | 2026-10-14 | **Chapter 14, Rhythm Patterns, built in full (her 09:17 '계속 가줘 최종검토는 한꺼번에하게'; Book rules 14 and 15). The second room of Level 3.** The Lesson Book (7 pages, dictionary entries: quaver, beam (in 4/4 it may join four, on beats 1 and 2 or 3 and 4), the middle of the bar; flag, quaver rest; dotted crotchet (the dot adds half the note's length), dotted crotchet and quaver (1 2 +); anacrusis (other names upbeat, pick-up), incomplete bar (usually the last bar too), count-in (one bar, then the missing beats); reading a rhythm), every note on G, right hand finger 3 as in chapter 8, every playable staff numbered (Line 1, 2, 3); its screen lesson (one listen-and-tap pad per page, srh-beams to srh-read; a tap is scored on time and on length: a crotchet held at least about half a beat, a longer note to within 0.4 of a beat of its end, a note before a rest let go by the rest); a 9-level drill on RHYTHM_DRILL in the book's order (beamed right?, how many beats, which count, fill the bar with every gap one width, before beat 1 (start beat, last-bar length), listen: which rhythm (never two with the same note starts), tap the rhythm; Extra semiquavers 1 e + a, Extra syncopation inside half a bar); the Workbook (pages 2 to 7, count lines with a box under every half beat, the check-up A to F, 16 marks, no practice bar repeated) and the Teacher copy (2 pages, with a beaming note). New drawing: `srhRaw` / `SrhStaff` (rows of q h hd w qd e er p p4 s4 r hr and boxes, an anacrusis offset, hearts, counts with + e a, boxes, ties, sound lines). Shared fixes: the drill's Korean answer line '정답: …' (was '정답은 1½박' with no copula, in every chapter); chapter 5's tap pad and tap levels stop a held note when the line ends and can no longer answer twice. Four fresh reviewers and a verifier; fixed: a match task with two right answers, a check-up answer that beamed wrongly, look-alike listening choices, overclaimed beaming entries, 'second line' unclear, the last bar called always short, a how-line that led to the wrong circle, syncopations across the middle, hold never scored, three different count-ins, answers that alternated, gap widths that gave the answer away, '1박' for beat 1, 온 마디, 혼자인, many Korean particles. Known compromise: count rows print about 3 mm between lines with boxes about 8 mm (a box under every half beat). Waiting for her combined review: the drill frame on phones, the drill nav's group title 'Compound time & rhythm patterns', the Workbook QR size. Checks: wbcheck work, teacher, spread and lesson PASS in English and Korean; lbcheck 0/0. |
"""
m = re.search(r'^\| 469 \| [^\n]*\n', s, re.M)
if not m: raise SystemExit('row 469')
s = s[:m.end()] + ROW + s[m.end():]
open(p, 'w', encoding='utf-8').write(s); print('CLAUDE.md: rules 8, 11, 15; log row 470')
