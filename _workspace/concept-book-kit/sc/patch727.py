# Build BH (2026-10-27): Blues jam (her 15:04: "the blues and making things up were fun; let the feel of creative
# toys run through it all. It must be fun, and easy step by step"). A 12-bar blues band in C loops (the Styles room's
# swung boogie, without its ending chord); only the keys of the C blues scale play (C, E♭, F, F♯, G, B♭), so whatever
# the child plays fits. Easy first: three notes (C, E♭, F), then all six. The bar the band is on lights on the 12-bar
# chart; every note is kept, and 'Hear my solo' plays it back over the band. In the Styles room's Blues step, after
# Blues and swing, and in the Toolbox.
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()

def rep(old, new, n=1):
    global s
    c = s.count(old)
    assert c == n, (c, n, old[:90])
    s = s.replace(old, new)

JAM = r'''
// ══ Build BH: Blues jam ══
const JAM_B6 = [0, 3, 5, 6, 7, 10, 12, 15, 17, 18, 19, 22, 24], JAM_B3 = [0, 3, 5, 12, 15, 17, 24];   // semitones from middle C
const JAM_NM = { 0: 'C', 3: 'E♭', 5: 'F', 6: 'F♯', 7: 'G', 10: 'B♭' };
function BluesJam() {
  const tm = useRef([]), loop = useRef(null), t0 = useRef(0), solo = useRef([]), alive = useRef(true);
  const [on, setOn] = useState(null), [bar, setBar] = useState(-1), [six, setSix] = useState(false), [n, setN] = useState(0), [lit, setLit] = useState(null), [box, w] = useCpxW(420);
  const bpm = 104, barMs = 4 * 60 / bpm * 1000, ev = React.useMemo(() => csxBluesEv(12).filter(e => e[0] < 48), []);
  const keys = six ? JAM_B6 : JAM_B3;
  const clear = () => { tm.current.forEach(clearTimeout); tm.current = []; clearTimeout(loop.current); loop.current = null; };
  const stop = () => { clear(); stopClicks(); if (alive.current) { setOn(null); setBar(-1); } };
  useEffect(() => () => { alive.current = false; clear(); stopClicks(); }, []);
  const flash = (k) => { setLit(k); tm.current.push(setTimeout(() => setLit(l => (l === k ? null : l)), 220)); };
  const round = (mode) => { const sec = playEvents('piano', ev, bpm); if (!sec) { stop(); return; } t0.current = performance.now() + 100;
    for (let i = 0; i < 12; i++) tm.current.push(setTimeout(() => setBar(i), 100 + i * barMs));
    if (mode === 'solo') solo.current.forEach(({ k, at }) => tm.current.push(setTimeout(() => { playKey(k, 0.45); flash(k); }, 100 + at)));
    loop.current = setTimeout(() => { if (mode === 'solo') { stop(); return; } if (mode === 'band') round('band'); }, 100 + 12 * barMs); };
  const startBand = () => { clear(); solo.current = []; setN(0); setOn('band'); round('band'); };
  const hearSolo = () => { if (!solo.current.length) return; clear(); setOn('solo'); round('solo'); };
  const tap = (k) => { if (!keys.includes(k)) return; playKey(k, 0.45); flash(k);
    if (on === 'band') { const at = (performance.now() - t0.current) % (12 * barMs); if (solo.current.length < 200) { solo.current.push({ k, at }); setN(solo.current.length); } } };
  const kl = {}; keys.forEach(k => { kl[k] = 'pale'; }); if (lit != null) kl[lit] = 'cor';
  const names = {}; keys.forEach(k => { names[k] = JAM_NM[k % 12]; });
  return (
    <div className="try-box" style={actBox} data-jam="blues">
      <div style={actTitle}>{t('Blues jam', '블루스 잼')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>밴드가 <b>12마디 블루스</b>를 계속 돌려요. 켜진 건반은 <b>블루스 음계</b>라서 <b>아무거나</b> 쳐도 어울려요. 먼저 세 음으로, 익숙해지면 여섯 음으로. 친 음은 모두 남아서, 밴드와 함께 다시 들을 수 있어요.</>
        : <>The band plays the <b>12-bar blues</b> round and round. The lit keys are the <b>blues scale</b>, so <b>anything</b> you play fits. Start with three notes, then all six. Every note you play is kept, so you can hear your solo back with the band.</>}</div>
      {spChips([[false, t('Three notes', '세 음')], [true, t('All six', '여섯 음 모두')]], six, (v) => setSix(v))}
      <div ref={box} style={{maxWidth:420,margin:'4px auto 6px'}}><CsxBlues W={w} ch={Math.max(40, Math.round(w / 8.5))} hl={bar} label={t('The 12-bar blues in C', 'C장조 12마디 블루스')}/></div>
      <div style={{margin:'6px 0 4px'}}><SpKb lo={0} hi={24} W={22} H={88} lit={kl} names={names} onTap={tap} label={t('The blues scale', '블루스 음계')}/></div>
      <div style={{textAlign:'center',fontSize:14,fontWeight:900,color:on ? BK.coral : BK.muted,minHeight:20}}>{on === 'band' ? t('Your turn: play along! Notes kept: ' + n, '이제 같이 쳐요! 남은 음: ' + n) : on === 'solo' ? t('Your solo, with the band', '내 솔로, 밴드와 함께') : n ? t(n + ' notes kept', n + '개 음이 남아 있어요') : t('Start the band, then play', '밴드를 켜고, 쳐요')}</div>
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        {on ? <button className="ghost-btn" style={spBtn} onClick={stop}>{t('■ Stop', '■ 멈추기')}</button> : <button className="ghost-btn" style={spBtn} onClick={startBand}>{t('▶ Start the band', '▶ 밴드 켜기')}</button>}
        <button className="ghost-btn" style={spBtn} disabled={!n || on === 'solo'} onClick={hearSolo}>{t('▶ Hear my solo', '▶ 내 솔로 듣기')}</button>
      </div>
    </div>
  );
}
'''
rep("const csxBluesEv = (bars = 12) => { const ev = [];", JAM.replace('function BluesJam', 'function BluesJam') + "const csxBluesEv = (bars = 12) => { const ev = [];")
# the Styles room's Blues step: the jam after Blues and swing
rep("], X('Blues: three chords, twelve bars. Jazz swings and improvises.', '블루스는 세 화음, 열두 마디. 재즈는 스윙하고 즉흥 연주해요.'), <CsxBluesPad/>),",
    "], X('Blues: three chords, twelve bars. Jazz swings and improvises.', '블루스는 세 화음, 열두 마디. 재즈는 스윙하고 즉흥 연주해요.'), <><CsxBluesPad/><div style={{height:12}}/><BluesJam/></>),")
rep("      X('Play quavers on one note, straight, then swung: long-short.', '한 음으로 8분음표를 스트레이트로, 그다음 스윙으로 쳐요: 길게-짧게.'),\n    ], X('Blues: three chords",
    "      X('Play quavers on one note, straight, then swung: long-short.', '한 음으로 8분음표를 스트레이트로, 그다음 스윙으로 쳐요: 길게-짧게.'),\n      X('Make up a blues: your teacher plays the 12 bars, you play any notes of C, E♭, F, F♯, G, B♭ on top.', '블루스 지어 보기: 선생님이 12마디를 치는 동안, C, E♭, F, F♯, G, B♭ 중 아무 음이나 위에서 쳐요.'),\n    ], X('Blues: three chords")
# the Toolbox and the Home's Styles room
rep("  { id: 'csx-blues', ch: 'styles', title: 'Blues and swing', blurb: 'The 12-bar blues swung, a missing chord to find, and straight against swing.', C: () => <CsxBluesPad/> },",
    "  { id: 'csx-blues', ch: 'styles', title: 'Blues and swing', blurb: 'The 12-bar blues swung, a missing chord to find, and straight against swing.', C: () => <CsxBluesPad/> },\n"
    "  { id: 'csx-jam', ch: 'styles', title: 'Blues jam', blurb: 'A blues band in C: play any lit key, then hear your solo back.', C: () => <BluesJam/> },   // Build BH")
rep("  'csx-blues': ['블루스와 스윙', '스윙으로 듣는 12마디 블루스, 빠진 화음 찾기, 스트레이트와 스윙.'],",
    "  'csx-blues': ['블루스와 스윙', '스윙으로 듣는 12마디 블루스, 빠진 화음 찾기, 스트레이트와 스윙.'],\n  'csx-jam': ['블루스 잼', 'C장조 블루스 밴드: 켜진 건반 아무거나, 그다음 내 솔로 듣기.'],")
rep("'csx-blues': ['about', 1, 3, 'show ear game'],", "'csx-blues': ['about', 1, 3, 'show ear game'], 'csx-jam': ['about', 0, 3, 'show ear game'],")
rep("  'csx-blues': () => (\n", "  'csx-jam': () => (\n    <svg width=\"34\" height=\"34\" viewBox=\"0 0 24 24\"><rect width=\"24\" height=\"24\" rx=\"6\" fill=\"#3f9a7e\"/><rect x=\"3\" y=\"9\" width=\"18\" height=\"11\" rx=\"1.5\" fill=\"#fefbf3\"/>{[6, 9, 14, 17].map(x => <rect key={x} x={x} y=\"9\" width=\"2.2\" height=\"6.5\" fill=\"#26296b\"/>)}<path d=\"M15 3 V7.5\" stroke=\"#e9a83a\" strokeWidth=\"1.4\"/><ellipse cx=\"13.8\" cy=\"7.6\" rx=\"1.6\" ry=\"1.2\" fill=\"#e9a83a\"/></svg>\n  ),\n  'csx-blues': () => (\n")
rep("  'styles': ['csx-map', 'csx-texture', 'csx-era', 'csx-penta', 'csx-blues', 'csx-pop', 'csx-ear'],",
    "  'styles': ['csx-map', 'csx-texture', 'csx-era', 'csx-penta', 'csx-blues', 'csx-jam', 'csx-pop', 'csx-ear'],")

rep("'csx-blues': 'about'", "'csx-blues': 'about', 'csx-jam': 'about'")
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
