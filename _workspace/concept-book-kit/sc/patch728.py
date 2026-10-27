# Build BI (2026-10-27): three toys to make with, the first of call 25 (her 15:04: "the feel of creative toys
# everywhere; it must be fun, and easy step by step"). My beat band (Pulse): two bars of claps, stamps, pats and silent
# beats, looped at three speeds, beat 1 marked as the strong one. Question and answer (Steps and skips): the app asks
# two bars in C position, the child answers in the same rhythm on C D E F G, and hears both; ending on C sounds
# finished. Four-chord loop (Chords): I, IV, V and vi looped by a little band, the chord's own notes lit as the safe
# ones to play, every note kept to hear back.
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()

def rep(old, new, n=1):
    global s
    c = s.count(old)
    assert c == n, (c, n, old[:90])
    s = s.replace(old, new)

CODE = r'''
// ══ Build BI: three toys to make with (call 25) ══
// body percussion from the click's noise and a low thump: clap (three quick bursts), stamp (a deep thud), pat (a soft knock)
function bodyHit(ctx, t, kind, vol = 0.5) {
  const out = ctx.createGain(); out.gain.value = vol; out.connect(ctx.destination);
  const burst = (at, f0, q, dec, lv) => { const n = ctx.createBufferSource(), f = ctx.createBiquadFilter(), g = ctx.createGain(); n.buffer = noiseBuf(ctx); f.type = 'bandpass'; f.frequency.value = f0; f.Q.value = q;
    g.gain.setValueAtTime(0, at); g.gain.linearRampToValueAtTime(lv, at + 0.002); g.gain.exponentialRampToValueAtTime(0.0005, at + dec); n.connect(f); f.connect(g); g.connect(out); n.start(at); n.stop(at + dec + 0.02); _clickNodes.push(n); };
  const thump = (at, f1, f2, dec, lv) => { const o = ctx.createOscillator(), g = ctx.createGain(); o.type = 'sine'; o.frequency.setValueAtTime(f1, at); o.frequency.exponentialRampToValueAtTime(f2, at + dec);
    g.gain.setValueAtTime(0, at); g.gain.linearRampToValueAtTime(lv, at + 0.004); g.gain.exponentialRampToValueAtTime(0.0005, at + dec); o.connect(g); g.connect(out); o.start(at); o.stop(at + dec + 0.02); _clickNodes.push(o); };
  if (kind === 'clap') [0, 0.011, 0.022].forEach((d, i) => burst(t + d, 1400, 1.2, i === 2 ? 0.12 : 0.03, 1.6));
  else if (kind === 'stamp') { thump(t, 95, 42, 0.28, 1.4); burst(t, 220, 0.8, 0.06, 0.9); }
  else if (kind === 'pat') { thump(t, 210, 130, 0.12, 0.9); burst(t, 900, 1, 0.04, 0.6); }
}
const BB_KINDS = ['clap', 'stamp', 'pat', 'rest'];
const BB_WORD = { clap: ['clap', '손뼉'], stamp: ['stamp', '발'], pat: ['pat', '무릎'], rest: ['rest', '쉼'] };
const bbIcon = (k, c) => <svg viewBox="0 0 32 24" style={{width:34,height:26,display:'block',margin:'0 auto'}} aria-hidden="true">{
  k === 'clap' ? <g fill="none" stroke={c} strokeWidth="2.2" strokeLinecap="round"><path d="M9 20 L13 6 Q14 3 16 5 L15 20"/><path d="M23 20 L19 6 Q18 3 16 5"/><path d="M5 6 L7 8 M27 6 L25 8 M16 1 V3"/></g>
  : k === 'stamp' ? <g fill={c}><path d="M7 19 Q6 12 10 9 L14 9 Q15 14 22 15 Q27 16 26 19 Z"/><rect x="4" y="21" width="24" height="2" rx="1" opacity="0.5"/></g>
  : k === 'pat' ? <g fill="none" stroke={c} strokeWidth="2.2" strokeLinecap="round"><path d="M4 20 Q10 10 18 12 Q24 13 28 20"/><path d="M13 3 V9 M17 2 V9 M21 3 V9 M10 6 Q11 10 13 10"/></g>
  : <path d="M14 3 L19 9 L15 13 L19 18 Q14 16 15 21 Q10 17 14 14 L11 9 Z" fill={c}/>}</svg>;
const BB_START = { 4: ['clap', 'pat', 'pat', 'pat', 'clap', 'pat', 'stamp', 'rest'], 3: ['stamp', 'clap', 'clap', 'stamp', 'clap', 'rest'] };
function BeatBand() {
  const [beats, setBeats] = useState(4), [cells, setCells] = useState(BB_START[4]), [bpm, setBpm] = useState(88), [on, setOn] = useState(false), [cur, setCur] = useState(-1);
  const sched = useRef(null), next = useRef(0), step = useRef(0), tms = useRef([]), st = useRef({}); st.current = { cells, beats, bpm };
  const stop = () => { clearInterval(sched.current); sched.current = null; tms.current.forEach(clearTimeout); tms.current = []; setOn(false); setCur(-1); };
  useEffect(() => () => { clearInterval(sched.current); tms.current.forEach(clearTimeout); }, []);
  const start = () => { const ctx = getAudio(); if (!ctx) return; stop(); next.current = ctx.currentTime + 0.12; step.current = 0;
    const tick = () => { const S = st.current, N = S.beats * 2; while (next.current < ctx.currentTime + 0.3) { const i = step.current % N, tt = next.current, k = S.cells[i];
        metroClick(ctx, tt, i % S.beats === 0, 0.06); if (k && k !== 'rest') bodyHit(ctx, tt, k, 0.5);
        tms.current.push(setTimeout(() => setCur(i), Math.max(0, (tt - ctx.currentTime) * 1000))); if (tms.current.length > 64) tms.current = tms.current.slice(-32);
        step.current++; next.current += 60 / S.bpm; } };
    tick(); sched.current = setInterval(tick, 60); setOn(true); };
  const flip = (i) => setCells(c => c.map((x, j) => (j === i ? BB_KINDS[(BB_KINDS.indexOf(x) + 1) % 4] : x)));
  const setB = (b) => { setBeats(b); setCells(BB_START[b]); step.current = 0; };
  const surprise = () => setCells(c => c.map((x, j) => (j % beats === 0 ? (Math.random() < 0.5 ? 'stamp' : 'clap') : BB_KINDS[Math.floor(Math.random() * 4)])));
  const bar = (b) => <div style={{display:'grid',gridTemplateColumns:'repeat(' + beats + ',minmax(0,1fr))',gap:6}}>{Array.from({ length: beats }, (_, j) => { const i = b * beats + j, k = cells[i], lit = cur === i, strong = j === 0;
    return <button key={i} type="button" onClick={() => flip(i)} aria-label={t('Beat ' + (j + 1) + ': ' + BB_WORD[k][0], (j + 1) + '박: ' + BB_WORD[k][1])} style={{padding:'6px 2px 5px',borderRadius:12,cursor:'pointer',background:lit ? BK.coral : '#fff',border:(strong ? 3 : 1.5) + 'px solid ' + (lit ? BK.coral : BK.ink),color:lit ? '#fff' : BK.ink,transition:'background 0.08s'}}>
      <div style={{fontSize:11,fontWeight:900,opacity:0.7}}>{j + 1}</div>{bbIcon(k, lit ? '#fff' : k === 'rest' ? BK.muted : BK.ink)}<div style={{fontSize:12.5,fontWeight:900,marginTop:2}}>{t(BB_WORD[k][0], BB_WORD[k][1])}</div></button>; })}</div>;
  return (
    <div className="try-box" style={actBox} data-bb="band">
      <div style={actTitle}>{t('My beat band', '나의 박 밴드')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>칸을 누를 때마다 <b>손뼉, 발, 무릎, 쉼</b>으로 바뀌어요. 1박(굵은 칸)이 센박이에요. 밴드를 켜고 같이 쳐요. 쉼에서도 박은 계속 가요.</> : <>Tap a box to change it: <b>clap, stamp, pat, rest</b>. Beat 1 (the thick box) is the strong one. Start the band and play along. On a rest the beat keeps going.</>}</div>
      {spChips([[4, t('Four beats', '네 박')], [3, t('Three beats', '세 박')]], beats, setB)}
      <div style={{display:'grid',gap:8,margin:'8px 0'}}>{bar(0)}{bar(1)}</div>
      {spChips([[66, t('Slow', '느리게')], [88, t('Walking', '걷는 빠르기')], [112, t('Fast', '빠르게')]], bpm, setBpm)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        {on ? <button className="ghost-btn" style={spBtn} onClick={stop}>{t('■ Stop', '■ 멈추기')}</button> : <button className="ghost-btn" style={spBtn} onClick={start}>{t('▶ Start the band', '▶ 밴드 켜기')}</button>}
        <button className="ghost-btn" style={spBtn} onClick={surprise}>{t('▶ Surprise me', '▶ 아무거나')}</button>
      </div>
    </div>
  );
}

// Question and answer: two bars in C position asked by the app (each ends away from home), answered in the same rhythm
const QA_Q = [[[0, 1], [4, 1], [7, 1], [4, 1], [2, 4]], [[4, 1], [2, 1], [0, 1], [2, 1], [4, 1], [4, 1], [7, 2]], [[7, 1], [5, 1], [4, 1], [2, 1], [4, 2], [2, 2]],
  [[7, 1], [4, 1], [5, 1], [2, 1], [4, 1], [0, 1], [2, 2]], [[4, 1], [5, 1], [7, 1], [4, 1], [5, 2], [2, 2]], [[2, 1], [4, 1], [5, 1], [7, 1], [4, 2], [7, 2]]];
const QA_KEYS = [0, 2, 4, 5, 7], QA_NM = { 0: 'C', 2: 'D', 4: 'E', 5: 'F', 7: 'G' };
const qaEv = (q, a, from = 0) => { const ev = []; let b = from; q.forEach(([k, d], j) => { const m = a ? a[j] : k; if (m != null) ev.push([b, 60 + m, d * 0.95, 0.55]); b += d; }); return ev; };
function QaPills({ q, ans, lit, who }) {
  return <div style={{display:'flex',gap:4,justifyContent:'center',alignItems:'flex-end',flexWrap:'wrap',margin:'4px 0'}}>{q.map(([k, d], j) => { const v = ans ? ans[j] : k, on = lit === j, w = d * 30 + (d - 1) * 4;
    return <span key={j} style={{width:w,height:32,borderRadius:16,boxSizing:'border-box',display:'inline-flex',alignItems:'center',justifyContent:'center',fontSize:15,fontWeight:900,
      background:on ? BK.coral : v == null ? '#fff' : who === 'a' ? BK.ink : '#fbe3da',border:'2px ' + (v == null ? 'dashed' : 'solid') + ' ' + (on ? BK.coral : BK.ink),color:on || (who === 'a' && v != null) ? '#fff' : BK.ink}}>{v == null ? '' : QA_NM[v]}</span>; })}</div>;
}
function QaMakePad() {
  const T = useSpTimers();
  const [qi, setQi] = useState(0), [ans, setAns] = useState([]), [lit, setLit] = useState(null), [heard, setHeard] = useState(false);
  const q = QA_Q[qi], full = ans.length >= q.length, home = full && ans[ans.length - 1] === 0, spb = 60 / 92;
  const play = (both) => { T.clear(); const ev = both ? qaEv(q, null).concat(qaEv(q, ans, 8)) : qaEv(q, null); playEvents('piano', ev, 92); setHeard(true);
    let b = 0; q.forEach(([, d], j) => { T.at(100 + b * spb * 1000, () => setLit(['q', j])); if (both) T.at(100 + (b + 8) * spb * 1000, () => setLit(['a', j])); b += d; });
    T.at(100 + (both ? 16 : 8) * spb * 1000, () => setLit(null)); };
  const tap = (k) => { if (!QA_KEYS.includes(k)) return; playKey(k, 0.5); if (!heard || full) return; setAns(a => [...a, k]); };
  const fresh = () => { T.clear(); setLit(null); setAns([]); setHeard(false); setQi(i => (i + 1 + Math.floor(Math.random() * (QA_Q.length - 1))) % QA_Q.length); };
  const kl = {}; QA_KEYS.forEach(k => { kl[k] = 'pale'; }); if (full) kl[ans[ans.length - 1]] = home ? 'good' : 'cor';
  return (
    <div className="try-box" style={actBox} data-qa="pad">
      <div style={actTitle}>{t('Question and answer', '묻고 대답하기')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>피아노가 두 마디로 <b>물어요</b>. 같은 리듬으로 <b>대답</b>해요: C D E F G 중에서 아무 음이나, 칸마다 하나씩. 그다음 둘을 이어서 들어요. <b>C로 끝나면</b> 끝난 느낌이 나요.</> : <>The piano <b>asks</b> two bars. <b>Answer</b> in the same rhythm: any of C D E F G, one for each box. Then hear them together. <b>End on C</b> and it sounds finished.</>}</div>
      <div style={{fontSize:12.5,fontWeight:900,color:BK.muted,textAlign:'center'}}>{t('The question', '질문')}</div>
      <QaPills q={q} lit={lit && lit[0] === 'q' ? lit[1] : -1} who="q"/>
      <div style={{fontSize:12.5,fontWeight:900,color:BK.muted,textAlign:'center',marginTop:6}}>{t('Your answer', '내 대답')}</div>
      <QaPills q={q} ans={q.map((_, j) => (j < ans.length ? ans[j] : null))} lit={lit && lit[0] === 'a' ? lit[1] : -1} who="a"/>
      <div style={{margin:'8px 0 4px'}}><SpKb lo={0} hi={7} W={40} H={96} lit={kl} names={QA_NM} onTap={tap} label={t('C position: C D E F G', 'C 자리: C D E F G')}/></div>
      <div style={{textAlign:'center',fontSize:14.5,fontWeight:900,minHeight:22,color:full ? (home ? BK.green : BK.coral) : BK.muted}}>{!heard ? t('Tap ▶ The question first.', '먼저 ▶ 질문 듣기를 눌러요.') : !full ? t('Answer: ' + (q.length - ans.length) + ' more', '대답: ' + (q.length - ans.length) + '개 더') : home ? t('Home on C: it sounds finished!', 'C로 집에 왔어요: 끝난 느낌!') : t('It still sounds like a question. Try ending on C.', '아직 묻는 느낌이에요. C로 끝내 봐요.')}</div>
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={spBtn} onClick={() => play(false)}>{t('▶ The question', '▶ 질문 듣기')}</button>
        <button className="ghost-btn" style={spBtn} disabled={!full} onClick={() => play(true)}>{t('▶ Question and answer', '▶ 질문과 대답')}</button>
        <button className="ghost-btn" style={spBtn} disabled={!ans.length} onClick={() => { T.clear(); setLit(null); setAns([]); }}>{t('Clear', '지우기')}</button>
        <button className="ghost-btn" style={spBtn} onClick={fresh}>{t('▶ Another question', '▶ 다른 질문')}</button>
      </div>
    </div>
  );
}

// Four-chord loop: I, IV, V and vi in C, a little band (the bass on beats 1 and 3, the chord on every beat), the chord's notes lit
const CL_CH = { I: [0, 4, 7], IV: [5, 9, 0], V: [7, 11, 2], vi: [9, 0, 4] };   // the pitch classes of each chord
const CL_VOICE = { I: [60, 64, 67], IV: [60, 65, 69], V: [59, 62, 67], vi: [60, 64, 69] }, CL_BASS = { I: 48, IV: 41, V: 43, vi: 45 };
const CL_NAME = { I: 'C', IV: 'F', V: 'G', vi: 'Am' }, CL_SEQ = ['I', 'IV', 'V', 'vi'];
const CL_LOOPS = [['I', 'V', 'vi', 'IV'], ['I', 'IV', 'V', 'I'], ['vi', 'IV', 'I', 'V'], ['I', 'vi', 'IV', 'V']];
const clEv = (loop) => { const ev = []; loop.forEach((c, i) => { const b0 = i * 4; [0, 2].forEach(k => ev.push([b0 + k, CL_BASS[c], 1.8, 0.5])); [0, 1, 2, 3].forEach(k => CL_VOICE[c].forEach(m => ev.push([b0 + k, m, 0.85, k % 2 ? 0.22 : 0.32]))); }); return ev; };
function ChordLoop() {
  const tm = useRef([]), loopT = useRef(null), t0 = useRef(0), solo = useRef([]), cur = useRef(CL_LOOPS[0]), alive = useRef(true);
  const [loop, setLoop] = useState(CL_LOOPS[0]), [on, setOn] = useState(null), [bar, setBar] = useState(-1), [n, setN] = useState(0), [lit, setLit] = useState(null);
  cur.current = loop;
  const bpm = 92, barMs = 4 * 60 / bpm * 1000;
  const clear = () => { tm.current.forEach(clearTimeout); tm.current = []; clearTimeout(loopT.current); loopT.current = null; };
  const stop = () => { clear(); stopClicks(); if (alive.current) { setOn(null); setBar(-1); } };
  useEffect(() => () => { alive.current = false; clear(); stopClicks(); }, []);
  const flash = (k) => { setLit(k); tm.current.push(setTimeout(() => setLit(l => (l === k ? null : l)), 220)); };
  const round = (mode, L) => { const sec = playEvents('piano', clEv(L), bpm); if (!sec) { stop(); return; } t0.current = performance.now() + 100;
    for (let i = 0; i < 4; i++) tm.current.push(setTimeout(() => setBar(i), 100 + i * barMs));
    if (mode === 'solo') solo.current.forEach(({ k, at }) => tm.current.push(setTimeout(() => { playKey(k, 0.45); flash(k); }, 100 + at)));
    loopT.current = setTimeout(() => { if (mode === 'solo') { stop(); return; } round('band', cur.current); }, 100 + 4 * barMs); };
  const startBand = () => { clear(); solo.current = []; setN(0); setOn('band'); round('band', cur.current); };
  const hearSolo = () => { if (!solo.current.length) return; clear(); setOn('solo'); round('solo', loop); };
  const tap = (k) => { playKey(k, 0.45); flash(k); if (on === 'band') { const at = (performance.now() - t0.current) % (4 * barMs); if (solo.current.length < 200) { solo.current.push({ k, at }); setN(solo.current.length); } } };
  const slot = (i) => setLoop(L => L.map((c, j) => (j === i ? CL_SEQ[(CL_SEQ.indexOf(c) + 1) % 4] : c)));
  const now = bar >= 0 ? loop[bar] : loop[0], kl = {}; for (let k = 0; k <= 19; k++) if (CL_CH[now].includes(((k % 12) + 12) % 12)) kl[k] = 'pale'; if (lit != null) kl[lit] = 'cor';
  return (
    <div className="try-box" style={actBox} data-cl="loop">
      <div style={actTitle}>{t('Four-chord loop', '네 화음 고리')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>화음 네 개가 계속 돌아요. 칸을 누르면 <b>I, IV, V, vi</b>로 바뀌어요. 지금 화음의 음이 건반에 켜져요: 그 음들은 언제나 어울려요. 밴드를 켜고 위에서 가락을 지어 봐요.</> : <>Four chords go round and round. Tap a box to change it: <b>I, IV, V, vi</b>. The notes of the chord now playing light up on the keys: those always fit. Start the band and make up a tune on top.</>}</div>
      {spChips(CL_LOOPS.map((L, i) => [i, L.map(c => CL_NAME[c]).join(' ')]), CL_LOOPS.findIndex(L => L.join() === loop.join()), (i) => setLoop(CL_LOOPS[i]))}
      <div style={{display:'grid',gridTemplateColumns:'repeat(4,minmax(0,1fr))',gap:6,margin:'8px 0'}}>{loop.map((c, i) => <button key={i} type="button" onClick={() => slot(i)} style={{padding:'8px 2px',borderRadius:12,cursor:'pointer',background:bar === i ? BK.coral : '#fff',border:'2px solid ' + (bar === i ? BK.coral : BK.ink),color:bar === i ? '#fff' : BK.ink}}>
        <div style={{fontFamily:LB_SERIF,fontSize:22,fontWeight:900,lineHeight:1.1}}>{c}</div><div style={{fontSize:13,fontWeight:900,opacity:0.8}}>{CL_NAME[c]}</div></button>)}</div>
      <div style={{margin:'6px 0 4px'}}><SpKb lo={0} hi={19} W={24} H={88} lit={kl} onTap={tap} label={t('Make up a tune', '가락 지어 보기')}/></div>
      <div style={{textAlign:'center',fontSize:14,fontWeight:900,color:on ? BK.coral : BK.muted,minHeight:20}}>{on === 'band' ? t('Play on top! Notes kept: ' + n, '위에서 쳐요! 남은 음: ' + n) : on === 'solo' ? t('Your tune, with the band', '내 가락, 밴드와 함께') : n ? t(n + ' notes kept', n + '개 음이 남아 있어요') : t('Start the band, then play', '밴드를 켜고, 쳐요')}</div>
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        {on ? <button className="ghost-btn" style={spBtn} onClick={stop}>{t('■ Stop', '■ 멈추기')}</button> : <button className="ghost-btn" style={spBtn} onClick={startBand}>{t('▶ Start the band', '▶ 밴드 켜기')}</button>}
        <button className="ghost-btn" style={spBtn} disabled={!n || on === 'solo'} onClick={hearSolo}>{t('▶ Hear my tune', '▶ 내 가락 듣기')}</button>
      </div>
    </div>
  );
}
'''
rep("// ══ Build BH: Blues jam ══", CODE + "\n// ══ Build BH: Blues jam ══")

# registrations: the Toolbox, Korean names, where they sit, icons
rep("  { id: 'csx-jam', ch: 'styles', title: 'Blues jam',",
    "  { id: 'mk-band', ch: 'pulse', title: 'My beat band', blurb: 'Claps, stamps, pats and rests in two bars, looped: beat 1 is the strong one.', C: () => <BeatBand/> },   // Build BI\n"
    "  { id: 'mk-qa', ch: 'reading-steps', title: 'Question and answer', blurb: 'The piano asks two bars; you answer on C D E F G and end at home.', C: () => <QaMakePad/> },\n"
    "  { id: 'mk-loop', ch: 'chords', title: 'Four-chord loop', blurb: 'I, IV, V and vi go round; make up a tune on the chord’s notes.', C: () => <ChordLoop/> },\n"
    "  { id: 'csx-jam', ch: 'styles', title: 'Blues jam',")
rep("  'csx-jam': ['블루스 잼',", "  'mk-band': ['나의 박 밴드', '손뼉, 발, 무릎, 쉼으로 두 마디, 계속 돌아요: 1박이 센박.'],\n  'mk-qa': ['묻고 대답하기', '피아노가 두 마디로 묻고, C D E F G로 대답해서 집으로.'],\n  'mk-loop': ['네 화음 고리', 'I, IV, V, vi가 돌고, 화음의 음으로 가락을 지어요.'],\n  'csx-jam': ['블루스 잼',")
rep("'csx-jam': ['about', 0, 3, 'show ear game'],", "'csx-jam': ['about', 0, 3, 'show ear game'], 'mk-band': ['rpulse', 0, 1, 'game home'], 'mk-qa': ['steps', 0, 1, 'game ear'], 'mk-loop': ['harmony', 1, 3, 'game ear'],")
rep("'csx-jam': 'about'", "'csx-jam': 'about', 'mk-band': 'r-beat', 'mk-qa': 'c-reading', 'mk-loop': 'p-chords'")
rep("  'csx-jam': () => (\n",
    "  'mk-band': () => (\n    <svg width=\"34\" height=\"34\" viewBox=\"0 0 24 24\"><rect width=\"24\" height=\"24\" rx=\"6\" fill=\"#e4572e\"/>{[0, 1, 2, 3].map(i => <rect key={i} x={3 + i * 4.7} y=\"8\" width=\"4\" height=\"8\" rx=\"1\" fill={i === 0 ? '#e9a83a' : '#fefbf3'}/>)}</svg>\n  ),\n"
    "  'mk-qa': () => (\n    <svg width=\"34\" height=\"34\" viewBox=\"0 0 24 24\"><rect width=\"24\" height=\"24\" rx=\"6\" fill=\"#3b4fa8\"/><rect x=\"3\" y=\"6\" width=\"12\" height=\"5\" rx=\"2.5\" fill=\"#fefbf3\"/><rect x=\"9\" y=\"13\" width=\"12\" height=\"5\" rx=\"2.5\" fill=\"#e9a83a\"/></svg>\n  ),\n"
    "  'mk-loop': () => (\n    <svg width=\"34\" height=\"34\" viewBox=\"0 0 24 24\"><rect width=\"24\" height=\"24\" rx=\"6\" fill=\"#7a4f96\"/><circle cx=\"12\" cy=\"12\" r=\"7\" fill=\"none\" stroke=\"#fefbf3\" strokeWidth=\"1.8\"/>{[0, 1, 2, 3].map(i => <circle key={i} cx={12 + 7 * Math.cos(i * Math.PI / 2 - Math.PI / 2)} cy={12 + 7 * Math.sin(i * Math.PI / 2 - Math.PI / 2)} r=\"2.2\" fill={i === 0 ? '#e9a83a' : '#fefbf3'}/>)}</svg>\n  ),\n"
    "  'csx-jam': () => (\n")
rep("  'pulse': ['steady-beat', 'count-ring', 'silent-beats', 'beat-or-rhythm', 'finger-beat'],", "  'pulse': ['steady-beat', 'count-ring', 'silent-beats', 'beat-or-rhythm', 'finger-beat', 'mk-band'],")
rep("  'chords': ['chx-clock', 'chx-stack', 'chx-mm', 'chx-tonic', 'chx-145', ", "  'chords': ['chx-clock', 'chx-stack', 'chx-mm', 'chx-tonic', 'chx-145', 'mk-loop', ")
rep("'mini-tune', 'five-positions', 'complete-melody']", "'mini-tune', 'five-positions', 'complete-melody', 'mk-qa']")

# on the Home: each toy in its room
rep("lessons: ['rb-beat', 'rb-count', 'rb-silent', 'rb-words', 'rb-finger'], check: 'pulse' }", "lessons: ['rb-beat', 'rb-count', 'rb-silent', 'rb-words', 'rb-finger', 'mk-band'], check: 'pulse' }")
rep("lessons: ['ch-tonic', 'ch-145', 'ch-seven', 'ch-inv', 'ch-cad'], check: 'chords', level: 7 }", "lessons: ['ch-tonic', 'ch-145', 'mk-loop', 'ch-seven', 'ch-inv', 'ch-cad'], check: 'chords', level: 7 }")
rep("'c-reading': { lessons: ['ssk-step', 'ssk-shape', 'ssk-read', 'mini-tune', 'tune-anatomy', 'hear-find', 'echo', 'sight-reading', 'draw-tune'],", "'c-reading': { lessons: ['ssk-step', 'ssk-shape', 'ssk-read', 'mini-tune', 'tune-anatomy', 'hear-find', 'echo', 'sight-reading', 'draw-tune', 'mk-qa'],")
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
