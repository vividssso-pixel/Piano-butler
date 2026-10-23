// ─── Rhythm on the Home (her order 2026-10-24: Pitch gaps, then Rhythm; groups from the four old rhythm chapters).
// Same engine as Pitch (KqEngine). RqTap is the listen-and-tap figure: one bar drawn like the book (NvBar),
// ▶ Listen (the notes sound with the click), ▶ Tap it (the click only: tap every note, or every beat with beats),
// scored on the audio clock (plRun, plMatch). Counting words as the app has them: 1 2 3 4, 1 + 2 +; walk, run-ning (타, 티-티).
const RQ_Q4 = [['q', 1], ['q', 1], ['q', 1], ['q', 1]];
// 4 clicks to get ready, then the bar; o.silent: the notes do not sound (you tap them); o.clicksTo: the click stops after that many beats of the bar
function rqRun(row, o = {}) {
  const n = nvBeats(row), snd = nvSounds(row), pairs = new Set(snd.filter(s => s.h === 1).map(s => Math.round(s.b - 0.5)));
  return plRun(4 + n, { bpm: o.bpm || NV_BPM, vol: 0.24, silentFrom: o.clicksTo != null ? 4 + o.clicksTo : null, extra: (ctx, tm, i, spb) => {
    if (i < 4) return; const b = i - 4;
    if (!o.silent) snd.filter(s => Math.floor(s.b + 1e-9) === b).forEach(s => blip(ctx, tm + (s.b - b) * spb, 261.63, Math.max(0.1, s.d * spb * 0.92), 0.2, 'triangle'));
    if (pairs.has(b) && SOUND.count === 'voice') sayCount(ctx, tm + spb / 2, 'and', 0.8);
  } });
}
// a long row drawn as bars of 4 beats, one under the other: [the bar's items, its first beat, its first sound]
const rqChunks = (row) => { if (nvBeats(row) <= 4) return [[row, 0, 0]]; const out = []; let cur = [], b = 0, b0 = 0, k = 0, k0 = 0;
  row.forEach(it => { cur.push(it); b += it[1]; if (b - b0 >= 4) { out.push([cur, b0, k0]); k0 = k + nvSounds(cur).length; k = k0; b0 = b; cur = []; } });
  if (cur.length) out.push([cur, b0, k0]); return out; };
function RqTap({ row, words = false, onResult, listen = true, tap = true, beats = false, clicksTo = null, maxW = 420 }) {
  const T = usePlTimers();
  const [mode, setMode] = useState(null), [phase, setPhase] = useState('ready'), [lit, setLit] = useState(-1), [count, setCount] = useState(0), [grow, setGrow] = useState({}), [res, setRes] = useState(null);
  const run = useRef(null), taps = useRef([]), held = useRef(null);
  const snd = nvSounds(row), n = nvBeats(row);
  function start(m) {
    T.clear(); setRes(null); setGrow({}); setLit(-1); taps.current = []; setMode(m);
    const r = rqRun(row, { silent: m === 'tap', clicksTo: m === 'tap' ? clicksTo : null }); if (!r) return; run.current = r;
    r.at.forEach((a, i) => T.at(r, a, () => { if (i < 4) { setCount(i + 1); setPhase('count'); } else { setLit(i - 4); setPhase('go'); } }));
    if (m !== 'tap') snd.forEach((s, k) => T.at(r, r.at[4] + s.b * r.spb, () => setGrow(g => ({ ...g, [k]: s.d * r.spb * 0.98 }))));
    T.at(r, r.at[4] + n * r.spb + 0.05, () => {
      if (held.current) { held.current(); held.current = null; }
      setLit(-1); setPhase('done');
      if (m !== 'tap') return;
      const want = beats ? Array.from({ length: n }, (_, i) => r.at[4] + i * r.spb) : snd.map(s => r.at[4] + s.b * r.spb), tol = Math.min(PL_TOL, r.spb * 0.22), mm = plMatch(want, taps.current, tol);
      const early = taps.current.filter(tp => tp < r.at[4] - tol).length, out = { hits: mm.hits, total: mm.total, extra: Math.max(0, mm.extra - early), marks: beats ? null : mm.offs.map(o => o === null ? '?' : '✓') };
      setRes(out); if (onResult) onResult(out);
    });
    setPhase('count'); setCount(0);
  }
  const doTap = React.useCallback(() => {
    const r = run.current; if (!r || mode !== 'tap' || (phase !== 'count' && phase !== 'go')) return;
    taps.current.push(r.now());
    const ctx = getAudio(); if (!ctx) return; if (held.current) held.current();
    held.current = beats ? blip(ctx, ctx.currentTime, 392, 0.12, 0.16, 'triangle') : blip(ctx, ctx.currentTime, 261.63, 4.3 * r.spb, 0.18, 'triangle');
  }, [phase, mode]);
  const release = React.useCallback(() => { if (held.current && !beats) { held.current(); held.current = null; } }, []);
  const live = phase === 'count' || phase === 'go', ok = res && res.hits === res.total && res.extra === 0;
  return <div style={{ margin: '0 0 6px' }} data-rq={JSON.stringify(beats ? Array.from({ length: n }, (_, i) => i) : snd.map(x => x.b))} data-rq-phase={phase}>
    {rqChunks(row).map(([sub, b0, k0], ci) => <NvBar key={ci} row={sub} grow={Object.fromEntries(Object.entries(grow).filter(([k]) => +k >= k0 && +k < k0 + nvSounds(sub).length).map(([k, v]) => [+k - k0, v]))} lit={lit >= b0 && lit < b0 + nvBeats(sub) ? lit - b0 : -1} marks={res && res.marks ? res.marks.slice(k0, k0 + nvSounds(sub).length) : null} words={words} maxW={maxW}/>)}
    <div style={{ textAlign: 'center', fontSize: 13, fontWeight: 800, color: BK.muted, minHeight: 18, margin: '2px 0 4px' }}>{phase === 'count' ? t('Get ready: ', '준비: ') + count : phase === 'go' ? (mode === 'tap' ? (clicksTo != null && lit >= clicksTo ? t('Keep going on your own!', '혼자 이어 가요!') : t('Tap!', '쳐요!')) : t('Listen and count', '들으면서 세요')) : ''}</div>
    <div style={{ display: 'flex', gap: 6, justifyContent: 'center', marginBottom: 8 }}>
      {listen && <button className="ghost-btn" onClick={() => start('listen')}>{t('▶ Listen', '▶ 듣기')}</button>}
      {tap && <button className="ghost-btn" onClick={() => start('tap')}>{beats ? t('▶ Tap the beat', '▶ 박 치기') : t('▶ Tap it', '▶ 쳐 보기')}</button>}
    </div>
    {mode === 'tap' && <PlPad on={live} onTap={doTap} onRelease={release} h={64} label={beats ? t('TAP EVERY BEAT', '박마다 쳐요') : t('TAP EVERY NOTE', '음마다 쳐요')}/>}
    {res && !onResult && <div style={{ textAlign: 'center', fontSize: 14.5, fontWeight: 900, marginTop: 6, color: ok ? BK.green : BK.coral }}>{t((beats ? 'Beats' : 'Notes') + ' on time: ' + res.hits + ' of ' + res.total + (res.extra ? ' · extra taps: ' + res.extra : ''), '제때 친 ' + (beats ? '박' : '음') + ': ' + res.total + '개 중 ' + res.hits + '개' + (res.extra ? ' · 더 친 것: ' + res.extra : ''))}</div>}
  </div>;
}
// a scored tap question: the figure calls c.pick(result); right when every note is on time and nothing extra
const rqTapQ = (row, o = {}) => ({ kind: 'tap', retry: true, ok: (v) => v && v.hits === v.total && v.extra === 0,
  fig: (c) => ({ mid: <RqTap key={c.qn} row={row} words={o.words} beats={o.beats} clicksTo={o.clicksTo} listen={o.listen !== false} onResult={(r) => c.pick(r)}/> }),
  no: (v) => ['On time: ' + v.hits + ' of ' + v.total + (v.extra ? ', with ' + v.extra + ' extra tap' + (v.extra > 1 ? 's' : '') : '') + '. ' + (o.tip ? o.tip[0] : 'Count out loud and try again.'), '제때 친 것: ' + v.total + '개 중 ' + v.hits + '개' + (v.extra ? ', 더 친 것 ' + v.extra + '개' : '') + '. ' + (o.tip ? o.tip[1] : '소리 내어 세면서 다시 해 봐요.')] });
const rqSmall = (row) => <div style={{ width: '100%', minWidth: 0 }}><NvBar row={row} count={false} maxW={230}/></div>;
// one bar played (no count-in, no clicks) for listening questions
const rqPlayRow = (row) => { const r = rqRun(row); return r; };
const RQ_SPEC = {};

// ══ 1. The steady beat ══
const rqSteady = (steady) => { const spb = 60 / PL_BPM; return plRun(8, steady ? { noVoice: true } : { noVoice: true, gaps: [spb, spb * 0.72, spb * 1.3, spb * 0.8, spb * 1.25, spb * 0.7, spb] }); };
const rqSteadyBtns = () => <><PlCircles n={8} r={13} gap={36}/><div style={{ display: 'flex', gap: 6, justifyContent: 'center', flexWrap: 'wrap', margin: '8px 0 8px' }}><button className="ghost-btn" onClick={() => rqSteady(true)}>{t('▶ Steady', '▶ 꾸준한 박')}</button><button className="ghost-btn" onClick={() => rqSteady(false)}>{t('▶ Not steady', '▶ 꾸준하지 않은 박')}</button></div></>;
RQ_SPEC['rb-beat'] = {
  title: ['The steady beat', '꾸준한 박'], allLine: ['The beat is the steady pulse under the music, like a heartbeat: the same gap every time. Listen, then tap along with the click.', '박은 음악 밑에 흐르는 꾸준한 맥박이에요. 심장 박동처럼 매번 간격이 같아요. 들어 보고, 클릭에 맞춰 쳐 보세요.'],
  fig: () => ({ mid: <RqTap row={RQ_Q4}/> }),
  steps: [
    { title: ['Like a heartbeat', '심장 박동처럼'], line: ['Four beats, evenly spaced. A heart lights up on each one.', '박 네 개가 똑같은 간격이에요. 박마다 하트가 켜져요.'], fig: () => ({ mid: <RqTap row={RQ_Q4} tap={false}/> }) },
    { title: ['Tap with the click', '클릭에 맞춰'], line: ['Four clicks to get ready, then tap once on every beat.', '클릭 네 번을 들으며 준비해요. 그다음 박마다 한 번씩 쳐요.'], fig: () => ({ mid: <RqTap row={RQ_Q4} listen={false}/> }) },
    { title: ['Steady or not?', '꾸준할까요?'], line: ['A steady beat never rushes and never drags. Listen to both.', '꾸준한 박은 서두르지도, 늦어지지도 않아요. 둘 다 들어 보세요.'], fig: () => ({ mid: rqSteadyBtns() }) },
  ],
  make: (n) => { if (n % 2 === 1) return { ...rqTapQ(RQ_Q4, { listen: false, tip: ['Tap exactly with each click.', '클릭과 꼭 같이 쳐요.'] }), prompt: ['Tap the beat with the click: four beats.', '클릭에 맞춰 박 네 개를 쳐 보세요.'], yes: ['Four beats, right on time.', '박 네 개, 딱 제때예요.'] };
    const steady = Math.random() < 0.5, ans = steady ? 's' : 'u';
    return { kind: 'choice', cols: 2, prompt: ['Listen: is the beat steady?', '들어 보세요. 박이 꾸준한가요?'], opts: [{ id: 's', label: () => t('Steady', '꾸준해요') }, { id: 'u', label: () => t('Not steady', '꾸준하지 않아요') }], ans, ok: (v) => v === ans, play: () => rqSteady(steady),
      fig: () => ({ mid: <PlCircles n={8} r={13} gap={36}/> }), yes: steady ? ['Steady: the same gap every time.', '꾸준해요. 매번 간격이 같아요.'] : ['Not steady: some beats came early, some late.', '꾸준하지 않아요. 어떤 박은 빨리, 어떤 박은 늦게 왔어요.'],
      no: steady ? ['It was steady: every gap the same. Press ♪ Again.', '꾸준한 박이었어요. 간격이 모두 같아요. ♪ 다시를 눌러 보세요.'] : ['Listen again: some beats rushed, some dragged.', '다시 들어 보세요. 어떤 박은 서두르고, 어떤 박은 늦어졌어요.'] }; },
};
const RQ_Q8 = RQ_Q4.concat(RQ_Q4);
RQ_SPEC['rb-count'] = {
  title: ['Count out loud', '소리 내어 세기'], allLine: ['Count 1 2 3 4 with the beats, then back to 1. Counting out loud keeps the beat steady, even when the click stops.', '박에 맞춰 1 2 3 4를 세고, 다시 1로 돌아가요. 소리 내어 세면 클릭이 멈춰도 박이 꾸준해요.'],
  fig: () => ({ mid: <RqTap row={RQ_Q8} maxW={520}/> }),
  steps: [
    { title: ['1 2 3 4', '1 2 3 4'], line: ['One number on each beat. After 4 comes 1 again.', '박마다 숫자 하나씩. 4 다음에는 다시 1이에요.'], fig: () => ({ mid: <RqTap row={RQ_Q8} tap={false} maxW={520}/> }) },
    { title: ['Keep it going', '혼자서 이어 가기'], line: ['The click plays for four beats, then stops. Keep counting and keep tapping on your own.', '클릭이 네 박 동안 나오다가 멈춰요. 혼자서 계속 세면서 계속 쳐요.'], fig: () => ({ mid: <RqTap row={RQ_Q8} listen={false} clicksTo={4} maxW={520}/> }) },
  ],
  make: (n) => n % 2 === 0 ? { ...rqTapQ(RQ_Q8, { listen: false, clicksTo: 4, tip: ['Count out loud when the click stops.', '클릭이 멈추면 소리 내어 세요.'] }), prompt: ['The click stops after four beats. Keep tapping all eight.', '클릭은 네 박 뒤에 멈춰요. 여덟 박을 끝까지 쳐요.'], yes: ['Steady all the way, click or no click.', '클릭이 있든 없든 끝까지 꾸준해요.'] }
    : { ...rqTapQ(RQ_Q8, { listen: false }), prompt: ['Tap all eight beats with the click. Count 1 2 3 4, 1 2 3 4.', '클릭에 맞춰 여덟 박을 쳐요. 1 2 3 4, 1 2 3 4로 세요.'], yes: ['Eight beats, all on time.', '여덟 박 모두 제때예요.'] },
};
const RQ_SIL = [[['q', 1], ['q', 1], ['r', 1], ['q', 1]], [['q', 1], ['r', 1], ['q', 1], ['r', 1]], [['r', 1], ['q', 1], ['q', 1], ['q', 1]], [['q', 1], ['q', 1], ['q', 1], ['r', 1]]];
RQ_SPEC['rb-silent'] = {
  title: ['Silent beats still count', '소리 없는 박도 세요'], allLine: ['A rest is a beat with no sound. Keep counting through it, and do not tap.', '쉼표는 소리가 없는 박이에요. 계속 세되, 치지는 않아요.'],
  fig: () => ({ mid: <RqTap row={RQ_SIL[0]}/> }),
  steps: [
    { title: ['A beat with no note', '음표 없는 박'], line: ['On beat 3 there is a rest: the beat goes on, but there is no sound.', '3박에 쉼표가 있어요. 박은 이어지지만 소리는 나지 않아요.'], fig: () => ({ mid: <RqTap row={RQ_SIL[0]} tap={false}/> }) },
    { title: ['Count it, do not tap it', '세고, 치지는 않아요'], line: ['Tap only the notes. Say the rest’s number in your head.', '음표만 쳐요. 쉼표의 숫자는 속으로 세요.'], fig: () => ({ mid: <RqTap row={RQ_SIL[1]}/> }) },
  ],
  make: (n, prev) => { let i, g = 0; do { i = kqRnd(RQ_SIL.length); } while (prev && prev.i === i && g++ < 8); const row = RQ_SIL[i], rb = row.map((x, j) => x[0] === 'r' ? j + 1 : null).filter(Boolean);
    if (n % 2 === 0) return { i, ...rqTapQ(row, { tip: ['Tap the notes only; count the rests.', '음표만 치고, 쉼표는 세기만 해요.'] }), prompt: ['Tap the notes. Count the rests, but do not tap them.', '음표를 쳐요. 쉼표는 세기만 하고 치지 않아요.'], yes: ['Notes tapped, rests counted.', '음표는 치고, 쉼표는 셌어요.'] };
    const ans = String(rb[0]);
    return { i, kind: 'choice', cols: 4, prompt: ['Listen: on which beat is there no sound?', '들어 보세요. 몇 박에 소리가 없나요?'], opts: ['1', '2', '3', '4'].map(x => ({ id: x, label: x })), ans, ok: (v) => rb.includes(+v), play: () => rqRun(row),
      fig: (c) => ({ mid: c.res ? <NvBar row={row} maxW={420}/> : <PlCircles n={4} r={14} gap={40}/> }), yes: [rb.length > 1 ? 'Beats ' + rb.join(' and ') + ': rests.' : 'Beat ' + rb[0] + ': a rest.', rb.join('박과 ') + '박: 쉼표예요.'], no: ['The silent beat' + (rb.length > 1 ? 's were ' : ' was ') + rb.join(' and ') + '. Count along and listen again.', '소리 없는 박은 ' + rb.join('박과 ') + '박이었어요. 세면서 다시 들어 보세요.'] }; },
};
const RQ_WB = [['q', 1], ['p', 1], ['q', 1], ['p', 1]], RQ_WB2 = [['p', 1], ['p', 1], ['q', 1], ['q', 1]];
RQ_SPEC['rb-words'] = {
  title: ['Beat or rhythm?', '박일까요, 리듬일까요?'], allLine: ['The beat stays the same. The rhythm is the pattern of long and short sounds on top of it: walk, run-ning.', '박은 늘 같아요. 리듬은 그 위에 놓인 길고 짧은 소리의 무늬예요. 타, 티-티.'],
  fig: () => ({ mid: <RqTap row={RQ_WB} words/> }),
  steps: [
    { title: ['The beat: every heart', '박: 하트마다'], line: ['Tap once on every heart, whatever the notes do.', '음표가 어떻든 하트마다 한 번씩 쳐요.'], fig: () => ({ mid: <RqTap row={RQ_WB} words beats/> }) },
    { title: ['The rhythm: every sound', '리듬: 소리마다'], line: ['Now tap every sound: walk is one tap, run-ning is two quick taps on one beat.', '이번엔 소리마다 쳐요. 타는 한 번, 티-티는 한 박에 빠르게 두 번이에요.'], fig: () => ({ mid: <RqTap row={RQ_WB} words/> }) },
  ],
  make: (n) => { const row = n % 4 < 2 ? RQ_WB : RQ_WB2, k = n % 3;
    if (k === 0) return { ...rqTapQ(row, { words: true, beats: true, tip: ['The beat: once on every heart.', '박: 하트마다 한 번.'] }), prompt: ['Tap the beat: once on every heart.', '박을 쳐요. 하트마다 한 번.'], yes: ['That is the beat: four even taps.', '그게 박이에요. 고른 탭 네 번.'] };
    if (k === 1) return { ...rqTapQ(row, { words: true, tip: ['The rhythm: every sound, two on run-ning.', '리듬: 소리마다, 티-티는 두 번.'] }), prompt: ['Tap the rhythm: every sound.', '리듬을 쳐요. 소리마다.'], yes: ['That is the rhythm: walk and run-ning.', '그게 리듬이에요. 타와 티-티.'] };
    const beat = Math.random() < 0.5, ans = beat ? 'b' : 'r';
    return { kind: 'choice', cols: 2, prompt: ['Listen: is that the beat or the rhythm?', '들어 보세요. 박일까요, 리듬일까요?'], opts: [{ id: 'b', label: () => t('The beat', '박') }, { id: 'r', label: () => t('The rhythm', '리듬') }], ans, ok: (v) => v === ans, play: () => rqRun(beat ? RQ_Q4 : row),
      fig: (c) => ({ mid: c.res ? <NvBar row={beat ? RQ_Q4 : row} words maxW={420}/> : null }), yes: beat ? ['The beat: four even sounds.', '박이에요. 고른 소리 네 번.'] : ['The rhythm: long and short sounds.', '리듬이에요. 길고 짧은 소리.'], no: beat ? ['Four even sounds, one on each beat: the beat.', '박마다 하나씩 고른 소리 네 번: 박이에요.'] : ['Long and short sounds, some two to a beat: the rhythm.', '길고 짧은 소리, 한 박에 두 개도 있어요: 리듬이에요.'] }; },
};

// ══ 2. How long notes last ══
const RQ_GL = { crotchet: [NV_NOTES[2], '1'], minim: [NV_NOTES[1], '2'], dminim: [NV_DOTTED[0], '3'], semibreve: [NV_NOTES[0], '4'], quaver: [NV_NOTES[3], '½'] };
const RQ_GL_W = { crotchet: ['crotchet', '4분음표'], minim: ['minim', '2분음표'], dminim: ['dotted minim', '점2분음표'], semibreve: ['semibreve', '온음표'], quaver: ['quaver', '8분음표'] };
const rqBeatsQ = (id) => { const [item, ans] = RQ_GL[id], w = RQ_GL_W[id];
  return { kind: 'choice', cols: 5, prompt: ['How many beats does a ' + w[0] + ' last?', w[1] + '는 몇 박일까요?'], opts: ['½', '1', '2', '3', '4'].map(x => ({ id: x, label: x })), ans, ok: (v) => v === ans,
    fig: () => ({ mid: <div style={{ display: 'flex', justifyContent: 'center', margin: '4px 0 8px' }}><Glyph item={item} size={90}/></div> }), yes: ['A ' + w[0] + ': ' + ans + (ans === '1' ? ' beat.' : ans === '½' ? ' a beat.' : ' beats.'), w[1] + ': ' + ans + '박이에요.'], no: ['A ' + w[0] + ' lasts ' + ans + (ans === '1' ? ' beat.' : ans === '½' ? ' a beat: two fill one beat.' : ' beats.'), w[1] + '는 ' + ans + '박이에요.' + (ans === '½' ? ' 둘이 모여 1박이에요.' : '')] }; };
const rqHearQ = (rows, i) => { const row = rows[i], opts = rows.map((r, j) => ({ id: String(j), label: () => rqSmall(r) }));
  return { kind: 'choice', cols: 1, prompt: ['Listen: which bar was it?', '들어 보세요. 어느 마디였을까요?'], opts, ans: String(i), ok: (v) => v === String(i), play: () => rqRun(row), fig: () => ({ mid: null }),
    yes: ['That is the one.', '바로 그거예요.'], no: ['Listen again and count the beats of each sound.', '다시 들으면서 소리마다 몇 박인지 세어 보세요.'] }; };
const rqNvLesson = (o) => ({
  title: o.title, allLine: o.allLine, fig: () => ({ mid: <RqTap row={o.rows[0]} words={o.words}/> }),
  steps: o.steps.map((s, j) => ({ title: s[0], line: s[1], fig: () => ({ mid: <RqTap row={o.rows[s[2]]} words={o.words} tap={s[3] !== false}/> }) })),
  make: (n, prev) => { const k = n % 3; let i, g = 0; do { i = kqRnd(o.rows.length); } while (prev && prev.i === i && o.rows.length > 1 && g++ < 8);
    if (k === 0) return { i, ...rqTapQ(o.rows[i], { words: o.words }), prompt: ['Tap it: one tap for each note, held as long as the note.', '쳐 보세요. 음마다 한 번, 음의 길이만큼 누르고 있어요.'], yes: ['Every note on time.', '모든 음이 제때예요.'] };
    if (k === 1) return { i, ...o.ask(n) };
    const pool = o.hear || o.rows; let j = kqRnd(pool.length); return { i: j, ...rqHearQ(pool.slice(0, 3), Math.min(j, 2)) }; },
});
const RQ_HEAR = [[['q', 1], ['q', 1], ['h', 2]], [['h', 2], ['h', 2]], [['q', 1], ['q', 1], ['q', 1], ['q', 1]]];
RQ_SPEC['rn-q'] = rqNvLesson({ title: ['The crotchet: one beat', '4분음표: 1박'], allLine: ['A crotchet lasts one beat: one note on each heart. Its word is walk.', '4분음표는 1박이에요. 하트마다 음 하나. 말로는 타예요.'], words: true,
  rows: [RQ_Q4], hear: RQ_HEAR, steps: [[['One beat each', '하나에 1박'], ['Listen: each sound line is one beat long.', '들어 보세요. 소리 줄 하나가 1박 길이예요.'], 0, false], [['Walk the crotchets', '4분음표 걷기'], ['Tap one walk on every beat.', '박마다 타를 한 번씩 쳐요.'], 0]], ask: () => rqBeatsQ('crotchet') });
RQ_SPEC['rn-h'] = rqNvLesson({ title: ['The minim: two beats', '2분음표: 2박'], allLine: ['A minim lasts two beats: play on 1, hold through 2. Its note head is open.', '2분음표는 2박이에요. 1에서 치고 2까지 누르고 있어요. 머리가 비어 있어요.'],
  rows: [[['h', 2], ['h', 2]], [['q', 1], ['q', 1], ['h', 2]]], hear: RQ_HEAR, steps: [[['Play, then hold', '치고, 누르고'], ['Two minims: each sound line grows for two beats.', '2분음표 둘: 소리 줄이 2박 동안 자라요.'], 0, false], [['Crotchets and a minim', '4분음표와 2분음표'], ['1, 2, then 3 held through 4.', '1, 2, 그다음 3에서 쳐서 4까지 누르고 있어요.'], 1]], ask: () => rqBeatsQ('minim') });
RQ_SPEC['rn-long'] = rqNvLesson({ title: ['Three and four beats', '3박과 4박'], allLine: ['A dot adds half again: a dotted minim lasts three beats. A semibreve lasts four, a whole 4/4 bar.', '점은 원래 길이의 반을 더해요. 점2분음표는 3박이에요. 온음표는 4박, 4/4 한 마디 전체예요.'],
  rows: [[['hd', 3], ['q', 1]], [['w', 4]]], hear: [[['hd', 3], ['q', 1]], [['w', 4]], [['h', 2], ['h', 2]]], steps: [[['The dotted minim', '점2분음표'], ['2 and half of 2 more: three beats, then a crotchet on 4.', '2박에 그 반을 더해 3박. 그다음 4에 4분음표.'], 0], [['The semibreve', '온음표'], ['One note held for the whole bar: 1 2 3 4.', '한 마디 내내 음 하나를 누르고 있어요. 1 2 3 4.'], 1]], ask: (n) => rqBeatsQ(n % 2 ? 'dminim' : 'semibreve') });
RQ_SPEC['rn-p'] = rqNvLesson({ title: ['Two quavers on one beat', '8분음표 둘이 1박'], allLine: ['Two quavers share one beat: count 1 +. Their word is run-ning, two quick sounds.', '8분음표 둘이 1박을 나눠요. 1 + 로 세요. 말로는 티-티, 빠른 소리 둘이에요.'], words: true,
  rows: [RQ_WB, RQ_WB2], hear: [RQ_WB, RQ_WB2, RQ_Q4], steps: [[['Walk and run', '걷고 달리기'], ['walk, run-ning, walk, run-ning: count 1, 2 +, 3, 4 +.', '타, 티-티, 타, 티-티: 1, 2 +, 3, 4 +로 세요.'], 0], [['Run first', '먼저 달리기'], ['run-ning, run-ning, walk, walk.', '티-티, 티-티, 타, 타.'], 1]], ask: () => rqBeatsQ('quaver') });
const RQ_RESTQ = () => { const pairs = [['crotchet', NV_NOTES[2], NV_RESTS[2]], ['minim', NV_NOTES[1], NV_RESTS[1]], ['semibreve', NV_NOTES[0], NV_RESTS[0]]], i = kqRnd(3), [id, note] = pairs[i], w = RQ_GL_W[id];
  return { kind: 'choice', cols: 3, prompt: ['Which rest lasts as long as this ' + w[0] + '?', '이 ' + w[1] + '와 길이가 같은 쉼표는?'], opts: pairs.map(([x, , r]) => ({ id: x, label: () => <Glyph item={r} size={54}/> })), ans: id, ok: (v) => v === id,
    fig: () => ({ mid: <div style={{ display: 'flex', justifyContent: 'center', margin: '4px 0 8px' }}><Glyph item={note} size={84}/></div> }), yes: ['The ' + w[0] + ' rest: the same length, in silence.', w[1].replace('음표', '쉼표') + ': 같은 길이의 침묵이에요.'], no: ['A note and its rest share a name and a length: the ' + w[0] + ' rest.', '음표와 쉼표는 이름과 길이가 같아요. ' + w[1].replace('음표', '쉼표') + '예요.'] }; };
RQ_SPEC['rn-rest'] = rqNvLesson({ title: ['Rests: silence you count', '쉼표: 세는 침묵'], allLine: ['Every note has a rest of the same length and name. Count the rest, but do not play.', '음표마다 길이와 이름이 같은 쉼표가 있어요. 쉼표는 세기만 하고 치지 않아요.'],
  rows: [[['q', 1], ['q', 1], ['r', 1], ['q', 1]], [['h', 2], ['hr', 2]]], hear: [[['q', 1], ['q', 1], ['r', 1], ['q', 1]], [['h', 2], ['hr', 2]], RQ_Q4], steps: [[['A crotchet rest', '4분쉼표'], ['Play 1, 2 and 4. On 3, count in silence.', '1, 2, 4에서 쳐요. 3에서는 소리 없이 세요.'], 0], [['A minim rest', '2분쉼표'], ['A minim on 1, then two beats of silence: 3 4.', '1에서 2분음표, 그다음 2박 동안 침묵: 3 4.'], 1]], ask: () => RQ_RESTQ() });

const RQ_ROWS = [
  ['rb-beat', 'The steady beat', '꾸준한 박', 'Like a heartbeat; tap with the click.', '심장 박동처럼, 클릭에 맞춰 치기.'],
  ['rb-count', 'Count out loud', '소리 내어 세기', '1 2 3 4, and keep going on your own.', '1 2 3 4, 그리고 혼자서 이어 가기.'],
  ['rb-silent', 'Silent beats still count', '소리 없는 박도 세요', 'A rest: count it, do not tap it.', '쉼표: 세되 치지 않기.'],
  ['rb-words', 'Beat or rhythm?', '박일까요, 리듬일까요?', 'The steady beat, the long and short sounds.', '꾸준한 박, 길고 짧은 소리.'],
  ['rn-q', 'The crotchet: one beat', '4분음표: 1박', 'One note on each beat: walk.', '박마다 음 하나: 타.'],
  ['rn-h', 'The minim: two beats', '2분음표: 2박', 'Play on 1, hold through 2.', '1에서 치고 2까지.'],
  ['rn-long', 'Three and four beats', '3박과 4박', 'The dotted minim and the semibreve.', '점2분음표와 온음표.'],
  ['rn-p', 'Two quavers on one beat', '8분음표 둘이 1박', 'run-ning: 1 +.', '티-티: 1 +.'],
  ['rn-rest', 'Rests: silence you count', '쉼표: 세는 침묵', 'The same name and length as the note.', '음표와 같은 이름, 같은 길이.'],
];
RQ_ROWS.forEach(([id, en, ko, benEn, bko]) => {
  TOOLS.push({ id, ch: 'concept', title: en, blurb: benEn, hidden: true, get kicker() { return TOOL_AREAS.find(a => a.id === 'rhythm').name + ' · ' + homeCatById('r-beat').name; }, C: () => <KqEngine spec={RQ_SPEC[id]}/> });
  TOOL_KO[id] = [ko, bko];
  const tl = TOOLS[TOOLS.length - 1], k = TOOL_KO[id], ti = tl.title, bl = tl.blurb; tl.titleEn = ti; tl.blurbEn = bl;
  Object.defineProperty(tl, 'title', { get: () => (LANG === 'ko' ? k[0] : ti), enumerable: true, configurable: true });
  Object.defineProperty(tl, 'blurb', { get: () => (LANG === 'ko' ? k[1] : bl), enumerable: true, configurable: true });
  TOOL_CONCEPT[id] = 'r-beat';
});
