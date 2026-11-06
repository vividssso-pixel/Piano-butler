#!/usr/bin/env python3
# Phases 420-421 in CLAUDE.md: the royals become crowns (rule 8 follows), and the Victorian sample (not applied).
#   python3 claudemd421.py CLAUDE.md      (after claudemd420.py, which adds rows 418-419)
import sys
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
def rep(a, b, what):
    global s
    if s.count(a) != 1: raise SystemExit(what + ': expected 1, got %d' % s.count(a))
    s = s.replace(a, b)
rep("""   treble staff is Queensland and the bass staff Kingsland from chapter 5; the cast is King A, Queen A (drop earrings),
   Clara A (braids and tiara); only the characters are hand-drawn, frames and props are straight; no songs inside the""",
    """   treble staff is Queensland and the bass staff Kingsland from chapter 5; the royals are SIGNS, like chess pieces, never
   faces (Phase 420: '체스처럼 저렇게 하는게 좀 더 깔끔한 듯. 상상력도 주고'): the King's crown (navy, a cross, three jewels),
   the Queen's crown (coral, five points with pearls), Princess Clara's tiara; the King's dragon and cows are words only;
   the rabbit butler appears only in the REMEMBER band; frames and props are straight; no songs inside the""", 'rule 8')
ROWS = """| 420 | 2026-10-10 | **The royals are crowns, not faces (her 'samples first', then '응 전체 다 바꾸자 -- 체스처럼 저렇게 하는게 좀 더 깔끔한 듯. 상상력도 주고').** patch420.py: sfQueen/sfKing/sfClara now draw the Queen's crown (coral, five points with pearls, jewelled band), the King's crown (navy, cross, three coral jewels on a pearl band) and Clara's tiara, each in the box the face used (the old faces kept as sfQueenFace/sfKingFace/sfClaraFace, unused) -- so chapters 3-5, the books, the Workbooks, the app and the check rows all follow; nnClara = the tiara. Chapter 5: the dragon and cow drawings went (wsDragon/wsCow removed; the sayings keep them in words), page 4's King's crown sits by his spaces as the Queen's by hers, the check row shows his crown. Labels say crowns (ch4 p1, ch5 p1). Chapter 2's opener without the rabbit (he stays in the REMEMBER band). Guide pages: svgs re-exported (first-steps/hero, note-names/who-lives -- it still had the pre-405 Clara --, staff/hero, kings-five, queens-five, same-key), the chapter 3 worksheet and its printables card recaptured (the tiara on C); guide pages rebuilt --final. Checks: ws419test 45/45, ch1 21/21, ch2 21/21, ch3 35/35, sf405 22/22, no-song 24/24, house 34/34, every Lesson Book en/ko 0 overflow. Sample shown first: Claude outputs/Crowns-only-sample.pdf. Still to ask her: the house-map rabbit ('Your butler opens the door', guide front page) and chapter 3's resident icons (Dog, Grandma, Apple garden, doors). |
| 421 | 2026-10-10 | **SAMPLE ONLY, not applied: the books in a Victorian, minimal dress** (her 08:15: '전체 빅토리안 스타일로 가는것도 샘플 ... 체크하는 곳에는 초록색 ... 미니멀함을 유지하되 ... 모던함'). _workspace/chapter-review/g421/x/vic_sample.py on a copy of drills.src.html: a hairline page frame with cut-in corners and the page number on its bottom line; running heads in spaced capitals over a thick-and-thin rule; titles centred over a small diamond ornament; subheads and numbers in Playfair italic; a drop capital and dotted leaders on the openers; picture boxes with square corners and a fine inner line; Workbook labels with pointed ends; double rules on PLAY, REMEMBER and the five checks. Colour by job: navy = ink, coral = the point (the example, the key word, YOUR TURN), GREEN #2e8a6e = the check (tick boxes, Got it!, Checked, the Teacher copy's answers). White paper and Inter for reading kept. All books of chapters 1-5 0 overflow with it. Claude outputs/Victorian-sample-v1.pdf (cover + 8 now/Victorian sheets). Waiting for her choice; if yes, it becomes a real patch (shared parts + every opener as one component) and the app's lesson screens follow. |
"""
i = s.index('| 419 | 2026-10-10 |'); j = s.index('\n', i) + 1
if '| 420 | 2026-10-10 |' in s: raise SystemExit('rows exist')
s = s[:j] + ROWS + s[j:]
open(p, 'w', encoding='utf-8').write(s); print('rule 8 + rows 420-421 ok')
