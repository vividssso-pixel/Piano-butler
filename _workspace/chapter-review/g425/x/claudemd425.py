#!/usr/bin/env python3
# Phase 424-425 in CLAUDE.md: Book rule 8 follows the chess pieces and the fox, a new rule 9 holds the Victorian look,
# and the two Phase rows.   python3 claudemd425.py <CLAUDE.md>
import sys
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
def rep(a, b):
    global s
    if s.count(a) != 1: raise SystemExit('CLAUDE.md: %r found %d' % (a[:70], s.count(a)))
    s = s.replace(a, b)
rep("""the royals are SIGNS, like chess pieces, never
   faces (Phase 420: '체스처럼 저렇게 하는게 좀 더 깔끔한 듯. 상상력도 주고'): the King's crown (navy, a cross, three jewels),
   the Queen's crown (coral, five points with pearls), Princess Clara's tiara; the King's dragon and cows are words only;
   the rabbit butler appears only in the REMEMBER band;""",
"""the royals are Staunton CHESS PIECES, never
   faces (Phases 420, 424: '체스 테마 너무 좋다'): the King navy, the Queen coral, Princess Clara a pink pawn with a tiara
   (pink is hers alone; a pawn that crosses the board becomes a queen); the King's dragon and cows are words only;
   the butler is a FOX and appears only as his oval portrait with a coral bow tie (the REMEMBER band, the map's Lodge,
   the welcomes) -- never as a full figure in a picture ('그냥 초상화에만 넣자'); the rabbit is gone;""")
rep("""## Verified Piece Counts (2026 Syllabus)""",
"""9. **The Victorian look** (Phases 424-425, her decisions of 2026-10-10). Colours: navy, coral and green only -- green
   is the check --, pink only for Clara, NO BEIGE anywhere (white paper; hairlines are navy at low opacity). The
   wainscoting is lines only: a cornice running head (thick line, thin line, dentils), white picture boxes with the
   cut-in-corner frame, 'At the piano' and PLAY as raised panels in lines, REMEMBER as the chair rail with the fox's
   portrait, a chequered floor at every page's foot with the page number on a plaque; step numbers and section letters
   on chess squares; a drop capital in a dark square and a chequered diamond under titles on openers; Playfair italic
   for subheads and numbers, spaced capitals for small labels. The chapter map is a STREET of classical buildings
   drawn in lines (Lodge, Library, Clock Tower, Conservatory, Academy, Theatre, Museum -- one a stage, each window a
   chapter: '단순하지만 그 쉐입으로 조금 클래식함을'), with 'Clara's journey' (the chapters as chess squares) to show
   where you are; no colour on the buildings. The room scene's piano is the parlour upright seen from the front; the
   grand piano waits for a concert room of its own.

## Verified Piece Counts (2026 Syllabus)""")
rows = """| 424 | 2026-10-10 | **The Victorian look, applied to every book and the app's book parts** (her decisions of 09:00-12:14, Phases 421-423). patch424.js (Node, @babel/parser removes the old parts by name) + vic424.gen.jsx (the pieces and the fox portrait, drawn once by cast/cast.py and cast/butlers.py) + vic424.jsx (the new parts): LbPage/WbPage with the cornice head, the chequered floor and the page plaque; LbPic white with the cut-in-corner frame; LbRemember = the chair rail with the fox portrait; LbTick/Faces/'Got it!'/'Checked' and the Teacher copy's answers GREEN #2b6e56; LbPiano/PLAY/LbTune as raised panels; step numbers and section letters on chess squares; openers with a drop capital, a dotted contents list and the chequered diamond; BK.soft white. sfKing/sfQueen/sfClara draw the Staunton pieces in the crowns' boxes, so every chapter, the app and the check rows follow. Playfair loaded in 700-900 and italics. |
| 425 | 2026-10-10 | **The map is a street; the books lose their last beige; a fresh-eyes pass.** Her 12:35 'B가 좋다 ... C를 같이 써서', 12:40 'single colours, classical lines', 12:50 '좋다 이렇게 가보자'. patch425.js + street425.jsx: houseShapes draws the street (lines only: entablatures with dentils and the building's name in the frieze, arched windows with keystones and bracketed sills, quoins, pilasters, Ionic columns, balustrades with urns, a pediment, a mansard with a lyre, a palm-house roof, a ribbed dome; dentils, balusters and pavement as patterns); each window a chapter button (number on a chess square, green when done, coral frame and Clara the pawn where you are); HouseMap = 'Clara's journey' (a 7 x 5 board, Clara on your square, a tap finds the window) over the street; the student page shows the board alone (its squares open chapters); the Workbook's front matter colours in the street over two pages (stages 1-4, 5-7), the chapter map pages show a table with chess squares. Review fixes (a reviewer agent that had not seen the work): the rabbit left chapter 1's pictures (puppet: the string hangs from above; mirror game: brother and sister face each other), 'C · D' gets two squares, chapter 2 page 2's pictures fit their frames, chapter 1 page 6's hands too, chapter 4 page 6's words off the staff lines, the wrist label clear of the piano, a smaller page plaque, note runs never break, beige rules/ground lines/boxes in the books now navy hairlines, labels say chess pieces. Guide: svgs re-exported (first-steps, note-names, staff; chapter 1's hero without the rabbit, its ground lines navy), the front page is the street ('The Piano Butler's street', three stretches on big screens, one on phones, house.jpg two stretches on white), 4 worksheets + printables cards recaptured, pages rebuilt --final. Checks: street425test 54/54 (new; house402test retired), ws419 45/45, ch1 21/21, ch2 21/21, ch3 35/35, sf405 22/22, no-song 24/24, lbcheck/wbcheck/spreadcheck chapters 1-5 + front matter 0 overflow en/ko, picfit425 (nothing crosses a frame's inner line). Not done: the printables cards of chapters 6-26 still show the old page head; chapter 5's 'crown check' wording is still to ask her. |
"""
i = s.index('| 423 | 2026-10-10 |'); j = s.index('\n', i) + 1
s = s[:j] + rows + s[j:]
open(p, 'w', encoding='utf-8').write(s); print('CLAUDE.md ok')
