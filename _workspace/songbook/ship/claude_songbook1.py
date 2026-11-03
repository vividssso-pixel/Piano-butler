"""Notes for the song Lesson Book's sample lesson (chat window, 4 Nov). Run from the repo root:
python3 _workspace/songbook/ship/claude_songbook1.py CLAUDE.md CLAUDE-history.md"""
import sys, io, re
md, hist = sys.argv[1], sys.argv[2]
s = io.open(md, encoding='utf-8').read()
old = "1. The song Lesson Book, Level 0 (her 4 Nov 01:00, 'books first'): a sample lesson for her to judge first, then the book."
new = ("1. The song Lesson Book, Level 0 (her 4 Nov 01:00, 'books first'): a sample lesson for her to judge first, then the book. "
       "The sample is made (4 Nov, chat window): Lesson 6, Mary had a little lamb, 4 A4 pages, in `_workspace/songbook/` "
       "(the PDF, the generator and a README); waiting for her call on the format, the four ways and the level fit. "
       "After her call: the Level 0 song list (12 to 16 public-domain songs), the rest of Level 0 by December, a print trial in January.")
assert s.count(old) == 1, 'Next (Claude) item 1 changed; read it again'
s = s.replace(old, new)
io.open(md, 'w', encoding='utf-8').write(s)

h = io.open(hist, encoding='utf-8').read().split('\n')
rows = [i for i, l in enumerate(h) if re.match(r'^\| \d+ \|', l)]
nums = [int(h[i].split('|')[1]) for i in rows]
# Two windows both took row 850 on 3-4 Nov (the Handbook's In action row and this window's books-first row, written
# 3 minutes apart); this window's row, the later in the table, becomes 851 if 851 is still free.
mine = [i for i in rows if h[i].startswith('| 850 | 2026-11-04 |')]
if len(mine) == 1 and 851 not in nums:
    h[mine[0]] = '| 851 |' + h[mine[0]][len('| 850 |'):]
    nums = [int(h[i].split('|')[1]) for i in rows]
n = max(nums) + 1
row = (f"| {n} | 2026-11-04 | **The song Lesson Book: the sample lesson (chat window; her 4 Nov 01:00 'books first', Level 0 first, "
       "the song-led set).** Lesson 6, Mary had a little lamb (the number a placeholder until the song list), 4 A4 pages in the "
       "Handbook's look (navy and coral on white, Atkinson Hyperlegible, Playfair heads). One song, five parts, sound before "
       "symbol: 1 Listen and sing (the tune with the words; a QR box for the recording, placeholder); 2 Say and clap (the words "
       "on a one-line rhythm staff, the counts under them, coral where a note starts and grey dashes while it is held); 3 Read "
       "it (C position on the keys with the song's notes lit and the finger numbers, the letter names of bars 1 to 4 in boxes, "
       "step or skip); 4 Play it four ways, one star to four, the tune the same and more for the left hand each way (Way 1 the "
       "tune with right-hand fingers; Way 2 one long note below, C or G; Way 3 with chords, C-G or D-G on beats 1 and 3; Way 4 "
       "a moving bass, 5 1 3 1 and 4 1 2 1), as her example book's A to D types; 5 Check (I can..., the four ways, the "
       "teacher's Pass or Not yet, lines for the teacher's note). The facts checked on Wikipedia: Sarah Josepha Hale, first "
       "printed in Boston in 1830; sung today to the tune of Merrily We Roll Along. Music engraved with Verovio from one JSON "
       "per song; check.js: every page's overflow 0, every label's ink clear of noteheads, stems and other labels, the answer "
       "boxes in a row of their own below middle C's ledger line. `_workspace/songbook/` (README has the build). Row 850 of "
       "4 Nov renumbered 851 (both windows had taken 850). Waiting for her call. |")
h.insert(rows[-1] + 1, row)
io.open(hist, 'w', encoding='utf-8').write('\n'.join(h))
print('CLAUDE.md and CLAUDE-history.md updated (row', n, ')')
