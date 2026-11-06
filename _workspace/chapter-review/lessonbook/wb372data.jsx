// ─── Posture and hand shape (chapter 'posture-hands') ───
// Phase 372: the Workbook follows the Lesson Book page by page -- workbook page N faces Lesson Book page N, so the two
// can be printed as spreads (lesson on the left, its workbook page on the right). Pictures: the Lesson Book's own
// drawings (art369.jsx), the quiz versions with no hints.
const PH_SIT = [['good', 'Just right', true], ['low', 'Stool too low', false], ['high', 'Stool too high', false], ['close', 'Too close', false], ['far', 'Too far', false]];
const PH_HAND = [['good', 'The good shape', true], ['flat', 'Flat fingers', false], ['bridge', 'Knuckles collapsed', false], ['nail', 'Tip joint caving in', false], ['low', 'Wrist dropped', false], ['high', 'Wrist too high', false]];
const PH_ARM = [['The arm leads from above.', true], ['My elbows stay stuck to my body.', false], ['Even while a finger presses a key, the whole arm stays free.', true],
  ['After a key goes down, my wrist sinks below the keys.', false], ['Rag doll comes first: big parts of the body before small ones.', true], ['I squeeze hard to play loud.', false]];
const PH_WARMUPS = [['ragdoll', 'Rag doll'], ['wings', 'Elbow wings'], ['glide', 'Arm glide'], ['dive', 'Arm drop'], ['bridge', 'Knuckle bridge'], ['balloon', 'Wrist balloon']];
const PH_TUNES = ['Hop on 3', 'Neighbours', 'Up and back', 'Little hill', 'Stairs and slide'];
// a picture to judge: tick or cross
function PhPic({ art, ok, n, ex, h = 76, lit }) {
  return <ExCell n={n} ex={ex}><div style={{display:'flex',flexDirection:'column',alignItems:'center',gap:4,padding:'12px 2px 2px'}}>
    <PbArt name={art} h={h} lit={lit} style={{maxWidth:'100%'}}/>
    <TickCross ok={ok} ex={ex}/>
  </div></ExCell>;
}
// finger-walk circles: a number, '-' (hold), '|' (bar line), '?n' (a blank to fill in; ex shows the answer in coral)
function PhCircles({ seq, ex, size = 26 }) {
  return <div style={{display:'flex',flexWrap:'wrap',alignItems:'center',gap:5}}>{seq.map((x, i) => {
    const box = { width:size, height:size, borderRadius:size / 2, display:'inline-flex', alignItems:'center', justifyContent:'center', fontSize:size * 0.52, fontWeight:900 };
    if (x === '|') return <span key={i} style={{width:1.6,height:size,background:BK.ink,opacity:0.5,margin:'0 3px'}}/>;
    if (x === '-') return <span key={i} style={{...box, border:'1.6px dashed ' + BK.line}}/>;
    if (x[0] === '?') return <span key={i} style={{...box, border:'2px solid ' + BK.coral, background:'#fff', color:BK.coral, fontStyle:'italic'}}>{ex && i === seq.findIndex(y => y[0] === '?') ? x.slice(1) : ''}</span>;
    return <span key={i} style={{...box, border:'2px solid ' + BK.ink, background:'#fff', color:BK.ink}}>{x}</span>;
  })}</div>;
}
// a week of tick boxes, one row per thing to do
function PhLog({ rows, days = 5, label = 140 }) {
  const ds = BK_DAYS.slice(0, days);
  return <div style={{display:'grid',gridTemplateColumns:label + 'px repeat(' + days + ',1fr)',gap:4,fontSize:11.5,color:BK.ink,alignItems:'center'}}>
    <span/>{ds.map(d => <b key={d} style={{textAlign:'center',color:BK.muted,fontSize:10.5}}>{d}</b>)}
    {rows.map((l, r) => <React.Fragment key={r}><span style={{fontWeight:700,lineHeight:1.25}}>{l}</span>{ds.map(d => <span key={d} style={{justifySelf:'center',width:22,height:22,border:'1.5px solid ' + BK.line,borderRadius:5}}/>)}</React.Fragment>)}
  </div>;
}
function phWorkbook() {
  const order = withSeed('ph-wb-order', () => shuffle(PH_WARMUPS.slice(1)));
  const fingers = withSeed('ph-wb-fingers', () => shuffle([['R', 3], ['L', 1], ['R', 5], ['L', 2], ['R', 4], ['L', 5]]));
  const chk = withSeed('ph-wb-chk2', () => ({ st: shuffle(PH_SIT).slice(0, 4), ar: shuffle(PH_ARM).slice(0, 4), hs: shuffle(PH_HAND).slice(0, 4),
    fn: shuffle([2, 4, 5, 1]), lr: shuffle(['L', 'R', 'R', 'L']) }));
  return { order, fingers, chk };
}
const PH_FILL = [['Up and back', ['1', '2', '?3', '-', '|', '3', '?2', '1', '-']], ['Little hill', ['1', '2', '?3', '4', '|', '?3', '2', '1', '-']], ['Stairs and slide', ['1', '2', '3', '?4', '5', '-', '|', '5', '?4', '3', '2', '1', '-']]];
const PH_FILL_CHK = [['1', '2', '3', '?4', '5'], ['5', '4', '?3', '2', '1'], ['2', '3', '2', '?3'], ['1', '?2', '3', '2', '1']];
function phConcepts() {
  return [
    { id: 'st', name: 'Sitting at the piano', step: '1', page: '2' },
    { id: 'ar', name: 'The arm leads', step: '2-3', page: '3' },
    { id: 'hs', name: 'A round hand', step: '4', page: '4' },
    { id: 'lr', name: 'Left hand, right hand', step: '5-6', page: '5' },
    { id: 'fn', name: 'Finger numbers', step: '5-6', page: '5' },
    { id: 'fw', name: 'Finger walks', step: '7', page: '6' },
  ];
}
