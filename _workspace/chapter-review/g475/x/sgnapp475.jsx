// ─── Phase 475: chapter 20's pads (pages 2 to 6), the screen lesson and the drill ───
const SGN_BPM = 100;
const SGN_SCR = 270;   // the staff's reference width on a phone screen (chapter 19's)
const SGN_STOP = { fn: null };   // the pad that is sounding: a new ▶ Listen on another pad stops it
const SGN_PAD = { 2: () => t('Repeat signs', '도돌이표'), 3: () => t('1st and 2nd time bars', '1번 괄호와 2번 괄호'), 4: () => 'D.C. al Fine', 5: () => 'D.S. al Fine', 6: () => t('The pause', '늘임표') };
// the notes (and rests) of a road in its order: { d, dur, bar, j, rest } (a pause held twice as long, unless plain)
const sgnNotes = (bars, ord, plain) => ord.flatMap(n => bars[n - 1].n.map((nt, j) => ({ d: sskIsRest(nt[0]) ? 28 : nt[2], acc: 0, rest: sskIsRest(nt[0]), dur: nt[1] * (!plain && (bars[n - 1].pause || []).includes(j) ? 2 : 1), bar: n - 1, j })));
// playMelody with rests (silent, their time kept)
function sgnPlayMel(notes, bpm, onStep) {
  const ctx = getAudio(); if (!ctx) return [];
  const spb = 60 / bpm, t0 = ctx.currentTime + 0.1, timers = []; let tt = 0;
  notes.forEach((n, i) => { if (!n.rest) blip(ctx, t0 + tt * spb, 440 * Math.pow(2, (ivMidi({ d: n.d, acc: n.acc || 0 }) - 69) / 12), n.dur * spb * 0.9, 0.17, 'triangle');
    if (onStep) timers.push(setTimeout(() => onStep(i), (0.1 + tt * spb) * 1000)); tt += n.dur; });
  if (onStep) timers.push(setTimeout(() => onStep(-1), (0.1 + tt * spb) * 1000 + 200));
  return timers;
}
// why a step of the order goes where it does (the line under the pad while it plays)
function sgnWhy(bars, ord, s) {
  const n = ord[s], p = s > 0 ? ord[s - 1] : 0, pb = p ? bars[p - 1] : null, b = bars[n - 1], bar = t('Bar ' + n, n + '마디');
  if (s > 0 && n !== p + 1) {
    if (pb.dc) return bar + t(': D.C., back to the beginning', ': D.C.에서 처음으로');
    if (pb.ds) return bar + t(': D.S., back to the sign', ': D.S.에서 세뇨로');
    if (pb.tocoda) return bar + t(': To Coda, on to the coda', ': To Coda에서 코다로');
    if (pb.end) return bar + (bars.slice(0, p).some(x => x.start) && n > 1 ? t(': back to the start-repeat sign', ': 시작 도돌이표로') : t(': back to the beginning', ': 처음으로'));
    if (b.v === 2) return bar + t(': the 2nd time bar (the 1st skipped)', ': 1번 괄호를 건너뛰고 2번 괄호');
  }
  if (s === ord.length - 1 && b.fine && ord.length > n) return bar + t(': Fine, the end', ': Fine에서 끝');
  if (b.v === 1) return bar + t(': the 1st time bar', ': 1번 괄호');
  return bar;
}
// one pad: a road: ▶ Listen (each bar lit as it sounds, the reason when it jumps), ▶ Your turn (tap the bar numbers in
// order); page 6: ▶ Listen with the pauses, ▶ Without them
function SgnPad({ page }) {
  const [ex, setEx] = useState(0);
  return <SgnPadRoad key={ex} page={page} ex={ex} setEx={setEx}/>;
}
function SgnPadRoad({ page, ex, setEx }) {
  const pz = page === 6, bars = pz && ex ? SGN_ROAD6B : SGN_ROADS[page], rows = page === 5 ? [[0, 1], [2, 3], [4, 4]] : SGN_ROWS[page], ord = sgnOrder(bars);
  const [mode, setMode] = useState(null);   // null | 'listen' | 'tap'
  const [step, setStep] = useState(-1);
  const [note, setNote] = useState(null);
  const [got, setGot] = useState([]);
  const [miss, setMiss] = useState(null);
  const [msg, setMsg] = useState('');
  const timers = useRef([]), tapSnd = useRef(false), turnBtn = useRef(null);
  const clear = () => { const on = timers.current.length > 0 || tapSnd.current; timers.current.forEach(clearTimeout); timers.current = []; tapSnd.current = false; if (on) stopClicks(); };
  const meRef = useRef(null);
  meRef.current = () => { clear(); setStep(-1); setNote(null); setMiss(null); setMsg(''); setMode(null); };
  const me = useRef(() => meRef.current()).current;
  const release = () => { if (SGN_STOP.fn === me) SGN_STOP.fn = null; };
  useEffect(() => () => { clear(); release(); }, []);
  const take = () => { if (SGN_STOP.fn && SGN_STOP.fn !== me) SGN_STOP.fn(); SGN_STOP.fn = me; };
  function listen(plain) {
    take(); clear(); setMode('listen'); setMiss(null); setGot([]);
    const seq = sgnNotes(bars, ord, plain), stepOf = (k) => { let c = -1; for (let i = 0; i <= k; i++) if (i === 0 || seq[i].bar !== seq[i - 1].bar || seq[i].j === 0) c++; return c; };
    timers.current = sgnPlayMel(seq, SGN_BPM, (i) => {
      if (i < 0) { timers.current = []; release(); setStep(-1); setNote(null); setMsg(''); setMode(null); return; }
      const s = stepOf(i), x = seq[i], held = (bars[x.bar].pause || []).includes(x.j);
      setStep(s); setNote([x.bar, x.j]);
      setMsg(pz ? (held ? (plain ? t('No pause: on in time', '늘임표 없이: 박자대로') : t('The pause: held longer', '늘임표: 더 길게')) : '') : sgnWhy(bars, ord, s)); });
    if (!timers.current.length) { release(); setMode(null); }
  }
  function tapMode() { take(); clear(); setMode('tap'); setStep(-1); setNote(null); setGot([]); setMiss(null); setMsg(t('Tap the bar numbers in the order you play them.', '치는 차례대로 마디 번호를 눌러요.')); }
  function onBar(n) {
    if (mode !== 'tap') return;
    const k = got.length;
    if (ord[k] === n) {
      const g = [...got, n]; setGot(g); setMiss(null);
      clear(); sgnPlayMel(sgnNotes(bars, [n], false), SGN_BPM * 1.2); tapSnd.current = true;
      if (g.length === ord.length) { setMsg(t('✓ Right: ', '✓ 맞았어요: ') + ord.join(' ')); setMode(null); release(); setTimeout(() => { if (turnBtn.current) turnBtn.current.focus(); }, 0); }
      else setMsg(sgnWhy(bars, ord, k));
    } else { setMiss(n); setMsg(k === 0 ? t('Not bar ' + n + '. Start at bar 1.', n + '마디가 아니에요. 1마디부터 시작해요.') : t('Not bar ' + n + '. Follow the signs after bar ' + ord[k - 1] + '.', n + '마디가 아니에요. ' + ord[k - 1] + '마디 다음에는 기호를 따라가요.')); }
  }
  const litBar = mode === 'listen' && step >= 0 ? ord[step] - 1 : mode === 'tap' && got.length ? got[got.length - 1] - 1 : null;
  const o = { ts: 4, nums: !pz, D: 26, coral: SGN_CORAL[page], lit: litBar, hl: note ? [note] : [] };
  return (
    <div className="try-box" style={actBox} data-sgn={'pad' + page}>
      <div style={actTitle}>{SGN_PAD[page]()}</div>
      <div style={actNote}>{pz ? t('▶ Listen: the pauses held. ▶ Without them: every note in time.', '▶ 듣기: 늘임표대로 길게. ▶ 늘임표 없이: 모두 박자대로.')
        : t('▶ Listen: each bar lights up as it sounds. ▶ Your turn: tap the bar numbers in the order you play them.', '▶ 듣기: 울리는 마디에 불이 켜져요. ▶ 내 차례: 치는 차례대로 마디 번호를 눌러요.')}</div>
      {pz && <div style={{display:'flex',gap:6,justifyContent:'center',margin:'0 0 6px'}}>{[t('Over a note', '음표 위'), t('Over a rest', '쉼표 위')].map((w, i) => <button key={i} className={'chip' + (i === ex ? ' active' : '')} style={{minHeight:44}} onClick={() => setEx(i)}>{w}</button>)}</div>}
      <SgnRoad bars={bars} rows={rows} rw={SGN_SCR} o={o} label={pz && ex ? SGN_LABEL6B() : SGN_LABEL[page]()}/>
      {pz && <div style={{margin:'10px 0 0'}}><SgnBeats bars={bars} stack h={30}/></div>}
      {!pz && mode !== 'tap' && <div style={{margin:'8px 0 0'}}>{sgnOrderRow(ord, 16, mode === 'listen' ? step : -1)}</div>}
      {!pz && mode === 'tap' && <div style={{display:'flex',flexDirection:'column',gap:8,margin:'8px 0 0'}}>
        <div style={{display:'flex',justifyContent:'center',flexWrap:'wrap',gap:4,minHeight:30,fontSize:16,fontWeight:900}}>{ord.map((n, j) => <span key={j} style={{minWidth:26,textAlign:'center',padding:'2px 4px',borderRadius:6,border:'1.5px ' + (j < got.length ? 'solid ' + PEN_N : 'dashed rgba(38,41,107,0.35)'),color:BK.ink}}>{j < got.length ? got[j] : ' '}</span>)}</div>
        <div style={{display:'grid',gridTemplateColumns:'repeat(' + (bars.length > 4 ? 3 : bars.length) + ', 44px)',justifyContent:'center',gap:4}}>{bars.map((_, i) => <button key={i} className="chip" aria-label={t('Bar ' + (i + 1), (i + 1) + '마디')} style={{minHeight:44,minWidth:44,width:44,padding:0,fontSize:18,fontWeight:900,borderColor:miss === i + 1 ? BK.coral : undefined,color:miss === i + 1 ? BK.coral : undefined}} onClick={() => onBar(i + 1)}>{i + 1}</button>)}</div>
      </div>}
      <div aria-live="polite" style={{textAlign:'center',fontSize:15,fontWeight:900,color:miss ? BK.coral : BK.ink,minHeight:22,margin:'6px 0',textWrap:'balance',wordBreak:'keep-all'}}>{msg}</div>
      <div style={{display:'flex',gap:6,justifyContent:'center',flexWrap:'wrap'}}>
        <button className="ghost-btn" style={{minHeight:44}} onClick={() => listen(false)}>{t('▶ Listen', '▶ 듣기')}</button>
        {pz ? <button className="ghost-btn" style={{minHeight:44}} onClick={() => listen(true)}>{t('▶ Without them', '▶ 늘임표 없이')}</button>
          : <button ref={turnBtn} className="ghost-btn" style={{minHeight:44}} onClick={tapMode}>{t('▶ Your turn', '▶ 내 차례')}</button>}
      </div>
    </div>
  );
}

// ── the book on screen: the opener is the lesson's head, every other page a step ──
function SgnLearn({ onStart }) {
  const pages = sgnLbPages(true);
  const opener = pages[0];
  return (
    <Lesson id="signs" title={bkChapterName('signs')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="signs"><div className="lb-screen lb-open" style={{display:'flex',flexDirection:'column',gap:12,margin:'0 0 8px'}}>{lbWordsFirst(opener.props.children)}</div></BkChapterCtx.Provider></LbScreenCtx.Provider>}>
      {pages.slice(1).map((pg, i) => (
        <Step key={i} title={<span>{pg.props.title}</span>} storeAs={'k' + (i + 1)}>
          <LbScreenPage page={pg}/>
        </Step>
      ))}
    </Lesson>
  );
}

// ── the drill, after page 6, in the book's order: what each sign tells you (1), the order with repeat signs (2), with
// 1st and 2nd time bars (3), D.C. al Fine (4), D.S. al Fine (5), how many bars (6), listening (7), all the roads (8);
// 9 extra (al Coda, with its key line above each question) ──
const SGN_LEVELS = [
  { n: 1, label: 'What does this sign tell you?', kind: 'mean', time: 9 },
  { n: 2, label: 'Repeat signs: the order', kind: 'rep', time: 12 },
  { n: 3, label: '1st and 2nd time bars: the order', kind: 'volta', time: 12 },
  { n: 4, label: 'D.C. al Fine: the order', kind: 'dc', time: 12 },
  { n: 5, label: 'D.S. al Fine: the order', kind: 'ds', time: 12 },
  { n: 6, label: 'How many bars do you play?', kind: 'count', time: 12 },
  { n: 7, label: 'Listen: right or wrong?', kind: 'ear', time: 36, noPrint: true },
  { n: 8, label: 'All the roads', kind: 'mix', time: 12 },
  { n: 9, label: 'Extra: al Coda', kind: 'coda', time: 14 },
];
Object.assign(LEVEL_KO, {
  'What does this sign tell you?': '기호의 뜻', 'Repeat signs: the order': '도돌이표: 치는 차례', '1st and 2nd time bars: the order': '1번 괄호와 2번 괄호: 치는 차례',
  'D.C. al Fine: the order': 'D.C. al Fine: 치는 차례', 'D.S. al Fine: the order': 'D.S. al Fine: 치는 차례', 'How many bars do you play?': '모두 몇 마디를 칠까요?',
  'All the roads': '여러 가지 길', 'Extra: al Coda': '더 해 보기: 코다(al Coda)',
});
// a bar of the drill's roads: C position, stepwise; 'end' bars finish on C
const SGN_RHY = [['q', 'q', 'q', 'q'], ['q', 'q', 'h'], ['h', 'q', 'q'], ['h', 'h'], ['q', 'h', 'q']];
function sgnRandBar(from, end) {
  const rhy = end ? pick([['q', 'q', 'h'], ['h', 'h'], ['w']]) : pick(SGN_RHY), out = []; let d = from;
  rhy.forEach((k, j) => { if (end && j === rhy.length - 1) d = 28; else { const nx = d + pick([-2, -1, -1, 1, 1, 2, 0]); d = Math.max(28, Math.min(32, nx)); } out.push(sgnQ(d, k)); });
  return out;
}
function sgnRandBars(n, endAt = []) {
  for (let g = 0; g < 30; g++) { let d = pick([28, 30, 32]); const bars = [];
    for (let i = 0; i < n; i++) { const e = i === n - 1 || endAt.includes(i), b = sgnRandBar(d, e); bars.push({ n: b }); d = b[b.length - 1][2]; }
    const sig = bars.map(b => b.n.map(x => x.join(',')).join(' ')); if (new Set(sig).size === n) return bars; }
  return Array.from({ length: n }, (_, i) => ({ n: sgnRandBar(28 + (i % 3), i === n - 1) }));
}
// the roads: a kind, with a mistake list (the wrong orders to offer, the wrong ways to play it; the first three are offered)
function sgnRoad(kind) {
  if (kind === 'rep') { const n = pick([4, 4, 5]), e = pick(n === 4 ? [1, 2, 3] : [2, 3]), s = pick([-1, -1, ...Array.from({ length: e }, (_, i) => i).filter(i => i > 0)]);
    const bars = sgnRandBars(n, e < n - 1 ? [e] : []); bars[e].end = true; if (s > 0) bars[s].start = true;
    return { bars, mis: s > 0 ? ['fromStart', 'noRep', 'lastOnly'] : ['noRep', 'twice', 'lastOnly'] }; }
  if (kind === 'volta') { const n = pick([4, 5]), v = n === 4 ? 2 : pick([2, 3]), s = pick([-1, -1, 1]), st = s > 0 && s < v;
    const bars = sgnRandBars(n, [v + 1]); bars[v].v = 1; bars[v].end = true; bars[v + 1].v = 2; if (st) bars[s].start = true; return { bars, mis: ['v1Again', 'noRep', ...(st ? ['fromStart'] : []), 'skipV1'] }; }
  if (kind === 'dc') { const n = pick([4, 5]), f = pick(n === 4 ? [1, 2] : [1, 2, 3]), bars = sgnRandBars(n, [f]); bars[f].fine = true; bars[n - 1].dc = true; return { bars, mis: ['noFine', 'fineFirst', 'dcToSign'] }; }
  if (kind === 'ds') { const n = 5, sg = pick([1, 2]), f = pick([sg + 1, sg + 1, sg, 3].filter(x => x >= sg && x <= 3)), bars = sgnRandBars(n, [f]); bars[sg].segno = true; bars[f].fine = true; bars[n - 1].ds = true; return { bars, mis: ['dsStart', 'noFine', 'fineFirst'] }; }
  if (kind === 'coda') { const ds = Math.random() < 0.4, n = 5, tc = pick([1, 2]), bars = sgnRandBars(n, [3]); bars[tc].tocoda = true; bars[3][ds ? 'ds' : 'dc'] = true; bars[3].al = 'coda'; bars[4].coda = true; if (ds) bars[pick([1, tc].filter(x => x <= tc))].segno = true;
    return { bars, mis: ['noCoda', 'codaFirst', ds ? 'dsStart' : 'codaEarly'] }; }
  if (kind === 'pause') { const bars = sgnRandBars(2); bars.forEach((b, i) => { b.pause = i === 0 || Math.random() < 0.5 ? [b.n.length - 1] : []; }); return { bars, mis: ['noPause'] }; }   // a pause before the end: one at the very end cannot be heard
  return sgnRoad(pick(['rep', 'volta', 'dc', 'ds']));
}
// a wrong order for a mistake (some made by hand: twice, skipV1, dcToSign, codaFirst, codaEarly, lastOnly)
function sgnWrong(bars, m) {
  const ord = sgnOrder(bars), to = (k) => Array.from({ length: k }, (_, i) => i + 1);
  if (m === 'twice') { const e = bars.findIndex(b => b.end); if (e < 0) return null; const s = bars.findIndex(b => b.start), from = s >= 0 ? s : 0, part = Array.from({ length: e - from + 1 }, (_, i) => from + i + 1);
    return [...to(e + 1), ...part, ...part, ...Array.from({ length: bars.length - e - 1 }, (_, i) => e + i + 2)]; }
  if (m === 'skipV1') return ord.filter((n, j) => !(bars[n - 1].v === 1 && j === ord.indexOf(n)));
  if (m === 'dcToSign') { const f = bars.findIndex(b => b.fine); return [...to(bars.length), ...Array.from({ length: Math.max(1, f) }, (_, i) => i + 2).slice(0, f)]; }
  if (m === 'codaFirst') return to(bars.length);
  if (m === 'codaEarly') { const tc = bars.findIndex(b => b.tocoda), c = bars.findIndex(b => b.coda); return tc < 0 || c < 0 ? null : [...to(tc + 1), c + 1]; }
  if (m === 'lastOnly') { const e = bars.findIndex(b => b.end); return e < 0 ? null : [...to(e + 1), e + 1, ...Array.from({ length: bars.length - e - 1 }, (_, i) => e + i + 2)]; }
  if (m === 'noPause') return null;
  return sgnOrder(bars, { [m]: true });
}
const SGN_MEAN = {
  end: () => t('Go back and play again', '돌아가서 한 번 더 쳐요'),
  start: () => t('Where the end-repeat sign goes back to', '끝 도돌이표에서 돌아갈 자리'),
  v1: () => t('Play this bar the first time only', '처음에만 치는 마디'),
  v2: () => t('The second time, play this bar instead', '두 번째에는 이 마디를 대신 쳐요'),
  dc: () => t('Go back to the beginning, then play up to Fine', '처음으로 돌아가 Fine까지 쳐요'),
  ds: () => t('Go back to the sign, then play up to Fine', '세뇨로 돌아가 Fine까지 쳐요'),
  segno: () => t('Where D.S. goes back to', 'D.S.가 돌아갈 자리'),
  fine: () => t('The end, after a D.C. or D.S.', 'D.C.나 D.S.로 돌아온 뒤에 끝나는 곳'),
  pause: () => t('Hold this note longer', '이 음을 더 길게 눌러요'),
};
const SGN_NAME = { end: () => t('the end-repeat sign', '끝 도돌이표'), start: () => t('the start-repeat sign', '시작 도돌이표'), v1: () => t('the 1st time bar', '1번 괄호'), v2: () => t('the 2nd time bar', '2번 괄호'),
  dc: () => 'D.C. al Fine', ds: () => 'D.S. al Fine', segno: () => t('the segno', '세뇨'), fine: () => 'Fine', pause: () => t('the pause', '늘임표') };
// the picture of a sign: a short road in which it does its job (the sign in coral; its partners in navy). The segno is on
// bar 2 (on bar 1 it would do what D.C. does) and every al Fine has its Fine
function sgnMeanBars(id) {
  const a = { n: [sgnQ(30, 'h'), sgnQ(32, 'h')] }, b = { n: [sgnQ(31, 'h'), sgnQ(28, 'h')] }, c = { n: [sgnQ(29, 'h'), sgnQ(31, 'h')] };
  const pics = { end: [a, { ...b, end: true }], start: [a, { ...c, start: true }, { ...b, end: true }], v1: [a, { ...c, v: 1, end: true }, { n: [sgnQ(28, 'w')], v: 2 }], v2: [a, { ...c, v: 1, end: true }, { n: [sgnQ(28, 'w')], v: 2 }],
    dc: [a, { ...b, fine: true }, { ...c, dc: true }], fine: [a, { ...b, fine: true }, { ...c, dc: true }], ds: [a, { ...b, segno: true, fine: true }, { ...c, ds: true }], segno: [a, { ...b, segno: true, fine: true }, { ...c, ds: true }],
    pause: [a, { ...b, pause: [0] }] };
  return pics[id];
}
const SGN_CORAL_OF = { end: ['end'], start: ['start'], v1: ['v1'], v2: ['v2'], dc: ['dc'], ds: ['dc'], segno: ['segno'], fine: ['fine'], pause: ['pause'] };
function genSgnQuestion(lv, prev) {   // never the same answer twice running (the roads repeat their shapes; the notes change)
  for (let g = 0; g < 30; g++) { const q = genSgnOne(lv, prev); if (!prev || q.kind === 'ear' || (q.key !== prev.key && String(q.answer) !== String(prev.answer))) return q; }
  return genSgnOne(lv, prev);
}
function genSgnOne(lv, prev) {
  const uid = Math.random();
  if (lv.kind === 'mean') { const ids = Object.keys(SGN_MEAN); let id = pick(ids), g = 0; while (prev && prev.id === id && g++ < 10) id = pick(ids);
    const near = { end: ['start', 'dc'], start: ['end', 'segno'], v1: ['v2', 'end'], v2: ['v1', 'end'], dc: ['ds', 'fine'], ds: ['dc', 'segno'], segno: ['start', 'ds'], fine: ['dc', 'pause'], pause: ['fine', 'end'] }[id];
    const others = [...near, ...shuffle(ids.filter(x => x !== id && !near.includes(x))).slice(0, 1)];
    return { kind: 'mean', id, key: 'm' + id, bars: sgnMeanBars(id), answer: id, choices: shuffle([id, ...others]), uid }; }
  const kind = lv.kind === 'count' || lv.kind === 'mix' ? pick(['rep', 'volta', 'dc', 'ds']) : lv.kind === 'ear' ? pick(['rep', 'volta', 'dc', 'ds', 'pause']) : lv.kind;
  const { bars, mis } = sgnRoad(kind), ord = sgnOrder(bars), ans = ord.join(' ');
  if (lv.kind === 'ear') { const right = Math.random() < 0.5, m = right ? null : pick(mis), wrong = m && m !== 'noPause' ? sgnWrong(bars, m) : null;
    const ok = !right && (m === 'noPause' || (wrong && wrong.join(' ') !== ans));
    return { kind: 'ear', road: kind, bars, play: ok && wrong ? wrong : ord, plain: ok && m === 'noPause', mis: ok ? m : null, key: 'e' + uid, answer: ok ? 'wrong' : 'right', choices: ['right', 'wrong'], uid }; }
  if (lv.kind === 'count') { const L = ord.length, alts = mis.map(m => sgnWrong(bars, m)).filter(Boolean).map(w => w.length);
    const ch = [...new Set([L, ...alts, bars.length, L + 2, L - 2].filter(x => x > 0))].slice(0, 4);
    return { kind: 'count', road: kind, bars, key: 'c' + L, answer: String(L), choices: shuffle(ch.map(String)), uid }; }
  const wrongs = [...new Set(mis.map(m => sgnWrong(bars, m)).filter(Boolean).map(w => w.join(' ')).filter(w => w !== ans))];
  return { kind: 'order', road: kind, bars, key: 'o' + kind + ans, answer: ans, choices: shuffle([ans, ...wrongs.slice(0, 3)]), uid };
}
const sgnRows = (bars) => bars.length <= 3 ? [[0, bars.length - 1]] : bars.length === 4 ? [[0, 1], [2, 3]] : [[0, 1], [2, 4]];
function sgnPlayQ(q) { stopClicks(); const ord = q.play || sgnOrder(q.bars); return sgnPlayMel(sgnNotes(q.bars, ord, q.plain), SGN_BPM); }
const SGN_EAR_W = { right: () => t('Played right', '바르게 쳤어요'), wrong: () => t('Played wrong', '잘못 쳤어요') };
function SgnQuestion({ q, given, locked, onAnswer, pixel }) {
  const board = useBoard(q, given);
  const answered = useRef(false); answered.current = !!given;
  useEffect(() => { if (q.kind !== 'ear') return undefined; const tm = setTimeout(() => { if (!answered.current) sgnPlayQ(q); }, 300); return () => { clearTimeout(tm); stopClicks(); }; }, [q.uid]);
  const isDone = !!given, btnCls = pixel ? 'pixel-choice' : 'choice-btn';
  const prompt = (txt) => <p style={pixel ? {fontSize:11.5,textAlign:'center',margin:'0 0 10px',lineHeight:1.7} : {fontSize:17,fontWeight:900,textAlign:'center',margin:'0 0 10px',color:'var(--text)',textWrap:'balance',wordBreak:'keep-all'}}>{txt}</p>;
  const st = (c) => !isDone ? '' : (String(c) === String(q.answer) ? ' good' : (String(given.ans) === String(c) ? ' bad' : ''));
  const grid = (min, render, pad = '12px 4px') => <div style={{display:'grid',gridTemplateColumns:'repeat(auto-fit,minmax(' + min + 'px,1fr))',gap:8}}>{q.choices.map(c => <button key={c} disabled={locked} onClick={() => { stopClicks(); onAnswer(c); }} className={btnCls + st(c)} style={{padding:pad,minHeight:44,wordBreak:'keep-all'}}>{render(c)}</button>)}</div>;
  const word = (s, sz = 18) => <span style={{fontSize:pixel ? 11 : sz,fontWeight:900}}>{s}</span>;
  const paper = (node, mw = 400) => <div style={{background:'#fff',borderRadius:pixel ? 0 : 8,padding:pixel ? 4 : '4px 0',margin:'0 auto 10px',maxWidth:mw}}>{node}</div>;
  // one staff size for every road and picture of the drill (rw 330: a wider road spaces its notes closer first)
  const road = (o = {}, label) => paper(<SgnRoad bars={q.bars} rows={q.kind === 'mean' ? [[0, q.bars.length - 1]] : sgnRows(q.bars)} rw={330} o={{ ts: 4, nums: q.kind !== 'mean', D: 24, ...o }} label={label || t('A road of ' + q.bars.length + ' bars', q.bars.length + '마디의 길')}/>, 360);
  const codaKey = q.road === 'coda' && <p style={{fontSize:pixel ? 10 : 14,fontWeight:700,textAlign:'center',margin:'-4px 0 10px',color:'var(--muted)',textWrap:'balance',wordBreak:'keep-all'}}>{sgnSx(t('To Coda 𝄌: after the D.C. or D.S., jump from here to the 𝄌 Coda.', 'To Coda 𝄌: D.C.나 D.S.로 돌아온 뒤, 여기서 𝄌 Coda로 건너뛰어요.'))}</p>;
  let body;
  if (q.kind === 'mean') body = <>{prompt(t('What does the coral sign tell you?', '산호색 기호가 알려 주는 것은?'))}{road({ coral: SGN_CORAL_OF[q.id] }, t('A short road; the coral sign is ' + SGN_NAME[q.id]() + '.', '짧은 길. 산호색 기호: ' + SGN_NAME[q.id]() + '.'))}
    {grid(220, c => word(SGN_MEAN[c](), 15), '10px 8px')}</>;
  else if (q.kind === 'order') body = <>{prompt(t('In what order do you play the bars?', '마디를 어떤 차례로 칠까요?'))}{codaKey}{road()}{grid(200, c => <span style={{fontSize:pixel ? 10 : 16,fontWeight:900,letterSpacing:'0.06em'}}>{c}</span>, '10px 4px')}</>;
  else if (q.kind === 'count') body = <>{prompt(t('How many bars do you play, from the first to the end?', '처음부터 끝까지 모두 몇 마디를 칠까요?'))}{road()}{grid(52, c => word(c, 20))}</>;
  else body = <>{prompt(t('Follow the road as you listen. Was it played right?', '들으면서 길을 따라가요. 바르게 쳤을까요?'))}{road()}
    <div style={{textAlign:'center',margin:'0 0 10px'}}><button className={pixel ? 'pixel-btn' : 'ghost-btn'} onClick={() => sgnPlayQ(q)} style={pixel ? {fontSize:9,minHeight:44} : {fontSize:15,padding:'8px 16px',minHeight:44}}>{t('▶ Hear it again', '▶ 다시 듣기')}</button></div>
    {grid(130, c => word(SGN_EAR_W[c](), 17))}</>;
  return <div><BoardTrack b={board} pixel={pixel}/>{body}</div>;
}
function sgnCheck(q, ans) { return ans != null && String(ans) === String(q.answer); }
// why the road goes that way (the answer line)
function sgnRoadWhy(bars) {
  const s = bars.findIndex(b => b.start), v = bars.some(b => b.v), e = bars.some(b => b.end), dc = bars.find(b => b.dc), ds = bars.find(b => b.ds);
  if (dc || ds) { const coda = (dc || ds).al === 'coda';
    return coda ? (dc ? t('back to the beginning, up to To Coda, then jump to the Coda', '처음으로 돌아가 To Coda까지 치고, 코다로 건너뛰어요') : t('back to the sign, up to To Coda, then jump to the Coda', '세뇨로 돌아가 To Coda까지 치고, 코다로 건너뛰어요'))
      : (dc ? t('back to the beginning, then up to Fine', '처음으로 돌아가 Fine까지') : t('back to the sign, then up to Fine', '세뇨로 돌아가 Fine까지')); }
  if (v) return s >= 0 ? t('the 1st time bar, back to the start-repeat sign at bar ' + (s + 1) + ', then the 2nd time bar', '1번 괄호를 치고 ' + (s + 1) + '마디의 시작 도돌이표로 돌아가서 2번 괄호로')
    : t('the 1st time bar, back to the beginning, then the 2nd time bar', '1번 괄호를 치고 처음으로 돌아가서 2번 괄호로');
  if (e) return s >= 0 ? t('back to the start-repeat sign at bar ' + (s + 1), (s + 1) + '마디의 시작 도돌이표로') : t('back to the beginning', '처음으로');
  return '';
}
const SGN_MIS_W = {
  noRep: () => t('the repeat was left out', '도돌이표에서 돌아가지 않았어요'),
  fromStart: () => t('it went back to the beginning, not to the start-repeat sign', '시작 도돌이표가 아니라 처음으로 돌아갔어요'),
  twice: () => t('it went back twice: the part was played three times', '두 번 돌아가서 세 번 쳤어요'),
  lastOnly: () => t('only the bar before the end-repeat sign was played again', '끝 도돌이표 앞 마디만 다시 쳤어요'),
  v1Again: () => t('the 1st time bar was played the second time too', '두 번째에도 1번 괄호를 쳤어요'),
  skipV1: () => t('the 1st time bar was left out the first time', '처음에 1번 괄호를 건너뛰었어요'),
  noFine: () => t('it went on past Fine', 'Fine에서 멈추지 않았어요'),
  fineFirst: () => t('it stopped at Fine before going back', '돌아가기 전에 Fine에서 멈췄어요'),
  dsStart: () => t('D.S. went back to the beginning, not to the sign', 'D.S.에서 세뇨가 아니라 처음으로 돌아갔어요'),
  dcToSign: () => t('D.C. went back to bar 2, not to the beginning', 'D.C.에서 처음이 아니라 2마디로 돌아갔어요'),
  noPause: () => t('the note with the pause was not held', '늘임표가 붙은 음을 길게 누르지 않았어요'),
  noCoda: () => t('it went on past To Coda', 'To Coda에서 코다로 가지 않았어요'),
  codaFirst: () => t('it played the coda without going back', '돌아가지 않고 코다를 쳤어요'),
  codaEarly: () => t('it went to the coda the first time', '돌아가기 전에 코다로 갔어요'),
};
function sgnAnswerLabel(q) {
  if (q.kind === 'mean') { const m = SGN_MEAN[q.id](); return SGN_NAME[q.id]() + ' (' + (LANG === 'ko' ? m : m[0].toLowerCase() + m.slice(1)) + ')'; }
  const ord = sgnOrder(q.bars).join(' '), why = sgnRoadWhy(q.bars), pz = q.road === 'pause';
  if (q.kind === 'count') return q.answer + t(' bars (', '마디 (') + ord + ')';
  if (q.kind === 'ear') { if (q.answer === 'right') return t('played right', '바르게 쳤어요') + (pz ? t(' (the pauses held)', ' (늘임표대로)') : ' (' + ord + ')');
    return t('played wrong (' + SGN_MIS_W[q.mis]() + (pz ? '' : '; the right road: ' + ord) + ')', '잘못 쳤어요. ' + SGN_MIS_W[q.mis]() + (pz ? '' : ' (바른 길: ' + ord + ')')); }
  return q.answer + (why ? ' (' + why + ')' : '');
}
Object.assign(SIGNS_DRILL, { levels: SGN_LEVELS, generate: genSgnQuestion, check: sgnCheck, answerLabel: sgnAnswerLabel, Question: SgnQuestion, Learn: SgnLearn });
