#!/usr/bin/env python3
# Phase 462: CLAUDE.md: Book rules 14 (like a dictionary) and 15 (recommendations by default, strict reviewers, her final
# review item by item); rule 13 (legato and the slur); rule 9 (the openers' diamond, the tapped key); rule 11; the log row.
import sys, re
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
def rep(a, b):
    global s
    if s.count(a) != 1: raise SystemExit('found %d: %s' % (s.count(a), a[:70]))
    s = s.replace(a, b)
rep("Next: Level 2's time-signatures (draft v1, Phase 461, waiting for her answers to B1-B12 and G1-G3),",
    "Next: Level 2's time-signatures (draft v1 in Phase 461; all as recommended, her 2026-10-13 23:51, built in full under rule 15),")
rep("   grand piano waits for a concert room of its own.\n10. **The path in five levels**",
    "   grand piano waits for a concert room of its own. The openers' two lists ('In this chapter', 'By the end, you can') mark\n"
    "   each row with a small coral diamond inside a navy one (`bkGoal`), never a tick box (her 2026-10-13 23:57: a box looks\n"
    "   like something to tick; Phase 462). On a keyboard, a tapped key is solid coral, the keys that go with it pale coral\n"
    "   inside one navy outline, the rest plain white; green only ever means 'correct' (her 23:56 on 'Whose house is this?').\n"
    "10. **The path in five levels**")
rep("   정하자').\n\n## Verified Piece Counts (2026 Syllabus)", """   정하자'). Legato and the slur (her 2026-10-13 23:56 '레가토를 공식적으로 설명해야할 것 같은데 어디서? 그리고 슬러는?'):
   legato, the touch, is defined where the student first plays notes one after another, chapter 2's 'Play on the
   patterns' (one dictionary line; the relay baton stays its REMEMBER), since legato is the default touch from day one
   (her 2026-09-28 '레가토 개념 기본으로 깔고 가져가거든, 좀 나중에 스타카토'); the slur, legato's sign, comes in chapter 10
   (dynamics and articulation) with staccato, after chapter 9 because a slur joins different notes, set beside chapter
   8's tie: the same curve, on the same note a tie, on different notes a slur. Chapter 8 teaches the tie only.
14. **Like a dictionary** (her 2026-10-13 23:51 '모든 설명을 사전처럼 깔끔하게. 군더더기 없이'). Every explanation reads like
   a dictionary entry: the term in bold first, then what it is in one short sentence; a page with several terms lists
   them as entries, one under another (`LbDefs`: **bar line** A line that divides the music into bars.). After the
   definition, at most one more fact a sentence: how long, where it sits, how to play it, its other name ('Its other
   name is a measure.'). No story, no warm-up, no 'let's', nothing the picture already shows. Tasks stay set tasks
   (rule 3). From chapter 8 on, then the finished books, chapter by chapter.
15. **Recommendations by default; strict reviewers; her final review item by item** (her 2026-10-13 23:51 '지금부터
   추천대로 다 가줘, 검토자 몇명이 까다롭게 나 대신 검수해서 레슨하기 쉽게 다 만들고 내가 최종 하나씩 검토할 수 있게 해줘').
   No more drafts that wait for her answers: each chapter is built in full (the Lesson Book, its screen lesson, the
   drill, the Workbook, the Teacher copy) with the recommendations. Then several fresh reviewers who did not make it
   check it hard, each from one side: easy to teach; the theory right against AMEB and ABRSM; easy for a child to read
   (rules 7, 8, 14); print and screen (fit, clipping, overlap, both languages). Every valid point is fixed, and only then
   does she see it: the final review page shows the chapter one item at a time, and she marks each OK or Change with a
   note. The G questions (what only her classroom knows) get my best guess, marked for that review. Still hers to
   decide: strategy, money, anything sent outside, deleting, AdSense.

## Verified Piece Counts (2026 Syllabus)""")
ROW = """| 462 | 2026-10-13 | **Two fixes she asked for, and the new way of working.** Her 23:56: on 'Whose house is this?' (chapter 2, page 3 on screen) the tapped key (green) and its housemates (coral borders on the coral house tint) ran together. Now the tapped key is solid coral, its housemates pale coral with thin borders, one navy outline round the house, the other keys plain white while a house is lit (TapKeyboard: marks 'pick' and 'mate' with their own stroke width, an `outline` prop). Her 23:57: the openers' lists looked like tick boxes to fill; every opener (nine books) now marks its rows with `bkGoal`, a coral diamond inside a navy one, the openers' chequered diamond in small. Book rules: 9 (both), 13 (legato in chapter 2, the slur in chapter 10 beside the tie, her 23:56 question), 14 (like a dictionary, her 23:51), 15 (recommendations by default, strict reviewers, her final review item by item, her 23:51). Work kit backed up to _workspace/kit-backup. |
"""
m = re.search(r'^\| 461 \| [^\n]*\n', s, re.M)
if not m: raise SystemExit('row 461')
s = s[:m.end()] + ROW + s[m.end():]
open(p, 'w', encoding='utf-8').write(s); print('CLAUDE.md: rules 9, 11, 13, 14, 15; log row 462')
