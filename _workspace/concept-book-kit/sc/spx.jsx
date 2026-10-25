
// ─── Chapter: Playing Scales (Build AB, 2026-10-26; the technique room after Scales, Prelim – Grade 1) ───
// The Scales room says which fingers (thumb under, 3 over); this room plays them: a turn without a bump, one note a beat at a
// steady speed, A and E minor (natural, then harmonic), contrary motion as mirror twins (both hands from one note, the same
// finger numbers), then two octaves, hands together, two notes a beat. Fingerings and speeds checked against the technical
// work book (Preliminary P.1 to P.8; Grade 1 1.1 to 1.10, rendered 26 Oct): C and G major and the A, E and D minors share one
// fingering (rhPattern / lhPattern); F major's right hand is its own (SCALES.F). One note a beat at 76; contrary motion at 66;
// Grade 1 two notes a beat at 76. The notes start where the book prints them (semitones from middle C).
const SP_MAJ = [0, 2, 4, 5, 7, 9, 11], SP_NAT = [0, 2, 3, 5, 7, 8, 10], SP_HAR = [0, 2, 3, 5, 7, 8, 11];
const SP_SC = {
  C: { steps: SP_MAJ, rh1: 0, lh1: -12, nm: ['C', 'D', 'E', 'F', 'G', 'A', 'B'], en: 'C major', ko: 'C장조' },
  G: { steps: SP_MAJ, rh1: 7, lh1: -17, rh2: -5, lh2: -17, nm: ['G', 'A', 'B', 'C', 'D', 'E', 'F♯'], en: 'G major', ko: 'G장조' },
  F: { steps: SP_MAJ, rh2: -7, lh2: -19, nm: ['F', 'G', 'A', 'B♭', 'C', 'D', 'E'], en: 'F major', ko: 'F장조' },
  Am: { steps: SP_NAT, rh1: -3, lh1: -15, nm: ['A', 'B', 'C', 'D', 'E', 'F', 'G'], en: 'A natural minor', ko: 'A 자연 단음계' },
  Amh: { steps: SP_HAR, rh1: -3, lh1: -15, nm: ['A', 'B', 'C', 'D', 'E', 'F', 'G♯'], en: 'A harmonic minor', ko: 'A 화성 단음계' },
  Em: { steps: SP_NAT, rh1: 4, lh1: -8, rh2: 4, lh2: -8, nm: ['E', 'F♯', 'G', 'A', 'B', 'C', 'D'], en: 'E natural minor', ko: 'E 자연 단음계' },
  Emh: { steps: SP_HAR, rh1: 4, lh1: -8, rh2: 4, lh2: -8, nm: ['E', 'F♯', 'G', 'A', 'B', 'C', 'D♯'], en: 'E harmonic minor', ko: 'E 화성 단음계' },
  Dm: { steps: SP_NAT, rh2: 2, lh2: -10, nm: ['D', 'E', 'F', 'G', 'A', 'B♭', 'C'], en: 'D natural minor', ko: 'D 자연 단음계' },
  Dmh: { steps: SP_HAR, rh2: 2, lh2: -10, nm: ['D', 'E', 'F', 'G', 'A', 'B♭', 'C♯'], en: 'D harmonic minor', ko: 'D 화성 단음계' },
};
const spName = (k) => t(SP_SC[k].en, SP_SC[k].ko);
const spKeys = (k, hand, n) => { const s = SP_SC[k], r = s[(hand === 'R' ? 'rh' : 'lh') + n], out = []; for (let o = 0; o < n; o++) s.steps.forEach(x => out.push(r + 12 * o + x)); out.push(r + 12 * n); return out; };
const spNames = (k, n) => { const s = SP_SC[k], out = []; for (let o = 0; o < n; o++) out.push(...s.nm); out.push(s.nm[0]); return out; };
const spFing = (k, hand, n) => (k === 'F' ? SCALES.F.octaves[n][hand === 'R' ? 'RH' : 'LH'] : hand === 'R' ? rhPattern(n) : lhPattern(n));
const spUpDown = (n) => { const up = Array.from({ length: n }, (_, j) => j); return up.concat(up.slice(0, -1).reverse()); };
// a metronome mark's crotchet, drawn (the font's ♩ leaves a wide gap after it); spTx: every ♩ in a sentence drawn this way
const spCrot = <svg viewBox="0 0 10 22" style={{width:'0.5em',height:'1.05em',verticalAlign:'-0.12em',display:'inline-block',overflow:'visible'}} aria-label="♩" role="img"><ellipse cx="4.4" cy="18.2" rx="4.2" ry="3.1" transform="rotate(-22 4.4 18.2)" fill="currentColor"/><line x1="8.1" x2="8.1" y1="17.4" y2="1.5" stroke="currentColor" strokeWidth="1.5"/></svg>;
const spTx = (str) => { const parts = String(str).split('♩'); return parts.length < 2 ? str : parts.map((x, i) => <React.Fragment key={i}>{i ? spCrot : null}{x}</React.Fragment>); };
const spMM = (n) => <span style={{whiteSpace:'nowrap'}}>{spCrot} = {n}</span>;
const spHz = (i) => 440 * Math.pow(2, (60 + i - 69) / 12);
const spHand = (h) => (h === 'R' ? t('Right hand', '오른손') : t('Left hand', '왼손'));
const spBtn = { padding:'10px 14px', fontSize:14, minHeight:44 };
const spMsg = (txt, col) => <div style={{textAlign:'center',fontSize:15,fontWeight:900,color:col || 'var(--navy)',minHeight:22,lineHeight:1.35,textWrap:'balance'}}>{txt}</div>;
const spChips = (opts, val, set) => <div style={{display:'flex',gap:6,justifyContent:'center',flexWrap:'wrap',marginBottom:8}}>{opts.map(([id, lab]) => <button key={id} className={'chip' + (id === val ? ' active' : '')} aria-pressed={id === val} style={{minHeight:40,padding:'6px 12px'}} onClick={() => set(id)}>{lab}</button>)}</div>;
// sound a list of notes on the audio clock: events [{ at (beats), keys, len (beats), vol }]; clicks: that many beats clicked first
function spPlay(events, bpm, clicks = 0) {
  const ctx = getAudio(); if (!ctx) return null;
  stopClicks();
  const spb = 60 / bpm, t0 = ctx.currentTime + 0.15;
  for (let b = 0; b < clicks; b++) metroClick(ctx, t0 + b * spb, false, 0.25);
  events.forEach(e => e.keys.forEach(i => blip(ctx, t0 + (clicks + e.at) * spb, spHz(i), Math.max(0.25, (e.len || 1) * spb * 0.92), e.vol || 0.16, 'triangle')));
  return { ctx, t0, spb, ms: (beat) => (0.15 + (clicks + beat) * spb) * 1000 };
}
function useSpTimers() {
  const ts = useRef([]), clear = () => { ts.current.forEach(clearTimeout); ts.current = []; stopClicks(); };
  useEffect(() => () => clear(), []);
  return { clear, at: (ms, fn) => ts.current.push(setTimeout(fn, ms)) };
}

// ── the keyboard in pen, by semitones from middle C ──
// lit {i: 'cor' | 'pale' | 'good' | 'bad'}; up / dn: finger numbers above (right hand) and below (left hand), a black key's one row
// further out; act {i: true}: that number filled (the finger playing now); names {i: letter}; hand: the five fingers of one hand
// as circles over their keys ([key of finger 1 … finger 5], hf: the finger playing), gliding when the hand moves on; arc: the
// finger that passes ({ from, to, over }): under for the thumb, over for 3 or 4
const SP_W = [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1], SP_X = [0, 0, 1, 1, 2, 3, 3, 4, 4, 5, 5, 6];
const spPc = (i) => ((i % 12) + 12) % 12;
const spIsW = (i) => SP_W[spPc(i)] === 1;
const spWIdx = (i) => Math.floor(i / 12) * 7 + SP_X[spPc(i)];
function SpKb({ lo, hi, W = 26, H = 76, lit = {}, up = {}, dn = {}, act = {}, names = null, hand = null, hf = null, arc = null, onTap, label, k = 1.3, maxW }) {
  const a = spIsW(lo) ? lo : lo - 1, b = spIsW(hi) ? hi : hi + 1, w0 = spWIdx(a), nw = spWIdx(b) - w0 + 1;
  const r = Math.min(10, W * 0.4), row = 2 * r + 3, BW = W * 0.6, BH = H * 0.6;
  const anyUp = !!hand || Object.keys(up).length > 0, anyDn = Object.keys(dn).length > 0;
  const top = (anyUp ? 2 * row + 6 : 6) + (arc && arc.over ? 16 : 0), height = top + H + (anyDn ? 2 * row + 6 : 6), width = 8 + nw * W;
  const kx = (i) => 4 + (spWIdx(i) - w0 + (spIsW(i) ? 0.5 : 1)) * W;
  const yUp = (i) => top - 4 - r - (spIsW(i) ? 0 : row), yDn = (i) => top + H + 4 + r + (spIsW(i) ? 0 : row);
  const keys = []; for (let i = a; i <= b; i++) keys.push(i);
  const wFill = (m) => (m === 'cor' ? PEN_C : m === 'pale' ? '#fbe3da' : m === 'good' ? PEN_G : m === 'bad' ? '#c8361b' : '#fff');
  const bFill = (m) => (m === 'cor' ? PEN_C : m === 'good' ? PEN_G : m === 'bad' ? '#c8361b' : PEN_N);
  const strong = (m) => m === 'cor' || m === 'good' || m === 'bad';
  const circ = (x, y, f, on, key) => <g key={key}><circle cx={x} cy={y} r={r} fill={on ? PEN_C : '#fff'} stroke={PEN_C} strokeWidth="1.5"/><text x={x} y={y + r * 0.45} textAnchor="middle" fontSize={r * 1.3} fontWeight="900" fill={on ? '#fff' : PEN_C} style={{fontFamily:'Inter, sans-serif'}}>{f}</text></g>;
  let arcEl = null;
  if (arc) { const x1 = kx(arc.from), x2 = kx(arc.to), dir = x2 > x1 ? 1 : -1;
    const y = arc.over ? top - 2 * row - 4 : top + 4, cy = arc.over ? y - 22 : y + H * 0.42;
    const ex = x2 - dir * 3, hd = 7, ang = arc.over ? 0.9 : -0.9;
    arcEl = <g style={{pointerEvents:'none',animation:'fadeUp 0.25s both'}} fill="none" stroke={PEN_C} strokeWidth="2.6" strokeLinecap="round" strokeLinejoin="round">
      <path d={'M' + x1 + ',' + y + ' Q' + ((x1 + x2) / 2) + ',' + cy + ' ' + ex + ',' + y} stroke="#fff" strokeWidth="5.5"/>
      <path d={'M' + x1 + ',' + y + ' Q' + ((x1 + x2) / 2) + ',' + cy + ' ' + ex + ',' + y}/>
      <path d={'M' + (ex - dir * hd) + ',' + (y + (arc.over ? -hd * 0.2 : hd * 0.2) + ang * 4) + ' L' + ex + ',' + y + ' L' + (ex - dir * hd * 0.35) + ',' + (y + (arc.over ? -hd : hd))}/>
    </g>; }
  return <svg viewBox={'0 0 ' + width + ' ' + height} style={{width:'100%',maxWidth:maxW || width * k,display:'block',margin:'0 auto',touchAction:'manipulation',userSelect:'none'}} role={onTap ? 'group' : 'img'} aria-label={label || t('Piano keys', '피아노 건반')}>
    {keys.filter(spIsW).map(i => <rect key={'w' + i} x={4 + (spWIdx(i) - w0) * W} y={top} width={W} height={H} fill={wFill(lit[i])} stroke={PEN_N} strokeWidth="1.3" style={{transition:'fill .12s'}}/>)}
    {keys.filter(i => !spIsW(i)).map(i => <g key={'b' + i}><rect x={kx(i) - BW / 2} y={top} width={BW} height={BH} rx="1.5" fill={bFill(lit[i])} style={{transition:'fill .12s'}}/>
      {lit[i] === 'pale' && <circle cx={kx(i)} cy={top + BH - 9} r="3.2" fill={PEN_C}/>}</g>)}
    {names && keys.map(i => names[i] == null ? null : spIsW(i)
      ? <text key={'n' + i} x={kx(i)} y={top + H - 7} textAnchor="middle" fontSize={Math.min(12.5, W * 0.48)} fontWeight="900" fill={strong(lit[i]) ? '#fff' : PEN_N} style={{fontFamily:'Inter, sans-serif'}}>{names[i]}</text>
      : <text key={'n' + i} x={kx(i)} y={top + BH - (lit[i] === 'pale' ? 16 : 6)} textAnchor="middle" fontSize={Math.min(9, W * 0.34)} fontWeight="900" fill="#fff" style={{fontFamily:'Inter, sans-serif'}}>{names[i]}</text>)}
    {Object.entries(up).map(([i, f]) => circ(kx(+i), yUp(+i), f, !!act[i], 'u' + i))}
    {Object.entries(dn).map(([i, f]) => circ(kx(+i), yDn(+i), f, !!act['d' + i], 'd' + i))}
    {hand && hand.map((i, j) => <g key={'h' + j} style={{transform:'translate(' + kx(i) + 'px,' + yUp(i) + 'px)',transition:'transform .38s ease'}}>{circ(0, 0, j + 1, hf === j + 1, 'c')}</g>)}
    {arcEl}
    {onTap && keys.filter(spIsW).map(i => <rect key={'tw' + i} data-key={i} x={4 + (spWIdx(i) - w0) * W} y={top} width={W} height={H} fill="transparent" style={{cursor:'pointer'}} role="button" aria-label={names && names[i] ? names[i] : String(i)} onClick={() => onTap(i)}/>)}
    {onTap && keys.filter(i => !spIsW(i)).map(i => <rect key={'tb' + i} data-key={i} x={kx(i) - BW / 2} y={top} width={BW} height={BH} fill="transparent" style={{cursor:'pointer'}} role="button" aria-label={names && names[i] ? names[i] : String(i)} onClick={() => onTap(i)}/>)}
  </svg>;
}
const spNameMap = (K, N) => Object.fromEntries(K.map((x, j) => [x, N[j]]));
const spFingMap = (K, F) => Object.fromEntries(K.map((x, j) => [x, F[j]]));

// ── step 1: smooth turns. The hand as five circles: three notes in one place, the thumb slides under, the hand moves on ──
// the up-and-back walk of one octave: each note's key, finger, and where the five fingers are (the hand's place)
const spTurnSeq = (k, hand) => { const K = spKeys(k, hand, 1), F = spFing(k, hand, 1);
  return spUpDown(8).map((j, s) => { const f = F[j]; return { j, key: K[j], f, s, up: s < 8, win: [1, 2, 3, 4, 5].map(x => (hand === 'R' ? K[j - f + x] : K[j + f - x])) }; }); };
const spTurns = (S) => S.map((x, s) => s > 0 && x.win[0] !== S[s - 1].win[0]);
// smooth: one note a beat; bumpy: the note after each turn comes late and loud (a thumb not ready)
const spTurnEvents = (k, hand, bumpy) => { const S = spTurnSeq(k, hand), tn = spTurns(S);
  return S.map((x, s) => ({ at: s + (bumpy && tn[s] ? 0.45 : 0), keys: [x.key], len: s === S.length - 1 ? 2 : 1, vol: bumpy && tn[s] ? 0.32 : 0.16 })); };
function spTurnRun(k, hand, bumpy, setAt, T, bpm = 72) {
  const S = spTurnSeq(k, hand), ev = spTurnEvents(k, hand, bumpy);
  const run = spPlay(ev, bpm); if (!run) return;
  ev.forEach((e, s) => T.at(run.ms(e.at), () => setAt(s)));
  T.at(run.ms(S.length + 1.2), () => setAt(-1));
}
const spTurnWord = (x) => (x.f === 1 ? t('Thumb under', '엄지 밑으로 넣기') : t(x.f + ' over', x.f + '번 넘기기'));
function SpTurnPad({ onResult, fixed }) {
  const T = useSpTimers();
  const [k, setK] = useState(fixed ? fixed.k : 'C'), [hand, setHand] = useState(fixed ? fixed.hand : 'R');
  const [at, setAt] = useState(-1), [mode, setMode] = useState(null), [ans, setAns] = useState(null);
  const S = spTurnSeq(k, hand), tn = spTurns(S), K = spKeys(k, hand, 1), cur = at >= 0 ? S[at] : null, prev = at > 0 ? S[at - 1] : null;
  const go = (m) => { T.clear(); setAns(null); const b = m === 'mys' ? Math.random() < 0.5 : m === 'bumpy'; setMode({ m, b }); spTurnRun(k, hand, b, setAt, T); };
  const reset = (fn) => { T.clear(); setAt(-1); setMode(null); setAns(null); fn(); };
  const lit = Object.fromEntries(K.map(x => [x, 'pale'])); if (cur) lit[cur.key] = 'cor';
  const arc = cur && tn[at] ? { from: prev.win[cur.f - 1], to: cur.key, over: cur.f !== 1 } : null;
  const say = (c) => { if (!mode || mode.m !== 'mys' || ans) return; setAns(c); if (onResult) onResult({ ok: (c === 'bumpy') === mode.b }); };
  const known = mode && mode.m !== 'mys';
  const line = cur && tn[at] ? (known && mode.b ? t('Bump! The thumb was not ready.', '덜컹! 엄지가 준비되지 않았어요.') : spTurnWord(cur) + (known ? t(': the hand moves on.', ': 손이 자리를 옮겨요.') : ''))
    : cur ? t('finger ' + cur.f + ' · ' + SP_SC[k].nm[cur.j % 7], cur.f + '번 · ' + SP_SC[k].nm[cur.j % 7]) : mode && mode.m === 'mys' && !ans ? t('Smooth, or bumpy?', '매끄럽게? 덜컹?') : '';
  return (
    <div className="try-box" style={actBox} data-sp="turn">
      <div style={actTitle}>{t('Smooth turns', '매끄럽게 넘기기')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>동그라미 다섯 개가 손가락이에요. 세 음을 치는 동안 엄지가 손 밑으로 들어가 준비하고, <b>팔이 손을 데려가요</b>. 매끄러운 음계와 덜컹하는 음계를 들어 보고, 맞혀 봐요.</> : <>The five circles are your fingers. While three notes play, the thumb slides under and gets ready; then <b>the arm carries the hand</b> on. Hear a smooth scale and a bumpy one, then spot which is which.</>}</div>
      {!fixed && spChips([['C', t('C major', 'C장조')], ['G', t('G major', 'G장조')]], k, (x) => reset(() => setK(x)))}
      {!fixed && spChips([['R', t('Right hand', '오른손')], ['L', t('Left hand', '왼손')]], hand, (x) => reset(() => setHand(x)))}
      <SpKb lo={K[0]} hi={K[7]} W={30} lit={lit} names={spNameMap(K, spNames(k, 1))} hand={(cur || S[0]).win} hf={cur ? cur.f : null} arc={arc} label={spName(k) + ' · ' + spHand(hand)}/>
      {spMsg(line, cur && tn[at] ? BK.coral : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={spBtn} onClick={() => go('smooth')}>{t('▶ Smooth', '▶ 매끄럽게')}</button>
        <button className="ghost-btn" style={spBtn} onClick={() => go('bumpy')}>{t('▶ Bumpy', '▶ 덜컹')}</button>
        <button className="ghost-btn" style={spBtn} onClick={() => go('mys')}>{t('▶ Which one?', '▶ 어느 쪽?')}</button>
      </div>
      {mode && mode.m === 'mys' && <div style={{display:'grid',gridTemplateColumns:'repeat(2,1fr)',gap:8,marginTop:10}}>{['smooth', 'bumpy'].map(c => <button key={c} className={'choice-btn' + (!ans ? '' : (c === 'bumpy') === mode.b ? ' good' : c === ans ? ' bad' : '')} onClick={() => say(c)} style={{padding:'12px 4px',fontSize:15,fontWeight:900}}>{c === 'smooth' ? t('Smooth', '매끄럽게') : t('Bumpy', '덜컹')}</button>)}</div>}
      {ans && spMsg((ans === 'bumpy') === mode.b ? t('Yes: it was ' + (mode.b ? 'bumpy. Listen how the note after the turn came late and loud.' : 'smooth: every note even.'), '맞아요: ' + (mode.b ? '덜컹했어요. 넘긴 다음 음이 늦고 크게 났어요.' : '매끄러웠어요: 모든 음이 고르게.')) : t('Listen again: it was ' + (mode.b ? 'bumpy, the note after the turn late and loud.' : 'smooth, every note even.'), '다시 들어 봐요: ' + (mode.b ? '덜컹했어요. 넘긴 다음 음이 늦고 컸어요.' : '매끄러웠어요. 모든 음이 고르게.')), (ans === 'bumpy') === mode.b ? BK.green : BK.coral)}
    </div>
  );
}

// ── step 2: on the beat. Four clicks, then one note on every click, up and back; the last note holds for two ──
const SP_CI = 4;
function SpBeatPad({ onResult, fixed }) {
  const T = usePlTimers();
  const [k, setK] = useState(fixed ? fixed.k : 'C'), [hand, setHand] = useState(fixed ? fixed.hand : 'R'), [bpm, setBpm] = useState(fixed ? fixed.bpm : 60);
  const [phase, setPhase] = useState('ready'), [at, setAt] = useState(-1), [res, setRes] = useState(null), [wrong, setWrong] = useState(null);
  const run = useRef(null), taps = useRef([]), mode = useRef('play');
  const K = spKeys(k, hand, 1), F = spFing(k, hand, 1), ix = spUpDown(8), N = ix.length;
  const reset = (fn) => { T.clear(); stopClicks(); setRes(null); setPhase('ready'); setAt(-1); setWrong(null); if (fn) fn(); };
  function start(m) {
    reset(); mode.current = m; taps.current = [];
    const r = plRun(SP_CI + N + 1, { bpm, noVoice: true, extra: m === 'listen' ? (ctx, tm, i, spb) => { const s = i - SP_CI; if (s >= 0 && s < N) blip(ctx, tm, spHz(K[ix[s]]), spb * (s === N - 1 ? 1.8 : 0.92), 0.17, 'triangle'); } : null });
    if (!r) return; run.current = r;
    for (let s = 0; s < N; s++) T.at(r, r.at[SP_CI + s] - r.spb * 0.45, () => setAt(s));
    T.at(r, r.at[0], () => setPhase('count')); T.at(r, r.at[SP_CI] - r.spb * 0.45, () => setPhase('go'));
    T.at(r, r.at[SP_CI + N - 1] + r.spb * 1.6, () => {
      setAt(-1); setPhase('done'); if (m !== 'play') return;
      const used = new Set(); let hits = 0;
      const marks = ix.map((j, s) => { const e = r.at[SP_CI + s]; let best = -1, bd = 1e9;
        taps.current.forEach((tp, q) => { if (used.has(q) || tp.i !== K[j]) return; const d = Math.abs(tp.t - e); if (d < bd) { bd = d; best = q; } });
        if (best >= 0 && bd <= PL_TOL) { used.add(best); hits++; return '✓'; } return '?'; });
      const out = { hits, total: N, marks, ok: hits >= N - 2 }; setRes(out); if (onResult) onResult(out);
    });
  }
  const tap = (i) => { playKey(i, 0.5); const r = run.current; if (r && mode.current === 'play' && (phase === 'go' || phase === 'count')) { taps.current.push({ t: r.now(), i }); const s = at; if (s >= 0 && i !== K[ix[s]]) setWrong(i); else setWrong(null); } };
  const lit = Object.fromEntries(K.map(x => [x, 'pale'])); if (at >= 0) lit[K[ix[at]]] = 'cor'; if (wrong != null && phase === 'go') lit[wrong] = 'bad';
  const act = at >= 0 ? { [K[ix[at]]]: true } : {};
  return (
    <div className="try-box" style={actBox} data-sp="beat">
      <div style={actTitle}>{t('On the beat', '박에 맞춰')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>클릭 네 번을 듣고, <b>클릭마다 한 음</b>씩 올라갔다 내려와요. 마지막 음은 두 박. 산호색 건반이 다음 음이에요. 먼저 {spCrot} = 60으로, 그다음 목표 빠르기 {spCrot} = 76으로.</> : <>Hear four clicks, then play <b>one note on every click</b>, up and back. The last note holds for two. The coral key is the next note. Start at {spCrot} = 60, then the target speed: {spCrot} = 76.</>}</div>
      {fixed ? <div style={{textAlign:'center',fontSize:14,fontWeight:900,color:'var(--navy)',marginBottom:6}}>{spName(k)} · {spHand(hand)} · {spMM(bpm)}</div> : <>
        {spChips([['C', t('C major', 'C장조')], ['G', t('G major', 'G장조')]], k, (x) => reset(() => setK(x)))}
        {spChips([['R', t('Right hand', '오른손')], ['L', t('Left hand', '왼손')]], hand, (x) => reset(() => setHand(x)))}
        {spChips([[60, spMM(60)], [76, spMM(76)]], bpm, (x) => reset(() => setBpm(x)))}
      </>}
      <SpKb lo={K[0]} hi={K[7]} W={32} H={84} lit={lit} names={spNameMap(K, spNames(k, 1))} up={spFingMap(K, F)} act={act} onTap={tap} label={spName(k) + ' · ' + spHand(hand)}/>
      <div style={{margin:'8px 0 2px'}}><PlCircles n={N} r={10} gap={23} group={8} kind={() => 'finger'} label={(s) => String(F[ix[s]])} lit={at} mark={(s) => (res ? res.marks[s] : null)}/></div>
      {spMsg(phase === 'count' ? t('Get ready… 1 2 3 4', '준비… 1 2 3 4') : phase === 'go' ? (mode.current === 'listen' ? t('Listen: one note on every click', '들어 봐요: 클릭마다 한 음') : wrong != null ? t('Not that key: the coral one', '그 건반이 아니에요: 산호색 건반') : t('Play the coral key on the click', '클릭에 맞춰 산호색 건반')) : '', wrong != null && phase === 'go' ? BK.coral : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={spBtn} onClick={() => start('listen')}>{t('▶ Listen', '▶ 듣기')}</button>
        <button className="ghost-btn" style={spBtn} onClick={() => start('play')}>{phase === 'done' && res ? t('▶ Again', '▶ 다시') : t('▶ Play along', '▶ 같이 치기')}</button>
      </div>
      {res && spMsg(t('On the beat: ' + res.hits + ' of ' + res.total, '박에 맞게: ' + res.total + '개 중 ' + res.hits + '개') + (res.ok ? ' ✓' : ''), res.ok ? BK.green : BK.coral)}
      <div style={{fontSize:12,color:'var(--muted)',textAlign:'center',marginTop:6,lineHeight:1.4}}>{t('Tap the keys here, or play along on your piano. The device speaker or wired headphones work best: Bluetooth adds a delay.', '여기 건반을 누르거나, 피아노로 같이 쳐요. 기기 스피커나 유선 이어폰이 가장 좋아요: 블루투스는 소리가 늦게 와요.')}</div>
    </div>
  );
}

// ── step 3: A and E minor, natural, then harmonic (the 7th up a half step); the fingers are C major's ──
function spMinorRun(k, hand, setAt, T, bpm = 80) {
  const K = spKeys(k, hand, 1), ix = spUpDown(8);
  const run = spPlay(ix.map((j, s) => ({ at: s, keys: [K[j]], len: s === ix.length - 1 ? 2 : 1 })), bpm); if (!run) return;
  ix.forEach((j, s) => T.at(run.ms(s), () => setAt(s)));
  T.at(run.ms(ix.length + 1.2), () => setAt(-1));
}
function SpMinorPad({ onResult }) {
  const T = useSpTimers();
  const [root, setRoot] = useState('A'), [form, setForm] = useState('nat'), [hand, setHand] = useState('R'), [at, setAt] = useState(-1), [mys, setMys] = useState(null), [ans, setAns] = useState(null);
  const k = root + 'm' + (form === 'har' ? 'h' : ''), K = spKeys(k, hand, 1), F = spFing(k, hand, 1), ix = spUpDown(8);
  const seventh = K[6];
  const reset = (fn) => { T.clear(); setAt(-1); setMys(null); setAns(null); fn(); };
  const play = () => { T.clear(); setMys(null); setAns(null); spMinorRun(k, hand, setAt, T); };
  const mystery = () => { T.clear(); setAns(null); const r = Math.random() < 0.5 ? 'A' : 'E', f = Math.random() < 0.5 ? 'nat' : 'har'; setMys({ r, f }); setRoot(r); setForm(f); setHand('R'); spMinorRun(r + 'm' + (f === 'har' ? 'h' : ''), 'R', setAt, T); };
  const say = (c) => { if (!mys || ans) return; setAns(c); if (onResult) onResult({ ok: c === mys.f }); };
  const hide = mys && !ans;
  const lit = Object.fromEntries(K.map(x => [x, 'pale'])); if (form === 'har' && at < 0 && !hide) lit[seventh] = 'cor'; if (at >= 0) lit[K[ix[at]]] = 'cor';
  const nm = spNameMap(K, spNames(k, 1)), L7 = SP_SC[root + 'm'].nm[6], H7 = SP_SC[root + 'mh'].nm[6];
  return (
    <div className="try-box" style={actBox} data-sp="minor">
      <div style={actTitle}>{t('A and E minor', 'A단조와 E단조')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>자연 단음계, 그다음 화성 단음계: <b>7번째 음이 반음 올라가요</b>. 손가락은 C장조와 똑같아요. 소리로도 구별해 봐요.</> : <>The natural minor, then the harmonic minor: <b>the 7th note goes up a half step</b>. The fingers are C major's. Then tell them apart by ear.</>}</div>
      {spChips([['A', t('A minor', 'A단조')], ['E', t('E minor', 'E단조')]], root, (x) => reset(() => setRoot(x)))}
      {spChips([['nat', t('Natural', '자연')], ['har', t('Harmonic', '화성')]], form, (x) => reset(() => setForm(x)))}
      {spChips([['R', t('Right hand', '오른손')], ['L', t('Left hand', '왼손')]], hand, (x) => reset(() => setHand(x)))}
      <SpKb lo={K[0]} hi={K[7]} W={32} H={84} lit={hide ? {} : lit} names={hide ? null : nm} up={hide ? {} : spFingMap(K, F)} act={at >= 0 && !hide ? { [K[ix[at]]]: true } : {}} label={spName(k)}/>
      {spMsg(hide ? t('Natural or harmonic?', '자연일까요, 화성일까요?') : form === 'har' ? t('The 7th goes up a half step: ' + L7 + ' → ' + H7 + '.', '7번째 음이 반음 올라가요: ' + L7 + ' → ' + H7 + '.') : t(root === 'A' ? 'A natural minor: the white keys from A to A.' : 'E natural minor: one black key, F♯.', root === 'A' ? 'A 자연 단음계: A부터 A까지 흰건반.' : 'E 자연 단음계: 검은건반 하나, F♯.'), form === 'har' && !hide ? BK.coral : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={spBtn} onClick={play}>{t('▶ Play it', '▶ 들어 보기')}</button>
        <button className="ghost-btn" style={spBtn} onClick={mystery}>{t('▶ Natural or harmonic?', '▶ 자연? 화성?')}</button>
      </div>
      {mys && <div style={{display:'grid',gridTemplateColumns:'repeat(2,1fr)',gap:8,marginTop:10}}>{['nat', 'har'].map(c => <button key={c} className={'choice-btn' + (!ans ? '' : c === mys.f ? ' good' : c === ans ? ' bad' : '')} onClick={() => say(c)} style={{padding:'12px 4px',fontSize:15,fontWeight:900}}>{c === 'nat' ? t('Natural', '자연') : t('Harmonic', '화성')}</button>)}</div>}
      {ans && spMsg(ans === mys.f ? t('Yes: ' + (mys.f === 'har' ? 'harmonic. Hear the raised 7th, just under the top?' : 'natural, no raised 7th.'), '맞아요: ' + (mys.f === 'har' ? '화성. 꼭대기 바로 밑에서 올라간 7번째 음이 들렸나요?' : '자연, 7번째 음이 올라가지 않았어요.')) : t('It was ' + (mys.f === 'har' ? 'harmonic: listen for the raised 7th, just under the top.' : 'natural: the 7th stays down.'), (mys.f === 'har' ? '화성이었어요: 꼭대기 바로 밑, 올라간 7번째 음을 들어 봐요.' : '자연이었어요: 7번째 음이 그대로예요.')), ans === mys.f ? BK.green : BK.coral)}
    </div>
  );
}

// ── step 4: mirror twins. Contrary motion: both hands on one note, the right hand up, the left hand down, the same finger numbers ──
const SP_CM = { C: { s: 0, steps: SP_MAJ, nm: SP_SC.C.nm, en: 'C major, from middle C', ko: '가운데 도에서 C장조' }, Amh: { s: -3, steps: SP_HAR, nm: SP_SC.Amh.nm, en: 'A harmonic minor, from the A below middle C', ko: '가운데 도 아래 A에서 A 화성 단음계' } };
const SP_CM_F = [1, 2, 3, 1, 2, 3, 4, 5];
const spCm = (k) => { const c = SP_CM[k], R = c.steps.map(x => c.s + x).concat([c.s + 12]), L = c.steps.map(x => c.s - 12 + x).concat([c.s]).reverse();
  const nmR = c.nm.concat([c.nm[0]]), nmL = c.nm.concat([c.nm[0]]).reverse(); return { R, L, nmR, nmL }; };
const spCmLet = (c, side, j) => { const nm = side === 'R' ? c.nmR : c.nmL; return nm[j]; };
function SpMirrorPad({ onResult }) {
  const T = useSpTimers();
  const [k, setK] = useState('C'), [at, setAt] = useState(-1), [q, setQ] = useState(null), [tapd, setTapd] = useState(null);
  const c = spCm(k), ix = spUpDown(8), j = at >= 0 ? ix[at] : q ? q.j : null;
  const reset = (fn) => { T.clear(); setAt(-1); setQ(null); setTapd(null); if (fn) fn(); };
  const play = () => { reset(); const run = spPlay(ix.map((jj, s) => ({ at: s, keys: [c.R[jj], c.L[jj]], len: s === ix.length - 1 ? 2 : 1, vol: 0.13 })), 66); if (!run) return;
    ix.forEach((jj, s) => T.at(run.ms(s), () => setAt(s))); T.at(run.ms(ix.length + 1.2), () => setAt(-1)); };
  const ask = () => { reset(); let x, g = 0; do { x = 1 + Math.floor(Math.random() * 7); } while (q && q.j === x && g++ < 10); setQ({ j: x }); playKey(c.R[x], 0.6); };
  const tap = (i) => { playKey(i, 0.5); if (!q || tapd != null) return; setTapd(i); if (onResult) onResult({ ok: i === c.L[q.j] }); };
  const ok = q && tapd === c.L[q.j];
  const up = spFingMap(c.R, SP_CM_F), dn = spFingMap(c.L, SP_CM_F);
  const lit = {}; c.R.concat(c.L).forEach(x => { lit[x] = 'pale'; });
  const act = {};
  if (j != null) { lit[c.R[j]] = 'cor'; act[c.R[j]] = true; if (!q || tapd != null) { lit[c.L[j]] = q ? 'good' : 'cor'; act['d' + c.L[j]] = true; } if (q && tapd != null && !ok) lit[tapd] = 'bad'; }
  const nm = {}; c.R.forEach((x, jj) => { nm[x] = c.nmR[jj]; }); c.L.forEach((x, jj) => { nm[x] = c.nmL[jj]; });
  const f = j != null ? SP_CM_F[j] : null;
  return (
    <div className="try-box" style={actBox} data-sp="mirror">
      <div style={actTitle}>{t('Mirror twins', '거울 쌍둥이')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>두 손이 한 음에서 시작해서 서로 멀어졌다가 돌아와요. 오른손은 위로, 왼손은 아래로, <b>언제나 같은 번호</b>: 1과 1, 3과 3. 엄지는 둘이 함께 넘어가요.</> : <>Both hands start on one note, move apart, and come back. The right hand goes up, the left hand down, <b>always the same number</b>: 1 with 1, 3 with 3. The thumbs turn together.</>}</div>
      {spChips([['C', t('C major', 'C장조')], ['Amh', t('A harmonic minor', 'A 화성 단음계')]], k, (x) => reset(() => setK(x)))}
      <SpKb lo={c.L[7]} hi={c.R[7]} W={22} H={70} lit={lit} names={nm} up={up} dn={dn} act={act} onTap={tap} label={t(SP_CM[k].en, SP_CM[k].ko)} k={1.5}/>
      <div style={{display:'flex',justifyContent:'space-between',fontSize:12,fontWeight:800,color:BK.muted,margin:'2px 4px 0'}}><span>{t('← left hand: down', '← 왼손: 아래로')}</span><span>{t('right hand: up →', '오른손: 위로 →')}</span></div>
      {spMsg(q ? (tapd == null ? t('The right hand plays ' + spCmLet(c, 'R', q.j) + ' with finger ' + f + '. Tap the key for the left hand’s finger ' + f + '.', '오른손 ' + f + '번: ' + spCmLet(c, 'R', q.j) + '. 왼손 ' + f + '번의 건반을 눌러요.')
        : ok ? t('Yes: ' + spCmLet(c, 'L', q.j) + ', finger ' + f + ' too. Mirror twins!', '맞아요: ' + spCmLet(c, 'L', q.j) + ', 왼손도 ' + f + '번. 거울 쌍둥이!') : t('Count out from the middle: the same number of steps each way. It is ' + spCmLet(c, 'L', q.j) + '.', '가운데에서부터 세어 봐요: 양쪽으로 같은 걸음 수. 답은 ' + spCmLet(c, 'L', q.j) + '.'))
        : f ? t('Right ' + f + ' · left ' + f, '오른손 ' + f + ' · 왼손 ' + f) : k === 'C' ? t('Both thumbs on middle C (Clara).', '두 엄지 모두 가운데 도(클라라)에.') : t('Both thumbs on the A below middle C.', '두 엄지 모두 가운데 도 아래 A에.'), q && tapd != null ? (ok ? BK.green : BK.coral) : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={spBtn} onClick={play}>{t('▶ Play', '▶ 들어 보기')} ({spMM(66)})</button>
        <button className="ghost-btn" style={spBtn} onClick={ask}>{q && tapd != null ? t('▶ Another', '▶ 다른 것') : t('▶ Your turn', '▶ 내가 해보기')}</button>
      </div>
    </div>
  );
}

// ── step 5: two octaves, hands together (Grade 1): the notes in a strip, the right hand's fingers above, the left hand's below;
// two notes on every beat (run-ning); the thumbs play together only in some places ──
const spStripCols = (k) => ({ N: spNames(k, 2), R: spFing(k, 'R', 2), L: spFing(k, 'L', 2) });
const spThumbs = (k) => { const s = spStripCols(k); return s.R.map((f, j) => (f === 1 && s.L[j] === 1 ? j : -1)).filter(j => j >= 0); };
function SpStrip({ k, cur = -1, ask = null, found = [], bad = null, onTap, hideR = null, hideL = null, mw = 440 }) {
  const s = spStripCols(k), n = s.N.length;
  const cell = (j, txt, row, col) => <div key={row + j} style={{gridRow:row,gridColumn:j + 2,textAlign:'center',fontWeight:900,fontSize:13,lineHeight:'26px',height:26,color:col,borderRadius:13,
    background:found.includes(j) ? '#d9efe7' : j === cur ? '#fbe3da' : 'transparent',border:'1.5px solid ' + (found.includes(j) ? PEN_G : j === bad ? '#c8361b' : j === cur ? PEN_C : 'transparent')}}>{txt}</div>;
  const nameSt = (j, x) => ({gridRow:2,gridColumn:j + 2,height:30,padding:0,minWidth:0,boxSizing:'border-box',display:'flex',alignItems:'center',justifyContent:'center',border:'1.5px solid ' + (j === ask ? PEN_C : PEN_N),borderRadius:6,background:found.includes(j) ? PEN_G : j === ask ? '#fbe3da' : '#fff',color:found.includes(j) ? '#fff' : PEN_N,fontWeight:900,fontSize:x.length > 1 ? 10 : 12.5,cursor:onTap ? 'pointer' : 'default',fontFamily:'Inter, sans-serif'});
  return <div style={{maxWidth:mw,margin:'0 auto'}}><div style={{display:'grid',gridTemplateColumns:'30px repeat(' + n + ',minmax(0,1fr))',gap:1,rowGap:4,alignItems:'center'}}>
    {Array.from({ length: Math.ceil(n / 2) }, (_, b) => <div key={'bg' + b} style={{gridRow:'1 / 4',gridColumn:(2 * b + 2) + ' / span ' + Math.min(2, n - 2 * b),background:b % 2 ? 'transparent' : 'rgba(38,41,107,0.06)',borderRadius:8,alignSelf:'stretch'}}/>)}
    <div style={{gridRow:1,gridColumn:1,fontSize:10.5,fontWeight:800,color:BK.muted}}>{t('right', '오른손')}</div>
    {s.R.map((f, j) => cell(j, hideR && hideR[j] ? '?' : f, 1, PEN_C))}
    <div style={{gridRow:2,gridColumn:1}}/>
    {s.N.map((x, j) => onTap ? <button key={'n' + j} onClick={() => onTap(j)} aria-label={x} style={nameSt(j, x)}>{x}</button> : <div key={'n' + j} style={nameSt(j, x)}>{x}</div>)}
    <div style={{gridRow:3,gridColumn:1,fontSize:10.5,fontWeight:800,color:BK.muted}}>{t('left', '왼손')}</div>
    {s.L.map((f, j) => cell(j, hideL && hideL[j] ? '?' : f, 3, PEN_N))}
  </div>
  <div style={{display:'flex',justifyContent:'center',gap:8,marginTop:6,fontSize:12,fontWeight:800,color:BK.muted}}><span style={{display:'inline-block',width:22,height:12,borderRadius:4,background:'rgba(38,41,107,0.10)',verticalAlign:'middle'}}/>{t('one beat: run-ning, two notes', '한 박: 티-티, 두 음')}</div></div>;
}
function SpTwoPad({ onResult }) {
  const T = useSpTimers();
  const [key, setKey] = useState('G'), [form, setForm] = useState('nat'), [bpm, setBpm] = useState(60), [cur, setCur] = useState(-1), [hunt, setHunt] = useState(false), [found, setFound] = useState([]), [bad, setBad] = useState(null);
  const minor = key === 'Em' || key === 'Dm', k = minor && form === 'har' ? key + 'h' : key, targets = spThumbs(k);
  const reset = (fn) => { T.clear(); setCur(-1); setHunt(false); setFound([]); setBad(null); if (fn) fn(); };
  const play = () => { reset(); const KR = spKeys(k, 'R', 2), KL = spKeys(k, 'L', 2), ix = spUpDown(15);
    const run = spPlay(ix.map((j, s) => ({ at: s / 2, keys: [KR[j], KL[j]], len: s === ix.length - 1 ? 2 : 0.5, vol: 0.12 })), bpm, 4); if (!run) return;
    const ctx = run.ctx; for (let b = 0; b < Math.ceil(ix.length / 2) + 1; b++) metroClick(ctx, run.t0 + (4 + b) * run.spb, false, 0.16);
    ix.forEach((j, s) => T.at(run.ms(s / 2), () => setCur(j))); T.at(run.ms(ix.length / 2 + 1.2), () => setCur(-1)); };
  const tap = (j) => { if (!hunt || found.length === targets.length) return; playKey(spKeys(k, 'R', 2)[j], 0.5);
    if (targets.includes(j)) { if (found.includes(j)) return; const nf = found.concat([j]); setFound(nf); setBad(null); if (nf.length === targets.length && onResult) onResult({ ok: true }); }
    else { setBad(j); T.at(1100, () => setBad(null)); } };
  const done = hunt && found.length === targets.length, s = spStripCols(k);
  return (
    <div className="try-box" style={actBox} data-sp="two">
      <div style={actTitle}>{t('Two octaves, hands together', '두 옥타브, 양손 함께')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>오른손 번호는 위, 왼손 번호는 아래. 두 손은 한 옥타브 떨어져서 같은 음을 쳐요. <b>한 박에 두 음: 티-티</b>. 두 엄지가 함께 치는 곳을 찾아봐요.</> : <>The right hand's fingers above, the left hand's below; the hands play the same notes an octave apart. <b>Two notes on every beat: run-ning</b>. Find where both thumbs play together.</>}</div>
      {spChips([['G', t('G major', 'G장조')], ['F', t('F major', 'F장조')], ['Em', t('E minor', 'E단조')], ['Dm', t('D minor', 'D단조')]], key, (x) => reset(() => setKey(x)))}
      {minor && spChips([['nat', t('Natural', '자연')], ['har', t('Harmonic', '화성')]], form, (x) => reset(() => setForm(x)))}
      <SpStrip k={k} cur={cur} found={found} bad={bad} onTap={hunt ? tap : null}/>
      {spMsg(hunt ? (done ? t(targets.length === 1 ? 'Only once: the ' + s.N[targets[0]] + ' in the middle. Everywhere else the thumbs turn at different times.' : targets.length + ' places: ' + targets.map(j => s.N[j]).join(', ') + '. In F major the thumbs meet more often.', targets.length === 1 ? '딱 한 번: 가운데 ' + s.N[targets[0]] + '. 다른 곳에서는 엄지가 따로따로 넘어가요.' : targets.length + '곳: ' + targets.map(j => s.N[j]).join(', ') + '. F장조는 엄지가 더 자주 만나요.')
        : bad != null ? t('Not there: look for a 1 above and a 1 below.', '거기가 아니에요: 위에도 1, 아래에도 1인 곳.') : t('Tap the notes where both thumbs play: ' + found.length + ' of ' + targets.length, '두 엄지가 함께 치는 음을 눌러요: ' + targets.length + '개 중 ' + found.length + '개'))
        : cur >= 0 ? t('run-ning, run-ning…', '티-티, 티-티…') : k === 'F' ? t('F major’s right hand: finger 4 always on B♭.', 'F장조 오른손: B♭은 언제나 4번.') : '', done ? BK.green : bad != null ? BK.coral : undefined)}
      {spChips([[60, spMM(60)], [76, spMM(76)]], bpm, (x) => reset(() => setBpm(x)))}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap'}}>
        <button className="ghost-btn" style={spBtn} onClick={play}>{t('▶ Hands together', '▶ 양손 함께 듣기')}</button>
        <button className="ghost-btn" style={spBtn} onClick={() => { reset(); setHunt(true); }}>{done ? t('▶ Again', '▶ 다시') : t('▶ Find the thumbs', '▶ 엄지 찾기')}</button>
      </div>
    </div>
  );
}

// ── the pictures on paper ──
function spMiniKeys(lo, hi, lit = {}, W = 9, H = 30, x0 = 2, y0 = 12) {
  const a = spIsW(lo) ? lo : lo - 1, b = spIsW(hi) ? hi : hi + 1, w0 = spWIdx(a), nw = spWIdx(b) - w0 + 1, BW = W * 0.6, BH = H * 0.6, out = [];
  out.push('<rect x="' + x0 + '" y="' + y0 + '" width="' + nw * W + '" height="' + H + '" fill="#fff" stroke="' + PEN_N + '" stroke-width="1.3"/>');
  for (let i = a; i <= b; i++) if (spIsW(i)) { const x = x0 + (spWIdx(i) - w0) * W; if (lit[i]) out.push('<rect x="' + (x + 0.8) + '" y="' + (y0 + 0.8) + '" width="' + (W - 1.6) + '" height="' + (H - 1.6) + '" fill="' + (lit[i] === 'cor' ? PEN_C : '#fbe3da') + '"/>'); if (i > a) out.push('<line x1="' + x + '" x2="' + x + '" y1="' + y0 + '" y2="' + (y0 + H) + '" stroke="' + PEN_N + '" stroke-width="1"/>'); }
  for (let i = a; i <= b; i++) if (!spIsW(i)) { const x = x0 + (spWIdx(i) - w0 + 1) * W; out.push('<rect x="' + (x - BW / 2) + '" y="' + y0 + '" width="' + BW + '" height="' + BH + '" fill="' + (lit[i] === 'cor' ? PEN_C : PEN_N) + '"/>'); }
  return { svg: out.join(''), kx: (i) => x0 + (spWIdx(i) - w0 + (spIsW(i) ? 0.5 : 1)) * W, w: nw * W + 2 * x0 };
}
const spPicTurn = () => { const m = spMiniKeys(0, 12, { 0: 'pale', 2: 'pale', 4: 'pale', 5: 'cor' }, 9, 30, 2, 4); const x1 = m.kx(0), x2 = m.kx(5);
  return { shapes: [{ k: 'raw', svg: m.svg + '<path d="M' + x1 + ',37 Q' + ((x1 + x2) / 2) + ',50 ' + x2 + ',37" fill="none" stroke="#e4572e" stroke-width="2"/><path d="M' + (x2 - 5) + ',40 L' + x2 + ',37 L' + (x2 + 1) + ',43" fill="none" stroke="#e4572e" stroke-width="2"/>' }], vb: [0, 0, m.w, 50] }; };
const spPicBeat = () => ({ shapes: [{ k: 'raw', svg: [1, 2, 3, 1].map((f, i) => lsCircleSvg(12 + i * 19, 22, 8, i === 2 ? 'play' : 'beat', String(f))).join('') }], vb: [0, 0, 80, 44] });
const spPicMinor = () => { const m = spMiniKeys(-3, 9, { [-3]: 'pale', [-1]: 'pale', 0: 'pale', 2: 'pale', 4: 'pale', 5: 'pale', 8: 'cor', 9: 'pale' }); return { shapes: [{ k: 'raw', svg: m.svg }], vb: [0, 0, m.w, 44] }; };
const spPicMirror = () => ({ shapes: [{ k: 'raw', svg: lsCircleSvg(30, 22, 8, 'beat', '1') + lsCircleSvg(50, 22, 8, 'beat', '1') + '<path d="M20 22 L6 22 M10 18 L6 22 L10 26 M60 22 L74 22 M70 18 L74 22 L70 26" fill="none" stroke="#e4572e" stroke-width="2"/>' }], vb: [0, 0, 80, 44] });
const spPicTwo = () => ({ shapes: [{ k: 'raw', svg: [0, 1, 2].map(b => '<rect x="' + (3 + b * 26) + '" y="11" width="22" height="22" rx="6" fill="' + (b % 2 ? '#fff' : 'rgba(38,41,107,0.10)') + '"/>' + lsCircleSvg(9 + b * 26, 22, 5, 'play', '') + lsCircleSvg(20 + b * 26, 22, 5, 'play', '')).join('') }], vb: [0, 0, 80, 44] });

function spLbPages(scr = false) {
  const ch = 'scale-play', sc = bkChapterNo('scales');
  const checks5 = [[spPicTurn(), t('I turn the thumb under and 3 over without a bump', '엄지 밑으로 넣기와 3번 넘기기를 덜컹하지 않게 해요')], [spPicBeat(), t('I play C and G major, each hand, one note a beat, at metronome 76', 'C장조와 G장조를 한 손씩, 메트로놈 76에 한 박에 한 음으로 쳐요')],
    [spPicMinor(), t('I play A and E minor, natural and harmonic', 'A단조와 E단조를 자연·화성 단음계로 쳐요')], [spPicMirror(), t('I play contrary motion from one note: mirror twins', '한 음에서 반대 방향으로 쳐요: 거울 쌍둥이')], [spPicTwo(), t('Grade 1: I play two octaves, hands together, two notes a beat', 'Grade 1: 두 옥타브를 양손 함께, 한 박에 두 음으로 쳐요')]];
  const pen = (x) => <PenArt shapes={x.shapes} vb={x.vb} style={{width:90}}/>;
  const toc = [[t('Smooth turns', '매끄럽게 넘기기'), 2], [t('On the beat', '박에 맞춰'), 3], [t('A and E minor', 'A단조와 E단조'), 4], [t('Mirror twins', '거울 쌍둥이'), 5], [t('Two octaves, hands together', '두 옥타브, 양손 함께'), 6], [t('My five checks', '나의 다섯 가지 확인'), 7]];
  const KC = spKeys('C', 'R', 1), FC = spFing('C', 'R', 1);
  const cS = spCm('C');
  const minorStill = <LbPic h={170}><div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:14,width:'100%'}}>{['Am', 'Amh'].map(x => { const K = spKeys(x, 'R', 1), h = x === 'Amh';
    return <div key={x}><div style={{textAlign:'center',fontSize:13,fontWeight:900,color:h ? BK.coral : BK.ink,marginBottom:2}}>{spName(x)}</div>
      <SpKb lo={K[0]} hi={K[7]} W={24} H={62} lit={Object.fromEntries(K.map((y, j) => [y, h && j === 6 ? 'cor' : 'pale']))} names={spNameMap(K, spNames(x, 1))} up={spFingMap(K, spFing(x, 'R', 1))}/></div>; })}</div></LbPic>;
  return [
    // 1. opener
    <LbPage key="1" no={1} chId={ch} teacher={<>{spTx(t('This room plays the scales that chapter ' + sc + ' explains: the fingerings are there (thumb under, 3 over). Scales are played from memory, mf and legato. The fingerings shown are the usual ones; another fingering is fine if it is logical and used the same way every time. Prelim: C and G major, A and E minor (natural and harmonic), one octave, hands separately, one note a beat at ♩ = 76; contrary motion in C major and A harmonic minor, one octave, ♩ = 66. Grade 1: G and F major, E and D minor (natural and harmonic), two octaves, hands separately and together, two notes a beat at ♩ = 76; contrary motion over two octaves at ♩ = 66; and the chromatic scale from G (see chapter ' + sc + ').', '이 방에서는 ' + sc + '장에서 배운 음계를 실제로 쳐요. 손가락 번호(엄지 밑으로 넣기, 3번 넘기기)는 거기 있어요. 음계는 외워서, mf로, 레가토로 쳐요. 여기 나온 손가락 번호는 흔히 쓰는 것이고, 논리적이고 매번 같게 쓴다면 다른 번호도 괜찮아요. Prelim: C장조와 G장조, A단조와 E단조(자연·화성), 한 옥타브, 한 손씩, ♩ = 76에 한 박에 한 음. 반대 방향은 C장조와 A 화성 단음계, 한 옥타브, ♩ = 66. Grade 1: G장조와 F장조, E단조와 D단조(자연·화성), 두 옥타브, 한 손씩 그리고 양손 함께, ♩ = 76에 한 박에 두 음. 반대 방향은 두 옥타브로 ♩ = 66. 그리고 G에서 시작하는 반음계(' + sc + '장 참고).'))}</>} qr={bkLink('drill=' + ch + '&lock=1')}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:50,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{t('Playing Scales', '스케일 치기')}</div>
      </div></LbOnly>
      <LbPic h={190}><div style={{width:'100%',maxWidth:560,margin:'0 auto'}}><SpKb lo={KC[0]} hi={KC[7]} W={44} H={92} lit={Object.fromEntries(KC.map(x => [x, 'pale']))} names={spNameMap(KC, spNames('C', 1))} up={spFingMap(KC, FC)} arc={{ from: KC[0], to: KC[3], over: false }} label={t('C major, right hand: 1 2 3, thumb under, 1 2 3 4 5', 'C장조 오른손: 1 2 3, 엄지 밑으로 넣기, 1 2 3 4 5')}/></div></LbPic>
      <LbSay size={18}>{t('Scales live in the hands. Turn without a bump, keep the beat, then minor scales, mirror twins, and two octaves with both hands.', '음계는 손이 기억해요. 덜컹하지 않게 넘기고, 박을 지키고, 그다음 단음계, 거울 쌍둥이, 그리고 양손으로 두 옥타브.')}</LbSay>
      <div className="lb-toc" style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>
        <LbOnly print><div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('In this chapter', '이 챕터에서는')}</div>
          {toc.map(([n, p]) => <div key={p} className="lb-toc-row" style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:14.5,padding:'5px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkGoal(15)}{n}</span><span style={{color:BK.muted,fontWeight:800}}>{p}</span></div>)}
        </div></LbOnly>
        <div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 챕터를 마치면')}</div>
          {[t('turn the thumb under and 3 over without a bump', '엄지 밑으로 넣기와 3번 넘기기를 덜컹하지 않게 할 수 있어요'), t('play a scale with one note on every beat', '한 박에 한 음씩 음계를 칠 수 있어요'), t('play A and E minor, natural and harmonic', 'A단조와 E단조를 자연·화성 단음계로 칠 수 있어요'), t('play contrary motion: mirror twins', '반대 방향으로 칠 수 있어요: 거울 쌍둥이'), t('play two octaves with both hands together', '두 옥타브를 양손 함께 칠 수 있어요')].map(x => <div key={x} style={{display:'flex',gap:9,alignItems:'flex-start',fontSize:14.5,padding:'5px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}><span style={{flex:'0 0 auto',marginTop:3}}>{bkGoal(15)}</span><span>{x}</span></div>)}
        </div>
      </div>
      <LbOnly print><LbDrillStrip id={ch}/></LbOnly>
    </LbPage>,
    // 2. smooth turns
    <LbPage key="2" no={2} chId={ch} kicker={t('Step 1', '1단계')} title={t('Smooth turns', '매끄럽게 넘기기')}
      teacher={<>{t('The turn is where a scale bumps: a late thumb, a loud note, a hand that jumps. The thumb starts moving under as 2 plays, so it is over its key before it is needed; the wrist stays level and the elbow does not fly out: the arm carries the hand along (chapter ' + bkChapterNo('posture-hands') + '). Play one bumpy on purpose and ask the child to spot it.', '음계가 덜컹하는 곳은 넘기는 곳이에요: 늦게 오는 엄지, 갑자기 큰 음, 튀어 오르는 손. 엄지는 2번이 칠 때부터 밑으로 움직여서, 필요하기 전에 이미 건반 위에 있어요. 손목은 평평하게, 팔꿈치는 바깥으로 튀어나가지 않게: 팔이 손을 데려가요(' + bkChapterNo('posture-hands') + '장). 일부러 덜컹하게 한 번 쳐 주고 아이가 찾아내게 해 주세요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=5')}>
      <LbLive still={<LbPic h={170}><div style={{width:'100%',maxWidth:620,margin:'0 auto'}}><SpKb maxW={600} lo={KC[0]} hi={KC[7]} W={40} H={84} lit={Object.fromEntries(KC.map((x, j) => [x, j === 3 ? 'cor' : 'pale']))} names={spNameMap(KC, spNames('C', 1))} hand={[KC[3], KC[4], KC[5], KC[6], KC[7]]} hf={1} arc={{ from: KC[0], to: KC[3], over: false }}/></div></LbPic>} live={<SpTurnPad/>}/>
      <LbSay>{LANG === 'ko' ? <>음계에서는 <b>손이 자리를 옮겨요</b>. 엄지는 <b>미리 준비해요</b>: 2번과 3번이 치는 동안 손 밑으로 들어가 있어요. 그리고 팔이 손을 데려가요. 들어 봐요: 모든 음이 고르게, <b>넘길 때 덜컹하지 않게</b>.</> : <>In a scale <b>the hand moves on</b>. The thumb <b>gets ready early</b>: it slides under while 2 and 3 are playing. Then the arm carries the hand along. Listen: every note even, <b>no bump at the turn</b>.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>오른손, C장조, 천천히: 2번이 D를 칠 때 엄지를 손 밑으로 미끄러뜨려요. 필요하기 전에 F 위에 가 있어요.</>,
        <>올라갔다 내려오기를 네 번. 넘기는 곳을 들어 봐요: F가 늦거나 크게 났나요? 모든 음을 똑같이.</>,
        <>왼손도 똑같이, 방향만 반대: 올라갈 때 3번 넘기기, 내려올 때 엄지 밑으로 넣기.</>,
      ] : [
        <>Right hand, C major, slowly: as finger 2 plays D, let the thumb slide under the hand. It is over F before you need it.</>,
        <>Up and back, four times. Listen to the turn: was F late, or loud? Make every note the same.</>,
        <>Left hand, the same the other way round: 3 over going up, thumb under coming down.</>,
      ]}/>
      <LbRemember>{t('The thumb gets ready early: no bump.', '엄지는 미리 준비: 덜컹 없이.')}</LbRemember>
    </LbPage>,
    // 3. on the beat
    <LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={t('On the beat', '박에 맞춰')}
      teacher={<>{spTx(t('One octave, hands separately, one note a beat: the target is ♩ = 76, legato, mf. Start at 60 with a metronome; move up only when the turns are even. The last note is held for two beats. The app clicks on: listen for the hands running ahead after a turn.', '한 옥타브, 한 손씩, 한 박에 한 음: 목표는 ♩ = 76, 레가토, mf. 메트로놈 60에서 시작해서, 넘기는 곳이 고르게 될 때만 빠르기를 올려요. 마지막 음은 두 박. 앱의 클릭은 계속 가요: 넘긴 다음 손이 앞서 달리지 않는지 들어 봐 주세요.'))}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=1')}>
      <LbLive still={<LbPic h={190}><div style={{display:'flex',flexDirection:'column',gap:8,width:'100%',maxWidth:620,margin:'0 auto'}}><SpKb maxW={600} lo={KC[0]} hi={KC[7]} W={40} H={80} lit={Object.fromEntries(KC.map(x => [x, 'pale']))} names={spNameMap(KC, spNames('C', 1))} up={spFingMap(KC, FC)}/>
        <PlCircles n={15} r={scr ? 9 : 11} gap={scr ? 21 : 26} group={8} kind={() => 'finger'} label={(s) => String(FC[spUpDown(8)[s]])}/></div></LbPic>} live={<SpBeatPad/>}/>
      <LbSay>{LANG === 'ko' ? <>C장조와 G장조, 한 옥타브, 한 손씩. <b>박마다 한 음</b>, 올라갔다 내려와요. 마지막 음은 두 박. 먼저 천천히({spCrot} = 60), 그다음 목표 빠르기 <b>{spCrot} = 76</b>. mf, 레가토로.</> : <>C major and G major, one octave, one hand at a time. <b>One note on every beat</b>, up and back; the last note holds for two. Slowly first ({spCrot} = 60), then the target speed, <b>{spCrot} = 76</b>. mf, legato.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>메트로놈 60. 네 번 듣고, 오른손 C장조를 박마다 한 음씩. 숫자를 세며: 1 2 3 4.</>,
        <>왼손도. 그다음 G장조: 오른손 4번이 F♯, 왼손 2번이 F♯.</>,
        <>넘기는 곳이 고르면 메트로놈을 76으로. 외워서 쳐요.</>,
      ] : [
        <>Metronome on 60. Listen to four clicks, then right hand C major, one note a click. Count: 1 2 3 4.</>,
        <>Now the left hand. Then G major: right hand finger 4 on F♯, left hand finger 2 on F♯.</>,
        <>When the turns are even, set the metronome to 76. Play it from memory.</>,
      ]}/>
      <LbRemember>{t('One note on every beat; the last one holds.', '박마다 한 음, 마지막 음은 길게.')}</LbRemember>
    </LbPage>,
    // 4. A and E minor
    <LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title={t('A and E minor', 'A단조와 E단조')}
      teacher={<>{t('Each minor in two forms: natural, then harmonic, which raises the 7th by a half step (A: G♯; E: D♯). The fingers are C major\'s in both hands. Sing the top of the harmonic minor slowly (6, raised 7, 8) before playing: the wider step between 6 and the raised 7 is the sound to listen for.', '단음계마다 두 가지: 자연, 그다음 7번째 음을 반음 올리는 화성(A단조는 G♯, E단조는 D♯). 손가락은 양손 모두 C장조와 같아요. 치기 전에 화성 단음계의 꼭대기를 천천히 불러 보세요(6, 올라간 7, 8): 6과 올라간 7 사이의 넓은 걸음이 들어야 할 소리예요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=2')}>
      <LbLive still={minorStill} live={<SpMinorPad/>}/>
      <LbSay>{LANG === 'ko' ? <><b>A 자연 단음계</b>는 A부터 A까지 흰건반이에요. <b>화성 단음계</b>는 7번째 음을 반음 올려요: G가 <b>G♯</b>가 돼요. E단조에는 F♯가 있고, 화성에서는 D가 <b>D♯</b>가 돼요. 손가락은 C장조와 똑같아요.</> : <><b>A natural minor</b> is the white keys from A to A. The <b>harmonic minor</b> raises the 7th a half step: G becomes <b>G♯</b>. E minor has F♯, and in the harmonic D becomes <b>D♯</b>. The fingers are C major's.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>오른손, A 자연 단음계: 올라갔다 내려와요. 손가락은 C장조와 같아요: 1 2 3, 엄지 밑으로 넣기, 1 2 3 4 5.</>,
        <>이번엔 화성: 4번이 G♯. 왼손은 2번이 G♯. 꼭대기를 들어 봐요.</>,
        <>E단조로: 자연은 F♯ 하나, 화성은 D♯도. 둘 다 {spCrot} = 76으로, 한 손씩.</>,
      ] : [
        <>Right hand, A natural minor, up and back. The fingers are C major's: 1 2 3, thumb under, 1 2 3 4 5.</>,
        <>Now the harmonic: finger 4 plays G♯. In the left hand, finger 2. Listen to the top.</>,
        <>Now E minor: the natural has one F♯, the harmonic a D♯ too. Both at {spCrot} = 76, one hand at a time.</>,
      ]}/>
      <LbRemember>{t('Harmonic minor: the 7th goes up a half step.', '화성 단음계: 7번째 음이 반음 올라가요.')}</LbRemember>
    </LbPage>,
    // 5. mirror twins
    <LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title={t('Mirror twins', '거울 쌍둥이')}
      teacher={<>{spTx(t('Contrary motion: both hands start on one note and move apart. C major starts with both thumbs on middle C; A harmonic minor on the A below middle C. The fingers match all the way (1 with 1, 3 with 3) and both thumbs turn at the same moment, so this is the easiest way to begin hands together. Prelim: one octave, ♩ = 66, one note a beat. Grade 1: two octaves (C major, A harmonic minor, G major, E harmonic minor), two notes a beat.', '반대 방향: 두 손이 한 음에서 시작해서 멀어져요. C장조는 두 엄지가 가운데 도에서, A 화성 단음계는 가운데 도 아래 A에서 시작해요. 손가락 번호가 끝까지 같고(1과 1, 3과 3) 두 엄지가 같은 순간에 넘어가서, 양손 함께를 시작하기에 가장 쉬워요. Prelim: 한 옥타브, ♩ = 66, 한 박에 한 음. Grade 1: 두 옥타브(C장조, A 화성 단음계, G장조, E 화성 단음계), 한 박에 두 음.'))}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=3')}>
      <LbLive still={<LbPic h={190}><div style={{width:'100%',maxWidth:600,margin:'0 auto'}}><SpKb lo={cS.L[7]} hi={cS.R[7]} W={30} H={74} lit={Object.fromEntries(cS.R.concat(cS.L).map(x => [x, 'pale']))} names={Object.assign(spNameMap(cS.R, cS.nmR), spNameMap(cS.L, cS.nmL))} up={spFingMap(cS.R, SP_CM_F)} dn={spFingMap(cS.L, SP_CM_F)}/>
        <div style={{display:'flex',justifyContent:'space-between',fontSize:12.5,fontWeight:900,color:BK.muted,margin:'2px 4px 0'}}><span>{t('← left hand: down', '← 왼손: 아래로')}</span><span>{t('right hand: up →', '오른손: 위로 →')}</span></div></div></LbPic>} live={<SpMirrorPad/>}/>
      <LbSay>{LANG === 'ko' ? <>두 엄지를 <b>가운데 도(클라라)</b>에 함께 놓아요. 오른손은 위로, 왼손은 아래로 멀어졌다가 돌아와요. 두 손은 <b>언제나 같은 번호</b>를 쳐요: 거울 쌍둥이. 엄지도 함께 넘어가요.</> : <>Put both thumbs on <b>middle C (Clara)</b>. The right hand goes up, the left hand goes down, then they come back. The hands <b>always play the same number</b>: mirror twins. The thumbs turn together too.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>두 엄지를 가운데 도에. 번호를 소리 내어 말하며 천천히: 1 2 3, 엄지, 1 2 3 4 5.</>,
        <>내려올 때도 같은 번호를 함께: 5 4 3 2 1, 3번 넘기기, 3 2 1. 두 3번이 함께 넘어가요.</>,
        <>A 화성 단음계는 가운데 도 아래 A에서: 오른손 4번은 위의 G♯, 왼손 2번은 아래의 G♯. {spCrot} = 66.</>,
      ] : [
        <>Both thumbs on middle C. Say the numbers out loud, slowly: 1 2 3, thumb, 1 2 3 4 5.</>,
        <>Coming back, the same numbers together: 5 4 3 2 1, 3 over, 3 2 1. Both 3s cross over together.</>,
        <>A harmonic minor starts on the A below middle C: right hand 4 on the G♯ above, left hand 2 on the G♯ below. {spCrot} = 66.</>,
      ]}/>
      <LbRemember>{t('Same numbers, both ways: mirror twins.', '양쪽으로 같은 번호: 거울 쌍둥이.')}</LbRemember>
    </LbPage>,
    // 6. two octaves, hands together
    <LbPage key="6" no={6} chId={ch} kicker={t('Step 5', '5단계')} title={t('Two octaves, hands together', '두 옥타브, 양손 함께')}
      teacher={<>{spTx(t('Grade 1: G and F major, E and D minor (natural and harmonic), two octaves, hands separately and then together, an octave apart, at ♩ = 76 with two notes a beat. In G major and the minors the thumbs play together only on the middle tonic, so the turns come at different moments in each hand: practise hands together a few notes at a time around each turn. F major\'s right hand has its own fingering: 4 always on B♭.', 'Grade 1: G장조와 F장조, E단조와 D단조(자연·화성), 두 옥타브, 한 손씩 그다음 한 옥타브 떨어져 양손 함께, ♩ = 76에 한 박에 두 음. G장조와 단음계는 가운데 으뜸음에서만 두 엄지가 함께 쳐서, 두 손이 다른 순간에 넘어가요: 넘기는 곳마다 몇 음씩 끊어서 양손 연습을 해 주세요. F장조 오른손은 따로 정해진 번호가 있어요: B♭은 언제나 4번.'))}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=4')}>
      <LbLive still={<LbPic h={150}><div style={{width:'100%',maxWidth:560,margin:'0 auto'}}><SpStrip k="G" found={spThumbs('G')} mw={640}/></div></LbPic>} live={<SpTwoPad/>}/>
      <LbSay>{LANG === 'ko' ? <>Grade 1: <b>두 옥타브</b>, 한 손씩, 그다음 <b>양손 함께</b> 한 옥타브 떨어져서. 한 박에 두 음: <b>티-티, 티-티</b>. G장조에서 두 엄지는 <b>가운데 G에서만</b> 함께 쳐요. 다른 곳에서는 따로따로 넘어가요.</> : <>Grade 1: <b>two octaves</b>, each hand, then <b>hands together</b>, an octave apart. Two notes on every beat: <b>run-ning, run-ning</b>. In G major the thumbs play together <b>only on the middle G</b>; everywhere else they turn at different times.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>오른손 G장조 두 옥타브: 1 2 3, 1 2 3 4, 1 2 3, 1 2 3 4 5. 왼손: 5 4 3 2 1, 3 2 1, 4 3 2 1, 3 2 1.</>,
        <>양손 함께, 아주 천천히. 가운데 G에서 두 엄지가 만나요. 넘기는 곳마다 멈춰서 확인해요.</>,
        <>메트로놈 60에 티-티, 그다음 76. F장조, E단조, D단조도 같은 방법으로.</>,
      ] : [
        <>Right hand, G major, two octaves: 1 2 3, 1 2 3 4, 1 2 3, 1 2 3 4 5. Left hand: 5 4 3 2 1, 3 2 1, 4 3 2 1, 3 2 1.</>,
        <>Hands together, very slowly. The thumbs meet on the middle G. Stop at each turn and check.</>,
        <>Run-ning at metronome 60, then 76. F major, E minor and D minor the same way.</>,
      ]}/>
      <LbRemember>{t('Two notes a beat: run-ning. The thumbs meet in the middle.', '한 박에 두 음: 티-티. 엄지는 가운데에서 만나요.')}</LbRemember>
    </LbPage>,
    // 7. five checks
    <LbPage key="7" no={7} chId={ch} kicker={t('Check-up', '점검')} title={t('My five checks', '나의 다섯 가지 확인')}
      teacher={<>{t('Each one played to you, from memory. The fifth is Grade 1: leave it for later if the child is working towards Prelim.', '하나씩 외워서 선생님에게 들려줘요. 다섯째는 Grade 1이에요: Prelim을 준비하는 아이라면 나중으로 미뤄도 돼요.')}</>}>
      <LbSay>{t('At the piano, tick each one: not yet, nearly, or got it!', '피아노 앞에서 하나씩 표시해요: 아직, 거의, 됐어요!')}</LbSay>
      <LbLive still={<LbStageRows big rows={checks5.map(([a, txt]) => [pen(a), txt])}/>} live={<FiveChecks376 rows={checks5} storeKey="pb_sp_five"/>}/>
    </LbPage>,
  ];
}
function ScalePlayLessonBook() { return <>{spLbPages(false)}</>; }
function SpLearn({ onStart }) {
  const pages = spLbPages(true), opener = pages[0];
  return (
    <Lesson id="scale-play" title={t('Playing scales', '스케일 치기')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="scale-play"><div className="lb-screen lb-open" style={{display:'flex',flexDirection:'column',gap:12,margin:'0 0 8px'}}>{lbWordsFirst(opener.props.children)}</div></BkChapterCtx.Provider></LbScreenCtx.Provider>}>
      {pages.slice(1).map((pg, i) => <Step key={i} title={pg.props.title}><LbScreenPage page={pg}/></Step>)}
    </Lesson>
  );
}

// ── the drill: four to see, two to hear ──
const SP_LEVELS = [
  { n: 1, label: 'Which finger? One octave', kind: 'f1', time: 10 },
  { n: 2, label: 'Natural or harmonic?', kind: 'nh', time: 10 },
  { n: 3, label: 'Mirror twins: contrary motion', kind: 'mirror', time: 12 },
  { n: 4, label: 'Which finger? Two octaves', kind: 'f2', time: 12 },
  { n: 5, label: 'Listen: smooth or bumpy?', kind: 'bump', time: 16, noPrint: true },
  { n: 6, label: 'Listen: natural or harmonic?', kind: 'earNH', time: 16, noPrint: true },
];
Object.assign(LEVEL_KO, { 'Which finger? One octave': '몇 번 손가락? 한 옥타브', 'Natural or harmonic?': '자연? 화성?', 'Mirror twins: contrary motion': '거울 쌍둥이: 반대 방향', 'Which finger? Two octaves': '몇 번 손가락? 두 옥타브', 'Listen: smooth or bumpy?': '듣기: 매끄럽게? 덜컹?', 'Listen: natural or harmonic?': '듣기: 자연? 화성?' });
function genSpQuestion(lv, prev) {
  const uid = Math.random(), kind = lv.kind, hand = Math.random() < 0.5 ? 'R' : 'L';
  if (kind === 'f1') { let k, j, g = 0; do { k = pick(['C', 'G', 'Am', 'Amh', 'Em', 'Emh']); j = Math.floor(Math.random() * 8); } while (prev && prev.k === k && prev.j === j && g++ < 10);
    return { kind, k, hand, j, answer: spFing(k, hand, 1)[j], choices: [1, 2, 3, 4, 5], key: k + hand + j, uid }; }
  if (kind === 'nh' || kind === 'earNH') { let r, f, g = 0; do { r = pick(['A', 'E']); f = Math.random() < 0.5 ? 'nat' : 'har'; } while (prev && prev.r === r && prev.answer === f && g++ < 4);
    return { kind, r, k: r + 'm' + (f === 'har' ? 'h' : ''), hand: kind === 'earNH' ? 'R' : hand, answer: f, choices: ['nat', 'har'], key: r + f, uid }; }
  if (kind === 'mirror') { let k, j, g = 0; do { k = Math.random() < 0.6 ? 'C' : 'Amh'; j = 1 + Math.floor(Math.random() * 7); } while (prev && prev.k === k && prev.j === j && g++ < 10);
    const c = spCm(k), ans = spCmLet(c, 'L', j), pool = Array.from(new Set(c.nmL.filter(x => x !== ans)));
    return { kind, k, j, answer: ans, choices: shuffle([ans].concat(shuffle(pool).slice(0, 3))), key: k + j, uid }; }
  if (kind === 'f2') { let k, j, g = 0; do { k = pick(['G', 'F', 'Em', 'Emh', 'Dm', 'Dmh']); j = Math.floor(Math.random() * 15); } while (prev && prev.k === k && prev.j === j && g++ < 10);
    return { kind, k, hand, j, answer: spFing(k, hand, 2)[j], choices: [1, 2, 3, 4, 5], key: k + hand + j, uid }; }
  const k = Math.random() < 0.5 ? 'C' : 'G', b = Math.random() < 0.5;
  return { kind: 'bump', k, hand, answer: b ? 'bumpy' : 'smooth', choices: ['smooth', 'bumpy'], key: k + hand + b, uid };
}
const SP_WORD = { nat: () => t('Natural', '자연'), har: () => t('Harmonic', '화성'), smooth: () => t('Smooth', '매끄럽게'), bumpy: () => t('Bumpy', '덜컹') };
function spAnswerLabel(q) {
  if (q.kind === 'f1' || q.kind === 'f2') return t('finger ' + q.answer, q.answer + '번 손가락');
  if (q.kind === 'mirror') return q.answer;
  return SP_WORD[q.answer]();
}
function SpQuestion({ q, given, locked, onAnswer, pixel }) {
  const T = useSpTimers(), [at, setAt] = useState(-1), done = !!given;
  const play = () => { T.clear(); setAt(-1);
    if (q.kind === 'bump') spTurnRun(q.k, q.hand, q.answer === 'bumpy', setAt, T);
    else if (q.kind === 'earNH') spMinorRun(q.k, 'R', setAt, T); };
  const heard = q.kind === 'bump' || q.kind === 'earNH';
  useEffect(() => { if (!heard) return; const id = setTimeout(play, 350); return () => { clearTimeout(id); T.clear(); }; }, [q.uid]);
  const btnCls = pixel ? 'pixel-choice' : 'choice-btn', cls = (c) => btnCls + (!done ? '' : c === q.answer ? ' good' : given.ans === c ? ' bad' : '');
  const handW = spHand(q.hand);
  let title, fig = null;
  if (q.kind === 'f1') { const K = spKeys(q.k, q.hand, 1), F = spFing(q.k, q.hand, 1);
    title = t(handW + ', ' + SP_SC[q.k].en + ': which finger plays the coral key?', handW + ', ' + SP_SC[q.k].ko + ': 산호색 건반은 몇 번 손가락일까요?');
    fig = <SpKb lo={K[0]} hi={K[7]} W={30} lit={Object.fromEntries(K.map((x, j) => [x, j === q.j ? 'cor' : 'pale']))} names={spNameMap(K, spNames(q.k, 1))} up={done ? spFingMap(K, F) : {}} act={done ? { [K[q.j]]: true } : {}}/>; }
  else if (q.kind === 'nh') { const K = spKeys(q.k, q.hand, 1);
    title = t(q.r + ' minor: natural or harmonic?', q.r + '단조: 자연일까요, 화성일까요?');
    fig = <SpKb lo={K[0]} hi={K[7]} W={30} lit={Object.fromEntries(K.map((x, j) => [x, done && j === 6 ? 'cor' : 'pale']))} names={spNameMap(K, spNames(q.k, 1))}/>; }
  else if (q.kind === 'mirror') { const c = spCm(q.k), f = SP_CM_F[q.j], lit = {}; c.R.concat(c.L).forEach(x => { lit[x] = 'pale'; }); lit[c.R[q.j]] = 'cor'; if (done) lit[c.L[q.j]] = 'good';
    title = t('Contrary motion, ' + SP_CM[q.k].en + '. The right hand plays ' + spCmLet(c, 'R', q.j) + ' with finger ' + f + '. Which key does the left hand’s finger ' + f + ' play?', '반대 방향, ' + SP_CM[q.k].ko + '. 오른손 ' + f + '번: ' + spCmLet(c, 'R', q.j) + '. 왼손 ' + f + '번은 어느 건반일까요?');
    fig = <SpKb lo={c.L[7]} hi={c.R[7]} W={22} H={66} lit={lit} names={done ? Object.assign(spNameMap(c.R, c.nmR), spNameMap(c.L, c.nmL)) : spNameMap(c.R, c.nmR)} up={{ [c.R[q.j]]: f }} dn={done ? { [c.L[q.j]]: f } : {}} act={{ [c.R[q.j]]: true, ['d' + c.L[q.j]]: true }} k={1.5}/>; }
  else if (q.kind === 'f2') { const s = spStripCols(q.k), hide = s.N.map((_, j) => j === q.j && !done);
    title = t(handW + ', ' + SP_SC[q.k].en + ', two octaves: which finger plays the coral note?', handW + ', ' + SP_SC[q.k].ko + ', 두 옥타브: 산호색 음은 몇 번 손가락일까요?');
    fig = <SpStrip k={q.k} ask={q.j} hideR={q.hand === 'R' ? hide : null} hideL={q.hand === 'L' ? hide : null}/>; }
  else if (q.kind === 'bump') { const K = spKeys(q.k, q.hand, 1), S = spTurnSeq(q.k, q.hand), cur = at >= 0 ? S[at] : null;
    title = t('Listen to the turns: smooth, or bumpy?', '넘기는 곳을 들어 봐요: 매끄럽게? 덜컹?');
    fig = <SpKb lo={K[0]} hi={K[7]} W={28} lit={Object.fromEntries(K.map(x => [x, cur && cur.key === x ? 'cor' : 'pale']))} hand={(cur || S[0]).win} hf={cur ? cur.f : null}/>; }
  else { const K = spKeys(q.k, 'R', 1), ix = spUpDown(8);
    title = t(q.r + ' minor: natural or harmonic?', q.r + '단조: 자연일까요, 화성일까요?');
    fig = <SpKb lo={K[0]} hi={K[7]} W={28} lit={Object.fromEntries(K.map(x => [x, at >= 0 && K[ix[at]] === x ? 'cor' : 'pale']))} names={done ? spNameMap(K, spNames(q.k, 1)) : null}/>; }
  const label = (c) => (typeof c === 'number' ? c : SP_WORD[c] ? SP_WORD[c]() : c);
  const why = !done ? null : q.kind === 'f1' ? t(handW + ': ' + (q.hand === 'R' ? '1 2 3, thumb under, 1 2 3 4 5.' : '5 4 3 2 1, 3 over, 3 2 1.'), handW + ': ' + (q.hand === 'R' ? '1 2 3, 엄지 밑으로 넣기, 1 2 3 4 5.' : '5 4 3 2 1, 3번 넘기기, 3 2 1.'))
    : q.kind === 'nh' || q.kind === 'earNH' ? t(q.answer === 'har' ? 'Harmonic: the 7th is raised, ' + SP_SC[q.r + 'mh'].nm[6] + '.' : 'Natural: the 7th is ' + SP_SC[q.r + 'm'].nm[6] + ', not raised.', q.answer === 'har' ? '화성: 7번째 음이 올라갔어요(' + SP_SC[q.r + 'mh'].nm[6] + ').' : '자연: 7번째 음이 ' + SP_SC[q.r + 'm'].nm[6] + ', 올라가지 않았어요.')
    : q.kind === 'mirror' ? t('Mirror twins: the same number of steps from the middle, the same finger.', '거울 쌍둥이: 가운데에서 같은 걸음 수, 같은 손가락.')
    : q.kind === 'f2' ? (q.k === 'F' && q.hand === 'R' ? t('F major’s right hand: 1 2 3 4, 1 2 3, 1 2 3 4, 1 2 3, 4.', 'F장조 오른손: 1 2 3 4, 1 2 3, 1 2 3 4, 1 2 3, 4.') : t(q.hand === 'R' ? 'Right hand: 1 2 3, 1 2 3 4, 1 2 3, 1 2 3 4 5.' : 'Left hand: 5 4 3 2 1, 3 2 1, 4 3 2 1, 3 2 1.', q.hand === 'R' ? '오른손: 1 2 3, 1 2 3 4, 1 2 3, 1 2 3 4 5.' : '왼손: 5 4 3 2 1, 3 2 1, 4 3 2 1, 3 2 1.'))
    : q.answer === 'bumpy' ? t('Bumpy: the note after each turn came late and loud.', '덜컹: 넘긴 다음 음이 늦고 크게 났어요.') : t('Smooth: every note even, the turns too.', '매끄럽게: 넘기는 곳까지 모든 음이 고르게.');
  const cols = q.choices.length === 5 ? 5 : q.choices.length === 4 ? 4 : 2;
  return (<div>
    <p style={pixel ? {fontSize:11.5,textAlign:'center'} : {fontSize:15,fontWeight:700,textAlign:'center',margin:'0 0 8px',color:'var(--muted)',textWrap:'balance'}}>{title}</p>
    {heard && <div style={{textAlign:'center',marginBottom:10}}><button className={pixel ? 'pixel-btn' : 'ghost-btn'} style={{minHeight:44}} onClick={play}>{t('▶ Play it again', '▶ 다시 듣기')}</button></div>}
    <div style={{marginBottom:12}}>{fig}</div>
    <div style={{display:'grid',gridTemplateColumns:'repeat(' + cols + ',minmax(0,1fr))',gap:8}}>{q.choices.map(c => <button key={c} disabled={locked} className={cls(c)} style={{padding:pixel ? '14px 4px' : '12px 4px',fontSize:pixel ? 9.5 : 16,fontWeight:900}} onClick={() => { if (locked || done) return; T.clear(); setAt(-1); onAnswer(c); }}>{label(c)}</button>)}</div>
    {why && !pixel && <div style={{marginTop:10,fontSize:13.5,color:'#4a4d86',background:'#fff',borderRadius:8,padding:'7px 10px',lineHeight:1.45}}>{why}</div>}
  </div>);
}
Object.assign(SCALE_PLAY_DRILL, { levels: SP_LEVELS, generate: genSpQuestion, check: (q, ans) => ans !== null && ans !== undefined && ans === q.answer, answerLabel: spAnswerLabel, Question: SpQuestion, Learn: SpLearn });
