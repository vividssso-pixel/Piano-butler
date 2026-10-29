import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 739 |')]
assert len(idx) == 1
assert not any(l.startswith('| 740 |') for l in lines)
rows = [
"| 740 | 2026-10-29 | **The Beginner Lesson Books, fun first (Build CU; her 12:51: the joke is not it, and not funny; 'what you learn' and 'what you can do after' must look plainly different, with tick boxes; the turtle and the bird can both walk on the ground, so middle C is where they meet; then the next chapters).** (1) The butler's joke is gone (LbJoke). In its place on every Beginner opener, 'Guess first!' (LbGuess): a question the chapter answers, a line for the guess and the page with the answer (online: one tap shows it). (2) Every opener of all 59 Lesson Books and the two whole-book openers: 'By the end, you can' is now 'After this chapter, I can' (or 'After this book') in a raised panel with green tick boxes (LB_CAN_CSS, keyed on the heading's lb-can-h), so it never looks like 'In this chapter', the contents with page numbers. (3) Chapter 2, step 3: middle C is the ground where the turtle and the bird can both walk; the picture shows them meeting there, and the Remember says so. (4) A challenge under every step's 'At the piano' (LbChallenge: 5 in a row, or beat your time) in all 13 Beginner chapters, 66 in all, and a guess on each opener; written to each page's own skill in her words (small and big house, turtle and bird, Clara, the Queen and the King, walk and run-ning, mirror twins, the arm carries the hand). (5) The strips took room from the pictures: a printed picture box now fits its drawing (LbPic measures the drawn extent, spills included, and narrows a full-width drawing or, failing that, zooms it; never below 60%; pages that fit are untouched). It also fixes three pages that spilled before (Dynamics pages 3 and 5, The Staff page 3). All 59 books: no picture spill, no page overflow. Sources patch768.py (1 to 4, chapters 1 to 7), patch769.py (chapters 8 to 13), patch770.py (5); tests cu768.js, pic769.js, sp770.js, ov761.js. |",
]
lines[idx[0] + 1:idx[0] + 1] = rows
open(p, 'w', encoding='utf-8').write('\n'.join(lines))
print('row 740 added')
