import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build CN (call 28; her 13:35 and 14:34): the checks in the app.
#  - Chapter check at the end of every room: 10 quick questions spread over the room's drill parts; 8 or more passes,
#    unless every question on one part (asked at least twice) was missed. A pass puts a star on the room in the house.
#    A miss names the weak parts with a link to practise each; a retry is a fresh set (every room has a generator).
#  - Floor checkpoint under the house: 15 mixed questions, about two from each room of the floor (Beginner: two
#    checkpoints of 14, one per half). No playing, no pass mark: it lists the rooms to visit again.
#  - Review: five questions from a passed room seven days later, at the top of the house (then 30 days; a miss: 2 days).
# The parts a check may ask (CHECK_LV) are the room's own drill levels, without the tapping-in-time, clap-back, sing-a-
# long-tune and memory levels (slow, and the playing is the teacher's tick), the 'Extra' levels and levels marked for a
# later grade (key signatures: only the two levels that keep to the Grade 1 keys).

CODE = r"""
// ══ Build CN: the checks (call 28) ══
const CHECK_KEY = 'pb_checks_v1', CHECK_N = 10, CHECK_PASS = 8, FLOOR_N = 15, FLOOR_HALF_N = 14, REVIEW_N = 5, DAY_MS = 864e5;
const CHECK_LV = {
  'posture-hands': [1, 2, 3], 'first-steps': [1, 2, 3, 4, 5, 6, 7, 8], pulse: [1, 2, 4, 5], 'note-names': [1, 2, 3, 4, 5],
  'hand-positions': [1, 2, 3, 4, 5], 'ear-prep': [1, 2, 3, 4, 5], 'note-values': [1, 2, 3, 5], dynamics: [1, 2, 3, 4, 5, 6, 7, 8],
  staff: [1, 2, 3, 4, 5, 6, 7], 'reading-steps': [1, 2, 3, 4, 5, 6, 7, 8], 'whole-staff': [1, 2, 3, 4, 5, 6, 7],
  'time-signatures': [1, 2, 4, 5, 6, 7], tones: [1, 2, 3, 4, 5, 6, 7],
  'listen-sing': [1, 2, 3], tempo: [1, 2, 3, 4, 5, 6, 7, 8], rhythm: [1, 2, 3, 4, 5, 6], 'ledger-lines': [1, 2, 3, 4, 5, 7],
  scales: [1, 2, 3, 5, 6, 63, 64, 9], 'scale-play': [1, 2, 3, 4, 5, 6], 'minor-scales': [1, 2, 3, 4, 5, 6], signs: [1, 2, 3, 4, 5, 6, 7, 8],
  'listen-write': [1, 2, 3], accidentals: [1, 2, 3, 4, 5, 6, 7, 8], 'key-signatures': [2, 6], terms: [1, 2, 3, 4, 5, 6, 7, 8],
  'six-eight': [1, 2, 3, 4, 5], intervals: [1, 3, 2, 4, 6, 8, 5, 7], chords: [1, 2, 4, 6, 3, 5, 7, 8, 10], form: [1, 2, 3, 4, 5, 6, 7, 8],
  'listen-23': [1], 'listen-3': [1, 2, 3], melody: [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12], 'scales-23': [1, 2, 3, 4, 5],
  'harmony-23': [1, 2, 3, 4, 5, 6], 'rhythm-23': [1, 2, 3, 4, 5, 6],
  'listen-4': [1, 2, 3], 'scales-4': [1, 2, 3, 4, 5], 'keys-4': [1, 2, 3, 4, 5, 6], 'harmony-4': [1, 2, 3, 4], 'rhythm-4': [1, 2, 3, 4],
  'listen-5': [1, 2, 3], 'scales-5': [1, 2, 3, 4, 5], 'keys-5': [1, 2, 3, 4, 5], 'harmony-5': [1, 2, 3, 4, 5],
  'listen-6': [1, 2, 3, 4], 'scales-6': [1, 2, 3, 4, 5, 6], 'arps-6': [1, 2, 3, 4], 'harmony-6': [1, 2, 3, 4, 5],
  'listen-7': [1, 2, 4], 'scales-7': [1, 2, 3, 4, 5, 6], 'arps-7': [1, 2, 3, 4], 'pieces-78': [1, 2, 3, 4],
  'listen-8': [1, 2, 4], 'scales-8': [1, 2, 3, 4, 5], 'arps-8': [1, 2, 3, 4],
  'piano-story': [1, 2, 3, 4, 5, 6, 7, 8], 'pitch-range': [1, 2, 3, 4, 5, 6, 7], composers: [1, 2, 3, 4, 5, 6, 7, 8], styles: [1, 2, 3, 4, 5, 6, 7, 8],
};
function loadChecks() { try { const v = JSON.parse(localStorage.getItem(CHECK_KEY)); if (v && typeof v === 'object') return { rooms: v.rooms || {}, floors: v.floors || {} }; } catch (e) {} return { rooms: {}, floors: {} }; }
function saveChecks(c) { try { localStorage.setItem(CHECK_KEY, JSON.stringify(c)); } catch (e) {} }
function chkConcept(id) { const d = DRILLS.find(x => x.id === id); return d && d.concept && d.concept.generate ? d.concept : null; }
function chkLevels(id) { const c = chkConcept(id); return c ? (CHECK_LV[id] || []).map(n => c.levels.find(l => l.n === n)).filter(Boolean) : []; }
function chkShuffle(a) { a = a.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); const x = a[i]; a[i] = a[j]; a[j] = x; } return a; }
function chkItems(id, n) { const lv = chkLevels(id), out = []; let pool = []; while (out.length < n && lv.length) { if (!pool.length) pool = chkShuffle(lv); out.push({ id, lv: pool.shift() }); } return out; }   // every part once before any part twice
function chkFloorItems(ids, n) { const rooms = chkShuffle(ids.filter(id => chkLevels(id).length)); return chkShuffle(rooms.flatMap((id, i) => chkItems(id, Math.floor(n / rooms.length) + (i < n % rooms.length ? 1 : 0)))); }
function checkFloors() {   // the checkpoints: one per grade floor; a floor of more than ten rooms has two, one per half
  const out = [];
  PATH_STAGES.forEach((st, k) => { if (stageExtra(st)) return; const ids = pathStageIds(st).filter(id => CHECK_LV[id]); if (!ids.length) return;
    if (ids.length > 10) { const h = Math.ceil(ids.length / 2); out.push({ key: k + 'a', k, ids: ids.slice(0, h), part: 1 }); out.push({ key: k + 'b', k, ids: ids.slice(h), part: 2 }); }
    else out.push({ key: String(k), k, ids }); });
  return out;
}
const chkFloorName = (f) => floorName(f.k) + (f.part ? (f.part === 1 ? t(', first half', ', 앞 절반') : t(', second half', ', 뒤 절반')) : '');
const chkDate = (ts) => { try { return new Date(ts).toLocaleDateString(LANG === 'ko' ? 'ko-KR' : 'en-AU', { day: 'numeric', month: 'short' }); } catch (e) { return ''; } };
const chkLvLabel = (id, n) => { const c = chkConcept(id), l = c && c.levels.find(x => x.n === n); return l ? lvName(typeof l.label === 'string' ? l.label : t(l.label[0], l.label[1])) : ''; };
const chkPracticeHref = (id, n) => '?drill=' + id + '&level=' + n + '&tab=drill' + (LANG === 'ko' ? '&lang=ko' : '');
function chkStarD(cx, cy, r) { let d = ''; for (let i = 0; i < 10; i++) { const a = -Math.PI / 2 + i * Math.PI / 5, rr = i % 2 ? r * 0.45 : r; d += (i ? 'L' : 'M') + (cx + rr * Math.cos(a)).toFixed(2) + ' ' + (cy + rr * Math.sin(a)).toFixed(2); } return d + 'Z'; }
const ChkStar = ({ size = 22, fill = '#2e8a6e' }) => <svg viewBox="0 0 24 24" width={size} height={size} aria-hidden="true" style={{flex:'0 0 auto',display:'block'}}><path d={chkStarD(12, 12.6, 11)} fill={fill}/></svg>;
function CheckStamp({ text, color }) {   // the stamp at the end of a round
  return <svg viewBox="0 0 120 120" width="108" height="108" aria-hidden="true" style={{display:'block',margin:'2px auto 4px',transform:'rotate(-8deg)'}}>
    <circle cx="60" cy="60" r="53" fill="#fff" stroke={color} strokeWidth="4.5"/><circle cx="60" cy="60" r="45" fill="none" stroke={color} strokeWidth="1.4" strokeDasharray="3 3"/>
    <path d={chkStarD(60, 36, 9)} fill={color}/>
    <text x="60" y="72" textAnchor="middle" fontFamily="'Playfair Display', Georgia, serif" fontWeight="900" fontSize={text.length > 6 ? 17 : 21} fill={color} letterSpacing="1">{text}</text>
    <path d={chkStarD(36, 88, 4)} fill={color} opacity="0.6"/><path d={chkStarD(84, 88, 4)} fill={color} opacity="0.6"/>
  </svg>;
}
const chkKicker = { fontSize:11.5, fontWeight:900, color:'#e4572e', letterSpacing:'0.1em', textTransform:'uppercase', margin:'0 0 3px' };
const chkBox = (pass) => ({ margin:'14px 0 0', padding:'12px', border:'1.5px solid ' + (pass ? '#2e8a6e' : 'rgba(38,41,107,0.28)'), borderRadius:10, background:'#fff' });

// One round: the questions come from each room's own drill (generate, check, answerLabel, Question).
function CheckRun({ items, floor, onDone, onQuit }) {
  const [qs] = useState(() => { const prev = {}; return items.map(it => { const c = chkConcept(it.id), k = it.id + '|' + it.lv.n; let q = null; try { q = c.generate(it.lv, prev[k] || null); } catch (e) { q = null; } if (q) prev[k] = q; return q; }); });
  const list = items.map((it, j) => ({ ...it, q: qs[j] })).filter(x => x.q);
  const [i, setI] = useState(0), [given, setGiven] = useState(null), [res, setRes] = useState([]), [streak, setStreak] = useState(0);
  const timer = useRef(null);
  useEffect(() => () => clearTimeout(timer.current), []);
  const it = list[i], drill = it && chkConcept(it.id);
  const next = (r) => { clearTimeout(timer.current); try { stopClicks(); } catch (e) {} if (i + 1 >= list.length) { onDone(r); return; } setGiven(null); setI(i + 1); };
  const answer = (ans, force) => {
    if (given || !it) return;
    let ok = false; if (force != null) ok = !!force; else { try { ok = ans !== null && ans !== undefined && !!drill.check(it.q, ans); } catch (e) { ok = false; } }
    const r = res.concat([{ id: it.id, n: it.lv.n, ok }]);
    setRes(r); setGiven({ ans, ok, timedOut: false }); setStreak(x => ok ? x + 1 : 0);
    if (ok) timer.current = setTimeout(() => next(r), 1100);
  };
  useEffect(() => { window.__pbCheckForce = (ok) => answer(null, !!ok); });
  useEffect(() => () => { try { delete window.__pbCheckForce; } catch (e) {} }, []);
  if (!it) return null;
  const Q = drill.Question, right = res.filter(x => x.ok).length;
  const fb = <div style={{minHeight:40,margin:drill.feedbackAbove ? '4px 0 6px' : '12px 0 0',textAlign:'center',order:1}}>{given && <DrillFeedback given={given} isGame={false} drill={drill} q={it.q}/>}</div>;
  const qProps = { q: it.q, level: it.lv, given, locked: !!given, onAnswer: (a) => answer(a), pixel: false, stats: { correct: right, asked: res.length, streak } };
  return <div data-testid="check-run" data-q={i + 1} data-n={list.length} style={{marginTop:10}}>
    <div style={{display:'flex',justifyContent:'space-between',alignItems:'baseline',gap:8,fontSize:13,fontWeight:800,color:'var(--muted)',margin:'0 0 8px'}}>
      <span>{t('Question ', '문제 ') + (i + 1) + ' / ' + list.length}</span>
      <span style={{color:streak >= 2 ? '#e4572e' : 'var(--muted)'}}>{streak >= 2 ? t(streak + ' in a row!', streak + '개 연속!') : t(right + ' right', right + '개 맞힘')}</span>
    </div>
    {floor && <div style={{...chkKicker,margin:'0 0 6px'}}>{bkChapterNo(it.id) + ' · ' + bkChapterName(it.id)}</div>}
    <div key={i} className="card" style={{padding:16}}>
      {drill.feedbackAbove ? <div style={{display:'flex',flexDirection:'column'}}><Q {...qProps} fbAbove/>{fb}</div> : <><Q {...qProps}/>{fb}</>}
      {given && <button className="primary-btn" style={{marginTop:10}} onClick={() => next(res)}>{i + 1 >= list.length ? t('See how I did →', '결과 보기 →') : t('Next →', '다음 →')}</button>}
    </div>
    <button className="ghost-btn" style={{marginTop:8,fontSize:13}} onClick={() => { clearTimeout(timer.current); try { stopClicks(); } catch (e) {} onQuit(); }}>{t('Stop the check', '그만하기')}</button>
  </div>;
}
function chkWeakChips(id, ns) {
  return <div style={{display:'flex',flexWrap:'wrap',gap:6,justifyContent:'center',margin:'6px 0 2px'}}>{ns.map(n => <a key={n} className="chip" href={chkPracticeHref(id, n)} style={{textDecoration:'none',minHeight:40,display:'inline-flex',alignItems:'center',whiteSpace:'normal',textAlign:'left',fontSize:13.5}}>{chkLvLabel(id, n)} ›</a>)}</div>;
}
// The chapter check, at the end of every room
function RoomCheckCard({ id }) {
  const [mode, setMode] = useState('idle'), [items, setItems] = useState(null), [out, setOut] = useState(null), [, setTick] = useState(0);
  const box = useRef(null);
  if (!chkLevels(id).length) return null;
  const rec = loadChecks().rooms[id] || {};
  const start = () => { setItems(chkItems(id, CHECK_N)); setOut(null); setMode('run'); setTimeout(() => { try { box.current.scrollIntoView({ behavior: 'smooth', block: 'start' }); } catch (e) {} }, 60); };
  const done = (r) => {
    const right = r.filter(x => x.ok).length, by = {};
    r.forEach(x => { (by[x.n] = by[x.n] || []).push(x.ok); });
    const lost = Object.keys(by).filter(n => by[n].length >= 2 && by[n].every(v => !v)).map(Number);
    const pass = right >= Math.min(CHECK_PASS, r.length) && !lost.length, weak = [...new Set(r.filter(x => !x.ok).map(x => x.n))];
    const c = loadChecks(), o = c.rooms[id] || {}, now = Date.now(), first = pass && !o.pass;
    o.last = right; o.best = Math.max(o.best || 0, right); o.tries = (o.tries || 0) + 1;
    if (first) { o.pass = now; o.review = { due: now + 7 * DAY_MS, stage: 1 }; }
    c.rooms[id] = o; saveChecks(c);
    setOut({ right, total: r.length, pass, lost, weak, first }); setMode('done'); setTick(x => x + 1);
  };
  return <div ref={box} data-testid="room-check" data-pass={rec.pass ? '1' : '0'} style={chkBox(rec.pass)}>
    <div style={chkKicker}>{t('Chapter check', '챕터 체크')}</div>
    {mode === 'idle' && <>
      <div style={{display:'flex',alignItems:'center',gap:10}}>
        <div style={{flex:1,minWidth:0}}>
          <div style={{fontSize:16,fontWeight:900,color:'#26296b',lineHeight:1.3}}>{t('10 quick questions. Get 8 and this room gets a star.', '빠른 10문제. 8개 맞히면 이 방에 별이 붙어요.')}</div>
          <div style={{fontSize:13,color:'#4a4d86',marginTop:3,lineHeight:1.4}}>{rec.pass ? t('Passed on ' + chkDate(rec.pass) + ' · best ' + rec.best + ' of 10', chkDate(rec.pass) + ' 통과 · 최고 10개 중 ' + rec.best + '개') : rec.tries ? t('Best so far: ' + rec.best + ' of 10', '지금까지 최고: 10개 중 ' + rec.best + '개') : t('No help and no piano. About three minutes.', '도움 없이, 피아노 없이. 3분쯤 걸려요.')}</div>
        </div>
        {rec.pass && <ChkStar size={30}/>}
      </div>
      <button className="primary-btn" data-testid="room-check-start" style={{marginTop:10}} onClick={start}>{rec.pass ? t('Do it again →', '다시 해 보기 →') : t('Start the check →', '체크 시작 →')}</button>
    </>}
    {mode === 'run' && items && <CheckRun key={'r' + (rec.tries || 0)} items={items} onDone={done} onQuit={() => setMode('idle')}/>}
    {mode === 'done' && out && <div data-testid="check-result" data-pass={out.pass ? '1' : '0'} data-right={out.right} style={{textAlign:'center',padding:'4px 0 2px'}}>
      {out.pass ? <CheckStamp text={t('PASSED', '통과!')} color="#2e8a6e"/> : null}
      <div style={{fontSize:40,fontWeight:900,color:'#26296b',lineHeight:1.1}}>{out.right}<span style={{fontSize:20,color:'var(--muted)'}}> / {out.total}</span></div>
      {out.pass ? <>
        <div style={{fontSize:17,fontWeight:900,color:'#2e8a6e',margin:'4px 0 2px'}}>{out.right === out.total ? t('Every one right! A star for this room.', '모두 맞혔어요! 이 방에 별이 붙었어요.') : t('A star for this room!', '이 방에 별이 붙었어요!')}</div>
        {out.first && <div style={{fontSize:13.5,color:'#4a4d86',lineHeight:1.45}}>{t('In a week, five quick questions will check it stuck.', '일주일 뒤에 빠른 5문제로 잘 남았는지 봐요.')}</div>}
      </> : <>
        <div style={{fontSize:17,fontWeight:900,color:'#e4572e',margin:'4px 0 2px'}}>{out.lost.length && out.right >= CHECK_PASS ? t('So close! But one part was missed every time.', '아깝다! 한 부분을 모두 틀렸어요.') : out.right === CHECK_PASS - 1 ? t('So close!', '아깝다!') : t('Not yet. Once more?', '아직이에요. 한 번 더?')}</div>
        <div style={{fontSize:13.5,color:'#4a4d86',lineHeight:1.45}}>{t('Practise these, then try again:', '이걸 연습하고 다시 해 봐요:')}</div>
        {chkWeakChips(id, out.lost.length ? out.lost : out.weak)}
      </>}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:10}}>
        <button className="primary-btn" style={{width:'auto',padding:'10px 16px'}} onClick={start}>{out.pass ? t('Again: new questions', '다시: 새 문제') : t('Try again: new questions →', '다시 하기: 새 문제 →')}</button>
        <button className="ghost-btn" style={{width:'auto'}} onClick={() => setMode('idle')}>{t('Close', '닫기')}</button>
      </div>
    </div>}
  </div>;
}
// The floor checkpoints, under the house
function FloorCheckCard({ here, onOpen }) {
  const floors = checkFloors(), hereF = Math.max(0, floors.findIndex(f => f.ids.includes(here)));
  const [sel, setSel] = useState(hereF), [mode, setMode] = useState('idle'), [items, setItems] = useState(null), [out, setOut] = useState(null), [, setTick] = useState(0);
  const box = useRef(null);
  const f = floors[sel]; if (!f) return null;
  const N = f.part ? FLOOR_HALF_N : FLOOR_N, c = loadChecks(), rec = c.floors[f.key];
  const nDone = f.ids.filter(id => chapterState(id).status === 'done').length;
  const nm = (id) => bkChapterNo(id) + ' · ' + bkChapterName(id);
  const start = () => { setItems(chkFloorItems(f.ids, N)); setOut(null); setMode('run'); setTimeout(() => { try { box.current.scrollIntoView({ behavior: 'smooth', block: 'start' }); } catch (e) {} }, 60); };
  const done = (r) => {
    const per = {}; r.forEach(x => { const p = per[x.id] = per[x.id] || { right: 0, n: 0, miss: [] }; p.n++; if (x.ok) p.right++; else p.miss.push(x.n); });
    const right = r.filter(x => x.ok).length, review = f.ids.filter(id => per[id] && per[id].miss.length);
    const cc = loadChecks(); cc.floors[f.key] = { at: Date.now(), right, total: r.length, review }; saveChecks(cc);
    setOut({ right, total: r.length, per, review }); setMode('done'); setTick(x => x + 1);
  };
  const chip = (g, j) => { const rr = c.floors[g.key], ok = rr && !rr.review.length;
    return <button key={g.key} className={'chip' + (j === sel ? ' active' : '')} disabled={mode === 'run'} onClick={() => { setSel(j); setMode('idle'); setOut(null); }} style={{fontSize:12.5,padding:'4px 10px',minHeight:34}}>{(ok ? '✓ ' : '') + (LANG === 'ko' ? PATH_STAGES[g.k].ko[0] : PATH_STAGES[g.k].en[0]) + (g.part ? ' ' + g.part : '')}</button>; };
  return <div ref={box} data-testid="floor-check" data-floor={f.key} style={{...chkBox(false),maxWidth:440,margin:'18px auto 0',textAlign:'left'}}>
    <div style={chkKicker}>{t('Floor checkpoint', '층 중간점검')}</div>
    <div style={{display:'flex',flexWrap:'wrap',gap:5,margin:'4px 0 8px'}}>{floors.map(chip)}</div>
    {mode === 'idle' && <>
      <div style={{fontSize:16,fontWeight:900,color:'#26296b',lineHeight:1.3}}>{chkFloorName(f)}</div>
      <div style={{fontSize:13.5,color:'#4a4d86',lineHeight:1.45,margin:'3px 0 0'}}>{t(N + ' mixed questions from its ' + f.ids.length + ' rooms (' + bkChapterNo(f.ids[0]) + '–' + bkChapterNo(f.ids[f.ids.length - 1]) + '). No playing and no pass mark: it shows which rooms to visit again.', '방 ' + f.ids.length + '개(' + bkChapterNo(f.ids[0]) + '~' + bkChapterNo(f.ids[f.ids.length - 1]) + '번)에서 섞은 ' + N + '문제. 연주도, 통과 점수도 없어요: 다시 가 볼 방을 알려 줘요.')}</div>
      <div style={{fontSize:13,color:'#6d6f9c',fontWeight:700,margin:'4px 0 0'}}>{rec ? t('Last time (' + chkDate(rec.at) + '): ' + rec.right + ' of ' + rec.total + (rec.review.length ? ' · rooms to visit again: ' + rec.review.length : ' · nothing to review'), '지난번(' + chkDate(rec.at) + '): ' + rec.total + '개 중 ' + rec.right + '개' + (rec.review.length ? ' · 다시 가 볼 방 ' + rec.review.length + '개' : ' · 복습할 방 없음')) : nDone === f.ids.length ? t('Every room on it is done: ready!', '방을 모두 끝냈어요: 준비 완료!') : t(nDone + ' of ' + f.ids.length + ' rooms done. You can try it any time.', '방 ' + f.ids.length + '개 중 ' + nDone + '개 완료. 언제든 해 볼 수 있어요.')}</div>
      <button className="primary-btn" data-testid="floor-check-start" style={{marginTop:10}} onClick={start}>{t('Start the checkpoint →', '중간점검 시작 →')}</button>
    </>}
    {mode === 'run' && items && <CheckRun key={'f' + f.key + (rec ? rec.at : 0)} items={items} floor onDone={done} onQuit={() => setMode('idle')}/>}
    {mode === 'done' && out && <div data-testid="floor-result" data-right={out.right} data-review={out.review.length} style={{textAlign:'center'}}>
      <CheckStamp text={t('DONE', '끝!')} color="#26296b"/>
      <div style={{fontSize:36,fontWeight:900,color:'#26296b',lineHeight:1.1}}>{out.right}<span style={{fontSize:18,color:'var(--muted)'}}> / {out.total}</span></div>
      <div style={{fontSize:15,fontWeight:900,color:out.review.length ? '#e4572e' : '#2e8a6e',margin:'4px 0 8px'}}>{out.review.length ? t('Rooms to visit again:', '다시 가 볼 방:') : t('Everything stuck. On to the next floor!', '모두 잘 남았어요. 다음 층으로!')}</div>
      <div style={{display:'grid',gap:4,textAlign:'left'}}>{f.ids.filter(id => out.per[id]).map(id => { const p = out.per[id], miss = p.miss.length > 0;
        return <div key={id} style={{display:'flex',alignItems:'center',gap:8,fontSize:14,minHeight:36,borderTop:'1px solid rgba(38,41,107,0.1)'}}>
          <span style={{flex:1,minWidth:0,color:'#26296b',fontWeight:700}}>{nm(id)}</span>
          <span style={{fontWeight:900,color:miss ? '#e4572e' : '#2e8a6e'}}>{p.right + '/' + p.n}</span>
          {miss ? <button className="chip" style={{fontSize:12.5,minHeight:34}} onClick={() => onOpen(id)}>{t('Visit again ›', '다시 가기 ›')}</button> : <span style={{color:'#2e8a6e',fontWeight:900,width:20,textAlign:'center'}}>✓</span>}
        </div>; })}</div>
      <button className="ghost-btn" style={{marginTop:10}} onClick={() => setMode('idle')}>{t('Close', '닫기')}</button>
    </div>}
  </div>;
}
// The review: a passed room comes back after seven days (then a month); at the top of the house
function chkDueReview() { const c = loadChecks(), now = Date.now(), ids = pathIds(); return Object.keys(c.rooms).filter(id => ids.includes(id) && c.rooms[id].review && c.rooms[id].review.due <= now && chkLevels(id).length).sort((a, b) => c.rooms[a].review.due - c.rooms[b].review.due)[0] || null; }
function ReviewCard() {
  const [id] = useState(() => chkDueReview());
  const [mode, setMode] = useState('idle'), [items, setItems] = useState(null), [out, setOut] = useState(null);
  if (!id) return null;
  const rec = loadChecks().rooms[id] || {}, stage = rec.review ? rec.review.stage : 1;
  const start = () => { setItems(chkItems(id, REVIEW_N)); setMode('run'); };
  const done = (r) => {
    const right = r.filter(x => x.ok).length, pass = right === r.length, now = Date.now(), c = loadChecks(), o = c.rooms[id] || {};
    o.review = pass ? (stage >= 2 ? { due: 9e15, stage: 3, kept: now } : { due: now + 30 * DAY_MS, stage: 2 }) : { due: now + 2 * DAY_MS, stage };
    c.rooms[id] = o; saveChecks(c);
    setOut({ right, total: r.length, pass, stage, weak: [...new Set(r.filter(x => !x.ok).map(x => x.n))] }); setMode('done');
  };
  return <div data-testid="review-card" data-room={id} style={{...chkBox(false),maxWidth:440,margin:'0 auto 12px',textAlign:'left',borderColor:'#e4572e'}}>
    <div style={chkKicker}>{t('Review time', '복습 시간')}</div>
    {mode === 'idle' && <>
      <div style={{fontSize:16,fontWeight:900,color:'#26296b',lineHeight:1.3}}>{bkChapterNo(id) + ' · ' + bkChapterName(id)}</div>
      <div style={{fontSize:13.5,color:'#4a4d86',lineHeight:1.45,margin:'3px 0 0'}}>{stage === 1 ? t('You passed it a week ago. Five quick questions: did it stick?', '일주일 전에 통과한 방이에요. 빠른 5문제: 잘 남았나요?') : t('A month on: five quick questions, all five to keep it.', '한 달 뒤: 빠른 5문제, 다섯 개 모두 맞히면 끝.')}</div>
      <button className="primary-btn" data-testid="review-start" style={{marginTop:10}} onClick={start}>{t('Start the review →', '복습 시작 →')}</button>
    </>}
    {mode === 'run' && items && <CheckRun items={items} onDone={done} onQuit={() => setMode('idle')}/>}
    {mode === 'done' && out && <div data-testid="review-result" data-pass={out.pass ? '1' : '0'} style={{textAlign:'center'}}>
      {out.pass && <CheckStamp text={t('KEPT', '기억!')} color="#2e8a6e"/>}
      <div style={{fontSize:36,fontWeight:900,color:'#26296b',lineHeight:1.1}}>{out.right}<span style={{fontSize:18,color:'var(--muted)'}}> / {out.total}</span></div>
      <div style={{fontSize:15,fontWeight:900,color:out.pass ? '#2e8a6e' : '#e4572e',margin:'4px 0 4px'}}>{out.pass ? (out.stage >= 2 ? t('It stuck for good!', '완전히 내 것이 됐어요!') : t('It stuck! See you in a month.', '잘 남았어요! 한 달 뒤에 또 봐요.')) : t('A little has slipped. Practise this, and it comes back in two days:', '조금 잊었어요. 이걸 연습하면, 이틀 뒤에 다시 와요:')}</div>
      {!out.pass && chkWeakChips(id, out.weak)}
    </div>}
  </div>;
}
"""

# the engine and the cards go in before the Lesson component
rep("""function Lesson({ id, title, intro, children, onStart, startLabel, head, noArt }) {""", CODE + """
function Lesson({ id, title, intro, children, onStart, startLabel, head, noArt }) {""")
# the chapter check at the end of every room, above Start the drill
rep("""      <LessonMore id={id}/>
      {onStart && <button className="primary-btn" style={{marginTop:16}} onClick={onStart}>{startLabel || t('Start the drill →', '드릴 시작하기 →')}</button>}""",
    """      <LessonMore id={id}/>
      <RoomCheckCard id={id}/>
      {onStart && <button className="primary-btn" style={{marginTop:16}} onClick={onStart}>{startLabel || t('Start the drill →', '드릴 시작하기 →')}</button>}""")
# the house: a green star on a room whose check is passed
rep("""  if (lines[1]) s += stT(cx, sy + 27, lines[1], { size: nz, weight: 700, font: TH_SERIF, fill: nfill, anchor: 'middle' });
  const ic = HOUSE_ICONS[id];""", """  if (lines[1]) s += stT(cx, sy + 27, lines[1], { size: nz, weight: 700, font: TH_SERIF, fill: nfill, anchor: 'middle' });
  const star = view.star && view.star[id];   // Build CN: the chapter check passed
  if (star) s += '<path d="' + chkStarD(x + w - (cmp ? 9 : 12), y + h - 6 - (cmp ? 8 : 11), cmp ? 5.5 : 7.5) + '" fill="' + ST.G + '" stroke="#fff" stroke-width="0.8"/>';
  const ic = HOUSE_ICONS[id];""")
rep("""  const label = num + '. ' + t(nm[0], nm[1] || nm[0]) + (done ? t(', done', ', 완료') : on ? t(', you are here', ', 지금 여기') : '');""",
    """  const label = num + '. ' + t(nm[0], nm[1] || nm[0]) + (done ? t(', done', ', 완료') : on ? t(', you are here', ', 지금 여기') : '') + (star ? t(', check passed', ', 체크 통과') : '');""")
rep("""  const sig = stages.map(x => x.st.join(',')).join('|') + here + LANG + compact + name + today + fontTick + wide + (topic || '');
  const view = { stages, here, nums, focus: topic, pawn: name ? (x, y, k) => stPiece(VIC_PAWN_NAVY, x, y, k) : null };""",
    """  const chkRooms = loadChecks().rooms, star = {}; Object.keys(chkRooms).forEach(id => { if (chkRooms[id].pass) star[id] = 1; });   // Build CN
  const sig = stages.map(x => x.st.join(',')).join('|') + here + LANG + compact + name + today + fontTick + wide + (topic || '') + Object.keys(star).join(',');
  const view = { stages, here, nums, focus: topic, star, pawn: name ? (x, y, k) => stPiece(VIC_PAWN_NAVY, x, y, k) : null };""")
# the review at the top of the house, the floor checkpoints under it
rep("""        {weekEl && <div style={{marginBottom:14,maxWidth:440}}>{weekEl}</div>}""",
    """        {weekEl && <div style={{marginBottom:14,maxWidth:440}}>{weekEl}</div>}
        {!compact && <ReviewCard/>}""")
rep("""                {peek && (() => { const k = stages.findIndex(x => x.ids.includes(peek)); return <RoomPeek id={peek} num={nums[peek]} floor={k >= 0 ? floorName(k) : ''} onGo={() => { const c = peek; setPeek(null); onOpen(c); }} onClose={() => setPeek(null)}/>; })()}</>""",
    """                {peek && (() => { const k = stages.findIndex(x => x.ids.includes(peek)); return <RoomPeek id={peek} num={nums[peek]} floor={k >= 0 ? floorName(k) : ''} onGo={() => { const c = peek; setPeek(null); onOpen(c); }} onClose={() => setPeek(null)}/>; })()}
                {!compact && <FloorCheckCard here={here} onOpen={onOpen}/>}</>""")
# the room's card in the house says whether its check is passed
rep("""          <div style={{fontSize:12,fontWeight:800,color:BK.muted,marginTop:2}}>{floor}{steps.length ? ' · ' + t(nDone + ' of ' + steps.length + ' steps done', steps.length + '단계 중 ' + nDone + '단계 완료') : ''}</div>""",
    """          <div style={{fontSize:12,fontWeight:800,color:BK.muted,marginTop:2}}>{floor}{steps.length ? ' · ' + t(nDone + ' of ' + steps.length + ' steps done', steps.length + '단계 중 ' + nDone + '단계 완료') : ''}</div>
          {CHECK_LV[id] && <div data-testid="peek-check" style={{fontSize:12,fontWeight:800,color:(loadChecks().rooms[id] || {}).pass ? '#2e8a6e' : BK.muted,marginTop:1}}>{(loadChecks().rooms[id] || {}).pass ? '★ ' + t('Chapter check passed', '챕터 체크 통과') : t('Chapter check: not yet', '챕터 체크: 아직')}</div>}""")

open(dst, 'w', encoding='utf-8').write(s)
print('ok')
