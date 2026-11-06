// ─── Phase 479: chapter 23's Workbook (pages 2 to 8: one per lesson step, a term hunt in any piece, the check-up) and
// the Teacher copy (they replace the Phase 117 ones). Chapter 21's ivxAns, ivxCircle and ivxTicks are reused.
const TMX_WB = {
  try2: [['Largo', 'Allegro'], ['Presto', 'Andante'], ['Lento', 'Vivace'], ['Allegretto', 'Adagio']],   // the faster: Allegro (done), Presto, Vivace, Allegretto
  turn2: ['Lento', 'Allegretto', 'Vivace', 'Presto', 'Largo', 'Prestissimo'],
  try3: ['accel.', 'riten.', 'a tempo', 'rit.'],
  turn3: ['accel.', 'rall.', 'riten.', 'a tempo'],                   // then: draw the beats for rit. and for accel.
  try4: [['p', 'f'], ['mf', 'mp'], ['ff', 'mf'], ['pp', 'p']],         // the louder: f (done), mf, ff, p
  bank4: ['mf', 'pp', 'ff', 'p', 'f', 'mp'],
  turn4: ['mp', 'ff', 'cresc.', 'sf'],
  try5: ['staccato', 'mezzo staccato', 'legato', 'mezzo staccato'],
  turn5: ['sostenuto', 'cantabile', 'leggiero', 'maestoso', 'espressivo', 'mezzo staccato'],
  try6: ['poco rit.', 'molto cresc.', 'sempre staccato', 'senza rit.'],
  turn6: ['più mosso', 'meno mosso', 'con moto', 'poco a poco cresc.', 'sempre', 'senza'],
};
const TMX_CHK = {
  mean: ['Allegretto', 'rit.', 'cresc.', 'mezzo staccato'],
  sign: ['ff', 'mp', 'sf'],
  pick: [['faster', 'Lento', 'Allegro'], ['louder', 'mf', 'pp']],
  term: ['poco', 'sempre', 'a tempo'],
};
const tmxChkNo = () => { const C = TMX_CHK, nB = C.mean.length + 1, nC = nB + C.sign.length, nD = nC + C.pick.length; return { nB, nC, nD, total: nD + C.term.length - 1 }; };
// writing lines; the example's answer written on the first in coral
const tmxLine = (ex, txt, h = 28, n = 1) => <div style={{margin:'auto 6px 2px'}}>{Array.from({ length: n }, (_, k) => <div key={k} style={{borderBottom:'1.3px solid ' + BK.line,minHeight:h,display:'flex',alignItems:'flex-end',justifyContent:'center',color:BK.coral,fontStyle:'italic',fontWeight:900,fontSize:13.5,textAlign:'center',lineHeight:1.2,paddingBottom:2}}>{ex && k === n - 1 ? txt : ''}</div>)}</div>;
const tmxHead = (w, s = 21, mt = 14) => <div style={{textAlign:'center',marginTop:mt}}>{tmxWord(w, s)}</div>;
const tmxMeanTxt = (w) => '“' + tmxOf(w).en + '”';
const tmxQuote = (x, mt = 16) => <div style={{textAlign:'center',fontSize:14,fontWeight:800,color:BK.ink,marginTop:mt,lineHeight:1.3,textWrap:'balance'}}>{x}</div>;
// words to circle, each its own size; the done one ringed in coral
const tmxCircleW = (words, on, size = 17, col) => <div style={{display:'flex',flexDirection:col ? 'column' : 'row',alignItems:'center',justifyContent:'center',gap:col ? 4 : 12,flexWrap:'wrap',margin:'4px 0 2px'}}>{words.map((w, i) => <span key={i} style={{border:'1.5px solid ' + (on === w ? BK.coral : 'transparent'),borderRadius:16,padding:'0 8px'}}>{tmxWord(w, size, on === w ? BK.coral : PEN_N)}</span>)}</div>;
const tmxTick = (w, size = 17) => <span key={w} style={{display:'flex',alignItems:'center',gap:8}}>{sprTick()}{tmxWord(w, size)}</span>;
const tmxTickRow = (ws) => <div style={{display:'flex',justifyContent:'center',gap:'8px 26px',flexWrap:'wrap'}}>{ws.map(w => tmxTick(w))}</div>;
const TMX_ORDER2 = ['Allegro', 'Adagio', 'Presto', 'Andante', 'Largo', 'Moderato'];   // number them, slowest first: 5 2 6 3 1 4 (no two neighbours on the ladder)
const tmxFaster = (a, b) => TMX_SPEED.findIndex(x => x.w === a) > TMX_SPEED.findIndex(x => x.w === b) ? a : b;
const TMX_SIX_C = [['ts', 3], ['q', 1, 28], ['q', 1, 28], ['q', 1, 28], ['|'], ['q', 1, 28], ['q', 1, 28], ['q', 1, 28], ['||']];
const tmxLouder = (a, b) => TMX_VOL6.indexOf(a) > TMX_VOL6.indexOf(b) ? a : b;

function TmxWorkbook({ startNo = 1 }) {
  const W = TMX_WB, pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + 1 + pages.length} chId="terms">{content}</WbPage>);
  const meanCell = (w, n, s = 21, h = 38) => <BkCell key={n} n={n}>{sdyCol(<>{tmxHead(w, s)}{tmxLine(false, '', h, 2)}</>, '6px 2px 8px')}</BkCell>;

  // 2 (faces "The speed ladder")
  P(<>
    <WbTop step={1}/>
    <Part kind="together" title="Which is faster?" how="Circle the faster word in each box. The first one is done.">
      <BkGrid cols={4} gap="8px 10px">{W.try2.map(([a, b], i) => <ExCell key={i} n={i + 1} ex={i === 0}>{sdyCol(<div style={{margin:'auto 0'}}>{tmxCircleW([a, b], i === 0 ? tmxFaster(a, b) : null, 21, true)}</div>, '30px 2px 18px')}</ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="What it means; in order" how="Write what each speed word means. Then number the six words in 11 from the slowest (1) to the fastest (6).">
      <div style={{display:'flex',flexDirection:'column',gap:8}}>
        <BkGrid cols={3} gap="8px 10px">{W.turn2.map((w, i) => meanCell(w, i + 5))}</BkGrid>
        <BkCell n={11}><div style={{display:'grid',gridTemplateColumns:'repeat(6,1fr)',justifyItems:'center',gap:6,padding:'14px 10px 8px'}}>{TMX_ORDER2.map(w => <div key={w} style={{display:'flex',flexDirection:'column',alignItems:'center',gap:6}}>{tmxWord(w, 18)}{bkBox(48, 44)}</div>)}</div></BkCell>
      </div>
    </Part>
    <Part kind="play" title="Four speeds" how="Play C D E F G at each speed. Your teacher plays a scale: say its word. Tick each one.">
      {sskRowN(12, <div style={{display:'flex',flexDirection:'column',gap:10,width:'100%'}}><div style={{maxWidth:600,margin:'0 auto',width:'100%'}}><TmxSpeedSvg nums label="The speed ladder, slow to fast, a metronome number by each word: Largo, Lento, Adagio, Andante, Moderato, Allegretto, Allegro, Vivace, Presto, Prestissimo."/></div><div style={{textAlign:'center',fontSize:12,color:BK.muted,marginTop:-4}}>The numbers are only about: pieces differ.</div>{tmxTickRow(['Lento', 'Andante', 'Allegretto', 'Presto'])}</div>)}
    </Part>
    <Faces/>
  </>);

  // 3 (faces "Changing speed")
  const beats = (w, k = 1, mw = 150) => <div style={{maxWidth:mw,margin:'0 auto',width:'100%'}}><TmxBeatsSvg gaps={TMX_GAPS[w].map(g => g * k)} x0={12} w0={174 * k} w={w} word={false} label={'A row of beats: ' + tmxOf(w).en + '.'}/></div>;
  P(<>
    <WbTop step={2}/>
    <Part kind="together" title="Read the beats" how="The dots are beats. Circle the word each row of beats shows. The first one is done.">
      <BkGrid cols={4} gap="8px 10px">{W.try3.map((w, i) => <ExCell key={i} n={i + 1} ex={i === 0}>{sdyCol(<>{beats(w)}
        <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',marginTop:'auto',rowGap:4}}>{['accel.', 'rit.', 'riten.', 'a tempo'].map(x => <div key={x}>{tmxCircleW([x], i === 0 ? w : null, 14.5)}</div>)}</div></>, '28px 2px 8px')}</ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="What it means; draw it" how="Write what each word means. Draw seven beats for rit. and for accel. Then circle the word that means the same as rall.">
      <div style={{display:'flex',flexDirection:'column',gap:8}}>
        <BkGrid cols={4} gap="8px 10px">{W.turn3.map((w, i) => meanCell(w, i + 5, 21, 44))}</BkGrid>
        <BkGrid cols={3} gap="8px 10px">{['rit.', 'accel.'].map((w, i) => <BkCell key={'d' + i} n={i + 9}>{sdyCol(<>{tmxHead(w, 20)}<div style={{height:100,margin:'auto 12px 6px',borderBottom:'1.3px dashed ' + BK.line}}/></>, '6px 2px 6px')}</BkCell>)}
          <BkCell n={11}>{sdyCol(<>{tmxQuote(<span>The same as {tmxWord('rall.', 16)}</span>, 14)}<div style={{margin:'auto 0 4px'}}>{tmxCircleW(['accel.', 'rit.', 'a tempo'], null, 17)}</div></>, '6px 2px 8px')}</BkCell></BkGrid>
      </div>
    </Part>
    <Part kind="play" title="Faster, slower, back" how="C D E F G A B C getting faster (accel.), then down getting slower (rit.). Then twelve Cs: four steady, four held back (riten.), four at the first speed again (a tempo). Tick each.">
      {sskRowN(12, <div style={{display:'grid',gridTemplateColumns:'110px minmax(0,1fr) 40px',alignItems:'center',gap:'22px 14px',width:'100%',maxWidth:580,margin:'0 auto'}}>{['accel.', 'rit.', 'riten.', 'a tempo'].map(w => [<div key={w} style={{textAlign:'right'}}>{tmxWord(w, 20)}</div>, <div key={w + 'b'}>{beats(w, 2.6, 400)}</div>, <span key={w + 't'}>{sprTick()}</span>])}</div>)}
    </Part>
    <Faces/>
  </>);

  // 4 (faces "Loud and soft")
  P(<>
    <WbTop step={3}/>
    <Part kind="together" title="Which is louder?" how="Circle the louder sign in each box. The first one is done.">
      <BkGrid cols={4} gap="8px 10px">{W.try4.map(([a, b], i) => <ExCell key={i} n={i + 1} ex={i === 0}>{sdyCol(<div style={{margin:'auto 0'}}>{tmxCircleW([a, b], i === 0 ? tmxLouder(a, b) : null, 28)}</div>, '34px 2px 22px')}</ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="The volume ladder" how={<span>Write these six signs in the boxes, softest first: {W.bank4.map((w, i) => <React.Fragment key={w}>{i > 0 && ' · '}{tmxWord(w, 15, BK.ink)}</React.Fragment>)}. Then write what each word means.</span>}>
      <div style={{display:'flex',flexDirection:'column',gap:8}}>
        <BkCell n={5}><div style={{padding:'12px 30px 10px'}}><svg viewBox="0 0 600 30" style={{width:'100%',display:'block'}} aria-hidden="true"><polygon points="20,15 580,3 580,27" fill="rgba(38,41,107,0.08)" stroke={PEN_N} strokeWidth="1.3" strokeLinejoin="round"/></svg>
          <div style={{display:'grid',gridTemplateColumns:'repeat(6,1fr)',justifyItems:'center',marginTop:8}}>{TMX_VOL6.map(w => <span key={w}>{bkBox(62, 58)}</span>)}</div></div></BkCell>
        <BkGrid cols={4} gap="8px 10px">{W.turn4.map((w, i) => meanCell(w, i + 6))}</BkGrid>
      </div>
    </Part>
    <Part kind="play" title="One rung louder" how={<span>{tmxRich('Play C six times, pp to ff. Then play the tune, doing what the signs say; then C D E F G with an sf on the G. Tick each.')}</span>}>
      {sskRowN(10, <div style={{display:'flex',flexDirection:'column',gap:10,width:'100%'}}>
        <div style={{maxWidth:322,margin:'0 auto',width:'100%'}}><SdyStaff full items={TMX_SIX_C} o={{ D: 46 }} k={{ dyn: TMX_VOL6.map((w, i) => [i, w]) }} label="Six crotchet Cs, pp, p, mp, mf, f, ff."/></div>
        <div style={{maxWidth:600,margin:'0 auto',width:'100%'}}><SdyStaff full items={SDY_ROWS.hair} o={{ D: 36 }} k={SDY_MARKS.hair} label="Four bars: C D E F from p getting louder; a semibreve G, f; G F E D getting softer; a semibreve C, p."/></div>{tmxTickRow(['pp → ff', 'the tune', 'sf'])}</div>)}
    </Part>
    <Faces/>
  </>);

  // 5 (faces "Touch and character")
  const bar = (w, mw = 150) => { const [k, nt] = TMX_T3B[w]; return <div style={{maxWidth:mw,margin:'0 auto',width:'100%'}}><SdyStaff full items={tmxBar(nt)} k={k} o={{ D: 20 }} label={'C D E F with ' + (k.slurs && k.stacc ? 'dots and a slur' : k.slurs ? 'a slur' : 'dots') + '.'}/></div>; };
  P(<>
    <WbTop step={4}/>
    <Part kind="together" title="Which touch?" how="Look at the marks. Circle legato, staccato or mezzo staccato. The first one is done.">
      <BkGrid cols={4} gap="8px 10px">{W.try5.map((w, i) => <ExCell key={i} n={i + 1} ex={i === 0}>{sdyCol(<>{bar(w)}<div style={{marginTop:'auto'}}>{tmxCircleW(['legato', 'staccato', 'mezzo staccato'], i === 0 ? w : null, 14, true)}</div></>, '26px 2px 8px')}</ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="What it means" how="Write what each word means.">
      <BkGrid cols={3} gap="8px 10px">{W.turn5.map((w, i) => meanCell(w, i + 5, 19, 44))}</BkGrid>
    </Part>
    <Part kind="play" title="Three touches, three characters" how="Play each bar with its touch. Then C D E F G three times: cantabile, leggiero, maestoso. Can your teacher tell which is which? Tick each.">
      {sskRowN(11, <div style={{display:'flex',flexDirection:'column',gap:12,width:'100%'}}>
        <div style={{display:'grid',gridTemplateColumns:'repeat(3,minmax(0,1fr))',gap:'4px 14px',alignItems:'start',justifyItems:'center'}}>{Object.keys(TMX_T3B).map(w => <div key={w} style={{width:'100%'}}>{bar(w, 220)}</div>)}{Object.keys(TMX_T3B).map(w => tmxTick(w, 16))}</div>
        {tmxTickRow(['cantabile', 'leggiero', 'maestoso'])}</div>)}
    </Part>
    <Faces/>
  </>);

  // 6 (faces "Little words")
  P(<>
    <WbTop step={5}/>
    <Part kind="together" title="Little word + term" how="Write what each term means. The first one is done.">
      <BkGrid cols={4} gap="8px 10px">{W.try6.map((w, i) => <ExCell key={i} n={i + 1} ex={i === 0}>{sdyCol(<>{tmxHead(w, 19)}{tmxLine(i === 0, tmxOf(w).en, 38, 2)}</>, '12px 2px 8px')}</ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Write the term; make one" how="Write the term for each meaning. In 11, make your own: a little word and a term, and what they mean together.">
      <div style={{display:'flex',flexDirection:'column',gap:8}}>
        <BkGrid cols={3} gap="8px 10px">{W.turn6.map((w, i) => <BkCell key={i} n={i + 5}>{sdyCol(<>{tmxQuote(tmxMeanTxt(w))}{tmxLine(false, '', 62)}</>, '6px 2px 8px')}</BkCell>)}</BkGrid>
        <BkCell n={11}><div style={{display:'grid',gridTemplateColumns:'110px 20px 130px 24px minmax(0,1fr)',alignItems:'end',gap:8,padding:'22px 14px 12px'}}>{bkBox(110, 50)}<span style={{fontWeight:900,color:BK.muted,textAlign:'center',paddingBottom:14}}>+</span>{bkBox(130, 50)}<span style={{fontWeight:900,color:BK.muted,textAlign:'center',paddingBottom:14}}>=</span><div style={{borderBottom:'1.3px solid ' + BK.line,height:50}}/></div></BkCell>
      </div>
    </Part>
    <Part kind="play" title="One piece, three ways" how="Play a piece you know sempre staccato, then più mosso, then with a poco rit. at the end. Then play your own term from 11. Tick each.">
      {sskRowN(12, <div style={{display:'grid',gridTemplateColumns:'30px 190px minmax(0,1fr)',alignItems:'center',gap:'14px 10px',width:'100%',maxWidth:520,margin:'0 auto'}}>{['sempre staccato', 'più mosso', 'poco rit.', null].map((w, i) => [<span key={i + 't'}>{sprTick()}</span>, <span key={i + 'w'}>{w ? tmxWord(w, 20) : <span style={{fontSize:15,fontWeight:800,color:BK.ink}}>My own (11)</span>}</span>, <span key={i + 'm'} style={{fontSize:13,fontWeight:700,color:BK.muted}}>{w ? tmxOf(w).en : ''}</span>])}</div>)}
    </Part>
    <Faces/>
  </>);

  // 7. any piece: a term hunt; 8. the check-up on paper
  P(<TmxHuntPage/>);
  P(<TmxPaperCheck/>);
  return <>{pages}</>;
}
function TmxHuntPage() {
  const fams = ['speed', 'change', 'vol', 'touch', 'little'];
  return <>
    <WbTop step={7}/>
    <div style={{display:'flex',justifyContent:'space-between',alignItems:'flex-end',gap:12,margin:'0 0 2px'}}>
      <div style={{minWidth:0}}><div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>ANY PIECE</div><div style={{fontSize:12.5,color:BK.muted,textWrap:'pretty'}}>Write the piece’s name. Each new piece gets a fresh copy of this page.</div></div>
      <span style={{display:'inline-block',width:230,borderBottom:'2px solid ' + BK.ink,height:26,flex:'0 0 auto'}}/></div>
    <Part kind="together" title="Term hunt" how="Find every word in the piece that says how to play. Write each in its family’s row, with what it means.">
      <div style={{display:'grid',gridTemplateColumns:'126px minmax(0,1fr) minmax(0,1fr)',border:'0.8px solid ' + BK.hair}}>
        {['', 'The words', 'What they mean'].map((h, i) => <div key={i} style={{fontSize:11,fontWeight:900,letterSpacing:'0.08em',textTransform:'uppercase',color:BK.muted,padding:'4px 8px',borderBottom:'0.8px solid ' + BK.hair,borderLeft:i ? '0.8px solid ' + BK.hair : 0}}>{h}</div>)}
        {fams.map(f => [<div key={f} style={{fontSize:13,fontWeight:900,color:BK.ink,padding:'8px',borderBottom:'0.8px solid ' + BK.hair,minHeight:74,display:'flex',alignItems:'center'}}>{TMX_FAM[f][0]}</div>,
          <div key={f + 'a'} style={{borderBottom:'0.8px solid ' + BK.hair,borderLeft:'0.8px solid ' + BK.hair}}/>, <div key={f + 'b'} style={{borderBottom:'0.8px solid ' + BK.hair,borderLeft:'0.8px solid ' + BK.hair}}/>])}
      </div>
    </Part>
    <Part kind="play" title="Play what it says" how="Play the piece, doing what each word says. Tick when your teacher says yes.">
      {sskRowN(1, <div style={{display:'flex',justifyContent:'center',gap:30,flexWrap:'wrap',fontSize:15,fontWeight:800,color:BK.ink}}>{['speed', 'changes', 'loud and soft', 'touch', 'little words'].map(w => sprTickW(w))}</div>)}
    </Part>
    <Part kind="year" title="My terms"><div style={{display:'grid',gridTemplateColumns:'repeat(4,1fr)',gap:'5px 10px'}}>{TMX.map(e => <div key={e.w} style={{display:'flex',alignItems:'center',justifyContent:'space-between',gap:6,borderBottom:'0.8px solid ' + BK.hair,padding:'1px 2px'}}>{tmxWord(e.w, 13.5)}{bkBox(16, 16)}</div>)}</div>
      <div style={{fontSize:12.5,color:BK.muted,marginTop:6}}>Tick a word when you can say what it means and play it. Keep this on your first copy.</div></Part>
    <Faces/>
  </>;
}
function TmxPaperCheck() {
  const C = TMX_CHK, { nB, nC, nD } = tmxChkNo();
  return <div className="lb-paper" style={{display:'flex',flexDirection:'column',gap:14,flex:'1 0 auto'}}>
    <LbPaperHead/>
    {bkSec('A', 'Write what each term means.')}
    <BkGrid cols={4} gap="6px 10px">{C.mean.map((w, i) => <BkCell key={i} n={i + 1}>{sdyCol(<>{tmxHead(w, w.length > 10 ? 18 : 22, 18)}{tmxLine(false, '', 48, 2)}</>, '6px 2px 8px')}</BkCell>)}</BkGrid>
    {bkSec('B', 'Write the sign.')}
    <BkGrid cols={3} gap="6px 10px">{C.sign.map((w, i) => <BkCell key={i} n={nB + i}>{sdyCol(<>{tmxQuote(tmxMeanTxt(w), 20)}<div style={{margin:'auto 0 8px'}}>{ivxAns(false, '', 92, 68)}</div></>, '6px 2px 8px')}</BkCell>)}</BkGrid>
    {bkSec('C', 'Circle one.')}
    <BkGrid cols={2} gap="6px 10px">{C.pick.map(([k, a, b], i) => <BkCell key={i} n={nC + i}>{sdyCol(<>{tmxQuote('The ' + k, 26)}<div style={{margin:'auto 0 16px'}}>{tmxCircleW([a, b], null, 30)}</div></>, '6px 2px 8px')}</BkCell>)}</BkGrid>
    {bkSec('D', 'Write the term.')}
    <BkGrid cols={3} gap="6px 10px">{C.term.map((w, i) => <BkCell key={i} n={nD + i}>{sdyCol(<>{tmxQuote(tmxMeanTxt(w), 20)}{tmxLine(false, '', 90)}</>, '6px 2px 8px')}</BkCell>)}</BkGrid>
  </div>;
}

function TmxTeacher() {
  const W = TMX_WB, C = TMX_CHK, pages = [], { nB, nC, nD, total } = tmxChkNo();
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="terms" teacher>{content}</WbPage>);
  const en = (w) => tmxOf(w).en, done = (i) => i === 0 ? ' (done)' : '';
  const order = TMX_ORDER2.map(w => w + ' ' + (TMX_SPEED.filter(x => TMX_ORDER2.includes(x.w)).findIndex(x => x.w === w) + 1)).join(', ');
  P(<>
    <div style={{fontFamily:"'Playfair Display', Georgia, serif",fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('terms')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 8px',lineHeight:1.5}}>{'Met before: chapter ' + bkChapterNo('dynamics') + ' (pp, p, mf, f, cresc., decresc., legato, staccato) and chapter ' + bkChapterNo('tempo') + ' (Adagio, Andante, Moderato, Allegro). AMEB Music Craft (2022): Preliminary, those words except cresc. and decresc. (Grade 1); Grade 1, Lento, Allegretto, Vivace, Presto, accel., rall., rit., riten., a tempo, mp, ff, cresc., decresc., sf (and rf); Grade 2, Largo, Prestissimo, Con moto, Maestoso, Più mosso, Meno mosso, sostenuto, sempre, poco, molto, senza, cantabile, leggiero, espressivo, mezzo staccato (and Vivo, Largamente, Larghetto, Allargando). ABRSM Music Theory asks Italian terms from Grade 1 (check the current list). Lesson Book page 1 is the expression ladder; the screen lesson ends with it again, the student ticking the words they know. Not here: Vivo, Largamente, Larghetto, Allargando, rf, Grade 3–4 and string terms (the toolbox: Term cards).'}</div>
    <div style={{border:'0.8px solid ' + BK.hair,padding:'6px 12px',margin:'0 0 8px',fontSize:12.5,color:BK.ink,lineHeight:1.5}}><b style={{color:BK.coral}}>Five families.</b> Speed, changing speed, loud and soft, touch and character, and the little words that change the term beside them. The speed numbers (page 2) are only about. The drill never sets Largo, Lento and Adagio against each other, nor Allegro against Vivace or Presto against Prestissimo; rall. and rit. mean the same.</div>
    <TcBlock page={2} title="The speed ladder" answers={<>{sscLesson('C D E F G at Lento, Andante, Allegretto and Presto; the teacher plays a scale and the child names its speed.')}{skgTcAns('TRY IT', W.try2.map(([a, b], i) => tmxFaster(a, b) + done(i)))}{skgTcAns('YOUR TURN', W.turn2.map(en).concat([order]), 5)}</>}
      watch="Allegretto taken as faster than Allegro (-etto: a little less). Lento and Largo mixed up: both slow, Largo also broad."
      say="“Largo at the bottom, Prestissimo at the top.”"/>
    <TcBlock page={3} title="Changing speed" answers={<>{sscLesson('C to C up with accel., down with rit.; then twelve Cs: four steady, four riten., four a tempo.')}{skgTcAns('TRY IT', W.try3.map((w, i) => w + done(i)))}{skgTcAns('YOUR TURN', W.turn3.map(en).concat(['dots further and further apart', 'dots closer and closer', 'rit.']), 5)}</>}
      watch="rit. played as a sudden change (that is riten.; some editions shorten ritenuto to rit. too: in this book rit. is always ritardando). a tempo read as “slower”: it means back to the speed before."
      say="“accel. faster, rit. slower, a tempo back.”"/>
    <TcBlock page={4} title="Loud and soft" answers={<>{sscLesson('C six times, pp to ff; C D E F G with a crescendo, then with an sf on G.')}{skgTcAns('TRY IT', W.try4.map(([a, b], i) => tmxLouder(a, b) + done(i)))}{skgTcAns('YOUR TURN', ['pp p mp mf f ff'].concat(W.turn4.map(en)), 5)}</>}
      watch="mp and mf swapped (m is medium: mp the softer). sf played as a loud passage, not one note."
      say="“pp p mp mf f ff.”"/>
  </>);
  P(<>
    <TcBlock page={5} title="Touch and character" answers={<>{sscLesson('C D E F three ways: legato, staccato, mezzo staccato; then C D E F G cantabile, leggiero and maestoso.')}{skgTcAns('TRY IT', W.try5.map((w, i) => w + done(i)))}{skgTcAns('YOUR TURN', W.turn5.map(en), 5)}</>}
      watch="Mezzo staccato played as staccato: it is half way. Sostenuto here means each note held its full length (not the pedal)."
      say="“Dots: short. A slur: smooth. Both: in between.”"/>
    <TcBlock page={6} title="Little words" answers={<>{sscLesson('C to C poco rit., then molto rit.; a known piece sempre staccato, then più mosso.')}{skgTcAns('TRY IT', W.try6.map((w, i) => en(w) + done(i)))}{skgTcAns('YOUR TURN', W.turn6.concat(['the student’s own']), 5)}</>}
      watch="più and meno swapped (più: more; meno: less). poco read as “slow”. senza rit. read as a rit."
      say="“A little word changes the term beside it.”"/>
    <TcBlock page={7} title="Any piece: a term hunt (a fresh copy for each piece)" answers={<div style={{fontSize:12,color:BK.ink,lineHeight:1.5}}>Every word in the student’s piece, by family, with its meaning. Words not in this chapter (dolce, rubato, D.C.): the toolbox’s Term cards, or chapter {bkChapterNo('signs')} for the signs. The year grid lists this chapter’s {TMX.length} words.</div>}/>
    <TcBlock page={8} title="The check-up on paper (the Workbook’s last page)" answers={<>
      {skgTcAns('A', C.mean.map(en))}
      {skgTcAns('B', C.sign, nB)}
      {skgTcAns('C', C.pick.map(([k, a, b]) => k === 'faster' ? tmxFaster(a, b) : tmxLouder(a, b)), nC)}
      {skgTcAns('D', C.term, nD)}
      <div style={{fontSize:12,color:BK.ink,marginTop:6,lineHeight:1.5}}>One mark each: A {C.mean.length}, B {C.sign.length}, C {C.pick.length}, D {C.term.length}; {total} in all. A: the student’s own words are fine (rit.: slowing down). B: sfz is right too. A section with a wrong answer is not passed yet: go back to its pages. Also listen to the student (My five checks, Lesson Book page 7).</div>
    </>}
      goBack={[{ id: 'a', step: '1 to 4', page: '2 to 5' }, { id: 'b', step: '3', page: '4' }, { id: 'c', step: '1 and 3', page: '2 and 4' }, { id: 'd', step: '2 and 5', page: '3 and 6' }]}/>
    <div style={{border:'0.8px solid ' + BK.hair,padding:'6px 12px',margin:'0 0 8px',fontSize:12,color:BK.ink,lineHeight:1.5}}><b style={{color:BK.coral}}>The drill (after page 6).</b> 1 speed words · 2 which is faster · 3 changing speed · 4 loud and soft · 5 listening (screen only) · 6 touch and character · 7 little words · 8 build the term · 9 extra: meaning → term.</div>
    <div style={{border:'0.8px solid ' + BK.hair,padding:'7px 12px',fontSize:12,color:BK.ink,lineHeight:1.5}}><b style={{color:BK.coral}}>My five checks (Lesson Book page 7).</b> 1. Put the ten speed words in order and say what each means. 2. Play accel., rit., riten. and a tempo. 3. Play C at all six rungs, a crescendo and an sf. 4. Play legato, staccato and mezzo staccato; name five character words. 5. Read and play poco rit., molto cresc., sempre staccato. Got it! means right without help.</div>
  </>);
  return <>{pages}</>;
}
WORKBOOKS['terms'] = TmxWorkbook;
TEACHER_COPIES['terms'] = TmxTeacher;
