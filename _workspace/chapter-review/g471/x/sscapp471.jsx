// ─── Phase 471: chapter 16's pads (pages 2 to 6), the screen lesson and the drill ───
const SSC_GAP = 520;   // ms between the notes of a scale played to the child
const sscPlay = (start, semi, len = 0.5) => playKey(SSC_BASE[start] + semi, len);
// the pads: ▶ Listen (the scale up and down, each note lit) and ▶ Tap it (the child plays it up from the tonic)
const SSC_PAD = {
  2: { start: 'C', nums: true, steps: true, title: () => t('The major scale’s steps', '장음계의 걸음') },
  3: { start: 'C', fingers: true, title: () => t('Fingers on C major', 'C장조 손가락') },
  4: { start: 'C', nums: true, degrees: true, title: () => t('Find the degrees', '음의 번호 찾기') },
  5: { start: 'G', nums: true, steps: true, coral: [6], title: () => t('G major and its F♯', 'G장조와 F♯') },
  6: { start: 'F', steps: true, coral: [3], fingers: true, onlyRH: true, title: () => t('F major and its B♭', 'F장조와 B♭') },
};
const SSC_STOP = { fn: null };   // the pad that is sounding: a new ▶ Listen on another pad stops it
function SscPad({ page }) {
  const P = SSC_PAD[page], sc = sscScale(P.start);
  const [hand, setHand] = useState('RH');
  const [mode, setMode] = useState(null);   // null | 'listen' | 'tap'
  const [lit, setLit] = useState(null);
  const [done, setDone] = useState([]);
  const [miss, setMiss] = useState(null);
  const [msg, setMsg] = useState('');
  const timers = useRef([]);
  const clear = () => { timers.current.forEach(clearTimeout); timers.current = []; };
  const stopMe = () => { clear(); setLit(null); setMsg(''); setMode(null); };
  useEffect(() => () => { clear(); if (SSC_STOP.fn === stopMe) SSC_STOP.fn = null; }, []);
  const fing = P.fingers ? SCALES[P.start].octaves[1][hand] : null;
  const stepWord = (d) => SSC_STEPS[d] === 'half' ? t('half', '반') : t('whole', '온');
  const nameOf = (s) => sscNameTxt(s.name);
  function listen() {
    if (SSC_STOP.fn && SSC_STOP.fn !== stopMe) SSC_STOP.fn(); SSC_STOP.fn = stopMe;
    clear(); setMode('listen'); setDone([]); setMiss(null);
    const order = [0, 1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 0];
    order.forEach((d, j) => timers.current.push(setTimeout(() => { setLit(d); sscPlay(P.start, sc[d].semi);
      setMsg(P.degrees ? String(d + 1) + ' · ' + nameOf(sc[d]) : j > 0 && j < 8 ? nameOf(sc[d - 1]) + ' → ' + nameOf(sc[d]) + ': ' + stepWord(d - 1) : nameOf(sc[d])); }, j * SSC_GAP)));
    timers.current.push(setTimeout(() => { setLit(null); setMsg(''); setMode(null); }, order.length * SSC_GAP + 200));
  }
  function tapMode() { clear(); setMode('tap'); setLit(null); setDone([]); setMiss(null); setMsg(P.degrees ? t('Tap a key of the scale.', '음계의 건반을 눌러요.') : t('Start on ' + nameOf(sc[0]) + ' and play the scale up.', nameOf(sc[0]) + '에서 시작해 음계를 올라가요.')); }
  function onTap(k) {
    if (mode !== 'tap') { sscPlay(P.start, k.semi, 0.4); return; }
    const d = sc.findIndex(s => s.id === k.id);
    sscPlay(P.start, k.semi, 0.45);
    if (P.degrees) { if (d < 0) { setMiss(k.id); setLit(null); setMsg(t('Not in C major.', 'C장조 음계에 없는 음이에요.')); } else { setMiss(null); setLit(d); setMsg(t('Degree ' + (d + 1), (d + 1) + '번 음') + (d === 0 || d === 7 ? t(': the tonic', ': 으뜸음') : '')); } return; }
    const next = done.length;
    if (next >= 8) return;
    if (d === next) { const nd = [...done, d]; setDone(nd); setMiss(null); setLit(d);
      setMsg(nd.length === 8 ? t(nameOf(sc[0]) + ' major ✓', nameOf(sc[0]) + '장조 음계 ✓') : d === 0 ? nameOf(sc[0]) : nameOf(sc[d - 1]) + ' → ' + nameOf(sc[d]) + ': ' + stepWord(d - 1)); }
    else { setMiss(k.id); setMsg(next === 0 ? t('Start on ' + nameOf(sc[0]) + '.', nameOf(sc[0]) + '에서 시작해요.') : t('Not that key: the next step is a ' + (SSC_STEPS[next - 1] === 'half' ? 'half' : 'whole') + ' step.', '그 건반이 아니에요: 다음은 ' + (SSC_STEPS[next - 1] === 'half' ? '반' : '온') + ' 걸음이에요.')); }
  }
  const o = { nums: P.nums, steps: P.steps, coral: P.coral, fingers: fing, hand: P.fingers ? (hand === 'RH' ? t('RIGHT HAND', '오른손') : t('LEFT HAND', '왼손')) : null, lit, done: mode === 'tap' && !P.degrees ? done : [], miss,
    arrow: page === 3 ? (hand === 'RH' ? { from: 2, to: 3, label: t('thumb under', '엄지 밑으로 넣기'), over: false } : { from: 4, to: 5, label: t('3 over', '3번 넘기기'), over: true }) : null };
  return (
    <div className="try-box" style={actBox} data-ssc={'pad' + page}>
      <div style={actTitle}>{P.title()}</div>
      <div style={actNote}>{P.degrees
        ? t('▶ Listen: the scale up and down with its numbers. ▶ Tap it: tap any key of the scale to see its number.', '▶ 듣기: 음계가 번호와 함께 올라갔다 내려와요. ▶ 쳐 보기: 음계의 건반을 눌러 번호를 봐요.')
        : t('▶ Listen: the scale up and down, each note lit. ▶ Tap it: play it up from ' + nameOf(sc[0]) + ', one key at a time.', '▶ 듣기: 음계가 올라갔다 내려오고, 치는 건반에 불이 켜져요. ▶ 쳐 보기: ' + nameOf(sc[0]) + '에서부터 한 건반씩 올라가요.')}</div>
      {P.fingers && !P.onlyRH && <div style={{display:'flex',gap:5,justifyContent:'center',marginBottom:8}}>{['RH', 'LH'].map(h => <button key={h} className={'chip' + (h === hand ? ' active' : '')} onClick={() => { clear(); setHand(h); setMode(null); setLit(null); setDone([]); setMiss(null); setMsg(''); }}>{h === 'RH' ? t('Right hand', '오른손') : t('Left hand', '왼손')}</button>)}</div>}
      <div style={{maxWidth:460,margin:'0 auto'}}><SscKeys start={P.start} o={o} onTap={onTap}/></div>
      <div style={{textAlign:'center',fontSize:15,fontWeight:900,color:miss ? BK.coral : BK.ink,minHeight:22,margin:'6px 0'}}>{msg}</div>
      <div style={{display:'flex',gap:6,justifyContent:'center'}}>
        <button className="ghost-btn" onClick={listen}>{t('▶ Listen', '▶ 듣기')}</button>
        <button className="ghost-btn" onClick={tapMode}>{t('▶ Tap it', '▶ 쳐 보기')}</button>
      </div>
    </div>
  );
}

// ── the book on screen: the opener is the lesson's head, every other page a step. Its id is the chapter's own, as in
// every other chapter (the old 'scales-major' and 'scales-minor' lessons are gone; chapterSteps skips their old ticks) ──
function SscLearn({ onStart }) {
  const pages = sscLbPages(true);
  const opener = pages[0];
  return (
    <Lesson id="scales" title={bkChapterName('scales')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="scales"><div className="lb-screen lb-open" style={{display:'flex',flexDirection:'column',gap:12,margin:'0 0 8px'}}>{lbWordsFirst(opener.props.children)}</div></BkChapterCtx.Provider></LbScreenCtx.Provider>}>
      {pages.slice(1).map((pg, i) => (
        <Step key={i} title={pg.props.title}>
          <LbScreenPage page={pg}/>
        </Step>
      ))}
    </Lesson>
  );
}

// ── the drill, after page 6, in the book's order: steps (1 to 3), fingering (4), degrees (5), names (6), listening (7);
// 8 and 9 are extra (D and B♭ major; the harmonic minors' raised 7th) ──
const SSC_LEVELS = [
  { n: 1, label: 'Whole or half?', kind: 'step', time: 8 },
  { n: 2, label: 'Where is the half step?', kind: 'half', time: 8 },
  { n: 3, label: 'Build the scale', kind: 'build', time: 20 },
  { n: 4, label: 'Which finger?', kind: 'finger', time: 9 },
  { n: 5, label: 'Which degree?', kind: 'degree', time: 8 },
  { n: 6, label: 'Name the note', kind: 'name', time: 9 },
  { n: 7, label: 'Listen: a major scale?', kind: 'ear', time: 14, noPrint: true },
  { n: 8, label: 'Extra: D and B♭ major', kind: 'acc2', time: 9 },
  { n: 9, label: 'Extra: harmonic minor, the raised 7th', kind: 'minor7', time: 9 },
];
Object.assign(LEVEL_KO, {
  'Whole or half?': '온 걸음? 반 걸음?', 'Where is the half step?': '반 걸음은 어디?', 'Build the scale': '음계 만들기', 'Which finger?': '몇 번 손가락?',
  'Which degree?': '몇 번 음?', 'Name the note': '음이름 맞히기', 'Listen: a major scale?': '듣기: 장음계일까요?',
  'Extra: D and B♭ major': '더 해 보기: D장조와 B♭장조', 'Extra: harmonic minor, the raised 7th': '더 해 보기: 화성단음계의 올린 7번 음',
});
const SSC_KEYS3 = ['C', 'G', 'F'];
const SSC_PAIRS_ALL = ['1–2', '2–3', '3–4', '4–5', '5–6', '6–7', '7–8'];
// a wrong note for the ear level: [degree, half steps]
const SSC_WRONG = [[2, -1], [3, 1], [6, -1], [5, -1], [1, -1]];
const SSC_ACC2 = { D: ['F♯ and C♯', ['F♯ and G♯', 'C♯ and G♯', 'B♭ and E♭']], Bb: ['B♭ and E♭', ['B♭ and A♭', 'E♭ and A♭', 'F♯ and C♯']] };
// the one sign of G and F major, with a wrong spelling of it (each letter once: F♯, never G♭) and two other signs
const SSC_ACC1 = { G: ['F♯', ['G♭', 'C♯', 'B♭']], F: ['B♭', ['A♯', 'E♭', 'F♯']] };
const SSC_MIN7 = { A: ['G♯', ['G', 'F♯', 'A♯']], E: ['D♯', ['D', 'C♯', 'F♯']], D: ['C♯', ['C', 'B♭', 'D♯']] };
const sscScaleName = (k) => t(sscNameTxt(k) + ' major', sscNameTxt(k) + '장조 음계');
function genSscQuestion(lv, prev) {
  const uid = Math.random(), pk = prev && prev.key;
  const again = (f) => { for (let g = 0; g < 20; g++) { const q = f(); if (q.key !== pk) return { ...q, uid }; } return { ...f(), uid }; };
  const sc8 = (k) => sscScale(k);
  const k3 = () => pick(SSC_KEYS3);
  if (lv.kind === 'step') return again(() => { const k = k3(), w = Math.random() < 0.5 ? 'half' : 'whole', d = pick([0, 1, 2, 3, 4, 5, 6].filter(i => SSC_STEPS[i] === w));   // half as often as whole
    return { kind: 'step', start: k, d, key: k + d, answer: SSC_STEPS[d], choices: ['whole', 'half'] }; });
  if (lv.kind === 'half') return again(() => { const k = k3(), ans = pick(['3–4', '7–8']), wrong = sampleN(SSC_PAIRS_ALL.filter(p => p !== '3–4' && p !== '7–8'), 3);
    return { kind: 'half', start: k, key: k + ans, answer: ans, choices: shuffle([ans, ...wrong]) }; });
  if (lv.kind === 'build') return again(() => { const k = k3(); return { kind: 'build', start: k, key: 'b' + k }; });
  if (lv.kind === 'finger') return again(() => { const k = k3(), hand = pick(['RH', 'LH']), d = Math.floor(Math.random() * 8);
    return { kind: 'finger', start: k, hand, d, key: k + hand + d, answer: SCALES[k].octaves[1][hand][d], choices: [1, 2, 3, 4, 5] }; });
  if (lv.kind === 'degree') return again(() => { const k = k3(), d = Math.floor(Math.random() * 8), ans = d + 1;
    const near = [1, 2, 3, 4, 5, 6, 7, 8].filter(v => v !== ans).sort((a, z) => Math.abs(a - ans) - Math.abs(z - ans)).slice(0, 4);
    return { kind: 'degree', start: k, d, key: k + d, answer: String(ans), choices: [ans, ...sampleN(near, 3)].sort((a, z) => a - z).map(String) }; });
  if (lv.kind === 'name') return again(() => {
    if (Math.random() < 0.3) { const k = pick(['G', 'F']), [acc, others] = SSC_ACC1[k];
      return { kind: 'name', sub: 'acc', start: k, key: 'a' + k, answer: acc, choices: shuffle([acc, ...others]) }; }
    const k = k3(), sc = sc8(k), d = 1 + Math.floor(Math.random() * 6), ans = sscNameTxt(sc[d].name);
    const L = sc[d].name[0], nb = [d - 1, d + 1, d + 2 <= 7 ? d + 2 : d - 2, d - 2 >= 0 ? d - 2 : d + 3].map(i => sscNameTxt(sc[i].name));
    const wrong = new Set([L !== ans ? L : null, ...nb].filter(x => x && x !== ans));   // its own letter, or names from the same scale (never E♯)
    return { kind: 'name', sub: 'deg', start: k, d, key: k + d, answer: ans, choices: shuffle([ans, ...sampleN([...wrong], 3)]) };
  });
  if (lv.kind === 'ear') return again(() => { const k = k3(), right = Math.random() < 0.5, w = right ? null : pick(SSC_WRONG);
    return { kind: 'ear', start: k, wrong: w, key: k + (w ? w.join() : 'ok') + Math.random(), answer: right ? 'right' : 'wrong', choices: ['right', 'wrong'] }; });
  if (lv.kind === 'acc2') return again(() => { const k = pick(['D', 'Bb']), [a, w] = SSC_ACC2[k];
    if (Math.random() < 0.5) return { kind: 'acc2', rev: true, start: k, key: 'r' + k, answer: k, choices: shuffle(['D', 'Bb', 'G', 'F']) };   // which scale has these two signs?
    return { kind: 'acc2', start: k, key: k, answer: a, choices: shuffle([a, ...w]) }; });
  return again(() => { const k = pick(['A', 'E', 'D']), [a, w] = SSC_MIN7[k]; return { kind: 'minor7', start: k, key: 'm' + k, answer: a, choices: shuffle([a, ...w]) }; });
}
function sscPlayScale(q) {
  const ctx = getAudio(); if (!ctx) return;
  stopClicks();
  const base = 60 + SSC_BASE[q.start], t0 = ctx.currentTime + 0.15;
  SSC_MAJOR.forEach((o, d) => { const semi = o + (q.wrong && q.wrong[0] === d ? q.wrong[1] : 0);
    blip(ctx, t0 + d * 0.42, 440 * Math.pow(2, (base + semi - 69) / 12), 0.4, 0.18, 'triangle'); });
}
const SSC_RW = { right: () => t('A major scale', '장음계예요'), wrong: () => t('A wrong note', '틀린 음이 있어요') };
const SSC_SW = { whole: () => t('Whole step', '온 걸음'), half: () => t('Half step', '반 걸음') };
const sscPair = (p) => LANG === 'ko' ? p[0] + ('245'.includes(p[0]) ? '와 ' : '과 ') + p.slice(2) + ' 사이' : p.replace('–', ' to ');   // 2와, 4와, 5와; 1과, 3과, 6과, 7과
const sscAcc2Txt = (c) => LANG === 'ko' ? c.replace(' and ', ', ') : c;
function SscQuestion({ q, given, locked, onAnswer, pixel }) {
  const board = useBoard(q, given);
  const [bs, setBs] = useState({ uid: q.uid, done: [0], miss: null });   // the build level's keys played, for this question only
  const cur = bs.uid === q.uid ? bs : { uid: q.uid, done: [0], miss: null }, done = cur.done, miss = cur.miss;
  useEffect(() => { if (q.kind === 'ear') { const tm = setTimeout(() => sscPlayScale(q), 250); return () => { clearTimeout(tm); stopClicks(); }; } return undefined; }, [q.uid]);
  const isDone = !!given;
  const btnCls = pixel ? 'pixel-choice' : 'choice-btn';
  const prompt = (txt) => <p style={pixel ? {fontSize:11.5,textAlign:'center',margin:'0 0 10px',lineHeight:1.7} : {fontSize:15,fontWeight:700,textAlign:'center',margin:'0 0 10px',color:'var(--muted)',textWrap:'balance',wordBreak:'keep-all'}}>{txt}</p>;
  const big = (txt) => <div style={{textAlign:'center',fontSize:pixel ? 14 : 22,fontWeight:900,margin:'0 0 8px',color:pixel ? 'var(--brass)' : BK.ink}}>{txt}</div>;
  const st = (c) => !isDone ? '' : (String(c) === String(q.answer) ? ' good' : (String(given.ans) === String(c) ? ' bad' : ''));
  const grid = (cols, render, pad = '14px 2px') => <div style={{display:'grid',gridTemplateColumns:'repeat(' + cols + ',minmax(0,1fr))',gap:8}}>{q.choices.map(c => <button key={c} disabled={locked} onClick={() => { if (q.kind === 'ear') stopClicks(); onAnswer(c); }} className={btnCls + st(c)} style={{padding:pad}}>{render(c)}</button>)}</div>;
  const word = (s, sz = 17) => <span style={{fontSize:pixel ? 11 : sz,fontWeight:900}}>{s}</span>;
  const paper = (node) => <div style={{background:'#fff',borderRadius:pixel ? 0 : 8,padding:pixel ? 4 : 0,margin:'0 auto 10px',maxWidth:440}}>{node}</div>;
  let body;
  if (q.kind === 'step') body = <>{big(sscScaleName(q.start))}{prompt(t('Between the two coral keys: a whole step or a half step?', '산호색 두 건반 사이는 온 걸음일까요, 반 걸음일까요?'))}
    {paper(<SscKeys start={q.start} o={{ lit: [q.d, q.d + 1], nums: isDone }}/>)}{grid(2, c => word(SSC_SW[c]()))}</>;
  else if (q.kind === 'half') body = <>{big(sscScaleName(q.start))}{prompt(t('Between which degrees is a half step?', '어느 두 번호 사이가 반 걸음일까요?'))}
    {paper(<SscKeys start={q.start} o={{ nums: true, steps: isDone }}/>)}{grid(4, c => word(sscPair(c), 15))}</>;
  else if (q.kind === 'build') {
    const sc = sscScale(q.start);
    const tap = (k) => { if (locked || isDone) return; const d = sc.findIndex(s => s.id === k.id), next = done.length; sscPlay(q.start, k.semi, 0.4);
      if (d === next) { const nd = [...done, d]; setBs({ uid: q.uid, done: nd, miss: null }); if (nd.length === 8) onAnswer({ ok: true }); }
      else if (!done.includes(d)) { setBs({ uid: q.uid, done, miss: k.id }); onAnswer({ ok: false, miss: k.id }); } };   // a key already played is only heard
    body = <>{big(sscScaleName(q.start))}{prompt(t('Play the scale up: tap each key from the coral one, step by step.', '음계를 올라가요: 산호색 건반부터 한 걸음씩 눌러요.'))}
      {paper(<SscKeys start={q.start} o={{ lit: done.length === 1 ? 0 : null, done: done, miss, nums: isDone, hideNames: !isDone }} onTap={tap}/>)}
      <div style={{display:'flex',flexWrap:'wrap',justifyContent:'center',fontSize:pixel ? 9 : 13,fontWeight:800,color:pixel ? '#faf6ec' : BK.muted}}>{SSC_STEPS.map((s, i) => <span key={i} style={{color:i < done.length - 1 ? (s === 'half' ? BK.coral : BK.ink) : 'rgba(38,41,107,0.35)',margin:'0 3px'}}>{s === 'half' ? t('half', '반') : t('whole', '온')}</span>)}</div></>;
  }
  else if (q.kind === 'finger') { const F = SCALES[q.start].octaves[1][q.hand];
    body = <>{big(sscScaleName(q.start) + ' · ' + (q.hand === 'RH' ? t('right hand', '오른손') : t('left hand', '왼손')))}{prompt(t('Going up, which finger plays the coral key?', '올라갈 때 산호색 건반은 몇 번 손가락으로 칠까요?'))}
      {paper(<SscKeys start={q.start} o={{ lit: q.d, fingers: isDone ? F : null }}/>)}{grid(5, c => word(c, 19), '12px 0')}</>; }
  else if (q.kind === 'degree') body = <>{big(sscScaleName(q.start))}{prompt(t('Which degree is the coral note?', '산호색 음은 몇 번 음일까요?'))}
    {paper(<SscStaff start={q.start} o={{ lit: q.d, under: isDone ? 'nums' : null, gap: 34, accInk: PEN_N }}/>)}{grid(4, c => word(c, 19))}</>;
  else if (q.kind === 'name') body = q.sub === 'acc'
    ? <>{big(sscScaleName(q.start))}{prompt(q.start === 'G' ? t('Which is G major’s sharp?', 'G장조 음계의 샤프는?') : t('Which is F major’s flat?', 'F장조 음계의 플랫은?'))}{grid(4, c => word(c, 19))}</>
    : <>{big(sscScaleName(q.start))}{prompt(t('Which note is degree ' + (q.d + 1) + '?', (q.d + 1) + '번 음은 무엇일까요?'))}{grid(4, c => word(c, 19))}</>;
  else if (q.kind === 'ear') body = <>{big(sscScaleName(q.start))}{prompt(t('Listen: a major scale, or a wrong note?', '들어 봐요: 장음계일까요, 틀린 음이 있을까요?'))}
    <div style={{textAlign:'center',margin:'0 0 12px'}}><button className={pixel ? 'pixel-btn' : 'ghost-btn'} onClick={() => sscPlayScale(q)} style={pixel ? {fontSize:9} : {fontSize:15,padding:'8px 16px',minHeight:44}}>{t('▶ Hear it again', '▶ 다시 듣기')}</button></div>
    {grid(2, c => word(SSC_RW[c](), 16))}</>;
  else if (q.kind === 'acc2' && q.rev) body = <>{big(sscAcc2Txt(SSC_ACC2[q.start][0]))}{prompt(q.start === 'D' ? t('Which major scale has these two sharps?', '이 두 샤프가 있는 장음계는?') : t('Which major scale has these two flats?', '이 두 플랫이 있는 장음계는?'))}{grid(2, c => word(sscScaleName(c), 16))}</>;
  else if (q.kind === 'acc2') body = <>{big(sscScaleName(q.start))}{prompt(q.start === 'D' ? t('D major has two sharps. Which two notes?', 'D장조 음계에는 샤프가 두 개 있어요. 어느 두 음일까요?') : t('B♭ major has two flats. Which two notes?', 'B♭장조 음계에는 플랫이 두 개 있어요. 어느 두 음일까요?'))}{grid(2, c => word(sscAcc2Txt(c), 17))}</>;
  else body = <>{big(t(q.start + ' harmonic minor', q.start + '단조 화성단음계'))}{prompt(t('Every harmonic minor raises its 7th a half step. What is ' + q.start + ' harmonic minor’s raised 7th?', '화성단음계는 7번 음을 반 걸음 올려요. 올린 7번 음은 어느 음일까요?'))}{grid(4, c => word(c, 19))}</>;
  return <div><BoardTrack b={board} pixel={pixel}/>{body}</div>;
}
function sscCheck(q, ans) {
  if (ans === null || ans === undefined) return false;
  if (q.kind === 'build') return !!(ans && ans.ok);
  return String(ans) === String(q.answer);
}
function sscAnswerLabel(q) {
  const sc = SSC_KEYS3.includes(q.start) ? sscScale(q.start) : null;   // C, G and F only (levels 1 to 7)
  if (q.kind === 'step') return t('a ' + q.answer + ' step', SSC_SW[q.answer]()) + ' (' + sscNameTxt(sc[q.d].name) + ' → ' + sscNameTxt(sc[q.d + 1].name) + ')';
  if (q.kind === 'half') { const other = q.answer === '3–4' ? '7–8' : '3–4'; return sscPair(q.answer) + t(' (the other is ' + sscPair(other) + ')', ' (다른 하나는 ' + sscPair(other) + ')'); }
  if (q.kind === 'build') return sc.map(s => sscNameTxt(s.name)).join(' ');
  if (q.kind === 'finger') return t('finger ' + q.answer, q.answer + '번 손가락');
  if (q.kind === 'degree') return t('degree ' + q.answer, q.answer + '번 음') + ' (' + sscNameTxt(sc[q.d].name) + ')';
  if (q.kind === 'name') return q.answer;
  if (q.kind === 'ear') return q.answer === 'right' ? SSC_RW.right() : t('a wrong note: degree ' + (q.wrong[0] + 1), '틀린 음: ' + (q.wrong[0] + 1) + '번 음');
  if (q.kind === 'acc2') return q.rev ? sscScaleName(q.answer) : sscAcc2Txt(q.answer);
  return q.answer;
}
Object.assign(SCALES_DRILL, { levels: SSC_LEVELS, generate: genSscQuestion, check: sscCheck, answerLabel: sscAnswerLabel, Question: SscQuestion, Learn: SscLearn });
