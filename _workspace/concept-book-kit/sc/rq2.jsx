// ─── Rhythm on the Home, part 2: bars and time signatures, rhythm patterns. Rows on the staff with the rhythm chapter's
// renderer (srhRaw: time signature, bar lines, beams, dots, ties, an anacrusis), played and scored the same way (srhRun,
// srhScore: on time, and held for the note's length). RqStaff is the figure; rqStaffQ the scored question.
// a row's sounds with its ties merged: the tied-to note is not played again, the first one lasts both
const rqTied = (items, ties) => { const snd = srhSounds(items), skip = new Set((ties || []).map(([, b]) => b));
  const keep = snd.map((s, i) => [s, i]).filter(([s]) => !skip.has(s.j));
  return keep.map(([s, i]) => { const tie = (ties || []).find(([a]) => a === s.j); if (!tie) return { ...s, orig: i }; const t2 = snd.find(x => x.j === tie[1]); return { ...s, d: s.d + (t2 ? t2.d : 0), orig: i }; }); };
// srhRun with ties: the tied-to notes are not struck
function rqRunS(items, o = {}) {
  const u = o.unit || 1, top = o.clicks || srhTop(items), from = Math.round(o.from || 0), lead = top + from, n = Math.ceil(srhBeats(items) / u - 1e-6), snd = rqTied(items, o.ties);
  const vol = 0.24, voice = SOUND.count === 'voice' && u === 1, acc = (pos) => !!o.accent && (o.accentAt ? o.accentAt.includes(pos) : pos === 0);
  const sw = (b) => o.swing && Math.abs(b % 1 - 0.5) < 1e-6 ? b + 1 / 6 : b;   // swing: the + comes two-thirds of the way through the beat
  const r = plRun(lead + n, { bpm: (o.bpm || SRH_BPM) / u, vol, silentFrom: 0, extra: (ctx, tm, i, spb) => {
    const pos = i < top ? i : i < lead ? i - top : (i - lead + from) % top;
    if (!(voice && sayCount(ctx, tm, String(pos + 1), 1))) metroClick(ctx, tm, acc(pos), acc(pos) ? 0.42 : vol);
    if (i < lead) return; const b = (i - lead) * u;
    snd.filter(s => s.b > b - 1e-9 && s.b < b + u - 1e-9).forEach(s => { if (!o.silent && !s.rest) blip(ctx, tm + (sw(s.b) - b) / u * spb, SRH_HZ, Math.max(0.08, s.d / u * spb * 0.9), 0.2, 'triangle'); });
  } });
  if (r) r.lead = lead; return r;
}
const rqD = (items) => items.some(x => x[0] === '|') ? 34 : 44;
// only: the beats (from the row's start) to tap instead of the notes, e.g. beat 1 of every bar
function RqStaff({ items, from = 0, ties, onResult, listen = true, tap = true, only = null, accent = false, counts, unit = 1, clicks, accentAt, swing, so = {}, bpm }) {
  const T = usePlTimers();
  const [mode, setMode] = useState(null), [phase, setPhase] = useState('ready'), [lit, setLit] = useState(-1), [count, setCount] = useState(''), [res, setRes] = useState(null);
  const run = useRef(null), taps = useRef([]), rels = useRef([]), held = useRef(null);
  const top = clicks || srhTop(items), snd = rqTied(items, ties).map(s => ({ ...s, b: s.b / unit, d: s.d / unit })), n = srhBeats(items) / unit;
  const stopHeld = () => { if (held.current) { held.current(); held.current = null; } };
  function start(m) {
    T.clear(); stopHeld(); setRes(null); setLit(-1); taps.current = []; rels.current = []; setMode(m);
    const r = rqRunS(items, { from, ties, silent: m === 'tap', accent, unit, clicks, accentAt, swing, bpm }); if (!r) return; run.current = r;
    const go = r.at[r.lead];
    r.at.slice(0, r.lead).forEach((a, i) => T.at(r, a, () => { setPhase('count'); setCount(String(i < top ? i + 1 : i - top + 1)); }));
    T.at(r, go, () => setPhase('go'));
    snd.forEach(s => T.at(r, go + s.b * r.spb, () => setLit(s.orig)));
    T.at(r, go + n * r.spb + 0.05, () => {
      stopHeld(); setLit(-1); setPhase('done');
      if (m !== 'tap') return;
      let out;
      if (only) { const tol = Math.min(PL_TOL, r.spb * 0.22), mm = plMatch(only.map(b => go + b * r.spb), taps.current, tol), early = taps.current.filter(tp => tp < go - tol).length, extra = Math.max(0, mm.extra - early);
        out = { hits: mm.hits, held: mm.hits, total: mm.total, extra, marks: null, ok: mm.hits === mm.total && extra === 0 }; }
      else { const sc = srhScore(snd, go, r.spb, taps.current, rels.current, r.now()), marks = {}; Object.entries(sc.marks).forEach(([i, v]) => { marks[snd[+i].orig] = v; }); out = { ...sc, marks }; }
      setRes(out); if (onResult) onResult(out);
    });
    setPhase('count'); setCount('');
  }
  const doTap = React.useCallback(() => {
    const r = run.current; if (!r || mode !== 'tap' || (phase !== 'count' && phase !== 'go')) return;
    taps.current.push(r.now()); const ctx = getAudio(); if (!ctx) return; stopHeld();
    held.current = only ? blip(ctx, ctx.currentTime, SRH_HZ, 0.12, 0.16, 'triangle') : blip(ctx, ctx.currentTime, SRH_HZ, 4.3 * r.spb, 0.18, 'triangle');
  }, [phase, mode]);
  const release = React.useCallback(() => { const r = run.current, j = taps.current.length - 1; if (r && j >= 0 && rels.current[j] == null) rels.current[j] = r.now(); stopHeld(); }, []);
  const live = phase === 'count' || phase === 'go';
  const want = only ? only.map(b => [b, 0.2]) : snd.filter(s => !s.rest).map(s => [s.b, s.d]);
  return <div style={{ margin: '0 0 6px' }} data-rq={JSON.stringify(want)} data-rq-spb={60 * unit / (bpm || SRH_BPM)} data-rq-phase={phase}>
    <SrhFit items={items} o={{ D: rqD(items), from, lit, ties, marks: res ? res.marks : null, counts, ...so }}/>
    <div style={{ textAlign: 'center', fontSize: 13, fontWeight: 800, color: BK.muted, minHeight: 18, margin: '2px 0 4px' }}>{phase === 'count' ? t('Get ready: ', '준비: ') + count : phase === 'go' ? (mode === 'tap' ? t('Tap!', '쳐요!') : t('Listen and count', '들으면서 세요')) : ''}</div>
    <div style={{ display: 'flex', gap: 6, justifyContent: 'center', marginBottom: 8 }}>
      {listen && <button className="ghost-btn" onClick={() => start('listen')}>{t('▶ Listen', '▶ 듣기')}</button>}
      {tap && <button className="ghost-btn" onClick={() => start('tap')}>{only ? t('▶ Tap the beats', '▶ 박 치기') : t('▶ Tap it', '▶ 쳐 보기')}</button>}
    </div>
    {mode === 'tap' && <PlPad on={live} onTap={doTap} onRelease={release} h={64} label={only ? t('TAP THE STRONG BEATS', '센박에서 쳐요') : t('HOLD EACH NOTE', '음표마다 누르고 있어요')}/>}
    {res && !onResult && <div style={{ textAlign: 'center', fontSize: 14.5, fontWeight: 900, marginTop: 6, color: res.ok ? BK.green : BK.coral }}>{srhResult(res)}{res.ok ? '  ✓' : ''}</div>}
  </div>;
}
const rqStaffQ = (items, o = {}) => ({ kind: 'tap', retry: true, ok: (v) => v && v.ok,
  fig: (c) => ({ mid: <RqStaff key={c.qn} items={items} from={o.from} ties={o.ties} only={o.only} accent={o.accent} listen={o.listen !== false} unit={o.unit} clicks={o.clicks} accentAt={o.accentAt} swing={o.swing} so={o.so} bpm={o.bpm} onResult={(r) => c.pick(r)}/> }),
  prompt: o.prompt || ['Tap it: press for each note and hold it for its length.', '쳐 보세요. 음표마다 누르고, 그 길이만큼 누르고 있어요.'], yes: o.yes || ['Every note on time and held right.', '모든 음이 제때, 길이도 맞아요.'],
  no: (v) => ['On time: ' + v.hits + ' of ' + v.total + (o.only ? '' : ' · held right: ' + v.held + ' of ' + v.total) + (v.extra ? ' · extra taps: ' + v.extra : '') + '. ' + (o.tip ? o.tip[0] : 'Count out loud and try again.'), '제때 친 것: ' + v.total + '개 중 ' + v.hits + '개' + (o.only ? '' : ' · 길이 맞게: ' + v.total + '개 중 ' + v.held + '개') + (v.extra ? ' · 더 친 것: ' + v.extra + '개' : '') + '. ' + (o.tip ? o.tip[1] : '소리 내어 세면서 다시 해 봐요.')] });
const rqStaffEl = (items, o = {}) => <SrhFit items={items} o={{ D: rqD(items), ...o }}/>;
const rqHearS = (rows, i, o = {}) => ({ kind: 'choice', cols: 1, prompt: ['Listen: which line was it?', '들어 보세요. 어느 줄이었을까요?'], opts: rows.map((r, j) => ({ id: String(j), label: () => <div style={{ width: '100%', minWidth: 0 }}>{rqStaffEl(r.items || r, { counts: false, hearts: false, from: r.from })}</div> })), ans: String(i), ok: (v) => v === String(i),
  play: () => rqRunS(rows[i].items || rows[i], { from: rows[i].from }), fig: () => ({ mid: null }), yes: ['That is the one.', '바로 그거예요.'], no: ['Listen again and count along.', '다시 들으면서 함께 세어 보세요.'] });

// ══ 3. Bars and time signatures ══
const RQ_BAR2 = [['ts', 4], ['q'], ['q'], ['q'], ['q'], ['|'], ['h'], ['h'], ['||']];
const RQ_BAR3 = [['ts', 3], ['q'], ['q'], ['q'], ['|'], ['h'], ['q'], ['|'], ['hd'], ['||']];
const RQ_BAR24 = [['ts', 2], ['q'], ['q'], ['|'], ['h'], ['|'], ['q'], ['q'], ['|'], ['h'], ['||']];
RQ_SPEC['rt-bars'] = {
  title: ['Bars and bar lines', '마디와 세로줄'], allLine: ['Bar lines cut the music into bars. In 4/4 every bar holds four beats. A double bar line marks the end.', '세로줄이 음악을 마디로 나눠요. 4/4에서는 마디마다 4박이 들어가요. 겹세로줄은 끝을 알려요.'],
  fig: () => ({ mid: <RqStaff items={RQ_BAR2}/> }),
  steps: [
    { title: ['A bar line', '세로줄'], line: ['Four crotchets, a bar line, then two minims: two bars, four beats each.', '4분음표 넷, 세로줄, 그다음 2분음표 둘. 두 마디이고, 마디마다 4박이에요.'], fig: () => ({ mid: <RqStaff items={RQ_BAR2} tap={false}/> }) },
    { title: ['After the bar line, 1 again', '세로줄 다음은 다시 1'], line: ['Each bar starts counting from 1. The thick double line at the end means the piece is over.', '마디마다 1부터 다시 세요. 끝의 굵은 겹세로줄은 곡이 끝났다는 뜻이에요.'], fig: () => ({ mid: <RqStaff items={RQ_BAR2}/> }) },
  ],
  make: (n) => { if (n % 2 === 0) return rqStaffQ(RQ_BAR2);
    const rows = [[RQ_BAR2, 2], [RQ_BAR3, 3], [RQ_BAR24, 4]], [items, ans] = kqPick(rows);
    return { kind: 'choice', cols: 4, prompt: ['How many bars are there?', '마디가 몇 개일까요?'], opts: ['1', '2', '3', '4'].map(x => ({ id: x, label: x })), ans: String(ans), ok: (v) => v === String(ans), fig: () => ({ mid: rqStaffEl(items) }),
      yes: [ans + ' bars: count the spaces between the bar lines.', ans + '마디예요. 세로줄 사이의 칸을 세어 보세요.'], no: ['Count from the time signature to the first bar line, then on to the double bar line: ' + ans + '.', '박자표에서 첫 세로줄까지, 그다음 겹세로줄까지 세어 보세요. ' + ans + '개예요.'] }; },
};
RQ_SPEC['rt-ts'] = {
  title: ['The two numbers', '박자표의 두 숫자'], allLine: ['A time signature has two numbers. The top one: how many beats in a bar. The bottom 4: each beat is a crotchet.', '박자표에는 숫자가 두 개 있어요. 위의 숫자는 한 마디의 박 수예요. 아래의 4는 한 박이 4분음표라는 뜻이에요.'],
  fig: () => ({ mid: <RqStaff items={RQ_BAR3}/> }),
  steps: [
    { title: ['2/4: two beats', '2/4: 2박'], line: ['Two crotchet beats in every bar: 1 2, 1 2.', '마디마다 4분음표 2박: 1 2, 1 2.'], fig: () => ({ mid: <RqStaff items={RQ_BAR24}/> }) },
    { title: ['3/4: three beats', '3/4: 3박'], line: ['Three beats in every bar: 1 2 3. A dotted minim fills a whole bar.', '마디마다 3박: 1 2 3. 점2분음표 하나가 한 마디를 채워요.'], fig: () => ({ mid: <RqStaff items={RQ_BAR3}/> }) },
    { title: ['4/4: four beats', '4/4: 4박'], line: ['Four beats in every bar. 4/4 is also written C, common time.', '마디마다 4박. 4/4는 C로도 써요.'], fig: () => ({ mid: <RqStaff items={RQ_BAR2}/> }) },
  ],
  make: (n, prev) => { if (n % 2 === 1) return rqStaffQ(kqPick([RQ_BAR3, RQ_BAR24]));
    let top, g = 0; do { top = kqPick([2, 3, 4]); } while (prev && prev.top === top && g++ < 8); const items = top === 2 ? RQ_BAR24 : top === 3 ? RQ_BAR3 : RQ_BAR2;
    return { top, kind: 'choice', cols: 3, prompt: ['How many beats are in each bar?', '한 마디에 몇 박이 들어갈까요?'], opts: ['2', '3', '4'].map(x => ({ id: x, label: x })), ans: String(top), ok: (v) => v === String(top), fig: () => ({ mid: rqStaffEl(items, { counts: false, hearts: false }) }),
      yes: ['The top number says ' + top + '.', '위의 숫자가 ' + top + '예요.'], no: ['Read the top number of the time signature: ' + top + ' beats in a bar.', '박자표의 위 숫자를 읽어요. 한 마디에 ' + top + '박이에요.'] }; },
};
const rqStrong = (top) => plRun(top * 3, { noVoice: true, silentFrom: 0, extra: (ctx, tm, i) => metroClick(ctx, tm, i % top === 0, i % top === 0 ? 0.45 : 0.22) });
const RQ_ST4 = [['ts', 4], ['q'], ['q'], ['q'], ['q'], ['|'], ['q'], ['q'], ['q'], ['q'], ['||']], RQ_ST3 = [['ts', 3], ['q'], ['q'], ['q'], ['|'], ['q'], ['q'], ['q'], ['||']];
RQ_SPEC['rt-strong'] = {
  title: ['Strong and weak beats', '센박과 여린박'], allLine: ['Beat 1 of every bar is the strong beat; the others are weaker. Listen for the stronger click.', '마디마다 1박이 센박이고, 나머지는 여린박이에요. 더 센 클릭을 들어 보세요.'],
  fig: () => ({ mid: <RqStaff items={RQ_ST4} accent/> }),
  steps: [
    { title: ['In 4/4', '4/4에서'], line: ['1 is strong, 3 a little strong, 2 and 4 weak: STRONG weak medium weak.', '1은 세고, 3은 조금 세고, 2와 4는 여려요. 강 약 중강 약.'], fig: () => ({ mid: <RqStaff items={RQ_ST4} accent tap={false}/> }) },
    { title: ['In 3/4', '3/4에서'], line: ['STRONG weak weak, like a waltz.', '강 약 약, 왈츠처럼요.'], fig: () => ({ mid: <RqStaff items={RQ_ST3} accent tap={false}/> }) },
    { title: ['Tap only beat 1', '1박에서만'], line: ['Count every beat, but tap only the strong one.', '박은 모두 세되, 센박에서만 쳐요.'], fig: () => ({ mid: <RqStaff items={RQ_ST4} accent listen={false} only={[0, 4]}/> }) },
  ],
  make: (n, prev) => { if (n % 2 === 0) { const three = Math.random() < 0.5, items = three ? RQ_ST3 : RQ_ST4; return { ...rqStaffQ(items, { only: three ? [0, 3] : [0, 4], accent: true, listen: false, tip: ['Count every beat; tap on 1 only.', '박은 모두 세고, 1에서만 쳐요.'] }), prompt: ['Tap only the strong beat: beat 1 of each bar.', '센박에서만 쳐요. 마디마다 1박.'], yes: ['Beat 1 every time.', '매번 1박이에요.'] }; }
    let top, g = 0; do { top = kqPick([2, 3, 4]); } while (prev && prev.top === top && g++ < 8);
    return { top, kind: 'choice', cols: 3, prompt: ['Listen for the strong beats. How many beats in a bar?', '센박을 들어 보세요. 한 마디에 몇 박일까요?'], opts: ['2', '3', '4'].map(x => ({ id: x, label: x })), ans: String(top), ok: (v) => v === String(top), play: () => rqStrong(top),
      fig: (c) => ({ mid: <PlCircles n={top * 2} r={12} gap={32} group={top} kind={(i) => c.res && i % top === 0 ? 'play' : 'beat'} label={(i) => String(i % top + 1)}/> }),
      yes: ['STRONG and ' + (top - 1) + ' weak: ' + top + ' beats.', '센박 하나와 여린박 ' + (top - 1) + '개: ' + top + '박이에요.'], no: ['Count from one strong click to the next: ' + top + ' beats.', '센 클릭에서 다음 센 클릭까지 세어 보세요. ' + top + '박이에요.'] }; },
};
const RQ_FILL = [[[['ts', 4], ['q'], ['q'], ['box', 2], ['||']], 2], [[['ts', 4], ['h'], ['box', 1], ['q'], ['||']], 1], [[['ts', 3], ['q'], ['box', 2], ['||']], 2], [[['ts', 4], ['box', 3], ['q'], ['||']], 3], [[['ts', 4], ['box', 4], ['||']], 4], [[['ts', 3], ['box', 3], ['||']], 3]];
const RQ_FILLG = { 1: [NV_NOTES[2], ['crotchet', '4분음표']], 2: [NV_NOTES[1], ['minim', '2분음표']], 3: [NV_DOTTED[0], ['dotted minim', '점2분음표']], 4: [NV_NOTES[0], ['semibreve', '온음표']] };
RQ_SPEC['rt-fill'] = {
  title: ['Fill the bar', '마디 채우기'], allLine: ['Every bar must add up to the top number. Count what is there; the missing beats tell you which note fits.', '마디마다 박의 합이 위의 숫자와 같아야 해요. 있는 것을 세면, 모자란 박이 어떤 음표가 들어갈지 알려 줘요.'],
  fig: () => ({ mid: rqStaffEl(RQ_FILL[0][0]) }),
  steps: [
    { title: ['Count what is there', '있는 것 세기'], line: ['4/4: crotchet, crotchet = 2 beats. 2 are missing: a minim.', '4/4: 4분음표, 4분음표 = 2박. 2박이 모자라요: 2분음표.'], fig: () => ({ mid: rqStaffEl(RQ_FILL[0][0]) }) },
    { title: ['3/4', '3/4'], line: ['3/4: a crotchet is 1 beat, so 2 are missing: a minim again.', '3/4: 4분음표가 1박이니 2박이 모자라요. 또 2분음표예요.'], fig: () => ({ mid: rqStaffEl(RQ_FILL[2][0]) }) },
  ],
  make: (n, prev) => { let i, g = 0; do { i = kqRnd(RQ_FILL.length); } while (prev && prev.i === i && g++ < 8); const [items, miss] = RQ_FILL[i], top = srhTop(items), have = top - miss;
    return { i, kind: 'choice', cols: 4, prompt: ['Which note fills the box?', '네모 칸에 들어갈 음표는?'], opts: [1, 2, 3, 4].map(x => ({ id: String(x), label: () => <Glyph item={RQ_FILLG[x][0]} size={50}/> })), ans: String(miss), ok: (v) => v === String(miss),
      fig: (c) => ({ mid: rqStaffEl(c.res ? items.map(x => x[0] === 'box' ? [miss === 1 ? 'q' : miss === 2 ? 'h' : miss === 3 ? 'hd' : 'w'] : x) : items, { counts: c.res ? undefined : false }) }),
      yes: have ? [have + ' + ' + miss + ' = ' + top + ': a ' + RQ_FILLG[miss][1][0] + '.', have + ' + ' + miss + ' = ' + top + ': ' + RQ_FILLG[miss][1][1] + '예요.'] : ['The whole bar, ' + top + ' beats: a ' + RQ_FILLG[miss][1][0] + '.', '한 마디 전체, ' + top + '박: ' + RQ_FILLG[miss][1][1] + '예요.'], no: have ? [top + ' beats in the bar, ' + have + ' there already: ' + miss + ' missing, a ' + RQ_FILLG[miss][1][0] + '.', '한 마디는 ' + top + '박, 이미 ' + have + '박이 있어요. ' + miss + '박이 모자라요: ' + RQ_FILLG[miss][1][1] + '예요.'] : ['The bar is empty: all ' + top + ' beats are missing, a ' + RQ_FILLG[miss][1][0] + '.', '빈 마디예요. ' + top + '박이 모두 모자라요: ' + RQ_FILLG[miss][1][1] + '예요.'] }; },
};
const RQ_TIE = [['ts', 4], ['q'], ['q'], ['h'], ['|'], ['h'], ['h'], ['||']], RQ_TIEB = [['ts', 4], ['h'], ['q'], ['q'], ['|'], ['q'], ['q'], ['h'], ['||']];
RQ_SPEC['rt-tie'] = {
  title: ['The tie', '붙임줄'], allLine: ['A tie joins two notes on the same pitch: play the first, then hold it on through the second. It can carry a note across a bar line.', '붙임줄은 같은 높이의 두 음을 이어요. 첫 음만 치고 둘째 음까지 계속 누르고 있어요. 세로줄을 넘어 이어질 수도 있어요.'],
  fig: () => ({ mid: <RqStaff items={RQ_TIE} ties={[[3, 5]]}/> }),
  steps: [
    { title: ['Without the tie', '붙임줄 없이'], line: ['A minim at the end of bar 1, another at the start of bar 2: two sounds.', '1마디 끝의 2분음표, 2마디 처음의 2분음표: 소리 둘.'], fig: () => ({ mid: <RqStaff items={RQ_TIE} tap={false}/> }) },
    { title: ['With the tie', '붙임줄이 있으면'], line: ['Tied: one sound, held for 2 + 2 = 4 beats, right across the bar line.', '이어지면 소리는 하나, 2 + 2 = 4박 동안 세로줄을 넘어 누르고 있어요.'], fig: () => ({ mid: <RqStaff items={RQ_TIE} ties={[[3, 5]]}/> }) },
  ],
  make: (n) => { if (n % 2 === 0) { const b = n % 4 === 0, items = b ? RQ_TIE : RQ_TIEB, ties = b ? [[3, 5]] : [[3, 5]]; return rqStaffQ(items, { ties, tip: ['Do not play the tied note again: hold on.', '이어진 음은 다시 치지 말고 계속 눌러요.'] }); }
    const opts = [[[['ts', 4], ['h'], ['h'], ['||']], 4, 'h + h'], [[['ts', 4], ['q'], ['q'], ['q'], ['q'], ['||']], 2, 'q + q'], [[['ts', 4], ['h'], ['q'], ['q'], ['||']], 3, 'h + q']], [items, ans] = kqPick(opts), ties = [[1, 2]];
    return { kind: 'choice', cols: 4, prompt: ['How many beats does the first tied note last?', '붙임줄로 이어진 첫 음은 몇 박 동안 울릴까요?'], opts: ['1', '2', '3', '4'].map(x => ({ id: x, label: x })), ans: String(ans), ok: (v) => v === String(ans), fig: () => ({ mid: rqStaffEl(items, { ties, counts: false }) }),
      yes: ['The two lengths add up: ' + ans + ' beats.', '두 길이를 더해요. ' + ans + '박이에요.'], no: ['Add the two tied notes together: ' + ans + ' beats, one sound.', '이어진 두 음의 길이를 더해요. ' + ans + '박, 소리는 하나예요.'] }; },
};

// ══ 4. Rhythm patterns ══
const rqLesson = (o) => ({ title: o.title, allLine: o.allLine, fig: () => ({ mid: <RqStaff items={SRH_ROWS[o.rows[0]]} from={SRH_FROM[o.rows[0]]}/> }),
  steps: o.steps.map(s => ({ title: s[0], line: s[1], fig: () => ({ mid: <RqStaff items={SRH_ROWS[s[2]]} from={SRH_FROM[s[2]]} tap={s[3] !== false}/> }) })),
  make: (n, prev) => { const k = n % 3; let i, g = 0; do { i = kqRnd(o.rows.length); } while (prev && prev.i === i && o.rows.length > 1 && g++ < 8); const key = o.rows[i];
    if (k === 0) return { i, ...rqStaffQ(SRH_ROWS[key], { from: SRH_FROM[key] }) };
    if (k === 1) return { i, ...o.ask(n) };
    const pool = o.hear.map(x => ({ items: SRH_ROWS[x], from: SRH_FROM[x] })), j = kqRnd(pool.length); return { i, ...rqHearS(pool, j) }; } });
RQ_SPEC['rp-beams'] = rqLesson({ title: ['Grouping quavers', '8분음표 묶기'], allLine: ['Quavers are joined by beams, one beat at a time (or two beats in 4/4), so you can see where each beat starts.', '8분음표는 빔으로 묶어요. 한 박씩 (4/4에서는 두 박씩도) 묶어서 박이 어디서 시작하는지 보이게 해요.'],
  rows: ['pairs', 'four', 'right'], hear: ['pairs', 'four', 'right'],
  steps: [[['Two on a beat', '한 박에 둘'], ['Two quavers, one beam, one beat: 1 +.', '8분음표 둘, 빔 하나, 1박: 1 +.'], 'pairs'], [['Four on two beats', '두 박에 넷'], ['In 4/4, four quavers can share a beam: half a bar, 1 + 2 +.', '4/4에서는 8분음표 넷을 한 빔으로 묶을 수 있어요. 반 마디, 1 + 2 +.'], 'four'], [['Never across the middle', '가운데를 넘지 않아요'], ['A beam never hides beat 3 of a 4/4 bar: the middle of the bar stays visible.', '4/4 마디에서 빔이 3박을 가리면 안 돼요. 마디의 가운데가 보여야 해요.'], 'right', false]],
  ask: () => { const good = Math.random() < 0.5, key = good ? 'right' : 'wrong'; return { kind: 'choice', cols: 2, prompt: ['Is this bar beamed right?', '이 마디는 바르게 묶였을까요?'], opts: [{ id: 'y', label: () => t('Yes', '네') }, { id: 'n', label: () => t('No', '아니요') }], ans: good ? 'y' : 'n', ok: (v) => v === (good ? 'y' : 'n'),
    fig: () => ({ mid: rqStaffEl(SRH_ROWS[key]) }), yes: good ? ['Right: each beam starts on a beat and beat 3 is clear.', '맞아요. 빔마다 박에서 시작하고 3박이 잘 보여요.'] : ['Not right: that beam runs across beat 3.', '바르지 않아요. 그 빔이 3박을 넘어가요.'], no: good ? ['It is right: the beams start on beats 2 and 3, and beat 3 is clear.', '바르게 묶였어요. 빔이 2박과 3박에서 시작하고, 3박이 잘 보여요.'] : ['The four quavers start on beat 2 and run across beat 3: beam them in twos.', '8분음표 넷이 2박에서 시작해 3박을 넘어가요. 둘씩 묶어야 해요.'] }; } });
RQ_SPEC['rp-alone'] = rqLesson({ title: ['A quaver alone', '혼자 있는 8분음표'], allLine: ['A quaver on its own has a flag. A quaver rest is half a beat of silence: rest on the beat, play on the +.', '혼자 있는 8분음표에는 꼬리가 있어요. 8분쉼표는 반 박의 침묵이에요. 박에서 쉬고, + 에서 쳐요.'],
  rows: ['alone', 'aloneB'], hear: ['alone', 'aloneB', 'pairs'],
  steps: [[['The quaver rest', '8분쉼표'], ['In this bar the rest takes the first half of beat 2, and the quaver sounds on its +. The same again on beat 4.', '이 마디에서는 쉼표가 2박의 앞 절반을 차지하고, 8분음표가 2박의 + 에서 소리 나요. 4박에서도 똑같아요.'], 'alone', false], [['A quaver, then a rest', '8분음표, 그다음 쉼표'], ['In 2/4: a quaver on 1, a rest on the +, then a crotchet on 2.', '2/4: 1에 8분음표, + 에 쉼표, 그다음 2에 4분음표.'], 'aloneB']],
  ask: () => ({ kind: 'choice', cols: 4, prompt: ['On which count does the first single quaver sound?', '첫 번째로 혼자 있는 8분음표는 어느 셈에서 소리 날까요?'], opts: ['2', '2 +', '3', '3 +'].map(x => ({ id: x, label: x })), ans: '2 +', ok: (v) => v === '2 +', fig: (c) => ({ mid: rqStaffEl(SRH_ROWS.alone, { counts: c.res ? undefined : false }) }),
    yes: ['On 2 +: the rest takes the first half of beat 2.', '2 + 에서요. 쉼표가 2박의 앞 절반을 차지해요.'], no: ['The rest takes the first half of beat 2, so the quaver comes on 2 +.', '쉼표가 2박의 앞 절반을 차지하니까, 8분음표는 2 + 에서 와요.'] }) });
RQ_SPEC['rp-dot'] = rqLesson({ title: ['The dotted crotchet', '점4분음표'], allLine: ['A dot adds half again: a dotted crotchet lasts 1½ beats. With a quaver after it: long, short, 1 (2) +.', '점은 원래 길이의 반을 더해요. 점4분음표는 1½박이에요. 뒤에 8분음표가 오면 길게, 짧게: 1 (2) +.'],
  rows: ['dot', 'dotB', 'dot3'], hear: ['dot', 'dotB', 'dot3'],
  steps: [[['Long, short', '길게, 짧게'], ['The dotted crotchet holds through beat 2; the quaver sounds on the + of 2.', '점4분음표는 2박까지 이어지고, 8분음표는 2박의 + 에서 소리 나요.'], 'dot', false], [['Tap it', '쳐 보기'], ['Hold the long one, then a quick short one.', '긴 음은 누르고 있다가, 짧은 음을 빠르게.'], 'dot']],
  ask: () => ({ kind: 'choice', cols: 4, prompt: ['How many beats does a dotted crotchet last?', '점4분음표는 몇 박일까요?'], opts: ['1', '1½', '2', '3'].map(x => ({ id: x, label: x })), ans: '1½', ok: (v) => v === '1½', fig: () => ({ mid: <div style={{ display: 'flex', justifyContent: 'center', margin: '4px 0 8px' }}><Glyph item={NV_DOTTED[1]} size={90}/></div> }),
    yes: ['1 + ½ = 1½ beats.', '1 + ½ = 1½박이에요.'], no: ['A crotchet is 1 beat; the dot adds half of it: 1½.', '4분음표는 1박, 점이 그 반을 더해요. 1½박이에요.'] }) });
RQ_SPEC['rp-up'] = rqLesson({ title: ['Before beat 1', '못갖춘마디'], allLine: ['Some tunes start before beat 1: an anacrusis. Count the missing beats first, then come in. The last bar is often short too.', '첫 박보다 먼저 시작하는 곡이 있어요. 못갖춘마디예요. 빠진 박을 먼저 세고 들어와요. 마지막 마디도 짧은 경우가 많아요.'],
  rows: ['up4', 'up3'], hear: ['up4', 'up3', 'upP'],
  steps: [[['Start on beat 4', '4박에서 시작'], ['4/4: count 1 2 3, then play on 4. The next bar starts on 1.', '4/4: 1 2 3을 세고 4에서 쳐요. 다음 마디가 1에서 시작해요.'], 'up4'], [['In 3/4', '3/4에서'], ['Count 1 2, play on 3. The last bar has only two beats: together with the start, they make a full bar.', '1 2를 세고 3에서 쳐요. 마지막 마디는 2박뿐이에요. 처음과 합치면 한 마디가 돼요.'], 'up3']],
  ask: () => { const key = kqPick(['up4', 'up3']), b = key === 'up4' ? '4' : '3'; return { kind: 'choice', cols: 4, prompt: ['On which beat does this tune start?', '이 곡은 몇 박에서 시작할까요?'], opts: ['1', '2', '3', '4'].map(x => ({ id: x, label: x })), ans: b, ok: (v) => v === b, fig: () => ({ mid: rqStaffEl(SRH_ROWS[key], { from: SRH_FROM[key] }) }),
    yes: ['On beat ' + b + ': the beats before it are counted, not played.', b + '박에서요. 그 앞의 박은 세기만 하고 치지 않아요.'], no: ['Only one beat comes before the first bar line, so it is the last beat: ' + b + '.', '첫 세로줄 앞에 박이 하나뿐이니까 마지막 박, ' + b + '박이에요.'] }; } });
RQ_SPEC['rp-read'] = rqLesson({ title: ['Count, clap, play', '세고, 손뼉 치고, 치기'], allLine: ['A new line: find the count of every note first, say it out loud, then clap it, then play it.', '새로운 줄: 먼저 음표마다 셈을 찾고, 소리 내어 말하고, 손뼉 치고, 그다음 쳐요.'],
  rows: ['mix4', 'mix2', 'mix3'], hear: ['mix4', 'mix2', 'mix3'],
  steps: [[['Find the count', '셈 찾기'], ['The counts under the notes: 1, 2 +, 3 +, 4 and so on.', '음표 아래의 셈: 1, 2 +, 3 +, 4, 이렇게요.'], 'mix4', false], [['Clap, then tap', '손뼉, 그다음 치기'], ['Clap it once while counting, then tap it.', '세면서 한 번 손뼉 치고, 그다음 쳐요.'], 'mix2']],
  ask: () => { const pool = ['mix4', 'mix2', 'mix3'].map(x => ({ items: SRH_ROWS[x], from: SRH_FROM[x] })); return rqHearS(pool, kqRnd(3)); } });

const RQ_ROWS2 = [
  ['rt-bars', 'Bars and bar lines', '마디와 세로줄', 'Bar lines cut the music into bars.', '세로줄이 음악을 마디로 나눠요.'],
  ['rt-ts', 'The two numbers', '박자표의 두 숫자', '2/4, 3/4, 4/4: beats in a bar, and the crotchet beat.', '2/4, 3/4, 4/4: 마디의 박 수와 4분음표 박.'],
  ['rt-strong', 'Strong and weak beats', '센박과 여린박', 'Beat 1 is strong.', '1박이 센박.'],
  ['rt-fill', 'Fill the bar', '마디 채우기', 'The beats must add up to the top number.', '박의 합이 위의 숫자와 같아야 해요.'],
  ['rt-tie', 'The tie', '붙임줄', 'One sound across two notes.', '두 음표에 걸친 소리 하나.'],
  ['rp-beams', 'Grouping quavers', '8분음표 묶기', 'Beams show where the beats are.', '빔이 박의 자리를 보여 줘요.'],
  ['rp-alone', 'A quaver alone', '혼자 있는 8분음표', 'Rest on 1, play on +.', '1에서 쉬고, + 에서 치기.'],
  ['rp-dot', 'The dotted crotchet', '점4분음표', 'Long, short: 1 (2) +.', '길게, 짧게: 1 (2) +.'],
  ['rp-up', 'Before beat 1', '못갖춘마디', 'Count the missing beats, then come in.', '빠진 박을 세고 들어오기.'],
  ['rp-read', 'Count, clap, play', '세고, 손뼉 치고, 치기', 'A new line, step by step.', '새로운 줄을 차근차근.'],
];
RQ_ROWS2.forEach(([id, en, ko, benEn, bko]) => {
  TOOLS.push({ id, ch: 'concept', title: en, blurb: benEn, hidden: true, get kicker() { return TOOL_AREAS.find(a => a.id === 'rhythm').name + ' · ' + homeCatById('r-beat').name; }, C: () => <KqEngine spec={RQ_SPEC[id]}/> });
  TOOL_KO[id] = [ko, bko];
  const tl = TOOLS[TOOLS.length - 1], k = TOOL_KO[id], ti = tl.title, bl = tl.blurb; tl.titleEn = ti; tl.blurbEn = bl;
  Object.defineProperty(tl, 'title', { get: () => (LANG === 'ko' ? k[0] : ti), enumerable: true, configurable: true });
  Object.defineProperty(tl, 'blurb', { get: () => (LANG === 'ko' ? k[1] : bl), enumerable: true, configurable: true });
  TOOL_CONCEPT[id] = 'r-beat';
});
