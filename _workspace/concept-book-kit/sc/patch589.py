import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
NEW = r"""
// ─── Phase 584 (her order, 2026-10-20): Scales, lessons 10 and 11. Her material only: ChromaticScale (CHROM_UP / CHROM_DOWN / chromFinger) and MinorFormsCard / MINOR_FORMS / STEP_PATTERNS.
const scColOf = (sz) => sz === 2 ? '#26296b' : '#c0431f';
function ScPillRow({ st, upTo, cur }) {
  const n = st.length;
  return <div style={{display:'grid',gridTemplateColumns:'repeat(' + n + ',minmax(0,1fr))',gap:n > 7 ? 3 : 5,maxWidth:330,margin:'10px auto 0'}}>
    {st.map((sz, i) => { const on = i < upTo, wide = sz === 3, half = sz === 1, c = scColOf(sz);
      return <div key={i} style={{height:34,borderRadius:9,display:'flex',alignItems:'center',justifyContent:'center',fontWeight:900,fontSize:n > 7 ? 12 : wide ? 12 : 16,
        background: !on ? 'transparent' : (half || wide) ? '#fbe3da' : '#e6e7f1', color: !on ? 'rgba(38,41,107,0.25)' : c,
        border:'1.5px solid ' + (i === cur ? c : on ? ((half || wide) ? '#e4572e' : 'rgba(38,41,107,0.25)') : 'rgba(38,41,107,0.14)'), boxShadow: i === cur ? '0 0 0 2px ' + c + '33' : 'none'}}>{on ? (wide ? 'T+S' : half ? 'S' : 'T') : ''}</div>; })}
  </div>;
}
// lesson 10: the chromatic scale
const SC_CH = [
  { text: ['Every key, black and white, one half step at a time: twelve steps from C up to the next C.', '검은건반, 흰건반 가리지 않고 모든 건반을 반음씩 가요. C에서 다음 C까지 열두 걸음이에요.'], mode: 'up' },
  { text: ['Going up, the black keys are written with sharps: C, C♯, D, D♯ …', '올라갈 때 검은건반은 샤프로 적어요: C, C♯, D, D♯ …'], mode: 'up' },
  { text: ['Coming down, the same black keys are written with flats: C, B, B♭, A …', '내려올 때는 같은 검은건반을 플랫으로 적어요: C, B, B♭, A …'], mode: 'down' },
  { text: ['Right hand: finger 3 on every black key, the thumb on the white keys, finger 2 on F and C (the upper key of two white keys side by side).', '오른손: 검은건반은 모두 3번, 흰건반은 엄지, 붙어 있는 흰건반 두 개 중 위쪽인 F와 C는 2번.'], mode: 'RH' },
  { text: ['Left hand: finger 3 on every black key, the thumb on the white keys, finger 2 on E and B.', '왼손: 검은건반은 모두 3번, 흰건반은 엄지, E와 B는 2번.'], mode: 'LH' },
];
function ScChrom() {
  const [view, setView] = useState('all');   // 'all' -> 'one' -> 'try'
  const [i, setI] = useState(0), [nonce, setNonce] = useState(0), [st0, setSt0] = useState(0), [at, setAt] = useState(0), [bad, setBad] = useState(null);
  const timers = useRef([]);
  const clear = () => { timers.current.forEach(clearTimeout); timers.current = []; };
  useEffect(() => clear, []);
  const title = t('The chromatic scale', '반음계');
  const ST = Array(12).fill(1), mv = (K, j, anim) => [K[j], K[j + 1], anim, '#c0431f'];
  const K0 = Array.from({ length: 13 }, (_, j) => j);
  let body;
  if (view === 'all') {
    const marks = {}, names = {}; K0.forEach(k => { marks[k] = 'pass'; });
    body = <>
      <div style={scS.title}>{title}</div>
      <div style={scS.line}>{t(SC_CH[0].text[0], SC_CH[0].text[1])}</div>
      <ScKeys ks={K0} marks={marks} names={names} arcs={ST.map((_, j) => mv(K0, j, false))} nonce="all"/>
      <ScPillRow st={ST} upTo={12}/>
      {scRow(<button className="ghost-btn" style={scS.prim} onClick={() => { setView('one'); setI(1); setNonce(n => n + 1); }}>{t('One by one →', '하나씩 →')}</button>)}
    </>;
  } else if (view === 'one') {
    const E = SC_CH[i], marks = {}, names = {}; let K = K0.slice();
    if (E.mode === 'down') K = K0.slice().reverse();
    K.forEach((k, j) => { marks[k] = 'pass'; });
    if (E.mode === 'up') K.forEach(k => { names[k] = CHROM_UP[k % 12]; });
    else if (E.mode === 'down') K.forEach(k => { names[k] = CHROM_DOWN[k % 12]; });
    else K.forEach((k, j) => { names[k] = String(chromFinger(k % 12, E.mode, j === 0)); });
    const nums = E.mode === 'RH' || E.mode === 'LH';
    const arcs = E.mode === 'down' ? K.slice(0, 12).map((k, j) => [K[j], K[j + 1], false, '#c0431f']) : nums ? [] : K.slice(0, 12).map((k, j) => [K[j], K[j + 1], false, '#c0431f']);
    body = <>
      <div style={scS.title}>{title}</div>
      <div style={scS.line}>{t(E.text[0], E.text[1])}</div>
      <ScKeys nums={nums} ks={K0} marks={marks} names={names} arcs={arcs} nonce={nonce + ':' + i}/>
      {scRow(<>
        <button className="ghost-btn" style={scS.back} onClick={() => { clear(); if (i === 1) setView('all'); else { setI(i - 1); setNonce(n => n + 1); } }}>{t('← Back', '← 이전')}</button>
        <button className="ghost-btn" style={scS.prim} onClick={() => { clear(); if (i === SC_CH.length - 1) { setView('try'); setAt(0); setBad(null); setNonce(n => n + 1); } else { setI(i + 1); setNonce(n => n + 1); } }}>{i === SC_CH.length - 1 ? t('Your turn →', '내가 해보기 →') : t('Next →', '다음 →')}</button>
      </>)}
    </>;
  } else {
    const K = Array.from({ length: 13 }, (_, j) => st0 + j), done = at >= 12, marks = {}, names = {}, arcs = [];
    for (let j = 0; j <= at; j++) { marks[K[j]] = j === at && !done ? 'pick' : 'pass'; names[K[j]] = CHROM_UP[K[j] % 12]; }
    for (let j = 0; j < at; j++) arcs.push(mv(K, j, j === at - 1));
    if (bad != null) marks[bad] = 'bad';
    const nm = (k) => CHROM_UP[k % 12];
    const line = done ? t('That is the chromatic scale from ' + nm(K[0]) + ': twelve half steps.', nm(K[0]) + '에서 시작하는 반음계예요. 반음 열두 걸음이에요.')
      : bad != null ? t('Not that key. From ' + nm(K[at]) + ', tap the very next key, black or white.', '그 건반이 아니에요. ' + nm(K[at]) + '에서 바로 옆 건반을 눌러요. 검은건반이든 흰건반이든요.')
      : at === 0 ? t('Start on ' + nm(K[0]) + '. Then tap the very next key.', nm(K[0]) + '에서 시작해요. 그다음 바로 옆 건반을 눌러요.')
      : t('From ' + nm(K[at]) + ', tap the very next key. (' + at + '/12)', nm(K[at]) + '에서 바로 옆 건반을 눌러요. (' + at + '/12)');
    const tap = (k) => { if (done) return; clear(); if (k === K[at + 1]) { setBad(null); setAt(at + 1); setNonce(n => n + 1); playKey(K[at], 0.3); timers.current.push(setTimeout(() => playKey(k, 0.5), 350)); }
      else { setBad(k); playKey(k, 0.4); timers.current.push(setTimeout(() => setBad(null), 1100)); } };
    body = <>
      <div style={scS.title}>{t('Your turn', '내가 해보기')}</div>
      <div style={{display:'grid',gridTemplateColumns:'repeat(6,minmax(0,1fr))',gap:5,maxWidth:330,margin:'0 auto 6px'}}>
        {[0, 2, 4, 5, 7, 9].map(p => <button key={p} className={'chip' + (st0 === p ? ' active' : '')} aria-pressed={st0 === p} style={{...KF_BTN,minHeight:38,padding:'0 2px',fontSize:14}} onClick={() => { clear(); setSt0(p); setAt(0); setBad(null); setNonce(n => n + 1); playKey(p, 0.5); }}>{CHROM_UP[p]}</button>)}
      </div>
      <div style={scS.line}>{line}</div>
      <ScKeys ks={K} marks={at === 0 ? { ...marks, [K[0]]: 'pick' } : marks} names={names} arcs={arcs} nonce={nonce + st0} onTap={tap}/>
      <ScPillRow st={ST} upTo={at} cur={at - 1}/>
      {scRow(<>
        <button className="ghost-btn" style={scS.back} onClick={() => { clear(); setView('one'); setI(SC_CH.length - 1); setNonce(n => n + 1); }}>{t('← Back', '← 이전')}</button>
        {done && <button className="ghost-btn" style={scS.prim} onClick={() => { setAt(0); setBad(null); setNonce(n => n + 1); }}>{t('Again', '다시 하기')}</button>}
      </>)}
    </>;
  }
  return scBox('chrom', body);
}
// lesson 11: three kinds of minor, shown on A minor (her card: no key signature, so every change is easy to see)
const SC_MF = ['natural', 'harmonic', 'melodic'];
const scMinSteps = (f) => { const s = MINOR_FORMS[f].steps.concat([12]); return s.slice(1).map((v, j) => v - s[j]); };
function ScMinor() {
  const [view, setView] = useState('all');   // 'all' -> 'one' -> 'try'
  const [i, setI] = useState(0), [nonce, setNonce] = useState(0), [fm, setFm] = useState('harmonic'), [at, setAt] = useState(0), [bad, setBad] = useState(null);
  const timers = useRef([]);
  const clear = () => { timers.current.forEach(clearTimeout); timers.current = []; };
  useEffect(() => clear, []);
  const title = t('Three kinds of minor', '세 가지 단음계');
  const TXT = {
    natural: ['Natural minor: the same notes as its relative major. A minor uses C major’s white keys, starting on A.', '자연 단음계: 나란한조인 장조와 음이 똑같아요. A 단조는 C 장조의 흰건반을 그대로 쓰고, A에서 시작해요.'],
    harmonic: ['Harmonic minor, the one you’ll play most: raise the 7th note a semitone, going up and coming down. G becomes G♯.', '화성 단음계, 가장 많이 치게 될 단음계: 7번째 음을 반음 올려요, 올라갈 때도 내려올 때도. G가 G♯이 돼요.'],
    melodic: ['Melodic minor: going up, raise the 6th and 7th (F♯ and G♯). Coming down, play the natural minor.', '가락 단음계: 올라갈 때는 6음과 7음(F♯과 G♯)을 올려요. 내려올 때는 자연 단음계를 쳐요.'],
  };
  const mk = (f) => { const stp = MINOR_FORMS[f].steps, K = stp.map(x => 9 + x).concat([21]), N = spellMinor('A', f).map(prettyAny).concat(['A']), marks = {}, names = {};
    K.forEach((k, j) => { marks[k] = (f === 'harmonic' && j === 6) || (f === 'melodic' && (j === 5 || j === 6)) ? 'target' : 'pass'; names[k] = N[j]; }); return { K, N, marks, names, ST: scMinSteps(f) }; };
  const mvK = (K, ST, j, anim) => [K[j], K[j + 1], anim, scColOf(ST[j])];
  let body;
  if (view === 'all') {
    body = <>
      <div style={scS.title}>{title}</div>
      <div style={scS.line}>{t('All three start on A. They differ in only one or two notes near the top.', '셋 모두 A에서 시작해요. 위쪽 한두 음만 달라요.')}</div>
      <div style={{display:'grid',gap:10,maxWidth:330,margin:'0 auto'}}>
        {SC_MF.map(f => { const M = mk(f); return <div key={f}><div style={{fontSize:12,fontWeight:800,color:'#6d6f9c',marginBottom:3}}>{MINOR_FORMS[f].label}</div><ScPillRow st={M.ST} upTo={7}/></div>; })}
      </div>
      {scRow(<button className="ghost-btn" style={scS.prim} onClick={() => { setView('one'); setI(0); setNonce(n => n + 1); }}>{t('One by one →', '하나씩 →')}</button>)}
    </>;
  } else if (view === 'one') {
    const f = SC_MF[i], M = mk(f);
    body = <>
      <div style={scS.title}>{title}</div>
      <div style={scS.line}>{t(TXT[f][0], TXT[f][1])}</div>
      <ScKeys ks={M.K} marks={M.marks} names={M.names} arcs={M.ST.map((_, j) => mvK(M.K, M.ST, j, false))} nonce={nonce + ':' + i}/>
      <ScPillRow st={M.ST} upTo={7}/>
      {scRow(<>
        <button className="ghost-btn" style={scS.back} onClick={() => { clear(); if (i === 0) setView('all'); else { setI(i - 1); setNonce(n => n + 1); } }}>{t('← Back', '← 이전')}</button>
        <button className="ghost-btn" style={scS.prim} onClick={() => { clear(); if (i === 2) { setView('try'); setAt(0); setBad(null); setNonce(n => n + 1); } else { setI(i + 1); setNonce(n => n + 1); } }}>{i === 2 ? t('Your turn →', '내가 해보기 →') : t('Next →', '다음 →')}</button>
      </>)}
    </>;
  } else {
    const M = mk(fm), K = M.K, ST = M.ST, done = at >= 7, marks = {}, names = {}, arcs = [];
    for (let j = 0; j <= at; j++) { marks[K[j]] = j === at && !done ? 'pick' : M.marks[K[j]] === 'target' ? 'target' : 'pass'; names[K[j]] = M.N[j]; }
    for (let j = 0; j < at; j++) arcs.push(mvK(K, ST, j, j === at - 1));
    if (bad != null) marks[bad] = 'bad';
    const word = (sz) => sz === 1 ? t('a half step up (S)', '반음 위로 (S)') : sz === 2 ? t('a whole step up (T)', '온음 위로 (T)') : t('a tone and a semitone up (T+S)', '온음에 반음을 더해 위로 (T+S)');
    const fl = MINOR_FORMS[fm].label;
    const line = done ? t('That is A ' + fl.toLowerCase() + ' minor.', 'A ' + fl + ' 단음계예요.')
      : bad != null ? t('Not that key. From ' + M.N[at] + ', go ' + word(ST[at]) + '.', '그 건반이 아니에요. ' + M.N[at] + '에서 ' + word(ST[at]) + ' 가요.')
      : at === 0 ? t('Start on A. Then tap ' + word(ST[0]) + '.', 'A에서 시작해요. 그다음 ' + word(ST[0]) + ' 건반을 눌러요.')
      : t('From ' + M.N[at] + ', tap ' + word(ST[at]) + '.', M.N[at] + '에서 ' + word(ST[at]) + ' 건반을 눌러요.');
    const tap = (k) => { if (done) return; clear(); if (k === K[at + 1]) { setBad(null); setAt(at + 1); setNonce(n => n + 1); playKey(K[at], 0.35); timers.current.push(setTimeout(() => playKey(k, 0.6), 400)); }
      else { setBad(k); playKey(k, 0.4); timers.current.push(setTimeout(() => setBad(null), 1100)); } };
    body = <>
      <div style={scS.title}>{t('Your turn', '내가 해보기')}</div>
      <div style={{display:'grid',gridTemplateColumns:'repeat(3,minmax(0,1fr))',gap:6,maxWidth:330,margin:'0 auto 6px'}}>
        {SC_MF.map(f => <button key={f} className={'chip' + (fm === f ? ' active' : '')} aria-pressed={fm === f} style={{...KF_BTN,minHeight:40,padding:'0 4px'}} onClick={() => { clear(); setFm(f); setAt(0); setBad(null); setNonce(n => n + 1); playKey(9, 0.5); }}>{MINOR_FORMS[f].label}</button>)}
      </div>
      <div style={scS.line}>{line}</div>
      <ScKeys ks={K} marks={at === 0 ? { ...marks, [K[0]]: 'pick' } : marks} names={names} arcs={arcs} nonce={nonce + fm} onTap={tap}/>
      <ScPillRow st={ST} upTo={at} cur={at - 1}/>
      {scRow(<>
        <button className="ghost-btn" style={scS.back} onClick={() => { clear(); setView('one'); setI(2); setNonce(n => n + 1); }}>{t('← Back', '← 이전')}</button>
        {done && <button className="ghost-btn" style={scS.prim} onClick={() => { setAt(0); setBad(null); setNonce(n => n + 1); }}>{t('Again', '다시 하기')}</button>}
      </>)}
    </>;
  }
  return scBox('minor3', body);
}
"""
a="\n// lesson 5: the natural."
rep(a, NEW + a)
rep(" ['sc-all', 'All twelve keys', '12개 조 모두', 'One pattern, twelve start notes.', '패턴 하나, 시작 음 열두 개.', ScAll]]",
    " ['sc-all', 'All twelve keys', '12개 조 모두', 'One pattern, twelve start notes.', '패턴 하나, 시작 음 열두 개.', ScAll],\n ['sc-chrom', 'The chromatic scale', '반음계', 'Every key, one half step at a time.', '모든 건반을 반음씩.', ScChrom],\n ['sc-min', 'Three kinds of minor', '세 가지 단음계', 'Natural, harmonic and melodic, shown on A.', 'A에서 보는 자연, 화성, 가락.', ScMinor]]")
rep("'sc-bl', 'sc-both', 'sc-all'], check: 'scales'","'sc-bl', 'sc-both', 'sc-all', 'sc-chrom', 'sc-min'], check: 'scales'")
open(sys.argv[2],'w',encoding='utf-8').write(s)
