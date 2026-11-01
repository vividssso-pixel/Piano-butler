import sys, io
md, hist = sys.argv[1], sys.argv[2]   # CLAUDE.md, CLAUDE-history.md
s = io.open(md, encoding='utf-8').read()
def R(old, new):
    global s
    assert s.count(old) == 1, old[:80]
    s = s.replace(old, new)
R("Pushed up to EH (`9355b3c`) on 2026-11-01. Dashboard D1 (`49923a9`, the dashboard window) and EI committed, waiting for her push.",
  "Pushed up to `b5f427b` on 2026-11-02 (EI, the dashboard's D1 to D1c, the direction and the SEO commits). EJ committed, waiting for her push.")
R("- Push: Dashboard D1 and EI (two commits), before she opens a cloud window.", "- Push: EJ (one commit), before she opens a cloud window.")
R("(sc/wbf47.code.js). |", "(sc/wbf47.code.js). The Grade 3 Workbooks the same way (EJ, her 23:32 'keep going'): Rhythm, Grade 3's three PLAYs (questions, the same as its check-up) now play with the same words: ap-ple even, then dotted; the minim beat in 2/2 and 3/2; simple or compound said in words; Writing a Melody, Scales, Grade 3 and Chords and Cadences, Grade 3 left as they are (sc/wbf48.code.js). |")
R("the Grade 2 floor done (EI); next the Grade 3 floor, the same way (her 1 Nov 19:44: no plan first; build the best and she checks; only the parts better changed).",
  "the Grade 2 floor done (EI), the Grade 3 floor done (EJ); next the Grade 4 floor, the same way (her 1 Nov 19:44: no plan first; build the best and she checks; only the parts better changed), taking turns with the Map merge on drills.src.html (the direction of 1 Nov: between workbook builds, in small commits).")
io.open(md, 'w', encoding='utf-8').write(s)
h = io.open(hist, encoding='utf-8').read().split('\n')
rows = [l for l in h if l.startswith('| 7')]
last = max(int(l.split('|')[1]) for l in rows if l.split('|')[1].strip().isdigit())
n = last + 1   # other windows add rows too: the next free number
idx = [i for i, l in enumerate(h) if l.startswith('| %d |' % last)]
assert len(idx) == 1
h[idx[0] + 1:idx[0] + 1] = [
 "| %d | 2026-11-02 | **The Grade 3 Workbooks, fun first (Build EJ; her 1 Nov 23:32 'keep going').** Five Grade 3 rooms; Ear Training, Grade 3 has no Workbook. Writing a Melody (the page is the writing), Scales, Grade 3 (its check-up only) and Chords and Cadences, Grade 3 (written PLAYs beside played weeks) left as they are. Rhythm, Grade 3 (steps 2, 4 and 5 of the shared R2Workbook; Grade 2's untouched): its three PLAYs were questions, the same as its check-up on paper, and now play with Grade 2's words, one beat a word, one note a syllable. 'Long and short' → even, then dotted: ap-ple ap-ple ap-ple pie drawn even (two quavers) and dotted (a dotted quaver and a semiquaver, counted 1 a), said, clapped, a scale each way. 'Beats in a bar' → one beat a word, in minims: 2/2 and 3/2 lines where pie is a minim, ap-ple two crotchets, wa-ter-mel-on four quavers. 'Simple or compound?' (write S or C) → say one bar of 9/8, 6/8, 3/8 and 3/4 in words, ap-ple for a beat in two, pine-ap-ple for one in three, then S or C (the words count the beats). Teacher copy: answers computed from the words; the minim-beat block moved to the first page (the second ran over). Code sc/wbf48.code.js, source sc/patch812.py; test sc/ej813.js (ei812.js's Grade 3 check follows the new parts); the full set. The direction of 1 Nov (read at commit time, decided in the dashboard window at 23:52, after her 'keep going'): workbook builds take turns with the Map merge on drills.src.html. |" % n,
]
io.open(hist, 'w', encoding='utf-8').write('\n'.join(h))
print('CLAUDE.md and CLAUDE-history.md updated (row %d)' % n)
