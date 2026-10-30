import sys, io
md, hist = sys.argv[1], sys.argv[2]   # CLAUDE.md, CLAUDE-history.md
s = io.open(md, encoding='utf-8').read()
def R(old, new):
    global s
    assert s.count(old) == 1, old[:80]
    s = s.replace(old, new)
R("DD to DF (`958c9fa`) and DG to DJ committed, waiting for her push. |", "DD to DF (`958c9fa`), DG to DJ (`935ca7f`) and DK to DL committed, waiting for her push. |")
R("The Books are their own tab next to Chapters in the teacher view, `?view=books` (DD, her 30 Oct call).", "The Books are their own tab next to Chapters in the teacher view, `?view=books` (DD, her 30 Oct call); the cut-out teaching aids are a Printables tab of their own, `?view=printables` (DL, her 30 Oct 14:57). Students read 'the red note / key' (never 'coral'), and every notehead on every staff fits its space (DK, her 15:03).")
R("- Push: CX, CY to DC, DD to DF, and DG to DJ (four commits).", "- Push: CX, CY to DC, DD to DF, DG to DJ, and DK to DL (five commits).")
R("1. A Printables tab for the cut-out teaching aids (her 14:57 question; my yes is on the board). Then own check-up items for the split rooms, and the Workbooks, fun first, floor by floor.",
  "1. Own check-up items for the split Grades 2 and 3 rooms; then the Workbooks, fun first, floor by floor.")
io.open(md, 'w', encoding='utf-8').write(s)
h = io.open(hist, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(h) if l.startswith('| 755 |')]
assert len(idx) == 1 and not any(l.startswith('| 756 |') for l in h)
h[idx[0] + 1:idx[0] + 1] = [
 "| 756 | 2026-10-30 | **'The red note', and noteheads that fit their lines (Build DK; her 15:03).** (1) Words: 'coral' meant nothing to a child, so every student-facing 'coral note / key / circle / ...' says 'red' (321 places; 'orange' too, 21), and the Korean 산호색 / 주황색 say 빨간 (빨간색 before a particle; 141). The colour itself stays coral; code names (BK.coral, var(--coral), the coral arguments) are untouched. One mistranslation fixed on the way: 'Chorale preludes for organ' was '산호색 전주곡', now '코랄 전주곡'. (2) Noteheads: an audit of every staff on every book page and online lesson (heads786.js: 272 pages, 6,278 heads; five equally spaced lines are a staff, a filled ellipse over one is a head, measured in the staff's own units with its tilt and stroke) found 5,271 heads taller than the space between two lines (the pen notation's 7.2 x 5.3 head on a gap of 10 reached 6.2 with its stroke). The rule now: a head's full height, stroke included, is 0.9 of the space; a space note sits clear of both lines and a line note's line enters and leaves at its middle; the open hole-style heads keep the short line through the hole. nvbHead (filled 5.8 x 4.1 and no stroke, the minim 4.6 x 3.1, the semibreve 6.2 x 2.8; stems and beams moved in to the new edge), the 7 x 5 tilted heads on gap-10 staffs (20 sites), the hole-style heads (SfStaff, LlRungs, IvxWrite, ChxWrite, StaffView online: 6.3 x 4.5), SatbStaff, K4Melody, MwStaff, MlxMapSvg, StmMiniPage, the two 5.4 x 3.9 heads, the pen mini staffs (3.8 x 2.7 on gap 6, 2.5 x 1.8 on gap 4). After: overflow 0 on every page. Augmentation and beat dots (r 2 to 3) sit between lines by design and are not heads. |",
 "| 757 | 2026-10-30 | **The Printables tab (Build DL; her 14:57 'a room of their own for the cut-out printables, so they can be shown later as free printables').** In the teacher view the cut-out sets are a tab of their own next to Books (Home · Chapters · Books · Printables · Toolbox · Practice), `?view=printables`: one sheet, a card per set in chapter order with its name, chapter and floor (the chapter name opens the chapter under the tab), one line on what it is for, its pages, Print, and Print all sets. Navy and coral only, no pictures. The Books tab keeps the books and the checkpoints; the chapter opener's note says 'Printables'. Nothing on the main site links to it (call 30 stays parked). Test: dd779.js (six tabs, 14 cards and Print links, a chapter opened from a card keeps the tab, no cut-outs on Books). |",
]
io.open(hist, 'w', encoding='utf-8').write('\n'.join(h))
print('CLAUDE.md and CLAUDE-history.md updated (rows 756 to 757)')
