import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build AJ (board call 14, the first Grades 2-3 room): Hear and Sing Further. The Grade 2 and Grade 3 practical aural tests
# (Manual of Syllabuses 2026, section 21, read from the PDF): G2 sing the higher or lower of two notes a major 3rd or perfect
# 5th apart, played together within an octave from middle C; G3 any two notes; G3 the keynote, then the 2nd, 3rd, 4th or 5th
# of the major scale in succession, sung and named; G2-3 clap back a passage in duple or triple time played twice (G3 also
# says which); G2-3 sing back a short phrase played twice, combining melody and time. All tests in these grades are played
# twice. Theory of Music has no aural part. Shaped like Listen, Clap, Write: the app plays and scores taps and answers; whether
# a child sang in tune is the teacher's ear.

rep("""const LISTEN_WRITE_DRILL = { id: 'listen-write', label: 'Listen, Clap, Write', noPrint: true };""",
    """const LISTEN_WRITE_DRILL = { id: 'listen-write', label: 'Listen, Clap, Write', noPrint: true };
const LISTEN_23_DRILL = { id: 'listen-23', label: 'Hear and Sing Further', noPrint: true };   // Build AJ: Grades 2-3 aural""")
rep("""  { id: 'listen-write', label: 'Listen, Clap, Write', concept: LISTEN_WRITE_DRILL, track: 'start' },   // Build AE""",
    """  { id: 'listen-write', label: 'Listen, Clap, Write', concept: LISTEN_WRITE_DRILL, track: 'start' },   // Build AE
  { id: 'listen-23', label: 'Hear and Sing Further', concept: LISTEN_23_DRILL, track: 'start' },   // Build AJ""")
rep("""'listen-write': '듣고, 치고, 적기'""", """'listen-write': '듣고, 치고, 적기', 'listen-23': '더 듣고 부르기'""")
rep("""'listen-write': ['listen-sing', 'time-signatures']""", """'listen-write': ['listen-sing', 'time-signatures'], 'listen-23': ['listen-write']""")
rep("""'listen-write': ['Listen & write', '듣고 적기']""", """'listen-write': ['Listen & write', '듣고 적기'], 'listen-23': ['Hear & sing', '듣고 부르기']""")
rep("""  'listen-write': 'aural ear grade 1 tonic""", """  'listen-23': 'aural ear grade 2 grade 3 two notes together higher lower sing major third perfect fifth keynote second third fourth fifth name interval clap back duple triple sing phrase',
  'listen-write': 'aural ear grade 1 tonic""")
rep("""if (id === 'listen-sing' || id === 'listen-write') return 'aural';""", """if (id === 'listen-sing' || id === 'listen-write' || id === 'listen-23') return 'aural';""")
rep("""  { ids: ['melody', 'more-scales'], en: ['Grades 2–3', 'How a tune is shaped, and more scales.'], ko: ['Grade 2–3', '선율의 모양, 그리고 더 많은 음계.'] },""",
    """  { ids: ['melody', 'listen-23', 'more-scales'], en: ['Grades 2–3', 'How a tune is shaped, your ears a step further, and more scales.'], ko: ['Grade 2–3', '선율의 모양, 귀를 한 걸음 더, 그리고 더 많은 음계.'] },   // Build AJ: Hear and Sing Further""")
rep("""    { id: 'au-lw', en: 'Listen, clap, write', ko: '듣고, 치고, 적기', lessons: ['lw-home', 'lw-metre', 'lw-clap', 'lw-phrase', 'lw-write'], check: 'listen-write' },""",
    """    { id: 'au-lw', en: 'Listen, clap, write', ko: '듣고, 치고, 적기', lessons: ['lw-home', 'lw-metre', 'lw-clap', 'lw-phrase', 'lw-write'], check: 'listen-write' },
    { id: 'au-23', en: 'Hear and sing further', ko: '더 듣고 부르기', lessons: ['l2-dyad', 'l2-any', 'l2-deg', 'l2-clap', 'l2-sing'], check: 'listen-23' },   // Build AJ""")
rep("""  set('home', 'ch-ext ch-blues');""", """  set('home', 'ch-ext ch-blues');
  set('23', 'l2-dyad l2-any l2-deg l2-clap l2-sing');   // Build AJ: Hear and Sing Further, the Grades 2-3 aural""")

CH = r'''
// ─── Chapter: Hear and Sing Further (Build AJ, 2026-10-26; board call 14, the first Grades 2-3 room) ───
// The Grade 2 and 3 practical aural tests (Manual 2026, section 21), one step each: two notes together, sing the higher or the
// lower (G2: a major 3rd or a perfect 5th; G3: any two notes), within an octave from middle C; the keynote, then the 2nd, 3rd,
// 4th or 5th of the major scale, sung and named (G3); a passage in two or three, heard twice, clapped back, then two or three
// said (G2-3); a longer phrase heard twice, sung back with its rhythm (G2-3). Every test is heard twice.
const L2_WHITE = [0, 2, 4, 5, 7, 9, 11, 12];   // middle C to the C above: 'within an octave from middle C'
const L2_G2 = [[0, 4], [5, 9], [7, 11], [0, 7], [2, 9], [4, 11], [5, 12]];   // a major 3rd or a perfect 5th, on white keys
const L2_G3 = (() => { const out = []; L2_WHITE.forEach((a, i) => L2_WHITE.slice(i + 1).forEach(b => out.push([a, b]))); return out; })();   // any two
const l2Num = (a, b) => L2_WHITE.indexOf(b) - L2_WHITE.indexOf(a) + 1;
const L2_QUAL = { '2-1': ['minor 2nd', '단2도'], '2-2': ['major 2nd', '장2도'], '3-3': ['minor 3rd', '단3도'], '3-4': ['major 3rd', '장3도'], '4-5': ['perfect 4th', '완전4도'], '4-6': ['augmented 4th (the tritone)', '증4도 (트라이톤)'],
  '5-7': ['perfect 5th', '완전5도'], '6-8': ['minor 6th', '단6도'], '6-9': ['major 6th', '장6도'], '7-10': ['minor 7th', '단7도'], '7-11': ['major 7th', '장7도'], '8-12': ['octave', '옥타브'] };
const l2IvName = (a, b) => { const q = L2_QUAL[l2Num(a, b) + '-' + (b - a)]; return q ? t(q[0], q[1]) : ''; };
const L2_KEYS = [0, 2, 5, 7];   // C, D, F, G: the keynote
const L2_DEG = [[2, 2], [3, 4], [4, 5], [5, 7]];   // the 2nd, 3rd, 4th and 5th of the major scale, in semitones
const l2DegName = (n) => t(['', '', '2nd', '3rd', '4th', '5th'][n], ['', '', '2도', '3도', '4도', '5도'][n]);
const l2Let = (i) => lwLet(i);
const l2PlayDyad = (a, b) => spPlay([{ at: 0, keys: [a, b], len: 2.2, vol: 0.13 }, { at: 3.2, keys: [a, b], len: 2.2, vol: 0.13 }], 72);   // played twice
const l2PlayDeg = (k, d) => spPlay([{ at: 0, keys: [k], len: 1.6 }, { at: 2, keys: [k + d], len: 1.8 }, { at: 4.6, keys: [k], len: 1.6 }, { at: 6.6, keys: [k + d], len: 1.8 }], 84);
// clap-back passages for Grades 2-3: the Grade 1 shapes, now with the dotted crotchet and quaver (long, short) and ties of a beat
const L2_CLAP = [
  [['ts', 2], ['q'], ['q'], ['|'], ['qd'], ['e'], ['|'], ['q'], ['q'], ['|'], ['h'], ['||']],
  [['ts', 3], ['q'], ['q'], ['q'], ['|'], ['qd'], ['e'], ['q'], ['|'], ['h'], ['q'], ['|'], ['hd'], ['||']],
  [['ts', 2], ['p'], ['q'], ['|'], ['qd'], ['e'], ['|'], ['p'], ['p'], ['|'], ['h'], ['||']],
  [['ts', 3], ['h'], ['q'], ['|'], ['p'], ['q'], ['q'], ['|'], ['qd'], ['e'], ['q'], ['|'], ['hd'], ['||']],
  [['ts', 2], ['q'], ['p'], ['|'], ['qd'], ['e'], ['|'], ['q'], ['p'], ['|'], ['h'], ['||']],
  [['ts', 3], ['qd'], ['e'], ['q'], ['|'], ['h'], ['q'], ['|'], ['p'], ['p'], ['q'], ['|'], ['hd'], ['||']],
];
const L2_CLAP_BPM = 84;
// longer phrases, within an octave from middle C: [semitone, beats], 8 beats each; skips as well as steps
const L2_PH = [
  [[0, 1], [4, 1], [7, 1], [4, 1], [5, 1], [2, 1], [0, 2]],
  [[7, 1], [9, 0.5], [11, 0.5], [12, 1], [7, 1], [9, 1], [5, 1], [7, 2]],
  [[4, 1], [7, 1], [12, 2], [11, 1], [9, 0.5], [7, 0.5], [7, 2]],
  [[12, 1], [11, 0.5], [9, 0.5], [7, 1], [4, 1], [5, 1], [2, 1], [0, 2]],
  [[2, 1], [5, 1], [9, 1], [5, 1], [4, 0.5], [2, 0.5], [4, 1], [0, 2]],
  [[7, 1], [4, 1], [0, 1], [4, 1], [7, 0.5], [9, 0.5], [7, 1], [12, 2]],
];
const l2Btn = lwBtn, l2Msg = lwMsg, l2Row = lwRow;

// ── steps 1 and 2: two notes at once; sing the higher or the lower one, then find it ──
function L2DyadPad({ any = false, onResult, fixed }) {
  const T = useSpTimers();
  const pool = any ? L2_G3 : L2_G2;
  const [x, setX] = useState(fixed || { p: pool[0], ask: 'hi' }), [heard, setHeard] = useState(false), [res, setRes] = useState(null), [tries, setTries] = useState([]);
  const [a, b] = x.p, target = x.ask === 'hi' ? b : a;
  const play = () => { T.clear(); setHeard(true); l2PlayDyad(a, b); };
  const fresh = () => { let y, g = 0; do { y = { p: pick(pool), ask: Math.random() < 0.5 ? 'hi' : 'lo' }; } while (y.p === x.p && y.ask === x.ask && g++ < 10); setX(y); setRes(null); setTries([]); setHeard(true); T.clear(); l2PlayDyad(y.p[0], y.p[1]); };
  const tap = (k) => { playKey(k, 0.5); if (!heard || res) return;
    if (k === target) { const r = { ok: tries.length === 0 }; setRes(r); if (onResult) onResult(r); } else setTries(ts => [...ts, k]); };
  const last = tries[tries.length - 1], lit = {}; if (res) { lit[a] = x.ask === 'lo' ? 'good' : 'cor'; lit[b] = x.ask === 'hi' ? 'good' : 'cor'; } else if (last != null) lit[last] = 'bad';
  const askW = x.ask === 'hi' ? t('the higher note', '높은 음') : t('the lower note', '낮은 음');
  return (
    <div className="try-box" style={actBox} data-l2={any ? 'any' : 'dyad'}>
      <div style={actTitle}>{any ? t('Any two notes', '어떤 두 음이든') : t('Two notes at once', '두 음을 함께')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>두 음이 <b>함께</b> 울려요(두 번). <b>{askW}</b>을 흥얼거리고, 건반에서 찾아요. 높은 음은 새 쪽, 낮은 음은 거북이 쪽.{any ? '' : ' 두 음은 장3도나 완전5도 떨어져 있어요.'}</>
        : <>Two notes sound <b>together</b> (twice). Hum <b>{askW}</b>, then find it on the keys. Higher is the bird's, lower the turtle's.{any ? '' : ' The two are a major 3rd or a perfect 5th apart.'}</>}</div>
      {heard && <div style={{textAlign:'center',fontSize:16,fontWeight:900,color:BK.coral,margin:'0 0 6px'}}>{x.ask === 'hi' ? t('Sing the higher note ↑', '높은 음을 불러요 ↑') : t('Sing the lower note ↓', '낮은 음을 불러요 ↓')}</div>}
      <SpKb lo={0} hi={12} W={34} H={86} lit={lit} names={res ? { [a]: l2Let(a), [b]: l2Let(b) } : { 0: 'C' }} onTap={tap} label={t('Find the note you sang', '부른 음 찾기')}/>
      {l2Msg(!heard ? t('Tap ▶ to hear the two notes.', '▶를 누르면 두 음이 나와요.') : res ? t(l2Let(a) + ' and ' + l2Let(b) + ': a ' + l2IvName(a, b) + '. ' + (res.ok ? 'First time!' : 'Found it.'), l2Let(a) + '와 ' + l2Let(b) + ': ' + l2IvName(a, b) + '. ' + (res.ok ? '한 번에!' : '찾았어요.'))
        : last != null ? t('Not that one: hum it again, then try.', '그 음이 아니에요: 다시 흥얼거리고 찾아봐요.') : t('Hum it first, then tap the key.', '먼저 흥얼거리고, 건반을 눌러요.'), res ? BK.green : last != null ? BK.coral : undefined)}
      {l2Row(<>
        <button className="ghost-btn" style={l2Btn} onClick={heard && !fixed ? fresh : play}>{!heard ? t('▶ Play two notes', '▶ 두 음 듣기') : fixed ? t('♪ Again', '♪ 다시') : t('▶ New pair', '▶ 새 두 음')}</button>
        {heard && !fixed && <button className="ghost-btn" style={l2Btn} onClick={play}>{t('♪ Again', '♪ 다시')}</button>}
        {heard && !res && <button className="ghost-btn" style={l2Btn} onClick={() => playKey(target, 1)}>{t('♪ Just that note', '♪ 그 음만')}</button>}
      </>)}
    </div>
  );
}

// ── step 3: from the keynote: the 2nd, 3rd, 4th or 5th of the major scale; sing it, then name it ──
function L2DegPad({ onResult, fixed }) {
  const [x, setX] = useState(fixed || { k: 0, n: 3 }), [heard, setHeard] = useState(false), [ans, setAns] = useState(null), [run, setRun] = useState(0);
  const d = L2_DEG.find(y => y[0] === x.n)[1];
  const play = () => { setHeard(true); l2PlayDeg(x.k, d); };
  const fresh = () => { let y, g = 0; do { y = { k: pick(L2_KEYS), n: pick([2, 3, 4, 5]) }; } while (y.k === x.k && y.n === x.n && g++ < 10); setX(y); setAns(null); setHeard(true); l2PlayDeg(y.k, L2_DEG.find(z => z[0] === y.n)[1]); };
  const say = (c) => { if (!heard || ans) return; setAns(c); const ok = c === x.n; setRun(r => (ok ? r + 1 : 0)); if (onResult) onResult({ ok }); };
  const lit = {}; if (ans) { lit[x.k] = 'pale'; lit[x.k + d] = ans === x.n ? 'good' : 'cor'; }
  const sc = [0, 2, 4, 5, 7].map(s => x.k + s);
  return (
    <div className="try-box" style={actBox} data-l2="deg">
      <div style={actTitle}>{t('From the keynote', '으뜸음에서')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>먼저 <b>으뜸음(1)</b>, 그다음 다른 음이 울려요(두 번). 으뜸음에서 <b>1 2 3 4 5</b>로 올라가며 불러서 그 음을 만나면, 그 숫자가 이름이에요: 2도, 3도, 4도, 5도.</>
        : <>First <b>the keynote (1)</b>, then another note (twice). Sing up from the keynote, <b>1 2 3 4 5</b>, until you meet it: that number is its name, the 2nd, 3rd, 4th or 5th.</>}</div>
      <SpKb lo={0} hi={14} W={28} H={78} lit={lit} names={ans ? Object.fromEntries(sc.map((s, j) => [s, String(j + 1)])) : { [x.k]: '1' }} label={t('The keynote and the scale', '으뜸음과 음계')}/>
      {heard && <div style={{display:'grid',gridTemplateColumns:'repeat(4,minmax(0,1fr))',gap:8,marginTop:10}}>{[2, 3, 4, 5].map(n => <button key={n} className={'choice-btn' + (!ans ? '' : n === x.n ? ' good' : n === ans ? ' bad' : '')} onClick={() => say(n)} style={{padding:'12px 4px',fontSize:16,fontWeight:900}}>{l2DegName(n)}</button>)}</div>}
      {l2Msg(!heard ? t('Tap ▶ to hear the keynote and the note.', '▶를 누르면 으뜸음과 음이 나와요.') : ans ? (ans === x.n ? t('Yes: the ' + l2DegName(x.n) + '. ' + (run > 1 ? run + ' in a row.' : ''), '맞아요: ' + l2DegName(x.n) + '. ' + (run > 1 ? run + '번 연속.' : '')) : t('It was the ' + l2DegName(x.n) + ': sing up 1 2 3 4 5 and listen where you meet it.', l2DegName(x.n) + '였어요: 1 2 3 4 5로 올라가며 어디서 만나는지 들어 봐요.')) : t('Sing it, then name it.', '부르고, 이름을 말해요.'), ans ? (ans === x.n ? BK.green : BK.coral) : undefined)}
      {l2Row(<>
        <button className="ghost-btn" style={l2Btn} onClick={heard && !fixed ? fresh : play}>{!heard ? t('▶ Keynote, then the note', '▶ 으뜸음, 그다음 음') : fixed ? t('♪ Again', '♪ 다시') : t('▶ Another', '▶ 다른 것')}</button>
        {heard && !fixed && <button className="ghost-btn" style={l2Btn} onClick={play}>{t('♪ Again', '♪ 다시')}</button>}
        {heard && <button className="ghost-btn" style={l2Btn} onClick={() => spPlay([0, 2, 4, 5, 7].map((s, j) => ({ at: j * 0.6, keys: [x.k + s], len: 0.55 })), 100)}>{t('♪ Sing up 1 to 5', '♪ 1부터 5까지')}</button>}
      </>)}
    </div>
  );
}

// ── step 4: clap it back, then say two or three (heard twice, as the tests are) ──
function L2ClapPad({ onResult, fixed }) {
  const T = usePlTimers();
  const [i, setI] = useState(fixed != null ? fixed : 0), [phase, setPhase] = useState('ready'), [heard, setHeard] = useState(0), [res, setRes] = useState(null), [met, setMet] = useState(null);
  const run = useRef(null), taps = useRef([]);
  const items = L2_CLAP[i], snd = srhSounds(items), notes = snd.map((s, j) => [s, j]).filter(([s]) => !s.rest), top = srhTop(items), n = srhBeats(items);
  const reset = () => { T.clear(); stopClicks(); setPhase('ready'); setHeard(0); setRes(null); setMet(null); };
  const listen = () => { T.clear(); setRes(null); setMet(null); const r = rqRunS(items, { bpm: L2_CLAP_BPM }); if (!r) return; setPhase('listen');
    T.at(r, r.at[r.lead] + n * r.spb, () => { const r2 = rqRunS(items, { bpm: L2_CLAP_BPM }); if (!r2) return; T.at(r2, r2.at[r2.lead] + n * r2.spb + 0.2, () => { setPhase('ready'); setHeard(2); }); }); setHeard(1); };
  const go = () => { T.clear(); setRes(null); setMet(null); taps.current = []; const r = rqRunS(items, { bpm: L2_CLAP_BPM, silent: true }); if (!r) return; run.current = r; setPhase('count');
    const g = r.at[r.lead]; T.at(r, g - 0.05, () => setPhase('tap'));
    T.at(r, g + n * r.spb + 0.1, () => { const tol = Math.min(PL_TOL, r.spb * 0.22), mt = plMatch(notes.map(([s]) => g + s.b * r.spb), taps.current.filter(tp => tp > g - tol), tol), marks = {};
      notes.forEach(([s, j], k) => { marks[j] = mt.offs[k] === null ? '?' : '✓'; });
      setRes({ hits: mt.hits, total: notes.length, extra: mt.extra, marks, ok: mt.hits >= notes.length - 1 && mt.extra <= 1 }); setPhase('done'); }); };
  const say = (m) => { if (!res || met) return; setMet(m); if (onResult) onResult({ ok: res.ok && m === top, clap: res.ok, metre: m === top }); };
  const tap = React.useCallback(() => { const r = run.current; if (r && (phase === 'count' || phase === 'tap')) { taps.current.push(r.now()); const ctx = getAudio(); if (ctx) blip(ctx, ctx.currentTime, SRH_HZ, 0.1, 0.16, 'triangle'); } }, [phase]);
  return (
    <div className="try-box" style={actBox} data-l2="clap">
      <div style={actTitle}>{t('Clap it back: two or three?', '따라 치고, 두 박? 세 박?')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>리듬을 <b>두 번</b> 들어요. 그다음 클릭에 맞춰 똑같이 치고, <b>두 박인지 세 박인지</b> 말해요. 이번에는 <b>점4분음표와 8분음표</b>(길게, 짧게)도 나와요.</>
        : <>Hear the passage <b>twice</b>. Then tap it back with the clicks and say: <b>two or three</b> beats in a bar? Now with <b>the dotted crotchet and quaver</b> too (long, short).</>}</div>
      {!fixed && spChips(L2_CLAP.map((_, j) => [j, t('Passage ' + (j + 1), (j + 1) + '번')]), i, (j) => { reset(); setI(j); })}
      {met ? rqStaffEl(items, { marks: res.marks, hearts: false }) : <div style={{textAlign:'center',fontSize:14,fontWeight:900,color:BK.muted,margin:'6px 0'}}>{t(['Not heard yet', 'Heard once', 'Heard twice'][heard], ['아직 안 들었어요', '한 번 들었어요', '두 번 들었어요'][heard])}</div>}
      {l2Msg(phase === 'listen' ? t('Listen…', '들어요…') : phase === 'count' ? t('Get ready…', '준비…') : phase === 'tap' ? t('Tap it back!', '따라 쳐요!') : res && !met ? t('On time: ' + res.hits + ' of ' + res.total + '. Two or three?', '제때: ' + res.total + '개 중 ' + res.hits + '개. 두 박? 세 박?')
        : met ? t((res.ok ? 'Clapped back ✓ ' : 'Clap: nearly. ') + (met === top ? (top === 2 ? 'Two ✓' : 'Three ✓') : 'It was ' + (top === 2 ? 'two.' : 'three.')), (res.ok ? '따라 치기 ✓ ' : '따라 치기: 거의. ') + (met === top ? (top === 2 ? '두 박 ✓' : '세 박 ✓') : (top === 2 ? '두 박이었어요.' : '세 박이었어요.'))) : '', met ? (res.ok && met === top ? BK.green : BK.coral) : undefined)}
      {res && !met && <div style={{display:'grid',gridTemplateColumns:'repeat(2,minmax(0,1fr))',gap:8,marginTop:8}}>{[[2, t('Two', '두 박')], [3, t('Three', '세 박')]].map(([m, lab]) => <button key={m} className="choice-btn" onClick={() => say(m)} style={{padding:'12px 4px',fontSize:16,fontWeight:900}}>{lab}</button>)}</div>}
      <PlPad on={phase === 'count' || phase === 'tap'} onTap={tap}/>
      {l2Row(<>
        <button className="ghost-btn" style={l2Btn} onClick={listen}>{t('▶ Listen (twice)', '▶ 듣기 (두 번)')}</button>
        <button className="ghost-btn" style={l2Btn} disabled={!heard} onClick={go}>{res ? t('▶ Again', '▶ 다시') : t('▶ Tap it back', '▶ 따라 치기')}</button>
      </>)}
      {plHint()}
    </div>
  );
}

// ── step 5: a longer tune with its rhythm, heard twice; sing it back, then play it ──
function L2Pills({ ph, got = 0, lit = -1, show = false, u = 34 }) {
  return <div style={{display:'flex',gap:4,justifyContent:'center',alignItems:'flex-end',flexWrap:'wrap',margin:'4px 0'}}>{ph.map(([k, b], j) => { const on = j === lit, done = j < got, w = b * u + (b - 1) * 4, hh = Math.round(u * 0.88);
    return <span key={j} style={{display:'inline-flex',flexDirection:'column',alignItems:'center',gap:3}}>
      <span style={{width:w,height:hh,borderRadius:hh / 2,boxSizing:'border-box',display:'inline-flex',alignItems:'center',justifyContent:'center',fontSize:Math.round(u * 0.41),fontWeight:900,background:on ? BK.coral : done ? BK.ink : '#fff',border:'2px solid ' + (on ? BK.coral : BK.ink),color:on || done ? '#fff' : BK.ink}}>{done || show ? l2Let(k) : ''}</span>
      <span style={{fontSize:Math.round(u * 0.33),fontWeight:900,color:BK.muted}}>{lwBeatWord(b)}</span></span>; })}</div>;
}
function L2SingPad({ onResult, fixed }) {
  const T = useSpTimers();
  const [i, setI] = useState(fixed != null ? fixed : 0), [lit, setLit] = useState(-1), [got, setGot] = useState(0), [miss, setMiss] = useState(0), [heard, setHeard] = useState(false), [wrong, setWrong] = useState(null);
  const ph = L2_PH[i], ks = ph.map(([k]) => k), done = got >= ph.length;
  const listen = () => { T.clear(); setHeard(true); const len = lwPlay(ph, 80, T, setLit); const spb = 60 / 80; T.at((0.15 + (len + 1) * spb) * 1000, () => lwPlay(ph, 80, T, setLit)); };
  const reset = (j) => { T.clear(); setI(j); setGot(0); setMiss(0); setHeard(false); setWrong(null); setLit(-1); };
  const tap = (k) => { playKey(k, 0.6); if (done || !heard) return; if (k === ks[got]) { const g = got + 1; setGot(g); setWrong(null); if (g >= ks.length && onResult) onResult({ ok: miss === 0, miss }); } else { setMiss(m => m + 1); setWrong(k); } };
  const kl = {}; if (got > 0 && !done) kl[ks[got - 1]] = 'cor'; if (wrong != null) kl[wrong] = 'bad';
  return (
    <div className="try-box" style={actBox} data-l2="sing">
      <div style={actTitle}>{t('Sing a longer tune', '더 긴 선율 따라 부르기')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>이번 선율은 더 길고, <b>건너뛰는 음</b>도 있어요. 두 번 듣고, <b>음과 리듬을 둘 다</b> "라"로 불러요. 그다음 건반에서 쳐요.</>
        : <>This tune is longer, with <b>skips</b> as well as steps. Hear it twice, sing it back on "la" with <b>the notes and the rhythm</b>, then play it.</>}</div>
      {!fixed && spChips(L2_PH.map((_, j) => [j, String(j + 1)]), i, reset)}
      <L2Pills ph={ph} got={got} lit={lit} show={done}/>
      <div style={{margin:'8px 0 4px'}}><SpKb lo={0} hi={12} W={34} H={86} lit={kl} names={{ 0: 'C' }} onTap={tap} label={t('Play the tune', '선율 치기')}/></div>
      {l2Msg(!heard ? t('Tap ▶ Listen: it plays twice.', '▶ 듣기를 눌러요: 두 번 나와요.') : done ? t('Sung and played ✓' + (miss ? '' : ' First time!'), '부르고 쳤어요 ✓' + (miss ? '' : ' 한 번에!')) : wrong != null ? t('Not that one: sing it again, then try.', '그 건반이 아니에요: 다시 불러 보고 찾아요.') : t('Sing it, then play it, note by note: ' + got + ' of ' + ks.length, '부르고, 한 음씩 쳐요: ' + ks.length + '개 중 ' + got + '개'), done ? BK.green : wrong != null ? BK.coral : undefined)}
      {l2Row(<button className="ghost-btn" style={l2Btn} onClick={listen}>{t('▶ Listen (twice)', '▶ 듣기 (두 번)')}</button>)}
    </div>
  );
}

// ── the pictures on paper ──
const l2PicDyad = () => lsRawPic('<ellipse cx="34" cy="28" rx="7" ry="5" transform="rotate(-20 34 28)" fill="#26296b"/><ellipse cx="34" cy="16" rx="7" ry="5" transform="rotate(-20 34 16)" fill="#e4572e"/><path d="M40.6 26 V4" stroke="#26296b" stroke-width="2"/>', [0, 0, 70, 44]);
const l2PicAny = () => lsRawPic('<ellipse cx="22" cy="32" rx="6" ry="4.4" transform="rotate(-20 22 32)" fill="#26296b"/><ellipse cx="22" cy="12" rx="6" ry="4.4" transform="rotate(-20 22 12)" fill="#26296b"/><ellipse cx="50" cy="26" rx="6" ry="4.4" transform="rotate(-20 50 26)" fill="#26296b"/><ellipse cx="50" cy="20" rx="6" ry="4.4" transform="rotate(-20 50 20)" fill="#e4572e"/>', [0, 0, 70, 44]);
const l2PicDeg = () => lsRawPic([1, 2, 3, 4, 5].map((n, i) => lsCircleSvg(8 + i * 15, 36 - i * 6, 6, n === 1 || n === 3 ? 'play' : 'beat', String(n))).join(''), [0, 0, 80, 44]);
const l2PicClap = () => lsPicEcho();
const l2PicSing = () => lsRawPic('<rect x="2" y="15" width="12" height="14" rx="7" fill="#fff" stroke="#26296b" stroke-width="2"/><rect x="16" y="15" width="12" height="14" rx="7" fill="#fff" stroke="#26296b" stroke-width="2"/><rect x="30" y="15" width="12" height="14" rx="7" fill="#fff" stroke="#26296b" stroke-width="2"/><rect x="44" y="15" width="32" height="14" rx="7" fill="#e4572e"/>', [0, 0, 80, 44]);

function l2LbPages(scr = false) {
  const ch = 'listen-23';
  const checks5 = [[l2PicDyad(), t('I hum the higher or the lower of two notes played together (a 3rd or a 5th)', '함께 울린 두 음(3도나 5도) 중 높은 음이나 낮은 음을 흥얼거려요')], [l2PicAny(), t('I hum the higher or the lower of any two notes', '어떤 두 음이든 높은 음이나 낮은 음을 흥얼거려요')],
    [l2PicDeg(), t('I sing and name the 2nd, 3rd, 4th or 5th from the keynote', '으뜸음에서 2도, 3도, 4도, 5도를 부르고 이름을 말해요')], [l2PicClap(), t('I clap back a passage and say two or three', '리듬을 따라 치고 두 박인지 세 박인지 말해요')], [l2PicSing(), t('I sing back a longer tune with its rhythm', '더 긴 선율을 리듬까지 따라 불러요')]];
  const pen = (x) => <PenArt shapes={x.shapes} vb={x.vb} style={{width:90}}/>;
  const toc = [[t('Two notes at once', '두 음을 함께'), 2], [t('Any two notes', '어떤 두 음이든'), 3], [t('From the keynote', '으뜸음에서'), 4], [t('Clap it back: two or three?', '따라 치고, 두 박? 세 박?'), 5], [t('Sing a longer tune', '더 긴 선율 따라 부르기'), 6], [t('My five checks', '나의 다섯 가지 확인'), 7]];
  const dyadStill = (pairs) => <LbPic h={170}><div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:14,width:'100%',maxWidth:620,margin:'0 auto'}}>{pairs.map(([a, b]) => <div key={a + '-' + b}>
    <div style={{textAlign:'center',fontSize:13,fontWeight:900,color:BK.ink,marginBottom:2}}>{l2Let(a)} + {l2Let(b)}: {l2IvName(a, b)}</div>
    <SpKb lo={0} hi={12} W={scr ? 26 : 36} H={scr ? 66 : 96} lit={{ [a]: 'pale', [b]: 'cor' }} names={{ [a]: l2Let(a), [b]: l2Let(b) }}/></div>)}</div></LbPic>;
  return [
    <LbPage key="1" no={1} chId={ch} teacher={<>{t('The Grade 2 and Grade 3 aural tests, one step each (Manual of Syllabuses, section 21): two notes played together, the higher or the lower sung (Grade 2: a major 3rd or a perfect 5th; Grade 3: any two notes), within an octave from middle C; the keynote, then the 2nd, 3rd, 4th or 5th of the major scale, sung and named (Grade 3); a passage in duple or triple time clapped back, and at Grade 3 named; a short phrase sung back with its rhythm. Every test in these grades is played twice. The app plays and scores the taps and answers; whether a child sang in tune is your ear.', '2·3급 청음 시험을 한 단계씩(실라버스 21절): 함께 울린 두 음 중 높은 음이나 낮은 음 부르기(2급: 장3도나 완전5도, 3급: 어떤 두 음이든), 가운데 도부터 한 옥타브 안에서; 으뜸음 다음의 2도, 3도, 4도, 5도를 부르고 이름 말하기(3급); 두 박이나 세 박 리듬 따라 치기, 3급은 박자도 말하기; 짧은 선율을 리듬까지 따라 부르기. 이 급의 시험은 모두 두 번 들려줘요. 앱은 탭과 답을 채점하고, 음정이 맞았는지는 선생님의 귀예요.')}</>}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:50,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{t('Hear and Sing Further', '더 듣고 부르기')}</div>
      </div></LbOnly>
      {dyadStill([[0, 4], [0, 7]])}
      <LbSay size={18}>{t('Your ears for Grades 2 and 3: two notes at once, the notes of the scale from home, two or three, and longer tunes.', '2·3급의 귀: 함께 울리는 두 음, 집에서 세는 음계의 음, 두 박·세 박, 더 긴 선율.')}</LbSay>
      <div className="lb-toc" style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>
        <LbOnly print><div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('In this chapter', '이 챕터에서는')}</div>
          {toc.map(([n, p]) => <div key={p} className="lb-toc-row" style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:14.5,padding:'5px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkGoal(15)}{n}</span><span style={{color:BK.muted,fontWeight:700}}>{p}</span></div>)}
        </div></LbOnly>
        <div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 챕터를 마치면')}</div>
          {[t('hum the higher or the lower of two notes together', '함께 울린 두 음 중 높은 음이나 낮은 음을 흥얼거릴 수 있어요'), t('sing and name the 2nd, 3rd, 4th or 5th from the keynote', '으뜸음에서 2도, 3도, 4도, 5도를 부르고 이름을 말할 수 있어요'), t('clap back a passage and say two or three', '리듬을 따라 치고 두 박인지 세 박인지 말할 수 있어요'), t('sing back a longer tune with its rhythm', '더 긴 선율을 리듬까지 따라 부를 수 있어요')].map((x, i) => <div key={i} style={{display:'flex',alignItems:'flex-start',gap:9,fontSize:14.5,padding:'5px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}>{bkGoal(15)}<span>{x}</span></div>)}
        </div>
      </div>
      <LbOnly print><LbDrillStrip id={ch}/></LbOnly>
    </LbPage>,
    <LbPage key="2" no={2} chId={ch} kicker={t('Step 1', '1단계')} title={t('Two notes at once', '두 음을 함께')}
      teacher={<>{t('Grade 2: two notes played together, a major 3rd or a perfect 5th apart, within an octave from middle C; the child hums or sings the higher or the lower one, as asked. Played twice. If it is hard, play the two one after the other, then together again; the top note is usually easier to hear first.', '2급: 장3도나 완전5도 떨어진 두 음을 함께 쳐요(가운데 도부터 한 옥타브 안). 아이는 묻는 대로 높은 음이나 낮은 음을 흥얼거리거나 불러요. 두 번 들려줘요. 어려우면 두 음을 하나씩 친 다음 다시 함께 쳐 주세요. 보통 위의 음이 먼저 잘 들려요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=1')}>
      <LbLive still={dyadStill([[0, 4], [5, 12]])} live={<L2DyadPad/>}/>
      <LbSay>{LANG === 'ko' ? <>두 음이 <b>함께</b> 울려요. 선생님이 묻는 음을 흥얼거려요: <b>높은 음</b>(새 쪽)이나 <b>낮은 음</b>(거북이 쪽). 그다음 건반에서 찾아요.</> : <>Two notes sound <b>together</b>. Hum the one your teacher asks for: <b>the higher</b> (the bird's) or <b>the lower</b> (the turtle's). Then find it on the keys.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>선생님이 두 음을 함께 두 번 쳐요. 높은 음부터 흥얼거려 봐요.</>, <>이번엔 낮은 음. 어려우면 선생님이 두 음을 하나씩 쳐 줘요.</>, <>흥얼거린 음을 건반에서 찾아요.</>]
        : [<>Your teacher plays two notes together, twice. Hum the higher one first.</>, <>Now the lower one. If it is hard, your teacher plays them one at a time.</>, <>Find the note you hummed on the keys.</>]}/>
      <LbRemember>{t('Two at once: pick one out and hum it.', '함께 울리는 두 음: 하나를 골라 흥얼거려요.')}</LbRemember>
    </LbPage>,
    <LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={t('Any two notes', '어떤 두 음이든')}
      teacher={<>{t('Grade 3: any two notes played together, within an octave from middle C. The closer the notes, the harder: a 2nd is the hardest. If the child is stuck, play the asked note alone, then the pair again.', '3급: 가운데 도부터 한 옥타브 안의 어떤 두 음이든 함께 쳐요. 두 음이 가까울수록 어려워요: 2도가 가장 어려워요. 막히면 묻는 음만 따로 친 다음 다시 두 음을 함께 쳐 주세요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=2')}>
      <LbLive still={dyadStill([[4, 5], [2, 11]])} live={<L2DyadPad any/>}/>
      <LbSay>{LANG === 'ko' ? <>이제 <b>어떤 두 음이든</b>. 가까운 두 음은 더 어려워요. 먼저 두 음을 듣고, 묻는 음 하나만 마음속으로 따라가요.</> : <>Now <b>any two notes</b>. Close ones are harder. Hear both, then follow just the one you are asked for.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>선생님이 두 음을 함께 두 번 쳐요. 높은 음, 그다음 낮은 음을 흥얼거려요.</>, <>가까운 두 음(2도)도 해 봐요.</>, <>흥얼거린 음을 건반에서 찾아요.</>]
        : [<>Your teacher plays two notes together, twice. Hum the higher, then the lower.</>, <>Try two close ones (a 2nd) too.</>, <>Find the note you hummed on the keys.</>]}/>
      <LbRemember>{t('Close or far: follow just one.', '가깝든 멀든: 하나만 따라가요.')}</LbRemember>
    </LbPage>,
    <LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title={t('From the keynote', '으뜸음에서')}
      teacher={<>{t('Grade 3: you sound the keynote, then the 2nd, 3rd, 4th or 5th of the major scale straight after it; the child sings it, then names it ("the 3rd"). Played twice. To find the number, sing up the scale from the keynote (1 2 3 4 5) until the voice meets the note.', '3급: 으뜸음을 울린 다음 바로 장음계의 2도, 3도, 4도, 5도를 쳐요. 아이는 그 음을 부르고 이름을 말해요("3도"). 두 번 들려줘요. 숫자를 찾으려면 으뜸음에서 음계를 1 2 3 4 5로 올라가며 불러서 그 음을 만날 때까지 가요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=3')}>
      <LbLive still={<LbPic h={160}><div style={{width:'100%',maxWidth:540,margin:'0 auto'}}><SpKb maxW={540} lo={0} hi={14} W={32} H={80} lit={{ 0: 'cor', 2: 'pale', 4: 'pale', 5: 'pale', 7: 'pale' }} names={{ 0: '1', 2: '2', 4: '3', 5: '4', 7: '5' }}/></div></LbPic>} live={<L2DegPad/>}/>
      <LbSay>{LANG === 'ko' ? <>먼저 <b>으뜸음(1)</b>, 그다음 다른 음. 1에서 <b>1 2 3 4 5</b>로 올라가며 불러요. 그 음을 만나는 숫자가 이름이에요: <b>2도, 3도, 4도, 5도</b>.</> : <>First <b>the keynote (1)</b>, then another note. Sing up from 1, <b>1 2 3 4 5</b>. The number where you meet it is its name: <b>the 2nd, 3rd, 4th or 5th</b>.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>선생님이 으뜸음과 다른 음을 두 번 쳐요. 그 음을 불러요.</>, <>으뜸음에서 1 2 3 4 5로 올라가며 불러서 숫자를 찾아요.</>, <>이름을 말해요: "3도", "5도".</>]
        : [<>Your teacher plays the keynote and another note, twice. Sing the note.</>, <>Sing up from the keynote, 1 2 3 4 5, to find its number.</>, <>Say its name: "the 3rd", "the 5th".</>]}/>
      <LbRemember>{t('Sing up from home until you meet it.', '집에서부터 올라가며, 만날 때까지 불러요.')}</LbRemember>
    </LbPage>,
    <LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title={t('Clap it back: two or three?', '따라 치고, 두 박? 세 박?')}
      teacher={<>{t('Grades 2 and 3: a passage in duple or triple time played twice; the child claps or taps it back. Grade 3 also says whether it was duple or triple. The Manual makes the examples harder with each grade, so these passages add the dotted crotchet and quaver (long, short). Listen both times without clapping; count inside.', '2·3급: 두 박이나 세 박의 리듬을 두 번 쳐요. 아이는 손뼉이나 탭으로 따라 쳐요. 3급은 두 박인지 세 박인지도 말해요. 실라버스는 급마다 예제를 더 어렵게 하니까, 이번 리듬에는 점4분음표와 8분음표(길게, 짧게)가 나와요. 두 번 다 손뼉 치지 않고 들으며 속으로 세요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=5')}>
      <LbLive still={<LbPic h={150}><div style={{width:'100%',maxWidth:560,margin:'0 auto'}}>{rqStaffEl(L2_CLAP[1], { hearts: false })}</div></LbPic>} live={<L2ClapPad/>}/>
      <LbSay>{LANG === 'ko' ? <>리듬을 <b>두 번</b> 들어요. 같은 빠르기로 똑같이 치고, <b>두 박인지 세 박인지</b> 말해요. <b>점4분음표와 8분음표</b>는 길게, 짧게.</> : <>Hear it <b>twice</b>. Clap it back at the same speed, then say <b>two or three</b>. <b>The dotted crotchet and quaver</b>: long, short.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>선생님이 네 마디를 두 번 쳐요. 듣기만 하며 속으로 세요.</>, <>같은 빠르기로 손뼉 쳐요.</>, <>두 박이었나요, 세 박이었나요? 센 박이 몇 박마다 오는지 떠올려요.</>]
        : [<>Your teacher plays four bars, twice. Just listen and count inside.</>, <>Clap it back at the same speed.</>, <>Two or three? Think how often the strong beat came.</>]}/>
      <LbRemember>{t('Clap it back, then say two or three.', '따라 치고, 두 박인지 세 박인지 말해요.')}</LbRemember>
    </LbPage>,
    <LbPage key="6" no={6} chId={ch} kicker={t('Step 5', '5단계')} title={t('Sing a longer tune', '더 긴 선율 따라 부르기')}
      teacher={<>{t('Grades 2 and 3: a short phrase played twice, combining melody and time. The Manual makes the examples harder with each grade, so the tunes here are longer and wider than the Grade 1 room\'s: up to eight notes, skips as well as steps, within an octave from middle C. Sing back on "la"; then play it. If the rhythm slips, clap it first.', '2·3급: 음과 리듬이 함께 있는 짧은 선율을 두 번 쳐요. 실라버스는 급마다 예제를 더 어렵게 하니까, 여기 선율은 1급 방보다 길고 넓어요: 여덟 음까지, 한 걸음과 건너뛰기, 가운데 도부터 한 옥타브 안. "라"로 따라 부르고, 그다음 쳐요. 리듬이 흔들리면 먼저 손뼉으로 쳐요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=6')}>
      <LbLive still={<LbPic h={150}><div style={{display:'flex',flexDirection:'column',gap:10,width:'100%',maxWidth:scr ? 480 : 640,margin:'0 auto'}}><L2Pills ph={L2_PH[1]} show u={scr ? 34 : 50}/><SpKb lo={0} hi={12} W={scr ? 30 : 44} H={scr ? 70 : 104} lit={Object.fromEntries(L2_PH[1].map(([k]) => [k, 'pale']))} names={Object.fromEntries(L2_PH[1].map(([k]) => [k, l2Let(k)]))}/></div></LbPic>} live={<L2SingPad/>}/>
      <LbSay>{LANG === 'ko' ? <>이번 선율은 <b>더 길고</b>, <b>건너뛰는 음</b>도 있어요. 두 번 듣고, <b>음도 리듬도</b> 따라 불러요: 타, 티-티, 길게.</> : <>This tune is <b>longer</b>, with <b>skips</b> as well as steps. Hear it twice and sing back <b>the notes and the rhythm</b>: walk, run-ning, hold.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>선생님이 선율을 두 번 쳐요. 들으며 속으로 따라 불러요.</>, <>"라"로 불러요: 음도, 리듬도.</>, <>건반에서 쳐요. 긴 음은 끝까지 누르고 있어요.</>]
        : [<>Your teacher plays the tune twice. Sing along inside as you listen.</>, <>Sing it on "la": the notes and the rhythm.</>, <>Play it on the keys. Hold the long note to its end.</>]}/>
      <LbRemember>{t('Longer, with skips: the notes and the rhythm, both.', '더 길고 건너뛰어도: 음도, 리듬도.')}</LbRemember>
    </LbPage>,
    <LbPage key="7" no={7} chId={ch} kicker={t('Check-up', '점검')} title={t('My five checks', '나의 다섯 가지 확인')}
      teacher={<>{t('Each one with you at the piano, away from the screen, played twice as in the exam: you play, the child hums, sings, names or claps. You only correct. The first is Grade 2; the second and third are Grade 3.', '하나씩 화면 없이 피아노 앞에서, 시험처럼 두 번씩: 선생님이 치고, 아이는 흥얼거리고, 부르고, 이름을 말하고, 손뼉 쳐요. 선생님은 고쳐 주기만 해요. 첫째는 2급, 둘째와 셋째는 3급이에요.')}</>}>
      <LbSay>{t('Tick each one: not yet, nearly, or got it!', '하나씩 표시해요: 아직, 거의, 됐어요!')}</LbSay>
      <LbLive still={<LbStageRows big rows={checks5.map(([a, txt]) => [pen(a), txt])}/>} live={<FiveChecks376 rows={checks5} storeKey="pb_l2_five"/>}/>
    </LbPage>,
  ];
}
function Listen23LessonBook() { return <>{l2LbPages(false)}</>; }
function L2Learn({ onStart }) {
  const pages = l2LbPages(true), opener = pages[0];
  return (
    <Lesson id="listen-23" title={t('Hear and Sing Further', '더 듣고 부르기')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="listen-23"><div className="lb-screen lb-open" style={{display:'flex',flexDirection:'column',gap:12,margin:'0 0 8px'}}>{lbWordsFirst(opener.props.children)}</div></BkChapterCtx.Provider></LbScreenCtx.Provider>}>
      {pages.slice(1).map((pg, i) => <Step key={i} title={pg.props.title}><LbScreenPage page={pg}/></Step>)}
    </Lesson>
  );
}
// ── the drill: every question is heard (twice, as the tests are) ──
const L2_LEVELS = [
  { n: 1, label: 'Two notes: hum the higher or the lower (3rd or 5th)', kind: 'dyad', time: 30 },
  { n: 2, label: 'Any two notes: hum the higher or the lower', kind: 'any', time: 30 },
  { n: 3, label: 'From the keynote: 2nd, 3rd, 4th or 5th?', kind: 'deg', time: 20 },
  { n: 4, label: 'Duple or triple?', kind: 'metre', time: 20 },
  { n: 5, label: 'Clap it back, then two or three', kind: 'clap', time: 45 },
  { n: 6, label: 'Sing a longer tune, then play it', kind: 'sing', time: 60 },
];
Object.assign(LEVEL_KO, { 'Two notes: hum the higher or the lower (3rd or 5th)': '두 음: 높은 음이나 낮은 음 (3도나 5도)', 'Any two notes: hum the higher or the lower': '어떤 두 음이든: 높은 음이나 낮은 음', 'From the keynote: 2nd, 3rd, 4th or 5th?': '으뜸음에서: 2도, 3도, 4도, 5도?', 'Duple or triple?': '두 박? 세 박?', 'Clap it back, then two or three': '따라 치고, 두 박? 세 박?', 'Sing a longer tune, then play it': '더 긴 선율 부르고 치기' });
function genL2Question(lv, prev) {
  const uid = Math.random(), kind = lv.kind;
  if (kind === 'dyad' || kind === 'any') { const pool = kind === 'any' ? L2_G3 : L2_G2; let p, ask, g = 0; do { p = pick(pool); ask = Math.random() < 0.5 ? 'hi' : 'lo'; } while (prev && prev.key === p.join() + ask && g++ < 10); return { kind, fx: { p, ask }, answer: 'ok', choices: [], key: p.join() + ask, uid }; }
  if (kind === 'deg') { let k, n, g = 0; do { k = pick(L2_KEYS); n = pick([2, 3, 4, 5]); } while (prev && prev.key === k + '-' + n && g++ < 10); return { kind, k, n, answer: n, choices: [2, 3, 4, 5], key: k + '-' + n, uid }; }
  if (kind === 'metre') { let i, g = 0; do { i = Math.floor(Math.random() * L2_CLAP.length); } while (prev && prev.i === i && g++ < 10); return { kind, i, answer: srhTop(L2_CLAP[i]), choices: [2, 3], key: 'm' + i, uid }; }
  if (kind === 'clap') { let i, g = 0; do { i = Math.floor(Math.random() * L2_CLAP.length); } while (prev && prev.i === i && g++ < 10); return { kind, i, answer: 'ok', choices: [], key: 'c' + i, uid }; }
  let i, g = 0; do { i = Math.floor(Math.random() * L2_PH.length); } while (prev && prev.i === i && g++ < 10); return { kind: 'sing', i, answer: 'ok', choices: [], key: 's' + i, uid };
}
function l2AnswerLabel(q) {
  if (q.kind === 'deg') return l2DegName(q.answer);
  if (q.kind === 'metre') return q.answer === 2 ? t('two beats', '두 박') : t('three beats', '세 박');
  return t('done', '완료');
}
function L2Question({ q, given, locked, onAnswer, pixel }) {
  const done = !!given;
  const play = () => { stopClicks(); if (q.kind === 'deg') l2PlayDeg(q.k, L2_DEG.find(y => y[0] === q.n)[1]); else if (q.kind === 'metre') rqRunS(L2_CLAP[q.i], { bpm: L2_CLAP_BPM }); };
  useEffect(() => { if (q.kind !== 'deg' && q.kind !== 'metre') return; const id = setTimeout(play, 350); return () => { clearTimeout(id); stopClicks(); }; }, [q.uid]);
  const btnCls = pixel ? 'pixel-choice' : 'choice-btn', cls = (c) => btnCls + (!done ? '' : c === q.answer ? ' good' : given.ans === c ? ' bad' : '');
  const pickIt = (c) => { if (locked || done) return; stopClicks(); onAnswer(c); };
  let title, body;
  if (q.kind === 'dyad' || q.kind === 'any') { title = q.fx.ask === 'hi' ? t('Hum the higher note, then find it.', '높은 음을 흥얼거리고, 찾아요.') : t('Hum the lower note, then find it.', '낮은 음을 흥얼거리고, 찾아요.'); body = <L2DyadPad key={q.uid} any={q.kind === 'any'} fixed={q.fx} onResult={(r) => pickIt(r.ok ? 'ok' : 'no')}/>; }
  else if (q.kind === 'deg') { title = t('The keynote, then a note: the 2nd, 3rd, 4th or 5th?', '으뜸음, 그다음 음: 2도, 3도, 4도, 5도?');
    body = <div style={{display:'grid',gridTemplateColumns:'repeat(4,minmax(0,1fr))',gap:8}}>{[2, 3, 4, 5].map(c => <button key={c} disabled={locked} className={cls(c)} style={{padding:'12px 4px',fontSize:16,fontWeight:900}} onClick={() => pickIt(c)}>{l2DegName(c)}</button>)}</div>; }
  else if (q.kind === 'metre') { title = t('Listen: two or three beats in a bar?', '들어 봐요: 한 마디에 두 박일까요, 세 박일까요?');
    body = <div style={{display:'grid',gridTemplateColumns:'repeat(2,minmax(0,1fr))',gap:8}}>{[2, 3].map(c => <button key={c} disabled={locked} className={cls(c)} style={{padding:'12px 4px',fontSize:16,fontWeight:900}} onClick={() => pickIt(c)}>{c === 2 ? t('Two', '두 박') : t('Three', '세 박')}</button>)}</div>; }
  else if (q.kind === 'clap') { title = t('Listen twice, clap it back, then say two or three.', '두 번 듣고, 따라 치고, 두 박인지 세 박인지 말해요.'); body = <L2ClapPad key={q.uid} fixed={q.i} onResult={(r) => pickIt(r.ok ? 'ok' : 'no')}/>; }
  else { title = t('Listen twice, sing it back, then play it.', '두 번 듣고, 따라 부르고, 쳐요.'); body = <L2SingPad key={q.uid} fixed={q.i} onResult={(r) => pickIt(r.ok ? 'ok' : 'no')}/>; }
  const why = !done ? null : q.kind === 'deg' ? t('It was the ' + l2DegName(q.n) + ' of ' + l2Let(q.k) + ' major: ' + l2Let(q.k) + ' to ' + l2Let(q.k + L2_DEG.find(y => y[0] === q.n)[1]) + '.', l2Let(q.k) + '장조의 ' + l2DegName(q.n) + '였어요: ' + l2Let(q.k) + '에서 ' + l2Let(q.k + L2_DEG.find(y => y[0] === q.n)[1]) + '.')
    : q.kind === 'metre' ? t(q.answer === 2 ? 'Two beats in a bar.' : 'Three beats in a bar.', q.answer === 2 ? '한 마디에 두 박.' : '한 마디에 세 박.') : null;
  return (<div>
    <p style={pixel ? {fontSize:11.5,textAlign:'center'} : {fontSize:15,fontWeight:700,textAlign:'center',margin:'0 0 8px',color:'var(--muted)',textWrap:'balance'}}>{title}</p>
    {(q.kind === 'deg' || q.kind === 'metre') && <div style={{textAlign:'center',marginBottom:10}}><button className={pixel ? 'pixel-btn' : 'ghost-btn'} style={{minHeight:44}} onClick={play}>{t('▶ Play it again', '▶ 다시 듣기')}</button></div>}
    {body}
    {why && !pixel && <div style={{marginTop:10,fontSize:13.5,color:'#4a4d86',background:'#fff',borderRadius:8,padding:'7px 10px',lineHeight:1.45}}>{why}</div>}
  </div>);
}
Object.assign(LISTEN_23_DRILL, { levels: L2_LEVELS, generate: genL2Question, check: (q, ans) => ans !== null && ans !== undefined && ans === q.answer, answerLabel: l2AnswerLabel, Question: L2Question, Learn: L2Learn });
// the teacher's copy (no Workbook: every step is by ear)
function L2Teacher() {
  const pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="listen-23" teacher>{content}</WbPage>);
  const lt = (i) => lwLet(i) + (i >= 12 ? "'" : '');   // C' = the C above middle C
  const pair = ([a, b]) => lt(a) + ' + ' + lt(b) + ' (' + l2IvName(a, b) + ')';
  const deg = (k, n) => lt(k) + ' then ' + lt(k + L2_DEG.find(y => y[0] === n)[1]) + ': the ' + l2DegName(n);
  const phText = (ph) => { const out = []; for (let j = 0; j < ph.length; j++) { const [k, b] = ph[j];
    if (b === 0.5 && ph[j + 1] && ph[j + 1][1] === 0.5) { out.push(lt(k) + '-' + lt(ph[j + 1][0]) + ' run-ning'); j++; } else out.push(lt(k) + ' ' + (b === 2 ? 'hold' : 'walk')); } return out.join(' · '); };
  P(<>
    <div style={{fontFamily:LB_SERIF,fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('listen-23')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 12px',lineHeight:1.5}}>No Workbook for this chapter: every step is by ear, as the Grade 2 and Grade 3 aural tests ask. Each block faces its Lesson Book page and gives you material to play, the same as the app uses. Play every test twice, as the examiner does. Middle C is C here; the C above is C'.</div>
    <TcBlock page={2} title="Two notes at once (Grade 2)" answers={<>{tcAns('PLAY TOGETHER', L2_G2.map(pair))}</>}
      watch="Humming a note between the two, or the top note every time. Ask for the lower one as often as the higher."
      say="“Two at once: pick one out and hum it.”"/>
    <TcBlock page={3} title="Any two notes (Grade 3)" answers={<>{tcAns('PLAY TOGETHER', [[4, 5], [0, 2], [2, 11], [5, 11], [9, 12], [0, 9]].map(pair))}</>}
      watch="The close ones (2nds) heard as one note. Play the asked note alone, then the pair again."
      say="“Close or far: follow just one.”"/>
    <TcBlock page={4} title="From the keynote (Grade 3)" answers={<>{tcAns('PLAY', [[0, 3], [7, 5], [5, 2], [2, 4], [0, 5], [7, 3]].map(([k, n]) => deg(k, n)))}</>}
      watch="Naming by guess. Sing up from the keynote, 1 2 3 4 5, every time until it is quick."
      say="“Sing up from home until you meet it.”"/>
  </>);
  P(<>
    <TcBlock page={5} title="Clap it back: two or three?" answers={<><div style={{fontSize:10.5,fontWeight:900,color:BK.muted,letterSpacing:'0.06em',marginBottom:4}}>{spTx('PLAY TWICE, THEN THE CHILD CLAPS AND SAYS TWO OR THREE (♩ = ' + L2_CLAP_BPM + ')')}</div>
      <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:'4px 14px'}}>{L2_CLAP.map((row, i) => <div key={i} style={{display:'flex',alignItems:'center',gap:6}}>{nvNum(i + 1)}<div style={{flex:1,minWidth:0}}>{rqStaffEl(row, { counts: false, hearts: false })}</div></div>)}</div></>}
      watch="The dotted crotchet clapped as two even notes. Long, short: the quaver comes late, just before the next beat."
      say="“Clap it back, then say two or three.”"/>
    <TcBlock page={6} title="Sing a longer tune" answers={<>{tcAns('PLAY TWICE, THEN THE CHILD SINGS', L2_PH.map(phText))}</>}
      watch="The skips sung as steps, or the held note cut short. Sing the skip slowly once, then the whole tune."
      say="“Longer, with skips: the notes and the rhythm, both.”"/>
    <TcBlock page={7} title="My five checks" answers={<div style={{fontSize:12,color:BK.ink,lineHeight:1.5}}>Each one with you at the piano, away from the screen, played twice: you play, the child hums, sings, names or claps. Use material the child has not heard this week. The first check is Grade 2; the second and third are Grade 3; the last two are both.</div>}/>
  </>);
  return <>{pages}</>;
}
TEACHER_COPIES['listen-23'] = L2Teacher;
'''
rep("""Object.assign(LISTEN_WRITE_DRILL, { levels: LW_LEVELS, generate: genLwQuestion, check: (q, ans) => ans !== null && ans !== undefined && ans === q.answer, answerLabel: lwAnswerLabel, Question: LwQuestion, Learn: LwLearn });""",
    """Object.assign(LISTEN_WRITE_DRILL, { levels: LW_LEVELS, generate: genLwQuestion, check: (q, ans) => ans !== null && ans !== undefined && ans === q.answer, answerLabel: lwAnswerLabel, Question: LwQuestion, Learn: LwLearn });""" + CH)

HOME = r'''
// ══ Build AJ: Hear and Sing Further on the Home (the Aural door, after Listen, clap, write) ══
LBH_FN['listen-23'] = (s) => l2LbPages(s);
const l2Add = (id, i, en, ko, benEn, bko, make) => { const spec = lbhSpec('listen-23', i, { make });
  TOOLS.push({ id, ch: 'concept', title: en, blurb: benEn, hidden: true, get kicker() { return t('Aural', '청음') + ' · ' + t('Hear and sing further', '더 듣고 부르기'); }, C: () => <KqEngine spec={spec}/> });
  lbhRetitle(id, en, ko, benEn, bko); };
const l2DegQ = (n, prev) => { let k, dg, g = 0; do { k = pick(L2_KEYS); dg = pick([2, 3, 4, 5]); } while (prev && prev.key === k + '-' + dg && g++ < 10); const d = L2_DEG.find(y => y[0] === dg)[1];
  return { kind: 'choice', cols: 4, prompt: ['The keynote, then a note: sing it, then name it.', '으뜸음, 그다음 음: 부르고, 이름을 말해요.'], opts: [2, 3, 4, 5].map(x => ({ id: x, label: () => l2DegName(x) })), ans: dg, ok: (v) => v === dg,
    key: k + '-' + dg, play: () => l2PlayDeg(k, d),
    fig: (c) => ({ mid: c.res ? <SpKb lo={0} hi={14} W={28} H={76} lit={{ [k]: 'pale', [k + d]: c.res === 'ok' ? 'good' : 'cor' }} names={Object.fromEntries([0, 2, 4, 5, 7].map((s, j) => [k + s, String(j + 1)]))}/> : null }), yes: ['Yes: the ' + ['', '', '2nd', '3rd', '4th', '5th'][dg] + '.', '맞아요: ' + ['', '', '2도', '3도', '4도', '5도'][dg] + '.'], no: ['It was the ' + ['', '', '2nd', '3rd', '4th', '5th'][dg] + ': sing up 1 2 3 4 5 and listen where you meet it.', ['', '', '2도', '3도', '4도', '5도'][dg] + '였어요: 1 2 3 4 5로 올라가며 어디서 만나는지 들어 봐요.'] }; };
l2Add('l2-dyad', 1, 'Two notes at once', '두 음을 함께', 'A 3rd or a 5th together: hum the higher or the lower.', '함께 울리는 3도나 5도: 높은 음이나 낮은 음.', lwTapQ(L2DyadPad, (n) => ({ fixed: { p: L2_G2[n % L2_G2.length], ask: n % 2 ? 'lo' : 'hi' } }), ['Hear the two notes, hum the one asked, then find it.', '두 음을 듣고, 묻는 음을 흥얼거리고, 찾아요.'], ['Heard and found ✓', '듣고 찾았어요 ✓']));
l2Add('l2-any', 2, 'Any two notes', '어떤 두 음이든', 'Any two together, within an octave from middle C.', '가운데 도부터 한 옥타브 안의 어떤 두 음이든.', lwTapQ((p) => <L2DyadPad any {...p}/>, (n) => ({ fixed: { p: L2_G3[(n * 7) % L2_G3.length], ask: n % 2 ? 'hi' : 'lo' } }), ['Hear the two notes, hum the one asked, then find it.', '두 음을 듣고, 묻는 음을 흥얼거리고, 찾아요.'], ['Heard and found ✓', '듣고 찾았어요 ✓']));
l2Add('l2-deg', 3, 'From the keynote', '으뜸음에서', 'The 2nd, 3rd, 4th or 5th: sing it, then name it.', '2도, 3도, 4도, 5도: 부르고, 이름 말하기.', l2DegQ);
l2Add('l2-clap', 4, 'Clap it back: two or three?', '따라 치고, 두 박? 세 박?', 'Heard twice, clapped back, then named.', '두 번 듣고, 따라 치고, 박자 말하기.', lwTapQ(L2ClapPad, (n) => ({ fixed: n % L2_CLAP.length }), ['Listen twice, tap it back, then say two or three.', '두 번 듣고, 따라 치고, 두 박인지 세 박인지 말해요.'], ['Clapped back and named ✓', '따라 치고 맞혔어요 ✓']));
l2Add('l2-sing', 5, 'Sing a longer tune', '더 긴 선율 따라 부르기', 'Longer, with skips: sing it, then play it.', '더 길고 건너뛰는 선율: 부르고 치기.', lwTapQ(L2SingPad, (n) => ({ fixed: n % L2_PH.length }), ['Listen twice, sing it back with its rhythm, then play it.', '두 번 듣고, 리듬까지 따라 부르고, 쳐요.'], ['Sung and played ✓', '부르고 쳤어요 ✓']));
'''
rep("""
lbhAdd('rb-finger', 'r-beat', 'rhythm', 'The beat in your fingers'""", HOME + """
lbhAdd('rb-finger', 'r-beat', 'rhythm', 'The beat in your fingers'""")
# the books and the house
rep("""const LESSON_BOOKS = { 'posture-hands': PostureLessonBook,""", """const LESSON_BOOKS = { 'listen-23': Listen23LessonBook, 'posture-hands': PostureLessonBook,""")
rep("""const LB_PAGE_FNS = { 'posture-hands': postureLbPages,""", """const LB_PAGE_FNS = { 'listen-23': l2LbPages, 'posture-hands': postureLbPages,""")
rep("""const HOUSE_ICONS = {"listen-write": """, """const HOUSE_ICONS = {"listen-23": "<path d=\\"M9 15C4 21 4 29 9 35M16 19C13 22 13 28 16 31\\"/><ellipse cx=\\"31\\" cy=\\"31\\" rx=\\"6\\" ry=\\"4.5\\" transform=\\"rotate(-20 31 31)\\" fill=\\"#26296b\\"/><ellipse cx=\\"31\\" cy=\\"21\\" rx=\\"6\\" ry=\\"4.5\\" transform=\\"rotate(-20 31 21)\\" fill=\\"#e4572e\\" stroke=\\"#e4572e\\"/><path d=\\"M36.6 29V8\\"/>", "listen-write": """)
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
