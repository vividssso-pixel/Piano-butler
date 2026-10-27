import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)
def rep_in(fn_start, pairs):   # replacements inside one function only
    global s
    assert s.count(fn_start) == 1, fn_start
    a = s.index(fn_start); b = s.index('\n}\n', a) + 3; body = s[a:b]
    for old, new, *k in pairs:
        n = k[0] if k else 1
        assert body.count(old) == n, (body.count(old), old[:80])
        body = body.replace(old, new)
    s = s[:a] + body + s[b:]

# Build AZ (board call 23, the first Grade 5 room): Hear and Sing, Grade 5. The Grade 5 practical aural tests (Manual of
# Syllabuses 2026, section 21, read 27 Oct): the keynote, then any interval of the major scale straight after it, sung and
# named in full; the higher or the lower part of a two-part progression of THREE successive intervals, within an octave from
# middle C, played slowly, sung from memory; any major or minor triad, root position or inverted, within an octave: hum or sing
# ALL THREE notes, ascending or descending as asked; a passage in duple or triple time played twice, tapped back and named.
# The house gains the Grade 5 floor (floor 6); Stories of music, now the top storey, is drawn as the attic under the roof
# (her 00:49 question, my recommendation, her 12:30 'go').

rep("""const LISTEN_4_DRILL = { id: 'listen-4', label: 'Hear and Sing, Grade 4', noPrint: true };   // Build AR""",
    """const LISTEN_4_DRILL = { id: 'listen-4', label: 'Hear and Sing, Grade 4', noPrint: true };   // Build AR
const LISTEN_5_DRILL = { id: 'listen-5', label: 'Hear and Sing, Grade 5', noPrint: true };   // Build AZ""")
rep("""  { id: 'listen-4', label: 'Hear and Sing, Grade 4', concept: LISTEN_4_DRILL, track: 'start' },   // Build AR""",
    """  { id: 'listen-4', label: 'Hear and Sing, Grade 4', concept: LISTEN_4_DRILL, track: 'start' },   // Build AR
  { id: 'listen-5', label: 'Hear and Sing, Grade 5', concept: LISTEN_5_DRILL, track: 'start' },   // Build AZ""")
rep("""'listen-4': '듣고 부르기, Grade 4'""", """'listen-4': '듣고 부르기, Grade 4', 'listen-5': '듣고 부르기, Grade 5'""")
rep("""'listen-4': ['listen-23', 'intervals']""", """'listen-4': ['listen-23', 'intervals'], 'listen-5': ['listen-4']""")
rep("""'listen-4': ['Hear & sing 4', '듣기 4']""", """'listen-4': ['Hear & sing 4', '듣기 4'], 'listen-5': ['Hear & sing 5', '듣기 5']""")
rep("""  'listen-4': 'aural ear grade 4""", """  'listen-5': 'aural ear grade 5 interval major scale keynote name two-part progression three intervals upper lower part triad all three notes ascending descending arpeggio sing clap back duple triple triplet syncopation',
  'listen-4': 'aural ear grade 4""")
rep("""if (id === 'listen-sing' || id === 'listen-write' || id === 'listen-23' || id === 'listen-4') return 'aural';""",
    """if (id === 'listen-sing' || id === 'listen-write' || id === 'listen-23' || id === 'listen-4' || id === 'listen-5') return 'aural';""")
# the house: the Grade 5 floor, then Stories of music in the attic
rep("""  { ids: ['piano-story', 'pitch-range', 'composers', 'styles'], stories: true,""",
    """  { ids: ['listen-5', 'scales-5', 'keys-5', 'harmony-5'], en: ['Grade 5', 'Your ears, scales and arpeggios, keys and intervals, and chords and cadences.'], ko: ['Grade 5', '귀, 스케일과 아르페지오, 조와 음정, 그리고 화음과 종지.'] },   // Build AZ: the Grade 5 floor (call 23); its rooms appear as they are built
  { ids: ['piano-story', 'pitch-range', 'composers', 'styles'], stories: true, garret: true,""")
rep("""  return w + (sm ? (ko ? (at ? ', 음악 이야기 방' : '과 음악 이야기 방') : (at ? ', a Stories of music room' : ' and a Stories of music room')) : '') + (at ? (ko ? '과 다락방' : ' and an attic') : ''); };""",
    """  const gr = PATH_STAGES.some(x => x.stories && x.garret);   // Build AZ: Stories of music is the attic
  return w + (sm ? (ko ? (gr ? '과 다락방의 음악 이야기 방' : at ? ', 음악 이야기 방' : '과 음악 이야기 방') : (gr ? ' and a Stories of music room in the attic' : at ? ', a Stories of music room' : ' and a Stories of music room')) : '') + (at ? (ko ? '과 다락방' : ' and an attic') : ''); };""")
# the townhouse: the top floor in the attic -- the mansard's lower slopes come down its sides in slate, the rooms between them;
# the roof, its cresting and the turrets step in to meet them; the quoins start below the attic
rep("""    const st = view.stages[k], fs = (st.s && st.s.th) || TH_FLOOR[k], n = st.ids.length, c = cols(n), here = st.ids.includes(view.here);
    const rwOf = (j) => (X1 - RX0) / Math.min(c, n - Math.floor(j / c) * c), lay = thNames(state, st.ids.map((id, j) => [id, rwOf(j)]));""",
    """    const st = view.stages[k], fs = (st.s && st.s.th) || TH_FLOOR[k], n = st.ids.length, c = cols(n), here = st.ids.includes(view.here);
    const gi = st.s && st.s.garret ? gTop : 0, L0 = RX0 + gi, L1 = X1 - gi;   // Build AZ: the attic's rooms sit between the slopes
    const rwOf = (j) => (L1 - L0) / Math.min(c, n - Math.floor(j / c) * c), lay = thNames(state, st.ids.map((id, j) => [id, rwOf(j)]));""")
rep("""    body += thCornice(y, X0, X1); const yy = y + SLAB;
    body += '<rect x="' + RX0 + '" y="' + pFix(yy) + '" width="' + (X1 - RX0) + '" height="' + LH + '" stroke="none"/>';""",
    """    body += gi ? thCornice(y, L0 - 4, L1 + 4) : thCornice(y, X0, X1); const yy = y + SLAB;
    body += '<rect x="' + L0 + '" y="' + pFix(yy) + '" width="' + (L1 - L0) + '" height="' + LH + '" stroke="none"/>';""")
rep("""      body += thRoom(view, state, id, RX0 + cc * rw, yy + LH + (nr - 1 - r) * rh, rw, rh, fs, out, o.dimNew, lay);
    });
    y = yy + fh;""", """      body += thRoom(view, state, id, L0 + cc * rw, yy + LH + (nr - 1 - r) * rh, rw, rh, fs, out, o.dimNew, lay);
    });
    if (gi) {   // the slopes: slate outside, a white knee wall inside, the line between them as strong as the walls
      const yb = yy + fh;
      [[X0, L0], [X1, L1]].forEach(([xo, xi]) => {
        body += '<path d="' + stD('M', xo, yb, 'L', xi, yb, 'L', xi, y, 'Z') + '" fill="#fff" stroke="none"/>'
          + '<path d="' + stD('M', xo, yb, 'L', xi, y, 'L', xo, y, 'Z') + '" fill="url(#thslate)" stroke="none"/>' + stL(xo, yb, xi, y, 2.2);
      });
      garretBot = yb;
    }
    y = yy + fh;""")
rep("""  const top = 176; let y = top;
  for (let k = view.stages.length - 1; k >= 0; k--) {   // the floors, the top stage first""",
    """  const top = 176; let y = top;
  const topS = view.stages.length ? view.stages[view.stages.length - 1].s : null, gTop = topS && topS.garret ? (o.wide ? 26 : 18) : 0;   // Build AZ: the attic's inset
  let garretBot = 0;
  for (let k = view.stages.length - 1; k >= 0; k--) {   // the floors, the top stage first""")
rep("""  body += stQuoins(X0, top, gb, false) + stQuoins(X1, top, gb, true) + stL(X0, top, X0, gb, 2.2) + stL(X1, top, X1, gb, 2.2);""",
    """  const qTop = garretBot || top;   // Build AZ: the quoins and the corner lines start under the attic
  body += stQuoins(X0, qTop, gb, false) + stQuoins(X1, qTop, gb, true) + stL(X0, qTop, X0, gb, 2.2) + stL(X1, qTop, X1, gb, 2.2);""")
rep("""  const rb = top, rt = top - 66, roof = stD('M', X0 + 6, rb, 'L', X0 + 30, rt, 'L', X1 - 30, rt, 'L', X1 - 6, rb, 'Z');
  head += '<path d="' + roof + '" fill="url(#thslate)" stroke-width="1.6"/>';
  for (let x = X0 + 30; x < X1 - 26; x += 8) head += '<path d="' + stD('M', x, rt, 'l', 0, -7, 'm', -3, 3, 'l', 3, -3, 'l', 3, 3) + '" fill="none" stroke-width="1"/>';
  head += stR(X0 + 26, rt - 1, X1 - X0 - 52, 2, 0, ST.N);""",
    """  const rb = top, rt = top - 66, g2 = gTop ? gTop - 8 : 0, roof = stD('M', X0 + 6 + g2, rb, 'L', X0 + 30 + g2, rt, 'L', X1 - 30 - g2, rt, 'L', X1 - 6 - g2, rb, 'Z');
  head += '<path d="' + roof + '" fill="url(#thslate)" stroke-width="1.6"/>';
  for (let x = X0 + 30 + g2; x < X1 - 26 - g2; x += 8) head += '<path d="' + stD('M', x, rt, 'l', 0, -7, 'm', -3, 3, 'l', 3, -3, 'l', 3, 3) + '" fill="none" stroke-width="1"/>';
  head += stR(X0 + 26 + g2, rt - 1, X1 - X0 - 52 - 2 * g2, 2, 0, ST.N);""")
rep("""  [[X0 + 4, VIC_KING], [X1 - 40, VIC_QUEEN]].forEach(([tx, pc]) => {""", """  [[X0 + 4 + g2, VIC_KING], [X1 - 40 - g2, VIC_QUEEN]].forEach(([tx, pc]) => {""")

# the Grade 4 pads learn to serve Grade 5: the keynotes, and the clap-back passages, speed and words
rep_in("function L4IvPad({ onResult, fixed }) {", [
    ("function L4IvPad({ onResult, fixed }) {", "function L4IvPad({ onResult, fixed, keys = L4_KEYS }) {"),
    ("y = { k: pick(L4_KEYS), n:", "y = { k: pick(keys), n:"),
])
rep_in("function L4ClapPad({ onResult, fixed }) {", [
    ("function L4ClapPad({ onResult, fixed }) {", "function L4ClapPad({ onResult, fixed, set = L4_CLAP, bpm = L4_CLAP_BPM, note = null }) {"),
    ("const P = L4_CLAP[i]", "const P = set[i]"),
    ("{ bpm: L4_CLAP_BPM }", "{ bpm }", 2),
    ("{ bpm: L4_CLAP_BPM, silent: true }", "{ bpm, silent: true }"),
    ("spChips(L4_CLAP.map(", "spChips(set.map("),
    ("<div style={actNote}>{LANG === 'ko'", "<div style={actNote}>{note || (LANG === 'ko'"),
    ("and <b>a quaver rest</b>.</>}</div>", "and <b>a quaver rest</b>.</>)}</div>"),
])

CH = r'''
// ─── Chapter: Hear and Sing, Grade 5 (Build AZ, 2026-10-27; board call 23, the first Grade 5 room) ───
// The Grade 5 practical aural tests (Manual 2026, section 21), one step each: the keynote, then any interval of the major
// scale, sung and named in full (now from any keynote); three intervals in two parts, played slowly, the higher or the lower
// part sung from memory; a major or minor triad, root position or inverted: all three notes sung, up or down as asked; a
// passage heard twice, tapped back, duple or triple said. Every test is heard twice.
const L5_KEYS = [0, 1, 2, 3, 4, 5, 6, 7, -1, -2, -3, -4];   // any keynote from the A flat below middle C to the G above
// three intervals in two parts, within an octave from middle C: parallel 3rds and 6ths, contrary and oblique motion
const L5_TWO = [
  [[0, 4], [2, 5], [4, 7]], [[4, 12], [2, 11], [0, 12]], [[0, 7], [2, 5], [4, 7]], [[5, 9], [4, 7], [2, 5]],
  [[0, 9], [2, 7], [4, 7]], [[7, 11], [5, 12], [4, 12]], [[0, 4], [0, 5], [0, 7]], [[4, 7], [2, 9], [0, 12]],
  [[2, 5], [4, 7], [0, 9]], [[0, 12], [2, 11], [4, 9]], [[5, 9], [7, 11], [4, 12]], [[7, 12], [5, 9], [4, 7]],
];
const l5PlayTwo = (pr) => { const g = 1.9, ev = []; for (let r = 0; r < 2; r++) pr.forEach((iv, j) => ev.push({ at: r * (pr.length * g + 1.4) + j * g, keys: iv, len: j === pr.length - 1 ? 1.9 : 1.6, vol: 0.13 })); return spPlay(ev, 66); };   // played slowly, twice
// clap-back passages for Grade 5: the triplet, the syncopated quaver-crotchet-quaver, four semiquavers (our reading of
// "the difficulty adjusted to the standards of the respective Grades": flagged to Sohyun)
const L5_CLAP = [
  { m: 2, items: [['ts', 2], ['e'], ['q'], ['e'], ['|'], ['t3'], ['q'], ['|'], ['ds'], ['p'], ['|'], ['h'], ['||']] },
  { m: 3, items: [['ts', 3], ['q'], ['t3'], ['q'], ['|'], ['e'], ['q'], ['e'], ['q'], ['|'], ['s4'], ['ds'], ['q'], ['|'], ['hd'], ['||']] },
  { m: 2, items: [['ts', 2], ['s4'], ['t3'], ['|'], ['e'], ['q'], ['e'], ['|'], ['qd'], ['e'], ['|'], ['h'], ['||']] },
  { m: 3, items: [['ts', 3], ['t3'], ['t3'], ['q'], ['|'], ['qd'], ['e'], ['q'], ['|'], ['e'], ['q'], ['e'], ['q'], ['|'], ['hd'], ['||']] },
  { m: 2, items: [['ts', 2], ['q'], ['er'], ['e'], ['|'], ['t3'], ['ds'], ['|'], ['e'], ['q'], ['e'], ['|'], ['h'], ['||']] },
  { m: 3, items: [['ts', 3], ['ds'], ['t3'], ['q'], ['|'], ['h'], ['q'], ['|'], ['e'], ['q'], ['q'], ['e'], ['|'], ['hd'], ['||']] },
];
const L5_CLAP_BPM = 76;
const l5ClapNote = () => (LANG === 'ko' ? <>리듬을 <b>두 번</b> 들어요. 클릭에 맞춰 똑같이 치고, <b>두 박인지 세 박인지</b> 말해요. 이번에는 <b>셋잇단음표</b>(한 박에 셋)와 <b>당김음</b>(8분-4분-8분)도 나와요.</>
  : <>Hear the passage <b>twice</b>. Tap it back with the clicks, then say <b>two or three</b>. Now with <b>the triplet</b> (three in a beat) and <b>syncopation</b> (quaver, crotchet, quaver).</>);

// ── step 2: three intervals in two parts; sing the higher or the lower part from memory, then find its three notes ──
function L5TwoPad({ onResult, fixed }) {
  const [x, setX] = useState(fixed || { pr: L5_TWO[0], ask: 'hi' }), [heard, setHeard] = useState(false), [got, setGot] = useState(0), [miss, setMiss] = useState(0), [wrong, setWrong] = useState(null);
  const part = x.pr.map(iv => x.ask === 'hi' ? iv[1] : iv[0]), N = part.length, done = got >= N;
  const play = () => { setHeard(true); l5PlayTwo(x.pr); };
  const fresh = () => { let y, g = 0; do { y = { pr: pick(L5_TWO), ask: Math.random() < 0.5 ? 'hi' : 'lo' }; } while (y.pr === x.pr && y.ask === x.ask && g++ < 10); setX(y); setGot(0); setMiss(0); setWrong(null); setHeard(true); l5PlayTwo(y.pr); };
  const tap = (k) => { playKey(k, 0.5); if (!heard || done) return; if (k === part[got]) { const g = got + 1; setGot(g); setWrong(null); if (g >= N && onResult) onResult({ ok: miss === 0 }); } else { setMiss(m => m + 1); setWrong(k); } };
  const lit = {}; if (done) { x.pr.forEach(iv => iv.forEach(k => { lit[k] = 'pale'; })); part.forEach(k => { lit[k] = 'good'; }); } else { part.slice(0, got).forEach(k => { lit[k] = 'cor'; }); if (wrong != null) lit[wrong] = 'bad'; }
  const askW = x.ask === 'hi' ? t('the higher part', '윗성부') : t('the lower part', '아랫성부');
  return (
    <div className="try-box" style={actBox} data-l5="two">
      <div style={actTitle}>{t('Three intervals: sing one part', '세 음정: 한 성부를 불러요')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>두 음씩 <b>세 번</b>, 천천히 울려요(전체를 두 번). 외워서 <b>{askW}</b>의 세 음을 부르고, 건반에서 차례로 찾아요. 윗성부는 새, 아랫성부는 거북이: 한 줄만 따라가요.</>
        : <>Two notes together, <b>three times</b>, slowly (all of it played twice). From memory, sing the three notes of <b>{askW}</b>, then find them on the keys in order. The higher part is the bird's, the lower the turtle's: follow one line.</>}</div>
      {heard && <div style={{textAlign:'center',fontSize:16,fontWeight:900,color:BK.coral,margin:'0 0 6px'}}>{x.ask === 'hi' ? t('Sing the higher part ↑', '윗성부를 불러요 ↑') : t('Sing the lower part ↓', '아랫성부를 불러요 ↓')}</div>}
      <SpKb lo={0} hi={12} W={34} H={86} lit={lit} names={done ? Object.fromEntries(x.pr.flat().map(k => [k, l4Let(k)])) : { 0: 'C' }} onTap={tap} label={t('Find the part you sang', '부른 성부 찾기')}/>
      {lwMsg(!heard ? t('Tap ▶ to hear the two parts.', '▶를 누르면 두 성부가 나와요.') : done ? t(askW.charAt(0).toUpperCase() + askW.slice(1) + ': ' + part.map(l4Let).join(', ') + '. ' + (miss ? 'Found it.' : 'First time!'), askW + ': ' + part.map(l4Let).join(', ') + '. ' + (miss ? '찾았어요.' : '한 번에!'))
        : wrong != null ? t('Not that one: sing the part again, then try.', '그 음이 아니에요: 다시 불러 보고 찾아요.') : t('Sing it, then find note ' + (got + 1) + ' of ' + N + '.', '부르고, 세 음 중 ' + (got + 1) + '번째를 찾아요.'), done ? BK.green : wrong != null ? BK.coral : undefined)}
      {lwRow(<>
        <button className="ghost-btn" style={lwBtn} onClick={heard && !fixed ? fresh : play}>{!heard ? t('▶ Play the two parts', '▶ 두 성부 듣기') : fixed ? t('♪ Again', '♪ 다시') : t('▶ Another', '▶ 다른 것')}</button>
        {heard && !fixed && <button className="ghost-btn" style={lwBtn} onClick={play}>{t('♪ Again', '♪ 다시')}</button>}
        {heard && !done && <button className="ghost-btn" style={lwBtn} onClick={() => spPlay(part.map((k, j) => ({ at: j * 1.3, keys: [k], len: 1.2 })), 72)}>{t('♪ Just that part', '♪ 그 성부만')}</button>}
      </>)}
    </div>
  );
}

// ── step 3: a triad, root position or inverted: sing all three notes, up or down as asked, then find them in that order ──
const L5_TRIS = L4_TRIS;
function L5TriPad({ onResult, fixed }) {
  const [x, setX] = useState(fixed || { tri: L5_TRIS[0], dir: 'up' }), [heard, setHeard] = useState(false), [got, setGot] = useState(0), [miss, setMiss] = useState(0), [wrong, setWrong] = useState(null);
  const n = l4Tri(x.tri[0], x.tri[1], x.tri[2]), seq = x.dir === 'up' ? n : n.slice().reverse(), done = got >= 3;
  const play = () => { setHeard(true); l4PlayTri(n); };
  const fresh = () => { let y, g = 0; do { y = { tri: pick(L5_TRIS), dir: Math.random() < 0.5 ? 'up' : 'down' }; } while (y.tri === x.tri && y.dir === x.dir && g++ < 10); setX(y); setGot(0); setMiss(0); setWrong(null); setHeard(true); l4PlayTri(l4Tri(y.tri[0], y.tri[1], y.tri[2])); };
  const tap = (k) => { playKey(k, 0.5); if (!heard || done) return; if (k === seq[got]) { const g = got + 1; setGot(g); setWrong(null); if (g >= 3 && onResult) onResult({ ok: miss === 0 }); } else { setMiss(m => m + 1); setWrong(k); } };
  const lit = {}; if (done) n.forEach(k => { lit[k] = 'good'; }); else { seq.slice(0, got).forEach(k => { lit[k] = 'cor'; }); if (wrong != null) lit[wrong] = 'bad'; }
  const name = l4Let(x.tri[0]) + (x.tri[1] === 'maj' ? t(' major', '장3화음') : t(' minor', '단3화음')), inv = t(L4_INVW[x.tri[2]][0], L4_INVW[x.tri[2]][1]);
  return (
    <div className="try-box" style={actBox} data-l5="tri">
      <div style={actTitle}>{t('All three notes of a triad', '3화음의 세 음 모두')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>장3화음이나 단3화음이 울려요(두 번). 기본형일 수도, 자리바꿈일 수도 있어요. 세 음을 <b>모두</b> 불러요: <b>위로</b>면 맨 아래부터, <b>아래로</b>면 맨 위부터. 그다음 건반에서 그 순서대로 찾아요.</>
        : <>A major or minor triad sounds (twice), in root position or inverted. Sing <b>all three</b> notes: <b>up</b> from the bottom, or <b>down</b> from the top, as asked. Then find them on the keys in that order.</>}</div>
      {heard && <div style={{textAlign:'center',fontSize:16,fontWeight:900,color:BK.coral,margin:'0 0 6px'}}>{x.dir === 'up' ? t('Sing them up ↑', '위로 불러요 ↑') : t('Sing them down ↓', '아래로 불러요 ↓')}</div>}
      <SpKb lo={-5} hi={16} W={24} H={76} lit={lit} names={done ? Object.fromEntries(n.map(k => [k, l4Let(k)])) : { 0: 'C' }} onTap={tap} label={t('Find the three notes', '세 음 찾기')}/>
      {lwMsg(!heard ? t('Tap ▶ to hear the triad.', '▶를 누르면 3화음이 나와요.') : done ? t(name + ', ' + inv + ': ' + seq.map(l4Let).join(', ') + '. ' + (miss ? 'Found them.' : 'First time!'), name + ', ' + inv + ': ' + seq.map(l4Let).join(', ') + '. ' + (miss ? '찾았어요.' : '한 번에!'))
        : wrong != null ? t('Not that one: sing the three again, ' + (x.dir === 'up' ? 'from the bottom.' : 'from the top.'), '그 음이 아니에요: ' + (x.dir === 'up' ? '맨 아래부터' : '맨 위부터') + ' 세 음을 다시 불러요.') : t('Sing them, then find note ' + (got + 1) + ' of 3.', '부르고, 세 음 중 ' + (got + 1) + '번째를 찾아요.'), done ? BK.green : wrong != null ? BK.coral : undefined)}
      {lwRow(<>
        <button className="ghost-btn" style={lwBtn} onClick={heard && !fixed ? fresh : play}>{!heard ? t('▶ Play a triad', '▶ 3화음 듣기') : fixed ? t('♪ Again', '♪ 다시') : t('▶ Another', '▶ 다른 것')}</button>
        {heard && !fixed && <button className="ghost-btn" style={lwBtn} onClick={play}>{t('♪ Again', '♪ 다시')}</button>}
        {heard && !done && <button className="ghost-btn" style={lwBtn} onClick={() => spPlay(seq.map((k, j) => ({ at: j * 0.8, keys: [k], len: 0.75 })), 90)}>{t('♪ One at a time', '♪ 하나씩')}</button>}
      </>)}
    </div>
  );
}
const L5IvPad = (p) => <L4IvPad {...p} keys={L5_KEYS}/>;
const L5ClapPad = (p) => <L4ClapPad {...p} set={L5_CLAP} bpm={L5_CLAP_BPM} note={l5ClapNote()}/>;

// ── the pictures on paper ──
const l5PicTwo = () => lsRawPic('<ellipse cx="14" cy="16" rx="6" ry="4.4" transform="rotate(-20 14 16)" fill="#e4572e"/><ellipse cx="14" cy="32" rx="6" ry="4.4" transform="rotate(-20 14 32)" fill="#26296b"/><ellipse cx="38" cy="12" rx="6" ry="4.4" transform="rotate(-20 38 12)" fill="#e4572e"/><ellipse cx="38" cy="28" rx="6" ry="4.4" transform="rotate(-20 38 28)" fill="#26296b"/><ellipse cx="62" cy="8" rx="6" ry="4.4" transform="rotate(-20 62 8)" fill="#e4572e"/><ellipse cx="62" cy="24" rx="6" ry="4.4" transform="rotate(-20 62 24)" fill="#26296b"/><path d="M20 16 L32 12 M44 12 L56 8" stroke="#e4572e" stroke-width="2" stroke-dasharray="3 2"/>', [0, 0, 74, 44]);
const l5PicTri = () => lsRawPic('<ellipse cx="16" cy="34" rx="6.5" ry="4.6" transform="rotate(-20 16 34)" fill="#e4572e"/><ellipse cx="36" cy="22" rx="6.5" ry="4.6" transform="rotate(-20 36 22)" fill="#e4572e"/><ellipse cx="56" cy="10" rx="6.5" ry="4.6" transform="rotate(-20 56 10)" fill="#e4572e"/><path d="M22 31 L30 25 M42 19 L50 13" stroke="#26296b" stroke-width="2"/>', [0, 0, 70, 44]);

function l5LbPages(scr = false) {
  const ch = 'listen-5', l4c = bkChapterNo('listen-4');
  const checks4 = [[l4PicIv(), t('I sing and name any interval of the major scale, from any keynote', '어느 으뜸음에서든 장음계의 음정을 부르고 이름을 말해요')], [l5PicTwo(), t('I sing the higher or the lower part of three intervals', '세 음정에서 윗성부나 아랫성부를 불러요')],
    [l5PicTri(), t('I sing all three notes of a triad, up or down', '3화음의 세 음을 위로나 아래로 모두 불러요')], [l4PicClap(), t('I tap back a passage with triplets and syncopation, and say two or three', '셋잇단음표와 당김음이 있는 리듬을 따라 치고 두 박인지 세 박인지 말해요')]];
  const pen = (x) => <PenArt shapes={x.shapes} vb={x.vb} style={{width:90}}/>;
  const toc = [[t('Any interval, any keynote', '어느 으뜸음에서든, 어떤 음정이든'), 2], [t('Three intervals: sing one part', '세 음정: 한 성부를 불러요'), 3], [t('All three notes of a triad', '3화음의 세 음 모두'), 4], [t('Clap it back: two or three?', '따라 치고, 두 박? 세 박?'), 5], [t('My four checks', '나의 네 가지 확인'), 6]];
  const ivRow = (k) => <div style={{width:'100%',maxWidth:560,margin:'0 auto'}}><SpKb maxW={560} lo={Math.min(0, k)} hi={Math.max(14, k + 12)} W={scr ? 26 : 34} H={scr ? 66 : 84} lit={Object.fromEntries([0, 2, 4, 5, 7, 9, 11, 12].map((s, j) => [k + s, j === 0 ? 'cor' : 'pale']))} names={Object.fromEntries([0, 2, 4, 5, 7, 9, 11, 12].map((s, j) => [k + s, String(j + 1)]))}/></div>;
  const twoStill = (pr) => <LbPic h={160}><div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr 1fr',gap:12,width:'100%',maxWidth:680,margin:'0 auto'}}>{pr.map((iv, j) => <div key={j}><div style={{textAlign:'center',fontSize:13,fontWeight:900,color:BK.ink,marginBottom:2}}>{t('Interval ' + (j + 1), (j + 1) + '번 음정')}: {l4Let(iv[0])} + {l4Let(iv[1])}</div>{l4Kb({ [iv[0]]: 'pale', [iv[1]]: 'cor' }, { [iv[0]]: l4Let(iv[0]), [iv[1]]: l4Let(iv[1]) }, scr, 0, 12)}</div>)}</div></LbPic>;
  const triStill = (list) => <LbPic h={170}><div style={{display:'grid',gridTemplateColumns:'1fr',gap:scr ? 12 : 16,width:'100%',maxWidth:scr ? 680 : 440,margin:'0 auto'}}>{list.map(([r, q, inv, dir]) => { const n = l4Tri(r, q, inv), sq = dir === 'up' ? n : n.slice().reverse();
    return <div key={r + q + inv + dir}><div style={{textAlign:'center',fontSize:13,fontWeight:900,color:BK.ink,marginBottom:2}}>{l4Let(r)}{q === 'maj' ? t(' major', '장3화음') : t(' minor', '단3화음')}, {t(L4_INVW[inv][0], L4_INVW[inv][1])}: {dir === 'up' ? t('up ↑', '위로 ↑') : t('down ↓', '아래로 ↓')} {sq.map(l4Let).join(' ')}</div>{l4Kb(Object.fromEntries(n.map(k => [k, 'cor'])), Object.fromEntries(n.map(k => [k, l4Let(k)])), scr, -2, 16)}</div>; })}</div></LbPic>;
  return [
    <LbPage key="1" no={1} chId={ch} teacher={<>{t('The Grade 5 aural tests, one step each (Manual of Syllabuses, section 21): the keynote, then any interval of the major scale straight after it, sung and named in full (as Grade 4, chapter ' + l4c + '; here from any keynote); the higher or the lower part of a two-part progression of three successive intervals, within an octave from middle C, played slowly, sung from memory; any major or minor triad, root position or inverted, within an octave: hum or sing all three notes, ascending or descending as required; a passage in duple or triple time played twice, tapped back and named. The app plays and scores the taps and answers; whether a child sang in tune is your ear.', '5급 청음 시험을 한 단계씩(실라버스 21절): 으뜸음 다음에 바로 장음계의 어떤 음정이든 부르고 온전한 이름 말하기(4급, ' + l4c + '장과 같지만 어느 으뜸음에서든); 연속된 세 음정으로 된 두 성부 진행을 천천히 듣고 윗성부나 아랫성부를 외워서 부르기(가운데 도부터 한 옥타브 안); 기본형이나 자리바꿈의 장·단3화음에서 세 음을 묻는 대로 위로나 아래로 모두 부르기(한 옥타브 안); 두 박이나 세 박 리듬을 두 번 듣고 따라 치고 박자 말하기. 앱은 탭과 답을 채점하고, 음정이 맞았는지는 선생님의 귀예요.')}</>}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:50,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{bkChapterName(ch)}</div>
      </div></LbOnly>
      <LbPic h={170}><div style={{width:'100%'}}>{triStill([[7, 'maj', 1, 'up'], [2, 'min', 0, 'down']]).props.children}</div></LbPic>
      <LbSay size={18}>{t('Your ears for Grade 5: intervals from any keynote, three moves in two parts, a whole triad sung, and rhythms with triplets.', '5급의 귀: 어느 으뜸음에서든 음정, 두 성부로 세 걸음, 3화음 전체 부르기, 셋잇단음표가 있는 리듬.')}</LbSay>
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
    <LbPage key="2" no={2} chId={ch} kicker={t('Step 1', '1단계')} title={t('Any interval, any keynote', '어느 으뜸음에서든, 어떤 음정이든')}
      teacher={<>{t('Grade 5, as Grade 4: you sound the keynote, then any note of its major scale straight after it (up to the octave); the child sings it, then names it in full. Played twice. Here the keynote can be any of the twelve, so the scale has to be sung, not remembered on white keys.', '5급, 4급과 같아요: 으뜸음을 울린 다음 바로 그 장음계의 어떤 음이든(옥타브까지) 쳐요. 아이는 그 음을 부르고 온전한 이름을 말해요. 두 번 들려줘요. 여기서는 으뜸음이 열두 음 중 어느 것이든 될 수 있어서, 흰건반으로 외우지 않고 음계를 불러서 찾아야 해요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=1')}>
      <LbLive still={<LbPic h={170}><div style={{width:'100%'}}>{ivRow(3)}</div></LbPic>} live={<L5IvPad/>}/>
      <LbSay>{LANG === 'ko' ? <>으뜸음이 어디든 장음계의 모양은 같아요. 1에서 음계를 불러 올라가 숫자를 찾고, 이름: <b>4도, 5도, 8도는 완전</b>, <b>나머지는 장</b>.</> : <>Wherever the keynote is, the major scale has the same shape. Sing up from 1 to find the number, then the name: <b>the 4th, 5th and octave are perfect</b>; <b>the rest are major</b>.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>선생님이 아무 으뜸음과 다른 음을 두 번 쳐요. 그 음을 불러요.</>, <>으뜸음에서 음계를 올라가며 불러서 숫자를 찾아요.</>, <>온전한 이름을 말해요.</>]
        : [<>Your teacher plays any keynote and another note, twice. Sing the note.</>, <>Sing up the scale from the keynote to find its number.</>, <>Say its full name.</>]}/>
      <LbRemember>{t('Any keynote, the same scale: 4, 5, 8 perfect; 2, 3, 6, 7 major.', '으뜸음이 어디든 같은 음계: 4, 5, 8은 완전, 2, 3, 6, 7은 장음정.')}</LbRemember>
    </LbPage>,
    <LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={t('Three intervals: sing one part', '세 음정: 한 성부를 불러요')}
      teacher={<>{t('Grade 5: three intervals played one after the other, slowly, in two parts, within an octave from middle C; the child sings the higher or the lower part (three notes) from memory, as asked. Played twice. The progressions move in parallel 3rds and 6ths, in contrary motion, or with one part still: follow one line.', '5급: 세 음정을 차례로 천천히, 두 성부로 쳐요(가운데 도부터 한 옥타브 안). 아이는 묻는 대로 윗성부나 아랫성부(세 음)를 외워서 불러요. 두 번 들려줘요. 진행은 나란한 3도와 6도, 반대 방향, 또는 한 성부가 머무는 모양이에요: 한 줄만 따라가요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=2')}>
      <LbLive still={twoStill(L5_TWO[1])} live={<L5TwoPad/>}/>
      <LbSay>{LANG === 'ko' ? <>두 음씩 세 번. 위의 세 음이 <b>윗성부</b>(새), 아래의 세 음이 <b>아랫성부</b>(거북이). 두 성부가 같이 갈 수도, 반대로 갈 수도, 하나는 머물 수도 있어요.</> : <>Two notes together, three times. The top three notes are <b>the higher part</b> (the bird's), the bottom three <b>the lower part</b> (the turtle's). The parts may move together, apart, or one may stay still.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>선생님이 세 음정을 천천히 두 번 쳐요. 윗성부를 불러요.</>, <>이번엔 아랫성부. 어려우면 선생님이 한 성부만 쳐 줘요.</>, <>부른 세 음을 건반에서 찾아요.</>]
        : [<>Your teacher plays the three intervals slowly, twice. Sing the higher part.</>, <>Now the lower part. If it is hard, your teacher plays one part alone.</>, <>Find the three notes you sang on the keys.</>]}/>
      <LbRemember>{t('Two parts, three moves: follow one line.', '두 성부, 세 걸음: 한 줄만 따라가요.')}</LbRemember>
    </LbPage>,
    <LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title={t('All three notes of a triad', '3화음의 세 음 모두')}
      teacher={<>{t('Grade 5: any major or minor triad, in root position or an inversion, played within an octave; the child hums or sings all three notes, ascending or descending as required. Played twice. Ascending starts on the bass note, descending on the top note; inverted, the notes are not root, 3rd, 5th in that order. If it is hard, play the three notes one at a time, then together again.', '5급: 장3화음이나 단3화음을 기본형이나 자리바꿈으로 한 옥타브 안에서 쳐요. 아이는 묻는 대로 세 음을 위로나 아래로 모두 흥얼거리거나 불러요. 두 번 들려줘요. 위로는 베이스 음부터, 아래로는 맨 위 음부터; 자리바꿈이면 근음, 3음, 5음의 순서가 아니에요. 어려우면 세 음을 하나씩 친 다음 다시 함께 쳐 주세요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=3')}>
      <LbLive still={triStill([[7, 'maj', 1, 'up'], [2, 'min', 0, 'down']])} live={<L5TriPad/>}/>
      <LbSay>{LANG === 'ko' ? <>4급에서는 가운데 음만. 이제는 <b>세 음 모두</b>: <b>위로</b>면 맨 아래부터, <b>아래로</b>면 맨 위부터 하나씩.</> : <>At Grade 4, only the middle note. Now <b>all three</b>: <b>up</b> from the bottom, or <b>down</b> from the top, one at a time.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>선생님이 3화음을 두 번 쳐요. 맨 아래 음을 흥얼거려요.</>, <>위로 세 음을 불러요. 그다음 아래로.</>, <>건반에서 그 순서대로 찾아요.</>]
        : [<>Your teacher plays a triad, twice. Hum the bottom note.</>, <>Sing the three notes up. Then down.</>, <>Find them on the keys, in that order.</>]}/>
      <LbRemember>{t('Up from the bottom, down from the top.', '위로는 맨 아래부터, 아래로는 맨 위부터.')}</LbRemember>
    </LbPage>,
    <LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title={t('Clap it back: two or three?', '따라 치고, 두 박? 세 박?')}
      teacher={<>{t('Grade 5, as Grade 4: a passage in duple or triple time played twice; the child taps or claps it back and says whether it is in duple or triple time. The Manual adjusts the difficulty to each grade; these passages add the triplet, the syncopated quaver-crotchet-quaver and four semiquavers (our reading: please check). Listen both times without clapping; count inside.', '5급, 4급과 같아요: 두 박이나 세 박의 리듬을 두 번 쳐요. 아이는 따라 치고 두 박인지 세 박인지 말해요. 실라버스는 급에 맞춰 난이도를 조절하니까, 이번 리듬에는 셋잇단음표, 당김음(8분-4분-8분), 16분음표 넷이 나와요(우리 해석이라 확인 부탁드려요). 두 번 다 손뼉 치지 않고 들으며 속으로 세요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=4')}>
      <LbLive still={<LbPic h={150}><div style={{width:'100%',maxWidth:560,margin:'0 auto'}}>{rqStaffEl(L5_CLAP[0].items, { hearts: false })}</div></LbPic>} live={<L5ClapPad/>}/>
      <LbSay>{LANG === 'ko' ? <>두 번 듣고, 같은 빠르기로 따라 치고, <b>두 박인지 세 박인지</b> 말해요. <b>셋잇단음표</b>는 한 박에 고르게 셋, <b>당김음</b>은 박 사이에서 시작해 박 위로.</> : <>Hear it twice, tap it back at the same speed, then say <b>two or three</b>. <b>A triplet</b>: three even notes in a beat. <b>Syncopation</b>: a note that starts between beats and is held over one.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>선생님이 네 마디를 두 번 쳐요. 듣기만 하며 속으로 세요.</>, <>같은 빠르기로 따라 쳐요.</>, <>두 박이었나요, 세 박이었나요?</>]
        : [<>Your teacher plays four bars, twice. Just listen and count inside.</>, <>Tap it back at the same speed.</>, <>Two or three?</>]}/>
      <LbRemember>{t('Clap it back, then say two or three.', '따라 치고, 두 박인지 세 박인지 말해요.')}</LbRemember>
    </LbPage>,
    <LbPage key="6" no={6} chId={ch} kicker={t('Check-up', '점검')} title={t('My four checks', '나의 네 가지 확인')}
      teacher={<>{t('Each one with you at the piano, away from the screen, played twice as in the exam: you play, the child sings, names or claps. You only correct.', '하나씩 화면 없이 피아노 앞에서, 시험처럼 두 번씩: 선생님이 치고, 아이는 부르고, 이름을 말하고, 손뼉 쳐요. 선생님은 고쳐 주기만 해요.')}</>}>
      <LbSay>{t('Tick each one: not yet, nearly, or got it!', '하나씩 표시해요: 아직, 거의, 됐어요!')}</LbSay>
      <LbLive still={<LbStageRows big rows={checks4.map(([a, txt]) => [pen(a), txt])}/>} live={<FiveChecks376 rows={checks4} storeKey="pb_l5_four"/>}/>
    </LbPage>,
  ];
}
function Listen5LessonBook() { return <>{l5LbPages(false)}</>; }
function L5Learn({ onStart }) {
  const pages = l5LbPages(true), opener = pages[0];
  return (
    <Lesson id="listen-5" title={bkChapterName('listen-5')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="listen-5"><div className="lb-screen lb-open" style={{display:'flex',flexDirection:'column',gap:12,margin:'0 0 8px'}}>{lbWordsFirst(opener.props.children)}</div></BkChapterCtx.Provider></LbScreenCtx.Provider>}>
      {pages.slice(1).map((pg, i) => <Step key={i} title={pg.props.title}><LbScreenPage page={pg}/></Step>)}
    </Lesson>
  );
}
// ── the drill: every question is heard (twice, as the tests are) ──
const L5_LEVELS = [
  { n: 1, label: 'Any keynote: name the interval', kind: 'iv', time: 20 },
  { n: 2, label: 'Three intervals: sing the higher or the lower part', kind: 'two', time: 50 },
  { n: 3, label: 'A triad: sing all three notes, up or down', kind: 'tri', time: 40 },
  { n: 4, label: 'Clap it back, then two or three (Grade 5)', kind: 'clap', time: 45 },
  { n: 5, label: 'All four, mixed, as in the Grade 5 exam', kind: 'mix', time: 50 },
];
Object.assign(LEVEL_KO, { 'Any keynote: name the interval': '어느 으뜸음에서든: 음정 이름', 'Three intervals: sing the higher or the lower part': '세 음정: 윗성부나 아랫성부 부르기', 'A triad: sing all three notes, up or down': '3화음: 세 음을 위로나 아래로', 'Clap it back, then two or three (Grade 5)': '따라 치고, 두 박? 세 박? (5급)', 'All four, mixed, as in the Grade 5 exam': '네 가지 섞어서, 5급 시험처럼' });
function genL5Question(lv, prev) {
  const uid = Math.random(); let kind = lv.kind;
  if (kind === 'mix') { const ks = ['iv', 'two', 'tri', 'clap'].filter(k => !prev || prev.kind !== k); kind = pick(ks); }
  if (kind === 'iv') { let k, n, g = 0; do { k = pick(L5_KEYS); n = pick([2, 3, 4, 5, 6, 7, 8]); } while (prev && prev.key === k + '-' + n && g++ < 10); return { kind, k, n, answer: n, choices: [2, 3, 4, 5, 6, 7, 8], key: k + '-' + n, uid }; }
  if (kind === 'two') { let pr, ask, g = 0; do { pr = pick(L5_TWO); ask = Math.random() < 0.5 ? 'hi' : 'lo'; } while (prev && prev.key === JSON.stringify(pr) + ask && g++ < 10); return { kind, fx: { pr, ask }, answer: 'ok', choices: [], key: JSON.stringify(pr) + ask, uid }; }
  if (kind === 'tri') { let x, dir, g = 0; do { x = pick(L5_TRIS); dir = Math.random() < 0.5 ? 'up' : 'down'; } while (prev && prev.key === x.join() + dir && g++ < 10); return { kind, fx: { tri: x, dir }, answer: 'ok', choices: [], key: x.join() + dir, uid }; }
  let i, g = 0; do { i = Math.floor(Math.random() * L5_CLAP.length); } while (prev && prev.i === i && g++ < 10); return { kind: 'clap', i, answer: 'ok', choices: [], key: 'c' + i, uid };
}
function L5Question({ q, given, locked, onAnswer, pixel }) {
  const done = !!given;
  const play = () => { stopClicks(); if (q.kind === 'iv') l4PlayIv(q.k, L4_IV.find(y => y[0] === q.n)[1]); };
  useEffect(() => { if (q.kind !== 'iv') return; const id = setTimeout(play, 350); return () => { clearTimeout(id); stopClicks(); }; }, [q.uid]);
  const btnCls = pixel ? 'pixel-choice' : 'choice-btn', cls = (c) => btnCls + (!done ? '' : c === q.answer ? ' good' : given.ans === c ? ' bad' : '');
  const pickIt = (c) => { if (locked || done) return; stopClicks(); onAnswer(c); };
  let title, body;
  if (q.kind === 'iv') { title = t('The keynote, then a note of its major scale: name the interval.', '으뜸음, 그다음 그 장음계의 음: 음정 이름은?');
    body = <div style={{display:'grid',gridTemplateColumns:'repeat(4,minmax(0,1fr))',gap:6}}>{[2, 3, 4, 5, 6, 7, 8].map(c => <button key={c} disabled={locked} className={cls(c)} style={{padding:'10px 2px',fontSize:13.5,fontWeight:900,lineHeight:1.15}} onClick={() => pickIt(c)}>{l4IvName(c)}</button>)}</div>; }
  else if (q.kind === 'two') { title = q.fx.ask === 'hi' ? t('Sing the higher part, then find its three notes.', '윗성부를 부르고, 세 음을 찾아요.') : t('Sing the lower part, then find its three notes.', '아랫성부를 부르고, 세 음을 찾아요.'); body = <L5TwoPad key={q.uid} fixed={q.fx} onResult={(r) => pickIt(r.ok ? 'ok' : 'no')}/>; }
  else if (q.kind === 'tri') { title = q.fx.dir === 'up' ? t('Sing the three notes up, then find them.', '세 음을 위로 부르고, 찾아요.') : t('Sing the three notes down, then find them.', '세 음을 아래로 부르고, 찾아요.'); body = <L5TriPad key={q.uid} fixed={q.fx} onResult={(r) => pickIt(r.ok ? 'ok' : 'no')}/>; }
  else { title = t('Listen twice, clap it back, then say two or three.', '두 번 듣고, 따라 치고, 두 박인지 세 박인지 말해요.'); body = <L5ClapPad key={q.uid} fixed={q.i} onResult={(r) => pickIt(r.ok ? 'ok' : 'no')}/>; }
  const why = !done ? null : q.kind === 'iv' ? t(l4Let(q.k) + ' to ' + l4Let(q.k + L4_IV.find(y => y[0] === q.n)[1]) + ': a ' + l4IvName(q.n) + ' (in a major scale, 4, 5, 8 perfect; 2, 3, 6, 7 major).', l4Let(q.k) + '에서 ' + l4Let(q.k + L4_IV.find(y => y[0] === q.n)[1]) + ': ' + l4IvName(q.n) + '(장음계에서 4, 5, 8은 완전, 2, 3, 6, 7은 장음정).') : null;
  return (<div>
    <p style={pixel ? {fontSize:11.5,textAlign:'center'} : {fontSize:15,fontWeight:700,textAlign:'center',margin:'0 0 8px',color:'var(--muted)',textWrap:'balance'}}>{title}</p>
    {q.kind === 'iv' && <div style={{textAlign:'center',marginBottom:10}}><button className={pixel ? 'pixel-btn' : 'ghost-btn'} style={{minHeight:44}} onClick={play}>{t('▶ Play it again', '▶ 다시 듣기')}</button></div>}
    {body}
    {why && !pixel && <div style={{marginTop:10,fontSize:13.5,color:'#4a4d86',background:'#fff',borderRadius:8,padding:'7px 10px',lineHeight:1.45}}>{why}</div>}
  </div>);
}
Object.assign(LISTEN_5_DRILL, { levels: L5_LEVELS, generate: genL5Question, check: (q, ans) => ans !== null && ans !== undefined && ans === q.answer, answerLabel: l4AnswerLabel, Question: L5Question, Learn: L5Learn });
// the teacher's copy (no Workbook: every step is by ear)
function L5Teacher() {
  const pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="listen-5" teacher>{content}</WbPage>);
  const lt = (i) => { const pc = ((i % 12) + 12) % 12, nm = ['C', 'C♯', 'D', 'E♭', 'E', 'F', 'F♯', 'G', 'A♭', 'A', 'B♭', 'B'][pc]; return i < 0 ? nm + ',' : nm + (i >= 12 ? "'" : ''); };   // B, = below middle C; C' = the C above
  const iv = (k, n) => lt(k) + ' then ' + lt(k + L4_IV.find(y => y[0] === n)[1]) + ': ' + L4_IVN[n][0];
  const two = (pr) => pr.map(([a, b]) => lt(a) + '+' + lt(b)).join(' → ') + ' (higher ' + pr.map(p => lt(p[1])).join(' ') + '; lower ' + pr.map(p => lt(p[0])).join(' ') + ')';
  const tri = ([r, q, inv], dir) => { const n = l4Tri(r, q, inv), sq = dir === 'up' ? n : n.slice().reverse(); return n.map(lt).join(' ') + ' (' + lt(r).replace(/[,']/g, '') + (q === 'maj' ? ' major, ' : ' minor, ') + L4_INVW[inv][0] + '): ' + dir + ' ' + sq.map(lt).join(' '); };
  P(<>
    <div style={{fontFamily:LB_SERIF,fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('listen-5')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 12px',lineHeight:1.5}}>No Workbook for this chapter: every step is by ear, as the Grade 5 aural tests ask. Each block faces its Lesson Book page and gives you material to play, the same as the app uses. Play every test twice, as the examiner does. Middle C is C here; the C above is C'; notes below middle C carry a comma (B♭,).</div>
    <TcBlock page={2} title="Any interval, any keynote" answers={<>{tcAns('PLAY', [[3, 6], [-2, 4], [6, 7], [1, 3], [-4, 5], [4, 8], [-1, 2], [5, 6]].map(([k, n]) => iv(k, n)))}</>}
      watch="The scale sung on white keys from a black keynote (E♭ major sung as E♭ F G A♭ is right; E♭ F G A is not). Sing up from 1 every time until the shape is in the ear."
      say="“Any keynote, the same scale: 4, 5, 8 perfect; 2, 3, 6, 7 major.”"/>
    <TcBlock page={3} title="Three intervals: sing one part" answers={<>{tcAns('PLAY SLOWLY', L5_TWO.slice(0, 8).map(two))}</>}
      watch="Jumping to the other part on the third interval, where the parts cross or one stays still. Ask for the lower part as often as the higher."
      say="“Two parts, three moves: follow one line.”"/>
  </>);
  P(<>
    <TcBlock page={4} title="All three notes of a triad" answers={<>{tcAns('PLAY', L5_TRIS.slice(0, 10).map((x, j) => tri(x, j % 2 ? 'down' : 'up')))}</>}
      watch="Root, 3rd, 5th sung whatever the position: an inverted triad sung up starts on its bass note, which is not the root. Down: start on the top note."
      say="“Up from the bottom, down from the top.”"/>
    <TcBlock page={5} title="Clap it back: two or three?" answers={<><div style={{fontSize:10.5,fontWeight:900,color:BK.muted,letterSpacing:'0.06em',marginBottom:4}}>{spTx('PLAY TWICE, THEN THE CHILD TAPS AND SAYS TWO OR THREE (♩ = ' + L5_CLAP_BPM + ')')}</div>
      <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:'4px 14px'}}>{L5_CLAP.map((row, i) => <div key={i} style={{display:'flex',alignItems:'center',gap:6}}>{nvNum(i + 1)}<div style={{flex:1,minWidth:0}}>{rqStaffEl(row.items, { counts: false, hearts: false })}</div></div>)}</div></>}
      watch="The triplet clapped as a quaver pair and a quaver; the syncopated crotchet clapped on the beat. Count the beat aloud the first time."
      say="“Clap it back, then say two or three.”"/>
    <TcBlock page={6} title="My four checks" answers={<div style={{fontSize:12,color:BK.ink,lineHeight:1.5}}>Each one with you at the piano, away from the screen, played twice: you play, the child sings, names or claps. Use material the child has not heard this week. The drill's level 5 mixes all four, as the exam does.</div>}/>
  </>);
  return <>{pages}</>;
}
TEACHER_COPIES['listen-5'] = L5Teacher;
'''
rep("""TEACHER_COPIES['listen-4'] = L4Teacher;""", """TEACHER_COPIES['listen-4'] = L4Teacher;""" + CH)

HOME = r'''
// ══ Build AZ: Hear and Sing, Grade 5 on the Home (the Aural door) ══
LBH_FN['listen-5'] = (s) => l5LbPages(s);
const l5Add = (id, i, en, ko, benEn, bko, make) => { const spec = lbhSpec('listen-5', i, { make });
  TOOLS.push({ id, ch: 'concept', title: en, blurb: benEn, hidden: true, get kicker() { return t('Aural', '청음') + ' · ' + t('Hear and sing, Grade 5', '듣고 부르기, Grade 5'); }, C: () => <KqEngine spec={spec}/> });
  lbhRetitle(id, en, ko, benEn, bko); };
const l5IvQ = (n, prev) => { let k, dg, g = 0; do { k = pick(L5_KEYS); dg = pick([2, 3, 4, 5, 6, 7, 8]); } while (prev && prev.key === k + '-' + dg && g++ < 10); const d = L4_IV.find(y => y[0] === dg)[1];
  return { kind: 'choice', cols: 3, prompt: ['The keynote, then a note: sing it, then name it.', '으뜸음, 그다음 음: 부르고, 이름을 말해요.'], opts: [2, 3, 4, 5, 6, 7, 8].map(x => ({ id: x, label: () => l4IvName(x) })), ans: dg, ok: (v) => v === dg,
    key: k + '-' + dg, play: () => l4PlayIv(k, d),
    fig: (c) => ({ mid: c.res ? <SpKb lo={Math.min(0, k)} hi={Math.max(14, k + 12)} W={24} H={72} lit={{ [k]: 'pale', [k + d]: c.res === 'ok' ? 'good' : 'cor' }} names={Object.fromEntries([0, 2, 4, 5, 7, 9, 11, 12].map((s, j) => [k + s, String(j + 1)]))}/> : null }),
    yes: ['Yes: a ' + L4_IVN[dg][0] + '.', '맞아요: ' + L4_IVN[dg][1] + '.'], no: ['It was a ' + L4_IVN[dg][0] + ': 4, 5, 8 perfect; 2, 3, 6, 7 major.', L4_IVN[dg][1] + '였어요: 4, 5, 8은 완전, 2, 3, 6, 7은 장음정.'] }; };
l5Add('l5-iv', 1, 'Any interval, any keynote', '어느 으뜸음에서든, 어떤 음정이든', 'From any of the twelve keynotes: sing it, then name it in full.', '열두 으뜸음 어디서든: 부르고, 온전한 이름 말하기.', l5IvQ);
l5Add('l5-two', 2, 'Three intervals: sing one part', '세 음정: 한 성부를 불러요', 'Three intervals in two parts, slowly: sing the higher or the lower.', '두 성부의 세 음정, 천천히: 윗성부나 아랫성부 부르기.', lwTapQ(L5TwoPad, (n) => ({ fixed: { pr: L5_TWO[(n * 5) % L5_TWO.length], ask: n % 2 ? 'lo' : 'hi' } }), ['Hear the two parts, sing the one asked, then find its notes.', '두 성부를 듣고, 묻는 성부를 부르고, 음을 찾아요.'], ['Sung and found ✓', '부르고 찾았어요 ✓']));
l5Add('l5-tri', 3, 'All three notes of a triad', '3화음의 세 음 모두', 'Root position or inverted: sing all three, up or down.', '기본형이든 자리바꿈이든: 세 음을 위로나 아래로.', lwTapQ(L5TriPad, (n) => ({ fixed: { tri: L5_TRIS[(n * 3) % L5_TRIS.length], dir: n % 2 ? 'down' : 'up' } }), ['Hear the triad, sing the three notes, then find them in order.', '3화음을 듣고, 세 음을 부르고, 차례로 찾아요.'], ['Sung and found ✓', '부르고 찾았어요 ✓']));
l5Add('l5-clap', 4, 'Clap it back: two or three? (Grade 5)', '따라 치고, 두 박? 세 박? (5급)', 'Triplets and syncopation: heard twice, clapped back, named.', '셋잇단음표와 당김음: 두 번 듣고, 따라 치고, 박자 말하기.', lwTapQ(L5ClapPad, (n) => ({ fixed: n % L5_CLAP.length }), ['Listen twice, tap it back, then say two or three.', '두 번 듣고, 따라 치고, 두 박인지 세 박인지 말해요.'], ['Clapped back and named ✓', '따라 치고 맞혔어요 ✓']));
'''
rep("""
lbhAdd('rb-finger', 'r-beat', 'rhythm', 'The beat in your fingers'""", HOME + """
lbhAdd('rb-finger', 'r-beat', 'rhythm', 'The beat in your fingers'""")
# the Home: the Aural door gains the Grade 5 room; the floor marks
rep("""    { id: 'au-4', en: 'Hear and sing, Grade 4', ko: '듣고 부르기, Grade 4', lessons: ['l4-iv', 'l4-two', 'l4-mid', 'l4-clap'], check: 'listen-4' },""",
    """    { id: 'au-4', en: 'Hear and sing, Grade 4', ko: '듣고 부르기, Grade 4', lessons: ['l4-iv', 'l4-two', 'l4-mid', 'l4-clap'], check: 'listen-4' },
    { id: 'au-5', en: 'Hear and sing, Grade 5', ko: '듣고 부르기, Grade 5', lessons: ['l5-iv', 'l5-two', 'l5-tri', 'l5-clap'], check: 'listen-5' },   // Build AZ""")
rep("""  set('4', 'l4-iv l4-two l4-mid l4-clap');   // Build AR: Hear and Sing, Grade 4""", """  set('4', 'l4-iv l4-two l4-mid l4-clap');   // Build AR: Hear and Sing, Grade 4
  set('5', 'l5-iv l5-two l5-tri l5-clap');   // Build AZ: Hear and Sing, Grade 5""")
# the books and the house
rep("""const LESSON_BOOKS = { 'rhythm-4': Rhythm4LessonBook,""", """const LESSON_BOOKS = { 'listen-5': Listen5LessonBook, 'rhythm-4': Rhythm4LessonBook,""")
rep("""const LB_PAGE_FNS = { 'rhythm-4': r4LbPages,""", """const LB_PAGE_FNS = { 'listen-5': l5LbPages, 'rhythm-4': r4LbPages,""")
rep("""const HOUSE_ICONS = {""", """const HOUSE_ICONS = {"listen-5": "<path d=\\"M8 15C3 21 3 29 8 35M15 19C12 22 12 28 15 31\\"/><ellipse cx=\\"24\\" cy=\\"34\\" rx=\\"5\\" ry=\\"3.7\\" transform=\\"rotate(-20 24 34)\\" fill=\\"#e4572e\\" stroke=\\"#e4572e\\"/><ellipse cx=\\"32\\" cy=\\"25\\" rx=\\"5\\" ry=\\"3.7\\" transform=\\"rotate(-20 32 25)\\" fill=\\"#e4572e\\" stroke=\\"#e4572e\\"/><ellipse cx=\\"40\\" cy=\\"16\\" rx=\\"5\\" ry=\\"3.7\\" transform=\\"rotate(-20 40 16)\\" fill=\\"#e4572e\\" stroke=\\"#e4572e\\"/>", """)
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
