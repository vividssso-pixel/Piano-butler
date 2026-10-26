import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build AI-3: 6/8 Time, the Workbook and teacher's copy. Pages 2 to 6 face the Lesson Book's steps; page 7, facing My five
# checks, is the check-up on paper. The rows are the room's own (E8, E8_FILL), the counts worked out by its rq68Count.
CODE = r'''
// ─── Chapter: 6/8 Time, the Workbook and teacher's copy (Build AI-3) ───
const E8_WB = {
  strong: ['big', 'm3'],                                         // circle the notes on 1 and 4
  len: ['e', 'q', 'qd', 'hd'],                                   // how many quavers?
  count: [['ls', 1], ['m2', 2], ['ls2', 6], ['m1', 4], ['m2', 7], ['ls', 3]],   // on which count does the coral note start?
  fill: [0, 1, 2, 3],                                            // E8_FILL: which note fills the bar?
  see: ['t34', 'big', 'big', 't34'],                             // 3/4 or 6/8, by the beams
  write: ['m1', 'm2'],                                           // write the counts under the notes
  chk: { len: ['qd', 'e', 'hd', 'q'], count: [['m1', 3], ['ls2', 3], ['m2', 5], ['dot', 1]], see: ['big', 't34', 't34', 'big'], fill: [5, 2, 1, 4] },
};
const e8wCountOf = (row, i) => rq68Count(srhSounds(E8[row])[i].b);
const e8wCounts = (row) => srhSounds(E8[row]).map((x, j, A) => (j && Math.floor(x.b / 3) !== Math.floor(A[j - 1].b / 3) ? '| ' : '') + rq68Count(x.b)).join(' ');
// which notes fall on 1 or 4, bar by bar ('bar 1: notes 1 and 4; bar 2: note 1')
const e8wStrong = (row) => { const S = srhSounds(E8[row]), bars = {}; S.forEach(x => { const k = Math.floor(x.b / 3); (bars[k] = bars[k] || []).push(x); });
  return Object.keys(bars).map(k => { const on = bars[k].map((x, j) => (['1', '4'].includes(rq68Count(x.b)) ? j + 1 : 0)).filter(Boolean); return 'bar ' + (+k + 1) + ': note' + (on.length > 1 ? 's ' : ' ') + on.join(' and '); }).join('; '); };
const E8W_LEN = { e: 1, q: 2, qd: 3, hd: 6 };
const e8wGlyph = (k, size = 54) => <Glyph item={{ e: NV_NOTES[3], q: NV_NOTES[2], qd: NV_DOTTED[1], hd: NV_DOTTED[0] }[k]} size={size}/>;
const e8wRow = (items, o = {}) => <div style={{width:'100%',maxWidth:o.mw || 560,margin:'0 auto'}}>{rqStaffEl(items, { counts: false, hearts: false, ...o })}</div>;
const e8wSee = (row) => E8[row].filter(it => it[0] !== 'ts').slice(0, row === 't34' ? 3 : 2).concat([['||']]);
function E8Workbook({ startNo = 1 }) {
  const W = E8_WB, pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + 1 + pages.length} chId="six-eight">{content}</WbPage>);
  const line = (n, label, box) => <span style={{display:'inline-flex',alignItems:'center',gap:8}}>{nvNum(n)} {label} {box}</span>;
  const nums = (lab, n) => <div style={{display:'flex',alignItems:'flex-end',gap:18}}><span style={{display:'inline-flex',alignItems:'baseline',gap:8,width:70}}>{nvNum(n)}<span style={{fontFamily:LB_SERIF,fontSize:22,fontWeight:900,color:BK.ink}}>{lab}</span></span>
    <div style={{display:'flex',gap:16,fontSize:24,fontWeight:900,color:BK.ink,padding:'26px 10px 0',letterSpacing:'0.08em'}}>{[1, 2, 3, 4, 5, 6].map(x => <span key={x} style={{width:26,textAlign:'center'}}>{x}</span>)}</div></div>;

  // 2 (faces "Two big beats")
  P(<>
    <WbTop step={1}/>
    <Part kind="together" title="Find the big beats" how="The counts are under the notes. Circle every note that falls on 1 or 4: the two big beats in each bar.">
      <div style={{display:'grid',gap:10}}>{W.strong.map((row, i) => <ExCell key={row} n={i + 1} ex={i === 0}><div style={{padding:'18px 6px 4px'}}>{e8wRow(E8[row], { ...E8P.so, counts: undefined, lit: i === 0 ? [0, 3, 6, 9] : undefined })}</div></ExCell>)}</div>
    </Part>
    <Part kind="home" title="Two big beats this week" how="Do each one and tick a box each day.">
      <PhLog rows={['Clap six quavers, saying 1 2 3 4 5 6, with 1 and 4 louder', 'Clap only 1 and 4 while you say all six', 'Walk the big beats while someone claps the quavers']} label={300}/>
    </Part>
    <Part kind="play" title="Six or two?" how="Say the counts and tap your knees: both hands on 1 and 4, one finger on the others. Then try it with your eyes closed. How many bars can you do without stopping?">
      <div style={{display:'flex',justifyContent:'center',gap:14,alignItems:'center',padding:'14px 0',fontSize:14,fontWeight:800,color:BK.ink}}>
        {[1, 2, 3, 4, 5, 6].map(x => <span key={x} style={{width:44,height:44,borderRadius:22,border:'2px solid ' + (x === 1 || x === 4 ? BK.coral : BK.ink),background:x === 1 || x === 4 ? '#fbe3da' : '#fff',display:'inline-flex',alignItems:'center',justifyContent:'center',fontSize:20,fontWeight:900,color:BK.ink}}>{x}</span>)}
        <span style={{marginLeft:16}}>bars without stopping:</span>{bkBox(56, 34)}</div>
    </Part>
    <Faces/>
  </>);

  // 3 (faces "The dotted crotchet")
  P(<>
    <WbTop step={2}/>
    <Part kind="together" title="How many quavers?" how="In 6/8 we count quavers. Write how many quavers each note lasts.">
      <BkGrid cols={4} gap="6px 10px">{W.len.map((k, i) => <ExCell key={k} n={i + 1} ex={i === 0}><div style={{display:'grid',gap:4,justifyItems:'center',padding:'16px 2px 4px'}}>{e8wGlyph(k, 70)}{nvBox(i === 0, String(E8W_LEN[k]), 44, 30)}</div></ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Count inside the long note" how="Clap this row each day, counting out loud: 1 (2 3), 4 (5 6). Hold the dotted crotchet for all three counts.">
      {e8wRow(E8.dot, { ...E8P.so, counts: undefined })}
      <PhLog rows={['Clapped the row, counting out loud', 'Played it on one note, holding each dotted crotchet']} label={300}/>
    </Part>
    <Part kind="play" title="Note sums" how="Add up the quavers. Write the answer as a number, then draw the one note that lasts that long.">
      <div style={{display:'grid',gap:16,justifyItems:'center',padding:'10px 0',fontSize:24,fontWeight:900,color:BK.ink}}>
        {[[['e', 'e', 'e'], 5], [['q', 'e'], 6], [['qd', 'qd'], 7]].map(([ks, n]) => <span key={n} style={{display:'flex',alignItems:'center',gap:10}}>{nvNum(n)}{ks.map((k, j) => <React.Fragment key={j}>{j > 0 && <span>+</span>}{e8wGlyph(k, 46)}</React.Fragment>)}<span>=</span>{bkBox(48, 36)}<span style={{fontSize:13,color:BK.muted}}>quavers, the note:</span>{bkBox(60, 52)}</span>)}
      </div>
    </Part>
    <Faces/>
  </>);

  // 4 (faces "Long, short")
  P(<>
    <WbTop step={3}/>
    <Part kind="together" title="On which count?" how="Count every quaver, 1 2 3 4 5 6. On which count does the coral note start?">
      <BkGrid cols={2} gap="6px 10px">{W.count.map(([row, i], k) => <ExCell key={k} n={k + 1} ex={k === 0}><div style={{display:'grid',gap:4,padding:'18px 4px 4px'}}>{e8wRow(E8[row], { ...E8P.so, counts: false, lit: i, mw: 300 })}
        <div style={{display:'flex',alignItems:'center',justifyContent:'center',gap:8,fontSize:11.5,fontWeight:800,color:BK.ink}}>count {nvBox(k === 0, e8wCountOf(row, i), 40, 28)}</div></div></ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Long, short this week" how="Tick a box each day.">
      <PhLog rows={['Say 1 (2) 3, 4 (5) 6, then tap long-short', 'Clap both long-short rows from the Lesson Book', 'Play them on one note, the crotchet held for two counts']} label={300}/>
    </Part>
    <Part kind="play" title="Fill the bar" how="Each bar of 6/8 holds six quavers. Draw the one note that fills the box: a quaver, a crotchet or a dotted crotchet.">
      <BkGrid cols={2} gap="10px 14px">{W.fill.map((f, i) => <div key={i} style={{display:'grid',gridTemplateColumns:'auto 1fr',alignItems:'center',gap:6}}>{nvNum(5 + i)}{e8wRow([['ts', 6, 8]].concat(E8_FILL[f][0], [['||']]), { mw: 210 })}</div>)}</BkGrid>
    </Part>
    <Faces/>
  </>);

  // 5 (faces "3/4 or 6/8?")
  P(<>
    <WbTop step={4}/>
    <Part kind="together" title="3/4 or 6/8?" how="Six quavers, no time signature. Look at the beams: in twos is 3/4 (three beats), in threes is 6/8 (two big beats). Write the time signature.">
      <BkGrid cols={2} gap="6px 10px">{W.see.map((row, i) => <ExCell key={i} n={i + 1} ex={i === 0}><div style={{display:'grid',gap:4,padding:'18px 4px 4px'}}>{e8wRow(e8wSee(row), { mw: 260 })}
        <div style={{display:'flex',alignItems:'center',justifyContent:'center',gap:8,fontSize:11.5,fontWeight:800,color:BK.ink}}>time signature {nvBox(i === 0, row === 't34' ? '3/4' : '6/8', 48, 28)}</div></div></ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Listen this week" how="Ask someone to clap six quavers again and again, loud on every second one (3/4) or every third one (6/8). Say which. Tick a box when you are right.">
      <PhLog rows={['3/4 or 6/8, by ear', 'Now you clap and they say', 'Count both out loud: 1 2, 3 4, 5 6 and 1 2 3, 4 5 6']} label={300}/>
    </Part>
    <Part kind="play" title="Two ways to group six" how="The same six counts. Draw a bracket over each beat: in twos for 3/4, in threes for 6/8. Then circle the count where each beat starts.">
      <div style={{display:'grid',gap:20,justifyItems:'center',padding:'10px 0'}}>{nums('3/4', 5)}{nums('6/8', 6)}</div>
    </Part>
    <Faces/>
  </>);

  // 6 (faces "Count, clap, play")
  P(<>
    <WbTop step={5}/>
    <Part kind="together" title="Write the counts" how="Write the count each note starts on, under the note (1 to 6). Then say them, clap, and play on one note.">
      <div style={{display:'grid',gap:12}}>{W.write.map((row, i) => <ExCell key={row} n={i + 1} ex={i === 0}><div style={{padding:'18px 6px 22px'}}>{e8wRow(E8[row], { ...E8P.so, counts: i === 0 ? undefined : false })}</div></ExCell>)}</div>
    </Part>
    <Part kind="home" title="New lines this week" how="The same order every time: say the counts, clap, play. Tick a box each day.">
      <PhLog rows={['Line 1', 'Line 2', 'The long-short rows', 'The dotted minim row: one note for the whole bar']} label={300}/>
    </Part>
    <Part kind="play" title="Write your own" how="Two bars of 6/8. In each box (one big beat) draw three quavers, a dotted crotchet, or a crotchet and a quaver. Write the counts, then clap it.">
      {e8wRow([['ts', 6, 8], ['box', 1.5], ['box', 1.5], ['|'], ['box', 1.5], ['box', 1.5], ['||']], { mw: 560 })}
    </Part>
    <Faces/>
  </>);

  // 7. the check-up on paper (faces My five checks)
  P(<E8PaperCheck/>);
  return <>{pages}</>;
}
function E8PaperCheck() {
  const C = E8_WB.chk;
  return <div className="lb-paper" style={{display:'flex',flexDirection:'column',gap:4}}>
    <LbPaperHead/>
    {bkSec('A', 'In 6/8, how many quavers does each note last?')}
    <BkGrid cols={4} gap="6px 8px">{C.len.map((k, i) => <BkCell key={k} n={i + 1}><div style={{display:'flex',alignItems:'center',justifyContent:'center',gap:10,padding:'14px 2px 2px'}}>{e8wGlyph(k, 54)}{bkBox(36, 26)}</div></BkCell>)}</BkGrid>
    {bkSec('B', 'On which count does the coral note start?')}
    <BkGrid cols={2} gap="6px 8px">{C.count.map(([row, i], k) => <BkCell key={k} n={k + 5}><div style={{display:'grid',gap:3,padding:'14px 2px 2px'}}>{e8wRow(E8[row], { ...E8P.so, counts: false, lit: i, mw: 280 })}<div style={{display:'flex',justifyContent:'center'}}>{bkBox(36, 26)}</div></div></BkCell>)}</BkGrid>
    {bkSec('C', '3/4 or 6/8? Look at the beams.')}
    <BkGrid cols={4} gap="6px 8px">{C.see.map((row, i) => <BkCell key={i} n={i + 9}><div style={{display:'grid',gap:3,padding:'14px 2px 2px'}}>{e8wRow(e8wSee(row), { mw: 150 })}<div style={{display:'flex',justifyContent:'center'}}>{bkBox(44, 26)}</div></div></BkCell>)}</BkGrid>
    {bkSec('D', 'Draw the note that fills the bar.')}
    <BkGrid cols={2} gap="6px 8px">{C.fill.map((f, i) => <BkCell key={i} n={i + 13}><div style={{padding:'14px 2px 2px'}}>{e8wRow([['ts', 6, 8]].concat(E8_FILL[f][0], [['||']]), { mw: 200 })}</div></BkCell>)}</BkGrid>
  </div>;
}
function E8Teacher() {
  const W = E8_WB, C = W.chk, pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="six-eight" teacher>{content}</WbPage>);
  const nm = (k) => ({ e: 'quaver', q: 'crotchet', qd: 'dotted crotchet', hd: 'dotted minim' })[k];
  P(<>
    <div style={{fontFamily:LB_SERIF,fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('six-eight')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 12px',lineHeight:1.5}}>Each workbook page faces its Lesson Book page. 6/8 is a Grade 1 time signature (with or without an anacrusis). Count every quaver while learning; feel the two big beats once it is easy. Clapping and playing are checked at the piano, counting out loud.</div>
    <TcBlock page={2} title="Two big beats" answers={<>{tcAns('TRY IT', W.strong.map(row => e8wStrong(row)))}{tcAns('PLAY', ['any number of bars, both hands on 1 and 4 only'])}</>}
      watch="Hearing 6/8 as three in a bar (1 3 5 strong). Say 1 2 3, 4 5 6 with 1 and 4 louder."
      say="“Six quavers, two big beats: 1 and 4.”"/>
    <TcBlock page={3} title="The dotted crotchet" answers={<>{tcAns('TRY IT', W.len.map(k => nm(k) + ' ' + E8W_LEN[k]))}{tcAns('PLAY', ['3, a dotted crotchet', '3, a dotted crotchet', '6, a dotted minim'], 5)}</>}
      watch="Holding the dotted crotchet for one count only: in 6/8 it is a whole big beat (three quavers). In 2/4, 3/4 and 4/4 it was a beat and a half."
      say="“Dotted crotchet: three quavers, one big beat.”"/>
    <TcBlock page={4} title="Long, short" answers={<>{tcAns('TRY IT', W.count.map(([row, i]) => e8wCountOf(row, i)))}{tcAns('PLAY', W.fill.map(f => nm(E8_FILL[f][1])), 5)}</>}
      watch="Giving the crotchet one count: in 6/8 it lasts two quavers (1, 3; 4, 6)."
      say="“Crotchet and quaver make one big beat: long, short.”"/>
  </>);
  P(<>
    <TcBlock page={5} title="3/4 or 6/8?" answers={<>{tcAns('TRY IT', W.see.map(row => (row === 't34' ? '3/4 (in twos)' : '6/8 (in threes)')))}{tcAns('PLAY', ['3/4: [1 2] [3 4] [5 6], beats start on 1, 3, 5', '6/8: [1 2 3] [4 5 6], beats start on 1 and 4'], 5)}</>}
      watch="Counting the quavers (six either way) instead of looking at how they are grouped."
      say="“3/4: in twos, three beats. 6/8: in threes, two big beats.”"/>
    <TcBlock page={6} title="Count, clap, play" answers={<>{tcAns('TRY IT', W.write.map(row => e8wCounts(row)))}{tcAns('PLAY', ['any two bars that fill 6/8: each box is three quavers long'])}</>}
      watch="Skipping the counting step and clapping by guess. Every new line in the same order: counts out loud, clap, then play."
      say="“Find the counts, say them, clap, play.”"/>
    <TcBlock page={7} title="The check-up on paper (the Workbook's last page)" answers={<>{tcAns('A', C.len.map(k => String(E8W_LEN[k])))}{tcAns('B', C.count.map(([row, i]) => e8wCountOf(row, i)), 5)}{tcAns('C', C.see.map(row => (row === 't34' ? '3/4' : '6/8')), 9)}{tcAns('D', C.fill.map(f => nm(E8_FILL[f][1])), 13)}
      <div style={{fontSize:12,color:BK.ink,marginTop:6,lineHeight:1.5}}>One mark for each answer. Score each part on its own (4 marks each, pass 3+). Not passed? Go back to that step's page: A p.3 · B p.4 · C p.5 · D p.4. Then clap it at the piano, counting out loud.</div></>}/>
  </>);
  return <>{pages}</>;
}
WORKBOOKS['six-eight'] = E8Workbook;
TEACHER_COPIES['six-eight'] = E8Teacher;
'''
rep("""function SixEightLessonBook() { return <>{e8LbPages(false)}</>; }""",
    """function SixEightLessonBook() { return <>{e8LbPages(false)}</>; }""" + CODE)
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
