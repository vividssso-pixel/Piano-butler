# Build BJ (2026-10-27): call 25, batch 2: three more toys to make with. Loud and soft, your way (Dynamics): the first
# line of Beethoven's Ode to Joy plays while the child taps pp to ff; every note keeps the sign it was played at, drawn
# as bars whose height is the loudness, then heard back. Drive the tempo (Tempo): Twinkle (the French song 'Ah vous
# dirai-je, maman') goes round while the child speeds it up or slows it down; the Italian word and the metronome mark
# follow (the room's own speeds: Largo 40-60 … Presto 168-200), and the change is named: accelerando, ritardando.
# Bright or dark? (Minor scales): play a tune on C D E F G, then hear it with the bright 3rd (E) or the darker one
# (E♭), the minor scales room's own words.
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()

def rep(old, new, n=1):
    global s
    c = s.count(old)
    assert c == n, (c, n, old[:90])
    s = s.replace(old, new)

CODE = r'''
// ══ Build BJ: three more toys to make with (call 25, batch 2) ══
// a tune played note by note on the audio clock, a little ahead: speed and loudness are read as each note is scheduled
function liveTune(o) {   // o: { notes: [[semitones from middle C, beats]], bpm: () => n, vol: (i) => v, onNote: (i) => {}, loop, onEnd }
  const ctx = getAudio(); if (!ctx) return () => {};
  let i = 0, next = ctx.currentTime + 0.12, stopped = false, done = false; const tms = [];
  const tick = () => { if (stopped || done) return; while (next < ctx.currentTime + 0.15) {
      if (i >= o.notes.length) { if (o.loop) i = 0; else { done = true; clearInterval(id); tms.push(setTimeout(() => { if (!stopped && o.onEnd) o.onEnd(); }, Math.max(0, (next - ctx.currentTime) * 1000))); return; } }
      const [k, d] = o.notes[i], spb = 60 / o.bpm(), j = i;
      if (k != null) blip(ctx, next, mFreq(60 + k), d * spb * 0.92, o.vol ? o.vol(j) : 0.22, 'triangle');
      tms.push(setTimeout(() => { if (!stopped && o.onNote) o.onNote(j); }, Math.max(0, (next - ctx.currentTime) * 1000)));
      if (tms.length > 80) tms.splice(0, 40);
      next += d * spb; i++; } };
  const id = setInterval(tick, 40); tick();
  return () => { stopped = true; clearInterval(id); tms.forEach(clearTimeout); stopClicks(); };
}
const DS_TUNE = [[4, 1], [4, 1], [5, 1], [7, 1], [7, 1], [5, 1], [4, 1], [2, 1], [0, 1], [0, 1], [2, 1], [4, 1], [4, 1.5], [2, 0.5], [2, 2]];   // Ode to Joy, its first line
const DS_SIGNS = ['pp', 'p', 'mp', 'mf', 'f', 'ff'], DS_NM = { 0: 'C', 2: 'D', 4: 'E', 5: 'F', 7: 'G', 9: 'A' };
function DsBars({ rec, cur }) {   // one bar a note: the louder, the taller; the sign written where it changes
  const n = DS_TUNE.length, W = 330, cw = W / n, H = 112, base = 86;
  return <svg viewBox={'0 0 ' + W + ' ' + H} style={{width:'100%',maxWidth:420,display:'block',margin:'4px auto'}} role="img" aria-label={t('The loudness of each note', '음마다의 셈여림')}>
    <line x1="0" x2={W} y1={base + 0.5} y2={base + 0.5} stroke="rgba(38,41,107,0.25)"/>
    {DS_TUNE.map(([k], i) => { const sgn = rec[i], h = sgn ? 8 + DS_SIGNS.indexOf(sgn) * 11 : 4, on = cur === i;
      return <g key={i}><rect x={i * cw + 3} y={base - h} width={cw - 6} height={h} rx="3" fill={on ? '#e4572e' : sgn ? '#26296b' : 'rgba(38,41,107,0.18)'}/>
        <text x={i * cw + cw / 2} y={base + 16} textAnchor="middle" fontSize="11" fontWeight="800" fill="#6d6f9c">{DS_NM[k]}</text>
        {sgn && sgn !== rec[i - 1] && <text x={i * cw + cw / 2} y={base - h - 6} textAnchor="middle" style={{fontFamily:SDY_FONT,fontStyle:'italic',fontWeight:900,fontSize:15}} fill="#26296b">{sgn}</text>}</g>; })}
  </svg>;
}
function DynShape() {
  const [lv, setLv] = useState('mf'), [rec, setRec] = useState([]), [cur, setCur] = useState(-1), [mode, setMode] = useState(null);
  const lvRef = useRef('mf'), recRef = useRef([]), stopRef = useRef(null);
  useEffect(() => () => { if (stopRef.current) stopRef.current(); }, []);
  const pickLv = (x) => { setLv(x); lvRef.current = x; };
  const go = (m) => { if (stopRef.current) stopRef.current(); setMode(m); setCur(-1); if (m === 'make') { recRef.current = []; setRec([]); }
    const R = m === 'back' ? recRef.current.slice() : null;
    stopRef.current = liveTune({ notes: DS_TUNE, bpm: () => 100, vol: (i) => { const x = R ? R[i] || 'mf' : lvRef.current; if (!R) recRef.current[i] = x; return SDY_VOL[x]; },
      onNote: (i) => { setCur(i); if (!R) setRec(recRef.current.slice()); }, onEnd: () => { setMode(null); setCur(-1); stopRef.current = null; } }); };
  const stop = () => { if (stopRef.current) stopRef.current(); stopRef.current = null; setMode(null); setCur(-1); };
  const all = rec.length >= DS_TUNE.length, flat = all && rec.every(x => x === rec[0]);
  return (
    <div className="try-box" style={actBox} data-ds="dyn">
      <div style={actTitle}>{t('Loud and soft, your way', '셈여림, 내 마음대로')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>“환희의 송가”(베토벤)의 첫 줄이 나오는 동안 <b>pp에서 ff까지</b> 눌러요. 음마다 그때의 셈여림이 남아서 막대 높이로 보여요. 그다음 내가 만든 대로 다시 들어요.</> : <>While the first line of Beethoven’s <b>Ode to Joy</b> plays, tap <b>pp to ff</b>. Each note keeps the sign it was played at, drawn as a bar: the louder, the taller. Then hear it back, your way.</>}</div>
      <div style={{display:'grid',gridTemplateColumns:'repeat(6,minmax(0,1fr))',gap:6,margin:'4px 0 6px'}}>{DS_SIGNS.map(x => <button key={x} type="button" onClick={() => pickLv(x)} aria-pressed={lv === x} style={{padding:'8px 0',borderRadius:12,cursor:'pointer',background:lv === x ? BK.ink : '#fff',color:lv === x ? '#fff' : BK.ink,border:'2px solid ' + BK.ink}}>{sdyBig(x, 22)}</button>)}</div>
      <DsBars rec={rec} cur={cur}/>
      <div style={{textAlign:'center',fontSize:14,fontWeight:900,minHeight:20,color:mode ? BK.coral : BK.muted}}>{mode === 'make' ? t('Tap the signs as it plays!', '나오는 동안 기호를 눌러요!') : mode === 'back' ? t('Your way', '내가 만든 셈여림') : !rec.length ? t('Choose where to start, then ▶ Play and shape it', '처음 셈여림을 고르고 ▶ 치면서 만들기') : flat ? t('All one sign: try growing from pp to ff', '모두 같은 기호예요: pp에서 ff까지 점점 키워 봐요') : t('Hear it back!', '다시 들어 봐요!')}</div>
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        {mode ? <button className="ghost-btn" style={spBtn} onClick={stop}>{t('■ Stop', '■ 멈추기')}</button> : <button className="ghost-btn" style={spBtn} onClick={() => go('make')}>{t('▶ Play and shape it', '▶ 치면서 만들기')}</button>}
        <button className="ghost-btn" style={spBtn} disabled={!all || !!mode} onClick={() => go('back')}>{t('▶ Hear it back', '▶ 다시 듣기')}</button>
      </div>
    </div>
  );
}

const TD_TUNE = [[0, 1], [0, 1], [7, 1], [7, 1], [9, 1], [9, 1], [7, 2], [5, 1], [5, 1], [4, 1], [4, 1], [2, 1], [2, 1], [0, 2]];   // Twinkle ('Ah vous dirai-je, maman')
const TD_WORDS = [['Largo', 40, 60, '라르고'], ['Adagio', 60, 76, '아다지오'], ['Andante', 76, 108, '안단테'], ['Moderato', 108, 120, '모데라토'], ['Allegro', 120, 168, '알레그로'], ['Presto', 168, 201, '프레스토']];   // the Tempo room's own speeds
const tdWord = (b) => TD_WORDS.find(([, a, z]) => b >= a && b < z) || TD_WORDS[0];
function TempoDrive() {
  const [bpm, setBpm] = useState(92), [on, setOn] = useState(false), [cur, setCur] = useState(-1), [chg, setChg] = useState(null);
  const bRef = useRef(92), stopRef = useRef(null), chgT = useRef(null);
  useEffect(() => () => { if (stopRef.current) stopRef.current(); clearTimeout(chgT.current); }, []);
  const set = (b) => { const v = Math.max(40, Math.min(200, Math.round(b))); setChg(v > bRef.current ? 'up' : v < bRef.current ? 'down' : null); bRef.current = v; setBpm(v); clearTimeout(chgT.current); chgT.current = setTimeout(() => setChg(null), 1600); };
  const start = () => { if (stopRef.current) stopRef.current(); setOn(true); stopRef.current = liveTune({ notes: TD_TUNE, bpm: () => bRef.current, loop: true, onNote: setCur }); };
  const stop = () => { if (stopRef.current) stopRef.current(); stopRef.current = null; setOn(false); setCur(-1); };
  const w = tdWord(bpm);
  return (
    <div className="try-box" style={actBox} data-td="tempo">
      <div style={actTitle}>{t('Drive the tempo', '빠르기 운전')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>“반짝반짝 작은 별”이 계속 돌아요. <b>빠르게, 느리게</b>를 눌러서 빠르기를 바꿔요. 이탈리아어 빠르기말과 메트로놈 숫자가 따라와요.</> : <>Twinkle goes round and round. Press <b>Faster</b> and <b>Slower</b> to change the speed. The Italian word and the metronome mark follow you.</>}</div>
      <div style={{textAlign:'center',margin:'6px 0 2px'}}><div style={{fontFamily:LB_SERIF,fontStyle:'italic',fontSize:34,fontWeight:900,color:BK.ink,lineHeight:1.1}}>{w[0]}</div>
        <div style={{fontSize:13,fontWeight:800,color:BK.muted}}>{LANG === 'ko' ? w[3] : ''}</div>
        <div style={{fontSize:20,fontWeight:900,color:BK.coral,marginTop:2}}>{spMM(bpm)}</div>
        <div style={{fontSize:13.5,fontWeight:900,color:BK.coral,minHeight:18}}>{chg === 'up' ? t('accelerando: getting faster', '아첼레란도: 점점 빠르게') : chg === 'down' ? t('ritardando: getting slower', '리타르단도: 점점 느리게') : ''}</div></div>
      <div style={{display:'flex',gap:4,justifyContent:'center',flexWrap:'wrap',margin:'6px 0'}}>{TD_TUNE.map(([k, d], i) => <span key={i} style={{width:d * 18 + (d - 1) * 4,height:18,borderRadius:9,background:cur === i ? BK.coral : '#fff',border:'2px solid ' + (cur === i ? BK.coral : BK.ink)}}/>)}</div>
      <input type="range" min="40" max="200" step="1" value={bpm} onChange={(e) => set(+e.target.value)} aria-label={t('Speed', '빠르기')} style={{width:'100%',accentColor:'#26296b'}}/>
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={spBtn} onClick={() => set(bRef.current - 8)}>{t('◀ Slower', '◀ 느리게')}</button>
        {on ? <button className="ghost-btn" style={spBtn} onClick={stop}>{t('■ Stop', '■ 멈추기')}</button> : <button className="ghost-btn" style={spBtn} onClick={start}>{t('▶ Play', '▶ 듣기')}</button>}
        <button className="ghost-btn" style={spBtn} onClick={() => set(bRef.current + 8)}>{t('Faster ▶', '빠르게 ▶')}</button>
      </div>
    </div>
  );
}

// Bright or dark? a tune on C D E F G, heard with the bright 3rd (E) or the darker one (E♭)
const BD_KEYS = [0, 2, 4, 5, 7], BD_NM = { 0: 'C', 2: 'D', 3: 'E♭', 4: 'E', 5: 'F', 7: 'G' };
function BrightDark() {
  const [notes, setNotes] = useState([]), [dark, setDark] = useState(false), [cur, setCur] = useState(-1), [on, setOn] = useState(false);
  const last = useRef(0), stopRef = useRef(null);
  useEffect(() => () => { if (stopRef.current) stopRef.current(); }, []);
  const third = dark ? 3 : 4, map = (k) => (k === 4 ? third : k);
  const tap = (k) => { if (!BD_KEYS.map(map).includes(k)) return; const real = k === third ? 4 : k; playKey(k, 0.5); if (on) return;
    const now = performance.now(), gap = last.current ? Math.min(2, Math.max(0.5, Math.round((now - last.current) / 600 * 2) / 2)) : 1; last.current = now;
    setNotes(ns => { const out = ns.slice(); if (out.length) out[out.length - 1] = [out[out.length - 1][0], gap]; if (out.length < 24) out.push([real, 1]); return out; }); };
  const play = (dk) => { if (stopRef.current) stopRef.current(); setDark(dk); setOn(true); const th = dk ? 3 : 4;
    stopRef.current = liveTune({ notes: notes.map(([k, d]) => [k === 4 ? th : k, d]), bpm: () => 100, onNote: setCur, onEnd: () => { setOn(false); setCur(-1); stopRef.current = null; } }); };
  const kl = {}; BD_KEYS.forEach(k => { kl[map(k)] = map(k) === third ? 'cor' : 'pale'; }); const names = {}; BD_KEYS.forEach(k => { names[map(k)] = BD_NM[map(k)]; });
  return (
    <div className="try-box" style={actBox} data-bd="pad">
      <div style={actTitle}>{t('Bright or dark?', '밝게? 어둡게?')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>C D E F G로 <b>나만의 가락</b>을 쳐요(또는 “환희의 송가”를 불러와요). 그다음 <b>밝은 셋째 음</b>(E)으로, <b>어두운 셋째 음</b>(E♭)으로 들어 봐요. 셋째 음 하나로 장조와 단조가 갈려요.</> : <>Play <b>your own tune</b> on C D E F G (or load Ode to Joy). Then hear it with the <b>bright 3rd</b> (E), and with the <b>darker 3rd</b> (E♭). One note, the 3rd, makes it major or minor.</>}</div>
      {spChips([[false, t('Bright: E (major)', '밝게: E (장조)')], [true, t('Dark: E♭ (minor)', '어둡게: E♭ (단조)')]], dark, (v) => setDark(v))}
      <div style={{display:'flex',gap:4,justifyContent:'center',flexWrap:'wrap',margin:'8px 0 4px',minHeight:34}}>{notes.length ? notes.map(([k, d], i) => { const m = map(k), c = cur === i;
        return <span key={i} style={{minWidth:d * 26,height:30,borderRadius:15,padding:'0 6px',boxSizing:'border-box',display:'inline-flex',alignItems:'center',justifyContent:'center',fontSize:14,fontWeight:900,background:c ? BK.coral : m === third ? '#fbe3da' : '#fff',border:'2px solid ' + (c ? BK.coral : BK.ink),color:c ? '#fff' : BK.ink}}>{BD_NM[m]}</span>; })
        : <span style={{fontSize:13.5,fontWeight:800,color:BK.muted,alignSelf:'center'}}>{t('Your tune appears here', '내 가락이 여기 나와요')}</span>}</div>
      <div style={{margin:'6px 0 4px'}}><SpKb lo={0} hi={7} W={40} H={96} lit={kl} names={names} onTap={tap} label={t('C D E F G', 'C D E F G')}/></div>
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={spBtn} disabled={!notes.length || on} onClick={() => play(false)}>{t('▶ Hear it bright', '▶ 밝게 듣기')}</button>
        <button className="ghost-btn" style={spBtn} disabled={!notes.length || on} onClick={() => play(true)}>{t('▶ Hear it dark', '▶ 어둡게 듣기')}</button>
        <button className="ghost-btn" style={spBtn} disabled={on} onClick={() => { last.current = 0; setNotes(DS_TUNE.slice()); }}>{t('Ode to Joy', '환희의 송가')}</button>
        <button className="ghost-btn" style={spBtn} disabled={!notes.length || on} onClick={() => { last.current = 0; setNotes([]); }}>{t('Clear', '지우기')}</button>
      </div>
    </div>
  );
}
'''
rep("// ══ Build BH: Blues jam ══", CODE + "\n// ══ Build BH: Blues jam ══")

rep("  { id: 'csx-jam', ch: 'styles', title: 'Blues jam',",
    "  { id: 'mk-dyn', ch: 'dynamics', title: 'Loud and soft, your way', blurb: 'Ode to Joy plays; tap pp to ff and shape it, then hear it back.', C: () => <DynShape/> },   // Build BJ\n"
    "  { id: 'mk-tempo', ch: 'tempo', title: 'Drive the tempo', blurb: 'Speed Twinkle up and slow it down; the Italian word follows.', C: () => <TempoDrive/> },\n"
    "  { id: 'mk-mm', ch: 'minor-scales', title: 'Bright or dark?', blurb: 'Your tune on C D E F G with the bright 3rd, then the darker one.', C: () => <BrightDark/> },\n"
    "  { id: 'csx-jam', ch: 'styles', title: 'Blues jam',")
rep("  'csx-jam': ['블루스 잼',", "  'mk-dyn': ['셈여림, 내 마음대로', '환희의 송가가 나오는 동안 pp에서 ff까지 눌러 만들고, 다시 들어요.'],\n  'mk-tempo': ['빠르기 운전', '반짝반짝 작은 별을 빠르게, 느리게. 이탈리아어 빠르기말이 따라와요.'],\n  'mk-mm': ['밝게? 어둡게?', 'C D E F G로 친 내 가락을 밝은 셋째 음으로, 그다음 어두운 셋째 음으로.'],\n  'csx-jam': ['블루스 잼',")
rep("'csx-jam': ['about', 0, 3, 'show ear game'],", "'csx-jam': ['about', 0, 3, 'show ear game'], 'mk-dyn': ['expression', 0, 1, 'game ear'], 'mk-tempo': ['rtempo', 0, 2, 'game ear'], 'mk-mm': ['scales', 1, 2, 'game ear'],")
rep("'csx-jam': 'about'", "'csx-jam': 'about', 'mk-dyn': 't-touch', 'mk-tempo': 't-tempo', 'mk-mm': 'p-scales'")
rep("  'csx-jam': () => (\n",
    "  'mk-dyn': () => (\n    <svg width=\"34\" height=\"34\" viewBox=\"0 0 24 24\"><rect width=\"24\" height=\"24\" rx=\"6\" fill=\"#cf5248\"/>{[3, 6, 9, 12, 9].map((h, i) => <rect key={i} x={3 + i * 3.8} y={19 - h} width=\"2.8\" height={h} rx=\"1\" fill={i === 3 ? '#e9a83a' : '#fefbf3'}/>)}</svg>\n  ),\n"
    "  'mk-tempo': () => (\n    <svg width=\"34\" height=\"34\" viewBox=\"0 0 24 24\"><rect width=\"24\" height=\"24\" rx=\"6\" fill=\"#3b4fa8\"/><path d=\"M4 16 A8 8 0 0 1 20 16\" fill=\"none\" stroke=\"#fefbf3\" strokeWidth=\"2\"/><path d=\"M12 16 L17 9\" stroke=\"#e9a83a\" strokeWidth=\"2\" strokeLinecap=\"round\"/></svg>\n  ),\n"
    "  'mk-mm': () => (\n    <svg width=\"34\" height=\"34\" viewBox=\"0 0 24 24\"><rect width=\"24\" height=\"24\" rx=\"6\" fill=\"#5a4fa0\"/><circle cx=\"8\" cy=\"12\" r=\"4.5\" fill=\"#e9a83a\"/><path d=\"M18.5 7.5 A5 5 0 1 0 18.5 16.5 A4 4 0 1 1 18.5 7.5 Z\" fill=\"#fefbf3\"/></svg>\n  ),\n"
    "  'csx-jam': () => (\n")
rep("  'dynamics': ['sdy-pf', 'sdy-ladder', 'sdy-hair', 'sdy-touch', 'sdy-tie', 'dyn-order', 'hairpin', 'touch-ear', 'touch-lengths', 'pedal']",
    "  'dynamics': ['sdy-pf', 'sdy-ladder', 'sdy-hair', 'sdy-touch', 'sdy-tie', 'mk-dyn', 'dyn-order', 'hairpin', 'touch-ear', 'touch-lengths', 'pedal']")
rep("  'tempo': ['stm-sf', 'stm-words', 'stm-read', 'stm-metro', 'stm-steady', ", "  'tempo': ['stm-sf', 'stm-words', 'stm-read', 'stm-metro', 'stm-steady', 'mk-tempo', ")
rep("lessons: ['sdy-pf', 'sdy-ladder', 'sdy-hair', 'hairpin', 'tmx-vol', 'dyn-order']", "lessons: ['sdy-pf', 'sdy-ladder', 'sdy-hair', 'hairpin', 'tmx-vol', 'dyn-order', 'mk-dyn']")
rep("lessons: ['stm-sf', 'stm-words', 'stm-read', 'stm-metro', 'stm-steady', 'tmx-speed', 'tmx-change', 'speed-change']", "lessons: ['stm-sf', 'stm-words', 'stm-read', 'stm-metro', 'stm-steady', 'tmx-speed', 'tmx-change', 'speed-change', 'mk-tempo']")
rep("lessons: ['ms-third', 'ms-rel', 'ms-har', 'ms-gaps', 'ms-ear', 'sc-min'], check: 'minor-scales' }", "lessons: ['ms-third', 'ms-rel', 'ms-har', 'ms-gaps', 'ms-ear', 'sc-min', 'mk-mm'], check: 'minor-scales' }")

open(dst, 'w', encoding='utf-8').write(s)
print('ok')
