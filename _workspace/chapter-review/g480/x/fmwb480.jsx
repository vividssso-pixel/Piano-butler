// ─── Phase 480: chapter 24's Workbook (pages 2 to 8: one per lesson step, my piece's map, the check-up) and the Teacher
// copy (they replace the Phase 117 ones). Chapter 21's ivxAns and chapter 22's chxCircle are reused.
const FMX_WB = {
  try2: ['A', 'B', 'C', 'D'],                                     // mark the phrase, circle its resting note (A done)
  turn2: [['B', 'E'], ['C', 'A']],                                 // eight bars, two phrases each: 4 and 4 (both end on C)
  try3: [['A', 'A'], ['B', 'C'], ['D', 'D'], ['E', 'A']],         // same (done), different, same, different
  turn3: ['B', 'C', 'B', 'A'],                                     // A B A C (ends on C)
  try4: [['A', 'B'], ['A', 'B', 'A'], ['A', 'A', 'B', 'B'], ['A', 'B', 'C']],        // binary (done), ternary, binary, neither
  try5: [['A', 'B', '?'], ['A', '?', 'A'], ['?', 'B', 'A'], ['?', 'B', '?']],         // A (done), B, A, A and A
  try6: [['C D E F', 'G A G F', 'C D E F'], ['E G F E', 'G F E D', 'C D E F'], ['G F E D', 'E G F G', 'G F E D'], ['E G F G', 'G F E D']],   // the book's openings: A B A (done), A B C, A B A, A B
  turn6: ['A', 'C', 'A'],                                          // twelve bars, three sections: A B A, ternary
};
const FMX_CHK = {
  sd: [['B', 'B'], ['A', 'E']],                                   // same, different
  bt: [['A', 'B', 'A'], ['A', 'A', 'B', 'B'], ['A', 'B']],        // ternary, binary, binary
  word: ['phrase', 'repetition', 'contrast', 'section'],
  pat: ['E', 'E', 'D', 'E'],                                       // A A B A (the first given: A)
};
const fmxChkNo = () => { const C = FMX_CHK, nB = C.sd.length + 1, nC = nB + C.bt.length, nD = nC + C.word.length; return { nB, nC, nD, total: nD + C.pat.length - 2 }; };
const fmxWbRow = (ids, o = {}) => <div style={{width:'100%',maxWidth:o.mw || 9999,margin:'0 auto'}}><FmxRow ids={ids} ts={o.ts} tsRoom={o.tsRoom} secEnd={o.secEnd} marks={o.marks} rest={o.rest} letters={o.letters} qmark={o.qmark || []} coral={o.coral || []} width={o.w || fmxVbw(ids, o.ts, o.D || 17)} D={o.D || 17} n0={o.n0} end={o.end}/></div>;
const fmxWbBlocks = (ls, on, w = 34) => <div style={{display:'flex',gap:5,justifyContent:'center',margin:'4px 0'}}>{ls.map((l, i) => <span key={i} style={{width:w,height:w,display:'inline-flex',alignItems:'center',justifyContent:'center',borderRadius:5,border:'1.6px ' + (l === '?' ? 'dashed ' : 'solid ') + (on === i ? BK.coral : BK.ink),fontFamily:LB_SERIF,fontSize:w * 0.58,fontWeight:900,color:on === i ? BK.coral : BK.ink}}>{l === '?' ? (on === i ? 'A' : '') : l}</span>)}</div>;
const fmxWbWords = (words, on) => <div style={{display:'flex',justifyContent:'center',gap:14,fontSize:13.5,fontWeight:800,color:BK.ink,margin:'2px 0'}}>{words.map(w => <span key={w} style={{border:'1.5px solid ' + (on === w ? BK.coral : 'transparent'),borderRadius:14,padding:'0 8px',color:on === w ? BK.coral : BK.ink}}>{w}</span>)}</div>;
const fmxEmptyBars = (n = 4, label, pad = [22, 22]) => { const W0 = 620, x0 = 60, bw = (W0 - 8 - x0) / n;
  return <div style={{width:'100%',maxWidth:620,margin:'0 auto'}}><SfStaff clef="treble" width={W0} pad={pad} label={label} extra={(yOf, layer) => layer !== 'over' ? null : <g>{Array.from({ length: n }, (_, i) => <line key={i} x1={x0 + (i + 1) * bw} x2={x0 + (i + 1) * bw} y1={yOf(38)} y2={yOf(30)} stroke={BK.ink} strokeWidth={i === n - 1 ? 1.5 : 1.3}/>)}</g>}/></div>; };
const fmxWbLine = (h = 30) => <div style={{borderBottom:'1.3px solid ' + BK.line,height:h,margin:'auto 8px 4px'}}/>;

function FmxWorkbook({ startNo = 1 }) {
  const W = FMX_WB, pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + 1 + pages.length} chId="form">{content}</WbPage>);

  // 2 (faces "The phrase")
  P(<>
    <WbTop step={1}/>
    <Part kind="together" title="Mark the phrase" how="Draw the phrase mark under each phrase and circle its resting note. The first one is done.">
      <BkGrid cols={2} gap="8px 10px">{W.try2.map((id, i) => <ExCell key={i} n={i + 1} ex={i === 0}>{sdyCol(fmxWbRow([id], { marks: i === 0, rest: i === 0 }), '22px 6px 10px')}</ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Two phrases" how="Each tune has two phrases. Draw a phrase mark under each, and write how many bars each phrase has.">
      <BkGrid cols={2} gap="8px 10px">{W.turn2.map((ids, i) => <BkCell key={i} n={i + 5}>{sdyCol(<>{fmxWbRow([ids[0]], { ts: true, end: false, w: fmxVbw([ids[0]], true, 17) })}{fmxWbRow([ids[1]], { tsRoom: true, n0: 5, w: fmxVbw([ids[0]], true, 17) })}<div style={{display:'flex',justifyContent:'center',gap:16,flexWrap:'wrap',alignItems:'center',fontSize:13,fontWeight:800,color:BK.ink,marginTop:'auto',paddingTop:6}}><span style={{display:'flex',alignItems:'center',gap:8}}>Phrase 1: {bkBox(40, 30)} bars</span><span style={{display:'flex',alignItems:'center',gap:8}}>Phrase 2: {bkBox(40, 30)} bars</span></div></>, '22px 6px 8px')}</BkCell>)}</BkGrid>
    </Part>
    <Part kind="play" title="One breath" how="Play the tunes above, each phrase in one breath. Lift your hand a little after each resting note. Tick each.">
      {sskRowN(7, <div style={{display:'flex',flexDirection:'column',gap:6,width:'100%'}}>{fmxWbRow(['A'], { ts: true, marks: true, rest: true, end: false, D: 22, n0: 1, w: fmxVbw(['A'], true, 22), mw: 560 })}{fmxWbRow(['E'], { tsRoom: true, marks: true, rest: true, D: 22, n0: 5, w: fmxVbw(['A'], true, 22), mw: 560 })}{ivxTicks(['these two', 'tune 5', 'tune 6', 'a piece I know'])}</div>)}
    </Part>
    <Faces/>
  </>);

  // 3 (faces "Same or different")
  P(<>
    <WbTop step={2}/>
    <Part kind="together" title="Same or different?" how="Compare the two phrases. Circle same or different. The first one is done.">
      <BkGrid cols={2} gap="8px 10px">{W.try3.map(([a, b], i) => <ExCell key={i} n={i + 1} ex={i === 0}>{sdyCol(<>{fmxWbRow([a])}{fmxWbRow([b])}<div style={{marginTop:'auto'}}>{fmxWbWords(['same', 'different'], i === 0 ? (a === b ? 'same' : 'different') : null)}</div></>, '20px 6px 8px')}</ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Give the letters" how="Sixteen bars, four phrases. Write a letter in each box: the first is A; same music, same letter; new music, the next letter.">
      <BkGrid cols={2} gap="8px 10px">{W.turn3.map((id, i) => <BkCell key={i} n={i + 5}>{sdyCol(fmxWbRow([id], { ts: i === 0, tsRoom: i > 0, letters: [''], qmark: [0], n0: i * 4 + 1, end: i === 3, w: fmxVbw([id], true, 17) }), '8px 6px 10px')}</BkCell>)}</BkGrid>
    </Part>
    <Part kind="play" title="Say the letters" how="Play the four phrases above, saying each letter as you start it. Tick when you can.">
      {sskRowN(9, ivxTicks(['phrases 5 to 8', 'with my letters said aloud']))}
    </Part>
    <Faces/>
  </>);

  // 4 (faces "Binary form")
  P(<>
    <WbTop step={3}/>
    <Part kind="together" title="Binary?" how="Each map shows a piece’s sections in the order they are played. Circle binary, ternary or neither. The first one is done.">
      <BkGrid cols={4} gap="8px 10px">{W.try4.map((ls, i) => <ExCell key={i} n={i + 1} ex={i === 0}>{sdyCol(<>{fmxWbBlocks(ls, null, 32)}<div style={{marginTop:'auto',display:'flex',flexDirection:'column',alignItems:'center',gap:2}}>{['binary', 'ternary', 'neither'].map(w => <span key={w} style={{border:'1.5px solid ' + (i === 0 && w === 'binary' ? BK.coral : 'transparent'),borderRadius:14,padding:'0 8px',fontSize:13,fontWeight:800,color:i === 0 && w === 'binary' ? BK.coral : BK.ink}}>{w}</span>)}</div></>, '22px 2px 6px')}</ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="The order" how="Write the letters in the order the sections are played. You may not need every box.">
      <BkGrid cols={1} gap="8px">{[['bin', 5], ['repA', 5]].map(([r, n], i) => <BkCell key={i} n={i + 5}>{sdyCol(<><div style={{maxWidth:530,margin:'0 auto',width:'100%'}}><SgnRoad bars={FMX_ROADS[r].bars} rows={[[0, 3], [4, 7]]} rw={560} o={{ ts: 4, nums: true }} label={'An eight-bar road with repeat signs.'}/></div>
        <div style={{display:'flex',gap:8,justifyContent:'center',marginTop:6}}>{Array.from({ length: n }, (_, k) => <span key={k}>{bkBox(40, 36)}</span>)}</div></>, '14px 6px 8px')}</BkCell>)}</BkGrid>
    </Part>
    <Part kind="play" title="Play it twice" how="Play road 5 with both repeats, saying A A B B. Tick it.">
      {sskRowN(7, ivxTicks(['road 5', 'saying the letters']))}
    </Part>
    <Faces/>
  </>);

  // 5 (faces "Ternary form")
  P(<>
    <WbTop step={4}/>
    <Part kind="together" title="Make it ternary" how="Fill the empty boxes so the piece is ternary: A B A. The first one is done.">
      <BkGrid cols={4} gap="8px 10px">{W.try5.map((ls, i) => <ExCell key={i} n={i + 1} ex={i === 0}>{sdyCol(fmxWbBlocks(ls, i === 0 ? 2 : null, 36), '42px 2px 30px')}</ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Follow the road" how="Write the bars in the order they are played, then the letters of the sections. You may not need every box.">
      <BkCell n={5}>{sdyCol(<><div style={{maxWidth:600,margin:'0 auto',width:'100%'}}><SgnRoad bars={FMX_TER} rows={[[0, 3], [4, 7]]} rw={560} o={{ ts: 4, nums: true }} label={'Eight bars with Fine after bar 4 and D.C. al Fine after bar 8.'}/></div>
        <div style={{display:'flex',gap:5,justifyContent:'center',marginTop:8}}>{Array.from({ length: 14 }, (_, k) => <span key={k}>{bkBox(34, 40)}</span>)}</div>
        <div style={{display:'flex',gap:8,justifyContent:'center',alignItems:'center',marginTop:8,fontSize:13,fontWeight:800,color:BK.ink}}>Letters: {[0, 1, 2].map(k => <span key={k}>{bkBox(44, 42)}</span>)}</div></>, '20px 6px 16px')}</BkCell>
    </Part>
    <Part kind="play" title="Your own B" how="Play the road with D.C. al Fine. Then play A, make up your own B, and play A again. Tick each.">
      {sskRowN(6, <div style={{display:'flex',flexDirection:'column',gap:4,width:'100%'}}><div style={{fontFamily:LB_SERIF,fontSize:17,fontWeight:900,color:BK.ink,textAlign:'center'}}>A <span style={{fontSize:13,fontFamily:'Inter, sans-serif',fontWeight:800,color:BK.muted}}>(bars 1 to 4)</span> · B <span style={{fontSize:13,fontFamily:'Inter, sans-serif',fontWeight:800,color:BK.muted}}>(my own, below)</span> · A</div>{fmxEmptyBars(4, 'Four empty bars for my own B.', [40, 36])}{ivxTicks(['the road', 'A, my own B, A'])}</div>)}
    </Part>
    <Faces/>
  </>);

  // 6 (faces "Finding the form")
  P(<>
    <WbTop step={5}/>
    <Part kind="together" title="Find the form" how="Each map shows a piece’s sections in the order they are played. A box shows how its section starts; here, the same start means the same music. Write a letter for each section, then circle the form. The first one is done.">
      <BkGrid cols={2} gap="8px 10px">{W.try6.map((st, i) => { const ls = fmxLettersOf(st), ter = ls.join('') === 'ABA';
        return <ExCell key={i} n={i + 1} ex={i === 0}>{sdyCol(<><div style={{display:'grid',gridTemplateColumns:'repeat(' + st.length + ',1fr)',gap:6,textAlign:'center',fontSize:13.5,fontWeight:800,color:BK.ink,marginTop:6}}>{st.map((s, k) => <div key={k}>{s}<div style={{marginTop:4,display:'flex',justifyContent:'center'}}>{i === 0 ? <span style={{width:34,height:30,display:'inline-flex',alignItems:'center',justifyContent:'center',border:'1.5px solid ' + BK.coral,borderRadius:5,color:BK.coral,fontFamily:LB_SERIF,fontWeight:900,fontSize:17}}>{ls[k]}</span> : bkBox(34, 30)}</div></div>)}</div>
          <div style={{marginTop:'auto',paddingTop:10}}>{chxCircle(['binary', 'ternary', 'neither'], i === 0 ? (ter ? 'ternary' : 'neither') : null)}</div></>, '20px 6px 6px')}</ExCell>; })}</BkGrid>
    </Part>
    <Part kind="home" title="Twelve bars" how="A piece in three sections, four bars each. Write a letter for each section, then circle its form.">
      <BkCell n={5}>{sdyCol(<>{W.turn6.map((id, k) => <div key={k} style={{display:'grid',gridTemplateColumns:'minmax(0,1fr) 58px minmax(0,380px) minmax(0,1fr)',alignItems:'center',gap:8}}><span/><div style={{display:'flex',justifyContent:'center'}}>{bkBox(40, 38)}</div>{fmxWbRow([id], { ts: k === 0, tsRoom: k > 0, n0: k * 4 + 1, end: k === 2, secEnd: k < 2, w: fmxVbw([id], true, 17), mw: 380 })}<span/></div>)}
        <div style={{marginTop:2}}>{chxCircle(['binary', 'ternary', 'neither'])}</div></>, '10px 10px 8px')}</BkCell>
    </Part>
    <Part kind="play" title="Say it as you play" how="Play the twelve bars, saying each letter as its section starts. Then find the form of a piece you are learning, with the four steps. Tick each.">
      {sskRowN(6, <div style={{display:'flex',flexDirection:'column',gap:4,width:'100%'}}>{['Find the sections: double bar lines, repeat signs, Fine.', 'Listen to each section: the same music as A, or new?', 'Same music, same letter; new music, the next letter.', 'Name the form.'].map((x, k) => <div key={k} style={{display:'flex',alignItems:'center',gap:10,fontSize:13.5,fontWeight:800,color:BK.ink}}><span style={{width:24,height:24,borderRadius:12,background:BK.ink,color:'#fff',display:'inline-flex',alignItems:'center',justifyContent:'center',fontSize:13}}>{k + 1}</span>{x}</div>)}<div style={{marginTop:6}}>{ivxTicks(['the twelve bars', 'a piece I am learning'])}</div></div>)}
    </Part>
    <Faces/>
  </>);

  // 7. my piece's map (any piece); 8. the check-up on paper
  P(<FmxMapPage/>);
  P(<FmxPaperCheck/>);
  return <>{pages}</>;
}
function FmxMapPage() {
  const row = (label, node) => <div style={{display:'grid',gridTemplateColumns:'110px minmax(0,1fr)',alignItems:'center',gap:10,minHeight:46}}><div style={{fontSize:11.5,fontWeight:900,letterSpacing:'0.08em',textTransform:'uppercase',color:BK.muted}}>{label}</div><div>{node}</div></div>;
  return <>
    <WbTop step={7}/>
    <div style={{display:'flex',justifyContent:'space-between',alignItems:'flex-end',gap:12,margin:'0 0 2px'}}>
      <div style={{minWidth:0}}><div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>ANY PIECE</div><div style={{fontSize:12.5,color:BK.muted,textWrap:'pretty'}}>Write the piece’s name. Each new piece gets a fresh copy of this page.</div></div>
      <span style={{display:'inline-block',width:230,borderBottom:'2px solid ' + BK.ink,height:26,flex:'0 0 auto'}}/></div>
    <Part kind="together" title="My piece’s map" how="Like Lesson Book page 1. Write how many bars the piece has. On the bar ruler: over the bars of each section, draw a box with its letter; over the bars of each phrase, draw a curve. Cross out the bars the piece does not have.">
      <div style={{display:'flex',flexDirection:'column',gap:8,border:'0.8px solid ' + BK.hair,padding:'10px 12px'}}>
        {row('The piece', <div style={{display:'flex',alignItems:'center',gap:8,fontSize:13,fontWeight:800,color:BK.ink}}>{bkBox(60, 34)} bars</div>)}
        {[0, 16].map(b0 => <div key={b0} style={{display:'grid',gridTemplateColumns:'110px minmax(0,1fr)',gap:10,alignItems:'stretch'}}>
          <div style={{display:'flex',flexDirection:'column',justifyContent:'space-between',fontSize:11.5,fontWeight:900,letterSpacing:'0.08em',textTransform:'uppercase',color:BK.muted,padding:'6px 0 4px'}}><span style={{height:44,display:'flex',alignItems:'center'}}>Sections</span><span style={{height:36,display:'flex',alignItems:'center'}}>Phrases</span><span style={{height:26,display:'flex',alignItems:'center'}}>Bars</span></div>
          <div style={{display:'flex',flexDirection:'column'}}>
            <div style={{height:50,borderBottom:'0.8px dashed ' + BK.hair}}/>
            <div style={{height:40,borderBottom:'0.8px dashed ' + BK.hair}}/>
            <div style={{display:'grid',gridTemplateColumns:'repeat(16,1fr)',border:'1.3px solid ' + BK.ink,height:28}}>{Array.from({ length: 16 }, (_, k) => <span key={k} style={{borderLeft:k ? '0.8px solid ' + BK.ink : 'none',fontSize:10.5,fontWeight:800,color:BK.muted,textAlign:'center',paddingTop:2,fontVariantNumeric:'tabular-nums'}}>{b0 + k + 1}</span>)}</div></div></div>)}
        {row('Its form', <div style={{display:'flex',alignItems:'center'}}>{chxCircle(['binary', 'ternary', 'another form'])}</div>)}
      </div>
    </Part>
    <Part kind="play" title="Play it by its map" how="Play the piece. Point to each section on your map as it starts. Tick when your teacher says yes.">
      {sskRowN(1, ivxTicks(['the sections', 'the phrases', 'the form named']))}
    </Part>
    <Part kind="year" title="My pieces and their forms"><div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:'4px 18px'}}>{Array.from({ length: 12 }, (_, i) => <div key={i} style={{display:'grid',gridTemplateColumns:'minmax(0,1fr) 110px',gap:8,borderBottom:'0.8px solid ' + BK.hair,height:36,alignItems:'end',fontSize:11.5,color:BK.muted}}><span/><span style={{borderLeft:'0.8px solid ' + BK.hair,paddingLeft:6}}>form</span></div>)}</div>
      <div style={{fontSize:12.5,color:BK.muted,marginTop:6}}>Write each piece you learn and its form. Keep this on your first copy.</div></Part>
    <Faces/>
  </>;
}
function FmxPaperCheck() {
  const C = FMX_CHK, { nB, nC, nD } = fmxChkNo();
  return <div className="lb-paper" style={{display:'flex',flexDirection:'column',gap:10,flex:'1 0 auto'}}>
    <LbPaperHead/>
    {bkSec('A', 'Same or different? Circle one.')}
    <BkGrid cols={2} gap="6px 10px">{C.sd.map(([a, b], i) => <BkCell key={i} n={i + 1}>{sdyCol(<>{fmxWbRow([a])}{fmxWbRow([b])}<div style={{marginTop:'auto'}}>{fmxWbWords(['same', 'different'])}</div></>, '20px 6px 8px')}</BkCell>)}</BkGrid>
    {bkSec('B', 'Binary or ternary? Circle one. The boxes show the sections in the order they are played.')}
    <BkGrid cols={3} gap="6px 10px">{C.bt.map((ls, i) => <BkCell key={i} n={nB + i}>{sdyCol(<>{fmxWbBlocks(ls, null, 36)}<div style={{marginTop:'auto'}}>{fmxWbWords(['binary', 'ternary'])}</div></>, '18px 4px 8px')}</BkCell>)}</BkGrid>
    {bkSec('C', 'Write the word.')}
    <BkGrid cols={4} gap="6px 10px">{C.word.map((w, i) => <BkCell key={i} n={nC + i}>{sdyCol(<><div style={{textAlign:'center',fontSize:13.5,fontWeight:800,color:BK.ink,marginTop:16,lineHeight:1.3,textWrap:'balance'}}>“{FMX_WORDS.find(x => x[0] === w)[1]}”</div>{fmxWbLine(46)}</>, '6px 2px 8px')}</BkCell>)}</BkGrid>
    {bkSec('D', 'Write a letter for each phrase. The first is A.')}
    <BkGrid cols={2} gap="6px 10px">{C.pat.map((id, i) => <BkCell key={i} n={i ? nD + i - 1 : ''}>{sdyCol(fmxWbRow([id], { ts: i === 0, tsRoom: i > 0, letters: [i ? '' : 'A'], qmark: i ? [0] : [], n0: i * 4 + 1, end: i === 3, w: fmxVbw([id], true, 17) }), '6px 6px 8px')}</BkCell>)}</BkGrid>
  </div>;
}

function FmxTeacher() {
  const W = FMX_WB, C = FMX_CHK, pages = [], { nB, nC, nD, total } = fmxChkNo();
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="form" teacher>{content}</WbPage>);
  const done = (i) => i === 0 ? ' (done)' : '';
  const nm = (ls) => { const s = ls.join(''); return s === 'AB' || s === 'AABB' ? 'binary' : s === 'ABA' ? 'ternary' : 'neither'; };
  P(<>
    <div style={{fontFamily:"'Playfair Display', Georgia, serif",fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('form')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 8px',lineHeight:1.5}}>{'Musical form: the piece, its sections, phrases, bars and beats (chapter ' + bkChapterNo('time-signatures') + ': bars and double bar lines; chapter ' + bkChapterNo('signs') + ': repeat signs, Fine, D.C. al Fine). AMEB Music Craft (2022): Grade 1, repetition and contrast in an eight-bar melody, repeat signs; Grade 2, the definition of phrase (and motif: chapter ' + bkChapterNo('melody') + '), binary and ternary form marked with A and B; Grade 3 (aural), A and B in a sixteen-bar four-phrase melody. Rondo comes at Grade 5 (the toolbox keeps it). Lesson Book page 1 is the map of a piece (piece, sections, phrases, bars, beats); the screen lesson ends with a piece the student builds from A and B. The book’s tunes are original, four-bar phrases from middle C.'}</div>
    <div style={{border:'0.8px solid ' + BK.hair,padding:'6px 12px',margin:'0 0 8px',fontSize:12,color:BK.ink,lineHeight:1.45}}><b style={{color:BK.coral}}>Letters.</b> The first music is A; the same music keeps its letter; new music takes the next letter. Music that is nearly the same (a changed ending) keeps its letter; exam papers may write A1 or A′. Page 3’s letters name phrases; pages 4 to 6’s letters name sections (a section is one or more phrases): A A B A on page 3 is a pattern of phrases, not a form name. Binary: two sections, A and B, often each repeated (A A B B played). Ternary: A, B, A again, often written with D.C. al Fine. Many minuets are ‖: A :‖: B A :‖ (rounded binary): A’s tune comes back inside the second repeat. Call it binary at this level (two repeated sections) and point out the return; ternary needs a whole B between two whole A sections. Korean school books count 한도막 / 두도막 / 세도막 형식 in 8-bar 큰악절 (8, 8 + 8, 8 + 8 + 8; 작은 세도막 = 4 + 4 + 4) and call a 4-bar phrase 작은악절; by that count this book’s 8-bar binary road is 한도막 and its ternary road is 작은 세도막. This book names the form by its sections: 2부 / 3부 형식 for binary and ternary.</div>
    <TcBlock page={2} title="The phrase" answers={<>{sscLesson('The picture’s two phrases, each in one breath, lifting after the resting note; then the phrases of a known piece, counted in bars.')}{skgTcAns('TRY IT', W.try2.map((id, i) => 'resting note ' + fmxLast(id) + done(i)))}{skgTcAns('YOUR TURN', W.turn2.map(() => '4 and 4 bars'), 5)}</>}
      watch="A phrase mark drawn bar by bar instead of under the whole phrase. The resting note taken for a rest: it is a note, held. Lifting in the middle of a phrase."
      say="“A phrase ends on a resting note.”"/>
    <TcBlock page={3} title="Same or different" answers={<>{sscLesson('Four phrases, saying each letter (A A B A); the teacher plays two phrases and the child says same or different.')}{skgTcAns('TRY IT', W.try3.map(([a, b], i) => (a === b ? 'same' : 'different') + done(i)))}{skgTcAns('YOUR TURN', fmxLettersOf(W.turn3), 5)}</>}
      watch="Letters given by the order of phrases (A B C D) instead of by their music. A new phrase after B given B again."
      say="“Same music, same letter.”"/>
    <TcBlock page={4} title="Binary form" answers={<>{sscLesson('The road with both repeats, saying A A B B; where A ends and B starts.')}{skgTcAns('TRY IT', W.try4.map((ls, i) => nm(ls) + done(i)))}{skgTcAns('YOUR TURN', [FMX_ROADS.bin.ls, FMX_ROADS.repA.ls], 5)}</>}
      watch="A A B B called four sections: the repeats play each section twice; it is still two sections, binary. A B C is neither: a third, new section."
      say="“Binary: A B.”"/>
  </>);
  P(<>
    <TcBlock page={5} title="Ternary form" answers={<>{sscLesson('The road with D.C. al Fine (A B A); then A, the child’s own B, and A again.')}{skgTcAns('TRY IT', W.try5.map((ls, i) => ls.map((l, k) => l === '?' ? 'ABA'[k] : null).filter(Boolean).join(' and ') + done(i)))}{skgTcAns('YOUR TURN', ['bars 1 2 3 4 5 6 7 8 1 2 3 4 (two boxes empty); A B A'], 5)}</>}
      watch="Stopping at the end of bar 8 instead of going back. Going back but playing past Fine."
      say="“Ternary: A B A.”"/>
    <TcBlock page={6} title="Finding the form" answers={<>{sscLesson('A piece the child is learning: its sections, letters and form.')}{skgTcAns('TRY IT', W.try6.map((st, i) => fmxLettersOf(st).join(' ') + ', ' + nm(fmxLettersOf(st)) + done(i)))}{skgTcAns('YOUR TURN', [fmxLettersOf(W.turn6).join(' ') + ', ' + nm(fmxLettersOf(W.turn6))], 5)}</>}
      watch="A section judged only by its first notes: listen to the whole of it (a B can open like A). A B C named ternary: here it is neither."
      say="“Find the sections, give the letters, name the form.”"/>
    <TcBlock page={7} title="Any piece: my piece’s map (a fresh copy for each piece)" answers={<div style={{fontSize:12,color:BK.ink,lineHeight:1.5}}>The student’s own piece drawn like Lesson Book page 1: its bars in all, its sections with letters and bar numbers, a curve over each phrase, and its form. Pieces in other forms (rondo, theme and variations, song forms like A A B A): circle “another form” and name it together.</div>}/>
    <TcBlock page={8} title="The check-up on paper (the Workbook’s last page)" answers={<>
      {skgTcAns('A', C.sd.map(([a, b]) => a === b ? 'same' : 'different'))}
      {skgTcAns('B', C.bt.map(ls => nm(ls)), nB)}
      {skgTcAns('C', C.word, nC)}
      {skgTcAns('D', fmxLettersOf(C.pat).slice(1), nD)}
      <div style={{fontSize:12,color:BK.ink,marginTop:6,lineHeight:1.5}}>One mark each: A {C.sd.length}, B {C.bt.length}, C {C.word.length}, D {C.pat.length - 1} (its first phrase is given: A); {total} in all. A section with a wrong answer is not passed yet: go back to its pages. Also listen to the student (My five checks, Lesson Book page 7).</div>
    </>}
      goBack={[{ id: 'a', step: '2', page: '3' }, { id: 'b', step: '3 and 4', page: '4 and 5' }, { id: 'c', step: '1 to 3', page: '2 to 4' }, { id: 'd', step: '2', page: '3' }]}/>
    <div style={{border:'0.8px solid ' + BK.hair,padding:'6px 12px',margin:'0 0 8px',fontSize:12,color:BK.ink,lineHeight:1.5}}><b style={{color:BK.coral}}>The drill (after page 6).</b> 1 same or different · 2 which letter · 3 listening: same or different (screen only) · 4 bar, phrase, section or piece · 5 binary or ternary · 6 listening: binary or ternary (screen only) · 7 read the road · 8 the words · 9 extra: four phrases, four letters.</div>
    <div style={{border:'0.8px solid ' + BK.hair,padding:'7px 12px',fontSize:12,color:BK.ink,lineHeight:1.5}}><b style={{color:BK.coral}}>My five checks (Lesson Book page 7).</b> 1. On page 1’s map, point to a section, a phrase, a bar and the beats. 2. Play page 2’s phrases, each to its resting note. 3. Give page 3’s four phrases their letters. 4. Play page 4’s road with its repeats, saying A A B B. 5. Play page 5’s road with D.C. al Fine, saying A B A. Got it! means right without help.</div>
  </>);
  return <>{pages}</>;
}
WORKBOOKS['form'] = FmxWorkbook;
TEACHER_COPIES['form'] = FmxTeacher;
