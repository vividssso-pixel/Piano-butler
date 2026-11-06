#!/usr/bin/env python3
# Phase 429 (her 2026-10-11 22:22): 'rung' is a hard word -- English says LADDER (Korean keeps 발판); chapter 6's Workbook
# gets dotted guide lines to draw ladders on (and to count them), no numbers over 'the missing notes'; the lid on a note in
# a space is a mistake the book shows, the Workbook checks and the app names.    python3 patch429.py <drills.src.html> <ll429.jsx>
import sys, re
src, jsx = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read(); add = open(jsx, encoding='utf-8').read()
def rep(a, b, what, n=1):
    global s
    c = s.count(a)
    if c != n: raise SystemExit(what + ': expected %d, got %d' % (n, c))
    s = s.replace(a, b)

# 1. chapter 6's pages, moving parts, Workbook and Teacher copy: the new version
i0 = s.index('// ─── Phases 427-428: chapter 6 (Ledger Lines) Lesson Book'); i1 = s.index('\nconst LESSON_BOOKS = {', i0)
s = s[:i0] + add.rstrip('\n') + s[i1:]

# 2. dotted guide lines on paper staves (guides = [above, below]), passed through SfRow; a list of answers may go unnumbered
rep("function PaperStaff({ clef = 'treble', notes = [], width = 150, ink = BK.ink, clefOn = true, minSpan }) {",
    "function PaperStaff({ clef = 'treble', notes = [], width = 150, ink = BK.ink, clefOn = true, minSpan, guides }) {", 'paper sig')
rep("""  if (minSpan) { ys.push(yOf(minSpan[0], staves[0]) - 9, yOf(minSpan[1], staves[staves.length - 1]) + 9); }
  const y0 = Math.min(...ys), y1 = Math.max(...ys);""",
    """  if (minSpan) { ys.push(yOf(minSpan[0], staves[0]) - 9, yOf(minSpan[1], staves[staves.length - 1]) + 9); }
  const guideDs = (st) => { const c = CLEFS[st], g = []; if (guides) { for (let k = 1; k <= (guides[0] || 0); k++) g.push(c.high + 2 * k); for (let k = 1; k <= (guides[1] || 0); k++) g.push(c.low - 2 * k); } return g; };
  staves.forEach(st => guideDs(st).forEach(p => ys.push(yOf(p, st) - 5, yOf(p, st) + 5)));
  const y0 = Math.min(...ys), y1 = Math.max(...ys);""", 'paper guides span')
rep("""      {grand && <line x1="2" x2="2" y1={yOf(38, 'treble')} y2={yOf(18, 'bass')} stroke={ink} strokeWidth="1.5"/>}
      {clefOn && staves.map(st => <ClefGlyph key={'c' + st} clef={st} st={st} yOf={yOf} ink={ink}/>)}""",
    """      {grand && <line x1="2" x2="2" y1={yOf(38, 'treble')} y2={yOf(18, 'bass')} stroke={ink} strokeWidth="1.5"/>}
      {staves.map(st => guideDs(st).map(p => <line key={st + 'g' + p} x1={clefOn ? 40 : 4} x2={width - 4} y1={yOf(p, st)} y2={yOf(p, st)} stroke={ink} strokeOpacity="0.45" strokeWidth="0.9" strokeDasharray="2.2 3"/>))}
      {clefOn && staves.map(st => <ClefGlyph key={'c' + st} clef={st} st={st} yOf={yOf} ink={ink}/>)}""", 'paper guides draw')
rep("function SfRow({ clef = 'none', notes = [], width = 360, items = [], minSpan, boxW = 40, boxH = 32 }) {",
    "function SfRow({ clef = 'none', notes = [], width = 360, items = [], minSpan, boxW = 40, boxH = 32, guides }) {", 'sfrow sig')
rep("    <PaperStaff clef={clefOn ? clef : 'treble'} clefOn={clefOn} notes={notes} width={width} minSpan={minSpan}/>",
    "    <PaperStaff clef={clefOn ? clef : 'treble'} clefOn={clefOn} notes={notes} width={width} minSpan={minSpan} guides={guides}/>", 'sfrow guides')
rep("""<span style={{color:BK.muted}}>{i + n0}.</span>""", """{n0 != null && <span style={{color:BK.muted}}>{i + n0}.</span>}""", 'tcAns unnumbered')

# 3. LADDER, not rung, wherever an English reader sees it (chapters 4-6, the drill, the toolbox); Korean keeps 발판
for a, b, n in [
    ("'One rung: Queensland'", "'One ladder: Queensland'", 2), ("'One rung: Kingsland'", "'One ladder: Kingsland'", 2),
    ("'Two rungs, both lands'", "'Two ladders, both lands'", 2), ("'Up to three rungs, fast (Grade 2)'", "'Up to three ladders, fast (Grade 2)'", 2),
    ("blurb: 'Up into the sky, down into the sea, a rung at a time.'", "blurb: 'Up into the sky, down into the sea, a ladder at a time.'", 1),
    ("blurb: 'Borrowed rungs: the same key, written two ways.'", "blurb: 'Borrowed ladders: the same key, written two ways.'", 1),
    ("title: 'Draw the rungs', blurb: 'As many rungs as the note needs: no gaps, none too many.'", "title: 'Draw the ladders', blurb: 'As many ladders as the note needs: no gaps, no lid, none too many.'", 1),
    ("little ladder rung of her own", "little ladder of her own", None), ("little ladder rung", "little ladder", None),
    ("its ladder rung", "its ladder", None), ("(ladder rung)", "(ladder)", None), ("on the ladder rung just", "on the ladder just", None),
    ("Clara\\'s rung", "Clara\\'s ladder", None), ("Clara's rung", "Clara's ladder", None),
    ]:
    c = s.count(a)
    if n is not None and c != n: raise SystemExit('ladder ' + a + ': %d' % c)
    if n is None and c == 0: raise SystemExit('ladder ' + a + ': none')
    s = s.replace(a, b)
open(src, 'w', encoding='utf-8').write(s); print('patch429 ok')
