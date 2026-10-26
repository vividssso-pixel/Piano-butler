import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build AM (board call 14, the fourth Grades 2-3 room): Rhythm Further. Theory of Music Grades 2 and 3, Time and Rhythm (Manual
# of Syllabuses 2026, page 66, read from the page image 26 Oct): Grade 2 adds, in simple time, the triplet quavers, the dotted
# crotchet and quaver, four quavers and four semiquavers beamed, the quaver rest; in compound time (6/8) three quavers, crotchet and
# quaver, the dotted crotchet and dotted minim, the quaver rest; a quaver anacrusis; the whole-bar rest. Grade 3 adds the quaver and
# two semiquavers, two semiquavers and a quaver, the dotted quaver and semiquaver (alone and before a quaver), the duplet, the single
# semiquaver, the dotted crotchet, dotted quaver and semiquaver rests, and the time signatures 3/2, 2/2, cut common time, 3/8 and 9/8.
# The rhythm engine learns five beamed groups with parts of different lengths (SRH_PARTS) and the cut-time sign.

# ── the engine: groups whose notes are not all the same length ──
rep("""const SRH_LEN = { q: 1, h: 2, hd: 3, w: 4, qd: 1.5, e: 0.5, er: 0.5, p: 1, p4: 2, s4: 1, r: 1, hr: 2, t3: 1, e3: 1.5 };""",
    """const SRH_LEN = { q: 1, h: 2, hd: 3, w: 4, qd: 1.5, e: 0.5, er: 0.5, p: 1, p4: 2, s4: 1, r: 1, hr: 2, t3: 1, e3: 1.5, es: 1, se: 1, ds: 1, du: 1.5, dse: 1.5, sr: 0.25, qdr: 1.5 };   // Build AM: es se ds du dse, and two rests""")
rep("""const SRH_HEADS = { p: 2, p4: 4, s4: 4, t3: 3, e3: 3 };   // notes joined by a beam
const srhRest = (k) => k === 'r' || k === 'hr' || k === 'er';""",
    """const SRH_HEADS = { p: 2, p4: 4, s4: 4, t3: 3, e3: 3, es: 3, se: 3, ds: 2, du: 2, dse: 3 };   // notes joined by a beam
// Build AM: a group whose notes are not all one length: each note's share of the group (in beats)
const SRH_PARTS = { es: [0.5, 0.25, 0.25], se: [0.25, 0.25, 0.5], ds: [0.75, 0.25], du: [0.75, 0.75], dse: [0.75, 0.25, 0.5] };
const srhRest = (k) => k === 'r' || k === 'hr' || k === 'er' || k === 'sr' || k === 'qdr';""")
rep("""    const k = it[0], n = SRH_HEADS[k] || 1, d = srhLen(it) / n;
    if (k !== 'box') for (let h = 0; h < n; h++) out.push({ b: b + h * d, d, j, h, rest: srhRest(k) });""",
    """    const k = it[0], n = SRH_HEADS[k] || 1, d = srhLen(it) / n, P = SRH_PARTS[k];
    if (P) { let o = 0; P.forEach((pd, h) => { out.push({ b: b + o, d: pd, j, h, rest: false }); o += pd; }); }
    else if (k !== 'box') for (let h = 0; h < n; h++) out.push({ b: b + h * d, d, j, h, rest: srhRest(k) });""")
rep("""    mine.forEach(([s, i]) => { soundX[i] = nx + s.h * step; });""", """    mine.forEach(([s, i]) => { soundX[i] = k === 'du' || k === 'dse' ? nx + (s.b - b) / len * (w - 12) : nx + s.h * step; });   // Build AM: a compound group's notes sit where they sound (its held counts fall between)""")
rep("""const srhW = (k, len, D, wide) => k === 't3' ? Math.max(D, 80)""", """const srhW = (k, len, D, wide) => SRH_PARTS[k] ? Math.max(len * D, k === 'ds' ? 66 : k === 'du' ? 96 : k === 'dse' ? 120 : 92) : k === 'sr' ? Math.max(len * D, 30) : k === 'qdr' ? Math.max(len * D, 44) : k === 't3' ? Math.max(D, 80)""")
rep("""    else if (SRH_HEADS[k]) { out.push(srhGroup(mine.map(([, i]) => soundX[i]), y, mine.map(([s]) => c(s.h)), k === 's4' ? 2 : 1, o.hl === j ? cor : col));""",
    """    else if (SRH_PARTS[k]) out.push(srhGroupParts(mine.map(([, i]) => soundX[i]), y, mine.map(([s]) => c(s.h)), SRH_PARTS[k], o.hl === j ? cor : col, G, k === 'du' ? '2' : null));
    else if (k === 'sr') out.push(srhSemiRest(nx + 2, G(34), c(0)));
    else if (k === 'qdr') out.push(nvbRest(nx + 2, G(34), 'q', { k: 0.82, col: c(0) }).svg + '<circle cx="' + pFix(nx + 12) + '" cy="' + pFix(G(33)) + '" r="2.6" fill="' + c(0) + '"/>');
    else if (SRH_HEADS[k]) { out.push(srhGroup(mine.map(([, i]) => soundX[i]), y, mine.map(([s]) => c(s.h)), k === 's4' ? 2 : 1, o.hl === j ? cor : col));""")
rep("""    if (k === 'ts') { [[it[1], G(36)], [it[2] || 4, G(32)]].forEach(""",
    """    if (k === 'ts' && it[1] === '¢') { out.push('<text x="' + pFix(x + 10) + '" y="' + pFix(G(34) + 10) + '" text-anchor="middle" font-family="Playfair Display, Georgia, serif" font-size="30" font-weight="900" fill="' + col + '">C</text><line x1="' + pFix(x + 11) + '" x2="' + pFix(x + 11) + '" y1="' + pFix(G(38) - 6) + '" y2="' + pFix(G(30) + 6) + '" stroke="' + col + '" stroke-width="2.2"/>'); x += 28; return; }
    if (k === 'ts') { [[it[1], G(36)], [it[2] || 4, G(32)]].forEach(""")
rep("""// heads with stems up joined by one beam (quavers) or two (semiquavers); cols: each note's colour
function srhGroup(""", """// Build AM: a semiquaver rest: two blobs on one stroke
const srhSemiRest = (x, y, col) => srhQuaverRest(x, y, col) + '<circle cx="' + pFix(x - 4.6) + '" cy="' + pFix(y + 1.2) + '" r="3" fill="' + col + '"/>';
// Build AM: a beamed group of mixed lengths (parts in beats): the main beam over all; a second beam over the semiquavers that
// sit side by side, a short stub for a semiquaver alone (pointing to its dotted neighbour); a dot after each dotted quaver;
// label: the duplet's 2 over the beam
function srhGroupParts(xs, y, cols, parts, ink, G, label) {
  let s = srhGroup(xs, y, cols, 1, ink); const top = y - 34;
  parts.forEach((pd, i) => {
    if (pd === 0.75 && parts.length > 1 && !label) s += '<circle cx="' + pFix(xs[i] + 13) + '" cy="' + pFix(G(33)) + '" r="2.6" fill="' + cols[i] + '"/>';
    if (pd !== 0.25) return;
    if (parts[i + 1] === 0.25) s += '<rect x="' + pFix(xs[i] + 5.5) + '" y="' + pFix(top + 7.8) + '" width="' + pFix(xs[i + 1] - xs[i] + 1.8) + '" height="5.2" fill="' + ink + '"/>';
    else if (parts[i - 1] !== 0.25) { const left = i > 0, x1 = left ? xs[i] + 7.3 - 11 : xs[i] + 5.5; s += '<rect x="' + pFix(x1) + '" y="' + pFix(top + 7.8) + '" width="11" height="5.2" fill="' + ink + '"/>'; }
  });
  if (label) s += '<text x="' + pFix((xs[0] + xs[xs.length - 1]) / 2 + 6.4) + '" y="' + pFix(y - 36.5) + '" text-anchor="middle" font-family="Playfair Display, Georgia, serif" font-style="italic" font-size="13" font-weight="900" fill="' + ink + '">' + label + '</text>';
  return s;
}
// heads with stems up joined by one beam (quavers) or two (semiquavers); cols: each note's colour
function srhGroup(""")

# ── registration ──
rep("""const HARMONY_23_DRILL = { id: 'harmony-23', label: 'Intervals and Chords Further' };   // Build AL: Grades 2-3 theory""",
    """const HARMONY_23_DRILL = { id: 'harmony-23', label: 'Intervals and Chords Further' };   // Build AL: Grades 2-3 theory
const RHYTHM_23_DRILL = { id: 'rhythm-23', label: 'Rhythm Further' };   // Build AM: Grades 2-3 time and rhythm""")
rep("""  { id: 'harmony-23', label: 'Intervals and Chords Further', concept: HARMONY_23_DRILL, track: 'start' },   // Build AL""",
    """  { id: 'harmony-23', label: 'Intervals and Chords Further', concept: HARMONY_23_DRILL, track: 'start' },   // Build AL
  { id: 'rhythm-23', label: 'Rhythm Further', concept: RHYTHM_23_DRILL, track: 'start' },   // Build AM""")
rep("""'harmony-23': '음정과 화음 한 걸음 더'""", """'harmony-23': '음정과 화음 한 걸음 더', 'rhythm-23': '리듬 한 걸음 더'""")
rep("""'harmony-23': ['intervals', 'chords']""", """'harmony-23': ['intervals', 'chords'], 'rhythm-23': ['rhythm', 'six-eight']""")
rep("""'harmony-23': ['Chords further', '화음 더']""", """'harmony-23': ['Chords further', '화음 더'], 'rhythm-23': ['Rhythm further', '리듬 더']""")
rep("""  'harmony-23': 'intervals chords grade 2 grade 3""", """  'rhythm-23': 'rhythm grade 2 grade 3 semiquavers dotted quaver triplet duplet minim beat 2/2 3/2 cut common time 3/8 9/8 compound triple anacrusis rests time signatures',
  'harmony-23': 'intervals chords grade 2 grade 3""")
rep("""'harmony-23': 'p-chords', 'key-signatures': 'p-scales',""", """'harmony-23': 'p-chords', 'rhythm-23': 'r-beat', 'key-signatures': 'p-scales',""")
rep("""  { ids: ['melody', 'listen-23', 'scales-23', 'harmony-23', 'more-scales'], en: ['Grades 2–3', 'How a tune is shaped, your ears, scales, intervals and chords a step further.'], ko: ['Grade 2–3', '선율의 모양, 그리고 귀, 스케일, 음정과 화음을 한 걸음 더.'] },""",
    """  { ids: ['melody', 'listen-23', 'scales-23', 'harmony-23', 'rhythm-23', 'more-scales'], en: ['Grades 2–3', 'How a tune is shaped; your ears, scales, intervals and chords, and rhythm a step further.'], ko: ['Grade 2–3', '선율의 모양, 그리고 귀, 스케일, 음정과 화음, 리듬을 한 걸음 더.'] },   // Build AM: Rhythm Further""")
rep("""    { id: 'rb-68', en: '6/8 time', ko: '6/8박자', lessons: ['e8-big', 'e8-dot', 'e8-ls', 'e8-34', 'e8-read'], check: 'six-eight' },   // Build AD""",
    """    { id: 'rb-68', en: '6/8 time', ko: '6/8박자', lessons: ['e8-big', 'e8-dot', 'e8-ls', 'e8-34', 'e8-read'], check: 'six-eight' },   // Build AD
    { id: 'rb-23', en: 'Rhythm further', ko: '리듬 한 걸음 더', lessons: ['r2-semi', 'r2-dot', 'r2-trip', 'r2-minim', 'r2-98'], check: 'rhythm-23' },   // Build AM""")
rep("""  set('23', 'h3-iv h3-deg h3-inv h3-satb h3-cad');""", """  set('23', 'h3-iv h3-deg h3-inv h3-satb h3-cad');
  set('23', 'r2-semi r2-dot r2-trip r2-minim r2-98');   // Build AM: Rhythm Further""")

CH = r'''
// ─── Chapter: Rhythm Further (Build AM, 2026-10-26; board call 14, the fourth Grades 2-3 room) ───
// Theory of Music Grades 2 and 3, Time and Rhythm, step by step: semiquavers (four on a beat at Grade 2; with a quaver at Grade 3);
// the dotted quaver and semiquaver (Grade 3); three in a beat and two in a dotted beat (the triplet, Grade 2; the duplet, Grade 3);
// the minim beat: 2/2, cut common time and 3/2 (Grade 3); three and nine quavers: 3/8 and 9/8 (Grade 3). Counting: 1 e + a, as the
// app counts semiquavers elsewhere; in compound time every quaver, as in the 6/8 room.
const r2Cmp = (top) => (pos) => { const q = pos / 0.5, r = Math.round(q); return Math.abs(q - r) < 1e-6 ? String(r % top + 1) : '+'; };
const R2 = {
  semiA: { items: [['ts', 4], ['q'], ['s4'], ['p'], ['q'], ['||']], g: 2 },
  semiB: { items: [['ts', 4], ['es'], ['se'], ['es'], ['q'], ['||']], g: 3 },
  semiC: { items: [['ts', 2], ['se'], ['q'], ['|'], ['es'], ['s4'], ['|'], ['h'], ['||']], g: 3 },
  dotA: { items: [['ts', 4], ['ds'], ['ds'], ['q'], ['q'], ['||']], g: 3 },
  dotB: { items: [['ts', 3], ['q'], ['ds'], ['q'], ['|'], ['ds'], ['ds'], ['q'], ['|'], ['hd'], ['||']], g: 3 },
  tripA: { items: [['ts', 2], ['t3'], ['q'], ['|'], ['t3'], ['t3'], ['|'], ['p'], ['t3'], ['|'], ['h'], ['||']], g: 2, so: { countFn: (p) => rqTripCount(p) } },
  duA: { items: [['ts', 6, 8], ['du'], ['e3'], ['|'], ['qd'], ['du'], ['|'], ['dse'], ['qd'], ['||']], g: 3, unit: 0.5, clicks: 6, accentAt: [0, 3], bpm: 54, so: { D: 48, countStep: 0.5, heartStep: 1.5, countFn: r2Cmp(6) } },
  minA: { items: [['ts', 2, 2], ['h'], ['q'], ['q'], ['|'], ['w'], ['||']], g: 3, unit: 2, clicks: 2, bpm: 96, so: { countStep: 1, heartStep: 2, countFn: (p) => rq22Count(p) } },
  minB: { items: [['ts', 3, 2], ['h'], ['h'], ['h'], ['|'], ['w'], ['h'], ['||']], g: 3, unit: 2, clicks: 3, bpm: 96, so: { countStep: 1, heartStep: 2, countFn: (p) => rq22Count(p) } },
  minC: { items: [['ts', '¢'], ['q'], ['q'], ['h'], ['|'], ['h'], ['h'], ['||']], g: 3, unit: 2, clicks: 2, bpm: 96, so: { countStep: 1, heartStep: 2, countFn: (p) => rq22Count(p) } },
  e38: { items: [['ts', 3, 8], ['e'], ['e'], ['e'], ['|'], ['q'], ['e'], ['|'], ['qd'], ['||']], g: 3, unit: 0.5, clicks: 3, accentAt: [0], bpm: 72, so: { countStep: 0.5, heartStep: 0.5, countFn: r2Cmp(3) } },
  e98: { items: [['ts', 9, 8], ['e3'], ['e3'], ['e3'], ['|'], ['qd'], ['q'], ['e'], ['qd'], ['||']], g: 3, unit: 0.5, clicks: 9, accentAt: [0, 3, 6], bpm: 60, so: { D: 44, countStep: 0.5, heartStep: 1.5, countFn: r2Cmp(9) } },
};
const r2Props = (key, extra = {}) => { const R = R2[key]; return { items: R.items, unit: R.unit, clicks: R.clicks, accentAt: R.accentAt, accent: !!R.accentAt, bpm: R.bpm, so: R.so, ...extra }; };
const r2El = (key, o = {}) => rqStaffEl(R2[key].items, { ...(R2[key].so || {}), ...o });
const r2Play = (key, o = {}) => { const R = R2[key]; return rqRunS(R.items, { unit: R.unit, clicks: R.clicks, accentAt: R.accentAt, accent: !!R.accentAt, bpm: R.bpm, ...o }); };
const r2GLab = (g) => <span style={{fontSize:11,fontWeight:900,color:BK.muted,letterSpacing:'0.06em'}}>{'GRADE ' + g}</span>;
// one pad for every step: the lines to choose from, the line on the staff with its counts, listen and tap (RqStaff), and one question
function R2Pad({ step, keys, title, note, ask }) {
  const [k, setK] = useState(keys[0]), [q, setQ] = useState(null), [pick, setPick] = useState(null);
  const say = (id) => { if (pick != null) return; setPick(id); };
  return (
    <div className="try-box" style={actBox} data-r2={step}>
      <div style={actTitle}>{title}</div>
      <div style={actNote}>{note}</div>
      {keys.length > 1 && spChips(keys.map((x, j) => [x, t('Line ' + (j + 1), (j + 1) + '번 줄')]), k, (x) => { setK(x); setQ(null); setPick(null); })}
      <div style={{textAlign:'center',margin:'0 0 2px'}}>{r2GLab(R2[k].g)}</div>
      <RqStaff key={k} {...r2Props(k)}/>
      {ask && !q && <div style={{textAlign:'center',marginTop:8}}><button className="ghost-btn" style={spBtn} onClick={() => { setQ(ask(k)); setPick(null); }}>{t('▶ A question', '▶ 질문 하나')}</button></div>}
      {q && <><div style={{textAlign:'center',fontSize:15,fontWeight:800,color:BK.ink,margin:'10px 0 0'}}>{t(q.prompt[0], q.prompt[1])}</div>
        <div style={{display:'grid',gridTemplateColumns:'repeat(' + (q.cols || q.opts.length) + ',minmax(0,1fr))',gap:8,marginTop:8}}>{q.opts.map(([id, lab]) => <button key={id} className={'choice-btn' + (pick == null ? '' : id === q.ans ? ' good' : id === pick ? ' bad' : '')} onClick={() => say(id)} style={{padding:'11px 4px',fontSize:15,fontWeight:900}}>{lab}</button>)}</div>
        {pick != null && spMsg(pick === q.ans ? t(q.yes[0], q.yes[1]) : t(q.no[0], q.no[1]), pick === q.ans ? BK.green : BK.coral)}
        {pick != null && <div style={{textAlign:'center',marginTop:6}}><button className="ghost-btn" style={spBtn} onClick={() => { setQ(ask(k)); setPick(null); }}>{t('▶ Another', '▶ 다른 것')}</button></div>}</>}
    </div>
  );
}
// the questions (also the drill's and the Home's)
const R2_Q = {
  semi: () => { const v = Math.floor(Math.random() * 3); return [
    { prompt: ['How many semiquavers make one crotchet beat?', '16분음표 몇 개가 4분음표 한 박이 될까요?'], opts: [['2', '2'], ['3', '3'], ['4', '4']], ans: '4', yes: ['Four: 1 e + a.', '넷: 1 e + a.'], no: ['A quaver is two semiquavers, and two quavers make a beat: four.', '8분음표 하나가 16분음표 둘, 8분음표 둘이 한 박: 넷.'] },
    { prompt: ['A quaver and two semiquavers: what is it worth?', '8분음표 하나와 16분음표 둘: 몇 박일까요?'], opts: [['half', t('half a beat', '반 박')], ['one', t('one beat', '한 박')], ['two', t('two beats', '두 박')]], ans: 'one', yes: ['One beat, counted 1 + a: half a beat, then two quarters.', '한 박, 1 + a로 세요: 반 박, 그다음 4분의 1 박 둘.'], no: ['Half a beat and two quarters: one beat, counted 1 + a.', '반 박과 4분의 1 박 둘: 한 박, 1 + a로 세요.'] },
    { prompt: ['Two semiquavers and a quaver: how is it counted?', '16분음표 둘과 8분음표 하나: 어떻게 셀까요?'], opts: [['1e+', '1 e +'], ['1+a', '1 + a'], ['1ea', '1 e a']], ans: '1e+', yes: ['1 e +: two quick, then a quaver on the +.', '1 e +: 빠르게 둘, 그다음 + 에 8분음표.'], no: ['The two semiquavers take 1 and e; the quaver starts on the +: 1 e +.', '16분음표 둘이 1과 e, 8분음표는 + 에서: 1 e +.'] }][v]; },
  dot: () => { const v = Math.floor(Math.random() * 2); return [
    { prompt: ['A dotted quaver is worth how many semiquavers?', '점8분음표는 16분음표 몇 개일까요?'], opts: [['2', '2'], ['3', '3'], ['4', '4']], ans: '3', yes: ['Three: a quaver (two) and its dot (one more).', '셋: 8분음표(둘)와 점(하나 더).'], no: ['A quaver is two semiquavers; the dot adds half again: three.', '8분음표는 16분음표 둘, 점이 반을 더해요: 셋.'] },
    { prompt: ['Dotted quaver and semiquaver: on which count does the semiquaver fall?', '점8분음표와 16분음표: 16분음표는 어느 셈에?'], opts: [['e', 'e'], ['+', '+'], ['a', 'a']], ans: 'a', yes: ['On a: long, then short, just before the next beat.', 'a 에서: 길게, 그다음 다음 박 바로 앞에 짧게.'], no: ['The dotted quaver lasts 1 e +, so the semiquaver comes on a.', '점8분음표가 1 e + 동안 이어지니까, 16분음표는 a 에서.'] }][v]; },
  trip: () => { const v = Math.floor(Math.random() * 2); return [
    { prompt: ['A triplet fits how many quavers into one crotchet beat?', '셋잇단음표는 4분음표 한 박에 8분음표 몇 개?'], opts: [['2', '2'], ['3', '3'], ['4', '4']], ans: '3', yes: ['Three, where two would normally go: 1 trip let.', '보통 둘 자리에 셋: 1 trip let.'], no: ['The 3 over the beam: three in the time of two.', '빔 위의 3: 둘의 시간에 셋.'] },
    { prompt: ['In 6/8, a duplet fits how many notes into a dotted crotchet beat?', '6/8에서 2잇단음표는 점4분음표 한 박에 몇 개?'], opts: [['2', '2'], ['3', '3'], ['4', '4']], ans: '2', yes: ['Two, where three quavers would normally go.', '보통 8분음표 셋 자리에 둘.'], no: ['The 2 over the beam: two in the time of three.', '빔 위의 2: 셋의 시간에 둘.'] }][v]; },
  minim: () => { const v = Math.floor(Math.random() * 2); return [
    { prompt: ['In 3/2, how many minim beats are in a bar?', '3/2에서 한 마디에 2분음표 박이 몇 개?'], opts: [['2', '2'], ['3', '3'], ['4', '4']], ans: '3', yes: ['Three: the top number. The bottom 2 means minims.', '셋: 위의 숫자. 아래의 2는 2분음표.'], no: ['Top number 3, bottom number 2 (minims): three minim beats.', '위의 3, 아래의 2(2분음표): 2분음표 세 박.'] },
    { prompt: ['Cut common time (C with a line) is the same as…', '세로선이 그어진 C는 어느 박자와 같을까요?'], opts: [['44', '4/4'], ['22', '2/2'], ['32', '3/2']], ans: '22', yes: ['2/2: two minim beats in a bar.', '2/2: 한 마디에 2분음표 두 박.'], no: ['The line cuts common time in half: 2/2, two minim beats.', '세로선이 4/4를 반으로 나눠요: 2/2, 2분음표 두 박.'] }][v]; },
  e98: () => { const v = Math.floor(Math.random() * 2); return [
    { prompt: ['9/8 is…', '9/8은…'], opts: [['ct', t('compound triple', '겹박자 세 박')], ['cd', t('compound duple', '겹박자 두 박')], ['st', t('simple triple', '홑박자 세 박')]], ans: 'ct', yes: ['Compound triple: three dotted-crotchet beats, each of three quavers.', '겹세박자: 점4분음표 세 박, 한 박에 8분음표 셋.'], no: ['Nine quavers in threes: three dotted-crotchet beats, compound triple.', '8분음표 아홉을 셋씩: 점4분음표 세 박, 겹세박자.'] },
    { prompt: ['3/8 has how many quaver beats in a bar?', '3/8은 한 마디에 8분음표 박이 몇 개?'], opts: [['2', '2'], ['3', '3'], ['6', '6']], ans: '3', yes: ['Three quaver beats: simple triple, counted 1 2 3.', '8분음표 세 박: 홑세박자, 1 2 3.'], no: ['Top 3, bottom 8 (quavers): three quaver beats.', '위의 3, 아래의 8(8분음표): 8분음표 세 박.'] }][v]; },
};
// ── the pictures on paper ──
const r2Pic = (svg) => lsRawPic(svg, [0, 0, 80, 44]);
const r2PicSemi = () => r2Pic([0, 1, 2, 3].map(i => '<ellipse cx="' + (14 + i * 16) + '" cy="34" rx="5.5" ry="4" transform="rotate(-20 ' + (14 + i * 16) + ' 34)" fill="#26296b"/><line x1="' + (19 + i * 16) + '" x2="' + (19 + i * 16) + '" y1="33" y2="8" stroke="#26296b" stroke-width="1.8"/>').join('') + '<rect x="18" y="7" width="50" height="4" fill="#26296b"/><rect x="18" y="13" width="50" height="4" fill="#e4572e"/>');
const r2PicDot = () => r2Pic('<ellipse cx="22" cy="34" rx="5.5" ry="4" transform="rotate(-20 22 34)" fill="#26296b"/><circle cx="33" cy="31" r="2.4" fill="#e4572e"/><ellipse cx="54" cy="34" rx="5.5" ry="4" transform="rotate(-20 54 34)" fill="#26296b"/><line x1="27" x2="27" y1="33" y2="8" stroke="#26296b" stroke-width="1.8"/><line x1="59" x2="59" y1="33" y2="8" stroke="#26296b" stroke-width="1.8"/><rect x="26" y="7" width="34" height="4" fill="#26296b"/><rect x="49" y="13" width="11" height="4" fill="#26296b"/>');
const r2PicTrip = () => r2Pic([0, 1, 2].map(i => '<ellipse cx="' + (20 + i * 18) + '" cy="34" rx="5.5" ry="4" transform="rotate(-20 ' + (20 + i * 18) + ' 34)" fill="#26296b"/><line x1="' + (25 + i * 18) + '" x2="' + (25 + i * 18) + '" y1="33" y2="12" stroke="#26296b" stroke-width="1.8"/>').join('') + '<rect x="24" y="11" width="38" height="4" fill="#26296b"/><text x="43" y="8" text-anchor="middle" font-family="Georgia, serif" font-style="italic" font-size="10" font-weight="900" fill="#e4572e">3</text>');
const r2PicMin = () => r2Pic('<text x="14" y="22" font-family="Georgia, serif" font-size="16" font-weight="900" fill="#26296b">3</text><text x="14" y="40" font-family="Georgia, serif" font-size="16" font-weight="900" fill="#e4572e">2</text><ellipse cx="50" cy="30" rx="6.5" ry="4.6" transform="rotate(-20 50 30)" fill="#fff" stroke="#26296b" stroke-width="2"/><line x1="56" x2="56" y1="29" y2="6" stroke="#26296b" stroke-width="1.8"/>');
const r2Pic98 = () => r2Pic('<text x="10" y="22" font-family="Georgia, serif" font-size="16" font-weight="900" fill="#e4572e">9</text><text x="10" y="40" font-family="Georgia, serif" font-size="16" font-weight="900" fill="#26296b">8</text>' + [0, 1, 2].map(i => lsCircleSvg(34 + i * 16, 22, 6, 'play', '')).join(''));

function r2LbPages(scr = false) {
  const ch = 'rhythm-23', rh = bkChapterNo('rhythm'), e8 = bkChapterNo('six-eight');
  const pen = (x) => <PenArt shapes={x.shapes} vb={x.vb} style={{width:90}}/>;
  const checks5 = [[r2PicSemi(), t('I count and clap semiquavers, alone and with a quaver: 1 e + a', '16분음표를 혼자서, 그리고 8분음표와 함께 세고 쳐요: 1 e + a')], [r2PicDot(), t('I clap the dotted quaver and semiquaver: long, short', '점8분음표와 16분음표를 쳐요: 길게, 짧게')],
    [r2PicTrip(), t('I fit three into a beat, and two into a dotted beat', '한 박에 셋, 점 박에 둘을 넣어요')], [r2PicMin(), t('I count minim beats in 2/2, cut common time and 3/2', '2/2, 세로선 C, 3/2에서 2분음표 박을 세요')], [r2Pic98(), t('I count 3/8 and 9/8, and say which is simple and which compound', '3/8과 9/8을 세고, 홑박자인지 겹박자인지 말해요')]];
  const toc = [[t('Semiquavers', '16분음표'), 2], [t('Dotted quaver and semiquaver', '점8분음표와 16분음표'), 3], [t('Three in a beat, two in a dotted beat', '한 박에 셋, 점 박에 둘'), 4], [t('The minim beat', '2분음표 박'), 5], [t('3/8 and 9/8', '3/8과 9/8'), 6], [t('My five checks', '나의 다섯 가지 확인'), 7]];
  const still = (keys) => <LbPic h={150}><div style={{display:'flex',flexDirection:'column',gap:12,width:'100%',maxWidth:600,margin:'0 auto'}}>{keys.map(k => <div key={k}>{r2El(k)}</div>)}</div></LbPic>;
  const pg = (no, step, title, keys, sayEn, sayKo, teach, pianoEn, pianoKo, remember, live, lvl) => <LbPage key={no} no={no} chId={ch} kicker={t('Step ' + step, step + '단계')} title={title} teacher={teach} qr={bkLink('drill=' + ch + '&tab=drill&level=' + lvl)}>
    <LbLive still={still(keys)} live={live}/>
    <LbSay>{LANG === 'ko' ? sayKo : sayEn}</LbSay>
    <LbPiano steps={LANG === 'ko' ? pianoKo : pianoEn}/>
    <LbRemember>{remember}</LbRemember>
  </LbPage>;
  return [
    <LbPage key="1" no={1} chId={ch} teacher={<>{t('Theory of Music, Grades 2 and 3, Time and Rhythm: the note values, rests and time signatures each grade adds, read in the music and written. Chapter ' + rh + ' has the Grade 1 rhythms and chapter ' + e8 + ' the 6/8 groundwork. Tap each line, then count it aloud.', 'Theory of Music 2·3급 박자와 리듬: 급마다 더해지는 음표, 쉼표, 박자표를 읽고 써요. 1급 리듬은 ' + rh + '장, 6/8 기초는 ' + e8 + '장에. 줄마다 쳐 보고, 그다음 소리 내어 세요.')}</>}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:50,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{t('Rhythm Further', '리듬 한 걸음 더')}</div>
      </div></LbOnly>
      {still(['semiB', 'e98'])}
      <LbSay size={18}>{t('Rhythm for Grades 2 and 3: smaller notes inside the beat, long and short, three for two, the minim beat, and nine quavers in a bar.', '2·3급 리듬: 박 안의 더 작은 음표, 길게 짧게, 둘 자리에 셋, 2분음표 박, 그리고 한 마디에 8분음표 아홉.')}</LbSay>
      <div className="lb-toc" style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>
        <LbOnly print><div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('In this chapter', '이 챕터에서는')}</div>
          {toc.map(([n, p]) => <div key={p} className="lb-toc-row" style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:14.5,padding:'5px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkGoal(15)}{n}</span><span style={{color:BK.muted,fontWeight:700}}>{p}</span></div>)}
        </div></LbOnly>
        <div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 챕터를 마치면')}</div>
          {[t('count and clap semiquavers and the dotted quaver', '16분음표와 점8분음표를 세고 칠 수 있어요'), t('fit three into a beat and two into a dotted beat', '한 박에 셋, 점 박에 둘을 넣을 수 있어요'), t('count in 2/2, 3/2, 3/8 and 9/8', '2/2, 3/2, 3/8, 9/8로 셀 수 있어요'), t('say whether a time signature is simple or compound', '박자표가 홑박자인지 겹박자인지 말할 수 있어요')].map((x, i) => <div key={i} style={{display:'flex',alignItems:'flex-start',gap:9,fontSize:14.5,padding:'5px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}>{bkGoal(15)}<span>{x}</span></div>)}
        </div>
      </div>
      <LbOnly print><LbDrillStrip id={ch}/></LbOnly>
    </LbPage>,
    pg(2, 1, t('Semiquavers', '16분음표'), ['semiA', 'semiB'], <>Four <b>semiquavers</b> share one beat, under two beams: <b>1 e + a</b>. At Grade 3 they team up with a quaver: <b>1 + a</b> and <b>1 e +</b>.</>, <>16분음표 넷이 한 박을 나눠요, 빔 두 개: <b>1 e + a</b>. 3급에서는 8분음표와 짝을 지어요: <b>1 + a</b>, <b>1 e +</b>.</>,
      <>{t('Grade 2: four semiquavers beamed. Grade 3: a quaver and two semiquavers, two semiquavers and a quaver, and the semiquaver on its own. Say the counts before clapping.', '2급: 빔으로 묶인 16분음표 넷. 3급: 8분음표 하나와 16분음표 둘, 16분음표 둘과 8분음표 하나, 그리고 혼자인 16분음표. 손뼉 전에 셈을 먼저 말해요.')}</>,
      [<>Say 1 e + a on every beat, steadily.</>, <>Clap line 1, then line 2, counting aloud.</>, <>Where do the two beams stop? That is where the quaver starts.</>], [<>박마다 1 e + a를 고르게 말해요.</>, <>1번 줄, 그다음 2번 줄을 소리 내어 세며 쳐요.</>, <>빔 두 개가 어디서 멈춰요? 거기서 8분음표가 시작해요.</>],
      t('Four to a beat: 1 e + a.', '한 박에 넷: 1 e + a.'), <R2Pad step="semi" keys={['semiA', 'semiB', 'semiC']} title={t('Semiquavers', '16분음표')} note={t('Two beams: four to a beat, 1 e + a. One beam on part of the group: a quaver there.', '빔 두 개: 한 박에 넷, 1 e + a. 일부에만 빔 하나: 거기는 8분음표.')} ask={R2_Q.semi}/>, 1),
    pg(3, 2, t('Dotted quaver and semiquaver', '점8분음표와 16분음표'), ['dotA', 'dotB'], <>A <b>dotted quaver</b> lasts three semiquavers, so the <b>semiquaver</b> comes last, on <b>a</b>: long, short.</>, <><b>점8분음표</b>는 16분음표 셋 길이라서, <b>16분음표</b>는 마지막 <b>a</b>에: 길게, 짧게.</>,
      <>{t('Grade 3: the dotted quaver and semiquaver, and in compound time the dotted quaver, semiquaver and quaver. The short note is often clapped too early; count 1 e + a under it.', '3급: 점8분음표와 16분음표, 그리고 겹박자에서 점8분음표, 16분음표, 8분음표. 짧은 음을 너무 일찍 치기 쉬워요: 아래에서 1 e + a를 세요.')}</>,
      [<>Count 1 e + a and clap only on 1 and a.</>, <>Clap line 1: long-short, long-short, then two crotchets.</>, <>Line 2 in 3/4: listen first, then tap it back.</>], [<>1 e + a를 세며 1과 a에만 쳐요.</>, <>1번 줄: 길게-짧게, 길게-짧게, 그다음 4분음표 둘.</>, <>2번 줄(3/4): 먼저 듣고, 따라 쳐요.</>],
      t('Long, short: the short one on a.', '길게, 짧게: 짧은 음은 a에.'), <R2Pad step="dot" keys={['dotA', 'dotB']} title={t('Dotted quaver and semiquaver', '점8분음표와 16분음표')} note={t('The dot makes the quaver three semiquavers long; the semiquaver fills the last quarter of the beat.', '점이 8분음표를 16분음표 셋 길이로 만들어요. 16분음표가 박의 마지막 4분의 1을 채워요.')} ask={R2_Q.dot}/>, 2),
    pg(4, 3, t('Three in a beat, two in a dotted beat', '한 박에 셋, 점 박에 둘'), ['tripA', 'duA'], <>A <b>triplet</b> puts three quavers where two go: <b>1 trip let</b>. In 6/8 a <b>duplet</b> puts two where three go.</>, <><b>셋잇단음표</b>는 둘 자리에 셋: <b>1 trip let</b>. 6/8에서 <b>2잇단음표</b>는 셋 자리에 둘.</>,
      <>{t('Grade 2: triplet quavers in simple time. Grade 3: the duplet in compound time. Keep the beat steady while the notes inside it change.', '2급: 홑박자의 셋잇단 8분음표. 3급: 겹박자의 2잇단음표. 박 안의 음이 바뀌어도 박은 고르게.')}</>,
      [<>Walk the beat; say 1 trip let on each step.</>, <>Clap line 1: triplets, then crotchets, then quavers.</>, <>Line 2 in 6/8: two even notes across three quavers.</>], [<>박을 걸으며 걸음마다 1 trip let.</>, <>1번 줄: 셋잇단음표, 4분음표, 8분음표.</>, <>2번 줄(6/8): 8분음표 셋 길이에 고른 음 둘.</>],
      t('Three for two, two for three.', '둘 자리에 셋, 셋 자리에 둘.'), <R2Pad step="trip" keys={['tripA', 'duA']} title={t('Three in a beat, two in a dotted beat', '한 박에 셋, 점 박에 둘')} note={t('The small number over the beam says how many fit in: 3 where two would go, 2 where three would go.', '빔 위의 작은 숫자가 몇 개가 들어가는지 말해요: 둘 자리에 3, 셋 자리에 2.')} ask={R2_Q.trip}/>, 3),
    pg(5, 4, t('The minim beat', '2분음표 박'), ['minA', 'minB'], <>When the bottom number is <b>2</b>, the <b>minim</b> is the beat: <b>2/2</b> (also written as a C with a line), <b>3/2</b>.</>, <>아래 숫자가 <b>2</b>이면 <b>2분음표</b>가 한 박: <b>2/2</b>(세로선 C로도 써요), <b>3/2</b>.</>,
      <>{t('Grade 3: 3/2, 2/2 and cut common time. The same notes as 4/4 or 3/4 look, but the beat is the minim: crotchets are half a beat.', '3급: 3/2, 2/2, 세로선 C. 4/4나 3/4와 같은 음표처럼 보여도 박은 2분음표: 4분음표는 반 박.')}</>,
      [<>Count 1 + 2 + with a minim on each number.</>, <>Clap line 1 in 2/2, then line 2 in 3/2.</>, <>Find a piece in cut common time and count it in two.</>], [<>숫자마다 2분음표, 1 + 2 + 로 세요.</>, <>1번 줄(2/2), 그다음 2번 줄(3/2)을 쳐요.</>, <>세로선 C로 된 곡을 찾아 둘로 세어 봐요.</>],
      t('Bottom number 2: the minim is the beat.', '아래 숫자 2: 2분음표가 한 박.'), <R2Pad step="minim" keys={['minA', 'minB', 'minC']} title={t('The minim beat', '2분음표 박')} note={t('2/2, cut common time and 3/2: a click on every minim.', '2/2, 세로선 C, 3/2: 2분음표마다 클릭.')} ask={R2_Q.minim}/>, 4),
    pg(6, 5, t('3/8 and 9/8', '3/8과 9/8'), ['e38', 'e98'], <><b>3/8</b>: three quaver beats, simple triple. <b>9/8</b>: nine quavers in threes, three dotted-crotchet beats: <b>compound triple</b>.</>, <><b>3/8</b>: 8분음표 세 박, 홑세박자. <b>9/8</b>: 8분음표 아홉을 셋씩, 점4분음표 세 박: <b>겹세박자</b>.</>,
      <>{t('Grade 3: 3/8 and 9/8, and compound triple time in general knowledge. Bottom number 8: quavers. Top 3: simple, each quaver a beat. Top 6 or 9: compound, the quavers in threes.', '3급: 3/8과 9/8, 일반 지식의 겹세박자. 아래 숫자 8: 8분음표. 위가 3: 홑박자, 8분음표마다 한 박. 위가 6이나 9: 겹박자, 8분음표를 셋씩.')}</>,
      [<>Count 1 2 3 in 3/8, one quaver to each number.</>, <>9/8: count 1 to 9, leaning on 1, 4 and 7.</>, <>Clap line 2, feeling three big beats.</>], [<>3/8: 숫자마다 8분음표 하나, 1 2 3.</>, <>9/8: 1부터 9까지, 1, 4, 7에 힘을 줘요.</>, <>2번 줄을 큰 박 셋으로 느끼며 쳐요.</>],
      t('9/8: three big beats of three.', '9/8: 셋씩 묶인 큰 박 셋.'), <R2Pad step="e98" keys={['e38', 'e98']} title={t('3/8 and 9/8', '3/8과 9/8')} note={t('Count every quaver. In 9/8 the strong ones are 1, 4 and 7.', '8분음표마다 세요. 9/8에서는 1, 4, 7이 세요.')} ask={R2_Q.e98}/>, 5),
    <LbPage key="7" no={7} chId={ch} kicker={t('Check-up', '점검')} title={t('My five checks', '나의 다섯 가지 확인')}
      teacher={<>{t('Clap and count each one to you, then write a bar of it.', '하나씩 손뼉과 셈으로 들려주고, 그다음 한 마디씩 써 봐요.')}</>}>
      <LbSay>{t('Tick each one: not yet, nearly, or got it!', '하나씩 표시해요: 아직, 거의, 됐어요!')}</LbSay>
      <LbLive still={<LbStageRows big rows={checks5.map(([a, txt]) => [pen(a), txt])}/>} live={<FiveChecks376 rows={checks5} storeKey="pb_r2_five"/>}/>
    </LbPage>,
  ];
}
function Rhythm23LessonBook() { return <>{r2LbPages(false)}</>; }
function R2Learn({ onStart }) {
  const pages = r2LbPages(true), opener = pages[0];
  return (
    <Lesson id="rhythm-23" title={t('Rhythm Further', '리듬 한 걸음 더')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="rhythm-23"><div className="lb-screen lb-open" style={{display:'flex',flexDirection:'column',gap:12,margin:'0 0 8px'}}>{lbWordsFirst(opener.props.children)}</div></BkChapterCtx.Provider></LbScreenCtx.Provider>}>
      {pages.slice(1).map((pg, i) => <Step key={i} title={pg.props.title}><LbScreenPage page={pg}/></Step>)}
    </Lesson>
  );
}
// ── the drill: the questions, then which line was played ──
const R2_LEVELS = [
  { n: 1, label: 'Semiquavers', kind: 'semi', time: 12 },
  { n: 2, label: 'Dotted quaver and semiquaver', kind: 'dot', time: 12 },
  { n: 3, label: 'Triplets and duplets', kind: 'trip', time: 12 },
  { n: 4, label: 'The minim beat', kind: 'minim', time: 12 },
  { n: 5, label: '3/8 and 9/8', kind: 'e98', time: 12 },
  { n: 6, label: 'Listen: which line?', kind: 'hear', time: 20 },
];
Object.assign(LEVEL_KO, { 'Semiquavers': '16분음표', 'Dotted quaver and semiquaver': '점8분음표와 16분음표', 'Triplets and duplets': '셋잇단음표와 2잇단음표', 'The minim beat': '2분음표 박', '3/8 and 9/8': '3/8과 9/8', 'Listen: which line?': '들어 보기: 어느 줄일까?' });
const R2_HEAR = [['semiA', 'semiB', 'dotA'], ['tripA', 'semiA', 'dotA'], ['minA', 'minB', 'minC'], ['e38', 'e98', 'duA']];
function genR2Question(lv, prev) {
  const uid = Math.random();
  if (lv.kind === 'hear') { let set, i, g = 0; do { set = R2_HEAR[Math.floor(Math.random() * R2_HEAR.length)]; i = Math.floor(Math.random() * 3); } while (prev && prev.key === set[i] && g++ < 10);
    return { kind: 'hear', set, i, answer: String(i), choices: ['0', '1', '2'], key: set[i], uid }; }
  let q, g = 0; do { q = R2_Q[lv.kind](); } while (prev && prev.key === q.prompt[0] && g++ < 10);
  return { kind: lv.kind, q, answer: q.ans, choices: q.opts.map(o => o[0]), key: q.prompt[0], uid };
}
const r2Fig = { semi: 'semiB', dot: 'dotA', trip: 'tripA', minim: 'minB', e98: 'e98' };
function r2AnswerLabel(q) { if (q.kind === 'hear') return t('line ' + (Number(q.answer) + 1), (Number(q.answer) + 1) + '번 줄'); const o = q.q.opts.find(x => x[0] === q.answer); return o ? (typeof o[1] === 'string' ? o[1] : o[0]) : q.answer; }
function R2Question({ q, given, locked, onAnswer, pixel }) {
  const done = !!given, btnCls = pixel ? 'pixel-choice' : 'choice-btn', cls = (c) => btnCls + (!done ? '' : c === q.answer ? ' good' : given.ans === c ? ' bad' : '');
  const pickIt = (c) => { if (locked || done) return; stopClicks(); onAnswer(c); };
  useEffect(() => { if (q.kind !== 'hear') return; const id = setTimeout(() => r2Play(q.set[q.i]), 400); return () => { clearTimeout(id); stopClicks(); }; }, [q.uid]);
  if (q.kind === 'hear') return (<div>
    <p style={pixel ? {fontSize:11.5,textAlign:'center'} : {fontSize:15,fontWeight:700,textAlign:'center',margin:'0 0 8px',color:'var(--muted)'}}>{t('Listen: which line was played?', '들어 봐요: 어느 줄이었을까요?')}</p>
    <div style={{textAlign:'center',marginBottom:8}}><button className={pixel ? 'pixel-btn' : 'ghost-btn'} style={{minHeight:40}} onClick={() => r2Play(q.set[q.i])}>{t('▶ Play it again', '▶ 다시 듣기')}</button></div>
    <div style={{display:'flex',flexDirection:'column',gap:8}}>{q.set.map((k, j) => <button key={j} disabled={locked} className={cls(String(j))} style={{padding:'6px 4px'}} onClick={() => pickIt(String(j))}><div style={{width:'100%',minWidth:0}}>{r2El(k, { counts: false, hearts: false })}</div></button>)}</div>
  </div>);
  return (<div>
    <p style={pixel ? {fontSize:11.5,textAlign:'center'} : {fontSize:15,fontWeight:700,textAlign:'center',margin:'0 0 8px',color:'var(--muted)',textWrap:'balance'}}>{t(q.q.prompt[0], q.q.prompt[1])}</p>
    <div style={{maxWidth:420,margin:'0 auto'}}>{r2El(r2Fig[q.kind], { counts: done ? undefined : false })}</div>
    <div style={{display:'grid',gridTemplateColumns:'repeat(' + q.q.opts.length + ',minmax(0,1fr))',gap:8,marginTop:10}}>{q.q.opts.map(([id, lab]) => <button key={id} disabled={locked} className={cls(id)} style={{padding:'12px 4px',fontSize:15,fontWeight:900}} onClick={() => pickIt(id)}>{lab}</button>)}</div>
    {done && !pixel && <div style={{marginTop:10,fontSize:13.5,color:'#4a4d86',background:'#fff',borderRadius:8,padding:'7px 10px',lineHeight:1.45}}>{t(q.q.yes[0], q.q.yes[1])}</div>}
  </div>);
}
Object.assign(RHYTHM_23_DRILL, { levels: R2_LEVELS, generate: genR2Question, check: (q, ans) => ans !== null && ans !== undefined && ans === q.answer, answerLabel: r2AnswerLabel, Question: R2Question, Learn: R2Learn });
// the teacher's copy: every line with its counts, and what to listen for
function R2Teacher() {
  const pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="rhythm-23" teacher>{content}</WbPage>);
  const lines = (keys) => <div style={{display:'flex',flexDirection:'column',gap:4}}>{keys.map((k, i) => <div key={k} style={{display:'flex',alignItems:'center',gap:6}}>{nvNum(i + 1)}<div style={{flex:1,minWidth:0}}>{r2El(k, { hearts: false })}</div></div>)}</div>;
  P(<>
    <div style={{fontFamily:LB_SERIF,fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('rhythm-23')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 12px',lineHeight:1.5}}>Theory of Music Grades 2 and 3, Time and Rhythm. Each line as the app plays it, with its counts. The child counts aloud first, then claps.</div>
    <TcBlock page={2} title="Semiquavers" answers={lines(['semiA', 'semiB', 'semiC'])} watch="Semiquavers rushed into the next beat. Say 1 e + a steadily before clapping." say="“Four to a beat: 1 e + a.”"/>
    <TcBlock page={3} title="Dotted quaver and semiquaver" answers={lines(['dotA', 'dotB'])} watch="The pair clapped as two even quavers. The short note comes late, on a." say="“Long, short: the short one on a.”"/>
  </>);
  P(<>
    <TcBlock page={4} title="Three in a beat, two in a dotted beat" answers={lines(['tripA', 'duA'])} watch="Triplets that turn into a quaver and two semiquavers; duplets that slip back into three." say="“Three for two, two for three.”"/>
    <TcBlock page={5} title="The minim beat" answers={lines(['minA', 'minB', 'minC'])} watch="Counting crotchets in 2/2. The click falls on every minim." say="“Bottom number 2: the minim is the beat.”"/>
    <TcBlock page={6} title="3/8 and 9/8" answers={lines(['e38', 'e98'])} watch="9/8 counted as three bars of 3/8 with equal weight. Lean on 1, 4 and 7." say="“9/8: three big beats of three.”"/>
    <TcBlock page={7} title="My five checks" answers={<div style={{fontSize:12,color:BK.ink,lineHeight:1.5}}>Each line clapped and counted to you; then the child writes one bar of each new value. Transposition (Grades 2 and 3, a melody of up to eight bars into another key of the grade) is in the Transposing lesson on the Home.</div>}/>
  </>);
  return <>{pages}</>;
}
TEACHER_COPIES['rhythm-23'] = R2Teacher;
'''
rep("""TEACHER_COPIES['harmony-23'] = H3Teacher;""", """TEACHER_COPIES['harmony-23'] = H3Teacher;""" + CH)

HOME = r'''
// ══ Build AM: Rhythm Further on the Home (Rhythm, after 6/8 time) ══
LBH_FN['rhythm-23'] = (s) => r2LbPages(s);
const r2Q = (kind) => (n, prev) => { if (n % 2 === 0) { const key = { semi: 'semiB', dot: 'dotA', trip: 'tripA', minim: 'minB', e98: 'e98' }[kind], R = R2[key]; return rqStaffQ(R.items, { unit: R.unit, clicks: R.clicks, accentAt: R.accentAt, accent: !!R.accentAt, bpm: R.bpm, so: R.so }); }
  const q = R2_Q[kind](); return { kind: 'choice', cols: q.opts.length, key: q.prompt[0], prompt: q.prompt, opts: q.opts.map(([id, lab]) => ({ id, label: lab })), ans: q.ans, ok: (v) => v === q.ans, fig: () => ({ mid: r2El(r2Fig[kind]) }), yes: q.yes, no: q.no }; };
const r2HomeAdd = (id, i, en, ko, benEn, bko, make) => lbhAdd(id, 'r-beat', 'rhythm', en, ko, benEn, bko, lbhSpec('rhythm-23', i, { make }));
r2HomeAdd('r2-semi', 1, 'Semiquavers', '16분음표', 'Four to a beat, and with a quaver.', '한 박에 넷, 그리고 8분음표와 함께.', r2Q('semi'));
r2HomeAdd('r2-dot', 2, 'Dotted quaver and semiquaver', '점8분음표와 16분음표', 'Long, short: the short one on a.', '길게, 짧게: 짧은 음은 a에.', r2Q('dot'));
r2HomeAdd('r2-trip', 3, 'Three in a beat, two in a dotted beat', '한 박에 셋, 점 박에 둘', 'Triplets and duplets.', '셋잇단음표와 2잇단음표.', r2Q('trip'));
r2HomeAdd('r2-minim', 4, 'The minim beat', '2분음표 박', '2/2, cut common time, 3/2.', '2/2, 세로선 C, 3/2.', r2Q('minim'));
r2HomeAdd('r2-98', 5, '3/8 and 9/8', '3/8과 9/8', 'Simple triple and compound triple.', '홑세박자와 겹세박자.', r2Q('e98'));
'''
rep("""
lbhAdd('rb-finger', 'r-beat', 'rhythm', 'The beat in your fingers'""", HOME + """
lbhAdd('rb-finger', 'r-beat', 'rhythm', 'The beat in your fingers'""")
rep("""const LESSON_BOOKS = { 'harmony-23': Harmony23LessonBook,""", """const LESSON_BOOKS = { 'rhythm-23': Rhythm23LessonBook, 'harmony-23': Harmony23LessonBook,""")
rep("""const LB_PAGE_FNS = { 'harmony-23': h3LbPages,""", """const LB_PAGE_FNS = { 'rhythm-23': r2LbPages, 'harmony-23': h3LbPages,""")
rep("""const HOUSE_ICONS = {"harmony-23": """, """const HOUSE_ICONS = {"rhythm-23": "<ellipse cx=\\"12\\" cy=\\"34\\" rx=\\"4.5\\" ry=\\"3.4\\" fill=\\"#26296b\\"/><ellipse cx=\\"24\\" cy=\\"34\\" rx=\\"4.5\\" ry=\\"3.4\\" fill=\\"#26296b\\"/><ellipse cx=\\"36\\" cy=\\"34\\" rx=\\"4.5\\" ry=\\"3.4\\" fill=\\"#26296b\\"/><path d=\\"M16 33V10M28 33V10M40 33V10\\"/><path d=\\"M16 10H40\\" stroke-width=\\"3.5\\"/><path d=\\"M28 16H40\\" stroke=\\"#e4572e\\" stroke-width=\\"3.5\\"/>", "harmony-23": """)
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
