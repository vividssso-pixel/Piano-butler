import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
a = s.index("// ─── Phase 577 (her call, 2026-10-20): lessons 4 and 5 are one lesson."); b = s.index("\n// lesson 5: the natural.")
NEW = r"""// ─── Phase 578 (her call, 2026-10-20 12:32): one hand per lesson. 4 white keys, right hand; 5 white keys, left hand; 6 black keys, right hand; 7 black keys, left hand; 8 both hands.
const scS = {
  title: {textAlign:'center',fontFamily:"'Playfair Display', Georgia, serif",fontSize:22,fontWeight:900,color:'#26296b',lineHeight:1.2,margin:'0 0 8px',textWrap:'balance'},
  line: {textAlign:'center',fontSize:15,fontWeight:800,color:'#26296b',margin:'8px 0 6px',minHeight:42,textWrap:'balance',wordBreak:'keep-all'},
  prim: {...KF_BTN,minWidth:140,background:'#26296b',color:'#fffefa',borderColor:'#26296b'},
  back: {...KF_BTN,minWidth:110},
};
const scRow = (children) => <div style={{textAlign:'center',marginTop:14,display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap'}}>{children}</div>;
const scBox = (kind, body) => <div className="try-box" data-sc-lesson={kind} style={{background:'#fff',border:'1px solid var(--border)',borderRadius:10,padding:'10px 10px 12px',margin:'4px 0 16px'}}>{body}</div>;
const scPaintKey = (key, hand, upto = 8) => { const K = scIdx(key), marks = {}, names = {}, ncol = {}; scPaint(key, hand, K, upto, marks, names, ncol); return { K, marks, names, ncol }; };
const scHandWord = (h) => h === 'RH' ? t('Right hand. ', '오른손. ') : t('Left hand. ', '왼손. ');
// white-key starts: the standard shape one hand at a time, one strip of that hand for every white key, then "standard or different?"
function ScWhite({ hand }) {
  const RHd = hand === 'RH', steps = SC_FSTEPS.filter(e => e.hand === hand), odd = RHd ? 'F' : 'B';
  const [view, setView] = useState('all');   // 'all' -> 'one' -> 'cmp' -> 'try'
  const [i, setI] = useState(0), [nonce, setNonce] = useState(0);
  const [seq, setSeq] = useState([]), [at, setAt] = useState(0), [given, setGiven] = useState(null), [score, setScore] = useState(0);
  const title = RHd ? t('White keys: right hand', '흰건반에서 시작: 오른손') : t('White keys: left hand', '흰건반에서 시작: 왼손');
  const last = steps.length - 1, N5 = 5;
  const newRound = () => { const rest = shuffle(['C', 'G', 'D', 'A', 'E', RHd ? 'B' : 'F']).slice(0, N5 - 1); setSeq(shuffle([odd, ...rest])); setAt(0); setGiven(null); setScore(0); setNonce(n => n + 1); };
  let body;
  if (view === 'all') {
    const P = scPaintKey('C', hand);
    body = <>
      <div style={scS.title}>{title}</div>
      <div style={scS.line}>{RHd ? t('A group of 3 (coral) and a group of 4 (blue). The thumb is circled.', '3개 묶음(산호색)과 4개 묶음(파란색). 엄지에 동그라미를 쳤어요.') : t('The mirror of the right hand: 5 at the bottom, then a group of 4 (blue), then a group of 3 (coral).', '오른손의 거울이에요: 맨 아래 5번, 그다음 4개 묶음(파란색), 그다음 3개 묶음(산호색).')}</div>
      <ScKeys nums ks={P.K} marks={P.marks} names={P.names} ncol={P.ncol} arcs={[]} nonce="all"/>
      {scRow(<button className="ghost-btn" style={scS.prim} onClick={() => { setView('one'); setI(0); setNonce(n => n + 1); }}>{t('One by one →', '하나씩 →')}</button>)}
    </>;
  } else if (view === 'one') {
    const E = steps[i], P = scPaintKey('C', hand, E.n);
    body = <>
      <div style={scS.title}>{title}</div>
      <div style={scS.line}>{t(E.text[0], E.text[1])}</div>
      <ScKeys nums ks={P.K} marks={P.marks} names={P.names} ncol={P.ncol} arcs={[]} nonce={nonce + ':' + i}/>
      {scRow(<>
        <button className="ghost-btn" style={scS.back} onClick={() => { if (i === 0) setView('all'); else { setI(i - 1); setNonce(n => n + 1); } }}>{t('← Back', '← 이전')}</button>
        <button className="ghost-btn" style={scS.prim} onClick={() => { if (i === last) { setView('cmp'); setNonce(n => n + 1); } else { setI(i + 1); setNonce(n => n + 1); } }}>{t('Next →', '다음 →')}</button>
      </>)}
    </>;
  } else if (view === 'cmp') {
    body = <>
      <div style={scS.title}>{title}</div>
      <div style={scS.line}>{RHd ? t('C, G, D, A, E and B share one fingering. Only F is different (≠).', 'C, G, D, A, E, B는 운지가 같아요. F만 달라요(≠).') : t('C, G, D, A, E and F share one fingering. Only B is different (≠).', 'C, G, D, A, E, F는 운지가 같아요. B만 달라요(≠).')}</div>
      <ScStrip rows={[{ keys: 'C G D A E', key: 'C', hand }, { keys: RHd ? 'B' : 'F', key: RHd ? 'B' : 'F', hand }, { keys: RHd ? 'F' : 'B', key: RHd ? 'F' : 'B', hand, odd: true }]}/>
      {scRow(<>
        <button className="ghost-btn" style={scS.back} onClick={() => { setView('one'); setI(last); setNonce(n => n + 1); }}>{t('← Back', '← 이전')}</button>
        <button className="ghost-btn" style={scS.prim} onClick={() => { setView('try'); newRound(); }}>{t('Your turn →', '내가 해보기 →')}</button>
      </>)}
    </>;
  } else {
    const done = at >= seq.length, ck = done ? 'C' : seq[at], isOdd = ck === odd, P = scPaintKey(ck, hand), N = scNames(ck);
    const handWord = RHd ? t('right hand', '오른손') : t('left hand', '왼손'), handKo = RHd ? '오른손' : '왼손';
    const answer = (v) => { if (given != null || done) return; setGiven(v); if ((v === 'odd') === isOdd) setScore(x => x + 1); setNonce(n => n + 1); };
    const line = done ? t('Only one is different: the ' + handWord + ' of ' + odd + '. You got ' + score + ' of ' + seq.length + '.', '다른 건 하나뿐이에요: ' + odd + '의 ' + handKo + '. ' + seq.length + '개 중 ' + score + '개 맞았어요.')
      : given == null ? t('The ' + handWord + ' of ' + N[0] + ' major: the standard shape, or different? (' + (at + 1) + '/' + seq.length + ')', N[0] + ' 장음계 ' + handKo + ': 기본 모양일까요, 다를까요? (' + (at + 1) + '/' + seq.length + ')')
      : ((given === 'odd') === isOdd ? t('Yes. ', '맞아요. ') : t('Not quite. ', '아니에요. ')) + (isOdd ? t('It is different.', '달라요.') : t('It is the standard shape.', '기본 모양이에요.'));
    body = <>
      <div style={scS.title}>{t('Your turn', '내가 해보기')}</div>
      <div style={scS.line}>{line}</div>
      {!done && <ScKeys nums ks={P.K} marks={given != null ? P.marks : { [P.K[0]]: 'pick' }} names={given != null ? P.names : {}} ncol={P.ncol} arcs={[]} nonce={nonce + ck}/>}
      {!done && given == null && <div style={{display:'grid',gridTemplateColumns:'repeat(2,minmax(0,1fr))',gap:8,maxWidth:330,margin:'12px auto 0'}}>
        <button className="ghost-btn" style={{...KF_BTN,minHeight:48}} onClick={() => answer('std')}>{t('Standard', '기본 모양')}</button>
        <button className="ghost-btn" style={{...KF_BTN,minHeight:48}} onClick={() => answer('odd')}>{t('Different', '달라요')}</button>
      </div>}
      {scRow(<>
        <button className="ghost-btn" style={scS.back} onClick={() => { setView('cmp'); setNonce(n => n + 1); }}>{t('← Back', '← 이전')}</button>
        {given != null && !done && <button className="ghost-btn" style={scS.prim} onClick={() => { setAt(at + 1); setGiven(null); setNonce(n => n + 1); }}>{t('Next →', '다음 →')}</button>}
        {done && <button className="ghost-btn" style={scS.prim} onClick={() => newRound()}>{t('Again', '다시 하기')}</button>}
      </>)}
    </>;
  }
  return scBox('white' + hand, body);
}
// black-key starts. Her text (SCALE_PATTERNS, SCALES comments): the right hand always starts on finger 2 and the first white key you reach gets the thumb;
// in B♭ E♭ A♭ D♭ the right-hand thumbs go on C and F; the left hand is one shape for all four, starting on 3: 3-2-1, 4-3-2-1, 3; G♭ / F♯: three black keys in a row, fingers 2-3-4, both thumbs on C♭ (B) and F.
const SC_BR = [
  { key: 'Bb', text: ['B♭ major starts on a black key. The right hand always starts on finger 2, and the thumb goes on the first white key: C.', 'B♭ 장음계는 검은건반에서 시작해요. 오른손은 늘 2번으로 시작하고, 엄지는 처음 닿는 흰건반 C에 가요.'] },
  { key: 'Eb', text: ['E♭: start on finger 2. The first white key is F: the thumb goes there.', 'E♭: 2번으로 시작해요. 처음 닿는 흰건반은 F: 엄지가 거기 가요.'] },
  { key: 'Ab', text: ['A♭: start on finger 2. The first white key is C: the thumb goes there.', 'A♭: 2번으로 시작해요. 처음 닿는 흰건반은 C: 엄지가 거기 가요.'] },
  { key: 'Db', text: ['D♭: start on finger 2. The first white key is F. In all four keys the right-hand thumbs go on C and F.', 'D♭: 2번으로 시작해요. 처음 닿는 흰건반은 F. 네 조 모두 오른손 엄지는 C와 F에 가요.'] },
  { key: 'Gb', text: ['G♭ / F♯: three black keys in a row. Fingers 2, 3, 4 cover them; the thumb lands on the first white key, C♭ (B).', 'G♭ / F♯: 나란히 있는 검은건반 세 개. 2, 3, 4번이 그 셋을 맡고, 엄지는 처음 닿는 흰건반 C♭(B)에 놓여요.'] },
];
const SC_BL = [
  { key: 'Bb', text: ['B♭, E♭, A♭, D♭: the left hand starts on finger 3 and is one shape for all four: 3-2-1, 4-3-2-1, 3.', 'B♭, E♭, A♭, D♭: 왼손은 3번으로 시작하고 네 조 모두 한 가지 모양이에요: 3-2-1, 4-3-2-1, 3.'] },
  { key: 'Gb', text: ['G♭ / F♯: three black keys in a row. Fingers 2, 3, 4 cover them; both thumbs land on the only two white keys, C♭ (B) and F.', 'G♭ / F♯: 나란히 있는 검은건반 세 개. 2, 3, 4번이 그 셋을 맡고, 양손 엄지는 단 두 개뿐인 흰건반 C♭(B)과 F에 놓여요.'] },
];
function ScBlackHand({ hand }) {
  const RHd = hand === 'RH', STEPS = RHd ? SC_BR : SC_BL;
  const [view, setView] = useState('all');   // 'all' (the strips) -> 'one' -> 'try'
  const [i, setI] = useState(0), [nonce, setNonce] = useState(0), [kk, setKk] = useState('Bb');
  const [found, setFound] = useState([]), [bad, setBad] = useState(null), [why, setWhy] = useState('');
  const timers = useRef([]);
  const clear = () => { timers.current.forEach(clearTimeout); timers.current = []; };
  useEffect(() => clear, []);
  const title = RHd ? t('Black keys: right hand', '검은건반에서 시작: 오른손') : t('Black keys: left hand', '검은건반에서 시작: 왼손');
  const reset = () => { setFound([]); setBad(null); setWhy(''); setNonce(n => n + 1); };
  let body;
  if (view === 'all') {
    body = <>
      <div style={scS.title}>{title}</div>
      <div style={scS.line}>{RHd ? t('The same groups of 3 and 4, in another order. The right hand always starts on finger 2.', '같은 3개, 4개 묶음이 순서만 바뀌어요. 오른손은 늘 2번으로 시작해요.') : t('One shape for B♭, E♭, A♭ and D♭. The left hand starts on finger 3.', 'B♭, E♭, A♭, D♭는 한 가지 모양이에요. 왼손은 3번으로 시작해요.')}</div>
      <ScStrip rows={RHd ? [{ keys: 'B♭', key: 'Bb', hand }, { keys: 'E♭', key: 'Eb', hand }, { keys: 'A♭', key: 'Ab', hand }, { keys: 'D♭', key: 'Db', hand }, { keys: 'G♭', key: 'Gb', hand }] : [{ keys: 'B♭ E♭ A♭ D♭', key: 'Bb', hand }, { keys: 'G♭', key: 'Gb', hand }]}/>
      {scRow(<button className="ghost-btn" style={scS.prim} onClick={() => { setView('one'); setI(0); setNonce(n => n + 1); }}>{t('One by one →', '하나씩 →')}</button>)}
    </>;
  } else if (view === 'one') {
    const E = STEPS[i], P = scPaintKey(E.key, hand);
    body = <>
      <div style={scS.title}>{title}</div>
      <div style={scS.line}>{t(E.text[0], E.text[1])}</div>
      <ScKeys nums ks={P.K} marks={P.marks} names={P.names} ncol={P.ncol} arcs={[]} nonce={nonce + ':' + i}/>
      {scRow(<>
        <button className="ghost-btn" style={scS.back} onClick={() => { if (i === 0) setView('all'); else { setI(i - 1); setNonce(n => n + 1); } }}>{t('← Back', '← 이전')}</button>
        <button className="ghost-btn" style={scS.prim} onClick={() => { if (i === STEPS.length - 1) { setView('try'); reset(); } else { setI(i + 1); setNonce(n => n + 1); } }}>{i === STEPS.length - 1 ? t('Your turn →', '내가 해보기 →') : t('Next →', '다음 →')}</button>
      </>)}
    </>;
  } else {
    const K = scIdx(kk), F = SCALES[kk].octaves[1][hand], N = scNames(kk), thumbs = F.map((f, j) => f === 1 ? K[j] : null).filter(x => x != null);
    const done = found.length >= thumbs.length, P = scPaintKey(kk, hand), marks = {}, names = {}, ncol = {};
    if (done) Object.assign(marks, P.marks), Object.assign(names, P.names), Object.assign(ncol, P.ncol);
    found.forEach(k => { marks[k] = 'good'; names[k] = '1'; ncol[k] = '#2e8a6e'; });
    if (bad != null) marks[bad] = 'bad';
    const handWord = RHd ? t('right hand', '오른손') : t('left hand', '왼손'), handKo = RHd ? '오른손' : '왼손';
    const line = done ? t('Both thumbs found. Here is the whole fingering of ' + N[0] + ' major.', '엄지 둘을 다 찾았어요. ' + N[0] + ' 장음계의 운지 전체예요.')
      : bad != null ? why : t(N[0] + ' major, ' + handWord + ': tap the keys where the thumb goes. (' + found.length + '/' + thumbs.length + ')', N[0] + ' 장음계 ' + handKo + ': 엄지가 가는 건반을 눌러요. (' + found.length + '/' + thumbs.length + ')');
    const tap = (k) => { if (done || found.includes(k)) return; clear();
      if (thumbs.includes(k)) { setBad(null); setFound(f => [...f, k]); setNonce(n => n + 1); playKey(k, 0.6); }
      else { setBad(k); setWhy(PC_INFO[((k % 12) + 12) % 12].white ? t('Not a thumb key. The thumbs go on the white keys.', '엄지 건반이 아니에요. 엄지는 흰건반에 가요.') : t('The thumb only ever plays white keys.', '엄지는 흰건반만 쳐요.')); playKey(k, 0.4); timers.current.push(setTimeout(() => setBad(null), 1400)); } };
    body = <>
      <div style={scS.title}>{t('Your turn', '내가 해보기')}</div>
      <div style={{display:'grid',gridTemplateColumns:'repeat(5,minmax(0,1fr))',gap:6,maxWidth:330,margin:'0 auto 6px'}}>
        {['Bb', 'Eb', 'Ab', 'Db', 'Gb'].map(k => <button key={k} className={'chip' + (kk === k ? ' active' : '')} aria-pressed={kk === k} style={{...KF_BTN,minHeight:40,padding:'0 4px'}} onClick={() => { clear(); setKk(k); reset(); playKey(SCALES[k].rootPc, 0.5); }}>{prettyNote(k)}</button>)}
      </div>
      <div style={scS.line}>{line}</div>
      <ScKeys nums ks={K} marks={marks} names={names} ncol={ncol} arcs={[]} nonce={nonce + kk + hand} onTap={tap}/>
      {scRow(<>
        <button className="ghost-btn" style={scS.back} onClick={() => { clear(); setView('one'); setI(STEPS.length - 1); setNonce(n => n + 1); }}>{t('← Back', '← 이전')}</button>
        {done && <button className="ghost-btn" style={scS.prim} onClick={() => reset()}>{t('Again', '다시 하기')}</button>}
      </>)}
    </>;
  }
  return scBox('black' + hand, body);
}
// ─── Phase 578: lesson 8, both hands together. One column per note of the scale: the note's name, the right hand's finger above, the left hand's below,
// in the group colours. 1 octave for every key, 2 octaves from her data for every key, 4 octaves for the five standard keys (her unit, repeated). Her turn: the left hand's finger for a note.
const SC_STD5 = ['C', 'G', 'D', 'A', 'E'];
const scFingers = (key, hand, n) => { const e = SCALES[key] && SCALES[key].octaves[n]; if (e) return e[hand]; if (SC_STD5.includes(key)) return hand === 'RH' ? rhPattern(n) : lhPattern(n); return null; };
// split a finger list into groups: coral = 1 2 3 (RH) or 3 2 1 (LH), blue = 1 2 3 4 or 4 3 2 1, all else plain (5, a lone note, a part-group); F's last 4 is its own note
function scRuns(key, hand, F) {
  const n = F.length, units = []; let cur = [0];
  for (let j = 1; j < n; j++) { const reset = hand === 'RH' ? F[j] <= F[j - 1] : F[j] >= F[j - 1]; if (reset) { units.push(cur); cur = [j]; } else cur.push(j); }
  units.push(cur);
  const out = [];
  units.forEach(u => { let a = u.slice(), pre = [], post = [];
    if (hand === 'LH' && F[a[0]] === 5) pre = [a.shift()];
    if (hand === 'RH' && F[a[a.length - 1]] === 5) post = [a.pop()];
    if (key === 'F' && hand === 'RH' && a.length === 4 && a[3] === n - 1 && F[a[0]] === 1) post = [a.pop()];
    [pre, a, post].forEach(g => { if (g.length) { const f = g.map(j => F[j]).join(); const ok = hand === 'RH' ? (f === '1,2,3' || f === '1,2,3,4') : (f === '3,2,1' || f === '4,3,2,1'); out.push({ from: g[0], len: g.length, kind: ok ? (g.length === 3 ? 3 : 4) : 0 }); } }); });
  return out;
}
function ScPair({ keyName, n, hideLH }) {
  const FR = scFingers(keyName, 'RH', n), FL = scFingers(keyName, 'LH', n), cols = FR.length, base = spellScale(keyName).map(prettyNote), top = prettyNote(keyName);
  const names = FR.map((_, j) => j === cols - 1 ? top : base[j % 7]);
  const blk = (key, hand, F, hide) => scRuns(key, hand, F).map((g, q) => { const k = g.kind, bg = k === 3 ? '#fbe3da' : k === 4 ? '#dfe9f8' : '#efeadc', bd = k === 3 ? '#e4572e' : k === 4 ? '#3b4fa8' : '#d8cfb6', col = k === 3 ? SC_G3 : k === 4 ? SC_G4 : '#26296b';
    const shown = !hide || hide.slice(g.from, g.from + g.len).every(Boolean);
    return <div key={q} style={{gridColumn:(g.from + 2) + ' / span ' + g.len,height:30,borderRadius:7,background:shown ? bg : '#fff',border:'1.5px ' + (shown ? 'solid ' : 'dashed ') + (shown ? bd : '#d8cfb6'),color:col,display:'flex',alignItems:'center',justifyContent:'center',fontWeight:900,fontSize:13,letterSpacing:'0.02em',whiteSpace:'nowrap'}}>{shown ? F.slice(g.from, g.from + g.len).join(' ') : '?'}</div>; });
  const cw = cols > 8 ? 22 : 38;
  return <div style={{maxWidth:330,margin:'0 auto',overflowX:'auto'}}><div style={{display:'grid',gridTemplateColumns:'40px repeat(' + cols + ', ' + cw + 'px)',gap:2,rowGap:5,minWidth:'min-content',alignItems:'center'}}>
    <div/>{names.map((nm, j) => <div key={j} style={{textAlign:'center',fontWeight:900,fontSize:cols > 8 ? 11 : 13,color:'#26296b'}}>{nm}</div>)}
    <div style={{fontSize:11,fontWeight:800,color:'#6d6f9c',gridRow:2}}>{t('right', '오른손')}</div>{blk(keyName, 'RH', FR).map(el => React.cloneElement(el, { style: { ...el.props.style, gridRow: 2 } }))}
    <div style={{fontSize:11,fontWeight:800,color:'#6d6f9c',gridRow:3}}>{t('left', '왼손')}</div>{blk(keyName, 'LH', FL, hideLH).map(el => React.cloneElement(el, { style: { ...el.props.style, gridRow: 3 } }))}
  </div></div>;
}
function ScBoth() {
  const [view, setView] = useState('all');   // 'all' -> 'more' -> 'try'
  const [kk, setKk] = useState('C'), [oc, setOc] = useState(1), [nonce, setNonce] = useState(0);
  const [seq, setSeq] = useState([]), [at, setAt] = useState(0), [bad, setBad] = useState(null), [tk, setTk] = useState('C');
  const timers = useRef([]);
  const clear = () => { timers.current.forEach(clearTimeout); timers.current = []; };
  useEffect(() => clear, []);
  const title = t('Both hands together', '양손 같이');
  const KEYS = ['C', 'G', 'D', 'A', 'E', 'B', 'F', 'Bb', 'Eb', 'Ab', 'Db', 'Gb'];
  const newRound = (k) => { setTk(k); setSeq(shuffle([0, 1, 2, 3, 4, 5, 6, 7])); setAt(0); setBad(null); setNonce(n => n + 1); };
  let body;
  if (view === 'all') {
    body = <>
      <div style={scS.title}>{title}</div>
      <div style={scS.line}>{t('Each column is one note of the scale: the right hand’s finger on top, the left hand’s below.', '한 칸이 스케일의 음 하나예요. 위는 오른손, 아래는 왼손 손가락이에요.')}</div>
      <ScPair keyName="C" n={1}/>
      {scRow(<button className="ghost-btn" style={scS.prim} onClick={() => { setView('more'); setKk('C'); setOc(1); setNonce(n => n + 1); }}>{t('Other keys, more octaves →', '다른 조, 더 많은 옥타브 →')}</button>)}
    </>;
  } else if (view === 'more') {
    const ok = (k, n) => !!scFingers(k, 'RH', n) && !!scFingers(k, 'LH', n);
    body = <>
      <div style={scS.title}>{title}</div>
      <div style={{display:'grid',gridTemplateColumns:'repeat(6,minmax(0,1fr))',gap:5,maxWidth:330,margin:'0 auto 6px'}}>
        {KEYS.map(k => <button key={k} className={'chip' + (kk === k ? ' active' : '')} aria-pressed={kk === k} style={{...KF_BTN,minHeight:38,padding:'0 2px',fontSize:14}} onClick={() => { setKk(k); if (!ok(k, oc)) setOc(1); setNonce(n => n + 1); }}>{prettyNote(k)}</button>)}
      </div>
      <div style={{display:'grid',gridTemplateColumns:'repeat(3,minmax(0,1fr))',gap:6,maxWidth:330,margin:'0 auto 6px'}}>
        {[1, 2, 4].map(n => <button key={n} disabled={!ok(kk, n)} className={'chip' + (oc === n ? ' active' : '')} aria-pressed={oc === n} style={{...KF_BTN,minHeight:38,opacity:ok(kk, n) ? 1 : 0.35}} onClick={() => { setOc(n); setNonce(n2 => n2 + 1); }}>{n === 1 ? t('1 octave', '1옥타브') : n === 2 ? t('2 octaves', '2옥타브') : t('4 octaves', '4옥타브')}</button>)}
      </div>
      <div style={scS.line}>{oc === 4 ? t('Four octaves: the same groups, over and over.', '4옥타브: 같은 묶음이 계속 이어져요.') : t(prettyNote(kk) + ' major, ' + oc + (oc === 1 ? ' octave.' : ' octaves.'), prettyNote(kk) + ' 장음계, ' + oc + '옥타브.')}</div>
      <ScPair keyName={kk} n={oc}/>
      {scRow(<>
        <button className="ghost-btn" style={scS.back} onClick={() => { setView('all'); setNonce(n => n + 1); }}>{t('← Back', '← 이전')}</button>
        <button className="ghost-btn" style={scS.prim} onClick={() => { setView('try'); newRound(kk); }}>{t('Your turn →', '내가 해보기 →')}</button>
      </>)}
    </>;
  } else {
    const FR = SCALES[tk].octaves[1].RH, FL = SCALES[tk].octaves[1].LH, N = scNames(tk), done = at >= 8, j = done ? 0 : seq[at];
    const hide = Array.from({ length: 8 }, (_, c) => seq.slice(0, at).includes(c));
    const line = done ? t('All eight notes. That is the fingering of ' + N[0] + ' major, both hands.', '여덟 음을 다 했어요. ' + N[0] + ' 장음계 양손 운지예요.')
      : bad != null ? t('Not that finger. On ' + N[j] + ' the right hand plays ' + FR[j] + '. Which finger does the left hand play?', '그 손가락이 아니에요. ' + N[j] + '에서 오른손은 ' + FR[j] + '번이에요. 왼손은 몇 번일까요?')
      : t(N[0] + ' major, on ' + N[j] + ' the right hand plays finger ' + FR[j] + '. The left hand? (' + (at + 1) + '/8)', N[0] + ' 장음계, ' + N[j] + '에서 오른손은 ' + FR[j] + '번이에요. 왼손은? (' + (at + 1) + '/8)');
    const pick = (f) => { if (done) return; clear(); if (f === FL[j]) { setBad(null); setAt(at + 1); setNonce(n => n + 1); } else { setBad(f); timers.current.push(setTimeout(() => setBad(null), 1100)); } };
    body = <>
      <div style={scS.title}>{t('Your turn', '내가 해보기')}</div>
      <div style={{display:'grid',gridTemplateColumns:'repeat(6,minmax(0,1fr))',gap:5,maxWidth:330,margin:'0 auto 6px'}}>
        {KEYS.map(k => <button key={k} className={'chip' + (tk === k ? ' active' : '')} aria-pressed={tk === k} style={{...KF_BTN,minHeight:38,padding:'0 2px',fontSize:14}} onClick={() => { clear(); newRound(k); }}>{prettyNote(k)}</button>)}
      </div>
      <div style={scS.line}>{line}</div>
      <ScPair keyName={tk} n={1} hideLH={done ? null : hide}/>
      {!done && <div style={{display:'grid',gridTemplateColumns:'repeat(5,minmax(0,1fr))',gap:6,maxWidth:330,margin:'10px auto 0'}}>
        {[1, 2, 3, 4, 5].map(f => <button key={f} className="ghost-btn" style={{...KF_BTN,minHeight:48,fontSize:18,padding:0,...(bad === f ? {background:'#fbe3da',borderColor:'#e4572e',color:'#c0431f'} : {})}} onClick={() => pick(f)}>{f}</button>)}
      </div>}
      {scRow(<>
        <button className="ghost-btn" style={scS.back} onClick={() => { clear(); setView('more'); setNonce(n => n + 1); }}>{t('← Back', '← 이전')}</button>
        {done && <button className="ghost-btn" style={scS.prim} onClick={() => newRound(tk)}>{t('Again', '다시 하기')}</button>}
      </>)}
    </>;
  }
  return scBox('both', body);
}
"""
s = s[:a] + NEW + s[b:]
rep(""" ['sc-finger', 'Fingering from a white key', '흰건반에서 시작하는 운지', 'The standard shape, and the two hands that differ.', '기본 모양, 그리고 다른 두 손.', ScFinger],
 ['sc-black', 'Fingering from a black key', '검은건반에서 시작하는 운지', 'The same groups, another order. The thumb plays white keys.', '같은 묶음, 다른 순서. 엄지는 흰건반.', ScBlack]]""",
""" ['sc-wr', 'White keys: right hand', '흰건반에서 시작: 오른손', 'A group of 3, a group of 4, finger 5 on top.', '3개 묶음, 4개 묶음, 맨 위는 5번.', () => <ScWhite hand="RH"/>],
 ['sc-wl', 'White keys: left hand', '흰건반에서 시작: 왼손', 'The mirror of the right hand.', '오른손의 거울.', () => <ScWhite hand="LH"/>],
 ['sc-br', 'Black keys: right hand', '검은건반에서 시작: 오른손', 'Start on finger 2; the first white key gets the thumb.', '2번으로 시작, 처음 닿는 흰건반에 엄지.', () => <ScBlackHand hand="RH"/>],
 ['sc-bl', 'Black keys: left hand', '검은건반에서 시작: 왼손', 'One shape for B♭, E♭, A♭ and D♭.', 'B♭, E♭, A♭, D♭는 한 가지 모양.', () => <ScBlackHand hand="LH"/>],
 ['sc-both', 'Both hands together', '양손 같이', 'One column per note: right hand above, left hand below.', '한 칸에 음 하나: 위는 오른손, 아래는 왼손.', ScBoth]]""")
rep("C: () => <Comp/> });", "C: Comp });")
rep("lessons: ['sc-shape', 'sc-same', 'sc-deg', 'sc-finger', 'sc-black'], check: 'scales'", "lessons: ['sc-shape', 'sc-same', 'sc-deg', 'sc-wr', 'sc-wl', 'sc-br', 'sc-bl', 'sc-both'], check: 'scales'")
open(sys.argv[2],'w',encoding='utf-8').write(s)
