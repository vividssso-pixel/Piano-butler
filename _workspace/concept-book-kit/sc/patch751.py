import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build CF (call 25, batch 4, part 2; her 09:56: fun first): the four rooms the board listed as still without a thing to
# make: The staff, Ledger lines, Signs, Terms. Each is a game with goals to chase (stars kept on the device):
#   The staff: My staff tune (tap the staff to write notes; play them; four stars: lines only, spaces only, steps only, skips only)
#   Ledger lines: Climb the ladders (the same staff with room above and below: two ladders up into the bird's sky, two down
#     into the turtle's sea, visit Clara, and find all five Cs: low, bass, middle, treble, high)
#   Signs: Build a road map (four bars, one sign at a time, placed where you like; guess how many bars you will hear, then
#     listen and watch the road)
#   Terms: A recipe for a tune (pick a speed, a loudness and a touch from the Grade 1 words and hear Twinkle cooked that way;
#     or the mystery recipe: hear it, then name the three words)
# Her words only: Clara's ladders (never 'rung'), the bird's sky and the turtle's sea, the five Cs by their names.

CODE = r'''
// ══ Build CF: batch 4, part 2: the staff, ledger lines, signs and terms (call 25; her 09:56: fun first) ══
// ── a staff to tap: notes written where you tap, ladders drawn as they are needed ──
const ST_CLEF = { treble: { bot: 30, top: 38 }, bass: { bot: 18, top: 26 } };
const stLadders = (d, c) => (d < c.bot ? Math.floor((c.bot - d) / 2) : d > c.top ? Math.floor((d - c.top) / 2) : 0);
const stLetter = (d) => 'CDEFGAB'[((d - 28) % 7 + 7) % 7];
function TapStaff({ clef, lo, hi, notes, on = -1, onTap, W = 340 }) {
  const c = ST_CLEF[clef], U = 6, yOf = (d) => 18 + (hi - d) * U, H = yOf(lo) + 30, x0 = 62, step = Math.min(34, (W - x0 - 14) / 8);
  const pick = (e) => { const r = e.currentTarget.getBoundingClientRect(), y = (e.clientY - r.top) * (H / r.height); const d = Math.max(lo, Math.min(hi, Math.round(hi - (y - 18) / U))); onTap(d); };
  return <svg viewBox={'0 0 ' + W + ' ' + H} style={{width:'100%',maxWidth:W,display:'block',margin:'0 auto',background:'#fff',borderRadius:8,cursor:'pointer',touchAction:'manipulation'}} onClick={pick} role="img" aria-label={t('Tap the staff to write a note', '오선을 눌러 음을 써요')}>
    {[0, 1, 2, 3, 4].map(i => <line key={i} x1="10" x2={W - 10} y1={yOf(c.bot + i * 2)} y2={yOf(c.bot + i * 2)} stroke={BK.ink} strokeWidth="1.2"/>)}
    <text x="14" y={yOf(clef === 'treble' ? 32 : 24) + (clef === 'treble' ? 9 : 4)} fontSize={clef === 'treble' ? 52 : 34} fill={BK.ink} style={{fontFamily:MUSIC_FONT}}>{clef === 'treble' ? '𝄞' : '𝄢'}</text>
    {notes.map((d, i) => { const x = x0 + i * step + step / 2, y = yOf(d), n = stLadders(d, c), lad = [];
      for (let k = 1; k <= n; k++) { const ld = d < c.bot ? c.bot - 2 * k : c.top + 2 * k; lad.push(<line key={k} x1={x - 13} x2={x + 13} y1={yOf(ld)} y2={yOf(ld)} stroke={BK.ink} strokeWidth="1.5"/>); }
      return <g key={i}>{lad}<ellipse cx={x} cy={y} rx="7" ry="5.2" transform={'rotate(-20 ' + x + ' ' + y + ')'} fill={i === on ? BK.coral : BK.ink}/>
        <text x={x} y={H - 8} textAnchor="middle" fontSize="12" fontWeight="900" fill={i === on ? BK.coral : BK.muted} fontFamily="Inter, sans-serif">{stLetter(d)}</text></g>; })}
  </svg>;
}
const ST_GOALS = {
  staff: [['lines', 'Lines only', '줄에만'], ['spaces', 'Spaces only', '칸에만'], ['steps', 'Steps only: line, space, line…', '한 칸씩만: 줄, 칸, 줄…'], ['skips', 'Skips only: line to line, or space to space', '건너뛰기만: 줄에서 줄, 칸에서 칸']],
  ledger: [['sky', 'Climb two ladders up into the bird\'s sky', '새의 하늘로 발판 두 개 올라가기'], ['sea', 'Dive two ladders down into the turtle\'s sea', '거북이의 바다로 발판 두 개 내려가기'], ['clara', 'Visit Clara (middle C)', '클라라(가운데 도) 만나기'], ['cs', 'Find all five Cs: low, bass, middle, treble, high', '다섯 C 모두 찾기: 낮은 도, 낮은음자리표 도, 가운데 도, 높은음자리표 도, 높은 도']] };
const ST_FIVE = [[14, 'low C', '낮은 도'], [21, 'bass C', '낮은음자리표 도'], [28, 'middle C', '가운데 도'], [35, 'treble C', '높은음자리표 도'], [42, 'high C', '높은 도']];
function StaffMaker({ kind }) {   // kind: 'staff' (on the staff) | 'ledger' (with room for ladders above and below)
  const T = useSpTimers(), store = 'pb_mk_' + kind;
  const [clef, setClef] = useState('treble'), [notes, setNotes] = useState([]), [on, setOn] = useState(-1), [fives, setFives] = useState([]), [news, setNews] = useState(null);
  const [stars, setStars] = useState(() => { try { return JSON.parse(localStorage.getItem(store)) || {}; } catch (e) { return {}; } });
  const c = ST_CLEF[clef], lo = kind === 'staff' ? c.bot - 1 : c.bot - 7, hi = kind === 'staff' ? c.top + 1 : c.top + 7;
  const play = (ns) => { T.clear(); const r = spPlay(ns.map((d, j) => ({ at: j * 0.5, keys: [hpSemi(d)], len: 0.45, vol: 0.14 })), 60); if (!r) return; ns.forEach((_, j) => T.at(r.ms(j * 0.5), () => setOn(j))); T.at(r.ms(ns.length * 0.5), () => setOn(-1)); };
  const check = (ns, fv) => { const got = [];
    if (kind === 'staff' && ns.length >= 4) { const ev = ns.every(d => d % 2 === 0), od = ns.every(d => d % 2 === 1), df = ns.slice(1).map((d, j) => Math.abs(d - ns[j]));
      if (ev) got.push('lines'); if (od) got.push('spaces'); if (df.every(x => x === 1)) got.push('steps'); if (df.every(x => x === 2)) got.push('skips'); }
    if (kind === 'ledger') { if (ns.some(d => d >= ST_CLEF.treble.top + 4) && clef === 'treble') got.push('sky'); if (ns.some(d => d <= ST_CLEF.bass.bot - 4) && clef === 'bass') got.push('sea'); if (ns.includes(28)) got.push('clara'); if (fv.length >= 5) got.push('cs'); }
    const fresh = got.filter(g => !stars[g]); if (fresh.length) { const n = { ...stars }; fresh.forEach(g => { n[g] = 1; }); setStars(n); setNews(fresh[0]); try { localStorage.setItem(store, JSON.stringify(n)); } catch (e) {} } };
  const tap = (d) => { if (notes.length >= 8) return; const ns = notes.concat([d]); setNotes(ns); playKey(hpSemi(d), 0.5); setNews(null);
    const fv = ST_FIVE.some(([cd]) => cd === d) && !fives.includes(d) ? fives.concat([d]) : fives; setFives(fv); check(ns, fv); };
  const G = ST_GOALS[kind], last = notes[notes.length - 1];
  const where = last == null ? '' : stLadders(last, c) ? t(stLetter(last) + ': ladder ' + stLadders(last, c) + (last > c.top ? ', up in the bird\'s sky' : ', down in the turtle\'s sea'), stLetter(last) + ': 발판 ' + stLadders(last, c) + (last > c.top ? ', 새의 하늘 위' : ', 거북이의 바다 아래'))
    : t(stLetter(last) + (last % 2 === 0 ? ' on a line' : ' in a space'), stLetter(last) + (last % 2 === 0 ? ', 줄 위' : ', 칸 안'));
  const five = ST_FIVE.find(([cd]) => cd === last);
  return (
    <div className="try-box" style={actBox} data-mk={kind === 'staff' ? 'lines' : 'ladders'}>
      <div style={actTitle}>{kind === 'staff' ? t('My staff tune', '나의 오선 선율') : t('Climb the ladders', '발판 오르내리기')}</div>
      <div style={actNote}>{kind === 'staff' ? (LANG === 'ko' ? <>오선을 눌러 음을 써요: <b>줄 위</b>든 <b>칸 안</b>이든. 여덟 음까지 쓰고 들어 봐요. 별 네 개에 도전!</> : <>Tap the staff to write a note: <b>on a line</b> or <b>in a space</b>. Write up to eight, then hear them. Can you earn all four stars?</>)
        : (LANG === 'ko' ? <>오선 밖으로 나가요! 높은음자리표 위는 <b>새의 하늘</b>, 낮은음자리표 아래는 <b>거북이의 바다</b>. 클라라의 작은 발판(덧줄)을 타고 올라가고 내려가요. 다섯 C를 모두 찾을 수 있을까요?</> : <>Out of the staff! Above the treble staff is <b>the bird's sky</b>, below the bass staff <b>the turtle's sea</b>. Climb Clara's little ladders (ledger lines) up and down. Can you find all five Cs?</>)}</div>
      <div style={{display:'flex',gap:'4px 12px',justifyContent:'center',flexWrap:'wrap',margin:'0 0 8px'}}>{G.map(([id, en, ko]) => <span key={id} style={{fontSize:12.5,fontWeight:800,color:stars[id] ? BK.coral : BK.muted}}>{stars[id] ? '★' : '☆'} {t(en, ko)}</span>)}</div>
      {spChips([['treble', t('Treble clef', '높은음자리표')], ['bass', t('Bass clef', '낮은음자리표')]], clef, (x) => { T.clear(); setClef(x); setNotes([]); setOn(-1); setNews(null); })}
      <TapStaff clef={clef} lo={lo} hi={hi} notes={notes} on={on} onTap={tap}/>
      {spMsg(news ? t('★ ' + G.find(g => g[0] === news)[1] + '!', '★ ' + G.find(g => g[0] === news)[2] + '!') : five && kind === 'ledger' ? t(where + ': ' + five[1] + '!', where + ': ' + five[2] + '!') : notes.length ? where : t('Tap the staff.', '오선을 눌러요.'), news ? BK.coral : undefined)}
      {kind === 'ledger' && <div style={{display:'flex',gap:4,justifyContent:'center',flexWrap:'wrap',marginTop:6}}>{ST_FIVE.map(([cd, en, ko]) => <span key={cd} style={{fontSize:12,fontWeight:800,padding:'2px 8px',borderRadius:10,border:'1px solid ' + (fives.includes(cd) ? BK.green : BK.line),color:fives.includes(cd) ? BK.green : BK.muted}}>{fives.includes(cd) ? '✓ ' : ''}{t(en, ko)}</span>)}</div>}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        {notes.length > 0 && <button className="ghost-btn" style={spBtn} onClick={() => play(notes)}>{t('▶ Play it', '▶ 들어 보기')}</button>}
        {notes.length > 0 && <button className="ghost-btn" style={spBtn} onClick={() => { setNotes(notes.slice(0, -1)); setNews(null); }}>{t('⌫ Back', '⌫ 지우기')}</button>}
        {notes.length > 0 && <button className="ghost-btn" style={spBtn} onClick={() => { setNotes([]); setNews(null); }}>{t('Clear', '처음부터')}</button>}
      </div>
    </div>
  );
}
function StaffTune() { return <StaffMaker kind="staff"/>; }
function LadderClimb() { return <StaffMaker kind="ledger"/>; }

// ── Signs: Build a road map ──
const RM_BARS = [[0, 2, 4, 2], [4, 5, 7, 7], [9, 7, 5, 4], [2, 4, 0, 0]];   // four bars to tell apart by ear, C position
const RM_SIGNS = [['none', 'No sign', '기호 없음'], ['rep', 'Repeat signs', '도돌이표'], ['volta', '1st and 2nd time bars', '1번·2번 괄호'], ['dc', 'D.C. al Fine', 'D.C. al Fine'], ['ds', 'D.S. al Fine', 'D.S. al Fine']];
const rmRoad = (sg, a) => { if (sg === 'rep') return [1, 2, 3, 4].concat([1, 2, 3, 4].slice(a - 1)); if (sg === 'volta') return [1, 2, 3, 1, 2, 4];
  if (sg === 'dc') return [1, 2, 3, 4].concat([1, 2, 3, 4].slice(0, a)); if (sg === 'ds') return [1, 2, 3, 4].concat([2, 3, 4].slice(0, a - 1)); return [1, 2, 3, 4]; };
function RoadBuilder() {
  const T = useSpTimers();
  const [sg, setSg] = useState('rep'), [a, setA] = useState(1), [guess, setGuess] = useState(null), [at, setAt] = useState(-1), [step, setStep] = useState(-1), [run, setRun] = useState(0);
  const road = rmRoad(sg, a), N = road.length;
  const opts = sg === 'rep' ? [1, 2, 3, 4] : sg === 'dc' ? [1, 2, 3] : sg === 'ds' ? [2, 3] : [];
  const reset = (fn) => { T.clear(); setGuess(null); setAt(-1); setStep(-1); fn(); };
  const play = () => { T.clear(); const ev = []; road.forEach((b, j) => RM_BARS[b - 1].forEach((k, q) => ev.push({ at: j * 2 + q * 0.5, keys: [k], len: 0.45, vol: 0.14 }))); const r = spPlay(ev, 96); if (!r) return; road.forEach((b, j) => T.at(r.ms(j * 2), () => { setAt(b); setStep(j); })); T.at(r.ms(N * 2), () => { setAt(-1); setStep(N); }); };
  const say = (g) => { if (guess != null) return; setGuess(g); setRun(n => (g === N ? n + 1 : 0)); setTimeout(play, 300); };
  const signsAt = (b) => { const L = [], R = [], top = [];
    if (sg === 'rep') { if (b === a && a > 1) L.push('‖:'); if (b === 4) R.push(':‖'); }
    if (sg === 'volta') { if (b === 3) { R.push(':‖'); top.push('1.'); } if (b === 4) top.push('2.'); }
    if (sg === 'dc') { if (b === a) top.push('Fine'); if (b === 4) top.push('D.C. al Fine'); }
    if (sg === 'ds') { if (b === 2) top.push('segno'); if (b === a) top.push('Fine'); if (b === 4) top.push('D.S. al Fine'); }
    return { L, R, top }; };
  return (
    <div className="try-box" style={actBox} data-mk="road">
      <div style={actTitle}>{t('Build a road map', '나만의 길 지도')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>네 마디, 기호 하나. 기호를 고르고 자리를 정해요. 그다음 <b>먼저 맞혀 봐요</b>: 모두 몇 마디를 듣게 될까요? 그리고 들으면서 길을 따라가요.</> : <>Four bars, one sign. Choose a sign and where it goes. Then <b>guess first</b>: how many bars will you hear in all? Then listen and follow the road.</>}</div>
      {spChips(RM_SIGNS.map(([id, en, ko]) => [id, t(en, ko)]), sg, (x) => reset(() => { setSg(x); setA(x === 'ds' ? 3 : x === 'dc' ? 2 : 1); }))}
      {opts.length > 0 && <div style={{textAlign:'center',fontSize:13,fontWeight:800,color:BK.muted,margin:'2px 0 4px'}}>{sg === 'rep' ? t('The repeat goes back to bar…', '도돌이표가 돌아가는 마디…') : t('Fine goes after bar…', 'Fine가 오는 마디…')}</div>}
      {opts.length > 0 && spChips(opts.map(n => [n, String(n)]), a, (n) => reset(() => setA(n)))}
      <div style={{display:'grid',gridTemplateColumns:'repeat(4,minmax(0,1fr))',gap:0,margin:'6px 0',border:'1.5px solid ' + BK.ink,borderRadius:6,background:'#fff'}}>{[1, 2, 3, 4].map(b => { const S = signsAt(b), lit = at === b;
        return <div key={b} style={{borderLeft:b > 1 ? '1.5px solid ' + BK.ink : 'none',padding:'4px 2px 8px',minHeight:84,background:lit ? '#fbe3da' : 'transparent',position:'relative',textAlign:'center'}}>
          <div style={{minHeight:22,fontSize:11.5,fontWeight:900,color:BK.coral,fontStyle:'italic',lineHeight:1.1}}>{S.top.map((x, i) => x === 'segno' ? <svg key={i} viewBox="-10 -28 20 30" width="14" height="20" style={{verticalAlign:'middle'}}>{sgnSegnoSvg(0, 0, 1, BK.coral)}</svg> : /^[12]\.$/.test(x) ? <div key={i} style={{borderTop:'1.5px solid ' + BK.coral,borderLeft:'1.5px solid ' + BK.coral,margin:'2px 4px 0',padding:'1px 4px',textAlign:'left'}}>{x}</div> : <div key={i}>{x}</div>)}</div>
          <div style={{display:'flex',alignItems:'center',justifyContent:'center',gap:3}}><span style={{fontSize:16,fontWeight:900,color:BK.ink,minWidth:12}}>{S.L.join(' ')}</span><span style={{fontFamily:LB_SERIF,fontSize:22,fontWeight:900,color:lit ? BK.coral : BK.ink}}>{b}</span><span style={{fontSize:16,fontWeight:900,color:BK.ink,minWidth:12}}>{S.R.join(' ')}</span></div>
          <div style={{display:'flex',gap:3,justifyContent:'center',marginTop:6}}>{RM_BARS[b - 1].map((k, i) => <span key={i} style={{width:6,height:6,borderRadius:3,background:lit ? BK.coral : BK.line,marginTop:(12 - k) * 1.2}}/>)}</div></div>; })}</div>
      {guess == null ? <><div style={{textAlign:'center',fontSize:14,fontWeight:900,color:BK.ink,margin:'4px 0'}}>{t('Guess first: how many bars will you hear?', '먼저 맞혀요: 모두 몇 마디를 들을까요?')}</div>
        <div style={{display:'grid',gridTemplateColumns:'repeat(5,minmax(0,1fr))',gap:5}}>{[4, 5, 6, 7, 8].map(n => <button key={n} className="choice-btn" onClick={() => say(n)} style={{padding:'10px 0',fontSize:17,fontWeight:900}}>{n}</button>)}</div></>
        : <div style={{display:'flex',gap:5,justifyContent:'center',flexWrap:'wrap',margin:'6px 0'}}>{road.map((b, j) => <span key={j} style={{width:28,height:28,borderRadius:14,display:'inline-flex',alignItems:'center',justifyContent:'center',fontWeight:900,fontSize:14,border:'2px solid ' + (j === step ? BK.coral : j < step ? BK.ink : BK.line),background:j === step ? BK.coral : j < step ? BK.ink : '#fff',color:j <= step ? '#fff' : BK.muted}}>{j <= step ? b : ''}</span>)}</div>}
      {spMsg(guess == null ? '' : step < N ? t('Follow the road…', '길을 따라가요…') : guess === N ? t('Yes: ' + N + ' bars: ' + road.join(' ') + '.' + (run > 1 ? ' ' + run + ' in a row!' : ''), '맞아요: ' + N + '마디: ' + road.join(' ') + '.' + (run > 1 ? ' ' + run + '번 연속!' : '')) : t('It was ' + N + ' bars: ' + road.join(' ') + '. Move the sign and try again.', N + '마디였어요: ' + road.join(' ') + '. 기호를 옮겨서 다시 해 봐요.'), guess != null && step >= N ? (guess === N ? BK.green : BK.coral) : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>{guess != null && step >= N && <button className="ghost-btn" style={spBtn} onClick={play}>{t('▶ Again', '▶ 다시')}</button>}{guess != null && <button className="ghost-btn" style={spBtn} onClick={() => reset(() => {})}>{t('▶ New guess', '▶ 새로 맞히기')}</button>}</div>
    </div>
  );
}

// ── Terms: A recipe for a tune (the Grade 1 words) ──
const RC_SPEED = [['Adagio', 70, 'slow, at ease', '느리고 여유 있게'], ['Andante', 84, 'at an easy walking pace', '편히 걷는 빠르기로'], ['Moderato', 108, 'at a moderate speed', '보통 빠르기로'], ['Allegro', 144, 'lively and fast', '활기차고 빠르게'], ['Presto', 184, 'very fast', '매우 빠르게']];   // the app's own meanings and speeds (TERMS, the Terms room)
const RC_LOUD = [['piano', 'p', 'soft', '여리게'], ['forte', 'f', 'loud', '세게'], ['crescendo', 'cresc.', 'getting louder', '점점 세게'], ['diminuendo', 'dim.', 'getting softer', '점점 여리게']];
const RC_TOUCH = [['legato', 'smoothly, joined', '부드럽게 이어서'], ['staccato', 'short and detached', '짧게 끊어서']];
const RC_TUNE = [0, 0, 7, 7, 9, 9, 7, -1, 5, 5, 4, 4, 2, 2, 0, -1];   // a well-known nursery tune (public domain); -1 holds the note before it
function RecipeTune() {
  const T = useSpTimers();
  const [mode, setMode] = useState('cook'), [sp, setSp] = useState(3), [ld, setLd] = useState(0), [tc, setTc] = useState(0), [on, setOn] = useState(-1);
  const [mys, setMys] = useState(null), [ans, setAns] = useState({}), [shown, setShown] = useState(false), [score, setScore] = useState(0);
  const cook = (s, l, c) => { T.clear(); const n = RC_TUNE.length, ev = [];
    RC_TUNE.forEach((k, j) => { if (k < 0) return; const hold = RC_TUNE[j + 1] === -1 ? 2 : 1, f = j / (n - 1), lv = RC_LOUD[l][0] === 'piano' ? 0.06 : RC_LOUD[l][0] === 'forte' ? 0.22 : RC_LOUD[l][0] === 'crescendo' ? 0.05 + 0.18 * f : 0.23 - 0.18 * f;
      ev.push({ at: j, keys: [k], len: RC_TOUCH[c][0] === 'staccato' ? 0.3 : hold * 0.95, vol: lv }); });
    const r = spPlay(ev, RC_SPEED[s][1]); if (!r) return; ev.forEach(e => T.at(r.ms(e.at), () => setOn(e.at))); T.at(r.ms(n), () => setOn(-1)); };
  const newMystery = () => { let m, g = 0; do { m = { s: Math.floor(Math.random() * 5), l: Math.floor(Math.random() * 4), c: Math.floor(Math.random() * 2) }; } while (mys && JSON.stringify(m) === JSON.stringify(mys) && g++ < 10); setMys(m); setAns({}); setShown(false); setTimeout(() => cook(m.s, m.l, m.c), 300); };
  const pickAns = (k, v) => { if (shown) return; const n = { ...ans, [k]: v }; setAns(n); if (n.s != null && n.l != null && n.c != null) { setShown(true); const right = (n.s === mys.s) + (n.l === mys.l) + (n.c === mys.c); setScore(x => x + right); } };
  const row = (lab, list, val, set, key) => <div style={{margin:'6px 0'}}><div style={{fontSize:12,fontWeight:900,color:BK.muted,letterSpacing:'0.06em',textTransform:'uppercase',marginBottom:3}}>{lab}</div>
    <div style={{display:'flex',gap:5,flexWrap:'wrap'}}>{list.map((x, i) => { const sel = mode === 'cook' ? val === i : ans[key] === i, right = mode === 'mystery' && shown && mys[key] === i, wrong = mode === 'mystery' && shown && ans[key] === i && mys[key] !== i;
      return <button key={i} onClick={() => (mode === 'cook' ? set(i) : pickAns(key, i))} style={{minHeight:40,padding:'4px 10px',borderRadius:20,fontFamily:"'Playfair Display', Georgia, serif",fontStyle:'italic',fontWeight:800,fontSize:15,cursor:'pointer',
        border:'1.5px solid ' + (right ? BK.green : wrong ? BK.coral : sel ? BK.ink : BK.line),background:right ? BK.greenSoft : wrong ? '#fbe3da' : sel ? BK.ink : '#fff',color:sel && !right && !wrong ? '#fff' : BK.ink}}>{x[0]}</button>; })}</div></div>;
  const card = mode === 'cook' ? t(RC_SPEED[sp][0] + ', ' + RC_LOUD[ld][0] + ', ' + RC_TOUCH[tc][0] + ': ' + RC_SPEED[sp][2] + ', ' + RC_LOUD[ld][2] + ', ' + RC_TOUCH[tc][1] + '.', RC_SPEED[sp][0] + ', ' + RC_LOUD[ld][0] + ', ' + RC_TOUCH[tc][0] + ': ' + RC_SPEED[sp][3] + ', ' + RC_LOUD[ld][3] + ', ' + RC_TOUCH[tc][2] + '.') : '';
  return (
    <div className="try-box" style={actBox} data-mk="recipe">
      <div style={actTitle}>{t('A recipe for a tune', '선율 요리법')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>재료는 세 가지: <b>빠르기</b> 한 낱말, <b>셈여림</b> 한 낱말, <b>터치</b> 한 낱말. 골라서 같은 선율을 요리해요. 미스터리 요리법에서는 듣고 세 낱말을 맞혀요!</> : <>Three ingredients: one word for <b>speed</b>, one for <b>loudness</b>, one for <b>touch</b>. Pick them and cook the same tune your way. In the mystery recipe, listen and name all three words!</>}</div>
      {spChips([['cook', t('Cook it', '요리하기')], ['mystery', t('Mystery recipe', '미스터리 요리법')]], mode, (m) => { T.clear(); setMode(m); setOn(-1); if (m === 'mystery') newMystery(); })}
      {row(t('Speed', '빠르기'), RC_SPEED, sp, setSp, 's')}{row(t('Loudness', '셈여림'), RC_LOUD, ld, setLd, 'l')}{row(t('Touch', '터치'), RC_TOUCH, tc, setTc, 'c')}
      <div style={{display:'flex',gap:3,justifyContent:'center',alignItems:'flex-end',height:34,margin:'8px 0 4px'}}>{RC_TUNE.map((k, j) => <span key={j} style={{width:10,height:k < 0 ? 4 : 8 + (k + 1) * 2,borderRadius:3,background:j === on ? BK.coral : k < 0 ? 'transparent' : BK.line}}/>)}</div>
      {spMsg(mode === 'cook' ? card : shown ? t('You got ' + ((ans.s === mys.s) + (ans.l === mys.l) + (ans.c === mys.c)) + ' of 3: it was ' + RC_SPEED[mys.s][0] + ', ' + RC_LOUD[mys.l][0] + ', ' + RC_TOUCH[mys.c][0] + '. Score: ' + score + '.', '3개 중 ' + ((ans.s === mys.s) + (ans.l === mys.l) + (ans.c === mys.c)) + '개: 정답은 ' + RC_SPEED[mys.s][0] + ', ' + RC_LOUD[mys.l][0] + ', ' + RC_TOUCH[mys.c][0] + '. 점수: ' + score + '.') : t('Listen, then pick one word in each row.', '듣고, 줄마다 낱말 하나씩 골라요.'), shown ? BK.green : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        {mode === 'cook' ? <button className="primary-btn" style={spBtn} onClick={() => cook(sp, ld, tc)}>{t('▶ Cook it', '▶ 요리하기')}</button>
          : <><button className="ghost-btn" style={spBtn} onClick={() => mys && cook(mys.s, mys.l, mys.c)}>{t('▶ Hear it again', '▶ 다시 듣기')}</button>{shown && <button className="ghost-btn" style={spBtn} onClick={newMystery}>{t('▶ Another mystery', '▶ 다른 미스터리')}</button>}</>}
      </div>
    </div>
  );
}
'''
rep("// ══ Build BH: Blues jam ══", CODE + "\n// ══ Build BH: Blues jam ══")
rep("""  { id: 'mk-word', ch: 'note-names',""", """  { id: 'mk-lines', ch: 'staff', title: 'My staff tune', blurb: 'Tap the staff to write notes, then hear them. Four stars: lines only, spaces only, steps, skips.', C: () => <StaffTune/> },   // Build CF
  { id: 'mk-ladders', ch: 'ledger-lines', title: 'Climb the ladders', blurb: 'Up into the bird\\'s sky, down into the turtle\\'s sea: find all five Cs.', C: () => <LadderClimb/> },
  { id: 'mk-road', ch: 'signs', title: 'Build a road map', blurb: 'Four bars and one sign, where you like: guess how many bars you will hear, then follow the road.', C: () => <RoadBuilder/> },
  { id: 'mk-recipe', ch: 'terms', title: 'A recipe for a tune', blurb: 'A speed, a loudness and a touch: cook a tune your way, or name the mystery recipe.', C: () => <RecipeTune/> },
  { id: 'mk-word', ch: 'note-names',""")
rep("""  'mk-word': ['나의 낱말 선율',""", """  'mk-lines': ['나의 오선 선율', '오선을 눌러 음을 쓰고 들어요. 별 넷: 줄에만, 칸에만, 한 칸씩, 건너뛰기.'],
  'mk-ladders': ['발판 오르내리기', '새의 하늘로 올라가고 거북이의 바다로 내려가요: 다섯 C를 모두 찾아요.'],
  'mk-road': ['나만의 길 지도', '네 마디와 기호 하나, 원하는 자리에: 몇 마디를 들을지 맞히고 길을 따라가요.'],
  'mk-recipe': ['선율 요리법', '빠르기, 셈여림, 터치 한 낱말씩: 나만의 선율을 요리하거나 미스터리 요리법을 맞혀요.'],
  'mk-word': ['나의 낱말 선율',""")
rep("""'mk-word': ['keys', 0, 0, 'game'],""", """'mk-word': ['keys', 0, 0, 'game'], 'mk-lines': ['pitch', 0, 1, 'game ear'], 'mk-ladders': ['ledger', 1, 2, 'game'], 'mk-road': ['words', 1, 2, 'game ear'], 'mk-recipe': ['words', 1, 2, 'game ear'],""")
rep("""'mk-word': 'p-staff',""", """'mk-word': 'p-staff', 'mk-lines': 'p-staff', 'mk-ladders': 'p-staff', 'mk-road': 'c-map', 'mk-recipe': 't-tempo',""")
rep("""  'mk-word': () => (\n""", """  'mk-lines': () => (
    <svg width="34" height="34" viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#2e8a6e"/>{[6, 9, 12, 15, 18].map(y => <path key={y} d={'M3 ' + y + 'H21'} stroke="#fefbf3" strokeWidth="0.8"/>)}{[[7, 15], [12, 12], [17, 9]].map(([x, y]) => <ellipse key={x} cx={x} cy={y} rx="1.9" ry="1.4" fill="#e9a83a"/>)}</svg>
  ),
  'mk-ladders': () => (
    <svg width="34" height="34" viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#3b4fa8"/>{[10, 13, 16, 19].map(y => <path key={y} d={'M3 ' + y + 'H14'} stroke="#fefbf3" strokeWidth="0.8"/>)}{[7, 4].map(y => <path key={y} d={'M15 ' + y + 'H21'} stroke="#fefbf3" strokeWidth="1"/>)}<ellipse cx="18" cy="4" rx="2" ry="1.5" fill="#e9a83a"/></svg>
  ),
  'mk-road': () => (
    <svg width="34" height="34" viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#7a4f96"/><rect x="3" y="9" width="18" height="7" rx="1" fill="none" stroke="#fefbf3" strokeWidth="1"/>{[7.5, 12, 16.5].map(x => <path key={x} d={'M' + x + ' 9V16'} stroke="#fefbf3" strokeWidth="1"/>)}<path d="M19 7 Q12 2 5 7" fill="none" stroke="#e9a83a" strokeWidth="1.5"/><path d="M5 7 L7 5 M5 7 L7.4 7.8" stroke="#e9a83a" strokeWidth="1.3"/></svg>
  ),
  'mk-recipe': () => (
    <svg width="34" height="34" viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#e4572e"/><text x="12" y="10.5" textAnchor="middle" fontFamily="Georgia, serif" fontStyle="italic" fontSize="6.5" fontWeight="900" fill="#fefbf3">Allegro</text><text x="12" y="18.5" textAnchor="middle" fontFamily="Georgia, serif" fontStyle="italic" fontSize="7" fontWeight="900" fill="#e9a83a">f</text></svg>
  ),
  'mk-word': () => (\n""")
rep("""  'ledger-lines': ['ledger-walk', 'ledger-landmarks', 'ledger-twins', 'ledger-write'],""", """  'ledger-lines': ['ledger-walk', 'ledger-landmarks', 'ledger-twins', 'ledger-write', 'mk-ladders'],""")
rep("""  'signs': ['sgn-rep', 'sgn-volta', 'sgn-dc', 'sgn-ds', 'sgn-pause', 'road-map', 'dc-ds-coda', 'ottava', 'ornaments', 'grace-write'],""", """  'signs': ['sgn-rep', 'sgn-volta', 'sgn-dc', 'sgn-ds', 'sgn-pause', 'road-map', 'dc-ds-coda', 'ottava', 'ornaments', 'grace-write', 'mk-road'],""")
rep("""  'staff': ['staff-basics', 'staff-climb', 'clef-basics', 'clef-story', 'alto-clef'],""", """  'staff': ['staff-basics', 'staff-climb', 'clef-basics', 'clef-story', 'alto-clef', 'mk-lines'],""")
rep("""  'terms': ['tmx-map', 'tmx-speed', 'tmx-change', 'tmx-vol', 'tmx-touch', 'tmx-build', 'term-sort', 'term-cards', 'term-mixer', 'term-match'],""", """  'terms': ['tmx-map', 'tmx-speed', 'tmx-change', 'tmx-vol', 'tmx-touch', 'tmx-build', 'term-sort', 'term-cards', 'term-mixer', 'term-match', 'mk-recipe'],""")
rep("""lessons: ['kq-lines', 'kq-climb', 'kq-clefs', 'kq-alto'], check: 'staff' }""", """lessons: ['kq-lines', 'kq-climb', 'kq-clefs', 'kq-alto', 'mk-lines'], check: 'staff' }""")
rep("""lessons: ['kq-ledger', 'kq-middlec', 'kq-8va'], check: 'ledger-lines' }""", """lessons: ['kq-ledger', 'kq-middlec', 'kq-8va', 'mk-ladders'], check: 'ledger-lines' }""")
rep("""lessons: ['tmx-build', 'tmx-map', 'term-mixer', 'term-cards', 'term-match', 'term-sort'], check: 'terms' }""", """lessons: ['tmx-build', 'tmx-map', 'term-mixer', 'term-cards', 'term-match', 'term-sort', 'mk-recipe'], check: 'terms' }""")
rep("""lessons: ['sgn-rep', 'sgn-volta', 'sgn-dc', 'sgn-ds', 'sgn-pause', 'dc-ds-coda', 'road-map'], check: 'signs' }""", """lessons: ['sgn-rep', 'sgn-volta', 'sgn-dc', 'sgn-ds', 'sgn-pause', 'dc-ds-coda', 'road-map', 'mk-road'], check: 'signs' }""")
rep("""  set('G', 'mk-word mk-staffword mk-move mk-trick mk-steps');   // Build CE: the Beginner floor's things to make""", """  set('G', 'mk-word mk-staffword mk-move mk-trick mk-steps');   // Build CE: the Beginner floor's things to make
  set('G', 'mk-lines'); set('P1', 'mk-ladders mk-road'); set('1', 'mk-recipe');   // Build CF (P1 becomes Prelim below)""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
