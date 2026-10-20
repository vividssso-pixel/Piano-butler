import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
# ScKeys: optional colour per name
rep("function ScKeys({ marks, onTap, arcs, nonce, names, ks }) {", "function ScKeys({ marks, onTap, arcs, nonce, names, ks, ncol }) {")
rep("""textAnchor="middle" fontSize="17" fontWeight="900" fill="#c0431f" style={{animation:'fadeUp 0.3s both'}}>{txt}</text>)}</g>}/>
  </div>);
}
// the story screens""","""textAnchor="middle" fontSize="17" fontWeight="900" fill={(ncol && ncol[k]) || '#c0431f'} style={{animation:'fadeUp 0.3s both'}}>{txt}</text>)}</g>}/>
  </div>);
}
// the story screens""")
a = s.index("const SC_FING = {"); b = s.index("\n// lesson 5: the natural.")
NEW = r"""// Colours by group (her 2026-10-20 call): a group of 3 is coral, a group of 4 is blue, finger 5 and any lone note stay plain keys.
// The groupings are hers: standard RH 3-4-1, LH 1-4-3; F's RH 4-3-1 (groups of 4-3-4-3-1 over two octaves); B's LH 4-4 (4321 4321).
const SC_LENS = { std: { RH: [3, 4, 1], LH: [1, 4, 3] }, F: { RH: [4, 3, 1] }, B: { LH: [4, 4] } };
const scLens = (key, hand) => (SC_LENS[key] && SC_LENS[key][hand]) || SC_LENS.std[hand];
const SC_G3 = '#c0431f', SC_G4 = '#3b4fa8';
// paint the first `upto` notes of a key's one-octave fingering: marks (pale coral / pale blue), the finger numbers and their colours
function scPaint(key, hand, K, upto, marks, names, ncol) {
  const F = SCALES[key].octaves[1][hand]; let p = 0;
  scLens(key, hand).forEach(len => { for (let j = p; j < p + len && j < upto; j++) { const col = len === 3 ? SC_G3 : len === 4 ? SC_G4 : '#26296b'; if (len === 3) marks[K[j]] = 'target'; else if (len === 4) marks[K[j]] = 'fof'; names[K[j]] = String(F[j]); ncol[K[j]] = col; } p += len; });
}
const SC_FSTEPS = [
  { hand: 'RH', n: 3, text: ['Right hand starts on the thumb: a group of 3, fingers 1, 2, 3.', '오른손은 엄지로 시작해요. 3개 묶음: 1, 2, 3번 손가락.'] },
  { hand: 'RH', n: 4, text: ['Then the thumb goes under and starts the next group.', '그다음 엄지가 밑으로 들어가서 다음 묶음을 시작해요.'] },
  { hand: 'RH', n: 7, text: ['Now a group of 4: fingers 1, 2, 3, 4.', '이제 4개 묶음: 1, 2, 3, 4번 손가락.'] },
  { hand: 'RH', n: 8, text: ['Finger 5 is on top.', '5번 손가락이 맨 위예요.'] },
  { hand: 'LH', n: 1, text: ['The left hand is the mirror: finger 5 at the bottom.', '왼손은 거울이에요. 5번 손가락이 맨 아래예요.'] },
  { hand: 'LH', n: 5, text: ['Then 4 fingers: 4, 3, 2, 1.', '그다음 4개: 4, 3, 2, 1번 손가락.'] },
  { hand: 'LH', n: 8, text: ['Then 3: fingers 3, 2, 1.', '그다음 3개: 3, 2, 1번 손가락.'] },
];
function ScFinger() {
  const [view, setView] = useState('all');   // 'all' -> 'one' -> 'same' -> 'try'
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
  const newRound = () => { setSeq(shuffle([0, 1, 2, 3, 4, 5, 6, 7])); setAt(0); setBad(null); setNonce(n => n + 1); };
  const last = SC_FSTEPS.length - 1;
  let body;
  if (view === 'all') {
    const K = scIdx('C'), marks = {}, names = {}, ncol = {}; scPaint('C', 'RH', K, 8, marks, names, ncol);
    body = <>
      <div style={titleStyle}>{title}</div>
      <div style={lineStyle}>{t('Right hand: a group of 3 (coral) and a group of 4 (blue).', '오른손: 3개 묶음(산호색)과 4개 묶음(파란색).')}</div>
      <ScKeys ks={K} marks={marks} names={names} ncol={ncol} arcs={[]} nonce="all"/>
      {row(<button className="ghost-btn" style={prim} onClick={() => { setView('one'); setI(0); setNonce(n => n + 1); }}>{t('One by one →', '하나씩 →')}</button>)}
    </>;
  } else if (view === 'one') {
    const E = SC_FSTEPS[i], K = scIdx('C'), marks = {}, names = {}, ncol = {}; scPaint('C', E.hand, K, E.n, marks, names, ncol);
    body = <>
      <div style={titleStyle}>{title}</div>
      <div style={lineStyle}>{(E.hand === 'RH' ? t('Right hand. ', '오른손. ') : t('Left hand. ', '왼손. ')) + t(E.text[0], E.text[1])}</div>
      <ScKeys ks={K} marks={marks} names={names} ncol={ncol} arcs={[]} nonce={nonce + ':' + i}/>
      {row(<>
        <button className="ghost-btn" style={{...KF_BTN,minWidth:110}} onClick={() => { clear(); if (i === 0) setView('all'); else { setI(i - 1); setNonce(n => n + 1); } }}>{t('← Back', '← 이전')}</button>
        <button className="ghost-btn" style={prim} onClick={() => { clear(); if (i === last) { setView('same'); setNonce(n => n + 1); } else { setI(i + 1); setNonce(n => n + 1); } }}>{t('Next →', '다음 →')}</button>
      </>)}
    </>;
  } else if (view === 'same') {
    const K = scIdx('G'), marks = {}, names = {}, ncol = {}; scPaint('G', 'RH', K, 8, marks, names, ncol);
    body = <>
      <div style={titleStyle}>{title}</div>
      <div style={lineStyle}>{t('The same fingers for these five keys: C, G, D, A, E. Here is G.', '이 다섯 조는 손가락이 같아요: C, G, D, A, E. 여기는 G예요.')}</div>
      <ScKeys ks={K} marks={marks} names={names} ncol={ncol} arcs={[]} nonce="same"/>
      {row(<>
        <button className="ghost-btn" style={{...KF_BTN,minWidth:110}} onClick={() => { setView('one'); setI(last); setNonce(n => n + 1); }}>{t('← Back', '← 이전')}</button>
        <button className="ghost-btn" style={prim} onClick={() => { setView('try'); newRound(); }}>{t('Your turn →', '내가 해보기 →')}</button>
      </>)}
    </>;
  } else {
    const K = scIdx(kk), F = SCALES[kk].octaves[1][hand], N = scNames(kk), done = at >= 8, marks = {}, names = {}, ncol = {};
    seq.slice(0, at).forEach(j => { marks[K[j]] = 'good'; names[K[j]] = String(F[j]); ncol[K[j]] = '#2e8a6e'; });
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
      <ScKeys ks={K} marks={marks} names={names} ncol={ncol} arcs={[]} nonce={nonce + kk + hand}/>
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
// ─── Phase 575: Scales, lesson 5: white-key starts whose fingering is different: F (right hand) and B (left hand). Only to notice that they differ.
// Her text: F's right hand plays the group of 4 first, so finger 4 takes the B♭ and the thumb stays off it; F's left hand is standard.
// B's right hand is standard; B's left hand starts on finger 4 and plays two groups of 4, so its thumb lands on the white keys E and B.
const SC_ODD = [
  { key: 'F', hand: 'RH', text: ['F: the right hand plays the group of 4 first, so finger 4 takes the B♭ and the thumb stays off it.', 'F: 오른손이 4개 묶음을 먼저 쳐서, B♭은 4번 손가락이 맡고 엄지는 닿지 않아요.'] },
  { key: 'F', hand: 'LH', text: ['F: the left hand is the standard shape.', 'F: 왼손은 기본 모양이에요.'] },
  { key: 'B', hand: 'RH', text: ['B: the right hand is the standard shape.', 'B: 오른손은 기본 모양이에요.'] },
  { key: 'B', hand: 'LH', text: ['B: the left hand starts on finger 4 and plays two groups of 4, so its thumb lands on the white keys E and B.', 'B: 왼손은 4번 손가락으로 시작해서 4개 묶음을 두 번 치니까, 엄지가 흰건반 E와 B에 놓여요.'] },
];
const SC_ODD_SET = ['F:RH', 'B:LH'];
function ScOdd() {
  const [view, setView] = useState('all');   // 'all' -> 'one' -> 'try'
  const [i, setI] = useState(0), [nonce, setNonce] = useState(0);
  const [seq, setSeq] = useState([]), [at, setAt] = useState(0), [given, setGiven] = useState(null), [score, setScore] = useState(0);
  const titleStyle = {textAlign:'center',fontFamily:"'Playfair Display', Georgia, serif",fontSize:22,fontWeight:900,color:'#26296b',lineHeight:1.2,margin:'0 0 8px',textWrap:'balance'};
  const lineStyle = {textAlign:'center',fontSize:15,fontWeight:800,color:'#26296b',margin:'8px 0 6px',minHeight:42,textWrap:'balance',wordBreak:'keep-all'};
  const prim = {...KF_BTN,minWidth:140,background:'#26296b',color:'#fffefa',borderColor:'#26296b'};
  const row = (children) => <div style={{textAlign:'center',marginTop:14,display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap'}}>{children}</div>;
  const title = t('White keys: two are different', '흰건반에서 시작: 둘은 달라요');
  const paint = (key, hand) => { const K = scIdx(key), marks = {}, names = {}, ncol = {}; scPaint(key, hand, K, 8, marks, names, ncol); return { K, marks, names, ncol }; };
  const newRound = () => { const all = []; ['C', 'G', 'D', 'A', 'E', 'F', 'B'].forEach(k => ['RH', 'LH'].forEach(h => all.push(k + ':' + h)));
    const rest = shuffle(all.filter(x => !SC_ODD_SET.includes(x))).slice(0, 4); setSeq(shuffle([...SC_ODD_SET, ...rest])); setAt(0); setGiven(null); setScore(0); setNonce(n => n + 1); };
  let body;
  if (view === 'all') {
    const P = paint('F', 'RH');
    body = <>
      <div style={titleStyle}>{title}</div>
      <div style={lineStyle}>{t('Most white-key scales share one fingering. F and B each have one hand that is different.', '흰건반에서 시작하는 스케일은 대부분 운지가 같아요. F와 B는 한 손씩 달라요.')}</div>
      <ScKeys ks={P.K} marks={P.marks} names={P.names} ncol={P.ncol} arcs={[]} nonce="all"/>
      {row(<button className="ghost-btn" style={prim} onClick={() => { setView('one'); setI(0); setNonce(n => n + 1); }}>{t('One by one →', '하나씩 →')}</button>)}
    </>;
  } else if (view === 'one') {
    const E = SC_ODD[i], P = paint(E.key, E.hand);
    body = <>
      <div style={titleStyle}>{title}</div>
      <div style={lineStyle}>{(E.hand === 'RH' ? t('Right hand. ', '오른손. ') : t('Left hand. ', '왼손. ')) + t(E.text[0], E.text[1])}</div>
      <ScKeys ks={P.K} marks={P.marks} names={P.names} ncol={P.ncol} arcs={[]} nonce={nonce + ':' + i}/>
      {row(<>
        <button className="ghost-btn" style={{...KF_BTN,minWidth:110}} onClick={() => { if (i === 0) setView('all'); else { setI(i - 1); setNonce(n => n + 1); } }}>{t('← Back', '← 이전')}</button>
        <button className="ghost-btn" style={prim} onClick={() => { if (i === SC_ODD.length - 1) { setView('try'); newRound(); } else { setI(i + 1); setNonce(n => n + 1); } }}>{i === SC_ODD.length - 1 ? t('Your turn →', '내가 해보기 →') : t('Next →', '다음 →')}</button>
      </>)}
    </>;
  } else {
    const done = at >= seq.length, cur = done ? null : seq[at], [ck, ch] = cur ? cur.split(':') : ['C', 'RH'];
    const odd = cur ? SC_ODD_SET.includes(cur) : false, P = paint(ck, ch), N = scNames(ck);
    const handWord = ch === 'RH' ? t('right hand', '오른손') : t('left hand', '왼손');
    const handKo = ch === 'RH' ? '오른손' : '왼손';
    const answer = (v) => { if (given != null || done) return; setGiven(v); if ((v === 'odd') === odd) setScore(x => x + 1); setNonce(n => n + 1); };
    const line = done ? t('Only two are different: the right hand of F and the left hand of B. You got ' + score + ' of ' + seq.length + '.', '다른 건 둘뿐이에요: F의 오른손과 B의 왼손. ' + seq.length + '개 중 ' + score + '개 맞았어요.')
      : given == null ? t('The ' + handWord + ' of ' + N[0] + ' major: the standard shape, or different? (' + (at + 1) + '/' + seq.length + ')', N[0] + ' 장음계 ' + handKo + ': 기본 모양일까요, 다를까요? (' + (at + 1) + '/' + seq.length + ')')
      : ((given === 'odd') === odd ? t('Yes. ', '맞아요. ') : t('Not quite. ', '아니에요. ')) + (odd ? t('It is different.', '달라요.') : t('It is the standard shape.', '기본 모양이에요.'));
    body = <>
      <div style={titleStyle}>{t('Your turn', '내가 해보기')}</div>
      <div style={lineStyle}>{line}</div>
      {!done && <ScKeys ks={P.K} marks={given != null ? P.marks : { [P.K[0]]: 'pick' }} names={given != null ? P.names : {}} ncol={P.ncol} arcs={[]} nonce={nonce + cur}/>}
      {!done && given == null && <div style={{display:'grid',gridTemplateColumns:'repeat(2,minmax(0,1fr))',gap:8,maxWidth:330,margin:'12px auto 0'}}>
        <button className="ghost-btn" style={{...KF_BTN,minHeight:48}} onClick={() => answer('std')}>{t('Standard', '기본 모양')}</button>
        <button className="ghost-btn" style={{...KF_BTN,minHeight:48}} onClick={() => answer('odd')}>{t('Different', '달라요')}</button>
      </div>}
      {row(<>
        <button className="ghost-btn" style={{...KF_BTN,minWidth:110}} onClick={() => { setView('one'); setI(SC_ODD.length - 1); setNonce(n => n + 1); }}>{t('← Back', '← 이전')}</button>
        {given != null && !done && <button className="ghost-btn" style={prim} onClick={() => { setAt(at + 1); setGiven(null); setNonce(n => n + 1); }}>{t('Next →', '다음 →')}</button>}
        {done && <button className="ghost-btn" style={prim} onClick={() => newRound()}>{t('Again', '다시 하기')}</button>}
      </>)}
    </>;
  }
  return <div className="try-box" data-sc-lesson="odd" style={{background:'#fff',border:'1px solid var(--border)',borderRadius:10,padding:'10px 10px 12px',margin:'4px 0 16px'}}>{body}</div>;
}
"""
s = s[:a] + NEW + s[b:]
rep(" ['sc-finger', 'The standard fingering', '기본 운지', 'Right hand 1 2 3, 1 2 3 4, 5. Left hand: the mirror.', '오른손 1 2 3, 1 2 3 4, 5. 왼손은 거울.', ScFinger]].forEach(",
    " ['sc-finger', 'The standard fingering', '기본 운지', 'Right hand 1 2 3, 1 2 3 4, 5. Left hand: the mirror.', '오른손 1 2 3, 1 2 3 4, 5. 왼손은 거울.', ScFinger],\n ['sc-odd', 'White keys: two are different', '흰건반에서 시작: 둘은 달라요', 'F and B: one hand each.', 'F와 B: 한 손씩.', ScOdd]].forEach(")
rep("lessons: ['sc-shape', 'sc-same', 'sc-deg', 'sc-finger'], check: 'scales'", "lessons: ['sc-shape', 'sc-same', 'sc-deg', 'sc-finger', 'sc-odd'], check: 'scales'")
open(sys.argv[2],'w',encoding='utf-8').write(s)
