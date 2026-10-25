
// ─── Chapter 6: Listen and Sing (Build X, 2026-10-26; the Beginner floor's aural room, decided 25 Oct) ───
// Ears first: keep the beat when the music stops, echo a rhythm, hear up or down (the bird and the turtle), sing a note and
// find it on the keys, sing a short tune back and play it. On the keys only, in C position (chapter 5); the rhythms in chapter
// 3's beat words (walk, run-ning). The app plays and listens to taps; whether a child sang in tune is the teacher's ear.
const LS_BPM = 80;
const lsHz = (d) => 440 * Math.pow(2, (60 + hpSemi(d) - 69) / 12);
const lsNote = (ctx, tm, d, len, vol = 0.2) => blip(ctx, tm, lsHz(d), len, vol, 'triangle');
const lsPlay = (d, len = 0.7) => playKey(hpSemi(d), len);
// play notes (d, or [d, beats]) one after another; returns stop()
function lsSeq(notes, gap = 560, onStep) {
  const ts = []; let at = 0;
  notes.forEach((n, j) => { const [d, b] = Array.isArray(n) ? n : [n, 1]; ts.push(setTimeout(() => { lsPlay(d, Math.max(0.35, b * gap / 1000 * 0.9)); if (onStep) onStep(j); }, at)); at += b * gap; });
  ts.push(setTimeout(() => { if (onStep) onStep(-1); }, at)); return () => ts.forEach(clearTimeout);
}
const lsBtn = { padding:'10px 14px', fontSize:14, minHeight:44 };
const lsMsg = (txt, col) => <div style={{textAlign:'center',fontSize:15,fontWeight:900,color:col || 'var(--navy)',minHeight:22,lineHeight:1.35}}>{txt}</div>;
const lsClara = (w = 30) => <PenArt shapes={sfClara(26, 31, 1.2)} vb={[0, 0, 52, 58]} style={{width:w}}/>;

// ── step 1: keep the beat; the music stops for a bar, the beat does not ──
// a little tune in C position over C and G chords: two bars, a quiet bar, a last bar (beats counted from the first bar)
const LS_MEL = [[0, 28, 1], [1, 29, 1], [2, 30, 1], [3, 28, 1], [4, 30, 1], [5, 31, 1], [6, 32, 2], [12, 30, 1], [13, 29, 1], [14, 28, 2]];
const lsChord = (b) => (b >= 8 && b < 12 ? null : b === 6 || b === 7 || b === 12 || b === 13 ? [18, 20, 22] : [21, 23, 25]);
const lsQuiet = (b) => b >= 8 && b < 12;
function lsBeatRun() {
  return plRun(4 + 16, { bpm: LS_BPM, silentFrom: 4, extra: (ctx, tm, i, spb) => { if (i < 4) return; const b = i - 4, ch = lsChord(b);
    if (ch) ch.forEach(d => lsNote(ctx, tm, d, spb * 0.55, 0.06));
    LS_MEL.filter(m => m[0] === b).forEach(m => lsNote(ctx, tm, m[1], m[2] * spb * 0.9, 0.2)); } });
}
function LsBeatPad({ onResult }) {
  const T = usePlTimers();
  const [phase, setPhase] = useState('ready'), [lit, setLit] = useState(-1), [res, setRes] = useState(null);
  const run = useRef(null), taps = useRef([]);
  function start() {
    T.clear(); setRes(null); taps.current = [];
    const r = lsBeatRun(); if (!r) return; run.current = r;
    r.at.forEach((a, i) => T.at(r, a, () => { setLit(i - 4); setPhase(i < 4 ? 'count' : lsQuiet(i - 4) ? 'quiet' : 'go'); }));
    T.at(r, r.at[19] + r.spb * 0.9, () => {
      setLit(-1); setPhase('done');
      const at = r.at.slice(4), m = plMatch(at, taps.current.filter(tp => tp > r.at[4] - PL_TOL));
      const quiet = m.offs.slice(8, 12).filter(o => o !== null).length;
      const out = { hits: m.hits, total: 16, quiet, extra: m.extra, marks: m.offs.map(o => (o === null ? '?' : '✓')), ok: m.hits >= 14 && quiet >= 3 && m.extra <= 2 };
      setRes(out); if (onResult) onResult(out);
    });
    setPhase('count');
  }
  const tap = React.useCallback(() => { const r = run.current; if (r && (phase === 'count' || phase === 'go' || phase === 'quiet')) taps.current.push(r.now()); }, [phase]);
  const live = phase === 'count' || phase === 'go' || phase === 'quiet';
  return (
    <div className="try-box" style={actBox} data-ls="beat">
      <div style={actTitle}>{t('Keep the beat', '박 지키기')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>클릭 4번을 듣고, 음악에 맞춰 박마다 패드를 쳐요. 셋째 마디에서 <b>음악이 멈춰도</b> 계속 쳐요. 넷째 마디에서 음악이 돌아올 때 함께 있나요?</> : <>Listen to 4 clicks, then tap every beat with the music. In bar 3 <b>the music stops</b>: keep tapping. When it comes back in bar 4, are you still with it?</>}</div>
      <PlCircles n={16} r={12} gap={30} kind={(i) => (lsQuiet(i) ? 'silent' : 'beat')} lit={lit} mark={(i) => (res ? res.marks[i] : null)}/>
      {lsMsg(phase === 'count' ? t('Get ready…', '준비…') : phase === 'go' ? t('Tap the beat', '박을 쳐요') : phase === 'quiet' ? t('The music stopped: keep going!', '음악이 멈췄어요: 계속 쳐요!') : '', phase === 'quiet' ? BK.coral : undefined)}
      <PlPad on={live} onTap={tap}/>
      <div style={{textAlign:'center',marginTop:8}}><button className="ghost-btn" style={lsBtn} onClick={start}>{phase === 'done' ? t('▶ Again', '▶ 다시') : t('▶ Start', '▶ 시작')}</button></div>
      {res && lsMsg(t('On the beat: ' + res.hits + ' of 16 · in the quiet bar: ' + res.quiet + ' of 4', '박에 맞게: 16개 중 ' + res.hits + '개 · 조용한 마디에서: 4개 중 ' + res.quiet + '개') + (res.ok ? ' ✓' : ''), res.ok ? BK.green : BK.coral)}
      {plHint()}
    </div>
  );
}

// ── step 2: echo a rhythm: two bars played, two bars tapped back, the beat never stopping ──
// cells, one a beat: 'w' walk (one sound), 'r' run-ning (two), '-' hold the last sound, '.' a silent beat
const LS_ECHO = ['w w w - | w w w -', 'w w r w | w w w -', 'r r w w | r r w -', 'w - w - | w w w -', 'w w . w | w w w -', 'r w r w | r r w -'].map(s => s.split(' ').filter(x => x !== '|'));
const lsOnsets = (cells) => cells.flatMap((c, i) => (c === 'w' ? [i] : c === 'r' ? [i, i + 0.5] : []));
const lsHold = (cells, i) => { let k = 1; while (cells[i + k] === '-') k++; return k; };
const lsBeatWord = (c) => (c === 'w' ? t('walk', '타') : c === 'r' ? t('run-ning', '티-티') : '');
function LsCells({ cells, lit = -1, show = true, size = 30 }) {
  const Z = size, half = cells.length / 2;
  const cell = (c, i) => { const on = i === lit, box = { width:Z, height:Z, boxSizing:'border-box', display:'inline-flex', alignItems:'center', justifyContent:'center', gap:3, borderRadius:Z / 2, transition:'background .1s' };
    if (!show) return <span style={{...box,border:'2px solid ' + (on ? BK.coral : BK.line),background:on ? '#fbe3da' : '#fff',fontSize:13,fontWeight:900,color:BK.muted}}>?</span>;
    if (c === '-') return <span style={{...box,border:'1.8px dashed ' + (on ? BK.coral : BK.line),background:on ? '#fbe3da' : 'transparent'}}/>;
    if (c === '.') return <span style={box}><span style={{width:7,height:7,borderRadius:4,background:on ? BK.coral : 'transparent',border:'1.5px solid ' + BK.line}}/></span>;
    const dot = (k) => <span key={k} style={{width:c === 'r' ? 8 : 11,height:c === 'r' ? 8 : 11,borderRadius:6,background:on ? '#fff' : BK.coral}}/>;
    return <span style={{...box,background:on ? BK.coral : '#fff',border:'2px solid ' + (on ? BK.coral : BK.ink)}}>{c === 'r' ? [dot(0), dot(1)] : dot(0)}</span>; };
  return <div style={{display:'flex',justifyContent:'center',alignItems:'flex-start',gap:6,flexWrap:'wrap'}}>
    {[0, 1].map(bar => <div key={bar} style={{display:'flex',gap:5,paddingLeft:bar ? 10 : 0,borderLeft:bar ? '1.6px solid rgba(38,41,107,0.45)' : 'none'}}>
      {cells.slice(bar * half, bar * half + half).map((c, j) => { const i = bar * half + j; return <div key={i} style={{display:'flex',flexDirection:'column',alignItems:'center',gap:2,width:Z + 12}}>{cell(c, i)}<span style={{fontSize:11,fontWeight:800,color:i === lit ? BK.coral : BK.muted,whiteSpace:'nowrap',minHeight:14}}>{show ? lsBeatWord(c) : ''}</span></div>; })}
    </div>)}
  </div>;
}
// count-in (4 clicks), the call (2 bars), the echo (2 bars); a soft click on every beat keeps the pulse going
function lsEchoRun(cells) {
  const n = cells.length;
  return plRun(4 + n * 2, { bpm: LS_BPM, silentFrom: 4, extra: (ctx, tm, i, spb) => { if (i < 4) return; metroClick(ctx, tm, false, 0.09); const b = i - 4; if (b >= n) return;
    const c = cells[b]; if (c === 'w') lsNote(ctx, tm, 32, lsHold(cells, b) * spb * 0.85, 0.22); else if (c === 'r') { lsNote(ctx, tm, 32, spb * 0.42, 0.22); lsNote(ctx, tm + spb / 2, 32, spb * 0.42, 0.22); } } });
}
function LsEchoPad({ onResult, fixed }) {
  const T = usePlTimers();
  const [pi, setPi] = useState(0), [phase, setPhase] = useState('ready'), [lit, setLit] = useState(-1), [res, setRes] = useState(null), [show, setShow] = useState(false);
  const run = useRef(null), taps = useRef([]);
  const cells = fixed || LS_ECHO[pi], n = cells.length;
  function start() {
    T.clear(); setRes(null); taps.current = [];
    const r = lsEchoRun(cells); if (!r) return; run.current = r;
    r.at.forEach((a, i) => T.at(r, a, () => { setLit(i < 4 ? -1 : (i - 4) % n); setPhase(i < 4 ? 'count' : i < 4 + n ? 'call' : 'echo'); }));
    T.at(r, r.at[4 + 2 * n - 1] + r.spb * 0.9, () => {
      setLit(-1); setPhase('done'); setShow(true);
      const want = lsOnsets(cells).map(s => r.at[4 + n] + s * r.spb), m = plMatch(want, taps.current.filter(tp => tp > r.at[4 + n] - PL_TOL));
      const out = { hits: m.hits, total: m.total, extra: m.extra, ok: m.hits === m.total && m.extra <= 1 };
      setRes(out); if (onResult) onResult(out);
    });
    setPhase('count');
  }
  const tap = React.useCallback(() => { const r = run.current; if (r && phase === 'echo') taps.current.push(r.now()); }, [phase]);
  return (
    <div className="try-box" style={actBox} data-ls="echo">
      <div style={actTitle}>{t('Echo the rhythm', '리듬 메아리')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>클릭 4번 뒤에 두 마디를 들어요. 바로 이어서, 박을 멈추지 않고 <b>똑같이</b> 패드를 쳐요.</> : <>After 4 clicks, listen to two bars. Straight after, without stopping the beat, tap them back <b>the same</b>.</>}</div>
      {!fixed && <div style={{display:'flex',gap:6,justifyContent:'center',flexWrap:'wrap',marginBottom:8}}>{LS_ECHO.map((_, i) => <button key={i} className={'chip' + (i === pi ? ' active' : '')} style={{minHeight:40,padding:'6px 12px'}} onClick={() => { T.clear(); stopClicks(); setPi(i); setRes(null); setShow(false); setPhase('ready'); setLit(-1); }}>{t('Rhythm ' + (i + 1), '리듬 ' + (i + 1))}</button>)}</div>}
      <LsCells cells={cells} lit={phase === 'call' || phase === 'echo' ? lit : -1} show={show}/>
      {lsMsg(phase === 'count' ? t('Get ready…', '준비…') : phase === 'call' ? t('Listen…', '들어요…') : phase === 'echo' ? t('Your turn: tap it back!', '이제 내 차례: 똑같이 쳐요!') : '', phase === 'echo' ? BK.coral : undefined)}
      <PlPad on={phase === 'call' || phase === 'echo' || phase === 'count'} onTap={tap}/>
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={lsBtn} onClick={start}>{phase === 'done' ? t('▶ Again', '▶ 다시') : t('▶ Start', '▶ 시작')}</button>
        {!show && <button className="ghost-btn" style={lsBtn} onClick={() => setShow(true)}>{t('Show the rhythm', '리듬 보기')}</button>}
      </div>
      {res && lsMsg(t('Echoed on time: ' + res.hits + ' of ' + res.total + (res.extra ? ', ' + res.extra + ' extra tap' + (res.extra > 1 ? 's' : '') : ''), '제때 따라 친 것: ' + res.total + '개 중 ' + res.hits + '개' + (res.extra ? ', 더 친 것 ' + res.extra + '개' : '')) + (res.ok ? ' ✓' : ''), res.ok ? BK.green : BK.coral)}
      {plHint()}
    </div>
  );
}

// ── step 3: up or down: higher is up towards the bird, lower is down towards the turtle ──
function lsPair(prev) {
  let a, b, g = 0;
  do { a = 24 + Math.floor(Math.random() * 11); b = a + pick([1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 0]); } while ((b < 21 || b > 38 || (prev && prev.a === a && prev.b === b)) && g++ < 30);
  return { a, b, answer: b > a ? 'up' : b < a ? 'down' : 'same' };
}
const LS_DIR = { up: () => t('Up', '위로'), down: () => t('Down', '아래로'), same: () => t('The same', '같아요') };
const lsDirIcon = (c, s = 30) => (c === 'up' ? birdIcon(s) : c === 'down' ? turtleIcon(s) : <span style={{fontSize:s * 0.8,fontWeight:900,lineHeight:1,color:BK.ink}}>=</span>);
// the keys from low to high, two keys lit (the first coral, the second navy), the turtle at the low end and the bird at the high end
function LsTwoKeys({ a, b, show = true, k = 1.1, ic = 34, nums = true }) {   // the first note pale, the second coral; 1 and 2 on the keys
  const lit = {}; if (a != null) lit[a] = 'pale'; if (show && b != null) lit[b] = 'cor';
  const r = hpKeysRaw('C', { hands: 'R', span: [21, 38], fingers: false, letters: false, names: false, mc: false, pale: false, lit, W: 14, H: 46 });
  const kx = (d) => r.x0 + (d - r.d0 + 0.5) * r.W, num = (d, n, col) => <text key={n} x={kx(d)} y={r.top + r.H - 7} textAnchor="middle" fontSize="10" fontWeight="900" fill={col} style={{fontFamily:'Inter, sans-serif'}}>{n}</text>;
  return <div style={{display:'flex',alignItems:'center',gap:6,justifyContent:'center'}}>{turtleIcon(ic)}<svg viewBox={r.vb.join(' ')} style={{flex:'1 1 auto',minWidth:0,maxWidth:r.vb[2] * k,display:'block'}} aria-hidden="true"><g dangerouslySetInnerHTML={{__html: r.svg}}/>
    {nums && a != null && (a !== b || !show) && num(a, '1', BK.ink)}{nums && show && b != null && num(b, a === b ? '1 2' : '2', '#fff')}</svg>{birdIcon(ic)}</div>;
}
function LsUpDownPad({ onResult }) {
  const [q, setQ] = useState(null), [ans, setAns] = useState(null), [run, setRun] = useState(0), stop = useRef(null);
  useEffect(() => () => stop.current && stop.current(), []);
  const hear = (x) => { stop.current && stop.current(); stop.current = lsSeq([x.a, x.b], 750); };
  const fresh = () => { const x = lsPair(q); setQ(x); setAns(null); hear(x); };
  const say = (c) => { if (!q || ans) return; setAns(c); const ok = c === q.answer; setRun(n => (ok ? n + 1 : 0)); if (onResult) onResult({ ok }); };
  return (
    <div className="try-box" style={actBox} data-ls="updown">
      <div style={actTitle}>{t('Up or down?', '위로? 아래로?')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>두 음을 들어요. 두 번째 음은 <b>위로</b>(하늘의 새 쪽) 갈까요, <b>아래로</b>(바다의 거북이 쪽) 갈까요?</> : <>Listen to two notes. Does the second go <b>up</b> (towards the bird in the sky) or <b>down</b> (towards the turtle in the sea)?</>}</div>
      <LsTwoKeys a={q && ans ? q.a : null} b={q && ans ? q.b : null}/>
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',margin:'10px 0'}}>
        <button className="ghost-btn" style={lsBtn} onClick={fresh}>{q ? t('▶ New pair', '▶ 새 두 음') : t('▶ Play two notes', '▶ 두 음 듣기')}</button>
        {q && <button className="ghost-btn" style={lsBtn} onClick={() => hear(q)}>{t('♪ Again', '♪ 다시 듣기')}</button>}
      </div>
      <div style={{display:'grid',gridTemplateColumns:'repeat(3,1fr)',gap:8}}>{['up', 'same', 'down'].map(c => <button key={c} disabled={!q} className={'choice-btn' + (!ans || !q ? '' : c === q.answer ? ' good' : c === ans ? ' bad' : '')} onClick={() => say(c)} style={{display:'flex',flexDirection:'column',alignItems:'center',gap:4,padding:'10px 4px'}}>{lsDirIcon(c)}<span style={{fontSize:15,fontWeight:900}}>{LS_DIR[c]()}</span></button>)}</div>
      {q && ans && lsMsg(ans === q.answer ? t('Yes: ' + LS_DIR[q.answer]().toLowerCase() + '. ' + (run > 1 ? run + ' in a row!' : ''), '맞아요: ' + LS_DIR[q.answer]() + '. ' + (run > 1 ? run + '번 연속!' : '')) : t('Listen again: it went ' + LS_DIR[q.answer]().toLowerCase() + '. The keys show where.', '다시 들어 봐요: ' + LS_DIR[q.answer]() + '예요. 건반이 어디인지 보여 줘요.'), ans === q.answer ? BK.green : BK.coral)}
    </div>
  );
}

// ── step 4: find your note: hear it, sing it on "la", then find it in C position ──
function LsKeys({ lit = {}, onTap, letters = false, label }) {
  const r = hpKeysRaw('C', { hands: 'R', fingers: false, letters, names: false, mc: true, lit });
  return <svg viewBox={r.vb.join(' ')} style={{width:'100%',maxWidth:r.vb[2] * 1.6,display:'block',margin:'0 auto'}} role="group" aria-label={label || t('C position, right hand: tap a key', 'C 자리 오른손: 건반을 눌러요')}>
    <g dangerouslySetInnerHTML={{__html: r.svg}}/>
    {onTap && Array.from({ length: r.nw }, (_, i) => r.d0 + i).map(d => <rect key={d} data-key={d} x={r.x0 + (d - r.d0) * r.W} y={r.top} width={r.W} height={r.H} fill="transparent" style={{cursor:'pointer'}} role="button" aria-label={hpLet(d)} onClick={() => onTap(d)}/>)}
  </svg>;
}
function LsFindPad({ onResult }) {
  const [d, setD] = useState(null), [tries, setTries] = useState([]), [found, setFound] = useState(false);
  const fresh = () => { let x, g = 0; do { x = 28 + Math.floor(Math.random() * 5); } while (x === d && g++ < 10); setD(x); setTries([]); setFound(false); setTimeout(() => lsPlay(x, 1.1), 120); };
  const tap = (k) => { if (d == null || found) { lsPlay(k, 0.6); return; } lsPlay(k, 0.7);
    if (k === d) { setFound(true); if (onResult) onResult({ ok: tries.length === 0, tries: tries.length }); } else setTries(ts => [...ts, k]); };
  const last = tries[tries.length - 1], lit = {}; if (found) lit[d] = 'cor';
  return (
    <div className="try-box" style={actBox} data-ls="find">
      <div style={actTitle}>{t('Find your note', '내 음 찾기')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>음 하나를 들어요. <b>"라"로 따라 불러요</b>. 그다음 C 자리에서 찾아요: 쳐 보고, 들어 보고, 더 높을까요 낮을까요?</> : <>Hear one note. <b>Sing it on "la"</b>. Then find it in C position: play, listen, higher or lower?</>}</div>
      <LsKeys lit={lit} onTap={tap} letters={found}/>
      {lsMsg(d == null ? t('Tap ▶ to hear a note.', '▶을 누르면 음이 나와요.') : found ? t('That\'s it: ' + hpLet(d) + (tries.length ? '.' : ', first time!') + ' Sing it again with the key.', '찾았어요: ' + hpLet(d) + (tries.length ? '.' : ', 한 번에!') + ' 건반과 함께 다시 불러요.')
        : last == null ? t('Sing it, then find it.', '불러 보고, 찾아요.') : d > last ? t('Higher: towards the bird.', '더 높아요: 새 쪽으로.') : t('Lower: towards the turtle.', '더 낮아요: 거북이 쪽으로.'), found ? BK.green : last != null ? BK.coral : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={lsBtn} onClick={fresh}>{d == null ? t('▶ Play a note', '▶ 음 듣기') : t('▶ New note', '▶ 새 음')}</button>
        {d != null && <button className="ghost-btn" style={lsBtn} onClick={() => lsPlay(d, 1.1)}>{t('♪ Again', '♪ 다시 듣기')}</button>}
      </div>
    </div>
  );
}

// ── step 5: sing it back: three notes, then five; then play them in C position, right hand ──
const LS_SING = { 3: ['1 2 3', '3 2 1', '1 2 1', '3 4 5', '5 4 3', '2 3 2'], 5: ['1 2 3 2 1', '3 4 5 4 3', '5 4 3 2 1', '1 2 3 4 5', '3 2 1 2 3', '5 4 3 4 5'] };
const lsFingers = (s) => s.split(' ').map(Number);
function LsSingRow({ fs, got = 0, lit = -1, show = false, size = 32 }) {
  return <div style={{display:'flex',gap:6,justifyContent:'center'}}>{fs.map((f, i) => { const on = i === lit, done = i < got;
    return <span key={i} style={{width:size,height:size,borderRadius:size / 2,boxSizing:'border-box',display:'inline-flex',alignItems:'center',justifyContent:'center',fontSize:15,fontWeight:900,
      background:on ? BK.coral : done ? BK.ink : '#fff',border:'2px solid ' + (on ? BK.coral : BK.ink),color:on || done ? '#fff' : BK.ink,transition:'background .1s'}}>{done || show ? f : ''}</span>; })}</div>;
}
function LsSingPad({ onResult, len0 = 3, fixed }) {
  const [len, setLen] = useState(len0), [ti, setTi] = useState(0), [got, setGot] = useState(0), [miss, setMiss] = useState(0), [lit, setLit] = useState(-1), [show, setShow] = useState(false), [heard, setHeard] = useState(false), [wrong, setWrong] = useState(null);
  const stop = useRef(null); useEffect(() => () => stop.current && stop.current(), []);
  const fs = lsFingers(fixed || LS_SING[len][ti]), ds = fs.map(f => hpFingerD('C', 'R', f)), done = got >= fs.length;
  const listen = () => { stop.current && stop.current(); setHeard(true); stop.current = lsSeq(ds, 600, setLit); };
  const reset = (l, i) => { stop.current && stop.current(); setLen(l); setTi(i); setGot(0); setMiss(0); setShow(false); setHeard(false); setWrong(null); setLit(-1); };
  const tap = (d) => { lsPlay(d, 0.6); if (done || !heard) return;
    if (d === ds[got]) { const g = got + 1; setGot(g); setWrong(null); if (g >= fs.length && onResult) onResult({ ok: miss === 0, miss }); } else { setMiss(m => m + 1); setWrong(d); } };
  const lit2 = {}; if (got > 0 && !done) lit2[ds[got - 1]] = 'cor';
  return (
    <div className="try-box" style={actBox} data-ls="sing">
      <div style={actTitle}>{t('Sing it back', '따라 부르기')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>짧은 선율을 들어요. <b>"라"로 따라 불러요</b>. 그다음 C 자리 오른손으로 쳐요. 엄지 1번은 가운데 도.</> : <>Listen to a short tune. <b>Sing it back on "la"</b>. Then play it in C position, right hand: thumb 1 on middle C.</>}</div>
      {!fixed && <div style={{display:'flex',gap:6,justifyContent:'center',flexWrap:'wrap',marginBottom:8}}>
        {[3, 5].map(l => <button key={l} className={'chip' + (l === len ? ' active' : '')} style={{minHeight:40,padding:'6px 12px'}} onClick={() => reset(l, 0)}>{t(l + ' notes', l + '음')}</button>)}
        <button className="chip" style={{minHeight:40,padding:'6px 12px'}} onClick={() => reset(len, (ti + 1) % LS_SING[len].length)}>{t('Another tune', '다른 선율')}</button>
      </div>}
      <LsSingRow fs={fs} got={got} lit={lit} show={show || done}/>
      <div style={{margin:'10px 0 4px'}}><LsKeys lit={lit2} onTap={tap} letters={done}/></div>
      {lsMsg(!heard ? t('Tap ▶ Listen first.', '먼저 ▶ 듣기를 눌러요.') : done ? t('Listen, sing, play ✓' + (miss ? '' : ' First time!'), '듣고, 부르고, 치기 ✓' + (miss ? '' : ' 한 번에!')) : wrong != null ? t('Not that one: sing it again, then try.', '그 건반이 아니에요: 다시 불러 보고 쳐요.') : t('Sing it, then play note ' + (got + 1) + '.', '불러 보고, ' + (got + 1) + '번째 음을 쳐요.'), done ? BK.green : wrong != null ? BK.coral : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={lsBtn} onClick={listen}>{t('▶ Listen', '▶ 듣기')}</button>
        {!done && <button className="ghost-btn" style={lsBtn} onClick={() => setShow(true)}>{t('Show the fingers', '손가락 번호 보기')}</button>}
      </div>
    </div>
  );
}

// ── the pictures on paper ──
const lsRawPic = (svg, vb) => ({ shapes: [{ k: 'raw', svg }], vb });
const lsCircleSvg = (x, y, r, kind, label) => '<circle cx="' + x + '" cy="' + y + '" r="' + r + '" fill="' + (kind === 'play' ? '#26296b' : '#fff') + '" stroke="#26296b" stroke-width="2"' + (kind === 'silent' ? ' stroke-dasharray="4 3"' : '') + '/>' + (label ? '<text x="' + x + '" y="' + (y + r * 0.4) + '" text-anchor="middle" font-family="Inter, sans-serif" font-size="' + (r * 1.05) + '" font-weight="900" fill="' + (kind === 'play' ? '#fff' : '#26296b') + '">' + label + '</text>' : '');
const lsPicBeat = () => lsRawPic([0, 1, 2, 3].map(i => lsCircleSvg(10 + i * 20, 22, 8, i === 2 ? 'silent' : 'play')).join(''), [0, 0, 80, 44]);
const lsPicEcho = () => lsRawPic([0, 1, 2].map(i => lsCircleSvg(10 + i * 18, 12, 6.5, 'play')).join('') + [0, 1, 2].map(i => lsCircleSvg(30 + i * 18, 32, 6.5, 'beat')).join('') + '<path d="M60 12 Q74 16 66 28" fill="none" stroke="#e4572e" stroke-width="2"/><path d="M62 24 L66 29 L70 24" fill="none" stroke="#e4572e" stroke-width="2"/>', [0, 0, 80, 44]);
const lsPicUpDown = () => ({ shapes: [...fsTurtle(16, 34, 0.55), ...fsBird(62, 12, 0.85), { k: 'raw', svg: '<path d="M24 24 L52 16" fill="none" stroke="#e4572e" stroke-width="2.2"/><path d="M46 13 L53 16 L47 21" fill="none" stroke="#e4572e" stroke-width="2.2"/>' }], vb: [0, 0, 80, 44] });
const lsPicFind = () => { const r = hpKeysRaw('C', { hands: 'R', W: 9, H: 30, names: false, mc: false, letters: false, fingers: false, lit: { 30: 'cor' } }); return { shapes: [{ k: 'raw', svg: r.svg }], vb: r.vb }; };
const lsPicSing = () => lsRawPic([1, 2, 3].map((f, i) => lsCircleSvg(16 + i * 24, 22, 9, 'beat', String(f))).join(''), [0, 0, 80, 44]);

function lsLbPages(scr = false) {
  const ch = 'listen-sing';
  const checks5 = [[lsPicBeat(), t('I keep the beat, and keep going when the music stops', '박을 지키고, 음악이 멈춰도 계속 가요')], [lsPicEcho(), t('I echo a two-bar rhythm, straight after it', '두 마디 리듬을 바로 이어서 따라 쳐요')],
    [lsPicUpDown(), t('I hear whether a tune goes up or down', '선율이 위로 가는지 아래로 가는지 들어요')], [lsPicFind(), t('I sing a note, then find it on the keys', '음 하나를 부르고, 건반에서 찾아요')], [lsPicSing(), t('I sing back three notes, then five, and play them', '세 음, 그다음 다섯 음을 따라 부르고 쳐요')]];
  const pen = (x) => <PenArt shapes={x.shapes} vb={x.vb} style={{width:90}}/>;
  const toc = [[t('Keep the beat', '박 지키기'), 2], [t('Echo the rhythm', '리듬 메아리'), 3], [t('Up or down', '위로? 아래로?'), 4], [t('Find your note', '내 음 찾기'), 5], [t('Sing it back', '따라 부르기'), 6], [t('My five checks', '나의 다섯 가지 확인'), 7]];
  const beatStill = <LbPic h={120}><div style={{width:'100%'}}><PlCircles n={16} r={scr ? 12 : 16} gap={scr ? 30 : 40} kind={(i) => (lsQuiet(i) ? 'silent' : 'play')} label={(i) => String(i % 4 + 1)}/>
    <div style={{display:'grid',gridTemplateColumns:'2fr 1fr 1fr',textAlign:'center',fontSize:12.5,fontWeight:900,color:BK.muted,marginTop:4}}><span>{t('the music', '음악')}</span><span style={{color:BK.coral}}>{t('quiet: keep going', '조용히: 계속')}</span><span>{t('the music again', '다시 음악')}</span></div></div></LbPic>;
  return [
    // 1. opener
    <LbPage key="1" no={1} chId={ch} teacher={<>{t('Ears first. Every step here is listening, then singing or tapping, then the keys: the app plays and scores the taps; whether a child sang in tune is your ear. Sing on "la" at a comfortable pitch: if a voice sits higher than C position, let it sing there. No staff yet: the staff comes in chapter ' + bkChapterNo('staff') + '.', '귀가 먼저예요. 모든 단계가 듣기, 그다음 부르거나 치기, 그다음 건반이에요. 앱은 소리를 들려주고 탭을 채점해요. 음정에 맞게 불렀는지는 선생님의 귀가 판단해요. 편한 높이에서 "라"로 불러요. 목소리가 C 자리보다 높은 곳에 있으면 거기서 불러도 돼요. 오선은 아직이에요: ' + bkChapterNo('staff') + '장에서 배워요.')}</>} qr={bkLink('drill=' + ch + '&lock=1')}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:50,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{t('Listen and Sing', '듣고 노래하기')}</div>
      </div></LbOnly>
      <LbPic h={170}><div style={{width:'100%',maxWidth:620,margin:'0 auto'}}><LsTwoKeys a={28} b={32} k={2.2} ic={48} nums={false}/>
        <div style={{display:'flex',justifyContent:'space-between',fontSize:13,fontWeight:900,color:BK.muted,marginTop:6,padding:'0 4px'}}><span>{t('← lower: down to the turtle', '← 낮게: 거북이 쪽으로')}</span><span>{t('higher: up to the bird →', '높게: 새 쪽으로 →')}</span></div></div></LbPic>
      <LbSay size={18}>{t('Ears first. Listen, sing it back, then find it on the keys.', '귀가 먼저예요. 듣고, 따라 부르고, 그다음 건반에서 찾아요.')}</LbSay>
      <div className="lb-toc" style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>
        <LbOnly print><div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('In this chapter', '이 챕터에서는')}</div>
          {toc.map(([n, p]) => <div key={p} className="lb-toc-row" style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:14.5,padding:'5px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkGoal(15)}{n}</span><span style={{color:BK.muted,fontWeight:800}}>{p}</span></div>)}
        </div></LbOnly>
        <div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 챕터를 마치면')}</div>
          {[t('keep a steady beat, even when the music stops', '음악이 멈춰도 꾸준한 박을 지킬 수 있어요'), t('echo a two-bar rhythm', '두 마디 리듬을 따라 칠 수 있어요'), t('hear whether a tune goes up or down', '선율이 위로 가는지 아래로 가는지 들을 수 있어요'), t('sing a note and find it on the keys', '음 하나를 부르고 건반에서 찾을 수 있어요'), t('sing back a short tune, then play it', '짧은 선율을 따라 부르고 칠 수 있어요')].map(x => <div key={x} style={{display:'flex',gap:9,alignItems:'flex-start',fontSize:14.5,padding:'5px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}><span style={{flex:'0 0 auto',marginTop:3}}>{bkGoal(15)}</span><span>{x}</span></div>)}
        </div>
      </div>
      <LbOnly print><LbDrillStrip id={ch}/></LbOnly>
    </LbPage>,
    // 2. keep the beat
    <LbPage key="2" no={2} chId={ch} kicker={t('Step 1', '1단계')} title={t('Keep the beat', '박 지키기')}
      teacher={<>{t('Play any tune the child knows, steady, and stop for a bar or two in the middle: the clapping should not stop or slow down. Then come back in together. Walking the beat round the room works as well as clapping.', '아이가 아는 곡을 일정하게 치다가 중간에 한두 마디 멈춰 주세요. 박수가 멈추거나 느려지면 안 돼요. 그다음 함께 다시 들어가요. 박수 대신 방을 걸으며 박을 걸어도 좋아요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=1')}>
      <LbLive still={beatStill} live={<LsBeatPad/>}/>
      <LbSay>{LANG === 'ko' ? <>음악 밑에는 언제나 <b>박</b>이 흘러요. 음악이 멈춰도 <b>박은 계속 가요</b>: 속으로 세면서 계속 쳐요. 음악이 돌아올 때 같이 있어야 해요.</> : <>Under the music there is always a <b>beat</b>. When the music stops, <b>the beat goes on</b>: keep tapping, counting inside. When the music comes back, be right there with it.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>선생님이 곡을 쳐요. 박마다 손뼉을 쳐요.</>,
        <>선생님이 중간에 멈춰요. 손뼉은 멈추지 않아요: 1 2 3 4, 속으로 세면서.</>,
        <>선생님이 다시 들어와요. 같이 있었나요? 이번엔 걸으면서 해 봐요.</>,
      ] : [
        <>Your teacher plays a tune. Clap every beat.</>,
        <>Your teacher stops in the middle. Your clapping doesn't: 1 2 3 4, counting inside.</>,
        <>Your teacher comes back in. Were you still together? Now try it walking.</>,
      ]}/>
      <LbRemember>{t('The beat keeps going, even when the music stops.', '음악이 멈춰도 박은 계속 가요.')}</LbRemember>
    </LbPage>,
    // 3. echo the rhythm
    <LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={t('Echo the rhythm', '리듬 메아리')}
      teacher={<>{t('Clap two bars; the child claps them back straight after, with no gap in the beat (call and echo). Use chapter ' + bkChapterNo('pulse') + '\'s words: walk is one sound on a beat, run-ning two. Start with walks and holds; add run-ning when the walks are easy.', '두 마디를 손뼉으로 치면, 아이가 박을 끊지 않고 바로 이어서 똑같이 쳐요(부르고, 메아리). ' + bkChapterNo('pulse') + '장의 낱말을 써요: 타는 한 박에 한 소리, 티-티는 두 소리. 타와 길게 누르는 박으로 시작하고, 쉬워지면 티-티를 더해요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=3')}>
      <LbLive still={<LbPic h={150}><div style={{display:'flex',flexDirection:'column',gap:10,width:'100%'}}>
        <div style={{display:'flex',alignItems:'center',gap:8}}><span style={{width:62,fontSize:12.5,fontWeight:900,color:BK.muted}}>{t('call', '부르기')}</span><div style={{flex:1,minWidth:0}}><LsCells cells={LS_ECHO[1]} size={scr ? 30 : 38}/></div></div>
        <div style={{display:'flex',alignItems:'center',gap:8}}><span style={{width:62,fontSize:12.5,fontWeight:900,color:BK.coral}}>{t('echo', '메아리')}</span><div style={{flex:1,minWidth:0}}><LsCells cells={LS_ECHO[1]} size={scr ? 30 : 38}/></div></div>
      </div></LbPic>} live={<LsEchoPad/>}/>
      <LbSay>{LANG === 'ko' ? <>두 마디를 <b>끝까지 들어요</b>. 그다음 <b>바로 이어서</b>, 박을 멈추지 않고 똑같이 쳐요. <b>타</b>는 한 박에 한 소리, <b>티-티</b>는 두 소리, 점선 동그라미는 길게.</> : <><b>Listen to the end</b> of the two bars. Then, <b>straight after</b> and without stopping the beat, clap them back the same. <b>Walk</b> is one sound on a beat, <b>run-ning</b> two, a dashed circle holds on.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>선생님이 두 마디를 손뼉으로 쳐요. 끝까지 듣고, 바로 이어서 똑같이 쳐요.</>,
        <>이번엔 소리 내어: "타 타 티-티 타"처럼 낱말로 말하며 쳐요.</>,
        <>피아노로: 가운데 도 하나로 같은 리듬을 쳐요.</>,
      ] : [
        <>Your teacher claps two bars. Listen to the end, then clap them straight back.</>,
        <>Now out loud: say the words as you clap, like "walk walk run-ning walk".</>,
        <>At the piano: play the same rhythm on middle C.</>,
      ]}/>
      <LbRemember>{t('Listen to the end, then echo it on the beat.', '끝까지 듣고, 박에 맞춰 메아리.')}</LbRemember>
    </LbPage>,
    // 4. up or down
    <LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title={t('Up or down', '위로? 아래로?')}
      teacher={<>{t('Play two notes, wide apart first, then closer. The child shows the answer with the body: arm up like the bird, down like the turtle. Watch for "up" meaning "louder": play the second note soft and higher, or loud and lower.', '두 음을 처음엔 멀리, 그다음 가깝게 쳐 주세요. 아이는 몸으로 답해요: 새처럼 팔을 위로, 거북이처럼 아래로. "위로"를 "더 크게"로 헷갈리는지 봐 주세요: 두 번째 음을 여리고 높게, 또는 세고 낮게 쳐 보세요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=1')}>
      <LbLive still={<LbPic h={150}><div style={{width:'100%',maxWidth:620,margin:'0 auto'}}><LsTwoKeys a={28} b={31} k={2.2} ic={48}/></div></LbPic>} live={<LsUpDownPad/>}/>
      <LbSay>{LANG === 'ko' ? <>두 번째 음이 더 높으면 <b>위로</b>: 오른쪽, 하늘의 <b>새</b> 쪽. 더 낮으면 <b>아래로</b>: 왼쪽, 바다의 <b>거북이</b> 쪽. 높고 낮음은 크고 작음과 달라요.</> : <>If the second note is higher, it goes <b>up</b>: to the right, towards the <b>bird</b> in the sky. Lower goes <b>down</b>: to the left, towards the <b>turtle</b> in the sea. High and low are not loud and soft.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>선생님이 두 음을 쳐요. 눈을 감고 들어요. 위로면 팔을 위로, 아래로면 아래로.</>,
        <>세 음: 위로-위로, 아래로-아래로, 위로-아래로? 팔로 모양을 그려요.</>,
        <>바꿔요: 내가 두 음을 치고, 선생님이 맞혀요.</>,
      ] : [
        <>Your teacher plays two notes. Close your eyes and listen: arm up for up, down for down.</>,
        <>Three notes: up-up, down-down, or up-down? Draw the shape with your arm.</>,
        <>Swap: you play two notes, your teacher guesses.</>,
      ]}/>
      <LbRemember>{t('Higher: up to the bird. Lower: down to the turtle.', '높게: 새 쪽으로. 낮게: 거북이 쪽으로.')}</LbRemember>
    </LbPage>,
    // 5. find your note
    <LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title={t('Find your note', '내 음 찾기')}
      teacher={<>{t('Sing first, then find it: the voice holds the note while the hand looks for it. Only C position (C to G) for now. If the child plays a wrong key, ask "higher or lower?" before they try again.', '먼저 부르고, 그다음 찾아요: 손이 찾는 동안 목소리가 그 음을 붙잡고 있어요. 지금은 C 자리(C부터 G)만 써요. 틀린 건반을 치면 다시 치기 전에 "더 높아? 더 낮아?"를 물어봐 주세요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=6')}>
      <LbLive still={<LbPic h={150}><div style={{width:'100%',maxWidth:420,margin:'0 auto',textAlign:'center'}}>
        <div style={{fontFamily:LB_SERIF,fontSize:22,fontWeight:800,fontStyle:'italic',color:BK.coral,marginBottom:4}}>“la”</div>
        <HpKeys pos="C" hands="R" fingers={false} names={false} lit={{ 30: 'cor' }} k={2}/></div></LbPic>} live={<LsFindPad/>}/>
      <LbSay>{LANG === 'ko' ? <>음 하나를 들어요. <b>"라"로 따라 불러요</b>. 그다음 C 자리에서 찾아요: 쳐 보고, 들어 보고, <b>더 높을까요, 더 낮을까요?</b></> : <>Hear one note. <b>Sing it on "la"</b>. Then find it in C position: play, listen, <b>higher or lower?</b></>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>선생님이 C부터 G 사이의 음 하나를 쳐요. "라"로 불러요.</>,
        <>계속 부르면서 C 자리에서 찾아요. 틀리면: 더 높을까, 더 낮을까?</>,
        <>찾으면 그 건반을 치면서 함께 불러요. 음이름도 말해요.</>,
      ] : [
        <>Your teacher plays one note from C to G. Sing it on "la".</>,
        <>Keep singing while you look for it in C position. A wrong key: higher or lower?</>,
        <>Found it? Play it and sing with it. Say its letter name too.</>,
      ]}/>
      <LbRemember>{t('Sing it, then find it: higher or lower?', '부르고, 찾아요: 더 높아? 더 낮아?')}</LbRemember>
    </LbPage>,
    // 6. sing it back
    <LbPage key="6" no={6} chId={ch} kicker={t('Step 5', '5단계')} title={t('Sing it back', '따라 부르기')}
      teacher={<>{t('Three notes first, by step, in C position; then five. Sing back before playing, every time: the ear leads and the hand follows. If the playing goes wrong, sing it again rather than hunting on the keys.', '처음엔 C 자리에서 한 걸음씩 움직이는 세 음, 그다음 다섯 음. 치기 전에 언제나 먼저 따라 불러요: 귀가 앞서고 손이 따라가요. 치다가 틀리면 건반을 더듬지 말고 다시 불러 보게 해 주세요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=4')}>
      <LbLive still={<LbPic h={160}><div style={{display:'flex',flexDirection:'column',gap:12,width:'100%',maxWidth:420,margin:'0 auto'}}>
        <LsSingRow fs={[1, 2, 3]} show size={scr ? 32 : 40}/><HpKeys pos="C" hands="R" fingers={false} names={false} lit={{ 28: 'cor', 29: 'cor', 30: 'cor' }} k={2}/></div></LbPic>} live={<LsSingPad/>}/>
      <LbSay>{LANG === 'ko' ? <>짧은 선율을 들어요. <b>"라"로 따라 불러요</b>. 그다음 C 자리 오른손으로 쳐요. <b>듣고, 부르고, 치기.</b> 세 음부터, 그다음 다섯 음.</> : <>Listen to a short tune. <b>Sing it back on "la"</b>. Then play it in C position, right hand. <b>Listen, sing, play.</b> Three notes first, then five.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>선생님이 세 음을 쳐요. "라"로 따라 불러요.</>,
        <>C 자리 오른손으로 쳐요. 엄지 1번은 가운데 도.</>,
        <>이제 다섯 음. 틀리면 다시 불러 보고 쳐요.</>,
      ] : [
        <>Your teacher plays three notes. Sing them back on "la".</>,
        <>Play them in C position, right hand: thumb 1 on middle C.</>,
        <>Now five notes. If it goes wrong, sing it again, then play.</>,
      ]}/>
      <LbRemember>{t('Listen, sing, play.', '듣고, 부르고, 치기.')}</LbRemember>
    </LbPage>,
    // 7. five checks
    <LbPage key="7" no={7} chId={ch} kicker={t('Check-up', '점검')} title={t('My five checks', '나의 다섯 가지 확인')}
      teacher={<>{t('Each one shown with you, at the piano or away from it: you play, the child answers by clapping, singing or playing. You only correct.', '하나씩 선생님과 함께 보여 줘요. 피아노 앞에서든 아니든: 선생님이 치고, 아이는 손뼉, 노래, 연주로 답해요. 선생님은 고쳐 주기만 해요.')}</>}>
      <LbSay>{t('At the piano, tick each one: not yet, nearly, or got it!', '피아노 앞에서 하나씩 표시해요: 아직, 거의, 됐어요!')}</LbSay>
      <LbLive still={<LbStageRows big rows={checks5.map(([a, txt]) => [pen(a), txt])}/>} live={<FiveChecks376 rows={checks5} storeKey="pb_ls_five"/>}/>
    </LbPage>,
  ];
}
function ListenSingLessonBook() { return <>{lsLbPages(false)}</>; }
function LsLearn({ onStart }) {
  const pages = lsLbPages(true), opener = pages[0];
  return (
    <Lesson id="listen-sing" title={t('Listen and sing', '듣고 노래하기')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="listen-sing"><div className="lb-screen lb-open" style={{display:'flex',flexDirection:'column',gap:12,margin:'0 0 8px'}}>{lbWordsFirst(opener.props.children)}</div></BkChapterCtx.Provider></LbScreenCtx.Provider>}>
      {pages.slice(1).map((pg, i) => <Step key={i} title={pg.props.title}><LbScreenPage page={pg}/></Step>)}
    </Lesson>
  );
}

// ── the drill: every question is heard (it plays by itself, and ▶ plays it again) ──
const LS_LEVELS = [
  { n: 1, label: 'Up or down?', kind: 'updown', time: 10 },
  { n: 2, label: 'Low, middle or high?', kind: 'hml', time: 10 },
  { n: 3, label: 'Same or different rhythm?', kind: 'rhythm', time: 14 },
  { n: 4, label: 'Same or different tune?', kind: 'tune', time: 14 },
  { n: 5, label: 'Which shape?', kind: 'shape', time: 12 },
  { n: 6, label: 'Find the note', kind: 'find', time: 14 },
];
Object.assign(LEVEL_KO, { 'Up or down?': '위로? 아래로?', 'Low, middle or high?': '낮은? 가운데? 높은?', 'Same or different rhythm?': '같은 리듬? 다른 리듬?', 'Same or different tune?': '같은 선율? 다른 선율?', 'Which shape?': '어떤 모양?', 'Find the note': '음 찾기' });
const LS_R1 = ['w w w w', 'w w r w', 'r r w w', 'w - w w', 'w w w -', 'r w r w', 'w r w r', 'r r r w', 'w - w -', 'r w w -'].map(s => s.split(' '));
const LS_T4 = ['1 2 3 1', '3 2 1 2', '1 3 5 3', '5 4 3 2', '1 2 3 4', '3 3 2 1', '5 3 4 2', '1 1 2 3', '2 3 4 3'].map(lsFingers);
const LS_REG = { low: [14, 18], middle: [27, 29], high: [41, 45] };
const LS_SHAPES = ['uu', 'dd', 'ud', 'du'];
function genLsQuestion(lv, prev) {
  const uid = Math.random(), k = lv.kind;
  if (k === 'updown') { const x = lsPair(prev); return { kind: k, ...x, choices: ['up', 'same', 'down'], key: x.a + ':' + x.b, uid }; }
  if (k === 'hml') { let reg, d, g = 0; do { reg = pick(['low', 'middle', 'high']); const [a, b] = LS_REG[reg]; d = a + Math.floor(Math.random() * (b - a + 1)); } while (prev && prev.d === d && g++ < 10); return { kind: k, d, answer: reg, choices: ['low', 'middle', 'high'], key: reg + d, uid }; }
  if (k === 'rhythm') { const ai = Math.floor(Math.random() * LS_R1.length), same = Math.random() < 0.4; let bi = ai, g = 0; if (!same) do { bi = Math.floor(Math.random() * LS_R1.length); } while (bi === ai && g++ < 20);
    return { kind: k, a: LS_R1[ai], b: LS_R1[bi], answer: ai === bi ? 'same' : 'different', choices: ['same', 'different'], key: ai + ':' + bi, uid }; }
  if (k === 'tune') { const a = pick(LS_T4), same = Math.random() < 0.4, b = a.slice();
    if (!same) { const j = 1 + Math.floor(Math.random() * 3); let f, g = 0; do { f = a[j] + pick([-2, -1, 1, 2]); } while ((f < 1 || f > 5) && g++ < 20); if (f >= 1 && f <= 5) b[j] = f; }
    return { kind: k, a, b, answer: a.join() === b.join() ? 'same' : 'different', choices: ['same', 'different'], key: a.join('') + b.join(''), uid }; }
  if (k === 'shape') { let s, a, b, c, g = 0; do { s = pick(LS_SHAPES); a = 27 + Math.floor(Math.random() * 6); const st = () => pick([1, 2, 2, 3]); b = a + (s[0] === 'u' ? st() : -st()); c = b + (s[1] === 'u' ? st() : -st()); } while ((Math.min(a, b, c) < 23 || Math.max(a, b, c) > 37 || (prev && prev.answer === s && g < 3)) && g++ < 30);
    return { kind: k, ds: [a, b, c], answer: s, choices: LS_SHAPES.slice(), key: [a, b, c].join(':'), uid }; }
  let d, g = 0; do { d = 28 + Math.floor(Math.random() * 5); } while (prev && prev.answer === d && g++ < 10);
  return { kind: 'find', answer: d, key: 'f' + d, uid };
}
const LS_SAME = { same: () => t('The same', '같아요'), different: () => t('Different', '달라요') };
const LS_HML = { low: () => t('Low', '낮은'), middle: () => t('Middle', '가운데'), high: () => t('High', '높은') };
const lsShapeName = (s) => s.split('').map(c => (c === 'u' ? t('up', '위로') : t('down', '아래로'))).join(t(', then ', ', 그다음 '));
const lsShapePic = (s, w = 64) => { const ys = [0, 1, 2].reduce((a, i) => (i ? a.concat(a[i - 1] + (s[i - 1] === 'u' ? -1 : 1)) : [0]), []), mn = Math.min(...ys), mx = Math.max(...ys);
  const pts = ys.map((y, i) => [10 + i * 22, 8 + (y - mn) / Math.max(1, mx - mn) * 24]);
  return <svg viewBox="0 0 64 40" width={w} style={{display:'block',margin:'0 auto'}} aria-hidden="true"><polyline points={pts.map(p => p.join(',')).join(' ')} fill="none" stroke={BK.coral} strokeWidth="2.4" strokeLinejoin="round"/>{pts.map((p, i) => <circle key={i} cx={p[0]} cy={p[1]} r="4.6" fill={BK.ink}/>)}</svg>; };
function lsAnswerLabel(q) {
  if (q.kind === 'updown') return LS_DIR[q.answer]();
  if (q.kind === 'hml') return LS_HML[q.answer]();
  if (q.kind === 'rhythm' || q.kind === 'tune') return LS_SAME[q.answer]();
  if (q.kind === 'shape') return lsShapeName(q.answer);
  return hpLet(q.answer);
}
// a one-bar rhythm on one note (setTimeout is close enough for listening)
function lsBar(cells, at, spb, ts) { cells.forEach((c, i) => { if (c === 'w') ts.push(setTimeout(() => lsPlay(32, lsHold(cells, i) * spb * 0.85), at + i * spb * 1000)); if (c === 'r') [0, 0.5].forEach(h => ts.push(setTimeout(() => lsPlay(32, spb * 0.42), at + (i + h) * spb * 1000))); }); }
function LsQuestion({ q, given, locked, onAnswer, pixel }) {
  const ts = useRef([]), stops = useRef([]), clear = () => { ts.current.forEach(clearTimeout); ts.current = []; stops.current.forEach(f => f()); stops.current = []; };
  const [lit, setLit] = useState(-1);
  const after = (ms, fn) => ts.current.push(setTimeout(fn, ms));
  const play = () => { clear(); setLit(-1); const spb = 60 / 96;
    if (q.kind === 'updown') stops.current.push(lsSeq([q.a, q.b], 750));
    else if (q.kind === 'hml') lsPlay(q.d, 1.2);
    else if (q.kind === 'rhythm') { setLit(0); lsBar(q.a, 0, spb, ts.current); after(5 * spb * 1000, () => setLit(1)); lsBar(q.b, 5 * spb * 1000, spb, ts.current); after(9 * spb * 1000, () => setLit(-1)); }
    else if (q.kind === 'tune') { const A = q.a.map(f => hpFingerD('C', 'R', f)), B = q.b.map(f => hpFingerD('C', 'R', f)); setLit(0); stops.current.push(lsSeq(A, 480));
      after(4 * 480 + 700, () => { setLit(1); stops.current.push(lsSeq(B, 480, (j) => { if (j < 0) setLit(-1); })); }); }
    else if (q.kind === 'shape') stops.current.push(lsSeq(q.ds, 620));
    else lsPlay(q.answer, 1.1); };
  useEffect(() => { const id = setTimeout(play, 350); return () => { clearTimeout(id); clear(); }; }, [q.uid]);
  useEffect(() => () => clear(), []);
  const done = !!given, btnCls = pixel ? 'pixel-choice' : 'choice-btn';
  const cls = (c) => btnCls + (!done ? '' : c === q.answer ? ' good' : given.ans === c ? ' bad' : '');
  const pick1 = (c) => { if (locked || done) return; clear(); setLit(-1); onAnswer(c); };
  const title = { updown: t('Does the second note go up, down or stay the same?', '두 번째 음은 위로 갈까요, 아래로 갈까요, 같을까요?'), hml: t('Is this note low, in the middle, or high?', '이 음은 낮은 음, 가운데 음, 높은 음 중 어느 것일까요?'),
    rhythm: t('Two rhythms: the same, or different?', '리듬 두 개: 같을까요, 다를까요?'), tune: t('Two tunes: the same, or different?', '선율 두 개: 같을까요, 다를까요?'), shape: t('Three notes: which shape do they make?', '세 음: 어떤 모양을 만들까요?'), find: t('Sing it, then find it in C position.', '불러 보고, C 자리에서 찾아요.') }[q.kind];
  const btnPad = pixel ? '14px 4px' : '12px 4px', fs = pixel ? 10 : 16;
  let body;
  if (q.kind === 'find') {
    const lit2 = done ? { [q.answer]: 'cor' } : {};
    body = <div style={{marginBottom:6}}><LsKeys lit={lit2} letters={done} onTap={(d) => { lsPlay(d, 0.6); pick1(d); }}/></div>;
  } else {
    const cols = q.kind === 'rhythm' || q.kind === 'tune' ? 2 : q.kind === 'shape' ? 4 : 3;
    const label = (c) => q.kind === 'updown' ? <>{lsDirIcon(c, 28)}<span style={{fontSize:fs,fontWeight:900}}>{LS_DIR[c]()}</span></>
      : q.kind === 'hml' ? <>{c === 'low' ? turtleIcon(30) : c === 'high' ? birdIcon(30) : lsClara(24)}<span style={{fontSize:fs,fontWeight:900}}>{LS_HML[c]()}</span></>
      : q.kind === 'shape' ? lsShapePic(c, pixel ? 44 : 56)
      : <span style={{fontSize:fs + 1,fontWeight:900}}>{LS_SAME[c]()}</span>;
    const vis = q.kind === 'rhythm' ? <div style={{display:'flex',justifyContent:'center',gap:14,margin:'0 0 10px'}}>{[0, 1].map(j => <span key={j} style={{padding:'6px 14px',borderRadius:16,fontWeight:900,fontSize:14,border:'2px solid ' + (lit === j ? BK.coral : BK.line),background:lit === j ? '#fbe3da' : '#fff',color:BK.ink}}>{t('Rhythm ', '리듬 ') + (j + 1)}</span>)}</div>
      : q.kind === 'tune' ? <div style={{display:'flex',justifyContent:'center',gap:14,margin:'0 0 10px'}}>{[0, 1].map(j => <span key={j} style={{padding:'6px 14px',borderRadius:16,fontWeight:900,fontSize:14,border:'2px solid ' + (lit === j ? BK.coral : BK.line),background:lit === j ? '#fbe3da' : '#fff',color:BK.ink}}>{t('Tune ', '선율 ') + (j + 1)}</span>)}</div>
      : q.kind === 'updown' && done ? <div style={{margin:'0 0 10px'}}><LsTwoKeys a={q.a} b={q.b}/></div> : null;
    body = <>{vis}<div style={{display:'grid',gridTemplateColumns:'repeat(' + cols + ',minmax(0,1fr))',gap:8}}>{q.choices.map(c => <button key={c} disabled={locked} className={cls(c)} style={{padding:btnPad,display:'flex',flexDirection:'column',alignItems:'center',gap:4}} onClick={() => pick1(c)}>{label(c)}</button>)}</div></>;
  }
  const why = !done ? null : q.kind === 'updown' ? t('It went ' + LS_DIR[q.answer]().toLowerCase() + (q.answer === 'up' ? ': towards the bird.' : q.answer === 'down' ? ': towards the turtle.' : '.'), LS_DIR[q.answer]() + (q.answer === 'up' ? ': 새 쪽으로.' : q.answer === 'down' ? ': 거북이 쪽으로.' : '.'))
    : q.kind === 'hml' ? t(q.answer === 'low' ? 'Low: down with the turtle.' : q.answer === 'high' ? 'High: up with the bird.' : 'In the middle, near Clara (middle C).', q.answer === 'low' ? '낮은 음: 거북이와 함께 아래.' : q.answer === 'high' ? '높은 음: 새와 함께 위.' : '가운데, 클라라(가운데 도) 근처.')
    : q.kind === 'rhythm' ? t(q.answer === 'same' ? 'The same rhythm twice.' : 'Different: listen for where the walks and run-nings change.', q.answer === 'same' ? '같은 리듬이 두 번.' : '달라요: 타와 티-티가 어디서 바뀌는지 들어 봐요.')
    : q.kind === 'tune' ? t(q.answer === 'same' ? 'The same tune twice.' : 'Different: one note changed.', q.answer === 'same' ? '같은 선율이 두 번.' : '달라요: 한 음이 바뀌었어요.')
    : q.kind === 'shape' ? t('It went ' + lsShapeName(q.answer) + '.', lsShapeName(q.answer) + ' 갔어요.')
    : t('It was ' + hpLet(q.answer) + '. Sing it with the key.', hpLet(q.answer) + '였어요. 건반과 함께 불러요.');
  return (<div>
    <p style={pixel ? {fontSize:11.5,textAlign:'center'} : {fontSize:15,fontWeight:700,textAlign:'center',margin:'0 0 8px',color:'var(--muted)',textWrap:'balance'}}>{title}</p>
    <div style={{textAlign:'center',marginBottom:10}}><button className={pixel ? 'pixel-btn' : 'ghost-btn'} style={{minHeight:44}} onClick={play}>{t('▶ Play it again', '▶ 다시 듣기')}</button></div>
    {body}
    {why && !pixel && <div style={{marginTop:10,fontSize:13.5,color:'#4a4d86',background:'#fff',borderRadius:8,padding:'7px 10px',lineHeight:1.45}}>{why}</div>}
  </div>);
}
Object.assign(LISTEN_DRILL, { levels: LS_LEVELS, generate: genLsQuestion, check: (q, ans) => ans !== null && ans !== undefined && ans === q.answer, answerLabel: lsAnswerLabel, Question: LsQuestion, Learn: LsLearn });
