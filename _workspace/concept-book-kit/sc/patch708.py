import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)
def rep_in(start_marker, end_marker, old, new, n=1):
    global s
    a = s.index(start_marker); b = s.index(end_marker, a)
    region = s[a:b]
    assert region.count(old) == n, (region.count(old), old[:90])
    s = s[:a] + region.replace(old, new) + s[b:]

# Build AO (board calls 16 and 17).
# Call 16: melody writing as two steps at the end of Melody & Phrasing (Theory of Music Grade 2 and 3 Creative), with a
# pad each, three drill levels, two Home lessons, two Lesson Book pages, two Workbook pages, a check-up section and the
# teacher's answers. Call 17: 'Seven chords in a key' moves to the Grade 4 mark (Theory of Music Grade 4: chords on I, II,
# IV, V, VI); 'Cadences' stays on Grades 2-3 and marks its imperfect and interrupted cadences Grade 4 (Theory of Music Grade
# 3 has the perfect and plagal; Grade 4 the four principal cadences).

# ── call 17 ──
rep("""    + ' ch-145 ch-seven ch-inv ch-cad md-home md-start sc-modes rm-semi rm-trip rm-cut rm-swing');""",
    """    + ' ch-145 ch-inv ch-cad md-home md-start sc-modes rm-semi rm-trip rm-cut rm-swing');""")
rep("""set('4', 'iv-invert iv-tritone ch-da md-family md-ladder');""",
    """set('4', 'iv-invert iv-tritone ch-da ch-seven md-family md-ladder');""")   # ch-seven: Build AO (Theory of Music Grade 4: chords on I II IV V VI)
rep("""const CHQ_CADS = ['perfect', 'plagal', 'imperfect', 'interrupted'];""",
    """const CHQ_CADS = ['perfect', 'plagal', 'imperfect', 'interrupted'];
const CHQ_CAD_G4 = ['imperfect', 'interrupted'];   // Build AO: Theory of Music Grade 4 (Grade 3 has the perfect and plagal)""")
rep("""<span style={{ fontWeight: 800, fontSize: 13 }}>{kqT(CHQ_CAD[x].w)}</span><span style={{ fontWeight: 900, fontSize: 15 }}>{CHQ_CAD[x].r.map(chqRom).join(' → ')}</span></button>)}""",
    """<span style={{ fontWeight: 800, fontSize: 13 }}>{kqT(CHQ_CAD[x].w)}</span><span style={{ fontWeight: 900, fontSize: 15 }}>{CHQ_CAD[x].r.map(chqRom).join(' → ')}</span>{CHQ_CAD_G4.includes(x) && <span data-g4 style={{ fontSize: 9.5, fontWeight: 800, letterSpacing: '0.07em', color: 'var(--navy-soft)' }}>GRADE 4</span>}</button>)}""")
rep("""  steps: CHQ_CADS.map(id => ({ title: [CHQ_CAD[id].w[0][0].toUpperCase() + CHQ_CAD[id].w[0].slice(1), CHQ_CAD[id].w[1]], line: CHQ_CAD[id].feel,""",
    """  steps: CHQ_CADS.map(id => ({ title: [CHQ_CAD[id].w[0][0].toUpperCase() + CHQ_CAD[id].w[0].slice(1) + (CHQ_CAD_G4.includes(id) ? ' · Grade 4' : ''), CHQ_CAD[id].w[1] + (CHQ_CAD_G4.includes(id) ? ' · Grade 4' : '')], line: CHQ_CAD[id].feel,""")

# ── the rhythm staff learns words under its notes (o.words: one per sound; ^ before a strong syllable, which gets an
# upright line before it) ──
rep("""  if (o.marks) snd.forEach((s, i) => { const m = o.marks[i]; if (m) under.push(""",
    """  if (o.words) snd.forEach((s, i) => { const w = o.words[i]; if (w == null || s.rest || soundX[i] == null) return;   // Build AO: the words of a song, under its notes
    const strong = w[0] === '^', tx = strong ? w.slice(1) : w, on = litSet.has(i), yW = G(30) + (o.dyW || 30), fs = o.wfs || 14, tw = [...tx].length * fs * 0.56;
    if (strong) under.push('<line x1="' + pFix(soundX[i] - tw / 2 - 3.5) + '" x2="' + pFix(soundX[i] - tw / 2 - 3.5) + '" y1="' + pFix(yW - fs * 0.95) + '" y2="' + pFix(yW + 3) + '" stroke="' + cor + '" stroke-width="2.2"/>');
    under.push('<text x="' + pFix(soundX[i]) + '" y="' + pFix(yW) + '" text-anchor="middle" font-family="Inter, sans-serif" font-size="' + fs + '" font-weight="' + (strong ? 900 : 700) + '" fill="' + (on ? cor : col) + '">' + tx + '</text>'); });
  if (o.marks) snd.forEach((s, i) => { const m = o.marks[i]; if (m) under.push(""")
rep("""const srhPadBottom = (o = {}) => o.hearts === false && o.counts === false ? 22 : (o.dyH || 28) + (o.dyC || 26) + (o.counts === 'blank' || o.counts === 'ans' ? 9 : 12) + (o.marks ? 24 : 0);""",
    """const srhPadBottom = (o = {}) => (o.hearts === false && o.counts === false ? 22 : (o.dyH || 28) + (o.dyC || 26) + (o.counts === 'blank' || o.counts === 'ans' ? 9 : 12) + (o.marks ? 24 : 0)) + (o.words ? (o.dyW || 30) - 8 : 0);   // Build AO: room for words""")

# ── the melody-writing code (pads, staff, drill, workbook pages) ──
MW = r'''// ══ Build AO (board call 16): melody writing, two steps at the end of Melody & Phrasing (call 14 put it here). Theory of
// Music, Creative (Manual of Syllabuses 2026, page 66, read 26 Oct): Grade 2, mark the accentuation in a simple couplet of
// words (an upright line before each accented syllable or word; online, the right emphasis picked from options); Grade 3,
// (a) a suitable rhythmic pattern to a simple couplet, (b) a melody of four bars in any major key up to two sharps or two
// flats, on a given rhythmic pattern, with phrasing. The couplets are new, written for this chapter. How the words are set
// here (a bar line before each strong syllable, one strong syllable a bar, the last syllable of a line held) and the five
// melody points (start on 1, 3 or 5; mostly steps; bar 2 rests away from the tonic; end on the tonic; phrase marks) are the
// usual textbook guidance, not syllabus text: flagged for Sohyun on the board.

// ── the couplets. ^ before a strong syllable; - between the syllables of a word
const MW_POEMS = [
  { id: 'kites', m: 2, l: ['^Kites are ^fly-ing ^high and ^free,', '^Dan-cing ^o-ver ^field and ^tree.'] },
  { id: 'snow', m: 2, l: ['^Snow-flakes ^drift-ing ^soft-ly ^down', '^Cov-er ^all the ^qui-et ^town.'] },
  { id: 'boat', m: 2, l: ['A ^lit-tle ^boat sails ^out to ^sea,', 'Its ^sail is ^white as ^white can ^be.'] },
  { id: 'hills', m: 3, l: ['^Mer-ri-ly ^o-ver the ^hills we will ^go,', '^Sing-ing a ^song as we ^march to and ^fro.'] },
  { id: 'moon', m: 3, l: ['In the ^light of the ^moon by the ^side of the ^sea,', 'All the ^fish in the ^wa-ter are ^dan-cing with ^me.'] },
];
const mwSyl = (line) => line.split(' ').flatMap(w => { const ps = w.split('-'); return ps.map((p, j) => ({ t: p.replace('^', ''), s: p.includes('^'), end: j === ps.length - 1 })); });
const MW_SYL = {}; MW_POEMS.forEach(p => { MW_SYL[p.id] = p.l.map(mwSyl); });
const mwPoem = (id) => MW_POEMS.find(p => p.id === id);
const mwTx = (x) => x.t + (x.end ? '' : '-');
const mwStarts = (syls) => syls.map((x, i) => x.s ? i : -1).filter(i => i >= 0);
// the line in capitals where it is strong (the teacher's answers): KITES are FLY-ing HIGH and FREE
const mwCaps = (syls) => syls.map((x, i) => (i > 0 && syls[i - 1].end ? ' ' : '') + (x.s ? x.t.toUpperCase() : x.t) + (x.end ? '' : '-')).join('');

// the rhythm of a bar of n syllables, len crotchet beats long: crotchets when they fill it; otherwise the first one held
function mwBarRhythm(n, len) {
  if (n === len) return Array(n).fill('q');
  if (n === 1) return [{ 1: 'q', 2: 'h', 3: 'hd', 4: 'w' }[len]];
  if (n === 2 && len === 3) return ['h', 'q'];
  if (n === 3 && len === 2) return ['q', 'p'];
  if (n === 4 && len === 2) return ['p', 'p'];
  if (n === 4 && len === 3) return ['q', 'q', 'p'];
  return null;
}
// a run of syllables set in m crotchet beats a bar, with a bar line before each start (syllables before the first start are
// an anacrusis, a crotchet each, and the last bar is that much shorter). per: bars a row. Returns the rows (items, words,
// the row's first sound), every item in one run (for the sound), and where in the bar it starts.
function mwSet(syls, m, starts, o = {}) {
  const a = starts[0] || 0, groups = [];
  if (a > 0) groups.push({ n: a, ana: true });
  starts.forEach((st, j) => groups.push({ n: (j + 1 < starts.length ? starts[j + 1] : syls.length) - st }));
  const lastJ = groups.length - 1;
  const rhy = groups.map((g, j) => { if (g.ana) return g.n < m ? Array(g.n).fill('q') : null; const len = j === lastJ && a > 0 ? m - a : m; return mwBarRhythm(g.n, len) || (len !== m ? mwBarRhythm(g.n, m) : null); });
  if (rhy.some(r => !r)) return null;
  const words = syls.map(x => (x.s ? '^' : '') + mwTx(x)), per = o.per || 4, rows = [];
  let cur = null, nBars = 0, w = 0;
  groups.forEach((g, j) => {
    if (!cur || (!g.ana && nBars === per)) { cur = { items: rows.length === 0 ? [['ts', m]] : [], words: [], off: w }; rows.push(cur); nBars = 0; }
    rhy[j].forEach(k => { cur.items.push([k]); for (let u = 0; u < (k === 'p' ? 2 : 1); u++) cur.words.push(words[w++]); });
    cur.items.push([j === lastJ ? '||' : '|']);
    if (!g.ana) nBars++;
  });
  const all = rows.flatMap(r => r.items);
  return { rows, all, from: a > 0 ? m - a : 0, m, a, rhy, starts };
}
const MW_RNM = { q: ['crotchet', '4분음표'], h: ['minim', '2분음표'], hd: ['dotted minim', '점2분음표'], w: ['semibreve', '온음표'], p: ['two quavers', '8분음표 둘'] };
// the rhythm in words, bar by bar (the teacher's answers)
const mwRhyTxt = (set) => set.m + '/4: ' + set.rhy.map(r => r.every(k => k === 'q') ? (r.length === 1 ? 'crotchet' : r.length + ' crotchets') : r.map(k => MW_RNM[k][0]).join(' + ')).join(' | ');

// rows of rhythm with words, all at one scale (each row as wide as its bars); lit: the sound playing, counted through the rows
function MwRows({ rows, o = {}, lit = -1, label }) {
  const vb = rows.map(r => Math.ceil(srhRaw((d) => dY(d), r.items, { ...o, words: r.words }).last + 6)), Wm = Math.max(...vb);
  return <div style={{width:'100%',maxWidth:Math.round(Wm * 1.3),margin:'0 auto'}}>{rows.map((r, j) => <SrhStaff key={j} items={r.items} width={Wm} o={{ ...o, words: r.words, lit: lit >= r.off && lit < r.off + r.words.length ? lit - r.off : -1 }} label={label}/>)}</div>;
}
// ── the couplet on screen and on paper: its syllables, an upright line before each marked one ──
function MwMarked({ syls, marks, size = 16, col }) {
  return <span style={{fontSize:size,fontWeight:800,color:col || BK.ink,lineHeight:1.5,wordBreak:'keep-all'}}>{syls.map((x, i) => <React.Fragment key={i}>{i > 0 && syls[i - 1].end ? ' ' : ''}{marks && marks[i] && <b style={{color:PEN_C,fontWeight:900,margin:'0 1px 0 0'}}>|</b>}{mwTx(x)}</React.Fragment>)}</span>;
}

// ── step 6: words and rhythm. Tap the strong syllables; check; then the bars and the rhythm, said and clapped ──
function MwWordsPad() {
  const [pid, setPid] = useState('kites'), [marks, setMarks] = useState({}), [chk, setChk] = useState(false), [show, setShow] = useState(false), [lit, setLit] = useState(-1);
  const T = usePlTimers();
  const P = mwPoem(pid), L = MW_SYL[pid], flat = L[0].concat(L[1]), n0 = L[0].length;
  const set = mwSet(flat, P.m, mwStarts(flat), { per: mlxPer() === 2 ? 2 : 4 });
  const nS = flat.filter(x => x.s).length, got = flat.filter((x, i) => x.s && marks[i]).length, extra = flat.filter((x, i) => !x.s && marks[i]).length, any = Object.values(marks).some(Boolean);
  const choose = (id) => { T.clear(); stopClicks(); setPid(id); setMarks({}); setChk(false); setShow(false); setLit(-1); };
  const tap = (i) => { if (chk) return; setMarks({ ...marks, [i]: !marks[i] }); };
  const listen = () => { T.clear(); setLit(-1); const r = rqRunS(set.all, { from: set.from, clicks: P.m, bpm: 80 }); if (!r) return; const go = r.at[r.lead];
    srhSounds(set.all).forEach((s, i) => T.at(r, go + s.b * r.spb, () => setLit(i))); T.at(r, go + srhBeats(set.all) * r.spb + 0.1, () => setLit(-1)); };
  const chip = (x, i) => { const on = !!marks[i], st = chk ? (x.s && on ? 'ok' : x.s ? 'miss' : on ? 'extra' : '') : '';
    const col = st === 'ok' ? BK.green : st === 'miss' || st === 'extra' ? BK.coral : BK.ink, gap = i > 0 && i !== n0 && flat[i - 1].end;
    return <button key={i} data-mw-syl={i} aria-pressed={on} onClick={() => tap(i)} style={{display:'inline-flex',alignItems:'center',gap:2,minHeight:42,padding:'4px 7px',marginLeft:gap ? 7 : 0,border:'1.5px ' + (st === 'miss' ? 'dashed ' : 'solid ') + (st ? col : on ? PEN_C : 'rgba(38,41,107,0.2)'),borderRadius:8,background:on && !chk ? '#fbe3da' : '#fff',fontSize:16,fontWeight:800,color:col,cursor:chk ? 'default' : 'pointer',fontFamily:'inherit'}}>
      {(on || st === 'miss') && <b style={{color:st === 'ok' ? BK.green : PEN_C,fontWeight:900,opacity:st === 'miss' ? 0.6 : 1}}>|</b>}{mwTx(x)}</button>; };
  return (
    <div className="try-box" style={actBox} data-mw="words">
      <div style={actTitle}>{t('Words and rhythm', '가사와 리듬')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>두 줄 시를 소리 내어 말해요. <b>힘주어 말하는 음절</b>을 눌러 그 앞에 세로줄(|)을 그어요. 그다음 확인.</> : <>Say the couplet out loud. Tap each syllable you say <b>with more weight</b>: an upright line (|) goes before it. Then check.</>}</div>
      {spChips(MW_POEMS.map((p, j) => [p.id, String(j + 1)]), pid, choose)}
      <div style={{display:'flex',flexDirection:'column',gap:8,margin:'4px 0 8px'}}>
        {[0, 1].map(li => <div key={li} style={{display:'flex',flexWrap:'wrap',gap:'6px 3px',justifyContent:'center'}}>{L[li].map((x, j) => chip(x, li ? n0 + j : j))}</div>)}
      </div>
      {chk && spMsg(got === nS && !extra ? t('All ' + nS + ' strong syllables.', '센 음절 ' + nS + '개를 모두 찾았어요.')
        : t('Found ' + got + ' of ' + nS + (extra ? '; ' + extra + ' on a weak syllable' : '') + '. Green: found; dashed: missed.', nS + '개 중 ' + got + '개' + (extra ? ', 여린 음절에 ' + extra + '개' : '') + '. 초록: 찾음, 점선: 놓침.'), got === nS && !extra ? BK.green : BK.coral)}
      <div style={{display:'flex',gap:6,justifyContent:'center',flexWrap:'wrap',marginTop:6}}>
        {!chk && <button className="ghost-btn" style={{...spBtn,...(any ? {} : {opacity:0.4})}} disabled={!any} onClick={() => setChk(true)}>{t('✓ Check', '✓ 확인')}</button>}
        {!chk && <button className="ghost-btn" style={spBtn} onClick={() => { setMarks(Object.fromEntries(flat.map((x, i) => [i, x.s]))); setChk(true); }}>{t('Show me', '보여 주세요')}</button>}
        {chk && !show && <button className="ghost-btn" style={spBtn} onClick={() => setShow(true)}>{t('▶ The rhythm', '▶ 리듬 보기')}</button>}
        {chk && <button className="ghost-btn" style={spBtn} onClick={() => choose(pid)}>{t('↺ Again', '↺ 다시')}</button>}
      </div>
      {show && <div style={{marginTop:10}} data-mw-rhythm>
        {spMsg(t('A bar line before each strong syllable. The last syllable of each line holds on.', '센 음절마다 그 앞에 마디줄. 줄 끝 음절은 길게.'))}
        <MwRows key={pid} rows={set.rows} o={{ D: 46, counts: false, hearts: false }} lit={lit} label={t('The rhythm, with the words under the notes.', '음표 아래에 가사가 있는 리듬.')}/>
        <div style={{textAlign:'center',marginTop:6}}><button className="ghost-btn" style={spBtn} onClick={listen}>{t('▶ Listen, then say it', '▶ 듣고 따라 말하기')}</button></div>
      </div>}
    </div>
  );
}

// ── step 7: a four-bar melody on a given rhythm, in a major key up to two sharps or two flats ──
// d: steps from middle C (28 = C4, as everywhere). t: the tonic the melody is written around.
const MW_KEYS = {
  C: { t: 28, n: 0, s: null, en: 'C major', ko: 'C장조' }, G: { t: 32, n: 1, s: 'sharp', en: 'G major', ko: 'G장조' }, D: { t: 29, n: 2, s: 'sharp', en: 'D major', ko: 'D장조' },
  F: { t: 31, n: 1, s: 'flat', en: 'F major', ko: 'F장조' }, Bb: { t: 34, n: 2, s: 'flat', en: 'B♭ major', ko: 'B♭장조' },
};
const MW_KEY_IDS = ['C', 'G', 'D', 'F', 'Bb'];
const MW_LO = 28, MW_HI = 39;   // C4 to G5: the keyboard's range
const mwLet = (d) => 'CDEFGAB'[((d - 28) % 7 + 7) % 7];
const mwAlt = (d, k) => { const K = MW_KEYS[k]; if (!K.s) return 0; const sig = (K.s === 'sharp' ? SHARP_ORDER : FLAT_ORDER).slice(0, K.n).map(x => x[0]); return sig.includes(mwLet(d)) ? (K.s === 'sharp' ? 1 : -1) : 0; };
const mwSemi = (d, k) => [0, 2, 4, 5, 7, 9, 11][((d - 28) % 7 + 7) % 7] + 12 * Math.floor((d - 28) / 7) + mwAlt(d, k);
const mwName = (d, k) => mwLet(d) + (mwAlt(d, k) > 0 ? '♯' : mwAlt(d, k) < 0 ? '♭' : '');
const mwDeg = (d, k) => ((d - MW_KEYS[k].t) % 7 + 7) % 7 + 1;
const mwDOf = (semi, k) => { for (let d = MW_LO; d <= MW_HI; d++) if (mwSemi(d, k) === semi) return d; return null; };
const MW_SEMI_NM = ['C', 'C♯', 'D', 'E♭', 'E', 'F', 'F♯', 'G', 'G♯', 'A', 'B♭', 'B'];
// the given rhythms (p: two quavers), and one answer for each in scale degrees (1 the tonic). Each answer starts on 1, moves
// mostly by step, rests away from the tonic at the end of bar 2 (2 or 5) and ends on the tonic.
const MW_RH = [
  { id: 'r1', m: 4, bars: [['q', 'q', 'q', 'q'], ['q', 'q', 'h'], ['q', 'q', 'q', 'q'], ['w']], model: [1, 2, 3, 1, 2, 3, 2, 3, 4, 5, 2, 1] },
  { id: 'r2', m: 3, bars: [['q', 'q', 'q'], ['hd'], ['q', 'q', 'q'], ['hd']], model: [1, 2, 3, 5, 4, 3, 2, 1] },
  { id: 'r3', m: 4, bars: [['q', 'p', 'q', 'q'], ['q', 'q', 'h'], ['p', 'p', 'q', 'q'], ['w']], model: [1, 2, 3, 4, 5, 6, 4, 5, 4, 3, 2, 3, 4, 2, 1] },
];
const mwRh = (id) => typeof id === 'string' ? MW_RH.find(r => r.id === id) : id;
const mwModel = (k, rh) => mwRh(rh).model.map(dg => MW_KEYS[k].t + dg - 1);
// the slots to fill: a note each (a pair of quavers is two)
const mwSlots = (rh) => { const out = []; mwRh(rh).bars.forEach((bar, b) => { let at = 0; bar.forEach(k => {
  if (k === 'p') { out.push({ b, k: 'e', len: 0.5, at, beam: 0 }, { b, k: 'e', len: 0.5, at: at + 0.5, beam: 1 }); at += 1; }
  else { const len = { q: 1, h: 2, hd: 3, w: 4 }[k]; out.push({ b, k, len, at }); at += len; } }); }); return out; };
// the rhythm alone, for the rhythm staff
const mwRhItems = (rh) => { const R = mwRh(rh); return [['ts', R.m]].concat(R.bars.flatMap((bar, b) => bar.map(k => [k]).concat([[b === R.bars.length - 1 ? '||' : '|']]))); };

// one line of the staff: bars b0 to b1 (the time signature on the first line only)
const MW_ADV = { e: 21, q: 32, h: 46, hd: 54, w: 62 };
function mwLine(k, R, b0, b1, ts, sp = 1) {
  const all = mwSlots(R), ids = all.map((s, i) => i).filter(i => all[i].b >= b0 && all[i].b <= b1), xs = {}, bars = [];
  let x = 46 + MW_KEYS[k].n * 10 + (ts ? 30 : 6);
  ids.forEach((i, j) => { if (j && all[i].b !== all[ids[j - 1]].b) { bars.push(x + 2); x += 14; } xs[i] = x + 10; x += MW_ADV[all[i].k] * sp; });
  return { all, ids, xs, bars, end: x + 4, W: x + 16 };
}
// the staff: the key signature, the slots (an empty one drawn faint on the middle line), the phrase marks ('22': bars 1-2
// and 3-4; '4': all four), the slot being filled (a coral mark under it). per: bars a line. empty: no notes (paper).
function MwStaff({ k, rh, notes = [], cur = null, lit = -1, hl = [], phr = null, onSlot, empty, per = 4, sp = 1, label }) {
  const R = mwRh(rh), K = MW_KEYS[k], sig = K.s ? (K.s === 'sharp' ? SHARP_ORDER : FLAT_ORDER).slice(0, K.n) : [], GH = 'rgba(38,41,107,0.26)';
  const lines = []; for (let b = 0; b < 4; b += per) lines.push(mwLine(k, R, b, Math.min(3, b + per - 1), b === 0, sp));
  const Wmax = Math.max(...lines.map(L => L.W));
  const all = lines[0].all, dOf = (i) => notes[i] != null ? notes[i] : 34, colOf = (i) => i === lit || hl.includes(i) ? PEN_C : notes[i] != null ? PEN_N : GH;
  const upOf = (i) => { const s = all[i]; if (s.k === 'e') { const j = s.beam ? i - 1 : i; return (dOf(j) + dOf(j + 1)) / 2 < 34; } return dOf(i) < 34; };
  const ranges = phr === '22' ? [[0, 1], [2, 3]] : phr === '4' ? [[0, 3]] : [];
  const one = (L, li) => { const b0 = li * per, b1 = Math.min(3, b0 + per - 1), els = [];
    let yA = dY(38) - 12, yB = dY(30) + 10;   // what the line holds, top and bottom
    const ext = (a, b) => { yA = Math.min(yA, a); yB = Math.max(yB, b); };
    if (cur != null && L.xs[cur] != null && !empty) els.push(<rect key="cu" x={L.xs[cur] - 12} y={dY(40)} width="24" height={dY(28) - dY(40)} rx="4" fill="#fbe3da"/>);
    [30, 32, 34, 36, 38].forEach(l => els.push(<line key={'l' + l} x1="4" x2={L.W - 4} y1={dY(l)} y2={dY(l)} stroke={PEN_N} strokeOpacity="0.55" strokeWidth="1.2"/>));
    els.push(<ClefGlyph key="cl" clef="treble" st="treble" yOf={dY} ink={PEN_N}/>);
    sig.forEach((a, j) => { const pos = (K.s === 'sharp' ? SHARP_POS : FLAT_POS)[a], x = 46 + j * 10, y = dY(30 + pos); els.push(K.s === 'sharp' ? <SharpShape key={'k' + j} x={x} y={y} color={PEN_N}/> : <FlatShape key={'k' + j} x={x} y={y} color={PEN_N}/>); });
    if (li === 0) [[R.m, dY(36)], [4, dY(32)]].forEach(([n, y], j) => els.push(<text key={'t' + j} x={46 + K.n * 10 + 13} y={y + 7.6} textAnchor="middle" fontFamily="Playfair Display, Georgia, serif" fontSize="25" fontWeight="900" fill={PEN_N}>{n}</text>));
    L.bars.forEach((bx, j) => els.push(<line key={'b' + j} x1={bx} x2={bx} y1={dY(38)} y2={dY(30)} stroke={PEN_N} strokeWidth="1.5"/>));
    if (b1 === 3) els.push(<line key="e1" x1={L.end} x2={L.end} y1={dY(38)} y2={dY(30)} stroke={PEN_N} strokeWidth="1.3"/>, <line key="e2" x1={L.end + 5} x2={L.end + 5} y1={dY(38)} y2={dY(30)} stroke={PEN_N} strokeWidth="3.8"/>);
    else els.push(<line key="e1" x1={L.end} x2={L.end} y1={dY(38)} y2={dY(30)} stroke={PEN_N} strokeWidth="1.5"/>);
    if (!empty) L.ids.forEach(i => { const s = all[i], d = dOf(i), x = L.xs[i], y = dY(d), c = colOf(i), up = upOf(i), hollow = s.k === 'h' || s.k === 'hd' || s.k === 'w';
      ext(up && s.k !== 'w' ? y - 34 : y - 8, !up && s.k !== 'w' ? y + 34 : y + 8);
      if (notes[i] != null) ledgersFor(d, 30, 38).forEach(p => els.push(<line key={'lg' + i + '_' + p} x1={x - 11} x2={x + 11} y1={dY(p)} y2={dY(p)} stroke={PEN_N} strokeWidth="1.3"/>));
      els.push(<ellipse key={'h' + i} cx={x} cy={y} rx="6.6" ry="4.8" transform={`rotate(-20 ${x} ${y})`} fill={hollow ? '#fff' : c} stroke={c} strokeWidth={hollow ? 2.2 : 1}/>);
      if (s.k === 'hd') els.push(<circle key={'dt' + i} cx={x + 12} cy={(d - 30) % 2 === 0 ? y - 5 : y} r="2.4" fill={c}/>);
      if (s.k === 'q' || s.k === 'h' || s.k === 'hd') els.push(<line key={'s' + i} x1={up ? x + 6 : x - 6} x2={up ? x + 6 : x - 6} y1={y + (up ? -1 : 1)} y2={y + (up ? -32 : 32)} stroke={c} strokeWidth="1.7"/>);
      if (s.k === 'e' && !s.beam) { const j = i + 1, x2 = L.xs[j], y2 = dY(dOf(j)), by = up ? Math.min(y, y2) - 30 : Math.max(y, y2) + 30, sx1 = up ? x + 6 : x - 6, sx2 = up ? x2 + 6 : x2 - 6;
        els.push(<line key={'s' + i} x1={sx1} x2={sx1} y1={y + (up ? -1 : 1)} y2={by} stroke={c} strokeWidth="1.7"/>, <line key={'s' + j} x1={sx2} x2={sx2} y1={y2 + (up ? -1 : 1)} y2={by} stroke={colOf(j)} strokeWidth="1.7"/>,
          <line key={'bm' + i} x1={sx1 - 0.8} x2={sx2 + 0.8} y1={by + (up ? 2.2 : -2.2)} y2={by + (up ? 2.2 : -2.2)} stroke={notes[i] != null && notes[j] != null ? (i === lit || j === lit ? PEN_C : PEN_N) : GH} strokeWidth="4.6"/>); }
    });
    if (!empty) ranges.forEach(([r0, r1], r) => { const s0 = Math.max(r0, b0), s1 = Math.min(r1, b1); if (s0 > s1) return;
      const ids = L.ids.filter(i => all[i].b >= s0 && all[i].b <= s1), tops = ids.map(i => { const y = dY(dOf(i)); return upOf(i) && all[i].k !== 'w' ? y - 33 : y - 8; });
      const ya = Math.min(dY(39), ...tops) - 7, openL = r0 < b0, openR = r1 > b1, x1 = openL ? 46 + K.n * 10 + 4 : L.xs[ids[0]] - 3, x2 = openR ? L.end - 2 : L.xs[ids[ids.length - 1]] + 5;
      const y1 = openL ? ya - 6 : ya + 7, y2 = openR ? ya - 6 : ya + 7; ext(ya - 14, ya);
      els.push(<path key={'ph' + r} d={`M${x1} ${y1} C${x1 + (openL ? 0 : 14)} ${ya - 12} ${x2 - (openR ? 0 : 14)} ${ya - 12} ${x2} ${y2}`} fill="none" stroke={PEN_N} strokeWidth="2" strokeLinecap="round"/>); });
    if (cur != null && L.xs[cur] != null && !empty) { const x = L.xs[cur], y = Math.max(yB, dY(28) + 8) + 4; ext(y, y + 10); els.push(<path key="tri" d={`M${x - 6} ${y + 8} L${x + 6} ${y + 8} L${x} ${y} Z`} fill={PEN_C}/>); }
    if (onSlot && !empty) L.ids.forEach(i => els.push(<rect key={'tap' + i} data-mw-slot={i} x={L.xs[i] - 12} y={dY(42)} width="24" height={dY(26) - dY(42)} fill="transparent" style={{cursor:'pointer'}} onClick={() => onSlot(i)}/>));
    return <svg key={li} viewBox={`0 ${yA - 3} ${L.W} ${yB - yA + 6}`} style={{width:(L.W / Wmax * 100) + '%',display:'block',margin:'0 auto 6px 0'}} role="img" aria-label={label || t('A four-bar melody on the staff.', '오선 위의 4마디 선율.')}>{els}</svg>; };
  return <div style={{width:'100%',maxWidth:Math.round(Wmax * 1.35),margin:'0 auto'}} data-mw-staff={k}>{lines.map(one)}</div>;
}

// the five points of a four-bar melody: true kept, false not, null not yet
function mwRules(notes, rh, k, phr) {
  const slots = mwSlots(rh), n = notes.length, deg = (d) => mwDeg(d, k), filled = notes.filter(d => d != null).length;
  const qi = slots.map((s, i) => s.b === 1 ? i : -1).filter(i => i >= 0).pop(), moves = [];
  for (let i = 1; i < n; i++) if (notes[i] != null && notes[i - 1] != null) moves.push(Math.abs(notes[i] - notes[i - 1]));
  const steps = moves.filter(m => m <= 1).length;
  return [
    ['start', notes[0] == null ? null : [1, 3, 5].includes(deg(notes[0]))],
    ['steps', filled < n ? (moves.length >= 4 && steps * 2 < moves.length ? false : null) : steps * 2 >= moves.length],
    ['q', notes[qi] == null ? null : deg(notes[qi]) !== 1],
    ['end', notes[n - 1] == null ? null : deg(notes[n - 1]) === 1],
    ['phr', phr ? true : null],
  ];
}
const MW_RULE_W = {
  start: ['Starts on note 1, 3 or 5 of the scale', '음계의 1, 3, 5번 음에서 시작해요'], steps: ['Moves mostly by step', '대부분 한 걸음씩 움직여요'],
  q: ['Bar 2 rests away from the tonic: a question', '2마디는 으뜸음이 아닌 음에서 쉬어요: 질문'], end: ['Bar 4 ends on the tonic: the answer', '4마디는 으뜸음에서 끝나요: 대답'], phr: ['Phrase marks', '프레이즈 표시'],
};
function MwWritePad() {
  const [k, setK] = useState('G'), [ri, setRi] = useState('r1'), R = mwRh(ri), slots = mwSlots(R);
  const [notes, setNotes] = useState(() => Array(mwSlots('r1').length).fill(null)), [cur, setCur] = useState(0), [phr, setPhr] = useState(null), [lit, setLit] = useState(-1), [msg, setMsg] = useState(null);
  const T = useSpTimers(), K = MW_KEYS[k], last = slots.length - 1;
  const chooseR = (id) => { T.clear(); setRi(id); setNotes(Array(mwSlots(id).length).fill(null)); setCur(0); setPhr(null); setLit(-1); setMsg(null); };
  const chooseK = (x) => { T.clear(); const sh = MW_KEYS[x].t - K.t; setK(x); setNotes(notes.map(d => d == null || d + sh < MW_LO || d + sh > MW_HI ? null : d + sh)); setLit(-1); setMsg(null); };
  const tap = (semi) => { T.clear(); setLit(-1); spPlay([{ keys: [semi], at: 0, len: 0.8 }], 120);
    const d = mwDOf(semi, k); if (d == null) { setMsg(t(MW_SEMI_NM[((semi % 12) + 12) % 12] + ' is not in ' + K.en + '. Use the named keys.', MW_SEMI_NM[((semi % 12) + 12) % 12] + '은(는) ' + K.ko + '의 음이 아니에요. 이름이 적힌 건반을 써요.')); return; }
    const nx = notes.slice(); nx[cur] = d; setNotes(nx); setMsg(null);
    let j = cur + 1; while (j <= last && nx[j] != null) j++; setCur(j <= last ? j : Math.min(cur + 1, last)); };
  const back = () => { T.clear(); const j = notes[cur] != null ? cur : Math.max(0, cur - 1), nx = notes.slice(); nx[j] = null; setNotes(nx); setCur(j); setMsg(null); };
  const play = () => { T.clear(); const ev = slots.map((s, i) => notes[i] == null ? null : { keys: [mwSemi(notes[i], k)], at: s.b * R.m + s.at, len: s.len }).filter(Boolean); if (!ev.length) return;
    const r = spPlay(ev, 92, R.m); if (!r) return; slots.forEach((s, i) => { if (notes[i] != null) T.at(r.ms(s.b * R.m + s.at), () => setLit(i)); }); T.at(r.ms(4 * R.m) + 150, () => setLit(-1)); };
  const rules = mwRules(notes, R, k, phr), allOk = notes.every(d => d != null) && rules.every(([, v]) => v === true);
  const names = {}, litK = {}; for (let d = MW_LO; d <= MW_HI; d++) { const sm = mwSemi(d, k); names[sm] = mwName(d, k); if (mwDeg(d, k) === 1) litK[sm] = 'pale'; }
  if (lit >= 0 && notes[lit] != null) litK[mwSemi(notes[lit], k)] = 'cor';
  const phrW = phr === '22' ? '2 + 2' : phr === '4' ? '4' : t('none', '없음');
  return (
    <div className="try-box" style={actBox} data-mw="write">
      <div style={actTitle}>{t('Write a four-bar melody', '4마디 선율 쓰기')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>주어진 리듬에 음을 하나씩 넣어요. <b>1·2마디는 질문, 3·4마디는 대답</b>이에요. 아래 다섯 가지가 모두 ✓가 되게 해 봐요.</> : <>Fill the rhythm, a note at a time. <b>Bars 1 and 2 ask; bars 3 and 4 answer.</b> Make all five points below ✓.</>}</div>
      {spChips(MW_KEY_IDS.map(x => [x, t(MW_KEYS[x].en, MW_KEYS[x].ko)]), k, chooseK)}
      {spChips(MW_RH.map((r, j) => [r.id, t('Rhythm ' + (j + 1), '리듬 ' + (j + 1))]), ri, chooseR)}
      <MwStaff k={k} rh={R} notes={notes} cur={cur} lit={lit} phr={phr} onSlot={(i) => { setCur(i); setMsg(null); }} per={mlxPer() === 2 ? 2 : 4}/>
      <div style={{margin:'6px 0 4px'}}><SpKb lo={0} hi={19} names={names} lit={litK} onTap={tap} label={t('Piano keys: the notes of ' + K.en + ' are named; the tonic is coral.', '피아노 건반: ' + K.ko + '의 음에 이름이 있고, 으뜸음은 산호색이에요.')}/></div>
      {msg ? spMsg(msg, BK.coral) : allOk ? spMsg(t('A question and an answer: a four-bar melody. ▶ Play it.', '질문과 대답: 4마디 선율이에요. ▶ 쳐 보세요.'), BK.green) : null}
      <div style={{display:'flex',gap:6,justifyContent:'center',flexWrap:'wrap',margin:'6px 0'}}>
        <button className="ghost-btn" style={spBtn} onClick={play}>{t('▶ Play', '▶ 듣기')}</button>
        <button className="ghost-btn" style={spBtn} onClick={back}>{t('⌫ Back', '⌫ 지우기')}</button>
        <button className="ghost-btn" style={spBtn} data-mw-phr onClick={() => setPhr(phr === null ? '22' : phr === '22' ? '4' : null)}>{t('Phrase marks: ', '프레이즈 표시: ') + phrW}</button>
        <button className="ghost-btn" style={spBtn} onClick={() => { T.clear(); setNotes(mwModel(k, R)); setPhr('22'); setCur(last); setMsg(null); }}>{t('An example', '보기')}</button>
        <button className="ghost-btn" style={spBtn} onClick={() => chooseR(ri)}>{t('Clear', '모두 지우기')}</button>
      </div>
      <div style={{display:'grid',gap:3,maxWidth:420,margin:'4px auto 0'}} data-mw-rules>
        {rules.map(([id, v]) => <div key={id} data-mw-rule={id + ':' + v} style={{display:'flex',gap:8,alignItems:'baseline',fontSize:14,fontWeight:800,color:v === true ? BK.green : v === false ? BK.coral : BK.muted}}>
          <span style={{width:16,flex:'0 0 16px',textAlign:'center',fontWeight:900}}>{v === true ? '✓' : v === false ? '✗' : '○'}</span><span>{t(MW_RULE_W[id][0], MW_RULE_W[id][1])}</span></div>)}
      </div>
    </div>
  );
}

// ── the drill: the strong syllables (the online exam's way: pick the right marks), the rhythm that fits the words, the
// last note that ends a melody on the tonic ──
const MW_KINDS = ['stress', 'wrhythm', 'mwend'];
const MW_LINES = MW_POEMS.flatMap(p => [0, 1].map(li => [p.id, li]));
function mwStressOpts(syls) {
  const ok = syls.map(x => x.s), n = syls.length, key = (m) => m.map(Number).join('');
  const late = ok.map((_, i) => i > 0 && ok[i - 1]), first = syls.map((x, i) => i === 0 || syls[i - 1].end), early = ok.map((_, i) => i < n - 1 && ok[i + 1]);
  const mixed = ok.slice(), j2 = ok.indexOf(true, ok.indexOf(true) + 1); if (j2 >= 0 && j2 < n - 1) { mixed[j2] = false; mixed[j2 + 1] = true; }
  const out = [ok]; [late, first, early, mixed].forEach(m => { if (out.length < 3 && m.some(Boolean) && !out.some(x => key(x) === key(m))) out.push(m); });
  return out.length === 3 ? out : null;
}
function mwRhythmOpts(syls, m) {
  const ok = mwStarts(syls), a = ok[0], m2 = m === 2 ? 3 : 2, every = (st, mm) => { const s = []; for (let i = st; i < syls.length; i += mm) s.push(i); return s; };
  const sets = [mwSet(syls, m, ok, { per: 9 }), mwSet(syls, m, every((a + 1) % m, m), { per: 9 }), mwSet(syls, m2, every(0, m2), { per: 9 })];
  return sets.every(Boolean) ? sets : null;
}
function genMwQuestion(lv, prev) {
  const uid = Math.random();
  for (let g = 0; g < 60; g++) {
    if (lv.kind === 'stress' || lv.kind === 'wrhythm') {
      const [pid, li] = pick(MW_LINES), key = lv.kind + pid + li; if (prev && prev.key === key && g < 50) continue;
      const syls = MW_SYL[pid][li], ms = lv.kind === 'stress' ? mwStressOpts(syls) : mwRhythmOpts(syls, mwPoem(pid).m); if (!ms) continue;
      const opts = shuffle(ms.map((m, j) => ({ m, ok: j === 0 }))).map((o, j) => ({ ...o, id: 'abc'[j] }));
      return { kind: lv.kind, key, pid, li, syls, opts, answer: opts.find(o => o.ok).id, choices: opts.map(o => o.id), uid };
    }
    const k = pick(MW_KEY_IDS), R = pick(MW_RH), key = 'e' + k + R.id; if (prev && prev.key === key && g < 50) continue;
    const K = MW_KEYS[k], names = [1, 5, 2].map(dg => mwName(K.t + dg - 1, k));
    return { kind: 'mwend', key, k, rh: R.id, notes: mwModel(k, R), answer: names[0], choices: shuffle(names.slice()), uid };
  }
  return null;
}
function mwAnswerLabel(q) {
  const o = q.opts && q.opts.find(x => x.ok), n = 'abc'.indexOf(q.answer) + 1;
  if (q.kind === 'stress') return t('line ' + n + ': ' + mwCaps(q.syls), n + '번: ' + mwCaps(q.syls));
  if (q.kind === 'wrhythm') return t('rhythm ' + n + ' (' + mwRhyTxt(o.m) + ')', n + '번 리듬(' + o.m.m + '/4)');
  return t(q.answer + ', the tonic of ' + MW_KEYS[q.k].en, q.answer + ', ' + MW_KEYS[q.k].ko + '의 으뜸음');
}
function MwQuestion({ q, given, locked, onAnswer, pixel, paper }) {
  const isDone = !!given, btnCls = pixel ? 'pixel-choice' : 'choice-btn', ink = pixel ? '#faf6ec' : 'var(--text)';
  const st = (c) => !isDone ? '' : (String(c) === String(q.answer) ? ' good' : (String(given.ans) === String(c) ? ' bad' : ''));
  const prompt = { stress: t('Which line has an upright line before each strong syllable?', '센 음절마다 그 앞에 세로줄이 있는 것은?'),
    wrhythm: t('Which rhythm fits the words? A strong syllable comes straight after each bar line.', '가사에 맞는 리듬은? 마디줄마다 바로 뒤에 센 음절이 와요.'),
    mwend: t('Which last note ends this melody on the tonic?', '이 선율을 으뜸음으로 끝내는 마지막 음은?') }[q.kind];
  const pic = q.kind === 'mwend' ? <div style={{maxWidth:paper ? 420 : 460,margin:'0 auto 8px',background:pixel ? '#fff' : 'transparent'}}><MwStaff k={q.k} rh={q.rh} notes={isDone ? q.notes : q.notes.slice(0, -1).concat([null])} cur={isDone ? null : q.notes.length - 1} lit={isDone ? q.notes.length - 1 : -1} phr="22" per={paper ? 4 : mlxPer() === 2 ? 2 : 4}/></div> : null;
  const body = (c) => { const o = q.opts && q.opts.find(x => x.id === c);
    if (q.kind === 'stress') return <MwMarked syls={q.syls} marks={o.m} size={pixel ? 12 : 16} col={pixel ? '#26296b' : undefined}/>;
    if (q.kind === 'wrhythm') return <div style={{width:'100%',minWidth:0,background:'#fff',borderRadius:6}}><MwRows rows={(paper || mlxPer() !== 2 ? o.m : mwSet(q.syls, o.m.m, o.m.starts, { per: 2 })).rows} o={{ D: 44, counts: false, hearts: false, wfs: 14.5 }} label={t('A rhythm with the words under it.', '가사가 아래에 있는 리듬.')}/></div>;
    return <span style={{fontSize:pixel ? 15 : 20,fontWeight:900}}>{c}</span>; };
  const cols = q.kind === 'mwend' ? 3 : 1;
  return <div>
    <p style={{fontSize:pixel ? 11.5 : 17,fontWeight:900,textAlign:'center',margin:'0 0 8px',color:ink,textWrap:'balance',wordBreak:'keep-all'}}>{prompt}</p>
    {pic}
    <div style={{display:'grid',gridTemplateColumns:'repeat(' + cols + ',minmax(0,1fr))',gap:8,maxWidth:q.kind === 'mwend' ? 360 : 520,margin:'0 auto'}}>{q.choices.map((c, j) => <button key={c} disabled={locked} data-mlx-choice={c} onClick={() => onAnswer(c)} className={btnCls + st(c)} style={{padding:q.kind === 'mwend' ? '10px 4px' : '8px 8px',minHeight:48,display:'flex',flexDirection:'column',alignItems:'center',gap:3}}>
      {q.kind !== 'mwend' && <span style={{fontSize:pixel ? 10 : 12,fontWeight:900,alignSelf:'flex-start'}}>{j + 1}</span>}{body(c)}</button>)}</div>
  </div>;
}

// ── the Workbook's two pages (they face Lesson Book pages 7 and 8) and the check-up's section E ──
const MW_WB = {
  mark: [['kites', 0], ['snow', 0], ['boat', 1], ['moon', 0]],
  rhy: [['kites', 1], ['hills', 0]],
  chk: [{ k: 'D', rh: 'r2', notes: mwModel('D', 'r2'), phr: '22' }, { k: 'F', rh: 'r1', notes: [3, 2, 3, 1, 2, 3, 1, 3, 4, 3, 4, 5].map(dg => MW_KEYS.F.t + dg - 1), phr: null }],
  write: [{ k: 'G', rh: 'r1' }, { k: 'F', rh: 'r2' }],
};
const MW_CHK_E = [['boat', 0], ['hills', 1]];
// a line of words on paper, room before each syllable for the upright line
function MwPaperLine({ syls, marks, size = 17 }) {
  return <div style={{display:'flex',flexWrap:'wrap',justifyContent:'center',alignItems:'baseline',gap:'4px 0',fontSize:size,fontWeight:700,color:BK.ink}}>{syls.map((x, i) => <span key={i} style={{paddingLeft:i > 0 && syls[i - 1].end ? 18 : 9,position:'relative'}}>{marks && marks[i] && <b style={{position:'absolute',left:i > 0 && syls[i - 1].end ? 9 : 2,color:BK.coral,fontWeight:900}}>|</b>}{mwTx(x)}</span>)}</div>;
}
// the words under a band to write the rhythm in (the strong syllables marked)
function MwPaperRhythm({ syls }) {
  return <div style={{display:'flex',flexDirection:'column',gap:2,maxWidth:600,margin:'0 auto',width:'100%'}}>
    <div style={{height:58,borderBottom:'1.3px solid ' + BK.line,margin:'0 0 0 0'}}/>
    <div style={{display:'grid',gridTemplateColumns:'repeat(' + syls.length + ',minmax(0,1fr))',fontSize:14.5,fontWeight:700,color:BK.ink,textAlign:'center',marginTop:6}}>{syls.map((x, i) => <span key={i}>{x.s && <b style={{color:BK.coral,marginRight:2}}>|</b>}{mwTx(x)}</span>)}</div>
  </div>;
}
const mwPaperTicks = (done) => <div style={{display:'grid',gap:3,marginTop:6}}>{done.map(([id, v]) => <div key={id} style={{display:'flex',gap:7,alignItems:'center',fontSize:11.5,fontWeight:700,color:BK.ink,lineHeight:1.25}}>
  <span style={{width:15,height:15,flex:'0 0 15px',border:'1.3px solid ' + BK.line,borderRadius:2,display:'inline-flex',alignItems:'center',justifyContent:'center',color:BK.coral,fontWeight:900,fontSize:13}}>{v === true ? '✓' : ''}</span>{MW_RULE_W[id][0]}</div>)}</div>;
function MwWbWords() {
  const W = MW_WB;
  return <>
    <WbTop step={6}/>
    <Part kind="together" title="Mark the strong syllables" how="Say each line. Draw an upright line (|) before each strong syllable: the ones you say with more weight. The first one is done.">
      <BkGrid cols={1} gap="6px">{W.mark.map(([pid, li], i) => { const s = MW_SYL[pid][li]; return <ExCell key={i} n={i + 1} ex={i === 0}>{sdyCol(<MwPaperLine syls={s} marks={i === 0 ? s.map(x => x.s) : null}/>, '14px 8px 10px')}</ExCell>; })}</BkGrid>
    </Part>
    <Part kind="home" title="Write the rhythm" how="The strong syllables are marked. Write the time signature, a note over each syllable and a bar line before each strong syllable. Hold the last syllable.">
      <BkGrid cols={1} gap="8px">{W.rhy.map(([pid, li], i) => <BkCell key={i} n={i + 5}>{sdyCol(<MwPaperRhythm syls={MW_SYL[pid][li]}/>, '6px 10px 10px')}</BkCell>)}</BkGrid>
    </Part>
    <Part kind="play" title="Clap and say" how="Clap your rhythms and say the words with them. Then play each on one note. Tick each.">
      {sskRowN(7, ivxTicks(['line 5', 'line 6', 'a rhyme I know']))}
    </Part>
    <Faces/>
  </>;
}
function MwWbWrite() {
  const W = MW_WB;
  return <>
    <WbTop step={7}/>
    <Part kind="together" title="Check the melody" how="Tick what each melody does. The first one is done.">
      <BkGrid cols={2} gap="8px 10px">{W.chk.map((m, i) => <ExCell key={i} n={i + 1} ex={i === 0}>{sdyCol(<>
        <div style={{fontSize:11.5,fontWeight:900,color:BK.muted,letterSpacing:'0.06em',margin:'0 0 2px'}}>{MW_KEYS[m.k].en.toUpperCase()}</div>
        <MwStaff k={m.k} rh={m.rh} notes={m.notes} phr={m.phr} per={2} label={MW_KEYS[m.k].en + ': a four-bar melody.'}/>
        {mwPaperTicks(mwRules(m.notes, m.rh, m.k, m.phr).map(([id, v]) => [id, i === 0 ? v : null]))}</>, '10px 8px 8px')}</ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Write a four-bar melody" how="Write a melody on the rhythm, in the key. Start on note 1, 3 or 5; move mostly by step; rest away from the tonic at the end of bar 2; end on the tonic; add phrase marks.">
      <BkGrid cols={1} gap="8px">{W.write.map((w, i) => <BkCell key={i} n={i + 3}>{sdyCol(<div style={{display:'flex',flexDirection:'column',gap:2,maxWidth:600,margin:'0 auto',width:'100%'}}>
        <div style={{display:'grid',gridTemplateColumns:'110px minmax(0,1fr)',alignItems:'center',gap:10}}><div style={{fontSize:11,fontWeight:900,letterSpacing:'0.08em',color:BK.muted}}>THE RHYTHM</div><div style={{maxWidth:360}}><SrhFit items={mwRhItems(w.rh)} o={{ D: 30, counts: false, hearts: false }} label="The rhythm to write on."/></div></div>
        <div style={{display:'grid',gridTemplateColumns:'110px minmax(0,1fr)',alignItems:'center',gap:10}}><div style={{fontSize:11,fontWeight:900,letterSpacing:'0.08em',color:BK.muted}}>{MW_KEYS[w.k].en.toUpperCase()}</div><MwStaff k={w.k} rh={w.rh} empty sp={1.35} label={'An empty staff in ' + MW_KEYS[w.k].en + '.'}/></div></div>, '8px 8px 10px')}</BkCell>)}</BkGrid>
    </Part>
    <Part kind="play" title="Play and sing" how="Play your melodies. Then sing them. Tick each.">
      {sskRowN(5, ivxTicks(['melody 3', 'melody 4', 'sung']))}
    </Part>
    <Faces/>
  </>;
}
'''
rep("""// ─── Phase 481: chapter 25's Workbook (pages 2 to 8:""", MW + """
// ─── Phase 481: chapter 25's Workbook (pages 2 to 8:""")

# ── the drill: three levels after 'Extra: what comes next?' ──
rep("""  { n: 9, label: 'Extra: what comes next?', kind: 'next', time: 16 },
];""", """  { n: 9, label: 'Extra: what comes next?', kind: 'next', time: 16 },
  { n: 10, label: 'Where are the strong syllables?', kind: 'stress', time: 14 },   // Build AO: page 7
  { n: 11, label: 'Which rhythm fits the words?', kind: 'wrhythm', time: 18 },   // Build AO: page 7
  { n: 12, label: 'Which note ends it on the tonic?', kind: 'mwend', time: 12 },   // Build AO: page 8
];
Object.assign(LEVEL_KO, { 'Where are the strong syllables?': '센 음절은 어디에?', 'Which rhythm fits the words?': '가사에 맞는 리듬은?', 'Which note ends it on the tonic?': '으뜸음으로 끝내는 음은?' });""")
rep("""function genMlxQuestion(lv, prev) {
  const uid = Math.random(), same = (key) => prev && prev.key === key;""",
    """function genMlxQuestion(lv, prev) {
  if (MW_KINDS.includes(lv.kind)) return genMwQuestion(lv, prev);   // Build AO
  const uid = Math.random(), same = (key) => prev && prev.key === key;""")
rep("""function mlxAnswerLabel0(q) {
""", """function mlxAnswerLabel0(q) {
  if (MW_KINDS.includes(q.kind)) return mwAnswerLabel(q);   // Build AO
""")
rep("""  useEffect(() => { if (ear && !locked) { const tm = setTimeout(hear, 350); return () => clearTimeout(tm); } }, [q.uid]);
""", """  useEffect(() => { if (ear && !locked) { const tm = setTimeout(hear, 350); return () => clearTimeout(tm); } }, [q.uid]);
  if (MW_KINDS.includes(q.kind)) return <div>{!paper && <BoardTrack b={board} pixel={pixel}/>}<MwQuestion q={q} given={given} locked={locked} onAnswer={(c) => { mlxStop(); onAnswer(c); }} pixel={pixel} paper={paper}/></div>;   // Build AO
""")

# ── the Lesson Book: two pages before the checks; seven checks ──
rep("""    cap(t('The same notes: repetition. The same shape a step higher or lower: sequence.', '같은 음으로 다시: 반복. 같은 모양으로 한 걸음 높거나 낮게: 동형 진행.'), 'c6')], 260, 26, 680);
""", """    cap(t('The same notes: repetition. The same shape a step higher or lower: sequence.', '같은 음으로 다시: 반복. 같은 모양으로 한 걸음 높거나 낮게: 동형 진행.'), 'c6')], 260, 26, 680);
  // p7 (Build AO): a couplet, its strong syllables marked, its rhythm with the words under it
  const kSyl = MW_SYL.kites, kFlat = kSyl[0].concat(kSyl[1]), kSet = mwSet(kFlat, 2, mwStarts(kFlat), { per: 4 });
  const p7 = stack([<div key="w" style={{textAlign:'center',display:'flex',flexDirection:'column',gap:2}}>{kSyl.map((l, j) => <div key={j}><MwMarked syls={l} marks={l.map(x => x.s)} size={20}/></div>)}</div>,
    <div key="r" style={{maxWidth:520,margin:'0 auto',width:'100%'}}><MwRows rows={kSet.rows} o={{ D: 46, counts: false, hearts: false }} label={t('The couplet as a rhythm in 2/4, a line a row: a bar line before each strong syllable, the words under the notes.', '두 줄 시를 2/4 리듬으로, 한 줄에 한 행: 센 음절마다 그 앞에 마디줄, 음표 아래에 가사.')}/></div>,
    cap(t('A bar line before each strong syllable; the last syllable of a line holds on.', '센 음절마다 그 앞에 마디줄을 긋고, 줄 끝 음절은 길게 끌어요.'), 'c7')], 330, 12, 640);
  // p8 (Build AO): a four-bar melody in G major on rhythm 1: a question (bars 1-2) and an answer (bars 3-4), phrase marks
  const lab8 = (en, ko, key) => <div key={key} style={{fontSize:12,fontWeight:900,letterSpacing:'0.08em',color:BK.muted,textAlign:'left',maxWidth:600,margin:'0 auto -4px',width:'100%'}}>{mlxKoT(t(en, ko)).toUpperCase()}</div>;
  const mark8 = (n, en, ko) => <div key={n} style={{display:'flex',gap:8,alignItems:'baseline',fontSize:scr ? 14 : 13.5,fontWeight:800,color:BK.ink,lineHeight:1.3}}><b style={{color:PEN_C,flex:'0 0 auto'}}>{n}</b><span>{mlxKoT(t(en, ko))}</span></div>;
  const p8 = stack([lab8('The rhythm', '리듬', 'l1'), <div key="r" style={{maxWidth:470,margin:'0 auto 0 0',width:'100%'}}><SrhFit items={mwRhItems('r1')} o={{ D: 34, counts: false, hearts: false }} label={t('The rhythm: four crotchets; two crotchets and a minim; four crotchets; a semibreve.', '리듬: 4분음표 넷, 4분음표 둘과 2분음표, 4분음표 넷, 온음표.')}/></div>,
    lab8('A melody on it, in G major', '그 리듬에 쓴 G장조 선율', 'l2'), <div key="m" style={{maxWidth:600,margin:'0 auto',width:'100%'}}><MwStaff k="G" rh="r1" notes={mwModel('G', 'r1')} hl={[0, 6, 11]} phr="22" label={t('A four-bar melody in G major: G A B G, A B A (a minim), B C D A, G (a semibreve), with a phrase mark over bars 1 and 2 and one over bars 3 and 4.', 'G장조의 4마디 선율: G A B G, A B A(2분음표), B C D A, G(온음표). 1·2마디와 3·4마디 위에 프레이즈 표시.')}/></div>,
    <div key="k" style={{display:'grid',gap:4,maxWidth:560,margin:'0 auto',width:'100%'}}>{mark8('1', 'It starts on G, note 1 (1, 3 or 5 are good starts).', 'G, 1번 음에서 시작해요(1, 3, 5번 음이 좋은 시작이에요).')}{mark8('2', 'Bar 2 rests on A, note 2: a question.', '2마디는 2번 음 A에서 쉬어요: 질문.')}{mark8('3', 'Bar 4 comes home to G, the tonic: the answer.', '4마디는 으뜸음 G로 돌아와요: 대답.')}</div>], 330, 12, 640);
""")
rep("""    seq: [{ k: 'raw', svg: dots([[8, 30], [16, 24], [24, 28], [32, 22]], PEN_N) + dots(""",
    """    words: [{ k: 'raw', svg: [[3, 'Kites'], [48, 'fly']].map(([x, w]) => '<line x1="' + x + '" x2="' + x + '" y1="11" y2="30" stroke="' + PEN_C + '" stroke-width="2.4"/><text x="' + (x + 4) + '" y="27" style="font-family:Inter, sans-serif" font-size="12" font-weight="900" fill="' + PEN_N + '">' + w + '</text>').join('') + '<text x="69" y="27" style="font-family:Inter, sans-serif" font-size="12" font-weight="700" fill="' + PEN_N + '">-ing</text>' }],   // Build AO
    write: [{ k: 'raw', svg: '<path d="M8 15 Q26 2 44 15" fill="none" stroke="' + PEN_N + '" stroke-width="1.8"/><path d="M50 15 Q68 2 86 15" fill="none" stroke="' + PEN_N + '" stroke-width="1.8"/>' + dots([[10, 32], [20, 28], [30, 25], [40, 28]], PEN_N) + dots([[52, 30], [62, 26], [72, 30], [84, 34]], PEN_N, 3) }],   // Build AO
    seq: [{ k: 'raw', svg: dots([[8, 30], [16, 24], [24, 28], [32, 22]], PEN_N) + dots(""")
rep("""    ['seq', t('I can play a motif in sequence, a step higher each time', '동기를 한 걸음씩 높여 동형 진행으로 칠 수 있어요')],
""", """    ['seq', t('I can play a motif in sequence, a step higher each time', '동기를 한 걸음씩 높여 동형 진행으로 칠 수 있어요')],
    ['words', t('I can mark strong syllables and clap the words', '센 음절에 표시하고 가사를 손뼉으로 칠 수 있어요')],   // Build AO
    ['write', t('I can write a four-bar melody on a rhythm', '주어진 리듬에 4마디 선율을 쓸 수 있어요')],   // Build AO
""")
rep("""[t('Repetition and sequence', '반복과 동형 진행'), 6], [t('My five checks', '나의 다섯 가지 확인'), 7]]""",
    """[t('Repetition and sequence', '반복과 동형 진행'), 6], [t('Words and rhythm', '가사와 리듬'), 7], [t('Writing a melody', '선율 쓰기'), 8], [t('My seven checks', '나의 일곱 가지 확인'), 9]]""")
rep("""    <LbPage key="7" no={7} chId={ch} kicker={t('Check-up', '점검')} title={t('My five checks', '나의 다섯 가지 확인')}>
      <LbSay>{t('Show each one at the piano, on its page (1 to 4, and 6). The check-up on paper is in the Workbook.', '1~4쪽과 6쪽을 하나씩 펴고 피아노 앞에서 보여 줘요. 종이 점검은 워크북에 있어요.')}</LbSay>""",
    """    <LbPage key="7" no={7} chId={ch} kicker={t('Step 6', '6단계')} title={t('Words and rhythm', '가사와 리듬')}>
      {live(p7, <MwWordsPad/>)}
      <LbDefs items={[
        [t('couplet', '두 줄 시'), X('Two lines of words that belong together, often ending in a rhyme.', '함께 짝을 이루는 두 줄의 가사. 끝말의 운이 맞는 일이 많아요.')],
        [t('strong syllable', '센 음절'), X('A syllable, or a short word, said with more weight: KITES are FLY-ing.', '더 힘주어 말하는 음절이나 짧은 낱말: KITES are FLY-ing.')],
      ]}/>
      <LbPiano steps={[
        X('Say the couplet and clap on each strong syllable. Then draw an upright line before each one.', '두 줄 시를 말하면서 센 음절마다 손뼉을 쳐요. 그다음 센 음절마다 그 앞에 세로줄을 그어요.'),
        X('Clap the rhythm and say the words with it. Then play it on one note.', '리듬을 손뼉으로 치면서 가사를 함께 말해요. 그다음 한 음으로 쳐요.'),
      ]}/>
      <LbRemember>{X('Strong syllables on strong beats: a bar line before each one.', '센 음절은 센박에: 센 음절마다 그 앞에 마디줄.')}</LbRemember>
    </LbPage>,

    <LbPage key="8" no={8} chId={ch} kicker={t('Step 7', '7단계')} title={t('Writing a melody', '선율 쓰기')}>
      {live(p8, <MwWritePad/>)}
      <LbDefs items={[
        [t('phrase mark', '프레이즈 표시'), X('A curved line over the notes of a phrase.', '프레이즈의 음들 위에 긋는 곡선.')],
      ]}/>
      <LbPiano steps={[
        X('Play the example and sing it. Then write your own on the same rhythm and play it.', '보기를 치고 노래해요. 그다음 같은 리듬에 나의 선율을 써서 쳐요.'),
        X('Write one in F major and one in D major. End each on its tonic.', 'F장조로 하나, D장조로 하나 써요. 모두 으뜸음에서 끝내요.'),
      ]}/>
      <LbRemember>{X('Bars 1 and 2 ask; bars 3 and 4 answer and come home to the tonic.', '1·2마디는 묻고, 3·4마디는 대답하며 으뜸음으로 돌아와요.')}</LbRemember>
    </LbPage>,

    <LbPage key="9" no={9} chId={ch} kicker={t('Check-up', '점검')} title={t('My seven checks', '나의 일곱 가지 확인')}>
      <LbSay>{t('Show each one at the piano, on its page (1 to 4, and 6 to 8). The check-up on paper is in the Workbook.', '1~4쪽과 6~8쪽을 하나씩 펴고 피아노 앞에서 보여 줘요. 종이 점검은 워크북에 있어요.')}</LbSay>""")
# the screen lesson: the steps keep the keys they were stored under (the checks k6, my tune k7); the new steps k8, k9
rep("""function MlxLearn({ onStart }) {""", """const MLX_STORE = ['k1', 'k2', 'k3', 'k4', 'k5', 'k8', 'k9', 'k6'];   // Build AO: pages 2 to 9 (the checks keep k6, my tune k7)
function MlxLearn({ onStart }) {""")
rep_in("function MlxLearn({ onStart }) {", "const MLX_LEVELS = [", """        <Step key={i} title={<span>{pg.props.title}</span>} storeAs={'k' + (i + 1)}>
          <LbScreenPage page={pg}/>""", """        <Step key={i} title={<span>{pg.props.title}</span>} storeAs={MLX_STORE[i] || 'k' + (i + 1)}>
          <LbScreenPage page={pg}/>""")

# ── the Workbook: two pages before my piece; my piece now faces step 9 (my tune); the check-up's section E ──
rep("""  P(<MlxMyPiece/>);
  P(<MlxPaperCheck/>);""", """  P(<MwWbWords/>);   // Build AO: faces page 7
  P(<MwWbWrite/>);   // Build AO: faces page 8
  P(<MlxMyPiece/>);
  P(<MlxPaperCheck/>);""")
rep_in("function MlxMyPiece() {", "function MlxPaperCheck() {", "<WbTop step={7}/>", "<WbTop step={9}/>")
rep("""const mlxChkNo = () => { const C = MLX_CHK, nB = C.line.length + 1, nC = nB + C.qa.length, nD = nC + C.word.length; return { nB, nC, nD, total: nD + C.rs.length - 1 }; };""",
    """const mlxChkNo = () => { const C = MLX_CHK, nB = C.line.length + 1, nC = nB + C.qa.length, nD = nC + C.word.length, nE = nD + C.rs.length; return { nB, nC, nD, nE, total: nE + MW_CHK_E.length - 1 }; };   // Build AO: E""")
rep_in("function MlxPaperCheck() {", "function MlxTeacher() {", "const C = MLX_CHK, { nB, nC, nD } = mlxChkNo();", "const C = MLX_CHK, { nB, nC, nD, nE } = mlxChkNo();")
rep_in("function MlxPaperCheck() {", "function MlxTeacher() {", """  </div>;
}""", """    {bkSec('E', 'Draw an upright line before each strong syllable.')}
    <BkGrid cols={1} gap="5px">{MW_CHK_E.map(([pid, li], i) => <BkCell key={i} n={nE + i}>{sdyCol(<MwPaperLine syls={MW_SYL[pid][li]} size={15}/>, '12px 6px 8px')}</BkCell>)}</BkGrid>
  </div>;
}""")
# room for E: the staves of A and B a little smaller, the writing lines of C a little shorter
# room for E: section B's three phrases side by side, like section D
rep_in("function MlxPaperCheck() {", "function MlxTeacher() {", """<BkGrid cols={1} gap="5px">{C.qa.map((bars, i) => <BkCell key={i} n={nB + i}>{sdyCol(<div style={{display:'grid',gridTemplateColumns:'minmax(0,400px) 200px',justifyContent:'center',alignItems:'center',gap:18}}>{mlxWbRow(bars, { D: 17, end: false })}{mlxWbWords(['question', 'answer'])}</div>, '3px 4px 2px')}</BkCell>)}</BkGrid>""",
    """<BkGrid cols={2} gap="6px 10px">{C.qa.map((bars, i) => <BkCell key={i} n={nB + i}>{sdyCol(<>{mlxWbRow(bars, { D: 17, end: false })}<div style={{marginTop:'auto'}}>{mlxWbWords(['question', 'answer'])}</div></>, '16px 6px 8px')}</BkCell>)}</BkGrid>""")
rep("""const mlxChkNo = () =>""", """MLX_CHK.qa = MLX_CHK.qa.slice(0, 2);   // Build AO: a question and an answer, side by side (room for section E)
const mlxChkNo = () =>""")

# ── the Teacher copy: pages 7 and 8; my piece 9, the check-up 10 (with E) ──
TA = "function MlxTeacher() {"
TB = "WORKBOOKS['melody'] = MlxWorkbook;"
rep_in(TA, TB, "its motif (repetition and sequence). Chapter ", "its motif (repetition and sequence); then writing: a rhythm for a couplet, a four-bar melody (Theory of Music Grades 2 and 3, Creative). Chapter ")
rep_in(TA, TB, "const W = MLX_WB, C = MLX_CHK, pages = [], { nB, nC, nD, total } = mlxChkNo();", "const W = MLX_WB, C = MLX_CHK, pages = [], { nB, nC, nD, nE, total } = mlxChkNo();")
NEW78 = """    <TcBlock page={7} title="Words and rhythm" answers={<>{sscLesson('The couplet said, clapped on its strong syllables and marked; its rhythm clapped with the words, then played on one note.')}{skgTcAns('TRY IT', MW_WB.mark.map(([pid, li], i) => mwCaps(MW_SYL[pid][li]) + done(i)))}{skgTcAns('YOUR TURN', MW_WB.rhy.map(([pid, li]) => { const sy = MW_SYL[pid][li]; return mwRhyTxt(mwSet(sy, mwPoem(pid).m, mwStarts(sy))); }), 5)}
      <div style={{fontSize:12,color:BK.ink,marginTop:4,lineHeight:1.5}}>Here every strong syllable starts a bar: 2/4 for strong-weak words, 3/4 for strong-weak-weak. Just as right: 4/4 with two strong syllables a bar, 6/8 for the three-syllable lines, longer notes on the important words. The couplets are new, written for this book. Grade 2 asks only for the marks; Grade 3 for the rhythm too.</div></>}
      watch="A syllable marked for its spelling or its length rather than for how it is said. Every word marked, the small ones too (the, a, and). A bar line before a weak syllable, so the words are said with the wrong weight. The last syllable of a line cut short."
      say="“A bar line before each strong syllable.”"/>
  </>);
  P(<>
    <TcBlock page={8} title="Writing a melody" answers={<>{sscLesson('The example played and sung; a melody of the student’s own on the same rhythm, in G major and in one more key, played and sung.')}{skgTcAns('TRY IT', ['all five (done)', 'starts on note 3, mostly by step; but bar 2 ends on the tonic (no question), the end is note 5 (no answer), no phrase marks'])}<div style={{fontSize:12,color:BK.ink,lineHeight:1.5}}>YOUR TURN: any melody on the rhythm, in the key, with the five points. One answer each:</div>{skgTcAns('', MW_WB.write.map(w => mwModel(w.k, w.rh).map(d => mwName(d, w.k)).join(' ')), 3)}
      <div style={{fontSize:12,color:BK.ink,marginTop:4,lineHeight:1.5}}>The five points are the usual textbook guidance for a four-bar melody, not the syllabus’s words (Grade 3: four bars, a major key up to two sharps or flats, on a given rhythm, with phrasing); a good melody may break one on purpose. Phrase marks: one over bars 1–2 and one over 3–4, or one over all four.</div></>}
      watch="Notes outside the key (an F, not F♯, in G major: the key signature already sharpens it). The tonic reached by a big leap. A question that already ends on the tonic. Phrase marks forgotten, or one over every bar."
      say="“Ask in bars 1 and 2; answer in bars 3 and 4.”"/>
"""
rep_in(TA, TB, """    <TcBlock page={7} title="Any piece: my piece’s melody (a fresh copy for each piece)\"""", NEW78 + """    <TcBlock page={9} title="Any piece: my piece’s melody (a fresh copy for each piece)\"""")
rep_in(TA, TB, """<TcBlock page={8} title="The check-up on paper (the Workbook’s last page)\"""", """<TcBlock page={10} title="The check-up on paper (the Workbook’s last page)\"""")
rep_in(TA, TB, """      {skgTcAns('D', C.rs.map(([, h]) => mlxRsNm(h)), nD)}
""", """      {skgTcAns('D', C.rs.map(([, h]) => mlxRsNm(h)), nD)}
      {skgTcAns('E', MW_CHK_E.map(([pid, li]) => mwCaps(MW_SYL[pid][li])), nE)}
""")
rep_in(TA, TB, "D {C.rs.length}; {total} in all.", "D {C.rs.length}, E {MW_CHK_E.length}; {total} in all.")
rep_in(TA, TB, "(My five checks, Lesson Book page 7).", "(My seven checks, Lesson Book page 9).")
rep_in(TA, TB, "{ id: 'd', step: '5', page: '6' }]}/>", "{ id: 'd', step: '5', page: '6' }, { id: 'e', step: '6', page: '7' }]}/>")
rep_in(TA, TB, "9 extra: what comes next in the sequence.</div>", "9 extra: what comes next in the sequence · 10 where are the strong syllables · 11 which rhythm fits the words · 12 which last note ends it on the tonic.</div>")
rep_in(TA, TB, "<b style={{color:BK.coral}}>My five checks (Lesson Book page 7).</b>", "<b style={{color:BK.coral}}>My seven checks (Lesson Book page 9).</b>")
rep_in(TA, TB, "5. Play page 6’s motif in sequence, a step higher each time. Got it!", "5. Play page 6’s motif in sequence, a step higher each time. 6. Mark a couplet’s strong syllables and clap its rhythm (page 7). 7. Write a four-bar melody on a rhythm, with phrase marks, ending on the tonic, and play it (page 8). Got it!")

# ── the Home: two lessons in the Melody room, on the Grades 2-3 floor ──
rep("""  { id: 'mlx-build', ch: 'melody', title: 'My tune',""", """  { id: 'mlx-words', ch: 'melody', title: 'Words and rhythm', blurb: 'Mark the strong syllables of a couplet; hear its rhythm.', C: () => <MwWordsPad/> },   // Build AO
  { id: 'mlx-write', ch: 'melody', title: 'Write a four-bar melody', blurb: 'A question and an answer on a given rhythm, in a major key.', C: () => <MwWritePad/> },   // Build AO
  { id: 'mlx-build', ch: 'melody', title: 'My tune',""")
rep("""  'mlx-build': ['나의 선율', '동기, 동기로 만든 두 마디, 마지막 음: 질문처럼, 또는 대답처럼 끝나요.'],""",
    """  'mlx-words': ['가사와 리듬', '두 줄 시의 센 음절에 표시하고 리듬을 들어요.'],   // Build AO
  'mlx-write': ['4마디 선율 쓰기', '주어진 리듬에 장조로 질문과 대답을 써요.'],   // Build AO
  'mlx-build': ['나의 선율', '동기, 동기로 만든 두 마디, 마지막 음: 질문처럼, 또는 대답처럼 끝나요.'],""")
rep("""'mlx-seq': ['melody', 1, 3, 'show ear'], 'mlx-build': ['melody', 1, 3, 'show ear'],""",
    """'mlx-seq': ['melody', 1, 3, 'show ear'], 'mlx-words': ['melody', 2, 3, 'show ear'], 'mlx-write': ['melody', 3, 3, 'show ear'], 'mlx-build': ['melody', 1, 3, 'show ear'],""")
rep("""  'melody': ['mlx-map', 'mlx-line', 'mlx-phrasing', 'mlx-qa', 'mlx-motif', 'mlx-seq', 'mlx-build', 'tune-anatomy',""",
    """  'melody': ['mlx-map', 'mlx-line', 'mlx-phrasing', 'mlx-qa', 'mlx-motif', 'mlx-seq', 'mlx-words', 'mlx-write', 'mlx-build', 'tune-anatomy',""")
rep("""'mlx-seq': 'c-map', 'modes':""", """'mlx-seq': 'c-map', 'mlx-words': 'c-map', 'mlx-write': 'c-map', 'modes':""")
rep("""lessons: ['mlx-map', 'mlx-line', 'mlx-phrasing', 'mlx-qa', 'mlx-motif', 'mlx-seq', 'mlx-build', 'phrase-marks',""",
    """lessons: ['mlx-map', 'mlx-line', 'mlx-phrasing', 'mlx-qa', 'mlx-motif', 'mlx-seq', 'mlx-words', 'mlx-write', 'mlx-build', 'phrase-marks',""")
rep("""    + ' mlx-map mlx-line mlx-phrasing mlx-qa mlx-motif mlx-seq mlx-build phrase-marks');""",
    """    + ' mlx-map mlx-line mlx-phrasing mlx-qa mlx-motif mlx-seq mlx-words mlx-write mlx-build phrase-marks');""")
rep("""'melody': 'Prelim–G2', 'form': 'G1–G3',""", """'melody': 'Prelim–G3', 'form': 'G1–G3',""")
rep("""  'melody': 'melody tune line contour high point phrase phrasing phrase mark breath mark comma question answer antecedent consequent period cadence motif repetition sequence tonic',""",
    """  'melody': 'melody tune line contour high point phrase phrasing phrase mark breath mark comma question answer antecedent consequent period cadence motif repetition sequence tonic words couplet syllable accent strong syllable rhythm for words writing a melody four-bar melody composing',""")

open(dst, 'w', encoding='utf-8').write(s)
print('ok')
