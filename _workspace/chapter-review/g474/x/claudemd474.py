#!/usr/bin/env python3
# Phase 474: CLAUDE.md: Book rules 8 (Korean words for chapter 19), 11 (key-signatures built; next signs), 15 (chapter 19
# waits for the combined review too); the log row.
import sys, re
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
def rep(a, b):
    global s
    if s.count(a) != 1: raise SystemExit('found %d: %s' % (s.count(a), a[:70]))
    s = s.replace(a, b)
rep("   kept on one line (no-break spaces). Skewer, not kebab",
    "   kept on one line (no-break spaces). Chapter 19: 조표 (written at the start of every line of music: 오선마다 맨 앞, never\n"
    "   줄마다, since 줄 is a staff line here), 임시표, 내추럴; keys G장조, F장조, D장조, B♭장조 (the app's way); a sign's place by\n"
    "   line or space: 맨 윗줄, 가운데 줄, 넷째 줄, 둘째 줄, 맨 아랫줄, 셋째 칸, 맨 위 칸, 맨 아래 칸; 'Both are F: the F line' = '둘\n"
    "   다 F 자리, F 줄이에요'; 이름이 같은 음 (every note of its letter); 조표대로, 다시 조표대로예요 (after the bar line);\n"
    "   G장조 음계를 쳐요; 엄지 밑으로 넣기, 3번 넘기기; chapter references as (16챕터); a sign never parts from the syllable after\n"
    "   it (a word joiner). Skewer, not kebab")
rep("   Phase 473): Level 3 is done. Next: Level 4 in PATH_STAGES order (key-signatures, signs, intervals, chords, composers,\n"
    "   melody); then Level 5.",
    "   Phase 473): Level 3 is done. Level 4: key-signatures (Phase 474). Next: signs, intervals, chords, composers, melody\n"
    "   (PATH_STAGES order); then Level 5.")
rep("   (dynamics), 12 (pitch-range), 13 (tempo), 14 (rhythm), 16 (scales), 17 (accidentals) and 18 (piano-story).",
    "   (dynamics), 12 (pitch-range), 13 (tempo), 14 (rhythm), 16 (scales), 17 (accidentals), 18 (piano-story) and 19\n"
    "   (key-signatures).")
ROW = """| 474 | 2026-10-17 | **Chapter 19, Key Signatures, built in full (her 09:17 '계속 가줘 최종검토는 한꺼번에하게'; Book rules 14 and 15). The first room of Level 4.** The level plan's scope: C, G and F major (AMEB Preliminary), then D and B♭ major (Grade 1); a key signature lasts the whole piece, an accidental one bar; all 15 keys, relative minors and the circle of fifths stay in the toolbox. The Lesson Book (7 pages, dictionary entries): the opener (a key signature is the sharps or flats just after the clef at the start of every line of music; a G major tune on two lines); the key signature (where it sits; its line or space; every octave); G major (one sharp, F♯: the top line, the bass staff's fourth line, 'the F line'); F major (one flat, B♭: the middle line, the bass staff's second line); key signature and accidental (the key signature the whole piece, an accidental and a natural until the bar line, then the key signature again); D major and B♭ major (two signs, always in order; naming the key by counting; a table of the five keys on both staves); My five checks. The screen lesson: the book with a pad on pages 2 to 6 (with and without the key signature; G and F major; the natural and its bar line; pick a key, its signature and scale). A 9-level drill (which key: C, G or F; which notes change; the coral note; key signature and accidental; all five keys; which is written right; listening, the key first; the bass staff; extra: A and E♭ major). The Workbook (pages 2 to 6 and the check-up, 11 marks; draw-the-key-signature staves at one size, about 5 mm) and the Teacher copy (AMEB and ABRSM placement; where the signs sit). Four reviewers (theory, Korean, design, code QA) and a verifier (67 of 72 held; the rest and the new points fixed). Kept for her combined review: book p6's ten small staves (about 3 mm: both clefs across one page), the AMEB 2026 wording (the reviewer read 2022), old drill bests and level links now pointing at the new levels, and old progress in earlier rebuilt chapters (this chapter ignores its old lesson ticks: storeAs k1 to k6, `skgOldStep`). Shared: every chapter's screen lesson ends with 'More in the toolbox' / '툴박스에 더 있어요' (`LessonMore`: its older tools, linked with the language; her 2026-10-16 22:21 question about things that seemed gone once the rooms were split by level); chapter 16's drill level 6 is 'Name the scale note' (it had taken note-values' Korean level name); the spread gives every page its own key; the older key-signature and scale tools say 샤프 (not 샵); old toolbox names now follow rule 8 (선율, 위로 한 걸음, 셈여림); the 'Easier after' line in Korean ends '. 아니면 여기서 계속해도 돼요.'; the chapter's grade tag Prelim–G1. printables.html: the chapter 19 card shows Workbook page 4 with new words. Waits for her combined review. |
"""
m = re.search(r'^\| 473 \| [^\n]*\n', s, re.M)
if not m: raise SystemExit('row 473')
s = s[:m.end()] + ROW + s[m.end():]
open(p, 'w', encoding='utf-8').write(s); print('CLAUDE.md: rules 8, 11, 15; log row 474')
