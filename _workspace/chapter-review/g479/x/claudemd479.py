#!/usr/bin/env python3
# Phase 479: CLAUDE.md: rule 10 (the map's new Level 4 and 5), rule 11 (terms built in the macro-first frame; the new
# order), rule 15 (23 waits for the combined review), the log row.
import sys, re
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
def one(a, b):
    global s
    if s.count(a) != 1: raise SystemExit('not found once: ' + a[:60])
    s = s.replace(a, b)
# rule 10: the order inside Levels 4 and 5 (her 2026-10-17 09:42)
one("   chapter number moves when it comes). Free order inside a\n",
    "   chapter number moves when it comes). Phase 479 (her 2026-10-17 09:42 '음악 용어 먼저 … 그다음 음악 형식 선율과 프레이즈'):\n"
    "   Level 4 is key-signatures, signs, intervals, chords, terms (23), form (24); Level 5 is melody (25), composers (26),\n"
    "   styles (27), more-scales; composers and styles will be built together on one timeline. Free order inside a\n")
one("Level 4: key-signatures (Phase 474), signs (Phase 475), intervals (Phase 477), chords (Phase 478). Next",
    "Level 4: key-signatures (Phase 474), signs (Phase 475), intervals (Phase 477), chords (Phase 478), terms (Phase 479). Next")
m = re.search(r"Next composers, melody;\s+then Level 5\.", s)
if not m: raise SystemExit('rule 11 tail')
s = s[:m.start()] + ("Phase 479 built terms (23) the same way: page 1 is the\n"
    "   expression ladder (every word on one map by family: speed slow to fast, changing speed as rows of beats, loud and\n"
    "   soft under a widening wedge, touch and character, the little words); the screen lesson ends with it again, the\n"
    "   student ticking the words they know; Workbook page 7 is a term hunt in any piece. Next form (24), then Level 5:\n"
    "   melody (25), composers and styles on one timeline (26, 27), more scales. The big-map first pages for chapters 1-18\n"
    "   come after her combined review.") + s[m.end():]
one("(key-signatures), 20 (signs), 21 (intervals) and 22 (chords).", "(key-signatures), 20 (signs), 21 (intervals), 22 (chords) and 23 (terms).")
ROW = """| 479 | 2026-10-17 | **Chapter 23, Musical Terms, built in full in the macro-first frame, and the map's new order (her 09:42 '음악 용어 먼저 만들어주고 그다음 음악 형식 선율과 프레이즈 이 순서로 가자').** `PATH_STAGES`: Level 4 key-signatures, signs, intervals, chords, terms, form; Level 5 melody, composers, styles, more-scales (so terms 23, form 24, melody 25, composers 26, styles 27); `ROOM_AFTER.form` is signs and reading-steps (not melody). The chapter replaces the 2025 one (Phase 117). **Lesson Book** (tmbook479.jsx; patch479.py wires it): p1 the expression ladder (speed words on an arrow slow to fast; accel., rit. · rall., riten., a tempo as rows of beats; pp to ff under a widening wedge, the hairpins and sf; touch and character; the little words); p2 the speed ladder standing up (Largo 46 … Prestissimo 208, ♩ = about); p3 changing speed (five rows of beats at one scale; a tempo is the first speed, held back, the first speed again); p4 loud and soft (mp, ff, cresc./decresc., sf as one coral note); p5 touch and character (C D E F legato, staccato, mezzo staccato: the marks the only change; sostenuto, cantabile, leggiero, maestoso, espressivo); p6 little words (molto, poco, sempre, senza, più, meno, con; eight combinations); p7 My five checks. Data `TMX` (word as printed, English and Korean meaning, Korean reading, AMEB grade); speed words upright bold, dynamics bold italic, the rest italic. Korean: 빠르기말, 셈여림, 터치와 느낌, 꾸며 주는 말 (not 작은 말), Lento 아주 느리게, riten. 곧바로 느리게, sf 그 음만 특히 세게, con ~와 함께, espressivo 표정 있게. **Screen lesson** pads: the map (a word's card opens under its family), the speed ladder (fast at the top), changing speed, loud and soft (hairpins on the buttons), touch, little words; the extra end step 'My terms' ticks the words the student knows (`pb_terms_known_v1`). **Drill** 9 levels: speed words, which is faster (35 pairs, two rungs apart), changing speed, loud and soft, listening (accel./rit., legato/staccato, cresc./decresc., Adagio/Presto, sf/cresc., a tempo/riten.; screen only), touch and character, little words, build the term, extra: meaning → term; wrong answers never synonyms (Largo/Lento/Adagio, Allegro/Vivace, Presto/Prestissimo, rall./rit.) and never the same Korean. **Workbook** p2–p6, p7 a term hunt in any piece (ALL YEAR grid of the 39 words), p8 check-up (12 marks); **Teacher copy** 2 pages (AMEB Music Craft 2022 placement). Toolbox: tmx-map, tmx-speed, tmx-change, tmx-vol, tmx-touch, tmx-build, then the older term tools; the chapter tagged Prelim–G2. Shared changes: `playTerm` gains `h.back` (a tempo, also in the toolbox's TERMS); chapter 10's `sdyMarks` puts a slur clear of staccato dots on the same note (mezzo staccato; chapters 10 and 13 pixel-identical); `STEPS_TOTAL_NOW.terms = 6`, `STEP_EXTRA.terms = 'k7'`, the old lesson's ticks ignored. printables.html: the chapter 23 card's words, and the topic numbers of terms, form, melody and composers (the card image waits for her combined review). Reviewed by four strict reviewers (theory 19, Korean 26, design 25, code 12 findings; 1 blocker, all fixed) and a verifier (8 more, all fixed). For her: 꾸며 주는 말 for the little words; the older Term cards' Korean wording (riten., sf). Waits for her combined review. |
"""
m = re.search(r'^\| 478 \| [^\n]*\n', s, re.M)
if not m: raise SystemExit('row 478')
s = s[:m.end()] + ROW + s[m.end():]
open(p, 'w', encoding='utf-8').write(s); print('CLAUDE.md: rules 10, 11, 15; log row 479')
