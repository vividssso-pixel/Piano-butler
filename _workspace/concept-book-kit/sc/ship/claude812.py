import sys, io
md, hist = sys.argv[1], sys.argv[2]   # CLAUDE.md, CLAUDE-history.md
s = io.open(md, encoding='utf-8').read()
def R(old, new):
    global s
    assert s.count(old) == 1, old[:80]
    s = s.replace(old, new)
R("Pushed up to EC (`754294a`) on 2026-10-31. ED, EE, EF, EG and EH committed, waiting for her push.", "Pushed up to EH (`9355b3c`) on 2026-11-01. Dashboard D1 (`49923a9`, the dashboard window) and EI committed, waiting for her push.")
R("- Push: ED, EE, EF, EG and EH (five commits), before she opens a cloud window.", "- Push: Dashboard D1 and EI (two commits), before she opens a cloud window.")
R("(sc/wbf46.code.js). |", "(sc/wbf46.code.js). The Grade 2 Workbooks the same way (EI, her 21:44 'yes'): Rhythm, Grade 2's two PLAYs (sums and questions) now play with words, one beat a word, one note a syllable (pie, ap-ple, wa-ter-mel-on; pine-ap-ple a triplet in 2/4, ap-ple a duplet in 6/8); Melody's sequences the other way in place of 'make your own'; Scales, Grade 2 and Intervals, Grade 2 left as they are (sc/wbf47.code.js). |")
R("the Grade 1 floor done (EH); next the Grade 2 floor, the same way", "the Grade 1 floor done (EH), the Grade 2 floor done (EI); next the Grade 3 floor, the same way")
io.open(md, 'w', encoding='utf-8').write(s)
h = io.open(hist, encoding='utf-8').read().split('\n')
rows = [l for l in h if l.startswith('| 7')]
last = max(int(l.split('|')[1]) for l in rows if l.split('|')[1].strip().isdigit())
n = last + 1   # the other window adds rows too: take the next free number
idx = [i for i, l in enumerate(h) if l.startswith('| %d |' % last)]
assert len(idx) == 1
h[idx[0] + 1:idx[0] + 1] = [
 "| %d | 2026-11-01 | **The Grade 2 Workbooks, fun first (Build EI; her 21:44 'yes' to going on the same way).** Five Grade 2 rooms; Ear Training, Grade 2 has no Workbook. Scales, Grade 2 and Intervals, Grade 2 left as they are: set tasks, and their weekly logs are how scales and intervals are practised. Rhythm, Grade 2 (its steps 1 and 3 of the shared R2Workbook; Grade 3's steps untouched): PLAY 'Semiquaver sums' (how many semiquavers in a crotchet, a quaver, a dotted quaver) → one beat a word: two 4/4 lines of pie, ap-ple, wa-ter-mel-on, one note a syllable; draw each beat's notes, then say, clap and play on one note (line 3 is the room's own semiA, q s4 p q). PLAY 'Three for two, two for three' (two questions) → the same, with pine-ap-ple and ap-ple: in 2/4 three syllables in a crotchet beat are a triplet, in 6/8 two in a dotted crotchet beat a duplet. The week's third row 'Make up a bar of 2/4 with one triplet' (a free task) → 'Switch every beat: three claps, then two, at 60'. Melody and Phrasing p. 6 PLAY 'make a motif of your own' → play sequences 5 and 6 the other way. Teacher copies: the word lines' notes computed from the words. Code sc/wbf47.code.js, source sc/patch811.py; test sc/ei812.js; the full set. |" % n,
]
io.open(hist, 'w', encoding='utf-8').write('\n'.join(h))
print('CLAUDE.md and CLAUDE-history.md updated (row %d)' % n)
