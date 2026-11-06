// ─── Phase 472: chapter 17's pads (pages 2 to 6), the screen lesson and the drill ───
const SAC_BPM = 84;
const SAC_SCR = 270;   // the staff's reference width on a phone screen: one size for the pads and the drill's tunes
const sacKey = (m, len = 0.45) => playKey(m - 60, len);
const sacSay = (n) => n.sign ? (n.sign === 'n' ? t(dName(n.d) + ' natural: the plain note', dName(n.d) + ' 내추럴: 원래 음') : sacNameTxt(n) + (n.sign === '#' ? t(': a half step up', ': 위로 반 걸음') : t(': a half step down', ': 아래로 반 걸음')))
  : n.carried ? sacNameTxt(n) + t(': the same bar, still ' + sacNameTxt(n), ': 같은 마디라 임시표가 그대로예요')
  : n.natHeld ? sacNameTxt(n) + t(': the natural still holds', ': 내추럴이 그대로예요')
  : n.reset ? sacNameTxt(n) + t(': a new bar, plain', ': 새 마디라 원래 음')
  : n.other ? sacNameTxt(n) + t(': another line or space, plain', ': 다른 줄이나 칸이라 원래 음') : sacNameTxt(n);
const SAC_PAD = {
  2: () => t('Play sharps and flats', '샤프와 플랫 치기'), 3: () => t('The natural', '내추럴'), 4: () => t('Until the bar line', '세로줄까지'),
  5: () => t('Its own line or space', '같은 줄이나 칸만'), 6: () => t('Read the tune', '선율 읽기'),
};
const SAC_STOP = { fn: null };   // the pad that is sounding: a new ▶ Listen on another pad stops it
function SacPad({ page }) {
  const items = SAC_TUNES[page], rows = page === 4 || page === 6 ? sacBars(items) : [items], seq = sacRead(items), [d0, n] = SAC_KEYS[page], to = SAC_TUNE_O[page] || {};
  const [mode, setMode] = useState(null);   // null | 'listen' | 'tap'
  const [lit, setLit] = useState(-1);        // the note sounding (listen) or the next to play (tap)
  const [key, setKey] = useState(null);      // the key lit on the keyboard
  const [miss, setMiss] = useState(null);
  const [msg, setMsg] = useState('');
  const timers = useRef([]);
  const clear = () => { const on = timers.current.length > 0; timers.current.forEach(clearTimeout); timers.current = []; if (on) stopClicks(); };
  // one stable stop function for this pad (its current state through a ref), released when it is not sounding
  const meRef = useRef(null);
  meRef.current = () => { clear(); setLit(-1); setKey(null); setMiss(null); setMsg(''); setMode(null); };
  const me = useRef(() => meRef.current()).current;
  const release = () => { if (SAC_STOP.fn === me) SAC_STOP.fn = null; };
  useEffect(() => () => { clear(); release(); }, []);
  function listen() {
    if (SAC_STOP.fn && SAC_STOP.fn !== me) SAC_STOP.fn(); SAC_STOP.fn = me;
    clear(); setMode('listen'); setMiss(null);
    timers.current = playMelody(seq.map(x => ({ d: x.d, acc: x.acc, dur: x.dur })), SAC_BPM, (i) => {
      if (i < 0) { timers.current = []; release(); setLit(-1); setKey(null); setMsg(''); setMode(null); return; }
      setLit(i); setKey(sacMidi(seq[i])); setMsg(sacSay(seq[i])); });
    if (!timers.current.length) { release(); setMode(null); }   // no sound here: nothing to wait for
  }
  function tapMode() { clear(); release(); setMode('tap'); setLit(0); setKey(null); setMiss(null); setMsg(t('Play the notes in order, one key at a time.', '음표를 차례로, 한 건반씩 쳐요.')); }
  function onTap(m) {
    sacKey(m);
    if (mode !== 'tap' || lit < 0) return;
    const want = sacMidi(seq[lit]);
    if (m === want) { setMiss(null); setKey(m); setMsg(sacSay(seq[lit]) + (lit === seq.length - 1 ? ' ✓' : '')); setLit(lit + 1 < seq.length ? lit + 1 : -1); if (lit + 1 >= seq.length) setMode(null); }
    else { setMiss(m); setKey(null); setMsg(t('Not that key. Look for a sign: just before this note, or earlier in its bar.', '그 건반이 아니에요. 임시표를 찾아요: 이 음표 바로 앞이나, 같은 마디의 앞쪽에서.')); }
  }
  let off = 0;
  const box = sacSetBox(rows, SAC_SCR, () => to);
  const staffRows = rows.map((row, r) => { const k = off, cnt = sacRead(row).length; off += cnt;
    return sacInSet(box, SAC_SCR, <SacStaff items={row} width={box} left o={{ ...to, hl: lit >= k && lit < k + cnt ? [lit - k] : [] }}/>, r); });
  return (
    <div className="try-box" style={actBox} data-sac={'pad' + page}>
      <div style={actTitle}>{SAC_PAD[page]()}</div>
      <div style={actNote}>{t('▶ Listen: the notes sound in turn, each lit, with its name. ▶ Tap it: play them in order on the keys.', '▶ 듣기: 음이 차례로 울리고, 음표마다 불이 켜지며 이름이 나와요. ▶ 쳐 보기: 건반에서 차례로 쳐요.')}</div>
      <div style={{display:'flex',flexDirection:'column',gap:6}}>{staffRows}</div>
      <div style={{maxWidth:n * 44,margin:'8px auto 0'}}><SacKeys d0={d0} n={n} o={{ lit: key == null ? [] : [key], miss, H: 120 }} onTap={onTap}/></div>
      <div style={{textAlign:'center',fontSize:15,fontWeight:900,color:miss ? BK.coral : BK.ink,minHeight:22,margin:'6px 0',textWrap:'balance',wordBreak:'keep-all'}}>{sscSx(msg)}</div>
      <div style={{display:'flex',gap:6,justifyContent:'center'}}>
        <button className="ghost-btn" onClick={listen}>{t('▶ Listen', '▶ 듣기')}</button>
        <button className="ghost-btn" onClick={tapMode}>{t('▶ Tap it', '▶ 쳐 보기')}</button>
      </div>
    </div>
  );
}

// ── the book on screen: the opener is the lesson's head, every other page a step ──
function SacLearn({ onStart }) {
  const pages = sacLbPages(true);
  const opener = pages[0];
  return (
    <Lesson id="accidentals" title={bkChapterName('accidentals')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="accidentals"><div className="lb-screen lb-open" style={{display:'flex',flexDirection:'column',gap:12,margin:'0 0 8px'}}>{lbWordsFirst(opener.props.children)}</div></BkChapterCtx.Provider></LbScreenCtx.Provider>}>
      {pages.slice(1).map((pg, i) => (
        <Step key={i} title={pg.props.title}>
          <LbScreenPage page={pg}/>
        </Step>
      ))}
    </Lesson>
  );
}

// ── the drill, after page 6, in the book's order: the signs (1, 2), the natural (3), the bar line (4), its own line or
// space (5), reading (6, 7), listening (8); 9 extra (the bass clef) ──
const SAC_LEVELS = [
  { n: 1, label: 'Name the sign', kind: 'sign', time: 7 },
  { n: 2, label: 'Find the key', kind: 'key', time: 9, noPrint: true },
  { n: 3, label: 'The natural', kind: 'nat', time: 10 },
  { n: 4, label: 'Until the bar line', kind: 'bar', time: 10 },
  { n: 5, label: 'Its own line or space', kind: 'line', time: 10 },
  { n: 6, label: 'Read the bar', kind: 'read', time: 15 },
  { n: 7, label: 'Which sign?', kind: 'write', time: 12 },
  { n: 8, label: 'Listen: which bar?', kind: 'ear', time: 14, noPrint: true },
  { n: 9, label: 'Extra: the bass clef', kind: 'bass', time: 10 },
];
Object.assign(LEVEL_KO, {
  'Name the sign': '임시표 이름', 'Find the key': '건반 찾기', 'The natural': '내추럴', 'Until the bar line': '세로줄까지',
  'Its own line or space': '같은 줄이나 칸만', 'Read the bar': '마디 읽기', 'Which sign?': '어떤 임시표?', 'Listen: which bar?': '듣기: 어느 마디?',
  'Extra: the bass clef': '더 해 보기: 낮은음자리표',
});
const SAC_WORD = { '#': () => t('sharp', '샤프'), b: () => t('flat', '플랫'), n: () => t('natural', '내추럴'), none: () => t('no sign', '임시표 없음') };
// the signs a letter may take here (never E♯, B♯, C♭, F♭)
const sacOk = (d, s) => !(s === '#' && 'EB'.includes(dName(d))) && !(s === 'b' && 'CF'.includes(dName(d)));
const sacSignFor = (d) => pick(['#', 'b'].filter(s => sacOk(d, s)));
const sacNm = (d, acc) => dName(d) + (acc === 1 ? '♯' : acc === -1 ? '♭' : '');
// a filler note in a bar: a step or two from x, never on x's line or space or an octave from it
const sacFill = (x, lo, hi) => pick([x - 2, x - 1, x + 1, x + 2].filter(v => v >= lo && v <= hi && (v - x) % 7 !== 0));
const SAC_SP = ' ';   // the gap between names in a choice
function genSacQuestion(lv, prev) {
  const uid = Math.random(), pk = prev && prev.key;
  const again = (f) => { for (let g = 0; g < 30; g++) { const q = f(); if (q.key !== pk) return { ...q, uid }; } return { ...f(), uid }; };
  const choicesOf = (ans, pool) => shuffle([ans, ...sampleN([...new Set(pool)].filter(c => c !== ans), 3)]);
  const nameAt = (items, at) => sacNameTxt(sacRead(items)[at]);
  if (lv.kind === 'sign') return again(() => { const s = pick(['#', 'b', 'n']), d = pick([29, 30, 31, 32, 33, 34, 35, 36, 37].filter(x => s === 'n' || sacOk(x, s)));
    return { kind: 'sign', items: [['w', 4, d, s], ['||']], key: s + d, answer: s, choices: ['#', 'b', 'n'] }; });
  if (lv.kind === 'key') return again(() => { const d = pick([28, 29, 30, 31, 32, 33, 34]), s = sacSignFor(d), m = ivMidi({ d, acc: SAC_ACC[s] });
    return { kind: 'key', items: [['w', 4, d, s], ['||']], key: 'k' + d + s, answer: m }; });
  if (lv.kind === 'nat') return again(() => {   // the coral note: the natural itself or a later note after it (plain), or a note the sign still holds (signed); notes 2, 3 and 4 each both ways
    const x = pick([29, 30, 31, 32, 33, 34, 35, 36]), s = sacSignFor(x), f = () => ['q', 1, sacFill(x, 28, 38)], X = (z) => ['q', 1, x, z];
    const v = pick(['self1', 'held1', 'self2', 'held2', 'after3', 'held3']);
    const notes = { self1: [X(s), X('n'), f(), f()], held1: [X(s), X(), f(), X('n')], self2: [X(s), f(), X('n'), f()], held2: [X(s), f(), X(), X('n')],
      after3: [X(s), X('n'), f(), X()], held3: [X('n'), X(s), f(), X()] }[v];
    const items = [...notes, ['||']], at = +v.slice(-1), ans = nameAt(items, at);
    return { kind: 'nat', items, at, key: 'n' + x + s + v, answer: ans, choices: choicesOf(ans, [sacNm(x, SAC_ACC[s]), sacNm(x, 0), sacNm(x - 1, 0), sacNm(x + 1, 0)]) }; });
  if (lv.kind === 'bar' || lv.kind === 'bass') return again(() => {
    const bass = lv.kind === 'bass', lo = bass ? 18 : 29, hi = bass ? 26 : 37, x = lo + 1 + Math.floor(Math.random() * (hi - lo - 1)), s = sacSignFor(x), f = () => sacFill(x, lo, hi);
    const v = pick(['held', 'held', 'before', 'next', 'back', 'own']), sb = v === 'next' ? 0 : v === 'back' ? 1 : pick([0, 1]);   // the bar with the sign
    const bars = [[0, 1, 2, 3].map(() => ['q', 1, f()]), [0, 1, 2, 3].map(() => ['q', 1, f()])];
    let at;
    if (v === 'held') { const ph = pick([1, 2, 3]), ps = Math.floor(Math.random() * ph); bars[sb][ps] = ['q', 1, x, s]; bars[sb][ph] = ['q', 1, x]; at = sb * 4 + ph; }
    else if (v === 'before') { const pb = pick([0, 1, 2]), ps = pb + 1 + Math.floor(Math.random() * (3 - pb)); bars[sb][ps] = ['q', 1, x, s]; bars[sb][pb] = ['q', 1, x]; at = sb * 4 + pb; }
    else if (v === 'own') { const ps = pick([0, 1, 2, 3]); bars[sb][ps] = ['q', 1, x, s]; at = sb * 4 + ps; }   // the note with the sign
    else { const ps = pick([0, 1, 2, 3]), po = pick([0, 1, 2, 3]); bars[sb][ps] = ['q', 1, x, s]; bars[1 - sb][po] = ['q', 1, x]; at = (1 - sb) * 4 + po; }   // next: plain in the bar after; back: plain in the bar before
    const items = [['ts', 4], ...bars[0], ['|'], ...bars[1], ['||']], ans = nameAt(items, at);
    return { kind: lv.kind, clef: bass ? 'bass' : 'treble', items, at, key: lv.kind + x + s + v + at, answer: ans, choices: choicesOf(ans, [sacNm(x, SAC_ACC[s]), sacNm(x, 0), sacNm(x - 1, 0), sacNm(x + 1, 0)]) }; });
  if (lv.kind === 'line') return again(() => {   // both octaves always printed; the coral note on the sign's line or space, or on the other
    const x = pick([29, 30, 31, 32]), s = sacSignFor(x), hiFirst = Math.random() < 0.5, a = hiFirst ? x + 7 : x, b = hiFirst ? x : x + 7, same = Math.random() < 0.5;
    const items = [['q', 1, a, s], ['q', 1, b], ['q', 1, sacFill(a, 29, 39)], ['q', 1, same ? a : b], ['||']], ans = nameAt(items, 3);
    return { kind: 'line', items, at: 3, key: 'l' + a + b + s + same, answer: ans, choices: choicesOf(ans, [sacNm(x, SAC_ACC[s]), sacNm(x, 0), sacNm(x + 1, 0), sacNm(x - 1, 0)]) }; });
  if (lv.kind === 'read') return again(() => {   // the sign in bar 1 or 2; one or two held notes after it; the same letter plain in the other bar
    const x = pick([30, 31, 32, 33, 34, 35]), s = sacSignFor(x), f = () => ['q', 1, sacFill(x, 29, 37)], X = (z) => ['q', 1, x, z], two = Math.random() < 0.4, inFirst = Math.random() < 0.6;
    const signed = two ? pick([[X(s), X(), f(), X()], [X(s), f(), X(), X()]]) : pick([[X(s), f(), X(), f()], [f(), X(s), f(), X()], [X(s), X(), f(), f()]]);
    const plain = pick([[X(), ['h', 2, sacFill(x, 29, 37)], f()], [f(), X(), ['h', 2, sacFill(x, 29, 37)]]]);
    const items = [['ts', 4], ...(inFirst ? signed : plain), ['|'], ...(inFirst ? plain : signed), ['||']], r = sacRead(items), right = r.map(sacNameTxt);
    const held = r.map((n, j) => n.carried ? j : -1).filter(j => j >= 0), otherJ = r.findIndex(n => n.d === x && !n.acc);
    const set = (a, js, acc) => a.map((v, j) => js.includes(j) ? sacNm(x, acc) : v);
    const forgot = set(right, held, 0), spill = set(right, [otherJ], SAC_ACC[s]), both = set(forgot, [otherJ], SAC_ACC[s]), part = set(right, held.slice(-1), 0);
    const cut = inFirst ? 4 : 3, fmt = (a) => a.slice(0, cut).join(SAC_SP) + SAC_SP + '|' + SAC_SP + a.slice(cut).join(SAC_SP);
    const wrong = shuffle([...new Set([forgot, spill, both, part].map(fmt))].filter(c => c !== fmt(right))).slice(0, 3);
    return { kind: 'read', items, key: 'r' + x + s + two + inFirst, answer: fmt(right), choices: shuffle([fmt(right), ...wrong]) }; });
  if (lv.kind === 'write') return again(() => {
    const x = pick([30, 31, 32, 33, 34, 35]), s = sacSignFor(x), mode = pick(['cancel', 'keep', 'add']), y = sacFill(x, 29, 37);
    const items = mode === 'add' ? [['q', 1, y], ['q', 1, sacFill(x, 29, 37)], ['q', 1, x], ['q', 1, sacFill(x, 29, 37)], ['||']] : [['q', 1, x, s], ['q', 1, y], ['q', 1, x], ['q', 1, sacFill(x, 29, 37)], ['||']];
    const want = mode === 'cancel' ? sacNm(x, 0) : sacNm(x, SAC_ACC[s]), ans = mode === 'cancel' ? 'n' : mode === 'keep' ? 'none' : s;
    // when the sign still holds, writing it again is right too (alt)
    return { kind: 'write', items, at: 2, want, key: 'w' + x + s + mode, answer: ans, alt: mode === 'keep' ? s : undefined, choices: ['#', 'b', 'n', 'none'] }; });
  if (lv.kind === 'ear') return again(() => {
    const x = pick([30, 31, 32, 33, 34]), s = sacSignFor(x), y = sacFill(x, 29, 37), z = sacFill(x, 29, 37);
    const a = [['q', 1, x, s], ['q', 1, y], ['q', 1, x], ['q', 1, z], ['||']], b = [['q', 1, x, s], ['q', 1, y], ['q', 1, x, 'n'], ['q', 1, z], ['||']], which = pick(['a', 'b']);
    return { kind: 'ear', a, b, items: which === 'a' ? a : b, key: 'e' + x + s + which + Math.random(), answer: which, choices: ['a', 'b'] }; });
  return genSacQuestion(SAC_LEVELS[0], prev);
}
function sacPlayItems(items) { stopClicks(); return playMelody(sacRead(items).map(n => ({ d: n.d, acc: n.acc, dur: n.dur })), 96); }
const sacSignBtn = (s, sz) => s === 'none' ? <span style={{fontSize:sz * 0.62,fontWeight:900}}>{SAC_WORD.none()}</span> : <span style={{display:'inline-flex',alignItems:'baseline',gap:6}}><span style={{fontFamily:MUSIC_FONT,fontSize:sz * 1.25,lineHeight:1}}>{s === '#' ? '♯' : s === 'b' ? '♭' : '♮'}</span><span style={{fontSize:sz * 0.62,fontWeight:900}}>{SAC_WORD[s]()}</span></span>;
const sacWithRo = (w) => w + (/♭$/.test(w) ? '으로' : '로');
function SacQuestion({ q, given, locked, onAnswer, pixel }) {
  const board = useBoard(q, given);
  useEffect(() => { if (q.kind !== 'ear') return undefined; const tm = setTimeout(() => sacPlayItems(q.items), 300); return () => { clearTimeout(tm); stopClicks(); }; }, [q.uid]);
  const isDone = !!given;
  const btnCls = pixel ? 'pixel-choice' : 'choice-btn';
  const prompt = (txt) => <p style={pixel ? {fontSize:11.5,textAlign:'center',margin:'0 0 10px',lineHeight:1.7} : {fontSize:15,fontWeight:700,textAlign:'center',margin:'0 0 10px',color:'var(--muted)',textWrap:'balance',wordBreak:'keep-all'}}>{txt}</p>;
  const st = (c) => !isDone ? '' : (String(c) === String(q.answer) || (q.alt && c === q.alt && given.ans === q.alt) ? ' good' : (String(given.ans) === String(c) ? ' bad' : ''));
  const grid = (cols, render, pad = '12px 2px') => <div style={{display:'grid',gridTemplateColumns:'repeat(' + cols + ',minmax(0,1fr))',gap:8}}>{q.choices.map(c => <button key={c} disabled={locked} onClick={() => { stopClicks(); onAnswer(c); }} className={btnCls + st(c)} style={{padding:pad}}>{render(c)}</button>)}</div>;
  const word = (s, sz = 18) => <span style={{fontSize:pixel ? 11 : sz,fontWeight:900}}>{sscSx(s)}</span>;
  const paper = (node, mw = 400) => <div style={{background:'#fff',borderRadius:pixel ? 0 : 8,padding:pixel ? 4 : '4px 0',margin:'0 auto 10px',maxWidth:mw}}>{node}</div>;
  const staff = (items, o = {}, clef = 'treble', mw = 400) => paper(<SacStaff items={items} clef={clef} width={mw} full o={{ ...o, x0: clef === 'bass' ? 54 : undefined }}/>, mw);
  const bars = (items, o = {}, clef = 'treble') => { const rows = sacBars(items), oo = { x0: clef === 'bass' ? 54 : undefined }, box = Math.max(...rows.map(r => sacVbw(r, oo, clef))); let off = 0;
    return paper(<div style={{display:'flex',flexDirection:'column',gap:2}}>{rows.map((r, i) => { const k = off, cnt = sacRead(r).length; off += cnt;
      return <SacStaff key={i} items={r} clef={clef} width={box} left o={{ ...o, ...oo, hl: (o.hl || []).filter(j => j >= k && j < k + cnt).map(j => j - k) }}/>; })}</div>, 300); };
  const coral = { hl: [q.at] };
  let body;
  if (q.kind === 'sign') body = <>{prompt(t('What is this sign called?', '이 임시표의 이름은?'))}{staff(q.items, { D: 18 }, 'treble', 200)}{grid(3, c => sacSignBtn(c, 20))}</>;
  else if (q.kind === 'key') body = <>{prompt(t('Tap the key of this note.', '이 음의 건반을 눌러요.'))}{staff(q.items, { D: 18 }, 'treble', 200)}
    {paper(<SacKeys d0={28} n={8} o={{ lit: isDone ? [q.answer] : [], miss: isDone && given.ans !== q.answer ? given.ans : null, H: 120 }} onTap={(m) => { if (locked || isDone) return; sacKey(m); onAnswer(m); }}/>, 360)}</>;
  else if (q.kind === 'nat' || q.kind === 'bar' || q.kind === 'line' || q.kind === 'bass') body = <>{prompt(t('What is the coral note?', '산호색 음의 이름은?'))}{q.kind === 'bar' || q.kind === 'bass' ? bars(q.items, coral, q.clef) : staff(q.items, coral, q.clef || 'treble')}{grid(4, c => word(c, 19))}</>;
  else if (q.kind === 'read') body = <>{prompt(t('Which names are right, note by note?', '음이름을 바르게 읽은 것은?'))}{bars(q.items)}{grid(1, c => word(c, 17), '10px 4px')}</>;
  else if (q.kind === 'write') body = <>{prompt(t('The coral note must sound ' + q.want + '. What goes just before it?', '산호색 음을 ' + sacWithRo(q.want) + ' 치려면 바로 앞에 무엇을 붙일까요?'))}{staff(q.items, coral)}{grid(4, c => sacSignBtn(c, 17), '10px 2px')}</>;
  else body = <>{prompt(t('Listen. Which bar did you hear?', '들어 봐요. 어느 마디였을까요?'))}
    <div style={{display:'flex',flexDirection:'column',gap:4,margin:'0 0 8px'}}>{['a', 'b'].map(w => <div key={w} style={{display:'grid',gridTemplateColumns:'22px 1fr',alignItems:'center',gap:6}}><div style={{textAlign:'center',fontWeight:900,fontSize:16}}>{w}</div>{paper(<SacStaff items={q[w]} width={330} full/>, 360)}</div>)}</div>
    <div style={{textAlign:'center',margin:'0 0 10px'}}><button className={pixel ? 'pixel-btn' : 'ghost-btn'} onClick={() => sacPlayItems(q.items)} style={pixel ? {fontSize:9} : {fontSize:15,padding:'8px 16px',minHeight:44}}>{t('▶ Hear it again', '▶ 다시 듣기')}</button></div>
    {grid(2, c => word(c, 20))}</>;
  return <div><BoardTrack b={board} pixel={pixel}/>{body}</div>;
}
function sacCheck(q, ans) { if (ans === null || ans === undefined) return false; return String(ans) === String(q.answer) || (q.alt != null && ans === q.alt); }
function sacAnswerLabel(q) {
  if (q.kind === 'sign') return t('a ' + SAC_WORD[q.answer](), SAC_WORD[q.answer]());
  if (q.kind === 'key') { const n = sacRead(q.items)[0]; return sacNameTxt(n); }
  if (q.kind === 'write') return q.answer === 'none' ? t('no sign: it still holds in this bar (another ' + (q.alt === '#' ? '♯' : '♭') + ' is also right)', '임시표 없음: 같은 마디라 그대로예요 (' + (q.alt === '#' ? '♯를' : '♭을') + ' 또 붙여도 맞아요)') : t('a ' + SAC_WORD[q.answer](), SAC_WORD[q.answer]());
  if (q.kind === 'ear') return t('bar ', '') + q.answer + t('', ' 마디');
  const n = q.at != null ? sacRead(q.items)[q.at] : null;
  if (n && (q.kind === 'bar' || q.kind === 'bass' || q.kind === 'line' || q.kind === 'nat')) return q.answer + (n.carried ? t(' (the same bar: it still holds)', ' (같은 마디라 그대로)') : n.natHeld ? t(' (the natural still holds)', ' (내추럴이 그대로예요)') : n.reset ? t(' (a new bar)', ' (새 마디)') : n.other ? t(' (another line or space)', ' (다른 줄이나 칸)') : n.sign === 'n' ? t(' (the natural)', ' (내추럴)') : !n.sign && !n.acc ? t(' (no sign before it)', ' (앞에 임시표가 없어요)') : '');
  return q.answer;
}
Object.assign(SAC_DRILL, { levels: SAC_LEVELS, generate: genSacQuestion, check: sacCheck, answerLabel: sacAnswerLabel, Question: SacQuestion, Learn: SacLearn });
