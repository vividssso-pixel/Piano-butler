import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
NEW = r"""
// ─── Phase 570: Scales, lesson 1 (rebuilt like the Accidentals lessons): the major scale pattern T T S T T T S, on C major.
// The whole picture, then one step at a time, then her turn: the line names the step (whole or half) and she taps the key.
// Her facts: T T S T T T S; the two half steps sit between notes 3-4 and 7-8 (E-F and B-C on C major) (MajorShapeCard).
const SC_C = { keys: [0, 2, 4, 5, 7, 9, 11, 12], names: ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C'], steps: [2, 2, 1, 2, 2, 2, 1] };
const SC_COL = { 2: '#26296b', 1: '#c0431f' };   // whole = navy, half = coral
const SC_EX = [
  ['C to D: a whole step (T). One black key sits between.', 'C에서 D: 온음(T). 사이에 검은건반이 하나 있어요.'],
  ['D to E: a whole step (T) again.', 'D에서 E: 이번에도 온음(T)이에요.'],
  ['E to F: a half step (S). No black key between: the very next key.', 'E에서 F: 반음(S). 사이에 검은건반이 없어요. 바로 옆 건반이에요.'],
  ['F to G: a whole step (T).', 'F에서 G: 온음(T)이에요.'],
  ['G to A: a whole step (T).', 'G에서 A: 온음(T)이에요.'],
  ['A to B: a whole step (T).', 'A에서 B: 온음(T)이에요.'],
  ['B to C: a half step (S). No black key between either.', 'B에서 C: 반음(S). 여기도 사이에 검은건반이 없어요.'],
];
function ScPills({ upTo = 7, cur = -1 }) {
  return <div style={{display:'grid',gridTemplateColumns:'repeat(7,minmax(0,1fr))',gap:5,maxWidth:330,margin:'10px auto 0'}}>
    {SC_C.steps.map((sz, i) => { const on = i < upTo, half = sz === 1;
      return <div key={i} style={{height:36,borderRadius:10,display:'flex',alignItems:'center',justifyContent:'center',fontWeight:900,fontSize:16,
        background: !on ? 'transparent' : half ? '#fbe3da' : '#e6e7f1', color: !on ? 'rgba(38,41,107,0.25)' : half ? '#c0431f' : '#26296b',
        border:'1.5px solid ' + (i === cur ? SC_COL[sz] : on ? (half ? '#e4572e' : 'rgba(38,41,107,0.25)') : 'rgba(38,41,107,0.14)'), boxShadow: i === cur ? '0 0 0 2px ' + SC_COL[sz] + '33' : 'none'}}>{on ? (half ? 'S' : 'T') : ''}</div>; })}
  </div>;
}
function ScShape() {
  const [view, setView] = useState('all');   // 'all' -> 'one' -> 'try'
  const [i, setI] = useState(0), [shown, setShown] = useState(false), [nonce, setNonce] = useState(0);
  const [at, setAt] = useState(0), [bad, setBad] = useState(null);   // her turn: how many notes she has found (0 = none), the wrong key just tapped
  const timers = useRef([]);
  const clear = () => { timers.current.forEach(clearTimeout); timers.current = []; };
  useEffect(() => clear, []);
  const K = SC_C.keys, N = SC_C.names, ST = SC_C.steps;
  const arc = (j, anim) => [K[j], K[j + 1], anim, SC_COL[ST[j]], 0];
  const show = (idx) => { clear(); setI(idx); setShown(false); setNonce(n => n + 1); playKey(K[idx], 0.45);
    timers.current.push(setTimeout(() => { setShown(true); playKey(K[idx + 1], 0.6); }, 750)); };
  const titleStyle = {textAlign:'center',fontFamily:"'Playfair Display', Georgia, serif",fontSize:22,fontWeight:900,color:'#26296b',lineHeight:1.2,margin:'0 0 8px',textWrap:'balance'};
  const lineStyle = {textAlign:'center',fontSize:15,fontWeight:800,color:'#26296b',margin:'8px 0 6px',minHeight:42,textWrap:'balance',wordBreak:'keep-all'};
  const prim = {...KF_BTN,minWidth:140,background:'#26296b',color:'#fffefa',borderColor:'#26296b'};
  const row = (children) => <div style={{textAlign:'center',marginTop:14,display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap'}}>{children}</div>;
  const nmAll = {}; K.forEach((k, j) => { nmAll[k] = N[j]; });
  let body;
  if (view === 'all') {
    body = <>
      <div style={titleStyle}>{t('The major scale pattern', '장음계의 모양')}</div>
      <div style={lineStyle}>{t('Tone, tone, semitone, tone, tone, tone, semitone.', '온음, 온음, 반음, 온음, 온음, 온음, 반음.')}</div>
      <AcKeys marks={Object.fromEntries(K.map(k => [k, 'pass']))} arcs={ST.map((_, j) => arc(j, false))} nonce="all" names={nmAll}/>
      <ScPills/>
      {row(<button className="ghost-btn" style={prim} onClick={() => { setView('one'); show(0); }}>{t('One by one →', '하나씩 →')}</button>)}
    </>;
  } else if (view === 'one') {
    const marks = {}; for (let j = 0; j <= i; j++) marks[K[j]] = 'pass'; marks[K[i]] = 'pass'; if (shown) marks[K[i + 1]] = 'pick';
    const nm = {}; for (let j = 0; j <= i; j++) nm[K[j]] = N[j]; if (shown) nm[K[i + 1]] = N[i + 1];
    const arcs = []; for (let j = 0; j < i; j++) arcs.push(arc(j, false)); if (shown) arcs.push(arc(i, true));
    body = <>
      <div style={titleStyle}>{t('The major scale pattern', '장음계의 모양')}</div>
      <div style={lineStyle}>{shown ? t(SC_EX[i][0], SC_EX[i][1]) : ''}</div>
      <AcKeys marks={marks} arcs={arcs} nonce={nonce} names={nm}/>
      <ScPills upTo={shown ? i + 1 : i} cur={shown ? i : -1}/>
      {row(<>
        <button className="ghost-btn" style={{...KF_BTN,minWidth:110}} onClick={() => { clear(); if (i === 0) setView('all'); else show(i - 1); }}>{t('← Back', '← 이전')}</button>
        <button className="ghost-btn" style={prim} onClick={() => { clear(); if (i === 6) { setView('try'); setAt(0); setBad(null); setNonce(n => n + 1); } else show(i + 1); }}>{i === 6 ? t('Your turn →', '내가 해보기 →') : t('Next →', '다음 →')}</button>
      </>)}
    </>;
  } else {
    // her turn: start on C; the line says the next step (whole or half); she taps that key
    const done = at >= 7, marks = {}, nm = {}, arcs = [];
    for (let j = 0; j <= at; j++) { marks[K[j]] = j === at && !done ? 'pick' : 'pass'; nm[K[j]] = N[j]; }
    for (let j = 0; j < at; j++) arcs.push(arc(j, j === at - 1));
    if (bad != null) marks[bad] = 'bad';
    const stepWord = (sz) => sz === 2 ? t('a whole step up (T)', '온음 위로 (T)') : t('a half step up (S)', '반음 위로 (S)');
    const line = done ? t('That is the C major scale: T T S T T T S.', '이게 C 장음계예요: T T S T T T S.')
      : bad != null ? t('Not that key. From ' + N[at] + ', go ' + stepWord(ST[at]) + '.', '그 건반이 아니에요. ' + N[at] + '에서 ' + stepWord(ST[at]) + ' 가요.')
      : at === 0 ? t('Start on C. Then tap ' + stepWord(ST[0]) + '.', 'C에서 시작해요. 그다음 ' + stepWord(ST[0]) + ' 건반을 눌러요.')
      : t('From ' + N[at] + ', tap ' + stepWord(ST[at]) + '.', N[at] + '에서 ' + stepWord(ST[at]) + ' 건반을 눌러요.');
    const tap = (k) => { if (done) return; clear(); if (k === K[at + 1]) { setBad(null); setAt(at + 1); setNonce(n => n + 1); playKey(K[at], 0.35); timers.current.push(setTimeout(() => playKey(k, 0.6), 400)); }
      else { setBad(k); playKey(k, 0.4); timers.current.push(setTimeout(() => setBad(null), 1100)); } };
    body = <>
      <div style={titleStyle}>{t('Your turn', '내가 해보기')}</div>
      <div style={lineStyle}>{line}</div>
      <AcKeys marks={at === 0 ? { ...marks, [K[0]]: 'pick' } : marks} arcs={arcs} nonce={nonce} names={nm} onTap={tap}/>
      <ScPills upTo={at} cur={at - 1}/>
      {row(<>
        <button className="ghost-btn" style={{...KF_BTN,minWidth:110}} onClick={() => { clear(); setView('one'); show(6); }}>{t('← Back', '← 이전')}</button>
        {done && <button className="ghost-btn" style={prim} onClick={() => { setAt(0); setBad(null); setNonce(n => n + 1); }}>{t('Again', '다시 하기')}</button>}
      </>)}
    </>;
  }
  return <div className="try-box" data-sc-lesson="shape" style={{background:'#fff',border:'1px solid var(--border)',borderRadius:10,padding:'10px 10px 12px',margin:'4px 0 16px'}}>{body}</div>;
}
[['sc-shape', 'The major scale pattern', '장음계의 모양', 'T T S T T T S, on the keys of C.', 'C의 건반 위에서 T T S T T T S.']].forEach(([id, en, ko, benEn, bko]) => {
  TOOLS.push({ id, ch: 'concept', title: en, blurb: benEn, hidden: true, get kicker() { return TOOL_AREAS.find(a => a.id === 'pitch').name + ' · ' + (LANG === 'ko' ? '스케일' : 'Scales'); }, C: () => <ScShape/> });
  TOOL_KO[id] = [ko, bko];
  const tl = TOOLS[TOOLS.length - 1], k = TOOL_KO[id], ti = tl.title, bl = tl.blurb; tl.titleEn = ti; tl.blurbEn = bl;
  Object.defineProperty(tl, 'title', { get: () => (LANG === 'ko' ? k[0] : ti), enumerable: true, configurable: true });
  Object.defineProperty(tl, 'blurb', { get: () => (LANG === 'ko' ? k[1] : bl), enumerable: true, configurable: true });
  TOOL_CONCEPT[id] = 'p-scale';
});
"""
rep("\n// lesson 5: the natural.", NEW + "\n// lesson 5: the natural.")
rep("""  'p-scale': {
    check: 'scales', tools: ['scale-finder'], more: ['csx-penta'],""","""  'p-scale': {
    lessons: ['sc-shape'], check: 'scales', tools: [], more: [],""")
open(sys.argv[2],'w',encoding='utf-8').write(s)
