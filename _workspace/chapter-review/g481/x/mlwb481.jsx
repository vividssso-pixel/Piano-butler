// ─── Phase 481: chapter 25's Workbook (pages 2 to 8: one per lesson step, my piece's melody, the check-up) and the
// Teacher copy (they replace the Phase 117 ones). Chapter 21's ivxTicks and chapter 22's chxCircle are reused.
const mB = (sh, s) => mlxBar(sh, s), mW = (d) => [['w', 4, d]];
const MLX_WB = {
  // which line? two-bar tunes; each with its three lines: [own | mirror | another tune's (index)]
  try2: [[mB([0, 2, 1, 3], 28), mB([0, 2, 1, 3], 29)], [mB([3, 2, 1, 0], 30), mB([2, 1, 0, 1], 28)], [mB([0, 1, 2, 0], 29), mB([0, 1, 2, 0], 30)], [mB([2, 0, 1, 0], 30), mB([1, 0, 1, 2], 28)]],
  try2opts: [['a', 'm', 2], [3, 'a', 'm'], ['m', 0, 'a'], [1, 'm', 'a']],
  // draw the line, circle the high point (the A in bar 2; the A in bar 2)
  turn2: [[mB([0, 2, 1, 3], 28), mB([0, 2, 1, 3], 30), mB([3, 2, 1, 0], 29), mW(28)], [mB([2, 1, 0, 1], 30), mB([3, 2, 1, 0], 30), mB([0, 1, 0, 2], 28), mW(28)]],
  // phrasing: high points G (bar 3), A (bar 1), A (bar 2)
  try3: [MLX_Q, [mB([0, 1, 2, 0], 28), mB([0, 1, 2, 0], 29), mB([0, 1, 2, 0], 30), mW(29)], [mB([3, 2, 1, 0], 30), mB([2, 0, 1, 0], 29), mB([0, 1, 0, 2], 28), mW(28)], [mB([1, 0, 1, 2], 29), mB([1, 0, 1, 2], 31), mB([2, 1, 0, 1], 29), mW(28)]],
  // hairpins: high points A (bar 2), A (bar 3)
  turn3: [[mB([0, 2, 1, 3], 29), mB([0, 2, 1, 3], 30), mB([2, 1, 0, 1], 29), mW(29)], [mB([0, 1, 2, 0], 28), mB([1, 0, 1, 2], 30), mB([3, 2, 1, 0], 30), mW(28)]],
  // question or answer: answer (done), question, answer, question
  try4: [MLX_A, [mB([0, 2, 1, 3], 28), mB([0, 2, 1, 3], 29), mB([3, 2, 1, 0], 29), mW(32)], [mB([0, 2, 0, 1], 28), mB([3, 2, 1, 0], 30), mB([2, 1, 0, 1], 28), mW(28)], [mB([0, 1, 2, 0], 28), mB([0, 1, 2, 0], 29), mB([1, 0, 1, 2], 29), mW(32)]],
  // write the answer's last bar: two questions, each with its answer's bars 5 to 7
  turn4: [[MLX_Q, MLX_A.slice(0, 3)], [[mB([0, 1, 2, 0], 28), mB([0, 1, 2, 0], 29), mB([3, 2, 1, 0], 30), mW(29)], [mB([0, 1, 2, 0], 28), mB([0, 1, 2, 0], 29), mB([2, 1, 0, 1], 29)]]],
  // bracket the motif: bars it comes back in (2 and 4; 3 and 4; 2 and 3; 4)
  try5: [[mB([0, 2, 1, 3], 28), mB([0, 2, 1, 3], 29), mB([3, 2, 1, 0], 30), mB([0, 2, 1, 3], 28)], [mB([0, 1, 2, 0], 29), mB([2, 1, 0, 1], 28), mB([0, 1, 2, 0], 29), mB([0, 1, 2, 0], 28)],
    [mB([3, 2, 1, 0], 30), mB([3, 2, 1, 0], 29), mB([3, 2, 1, 0], 28), mB([0, 2, 0, 1], 28)], [mB([1, 0, 1, 2], 28), mB([0, 2, 1, 3], 29), mB([2, 0, 1, 0], 30), mB([1, 0, 1, 2], 29)]],
  try5ans: [[2, 4], [3, 4], [2, 3], [4]],
  // count the motif: 8 bars (5 times), 4 bars (3 times)
  turn5: [[mB([0, 1, 2, 0], 28), mB([0, 1, 2, 0], 29), mB([0, 1, 2, 0], 30), mW(32), mB([0, 1, 2, 0], 28), mB([0, 1, 2, 0], 29), mB([2, 1, 0, 1], 29), mW(28)], [mB([2, 1, 0, 1], 30), mB([2, 1, 0, 1], 29), mB([2, 1, 0, 1], 28), mW(28)]],
  turn5ans: [5, 3],
  // repetition or sequence: up (done), repetition, down, up
  try6: [[mB([0, 2, 1, 3], 28), 'up'], [mB([3, 2, 1, 0], 30), 'rep'], [mB([0, 1, 2, 0], 30), 'down'], [mB([1, 0, 1, 2], 28), 'up']],
  // write the sequence: two bars a step higher each; two bars a step lower each
  turn6: [[mB([0, 2, 1, 3], 28), 'up'], [mB([3, 2, 1, 0], 30), 'down']],
};
const MLX_CHK = {
  line: [[mB([0, 1, 0, 2], 28), mB([0, 1, 0, 2], 29)], [mB([3, 2, 1, 0], 30), mB([0, 2, 1, 3], 28)]],
  lineOpts: [['m', 'a', 1], ['a', 0, 'm']],
  qa: [[mB([0, 1, 2, 0], 28), mB([2, 1, 0, 1], 29), mB([0, 1, 2, 0], 29), mW(32)], [mB([0, 2, 1, 3], 28), mB([2, 1, 0, 1], 29), mB([3, 2, 1, 0], 30), mW(28)], [mB([0, 2, 0, 1], 28), mB([1, 0, 1, 2], 29), mB([2, 1, 0, 1], 29), mW(32)]],
  word: ['motif', 'sequence', 'contour', 'answer phrase'],
  rs: [[mB([2, 0, 1, 0], 30), 'down'], [mB([0, 2, 0, 1], 28), 'rep'], [mB([0, 1, 2, 0], 29), 'up']],
};
const mlxChkNo = () => { const C = MLX_CHK, nB = C.line.length + 1, nC = nB + C.qa.length, nD = nC + C.word.length; return { nB, nC, nD, total: nD + C.rs.length - 1 }; };
// a staff row on paper (D 17 by default; bars stacked bar under bar with tsRoom)
const mlxWbRow = (bars, o = {}) => <div style={{width:'100%',maxWidth:o.mw || 9999,margin:'0 auto'}}><MlxRow bars={bars} ts={o.ts !== false} tsRoom={o.tsRoom} end={o.end} D={o.D || 17} marks={o.marks} hair={o.hair} hl={o.hl || []} ring={o.ring} motifs={o.motifs} breath={o.breath} line={o.line} n0={o.n0} tag={o.tag} width={o.w || mlxVbw(bars, o.ts !== false, o.D || 17)} label={o.label || 'A tune.'}/></div>;
const mlxWbLines = (bars, opts, own, ring) => <div style={{display:'grid',gridTemplateColumns:'repeat(3,minmax(0,1fr))',gap:6,marginTop:'auto'}}>{opts.map((o, j) => { const b = o === 'a' || o === 'm' ? bars : own[o], on = ring === j;
  return <div key={j} style={{border:'1.4px solid ' + (on ? BK.coral : BK.hair),borderRadius:on ? 14 : 4,padding:'2px 4px',position:'relative'}}><span style={{position:'absolute',top:1,left:4,fontSize:9.5,fontWeight:900,color:BK.muted}}>{'abc'[j]}</span><MlxLine bars={b} mirror={o === 'm'} w={120} h={40} pad={7} col={on ? BK.coral : PEN_N}/></div>; })}</div>;
const mlxWbWords = (words, on) => <div style={{display:'flex',justifyContent:'center',gap:12,fontSize:13,fontWeight:800,color:BK.ink,margin:'2px 0',flexWrap:'wrap'}}>{words.map(w => <span key={w} style={{border:'1.5px solid ' + (on === w ? BK.coral : 'transparent'),borderRadius:14,padding:'0 8px',color:on === w ? BK.coral : BK.ink}}>{w}</span>)}</div>;
// a staff with given bars, then empty bars to write in
function MlxWrite({ bars, empty = 2, label, D = 17, ts = true, tsRoom, n0, end = true, whole }) {
  const items = (ts ? [['ts', 4]] : tsRoom ? [['sp', 26]] : []).concat(bars.flatMap(b => b.concat([['sp', mlxGap(D)], ['|']])));
  // an empty bar as wide as a bar of four crotchets (or of one whole note, to stand under one)
  const barW = sdyVbw([['ts', 4]].concat(whole ? [['w', 4, 28]] : mlxQ([28, 30, 29, 31]), [['|']]), { D }) - sdyVbw([['ts', 4], ['|']], { D });
  for (let j = 0; j < empty; j++) items.push(['sp', barW - 12], ['sp', mlxGap(D)], j === empty - 1 && end ? ['||'] : ['|']);
  const extra = n0 == null || !bars.length ? null : (yOf, txt, mm) => <text x={mm.notes[0].x - 8} y={yOf(38) - 6} fontSize="11" fontWeight="800" fill={BK.muted} style={{fontFamily:'Inter, sans-serif'}}>{n0}</text>;
  return <SdyStaff width={sdyVbw(items, { D })} items={items} o={{ D }} label={label} extra={extra} room={n0 != null ? 6 : 0}/>;
}
const mlxRsNm = (h) => ({ rep: 'repetition', up: 'sequence up', down: 'sequence down' })[h];

function MlxWorkbook({ startNo = 1 }) {
  const W = MLX_WB, pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + 1 + pages.length} chId="melody">{content}</WbPage>);

  // 2 (faces "The line of a tune")
  P(<>
    <WbTop step={1}/>
    <Part kind="together" title="Which line?" how="Look at the notes. Circle the line that goes where they go. The first one is done.">
      <BkGrid cols={2} gap="8px 10px">{W.try2.map((bars, i) => <ExCell key={i} n={i + 1} ex={i === 0}>{sdyCol(<>{mlxWbRow(bars, { D: 18, mw: 250, end: false })}{mlxWbLines(bars, W.try2opts[i], W.try2, i === 0 ? W.try2opts[0].indexOf('a') : null)}</>, '20px 6px 8px')}</ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Draw the line" how="Draw the tune’s line above its notes: a dot over each note, joined. Then circle the high point.">
      <BkGrid cols={1} gap="8px">{W.turn2.map((bars, i) => <BkCell key={i} n={i + 5}>{sdyCol(<div style={{paddingTop:52,maxWidth:560,margin:'0 auto',width:'100%'}}>{mlxWbRow(bars, { D: 20 })}</div>, '6px 6px 8px')}</BkCell>)}</BkGrid>
    </Part>
    <Part kind="play" title="Play and draw" how="Play each tune above. Draw its line in the air with your other hand. Tick each.">
      {sskRowN(7, ivxTicks(['tune 5', 'tune 6', 'a piece I know']))}
    </Part>
    <Faces/>
  </>);

  // 3 (faces "Phrasing")
  P(<>
    <WbTop step={2}/>
    <Part kind="together" title="Mark the phrasing" how="Draw the phrase mark under the phrase, circle the high point, and write a breath mark (,) above the staff after the last note, before the next phrase. The first one is done.">
      <BkGrid cols={2} gap="8px 10px">{W.try3.map((bars, i) => <ExCell key={i} n={i + 1} ex={i === 0}>{sdyCol(mlxWbRow(bars, i === 0 ? { end: false, marks: [[0, 3]], ring: [mlxHigh(bars)], breath: true } : { end: false }), '26px 6px 14px')}</ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Louder, softer" how="Circle the high point. Write a crescendo (<) from the first note to it, and a diminuendo (>) from it to the last note.">
      <BkGrid cols={1} gap="8px">{W.turn3.map((bars, i) => <BkCell key={i} n={i + 5}>{sdyCol(<div style={{maxWidth:540,margin:'0 auto',width:'100%'}}>{mlxWbRow(bars, { D: 20, end: false })}<div style={{height:70,borderBottom:'1px dashed ' + BK.hair,margin:'4px 10px 0'}}/></div>, '14px 6px 8px')}</BkCell>)}</BkGrid>
    </Part>
    <Part kind="play" title="Play it shaped" how="Play phrases 5 and 6 with your marks: louder to the high point, softer to the end, then a breath. Tick each.">
      {sskRowN(7, ivxTicks(['phrase 5', 'phrase 6', 'with a breath']))}
    </Part>
    <Faces/>
  </>);

  // 4 (faces "Question and answer")
  P(<>
    <WbTop step={3}/>
    <Part kind="together" title="Question or answer?" how="Look at the last note. Circle question or answer. The first one is done.">
      <BkGrid cols={2} gap="8px 10px">{W.try4.map((bars, i) => { const a = mlxFlat(bars).slice(-1)[0][2] === 28;
        return <ExCell key={i} n={i + 1} ex={i === 0}>{sdyCol(<>{mlxWbRow(bars, { end: false, hl: i === 0 ? [mlxCount(bars) - 1] : [] })}<div style={{marginTop:'auto'}}>{mlxWbWords(['question', 'answer'], i === 0 ? (a ? 'answer' : 'question') : null)}</div></>, '18px 6px 5px')}</ExCell>; })}</BkGrid>
    </Part>
    <Part kind="home" title="Write the answer’s end" how="Each question is followed by its answer. Write the answer’s last note in bar 8: a whole note on the tonic.">
      <BkGrid cols={1} gap="8px">{W.turn4.map(([q, a], i) => <BkCell key={i} n={i + 5}>{sdyCol(<div style={{display:'flex',flexDirection:'column',gap:4,maxWidth:450,margin:'0 auto',width:'100%'}}>{mlxWbRow(q, { end: false, n0: 1, D: 18, tag: 'question' })}<MlxWrite bars={a} empty={1} ts={false} tsRoom whole D={18} n0={5} label={'The answer: bars 5 to 7, then an empty bar 8.'}/></div>, '14px 6px 8px')}</BkCell>)}</BkGrid>
    </Part>
    <Part kind="play" title="Ask and answer" how="Play each question, then its answer. Tick each.">
      {sskRowN(7, ivxTicks(['question and answer 5', 'question and answer 6']))}
    </Part>
    <Faces/>
  </>);

  // 5 (faces "The motif")
  P(<>
    <WbTop step={4}/>
    <Part kind="together" title="Bracket the motif" how="Bar 1 is the motif. Draw a bracket over every bar where it comes back, the same or a step higher or lower. The first one is done.">
      <BkGrid cols={2} gap="8px 10px">{W.try5.map((bars, i) => <ExCell key={i} n={i + 1} ex={i === 0}>{sdyCol(mlxWbRow(bars, { end: false, motifs: [[0, 'motif', true]].concat(i === 0 ? W.try5ans[0].map(b => [b - 1, '', false]) : []) }), '18px 6px 10px')}</ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="How many times?" how="Bar 1 is the motif. Count every bar that is the motif, the same or a step higher or lower, bar 1 too. Write the number.">
      <BkGrid cols={1} gap="8px">{W.turn5.map((bars, i) => <BkCell key={i} n={i + 5}>{sdyCol(<div style={{display:'grid',gridTemplateColumns:'minmax(0,510px) 120px',justifyContent:'center',alignItems:'center',gap:16}}><div>{bars.length > 4 ? <>{mlxWbRow(bars.slice(0, 4), { end: false, n0: 1, motifs: [[0, 'motif', true]], D: 18 })}{mlxWbRow(bars.slice(4), { ts: false, tsRoom: true, n0: 5, D: 18, w: mlxVbw(bars.slice(0, 4), true, 18) })}</> : mlxWbRow(bars, { n0: 1, motifs: [[0, 'motif', true]], D: 18 })}</div>
        <div style={{display:'flex',alignItems:'center',gap:6,fontSize:13,fontWeight:800,color:BK.ink}}>{bkBox(44, 38)} times</div></div>, '12px 8px 8px')}</BkCell>)}</BkGrid>
    </Part>
    <Part kind="play" title="Say “motif”" how="Play tunes 5 and 6. Say “motif” each time it starts. Tick each.">
      {sskRowN(7, ivxTicks(['tune 5', 'tune 6']))}
    </Part>
    <Faces/>
  </>);

  // 6 (faces "Repetition and sequence")
  P(<>
    <WbTop step={5}/>
    <Part kind="together" title="Repetition or sequence?" how="Bar 2 is made from bar 1. Circle repetition, sequence up or sequence down. The first one is done.">
      <BkGrid cols={2} gap="8px 10px">{W.try6.map(([b1, h], i) => <ExCell key={i} n={i + 1} ex={i === 0}>{sdyCol(<>{mlxWbRow([b1, mlxNext(b1, h)], { end: false, mw: 300 })}<div style={{marginTop:'auto'}}>{chxCircle(['repetition', 'sequence up', 'sequence down'], i === 0 ? mlxRsNm(h) : null)}</div></>, '20px 6px 8px')}</ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Write the sequence" how="Bar 1 is the motif. Write it in sequence in bars 2 and 3, each a step higher (5) or a step lower (6).">
      <BkGrid cols={1} gap="8px">{W.turn6.map(([b1, h], i) => <BkCell key={i} n={i + 5}>{sdyCol(<div style={{maxWidth:470,margin:'0 auto',width:'100%'}}><div style={{textAlign:'center',fontSize:13,fontWeight:900,color:BK.ink,margin:'0 0 4px'}}>{h === 'up' ? 'each a step higher ↑' : 'each a step lower ↓'}</div><MlxWrite bars={[b1]} empty={2} end={false} D={20} label={'The motif, then two empty bars.'}/></div>, '14px 6px 10px')}</BkCell>)}</BkGrid>
    </Part>
    <Part kind="play" title="Play your sequences" how="Play sequences 5 and 6. Then make a motif of your own and play it in sequence. Tick each.">
      {sskRowN(7, ivxTicks(['sequence 5', 'sequence 6', 'my own']))}
    </Part>
    <Faces/>
  </>);

  P(<MlxMyPiece/>);
  P(<MlxPaperCheck/>);
  return <>{pages}</>;
}
function MlxMyPiece() {
  const row = (label, node, h = 46) => <div style={{display:'grid',gridTemplateColumns:'130px minmax(0,1fr)',alignItems:'center',gap:10,minHeight:h}}><div style={{fontSize:11.5,fontWeight:900,letterSpacing:'0.08em',textTransform:'uppercase',color:BK.muted}}>{label}</div><div>{node}</div></div>;
  const line = <span style={{display:'inline-block',width:70,borderBottom:'1.3px solid ' + BK.line,height:22}}/>;
  return <>
    <WbTop step={7}/>
    <div style={{display:'flex',justifyContent:'space-between',alignItems:'flex-end',gap:12,margin:'0 0 2px'}}>
      <div style={{minWidth:0}}><div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>ANY PIECE</div><div style={{fontSize:12.5,color:BK.muted,textWrap:'pretty'}}>Write the piece’s name. Each new piece gets a fresh copy of this page.</div></div>
      <span style={{display:'inline-block',width:230,borderBottom:'2px solid ' + BK.ink,height:26,flex:'0 0 auto'}}/></div>
    <Part kind="together" title="My piece’s melody" how="Like Lesson Book page 1: look at the first two phrases of your piece and fill each row.">
      <div style={{display:'flex',flexDirection:'column',gap:8,border:'0.8px solid ' + BK.hair,padding:'10px 12px'}}>
        {row('Its line', <div style={{height:96,border:'1.3px dashed ' + BK.line,borderRadius:6,position:'relative'}}><span style={{position:'absolute',left:8,top:6,fontSize:11,color:BK.muted}}>draw the line of the first phrase</span></div>, 100)}
        {row('High point', <div style={{display:'flex',alignItems:'center',gap:8,fontSize:13,fontWeight:800,color:BK.ink}}>bar {line} note {line}</div>)}
        {row('Phrase 1', <div style={{display:'flex',alignItems:'center'}}>{chxCircle(['question', 'answer'])}</div>)}
        {row('Phrase 2', <div style={{display:'flex',alignItems:'center'}}>{chxCircle(['question', 'answer'])}</div>)}
        {row('Its motif', <div style={{display:'grid',gridTemplateColumns:'minmax(0,190px) minmax(0,1fr)',alignItems:'center',gap:16}}><MlxWrite bars={[]} empty={1} end={false} ts={false} D={18} label={'An empty bar for the motif.'}/><div style={{fontSize:13,fontWeight:800,color:BK.ink}}>comes back in bars <span style={{display:'inline-block',width:120,borderBottom:'1.3px solid ' + BK.line,height:22}}/></div></div>, 70)}
      </div>
    </Part>
    <Part kind="play" title="Play it with its shape" how="Play the two phrases: louder to each high point, a breath at each end. Tick when your teacher says yes.">
      {sskRowN(1, ivxTicks(['the line', 'the motif', 'the breaths']))}
    </Part>
    <Part kind="year" title="My pieces and their motifs"><div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:'4px 18px'}}>{Array.from({ length: 12 }, (_, i) => <div key={i} style={{display:'grid',gridTemplateColumns:'minmax(0,1fr) 120px',gap:8,borderBottom:'0.8px solid ' + BK.hair,height:33,alignItems:'end',fontSize:11.5,color:BK.muted}}><span/><span style={{borderLeft:'0.8px solid ' + BK.hair,paddingLeft:6}}>motif</span></div>)}</div>
      <div style={{fontSize:12.5,color:BK.muted,marginTop:6}}>Write each piece you learn and its motif’s first notes. Keep this on your first copy.</div></Part>
    <Faces/>
  </>;
}
function MlxPaperCheck() {
  const C = MLX_CHK, { nB, nC, nD } = mlxChkNo();
  return <div className="lb-paper" style={{display:'flex',flexDirection:'column',gap:10,flex:'1 0 auto'}}>
    <LbPaperHead/>
    {bkSec('A', 'Which line? Circle a, b or c.')}
    <BkGrid cols={2} gap="6px 10px">{C.line.map((bars, i) => <BkCell key={i} n={i + 1}>{sdyCol(<>{mlxWbRow(bars, { D: 18, mw: 250, end: false })}{mlxWbLines(bars, C.lineOpts[i], C.line, null)}</>, '18px 6px 8px')}</BkCell>)}</BkGrid>
    {bkSec('B', 'Question or answer? Circle one.')}
    <BkGrid cols={1} gap="5px">{C.qa.map((bars, i) => <BkCell key={i} n={nB + i}>{sdyCol(<div style={{display:'grid',gridTemplateColumns:'minmax(0,400px) 200px',justifyContent:'center',alignItems:'center',gap:18}}>{mlxWbRow(bars, { D: 17, end: false })}{mlxWbWords(['question', 'answer'])}</div>, '3px 4px 2px')}</BkCell>)}</BkGrid>
    {bkSec('C', 'Write the word.')}
    <BkGrid cols={4} gap="6px 10px">{C.word.map((w, i) => <BkCell key={i} n={nC + i}>{sdyCol(<><div style={{textAlign:'center',fontSize:13,fontWeight:800,color:BK.ink,marginTop:16,lineHeight:1.3,textWrap:'balance'}}>“{MLX_WORDS.find(x => x[0] === w)[1]}”</div><div style={{borderBottom:'1.3px solid ' + BK.line,height:40,margin:'auto 8px 4px'}}/></>, '6px 2px 8px')}</BkCell>)}</BkGrid>
    {bkSec('D', 'Bar 2 is made from bar 1. Circle one.')}
    <BkGrid cols={3} gap="6px 10px">{C.rs.map(([b1, h], i) => <BkCell key={i} n={nD + i}>{sdyCol(<>{mlxWbRow([b1, mlxNext(b1, h)], { end: false, D: 14 })}<div style={{marginTop:'auto'}}>{mlxWbWords(['repetition', 'sequence up', 'sequence down'])}</div></>, '18px 4px 8px')}</BkCell>)}</BkGrid>
  </div>;
}

function MlxTeacher() {
  const W = MLX_WB, C = MLX_CHK, pages = [], { nB, nC, nD, total } = mlxChkNo();
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="melody" teacher>{content}</WbPage>);
  const done = (i) => i === 0 ? ' (done)' : '';
  const qa = (bars) => mlxFlat(bars).slice(-1)[0][2] === 28 ? 'answer' : 'question';
  const hiOf = (bars) => { const h = mlxHigh(bars), b = mlxBarRanges(bars).findIndex(([a, z]) => h >= a && h <= z); return mlxName(mlxFlat(bars)[h][2]) + ' in bar ' + (b + 1); };
  const nm = (bar) => bar.map(n => mlxName(n[2])).join(' ');
  P(<>
    <div style={{fontFamily:"'Playfair Display', Georgia, serif",fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('melody')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 8px',lineHeight:1.5}}>{'Melody and phrasing: the tune, its line, its phrases (question and answer), its motif (repetition and sequence). Chapter ' + bkChapterNo('reading-steps') + ' (steps and skips) and chapter ' + bkChapterNo('form') + ' (the phrase, the phrase mark, the resting note, repetition) come first. AMEB Music Craft: Preliminary, two short melodies the same or different (pages 5, 6); Grade 1 (aural), a line drawing of a melody’s high and low points (page 2); Grade 2 (written), the definition of motif. Not here: Grade 2 (aural), marks written by ear; Grade 3, cadences (prepared by the last note only). The tunes are the book’s own, from middle C to A.'}</div>
    <div style={{border:'0.8px solid ' + BK.hair,padding:'6px 12px',margin:'0 0 8px',fontSize:11.5,color:BK.ink,lineHeight:1.42}}><b style={{color:BK.coral}}>Words.</b> A question (antecedent) ends away from the tonic, most often on a note of the dominant chord (G, B or D in C: an imperfect or half cadence); its answer (consequent) ends on the tonic, usually by a perfect or authentic cadence (V–I); together they make a period. Here the student hears it by the last note only; cadences come with chords (chapter {bkChapterNo('chords')}). A sequence follows straight after its model, its shape kept in the key (a step can be a tone or a semitone). On a piano part the breath mark (,) is a short lift between phrases. Korean: 선율 (school: 가락); 선율선 (school: 가락선); 숨표, never 쉼표 (a rest); 질문·대답 프레이즈 (school: 반마침 / 온마침); 으뜸음; 동기 (school counts a 동기 as two bars; here one bar); 동형 진행 (also 시퀀스; not 반복 진행, close to 반복).</div>
    <TcBlock page={2} title="The line of a tune" answers={<>{sscLesson('The tune played while the other hand draws its line in the air; the teacher plays a tune and the child draws its line and marks its high point.')}{skgTcAns('TRY IT', W.try2.map((_, i) => 'abc'[W.try2opts[i].indexOf('a')] + done(i)))}{skgTcAns('YOUR TURN', W.turn2.map(b => 'high point ' + hiOf(b)), 5)}</>}
      watch="A line drawn by the note names (letters) rather than by height. A line that moves up or down between two same notes (it should stay flat there)."
      say="“The line goes where the notes go.”"/>
    <TcBlock page={3} title="Phrasing" answers={<>{sscLesson('The phrase shaped: louder to the high point, softer to the resting note, a lift at the breath mark; once flat, once shaped. Dynamics written in a piece come first; this shape is the default when there are none.')}{skgTcAns('TRY IT', W.try3.map((b, i) => hiOf(b) + done(i)))}{skgTcAns('YOUR TURN', W.turn3.map(b => '< to ' + hiOf(b) + ', > to the end'), 5)}</>}
      watch="An accent on the high point instead of a growth to it. The breath taken in the middle of the phrase, or no lift at all."
      say="“A phrase often gets louder to its high point and softer to its end.”"/>
    <TcBlock page={4} title="Question and answer" answers={<>{sscLesson('The question, then the answer, listening to the ends; the answer turned into a question by ending it on G.')}{skgTcAns('TRY IT', W.try4.map((b, i) => qa(b) + done(i)))}{skgTcAns('YOUR TURN', ['a whole note C in bar 8', 'a whole note C in bar 8'], 5)}</>}
      watch="Any long note called an answer: it is the last note that decides, and only the tonic answers. An answer that copies the question to its last note (it then asks again)."
      say="“A question ends away from the tonic; its answer ends on the tonic.”"/>
  </>);
  P(<>
    <TcBlock page={5} title="The motif" answers={<>{sscLesson('The motif played, then the tune with “motif” said at each return; a motif found in a piece being learnt.')}{skgTcAns('TRY IT', W.try5ans.map((bs, i) => (bs.length > 1 ? 'bars ' + bs.join(' and ') : 'bar ' + bs[0]) + done(i)))}{skgTcAns('YOUR TURN', W.turn5ans.map(n => n + ' times'), 5)}</>}
      watch="Only exact repeats counted: a sequence is the motif too. A bar with the same notes in a different order counted as the motif. Every motif here is four crotchets in one bar so that shapes can be compared; a motif can be any length, and its rhythm is part of it."
      say="“A motif is a short idea that comes back.”"/>
    <TcBlock page={6} title="Repetition and sequence" answers={<>{sscLesson('The motif from D twice (repetition), then from D and E (sequence up) and from D and C (sequence down); a motif of the child’s own in sequence.')}{skgTcAns('TRY IT', W.try6.map(([, h], i) => mlxRsNm(h) + done(i)))}{skgTcAns('YOUR TURN', W.turn6.map(([b1, h]) => nm(mlxNext(b1, h)) + ' | ' + nm(mlxNext(mlxNext(b1, h), h))), 5)}</>}
      watch="Every note moved a step but the shape changed (one note forgotten). A repetition called a sequence because it is in a new bar."
      say="“Same notes: repetition. Same shape, new start: sequence.”"/>
    <TcBlock page={7} title="Any piece: my piece’s melody (a fresh copy for each piece)" answers={<div style={{fontSize:12,color:BK.ink,lineHeight:1.5}}>The student’s own piece: the line of its first phrase, its high point, its motif and where it comes back, and whether its first two phrases are a question and an answer. Real pieces often have a motif that comes back changed (a different rhythm, an interval stretched): count it, and say what changed.</div>}/>
    <TcBlock page={8} title="The check-up on paper (the Workbook’s last page)" answers={<>
      {skgTcAns('A', C.line.map((_, i) => 'abc'[C.lineOpts[i].indexOf('a')]))}
      {skgTcAns('B', C.qa.map(qa), nB)}
      {skgTcAns('C', C.word.map(w => w === 'contour' ? 'contour (or “line”)' : w), nC)}
      {skgTcAns('D', C.rs.map(([, h]) => mlxRsNm(h)), nD)}
      <div style={{fontSize:12,color:BK.ink,marginTop:6,lineHeight:1.5}}>One mark each: A {C.line.length}, B {C.qa.length}, C {C.word.length}, D {C.rs.length}; {total} in all. A section with a wrong answer is not passed yet: go back to its pages. Also listen to the student (My five checks, Lesson Book page 7).</div>
    </>}
      goBack={[{ id: 'a', step: '1', page: '2' }, { id: 'b', step: '3', page: '4' }, { id: 'c', step: '1, 3, 4 and 5', page: '2, 4, 5 and 6' }, { id: 'd', step: '5', page: '6' }]}/>
    <div style={{border:'0.8px solid ' + BK.hair,padding:'6px 12px',margin:'0 0 8px',fontSize:12,color:BK.ink,lineHeight:1.5}}><b style={{color:BK.coral}}>The drill (after page 6).</b> 1 which line · 2 where is the high point · 3 listening: which line (screen only) · 4 question or answer · 5 listening: question or answer (screen only) · 6 where does the motif come back · 7 repetition or sequence · 8 the words · 9 extra: what comes next in the sequence.</div>
    <div style={{border:'0.8px solid ' + BK.hair,padding:'7px 12px',fontSize:12,color:BK.ink,lineHeight:1.5}}><b style={{color:BK.coral}}>My five checks (Lesson Book page 7).</b> 1. On page 1’s map, point to the question, the answer, the motif and the high point. 2. Draw the line of a tune the teacher plays. 3. Play page 3’s phrase shaped, with its breath. 4. Play page 4’s question and answer and say which is which. 5. Play page 6’s motif in sequence, a step higher each time. Got it! means right without help.</div>
  </>);
  return <>{pages}</>;
}
WORKBOOKS['melody'] = MlxWorkbook;
TEACHER_COPIES['melody'] = MlxTeacher;
