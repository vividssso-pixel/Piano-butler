import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
NEW = r"""
// lesson 7: play it. She reads three little tunes with signs and plays them key by key. Tune 1 shows the bands, tune 2 and 3 only after a wrong key.
const AC_PLAY = [
  { notes: [{ d: 32, snd: 0 }, { d: 31, sign: 1, snd: 1, g: 's' }, { d: 32, snd: 0 }, { d: 31, snd: 1, g: 's' }, { d: 31, snd: 0, bar: true }],
    bands: [{ g: 's', d: 31, from: 1, to: 'bar' }], hint: false },
  { notes: [{ d: 33, snd: 0 }, { d: 34, sign: -1, snd: -1, g: 'f' }, { d: 33, snd: 0 }, { d: 34, snd: -1, g: 'f' }, { d: 34, sign: 2, snd: 0 }, { d: 34, snd: 0, bar: true }],
    bands: [{ g: 'f', d: 34, from: 1, to: 4 }, { g: 'n', d: 34, from: 4, to: 'bar' }], hint: true },
  { notes: [{ d: 32, sign: 1, snd: 1, g: 's' }, { d: 33, snd: 0 }, { d: 32, snd: 1, g: 's' }, { d: 31, snd: 0 }, { d: 33, sign: -1, snd: -1, g: 'f', bar: true }, { d: 32, snd: 0 }, { d: 33, snd: -1, g: 'f' }],
    bands: [{ g: 's', d: 32, from: 0, to: 'bar' }, { g: 'f', d: 33, from: 4, to: 'end' }], hint: true },
];
function AcPlay() {
  const [e, setE] = useState(0), [p, setP] = useState(0), [miss, setMiss] = useState(null), [wrong, setWrong] = useState(false), [lit, setLit] = useState(-1), [nonce, setNonce] = useState(0);
  const timers = useRef([]);
  const clear = () => { timers.current.forEach(clearTimeout); timers.current = []; };
  useEffect(() => clear, []);
  const TUNE = AC_PLAY[e], NOTES = TUNE.notes, done = p >= NOTES.length;
  const snd = (k) => { if (k >= 0) playKey(k, 0.6); };
  const key = (n) => dMidiKey(n.d) + n.snd;
  const pc = (k) => ((k % 12) + 12) % 12;
  const NAME = (n) => dName(n.d) + (n.snd > 0 ? '♯' : n.snd < 0 ? '♭' : '');
  const y = (d) => dY(d) - 30;
  let x = 66; const placed = NOTES.map(n => { if (n.bar) x += 24; const px = x; x += 31; return { ...n, x: px, barX: px - 20 }; });
  const W = x + 6, bi = placed.findIndex(n => n.bar), barAt = placed[bi].barX;
  const showBands = !TUNE.hint || wrong || done;   // tune 1 always; the others only after a wrong key, or when finished
  const titleStyle = {textAlign:'center',fontFamily:"'Playfair Display', Georgia, serif",fontSize:22,fontWeight:900,color:'#26296b',lineHeight:1.2,margin:'0 0 8px',textWrap:'balance'};
  const lineStyle = {textAlign:'center',fontSize:15,fontWeight:800,color:'#26296b',margin:'8px 0 6px',minHeight:62,textWrap:'balance',wordBreak:'keep-all'};
  const prim = {...KF_BTN,minWidth:140,background:'#26296b',color:'#fffefa',borderColor:'#26296b'};
  const reset = (ne) => { clear(); setE(ne); setP(0); setMiss(null); setWrong(false); setLit(-1); setNonce(m => m + 1); };
  const tap = (kk) => {
    if (done) { snd(kk); return; }
    clear(); snd(kk);
    if (pc(kk) === pc(key(NOTES[p]))) { setP(p + 1); setMiss(null); setNonce(m => m + 1); }
    else { setMiss(pc(kk)); setWrong(true); }
  };
  const listen = () => { clear(); setLit(-1); NOTES.forEach((n, i) => timers.current.push(setTimeout(() => { setLit(i); snd(key(n)); }, 250 + i * 650))); timers.current.push(setTimeout(() => setLit(-1), 250 + NOTES.length * 650)); };
  const line = done ? t('Well played! Press Listen to hear it.', '잘 쳤어요! 듣기를 눌러 들어 봐요.')
    : miss != null ? t('Not that key. Look for a sign: just before this note, or earlier in its bar.', '그 건반이 아니에요. 임시표를 찾아요: 이 음표 바로 앞이나, 같은 마디의 앞쪽에서.')
    : p === 0 ? (e === 0 ? t('Play the notes in order, one key at a time. The band shows how far a sign reaches.', '음표를 차례로, 한 건반씩 쳐요. 띠는 임시표가 어디까지 닿는지 보여줘요.') : t('Play the notes in order. Read the signs yourself this time.', '음표를 차례로 쳐요. 이번에는 임시표를 스스로 읽어 봐요.'))
    : t(NAME(NOTES[p - 1]) + '. Next note.', NAME(NOTES[p - 1]) + '. 다음 음표.');
  const bands = showBands ? TUNE.bands : [];
  return <div className="try-box" data-ac-lesson="play" style={{background:'#fff',border:'1px solid var(--border)',borderRadius:10,padding:'10px 10px 12px',margin:'4px 0 16px'}}>
    <div style={titleStyle}>{t('Play it', '쳐 보기')}</div>
    <div style={{textAlign:'center',fontSize:12,fontWeight:800,color:'#6d6f9c',margin:'-4px 0 6px',letterSpacing:0.4}}>{t('Tune ', '곡 ')}{e + 1} / {AC_PLAY.length}</div>
    <div style={lineStyle}>{line}</div>
    <svg viewBox={`0 12 ${W} 78`} style={{width:'100%',maxWidth:360,display:'block',margin:'0 auto'}}>
      {bands.map((B, j) => { const col = AC_BAR_COL[B.g], x0 = placed[B.from].x - 17, x1 = B.to === 'bar' ? barAt - 5 : B.to === 'end' ? W - 10 : placed[B.to].x - 19;
        return <rect key={'b' + j} x={x0} y={y(B.d) - 5} width={x1 - x0} height="10" rx="3" fill={col[1]} stroke={col[0]} strokeWidth="0.9" strokeOpacity="0.6" style={{animation:'fadeUp 0.35s both'}}/>; })}
      {[30, 32, 34, 36, 38].map(d => <line key={d} x1="4" x2={W - 4} y1={y(d)} y2={y(d)} stroke="#26296b" strokeOpacity="0.55" strokeWidth="1.2"/>)}
      <ClefGlyph clef="treble" st="treble" yOf={(d) => y(d)} ink="#26296b"/>
      <line x1={barAt} x2={barAt} y1={y(38)} y2={y(30)} stroke="#26296b" strokeWidth="1.6"/>
      <line x1={W - 4} x2={W - 4} y1={y(38)} y2={y(30)} stroke="#26296b" strokeWidth="2.6"/>
      {placed.map((n, j) => {
        const played = j < p || done, ink = played && n.g ? AC_BAR_COL[n.g][0] : '#26296b', down = n.d >= 34, sgCol = n.sign === 1 ? AC_BAR_COL.s[0] : n.sign === -1 ? AC_BAR_COL.f[0] : AC_BAR_COL.n[0];
        return <g key={j}>
          {(j === p && !done || j === lit) && <circle cx={n.x} cy={y(n.d)} r="12.5" fill="none" stroke="#26296b" strokeWidth="1.8"/>}
          {n.sign === 1 && <SharpShape x={n.x - 15} y={y(n.d)} color={sgCol}/>}
          {n.sign === -1 && <FlatShape x={n.x - 14} y={y(n.d)} color={sgCol}/>}
          {n.sign === 2 && <NaturalShape x={n.x - 14} y={y(n.d)} color={sgCol}/>}
          <ellipse cx={n.x} cy={y(n.d)} rx="6.5" ry="4.7" transform={`rotate(-20 ${n.x} ${y(n.d)})`} fill={ink}/>
          {down ? <line x1={n.x - 6} x2={n.x - 6} y1={y(n.d)} y2={y(n.d) + 28} stroke={ink} strokeWidth="1.3"/> : <line x1={n.x + 6} x2={n.x + 6} y1={y(n.d)} y2={y(n.d) - 28} stroke={ink} strokeWidth="1.3"/>}
          {played && <text x={n.x} y={84} textAnchor="middle" fontSize="12" fontWeight="900" fill={n.g ? AC_BAR_COL[n.g][0] : '#6d6f9c'}>{NAME(n)}</text>}
        </g>; })}
    </svg>
    <AcKeys marks={miss != null ? { [miss]: 'bad' } : {}} arcs={[]} names={{}} nonce={nonce} topRoom={4} onTap={tap}/>
    <div style={{textAlign:'center',marginTop:14,display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap'}}>
      <button className="ghost-btn" style={{...KF_BTN,minWidth:110}} onClick={listen}>{t('▶ Listen', '▶ 듣기')}</button>
      {done && <button className="ghost-btn" style={prim} onClick={() => reset((e + 1) % AC_PLAY.length)}>{e === AC_PLAY.length - 1 ? t('Start again →', '처음부터 →') : t('Next tune →', '다음 곡 →')}</button>}
    </div>
  </div>;
}
[['ac-play', 'Play it', '쳐 보기', 'Read the signs and play three little tunes.', '임시표를 읽고 짧은 곡 세 개를 쳐요.']].forEach(([id, en, ko, benEn, bko]) => {
  TOOLS.push({ id, ch: 'concept', title: en, blurb: benEn, hidden: true, get kicker() { return TOOL_AREAS.find(a => a.id === 'pitch').name + ' · ' + (LANG === 'ko' ? '임시표' : 'Accidentals'); }, C: () => <AcPlay/> });
  TOOL_KO[id] = [ko, bko];
  const tl = TOOLS[TOOLS.length - 1], k = TOOL_KO[id], ti = tl.title, bl = tl.blurb; tl.titleEn = ti; tl.blurbEn = bl;
  Object.defineProperty(tl, 'title', { get: () => (LANG === 'ko' ? k[0] : ti), enumerable: true, configurable: true });
  Object.defineProperty(tl, 'blurb', { get: () => (LANG === 'ko' ? k[1] : bl), enumerable: true, configurable: true });
  TOOL_CONCEPT[id] = 'p-clock';
});
"""
rep("// the Toolbox: a concept's book, right under its name (open on screen, or print)\nfunction CbCard(", NEW + "// the Toolbox: a concept's book, right under its name (open on screen, or print)\nfunction CbCard(")
rep("'ac-bar', 'sac-signs', 'sac-natural', 'chromatic',", "'ac-bar', 'ac-play', 'chromatic',")
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
