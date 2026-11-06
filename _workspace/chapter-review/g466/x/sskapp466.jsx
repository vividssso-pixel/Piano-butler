// ─── Phase 466: chapter 9 on screen (what moves on each page), the book as the online lesson, and the drill ───
// Tunes sound on the audio clock like chapters 3, 5 and 8 (plRun, usePlTimers): a bar of clicks to count in, then the
// notes, each lit as it sounds. Keys sound when tapped (playKey).
const SSK_BPM = 84;
const sskHz = (d) => 440 * Math.pow(2, (ivMidi({ d, acc: 0 }) - 69) / 12);
// the sounds of a tune: { b (beat), d (beats long), pitch, j (note index) }
function sskSeq(items) {
  let b = 0, top = 4; const snd = [];
  items.forEach(it => {
    const k = it[0];
    if (k === 'ts') { top = it[1]; return; }
    if (k === '|' || k === '||' || k === 'sp') return;
    const n = it[1];
    if (k === 'p') { snd.push({ b, d: 0.5, pitch: it[2][0], j: snd.length }, { b: b + 0.5, d: 0.5, pitch: it[2][1], j: snd.length + 1 }); }
    else if (!sskIsRest(k)) snd.push({ b, d: n, pitch: it[2], j: snd.length });
    b += n;
  });
  return { n: b, snd, top };
}
// a bar to count in (clicks, or the spoken count when the sound settings ask for a voice), then the tune
function sskPlay(seq, o = {}) {
  const ci = o.countIn === false ? 0 : seq.top;
  return plRun(ci + Math.ceil(seq.n), { bpm: o.bpm || SSK_BPM, silentFrom: 0, noVoice: true, extra: (ctx, tm, i, spb) => {
    if (i < ci) { const said = SOUND.count === 'voice' && sayCount(ctx, tm, String(i + 1), 1); if (!said) metroClick(ctx, tm, i === 0, 0.27); return; }
    const b = i - ci;
    seq.snd.filter(s => Math.floor(s.b + 1e-9) === b).forEach(s => blip(ctx, tm + (s.b - b) * spb, sskHz(s.pitch), Math.max(0.1, s.d * spb * 0.92), 0.2, 'triangle'));
  } });
}
// light each note as it sounds; done() after the last
function sskLight(T, r, seq, ci, setLit, done) {
  seq.snd.forEach(s => T.at(r, r.at[ci] + s.b * r.spb, () => setLit(s.j)));
  T.at(r, r.at[ci] + seq.n * r.spb + 0.05, () => { setLit(-1); if (done) done(); });
}
const sskTwo = (a, b) => playMelody([{ d: a, dur: 1 }, { d: b, dur: 1.5 }], 100);
// the keyboard under a hand's notes: its first C (midi) and how many octaves
const sskKb = (clef, lo, hi) => clef === 'bass' ? (lo >= 21 && hi <= 27 ? { base: 48, oct: 1 } : { base: 36, oct: 2 }) : (hi > 34 ? { base: 60, oct: 2 } : { base: 60, oct: 1 });
const sskKey = (kb, d) => ivMidi({ d, acc: 0 }) - kb.base;

// ── page 2: listen to a tune, then say how each note moves: up, down or the same ──
const SSK_SHAPES = [
  { name: () => t('Tune 1', '선율 1'), clef: 'treble', items: [['ts', 4], ['q', 1, 28], ['q', 1, 30], ['q', 1, 30], ['q', 1, 29], ['|'], ['q', 1, 31], ['q', 1, 30], ['h', 2, 28], ['||']] },
  { name: () => t('Tune 2', '선율 2'), clef: 'bass', items: SSK_TUNES[1].items },
  { name: () => t('Tune 3', '선율 3'), clef: 'treble', items: SSK_ROWS.read },
];
function SskShapePad() {
  const T = usePlTimers();
  const [ti, setTi] = useState(0), [lit, setLit] = useState(-1), [turn, setTurn] = useState(false), [ans, setAns] = useState([]);
  const S = SSK_SHAPES[ti], seq = sskSeq(S.items), ns = seq.snd.map(s => s.pitch), nMoves = ns.length - 1;
  const cur = turn && ans.length < nMoves ? ans.length : -1;
  const right = ans.filter((a, j) => a === Math.sign(ns[j + 1] - ns[j])).length;
  function pickTune(i) { T.clear(); stopClicks(); setTi(i); setLit(-1); setTurn(false); setAns([]); }
  function listen() { T.clear(); setLit(-1); const r = sskPlay(seq); if (r) sskLight(T, r, seq, seq.top, setLit); }
  function say(dir) { if (cur < 0) return; sskTwo(ns[cur], ns[cur + 1]); setAns(a => [...a, dir]); }
  const moveCol = ans.map((a, j) => a === Math.sign(ns[j + 1] - ns[j]) ? PEN_G : PEN_C);
  const btn = (dir, label) => <button className="choice-btn" disabled={cur < 0} onClick={() => say(dir)} style={{padding:'10px 4px',display:'flex',flexDirection:'column',alignItems:'center',gap:2}}>
    <svg viewBox="0 0 24 24" width="28" height="28" aria-hidden="true" dangerouslySetInnerHTML={{ __html: sskArrow(12, 12, dir, BK.coral, 1) }}/><span style={{fontSize:13,fontWeight:900}}>{label}</span></button>;
  return (
    <div className="try-box" style={actBox} data-ssk="shape">
      <div style={actTitle}>{t('Which way does it go?', '어디로 갈까요?')}</div>
      <div style={actNote}>{t('Listen first: each note lights up as it sounds. Then press Your turn and tap up, the same or down for each note.', '먼저 들어 봐요: 음마다 소리 날 때 불이 켜져요. 그다음 ‘내\u00a0차례’를 누르고, 음마다 위로, 같은 음, 아래로 중에서 골라요.')}</div>
      <div style={{display:'flex',gap:5,justifyContent:'center',flexWrap:'wrap',marginBottom:8}}>{SSK_SHAPES.map((x, i) => <button key={i} className={'chip' + (i === ti ? ' active' : '')} onClick={() => pickTune(i)}>{x.name()}</button>)}</div>
      <div style={{maxWidth:480,margin:'0 auto'}}><SskStaff full clef={S.clef} items={S.items} o={{ D: 24, lit, moves: turn ? 'box' : undefined, moveAns: ans.map(() => true), moveCol, moveCur: cur }}/></div>
      <div style={{display:'flex',gap:6,justifyContent:'center',margin:'6px 0 8px'}}>
        <button className="ghost-btn" onClick={listen}>{t('▶ Listen', '▶ 듣기')}</button>
        <button className="ghost-btn" onClick={() => { T.clear(); setLit(-1); setTurn(true); setAns([]); }}>{t('Your turn', '내\u00a0차례')}</button>
      </div>
      {turn && <div style={{display:'grid',gridTemplateColumns:'repeat(3,minmax(0,1fr))',gap:6,maxWidth:360,margin:'0 auto'}}>{btn(1, t('up', '위로'))}{btn(0, t('the same', '같은 음'))}{btn(-1, t('down', '아래로'))}</div>}
      {turn && ans.length === nMoves && <div style={{textAlign:'center',fontSize:14.5,fontWeight:900,marginTop:8,color:right === nMoves ? BK.green : BK.coral}}>{t('Correct: ' + right + ' of ' + nMoves, '맞혔어요: ' + nMoves + '개 중 ' + right + '개')}{right === nMoves ? '  ✓' : ''}</div>}
    </div>
  );
}

// ── page 3: pick a move; see it on the staff and on the keys, and hear it ──
const SSK_MOVES = [['step', 1], ['step', -1], ['skip', 2], ['skip', -2], ['same', 0]];
function SskStepPad() {
  const [clef, setClef] = useState('treble'), [mv, setMv] = useState(1), [a, setA] = useState(30), [nonce, setNonce] = useState(0);
  const b = a + mv, kb = sskKb(clef, clef === 'treble' ? 28 : 18, clef === 'treble' ? 36 : 26), word = sskMove(a, b);
  function go(m, c = clef) {
    const l = c === 'treble' ? 28 : 18, h = c === 'treble' ? 34 : 24;
    let na = l + Math.floor(Math.random() * (h - l + 1)), g = 0;
    while ((na + m < l || na + m > h + 2 || (na === a && m === mv)) && g++ < 20) na = l + Math.floor(Math.random() * (h - l + 1));
    setA(na); setMv(m); setNonce(x => x + 1); sskTwo(na, na + m);
  }
  const lineA = (a - CLEFS[clef].low) % 2 === 0;
  const detail = word === 'same' ? t('the same line or space, the same key.', '같은 줄이나 칸, 같은 건반.')
    : word === 'step' ? (lineA ? t('line to space, the next white key.', '줄에서 칸으로, 바로 옆 흰 건반.') : t('space to line, the next white key.', '칸에서 줄로, 바로 옆 흰 건반.'))
    : (lineA ? t('line to line, jump over one white key.', '줄에서 줄로, 흰 건반 하나 건너.') : t('space to space, jump over one white key.', '칸에서 칸으로, 흰 건반 하나 건너.'));
  const marks = { [sskKey(kb, a)]: 'mate', [sskKey(kb, b)]: 'pick' };
  const name = (w, m) => w === 'same' ? t('the same', '같은 음') : LANG === 'ko' ? (m > 0 ? '위로 ' : '아래로 ') + (w === 'step' ? '한 걸음' : '건너뛰기') : (w === 'step' ? 'step ' : 'skip ') + (m > 0 ? 'up' : 'down');
  return (
    <div className="try-box" style={actBox} data-ssk="step">
      <div style={actTitle}>{t('Step, skip or the same', '한 걸음, 건너뛰기, 같은 음')}</div>
      <div style={actNote}>{t('Pick a move. See it on the staff and on the keys, and hear it.', '움직임을 골라요. 오선과 건반에서 보고, 들어 봐요.')}</div>
      <div style={{display:'flex',gap:5,justifyContent:'center',marginBottom:6}}>{[['treble', t('Treble clef', '높은음자리표')], ['bass', t('Bass clef', '낮은음자리표')]].map(([c, l]) => <button key={c} className={'chip' + (c === clef ? ' active' : '')} onClick={() => { setClef(c); go(mv, c); }}>{l}</button>)}</div>
      <div style={{display:'flex',gap:5,justifyContent:'center',flexWrap:'wrap',marginBottom:8}}>{SSK_MOVES.map(([w, m]) => <button key={w + m} className={'chip' + (m === mv ? ' active' : '')} onClick={() => go(m)}>{name(w, m)}</button>)}</div>
      <div key={nonce} style={{maxWidth:260,margin:'0 auto'}}><SskStaff full clef={clef} items={[['w', 4, a], ['w', 4, b]]} o={{ D: 18, x0: 52, hl: [1], moves: 'bracket' }}/></div>
      <div style={{maxWidth:420,margin:'4px auto 0'}}><TapKeyboard octaves={kb.oct} labels="white" marks={marks} onTap={(k) => playKey(k + kb.base - 60)}/></div>
      <div style={{textAlign:'center',fontSize:13.5,color:BK.ink,fontWeight:700,marginTop:6}}>{dName(a)} → {dName(b)}: {detail}</div>
      <div style={{textAlign:'center',marginTop:6}}><button className="ghost-btn" onClick={() => sskTwo(a, b)}>{t('▶ Hear it', '▶ 듣기')}</button></div>
    </div>
  );
}

// ── pages 4 and 5: a position under each hand; tap the keys, or say which finger plays a note ──
function SskPosPad({ pos }) {
  const T = usePlTimers();
  const [hand, setHand] = useState('rh'), [lit, setLit] = useState(-1), [quiz, setQuiz] = useState(null), [score, setScore] = useState({ right: 0, tries: 0 });
  const ds = SSK_POS[pos][hand], clef = hand === 'rh' ? 'treble' : 'bass', kb = sskKb(clef, ds[0], ds[4]);
  const fingers = ds.map(d => sskFingerOf(pos, hand, d));
  const items = ds.map(d => ['w', 4, d]);
  const names = {}, marks = {};
  ds.forEach((d, i) => { const k = sskKey(kb, d); marks[k] = lit === i ? 'pick' : 'mate'; if (!quiz) names[k] = String(fingers[i]); });
  function pickHand(h) { T.clear(); setHand(h); setLit(-1); setQuiz(null); }
  function tapKey(k) { playKey(k + kb.base - 60); const i = ds.findIndex(d => sskKey(kb, d) === k); setLit(i); }
  function upDown() { T.clear(); setQuiz(null); const run = [...ds, ...ds.slice(0, 4).reverse()]; const it = [['ts', 4], ...run.map(d => ['q', 1, d])]; const seq = sskSeq(it); const r = sskPlay(seq, { countIn: false, bpm: 110 }); if (r) sskLight(T, r, seq, 0, (j) => setLit(j < 0 ? -1 : j < 5 ? j : 8 - j)); }
  function ask() { T.clear(); let i, g = 0; do { i = Math.floor(Math.random() * 5); } while (quiz && quiz.i === i && g++ < 10); setLit(-1); setQuiz({ i, ans: null }); }
  function answer(f) { if (!quiz || quiz.ans != null) return; const ok = f === fingers[quiz.i]; setQuiz({ ...quiz, ans: f }); setScore(s => ({ right: s.right + (ok ? 1 : 0), tries: s.tries + 1 })); playKey(sskKey(kb, ds[quiz.i]) + kb.base - 60); }
  const qOk = quiz && quiz.ans != null && quiz.ans === fingers[quiz.i];
  return (
    <div className="try-box" style={actBox} data-ssk={'pos' + pos}>
      <div style={actTitle}>{pos === 'C' ? t('C position', 'C 자리') : t('G position', 'G 자리')}</div>
      <div style={actNote}>{t('Tap the keys: each note lights up on the staff. Then press Which finger? and pick the finger for the orange note.', '건반을 눌러 봐요: 오선에서 그 음에 불이 켜져요. 그다음 ‘어떤 손가락?’을 누르고, 주황색 음을 칠 손가락을 골라요.')}</div>
      <div style={{display:'flex',gap:5,justifyContent:'center',marginBottom:8}}>{[['rh', t('Right hand', '오른손')], ['lh', t('Left hand', '왼손')]].map(([h, l]) => <button key={h} className={'chip' + (h === hand ? ' active' : '')} onClick={() => pickHand(h)}>{l}</button>)}</div>
      <div style={{maxWidth:330,margin:'0 auto'}}><SskStaff full clef={clef} items={items} o={{ D: 11.5, x0: 50, lit: quiz ? quiz.i : lit, fingers: quiz ? fingers.map((f, j) => j === quiz.i ? (quiz.ans != null ? f : '') : undefined) : fingers, fingerAt: hand === 'rh' ? 'above' : 'below' }}/></div>
      <div style={{maxWidth:kb.oct === 1 ? 300 : 420,margin:'4px auto 0'}}><TapKeyboard octaves={kb.oct} labels="white" marks={marks} names={names} outline={[sskKey(kb, ds[0]), sskKey(kb, ds[4])]} onTap={quiz ? null : tapKey}/></div>
      {quiz && <div style={{display:'grid',gridTemplateColumns:'repeat(5,minmax(0,1fr))',gap:6,maxWidth:340,margin:'8px auto 0'}}>{[1, 2, 3, 4, 5].map(f => <button key={f} className={'choice-btn' + (quiz.ans == null ? '' : f === fingers[quiz.i] ? ' good' : f === quiz.ans ? ' bad' : '')} onClick={() => answer(f)} style={{padding:'12px 0',fontSize:18,fontWeight:900}}>{f}</button>)}</div>}
      {quiz && quiz.ans != null && <div style={{textAlign:'center',fontSize:14,fontWeight:900,marginTop:6,color:qOk ? BK.green : BK.coral}}>{qOk ? t('Yes: ', '맞아요: ') : t('Not quite: ', '아쉬워요: ')}{t(dName(ds[quiz.i]) + ' is finger ' + fingers[quiz.i], dName(ds[quiz.i]) + '는 ' + fingers[quiz.i] + '번 손가락')}<span style={{color:BK.muted,fontWeight:800}}>{'  ·  ' + t(score.right + ' of ' + score.tries, score.tries + '개 중 ' + score.right + '개')}</span></div>}
      <div style={{display:'flex',gap:6,justifyContent:'center',marginTop:8,flexWrap:'wrap'}}>
        <button className="ghost-btn" onClick={upDown}>{t('▶ Up and down', '▶ 올라갔다 내려오기')}</button>
        <button className="ghost-btn" onClick={ask}>{quiz ? t('Next note →', '다음 음 →') : t('Which finger?', '어떤 손가락?')}</button>
        {quiz && <button className="ghost-btn" onClick={() => { setQuiz(null); setLit(-1); }}>{t('Back to the keys', '건반으로')}</button>}
      </div>
    </div>
  );
}

// ── page 6: read a tune: listen, then play it on the keys, one note after another ──
function SskReadPad() {
  const T = usePlTimers();
  const [ti, setTi] = useState(2), [lit, setLit] = useState(-1), [turn, setTurn] = useState(false), [at, setAt] = useState(0), [bad, setBad] = useState(null), [miss, setMiss] = useState(0);
  const tune = SSK_TUNES[ti], seq = sskSeq(tune.items), ns = seq.snd.map(s => s.pitch);
  const kb = sskKb(tune.clef, Math.min(...ns), Math.max(...ns)), first = ns[0];
  function pickTune(i) { T.clear(); stopClicks(); setTi(i); setLit(-1); setTurn(false); setAt(0); setBad(null); setMiss(0); }
  function listen() { T.clear(); setTurn(false); setLit(-1); const r = sskPlay(seq); if (r) sskLight(T, r, seq, seq.top, setLit); }
  function tap(k) {
    playKey(k + kb.base - 60);
    if (!turn || at >= ns.length) return;
    if (k === sskKey(kb, ns[at])) { setLit(at); setAt(at + 1); setBad(null); setMiss(0); } else { setBad(k); setMiss(m => m + 1); setTimeout(() => setBad(b => (b === k ? null : b)), 500); }
  }
  const marks = {};
  if (turn && at < ns.length && miss >= 2) marks[sskKey(kb, ns[at])] = 'mate';   // the right key only after two wrong taps
  if (lit >= 0) marks[sskKey(kb, ns[lit])] = 'pick';
  if (bad !== null) marks[bad] = 'miss';
  const done = turn && at >= ns.length;
  return (
    <div className="try-box" style={actBox} data-ssk="read">
      <div style={actTitle}>{t('Read a tune', '선율 읽기')}</div>
      <div style={actNote}>{t('Find the first note, clap and count the rhythm, say the moves. Listen to check. Then press Your turn and play it on the keys, note by note.', '첫 음을 찾고, 세면서 리듬에 맞춰 손뼉을 치고, 움직임을 말해요. 들어 보며 확인해요. 그다음 ‘내\u00a0차례’를 누르고 건반에서 한 음씩 쳐요.')}</div>
      <div style={{display:'flex',gap:5,justifyContent:'center',flexWrap:'wrap',marginBottom:8}}>{SSK_TUNES.map((x, i) => <button key={x.id} className={'chip' + (i === ti ? ' active' : '')} onClick={() => pickTune(i)}>{x.name()}</button>)}</div>
      <div style={{maxWidth:480,margin:'0 auto'}}><SskStaff full clef={tune.clef} items={tune.items} o={{ D: 24, lit, fingers: [sskFingerOf(tune.pos, tune.hand, first)], fingerAt: tune.hand === 'rh' ? 'above' : 'below' }}/></div>
      <div style={{maxWidth:kb.oct === 1 ? 300 : 420,margin:'4px auto 0'}}><TapKeyboard octaves={kb.oct} labels="white" marks={marks} onTap={tap}/></div>
      {done && <div style={{textAlign:'center',fontSize:15,fontWeight:900,color:BK.green,margin:'6px 0'}}>{t('You read it! ✓', '다 읽었어요! ✓')}</div>}
      <div style={{display:'flex',gap:6,justifyContent:'center',marginTop:8}}>
        <button className="ghost-btn" onClick={listen}>{t('▶ Listen', '▶ 듣기')}</button>
        <button className="ghost-btn" onClick={() => { T.clear(); stopClicks(); setLit(-1); setTurn(true); setAt(0); setBad(null); setMiss(0); }}>{t('Your turn', '내\u00a0차례')}</button>
      </div>
    </div>
  );
}

// ── the book on screen: the opener is the lesson's head, every other page a step. Old ticks kept where the idea is
// the same: 'Where does it go?' (0), 'Five-finger positions' (5), 'Read a tiny tune' (1); steps and skips, G position
// and the checks are new (6, 7, 8) ──
const SSK_STORE = [0, 6, 5, 7, 1, 8];
function SskLearn({ onStart }) {
  const pages = sskLbPages(true);
  const opener = pages[0];
  return (
    <Lesson id="reading-steps" title={t('Steps & Skips', '차례가기와 건너뛰기')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="reading-steps"><div className="lb-screen lb-open" style={{display:'flex',flexDirection:'column',gap:12,margin:'0 0 8px'}}>{lbWordsFirst(opener.props.children)}</div></BkChapterCtx.Provider></LbScreenCtx.Provider>}>
      {pages.slice(1).map((pg, i) => (
        <Step key={i} storeAs={SSK_STORE[i]} title={pg.props.title}>
          <LbScreenPage page={pg}/>
        </Step>
      ))}
    </Lesson>
  );
}

// ── the drill: six levels for this room, two by ear, then all twelve positions ──
const SSK_LEVELS = [
  { n: 1, label: 'Up, down or the same?', kind: 'dir', time: 6 },
  { n: 2, label: 'Step, skip or the same?', kind: 'move', time: 7 },
  { n: 3, label: 'Name the next note', kind: 'next', time: 8 },
  { n: 4, label: 'C position: which finger? (right hand)', kind: 'ff', pos: 'C', hand: 'rh', time: 7 },
  { n: 5, label: 'C position: which finger? (left hand)', kind: 'ff', pos: 'C', hand: 'lh', time: 7 },
  { n: 6, label: 'G position: which finger?', kind: 'ff', pos: 'G', hand: null, time: 7 },
  { n: 7, label: 'Which tune did you hear?', kind: 'which', time: 16, noPrint: true },
  { n: 8, label: 'Spot the change', kind: 'change', time: 18, noPrint: true },
  { n: 9, label: 'Extra: all 12 five-finger positions', kind: 'ff12', time: 8 },
];
Object.assign(LEVEL_KO, {
  'Up, down or the same?': '위로, 아래로, 같은 음?', 'Step, skip or the same?': '한 걸음, 건너뛰기, 같은 음?', 'Name the next note': '다음 음의 이름',
  'C position: which finger? (right hand)': 'C 자리: 어떤 손가락? (오른손)', 'C position: which finger? (left hand)': 'C 자리: 어떤 손가락? (왼손)',
  'G position: which finger?': 'G 자리: 어떤 손가락?', 'Which tune did you hear?': '어떤 선율을 들었을까요?', 'Spot the change': '바뀐 음 찾기',
  'Extra: all 12 five-finger positions': '더 해 보기: 다섯 손가락 자리 12개 모두',
});
// a little walk inside C position, right hand (d 28 to 32): steps, skips and repeated notes
function sskWalk(len) { const out = [28 + Math.floor(Math.random() * 3)]; while (out.length < len) { const nx = out[out.length - 1] + pick([-2, -1, -1, 0, 1, 1, 2]); if (nx >= 28 && nx <= 32) out.push(nx); } return out; }
function genSskQuestion(lv, prev) {
  const uid = Math.random();
  if (lv.kind === 'ff12') return { ...genFfQuestion({ pos: null, hand: null }, prev), kind: 'ff12' };
  if (lv.kind === 'ff') {
    for (let g = 0; g < 30; g++) {
      const hand = lv.hand || pick(['rh', 'lh']), i = Math.floor(Math.random() * 5), d = SSK_POS[lv.pos][hand][i], key = lv.pos + hand + d;
      if (prev && prev.key === key) continue;
      return { kind: 'ff', pos: lv.pos, hand, d, key, answer: String(sskFingerOf(lv.pos, hand, d)), choices: ['1', '2', '3', '4', '5'], uid };
    }
  }
  if (lv.kind === 'which') {
    const a = sskWalk(4), opts = [a], key = (x) => x.join('');
    let g = 0;
    const near = (b, i) => (i === 0 || Math.abs(b[i] - b[i - 1]) <= 2) && (i === b.length - 1 || Math.abs(b[i + 1] - b[i]) <= 2);
    while (opts.length < 3 && g++ < 300) { const b = [...a], i = Math.floor(Math.random() * 4), nv = b[i] + pick([-2, -1, 1, 2]); if (nv < 28 || nv > 32) continue; b[i] = nv; if (!near(b, i)) continue; if (!opts.some(o => key(o) === key(b))) opts.push(b); }
    while (opts.length < 3) { const r = sskWalk(4); if (!opts.some(o => key(o) === key(r))) opts.push(r); }
    const sh = shuffle(opts);
    return { kind: 'which', tune: a, opts: sh, key: 'w' + key(a), answer: String(1 + sh.findIndex(o => key(o) === key(a))), choices: ['1', '2', '3'], uid };
  }
  if (lv.kind === 'change') {
    for (;;) {
      const w = sskWalk(6), i = Math.floor(Math.random() * 6), mv = pick([-2, -1, 1, 2]), nv = w[i] + mv;
      if (nv < 28 || nv > 32) continue;
      const heard = [...w]; heard[i] = nv;
      if ((i > 0 && Math.abs(heard[i] - heard[i - 1]) > 2) || (i < 5 && Math.abs(heard[i + 1] - heard[i]) > 2)) continue;
      return { kind: 'change', written: w, heard, at: i, mv, key: 'c' + w.join('') + i, answer: String(i + 1), choices: ['1', '2', '3', '4', '5', '6'], uid };
    }
  }
  for (let g = 0; g < 40; g++) {
    const clef = Math.random() < 0.6 ? 'treble' : 'bass', lo = clef === 'treble' ? 28 : 18, hi = clef === 'treble' ? 36 : 26;
    const a = lo + Math.floor(Math.random() * (hi - lo + 1)), k = pick([0, 1, -1, 2, -2]), b = a + k;
    if (b < lo || b > hi) continue;
    const key = clef + a + ':' + b; if (prev && prev.key === key) continue;
    if (lv.kind === 'dir') return { kind: 'dir', clef, a, b, key, answer: k === 0 ? 'same' : k > 0 ? 'up' : 'down', choices: ['up', 'same', 'down'], uid };
    if (lv.kind === 'move') return { kind: 'move', clef, a, b, key, answer: sskMove(a, b), choices: ['step', 'skip', 'same'], uid };
    return { kind: 'next', clef, a, b, key, answer: dName(b), choices: STAFF_LETTERS.slice(), uid };
  }
}
const SSK_DIR = { up: () => t('up', '위로'), down: () => t('down', '아래로'), same: () => t('the same', '같은 음') };
function SskQuestion(props) {
  const { q, given, locked, onAnswer, pixel } = props;
  const board = useBoard(q, given);
  const T = usePlTimers();
  const [lit, setLit] = useState({ who: null, j: -1 });
  useEffect(() => { T.clear(); setLit({ who: null, j: -1 }); if (q.kind === 'which') setTimeout(() => play(q.tune, 'tune'), 250); if (q.kind === 'change') setTimeout(() => play(q.heard, 'written', true), 250); }, [q.uid]);
  if (q.kind === 'ff12') return <FfQuestion {...props}/>;
  const done = !!given;
  const ink = pixel ? '#faf6ec' : '#26296b';
  const btnCls = pixel ? 'pixel-choice' : 'choice-btn';
  const st = (c) => !done ? '' : c === q.answer ? ' good' : (given.ans === c ? ' bad' : '');
  const prompt = (txt) => <p style={pixel ? {fontSize:11.5,textAlign:'center',margin:'0 0 10px',lineHeight:1.7} : {fontSize:15,fontWeight:700,textAlign:'center',margin:'0 0 10px',color:'var(--muted)'}}>{txt}</p>;
  const box = (kids) => <div style={{background:pixel ? '#faf6ec' : 'transparent',borderRadius:8,padding:pixel ? 6 : 0,margin:'0 auto 10px'}}>{kids}</div>;
  const grid = (cols, render, pad = '14px 4px') => <div style={{display:'grid',gridTemplateColumns:'repeat(' + cols + ',minmax(0,1fr))',gap:8}}>{q.choices.map(c => <button key={c} disabled={locked} onClick={() => { T.clear(); setLit({ who: null, j: -1 }); onAnswer(c); if (q.a != null && q.b != null) sskTwo(q.a, q.b); }} className={btnCls + st(c)} style={{padding:pad}}>{render(c)}</button>)}</div>;
  function play(ds, who, heard) { T.clear(); const it = [['ts', 4], ...ds.map((d, j) => ['q', heard && j >= 4 ? 2 : 1, d])]; const seq = sskSeq(it); const r = sskPlay(seq, { countIn: false, bpm: 92 }); if (r) { seq.snd.forEach(s => T.at(r, r.at[0] + s.b * r.spb, () => setLit({ who, j: s.j }))); T.at(r, r.at[0] + seq.n * r.spb + 0.1, () => setLit({ who: null, j: -1 })); } }
  const two = (o = {}) => box(<div style={{maxWidth:240,margin:'0 auto'}}><SskStaff full clef={q.clef} items={[['w', 4, q.a], ['w', 4, q.b]]} o={{ D: 18, x0: 52, ...o }}/></div>);
  let body;
  if (q.kind === 'dir') body = <>{prompt(t('Does the second note go up, down or stay the same?', '두 번째 음은 위로 갈까요, 아래로 갈까요, 같은 음일까요?'))}{two({ hl: done ? [1] : [], moves: done ? 'arrow' : undefined })}{grid(3, c => <span style={{display:'flex',flexDirection:'column',alignItems:'center',gap:2}}><svg viewBox="0 0 24 24" width="26" height="26" aria-hidden="true" dangerouslySetInnerHTML={{ __html: sskArrow(12, 12, c === 'up' ? 1 : c === 'down' ? -1 : 0, pixel ? '#faf6ec' : BK.coral, 1) }}/><span style={{fontSize:pixel ? 10 : 14,fontWeight:900}}>{SSK_DIR[c]()}</span></span>, '8px 4px')}</>;
  else if (q.kind === 'move') body = <>{prompt(t('A step, a skip or the same note?', '한 걸음, 건너뛰기, 같은 음 중 어느 것일까요?'))}{two({ hl: done ? [1] : [], moves: done ? 'bracket' : undefined })}{grid(3, c => <span style={{fontSize:pixel ? 10 : 16,fontWeight:900}}>{c === 'same' ? t('the same', '같은 음') : SSK_WORD[c]()}</span>)}</>;
  else if (q.kind === 'next') body = <>{prompt(t('The first note is ' + dName(q.a) + '. What is the second?', '첫 음은 ' + dName(q.a) + '예요. 두 번째 음은?'))}{two({ hl: done ? [1] : [], under: [dName(q.a), done ? dName(q.b) : null] })}{grid(7, c => <span style={{fontSize:pixel ? 11 : 17,fontWeight:900}}><NoteName n={c}/></span>, '12px 0')}</>;
  else if (q.kind === 'ff') {
    const clef = q.hand === 'rh' ? 'treble' : 'bass', name = q.pos === 'C' ? t('C position', 'C 자리') : t('G position', 'G 자리');
    body = <>{prompt(name + ', ' + (q.hand === 'rh' ? t('right hand', '오른손') : t('left hand', '왼손')) + ': ' + t('which finger plays this note?', '어떤 손가락으로 이 음을 칠까요?'))}
      {box(<div style={{maxWidth:200,margin:'0 auto'}}><SskStaff full clef={clef} items={[['w', 4, q.d]]} o={{ D: 18, x0: 60, fingers: done ? [q.answer] : undefined, fingerAt: q.hand === 'rh' ? 'above' : 'below', under: done ? [dName(q.d)] : undefined }}/></div>)}
      {grid(5, c => <span style={{fontSize:pixel ? 11 : 18,fontWeight:900}}>{c}</span>, '14px 0')}</>;
  }
  else if (q.kind === 'which') body = <>{prompt(t('Listen, then read: which tune did you hear?', '듣고 나서 읽어요: 어떤 선율을 들었을까요?'))}
    <div style={{display:'grid',gap:8,marginBottom:10}}>{q.opts.map((o, k) => <div key={k} style={{display:'flex',alignItems:'center',gap:8,border:'2px solid ' + (done && String(k + 1) === q.answer ? BK.green : 'rgba(38,41,107,0.18)'),borderRadius:12,padding:'2px 8px',background:pixel ? '#faf6ec' : '#fff'}}>
      <b style={{fontSize:16,color:BK.ink,width:16}}>{k + 1}</b><div style={{flex:1,minWidth:0}}><SskStaff full items={o.map(d => ['w', 4, d])} o={{ D: 10, x0: 50, lit: lit.who === k ? lit.j : -1 }}/></div>
      {done && <button className="chip" onClick={() => play(o, k)} style={{padding:'3px 8px',fontSize:12}}>♪</button>}</div>)}</div>
    <div style={{textAlign:'center',marginBottom:8}}><button className={pixel ? 'pixel-btn' : 'ghost-btn'} onClick={() => play(q.tune, 'tune')}>{t('▶ Play the tune', '▶ 선율 듣기')}</button></div>
    {grid(3, c => <span style={{fontSize:pixel ? 12 : 18,fontWeight:900}}>{c}</span>)}</>;
  else body = <>{prompt(t('Read along while it plays. One note sounds different from what is written: which one?', '들으면서 악보를 따라 읽어요. 한 음이 악보와 다르게 소리 나요: 몇 번째일까요?'))}
    {box(<div style={{maxWidth:420,margin:'0 auto'}}><SskStaff full items={[['ts', 4], ...q.written.slice(0, 4).map(d => ['q', 1, d]), ['|'], ...q.written.slice(4).map(d => ['h', 2, d]), ['||']]} o={{ D: 34, lit: lit.who === 'written' ? lit.j : -1, hl: done ? [q.at] : [], under: q.written.map((_, j) => String(j + 1)), underCoral: done ? [q.at] : [] }}/></div>)}
    <div style={{textAlign:'center',marginBottom:8}}><button className={pixel ? 'pixel-btn' : 'ghost-btn'} onClick={() => play(q.heard, 'written', true)}>{t('▶ Play it', '▶ 듣기')}</button>{done && <button className={pixel ? 'pixel-btn' : 'ghost-btn'} style={{marginLeft:6}} onClick={() => play(q.written, 'written', true)}>{t('▶ As written', '▶ 악보대로')}</button>}</div>
    {grid(6, c => <span style={{fontSize:pixel ? 12 : 18,fontWeight:900}}>{c}</span>, '12px 0')}</>;
  return <div><BoardTrack b={board} pixel={pixel}/>{body}</div>;
}
function sskCheck(q, ans) {
  if (q.kind === 'ff12') return ans === q.answer;
  return ans !== null && ans !== undefined && ans === q.answer;
}
function sskAnswerLabel(q) {
  if (q.kind === 'ff12') return t('finger ' + q.answer, q.answer + '번 손가락') + ' (' + ffName(q.d, q.acc) + ')';
  if (q.kind === 'ff') return t('finger ' + q.answer, q.answer + '번 손가락') + ' (' + dName(q.d) + ')';
  if (q.kind === 'which') return t('tune ' + q.answer, q.answer + '번 선율');
  if (q.kind === 'change') return t('note ' + q.answer + ', played ' + (Math.abs(q.mv) === 1 ? 'a step' : 'a skip') + (q.mv > 0 ? ' higher' : ' lower'), q.answer + '번째 음, ' + (Math.abs(q.mv) === 1 ? '한 걸음 ' : '건너뛰어 ') + (q.mv > 0 ? '높게' : '낮게') + ' 쳤어요');
  const pair = ' (' + dName(q.a) + ' → ' + dName(q.b) + ')';
  if (q.kind === 'dir') return SSK_DIR[q.answer]() + pair;
  if (q.kind === 'move') return (q.answer === 'same' ? t('the same note', '같은 음') : LANG === 'ko' ? (q.b > q.a ? '위로 ' : '아래로 ') + SSK_WORD[q.answer]() : 'a ' + SSK_WORD[q.answer]() + (q.b > q.a ? ' up' : ' down')) + pair;
  return withSolfa(q.answer) + pair;
}
Object.assign(READING_STEPS_DRILL, { levels: SSK_LEVELS, generate: genSskQuestion, check: sskCheck, answerLabel: sskAnswerLabel, Question: SskQuestion, Learn: SskLearn });
