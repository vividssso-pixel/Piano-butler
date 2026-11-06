// ─── Phase 455: chapter 3's Workbook (B10) and Teacher copy. English, like every Workbook. Each page faces its Lesson
// Book page (2 to 6); the last page is the check-up on paper, facing 'My five checks'. Counting is 1 2 3 4 only (B5);
// a silent beat is a dashed circle with no rest name (B6); finger numbers sit in coral circles (B8). ───
// paper pieces: a beat circle ('beat' white, 'play' navy, 'silent' dashed, 'finger' coral, 'fingerOpen' a coral ring to
// write a finger in); label: a printed number, or (ans) a worked answer in coral handwriting
function plC(kind, label, o = {}) {
  const s = o.size || 30, fill = kind === 'play' ? BK.ink : kind === 'finger' ? BK.coral : '#fff';
  const stroke = kind === 'finger' || kind === 'fingerOpen' ? BK.coral : BK.ink;
  const tc = kind === 'play' || kind === 'finger' || o.ansFill ? '#fff' : o.ans ? BK.coral : kind === 'fingerOpen' ? BK.coral : BK.ink;   // ansFill: a worked colouring, navy like a played beat
  return <svg width={s} height={s} viewBox="0 0 30 30" style={{display:'block',flex:'0 0 auto'}}>
    <circle cx="15" cy="15" r="13" fill={o.ansFill ? BK.ink : fill} stroke={o.ansFill ? BK.ink : stroke} strokeWidth="1.8" strokeDasharray={kind === 'silent' && !o.ansFill ? '3.6 3' : undefined}/>
    {label != null && label !== '' && <text x="15" y="20.6" textAnchor="middle" fontSize="15.5" fontWeight="900" fontStyle={o.ans ? 'italic' : undefined} fill={tc} fontFamily="Inter,sans-serif">{label}</text>}
  </svg>;
}
// a row of circles in groups of four; under(i): what sits under circle i (a count, a box)
function PlRow({ n, circ, under, size = 30, gap = 6, group = 10 }) {
  return <div style={{display:'flex',alignItems:'flex-start',justifyContent:'center'}}>{Array.from({ length: n }, (_, i) => <div key={i} style={{display:'flex',flexDirection:'column',alignItems:'center',gap:3,marginLeft:i === 0 ? 0 : i % 4 === 0 ? group : gap}}>
    {circ(i)}{under && under(i)}</div>)}</div>;
}
const plCount = (txt, col = BK.ink) => <span style={{fontSize:13.5,fontWeight:900,color:col,lineHeight:1}}>{txt}</span>;
const plWBox = (ex, txt, w = 34, h = 30) => ex ? bkHand(txt, w, h) : bkBox(w, h);
// a trail of bare footprints walking right: gaps in the viewBox's units; a footprint for each place
function PlTrail({ gaps, w = 210, h, first = 12, more = 0, color = BK.ink, k = 1.7 }) {
  const xs = [first]; gaps.forEach(g => xs.push(xs[xs.length - 1] + g));
  const y1 = 5 + 4 * k, y2 = y1 + 9 * k + 4, H = h || y2 + 4 * k + 6;
  h = H;
  const foot = (x, i) => { const y = i % 2 ? y2 : y1, m = i % 2 ? 1 : -1;
    return <g key={i} fill={color} transform={'translate(' + x + ' ' + y + ') scale(' + k + ')'}><ellipse cx="0.6" cy="0" rx="3.4" ry="2.9"/><ellipse cx="-4.6" cy={0.5 * m} rx="2.4" ry="2"/>
      {[[4.9, -2.4, 1], [5.9, -0.7, 0.9], [5.8, 0.9, 0.78], [5, 2.4, 0.68]].map(([a, b, r], j) => <circle key={j} cx={a} cy={b * m} r={r}/>)}</g>; };
  return <svg viewBox={'0 0 ' + w + ' ' + h} style={{width:'100%',display:'block'}}>
    <line x1="4" x2={w - 4} y1={h - 3} y2={h - 3} stroke={BK.line} strokeWidth="1" strokeDasharray={more ? '3 3' : undefined}/>
    {xs.map(foot)}
  </svg>;
}
const plHeart = (s = 16, col = BK.coral) => <svg width={s} height={s * 0.86} viewBox="-8 -7 16 13.6" style={{display:'block'}}><path d="M0 5.6 Q-7.6 -0.4 -5.1 -4.3 Q-2.5 -7 0 -3 Q2.5 -7 5.1 -4.3 Q7.6 -0.4 0 5.6 Z" fill={col}/></svg>;
const PL_WN = { bird: ['bird', 1], turtle: ['tur-tle', 2], lighthouse: ['light-house', 2], sea: ['sea', 1], sky: ['sky', 1] };
// a row of four words over four beats; dots: draw the sound dots (ex: in coral); lines: a dotted line to draw on
function PlWordRow({ row, dots, w = 300, size = 15 }) {
  return <div style={{display:'grid',gridTemplateColumns:'repeat(4,1fr)',width:'100%',maxWidth:w,margin:'0 auto'}}>{row.map((x, i) => <div key={i} style={{display:'flex',flexDirection:'column',alignItems:'center',gap:3}}>
    <div style={{height:18,display:'flex',alignItems:'flex-end',gap:7}}>{dots ? Array.from({ length: PL_WN[x][1] }, (_, k) => <span key={k} style={{width:10,height:10,borderRadius:5,background:BK.coral}}/>) : <span style={{width:46,borderBottom:'1.2px dotted ' + BK.muted}}/>}</div>
    <span style={{fontSize:size,fontWeight:900,color:BK.ink,whiteSpace:'nowrap'}}>{PL_WN[x][0]}</span>
    {plHeart(15)}
  </div>)}</div>;
}
const plSounds = (row) => row.reduce((a, x) => a + PL_WN[x][1], 0);

// the Workbook's tasks, fixed so the Teacher copy always matches
const PL_WB = {
  // footprint trails (gaps): steady or not
  trails: [[30, 30, 30, 30, 30], [18, 40, 28, 40, 22], [34, 34, 18, 34, 34], [24, 24, 24, 24, 24]],
  trails2: [[34, 20, 34, 48, 34], [28, 28, 28, 28, 28], [36, 36, 36, 36, 36], [22, 22, 22, 42, 22]],
  keep: [24, 34, 44],   // three footprints at this gap: draw the next two
  // number the beats: the numbers printed in each row of eight (the rest to write)
  fill: [{}, { 0: 1, 4: 1 }, { 0: 1, 3: 4, 6: 3 }, { 1: 2, 5: 2 }],
  next: [3, 2, 4, 1],   // six circles from this number: the first two printed
  snake: { 0: 1, 6: 3, 13: 2, 19: 4 },
  // silent beats: the beats you play in each group of four
  silent: [[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 1]],
  colour: [[1, 3], [4], [1, 2, 4], [2, 3]],
  fix: [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 0], [1, 1, 1, 0]],   // counted wrongly: only the played notes got a number
  // words over the beat
  dots: [['turtle', 'bird', 'bird', 'turtle'], ['bird', 'lighthouse', 'bird', 'bird'], ['turtle', 'turtle', 'lighthouse', 'bird'], ['lighthouse', 'turtle', 'bird', 'turtle']],
  count: [['bird', 'bird', 'bird', 'turtle'], ['turtle', 'turtle', 'turtle', 'turtle'], ['lighthouse', 'bird', 'turtle', 'bird'], ['bird', 'bird', 'bird', 'bird']],
  // fingers on the beat
  which: [[[2, 3, 2, 3], 3], [[2, 3, 4, 3], 2], [[3, 2, 3, 2], 4], [[2, 3, 4, 3], 3]],
  go: [[2, 3, 2, 3], [2, 3, 4, 3], [3, 2, 3, 2], [4, 3, 2, 3]],
  wordsFromDots: [[1, 2, 2, 1], [2, 1, 2, 2], [1, 1, 1, 2]],   // one dot: bird; two dots: tur-tle
  keys: [{ 2: [1, 3], 3: [2], 4: [4] }, { 2: [1], 3: [2, 4], 4: [3] }, { 2: [2, 4], 3: [3], 4: [1] }],   // the beats each finger's key plays
};
const PL_CHK = {
  trails: [[32, 32, 32, 14, 32], [26, 26, 26, 26, 26], [18, 30, 40, 22, 34], [20, 20, 34, 20, 20]],
  fill: [{ 0: 1, 5: 2 }, { 2: 3, 4: 1 }, { 1: 2, 7: 4 }, { 3: 4, 6: 3 }],
  play: [[1, 0, 1, 0], [1, 1, 1, 0], [0, 0, 1, 1], [1, 0, 0, 1]],
  sounds: [['turtle', 'bird', 'bird', 'bird'], ['lighthouse', 'bird', 'bird', 'turtle'], ['bird', 'turtle', 'bird', 'bird'], ['turtle', 'bird', 'turtle', 'turtle']],
  which: [[[2, 3, 4, 3], 3], [[3, 2, 3, 2], 2], [[2, 3, 2, 3], 4], [[4, 3, 2, 3], 1]],
};
const plSteady = (g) => g.every(x => x === g[0]);
const plFingerRow = (fs, size = 28, ans) => <PlRow n={4} gap={8} circ={(i) => plC('finger', fs[i], { size })} under={(i) => plCount(String(i + 1), BK.muted)}/>;

function PlWorkbook({ startNo = 1 }) {
  const W = PL_WB, pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + 1 + pages.length} chId="pulse">{content}</WbPage>);
  const trailCell = (g, i, n0, ex) => <ExCell key={i} n={n0 + i} ex={ex}><div style={{display:'grid',gridTemplateColumns:'1fr auto',alignItems:'center',gap:10,padding:'14px 8px 4px'}}><PlTrail gaps={g}/><TickCross ok={plSteady(g)} ex={ex}/></div></ExCell>;

  // 2 (faces "A steady beat")
  P(<>
    <WbTop step={1}/>
    <Part kind="together" title="Steady or not?" how="Look at the gaps between the footprints. Tick a trail with the same gap every time; cross a trail whose gaps change.">
      <BkGrid cols={2} gap="8px 12px">{W.trails.map((g, i) => trailCell(g, i, 1, i === 0))}</BkGrid>
    </Part>
    <Part kind="home" title="Steady or not, on your own" how="Tick or cross. Look carefully: one gap that changes makes a trail not steady.">
      <BkGrid cols={2} gap="8px 12px">{W.trails2.map((g, i) => trailCell(g, i, 5, false))}</BkGrid>
    </Part>
    <Part kind="play" title="Keep the trail going" how="Draw the next two footprints on each trail, the same gap every time. Then walk it across the room: one step on each beat, counting 1 2 3 4.">
      <div style={{display:'grid',gap:22}}>{W.keep.map((g, i) => <div key={i} style={{display:'grid',gridTemplateColumns:'24px 1fr',alignItems:'center',gap:8}}><span style={{fontFamily:LB_SERIF,fontStyle:'italic',fontWeight:700,fontSize:14,color:BK.ink}}>{9 + i}</span><PlTrail gaps={[g, g]} w={300} more={1} k={1.7}/></div>)}</div>
    </Part>
    <Faces/>
  </>);

  // 3 (faces "Count out loud")
  P(<>
    <WbTop step={2}/>
    <Part kind="together" title="Number the beats" how="Write the count in every empty circle: 1 2 3 4, then start again at 1.">
      <div style={{display:'grid',gap:8}}>{W.fill.map((m, i) => <ExCell key={i} n={i + 1} ex={i === 0}><div style={{padding:'16px 6px 4px'}}>
        <PlRow n={8} circ={(j) => i === 0 ? plC('beat', String(j % 4 + 1), { ans: j !== 0 && j !== 4, size: 38 }) : plC('beat', m[j] != null ? String(m[j]) : '', { size: 38 })}/></div></ExCell>)}</div>
    </Part>
    <Part kind="home" title="What comes next?" how="The count goes round: after 4 comes 1. Write the next four numbers.">
      <BkGrid cols={2} gap="8px 12px">{W.next.map((s, i) => <ExCell key={i} n={i + 5}><div style={{padding:'16px 4px 4px'}}><PlRow n={6} gap={5} group={5} circ={(j) => plC('beat', j < 2 ? String((s - 1 + j) % 4 + 1) : '', { size: 37 })}/></div></ExCell>)}</BkGrid>
    </Part>
    <Part kind="play" title="The counting snake" how="Fill in the whole snake, from its head to its tail. Then pat your knees and count it out loud, one number on each pat.">
      <PlSnake given={W.snake}/>
    </Part>
    <Faces/>
  </>);

  // 4 (faces "When the notes stop")
  P(<>
    <WbTop step={3}/>
    <Part kind="together" title="Count every beat" how="Write the count under every circle: the navy ones you play and the dashed silent ones too.">
      <BkGrid cols={2} gap="8px 12px">{W.silent.map((m, i) => <ExCell key={i} n={i + 1} ex={i === 0}><div style={{padding:'16px 2px 4px'}}>
        <PlRow n={8} gap={3} group={9} circ={(j) => plC(m[j % 4] ? 'play' : 'silent', '', { size: 33 })} under={(j) => plWBox(i === 0, String(j % 4 + 1), 33, 30)}/></div></ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Colour the beats you play" how="Colour the circles you play. Leave the silent beats white and dashed.">
      <BkGrid cols={2} gap="8px 12px">{W.colour.map((pl, i) => <ExCell key={i} n={i + 5} ex={i === 0}><div style={{display:'grid',gap:6,justifyItems:'center',padding:'16px 4px 4px'}}>
        <span style={{fontSize:13.5,fontWeight:900,color:BK.ink}}>{pl.length === 1 ? 'Play only on ' + pl[0] : 'Play on ' + pl.slice(0, -1).join(', ') + ' and ' + pl[pl.length - 1]}</span>
        <PlRow n={4} gap={10} circ={(j) => plC('silent', String(j + 1), { size: 36, ansFill: i === 0 && pl.includes(j + 1) })}/></div></ExCell>)}</BkGrid>
    </Part>
    <Part kind="play" title="Fix the count" how="Only the played notes got a number here. Write the right count under every circle, then play each row: right hand, finger 3, the 4th small house.">
      <div style={{display:'grid',gap:12}}>{W.fix.map((m, r) => { let k = 0; const lab = Array.from({ length: 8 }, (_, j) => m[j % 4] ? String(++k > 4 ? k - 4 : k) : '');
        return <div key={r} style={{display:'grid',gridTemplateColumns:'24px 1fr',alignItems:'center',gap:6}}><span style={{fontFamily:LB_SERIF,fontStyle:'italic',fontWeight:700,fontSize:14,color:BK.ink}}>{9 + r}</span>
          <PlRow n={8} gap={8} group={18} circ={(j) => plC(m[j % 4] ? 'play' : 'silent', lab[j], { size: 32 })} under={() => bkBox(34, 28)}/></div>; })}</div>
    </Part>
    <Faces/>
  </>);

  // 5 (faces "Beat or rhythm?")
  P(<>
    <WbTop step={4}/>
    <Part kind="together" title="One dot for each sound" how="Say each row, one word on each heart. Draw one dot over a word for each sound.">
      <BkGrid cols={2} gap="8px 12px">{W.dots.map((row, i) => <ExCell key={i} n={i + 1} ex={i === 0}><div style={{padding:'16px 4px 4px'}}><PlWordRow row={row} dots={i === 0}/></div></ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Beats and sounds" how="How many beats? How many sounds? Draw the dots, then write both numbers.">
      <BkGrid cols={2} gap="8px 12px">{W.count.map((row, i) => <ExCell key={i} n={i + 5}><div style={{display:'grid',gap:6,padding:'16px 4px 4px'}}>
        <PlWordRow row={row} dots={false}/>
        <div style={{display:'flex',justifyContent:'center',alignItems:'center',gap:8,fontSize:12.5,fontWeight:800,color:BK.ink}}>beats {bkBox(40, 32)} <span style={{width:8}}/>sounds {bkBox(40, 32)}</div></div></ExCell>)}</BkGrid>
    </Part>
    <Part kind="play" title="Words from dots" how="One dot: write bird. Two dots: write tur-tle. Then say each row, tapping the beat with your foot.">
      <div style={{display:'grid',gap:22}}>{W.wordsFromDots.map((row, r) => <div key={r} style={{display:'grid',gridTemplateColumns:'24px 1fr',alignItems:'center',gap:6}}><span style={{fontFamily:LB_SERIF,fontStyle:'italic',fontWeight:700,fontSize:14,color:BK.ink}}>{9 + r}</span>
        <div style={{display:'grid',gridTemplateColumns:'repeat(4,1fr)',maxWidth:540,width:'100%',margin:'0 auto'}}>{row.map((d, k) => <div key={k} style={{display:'flex',flexDirection:'column',alignItems:'center',gap:6}}>
          <div style={{display:'flex',gap:8,height:12}}>{Array.from({ length: d }, (_, q) => <span key={q} style={{width:12,height:12,borderRadius:6,background:BK.coral}}/>)}</div>
          <span style={{width:100,borderBottom:'1.4px solid ' + BK.ink,height:26}}/>{plHeart(17)}</div>)}</div></div>)}</div>
    </Part>
    <Faces/>
  </>);

  // 6 (faces "The pulse in your fingers")
  P(<>
    <WbTop step={5}/>
    <Part kind="together" title="Which finger on the beat?" how="Which finger plays on the beat asked for? Write its number in the box.">
      <BkGrid cols={2} gap="8px 12px">{W.which.map(([fs, b], i) => <ExCell key={i} n={i + 1} ex={i === 0}><div style={{display:'grid',gridTemplateColumns:'1fr auto',alignItems:'center',gap:10,padding:'16px 8px 4px'}}>
        {plFingerRow(fs, 28, i === 0 ? b : null)}
        <span style={{display:'inline-flex',alignItems:'center',gap:6,fontSize:12.5,fontWeight:800,color:BK.ink}}>on {b}: {plWBox(i === 0, String(fs[b - 1]), 40, 34)}</span></div></ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Keep the pattern going" how="Write the finger numbers for the next four beats: the same pattern again. Then play each row, counting out loud.">
      <div style={{display:'grid',gap:7}}>{W.go.map((fs, i) => <ExCell key={i} n={i + 5}><div style={{padding:'13px 6px 2px'}}>
        <PlRow n={8} gap={7} circ={(j) => j < 4 ? plC('finger', fs[j], { size: 34 }) : plC('fingerOpen', '', { size: 34 })} under={(j) => plCount(String(j % 4 + 1), BK.muted)}/></div></ExCell>)}</div>
    </Part>
    <Part kind="play" title="Read the keys" how="Over each key: the beats it plays on. Write the finger for each beat, then play it: right hand, the big house next to the 4th small house.">
      <BkGrid cols={3} gap="8px 12px">{W.keys.map((m, i) => <div key={i} style={{display:'grid',justifyItems:'center',gap:6}}>
        <span style={{fontFamily:LB_SERIF,fontStyle:'italic',fontWeight:700,fontSize:14,color:BK.ink,justifySelf:'start'}}>{9 + i}</span>
        <PlKeys3 beats={m}/>
        <PlRow n={4} gap={6} circ={() => plC('fingerOpen', '', { size: 34 })} under={(j) => plCount(String(j + 1), BK.muted)}/></div>)}</BkGrid>
    </Part>
    <Faces/>
  </>);

  // 7. the check-up on paper (the Workbook's last page)
  P(<PlPaperCheck/>);
  return <>{pages}</>;
}
function PlKeys3({ beats }) {
  const X = [18, 54, 90];
  return <svg viewBox="0 0 132 104" style={{width:136,display:'block'}}>
    {[2, 3, 4].map((f, i) => <text key={'b' + f} x={X[i] + 12} y="15" textAnchor="middle" fontSize="15" fontWeight="900" fill={BK.ink}>{(beats[f] || []).join(', ')}</text>)}
    <rect x="2" y="24" width="128" height="78" fill="#fff" stroke={BK.ink} strokeWidth="1.6"/>
    {[1, 2, 3].map(i => <line key={i} x1={2 + i * 32} x2={2 + i * 32} y1="74" y2="102" stroke={BK.ink} strokeWidth="1"/>)}
    {[2, 3, 4].map((f, i) => <g key={f}><rect x={X[i]} y="24" width="24" height="50" fill={BK.ink}/><circle cx={X[i] + 12} cy="60" r="9.5" fill={BK.coral}/><text x={X[i] + 12} y="64.6" textAnchor="middle" fontSize="12.5" fontWeight="900" fill="#fff">{f}</text></g>)}
  </svg>;
}
// the counting snake: twenty-four circles, eight along, eight back, eight along again; a head and a tail
function PlSnake({ given = {}, answers }) {
  const r = 17, dx = 50, x0 = 76, W = x0 * 2 + dx * 7 + 30, ys = [34, 100, 166], H = 198;
  const at = (i) => { const row = Math.floor(i / 8), k = i % 8; return [x0 + (row % 2 ? 7 - k : k) * dx, ys[row]]; };
  const xe = x0 + 7 * dx, band = `M${x0 - 10} ${ys[0]} L${xe} ${ys[0]} Q${xe + 50} ${(ys[0] + ys[1]) / 2} ${xe} ${ys[1]} L${x0} ${ys[1]} Q${x0 - 50} ${(ys[1] + ys[2]) / 2} ${x0} ${ys[2]} L${xe + 6} ${ys[2]}`;
  return <svg viewBox={'0 0 ' + W + ' ' + H} style={{width:'100%',maxWidth:580,display:'block',margin:'0 auto'}}>
    {[[BK.ink, 30], ['#fff', 27]].map(([c, w]) => <path key={c} d={band} fill="none" stroke={c} strokeWidth={w} strokeLinejoin="round"/>)}
    <path d={`M${xe + 6} ${ys[2] - 15} L${xe + 36} ${ys[2] + 2} L${xe + 6} ${ys[2] + 15}`} fill="#fff" stroke={BK.ink} strokeWidth="1.5" strokeLinejoin="round"/>
    <ellipse cx={x0 - 38} cy={ys[0]} rx="21" ry="16" fill="#fff" stroke={BK.ink} strokeWidth="1.5"/><circle cx={x0 - 46} cy={ys[0] - 5} r="2.6" fill={BK.ink}/>
    <path d={`M${x0 - 58} ${ys[0] + 3} l-8 0 m8 0 l-6 -4 m6 4 l-6 4`} fill="none" stroke={BK.coral} strokeWidth="1.8" strokeLinecap="round"/>
    {Array.from({ length: 24 }, (_, i) => { const [x, y] = at(i), g = given[i], a = answers && g == null;
      return <g key={i}><circle cx={x} cy={y} r={r} fill="#fff" stroke={BK.ink} strokeWidth="1.8"/>
        {(g != null || a) && <text x={x} y={y + 6.5} textAnchor="middle" fontSize="18" fontWeight="900" fontStyle={a ? 'italic' : undefined} fill={a ? BK.coral : BK.ink}>{g != null ? g : i % 4 + 1}</text>}</g>; })}
  </svg>;
}
function PlPaperCheck() {
  const C = PL_CHK;
  return <div className="lb-paper" style={{display:'flex',flexDirection:'column',gap:4}}>
    <LbPaperHead/>
    {bkSec('A', 'Steady or not? Tick a steady trail; cross a trail whose gaps change.')}
    <BkGrid cols={2} gap="6px 10px">{C.trails.map((g, i) => <BkCell key={i} n={i + 1}><div style={{display:'grid',gridTemplateColumns:'1fr auto',alignItems:'center',gap:10,padding:'12px 6px 2px'}}><PlTrail gaps={g}/><TickCross ok={plSteady(g)}/></div></BkCell>)}</BkGrid>
    {bkSec('B', 'Write the count in every empty circle: 1 2 3 4, then 1 again.')}
    <BkGrid cols={2} gap="6px 10px">{C.fill.map((m, i) => <BkCell key={i} n={i + 5}><div style={{padding:'14px 2px 2px'}}><PlRow n={8} gap={3} group={8} circ={(j) => plC('beat', m[j] != null ? String(m[j]) : '', { size: 33 })}/></div></BkCell>)}</BkGrid>
    {bkSec('C', 'Which beats do you play? Write their numbers.')}
    <BkGrid cols={2} gap="6px 10px">{C.play.map((m, i) => <BkCell key={i} n={i + 9}><div style={{display:'grid',gridTemplateColumns:'1fr auto',alignItems:'center',gap:10,padding:'12px 8px 2px'}}><PlRow n={4} gap={8} circ={(j) => plC(m[j] ? 'play' : 'silent', '', { size: 32 })} under={(j) => plCount(String(j + 1), BK.muted)}/>{bkBox(84, 36)}</div></BkCell>)}</BkGrid>
    {bkSec('D', 'Four beats: how many sounds? Write the number.')}
    <BkGrid cols={2} gap="6px 10px">{C.sounds.map((row, i) => <BkCell key={i} n={i + 13}><div style={{display:'grid',gridTemplateColumns:'1fr auto',alignItems:'center',gap:8,padding:'12px 6px 2px'}}><PlWordRow row={row} dots={false} w={280} size={14}/>{bkBox(40, 36)}</div></BkCell>)}</BkGrid>
    {bkSec('E', 'Which finger plays on the beat asked for?')}
    <BkGrid cols={2} gap="6px 10px">{C.which.map(([fs, b], i) => <BkCell key={i} n={i + 17}><div style={{display:'grid',gridTemplateColumns:'1fr auto',alignItems:'center',gap:10,padding:'12px 8px 2px'}}>{plFingerRow(fs, 30)}<span style={{display:'inline-flex',alignItems:'center',gap:6,fontSize:12.5,fontWeight:800,color:BK.ink}}>on {b}: {bkBox(40, 36)}</span></div></BkCell>)}</BkGrid>
  </div>;
}

function PlTeacher() {
  const W = PL_WB, C = PL_CHK, pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="pulse" teacher>{content}</WbPage>);
  const st = (g) => plSteady(g) ? 'steady ✓' : 'not steady ✗';
  const plays = (m) => m.map((x, j) => x ? j + 1 : null).filter(Boolean).join(' ');
  const playName = (pl) => pl.length === 1 ? 'only ' + pl[0] : pl.join(' ');
  P(<>
    <div style={{fontFamily:"'Playfair Display', Georgia, serif",fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('pulse')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 8px',lineHeight:1.5}}>Each workbook page faces its Lesson Book page. The book uses <b>pulse</b> in the title and the opener and <b>beat</b> everywhere else (Korean: 박). It counts <b>1 2 3 4</b> only. Later: strong and weak beats (chapter {bkChapterNo('time-signatures')}, Time signatures); note values, rest names and + for “and” (chapter {bkChapterNo('note-values')}: 1 + 2 + 3 + 4 +, then 1 e + a 2 e + a); speed (chapter {bkChapterNo('tempo')}, Tempo). A silent beat is a dashed circle with no rest name yet. AMEB: practical, the groundwork for 2/4 and 3/4 at Preliminary.</div>
    <div style={{fontSize:12.5,color:BK.ink,margin:'0 0 12px',lineHeight:1.5,border:'0.8px solid ' + BK.hair,padding:'7px 10px'}}><b style={{color:BK.coral}}>Lesson time: walk, then run.</b> Walk round the room to a steady beat: one step on each beat. Later, running (two quick steps on each beat) becomes two quavers, counted 1 + 2 + in chapter {bkChapterNo('note-values')}. In this chapter, keep to walking.</div>
    <TcBlock page={2} title="A steady beat" answers={<>{tcAns('TRY IT', W.trails.map(st))}{tcAns('YOUR TURN', W.trails2.map(st), 5)}{tcAns('PLAY', ['9 to 11: two more footprints on each trail, the same gap as the first three'], null)}</>}
      watch="Judging a trail by its length instead of its gaps. Missing a single gap that changes (3 and 8). When the student pats or walks: speeding up as the beat goes on, slowing down, or stopping to think: the count must stay steady."
      say="“Look between the feet: is every gap the same?”"/>
    <TcBlock page={3} title="Count out loud" answers={<>{tcAns('TRY IT', ['1 to 4: 1 2 3 4 1 2 3 4 in every row'], null)}{tcAns('YOUR TURN', W.next.map(s => Array.from({ length: 6 }, (_, j) => (s - 1 + j) % 4 + 1).join(' ')), 5)}{tcAns('PLAY', ['1 2 3 4 six times round, from the head to the tail'], 9)}</>}
      watch="Counting on past 4 (“5, 6”). Playing or patting the first beat and only then starting the count, so the count lands late and every number is behind its beat: the number and the beat start together. Letting the count speed up or slow down: it should be as steady as the beat."
      say="“Say 1 at the same moment as you pat: number and pat together.”"/>
    <TcBlock page={4} title="When the notes stop" answers={<>{tcAns('TRY IT', ['1 to 4: 1 2 3 4 1 2 3 4 under every row, the silent circles too'], null)}{tcAns('YOUR TURN', W.colour.map(playName), 5)}{tcAns('PLAY', ['9 to 12: 1 2 3 4 1 2 3 4 under every row (the numbers in the circles counted only the notes)'], null)}</>}
      watch="Writing numbers only under the played circles. At the piano: stopping the count when the hand lifts, or rushing through the silent beats to the next note, so the next 1 comes early. Numbers 4 and 11 begin with a silent beat: the count still starts on 1."
      say="“Your hand stops; your count doesn't.”"/>
  </>);
  P(<>
    <TcBlock page={5} title="Beat or rhythm?" answers={<>{tcAns('TRY IT', W.dots.map(r => r.map(x => PL_WN[x][1]).join(' ') + ' dots'))}{tcAns('YOUR TURN', W.count.map(r => '4 beats, ' + plSounds(r) + ' sounds'), 5)}{tcAns('PLAY', W.wordsFromDots.map(r => r.map(d => d === 1 ? 'bird' : 'tur-tle').join(' ')), 9)}</>}
      watch="Tapping the foot on every sound of the words instead of the beat (the commonest mix-up). Giving a two-sound word two beats. Number 8: bird bird bird bird has 4 beats and 4 sounds: here the rhythm and the beat are the same."
      say="“The foot is the heartbeat: it never changes. The hands say the words.”"/>
    <TcBlock page={6} title="The beat in your fingers" answers={<>{tcAns('TRY IT', W.which.map(([fs, b]) => 'on ' + b + ': finger ' + fs[b - 1]))}{tcAns('YOUR TURN', W.go.map(fs => [...fs, ...fs].join(' ')), 5)}{tcAns('PLAY', W.keys.map(m => [1, 2, 3, 4].map(b => [2, 3, 4].find(f => (m[f] || []).includes(b))).join(' ')), 9)}</>}
      watch="Reading the finger numbers as the count, or the count as finger numbers: the coral circles are fingers, the numbers under them are the count. Pausing to find the next finger, so the beat stops: put every finger on its key before the count starts. Playing the first note and then starting the count late."
      say="“Coral is the finger, the number under it is the count. Keep the count going even while you look.”"/>
    <TcBlock page={7} title="The check-up on paper (the Workbook's last page)" answers={<>
      {tcAns('A', C.trails.map(st))}
      {tcAns('B', ['5 to 8: 1 2 3 4 1 2 3 4 in every row'], null)}
      {tcAns('C', C.play.map(plays), 9)}
      {tcAns('D', C.sounds.map(plSounds), 13)}
      {tcAns('E', C.which.map(([fs, b]) => 'finger ' + fs[b - 1]), 17)}
      <div style={{fontSize:12,color:BK.ink,marginTop:6,lineHeight:1.5}}>Four marks for each section. The paper shows the idea; the beat itself is heard: also listen to the student pat and count (My five checks, Lesson Book page 7).</div>
    </>}
      goBack={[{ id: 'a', step: 1, page: 2 }, { id: 'b', step: 2, page: 3 }, { id: 'c', step: 3, page: 4 }, { id: 'd', step: 4, page: 5 }, { id: 'e', step: 5, page: 6 }]}/>
  </>);
  return <>{pages}</>;
}
WORKBOOKS.pulse = PlWorkbook;
TEACHER_COPIES.pulse = PlTeacher;
