#!/usr/bin/env python3
# Phase 471: CLAUDE.md: Book rules 8 (Korean words for chapter 16), 11 (scales built; next accidentals), 15 (chapter 16
# waits for the combined review too); the log row.
import sys, re
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
def rep(a, b):
    global s
    if s.count(a) != 1: raise SystemExit('found %d: %s' % (s.count(a), a[:70]))
    s = s.replace(a, b)
rep("   패턴 stays (리듬꼴 is the school-book word, offered once).",
    "   패턴 stays (리듬꼴 is the school-book word, offered once). Chapter 16: 음계 (its other name 스케일; the chapter name\n"
    "   stays 스케일), 장음계, 온 걸음 / 반 걸음 as in chapter 11, 음계의 손가락 번호 (its other name 운지), 엄지 밑으로 넣기,\n"
    "   3번 넘기기 and 4번 넘기기, 음의 번호 (its other name 음도), 으뜸음 (음계의 집 같은 음), 화성단음계; ♯ is read 샤프, so\n"
    "   F♯를 / F♯와 but B♭을 / B♭과; 2와, 4와, 5와 but 1과, 3과, 6과, 7과.")
rep("   ledger-lines (Level 3, written early), tempo (Level 3, built in full in Phase 469 under rule 15), rhythm (Level 3,\n   Phase 470). Next: Level 3's scales, accidentals (a new chapter), piano-story; then Levels 4 and 5.",
    "   ledger-lines (Level 3, written early), tempo (Level 3, built in full in Phase 469 under rule 15), rhythm (Level 3,\n   Phase 470), scales (Level 3, Phase 471). Next: Level 3's accidentals (a new chapter), piano-story; then Levels 4 and 5.")
rep("   (dynamics), 12 (pitch-range), 13 (tempo) and 14 (rhythm).", "   (dynamics), 12 (pitch-range), 13 (tempo), 14 (rhythm) and 16 (scales).")
ROW = """| 471 | 2026-10-14 | **Chapter 16, Scales, built in full (her 09:17 '계속 가줘 최종검토는 한꺼번에하게'; Book rules 14 and 15). The third room of Level 3.** C, G and F major, one octave, hands separately. The Lesson Book (7 pages, dictionary entries): the opener (a scale is notes in order, step by step, up or down, from one note to the same letter an octave away; C major on the staff, each note over its numbered key); the major scale (eight notes: seven letters, then the first again; whole whole half whole whole whole half; T T S T T T S); C major fingering (thumb under, 3 over; straight arrows); scale degrees (1 to 8; tonic = the scale's home note); G major (F♯; 'each letter once': F♯ never G♭); F major (B♭ never A♯; right hand 1 2 3 4, 1 2 3 4; 4 over); My five checks. Steps drawn as straight brackets (rule 8), words on a second row where two would touch; ♯ and ♭ in running text set in the music font (Korean had a full-width gap). The screen lesson: the book with a listen-and-tap keyboard on pages 2 to 6 (a new Listen stops the pad that is sounding); its lesson id is now 'scales' like every chapter's (chapterSteps skips the old scales-major / scales-minor ticks). A 9-level drill (whole or half, where is the half step, build the scale with no names shown, which finger, which degree, name the note (incl. F♯ vs G♭), listening; extra: D and B♭ major both ways round, the harmonic minors' raised 7th). The Workbook (pages 2 to 6 and the check-up on paper; nothing on a page gives away another task; the check-up repeats no practice item) and the Teacher copy (13 marks; AMEB technical work placement from the app's own Scale finder data: C and G major and A harmonic minor Preliminary, F major and E and D harmonic minor Grade 1, B♭ major Grade 2, for her to confirm). Four reviewers (theory, Korean, design, code QA) and a verifier; every finding fixed except the series-wide ones, kept for her combined review (drill frame on phones, the TRY IT badge in Korean, the nav group name 'Scales & Keys', shared Korean strings). Shared: the REMEMBER label never wraps; kit/wbcheck.js measures the PLAY box's empty space again (it had looked for the old dashed box). printables.html: the chapter 16 card shows Workbook page 4. Waits for her combined review. |
"""
m = re.search(r'^\| 470 \| [^\n]*\n', s, re.M)
if not m: raise SystemExit('row 470')
s = s[:m.end()] + ROW + s[m.end():]
open(p, 'w', encoding='utf-8').write(s); print('CLAUDE.md: rules 8, 11, 15; log row 471')
