import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
# AcKeys: a name may be a pair [sharp name, flat name], two lines, coral over blue
rep("""{Object.entries(names || {}).map(([k, txt]) => <text key={'n' + k + txt} x={kx(+k)} y={stagger && white(+k) ? -27 : -9} textAnchor="middle" fontSize="17" fontWeight="900" fill="#c0431f" style={{animation:'fadeUp 0.3s both'}}>{txt}</text>)}""",
"""{Object.entries(names || {}).map(([k, txt]) => Array.isArray(txt)
        ? txt.map((tx, q) => <text key={'n' + k + tx} x={kx(+k)} y={q === 0 ? -27 : -9} textAnchor="middle" fontSize="16" fontWeight="900" fill={q === 0 ? '#c0431f' : '#2f62c9'} style={{animation:'fadeUp 0.3s both'}}>{tx}</text>)
        : <text key={'n' + k + txt} x={kx(+k)} y={stagger && white(+k) ? -27 : -9} textAnchor="middle" fontSize="17" fontWeight="900" fill="#c0431f" style={{animation:'fadeUp 0.3s both'}}>{txt}</text>)}""")
NEW = r"""
// lesson 8: one key, two names. Every black key is a sharp from the white key on its left AND a flat from the white key on its right; a white key can be a sharp or a flat too.
const AC_TWO_UP = '#c0431f', AC_TWO_DN = '#2f62c9';
const AC_TWO = [   // k: the key, up: where its sharp name comes from, dn: where its flat name comes from, names [sharp name, flat name]
  { k: 1, up: 0, dn: 2, n: ['C♯', 'D♭'] }, { k: 3, up: 2, dn: 4, n: ['D♯', 'E♭'] }, { k: 6, up: 5, dn: 7, n: ['F♯', 'G♭'] }, { k: 8, up: 7, dn: 9, n: ['G♯', 'A♭'] }, { k: 10, up: 9, dn: 11, n: ['A♯', 'B♭'] },
  { k: 5, up: 4, dn: null, n: ['E♯', 'F'], w: 'F' }, { k: 12, up: 11, dn: null, n: ['B♯', 'C'], w: 'C' }, { k: 4, up: null, dn: 5, n: ['E', 'F♭'], w: 'E' }, { k: -1, up: null, dn: 0, n: ['B', 'C♭'], w: 'B' },
];
function AcTwo() {
  const [view, setView] = useState('all');   // 'all' -> 'one' -> 'try'
  const [i, setI] = useState(0), [nonce, setNonce] = useState(0), [c, setC] = useState(0), [done, setDone] = useState(false), [miss, setMiss] = useState(false);
  const timers = useRef([]);
  const clear = () => { timers.current.forEach(clearTimeout); timers.current = []; };
  useEffect(() => clear, []);
  const snd = (k) => { if (k >= 0) playKey(k, 0.6); };
  const pcOf = (k) => ((k % 12) + 12) % 12;
  const isW = (k) => PC_INFO[pcOf(k)].white;
  const arcsOf = (E, anim) => { const a = []; if (E.up != null) a.push([E.up, E.k, anim, AC_TWO_UP, 0]); if (E.dn != null) a.push([E.dn, E.k, anim, AC_TWO_DN, anim ? 0.5 : 0]); return a; };
  const nameMap = (E) => E.w ? { [E.k]: E.n[0].length === 2 && E.n[0][1] === '♯' ? E.n[0] : E.n[1] } : { [E.k]: E.n };
  const lineOf = (E) => E.w
    ? t(E.w + ' is also ' + (E.up != null ? E.n[0] : E.n[1]) + ': one white key, two names.', E.w + '는 ' + (E.up != null ? E.n[0] : E.n[1]) + '이기도 해요: 흰건반 하나, 이름 둘.')
    : t(E.n[0] + ' and ' + E.n[1] + ' are the same key: one sound, two names.', E.n[0] + '과 ' + E.n[1] + '은 같은 건반이에요: 소리는 하나, 이름은 둘.');
  const sub = (E) => E.w ? '' : t('♯ comes from the white key on the left, ♭ from the one on the right.', '♯은 왼쪽 흰건반에서, ♭은 오른쪽 흰건반에서 와요.');
  const titleStyle = {textAlign:'center',fontFamily:"'Playfair Display', Georgia, serif",fontSize:22,fontWeight:900,color:'#26296b',lineHeight:1.2,margin:'0 0 8px',textWrap:'balance'};
  const lineStyle = {textAlign:'center',fontSize:15,fontWeight:800,color:'#26296b',margin:'8px 0 6px',minHeight:62,textWrap:'balance',wordBreak:'keep-all'};
  const prim = {...KF_BTN,minWidth:140,background:'#26296b',color:'#fffefa',borderColor:'#26296b'};
  const row = (children) => <div style={{textAlign:'center',marginTop:14,display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap'}}>{children}</div>;
  const title = t('One key, two names', '한 건반, 두 이름');
  const show = (idx) => { clear(); setI(idx); setNonce(n => n + 1); snd(AC_TWO[idx].k); };
  let body;
  if (view === 'all') {
    const arcs = [], names = {}; AC_TWO.slice(0, 5).forEach(E => { arcs.push(...arcsOf(E, false)); names[E.k] = E.n; });
    body = <>
      <div style={titleStyle}>{title}</div>
      <div style={lineStyle}>{t('Every black key has two names: ♯ from the key on its left, ♭ from the key on its right.', '검은건반은 이름이 둘이에요: 왼쪽 건반에서 온 ♯, 오른쪽 건반에서 온 ♭.')}</div>
      <AcKeys marks={{}} arcs={arcs} names={names} nonce="all" topRoom={46}/>
      {row(<button className="ghost-btn" style={prim} onClick={() => { setView('one'); show(0); }}>{t('One by one →', '하나씩 →')}</button>)}
    </>;
  } else if (view === 'one') {
    const E = AC_TWO[i], marks = { [E.k]: 'pick' }; if (E.up != null) marks[E.up] = 'pass'; if (E.dn != null) marks[E.dn] = 'pass';
    body = <>
      <div style={titleStyle}>{title}</div>
      <div style={lineStyle}>{lineOf(E)}{sub(E) ? <><br/><span style={{fontWeight:700,fontSize:13.5}}>{sub(E)}</span></> : null}</div>
      <AcKeys marks={marks} arcs={arcsOf(E, true)} names={E.w ? { [E.k]: (E.up != null ? E.n[0] : E.n[1]) } : { [E.k]: E.n }} nonce={nonce} stagger topRoom={46}/>
      {row(<>
        <button className="ghost-btn" style={{...KF_BTN,minWidth:110}} onClick={() => { clear(); if (i === 0) setView('all'); else show(i - 1); }}>{t('← Back', '← 이전')}</button>
        <button className="ghost-btn" style={prim} onClick={() => { clear(); if (i === AC_TWO.length - 1) { setView('try'); setC(0); setDone(false); setMiss(false); setNonce(n => n + 1); } else show(i + 1); }}>{i === AC_TWO.length - 1 ? t('Your turn →', '내가 해보기 →') : t('Next →', '다음 →')}</button>
      </>)}
    </>;
  } else {
    const ASK = [[6, 'G♭', 'F♯', 'G'], [10, 'A♯', 'B♭', 'A'], [1, 'D♭', 'C♯', 'D'], [5, 'E♯', 'F', 'E'], [-1, 'C♭', 'B', 'C'], [3, 'D♯', 'E♭', 'D'], [12, 'B♯', 'C', 'B'], [4, 'F♭', 'E', 'F'], [8, 'A♭', 'G♯', 'A']];
    const [kk, nm, other, from] = ASK[c % ASK.length], flat = nm[1] === '♭';
    const tap = (k) => { if (done) return; clear(); snd(k); if (pcOf(k) === pcOf(kk)) { setDone(true); setMiss(false); setNonce(n => n + 1); } else setMiss(true); };
    const line = done ? t(nm + ' = ' + other + ': the same key, two names.', nm + ' = ' + other + ': 같은 건반, 이름 둘.')
      : miss ? t('Not that key. ' + nm + ' is one half step ' + (flat ? 'below ' : 'above ') + from + '.', '그 건반이 아니에요. ' + nm + '은 ' + from + '보다 반음 ' + (flat ? '아래' : '위') + '예요.')
      : t('Tap the key for ' + nm + '.', nm + ' 건반을 눌러요.');
    const from0 = flat ? kk + 1 : kk - 1;
    body = <>
      <div style={titleStyle}>{t('Your turn', '내가 해보기')}</div>
      <div style={lineStyle}>{line}</div>
      <AcKeys marks={done ? { [kk]: 'pick' } : {}} arcs={[]} names={done ? { [kk]: nm + ' = ' + other } : {}} nonce={nonce + c} stagger topRoom={46} onTap={tap}/>
      {done && row(<button className="ghost-btn" style={prim} onClick={() => { setC(c + 1); setDone(false); setMiss(false); }}>{t('Another →', '하나 더 →')}</button>)}
      {row(<button className="ghost-btn" style={{...KF_BTN,minWidth:110}} onClick={() => { clear(); setView('one'); show(AC_TWO.length - 1); }}>{t('← Back', '← 이전')}</button>)}
    </>;
  }
  return <div className="try-box" data-ac-lesson="two" style={{background:'#fff',border:'1px solid var(--border)',borderRadius:10,padding:'10px 10px 12px',margin:'4px 0 16px'}}>{body}</div>;
}
[['ac-two', 'One key, two names', '한 건반, 두 이름', 'C♯ and D♭: the same key.', 'C♯과 D♭: 같은 건반.']].forEach(([id, en, ko, benEn, bko]) => {
  TOOLS.push({ id, ch: 'concept', title: en, blurb: benEn, hidden: true, get kicker() { return TOOL_AREAS.find(a => a.id === 'pitch').name + ' · ' + (LANG === 'ko' ? '임시표' : 'Accidentals'); }, C: () => <AcTwo/> });
  TOOL_KO[id] = [ko, bko];
  const tl = TOOLS[TOOLS.length - 1], k = TOOL_KO[id], ti = tl.title, bl = tl.blurb; tl.titleEn = ti; tl.blurbEn = bl;
  Object.defineProperty(tl, 'title', { get: () => (LANG === 'ko' ? k[0] : ti), enumerable: true, configurable: true });
  Object.defineProperty(tl, 'blurb', { get: () => (LANG === 'ko' ? k[1] : bl), enumerable: true, configurable: true });
  TOOL_CONCEPT[id] = 'p-clock';
});
"""
rep("// the Toolbox: a concept's book, right under its name (open on screen, or print)\nfunction CbCard(", NEW + "// the Toolbox: a concept's book, right under its name (open on screen, or print)\nfunction CbCard(")
rep("'ac-bar', 'ac-play', 'chromatic',", "'ac-bar', 'ac-play', 'ac-two', 'chromatic',")
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
