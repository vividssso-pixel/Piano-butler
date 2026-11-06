// ─── Phase 469: chapter 13's Workbook (pages 2 to 6 face Lesson Book pages 2 to 6: slow and fast; the four words;
// reading the tempo; the metronome; a steady tempo; page 7 the check-up on paper) and its Teacher copy. English, like
// every Workbook. Every task set (rule 3) and done alone (rule 4); a word to write is words to circle (rule 5); no PLAY
// task repeats its Lesson Book page. The sets' answers vary (rule 7).
// two rows of beats in the same five seconds, the top one at a, the bottom one at b (beats a minute)
const stmTwoRows = (a, b) => <svg viewBox="0 0 300 70" style={{width:'100%',display:'block'}}>
  {[[a, 18], [b, 52]].map(([n, y]) => <g key={y}><line x1={8} x2={292} y1={y} y2={y} stroke="rgba(38,41,107,0.2)" strokeWidth="1"/>{stmDotsRow(14, y, stmBeats(n, 5), 54, { r: 6 })}</g>)}</svg>;
// eight beats: steady, rushing or dragging (two of each kind, so no row repeats the worked example)
const STM_GAPS = { steady: [0, 1, 2, 3, 4, 5, 6, 7].map(i => i * 38), steady2: [0, 1, 2, 3, 4, 5, 6, 7].map(i => i * 33),
  rush: [0, 38, 74, 107, 137, 164, 188, 209], rush2: [0, 42, 82, 118, 150, 178, 201, 220],
  drag: [0, 30, 62, 97, 135, 176, 220, 267], drag2: [0, 26, 54, 85, 119, 157, 199, 246] };
const stmFeelRow = (k, w = 300) => <svg viewBox={'0 0 ' + w + ' 26'} style={{width:'100%',display:'block'}}>{STM_GAPS[k].map((x, i) => <circle key={i} cx={14 + x} cy={13} r="6.5" fill={PEN_N}/>)}</svg>;
const stmFeelOf = (k) => k.replace(/2$/, '');
// two metronomes, the weight high (slow) or low (fast)
const stmTwoMetros = (lowLeft) => <svg viewBox="0 0 200 120" style={{width:'100%',display:'block'}}>
  {[0, 1].map(i => { const low = (i === 0) === lowLeft, cx = 50 + i * 100; return <g key={i}><StmMetronome x={cx} y={108} h={96} wt={low ? 0.9 : 0.08}/></g>; })}</svg>;
// a pair of metronome marks, far enough apart to circle one
const stmMarkPair = (a, b, ring) => <div style={{display:'flex',justifyContent:'space-around',alignItems:'center',fontSize:19,padding:'16px 4px 6px'}}>{[a, b].map(n => <span key={n} style={{border:'1.6px solid ' + (ring && n === Math.max(a, b) ? BK.coral : 'transparent'),borderRadius:16,padding:'2px 10px'}}>{stmMm(n)}</span>)}</div>;
// what a mark means: words to circle
const stmMarkMean = (n, q, on) => <div style={{display:'flex',flexDirection:'column',alignItems:'center',gap:4,padding:'14px 4px 4px',fontSize:15,fontWeight:800,color:BK.ink}}>
  <span>{stmMm(n)}{q === 'min' ? ': ' + n + ' beats in' : ': beats a second'}</span>{sdyCircle(q === 'min' ? ['a minute', 'a second'] : ['1', '2'], on, false, 40)}</div>;
// a row for dots to be drawn: the first two given, the rest left blank
const stmDrawRow = (gap) => <svg viewBox="0 0 330 30" style={{width:'100%',display:'block'}}><line x1={6} x2={324} y1={15} y2={15} stroke="rgba(38,41,107,0.25)" strokeWidth="1" strokeDasharray="2 4"/>{[0, 1].map(i => <circle key={i} cx={14 + i * gap} cy={15} r="6.5" fill={PEN_N}/>)}</svg>;
const stmWordsCircle = (list, on) => <div style={{display:'flex',flexDirection:'column',alignItems:'center',gap:8,marginTop:'auto',paddingTop:6,fontSize:13,fontWeight:800,color:BK.ink}}>{list.map(w => <span key={w} style={{border:'1.5px solid ' + (on === w ? BK.coral : 'transparent'),borderRadius:13,padding:'1px 8px',color:on === w ? BK.coral : BK.ink,textAlign:'center'}}>{w}</span>)}</div>;
const stmMeanEn = (w) => ({ Adagio: 'slow', Andante: 'at a walking pace', Moderato: 'at a medium speed', Allegro: 'fast and lively' })[w];

const STM_WB = {
  rows: [[66, 132], [112, 72], [144, 88], [60, 120]],
  about: [['The beats come closer together.', 'yes'], ['The notes get louder.', 'no'], ['The notes get higher.', 'no'], ['The tune is over more quickly.', 'yes']],
  play2: ['hill', 'steps'],
  mean: [['Adagio', ['fast and lively', 'slow']], ['Allegro', ['fast and lively', 'at a walking pace']], ['Andante', ['at a walking pace', 'at a medium speed']], ['Moderato', ['slow', 'at a medium speed']]],
  order: [['Allegro', 'Adagio', 'Moderato', 'Andante'], ['Andante', 'Allegro', 'Adagio', 'Moderato']],
  pages: [{ en: 'Garden Path', dyn: 'p' }, { en: 'Rainy Day', dyn: 'mf', mark: true }, { en: 'Clock Tower', dyn: 'f' }, { en: 'Kite Song', dyn: 'p', mark: true }],
  fit: [['a sleepy lullaby', ['Adagio', 'Allegro'], 'Adagio'], ['a happy, quick dance', ['Adagio', 'Allegro'], 'Allegro'], ['a walk in the park', ['Allegro', 'Andante'], 'Andante'], ['not fast and not slow', ['Moderato', 'Adagio'], 'Moderato']],
  play4: [['Moderato', 'steps', 'count in 1 2 3 4'], ['Adagio', 'sway', 'count in 1 2 3']],
  marks: [['faster', 60, 120], ['min', 60], ['faster', 144, 66], ['sec', 120]],
  metros: [true, false, false, true],
  play5: [60, 80, 100, 120],
  feel: ['rush', 'drag', 'steady2', 'drag2'],
  draw: [['Adagio', 70], ['Allegro', 140], ['Andante', 90], ['Moderato', 110]],
};
const STM_CHK = {
  rows: [[132, 66], [88, 144], [120, 72], [120, 60]],
  mean: [['Andante', ['at a walking pace', 'fast and lively']], ['Allegro', ['slow', 'fast and lively']], ['Moderato', ['at a walking pace', 'at a medium speed']], ['Adagio', ['slow', 'at a medium speed']]],
  order: ['Moderato', 'Adagio', 'Allegro', 'Andante'],
  pages: [{ en: 'Snow at Night', dyn: 'mf', mark: true }, { en: 'Paper Boat', dyn: 'p' }],
  marks: [['faster', 120, 80], ['min', 90], ['faster', 72, 132], ['sec', 60]],
  feel: ['drag2', 'steady', 'rush'],
};
STM_ROWS.bells = [['ts', 4], ['q', 1, 30], ['q', 1, 32], ['q', 1, 30], ['q', 1, 28], ['|'], ['q', 1, 29], ['q', 1, 31], ['h', 2, 30], ['||']];
STM_ROWS.sway = [['ts', 3], ['h', 2, 28], ['q', 1, 30], ['|'], ['h', 2, 29], ['q', 1, 31], ['|'], ['hd', 3, 30], ['||']];
const stmFaster = ([a, b]) => b > a ? 'bottom' : 'top';
const stmMarkAns = (m) => m[0] === 'faster' ? Math.max(m[1], m[2]) : m[0] === 'min' ? 'a minute' : String(m[1] / 60);
const stmMarkCell = (m, ex) => m[0] === 'faster' ? stmMarkPair(m[1], m[2], ex) : stmMarkMean(m[1], m[0], ex ? stmMarkAns(m) : null);
const stmBoxW = (w, key) => <span key={key || w} style={{display:'flex',alignItems:'center',gap:8}}>{sprTick()}{w}</span>;

function StmWorkbook({ startNo = 1 }) {
  const W = STM_WB, pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + 1 + pages.length} chId="tempo">{content}</WbPage>);

  // 2 (faces "Slow and fast")
  P(<>
    <WbTop step={1}/>
    <Part kind="together" title="Which is faster?" how="Both rows last five seconds. Circle the faster row: top or bottom. The first one is done.">
      <BkGrid cols={2} gap="8px 14px">{W.rows.map((r, i) => <ExCell key={i} n={i + 1} ex={i === 0}>{sdyCol(<>{stmTwoRows(r[0], r[1])}{sdyCircle(['top', 'bottom'], i === 0 ? stmFaster(r) : null)}</>, '14px 6px 4px')}</ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Is it about tempo?" how="Circle yes if it is about the tempo, no if it is not.">
      <div style={{display:'grid',gap:8,maxWidth:600}}>{W.about.map(([s], i) => <div key={i} style={{display:'grid',gridTemplateColumns:'24px 1fr 130px',alignItems:'center',gap:8,fontSize:14.5,fontWeight:800,color:BK.ink}}>{sskNum(i + 5)}<span>{s}</span><span style={{display:'flex',justifyContent:'space-between',padding:'0 8px'}}><span style={{padding:'0 7px'}}>yes</span><span style={{padding:'0 7px'}}>no</span></span></div>)}</div>
    </Part>
    <Part kind="play" title="Play it slow, then fast" how="Right hand, thumb on middle C. Play each tune slow, then fast. Tick each one you play.">
      <div style={{display:'grid',gap:44}}>{W.play2.map((k, i) => sskRowN(i + 9, <div style={{display:'grid',gridTemplateColumns:'minmax(0,1fr) 120px',gap:16,alignItems:'center',width:'100%'}}>
        <div style={{maxWidth:510}}><SdyPaper mm={7} items={STM_ROWS[k]} o={{ D: 32 }}/></div>
        <div style={{display:'flex',flexDirection:'column',gap:12,fontSize:15,fontWeight:800,color:BK.ink}}>{sprTickW('slow', 's')}{sprTickW('fast', 'f')}</div></div>))}</div>
    </Part>
    <Faces/>
  </>);

  // 3 (faces "Four tempo words")
  P(<>
    <WbTop step={2}/>
    <Part kind="together" title="What does it mean?" how="Circle what each word means. The first one is done.">
      <BkGrid cols={4} gap="8px 10px">{W.mean.map(([w, opts], i) => <ExCell key={i} n={i + 1} ex={i === 0}>{sdyCol(<><div style={{textAlign:'center',fontFamily:STM_FONT,fontWeight:900,fontSize:21,color:BK.ink,padding:'4px 0 2px'}}>{w}</div>{stmWordsCircle(opts, i === 0 ? stmMeanEn(w) : null)}</>, '14px 2px 6px')}</ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Slow to fast" how="Number the words from the slowest (1) to the fastest (4).">
      <div style={{display:'grid',gap:14}}>{W.order.map((set, k) => sskRowN(k + 5, <div style={{display:'grid',gridTemplateColumns:'repeat(4,minmax(0,1fr))',gap:10}}>{set.map(w => <div key={w} style={{display:'flex',flexDirection:'column',alignItems:'center',gap:6}}><span style={{fontFamily:STM_FONT,fontWeight:900,fontSize:18,color:BK.ink}}>{w}</span>{sprBoxN()}</div>)}</div>))}</div>
    </Part>
    <Part kind="play" title="Play them four ways" how="Thumb on middle C. Play each tune four ways: Andante at your walking pace, Adagio slower, then Moderato and Allegro faster. Tick each one you play.">
      <div style={{display:'grid',gap:40}}>{['bells', 'sway'].map((k, i) => sskRowN(i + 7, <div style={{display:'flex',flexDirection:'column',gap:14,width:'100%',alignItems:'center'}}><div style={{width:'100%',maxWidth:500}}><SdyPaper mm={6.4} items={STM_ROWS[k]} o={{ D: 32 }}/></div>
        <div style={{display:'flex',justifyContent:'center',gap:26,flexWrap:'wrap',fontSize:15,color:BK.ink}}>{STM_WORDS.map(x => <span key={x.w} style={{display:'flex',alignItems:'center',gap:8}}>{sprTick()}<b style={{fontFamily:STM_FONT,fontWeight:900,fontSize:17}}>{x.w}</b></span>)}</div></div>))}</div>
    </Part>
    <Faces/>
  </>);

  // 4 (faces "Reading the tempo")
  P(<>
    <WbTop step={3}/>
    <Part kind="together" title="Find the tempo word" how="Circle the tempo word in each piece. The first one is done.">
      <BkGrid cols={2} gap="8px 14px">{W.pages.map((pg, i) => <ExCell key={i} n={i + 1} ex={i === 0}><div style={{padding:'10px 4px 2px'}}><StmMiniPage pg={pg} exWord={i === 0} maxW={270}/></div></ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Which word fits?" how="Circle the tempo word that fits each piece.">
      <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:'10px 26px'}}>{W.fit.map(([s, opts], i) => <div key={i} style={{display:'grid',gridTemplateColumns:'24px 1fr',alignItems:'center',rowGap:6,fontSize:14.5,fontWeight:800,color:BK.ink}}>{sskNum(i + 5)}<span>{s}</span><span/><span style={{display:'flex',gap:48}}>{opts.map(w => <span key={w} style={{fontFamily:STM_FONT,fontWeight:900,fontSize:15.5}}>{w}</span>)}</span></div>)}</div>
    </Part>
    <Part kind="play" title="Count in, then play" how="Read the tempo word. Count in one bar at that tempo, then play. Tick each one you play.">
      <div style={{display:'grid',gap:14}}>{W.play4.map(([w, k, ci], i) => sskRowN(i + 9, <div style={{display:'grid',gridTemplateColumns:'minmax(0,1fr) 170px',gap:16,alignItems:'center',width:'100%'}}>
        <div style={{maxWidth:370}}><StmTune items={STM_ROWS[k]} word={w}/></div>
        <span style={{display:'flex',alignItems:'center',gap:8,fontSize:14.5,fontWeight:800,color:BK.ink}}>{sprTick()}{ci}</span></div>))}</div>
    </Part>
    <Faces/>
  </>);

  // 5 (faces "The metronome")
  P(<>
    <WbTop step={4}/>
    <Part kind="together" title="Metronome marks" how="Circle the faster mark, or the right words. The first one is done.">
      <BkGrid cols={2} gap="8px 14px">{W.marks.map((m, i) => <ExCell key={i} n={i + 1} ex={i === 0}>{stmMarkCell(m, i === 0)}</ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Which ticks faster?" how="Circle the metronome that ticks faster.">
      <BkGrid cols={2} gap="8px 14px">{W.metros.map((lowLeft, i) => <BkCell key={i} n={i + 5}><div style={{padding:'12px 2px 2px',maxWidth:220,margin:'0 auto'}}>{stmTwoMetros(lowLeft)}</div></BkCell>)}</BkGrid>
    </Part>
    <Part kind="play" title="Play with a metronome" how="Set a metronome to each number. Play this tune, one beat on each tick. Colour a box for each one you play.">
      {sskRowN(9, <div style={{display:'flex',flexDirection:'column',gap:20,width:'100%',alignItems:'center'}}><div style={{width:'100%',maxWidth:520}}><SdyPaper mm={6.8} items={STM_ROWS.bells} o={{ D: 32 }}/></div>
        <div style={{display:'flex',justifyContent:'center',gap:26,flexWrap:'wrap',fontSize:18,color:BK.ink}}>{W.play5.map(n => <span key={n} style={{display:'flex',alignItems:'center',gap:8}}>{sprTick()}{stmMm(n)}</span>)}</div></div>)}
    </Part>
    <Faces/>
  </>);

  // 6 (faces "A steady tempo")
  P(<>
    <WbTop step={5}/>
    <Part kind="together" title="Steady, rushing or dragging?" how="Circle what each row of beats does. The first one is done.">
      <BkGrid cols={2} gap="8px 14px">{W.feel.map((k, i) => <ExCell key={i} n={i + 1} ex={i === 0}>{sdyCol(<><div style={{padding:'4px 10px 0'}}>{stmFeelRow(k)}</div>{sdyCircle(['steady', 'rushing', 'dragging'], i === 0 ? { steady: 'steady', rush: 'rushing', drag: 'dragging' }[stmFeelOf(k)] : null, false, 22)}</>, '16px 6px 4px')}</ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Draw it steady" how="Each row starts with two dots. Draw four more, the same gap every time.">
      <div style={{display:'grid',gap:12}}>{W.draw.map(([w, n], i) => <div key={w} style={{display:'grid',gridTemplateColumns:'24px 100px minmax(0,1fr)',alignItems:'center',gap:10}}>{sskNum(i + 5)}<span style={{fontFamily:STM_FONT,fontWeight:900,fontSize:16,color:BK.ink}}>{w}</span>{stmDrawRow(Math.round(3600 / n))}</div>)}</div>
    </Part>
    <Part kind="play" title="On, off, on" how="Set a metronome to 72. Play this tune three times without stopping: the sound on, then off, then on again. Colour a box each time.">
      {sskRowN(9, <div style={{display:'flex',flexDirection:'column',gap:20,width:'100%',alignItems:'center'}}><div style={{width:'100%',maxWidth:530}}><StmTune items={STM_ROWS.steps} word="Adagio" mark={72}/></div>
        <div style={{display:'flex',justifyContent:'center',gap:22,flexWrap:'wrap',fontSize:15,fontWeight:800,color:BK.ink}}>{['1st: with the ticks', '2nd: on my own', '3rd: still with them'].map(w => stmBoxW(w))}</div></div>)}
    </Part>
    <Faces/>
  </>);

  // 7. the check-up on paper
  P(<StmPaperCheck/>);
  return <>{pages}</>;
}
function StmPaperCheck() {
  const C = STM_CHK;
  return <div className="lb-paper" style={{display:'flex',flexDirection:'column',gap:4,flex:'1 0 auto'}}>
    <LbPaperHead/>
    {bkSec('A', 'Both rows last five seconds. Circle the faster row.')}
    <BkGrid cols={4} gap="6px 8px">{C.rows.map((r, i) => <BkCell key={i} n={i + 1}>{sdyCol(<>{stmTwoRows(r[0], r[1])}{sdyCircle(['top', 'bottom'], null, true, 18)}</>, '14px 4px 2px')}</BkCell>)}</BkGrid>
    {bkSec('B', 'Circle what each word means.')}
    <BkGrid cols={4} gap="6px 8px">{C.mean.map(([w, opts], i) => <BkCell key={i} n={i + 5}>{sdyCol(<><div style={{textAlign:'center',fontFamily:STM_FONT,fontWeight:900,fontSize:19,color:BK.ink}}>{w}</div>{stmWordsCircle(opts, null)}</>, '12px 2px 4px')}</BkCell>)}</BkGrid>
    {bkSec('C', 'Number the words from the slowest (1) to the fastest (4).')}
    <BkCell n={9}><div style={{display:'grid',gridTemplateColumns:'repeat(4,minmax(0,1fr))',gap:10,padding:'10px 10px 4px'}}>{C.order.map(w => <div key={w} style={{display:'flex',flexDirection:'column',alignItems:'center',gap:5}}><span style={{fontFamily:STM_FONT,fontWeight:900,fontSize:17,color:BK.ink}}>{w}</span>{sprBoxN()}</div>)}</div></BkCell>
    {bkSec('D', 'Circle the tempo word in each piece.')}
    <BkGrid cols={2} gap="6px 10px">{C.pages.map((pg, i) => <BkCell key={i} n={i + 10}><div style={{padding:'10px 4px 2px'}}><StmMiniPage pg={pg} maxW={250}/></div></BkCell>)}</BkGrid>
    {bkSec('E', 'Circle the faster mark, or the right words.')}
    <BkGrid cols={2} gap="6px 10px">{C.marks.map((m, i) => <BkCell key={i} n={i + 12}>{stmMarkCell(m)}</BkCell>)}</BkGrid>
    {bkSec('F', 'Steady, rushing or dragging?')}
    <BkGrid cols={3} gap="6px 8px">{C.feel.map((k, i) => <BkCell key={i} n={i + 16}><div style={{padding:'12px 4px 2px'}}>{stmFeelRow(k, 290)}<div style={{display:'flex',justifyContent:'space-around',fontSize:12.5,fontWeight:800,color:BK.ink,marginTop:6}}>{['steady', 'rushing', 'dragging'].map(w => <span key={w}>{w}</span>)}</div></div></BkCell>)}</BkGrid>
  </div>;
}

const stmLesson = (txt) => <div style={{fontSize:12,color:BK.ink,lineHeight:1.5,marginBottom:4}}><b style={{color:BK.coral}}>In the lesson</b>{'  '}{txt}</div>;
function StmTeacher() {
  const W = STM_WB, C = STM_CHK, pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="tempo" teacher>{content}</WbPage>);
  const rank = (w) => STM_WORDS.findIndex(x => x.w === w) + 1;
  const feelW = { steady: 'steady', rush: 'rushing', drag: 'dragging' };
  const markA = (m) => m[0] === 'faster' ? stmMm(stmMarkAns(m)) : stmMarkAns(m);
  const marks = { A: C.rows.length, B: C.mean.length, C: 1, D: C.pages.length, E: C.marks.length, F: C.feel.length };
  const total = Object.values(marks).reduce((a, b) => a + b, 0);
  P(<>
    <div style={{fontFamily:"'Playfair Display', Georgia, serif",fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('tempo')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 8px',lineHeight:1.5}}>Tempo is the speed of the beat (chapter {bkChapterNo('pulse')}: the steady beat; chapter {bkChapterNo('note-values')}: the crotchet). AMEB Preliminary: Adagio, Andante, Moderato and Allegro, and the metronome. Say them a-DAH-jo, an-DAN-tay, mod-er-AH-toh, a-LEG-roh. Each word sounds at one speed in the app (70, 90, 110, 140), so six seconds hold 7, 9, 11 and 14 beats; real music gives each word a span (about Adagio 66 to 76, Andante 76 to 108, Moderato 108 to 120, Allegro 120 to 168, as on a metronome's scale; sources differ). The tempo word is printed in bold above the first bar; a metronome mark may stand beside it. No metronome at home? Lesson Book page 5 online has one. Drill: in the book's order (1 page 2; 2 to 5 page 3; 6 page 4; 7 page 5; 8 page 6); 9 (rit., accel., a tempo, Presto) is extra, for Grade 1.</div>
    <div style={{fontSize:12.5,color:BK.ink,margin:'0 0 12px',lineHeight:1.5,border:'0.8px solid ' + BK.hair,padding:'7px 10px'}}><b style={{color:BK.coral}}>Lesson time: walk the tempo.</b> Play a tune; the child walks to its beat. Change the tempo word (Adagio, Andante, Moderato, Allegro) and they change their steps.</div>
    <TcBlock page={2} title="Slow and fast" answers={<>{stmLesson('Play one tune slow and fast; the child claps the beat. Then the child plays and you clap.')}{tcAns('TRY IT', W.rows.map(stmFaster))}{tcAns('YOUR TURN', W.about.map(s => s[1]), 5)}{tcAns('PLAY', ['the first tune slow, then fast', 'the second tune slow, then fast'], 9)}</>}
      watch="Fast taken to mean loud. Short notes taken for a fast tempo: quavers at Adagio still sit on slow beats. Speeding up only in the easy bars."
      say="“Tempo: how fast the beat goes. Same notes, new tempo.”"/>
    <TcBlock page={3} title="Four tempo words" answers={<>{stmLesson('Say a word; the child walks or claps at that tempo. Swap: the child says a word, you walk.')}{tcAns('TRY IT', W.mean.map(([w]) => stmMeanEn(w)))}{tcAns('YOUR TURN', W.order.map(set => set.map(rank).join(' ')), 5)}{tcAns('PLAY', ['the first tune at the four tempos', 'the second tune at the four tempos'], 7)}</>}
      watch="Andante taken for slow: it is a walking pace, between Adagio and Moderato. Andante and Moderato mixed up. The words read as English: say them together."
      say="“Adagio, Andante, Moderato, Allegro: slow to fast.”"/>
    <TcBlock page={4} title="Reading the tempo" answers={<>{stmLesson('Open a piece the child is learning: find its tempo word together, count in one bar at that tempo, and play.')}{tcAns('TRY IT', W.pages.map(pg => stmPiece(pg.en).w))}{tcAns('YOUR TURN', W.fit.map(f => f[2]), 5)}{tcAns('PLAY', W.play4.map(([w, , ci]) => ci + ' at ' + w + ', then play'), 9)}</>}
      watch="The title, the metronome mark or a dynamic (mf) taken for the tempo word. Counting in at one speed and playing at another. Starting with no count-in."
      say="“Read the tempo word first. Count in, then play.”"/>
  </>);
  P(<>
    <TcBlock page={5} title="The metronome" answers={<>{stmLesson('Show a metronome, a real one or an app: set 60, then 120. On a wind-up one, slide the weight down (faster) and up (slower).')}{tcAns('TRY IT', W.marks.map(markA))}{tcAns('YOUR TURN', W.metros.map(l => l ? 'the left one (weight low)' : 'the right one (weight low)'), 5)}{tcAns('PLAY', [<>{W.play5.map((n, i) => <React.Fragment key={n}>{i ? ', ' : ''}{stmMm(n)}</React.Fragment>)}, a box for each</>], 9)}</>}
      watch="The weight moved the wrong way: down is faster. A mark of 60 read as ‘60 seconds’: it is 60 beats in a minute. Playing a note between the ticks; holding long notes short."
      say={<>“{stmMm(60)}: 60 beats a minute, one every second.”</>}/>
    <TcBlock page={6} title="A steady tempo" answers={<>{stmLesson('Play together with the metronome, then turn its sound off for a bar or two and on again: still together?')}{tcAns('TRY IT', W.feel.map(k => feelW[stmFeelOf(k)]))}{tcAns('YOUR TURN', W.draw.map(([w]) => 'four more dots, the gap as given (' + w + ')'), 5)}{tcAns('PLAY', ['three times at 72: with the ticks, alone, with them again'], 9)}</>}
      watch="Rushing in easy bars and dragging in hard ones. No wind-up metronome mutes: use an app, or the one on Lesson Book page 5 online (Sound off keeps the beat going). Slowing down at the end without a sign. Stopping to fix a note: keep the beat going instead."
      say="“Keep the tempo steady: no rushing, no dragging.”"/>
    <TcBlock page={7} title="The check-up on paper (the Workbook's last page)" answers={<>
      {tcAns('A', C.rows.map(stmFaster))}
      {tcAns('B', C.mean.map(([w]) => stmMeanEn(w)), 5)}
      {tcAns('C', [C.order.map(rank).join(' ')], 9)}
      {tcAns('D', C.pages.map(pg => stmPiece(pg.en).w), 10)}
      {tcAns('E', C.marks.map(markA), 12)}
      {tcAns('F', C.feel.map(k => feelW[stmFeelOf(k)]), 16)}
      <div style={{fontSize:12,color:BK.ink,marginTop:6,lineHeight:1.5}}>One mark for each answer; C is one mark if all four numbers are right: A {marks.A}, B {marks.B}, C {marks.C}, D {marks.D}, E {marks.E}, F {marks.F}; {total} in all. A section with any wrong answer is not passed yet: go back to its page below. Also listen to the student (My five checks, Lesson Book page 7).</div>
    </>}
      goBack={[{ id: 'a', step: 1, page: 2 }, { id: 'b', step: 2, page: 3 }, { id: 'c', step: 2, page: 3 }, { id: 'd', step: 3, page: 4 }, { id: 'e', step: 4, page: 5 }, { id: 'f', step: 5, page: 6 }]}/>
    <div style={{border:'0.8px solid ' + BK.hair,padding:'7px 12px',fontSize:12,color:BK.ink,lineHeight:1.5}}><b style={{color:BK.coral}}>My five checks (Lesson Book page 7): what to ask.</b> 1. Page 2: what tempo is; a tune slow, then fast. 2. Page 3: the four words in order, with their meanings. 3. Page 4: the tempo word in a piece; a count-in at that tempo. 4. Page 5: what {stmMm(60)} means; a tune with a metronome. 5. Page 6: a tune with the metronome, its sound off for a bar or two, then on: still together. Got it! means right without help.</div>
  </>);
  return <>{pages}</>;
}
WORKBOOKS.tempo = StmWorkbook;
TEACHER_COPIES.tempo = StmTeacher;
