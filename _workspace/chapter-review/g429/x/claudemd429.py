#!/usr/bin/env python3
# Phase 429 in CLAUDE.md: Book rule 8 says LADDER (not rung) in English, and the Phase row.   python3 claudemd429.py <CLAUDE.md>
import sys
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
def rep(a, b):
    global s
    if s.count(a) != 1: raise SystemExit('CLAUDE.md: %r found %d' % (a[:70], s.count(a)))
    s = s.replace(a, b)
rep("its short line is a ladder rung (사다리 발판) until the ledger-lines chapter, which names it a\n   LEDGER LINE (덧줄; 'leger' accepted): the rungs of a ladder up into the bird's sky over Queensland and down into the\n   turtle's sea under Kingsland,",
    "its short line is Clara's little LADDER (사다리 발판; in English never 'rung' -- her 2026-10-11 22:22: a hard word)\n   until the ledger-lines chapter, which names it a LEDGER LINE (덧줄; 'leger' accepted): little ladders up into the\n   bird's sky over Queensland and down into the turtle's sea under Kingsland ('ladder 1, ladder 2'),")
row = """| 429 | 2026-10-11 | **'Ladder', not 'rung'; guide lines to draw on; the lid.** Her 22:22 notes on the chapter 6 PDF: (1) 'rung' is a word many don't know -- say LADDER: English everywhere a reader sees it (chapters 4-6 books, app, drill levels 'One ladder: Queensland' ..., toolbox, Teacher copies, the ch4 and ch6 guide pages); Korean keeps 발판. (2) The 'e.g. 1 2 3' numbers over the ladder on Workbook pp.3-4 are gone (the activity is now 'The missing notes'; the coral note is the example; the Teacher copy lists its answers unnumbered -- tcAns(label, list, null)). (3) 'How do you know how many ledger lines go there?' -- every drawing task has DOTTED GUIDE LINES beyond the staff (PaperStaff/SfRow guides=[above, below]): Draw the ladders, How many ladders? (count the dotted lines out to the note), The missing notes, Words in the sky/sea, check-up A. (4) Her students' mistake, a LID on a note in a space: the book's fourth cross is 'no lid on a note in a space' (B over Queensland with a line on top) and its text says so; Neat or not? has a lid; the app's Draw the ladders names it ('That is a lid -- a note in a space gets no line on top of it'); the Teacher copy watches for it. Guide page drawings, worksheet and printables pictures redone; both guide pages rebuilt --final. Checks: ll429test 82/82 (the 428 test, renamed words + no 'rung' in any English book of chapters 4-6, the guides, the lid), ws419 45/45, sf405 22/22, ch1 21/21, ch2 21/21, ch3 35/35, no-song 24/24, lbcheck/wbcheck 0 overflow en/ko. Samples only (not applied, her choice waits): the fox butler redrawn four ways with no jagged fur at the neck and the figure centred (cast/fox429), and seven heading fonts on a book page. |
"""
i = s.index('| 428 | 2026-10-11 |'); j = s.index('\n', i) + 1
s = s[:j] + row + s[j:]
open(p, 'w', encoding='utf-8').write(s); print('CLAUDE.md ok')
