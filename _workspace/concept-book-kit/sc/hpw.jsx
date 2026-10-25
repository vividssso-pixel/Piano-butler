
// ─── Chapter 5's Workbook and teacher's copy (Build Y; the decision board's build queue, item 2) ───
// Each Workbook page faces its Lesson Book page (2 to 7); the last one, facing My five checks, is the check-up on paper.
// Fixed items, so the teacher's copy always matches the page.
const HP_WB = {
  c: [['R', 3], ['L', 2], ['R', 5], ['L', 4], ['R', 1], ['L', 5]],   // C position: which finger plays the coral key (hand, finger)
  g: [['R', 2], ['L', 3], ['R', 4], ['L', 1], ['R', 5], ['L', 2]],   // G position
  where: [['C', 'R'], ['G', 'L'], ['G', 'R'], ['C', 'L']],           // which position, which hand (five dots)
  mirror: [['C', 'R', 3], ['C', 'L', 2], ['G', 'R', 4], ['C', 'R', 5], ['G', 'L', 1], ['C', 'L', 4]],   // this hand plays finger f; the other hand's f plays?
  echo: [['1 2 3 -', '5 4 3 -'], ['3 4 5 -', '3 2 1 -'], ['5 4 3 -', '1 2 3 -'], ['1 3 5 -', '5 3 1 -']],   // right hand call; left hand answer, the same letters
  fill: [['Up and down the street (bars 1-2)', ['1', '2', '?3', '4', '|', '5', '-', '-', '-']], ['Up and down the street (bars 3-4)', ['5', '?4', '3', '2', '|', '1', '-', '-', '-']],
    ['Over to G (the first two bars)', ['1', '?3', '5', '-', '|', '5', '3', '?1', '-']],
    ['Mirror twins (both hands)', ['1', '2', '?3', '2', '|', '?1', '-', '-', '-']]],
  chk: { c: [['L', 3], ['R', 4], ['L', 1], ['R', 2]], g: [['R', 3], ['L', 5], ['R', 1], ['L', 4]], where: [['G', 'R'], ['C', 'L'], ['C', 'R'], ['G', 'L']],
    mirror: [['C', 'L', 3], ['G', 'R', 2], ['C', 'R', 4], ['G', 'L', 5]], fill: [['1', '2', '?3', '4', '5'], ['5', '?4', '3', '2', '1'], ['2', '3', '?4', '5'], ['4', '3', '?2', '1']] },   // steps only: one right answer each
};
const hpwHand = (h) => (h === 'R' ? 'Right hand' : 'Left hand');
const hpwOther = (h) => (h === 'R' ? 'L' : 'R');
const hpwMirror = ([pos, h, f]) => hpLet(hpFingerD(pos, hpwOther(h), f));
// one hand in a position with one key coral, for 'which finger?'
const hpwKeys = (pos, h, d, o = {}) => <HpKeys pos={pos} hands={h} fingers={false} letters={false} names={false} mc={false} lit={d != null ? { [d]: 'cor' } : {}} W={o.W || 16} k={o.k || 1.15} {...o}/>;
function HpwFingerCell({ pos, h, f, n, ex }) {
  return <ExCell n={n} ex={ex}><div style={{display:'flex',alignItems:'center',gap:8,padding:'16px 2px 2px'}}>
    <div style={{flex:1,minWidth:0}}><div style={{fontSize:10.5,fontWeight:900,color:BK.muted,textAlign:'center',marginBottom:2}}>{hpwHand(h)}</div>{hpwKeys(pos, h, hpFingerD(pos, h, f))}</div>
    {nvBox(ex, String(f), 38, 32)}</div></ExCell>;
}
// five dots on a long keyboard: which position, which hand?
function HpwWhereCell({ pos, h, n, ex }) {
  const lit = {}; hpKeysOf(pos, h).forEach(d => { lit[d] = 'cor'; });
  return <ExCell n={n} ex={ex}><div style={{display:'flex',alignItems:'center',gap:10,padding:'16px 2px 2px'}}>
    <div style={{flex:1,minWidth:0}}><HpKeys pos={pos} hands={h} span={[17, 37]} fingers={false} letters={false} names={false} mc pale={false} lit={lit} W={10} k={1.3}/></div>
    <div style={{display:'grid',gap:6,fontSize:11,fontWeight:900,color:BK.muted}}><span style={{display:'inline-flex',alignItems:'center',gap:5}}>C or G {nvBox(ex, pos, 32, 28)}</span><span style={{display:'inline-flex',alignItems:'center',gap:5}}>R or L {nvBox(ex, h, 32, 28)}</span></div>
  </div></ExCell>;
}
// mirror twins: this hand plays finger f (coral); which key does the other hand's finger f play?
function HpwMirrorCell({ item, n, ex }) {
  const [pos, h, f] = item, other = hpwOther(h);
  return <ExCell n={n} ex={ex}><div style={{display:'flex',alignItems:'center',gap:8,padding:'16px 2px 2px'}}>
    <div style={{flex:1,minWidth:0,display:'grid',gap:2}}>
      <div style={{fontSize:10.5,fontWeight:900,color:BK.muted}}>{hpwHand(h)}, {pos} position: finger {f}</div>
      <HpKeys pos={pos} hands="LR" fingers={false} letters={false} names={false} mc={false} lit={{ [hpFingerD(pos, h, f)]: 'cor' }} W={9} k={1}/>
      <div style={{fontSize:10.5,fontWeight:900,color:BK.ink}}>{hpwHand(other)}'s finger {f}: which letter?</div>
    </div>
    {nvBox(ex, hpwMirror(item), 38, 32)}</div></ExCell>;
}
const hpwCircles = (s, ex, size = 30) => <PhCircles seq={s.split(' ')} ex={ex} size={size}/>;

function HpWorkbook({ startNo = 1 }) {
  const W = HP_WB, pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + 1 + pages.length} chId="hand-positions">{content}</WbPage>);
  const area = (l, h = 150) => <div style={{border:'1.5px solid ' + BK.line,borderRadius:10,minHeight:h,flex:1,display:'flex',alignItems:'flex-end',padding:'6px 10px',fontSize:11.5,color:BK.muted}}>{l}</div>;

  // 2 (faces "C position")
  P(<>
    <WbTop step={1}/>
    <Part kind="together" title="Which finger?" how="Each hand is in C position. Write the number of the finger that plays the coral key. Thumbs are 1 on both hands.">
      <BkGrid cols={3} gap="6px 10px">{W.c.map(([h, f], i) => <HpwFingerCell key={i} pos="C" h={h} f={f} n={i + 1} ex={i === 0}/>)}</BkGrid>
    </Part>
    <Part kind="home" title="C position this week" how="Do each one at the piano and tick a box each day.">
      <PhLog rows={['Right hand: C D E F G and back, saying 1 2 3 4 5 4 3 2 1', 'Left hand: C D E F G and back, saying 5 4 3 2 1 2 3 4 5', 'Hands on knees, then back to C position in one go (5 times)']} label={300}/>
    </Part>
    <Part kind="play" title="Colour C position" how="Colour the right hand's five keys one colour and the left hand's five keys another. Write the finger numbers on the keys. Middle C is marked for you.">
      <div style={{padding:'4px 20px'}}><HpKeys pos="C" fingers={false} letters={false} names={false} pale={false} W={30} k={2.4}/></div>
    </Part>
    <Faces/>
  </>);

  // 3 (faces "G position")
  P(<>
    <WbTop step={2}/>
    <Part kind="together" title="Which finger? G position" how="The same shape on G. Write the number of the finger that plays the coral key.">
      <BkGrid cols={3} gap="6px 10px">{W.g.map(([h, f], i) => <HpwFingerCell key={i} pos="G" h={h} f={f} n={i + 1} ex={i === 0}/>)}</BkGrid>
    </Part>
    <Part kind="home" title="Where is C in G position?" how="Find C in G position. Write the finger that plays it, then check at the piano.">
      <div style={{display:'flex',gap:30,justifyContent:'center',fontSize:13.5,fontWeight:800,color:BK.ink,padding:'6px 0'}}>{['Right hand', 'Left hand'].map((l, i) => <span key={l} style={{display:'inline-flex',alignItems:'center',gap:8}}>{nvNum(7 + i)} {l}: finger {bkBox(40, 32)}</span>)}</div>
    </Part>
    <Part kind="play" title="The letter ladder" how="Write the missing letters of G position. Then say them up and down, without the piano: G A B C D, D C B A G.">
      <div style={{display:'flex',gap:10,justifyContent:'center',padding:'10px 0'}}>{['G', '', 'B', '', 'D'].map((l, i) => <span key={i} style={{width:52,height:52,border:'2px solid ' + (l ? BK.ink : BK.coral),borderRadius:8,display:'inline-flex',alignItems:'center',justifyContent:'center',fontFamily:LB_SERIF,fontSize:26,fontWeight:800,color:BK.ink}}>{l}</span>)}</div>
    </Part>
    <Faces/>
  </>);

  // 4 (faces "Move between them")
  P(<>
    <WbTop step={3}/>
    <Part kind="together" title="Which position? Which hand?" how="Five keys are coloured. Write C or G for the position, and R or L for the hand.">
      <BkGrid cols={2} gap="6px 10px">{W.where.map(([pos, h], i) => <HpwWhereCell key={i} pos={pos} h={h} n={i + 1} ex={i === 0}/>)}</BkGrid>
    </Part>
    <Part kind="home" title="Lift, travel, land" how="Do each one at the piano and tick a box each day. The arm carries the hand; the shape stays round.">
      <PhLog rows={['Right hand: C D E F G, lift, travel, land, G A B C D', 'And back again, from G to C', 'On a steady beat: one silent beat to move', 'The left hand the same']} label={300}/>
    </Part>
    <Part kind="play" title="The bridge" how="Trace the dotted bridge from C position to G position in one smooth line, without lifting your pencil. Write lift, travel and land where they happen.">
      <svg viewBox="0 0 600 150" style={{width:'100%',display:'block'}}>
        {[[40, 'C position'], [360, 'G position']].map(([x, l]) => <g key={l}>{[0, 1, 2, 3, 4].map(k => <rect key={k} x={x + k * 40} y="92" width="40" height="44" fill={k === 0 ? '#fbe3da' : '#fff'} stroke={BK.ink} strokeWidth="1.6"/>)}<text x={x + 100} y="84" textAnchor="middle" fontSize="13" fontWeight="900" fill={BK.ink}>{l}</text></g>)}
        <path d="M60 92 C90 10 400 10 380 92" fill="none" stroke={BK.coral} strokeWidth="2.4" strokeDasharray="2 7" strokeLinecap="round"/>
        {[[118, 40], [220, 22], [330, 40]].map(([x, y], i) => <line key={i} x1={x - 26} x2={x + 26} y1={y + 18} y2={y + 18} stroke={BK.line} strokeWidth="1.4"/>)}
      </svg>
    </Part>
    <Faces/>
  </>);

  // 5 (faces "Hands together")
  P(<>
    <WbTop step={4}/>
    <Part kind="together" title="Mirror twins" how="Both hands are in the same position. One hand plays the coral key. Which letter does the other hand's same finger play?">
      <BkGrid cols={2} gap="6px 10px">{W.mirror.map((it, i) => <HpwMirrorCell key={i} item={it} n={i + 1} ex={i === 0}/>)}</BkGrid>
    </Part>
    <Part kind="home" title="Together this week" how="Do each one at the piano and tick a box each day.">
      <PhLog rows={['1+1, 2+2, 3+3, 4+4, 5+5 and back, saying the numbers', 'Slowly: one steady beat each, both keys exactly together', 'Eyes closed: feel both thumbs on their keys']} label={300}/>
    </Part>
    <Part kind="play" title="Draw the mirror" how="Put both hands flat, thumbs touching, and draw round them. Write the finger numbers: the same numbers face each other, like a mirror.">
      <div style={{display:'flex',flex:1}}>{area('Left hand · thumbs touching · right hand', 110)}</div>
    </Part>
    <Faces/>
  </>);

  // 6 (faces "Taking turns")
  P(<>
    <WbTop step={5}/>
    <Part kind="together" title="Call and answer" how="Both hands in C position. The right hand calls; the left hand answers with the same letters. Write the left hand's finger numbers.">
      <div style={{display:'grid',gap:8}}>{W.echo.map(([call, ans], i) => <ExCell key={i} n={i + 1} ex={i === 0}><div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:16,alignItems:'center',padding:'14px 6px 2px'}}>
        <div><div style={{fontSize:10.5,fontWeight:900,color:BK.muted,marginBottom:3}}>Right hand calls</div>{hpwCircles(call, false)}</div>
        <div><div style={{fontSize:10.5,fontWeight:900,color:BK.coral,marginBottom:3}}>Left hand answers</div>{hpwCircles(i === 0 ? ans : ans.split(' ').map(x => (x === '-' ? '-' : '?' + x)).join(' '), false)}</div>
      </div></ExCell>)}</div>
    </Part>
    <Part kind="play" title="Make your own echo" how="Write a call for the right hand in the first four circles. Write the left hand's answer, with the same letters, in the next four. Play it with someone at home: you call, they answer.">
      <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:16,padding:'8px 4px'}}>{['Right hand calls', 'Left hand answers'].map((l, k) => <div key={l}><div style={{fontSize:10.5,fontWeight:900,color:k ? BK.coral : BK.muted,marginBottom:4}}>{l}</div><PhCircles seq={['?', '?', '?', '?']} size={40}/></div>)}</div>
    </Part>
    <Faces/>
  </>);

  // 7 (faces "Tunes in C and G")
  P(<>
    <WbTop step={6}/>
    <Part kind="together" title="Fill in the missing numbers" how="Write the missing finger numbers in the coral circles, then play the tune. The first one is done.">
      <div style={{display:'grid',gap:8}}>{W.fill.map(([name, seq], i) => <div key={name} style={{display:'grid',gridTemplateColumns:'118px 1fr',alignItems:'center',gap:8,border:'1px solid rgba(38,41,107,0.16)',borderRadius:10,padding:'6px 8px'}}>
        <span style={{fontFamily:LB_SERIF,fontSize:14,fontWeight:800,color:BK.ink,lineHeight:1.15}}>{name}</span><PhCircles seq={seq} ex={i === 0} size={25}/></div>)}</div>
    </Part>
    <Part kind="home" title="Tunes this week" how="Play each tune. Tick it when the hand stays round and the beat stays steady.">
      <PhLog rows={['Up and down the street', 'The left hand climbs too', 'Over to G', 'Mirror twins', 'Echo']} label={190}/>
    </Part>
    <Part kind="play" title="Write your own tune" how="Right hand, C position. Write a finger number in each circle; a dashed circle holds one more beat. End on 1. Then play it, and give it a name.">
      <div style={{display:'grid',gap:8,padding:'4px 0'}}><PhCircles seq={['?', '?', '?', '?', '|', '?', '?', '?', '?', '|', '?', '?', '?', '?', '|', '?', '-', '-', '-']} size={27}/>
        <div style={{fontSize:12,color:BK.muted,display:'flex',alignItems:'center',gap:8}}>Name of my tune <span style={{display:'inline-block',flex:1,borderBottom:'1.5px solid ' + BK.line,height:18}}/></div></div>
    </Part>
    <Faces/>
  </>);

  // 8. the check-up on paper (faces My five checks)
  P(<HpPaperCheck/>);
  return <>{pages}</>;
}
function HpPaperCheck() {
  const C = HP_WB.chk;
  const cell = (pos, h, f, n) => <BkCell key={n} n={n}><div style={{display:'flex',alignItems:'center',gap:8,padding:'14px 2px 2px'}}><div style={{flex:1,minWidth:0}}><div style={{fontSize:10,fontWeight:900,color:BK.muted,textAlign:'center'}}>{hpwHand(h)}</div>{hpwKeys(pos, h, hpFingerD(pos, h, f), { W: 11, k: 1 })}</div>{bkBox(32, 28)}</div></BkCell>;
  return <div className="lb-paper" style={{display:'flex',flexDirection:'column',gap:4}}>
    <LbPaperHead/>
    {bkSec('A', 'C position: which finger plays the coral key?')}
    <BkGrid cols={4} gap="6px 8px">{C.c.map(([h, f], i) => cell('C', h, f, i + 1))}</BkGrid>
    {bkSec('B', 'G position: which finger plays the coral key?')}
    <BkGrid cols={4} gap="6px 8px">{C.g.map(([h, f], i) => cell('G', h, f, i + 5))}</BkGrid>
    {bkSec('C', 'Which position (C or G)? Which hand (R or L)?')}
    <BkGrid cols={4} gap="6px 8px">{C.where.map(([pos, h], i) => { const lit = {}; hpKeysOf(pos, h).forEach(d => { lit[d] = 'cor'; });
      return <BkCell key={i} n={i + 9}><div style={{display:'grid',gap:4,padding:'14px 0 0'}}><HpKeys pos={pos} hands={h} span={[17, 37]} fingers={false} letters={false} names={false} mc={false} pale={false} lit={lit} W={7} k={1}/>
        <div style={{display:'flex',justifyContent:'center',gap:8,fontSize:10.5,fontWeight:900,color:BK.muted}}><span style={{display:'inline-flex',alignItems:'center',gap:3}}>C/G {bkBox(26, 22)}</span><span style={{display:'inline-flex',alignItems:'center',gap:3}}>R/L {bkBox(26, 22)}</span></div></div></BkCell>; })}</BkGrid>
    {bkSec('D', 'Mirror twins: which letter does the other hand\'s same finger play?')}
    <BkGrid cols={4} gap="6px 8px">{C.mirror.map((it, i) => { const [pos, h, f] = it; return <BkCell key={i} n={i + 13}><div style={{display:'grid',gap:3,padding:'14px 0 0'}}>
      <div style={{fontSize:9.5,fontWeight:900,color:BK.muted,lineHeight:1.2}}>{hpwHand(h)}, {pos} position, finger {f}</div><HpKeys pos={pos} hands="LR" fingers={false} letters={false} names={false} mc={false} lit={{ [hpFingerD(pos, h, f)]: 'cor' }} W={7} k={1}/>
      <div style={{display:'flex',justifyContent:'center'}}>{bkBox(30, 24)}</div></div></BkCell>; })}</BkGrid>
    {bkSec('E', 'Right hand, C position: write the missing finger number.')}
    <BkGrid cols={4} gap="6px 8px">{C.fill.map((seq, i) => <BkCell key={i} n={i + 17}><div style={{display:'flex',justifyContent:'center',padding:'14px 2px 4px'}}><PhCircles seq={seq} size={22}/></div></BkCell>)}</BkGrid>
  </div>;
}
function HpTeacher() {
  const W = HP_WB, C = W.chk, pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="hand-positions" teacher>{content}</WbPage>);
  const fill = (seq) => seq.filter(x => x[0] === '?').map(x => x.slice(1)).join(', ');
  P(<>
    <div style={{fontFamily:LB_SERIF,fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('hand-positions')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 12px',lineHeight:1.5}}>Each workbook page faces its Lesson Book page. On the keys only: no staff yet. Every answer here should also be shown at the piano; the paper is the reminder. Chapter 1's five checks still come first, every time at the piano.</div>
    <TcBlock page={2} title="C position" answers={<>{tcAns('TRY IT', W.c.map(([h, f]) => f + ' (' + h + ')'))}{tcAns('PLAY', ['right hand C D E F G from middle C, 1 to 5; left hand C D E F G below it, 5 to 1'])}</>}
      watch="Numbering the left hand from the thumb up the keys (it goes 5 4 3 2 1). Two fingers squeezed onto one key, or a finger left with no key."
      say="“One finger, one key. Right thumb on middle C; left little finger on the C below.”"/>
    <TcBlock page={3} title="G position" answers={<>{tcAns('TRY IT', W.g.map(([h, f]) => f + ' (' + h + ')'), 1)}{tcAns('YOUR TURN', ['right hand: finger 4', 'left hand: finger 2'], 7)}{tcAns('PLAY', ['G A B C D'])}</>}
      watch="Moving the hand but not the numbers: the shape is the same, only the place changes. The left hand sits lower than it did for C."
      say="“The same shape on G. Which finger plays C now?”"/>
    <TcBlock page={4} title="Move between them" answers={<>{tcAns('TRY IT', W.where.map(([pos, h]) => pos + ', ' + h))}{tcAns('PLAY', ['one unbroken line from C to G; lift over the first keys, travel over the middle, land on G'])}</>}
      watch="Fingers crawling along the keys to the new place, or a hand that flattens on the way. One silent beat to move, on a steady beat."
      say="“Lift, travel, land: the arm carries the hand.”"/>
  </>);
  P(<>
    <TcBlock page={5} title="Hands together" answers={<>{tcAns('TRY IT', W.mirror.map(hpwMirror))}{tcAns('PLAY', ['two hands drawn thumbs touching, the same numbers facing each other'])}</>}
      watch="Same numbers together move the hands in opposite directions: the shapes mirror each other. Both keys exactly together; slow."
      say="“Same numbers together: mirror twins.”"/>
    <TcBlock page={6} title="Taking turns" answers={<>{tcAns('TRY IT', W.echo.map(([c, a]) => 'right ' + c.replace(/ -/, '') + ' → left ' + a.replace(/ -/, '')))}{tcAns('PLAY', ['any call; the answer uses the same letters, so right 1 2 3 is left 5 4 3'])}</>}
      watch="The waiting hand lifting off into the lap. It stays on its keys, ready and quiet."
      say="“The waiting hand stays ready on its keys.”"/>
    <TcBlock page={7} title="Tunes in C and G" answers={<>{tcAns('TRY IT', W.fill.map(([n, s]) => n + ': ' + fill(s)))}{tcAns('PLAY', ['any tune of finger numbers 1 to 5, ending on 1'])}</>}
      watch="Rushing the dashed circles: each one holds a whole beat. Over to G: the lift happens in the silent moment, not by stretching."
      say="“Round hand, one finger on each key, a steady beat.”"/>
    <TcBlock page={8} title="The check-up on paper (the Workbook's last page)" answers={<>{tcAns('A', C.c.map(([, f]) => String(f)))}{tcAns('B', C.g.map(([, f]) => String(f)), 5)}{tcAns('C', C.where.map(([pos, h]) => pos + ', ' + h), 9)}{tcAns('D', C.mirror.map(hpwMirror), 13)}{tcAns('E', C.fill.map(fill), 17)}
      <div style={{fontSize:12,color:BK.ink,marginTop:6,lineHeight:1.5}}>One mark for each answer (C: both letters right for the mark). Score each part on its own (4 marks each, pass 3+). Not passed? Go back to that step's page: A p.2 · B p.3 · C p.4 · D p.5 · E p.7. Then check it at the piano, not just on paper.</div></>}/>
  </>);
  return <>{pages}</>;
}
WORKBOOKS['hand-positions'] = HpWorkbook;
TEACHER_COPIES['hand-positions'] = HpTeacher;
