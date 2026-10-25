
// ─── Chapter: Listen, Clap, Write (Build AE, 2026-10-26; the syllabus check's 'Ears for Grade 1') ───
// The Grade 1 aural tests and the listening part of the Grade 1 theory, one step each: hum the home note at the end of an
// unfinished phrase; two or three beats in a bar (oom-pah, oom-pah-pah); clap back a passage heard twice; sing back a phrase that
// has its own rhythm (walk, run-ning, hold), then play it; write down two bars of crotchets and minims. Chapter 6's ways
// (Listen and Sing): the app plays and scores taps; whether a child sang in tune is the teacher's ear. In C and G position.
const LW_STEP = [0, 2, 4, 5, 7];
const LW_TON = { C: 0, G: 7 };   // the home note (C4, G4); the phrase in that hand position, degrees 1 to 5 on fingers 1 to 5
const LW_HOME = ['1 2 3 4 5 4 3 2', '3 4 5 3 2', '5 4 3 4 2', '1 3 2 4 3 2', '3 2 1 2 3 5', '5 3 4 2 3 2', '1 2 3 2 3 4 5', '3 3 4 5 4 3 2'].map(s => s.split(' ').map(Number));
const lwKeysOf = (pos, degs) => degs.map(g => LW_TON[pos] + LW_STEP[g - 1]);
const lwLet = (i) => ['C', 'C♯', 'D', 'E♭', 'E', 'F', 'F♯', 'G', 'G♯', 'A', 'B♭', 'B'][spPc(i)];
const lwBtn = { padding:'10px 14px', fontSize:14, minHeight:44 };
const lwMsg = (txt, col) => <div style={{textAlign:'center',fontSize:15,fontWeight:900,color:col || 'var(--navy)',minHeight:22,lineHeight:1.35,textWrap:'balance'}}>{txt}</div>;
const lwRow = (children) => <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>{children}</div>;
// a phrase of [semitone, beats] notes on the audio clock; T and setAt light each note as it sounds
function lwPlay(notes, bpm, T, setAt, from = 0) {
  let at = 0; const ev = notes.map(([k, b], j) => { const e = { at, keys: [k], len: b * 0.95 }; at += b; return e; });
  const run = spPlay(ev, bpm); if (!run || !T) return at;
  if (setAt) { ev.forEach((e, j) => T.at(run.ms(e.at), () => setAt(from + j))); T.at(run.ms(at + 0.3), () => setAt(-1)); }
  return at;
}

// ── step 1: the home note: the phrase stops before it gets home; hum home, then find it ──
function LwHomePad({ onResult, fixed }) {
  const T = useSpTimers();
  const [x, setX] = useState(fixed || { pos: 'C', i: 0 }), [heard, setHeard] = useState(false), [found, setFound] = useState(false), [tries, setTries] = useState([]), [at, setAt] = useState(-1);
  const keys = lwKeysOf(x.pos, LW_HOME[x.i]), tonic = LW_TON[x.pos];
  const play = (y) => { T.clear(); setHeard(true); lwPlay(keysOf(y).map((k, j, a) => [k, j === a.length - 1 ? 2 : 1]), 100, T, setAt); };
  const keysOf = (y) => lwKeysOf(y.pos, LW_HOME[y.i]);
  const fresh = () => { let y, g = 0; do { y = { pos: Math.random() < 0.5 ? 'C' : 'G', i: Math.floor(Math.random() * LW_HOME.length) }; } while (y.pos === x.pos && y.i === x.i && g++ < 10); setX(y); setFound(false); setTries([]); play(y); };
  const tap = (k) => { if (!heard || found) { playKey(k, 0.5); return; }
    if (spPc(k) === spPc(tonic)) { setFound(true); T.clear(); const last = keys[keys.length - 1]; spPlay([{ at: 0, keys: [last], len: 0.9 }, { at: 1, keys: [k], len: 2 }], 90); if (onResult) onResult({ ok: tries.length === 0, tries: tries.length }); }
    else { setTries(ts => [...ts, k]); playKey(k, 0.5); } };
  const last = tries[tries.length - 1], lit = {}; if (found) lit[tonic] = 'good'; else if (last != null) lit[last] = 'bad'; if (at >= 0 && !found) lit[keys[at]] = 'cor';
  return (
    <div className="try-box" style={actBox} data-lw="home">
      <div style={actTitle}>{t('The home note', '집 음')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>짧은 선율이 집에 도착하기 전에 멈춰요. <b>집 음(으뜸음)을 흥얼거리고</b>, 그다음 건반에서 찾아요. 찾으면 선율이 집에 도착해요.</> : <>A short tune stops before it gets home. <b>Hum the home note</b> (the tonic), then find it on the keys. Find it, and the tune gets home.</>}</div>
      {found && <div style={{textAlign:'center',fontSize:13,fontWeight:900,color:BK.muted,marginBottom:4}}>{t('The tune was in ' + x.pos + ' position', x.pos + ' 자리 선율이었어요')}</div>}
      <SpKb lo={0} hi={14} W={28} H={78} lit={lit} names={found ? { [tonic]: lwLet(tonic) } : null} onTap={tap} label={t('Find the home note', '집 음 찾기')}/>
      {lwMsg(!heard ? t('Tap ▶ to hear the tune.', '▶를 누르면 선율이 나와요.') : found ? t('Home: ' + lwLet(tonic) + (tries.length ? '.' : ', first time!') + ' Hum it with the key.', '집: ' + lwLet(tonic) + (tries.length ? '.' : ', 한 번에!') + ' 건반과 함께 흥얼거려요.') : last != null ? t('Not home yet. Hum it again, then try.', '아직 집이 아니에요. 다시 흥얼거리고 쳐요.') : t('Hum the home note, then find it.', '집 음을 흥얼거리고, 찾아요.'), found ? BK.green : last != null ? BK.coral : undefined)}
      {lwRow(<>
        <button className="ghost-btn" style={lwBtn} onClick={heard && !fixed ? fresh : () => play(x)}>{!heard ? t('▶ Play a tune', '▶ 선율 듣기') : fixed ? t('♪ Again', '♪ 다시') : t('▶ New tune', '▶ 새 선율')}</button>
        {heard && !fixed && <button className="ghost-btn" style={lwBtn} onClick={() => play(x)}>{t('♪ Again', '♪ 다시')}</button>}
      </>)}
    </div>
  );
}

// ── step 2: two or three? oom-pah or oom-pah-pah: the low note on beat 1, the chord on the other beats ──
function lwMetreEvents(m) { const ev = []; for (let bar = 0; bar < 4; bar++) { const C = bar !== 1 && bar !== 2; for (let b = 0; b < m; b++) { const at = bar * m + b;
  if (b === 0) ev.push({ at, keys: [C ? -12 : -17], len: 0.9, vol: 0.22 }); else if (bar < 3) ev.push({ at, keys: C ? [4, 7] : [-1, 2], len: 0.45, vol: 0.08 }); } } ev.push({ at: 3 * m, keys: [4, 7, 12], len: m * 0.9, vol: 0.09 }); return ev; }
const lwMetrePlay = (m) => spPlay(lwMetreEvents(m), 104);
function LwMetrePad({ onResult }) {
  const [m, setM] = useState(null), [ans, setAns] = useState(null), [run, setRun] = useState(0);
  const fresh = () => { const x = Math.random() < 0.5 ? 2 : 3; setM(x); setAns(null); lwMetrePlay(x); };
  const say = (c) => { if (!m || ans) return; setAns(c); const ok = c === m; setRun(n => (ok ? n + 1 : 0)); if (onResult) onResult({ ok }); };
  return (
    <div className="try-box" style={actBox} data-lw="metre">
      <div style={actTitle}>{t('Two or three?', '두 박? 세 박?')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>낮은 음은 1박, 화음은 나머지 박. <b>쿵-짝</b>이면 두 박, <b>쿵-짝-짝</b>이면 세 박이에요. 박을 세면서 들어요.</> : <>The low note is beat 1; the chord plays the other beats. <b>Oom-pah</b> is two beats in a bar, <b>oom-pah-pah</b> three. Count as you listen.</>}</div>
      {ans && <div style={{margin:'0 0 6px'}}><PlCircles n={m * 4} r={11} gap={27} group={m} kind={(i) => (i % m === 0 ? 'play' : 'beat')} label={(i) => String(i % m + 1)}/></div>}
      {lwRow(<>
        <button className="ghost-btn" style={lwBtn} onClick={() => { setM(null); setAns(null); lwMetrePlay(2); }}>{t('▶ Two', '▶ 두 박')}</button>
        <button className="ghost-btn" style={lwBtn} onClick={() => { setM(null); setAns(null); lwMetrePlay(3); }}>{t('▶ Three', '▶ 세 박')}</button>
        <button className="ghost-btn" style={lwBtn} onClick={fresh}>{t('▶ Which one?', '▶ 어느 쪽?')}</button>
        {m && <button className="ghost-btn" style={lwBtn} onClick={() => lwMetrePlay(m)}>{t('♪ Again', '♪ 다시')}</button>}
      </>)}
      {m && <div style={{display:'grid',gridTemplateColumns:'repeat(2,1fr)',gap:8,marginTop:10}}>{[[2, t('Two: oom-pah', '두 박: 쿵-짝')], [3, t('Three: oom-pah-pah', '세 박: 쿵-짝-짝')]].map(([id, lab]) => <button key={id} className={'choice-btn' + (!ans ? '' : id === m ? ' good' : id === ans ? ' bad' : '')} onClick={() => say(id)} style={{padding:'12px 4px',fontSize:15,fontWeight:900}}>{lab}</button>)}</div>}
      {ans && lwMsg(ans === m ? t('Yes! ' + (run > 1 ? run + ' in a row.' : ''), '맞아요! ' + (run > 1 ? run + '번 연속.' : '')) : t('Count from each low note: 1 2, or 1 2 3?', '낮은 음마다 1부터 세어 봐요: 1 2, 아니면 1 2 3?'), ans === m ? BK.green : BK.coral)}
    </div>
  );
}

// ── step 3: clap it back: a passage in two or three, heard twice, then tapped; the notes show only afterwards ──
const LW_CLAP = [
  [['ts', 2], ['q'], ['q'], ['|'], ['p'], ['q'], ['|'], ['q'], ['q'], ['|'], ['h'], ['||']],
  [['ts', 3], ['q'], ['q'], ['q'], ['|'], ['h'], ['q'], ['|'], ['p'], ['q'], ['q'], ['|'], ['hd'], ['||']],
  [['ts', 2], ['p'], ['q'], ['|'], ['p'], ['p'], ['|'], ['q'], ['q'], ['|'], ['h'], ['||']],
  [['ts', 3], ['h'], ['q'], ['|'], ['p'], ['p'], ['q'], ['|'], ['q'], ['q'], ['q'], ['|'], ['hd'], ['||']],
  [['ts', 2], ['q'], ['p'], ['|'], ['q'], ['q'], ['|'], ['p'], ['p'], ['|'], ['h'], ['||']],
  [['ts', 3], ['q'], ['p'], ['q'], ['|'], ['h'], ['q'], ['|'], ['q'], ['q'], ['q'], ['|'], ['hd'], ['||']],
];
const LW_CLAP_BPM = 84;
function LwClapPad({ onResult, fixed }) {
  const T = usePlTimers();
  const [i, setI] = useState(fixed != null ? fixed : 0), [phase, setPhase] = useState('ready'), [heard, setHeard] = useState(0), [res, setRes] = useState(null);
  const run = useRef(null), taps = useRef([]);
  const items = LW_CLAP[i], snd = srhSounds(items), notes = snd.map((s, j) => [s, j]).filter(([s]) => !s.rest), top = srhTop(items), n = srhBeats(items);
  const reset = () => { T.clear(); stopClicks(); setPhase('ready'); setHeard(0); setRes(null); };
  const listen = () => { T.clear(); setRes(null); const r = rqRunS(items, { bpm: LW_CLAP_BPM }); if (!r) return; setPhase('listen');
    T.at(r, r.at[r.lead] + n * r.spb, () => { const r2 = rqRunS(items, { bpm: LW_CLAP_BPM }); if (!r2) return; T.at(r2, r2.at[r2.lead] + n * r2.spb + 0.2, () => { setPhase('ready'); setHeard(2); }); }); setHeard(1); };
  const go = () => { T.clear(); setRes(null); taps.current = []; const r = rqRunS(items, { bpm: LW_CLAP_BPM, silent: true }); if (!r) return; run.current = r; setPhase('count');
    const g = r.at[r.lead]; T.at(r, g - 0.05, () => setPhase('tap'));
    T.at(r, g + n * r.spb + 0.1, () => { const tol = Math.min(PL_TOL, r.spb * 0.22), mt = plMatch(notes.map(([s]) => g + s.b * r.spb), taps.current.filter(tp => tp > g - tol), tol), marks = {};
      notes.forEach(([s, j], k) => { marks[j] = mt.offs[k] === null ? '?' : '✓'; });
      const out = { hits: mt.hits, total: notes.length, extra: mt.extra, marks, ok: mt.hits >= notes.length - 1 && mt.extra <= 1 }; setRes(out); setPhase('done'); if (onResult) onResult(out); }); };
  const tap = React.useCallback(() => { const r = run.current; if (r && (phase === 'count' || phase === 'tap')) { taps.current.push(r.now()); const ctx = getAudio(); if (ctx) blip(ctx, ctx.currentTime, SRH_HZ, 0.1, 0.16, 'triangle'); } }, [phase]);
  return (
    <div className="try-box" style={actBox} data-lw="clap">
      <div style={actTitle}>{t('Clap it back', '따라 치기')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>짧은 리듬을 <b>두 번</b> 들어요(두 박 또는 세 박). 그다음 클릭에 맞춰 똑같이 쳐요. 음표는 친 다음에 보여요.</> : <>Hear a short passage <b>twice</b> (in two or in three). Then tap it back with the clicks. The notes show afterwards.</>}</div>
      {!fixed && spChips(LW_CLAP.map((_, j) => [j, t('Passage ' + (j + 1), (j + 1) + '번')]), i, (j) => { reset(); setI(j); })}
      {res ? rqStaffEl(items, { marks: res.marks, hearts: false }) : <div style={{textAlign:'center',fontSize:14,fontWeight:900,color:BK.muted,margin:'6px 0'}}>{t(top === 2 ? 'Two beats in a bar' : 'Three beats in a bar', top === 2 ? '한 마디에 두 박' : '한 마디에 세 박')} · {t(['Not heard yet', 'Heard once', 'Heard twice'][Math.min(heard, 2)], ['아직 안 들었어요', '한 번 들었어요', '두 번 들었어요'][Math.min(heard, 2)])}</div>}
      {lwMsg(phase === 'listen' ? t('Listen…', '들어요…') : phase === 'count' ? t('Get ready…', '준비…') : phase === 'tap' ? t('Tap it back!', '따라 쳐요!') : res ? t('On time: ' + res.hits + ' of ' + res.total + (res.extra ? ' · extra taps: ' + res.extra : '') + (res.ok ? ' ✓' : ''), '제때: ' + res.total + '개 중 ' + res.hits + '개' + (res.extra ? ' · 더 친 것: ' + res.extra : '') + (res.ok ? ' ✓' : '')) : '', res ? (res.ok ? BK.green : BK.coral) : undefined)}
      <PlPad on={phase === 'count' || phase === 'tap'} onTap={tap}/>
      {lwRow(<>
        <button className="ghost-btn" style={lwBtn} onClick={listen}>{t('▶ Listen (twice)', '▶ 듣기 (두 번)')}</button>
        <button className="ghost-btn" style={lwBtn} disabled={!heard} onClick={go}>{res ? t('▶ Again', '▶ 다시') : t('▶ Tap it back', '▶ 따라 치기')}</button>
      </>)}
      {plHint()}
    </div>
  );
}

// ── step 4: sing a phrase with its own rhythm (walk, run-ning, hold), heard twice; then play it in C position ──
const LW_PH = [[[28, 1], [29, 1], [30, 2]], [[30, 1], [29, 1], [28, 2]], [[28, 1], [30, 1], [32, 1], [30, 1], [28, 2]], [[32, 1], [31, 1], [30, 1], [29, 1], [28, 2]],
  [[28, 0.5], [29, 0.5], [30, 1], [31, 1], [32, 2]], [[30, 1], [30, 0.5], [31, 0.5], [32, 2]], [[32, 0.5], [31, 0.5], [30, 1], [29, 0.5], [30, 0.5], [28, 2]], [[28, 2], [30, 1], [29, 0.5], [30, 0.5], [32, 2]]];
const lwBeatWord = (b) => (b === 2 ? t('hold', '길게') : b === 1 ? t('walk', '타') : t('run', '티'));
function LwPills({ ph, got = 0, lit = -1, show = false }) {
  return <div style={{display:'flex',gap:4,justifyContent:'center',alignItems:'flex-end',flexWrap:'wrap',margin:'4px 0'}}>{ph.map(([d, b], j) => { const on = j === lit, done = j < got, w = b * 34 + (b - 1) * 4;
    return <span key={j} style={{display:'inline-flex',flexDirection:'column',alignItems:'center',gap:3}}>
      <span style={{width:w,height:30,borderRadius:15,boxSizing:'border-box',display:'inline-flex',alignItems:'center',justifyContent:'center',fontSize:15,fontWeight:900,background:on ? BK.coral : done ? BK.ink : '#fff',border:'2px solid ' + (on ? BK.coral : BK.ink),color:on || done ? '#fff' : BK.ink}}>{done || show ? hpFingerOf('C', 'R', d) : ''}</span>
      <span style={{fontSize:11,fontWeight:900,color:BK.muted}}>{lwBeatWord(b)}</span></span>; })}</div>;
}
function LwPhrasePad({ onResult, fixed }) {
  const T = useSpTimers();
  const [i, setI] = useState(fixed != null ? fixed : 0), [lit, setLit] = useState(-1), [got, setGot] = useState(0), [miss, setMiss] = useState(0), [heard, setHeard] = useState(false), [wrong, setWrong] = useState(null);
  const ph = LW_PH[i], ds = ph.map(([d]) => d), done = got >= ph.length;
  const notes = ph.map(([d, b]) => [hpSemi(d), b]);
  const listen = () => { T.clear(); setHeard(true); const len = lwPlay(notes, 84, T, setLit); const spb = 60 / 84; T.at((0.15 + (len + 1) * spb) * 1000, () => lwPlay(notes, 84, T, setLit)); };
  const reset = (j) => { T.clear(); setI(j); setGot(0); setMiss(0); setHeard(false); setWrong(null); setLit(-1); };
  const tap = (d) => { lsPlay(d, 0.6); if (done || !heard) return; if (d === ds[got]) { const g = got + 1; setGot(g); setWrong(null); if (g >= ds.length && onResult) onResult({ ok: miss === 0, miss }); } else { setMiss(m => m + 1); setWrong(d); } };
  const lit2 = {}; if (got > 0 && !done) lit2[ds[got - 1]] = 'cor';
  return (
    <div className="try-box" style={actBox} data-lw="phrase">
      <div style={actTitle}>{t('Sing it with its rhythm', '리듬까지 따라 부르기')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>이번 선율에는 리듬이 있어요: <b>타</b>, <b>티-티</b>, <b>길게</b>. 두 번 듣고, 리듬까지 똑같이 "라"로 불러요. 그다음 C 자리 오른손으로 쳐요.</> : <>This tune has its own rhythm: <b>walk</b>, <b>run-ning</b>, <b>hold</b>. Hear it twice, sing it back on "la" with the same rhythm, then play it in C position, right hand.</>}</div>
      {!fixed && spChips(LW_PH.map((_, j) => [j, String(j + 1)]), i, reset)}
      <LwPills ph={ph} got={got} lit={lit} show={done}/>
      <div style={{margin:'8px 0 4px'}}><LsKeys lit={lit2} onTap={tap} letters={done}/></div>
      {lwMsg(!heard ? t('Tap ▶ Listen: it plays twice.', '▶ 듣기를 눌러요: 두 번 나와요.') : done ? t('Sung and played ✓' + (miss ? '' : ' First time!'), '부르고 쳤어요 ✓' + (miss ? '' : ' 한 번에!')) : wrong != null ? t('Not that one: sing it again, then try.', '그 건반이 아니에요: 다시 불러 보고 쳐요.') : t('Sing it, then play note ' + (got + 1) + '.', '불러 보고, ' + (got + 1) + '번째 음을 쳐요.'), done ? BK.green : wrong != null ? BK.coral : undefined)}
      {lwRow(<button className="ghost-btn" style={lwBtn} onClick={listen}>{t('▶ Listen (twice)', '▶ 듣기 (두 번)')}</button>)}
    </div>
  );
}

// ── step 5: write the rhythm: two bars of crotchets and minims in 2/4 or 3/4, built note by note ──
const LW_BARS = { 2: [[1, 1], [2]], 3: [[2, 1], [1, 2], [1, 1, 1]] };
const lwDict = (ts, a, b) => ({ ts, bars: [LW_BARS[ts][a], LW_BARS[ts][b]] });
const LW_DICTS = [lwDict(2, 0, 1), lwDict(2, 1, 0), lwDict(3, 0, 2), lwDict(3, 2, 1), lwDict(3, 1, 0), lwDict(2, 0, 0), lwDict(3, 2, 0)];
const lwItemOf = (v) => [v === 2 ? 'h' : 'q'];
const lwDictItems = (D) => [['ts', D.ts]].concat(D.bars[0].map(lwItemOf), [['|']], D.bars[1].map(lwItemOf), [['||']]);
const lwBuiltItems = (ts, mine) => { const out = [['ts', ts]]; [0, 1].forEach(bi => { const bar = mine[bi] || [], used = bar.reduce((a, v) => a + v, 0); bar.forEach(v => out.push(lwItemOf(v))); if (used < ts) out.push(['box', ts - used]); out.push(bi ? ['||'] : ['|']); }); return out; };
const lwDictPlay = (D) => rqRunS(lwDictItems(D), { bpm: 76 });
function LwWritePad({ onResult, fixed }) {
  const [di, setDi] = useState(fixed != null ? fixed : 0), [mine, setMine] = useState([[], []]), [plays, setPlays] = useState(0), [res, setRes] = useState(null), [note, setNote] = useState('');
  const D = LW_DICTS[di], used = (bi) => mine[bi].reduce((a, v) => a + v, 0), cur = used(0) < D.ts ? 0 : 1, full = used(0) === D.ts && used(1) === D.ts;
  const add = (v) => { if (res || full) return; if (used(cur) + v > D.ts) { setNote(t('That does not fit: ' + (D.ts - used(cur)) + ' beat left in this bar.', '들어가지 않아요: 이 마디에 ' + (D.ts - used(cur)) + '박 남았어요.')); return; } setNote(''); const nx = mine.map(b => b.slice()); nx[cur].push(v); setMine(nx); };
  const undo = () => { if (res) return; const nx = mine.map(b => b.slice()); if (nx[1].length) nx[1].pop(); else nx[0].pop(); setMine(nx); setNote(''); };
  const check = () => { const ok = mine[0].join() === D.bars[0].join() && mine[1].join() === D.bars[1].join(); setRes({ ok }); if (onResult) onResult({ ok }); };
  const fresh = () => { let j, g = 0; do { j = Math.floor(Math.random() * LW_DICTS.length); } while (j === di && g++ < 10); setDi(j); setMine([[], []]); setPlays(0); setRes(null); setNote(''); };
  const play = () => { setPlays(p => p + 1); lwDictPlay(D); };
  return (
    <div className="try-box" style={actBox} data-lw="write">
      <div style={actTitle}>{t('Write the rhythm', '리듬 받아 적기')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>두 마디 리듬을 들어요(4분음표와 2분음표). 들을 때마다 박을 세고, <b>음표를 하나씩 골라</b> 마디를 채워요. 다섯 번까지 들을 수 있어요.</> : <>Hear two bars of crotchets and minims. Count the beats each time you listen, then <b>choose the notes one by one</b> to fill the bars. You may listen up to five times.</>}</div>
      {rqStaffEl(res ? lwDictItems(D) : lwBuiltItems(D.ts, mine), { counts: res ? undefined : false, hearts: false })}
      {res && <div style={{fontSize:12.5,fontWeight:900,color:BK.muted,textAlign:'center',marginTop:2}}>{t('You wrote:', '내가 적은 것:')}</div>}
      {res && rqStaffEl(lwBuiltItems(D.ts, mine), { counts: false, hearts: false })}
      {lwMsg(res ? (res.ok ? t('Exactly right ✓', '딱 맞았어요 ✓') : t('Not quite: compare your bars with the answer above.', '조금 달라요: 위의 답과 내 마디를 비교해 봐요.')) : note || (full ? t('Both bars full: check it.', '두 마디가 찼어요: 확인해요.') : t('Bar ' + (cur + 1) + ': ' + (D.ts - used(cur)) + ' beat' + (D.ts - used(cur) > 1 ? 's' : '') + ' to fill.', (cur + 1) + '마디: ' + (D.ts - used(cur)) + '박 남았어요.')), res ? (res.ok ? BK.green : BK.coral) : note ? BK.coral : undefined)}
      {!res && <div style={{display:'grid',gridTemplateColumns:'repeat(3,minmax(0,1fr))',gap:8,marginTop:8}}>
        <button className="choice-btn" onClick={() => add(1)} style={{display:'flex',flexDirection:'column',alignItems:'center',padding:'6px 4px'}} aria-label={t('crotchet', '4분음표')}><Glyph item={NV_NOTES[2]} size={44}/><span style={{fontSize:12,fontWeight:900}}>{t('1 beat', '1박')}</span></button>
        <button className="choice-btn" onClick={() => add(2)} style={{display:'flex',flexDirection:'column',alignItems:'center',padding:'6px 4px'}} aria-label={t('minim', '2분음표')}><Glyph item={NV_NOTES[1]} size={44}/><span style={{fontSize:12,fontWeight:900}}>{t('2 beats', '2박')}</span></button>
        <button className="choice-btn" onClick={undo} style={{padding:'6px 4px',fontSize:15,fontWeight:900}}>{t('⌫ Undo', '⌫ 지우기')}</button>
      </div>}
      {lwRow(<>
        <button className="ghost-btn" style={lwBtn} disabled={plays >= 5 && !res} onClick={play}>{t('▶ Listen (' + Math.max(0, 5 - plays) + ' left)', '▶ 듣기 (' + Math.max(0, 5 - plays) + '번 남음)')}</button>
        {!res && full && <button className="ghost-btn" style={{...lwBtn,background:BK.ink,color:'#fff',borderColor:BK.ink}} onClick={check}>{t('Check', '확인')}</button>}
        {res && !fixed && <button className="ghost-btn" style={lwBtn} onClick={fresh}>{t('▶ Another', '▶ 다른 것')}</button>}
      </>)}
    </div>
  );
}

// ── the pictures on paper ──
const lwPicHome = () => ({ shapes: [{ k: 'raw', svg: '<path d="M8 30 L20 22 L32 26 L44 16" fill="none" stroke="#26296b" stroke-width="2" stroke-dasharray="1 0"/>' + [[8, 30], [20, 22], [32, 26], [44, 16]].map(([x, y]) => '<circle cx="' + x + '" cy="' + y + '" r="3.4" fill="#26296b"/>').join('') + '<path d="M50 30 L60 21 L70 30 V38 H50 Z" fill="none" stroke="#e4572e" stroke-width="2"/>' }], vb: [0, 0, 80, 44] });
const lwPicMetre = () => ({ shapes: [{ k: 'raw', svg: [0, 1, 2, 3, 4, 5].map(i => lsCircleSvg(8 + i * 13 + (i > 2 ? 4 : 0), 22, 5.5, i % 3 === 0 ? 'play' : 'beat', String(i % 3 + 1))).join('') }], vb: [0, 0, 84, 44] });
const lwPicClap = () => lsPicEcho();
const lwPicPhrase = () => ({ shapes: [{ k: 'raw', svg: '<rect x="4" y="15" width="14" height="14" rx="7" fill="#fff" stroke="#26296b" stroke-width="2"/><rect x="21" y="15" width="14" height="14" rx="7" fill="#fff" stroke="#26296b" stroke-width="2"/><rect x="38" y="15" width="34" height="14" rx="7" fill="#e4572e"/>' }], vb: [0, 0, 80, 44] });
const lwPicWrite = () => ({ shapes: [{ k: 'raw', svg: '<path d="M6 34 H74" stroke="#26296b" stroke-width="1.4"/><ellipse cx="18" cy="30" rx="4.6" ry="3.4" fill="#26296b" transform="rotate(-22 18 30)"/><line x1="22.2" x2="22.2" y1="29" y2="10" stroke="#26296b" stroke-width="1.6"/><ellipse cx="40" cy="30" rx="4.6" ry="3.4" fill="none" stroke="#26296b" stroke-width="1.6" transform="rotate(-22 40 30)"/><line x1="44.2" x2="44.2" y1="29" y2="10" stroke="#26296b" stroke-width="1.6"/><rect x="54" y="12" width="14" height="20" rx="2" fill="none" stroke="#e4572e" stroke-width="1.6" stroke-dasharray="3 2"/>' }], vb: [0, 0, 80, 44] });

function lwLbPages(scr = false) {
  const ch = 'listen-write';
  const checks5 = [[lwPicHome(), t('I hum the home note at the end of an unfinished tune', '끝나지 않은 선율 끝에 집 음을 흥얼거려요')], [lwPicMetre(), t('I hear two or three beats in a bar', '한 마디에 두 박인지 세 박인지 들어요')],
    [lwPicClap(), t('I clap back a passage I have heard twice', '두 번 들은 리듬을 따라 쳐요')], [lwPicPhrase(), t('I sing back a tune with its rhythm, then play it', '리듬까지 선율을 따라 부르고 쳐요')], [lwPicWrite(), t('I write down two bars of crotchets and minims', '4분음표와 2분음표 두 마디를 받아 적어요')]];
  const pen = (x) => <PenArt shapes={x.shapes} vb={x.vb} style={{width:90}}/>;
  const toc = [[t('The home note', '집 음'), 2], [t('Two or three?', '두 박? 세 박?'), 3], [t('Clap it back', '따라 치기'), 4], [t('Sing it with its rhythm', '리듬까지 따라 부르기'), 5], [t('Write the rhythm', '리듬 받아 적기'), 6], [t('My five checks', '나의 다섯 가지 확인'), 7]];
  return [
    <LbPage key="1" no={1} chId={ch} teacher={<>{t('Chapter ' + bkChapterNo('listen-sing') + ' a step further, as the Grade 1 aural tests and the listening part of the Grade 1 theory ask: the tonic at the end of an unfinished phrase; a passage in duple or triple time played twice, then tapped or clapped; a short phrase played twice, sung back with its rhythm; and, on paper, two bars of crotchets and minims in 2/4 or 3/4 written from dictation (played up to five times).', bkChapterNo('listen-sing') + '장에서 한 걸음 더: 2단계 청음과 이론 시험의 듣기처럼, 끝나지 않은 선율 끝의 으뜸음, 두 번 들려준 두 박·세 박 리듬 따라 치기, 두 번 들려준 짧은 선율을 리듬까지 따라 부르기, 그리고 종이에 2/4나 3/4의 4분음표·2분음표 두 마디 받아 적기(다섯 번까지 들려줘요).')}</>} qr={bkLink('drill=' + ch + '&lock=1')}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:50,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{t('Listen, Clap, Write', '듣고, 치고, 적기')}</div>
      </div></LbOnly>
      <LbPic h={170}><div style={{width:'100%',maxWidth:560,margin:'0 auto'}}>{rqStaffEl(lwDictItems(LW_DICTS[2]), { hearts: false })}</div></LbPic>
      <LbSay size={18}>{t('Your ears a step further: find home, feel two or three, clap it back, sing it with its rhythm, write it down.', '귀를 한 걸음 더: 집 음 찾기, 두 박·세 박 느끼기, 따라 치기, 리듬까지 부르기, 받아 적기.')}</LbSay>
      <div className="lb-toc" style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>
        <LbOnly print><div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('In this chapter', '이 챕터에서는')}</div>
          {toc.map(([n, p]) => <div key={p} className="lb-toc-row" style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:14.5,padding:'5px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkGoal(15)}{n}</span><span style={{color:BK.muted,fontWeight:800}}>{p}</span></div>)}
        </div></LbOnly>
        <div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 챕터를 마치면')}</div>
          {[t('hum the home note of a tune', '선율의 집 음을 흥얼거릴 수 있어요'), t('hear two or three beats in a bar', '한 마디의 두 박·세 박을 들을 수 있어요'), t('clap back a passage heard twice', '두 번 들은 리듬을 따라 칠 수 있어요'), t('sing back a tune with its rhythm', '리듬까지 선율을 따라 부를 수 있어요'), t('write down a two-bar rhythm', '두 마디 리듬을 받아 적을 수 있어요')].map(x => <div key={x} style={{display:'flex',gap:9,alignItems:'flex-start',fontSize:14.5,padding:'5px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}><span style={{flex:'0 0 auto',marginTop:3}}>{bkGoal(15)}</span><span>{x}</span></div>)}
        </div>
      </div>
      <LbOnly print><LbDrillStrip id={ch}/></LbOnly>
    </LbPage>,
    <LbPage key="2" no={2} chId={ch} kicker={t('Step 1', '1단계')} title={t('The home note', '집 음')}
      teacher={<>{t('Play a short phrase in C or G position that stops on 2 or 5; the child hums the tonic. If it is hard, sing the scale down to it (5 4 3 2 1) and let the voice fall home. Then find it on the keys.', 'C 자리나 G 자리에서 2음이나 5음에서 멈추는 짧은 선율을 쳐 주세요. 아이는 으뜸음을 흥얼거려요. 어려우면 음계를 내려 불러서(5 4 3 2 1) 목소리가 집으로 떨어지게 해 주세요. 그다음 건반에서 찾아요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=1')}>
      <LbLive still={<LbPic h={160}><div style={{width:'100%',maxWidth:520,margin:'0 auto'}}><SpKb maxW={520} lo={0} hi={14} W={32} H={80} lit={{ 0: 'cor', 2: 'pale', 4: 'pale', 5: 'pale', 7: 'pale' }} names={{ 0: t('home', '집') }}/></div></LbPic>} live={<LwHomePad/>}/>
      <LbSay>{LANG === 'ko' ? <>선율이 <b>집에 도착하기 전에</b> 멈추면, 귀가 집을 찾아요. 그 <b>집 음(으뜸음)을 흥얼거리고</b>, 건반에서 찾아요.</> : <>When a tune stops <b>before it gets home</b>, your ear wants home. <b>Hum the home note</b> (the tonic), then find it on the keys.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>선생님이 짧은 선율을 쳐요. 멈추면 집 음을 흥얼거려요.</>, <>어려우면 5 4 3 2 1로 내려 불러요. 마지막 음이 집이에요.</>, <>그 음을 건반에서 찾아서 함께 흥얼거려요.</>]
        : [<>Your teacher plays a short tune. When it stops, hum the home note.</>, <>If it is hard, sing down 5 4 3 2 1: the last one is home.</>, <>Find it on the keys and hum along.</>]}/>
      <LbRemember>{t('The tune stops; your ear goes home.', '선율이 멈추면 귀가 집을 찾아가요.')}</LbRemember>
    </LbPage>,
    <LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={t('Two or three?', '두 박? 세 박?')}
      teacher={<>{t('Play a simple accompaniment: the low note on beat 1, the chord on the others (oom-pah, oom-pah-pah). The child counts from each low note, or sways on 1. Then play a tune with no accompaniment and ask again.', '간단한 반주를 쳐 주세요: 1박에 낮은 음, 나머지 박에 화음(쿵-짝, 쿵-짝-짝). 아이는 낮은 음마다 1부터 세거나, 1에서 몸을 흔들어요. 그다음 반주 없이 선율만 치고 다시 물어봐요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=2')}>
      <LbLive still={<LbPic h={150}><div style={{width:'100%',display:'grid',gap:10}}>{[2, 3].map(m => <div key={m} style={{display:'grid',gridTemplateColumns:'90px 1fr',alignItems:'center',gap:6}}><span style={{fontSize:12.5,fontWeight:900,color:BK.muted}}>{m === 2 ? t('oom-pah', '쿵-짝') : t('oom-pah-pah', '쿵-짝-짝')}</span><PlCircles n={m * 4} r={scr ? 10 : 13} gap={scr ? 24 : 32} group={m} kind={(i) => (i % m === 0 ? 'play' : 'beat')} label={(i) => String(i % m + 1)}/></div>)}</div></LbPic>} live={<LwMetrePad/>}/>
      <LbSay>{LANG === 'ko' ? <>센 박(1)이 몇 박마다 오는지 들어요. <b>쿵-짝</b>이면 한 마디에 <b>두 박</b>, <b>쿵-짝-짝</b>이면 <b>세 박</b>.</> : <>Listen for how often the strong beat (1) comes. <b>Oom-pah</b>: <b>two</b> beats in a bar. <b>Oom-pah-pah</b>: <b>three</b>.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>선생님이 반주를 쳐요. 낮은 음마다 1부터 세어요.</>, <>두 박이면 1에서 손뼉, 2에서 무릎. 세 박이면 손뼉, 무릎, 무릎.</>, <>선율만 들을 때도 해 봐요.</>]
        : [<>Your teacher plays an accompaniment. Count from 1 at each low note.</>, <>In two: clap on 1, pat your knees on 2. In three: clap, pat, pat.</>, <>Now try it with a tune on its own.</>]}/>
      <LbRemember>{t('Oom-pah: two. Oom-pah-pah: three.', '쿵-짝: 두 박. 쿵-짝-짝: 세 박.')}</LbRemember>
    </LbPage>,
    <LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title={t('Clap it back', '따라 치기')}
      teacher={<>{t('Play a passage of four bars in two or three, twice. The child listens both times without clapping, then claps or taps it back at the same speed. Longer than chapter ' + bkChapterNo('listen-sing') + '\'s echo, and heard twice: listen for the shape of the whole passage.', '두 박이나 세 박의 네 마디 리듬을 두 번 쳐 주세요. 아이는 두 번 다 손뼉 치지 않고 듣기만 하고, 그다음 같은 빠르기로 손뼉이나 탭으로 따라 쳐요. ' + bkChapterNo('listen-sing') + '장의 메아리보다 길고, 두 번 들어요: 전체 모양을 들어요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=3')}>
      <LbLive still={<LbPic h={150}><div style={{width:'100%',maxWidth:560,margin:'0 auto'}}>{rqStaffEl(LW_CLAP[1], { hearts: false })}</div></LbPic>} live={<LwClapPad/>}/>
      <LbSay>{LANG === 'ko' ? <>리듬을 <b>두 번</b> 들어요. 듣는 동안은 손뼉 치지 않고 <b>속으로 세어요</b>. 그다음 같은 빠르기로 똑같이 쳐요.</> : <>Hear the passage <b>twice</b>. While it plays, don't clap: <b>count inside</b>. Then clap it back at the same speed.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>선생님이 네 마디를 두 번 쳐요. 듣기만 해요.</>, <>같은 빠르기로 손뼉 쳐요. 긴 음에서는 손을 모은 채 기다려요.</>, <>틀린 곳은 선생님이 그 마디만 다시 쳐 줘요.</>]
        : [<>Your teacher plays four bars, twice. Just listen.</>, <>Clap it back at the same speed. On a long note, keep your hands together and wait.</>, <>Where it went wrong, your teacher plays just that bar again.</>]}/>
      <LbRemember>{t('Listen twice, count inside, then clap.', '두 번 듣고, 속으로 세고, 그다음 손뼉.')}</LbRemember>
    </LbPage>,
    <LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title={t('Sing it with its rhythm', '리듬까지 따라 부르기')}
      teacher={<>{t('A short phrase played twice, with walks, run-nings and a held note: the child sings it back on "la" with both the notes and the rhythm. Then plays it in C position. If the rhythm slips, clap it first, then sing.', '타, 티-티, 긴 음이 섞인 짧은 선율을 두 번 쳐 주세요. 아이는 음과 리듬을 둘 다 살려 "라"로 따라 불러요. 그다음 C 자리에서 쳐요. 리듬이 흔들리면 먼저 손뼉으로 치고, 그다음 불러요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=4')}>
      <LbLive still={<LbPic h={150}><div style={{display:'flex',flexDirection:'column',gap:10,width:'100%',maxWidth:440,margin:'0 auto'}}><LwPills ph={LW_PH[4]} show/><HpKeys pos="C" hands="R" fingers={false} names={false} lit={{ 28: 'cor', 29: 'cor', 30: 'cor', 31: 'cor', 32: 'cor' }} k={2}/></div></LbPic>} live={<LwPhrasePad/>}/>
      <LbSay>{LANG === 'ko' ? <>이번 선율은 음마다 길이가 달라요: <b>타</b>는 한 박, <b>티-티</b>는 반 박씩, <b>길게</b>는 두 박. 두 번 듣고, <b>음과 리듬을 둘 다</b> 따라 불러요.</> : <>In this tune the notes have different lengths: <b>walk</b> is one beat, <b>run-ning</b> half a beat each, <b>hold</b> two beats. Hear it twice, then sing back <b>the notes and the rhythm</b>.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>선생님이 짧은 선율을 두 번 쳐요. 들으면서 속으로 리듬을 세요.</>, <>"라"로 따라 불러요: 음도, 리듬도.</>, <>C 자리 오른손으로 쳐요. 긴 음은 끝까지 누르고 있어요.</>]
        : [<>Your teacher plays a short tune twice. Count the rhythm inside as you listen.</>, <>Sing it back on "la": the notes and the rhythm.</>, <>Play it in C position, right hand. Hold the long note to its end.</>]}/>
      <LbRemember>{t('The notes and the rhythm, both.', '음도, 리듬도, 둘 다.')}</LbRemember>
    </LbPage>,
    <LbPage key="6" no={6} chId={ch} kicker={t('Step 5', '5단계')} title={t('Write the rhythm', '리듬 받아 적기')}
      teacher={<>{t('The written test: the time signature and the speed of the beat are given; two bars of crotchets and minims in 2/4 or 3/4 are played, the child may begin writing at any time. Clap the beat lightly while listening; write the beats first as small strokes, then the notes.', '필기 시험: 박자표와 박의 빠르기를 알려 줘요. 2/4나 3/4의 4분음표·2분음표 두 마디를 들려주고, 아이는 언제든 적기 시작할 수 있어요. 들으면서 박을 살짝 치고, 먼저 박을 작은 선으로 적은 다음 음표를 적어요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=6')}>
      <LbLive still={<LbPic h={190}><div style={{display:'flex',flexDirection:'column',gap:8,width:'100%',maxWidth:560,margin:'0 auto'}}>{rqStaffEl(lwBuiltItems(3, [[2, 1], []]), { counts: false, hearts: false })}<div style={{display:'flex',gap:16,justifyContent:'center'}}><Glyph item={NV_NOTES[2]} size={50}/><Glyph item={NV_NOTES[1]} size={50}/></div></div></LbPic>} live={<LwWritePad/>}/>
      <LbSay>{LANG === 'ko' ? <>두 마디 리듬을 들어요. <b>박자표</b>(2/4 또는 3/4)를 보고, 들을 때마다 <b>박을 세면서</b> 4분음표(1박)와 2분음표(2박)로 마디를 채워요.</> : <>Hear a two-bar rhythm. Look at the <b>time signature</b> (2/4 or 3/4), <b>count the beats</b> each time you listen, and fill the bars with crotchets (1 beat) and minims (2 beats).</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>선생님이 박자표를 말하고 두 마디를 쳐요. 박을 살짝 치며 들어요.</>, <>공책에 박마다 작은 선을 긋고, 소리가 이어지는 곳을 표시해요.</>, <>표시를 음표로 바꿔요: 한 박은 4분음표, 두 박은 2분음표.</>]
        : [<>Your teacher names the time signature and plays two bars. Tap the beat lightly as you listen.</>, <>In your book, draw a small stroke for every beat and mark where a sound carries on.</>, <>Turn the marks into notes: one beat a crotchet, two beats a minim.</>]}/>
      <LbRemember>{t('Count the beats, then choose the notes.', '박을 세고, 그다음 음표를 골라요.')}</LbRemember>
    </LbPage>,
    <LbPage key="7" no={7} chId={ch} kicker={t('Check-up', '점검')} title={t('My five checks', '나의 다섯 가지 확인')}
      teacher={<>{t('Each one with you at the piano, away from the screen: you play, the child hums, says, claps, sings or writes. You only correct.', '하나씩 화면 없이 피아노 앞에서: 선생님이 치고, 아이는 흥얼거리고, 말하고, 손뼉 치고, 부르고, 적어요. 선생님은 고쳐 주기만 해요.')}</>}>
      <LbSay>{t('Tick each one: not yet, nearly, or got it!', '하나씩 표시해요: 아직, 거의, 됐어요!')}</LbSay>
      <LbLive still={<LbStageRows big rows={checks5.map(([a, txt]) => [pen(a), txt])}/>} live={<FiveChecks376 rows={checks5} storeKey="pb_lw_five"/>}/>
    </LbPage>,
  ];
}
function ListenWriteLessonBook() { return <>{lwLbPages(false)}</>; }
function LwLearn({ onStart }) {
  const pages = lwLbPages(true), opener = pages[0];
  return (
    <Lesson id="listen-write" title={t('Listen, clap, write', '듣고, 치고, 적기')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="listen-write"><div className="lb-screen lb-open" style={{display:'flex',flexDirection:'column',gap:12,margin:'0 0 8px'}}>{lbWordsFirst(opener.props.children)}</div></BkChapterCtx.Provider></LbScreenCtx.Provider>}>
      {pages.slice(1).map((pg, i) => <Step key={i} title={pg.props.title}><LbScreenPage page={pg}/></Step>)}
    </Lesson>
  );
}

// ── the drill: every question is heard ──
const LW_LEVELS = [
  { n: 1, label: 'Find the home note', kind: 'home', time: 16 },
  { n: 2, label: 'Two or three beats?', kind: 'metre', time: 14 },
  { n: 3, label: 'Which rhythm did you hear?', kind: 'which', time: 16 },
  { n: 4, label: 'Which shape did the tune make?', kind: 'shape', time: 16 },
  { n: 5, label: 'Clap it back', kind: 'clap', time: 40 },
  { n: 6, label: 'Write the rhythm', kind: 'write', time: 60 },
];
Object.assign(LEVEL_KO, { 'Find the home note': '집 음 찾기', 'Two or three beats?': '두 박? 세 박?', 'Which rhythm did you hear?': '어떤 리듬을 들었나요?', 'Which shape did the tune make?': '선율은 어떤 모양이었나요?', 'Clap it back': '따라 치기', 'Write the rhythm': '리듬 받아 적기' });
// six-note tunes in C position for the shape question: d values; the shape drawn from the notes
const LW_SHAPES = [[28, 29, 30, 31, 32, 30], [32, 31, 30, 29, 28, 30], [28, 30, 32, 31, 29, 28], [32, 30, 28, 29, 31, 32], [30, 31, 32, 31, 30, 29], [29, 28, 30, 32, 31, 30]];
const lwShapePic = (ds, w = 110) => { const mn = Math.min(...ds), mx = Math.max(...ds), pts = ds.map((d, i) => [10 + i * 18, 8 + (mx - d) / Math.max(1, mx - mn) * 28]);
  return <svg viewBox="0 0 110 44" width={w} style={{display:'block',margin:'0 auto',maxWidth:'100%'}} aria-hidden="true"><polyline points={pts.map(p => p.join(',')).join(' ')} fill="none" stroke={BK.coral} strokeWidth="2.4" strokeLinejoin="round"/>{pts.map((p, i) => <circle key={i} cx={p[0]} cy={p[1]} r="3.6" fill={BK.ink}/>)}</svg>; };
function genLwQuestion(lv, prev) {
  const uid = Math.random(), kind = lv.kind;
  if (kind === 'home') { let pos, i, g = 0; do { pos = Math.random() < 0.5 ? 'C' : 'G'; i = Math.floor(Math.random() * LW_HOME.length); } while (prev && prev.key === pos + i && g++ < 10); return { kind, pos, i, answer: spPc(LW_TON[pos]), key: pos + i, uid }; }
  if (kind === 'metre') { const m = Math.random() < 0.5 ? 2 : 3; return { kind, m, answer: m, choices: [2, 3], key: 'm' + m + Math.random(), uid }; }
  if (kind === 'which') { const pool = shuffle(LW_CLAP.map((_, j) => j)).slice(0, 3), a = pick(pool); return { kind, pool, answer: a, choices: pool, key: 'w' + a, uid }; }
  if (kind === 'shape') { const pool = shuffle(LW_SHAPES.map((_, j) => j)).slice(0, 3), a = pick(pool); return { kind, pool, answer: a, choices: pool, key: 's' + a, uid }; }
  if (kind === 'clap') { let i, g = 0; do { i = Math.floor(Math.random() * LW_CLAP.length); } while (prev && prev.i === i && g++ < 10); return { kind, i, answer: 'ok', choices: [], key: 'c' + i, uid }; }
  let i, g = 0; do { i = Math.floor(Math.random() * LW_DICTS.length); } while (prev && prev.i === i && g++ < 10); return { kind: 'write', i, answer: 'ok', choices: [], key: 'd' + i, uid };
}
function lwAnswerLabel(q) {
  if (q.kind === 'home') return lwLet(LW_TON[q.pos]);
  if (q.kind === 'metre') return q.answer === 2 ? t('two beats', '두 박') : t('three beats', '세 박');
  if (q.kind === 'which') return t('passage ' + (q.pool.indexOf(q.answer) + 1), (q.pool.indexOf(q.answer) + 1) + '번');
  if (q.kind === 'shape') return t('shape ' + (q.pool.indexOf(q.answer) + 1), (q.pool.indexOf(q.answer) + 1) + '번 모양');
  return t('done', '완료');
}
function LwQuestion({ q, given, locked, onAnswer, pixel }) {
  const T = useSpTimers(), done = !!given;
  const play = () => { T.clear(); stopClicks();
    if (q.kind === 'home') { const k = lwKeysOf(q.pos, LW_HOME[q.i]); lwPlay(k.map((x, j) => [x, j === k.length - 1 ? 2 : 1]), 100); }
    else if (q.kind === 'metre') lwMetrePlay(q.m);
    else if (q.kind === 'which') rqRunS(LW_CLAP[q.answer], { bpm: LW_CLAP_BPM });
    else if (q.kind === 'shape') lwPlay(LW_SHAPES[q.answer].map(d => [hpSemi(d), 1]), 110); };
  useEffect(() => { if (q.kind === 'clap' || q.kind === 'write') return; const id = setTimeout(play, 350); return () => { clearTimeout(id); T.clear(); }; }, [q.uid]);
  const btnCls = pixel ? 'pixel-choice' : 'choice-btn', cls = (c) => btnCls + (!done ? '' : c === q.answer ? ' good' : given.ans === c ? ' bad' : '');
  const pickIt = (c) => { if (locked || done) return; T.clear(); stopClicks(); onAnswer(c); };
  let title, body;
  if (q.kind === 'home') { title = t('Hum the home note, then tap it.', '집 음을 흥얼거리고, 눌러요.'); const lit = done ? { [LW_TON[q.pos]]: 'good' } : {};
    body = <SpKb lo={0} hi={14} W={28} H={74} lit={lit} names={done ? { [LW_TON[q.pos]]: lwLet(LW_TON[q.pos]) } : null} onTap={(k) => { playKey(k, 0.5); pickIt(spPc(k)); }}/>; }
  else if (q.kind === 'metre') { title = t('Two or three beats in a bar?', '한 마디에 두 박일까요, 세 박일까요?');
    body = <div style={{display:'grid',gridTemplateColumns:'repeat(2,minmax(0,1fr))',gap:8}}>{[2, 3].map(c => <button key={c} disabled={locked} className={cls(c)} style={{padding:'12px 4px',fontSize:16,fontWeight:900}} onClick={() => pickIt(c)}>{c === 2 ? t('Two: oom-pah', '두 박: 쿵-짝') : t('Three: oom-pah-pah', '세 박: 쿵-짝-짝')}</button>)}</div>; }
  else if (q.kind === 'which') { title = t('Listen: which rhythm was it?', '들어 봐요: 어떤 리듬이었나요?');
    body = <div style={{display:'grid',gap:8}}>{q.pool.map((c, j) => <button key={c} disabled={locked} className={cls(c)} style={{padding:'6px 4px'}} onClick={() => pickIt(c)}><div style={{width:'100%',minWidth:0}}>{rqStaffEl(LW_CLAP[c], { counts: false, hearts: false })}</div></button>)}</div>; }
  else if (q.kind === 'shape') { title = t('Listen: which shape did the tune make?', '들어 봐요: 선율은 어떤 모양이었나요?');
    body = <div style={{display:'grid',gridTemplateColumns:'repeat(3,minmax(0,1fr))',gap:8}}>{q.pool.map(c => <button key={c} disabled={locked} className={cls(c)} style={{padding:'8px 4px'}} onClick={() => pickIt(c)}>{lwShapePic(LW_SHAPES[c], pixel ? 70 : 96)}</button>)}</div>; }
  else if (q.kind === 'clap') { title = t('Listen twice, then clap it back.', '두 번 듣고, 따라 쳐요.'); body = <LwClapPad key={q.uid} fixed={q.i} onResult={(r) => pickIt(r.ok ? 'ok' : 'no')}/>; }
  else { title = t('Listen, then write the two bars.', '듣고, 두 마디를 적어요.'); body = <LwWritePad key={q.uid} fixed={q.i} onResult={(r) => pickIt(r.ok ? 'ok' : 'no')}/>; }
  const why = !done ? null : q.kind === 'home' ? t('Home was ' + lwLet(LW_TON[q.pos]) + ': the tune was in ' + q.pos + ' position.', '집은 ' + lwLet(LW_TON[q.pos]) + ': ' + q.pos + ' 자리 선율이었어요.') : q.kind === 'metre' ? t(q.m === 2 ? 'Oom-pah: two beats.' : 'Oom-pah-pah: three beats.', q.m === 2 ? '쿵-짝: 두 박.' : '쿵-짝-짝: 세 박.') : null;
  return (<div>
    <p style={pixel ? {fontSize:11.5,textAlign:'center'} : {fontSize:15,fontWeight:700,textAlign:'center',margin:'0 0 8px',color:'var(--muted)',textWrap:'balance'}}>{title}</p>
    {q.kind !== 'clap' && q.kind !== 'write' && <div style={{textAlign:'center',marginBottom:10}}><button className={pixel ? 'pixel-btn' : 'ghost-btn'} style={{minHeight:44}} onClick={play}>{t('▶ Play it again', '▶ 다시 듣기')}</button></div>}
    {body}
    {why && !pixel && <div style={{marginTop:10,fontSize:13.5,color:'#4a4d86',background:'#fff',borderRadius:8,padding:'7px 10px',lineHeight:1.45}}>{why}</div>}
  </div>);
}
Object.assign(LISTEN_WRITE_DRILL, { levels: LW_LEVELS, generate: genLwQuestion, check: (q, ans) => ans !== null && ans !== undefined && ans === q.answer, answerLabel: lwAnswerLabel, Question: LwQuestion, Learn: LwLearn });
