import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
NEW = r"""
// lesson 5: the natural. A sign changed the key; the natural brings back the plain white key.
const AC_NAT = [   // a: the key with a sign, b: its plain white key, sg: the sign
  { a: 6, b: 5, sg: '♯' }, { a: 10, b: 11, sg: '♭' }, { a: 1, b: 0, sg: '♯' }, { a: 3, b: 4, sg: '♭' }, { a: 8, b: 7, sg: '♯' }, { a: 8, b: 9, sg: '♭' },
];
function AcNatural() {
  const L = (k) => PC_INFO[((k % 12) + 12) % 12].names[0];
  const [view, setView] = useState('all');   // 'all' -> 'one' -> 'try'
  const [i, setI] = useState(0), [shown, setShown] = useState(false), [nonce, setNonce] = useState(0);
  const [c, setC] = useState(0), [done, setDone] = useState(false), [miss, setMiss] = useState(false);
  const timers = useRef([]);
  const clear = () => { timers.current.forEach(clearTimeout); timers.current = []; };
  useEffect(() => clear, []);
  const snd = (k, d) => { if (k >= 0) playKey(k, d); };
  const sgW = (sg) => sg === '♯' ? t('sharp', '샵') : t('flat', '플랫');
  const nm = (e) => L(e.b) + e.sg;                       // the name of the key with the sign, e.g. F♯ (the white letter it hangs from)
  const show = (idx) => { clear(); setI(idx); setShown(false); setNonce(n => n + 1); const e = AC_NAT[idx]; snd(e.a, 0.45); timers.current.push(setTimeout(() => { setShown(true); snd(e.b, 0.6); }, 750)); };
  const enLine = (e) => nm(e) + ' ' + '♮ = ' + L(e.b) + '. The natural cancels the ' + (e.sg === '♯' ? 'sharp' : 'flat') + ': back to the plain white key.';
  const koLine = (e) => nm(e) + ' ♮ = ' + L(e.b) + '. 내추럴이 ' + (e.sg === '♯' ? '샵' : '플랫') + '을 취소해요: 다시 원래 흰건반이에요.';
  const titleStyle = {textAlign:'center',fontFamily:"'Playfair Display', Georgia, serif",fontSize:22,fontWeight:900,color:'#26296b',lineHeight:1.2,margin:'0 0 8px',textWrap:'balance'};
  const lineStyle = {textAlign:'center',fontSize:15,fontWeight:800,color:'#26296b',margin:'8px 0 6px',minHeight:42,textWrap:'balance',wordBreak:'keep-all'};
  const prim = {...KF_BTN,minWidth:140,background:'#26296b',color:'#fffefa',borderColor:'#26296b'};
  const row = (children) => <div style={{textAlign:'center',marginTop:14,display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap'}}>{children}</div>;
  const title = t('The natural ♮', '내추럴 ♮');
  let body;
  if (view === 'all') {
    const arcs = [], names = {};
    [[1, 0], [1, 2], [3, 2], [3, 4], [6, 5], [6, 7], [8, 7], [8, 9], [10, 9], [10, 11]].forEach(([a, b]) => { arcs.push([a, b, false]); });
    [0, 2, 4, 5, 7, 9, 11].forEach(k => { names[k] = L(k) + '♮'; });
    body = <>
      <div style={titleStyle}>{title}</div>
      <AcKeys marks={{}} arcs={arcs} names={names} nonce="all" stagger topRoom={46}/>
      <div style={lineStyle}>{t('Natural (♮) = the plain white key again. It cancels a sharp or a flat.', '내추럴(♮) = 다시 원래 흰건반. 샵이나 플랫을 취소해요.')}</div>
      {row(<button className="ghost-btn" style={prim} onClick={() => { setView('one'); show(0); }}>{t('One by one →', '하나씩 →')}</button>)}
    </>;
  } else if (view === 'one') {
    const e = AC_NAT[i], marks = { [e.a]: 'pass' }; if (shown) marks[e.b] = 'pick';
    const names = { [e.a]: nm(e) }; if (shown) names[e.b] = L(e.b) + '♮';
    body = <>
      <div style={titleStyle}>{title}</div>
      <AcKeys marks={marks} arcs={shown ? [[e.a, e.b, true]] : []} names={names} nonce={nonce}/>
      <div style={lineStyle}>{shown ? t(enLine(e), koLine(e)) : ''}</div>
      {row(<>
        <button className="ghost-btn" style={{...KF_BTN,minWidth:110}} onClick={() => { clear(); if (i === 0) setView('all'); else show(i - 1); }}>{t('← Back', '← 이전')}</button>
        <button className="ghost-btn" style={prim} onClick={() => { clear(); if (i === AC_NAT.length - 1) { setView('try'); setC(0); setDone(false); setMiss(false); setNonce(n => n + 1); } else show(i + 1); }}>{i === AC_NAT.length - 1 ? t('Your turn →', '내가 해보기 →') : t('Next →', '다음 →')}</button>
      </>)}
    </>;
  } else {
    const e = AC_NAT[c];
    const marks = { [e.a]: 'pass' }; if (done) marks[e.b] = 'pick';
    const names = { [e.a]: nm(e) }; if (done) names[e.b] = L(e.b) + '♮';
    const tap = (k) => {
      if (done) return; clear(); snd(k, 0.5);
      if (k === e.b) { setDone(true); setMiss(false); setNonce(n => n + 1); } else { setMiss(true); }
    };
    const line = done ? t(enLine(e), koLine(e))
      : miss ? t('Not that one. Where is the plain ' + L(e.b) + '?', '그 건반이 아니에요. 원래 ' + L(e.b) + '는 어디일까요?')
      : t('Tap the natural: ' + nm(e) + ' ♮', '내추럴을 눌러요: ' + nm(e) + ' ♮');
    body = <>
      <div style={titleStyle}>{t('Your turn', '내가 해보기')}</div>
      <AcKeys marks={marks} arcs={done ? [[e.a, e.b, true]] : []} names={names} nonce={nonce} onTap={tap}/>
      <div style={lineStyle}>{line}</div>
      {done && row(<button className="ghost-btn" style={prim} onClick={() => { setC((c + 1) % AC_NAT.length); setDone(false); setMiss(false); setNonce(n => n + 1); }}>{t('Another →', '하나 더 →')}</button>)}
      {row(<button className="ghost-btn" style={{...KF_BTN,minWidth:110}} onClick={() => { clear(); setView('one'); show(AC_NAT.length - 1); }}>{t('← Back', '← 이전')}</button>)}
    </>;
  }
  return <div className="try-box" data-ac-lesson="natural" style={{background:'#fff',border:'1px solid var(--border)',borderRadius:10,padding:'10px 10px 12px',margin:'4px 0 16px'}}>{body}</div>;
}
[['ac-natural', 'The natural ♮', '내추럴 ♮', 'Back to the plain white key.', '다시 원래 흰건반으로.']].forEach(([id, en, ko, benEn, bko]) => {
  TOOLS.push({ id, ch: 'concept', title: en, blurb: benEn, hidden: true, get kicker() { return TOOL_AREAS.find(a => a.id === 'pitch').name + ' · ' + (LANG === 'ko' ? '임시표' : 'Accidentals'); }, C: () => <AcNatural/> });
  TOOL_KO[id] = [ko, bko];
  const tl = TOOLS[TOOLS.length - 1], k = TOOL_KO[id], ti = tl.title, bl = tl.blurb; tl.titleEn = ti; tl.blurbEn = bl;
  Object.defineProperty(tl, 'title', { get: () => (LANG === 'ko' ? k[0] : ti), enumerable: true, configurable: true });
  Object.defineProperty(tl, 'blurb', { get: () => (LANG === 'ko' ? k[1] : bl), enumerable: true, configurable: true });
  TOOL_CONCEPT[id] = 'p-clock';
});
"""
rep("// the Toolbox: a concept's book, right under its name (open on screen, or print)\nfunction CbCard(", NEW + "// the Toolbox: a concept's book, right under its name (open on screen, or print)\nfunction CbCard(")
rep("'ac-flat', 'sac-signs', 'cl-natural', 'sac-natural',", "'ac-flat', 'ac-natural', 'sac-signs', 'sac-natural',")
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
