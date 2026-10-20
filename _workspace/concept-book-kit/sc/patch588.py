import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
NEW = r"""
// ─── Phase 583 (her order, 2026-10-20): Scales, lesson 9, all twelve keys. One pattern (T T S T T T S), twelve start notes: white-key starts, black-key starts, all twelve; then her turn on any of the twelve.
const SC_W7 = ['C', 'G', 'D', 'A', 'E', 'F', 'B'], SC_B5 = ['Bb', 'Eb', 'Ab', 'Db', 'Gb'], SC_12 = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B'];
const SC_ALLSTEPS = [
  { set: SC_W7, text: ['White-key starts: C G D A E F B. Tap one: the pattern T T S T T T S stays the same.', '흰건반에서 시작하는 조: C G D A E F B. 하나 눌러봐요. 패턴 T T S T T T S는 그대로예요.'] },
  { set: SC_B5, text: ['Black-key starts: B♭ E♭ A♭ D♭ G♭. Tap one: the same pattern again.', '검은건반에서 시작하는 조: B♭ E♭ A♭ D♭ G♭. 하나 눌러봐요. 같은 패턴이에요.'] },
  { set: SC_12, text: ['Twelve start notes in all, and one pattern for every one of them.', '시작하는 음은 모두 열두 개예요. 열두 개 모두 패턴은 하나예요.'] },
];
function ScAll() {
  const [view, setView] = useState('all');   // 'all' -> 'one' -> 'try'
  const [i, setI] = useState(0), [nonce, setNonce] = useState(0), [kk, setKk] = useState('C');
  const [tk, setTk] = useState('Eb'), [at, setAt] = useState(0), [bad, setBad] = useState(null);
  const timers = useRef([]);
  const clear = () => { timers.current.forEach(clearTimeout); timers.current = []; };
  useEffect(() => clear, []);
  const title = t('All twelve keys', '12개 조 모두');
  const ST = [2, 2, 1, 2, 2, 2, 1];
  const mv = (K, j, anim) => [K[j], K[j + 1], anim, SC_COL[ST[j]]];
  const chips = (set, cur, on, cols) => <div style={{display:'grid',gridTemplateColumns:'repeat(' + cols + ',minmax(0,1fr))',gap:6,maxWidth:330,margin:'0 auto 6px'}}>
    {set.map(k => <button key={k} className={'chip' + (cur === k ? ' active' : '')} aria-pressed={cur === k} style={{...KF_BTN,minHeight:40,padding:'0 4px'}} onClick={() => on(k)}>{prettyNote(k)}</button>)}
  </div>;
  let body;
  if (view === 'all') {
    const K = scIdx('C'), N = scNames('C'), marks = {}, names = {}; K.forEach((k, j) => { marks[k] = 'pass'; names[k] = N[j]; });
    body = <>
      <div style={scS.title}>{title}</div>
      <div style={scS.line}>{t('One pattern, T T S T T T S. Start it on any of the twelve notes.', '패턴은 하나, T T S T T T S. 열두 음 어디서든 시작할 수 있어요.')}</div>
      <ScKeys ks={K} marks={marks} names={names} arcs={ST.map((_, j) => mv(K, j, false))} nonce="all"/>
      <ScPills/>
      {scRow(<button className="ghost-btn" style={scS.prim} onClick={() => { setView('one'); setI(0); setKk('C'); setNonce(n => n + 1); }}>{t('One by one →', '하나씩 →')}</button>)}
    </>;
  } else if (view === 'one') {
    const E = SC_ALLSTEPS[i], K = scIdx(kk), N = scNames(kk), marks = {}, names = {};
    K.forEach((k, j) => { marks[k] = j === 7 ? 'pick' : 'pass'; names[k] = N[j]; });
    const pickK = (k) => { clear(); setKk(k); setNonce(n => n + 1); playKey(SCALES[k].rootPc, 0.5); };
    body = <>
      <div style={scS.title}>{title}</div>
      {chips(E.set, kk, pickK, E.set.length === 7 ? 7 : E.set.length === 5 ? 5 : 6)}
      <div style={scS.line}>{kk && E.set.includes(kk) ? t(N[0] + ' major: T T S T T T S.', N[0] + ' 장음계: T T S T T T S.') : t(E.text[0], E.text[1])}</div>
      <ScKeys ks={K} marks={marks} names={names} arcs={ST.map((_, j) => mv(K, j, false))} nonce={nonce + ':' + i + kk}/>
      <ScPills/>
      {scRow(<>
        <button className="ghost-btn" style={scS.back} onClick={() => { clear(); if (i === 0) setView('all'); else { const p = SC_ALLSTEPS[i - 1]; setI(i - 1); setKk(p.set[0]); setNonce(n => n + 1); } }}>{t('← Back', '← 이전')}</button>
        <button className="ghost-btn" style={scS.prim} onClick={() => { clear(); if (i === SC_ALLSTEPS.length - 1) { setView('try'); setTk('Eb'); setAt(0); setBad(null); setNonce(n => n + 1); } else { const nx = SC_ALLSTEPS[i + 1]; setI(i + 1); setKk(nx.set[0]); setNonce(n => n + 1); } }}>{i === SC_ALLSTEPS.length - 1 ? t('Your turn →', '내가 해보기 →') : t('Next →', '다음 →')}</button>
      </>)}
      <div style={{...scS.line,minHeight:0,marginTop:10,fontWeight:700,fontSize:13}}>{t(E.text[0], E.text[1])}</div>
    </>;
  } else {
    const K = scIdx(tk), N = scNames(tk), done = at >= 7, marks = {}, names = {}, arcs = [];
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
      <div style={scS.title}>{t('Your turn', '내가 해보기')}</div>
      {chips(SC_12, tk, (k) => { clear(); setTk(k); setAt(0); setBad(null); setNonce(n => n + 1); playKey(SCALES[k].rootPc, 0.5); }, 6)}
      <div style={scS.line}>{line}</div>
      <ScKeys ks={K} marks={at === 0 ? { ...marks, [K[0]]: 'pick' } : marks} names={names} arcs={arcs} nonce={nonce + tk} onTap={tap}/>
      <ScPills upTo={at} cur={at - 1}/>
      {scRow(<>
        <button className="ghost-btn" style={scS.back} onClick={() => { clear(); setView('one'); setI(SC_ALLSTEPS.length - 1); setKk('C'); setNonce(n => n + 1); }}>{t('← Back', '← 이전')}</button>
        {done && <button className="ghost-btn" style={scS.prim} onClick={() => { setAt(0); setBad(null); setNonce(n => n + 1); }}>{t('Again', '다시 하기')}</button>}
      </>)}
    </>;
  }
  return scBox('all12', body);
}
"""
a="\n// lesson 5: the natural."
rep(a, NEW + a)
rep(" ['sc-both', 'Both hands together', '양손 같이', 'One column per note: right hand above, left hand below.', '한 칸에 음 하나: 위는 오른손, 아래는 왼손.', ScBoth]]",
    " ['sc-both', 'Both hands together', '양손 같이', 'One column per note: right hand above, left hand below.', '한 칸에 음 하나: 위는 오른손, 아래는 왼손.', ScBoth],\n ['sc-all', 'All twelve keys', '12개 조 모두', 'One pattern, twelve start notes.', '패턴 하나, 시작 음 열두 개.', ScAll]]")
rep("'sc-bl', 'sc-both'], check: 'scales'","'sc-bl', 'sc-both', 'sc-all'], check: 'scales'")
open(sys.argv[2],'w',encoding='utf-8').write(s)
