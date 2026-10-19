import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
# the double sign glyphs need the music font
rep("""fontSize="16" fontWeight="900" fill={q === 0 ? '#c0431f' : '#2f62c9'} style={{animation:'fadeUp 0.3s both'}}>{tx}</text>)""", """fontSize="16" fontWeight="900" fontFamily={/[𝄪𝄫]/.test(tx) ? MUSIC_FONT : undefined} fill={q === 0 ? '#c0431f' : '#2f62c9'} style={{animation:'fadeUp 0.3s both'}}>{tx}</text>)""")
rep("""textAnchor="middle" fontSize="17" fontWeight="900" fill="#c0431f" style={{animation:'fadeUp 0.3s both'}}>{txt}</text>)}""", """textAnchor="middle" fontSize="17" fontWeight="900" fontFamily={/[𝄪𝄫]/.test(txt) ? MUSIC_FONT : undefined} fill="#c0431f" style={{animation:'fadeUp 0.3s both'}}>{txt}</text>)}""")
# lesson 8: name the term (from her chromatic tool)
rep("{t('Every black key has two names: ♯ from the key on its left, ♭ from the key on its right.', '검은건반은 이름이 둘이에요: 왼쪽 건반에서 온 ♯, 오른쪽 건반에서 온 ♭.')}</div>",
    "{t('Every black key has two names: ♯ from the key on its left, ♭ from the key on its right. Same key, different names: enharmonic.', '검은건반은 이름이 둘이에요: 왼쪽 건반에서 온 ♯, 오른쪽 건반에서 온 ♭. 같은 건반에 다른 이름: 딴이름한소리(이명동음).')}</div>")
NEW = r"""
// lesson 9: double sharp and double flat. Two half steps, as in the whole step: every name a key can have (her ALL_NAMES).
const AC_DBL = [   // a: the letter's key, b: where it lands, mid: the key in between, n: the name, eq: the name it equals
  { a: 0, b: 2, n: 'C𝄪', eq: 'D', up: true, L: 'C' }, { a: 4, b: 6, n: 'E𝄪', eq: 'F♯', up: true, L: 'E' }, { a: 5, b: 7, n: 'F𝄪', eq: 'G', up: true, L: 'F' }, { a: 9, b: 11, n: 'A𝄪', eq: 'B', up: true, L: 'A' },
  { a: 2, b: 0, n: 'D𝄫', eq: 'C', up: false, L: 'D' }, { a: 5, b: 3, n: 'F𝄫', eq: 'E♭', up: false, L: 'F' }, { a: 7, b: 5, n: 'G𝄫', eq: 'F', up: false, L: 'G' }, { a: 11, b: 9, n: 'B𝄫', eq: 'A', up: false, L: 'B' },
];
function AcDouble() {
  const [view, setView] = useState('all');   // 'all' -> 'one' -> 'try'
  const [i, setI] = useState(0), [nonce, setNonce] = useState(0), [c, setC] = useState(0), [done, setDone] = useState(false), [miss, setMiss] = useState(false);
  const timers = useRef([]);
  const clear = () => { timers.current.forEach(clearTimeout); timers.current = []; };
  useEffect(() => clear, []);
  const snd = (k) => { if (k >= 0) playKey(k, 0.6); };
  const pcOf = (k) => ((k % 12) + 12) % 12;
  const mf = (str) => str.split(/([𝄪𝄫])/).map((p, j) => /[𝄪𝄫]/.test(p) ? <span key={j} style={{fontFamily:MUSIC_FONT}}>{p}</span> : p);
  const legs = (E, anim) => { const m = E.a + (E.b > E.a ? 1 : -1); return [[E.a, m, anim, '#26296b', 0], [m, E.b, anim, '#c0431f', anim ? 0.55 : 0]]; };
  const titleStyle = {textAlign:'center',fontFamily:"'Playfair Display', Georgia, serif",fontSize:22,fontWeight:900,color:'#26296b',lineHeight:1.2,margin:'0 0 8px',textWrap:'balance'};
  const lineStyle = {textAlign:'center',fontSize:15,fontWeight:800,color:'#26296b',margin:'8px 0 6px',minHeight:62,textWrap:'balance',wordBreak:'keep-all'};
  const prim = {...KF_BTN,minWidth:140,background:'#26296b',color:'#fffefa',borderColor:'#26296b'};
  const row = (children) => <div style={{textAlign:'center',marginTop:14,display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap'}}>{children}</div>;
  const title = t('Double sharp, double flat', '겹샵, 겹플랫');
  const show = (idx) => { clear(); setI(idx); setNonce(n => n + 1); const E = AC_DBL[idx], m = E.a + (E.b > E.a ? 1 : -1); snd(E.a); timers.current.push(setTimeout(() => snd(m), 450)); timers.current.push(setTimeout(() => snd(E.b), 900)); };
  const lineOf = (E) => E.up
    ? t(E.n + ' is two half steps above ' + E.L + ': the key ' + E.eq + '.', E.n + '은 ' + E.L + '보다 반음 두 개 위예요: ' + E.eq + ' 건반이에요.')
    : t(E.n + ' is two half steps below ' + E.L + ': the key ' + E.eq + '.', E.n + '은 ' + E.L + '보다 반음 두 개 아래예요: ' + E.eq + ' 건반이에요.');
  let body;
  if (view === 'all') {
    const A = AC_DBL[2], B = AC_DBL[7];
    body = <>
      <div style={titleStyle}>{title}</div>
      <div style={lineStyle}>{mf(t('Double sharp 𝄪 = two half steps up. Double flat 𝄫 = two half steps down. Just like a whole step.', '겹샵 𝄪 = 반음 두 개 위. 겹플랫 𝄫 = 반음 두 개 아래. 온음과 같아요.'))}</div>
      <AcKeys marks={{}} arcs={[...legs(A, false), ...legs(B, false)]} names={{ [A.a]: A.n, [B.a]: B.n }} nonce="all" stagger topRoom={46}/>
      {row(<button className="ghost-btn" style={prim} onClick={() => { setView('one'); show(0); }}>{t('One by one →', '하나씩 →')}</button>)}
    </>;
  } else if (view === 'one') {
    const E = AC_DBL[i], marks = { [E.a]: 'pass', [E.b]: 'pick' };
    body = <>
      <div style={titleStyle}>{title}</div>
      <div style={lineStyle}>{mf(lineOf(E))}</div>
      <AcKeys marks={marks} arcs={legs(E, true)} names={{ [E.a]: E.n, [E.b]: '= ' + E.eq }} nonce={nonce} stagger topRoom={46}/>
      {row(<>
        <button className="ghost-btn" style={{...KF_BTN,minWidth:110}} onClick={() => { clear(); if (i === 0) setView('all'); else show(i - 1); }}>{t('← Back', '← 이전')}</button>
        <button className="ghost-btn" style={prim} onClick={() => { clear(); if (i === AC_DBL.length - 1) { setView('try'); setC(0); setDone(false); setMiss(false); setNonce(n => n + 1); } else show(i + 1); }}>{i === AC_DBL.length - 1 ? t('Your turn →', '내가 해보기 →') : t('Next →', '다음 →')}</button>
      </>)}
    </>;
  } else {
    const ORDER = [2, 7, 1, 5, 0, 4, 3, 6], E = AC_DBL[ORDER[c % ORDER.length]];
    const tap = (k) => { if (done) return; clear(); snd(k); if (pcOf(k) === pcOf(E.b)) { setDone(true); setMiss(false); setNonce(n => n + 1); } else setMiss(true); };
    const line = done ? t(E.n + ' = ' + E.eq + ': two half steps ' + (E.up ? 'up' : 'down') + '.', E.n + ' = ' + E.eq + ': 반음 두 개 ' + (E.up ? '위' : '아래') + '.')
      : miss ? t('Not that key. Two half steps ' + (E.up ? 'above ' : 'below ') + E.L + '.', '그 건반이 아니에요. ' + E.L + '보다 반음 두 개 ' + (E.up ? '위' : '아래') + '예요.')
      : t('Tap the key for ' + E.n + '.', E.n + ' 건반을 눌러요.');
    body = <>
      <div style={titleStyle}>{t('Your turn', '내가 해보기')}</div>
      <div style={lineStyle}>{mf(line)}</div>
      <AcKeys marks={done ? { [E.a]: 'pass', [E.b]: 'pick' } : { [E.a]: 'pass' }} arcs={done ? legs(E, true) : []} names={done ? { [E.a]: E.n, [E.b]: '= ' + E.eq } : { [E.a]: E.L }} nonce={nonce + c} stagger topRoom={46} onTap={tap}/>
      {done && row(<button className="ghost-btn" style={prim} onClick={() => { setC(c + 1); setDone(false); setMiss(false); }}>{t('Another →', '하나 더 →')}</button>)}
      {row(<button className="ghost-btn" style={{...KF_BTN,minWidth:110}} onClick={() => { clear(); setView('one'); show(AC_DBL.length - 1); }}>{t('← Back', '← 이전')}</button>)}
    </>;
  }
  return <div className="try-box" data-ac-lesson="double" style={{background:'#fff',border:'1px solid var(--border)',borderRadius:10,padding:'10px 10px 12px',margin:'4px 0 16px'}}>{body}</div>;
}
[['ac-double', 'Double sharp, double flat', '겹샵, 겹플랫', 'Two half steps up or down.', '반음 두 개 위로 또는 아래로.']].forEach(([id, en, ko, benEn, bko]) => {
  TOOLS.push({ id, ch: 'concept', title: en, blurb: benEn, hidden: true, get kicker() { return TOOL_AREAS.find(a => a.id === 'pitch').name + ' · ' + (LANG === 'ko' ? '임시표' : 'Accidentals'); }, C: () => <AcDouble/> });
  TOOL_KO[id] = [ko, bko];
  const tl = TOOLS[TOOLS.length - 1], k = TOOL_KO[id], ti = tl.title, bl = tl.blurb; tl.titleEn = ti; tl.blurbEn = bl;
  Object.defineProperty(tl, 'title', { get: () => (LANG === 'ko' ? k[0] : ti), enumerable: true, configurable: true });
  Object.defineProperty(tl, 'blurb', { get: () => (LANG === 'ko' ? k[1] : bl), enumerable: true, configurable: true });
  TOOL_CONCEPT[id] = 'p-clock';
});
"""
rep("// the Toolbox: a concept's book, right under its name (open on screen, or print)\nfunction CbCard(", NEW + "// the Toolbox: a concept's book, right under its name (open on screen, or print)\nfunction CbCard(")
rep("'ac-play', 'ac-two', 'chromatic',", "'ac-play', 'ac-two', 'ac-double', 'chromatic',")
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
