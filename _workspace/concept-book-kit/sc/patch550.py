import sys
s=open(sys.argv[1],encoding='utf-8').read()
a=s.index("// Phase 545: Accidentals, lesson 1 (rebuilt like the key signatures)")
b=s.index("// the Toolbox: a concept's book, right under its name (open on screen, or print)\nfunction CbCard(")
new=r"""// Phase 547: Accidentals, lessons 1 and 2 (rebuilt like the key signatures): the half step = semitone, the whole step = tone. The whole picture, then one by one, then her turn.
const AC_STEP = {
  half: { size: 1, title: ['The half step = semitone', '반음 = semitone'],
    all: ['A half step (semitone) is the very next key.', '반음(semitone)은 바로 옆 건반이에요.'],
    ex: [
      { a: 0, b: 1, en: 'From C, the very next key up is black.', ko: 'C에서 바로 위 건반은 검은건반이에요.' },
      { a: 4, b: 5, en: 'E to F: no black key between, but still the very next key.', ko: 'E에서 F: 사이에 검은건반이 없어도 바로 옆 건반이에요.' },
      { a: 2, b: 1, en: 'Down is a half step too.', ko: '아래로 내려가도 반음이에요.' },
      { a: 6, b: 7, en: 'From a black key up to a white one: a half step too.', ko: '검은건반에서 흰건반으로 올라가도 반음이에요.' },
      { a: 11, b: 12, en: 'B to C: no black key between either.', ko: 'B에서 C도 사이에 검은건반이 없어요.' },
    ], up: ['↑ Half step up', '↑ 반음 위로'], down: ['↓ Half step down', '↓ 반음 아래로'], word: ['a half step', '반음'] },
  whole: { size: 2, title: ['The whole step = tone', '온음 = tone'],
    all: ['A whole step (tone) is two half steps: skip one key.', '온음(tone)은 반음 두 개예요: 건반 하나를 건너뛰어요.'],
    ex: [
      { a: 0, b: 2, en: 'From C, skip the black key: D. A whole step.', ko: 'C에서 검은건반을 건너뛰면 D. 온음이에요.' },
      { a: 4, b: 6, en: 'From E, skip F: a black key. A whole step.', ko: 'E에서 F를 건너뛰면 검은건반. 온음이에요.' },
      { a: 1, b: 3, en: 'Black to black can be a whole step too.', ko: '검은건반에서 검은건반도 온음일 수 있어요.' },
      { a: 7, b: 5, en: 'Down is a whole step too.', ko: '아래로 내려가도 온음이에요.' },
      { a: 9, b: 11, en: 'A to B: skip the black key between.', ko: 'A에서 B: 사이의 검은건반을 건너뛰어요.' },
    ], up: ['↑ Whole step up', '↑ 온음 위로'], down: ['↓ Whole step down', '↓ 온음 아래로'], word: ['a whole step', '온음'] },
};
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
function AcStep({ kind }) {
  const D = AC_STEP[kind], EX = D.ex, SZ = D.size;
  const [view, setView] = useState('all');   // 'all' -> 'one' -> 'try'
  const [i, setI] = useState(0), [shown, setShown] = useState(false), [nonce, setNonce] = useState(0);
  const [from, setFrom] = useState(null), [to, setTo] = useState(null);   // her turn: the key she stands on, and where the button took her
  const timers = useRef([]);
  const clear = () => { timers.current.forEach(clearTimeout); timers.current = []; };
  useEffect(() => clear, []);
  const snd = (k, d) => { if (k >= 0) playKey(k, d); };
  const show = (idx) => { clear(); setI(idx); setShown(false); setNonce(n => n + 1); const e = EX[idx]; snd(e.a, 0.45);
    timers.current.push(setTimeout(() => { setShown(true); snd(e.b, 0.6); }, 750)); };
  const titleStyle = {textAlign:'center',fontFamily:"'Playfair Display', Georgia, serif",fontSize:22,fontWeight:900,color:'#26296b',lineHeight:1.2,margin:'0 0 8px',textWrap:'balance'};
  const lineStyle = {textAlign:'center',fontSize:15,fontWeight:800,color:'#26296b',margin:'8px 0 6px',minHeight:42,textWrap:'balance',wordBreak:'keep-all'};
  const prim = {...KF_BTN,minWidth:140,background:'#26296b',color:'#fffefa',borderColor:'#26296b'};
  const row = (children) => <div style={{textAlign:'center',marginTop:14,display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap'}}>{children}</div>;
  const title = t(D.title[0], D.title[1]);
  let body;
  if (view === 'all') {
    const arcs = []; if (SZ === 1) { for (let k = -1; k <= 11; k++) arcs.push([k, k + 1, false]); } else { for (let k = 0; k <= 10; k += 2) arcs.push([k, k + 2, false]); }
    body = <>
      <div style={titleStyle}>{title}</div>
      <AcKeys marks={{}} arcs={arcs} nonce="all"/>
      <div style={lineStyle}>{t(D.all[0], D.all[1])}</div>
      {row(<button className="ghost-btn" style={prim} onClick={() => { setView('one'); show(0); }}>{t('One by one →', '하나씩 →')}</button>)}
    </>;
  } else if (view === 'one') {
    const e = EX[i], marks = { [e.a]: 'pass' }; if (shown) marks[e.b] = 'pick';
    body = <>
      <div style={titleStyle}>{title}</div>
      <AcKeys marks={marks} arcs={shown ? [[e.a, e.b, true]] : []} nonce={nonce}/>
      <div style={lineStyle}>{shown ? t(e.en, e.ko) : ''}</div>
      {row(<>
        <button className="ghost-btn" style={{...KF_BTN,minWidth:110}} onClick={() => { clear(); if (i === 0) setView('all'); else show(i - 1); }}>{t('← Back', '← 이전')}</button>
        <button className="ghost-btn" style={prim} onClick={() => { clear(); if (i === EX.length - 1) { setView('try'); setFrom(null); setTo(null); setNonce(n => n + 1); } else show(i + 1); }}>{i === EX.length - 1 ? t('Your turn →', '내가 해보기 →') : t('Next →', '다음 →')}</button>
      </>)}
    </>;
  } else {
    // her turn: tap a key to stand on it (pale), then press Up or Down: only that one move is drawn, the arrival strong
    const marks = {}, arcs = [];
    if (from != null) marks[from] = 'pass';
    if (from != null && to != null) { marks[to] = 'pick'; arcs.push([from, to, true]); }
    const can = (d) => from != null && from + d * SZ >= -1 && from + d * SZ <= 12;
    const go = (d) => { if (!can(d)) return; clear(); const k = from + d * SZ; setTo(k); setNonce(n => n + 1); snd(from, 0.4); timers.current.push(setTimeout(() => snd(k, 0.6), 450)); };
    const nm = from != null && from >= 0 && PC_INFO[from % 12].white ? PC_INFO[from % 12].names[0] : (from === -1 ? 'B' : null);
    const line = from == null ? t('Tap a key to stand on. Then press up or down.', '서 있을 건반을 눌러요. 그다음 위나 아래를 눌러요.')
      : to == null ? t('Now press up or down.', '이제 위나 아래를 눌러요.')
      : t((nm ? 'From ' + nm : 'From this key') + ', ' + D.word[0] + (to > from ? ' up.' : ' down.'), (nm ? nm + '에서 ' : '이 건반에서 ') + D.word[1] + (to > from ? ' 위로.' : ' 아래로.'));
    const bs = (d) => ({...KF_BTN,minWidth:132,opacity:can(d) ? 1 : 0.4});
    body = <>
      <div style={titleStyle}>{t('Your turn', '내가 해보기')}</div>
      <AcKeys marks={marks} arcs={arcs} nonce={nonce} onTap={(k) => { clear(); setFrom(k); setTo(null); setNonce(n => n + 1); snd(k, 0.5); }}/>
      <div style={lineStyle}>{line}</div>
      {row(<>
        <button className="ghost-btn" style={bs(-1)} disabled={!can(-1)} onClick={() => go(-1)}>{t(D.down[0], D.down[1])}</button>
        <button className="ghost-btn" style={bs(1)} disabled={!can(1)} onClick={() => go(1)}>{t(D.up[0], D.up[1])}</button>
      </>)}
      {row(<button className="ghost-btn" style={{...KF_BTN,minWidth:110}} onClick={() => { clear(); setView('one'); show(EX.length - 1); }}>{t('← Back', '← 이전')}</button>)}
    </>;
  }
  return <div className="try-box" data-ac-lesson={kind} style={{background:'#fff',border:'1px solid var(--border)',borderRadius:10,padding:'10px 10px 12px',margin:'4px 0 16px'}}>{body}</div>;
}
[['ac-half', 'half', 'Half step = semitone', '반음 = semitone', 'The very next key, up or down.', '바로 옆 건반, 위로 또는 아래로.'],
 ['ac-whole', 'whole', 'Whole step = tone', '온음 = tone', 'Two half steps: skip one key.', '반음 두 개: 건반 하나를 건너뛰어요.']].forEach(([id, kind, en, ko, benEn, bko]) => {
  TOOLS.push({ id, ch: 'concept', title: en, blurb: benEn, hidden: true, get kicker() { return TOOL_AREAS.find(a => a.id === 'pitch').name + ' · ' + (LANG === 'ko' ? '임시표' : 'Accidentals'); }, C: () => <AcStep kind={kind}/> });
  TOOL_KO[id] = [ko, bko];
  const tl = TOOLS[TOOLS.length - 1], k = TOOL_KO[id], ti = tl.title, bl = tl.blurb; tl.titleEn = ti; tl.blurbEn = bl;
  Object.defineProperty(tl, 'title', { get: () => (LANG === 'ko' ? k[0] : ti), enumerable: true, configurable: true });
  Object.defineProperty(tl, 'blurb', { get: () => (LANG === 'ko' ? k[1] : bl), enumerable: true, configurable: true });
  TOOL_CONCEPT[id] = 'p-clock';
});
"""
s=s[:a]+new+s[b:]
def rep(x,y,n=1):
    global s
    assert s.count(x)==n,(x[:90],s.count(x)); s=s.replace(x,y)
rep("lessons: ['ac-half', 'cl-sharp',", "lessons: ['ac-half', 'ac-whole', 'cl-sharp',")
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
