import sys,re
s=open(sys.argv[1],encoding='utf-8').read()
a=s.index("// lesson 6: signs in a bar."); b=s.index("[['ac-bar',")
NEW = r"""// lesson 6: signs in a bar. A sign lives on ONE line or space (one pitch) until the bar line; a natural ends it; a new bar starts plain.
// g: which sign's colour the note wears (s sharp / f flat), snd: half steps from the plain note, hi: the F an octave up (a different line)
const AC_BAR_COL = { s: ['#c0431f', '#fbe3da'], f: ['#2f62c9', '#dce6fb'], n: ['#26296b', '#e6e7f1'] };   // [ink, pale band]
// three little bars. notes: d = staff step (31 F, 34 B, 30 E, 35 C), sign 1 sharp / -1 flat / 2 natural, snd = half steps from the plain note, g = whose colour it wears, bar = a bar line comes before it.
// bands: the row a sign sits on, from which note to which note (or to the bar line). steps: what is on show (upto notes, cur ringed, bands drawn, band in focus). asks: her-turn questions.
const AC_BARS = [
  { notes: [{ d: 31, sign: 1, snd: 1, g: 's' }, { d: 32, sign: 0, snd: 0 }, { d: 31, sign: 0, snd: 1, g: 's' }, { d: 38, sign: 0, snd: 0 }, { d: 34, sign: -1, snd: -1, g: 'f' }, { d: 34, sign: 2, snd: 0 }, { d: 31, sign: 0, snd: 0, bar: true }],
    bands: [{ g: 's', d: 31, from: 0, to: 'bar' }, { g: 'f', d: 34, from: 4, to: 5 }, { g: 'n', d: 34, from: 5, to: 'bar' }],
    steps: [
      { upto: 0, cur: 0, bands: 0, en: 'F♯: the sharp raises this F one half step.', ko: 'F♯: 샵이 이 F를 반음 올려요.' },
      { upto: 0, cur: -1, bands: 1, band: 0, en: 'The sharp now covers this space, all the way to the bar line. Any F on it is F♯.', ko: '샵이 이 칸을 세로줄까지 덮어요. 이 칸의 F는 모두 F♯이에요.' },
      { upto: 1, cur: 1, bands: 1, en: 'G is on a different line or space: the sharp does not touch it.', ko: 'G는 다른 줄이나 칸에 있어요: 샵이 닿지 않아요.' },
      { upto: 2, cur: 2, bands: 1, en: 'F on the same space: F♯ again. No sign needed, it follows automatically.', ko: '같은 칸의 F: 또 F♯이에요. 표시가 없어도 자동으로 따라와요.' },
      { upto: 3, cur: 3, bands: 1, en: 'The F an octave higher is on another line, outside the coral band: plain F. A sign covers only its own pitch.', ko: '한 옥타브 위 F는 다른 줄이라 코랄 띠 밖이에요: 그냥 F. 임시표는 자기 높이의 음에만 적용돼요.' },
      { upto: 4, cur: 4, bands: 2, band: 1, en: 'B♭: the flat covers this line (blue band) until it is cancelled or the bar ends.', ko: 'B♭: 플랫이 이 줄(파란 띠)을 덮어요. 취소되거나 마디가 끝날 때까지요.' },
      { upto: 5, cur: 5, bands: 3, band: 2, en: 'The natural ends the flat: plain B, with a grey band to the bar line.', ko: '내추럴이 플랫을 끝내요: 그냥 B. 회색 띠가 세로줄까지 가요.' },
      { upto: 6, cur: 6, bands: 3, en: 'New bar: every band stopped at the bar line. Plain F again.', ko: '새 마디: 모든 띠가 세로줄에서 멈췄어요. 다시 그냥 F.' },
    ],
    asks: [[2, 'Same space as the sharp.', '샵과 같은 칸이에요.'], [3, 'Another line from the sharp, so plain.', '샵과 다른 줄이라 그냥 음이에요.'], [1, 'Another space, so plain.', '다른 칸이라 그냥 음이에요.'], [5, 'The natural cancelled the flat.', '내추럴이 플랫을 취소했어요.'], [6, 'New bar: plain.', '새 마디라 그냥 음이에요.'], [4, 'The flat covers this line.', '플랫이 이 줄을 덮어요.']] },
  { notes: [{ d: 30, sign: -1, snd: -1, g: 'f' }, { d: 33, sign: 0, snd: 0 }, { d: 30, sign: 0, snd: -1, g: 'f' }, { d: 37, sign: 0, snd: 0 }, { d: 30, sign: 0, snd: 0, bar: true }],
    bands: [{ g: 'f', d: 30, from: 0, to: 'bar' }],
    steps: [
      { upto: 0, cur: 0, bands: 0, en: 'E♭: the flat lowers this E one half step.', ko: 'E♭: 플랫이 이 E를 반음 내려요.' },
      { upto: 0, cur: -1, bands: 1, band: 0, en: 'The flat covers this bottom line until the bar line. Any E on it is E♭.', ko: '플랫이 이 맨 아래 줄을 세로줄까지 덮어요. 이 줄의 E는 모두 E♭이에요.' },
      { upto: 1, cur: 1, bands: 1, en: 'A is on another space: the flat does not touch it.', ko: 'A는 다른 칸에 있어요: 플랫이 닿지 않아요.' },
      { upto: 2, cur: 2, bands: 1, en: 'E on the same line: E♭ again, with no sign. It follows automatically.', ko: '같은 줄의 E: 표시가 없어도 또 E♭이에요. 자동으로 따라와요.' },
      { upto: 3, cur: 3, bands: 1, en: 'The E an octave higher is on another space: plain E.', ko: '한 옥타브 위 E는 다른 칸이에요: 그냥 E.' },
      { upto: 4, cur: 4, bands: 1, en: 'New bar: the band stopped at the bar line. Plain E again.', ko: '새 마디: 띠가 세로줄에서 멈췄어요. 다시 그냥 E.' },
    ],
    asks: [[2, 'Same line as the flat.', '플랫과 같은 줄이에요.'], [3, 'Another space from the flat, so plain.', '플랫과 다른 칸이라 그냥 음이에요.'], [1, 'Another space, so plain.', '다른 칸이라 그냥 음이에요.'], [4, 'New bar: plain.', '새 마디라 그냥 음이에요.']] },
  { notes: [{ d: 35, sign: 1, snd: 1, g: 's' }, { d: 36, sign: 0, snd: 0 }, { d: 35, sign: 0, snd: 1, g: 's' }, { d: 35, sign: 2, snd: 0 }, { d: 35, sign: 0, snd: 0 }, { d: 35, sign: 0, snd: 0, bar: true }],
    bands: [{ g: 's', d: 35, from: 0, to: 3 }, { g: 'n', d: 35, from: 3, to: 'bar' }],
    steps: [
      { upto: 0, cur: 0, bands: 0, en: 'C♯: the sharp raises this C one half step.', ko: 'C♯: 샵이 이 C를 반음 올려요.' },
      { upto: 0, cur: -1, bands: 1, band: 0, en: 'The sharp covers this space until it is cancelled or the bar ends.', ko: '샵이 이 칸을 취소되거나 마디가 끝날 때까지 덮어요.' },
      { upto: 1, cur: 1, bands: 1, en: 'D is on another line: not touched. Plain D.', ko: 'D는 다른 줄이에요: 닿지 않아요. 그냥 D.' },
      { upto: 2, cur: 2, bands: 1, en: 'C on the same space: C♯ again, automatically.', ko: '같은 칸의 C: 또 C♯이에요. 자동으로 따라와요.' },
      { upto: 3, cur: 3, bands: 2, band: 1, en: 'The natural ends the sharp: plain C. Its grey band runs to the bar line.', ko: '내추럴이 샵을 끝내요: 그냥 C. 회색 띠가 세로줄까지 가요.' },
      { upto: 4, cur: 4, bands: 2, en: 'Still plain C: the natural lasts to the bar line too, so no sign is needed.', ko: '여전히 그냥 C: 내추럴도 세로줄까지 효과가 있어서 표시가 필요 없어요.' },
      { upto: 5, cur: 5, bands: 2, en: 'New bar: plain C again.', ko: '새 마디: 다시 그냥 C.' },
    ],
    asks: [[2, 'Same space as the sharp.', '샵과 같은 칸이에요.'], [1, 'Another line, so plain.', '다른 줄이라 그냥 음이에요.'], [4, 'The natural lasts to the bar line.', '내추럴도 세로줄까지 이어져요.'], [3, 'The natural cancelled the sharp.', '내추럴이 샵을 취소했어요.']] },
];
function AcBar() {
  const [ex, setEx] = useState(0);
  const [view, setView] = useState('all');   // 'all' -> 'one' -> 'try'
  const [i, setI] = useState(0), [nonce, setNonce] = useState(0), [c, setC] = useState(0), [done, setDone] = useState(false), [miss, setMiss] = useState(false);
  // her turn mixes the three examples: first question of each, then second of each, ...
  const qs = []; for (let r = 0; r < 6; r++) AC_BARS.forEach((B, e) => { if (B.asks[r]) qs.push({ e, j: B.asks[r][0], en: B.asks[r][1], ko: B.asks[r][2] }); });
  const q = qs[c % qs.length], exi = view === 'try' ? q.e : ex;
  const BAR = AC_BARS[exi], AC_BAR = BAR.notes, AC_BANDS = BAR.bands, AC_BAR_STEPS = BAR.steps;
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
      <div style={{textAlign:'center',fontSize:12,fontWeight:800,color:'#6d6f9c',margin:'-4px 0 6px',letterSpacing:0.4}}>{t('Example ', '예 ')}{exi + 1} / {AC_BARS.length}</div>
      {staff(AC_BAR.length - 1, -1, AC_BANDS.length, -1, -1)}
      <div style={lineStyle}>{t('A sign covers its own line or space until the bar line. The band shows how far.', '임시표는 자기 줄이나 칸을 세로줄까지 덮어요. 띠가 어디까지인지 보여줘요.')}</div>
      {row(<button className="ghost-btn" style={prim} onClick={() => { setView('one'); setI(0); setNonce(n => n + 1); snd(key(AC_BAR[0])); }}>{t('One by one →', '하나씩 →')}</button>)}
    </>;
  } else if (view === 'one') {
    const st = AC_BAR_STEPS[i], n = AC_BAR[Math.max(st.cur, 0)], go = (k) => { clear(); setI(k); setNonce(m => m + 1); const q = AC_BAR_STEPS[k]; if (q.cur >= 0) snd(key(AC_BAR[q.cur])); };
    body = <>
      <div style={titleStyle}>{title}</div>
      <div style={{textAlign:'center',fontSize:12,fontWeight:800,color:'#6d6f9c',margin:'-4px 0 6px',letterSpacing:0.4}}>{t('Example ', '예 ')}{exi + 1} / {AC_BARS.length}</div>
      {staff(st.upto, st.cur, st.bands, st.band, -1)}
      <AcKeys marks={st.cur >= 0 ? { [((key(n) % 12) + 12) % 12]: 'pick' } : {}} arcs={[]} names={{}} nonce={nonce} topRoom={4}/>
      <div style={lineStyle}>{t(st.en, st.ko)}</div>
      {row(<>
        <button className="ghost-btn" style={{...KF_BTN,minWidth:110}} onClick={() => { if (i === 0) setView('all'); else go(i - 1); }}>{t('← Back', '← 이전')}</button>
        <button className="ghost-btn" style={prim} onClick={() => { if (i === N - 1) { if (ex < AC_BARS.length - 1) { clear(); setEx(ex + 1); setView('all'); setI(0); setNonce(m => m + 1); } else { setView('try'); setC(0); setDone(false); setMiss(false); setNonce(m => m + 1); } } else go(i + 1); }}>{i === N - 1 ? (ex < AC_BARS.length - 1 ? t('Another example →', '다른 예 →') : t('Your turn →', '내가 해보기 →')) : t('Next →', '다음 →')}</button>
      </>)}
    </>;
  } else {
    const j = q.j, n = AC_BAR[j], k = ((key(n) % 12) + 12) % 12;
    const tap = (kk) => { if (done) return; clear(); snd(kk); if (((kk % 12) + 12) % 12 === k) { setDone(true); setMiss(false); } else setMiss(true); };
    const line = done ? t(NAME(n) + '. ' + q.en, NAME(n) + '. ' + q.ko) : miss ? t('Not that one. Is the note on a coloured band?', '그 건반이 아니에요. 음표가 색 띠 위에 있나요?') : t('Which key does the ringed ? note play?', '동그라미 친 ? 음표는 어느 건반일까요?');
    body = <>
      <div style={titleStyle}>{t('Your turn', '내가 해보기')}</div>
      {staff(AC_BAR.length - 1, -1, AC_BANDS.length, -1, done ? -1 : j)}
      <AcKeys marks={done ? { [k]: 'pick' } : {}} arcs={[]} names={{}} nonce={nonce + c} topRoom={4} onTap={tap}/>
      <div style={lineStyle}>{line}</div>
      {done && row(<button className="ghost-btn" style={prim} onClick={() => { setC(c + 1); setDone(false); setMiss(false); }}>{t('Another →', '하나 더 →')}</button>)}
      {row(<button className="ghost-btn" style={{...KF_BTN,minWidth:110}} onClick={() => { clear(); setEx(AC_BARS.length - 1); setView('one'); setI(AC_BARS[AC_BARS.length - 1].steps.length - 1); setNonce(m => m + 1); }}>{t('← Back', '← 이전')}</button>)}
    </>;
  }
  return <div className="try-box" data-ac-lesson="bar" style={{background:'#fff',border:'1px solid var(--border)',borderRadius:10,padding:'10px 10px 12px',margin:'4px 0 16px'}}>{body}</div>;
}
"""
s=s[:a]+NEW+s[b:]
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
