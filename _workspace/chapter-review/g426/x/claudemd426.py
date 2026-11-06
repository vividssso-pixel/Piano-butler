#!/usr/bin/env python3
# Phase 426 in CLAUDE.md: Book rule 9 now names the townhouse as the chapter map (and the week board), and the Phase row.
#   python3 claudemd426.py <CLAUDE.md>
import sys
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
def rep(a, b):
    global s
    if s.count(a) != 1: raise SystemExit('CLAUDE.md: %r found %d' % (a[:70], s.count(a)))
    s = s.replace(a, b)
rep("9. **The Victorian look** (Phases 424-425, her decisions of 2026-10-10).", "9. **The Victorian look** (Phases 424-426, her decisions of 2026-10-10).")
rep("""The chapter map is a STREET of classical buildings
   drawn in lines (Lodge, Library, Clock Tower, Conservatory, Academy, Theatre, Museum -- one a stage, each window a
   chapter: '단순하지만 그 쉐입으로 조금 클래식함을'), with 'Clara's journey' (the chapters as chess squares) to show
   where you are; no colour on the buildings.""",
"""The chapter map is the TOWNHOUSE (Phase 426;
   her 17:30 '좋다 이렇게 정하자' after a street, a village, a château garden and a classical plan): one tall house cut
   open like a doll's house -- the hall at the foot (the fox's portrait, a pedimented front door), a floor per stage, a
   room per chapter, every floor with its own wallpaper, floor and lamp (lamps lit coral with a soft glow), NO STAIRS
   ('계단 빼고 층층이'); quoins, dentil cornices, panelled wainscot, each chapter's picture in a cut-in-corner frame
   hung on cords; a mansard in chequered slates, a pedimented dormer 'Piano Butler', two turrets with the King on the
   LEFT and the Queen on the RIGHT. Classical letters on the map: Cinzel capitals for floors, Cormorant Garamond for
   rooms (Inter and plain icons 'had no classicism'). The map opens on the hall; the door swings open and the house
   rises above the hall, anchored at the bottom; for the rest of the session the house shows straight away. Above it
   the WEEK BOARD: five practice days take the pawn (Clara, or the linked student's own) across the board to become a
   queen. The Workbook colours in the wide house (one row of rooms per floor); the guides' front page shows it too.""")
row = """| 426 | 2026-10-10 | **The chapter map is a townhouse; the week board.** Her afternoon, 13:00-17:30: the street became a village of buildings that grow when tapped (14:11 '마을형식 ... 누르면 크게 커지는 방식'), the chessboard became 'Clara's week' (14:22-14:30), a picture map with silhouettes, Victorian trees and lamps, left to right (14:31-14:42), a château garden round a fountain (14:51-14:56), a 3x3 classical plan (16:48), then, between a two-row street and a single house, 'A · The townhouse, close up' (17:10 '이게 더 나은듯 ... 클래식함 가미'), every floor dressed differently like a doll's house (17:08), the hall first and the house rising from its door, the King left and the Queen right (17:17), no stairs, classical letters and icons (17:22), '좋다 이렇게 정하자' (17:30). patch425.js (rerun) + street425.jsx: townhouseSvg (narrow: rooms in rows of up to three; wide: every floor in one row; print: no glow, no buttons), HouseMap (the hall with the door as a button; data-layout hall/house; sessionStorage pb_house_in_v1; the leaves swing, the house rises with a clip-path, the hall stays put; reduced motion: at once; your room framed coral with Clara in it; your floor's name coral), the WEEK BOARD (weekSvg: practice days from check-ins, drill history and lesson steps -- saveDone now marks pb_practice_days_v1; the pawn climbs the e-file, two squares on the week's first day, a queen at five; last weeks beside it; Clara by default, a navy pawn named for a linked student), the Workbook's front pages: ONE page with the wide house to colour in (was two street pages), the chapter-map table in Cinzel/Cormorant; the street's seven buildings, the village and the samples removed by a reachability pass (kit/prune428.js). Fonts: Cinzel and Cormorant Garamond added to the drills Google Fonts link; rdWidth measures any font. Guide: the front page is the house (house428gen.js, houseimg428.js; build.py loads the classical letters and Playfair italics, .house-wide held to 680px), words street -> house, every guide page rebuilt --final. A fresh-eyes reviewer (an agent that had not seen the work) -> fixed: the hall's crop, white slabs between floors, the mansard ends under the turrets, Clara clear of the frame, seven different lamps and wallpapers, bigger navy room names (the tick drops when a name would not fit), floor names in full capitals sized to the measured text, no slanted Hangul, no START line on paper, a1 dark on the week board, the sharing picture centred. Kept on purpose (her standing decisions): the coral Queen and bow tie, odd numbers on dark chess squares. Checks: house428test 72/72 (new; street425test retired), ws419 45/45, ch1 21/21, ch2 21/21, ch3 35/35, sf405 22/22, no-song 24/24, lbcheck/wbcheck chapters 1-5 + front matter 0 overflow en/ko, spreads unchanged, picfit clean en/ko. Not done: the printables cards of chapters 6-26 still show the old page head; chapter 5's 'crown check' wording still to ask. |
"""
i = s.index('| 425 | 2026-10-10 |'); j = s.index('\n', i) + 1
s = s[:j] + row + s[j:]
open(p, 'w', encoding='utf-8').write(s); print('CLAUDE.md ok')
