import sys,re
s=open(sys.argv[1],encoding='utf-8').read()
a=s.index("// lesson 6: signs in a bar."); b=s.index("[['ac-bar',")
NEW = r"""// lesson 6: signs in a bar. A sign lives on ONE line or space (one pitch) until the bar line; a natural ends it; a new bar starts plain.
// g: which sign's colour the note wears (s sharp / f flat), snd: half steps from the plain note, hi: the F an octave up (a different line)
const AC_BAR = [
  { d: 31, sign: 1, snd: 1, g: 's' },
  { d: 32, sign: 0, snd: 0 },
  { d: 31, sign: 0, snd: 1, g: 's' },
  { d: 38, sign: 0, snd: 0 },
  { d: 34, sign: -1, snd: -1, g: 'f' },
  { d: 34, sign: 2, snd: 0 },
  { d: 31, sign: 0, snd: 0, bar: true },
];
const AC_BAR_COL = { s: ['#c0431f', '#fbe3da'], f: ['#2f62c9', '#dce6fb'], n: ['#26296b', '#e6e7f1'] };   // [ink, pale band]
// each sign's reach: the row it sits on, from which note to which note (inclusive of the note before the end)
const AC_BANDS = [{ g: 's', d: 31, from: 0, to: 'bar' }, { g: 'f', d: 34, from: 4, to: 5 }, { g: 'n', d: 34, from: 5, to: 'bar' }];
// the walk: what is on show at each step. upto: notes shown, cur: the note in focus, bands: how many bands are drawn, band: the band in focus
const AC_BAR_STEPS = [
  { upto: 0, cur: 0, bands: 0, en: 'F♯: the sharp raises this F one half step.', ko: 'F♯: 샵이 이 F를 반음 올려요.' },
  { upto: 0, cur: -1, bands: 1, band: 0, en: 'The sharp now covers this space, all the way to the bar line. Any F on it is F♯.', ko: '샵이 이 칸을 세로줄까지 덮어요. 이 칸의 F는 모두 F♯이에요.' },
  { upto: 1, cur: 1, bands: 1, en: 'G is on a different line or space: the sharp does not touch it.', ko: 'G는 다른 줄이나 칸에 있어요: 샵이 닿지 않아요.' },
  { upto: 2, cur: 2, bands: 1, en: 'F on the same space: F♯ again. No sign needed, it follows automatically.', ko: '같은 칸의 F: 또 F♯이에요. 표시가 없어도 자동으로 따라와요.' },
  { upto: 3, cur: 3, bands: 1, en: 'The F an octave higher is on another line, outside the coral band: plain F. A sign covers only its own pitch.', ko: '한 옥타브 위 F는 다른 줄이라 코랄 띠 밖이에요: 그냥 F. 임시표는 자기 높이의 음에만 적용돼요.' },
  { upto: 4, cur: 4, bands: 2, band: 1, en: 'B♭: the flat covers this line (blue band) until it is cancelled or the bar ends.', ko: 'B♭: 플랫이 이 줄(파란 띠)을 덮어요. 취소되거나 마디가 끝날 때까지요.' },
  { upto: 5, cur: 5, bands: 3, band: 2, en: 'The natural ends the flat: plain B, with a grey band to the bar line.', ko: '내추럴이 플랫을 끝내요: 그냥 B. 회색 띠가 세로줄까지 가요.' },
  { upto: 6, cur: 6, bands: 3, en: 'New bar: every band stopped at the bar line. Plain F again.', ko: '새 마디: 모든 띠가 세로줄에서 멈췄어요. 다시 그냥 F.' },
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
  let x = 66; const placed = AC_BAR.map(n => { if (n.bar) x += 24; const px = x; x += 31; return { ...n, x: px, barX: px - 20 }; });
  const W = x + 6, barAt = placed.find(n => n.bar).barX, barIdx = AC_BAR.findIndex(n => n.bar);
  const titleStyle = {textAlign:'center',fontFamily:"'Playfair Display', Georgia, serif",fontSize:22,fontWeight:900,color:'#26296b',lineHeight:1.2,margin:'0 0 8px',textWrap:'balance'};
  const lineStyle = {textAlign:'center',fontSize:15,fontWeight:800,color:'#26296b',margin:'8px 0 6px',minHeight:62,textWrap:'balance',wordBreak:'keep-all'};
  const prim = {...KF_BTN,minWidth:140,background:'#26296b',color:'#fffefa',borderColor:'#26296b'};
  const row = (children) => <div style={{textAlign:'center',marginTop:14,display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap'}}>{children}</div>;
  // the staff. upto: notes shown; cur: the note ringed; nb: how many bands are drawn; hb: the band in focus; ask: the note hidden behind a '?'
  const staff = (upto, cur, nb, hb, ask) => <svg viewBox={`0 12 ${W} 78`} style={{width:'100%',maxWidth:360,display:'block',margin:'0 auto'}}>
    {AC_BANDS.slice(0, nb).map((B, j) => { const x0 = placed[B.from].x - 17, x1 = B.to === 'bar' ? barAt - 5 : placed[B.to].x - 19, col = AC_BAR_COL[B.g];
      return <rect key={'b' + j} x={x0} y={y(B.d) - 5} width={x1 - x0} height="10" rx="3" fill={col[1]} stroke={col[0]} strokeWidth={hb === j ? 1.6 : 0.8} strokeOpacity={hb === j ? 1 : 0.55} style={{animation:'fadeUp 0.35s both'}}/>; })}
    {[30, 32, 34, 36, 38].map(d => <line key={d} x1="4" x2={W - 4} y1={y(d)} y2={y(d)} stroke="#26296b" strokeOpacity="0.55" strokeWidth="1.2"/>)}
    <ClefGlyph clef="treble" st="treble" yOf={(d) => y(d)} ink="#26296b"/>
    <line x1={barAt} x2={barAt} y1={y(38)} y2={y(30)} stroke="#26296b" strokeWidth="1.6" opacity={upto >= barIdx ? 1 : 0.3}/>
    <line x1={W - 4} x2={W - 4} y1={y(38)} y2={y(30)} stroke="#26296b" strokeWidth="2.6"/>
    {placed.map((n, j) => {
      const on = j <= upto, col = n.g ? AC_BAR_COL[n.g][0] : '#26296b', op = on ? 1 : 0.25, down = n.d >= 34, sgCol = n.sign === 1 ? AC_BAR_COL.s[0] : n.sign === -1 ? AC_BAR_COL.f[0] : AC_BAR_COL.n[0];
      return <g key={j} opacity={op}>
        {j === cur && <circle cx={n.x} cy={y(n.d)} r="12.5" fill="none" stroke="#26296b" strokeWidth="1.8"/>}
        {ask === j && <circle cx={n.x} cy={y(n.d)} r="12.5" fill="none" stroke="#26296b" strokeWidth="1.8" strokeDasharray="3 3"/>}
        {n.sign === 1 && <SharpShape x={n.x - 15} y={y(n.d)} color={sgCol}/>}
        {n.sign === -1 && <FlatShape x={n.x - 14} y={y(n.d)} color={sgCol}/>}
        {n.sign === 2 && <NaturalShape x={n.x - 14} y={y(n.d)} color={sgCol}/>}
        <ellipse cx={n.x} cy={y(n.d)} rx="6.5" ry="4.7" transform={`rotate(-20 ${n.x} ${y(n.d)})`} fill={col}/>
        {down ? <line x1={n.x - 6} x2={n.x - 6} y1={y(n.d)} y2={y(n.d) + 28} stroke={col} strokeWidth="1.3"/> : <line x1={n.x + 6} x2={n.x + 6} y1={y(n.d)} y2={y(n.d) - 28} stroke={col} strokeWidth="1.3"/>}
        {on && ask !== j && <text x={n.x} y={84} textAnchor="middle" fontSize="12" fontWeight="900" fill={n.g ? col : '#6d6f9c'}>{NAME(n)}</text>}
        {ask === j && <text x={n.x} y={84} textAnchor="middle" fontSize="13" fontWeight="900" fill="#26296b">?</text>}
      </g>; })}
  </svg>;
  const title = t('Signs in a bar', '마디 안의 임시표');
  const N = AC_BAR_STEPS.length;
  let body;
  if (view === 'all') {
    body = <>
      <div style={titleStyle}>{title}</div>
      {staff(AC_BAR.length - 1, -1, 3, -1, -1)}
      <div style={lineStyle}>{t('A sign covers its own line or space until the bar line. The band shows how far.', '임시표는 자기 줄이나 칸을 세로줄까지 덮어요. 띠가 어디까지인지 보여줘요.')}</div>
      {row(<button className="ghost-btn" style={prim} onClick={() => { setView('one'); setI(0); setNonce(n => n + 1); snd(key(AC_BAR[0])); }}>{t('One by one →', '하나씩 →')}</button>)}
    </>;
  } else if (view === 'one') {
    const st = AC_BAR_STEPS[i], n = AC_BAR[Math.max(st.cur, 0)], go = (k) => { clear(); setI(k); setNonce(m => m + 1); const q = AC_BAR_STEPS[k]; if (q.cur >= 0) snd(key(AC_BAR[q.cur])); };
    body = <>
      <div style={titleStyle}>{title}</div>
      {staff(st.upto, st.cur, st.bands, st.band, -1)}
      <AcKeys marks={st.cur >= 0 ? { [((key(n) % 12) + 12) % 12]: 'pick' } : {}} arcs={[]} names={{}} nonce={nonce} topRoom={4}/>
      <div style={lineStyle}>{t(st.en, st.ko)}</div>
      {row(<>
        <button className="ghost-btn" style={{...KF_BTN,minWidth:110}} onClick={() => { if (i === 0) setView('all'); else go(i - 1); }}>{t('← Back', '← 이전')}</button>
        <button className="ghost-btn" style={prim} onClick={() => { if (i === N - 1) { setView('try'); setC(0); setDone(false); setMiss(false); setNonce(m => m + 1); } else go(i + 1); }}>{i === N - 1 ? t('Your turn →', '내가 해보기 →') : t('Next →', '다음 →')}</button>
      </>)}
    </>;
  } else {
    const ASK = [2, 3, 1, 5, 6, 4], j = ASK[c % ASK.length], n = AC_BAR[j], k = ((key(n) % 12) + 12) % 12;
    const why = [t('Same space as the sharp.', '샵과 같은 칸이에요.'), t('Another line from the sharp, so plain.', '샵과 다른 줄이라 그냥 음이에요.'), t('Another space, so plain.', '다른 칸이라 그냥 음이에요.'), t('The natural cancelled the flat.', '내추럴이 플랫을 취소했어요.'), t('New bar: plain.', '새 마디라 그냥 음이에요.'), t('The flat covers this line.', '플랫이 이 줄을 덮어요.')];
    const tap = (kk) => { if (done) return; clear(); snd(kk); if (((kk % 12) + 12) % 12 === k) { setDone(true); setMiss(false); } else setMiss(true); };
    const line = done ? t(NAME(n) + '. ' + why[c % ASK.length], NAME(n) + '. ' + why[c % ASK.length]) : miss ? t('Not that one. Is the note on a coloured band?', '그 건반이 아니에요. 음표가 색 띠 위에 있나요?') : t('Which key does the ringed ? note play?', '동그라미 친 ? 음표는 어느 건반일까요?');
    body = <>
      <div style={titleStyle}>{t('Your turn', '내가 해보기')}</div>
      {staff(AC_BAR.length - 1, -1, 3, -1, done ? -1 : j)}
      <AcKeys marks={done ? { [k]: 'pick' } : {}} arcs={[]} names={{}} nonce={nonce + c} topRoom={4} onTap={tap}/>
      <div style={lineStyle}>{line}</div>
      {done && row(<button className="ghost-btn" style={prim} onClick={() => { setC(c + 1); setDone(false); setMiss(false); }}>{t('Another →', '하나 더 →')}</button>)}
      {row(<button className="ghost-btn" style={{...KF_BTN,minWidth:110}} onClick={() => { clear(); setView('one'); setI(N - 1); setNonce(m => m + 1); }}>{t('← Back', '← 이전')}</button>)}
    </>;
  }
  return <div className="try-box" data-ac-lesson="bar" style={{background:'#fff',border:'1px solid var(--border)',borderRadius:10,padding:'10px 10px 12px',margin:'4px 0 16px'}}>{body}</div>;
}
"""
s=s[:a]+NEW+s[b:]
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
