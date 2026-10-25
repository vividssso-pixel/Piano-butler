import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 658 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 659 | 2026-10-25 | **Chapter 5's tunes fit a phone, and the beat is seen passing (her 23:04, 'this is cut off; and when it plays, show the beat passing in the rests too').** Built on row 658. HpRows draws a tune in lines of two bars (each hand's row stacked inside a bar, a bar line after each), so no row runs off the screen or the page. While a tune plays, every beat lights as it passes: the note (coral), a held note's dashed circle (soft coral; the note now keeps sounding for its held beats), and in the hand that waits its turn a coral dot. Two-hand tunes keep 'right'/'left' at the start of each line; Over to G names the position over the bar where it changes ('C position', 'G position'). The same in the Lesson Book page 7 and the Echo on page 6. hp682.jsx updated to match. Files: drills.html, drills.src.html, _workspace/concept-book-kit/sc/patch683.py, _workspace/concept-book-kit/sc/hp682.jsx. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
