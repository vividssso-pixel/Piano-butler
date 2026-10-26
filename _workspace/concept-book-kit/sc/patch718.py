import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build AY: a melody for a couplet (Theory of Music Grade 4: a melody to a couplet, in a major or minor key). A lesson in the
# Melody room, marked Grade 4, after Writing a melody: the couplet's words set the rhythm the way Words and rhythm does (a bar
# line before each strong syllable, an anacrusis when the line starts weak), the child writes a note for every syllable in a major
# key or a harmonic minor key (up to two sharps or flats), the words sit under the notes, line 1 asks and line 2 answers.
# The staff of Writing a melody learns any number of bars, two lines of words, slot-based phrase marks and the raised 7th's sharp.

# ── the keys: the five minor keys up to two sharps or flats (harmonic: the 7th raised) ──
rep("""  F: { t: 31, n: 1, s: 'flat', en: 'F major', ko: 'F장조' }, Bb: { t: 34, n: 2, s: 'flat', en: 'B♭ major', ko: 'B♭장조' },
};""", """  F: { t: 31, n: 1, s: 'flat', en: 'F major', ko: 'F장조' }, Bb: { t: 34, n: 2, s: 'flat', en: 'B♭ major', ko: 'B♭장조' },
  Am: { t: 33, n: 0, s: null, en: 'A minor', ko: 'A단조', minor: true }, Em: { t: 30, n: 1, s: 'sharp', en: 'E minor', ko: 'E단조', minor: true }, Bm: { t: 34, n: 2, s: 'sharp', en: 'B minor', ko: 'B단조', minor: true },
  Dm: { t: 29, n: 1, s: 'flat', en: 'D minor', ko: 'D단조', minor: true }, Gm: { t: 32, n: 2, s: 'flat', en: 'G minor', ko: 'G단조', minor: true },   // Build AY: harmonic minor
};""")
rep("""const mwAlt = (d, k) => { const K = MW_KEYS[k]; if (!K.s) return 0; const sig = (K.s === 'sharp' ? SHARP_ORDER : FLAT_ORDER).slice(0, K.n).map(x => x[0]); return sig.includes(mwLet(d)) ? (K.s === 'sharp' ? 1 : -1) : 0; };""",
    """const mwAlt = (d, k) => { const K = MW_KEYS[k], up = K.minor && ((d - K.t) % 7 + 7) % 7 === 6 ? 1 : 0; if (!K.s) return up; const sig = (K.s === 'sharp' ? SHARP_ORDER : FLAT_ORDER).slice(0, K.n).map(x => x[0]); return (sig.includes(mwLet(d)) ? (K.s === 'sharp' ? 1 : -1) : 0) + up; };   // Build AY: the harmonic minor's raised 7th""")

# ── the staff: any number of bars, in lines; phrase marks by slot; words under the notes; the raised 7th's sharp ──
rep("""  return { all, ids, xs, bars, end: x + 4, W: x + 16 };
}""", """  return { all, ids, xs, bars, end: x + 4, W: x + 16, b0, b1 };
}""")
i0 = s.index('function MwStaff({ k, rh, notes = [], cur = null,')
assert s.count('function MwStaff({ k, rh, notes = [], cur = null,') == 1
i1 = s.index('\n}\n', i0) + 3
NEW_STAFF = r'''function MwStaff({ k, rh, notes = [], cur = null, lit = -1, hl = [], phr = null, onSlot, empty, per = 4, sp = 1, label, words = null }) {
  const R = mwRh(rh), K = MW_KEYS[k], sig = K.s ? (K.s === 'sharp' ? SHARP_ORDER : FLAT_ORDER).slice(0, K.n) : [], GH = 'rgba(38,41,107,0.26)', nB = R.bars.length;
  // Build AY: the lines of the staff: R.lines (a couplet: one line of words each), each cut into rows of per bars (an anacrusis rides along)
  const segs = []; (R.lines || [[0, nB - 1]]).forEach(([r0, r1]) => { let b = r0, first = true; while (b <= r1) { const size = per + (first && R.ana && b === 0 ? 1 : 0); segs.push([b, Math.min(r1, b + size - 1)]); b += size; first = false; } });
  const lines = segs.map(([b0, b1]) => mwLine(k, R, b0, b1, b0 === 0, sp));
  const Wmax = Math.max(...lines.map(L => L.W));
  const all = lines[0].all, dOf = (i) => notes[i] != null ? notes[i] : 34, colOf = (i) => i === lit || hl.includes(i) ? PEN_C : notes[i] != null ? PEN_N : GH;
  const upOf = (i) => { const s = all[i]; if (s.k === 'e') { const j = s.beam ? i - 1 : i; return (dOf(j) + dOf(j + 1)) / 2 < 34; } return dOf(i) < 34; };
  const slotR = (b0, b1) => { const ix = all.map((_, i) => i).filter(i => all[i].b >= b0 && all[i].b <= b1); return [ix[0], ix[ix.length - 1]]; };
  const ranges = phr === '22' ? [slotR(0, 1), slotR(2, 3)] : phr === '4' ? [slotR(0, nB - 1)] : phr === 'lines' && R.phr ? R.phr : [];   // slot ranges
  const raised = (d) => !!K.minor && ((d - K.t) % 7 + 7) % 7 === 6;
  const one = (L, li) => { const els = [], shown = {};
    let yA = dY(38) - 12, yB = dY(30) + 10;   // what the line holds, top and bottom
    const ext = (a, b) => { yA = Math.min(yA, a); yB = Math.max(yB, b); };
    if (cur != null && L.xs[cur] != null && !empty) els.push(<rect key="cu" x={L.xs[cur] - 12} y={dY(40)} width="24" height={dY(28) - dY(40)} rx="4" fill="#fbe3da"/>);
    [30, 32, 34, 36, 38].forEach(l => els.push(<line key={'l' + l} x1="4" x2={L.W - 4} y1={dY(l)} y2={dY(l)} stroke={PEN_N} strokeOpacity="0.55" strokeWidth="1.2"/>));
    els.push(<ClefGlyph key="cl" clef="treble" st="treble" yOf={dY} ink={PEN_N}/>);
    sig.forEach((a, j) => { const pos = (K.s === 'sharp' ? SHARP_POS : FLAT_POS)[a], x = 46 + j * 10, y = dY(30 + pos); els.push(K.s === 'sharp' ? <SharpShape key={'k' + j} x={x} y={y} color={PEN_N}/> : <FlatShape key={'k' + j} x={x} y={y} color={PEN_N}/>); });
    if (li === 0) [[R.m, dY(36)], [4, dY(32)]].forEach(([n, y], j) => els.push(<text key={'t' + j} x={46 + K.n * 10 + 13} y={y + 7.6} textAnchor="middle" fontFamily="Playfair Display, Georgia, serif" fontSize="25" fontWeight="900" fill={PEN_N}>{n}</text>));
    L.bars.forEach((bx, j) => els.push(<line key={'b' + j} x1={bx} x2={bx} y1={dY(38)} y2={dY(30)} stroke={PEN_N} strokeWidth="1.5"/>));
    if (L.b1 === nB - 1) els.push(<line key="e1" x1={L.end} x2={L.end} y1={dY(38)} y2={dY(30)} stroke={PEN_N} strokeWidth="1.3"/>, <line key="e2" x1={L.end + 5} x2={L.end + 5} y1={dY(38)} y2={dY(30)} stroke={PEN_N} strokeWidth="3.8"/>);
    else els.push(<line key="e1" x1={L.end} x2={L.end} y1={dY(38)} y2={dY(30)} stroke={PEN_N} strokeWidth="1.5"/>);
    if (!empty) L.ids.forEach(i => { const s = all[i], d = dOf(i), x = L.xs[i], y = dY(d), c = colOf(i), up = upOf(i), hollow = s.k === 'h' || s.k === 'hd' || s.k === 'w';
      ext(up && s.k !== 'w' ? y - 34 : y - 8, !up && s.k !== 'w' ? y + 34 : y + 8);
      if (notes[i] != null) ledgersFor(d, 30, 38).forEach(p => els.push(<line key={'lg' + i + '_' + p} x1={x - 11} x2={x + 11} y1={dY(p)} y2={dY(p)} stroke={PEN_N} strokeWidth="1.3"/>));
      if (notes[i] != null && raised(d) && !shown[s.b + ':' + d]) { shown[s.b + ':' + d] = 1; els.push(<SharpShape key={'ac' + i} x={x - 16} y={y} color={c}/>); }   // the raised 7th: once a bar
      els.push(<ellipse key={'h' + i} cx={x} cy={y} rx="6.6" ry="4.8" transform={`rotate(-20 ${x} ${y})`} fill={hollow ? '#fff' : c} stroke={c} strokeWidth={hollow ? 2.2 : 1}/>);
      if (s.k === 'hd') els.push(<circle key={'dt' + i} cx={x + 12} cy={(d - 30) % 2 === 0 ? y - 5 : y} r="2.4" fill={c}/>);
      if (s.k === 'q' || s.k === 'h' || s.k === 'hd') els.push(<line key={'s' + i} x1={up ? x + 6 : x - 6} x2={up ? x + 6 : x - 6} y1={y + (up ? -1 : 1)} y2={y + (up ? -32 : 32)} stroke={c} strokeWidth="1.7"/>);
      if (s.k === 'e' && !s.beam) { const j = i + 1, x2 = L.xs[j], y2 = dY(dOf(j)), by = up ? Math.min(y, y2) - 30 : Math.max(y, y2) + 30, sx1 = up ? x + 6 : x - 6, sx2 = up ? x2 + 6 : x2 - 6;
        els.push(<line key={'s' + i} x1={sx1} x2={sx1} y1={y + (up ? -1 : 1)} y2={by} stroke={c} strokeWidth="1.7"/>, <line key={'s' + j} x1={sx2} x2={sx2} y1={y2 + (up ? -1 : 1)} y2={by} stroke={colOf(j)} strokeWidth="1.7"/>,
          <line key={'bm' + i} x1={sx1 - 0.8} x2={sx2 + 0.8} y1={by + (up ? 2.2 : -2.2)} y2={by + (up ? 2.2 : -2.2)} stroke={notes[i] != null && notes[j] != null ? (i === lit || j === lit ? PEN_C : PEN_N) : GH} strokeWidth="4.6"/>); }
    });
    if (!empty) ranges.forEach(([r0, r1], r) => { const ids = L.ids.filter(i => i >= r0 && i <= r1); if (!ids.length) return;
      const tops = ids.map(i => { const y = dY(dOf(i)); return upOf(i) && all[i].k !== 'w' ? y - 33 : y - 8; });
      const ya = Math.min(dY(39), ...tops) - 7, openL = r0 < L.ids[0], openR = r1 > L.ids[L.ids.length - 1], x1 = openL ? 46 + K.n * 10 + 4 : L.xs[ids[0]] - 3, x2 = openR ? L.end - 2 : L.xs[ids[ids.length - 1]] + 5;
      const y1 = openL ? ya - 6 : ya + 7, y2 = openR ? ya - 6 : ya + 7; ext(ya - 14, ya);
      els.push(<path key={'ph' + r} d={`M${x1} ${y1} C${x1 + (openL ? 0 : 14)} ${ya - 12} ${x2 - (openR ? 0 : 14)} ${ya - 12} ${x2} ${y2}`} fill="none" stroke={PEN_N} strokeWidth="2" strokeLinecap="round"/>); });
    if (words && !empty) { const wy = Math.max(yB, dY(28) + 6) + 15; L.ids.forEach(i => { if (words[i]) els.push(<text key={'w' + i} x={L.xs[i] + (all[i].k === 'e' ? 0 : 2)} y={wy} textAnchor="middle" fontSize="12" fontWeight={i === lit ? 900 : 700} fill={i === lit ? PEN_C : PEN_N} fontFamily="Inter, sans-serif">{words[i]}</text>); }); ext(wy - 11, wy + 4); }   // Build AY
    if (cur != null && L.xs[cur] != null && !empty) { const x = L.xs[cur], y = Math.max(yB, dY(28) + 8) + 4; ext(y, y + 10); els.push(<path key="tri" d={`M${x - 6} ${y + 8} L${x + 6} ${y + 8} L${x} ${y} Z`} fill={PEN_C}/>); }
    if (onSlot && !empty) L.ids.forEach(i => els.push(<rect key={'tap' + i} data-mw-slot={i} x={L.xs[i] - 12} y={dY(42)} width="24" height={dY(26) - dY(42)} fill="transparent" style={{cursor:'pointer'}} onClick={() => onSlot(i)}/>));
    return <svg key={li} viewBox={`0 ${yA - 3} ${L.W} ${yB - yA + 6}`} style={{width:(L.W / Wmax * 100) + '%',display:'block',margin:'0 auto 6px 0'}} role="img" aria-label={label || t('A four-bar melody on the staff.', '오선 위의 4마디 선율.')}>{els}</svg>; };
  return <div style={{width:'100%',maxWidth:Math.round(Wmax * 1.35),margin:'0 auto'}} data-mw-staff={k}>{lines.map(one)}</div>;
}
'''
s = s[:i0] + NEW_STAFF + s[i1:]

# ── the couplets set as rhythms (the words decide), one model melody each in scale degrees (1 the tonic; 1 to 6 keep every key
# in the keyboard's range), and the pad ──
CODE = r'''
// ─── Build AY: a melody for a couplet (Grade 4) ───
const MW_CPL_MODEL = {   // line 1 rests away from the tonic (a question); line 2 ends on it
  kites: [3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 3, 4, 2, 1],
  snow: [1, 2, 3, 4, 5, 4, 2, 3, 4, 5, 3, 2, 2, 1],
  boat: [5, 3, 2, 1, 2, 3, 4, 5, 5, 6, 5, 4, 3, 4, 2, 1],
  hills: [1, 2, 3, 4, 5, 4, 3, 2, 3, 5, 6, 5, 4, 3, 4, 5, 4, 3, 2, 1],
  moon: [1, 2, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 3, 4, 2, 1],
};
const MW_CPL = {};
MW_POEMS.forEach(P => { const s1 = MW_SYL[P.id][0], syls = s1.concat(MW_SYL[P.id][1]), set = mwSet(syls, P.m, mwStarts(syls), { per: 99 }); if (!set) return;
  let si = 0, qb = 0; set.rhy.forEach((bar, b) => bar.forEach(kk => { for (let u = 0; u < (kk === 'p' ? 2 : 1); u++) { if (si === s1.length - 1) qb = b; si++; } }));
  const nB = set.rhy.length;
  MW_CPL[P.id] = { id: 'c-' + P.id, m: P.m, bars: set.rhy, ana: set.a || 0, lines: [[0, qb], [qb + 1, nB - 1]], qi: s1.length - 1, phr: [[0, s1.length - 1], [s1.length, syls.length - 1]], words: syls.map(mwTx), model: MW_CPL_MODEL[P.id] }; });
const MW_CPL_IDS = MW_POEMS.map(p => p.id).filter(id => MW_CPL[id]);
const MW_KEY_MAJ = ['C', 'G', 'D', 'F', 'Bb'], MW_KEY_MIN = ['Am', 'Em', 'Bm', 'Dm', 'Gm'];
const mwBarAt = (R, b) => (R.ana ? (b === 0 ? 0 : R.ana + (b - 1) * R.m) : b * R.m);
const mwModelC = (k, R) => R.model.map(dg => MW_KEYS[k].t + dg - 1);
function mwRulesC(notes, R, k, phr) {
  const n = notes.length, deg = (d) => mwDeg(d, k), filled = notes.filter(d => d != null).length, moves = [];
  for (let i = 1; i < n; i++) if (notes[i] != null && notes[i - 1] != null) moves.push(Math.abs(notes[i] - notes[i - 1]));
  const steps = moves.filter(m => m <= 1).length;
  return [
    ['start', notes[0] == null ? null : [1, 3, 5].includes(deg(notes[0]))],
    ['steps', filled < n ? (moves.length >= 6 && steps * 2 < moves.length ? false : null) : steps * 2 >= moves.length],
    ['q', notes[R.qi] == null ? null : deg(notes[R.qi]) !== 1],
    ['end', notes[n - 1] == null ? null : deg(notes[n - 1]) === 1],
    ['phr', phr === 'lines' ? true : null],
  ];
}
const MW_RULE_C = {
  start: MW_RULE_W.start, steps: MW_RULE_W.steps,
  q: ['Line 1 ends away from the tonic: a question', '첫 줄은 으뜸음이 아닌 음에서 끝나요: 질문'], end: ['Line 2 ends on the tonic: the answer', '둘째 줄은 으뜸음에서 끝나요: 대답'], phr: ['A phrase mark over each line', '줄마다 프레이즈 표시'],
};
const mwCplChip = (id) => mwPlain(mwPoem(id).l[0]).split(' ').slice(0, 3).join(' ').replace(/[,.]/g, '') + '…';
function MwCoupletPad() {
  const [pid, setPid] = useState('kites'), [k, setK] = useState('F'), R = MW_CPL[pid], slots = mwSlots(R), last = slots.length - 1;
  const [notes, setNotes] = useState(() => Array(mwSlots(MW_CPL.kites).length).fill(null)), [cur, setCur] = useState(0), [phr, setPhr] = useState(null), [lit, setLit] = useState(-1), [msg, setMsg] = useState(null);
  const T = useSpTimers(), K = MW_KEYS[k];
  const chooseP = (id) => { T.clear(); setPid(id); setNotes(Array(mwSlots(MW_CPL[id]).length).fill(null)); setCur(0); setPhr(null); setLit(-1); setMsg(null); };
  const chooseK = (x) => { T.clear(); const sh = MW_KEYS[x].t - K.t; setK(x); setNotes(notes.map(d => d == null || d + sh < MW_LO || d + sh > MW_HI ? null : d + sh)); setLit(-1); setMsg(null); };
  const tap = (semi) => { T.clear(); setLit(-1); spPlay([{ keys: [semi], at: 0, len: 0.8 }], 120);
    const d = mwDOf(semi, k); if (d == null) { const nm = MW_SEMI_NM[((semi % 12) + 12) % 12]; setMsg(K.minor ? t(nm + ' is not in ' + K.en + ' (the harmonic minor: its 7th is raised). Use the named keys.', nm + '은(는) ' + K.ko + '(화성 단음계: 7음을 올려요)의 음이 아니에요. 이름이 적힌 건반을 써요.') : t(nm + ' is not in ' + K.en + '. Use the named keys.', nm + '은(는) ' + K.ko + '의 음이 아니에요. 이름이 적힌 건반을 써요.')); return; }
    const nx = notes.slice(); nx[cur] = d; setNotes(nx); setMsg(null);
    let j = cur + 1; while (j <= last && nx[j] != null) j++; setCur(j <= last ? j : Math.min(cur + 1, last)); };
  const back = () => { T.clear(); const j = notes[cur] != null ? cur : Math.max(0, cur - 1), nx = notes.slice(); nx[j] = null; setNotes(nx); setCur(j); setMsg(null); };
  const play = () => { T.clear(); const ev = slots.map((s, i) => notes[i] == null ? null : { keys: [mwSemi(notes[i], k)], at: mwBarAt(R, s.b) + s.at, len: s.len }).filter(Boolean); if (!ev.length) return;
    const r = spPlay(ev, 92, R.m); if (!r) return; const endB = Math.max(...slots.map(s => mwBarAt(R, s.b) + s.at + s.len));
    slots.forEach((s, i) => { if (notes[i] != null) T.at(r.ms(mwBarAt(R, s.b) + s.at), () => setLit(i)); }); T.at(r.ms(endB) + 150, () => setLit(-1)); };
  const rules = mwRulesC(notes, R, k, phr), allOk = notes.every(d => d != null) && rules.every(([, v]) => v === true);
  const names = {}, litK = {}; for (let d = MW_LO; d <= MW_HI; d++) { const sm = mwSemi(d, k); names[sm] = mwName(d, k); if (mwDeg(d, k) === 1) litK[sm] = 'pale'; }
  if (lit >= 0 && notes[lit] != null) litK[mwSemi(notes[lit], k)] = 'cor';
  return (
    <div className="try-box" style={actBox} data-mw="couplet">
      <div style={actTitle}>{t('A melody for a couplet', '두 줄 시에 선율 붙이기')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>4급: 가사가 리듬을 정해요(가사와 리듬 단계처럼 센 음절마다 마디줄). <b>음절마다 음 하나</b>를 장조나 단조로 써요. 가사는 음표 아래에 있어요. <b>첫 줄은 묻고, 둘째 줄은 대답하며 으뜸음으로</b> 돌아와요. 아래 다섯 가지가 모두 ✓가 되게 해 봐요.</>
        : <>Grade 4: the words set the rhythm (a bar line before each strong syllable, as in Words and rhythm). Write <b>a note for every syllable</b>, in a major or a minor key; the words sit under the notes. <b>Line 1 asks; line 2 answers</b> and comes home to the tonic. Make all five points below ✓.</>}</div>
      {spChips(MW_CPL_IDS.map(id => [id, mwCplChip(id)]), pid, chooseP)}
      {spChips(MW_KEY_MAJ.map(x => [x, t(MW_KEYS[x].en, MW_KEYS[x].ko)]), k, chooseK)}
      {spChips(MW_KEY_MIN.map(x => [x, t(MW_KEYS[x].en, MW_KEYS[x].ko)]), k, chooseK)}
      <MwStaff k={k} rh={R} notes={notes} cur={cur} lit={lit} phr={phr} words={R.words} sp={1.3} onSlot={(i) => { setCur(i); setMsg(null); }} per={mlxPer() === 2 ? 2 : 4} label={t('An eight-bar melody with the words under the notes.', '음표 아래에 가사가 있는 8마디 선율.')}/>
      <div style={{margin:'6px 0 4px'}}><SpKb lo={0} hi={19} names={names} lit={litK} onTap={tap} label={t('Piano keys: the notes of ' + K.en + ' are named; the tonic is coral.', '피아노 건반: ' + K.ko + '의 음에 이름이 있고, 으뜸음은 산호색이에요.')}/></div>
      {msg ? spMsg(msg, BK.coral) : allOk ? spMsg(t('A question and an answer: an eight-bar melody for the words. ▶ Play it, then sing it.', '질문과 대답: 가사에 붙인 8마디 선율이에요. ▶ 치고, 노래해 봐요.'), BK.green) : null}
      <div style={{display:'flex',gap:6,justifyContent:'center',flexWrap:'wrap',margin:'6px 0'}}>
        <button className="ghost-btn" style={spBtn} onClick={play}>{t('▶ Play', '▶ 듣기')}</button>
        <button className="ghost-btn" style={spBtn} onClick={back}>{t('⌫ Back', '⌫ 지우기')}</button>
        <button className="ghost-btn" style={spBtn} data-mw-phr onClick={() => setPhr(phr === null ? 'lines' : null)}>{t('Phrase marks: ', '프레이즈 표시: ') + (phr ? t('one a line', '줄마다') : t('none', '없음'))}</button>
        <button className="ghost-btn" style={spBtn} onClick={() => { T.clear(); setNotes(mwModelC(k, R)); setPhr('lines'); setCur(last); setMsg(null); }}>{t('An example', '보기')}</button>
        <button className="ghost-btn" style={spBtn} onClick={() => chooseP(pid)}>{t('Clear', '모두 지우기')}</button>
      </div>
      <div style={{display:'grid',gap:3,maxWidth:440,margin:'4px auto 0'}} data-mw-rules>
        {rules.map(([id, v]) => <div key={id} data-mw-rule={id + ':' + v} style={{display:'flex',gap:8,alignItems:'baseline',fontSize:14,fontWeight:800,color:v === true ? BK.green : v === false ? BK.coral : BK.muted}}>
          <span style={{width:16,flex:'0 0 16px',textAlign:'center',fontWeight:900}}>{v === true ? '✓' : v === false ? '✗' : '○'}</span><span>{t(MW_RULE_C[id][0], MW_RULE_C[id][1])}</span></div>)}
      </div>
    </div>
  );
}
'''
rep("""
// ── the drill: the strong syllables (the online exam's way: pick the right marks), the rhythm that fits the words, the""", CODE + """
// ── the drill: the strong syllables (the online exam's way: pick the right marks), the rhythm that fits the words, the""")

# ── the lesson in the Melody room (after Writing a melody), marked Grade 4 ──
rep("""  { id: 'mlx-write', ch: 'melody', title: 'Write a four-bar melody', blurb: 'A question and an answer on a given rhythm, in a major key.', C: () => <MwWritePad/> },   // Build AO""",
    """  { id: 'mlx-write', ch: 'melody', title: 'Write a four-bar melody', blurb: 'A question and an answer on a given rhythm, in a major key.', C: () => <MwWritePad/> },   // Build AO
  { id: 'mlx-couplet', ch: 'melody', title: 'A melody for a couplet', blurb: 'The words set the rhythm: eight bars in a major or minor key, the words under the notes.', C: () => <MwCoupletPad/> },   // Build AY: Grade 4""")
rep("""  'mlx-write': ['4마디 선율 쓰기', '주어진 리듬에 장조로 질문과 대답을 써요.'],   // Build AO""",
    """  'mlx-write': ['4마디 선율 쓰기', '주어진 리듬에 장조로 질문과 대답을 써요.'],   // Build AO
  'mlx-couplet': ['두 줄 시에 선율 붙이기', '가사가 리듬을 정해요: 장조나 단조로 8마디, 음표 아래에 가사.'],   // Build AY""")
rep("""'mlx-write': ['melody', 3, 3, 'show ear'], 'mlx-build'""", """'mlx-write': ['melody', 3, 3, 'show ear'], 'mlx-couplet': ['melody', 3, 3, 'show ear'], 'mlx-build'""")
rep("""'mlx-write': 'c-map', 'modes'""", """'mlx-write': 'c-map', 'mlx-couplet': 'c-map', 'modes'""")
rep("""  'melody': ['mlx-map', 'mlx-line', 'mlx-phrasing', 'mlx-qa', 'mlx-motif', 'mlx-seq', 'mlx-words', 'mlx-write', 'mlx-build',""",
    """  'melody': ['mlx-map', 'mlx-line', 'mlx-phrasing', 'mlx-qa', 'mlx-motif', 'mlx-seq', 'mlx-words', 'mlx-write', 'mlx-couplet', 'mlx-build',""")
rep("""lessons: ['mlx-map', 'mlx-line', 'mlx-phrasing', 'mlx-qa', 'mlx-motif', 'mlx-seq', 'mlx-words', 'mlx-write', 'mlx-build', 'phrase-marks',""",
    """lessons: ['mlx-map', 'mlx-line', 'mlx-phrasing', 'mlx-qa', 'mlx-motif', 'mlx-seq', 'mlx-words', 'mlx-write', 'mlx-couplet', 'mlx-build', 'phrase-marks',""")
rep("""  set('4', 'spr-tune cpx-dances');   // Build AW""", """  set('4', 'mlx-couplet');   // Build AY: a melody for a couplet, Theory of Music Grade 4
  set('4', 'spr-tune cpx-dances');   // Build AW""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
