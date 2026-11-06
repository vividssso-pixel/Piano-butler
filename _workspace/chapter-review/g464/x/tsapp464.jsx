// ─── Phase 464: chapter 8 on screen (B12: what moves on each page), the book as the online lesson, the drill (B10) ───
// Everything is booked on the audio clock like chapters 3 and 5 (plRun, plMatch, PlPad, usePlTimers). The rhythms sound
// on G (392 Hz); a count-in bar first, then the row; the click on every beat, the count spoken when the sound settings ask
// for a voice. Tapped notes sound while the pad is held (Phase 463).
const TS_BPM = 72;
// the beats and sounds of a row: n beats, snd [{ b, d }] (a tie makes two notes one sound), top, repeat (played twice)
function tsSeq(items, ties = []) {
  let b = 0, top = 4, repeat = false; const snd = [], at = {}, into = new Map(ties.map(([a, c]) => [c, a]));
  items.forEach((it, i) => {
    const k = it[0];
    if (k === 'ts') { top = it[1]; return; }
    if (k === 'C') { top = 4; return; }
    if (k === ':||') { repeat = true; return; }
    if (k === '|' || k === '||' || k === 'sp') return;
    const n = it[1];
    if (k === 'p') snd.push({ b, d: 0.5 }, { b: b + 0.5, d: 0.5 });
    else if (!tsIsRest(k) && k !== 'box') { if (into.has(i) && at[into.get(i)]) at[into.get(i)].d += n; else { const s = { b, d: n }; snd.push(s); at[i] = s; } }
    b += n;
  });
  const len = b;
  if (repeat) { snd.push(...snd.map(s => ({ b: s.b + len, d: s.d }))); b *= 2; }
  return { n: b, len, snd, top, repeat };
}
// a count-in bar, then the row. o.accent: beat 1 a little stronger (false for the strong-beat game); o.voiceIn: the
// spoken count only in the count-in (a child counting in her head); o.silent: no notes (she taps them)
function tsPlayRow(seq, o = {}) {
  const top = seq.top, ands = new Set(seq.snd.filter(s => Math.abs(s.b % 1 - 0.5) < 1e-9).map(s => Math.floor(s.b)));
  return plRun(top + seq.n, { bpm: o.bpm || TS_BPM, silentFrom: 0, noVoice: true, extra: (ctx, tm, i, spb) => {
    const inBar = i % top, countIn = i < top;
    const said = SOUND.count === 'voice' && (countIn || !o.voiceIn) && sayCount(ctx, tm, String(inBar + 1), 1);
    if (!said) metroClick(ctx, tm, (o.accent !== false || countIn) && inBar === 0, 0.27);
    if (countIn) return;
    const b = i - top;
    if (!o.silent) seq.snd.filter(s => Math.floor(s.b + 1e-9) === b).forEach(s => blip(ctx, tm + (s.b - b) * spb, 392, Math.max(0.1, s.d * spb * 0.92), 0.2, 'triangle'));
    if (ands.has(b) && SOUND.count === 'voice' && !o.voiceIn) sayCount(ctx, tm + spb / 2, 'and', 0.8);
  } });
}
const tsHold = (r, held) => { const ctx = getAudio(); if (!ctx) return; if (held.current) held.current(); held.current = blip(ctx, ctx.currentTime, 392, 4.3 * r.spb, 0.18, 'triangle'); };
const tsLetGo = (held) => { if (held.current) { held.current(); held.current = null; } };
const tsBar2 = (top) => top === 'C' ? [['C'], ...tsQ(4), ['|'], ...tsQ(4), ['||']] : [['ts', top], ...tsQ(top), ['|'], ...tsQ(top), ['||']];
const tsBox = (pixel, kids) => <div style={{background:pixel ? '#faf6ec' : 'transparent',borderRadius:8,padding:pixel ? 6 : 0}}>{kids}</div>;

// ── pages 2 and 3: listen to the bars (the hearts light), then tap each note (held as long as the note) ──
const TS_PAD = {
  2: { title: () => t('Play with the click', '클릭에 맞춰 쳐요'), rows: [[() => t('Three bars', '세 마디'), TS_ROWS.bars3], [() => t('The repeat sign', '도돌이표'), TS_ROWS.repeat]] },
  3: { title: () => t('Count each time signature', '박자표마다 세요'), rows: [2, 3, 4, 'C'].map(n => [() => n === 'C' ? 'C' : n + '/4', tsBar2(n)]) },
};
function TsPad({ page }) {
  const P = TS_PAD[page], T = usePlTimers();
  const [ri, setRi] = useState(0), [mode, setMode] = useState(null), [phase, setPhase] = useState('ready');
  const [lit, setLit] = useState(-1), [count, setCount] = useState(0), [res, setRes] = useState(null);
  const run = useRef(null), taps = useRef([]), held = useRef(null);
  const items = P.rows[ri][1], seq = tsSeq(items);
  function reset(i) { T.clear(); stopClicks(); setRi(i); setRes(null); setLit(-1); setPhase('ready'); setMode(null); }
  function start(m) {
    T.clear(); setRes(null); setLit(-1); taps.current = []; setMode(m);
    const r = tsPlayRow(seq, { silent: m === 'tap' }); if (!r) return; run.current = r;
    r.at.forEach((a, i) => T.at(r, a, () => { if (i < seq.top) { setCount(i + 1); setPhase('count'); } else { setLit((i - seq.top) % seq.len); setPhase('go'); } }));
    T.at(r, r.at[seq.top] + seq.n * r.spb + 0.05, () => {
      setLit(-1); setPhase('done'); tsLetGo(held);
      if (m !== 'tap') return;
      const want = seq.snd.map(s => r.at[seq.top] + s.b * r.spb), tol = Math.min(PL_TOL, r.spb * 0.22), mm = plMatch(want, taps.current, tol);
      const early = taps.current.filter(tp => tp < r.at[seq.top] - tol).length, marks = [];
      seq.snd.forEach((s, k) => { const j = Math.floor(s.b + 1e-9) % seq.len; marks[j] = mm.offs[k] === null || marks[j] === '?' ? '?' : '✓'; });
      setRes({ hits: mm.hits, total: mm.total, extra: Math.max(0, mm.extra - early), marks });
    });
    setPhase('count'); setCount(0);
  }
  const live = phase === 'count' || phase === 'go';
  const tap = React.useCallback(() => { const r = run.current; if (!r || mode !== 'tap' || !live) return; taps.current.push(r.now()); tsHold(r, held); }, [phase, mode]);
  const release = React.useCallback(() => tsLetGo(held), []);
  const ok = res && res.hits === res.total && res.extra === 0;
  return (
    <div className="try-box" style={actBox} data-ts={'pad' + page}>
      <div style={actTitle}>{P.title()}</div>
      <div style={actNote}>{LANG === 'ko'
        ? <>먼저 <b>들어 봐요</b>: 박마다 심장에 불이 켜져요. 그다음 <b>쳐 봐요</b>: 음마다 그 길이만큼 누르고 있어요.{page === 2 ? <> 도돌이표에서는 처음으로 돌아가요.</> : null} 소리 내어 세요.</>
        : <>First <b>listen</b>: a heart lights up on every beat. Then <b>tap it</b>: hold each note as long as it lasts.{page === 2 ? <> At the repeat sign, go back to the start.</> : null} Count out loud.</>}</div>
      <div style={{display:'flex',gap:5,justifyContent:'center',flexWrap:'wrap',marginBottom:8}}>{P.rows.map(([nm], i) => <button key={i} className={'chip' + (i === ri ? ' active' : '')} onClick={() => reset(i)}>{nm()}</button>)}</div>
      <div style={{maxWidth:470,margin:'0 auto'}}><TsStaff full items={items} o={{ D: 34, lit, marks: res ? res.marks : null }}/></div>
      <div style={{textAlign:'center',fontSize:13,fontWeight:800,color:BK.muted,minHeight:18,margin:'2px 0 4px'}}>{phase === 'count' ? t('Get ready: ', '준비: ') + count : phase === 'go' ? (mode === 'tap' ? t('Tap and hold!', '누르고 있어요!') : t('Listen and count', '들으면서 세요')) : ''}</div>
      <div style={{display:'flex',gap:6,justifyContent:'center',marginBottom:8}}>
        <button className="ghost-btn" onClick={() => start('listen')}>{t('▶ Listen', '▶ 듣기')}</button>
        <button className="ghost-btn" onClick={() => start('tap')}>{t('▶ Tap it', '▶ 쳐 보기')}</button>
      </div>
      {mode === 'tap' && <PlPad on={live} onTap={tap} onRelease={release} label={t('HOLD EACH NOTE', '음마다 누르고 있어요')}/>}
      {res && <div style={{textAlign:'center',fontSize:14.5,fontWeight:900,marginTop:6,color:ok ? BK.green : BK.coral}}>{t('Notes on time: ' + res.hits + ' of ' + res.total + (res.extra ? ' · extra taps: ' + res.extra : ''), '제때 친 음: ' + res.total + '개 중 ' + res.hits + '개' + (res.extra ? ' · 더 친 것: ' + res.extra + '개' : ''))}{ok ? '  ✓' : ''}</div>}
      {mode === 'tap' && plHint()}
    </div>
  );
}

// ── page 4: tap the strong beat. One bar to count in, then four bars of plain clicks: tap on every 1 ──
function TsStrongPad() {
  const T = usePlTimers();
  const [top, setTop] = useState(3), [phase, setPhase] = useState('ready'), [lit, setLit] = useState(-1), [count, setCount] = useState(0), [res, setRes] = useState(null);
  const run = useRef(null), taps = useRef([]);
  const BARS = 4;
  function pickTop(n) { T.clear(); stopClicks(); setTop(n); setRes(null); setLit(-1); setPhase('ready'); }
  function start() {
    T.clear(); setRes(null); setLit(-1); taps.current = [];
    const seq = { n: BARS * top, len: 2 * top, snd: [], top };
    const r = tsPlayRow(seq, { accent: false, voiceIn: true, silent: true }); if (!r) return; run.current = r;
    r.at.forEach((a, i) => T.at(r, a, () => { if (i < top) { setCount(i + 1); setPhase('count'); } else { setLit((i - top) % (2 * top)); setPhase('go'); } }));
    T.at(r, r.at[top] + BARS * top * r.spb + 0.05, () => {
      setLit(-1); setPhase('done');
      const want = Array.from({ length: BARS }, (_, k) => r.at[top + k * top]), tol = Math.min(PL_TOL, r.spb * 0.24), mm = plMatch(want, taps.current, tol);
      const early = taps.current.filter(tp => tp < r.at[top] - tol).length;
      setRes({ hits: mm.hits, total: BARS, extra: Math.max(0, mm.extra - early) });
    });
    setPhase('count'); setCount(0);
  }
  const live = phase === 'count' || phase === 'go';
  const tap = React.useCallback(() => { const r = run.current; if (!r || !live) return; taps.current.push(r.now()); const ctx = getAudio(); if (ctx) blip(ctx, ctx.currentTime, 196, 0.32, 0.24, 'triangle'); }, [phase]);
  const ok = res && res.hits === res.total && res.extra === 0;
  return (
    <div className="try-box" style={actBox} data-ts="strong">
      <div style={actTitle}>{t('Tap the strong beat', '센박에 쳐요')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>한 마디 세고 시작해요. 그다음 클릭은 모두 같은 소리예요: 소리 내어 세면서 <b>1</b>에서만 쳐요. 네\u00a0마디.</> : <>One bar to count in. Then every click sounds the same: count out loud and tap only on <b>1</b>. Four bars.</>}</div>
      <div style={{display:'flex',gap:5,justifyContent:'center',marginBottom:8}}>{[2, 3, 4].map(n => <button key={n} className={'chip' + (n === top ? ' active' : '')} onClick={() => pickTop(n)}>{n + '/4'}</button>)}</div>
      <div style={{maxWidth:470,margin:'0 auto'}}><TsStaff full items={tsBar2(top)} o={{ D: 34, strong: true, mid: top === 4, lit }}/></div>
      <div style={{textAlign:'center',fontSize:13,fontWeight:800,color:BK.muted,minHeight:18,margin:'2px 0 4px'}}>{phase === 'count' ? t('Get ready: ', '준비: ') + count : phase === 'go' ? t('Tap on 1!', '1에서 쳐요!') : ''}</div>
      <div style={{textAlign:'center',marginBottom:8}}><button className="ghost-btn" onClick={start}>{t('▶ Start', '▶ 시작')}</button></div>
      <PlPad on={live} onTap={tap} label={t('TAP ON EVERY 1', '1박마다 쳐요')}/>
      {res && <div style={{textAlign:'center',fontSize:14.5,fontWeight:900,marginTop:6,color:ok ? BK.green : BK.coral}}>{t('Strong beats on time: ' + res.hits + ' of ' + res.total + (res.extra ? ' · extra taps: ' + res.extra : ''), '제때 친 센박: ' + res.total + '개 중 ' + res.hits + '개' + (res.extra ? ' · 더 친 것: ' + res.extra + '개' : ''))}{ok ? '  ✓' : ''}</div>}
      {plHint()}
    </div>
  );
}

// ── page 5: build a bar until it is full. Only what fits can go in; in 4/4 the minim rest starts on 1 or 3 and the
// semibreve rest is a whole bar (B6); 3/4 uses the crotchet rest only ──
const TS_BUILD = { 4: ['q', 'h', 'hd', 'w', 'p', 'r', 'hr', 'wr'], 3: ['q', 'h', 'hd', 'p', 'r'] };
function tsFits(k, top, used, items = []) {
  const b = NV_ROOM[k].b, rem = top - used;
  if (b > rem) return false;
  if ((k === 'wr' || k === 'w') && used > 0) return false;
  if (k === 'hr' && used !== 0 && used !== 2) return false;
  if (k === 'r' && top === 4 && (used === 1 || used === 3) && items[items.length - 1] === 'r') return false;   // silent 1-2 or 3-4: a minim rest
  if (tsIsRest(k) && k !== 'wr' && b === rem && items.every(tsIsRest)) return false;   // a whole silent bar: the semibreve rest
  return true;
}
function TsBuildBar() {
  const T = usePlTimers();
  const [top, setTop] = useState(4), [items, setItems] = useState([]), [lit, setLit] = useState(-1);
  const used = items.reduce((a, k) => a + NV_ROOM[k].b, 0), rem = top - used;
  const row = [['ts', top], ...items.map(k => [k, NV_ROOM[k].b]), ...(rem > 0 ? [['box', rem]] : []), ['||']];
  function play() { T.clear(); setLit(-1); const seq = tsSeq(row); const r = tsPlayRow(seq); if (!r) return; r.at.forEach((a, i) => T.at(r, a, () => setLit(i < top ? -1 : i - top))); T.at(r, r.at[top] + seq.n * r.spb + 0.05, () => setLit(-1)); }
  function add(k) { if (!tsFits(k, top, used, items)) return; T.clear(); stopClicks(); setLit(-1); setItems(x => [...x, k]); }
  const pickTop = (n) => { T.clear(); stopClicks(); setLit(-1); setTop(n); setItems([]); };
  return (
    <div className="try-box" style={actBox} data-ts="build">
      <div style={actTitle}>{t('Build a bar', '마디 만들기')}</div>
      <div style={actNote}>{t('Add notes and rests until the bar is full. Only what fits can go in. Then press ▶ Play it to hear it.', '마디가 꽉 찰 때까지 음표와 쉼표를 넣어요. 들어갈 수 있는 것만 들어가요. 그다음 ▶ 들어 보기를 눌러요.')}</div>
      <div style={{display:'flex',gap:5,justifyContent:'center',marginBottom:8}}>{[3, 4].map(n => <button key={n} className={'chip' + (n === top ? ' active' : '')} onClick={() => pickTop(n)}>{n + '/4'}</button>)}</div>
      <div style={{maxWidth:360,margin:'0 auto'}}><TsStaff full items={row} o={{ D: 44, lit }}/></div>
      <div style={{textAlign:'center',fontSize:15,fontWeight:900,margin:'4px 0 8px',color:rem ? BK.ink : BK.green}}>{rem ? t(rem + (rem === 1 ? ' beat' : ' beats') + ' left', rem + '박 남았어요') : t('Full: ' + top + ' beats ✓', '꽉 찼어요: ' + top + '박 ✓')}</div>
      <div style={{display:'grid',gridTemplateColumns:'repeat(4,minmax(0,1fr))',gap:6,maxWidth:420,margin:'0 auto'}}>
        {TS_BUILD[top].map(k => { const fit = tsFits(k, top, used, items);
          return <button key={k} onClick={() => add(k)} disabled={!fit} aria-label={nvRoomName(k)} className="choice-btn" style={{padding:'4px 2px 6px',opacity:fit ? 1 : 0.32,display:'flex',flexDirection:'column',alignItems:'center',gap:0}}>
            <NvGlyph kind={k} size={42}/><span style={{fontSize:11,fontWeight:800,lineHeight:1.2}}>{nvRoomName(k)}</span><span style={{fontSize:11,fontWeight:900,color:BK.coral}}>{NV_ROOM[k].b}</span></button>; })}
      </div>
      <div style={{fontSize:12.5,color:BK.muted,textAlign:'center',margin:'6px 0 2px'}}>{top === 4 ? t('Silent beats 1 and 2, or 3 and 4: one minim rest. A whole silent bar: the semibreve rest.', '1박과 2박, 또는 3박과 4박을 쉬면 2분쉼표 하나. 한 마디 내내 쉬면 온쉼표.') : t('In 3/4, each silent beat is a crotchet rest. A whole silent bar is not built here.', '3/4에서 쉬는 박은 하나씩 4분쉼표예요. 한 마디 내내 쉬는 마디는 여기서 만들지 않아요.')}</div>
      <div style={{display:'flex',gap:6,justifyContent:'center',marginTop:8}}>
        <button className="ghost-btn" onClick={play} disabled={rem > 0}>{t('▶ Play it', '▶ 들어 보기')}</button>
        <button className="ghost-btn" onClick={() => { T.clear(); stopClicks(); setLit(-1); setItems(x => x.slice(0, -1)); }} disabled={!items.length}>{t('Undo', '되돌리기')}</button>
        <button className="ghost-btn" onClick={() => pickTop(top)} disabled={!items.length}>{t('Clear', '지우기')}</button>
      </div>
    </div>
  );
}

// ── page 6: hear the tie, then the same bars without it ──
function TsTiePad() {
  const T = usePlTimers();
  const [tie, setTie] = useState(true), [lit, setLit] = useState(-1);
  const ties = tie ? [[3, 5]] : [];
  function play(tt) { T.clear(); setLit(-1); setTie(tt); const seq = tsSeq(TS_ROWS.tie, tt ? [[3, 5]] : []); const r = tsPlayRow(seq); if (!r) return;
    r.at.forEach((a, i) => T.at(r, a, () => setLit(i < seq.top ? -1 : i - seq.top))); T.at(r, r.at[seq.top] + seq.n * r.spb + 0.05, () => setLit(-1)); }
  return (
    <div className="try-box" style={actBox} data-ts="tie">
      <div style={actTitle}>{t('Hear the tie', '붙임줄 들어 보기')}</div>
      <div style={actNote}>{t('With the tie, G sounds once and holds through beat 1 of bar 2. Without it, G plays again on beat 1 of bar 2.', '붙임줄이 있으면 G를 한 번 치고 2마디 1박까지 누르고 있어요. 없으면 2마디 1박에서 G를 다시 쳐요.')}</div>
      <div style={{maxWidth:470,margin:'0 auto'}}><TsStaff full items={TS_ROWS.tie} o={{ D: 34, ties, lit }}/></div>
      <div style={{display:'flex',gap:6,justifyContent:'center',marginTop:8}}>
        <button className={'ghost-btn' + (tie ? ' active' : '')} onClick={() => play(true)}>{t('▶ With the tie', '▶ 붙임줄 있음')}</button>
        <button className={'ghost-btn' + (!tie ? ' active' : '')} onClick={() => play(false)}>{t('▶ Without the tie', '▶ 붙임줄 없음')}</button>
      </div>
    </div>
  );
}

// ── the book on screen: the opener is the lesson's head, every other page a step. Old ticks kept where the idea is
// the same: 'Bar lines' (2), 'The two numbers' (0), 'Strong and weak beats' (7), 'Fill the bar' (11); the tie and the
// checks are new (13, 14). ──
const TS_STORE = [2, 0, 7, 11, 13, 14];
function TsLearn({ onStart }) {
  const pages = tsLbPages(true);
  const opener = pages[0];
  return (
    <Lesson id="time-signatures" title={t('Time Signatures', '박자표')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="time-signatures"><div className="lb-screen lb-open" style={{display:'flex',flexDirection:'column',gap:12,margin:'0 0 8px'}}>{lbWordsFirst(opener.props.children)}</div></BkChapterCtx.Provider></LbScreenCtx.Provider>}>
      {pages.slice(1).map((pg, i) => (
        <Step key={i} storeAs={TS_STORE[i]} title={pg.props.title}>
          <LbScreenPage page={pg}/>
        </Step>
      ))}
    </Lesson>
  );
}

// ── the drill (B10): six levels for this room, then four higher ones, each marked with its grades
// (AMEB Theory: the whole-bar rest and 6/8 at Grade 2, 2/2 3/2 3/8 9/8 at Grade 3, 6/4 12/8 at Grade 4; ABRSM: 2/2 3/2
// 4/2 3/8 at Grade 2, 6/8 9/8 12/8 at Grade 3, 2/8 4/8 6/4 9/4 12/4 at Grade 4, 5/4 7/4 5/8 7/8 at Grade 5) ──
const TS_LEVELS = [
  { n: 1, label: 'How many beats in a bar?', kind: 'top', time: 8 },
  { n: 2, label: 'Where does the bar line go?', kind: 'barline', time: 12 },
  { n: 3, label: 'Tap the strong beat', kind: 'tapstrong', time: 24, noPrint: true },
  { n: 4, label: 'Rests on the staff', kind: 'reston', time: 8 },
  { n: 5, label: 'Fill the bar', kind: 'fill', time: 12 },
  { n: 6, label: 'Ties: how many beats?', kind: 'tie', time: 10 },
  { n: 7, label: 'Whole-bar rests (ABRSM 1, AMEB 2)', kind: 'wholebar', time: 8 },
  { n: 8, label: 'The bottom number: 2, 4 or 8 (ABRSM 2 to 4, AMEB 3)', kind: 'bottom', time: 10 },
  { n: 9, label: 'Compound time: big beats (AMEB 2 to 4, ABRSM 3)', kind: 'six8', time: 10 },
  { n: 10, label: 'Simple, compound or irregular? (ABRSM 3 to 5)', kind: 'meter', time: 10 },
];
Object.assign(LEVEL_KO, {
  'How many beats in a bar?': '한 마디에 몇 박?', 'Where does the bar line go?': '세로줄은 어디에?', 'Tap the strong beat': '센박에 쳐요',
  'Fill the bar': '마디 채우기', 'Rests on the staff': '오선 위의 쉼표', 'Ties: how many beats?': '붙임줄: 몇 박?',
  'Whole-bar rests (ABRSM 1, AMEB 2)': '한 마디 쉼표 (ABRSM 1급, AMEB 2급)', 'The bottom number: 2, 4 or 8 (ABRSM 2 to 4, AMEB 3)': '아래 숫자: 2, 4, 8 (ABRSM 2~4급, AMEB 3급)',
  'Compound time: big beats (AMEB 2 to 4, ABRSM 3)': '겹박자: 큰 박 (AMEB 2~4급, ABRSM 3급)', 'Simple, compound or irregular? (ABRSM 3 to 5)': '홑박자, 겹박자, 혼합박자? (ABRSM 3~5급)',
});
// the higher levels say their rule over every question (nothing in the book teaches it yet)
const TS_RULE = {
  wholebar: () => t('A semibreve rest also fills a whole bar of 2/4 or 3/4.', '온쉼표는 2/4나 3/4에서도 한 마디 전체를 쉬어요.'),
  bottom: () => t('The bottom number is the beat: 2 a minim, 4 a crotchet, 8 a quaver. C with a line through it is 2/2.', '아래 숫자가 한 박이에요: 2는 2분음표, 4는 4분음표, 8은 8분음표. 줄이 그어진 C는 2/2예요.'),
  six8: () => t('6/8, 9/8, 12/8: the quavers go in threes. Three quavers make one big beat.', '6/8, 9/8, 12/8: 8분음표가 셋씩 묶여요. 8분음표 셋이 큰 박 하나예요.'),
  meter: () => t('Simple: each beat splits in two. Compound: each beat splits in three (top 6, 9 or 12). Irregular: 5 or 7.', '홑박자: 한 박이 둘로 나뉘어요. 겹박자: 한 박이 셋으로 나뉘어요 (위 숫자 6, 9, 12). 혼합박자: 5나\u00a07.'),
};
// the bars the levels are made of, by time signature (every one written the way the books write it)
const TS_BARS = {
  2: [['q', 'q'], ['h'], ['p', 'q'], ['q', 'p'], ['q', 'r'], ['r', 'q']],
  3: [['q', 'q', 'q'], ['h', 'q'], ['q', 'h'], ['hd'], ['p', 'q', 'q'], ['q', 'p', 'q'], ['h', 'r'], ['q', 'r', 'q'], ['r', 'q', 'q']],
  4: [['q', 'q', 'q', 'q'], ['h', 'h'], ['h', 'q', 'q'], ['q', 'q', 'h'], ['hd', 'q'], ['w'], ['p', 'q', 'h'], ['q', 'p', 'q', 'q'], ['q', 'q', 'r', 'q'], ['h', 'hr'], ['hr', 'h'], ['q', 'r', 'h']],
};
const tsItems = (bar) => bar.map(k => [k, NV_ROOM[k].b]);
const TS_TIES = [   // [top, bar 1, bar 2, beats the tied G sounds]
  [4, ['q', 'q', 'h'], ['q', 'q', 'h'], 3], [4, ['h', 'h'], ['h', 'q', 'q'], 4], [4, ['q', 'q', 'q', 'q'], ['h', 'h'], 3], [4, ['hd', 'q'], ['hd', 'q'], 4], [4, ['h', 'h'], ['w'], 6],
  [3, ['q', 'h'], ['q', 'h'], 3], [3, ['q', 'q', 'q'], ['hd'], 4], [3, ['hd'], ['hd'], 6], [2, ['q', 'q'], ['h'], 3], [2, ['h'], ['q', 'q'], 3],
];
const TS_NOTE = { minim: () => NV_NOTES[1], crotchet: () => NV_NOTES[2], quaver: () => NV_NOTES[3], dcrotchet: () => NV_DOTTED.find(d => d.id === 'crotchet') };
const TS_METERS = { simple: ['2/4', '3/4', '4/4', '2/2', '3/8', '3/2'], compound: ['6/8', '9/8', '12/8', '6/4', '9/4', '12/4'], irregular: ['5/4', '7/4', '5/8', '7/8'] };
function genTsQuestion(lv, prev) {
  const uid = Math.random();
  const notPrev = (make, keyOf) => { let x = make(), g = 0; while (prev && prev.key === keyOf(x) && g++ < 14) x = make(); return x; };
  // level 1: 2, 3 and 4 (or C) a third each
  if (lv.kind === 'top') { const n = notPrev(() => pick([2, 3, pick([4, 'C'])]), x => 'top' + x); return { kind: 'top', sig: n, key: 'top' + n, answer: n === 'C' ? 4 : n, choices: [2, 3, 4], uid }; }
  if (lv.kind === 'barline') {
    return notPrev(() => {
      const n = pick([2, 3, 4]); let a, b, g = 0;
      do { a = pick(TS_BARS[n]); b = pick(TS_BARS[n]); } while (a.length + b.length < 4 && g++ < 30);
      const items = [['ts', n], ...tsItems(a), ['|'], ...tsItems(b), ['||']];
      const right = a.length + 2;   // the item after the bar line
      const gaps = []; for (let j = 2; j < items.length - 1; j++) if (items[j][0] !== '|' && items[j - 1][0] !== '|' && items[j - 1][0] !== 'ts') gaps.push(j);
      const cand = shuffle([right, ...sampleN(gaps, 2)]).sort((x, y) => x - y);
      return { kind: 'barline', items, cand, key: 'bl' + items.map(x => x[0]).join(), answer: 'ABC'[cand.indexOf(right)], choices: cand.map((_, i) => 'ABC'[i]), uid };
    }, q => q.key);
  }
  if (lv.kind === 'tapstrong') { const n = notPrev(() => pick([2, 3, 4]), x => 'ts' + x); return { kind: 'tapstrong', top: n, key: 'ts' + n, uid }; }
  if (lv.kind === 'fill') {
    return notPrev(() => {
      const n = pick([2, 3, 4]); const bar = pick(TS_BARS[n].filter(x => x.length > 1)); const j = Math.floor(Math.random() * bar.length), k = bar[j], b = NV_ROOM[k].b;
      const wrong = sampleN(['q', 'h', 'hd', 'w', 'r', 'hr'].filter(x => NV_ROOM[x].b !== b), 2);
      const items = [['ts', n], ...tsItems(bar), ['||']];
      return { kind: 'fill', items, at: j + 1, ans: k, key: 'f' + n + bar.join() + j, answer: k, choices: shuffle([k, ...wrong]), uid };
    }, q => q.key);
  }
  if (lv.kind === 'reston') {
    return notPrev(() => {
      const want = pick(['r', 'hr', 'wr']), n = want === 'r' ? pick([2, 3, 4]) : 4;   // the rest first: each one as often
      const bars = want === 'wr' ? [['wr']] : TS_BARS[n].filter(x => x.includes(want));
      const bar = pick(bars).map(k => k === 'wr' ? ['wr', 4] : [k, NV_ROOM[k].b]), j = bar.findIndex(x => x[0] === want);
      return { kind: 'reston', items: [['ts', n], ...bar, ['||']], hl: j + 1, key: 'r' + n + bar.map(x => x[0]).join(), answer: bar[j][0], choices: ['r', 'hr', 'wr'], uid };
    }, q => q.key);
  }
  if (lv.kind === 'tie') {
    const [n, a, b, ans] = notPrev(() => pick(TS_TIES), x => 'tie' + x.join());
    const items = [['ts', n], ...tsItems(a), ['|'], ...tsItems(b), ['||']];
    const place = pick([0, 1, 2, 3].filter(p => ans - p >= 1)), lo = ans - place, opts = [lo, lo + 1, lo + 2, lo + 3];   // the answer in any of the four places
    return { kind: 'tie', items, ties: [[a.length, a.length + 2]], key: 'tie' + [n, a, b, ans].join(), answer: ans, choices: opts, uid };
  }
  if (lv.kind === 'wholebar') {
    const n = notPrev(() => pick([2, 3, 4]), x => 'wb' + x);
    const items = [['ts', n], ...tsItems(pick(TS_BARS[n].filter(x => !x.some(tsIsRest)))), ['|'], ['wr', n], ['||']];
    return { kind: 'wholebar', items, top: n, key: 'wb' + n, answer: n, choices: [1, 2, 3, 4], uid };
  }
  if (lv.kind === 'six8') {   // 6/8, 9/8, 12/8: how many big beats; how many quavers; which note is one big beat
    const [v, sig] = notPrev(() => [pick(['beats', 'beats', 'quavers', 'unit']), pick(['6/8', '9/8', '12/8'])], x => 's8' + x.join());
    const top = Number(sig.split('/')[0]);
    if (v === 'beats') return { kind: 'six8', v, sig, key: 's8' + v + sig, answer: top / 3, choices: [2, 3, 4, 6], uid };
    if (v === 'quavers') return { kind: 'six8', v, sig, key: 's8' + v + sig, answer: top, choices: [6, 8, 9, 12], uid };
    return { kind: 'six8', v, sig, key: 's8' + v + sig, answer: 'dcrotchet', choices: shuffle(['dcrotchet', 'crotchet', 'quaver', 'minim']), uid };
  }
  if (lv.kind === 'bottom') {
    const sig = notPrev(() => pick(['2/2', '3/2', '4/2', '3/8', '2/8', '4/8', '2/4', '3/4', '4/4', 'cut']), x => 'bt' + x);
    const bot = sig === 'cut' ? 2 : Number(sig.split('/')[1]);
    return { kind: 'bottom', sig, key: 'bt' + sig, answer: ({ 2: 'minim', 4: 'crotchet', 8: 'quaver' })[bot], choices: ['minim', 'crotchet', 'quaver'], uid };
  }
  const cat = pick(['simple', 'compound', 'irregular']), sig = notPrev(() => pick(TS_METERS[cat]), x => 'm' + x);
  return { kind: 'meter', sig, key: 'm' + sig, answer: cat, choices: ['simple', 'compound', 'irregular'], uid };
}
const TS_METER_NAME = { simple: () => t('Simple', '홑박자'), compound: () => t('Compound', '겹박자'), irregular: () => t('Irregular', '혼합박자') };
const tsNoteName = (k) => k === 'dcrotchet' ? t('dotted crotchet', '점4분음표') : k === 'minim' ? t('minim', '2분음표') : k === 'crotchet' ? t('crotchet', '4분음표') : t('quaver', '8분음표');
// a time signature on its own, big (the higher levels); 'cut': C with a line through it
function TsBigSig({ sig, ink }) {
  if (sig === 'cut') return <svg viewBox="0 0 40 56" width="40" height="56" aria-label={t('cut time', '알라 브레베')}><text x="20" y="40" textAnchor="middle" fontFamily="Playfair Display, Georgia, serif" fontSize="40" fontWeight="900" fill={ink}>C</text><line x1="21" x2="21" y1="6" y2="50" stroke={ink} strokeWidth="2.6"/></svg>;
  const [a, b] = sig.split('/'); return <TSig top={a} bottom={b} size={52} ink={ink}/>;
}
function TsQuestion({ q, given, locked, onAnswer, pixel }) {
  const board = useBoard(q, given);
  const T = usePlTimers();
  const [phase, setPhase] = useState('ready'), [lit, setLit] = useState(-1);
  const run = useRef(null), taps = useRef([]);
  const done = !!given;
  const ink = pixel ? '#faf6ec' : '#26296b';
  const btnCls = pixel ? 'pixel-choice' : 'choice-btn';
  const prompt = (txt) => <p style={pixel ? {fontSize:11.5,textAlign:'center',margin:'0 0 10px',lineHeight:1.7} : {fontSize:15,fontWeight:700,textAlign:'center',margin:'0 0 10px',color:'var(--muted)'}}>{txt}</p>;
  const same = (c) => c === q.answer || (typeof c === 'number' && Math.abs(c - q.answer) < 1e-9);
  const st = (c) => !done ? '' : same(c) ? ' good' : (given.ans === c ? ' bad' : '');
  const grid = (cols, render, pad = '14px 4px') => <div style={{display:'grid',gridTemplateColumns:'repeat(' + cols + ',1fr)',gap:8}}>{q.choices.map(c => <button key={c} disabled={locked} onClick={() => onAnswer(c)} className={btnCls + st(c)} style={{padding:pad}}>{render(c)}</button>)}</div>;
  const staff = (items, o, extra, mw = 430) => tsBox(pixel, <div style={{maxWidth:mw,margin:'0 auto 10px'}}><TsStaff full items={items} o={o} extra={extra}/></div>);
  useEffect(() => { T.clear(); stopClicks(); setPhase('ready'); setLit(-1); taps.current = []; }, [q.uid]);
  if (q.kind === 'tapstrong') {
    const top = q.top, BARS = 4;
    function start() {
      if (done || phase !== 'ready') return;
      T.clear(); taps.current = [];
      const r = tsPlayRow({ n: BARS * top, len: 2 * top, snd: [], top }, { accent: false, voiceIn: true, silent: true }); if (!r) return; run.current = r;
      r.at.forEach((a, i) => T.at(r, a, () => { setPhase(i < top ? 'count' : 'go'); setLit(i < top ? -1 : (i - top) % (2 * top)); }));
      T.at(r, r.at[top] + BARS * top * r.spb + 0.05, () => {
        setPhase('scoring'); setLit(-1);
        const want = Array.from({ length: BARS }, (_, k) => r.at[top + k * top]), tol = Math.min(PL_TOL, r.spb * 0.24), m = plMatch(want, taps.current, tol);
        const early = taps.current.filter(tp => tp < r.at[top] - tol).length, extra = Math.max(0, m.extra - early);
        onAnswer({ ok: m.hits === m.total && extra === 0, hits: m.hits, total: m.total, extra });
      });
      setPhase('count');
    }
    const onTap = () => { const r = run.current; if (r && (phase === 'count' || phase === 'go')) { taps.current.push(r.now()); const ctx = getAudio(); if (ctx) blip(ctx, ctx.currentTime, 196, 0.32, 0.24, 'triangle'); } };
    const res = done && given.ans && typeof given.ans === 'object' ? given.ans : null;
    return <div>
      <BoardTrack b={board} pixel={pixel}/>
      {prompt(t('One bar to count in. Then count out loud and tap only on 1. Four bars.', '한 마디 세고 시작해요. 그다음 소리 내어 세면서 1에서만 쳐요. 네 마디.'))}
      {staff(tsBar2(top), { D: 34, strong: true, mid: top === 4, lit })}
      <div style={{textAlign:'center',fontSize:13,fontWeight:800,color:pixel ? '#faf6ec' : BK.muted,minHeight:18,margin:'2px 0 4px'}}>{phase === 'count' ? t('Get ready…', '준비…') : phase === 'go' ? t('Tap on 1!', '1에서 쳐요!') : ''}</div>
      {!done && phase === 'ready' && <div style={{textAlign:'center',marginBottom:8}}><button className={pixel ? 'pixel-btn' : 'ghost-btn'} onClick={start} style={{fontSize:15,padding:'10px 18px'}}>{t('▶ Start', '▶ 시작')}</button></div>}
      {!done && <PlPad on={phase === 'count' || phase === 'go'} onTap={onTap} h={64} label={t('TAP ON EVERY 1', '1박마다 쳐요')}/>}
      {res && <div style={{textAlign:'center',fontSize:15,fontWeight:900,marginTop:8,color:res.ok ? BK.green : BK.coral}}>{t('Strong beats on time: ' + res.hits + ' of ' + res.total + (res.extra ? ' · extra taps: ' + res.extra : ''), '제때 친 센박: ' + res.total + '개 중 ' + res.hits + '개' + (res.extra ? ' · 더 친 것: ' + res.extra + '개' : ''))}</div>}
    </div>;
  }
  let body;
  if (q.kind === 'top') body = <>
    {prompt(t('How many beats are in each bar?', '한 마디에 몇 박이 있을까요?'))}
    {staff([q.sig === 'C' ? ['C'] : ['ts', q.sig], ['sp', 60], ['||']], { hearts: false }, null, 200)}
    {grid(3, c => <span style={{fontSize:pixel ? 12 : 18,fontWeight:900}}>{c}</span>)}
  </>;
  else if (q.kind === 'barline') body = <>
    {prompt(t('The bar line is missing. Where does it go: A, B or C?', '세로줄이 빠졌어요. 어디에 들어갈까요: A, B, C?'))}
    {staff(q.items, { hearts: false, noBars: true, D: 30 }, (yOf, txt, m) => <g>
      {q.cand.map((j, i) => { const gx = m.noteX[j] - 18, right = done && 'ABC'[i] === q.answer; return <g key={j}>
        <text x={gx} y={yOf(40, 'treble') - 4} textAnchor="middle" fontSize="13" fontWeight="900" fill={BK.coral} style={txt}>{'ABC'[i]}</text>
        {right ? <line x1={gx} x2={gx} y1={yOf(38, 'treble')} y2={yOf(30, 'treble')} stroke={BK.coral} strokeWidth="2.2"/> : <path d={`M${gx - 4} ${yOf(39, 'treble') - 2} L${gx + 4} ${yOf(39, 'treble') - 2} L${gx} ${yOf(39, 'treble') + 4} Z`} fill={BK.coral}/>}
      </g>; })}
    </g>)}
    {grid(3, c => <span style={{fontSize:pixel ? 12 : 18,fontWeight:900}}>{c}</span>)}
  </>;
  else if (q.kind === 'fill') {
    const items = q.items.map((x, i) => i === q.at ? (done ? [q.ans, NV_ROOM[q.ans].b] : ['box', NV_ROOM[q.ans].b]) : x);
    body = <>
      {prompt(t('Which one fills the bar?', '어느 것이 마디를 채울까요?'))}
      {staff(items, { D: 40, hl: done ? q.at : undefined })}
      {grid(3, c => <><NvGlyph kind={c} size={48} ink={pixel ? '#faf6ec' : undefined}/>{done && !pixel && <span style={{display:'block',fontSize:12,fontWeight:700}}>{nvRoomName(c)}</span>}</>, '6px 2px')}
    </>;
  }
  else if (q.kind === 'reston') body = <>
    {prompt(t('What is the coloured rest called?', '색칠된 쉼표의 이름은 무엇일까요?'))}
    {staff(q.items, { D: 40, hearts: false, hl: q.hl })}
    {grid(3, c => <span style={{fontSize:pixel ? 10 : 14,fontWeight:800}}>{cap(nvRoomName(c))}</span>)}
  </>;
  else if (q.kind === 'tie') body = <>
    {prompt(t('The tie joins two Gs. How many beats does G sound?', '붙임줄이 G 두 개를 이어요. G는 몇 박 동안 소리 날까요?'))}
    {staff(q.items, { D: 34, hearts: false, ties: q.ties })}
    {grid(q.choices.length, c => <span style={{fontSize:pixel ? 12 : 18,fontWeight:900}}>{c}</span>)}
  </>;
  else if (q.kind === 'wholebar') body = <>
    {prompt(t('How many beats of silence are in bar 2?', '2마디는 몇 박 동안 쉴까요?'))}
    {staff(q.items, { D: 34, hearts: false })}
    {grid(4, c => <span style={{fontSize:pixel ? 12 : 18,fontWeight:900}}>{c}</span>)}
  </>;
  else if (q.kind === 'six8') body = <>
    {prompt(q.v === 'quavers' ? t('How many quavers fill a bar of ' + q.sig + '?', q.sig + '에서 한 마디는 8분음표 몇 개일까요?') : q.v === 'beats' ? t('How many big beats are in a bar of ' + q.sig + '?', q.sig + '에서 한 마디는 큰 박 몇 개일까요?') : t('Which note is one big beat in ' + q.sig + '?', q.sig + '에서 큰 박 하나는 어떤 음표일까요?'))}
    <div style={{textAlign:'center',margin:'0 0 12px',color:ink}}><TsBigSig sig={q.sig} ink={ink}/></div>
    {q.v === 'unit' ? grid(2, c => <><Glyph item={TS_NOTE[c]()} ink={ink} size={52}/>{done && !pixel && <span style={{display:'block',fontSize:12,fontWeight:700}}>{tsNoteName(c)}</span>}</>, '6px 2px') : grid(q.choices.length, c => <span style={{fontSize:pixel ? 12 : 18,fontWeight:900}}>{c}</span>)}
  </>;
  else if (q.kind === 'bottom') body = <>
    {prompt(t('Which note is one beat?', '어떤 음표가 한 박일까요?'))}
    <div style={{textAlign:'center',margin:'0 0 12px',color:ink}}><TsBigSig sig={q.sig} ink={ink}/></div>
    {grid(3, c => <><Glyph item={TS_NOTE[c]()} ink={ink} size={52}/>{done && !pixel && <span style={{display:'block',fontSize:12,fontWeight:700}}>{tsNoteName(c)}</span>}</>, '6px 2px')}
  </>;
  else body = <>
    {prompt(t('Simple, compound or irregular time?', '홑박자, 겹박자, 혼합박자 중 어느 것일까요?'))}
    <div style={{textAlign:'center',margin:'0 0 12px',color:ink}}><TsBigSig sig={q.sig} ink={ink}/></div>
    {grid(3, c => <span style={{fontSize:pixel ? 10 : 15,fontWeight:900}}>{TS_METER_NAME[c]()}</span>)}
  </>;
  const rule = TS_RULE[q.kind];
  return <div><BoardTrack b={board} pixel={pixel}/>{rule && <div style={{fontSize:pixel ? 10 : 13,fontWeight:800,color:pixel ? '#faf6ec' : BK.ink,background:pixel ? 'transparent' : '#fbe3da',borderRadius:8,padding:'6px 10px',margin:'0 0 10px',lineHeight:1.45,textAlign:'center'}}>{rule()}</div>}{body}</div>;
}
function tsCheck(q, ans) {
  if (ans === null || ans === undefined) return false;
  if (q.kind === 'tapstrong') return !!(ans && ans.ok);
  if (typeof q.answer === 'number') return typeof ans === 'number' && Math.abs(ans - q.answer) < 1e-9;
  return ans === q.answer;
}
function tsAnswerLabel(q) {
  const beats = (n) => t(n + (n === 1 ? ' beat' : ' beats'), n + '박');
  if (q.kind === 'top') return t(q.answer + ' beats in a bar (' + (q.sig === 'C' ? 'C' : q.sig + '/4') + ')', '한 마디에 ' + q.answer + '박 (' + (q.sig === 'C' ? 'C' : q.sig + '/4') + ')');
  if (q.kind === 'barline') return t(q.answer + ', after ' + q.items[0][1] + ' beats', q.answer + ', ' + q.items[0][1] + '박 다음');
  if (q.kind === 'tapstrong') return t('4 taps, one on every 1', '1박마다 한 번, 4번');
  if (q.kind === 'fill') return LANG === 'ko' ? nvRoomName(q.answer) + ' (' + NV_ROOM[q.answer].b + '박)' : (q.answer === 'p' ? '' : 'a ') + nvRoomName(q.answer) + ' (' + beats(NV_ROOM[q.answer].b) + ')';
  if (q.kind === 'reston') return LANG === 'ko' ? nvRoomName(q.answer) + ({ r: '. 오선 가운데에 서 있어요', hr: '. 3번 줄 위에 앉아요', wr: '. 4번 줄에 매달려요' })[q.answer] : 'a ' + nvRoomName(q.answer) + ({ r: '. It stands in the middle of the staff', hr: '. It sits on line 3', wr: '. It hangs from line 4' })[q.answer];
  if (q.kind === 'tie') return beats(q.answer);
  if (q.kind === 'wholebar') return t(q.answer + ' beats (a whole bar)', q.answer + '박 (한 마디 전체)');
  if (q.kind === 'six8') return (q.v === 'unit' ? t('a dotted crotchet', '점4분음표') : q.v === 'beats' ? t(q.answer + ' big beats', '큰 박 ' + q.answer + '개') : t(q.answer + ' quavers', '8분음표 ' + q.answer + '개')) + ' (' + q.sig + ')';
  if (q.kind === 'bottom') return t('a ' + tsNoteName(q.answer), tsNoteName(q.answer)) + ' (' + (q.sig === 'cut' ? t('cut time, 2/2', '알라 브레베, 2/2') : q.sig) + ')';
  return (LANG === 'ko' ? TS_METER_NAME[q.answer]() : TS_METER_NAME[q.answer]().toLowerCase() + ' time') + ' (' + q.sig + ')';
}
Object.assign(TIMESIG_DRILL, { levels: TS_LEVELS, generate: genTsQuestion, check: tsCheck, answerLabel: tsAnswerLabel, Question: TsQuestion, Learn: TsLearn });
