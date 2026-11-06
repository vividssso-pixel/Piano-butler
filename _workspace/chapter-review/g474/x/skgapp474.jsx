// ─── Phase 474: chapter 19's pads (pages 2 to 6), the screen lesson and the drill ───
const SKG_BPM = 84;
const SKG_SCR = 270;   // the staff's reference width on a phone screen (chapter 17's)
const skgSay = (n) => n.sign === 'n' ? sacNameTxt(n) + t(': the natural, until the bar line', ': 내추럴, 세로줄까지')
  : n.sign ? sacNameTxt(n) + t(': an accidental, until the bar line', ': 임시표, 세로줄까지')
  : n.natHeld ? sacNameTxt(n) + t(': the natural still holds', ': 내추럴이 그대로예요')
  : n.held ? sacNameTxt(n) + t(': the same bar, still ' + sacNameTxt(n), ': 같은 마디라 임시표가 그대로예요')
  : n.back && n.byKey ? sacNameTxt(n) + t(': a new bar, the key signature again', ': 새 마디라 다시 조표대로예요')
  : n.byKey ? sacNameTxt(n) + t(': the key signature', ': 조표대로') : sacNameTxt(n);
const SKG_PAD = { 2: () => t('Every F', '모든 F'), 3: () => t('G major', 'G장조'), 4: () => t('F major', 'F장조'), 5: () => t('Key signature and accidental', '조표와 임시표') };
const SKG_STOP = { fn: null };   // the pad that is sounding: a new ▶ Listen on another pad stops it
// one pad: a tune (or a scale) with its key: ▶ Listen (each note lit, with its name), ▶ Tap it (play it in order on the keys);
// page 2 also plays it ▶ Without the key signature
function useSkgPlayer(items, key) {
  const seq = skgRead(items, key);
  const [mode, setMode] = useState(null);   // null | 'listen' | 'tap'
  const [lit, setLit] = useState(-1);
  const [keyLit, setKeyLit] = useState(null);
  const [miss, setMiss] = useState(null);
  const [msg, setMsg] = useState('');
  const timers = useRef([]);
  const clear = () => { const on = timers.current.length > 0; timers.current.forEach(clearTimeout); timers.current = []; if (on) stopClicks(); };
  const meRef = useRef(null);
  meRef.current = () => { clear(); setLit(-1); setKeyLit(null); setMiss(null); setMsg(''); setMode(null); };
  const me = useRef(() => meRef.current()).current;
  const release = () => { if (SKG_STOP.fn === me) SKG_STOP.fn = null; };
  useEffect(() => () => { clear(); release(); }, []);
  const take = () => { if (SKG_STOP.fn && SKG_STOP.fn !== me) SKG_STOP.fn(); SKG_STOP.fn = me; };
  function listen(plain) {
    take(); clear(); setMode('listen'); setMiss(null);
    const s = plain ? skgRead(items, 'C') : seq;
    timers.current = playMelody(s.map(x => ({ d: x.d, acc: x.acc, dur: x.dur })), SKG_BPM, (i) => {
      if (i < 0) { timers.current = []; release(); setLit(-1); setKeyLit(null); setMsg(''); setMode(null); return; }
      setLit(i); setKeyLit(sacMidi(s[i])); setMsg(plain ? sacNameTxt(s[i]) + (seq[i].byKey ? t(': without the key signature', ': 조표 없이') : '') : skgSay(s[i])); });
    if (!timers.current.length) { release(); setMode(null); }
  }
  function tapMode() { take(); clear(); release(); setMode('tap'); setLit(0); setKeyLit(null); setMiss(null); setMsg(t('Play the notes in order, one key at a time.', '음표를 차례로, 한 건반씩 쳐요.')); }
  function onTap(m) {
    sacKey(m);
    if (mode !== 'tap' || lit < 0) return;
    const want = sacMidi(seq[lit]);
    if (m === want) { setMiss(null); setKeyLit(m); setMsg(skgSay(seq[lit]) + (lit === seq.length - 1 ? ' ✓' : '')); setLit(lit + 1 < seq.length ? lit + 1 : -1); if (lit + 1 >= seq.length) setMode(null); }
    else { setMiss(m); setKeyLit(null); setMsg(t('Not that key. Look at the key signature, and for a sign earlier in the bar.', '그 건반이 아니에요. 조표를 보고, 같은 마디 앞쪽의 임시표도 찾아요.')); }
  }
  const stop = () => meRef.current();
  return { seq, mode, lit, keyLit, miss, msg, listen, tapMode, onTap, stop };
}
const skgMsgLine = (msg, miss) => <div style={{textAlign:'center',fontSize:15,fontWeight:900,color:miss ? BK.coral : BK.ink,minHeight:22,margin:'6px 0',textWrap:'balance',wordBreak:'keep-all'}}>{sscSx(msg)}</div>;
function SkgPad({ page }) {
  const items = SKG_TUNES[page], key = SKG_TUNE_KEY[page], [d0, n] = SKG_KEYS[page];
  const P = useSkgPlayer(items, key), rows = page === 5 || page === 2 ? sacBars(items) : [items], scale = page === 3 || page === 4;
  const o = scale ? { D: 25 } : {};
  let off = 0;
  const box = skgSetBox(rows, key, SKG_SCR, (row, r) => ({ ...o, ...(page === 5 ? (r === 0 ? { bracket: {} } : {}) : {}) }));
  const extra = (row, r, k) => { if (page !== 5) return {}; const c = SKG_P5O(), cnt = skgRead(row, key).length, loc = (js) => js.filter(j => j >= k && j < k + cnt).map(j => j - k);
    return { under: c.under.slice(k, k + cnt), underCoral: loc(c.underCoral), signHl: loc(c.signHl), ...(r === 0 ? { bracket: c.bracket } : {}) }; };
  const staffRows = rows.map((row, r) => { const k = off, cnt = skgRead(row, key).length; off += cnt;
    return sacInSet(box, SKG_SCR, <SkgStaff items={row} k={key} width={box} left o={{ ...o, ...extra(row, r, k), boxS: 24, ksCol: PEN_C, hl: P.lit >= k && P.lit < k + cnt ? [P.lit - k] : [] }}/>, r); });
  return (
    <div className="try-box" style={actBox} data-skg={'pad' + page}>
      <div style={actTitle}>{SKG_PAD[page]()}</div>
      <div style={actNote}>{page === 2 ? t('▶\u00a0Listen: with the key signature. ▶\u00a0Without\u00a0it: every F plain. ▶\u00a0Tap\u00a0it: play the notes in order on the keys.', '▶\u00a0듣기: 조표대로. ▶\u00a0조표\u00a0없이: F가 모두 그냥\u00a0F. ▶\u00a0쳐\u00a0보기: 건반에서 차례로 쳐요.') : t('▶\u00a0Listen: the notes sound in turn, each lit, with its name. ▶\u00a0Tap\u00a0it: play them in order on the keys.', '▶\u00a0듣기: 음이 차례로 울리고, 음표마다 불이 켜지며 이름이 나와요. ▶\u00a0쳐\u00a0보기: 건반에서 차례로 쳐요.')}</div>
      <div style={{display:'flex',flexDirection:'column',gap:6}}>{staffRows}</div>
      <div style={{maxWidth:n * 44,margin:'8px auto 0'}}><SacKeys d0={d0} n={n} o={{ lit: P.keyLit == null ? [] : [P.keyLit], miss: P.miss, H: 120 }} onTap={P.onTap}/></div>
      {skgMsgLine(P.msg, P.miss)}
      <div style={{display:'flex',gap:6,justifyContent:'center',flexWrap:'wrap'}}>
        <button className="ghost-btn" style={{minHeight:44}} onClick={() => P.listen(false)}>{t('▶ Listen', '▶ 듣기')}</button>
        {page === 2 && <button className="ghost-btn" style={{minHeight:44}} onClick={() => P.listen(true)}>{t('▶ Without it', '▶ 조표 없이')}</button>}
        <button className="ghost-btn" style={{minHeight:44}} onClick={P.tapMode}>{t('▶ Tap it', '▶ 쳐 보기')}</button>
      </div>
    </div>
  );
}
// page 6: pick a key: its key signature, its scale; ▶ Listen, ▶ Tap it
function SkgFivePad() {
  const [key, setKey] = useState('D');
  return <SkgFivePadKey key={key} k={key} setKey={setKey}/>;
}
function SkgFivePadKey({ k, setKey }) {
  const items = skgScale(k), [d0, n] = skgScaleKeys(k), P = useSkgPlayer(items, k);
  return (
    <div className="try-box" style={actBox} data-skg="pad6">
      <div style={actTitle}>{t('Name the key', '조 이름')}</div>
      <div style={actNote}>{t('Pick a key: its key signature and its scale. ▶\u00a0Listen, or ▶\u00a0Tap\u00a0it on the keys.', '조를 골라요: 그 조의 조표와 음계. ▶\u00a0듣기, 또는 건반에서 ▶\u00a0쳐\u00a0보기.')}</div>
      <div style={{display:'flex',gap:6,justifyContent:'center',flexWrap:'wrap',margin:'0 0 8px'}}>{SKG_FIVE.map(x => <button key={x} className={'chip' + (x === k ? ' active' : '')} style={{minHeight:44,minWidth:52,fontSize:16,fontWeight:900}} onClick={() => { P.stop(); setKey(x); }}>{sscSx(prettyNote(x))}</button>)}</div>
      <div style={{textAlign:'center',fontSize:16,fontWeight:900,color:BK.ink,margin:'0 0 2px'}}>{sscSx(skgKeyName(k))} <span style={{color:BK.muted,fontWeight:800,fontSize:14}}>· {sscSx(skgCountWords(k) + (SKG_KEY[k][1] ? ': ' + skgSignNames(k).join('\u00a0') : ''))}</span></div>
      <SkgStaff items={items} k={k} width={SKG_SCR} o={{ D: 25, ksCol: PEN_C, hl: P.lit >= 0 ? [P.lit] : [] }}/>
      <div style={{maxWidth:n * 44,margin:'8px auto 0'}}><SacKeys d0={d0} n={n} o={{ lit: P.keyLit == null ? [] : [P.keyLit], miss: P.miss, H: 120 }} onTap={P.onTap}/></div>
      {skgMsgLine(P.msg, P.miss)}
      <div style={{display:'flex',gap:6,justifyContent:'center'}}>
        <button className="ghost-btn" style={{minHeight:44}} onClick={() => P.listen(false)}>{t('▶ Listen', '▶ 듣기')}</button>
        <button className="ghost-btn" style={{minHeight:44}} onClick={P.tapMode}>{t('▶ Tap it', '▶ 쳐 보기')}</button>
      </div>
    </div>
  );
}

// ── the book on screen: the opener is the lesson's head, every other page a step ──
function SkgLearn({ onStart }) {
  const pages = skgLbPages(true);
  const opener = pages[0];
  return (
    <Lesson id="key-signatures" title={bkChapterName('key-signatures')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="key-signatures"><div className="lb-screen lb-open" style={{display:'flex',flexDirection:'column',gap:12,margin:'0 0 8px'}}>{lbWordsFirst(opener.props.children)}</div></BkChapterCtx.Provider></LbScreenCtx.Provider>}>
      {pages.slice(1).map((pg, i) => (
        <Step key={i} title={<span>{pg.props.title}</span>} storeAs={'k' + (i + 1)}>
          <LbScreenPage page={pg}/>
        </Step>
      ))}
    </Lesson>
  );
}

// ── the drill, after page 6, in the book's order: which key (1), what it changes (2), reading in G and F (3), with
// accidentals (4), all five keys (5), writing it (6), listening (7), the bass staff (8); 9 extra (three sharps or flats) ──
const SKG_LEVELS = [
  { n: 1, label: 'Which key: C, G or F?', kind: 'name3', time: 8 },
  { n: 2, label: 'Which notes change?', kind: 'which', time: 9 },
  { n: 3, label: 'Name the coral note', kind: 'note', time: 10 },
  { n: 4, label: 'Key signature and accidental', kind: 'acc', time: 12 },
  { n: 5, label: 'Which key? All five', kind: 'name5', time: 9 },
  { n: 6, label: 'Which is written right?', kind: 'write', time: 12 },
  { n: 7, label: 'Listen: right or wrong?', kind: 'ear', time: 14, noPrint: true },
  { n: 8, label: 'The bass staff', kind: 'bass', time: 11 },
  { n: 9, label: 'Extra: three sharps or flats', kind: 'three', time: 10 },
];
Object.assign(LEVEL_KO, {
  'Which key: C, G or F?': '어떤 조? C, G, F', 'Which notes change?': '바뀌는 음', 'Name the coral note': '산호색 음 이름', 'Key signature and accidental': '조표와 임시표',
  'Which key? All five': '어떤 조? 다섯 가지', 'Which is written right?': '바르게 쓴 조표', 'Listen: right or wrong?': '듣기: 맞았을까?', 'The bass staff': '낮은음자리표 오선',
  'Extra: three sharps or flats': '더 해 보기: 샤프나 플랫 셋',
});
// a key's sign on a letter, as a name; the signs a letter may take here (never E♯, B♯, C♭, F♭)
const skgNm = (d, acc) => sacNm(d, acc);
const skgKeySign = (key) => SKG_KEY[key][0];
// fillers: other letters than the key's changed ones and than x, a step or two from x
const skgFill = (x, lo, hi, avoid = []) => pick([x - 2, x - 1, x + 1, x + 2, x + 3].filter(v => v >= lo && v <= hi && (v - x) % 7 !== 0 && !avoid.includes(dName(v))));
// where the key's changed letters sit in a range (every octave)
const skgDsOf = (key, lo, hi) => { const L = Object.keys(skgMap(key)); const out = []; for (let d = lo; d <= hi; d++) if (L.includes(dName(d))) out.push(d); return out; };
function genSkgQuestion(lv, prev) {
  const uid = Math.random(), pk = prev && prev.key;
  const again = (f, p = 0) => { const pp = /[?&]print=1/.test(location.search) ? 0 : p; for (let g = 0; g < 40; g++) { const q = f(); if (q.key !== pk || Math.random() < pp) return { ...q, uid }; } return { ...f(), uid }; };
  const nameQ = (kind, pool, clef = 'treble', weight, p = 0) => again(() => {
    const k = weight && Math.random() < 0.6 ? pick(weight) : pick(pool), others = shuffle(pool.filter(x => x !== k)).slice(0, Math.min(3, pool.length - 1));
    return { kind, sub: 'name', k, clef, items: SKG_ALONE, key: kind + k + clef, answer: k, choices: shuffle([k, ...others]) }; }, p);
  // a coral note to name in a bar of four (the key's letter in 6 of 10, both octaves; another letter otherwise)
  const noteQ = (kind, keys, clef, lo, hi) => again(() => {
    const k = pick(keys), on = Math.random() < 0.6, Ls = Object.keys(skgMap(k));
    const x = on ? pick(skgDsOf(k, lo, hi)) : pick(Array.from({ length: hi - lo + 1 }, (_, i) => lo + i).filter(d => !Ls.includes(dName(d)))), at = pick([0, 1, 2, 3]);
    const notes = [0, 1, 2, 3].map(i => i === at ? ['q', 1, x] : ['q', 1, skgFill(x, lo, hi, Ls)]);
    const items = [...notes, ['||']], n = skgRead(items, k)[at], ans = sacNameTxt(n), s = skgKeySign(k), sAcc = SAC_ACC[s];
    const other = on ? skgNm(x, 0) : sacOk(x, s) ? skgNm(x, sAcc) : null, nbs = [x - 1, x + 1].filter(v => !Ls.includes(dName(v))), nb = skgNm(nbs.length ? pick(nbs) : x + 2, 0);
    const ch = [...new Set([ans, other || skgNm(x, on ? 0 : -sAcc), nb])];
    return { kind, sub: 'note', k, clef, items, at, key: kind + k + x + at, answer: ans, choices: shuffle(ch) }; });
  if (lv.kind === 'name3') return nameQ('name3', ['C', 'G', 'F'], 'treble', null, 0.3);
  if (lv.kind === 'name5') return nameQ('name5', SKG_FIVE);
  if (lv.kind === 'three') return nameQ('three', ['C', 'G', 'D', 'A', 'F', 'Bb', 'Eb'], Math.random() < 0.3 ? 'bass' : 'treble', ['A', 'Eb']);
  if (lv.kind === 'which') return again(() => {
    const k = pick(['G', 'F', 'D', 'Bb']), s = skgKeySign(k), O = SKG_ORDER[s].map(l => l + (s === '#' ? '♯' : '♭'));
    const ans = skgSignNames(k).join(' '), choices = [O[0], O[1], O[0] + ' ' + O[1], O[2]];
    return { kind: 'which', k, clef: 'treble', items: SKG_ALONE, key: 'w' + k, answer: ans, choices: shuffle(choices) }; }, 0.25);
  if (lv.kind === 'note') return noteQ('note', ['G', 'F'], 'treble', 29, 38);
  if (lv.kind === 'bass') return Math.random() < 0.5 ? nameQ('bass', SKG_FIVE, 'bass') : noteQ('bass', ['G', 'F', 'D', 'Bb'], 'bass', 17, 26);
  if (lv.kind === 'acc') return again(() => {   // two bars in a key with a natural (or another letter's accidental) in one of them
    const k = pick(['G', 'F', 'D', 'Bb']), Ls = Object.keys(skgMap(k)), x = pick(skgDsOf(k, 30, 37)), f = () => ['q', 1, skgFill(x, 29, 38, Ls)];
    const v = pick(['held', 'held', 'self', 'next', 'before', 'acc']), sb = v === 'next' ? 0 : pick([0, 1]);
    const bars = [[f(), f(), f(), f()], [f(), f(), f(), f()]];
    let at, y = x, sg = 'n';
    if (v === 'acc') { const s = skgKeySign(k), L = SKG_ORDER[s][SKG_KEY[k][1]]; y = pick([29, 30, 31, 32, 33, 34, 35, 36, 37, 38].filter(d => dName(d) === L)); sg = s; }
    if (v === 'held' || v === 'acc') { const ph = pick([1, 2, 3]), ps = Math.floor(Math.random() * ph); bars[sb][ps] = ['q', 1, y, sg]; bars[sb][ph] = ['q', 1, y]; at = sb * 4 + ph;
      if (v === 'acc' && Math.random() < 0.5) { const po = pick([0, 1, 2, 3]); bars[1 - sb][po] = ['q', 1, y]; at = (1 - sb) * 4 + po; } }
    else if (v === 'self') { const ps = pick([0, 1, 2, 3]); bars[sb][ps] = ['q', 1, x, 'n']; at = sb * 4 + ps; }
    else if (v === 'before') { const pb = pick([0, 1, 2]), ps = pb + 1 + Math.floor(Math.random() * (3 - pb)); bars[sb][ps] = ['q', 1, x, 'n']; bars[sb][pb] = ['q', 1, x]; at = sb * 4 + pb; }
    else { const ps = pick([0, 1, 2, 3]), po = pick([0, 1, 2, 3]); bars[0][ps] = ['q', 1, x, 'n']; bars[1][po] = ['q', 1, x]; at = 4 + po; }
    const items = [['ts', 4], ...bars[0], ['|'], ...bars[1], ['||']], n = skgRead(items, k)[at], ans = sacNameTxt(n), s = skgKeySign(k);
    const nbs = [n.d - 1, n.d + 1].filter(v2 => !Ls.includes(dName(v2))), nb = skgNm(nbs.length ? pick(nbs) : n.d + 2, 0), alt = sacOk(n.d, s) ? skgNm(n.d, n.acc ? 0 : SAC_ACC[s]) : skgNm(n.d, n.acc ? 0 : -SAC_ACC[s]);
    return { kind: 'acc', k, clef: 'treble', items, at, key: 'a' + k + x + v + at, answer: ans, choices: shuffle([...new Set([ans, alt, nb])]) }; });
  if (lv.kind === 'write') return again(() => {   // three key signatures: one right, two not (a sign on a wrong line or space, the wrong order, a sign missing, the other kind)
    const k = pick(['G', 'F', 'D', 'Bb']), clef = 'treble', right = skgKs(k, clef), s = skgKeySign(k);
    const shift = (list, i) => list.map(([g, d], j) => j === i ? [g, d + (d >= 37 ? -2 : d <= 31 ? 2 : pick([-2, 2]))] : [g, d]);
    const wrongs = right.length === 1 ? [shift(right, 0), [[s === '#' ? 'b' : '#', right[0][1]]], skgKs(s === '#' ? 'F' : 'G', clef)]
      : [[right[1], right[0]], shift(right, 1), [right[0]], shift(right, 0)];
    const opts = shuffle([right, ...shuffle(wrongs).slice(0, 2)]), L = ['1', '2', '3'], ans = L[opts.indexOf(right)];
    return { kind: 'write', k, clef, opts, key: 'r' + k + ans, answer: ans, choices: L }; });
  if (lv.kind === 'ear') return again(() => {   // a tune in a key, played right or with one of its changed notes plain
    const k = pick(['G', 'F', 'D', 'Bb']), Ls = Object.keys(skgMap(k)), x = pick(skgDsOf(k, 30, 37)), f = () => ['q', 1, skgFill(x, 29, 37, Ls)], X = ['q', 1, x];
    const tonic = SKG_SCALE_D[k] < 31 ? SKG_SCALE_D[k] + 7 : SKG_SCALE_D[k];
    const b0 = pick([[f(), X, f(), f()], [X, f(), f(), X], [f(), f(), X, f()]]), b1 = pick([[X, f()], [f(), X]]);
    const items = [['ts', 4], ...b0, ['|'], ...b1, ['h', 2, tonic], ['||']];
    const changed = skgOf(items, k, n => n.byKey), which = Math.random() < 0.5 ? 'right' : 'wrong', bad = which === 'wrong' ? pick(changed) : -1;
    return { kind: 'ear', k, clef: 'treble', items, bad, key: 'e' + k + which + Math.random(), answer: which, choices: ['right', 'wrong'] }; });
  return genSkgQuestion(SKG_LEVELS[0], prev);
}
function skgPlay(q) { stopClicks(); const r = skgRead(q.items, q.k), d0 = SKG_SCALE_D[q.k], ks = skgMap(q.k), key = [0, 2, 4, 7, 0].map((i, j) => ({ d: d0 + i, acc: ks[dName(d0 + i)] || 0, dur: j < 4 ? 0.5 : 2 }));
  return playMelody(key.concat(r.map((n, j) => ({ d: n.d, acc: j === q.bad ? 0 : n.acc, dur: n.dur }))), 96); }
const SKG_EAR_W = { right: () => t('All right', '모두 맞아요'), wrong: () => t('A wrong note', '틀린 음이 있어요') };
function SkgQuestion({ q, given, locked, onAnswer, pixel }) {
  const board = useBoard(q, given);
  const answered = useRef(false); answered.current = !!given;
  useEffect(() => { if (q.kind !== 'ear') return undefined; const tm = setTimeout(() => { if (!answered.current) skgPlay(q); }, 300); return () => { clearTimeout(tm); stopClicks(); }; }, [q.uid]);
  const isDone = !!given, btnCls = pixel ? 'pixel-choice' : 'choice-btn';
  const prompt = (txt) => <p style={pixel ? {fontSize:11.5,textAlign:'center',margin:'0 0 10px',lineHeight:1.7} : {fontSize:17,fontWeight:900,textAlign:'center',margin:'0 0 10px',color:'var(--text)',textWrap:'balance',wordBreak:'keep-all'}}>{txt}</p>;
  const st = (c) => !isDone ? '' : (String(c) === String(q.answer) ? ' good' : (String(given.ans) === String(c) ? ' bad' : ''));
  const grid = (min, render, pad = '12px 4px') => <div style={{display:'grid',gridTemplateColumns:'repeat(auto-fit,minmax(' + min + 'px,1fr))',gap:8}}>{q.choices.map(c => <button key={c} disabled={locked} onClick={() => { stopClicks(); onAnswer(c); }} className={btnCls + st(c)} style={{padding:pad,minHeight:44,wordBreak:'keep-all'}}>{render(c)}</button>)}</div>;
  const word = (s, sz = 18) => <span style={{fontSize:pixel ? 11 : sz,fontWeight:900}}>{sscSx(s)}</span>;
  const paper = (node, mw = 400) => <div style={{background:'#fff',borderRadius:pixel ? 0 : 8,padding:pixel ? 4 : '4px 0',margin:'0 auto 10px',maxWidth:mw}}>{node}</div>;
  const alone = (mw = 190) => paper(<SkgStaff items={SKG_ALONE} k={q.k} clef={q.clef} width={mw} full pad={SKG_AL_PAD} o={{ base: 54, ksRoom: q.kind === 'three' ? 3 : 2 }}/>, mw);
  const bars = (items) => { const rows = sacBars(items), box = Math.max(...rows.map(r => skgVbw(r, q.k, { D: 26 }, q.clef))); let off = 0;
    return paper(<div style={{display:'flex',flexDirection:'column',gap:2}}>{rows.map((r, i) => { const k = off, cnt = skgRead(r, q.k).length; off += cnt;
      return <SkgStaff key={i} items={r} k={q.k} clef={q.clef} width={box} left o={{ D: 26, hl: [q.at].filter(j => j != null && j >= k && j < k + cnt).map(j => j - k) }}/>; })}</div>, 300); };
  let body;
  if (q.sub === 'name') body = <>{prompt(t('Which major key has this key signature?', '이 조표는 어떤 장조일까요?'))}{alone()}{grid(120, c => word(skgKeyName(c), 18))}</>;
  else if (q.kind === 'which') body = <>{prompt(t('Which notes does this key signature change?', '이 조표가 바꾸는 음은?'))}{alone()}{grid(120, c => word(c, 20))}</>;
  else if (q.sub === 'note') body = <>{prompt(t('What is the coral note?', '산호색 음의 이름은?'))}{paper(<SkgStaff items={q.items} k={q.k} clef={q.clef} width={300} full o={{ D: 26, hl: [q.at] }}/>, 300)}{grid(90, c => word(c, 20))}</>;
  else if (q.kind === 'acc') body = <>{prompt(t('What is the coral note?', '산호색 음의 이름은?'))}{bars(q.items)}{grid(90, c => word(c, 20))}</>;
  else if (q.kind === 'write') body = <>{prompt(sscSx(t('Which is ' + skgKeyName(q.k) + '’s key signature, written right?', skgKeyName(q.k) + '의 조표를 바르게 쓴 것은?')))}
    <div style={{display:'grid',gridTemplateColumns:'1fr',gap:8}}>{q.choices.map((c, i) => <button key={c} disabled={locked} onClick={() => onAnswer(c)} className={btnCls + st(c)} style={{padding:'4px 8px',minHeight:44,display:'grid',gridTemplateColumns:'28px 1fr',alignItems:'center',gap:6}}>
      <div style={{fontWeight:900,fontSize:pixel ? 10 : 18}}>{c}</div><div style={{background:'#fff',borderRadius:6,maxWidth:220,width:'100%',margin:'0 auto'}}><SkgStaff items={SKG_ALONE} k="C" clef={q.clef} width={150} full pad={[22, 16]} o={{ ks: q.opts[i], base: 54, ksRoom: 2 }}/></div></button>)}</div></>;
  else body = <>{prompt(t('Listen: first the key, then the tune. Was every note right?', '들어 봐요: 먼저 조, 그다음 선율. 모든 음을 바르게 쳤을까요?'))}{bars(q.items)}
    <div style={{textAlign:'center',margin:'0 0 10px'}}><button className={pixel ? 'pixel-btn' : 'ghost-btn'} onClick={() => skgPlay(q)} style={pixel ? {fontSize:9} : {fontSize:15,padding:'8px 16px',minHeight:44}}>{t('▶ Hear it again', '▶ 다시 듣기')}</button></div>
    {grid(130, c => word(SKG_EAR_W[c](), 18))}</>;
  return <div><BoardTrack b={board} pixel={pixel}/>{body}</div>;
}
function skgCheck(q, ans) { return ans != null && String(ans) === String(q.answer); }
function skgAnswerLabel(q) {
  if (q.sub === 'name') return skgKeyName(q.k) + ' (' + skgCountWords(q.k) + (SKG_KEY[q.k][1] ? ': ' + skgSignNames(q.k).join('\u00a0') : '') + ')';
  if (q.kind === 'which') { const L = skgSigns(q.k).map(([, l]) => l); return q.answer + t(' (every ' + L.join(' and every ') + ')', ' (모든 ' + L.join('와 모든 ') + ')'); }
  if (q.kind === 'write') { const right = q.opts[q.choices.indexOf(q.answer)]; return q.answer + ': ' + right.map(([s, d]) => { const nm = dName(d) + (s === '#' ? '♯' : '♭'); return t(nm + ' on ' + skgWhere(d, q.clef), skgKo(skgWhere(d, q.clef) + '의 ' + nm)); }).join(t(', then ', ', 그다음 ')); }
  if (q.kind === 'ear') { if (q.answer === 'right') return t('every note right', '모든 음이 맞아요'); const n = skgRead(q.items, q.k)[q.bad], no = q.bad + 1;
    return t('a wrong note (note ' + no + ': ' + dName(n.d) + ' without its ' + (n.acc > 0 ? 'sharp' : 'flat') + ')', '틀린 음이 있어요 (' + no + '번째 음: ' + dName(n.d) + '를 ' + (n.acc > 0 ? '샤프' : '플랫') + ' 없이 쳤어요)'); }
  const n = skgRead(q.items, q.k)[q.at];
  return q.answer + (n.sign === 'n' ? t(' (the natural)', ' (내추럴)') : n.sign ? t(' (the accidental)', ' (임시표)') : n.natHeld ? t(' (the natural still holds)', ' (내추럴이 그대로예요)')
    : n.held ? t(' (the same bar: the accidental holds)', ' (같은 마디라 임시표가 그대로예요)') : n.back && n.byKey ? t(' (a new bar: the key signature again)', ' (새 마디라 다시 조표대로예요)')
    : n.byKey ? t(' (the key signature)', ' (조표)') : n.back ? t(' (a new bar: the accidental is over)', ' (새 마디라 임시표가 끝났어요)') : t(' (not in the key signature)', ' (조표에 없는 음)'));
}
Object.assign(KEYSIG_DRILL, { levels: SKG_LEVELS, generate: genSkgQuestion, check: skgCheck, answerLabel: skgAnswerLabel, Question: SkgQuestion, Learn: SkgLearn });
