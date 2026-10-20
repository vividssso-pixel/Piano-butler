import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
HAT = '̂'
NEW = r"""
// ─── Phase 572: Scales, lesson 3: the degrees of the scale, their numbers (1̂ 2̂ 3̂…) and names (tonic … leading note).
// Her text only: DEGREE_NAMES / DEGREE_WHY (and the Korean pair) from her Scale degree names card.
const scHat = (n) => n + '__HAT__';
function ScDeg() {
  const [view, setView] = useState('all');   // 'all' -> 'one' -> 'try'
  const [i, setI] = useState(0), [nonce, setNonce] = useState(0), [kk, setKk] = useState('C');
  const [seq, setSeq] = useState([]), [at, setAt] = useState(0), [bad, setBad] = useState(null);
  const timers = useRef([]);
  const clear = () => { timers.current.forEach(clearTimeout); timers.current = []; };
  useEffect(() => clear, []);
  const titleStyle = {textAlign:'center',fontFamily:"'Playfair Display', Georgia, serif",fontSize:22,fontWeight:900,color:'#26296b',lineHeight:1.2,margin:'0 0 8px',textWrap:'balance'};
  const lineStyle = {textAlign:'center',fontSize:15,fontWeight:800,color:'#26296b',margin:'8px 0 6px',minHeight:42,textWrap:'balance',wordBreak:'keep-all'};
  const prim = {...KF_BTN,minWidth:140,background:'#26296b',color:'#fffefa',borderColor:'#26296b'};
  const row = (children) => <div style={{textAlign:'center',marginTop:14,display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap'}}>{children}</div>;
  const title = t('The degrees of the scale', '음계의 음 번호와 이름');
  const nm = (j) => LANG === 'ko' ? DEGREE_NAMES_KO[j] : DEGREE_NAMES[j];
  const why = (j) => LANG === 'ko' ? DEGREE_WHY_KO[j] : DEGREE_WHY[j];
  const newRound = (key) => { const order = shuffle([0, 1, 2, 3, 4, 5, 6]); setSeq(order.map((d, q) => ({ d, by: q % 2 === 0 ? 'name' : 'num' }))); setAt(0); setBad(null); setNonce(n => n + 1); };
  let body;
  if (view === 'all') {
    const K = scIdx('C'), marks = {}, names = {}; K.forEach((k, j) => { marks[k] = 'pass'; names[k] = scHat(j === 7 ? 8 : j + 1); });
    body = <>
      <div style={titleStyle}>{title}</div>
      <div style={lineStyle}>{t('Every note of the scale has a number and a name.', '음계의 음마다 번호와 이름이 있어요.')}</div>
      <ScKeys ks={K} marks={marks} names={names} arcs={[]} nonce="all"/>
      {row(<button className="ghost-btn" style={prim} onClick={() => { setView('one'); setI(0); setNonce(n => n + 1); playKey(K[0], 0.6); }}>{t('One by one →', '하나씩 →')}</button>)}
    </>;
  } else if (view === 'one') {
    const K = scIdx('C'), marks = { [K[0]]: 'pass' }, names = {}; for (let j = 0; j <= i; j++) names[K[j]] = scHat(j + 1); marks[K[i]] = 'pick';
    body = <>
      <div style={titleStyle}>{title}</div>
      <div style={lineStyle}><span style={{color:'#c0431f'}}>{scHat(i + 1) + ' ' + nm(i)}</span>{': ' + why(i) + '.'}</div>
      <ScKeys ks={K} marks={marks} names={names} arcs={[]} nonce={nonce + ':' + i}/>
      {row(<>
        <button className="ghost-btn" style={{...KF_BTN,minWidth:110}} onClick={() => { clear(); if (i === 0) setView('all'); else { setI(i - 1); setNonce(n => n + 1); playKey(K[0], 0.4); timers.current.push(setTimeout(() => playKey(K[i - 1], 0.6), 400)); } }}>{t('← Back', '← 이전')}</button>
        <button className="ghost-btn" style={prim} onClick={() => { clear(); if (i === 6) { setView('try'); newRound(kk); } else { setI(i + 1); setNonce(n => n + 1); playKey(K[0], 0.4); timers.current.push(setTimeout(() => playKey(K[i + 1], 0.6), 400)); } }}>{i === 6 ? t('Your turn →', '내가 해보기 →') : t('Next →', '다음 →')}</button>
      </>)}
    </>;
  } else {
    const K = scIdx(kk), N = scNames(kk), done = at >= 7, marks = {}, names = {};
    seq.slice(0, at).forEach(({ d }) => { marks[K[d]] = 'good'; names[K[d]] = scHat(d + 1); });
    if (done) { marks[K[7]] = 'pass'; }
    if (bad != null) marks[bad] = 'bad';
    const cur = seq[at];
    const ask = cur ? (cur.by === 'name' ? t('Tap the ' + nm(cur.d) + '.', nm(cur.d) + ' 건반을 눌러요.') : t('Tap ' + scHat(cur.d + 1) + '.', scHat(cur.d + 1) + ' 건반을 눌러요.')) : '';
    const line = done ? t('All seven found: that is every degree of ' + N[0] + ' major.', '일곱 개를 다 찾았어요. ' + N[0] + ' 장음계의 모든 음이에요.')
      : bad != null ? t('Not that key. ' + ask, '그 건반이 아니에요. ' + ask) : ask + ' (' + (at + 1) + '/7)';
    const tap = (k) => { if (done) return; clear(); const j = K.indexOf(k);
      if (cur && k === K[cur.d] && j < 7) { setBad(null); setAt(at + 1); setNonce(n => n + 1); playKey(K[0], 0.35); timers.current.push(setTimeout(() => playKey(k, 0.6), 400)); }
      else { setBad(k); playKey(k, 0.4); timers.current.push(setTimeout(() => setBad(null), 1100)); } };
    body = <>
      <div style={titleStyle}>{t('Your turn', '내가 해보기')}</div>
      <div style={{display:'grid',gridTemplateColumns:'repeat(4,minmax(0,1fr))',gap:6,maxWidth:330,margin:'0 auto 6px'}}>
        {['C', 'G', 'F', 'D'].map(k => <button key={k} className={'chip' + (kk === k ? ' active' : '')} aria-pressed={kk === k} style={{...KF_BTN,minHeight:40,padding:'0 4px'}} onClick={() => { clear(); setKk(k); newRound(k); playKey(SF12.indexOf(k), 0.5); }}>{prettyNote(k)}</button>)}
      </div>
      <div style={lineStyle}>{line}</div>
      <ScKeys ks={K} marks={marks} names={names} arcs={[]} nonce={nonce + kk} onTap={tap}/>
      {row(<>
        <button className="ghost-btn" style={{...KF_BTN,minWidth:110}} onClick={() => { clear(); setView('one'); setI(6); setNonce(n => n + 1); }}>{t('← Back', '← 이전')}</button>
        {done && <button className="ghost-btn" style={prim} onClick={() => newRound(kk)}>{t('Again', '다시 하기')}</button>}
      </>)}
    </>;
  }
  return <div className="try-box" data-sc-lesson="deg" style={{background:'#fff',border:'1px solid var(--border)',borderRadius:10,padding:'10px 10px 12px',margin:'4px 0 16px'}}>{body}</div>;
}
""".replace('__HAT__', HAT)
rep("\n// lesson 5: the natural.", NEW + "\n// lesson 5: the natural.")
rep(" ['sc-same', 'The same pattern from any note', '어느 음에서 시작해도 같은 패턴', 'G has an F♯, F has a B♭: the pattern decides.', 'G에는 F♯, F에는 B♭: 패턴이 정해 줘요.', ScSame]].forEach(",
    " ['sc-same', 'The same pattern from any note', '어느 음에서 시작해도 같은 패턴', 'G has an F♯, F has a B♭: the pattern decides.', 'G에는 F♯, F에는 B♭: 패턴이 정해 줘요.', ScSame],\n ['sc-deg', 'The degrees of the scale', '음계의 음 번호와 이름', 'Tonic, supertonic … leading note.', '으뜸음, 윗으뜸음 … 이끎음.', ScDeg]].forEach(")
rep("lessons: ['sc-shape', 'sc-same'], check: 'scales'", "lessons: ['sc-shape', 'sc-same', 'sc-deg'], check: 'scales'")
open(sys.argv[2],'w',encoding='utf-8').write(s)
