import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
NEW = r"""
// lesson 6: signs in a bar. A sign changes its own note until the bar line; a natural cancels it; a new bar starts plain.
const AC_BAR = [   // d: staff step (31 = F, 32 = G, 34 = B), sign: 1 sharp / -1 flat / 2 natural / 0 none, snd: half steps from the plain note, bar: a bar line comes before this note
  { d: 31, sign: 1, snd: 1, en: 'F♯: the sharp raises F one half step.', ko: 'F♯: 샵이 F를 반음 올려요.' },
  { d: 32, sign: 0, snd: 0, en: 'G: no sign, so plain G. A sign only changes its own note.', ko: 'G: 표시가 없으니 그냥 G. 임시표는 자기 음만 바꿔요.' },
  { d: 31, sign: 0, snd: 1, en: 'No sign here, but still F♯: a sign lasts until the bar line.', ko: '표시가 없어도 여전히 F♯: 임시표는 세로줄까지 효과가 있어요.' },
  { d: 34, sign: -1, snd: -1, en: 'B♭: the flat lowers B one half step.', ko: 'B♭: 플랫이 B를 반음 내려요.' },
  { d: 34, sign: 2, snd: 0, en: 'The natural cancels the flat: plain B.', ko: '내추럴이 플랫을 취소해요: 그냥 B.' },
  { d: 31, sign: 0, snd: 0, bar: true, en: 'New bar: plain F again. The bar line ended the sharp.', ko: '새 마디: 다시 그냥 F. 세로줄이 샵을 끝냈어요.' },
];
function AcBar() {
  const [view, setView] = useState('all');   // 'all' -> 'one' -> 'try'
  const [i, setI] = useState(0), [nonce, setNonce] = useState(0), [c, setC] = useState(0), [done, setDone] = useState(false), [miss, setMiss] = useState(false);
  const timers = useRef([]);
  const clear = () => { timers.current.forEach(clearTimeout); timers.current = []; };
  useEffect(() => clear, []);
  const snd = (k) => { if (k >= 0) playKey(k, 0.6); };
  const key = (n) => dMidiKey(n.d) + n.snd;
  const NAME = (n) => dName(n.d) + (n.snd > 0 ? '♯' : n.snd < 0 ? '♭' : '');
  const y = (d) => dY(d) - 30;
  let x = 68; const placed = AC_BAR.map(n => { if (n.bar) x += 26; const px = x; x += 34; return { ...n, x: px, barX: px - 22 }; });
  const W = x + 8, barAt = placed.find(n => n.bar).barX;
  const titleStyle = {textAlign:'center',fontFamily:"'Playfair Display', Georgia, serif",fontSize:22,fontWeight:900,color:'#26296b',lineHeight:1.2,margin:'0 0 8px',textWrap:'balance'};
  const lineStyle = {textAlign:'center',fontSize:15,fontWeight:800,color:'#26296b',margin:'8px 0 6px',minHeight:42,textWrap:'balance',wordBreak:'keep-all'};
  const prim = {...KF_BTN,minWidth:140,background:'#26296b',color:'#fffefa',borderColor:'#26296b'};
  const row = (children) => <div style={{textAlign:'center',marginTop:14,display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap'}}>{children}</div>;
  // the staff: notes up to `upto` are shown (the others wait, pale); `cur` is the note being looked at; `ask` hides a note's name
  const staff = (upto, cur, ask) => <svg viewBox={`0 12 ${W} 78`} style={{width:'100%',maxWidth:340,display:'block',margin:'0 auto'}}>
    {[30, 32, 34, 36, 38].map(d => <line key={d} x1="4" x2={W - 4} y1={y(d)} y2={y(d)} stroke="#26296b" strokeOpacity="0.55" strokeWidth="1.2"/>)}
    <ClefGlyph clef="treble" st="treble" yOf={(d) => y(d)} ink="#26296b"/>
    <line x1={barAt} x2={barAt} y1={y(38)} y2={y(30)} stroke="#26296b" strokeWidth="1.6" opacity={upto >= AC_BAR.findIndex(n => n.bar) ? 1 : 0.3}/>
    <line x1={W - 4} x2={W - 4} y1={y(38)} y2={y(30)} stroke="#26296b" strokeWidth="2.6"/>
    {placed.map((n, j) => {
      const on = j <= upto, hot = j === cur, col = hot ? '#e4572e' : (n.snd !== 0 ? '#c0431f' : '#26296b'), op = on ? 1 : 0.28;
      return <g key={j} opacity={op}>
        {n.sign === 1 && <SharpShape x={n.x - 15} y={y(n.d)} color={col}/>}
        {n.sign === -1 && <FlatShape x={n.x - 14} y={y(n.d)} color={col}/>}
        {n.sign === 2 && <NaturalShape x={n.x - 14} y={y(n.d)} color={col}/>}
        <ellipse cx={n.x} cy={y(n.d)} rx="6.5" ry="4.7" transform={`rotate(-20 ${n.x} ${y(n.d)})`} fill={col}/>
        <line x1={n.x + 6} x2={n.x + 6} y1={y(n.d)} y2={y(n.d) - 28} stroke={col} strokeWidth="1.3"/>
        {on && !(ask === j) && <text x={n.x} y={84} textAnchor="middle" fontSize="12" fontWeight="900" fill={hot ? '#e4572e' : '#6d6f9c'}>{NAME(n)}</text>}
        {ask === j && <text x={n.x} y={84} textAnchor="middle" fontSize="13" fontWeight="900" fill="#e4572e">?</text>}
      </g>; })}
  </svg>;
  const title = t('Signs in a bar', '마디 안의 임시표');
  let body;
  if (view === 'all') {
    body = <>
      <div style={titleStyle}>{title}</div>
      {staff(AC_BAR.length - 1, -1, -1)}
      <div style={lineStyle}>{t('A ♯ or ♭ lasts until the bar line. A ♮ cancels it. A new bar starts plain.', '♯, ♭는 세로줄까지 효과가 있어요. ♮가 취소하고, 새 마디는 다시 원래대로 시작해요.')}</div>
      {row(<button className="ghost-btn" style={prim} onClick={() => { setView('one'); setI(0); setNonce(n => n + 1); snd(key(AC_BAR[0])); }}>{t('One by one →', '하나씩 →')}</button>)}
    </>;
  } else if (view === 'one') {
    const n = AC_BAR[i], go = (k) => { clear(); setI(k); setNonce(m => m + 1); snd(key(AC_BAR[k])); };
    body = <>
      <div style={titleStyle}>{title}</div>
      {staff(i, i, -1)}
      <AcKeys marks={{ [((key(n) % 12) + 12) % 12]: 'pick' }} arcs={[]} names={{}} nonce={nonce} topRoom={4}/>
      <div style={lineStyle}>{t(n.en, n.ko)}</div>
      {row(<>
        <button className="ghost-btn" style={{...KF_BTN,minWidth:110}} onClick={() => { if (i === 0) setView('all'); else go(i - 1); }}>{t('← Back', '← 이전')}</button>
        <button className="ghost-btn" style={prim} onClick={() => { if (i === AC_BAR.length - 1) { setView('try'); setC(0); setDone(false); setMiss(false); setNonce(m => m + 1); } else go(i + 1); }}>{i === AC_BAR.length - 1 ? t('Your turn →', '내가 해보기 →') : t('Next →', '다음 →')}</button>
      </>)}
    </>;
  } else {
    const ASK = [2, 5, 1, 4, 3], j = ASK[c % ASK.length], n = AC_BAR[j], k = ((key(n) % 12) + 12) % 12;
    const tap = (kk) => { if (done) return; clear(); snd(kk); if (((kk % 12) + 12) % 12 === k) { setDone(true); setMiss(false); } else setMiss(true); };
    const line = done ? t(n.en, n.ko) : miss ? t('Not that one. Look at the sign, and at the bar line.', '그 건반이 아니에요. 임시표와 세로줄을 다시 봐요.') : t('Which key does the ? note play?', '? 음표는 어느 건반일까요?');
    body = <>
      <div style={titleStyle}>{t('Your turn', '내가 해보기')}</div>
      {staff(AC_BAR.length - 1, j, done ? -1 : j)}
      <AcKeys marks={done ? { [k]: 'pick' } : {}} arcs={[]} names={{}} nonce={nonce + c} topRoom={4} onTap={tap}/>
      <div style={lineStyle}>{line}</div>
      {done && row(<button className="ghost-btn" style={prim} onClick={() => { setC(c + 1); setDone(false); setMiss(false); }}>{t('Another →', '하나 더 →')}</button>)}
      {row(<button className="ghost-btn" style={{...KF_BTN,minWidth:110}} onClick={() => { clear(); setView('one'); setI(AC_BAR.length - 1); setNonce(m => m + 1); }}>{t('← Back', '← 이전')}</button>)}
    </>;
  }
  return <div className="try-box" data-ac-lesson="bar" style={{background:'#fff',border:'1px solid var(--border)',borderRadius:10,padding:'10px 10px 12px',margin:'4px 0 16px'}}>{body}</div>;
}
[['ac-bar', 'Signs in a bar', '마디 안의 임시표', 'How ♯, ♭ and ♮ work inside a bar.', '마디 안에서 ♯, ♭, ♮가 어떻게 적용되는지.']].forEach(([id, en, ko, benEn, bko]) => {
  TOOLS.push({ id, ch: 'concept', title: en, blurb: benEn, hidden: true, get kicker() { return TOOL_AREAS.find(a => a.id === 'pitch').name + ' · ' + (LANG === 'ko' ? '임시표' : 'Accidentals'); }, C: () => <AcBar/> });
  TOOL_KO[id] = [ko, bko];
  const tl = TOOLS[TOOLS.length - 1], k = TOOL_KO[id], ti = tl.title, bl = tl.blurb; tl.titleEn = ti; tl.blurbEn = bl;
  Object.defineProperty(tl, 'title', { get: () => (LANG === 'ko' ? k[0] : ti), enumerable: true, configurable: true });
  Object.defineProperty(tl, 'blurb', { get: () => (LANG === 'ko' ? k[1] : bl), enumerable: true, configurable: true });
  TOOL_CONCEPT[id] = 'p-clock';
});
"""
rep("// the Toolbox: a concept's book, right under its name (open on screen, or print)\nfunction CbCard(", NEW + "// the Toolbox: a concept's book, right under its name (open on screen, or print)\nfunction CbCard(")
rep("'ac-natural', 'sac-signs', 'sac-natural', 'chromatic', 'accidental-bar', 'sac-bar',", "'ac-natural', 'ac-bar', 'sac-signs', 'sac-natural', 'chromatic', 'sac-bar',")
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
