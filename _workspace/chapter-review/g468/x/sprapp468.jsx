// ─── Phase 468: chapter 12 on screen (what moves on pages 2 to 6), the book as the online lesson, and the drill ───
// Notes sound with the piano (instNote); the xylophone's bars ring with a third partial (a xylophone's, not a marimba's).
// Child-facing words name notes by their letter only (no octave numbers: they are not taught).
const SPR_ZONE = { low: [33, 35, 36, 38, 40, 41, 43], middle: [55, 57, 59, 60, 62, 64, 65], high: [79, 81, 83, 84, 86, 88, 89, 91, 93] };
const SPR_ZW = { low: () => t('low', '낮은 음'), middle: () => t('middle', '가운데 음'), high: () => t('high', '높은 음') };
const sprPiano = (m, at = 0, len = 0.9) => { const ctx = getAudio(); if (!ctx) return; instNote('piano', ctx, ctx.currentTime + 0.04 + at, m, len, 0.48); };
const sprBar = (m, at = 0) => { const ctx = getAudio(); if (!ctx) return; const tt = ctx.currentTime + 0.03 + at; blip(ctx, tt, mFreq(m), 0.5, 0.24, 'sine'); blip(ctx, tt, mFreq(m) * 3, 0.08, 0.05, 'sine'); };
const sprCap = (s) => typeof s === 'string' && LANG !== 'ko' ? s.charAt(0).toUpperCase() + s.slice(1) : s;
const sprScore = (s) => <span style={{color:BK.muted,fontWeight:800,whiteSpace:'nowrap'}}>{'  ·  ' + t(s.right + ' of ' + s.tries, s.tries + '개 중 ' + s.right + '개')}</span>;
const sprNote = (ok, txt) => <div style={{textAlign:'center',fontSize:14,fontWeight:900,marginTop:6,color:ok ? BK.green : BK.coral,textWrap:'balance'}}>{ok ? t('Yes! ', '맞아요! ') : t('Not quite. ', '아쉬워요. ')}{txt}</div>;
const SPR_TAP = { minHeight: 44 };
const sprRow = (kids) => <div style={{display:'flex',gap:6,justifyContent:'center',marginTop:8,flexWrap:'wrap'}}>{kids}</div>;
const sprQuizBtns = (quiz, onNext, onBack, extra) => sprRow(<>{extra}<button className="ghost-btn" style={SPR_TAP} onClick={onNext}>{quiz ? t('Next →', '다음 →') : t('Quiz', '퀴즈')}</button>{quiz && <button className="ghost-btn" style={SPR_TAP} onClick={onBack}>{t('Back', '돌아가기')}</button>}</>);
// the 88 keys as a phone picture: one key lit (an arrow over it), or a range shaded
const SprStrip = ({ lit, range }) => <svg viewBox="0 -22 524 92" style={{width:'100%',display:'block'}}><SprKeys88 x0={2} y0={2} kw={10} h={44} key1={lit != null ? lit : undefined} range={range} cfs={15}/></svg>;
const SPR_LOWER_Q = () => t('Which can go lower?', '어느 쪽이 더 낮은 음을 낼 수 있을까요?');

// ── page 2: hear low, middle and high; then listen and say which ──
function SprZonePad() {
  const [lit, setLit] = useState(null), [quiz, setQuiz] = useState(null), [score, setScore] = useState({ right: 0, tries: 0 });
  const zones = ['low', 'middle', 'high'];
  function hearZone(z) { const m = pick(SPR_ZONE[z]); setLit(m); sprPiano(m); }
  function ask() { const z = pick(zones), m = pick(SPR_ZONE[z]); setLit(null); setQuiz({ z, m, ans: null }); sprPiano(m); }
  function tap(z) { if (!quiz) { hearZone(z); return; } if (quiz.ans) return; const ok = z === quiz.z; setQuiz({ ...quiz, ans: z }); setLit(quiz.m); setScore(s => ({ right: s.right + (ok ? 1 : 0), tries: s.tries + 1 })); }
  const st = (z) => !quiz || !quiz.ans ? '' : z === quiz.z ? ' good' : z === quiz.ans ? ' bad' : '';
  return (
    <div className="try-box" style={actBox} data-spr="zone">
      <div style={actTitle}>{t('Low, middle or high?', '낮은 음? 가운데 음? 높은 음?')}</div>
      <div style={actNote}>{t('Tap low, middle or high to hear a note there; an arrow shows its key. Then tap Quiz: listen, and tap where it was.', '낮은 음, 가운데 음, 높은 음을 눌러 그곳의 음을 들어 봐요. 화살표가 건반을 보여 줘요. 그다음 ‘퀴즈’를 누르고, 듣고 나서 어디였는지 눌러요.')}</div>
      <div style={{maxWidth:520,margin:'0 auto'}}><SprStrip lit={lit}/></div>
      <div style={{display:'grid',gridTemplateColumns:'repeat(3,minmax(0,1fr))',gap:8,maxWidth:360,margin:'6px auto 0'}}>{zones.map(z => <button key={z} className={'choice-btn' + st(z)} onClick={() => tap(z)} style={{padding:'12px 0',fontSize:15,fontWeight:900}}>{quiz ? SPR_ZW[z]() : '▶ ' + SPR_ZW[z]()}</button>)}</div>
      {quiz && quiz.ans && sprNote(quiz.ans === quiz.z, <>{sprCap(SPR_ZW[quiz.z]())}.{sprScore(score)}</>)}
      {sprQuizBtns(quiz, ask, () => { setQuiz(null); setLit(null); }, quiz && <button className="ghost-btn" style={SPR_TAP} onClick={() => sprPiano(quiz.m)}>{t('▶ Hear again', '▶ 다시 듣기')}</button>)}
    </div>
  );
}

// ── page 3: the xylophone's bars; then two things: which sounds higher? ──
const SPR_XY = [72, 74, 76, 77, 79, 81, 83, 84];
const sprBell = (cx, cy, k) => <g><path d={'M' + (cx - 16 * k) + ' ' + (cy + 18 * k) + ' Q' + (cx - 15 * k) + ' ' + (cy - 14 * k) + ' ' + cx + ' ' + (cy - 16 * k) + ' Q' + (cx + 15 * k) + ' ' + (cy - 14 * k) + ' ' + (cx + 16 * k) + ' ' + (cy + 18 * k) + ' Z'} {...SPR_SWF}/><line x1={cx - 19 * k} x2={cx + 19 * k} y1={cy + 18 * k} y2={cy + 18 * k} {...SPR_SW}/><circle cx={cx} cy={cy + 22 * k} r={3.4 * k} fill={PEN_C}/><circle cx={cx} cy={cy - 20 * k} r={3.5 * k} {...SPR_SW}/></g>;
// a string stretched between two pegs (long and thick, or short and thin)
const sprString = (cx, cy, len, w) => <g><line x1={cx} x2={cx} y1={cy - len / 2} y2={cy + len / 2} stroke={PEN_N} strokeWidth={w} strokeLinecap="round"/><circle cx={cx} cy={cy - len / 2 - 5} r="5" fill={PEN_C}/><circle cx={cx} cy={cy + len / 2 + 5} r="5" fill={PEN_C}/></g>;
const sprXyBar = (cx, cy, h) => <g><rect x={cx - 12} y={cy - h / 2} width="24" height={h} rx="5" fill={PEN_N}/><circle cx={cx} cy={cy - h / 2 + h * 0.22} r="2.6" fill="#fff"/><circle cx={cx} cy={cy + h / 2 - h * 0.22} r="2.6" fill="#fff"/></g>;
const SPR_PAIRS = [
  { id: 'bar', big: (x, y) => sprXyBar(x, y, 110), small: (x, y) => sprXyBar(x, y, 54), lo: 60, hi: 79, sound: 'bar' },
  { id: 'drum', big: (x, y) => <SprInst id="drum" x={x - 51} y={y - 51} s={1.7}/>, small: (x, y) => <SprInst id="drum" x={x - 30} y={y - 30} s={1}/>, lo: 41, hi: 65 },
  { id: 'fiddle', big: (x, y) => <SprFiddle cx={x} base={y + 66} h={130} peg/>, small: (x, y) => <SprFiddle cx={x} base={y + 30} h={60}/>, lo: 36, hi: 55 },
  { id: 'brass', big: (x, y) => <SprInst id="tuba" x={x - 48} y={y - 48} s={1.6}/>, small: (x, y) => <SprInst id="trumpet" x={x - 30} y={y - 30} s={1}/>, lo: 38, hi: 67 },
  { id: 'bell', big: (x, y) => sprBell(x, y, 2.6), small: (x, y) => sprBell(x, y, 1.15), lo: 55, hi: 79 },
  { id: 'string', big: (x, y) => sprString(x, y, 136, 4.2), small: (x, y) => sprString(x, y, 58, 1.8), lo: 43, hi: 67 },
];
function SprBigPad() {
  const [hit, setHit] = useState(-1), [quiz, setQuiz] = useState(null), [score, setScore] = useState({ right: 0, tries: 0 });
  const T = useRef([]);
  useEffect(() => () => T.current.forEach(clearTimeout), []);
  function bar(i, at = 0) { sprBar(SPR_XY[i], at); T.current.push(setTimeout(() => setHit(i), at * 1000 + 30), setTimeout(() => setHit(h => (h === i ? -1 : h)), at * 1000 + 280)); }
  function run() { T.current.forEach(clearTimeout); T.current = []; SPR_XY.forEach((_, k) => bar(k, k * 0.17)); }
  function ask() { let p; do { p = pick(SPR_PAIRS); } while (quiz && quiz.p.id === p.id); setQuiz({ p, bigLeft: Math.random() < 0.5, ans: null }); }
  function choose(side) { if (!quiz || quiz.ans) return; const smallSide = quiz.bigLeft ? 'right' : 'left', ok = side === smallSide; setQuiz({ ...quiz, ans: side }); setScore(s => ({ right: s.right + (ok ? 1 : 0), tries: s.tries + 1 }));
    const P = quiz.p; if (P.sound === 'bar') { sprBar(P.lo); sprBar(P.hi, 0.9); } else { sprPiano(P.lo); sprPiano(P.hi, 0.9); } }
  const W = 320, bw = 30, gap = 6, x0 = (W - (8 * bw + 7 * gap)) / 2, xyH = (i) => 80 - i * 6;
  return (
    <div className="try-box" style={actBox} data-spr="big">
      <div style={actTitle}>{t('Big is low, small is high', '크면 낮고, 작으면 높아요')}</div>
      <div style={actNote}>{t('Tap the bars: long bars sound low, short ones high. Then tap Quiz: which one sounds higher? Tap it.', '막대를 눌러 봐요: 긴 막대는 낮은 소리, 짧은 막대는 높은 소리. 그다음 ‘퀴즈’를 누르고, 더 높은 소리를 낼 것을 눌러요.')}</div>
      {!quiz && <svg viewBox={'0 0 ' + W + ' 130'} style={{width:'100%',maxWidth:460,display:'block',margin:'0 auto',touchAction:'manipulation'}}>
        {SPR_XY.map((m, i) => { const h = xyH(i), x = x0 + i * (bw + gap), y = 62 - h / 2; return <g key={m} onClick={() => bar(i)} style={{cursor:'pointer'}}>
          <rect x={x - gap / 2} y="0" width={bw + gap} height="130" fill="transparent"/>
          <rect x={x} y={y} width={bw} height={h} rx="5" fill={hit === i ? PEN_C : PEN_N}/><text x={x + bw / 2} y="122" textAnchor="middle" fontSize="13" fontWeight="900" fill={PEN_N}>{'CDEFGABC'[i]}</text></g>; })}
      </svg>}
      {quiz && <svg viewBox="0 0 320 180" style={{width:'100%',maxWidth:420,display:'block',margin:'0 auto',touchAction:'manipulation'}}>
        {['left', 'right'].map(side => { const cx = side === 'left' ? 88 : 232, big = (side === 'left') === quiz.bigLeft, smallSide = quiz.bigLeft ? 'right' : 'left';
          const fill = !quiz.ans ? '#fff' : side === smallSide ? '#dcefe7' : side === quiz.ans ? '#fbdcd2' : '#fff';
          return <g key={side} onClick={() => choose(side)} style={{cursor:quiz.ans ? 'default' : 'pointer'}}><rect x={cx - 70} y="4" width="140" height="172" rx="12" fill={fill} stroke="rgba(38,41,107,0.2)"/>{(big ? quiz.p.big : quiz.p.small)(cx, 92)}</g>; })}
      </svg>}
      {quiz && !quiz.ans && <div style={{textAlign:'center',fontSize:14,fontWeight:800,color:BK.ink,marginTop:4}}>{t('Which one sounds higher? Tap it.', '어느 쪽이 더 높은 소리를 낼까요? 눌러요.')}</div>}
      {quiz && quiz.ans && sprNote(quiz.ans === (quiz.bigLeft ? 'right' : 'left'), <>{t('The smaller one. Listen: big, then small.', '작은 쪽이에요. 들어 봐요: 큰 것, 그다음 작은 것.')}{sprScore(score)}</>)}
      {sprQuizBtns(quiz, ask, () => setQuiz(null), !quiz && <button className="ghost-btn" style={SPR_TAP} onClick={run}>{t('▶ All the bars', '▶ 막대 전부')}</button>)}
    </div>
  );
}

// ── page 4: tap an instrument: its family and how it sounds; then the quiz: which family? ──
function SprFamilyPad() {
  const [sel, setSel] = useState(null), [quiz, setQuiz] = useState(null), [score, setScore] = useState({ right: 0, tries: 0 });
  function ask() { let it; do { it = pick(SPR_INST); } while (quiz && quiz.it.id === it.id); setSel(null); setQuiz({ it, ans: null }); }
  function answer(f) { if (!quiz || quiz.ans) return; const ok = f === quiz.it.fam; setQuiz({ ...quiz, ans: f }); setScore(s => ({ right: s.right + (ok ? 1 : 0), tries: s.tries + 1 })); }
  const S = sel && SPR_INST.find(i => i.id === sel);
  return (
    <div className="try-box" style={actBox} data-spr="fam">
      <div style={actTitle}>{t('Which family?', '어느 가족일까요?')}</div>
      <div style={actNote}>{t('Tap an instrument to see its family and how it makes its sound. Then tap Quiz.', '악기를 눌러 가족과 소리 내는 방법을 봐요. 그다음 ‘퀴즈’를 눌러요.')}</div>
      {!quiz && <><div style={{display:'grid',gap:6,maxWidth:460,margin:'0 auto'}}>{SPR_FAMS.map(f => <div key={f} style={{display:'grid',gridTemplateColumns:'repeat(4,minmax(0,1fr))',gap:6}}>{SPR_INST.filter(i => i.fam === f).map(it => <button key={it.id} className={'choice-btn' + (sel === it.id ? ' active' : '')} onClick={() => setSel(it.id)} style={{padding:'4px 2px',display:'flex',flexDirection:'column',alignItems:'center'}}>
          <svg viewBox="0 0 60 60" style={{width:48,height:48}}><SprInst id={it.id}/></svg><span style={{fontSize:11.5,fontWeight:800}}>{sprName(it.id)}</span></button>)}</div>)}</div>
        {S && <div style={{textAlign:'center',fontSize:14.5,fontWeight:900,color:BK.ink,marginTop:8}}>{sprName(S.id)}: <span style={{color:BK.coral}}>{sprFamName(S.fam)}</span> · {SPR_FAM[S.fam].how()}</div>}</>}
      {quiz && <><div style={{display:'flex',flexDirection:'column',alignItems:'center'}}><svg viewBox="0 0 60 60" style={{width:100,height:100}}><SprInst id={quiz.it.id}/></svg><b style={{fontSize:16,color:BK.ink}}>{sprName(quiz.it.id)}</b></div>
        <div style={{display:'grid',gridTemplateColumns:'repeat(2,minmax(0,1fr))',gap:8,maxWidth:340,margin:'8px auto 0'}}>{SPR_FAMS.map(f => <button key={f} className={'choice-btn' + (!quiz.ans ? '' : f === quiz.it.fam ? ' good' : f === quiz.ans ? ' bad' : '')} onClick={() => answer(f)} style={{padding:'12px 0',fontSize:15,fontWeight:900}}>{sprFamName(f)}</button>)}</div>
        {quiz.ans && sprNote(quiz.ans === quiz.it.fam, <>{sprCap(sprFamName(quiz.it.fam))}: {SPR_FAM[quiz.it.fam].how()}.{sprScore(score)}</>)}</>}
      {sprQuizBtns(quiz, ask, () => setQuiz(null))}
    </div>
  );
}

// ── page 5: the violin family: hear each one's lowest note on the piano; then put them in order, lowest first ──
const SPR_VLOW = { 'Double bass': 28, Cello: 36, Viola: 48, Violin: 55 };
function SprLadderPad() {
  const shuffled = () => { let o; do { o = shuffle(SPR_VFAM.map(v => v.n)); } while (o.every((n, i) => n === SPR_VFAM[i].n)); return o; };
  const [order, setOrder] = useState(shuffled), [turn, setTurn] = useState(false), [got, setGot] = useState([]), [bad, setBad] = useState(null), [slips, setSlips] = useState(0);
  const want = SPR_VFAM.map(v => v.n), done = got.length === 4;
  const shown = turn ? order : want;
  function tap(n) { sprPiano(SPR_VLOW[n]); if (!turn || got.includes(n) || done) return; if (n === want[got.length]) { setGot(g => [...g, n]); setBad(null); } else { setBad(n); setSlips(x => x + 1); } }
  function start() { setTurn(true); setOrder(shuffled()); setGot([]); setBad(null); setSlips(0); }
  const H = { 'Double bass': 128, Cello: 92, Viola: 54, Violin: 46 };
  return (
    <div className="try-box" style={actBox} data-spr="ladder">
      <div style={actTitle}>{t('The violin family', '바이올린 가족')}</div>
      <div style={actNote}>{t('Tap each one to hear its lowest note on the piano. Then tap Your turn and tap them from the lowest to the highest.', '하나씩 눌러 가장 낮은 음을 피아노 소리로 들어 봐요. 그다음 ‘내 차례’를 누르고 가장 낮은 것부터 가장 높은 것까지 눌러요.')}</div>
      <svg viewBox="0 0 320 176" style={{width:'100%',maxWidth:440,display:'block',margin:'0 auto',touchAction:'manipulation'}}>
        {shown.map((n, i) => { const cx = 44 + i * 77, used = turn && got.includes(n), wrong = bad === n, v = SPR_VFAM.find(x => x.n === n);
          return <g key={n} onClick={() => tap(n)} style={{cursor:'pointer'}}><rect x={cx - 36} y="2" width="72" height="172" rx="10" fill={wrong ? '#fbdcd2' : '#fff'} stroke="rgba(38,41,107,0.18)"/>
            <g opacity={used ? 0.35 : 1}><SprFiddle cx={cx} base={150} h={H[n]} peg={v.peg} bass={v.bass} hl={used}/></g>
            {(!turn || used) && <text x={cx} y="167" textAnchor="middle" fontSize="11.5" fontWeight="900" fill={PEN_N}>{sprRName(n)}</text>}
            {used && <text x={cx} y="20" textAnchor="middle" fontSize="16" fontWeight="900" fill={BK.green}>{got.indexOf(n) + 1}</text>}</g>; })}
      </svg>
      {turn && <div style={{textAlign:'center',fontSize:14,fontWeight:900,marginTop:4,color:done ? BK.green : bad ? BK.coral : BK.muted}}>
        {done ? (slips ? t('Done! ' + slips + (slips > 1 ? ' mistakes.' : ' mistake.'), '다 했어요! 실수 ' + slips + '번.') : t('Perfect, no mistakes! ✓', '완벽해요, 실수 없이! ✓'))
          : bad ? t('Not yet: find a lower one.', '아직이에요: 더 낮은 것을 찾아요.') : got.length ? t('Next: the next lowest', '다음: 그다음으로 낮은 것') : t('Next: the lowest', '다음: 가장 낮은 것')}</div>}
      {sprRow(<button className="ghost-btn" style={SPR_TAP} onClick={start}>{turn ? t('Start again', '처음부터') : t('Your turn', '내 차례')}</button>)}
    </div>
  );
}

// ── page 6: an instrument's range over the 88 keys; hear its lowest and highest notes on the piano ──
const SPR_RLIST = ['Double bass', 'Cello', 'Viola', 'Violin', 'Flute', 'Piccolo', 'Tuba', 'Trumpet', 'Bass', 'Soprano'];
const SPR_BOOK6 = ['Double bass', 'Cello', 'Viola', 'Violin', 'Flute', 'Piccolo'];   // the ranges book page 6 draws (with the two voices)
const sprFar = (a, b) => Math.abs(SPR_RANGE(a).lo - SPR_RANGE(b).lo) >= 4;
const SPR_RQ = (() => { const out = [['Tuba', 'Trumpet'], ['Bass', 'Soprano']]; SPR_BOOK6.forEach((a, i) => SPR_BOOK6.slice(i + 1).forEach(b => { if (sprFar(a, b)) out.push([a, b]); })); return out; })();
function SprRangePad() {
  const [sel, setSel] = useState('Violin'), [quiz, setQuiz] = useState(null), [score, setScore] = useState({ right: 0, tries: 0 });
  const R = SPR_RANGE(sel);
  function show(n) { setSel(n); const r = SPR_RANGE(n); sprPiano(r.lo); sprPiano(r.hi, 0.95); }
  function ask() { let p; do { p = pick(SPR_RQ); } while (quiz && quiz.pair.includes(p[0]) && quiz.pair.includes(p[1])); setQuiz({ pair: shuffle(p.slice()), ans: null }); }
  const lower = quiz && (SPR_RANGE(quiz.pair[0]).lo < SPR_RANGE(quiz.pair[1]).lo ? quiz.pair[0] : quiz.pair[1]);
  function answer(n) { if (!quiz || quiz.ans) return; setQuiz({ ...quiz, ans: n }); setScore(s => ({ right: s.right + (n === lower ? 1 : 0), tries: s.tries + 1 })); quiz.pair.forEach((p, i) => sprPiano(SPR_RANGE(p).lo, i * 0.95)); }
  return (
    <div className="try-box" style={actBox} data-spr="range">
      <div style={actTitle}>{t('Ranges on the keys', '건반 위의 음역')}</div>
      <div style={actNote}>{t('Tap a name: its range lights up on the keys, and you hear its lowest and highest notes on the piano. Then tap Quiz.', '이름을 눌러 봐요: 건반에 음역이 켜지고, 가장 낮은 음과 가장 높은 음이 피아노 소리로 들려요. 그다음 ‘퀴즈’를 눌러요.')}</div>
      {!quiz && <><div style={{maxWidth:520,margin:'0 auto'}}><SprStrip range={[R.lo, R.hi]}/></div>
        <div style={{display:'flex',flexWrap:'wrap',gap:5,justifyContent:'center',marginTop:6}}>{SPR_RLIST.map(n => <button key={n} className={'chip' + (n === sel ? ' active' : '')} onClick={() => show(n)} style={{padding:'6px 12px',minHeight:44}}>{sprRName(n)}</button>)}</div></>}
      {quiz && <><div style={{maxWidth:520,margin:'0 auto'}}><SprStrip range={quiz.ans ? [SPR_RANGE(lower).lo, SPR_RANGE(lower).hi] : null}/></div>
        {!quiz.ans && <div style={{textAlign:'center',fontSize:14,fontWeight:800,color:BK.ink,margin:'4px 0'}}>{SPR_LOWER_Q()}</div>}
        <div style={{display:'grid',gridTemplateColumns:'repeat(2,minmax(0,1fr))',gap:8,maxWidth:340,margin:'6px auto 0'}}>{quiz.pair.map(n => <button key={n} className={'choice-btn' + (!quiz.ans ? '' : n === lower ? ' good' : n === quiz.ans ? ' bad' : '')} onClick={() => answer(n)} style={{padding:'12px 0',fontSize:15,fontWeight:900}}>{sprRName(n)}</button>)}</div>
        {quiz.ans && sprNote(quiz.ans === lower, <>{t('The ' + sprRName(lower) + ': its range starts lower.', sprRName(lower) + '의 음역이 더 낮은 데서 시작해요.')}{sprScore(score)}</>)}</>}
      {sprQuizBtns(quiz, ask, () => setQuiz(null))}
    </div>
  );
}
function SprPad({ page }) { return page === 2 ? <SprZonePad/> : page === 3 ? <SprBigPad/> : page === 4 ? <SprFamilyPad/> : page === 5 ? <SprLadderPad/> : <SprRangePad/>; }

// ── the book on screen. Old ticks kept where the idea is the same: 'Big is low, small is high' (2), 'The piano and the
// orchestra' (4); low/middle/high, the families and low to high are new (5, 6, 7); the checks 8. Hz and the octave
// ladder (old 0, 3) are the drill's extra level 8 ──
const SPR_STORE = [5, 2, 6, 7, 4, 8];
function SprLearn({ onStart }) {
  const pages = sprLbPages(true);
  const opener = pages[0];
  return (
    <Lesson id="pitch-range" title={t('Pitch, Hz & Range', '음높이, 헤르츠와 음역')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="pitch-range"><div className="lb-screen lb-open" style={{display:'flex',flexDirection:'column',gap:12,margin:'0 0 8px'}}>{lbWordsFirst(opener.props.children)}</div></BkChapterCtx.Provider></LbScreenCtx.Provider>}>
      {pages.slice(1).map((pg, i) => (
        <Step key={i} storeAs={SPR_STORE[i]} title={pg.props.title}>
          <LbScreenPage page={pg}/>
        </Step>
      ))}
    </Lesson>
  );
}

// ── the drill: five levels by eye, two by ear, two extras ──
const SPR_LEVELS = [
  { n: 1, label: 'Low, middle or high?', kind: 'zone', time: 6 },
  { n: 2, label: 'Which sounds higher?', kind: 'size', time: 6 },
  { n: 3, label: 'Which family?', kind: 'fam', time: 7 },
  { n: 4, label: 'How does it make its sound?', kind: 'how', time: 8 },
  { n: 5, label: 'Which can go lower?', kind: 'order', time: 7 },
  { n: 6, label: 'Listen: higher or lower?', kind: 'earHL', time: 10, noPrint: true },
  { n: 7, label: 'Listen: low, middle or high?', kind: 'earZone', time: 10, noPrint: true },
  { n: 8, label: 'Extra: each A doubles (Hz)', kind: 'oct', time: 12 },
  { n: 9, label: 'Extra: who can play this note?', kind: 'who', time: 12 },
];
Object.assign(LEVEL_KO, {
  'Low, middle or high?': '낮은 음? 가운데 음? 높은 음?', 'Which sounds higher?': '어느 쪽이 더 높을까요?', 'Which family?': '어느 가족일까요?',
  'How does it make its sound?': '어떻게 소리를 낼까요?', 'Which can go lower?': '어느 쪽이 더 낮을까요?', 'Listen: higher or lower?': '듣기: 더 높아요? 더 낮아요?',
  'Listen: low, middle or high?': '듣기: 낮은 음? 가운데 음? 높은 음?', 'Extra: each A doubles (Hz)': '더 해 보기: A마다 두 배 (Hz)', 'Extra: who can play this note?': '더 해 보기: 누가 이 음을 낼 수 있을까요?',
});
const SPR_ORDER_SETS = [['Double bass', 'Cello', 'Viola', 'Violin'], ['Bass', 'Soprano'], ['Tuba', 'Trumpet'], ['Flute', 'Piccolo'], ['Cello', 'Flute'], ['Double bass', 'Piccolo']];
const SPR_OCT = [[1, 880], [2, 1760], [-1, 220], [-2, 110]];
function genSprQuestion(lv, prev) {
  const uid = Math.random(), pk = prev && prev.key;
  const again = (f) => { for (let g = 0; g < 20; g++) { const q = f(); if (q.key !== pk) return { ...q, uid }; } return { ...f(), uid }; };
  if (lv.kind === 'zone' || lv.kind === 'earZone') return again(() => { const z = pick(['low', 'middle', 'high']), m = pick(SPR_ZONE[z]); return { kind: lv.kind, z, m, key: 'z' + m, answer: z, choices: ['low', 'middle', 'high'] }; });
  if (lv.kind === 'size') return again(() => { const p = pick(SPR_PAIRS), bigLeft = Math.random() < 0.5; return { kind: 'size', pid: p.id, bigLeft, key: p.id + bigLeft, answer: bigLeft ? 'right' : 'left', choices: ['left', 'right'] }; });
  if (lv.kind === 'fam') return again(() => { const it = pick(SPR_INST); return { kind: 'fam', id: it.id, key: it.id, answer: it.fam, choices: SPR_FAMS.slice() }; });
  if (lv.kind === 'how') return again(() => { const it = pick(SPR_INST); return { kind: 'how', id: it.id, key: 'h' + it.id, answer: it.fam, choices: shuffle(SPR_FAMS.slice()) }; });
  if (lv.kind === 'order') return again(() => { const set = pick(SPR_ORDER_SETS), pr = shuffle(sampleN(set, 2)); const low = SPR_RANGE(pr[0]).lo < SPR_RANGE(pr[1]).lo ? pr[0] : pr[1]; return { kind: 'order', pr, key: pr.join(), answer: low, choices: pr }; });
  if (lv.kind === 'oct') return again(() => { const [n, hz] = pick(SPR_OCT); return { kind: 'oct', n, key: 'o' + n, answer: String(hz), choices: SPR_OCT.map(x => String(x[1])) }; });
  if (lv.kind === 'who') return again(() => { for (let g = 0; g < 60; g++) { const three = sampleN(SPR_BOOK6, 3); if (!sprFar(three[0], three[1]) || !sprFar(three[0], three[2]) || !sprFar(three[1], three[2])) continue;
      const lows = three.map(n => SPR_RANGE(n).lo).sort((a, b) => a - b), ans = three.find(n => SPR_RANGE(n).lo === lows[0]), top = Math.min(lows[1] - 1, SPR_RANGE(ans).hi), cands = []; for (let m = lows[0]; m <= top; m++) if (sprIsWhite(m)) cands.push(m); if (!cands.length) continue;
      const m = pick(cands); return { kind: 'who', m, three: shuffle(three), key: 'w' + m + three.join(), answer: ans, choices: shuffle(three) }; }
    return { kind: 'who', m: 33, key: 'w33', answer: 'Double bass', choices: ['Double bass', 'Violin', 'Flute'] }; });
  return again(() => { const a = 48 + Math.floor(Math.random() * 25), d = pick([-7, -5, -4, -3, 3, 4, 5, 7]); return { kind: 'earHL', a, b: a + d, key: 'e' + a + d, answer: d > 0 ? 'higher' : 'lower', choices: ['higher', 'lower'] }; });
}
const SPR_HL = { higher: () => t('higher', '더 높아요'), lower: () => t('lower', '더 낮아요') };
const sprOctWhere = (n) => n === 1 ? t('the next A to the right', '오른쪽으로 바로 다음 A') : n === 2 ? t('the second A to the right', '오른쪽으로 두 번째 A') : n === -1 ? t('the next A to the left', '왼쪽으로 바로 다음 A') : t('the second A to the left', '왼쪽으로 두 번째 A');
function SprQuestion(props) {
  const { q, given, locked, onAnswer, pixel } = props;
  const board = useBoard(q, given);
  const hear = () => { if (q.kind === 'earZone') sprPiano(q.m); else if (q.kind === 'earHL') { sprPiano(q.a); sprPiano(q.b, 0.9); } };
  useEffect(() => { if (q.kind && q.kind.startsWith('ear')) { const tm = setTimeout(hear, 250); return () => clearTimeout(tm); } }, [q.uid]);
  const done = !!given;
  const btnCls = pixel ? 'pixel-choice' : 'choice-btn';
  const st = (c) => !done ? '' : c === q.answer ? ' good' : (given.ans === c ? ' bad' : '');
  const prompt = (txt) => <p style={pixel ? {fontSize:11.5,textAlign:'center',margin:'0 0 10px',lineHeight:1.7} : {fontSize:15,fontWeight:700,textAlign:'center',margin:'0 0 10px',color:'var(--muted)',textWrap:'balance'}}>{txt}</p>;
  const box = (kids) => <div style={{background:pixel ? '#faf6ec' : 'transparent',borderRadius:8,padding:pixel ? 6 : 0,margin:'0 auto 10px'}}>{kids}</div>;
  const after = () => { if (q.kind === 'zone' || q.kind === 'who') sprPiano(q.m); else if (q.kind === 'order') q.pr.forEach((p, i) => sprPiano(SPR_RANGE(p).lo, i * 0.9)); else if (q.kind === 'oct') { sprPiano(69); sprPiano(69 + 12 * q.n, 0.9); } else if (q.kind === 'size') { const P = SPR_PAIRS.find(p => p.id === q.pid); if (P.sound === 'bar') { sprBar(P.lo); sprBar(P.hi, 0.9); } else { sprPiano(P.lo); sprPiano(P.hi, 0.9); } } };
  const grid = (cols, render, pad = '14px 4px') => <div style={{display:'grid',gridTemplateColumns:'repeat(' + cols + ',minmax(0,1fr))',gap:8}}>{q.choices.map(c => <button key={c} disabled={locked} onClick={() => { onAnswer(c); if (!q.kind.startsWith('ear')) setTimeout(after, 120); }} className={btnCls + st(c)} style={{padding:pad,textWrap:'balance'}}>{render(c)}</button>)}</div>;
  const again = <div style={{textAlign:'center',margin:'0 0 12px'}}><button className={pixel ? 'pixel-btn' : 'ghost-btn'} onClick={hear} style={pixel ? {fontSize:9} : {fontSize:15,padding:'8px 16px',minHeight:44}}>{t('▶ Hear again', '▶ 다시 듣기')}</button></div>;
  const word = (s) => <span style={{fontSize:pixel ? 11 : 16,fontWeight:900}}>{s}</span>;
  const inst = (id) => box(<div style={{display:'flex',flexDirection:'column',alignItems:'center'}}><svg viewBox="0 0 60 60" style={{width:96,height:96}}><SprInst id={id}/></svg><b style={{fontSize:16,color:pixel ? '#26296b' : BK.ink}}>{sprName(id)}</b></div>);
  let body;
  if (q.kind === 'zone') body = <>{prompt(t('Is the orange key low, middle or high?', '주황색 건반은 낮은 음, 가운데 음, 높은 음 중 어디일까요?'))}{box(<div style={{maxWidth:420,margin:'0 auto'}}><SprStrip lit={q.m}/></div>)}{grid(3, c => word(SPR_ZW[c]()))}</>;
  else if (q.kind === 'earZone') body = <>{prompt(t('Listen. Low, middle or high?', '들어 봐요. 낮은 음, 가운데 음, 높은 음?'))}{box(<div style={{maxWidth:420,margin:'0 auto'}}><SprStrip lit={done ? q.m : null}/></div>)}{again}{grid(3, c => word(SPR_ZW[c]()))}</>;
  else if (q.kind === 'earHL') body = <>{prompt(t('Two notes. Is the second one higher or lower?', '음 두 개. 두 번째 음이 더 높을까요, 더 낮을까요?'))}{again}{grid(2, c => word(SPR_HL[c]()))}</>;
  else if (q.kind === 'size') { const P = SPR_PAIRS.find(p => p.id === q.pid);
    body = <>{prompt(t('Which one sounds higher?', '어느 쪽이 더 높은 소리를 낼까요?'))}{box(<svg viewBox="0 0 320 180" style={{width:'100%',maxWidth:360,display:'block',margin:'0 auto'}}>{['left', 'right'].map(side => { const cx = side === 'left' ? 88 : 232, big = (side === 'left') === q.bigLeft; return <g key={side}>{(big ? P.big : P.small)(cx, 92)}</g>; })}</svg>)}
      {grid(2, c => word(c === 'left' ? t('the left one', '왼쪽') : t('the right one', '오른쪽')))}</>; }
  else if (q.kind === 'fam') body = <>{prompt(t('Which family is it in?', '어느 가족일까요?'))}{inst(q.id)}{grid(2, c => word(sprFamName(c)))}</>;
  else if (q.kind === 'how') body = <>{prompt(t('How does it make its sound?', '어떻게 소리를 낼까요?'))}{inst(q.id)}{grid(2, c => <span style={{fontSize:pixel ? 10 : 14,fontWeight:800}}>{SPR_FAM[c].how()}</span>, '12px 4px')}</>;
  else if (q.kind === 'oct') body = <>{prompt(t('The A above middle C vibrates 440 times a second: 440 Hz. Each A to the right vibrates twice as many times a second; each A to the left, half as many. How many Hz is ' + sprOctWhere(q.n) + '?', '가운데 도 위의 A는 1초에 440번 떨려요: 440 Hz. A는 오른쪽으로 하나 갈 때마다 떨리는 횟수가 두 배가 되고, 왼쪽으로 하나 갈 때마다 절반이 돼요. ' + sprOctWhere(q.n) + '는 몇 Hz일까요?'))}{box(<div style={{maxWidth:420,margin:'0 auto'}}><SprStrip lit={69 + 12 * q.n}/></div>)}{grid(2, c => word(c + ' Hz'))}</>;
  else if (q.kind === 'who') body = <>{prompt(t('Which of these can play the orange key?', '이 중에서 주황색 건반의 음을 낼 수 있는 것은?'))}{box(<div style={{maxWidth:420,margin:'0 auto'}}><SprStrip lit={q.m}/></div>)}{grid(3, c => word(sprRName(c)), '12px 2px')}</>;
  else body = <>{prompt(SPR_LOWER_Q())}{grid(2, c => word(sprRName(c)))}</>;
  return <div><BoardTrack b={board} pixel={pixel}/>{body}</div>;
}
function sprCheck(q, ans) { return ans !== null && ans !== undefined && ans === q.answer; }
function sprAnswerLabel(q) {
  if (q.kind === 'zone' || q.kind === 'earZone') return SPR_ZW[q.answer]();
  if (q.kind === 'earHL') return SPR_HL[q.answer]();
  if (q.kind === 'size') return t('the smaller one', '작은 쪽');
  if (q.kind === 'fam') return sprFamName(q.answer);
  if (q.kind === 'how') return SPR_FAM[q.answer].how() + ' (' + sprFamName(q.answer) + ')';
  if (q.kind === 'oct') return q.answer + ' Hz';
  if (q.kind === 'who') return t('the ' + sprRName(q.answer) + ': its range starts lowest', sprRName(q.answer) + ': 음역이 가장 낮은 데서 시작해요');
  return t('the ' + sprRName(q.answer), sprRName(q.answer));
}
Object.assign(PITCH_RANGE_DRILL, { levels: SPR_LEVELS, generate: genSprQuestion, check: sprCheck, answerLabel: sprAnswerLabel, Question: SprQuestion, Learn: SprLearn });
