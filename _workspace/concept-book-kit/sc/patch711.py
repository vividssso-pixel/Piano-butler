import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build AR (board call 18, the first Grade 4 room): Hear and Sing, Grade 4. The Grade 4 practical aural tests (Manual of
# Syllabuses 2026, section 21, read 26 Oct): the keynote, then any interval of the major scale straight after it, sung and
# named in full (major 2nd, major 3rd, perfect 4th ...: "Grades 4, 5 and 6 require candidates to name the intervals as major
# second, major third, perfect fourth, etc."); the higher or the lower part of a two-part progression of two successive
# intervals, within an octave from middle C, sung from memory; any major or minor triad, root position or inverted, within an
# octave: sing the middle note; a passage in duple or triple time played twice, tapped back and named. The Grade 4 floor
# opens in the house (call 9: Grades 4 and 5 are two floors); its other rooms wait off the map until they are built.

rep("""const LISTEN_WRITE_DRILL = { id: 'listen-write', label: 'Listen, Clap, Write', noPrint: true };""",
    """const LISTEN_WRITE_DRILL = { id: 'listen-write', label: 'Listen, Clap, Write', noPrint: true };
const LISTEN_4_DRILL = { id: 'listen-4', label: 'Hear and Sing, Grade 4', noPrint: true };   // Build AR""")
rep("""  { id: 'listen-write', label: 'Listen, Clap, Write', concept: LISTEN_WRITE_DRILL, track: 'start' },   // Build AE""",
    """  { id: 'listen-write', label: 'Listen, Clap, Write', concept: LISTEN_WRITE_DRILL, track: 'start' },   // Build AE
  { id: 'listen-4', label: 'Hear and Sing, Grade 4', concept: LISTEN_4_DRILL, track: 'start' },   // Build AR""")
rep("""'listen-23': '더 듣고 부르기'""", """'listen-23': '더 듣고 부르기', 'listen-4': '듣고 부르기, Grade 4'""", n=1)
rep("""'listen-23': ['listen-write']""", """'listen-23': ['listen-write'], 'listen-4': ['listen-23', 'intervals']""")
rep("""'listen-23': ['Hear & sing', '듣고 부르기']""", """'listen-23': ['Hear & sing', '듣고 부르기'], 'listen-4': ['Hear, Grade 4', '듣기 4']""")
rep("""  'listen-23': 'aural ear grade 2 grade 3""", """  'listen-4': 'aural ear grade 4 interval major scale keynote name major second third perfect fourth fifth sixth seventh octave two-part progression upper lower part triad middle note inversion clap back duple triple',
  'listen-23': 'aural ear grade 2 grade 3""")
rep("""if (id === 'listen-sing' || id === 'listen-write' || id === 'listen-23') return 'aural';""", """if (id === 'listen-sing' || id === 'listen-write' || id === 'listen-23' || id === 'listen-4') return 'aural';""")
# the house: the Grade 4 floor, between Grades 2-3 and Stories of music
rep("""  { ids: ['piano-story', 'pitch-range', 'composers', 'styles'], stories: true,""",
    """  { ids: ['listen-4', 'scales-4', 'keys-4', 'harmony-4', 'rhythm-4', 'terms-4'], en: ['Grade 4', 'Your ears, scales and arpeggios, keys and intervals, chords and cadences, rhythm, and the words and ornaments.'], ko: ['Grade 4', '귀, 스케일과 아르페지오, 조와 음정, 화음과 종지, 리듬, 용어와 꾸밈음.'] },   // Build AR: the Grade 4 floor (call 9); its rooms appear as they are built (call 18)
  { ids: ['piano-story', 'pitch-range', 'composers', 'styles'], stories: true,""")
# the Home: the Aural door gains the Grade 4 room
rep("""    { id: 'au-23', en: 'Hear and sing further', ko: '더 듣고 부르기', lessons: ['l2-dyad', 'l2-any', 'l2-deg', 'l2-clap', 'l2-sing'], check: 'listen-23' },""",
    """    { id: 'au-23', en: 'Hear and sing further', ko: '더 듣고 부르기', lessons: ['l2-dyad', 'l2-any', 'l2-deg', 'l2-clap', 'l2-sing'], check: 'listen-23' },
    { id: 'au-4', en: 'Hear and sing, Grade 4', ko: '듣고 부르기, Grade 4', lessons: ['l4-iv', 'l4-two', 'l4-mid', 'l4-clap'], check: 'listen-4' },   // Build AR""")
rep("""  set('23', 'l2-dyad l2-any l2-deg l2-clap l2-sing');""", """  set('23', 'l2-dyad l2-any l2-deg l2-clap l2-sing');
  set('4', 'l4-iv l4-two l4-mid l4-clap');   // Build AR: Hear and Sing, Grade 4""")

CH = r'''
// ─── Chapter: Hear and Sing, Grade 4 (Build AR, 2026-10-26; board call 18, the first Grade 4 room) ───
// The Grade 4 practical aural tests (Manual 2026, section 21), one step each: the keynote, then any interval of the major
// scale, sung and named in full; two intervals in two parts, the higher or the lower part sung from memory; a major or minor
// triad, root position or inverted, its middle note sung; a passage heard twice, tapped back, duple or triple said. All
// within an octave from middle C. Every test is heard twice.
// the intervals of the major scale from the keynote: [number, semitones]; 1 2 3 6 7 major, 4 5 8 perfect
const L4_IV = [[2, 2], [3, 4], [4, 5], [5, 7], [6, 9], [7, 11], [8, 12]];
const L4_IVN = { 2: ['major 2nd', '장2도'], 3: ['major 3rd', '장3도'], 4: ['perfect 4th', '완전4도'], 5: ['perfect 5th', '완전5도'], 6: ['major 6th', '장6도'], 7: ['major 7th', '장7도'], 8: ['perfect octave', '완전8도'] };
const l4IvName = (n) => t(L4_IVN[n][0], L4_IVN[n][1]);
const L4_KEYS = [0, 2, 5, 7, -1, -3];   // C, D, F, G, and B, A below middle C: the keynote, the interval still within an octave and a bit
const l4Let = (i) => lwLet(((i % 12) + 12) % 12);
const l4PlayIv = (k, d) => spPlay([{ at: 0, keys: [k], len: 1.5 }, { at: 1.9, keys: [k + d], len: 1.8 }, { at: 4.5, keys: [k], len: 1.5 }, { at: 6.4, keys: [k + d], len: 1.8 }], 84);
// two intervals in two parts, within an octave from middle C: [[low, high], [low, high]], white keys, the parts moving by
// step, skip or staying, as in simple two-part writing
const L4_TWO = [
  [[0, 4], [2, 5]], [[4, 7], [2, 7]], [[0, 7], [2, 5]], [[5, 9], [4, 7]], [[2, 11], [0, 12]], [[4, 12], [5, 11]],
  [[0, 9], [2, 7]], [[7, 11], [5, 12]], [[2, 5], [0, 4]], [[4, 9], [5, 9]], [[0, 12], [2, 11]], [[5, 11], [4, 12]],
];
const l4PlayTwo = (pr) => spPlay([{ at: 0, keys: pr[0], len: 1.4, vol: 0.13 }, { at: 1.6, keys: pr[1], len: 1.8, vol: 0.13 }, { at: 4.4, keys: pr[0], len: 1.4, vol: 0.13 }, { at: 6, keys: pr[1], len: 1.8, vol: 0.13 }], 72);
// triads, root position and inverted, within an octave from middle C: [root, 'maj' | 'min', inversion 0 | 1 | 2]
const L4_TRI_Q = { maj: [0, 4, 7], min: [0, 3, 7] };
// the lowest note between the A flat below middle C and the G above it, so the whole triad sits between G below and E above
const l4Tri = (r, q, inv) => { const n = L4_TRI_Q[q].map(x => r + x); for (let j = 0; j < inv; j++) n.push(n.shift() + 12); while (n[0] > 7) n.forEach((_, i) => { n[i] -= 12; }); while (n[0] < -4) n.forEach((_, i) => { n[i] += 12; }); return n; };
const L4_TRIS = [[0, 'maj', 0], [0, 'maj', 1], [0, 'maj', 2], [2, 'min', 0], [2, 'min', 1], [4, 'min', 0], [5, 'maj', 0], [5, 'maj', 1], [7, 'maj', 2], [9, 'min', 2], [9, 'min', 1], [7, 'maj', 1], [2, 'min', 2], [4, 'min', 2],
  [2, 'maj', 0], [9, 'maj', 1], [4, 'maj', 2], [0, 'min', 0], [7, 'min', 1]];
const L4_INVW = [['root position', '기본형'], ['first inversion', '첫째 자리바꿈'], ['second inversion', '둘째 자리바꿈']];
const l4PlayTri = (n) => spPlay([{ at: 0, keys: n, len: 2.2, vol: 0.12 }, { at: 3.2, keys: n, len: 2.2, vol: 0.12 }], 72);
// clap-back passages for Grade 4, harder than Grades 2-3 ("the difficulty of the examples ... adjusted to the standards of the
// respective Grades", section 21): the dotted quaver and semiquaver, a quaver rest (our choice of what "harder" means: flagged
// to Sohyun); each with its metre (2 or 3)
const L4_CLAP = [
  { m: 2, items: [['ts', 2], ['q'], ['ds'], ['|'], ['qd'], ['e'], ['|'], ['ds'], ['ds'], ['|'], ['h'], ['||']] },
  { m: 3, items: [['ts', 3], ['qd'], ['e'], ['q'], ['|'], ['ds'], ['q'], ['q'], ['|'], ['p'], ['ds'], ['q'], ['|'], ['hd'], ['||']] },
  { m: 2, items: [['ts', 2], ['er'], ['e'], ['q'], ['|'], ['ds'], ['p'], ['|'], ['qd'], ['e'], ['|'], ['h'], ['||']] },
  { m: 3, items: [['ts', 3], ['q'], ['ds'], ['ds'], ['|'], ['h'], ['q'], ['|'], ['qd'], ['e'], ['p'], ['|'], ['hd'], ['||']] },
  { m: 2, items: [['ts', 2], ['ds'], ['q'], ['|'], ['p'], ['ds'], ['|'], ['q'], ['er'], ['e'], ['|'], ['h'], ['||']] },
  { m: 3, items: [['ts', 3], ['h'], ['ds'], ['|'], ['qd'], ['e'], ['q'], ['|'], ['ds'], ['p'], ['q'], ['|'], ['hd'], ['||']] },
];
const L4_CLAP_BPM = 80;

// ── step 1: the keynote, then any interval of the major scale: sing it, then name it in full ──
function L4IvPad({ onResult, fixed }) {
  const [x, setX] = useState(fixed || { k: 0, n: 3 }), [heard, setHeard] = useState(false), [ans, setAns] = useState(null), [run, setRun] = useState(0);
  const d = L4_IV.find(y => y[0] === x.n)[1];
  const play = () => { setHeard(true); l4PlayIv(x.k, d); };
  const fresh = () => { let y, g = 0; do { y = { k: pick(L4_KEYS), n: pick([2, 3, 4, 5, 6, 7, 8]) }; } while (y.k === x.k && y.n === x.n && g++ < 10); setX(y); setAns(null); setHeard(true); l4PlayIv(y.k, L4_IV.find(z => z[0] === y.n)[1]); };
  const say = (c) => { if (!heard || ans) return; setAns(c); const ok = c === x.n; setRun(r => (ok ? r + 1 : 0)); if (onResult) onResult({ ok }); };
  const sc = [0, 2, 4, 5, 7, 9, 11, 12].map(s => x.k + s), lit = {}; if (ans) { lit[x.k] = 'pale'; lit[x.k + d] = ans === x.n ? 'good' : 'cor'; }
  return (
    <div className="try-box" style={actBox} data-l4="iv">
      <div style={actTitle}>{t('Any interval from the keynote', '으뜸음에서 어떤 음정이든')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>먼저 <b>으뜸음</b>, 그다음 장음계의 다른 음(두 번). 그 음을 부르고 <b>온전한 이름</b>을 말해요. 장음계에서 으뜸음 위의 <b>4도, 5도, 8도는 완전</b>, <b>2도, 3도, 6도, 7도는 장</b>음정이에요.</>
        : <>First <b>the keynote</b>, then another note of the major scale (twice). Sing it, then give its <b>full name</b>. Above the keynote of a major scale, <b>the 4th, 5th and octave are perfect</b>; <b>the 2nd, 3rd, 6th and 7th are major</b>.</>}</div>
      <SpKb lo={Math.min(0, x.k)} hi={Math.max(14, x.k + 12)} W={24} H={74} lit={lit} names={ans ? Object.fromEntries(sc.map((s, j) => [s, String(j + 1)])) : { [x.k]: '1' }} label={t('The keynote and the scale', '으뜸음과 음계')}/>
      {heard && <div style={{display:'grid',gridTemplateColumns:'repeat(4,minmax(0,1fr))',gap:6,marginTop:10}}>{[2, 3, 4, 5, 6, 7, 8].map(n => <button key={n} className={'choice-btn' + (!ans ? '' : n === x.n ? ' good' : n === ans ? ' bad' : '')} onClick={() => say(n)} style={{padding:'10px 2px',fontSize:13.5,fontWeight:900,lineHeight:1.15}}>{l4IvName(n)}</button>)}</div>}
      {lwMsg(!heard ? t('Tap ▶ to hear the keynote and the note.', '▶를 누르면 으뜸음과 음이 나와요.') : ans ? (ans === x.n ? t('Yes: a ' + l4IvName(x.n) + '. ' + (run > 1 ? run + ' in a row.' : ''), '맞아요: ' + l4IvName(x.n) + '. ' + (run > 1 ? run + '번 연속.' : '')) : t('It was a ' + l4IvName(x.n) + ': sing up the scale from the keynote, 1 to ' + x.n + '.', l4IvName(x.n) + '였어요: 으뜸음에서 1부터 ' + x.n + '까지 음계를 올라가며 불러 봐요.')) : t('Sing it, then name it.', '부르고, 이름을 말해요.'), ans ? (ans === x.n ? BK.green : BK.coral) : undefined)}
      {lwRow(<>
        <button className="ghost-btn" style={lwBtn} onClick={heard && !fixed ? fresh : play}>{!heard ? t('▶ Keynote, then the note', '▶ 으뜸음, 그다음 음') : fixed ? t('♪ Again', '♪ 다시') : t('▶ Another', '▶ 다른 것')}</button>
        {heard && !fixed && <button className="ghost-btn" style={lwBtn} onClick={play}>{t('♪ Again', '♪ 다시')}</button>}
        {heard && <button className="ghost-btn" style={lwBtn} onClick={() => spPlay([0, 2, 4, 5, 7, 9, 11, 12].map((s, j) => ({ at: j * 0.55, keys: [x.k + s], len: 0.5 })), 100)}>{t('♪ The scale', '♪ 음계')}</button>}
      </>)}
    </div>
  );
}

// ── step 2: two intervals in two parts; sing the higher part or the lower part from memory, then find its two notes ──
function L4TwoPad({ onResult, fixed }) {
  const [x, setX] = useState(fixed || { pr: L4_TWO[0], ask: 'hi' }), [heard, setHeard] = useState(false), [got, setGot] = useState(0), [miss, setMiss] = useState(0), [wrong, setWrong] = useState(null);
  const part = x.pr.map(iv => x.ask === 'hi' ? iv[1] : iv[0]), done = got >= 2;
  const play = () => { setHeard(true); l4PlayTwo(x.pr); };
  const fresh = () => { let y, g = 0; do { y = { pr: pick(L4_TWO), ask: Math.random() < 0.5 ? 'hi' : 'lo' }; } while (y.pr === x.pr && y.ask === x.ask && g++ < 10); setX(y); setGot(0); setMiss(0); setWrong(null); setHeard(true); l4PlayTwo(y.pr); };
  const tap = (k) => { playKey(k, 0.5); if (!heard || done) return; if (k === part[got]) { const g = got + 1; setGot(g); setWrong(null); if (g >= 2 && onResult) onResult({ ok: miss === 0 }); } else { setMiss(m => m + 1); setWrong(k); } };
  const lit = {}; if (done) { x.pr.forEach(iv => iv.forEach(k => { lit[k] = 'pale'; })); part.forEach(k => { lit[k] = 'good'; }); } else { if (got > 0) lit[part[0]] = 'cor'; if (wrong != null) lit[wrong] = 'bad'; }
  const askW = x.ask === 'hi' ? t('the higher part', '윗성부') : t('the lower part', '아랫성부');
  return (
    <div className="try-box" style={actBox} data-l4="two">
      <div style={actTitle}>{t('Two parts: sing one', '두 성부: 하나를 불러요')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>두 음씩 <b>두 번</b> 함께 울려요(전체를 두 번). 외워서 <b>{askW}</b>의 두 음을 부르고, 건반에서 차례로 찾아요. 윗성부는 새, 아랫성부는 거북이.</>
        : <>Two notes together, <b>twice in a row</b> (all of it played twice). From memory, sing the two notes of <b>{askW}</b>, then find them on the keys in order. The higher part is the bird's, the lower the turtle's.</>}</div>
      {heard && <div style={{textAlign:'center',fontSize:16,fontWeight:900,color:BK.coral,margin:'0 0 6px'}}>{x.ask === 'hi' ? t('Sing the higher part ↑', '윗성부를 불러요 ↑') : t('Sing the lower part ↓', '아랫성부를 불러요 ↓')}</div>}
      <SpKb lo={0} hi={12} W={34} H={86} lit={lit} names={done ? Object.fromEntries(x.pr.flat().map(k => [k, l4Let(k)])) : { 0: 'C' }} onTap={tap} label={t('Find the part you sang', '부른 성부 찾기')}/>
      {lwMsg(!heard ? t('Tap ▶ to hear the two parts.', '▶를 누르면 두 성부가 나와요.') : done ? t(askW.charAt(0).toUpperCase() + askW.slice(1) + ': ' + part.map(l4Let).join(' then ') + '. ' + (miss ? 'Found it.' : 'First time!'), askW + ': ' + part.map(l4Let).join(', 그다음 ') + '. ' + (miss ? '찾았어요.' : '한 번에!'))
        : wrong != null ? t('Not that one: sing the part again, then try.', '그 음이 아니에요: 다시 불러 보고 찾아요.') : t('Sing it, then find note ' + (got + 1) + ' of 2.', '부르고, 두 음 중 ' + (got + 1) + '번째를 찾아요.'), done ? BK.green : wrong != null ? BK.coral : undefined)}
      {lwRow(<>
        <button className="ghost-btn" style={lwBtn} onClick={heard && !fixed ? fresh : play}>{!heard ? t('▶ Play the two parts', '▶ 두 성부 듣기') : fixed ? t('♪ Again', '♪ 다시') : t('▶ Another', '▶ 다른 것')}</button>
        {heard && !fixed && <button className="ghost-btn" style={lwBtn} onClick={play}>{t('♪ Again', '♪ 다시')}</button>}
        {heard && !done && <button className="ghost-btn" style={lwBtn} onClick={() => spPlay(part.map((k, j) => ({ at: j * 1.2, keys: [k], len: 1.1 })), 84)}>{t('♪ Just that part', '♪ 그 성부만')}</button>}
      </>)}
    </div>
  );
}

// ── step 3: a triad, root position or inverted: sing its middle note, then find it ──
function L4MidPad({ onResult, fixed }) {
  const [x, setX] = useState(fixed || L4_TRIS[0]), [heard, setHeard] = useState(false), [res, setRes] = useState(null), [tries, setTries] = useState([]);
  const n = l4Tri(x[0], x[1], x[2]), mid = n[1];
  const play = () => { setHeard(true); l4PlayTri(n); };
  const fresh = () => { let y, g = 0; do { y = pick(L4_TRIS); } while (y === x && g++ < 10); setX(y); setRes(null); setTries([]); setHeard(true); l4PlayTri(l4Tri(y[0], y[1], y[2])); };
  const tap = (k) => { playKey(k, 0.5); if (!heard || res) return; if (k === mid) { const r = { ok: tries.length === 0 }; setRes(r); if (onResult) onResult(r); } else setTries(ts => [...ts, k]); };
  const last = tries[tries.length - 1], lit = {}; if (res) { n.forEach(k => { lit[k] = 'pale'; }); lit[mid] = 'good'; } else if (last != null) lit[last] = 'bad';
  const name = l4Let(x[0]) + (x[1] === 'maj' ? t(' major', '장3화음') : t(' minor', '단3화음')), inv = t(L4_INVW[x[2]][0], L4_INVW[x[2]][1]);
  return (
    <div className="try-box" style={actBox} data-l4="mid">
      <div style={actTitle}>{t('The middle note of a triad', '3화음의 가운데 음')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>장3화음이나 단3화음이 울려요(두 번). 기본형일 수도, 자리바꿈일 수도 있어요. 세 음 중 <b>가운데 음</b>을 흥얼거리고 건반에서 찾아요. 맨 위와 맨 아래는 쉬우니까, 그 사이를 노려요.</>
        : <>A major or minor triad sounds (twice), in root position or inverted. Hum <b>the middle note</b> of the three, then find it on the keys. The top and the bottom are easy to hear: aim between them.</>}</div>
      <SpKb lo={-5} hi={16} W={24} H={76} lit={lit} names={res ? Object.fromEntries(n.map(k => [k, l4Let(k)])) : { 0: 'C' }} onTap={tap} label={t('Find the middle note', '가운데 음 찾기')}/>
      {lwMsg(!heard ? t('Tap ▶ to hear the triad.', '▶를 누르면 3화음이 나와요.') : res ? t(name + ', ' + inv + ': the middle note is ' + l4Let(mid) + '. ' + (res.ok ? 'First time!' : 'Found it.'), name + ', ' + inv + ': 가운데 음은 ' + l4Let(mid) + '. ' + (res.ok ? '한 번에!' : '찾았어요.'))
        : last != null ? t('Not that one: hum the top, the bottom, then between.', '그 음이 아니에요: 맨 위, 맨 아래, 그다음 그 사이를 흥얼거려요.') : t('Hum it first, then tap the key.', '먼저 흥얼거리고, 건반을 눌러요.'), res ? BK.green : last != null ? BK.coral : undefined)}
      {lwRow(<>
        <button className="ghost-btn" style={lwBtn} onClick={heard && !fixed ? fresh : play}>{!heard ? t('▶ Play a triad', '▶ 3화음 듣기') : fixed ? t('♪ Again', '♪ 다시') : t('▶ Another', '▶ 다른 것')}</button>
        {heard && !fixed && <button className="ghost-btn" style={lwBtn} onClick={play}>{t('♪ Again', '♪ 다시')}</button>}
        {heard && !res && <button className="ghost-btn" style={lwBtn} onClick={() => spPlay(n.map((k, j) => ({ at: j * 0.8, keys: [k], len: 0.75 })), 90)}>{t('♪ One at a time', '♪ 하나씩')}</button>}
      </>)}
    </div>
  );
}

// ── step 4: clap it back, then say two or three (heard twice) ──
function L4ClapPad({ onResult, fixed }) {
  const T = usePlTimers();
  const [i, setI] = useState(fixed != null ? fixed : 0), [phase, setPhase] = useState('ready'), [heard, setHeard] = useState(0), [res, setRes] = useState(null), [met, setMet] = useState(null);
  const run = useRef(null), taps = useRef([]);
  const P = L4_CLAP[i], items = P.items, snd = srhSounds(items), notes = snd.map((s, j) => [s, j]).filter(([s]) => !s.rest), top = P.m, n = srhBeats(items);
  const reset = () => { T.clear(); stopClicks(); setPhase('ready'); setHeard(0); setRes(null); setMet(null); };
  const listen = () => { T.clear(); setRes(null); setMet(null); const r = rqRunS(items, { bpm: L4_CLAP_BPM }); if (!r) return; setPhase('listen');
    T.at(r, r.at[r.lead] + n * r.spb, () => { const r2 = rqRunS(items, { bpm: L4_CLAP_BPM }); if (!r2) return; T.at(r2, r2.at[r2.lead] + n * r2.spb + 0.2, () => { setPhase('ready'); setHeard(2); }); }); setHeard(1); };
  const go = () => { T.clear(); setRes(null); setMet(null); taps.current = []; const r = rqRunS(items, { bpm: L4_CLAP_BPM, silent: true }); if (!r) return; run.current = r; setPhase('count');
    const g = r.at[r.lead]; T.at(r, g - 0.05, () => setPhase('tap'));
    T.at(r, g + n * r.spb + 0.1, () => { const tol = Math.min(PL_TOL, r.spb * 0.18), mt = plMatch(notes.map(([s]) => g + s.b * r.spb), taps.current.filter(tp => tp > g - tol), tol), marks = {};
      notes.forEach(([s, j], k) => { marks[j] = mt.offs[k] === null ? '?' : '✓'; });
      setRes({ hits: mt.hits, total: notes.length, extra: mt.extra, marks, ok: mt.hits >= notes.length - 1 && mt.extra <= 1 }); setPhase('done'); }); };
  const say = (m) => { if (!res || met) return; setMet(m); if (onResult) onResult({ ok: res.ok && m === top, clap: res.ok, metre: m === top }); };
  const tap = React.useCallback(() => { const r = run.current; if (r && (phase === 'count' || phase === 'tap')) { taps.current.push(r.now()); const ctx = getAudio(); if (ctx) blip(ctx, ctx.currentTime, SRH_HZ, 0.1, 0.16, 'triangle'); } }, [phase]);
  return (
    <div className="try-box" style={actBox} data-l4="clap">
      <div style={actTitle}>{t('Clap it back: two or three?', '따라 치고, 두 박? 세 박?')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>리듬을 <b>두 번</b> 들어요. 클릭에 맞춰 똑같이 치고, <b>두 박인지 세 박인지</b> 말해요. 이번에는 <b>점8분음표와 16분음표</b>(길게-짧게, 콩-닥)와 <b>8분쉼표</b>도 나와요.</>
        : <>Hear the passage <b>twice</b>. Tap it back with the clicks, then say <b>two or three</b>. Now with <b>the dotted quaver and semiquaver</b> (long-short, snappy) and <b>a quaver rest</b>.</>}</div>
      {!fixed && spChips(L4_CLAP.map((_, j) => [j, t('Passage ' + (j + 1), (j + 1) + '번')]), i, (j) => { reset(); setI(j); })}
      {met ? rqStaffEl(items, { marks: res.marks, hearts: false }) : <div style={{textAlign:'center',fontSize:14,fontWeight:900,color:BK.muted,margin:'6px 0'}}>{t(['Not heard yet', 'Heard once', 'Heard twice'][heard], ['아직 안 들었어요', '한 번 들었어요', '두 번 들었어요'][heard])}</div>}
      {lwMsg(phase === 'listen' ? t('Listen…', '들어요…') : phase === 'count' ? t('Get ready…', '준비…') : phase === 'tap' ? t('Tap it back!', '따라 쳐요!') : res && !met ? t('On time: ' + res.hits + ' of ' + res.total + '. Two or three?', '제때: ' + res.total + '개 중 ' + res.hits + '개. 두 박? 세 박?')
        : met ? t((res.ok ? 'Clapped back ✓ ' : 'Clap: nearly. ') + (met === top ? (top === 2 ? 'Two ✓' : 'Three ✓') : 'It was ' + (top === 2 ? 'two.' : 'three.')), (res.ok ? '따라 치기 ✓ ' : '따라 치기: 거의. ') + (met === top ? (top === 2 ? '두 박 ✓' : '세 박 ✓') : (top === 2 ? '두 박이었어요.' : '세 박이었어요.'))) : '', met ? (res.ok && met === top ? BK.green : BK.coral) : undefined)}
      {res && !met && <div style={{display:'grid',gridTemplateColumns:'repeat(2,minmax(0,1fr))',gap:8,marginTop:8}}>{[[2, t('Two', '두 박')], [3, t('Three', '세 박')]].map(([m, lab]) => <button key={m} className="choice-btn" onClick={() => say(m)} style={{padding:'12px 4px',fontSize:16,fontWeight:900}}>{lab}</button>)}</div>}
      <PlPad on={phase === 'count' || phase === 'tap'} onTap={tap}/>
      {lwRow(<>
        <button className="ghost-btn" style={lwBtn} onClick={listen}>{t('▶ Listen (twice)', '▶ 듣기 (두 번)')}</button>
        <button className="ghost-btn" style={lwBtn} disabled={!heard} onClick={go}>{res ? t('▶ Again', '▶ 다시') : t('▶ Tap it back', '▶ 따라 치기')}</button>
      </>)}
      {plHint()}
    </div>
  );
}

// ── the pictures on paper ──
const l4PicIv = () => lsRawPic([1, 2, 3, 4, 5, 6, 7, 8].map((n, i) => lsCircleSvg(6 + i * 9.5, 38 - i * 4.4, 4.6, n === 1 || n === 6 ? 'play' : 'beat', String(n))).join(''), [0, 0, 84, 44]);
const l4PicTwo = () => lsRawPic('<ellipse cx="22" cy="14" rx="6" ry="4.4" transform="rotate(-20 22 14)" fill="#e4572e"/><ellipse cx="22" cy="30" rx="6" ry="4.4" transform="rotate(-20 22 30)" fill="#26296b"/><ellipse cx="50" cy="10" rx="6" ry="4.4" transform="rotate(-20 50 10)" fill="#e4572e"/><ellipse cx="50" cy="26" rx="6" ry="4.4" transform="rotate(-20 50 26)" fill="#26296b"/><path d="M28 14 L44 10" stroke="#e4572e" stroke-width="2" stroke-dasharray="3 2"/>', [0, 0, 74, 44]);
const l4PicMid = () => lsRawPic('<ellipse cx="34" cy="34" rx="6.5" ry="4.6" transform="rotate(-20 34 34)" fill="#26296b"/><ellipse cx="34" cy="22" rx="6.5" ry="4.6" transform="rotate(-20 34 22)" fill="#e4572e"/><ellipse cx="34" cy="10" rx="6.5" ry="4.6" transform="rotate(-20 34 10)" fill="#26296b"/>', [0, 0, 70, 44]);
const l4PicClap = () => lsPicEcho();
const l4Kb = (lit, names, scr, lo = 0, hi = 14) => <SpKb lo={lo} hi={hi} W={scr ? 26 : 36} H={scr ? 66 : 92} lit={lit} names={names}/>;

function l4LbPages(scr = false) {
  const ch = 'listen-4';
  const checks4 = [[l4PicIv(), t('I sing and name any interval of the major scale from the keynote', '으뜸음에서 장음계의 어떤 음정이든 부르고 이름을 말해요')], [l4PicTwo(), t('I sing the higher or the lower part of two intervals', '두 음정에서 윗성부나 아랫성부를 불러요')],
    [l4PicMid(), t('I hum the middle note of a triad, root position or inverted', '기본형이든 자리바꿈이든 3화음의 가운데 음을 흥얼거려요')], [l4PicClap(), t('I tap back a passage and say two or three', '리듬을 따라 치고 두 박인지 세 박인지 말해요')]];
  const pen = (x) => <PenArt shapes={x.shapes} vb={x.vb} style={{width:90}}/>;
  const toc = [[t('Any interval from the keynote', '으뜸음에서 어떤 음정이든'), 2], [t('Two parts: sing one', '두 성부: 하나를 불러요'), 3], [t('The middle note of a triad', '3화음의 가운데 음'), 4], [t('Clap it back: two or three?', '따라 치고, 두 박? 세 박?'), 5], [t('My four checks', '나의 네 가지 확인'), 6]];
  const ivRow = (k) => <div style={{width:'100%',maxWidth:560,margin:'0 auto'}}><SpKb maxW={560} lo={0} hi={14} W={scr ? 26 : 34} H={scr ? 66 : 84} lit={Object.fromEntries([0, 2, 4, 5, 7, 9, 11, 12].map((s, j) => [k + s, j === 0 ? 'cor' : 'pale']))} names={Object.fromEntries([0, 2, 4, 5, 7, 9, 11, 12].map((s, j) => [k + s, String(j + 1)]))}/></div>;
  const ivTable = <div style={{display:'grid',gridTemplateColumns:'repeat(4,minmax(0,1fr))',gap:'4px 10px',maxWidth:560,margin:'8px auto 0',fontSize:scr ? 13 : 13.5,fontWeight:800,color:BK.ink}}>{[2, 3, 4, 5, 6, 7, 8].map(n => <div key={n}><b style={{color:[4, 5, 8].includes(n) ? BK.coral : BK.ink}}>1 → {n}</b> {l4IvName(n)}</div>)}</div>;
  const triStill = (list) => <LbPic h={170}><div style={{display:'grid',gridTemplateColumns:'1fr',gap:scr ? 12 : 16,width:'100%',maxWidth:scr ? 680 : 440,margin:'0 auto'}}>{list.map(([r, q, inv]) => { const n = l4Tri(r, q, inv);
    return <div key={r + q + inv}><div style={{textAlign:'center',fontSize:13,fontWeight:900,color:BK.ink,marginBottom:2}}>{l4Let(r)}{q === 'maj' ? t(' major', '장3화음') : t(' minor', '단3화음')}: {t(L4_INVW[inv][0], L4_INVW[inv][1])}</div>{l4Kb({ [n[0]]: 'pale', [n[1]]: 'cor', [n[2]]: 'pale' }, Object.fromEntries(n.map(k => [k, l4Let(k)])), scr, 0, 16)}</div>; })}</div></LbPic>;
  const twoStill = (pr) => <LbPic h={160}><div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:14,width:'100%',maxWidth:620,margin:'0 auto'}}>{pr.map((iv, j) => <div key={j}><div style={{textAlign:'center',fontSize:13,fontWeight:900,color:BK.ink,marginBottom:2}}>{t('Interval ' + (j + 1), (j + 1) + '번 음정')}: {l4Let(iv[0])} + {l4Let(iv[1])}</div>{l4Kb({ [iv[0]]: 'pale', [iv[1]]: 'cor' }, { [iv[0]]: l4Let(iv[0]), [iv[1]]: l4Let(iv[1]) }, scr, 0, 12)}</div>)}</div></LbPic>;
  return [
    <LbPage key="1" no={1} chId={ch} teacher={<>{t('The Grade 4 aural tests, one step each (Manual of Syllabuses, section 21): the keynote, then any interval of the major scale straight after it, sung and named in full (Grades 4 to 6 name intervals as major 2nd, major 3rd, perfect 4th and so on); the higher or the lower part of a two-part progression of two successive intervals, within an octave from middle C, sung from memory; a major or minor triad, root position or inverted, within an octave: hum the middle note; a passage in duple or triple time played twice, tapped back and named. The app plays and scores the taps and answers; whether a child sang in tune is your ear.', '4급 청음 시험을 한 단계씩(실라버스 21절): 으뜸음 다음에 바로 장음계의 어떤 음정이든 부르고 온전한 이름 말하기(4~6급은 장2도, 장3도, 완전4도처럼 이름을 말해요); 연속된 두 음정으로 된 두 성부 진행에서 윗성부나 아랫성부를 외워서 부르기(가운데 도부터 한 옥타브 안); 기본형이나 자리바꿈의 장·단3화음에서 가운데 음 흥얼거리기(한 옥타브 안); 두 박이나 세 박 리듬을 두 번 듣고 따라 치고 박자 말하기. 앱은 탭과 답을 채점하고, 음정이 맞았는지는 선생님의 귀예요.')}</>}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:50,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{bkChapterName(ch)}</div>
      </div></LbOnly>
      <LbPic h={170}><div style={{width:'100%'}}>{ivRow(0)}{ivTable}</div></LbPic>
      <LbSay size={18}>{t('Your ears for Grade 4: every interval of the major scale by name, two parts at once, the middle of a chord, and harder rhythms.', '4급의 귀: 장음계의 모든 음정을 이름으로, 한꺼번에 두 성부, 화음의 가운데, 더 어려운 리듬.')}</LbSay>
      <div className="lb-toc" style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>
        <LbOnly print><div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('In this chapter', '이 챕터에서는')}</div>
          {toc.map(([n, p]) => <div key={p} className="lb-toc-row" style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:14.5,padding:'5px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkGoal(15)}{n}</span><span style={{color:BK.muted,fontWeight:700}}>{p}</span></div>)}
        </div></LbOnly>
        <div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 챕터를 마치면')}</div>
          {checks4.map(([, x], i) => <div key={i} style={{display:'flex',alignItems:'flex-start',gap:9,fontSize:14.5,padding:'5px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}>{bkGoal(15)}<span>{x.replace(/^I /, '').replace(/^나는 /, '')}</span></div>)}
        </div>
      </div>
      <LbOnly print><LbDrillStrip id={ch}/></LbOnly>
    </LbPage>,
    <LbPage key="2" no={2} chId={ch} kicker={t('Step 1', '1단계')} title={t('Any interval from the keynote', '으뜸음에서 어떤 음정이든')}
      teacher={<>{t('Grade 4: you sound the keynote, then any note of its major scale straight after it (up to the octave); the child sings it, then names it in full: "a major 6th". Played twice. The rule that gives the full name: above the keynote of a major scale, the 4th, 5th and octave are perfect; the 2nd, 3rd, 6th and 7th are major. To find the number, sing up the scale from the keynote.', '4급: 으뜸음을 울린 다음 바로 그 장음계의 어떤 음이든(옥타브까지) 쳐요. 아이는 그 음을 부르고 온전한 이름을 말해요: "장6도". 두 번 들려줘요. 이름을 정하는 규칙: 장음계의 으뜸음 위에서 4도, 5도, 8도는 완전, 2도, 3도, 6도, 7도는 장음정. 숫자를 찾으려면 으뜸음에서 음계를 올라가며 불러요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=1')}>
      <LbLive still={<LbPic h={170}><div style={{width:'100%'}}>{ivRow(0)}{ivTable}</div></LbPic>} live={<L4IvPad/>}/>
      <LbSay>{LANG === 'ko' ? <>먼저 <b>으뜸음(1)</b>, 그다음 음계의 다른 음. 1에서 음계를 올라가며 불러서 숫자를 찾아요. 그리고 이름: <b>4도, 5도, 8도는 완전</b>, <b>나머지는 장</b>.</> : <>First <b>the keynote (1)</b>, then another note of its scale. Sing up the scale from 1 to find the number. Then the name: <b>the 4th, 5th and octave are perfect</b>; <b>the rest are major</b>.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>선생님이 으뜸음과 다른 음을 두 번 쳐요. 그 음을 불러요.</>, <>으뜸음에서 음계를 올라가며 불러서 숫자를 찾아요.</>, <>온전한 이름을 말해요: "완전5도", "장6도".</>]
        : [<>Your teacher plays the keynote and another note, twice. Sing the note.</>, <>Sing up the scale from the keynote to find its number.</>, <>Say its full name: "a perfect 5th", "a major 6th".</>]}/>
      <LbRemember>{t('In a major scale, from home: 4, 5, 8 perfect; 2, 3, 6, 7 major.', '장음계에서 집부터: 4, 5, 8은 완전, 2, 3, 6, 7은 장음정.')}</LbRemember>
    </LbPage>,
    <LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={t('Two parts: sing one', '두 성부: 하나를 불러요')}
      teacher={<>{t('Grade 4: two intervals played one after the other, in two parts, within an octave from middle C; the child sings the higher or the lower part (two notes) from memory, as asked. Played twice. If it is hard, play each part alone once, then both again; the top part is usually easier first.', '4급: 두 음정을 차례로, 두 성부로 쳐요(가운데 도부터 한 옥타브 안). 아이는 묻는 대로 윗성부나 아랫성부(두 음)를 외워서 불러요. 두 번 들려줘요. 어려우면 각 성부를 한 번씩 따로 친 다음 다시 함께 쳐 주세요. 보통 윗성부가 먼저 잘 들려요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=2')}>
      <LbLive still={twoStill(L4_TWO[0])} live={<L4TwoPad/>}/>
      <LbSay>{LANG === 'ko' ? <>두 음씩 두 번 울려요. 위의 두 음이 <b>윗성부</b>(새), 아래의 두 음이 <b>아랫성부</b>(거북이). 묻는 성부의 두 음을 외워서 불러요.</> : <>Two notes together, twice in a row. The top two notes are <b>the higher part</b> (the bird's), the bottom two <b>the lower part</b> (the turtle's). Sing the two notes of the part you are asked for, from memory.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>선생님이 두 음정을 차례로 두 번 쳐요. 윗성부를 불러요.</>, <>이번엔 아랫성부. 어려우면 선생님이 한 성부만 쳐 줘요.</>, <>부른 두 음을 건반에서 찾아요.</>]
        : [<>Your teacher plays the two intervals, twice. Sing the higher part.</>, <>Now the lower part. If it is hard, your teacher plays one part alone.</>, <>Find the two notes you sang on the keys.</>]}/>
      <LbRemember>{t('Two parts at once: follow one line.', '두 성부가 함께: 한 줄만 따라가요.')}</LbRemember>
    </LbPage>,
    <LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title={t('The middle note of a triad', '3화음의 가운데 음')}
      teacher={<>{t('Grade 4: any major or minor triad, in root position or an inversion, played within an octave; the child hums or sings the middle note. Played twice. In root position the middle note is the 3rd; in first inversion, the 5th; in second inversion, the root. If it is hard, play the three notes one at a time, then together again.', '4급: 장3화음이나 단3화음을 기본형이나 자리바꿈으로 한 옥타브 안에서 쳐요. 아이는 가운데 음을 흥얼거리거나 불러요. 두 번 들려줘요. 기본형에서 가운데 음은 3음, 첫째 자리바꿈에서는 5음, 둘째 자리바꿈에서는 근음이에요. 어려우면 세 음을 하나씩 친 다음 다시 함께 쳐 주세요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=3')}>
      <LbLive still={triStill([[0, 'maj', 0], [0, 'maj', 1], [0, 'maj', 2]])} live={<L4MidPad/>}/>
      <LbSay>{LANG === 'ko' ? <>3화음은 세 음. 맨 위와 맨 아래는 잘 들리고, <b>가운데 음</b>은 그 사이에 숨어 있어요. 자리바꿈을 해도 가운데는 가운데예요.</> : <>A triad is three notes. The top and the bottom stand out; <b>the middle note</b> hides between them. Inverted or not, the middle is the middle.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>선생님이 3화음을 두 번 쳐요. 맨 위, 맨 아래를 흥얼거려 봐요.</>, <>이제 그 사이의 가운데 음을 흥얼거려요.</>, <>건반에서 찾아요.</>]
        : [<>Your teacher plays a triad, twice. Hum the top, then the bottom.</>, <>Now hum the middle note, between them.</>, <>Find it on the keys.</>]}/>
      <LbRemember>{t('Top, bottom, then the one between.', '맨 위, 맨 아래, 그다음 그 사이.')}</LbRemember>
    </LbPage>,
    <LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title={t('Clap it back: two or three?', '따라 치고, 두 박? 세 박?')}
      teacher={<>{t('Grade 4: a passage in duple or triple time played twice; the child taps or claps it back and says whether it is in duple or triple time. The Manual adjusts the difficulty of the examples to each grade, so these passages add the dotted quaver and semiquaver and a quaver rest. Listen both times without clapping; count inside.', '4급: 두 박이나 세 박의 리듬을 두 번 쳐요. 아이는 따라 치고 두 박인지 세 박인지 말해요. 실라버스는 급에 맞춰 예제의 난이도를 조절하니까, 이번 리듬에는 점8분음표와 16분음표, 8분쉼표가 나와요. 두 번 다 손뼉 치지 않고 들으며 속으로 세요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=4')}>
      <LbLive still={<LbPic h={150}><div style={{width:'100%',maxWidth:560,margin:'0 auto'}}>{rqStaffEl(L4_CLAP[1].items, { hearts: false })}</div></LbPic>} live={<L4ClapPad/>}/>
      <LbSay>{LANG === 'ko' ? <>두 번 듣고, 같은 빠르기로 따라 치고, <b>두 박인지 세 박인지</b> 말해요. <b>점8분음표와 16분음표</b>는 길게-짧게, 콩-닥.</> : <>Hear it twice, tap it back at the same speed, then say <b>two or three</b>. <b>The dotted quaver and semiquaver</b>: long-short, snappy.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>선생님이 네 마디를 두 번 쳐요. 듣기만 하며 속으로 세요.</>, <>같은 빠르기로 따라 쳐요.</>, <>두 박이었나요, 세 박이었나요?</>]
        : [<>Your teacher plays four bars, twice. Just listen and count inside.</>, <>Tap it back at the same speed.</>, <>Two or three?</>]}/>
      <LbRemember>{t('Clap it back, then say two or three.', '따라 치고, 두 박인지 세 박인지 말해요.')}</LbRemember>
    </LbPage>,
    <LbPage key="6" no={6} chId={ch} kicker={t('Check-up', '점검')} title={t('My four checks', '나의 네 가지 확인')}
      teacher={<>{t('Each one with you at the piano, away from the screen, played twice as in the exam: you play, the child sings, names or claps. You only correct.', '하나씩 화면 없이 피아노 앞에서, 시험처럼 두 번씩: 선생님이 치고, 아이는 부르고, 이름을 말하고, 손뼉 쳐요. 선생님은 고쳐 주기만 해요.')}</>}>
      <LbSay>{t('Tick each one: not yet, nearly, or got it!', '하나씩 표시해요: 아직, 거의, 됐어요!')}</LbSay>
      <LbLive still={<LbStageRows big rows={checks4.map(([a, txt]) => [pen(a), txt])}/>} live={<FiveChecks376 rows={checks4} storeKey="pb_l4_four"/>}/>
    </LbPage>,
  ];
}
function Listen4LessonBook() { return <>{l4LbPages(false)}</>; }
function L4Learn({ onStart }) {
  const pages = l4LbPages(true), opener = pages[0];
  return (
    <Lesson id="listen-4" title={bkChapterName('listen-4')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="listen-4"><div className="lb-screen lb-open" style={{display:'flex',flexDirection:'column',gap:12,margin:'0 0 8px'}}>{lbWordsFirst(opener.props.children)}</div></BkChapterCtx.Provider></LbScreenCtx.Provider>}>
      {pages.slice(1).map((pg, i) => <Step key={i} title={pg.props.title}><LbScreenPage page={pg}/></Step>)}
    </Lesson>
  );
}
// ── the drill: every question is heard (twice, as the tests are) ──
const L4_LEVELS = [
  { n: 1, label: 'From the keynote: name the interval', kind: 'iv', time: 20 },
  { n: 2, label: 'Two parts: sing the higher or the lower', kind: 'two', time: 40 },
  { n: 3, label: 'A triad: hum the middle note', kind: 'mid', time: 30 },
  { n: 4, label: 'Clap it back, then two or three', kind: 'clap', time: 45 },
  { n: 5, label: 'All four, mixed, as in the exam', kind: 'mix', time: 45 },
];
Object.assign(LEVEL_KO, { 'From the keynote: name the interval': '으뜸음에서: 음정 이름', 'Two parts: sing the higher or the lower': '두 성부: 윗성부나 아랫성부 부르기', 'A triad: hum the middle note': '3화음: 가운데 음', 'All four, mixed, as in the exam': '네 가지 섞어서, 시험처럼' });
function genL4Question(lv, prev) {
  const uid = Math.random(); let kind = lv.kind;
  if (kind === 'mix') { const ks = ['iv', 'two', 'mid', 'clap'].filter(k => !prev || prev.kind !== k); kind = pick(ks); }
  if (kind === 'iv') { let k, n, g = 0; do { k = pick(L4_KEYS); n = pick([2, 3, 4, 5, 6, 7, 8]); } while (prev && prev.key === k + '-' + n && g++ < 10); return { kind, k, n, answer: n, choices: [2, 3, 4, 5, 6, 7, 8], key: k + '-' + n, uid }; }
  if (kind === 'two') { let pr, ask, g = 0; do { pr = pick(L4_TWO); ask = Math.random() < 0.5 ? 'hi' : 'lo'; } while (prev && prev.key === JSON.stringify(pr) + ask && g++ < 10); return { kind, fx: { pr, ask }, answer: 'ok', choices: [], key: JSON.stringify(pr) + ask, uid }; }
  if (kind === 'mid') { let x, g = 0; do { x = pick(L4_TRIS); } while (prev && prev.key === x.join() && g++ < 10); return { kind, fx: x, answer: 'ok', choices: [], key: x.join(), uid }; }
  let i, g = 0; do { i = Math.floor(Math.random() * L4_CLAP.length); } while (prev && prev.i === i && g++ < 10); return { kind: 'clap', i, answer: 'ok', choices: [], key: 'c' + i, uid };
}
function l4AnswerLabel(q) {
  if (q.kind === 'iv') return l4IvName(q.answer);
  return t('done', '완료');
}
function L4Question({ q, given, locked, onAnswer, pixel }) {
  const done = !!given;
  const play = () => { stopClicks(); if (q.kind === 'iv') l4PlayIv(q.k, L4_IV.find(y => y[0] === q.n)[1]); };
  useEffect(() => { if (q.kind !== 'iv') return; const id = setTimeout(play, 350); return () => { clearTimeout(id); stopClicks(); }; }, [q.uid]);
  const btnCls = pixel ? 'pixel-choice' : 'choice-btn', cls = (c) => btnCls + (!done ? '' : c === q.answer ? ' good' : given.ans === c ? ' bad' : '');
  const pickIt = (c) => { if (locked || done) return; stopClicks(); onAnswer(c); };
  let title, body;
  if (q.kind === 'iv') { title = t('The keynote, then a note of its major scale: name the interval.', '으뜸음, 그다음 그 장음계의 음: 음정 이름은?');
    body = <div style={{display:'grid',gridTemplateColumns:'repeat(4,minmax(0,1fr))',gap:6}}>{[2, 3, 4, 5, 6, 7, 8].map(c => <button key={c} disabled={locked} className={cls(c)} style={{padding:'10px 2px',fontSize:13.5,fontWeight:900,lineHeight:1.15}} onClick={() => pickIt(c)}>{l4IvName(c)}</button>)}</div>; }
  else if (q.kind === 'two') { title = q.fx.ask === 'hi' ? t('Sing the higher part, then find its two notes.', '윗성부를 부르고, 두 음을 찾아요.') : t('Sing the lower part, then find its two notes.', '아랫성부를 부르고, 두 음을 찾아요.'); body = <L4TwoPad key={q.uid} fixed={q.fx} onResult={(r) => pickIt(r.ok ? 'ok' : 'no')}/>; }
  else if (q.kind === 'mid') { title = t('Hum the middle note of the triad, then find it.', '3화음의 가운데 음을 흥얼거리고, 찾아요.'); body = <L4MidPad key={q.uid} fixed={q.fx} onResult={(r) => pickIt(r.ok ? 'ok' : 'no')}/>; }
  else { title = t('Listen twice, clap it back, then say two or three.', '두 번 듣고, 따라 치고, 두 박인지 세 박인지 말해요.'); body = <L4ClapPad key={q.uid} fixed={q.i} onResult={(r) => pickIt(r.ok ? 'ok' : 'no')}/>; }
  const why = !done ? null : q.kind === 'iv' ? t(l4Let(q.k) + ' to ' + l4Let(q.k + L4_IV.find(y => y[0] === q.n)[1]) + ': a ' + l4IvName(q.n) + ' (in a major scale, 4, 5, 8 perfect; 2, 3, 6, 7 major).', l4Let(q.k) + '에서 ' + l4Let(q.k + L4_IV.find(y => y[0] === q.n)[1]) + ': ' + l4IvName(q.n) + '(장음계에서 4, 5, 8은 완전, 2, 3, 6, 7은 장음정).') : null;
  return (<div>
    <p style={pixel ? {fontSize:11.5,textAlign:'center'} : {fontSize:15,fontWeight:700,textAlign:'center',margin:'0 0 8px',color:'var(--muted)',textWrap:'balance'}}>{title}</p>
    {q.kind === 'iv' && <div style={{textAlign:'center',marginBottom:10}}><button className={pixel ? 'pixel-btn' : 'ghost-btn'} style={{minHeight:44}} onClick={play}>{t('▶ Play it again', '▶ 다시 듣기')}</button></div>}
    {body}
    {why && !pixel && <div style={{marginTop:10,fontSize:13.5,color:'#4a4d86',background:'#fff',borderRadius:8,padding:'7px 10px',lineHeight:1.45}}>{why}</div>}
  </div>);
}
Object.assign(LISTEN_4_DRILL, { levels: L4_LEVELS, generate: genL4Question, check: (q, ans) => ans !== null && ans !== undefined && ans === q.answer, answerLabel: l4AnswerLabel, Question: L4Question, Learn: L4Learn });
// the teacher's copy (no Workbook: every step is by ear)
function L4Teacher() {
  const pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="listen-4" teacher>{content}</WbPage>);
  const lt = (i) => (i < 0 ? lwLet(i + 12) + ',' : lwLet(((i % 12) + 12) % 12) + (i >= 12 ? "'" : ''));   // B, = the B below middle C; C' = the C above
  const iv = (k, n) => lt(k) + ' then ' + lt(k + L4_IV.find(y => y[0] === n)[1]) + ': ' + L4_IVN[n][0];
  const two = (pr) => pr.map(([a, b]) => lt(a) + '+' + lt(b)).join(' → ') + ' (higher ' + lt(pr[0][1]) + ' ' + lt(pr[1][1]) + '; lower ' + lt(pr[0][0]) + ' ' + lt(pr[1][0]) + ')';
  const tri = ([r, q, inv]) => { const n = l4Tri(r, q, inv); return n.map(lt).join(' ') + ' (' + lwLet(r) + (q === 'maj' ? ' major, ' : ' minor, ') + L4_INVW[inv][0] + '): middle ' + lt(n[1]); };
  P(<>
    <div style={{fontFamily:LB_SERIF,fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('listen-4')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 12px',lineHeight:1.5}}>No Workbook for this chapter: every step is by ear, as the Grade 4 aural tests ask. Each block faces its Lesson Book page and gives you material to play, the same as the app uses. Play every test twice, as the examiner does. Middle C is C here; the C above is C'; the B below is B,.</div>
    <TcBlock page={2} title="Any interval from the keynote" answers={<>{tcAns('PLAY', [[0, 6], [7, 4], [5, 7], [2, 8], [0, 3], [7, 2], [5, 5], [-3, 6]].map(([k, n]) => iv(k, n)))}</>}
      watch="The number found but the quality guessed. In a major scale, from the keynote: 4, 5 and 8 perfect; 2, 3, 6 and 7 major. The 7th heard as the octave: it leans up to it."
      say="“In a major scale, from home: 4, 5, 8 perfect; 2, 3, 6, 7 major.”"/>
    <TcBlock page={3} title="Two parts: sing one" answers={<>{tcAns('PLAY', L4_TWO.slice(0, 8).map(two))}</>}
      watch="Singing the first note of one part and the second of the other. Ask for the lower part as often as the higher."
      say="“Two parts at once: follow one line.”"/>
  </>);
  P(<>
    <TcBlock page={4} title="The middle note of a triad" answers={<>{tcAns('PLAY', L4_TRIS.slice(0, 9).map(tri))}</>}
      watch="Humming the top note (the easiest to hear). Hum top, bottom, then between. In root position the middle is the 3rd; in first inversion, the 5th; in second inversion, the root."
      say="“Top, bottom, then the one between.”"/>
    <TcBlock page={5} title="Clap it back: two or three?" answers={<><div style={{fontSize:10.5,fontWeight:900,color:BK.muted,letterSpacing:'0.06em',marginBottom:4}}>{spTx('PLAY TWICE, THEN THE CHILD TAPS AND SAYS TWO OR THREE (♩ = ' + L4_CLAP_BPM + ')')}</div>
      <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:'4px 14px'}}>{L4_CLAP.map((row, i) => <div key={i} style={{display:'flex',alignItems:'center',gap:6}}>{nvNum(i + 1)}<div style={{flex:1,minWidth:0}}>{rqStaffEl(row.items, { counts: false, hearts: false })}</div></div>)}</div></>}
      watch="The dotted quaver and semiquaver clapped as two even quavers: long-short, the semiquaver just before the next note. The quaver rest skipped: wait, then clap."
      say="“Clap it back, then say two or three.”"/>
    <TcBlock page={6} title="My four checks" answers={<div style={{fontSize:12,color:BK.ink,lineHeight:1.5}}>Each one with you at the piano, away from the screen, played twice: you play, the child sings, names or claps. Use material the child has not heard this week. The drill's level 5 mixes all four, as the exam does.</div>}/>
  </>);
  return <>{pages}</>;
}
TEACHER_COPIES['listen-4'] = L4Teacher;
'''
rep("""TEACHER_COPIES['listen-23'] = L2Teacher;""", """TEACHER_COPIES['listen-23'] = L2Teacher;""" + CH)

HOME = r'''
// ══ Build AR: Hear and Sing, Grade 4 on the Home (the Aural door) ══
LBH_FN['listen-4'] = (s) => l4LbPages(s);
const l4Add = (id, i, en, ko, benEn, bko, make) => { const spec = lbhSpec('listen-4', i, { make });
  TOOLS.push({ id, ch: 'concept', title: en, blurb: benEn, hidden: true, get kicker() { return t('Aural', '청음') + ' · ' + t('Hear and sing, Grade 4', '듣고 부르기, Grade 4'); }, C: () => <KqEngine spec={spec}/> });
  lbhRetitle(id, en, ko, benEn, bko); };
const l4IvQ = (n, prev) => { let k, dg, g = 0; do { k = pick(L4_KEYS); dg = pick([2, 3, 4, 5, 6, 7, 8]); } while (prev && prev.key === k + '-' + dg && g++ < 10); const d = L4_IV.find(y => y[0] === dg)[1];
  return { kind: 'choice', cols: 3, prompt: ['The keynote, then a note: sing it, then name it.', '으뜸음, 그다음 음: 부르고, 이름을 말해요.'], opts: [2, 3, 4, 5, 6, 7, 8].map(x => ({ id: x, label: () => l4IvName(x) })), ans: dg, ok: (v) => v === dg,
    key: k + '-' + dg, play: () => l4PlayIv(k, d),
    fig: (c) => ({ mid: c.res ? <SpKb lo={Math.min(0, k)} hi={Math.max(14, k + 12)} W={24} H={72} lit={{ [k]: 'pale', [k + d]: c.res === 'ok' ? 'good' : 'cor' }} names={Object.fromEntries([0, 2, 4, 5, 7, 9, 11, 12].map((s, j) => [k + s, String(j + 1)]))}/> : null }),
    yes: ['Yes: a ' + L4_IVN[dg][0] + '.', '맞아요: ' + L4_IVN[dg][1] + '.'], no: ['It was a ' + L4_IVN[dg][0] + ': 4, 5, 8 perfect; 2, 3, 6, 7 major.', L4_IVN[dg][1] + '였어요: 4, 5, 8은 완전, 2, 3, 6, 7은 장음정.'] }; };
l4Add('l4-iv', 1, 'Any interval from the keynote', '으뜸음에서 어떤 음정이든', 'Sing it, then give its full name: a major 6th, a perfect 4th.', '부르고, 온전한 이름 말하기: 장6도, 완전4도.', l4IvQ);
l4Add('l4-two', 2, 'Two parts: sing one', '두 성부: 하나를 불러요', 'Two intervals in two parts: sing the higher or the lower.', '두 성부의 두 음정: 윗성부나 아랫성부 부르기.', lwTapQ(L4TwoPad, (n) => ({ fixed: { pr: L4_TWO[(n * 5) % L4_TWO.length], ask: n % 2 ? 'lo' : 'hi' } }), ['Hear the two parts, sing the one asked, then find its notes.', '두 성부를 듣고, 묻는 성부를 부르고, 음을 찾아요.'], ['Sung and found ✓', '부르고 찾았어요 ✓']));
l4Add('l4-mid', 3, 'The middle note of a triad', '3화음의 가운데 음', 'Root position or inverted: hum the middle note.', '기본형이든 자리바꿈이든: 가운데 음 흥얼거리기.', lwTapQ(L4MidPad, (n) => ({ fixed: L4_TRIS[(n * 3) % L4_TRIS.length] }), ['Hear the triad, hum the middle note, then find it.', '3화음을 듣고, 가운데 음을 흥얼거리고, 찾아요.'], ['Heard and found ✓', '듣고 찾았어요 ✓']));
l4Add('l4-clap', 4, 'Clap it back: two or three?', '따라 치고, 두 박? 세 박?', 'Harder rhythms: heard twice, clapped back, named.', '더 어려운 리듬: 두 번 듣고, 따라 치고, 박자 말하기.', lwTapQ(L4ClapPad, (n) => ({ fixed: n % L4_CLAP.length }), ['Listen twice, tap it back, then say two or three.', '두 번 듣고, 따라 치고, 두 박인지 세 박인지 말해요.'], ['Clapped back and named ✓', '따라 치고 맞혔어요 ✓']));
'''
rep("""
lbhAdd('rb-finger', 'r-beat', 'rhythm', 'The beat in your fingers'""", HOME + """
lbhAdd('rb-finger', 'r-beat', 'rhythm', 'The beat in your fingers'""")
# the books and the house
rep("""const LESSON_BOOKS = { 'rhythm-23': Rhythm23LessonBook,""", """const LESSON_BOOKS = { 'listen-4': Listen4LessonBook, 'rhythm-23': Rhythm23LessonBook,""")
rep("""const LB_PAGE_FNS = { 'rhythm-23': r2LbPages,""", """const LB_PAGE_FNS = { 'listen-4': l4LbPages, 'rhythm-23': r2LbPages,""")
rep("""const HOUSE_ICONS = {"rhythm-23": """, """const HOUSE_ICONS = {"listen-4": "<path d=\\"M8 15C3 21 3 29 8 35M15 19C12 22 12 28 15 31\\"/><ellipse cx=\\"30\\" cy=\\"33\\" rx=\\"5.5\\" ry=\\"4\\" transform=\\"rotate(-20 30 33)\\" fill=\\"#26296b\\"/><ellipse cx=\\"30\\" cy=\\"25\\" rx=\\"5.5\\" ry=\\"4\\" transform=\\"rotate(-20 30 25)\\" fill=\\"#e4572e\\" stroke=\\"#e4572e\\"/><ellipse cx=\\"30\\" cy=\\"17\\" rx=\\"5.5\\" ry=\\"4\\" transform=\\"rotate(-20 30 17)\\" fill=\\"#26296b\\"/>", "rhythm-23": """)
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
