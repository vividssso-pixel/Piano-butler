#!/usr/bin/env python3
# Phases 442-443: CLAUDE.md -- rule 8 (the rabbit in two pictures; Clara without the title; the student is 'you'; no '--'),
# and the log rows.
import sys, re
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
def rep(a, b):
    global s
    if s.count(a) != 1: raise SystemExit('found %d: %s' % (s.count(a), a[:80]))
    s = s.replace(a, b)
rep("the King navy, the Queen coral, Princess Clara a pink pawn with a tiara",
    "the King navy, the Queen coral, Clara a pink pawn with a tiara (a princess -- said ONCE, where she first appears, 'Clara, a little princess'; never 'Princess Clara' / '클라라 공주', her 2026-10-12 16:02; she is a character the student meets, never the student: the student is always 'you', the week board says 'My week' / '나의 일주일' when no name is linked)")
rep("-- never as a full figure in a picture ('그냥 초상화에만 넣자');",
    "-- never as a full figure in a picture ('그냥 초상화에만 넣자'), except two: chapter 1's puppet (he holds the strings) and chapter 2's opener (he stands between the houses) -- her 2026-10-12 15:56 '이 두개 사진에 있던 토끼 돌려줘';")
rep("8. **Words and cast.**", "8. **Words and cast.** No double dash '--' in anything a reader sees (her 2026-10-12 16:07 '-- 이거 없애주고', then 'rewrite without dashes'): write it with a colon, a comma or a full stop -- new text from now on, the old text chapter by chapter.")
ROWS = """| 442 | 2026-10-12 | **The rabbit back in two pictures; rooms counted from the bottom; the door on every visit.** Her 15:56 (two screenshots: chapter 1's puppet, chapter 2's opener) '이 두개 사진에 있던 토끼 돌려줘'; 15:58 '순서가 아래 왼쪽부터 1 2 3 이렇게 되야 맞는거 아닌가? 그리고 처음들어올 때 문여는거 다시 웹페이지 로드했을 때 문열수있게'. patch442.py: (1) PB_ART.puppet is Phase 369's drawing again -- the rabbit holds the control bar, its string to the girl's head (from drills.src.html before Phase 425), the ground line navy; chapter 2's opener (FsCoverScene) has the rabbit on the ground between the houses again (Phase 420 had taken him out); guide heroes for chapters 1 and 2 re-exported. (2) townhouseSvg: a floor's first rooms sit on its LOWEST row, counted from the bottom left (1 2 3 below, 4 5 6 above; a short row goes on top), so you climb the house; the wide house (one row a floor) is unchanged; the phones' guide house redrawn. (3) The hall's door opens again every time the page loads: 'came in' is kept in memory (houseCameIn), not sessionStorage -- moving between chapters keeps the house open, a reload shows the door. Rule 8: the rabbit's two pictures. Checks: house443test 63/63 (house438 checks), v442 (door: hall -> house -> reload -> hall; rooms 1-3 below 4-6). |
| 443 | 2026-10-12 | **Clara, not Princess Clara; the student is 'you'.** Her 15:59 '공주는 너무 좀 오글거려서 ... 학생들이 들어오면 제 3자가 되는거잖아?', 16:01 (a pawn: ordinary to special), 16:02 '공주인데 프린세스 클라라 라고 계속 안해도 되는거정도로 하자', 16:05 '응' to: Clara is a character the student meets (like the Dog and Grandma), never the student. patch443.py: 'Princess Clara' -> 'Clara' (35 in the app and books), '클라라 공주' -> '클라라' (19) and her bare '공주' -> '클라라' (16; Scarlatti's Portuguese princess stays); said once where she first appears, the Musical Alphabet's page 5: 'In the small house lives Clara, a little princess, at the left door (C)' / '꼬마 공주 클라라(Clara)'; the tiara and 'Clara belongs to the royal family' stay. The week board without a linked name: 'My week' / '나의 일주일' (was 'Clara's week'). Guide pages (note-names, staff, ledger-lines) and printables.html the same; rebuilt --final. Rule 8 updated. Checks: ch1app376 21, ch2app395 21, ch3app397 35, sf405 22, ll431 24, ws419 45, nosong399 24, tn441 16, house443 63 -- all pass. |
"""
m = re.search(r'^\| 441 \| [^\n]*\n', s, re.M)
if not m: raise SystemExit('row 441')
s = s[:m.end()] + ROWS + s[m.end():]
open(p, 'w', encoding='utf-8').write(s); print('CLAUDE.md: rule 8, log rows 442-443')
