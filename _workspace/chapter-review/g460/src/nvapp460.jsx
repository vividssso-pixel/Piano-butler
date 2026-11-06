// ─── Phase 460: chapter 5 on screen: what moves on each page (B12), the book as the online lesson, the drill (B10) ───
// A row is a list of [kind, beats]: 'w' semibreve 4, 'hd' dotted minim 3, 'h' minim 2, 'q' crotchet 1, 'p' two quavers on
// one beat, 'r' crotchet rest 1, 'hr' minim rest 2, 'wr' semibreve rest 4. Everything is booked on the audio clock like
// chapter 3 (plRun, plMatch, PlPad); the click says 1 2 3 4, and 'and' between when the sound settings ask for a voice.
const NV_BPM = 66;
const nvRestKind = (k) => k === 'r' || k === 'hr' || k === 'wr';
const nvBeats = (row) => row.reduce((a, x) => a + x[1], 0);
// each sound of a row: b its start in beats, d its length, j the item, h which quaver of a pair
function nvSounds(row) {
  const out = []; let b = 0;
  row.forEach(([k, n], j) => { if (k === 'p') out.push({ b, d: 0.5, j, h: 0 }, { b: b + 0.5, d: 0.5, j, h: 1 }); else if (!nvRestKind(k)) out.push({ b, d: n, j, h: 0 }); b += n; });
  return out;
}
// 4 clicks to get ready, then the row: its notes on middle C (none when the child taps them), 'and' over a pair's beat
function nvRunRow(row, o = {}) {
  const n = nvBeats(row), snd = nvSounds(row), pairs = new Set(snd.filter(s => s.h === 1).map(s => Math.round(s.b - 0.5)));
  return plRun(4 + n, { bpm: NV_BPM, vol: o.vol != null ? o.vol : 0.24, extra: (ctx, tm, i, spb) => {
    if (i < 4) return;
    const b = i - 4;
    if (!o.silent) snd.filter(s => Math.floor(s.b + 1e-9) === b).forEach(s => blip(ctx, tm + (s.b - b) * spb, 261.63, Math.max(0.1, s.d * spb * 0.92), 0.2, 'triangle'));
    if (pairs.has(b) && SOUND.count === 'voice') sayCount(ctx, tm + spb / 2, 'and', 0.8);
  } });
}
const nvWord = (k) => k === 'p' ? t('run-ning', '달리기') : t('walk', '걷기');

// one bar, drawn like the book: each note (or rest), its sound line, a heart on every beat, the count under it (held
// beats lighter, a rest's beats in dashed circles). grow: { sound index: seconds } the lines growing now (on screen);
// lit: the beat sounding; arrow: an item marked from above; marks: '✓' | '?' under each sound; words: walk / run-ning
function NvBar({ row, D = 88, grow = null, lit = -1, arrow = null, marks = null, words = false, count = true, maxW = 470 }) {
  const n = nvBeats(row), P = 12, W = P * 2 + n * D, H = (b) => P + D * (b + 0.5);
  const yN = 56, yL = 74, yW = 96, yH = words ? 118 : 100, yC = yH + 32, yM = yC + 24, HT = (marks ? yM : yC) + 10;
  const raw = [], lines = [], counts = [], held = new Set(), rest = new Set(), pairAt = new Set();
  const sx = (s) => s.h === 0 && row[s.j][0] === 'p' ? H(s.b) - 15 : s.h === 1 ? H(Math.floor(s.b)) + 11 : H(s.b);
  let b = 0;
  row.forEach(([k, len], j) => {
    if (k === 'p') { raw.push(nvbPair(H(b) - 15, H(b) + 11, yN, { k: 0.92 }).svg); pairAt.add(b); }
    else if (k === 'r') { raw.push(nvbRest(H(b) + 1, yN - 12, 'q').svg); rest.add(b); }
    else if (k === 'hr' || k === 'wr') { const xm = (H(b) + H(b + len - 1)) / 2; raw.push(nvbRest(xm, k === 'hr' ? yN - 2 : yN - 14, k === 'hr' ? 'h' : 'w', { k: 1.3 }).svg); for (let i = 0; i < len; i++) rest.add(b + i); }
    else { raw.push(nvbNote(k === 'w' ? H(b) - 1 : H(b) - 3, yN, k === 'hd' ? 'h' : k, { dot: k === 'hd' }).svg); for (let i = 1; i < len; i++) held.add(b + i); }
    if (arrow && arrow[0] === j) { const ax = k === 'p' ? (arrow[1] ? H(b) + 11 : H(b) - 15) : k === 'w' ? H(b) - 1 : H(b) - 3; raw.push('<path d="M' + pFix(ax - 7) + ' 4 L' + pFix(ax + 7) + ' 4 L' + pFix(ax) + ' 13 Z" fill="' + BK.coral + '"/>'); }
    b += len;
  });
  nvSounds(row).forEach((s, k) => {
    const len = row[s.j][0] === 'p' ? 0.5 : s.d, x0 = row[s.j][0] === 'p' ? (s.h ? H(Math.floor(s.b)) + 3 : H(s.b) - D / 2 + 6) : H(s.b) - D / 2 + 6;
    const x1 = row[s.j][0] === 'p' ? (s.h ? H(Math.floor(s.b)) + D / 2 - 6 : H(s.b) - 3) : H(s.b + len - 1) + D / 2 - 6;
    const g = grow && grow[k];
    lines.push(<g key={'l' + k}>
      {grow && <line x1={x0} x2={x1} y1={yL} y2={yL} stroke={BK.coral} strokeOpacity="0.2" strokeWidth="4" strokeLinecap="round"/>}
      <line x1={x0} x2={x1} y1={yL} y2={yL} stroke={BK.coral} strokeWidth="4" strokeLinecap="round"
        style={grow ? { transformBox: 'fill-box', transformOrigin: 'left center', transform: g ? 'scaleX(1)' : 'scaleX(0)', transition: g ? 'transform ' + g.toFixed(2) + 's linear' : 'none' } : undefined}/>
      {marks && marks[k] && <text x={sx(s)} y={yM} textAnchor="middle" fontSize="15" fontWeight="900" fill={marks[k] === '✓' ? BK.green : BK.coral}>{marks[k]}</text>}
    </g>);
  });
  for (let i = 0; i < n; i++) {
    const on = i === lit, x = H(i);
    counts.push(<g key={'c' + i}>
      <path d="M0 5 Q-7.5 -0.5 -5 -4.2 Q-2.4 -6.8 0 -3 Q2.4 -6.8 5 -4.2 Q7.5 -0.5 0 5 Z" transform={'translate(' + x + ' ' + yH + ') scale(1.7)'} fill={on ? BK.coral : '#fff'} stroke={BK.coral} strokeWidth="0.9" strokeLinejoin="round"/>
      {count && rest.has(i) && <circle cx={x} cy={yC - 6} r="13" fill="#fff" stroke={BK.ink} strokeWidth="1.6" strokeDasharray="3.6 3"/>}
      {count && <text x={pairAt.has(i) ? x - 15 : x} y={yC} textAnchor="middle" fontSize="17" fontWeight="900" fill={on ? BK.coral : held.has(i) ? 'rgba(38,41,107,0.38)' : BK.ink}>{i % 4 + 1}</text>}
      {count && pairAt.has(i) && <text x={x + 11} y={yC} textAnchor="middle" fontSize="17" fontWeight="900" fill={on ? BK.coral : BK.ink}>+</text>}
    </g>);
  }
  let wb = 0;
  const wordEls = words ? row.map(([k, len], j) => { const x = H(wb); wb += len; return nvRestKind(k) ? null : <text key={'w' + j} x={x} y={yW} textAnchor="middle" fontSize="14" fontWeight="900" fill={BK.ink}>{nvWord(k)}</text>; }) : null;
  return <svg viewBox={'0 0 ' + W + ' ' + HT} style={{width:'100%',maxWidth:maxW,display:'block',margin:'0 auto'}}>
    <g dangerouslySetInnerHTML={{ __html: raw.join('') }}/>
    {lines}{wordEls}{counts}
  </svg>;
}

// ── each page's rhythms: the book's own tasks (pages 2 to 6) ──
const NV_PAGE_ROWS = {
  2: [[() => t('Crotchets', '4분음표'), [['q', 1], ['q', 1], ['q', 1], ['q', 1]]]],
  3: [[() => t('Two minims', '2분음표 둘'), [['h', 2], ['h', 2]]], [() => t('Crotchet, crotchet, minim', '4분음표, 4분음표, 2분음표'), [['q', 1], ['q', 1], ['h', 2]]]],
  4: [[() => t('Dotted minim, crotchet', '점2분음표, 4분음표'), [['hd', 3], ['q', 1]]], [() => t('Semibreve', '온음표'), [['w', 4]]]],
  5: [[() => t('walk, run-ning, walk, run-ning', '걷기, 달리기, 걷기, 달리기'), [['q', 1], ['p', 1], ['q', 1], ['p', 1]]], [() => t('run-ning, run-ning, walk, walk', '달리기, 달리기, 걷기, 걷기'), [['p', 1], ['p', 1], ['q', 1], ['q', 1]]]],
  6: [[() => t('A crotchet rest on 3', '3에 4분쉼표'), [['q', 1], ['q', 1], ['r', 1], ['q', 1]]], [() => t('Minim, minim rest', '2분음표, 2분쉼표'), [['h', 2], ['hr', 2]]]],
};
const NV_PAD_TITLE = { 2: () => t('Walk the crotchets', '4분음표 걷기'), 3: () => t('Play, then hold', '치고, 누르고 있어요'), 4: () => t('Hold 3 beats, hold 4', '3박, 4박 누르기'), 5: () => t('Walk and run', '걷고, 달려요'), 6: () => t('Count the silence', '쉬면서 세요') };
// listen: the sound lines grow while each note sounds; tap it: the click goes on and you tap every note
function NvPad({ page }) {
  const rows = NV_PAGE_ROWS[page];
  const T = usePlTimers();
  const [ri, setRi] = useState(0);
  const [mode, setMode] = useState(null);   // null | 'listen' | 'tap'
  const [phase, setPhase] = useState('ready');   // ready | count | go | done
  const [lit, setLit] = useState(-1);
  const [count, setCount] = useState(0);
  const [grow, setGrow] = useState({});
  const [res, setRes] = useState(null);
  const run = useRef(null), taps = useRef([]);
  const row = rows[ri][1], snd = nvSounds(row), n = nvBeats(row);
  function reset(i) { T.clear(); stopClicks(); setRi(i); setRes(null); setGrow({}); setLit(-1); setPhase('ready'); setMode(null); }
  function start(m) {
    T.clear(); setRes(null); setGrow({}); setLit(-1); taps.current = []; setMode(m);
    const r = nvRunRow(row, { silent: m === 'tap' }); if (!r) return; run.current = r;
    r.at.forEach((a, i) => T.at(r, a, () => { if (i < 4) { setCount(i + 1); setPhase('count'); } else { setLit(i - 4); setPhase('go'); } }));
    snd.forEach((s, k) => T.at(r, r.at[4] + s.b * r.spb, () => setGrow(g => ({ ...g, [k]: s.d * r.spb * 0.98 }))));
    T.at(r, r.at[4] + n * r.spb + 0.05, () => {
      setLit(-1); setPhase('done');
      if (m !== 'tap') return;
      const want = snd.map(s => r.at[4] + s.b * r.spb), tol = Math.min(PL_TOL, r.spb * 0.22), mm = plMatch(want, taps.current, tol);
      const early = taps.current.filter(tp => tp < r.at[4] - tol).length;
      setRes({ hits: mm.hits, total: mm.total, extra: Math.max(0, mm.extra - early), marks: mm.offs.map(o => o === null ? '?' : '✓') });
    });
    setPhase('count'); setCount(0);
  }
  const tap = React.useCallback(() => {
    const r = run.current; if (!r || mode !== 'tap' || (phase !== 'count' && phase !== 'go')) return;
    taps.current.push(r.now());
    const ctx = getAudio(); if (ctx) blip(ctx, ctx.currentTime, 261.63, 0.16, 0.16, 'triangle');
  }, [phase, mode]);
  const ok = res && res.hits === res.total && res.extra === 0;
  const live = phase === 'count' || phase === 'go';
  return (
    <div className="try-box" style={actBox} data-nv={'pad' + page}>
      <div style={actTitle}>{NV_PAD_TITLE[page]()}</div>
      <div style={actNote}>{LANG === 'ko'
        ? <>먼저 <b>들어 봐요</b>: 음이 울리는 동안 소리 줄이 자라요. 그다음 <b>쳐 봐요</b>: 클릭 4번을 듣고, 음마다 한 번씩 쳐요{page === 6 ? <>. 쉼표에서는 치지 않고 세요</> : null}. 소리 내어 세요.</>
        : <>First <b>listen</b>: each sound line grows while its note sounds. Then <b>tap it</b>: 4 clicks to get ready, then tap once for each note{page === 6 ? <>, and count through the rests</> : null}. Count out loud.</>}</div>
      {rows.length > 1 && <div style={{display:'flex',gap:5,justifyContent:'center',flexWrap:'wrap',marginBottom:8}}>{rows.map(([nm], i) => <button key={i} className={'chip' + (i === ri ? ' active' : '')} onClick={() => reset(i)}>{nm()}</button>)}</div>}
      <NvBar row={row} grow={grow} lit={lit} marks={res ? res.marks : null} words={page === 2 || page === 5}/>
      <div style={{textAlign:'center',fontSize:13,fontWeight:800,color:BK.muted,minHeight:18,margin:'2px 0 4px'}}>{phase === 'count' ? t('Get ready: ', '준비: ') + count : phase === 'go' ? (mode === 'tap' ? t('Tap!', '쳐요!') : t('Listen and count', '들으면서 세요')) : ''}</div>
      <div style={{display:'flex',gap:6,justifyContent:'center',marginBottom:8}}>
        <button className="ghost-btn" onClick={() => start('listen')}>{t('▶ Listen', '▶ 듣기')}</button>
        <button className="ghost-btn" onClick={() => start('tap')}>{t('▶ Tap it', '▶ 쳐 보기')}</button>
      </div>
      {mode === 'tap' && <PlPad on={live} onTap={tap} label={t('TAP EACH NOTE', '음마다 쳐요')}/>}
      {res && <div style={{textAlign:'center',fontSize:14.5,fontWeight:900,marginTop:6,color:ok ? BK.green : BK.coral}}>{t('Notes on time: ' + res.hits + ' of ' + res.total + (res.extra ? ' · extra taps: ' + res.extra : ''), '제때 친 음: ' + res.total + '개 중 ' + res.hits + '개' + (res.extra ? ' · 더 친 것: ' + res.extra + '개' : ''))}{ok ? '  ✓' : ''}</div>}
      {mode === 'tap' && plHint()}
    </div>
  );
}

// ── the book on screen: the opener is the lesson's head, every other page a step. Old ticks kept where the idea is
// close: 'Count it out loud' (11) for crotchets, 'Split it' (4) for minims, 'Dotted notes' (6) for longer notes,
// 'One beat = one apple' (5) for quavers, 'Same name for the note and the rest' (1) for rests. ──
const NV_STORE = [11, 4, 6, 5, 1, 12];
function NvLearn({ onStart }) {
  const pages = nvLbPages(true);
  const opener = pages[0];
  return (
    <Lesson id="note-values" title={t('Notes & Rests', '음표와 쉼표')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="note-values"><div className="lb-screen lb-open" style={{display:'flex',flexDirection:'column',gap:12,margin:'0 0 8px'}}>{lbWordsFirst(opener.props.children)}</div></BkChapterCtx.Provider></LbScreenCtx.Provider>}>
      {pages.slice(1).map((pg, i) => (
        <Step key={i} storeAs={NV_STORE[i]} title={pg.props.title}>
          <LbScreenPage page={pg}/>
        </Step>
      ))}
    </Lesson>
  );
}

// ── the drill (B10): six levels for this room, then three higher ones, each marked with its grade ──
// (AMEB Theory: single quavers at Grade 1, semiquavers and other dotted notes at Grade 2; ABRSM: both at Grade 1, the
// breve and double dots at Grade 4.)
const NV_LEVELS = [
  { n: 1, label: 'Name the note', kind: 'name', time: 8 },
  { n: 2, label: 'How many beats?', kind: 'beats', time: 8 },
  { n: 3, label: 'Find the matching rest', kind: 'rest', time: 8 },
  { n: 4, label: 'Tap the rhythm', kind: 'tap', time: 24, noPrint: true },
  { n: 5, label: 'Which count?', kind: 'count', time: 10 },
  { n: 6, label: 'Rests: tap, then count the silence', kind: 'tapr', time: 24, noPrint: true },
  { n: 7, label: 'Dotted crotchets & single quavers (Grades 1 and 2)', kind: 'g1', time: 10 },
  { n: 8, label: 'Semiquavers: add them up (Grades 1 and 2)', kind: 'g2', time: 12 },
  { n: 9, label: 'The breve & double dots (Grade 4)', kind: 'g4', time: 10 },
];
Object.assign(LEVEL_KO, {
  'Name the note': '음표 이름 맞히기', 'How many beats?': '몇 박일까요?', 'Tap the rhythm': '리듬 치기', 'Which count?': '몇에서 칠까요?',
  'Rests: tap, then count the silence': '쉼표: 치고, 쉬면서 세요', 'Dotted crotchets & single quavers (Grades 1 and 2)': '점4분음표와 8분음표 하나 (1, 2급)',
  'Semiquavers: add them up (Grades 1 and 2)': '16분음표: 박을 더해요 (1, 2급)', 'The breve & double dots (Grade 4)': '겹온음표와 겹점 (4급)',
});
// the room's notes and rests, with their names
const NV_ROOM = {
  w: { b: 4, get name() { return t('semibreve', '온음표'); }, other: 'whole note' },
  h: { b: 2, get name() { return t('minim', '2분음표'); }, other: 'half note' },
  hd: { b: 3, get name() { return t('dotted minim', '점2분음표'); }, other: 'dotted half note' },
  q: { b: 1, get name() { return t('crotchet', '4분음표'); }, other: 'quarter note' },
  p: { b: 1, get name() { return t('two quavers', '8분음표 둘'); }, other: 'eighth notes' },
  r: { b: 1, get name() { return t('crotchet rest', '4분쉼표'); }, other: 'quarter rest' },
  hr: { b: 2, get name() { return t('minim rest', '2분쉼표'); }, other: 'half rest' },
  wr: { b: 4, get name() { return t('semibreve rest', '온쉼표'); }, other: 'whole rest' },
};
// one note or rest of the room, drawn like the book (the minim and semibreve rests on a little piece of the five lines)
function nvGlyphRaw(kind, ink) {
  const col = ink || PEN_N;
  let svg;
  if (kind === 'p') svg = nvbPair(26, 48, 62, { col }).svg;
  else if (kind === 'r') svg = nvbRest(40, 48, 'q', { col }).svg;
  else if (kind === 'hr' || kind === 'wr') {
    svg = [0, 1, 2, 3, 4].map(i => '<line x1="12" x2="68" y1="' + (24 + i * 9) + '" y2="' + (24 + i * 9) + '" stroke="' + col + '" stroke-opacity="0.45" stroke-width="1.1"/>').join('')
      + '<line x1="12" x2="68" y1="' + (kind === 'hr' ? 42 : 33) + '" y2="' + (kind === 'hr' ? 42 : 33) + '" stroke="' + col + '" stroke-width="1.4"/><rect x="31" y="' + (kind === 'hr' ? 37.5 : 33) + '" width="18" height="4.5" fill="' + col + '"/>';
  } else svg = nvbNote(kind === 'w' ? 40 : 36, kind === 'w' ? 52 : 62, kind === 'hd' ? 'h' : kind, { dot: kind === 'hd', col, k: kind === 'w' ? 1.45 : 1 }).svg;
  return svg;
}
function NvGlyph({ kind, size = 84, ink }) {
  return <svg viewBox="0 10 80 66" style={{width:size * 80 / 66,height:size,display:'inline-block',verticalAlign:'middle'}} dangerouslySetInnerHTML={{ __html: nvGlyphRaw(kind, ink) }}/>;
}
// four beats for the tap levels: a minim on 1 or 3, a dotted minim or a semibreve on 1; level 6 has a rest in every bar
const NV_TAP_BARS = [
  [['q', 1], ['q', 1], ['q', 1], ['q', 1]], [['h', 2], ['h', 2]], [['q', 1], ['q', 1], ['h', 2]], [['h', 2], ['q', 1], ['q', 1]], [['hd', 3], ['q', 1]], [['w', 4]],
  [['q', 1], ['p', 1], ['q', 1], ['p', 1]], [['p', 1], ['p', 1], ['q', 1], ['q', 1]], [['p', 1], ['q', 1], ['h', 2]], [['h', 2], ['p', 1], ['q', 1]], [['q', 1], ['q', 1], ['p', 1], ['q', 1]], [['p', 1], ['p', 1], ['p', 1], ['q', 1]],
];
const NV_REST_BARS = [
  [['q', 1], ['q', 1], ['r', 1], ['q', 1]], [['h', 2], ['hr', 2]], [['q', 1], ['r', 1], ['q', 1], ['r', 1]], [['q', 1], ['q', 1], ['hr', 2]], [['hr', 2], ['h', 2]],
  [['p', 1], ['q', 1], ['r', 1], ['q', 1]], [['h', 2], ['r', 1], ['q', 1]], [['r', 1], ['q', 1], ['q', 1], ['q', 1]], [['q', 1], ['p', 1], ['hr', 2]],
];
const NV_COUNTS = ['1', '1 +', '2', '2 +', '3', '3 +', '4', '4 +'];
// the extra levels use the app's old note shapes (Glyph), with the breve and double dots added for level 9
const NV_BREVE = { id: 'breve', us: 'double whole', base: 8 };
const NV_HI = {
  g1: () => [NV_DOTTED[1], NV_NOTES[3], NV_RESTS[3], NV_DOTTED[0], NV_NOTES[2], NV_RESTS[2], NV_DOTTED[2]],
  g2: () => [NV_NOTES[4], NV_RESTS[4], NV_NOTES[3], NV_DOTTED[2], NV_NOTES[2], NV_DOTTED[1]],
  g4: () => [nvItem(NV_BREVE), nvItem(NV_BREVE, { rest: true }), nvItem(NOTE_VALUES[1], { dd: true }), nvItem(NOTE_VALUES[2], { dd: true }), nvItem(NOTE_VALUES[0], { dot: true }), NV_DOTTED[0], NV_NOTES[0]],
};
function genNvQuestion(lv, prev) {
  const uid = Math.random();
  const notPrev = (list, keyOf) => { let x = pick(list), g = 0; while (prev && prev.key === keyOf(x) && g++ < 12) x = pick(list); return x; };
  if (lv.kind === 'name') {
    const k = notPrev(['w', 'h', 'hd', 'q', 'p'], x => 'n' + x);
    return { kind: 'name', glyph: k, key: 'n' + k, answer: k, choices: shuffle([k, ...sampleN(['w', 'h', 'hd', 'q', 'p'].filter(x => x !== k), 3)]), uid };
  }
  if (lv.kind === 'beats') {
    const k = notPrev(['w', 'h', 'hd', 'q', 'p', 'r', 'hr', 'wr'], x => 'b' + x);
    return { kind: 'beats', glyph: k, key: 'b' + k, answer: NV_ROOM[k].b, choices: [1, 2, 3, 4], uid };
  }
  if (lv.kind === 'rest') {
    const k = notPrev(['w', 'h', 'q'], x => 'r' + x);
    return { kind: 'rest', glyph: k, key: 'r' + k, answer: { w: 'wr', h: 'hr', q: 'r' }[k], choices: shuffle(['r', 'hr', 'wr']), uid };
  }
  if (lv.kind === 'tap' || lv.kind === 'tapr') {
    const bars = lv.kind === 'tap' ? NV_TAP_BARS : NV_REST_BARS;
    const i = notPrev(bars.map((_, j) => j), x => lv.kind + x);
    return { kind: lv.kind, row: bars[i], key: lv.kind + i, uid };
  }
  if (lv.kind === 'count') {
    let row, j, g = 0;
    let h = 0;
    do { row = pick(NV_TAP_BARS.slice(1).concat(NV_REST_BARS.slice(1))); const items = row.map((x, k) => k).filter(k => !nvRestKind(row[k][0])); j = pick(items); h = row[j][0] === 'p' && Math.random() < 0.6 ? 1 : 0; } while (prev && prev.key === 'c' + row.map(x => x[0]).join() + j + h && g++ < 12);
    const at = row.slice(0, j).reduce((a, x) => a + x[1], 0) + h / 2, ans = NV_COUNTS[at * 2];
    const others = sampleN(NV_COUNTS.filter(c => c !== ans), 3);
    return { kind: 'count', row, arrow: [j, h], key: 'c' + row.map(x => x[0]).join() + j + h, answer: ans, choices: NV_COUNTS.filter(c => c === ans || others.includes(c)), uid };
  }
  // the higher levels: how many beats (g1, g4) or add two of them up (g2)
  const pool = NV_HI[lv.kind]();
  if (lv.kind === 'g2') {
    const a = pick(pool), b = pick(pool), total = a.beats + b.beats;
    const cands = [...new Set([total - 0.25, total + 0.25, total - 0.5, total + 0.5, total + 1, total * 2].filter(v => v > 0 && Math.abs(v - total) > 1e-9))];
    return { kind: 'sum', a, b, key: 'g2' + a.key + b.key, answer: total, choices: shuffle([total, ...sampleN(cands, 3)]), uid };
  }
  const it = notPrev(pool, x => lv.kind + x.key);
  const vals = [...new Set(pool.map(x => x.beats).concat(lv.kind === 'g4' ? [2, 7, 12] : [0.25, 2, 0.75]))].filter(v => Math.abs(v - it.beats) > 1e-9);
  return { kind: 'hbeats', item: it, key: lv.kind + it.key, answer: it.beats, choices: shuffle([it.beats, ...sampleN(vals, 3)]).sort((x, y) => x - y), uid };
}
const nvRoomName = (k) => NV_ROOM[k].name;
const nvOther = (k) => k === 'p' ? 'Their other name is eighth notes.' : 'Its other name is a ' + NV_ROOM[k].other + '.';
function NvQuestion({ q, given, locked, onAnswer, pixel }) {
  const board = useBoard(q, given);
  const T = usePlTimers();
  const [phase, setPhase] = useState('ready');
  const [lit, setLit] = useState(-1);
  const [grow, setGrow] = useState({});
  const run = useRef(null), taps = useRef([]);
  const done = !!given;
  const ink = pixel ? '#faf6ec' : '#26296b';
  const btnCls = pixel ? 'pixel-choice' : 'choice-btn';
  const prompt = (txt) => <p style={pixel ? {fontSize:11.5,textAlign:'center',margin:'0 0 10px',lineHeight:1.7} : {fontSize:15,fontWeight:700,textAlign:'center',margin:'0 0 10px',color:'var(--muted)'}}>{txt}</p>;
  const st = (c) => !done ? '' : (c === q.answer || (typeof c === 'number' && Math.abs(c - q.answer) < 1e-9) ? ' good' : (given.ans === c ? ' bad' : ''));
  useEffect(() => { T.clear(); stopClicks(); setPhase('ready'); setLit(-1); setGrow({}); taps.current = []; }, [q.uid]);
  if (q.kind === 'tap' || q.kind === 'tapr') {
    const snd = nvSounds(q.row), n = nvBeats(q.row);
    function start() {
      if (done || phase !== 'ready') return;
      T.clear(); taps.current = []; setGrow({});
      const r = nvRunRow(q.row, { silent: true }); if (!r) return; run.current = r;
      r.at.forEach((a, i) => T.at(r, a, () => { setPhase(i < 4 ? 'count' : 'go'); setLit(i < 4 ? -1 : i - 4); }));
      snd.forEach((s, k) => T.at(r, r.at[4] + s.b * r.spb, () => setGrow(g => ({ ...g, [k]: s.d * r.spb * 0.98 }))));
      T.at(r, r.at[4] + n * r.spb + 0.05, () => {
        setPhase('scoring'); setLit(-1);
        const want = snd.map(s => r.at[4] + s.b * r.spb), tol = Math.min(PL_TOL, r.spb * 0.22), m = plMatch(want, taps.current, tol);
        const early = taps.current.filter(tp => tp < r.at[4] - tol).length, extra = Math.max(0, m.extra - early);
        onAnswer({ ok: m.hits === m.total && extra === 0, hits: m.hits, total: m.total, extra, marks: m.offs.map(o => o === null ? '?' : '✓') });
      });
      setPhase('count');
    }
    const onTap = () => { const r = run.current; if (r && (phase === 'count' || phase === 'go')) { taps.current.push(r.now()); const ctx = getAudio(); if (ctx) blip(ctx, ctx.currentTime, 261.63, 0.16, 0.16, 'triangle'); } };
    const res = done && given.ans && typeof given.ans === 'object' ? given.ans : null;
    return <div>
      <BoardTrack b={board} pixel={pixel}/>
      {prompt(q.kind === 'tap' ? t('4 clicks to get ready, then tap once for each note. Count out loud.', '클릭 4번을 듣고, 음마다 한 번씩 쳐요. 소리 내어 세요.') : t('Tap the notes. In a rest, don’t tap: count the silence.', '음을 쳐요. 쉼표에서는 치지 말고 쉬면서 세요.'))}
      <div style={{background:pixel ? '#faf6ec' : 'transparent',borderRadius:8,padding:pixel ? 6 : 0}}><NvBar row={q.row} grow={phase === 'ready' && !done ? null : grow} lit={lit} marks={res ? res.marks : null} maxW={430}/></div>
      <div style={{textAlign:'center',fontSize:13,fontWeight:800,color:pixel ? '#faf6ec' : BK.muted,minHeight:18,margin:'2px 0 4px'}}>{phase === 'count' ? t('Get ready…', '준비…') : phase === 'go' ? t('Tap!', '쳐요!') : ''}</div>
      {!done && phase === 'ready' && <div style={{textAlign:'center',marginBottom:8}}><button className={pixel ? 'pixel-btn' : 'ghost-btn'} onClick={start} style={{fontSize:15,padding:'10px 18px'}}>{t('▶ Start', '▶ 시작')}</button></div>}
      {!done && <PlPad on={phase === 'count' || phase === 'go'} onTap={onTap} h={64}/>}
      {res && <div style={{textAlign:'center',fontSize:15,fontWeight:900,marginTop:8,color:res.ok ? BK.green : BK.coral}}>{t('Notes on time: ' + res.hits + ' of ' + res.total + (res.extra ? ' · extra taps: ' + res.extra : ''), '제때 친 음: ' + res.total + '개 중 ' + res.hits + '개' + (res.extra ? ' · 더 친 것: ' + res.extra + '개' : ''))}</div>}
    </div>;
  }
  let body;
  if (q.kind === 'name') body = <>
    {prompt(t('What is this note called?', '이 음표의 이름은?'))}
    <div style={{textAlign:'center',margin:'0 0 12px'}}><NvGlyph kind={q.glyph} ink={ink} size={96}/></div>
    <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:8}}>{q.choices.map(c => <button key={c} disabled={locked} onClick={() => onAnswer(c)} className={btnCls + st(c)} style={{padding:'12px 4px'}}>{cap(nvRoomName(c))}</button>)}</div>
    {done && LANG !== 'ko' && !pixel && <div style={{textAlign:'center',fontSize:13,color:'var(--muted)',marginTop:8}}>{nvOther(q.answer)}</div>}
  </>;
  else if (q.kind === 'beats') body = <>
    {prompt(t('How many beats does it last?', '몇 박일까요?'))}
    <div style={{textAlign:'center',margin:'0 0 12px'}}><NvGlyph kind={q.glyph} ink={ink} size={96}/></div>
    {done && !pixel && <div style={{textAlign:'center',fontSize:13,color:'var(--muted)',margin:'-6px 0 10px'}}>{cap(nvRoomName(q.glyph))}</div>}
    <div style={{display:'grid',gridTemplateColumns:'repeat(4,1fr)',gap:8}}>{q.choices.map(v => <button key={v} disabled={locked} onClick={() => onAnswer(v)} className={btnCls + st(v)} style={{padding:'14px 2px'}}>{fmtBeats(v)}</button>)}</div>
  </>;
  else if (q.kind === 'rest') body = <>
    {prompt(t('Which rest lasts just as long?', '똑같은 길이의 쉼표는?'))}
    <div style={{textAlign:'center',margin:'0 0 12px'}}><NvGlyph kind={q.glyph} ink={ink} size={96}/></div>
    <div style={{display:'grid',gridTemplateColumns:'repeat(3,1fr)',gap:8}}>{q.choices.map(c => <button key={c} disabled={locked} onClick={() => onAnswer(c)} className={btnCls + st(c)} style={{padding:'8px 2px'}} aria-label={nvRoomName(c)}><NvGlyph kind={c} size={56} ink={pixel ? '#faf6ec' : undefined}/>{done && !pixel && <span style={{display:'block',fontSize:12,fontWeight:700}}>{nvRoomName(c)}</span>}</button>)}</div>
  </>;
  else if (q.kind === 'count') body = <>
    {prompt(t('The arrow points to a note. On which count do you play it?', '화살표가 가리키는 음표는 몇에서 칠까요?'))}
    <div style={{background:pixel ? '#faf6ec' : 'transparent',borderRadius:8,padding:pixel ? 6 : 0,margin:'0 0 10px'}}><NvBar row={q.row} arrow={q.arrow} count={false} maxW={430}/></div>
    <div style={{display:'grid',gridTemplateColumns:'repeat(4,1fr)',gap:8}}>{q.choices.map(c => <button key={c} disabled={locked} onClick={() => onAnswer(c)} className={btnCls + st(c)} style={{padding:'14px 2px',fontSize:pixel ? 10 : 18}}>{c}</button>)}</div>
  </>;
  else if (q.kind === 'sum') body = <>
    {prompt(t('How many beats altogether?', '모두 몇 박일까요?'))}
    <div style={{display:'flex',justifyContent:'center',alignItems:'center',gap:6,margin:'0 0 12px',color:ink}}><Glyph item={q.a} ink={ink} size={84}/><span style={{fontSize:30,fontWeight:900}}>+</span><Glyph item={q.b} ink={ink} size={84}/><span style={{fontSize:30,fontWeight:900}}>= ?</span></div>
    <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:8}}>{q.choices.map(v => <button key={v} disabled={locked} onClick={() => onAnswer(v)} className={btnCls + st(v)} style={{padding:'14px 4px'}}>{fmtBeats(v)}</button>)}</div>
  </>;
  else body = <>
    {prompt(t('How many crotchet beats does it last?', '4분음표 박으로 몇 박일까요?'))}
    <div style={{textAlign:'center',margin:'0 0 12px'}}><Glyph item={q.item} ink={ink} size={96}/></div>
    {done && !pixel && <div style={{textAlign:'center',fontSize:13,color:'var(--muted)',margin:'-6px 0 10px'}}>{LANG === 'ko' ? q.item.ko : cap(q.item.uk) + '. Its other name is a ' + q.item.us + '.'}</div>}
    <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:8}}>{q.choices.map(v => <button key={v} disabled={locked} onClick={() => onAnswer(v)} className={btnCls + st(v)} style={{padding:'14px 4px'}}>{fmtBeats(v)}</button>)}</div>
  </>;
  return <div><BoardTrack b={board} pixel={pixel}/>{body}</div>;
}
function nvCheck(q, ans) {
  if (ans === null || ans === undefined) return false;
  if (q.kind === 'tap' || q.kind === 'tapr') return !!(ans && ans.ok);
  if (typeof q.answer === 'number') return typeof ans === 'number' && Math.abs(ans - q.answer) < 1e-9;
  return ans === q.answer;
}
const nvBarWords = (row) => row.map(([k]) => nvRoomName(k)).join(', ');
function nvAnswerLabel(q) {
  if (q.kind === 'name') return cap(nvRoomName(q.answer)) + (LANG === 'ko' ? '' : '. ' + nvOther(q.answer));
  if (q.kind === 'beats') return fmtBeats(q.answer);
  if (q.kind === 'rest') return LANG === 'ko' ? nvRoomName(q.answer) : 'a ' + nvRoomName(q.answer);
  if (q.kind === 'tap') return t('a tap for each note: ', '음마다 한 번: ') + nvSounds(q.row).length + t(' taps', '번');
  if (q.kind === 'tapr') return t('a tap for each note, none in the rests: ', '음마다 한 번, 쉼표에서는 안 쳐요: ') + nvSounds(q.row).length + t(' taps', '번');
  if (q.kind === 'count') return q.answer;
  return fmtBeats(q.answer);
}
Object.assign(NOTEVAL_DRILL, { levels: NV_LEVELS, generate: genNvQuestion, check: nvCheck, answerLabel: nvAnswerLabel, Question: NvQuestion, Learn: NvLearn });
