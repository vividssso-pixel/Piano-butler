import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build BT (board call 26, the first Grade 7 room): Hear and Sing, Grade 7. The Grade 7 aural tests (Manual 2026, section 21):
# any major or minor triad, root position or an inversion, within an octave: major or minor, and its position; perfect, plagal
# and interrupted cadences in a major key as they occur in a short piece, the tonic chord first; about one minute to memorise a
# two-bar phrase from a printed copy, away from the instrument, then play or sing it (the keynote sounded first); the higher or
# lower part of a two-part phrase of not more than six notes, note against note, within an octave from middle C, hummed or sung.
# Every step has an easier rung first (call 25). The thing to make: a tune of my own to remember. The phrases are our own.

rep("""const LISTEN_6_DRILL = { id: 'listen-6', label: 'Hear and Sing, Grade 6', noPrint: true };   // Build BO""",
    """const LISTEN_6_DRILL = { id: 'listen-6', label: 'Hear and Sing, Grade 6', noPrint: true };   // Build BO
const LISTEN_7_DRILL = { id: 'listen-7', label: 'Hear and Sing, Grade 7', noPrint: true };   // Build BT""")
rep("""  { id: 'listen-6', label: 'Hear and Sing, Grade 6', concept: LISTEN_6_DRILL, track: 'start' },   // Build BO""",
    """  { id: 'listen-6', label: 'Hear and Sing, Grade 6', concept: LISTEN_6_DRILL, track: 'start' },   // Build BO
  { id: 'listen-7', label: 'Hear and Sing, Grade 7', concept: LISTEN_7_DRILL, track: 'start' },   // Build BT""")
rep("""'listen-6': '듣고 부르기, Grade 6'""", """'listen-6': '듣고 부르기, Grade 6', 'listen-7': '듣고 부르기, Grade 7'""")
rep("""'listen-6': ['listen-5']""", """'listen-6': ['listen-5'], 'listen-7': ['listen-6']""")
rep("""'listen-6': ['Hear & sing 6', '듣기 6']""", """'listen-6': ['Hear & sing 6', '듣기 6'], 'listen-7': ['Hear & sing 7', '듣기 7']""")
rep("""  'listen-6': 'aural ear grade 6""", """  'listen-7': 'aural ear grade 7 triad major minor position inversion cadence perfect plagal interrupted memory memorise phrase two bars printed sing play six notes two-part higher lower part',
  'listen-6': 'aural ear grade 6""")
rep("""id === 'listen-5' || id === 'listen-6') return 'aural';""", """id === 'listen-5' || id === 'listen-6' || id === 'listen-7') return 'aural';""")
# the house: the Grade 7 floor above Grade 6; its rooms appear as they are built
rep("""  { ids: ['piano-story', 'pitch-range', 'composers', 'styles'], stories: true,""",
    """  { ids: ['listen-7', 'scales-7', 'arps-7', 'pieces-78'], en: ['Grade 7', 'Your ears, scales, arpeggios and chord walks, and knowing your pieces.'], ko: ['Grade 7', '귀, 스케일, 아르페지오와 화음 진행, 그리고 내 곡 알기.'] },   // Build BT: the Grade 7 floor (call 26)
  { ids: ['piano-story', 'pitch-range', 'composers', 'styles'], stories: true,""")

CH = r'''
// ─── Chapter: Hear and Sing, Grade 7 (Build BT, 2026-10-28; board call 26, the first Grade 7 room) ───
// ── step 3: remember a two-bar phrase: look (with a clock), then play it back from memory. Phrases are { k: keynote (semitones
// from middle C), beats, n: [{ d (staff step, middle C = 28), dur, acc }] }, written for this app ──
const L7_MEM = [
  { k: 0, beats: 4, n: [[28, 1], [29, 1], [30, 1], [31, 1], [32, 2], [30, 2]] },
  { k: 0, beats: 4, n: [[32, 1], [30, 1], [31, 1], [29, 1], [30, 1.5], [29, .5], [28, 2]] },
  { k: 7, beats: 4, n: [[32, 1], [33, 1], [34, 1], [32, 1], [36, 2], [34, 2]] },
  { k: 7, beats: 3, n: [[29, 1], [32, 1], [33, 1], [34, 1.5], [33, .5], [32, 1]] },
  { k: 5, beats: 4, n: [[31, 1], [33, 1], [35, 1], [33, 1], [34, 1, -1], [32, 1], [31, 2]] },
  { k: 2, beats: 4, n: [[29, 1], [31, 1, 1], [33, 1], [31, 1, 1], [30, 1], [28, 1, 1], [29, 2]] },
  { k: 0, beats: 3, n: [[30, 1], [32, 1], [35, 1], [34, 2], [32, 1]] },
  { k: 5, beats: 3, n: [[28, 1], [31, 1], [33, 1], [32, 2], [31, 1]] },
  { k: 7, beats: 4, n: [[34, 1], [33, 1], [32, 1], [31, 1, 1], [32, 2], [29, 2]] },
  { k: 2, beats: 3, n: [[33, 1], [31, 1, 1], [29, 1], [30, 1], [31, 1, 1], [29, 1]] },
];
const L7_KN = { 0: 'C', 7: 'G', 5: 'F', 2: 'D', '-2': 'B♭', 9: 'A', 4: 'E', '-3': 'A', 3: 'E♭' };
const memSemi = (x) => hpSemi(x[0]) + (x[2] || 0);
const memNotes = (P) => P.n.map(x => ({ d: x[0], dur: x[1], acc: x[2] || 0 }));
const memW = (P, min = 330) => Math.max(min, P.n.reduce((a, x) => a + x[1], 0) * (P.n.some(x => x[1] < 1) ? 46 : 30) + 80);   // the staff spaces notes by length: give quavers room
const memPlay = (P, bpm = 80, key = true) => { const ev = []; let at = 0; if (key) { ev.push({ at: 0, keys: [P.k > 4 ? P.k - 12 : P.k], len: 1.6, vol: 0.14 }); at = 2.5; }
  P.n.forEach(x => { ev.push({ at, keys: [memSemi(x)], len: x[1] * 0.92, vol: 0.15 }); at += x[1]; }); return spPlay(ev, bpm); };
const memLetter = (x) => ['C', 'D', 'E', 'F', 'G', 'A', 'B'][((x[0] - 28) % 7 + 7) % 7] + (x[2] === 1 ? '♯' : x[2] === -1 ? '♭' : '');
function L7MemPad({ onResult, fixed, set = L7_MEM, secs = 60, bars = 2, g = 7 }) {
  const [i, setI] = useState(fixed ? fixed.i : 0), [phase, setPhase] = useState('ready'), [left, setLeft] = useState(secs), [hear, setHear] = useState(!fixed), [got, setGot] = useState(0), [miss, setMiss] = useState(0), [wrong, setWrong] = useState(null);
  const P = set[i], N = P.n.length, done = got >= N, tm = useRef(null);
  const stopT = () => { if (tm.current) { clearInterval(tm.current); tm.current = null; } };
  useEffect(() => () => stopT(), []);
  const look = () => { stopT(); setGot(0); setMiss(0); setWrong(null); setPhase('look'); setLeft(secs); spPlay([{ at: 0, keys: [P.k > 4 ? P.k - 12 : P.k], len: 1.6, vol: 0.14 }], 80);
    tm.current = setInterval(() => setLeft(v => { if (v <= 1) { stopT(); setPhase('play'); return 0; } return v - 1; }), 1000); };
  const ready = () => { stopT(); setPhase('play'); };
  const fresh = () => { stopT(); let j, gg = 0; do { j = Math.floor(Math.random() * set.length); } while (j === i && gg++ < 10); setI(j); setPhase('ready'); setGot(0); setMiss(0); setWrong(null); };
  const tap = (k) => { playKey(k, 0.5); if (phase !== 'play' || done) return; if (k === memSemi(P.n[got])) { const g2 = got + 1; setGot(g2); setWrong(null); if (g2 >= N) { setPhase('done'); if (onResult) onResult({ ok: miss === 0 }); setTimeout(() => memPlay(P, 80, false), 500); } } else { setMiss(m => m + 1); setWrong(k); } };
  const lit = {}; P.n.slice(0, got).forEach(x => { lit[memSemi(x)] = 'good'; }); if (wrong != null && phase === 'play') lit[wrong] = 'bad';
  const kn = L7_KN[P.k] || lwLet(P.k), names = { 0: 'C', 12: 'C' }; names[P.k > 4 ? P.k - 12 : P.k] = kn;
  const lo = Math.min(-5, ...P.n.map(memSemi)) , hi = Math.max(14, ...P.n.map(memSemi));
  const show = phase === 'look' || phase === 'done' || (phase === 'ready' && false);
  return (
    <div className="try-box" style={actBox} data-l7="mem">
      <div style={actTitle}>{t('Remember the phrase', '프레이즈 외우기')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>{g}급: 먼저 <b>으뜸음</b>이 울리고, 악보로 <b>{bars}마디</b>를 {secs === 60 ? '약 1분' : '약 1분 반'} 동안 외워요. 그다음 악보 없이 <b>치거나 불러요</b>. 여기서는 건반으로 차례로 찾아요. 처음엔 <b>보면서 들어도</b> 돼요.</>
        : <>Grade {g}: first <b>the keynote</b>, then <b>{bars} bars</b> on paper to memorise in about {secs === 60 ? 'one minute' : 'a minute and a half'}. Then, with no copy, <b>play or sing it</b>. Here you find it on the keys, in order. To begin, you may <b>hear it while you look</b>.</>}</div>
      {!fixed && spChips([[true, t('Look and hear', '보면서 듣기')], [false, t('Look only, like the test', '보기만, 시험처럼')]], hear, (v) => { setHear(v); setPhase('ready'); stopT(); })}
      <div style={{minHeight:96,display:'flex',alignItems:'center',justifyContent:'center',margin:'4px 0'}}>{show
        ? <div style={{width:'100%',maxWidth:360,background:'#fff',borderRadius:8}}><MelodyStaff notes={memNotes(P)} beats={P.beats} width={330} colors={phase === 'done' ? P.n.map((_, j) => j < got ? '#2e8a6e' : '#26296b') : null}/></div>
        : <div style={{display:'flex',gap:5,flexWrap:'wrap',justifyContent:'center'}}>{P.n.map((x, j) => <span key={j} style={{width:30,height:30,borderRadius:6,display:'inline-flex',alignItems:'center',justifyContent:'center',fontWeight:900,fontSize:13,border:'1.5px solid ' + (j < got ? BK.green : 'rgba(38,41,107,0.3)'),color:j < got ? BK.green : BK.muted,background:'#fff'}}>{j < got ? memLetter(x) : phase === 'play' ? '?' : '·'}</span>)}</div>}</div>
      {phase === 'look' && <div style={{textAlign:'center',fontSize:22,fontWeight:900,color:left <= 10 ? BK.coral : BK.ink,fontVariantNumeric:'tabular-nums'}}>{left}{t(' s', '초')}</div>}
      <SpKb lo={lo} hi={hi} W={18} H={66} lit={lit} names={names} onTap={tap} label={t('Play it back', '쳐서 돌려주기')}/>
      {spMsg(phase === 'ready' ? t('▶ The keynote sounds, then the phrase appears.', '▶ 으뜸음이 울리고, 프레이즈가 나타나요.') : phase === 'look' ? t('Memorise it: sing it inside, see the shape.', '외워요: 속으로 부르고, 모양을 봐요.') : phase === 'play' ? (wrong != null ? t('Not that one: hum it again from the start.', '그 음이 아니에요: 처음부터 다시 흥얼거려요.') : t('From memory: note ' + (got + 1) + ' of ' + N + '.', '외운 대로: ' + N + '개 중 ' + (got + 1) + '번째.'))
        : (miss === 0 ? t('All ' + N + ' notes from memory ✓', N + '음 모두 외워서 ✓') : t('Found, with ' + miss + ' slip' + (miss > 1 ? 's' : '') + '. Look at the shape again.', '찾았어요, 실수 ' + miss + '번. 모양을 다시 봐요.')), phase === 'done' ? (miss === 0 ? BK.green : BK.coral) : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        {phase === 'ready' && <button className="ghost-btn" style={spBtn} onClick={look}>{t('▶ Keynote, then look', '▶ 으뜸음, 그다음 보기')}</button>}
        {phase === 'look' && hear && <button className="ghost-btn" style={spBtn} onClick={() => memPlay(P, 80, false)}>{t('♪ Hear it', '♪ 들어 보기')}</button>}
        {phase === 'look' && <button className="ghost-btn" style={spBtn} onClick={ready}>{t('I have it: hide it', '외웠어요: 숨기기')}</button>}
        {phase === 'done' && <button className="ghost-btn" style={spBtn} onClick={() => memPlay(P, 80)}>{t('♪ Hear it', '♪ 들어 보기')}</button>}
        {(phase === 'done' || phase === 'play') && !fixed && <button className="ghost-btn" style={spBtn} onClick={fresh}>{t('▶ Another phrase', '▶ 다른 프레이즈')}</button>}
      </div>
    </div>
  );
}
// ── step 4: six notes in two parts, note against note, within an octave from middle C ──
const L7_TWO = [
  [[0, 4], [2, 5], [4, 7], [5, 9], [4, 7], [0, 4]], [[0, 12], [2, 11], [4, 9], [5, 9], [7, 11], [0, 12]], [[7, 11], [5, 12], [4, 12], [2, 11], [0, 9], [0, 12]],
  [[0, 4], [0, 5], [0, 7], [0, 9], [0, 7], [0, 4]], [[4, 12], [5, 9], [7, 11], [9, 12], [7, 11], [4, 12]], [[2, 5], [4, 7], [5, 9], [7, 11], [5, 9], [4, 7]],
  [[0, 9], [2, 9], [4, 7], [5, 9], [7, 11], [0, 12]], [[7, 11], [5, 9], [4, 7], [0, 4], [2, 5], [0, 4]], [[0, 7], [4, 7], [5, 9], [2, 11], [4, 12], [0, 12]],
  [[5, 9], [7, 11], [9, 12], [7, 11], [5, 9], [4, 7]],
].map(l6Pairs);
function L7TwoPad(p) { return <PartsPad set={L7_TWO} bpm={60} tag="two7" rungs={[[3, t('First three', '처음 셋')], [6, t('All six, like the test', '여섯 모두, 시험처럼')]]} title={t('Six notes: sing one part', '여섯 음: 한 성부를 불러요')}
  note={LANG === 'ko' ? <>두 음씩 <b>여섯 번</b>, 두 성부로 천천히(전체를 두 번). 외워서 묻는 성부의 여섯 음을 부르고, 건반에서 차례로 찾아요. 윗성부는 새, 아랫성부는 거북이. 처음엔 <b>셋만</b>.</>
    : <>Two notes together, <b>six times</b>, slowly, in two parts (all of it played twice). From memory, sing the six notes of the part asked for, then find them on the keys in order. The higher part is the bird's, the lower the turtle's. First <b>just three</b>.</>} {...p}/>; }
const L7CadPad = (p) => <CadPad cads={['perfect', 'plagal', 'interrupted']} tag="cad7" {...p}/>;
const L7PosPad = (p) => <L6PosPad quals={['maj', 'min']} {...p}/>;
// ── make: a tune of my own to remember ──
function MemMaker() {
  const [notes, setNotes] = useState([]), [phase, setPhase] = useState('write'), [got, setGot] = useState(0), [miss, setMiss] = useState(0), [wrong, setWrong] = useState(null);
  const W7 = [0, 2, 4, 5, 7, 9, 11], dOf = (k) => { const o = Math.floor(k / 12), pc = spPc(k), w = W7.indexOf(pc); return w >= 0 ? { d: 28 + 7 * o + w, acc: 0 } : { d: 28 + 7 * o + W7.indexOf(pc - 1), acc: 1 }; };
  const staff = notes.map((k, j) => ({ ...dOf(k), dur: j === notes.length - 1 && notes.length >= 4 ? 2 : 1 }));
  const total = staff.reduce((a, x) => a + x.dur, 0);
  const play = (ns = notes) => spPlay(ns.map((k, j) => ({ at: j, keys: [k], len: j === ns.length - 1 ? 1.8 : 0.9, vol: 0.15 })), 84);
  const tap = (k) => { playKey(k, 0.5);
    if (phase === 'write') { if (notes.length < 8) setNotes(notes.concat([k])); return; }
    if (phase !== 'back') return; if (k === notes[got]) { const g2 = got + 1; setGot(g2); setWrong(null); if (g2 >= notes.length) setPhase('done'); } else { setMiss(m => m + 1); setWrong(k); } };
  const lit = {}; if (phase === 'back' || phase === 'done') { notes.slice(0, got).forEach(k => { lit[k] = 'good'; }); if (wrong != null) lit[wrong] = 'bad'; }
  return (
    <div className="try-box" style={actBox} data-mk="mem">
      <div style={actTitle}>{t('A tune to remember', '외울 내 선율')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>건반을 눌러 <b>나만의 선율</b>을 써요(음표 여덟 개까지). 악보에 바로 나타나요. 다 썼으면 <b>숨기고</b>, 외운 대로 다시 쳐 봐요. 친구에게도 내 봐요!</> : <>Tap keys to write <b>a tune of your own</b> (up to eight notes); it appears on the staff as you go. Then <b>hide it</b> and play it back from memory. Try it on a friend too!</>}</div>
      <div style={{minHeight:92,display:'flex',alignItems:'center',justifyContent:'center'}}>{phase === 'back' ? <div style={{display:'flex',gap:5}}>{notes.map((k, j) => <span key={j} style={{width:28,height:28,borderRadius:6,display:'inline-flex',alignItems:'center',justifyContent:'center',fontWeight:900,fontSize:13,border:'1.5px solid ' + (j < got ? BK.green : 'rgba(38,41,107,0.3)'),color:j < got ? BK.green : BK.muted,background:'#fff'}}>{j < got ? lwLet(k) : '?'}</span>)}</div>
        : notes.length ? <div style={{width:'100%',maxWidth:340,background:'#fff',borderRadius:8}}><MelodyStaff notes={staff} beats={4} width={Math.max(220, total * 38 + 90)}/></div> : <div style={{fontSize:13,fontWeight:800,color:BK.muted}}>{t('Your tune will appear here.', '여기에 내 선율이 나타나요.')}</div>}</div>
      <SpKb lo={0} hi={12} W={26} H={70} lit={lit} names={{ 0: 'C', 12: 'C' }} onTap={tap} label={t('Write, then play back', '쓰고, 다시 치기')}/>
      {spMsg(phase === 'write' ? t(notes.length + ' of 8 notes', '8개 중 ' + notes.length + '개') : phase === 'back' ? t('From memory: note ' + (got + 1) + ' of ' + notes.length, '외운 대로: ' + notes.length + '개 중 ' + (got + 1) + '번째') : (miss === 0 ? t('Every note from memory ✓', '모든 음을 외워서 ✓') : t('Back, with ' + miss + ' slip' + (miss > 1 ? 's' : '') + '.', '돌려줬어요, 실수 ' + miss + '번.')), phase === 'done' ? (miss === 0 ? BK.green : BK.coral) : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={spBtn} disabled={!notes.length} onClick={() => play()}>{t('▶ Play my tune', '▶ 내 선율 듣기')}</button>
        {phase === 'write' && <button className="ghost-btn" style={spBtn} disabled={notes.length < 3} onClick={() => { setPhase('back'); setGot(0); setMiss(0); setWrong(null); }}>{t('Hide it: play it back', '숨기고 다시 치기')}</button>}
        {phase === 'write' && <button className="ghost-btn" style={spBtn} disabled={!notes.length} onClick={() => setNotes(notes.slice(0, -1))}>{t('Undo', '되돌리기')}</button>}
        {phase !== 'write' && <button className="ghost-btn" style={spBtn} onClick={() => { setPhase('write'); setGot(0); setWrong(null); }}>{t('Show it again', '다시 보기')}</button>}
        <button className="ghost-btn" style={spBtn} disabled={!notes.length} onClick={() => { setNotes([]); setPhase('write'); setGot(0); setMiss(0); setWrong(null); }}>{t('Clear', '지우기')}</button>
      </div>
    </div>
  );
}

// ── the pictures on paper ──
const l7PicTri = () => lsRawPic('<ellipse cx="18" cy="34" rx="6.5" ry="4.6" transform="rotate(-20 18 34)" fill="#26296b"/><ellipse cx="18" cy="24" rx="6.5" ry="4.6" transform="rotate(-20 18 24)" fill="#e4572e"/><ellipse cx="18" cy="14" rx="6.5" ry="4.6" transform="rotate(-20 18 14)" fill="#26296b"/><text x="32" y="22" font-family="Inter, sans-serif" font-size="11" font-weight="900" fill="#26296b">M</text><text x="32" y="36" font-family="Inter, sans-serif" font-size="11" font-weight="900" fill="#e4572e">m</text>', [0, 0, 50, 44]);
const l7PicCad = () => lsRawPic('<rect x="3" y="9" width="70" height="26" rx="3" fill="#fff" stroke="#26296b" stroke-width="2"/><path d="M38 9 V35" stroke="#26296b" stroke-width="2"/><text x="20" y="28" text-anchor="middle" font-family="Georgia, serif" font-size="14" font-weight="900" fill="#e4572e">V</text><text x="56" y="28" text-anchor="middle" font-family="Georgia, serif" font-size="14" font-weight="900" fill="#e4572e">vi</text>', [0, 0, 76, 44]);
const l7PicMem = () => lsRawPic('<path d="M4 10 H70 M4 16 H70 M4 22 H70 M4 28 H70 M4 34 H70" stroke="#26296b" stroke-width="1.1"/>' + [[14, 28], [26, 25], [38, 22], [50, 19], [62, 25]].map(([x, y]) => '<ellipse cx="' + x + '" cy="' + y + '" rx="4.4" ry="3.2" transform="rotate(-20 ' + x + ' ' + y + ')" fill="#26296b"/>').join('') + '<circle cx="66" cy="8" r="6" fill="none" stroke="#e4572e" stroke-width="2"/><path d="M66 4 V8 H69" stroke="#e4572e" stroke-width="1.8" fill="none"/>', [0, 0, 76, 44]);
const l7PicTwo = () => lsRawPic('<path d="M4 12 L16 8 L28 12 L40 6 L52 10 L64 8" fill="none" stroke="#e4572e" stroke-width="2.4"/><path d="M4 34 L16 30 L28 34 L40 26 L52 32 L64 30" fill="none" stroke="#26296b" stroke-width="2.4"/>' + [4, 16, 28, 40, 52, 64].map((x, i) => '<circle cx="' + x + '" cy="' + [12, 8, 12, 6, 10, 8][i] + '" r="3.2" fill="#e4572e"/><circle cx="' + x + '" cy="' + [34, 30, 34, 26, 32, 30][i] + '" r="3.2" fill="#26296b"/>').join(''), [0, 0, 70, 44]);

function l7LbPages(scr = false) {
  const ch = 'listen-7', l6c = bkChapterNo('listen-6');
  const checks4 = [[l7PicTri(), t('I hear whether a triad is major or minor, and its position', '3화음이 장3화음인지 단3화음인지, 그리고 그 자리를 들어요')], [l7PicCad(), t('I hear a perfect, plagal or interrupted cadence in a short piece', '짧은 곡에서 정격, 변격, 거짓종지를 들어요')],
    [l7PicMem(), t('I memorise a two-bar phrase in a minute, then play or sing it', '2마디 프레이즈를 1분 안에 외워 치거나 불러요')], [l7PicTwo(), t('I sing the higher or the lower part of six notes in two parts', '두 성부 여섯 음의 윗성부나 아랫성부를 불러요')]];
  const pen = (x) => <PenArt shapes={x.shapes} vb={x.vb} style={{width:90}}/>;
  const toc = [[t('Major or minor, and which position?', '장3화음? 단3화음? 그리고 어느 자리?'), 2], [t('Perfect, plagal or interrupted?', '정격, 변격, 거짓종지?'), 3], [t('Remember the phrase', '프레이즈 외우기'), 4], [t('Six notes: sing one part', '여섯 음: 한 성부를 불러요'), 5], [t('My four checks', '나의 네 가지 확인'), 6]];
  const triStill = <LbPic h={170}><div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:14,width:'100%',maxWidth:620,margin:'0 auto'}}>{['maj', 'min'].map(q => { const n = l6Tri(0, q, 0);
    return <div key={q}><div style={{textAlign:'center',fontSize:13.5,fontWeight:900,color:BK.ink}}>{t('C ' + L6_QN[q][0] + ': the middle note ' + (q === 'maj' ? 'E' : 'E♭'), 'C ' + L6_QN[q][1] + ': 가운데 음 ' + (q === 'maj' ? 'E' : 'E♭'))}</div>{l4Kb(Object.fromEntries(n.map((k, j) => [k, j === 1 ? 'cor' : 'pale'])), Object.fromEntries(n.map(k => [k, lwLet(k)])), scr, -2, 16)}</div>; })}</div></LbPic>;
  const cadStill = <LbPic h={150}><div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr 1fr',gap:12,width:'100%',maxWidth:760,margin:'0 auto'}}>{[['perfect', 0], ['plagal', 1], ['interrupted', 0]].map(([c, ti]) => <div key={c}><div style={{textAlign:'center',fontSize:13.5,fontWeight:900,color:BK.ink}}>{cadCap(c)} · {CAD_N[c][2]}</div><CadChart x={{ key: 0, cad: c, ti }}/></div>)}</div></LbPic>;
  return [
    <LbPage key="1" no={1} chId={ch} teacher={<>{t('The Grade 7 aural tests, one step each (Manual of Syllabuses, section 21): any major or minor triad, root position or an inversion, within an octave: major or minor, and its position (Grade 6, chapter ' + l6c + ', had the major only); perfect, plagal and interrupted cadences in a major key as they occur in a short piece, the tonic chord first; about one minute to memorise a two-bar phrase from a printed copy away from the instrument, then play or sing it (the keynote sounded first); the higher or lower part of a two-part phrase of not more than six notes, note against note, within an octave from middle C. The tunes are written for this app.', '7급 청음 시험을 한 단계씩(실라버스 21절): 장3화음이나 단3화음을 기본형이나 자리바꿈으로 한 옥타브 안에서: 장단과 자리 알기(' + l6c + '장의 6급은 장3화음만); 장조의 짧은 곡에서 나오는 정격, 변격, 거짓종지 알기, 먼저 으뜸화음; 악보로 2마디 프레이즈를 악기 없이 약 1분 동안 외우고 치거나 부르기(먼저 으뜸음); 두 성부 프레이즈(여섯 음까지, 음 대 음, 가운데 도부터 한 옥타브 안)의 윗성부나 아랫성부. 선율은 이 앱을 위해 지었어요.')}</>}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:50,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{bkChapterName(ch)}</div>
      </div></LbOnly>
      <LbPic h={150}><div style={{width:'100%',maxWidth:380,margin:'0 auto',background:'#fff',borderRadius:8}}><MelodyStaff notes={memNotes(L7_MEM[2])} beats={4} width={memW(L7_MEM[2])}/></div></LbPic>
      <LbSay size={18}>{t('Your ears for Grade 7: major or minor and where it stands, three endings, a phrase held in your memory, and six notes in two parts.', '7급의 귀: 장단과 자리, 세 가지 끝, 기억에 담는 프레이즈, 그리고 두 성부 여섯 음.')}</LbSay>
      <div className="lb-toc" style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>
        <LbOnly print><div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('In this chapter', '이 챕터에서는')}</div>
          {toc.map(([n, p]) => <div key={p} className="lb-toc-row" style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:14.5,padding:'5px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkGoal(15)}{n}</span><span style={{color:BK.muted,fontWeight:700}}>{p}</span></div>)}
        </div></LbOnly>
        <div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 챕터를 마치면')}</div>
          {checks4.map(([, x], i) => <div key={i} style={{display:'flex',alignItems:'flex-start',gap:9,fontSize:14.5,padding:'5px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}>{bkGoal(15)}<span>{x.replace(/^I /, '')}</span></div>)}
        </div>
      </div>
      <LbOnly print><LbDrillStrip id={ch}/></LbOnly>
    </LbPage>,
    <LbPage key="2" no={2} chId={ch} kicker={t('Step 1', '1단계')} title={t('Major or minor, and which position?', '장3화음? 단3화음? 그리고 어느 자리?')}
      teacher={<>{t('Grade 7: any major or minor triad, root position or an inversion, within an octave; the child says major or minor, then its position. Played twice. Major or minor is in the 3rd above the root (bright or dark); the position is in the 4th, as in Grade 6 (none, root position; on top, first inversion; at the bottom, second inversion). The pad asks for the triad first, then the position.', '7급: 장3화음이나 단3화음을 기본형이나 자리바꿈으로 한 옥타브 안에서 쳐요. 아이는 장단을 말하고, 그다음 자리를 말해요. 두 번 들려줘요. 장단은 근음 위의 3도에(밝음, 어두움); 자리는 6급처럼 4도에(없음, 기본형; 위, 첫째 자리바꿈; 아래, 둘째 자리바꿈). 패드는 먼저 3화음, 그다음 자리를 물어요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=1')}>
      <LbLive still={triStill} live={<L7PosPad/>}/>
      <LbSay>{LANG === 'ko' ? <>두 가지를 들어요. <b>밝은가, 어두운가</b>: 장3화음과 단3화음. 그다음 <b>4도가 어디</b>: 없으면 기본형, 위면 첫째, 아래면 둘째 자리바꿈.</> : <>Listen for two things. <b>Bright or dark</b>: major or minor. Then <b>where the 4th is</b>: none, root position; on top, first inversion; at the bottom, second.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>선생님이 C장3화음과 C단3화음을 쳐요. 가운데 음을 흥얼거려요.</>, <>이번엔 자리바꿈한 3화음. 아래부터 한 음씩 흥얼거려요.</>, <>장단, 그리고 자리를 말해요.</>]
        : [<>Your teacher plays C major, then C minor. Hum the middle note.</>, <>Now a triad in an inversion. Hum it one note at a time from the bottom.</>, <>Say major or minor, then the position.</>]}/>
      <LbRemember>{t('Bright or dark, then find the 4th.', '밝은지 어두운지, 그다음 4도 찾기.')}</LbRemember>
    </LbPage>,
    <LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={t('Perfect, plagal or interrupted?', '정격, 변격, 거짓종지?')}
      teacher={<>{t('Grade 7: perfect, plagal and interrupted cadences in a major key as they occur in a short piece played by you, the tonic chord being first sounded. New since Grade 6: the interrupted cadence, V–vi, the surprise ending. The app’s pieces are four bars of chords in C, G, D, F, B♭ or A major; the first rung plays only the last two chords.', '7급: 선생님이 치는 장조의 짧은 곡에서 나오는 정격, 변격, 거짓종지 알기, 먼저 으뜸화음. 6급에서 새로운 것: 거짓종지 V–vi, 깜짝 끝. 앱의 곡은 C, G, D, F, B♭, A장조의 네 마디 화음; 첫 걸음은 마지막 두 화음만.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=2')}>
      <LbLive still={cadStill} live={<L7CadPad/>}/>
      <LbSay>{LANG === 'ko' ? <><b>V에서 I</b>은 정격: 단단히 닫혀요. <b>IV에서 I</b>은 변격: 부드럽게. <b>V에서 vi</b>는 거짓종지: 집에 올 줄 알았는데, 깜짝!</> : <><b>V to I</b>, perfect: firmly closed. <b>IV to I</b>, plagal: softly closed. <b>V to vi</b>, interrupted: you expect home, and get a surprise!</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>선생님이 V–I, 그다음 V–vi를 쳐요. 어느 쪽이 놀라운가요?</>, <>짧은 곡 전체. 끝 두 화음만 기억해요.</>, <>정격, 변격, 거짓종지 중 무엇일까요?</>]
        : [<>Your teacher plays V–I, then V–vi. Which one surprises you?</>, <>Now a whole short piece. Remember just the last two chords.</>, <>Perfect, plagal or interrupted?</>]}/>
      <LbRemember>{t('V to vi: the surprise.', 'V에서 vi: 깜짝 끝.')}</LbRemember>
    </LbPage>,
    <LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title={t('Remember the phrase', '프레이즈 외우기')}
      teacher={<>{t('Grade 7: about one minute to memorise a two-bar melodic phrase from a printed copy, away from the instrument; then the child plays or sings it from memory. You sound the keynote before the phrase is memorised. Ways in: sing it inside; see its shape (steps, leaps, where it turns); count its rhythm; find its last note against the keynote. The first rung lets the child hear it while looking; then look only, with the clock.', '7급: 악기에서 떨어져 악보로 2마디 선율 프레이즈를 약 1분 동안 외우고, 외운 대로 치거나 불러요. 외우기 전에 선생님이 으뜸음을 울려요. 방법: 속으로 부르기; 모양 보기(차례 진행, 도약, 방향이 바뀌는 곳); 리듬 세기; 마지막 음을 으뜸음과 견주기. 첫 걸음은 보면서 들어도 돼요; 그다음 보기만, 시계와 함께.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=3')}>
      <LbLive still={<LbPic h={150}><div style={{width:'100%',maxWidth:480,margin:'0 auto',background:'#fff',borderRadius:8}}><MelodyStaff notes={memNotes(L7_MEM[1])} beats={4} width={memW(L7_MEM[1])}/></div></LbPic>} live={<L7MemPad/>}/>
      <LbSay>{LANG === 'ko' ? <>1분 동안: <b>속으로 부르고</b>, <b>모양</b>(차례로? 뛰어서?)을 보고, <b>리듬</b>을 세고, <b>마지막 음</b>을 기억해요.</> : <>In one minute: <b>sing it inside</b>, see <b>its shape</b> (steps? leaps?), count <b>its rhythm</b>, and remember <b>its last note</b>.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>선생님이 으뜸음을 울려요. 악보를 1분 동안 봐요.</>, <>악보를 덮고, 그 프레이즈를 쳐요.</>, <>이번엔 불러요. 박자도 지켜요.</>]
        : [<>Your teacher sounds the keynote. Look at the copy for one minute.</>, <>Close the copy and play the phrase.</>, <>Now sing it, keeping its rhythm.</>]}/>
      <LbRemember>{t('Sing it inside; see its shape.', '속으로 부르고, 모양을 봐요.')}</LbRemember>
    </LbPage>,
    <LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title={t('Six notes: sing one part', '여섯 음: 한 성부를 불러요')}
      teacher={<>{t('Grade 7: a two-part phrase of not more than six notes, note against note, within an octave from middle C, played slowly; the child hums or sings the higher or the lower part from memory. Two more notes than Grade 6. The first rung is the first three only.', '7급: 여섯 음까지의 두 성부 프레이즈, 음 대 음, 가운데 도부터 한 옥타브 안에서 천천히; 아이는 윗성부나 아랫성부를 외워서 흥얼거리거나 불러요. 6급보다 두 음 더. 첫 걸음은 처음 셋만.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=4')}>
      <LbLive still={<LbPic h={150}><div style={{width:'100%',maxWidth:440,margin:'0 auto'}}><PartsLines P={L7_TWO[1]}/></div></LbPic>} live={<L7TwoPad/>}/>
      <LbSay>{LANG === 'ko' ? <>여섯 걸음, 두 줄. 묻는 줄만 귀로 따라가요: 위는 <b>새</b>, 아래는 <b>거북이</b>.</> : <>Six steps, two lines. Follow only the line asked for: the top is <b>the bird</b>, the bottom <b>the turtle</b>.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>선생님이 처음 세 음을 쳐요. 윗성부를 불러요.</>, <>이제 여섯 음 모두, 두 번. 아랫성부를 불러요.</>, <>부른 음을 건반에서 찾아요.</>]
        : [<>Your teacher plays the first three. Sing the higher part.</>, <>Now all six, twice. Sing the lower part.</>, <>Find the notes you sang on the keys.</>]}/>
      <LbRemember>{t('Six moves: follow one line.', '여섯 걸음: 한 줄만 따라가요.')}</LbRemember>
    </LbPage>,
    <LbPage key="6" no={6} chId={ch} kicker={t('Check-up', '점검')} title={t('My four checks', '나의 네 가지 확인')}
      teacher={<>{t('Each one with you at the piano, away from the screen, as in the exam: you play (twice), the child sings, plays or names. The memory test with a printed phrase the child has not seen: the teacher copy has ten.', '하나씩 화면 없이 피아노 앞에서, 시험처럼: 선생님이 치고(두 번), 아이는 부르거나 치거나 이름을 말해요. 외우기는 아이가 처음 보는 악보로: 선생님용에 열 개가 있어요.')}</>}>
      <LbSay>{t('Tick each one: not yet, nearly, or got it!', '하나씩 표시해요: 아직, 거의, 됐어요!')}</LbSay>
      <LbLive still={<LbStageRows big rows={checks4.map(([a, txt]) => [pen(a), txt])}/>} live={<FiveChecks376 rows={checks4} storeKey="pb_l7_four"/>}/>
    </LbPage>,
  ];
}
function Listen7LessonBook() { return <>{l7LbPages(false)}</>; }
function L7Learn({ onStart }) {
  const pages = l7LbPages(true), opener = pages[0];
  return (
    <Lesson id="listen-7" title={bkChapterName('listen-7')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="listen-7"><div className="lb-screen lb-open" style={{display:'flex',flexDirection:'column',gap:12,margin:'0 0 8px'}}>{lbWordsFirst(opener.props.children)}</div></BkChapterCtx.Provider></LbScreenCtx.Provider>}>
      {pages.slice(1).map((pg, i) => <Step key={i} title={pg.props.title}><LbScreenPage page={pg}/></Step>)}
    </Lesson>
  );
}
const L7_LEVELS = [
  { n: 1, label: 'Major or minor, and which position?', kind: 'pos', time: 30 },
  { n: 2, label: 'Perfect, plagal or interrupted?', kind: 'cad', time: 40 },
  { n: 3, label: 'Remember a two-bar phrase', kind: 'mem', time: 120 },
  { n: 4, label: 'Six notes: sing the higher or the lower part', kind: 'two', time: 60 },
  { n: 5, label: 'All four, mixed, as in the Grade 7 exam', kind: 'mix', time: 120 },
];
Object.assign(LEVEL_KO, { 'Major or minor, and which position?': '장3화음? 단3화음? 그리고 어느 자리?', 'Perfect, plagal or interrupted?': '정격, 변격, 거짓종지?', 'Remember a two-bar phrase': '2마디 프레이즈 외우기', 'Six notes: sing the higher or the lower part': '여섯 음: 윗성부나 아랫성부 부르기', 'All four, mixed, as in the Grade 7 exam': '네 가지 섞어서, 7급 시험처럼' });
function genL7Question(lv, prev) {
  const uid = Math.random(); let kind = lv.kind;
  if (kind === 'mix') kind = pick(['pos', 'cad', 'mem', 'two'].filter(k => !prev || prev.kind !== k));
  let fx, key, g = 0;
  do {
    if (kind === 'pos') fx = { r: Math.floor(Math.random() * 12), q: pick(['maj', 'min']), inv: pick([0, 1, 2]) };
    else if (kind === 'cad') fx = { key: pick(CAD_KEYS), cad: pick(['perfect', 'plagal', 'interrupted']), ti: Math.floor(Math.random() * 3) };
    else if (kind === 'mem') fx = { i: Math.floor(Math.random() * L7_MEM.length) };
    else fx = { i: Math.floor(Math.random() * L7_TWO.length), ask: Math.random() < 0.5 ? 'hi' : 'lo' };
    key = kind + JSON.stringify(fx);
  } while (prev && prev.key === key && g++ < 10);
  return { kind, fx, answer: 'ok', choices: [], key, uid };
}
function L7Question({ q, given, locked, onAnswer, pixel }) {
  const pickIt = (c) => { if (locked || given) return; stopClicks(); onAnswer(c); };
  const res = (r) => pickIt(r.ok ? 'ok' : 'no');
  const title = { pos: t('Major or minor, and which position?', '장3화음? 단3화음? 그리고 어느 자리?'), cad: t('Home first, then the piece: which cadence?', '먼저 집, 그다음 곡: 어떤 종지?'), mem: t('Look, remember, then play it back.', '보고, 외우고, 다시 쳐요.'),
    two: q.fx.ask === 'hi' ? t('Sing the higher part, then find its six notes.', '윗성부를 부르고, 여섯 음을 찾아요.') : t('Sing the lower part, then find its six notes.', '아랫성부를 부르고, 여섯 음을 찾아요.') }[q.kind];
  const body = q.kind === 'pos' ? <L7PosPad key={q.uid} fixed={q.fx} onResult={res}/> : q.kind === 'cad' ? <L7CadPad key={q.uid} fixed={q.fx} onResult={res}/> : q.kind === 'mem' ? <L7MemPad key={q.uid} fixed={q.fx} onResult={res}/> : <L7TwoPad key={q.uid} fixed={q.fx} onResult={res}/>;
  return (<div>
    <p style={pixel ? {fontSize:11.5,textAlign:'center'} : {fontSize:15,fontWeight:700,textAlign:'center',margin:'0 0 8px',color:'var(--muted)',textWrap:'balance'}}>{title}</p>
    {body}
  </div>);
}
Object.assign(LISTEN_7_DRILL, { levels: L7_LEVELS, generate: genL7Question, check: (q, ans) => ans !== null && ans !== undefined && ans === q.answer, answerLabel: () => t('done', '완료'), Question: L7Question, Learn: L7Learn });
// the teacher's copy (no Workbook: every step is by ear; the memory phrases are printed here for you to show)
function L7Teacher() {
  const pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="listen-7" teacher>{content}</WbPage>);
  const lt = (i) => { const nm = lwLet(i); return i < 0 ? nm + ',' : nm + (i >= 12 ? "'" : ''); };
  const two = (P2) => P2.lo.map((p, j) => lt(p[0]) + '+' + lt(P2.hi[j][0])).join(' → ');
  const ltS = (r, i) => { const sm = spPc(i - r), nm = l6Spell(lwLet(r), sm, sm === 0 ? 1 : sm <= 4 ? 3 : 5); return nm + (i < 0 ? ',' : i >= 12 ? "'" : ''); };
  const tri = ([r, q, inv]) => { const n = l6Tri(r, q, inv); return n.map(x => ltS(r, x)).join(' ') + ' (' + lwLet(r) + ' ' + L6_QN[q][0] + ', ' + L4_INVW[inv][0] + ')'; };
  const cad = ([key, c, ti]) => CAD_KN[key] + ': ' + CAD_TPL[c][ti].slice(0, 6).reduce((a, x, j) => a + (j % 2 === 0 && j ? ' | ' : ' ') + x, '').trim() + ' | ' + CAD_TPL[c][ti][6] + ' (' + c + ')';
  P(<>
    <div style={{fontFamily:LB_SERIF,fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('listen-7')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 12px',lineHeight:1.5}}>No Workbook for this chapter: every step is by ear, as the Grade 7 aural tests ask. Each block faces its Lesson Book page and gives you material to play, the same as the app uses. Play every test twice. Middle C is C here; the C above is C'; notes below middle C carry a comma (B♭,).</div>
    <TcBlock page={2} title="Major or minor, and which position?" answers={<>{tcAns('PLAY', [[0, 'min', 1], [7, 'maj', 2], [2, 'min', 0], [5, 'maj', 1], [9, 'min', 2], [4, 'maj', 0], [10, 'min', 1], [3, 'maj', 2]].map(tri))}</>}
      watch="A minor triad in an inversion heard as major: the top note can sound bright. Ask for the triad in root position first (hum it), then the position."
      say="“Bright or dark, then find the 4th.”"/>
    <TcBlock page={3} title="Perfect, plagal or interrupted?" answers={<>{tcAns('PLAY THE TONIC CHORD, THEN', [[0, 'interrupted', 0], [7, 'perfect', 1], [2, 'plagal', 2], [5, 'interrupted', 2], [-2, 'perfect', 0], [9, 'plagal', 1]].map(cad))}</>}
      watch="Interrupted heard as perfect: V is there in both. Ask whether the last chord felt like home."
      say="“V to vi: the surprise.”"/>
  </>);
  P(<>
    <TcBlock page={4} title="Remember the phrase" answers={<div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:'4px 10px'}}>{L7_MEM.map((M, j) => <div key={j} style={{display:'flex',alignItems:'center',gap:4}}><span style={{fontSize:11,fontWeight:900,color:BK.muted,minWidth:14}}>{j + 1}.</span><div style={{flex:1,minWidth:0}}><MelodyStaff notes={memNotes(M)} beats={M.beats} width={memW(M, 300)}/></div></div>)}</div>}
      watch="Rushing to play before the shape is clear, or forgetting the rhythm of the second bar. One minute, away from the piano; sound the keynote first."
      say="“Sing it inside; see its shape.”"/>
  </>);
  P(<>
    <TcBlock page={5} title="Six notes: sing one part" answers={<>{tcAns('PLAY (LOWER+HIGHER)', L7_TWO.slice(0, 8).map(two))}</>}
      watch="Losing the lower part where the upper one leaps (phrases 2 and 9), or where the lower part stays still (phrase 4)."
      say="“Six moves: follow one line.”"/>
    <TcBlock page={6} title="My four checks" answers={<div style={{fontSize:12,color:BK.ink,lineHeight:1.5}}>Each one with you at the piano, away from the screen: you play twice, the child sings, plays or names. Use material the child has not heard or seen this week. The drill's level 5 mixes all four, as the exam does.</div>}/>
  </>);
  return <>{pages}</>;
}
TEACHER_COPIES['listen-7'] = L7Teacher;
'''
rep("""TEACHER_COPIES['listen-6'] = L6Teacher;""", """TEACHER_COPIES['listen-6'] = L6Teacher;""" + CH)

HOME = r'''
// ══ Build BT: Hear and Sing, Grade 7 on the Home (the Aural door) ══
LBH_FN['listen-7'] = (s) => l7LbPages(s);
const l7Add = (id, i, en, ko, benEn, bko, make) => { const spec = lbhSpec('listen-7', i, { make });
  TOOLS.push({ id, ch: 'concept', title: en, blurb: benEn, hidden: true, get kicker() { return t('Aural', '청음') + ' · ' + t('Hear and sing, Grade 7', '듣고 부르기, Grade 7'); }, C: () => <KqEngine spec={spec}/> });
  lbhRetitle(id, en, ko, benEn, bko); };
const l7CadQ = (n, prev) => { let x, g = 0; do { x = { key: pick(CAD_KEYS), cad: ['perfect', 'plagal', 'interrupted'][n % 3], ti: Math.floor(Math.random() * 3) }; } while (prev && prev.key === JSON.stringify(x) && g++ < 10); const sq = CAD_TPL[x.cad][x.ti];
  return { kind: 'choice', cols: 3, prompt: ['Home first, then the piece: which cadence?', '먼저 집, 그다음 곡: 어떤 종지?'], opts: ['perfect', 'plagal', 'interrupted'].map(c => ({ id: c, label: () => cadCap(c) })), ans: x.cad, ok: (a) => a === x.cad, key: JSON.stringify(x), play: () => cadPlay(x, false),
    fig: (c) => ({ mid: c.res ? <CadChart x={x}/> : null }), yes: ['Yes: ' + sq[5] + ' to ' + sq[6] + '.', '맞아요: ' + sq[5] + '에서 ' + sq[6] + '.'], no: ['It was ' + CAD_N[x.cad][0] + ': ' + sq[5] + ' to ' + sq[6] + '.', '정답은 ' + CAD_N[x.cad][1] + ': ' + sq[5] + '에서 ' + sq[6] + '.'] }; };
l7Add('l7-pos', 1, 'Major or minor, and which position?', '장3화음? 단3화음? 그리고 어느 자리?', 'Bright or dark, then find the 4th.', '밝은지 어두운지, 그다음 4도 찾기.', lwTapQ(L7PosPad, (n) => ({ fixed: { r: (n * 5) % 12, q: n % 2 ? 'min' : 'maj', inv: n % 3 } }), ['Major or minor, then the position.', '장단, 그다음 자리.'], ['Heard ✓', '들었어요 ✓']));
l7Add('l7-cad', 2, 'Perfect, plagal or interrupted?', '정격, 변격, 거짓종지?', 'Home first, then a short piece: how does it end?', '먼저 집, 그다음 짧은 곡: 어떻게 끝날까요?', l7CadQ);
l7Add('l7-mem', 3, 'Remember the phrase', '프레이즈 외우기', 'Look for a minute, then play it from memory.', '1분 동안 보고, 외워서 쳐요.', lwTapQ(L7MemPad, (n) => ({ fixed: { i: (n * 3) % L7_MEM.length } }), ['The keynote, then look: play it back from memory.', '으뜸음, 그다음 보기: 외워서 다시 쳐요.'], ['From memory ✓', '외워서 ✓']));
l7Add('l7-two', 4, 'Six notes: sing one part', '여섯 음: 한 성부를 불러요', 'Six notes in two parts: sing the higher or the lower.', '두 성부의 여섯 음: 윗성부나 아랫성부 부르기.', lwTapQ(L7TwoPad, (n) => ({ fixed: { i: (n * 3) % L7_TWO.length, ask: n % 2 ? 'lo' : 'hi' } }), ['Hear the two parts, sing the one asked, then find its notes.', '두 성부를 듣고, 묻는 성부를 부르고, 음을 찾아요.'], ['Sung and found ✓', '부르고 찾았어요 ✓']));
'''
rep("""
lbhAdd('rb-finger', 'r-beat', 'rhythm', 'The beat in your fingers'""", HOME + """
lbhAdd('rb-finger', 'r-beat', 'rhythm', 'The beat in your fingers'""")
rep("""  { id: 'mk-cad', ch: 'listen-6',""", """  { id: 'mk-mem', ch: 'listen-7', title: 'A tune to remember', blurb: 'Write a tune of your own, hide it, and play it back from memory.', C: () => <MemMaker/> },   // Build BT
  { id: 'mk-cad', ch: 'listen-6',""")
rep("""  'mk-cad': ['나만의 끝 만들기',""", """  'mk-mem': ['외울 내 선율', '나만의 선율을 쓰고, 숨기고, 외워서 다시 쳐요.'],
  'mk-cad': ['나만의 끝 만들기',""")
rep("""'mk-cad': ['chords', 3, 3, 'game ear'],""", """'mk-cad': ['chords', 3, 3, 'game ear'], 'mk-mem': ['melody', 3, 3, 'game ear'],""")
rep("""'mk-cad': 'p-chords',""", """'mk-cad': 'p-chords', 'mk-mem': 'c-map',""")
rep("""  'mk-cad': () => (\n""", """  'mk-mem': () => (
    <svg width="34" height="34" viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#3b4fa8"/><path d="M3 8 H21 M3 11 H21 M3 14 H21 M3 17 H21" stroke="#fefbf3" strokeWidth="0.8"/><ellipse cx="8" cy="14" rx="2.2" ry="1.6" fill="#e9a83a"/><ellipse cx="13" cy="11" rx="2.2" ry="1.6" fill="#e9a83a"/><ellipse cx="18" cy="8" rx="2.2" ry="1.6" fill="#fefbf3"/></svg>
  ),
  'mk-cad': () => (\n""")
rep("""    { id: 'au-6', en: 'Hear and sing, Grade 6', ko: '듣고 부르기, Grade 6', lessons: ['l6-iv', 'l6-pos', 'l6-two', 'l6-cad', 'mk-cad'], check: 'listen-6' },""",
    """    { id: 'au-6', en: 'Hear and sing, Grade 6', ko: '듣고 부르기, Grade 6', lessons: ['l6-iv', 'l6-pos', 'l6-two', 'l6-cad', 'mk-cad'], check: 'listen-6' },
    { id: 'au-7', en: 'Hear and sing, Grade 7', ko: '듣고 부르기, Grade 7', lessons: ['l7-pos', 'l7-cad', 'l7-mem', 'l7-two', 'mk-mem'], check: 'listen-7' },   // Build BT""")
rep("""  set('6', 'l6-iv l6-pos l6-two l6-cad mk-cad');   // Build BO: Hear and Sing, Grade 6""", """  set('6', 'l6-iv l6-pos l6-two l6-cad mk-cad');   // Build BO: Hear and Sing, Grade 6
  set('7', 'l7-pos l7-cad l7-mem l7-two mk-mem');   // Build BT: Hear and Sing, Grade 7""")
rep("""const LESSON_BOOKS = { 'harmony-6': Harmony6LessonBook,""", """const LESSON_BOOKS = { 'listen-7': Listen7LessonBook, 'harmony-6': Harmony6LessonBook,""")
rep("""const LB_PAGE_FNS = { 'harmony-6': h6LbPages,""", """const LB_PAGE_FNS = { 'listen-7': l7LbPages, 'harmony-6': h6LbPages,""")
rep("""const HOUSE_ICONS = {""", """const HOUSE_ICONS = {"listen-7": "<path d=\\"M8 15C3 21 3 29 8 35M15 19C12 22 12 28 15 31\\"/><path d=\\"M22 12 H44 M22 18 H44 M22 24 H44 M22 30 H44 M22 36 H44\\" stroke-width=\\"1\\"/><ellipse cx=\\"28\\" cy=\\"30\\" rx=\\"3.6\\" ry=\\"2.7\\" transform=\\"rotate(-20 28 30)\\" fill=\\"#26296b\\"/><ellipse cx=\\"34\\" cy=\\"24\\" rx=\\"3.6\\" ry=\\"2.7\\" transform=\\"rotate(-20 34 24)\\" fill=\\"#26296b\\"/><ellipse cx=\\"40\\" cy=\\"18\\" rx=\\"3.6\\" ry=\\"2.7\\" transform=\\"rotate(-20 40 18)\\" fill=\\"#e4572e\\" stroke=\\"#e4572e\\"/>", """)
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
