// ─── Phase 469: chapter 13 on screen (what moves on pages 2 to 6), the book as the online lesson, and the drill ───
// Tunes and ticks on the audio clock (plRun): a count-in when asked, the metronome ticking on when asked, each note
// joined to the next.
const STM_VOL = 0.26;
function stmPlay(items, bpm, o = {}) {
  const seq = sskSeq(items), ci = o.countIn || 0, n = Math.ceil(seq.n) + ci;
  const run = plRun(n, { bpm, silentFrom: o.click ? undefined : ci, noVoice: true, vol: 0.3, extra: (ctx, tm, i, spb) => {
    seq.snd.filter(s => Math.floor(s.b + 1e-9) === i - ci).forEach(s => blip(ctx, tm + (s.b - (i - ci)) * spb, sskHz(s.pitch), s.d * spb * 0.96, STM_VOL, 'triangle')); } });
  return run ? { run, seq, ci } : null;
}
function stmLight(T, p, setLit, done) {
  p.seq.snd.forEach(s => T.at(p.run, p.run.at[0] + (s.b + p.ci) * p.run.spb, () => setLit(s.j)));
  T.at(p.run, p.run.at[0] + (p.seq.n + p.ci) * p.run.spb + 0.05, () => { setLit(-1); if (done) done(); });
}
// eight ticks: steady, rushing (the gaps shrink) or dragging (the gaps grow)
const STM_FEEL = { steady: (i) => 1, rush: (i) => 1 - 0.05 * i, drag: (i) => 1 + 0.07 * i };
function stmFeel(kind, bpm = 90) { const spb = 60 / bpm; return plRun(8, { bpm, noVoice: true, vol: 0.32, gaps: Array.from({ length: 8 }, (_, i) => spb * STM_FEEL[kind](i)) }); }
const STM_FEEL_W = { steady: () => t('steady', '꾸준하게'), rush: () => t('rushing', '서두르기'), drag: () => t('dragging', '처지기') };
const stmScore = (s) => <span style={{color:BK.muted,fontWeight:800,whiteSpace:'nowrap'}}>{'  ·  ' + t(s.right + ' of ' + s.tries, s.tries + '개 중 ' + s.right + '개')}</span>;
const stmNote = (ok, txt) => <div style={{textAlign:'center',fontSize:14,fontWeight:900,marginTop:6,color:ok ? BK.green : BK.coral,textWrap:'balance',wordBreak:'keep-all'}}>{ok ? t('Yes!', '맞아요!') : t('Not quite.', '아쉬워요.')}{' '}{txt}</div>;
const STM_TAP = { minHeight: 44 };
const stmRow = (kids) => <div style={{display:'flex',gap:6,justifyContent:'center',marginTop:8,flexWrap:'wrap'}}>{kids}</div>;
const stmQuizBtns = (quiz, onNext, onBack, extra) => stmRow(<>{extra}<button className="ghost-btn" style={STM_TAP} onClick={onNext}>{quiz ? t('Next →', '다음 →') : t('Quiz', '퀴즈')}</button>{quiz && <button className="ghost-btn" style={STM_TAP} onClick={onBack}>{t('Back', '돌아가기')}</button>}</>);
const STM_AGAIN = () => t('▶ Hear again', '▶ 다시 듣기');
const stmWordHtml = (w, size = 17) => <span style={{fontFamily:STM_FONT,fontWeight:900,fontSize:size,color:'inherit'}}>{w}</span>;
const stmAsk = (txt) => <div style={{textAlign:'center',fontSize:14,fontWeight:800,color:BK.ink,margin:'4px 0',textWrap:'balance',wordBreak:'keep-all'}}>{txt}</div>;
const STM_SF = { slow: () => t('slow', '느리게'), fast: () => t('fast', '빠르게') };
const STM_SF_BPM = { slow: 60, fast: 120 };   // as the seconds ruler on book page 2: one beat a second, then two
const useStmScore = () => useState({ right: 0, tries: 0 });

// ── page 2: the tune slow or fast; then listen and say which ──
function StmSlowFastPad() {
  const T = usePlTimers();
  const [lit, setLit] = useState(-1), [quiz, setQuiz] = useState(null), [score, setScore] = useStmScore();
  function hear(k) { T.clear(); setLit(-1); const p = stmPlay(STM_ROWS.walk, STM_SF_BPM[k], { click: true }); if (p) stmLight(T, p, setLit); }
  function tap(k) { if (!quiz) { hear(k); return; } if (quiz.ans) return; const ok = k === quiz.k; setQuiz({ ...quiz, ans: k }); setScore(s => ({ right: s.right + (ok ? 1 : 0), tries: s.tries + 1 })); }
  function ask() { const k = pick(['slow', 'fast']); setQuiz({ k, ans: null }); hear(k); }
  const st = (k) => !quiz || !quiz.ans ? '' : k === quiz.k ? ' good' : k === quiz.ans ? ' bad' : '';
  return (
    <div className="try-box" style={actBox} data-stm="sf">
      <div style={actTitle}>{t('Slow or fast?', '느리게? 빠르게?')}</div>
      {!quiz && <div style={actNote}>{t('Tap slow or fast to hear the tune. Then tap Quiz.', '‘느리게’나 ‘빠르게’를 눌러 선율을 들어 봐요. 그다음 ‘퀴즈’를 눌러요.')}</div>}
      <div style={{maxWidth:420,margin:'0 auto'}}><StmTune items={STM_ROWS.walk} o={{ lit }}/></div>
      {quiz && stmAsk(t('Listen. Slow or fast?', '들어 봐요. 느리게? 빠르게?'))}
      <div style={{display:'grid',gridTemplateColumns:'repeat(2,minmax(0,1fr))',gap:8,maxWidth:300,margin:'6px auto 0'}}>{['slow', 'fast'].map(k => <button key={k} className={'choice-btn' + st(k)} onClick={() => tap(k)} style={{padding:'12px 0',fontSize:16,fontWeight:900}}>{quiz ? STM_SF[k]() : '▶ ' + STM_SF[k]()}</button>)}</div>
      {quiz && quiz.ans && stmNote(quiz.ans === quiz.k, <>{quiz.k === 'slow' ? t('Slow: the beats far apart.', '느리게: 박과 박 사이가 멀어요.') : t('Fast: the beats close together.', '빠르게: 박과 박 사이가 가까워요.')}{stmScore(score)}</>)}
      {stmQuizBtns(quiz, ask, () => { T.clear(); stopClicks(); setQuiz(null); setLit(-1); }, quiz && <button className="ghost-btn" style={STM_TAP} onClick={() => hear(quiz.k)}>{STM_AGAIN()}</button>)}
    </div>
  );
}

// ── page 3: tap a word to hear the tune at its tempo, the beats lighting up; then listen and say which word ──
const STM_FAR = [['Adagio', 'Moderato'], ['Adagio', 'Allegro'], ['Andante', 'Allegro']];
function StmBeatLane({ beat, n = 8 }) {
  const W = 320, gap = (W - 30) / (n - 1);
  return <svg viewBox={'0 0 ' + W + ' 30'} style={{width:'100%',maxWidth:420,display:'block',margin:'4px auto 0'}}>{Array.from({ length: n }, (_, i) => <circle key={i} cx={15 + i * gap} cy={15} r={beat === i ? 10 : 7} fill={beat === i ? PEN_C : beat > i ? PEN_N : '#fff'} stroke={PEN_N} strokeWidth="1.5"/>)}</svg>;
}
function StmWordsPad() {
  const T = usePlTimers();
  const [sel, setSel] = useState(null), [lit, setLit] = useState(-1), [beat, setBeat] = useState(-1), [quiz, setQuiz] = useState(null), [score, setScore] = useStmScore();
  function hear(w) { T.clear(); setLit(-1); setBeat(-1); const p = stmPlay(STM_ROWS.walk, STM_W(w).bpm, { click: true }); if (!p) return; stmLight(T, p, setLit, () => setBeat(-1)); p.run.at.forEach((a, i) => T.at(p.run, a, () => setBeat(i))); }
  function tap(w) { if (!quiz) { setSel(w); hear(w); return; } if (quiz.ans) return; const ok = w === quiz.w; setQuiz({ ...quiz, ans: w }); setScore(s => ({ right: s.right + (ok ? 1 : 0), tries: s.tries + 1 })); }
  function ask() { const pr = pick(STM_FAR), w = pick(pr); setSel(null); setQuiz({ pr: shuffle(pr.slice()), w, ans: null }); hear(w); }
  const list = quiz ? quiz.pr : STM_WORDS.map(x => x.w);
  const st = (w) => quiz ? (!quiz.ans ? '' : w === quiz.w ? ' good' : w === quiz.ans ? ' bad' : '') : sel === w ? ' active' : '';
  return (
    <div className="try-box" style={actBox} data-stm="words">
      <div style={actTitle}>{t('Four tempo words', '빠르기말 네 개')}</div>
      {!quiz && <div style={actNote}>{t('Tap a word to hear the tune at its tempo. Then tap Quiz.', '빠르기말을 눌러 그 빠르기로 선율을 들어 봐요. 그다음 ‘퀴즈’를 눌러요.')}</div>}
      <div style={{maxWidth:420,margin:'0 auto'}}><StmTune items={STM_ROWS.walk} o={{ lit }}/></div>
      <StmBeatLane beat={beat}/>
      {quiz && stmAsk(t('Listen. Which tempo word is it?', '들어 봐요. 어느 빠르기말일까요?'))}
      <div style={{display:'grid',gridTemplateColumns:'repeat(2,minmax(0,1fr))',gap:8,maxWidth:380,margin:'8px auto 0'}}>{list.map(w => <button key={w} className={'choice-btn' + st(w)} onClick={() => tap(w)} style={{padding:'8px 4px',display:'flex',flexDirection:'column',alignItems:'center',gap:2,minHeight:56}}>{stmWordHtml(w, 18)}{!quiz && <span style={{fontSize:12,fontWeight:800}}>{STM_W(w).short()}</span>}</button>)}</div>
      {quiz && quiz.ans && stmNote(quiz.ans === quiz.w, <>{quiz.w}: {STM_W(quiz.w).short()}.{stmScore(score)}</>)}
      {stmQuizBtns(quiz, ask, () => { T.clear(); stopClicks(); setQuiz(null); setLit(-1); setBeat(-1); }, quiz && <button className="ghost-btn" style={STM_TAP} onClick={() => hear(quiz.w)}>{STM_AGAIN()}</button>)}
    </div>
  );
}

// ── page 4: a page of music: count in and play; then find the tempo word among the other things on the page ──
// each piece keeps one tempo word everywhere (the book's two, the Workbook's and the drill's)
const STM_PIECES = [
  { en: 'Rainy Day', ko: '비 오는 날', w: 'Adagio' }, { en: 'Snow at Night', ko: '밤에 내리는 눈', w: 'Adagio' },
  { en: 'Morning Walk', ko: '아침 산책', w: 'Andante' }, { en: 'Garden Path', ko: '정원 길', w: 'Andante' },
  { en: 'Paper Boat', ko: '종이배', w: 'Moderato' }, { en: 'Clock Tower', ko: '시계탑', w: 'Moderato' },
  { en: 'Spinning Top', ko: '팽이', w: 'Allegro' }, { en: 'Kite Song', ko: '연 노래', w: 'Allegro' },
];
const stmPiece = (en) => STM_PIECES.find(p => p.en === en);
// pg: { en (the piece), dyn, mark (true: the metronome mark beside the word) }
function StmMiniPage({ pg, onTap, ans, right, exWord, maxW = 440 }) {
  const P = stmPiece(pg.en), word = P.w, ink = PEN_N, W = 340, H = 176;
  const markX = 12 + word.length * 9.8 + 12, wordR = pg.mark ? markX - 4 : 124;
  const box = { title: [92, 2, 156, 40], composer: [244, 44, 94, 40], word: [2, 44, wordR - 2, 40], mark: [markX - 4, 44, 76, 40], dyn: [66, 136, 76, 38] };
  const hit = (kind) => onTap && box[kind] ? <rect x={box[kind][0]} y={box[kind][1]} width={box[kind][2]} height={box[kind][3]} fill="transparent" style={{cursor:'pointer'}} onClick={() => onTap(kind)}/> : null;
  const col = (kind) => ans && kind === right ? BK.green : ans === kind ? BK.coral : ink;
  const ring = (kind, c) => { const b = box[kind]; return <rect x={b[0] + 2} y={b[1] + 4} width={b[2] - 4} height={b[3] - 8} rx="8" fill="none" stroke={c} strokeWidth="2.2"/>; };
  const nY = (d) => 130 - (d - 30) * 4, noteX = [112, 154, 196, 238, 290], noteD = [28, 30, 32, 30, 28];
  return <svg viewBox={'0 0 ' + W + ' ' + H} style={{width:'100%',maxWidth:maxW,display:'block',margin:'0 auto',background:'#fff',border:'1px solid rgba(38,41,107,0.18)',borderRadius:8,touchAction:'manipulation'}}>
    <text x={W / 2} y={28} textAnchor="middle" fontFamily={STM_FONT} fontWeight="800" fontSize="17" fill={col('title')}>{t(P.en, P.ko)}</text>
    <text x={W - 10} y={70} textAnchor="end" fontSize="12" fontWeight="800" fill={col('composer')}>{t('by Clara', '클라라 작곡')}</text>
    {stmWordSvg(12, 70, word, { size: 16, c: col('word') })}
    {pg.mark && <StmMark x={markX} y={70} n={STM_W(word).bpm} size={13} c={col('mark')}/>}
    {[38, 36, 34, 32, 30].map(d => <line key={d} x1={10} x2={W - 10} y1={nY(d)} y2={nY(d)} stroke={ink} strokeWidth="1"/>)}
    <ClefGlyph clef="treble" st="treble" yOf={(d) => nY(d)} ink={ink}/>
    {noteX.map((x, i) => <g key={i}><ellipse cx={x} cy={nY(noteD[i])} rx="6" ry="4.4" transform={'rotate(-20 ' + x + ' ' + nY(noteD[i]) + ')'} fill={ink}/><line x1={x + 5.4} x2={x + 5.4} y1={nY(noteD[i])} y2={nY(noteD[i]) - 28} stroke={ink} strokeWidth="1.3"/>{noteD[i] <= 28 && <line x1={x - 10} x2={x + 10} y1={nY(28)} y2={nY(28)} stroke={ink} strokeWidth="1.2"/>}</g>)}
    <text x={104} y={164} textAnchor="middle" fontFamily={SDY_FONT} fontStyle="italic" fontWeight="900" fontSize="21" fill={col('dyn')}>{pg.dyn}</text>
    {ans && ring(right, BK.green)}{ans && ans !== right && box[ans] && ring(ans, BK.coral)}{exWord && ring('word', BK.coral)}
    {['title', 'composer', 'word', 'mark', 'dyn'].filter(k => k !== 'mark' || pg.mark).map(k => <g key={k}>{hit(k)}</g>)}
  </svg>;
}
const stmNewPage = (prev) => { let pg; do { pg = { en: pick(STM_PIECES).en, dyn: pick(['p', 'mf', 'f']), mark: Math.random() < 0.5 }; } while (prev && prev.en === pg.en); return pg; };
const STM_KIND_W = { title: () => t('the title', '제목이에요'), composer: () => t('who wrote it', '작곡가 이름이에요'), mark: () => t('the metronome mark', '메트로놈 표시예요'), dyn: () => t('a dynamic', '셈여림이에요') };
function StmReadPad() {
  const T = usePlTimers();
  const [word, setWord] = useState('Andante'), [lit, setLit] = useState(-1), [beat, setBeat] = useState(-1), [quiz, setQuiz] = useState(null), [score, setScore] = useStmScore();
  function play() { T.clear(); setLit(-1); setBeat(-1); const p = stmPlay(STM_ROWS.hill, STM_W(word).bpm, { countIn: 4 }); if (!p) return; stmLight(T, p, setLit); p.run.at.slice(0, 4).forEach((a, i) => T.at(p.run, a, () => setBeat(i))); T.at(p.run, p.run.at[0] + 4 * p.run.spb, () => setBeat(-1)); }
  function ask() { T.clear(); stopClicks(); setQuiz({ pg: stmNewPage(quiz && quiz.pg), ans: null }); }
  function tap(kind) { if (!quiz || quiz.ans) return; const ok = kind === 'word'; setQuiz({ ...quiz, ans: kind }); setScore(s => ({ right: s.right + (ok ? 1 : 0), tries: s.tries + 1 })); }
  return (
    <div className="try-box" style={actBox} data-stm="read">
      <div style={actTitle}>{t('Read it, count in, play', '읽고, 미리 세고, 치기')}</div>
      {!quiz && <div style={actNote}>{t('Pick a tempo word, then tap Count in and play: four ticks, then the tune. Then tap Quiz.', '빠르기말을 고르고 ‘미리 세고 치기’를 눌러요: 똑딱 네 번, 그다음 선율. 그다음 ‘퀴즈’를 눌러요.')}</div>}
      {!quiz && <><div style={{maxWidth:420,margin:'0 auto'}}><StmTune items={STM_ROWS.hill} word={word} o={{ lit }}/></div>
        <div style={{display:'flex',justifyContent:'center',gap:10,margin:'4px 0',minHeight:26}}>{[0, 1, 2, 3].map(i => <span key={i} style={{width:26,height:26,borderRadius:13,display:'inline-flex',alignItems:'center',justifyContent:'center',fontWeight:900,fontSize:14,background:beat === i ? BK.coral : '#fff',color:beat === i ? '#fff' : BK.ink,border:'1.5px solid ' + BK.ink}}>{i + 1}</span>)}</div>
        <div style={{display:'grid',gridTemplateColumns:'repeat(2,minmax(0,1fr))',gap:6,maxWidth:320,margin:'4px auto 0'}}>{STM_WORDS.map(x => <button key={x.w} className={'chip' + (x.w === word ? ' active' : '')} onClick={() => { T.clear(); stopClicks(); setWord(x.w); }} style={{padding:'6px 12px',minHeight:44}}>{stmWordHtml(x.w, 15)}</button>)}</div></>}
      {quiz && <>{stmAsk(t('Tap the tempo word.', '빠르기말을 눌러요.'))}<StmMiniPage pg={quiz.pg} onTap={tap} ans={quiz.ans} right="word"/>
        {quiz.ans && stmNote(quiz.ans === 'word', <>{quiz.ans === 'word' ? t('The tempo word, above the staff at the start.', '빠르기말, 맨 앞 오선 위에 있어요.') : t('That is ' + STM_KIND_W[quiz.ans]() + '. The tempo word is above the staff at the start.', '그건 ' + STM_KIND_W[quiz.ans]() + '. 빠르기말은 맨 앞 오선 위에 있어요.')}{stmScore(score)}</>)}</>}
      {stmQuizBtns(quiz, ask, () => setQuiz(null), !quiz && <button className="ghost-btn" style={STM_TAP} onClick={play}>{t('▶ Count in and play', '▶ 미리 세고 치기')}</button>)}
    </div>
  );
}

// ── page 5: a metronome to set and start; then listen: 60 or 120? ──
const STM_WORD_SPAN = [['Adagio', 66, 76], ['Andante', 76, 108], ['Moderato', 108, 120], ['Allegro', 120, 168]];
const stmWordFor = (n) => { const x = STM_WORD_SPAN.find(([, a, b]) => n >= a && n < b); return x ? x[0] : null; };
function StmMetroPad() {
  const T = usePlTimers();
  const [bpm, setBpm] = useState(90), [on, setOn] = useState(false), [muted, setMuted] = useState(false), [ang, setAng] = useState(0), [quiz, setQuiz] = useState(null), [score, setScore] = useStmScore();
  const R = useRef(null);
  useEffect(() => () => { if (R.current) cancelAnimationFrame(R.current.raf); }, []);
  function stop() { T.clear(); stopClicks(); if (R.current) cancelAnimationFrame(R.current.raf); R.current = null; setOn(false); setAng(0); }
  const ticks = (r, from) => { for (let i = Math.max(0, from); i < r.beats; i++) metroClick(r.ctx, r.t0 + i * r.spb, false, 0.32); };
  function go(n, beats = 240, silent = false) {
    stop(); const ctx = getAudio(); if (!ctx) return;
    const r = { ctx, spb: 60 / n, t0: ctx.currentTime + 0.18, lat: outLatency(ctx), beats, raf: 0 }; R.current = r; setOn(true);
    if (!silent) ticks(r, 0);
    const frame = () => { const tt = (ctx.currentTime - r.t0 - r.lat) / r.spb; setAng(tt < 0 ? -22 : 22 * Math.cos(Math.PI * (tt + 1))); if (tt < beats) r.raf = requestAnimationFrame(frame); else stop(); };
    r.raf = requestAnimationFrame(frame);
  }
  function sound() { const r = R.current, m = !muted; setMuted(m); if (!r) return; stopClicks(); if (!m) ticks(r, Math.ceil((r.ctx.currentTime + 0.05 - r.t0) / r.spb)); }
  function set(n) { const v = Math.max(40, Math.min(208, n)); setBpm(v); if (on) go(v, 240, muted); }
  function ask() { stop(); setMuted(false); const n = pick([60, 120]); setQuiz({ n, ans: null }); go(n, 8); }
  function answer(n) { if (!quiz || quiz.ans) return; setQuiz({ ...quiz, ans: n }); setScore(s => ({ right: s.right + (n === quiz.n ? 1 : 0), tries: s.tries + 1 })); }
  const w = stmWordFor(bpm);
  return (
    <div className="try-box" style={actBox} data-stm="metro">
      <div style={actTitle}>{t('The metronome', '메트로놈')}</div>
      {!quiz && <div style={actNote}>{t('Set a number and tap Start. Sound off keeps the beat going in silence. Then tap Quiz.', '숫자를 맞추고 ‘시작’을 눌러요. ‘소리 끄기’를 누르면 소리 없이 박이 계속돼요. 그다음 ‘퀴즈’를 눌러요.')}</div>}
      <div style={{display:'flex',flexDirection:'column',alignItems:'center',gap:8,maxWidth:440,margin:'0 auto'}}>
        <div style={{display:'flex',alignItems:'center',justifyContent:'center',gap:14,width:'100%'}}>
          <svg viewBox="0 0 160 200" style={{width:'42%',maxWidth:160,display:'block'}}><StmMetronome x={80} y={186} h={170} swing={ang} wt={quiz ? 0.5 : stmWt(bpm)}/></svg>
          {!quiz ? <div style={{display:'flex',flexDirection:'column',alignItems:'center',gap:6}}><div style={{fontSize:28,color:BK.ink}}>{stmMm(bpm)}</div><div style={{minHeight:22,fontSize:15,color:BK.coral,textAlign:'center'}}>{w ? (LANG === 'ko' ? <>{stmWordHtml(w, 17)}쯤</> : <>about {stmWordHtml(w, 17)}</>) : ''}</div></div>
            : <div style={{display:'flex',flexDirection:'column',alignItems:'center',gap:8}}>{stmAsk(t('Listen. Which mark is it?', '들어 봐요. 어느 표시일까요?'))}
              {[60, 120].map(n => <button key={n} className={'choice-btn' + (!quiz.ans ? '' : n === quiz.n ? ' good' : n === quiz.ans ? ' bad' : '')} style={{padding:'10px 16px',fontSize:20,minWidth:120}} onClick={() => answer(n)}>{stmMm(n)}</button>)}</div>}
        </div>
        {!quiz && <><div style={{display:'flex',gap:6,justifyContent:'center'}}>{[-10, -1, 1, 10].map(d => <button key={d} className="ghost-btn" style={{...STM_TAP,minWidth:52,padding:'0 6px'}} onClick={() => set(bpm + d)}>{d > 0 ? '+' + d : '−' + (-d)}</button>)}</div>
          <div style={{display:'flex',gap:6,justifyContent:'center'}}>{[60, 90, 120].map(n => <button key={n} className={'chip' + (n === bpm ? ' active' : '')} style={{minHeight:44,padding:'4px 14px'}} onClick={() => set(n)}>{n}</button>)}</div>
          <div style={{display:'flex',gap:6,justifyContent:'center'}}><button className="ghost-btn" style={{...STM_TAP,minWidth:120,fontWeight:900}} onClick={() => on ? stop() : go(bpm, 240, muted)}>{on ? t('■ Stop', '■ 멈춤') : t('▶ Start', '▶ 시작')}</button>
            <button className={'chip' + (muted ? ' active' : '')} style={{minHeight:44,padding:'4px 14px'}} onClick={sound}>{muted ? t('Sound on', '소리 켜기') : t('Sound off', '소리 끄기')}</button></div></>}
      </div>
      {quiz && quiz.ans && stmNote(quiz.ans === quiz.n, <>{stmMm(quiz.n)}{quiz.n === 60 ? t(': one beat a second.', ': 1초에 한 박.') : t(': two beats a second.', ': 1초에 두 박.')}{stmScore(score)}</>)}
      {stmQuizBtns(quiz, ask, () => { stop(); setQuiz(null); }, quiz && <button className="ghost-btn" style={STM_TAP} onClick={() => go(quiz.n, 8)}>{STM_AGAIN()}</button>)}
    </div>
  );
}

// ── page 6: tap with the metronome, then keep going when it stops; then listen: steady, rushing or dragging? ──
const STM_STEADY_BPM = 90, STM_N = 8;
function StmSteadyPad() {
  const T = usePlTimers();
  const [phase, setPhase] = useState('idle'), [taps, setTaps] = useState([]), [res, setRes] = useState(null), [lit, setLit] = useState(-1), [quiz, setQuiz] = useState(null), [score, setScore] = useStmScore();
  const R = useRef(null), P = useRef('idle');
  const setP = (p) => { P.current = p; setPhase(p); };
  function finish() {
    const r = R.current; if (!r || P.current === 'done') return; T.clear();
    const from = r.run.at[STM_N - 1] + r.run.spb * 0.5, alone = r.taps.filter(x => x > from);
    if (alone.length < 4) { setRes({ kind: 'few' }); setP('done'); return; }
    const iv = alone.slice(1).map((x, i) => x - alone[i]), ratio = iv.reduce((a, b) => a + b, 0) / iv.length / r.run.spb;
    setRes({ kind: ratio < 0.93 ? 'rush' : ratio > 1.07 ? 'drag' : 'steady', ratio, alone, from }); setP('done');
  }
  function start() {
    T.clear(); setRes(null); setTaps([]); setLit(-1);
    const run = plRun(STM_N, { bpm: STM_STEADY_BPM, noVoice: true, vol: 0.34 }); if (!run) return;
    R.current = { run, taps: [] }; setP('with');
    run.at.forEach((a, i) => T.at(run, a, () => setLit(i)));
    T.at(run, run.at[STM_N - 1] + run.spb * 0.5, () => { setP('alone'); setLit(-1); });
    T.at(run, run.at[STM_N - 1] + run.spb * (STM_N + 3), finish);
  }
  const tap = React.useCallback(() => { const r = R.current; if (!r || (P.current !== 'with' && P.current !== 'alone')) return; const now = r.run.now(); r.taps.push(now); setTaps(r.taps.slice());
    if (P.current === 'alone' && r.taps.filter(x => x > r.run.at[STM_N - 1] + r.run.spb * 0.5).length >= STM_N) finish(); }, []);
  function ask() { T.clear(); stopClicks(); setP('idle'); setRes(null); const k = pick(['steady', 'rush', 'drag']); setQuiz({ k, ans: null }); stmFeel(k); }
  function answer(k) { if (!quiz || quiz.ans) return; setQuiz({ ...quiz, ans: k }); setScore(s => ({ right: s.right + (k === quiz.k ? 1 : 0), tries: s.tries + 1 })); }
  const strip = () => { if (!res || !res.alone) return null; const spb = R.current.run.spb, x0 = res.alone[0], W = 320, s = (W - 30) / Math.max(spb * (STM_N - 1), res.alone[res.alone.length - 1] - x0);
    return <svg viewBox={'0 0 ' + W + ' 46'} style={{width:'100%',maxWidth:420,display:'block',margin:'6px auto 0'}}>
      {Array.from({ length: STM_N }, (_, i) => <line key={i} x1={15 + i * spb * s} x2={15 + i * spb * s} y1={6} y2={40} stroke="rgba(38,41,107,0.35)" strokeWidth="1.2" strokeDasharray="3 3"/>)}
      {res.alone.map((x, i) => { const cx = 15 + (x - x0) * s; return <circle key={i} cx={cx} cy={23} r="7" fill={res.kind === 'steady' ? PEN_N : PEN_C}/>; })}</svg>; };
  const verdict = res && (res.kind === 'few' ? t('Keep tapping after the ticks stop: eight more taps.', '똑딱 소리가 멈춘 뒤에도 여덟 번 더 쳐요.') : res.kind === 'steady' ? t('Steady! You kept the tempo.', '꾸준해요! 빠르기를 지켰어요.') : res.kind === 'rush' ? t('You rushed: your taps got faster. Try again.', '서둘렀어요: 점점 빨라졌어요. 다시 해 봐요.') : t('You dragged: your taps got slower. Try again.', '처졌어요: 점점 느려졌어요. 다시 해 봐요.'));
  return (
    <div className="try-box" style={actBox} data-stm="steady">
      <div style={actTitle}>{t('Keep the tempo', '빠르기 지키기')}</div>
      {!quiz && <div style={actNote}>{t('Tap Start. Tap with the 8 ticks, then 8 more on your own. Then tap Quiz.', '‘시작’을 누르고 똑딱 소리 여덟 번에 맞춰 쳐요. 소리가 멈추면 혼자 여덟 번 더. 그다음 ‘퀴즈’를 눌러요.')}</div>}
      {!quiz && <><div style={{display:'flex',justifyContent:'center',gap:6,margin:'2px 0 8px'}}>{Array.from({ length: STM_N }, (_, i) => <span key={i} style={{width:22,height:22,borderRadius:11,background:lit === i ? BK.coral : lit > i ? BK.ink : '#fff',border:'1.5px solid ' + BK.ink}}/>)}</div>
        <div style={{maxWidth:360,margin:'0 auto'}}><PlPad on={phase === 'with' || phase === 'alone'} onTap={tap} label={phase === 'with' ? t('Tap with the ticks', '똑딱 소리에 맞춰 쳐요') : phase === 'alone' ? t('Keep going!', '계속!') : t('Tap here', '여기를 쳐요')} h={70}/></div>
        {res && <div style={{textAlign:'center',fontSize:14.5,fontWeight:900,marginTop:6,color:res.kind === 'steady' ? BK.green : BK.coral,wordBreak:'keep-all'}}>{verdict}</div>}{strip()}</>}
      {quiz && <>{stmAsk(<>{t('Listen to eight ticks.', '똑딱 소리 여덟 번을 들어요.')}<br/>{t('Steady, rushing or dragging?', '꾸준하게? 서두르기? 처지기?')}</>)}
        <div style={{display:'grid',gridTemplateColumns:'repeat(3,minmax(0,1fr))',gap:8,maxWidth:380,margin:'6px auto 0'}}>{['steady', 'rush', 'drag'].map(k => <button key={k} className={'choice-btn' + (!quiz.ans ? '' : k === quiz.k ? ' good' : k === quiz.ans ? ' bad' : '')} onClick={() => answer(k)} style={{padding:'12px 0',fontSize:15,fontWeight:900}}>{STM_FEEL_W[k]()}</button>)}</div>
        {quiz.ans && stmNote(quiz.ans === quiz.k, <>{quiz.k === 'steady' ? t('The same gap every time.', '매번 똑같은 간격.') : quiz.k === 'rush' ? t('The ticks got closer and closer.', '똑딱 소리가 점점 가까워졌어요.') : t('The ticks got further and further apart.', '똑딱 소리가 점점 멀어졌어요.')}{stmScore(score)}</>)}</>}
      {stmQuizBtns(quiz, ask, () => { T.clear(); stopClicks(); setQuiz(null); }, quiz ? <button className="ghost-btn" style={STM_TAP} onClick={() => stmFeel(quiz.k)}>{STM_AGAIN()}</button> : <button className="ghost-btn" style={STM_TAP} onClick={start}>{phase === 'idle' ? t('▶ Start', '▶ 시작') : t('▶ Again', '▶ 다시')}</button>)}
      {!quiz && plHint()}
    </div>
  );
}
function StmPad({ page }) { return page === 2 ? <StmSlowFastPad/> : page === 3 ? <StmWordsPad/> : page === 4 ? <StmReadPad/> : page === 5 ? <StmMetroPad/> : <StmSteadyPad/>; }

// ── the book on screen. Old ticks kept where the idea is the same: 'What is tempo?' (0), 'Slow to fast' (1), 'The
// metronome' (5); reading the tempo and a steady tempo are new (6, 7); the checks 8 ──
const STM_STORE = [0, 1, 6, 5, 7, 8];
function StmLearn({ onStart }) {
  const pages = stmLbPages(true);
  const opener = pages[0];
  return (
    <Lesson id="tempo" title={bkChapterName('tempo')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="tempo"><div className="lb-screen lb-open" style={{display:'flex',flexDirection:'column',gap:12,margin:'0 0 8px'}}>{lbWordsFirst(opener.props.children)}</div></BkChapterCtx.Provider></LbScreenCtx.Provider>}>
      {pages.slice(1).map((pg, i) => (
        <Step key={i} storeAs={STM_STORE[i]} title={pg.props.title}>
          <LbScreenPage page={pg}/>
        </Step>
      ))}
    </Lesson>
  );
}

// ── the drill, in the book's order: page 2 (1), page 3 (2 to 5), page 4 (6), page 5 (7), page 6 (8); 9 the extra ──
const STM_EXTRA = [
  { w: 'rit.', en: 'getting slower', ko: '점점 느리게' },
  { w: 'accel.', en: 'getting faster', ko: '점점 빠르게' },
  { w: 'a tempo', en: 'back to the speed before', ko: '본디 빠르기로' },
  { w: 'Presto', en: 'very fast', ko: '매우 빠르게' },
];
const STM_LEVELS = [
  { n: 1, label: 'Listen: slow or fast?', kind: 'earSF', time: 10, noPrint: true },
  { n: 2, label: 'Word meanings', kind: 'meaning', time: 8 },
  { n: 3, label: 'Faster word', kind: 'faster', time: 6 },
  { n: 4, label: 'Slow to fast', kind: 'order', time: 15 },
  { n: 5, label: 'Listen: tempo words', kind: 'earWord', time: 12, noPrint: true },
  { n: 6, label: 'Find the tempo word', kind: 'where', time: 8 },
  { n: 7, label: 'Metronome marks', kind: 'mark', time: 8 },
  { n: 8, label: 'Listen: steady, rushing or dragging?', kind: 'earSteady', time: 12, noPrint: true },
  { n: 9, label: 'Extra: rit., accel., a tempo, Presto', kind: 'extra', time: 8 },
];
Object.assign(LEVEL_KO, {
  'Listen: slow or fast?': '듣기: 느리게? 빠르게?', 'Word meanings': '빠르기말 뜻', 'Faster word': '더 빠른 빠르기말', 'Slow to fast': '느린 것부터 빠른 것까지',
  'Listen: tempo words': '듣기: 빠르기말', 'Find the tempo word': '빠르기말 찾기', 'Metronome marks': '메트로놈 표시',
  'Listen: steady, rushing or dragging?': '듣기: 꾸준하게? 서두르기? 처지기?', 'Extra: rit., accel., a tempo, Presto': '더 해 보기: rit., accel., a tempo, Presto',
});
const STM_MARKS = [60, 66, 72, 80, 88, 96, 104, 112, 120, 132, 144, 160];
const STM_RANK = (w) => STM_WORDS.findIndex(x => x.w === w);
function genStmQuestion(lv, prev) {
  const uid = Math.random(), pk = prev && prev.key;
  const again = (f) => { for (let g = 0; g < 20; g++) { const q = f(); if (q.key !== pk) return { ...q, uid }; } return { ...f(), uid }; };
  const words = STM_WORDS.map(x => x.w);
  if (lv.kind === 'meaning') return again(() => { const w = pick(words); return { kind: 'meaning', w, key: w, answer: w, choices: shuffle(words.slice()) }; });
  if (lv.kind === 'faster') return again(() => { const pr = sampleN(words, 2); return { kind: 'faster', pr, key: pr.slice().sort().join(), answer: STM_RANK(pr[0]) > STM_RANK(pr[1]) ? pr[0] : pr[1], choices: pr }; });
  if (lv.kind === 'order') return again(() => { let sh; do { sh = shuffle(words.slice()); } while (sh.join() === words.join()); return { kind: 'order', items: sh, key: sh.join(), answer: words.join() }; });
  if (lv.kind === 'mark') return again(() => { const r = Math.random();
    if (r < 0.5) { let a, b; do { [a, b] = sampleN(STM_MARKS, 2); } while (Math.abs(a - b) < 20); return { kind: 'mark', sub: 'faster', pr: [a, b], key: a + '-' + b, answer: String(Math.max(a, b)), choices: [String(a), String(b)] }; }
    if (r < 0.75) { const n = pick([60, 72, 90, 120]); return { kind: 'mark', sub: 'min', n, key: 'm' + n, answer: 'minute', choices: shuffle(['minute', 'second']) }; }
    const n = pick([60, 120]); return { kind: 'mark', sub: 'sec', n, key: 's' + n, answer: String(n / 60), choices: ['1', '2'] }; });
  if (lv.kind === 'where') return again(() => { const pg = stmNewPage(prev && prev.pg); return { kind: 'where', pg, key: pg.en + pg.dyn, answer: 'word' }; });
  if (lv.kind === 'earSF') return again(() => { const k = pick(['slow', 'fast']), items = pick([STM_ROWS.walk, STM_ROWS.hill, STM_ROWS.steps]); return { kind: 'earSF', k, items, key: k + Math.random(), answer: k, choices: ['slow', 'fast'] }; });
  if (lv.kind === 'earWord') return again(() => { const pr = pick(STM_FAR), w = pick(pr); return { kind: 'earWord', w, key: w + pr.join(), answer: w, choices: shuffle(pr.slice()) }; });
  if (lv.kind === 'earSteady') return again(() => { const k = pick(['steady', 'rush', 'drag']); return { kind: 'earSteady', k, key: k + Math.random(), answer: k, choices: ['steady', 'rush', 'drag'] }; });
  return again(() => { const x = pick(STM_EXTRA); return { kind: 'extra', w: x.w, key: x.w, answer: x.w, choices: shuffle(STM_EXTRA.map(e => e.w)) }; });
}
const stmExtraMean = (w) => { const x = STM_EXTRA.find(e => e.w === w); return t(x.en, x.ko); };
const STM_UNIT = { minute: () => t('in a minute', '1분 동안'), second: () => t('in a second', '1초 동안') };
function StmQuestion(props) {
  const { q, given, locked, onAnswer, pixel, stats } = props;
  const [seq, setSeq] = useState([]);
  useEffect(() => { setSeq([]); }, [q.uid]);
  const hear = () => { if (q.kind === 'earSF') stmPlay(q.items, STM_SF_BPM[q.k], { click: true }); else if (q.kind === 'earWord') stmPlay(STM_ROWS.walk, STM_W(q.w).bpm, { click: true }); else if (q.kind === 'earSteady') stmFeel(q.k); };
  useEffect(() => { if (q.kind && q.kind.startsWith('ear')) { const tm = setTimeout(hear, 250); return () => { clearTimeout(tm); stopClicks(); }; } return undefined; }, [q.uid]);
  const done = !!given;
  const btnCls = pixel ? 'pixel-choice' : 'choice-btn';
  const st = (c) => !done ? '' : c === q.answer ? ' good' : (given.ans === c ? ' bad' : '');
  const prompt = (txt) => <p style={pixel ? {fontSize:11.5,textAlign:'center',margin:'0 0 10px',lineHeight:1.7} : {fontSize:15,fontWeight:700,textAlign:'center',margin:'0 0 10px',color:'var(--muted)',textWrap:'balance',wordBreak:'keep-all'}}>{txt}</p>;
  const big = (s) => <div style={{textAlign:'center',margin:'2px 0 14px',color:pixel ? 'var(--brass)' : BK.ink}}>{stmWordHtml(s, pixel ? 22 : 40)}</div>;
  const track = <RaceTrack steps={pixel ? 15 : LESSON_TOTAL} pos={stats ? stats.correct : 0} pixel={pixel}/>;
  const grid = (cols, render, pad = '14px 4px') => <div style={{display:'grid',gridTemplateColumns:'repeat(' + cols + ',minmax(0,1fr))',gap:8}}>{q.choices.map(c => <button key={c} disabled={locked} onClick={() => { if (q.kind.startsWith('ear')) stopClicks(); onAnswer(c); }} className={btnCls + st(c)} style={{padding:pad,textWrap:'balance'}}>{render(c)}</button>)}</div>;
  const word = (s, sz = 16) => <span style={{fontSize:pixel ? 11 : sz,fontWeight:900}}>{s}</span>;
  const again = <div style={{textAlign:'center',margin:'0 0 12px'}}><button className={pixel ? 'pixel-btn' : 'ghost-btn'} onClick={hear} style={pixel ? {fontSize:9} : {fontSize:15,padding:'8px 16px',minHeight:44}}>{STM_AGAIN()}</button></div>;
  let body;
  if (q.kind === 'meaning') body = <>{prompt(t('What does it mean?', '무슨 뜻일까요?'))}{big(q.w)}{grid(2, c => word(STM_W(c).short(), 15), '12px 4px')}</>;
  else if (q.kind === 'faster') body = <>{prompt(t('Which one is faster?', '어느 쪽이 더 빠를까요?'))}{grid(2, c => stmWordHtml(c, pixel ? 12 : 20), '22px 4px')}</>;
  else if (q.kind === 'order') {
    const right = STM_WORDS.map(x => x.w);
    const tapW = (w) => { if (locked || done || seq.includes(w)) return; const next = [...seq, w]; setSeq(next); if (next.length === 4) onAnswer(next.join()); };
    body = <>{prompt(t('Tap them from the slowest to the fastest.', '가장 느린 것부터 가장 빠른 것까지 눌러요.'))}
      <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:8}}>{q.items.map(w => { const idx = seq.indexOf(w), stt = done ? (right.indexOf(w) === idx ? ' good' : ' bad') : '';
        return <button key={w} disabled={locked || idx >= 0} onClick={() => tapW(w)} className={btnCls + stt} style={{padding:'14px 6px',opacity:!done && idx >= 0 ? 0.55 : 1}}>{idx >= 0 ? (idx + 1) + '. ' : ''}{stmWordHtml(w, pixel ? 12 : 18)}</button>; })}</div>
      {!done && seq.length > 0 && <div style={{textAlign:'center',marginTop:10}}><button className={pixel ? 'pixel-btn' : 'ghost-btn'} style={pixel ? {fontSize:8,padding:'8px 10px'} : STM_TAP} onClick={() => setSeq(seq.slice(0, -1))}>{t('Undo', '되돌리기')}</button></div>}</>;
  }
  else if (q.kind === 'mark') {
    if (q.sub === 'faster') body = <>{prompt(t('Which metronome mark is faster?', '어느 메트로놈 표시가 더 빠를까요?'))}{grid(2, c => <span style={{fontSize:pixel ? 13 : 22}}>{stmMm(c)}</span>, '18px 4px')}</>;
    else if (q.sub === 'min') body = <>{prompt(<>{stmMm(q.n)}{t(' means ' + q.n + ' beats…', ': 얼마 동안 ' + q.n + '박일까요?')}</>)}{grid(2, c => word(STM_UNIT[c](), 17), '18px 4px')}</>;
    else body = <>{prompt(<>{stmMm(q.n)}{t(': how many beats in one second?', ': 1초에 몇 박일까요?')}</>)}{grid(2, c => word(c, 22), '18px 4px')}</>;
  }
  else if (q.kind === 'where') { const ans = done ? given.ans : null;
    body = <>{prompt(t('Tap the tempo word.', '빠르기말을 눌러요.'))}<div style={{background:pixel ? '#faf6ec' : 'transparent',borderRadius:8,padding:pixel ? 6 : 0,margin:'0 auto 10px'}}><StmMiniPage pg={q.pg} onTap={locked || done ? null : (k) => onAnswer(k)} ans={ans} right="word"/></div></>; }
  else if (q.kind === 'earSF') body = <>{prompt(t('Listen. Slow or fast?', '들어 봐요. 느리게? 빠르게?'))}{again}{grid(2, c => word(STM_SF[c]()))}</>;
  else if (q.kind === 'earWord') body = <>{prompt(t('Listen. Which tempo word is it?', '들어 봐요. 어느 빠르기말일까요?'))}{again}{grid(2, c => stmWordHtml(c, pixel ? 12 : 20), '18px 4px')}</>;
  else if (q.kind === 'earSteady') body = <>{prompt(<>{t('Listen to eight ticks.', '똑딱 소리 여덟 번을 들어요.')}<br/>{t('Steady, rushing or dragging?', '꾸준하게? 서두르기? 처지기?')}</>)}{again}{grid(3, c => word(STM_FEEL_W[c](), 15), '14px 2px')}</>;
  else body = <>{prompt(t('What does it mean?', '무슨 뜻일까요?'))}{big(q.w)}{grid(2, c => word(stmExtraMean(c), 15), '12px 4px')}</>;
  return <div>{track}{body}</div>;
}
function stmCheck(q, ans) { return ans !== null && ans !== undefined && String(ans) === String(q.answer); }
function stmAnswerLabel(q) {
  if (q.kind === 'meaning') return q.w + ': ' + STM_W(q.w).short();
  if (q.kind === 'faster') return q.answer + ' (' + STM_W(q.answer).short() + ')';
  if (q.kind === 'order') return STM_WORDS.map(x => x.w).join(' → ');
  if (q.kind === 'mark') return q.sub === 'faster' ? t(q.answer + ' beats a minute', '1분에 ' + q.answer + '박') : q.sub === 'min' ? t(q.n + ' beats in a minute', '1분에 ' + q.n + '박') : t(q.answer === '1' ? '1 beat a second' : q.answer + ' beats a second', '1초에 ' + q.answer + '박');
  if (q.kind === 'where') return t('the tempo word, ' + stmPiece(q.pg.en).w + ', above the staff at the start', '빠르기말 ' + stmPiece(q.pg.en).w + ', 맨 앞 오선 위');
  if (q.kind === 'earSF') return STM_SF[q.answer]();
  if (q.kind === 'earWord') return q.answer + ' (' + STM_W(q.answer).short() + ')';
  if (q.kind === 'earSteady') return STM_FEEL_W[q.answer]();
  return q.w + ': ' + stmExtraMean(q.w);
}
Object.assign(TEMPO_DRILL, { levels: STM_LEVELS, generate: genStmQuestion, check: stmCheck, answerLabel: stmAnswerLabel, Question: StmQuestion, Learn: StmLearn });
