import sys, io
md, hist = sys.argv[1], sys.argv[2]   # CLAUDE.md, CLAUDE-history.md
s = io.open(md, encoding='utf-8').read()
def R(old, new):
    global s
    assert s.count(old) == 1, old[:80]
    s = s.replace(old, new)
R("| **Git** | Pushed up to CW (`93fc0e3`) on 2026-10-29. CX, and CY to DC together, committed, waiting for her push. |",
  "| **Git** | Pushed up to CW (`93fc0e3`) on 2026-10-29. CX, CY to DC (`28013ea`) and DD to DF committed, waiting for her push. |")
R("the 8 Prelim books (CZ) and the 8 Grade 1 books (DB) too.", "the 8 Prelim books (CZ), the 8 Grade 1 books (DB) and the 6 Grades 2 and 3 books (DE) too.")
R(" The Prelim and Grade 1 checkpoints are on paper too: `?book=check&floor=1|2` and `?book=checkkey&floor=1|2`, on the Books shelf after chapters 21 and 29 (DA, DC).",
  " The Prelim, Grade 1, Grade 2 and Grade 3 checkpoints are on paper too: `?book=check&floor=1|2|3|4` and `?book=checkkey&floor=…`, on the Books shelf after each floor's last chapter (DA, DC, DF). The Books are their own tab next to Chapters in the teacher view, `?view=books` (DD, her 30 Oct call).")
R("- Push: CX, and CY to DC (one commit).", "- Push: CX, CY to DC, and DD to DF (three commits).")
R("1. The Grades 2 and 3 books, fun first (and splitting their mixed rooms), with their checkpoints on paper. Then the Workbooks.",
  "1. Her call on splitting the mixed Grades 2-3 rooms by grade (on the board). Then the Workbooks, fun first, floor by floor.")
io.open(md, 'w', encoding='utf-8').write(s)
h = io.open(hist, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(h) if l.startswith('| 748 |')]
assert len(idx) == 1 and not any(l.startswith('| 749 |') for l in h)
h[idx[0] + 1:idx[0] + 1] = [
 "| 749 | 2026-10-30 | **The Books tab (Build DD; her 13:03).** In the teacher view the Books are a tab of their own next to Chapters (Home · Chapters · Books · Toolbox · Practice), `?view=books`; the Toolbox keeps its activities only, and the old `?view=toolbox&sec=books` still lands on the Books tab. The tab shows only when booksUnlocked() (BOOKS_PUBLIC, so always). A chapter opened from the shelf keeps the Books tab. Test: dd779.js. |",
 "| 750 | 2026-10-30 | **The Grades 2 and 3 floors' Lesson Books, fun first (Build DE).** As CZ and DB: one 'Guess first!' on each opener and one challenge above every step's Remember line: Ear Training Grade 2 (3) and Grade 3 (5, one function l2LbPages with g; the guess and the clap challenge differ by g), Melody & Phrasing 9, Scales further 5 (two 'Beat your time', beat20 B flat major and beat21 the chromatic scale), Intervals and chords further 5, Rhythm further 5 (its pages come from pg(no, …): R2_CHAL[no] after the piano steps). 38 challenges, 7 guesses. The Melody opener's map is lower in print only (270). Test: cz775.js with the six ids. |",
 "| 751 | 2026-10-30 | **The Grade 2 and Grade 3 checkpoints on paper (Build DF).** `?book=check&floor=3|4` (two pages each) and `?book=checkkey&floor=3|4`. Parts: Ear Training Grade 2 A B (new, the teacher plays: the higher or the lower of two together; same or different rhythm; L2CkpPaper and L2CkpKey with g), Melody B C, Scales further B D; Ear Training Grade 3 A B (which degree from the keynote; in two or in three), Intervals and chords further B D, Rhythm further C D. New items on the checkpoint route (MLX_CHK qa and word, after the AO trim; SCF_WB.chk meet and chrom; H3_WB.chk deg and cad; R2_CHK). Rhythm further's parts B to D were written out by hand in the check and the key: now data (R2_CHK). Test: df781.js (FLOORS=0a,0b,1,2,3,4), shelf776.js with N=6. |",
]
io.open(hist, 'w', encoding='utf-8').write('\n'.join(h))
print('CLAUDE.md and CLAUDE-history.md updated (rows 749 to 751)')
