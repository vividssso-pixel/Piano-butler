import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
# --- ScKeys: both names on the black keys (when no arrows are drawn); finger numbers in one straight row with a ring round each thumb
rep("function ScKeys({ marks, onTap, arcs, nonce, names, ks, ncol }) {", "function ScKeys({ marks, onTap, arcs, nonce, names, ks, ncol, nums }) {")
rep("""<TapKeyboard octaves={2} extraC labels="white" marks={marks} onTap={onTap} top={46} vx={[x0, x1]} overlay={<g aria-hidden="true">{arrows}{Object.entries(names || {}).map(([k, txt]) =>
      <text key={'n' + k + txt} x={kx(+k)} y={white(+k) ? -9 : -27} textAnchor="middle" fontSize="17" fontWeight="900" fill={(ncol && ncol[k]) || '#c0431f'} style={{animation:'fadeUp 0.3s both'}}>{txt}</text>)}</g>}/>""",
"""<TapKeyboard octaves={2} extraC labels={arcs.length ? 'white' : 'all'} marks={marks} onTap={onTap} top={46} vx={[x0, x1]} overlay={<g aria-hidden="true">{arrows}{Object.entries(names || {}).map(([k, txt]) => { const col = (ncol && ncol[k]) || '#c0431f';
      return <g key={'n' + k + txt} style={{animation:'fadeUp 0.3s both'}}>
        {nums && txt === '1' && <circle cx={kx(+k)} cy={-18} r={13} fill="none" stroke={col} strokeWidth="2.4"/>}
        <text x={kx(+k)} y={nums ? -12 : (white(+k) ? -9 : -27)} textAnchor="middle" fontSize="17" fontWeight="900" fill={col}>{txt}</text>
      </g>; })}</g>}/>""")
# --- replace lessons 4, 5, 6 (finger lessons) as one block
a = s.index("const SC_FSTEPS = ["); b = s.index("\n// lesson 5: the natural.")
NEW = r"""const SC_FSTEPS = [
  { hand: 'RH', n: 3, text: ['Right hand starts on the thumb: a group of 3, fingers 1, 2, 3.', '오른손은 엄지로 시작해요. 3개 묶음: 1, 2, 3번 손가락.'] },
  { hand: 'RH', n: 4, text: ['Then the thumb goes under and starts the next group.', '그다음 엄지가 밑으로 들어가서 다음 묶음을 시작해요.'] },
  { hand: 'RH', n: 7, text: ['Now a group of 4: fingers 1, 2, 3, 4.', '이제 4개 묶음: 1, 2, 3, 4번 손가락.'] },
  { hand: 'RH', n: 8, text: ['Finger 5 is on top.', '5번 손가락이 맨 위예요.'] },
  { hand: 'LH', n: 1, text: ['The left hand is the mirror: finger 5 at the bottom.', '왼손은 거울이에요. 5번 손가락이 맨 아래예요.'] },
  { hand: 'LH', n: 5, text: ['Then 4 fingers: 4, 3, 2, 1.', '그다음 4개: 4, 3, 2, 1번 손가락.'] },
  { hand: 'LH', n: 8, text: ['Then 3: fingers 3, 2, 1.', '그다음 3개: 3, 2, 1번 손가락.'] },
];
// a strip of group blocks: coral = a group of 3, blue = a group of 4, grey = the rest (finger numbers inside); rows: { keys, key, hand, odd }
function ScStrip({ rows }) {
  const blocks = (key, hand) => { const F = SCALES[key].octaves[1][hand]; let p = 0; return scLens(key, hand).map((raw, g) => { const len = Math.abs(raw), pl = raw < 0, a = p; p += len;
    const bg = !pl && len === 3 ? '#fbe3da' : !pl && len === 4 ? '#dfe9f8' : '#efeadc', bd = !pl && len === 3 ? '#e4572e' : !pl && len === 4 ? '#3b4fa8' : '#d8cfb6', col = !pl && len === 3 ? SC_G3 : !pl && len === 4 ? SC_G4 : '#26296b';
    return <div key={g} style={{gridColumn:'span ' + len,height:30,borderRadius:7,background:bg,border:'1.5px solid ' + bd,color:col,display:'flex',alignItems:'center',justifyContent:'center',fontWeight:900,fontSize:14,letterSpacing:'0.04em'}}>{F.slice(a, p).join(' ')}</div>; }); };
  return <div style={{display:'grid',gap:8,maxWidth:330,margin:'0 auto'}}>
    {rows.map((r, i) => <div key={i} style={{display:'grid',gridTemplateColumns:'74px minmax(0,1fr) 18px',alignItems:'center',gap:6}}>
      <div style={{lineHeight:1.15}}><div style={{fontWeight:900,fontSize:13,color:'#26296b',wordSpacing:4}}>{r.keys}</div><div style={{fontSize:11,fontWeight:700,color:'#6d6f9c'}}>{r.hand === 'RH' ? t('right hand', '오른손') : t('left hand', '왼손')}</div></div>
      <div style={{display:'grid',gridTemplateColumns:'repeat(8,minmax(0,1fr))',gap:2}}>{blocks(r.key, r.hand)}</div>
      <div style={{fontWeight:900,fontSize:18,color:'#c0431f',textAlign:'center'}}>{r.odd ? '≠' : ''}</div>
    </div>)}
  </div>;
}
// ─── Phase 577 (her call, 2026-10-20): lessons 4 and 5 are one lesson. The standard fingering, then one strip of groups for every white-key start,
// so F's right hand and B's left hand are only noticed as different; then "standard or different?".
const SC_ODD_SET = ['F:RH', 'B:LH'];
function ScFinger() {
  const [view, setView] = useState('all');   // 'all' -> 'one' -> 'cmp' -> 'try'
  const [i, setI] = useState(0), [nonce, setNonce] = useState(0);
  const [seq, setSeq] = useState([]), [at, setAt] = useState(0), [given, setGiven] = useState(null), [score, setScore] = useState(0);
  const titleStyle = {textAlign:'center',fontFamily:"'Playfair Display', Georgia, serif",fontSize:22,fontWeight:900,color:'#26296b',lineHeight:1.2,margin:'0 0 8px',textWrap:'balance'};
  const lineStyle = {textAlign:'center',fontSize:15,fontWeight:800,color:'#26296b',margin:'8px 0 6px',minHeight:42,textWrap:'balance',wordBreak:'keep-all'};
  const prim = {...KF_BTN,minWidth:140,background:'#26296b',color:'#fffefa',borderColor:'#26296b'};
  const row = (children) => <div style={{textAlign:'center',marginTop:14,display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap'}}>{children}</div>;
  const title = t('Fingering from a white key', '흰건반에서 시작하는 운지');
  const paint = (key, hand, upto = 8) => { const K = scIdx(key), marks = {}, names = {}, ncol = {}; scPaint(key, hand, K, upto, marks, names, ncol); return { K, marks, names, ncol }; };
  const last = SC_FSTEPS.length - 1;
  const newRound = () => { const all = []; ['C', 'G', 'D', 'A', 'E', 'F', 'B'].forEach(k => ['RH', 'LH'].forEach(h => all.push(k + ':' + h)));
    const rest = shuffle(all.filter(x => !SC_ODD_SET.includes(x))).slice(0, 4); setSeq(shuffle([...SC_ODD_SET, ...rest])); setAt(0); setGiven(null); setScore(0); setNonce(n => n + 1); };
  let body;
  if (view === 'all') {
    const P = paint('C', 'RH');
    body = <>
      <div style={titleStyle}>{title}</div>
      <div style={lineStyle}>{t('Right hand: a group of 3 (coral) and a group of 4 (blue). The thumb is circled.', '오른손: 3개 묶음(산호색)과 4개 묶음(파란색). 엄지에 동그라미를 쳤어요.')}</div>
      <ScKeys nums ks={P.K} marks={P.marks} names={P.names} ncol={P.ncol} arcs={[]} nonce="all"/>
      {row(<button className="ghost-btn" style={prim} onClick={() => { setView('one'); setI(0); setNonce(n => n + 1); }}>{t('One by one →', '하나씩 →')}</button>)}
    </>;
  } else if (view === 'one') {
    const E = SC_FSTEPS[i], P = paint('C', E.hand, E.n);
    body = <>
      <div style={titleStyle}>{title}</div>
      <div style={lineStyle}>{(E.hand === 'RH' ? t('Right hand. ', '오른손. ') : t('Left hand. ', '왼손. ')) + t(E.text[0], E.text[1])}</div>
      <ScKeys nums ks={P.K} marks={P.marks} names={P.names} ncol={P.ncol} arcs={[]} nonce={nonce + ':' + i}/>
      {row(<>
        <button className="ghost-btn" style={{...KF_BTN,minWidth:110}} onClick={() => { if (i === 0) setView('all'); else { setI(i - 1); setNonce(n => n + 1); } }}>{t('← Back', '← 이전')}</button>
        <button className="ghost-btn" style={prim} onClick={() => { if (i === last) { setView('cmp'); setNonce(n => n + 1); } else { setI(i + 1); setNonce(n => n + 1); } }}>{t('Next →', '다음 →')}</button>
      </>)}
    </>;
  } else if (view === 'cmp') {
    body = <>
      <div style={titleStyle}>{title}</div>
      <div style={lineStyle}>{t('C, G, D, A and E share one fingering. F and B each have one hand that is different (≠).', 'C, G, D, A, E는 운지가 같아요. F와 B는 한 손씩 달라요(≠).')}</div>
      <ScStrip rows={[{ keys: 'C G D A E', key: 'C', hand: 'RH' }, { keys: 'C G D A E', key: 'C', hand: 'LH' }, { keys: 'F', key: 'F', hand: 'RH', odd: true }, { keys: 'F', key: 'F', hand: 'LH' }, { keys: 'B', key: 'B', hand: 'RH' }, { keys: 'B', key: 'B', hand: 'LH', odd: true }]}/>
      {row(<>
        <button className="ghost-btn" style={{...KF_BTN,minWidth:110}} onClick={() => { setView('one'); setI(last); setNonce(n => n + 1); }}>{t('← Back', '← 이전')}</button>
        <button className="ghost-btn" style={prim} onClick={() => { setView('try'); newRound(); }}>{t('Your turn →', '내가 해보기 →')}</button>
      </>)}
    </>;
  } else {
    const done = at >= seq.length, cur = done ? null : seq[at], [ck, ch] = cur ? cur.split(':') : ['C', 'RH'];
    const odd = cur ? SC_ODD_SET.includes(cur) : false, P = paint(ck, ch), N = scNames(ck);
    const handWord = ch === 'RH' ? t('right hand', '오른손') : t('left hand', '왼손'), handKo = ch === 'RH' ? '오른손' : '왼손';
    const answer = (v) => { if (given != null || done) return; setGiven(v); if ((v === 'odd') === odd) setScore(x => x + 1); setNonce(n => n + 1); };
    const line = done ? t('Only two are different: the right hand of F and the left hand of B. You got ' + score + ' of ' + seq.length + '.', '다른 건 둘뿐이에요: F의 오른손과 B의 왼손. ' + seq.length + '개 중 ' + score + '개 맞았어요.')
      : given == null ? t('The ' + handWord + ' of ' + N[0] + ' major: the standard shape, or different? (' + (at + 1) + '/' + seq.length + ')', N[0] + ' 장음계 ' + handKo + ': 기본 모양일까요, 다를까요? (' + (at + 1) + '/' + seq.length + ')')
      : ((given === 'odd') === odd ? t('Yes. ', '맞아요. ') : t('Not quite. ', '아니에요. ')) + (odd ? t('It is different.', '달라요.') : t('It is the standard shape.', '기본 모양이에요.'));
    body = <>
      <div style={titleStyle}>{t('Your turn', '내가 해보기')}</div>
      <div style={lineStyle}>{line}</div>
      {!done && <ScKeys nums ks={P.K} marks={given != null ? P.marks : { [P.K[0]]: 'pick' }} names={given != null ? P.names : {}} ncol={P.ncol} arcs={[]} nonce={nonce + cur}/>}
      {!done && given == null && <div style={{display:'grid',gridTemplateColumns:'repeat(2,minmax(0,1fr))',gap:8,maxWidth:330,margin:'12px auto 0'}}>
        <button className="ghost-btn" style={{...KF_BTN,minHeight:48}} onClick={() => answer('std')}>{t('Standard', '기본 모양')}</button>
        <button className="ghost-btn" style={{...KF_BTN,minHeight:48}} onClick={() => answer('odd')}>{t('Different', '달라요')}</button>
      </div>}
      {row(<>
        <button className="ghost-btn" style={{...KF_BTN,minWidth:110}} onClick={() => { setView('cmp'); setNonce(n => n + 1); }}>{t('← Back', '← 이전')}</button>
        {given != null && !done && <button className="ghost-btn" style={prim} onClick={() => { setAt(at + 1); setGiven(null); setNonce(n => n + 1); }}>{t('Next →', '다음 →')}</button>}
        {done && <button className="ghost-btn" style={prim} onClick={() => newRound()}>{t('Again', '다시 하기')}</button>}
      </>)}
    </>;
  }
  return <div className="try-box" data-sc-lesson="finger" style={{background:'#fff',border:'1px solid var(--border)',borderRadius:10,padding:'10px 10px 12px',margin:'4px 0 16px'}}>{body}</div>;
}
// ─── Lesson 5 (was 6): the keys that start on a black key. Her text (SCALE_PATTERNS): the thumb only ever plays white keys; in all four keys the
// right-hand thumbs go on C and F; the left hand is one shape for all four: 3-2-1, 4-3-2-1, 3; G♭ / F♯: three black keys in a row, fingers 2-3-4,
// both thumbs on the only two white keys, C♭ (B) and F. First one strip: the same groups of 3 and 4, in another order.
const SC_BLK = [
  { key: 'Bb', hand: 'RH', text: ['B♭ major starts on a black key. The thumb only ever plays white keys: here C and F.', 'B♭ 장음계는 검은건반에서 시작해요. 엄지는 흰건반만 쳐요: 여기서는 C와 F.'] },
  { key: 'Eb', hand: 'RH', text: ['E♭ major: again the right-hand thumbs are on C and F.', 'E♭ 장음계: 오른손 엄지는 이번에도 C와 F예요.'] },
  { key: 'Ab', hand: 'RH', text: ['A♭ major: the right-hand thumbs are on C and F.', 'A♭ 장음계: 오른손 엄지는 C와 F예요.'] },
  { key: 'Db', hand: 'RH', text: ['D♭ major: the right-hand thumbs are on C and F.', 'D♭ 장음계: 오른손 엄지는 C와 F예요.'] },
  { key: 'Bb', hand: 'LH', text: ['The left hand is one shape for all four keys: 3-2-1, 4-3-2-1, 3.', '왼손은 네 조 모두 한 가지 모양이에요: 3-2-1, 4-3-2-1, 3.'] },
  { key: 'Gb', hand: 'RH', text: ['G♭ / F♯: three black keys in a row. Fingers 2, 3, 4 cover them; the thumbs land on the only two white keys, C♭ (B) and F.', 'G♭ / F♯: 나란히 있는 검은건반 세 개. 2, 3, 4번이 그 셋을 맡고, 엄지는 단 두 개뿐인 흰건반 C♭(B)과 F에 놓여요.'] },
];
function ScBlack() {
  const [view, setView] = useState('all');   // 'all' (the strips) -> 'one' -> 'try'
  const [i, setI] = useState(0), [nonce, setNonce] = useState(0), [kk, setKk] = useState('Bb'), [hand, setHand] = useState('RH');
  const [found, setFound] = useState([]), [bad, setBad] = useState(null), [why, setWhy] = useState('');
  const timers = useRef([]);
  const clear = () => { timers.current.forEach(clearTimeout); timers.current = []; };
  useEffect(() => clear, []);
  const titleStyle = {textAlign:'center',fontFamily:"'Playfair Display', Georgia, serif",fontSize:22,fontWeight:900,color:'#26296b',lineHeight:1.2,margin:'0 0 8px',textWrap:'balance'};
  const lineStyle = {textAlign:'center',fontSize:15,fontWeight:800,color:'#26296b',margin:'8px 0 6px',minHeight:42,textWrap:'balance',wordBreak:'keep-all'};
  const prim = {...KF_BTN,minWidth:140,background:'#26296b',color:'#fffefa',borderColor:'#26296b'};
  const row = (children) => <div style={{textAlign:'center',marginTop:14,display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap'}}>{children}</div>;
  const title = t('Fingering from a black key', '검은건반에서 시작하는 운지');
  const paint = (key, h) => { const K = scIdx(key), marks = {}, names = {}, ncol = {}; scPaint(key, h, K, 8, marks, names, ncol); return { K, marks, names, ncol }; };
  const reset = () => { setFound([]); setBad(null); setWhy(''); setNonce(n => n + 1); };
  let body;
  if (view === 'all') {
    body = <>
      <div style={titleStyle}>{title}</div>
      <div style={lineStyle}>{t('The same groups of 3 and 4, in another order. The thumb only ever plays white keys.', '같은 3개, 4개 묶음이 순서만 바뀌어요. 엄지는 흰건반만 쳐요.')}</div>
      <ScStrip rows={[{ keys: 'B♭', key: 'Bb', hand: 'RH' }, { keys: 'E♭', key: 'Eb', hand: 'RH' }, { keys: 'A♭', key: 'Ab', hand: 'RH' }, { keys: 'D♭', key: 'Db', hand: 'RH' }, { keys: 'B♭ E♭ A♭ D♭', key: 'Bb', hand: 'LH' }]}/>
      {row(<button className="ghost-btn" style={prim} onClick={() => { setView('one'); setI(0); setNonce(n => n + 1); }}>{t('One by one →', '하나씩 →')}</button>)}
    </>;
  } else if (view === 'one') {
    const E = SC_BLK[i], P = paint(E.key, E.hand);
    body = <>
      <div style={titleStyle}>{title}</div>
      <div style={lineStyle}>{(E.hand === 'RH' ? t('Right hand. ', '오른손. ') : t('Left hand. ', '왼손. ')) + t(E.text[0], E.text[1])}</div>
      <ScKeys nums ks={P.K} marks={P.marks} names={P.names} ncol={P.ncol} arcs={[]} nonce={nonce + ':' + i}/>
      {row(<>
        <button className="ghost-btn" style={{...KF_BTN,minWidth:110}} onClick={() => { if (i === 0) setView('all'); else { setI(i - 1); setNonce(n => n + 1); } }}>{t('← Back', '← 이전')}</button>
        <button className="ghost-btn" style={prim} onClick={() => { if (i === SC_BLK.length - 1) { setView('try'); reset(); } else { setI(i + 1); setNonce(n => n + 1); } }}>{i === SC_BLK.length - 1 ? t('Your turn →', '내가 해보기 →') : t('Next →', '다음 →')}</button>
      </>)}
    </>;
  } else {
    const K = scIdx(kk), F = SCALES[kk].octaves[1][hand], N = scNames(kk), thumbs = F.map((f, j) => f === 1 ? K[j] : null).filter(x => x != null);
    const done = found.length >= thumbs.length, P = paint(kk, hand), marks = {}, names = {}, ncol = {};
    if (done) Object.assign(marks, P.marks), Object.assign(names, P.names), Object.assign(ncol, P.ncol);
    found.forEach(k => { marks[k] = 'good'; names[k] = '1'; ncol[k] = '#2e8a6e'; });
    if (bad != null) marks[bad] = 'bad';
    const handWord = hand === 'RH' ? t('right hand', '오른손') : t('left hand', '왼손'), handKo = hand === 'RH' ? '오른손' : '왼손';
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
      <ScKeys nums ks={K} marks={marks} names={names} ncol={ncol} arcs={[]} nonce={nonce + kk + hand} onTap={tap}/>
      {row(<>
        <button className="ghost-btn" style={{...KF_BTN,minWidth:110}} onClick={() => { clear(); setView('one'); setI(SC_BLK.length - 1); setNonce(n => n + 1); }}>{t('← Back', '← 이전')}</button>
        {done && <button className="ghost-btn" style={prim} onClick={() => reset()}>{t('Again', '다시 하기')}</button>}
      </>)}
    </>;
  }
  return <div className="try-box" data-sc-lesson="black" style={{background:'#fff',border:'1px solid var(--border)',borderRadius:10,padding:'10px 10px 12px',margin:'4px 0 16px'}}>{body}</div>;
}
"""
s = s[:a] + NEW + s[b:]
rep(""" ['sc-finger', 'The standard fingering', '기본 운지', 'Right hand 1 2 3, 1 2 3 4, 5. Left hand: the mirror.', '오른손 1 2 3, 1 2 3 4, 5. 왼손은 거울.', ScFinger],
 ['sc-odd', 'White keys: two are different', '흰건반에서 시작: 둘은 달라요', 'F and B: one hand each.', 'F와 B: 한 손씩.', ScOdd],
 ['sc-black', 'Starting on a black key', '검은건반에서 시작하기', 'The thumb only ever plays white keys.', '엄지는 흰건반만 쳐요.', ScBlack]]""",
""" ['sc-finger', 'Fingering from a white key', '흰건반에서 시작하는 운지', 'The standard shape, and the two hands that differ.', '기본 모양, 그리고 다른 두 손.', ScFinger],
 ['sc-black', 'Fingering from a black key', '검은건반에서 시작하는 운지', 'The same groups, another order. The thumb plays white keys.', '같은 묶음, 다른 순서. 엄지는 흰건반.', ScBlack]]""")
rep("lessons: ['sc-shape', 'sc-same', 'sc-deg', 'sc-finger', 'sc-odd', 'sc-black'], check: 'scales'", "lessons: ['sc-shape', 'sc-same', 'sc-deg', 'sc-finger', 'sc-black'], check: 'scales'")
open(sys.argv[2],'w',encoding='utf-8').write(s)
