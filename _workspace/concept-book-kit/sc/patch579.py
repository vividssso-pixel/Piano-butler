import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
NEW = r"""
// ─── Phase 574: Scales, lesson 4: the standard fingering (C G D A E). Her text (SCALE_PATTERNS): start on the thumb; right hand a group of 3,
// then a group of 4, finger 5 on top; the left hand is the mirror: 5 at the bottom, then 4 fingers, then 3; the same fingers for all five keys.
// The finger numbers are her SCALES[key].octaves[1] arrays (RH 1 2 3 1 2 3 4 5, LH 5 4 3 2 1 3 2 1).
const SC_FING = {
  RH: [1, 2, 3, 1, 2, 3, 4, 5], LH: [5, 4, 3, 2, 1, 3, 2, 1],
};
const SC_FSTEPS = [
  { hand: 'RH', n: [0, 1, 2], th: [0], text: ['Right hand starts on the thumb: a group of 3, fingers 1, 2, 3.', '오른손은 엄지로 시작해요. 3개 묶음: 1, 2, 3번 손가락.'] },
  { hand: 'RH', n: [0, 1, 2, 3], th: [0, 3], text: ['Then the thumb goes under and plays the next key.', '그다음 엄지가 밑으로 들어가서 다음 건반을 쳐요.'] },
  { hand: 'RH', n: [0, 1, 2, 3, 4, 5, 6], th: [0, 3], text: ['Now a group of 4: fingers 1, 2, 3, 4.', '이제 4개 묶음: 1, 2, 3, 4번 손가락.'] },
  { hand: 'RH', n: [0, 1, 2, 3, 4, 5, 6, 7], th: [0, 3], text: ['Finger 5 is on top.', '5번 손가락이 맨 위예요.'] },
  { hand: 'LH', n: [0], th: [], text: ['The left hand is the mirror: finger 5 at the bottom.', '왼손은 거울이에요. 5번 손가락이 맨 아래예요.'] },
  { hand: 'LH', n: [0, 1, 2, 3, 4], th: [4], text: ['Then 4 fingers: 4, 3, 2, 1.', '그다음 4개: 4, 3, 2, 1번 손가락.'] },
  { hand: 'LH', n: [0, 1, 2, 3, 4, 5, 6, 7], th: [4, 7], text: ['Then 3: fingers 3, 2, 1.', '그다음 3개: 3, 2, 1번 손가락.'] },
];
function ScFinger() {
  const [view, setView] = useState('all');   // 'all' -> 'one' -> 'try'
  const [i, setI] = useState(0), [nonce, setNonce] = useState(0), [kk, setKk] = useState('C'), [hand, setHand] = useState('RH');
  const [seq, setSeq] = useState([]), [at, setAt] = useState(0), [bad, setBad] = useState(null);
  const timers = useRef([]);
  const clear = () => { timers.current.forEach(clearTimeout); timers.current = []; };
  useEffect(() => clear, []);
  const titleStyle = {textAlign:'center',fontFamily:"'Playfair Display', Georgia, serif",fontSize:22,fontWeight:900,color:'#26296b',lineHeight:1.2,margin:'0 0 8px',textWrap:'balance'};
  const lineStyle = {textAlign:'center',fontSize:15,fontWeight:800,color:'#26296b',margin:'8px 0 6px',minHeight:42,textWrap:'balance',wordBreak:'keep-all'};
  const prim = {...KF_BTN,minWidth:140,background:'#26296b',color:'#fffefa',borderColor:'#26296b'};
  const row = (children) => <div style={{textAlign:'center',marginTop:14,display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap'}}>{children}</div>;
  const title = t('The standard fingering', '기본 운지');
  const newRound = (h) => { setSeq(shuffle([0, 1, 2, 3, 4, 5, 6, 7])); setAt(0); setBad(null); setNonce(n => n + 1); };
  const last = SC_FSTEPS.length - 1;
  let body;
  if (view === 'all') {
    const K = scIdx('C'), F = SC_FING.RH, marks = {}, names = {}; K.forEach((k, j) => { marks[k] = F[j] === 1 ? 'pick' : 'pass'; names[k] = String(F[j]); });
    body = <>
      <div style={titleStyle}>{title}</div>
      <div style={lineStyle}>{t('Right hand: a group of 3, then a group of 4. The thumb is coral.', '오른손: 3개 묶음, 그다음 4개 묶음. 엄지는 산호색이에요.')}</div>
      <ScKeys ks={K} marks={marks} names={names} arcs={[]} nonce="all"/>
      {row(<button className="ghost-btn" style={prim} onClick={() => { setView('one'); setI(0); setNonce(n => n + 1); }}>{t('One by one →', '하나씩 →')}</button>)}
    </>;
  } else if (view === 'one') {
    const E = SC_FSTEPS[i], key = i === last + 1 ? 'G' : 'C', K = scIdx('C'), F = SC_FING[E.hand], marks = {}, names = {};
    E.n.forEach(j => { marks[K[j]] = E.th.includes(j) ? 'pick' : 'pass'; names[K[j]] = String(F[j]); });
    body = <>
      <div style={titleStyle}>{title}</div>
      <div style={lineStyle}>{(E.hand === 'RH' ? t('Right hand. ', '오른손. ') : t('Left hand. ', '왼손. ')) + t(E.text[0], E.text[1])}</div>
      <ScKeys ks={K} marks={marks} names={names} arcs={[]} nonce={nonce + ':' + i}/>
      {row(<>
        <button className="ghost-btn" style={{...KF_BTN,minWidth:110}} onClick={() => { clear(); if (i === 0) setView('all'); else { setI(i - 1); setNonce(n => n + 1); } }}>{t('← Back', '← 이전')}</button>
        <button className="ghost-btn" style={prim} onClick={() => { clear(); if (i === last) { setView('same'); setNonce(n => n + 1); } else { setI(i + 1); setNonce(n => n + 1); } }}>{t('Next →', '다음 →')}</button>
      </>)}
    </>;
  } else if (view === 'same') {
    const K = scIdx('G'), F = SC_FING.RH, N = scNames('G'), marks = {}, names = {}; K.forEach((k, j) => { marks[k] = F[j] === 1 ? 'pick' : 'pass'; names[k] = String(F[j]); });
    body = <>
      <div style={titleStyle}>{title}</div>
      <div style={lineStyle}>{t('The same fingers for all five keys: C, G, D, A, E. Here is G.', '다섯 조 모두 같은 손가락이에요: C, G, D, A, E. 여기는 G예요.')}</div>
      <ScKeys ks={K} marks={marks} names={names} arcs={[]} nonce="same"/>
      {row(<>
        <button className="ghost-btn" style={{...KF_BTN,minWidth:110}} onClick={() => { setView('one'); setI(last); setNonce(n => n + 1); }}>{t('← Back', '← 이전')}</button>
        <button className="ghost-btn" style={prim} onClick={() => { setView('try'); newRound(); }}>{t('Your turn →', '내가 해보기 →')}</button>
      </>)}
    </>;
  } else {
    const K = scIdx(kk), F = SC_FING[hand], N = scNames(kk), done = at >= 8, marks = {}, names = {};
    seq.slice(0, at).forEach(j => { marks[K[j]] = 'good'; names[K[j]] = String(F[j]); });
    const cur = seq[at]; if (cur != null && !done) marks[K[cur]] = 'pick';
    const handWord = hand === 'RH' ? t('Right hand', '오른손') : t('Left hand', '왼손');
    const line = done ? t('All eight notes: that is the ' + handWord.toLowerCase() + ' fingering of ' + N[0] + ' major.', '여덟 음을 다 했어요. ' + N[0] + ' 장음계 ' + handWord + ' 운지예요.')
      : bad != null ? t('Not that finger. Which finger plays ' + N[cur] + '?', '그 손가락이 아니에요. ' + N[cur] + '은 몇 번 손가락일까요?')
      : t(handWord + ': which finger plays ' + N[cur] + '? (' + (at + 1) + '/8)', handWord + ': ' + N[cur] + '은 몇 번 손가락일까요? (' + (at + 1) + '/8)');
    const pick = (f) => { if (done) return; clear(); if (f === F[cur]) { setBad(null); setAt(at + 1); setNonce(n => n + 1); playKey(K[cur], 0.6); } else { setBad(f); playKey(K[cur], 0.4); timers.current.push(setTimeout(() => setBad(null), 1100)); } };
    body = <>
      <div style={titleStyle}>{t('Your turn', '내가 해보기')}</div>
      <div style={{display:'grid',gridTemplateColumns:'repeat(5,minmax(0,1fr))',gap:6,maxWidth:330,margin:'0 auto 6px'}}>
        {['C', 'G', 'D', 'A', 'E'].map(k => <button key={k} className={'chip' + (kk === k ? ' active' : '')} aria-pressed={kk === k} style={{...KF_BTN,minHeight:40,padding:'0 4px'}} onClick={() => { clear(); setKk(k); newRound(); playKey(SF12.indexOf(k), 0.5); }}>{k}</button>)}
      </div>
      <div style={{display:'grid',gridTemplateColumns:'repeat(2,minmax(0,1fr))',gap:6,maxWidth:330,margin:'0 auto 6px'}}>
        {[['RH', t('Right hand', '오른손')], ['LH', t('Left hand', '왼손')]].map(([h, lab]) => <button key={h} className={'chip' + (hand === h ? ' active' : '')} aria-pressed={hand === h} style={{...KF_BTN,minHeight:40}} onClick={() => { clear(); setHand(h); newRound(); }}>{lab}</button>)}
      </div>
      <div style={lineStyle}>{line}</div>
      <ScKeys ks={K} marks={marks} names={names} arcs={[]} nonce={nonce + kk + hand}/>
      {!done && <div style={{display:'grid',gridTemplateColumns:'repeat(5,minmax(0,1fr))',gap:6,maxWidth:330,margin:'10px auto 0'}}>
        {[1, 2, 3, 4, 5].map(f => <button key={f} className="ghost-btn" style={{...KF_BTN,minHeight:48,fontSize:18,padding:0,...(bad === f ? {background:'#fbe3da',borderColor:'#e4572e',color:'#c0431f'} : {})}} onClick={() => pick(f)}>{f}</button>)}
      </div>}
      {row(<>
        <button className="ghost-btn" style={{...KF_BTN,minWidth:110}} onClick={() => { clear(); setView('same'); setNonce(n => n + 1); }}>{t('← Back', '← 이전')}</button>
        {done && <button className="ghost-btn" style={prim} onClick={() => newRound()}>{t('Again', '다시 하기')}</button>}
      </>)}
    </>;
  }
  return <div className="try-box" data-sc-lesson="finger" style={{background:'#fff',border:'1px solid var(--border)',borderRadius:10,padding:'10px 10px 12px',margin:'4px 0 16px'}}>{body}</div>;
}
"""
rep("\n// lesson 5: the natural.", NEW + "\n// lesson 5: the natural.")
rep(" ['sc-deg', 'The degrees of the scale', '음계의 음 번호와 이름', 'Tonic, supertonic … leading note.', '으뜸음, 윗으뜸음 … 이끎음.', ScDeg]].forEach(",
    " ['sc-deg', 'The degrees of the scale', '음계의 음 번호와 이름', 'Tonic, supertonic … leading note.', '으뜸음, 윗으뜸음 … 이끎음.', ScDeg],\n ['sc-finger', 'The standard fingering', '기본 운지', 'Right hand 1 2 3, 1 2 3 4, 5. Left hand: the mirror.', '오른손 1 2 3, 1 2 3 4, 5. 왼손은 거울.', ScFinger]].forEach(")
rep("lessons: ['sc-shape', 'sc-same', 'sc-deg'], check: 'scales'", "lessons: ['sc-shape', 'sc-same', 'sc-deg', 'sc-finger'], check: 'scales'")
open(sys.argv[2],'w',encoding='utf-8').write(s)
