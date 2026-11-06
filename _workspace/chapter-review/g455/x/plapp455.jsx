// ─── Phase 455: chapter 3 on screen: what moves on each page (B11), the book as the online lesson, the drill (B9) ───
// Every beat is booked on the audio clock (like SteadyBeat); a tap is compared with the time the beat reached the ear
// (scheduled time + the speaker's latency). 72 beats a minute, as the old lesson (A6). Counting is 1 2 3 4 only (B5).
const PL_BPM = 72;
const PL_TOL = 0.19;   // how far from the beat a tap may land and still count (s): kind to young hands
// n beats; o.gaps: the time to each next beat (s) instead of an even beat; o.silentFrom: no click from that beat on;
// o.vol: click loudness; o.extra(ctx, t, i): anything else to sound on beat i
function plRun(n, o = {}) {
  const ctx = getAudio(); if (!ctx) return null;
  stopClicks();
  const spb = 60 / (o.bpm || PL_BPM), t0 = ctx.currentTime + 0.18, lat = outLatency(ctx), at = [];
  let t = t0;
  for (let i = 0; i < n; i++) {
    at.push(t + lat);
    if (o.silentFrom == null || i < o.silentFrom) plTick(ctx, t, i, o.vol != null ? o.vol : 0.3, o.noVoice);
    if (o.extra) o.extra(ctx, t, i, spb);
    t += o.gaps ? o.gaps[i] || spb : spb;
  }
  return { ctx, spb, at, lat, t0, now: () => ctx.currentTime };
}
// one beat: the same click every time (strong and weak beats are room 8's, B4), or the spoken count when the sound
// settings ask for a voice (never while a child counts inside her head)
function plTick(ctx, t, i, vol, noVoice) {
  if (SOUND.count === 'voice' && !noVoice && sayCount(ctx, t, String(i % 4 + 1), 1)) return;
  metroClick(ctx, t, false, vol);
}
// each expected time takes the nearest free tap within the tolerance
function plMatch(expect, taps, tol = PL_TOL) {
  const used = new Set(), offs = [];
  let hits = 0;
  expect.forEach(e => {
    let best = -1, bd = 1e9;
    taps.forEach((tp, j) => { if (used.has(j)) return; const d = Math.abs(tp - e); if (d < bd) { bd = d; best = j; } });
    if (best >= 0 && bd <= tol) { used.add(best); hits++; offs.push(taps[best] - e); } else offs.push(null);
  });
  return { hits, total: expect.length, extra: taps.length - used.size, offs };
}
// are the gaps between taps the same? (the largest gap differs from the average by at most a fifth)
function plEven(taps) {
  if (taps.length < 3) return null;
  const g = taps.slice(1).map((x, i) => x - taps[i]), m = g.reduce((a, b) => a + b, 0) / g.length;
  return { gaps: g, mean: m, dev: Math.max(...g.map(x => Math.abs(x - m) / m)), steady: Math.max(...g.map(x => Math.abs(x - m) / m)) <= 0.2 };
}
// timers that fire when a beat reaches the ear; cleared together
function usePlTimers() {
  const ref = useRef([]);
  useEffect(() => () => { ref.current.forEach(clearTimeout); stopClicks(); }, []);
  return {
    at: (run, when, fn) => ref.current.push(setTimeout(fn, Math.max(0, (when - run.now()) * 1000))),
    clear: () => { ref.current.forEach(clearTimeout); ref.current = []; },
  };
}
// a big tap pad, and the space bar while it is live
function PlPad({ on, onTap, label, h = 74 }) {
  useEffect(() => {
    if (!on) return;
    const k = (e) => { if (e.code === 'Space' || e.key === ' ') { e.preventDefault(); onTap(); } };
    window.addEventListener('keydown', k); return () => window.removeEventListener('keydown', k);
  }, [on, onTap]);
  return <button data-pl-pad onPointerDown={(e) => { e.preventDefault(); if (on) onTap(); }} disabled={!on}
    style={{width:'100%',height:h,borderRadius:14,border:'2px solid ' + (on ? BK.coral : BK.line),background:on ? '#fbe3da' : '#fff',color:on ? BK.coral : BK.muted,fontSize:18,fontWeight:900,touchAction:'manipulation',cursor:on ? 'pointer' : 'default',userSelect:'none'}}>{label || t('TAP', '탭')}</button>;
}
const plHint = () => <div style={{fontSize:12,color:'var(--muted)',textAlign:'center',marginTop:6,lineHeight:1.4}}>{t('Tap the pad or press the space bar. The device speaker or wired headphones work best: Bluetooth adds a delay.', '패드를 누르거나 스페이스 바를 눌러요. 기기 스피커나 유선 이어폰이 가장 좋아요: 블루투스는 소리가 늦게 와요.')}</div>;
// a row of beat circles in plain SVG (the book's beat circles): kinds 'beat' | 'play' | 'silent'; lit = the one sounding now
// kinds: 'beat' (white), 'play' (navy), 'silent' (dashed), 'finger' (a finger number in a coral circle, B8);
// under(i): the count under each circle (lit in coral with its beat)
function PlCircles({ n, kind = () => 'beat', label = (i) => String(i % 4 + 1), lit = -1, mark = () => null, under = null, r = 17, gap = 46, group = 4 }) {
  const W = 24 + (n - 1) * gap + Math.floor((n - 1) / group) * 14 + 24;
  const X = (i) => 24 + i * gap + Math.floor(i / group) * 14;
  const uy = r * 2 + 24, my = under ? r * 2 + 46 : r * 2 + 24;
  return <svg viewBox={'0 0 ' + W + ' ' + (my + 6)} style={{width:'100%',maxWidth:W * 1.15,display:'block',margin:'0 auto'}}>
    {Array.from({ length: n }, (_, i) => { const k = kind(i), on = i === lit, play = k === 'play', fin = k === 'finger', m = mark(i);
      const fill = fin ? (on ? '#c0431f' : BK.coral) : on ? (play ? BK.coral : '#fbe3da') : play ? BK.ink : '#fff';
      return <g key={i}>
        <circle cx={X(i)} cy={r + 4} r={on && fin ? r + 2 : r} fill={fill} stroke={fin ? (on ? '#c0431f' : BK.coral) : on ? BK.coral : BK.ink} strokeWidth="2.2" strokeDasharray={k === 'silent' ? '4.2 3.4' : undefined} style={{transition:'fill 0.08s'}}/>
        <text x={X(i)} y={r + 4 + r * 0.38} textAnchor="middle" fontSize={r * 1.05} fontWeight="900" fill={play || fin ? '#fff' : on ? BK.coral : BK.ink}>{label(i)}</text>
        {under && <text x={X(i)} y={uy} textAnchor="middle" fontSize="15" fontWeight="900" fill={on ? BK.coral : BK.muted}>{under(i)}</text>}
        {m && <text x={X(i)} y={my} textAnchor="middle" fontSize="15" fontWeight="900" fill={m === '✓' ? BK.green : BK.coral}>{m}</text>}
      </g>; })}
  </svg>;
}

// ── page 2: a steady click, a tap pad, and your gaps drawn as footprints ──
function PlSteadyPad() {
  const T = usePlTimers();
  const [mode, setMode] = useState(null);   // null | 'click' | 'alone'
  const [taps, setTaps] = useState([]);
  const [lit, setLit] = useState(-1);
  const run = useRef(null), tapsRef = useRef([]);
  const N = 8;
  function start(m) {
    T.clear(); tapsRef.current = []; setTaps([]); setLit(-1);
    if (m === 'click') {
      const r = plRun(4 + N); if (!r) return; run.current = r;
      r.at.forEach((a, i) => T.at(r, a, () => setLit(i)));
      T.at(r, r.at[4 + N - 1] + r.spb * 0.9, () => { setLit(-1); setMode('done-click'); });
    } else { const ctx = getAudio(); run.current = { now: () => ctx ? ctx.currentTime : performance.now() / 1000 }; }
    setMode(m);
  }
  const tap = React.useCallback(() => {
    const r = run.current; if (!r || (mode !== 'click' && mode !== 'alone')) return;
    const tm = r.now(); tapsRef.current = [...tapsRef.current, tm].slice(0, N); setTaps(tapsRef.current);
    if (mode === 'alone' && tapsRef.current.length >= N) setMode('done-alone');
  }, [mode]);
  const ev = plEven(taps);
  const fromClick = mode === 'click' || mode === 'done-click';
  const W = 560, X0 = 24, span = run.current && run.current.spb ? run.current.spb * (N - 1) : (ev ? ev.mean * (N - 1) : 1);
  const x = (tm) => { const base = fromClick && run.current && run.current.at ? run.current.at[4] : taps[0]; return X0 + (tm - base) / span * (W - 2 * X0); };
  const done = mode === 'done-click' || mode === 'done-alone';
  return (
    <div className="try-box" style={actBox} data-pl="steady">
      <div style={actTitle}>{t('Tap a steady beat', '꾸준한 박 치기')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>클릭과 함께 8번 쳐 보고, 그다음 혼자 8번 쳐 봐요. 발자국이 내 간격을 보여 줘요: <b>매번 똑같은 간격</b>이면 꾸준해요.</> : <>Tap 8 times with the click, then 8 times on your own. The footprints show your gaps: <b>the same gap every time</b> is steady.</>}</div>
      <div style={{display:'flex',gap:6,justifyContent:'center',flexWrap:'wrap',marginBottom:8}}>
        <button className={'chip' + (fromClick ? ' active' : '')} onClick={() => start('click')}>{t('▶ With the click (4 to get ready)', '▶ 클릭과 함께 (4번 듣고 시작)')}</button>
        <button className={'chip' + (mode === 'alone' || mode === 'done-alone' ? ' active' : '')} onClick={() => start('alone')}>{t('On my own', '나 혼자')}</button>
      </div>
      {fromClick && <PlCircles n={4} lit={lit >= 0 ? lit % 4 : -1} r={13} gap={36}/>}
      <svg viewBox={'0 0 ' + W + ' 86'} style={{width:'100%',display:'block',margin:'4px 0'}}>
        <line x1={X0 - 10} x2={W - X0 + 10} y1="44" y2="44" stroke={BK.line} strokeWidth="1.4"/>
        {fromClick && run.current && run.current.at && Array.from({ length: N }, (_, i) => <line key={i} x1={X0 + i * (W - 2 * X0) / (N - 1)} x2={X0 + i * (W - 2 * X0) / (N - 1)} y1="36" y2="52" stroke={BK.muted} strokeWidth="1.4" strokeDasharray="2 2"/>)}
        {taps.map((tm, i) => { const cx = Math.max(10, Math.min(W - 10, x(tm))), cy = i % 2 ? 58 : 30, bad = ev && done && Math.abs((i ? tm - taps[i - 1] : ev.mean) - ev.mean) / ev.mean > 0.2;
          return <g key={i}><ellipse cx={cx + 2} cy={cy} rx="7" ry="5" fill={bad ? BK.coral : BK.ink}/><ellipse cx={cx - 7} cy={cy} rx="4" ry="3.6" fill={bad ? BK.coral : BK.ink}/></g>; })}
        {done && ev && ev.gaps.map((g, i) => { const a = x(taps[i]), b = x(taps[i + 1]), off = Math.abs(g - ev.mean) / ev.mean > 0.2;
          return <path key={i} d={`M${a} 76 L${a} 80 L${b} 80 L${b} 76`} fill="none" stroke={off ? BK.coral : BK.green} strokeWidth="1.8"/>; })}
      </svg>
      <PlPad on={mode === 'click' || mode === 'alone'} onTap={tap} label={mode === 'alone' ? t('TAP · ' + taps.length + ' of 8', '탭 · ' + taps.length + ' / 8') : t('TAP', '탭')}/>
      {done && ev && <div style={{textAlign:'center',fontSize:15,fontWeight:900,marginTop:8,color:ev.steady ? BK.green : BK.coral}}>{ev.steady ? t('Steady: the same gap every time ✓', '꾸준해요: 매번 똑같은 간격 ✓') : t('The gaps change (the coral ones). Try again, like a clock.', '간격이 바뀌었어요 (산호색). 시계처럼 다시 해 봐요.')}</div>}
      {done && !ev && <div style={{textAlign:'center',fontSize:14,fontWeight:800,marginTop:8,color:BK.muted}}>{t('Tap 8 times to see your gaps.', '8번 쳐야 간격이 보여요.')}</div>}
      {plHint()}
    </div>
  );
}

// ── page 3: the counting ring lights up with the click, four times round ──
function PlCountRing() {
  const T = usePlTimers();
  const [lit, setLit] = useState(-1);
  const [round, setRound] = useState(0);
  const [on, setOn] = useState(false);
  function start() {
    T.clear(); if (on) { stopClicks(); setOn(false); setLit(-1); setRound(0); return; }
    const r = plRun(16); if (!r) return;
    r.at.forEach((a, i) => T.at(r, a, () => { setLit(i % 4); setRound(Math.floor(i / 4) + 1); }));
    T.at(r, r.at[15] + r.spb * 0.9, () => { setLit(-1); setOn(false); });
    setOn(true);
  }
  const cx = 110, cy = 92, R = 58, at = (i) => { const a = -Math.PI / 2 + i * Math.PI / 2; return [cx + R * Math.cos(a), cy + R * Math.sin(a)]; };
  return (
    <div className="try-box" style={actBox} data-pl="ring">
      <div style={actTitle}>{t('Count with the ring', '동그라미와 함께 세기')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>시작을 누르고 무릎을 치면서 소리 내어 세요: <b>1 2 3 4</b>, 불이 켜지는 동그라미마다 숫자 하나. 네 번 돌아요.</> : <>Press start, pat your knees and count out loud: <b>1 2 3 4</b>, one number on each lit circle. Four times round.</>}</div>
      <svg viewBox="0 0 220 186" style={{width:'100%',maxWidth:260,display:'block',margin:'0 auto'}}>
        {[0, 1, 2, 3].map(i => { const a1 = -Math.PI / 2 + i * Math.PI / 2 + 0.46, a2 = -Math.PI / 2 + (i + 1) * Math.PI / 2 - 0.46, am = (a1 + a2) / 2, k2 = R / Math.cos((a2 - a1) / 2);
          const p1 = [cx + R * Math.cos(a1), cy + R * Math.sin(a1)], p2 = [cx + R * Math.cos(a2), cy + R * Math.sin(a2)], pm = [cx + k2 * Math.cos(am), cy + k2 * Math.sin(am)];
          const tg = [-Math.sin(a2), Math.cos(a2)], nm = [Math.cos(a2), Math.sin(a2)], col = i === 3 ? BK.coral : BK.ink;
          return <g key={'a' + i} fill="none" stroke={col} strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d={`M${p1[0]} ${p1[1]} Q${pm[0]} ${pm[1]} ${p2[0]} ${p2[1]}`}/>
            <path d={`M${p2[0] - tg[0] * 6 + nm[0] * 3.6} ${p2[1] - tg[1] * 6 + nm[1] * 3.6} L${p2[0]} ${p2[1]} L${p2[0] - tg[0] * 6 - nm[0] * 3.6} ${p2[1] - tg[1] * 6 - nm[1] * 3.6}`}/></g>; })}
        <text x={cx - R + 4} y={cy - R + 8} textAnchor="end" fontSize="12" fontWeight="900" fill={BK.coral}>{t('back to 1', '다시 1')}</text>
        {[0, 1, 2, 3].map(i => { const [x, y] = at(i), o = i === lit; return <g key={i}><circle cx={x} cy={y} r={o ? 25 : 21} fill={o ? BK.coral : '#fff'} stroke={o ? BK.coral : BK.ink} strokeWidth="2.4" style={{transition:'r 0.06s'}}/><text x={x} y={y + 8} textAnchor="middle" fontSize="22" fontWeight="900" fill={o ? '#fff' : BK.ink}>{i + 1}</text></g>; })}
        <text x={cx} y={cy + 6} textAnchor="middle" fontSize="13" fontWeight="900" fill={BK.muted}>{on && round ? t('round ' + round + ' of 4', round + ' / 4 바퀴') : ''}</text>
      </svg>
      <div style={{textAlign:'center'}}><button className="ghost-btn" onClick={start}>{on ? t('■ Stop', '■ 멈춤') : t('▶ Start: four times round', '▶ 시작: 네 바퀴')}</button></div>
    </div>
  );
}

// ── page 4: play on some beats, count the silent ones; tap only where you play ──
const PL_SILENT = [
  { id: '12', play: [1, 1, 0, 0], get name() { return t('Play on 1 and 2', '1과 2에서 치기'); } },
  { id: '1', play: [1, 0, 0, 0], get name() { return t('Play only on 1', '1에서만 치기'); } },
];
function PlSilentBeats() {
  const T = usePlTimers();
  const [pi, setPi] = useState(0);
  const [lit, setLit] = useState(-1);
  const [phase, setPhase] = useState('ready');   // ready | count | go | done
  const [res, setRes] = useState(null);
  const run = useRef(null), taps = useRef([]);
  const P = PL_SILENT[pi], N = 8, play = (i) => P.play[i % 4] === 1;
  function start() {
    T.clear(); setRes(null); taps.current = [];
    const r = plRun(4 + N, { vol: 0.22 }); if (!r) return; run.current = r;
    r.at.forEach((a, i) => T.at(r, a, () => { setLit(i - 4); setPhase(i < 4 ? 'count' : 'go'); }));
    T.at(r, r.at[4 + N - 1] + r.spb * 0.9, () => {
      setLit(-1); setPhase('done');
      const at = r.at.slice(4), playAt = at.filter((_, i) => play(i)), silentAt = at.filter((_, i) => !play(i));
      const m = plMatch(playAt, taps.current), onSilent = plMatch(silentAt, taps.current);
      const marks = at.map((a, i) => { const near = taps.current.some(tp => Math.abs(tp - a) <= PL_TOL); return play(i) ? (near ? '✓' : '?') : (near ? '✗' : null); });
      setRes({ m, silentHit: onSilent.hits, marks });
    });
    setPhase('count');
  }
  const tap = React.useCallback(() => { const r = run.current; if (r && (phase === 'count' || phase === 'go')) taps.current.push(r.now()); }, [phase]);
  const nPlay = Array.from({ length: N }, (_, i) => play(i)).filter(Boolean).length;
  return (
    <div className="try-box" style={actBox} data-pl="silent">
      <div style={actTitle}>{t('Silent beats still count', '조용한 박에서도 계속 세요')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>클릭 4번을 듣고, 꽉 찬 동그라미에서만 패드를 쳐요. 점선 동그라미에서는 손을 들고 계속 세요.</> : <>Listen to 4 clicks, then tap the pad only on the full circles. On the dashed circles, lift your hand and keep counting.</>}</div>
      <div style={{display:'flex',gap:6,justifyContent:'center',marginBottom:6}}>{PL_SILENT.map((x, i) => <button key={x.id} className={'chip' + (i === pi ? ' active' : '')} onClick={() => { T.clear(); stopClicks(); setPi(i); setRes(null); setPhase('ready'); setLit(-1); }}>{x.name}</button>)}</div>
      <PlCircles n={N} kind={(i) => play(i) ? 'play' : 'silent'} lit={lit} mark={(i) => res ? res.marks[i] : null}/>
      <div style={{textAlign:'center',fontSize:13,fontWeight:800,color:BK.muted,minHeight:18}}>{phase === 'count' ? t('Get ready…', '준비…') : phase === 'go' ? t('Count out loud: 1 2 3 4', '소리 내어 세요: 1 2 3 4') : ''}</div>
      <PlPad on={phase === 'count' || phase === 'go'} onTap={tap}/>
      <div style={{textAlign:'center',marginTop:8}}><button className="ghost-btn" onClick={start}>{phase === 'done' ? t('▶ Again', '▶ 다시') : t('▶ Start', '▶ 시작')}</button></div>
      {res && <div style={{textAlign:'center',fontSize:14.5,fontWeight:900,marginTop:6,color:res.m.hits === nPlay && res.silentHit === 0 ? BK.green : BK.coral}}>
        {t('Played on time: ' + res.m.hits + ' of ' + nPlay + ' · taps on a silent beat: ' + res.silentHit, '제때 친 박: ' + nPlay + '개 중 ' + res.m.hits + '개 · 조용한 박에 친 것: ' + res.silentHit + '개')}
        {res.m.hits === nPlay && res.silentHit === 0 ? t('  ✓', '  ✓') : ''}</div>}
      {plHint()}
    </div>
  );
}

// ── page 5: words over a beat (the cast's words, B7): tap the beat, then the words ──
const PL_WORDS = { bird: [t => t('bird', '새'), 1], turtle: [t => t('tur-tle', '거-북'), 2], lighthouse: [t => t('light-house', '등-대'), 2] };
const PL_WORD_SETS = [['bird', 'turtle', 'bird', 'turtle'], ['turtle', 'turtle', 'bird', 'bird'], ['lighthouse', 'bird', 'lighthouse', 'bird']];
const plWordName = (w) => PL_WORDS[w][0](t);
// a beat's heart: coral while its beat sounds, an outline otherwise
const plBeatHeart = (on, w = 20) => <svg viewBox="-8.5 -7.5 17 14" width={w} style={{display:'block',margin:'4px auto 0'}}><path d="M0 5 Q-7.5 -0.5 -5 -4.2 Q-2.4 -6.8 0 -3 Q2.4 -6.8 5 -4.2 Q7.5 -0.5 0 5 Z" fill={on ? BK.coral : '#fff'} stroke={BK.coral} strokeWidth="1.3" strokeLinejoin="round"/></svg>;
// the sounds of a row of words, in beats from its start (a two-sound word: on the beat and halfway to the next)
const plSyll = (row) => row.flatMap((w, i) => PL_WORDS[w][1] === 1 ? [i] : [i, i + 0.5]);
function plWordSounds(row, rounds) {
  return (ctx, t, i, spb) => { if (i < 4) return; const b = i - 4, w = row[b % 4];
    blip(ctx, t, 587.33, PL_WORDS[w][1] === 1 ? spb * 0.8 : spb * 0.42, 0.2, 'triangle');
    if (PL_WORDS[w][1] === 2) blip(ctx, t + spb / 2, 493.88, spb * 0.42, 0.2, 'triangle'); };
}
function PlWordsBeat() {
  const T = usePlTimers();
  const [si, setSi] = useState(0);
  const [mode, setMode] = useState('beat');   // beat | words
  const [phase, setPhase] = useState('ready');
  const [pos, setPos] = useState(-1);
  const [res, setRes] = useState(null);
  const run = useRef(null), taps = useRef([]);
  const row = PL_WORD_SETS[si], ROUNDS = 2, N = 4 * ROUNDS;
  function start(m) {
    T.clear(); setRes(null); taps.current = []; setMode(m);
    const r = plRun(4 + N, { vol: 0.25, extra: plWordSounds(row) }); if (!r) return; run.current = r;
    r.at.forEach((a, i) => T.at(r, a, () => { setPos(i - 4); setPhase(i < 4 ? 'count' : 'go'); }));
    T.at(r, r.at[4 + N - 1] + r.spb * 0.95, () => {
      setPos(-1); setPhase('done');
      const beats = r.at.slice(4), sounds = [];
      for (let k = 0; k < ROUNDS; k++) plSyll(row).forEach(o => sounds.push(r.at[4 + k * 4] + o * r.spb));
      const want = m === 'beat' ? beats : sounds;
      setRes({ m: plMatch(want, taps.current, Math.min(PL_TOL, r.spb * 0.22)), want: want.length });
    });
    setPhase('count');
  }
  const tap = React.useCallback(() => { const r = run.current; if (r && (phase === 'count' || phase === 'go')) taps.current.push(r.now()); }, [phase]);
  const b = pos >= 0 ? pos % 4 : -1;
  const ok = res && res.m.hits === res.want && res.m.extra === 0;
  return (
    <div className="try-box" style={actBox} data-pl="words">
      <div style={actTitle}>{t('Beat or rhythm?', '박일까, 리듬일까?')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>낱말이 박 위에서 소리를 내요. 먼저 <b>박</b>만 쳐요 (낱말 하나에 한 번). 그다음 <b>낱말 소리</b>마다 쳐요.</> : <>The words sound over the beat. First tap only the <b>beat</b>, once for each word. Then tap every <b>sound</b> of the words.</>}</div>
      <div style={{display:'flex',gap:5,justifyContent:'center',flexWrap:'wrap',marginBottom:8}}>{PL_WORD_SETS.map((s, i) => <button key={i} className={'chip' + (i === si ? ' active' : '')} onClick={() => { T.clear(); stopClicks(); setSi(i); setRes(null); setPhase('ready'); setPos(-1); }}>{s.map(plWordName).join(', ')}</button>)}</div>
      <div style={{display:'grid',gridTemplateColumns:'repeat(4,auto)',justifyContent:'space-around',gap:4,textAlign:'center',margin:'0 auto 6px',maxWidth:420}}>
        {row.map((w, i) => <div key={i} style={{padding:'6px 2px',borderRadius:10,background:i === b ? '#fbe3da' : 'transparent',transition:'background 0.08s'}}>
          <div style={{display:'flex',justifyContent:'center',gap:6,height:14}}>{Array.from({ length: PL_WORDS[w][1] }, (_, k) => <span key={k} style={{width:12,height:12,borderRadius:6,background:BK.coral}}/>)}</div>
          <div style={{fontSize:row.includes('lighthouse') ? 14 : 15.5,fontWeight:900,color:BK.ink,marginTop:3,whiteSpace:'nowrap'}}>{plWordName(w)}</div>
          {plBeatHeart(i === b, 22)}
        </div>)}
      </div>
      <PlPad on={phase === 'count' || phase === 'go'} onTap={tap} label={mode === 'beat' ? t('TAP THE BEAT', '박을 쳐요') : t('TAP THE WORDS', '낱말을 쳐요')}/>
      <div style={{display:'flex',gap:6,justifyContent:'center',marginTop:8}}>
        <button className="ghost-btn" onClick={() => start('beat')}>{t('▶ Tap the beat', '▶ 박 치기')}</button>
        <button className="ghost-btn" onClick={() => start('words')}>{t('▶ Tap the words', '▶ 낱말 치기')}</button>
      </div>
      {res && <div style={{textAlign:'center',fontSize:14.5,fontWeight:900,marginTop:6,color:ok ? BK.green : BK.coral}}>
        {mode === 'beat' ? t('Beats: ' + res.m.hits + ' of ' + res.want + (res.m.extra ? ' · extra taps: ' + res.m.extra + ' (the words?)' : ''), '박: ' + res.want + '개 중 ' + res.m.hits + '개' + (res.m.extra ? ' · 더 친 것: ' + res.m.extra + '개 (낱말 소리?)' : ''))
          : t('Sounds: ' + res.m.hits + ' of ' + res.want + (res.m.extra ? ' · extra taps: ' + res.m.extra : ''), '소리: ' + res.want + '개 중 ' + res.m.hits + '개' + (res.m.extra ? ' · 더 친 것: ' + res.m.extra + '개' : ''))}{ok ? '  ✓' : ''}</div>}
      {plHint()}
    </div>
  );
}

// ── page 6: the pulse in the fingers: tap the black keys on the beat, a new finger each time (the book's three rows) ──
const PL_FINGER_TUNES = [
  { id: 'small', get name() { return t('Small-house beat', '작은 집 박'); }, keys: [['2', 1], ['3', 3]], seq: ['2', '3', '2', '3'] },
  { id: 'big', get name() { return t('Big-house beat', '큰 집 박'); }, keys: [['2', 6], ['3', 8], ['4', 10]], seq: ['2', '3', '4', '3'] },
  { id: 'left', get name() { return t('Left-hand beat', '왼손 박'); }, keys: [['3', -11], ['2', -9]], seq: ['3', '2', '3', '2'] },
];
function PlFingerBeat() {
  const T = usePlTimers();
  const [ti, setTi] = useState(0);
  const [phase, setPhase] = useState('ready');
  const [pos, setPos] = useState(-1);
  const [res, setRes] = useState(null);
  const [down, setDown] = useState(null);
  const run = useRef(null), taps = useRef([]);
  const tune = PL_FINGER_TUNES[ti], N = 8, want = (i) => tune.seq[i % 4];
  function start() {
    T.clear(); setRes(null); taps.current = [];
    const r = plRun(4 + N, { vol: 0.22 }); if (!r) return; run.current = r;
    r.at.forEach((a, i) => T.at(r, a, () => { setPos(i - 4); setPhase(i < 4 ? 'count' : 'go'); }));
    T.at(r, r.at[4 + N - 1] + r.spb * 0.9, () => {
      setPos(-1); setPhase('done');
      let hits = 0; const marks = r.at.slice(4).map((a, i) => { const ok = taps.current.some(([tm, f]) => f === want(i) && Math.abs(tm - a) <= PL_TOL); if (ok) hits++; return ok ? '✓' : '?'; });
      setRes({ hits, marks, extra: Math.max(0, taps.current.length - hits) });
    });
    setPhase('count');
  }
  function press(f, k) {
    playKey(k, 0.4); setDown(f); setTimeout(() => setDown(d => d === f ? null : d), 160);
    const r = run.current; if (r && (phase === 'count' || phase === 'go')) taps.current.push([r.now(), f]);
  }
  return (
    <div className="try-box" style={actBox} data-pl="fingers">
      <div style={actTitle}>{t('A new finger on each beat', '박마다 다른 손가락')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>클릭 4번을 듣고, 박마다 산호색 번호의 손가락으로 검은건반을 쳐요. 소리 내어 세요: 1 2 3 4.</> : <>Listen to 4 clicks, then on every beat tap the black key for the finger in the coral circle. Count out loud: 1 2 3 4.</>}</div>
      <div style={{display:'flex',gap:5,justifyContent:'center',flexWrap:'wrap',marginBottom:8}}>{PL_FINGER_TUNES.map((x, i) => <button key={x.id} className={'chip' + (i === ti ? ' active' : '')} onClick={() => { T.clear(); stopClicks(); setTi(i); setRes(null); setPhase('ready'); setPos(-1); }}>{x.name}</button>)}</div>
      <PlCircles n={N} kind={() => 'finger'} label={(i) => want(i)} under={(i) => String(i % 4 + 1)} lit={pos} mark={(i) => res ? res.marks[i] : null} r={15} gap={40}/>
      <div style={{display:'flex',gap:10,justifyContent:'center'}}>{tune.keys.map(([f, k]) => <button key={f} onPointerDown={(e) => { e.preventDefault(); press(f, k); }}
        style={{width:64,height:120,borderRadius:'0 0 10px 10px',border:'none',background:down === f ? '#3b3f8f' : BK.ink,display:'flex',flexDirection:'column',justifyContent:'flex-end',alignItems:'center',paddingBottom:10,touchAction:'manipulation',cursor:'pointer'}}>
        <span style={{width:30,height:30,borderRadius:15,background:BK.coral,color:'#fff',fontWeight:900,fontSize:16,display:'flex',alignItems:'center',justifyContent:'center'}}>{f}</span></button>)}</div>
      <div style={{textAlign:'center',fontSize:12,color:BK.muted,marginTop:4}}>{ti === 2 ? t('left hand · the 3rd small house', '왼손 · 셋째 작은 집') : ti === 1 ? t('right hand · the big house next to the 4th small house', '오른손 · 넷째 작은 집 옆 큰 집') : t('right hand · the 4th small house', '오른손 · 넷째 작은 집')}</div>
      <div style={{textAlign:'center',marginTop:8}}><button className="ghost-btn" onClick={start}>{phase === 'done' ? t('▶ Again', '▶ 다시') : t('▶ Start', '▶ 시작')}</button></div>
      {res && <div style={{textAlign:'center',fontSize:14.5,fontWeight:900,marginTop:6,color:res.hits === N ? BK.green : BK.coral}}>{t('On the beat with the right finger: ' + res.hits + ' of 8', '제 박에 맞는 손가락: 8개 중 ' + res.hits + '개')}{res.hits === N ? '  ✓' : ''}</div>}
    </div>
  );
}

// ── the book on screen: the opener is the lesson's head, every other page a step. Old ticks kept where the idea is the
// same: 'Feel the pulse' (0) is now 'A steady beat', 'Beat or rhythm?' (1) stays, 'Count out loud' (4) stays. ──
const PL_STORE = [0, 4, 6, 1, 7, 8];
function PlLearn({ onStart }) {
  const pages = plLbPages(true);
  const opener = pages[0];
  return (
    <Lesson id="pulse" title={t('Pulse & Counting', '박과 세기')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="pulse"><div className="lb-screen lb-open" style={{display:'flex',flexDirection:'column',gap:12,margin:'0 0 8px'}}>{lbWordsFirst(opener.props.children)}</div></BkChapterCtx.Provider></LbScreenCtx.Provider>}>
      {pages.slice(1).map((pg, i) => (
        <Step key={i} storeAs={PL_STORE[i]} title={pg.props.title}>
          <LbScreenPage page={pg}/>
        </Step>
      ))}
    </Lesson>
  );
}

// ── the drill (B9): five levels, one idea a level. 1 listens; 2 to 5 are tapped. ──
const PL_LEVELS = [
  { n: 1, label: 'Steady or not?', kind: 'steady', time: 16 },
  { n: 2, label: 'Tap along with the click', kind: 'along', time: 24 },
  { n: 3, label: 'Keep it going on your own', kind: 'keep', time: 20 },
  { n: 4, label: 'Count inside, tap one beat', kind: 'inside', time: 24 },
  { n: 5, label: 'Tap the beat, not the words', kind: 'words', time: 24 },
];
Object.assign(LEVEL_KO, {
  'Steady or not?': '꾸준할까, 아닐까?', 'Tap along with the click': '클릭에 맞춰 치기', 'Keep it going on your own': '혼자 계속 이어 가기',
  'Count inside, tap one beat': '속으로 세고 한 박만 치기', 'Tap the beat, not the words': '낱말 말고 박을 쳐요',
});
function genPlQuestion(lv, prev) {
  const uid = Math.random(), spb = 60 / PL_BPM;
  if (lv.kind === 'steady') {
    const steady = Math.random() < 0.5;
    let gaps = Array(7).fill(spb);
    if (!steady) { const at = shuffle([1, 2, 3, 4, 5]).slice(0, 2 + Math.floor(Math.random() * 2)); at.forEach((i, k) => { gaps[i] = spb * (k % 2 ? 0.62 : 1.42); }); }
    return { kind: 'steady', gaps, answer: steady ? 'steady' : 'not', key: 'st' + gaps.map(g => Math.round(g * 100)).join('.'), uid };
  }
  if (lv.kind === 'inside') { let b = 1 + Math.floor(Math.random() * 4), g = 0; while (prev && prev.key === 'in' + b && g++ < 6) b = 1 + Math.floor(Math.random() * 4); return { kind: 'inside', beat: b, key: 'in' + b, uid }; }
  if (lv.kind === 'words') {
    let row, g = 0;
    do { row = Array.from({ length: 4 }, () => pick(['bird', 'turtle', 'lighthouse'])); } while ((row.every(w => w === 'bird') || row.filter(w => w === 'lighthouse').length > 1 || (prev && prev.key === row.join())) && g++ < 20);
    return { kind: 'words', row, key: row.join(), uid };
  }
  return { kind: lv.kind, key: lv.kind, uid };
}
// what each tapped level asks for, from the run's beat times (4 count-in clicks first)
function plWant(q, r) {
  const b = r.at.slice(4);
  if (q.kind === 'along') return b;
  if (q.kind === 'keep') return b.slice(0, 8);   // 4 with the clicks, then 4 alone
  if (q.kind === 'inside') return b.filter((_, i) => i % 4 === q.beat - 1);
  return b.slice(0, 4);   // words: the beat
}
function PlQuestion({ q, given, locked, onAnswer, pixel }) {
  const T = usePlTimers();
  const [phase, setPhase] = useState('ready');
  const [pos, setPos] = useState(-1);
  const run = useRef(null), taps = useRef([]);
  const done = !!given;
  const btnCls = pixel ? 'pixel-choice' : 'choice-btn';
  const prompt = (txt) => <p style={{fontSize:15,fontWeight:700,textAlign:'center',margin:'0 0 10px',color:'var(--muted)'}}>{txt}</p>;
  function listen() {
    T.clear();
    const r = plRun(8, { gaps: q.gaps }); if (!r) return;
    r.at.forEach((a, i) => T.at(r, a, () => setPos(i)));
    T.at(r, r.at[7] + 0.5, () => setPos(-1));
  }
  useEffect(() => { T.clear(); stopClicks(); setPhase('ready'); setPos(-1); taps.current = []; if (q.kind === 'steady') { const id = setTimeout(listen, 300); return () => clearTimeout(id); } }, [q.uid]);
  function start() {
    if (done || phase !== 'ready') return;
    T.clear(); taps.current = [];
    const n = q.kind === 'along' || q.kind === 'inside' ? 4 + 8 : 4 + 4 + (q.kind === 'keep' ? 4 : 0);
    const r = plRun(n, { silentFrom: q.kind === 'keep' ? 8 : undefined, vol: q.kind === 'inside' ? 0.18 : 0.3, noVoice: q.kind === 'inside', extra: q.kind === 'words' ? plWordSounds(q.row) : undefined }); if (!r) return;
    run.current = r;
    r.at.forEach((a, i) => T.at(r, a, () => { setPos(i); setPhase(i < 4 ? 'count' : 'go'); }));
    T.at(r, r.at[n - 1] + r.spb * 0.95, () => {
      setPhase('scoring'); setPos(-1);
      const want = plWant(q, r), m = plMatch(want, taps.current, q.kind === 'keep' ? 0.24 : PL_TOL);
      const early = taps.current.filter(tp => tp < r.at[4] - PL_TOL).length;   // taps during the count-in don't count against you
      const extra = Math.max(0, m.extra - early), alone = m.offs.slice(4).filter(x => x !== null).length;
      const ok = q.kind === 'along' ? m.hits >= 7 && extra <= 1 : q.kind === 'keep' ? m.hits >= 6 && alone >= 3 && extra <= 1 : m.hits === m.total && extra === 0;
      onAnswer({ ok, hits: m.hits, total: m.total, extra });
    });
    setPhase('count');
  }
  const tap = React.useCallback(() => { const r = run.current; if (r && (phase === 'count' || phase === 'go')) taps.current.push(r.now()); }, [phase]);
  if (q.kind === 'steady') {
    const cls = (c) => btnCls + (!done ? '' : c === q.answer ? ' good' : given.ans === c ? ' bad' : '');
    return (<div>
      {prompt(t('Listen to 8 clicks. Is the beat steady, the same gap every time?', '클릭 8번을 들어요. 박이 꾸준한가요, 매번 똑같은 간격인가요?'))}
      <PlCircles n={8} lit={pos} label={() => ''} r={13} gap={34}/>
      <div style={{textAlign:'center',margin:'6px 0 10px'}}><button className={pixel ? 'pixel-btn' : 'ghost-btn'} onClick={listen}>{t('♪ Listen again', '♪ 다시 듣기')}</button></div>
      <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:8}}>
        <button disabled={locked} className={cls('steady')} style={{padding:'14px 0',fontSize:pixel ? 10 : 17}} onClick={() => { T.clear(); stopClicks(); onAnswer('steady'); }}>{t('Steady', '꾸준해요')}</button>
        <button disabled={locked} className={cls('not')} style={{padding:'14px 0',fontSize:pixel ? 10 : 17}} onClick={() => { T.clear(); stopClicks(); onAnswer('not'); }}>{t('Not steady', '들쭉날쭉해요')}</button>
      </div>
    </div>);
  }
  const res = done && given.ans && typeof given.ans === 'object' ? given.ans : null;
  const say = q.kind === 'along' ? t('4 clicks to get ready, then tap with every click: 8 taps.', '클릭 4번을 듣고, 클릭마다 같이 쳐요: 8번.')
    : q.kind === 'keep' ? t('4 clicks to get ready, 4 clicks to tap with, then the click stops: tap 4 more on your own, the same gap.', '클릭 4번을 듣고, 클릭 4번에 맞춰 치고, 클릭이 멈추면 혼자 4번 더 쳐요, 같은 간격으로.')
    : q.kind === 'inside' ? t('Count 1 2 3 4 inside your head and tap only on ' + q.beat + '. Two rounds.', '속으로 1 2 3 4를 세고 ' + q.beat + '에서만 쳐요. 두 바퀴.')
    : t('Words over a beat: tap the beat, once for each word, not every sound.', '박 위의 낱말: 낱말 하나에 한 번, 박을 쳐요. 소리마다 치지 않아요.');
  const N = q.kind === 'keep' ? 8 : q.kind === 'words' ? 4 : 8, show = (i) => q.kind === 'keep' ? i < 4 || phase === 'scoring' || done : q.kind === 'inside' ? false : true;
  const ring = pos >= 4 ? pos - 4 : -1;
  return (<div>
    {prompt(say)}
    {q.kind === 'words' && <div style={{display:'grid',gridTemplateColumns:'repeat(4,1fr)',gap:6,textAlign:'center',maxWidth:380,margin:'0 auto 8px'}}>{q.row.map((w, i) => <div key={i} style={{borderRadius:10,padding:'4px 0',background:i === ring ? '#fbe3da' : 'transparent'}}>
      <div style={{display:'flex',justifyContent:'center',gap:5,height:12}}>{Array.from({ length: PL_WORDS[w][1] }, (_, k) => <span key={k} style={{width:10,height:10,borderRadius:5,background:BK.coral}}/>)}</div>
      <div style={{fontSize:15,fontWeight:900,color:BK.ink,whiteSpace:'nowrap'}}>{plWordName(w)}</div>{plBeatHeart(i === ring)}</div>)}</div>}
    {q.kind !== 'words' && <PlCircles n={N} lit={q.kind === 'inside' ? -1 : ring} kind={(i) => q.kind === 'inside' ? (i % 4 === q.beat - 1 ? 'play' : 'silent') : 'beat'}
      label={(i) => String(i % 4 + 1)} r={14} gap={36}/>}
    {q.kind === 'keep' && <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',maxWidth:330,margin:'-18px auto 6px',textAlign:'center',fontSize:12.5,fontWeight:800,color:BK.muted}}><span>{t('with the click', '클릭과 함께')}</span><span style={{color:BK.ink}}>{t('on your own', '혼자서')}</span></div>}
    <div style={{textAlign:'center',fontSize:13,fontWeight:800,color:BK.muted,minHeight:18,margin:'2px 0 4px'}}>{phase === 'count' ? t('Get ready: ', '준비: ') + (pos + 1) : phase === 'go' ? (q.kind === 'keep' && pos >= 8 ? t('On your own now!', '이제 혼자!') : t('Go!', '시작!')) : ''}</div>
    {!done && phase === 'ready' && <div style={{textAlign:'center',marginBottom:8}}><button className={pixel ? 'pixel-btn' : 'ghost-btn'} onClick={start} style={{fontSize:15,padding:'10px 18px'}}>{t('▶ Start', '▶ 시작')}</button></div>}
    {!done && <PlPad on={phase === 'count' || phase === 'go'} onTap={tap} h={64}/>}
    {res && <div style={{textAlign:'center',fontSize:15,fontWeight:900,marginTop:8,color:res.ok ? BK.green : BK.coral}}>{t('On the beat: ' + res.hits + ' of ' + res.total + (res.extra ? ' · extra taps: ' + res.extra : ''), '박에 맞게: ' + res.total + '개 중 ' + res.hits + '개' + (res.extra ? ' · 더 친 것: ' + res.extra + '개' : ''))}</div>}
  </div>);
}
Object.assign(PULSE_DRILL, {
  levels: PL_LEVELS, generate: genPlQuestion, noPrint: true,   // tapped by ear: no printed worksheet (the Workbook is the paper)
  check: (q, ans) => { if (ans === null || ans === undefined) return false; if (q.kind === 'steady') return ans === q.answer; return !!(ans && ans.ok); },
  answerLabel: (q) => q.kind === 'steady' ? (q.answer === 'steady' ? t('steady: the same gap every time', '꾸준해요: 매번 똑같은 간격') : t('not steady: the gaps change', '들쭉날쭉해요: 간격이 바뀌어요'))
    : q.kind === 'along' ? t('a tap with every click: 8 taps', '클릭마다 한 번: 8번')
    : q.kind === 'keep' ? t('4 taps with the clicks, then 4 on your own, the same gap', '클릭에 맞춰 4번, 그다음 혼자 4번, 같은 간격으로')
    : q.kind === 'inside' ? t('a tap on ' + q.beat + ' only: twice', q.beat + '에서만: 두 번')
    : t('the beat: 4 taps (the words have ' + plSyll(q.row).length + ' sounds)', '박: 4번 (낱말 소리는 ' + plSyll(q.row).length + '개)'),
  Question: PlQuestion, Learn: PlLearn,
});
