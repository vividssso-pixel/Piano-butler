import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)

# Accidentals, lesson 1 rebuilt in the key signatures template: the whole picture, then one at a time, then her turn
rep("// the Toolbox: a concept's book, right under its name (open on screen, or print)\nfunction CbCard(",
r"""// Phase 545: Accidentals, lesson 1 (rebuilt like the key signatures): the half step. The whole picture, then one by one, then her turn.
const AC_HALF_EX = [
  { a: 0, b: 1, en: 'From C, the very next key up is black.', ko: 'C에서 바로 위 건반은 검은건반이에요.' },
  { a: 4, b: 5, en: 'E to F: no black key between, but still the very next key.', ko: 'E에서 F: 사이에 검은건반이 없어도 바로 옆 건반이에요.' },
  { a: 2, b: 1, en: 'Down is a half step too.', ko: '아래로 내려가도 반음이에요.' },
  { a: 6, b: 7, en: 'From a black key up to a white one: a half step too.', ko: '검은건반에서 흰건반으로 올라가도 반음이에요.' },
  { a: 11, b: 12, en: 'B to C: no black key between either.', ko: 'B에서 C도 사이에 검은건반이 없어요.' },
];
// one octave C to C with the B below and the C above, so every key has a neighbour on both sides; arcs [from, to, animate?] drawn over it
function AcKeys({ marks, onTap, arcs, nonce }) {
  const kx = (i) => i === -1 ? 18 : keyCenterX(i) + 36;
  const W = 9 * 36;
  return (<div style={{maxWidth:330,margin:'0 auto'}}>
    <svg viewBox={'-1 0 ' + (W + 2) + ' 30'} style={{width:'100%',display:'block'}} aria-hidden="true">
      {arcs.map(([a, b, anim], j) => { const x1 = kx(a), x2 = kx(b), sp = Math.abs(x2 - x1), cy = 26 - Math.min(28, sp * 0.8 + 6);
        return <path key={j + ':' + a + ':' + b + ':' + nonce} d={'M' + x1 + ',26 Q' + (x1 + x2) / 2 + ',' + cy + ' ' + x2 + ',26'} fill="none" stroke="#e4572e" strokeWidth={anim ? 3 : 1.8} strokeLinecap="round"
          strokeDasharray={anim ? '120' : undefined} strokeDashoffset={anim ? '120' : undefined} style={anim ? {animation:'drawArc 0.45s ease-out forwards'} : undefined}/>; })}
    </svg>
    <TapKeyboard octaves={1} extraB extraC labels="white" marks={marks} onTap={onTap}/>
  </div>);
}
function AcHalf() {
  const [view, setView] = useState('all');   // 'all' -> 'one' -> 'try'
  const [i, setI] = useState(0), [shown, setShown] = useState(false), [pick, setPick] = useState(null), [nonce, setNonce] = useState(0);
  const timers = useRef([]);
  const clear = () => { timers.current.forEach(clearTimeout); timers.current = []; };
  useEffect(() => clear, []);
  const snd = (k, d) => { if (k >= 0) playKey(k, d); };
  const show = (idx) => { clear(); setI(idx); setShown(false); setNonce(n => n + 1); const e = AC_HALF_EX[idx]; snd(e.a, 0.45);
    timers.current.push(setTimeout(() => { setShown(true); snd(e.b, 0.6); }, 750)); };
  const titleStyle = {textAlign:'center',fontFamily:"'Playfair Display', Georgia, serif",fontSize:22,fontWeight:900,color:'#26296b',lineHeight:1.2,margin:'0 0 8px',textWrap:'balance'};
  const lineStyle = {textAlign:'center',fontSize:15,fontWeight:800,color:'#26296b',margin:'8px 0 6px',minHeight:42,textWrap:'balance',wordBreak:'keep-all'};
  const prim = {...KF_BTN,minWidth:140,background:'#26296b',color:'#fffefa',borderColor:'#26296b'};
  const row = (children) => <div style={{textAlign:'center',marginTop:14,display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap'}}>{children}</div>;
  let body;
  if (view === 'all') {
    const all = []; for (let k = -1; k <= 11; k++) all.push([k, k + 1, false]);
    body = <>
      <div style={titleStyle}>{t('The half step', '반음')}</div>
      <AcKeys marks={{}} arcs={all} nonce="all"/>
      <div style={lineStyle}>{t('A half step is the very next key.', '반음은 바로 옆 건반이에요.')}</div>
      {row(<button className="ghost-btn" style={prim} onClick={() => { setView('one'); show(0); }}>{t('One by one →', '하나씩 →')}</button>)}
    </>;
  } else if (view === 'one') {
    const e = AC_HALF_EX[i], marks = { [e.a]: 'pass' }; if (shown) marks[e.b] = 'pick';
    body = <>
      <div style={titleStyle}>{t('The half step', '반음')}</div>
      <AcKeys marks={marks} arcs={shown ? [[e.a, e.b, true]] : []} nonce={nonce}/>
      <div style={lineStyle}>{shown ? t(e.en, e.ko) : ''}</div>
      {row(<>
        <button className="ghost-btn" style={{...KF_BTN,minWidth:110}} onClick={() => { clear(); if (i === 0) setView('all'); else show(i - 1); }}>{t('← Back', '← 이전')}</button>
        <button className="ghost-btn" style={prim} onClick={() => { clear(); if (i === AC_HALF_EX.length - 1) { setView('try'); setPick(null); setNonce(n => n + 1); } else show(i + 1); }}>{i === AC_HALF_EX.length - 1 ? t('Your turn →', '내가 해보기 →') : t('Next →', '다음 →')}</button>
      </>)}
    </>;
  } else {
    const marks = {}, arcs = [];
    if (pick != null) { marks[pick] = 'pick'; [pick - 1, pick + 1].filter(k => k >= -1 && k <= 12).forEach(k => { marks[k] = 'pass'; arcs.push([pick, k, true]); }); }
    body = <>
      <div style={titleStyle}>{t('Your turn', '내가 해보기')}</div>
      <AcKeys marks={marks} arcs={arcs} nonce={nonce} onTap={(k) => { clear(); setPick(k); setNonce(n => n + 1); snd(k, 0.5); [k - 1, k + 1].forEach((q, j) => timers.current.push(setTimeout(() => snd(q, 0.4), 500 + j * 450))); }}/>
      <div style={lineStyle}>{pick == null ? t('Tap any key. Its two nearest keys are a half step away.', '건반을 아무거나 눌러 봐요. 양옆 건반이 반음이에요.') : t('One up, one down: both a half step away.', '위로 하나, 아래로 하나: 둘 다 반음이에요.')}</div>
      {row(<button className="ghost-btn" style={{...KF_BTN,minWidth:110}} onClick={() => { clear(); setView('one'); show(AC_HALF_EX.length - 1); }}>{t('← Back', '← 이전')}</button>)}
    </>;
  }
  return <div className="try-box" data-ac-lesson="half" style={{background:'#fff',border:'1px solid var(--border)',borderRadius:10,padding:'10px 10px 12px',margin:'4px 0 16px'}}>{body}</div>;
}
[['ac-half', 'The half step', '반음', 'The very next key, up or down.', '바로 옆 건반, 위로 또는 아래로.']].forEach(([id, en, ko, benEn, bko]) => {
  TOOLS.push({ id, ch: 'concept', title: en, blurb: benEn, hidden: true, get kicker() { return TOOL_AREAS.find(a => a.id === 'pitch').name + ' · ' + (LANG === 'ko' ? '임시표' : 'Accidentals'); }, C: () => <AcHalf/> });
  TOOL_KO[id] = [ko, bko];
  const tl = TOOLS[TOOLS.length - 1], k = TOOL_KO[id], ti = tl.title, bl = tl.blurb; tl.titleEn = ti; tl.blurbEn = bl;
  Object.defineProperty(tl, 'title', { get: () => (LANG === 'ko' ? k[0] : ti), enumerable: true, configurable: true });
  Object.defineProperty(tl, 'blurb', { get: () => (LANG === 'ko' ? k[1] : bl), enumerable: true, configurable: true });
  TOOL_CONCEPT[id] = 'p-clock';
});
// the Toolbox: a concept's book, right under its name (open on screen, or print)
function CbCard(""")
rep("lessons: ['tone-semitone', 'cl-sharp',", "lessons: ['ac-half', 'cl-sharp',")
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
