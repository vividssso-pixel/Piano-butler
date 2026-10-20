import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
# TapKeyboard: optional crop window vx = [x0, x1] (svg units) so a two-octave board can show just one scale
rep("extraC = false, extraB = false, trail = null, trailLabels = null, overlay = null, top = 0 }) {", "extraC = false, extraB = false, trail = null, trailLabels = null, overlay = null, top = 0, vx = null }) {")
rep("<svg viewBox={'-1 ' + (-1 - TR) + ' ' + (width + 2) + ' ' + (whiteH + 2 + TR)} shapeRendering={edge}", "<svg viewBox={(vx ? vx[0] : -1) + ' ' + (-1 - TR) + ' ' + (vx ? vx[1] - vx[0] : width + 2) + ' ' + (whiteH + 2 + TR)} shapeRendering={edge}")
NEW = r"""
// ─── Phase 571: Scales, lesson 2: the same pattern from every note. G major (its F♯) and F major (its B♭), step by step, then her turn on any key.
// Her facts (MajorShapeCard / spellScale): start on G, keep the shape, the 6th-to-7th step must be a tone, so F becomes F♯; F major has the B♭.
const SC_OFF = [0, 2, 4, 5, 7, 9, 11, 12];
const scIdx = (key) => SC_OFF.map(o => SF12.indexOf(key) + o);
const scNames = (key) => spellScale(key).concat([key]).map(prettyNote);
function ScKeys({ marks, onTap, arcs, nonce, names, ks }) {
  const kx = keyCenterX, white = (i) => PC_INFO[((i % 12) + 12) % 12].white;
  const x0 = Math.min(...ks.map(kx)) - 24, x1 = Math.max(...ks.map(kx)) + 24;
  const pt = (i) => [kx(i), white(i) ? 99 : 58];
  const arrows = arcs.map(([a, b, anim, col], j) => {
    const [xa, ya] = pt(a), [xb, yb] = pt(b), dx = xb - xa, dy = yb - ya, L = Math.hypot(dx, dy), ux = dx / L, uy = dy / L;
    const s0 = anim ? 7 : 4, s1 = anim ? 5 : 3, hd = anim ? 10 : 4.5, w = anim ? 3.4 : 1.5;
    const sx = xa + ux * s0, sy = ya + uy * s0, ex = xb - ux * s1, ey = yb - uy * s1, ang = 0.55;
    const hx = (sg) => ex - hd * (ux * Math.cos(ang) - sg * uy * Math.sin(ang)), hy = (sg) => ey - hd * (uy * Math.cos(ang) + sg * ux * Math.sin(ang));
    const line = 'M' + sx + ',' + sy + ' L' + ex + ',' + ey, head = 'M' + hx(1) + ',' + hy(1) + ' L' + ex + ',' + ey + ' L' + hx(-1) + ',' + hy(-1);
    const dash = anim ? { strokeDasharray: '120', strokeDashoffset: '120', animation: 'drawArc 0.45s ease-out forwards' } : {};
    const headAnim = anim ? { animation: 'fadeUp 0.3s both 0.3s' } : {};
    return <g key={j + ':' + a + ':' + b + ':' + nonce} fill="none" strokeLinecap="round" strokeLinejoin="round" style={{pointerEvents:'none'}}>
      <path d={line} stroke="#fff" strokeWidth={w + 3} style={dash}/><path d={head} stroke="#fff" strokeWidth={w + 3} style={headAnim}/>
      <path d={line} stroke={col || '#26296b'} strokeWidth={w} style={dash}/><path d={head} stroke={col || '#26296b'} strokeWidth={w} style={headAnim}/>
    </g>; });
  return (<div style={{maxWidth:330,margin:'0 auto'}}>
    <TapKeyboard octaves={2} extraC labels="white" marks={marks} onTap={onTap} top={46} vx={[x0, x1]} overlay={<g aria-hidden="true">{arrows}{Object.entries(names || {}).map(([k, txt]) =>
      <text key={'n' + k + txt} x={kx(+k)} y={white(+k) ? -9 : -27} textAnchor="middle" fontSize="17" fontWeight="900" fill="#c0431f" style={{animation:'fadeUp 0.3s both'}}>{txt}</text>)}</g>}/>
  </div>);
}
// the story screens: n = notes shown (from the tonic), bad = a key the pattern rules out, arc = the one move drawn strong
const SC_SAME = [
  { key: 'G', n: 6, text: ['Start on G and keep the pattern: T T S T T. Now we stand on E.', 'G에서 시작해서 패턴을 지켜요: T T S T T. 지금 E에 있어요.'] },
  { key: 'G', n: 6, bad: 17, text: ['The pattern wants a whole step (T) from E. F is only a half step: too short.', '패턴은 E에서 온음(T)을 원해요. F는 반음뿐이라 너무 짧아요.'] },
  { key: 'G', n: 7, arc: 5, text: ['So the 7th note is the next key on: F♯, a whole step from E.', '그래서 7번째 음은 한 건반 더 가서 F♯이에요. E에서 온음이에요.'] },
  { key: 'G', n: 8, arc: 6, text: ['F♯ to G is a half step (S). That F♯ is G major’s key signature.', 'F♯에서 G는 반음(S)이에요. 이 F♯이 G장조의 조표예요.'] },
  { key: 'F', n: 3, text: ['Start on F: T T. F, G, A.', 'F에서 시작해요: T T. F, G, A.'] },
  { key: 'F', n: 3, bad: 11, text: ['The pattern wants a half step (S) from A. B is a whole step: too far.', '패턴은 A에서 반음(S)을 원해요. B는 온음이라 너무 멀어요.'] },
  { key: 'F', n: 4, arc: 2, text: ['So the 4th note is the very next key: B♭, a half step from A.', '그래서 4번째 음은 바로 옆 건반 B♭이에요. A에서 반음이에요.'] },
  { key: 'F', n: 8, arc: 6, text: ['Then T T T S: C, D, E, F. That B♭ is F major’s key signature.', '그다음 T T T S: C, D, E, F. 이 B♭이 F장조의 조표예요.'] },
];
const SC_PICK = ['G', 'D', 'A', 'E', 'F', 'Bb', 'Eb', 'Ab'];
function ScSame() {
  const [view, setView] = useState('all');   // 'all' -> 'one' -> 'try'
  const [i, setI] = useState(0), [nonce, setNonce] = useState(0), [kk, setKk] = useState('G'), [at, setAt] = useState(0), [bad, setBad] = useState(null);
  const timers = useRef([]);
  const clear = () => { timers.current.forEach(clearTimeout); timers.current = []; };
  useEffect(() => clear, []);
  const titleStyle = {textAlign:'center',fontFamily:"'Playfair Display', Georgia, serif",fontSize:22,fontWeight:900,color:'#26296b',lineHeight:1.2,margin:'0 0 8px',textWrap:'balance'};
  const lineStyle = {textAlign:'center',fontSize:15,fontWeight:800,color:'#26296b',margin:'8px 0 6px',minHeight:42,textWrap:'balance',wordBreak:'keep-all'};
  const prim = {...KF_BTN,minWidth:140,background:'#26296b',color:'#fffefa',borderColor:'#26296b'};
  const row = (children) => <div style={{textAlign:'center',marginTop:14,display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap'}}>{children}</div>;
  const title = t('The same pattern, from any note', '어느 음에서 시작해도 같은 패턴');
  const ST = [2, 2, 1, 2, 2, 2, 1];
  const mv = (K, j, anim) => [K[j], K[j + 1], anim, SC_COL[ST[j]]];
  const playAt = (K, j) => { clear(); playKey(K[j], 0.4); timers.current.push(setTimeout(() => playKey(K[j + 1], 0.6), 450)); };
  let body;
  if (view === 'all') {
    const K = scIdx('G'), N = scNames('G'), marks = {}, names = {}; K.forEach((k, j) => { marks[k] = j === 6 ? 'pick' : 'pass'; names[k] = N[j]; });
    body = <>
      <div style={titleStyle}>{title}</div>
      <div style={lineStyle}>{t('Start on G and keep the same pattern. One note has to change.', 'G에서 시작해도 같은 패턴이에요. 음 하나가 바뀌어요.')}</div>
      <ScKeys ks={K} marks={marks} names={names} arcs={ST.map((_, j) => mv(K, j, false))} nonce="all"/>
      <ScPills/>
      {row(<button className="ghost-btn" style={prim} onClick={() => { setView('one'); setI(0); setNonce(n => n + 1); }}>{t('One by one →', '하나씩 →')}</button>)}
    </>;
  } else if (view === 'one') {
    const E = SC_SAME[i], K = scIdx(E.key), N = scNames(E.key), marks = {}, names = {}, arcs = [];
    for (let j = 0; j < E.n; j++) { marks[K[j]] = 'pass'; names[K[j]] = N[j]; }
    if (E.arc != null) marks[K[E.arc + 1]] = 'pick';
    for (let j = 0; j < E.n - 1; j++) arcs.push(mv(K, j, j === E.arc));
    if (E.bad != null) { marks[E.bad] = 'bad'; arcs.push([K[E.n - 1], E.bad, false, SC_COL[E.bad - K[E.n - 1] === 1 ? 1 : 2]]); }
    body = <>
      <div style={titleStyle}>{title}</div>
      <div style={lineStyle}>{t(E.text[0], E.text[1])}</div>
      <ScKeys ks={K} marks={marks} names={names} arcs={arcs} nonce={nonce + ':' + i}/>
      <ScPills upTo={E.arc != null ? E.arc + 1 : Math.max(E.n - 1, 0)} cur={E.arc != null ? E.arc : -1}/>
      {row(<>
        <button className="ghost-btn" style={{...KF_BTN,minWidth:110}} onClick={() => { clear(); if (i === 0) setView('all'); else { setI(i - 1); setNonce(n => n + 1); } }}>{t('← Back', '← 이전')}</button>
        <button className="ghost-btn" style={prim} onClick={() => { clear(); if (i === SC_SAME.length - 1) { setView('try'); setAt(0); setBad(null); setNonce(n => n + 1); } else { const nx = SC_SAME[i + 1]; if (nx.arc != null) playAt(scIdx(nx.key), nx.arc); setI(i + 1); setNonce(n => n + 1); } }}>{i === SC_SAME.length - 1 ? t('Your turn →', '내가 해보기 →') : t('Next →', '다음 →')}</button>
      </>)}
    </>;
  } else {
    const K = scIdx(kk), N = scNames(kk), done = at >= 7, marks = {}, names = {}, arcs = [];
    for (let j = 0; j <= at; j++) { marks[K[j]] = j === at && !done ? 'pick' : 'pass'; names[K[j]] = N[j]; }
    for (let j = 0; j < at; j++) arcs.push(mv(K, j, j === at - 1));
    if (bad != null) marks[bad] = 'bad';
    const word = (sz) => sz === 2 ? t('a whole step up (T)', '온음 위로 (T)') : t('a half step up (S)', '반음 위로 (S)');
    const line = done ? t('That is ' + N[0] + ' major: the same pattern.', N[0] + ' 장음계예요. 같은 패턴이에요.')
      : bad != null ? t('Not that key. From ' + N[at] + ', go ' + word(ST[at]) + '.', '그 건반이 아니에요. ' + N[at] + '에서 ' + word(ST[at]) + ' 가요.')
      : at === 0 ? t('Start on ' + N[0] + '. Then tap ' + word(ST[0]) + '.', N[0] + '에서 시작해요. 그다음 ' + word(ST[0]) + ' 건반을 눌러요.')
      : t('From ' + N[at] + ', tap ' + word(ST[at]) + '.', N[at] + '에서 ' + word(ST[at]) + ' 건반을 눌러요.');
    const tap = (k) => { if (done) return; clear(); if (k === K[at + 1]) { setBad(null); setAt(at + 1); setNonce(n => n + 1); playKey(K[at], 0.35); timers.current.push(setTimeout(() => playKey(k, 0.6), 400)); }
      else { setBad(k); playKey(k, 0.4); timers.current.push(setTimeout(() => setBad(null), 1100)); } };
    body = <>
      <div style={titleStyle}>{t('Your turn', '내가 해보기')}</div>
      <div style={{display:'grid',gridTemplateColumns:'repeat(4,minmax(0,1fr))',gap:6,maxWidth:330,margin:'0 auto 6px'}}>
        {SC_PICK.map(k => <button key={k} className={'chip' + (kk === k ? ' active' : '')} aria-pressed={kk === k} style={{...KF_BTN,minHeight:40,padding:'0 4px'}} onClick={() => { clear(); setKk(k); setAt(0); setBad(null); setNonce(n => n + 1); playKey(SF12.indexOf(k), 0.5); }}>{prettyNote(k)}</button>)}
      </div>
      <div style={lineStyle}>{line}</div>
      <ScKeys ks={K} marks={at === 0 ? { ...marks, [K[0]]: 'pick' } : marks} names={names} arcs={arcs} nonce={nonce + kk} onTap={tap}/>
      <ScPills upTo={at} cur={at - 1}/>
      {row(<>
        <button className="ghost-btn" style={{...KF_BTN,minWidth:110}} onClick={() => { clear(); setView('one'); setI(SC_SAME.length - 1); setNonce(n => n + 1); }}>{t('← Back', '← 이전')}</button>
        {done && <button className="ghost-btn" style={prim} onClick={() => { setAt(0); setBad(null); setNonce(n => n + 1); }}>{t('Again', '다시 하기')}</button>}
      </>)}
    </>;
  }
  return <div className="try-box" data-sc-lesson="same" style={{background:'#fff',border:'1px solid var(--border)',borderRadius:10,padding:'10px 10px 12px',margin:'4px 0 16px'}}>{body}</div>;
}
"""
rep("\n// lesson 5: the natural.", NEW + "\n// lesson 5: the natural.")
rep("[['sc-shape', 'The major scale pattern', '장음계의 모양', 'T T S T T T S, on the keys of C.', 'C의 건반 위에서 T T S T T T S.']].forEach(([id, en, ko, benEn, bko]) => {",
    "[['sc-shape', 'The major scale pattern', '장음계의 모양', 'T T S T T T S, on the keys of C.', 'C의 건반 위에서 T T S T T T S.', ScShape],\n ['sc-same', 'The same pattern from any note', '어느 음에서 시작해도 같은 패턴', 'G has an F♯, F has a B♭: the pattern decides.', 'G에는 F♯, F에는 B♭: 패턴이 정해 줘요.', ScSame]].forEach(([id, en, ko, benEn, bko, Comp]) => {")
rep("C: () => <ScShape/> });", "C: () => <Comp/> });")
rep("lessons: ['sc-shape'], check: 'scales'", "lessons: ['sc-shape', 'sc-same'], check: 'scales'")
open(sys.argv[2],'w',encoding='utf-8').write(s)
