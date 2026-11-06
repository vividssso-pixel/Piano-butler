#!/usr/bin/env python3
# CLAUDE.md: the Book rules section (Sohyun 2026-10-10 00:39: 'gather everything we decided, once, so we never have to
# say it again') + Phase rows 411-417 + a pointer from row 0h.
import sys
p = sys.argv[1]; s = open(p, encoding='utf-8').read()

RULES = """## Book rules -- Sohyun's decisions for the Lesson Book, Workbook and Teacher copy (Phase 417, 2026-10-10)

She asked (2026-10-10 00:39) for everything decided so far in one place, so she never has to say it twice, and for every
page to be checked for balance, use of space, readability and information load BEFORE she sees it. Apply these to every
chapter, old and new; when a rule and a page disagree, fix the page.

1. **The Lesson Book is the spine** (Phase 368). Workbook page N faces book page N; the app lesson is the book on screen
   (only what moves is different) plus the drill; the Teacher copy holds every teacher note, answer, watch-for and saying
   (no teacher strips in the book or the app, Phase 399); the public guide page is the short summary. If they disagree,
   the Lesson Book wins.
2. **Nothing twice** (Phases 394, 409, 417). The chapter opener is the Lesson Book's page 1 only -- the Workbook starts at
   page 2. The paper check-up is the Workbook's last page only; the book's last page is 'My five checks' at the piano
   (Not yet / Nearly / Got it!), and in the side-by-side print the two face each other. The Workbook's online box is the
   QR code only. The Workbook never re-teaches what the facing book page shows: no explanation panels or copied
   pictures; its how-lines say what to DO, in one or two lines.
3. **Set tasks, not free ones** (Phase 410: '자유를 주는 것보다 뭘 하라고 지정해서 주는게 더 낫더라'). Every activity says
   exactly what to draw, write or play: which notes, which letters, which lines, what to draw where, which letter to
   start from. No 'make your own', 'any', 'draw anything', 'a different letter each day'.
4. **A child can do every Workbook activity alone** (Phase 414: '혼자 할 수 있는 활동으로'). Nothing on paper needs a
   caller, a partner or a grown-up: calls are printed, clues are given, checking is in a mirror. Partner games (the echo
   game, the letter chain with someone) stay in the lesson, not in the Workbook or its practice logs.
5. **Big enough to draw and write in** (Phase 409: '오선들이 너무 작아... 그릴 때도 덜 어려워'). Staves about 5 mm between
   lines; big keyboards and pictures; answer boxes about 10 mm, under the keys rather than squeezed inside them when the
   keys are narrow; a box for a word is replaced by words to circle.
6. **Fill the page** (Phases 408-409: '중간에 비우지 말고'; 414: '아래 꽉 채워줘'). No empty middles, no empty bottoms:
   room left over goes to bigger drawings or one more set task of the same kind, never to blank space. Every Workbook
   step page ends with 'How did it feel? ... Checked'; the book's last page grows its five rows to the foot.
7. **Balance and reading, checked before she sees anything.** One idea per page; no more than three parts on a Workbook
   page; how-lines of at most two lines; nothing clipped, overlapping or touching (check the print, not only the
   screen); answers not bunched (e.g. no two middle Cs side by side); the answers of a set vary (not all crosses, not the
   first note always higher, every note once before any repeats); the same layout from chapter to chapter. Before
   showing her: run `_workspace/chapter-review/kit/wbcheck.js` (overflow, clipping, bottom free space, empty space in the
   PLAY box -- aim for 0 / 0 / under ~40 px / under ~35 px), `lbcheck.js`, `spreadcheck.js` and the chapter's own test,
   look at every page image yourself, and for a whole-chapter pass let a fresh reviewer (an agent that did not make the
   pages) check them against these rules.
8. **Words and cast.** Skewer, not kebab (Korean 꼬치); stool; tip joint; middle C is 'the left door of the 4th small
   house' (never 'just left of' it); its short line is a ladder rung (사다리 발판) until the ledger-lines chapter; the
   treble staff is Queensland and the bass staff Kingsland from chapter 5; the cast is King A, Queen A (drop earrings),
   Clara A (braids and tiara); only the characters are hand-drawn, frames and props are straight; no songs inside the
   chapters (the song book comes after the review); the lesson's words sit straight under the page title.

"""
anchor = "## Verified Piece Counts (2026 Syllabus)"
if s.count(anchor) != 1: raise SystemExit('anchor')
if '## Book rules' in s: raise SystemExit('rules already there')
s = s.replace(anchor, RULES + anchor)

ROWS = """| 411 | 2026-10-10 | **Chapter 1's Workbook redrawn big, every task set** (her 'the same for chapters 1-3 -- 그렇게 해줘'). Bigger set-up, warm-up and hand pictures; the drawing tasks list what to draw; 'Which finger?' hands bigger; the free finger walk became THE SECRET WALK (clues in words -> finger numbers: 1 2 3 5 4 3 2 1); the check-up page bigger. patch411.py. |
| 412 | 2026-10-10 | **Chapter 2's Workbook bigger, every task set.** 'Whose house?' two across with bigger keyboards; 'Who lives here?' = one smiley face per white key; 'Under the sea, up in the sky' = a fish, a crab and the turtle / a cloud, the sun and the bird, then a low or high note for each; the sound pairs bigger; the 88 keys taller; the check-up page two across, big keys; Teacher copy PLAY answers. patch412.py. |
| 413 | 2026-10-10 | **Chapter 3's Workbook bigger, set, and nothing twice.** The four explanation panels (doors, letter wheel, staircase, skip wheel) left the Workbook -- the facing book page teaches them; the room went to bigger keys and letter boxes (LetterRow/UpDownCell 'big'); the treasure hunt has 8 clues; the letter star bigger; the word search's free bonus became two riddles (E B E = BEE, D B E = BED); the check-up page fills (big rows one to a line, big keys). patch413.py. |
| 414 | 2026-10-10 | **Her three notes on chapter 4's Workbook** (00:39): note bingo is played ALONE ('Bingo on your own': the nine calls printed in order, 'BINGO on call [ ]'; seeded so exactly one line fills first, at call 5 or later); 'Clara visits' fills the page with two steps up (E) and two steps down (A); 'Circle every middle C' has the three Cs at set places 2, 5, 8 (never side by side) with B and D as decoys. Also: How did it feel? on every step page (it was missing in chapter 4), bigger plates/staircase/tunes, a 4-row F maze, the check-up page without the lesson-step strip, how-lines that say what to do. patch414.py. |
| 415 | 2026-10-10 | **The book's last page fills its page; the side-by-side print is whole again.** LbStageRows big rows grow to the foot of 'My five checks' (all four chapters; chapter 4's rows are the big ones too). The spread had lost the paper check-up since Phase 409 (it asked for the Workbook without its frame) and chapter 4's puzzle page: now opener, each lesson page facing its Workbook page, extra Workbook pages facing a blank, and the five checks facing the check-up on paper (ch1 13 pages, ch2 11, ch3 15, ch4 15). patch415.py. |
| 416 | 2026-10-10 | **Chapter 1 against the rules:** two secret walks (right hand 1 2 3 5 4 3 2 1, left hand 5 4 3 1 2 3 4 5) fill the play box; How did it feel? on the step-4 page; the check-up's hand pictures two across, big. patch416.py. |
| 417 | 2026-10-10 | **Book rules written down, and a fresh-eyes review of all 25 Workbook pages fixed.** Sohyun: gather every decision once, and always check balance, space, readability and load before showing her -> the 'Book rules' section near the top of this file. A reviewer agent that had not seen the work checked every page against them; fixed (patch417.py): ch1 set-up pictures not all crosses, 'check yourself in a mirror' (solo), the warm-up log no longer prints the order the TRY IT asks for, no 'say what is wrong', the ball in the hand you don't draw with, the finger quiz in one row so the hand-tracing boxes fit a child's hand, check-up '2 3 4 _' (was '2 3 2 _', two answers); ch2 circle/star instead of lines across the cards, no colouring of tiny roofs, the count box empty, circle the lighthouse key, MIDDLE C = 'the left door of the 4th small house' (the book's five checks, the Workbook, the Teacher copy and the guide page said 'just left of', which is B), legato pictures became 'which walk is legato, A or B?', check-up A's boxes under the houses (KeyBoxRow); ch3 dotted-key answer boxes under the keys, 'in my head' from a printed letter each day (G C E A D B F), numbers 1-4 / 5-7 / 8-13 (4 was used twice), the star from C (the book shows it from A), check-up A starts on F (a cut black-key group looked like a small house); ch4 real titles for 'Your turn', the line/space number is required, step/skip and up/down are CIRCLED (no writing 'skip down' in a box), all four kinds of move appear and the higher note is not always first, the Queen's and King's five each note once, the F road joins side by side from the King's row to the castle's row, check-up item 7 E-G (it was E-B, a 5th). Site: the four guide worksheets and printables images recaptured; printables' chapter 1-3 cards finally match the pages they link to (names Keyboard Patterns / The Musical Alphabet, same sample page as each guide page); guide pages rebuilt --final. Checks: wbcheck/lbcheck/spreadcheck 0 overflow and 0 clipping in en and ko; ch1 21/21, ch2 21/21, ch3 35/35 (spread now 15), sf405 22/22, no-song 24/24, house 34/34. |
"""
row410 = s.index('| 410 | 2026-10-10 |')
end410 = s.index('\n', row410) + 1
s = s[:end410] + ROWS + s[end410:]

a = "| 0h | **Chapter-by-chapter review, one chapter at a time in map order -- Lesson Book first** (Phases 367-379) | Top -- Sohyun checks, then Claude fixes | Decided 2026-10-08: the Lesson Book is the spine (see Phase 368);"
if s.count(a) != 1: raise SystemExit('0h')
s = s.replace(a, a + " **Every book page follows the 'Book rules' section near the top of this file -- check them before showing her (Phase 417).**")
open(p, 'w', encoding='utf-8').write(s); print('CLAUDE.md ok')
