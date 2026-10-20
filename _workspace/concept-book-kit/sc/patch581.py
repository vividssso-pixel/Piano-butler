import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
rep("const scIdx = (key) => SC_OFF.map(o => SF12.indexOf(key) + o);", "const scIdx = (key) => SC_OFF.map(o => (SCALES[key] ? SCALES[key].rootPc : SF12.indexOf(key)) + o);")
# groups: a negative length is a plain group (finger numbers only, no colour); the black-key starts' shapes are hers (SCALE_PATTERNS, SCALES comments)
rep("const SC_LENS = { std: { RH: [3, 4, 1], LH: [1, 4, 3] }, F: { RH: [4, 3, 1] }, B: { LH: [4, 4] } };",
    "const SC_BLH = [3, 4, -1];   // the left hand of B♭ E♭ A♭ D♭: 3-2-1, 4-3-2-1, 3\nconst SC_LENS = { std: { RH: [3, 4, 1], LH: [1, 4, 3] }, F: { RH: [4, 3, 1] }, B: { LH: [4, 4] },\n  Bb: { RH: [-1, 3, 4], LH: SC_BLH }, Eb: { RH: [-1, 4, 3], LH: SC_BLH }, Ab: { RH: [-2, 3, 3], LH: SC_BLH }, Db: { RH: [-2, 4, -2], LH: SC_BLH }, Gb: { RH: [-3, 3, -2], LH: [4, 3, -1] } };")
rep("""  scLens(key, hand).forEach(len => { for (let j = p; j < p + len && j < upto; j++) { const col = len === 3 ? SC_G3 : len === 4 ? SC_G4 : '#26296b'; if (len === 3) marks[K[j]] = 'target'; else if (len === 4) marks[K[j]] = 'fof'; names[K[j]] = String(F[j]); ncol[K[j]] = col; } p += len; });""",
"""  scLens(key, hand).forEach(raw => { const len = Math.abs(raw), pl = raw < 0; for (let j = p; j < p + len && j < upto; j++) { const col = !pl && len === 3 ? SC_G3 : !pl && len === 4 ? SC_G4 : '#26296b'; if (!pl && len === 3) marks[K[j]] = 'target'; else if (!pl && len === 4) marks[K[j]] = 'fof'; names[K[j]] = String(F[j]); ncol[K[j]] = col; } p += len; });""")
NEW = r"""
// ─── Phase 576: Scales, lesson 6: the keys that start on a black key (B♭ E♭ A♭ D♭, then G♭ / F♯). Her text (SCALE_PATTERNS):
// the thumb only ever plays white keys; in all four keys the right-hand thumbs go on C and F, and the left hand is one shape for all four:
// 3-2-1, 4-3-2-1, 3. G♭ / F♯: three black keys in a row, fingers 2-3-4 cover them; both thumbs land on the only two white keys, C♭ (B) and F.
// Finger numbers are her SCALES[key].octaves[1] arrays.
const SC_BLK = [
  { key: 'Bb', hand: 'RH', text: ['B♭ major starts on a black key. The thumb only ever plays white keys: here C and F.', 'B♭ 장음계는 검은건반에서 시작해요. 엄지는 흰건반만 쳐요: 여기서는 C와 F.'] },
  { key: 'Eb', hand: 'RH', text: ['E♭ major: again the right-hand thumbs are on C and F.', 'E♭ 장음계: 오른손 엄지는 이번에도 C와 F예요.'] },
  { key: 'Ab', hand: 'RH', text: ['A♭ major: the right-hand thumbs are on C and F.', 'A♭ 장음계: 오른손 엄지는 C와 F예요.'] },
  { key: 'Db', hand: 'RH', text: ['D♭ major: the right-hand thumbs are on C and F.', 'D♭ 장음계: 오른손 엄지는 C와 F예요.'] },
  { key: 'Bb', hand: 'LH', text: ['The left hand is one shape for all four keys: 3-2-1, 4-3-2-1, 3.', '왼손은 네 조 모두 한 가지 모양이에요: 3-2-1, 4-3-2-1, 3.'] },
  { key: 'Gb', hand: 'RH', text: ['G♭ / F♯: three black keys in a row. Fingers 2, 3, 4 cover them; the thumbs land on the only two white keys, C♭ (B) and F.', 'G♭ / F♯: 나란히 있는 검은건반 세 개. 2, 3, 4번이 그 셋을 맡고, 엄지는 단 두 개뿐인 흰건반 C♭(B)과 F에 놓여요.'] },
];
function ScBlack() {
  const [view, setView] = useState('all');   // 'all' -> 'one' -> 'try'
  const [i, setI] = useState(0), [nonce, setNonce] = useState(0), [kk, setKk] = useState('Bb'), [hand, setHand] = useState('RH');
  const [found, setFound] = useState([]), [bad, setBad] = useState(null), [why, setWhy] = useState('');
  const timers = useRef([]);
  const clear = () => { timers.current.forEach(clearTimeout); timers.current = []; };
  useEffect(() => clear, []);
  const titleStyle = {textAlign:'center',fontFamily:"'Playfair Display', Georgia, serif",fontSize:22,fontWeight:900,color:'#26296b',lineHeight:1.2,margin:'0 0 8px',textWrap:'balance'};
  const lineStyle = {textAlign:'center',fontSize:15,fontWeight:800,color:'#26296b',margin:'8px 0 6px',minHeight:42,textWrap:'balance',wordBreak:'keep-all'};
  const prim = {...KF_BTN,minWidth:140,background:'#26296b',color:'#fffefa',borderColor:'#26296b'};
  const row = (children) => <div style={{textAlign:'center',marginTop:14,display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap'}}>{children}</div>;
  const title = t('Starting on a black key', '검은건반에서 시작하기');
  const paint = (key, h) => { const K = scIdx(key), marks = {}, names = {}, ncol = {}; scPaint(key, h, K, 8, marks, names, ncol); return { K, marks, names, ncol }; };
  const reset = () => { setFound([]); setBad(null); setWhy(''); setNonce(n => n + 1); };
  let body;
  if (view === 'all') {
    const P = paint('Bb', 'RH');
    body = <>
      <div style={titleStyle}>{title}</div>
      <div style={lineStyle}>{t('When a scale starts on a black key, the thumb only ever plays white keys.', '검은건반에서 시작하는 스케일에서 엄지는 흰건반만 쳐요.')}</div>
      <ScKeys ks={P.K} marks={P.marks} names={P.names} ncol={P.ncol} arcs={[]} nonce="all"/>
      {row(<button className="ghost-btn" style={prim} onClick={() => { setView('one'); setI(0); setNonce(n => n + 1); }}>{t('One by one →', '하나씩 →')}</button>)}
    </>;
  } else if (view === 'one') {
    const E = SC_BLK[i], P = paint(E.key, E.hand);
    body = <>
      <div style={titleStyle}>{title}</div>
      <div style={lineStyle}>{(E.hand === 'RH' ? t('Right hand. ', '오른손. ') : t('Left hand. ', '왼손. ')) + t(E.text[0], E.text[1])}</div>
      <ScKeys ks={P.K} marks={P.marks} names={P.names} ncol={P.ncol} arcs={[]} nonce={nonce + ':' + i}/>
      {row(<>
        <button className="ghost-btn" style={{...KF_BTN,minWidth:110}} onClick={() => { if (i === 0) setView('all'); else { setI(i - 1); setNonce(n => n + 1); } }}>{t('← Back', '← 이전')}</button>
        <button className="ghost-btn" style={prim} onClick={() => { if (i === SC_BLK.length - 1) { setView('try'); reset(); } else { setI(i + 1); setNonce(n => n + 1); } }}>{i === SC_BLK.length - 1 ? t('Your turn →', '내가 해보기 →') : t('Next →', '다음 →')}</button>
      </>)}
    </>;
  } else {
    // her turn: tap the two thumb keys (finger 1) of the key and hand she picked
    const K = scIdx(kk), F = SCALES[kk].octaves[1][hand], N = scNames(kk), thumbs = F.map((f, j) => f === 1 ? K[j] : null).filter(x => x != null);
    const done = found.length >= thumbs.length, P = paint(kk, hand), marks = {}, names = {}, ncol = {};
    if (done) Object.assign(marks, P.marks), Object.assign(names, P.names), Object.assign(ncol, P.ncol);
    found.forEach(k => { marks[k] = 'good'; names[k] = '1'; ncol[k] = '#2e8a6e'; });
    if (bad != null) marks[bad] = 'bad';
    const handWord = hand === 'RH' ? t('right hand', '오른손') : t('left hand', '왼손');
    const handKo = hand === 'RH' ? '오른손' : '왼손';
    const line = done ? t('Both thumbs found. Here is the whole fingering of ' + N[0] + ' major.', '엄지 둘을 다 찾았어요. ' + N[0] + ' 장음계의 운지 전체예요.')
      : bad != null ? why : t(N[0] + ' major, ' + handWord + ': tap the keys where the thumb goes. (' + found.length + '/' + thumbs.length + ')', N[0] + ' 장음계 ' + handKo + ': 엄지가 가는 건반을 눌러요. (' + found.length + '/' + thumbs.length + ')');
    const tap = (k) => { if (done || found.includes(k)) return; clear();
      if (thumbs.includes(k)) { setBad(null); setFound(f => [...f, k]); setNonce(n => n + 1); playKey(k, 0.6); }
      else { setBad(k); setWhy(PC_INFO[((k % 12) + 12) % 12].white ? t('Not a thumb key. The thumbs go on the white keys where a new group starts.', '엄지 건반이 아니에요. 엄지는 새 묶음이 시작하는 흰건반에 가요.') : t('The thumb only ever plays white keys.', '엄지는 흰건반만 쳐요.')); playKey(k, 0.4); timers.current.push(setTimeout(() => setBad(null), 1400)); } };
    body = <>
      <div style={titleStyle}>{t('Your turn', '내가 해보기')}</div>
      <div style={{display:'grid',gridTemplateColumns:'repeat(5,minmax(0,1fr))',gap:6,maxWidth:330,margin:'0 auto 6px'}}>
        {['Bb', 'Eb', 'Ab', 'Db', 'Gb'].map(k => <button key={k} className={'chip' + (kk === k ? ' active' : '')} aria-pressed={kk === k} style={{...KF_BTN,minHeight:40,padding:'0 4px'}} onClick={() => { clear(); setKk(k); reset(); playKey(SCALES[k].rootPc, 0.5); }}>{prettyNote(k)}</button>)}
      </div>
      <div style={{display:'grid',gridTemplateColumns:'repeat(2,minmax(0,1fr))',gap:6,maxWidth:330,margin:'0 auto 6px'}}>
        {[['RH', t('Right hand', '오른손')], ['LH', t('Left hand', '왼손')]].map(([h, lab]) => <button key={h} className={'chip' + (hand === h ? ' active' : '')} aria-pressed={hand === h} style={{...KF_BTN,minHeight:40}} onClick={() => { clear(); setHand(h); reset(); }}>{lab}</button>)}
      </div>
      <div style={lineStyle}>{line}</div>
      <ScKeys ks={K} marks={marks} names={names} ncol={ncol} arcs={[]} nonce={nonce + kk + hand} onTap={tap}/>
      {row(<>
        <button className="ghost-btn" style={{...KF_BTN,minWidth:110}} onClick={() => { clear(); setView('one'); setI(SC_BLK.length - 1); setNonce(n => n + 1); }}>{t('← Back', '← 이전')}</button>
        {done && <button className="ghost-btn" style={prim} onClick={() => reset()}>{t('Again', '다시 하기')}</button>}
      </>)}
    </>;
  }
  return <div className="try-box" data-sc-lesson="black" style={{background:'#fff',border:'1px solid var(--border)',borderRadius:10,padding:'10px 10px 12px',margin:'4px 0 16px'}}>{body}</div>;
}
"""
rep("\n// lesson 5: the natural.", NEW + "\n// lesson 5: the natural.")
rep(" ['sc-odd', 'White keys: two are different', '흰건반에서 시작: 둘은 달라요', 'F and B: one hand each.', 'F와 B: 한 손씩.', ScOdd]].forEach(",
    " ['sc-odd', 'White keys: two are different', '흰건반에서 시작: 둘은 달라요', 'F and B: one hand each.', 'F와 B: 한 손씩.', ScOdd],\n ['sc-black', 'Starting on a black key', '검은건반에서 시작하기', 'The thumb only ever plays white keys.', '엄지는 흰건반만 쳐요.', ScBlack]].forEach(")
rep("lessons: ['sc-shape', 'sc-same', 'sc-deg', 'sc-finger', 'sc-odd'], check: 'scales'", "lessons: ['sc-shape', 'sc-same', 'sc-deg', 'sc-finger', 'sc-odd', 'sc-black'], check: 'scales'")
open(sys.argv[2],'w',encoding='utf-8').write(s)
