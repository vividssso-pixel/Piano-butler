#!/usr/bin/env python3
# Phase 414: her three notes on chapter 4's Workbook (2026-10-10 00:39) + the Workbook rules applied:
#   (1) note bingo becomes a game a child can play ALONE ('혼자 할 수 있는 활동으로'): the calls are printed in order;
#       colour each one, and write the call that makes three in a row;
#   (2) 'Clara visits' fills its page with one more pair: two steps up (E) and two steps down (A) ('draw E 그리고 A 까지');
#   (3) 'Circle every middle C': the three Cs no longer sit side by side ('너무 같이 붙어있는데 도가') -- set places,
#       notes 2, 5 and 8, the decoys B (over the King's staff) and D (under the Queen's) between them;
#   (4) how-lines say what to do; the facing book page does the teaching (nothing twice).
#   python3 patch414.py <drills.src.html>
import sys
src = sys.argv[1]; s = open(src, encoding='utf-8').read()
def rep(a, b, what, n=1):
    global s
    c = s.count(a)
    if c != n: raise SystemExit(what + ': expected %d, got %d' % (n, c))
    s = s.replace(a, b)

# (3) middle C at set places, never next to each other
rep("""  const s5 = withSeed(k('s5'), () => {
    const cs = shuffle([0, 1, 2, 3, 4, 5, 6, 7]).slice(0, 3), rest = [24, 25, 26, 27, 29, 30, 31, 32];
    return { mid: [0, 1, 2, 3, 4, 5, 6, 7].map(i => cs.includes(i) ? { d: 28, staff: Math.random() < 0.5 ? 'treble' : 'bass' } : { d: rest[Math.floor(Math.random() * rest.length)] }) };
  });""",
    """  // Phase 414: set places -- Clara's C is notes 2, 5 and 8 (never side by side), with B and D as decoys near her
  const s5 = { mid: [{ d: 30 }, { d: 28, staff: 'treble' }, { d: 25 }, { d: 27 }, { d: 28, staff: 'bass' }, { d: 29 }, { d: 24 }, { d: 28, staff: 'treble' }] };""", 'middle C places')

# (1) solo bingo: the calls in order, and the call that makes BINGO
rep("""  const s6 = withSeed(k('s6'), () => ({ bingo: shuffle([24, 25, 26, 27, 28, 29, 30, 31, 32]) }));""",
    """  const s6 = withSeed(k('s6'), () => ({ bingo: shuffle([24, 25, 26, 27, 28, 29, 30, 31, 32]) }));
  // Phase 414: played alone -- the calls are printed; one line (only one) is the first to fill, and not before call 5
  Object.assign(s6, withSeed(k('s6calls'), () => { for (;;) { const calls = shuffle([24, 25, 26, 27, 28, 29, 30, 31, 32]); const w = sfBingoWin(s6.bingo, calls); if (w && w.lines.length === 1 && w.at >= 5) return { calls, win: w }; } }));""", 'bingo calls')
rep("""const sfLS = (d, clef = 'treble') =>""",
    """// the call names: whose note it is (F and G live in both palaces)
const SF_CALL = { 24: 'the King’s F', 25: 'the King’s G', 26: 'the King’s A', 27: 'the King’s B', 28: 'Clara’s C', 29: 'the Queen’s D', 30: 'the Queen’s E', 31: 'the Queen’s F', 32: 'the Queen’s G' };
const SF_LINES = [['row 1', [0, 1, 2]], ['row 2', [3, 4, 5]], ['row 3', [6, 7, 8]], ['column 1', [0, 3, 6]], ['column 2', [1, 4, 7]], ['column 3', [2, 5, 8]], ['corner to corner, from the top left', [0, 4, 8]], ['corner to corner, from the top right', [2, 4, 6]]];
function sfBingoWin(card, calls) {
  const on = new Set();
  for (let i = 0; i < calls.length; i++) { on.add(card.indexOf(calls[i])); const lines = SF_LINES.filter(([, c]) => c.every(j => on.has(j))).map(([n]) => n); if (lines.length) return { at: i + 1, lines }; }
  return null;
}
const sfLS = (d, clef = 'treble') =>""", 'bingo helpers')
rep("""    <Part kind="play" title="Note bingo" how="Someone names (or plays) one of the nine notes. Find it and colour it. Three in a row -- across, down or corner to corner -- wins!">
      <div style={{display:'grid',gridTemplateColumns:'repeat(3, 1fr)',gap:8,maxWidth:520,margin:'0 auto',width:'100%'}}>
        {W.s6.bingo.map((d, i) => <div key={i} style={{border:'1.6px solid ' + BK.ink,borderRadius:10,padding:'4px 10px'}}><PaperStaff clef={d >= 28 ? 'treble' : 'bass'} notes={[{ d }]} width={130} minSpan={d >= 28 ? [39, 27] : [29, 17]}/></div>)}
      </div>
    </Part>""",
    """    <Part kind="play" title="Bingo on your own" how="Read the calls in order. Find each note on the card and colour it. The first three in a row -- across, down or corner to corner -- is BINGO! Write the number of the call that made it.">
      <div style={{display:'grid',gridTemplateColumns:'1fr 184px',gap:18,alignItems:'center'}}>
        <div style={{display:'grid',gridTemplateColumns:'repeat(3, 1fr)',gap:8}}>
          {W.s6.bingo.map((d, i) => <div key={i} style={{border:'1.6px solid ' + BK.ink,borderRadius:10,padding:'4px 8px'}}><PaperStaff clef={d >= 28 ? 'treble' : 'bass'} notes={[{ d }]} width={130} minSpan={d >= 28 ? [39, 27] : [29, 17]}/></div>)}
        </div>
        <div>
          <div style={{fontSize:12,fontWeight:900,color:BK.coral,letterSpacing:'0.06em',marginBottom:5}}>THE CALLS</div>
          <div style={{display:'grid',gap:4}}>{W.s6.calls.map((d, i) => <div key={i} style={{display:'flex',alignItems:'center',gap:8,fontSize:13.5,color:BK.ink,fontWeight:700}}><span style={{width:20,height:20,borderRadius:10,background:BK.soft,display:'inline-flex',alignItems:'center',justifyContent:'center',fontSize:11,fontWeight:900,color:BK.coral}}>{i + 1}</span>{SF_CALL[d]}</div>)}</div>
          <div style={{display:'flex',alignItems:'center',gap:8,marginTop:12,fontSize:13.5,fontWeight:900,color:BK.ink}}>BINGO on call {bkBox(44, 34)}</div>
        </div>
      </div>
    </Part>""", 'solo bingo')

# (2) Clara visits: a third pair fills the page
rep("""        {visit('One step down from Clara: draw B', 'bass', 'king')}
      </div>""", """        {visit('One step down from Clara: draw B', 'bass', 'king')}
        {visit('Two steps up from Clara: draw E', 'treble', 'queen')}
        {visit('Two steps down from Clara: draw A', 'bass', 'king')}
      </div>""", 'clara visits E and A')

# (4) how-lines: what to do (the book page beside it teaches)
rep("""how="A treble clef starts on the G line -- the Queen's house, in coral -- and spirals out. Trace the faint ones.\"""",
    """how="Start on the coral G line and spiral out. Trace the three faint ones.\"""", 'how treble')
rep("""how="A bass clef starts with a dot on the F line -- the King's house, in coral -- curls down, then the two guards: one above the F line and one below.\"""",
    """how="Start with the dot on the coral F line, curl down, then add the two guards -- one above the line, one below. Trace the three faint ones.\"""", 'how bass')
rep("""<Part kind="together" title="Circle every middle C" how="Clara's note sits on its own little ladder rung -- just under the Queen's staff, or just over the King's. Same key!">""",
    """<Part kind="together" title="Circle every middle C" how="Find Clara's C on both staves and circle it. Some notes near her are not C -- look closely!">""", 'how middle C')

# (5) every step page ends like chapters 1-3: How did it feel? + Checked (the faces were missing in chapter 4)
import re
body_start = s.index('function SfWorkbook(')
body_end = s.index('function SfPaperCheck(')
body = s[body_start:body_end]
n_before = body.count('    </Part>\n  </>);')
body = body.replace('    </Part>\n  </>);', '    </Part>\n    <Faces/>\n  </>);')
if n_before != 6: raise SystemExit('faces: expected 6 step pages, got %d' % n_before)
s = s[:body_start] + body + s[body_end:]
# (6) the room left in the play boxes goes to bigger drawings, not blank (fill the page)
rep("""      <Lead max={400}><KebabSandwich/></Lead>
      {singles(W.s1.tog, 380, 'none', true)}""", """      <Lead max={540}><KebabSandwich/></Lead>
      {singles(W.s1.tog, 380, 'none', true)}""", 'p2 legend bigger')
rep("""        {sfPlate('Skewer plate · line notes', <SfRow width={170} notes={[]} minSpan={[29, 39]} items={[[44, 'line 1'], [86, 'line 3'], [128, 'line 5']].map(([x, label]) => ({ x, label }))}/>)}
        {sfPlate('Sandwich plate · space notes', <SfRow width={170} notes={[]} minSpan={[29, 39]} items={[[44, 'space 1'], [86, 'space 2'], [128, 'space 4']].map(([x, label]) => ({ x, label }))}/>)}""",
    """        {sfPlate('Skewer plate · line notes', <SfRow width={132} notes={[]} minSpan={[29, 39]} items={[[30, 'line 1'], [66, 'line 3'], [102, 'line 5']].map(([x, label]) => ({ x, label }))}/>)}
        {sfPlate('Sandwich plate · space notes', <SfRow width={132} notes={[]} minSpan={[29, 39]} items={[[30, 'space 1'], [66, 'space 2'], [102, 'space 4']].map(([x, label]) => ({ x, label }))}/>)}""", 'p2 plates bigger')
rep("""      <SfRow width={420} notes={[{ d: W.s2.stair.start, x: 40, color: BK.coral }]} minSpan={[29, 39]}
        items={W.s2.stair.moves.map((mv, i) => ({ x: 40 + (i + 1) * 72, label: SF_MOVE[mv.m] }))}/>""",
    """      <SfRow width={360} notes={[{ d: W.s2.stair.start, x: 34, color: BK.coral }]} minSpan={[29, 39]}
        items={W.s2.stair.moves.map((mv, i) => ({ x: 34 + (i + 1) * 60, label: SF_MOVE[mv.m] }))}/>""", 'p3 staircase bigger')
rep("""      {SF_QUEEN_TUNES.map((tu, k) => { const xs = sfXs(tu.notes.length, 400, true); return <div key={k} style={{marginTop:k ? 8 : 0}}>""",
    """      {SF_QUEEN_TUNES.map((tu, k) => { const xs = sfXs(tu.notes.length, 360, true); return <div key={k} style={{marginTop:k ? 8 : 0}}>""", 'p4 tunes xs')
rep("""        <SfRow clef="treble" width={400} notes={[]} minSpan={[27, 34]} items={xs.map((x, i) => ({ x, ex: true, ans: dName(tu.notes[i]), w: 34 }))}/>""",
    """        <SfRow clef="treble" width={360} notes={[]} minSpan={[27, 34]} items={xs.map((x, i) => ({ x, ex: true, ans: dName(tu.notes[i]), w: 34 }))}/>""", 'p4 tunes bigger')
# the F maze gets a fourth row of stones
rep("""    let r = rnd(0, 2); const path = [[r, 0]];
    for (let c = 1; c < 5; c++) { r = Math.max(0, Math.min(2, r + rnd(-1, 1))); path.push([r, c]); }
    const grid = Array.from({ length: 3 }, () => Array.from({ length: 5 }, () => rnd(25, 28)));""",
    """    let r = rnd(0, 3); const path = [[r, 0]];
    for (let c = 1; c < 5; c++) { r = Math.max(0, Math.min(3, r + rnd(-1, 1))); path.push([r, c]); }
    const grid = Array.from({ length: 4 }, () => Array.from({ length: 5 }, () => rnd(25, 28)));""", 'p5 maze 4 rows')
# the secret message: the three short words' boxes on one line (the bass staff is shorter)
rep("""      <div style={{display:'grid',gridTemplateColumns:'1fr 1fr 1fr',gap:'4px 14px'}}>
        {SF_MSG.slice(0, 3)""", """      <div style={{display:'grid',gridTemplateColumns:'1fr 1fr 1fr',gap:'4px 14px',alignItems:'end'}}>
        {SF_MSG.slice(0, 3)""", 'p7 message align')

rep("""<PaperStaff clef="bass" notes={[{ d }]} width={76} minSpan={[29, 17]}/></div>))}</BkGrid></div>""",
    """<PaperStaff clef="bass" notes={[{ d }]} width={84} minSpan={[29, 17]}/></div>))}</BkGrid></div>""", 'p5 maze cells')
rep("""    <PaperStaff clef={clef} notes={[]} width={150} minSpan={clef === 'treble' ? [27, 39] : [17, 29]}/>
  </div>;""", """    <PaperStaff clef={clef} notes={[]} width={172} minSpan={clef === 'treble' ? [27, 39] : [17, 29]}/>
  </div>;""", 'p6 visit staves')

# the check-up page opens like chapters 1-3's: straight onto 'On paper' (no lesson-step strip, no code)
rep("""  P(<>
    <WbTop step={6}/>
    <SfPaperCheck/>
  </>);""", """  P(<>
    <SfPaperCheck/>
  </>);""", 'paper page head')

# the check-up's staves a little bigger, to fill its page
i0 = s.index('function SfPaperCheck() {'); i1 = s.index('\n}\n', i0)
body = s[i0:i1]
if body.count('480') != 6: raise SystemExit('paper widths %d' % body.count('480'))
body = body.replace('480', '436').replace('const pcs = [70, 180, 290, 400];', 'const pcs = [64, 164, 264, 364];')
s = s[:i0] + body + s[i1:]

# the Teacher copy follows
rep("""'D just under line 1 of the treble staff', 'B just over line 5 of the bass staff'])}</>}""",
    """'D just under line 1 of the treble staff', 'B just over line 5 of the bass staff', 'E on line 1 of the treble staff', 'A on line 5 of the bass staff'])}</>}""", 'tc visits')
rep("""{tcAns('BINGO CARD', W.s6.bingo.map(d => withSolfa(dName(d)) + (d === 28 ? ' (middle C)' : '')))}</>}
      watch="In bingo, F and G live in both palaces: the treble F/G are high, the bass F/G low. Call them by palace: “the Queen's G”, “the King's F”."
      say="“Which palace? Then which friend is nearest?”"/>""",
    """{tcAns('BINGO', ['call ' + W.s6.win.at + ' (' + SF_CALL[W.s6.calls[W.s6.win.at - 1]] + '): ' + W.s6.win.lines[0]])}</>}
      watch="In bingo, F and G live in both palaces: the call says whose -- the Queen's G is on her staff (high), the King's G on his (low)."
      say="“Whose palace? Then which friend is nearest?”"/>""", 'tc bingo')

open(src, 'w', encoding='utf-8').write(s); print('patch414 ok')
