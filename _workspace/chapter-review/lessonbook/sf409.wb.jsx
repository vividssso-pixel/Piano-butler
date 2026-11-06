// ─── the Workbook (Phase 409, Sohyun: "the staves are too small -- bigger, so drawing is easier; use the page") ───
// One long staff per exercise, the answer boxes under the notes: about 5 mm between the lines on paper.
function sfWorkbook() {
  const k = (s) => 'sf-wb409-' + s;
  const rnd = (a, b) => a + Math.floor(Math.random() * (b - a + 1));
  const run = (n, lo, hi) => { const out = []; for (let i = 0; i < n; i++) { let d; do { d = rnd(lo, hi); } while (out.length && out[out.length - 1].d === d); out.push({ d }); } return out; };
  const mkSS = (lo, hi) => { for (;;) { const a = rnd(lo, hi), gap = Math.random() < 0.5 ? 1 : 2, dir = Math.random() < 0.5 ? 1 : -1, b = a + gap * dir; if (b >= lo && b <= hi) return { a, b }; } };
  const s1 = withSeed(k('s1'), () => ({ tog: run(4, 30, 38), home: run(6, 30, 38) }));
  const s2 = withSeed(k('s2'), () => ({ tog: Array.from({ length: 3 }, () => mkSS(30, 38)), home: Array.from({ length: 4 }, () => mkSS(30, 38)), hi: Array.from({ length: 4 }, () => mkSS(30, 38)),
    stair: (() => { let d = 31; const moves = []; for (let i = 0; i < 5; i++) { let m; do { m = [1, 2, -1, -2][Math.floor(Math.random() * 4)]; } while (d + m < 30 || d + m > 38); d += m; moves.push({ m, d }); } return { start: 31, moves }; })() }));
  const s3 = withSeed(k('s3'), () => ({ home: run(6, 28, 32) }));
  const s4 = withSeed(k('s4'), () => {
    let r = rnd(0, 2); const path = [[r, 0]];
    for (let c = 1; c < 5; c++) { r = Math.max(0, Math.min(2, r + rnd(-1, 1))); path.push([r, c]); }
    const grid = Array.from({ length: 3 }, () => Array.from({ length: 5 }, () => rnd(25, 28)));
    path.forEach(([pr, pc]) => { grid[pr][pc] = 24; });
    return { home: run(6, 24, 28), grid, path };
  });
  const s5 = withSeed(k('s5'), () => {
    const cs = shuffle([0, 1, 2, 3, 4, 5, 6, 7]).slice(0, 3), rest = [24, 25, 26, 27, 29, 30, 31, 32];
    return { mid: [0, 1, 2, 3, 4, 5, 6, 7].map(i => cs.includes(i) ? { d: 28, staff: Math.random() < 0.5 ? 'treble' : 'bass' } : { d: rest[Math.floor(Math.random() * rest.length)] }) };
  });
  const s6 = withSeed(k('s6'), () => ({ bingo: shuffle([24, 25, 26, 27, 28, 29, 30, 31, 32]) }));
  return { s1, s2, s3, s4, s5, s6 };
}
const sfLS = (d, clef = 'treble') => (d - CLEFS[clef].low) % 2 === 0 ? 'L' : 'S';
const sfSSName = (it) => (Math.abs(it.b - it.a) === 1 ? 'step ' : 'skip ') + (it.b > it.a ? 'up' : 'down');
const SF_MOVE = { 1: 'step up', 2: 'skip up', '-1': 'step down', '-2': 'skip down' };
// the secret words, spelled with the nine notes round Clara (w3; CABBAGE is the long one)
const SF_MSG = [
  { word: 'BAG', clef: 'bass', notes: [27, 26, 25] },
  { word: 'FED', clef: 'treble', notes: [31, 30, 29] },
  { word: 'EGG', clef: 'treble', notes: [30, 32, 32] },
  { word: 'CABBAGE', clef: 'grand', notes: [28, 26, 27, 27, 26, 25, 30] },
];
// note positions along a staff of width w (room for the clef when there is one)
const sfXs = (n, w, clefOn) => { const a = clefOn ? 82 : 36, b = w - 32; return Array.from({ length: n }, (_, i) => n === 1 ? (a + b) / 2 : a + i * (b - a) / (n - 1)); };
// a big staff row: notes at set places, a number over each, an answer box (or a label) under each
function SfRow({ clef = 'none', notes = [], width = 360, items = [], minSpan, boxW = 40, boxH = 32 }) {
  const clefOn = clef !== 'none';
  const pct = (x) => (x / width * 100) + '%';
  return <div style={{width:'100%'}}>
    {items.some(it => it.n != null) && <div style={{position:'relative',height:15}}>{items.map((it, i) => it.n != null && <span key={i} style={{position:'absolute',left:pct(it.x),transform:'translateX(-50%)',fontSize:11,fontWeight:900,color:BK.coral,whiteSpace:'nowrap'}}>{it.ex ? 'e.g.' : it.n}</span>)}</div>}
    <PaperStaff clef={clefOn ? clef : 'treble'} clefOn={clefOn} notes={notes} width={width} minSpan={minSpan}/>
    {items.some(it => it.box !== false) && <div style={{position:'relative',height:boxH + 4,marginTop:3}}>{items.map((it, i) => it.box !== false && (it.label != null
      ? <span key={i} style={{position:'absolute',left:pct(it.x),transform:'translateX(-50%)',top:4,fontSize:12,fontWeight:900,color:BK.ink,whiteSpace:'nowrap',background:BK.soft,borderRadius:12,padding:'3px 9px'}}>{it.label}</span>
      : <span key={i} style={{position:'absolute',left:pct(it.x),transform:'translateX(-50%)',top:0,width:it.w || boxW,height:boxH,border:'1.5px solid ' + (it.ex ? BK.coral : BK.ink),borderRadius:7,background:it.ex ? '#fdf3ef' : '#fff',display:'flex',alignItems:'center',justifyContent:'center',fontSize:it.w ? 13 : 16,fontWeight:900,color:BK.coral,whiteSpace:'nowrap'}}>{it.ex ? it.ans : ''}</span>))}</div>}
  </div>;
}
// one long staff with the clef four times: the first solid, the rest faint to trace (N4/N5)
function SfTraceStaff({ clef, n = 4, width = 380 }) {
  const c = CLEFS[clef], g = CLEF_GLYPH[clef];
  const yOf = (d) => dY(d);
  const y0 = Math.min(yOf(c.high), yOf(g.top) - g.topPad) - 6, y1 = Math.max(yOf(c.low), yOf(g.bottom) + g.bottomPad) + 6;
  const step = (width - 10) / n;
  return <svg viewBox={`0 ${y0} ${width} ${y1 - y0}`} style={{width:'100%',display:'block'}} aria-hidden="true">
    {c.lines.map(l => <line key={l} x1="2" x2={width - 2} y1={yOf(l)} y2={yOf(l)} stroke={l === (clef === 'treble' ? 32 : 24) ? BK.coral : BK.ink} strokeOpacity={l === (clef === 'treble' ? 32 : 24) ? 0.5 : 0.6} strokeWidth={l === (clef === 'treble' ? 32 : 24) ? 2.2 : 1.1}/>)}
    {Array.from({ length: n }, (_, i) => <g key={i} transform={`translate(${6 + i * step} 0)`}><ClefGlyph clef={clef} st={clef} yOf={(d) => yOf(d)} ink={i === 0 ? BK.ink : '#c9c4de'}/></g>)}
  </svg>;
}
const sfPlate = (label, kids) => <div style={{border:'1.8px solid ' + BK.ink,borderRadius:46,padding:'8px 26px 10px',background:'#fff'}}>
  <div style={{textAlign:'center',fontSize:12.5,fontWeight:900,color:BK.ink,marginBottom:2}}>{label}</div>{kids}</div>;

function SfWorkbook({ startNo = 1, frames = true }) {
  const W = useMemo(() => sfWorkbook(), [LANG]);
  const pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + 1 + pages.length} chId="staff">{content}</WbPage>);
  const sub = (title, how) => <><div style={{fontFamily:"'Playfair Display', Georgia, serif",fontSize:17,fontWeight:800,color:BK.ink,margin:'10px 0 2px'}}>{title}</div>{how && <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 6px',lineHeight:1.45}}>{how}</div>}</>;
  const singles = (list, width, clef, exFirst, from = 1) => { const xs = sfXs(list.length, width, clef !== 'none');
    return <SfRow clef={clef} width={width} notes={list.map((it, i) => ({ d: it.d, x: xs[i] }))} minSpan={clef === 'bass' ? [29, 17] : clef === 'treble' ? [27, 39] : undefined}
      items={list.map((it, i) => ({ x: xs[i], n: from + i, ex: exFirst && i === 0, ans: clef === 'none' ? sfLS(it.d) : dName(it.d) }))}/>; };
  const pairs = (list, width, opts = {}) => { const cs = sfXs(list.length, width, false).map((c, i, a) => list.length === 1 ? c : 50 + i * (width - 100) / (list.length - 1));
    return <SfRow width={width} notes={list.flatMap((it, i) => [{ d: it.a, x: cs[i] - 16 }, { d: it.b, x: cs[i] + 16 }])}
      items={list.map((it, i) => ({ x: cs[i], n: (opts.from || 1) + i, ex: opts.ex && i === 0, ans: sfSSName(it), w: 88, box: opts.box }))}/>; };

  // 2 (faces "Lines and spaces")
  P(<>
    <WbTop step={1}/>
    <Part kind="together" title="Line or space?" how="Kebab = on a line, write L. Sandwich = in a space, write S. Count from the bottom.">
      <Lead max={400}><KebabSandwich/></Lead>
      {singles(W.s1.tog, 380, 'none', true)}
    </Part>
    <Part kind="home" title="Your turn" how="L or S -- and add the number if you can: L3 is line 3, S2 is space 2.">
      {singles(W.s1.home, 380, 'none', false, 5)}
    </Part>
    <Part kind="play" title="Kebab plate, sandwich plate" how="Cook! Draw three kebabs on the kebab plate -- notes ON a line -- and three sandwiches on the sandwich plate -- notes IN a space.">
      <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:16}}>
        {sfPlate('Kebab plate · line notes', <PaperStaff clefOn={false} notes={[]} width={170} minSpan={[29, 39]}/>)}
        {sfPlate('Sandwich plate · space notes', <PaperStaff clefOn={false} notes={[]} width={170} minSpan={[29, 39]}/>)}
      </div>
    </Part>
  </>);
  // 3 (faces "Up the staff, up the piano")
  P(<>
    <WbTop step={2}/>
    <Part kind="together" title="Step or skip? Up or down?" how="From the first note to the second. Write it, like “step up” or “skip down”.">
      {pairs(W.s2.tog, 380, { ex: true })}
    </Part>
    <Part kind="home" title="Your turn">
      {pairs(W.s2.home, 400, { from: 4 })}
    </Part>
    <Part kind="play" title="Which is higher? · The staircase tune" how="Circle the higher note in each pair -- then play both and check with your ears.">
      {pairs(W.s2.hi, 400, { box: false })}
      {sub('The staircase tune', 'The first note is drawn. Follow the signs left to right and draw each next note -- then play your staircase and hear it climb and fall.')}
      <SfRow width={420} notes={[{ d: W.s2.stair.start, x: 40, color: BK.coral }]} minSpan={[29, 39]}
        items={W.s2.stair.moves.map((mv, i) => ({ x: 40 + (i + 1) * 72, label: SF_MOVE[mv.m] }))}/>
    </Part>
  </>);
  // 4 (faces "The Queen's five")
  P(<>
    <WbTop step={3}/>
    <Part kind="together" title="Trace the Queen's curl" how="A treble clef starts on the G line -- the Queen's house, in coral -- and spirals out. Trace the faint ones.">
      <SfTraceStaff clef="treble"/>
    </Part>
    <Part kind="home" title="The Queen's five: name the notes" how="Count up from Clara's C or down from the Queen's G.">
      {singles(W.s3.home, 400, 'treble', true)}
    </Part>
    <Part kind="play" title="Make a tune for the Queen" how="Draw any FOUR of her five notes -- C D E F G -- your own tune! Write the letters in the boxes, then play it to someone with your right hand.">
      <SfRow clef="treble" width={400} notes={[]} minSpan={[27, 34]} items={sfXs(4, 400, true).map((x, i) => ({ x, n: i + 1 }))}/>
      <div style={{fontSize:12.5,color:BK.muted,textAlign:'center',marginTop:8}}>The name of my tune: ______________________</div>
    </Part>
  </>);
  // 5 (faces "The King's five")
  P(<>
    <WbTop step={4}/>
    <Part kind="together" title="Trace the King's guards" how="A bass clef starts with a dot on the F line -- the King's house, in coral -- curls down, then the two guards: one above the F line and one below.">
      <SfTraceStaff clef="bass"/>
    </Part>
    <Part kind="home" title="The King's five: name the notes" how="Start from the King's F -- the line between the two guards -- or from Clara's C.">
      {singles(W.s4.home, 400, 'bass', true)}
    </Part>
    <Part kind="play" title="Help the King get home" how="Colour every F. The F stones touching each other make the road from the King to his castle.">
      <div style={{display:'flex',alignItems:'center',gap:8}}>
        <PenArt shapes={sfKing(22, 26, 1)} vb={[4, 0, 36, 48]} style={{width:44,flex:'0 0 auto'}} label="the King"/>
        <div style={{flex:1}}><BkGrid cols={5} gap="6px 6px">{W.s4.grid.flatMap((row, r) => row.map((d, c) => <div key={r + '-' + c} style={{border:'1.2px solid #e2dccb',borderRadius:9,padding:'3px 5px'}}><PaperStaff clef="bass" notes={[{ d }]} width={76} minSpan={[29, 17]}/></div>))}</BkGrid></div>
        <svg viewBox="0 0 36 48" style={{width:44,flex:'0 0 auto'}} aria-label="his castle"><path d="M6 44 V20 H10 V15 H14 V20 H16 V15 H20 V20 H22 V15 H26 V20 H30 V44 Z" fill={BK.soft} stroke={BK.ink} strokeWidth="1.8" strokeLinejoin="round"/><path d="M15 44 V32 Q18 28 21 32 V44" fill={BK.coral} stroke={BK.ink} strokeWidth="1.4"/></svg>
      </div>
    </Part>
  </>);
  // 6 (faces "Middle C: Princess Clara")
  const visit = (label, clef, who) => <div style={{border:'1.2px solid #e2dccb',borderRadius:12,padding:'8px 12px 6px'}}>
    <div style={{display:'flex',alignItems:'center',gap:8,marginBottom:2}}><PenArt shapes={who === 'clara' ? sfClara(22, 24, 1) : who === 'queen' ? sfQueen(22, 24, 1) : sfKing(22, 24, 1)} vb={[0, 2, 44, 42]} style={{width:30,flex:'0 0 auto'}}/><span style={{fontSize:13,fontWeight:800,color:BK.ink}}>{label}</span></div>
    <PaperStaff clef={clef} notes={[]} width={150} minSpan={clef === 'treble' ? [27, 39] : [17, 29]}/>
  </div>;
  P(<>
    <WbTop step={5}/>
    <Part kind="together" title="Circle every middle C" how="Clara's note sits on its own little ladder rung -- just under the Queen's staff, or just over the King's. Same key!">
      <div style={{maxWidth:640,margin:'0 auto',width:'100%'}}><PaperStaff clef="grand" notes={W.s5.mid.map((n, i) => ({ ...n, x: sfXs(8, 440, true)[i] }))} width={440}/></div>
    </Part>
    <Part kind="home" title="Clara visits" how="Draw the note each time -- on its little ladder rung when it is Clara's C.">
      <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:12}}>
        {visit('Visiting the Queen: draw Clara’s C', 'treble', 'clara')}
        {visit('Visiting the King: draw Clara’s C', 'bass', 'clara')}
        {visit('One step up from Clara: draw D', 'treble', 'queen')}
        {visit('One step down from Clara: draw B', 'bass', 'king')}
      </div>
    </Part>
  </>);
  // 7 (puzzle page for step 5)
  P(<>
    <WbTop step={5}/>
    <Part kind="play" grow={false} title="The secret message" how="Write each note's letter in its box -- every staff spells a word. The last one is seven notes long!">
      <div style={{display:'grid',gridTemplateColumns:'1fr 1fr 1fr',gap:'4px 14px'}}>
        {SF_MSG.slice(0, 3).map((m, i) => { const xs = [64, 98, 132]; return <SfRow key={i} clef={m.clef} width={152} notes={m.notes.map((d, j) => ({ d, x: xs[j] }))} minSpan={m.clef === 'bass' ? [29, 17] : [27, 39]} items={xs.map((x, j) => ({ x, ex: i === 0, ans: m.word[j], box: true, w: 30 }))}/>; })}
      </div>
      {SF_MSG.slice(3).map(m => { const xs = sfXs(7, 440, true); return <div key={m.word} style={{maxWidth:620,margin:'10px auto 0',width:'100%'}}><SfRow clef="grand" width={440} notes={m.notes.map((d, j) => ({ d, x: xs[j] }))} items={xs.map(x => ({ x, w: 30 }))}/></div>; })}
    </Part>
    <Part kind="play" title="Note bingo" how="Someone names (or plays) one of the nine notes. Find it and colour it. Three in a row -- across, down or corner to corner -- wins!">
      <div style={{display:'grid',gridTemplateColumns:'repeat(3, 1fr)',gap:8,maxWidth:520,margin:'0 auto',width:'100%'}}>
        {W.s6.bingo.map((d, i) => <div key={i} style={{border:'1.6px solid ' + BK.ink,borderRadius:10,padding:'4px 10px'}}><PaperStaff clef={d >= 28 ? 'treble' : 'bass'} notes={[{ d }]} width={130} minSpan={d >= 28 ? [39, 27] : [29, 17]}/></div>)}
      </div>
    </Part>
  </>);
  // 8. the check-up on paper (Phase 406: it belongs in the Workbook)
  P(<>
    <WbTop step={6}/>
    <SfPaperCheck/>
  </>);
  return <>{frames ? lbFramed('staff', pages, startNo) : pages}</>;
}

// the check-up on paper, big staves (Phase 409)
function SfPaperCheck() {
  const C = useMemo(() => sfChkData(), [LANG]);
  const xs4n = sfXs(4, 480, false), xs4c = sfXs(4, 480, true);
  const pcs = [70, 180, 290, 400];
  return <div className="lb-paper" style={{display:'flex',flexDirection:'column',gap:4}}>
    <LbPaperHead/>
    {bkSec('A', 'Line or space? Write L or S.')}
    <SfRow width={480} notes={C.ls.map((it, i) => ({ d: it.d, x: xs4n[i] }))} minSpan={[29, 39]} items={xs4n.map((x, i) => ({ x, n: i + 1 }))}/>
    {bkSec('B', 'Step or skip? Up or down? Write it.')}
    <SfRow width={480} notes={C.ss.flatMap((it, i) => [{ d: it.a, x: pcs[i] - 16 }, { d: it.b, x: pcs[i] + 16 }])} minSpan={[29, 39]} items={pcs.map((x, i) => ({ x, n: i + 5, w: 88 }))}/>
    {bkSec('C', 'The Queen’s five: name the notes.')}
    <SfRow clef="treble" width={480} notes={C.tr.map((d, i) => ({ d, x: xs4c[i] }))} minSpan={[27, 39]} items={xs4c.map((x, i) => ({ x, n: i + 9 }))}/>
    {bkSec('D', 'The King’s five: name the notes.')}
    <SfRow clef="bass" width={480} notes={C.ba.map((d, i) => ({ d, x: xs4c[i] }))} minSpan={[17, 29]} items={xs4c.map((x, i) => ({ x, n: i + 13 }))}/>
    {bkSec('E', 'Circle every middle C.')}
    <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:14}}>{['treble', 'bass'].map(cl => <div key={cl}><PaperStaff clef={cl} notes={C.mc[cl].map((n, i) => ({ ...n, x: sfXs(3, 230, true)[i] }))} width={230} minSpan={cl === 'treble' ? [27, 39] : [17, 29]}/></div>)}</div>
  </div>;
}

// ─── the Teacher copy (Phase 405, pages re-laid in Phase 409): answers, what to watch for, what to say ───
function SfTeacher() {
  const W = useMemo(() => sfWorkbook(), [LANG]);
  const C = useMemo(() => sfChkData(), [LANG]);
  const pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="staff" teacher>{content}</WbPage>);
  const path = W.s4.path.map(([r, c]) => 'row ' + (r + 1) + ' col ' + (c + 1));
  const lsNum = (d) => sfLS(d) + (sfLS(d) === 'L' ? (d - 30) / 2 + 1 : (d - 29) / 2);
  const pos = (d) => (d - 30) % 2 === 0 ? 'line ' + ((d - 30) / 2 + 1) : 'space ' + ((d - 29) / 2);
  P(<>
    <div style={{fontFamily:"'Playfair Display', Georgia, serif",fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('staff')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 12px',lineHeight:1.5}}>Answers for every workbook page, the mistakes students make most, and a line to say when they get stuck. This chapter reads only the nine notes round middle C; the whole staff, the rhymes and fast reading from landmarks come in the next chapter.</div>
    <TcBlock page={2} title="Lines and spaces" answers={<>{tcAns('TRY IT', W.s1.tog.map(it => sfLS(it.d)))}{tcAns('YOUR TURN', W.s1.home.map(it => lsNum(it.d)))}{tcAns('PLATES', ['kebabs: three notes with a line through the middle', 'sandwiches: three notes filling a space'])}</>}
      watch="Counting from the top line down, and space notes drawn leaning on a line so they look like line notes."
      say="“Count like climbing a ladder -- from the floor up. Line 1 is the bottom one.”"/>
    <TcBlock page={3} title="Up the staff, up the piano" answers={<>{tcAns('TRY IT', W.s2.tog.map(sfSSName))}{tcAns('YOUR TURN', W.s2.home.map(sfSSName))}{tcAns('HIGHER', W.s2.hi.map(it => it.a > it.b ? '1st' : '2nd'))}{tcAns('STAIRS', W.s2.stair.moves.map(mv => pos(mv.d)))}</>}
      watch="Circling the note that comes later in time instead of the higher one, and calling every move “up”."
      say="“Higher on the page is higher on the piano -- which one would your right hand reach for?”"/>
    <TcBlock page={4} title="The Queen's five" answers={<>{tcAns('YOUR TURN', W.s3.home.map(it => withSolfa(dName(it.d))))}{tcAns('COMPOSE', ['any four of C D E F G -- check each drawn note against the letter under it; then they play it'])}</>}
      watch="Starting to count without looking at the clef first -- most children grab whatever they remember."
      say="“Crown check first: whose palace is this? The curl holds the Queen's G -- start from her line, or from Clara's C.”"/>
    <TcBlock page={5} title="The King's five" answers={<>{tcAns('YOUR TURN', W.s4.home.map(it => withSolfa(dName(it.d))))}{tcAns('MAZE', ['the F road: ' + path.join(' › ')])}</>}
      watch="Reading bass notes with treble names -- the answer comes out two letters too high."
      say="“Crown check: this is the King's staff. His two dots guard F -- find F first, then walk from there.”"/>
  </>);
  P(<>
    <TcBlock page={6} title="Middle C: Princess Clara" answers={<>{tcAns('CIRCLE', ['notes ' + W.s5.mid.map((n, j) => n.d === 28 ? j + 1 : null).filter(Boolean).join(', ')])}{tcAns('CLARA VISITS', ['C on the ladder rung just under the treble staff', 'C on the ladder rung just over the bass staff', 'D just under line 1 of the treble staff', 'B just over line 5 of the bass staff'])}</>}
      watch="Thinking the C under the treble staff and the C over the bass staff are two different keys."
      say="“One Clara, one key -- written from the Queen's side or the King's side.”"/>
    <TcBlock page={7} title="Puzzle page" answers={<>{tcAns('MESSAGE', SF_MSG.map(m => m.word))}{tcAns('BINGO CARD', W.s6.bingo.map(d => withSolfa(dName(d)) + (d === 28 ? ' (middle C)' : '')))}</>}
      watch="In bingo, F and G live in both palaces: the treble F/G are high, the bass F/G low. Call them by palace: “the Queen's G”, “the King's F”."
      say="“Which palace? Then which friend is nearest?”"/>
    <TcBlock page={8} title="Check-up" goBack={[{ id: 'ls', step: 1, page: 2 }, { id: 'ss', step: 2, page: 3 }, { id: 'tr', step: 3, page: 4 }, { id: 'ba', step: 4, page: 5 }, { id: 'mc', step: 5, page: 6 }]} answers={<>
      {tcAns('A', C.ls.map(it => sfLS(it.d)))}
      {tcAns('B', C.ss.map(it => sfSSName({ a: it.a, b: it.b })))}
      {tcAns('C', C.tr.map(d => withSolfa(dName(d))))}
      {tcAns('D', C.ba.map(d => withSolfa(dName(d))))}
      {tcAns('E', ['treble staff: note ' + (C.mc.treble.findIndex(n => n.d === 28) + 1) + ' · bass staff: note ' + (C.mc.bass.findIndex(n => n.d === 28) + 1)])}
    </>}
      watch="A wobbly B: step down from Clara's C. And F and G living in both palaces -- on the Queen's staff they are high, on the King's they are low."
      say="“Crown check, then count from the nearest friend: the Queen's G, Clara's C or the King's F.”"/>
    <div style={{fontSize:12.5,color:BK.ink,lineHeight:1.6,marginTop:6}}>
      <b style={{color:BK.muted,fontSize:10.5,letterSpacing:'0.06em'}}>LESSON TIME</b> The hand staff (page 2 of the book) is the one prop this chapter needs: five fingers are the five lines. Short lessons: set the drill levels as the week's practice -- random notes, a little every day, tracked on the student page.
    </div>
  </>);
  return <>{pages}</>;
}
