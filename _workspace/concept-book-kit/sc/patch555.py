import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
rep("function AcKeys({ marks, onTap, arcs, nonce }) {", "function AcKeys({ marks, onTap, arcs, nonce, names }) {")
rep("<TapKeyboard octaves={1} extraB extraC labels=\"white\" marks={marks} onTap={onTap} overlay=", "<TapKeyboard octaves={1} extraB extraC labels=\"white\" marks={marks} names={names} onTap={onTap} overlay=")
rep("[['ac-half', 'half', 'Half step = semitone',",
r"""// Phase 552: Accidentals, lesson 3 (and the flat, lesson 4, from the same table): the sharp. The whole picture, one at a time, then her turn.
const AC_SIGN = {
  sharp: { dir: 1, sym: '♯', title: ['The sharp ♯', '샵 ♯'],
    all: ['Sharp (♯) = one half step up: the very next key to the right.', '샵(♯) = 반음 위: 바로 오른쪽 건반이에요.'],
    order: [0, 5, 9, 2, 7], btn: ['♯ Sharp →', '♯ 샵 →'], word: ['sharp', '샵'], above: ['above', '위'] },
};
function AcSign({ kind }) {
  const D = AC_SIGN[kind], dir = D.dir, sym = D.sym;
  const L = (k) => PC_INFO[((k % 12) + 12) % 12].names[0];   // the white key's letter
  const isW = (k) => PC_INFO[((k % 12) + 12) % 12].white;
  const target = (k) => k + dir;
  const ok = (k) => k != null && k >= 0 && k <= 11 && isW(k) && target(k) >= 0 && target(k) <= 11 && !isW(target(k));   // a white key with a black key right beside it on that side
  const pairs = [0, 2, 4, 5, 7, 9, 11].filter(ok).map(k => [k, target(k)]);
  const nameOf = (k) => L(k) + sym;
  const en = (k) => nameOf(k) + ' (' + L(k) + ' ' + D.word[0] + '): one half step ' + D.above[0] + ' ' + L(k) + '.';
  const ko = (k) => nameOf(k) + '(' + L(k) + ' ' + D.word[1] + '): ' + L(k) + '보다 반음 ' + D.above[1] + '예요.';
  const [view, setView] = useState('all');   // 'all' -> 'one' -> 'try'
  const [i, setI] = useState(0), [shown, setShown] = useState(false), [nonce, setNonce] = useState(0);
  const [from, setFrom] = useState(null), [to, setTo] = useState(null);
  const timers = useRef([]);
  const clear = () => { timers.current.forEach(clearTimeout); timers.current = []; };
  useEffect(() => clear, []);
  const snd = (k, d) => { if (k >= 0) playKey(k, d); };
  const EX = D.order.map(k => ({ a: k, b: target(k) }));
  const show = (idx) => { clear(); setI(idx); setShown(false); setNonce(n => n + 1); const e = EX[idx]; snd(e.a, 0.45); timers.current.push(setTimeout(() => { setShown(true); snd(e.b, 0.6); }, 750)); };
  const titleStyle = {textAlign:'center',fontFamily:"'Playfair Display', Georgia, serif",fontSize:22,fontWeight:900,color:'#26296b',lineHeight:1.2,margin:'0 0 8px',textWrap:'balance'};
  const lineStyle = {textAlign:'center',fontSize:15,fontWeight:800,color:'#26296b',margin:'8px 0 6px',minHeight:42,textWrap:'balance',wordBreak:'keep-all'};
  const prim = {...KF_BTN,minWidth:140,background:'#26296b',color:'#fffefa',borderColor:'#26296b'};
  const row = (children) => <div style={{textAlign:'center',marginTop:14,display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap'}}>{children}</div>;
  const title = t(D.title[0], D.title[1]);
  let body;
  if (view === 'all') {
    const names = {}; pairs.forEach(([a, b]) => { names[b] = nameOf(a); });
    body = <>
      <div style={titleStyle}>{title}</div>
      <AcKeys marks={{}} arcs={pairs.map(([a, b]) => [a, b, false])} names={names} nonce="all"/>
      <div style={lineStyle}>{t(D.all[0], D.all[1])}</div>
      {row(<button className="ghost-btn" style={prim} onClick={() => { setView('one'); show(0); }}>{t('One by one →', '하나씩 →')}</button>)}
    </>;
  } else if (view === 'one') {
    const e = EX[i], marks = { [e.a]: 'pass' }; if (shown) marks[e.b] = 'pick';
    body = <>
      <div style={titleStyle}>{title}</div>
      <AcKeys marks={marks} arcs={shown ? [[e.a, e.b, true]] : []} names={shown ? { [e.b]: nameOf(e.a) } : {}} nonce={nonce}/>
      <div style={lineStyle}>{shown ? t(en(e.a), ko(e.a)) : ''}</div>
      {row(<>
        <button className="ghost-btn" style={{...KF_BTN,minWidth:110}} onClick={() => { clear(); if (i === 0) setView('all'); else show(i - 1); }}>{t('← Back', '← 이전')}</button>
        <button className="ghost-btn" style={prim} onClick={() => { clear(); if (i === EX.length - 1) { setView('try'); setFrom(null); setTo(null); setNonce(n => n + 1); } else show(i + 1); }}>{i === EX.length - 1 ? t('Your turn →', '내가 해보기 →') : t('Next →', '다음 →')}</button>
      </>)}
    </>;
  } else {
    const marks = {}, arcs = [], names = {};
    if (from != null) marks[from] = 'pass';
    if (from != null && to != null) { marks[to] = 'pick'; arcs.push([from, to, true]); names[to] = nameOf(from); }
    const go = () => { if (!ok(from)) return; clear(); setTo(target(from)); setNonce(n => n + 1); snd(from, 0.4); timers.current.push(setTimeout(() => snd(target(from), 0.6), 450)); };
    const line = from == null ? t('Tap a white key. Then press ' + D.word[0] + '.', '흰건반을 눌러요. 그다음 ' + D.word[1] + '을 눌러요.')
      : to != null ? t(en(from), ko(from))
      : !isW(from) ? t('Tap a white key.', '흰건반을 눌러요.')
      : !ok(from) ? t('No black key right beside this one. Try another.', '바로 옆에 검은건반이 없어요. 다른 건반을 눌러 봐요.')
      : t('Now press ' + D.word[0] + '.', '이제 ' + D.word[1] + '을 눌러요.');
    body = <>
      <div style={titleStyle}>{t('Your turn', '내가 해보기')}</div>
      <AcKeys marks={marks} arcs={arcs} names={names} nonce={nonce} onTap={(k) => { clear(); setFrom(k); setTo(null); setNonce(n => n + 1); snd(k, 0.5); }}/>
      <div style={lineStyle}>{line}</div>
      {row(<button className="ghost-btn" style={{...KF_BTN,minWidth:150,opacity:ok(from) && to == null ? 1 : 0.4}} disabled={!ok(from) || to != null} onClick={go}>{t(D.btn[0], D.btn[1])}</button>)}
      {row(<button className="ghost-btn" style={{...KF_BTN,minWidth:110}} onClick={() => { clear(); setView('one'); show(EX.length - 1); }}>{t('← Back', '← 이전')}</button>)}
    </>;
  }
  return <div className="try-box" data-ac-lesson={kind} style={{background:'#fff',border:'1px solid var(--border)',borderRadius:10,padding:'10px 10px 12px',margin:'4px 0 16px'}}>{body}</div>;
}
[['ac-sharp', 'sharp', 'The sharp ♯', '샵 ♯', 'One half step up: the very next key to the right.', '반음 위로: 바로 오른쪽 건반.']].forEach(([id, kind, en, ko, benEn, bko]) => {
  TOOLS.push({ id, ch: 'concept', title: en, blurb: benEn, hidden: true, get kicker() { return TOOL_AREAS.find(a => a.id === 'pitch').name + ' · ' + (LANG === 'ko' ? '임시표' : 'Accidentals'); }, C: () => <AcSign kind={kind}/> });
  TOOL_KO[id] = [ko, bko];
  const tl = TOOLS[TOOLS.length - 1], k = TOOL_KO[id], ti = tl.title, bl = tl.blurb; tl.titleEn = ti; tl.blurbEn = bl;
  Object.defineProperty(tl, 'title', { get: () => (LANG === 'ko' ? k[0] : ti), enumerable: true, configurable: true });
  Object.defineProperty(tl, 'blurb', { get: () => (LANG === 'ko' ? k[1] : bl), enumerable: true, configurable: true });
  TOOL_CONCEPT[id] = 'p-clock';
});
[['ac-half', 'half', 'Half step = semitone',""")
rep("lessons: ['ac-half', 'ac-whole', 'cl-sharp',", "lessons: ['ac-half', 'ac-whole', 'ac-sharp',")
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
