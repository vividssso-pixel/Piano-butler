// ─── Phase 473: chapter 18 on screen (what moves on pages 2 to 6), the book as the online lesson, and the drill ───
// Sounds: instNote's harpsichord, clavichord and piano (its loudness follows how hard the key is pressed). One sound at a
// time across the pads: each pad hands SPS_STOP its own stop function while it sounds; a new sound stops the last one.
const SPS_INST = ['harpsichord', 'clavichord', 'piano'];
const SPS_IW = { harpsichord: () => t('harpsichord', '하프시코드'), clavichord: () => t('clavichord', '클라비코드'), piano: () => t('piano', '피아노') };
const SPS_HOW = { harpsichord: 'pluck', clavichord: 'press', piano: 'strike' };
const SPS_PART_OF = { harpsichord: 'quill', clavichord: 'tangent', piano: 'hammer' };
const SPS_MOVER_W = { quill: () => t('a quill', '깃촉'), tangent: () => t('a tangent', '탄젠트'), hammer: () => t('a hammer', '해머') };
const SPS_MOVES = { harpsichord: () => t('a quill plucks the string', '깃촉이 현을 뜯어요'), clavichord: () => t('a tangent pushes up against the string and stays', '탄젠트가 현을 밀어 올린 채 머물러요'), piano: () => t('a hammer strikes the string', '해머가 현을 쳐요') };
const SPS_TUNE = [60, 62, 64, 65, 67];
const SPS_STOP = { fn: null };
const spsCap = (s) => typeof s === 'string' && LANG !== 'ko' ? s.charAt(0).toUpperCase() + s.slice(1) : s;
const spsNote = (ok, txt) => <div style={{textAlign:'center',fontSize:14,fontWeight:900,marginTop:6,color:ok ? BK.green : BK.coral,textWrap:'balance',wordBreak:'keep-all'}}>{ok ? t('Yes! ', '맞아요! ') : t('Not quite. ', '아쉬워요. ')}{txt}</div>;
const SPS_TAP = { minHeight: 44 };
const spsRow = (kids) => <div style={{display:'flex',gap:6,justifyContent:'center',marginTop:8,flexWrap:'wrap'}}>{kids}</div>;
const spsScore = (s) => s.tries ? <span style={{color:BK.muted,fontWeight:800,whiteSpace:'nowrap'}}>{'  ·  ' + t(s.right + ' of ' + s.tries, s.tries + '개 중 ' + s.right + '개')}</span> : null;
// stop whatever is sounding (the pad that owns SPS_STOP resets itself), then hand SPS_STOP to `me` (or to nobody)
function spsTake(me) { const f = SPS_STOP.fn; SPS_STOP.fn = null; if (f && f !== me) { try { f(); } catch (e) {} } stopClicks(); SPS_STOP.fn = me || null; }
const spsRelease = (me) => { if (SPS_STOP.fn === me) SPS_STOP.fn = null; };
// a pad's sound: stop the last, play, own SPS_STOP until stopped or unmounted
function useSpsSound(reset) {
  const T = useRef([]), resetRef = useRef(reset); resetRef.current = reset;
  const me = useRef(() => { T.current.forEach(clearTimeout); T.current = []; stopClicks(); if (resetRef.current) resetRef.current(); }).current;
  useEffect(() => () => { T.current.forEach(clearTimeout); if (SPS_STOP.fn === me) { SPS_STOP.fn = null; stopClicks(); } }, []);
  const play = (fn) => { spsTake(me); T.current.forEach(clearTimeout); T.current = []; const len = fn(); if (len) T.current.push(setTimeout(() => spsRelease(me), len * 1000 + 600)); return len; };
  return { me, T, play, tune: (inst, notes, vel = 0.5, bpm = 120, nlen = 0.9) => play(() => playEvents(inst, notes.map((m, i) => [i, m, nlen, vel]), bpm)) };
}
const spsQuizBtns = (quiz, onNext, onBack, extra) => spsRow(<>{extra}<button className="ghost-btn" style={SPS_TAP} onClick={onNext}>{quiz ? t('Next →', '다음 →') : t('Quiz', '퀴즈')}</button>{quiz && <button className="ghost-btn" style={SPS_TAP} onClick={onBack}>{t('← Back', '← 돌아가기')}</button>}</>);
const spsChoice = (cls, label, onClick, key) => <button key={key} className={'choice-btn' + cls} onClick={onClick} style={{padding:'11px 6px',fontSize:15,fontWeight:900,minHeight:44,wordBreak:'keep-all'}}>{label}</button>;
const spsGrid = (min, kids) => <div style={{display:'grid',gridTemplateColumns:'repeat(auto-fit,minmax(' + min + 'px,1fr))',gap:6,marginTop:6}}>{kids}</div>;
// answer a pad quiz once (a ref, so two taps in one moment count once)
function useSpsQuiz() { const [quiz, setQuizS] = useState(null), done = useRef(false), [score, setScore] = useState({ right: 0, tries: 0 });
  const setQuiz = (q) => { done.current = !!(q && q.ans != null); setQuizS(q); };
  const answer = (v, ok) => { if (!quiz || done.current) return false; done.current = true; setQuizS({ ...quiz, ans: v }); setScore(s => ({ right: s.right + (ok ? 1 : 0), tries: s.tries + 1 })); return true; };
  return { quiz, setQuiz, score, answer }; }
function spsInstPicture(i, maxW = 260) {
  return <svg viewBox={i === 'clavichord' ? '0 0 204 116' : '0 0 204 116'} style={{width:'100%',maxWidth:maxW,display:'block',margin:'0 auto'}}>{i === 'harpsichord' ? <SpsHarpsichord x={2} y={0}/> : i === 'clavichord' ? <SpsClavichord x={2} y={0}/> : <SpsGrand x={2} y={0}/>}</svg>;
}

// ── page 2: three keyboards: see it, press gently or hard and hear; then a quiz: which one was it? ──
function SpsSoundPad() {
  const [inst, setInst] = useState('harpsichord'), [lv, setLv] = useState(null), { quiz, setQuiz, score, answer } = useSpsQuiz();
  const S = useSpsSound(() => setLv(null));
  const meter = (i, v) => i === 'harpsichord' ? 0.6 : i === 'clavichord' ? 0.08 + 0.18 * v : 0.12 + 0.86 * v;
  function press(v) { setLv(v); S.tune(inst, [67], v, 60, 1.4); }
  function hear(i) { S.tune(i, SPS_TUNE, 0.55); }
  function ask() { const i = pick(SPS_INST.filter(x => !quiz || x !== quiz.i || Math.random() < 0.3)); setQuiz({ i, ans: null }); hear(i); }
  const st = (i) => !quiz || quiz.ans == null ? '' : i === quiz.i ? ' good' : i === quiz.ans ? ' bad' : '';
  return (
    <div className="try-box" style={actBox} data-sps="sound">
      <div style={actTitle}>{t('Pluck, push or strike', '뜯기, 밀기, 치기')}</div>
      <div style={actNote}>{quiz ? t('Listen to the tune: which keyboard plays it?', '선율을 들어 봐요: 어느 건반 악기일까요?') : t('Pick a keyboard. Press gently, then hard: does it get louder?', '건반 악기를 골라요. 살살, 그다음 세게 눌러 봐요: 소리가 커지나요?')}</div>
      {!quiz && <>
        {spsGrid(104, SPS_INST.map(i => <button key={i} className={'chip' + (i === inst ? ' active' : '')} style={{padding:'8px 4px',fontSize:15,minHeight:44,wordBreak:'keep-all'}} onClick={() => { setInst(i); setLv(null); }}>{SPS_IW[i]()}</button>))}
        <div style={{margin:'8px auto 0',maxWidth:300}}>{spsInstPicture(inst)}</div>
        <svg viewBox="0 0 130 100" style={{width:'100%',maxWidth:240,display:'block',margin:'4px auto 0'}}><SpsMech kind={SPS_HOW[inst]}/></svg>
        <div style={{textAlign:'center',fontSize:16,fontWeight:900,color:PEN_C,margin:'2px 0 4px',wordBreak:'keep-all'}}>{spsCap(SPS_MOVES[inst]())}</div>
        <div style={{display:'grid',gridTemplateColumns:'auto 1fr',gap:'4px 10px',alignItems:'center',maxWidth:320,margin:'4px auto 0',fontSize:14,fontWeight:800}}>
          <span>{t('Sound', '소리')}</span><div style={{height:12,borderRadius:6,background:'#fff',border:'1px solid rgba(38,41,107,0.3)',overflow:'hidden'}}><div style={{width:(lv == null ? 0 : meter(inst, lv) * 100) + '%',height:'100%',background:PEN_C,transition:'width 0.2s'}}/></div>
        </div>
        {spsRow(<><button className="ghost-btn" style={SPS_TAP} onClick={() => press(0.15)}>{t('▶ Gently', '▶ 살살')}</button><button className="ghost-btn" style={SPS_TAP} onClick={() => press(0.95)}>{t('▶ Hard', '▶ 세게')}</button></>)}
      </>}
      {quiz && spsGrid(104, SPS_INST.map(i => spsChoice(st(i), SPS_IW[i](), () => answer(i, i === quiz.i), i)))}
      {quiz && quiz.ans != null && spsNote(quiz.ans === quiz.i, <>{spsCap(SPS_IW[quiz.i]())}{t(': ', '는 ')}{SPS_MOVES[quiz.i]()}.{spsScore(score)}</>)}
      {spsQuizBtns(quiz, ask, () => { S.me(); spsRelease(S.me); setQuiz(null); }, quiz && <button className="ghost-btn" style={SPS_TAP} onClick={() => hear(quiz.i)}>{t('▶ Hear again', '▶ 다시 듣기')}</button>)}
    </div>
  );
}

// ── page 3: the timeline; piano and forte: the tune soft, loud, or getting louder; on the harpsichord it never changes;
// quiz: which C was forte? ──
function SpsSoftLoudPad() {
  const [inst, setInst] = useState('piano'), { quiz, setQuiz, score, answer } = useSpsQuiz();
  const S = useSpsSound();
  function play(kind) { if (kind === 'cresc') S.play(() => playEvents(inst, SPS_TUNE.map((m, i) => [i, m, 0.9, 0.12 + i * 0.2]), 120)); else S.tune(inst, SPS_TUNE, kind === 'p' ? 0.15 : 0.95); }
  function hear(q) { S.play(() => playEvents('piano', [[0, 60, 1.2, q.loud === 0 ? 0.95 : 0.15], [2, 60, 1.2, q.loud === 1 ? 0.95 : 0.15]], 100)); }
  function ask() { const q = { loud: pick([0, 1]), ans: null }; setQuiz(q); hear(q); }
  const st = (k) => !quiz || quiz.ans == null ? '' : k === quiz.loud ? ' good' : k === quiz.ans ? ' bad' : '';
  const W = [t('the first', '첫 번째'), t('the second', '두 번째')];
  return (
    <div className="try-box" style={actBox} data-sps="softloud">
      <div style={actTitle}>{t('Piano and forte', '피아노와 포르테')}</div>
      {!quiz && <div style={{maxWidth:420,margin:'0 auto 6px'}}><SpsTimeline scr/></div>}
      <div style={actNote}>{quiz ? t('Two Cs. Which one was forte, loud?', 'C를 두 번 들어 봐요. 포르테(세게)는 어느 쪽이었나요?') : t('Play the tune soft, loud, or getting louder. Then try it on the harpsichord.', '선율을 여리게, 세게, 점점 세게 쳐 봐요. 그다음 하프시코드로도 쳐 봐요.')}</div>
      {!quiz && <>
        <div style={{display:'grid',gridTemplateColumns:'repeat(2,minmax(0,1fr))',gap:6,maxWidth:340,margin:'0 auto'}}>{['piano', 'harpsichord'].map(i => <button key={i} className={'chip' + (i === inst ? ' active' : '')} style={{padding:'8px 2px',fontSize:15,minHeight:44}} onClick={() => setInst(i)}>{SPS_IW[i]()}</button>)}</div>
        {spsRow(<>{[['p', t('▶ p: soft', '▶ p: 여리게')], ['f', t('▶ f: loud', '▶ f: 세게')], ['cresc', t('▶ p to f', '▶ p에서 f로')]].map(([k, l]) => <button key={k} className="ghost-btn" style={SPS_TAP} onClick={() => play(k)}>{l}</button>)}</>)}
        {inst === 'harpsichord' && <div style={{textAlign:'center',fontSize:13.5,fontWeight:800,color:BK.coral,marginTop:6}}>{t('On the harpsichord all three sound the same.', '하프시코드에서는 셋 다 같은 세기예요.')}</div>}
      </>}
      {quiz && <div style={{display:'grid',gridTemplateColumns:'repeat(2,minmax(0,1fr))',gap:6,maxWidth:340,margin:'6px auto 0'}}>{[0, 1].map(k => spsChoice(st(k), W[k], () => answer(k, k === quiz.loud), k))}</div>}
      {quiz && quiz.ans != null && spsNote(quiz.ans === quiz.loud, <>{t('Forte was ' + W[quiz.loud] + '.', '포르테는 ' + W[quiz.loud] + '였어요.')}{spsScore(score)}</>)}
      {spsQuizBtns(quiz, ask, () => { S.me(); spsRelease(S.me); setQuiz(null); }, quiz && <button className="ghost-btn" style={SPS_TAP} onClick={() => hear(quiz)}>{t('▶ Hear again', '▶ 다시 듣기')}</button>)}
    </div>
  );
}

// ── page 4: hold a key: the hammer strikes and comes back, the damper moves off; let go: the damper stops the sound.
// Quiz: name the coral part ──
function SpsActionPad() {
  const [down, setDown] = useState(false), [ham, setHam] = useState('rest'), [ring, setRing] = useState(false), { quiz, setQuiz, score, answer } = useSpsQuiz();
  const note = useRef(null), downRef = useRef(false), T = useRef([]);
  const stopMe = useRef(() => { T.current.forEach(clearTimeout); T.current = []; if (note.current) { note.current.damp(); note.current = null; } downRef.current = false; setRing(false); setDown(false); setHam('rest'); }).current;
  useEffect(() => () => { T.current.forEach(clearTimeout); if (note.current) note.current.damp(); spsRelease(stopMe); }, []);
  function press() { if (downRef.current || quiz) return; spsTake(stopMe); downRef.current = true; setDown(true); setRing(true); setHam('strike');
    T.current.push(setTimeout(() => setHam(h => (h === 'strike' ? 'held' : h)), 110));
    const ctx = getAudio(); if (ctx) note.current = actionNote(ctx, false); }
  function release() { if (!downRef.current) return; stopMe(); spsRelease(stopMe); }
  function ask() { release(); let p; do { p = pick(SPS_PARTS); } while (quiz && quiz.p === p); setQuiz({ p, ans: null }); }
  const st = (p) => !quiz || quiz.ans == null ? '' : p === quiz.p ? ' good' : p === quiz.ans ? ' bad' : '';
  return (
    <div className="try-box" style={actBox} data-sps="action">
      <div style={actTitle}>{t('Key, hammer, damper', '건반, 해머, 댐퍼')}</div>
      <div style={actNote}>{quiz ? t('What is the coral part called?', '산호색 부분의 이름은?') : t('Hold the key down: the hammer strikes the string and comes back; the damper moves off. Let go: the damper stops the sound.', '건반을 꾹 누르고 있어 봐요: 해머가 현을 치고 되돌아오고, 댐퍼가 현에서 떨어져요. 손을 떼 봐요: 댐퍼가 소리를 멈춰요.')}</div>
      <div style={{maxWidth:460,margin:'0 auto',touchAction:'none',userSelect:'none'}} onPointerDown={(e) => { if (quiz) return; e.preventDefault(); press(); }} onPointerUp={release} onPointerLeave={release} onPointerCancel={release}>
        <SpsAction down={!quiz && down} ham={quiz ? 'rest' : ham} ring={!quiz && ring} show={quiz ? 'none' : 'words'} hl={quiz ? quiz.p : undefined} size={20}/>
      </div>
      {!quiz && <div style={{textAlign:'center',marginTop:4}}><button className="primary-btn" style={{width:'auto',padding:'10px 20px',fontSize:15,touchAction:'none',minHeight:44}} onPointerDown={(e) => { e.preventDefault(); press(); }} onPointerUp={release} onPointerLeave={release} onPointerCancel={release}
        onKeyDown={(e) => { if ((e.key === ' ' || e.key === 'Enter') && !e.repeat) { e.preventDefault(); press(); } }} onKeyUp={(e) => { if (e.key === ' ' || e.key === 'Enter') release(); }}>{t('Hold the key', '건반 누르고 있기')}</button></div>}
      {quiz && <div style={{display:'grid',gridTemplateColumns:'repeat(2,minmax(0,1fr))',gap:6,marginTop:6}}>{shuffleOnce(quiz, SPS_PARTS).map(p => spsChoice(st(p), SPS_PART_W[p](), () => answer(p, p === quiz.p), p))}</div>}
      {quiz && quiz.ans != null && spsNote(quiz.ans === quiz.p, <>{spsCap(t('the ' + SPS_PART_W[quiz.p](), SPS_PART_W[quiz.p]()))}.{spsScore(score)}</>)}
      {spsQuizBtns(quiz, ask, () => setQuiz(null))}
    </div>
  );
}
// a fixed shuffle for one quiz (kept on the quiz object so the buttons don't move between renders)
const shuffleOnce = (q, list) => q._order || (q._order = shuffle(list.slice()));

// ── page 5: the pedals: press a pedal (tap it), then play C E G: with the sustain pedal the notes ring on; the soft pedal
// makes them softer. Quiz: was the sustain pedal down? ──
function SpsPedalPad() {
  const [sus, setSus] = useState(false), [soft, setSoft] = useState(false), { quiz, setQuiz, score, answer } = useSpsQuiz();
  const S = useSpsSound();
  // C E G one after another: with the sustain pedal each note rings on under the next; without, each stops as the next starts
  const chord = (withSus, withSoft) => S.play(() => playEvents('piano', [[0, 60, withSus ? 4 : 0.9, withSoft ? 0.22 : 0.6], [1, 64, withSus ? 3 : 0.9, withSoft ? 0.22 : 0.6], [2, 67, withSus ? 2.5 : 0.9, withSoft ? 0.22 : 0.6]], 90));
  function ask() { const q = { sus: Math.random() < 0.5, ans: null }; setQuiz(q); chord(q.sus, false); }
  const st = (v) => !quiz || quiz.ans == null ? '' : v === quiz.sus ? ' good' : v === quiz.ans ? ' bad' : '';
  const W = (v) => v ? t('yes, it was down', '네, 밟았어요') : t('no pedal', '아니요, 안 밟았어요');
  const tap = (p) => { if (p === 'sustain') setSus(v => !v); else if (p === 'soft') setSoft(v => !v); };
  return (
    <div className="try-box" style={actBox} data-sps="pedals">
      <div style={actTitle}>{t('The pedals', '페달')}</div>
      <div style={actNote}>{quiz ? t('Listen to C, E, G: was the sustain pedal down?', 'C, E, G를 들어 봐요: 댐퍼 페달을 밟았을까요?') : t('Tap a pedal to press it; tap it again to let it up. Then play C E G.', '페달을 한 번 누르면 밟고, 다시 누르면 떼요. 밟은 채로 C E G를 쳐요.')}</div>
      {!quiz && <>
        <div style={{maxWidth:420,margin:'0 auto'}}><SpsPedals down={[sus && 'sustain', soft && 'soft'].filter(Boolean)} size={20} side short onTap={tap}/></div>
        {spsRow(<>{[['soft', soft], ['sustain', sus]].map(([p, on]) => <button key={p} className={'chip' + (on ? ' active' : '')} style={{padding:'8px 12px',fontSize:15,minHeight:44}} onClick={() => tap(p)}>{SPS_PEDAL_W[p]()}</button>)}<button className="ghost-btn" style={SPS_TAP} onClick={() => chord(sus, soft)}>{t('▶ Play C E G', '▶ C E G 치기')}</button></>)}
        <div style={{textAlign:'center',fontSize:13.5,fontWeight:800,color:BK.ink,marginTop:6,minHeight:20}}>{sus ? t('Every damper is off its string: the notes ring on.', '댐퍼가 모두 현에서 떨어져 있어요: 소리가 계속 울려요.') : soft ? t('A little softer.', '조금 더 여리게.') : ''}</div>
      </>}
      {quiz && <div style={{display:'grid',gridTemplateColumns:'repeat(auto-fit,minmax(130px,1fr))',gap:6,maxWidth:420,margin:'6px auto 0'}}>{[true, false].map(v => spsChoice(st(v), spsCap(W(v)), () => answer(v, v === quiz.sus), String(v)))}</div>}
      {quiz && quiz.ans != null && spsNote(quiz.ans === quiz.sus, <>{quiz.sus ? t('The pedal was down: the notes rang on.', '페달을 밟았어요: 소리가 계속 울렸어요.') : t('No pedal: each note stopped.', '페달을 안 밟았어요: 음마다 소리가 멈췄어요.')}{spsScore(score)}</>)}
      {spsQuizBtns(quiz, ask, () => { S.me(); spsRelease(S.me); setQuiz(null); }, quiz && <button className="ghost-btn" style={SPS_TAP} onClick={() => chord(quiz.sus, false)}>{t('▶ Hear again', '▶ 다시 듣기')}</button>)}
    </div>
  );
}

// ── page 6: grand and upright; the 88 keys in two rows (A to B, then C to C): hear the lowest A, middle C and the highest C;
// count the Cs from the bottom ──
const spsIsW = (m) => [0, 2, 4, 5, 7, 9, 11].includes(m % 12);
function SpsKeyRow({ lo, hi, lit, kw = 17, h = 70 }) {
  const whites = []; for (let m = lo; m <= hi; m++) if (spsIsW(m)) whites.push(m);
  const xw = (m) => whites.indexOf(m) * kw + 1, W = whites.length * kw + 2;
  return <svg viewBox={'0 0 ' + W + ' ' + (h + 2)} style={{width:(W / (29 * kw + 2) * 100) + '%',display:'block'}}>
    {whites.map(m => <rect key={m} x={xw(m)} y="1" width={kw} height={h} fill={lit === m ? PEN_C : '#fff'} stroke={PEN_N} strokeWidth="1"/>)}
    {whites.map(m => <text key={'t' + m} x={xw(m) + kw / 2} y={h - 6} textAnchor="middle" fontSize="14" fontWeight="900" fill={lit === m ? '#fff' : PEN_N}>{m % 12 === 0 ? 'C' : ''}</text>)}
    {Array.from({ length: hi - lo + 1 }, (_, k) => lo + k).filter(m => !spsIsW(m)).map(m => <rect key={m} x={xw(m - 1) + kw * 0.68} y="1" width={kw * 0.64} height={h * 0.6} fill={lit === m ? PEN_C : PEN_N}/>)}
  </svg>;
}
function SpsKeysPad() {
  const [lit, setLit] = useState(null), [count, setCount] = useState(0);
  const S = useSpsSound(() => { setLit(null); setCount(0); });
  function one(m) { S.tune('piano', [m], 0.55, 60, 1.6); setCount(0); setLit(m); }
  function cs() { const list = [24, 36, 48, 60, 72, 84, 96, 108]; S.play(() => playEvents('piano', list.map((m, i) => [i, m, 0.9, 0.5]), 110));
    list.forEach((m, i) => S.T.current.push(setTimeout(() => { setLit(m); setCount(i + 1); }, 100 + i * 545))); }
  return (
    <div className="try-box" style={actBox} data-sps="keys">
      <div style={actTitle}>{t('Grand, upright, 88 keys', '그랜드, 업라이트, 88건반')}</div>
      <div style={{display:'grid',gridTemplateColumns:'1.4fr 1fr',gap:10,alignItems:'end',maxWidth:420,margin:'0 auto 6px'}}>
        <div><svg viewBox="0 0 204 116" style={{width:'100%',display:'block'}}><SpsGrand x={2} y={0} cut/></svg>{<div style={{textAlign:'center',fontSize:13,fontWeight:900}}>{t('grand', '그랜드')}</div>}</div>
        <div><svg viewBox="0 0 160 122" style={{width:'100%',display:'block'}}><SpsUpright cut/></svg>{<div style={{textAlign:'center',fontSize:13,fontWeight:900}}>{t('upright', '업라이트')}</div>}</div>
      </div>
      <div style={actNote}>{t('Hear the two ends and the middle. Then count the Cs from the bottom to the top.', '양 끝과 가운데를 들어 봐요. 그다음 맨 아래부터 맨 위까지 C를 세어 봐요.')}</div>
      <div style={{display:'flex',flexDirection:'column',gap:6,maxWidth:540,margin:'0 auto'}}><SpsKeyRow lo={21} hi={59} lit={lit}/><SpsKeyRow lo={60} hi={108} lit={lit}/></div>
      {spsRow(<>{[[21, t('▶ Lowest A', '▶ 가장 낮은 A')], [60, t('▶ Middle C', '▶ 가운데 도')], [108, t('▶ Highest C', '▶ 가장 높은 C')]].map(([m, l]) => <button key={m} className="ghost-btn" style={SPS_TAP} onClick={() => one(m)}>{l}</button>)}<button className="ghost-btn" style={SPS_TAP} onClick={cs}>{t('▶ Count the Cs', '▶ C 세기')}</button></>)}
      <div style={{textAlign:'center',fontSize:16,fontWeight:900,color:PEN_C,minHeight:24,marginTop:6}}>{count ? t('C number ' + count, count + '번째 C') + (count === 8 ? t(': eight Cs', ': C는 여덟 개') : '') : ''}</div>
    </div>
  );
}
function SpsPad({ page }) { return page === 2 ? <SpsSoundPad/> : page === 3 ? <SpsSoftLoudPad/> : page === 4 ? <SpsActionPad/> : page === 5 ? <SpsPedalPad/> : <SpsKeysPad/>; }

// ── the book on screen: the opener is the lesson's head, every other page a step ──
function SpsLearn({ onStart }) {
  const pages = spsLbPages(true);
  const opener = pages[0];
  return (
    <Lesson id="piano-story" title={bkChapterName('piano-story')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="piano-story"><div className="lb-screen lb-open" style={{display:'flex',flexDirection:'column',gap:12,margin:'0 0 8px'}}>{lbWordsFirst(opener.props.children)}</div></BkChapterCtx.Provider></LbScreenCtx.Provider>}>
      {pages.slice(1).map((pg, i) => (
        <Step key={i} title={pg.props.title}>
          <LbScreenPage page={pg}/>
        </Step>
      ))}
    </Lesson>
  );
}

// ── the drill, after page 6, in the book's order; 9 extra: how the piano grew (the toolbox's timeline) ──
const SPS_LEVELS = [
  { n: 1, label: 'Quill, tangent or hammer?', kind: 'how', time: 12 },
  { n: 2, label: 'Listen: which keyboard?', kind: 'ear', time: 12, noPrint: true },
  { n: 3, label: 'The first piano', kind: 'first', time: 12 },
  { n: 4, label: 'Name the part', kind: 'part', time: 10 },
  { n: 5, label: 'What does it do?', kind: 'does', time: 12 },
  { n: 6, label: 'The pedals', kind: 'pedal', time: 12 },
  { n: 7, label: 'Listen: pedal or not?', kind: 'pedalEar', time: 12, noPrint: true },
  { n: 8, label: 'Grand, upright and 88 keys', kind: 'kinds', time: 12 },
  { n: 9, label: 'Extra: how the piano grew', kind: 'grow', time: 14 },
];
Object.assign(LEVEL_KO, {
  'Quill, tangent or hammer?': '깃촉, 탄젠트, 해머?', 'Listen: which keyboard?': '듣기: 어느 건반 악기?', 'The first piano': '최초의 피아노',
  'Name the part': '부분 이름 맞히기', 'What does it do?': '무슨 일을 할까?', 'The pedals': '페달', 'Listen: pedal or not?': '듣기: 페달을 밟았을까?',
  'Grand, upright and 88 keys': '그랜드, 업라이트, 88건반', 'Extra: how the piano grew': '더 해 보기: 피아노의 변화',
});
// a fact question: [key, en, ko, answer en, answer ko, wrong en[], wrong ko[]]
const SPS_FIRST = [
  ['who', 'Who built the first piano?', '최초의 피아노를 만든 사람은?', 'Cristofori', '크리스토포리', ['Mozart', 'Bach', 'Beethoven'], ['모차르트', '바흐', '베토벤']],
  ['where', 'Where was the first piano built?', '최초의 피아노는 어디에서 만들어졌을까요?', 'Florence, Italy', '이탈리아 피렌체', ['Vienna, Austria', 'London, England', 'Paris, France'], ['오스트리아 빈', '영국 런던', '프랑스 파리']],
  ['when', 'When was the first piano built?', '최초의 피아노는 언제 만들어졌을까요?', 'about 1700', '1700년쯤', ['about 1500', 'about 1800', 'about 1900'], ['1500년쯤', '1800년쯤', '1900년쯤']],
  ['name', 'What does “pianoforte” mean?', '“피아노포르테”의 뜻은?', 'soft-loud', '여리게-세게', ['long-short', 'fast-slow', 'high-low'], ['길게-짧게', '빠르게-느리게', '높게-낮게']],
  ['short', 'What do we call the pianoforte for short?', '피아노포르테를 줄여 부르는 이름은?', 'piano', '피아노', ['harpsichord', 'clavichord', 'organ'], ['하프시코드', '클라비코드', '오르간']],
  ['new', 'What could the first piano do that the harpsichord could not?', '최초의 피아노가 하프시코드와 달리 할 수 있었던 것은?', 'play soft and loud by touch', '누르는 힘에 따라 여리게, 세게 치기', ['play two notes at once', 'play very high notes', 'play without strings'], ['두 음을 한꺼번에 치기', '아주 높은 음 내기', '현 없이 소리 내기']],
  ['maker', 'What was Cristofori?', '크리스토포리는 무엇을 하는 사람이었을까요?', 'an instrument maker', '악기 제작자', ['a king', 'a painter', 'a singer'], ['왕', '화가', '가수']],
];
const SPS_DOES = [
  ['hammer', 'What strikes the string?', '현을 치는 것은?'],
  ['damper', 'What stops the sound when you let go?', '손을 떼면 소리를 멈추는 것은?'],
  ['string', 'What sounds when the hammer strikes it?', '해머가 치면 소리가 나는 것은?'],
  ['key', 'What do your fingers press?', '손가락으로 누르는 것은?'],
  ['damper', 'What moves off the string when you press a key?', '건반을 누르면 현에서 떨어지는 것은?'],
  ['hammer', 'What is covered in felt and comes straight back after striking?', '펠트를 씌웠고, 현을 친 다음 곧바로 되돌아오는 것은?'],
  ['string', 'What is long and thick for a low note?', '낮은 음일수록 길고 굵은 것은?'],
  ['key', 'What is a lever that sends the hammer to the string?', '해머를 현으로 보내는 지렛대는?'],
];
const SPS_PEDAL_Q = [
  ['sustain', 'Which pedal keeps the notes sounding after you let go?', '손을 떼도 소리가 계속 나게 하는 페달은?'],
  ['soft', 'Which pedal’s other name is una corda?', '다른 이름이 우나 코르다인 페달은?'],
  ['sustain', 'Which pedal’s other name is the damper pedal?', '다른 이름이 서스테인 페달인 페달은?'],
  ['middle', 'On most grands, which pedal keeps sounding only the notes you are holding?', '그랜드에서 대개, 누르고 있던 음만 계속 울리게 하는 페달은?'],
  ['middle', 'On most uprights, which pedal makes the piano very quiet for practice?', '업라이트에서 대개, 연습용으로 소리를 아주 작게 하는 페달은?'],
];
const SPS_KINDS = [
  ['flat', 'Its strings lie flat. Which piano is it?', '현이 누워 있어요. 어떤 피아노일까요?', 'grand', '그랜드', ['upright'], ['업라이트']],
  ['wall', 'It fits against a wall. Which piano is it?', '벽에 붙여 놓을 수 있어요. 어떤 피아노일까요?', 'upright', '업라이트', ['grand'], ['그랜드']],
  ['lid', 'Its lid opens like a wing. Which piano is it?', '뚜껑이 날개처럼 열려요. 어떤 피아노일까요?', 'grand', '그랜드', ['upright'], ['업라이트']],
  ['stand', 'Its strings stand up in a tall case. Which piano is it?', '현이 키 큰 상자 안에 서 있어요. 어떤 피아노일까요?', 'upright', '업라이트', ['grand'], ['그랜드']],
  ['keys', 'How many keys does a piano have?', '피아노의 건반은 모두 몇 개일까요?', '88', '88', ['76', '61', '100'], ['76', '61', '100']],
  ['white', 'How many white keys?', '흰건반은 몇 개일까요?', '52', '52', ['36', '44', '56'], ['36', '44', '56']],
  ['black', 'How many black keys?', '검은건반은 몇 개일까요?', '36', '36', ['52', '32', '40'], ['52', '32', '40']],
  ['low', 'What is the lowest key?', '가장 낮은 건반은?', 'A', 'A', ['C', 'E', 'G'], ['C', 'E', 'G']],
  ['high', 'What is the highest key?', '가장 높은 건반은?', 'C', 'C', ['A', 'B', 'G'], ['A', 'B', 'G']],
  ['cs', 'How many Cs are there on 88 keys?', '88건반에 C는 모두 몇 개일까요?', '8', '8', ['7', '9', '12'], ['7', '9', '12']],
];
// how the piano grew (the toolbox's timeline): which came first, or which came later?
const SPS_GROW = [
  { k: 'harp', y: 1400, en: 'the harpsichord', ko: '하프시코드', when: ['about 1400', '1400년쯤'] },
  { k: 'cris', y: 1700, en: 'Cristofori’s piano', ko: '크리스토포리의 피아노', when: ['about 1700', '1700년쯤'] },
  { k: 'forte', y: 1780, en: 'Mozart’s fortepiano', ko: '모차르트의 포르테피아노', when: ['the 1780s', '1780년대'] },
  { k: 'iron', y: 1840, en: 'the iron frame', ko: '철 프레임', when: ['the mid-1800s', '1800년대 중반'] },
  { k: 'k88', y: 1885, en: 'the 88-key piano', ko: '88건반 피아노', when: ['the 1880s', '1880년대'] },
];
function genSpsQuestion(lv, prev) {
  const uid = Math.random(), pk = prev && prev.key;
  const again = (f) => { for (let g = 0; g < 30; g++) { const q = f(); if (q.key !== pk) return { ...q, uid }; } return { ...f(), uid }; };
  // the words are chosen when the question is shown (the language can change after it is made): answers are English keys
  const fact = (list, kind) => again(() => { const r = pick(list);
    return { kind, key: r[0], tx: [r[1], r[2]], answer: r[3], choices: shuffle([r[3], ...r[5]]), names: Object.fromEntries([r[3], ...r[5]].map((e, i) => [e, i ? r[6][i - 1] : r[4]])) }; });
  if (lv.kind === 'how') return again(() => {
    const i = pick(SPS_INST);
    if (Math.random() < 0.5) return { kind: 'how', mode: 'part', inst: i, key: 'v' + i, answer: SPS_PART_OF[i], choices: shuffle(['quill', 'tangent', 'hammer']) };
    return { kind: 'how', mode: 'pic', inst: i, key: 'p' + i, tx: ['Which keyboard works like this?', '이렇게 소리 내는 건반 악기는?'], answer: i, choices: shuffle(SPS_INST.slice()) }; });
  if (lv.kind === 'ear') return again(() => { const i = pick(SPS_INST), tune = pick([[60, 62, 64, 65, 67], [67, 65, 64, 62, 60], [60, 64, 67, 64, 60], [64, 62, 60, 62, 64]]);
    return { kind: 'ear', inst: i, tune, key: 'e' + i + tune.join(), tx: ['Listen. Which keyboard is it?', '들어 봐요. 어느 건반 악기일까요?'], answer: i, choices: shuffle(SPS_INST.slice()) }; });
  if (lv.kind === 'first') return fact(SPS_FIRST, 'first');
  if (lv.kind === 'part') return again(() => { const p = pick(SPS_PARTS); return { kind: 'part', part: p, key: 'pt' + p, tx: ['What is the coral part called?', '산호색 부분의 이름은?'], answer: p, choices: shuffle(SPS_PARTS.slice()) }; });
  if (lv.kind === 'does') return again(() => { const r = pick(SPS_DOES); return { kind: 'does', key: r[1], tx: [r[1], r[2]], answer: r[0], choices: shuffle(SPS_PARTS.slice()) }; });
  if (lv.kind === 'pedal') return again(() => {
    if (Math.random() < 0.4) { const p = pick(SPS_PEDALS); return { kind: 'pedal', mode: 'pic', pedal: p, key: 'pp' + p, tx: ['What is the coral pedal called?', '산호색 페달의 이름은?'], answer: p, choices: shuffle(SPS_PEDALS.slice()) }; }
    const r = pick(SPS_PEDAL_Q); return { kind: 'pedal', mode: 'text', key: r[1], tx: [r[1], r[2]], answer: r[0], choices: shuffle(SPS_PEDALS.slice()) }; });
  if (lv.kind === 'pedalEar') return again(() => { const sus = Math.random() < 0.5, notes = pick([[60, 64, 67], [62, 65, 69], [60, 65, 69], [59, 62, 67]]);
    return { kind: 'pedalEar', sus, notes, key: 'pe' + sus + notes.join(), tx: ['Listen. Was the sustain pedal down?', '들어 봐요. 댐퍼 페달을 밟았을까요?'], answer: sus ? 'yes' : 'no', choices: ['yes', 'no'] }; });
  if (lv.kind === 'kinds') return fact(SPS_KINDS, 'kinds');
  return again(() => { const [a, b] = sampleN(SPS_GROW, 2), later = Math.random() < 0.5, pair = shuffle([a, b]), ans = (a.y < b.y) !== later ? a : b;
    return { kind: 'grow', later, key: [a.k, b.k].sort().join(''), tx: later ? ['Which came later?', '어느 것이 나중일까요?'] : ['Which came first?', '어느 것이 먼저일까요?'], answer: ans.k, choices: pair.map(x => x.k), pair: [a, b] }; });
}
const SPS_CHOICE_W = { yes: () => t('yes: the notes rang on', '네, 소리가 계속 울렸어요'), no: () => t('no: each note stopped', '아니요, 음마다 소리가 멈췄어요') };
function spsChoiceLabel(q, c) {
  if (q.kind === 'how' && q.mode === 'part') return SPS_MOVER_W[c]();
  if (q.kind === 'how' || q.kind === 'ear') return SPS_IW[c]();
  if (q.kind === 'part' || q.kind === 'does') return SPS_PART_W[c]();
  if (q.kind === 'pedal') return SPS_PEDAL_W[c]() + (q.mode === 'pic' || c === 'middle' ? '' : ' (' + (c === 'soft' ? t('left', '왼쪽') : t('right', '오른쪽')) + ')');
  if (q.kind === 'pedalEar') return SPS_CHOICE_W[c]();
  if (q.kind === 'grow') { const g = SPS_GROW.find(x => x.k === c); return t(g.en, g.ko); }
  if (q.names) return t(c, q.names[c]);
  return c;
}
const spsText = (q) => q.kind === 'how' && q.mode === 'part' ? t('What sounds the ' + SPS_IW[q.inst]() + '’s strings?', SPS_IW[q.inst]() + '의 현을 울리는 것은?') : t(q.tx[0], q.tx[1]);
function spsHear(q) {
  if (q.kind === 'ear') { spsTake(null); return playEvents(q.inst, q.tune.map((m, i) => [i, m, 0.9, 0.55]), 120); }
  if (q.kind === 'pedalEar') { spsTake(null); return playEvents('piano', q.notes.map((m, i) => [i, m, q.sus ? 4 - i * 0.6 : 0.9, 0.6]), 90); }
}
function SpsQuestion({ q, given, locked, onAnswer, pixel }) {
  const board = useBoard(q, given);
  useEffect(() => { if (q.kind !== 'ear' && q.kind !== 'pedalEar') return undefined; const tm = setTimeout(() => spsHear(q), 300); return () => { clearTimeout(tm); stopClicks(); }; }, [q.uid]);
  const isDone = !!given, btnCls = pixel ? 'pixel-choice' : 'choice-btn';
  const st = (c) => !isDone ? '' : (String(c) === String(q.answer) ? ' good' : (String(given.ans) === String(c) ? ' bad' : ''));
  const min = q.kind === 'part' || q.kind === 'does' ? 130 : q.kind === 'pedal' || q.kind === 'pedalEar' || q.kind === 'grow' || q.kind === 'first' ? 220 : 104;
  const pic = (node, mw = 300) => <div style={{background:'#fff',borderRadius:pixel ? 0 : 8,padding:pixel ? 4 : '6px 4px',margin:'0 auto 10px',maxWidth:mw}}>{node}</div>;
  let art = null;
  if (q.kind === 'how' && q.mode === 'pic') art = pic(<svg viewBox="0 0 130 100" style={{width:'100%',display:'block'}}><SpsMech kind={SPS_HOW[q.inst]} hl/></svg>, 240);
  if (q.kind === 'part') art = pic(<SpsAction show="none" hl={q.part}/>, 380);
  if (q.kind === 'pedal' && q.mode === 'pic') art = pic(<SpsPedals hl={q.pedal} words={false} side={false}/>, 340);
  return <div><BoardTrack b={board} pixel={pixel}/>
    <p style={pixel ? {fontSize:11.5,textAlign:'center',margin:'0 0 10px',lineHeight:1.7} : {fontSize:17,fontWeight:900,textAlign:'center',margin:'0 0 10px',color:'var(--text)',textWrap:'balance',wordBreak:'keep-all'}}>{spsText(q)}</p>
    {art}
    {(q.kind === 'ear' || q.kind === 'pedalEar') && <div style={{textAlign:'center',margin:'0 0 10px'}}><button className={pixel ? 'pixel-btn' : 'ghost-btn'} onClick={() => spsHear(q)} style={pixel ? {fontSize:9} : {fontSize:15,padding:'8px 16px',minHeight:44}}>{t('▶ Hear it again', '▶ 다시 듣기')}</button></div>}
    <div style={{display:'grid',gridTemplateColumns:'repeat(auto-fit,minmax(' + min + 'px,1fr))',gap:8}}>{q.choices.map(c => <button key={c} disabled={locked} onClick={() => { stopClicks(); onAnswer(c); }} className={btnCls + st(c)} style={{padding:'12px 6px',fontSize:pixel ? 10 : 16,fontWeight:900,minHeight:44,wordBreak:'keep-all'}}>{spsChoiceLabel(q, c)}</button>)}</div>
  </div>;
}
function spsCheck(q, ans) { return ans != null && String(ans) === String(q.answer); }
function spsAnswerLabel(q) {
  if (q.kind === 'grow') { const A = SPS_GROW.find(x => x.k === q.answer), B = q.pair.find(x => x.k !== q.answer);
    return t(A.en + ' (' + A.when[0] + '), ' + (q.later ? 'after ' : 'before ') + B.en + ' (' + B.when[0] + ')', A.ko + ' (' + A.when[1] + '), ' + (q.later ? '그 전에 ' : '그다음 ') + B.ko + ' (' + B.when[1] + ')'); }
  if (q.kind === 'how' && q.mode === 'part') return t(SPS_MOVER_W[q.answer]() + ' (it ' + SPS_MOVES[q.inst]().replace(/^an? \w+ /, '') + ')', SPS_MOVES[q.inst]());
  if (q.kind === 'part' || q.kind === 'does') return t('the ' + SPS_PART_W[q.answer](), SPS_PART_W[q.answer]());
  if (q.kind === 'how' || q.kind === 'ear') return t('the ' + SPS_IW[q.answer](), SPS_IW[q.answer]());
  if (q.kind === 'pedal') return t('the ' + spsChoiceLabel(q, q.answer), spsChoiceLabel(q, q.answer));
  return spsChoiceLabel(q, q.answer);
}
Object.assign(PIANO_STORY_DRILL, { levels: SPS_LEVELS, generate: genSpsQuestion, check: spsCheck, answerLabel: spsAnswerLabel, Question: SpsQuestion, Learn: SpsLearn });
