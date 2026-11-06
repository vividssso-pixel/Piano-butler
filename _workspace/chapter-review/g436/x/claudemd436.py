#!/usr/bin/env python3
# Phase 436: CLAUDE.md -- the house has a floor per level; book rule 10, the path in five levels.
import sys, re
ROW = '| 436 | 2026-10-12 | **The path in five levels, and every box centred.** Her 11:43 \'첫레슨이라도 하지말고 다른 그냥 층을 나타낼까? 그리고 층에 나오는 글자는 가운데로 맞추는게 맞을 것 같아\' -- three plaque versions shown (LEVEL 2 / 2단계, SECOND FLOOR / 2층, II) -- then 12:08 \'좋아 너 의견에 맞춰가자 그리고 전체적으로 박스가 있거나하는건 다 가운데 정렬 해서 보기 좋게 발란스 맞추자\': "LEVEL n" in English, "n층" in Korean, plan C1-C10 as recommended. App: PATH_STAGES = five levels by chapter id (g435 plan levels.json), numbered 1-26 (Accidentals, room 17, waits off the map until its chapter exists). The house: plaques centred, coral on your floor and green once every room on it is done (the plaque\'s chess square is gone); each room\'s number and name centred over its picture; one name size and one picture height per floor (a floor with a two-line name is one line taller); the done ticks on all done rooms of a floor or none; a name may break after a middle dot (걸음·건너뛰기); the hall\'s words centred opposite the portrait; footer \'Start · floor by floor, any room first\' / \'출발 · 한 층씩, 방은 마음대로\'. CH_SHORT: Tones & semitones / 온음과 반음, 걸음·건너뛰기. Start guide and the end of a chapter speak of levels (\'That was the last room on Level 1. Next floor: Level 2.\', \'Level 2 of 5\'). A chapter opened early says \'Easier after 6 · Reading the Staff and 8 · Time Signatures -- or carry on here.\' (ROOM_AFTER; a teacher sees \'Builds on ...\'). The books\' small house: LEVEL rows, every room centred in its cell, one size per row. The Workbook\'s house page: \'numbered 1 to 26\', any room first on a floor. The finished books take chapter numbers from bkChapterNo (Musical Alphabet 4, Reading the Staff 6, The Whole Staff 7, Ledger Lines 15; Tones 11). Guides: kickers and crumbs (1, 2, 4, 6, 15 of 26 · Level 1 or 3), the front page\'s lead and room numbers, its house and sharing picture redrawn; tools/lessons/README. Chapter 7 draft: tn436.jsx counts \'Chapter 3\'s steps\' from the path. Book rule 10 added. Checks: house436test at 390/320/1024 en, 390/1440 ko all pass; house428 (plaque count adjusted) 72/72, ll431 24/24, ll429 82/82, ws419 45/45, ch1app376 21/21, ch2app395 21/21, ch3app397 35/35, sf405 22/22, nosong399 24/24, frame430 0 out of box; lbcheck the same as Phase 433; wbcheck no overflow (front and the six books). |\n'
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
s2, n = re.subn(r'a floor per stage, a(\s+)room per chapter', r'a floor per level, a\1room per chapter', s)
if n != 1: raise SystemExit('floor per stage: %d' % n)
a = "   grand piano waits for a concert room of its own.\n"
if s2.count(a) != 1: raise SystemExit('rule 9 end')
s2 = s2.replace(a, a + """10. **The path in five levels** (Phase 436; the level plan of Phase 435, her '좋아. 그렇게 해보자' and '너 의견에 맞춰가자',
   2026-10-11/12). The house has five floors: LEVEL 1-5 on the plaques, 'n층' in Korean, no floor names ('첫레슨이라도
   하지말고 ... 그냥 층'). `PATH_STAGES` lists each level's chapter ids; the chapters are numbered 1 to 26 in that order
   (27 once Accidentals, room 17 on Level 3, has its chapter; until then it stays off the map). Free order inside a
   floor; the rooms a chapter is easier after (`ROOM_AFTER`) are one gentle line at its top, never a lock. The books never
   type a chapter number: they use `bkChapterNo(id)`. Everything in a box is centred ('박스가 있거나 하는 건 다 가운데
   정렬'): the floor plaques, each room's number and name over its picture, the hall's words; one name size and one
   picture height on each floor.
""")
import re as _re
m = _re.search(r'^\| 435 \| [^\n]*\n', s2, _re.M)
if not m: raise SystemExit('row 435')
s2 = s2[:m.end()] + ROW + s2[m.end():]
open(p, 'w', encoding='utf-8').write(s2); print('CLAUDE.md: floor per level, rule 10, log row 436')
