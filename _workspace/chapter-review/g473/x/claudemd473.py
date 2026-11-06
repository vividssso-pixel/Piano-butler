#!/usr/bin/env python3
# Phase 473: CLAUDE.md: Book rules 8 (Korean words for chapter 18), 11 (piano-story built; Level 3 done; next Level 4),
# 15 (chapter 18 waits for the combined review too); the log row.
import sys, re
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
def rep(a, b):
    global s
    if s.count(a) != 1: raise SystemExit('found %d: %s' % (s.count(a), a[:70]))
    s = s.replace(a, b)
rep("   붙임줄; C 자리; 그림의 음을 쳐요 (never 그림을 쳐요); direction first (위로 반 걸음); B♭으로 but F♯로.",
    "   붙임줄; C 자리; 그림의 음을 쳐요 (never 그림을 쳐요); direction first (위로 반 걸음); B♭으로 but F♯로. Chapter 18:\n"
    "   하프시코드 and 클라비코드 (쳄발로 not used); 깃촉 (a quill) 뜯어요; 탄젠트 (a brass piece, 놋쇠 조각) 밀어 올린 채 머물러요;\n"
    "   해머 (펠트를 씌운 작은 나무 망치) 쳐요; 현; the damper moves off: 댐퍼가 현에서 떨어져요 (never 들려요); 건반 악기;\n"
    "   the right pedal is 댐퍼 페달 in Korean (its other name 서스테인 페달) but the sustain pedal in English (its other name\n"
    "   the damper pedal): each language's usual name; 소프트 페달 (its other name 우나 코르다); 가운데 페달; 피아노포르테 =\n"
    "   '여리게-세게'; 크리스토포리, 피렌체, 1700년쯤; 그랜드 피아노, 업라이트 피아노, 88건반; 'ㄹ 수 있어요' and '양 끝'\n"
    "   kept on one line (no-break spaces).")
rep("   Phase 470), scales (Level 3, Phase 471), accidentals (Level 3, a new chapter, Phase 472). Next: Level 3's piano-story;\n"
    "   then Levels 4 and 5.",
    "   Phase 470), scales (Level 3, Phase 471), accidentals (Level 3, a new chapter, Phase 472), piano-story (Level 3,\n"
    "   Phase 473): Level 3 is done. Next: Level 4 in PATH_STAGES order (key-signatures, signs, intervals, chords, composers,\n"
    "   melody); then Level 5.")
rep("   (dynamics), 12 (pitch-range), 13 (tempo), 14 (rhythm), 16 (scales) and 17 (accidentals).",
    "   (dynamics), 12 (pitch-range), 13 (tempo), 14 (rhythm), 16 (scales), 17 (accidentals) and 18 (piano-story).")
ROW = """| 473 | 2026-10-14 | **Chapter 18, The Piano's Story, built in full (her 09:17 '계속 가줘 최종검토는 한꺼번에하게'; Book rules 14 and 15). The last room of Level 3, so Level 3 is done.** The Lesson Book (7 pages, dictionary entries, each with its drawing): the opener (the piano is a keyboard instrument whose hammers strike its strings; invented about 1700); before the piano (the harpsichord's quill plucks, the clavichord's brass tangent pushes up and stays; each drawn with its close-up); the first piano (Cristofori, an Italian instrument maker, Florence, about 1700; pianoforte, Italian for 'soft-loud'; a timeline from about 1400 to the 88 keys of the late 1800s); inside the piano (key, hammer, string, damper, drawn at rest); the pedals (sustain or damper, soft or una corda, middle on grands and uprights); grand and upright, the 88 keys and their two ends; My five checks. The screen lesson: the book with a pad on pages 2 to 6 (pluck, push or strike with a loudness meter; soft, loud and getting louder; hold a key: the hammer strikes and falls back, the damper stays off until you let go; the pedals, tapped on the drawing; the lowest A, middle C, the highest C and counting the Cs on the 88 keys in two rows), every pad stopping its sound when you leave it or another pad plays. A 9-level drill (quill, tangent or hammer; which instrument by ear; facts about the first piano; name the part; what each part does; which pedal; pedal or not by ear; grand or upright; extra: which came first or later), its text in either language at the moment it is shown and its answers placed evenly. The Workbook (pages 2 to 6 and the check-up; nothing copied from the facing page; no item answers another; the check-up 16 marks, never repeating a practice item) and the Teacher copy (the facts behind the book: the tangent, una corda on two of three strings, an upright's action, digital pianos; 'open the lid' for the lesson). Tasks that need an acoustic or 88-key piano say so. Four reviewers (history and pedagogy, Korean, design, code QA) and a verifier (71 of 74 held; the rest and 9 new points fixed). Kept for her combined review: 쳄발로 not used, the right pedal's main name differs by language (damper pedal in Korean, sustain pedal in English), old progress carries over (the same lesson id), and the series-wide cream background and small chrome targets. Shared: the Styles Workbook's page 5 (the style eras) now goes with The style eras in the toolbox (its code opens `?tool=eras`; `bkStepLabel` and `bkStepLink` know a 'tool ...' step), since The Piano's Story no longer has an eras step; the Styles map table still has no row for page 5 (as before). The chapter's older tools (keyboard ancestors, piano timeline, piano action, eras) stay in its toolbox after the five new pads. printables.html: the chapter 18 card shows Workbook page 4 (inside the piano) with new words; two alt texts lose a doubled 'the'. Waits for her combined review. |
"""
m = re.search(r'^\| 472 \| [^\n]*\n', s, re.M)
if not m: raise SystemExit('row 472')
s = s[:m.end()] + ROW + s[m.end():]
open(p, 'w', encoding='utf-8').write(s); print('CLAUDE.md: rules 8, 11, 15; log row 473')
