// ─── Phase 482: chapter 26's Workbook (pages 2 to 8: one per lesson step, my composers, the check-up) and the Teacher
// copy. English only. ───
const CPX_WB = {
  life: [{ ids: ['vivaldi', 'bach', 'handel', 'scarlatti'], from: 1670, to: 1770, step: 10 }, { ids: ['haydn', 'clementi', 'mozart', 'beethoven'], from: 1725, to: 1835, step: 10 },
    { ids: ['schubert', 'chopin', 'rschumann', 'liszt', 'cschumann', 'brahms', 'tchaikovsky'], from: 1790, to: 1910, step: 10 }, { ids: ['debussy', 'joplin', 'bartok', 'prokofiev', 'kabalevsky', 'sculthorpe'], from: 1850, to: 2020, step: 20 }],
  // who wrote it: the pieces in this order, the names in that order; the first pair is done
  match: [{ left: ['vivaldi', 'bach', 'handel', 'scarlatti'], right: ['bach', 'scarlatti', 'vivaldi', 'handel'] }, { left: ['haydn', 'mozart', 'clementi', 'beethoven'], right: ['mozart', 'haydn', 'beethoven', 'clementi'] },
    { left: ['schubert', 'chopin', 'liszt', 'brahms', 'tchaikovsky'], right: ['chopin', 'tchaikovsky', 'schubert', 'brahms', 'liszt'] }, { left: ['debussy', 'joplin', 'bartok', 'prokofiev', 'williams', 'hisaishi'], right: ['prokofiev', 'debussy', 'hisaishi', 'joplin', 'williams', 'bartok'] }],
  rh: [44, 48, 34, 32],   // row heights (the pages fill)
  alive: [1745, 1785, 1815, 1845],
  // the words of each page, written from their meaning
  words: [[['counterpoint', 'two or more tunes at once, each as important as the other'], ['harpsichord', 'a keyboard whose strings are plucked'], ['Baroque', 'the period from about 1600 to 1750']],
    [['fortepiano', 'the early piano of Mozart’s time'], ['Alberti bass', 'a left hand that breaks a chord: lowest, highest, middle, highest'], ['Classical', 'the period from about 1750 to 1820']],
    [['rubato', 'time bent for feeling'], ['virtuoso', 'a performer with dazzling skill'], ['Romantic', 'the period from about 1820 to 1900']],
    [['Impressionism', 'music of soft colours and moods, about 1890 to 1920'], ['Modern', 'the period from about 1900 to 1950'], ['Contemporary', 'the period from 1950 to today']]],
  order: [['mozart', 'bach', 'chopin', 'debussy'], ['brahms', 'haydn', 'vivaldi', 'liszt'], ['kabalevsky', 'schubert', 'handel', 'joplin']],
};
const CPX_CHK = {
  era: ['handel', 'mozart', 'brahms', 'prokofiev', 'hisaishi', 'chopin'],
  year: [1720, 1790, 1860, 1930, 1985],
  word: ['counterpoint', 'fortepiano', 'rubato', 'contemporaries'],
  first: [['mozart', 'bach'], ['chopin', 'beethoven'], ['debussy', 'brahms'], ['haydn', 'vivaldi']],
  keys: ['bach', 'mozart', 'chopin'],   // the keyboard of their time (check 2)
};
const CPX_KEY_OF = { bach: 'harpsichord', mozart: 'fortepiano', chopin: 'piano' };
const cpxChkNo = () => { const C = CPX_CHK, nB = C.era.length + 1, nC = nB + C.year.length, nD = nC + C.word.length, nE = nD + C.first.length; return { nB, nC, nD, nE, total: nE + C.keys.length - 1 }; };
const cpxE = (id) => cmpById(id);
const cpxEn = { name: (id) => cpxE(id).name[0], sur: (id) => cpxE(id).sur[0], life: (id) => { const c = cpxE(id); return (c.bornApprox ? 'c. ' : '') + c.born + '–' + (c.died || ''); }, piece: (id) => CPX_PIECE[id][0], era: (id) => CMP_PERIODS[id].name[0].replace(/ \(.*\)$/, '') };
const cpxAliveIn = (y) => CPX_P6.filter(id => mtlAlive(cpxE(id), y));

// a ruler of years; each row a composer (name and years) and a track to draw the life on; the first row drawn (the example)
function CpxLifeRows({ from, to, step, ids, ex = true, W = 680, rh = 30, n0 }) {
  const LW = 172, x0 = LW + 12, x1 = W - 16, X = (y) => x0 + (y - from) / (to - from) * (x1 - x0), top = 24, H = top + ids.length * rh + 6;
  const ticks = [], minor = [];
  for (let v = Math.ceil(from / step) * step; v <= to; v += step) ticks.push(v);
  for (let v = Math.ceil(from / (step / 2)) * (step / 2); v <= to; v += step / 2) if (v % step) minor.push(v);
  return <svg viewBox={`0 0 ${W} ${H}`} role="img" aria-label={'A ruler from ' + from + ' to ' + to + ' and a row for each composer: ' + ids.map(id => cpxEn.name(id) + ' ' + cpxEn.life(id)).join('; ') + '.'} style={{width:'100%',height:'auto',display:'block',fontFamily:'Inter, system-ui, sans-serif'}}>
    {ticks.map(v => <g key={v}><text x={X(v)} y={12} textAnchor="middle" fontSize="11" fontWeight="800" fill={BK.ink}>{v}</text><line x1={X(v)} x2={X(v)} y1={16} y2={H - 4} stroke="rgba(38,41,107,0.28)" strokeWidth="0.8" strokeDasharray="2 3"/></g>)}
    {ids.map((id, i) => { const y = top + i * rh, mid = y + rh / 2, c = cpxE(id);
      return <g key={id}>
        {n0 != null && <text x={0} y={mid + 4} fontSize="13" fontWeight="700" fontStyle="italic" fill={i === 0 && ex ? BK.coral : BK.ink} style={{fontFamily:LB_SERIF}}>{n0 + i}</text>}
        <text x={n0 != null ? 20 : 0} y={mid + 4} fontSize="12.5" fontWeight="900" fill={BK.ink}>{cpxEn.sur(id)}</text>
        <text x={LW} y={mid + 4} textAnchor="end" fontSize="12" fontWeight="700" fill={BK.muted}>{cpxEn.life(id)}</text>
        <line x1={x0} x2={x1} y1={mid + 7} y2={mid + 7} stroke="rgba(38,41,107,0.45)" strokeWidth="0.9"/>
        {ticks.map(v => <line key={v} x1={X(v)} x2={X(v)} y1={mid + 3} y2={mid + 11} stroke="rgba(38,41,107,0.55)" strokeWidth="0.9"/>)}
        {minor.map(v => <line key={'m' + v} x1={X(v)} x2={X(v)} y1={mid + 5} y2={mid + 9} stroke="rgba(38,41,107,0.45)" strokeWidth="0.7"/>)}
        {ex && i === 0 && <rect x={X(c.born)} y={mid} width={X(c.died) - X(c.born)} height={7} rx={3.5} fill={BK.coral}/>}
      </g>; })}
  </svg>;
}
// join each piece to its composer: pieces on the left, names on the right, a dot at each end; the first pair joined
function CpxMatch({ left, right, rowH = 30, n0 }) {
  const W = 680, H = Math.max(left.length, right.length) * rowH + 4, xl = 262, xr = 450;
  const yl = (i) => 4 + i * rowH + rowH / 2, yr = (id) => 4 + right.indexOf(id) * rowH + rowH / 2;
  return <svg viewBox={`0 0 ${W} ${H}`} role="img" aria-label={'Pieces: ' + left.map(cpxEn.piece).join('; ') + '. Composers: ' + right.map(cpxEn.name).join('; ') + '.'} style={{width:'100%',height:'auto',display:'block',fontFamily:'Inter, system-ui, sans-serif'}}>
    {left.map((id, i) => <g key={'l' + id}>{n0 != null && <text x={0} y={yl(i) + 4.5} fontSize="13" fontWeight="700" fontStyle="italic" fill={i === 0 ? BK.coral : BK.ink} style={{fontFamily:LB_SERIF}}>{n0 + i}</text>}<text x={xl - 12} y={yl(i) + 4.5} textAnchor="end" fontSize="13" fontWeight="700" fontStyle="italic" fill={BK.ink}>{cpxEn.piece(id)}</text><circle cx={xl} cy={yl(i)} r="3.6" fill={BK.ink}/></g>)}
    {right.map((id, i) => <g key={'r' + id}><circle cx={xr} cy={yl(i)} r="3.6" fill={BK.ink}/><text x={xr + 12} y={yl(i) + 4.5} fontSize="13" fontWeight="900" fill={BK.ink}>{cpxEn.name(id)}</text></g>)}
    <line x1={xl} y1={yl(0)} x2={xr} y2={yr(left[0])} stroke={BK.coral} strokeWidth="2"/>
  </svg>;
}
const cpxWrite = (w = 300, h = 26) => <span style={{display:'inline-block',width:w,maxWidth:'100%',borderBottom:'1.3px solid ' + BK.line,height:h}}/>;
const cpxHand = (txt) => <span style={{fontFamily:"'Caveat', 'Comic Sans MS', cursive",fontSize:18,color:BK.coral,fontWeight:700}}>{txt}</span>;
const cpxCircleRow = (words) => <div style={{display:'flex',justifyContent:'center',gap:6,flexWrap:'wrap',fontSize:12,fontWeight:800,color:BK.ink}}>{words.map(w => <span key={w} style={{padding:'1px 6px'}}>{w}</span>)}</div>;

function CpxWorkbook({ startNo = 1 }) {
  const W = CPX_WB, pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + 1 + pages.length} chId="composers">{content}</WbPage>);
  const lifePart = (k) => { const L = W.life[k];
    return <Part kind="together" title="Draw the lives" how={'Each composer’s life is a bar from the year they were born to the year they died. Draw each one on its line. The first one is done.'}>
      <div style={{border:'0.8px solid ' + BK.hair,padding:'8px 10px 6px'}}><CpxLifeRows {...L} n0={1} rh={CPX_WB.rh[k]}/></div></Part>; };
  const matchPart = (k) => <Part kind="home" title="Who wrote it?" how="Join each piece to its composer with a line. The first one is done.">
    <div style={{border:'0.8px solid ' + BK.hair,padding:'8px 10px'}}><CpxMatch {...W.match[k]} n0={W.life[k].ids.length + 1} rowH={CPX_WB.rh[k]}/></div></Part>;
  const wordsPart = (ws, n0) => <Part kind="home" title="The words" how="Write the word for each meaning.">
    <BkGrid cols={ws.length} gap="6px 10px">{ws.map(([w, mean], i) => <BkCell key={w} n={n0 + i}>{sdyCol(<><div style={{textAlign:'center',fontSize:13,fontWeight:800,color:BK.ink,marginTop:14,lineHeight:1.3,textWrap:'balance'}}>“{mean}”</div><div style={{borderBottom:'1.3px solid ' + BK.line,height:34,margin:'auto 8px 4px'}}/></>, '6px 2px 8px')}</BkCell>)}</BkGrid></Part>;
  const eraPage = (k, play, words) => P(<>
    <WbTop step={k + 1}/>
    {lifePart(k)}
    {matchPart(k)}
    {wordsPart(words, W.life[k].ids.length + W.match[k].left.length + 1)}
    <Part kind="play" title="At the piano" how="Play, then tick each.">{sskRowN(W.life[k].ids.length + W.match[k].left.length + 4, ivxTicks(play))}</Part>
    <Faces/>
  </>);
  eraPage(0, ['a Baroque piece', 'its composer and years', 'one loudness, then soft and loud'], CPX_WB.words[0]);
  eraPage(1, ['an Alberti bass on C', 'a Classical piece', 'its composer and years'], CPX_WB.words[1]);
  eraPage(2, ['a slow tune with rubato', 'a Romantic piece', 'its composer and years'], CPX_WB.words[2]);
  eraPage(3, ['a Modern or Contemporary piece', 'its composer and years', 'blurred with the pedal'], CPX_WB.words[3]);

  // 6 (faces "Who lived when")
  P(<>
    <WbTop step={5}/>
    <Part kind="together" title="A line down from one year" how="Draw a line straight down from each year. Write who was alive then (born before it, died after it). The first one is done.">
      <div style={{border:'0.8px solid ' + BK.hair,padding:'8px 10px 4px'}}><MusTimeline en stack W={640} fs={10.5} laneH={14} barH={8} from={1670} to={1910} rows={['era', 'cmp']} ids={CPX_P6} year={W.alive[0]} step={20} label={'Fifteen lives, Baroque to Romantic, with a line down from ' + W.alive[0] + '.'}/></div>
      <div style={{display:'flex',flexDirection:'column',gap:4,marginTop:6}}>{W.alive.map((y, i) => <div key={y} style={{display:'grid',gridTemplateColumns:'26px 58px minmax(0,1fr)',alignItems:'end',gap:8,fontSize:14,fontWeight:900,color:BK.ink,minHeight:38}}>
        <span style={{fontFamily:LB_SERIF,fontStyle:'italic',fontWeight:700}}>{i + 1}</span><span>{y}</span>{i === 0 ? <span style={{borderBottom:'1.3px solid ' + BK.line}}>{cpxHand(cpxAliveIn(y).map(cpxEn.sur).join(', '))}</span> : <span style={{borderBottom:'1.3px solid ' + BK.line,height:26}}/>}</div>)}</div>
    </Part>
    <Part kind="home" title="Who came first?" how="Number each row 1 to 4, in the order they were born. Look back at Lesson Book pages 2 to 5. The first one is done.">
      <div style={{display:'flex',flexDirection:'column',gap:6}}>{W.order.map((g, i) => { const ord = [...g].sort((a, b) => cpxE(a).born - cpxE(b).born);
        return <div key={i} style={{display:'grid',gridTemplateColumns:'26px repeat(4,minmax(0,1fr))',alignItems:'center',gap:8,border:i === 0 ? '1.4px solid ' + BK.coral : '0.8px solid ' + BK.hair,background:i === 0 ? '#fff8f5' : '#fff',padding:'9px 8px'}}>
          <span style={{fontFamily:LB_SERIF,fontStyle:'italic',fontSize:13,fontWeight:700,color:i === 0 ? BK.coral : BK.ink}}>{i + 5}</span>
          {g.map(id => <span key={id} style={{display:'flex',alignItems:'center',gap:6,fontSize:13.5,fontWeight:900,color:BK.ink}}><span style={{width:24,height:24,border:'1.4px solid ' + BK.line,borderRadius:3,display:'inline-flex',alignItems:'center',justifyContent:'center',flex:'0 0 auto'}}>{i === 0 && cpxHand(ord.indexOf(id) + 1)}</span>{cpxEn.sur(id)}</span>)}</div>; })}</div>
    </Part>
    <Part kind="play" title="At the piano" how="Play, then tick each.">{sskRowN(8, ivxTicks(['Haydn: C\u00a0C\u00a0E\u00a0E\u00a0G\u00a0G\u00a0E', 'Beethoven: E\u00a0E\u00a0F\u00a0G\u00a0G\u00a0F\u00a0E\u00a0D', 'both found on the timeline']))}</Part>
    <Faces/>
  </>);
  // 7: my composers (any piece)
  P(<CpxMyComposers/>);
  // 8: the check-up
  P(<CpxPaperCheck/>);
  return <>{pages}</>;
}

function CpxMyComposers() {
  const head = ['My piece', 'Composer', 'Born–died', 'Period', 'Keyboard of their time'];
  const cols = 'minmax(0,1.4fr) minmax(0,1.2fr) 112px minmax(0,0.9fr) minmax(0,1.1fr)';
  return <>
    <WbTop step={7}/>
    <div style={{display:'flex',justifyContent:'space-between',alignItems:'flex-end',gap:12,margin:'0 0 2px'}}>
      <div style={{minWidth:0}}><div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>ANY PIECE</div><div style={{fontSize:12.5,color:BK.muted,textWrap:'pretty'}}>Keep this page all year. Add each new piece you learn.</div></div></div>
    <Part kind="together" title="My composers" how="For each piece: its composer, the years they lived, their period, and the keyboard of their time (harpsichord, fortepiano or piano). The composer’s name and years are printed above the music, on the right.">
      <div style={{border:'0.8px solid ' + BK.hair}}>
        <div style={{display:'grid',gridTemplateColumns:cols,gap:8,padding:'6px 10px',borderBottom:'1px solid ' + BK.line,fontSize:10.5,fontWeight:900,letterSpacing:'0.07em',textTransform:'uppercase',color:BK.muted}}>{head.map(h => <span key={h}>{h}</span>)}</div>
        {Array.from({ length: 10 }, (_, i) => <div key={i} style={{display:'grid',gridTemplateColumns:cols,gap:8,padding:'0 10px',height:34,borderBottom:'0.8px solid ' + BK.hair}}>{head.map(h => <span key={h} style={{borderRight:h === head[4] ? 'none' : '0.8px dotted ' + BK.hair}}/>)}</div>)}
      </div>
    </Part>
    <Part kind="home" title="My composers on the timeline" how="Draw each composer’s life above the periods, and write their name beside it.">
      <div style={{border:'0.8px solid ' + BK.hair,padding:'8px 10px 4px'}}>
        <MusTimeline en rows={['draw', 'era', 'keys']} ids={[]} label="Six empty lines to draw lives on, above the periods and keyboards from 1600 to today."/></div>
    </Part>
    <Part kind="play" title="At the piano" how="Play each piece on your list. Say its composer, years and period. Tick when your teacher says yes.">{sskRowN(1, ivxTicks(['composer', 'years', 'period']))}</Part>
    <Faces/>
  </>;
}
function CpxPaperCheck() {
  const C = CPX_CHK, { nB, nC, nD, nE } = cpxChkNo(), eras = MTL_ERAS.map(cpxEn.era);
  return <div className="lb-paper" style={{display:'flex',flexDirection:'column',gap:10,flex:'1 0 auto'}}>
    <LbPaperHead/>
    {bkSec('A', 'Which period? Circle one.')}
    <BkGrid cols={3} gap="6px 10px">{C.era.map((id, i) => <BkCell key={id} n={i + 1}>{sdyCol(<><div style={{textAlign:'center',fontSize:15,fontWeight:900,color:BK.ink,margin:'2px 0 6px'}}>{cpxEn.name(id)}</div>{cpxCircleRow(eras)}</>, '14px 4px 6px')}</BkCell>)}</BkGrid>
    {bkSec('B', 'Which period is this year in? Write it.')}
    <BkGrid cols={5} gap="6px 10px">{C.year.map((y, i) => <BkCell key={y} n={nB + i}>{sdyCol(<><div style={{textAlign:'center',fontFamily:LB_SERIF,fontSize:24,fontWeight:900,color:BK.ink,margin:'4px 0 0',fontVariantNumeric:'lining-nums'}}>{y}</div><div style={{borderBottom:'1.3px solid ' + BK.line,height:34,margin:'auto 6px 4px'}}/></>, '12px 2px 6px')}</BkCell>)}</BkGrid>
    {bkSec('C', 'Write the word.')}
    <BkGrid cols={4} gap="6px 10px">{C.word.map((w, i) => <BkCell key={w} n={nC + i}>{sdyCol(<><div style={{textAlign:'center',fontSize:13,fontWeight:800,color:BK.ink,marginTop:16,lineHeight:1.3,textWrap:'balance'}}>“{CPX_WORDS.find(x => x[0] === w)[1]}”</div><div style={{borderBottom:'1.3px solid ' + BK.line,height:40,margin:'auto 8px 4px'}}/></>, '6px 2px 8px')}</BkCell>)}</BkGrid>
    {bkSec('D', 'Who was born first? Circle one.')}
    <BkGrid cols={4} gap="6px 10px">{C.first.map(([a, b], i) => <BkCell key={a + b} n={nD + i}>{sdyCol(<div style={{display:'flex',justifyContent:'center',gap:14,fontSize:15,fontWeight:900,color:BK.ink,margin:'auto 0'}}><span>{cpxEn.sur(a)}</span><span>{cpxEn.sur(b)}</span></div>, '16px 4px 6px')}</BkCell>)}</BkGrid>
    {bkSec('E', 'Which keyboard did they write for? Circle one.')}
    <BkGrid cols={3} gap="6px 10px">{C.keys.map((id, i) => <BkCell key={id} n={nE + i}>{sdyCol(<><div style={{textAlign:'center',fontSize:15,fontWeight:900,color:BK.ink,margin:'2px 0 6px'}}>{cpxEn.name(id)}</div>{cpxCircleRow(['harpsichord', 'fortepiano', 'piano'])}</>, '14px 4px 6px')}</BkCell>)}</BkGrid>
  </div>;
}

function CpxTeacher() {
  const W = CPX_WB, C = CPX_CHK, pages = [], { nB, nC, nD, nE, total } = cpxChkNo();
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="composers" teacher>{content}</WbPage>);
  const done = (i) => i === 0 ? ' (done)' : '';
  const lifeAns = (k) => W.life[k].ids.map((id, i) => cpxEn.sur(id) + ' ' + cpxEn.life(id) + done(i));
  const matchAns = (k) => W.match[k].left.map((id, i) => cpxEn.piece(id).replace(/ \(film music\)$/, '') + ': ' + cpxEn.sur(id) + done(i));
  const wordAns = (k) => skgTcAns('THE WORDS', W.words[k].map(w => w[0]), W.life[k].ids.length + W.match[k].left.length + 1);
  const firstOf = ([a, b]) => cpxE(a).born < cpxE(b).born ? a : b;
  P(<>
    <div style={{fontFamily:"'Playfair Display', Georgia, serif",fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('composers')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 8px',lineHeight:1.5}}>{'The timeline of music: five periods, the keyboard of each time, and ' + CPX_IDS.length + ' composers placed on it. Chapter ' + bkChapterNo('piano-story') + ' (the harpsichord, the first piano, the fortepiano) comes first; chapter ' + bkChapterNo('styles') + ' reads the same timeline’s sound and styles rows. AMEB: general knowledge (the composer and period of each exam piece).'}</div>
    <div style={{border:'0.8px solid ' + BK.hair,padding:'6px 12px',margin:'0 0 8px',fontSize:11.5,color:BK.ink,lineHeight:1.42}}><b style={{color:BK.coral}}>Dates.</b> Period boundaries are conventions (Classical: 1730 or 1750 to 1820 or 1830). A composer’s period is when the music was written; Beethoven, Debussy and Kabalevsky (Op. 51, 60 and 89, 1952–74, are Contemporary) cross a boundary, and the drill never asks theirs. The keyboards row is simplified: harpsichords lasted past 1770; the piano row starts about 1830, as the iron frame came in (1825–1859, chapter {bkChapterNo('piano-story')}).</div>
    <TcBlock page={2} title="Baroque: 1600 to 1750" answers={<>{sscLesson('A Baroque piece with its composer and years; a tune at one loudness (harpsichord), then soft and loud (piano).')}{skgTcAns('TRY IT', lifeAns(0))}{skgTcAns('YOUR TURN', matchAns(0), W.life[0].ids.length + 1)}{wordAns(0)}</>}
      watch="A life drawn from tick to tick instead of from its own years: 1678 falls between 1670 and 1680. Three lives that start at the same tick (1685) are right, not a mistake."
      say="“Baroque: 1600 to 1750. Bach, Handel and Scarlatti were all born in 1685.”"/>
    <TcBlock page={3} title="Classical: 1750 to 1820" answers={<>{sscLesson('An Alberti bass on C (C G E G); a Classical piece with its composer and years.')}{skgTcAns('TRY IT', lifeAns(1))}{skgTcAns('YOUR TURN', matchAns(1), W.life[1].ids.length + 1)}{wordAns(1)}</>}
      watch="Haydn called Baroque because he was born in 1732: the period is when the music was written. The Alberti bass played as a block chord."
      say="“Classical: 1750 to 1820. Haydn, Mozart and Beethoven all worked in Vienna.”"/>
    <TcBlock page={4} title="Romantic: 1820 to 1900" answers={<>{sscLesson('A slow tune in strict time, then with a little rubato; a Romantic piece with its composer and years.')}{skgTcAns('TRY IT', lifeAns(2))}{skgTcAns('YOUR TURN', matchAns(2), W.life[2].ids.length + 1)}{wordAns(2)}</>}
      watch="Rubato that only slows down (it gives time back). Clara and Robert Schumann taken for one person: two lives, two composers."
      say="“Romantic: 1820 to 1900. Chopin and Robert Schumann were both born in 1810.”"/>
  </>);
  P(<>
    <TcBlock page={5} title="Modern and Contemporary: 1900 to today" answers={<>{sscLesson('A Modern or Contemporary piece, its composer and years; soft high notes blurred.')}{skgTcAns('TRY IT', lifeAns(3))}{skgTcAns('YOUR TURN', matchAns(3), W.life[3].ids.length + 1)}{wordAns(3)}</>}
      watch="“Modern” taken to mean today’s music: here it is 1900 to 1950; today’s is Contemporary. This ruler’s ticks are 20 years apart."
      say="“Modern: 1900 to 1950. Contemporary: 1950 to today.”"/>
    <TcBlock page={6} title="Who lived when" answers={<>{sscLesson('1685 on the timeline (Bach, Handel, Scarlatti born); Beethoven to Vienna in 1792 to study with Haydn; Haydn’s “Surprise” tune and Beethoven’s “Ode to Joy”.')}{skgTcAns('TRY IT', W.alive.map((y, i) => y + ': ' + cpxAliveIn(y).map(cpxEn.sur).join(', ') + done(i)))}{skgTcAns('YOUR TURN', W.order.map((g, i) => g.map(id => cpxEn.sur(id) + ' ' + ([...g].sort((a, b) => cpxE(a).born - cpxE(b).born).indexOf(id) + 1)).join(', ') + done(i)), 5)}</>}
      watch="A line drawn on a slant. (No year asked here is a year of birth or death.)"
      say="“Contemporaries lived at the same time. A line down from one year finds them.”"/>
    <TcBlock page={7} title="Any piece: my composers (one page, kept all year)" answers={<div style={{fontSize:12,color:BK.ink,lineHeight:1.5}}>Composer, years, period, keyboard (harpsichord to about 1770, fortepiano to about 1830, then piano). Others (Czerny, Grieg, Miriam Hyde …) by their years. The Minuet in G (Anna Magdalena Notebook) is by Petzold.</div>}/>
    <TcBlock page={8} title="The check-up on paper (the Workbook’s last page)" answers={<>
      {skgTcAns('A', C.era.map(id => cpxEn.era(cpxE(id).era)))}
      {skgTcAns('B', C.year.map(y => cpxEn.era(mtlEraOf(y))), nB)}
      {skgTcAns('C', C.word, nC)}
      {skgTcAns('D', C.first.map(p => cpxEn.sur(firstOf(p))), nD)}
      {skgTcAns('E', C.keys.map(id => CPX_KEY_OF[id]), nE)}
      <div style={{fontSize:12,color:BK.ink,marginTop:6,lineHeight:1.5}}>One mark each, {total} in all. A section with a wrong answer is not passed yet: go back to its pages. Also listen to the student (My five checks, page 7).</div>
    </>}
      goBack={[{ id: 'a', step: '1 to 4', page: '2 to 5' }, { id: 'b', step: '1 to 4', page: '2 to 5' }, { id: 'c', step: '1 to 5', page: '2 to 6' }, { id: 'd', step: '5', page: '6' }, { id: 'e', step: '1 to 3', page: '2 to 4' }]}/>
    <div style={{border:'0.8px solid ' + BK.hair,padding:'6px 12px',margin:'0 0 8px',fontSize:12,color:BK.ink,lineHeight:1.5}}><b style={{color:BK.coral}}>The drill (after page 6).</b> 1 period of a year · 2 period of a composer · 3 born first · 4 alive together · 5 who wrote it · 6 listening: Baroque, Classical or Romantic (real openings) · 7 listening: who wrote it (6, 7 screen only) · 8 the words · 9 extra: order of birth.</div>
  </>);
  return <>{pages}</>;
}
WORKBOOKS['composers'] = CpxWorkbook;
TEACHER_COPIES['composers'] = CpxTeacher;
