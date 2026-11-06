// ─── Phase 470: chapter 14's sound, the pads of pages 2 to 6, the screen lesson and the drill ───
const SRH_BPM = 72, SRH_HZ = 392;   // every note on G above middle C
// a full bar of clicks, then the beats an anacrusis leaves out, then the row: its notes on G (none while the child taps
// them). With the spoken count on, the voice says the count of every beat, and 'and' on every + that has a note or rest.
// An anacrusis here always starts on a beat (from: whole beats).
function srhRun(items, o = {}) {
  const top = srhTop(items), from = Math.round(o.from || 0), lead = top + from, n = Math.ceil(srhBeats(items) - 1e-6), snd = srhSounds(items);
  const vol = 0.24, voice = SOUND.count === 'voice';
  const r = plRun(lead + n, { bpm: o.bpm || SRH_BPM, vol, silentFrom: 0, extra: (ctx, tm, i, spb) => {
    const pos = i < top ? i : i < lead ? i - top : (i - lead + from) % top;
    if (!(voice && sayCount(ctx, tm, String(pos + 1), 1))) metroClick(ctx, tm, false, vol);
    if (i < lead) return;
    const b = i - lead;
    snd.filter(s => s.b > b - 1e-9 && s.b < b + 1 - 1e-9).forEach(s => {
      if (!o.silent && !s.rest) blip(ctx, tm + (s.b - b) * spb, SRH_HZ, Math.max(0.08, s.d * spb * 0.9), 0.2, 'triangle');
      if (voice && Math.abs(s.b - b - 0.5) < 1e-6) sayCount(ctx, tm + spb / 2, 'and', 0.8);
    });
  } });
  if (r) r.lead = lead;
  return r;
}
// which tap answers each note (the nearest free tap within the tolerance), or -1
function srhMatch(want, taps, tols) {
  const used = new Set();
  return want.map((e, k) => { const tol = tols[k]; let best = -1, bd = 1e9; taps.forEach((tp, j) => { if (used.has(j)) return; const d = Math.abs(tp - e); if (d < bd) { bd = d; best = j; } });
    if (best >= 0 && bd <= tol) { used.add(best); return best; } return -1; });
}
// a tapped row, scored: on time (the press) and held right (a crotchet held at least about half a beat, a longer note
// to within 0.4 of a beat of its end; a note before a rest let go by the rest). marks: ✓ both, ? missed, – on time but held wrong.
function srhScore(snd, go, spb, taps, rels, endT) {
  // a note on a beat may land a little further off than a note between beats (quavers must stay even)
  const notes = snd.map((s, i) => i).filter(i => !snd[i].rest), tol = Math.min(PL_TOL, spb * 0.22), tols = notes.map(i => Math.abs(snd[i].b % 1) < 1e-6 ? tol : Math.min(tol, spb * 0.15));
  const want = notes.map(i => go + snd[i].b * spb), idx = srhMatch(want, taps, tols);
  const early = taps.filter(tp => tp < go - tol).length, used = idx.filter(j => j >= 0).length, marks = {};
  let hits = 0, held = 0;
  notes.forEach((i, k) => { const j = idx[k]; if (j < 0) { marks[i] = '?'; return; } hits++;
    const s = snd[i], rel = rels[j] != null ? rels[j] : j + 1 < taps.length ? taps[j + 1] : endT, dur = rel - taps[j], nxt = snd[i + 1];
    const longOk = s.d < 1 || dur >= (s.d >= 1.5 ? s.d - 0.4 : 0.55 * s.d) * spb, restOk = !(nxt && nxt.rest) || rel <= want[k] + (s.d + 0.35) * spb;
    if (longOk && restOk) { held++; marks[i] = '✓'; } else marks[i] = '–'; });
  return { hits, held, total: notes.length, extra: Math.max(0, taps.length - used - early), marks, ok: hits === notes.length && held === notes.length && taps.length - used - early <= 0 };
}
const srhResult = (res) => t('On time: ' + res.hits + ' of ' + res.total + ' · held right: ' + res.held + ' of ' + res.total + (res.extra ? ' · extra taps: ' + res.extra : ''),
  '제때 친 음: ' + res.total + '개 중 ' + res.hits + '개 · 길이 맞게: ' + res.total + '개 중 ' + res.held + '개' + (res.extra ? ' · 더 친 것: ' + res.extra + '개' : ''));
// a staff that fills its box, but never wider than the book draws it
const SrhFit = ({ items, o = {}, label, k = 1.3 }) => { const m = srhRaw((d) => dY(d), items, o);
  return <div style={{width:'100%',maxWidth:Math.round((m.last + 6) * k),margin:'0 auto'}}><SrhStaff full items={items} o={o} label={label}/></div>; };

// ── the pads: listen (each note lights up as it sounds), then tap it (a press for each note, held for its length) ──
const SRH_LINE = (n) => t('Line ' + n, n + '번 줄');
const SRH_PAD_ROWS = { 2: [[1, 'l2'], [2, 'right']], 3: [[1, 'alone'], [2, 'aloneB']], 4: [[1, 'dot'], [2, 'dot3']], 5: [[1, 'up4'], [2, 'up3']], 6: [[1, 'mix4'], [2, 'mix3'], [3, 'mix2']] };
const SRH_PAD_TITLE = { 2: () => t('Grouping quavers', '8분음표 묶기'), 3: () => t('Rest, then play', '쉬었다가 치기'), 4: () => t('Long, short', '길게, 짧게'), 5: () => t('Start before beat 1', '첫 박보다 먼저 시작하기'), 6: () => t('Count, clap, play', '세기, 손뼉 치기, 피아노 치기') };
function SrhPad({ page }) {
  const rows = SRH_PAD_ROWS[page];
  const T = usePlTimers();
  const [ri, setRi] = useState(0);
  const [mode, setMode] = useState(null);   // null | 'listen' | 'tap'
  const [phase, setPhase] = useState('ready');   // ready | count | go | done
  const [lit, setLit] = useState(-1);
  const [count, setCount] = useState('');
  const [res, setRes] = useState(null);
  const run = useRef(null), taps = useRef([]), rels = useRef([]), held = useRef(null);
  const key = rows[ri][1], items = SRH_ROWS[key], from = SRH_FROM[key] || 0, top = srhTop(items), snd = srhSounds(items), n = srhBeats(items);
  const stopHeld = () => { if (held.current) { held.current(); held.current = null; } };
  function reset(i) { T.clear(); stopClicks(); stopHeld(); setRi(i); setRes(null); setLit(-1); setPhase('ready'); setMode(null); }
  function start(m) {
    T.clear(); stopHeld(); setRes(null); setLit(-1); taps.current = []; rels.current = []; setMode(m);
    const r = srhRun(items, { from, silent: m === 'tap' }); if (!r) return; run.current = r;
    const go = r.at[r.lead];
    r.at.slice(0, r.lead).forEach((a, i) => T.at(r, a, () => { setPhase('count'); setCount(String(i < top ? i + 1 : i - top + 1)); }));
    T.at(r, go, () => setPhase('go'));
    snd.forEach((s, k) => T.at(r, go + s.b * r.spb, () => setLit(k)));
    T.at(r, go + n * r.spb + 0.05, () => {
      stopHeld(); setLit(-1); setPhase('done');
      if (m === 'tap') setRes(srhScore(snd, go, r.spb, taps.current, rels.current, r.now()));
    });
    setPhase('count'); setCount('');
  }
  const tap = React.useCallback(() => {
    const r = run.current; if (!r || mode !== 'tap' || (phase !== 'count' && phase !== 'go')) return;
    taps.current.push(r.now());
    const ctx = getAudio(); if (ctx) { stopHeld(); held.current = blip(ctx, ctx.currentTime, SRH_HZ, 4.3 * r.spb, 0.18, 'triangle'); }
  }, [phase, mode]);
  const release = React.useCallback(() => { const r = run.current, j = taps.current.length - 1; if (r && j >= 0 && rels.current[j] == null) rels.current[j] = r.now(); stopHeld(); }, []);
  const live = phase === 'count' || phase === 'go';
  const rest = page === 3 || page === 6;
  const hideCount = page === 6 && ri >= 1 && phase !== 'done';   // lines 2 and 3: the child finds the count first
  return (
    <div className="try-box" style={actBox} data-srh={'pad' + page}>
      <div style={actTitle}>{SRH_PAD_TITLE[page]()}</div>
      <div style={actNote}>{LANG === 'ko'
        ? <><b>▶ 듣기</b>: 소리 나는 음표가 주황색으로 켜져요. <b>▶ 쳐 보기</b>: 음표마다 눌러 그 길이만큼 누르고 있어요.{rest ? ' 쉼표에서는 누르지 않아요.' : ''}</>
        : <><b>▶ Listen</b>: each note lights up orange as it sounds. <b>▶ Tap it</b>: press for each note, held for its length.{rest ? ' No press in a rest.' : ''}</>}</div>
      <div style={{display:'flex',gap:5,justifyContent:'center',flexWrap:'wrap',marginBottom:8}}>{rows.map(([ln], i) => <button key={i} className={'chip' + (i === ri ? ' active' : '')} onClick={() => reset(i)}>{SRH_LINE(ln)}</button>)}</div>
      <SrhFit items={items} o={{ D: items.some(x => x[0] === '|') ? 36 : 44, from, lit, marks: res ? res.marks : null, counts: hideCount ? false : undefined }}/>
      <div style={{textAlign:'center',fontSize:13,fontWeight:800,color:BK.muted,minHeight:18,margin:'2px 0 4px'}}>{phase === 'count' ? t('Get ready: ', '준비: ') + count : phase === 'go' ? (mode === 'tap' ? t('Tap!', '쳐요!') : t('Listen and count', '들으면서 세요')) : ''}</div>
      <div style={{display:'flex',gap:6,justifyContent:'center',marginBottom:8}}>
        <button className="ghost-btn" onClick={() => start('listen')}>{t('▶ Listen', '▶ 듣기')}</button>
        <button className="ghost-btn" onClick={() => start('tap')}>{t('▶ Tap it', '▶ 쳐 보기')}</button>
      </div>
      {mode === 'tap' && <PlPad on={live} onTap={tap} onRelease={release} label={t('HOLD EACH NOTE', '음표마다 누르고 있어요')}/>}
      {res && <div style={{textAlign:'center',fontSize:14.5,fontWeight:900,marginTop:6,color:res.ok ? BK.green : BK.coral}}>{srhResult(res)}{res.ok ? '  ✓' : ''}</div>}
      {mode === 'tap' && plHint()}
    </div>
  );
}

// ── the book on screen: the opener is the lesson's head, every other page a step. Old ticks kept where the idea is
// close: 'Grouping notes to show the beat' (7), 'One beat = one apple' (4), 'Dotted notes' (5), 'Anacrusis' (2),
// 'The 40 cards' (0), 'Make your own' (3). ──
const SRH_STORE = [7, 4, 5, 2, 0, 3];
function SrhLearn({ onStart }) {
  const pages = srhLbPages(true);
  const opener = pages[0];
  return (
    <Lesson id="rhythm" title={bkChapterName('rhythm')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="rhythm"><div className="lb-screen lb-open" style={{display:'flex',flexDirection:'column',gap:12,margin:'0 0 8px'}}>{lbWordsFirst(opener.props.children)}</div></BkChapterCtx.Provider></LbScreenCtx.Provider>}>
      {pages.slice(1).map((pg, i) => (
        <Step key={i} storeAs={SRH_STORE[i]} title={pg.props.title}>
          <LbScreenPage page={pg}/>
        </Step>
      ))}
    </Lesson>
  );
}

// ── the drill, in the book's order: page 2 (1), pages 2 to 4 (2 to 4), page 5 (5), page 6 (6, 7); 8 and 9 the extras ──
const SRH_LEVELS = [
  { n: 1, label: 'Beamed right?', kind: 'beam', time: 8 },
  { n: 2, label: 'How many beats?', kind: 'beats', time: 8 },
  { n: 3, label: 'Which count?', kind: 'count', time: 10 },
  { n: 4, label: 'Fill the bar', kind: 'fill', time: 10 },
  { n: 5, label: 'Before beat 1', kind: 'up', time: 10 },
  { n: 6, label: 'Listen: which rhythm?', kind: 'ear', time: 14, noPrint: true },
  { n: 7, label: 'Tap the rhythm', kind: 'tap', time: 24, noPrint: true },
  { n: 8, label: 'Extra: semiquavers, 1 e + a', kind: 's16', time: 10 },
  { n: 9, label: 'Extra: syncopation', kind: 'sync', time: 10 },
];
Object.assign(LEVEL_KO, {
  'How many beats?': '몇 박일까요?', 'Beamed right?': '바르게 묶였나요?', 'Which count?': '언제 칠까요?', 'Fill the bar': '마디 채우기',
  'Before beat 1': '첫 박보다 먼저', 'Listen: which rhythm?': '듣기: 어느 리듬?', 'Tap the rhythm': '리듬 치기',
  'Extra: semiquavers, 1 e + a': '더 해 보기: 16분음표, 1 e + a', 'Extra: syncopation': '더 해 보기: 당김음',
});
const srhBar = (top, ...ks) => [['ts', top], ...ks.map(k => Array.isArray(k) ? k : [k]), ['||']];
// level 2: one note, rest or group, and its beats
const SRH_GLYPH_B = { e: 0.5, er: 0.5, q: 1, p: 1, qd: 1.5, qde: 2, h: 2, p4: 2 };
function srhGlyphRaw(k, col = PEN_N) {
  const y = 50, dot = (x) => '<circle cx="' + x + '" cy="' + (y - 3) + '" r="3.6" fill="' + col + '"/>';
  if (k === 'e') return { w: 46, svg: nvbNote(16, y, 'e', { col }).svg };
  if (k === 'er') return { w: 36, svg: srhQuaverRest(20, 33, col, 1.3) };
  if (k === 'q') return { w: 36, svg: nvbNote(16, y, 'q', { col }).svg };
  if (k === 'r') return { w: 36, svg: nvbRest(18, 34, 'q', { col, k: 1.1 }).svg };
  if (k === 'qd') return { w: 46, svg: nvbNote(16, y, 'q', { col }).svg + dot(31) };
  if (k === 'h') return { w: 36, svg: nvbNote(16, y, 'h', { col }).svg };
  if (k === 'p') return { w: 60, svg: srhGroup([16, 42], y, [col, col], 1, col) };
  if (k === 'p4') return { w: 108, svg: srhGroup([16, 40, 64, 88], y, [col, col, col, col], 1, col) };
  if (k === 's4') return { w: 108, svg: srhGroup([16, 40, 64, 88], y, [col, col, col, col], 2, col) };
  return { w: 84, svg: nvbNote(16, y, 'q', { col }).svg + dot(31) + nvbNote(52, y, 'e', { col }).svg };   // qde
}
const SrhGlyph = ({ k, col, h = 64 }) => { const g = srhGlyphRaw(k, col); return <svg viewBox={'0 0 ' + g.w + ' 60'} style={{height:h,width:'auto',maxWidth:'100%',display:'inline-block'}} dangerouslySetInnerHTML={{ __html: g.svg }}/>; };
// level 1: bars beamed right, and bars beamed wrong (across the middle of 4/4, or across a beat)
const SRH_BEAM_OK = [srhBar(4, 'p', 'p', 'q', 'q'), srhBar(4, 'p4', 'q', 'q'), srhBar(4, 'q', 'q', 'p4'), srhBar(4, 'q', 'p', 'p', 'q'), srhBar(4, 'p4', 'p4'), srhBar(3, 'p', 'p', 'p'), srhBar(3, 'q', 'p', 'q'), srhBar(4, 'p', 'q', 'p', 'q'), srhBar(2, 'p', 'p'), srhBar(3, 'q', 'q', 'p')];
const SRH_BEAM_BAD = [[srhBar(4, 'q', 'p4', 'q'), 'mid'], [srhBar(4, 'p', 'p4', 'q'), 'mid'], [srhBar(4, 'q', 'p4', 'p'), 'mid'], [srhBar(4, 'e', 'p', 'e', 'h'), 'beat'], [srhBar(4, 'q', 'e', 'p', 'e', 'q'), 'beat'], [srhBar(3, 'e', 'p', 'e', 'q'), 'beat']];
// level 3 and level 7: one bar to count, or to tap
const SRH_COUNT_BARS = [srhBar(4, 'p', 'p', 'q', 'q'), srhBar(4, 'p4', 'q', 'q'), srhBar(4, 'q', 'q', 'p4'), srhBar(4, 'q', 'p', 'p', 'q'), srhBar(3, 'p', 'p', 'q'), srhBar(4, 'q', 'er', 'e', 'q', 'er', 'e'), srhBar(2, 'e', 'er', 'q'), srhBar(4, 'qd', 'e', 'h'), srhBar(4, 'qd', 'e', 'qd', 'e'), srhBar(3, 'qd', 'e', 'q'), srhBar(4, 'p', 'q', 'qd', 'e'), srhBar(3, 'p', 'qd', 'e'), srhBar(2, 'qd', 'e'), srhBar(4, 'q', 'er', 'e', 'p', 'q')];
// level 4: a bar with a gap (every gap the same width), and what fills it: a quaver, a crotchet, a dotted crotchet or a minim
const SRH_GAP_W = 58;
const SRH_FILL = [[4, ['q', 'q', ['box', 2]], 'h'], [4, [['box', 1.5], 'e', 'h'], 'qd'], [4, ['h', 'q', ['box', 1]], 'q'], [4, ['q', 'q', 'qd', ['box', 0.5]], 'e'], [4, ['p', ['box', 1], 'h'], 'q'], [4, ['qd', 'e', ['box', 2]], 'h'], [4, ['h', ['box', 1.5], 'e'], 'qd'], [4, ['p4', 'q', ['box', 1]], 'q'], [4, ['qd', ['box', 0.5], 'h'], 'e'],
  [3, [['box', 1.5], 'e', 'q'], 'qd'], [3, ['q', ['box', 2]], 'h'], [3, ['p', 'q', ['box', 1]], 'q'], [3, ['qd', ['box', 0.5], 'q'], 'e'], [2, ['qd', ['box', 0.5]], 'e'], [2, [['box', 1.5], 'e'], 'qd'], [2, ['p', ['box', 1]], 'q']];
const SRH_FILL_KS = ['e', 'q', 'qd', 'h'];
const srhGapItems = (top, ks) => srhBar(top, ...ks.map(k => Array.isArray(k) && k[0] === 'box' ? ['box', k[1], SRH_GAP_W] : k));
// level 5: an anacrusis, a full bar, and the short last bar
const SRH_UPS = [[4, ['q'], 3], [4, ['h'], 2], [4, ['p'], 3], [4, ['q', 'q'], 2], [4, ['hd'], 1], [4, ['qd', 'e'], 2], [3, ['q'], 2], [3, ['p'], 2], [3, ['h'], 1], [3, ['q', 'q'], 1], [2, ['q'], 1], [2, ['p'], 1]];
const SRH_FULL = { 4: [['q', 'q', 'q', 'q'], ['h', 'q', 'q'], ['p', 'p', 'h'], ['qd', 'e', 'h'], ['q', 'q', 'h']], 3: [['h', 'q'], ['q', 'q', 'q'], ['p', 'q', 'q'], ['qd', 'e', 'q']], 2: [['q', 'q'], ['p', 'q'], ['qd', 'e']] };
const SRH_LAST = { 1: [['q']], 2: [['h'], ['q', 'q']], 3: [['hd'], ['h', 'q'], ['q', 'q', 'q']] };
// beats as Korean says them: 반 박, 한 박, 한 박 반, 두 박
const srhFmtB = (v) => LANG === 'ko' && ({ 0.5: '반 박', 1: '한 박', 1.5: '한 박 반', 2: '두 박' })[v] || fmtBeats(v);
const srhBeatsW = (n) => t(n === 1 ? '1 beat' : n + ' beats', ['한', '두', '세', '네'][n - 1] + ' 박');
const SRH_NTH = ['첫째', '둘째', '셋째', '넷째'];
// level 6: one bar of 4/4 to hear (no two choices with the same note starts)
const SRH_EAR = [srhBar(4, 'qd', 'e', 'h'), srhBar(4, 'q', 'p', 'h'), srhBar(4, 'p', 'q', 'h'), srhBar(4, 'p4', 'h'), srhBar(4, 'h', 'p4'), srhBar(4, 'q', 'q', 'p', 'q'), srhBar(4, 'qd', 'e', 'q', 'q'), srhBar(4, 'q', 'qd', 'e', 'q'), srhBar(4, 'q', 'er', 'e', 'q', 'q'), srhBar(4, 'p', 'p', 'q', 'q')];
const srhOnsets = (items) => srhSounds(items).filter(s => !s.rest).map(s => s.b).join();
// level 8: semiquavers (four to a beat: 1 e + a); level 9: syncopation (a note on the + that holds through the next beat,
// always inside half a 4/4 bar)
const SRH_S16 = [srhBar(4, 's4', 'q', 's4', 'q'), srhBar(4, 'q', 's4', 'h'), srhBar(2, 's4', 'q'), srhBar(4, 's4', 's4', 'h'), srhBar(3, 's4', 'q', 'q'), srhBar(4, 'p', 's4', 'h')];
const SRH_SYNC = [srhBar(4, 'e', 'q', 'e', 'h'), srhBar(4, 'h', 'e', 'q', 'e'), srhBar(3, 'e', 'q', 'e', 'q'), srhBar(2, 'e', 'q', 'e'), srhBar(4, 'e', 'q', 'e', 'q', 'q'), srhBar(3, 'q', 'e', 'q', 'e'), srhBar(4, 'q', 'q', 'e', 'q', 'e'), srhBar(4, 'e', 'q', 'e', 'e', 'q', 'e'), srhBar(3, 'e', 'q', 'q', 'e')];
// a count with its beat: '2', '2 +', '3 e', '3 a'
const srhFull = (pos) => { const w = Math.floor(pos + 1e-6), c = srhCount(pos); return c === String(w + 1) ? c : (w + 1) + ' ' + c; };
const srhKey = (items) => items.map(x => x.join('')).join(',');
function genSrhQuestion(lv, prev) {
  const uid = Math.random(), pk = prev && prev.key;
  const again = (f) => { for (let g = 0; g < 20; g++) { const q = f(); if (q.key !== pk) return { ...q, uid }; } return { ...f(), uid }; };
  if (lv.kind === 'beats') return again(() => { const k = pick(Object.keys(SRH_GLYPH_B)); return { kind: 'beats', k, key: k, answer: SRH_GLYPH_B[k], choices: [0.5, 1, 1.5, 2] }; });
  if (lv.kind === 'beam') return again(() => { const bad = Math.random() < 0.5, x = bad ? pick(SRH_BEAM_BAD) : [pick(SRH_BEAM_OK), null];
    return { kind: 'beam', items: x[0], why: x[1], key: srhKey(x[0]), answer: bad ? 'wrong' : 'right', choices: ['right', 'wrong'] }; });
  if (lv.kind === 'count' || lv.kind === 's16' || lv.kind === 'sync') return again(() => {
    const items = pick(lv.kind === 'count' ? SRH_COUNT_BARS : lv.kind === 's16' ? SRH_S16 : SRH_SYNC), snd = srhSounds(items), top = srhTop(items);
    const cand = snd.map((s, j) => j).filter(j => !snd[j].rest && (lv.kind === 'count' || (lv.kind === 's16' ? items[snd[j].j][0] === 's4' : Math.abs(snd[j].b % 1 - 0.5) < 1e-6 && snd[j].d >= 1)));
    const i = pick(cand), pos = snd[i].b, ans = srhFull(pos);
    let choices;
    if (lv.kind === 's16') { const w = Math.floor(pos + 1e-6); choices = [w, w + 0.25, w + 0.5, w + 0.75].map(srhFull); }
    else { const all = Array.from({ length: top * 2 }, (_, j) => j / 2).filter(p => Math.abs(p - pos) > 1e-6).sort((a, z) => Math.abs(a - pos) - Math.abs(z - pos));
      choices = [pos, ...sampleN(all.slice(0, 5), 3)].sort((a, z) => a - z).map(srhFull); }
    return { kind: lv.kind, items, lit: i, key: srhKey(items) + i, answer: ans, choices };
  });
  if (lv.kind === 'fill') return again(() => { const [top, ks, a] = pick(SRH_FILL), items = srhGapItems(top, ks); return { kind: 'fill', items, key: srhKey(items), answer: a, choices: SRH_FILL_KS.slice() }; });
  if (lv.kind === 'up') return again(() => {
    const last = Math.random() < 0.5;
    const [top, ana, from] = pick(SRH_UPS.filter(u => !last || u[0] > 2));
    const full = pick(SRH_FULL[top]), tail = last ? [['box', from, 64]] : pick(SRH_LAST[from]).map(k => [k]);
    const items = [['ts', top], ...ana.map(k => [k]), ['|'], ...full.map(k => [k]), ['|'], ...tail, ['||']];
    return last ? { kind: 'up', sub: 'last', items, from, top, key: 'l' + srhKey(items), answer: String(from), choices: Array.from({ length: top - 1 }, (_, j) => String(j + 1)) }
      : { kind: 'up', sub: 'start', items, from, top, key: 's' + srhKey(items), answer: String(from + 1), choices: Array.from({ length: top }, (_, j) => String(j + 1)) };
  });
  if (lv.kind === 'ear') return again(() => { let idx, g = 0; do { idx = sampleN(SRH_EAR.map((_, j) => j), 3); } while (new Set(idx.map(j => srhOnsets(SRH_EAR[j]))).size < 3 && g++ < 50);
    const a = idx[0]; return { kind: 'ear', items: SRH_EAR[a], key: 'e' + a, answer: String(a), choices: shuffle(idx.map(String)) }; });
  return again(() => { const items = pick(SRH_COUNT_BARS); return { kind: 'tap', items, key: 't' + srhKey(items) }; });
}
const SRH_RW = { right: () => t('Beamed right', '바르게 묶였어요'), wrong: () => t('Beamed wrong', '잘못 묶였어요') };
const SRH_WHY = { mid: () => t('A beam never crosses the middle of a 4/4 bar.', '빔은 4/4 마디 한가운데를 넘지 않아요.'), beat: () => t('A beam joins the quavers of one beat; this one goes across two beats.', '빔은 한 박의 8분음표끼리 이어요. 이 빔은 두 박에 걸쳐 있어요.') };
// a count as an answer: 'on 2' / '2'; 'on the “+” after 2' / '2 다음 +'
const srhOn = (c) => { const [w, x] = c.split(' '); return x ? t('on the “' + x + '” after ' + w, w + ' 다음 ' + x) : t('on ' + w, w); };
function SrhQuestion({ q, given, locked, onAnswer, pixel }) {
  const board = useBoard(q, given);
  const T = usePlTimers();
  const [phase, setPhase] = useState('ready');
  const [lit, setLit] = useState(-1);
  const run = useRef(null), taps = useRef([]), rels = useRef([]), held = useRef(null);
  const done = !!given;
  const ink = pixel ? '#faf6ec' : PEN_N;
  const btnCls = pixel ? 'pixel-choice' : 'choice-btn';
  const stopHeld = () => { if (held.current) { held.current(); held.current = null; } };
  const prompt = (txt) => <p style={pixel ? {fontSize:11.5,textAlign:'center',margin:'0 0 10px',lineHeight:1.7} : {fontSize:15,fontWeight:700,textAlign:'center',margin:'0 0 10px',color:'var(--muted)',textWrap:'balance',wordBreak:'keep-all'}}>{txt}</p>;
  const st = (c) => !done ? '' : (String(c) === String(q.answer) ? ' good' : (String(given.ans) === String(c) ? ' bad' : ''));
  const paper = (node) => <div style={{background:pixel ? '#faf6ec' : 'transparent',borderRadius:8,padding:pixel ? 6 : 0,margin:'0 0 10px'}}>{node}</div>;
  const note = (txt, always) => (always || done) && !pixel && <div style={{textAlign:'center',fontSize:13,color:'var(--muted)',margin:'8px 0 0',textWrap:'balance',wordBreak:'keep-all'}}>{txt}</div>;
  const hear = () => { if (q.kind === 'ear') srhRun(q.items, {}); };
  useEffect(() => { T.clear(); stopClicks(); stopHeld(); setPhase('ready'); setLit(-1); taps.current = []; rels.current = []; if (q.kind === 'ear') { const tm = setTimeout(hear, 250); return () => { clearTimeout(tm); stopClicks(); }; } return undefined; }, [q.uid]);
  // answered (or out of time): no run may answer again, and no note may ring on
  useEffect(() => { if (given) { T.clear(); stopHeld(); stopClicks(); setLit(-1); } }, [given]);
  const countBtn = (c) => { const [a, b] = c.split(' '); return <span style={{fontSize:pixel ? 11 : 19,fontWeight:900}}>{a}{b && <span style={{color:pixel ? undefined : BK.coral,marginLeft:4}}>{b}</span>}</span>; };
  const grid = (cols, render, pad = '14px 2px') => <div style={{display:'grid',gridTemplateColumns:'repeat(' + cols + ',minmax(0,1fr))',gap:8}}>{q.choices.map(c => <button key={c} disabled={locked} onClick={() => { if (q.kind === 'ear') stopClicks(); onAnswer(c); }} className={btnCls + st(c)} style={{padding:pad}}>{render(c)}</button>)}</div>;
  if (q.kind === 'tap') {
    const snd = srhSounds(q.items), n = srhBeats(q.items);
    function start() {
      if (done || phase !== 'ready') return;
      T.clear(); taps.current = []; rels.current = [];
      const r = srhRun(q.items, { silent: true }); if (!r) return; run.current = r;
      const go = r.at[r.lead];
      T.at(r, go, () => setPhase('go'));
      snd.forEach((s, k) => T.at(r, go + s.b * r.spb, () => setLit(k)));
      T.at(r, go + n * r.spb + 0.05, () => { stopHeld(); setPhase('scoring'); setLit(-1); onAnswer(srhScore(snd, go, r.spb, taps.current, rels.current, r.now())); });
      setPhase('count');
    }
    const onTap = () => { const r = run.current; if (r && (phase === 'count' || phase === 'go')) { taps.current.push(r.now()); const ctx = getAudio(); if (ctx) { stopHeld(); held.current = blip(ctx, ctx.currentTime, SRH_HZ, 4.3 * r.spb, 0.18, 'triangle'); } } };
    const onRelease = () => { const r = run.current, j = taps.current.length - 1; if (r && j >= 0 && rels.current[j] == null) rels.current[j] = r.now(); stopHeld(); };
    const res = done && given.ans && typeof given.ans === 'object' ? given.ans : null;
    return <div>
      <BoardTrack b={board} pixel={pixel}/>
      {prompt(snd.some(s => s.rest) ? t('A bar of clicks to get ready, then one press for each note, held for its length. No press in a rest. Count out loud.', '미리 세는 한 마디를 듣고, 음표마다 한 번씩 눌러 그 길이만큼 누르고 있어요. 쉼표에서는 누르지 않아요. 소리 내어 세요.') : t('A bar of clicks to get ready, then one press for each note, held for its length. Count out loud.', '미리 세는 한 마디를 듣고, 음표마다 한 번씩 눌러 그 길이만큼 누르고 있어요. 소리 내어 세요.'))}
      {paper(<SrhFit items={q.items} o={{ D: 44, lit, marks: res ? res.marks : null }} k={1.2}/>)}
      <div style={{textAlign:'center',fontSize:13,fontWeight:800,color:pixel ? '#faf6ec' : BK.muted,minHeight:18,margin:'2px 0 4px'}}>{phase === 'count' ? t('Get ready…', '준비…') : phase === 'go' ? t('Tap!', '쳐요!') : ''}</div>
      {!done && phase === 'ready' && <div style={{textAlign:'center',marginBottom:8}}><button className={pixel ? 'pixel-btn' : 'ghost-btn'} onClick={start} style={{fontSize:15,padding:'10px 18px'}}>{t('▶ Start', '▶ 시작')}</button></div>}
      {!done && <PlPad on={phase === 'count' || phase === 'go'} onTap={onTap} onRelease={onRelease} h={64}/>}
      {res && <div style={{textAlign:'center',fontSize:15,fontWeight:900,marginTop:8,color:res.ok ? BK.green : BK.coral}}>{srhResult(res)}</div>}
    </div>;
  }
  const rightPick = done && String(given.ans) === String(q.answer);
  let body;
  if (q.kind === 'beats') body = <>{prompt(t('How many beats?', '몇 박일까요?'))}
    <div style={{textAlign:'center',margin:'0 0 12px'}}><SrhGlyph k={q.k} col={ink} h={pixel ? 72 : 92}/></div>
    {grid(4, v => <span style={{fontSize:pixel ? 11 : 17,fontWeight:900}}>{srhFmtB(v)}</span>)}</>;
  else if (q.kind === 'beam') body = <>{prompt(t('Are the quavers beamed right?', '8분음표가 바르게 묶였나요?'))}
    {paper(<SrhFit items={q.items} o={{ D: 44, counts: false, hearts: false }}/>)}
    {grid(2, c => <span style={{fontSize:pixel ? 11 : 16,fontWeight:900}}>{SRH_RW[c]()}</span>)}
    {rightPick && note(q.why ? SRH_WHY[q.why]() : t('Each beam joins the quavers of one beat, or four in half a 4/4 bar.', '빔은 한 박의 8분음표끼리 이어요. 4/4에서는 반 마디의 넷을 이을 수도 있어요.'))}</>;
  else if (q.kind === 'count' || q.kind === 's16' || q.kind === 'sync') body = <>{prompt(t('On which count do you play the orange note?', '주황색 음표는 언제 칠까요?'))}
    {q.kind === 's16' && note(t('Four semiquavers make one beat: 1 e + a.', '16분음표 넷이 한 박: 1 e + a.'), true)}
    {q.kind === 'sync' && note(t('Syncopation: a note on the + that holds through the next beat.', '당김음: +에서 친 음이 다음 박에 걸쳐 이어져요.'), true)}
    <div style={{height:8}}/>
    {paper(<SrhFit items={q.items} o={{ D: 44, lit: q.lit, counts: done ? undefined : false }}/>)}
    {grid(4, countBtn)}</>;
  else if (q.kind === 'fill') body = <>{prompt(t('Which note fills the gap?', '빈칸에 들어갈 음표는 무엇일까요?'))}
    {paper(<SrhFit items={q.items} o={{ D: 44, counts: false, hearts: false }}/>)}
    {grid(4, c => <SrhGlyph k={c} col={ink} h={pixel ? 40 : 52}/>, '6px 2px')}
    {rightPick && note(srhFmtB(srhLen(q.items.find(x => x[0] === 'box'))))}</>;
  else if (q.kind === 'up') body = <>{prompt(q.sub === 'start' ? t('On which beat does the tune start?', '선율은 몇째 박에서 시작할까요?') : t('The last bar is missing. How many beats will it have?', '마지막 마디가 비었어요. 몇 박일까요?'))}
    {paper(<SrhFit items={q.items} o={{ D: 34, from: q.from, counts: false, hearts: false }} k={1.1}/>)}
    {grid(q.choices.length, c => <span style={{fontSize:pixel ? 12 : 20,fontWeight:900}}>{q.sub === 'start' ? c : srhBeatsW(Number(c))}</span>)}
    {note(t('In this tune, the short first bar and the last bar make one full bar.', '이 선율에서는 짧은 첫 마디와 마지막 마디를 합치면 갖춘마디 하나가 돼요.'))}</>;
  else body = <>{prompt(t('Listen. Which rhythm is it?', '들어 봐요. 어느 리듬일까요?'))}
    <div style={{textAlign:'center',margin:'0 0 12px'}}><button className={pixel ? 'pixel-btn' : 'ghost-btn'} onClick={hear} style={pixel ? {fontSize:9} : {fontSize:15,padding:'8px 16px',minHeight:44}}>{t('▶ Hear it again', '▶ 다시 듣기')}</button></div>
    <div style={{display:'grid',gap:8}}>{q.choices.map(c => <button key={c} disabled={locked} onClick={() => { stopClicks(); onAnswer(c); }} className={btnCls + st(c)} style={{padding:'4px 6px',background:pixel ? '#faf6ec' : undefined}}><SrhFit items={SRH_EAR[+c]} o={{ D: 40, counts: false, hearts: false }} k={1}/></button>)}</div></>;
  return <div><BoardTrack b={board} pixel={pixel}/>{body}</div>;
}
function srhCheck(q, ans) {
  if (ans === null || ans === undefined) return false;
  if (q.kind === 'tap') return !!(ans && ans.ok);
  if (typeof q.answer === 'number') return Math.abs(Number(ans) - q.answer) < 1e-9;
  return String(ans) === String(q.answer);
}
const SRH_NAME = { q: () => t('crotchet', '4분음표'), h: () => t('minim', '2분음표'), qd: () => t('dotted crotchet', '점4분음표'), e: () => t('quaver', '8분음표'), er: () => t('quaver rest', '8분쉼표'), p: () => t('two quavers', '8분음표 둘'), p4: () => t('four quavers', '8분음표 넷'), r: () => t('crotchet rest', '4분쉼표') };
const SRH_GNAME = { e: () => t('a quaver', '8분음표'), q: () => t('a crotchet', '4분음표'), qd: () => t('a dotted crotchet', '점4분음표'), h: () => t('a minim', '2분음표') };
function srhAnswerLabel(q) {
  if (q.kind === 'beats') return srhFmtB(q.answer);
  if (q.kind === 'beam') return SRH_RW[q.answer]() + (q.why ? '. ' + SRH_WHY[q.why]() : '');
  if (q.kind === 'count' || q.kind === 's16' || q.kind === 'sync') return srhOn(q.answer);
  if (q.kind === 'fill') return SRH_GNAME[q.answer]() + ' (' + srhFmtB(srhLen(q.items.find(x => x[0] === 'box'))) + ')';
  if (q.kind === 'up') return q.sub === 'start' ? t('beat ' + q.answer, SRH_NTH[q.answer - 1] + ' 박') : srhBeatsW(Number(q.answer));
  if (q.kind === 'ear') return q.items.filter(srhIsNote).map(x => SRH_NAME[x[0]]()).join(', ');
  const n = srhSounds(q.items).filter(s => !s.rest).length;
  return t('one press for each note, held for its length: ' + n + ' in all', '음표마다 한 번씩 그 길이만큼, 모두 ' + n + '번');
}
Object.assign(RHYTHM_DRILL, { levels: SRH_LEVELS, generate: genSrhQuestion, check: srhCheck, answerLabel: srhAnswerLabel, Question: SrhQuestion, Learn: SrhLearn });
