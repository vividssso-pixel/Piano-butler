// ─── Phase 467: chapter 10 on screen (what moves on pages 2 to 6), the book as the online lesson, and the drill ───
// Tunes sound on the audio clock (plRun, usePlTimers) with no count-in: each note at its loudness (the last sign before
// it; under a hairpin, an even step in loudness at every note towards the next sign) and its length (staccato short;
// unmarked and slurred notes joined, the last note of a slur lifted a little; a tie held for both notes). The loudness
// levels are the drill's old ones (DYNAMICS).
const SDY_BPM = 88;
const SDY_FOUR = ['pp', 'p', 'mf', 'f'];
const SDY_SIX = ['pp', 'p', 'mp', 'mf', 'f', 'ff'];
const SDY_IT = { pp: 'pianissimo', p: 'piano', mp: 'mezzo piano', mf: 'mezzo forte', f: 'forte', ff: 'fortissimo' };
const SDY_MEAN = { pp: () => t('very soft', '매우 여리게'), p: () => t('soft', '여리게'), mp: () => t('medium soft', '조금 여리게'), mf: () => t('medium loud', '조금 세게'), f: () => t('loud', '세게'), ff: () => t('very loud', '매우 세게') };
function sdyVols(items, k = {}) {
  const n = sskNotesOf(items).length, v = [], dyn = (k.dyn || []).slice().sort((a, b) => a[0] - b[0]);
  let cur = SDY_VOL.mf;
  for (let j = 0; j < n; j++) { const d = dyn.find(([i]) => i === j); if (d) cur = SDY_VOL[d[1]]; v.push(cur); }
  (k.hair || []).forEach(([a, b, dir]) => { const from = v[a], nx = dyn.find(([i]) => i > b), to = nx ? SDY_VOL[nx[1]] : dir === 'cresc' ? from * 3 : from / 3;
    for (let j = a; j <= b; j++) v[j] = from * Math.pow(to / from, (j - a) / (b - a + 1)); });
  return v;
}
function sdyPlay(items, k = {}, o = {}) {
  const seq = sskSeq(items), vols = o.vols || sdyVols(items, k), st = new Set(k.stacc || []), ties = k.ties || [], slurs = k.slurs || [];
  const tiedTo = new Set(ties.map(([, b]) => b)), hold = {};
  ties.forEach(([a, b]) => { hold[a] = seq.snd[b].b + seq.snd[b].d - seq.snd[a].b; });
  const inSlur = (j) => slurs.some(([a, b]) => j >= a && j < b), slurEnd = (j) => slurs.some(([, b]) => j === b);
  const run = plRun(Math.ceil(seq.n), { bpm: o.bpm || SDY_BPM, silentFrom: 0, noVoice: true, extra: (ctx, tm, i, spb) => {
    seq.snd.filter(s => Math.floor(s.b + 1e-9) === i).forEach(s => { if (tiedTo.has(s.j)) return;
      const len = (hold[s.j] != null ? hold[s.j] : s.d) * spb, dur = st.has(s.j) ? Math.min(0.16, len) : inSlur(s.j) ? len * 1.04 : slurEnd(s.j) ? len * 0.85 : len * 0.98;
      blip(ctx, tm + (s.b - i) * spb, sskHz(s.pitch), dur, vols[s.j], 'triangle'); });
  } });
  return run ? { run, seq } : null;
}
// light each note as it sounds (a tied note stays lit through its tie); done() after the last
function sdyLight(T, p, setLit, k = {}, done) {
  const tiedTo = new Set((k.ties || []).map(([, b]) => b));
  p.seq.snd.forEach(s => { if (!tiedTo.has(s.j)) T.at(p.run, p.run.at[0] + s.b * p.run.spb, () => setLit(s.j)); });
  T.at(p.run, p.run.at[0] + p.seq.n * p.run.spb + 0.05, () => { setLit(-1); if (done) done(); });
}
const sdyQ = (ds) => ds.map(d => ['q', 1, d]);
// a big sign on a button
const sdyBig = (s, size = 30, col) => <span style={{fontFamily:SDY_FONT,fontStyle:'italic',fontWeight:900,fontSize:size,lineHeight:1,color:col}}>{s}</span>;
const sdyHairIcon = (dir, col = BK.ink, w = 54) => <svg viewBox="0 0 54 20" width={w} height={w * 20 / 54} aria-hidden="true">{dir === 'cresc' ? <polyline points="50,3 4,10 50,17" fill="none" stroke={col} strokeWidth="2.2" strokeLinejoin="round"/> : <polyline points="4,3 50,10 4,17" fill="none" stroke={col} strokeWidth="2.2" strokeLinejoin="round"/>}</svg>;
const sdyScore = (s) => <span style={{color:BK.muted,fontWeight:800,whiteSpace:'nowrap'}}>{'  ·  ' + t(s.right + ' of ' + s.tries, s.tries + '개 중 ' + s.right + '개')}</span>;
const SDY_TAP = { minHeight: 44 };
const sdyBtnRow = (kids) => <div style={{display:'flex',gap:6,justifyContent:'center',marginTop:8,flexWrap:'wrap'}}>{kids}</div>;
const sdyNote = (ok, txt) => <div style={{textAlign:'center',fontSize:14,fontWeight:900,marginTop:6,color:ok ? BK.green : BK.coral}}>{ok ? t('Yes! ', '맞아요! ') : t('Not quite. ', '아쉬워요. ')}{txt}</div>;
const sdyLS = (d) => d === 'cresc' ? t('louder', '점점 세게') : t('softer', '점점 여리게');
const sdyLSName = (d) => d === 'cresc' ? t('Louder: crescendo.', '점점 세게: 크레셴도.') : t('Softer: diminuendo.', '점점 여리게: 디미누엔도.');
const SDY_AGAIN = () => t('▶ Hear again', '▶ 다시 듣기');

// ── page 2: hear the tune p or f; then listen and say which ──
function SdyPfPad() {
  const T = usePlTimers();
  const [show, setShow] = useState('p'), [lit, setLit] = useState(-1), [quiz, setQuiz] = useState(null), [score, setScore] = useState({ right: 0, tries: 0 });
  const items = SDY_ROWS.pf;
  function hear(s) { T.clear(); setLit(-1); const p = sdyPlay(items, { dyn: [[0, s]] }); if (p) sdyLight(T, p, setLit); }
  function tapSign(s) {
    if (!quiz) { setShow(s); hear(s); return; }
    if (quiz.ans) return;
    const ok = s === quiz.s; setQuiz({ ...quiz, ans: s }); setScore(x => ({ right: x.right + (ok ? 1 : 0), tries: x.tries + 1 }));
  }
  function ask() { const s = pick(['p', 'f']); setQuiz({ s, ans: null }); hear(s); }
  const k = quiz ? (quiz.ans ? { dyn: [[0, quiz.s]], dynOk: [0] } : { dynBox: [0] }) : { dyn: [[0, show]] };
  const st = (s) => !quiz || !quiz.ans ? (!quiz && s === show ? ' active' : '') : s === quiz.s ? ' good' : s === quiz.ans ? ' bad' : '';
  return (
    <div className="try-box" style={actBox} data-sdy="pf">
      <div style={actTitle}>{t('Soft or loud?', '여리게? 세게?')}</div>
      <div style={actNote}>{sdyRich(t('Tap p or f to hear the tune that way. Then tap Quiz: listen, and tap the sign you heard.', 'p나 f를 눌러 그렇게 치는 선율을 들어 봐요. 그다음 ‘퀴즈’를 누르고, 들은 기호를 눌러요.'))}</div>
      <div style={{maxWidth:440,margin:'0 auto'}}><SdyStaff full items={items} o={{ D: 22, lit }} k={k}/></div>
      <div style={{display:'grid',gridTemplateColumns:'repeat(2,minmax(0,1fr))',gap:8,maxWidth:260,margin:'6px auto 0'}}>{['p', 'f'].map(s => <button key={s} className={'choice-btn' + st(s)} onClick={() => tapSign(s)} style={{padding:'8px 0',display:'flex',flexDirection:'column',alignItems:'center',gap:2}}>{sdyBig(s, 32)}<span style={{fontSize:12.5,fontWeight:800}}>{SDY_MEAN[s]()}</span></button>)}</div>
      {quiz && quiz.ans && sdyNote(quiz.ans === quiz.s, <>{sdyBig(quiz.s, 18)} {SDY_MEAN[quiz.s]()}{sdyScore(score)}</>)}
      {sdyBtnRow(<>
        {quiz && <button className="ghost-btn" style={SDY_TAP} onClick={() => hear(quiz.s)}>{SDY_AGAIN()}</button>}
        <button className="ghost-btn" style={SDY_TAP} onClick={ask}>{quiz ? t('Next →', '다음 →') : t('Quiz', '퀴즈')}</button>
        {quiz && <button className="ghost-btn" style={SDY_TAP} onClick={() => { T.clear(); setQuiz(null); setLit(-1); }}>{t('Back', '돌아가기')}</button>}
      </>)}
    </div>
  );
}

// ── page 3: hear the ladder; then put the four signs in order, softest first ──
function SdyLadder() {
  const T = usePlTimers();
  const shuffled = () => { let o; do { o = shuffle(SDY_FOUR.slice()); } while (o.every((d, i) => d === SDY_FOUR[i])); return o; };
  const [lit, setLit] = useState(-1), [turn, setTurn] = useState(false), [cards, setCards] = useState(shuffled), [got, setGot] = useState([]), [bad, setBad] = useState(null), [slips, setSlips] = useState(0);
  const items = SDY_ROWS.four, done = got.length === 4;
  function all() { T.clear(); setLit(-1); const p = sdyPlay(items, SDY_MARKS.four); if (p) sdyLight(T, p, setLit); }
  function one(s) { T.clear(); setLit(-1); sdyPlay([['ts', 3], ...sdyQ([28, 30, 32]), ['||']], { dyn: [[0, s]] }); }
  function tap(s) {
    if (!turn) { one(s); return; }
    if (got.includes(s) || done) return;
    one(s);
    if (s === SDY_FOUR[got.length]) { setGot(g => [...g, s]); setBad(null); } else { setBad(s); setSlips(x => x + 1); }
  }
  function start() { T.clear(); setLit(-1); setTurn(true); setGot([]); setSlips(0); setBad(null); setCards(shuffled()); }
  const k = turn ? { dyn: got.map((s, i) => [i * 3, s]), dynOk: got.map((_, i) => i * 3), dynBox: [0, 3, 6, 9].slice(got.length) } : SDY_MARKS.four;
  return (
    <div className="try-box" style={actBox} data-sdy="ladder">
      <div style={actTitle}>{sdyRich(t('From pp to f', 'pp에서 f까지'))}</div>
      <div style={actNote}>{t('Listen: each bar a little louder. Then tap Your turn and tap the signs from the softest to the loudest. Each one sounds as you tap it.', '들어 봐요: 한 마디씩 조금 더 세게. 그다음 ‘내 차례’를 누르고 가장 여린 것부터 가장 센 것까지 기호를 눌러요. 누를 때마다 소리가 나요.')}</div>
      <div style={{maxWidth:520,margin:'0 auto'}}><SdyStaff full items={items} o={{ D: 22, lit }} k={k}/></div>
      <div style={{display:'grid',gridTemplateColumns:'repeat(4,minmax(0,1fr))',gap:6,maxWidth:340,margin:'6px auto 0'}}>{(turn ? cards : SDY_FOUR).map(s => { const used = turn && got.includes(s);
        return <button key={s} className={'choice-btn' + (bad === s ? ' bad' : '')} disabled={used} onClick={() => tap(s)} style={{padding:'8px 0',minHeight:48,opacity:used ? 0.3 : 1}}>{sdyBig(s, 26)}</button>; })}</div>
      {turn && <div style={{textAlign:'center',fontSize:14,fontWeight:900,marginTop:6,color:done ? BK.green : bad ? BK.coral : BK.muted}}>
        {done ? (slips ? t('Done! ' + slips + (slips > 1 ? ' mistakes' : ' mistake') + '.', '다 했어요! 실수 ' + slips + '번.') : t('Perfect, no mistakes! ✓', '완벽해요, 실수 없이! ✓'))
          : bad ? t('Not yet: find a softer one.', '아직이에요: 더 여린 것을 찾아요.') : got.length ? t('Next: the next softest', '다음: 그다음으로 여린 것') : t('Next: the softest', '다음: 가장 여린 것')}</div>}
      {sdyBtnRow(<>
        <button className="ghost-btn" style={SDY_TAP} onClick={all}>{t('▶ Listen', '▶ 듣기')}</button>
        <button className="ghost-btn" style={SDY_TAP} onClick={start}>{turn ? t('Start again', '처음부터') : t('Your turn', '내 차례')}</button>
      </>)}
    </div>
  );
}

// ── page 4: hear the hairpins; then listen and say: louder or softer? ──
const sdyHairItems = (w) => [['ts', 4], ...sdyQ(w.slice(0, 4)), ['|'], ['w', 4, w[4]], ['||']];
const sdyHairMarks = (dir) => dir === 'cresc' ? { dyn: [[0, 'p'], [4, 'f']], hair: [[0, 3, 'cresc']] } : { dyn: [[0, 'f'], [4, 'p']], hair: [[0, 3, 'dim']] };
function SdyHairPad() {
  const T = usePlTimers();
  const [lit, setLit] = useState(-1), [quiz, setQuiz] = useState(null), [score, setScore] = useState({ right: 0, tries: 0 });
  function play(items, k) { T.clear(); setLit(-1); const p = sdyPlay(items, k); if (p) sdyLight(T, p, setLit); }
  function ask() { const dir = pick(['cresc', 'dim']), w = sskWalk(5); setQuiz({ dir, w, ans: null }); play(sdyHairItems(w), sdyHairMarks(dir)); }
  function answer(d) { if (!quiz || quiz.ans) return; const ok = d === quiz.dir; setQuiz({ ...quiz, ans: d }); setScore(x => ({ right: x.right + (ok ? 1 : 0), tries: x.tries + 1 })); }
  const items = quiz ? sdyHairItems(quiz.w) : SDY_ROWS.hair;
  const k = quiz ? (quiz.ans ? { ...sdyHairMarks(quiz.dir), dynOk: [0, 4], hairOk: [0] } : { hairBox: [[0, 3]] }) : SDY_MARKS.hair;
  return (
    <div className="try-box" style={actBox} data-sdy="hair">
      <div style={actTitle}>{t('Louder or softer?', '점점 세게? 점점 여리게?')}</div>
      <div style={actNote}>{t('Listen: louder through the hairpin that opens, softer through the one that closes. Then tap Quiz: listen, and tap the hairpin you heard.', '들어 봐요: 벌어지는 헤어핀에서 점점 세게, 좁아지는 헤어핀에서 점점 여리게. 그다음 ‘퀴즈’를 누르고, 들은 헤어핀을 눌러요.')}</div>
      <div style={{maxWidth:quiz ? 360 : 520,margin:'0 auto'}}><SdyStaff full items={items} o={{ D: quiz ? 26 : 17, lit }} k={k}/></div>
      {quiz && <div style={{display:'grid',gridTemplateColumns:'repeat(2,minmax(0,1fr))',gap:8,maxWidth:320,margin:'6px auto 0'}}>{['cresc', 'dim'].map(d => <button key={d} className={'choice-btn' + (!quiz.ans ? '' : d === quiz.dir ? ' good' : d === quiz.ans ? ' bad' : '')} onClick={() => answer(d)} style={{padding:'8px 0',display:'flex',flexDirection:'column',alignItems:'center',gap:3}}>{sdyHairIcon(d)}<span style={{fontSize:13,fontWeight:900}}>{sdyLS(d)}</span></button>)}</div>}
      {quiz && quiz.ans && sdyNote(quiz.ans === quiz.dir, <>{sdyLSName(quiz.dir)}{sdyScore(score)}</>)}
      {sdyBtnRow(<>
        <button className="ghost-btn" style={SDY_TAP} onClick={() => quiz ? play(sdyHairItems(quiz.w), sdyHairMarks(quiz.dir)) : play(SDY_ROWS.hair, SDY_MARKS.hair)}>{quiz ? SDY_AGAIN() : t('▶ Listen', '▶ 듣기')}</button>
        <button className="ghost-btn" style={SDY_TAP} onClick={ask}>{quiz ? t('Next →', '다음 →') : t('Quiz', '퀴즈')}</button>
        {quiz && <button className="ghost-btn" style={SDY_TAP} onClick={() => { T.clear(); setQuiz(null); setLit(-1); }}>{t('Back', '돌아가기')}</button>}
      </>)}
    </div>
  );
}

// ── page 5: hear legato and staccato, the sound lines lighting; then listen and say which ──
function SdyTouchPad() {
  const T = usePlTimers();
  const [lit, setLit] = useState({ row: -1, j: -1 }), [quiz, setQuiz] = useState(null), [score, setScore] = useState({ right: 0, tries: 0 });
  const rows = [['legato', SDY_MARKS.leg], ['staccato', SDY_MARKS.stac]];
  function play(row) { T.clear(); setLit({ row: -1, j: -1 }); const p = sdyPlay(SDY_ROWS.touch, rows[row][1]); if (p) sdyLight(T, p, (j) => setLit({ row, j })); }
  function ask() { const row = Math.random() < 0.5 ? 0 : 1; setQuiz({ row, ans: null }); play(row); }
  function answer(r) { if (!quiz || quiz.ans != null) return; const ok = r === quiz.row; setQuiz({ ...quiz, ans: r }); setScore(x => ({ right: x.right + (ok ? 1 : 0), tries: x.tries + 1 })); }
  const name = (r) => r === 0 ? t('legato', '레가토') : t('staccato', '스타카토');
  const staff = (row, k) => <SdyStaff full items={SDY_ROWS.touch} o={{ D: 24, lit: lit.row === row ? lit.j : -1 }} k={{ ...k, lit: lit.row === row ? lit.j : -1 }}/>;
  return (
    <div className="try-box" style={actBox} data-sdy="touch">
      <div style={actTitle}>{t('Legato or staccato?', '레가토? 스타카토?')}</div>
      <div style={actNote}>{t('Tap ▶ on each tune and watch its sound lines. Then tap Quiz: listen, and tap legato or staccato.', '▶를 눌러 악보마다 들으며 소리 줄을 봐요. 그다음 ‘퀴즈’를 누르고, 레가토나 스타카토를 눌러요.')}</div>
      {!quiz && <div style={{display:'grid',gap:6,maxWidth:420,margin:'0 auto'}}>{rows.map(([n, k], row) => <div key={n}>
        <button className={'chip' + (lit.row === row ? ' active' : '')} onClick={() => play(row)} style={{padding:'5px 14px',minHeight:44,fontWeight:900}}>▶ {name(row)}</button>{staff(row, k)}</div>)}</div>}
      {quiz && <div style={{maxWidth:380,margin:'0 auto'}}>{staff(quiz.row, quiz.ans != null ? rows[quiz.row][1] : {})}</div>}
      {quiz && <div style={{display:'grid',gridTemplateColumns:'repeat(2,minmax(0,1fr))',gap:8,maxWidth:300,margin:'6px auto 0'}}>{[0, 1].map(r => <button key={r} className={'choice-btn' + (quiz.ans == null ? '' : r === quiz.row ? ' good' : r === quiz.ans ? ' bad' : '')} onClick={() => answer(r)} style={{padding:'12px 0',fontSize:16,fontWeight:900}}>{name(r)}</button>)}</div>}
      {quiz && quiz.ans != null && sdyNote(quiz.ans === quiz.row, <>{quiz.row === 0 ? t('Legato: smooth and joined.', '레가토: 부드럽게 이어서.') : t('Staccato: short.', '스타카토: 짧게 끊어서.')}{sdyScore(score)}</>)}
      {sdyBtnRow(<>
        {quiz && <button className="ghost-btn" style={SDY_TAP} onClick={() => play(quiz.row)}>{SDY_AGAIN()}</button>}
        <button className="ghost-btn" style={SDY_TAP} onClick={ask}>{quiz ? t('Next →', '다음 →') : t('Quiz', '퀴즈')}</button>
        {quiz && <button className="ghost-btn" style={SDY_TAP} onClick={() => { T.clear(); setQuiz(null); setLit({ row: -1, j: -1 }); }}>{t('Back', '돌아가기')}</button>}
      </>)}
    </div>
  );
}

// ── page 6: a curve over two or three notes: tie or slur? Then hear it. A pair always has a bar line between, so only
// the notes tell (two tied notes in one bar would be one longer note) ──
function sdyTieQ(prevKey) {
  for (let g = 0; g < 30; g++) {
    const tie = Math.random() < 0.5, d = 28 + Math.floor(Math.random() * 5), kind = pick(['h', 'q']), n = kind === 'h' ? 2 : 1;
    let items, k;
    if (tie) { items = [[kind, n, d], ['|'], [kind, n, d]]; k = { ties: [[0, 1]] }; }
    else if (Math.random() < 0.6) { const e = d + pick([-2, -1, 1, 2]); if (e < 28 || e > 32) continue; items = [[kind, n, d], ['|'], [kind, n, e]]; k = { slurs: [[0, 1]] }; }
    else { const s = pick([-1, 1]), ds = [d, d + s, d + 2 * s]; if (ds.some(x => x < 28 || x > 32)) continue; items = sdyQ(ds); k = { slurs: [[0, 2]] }; }
    items = [...items, ['sp', 8]];
    const key = (tie ? 't' : 's') + JSON.stringify(items);
    if (key === prevKey) continue;
    return { tie, items, k, key, answer: tie ? 'tie' : 'slur' };
  }
  return { tie: true, items: [['h', 2, 30], ['|'], ['h', 2, 30], ['sp', 8]], k: { ties: [[0, 1]] }, key: 'x', answer: 'tie' };
}
function SdyTiePad() {
  const T = usePlTimers();
  const [lit, setLit] = useState({ row: -1, j: -1 }), [quiz, setQuiz] = useState(null), [score, setScore] = useState({ right: 0, tries: 0 });
  const rows = [['slur', SDY_ROWS.slur, SDY_MARKS.slur], ['tie', SDY_ROWS.tie, SDY_MARKS.tie]];
  function play(items, k, row) { T.clear(); setLit({ row: -1, j: -1 }); const p = sdyPlay(items, k); if (p) sdyLight(T, p, (j) => setLit({ row, j }), k); }
  function ask() { T.clear(); setLit({ row: -1, j: -1 }); setQuiz({ ...sdyTieQ(quiz && quiz.key), ans: null }); }
  function answer(a) { if (!quiz || quiz.ans) return; const ok = a === quiz.answer; setQuiz({ ...quiz, ans: a }); setScore(x => ({ right: x.right + (ok ? 1 : 0), tries: x.tries + 1 })); play(quiz.items, quiz.k, 9); }
  const name = (a) => a === 'tie' ? t('tie', '붙임줄') : t('slur', '이음줄');
  const qLit = lit.row === 9 ? lit.j : -1;
  return (
    <div className="try-box" style={actBox} data-sdy="tie">
      <div style={actTitle}>{t('Tie or slur?', '붙임줄? 이음줄?')}</div>
      <div style={actNote}>{t('Tap ▶ on each tune and watch its sound lines. Then tap Quiz: is the curve a tie or a slur? Look at the notes: the same, or different?', '▶를 눌러 악보마다 들으며 소리 줄을 봐요. 그다음 ‘퀴즈’를 눌러요: 이 곡선은 붙임줄일까요, 이음줄일까요? 음을 봐요: 같은 음, 다른 음?')}</div>
      {!quiz && <div style={{display:'grid',gap:6,maxWidth:420,margin:'0 auto'}}>{rows.map(([n, items, k], row) => <div key={n}>
        <button className={'chip' + (lit.row === row ? ' active' : '')} onClick={() => play(items, k, row)} style={{padding:'5px 14px',minHeight:44,fontWeight:900}}>▶ {name(n)}</button>
        <SdyStaff full items={items} o={{ D: 24, lit: lit.row === row ? lit.j : -1 }} k={{ ...k, lit: lit.row === row ? lit.j : -1 }}/></div>)}</div>}
      {quiz && <div style={{maxWidth:260,margin:'0 auto'}}><SdyStaff full items={quiz.items} o={{ D: 34, x0: 52, lit: qLit }} k={{ ...quiz.k, sound: !!quiz.ans, lit: qLit }}/></div>}
      {quiz && <div style={{display:'grid',gridTemplateColumns:'repeat(2,minmax(0,1fr))',gap:8,maxWidth:300,margin:'6px auto 0'}}>{['tie', 'slur'].map(a => <button key={a} className={'choice-btn' + (!quiz.ans ? '' : a === quiz.answer ? ' good' : a === quiz.ans ? ' bad' : '')} onClick={() => answer(a)} style={{padding:'12px 0',fontSize:16,fontWeight:900}}>{name(a)}</button>)}</div>}
      {quiz && quiz.ans && sdyNote(quiz.ans === quiz.answer, <>{quiz.tie ? t('A tie: the same note, played once and held.', '붙임줄: 같은 음, 한 번 치고 계속 눌러요.') : t('A slur: different notes, played legato.', '이음줄: 다른 음, 레가토로 쳐요.')}{sdyScore(score)}</>)}
      {sdyBtnRow(<>
        {quiz && quiz.ans && <button className="ghost-btn" style={SDY_TAP} onClick={() => play(quiz.items, quiz.k, 9)}>{SDY_AGAIN()}</button>}
        <button className="ghost-btn" style={SDY_TAP} onClick={ask}>{quiz ? t('Next →', '다음 →') : t('Quiz', '퀴즈')}</button>
        {quiz && <button className="ghost-btn" style={SDY_TAP} onClick={() => { T.clear(); setQuiz(null); setLit({ row: -1, j: -1 }); }}>{t('Back', '돌아가기')}</button>}
      </>)}
    </div>
  );
}
function SdyPad({ page }) { return page === 2 ? <SdyPfPad/> : page === 4 ? <SdyHairPad/> : page === 5 ? <SdyTouchPad/> : <SdyTiePad/>; }

// ── the book on screen: the opener is the lesson's head, every other page a step. Old ticks kept where the idea is the
// same: 'Soft to loud' (0), 'Getting louder and softer' (1), 'Articulation' (3); pp to f, slur and tie and the checks
// are new (5, 6, 7). The pedals (old step 2) wait for their room; the old ear step (4) is drill levels 6 to 8 ──
const SDY_STORE = [0, 5, 1, 3, 6, 7];
function SdyLearn({ onStart }) {
  const pages = sdyLbPages(true);
  const opener = pages[0];
  return (
    <Lesson id="dynamics" title={t('Dynamics & Articulation', '다이나믹과 아티큘레이션')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="dynamics"><div className="lb-screen lb-open" style={{display:'flex',flexDirection:'column',gap:12,margin:'0 0 8px'}}>{lbWordsFirst(opener.props.children)}</div></BkChapterCtx.Provider></LbScreenCtx.Provider>}>
      {pages.slice(1).map((pg, i) => (
        <Step key={i} storeAs={SDY_STORE[i]} title={pg.props.title}>
          <LbScreenPage page={pg}/>
        </Step>
      ))}
    </Lesson>
  );
}

// ── the drill: five levels by eye, three by ear, then the Grade 1 signs ──
const SDY_LEVELS = [
  { n: 1, label: 'pp p mf f: what does it mean?', kind: 'mean', time: 8 },
  { n: 2, label: 'Which is louder?', kind: 'louder', time: 6 },
  { n: 3, label: 'Hairpins and words: louder or softer?', kind: 'hair', time: 7 },
  { n: 4, label: 'Legato or staccato?', kind: 'touch', time: 7 },
  { n: 5, label: 'Tie or slur?', kind: 'tie', time: 7 },
  { n: 6, label: 'Listen: which time was louder?', kind: 'earLoud', time: 14, noPrint: true },
  { n: 7, label: 'Listen: louder or softer?', kind: 'earHair', time: 12, noPrint: true },
  { n: 8, label: 'Listen: legato or staccato?', kind: 'earTouch', time: 12, noPrint: true },
  { n: 9, label: 'Extra: mp and ff', kind: 'more', time: 8 },
];
Object.assign(LEVEL_KO, {
  'pp p mf f: what does it mean?': 'pp p mf f: 무슨 뜻일까요?', 'Which is louder?': '어느 쪽이 더 셀까요?', 'Hairpins and words: louder or softer?': '헤어핀과 줄임말: 점점 세게? 점점 여리게?',
  'Legato or staccato?': '레가토? 스타카토?', 'Tie or slur?': '붙임줄? 이음줄?', 'Listen: which time was louder?': '듣기: 몇 번째가 더 셌을까요?',
  'Listen: louder or softer?': '듣기: 점점 세게? 점점 여리게?', 'Listen: legato or staccato?': '듣기: 레가토? 스타카토?', 'Extra: mp and ff': '더 해 보기: mp와 ff',
});
function genSdyQuestion(lv, prev) {
  const uid = Math.random(), pk = prev && prev.key;
  const again = (f) => { for (let g = 0; g < 20; g++) { const q = f(); if (q.key !== pk) return { ...q, uid }; } return { ...f(), uid }; };
  if (lv.kind === 'mean') return again(() => { const d = pick(SDY_FOUR); return { kind: 'mean', d, key: d, answer: d, choices: SDY_FOUR.slice() }; });
  if (lv.kind === 'louder') return again(() => { const pr = shuffle(sampleN(SDY_FOUR, 2)); return { kind: 'louder', key: pr.join(), answer: SDY_SIX.indexOf(pr[0]) > SDY_SIX.indexOf(pr[1]) ? pr[0] : pr[1], choices: pr }; });
  if (lv.kind === 'hair') return again(() => { const dir = pick(['cresc', 'dim']);
    if (Math.random() < 0.35) { const w = dir === 'cresc' ? 'cresc.' : pick(['dim.', 'decresc.']); return { kind: 'word', w, key: 'w' + w, answer: dir === 'cresc' ? 'cresc' : 'dim', choices: ['cresc', 'dim'] }; }
    const w = sskWalk(5); return { kind: 'hair', dir, w, key: 'h' + dir + w.join(''), answer: dir, choices: ['cresc', 'dim'] }; });
  if (lv.kind === 'earHair') return again(() => { const dir = pick(['cresc', 'dim']), w = sskWalk(5); return { kind: 'earHair', dir, w, key: 'e' + dir + w.join(''), answer: dir, choices: ['cresc', 'dim'] }; });
  if (lv.kind === 'touch' || lv.kind === 'earTouch') return again(() => { const leg = Math.random() < 0.5, w = sskWalk(lv.kind === 'touch' ? 4 : 5); return { kind: lv.kind, leg, w, key: lv.kind + leg + w.join(''), answer: leg ? 'legato' : 'staccato', choices: ['legato', 'staccato'] }; });
  if (lv.kind === 'tie') { const q = sdyTieQ(pk); return { kind: 'tie', ...q, choices: ['tie', 'slur'], uid }; }
  if (lv.kind === 'earLoud') return again(() => { const pr = shuffle(pick([['pp', 'mf'], ['pp', 'f'], ['p', 'f']])), w = sskWalk(3); return { kind: 'earLoud', pr, w, key: pr.join() + w.join(''), answer: SDY_SIX.indexOf(pr[0]) > SDY_SIX.indexOf(pr[1]) ? '1' : '2', choices: ['1', '2'] }; });
  // the extra level: mp and ff
  return again(() => { const sub = pick(['mean', 'louder']);
    if (sub === 'mean') { const d = pick(['mp', 'ff']); return { kind: 'more', sub, d, key: 'm' + d, answer: d, choices: shuffle([d, ...sampleN(SDY_SIX.filter(x => x !== d), 3)]) }; }
    const a = pick(['mp', 'ff']), b = pick(SDY_SIX.filter(x => x !== a)), pr = shuffle([a, b]);
    return { kind: 'more', sub, key: 'l' + pr.join(), answer: SDY_SIX.indexOf(pr[0]) > SDY_SIX.indexOf(pr[1]) ? pr[0] : pr[1], choices: pr }; });
}
const sdyTouchItems = (w) => w.length === 4 ? [['ts', 4], ...sdyQ(w), ['sp', 10], ['||']] : [['ts', 4], ...sdyQ(w.slice(0, 4)), ['|'], ['w', 4, w[4]], ['||']];
const sdyTouchMarks = (leg, n) => leg ? { slurs: [[0, n - 1]] } : { stacc: [0, 1, 2, 3] };
const sdyLoudItems = (w) => [['ts', 4], ...sdyQ(w.slice(0, 2)), ['h', 2, w[2]], ['|'], ...sdyQ(w.slice(0, 2)), ['h', 2, w[2]], ['||']];
function SdyQuestion(props) {
  const { q, given, locked, onAnswer, pixel } = props;
  const board = useBoard(q, given);
  const T = usePlTimers();
  const [lit, setLit] = useState(-1);
  const play = (items, k, o) => { T.clear(); setLit(-1); const p = sdyPlay(items, k, o); if (p) sdyLight(T, p, setLit, k); };
  const earLoud = () => { const v = [0, 1, 2].map(() => SDY_VOL[q.pr[0]]).concat([0, 1, 2].map(() => SDY_VOL[q.pr[1]])); play(sdyLoudItems(q.w), {}, { vols: v }); };
  const hear = () => { if (q.kind === 'earHair') play(sdyHairItems(q.w), sdyHairMarks(q.dir)); else if (q.kind === 'earTouch') play(sdyTouchItems(q.w), sdyTouchMarks(q.leg, 5)); else if (q.kind === 'earLoud') earLoud(); };
  useEffect(() => { T.clear(); setLit(-1); if (q.kind.startsWith('ear')) setTimeout(hear, 250); }, [q.uid]);
  const done = !!given;
  const ink = pixel ? '#faf6ec' : '#26296b';
  const btnCls = pixel ? 'pixel-choice' : 'choice-btn';
  const st = (c) => !done ? '' : c === q.answer ? ' good' : (given.ans === c ? ' bad' : '');
  const prompt = (txt) => <p style={pixel ? {fontSize:11.5,textAlign:'center',margin:'0 0 10px',lineHeight:1.7} : {fontSize:15,fontWeight:700,textAlign:'center',margin:'0 0 10px',color:'var(--muted)'}}>{txt}</p>;
  const box = (kids) => <div style={{background:pixel ? '#faf6ec' : 'transparent',borderRadius:8,padding:pixel ? 6 : 0,margin:'0 auto 10px'}}>{kids}</div>;
  const after = () => { if (q.kind === 'hair') play(sdyHairItems(q.w), sdyHairMarks(q.dir)); else if (q.kind === 'touch') play(sdyTouchItems(q.w), sdyTouchMarks(q.leg, 4)); else if (q.kind === 'tie') play(q.items, q.k); else if (q.kind === 'mean' || (q.kind === 'more' && q.sub === 'mean')) play([['ts', 3], ...sdyQ([28, 30, 32]), ['||']], { dyn: [[0, q.d]] }); };
  const grid = (cols, render, pad = '14px 4px') => <div style={{display:'grid',gridTemplateColumns:'repeat(' + cols + ',minmax(0,1fr))',gap:8}}>{q.choices.map(c => <button key={c} disabled={locked} onClick={() => { T.clear(); setLit(-1); onAnswer(c); if (!q.kind.startsWith('ear')) setTimeout(after, 150); }} className={btnCls + st(c)} style={{padding:pad}}>{render(c)}</button>)}</div>;
  const again = <div style={{textAlign:'center',margin:'0 0 12px'}}><button className={pixel ? 'pixel-btn' : 'ghost-btn'} onClick={hear} style={pixel ? {fontSize:9} : {fontSize:15,padding:'8px 16px',minHeight:44}}>{SDY_AGAIN()}</button></div>;
  const hairBtn = (c) => <span style={{display:'flex',flexDirection:'column',alignItems:'center',gap:3}}>{sdyHairIcon(c, pixel ? '#faf6ec' : BK.ink, pixel ? 40 : 54)}<span style={{fontSize:pixel ? 10 : 14,fontWeight:900}}>{sdyLS(c)}</span></span>;
  const touchName = (c) => c === 'legato' ? t('legato', '레가토') : t('staccato', '스타카토');
  const big = (s) => <div style={{textAlign:'center',margin:'4px 0 14px',minHeight:50,display:'flex',justifyContent:'center',alignItems:'center'}}>{sdyBig(s, 58, ink)}</div>;
  let body;
  if (q.kind === 'mean' || (q.kind === 'more' && q.sub === 'mean')) body = <>{prompt(t('What does this sign mean?', '이 기호는 무슨 뜻일까요?'))}{big(q.d)}{grid(2, c => <span style={{fontSize:pixel ? 10 : 15,fontWeight:800}}>{SDY_MEAN[c]()}</span>)}</>;
  else if (q.kind === 'louder' || q.kind === 'more') body = <>{prompt(t('Which one is louder?', '어느 쪽이 더 셀까요?'))}{grid(2, c => sdyBig(c, pixel ? 24 : 36), '10px 4px')}</>;
  else if (q.kind === 'word') body = <>{prompt(t('What does this word mean?', '이 줄임말은 무슨 뜻일까요?'))}<div style={{textAlign:'center',margin:'4px 0 14px',fontFamily:SDY_FONT,fontStyle:'italic',fontSize:40,color:ink}}>{q.w}</div>{grid(2, hairBtn, '8px 4px')}</>;
  else if (q.kind === 'hair') body = <>{prompt(t('This hairpin means:', '이 헤어핀의 뜻은:'))}{box(<div style={{maxWidth:320,margin:'0 auto'}}><SdyStaff full items={sdyHairItems(q.w)} o={{ D: 28, lit }} k={{ hair: [[0, 3, q.dir]] }}/></div>)}{grid(2, hairBtn, '8px 4px')}</>;
  else if (q.kind === 'touch') body = <>{prompt(t('Legato or staccato?', '레가토일까요, 스타카토일까요?'))}{box(<div style={{maxWidth:280,margin:'0 auto'}}><SdyStaff full items={sdyTouchItems(q.w)} o={{ D: 30, lit }} k={{ ...sdyTouchMarks(q.leg, 4), sound: done, lit }}/></div>)}{grid(2, c => <span style={{fontSize:pixel ? 11 : 16,fontWeight:900}}>{touchName(c)}</span>)}</>;
  else if (q.kind === 'tie') body = <>{prompt(t('A tie or a slur?', '붙임줄일까요, 이음줄일까요?'))}{box(<div style={{maxWidth:280,margin:'0 auto'}}><SdyStaff full items={q.items} o={{ D: 36, x0: 52, lit }} k={{ ...q.k, sound: done, lit }}/></div>)}{grid(2, c => <span style={{fontSize:pixel ? 11 : 16,fontWeight:900}}>{c === 'tie' ? t('tie', '붙임줄') : t('slur', '이음줄')}</span>)}</>;
  else if (q.kind === 'earLoud') body = <>{prompt(t('The same tune, twice. Which time was louder?', '같은 선율이 두 번 나와요. 어느 쪽이 더 셌나요?'))}{box(<div style={{maxWidth:340,margin:'0 auto'}}><SdyStaff full items={sdyLoudItems(q.w)} o={{ D: 26, lit }} k={done ? { dyn: [[0, q.pr[0]], [3, q.pr[1]]], dynOk: [q.answer === '1' ? 0 : 3] } : {}}/></div>)}{again}{grid(2, c => <span style={{fontSize:pixel ? 11 : 16,fontWeight:900}}>{c === '1' ? t('the first time', '첫 번째') : t('the second time', '두 번째')}</span>)}</>;
  else if (q.kind === 'earHair') body = <>{prompt(t('Listen. Louder or softer?', '들어 봐요. 점점 세게일까요, 점점 여리게일까요?'))}{box(<div style={{maxWidth:320,margin:'0 auto'}}><SdyStaff full items={sdyHairItems(q.w)} o={{ D: 28, lit }} k={done ? { ...sdyHairMarks(q.dir), hairOk: [0], dynOk: [0, 4] } : {}}/></div>)}{again}{grid(2, hairBtn, '8px 4px')}</>;
  else body = <>{prompt(t('Listen. Legato or staccato?', '들어 봐요. 레가토일까요, 스타카토일까요?'))}{box(<div style={{maxWidth:320,margin:'0 auto'}}><SdyStaff full items={sdyTouchItems(q.w)} o={{ D: 28, lit }} k={done ? { ...sdyTouchMarks(q.leg, 5), sound: true, lit } : {}}/></div>)}{again}{grid(2, c => <span style={{fontSize:pixel ? 11 : 16,fontWeight:900}}>{touchName(c)}</span>)}</>;
  return <div><BoardTrack b={board} pixel={pixel}/>{body}</div>;
}
function sdyCheck(q, ans) { return ans !== null && ans !== undefined && ans === q.answer; }
function sdyAnswerLabel(q) {
  const sign = (d) => d + ' (' + SDY_IT[d] + ': ' + SDY_MEAN[d]() + ')';
  if (q.kind === 'mean' || (q.kind === 'more' && q.sub === 'mean')) return sign(q.d);
  if (q.kind === 'louder' || q.kind === 'more') return sign(q.answer);
  if (q.kind === 'word') return q.w + ' (' + sdyLS(q.answer) + ')';
  if (q.kind === 'hair' || q.kind === 'earHair') return q.answer === 'cresc' ? t('crescendo (louder)', '크레셴도(점점 세게)') : t('diminuendo (softer)', '디미누엔도(점점 여리게)');
  if (q.kind === 'touch' || q.kind === 'earTouch') return q.answer === 'legato' ? t('legato (smooth and joined)', '레가토(부드럽게 이어서)') : t('staccato (short)', '스타카토(짧게 끊어서)');
  if (q.kind === 'tie') return q.tie ? t('a tie (the same note)', '붙임줄(같은 음)') : t('a slur (different notes)', '이음줄(다른 음)');
  return (q.answer === '1' ? t('the first time', '첫 번째') : t('the second time', '두 번째')) + ' (' + q.pr[0] + ', ' + q.pr[1] + ')';
}
Object.assign(DYN_DRILL, { levels: SDY_LEVELS, generate: genSdyQuestion, check: sdyCheck, answerLabel: sdyAnswerLabel, Question: SdyQuestion, Learn: SdyLearn });
