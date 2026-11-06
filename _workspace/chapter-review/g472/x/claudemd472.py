#!/usr/bin/env python3
# Phase 472: CLAUDE.md: Book rules 8 (Korean words for chapter 17), 10 (27 chapters: Accidentals joined the map),
# 11 (accidentals built; next piano-story), 15 (chapter 17 waits for the combined review too); the log row.
import sys, re
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
def rep(a, b):
    global s
    if s.count(a) != 1: raise SystemExit('found %d: %s' % (s.count(a), a[:70]))
    s = s.replace(a, b)
rep("   F♯를 / F♯와 but B♭을 / B♭과; 2와, 4와, 5와 but 1과, 3과, 6과, 7과.",
    "   F♯를 / F♯와 but B♭을 / B♭과; 2와, 4와, 5와 but 1과, 3과, 6과, 7과. Chapter 17: 임시표; 샤프 (its other name 올림표),\n"
    "   플랫 (내림표), 내추럴 (제자리표); 세로줄; a sign 'has effect' to the bar line (세로줄까지 효과가 있어요, never 이어져요);\n"
    "   'starts plain' is 임시표 없이 시작해요 (원래 음 only for the natural's note); 같은 마디라 그대로예요 for a held note;\n"
    "   붙임줄; C 자리; 그림의 음을 쳐요 (never 그림을 쳐요); direction first (위로 반 걸음); B♭으로 but F♯로.")
rep("   하지말고 ... 그냥 층'). `PATH_STAGES` lists each level's chapter ids; the chapters are numbered 1 to 26 in that order\n"
    "   (27 once Accidentals, room 17 on Level 3, has its chapter; until then it stays off the map; likewise More Scales,\n"
    "   `more-scales`, the last room on Level 5 after Styles, so no chapter number moves when it comes).",
    "   하지말고 ... 그냥 층'). `PATH_STAGES` lists each level's chapter ids; the chapters are numbered 1 to 27 in that order\n"
    "   (Accidentals, room 17 on Level 3, joined the map with its chapter in Phase 472, and every chapter after it moved up one;\n"
    "   More Scales, `more-scales`, the last room on Level 5 after Styles, stays off the map until it has its chapter, so no\n"
    "   chapter number moves when it comes).")
rep("   Phase 470), scales (Level 3, Phase 471). Next: Level 3's accidentals (a new chapter), piano-story; then Levels 4 and 5.",
    "   Phase 470), scales (Level 3, Phase 471), accidentals (Level 3, a new chapter, Phase 472). Next: Level 3's piano-story;\n"
    "   then Levels 4 and 5.")
rep("   (dynamics), 12 (pitch-range), 13 (tempo), 14 (rhythm) and 16 (scales).", "   (dynamics), 12 (pitch-range), 13 (tempo), 14 (rhythm), 16 (scales) and 17 (accidentals).")
ROW = """| 472 | 2026-10-14 | **Chapter 17, Accidentals, a new chapter, built in full (her 09:17 '계속 가줘 최종검토는 한꺼번에하게'; Book rules 14 and 15). The fourth room of Level 3; it joins the map, so The Piano's Story is now 18 and every chapter after it moves up one (printables.html renumbered the same way).** The Lesson Book (7 pages, dictionary entries): the opener (an accidental is a sharp, flat or natural just before a note; it lasts until the bar line); sharp and flat (the next key up or down: a half step; just before the note, on its line or space); the natural (cancels: the plain note again); until the bar line (every later note on its line or space in that bar; after the bar line the note is plain again, a tied note keeps its sign); its own line or space (an F an octave away stays F); reading a tune (find the signs, find the bar lines, then play; C position); My five checks. One staff size on every page, each picture with its keys. The screen lesson: the book with a listen-and-tap pad on pages 2 to 6 (a new Listen stops the pad that is sounding, and its notes stop at once). A 9-level drill (name the sign, find the key, the natural, until the bar line, its own line or space, read the bar, which sign? (no sign or the same sign again both right when it still holds), listening; extra: the bass clef), its answers never given away by the coral note's place, the number of buttons or the number of signs; on a phone the two-bar tunes one bar a row. The Workbook (pages 2 to 6 and the check-up on paper; nothing copied from the facing page; the check-up repeats no practice item) and the Teacher copy (12 marks; AMEB Preliminary reads sharps and flats, Grade 1 adds the natural). Four reviewers (theory, Korean, design, code QA) and a verifier; every finding fixed except the series-wide ones, kept for her combined review (the app header shows the Toolbox group 'Tones & semitones', cream background, TRY IT badge in Korean, shared Korean strings, the drop capital). Chapter 11's two older accidental tools stay in chapter 11's toolbox; their bar-line line no longer says the bar line 'wipes it clean'. Shared: chapter 11's keyboard can ring every white key too (`wslots`, opt-in); chapter 16's pads release their stop function like this chapter's. teacher-dashboard.html: Accidentals in the 'For the student' list. printables.html: the chapter 17 Workbook card (page 4), 26 worksheet pages. Waits for her combined review. |
"""
m = re.search(r'^\| 471 \| [^\n]*\n', s, re.M)
if not m: raise SystemExit('row 471')
s = s[:m.end()] + ROW + s[m.end():]
open(p, 'w', encoding='utf-8').write(s); print('CLAUDE.md: rules 8, 10, 11, 15; log row 472')
