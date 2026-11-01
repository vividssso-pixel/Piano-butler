import sys, io
md, hist = sys.argv[1], sys.argv[2]   # CLAUDE.md, CLAUDE-history.md
s = io.open(md, encoding='utf-8').read()
def R(old, new):
    global s
    assert s.count(old) == 1, old[:80]
    s = s.replace(old, new)
R("Pushed up to EC (`754294a`) on 2026-10-31. ED, EE and EF committed, waiting for her push.", "Pushed up to EC (`754294a`) on 2026-10-31. ED, EE, EF and EG committed, waiting for her push.")
R("- Push: ED, EE and EF (three commits), before she opens a cloud window.", "- Push: ED, EE, EF and EG (four commits), before she opens a cloud window.")
R("(sc/wbf44.code.js). |", "(sc/wbf44.code.js). The Prelim Workbooks the same way (EG, her 1 Nov 10:39 and 14:37): the ladder race (ch. 17), the four-bar scale (ch. 19), and in Minor Scales (ch. 20) same keys, a new home, the step trail with the T½, and the same tune, darker; Tempo, Rhythm, Scales and Signs left as they are (sc/wbf45.code.js). |")
R("1. The Workbooks, fun first, floor by floor: the Beginner floor done (EF); next the Prelim floor, the same way", "1. The Workbooks, fun first, floor by floor: the Beginner floor done (EF), the Prelim floor done (EG); next the Grade 1 floor, the same way")
io.open(md, 'w', encoding='utf-8').write(s)
h = io.open(hist, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(h) if l.startswith('| 776 |')]
assert len(idx) == 1 and not any(l.startswith('| 777 |') for l in h)
h[idx[0] + 1:idx[0] + 1] = [
 "| 777 | 2026-11-01 | **The Prelim Workbooks, fun first (Build EG; her 10:39 'yes' to showing the plan, 14:37 'yes' to the plan and to one page first, 14:58 'go on').** All seven Prelim Workbooks read page by page (Ear Training, Prelim has none). Four left as they are: Tempo, Scales and Signs are set tasks, a different job in each part, done alone; Rhythm writes the count often, but every PLAY plays it, and Signs plays every road map. In the other three, five parts swapped for a game that practises the same thing, none added. Ch. 17 p. 2 PLAY 'How many ladders?' (the same notes' ladders YOUR TURN had just drawn) → the ladder race: 14 chess squares, a note without its ladders on each of the first 13 (the room's sky, sea and between-the-staves notes, 1 to 3 ladders); write each note's ladders, then from the star move that many squares: the right counts land exactly on the flag (squares 1 3 6 7 9 12, then 14), and from every square off the path the counts run past it (LL_RACE). Ch. 19 p. 3 PLAY 'Beat puzzle' (sums: at 76, more or less than 15 seconds?) → the four-bar scale: C and G major up and back, one letter a beat box, the last note held for two: 15 notes and the hold fill four bars exactly, then play it at 60 (the room's own 'last note held for two beats'). Ch. 20 p. 3 PLAY 'Key signature twins' (the same four pairs as YOUR TURN above, as lines) → same keys, a new home: C/A, G/E, F/D on lit keys, a navy bracket over the major, a red one under its natural minor twin; play both (MS_TWINS). P. 5 PLAY 'The secret code' ('from memory', the answer in the boxes above) → the step trail of chapter 13 with the T½: from the star on E, T S T T S T½ S (SP_HAR), the seventh on the flag; then name it, E harmonic minor. P. 6 YOUR TURN 'Listen this week' (someone at home had to play: Book rules 3 and 4) → the same tune, darker: Hot cross buns and Mary had a little lamb (MT_SONGS) in C, G or F major with their steps; write the same steps in the minor twin (A, E, D minor), play both; the tunes use no 7th, so the page says minor; Code breaker renumbered 9 and 10. Teacher copies: every new answer computed from the same data. Workbooks stay English. Code sc/wbf45.code.js, source sc/patch809.py; test sc/eg810.js (the parts, nothing over in the three Workbooks and Teacher copies, the race, the four bars, the trail, the twins, the tunes); the full set. |",
]
io.open(hist, 'w', encoding='utf-8').write('\n'.join(h))
print('CLAUDE.md and CLAUDE-history.md updated (row 777)')
