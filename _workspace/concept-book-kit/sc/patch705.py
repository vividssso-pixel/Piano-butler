import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build AL (board call 14, the third Grades 2-3 room): Intervals and Chords Further, Theory of Music Grades 2 and 3 (Manual of
# Syllabuses 2026, Theory of Music, read 26 Oct): G2 intervals above the tonic, quality and number, treble clef, in the grade's
# keys (adds A, E and D harmonic minor); G3 the same in treble or bass clef (adds G and C minor) and the technical names of the
# degrees; G3 chords: the three primary triads in close position, root position and first inversion, treble or bass; the
# perfect and plagal cadences in four-part vocal style; general knowledge: the approximate compass of soprano, alto, tenor and
# bass in choral writing. The ranges used here are the usual textbook ones: flagged for her.

rep("""const SCALES_23_DRILL = { id: 'scales-23', label: 'Scales Further' };   // Build AK: Grades 2-3 scales""",
    """const SCALES_23_DRILL = { id: 'scales-23', label: 'Scales Further' };   // Build AK: Grades 2-3 scales
const HARMONY_23_DRILL = { id: 'harmony-23', label: 'Intervals and Chords Further' };   // Build AL: Grades 2-3 theory""")
rep("""  { id: 'scales-23', label: 'Scales Further', concept: SCALES_23_DRILL, track: 'start' },   // Build AK""",
    """  { id: 'scales-23', label: 'Scales Further', concept: SCALES_23_DRILL, track: 'start' },   // Build AK
  { id: 'harmony-23', label: 'Intervals and Chords Further', concept: HARMONY_23_DRILL, track: 'start' },   // Build AL""")
rep("""'scales-23': '스케일 한 걸음 더'""", """'scales-23': '스케일 한 걸음 더', 'harmony-23': '음정과 화음 한 걸음 더'""")
rep("""'scales-23': ['scale-play', 'minor-scales']""", """'scales-23': ['scale-play', 'minor-scales'], 'harmony-23': ['intervals', 'chords']""")
rep("""'scales-23': ['Scales further', '스케일 더']""", """'scales-23': ['Scales further', '스케일 더'], 'harmony-23': ['Chords further', '화음 더']""")
rep("""  'scales-23': 'scales grade 2 grade 3""", """  'harmony-23': 'intervals chords grade 2 grade 3 theory above the tonic major minor perfect bass clef degree names tonic supertonic mediant subdominant dominant submediant leading note primary triads first inversion soprano alto tenor bass four part vocal cadence perfect plagal',
  'scales-23': 'scales grade 2 grade 3""")
rep("""'scales-23': 'k-play', 'key-signatures': 'p-scales',""", """'scales-23': 'k-play', 'harmony-23': 'p-chords', 'key-signatures': 'p-scales',""")
rep("""  { ids: ['melody', 'listen-23', 'scales-23', 'more-scales'], en: ['Grades 2–3', 'How a tune is shaped, your ears a step further, and scales a step further.'], ko: ['Grade 2–3', '선율의 모양, 귀를 한 걸음 더, 그리고 스케일 한 걸음 더.'] },""",
    """  { ids: ['melody', 'listen-23', 'scales-23', 'harmony-23', 'more-scales'], en: ['Grades 2–3', 'How a tune is shaped, your ears, scales, intervals and chords a step further.'], ko: ['Grade 2–3', '선율의 모양, 그리고 귀, 스케일, 음정과 화음을 한 걸음 더.'] },   // Build AL: Intervals and Chords Further""")
rep("""    { id: 'ch-key', en: 'Chords in a key', ko: '조 안의 화음', lessons: ['ch-tonic', 'ch-145', 'ch-seven', 'ch-inv', 'ch-cad'], check: 'chords', level: 7 },""",
    """    { id: 'ch-key', en: 'Chords in a key', ko: '조 안의 화음', lessons: ['ch-tonic', 'ch-145', 'ch-seven', 'ch-inv', 'ch-cad'], check: 'chords', level: 7 },
    { id: 'ch-23', en: 'Intervals and chords further', ko: '음정과 화음 한 걸음 더', lessons: ['h3-iv', 'h3-deg', 'h3-inv', 'h3-satb', 'h3-cad'], check: 'harmony-23' },   // Build AL""")
rep("""  set('23', 'scf-thumb scf-meet scf-mel scf-mirror scf-chrom');""", """  set('23', 'scf-thumb scf-meet scf-mel scf-mirror scf-chrom');
  set('23', 'h3-iv h3-deg h3-inv h3-satb h3-cad');   // Build AL: Intervals and Chords Further""")

CH = r'''
// ─── Chapter: Intervals and Chords Further (Build AL, 2026-10-26; board call 14, the third Grades 2-3 room) ───
// Theory of Music Grades 2 and 3: intervals above the tonic in a minor key (quality and number; Grade 3 in the bass clef too);
// the degree names; the primary triads in root position and first inversion; soprano, alto, tenor and bass; the perfect and
// plagal cadences in four-part vocal style. Every chord below is spelled by hand: root doubled, the leading note rising, the
// common note kept, no parallel 5ths or octaves (checked pair by pair), each voice inside its usual range.
const H3_L = 'CDEFGAB';
const h3N = (str) => { const m = /^([A-G])([#b]?)(\d)$/.exec(str); return { d: Number(m[3]) * 7 + H3_L.indexOf(m[1]), acc: m[2] === '#' ? 1 : m[2] === 'b' ? -1 : 0 }; };
const h3Let = (n) => H3_L[((n.d % 7) + 7) % 7] + (n.acc > 0 ? '♯' : n.acc < 0 ? '♭' : '');
const h3Semi = (n) => ivMidi(n) - 60;   // semitones from middle C, for spPlay
const h3Play = (chords, bpm = 60, gap = 2) => spPlay(chords.map((c, i) => ({ at: i * gap, keys: c.map(h3Semi), len: gap * 0.9, vol: 0.11 })), bpm);
const H3_ORD = ['', '', '2nd', '3rd', '4th', '5th', '6th', '7th', 'octave'], H3_ORDK = ['', '', '2도', '3도', '4도', '5도', '6도', '7도', '8도'];
const H3_QW = { M: ['major', '장'], m: ['minor', '단'], P: ['perfect', '완전'] };
const h3IvName = (q, n) => t(H3_QW[q][0] + ' ' + H3_ORD[n], H3_QW[q][1] + H3_ORDK[n]);
// step 1: above the tonic in a harmonic minor key (the key's own notes, the raised 7th)
const H3_MIN = {
  Am: { g: 2, en: 'A minor', ko: 'A단조', tr: 'A4', bs: 'A2', acc: { G: 1 } },
  Em: { g: 2, en: 'E minor', ko: 'E단조', tr: 'E4', bs: 'E3', acc: { F: 1, D: 1 } },
  Dm: { g: 2, en: 'D minor', ko: 'D단조', tr: 'D4', bs: 'D3', acc: { B: -1, C: 1 } },
  Gm: { g: 3, en: 'G minor', ko: 'G단조', tr: 'G4', bs: 'G2', acc: { B: -1, E: -1, F: 1 } },
  Cm: { g: 3, en: 'C minor', ko: 'C단조', tr: 'C4', bs: 'C3', acc: { E: -1, A: -1 } },
};
const H3_MIN_KEYS = ['Am', 'Em', 'Dm', 'Gm', 'Cm'];
const H3_QMIN = [null, null, 'M', 'm', 'P', 'P', 'm', 'M', 'P'], H3_QMAJ = [null, null, 'M', 'M', 'P', 'P', 'M', 'M', 'P'];
const H3_DIST = { 2: [['M', 2], ['m', 2], ['m', 3]], 3: [['m', 3], ['M', 3], ['P', 4]], 4: [['P', 4], ['P', 5], ['m', 3]], 5: [['P', 5], ['P', 4], ['m', 6]], 6: [['m', 6], ['M', 6], ['P', 5]], 7: [['M', 7], ['m', 7], ['m', 6]], 8: [['P', 8], ['M', 7], ['P', 5]] };
const h3Above = (k, clef, n) => { const c = H3_MIN[k], t0 = h3N(clef === 'bass' ? c.bs : c.tr), d = t0.d + n - 1, L = H3_L[((d % 7) + 7) % 7]; return [t0, { d, acc: c.acc[L] || 0 }]; };
// step 2: the degree names
const H3_DEGN = [['tonic', '으뜸음'], ['supertonic', '윗으뜸음'], ['mediant', '가온음'], ['subdominant', '버금딸림음'], ['dominant', '딸림음'], ['submediant', '버금가온음'], ['leading note', '이끎음']];
const h3DegName = (i) => t(H3_DEGN[i][0], H3_DEGN[i][1]);
// step 3: the primary triads, root position and first inversion (close position)
const H3_TRI = {
  C: { en: 'C major', ko: 'C장조', tr: 'C4', bs: 'C3', acc: {} },
  G: { en: 'G major', ko: 'G장조', tr: 'G4', bs: 'G2', acc: { F: 1 } },
  F: { en: 'F major', ko: 'F장조', tr: 'F4', bs: 'F2', acc: { B: -1 } },
  D: { en: 'D major', ko: 'D장조', tr: 'D4', bs: 'D3', acc: { F: 1, C: 1 } },
  Bb: { en: 'B♭ major', ko: 'B♭장조', tr: 'Bb3', bs: 'Bb2', acc: { B: -1, E: -1 } },
  Am: { en: 'A minor', ko: 'A단조', tr: 'A3', bs: 'A2', acc: { G: 1 }, minor: true },
};
const H3_TRI_KEYS = ['C', 'G', 'F', 'D', 'Bb', 'Am'];
const H3_ROM = { 1: ['I', 'i'], 4: ['IV', 'iv'], 5: ['V', 'V'] };
const h3Rom = (k, deg) => H3_ROM[deg][H3_TRI[k].minor ? 1 : 0];
const h3Triad = (k, deg, clef, inv) => { const c = H3_TRI[k], t0 = h3N(clef === 'bass' ? c.bs : c.tr), r = t0.d + deg - 1;
  const ns = [r, r + 2, r + 4].map(d => ({ d, acc: c.acc[H3_L[((d % 7) + 7) % 7]] || 0 }));
  return inv ? [ns[1], ns[2], { d: ns[0].d + 7, acc: ns[0].acc }] : ns; };
// steps 4 and 5: four voices; the cadences, spelled by hand (soprano, alto, tenor, bass)
const H3_RANGE = { S: ['C4', 'G5'], A: ['G3', 'C5'], T: ['C3', 'G4'], B: ['E2', 'C4'] };
const H3_VOICE = { S: ['soprano', '소프라노'], A: ['alto', '알토'], T: ['tenor', '테너'], B: ['bass', '베이스'] };
const h3Voice = (v) => t(H3_VOICE[v][0], H3_VOICE[v][1]);
const H3_CAD = {
  C: { en: 'C major', ko: 'C장조', ks: [null, 0], perfect: [['B4', 'G4', 'D4', 'G3'], ['C5', 'G4', 'E4', 'C3']], plagal: [['C5', 'A4', 'F4', 'F3'], ['C5', 'G4', 'E4', 'C3']] },
  G: { en: 'G major', ko: 'G장조', ks: ['sharp', 1], perfect: [['F#4', 'D4', 'A3', 'D3'], ['G4', 'D4', 'B3', 'G2']], plagal: [['G4', 'E4', 'C4', 'C3'], ['G4', 'D4', 'B3', 'G2']] },
  F: { en: 'F major', ko: 'F장조', ks: ['flat', 1], perfect: [['E4', 'C4', 'G3', 'C3'], ['F4', 'C4', 'A3', 'F2']], plagal: [['F4', 'D4', 'Bb3', 'Bb2'], ['F4', 'C4', 'A3', 'F2']] },
  D: { en: 'D major', ko: 'D장조', ks: ['sharp', 2], perfect: [['C#5', 'A4', 'E4', 'A3'], ['D5', 'A4', 'F#4', 'D3']], plagal: [['D5', 'B4', 'G4', 'G3'], ['D5', 'A4', 'F#4', 'D3']] },
  Am: { en: 'A minor', ko: 'A단조', ks: [null, 0], minor: true, perfect: [['G#4', 'E4', 'B3', 'E3'], ['A4', 'E4', 'C4', 'A2']], plagal: [['A4', 'F4', 'D4', 'D3'], ['A4', 'E4', 'C4', 'A2']] },
  Dm: { en: 'D minor', ko: 'D단조', ks: ['flat', 1], minor: true, perfect: [['C#5', 'A4', 'E4', 'A3'], ['D5', 'A4', 'F4', 'D3']], plagal: [['D5', 'Bb4', 'G4', 'G3'], ['D5', 'A4', 'F4', 'D3']] },
};
const H3_CAD_KEYS = ['C', 'G', 'F', 'D', 'Am', 'Dm'];
const h3CadChords = (k, id) => H3_CAD[k][id].map(ch => { const [S, A, T, B] = ch.map(h3N); return { S, A, T, B }; });
const h3CadRom = (k, id) => (id === 'perfect' ? ['V', H3_CAD[k].minor ? 'i' : 'I'] : H3_CAD[k].minor ? ['iv', 'i'] : ['IV', 'I']);
const h3CadName = (id) => (id === 'perfect' ? t('perfect cadence', '정격종지') : t('plagal cadence', '변격종지'));
const h3KeyOfCad = (k) => t(H3_CAD[k].en, H3_CAD[k].ko);

// ── the grand staff for four voices: soprano and alto on the treble staff (stems up, down), tenor and bass on the bass staff ──
const H3_GAP = 60;
function SatbStaff({ chords, ks = [null, 0], labels, width = 300, hi = null, bands = null, stems = true }) {
  const yT = (d) => dY(d), yB = (d) => dY(d) + H3_GAP, yOf = (d, st) => (st === 'bass' ? yB(d) : yT(d));
  const ksN = ks[0] ? ks[1] : 0, x0 = 46 + ksN * 10, n = chords.length;
  const xOf = (i) => (n === 1 ? (x0 + width) / 2 + 6 : x0 + 30 + i * ((width - x0 - 54) / Math.max(1, n - 1)));
  const sig = ks[0] ? (ks[0] === 'sharp' ? SHARP_ORDER : FLAT_ORDER).slice(0, ksN) : [];
  const sigAcc = {}; sig.forEach(a => { sigAcc[a[0]] = ks[0] === 'sharp' ? 1 : -1; });
  const yTop = yT(40) - 30, yBot = yB(12) + (labels ? 26 : 4);
  const voice = (v, nt, x, st, i) => { const y = yOf(nt.d, st), L = H3_L[((nt.d % 7) + 7) % 7], showAcc = (sigAcc[L] || 0) !== nt.acc, on = hi && hi.i === i && hi.v === v, col = on ? BK.coral : BK.ink, up = v === 'S' || v === 'T';
    const low = st === 'bass' ? 18 : 30, high = st === 'bass' ? 26 : 38;
    return <g key={v + i}>
      {ledgersFor(nt.d, low, high).map(p => <line key={p} x1={x - 11} x2={x + 11} y1={yOf(p, st)} y2={yOf(p, st)} stroke={BK.ink} strokeWidth="1.3"/>)}
      {showAcc && (nt.acc > 0 ? <SharpShape x={x - 16} y={y} color={col}/> : nt.acc < 0 ? <FlatShape x={x - 15} y={y} color={col}/> : <NaturalShape x={x - 15} y={y} color={col}/>)}
      <ellipse cx={x} cy={y} rx="6.6" ry="4.8" transform={`rotate(-20 ${x} ${y})`} fill="#fff" stroke={col} strokeWidth="2.2"/>
      {stems && <line x1={up ? x + 6 : x - 6} x2={up ? x + 6 : x - 6} y1={y + (up ? -1 : 1)} y2={y + (up ? -32 : 32)} stroke={col} strokeWidth="1.6"/>}
    </g>; };
  const band = (v) => { const [lo, hi2] = H3_RANGE[v].map(h3N), st = v === 'S' || v === 'A' ? 'treble' : 'bass'; return <rect key={'b' + v} x={x0 + 8} width={width - x0 - 14} y={yOf(hi2.d, st) - 3} height={yOf(lo.d, st) - yOf(hi2.d, st) + 6} rx="4" fill="#fbe3da" opacity="0.8"/>; };
  return (
    <svg viewBox={`0 ${yTop} ${width} ${yBot - yTop}`} style={{width:'100%',maxWidth:width * 1.5,display:'block',margin:'0 auto'}}>
      {bands && bands.map(band)}
      {['treble', 'bass'].map(st => CLEFS[st].lines.map(l => <line key={st + l} x1="4" x2={width - 4} y1={yOf(l, st)} y2={yOf(l, st)} stroke={BK.ink} strokeOpacity="0.55" strokeWidth="1.2"/>))}
      <line x1="4" x2="4" y1={yT(38)} y2={yB(18)} stroke={BK.ink} strokeWidth="1.4"/>
      {['treble', 'bass'].map(st => <ClefGlyph key={'c' + st} clef={st} st={st} yOf={(d) => yOf(d, st)} ink={BK.ink}/>)}
      {['treble', 'bass'].map(st => sig.map((a, j) => { const pos = (ks[0] === 'sharp' ? SHARP_POS : FLAT_POS)[a], d = st === 'bass' ? 16 + pos : 30 + pos, x = 46 + j * 10, y = yOf(d, st);
        return ks[0] === 'sharp' ? <SharpShape key={st + a} x={x} y={y} color={BK.ink}/> : <FlatShape key={st + a} x={x} y={y} color={BK.ink}/>; }))}
      {chords.map((c, i) => { const x = xOf(i); return <g key={i}>{c.S && voice('S', c.S, x, 'treble', i)}{c.A && voice('A', c.A, x, 'treble', i)}{c.T && voice('T', c.T, x, 'bass', i)}{c.B && voice('B', c.B, x, 'bass', i)}
        {labels && labels[i] && <text x={x} y={yBot - 8} textAnchor="middle" fontSize="15" fontWeight="900" fill={BK.ink} fontFamily="Inter, sans-serif">{labels[i]}</text>}</g>; })}
      <line x1={width - 4} x2={width - 4} y1={yT(38)} y2={yB(18)} stroke={BK.ink} strokeWidth="1.4"/>
    </svg>
  );
}
const h3Btn = spBtn, h3Msg = spMsg;
const h3Choice = (opts, ans, picked, onPick, cols = opts.length) => <div style={{display:'grid',gridTemplateColumns:'repeat(' + cols + ',minmax(0,1fr))',gap:8,marginTop:10}}>{opts.map(([id, lab]) => <button key={id} className={'choice-btn' + (picked == null ? '' : id === ans ? ' good' : id === picked ? ' bad' : '')} onClick={() => onPick(id)} style={{padding:'11px 4px',fontSize:14.5,fontWeight:900}}>{lab}</button>)}</div>;

// ── step 1: above the tonic, in a minor key ──
function H3IvPad({ fixed, onResult }) {
  const [k, setK] = useState(fixed ? fixed.k : 'Am'), [clef, setClef] = useState(fixed ? fixed.clef : 'treble'), [n, setN] = useState(fixed ? fixed.n : 3), [quiz, setQuiz] = useState(!!fixed), [pick, setPick] = useState(null), [opts, setOpts] = useState(null);
  const [t0, nt] = h3Above(k, clef, n), q = H3_QMIN[n], name = h3IvName(q, n);
  const ask = () => { const m = 2 + Math.floor(Math.random() * 7); setN(m); setQuiz(true); setPick(null); setOpts(shuffle(H3_DIST[m].slice())); h3Play([[...h3Above(k, clef, m)]]); };
  useEffect(() => { if (fixed) setOpts(shuffle(H3_DIST[fixed.n].slice())); }, []);
  const say = (id) => { if (pick != null) return; setPick(id); if (onResult) onResult({ ok: id === q + n }); };
  return (
    <div className="try-box" style={actBox} data-h3="iv">
      <div style={actTitle}>{t('Above the tonic, in a minor key', '단조에서 으뜸음 위의 음정')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>화성 단음계의 음을 으뜸음과 함께 쌓아요. <b>3도와 6도는 단음정</b>, 7도는 올린 이끎음이라 <b>장7도</b>, 4도·5도·8도는 <b>완전음정</b>.</>
        : <>Each note of the harmonic minor, above the tonic. <b>The 3rd and 6th are minor</b>; the 7th is the raised leading note, so <b>a major 7th</b>; the 4th, 5th and octave are <b>perfect</b>.</>}</div>
      {!fixed && spChips(H3_MIN_KEYS.map(x => [x, t(H3_MIN[x].en, H3_MIN[x].ko)]), k, (x) => { setK(x); setPick(null); setQuiz(false); })}
      {!fixed && spChips([['treble', t('Treble clef', '높은음자리표')], ['bass', t('Bass clef', '낮은음자리표')]], clef, (x) => { setClef(x); setPick(null); setQuiz(false); })}
      <IntervalStaff clef={clef} notes={[t0, nt]} colors={[BK.ink, pick == null && quiz ? BK.ink : BK.coral]} labels={[h3Let(t0), quiz && pick == null ? '?' : h3Let(nt)]} width={220}/>
      {!quiz && spChips([2, 3, 4, 5, 6, 7, 8].map(m => [m, H3_ORD[m] === 'octave' ? t('8ve', '8도') : t(H3_ORD[m], H3_ORDK[m])]), n, (m) => { setN(m); h3Play([[...h3Above(k, clef, m)]]); })}
      {quiz ? (opts && h3Choice(opts.map(([qq, nn]) => [qq + nn, h3IvName(qq, nn)]), q + n, pick, say, 1)) : null}
      {h3Msg(!quiz ? t(name + (H3_QMIN[n] !== H3_QMAJ[n] ? ' (in the major key: ' + h3IvName(H3_QMAJ[n], n) + ')' : ''), name + (H3_QMIN[n] !== H3_QMAJ[n] ? ' (장조라면 ' + h3IvName(H3_QMAJ[n], n) + ')' : ''))
        : pick == null ? t('Count the lines and spaces, then think: is it the minor key\'s 3rd or 6th?', '선과 칸을 세고, 단조의 3도나 6도인지 생각해요.') : pick === q + n ? t('Yes: ' + name + '.', '맞아요: ' + name + '.') : t('It is a ' + name + ': ' + h3Let(t0) + ' to ' + h3Let(nt) + '.', name + '예요: ' + h3Let(t0) + '에서 ' + h3Let(nt) + '.'), quiz && pick != null ? (pick === q + n ? BK.green : BK.coral) : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={h3Btn} onClick={() => h3Play([[t0, nt]])}>{t('▶ Hear it', '▶ 들어 보기')}</button>
        {!fixed && <button className="ghost-btn" style={h3Btn} onClick={ask}>{quiz && pick != null ? t('▶ Another', '▶ 다른 것') : t('▶ Your turn', '▶ 내가 해보기')}</button>}
      </div>
    </div>
  );
}

// ── step 2: the degree names ──
function H3DegPad({ fixed, onResult }) {
  const [sel, setSel] = useState(fixed != null ? fixed : 0), [quiz, setQuiz] = useState(fixed != null), [pick, setPick] = useState(null), [opts, setOpts] = useState(() => fixed != null ? h3DegOpts(fixed) : null);
  const K = [0, 2, 4, 5, 7, 9, 11, 12], N = ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C'];
  const ask = () => { let m, g = 0; do { m = Math.floor(Math.random() * 7); } while (m === sel && g++ < 8); setSel(m); setQuiz(true); setPick(null); setOpts(h3DegOpts(m)); playKey(K[m], 0.7); };
  const say = (id) => { if (pick != null) return; setPick(id); if (onResult) onResult({ ok: id === sel }); };
  const lit = {}; K.forEach((x, j) => { lit[x] = j === sel || (sel === 0 && j === 7) ? 'cor' : 'pale'; });
  return (
    <div className="try-box" style={actBox} data-h3="deg">
      <div style={actTitle}>{t('The degree names', '음계 음의 이름')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>음계의 음마다 이름이 있어요. <b>딸림음</b>은 으뜸음 5도 위, <b>버금딸림음</b>은 5도 아래(그래서 '버금'). <b>가온음</b>은 으뜸음과 딸림음의 가운데, <b>이끎음</b>은 으뜸음으로 이끄는 반음 아래 음.</>
        : <>Every note of the scale has a name. <b>The dominant</b> is a 5th above the tonic, <b>the subdominant</b> a 5th below it ("sub" = under). <b>The mediant</b> is halfway from tonic to dominant; <b>the leading note</b> leads up to the tonic, a semitone below it.</>}</div>
      <div style={{display:'grid',gridTemplateColumns:'repeat(7,minmax(0,1fr))',gap:4,margin:'4px 0 8px'}}>{H3_DEGN.map((nm, j) => <button key={j} className={'chip' + (j === sel ? ' active' : '')} onClick={() => { if (quiz && pick == null) return; setSel(j); setQuiz(false); setPick(null); playKey(K[j], 0.6); }} style={{minHeight:44,padding:'2px 0',display:'flex',flexDirection:'column',alignItems:'center',justifyContent:'center',fontWeight:900,fontSize:15}}>{j + 1}</button>)}</div>
      <SpKb lo={0} hi={12} W={30} H={80} lit={lit} names={Object.fromEntries(K.map((x, j) => [x, N[j]]))}/>
      {quiz ? (opts && h3Choice(opts.map(j => [j, h3DegName(j)]), sel, pick, say, 2)) : <div style={{textAlign:'center',fontSize:20,fontWeight:900,color:BK.coral,margin:'8px 0 2px'}}>{(sel + 1) + ' · ' + h3DegName(sel)}</div>}
      {h3Msg(quiz ? (pick == null ? t('Note ' + (sel + 1) + ' of the scale: its name?', '음계의 ' + (sel + 1) + '번째 음: 이름은?') : pick === sel ? t('Yes: the ' + H3_DEGN[sel][0] + '.', '맞아요: ' + H3_DEGN[sel][1] + '.') : t('Note ' + (sel + 1) + ' is the ' + H3_DEGN[sel][0] + '.', (sel + 1) + '번째 음은 ' + H3_DEGN[sel][1] + '이에요.')) : t('Tap a number to hear and name it.', '숫자를 누르면 듣고 이름을 봐요.'), quiz && pick != null ? (pick === sel ? BK.green : BK.coral) : undefined)}
      {fixed == null && <div style={{textAlign:'center',marginTop:8}}><button className="ghost-btn" style={h3Btn} onClick={ask}>{quiz && pick != null ? t('▶ Another', '▶ 다른 것') : t('▶ Your turn', '▶ 내가 해보기')}</button></div>}
    </div>
  );
}
const h3DegOpts = (m) => { const o = [m]; while (o.length < 4) { const x = Math.floor(Math.random() * 7); if (!o.includes(x)) o.push(x); } return shuffle(o); };

// ── step 3: root position and first inversion ──
function H3InvPad({ fixed, onResult }) {
  const [k, setK] = useState(fixed ? fixed.k : 'C'), [deg, setDeg] = useState(fixed ? fixed.deg : 1), [inv, setInv] = useState(fixed ? fixed.inv : 0), [clef, setClef] = useState(fixed ? fixed.clef : 'treble'), [quiz, setQuiz] = useState(!!fixed), [pick, setPick] = useState(null);
  const ns = h3Triad(k, deg, clef, inv), rom = h3Rom(k, deg) + (inv ? 'b' : '');
  const ask2 = () => { const kk = H3_TRI_KEYS[Math.floor(Math.random() * H3_TRI_KEYS.length)], dd = [1, 4, 5][Math.floor(Math.random() * 3)], ii = Math.random() < 0.5 ? 0 : 1; setK(kk); setDeg(dd); setInv(ii); setQuiz(true); setPick(null); h3Play([h3Triad(kk, dd, clef, ii)]); };
  const say = (id) => { if (pick != null) return; setPick(id); if (onResult) onResult({ ok: id === inv }); };
  const posW = (i) => (i ? t('first inversion', '제1전위') : t('root position', '기본 위치'));
  return (
    <div className="try-box" style={actBox} data-h3="inv">
      <div style={actTitle}>{t('Root position and first inversion', '기본 위치와 제1전위')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>주요 3화음 <b>I, IV, V</b>를 가깝게(밀집 위치) 쌓아요. <b>기본 위치</b>는 근음이 맨 아래. 근음을 한 옥타브 올리면 <b>3음이 맨 아래</b>: <b>제1전위</b>예요. 단조의 V는 이끎음을 올려 장3화음.</>
        : <>The primary triads <b>I, IV and V</b>, in close position. In <b>root position</b> the root is at the bottom. Move the root up an octave and <b>the 3rd is at the bottom</b>: <b>first inversion</b>. In a minor key V takes the raised leading note.</>}</div>
      {!fixed && spChips(H3_TRI_KEYS.map(x => [x, t(H3_TRI[x].en, H3_TRI[x].ko)]), k, (x) => { setK(x); setQuiz(false); setPick(null); })}
      {!fixed && spChips([1, 4, 5].map(d => [d, h3Rom(k, d)]), deg, (d) => { setDeg(d); setQuiz(false); setPick(null); })}
      {!fixed && spChips([[0, t('Root position', '기본 위치')], [1, t('First inversion', '제1전위')], ['c', clef === 'treble' ? t('→ Bass clef', '→ 낮은음자리표') : t('→ Treble clef', '→ 높은음자리표')]], inv, (x) => { if (x === 'c') setClef(clef === 'treble' ? 'bass' : 'treble'); else setInv(x); setQuiz(false); setPick(null); })}
      <ChordStaff clef={clef} chords={[{ notes: ns, label: quiz && pick == null ? '?' : rom, color: quiz && pick == null ? BK.ink : BK.coral }]} width={200}/>
      {quiz && h3Choice([[0, posW(0)], [1, posW(1)]], inv, pick, say, 2)}
      {h3Msg(quiz ? (pick == null ? t('Which note is at the bottom: the root or the 3rd?', '맨 아래 음은 근음일까요, 3음일까요?') : pick === inv ? t('Yes: ' + rom + ', ' + posW(inv) + '.', '맞아요: ' + rom + ', ' + posW(inv) + '.') : t('The ' + (inv ? '3rd' : 'root') + ', ' + h3Let(ns[0]) + ', is at the bottom: ' + posW(inv) + '.', '맨 아래가 ' + (inv ? '3음' : '근음') + ' ' + h3Let(ns[0]) + ': ' + posW(inv) + '.'))
        : t(rom + ' in ' + H3_TRI[k].en + ': ' + ns.map(h3Let).join(' ') + (inv ? ' (the 3rd at the bottom)' : ' (the root at the bottom)'), H3_TRI[k].ko + '의 ' + rom + ': ' + ns.map(h3Let).join(' ') + (inv ? ' (3음이 맨 아래)' : ' (근음이 맨 아래)')), quiz && pick != null ? (pick === inv ? BK.green : BK.coral) : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={h3Btn} onClick={() => h3Play([ns])}>{t('▶ Hear it', '▶ 들어 보기')}</button>
        {!fixed && <button className="ghost-btn" style={h3Btn} onClick={ask2}>{quiz && pick != null ? t('▶ Another', '▶ 다른 것') : t('▶ Your turn', '▶ 내가 해보기')}</button>}
      </div>
    </div>
  );
}

// ── step 4: four voices ──
function H3SatbPad({ fixed, onResult }) {
  const ch = h3CadChords('C', 'perfect')[1];
  const [v, setV] = useState(fixed ? fixed.v : 'S'), [quiz, setQuiz] = useState(!!fixed), [pick, setPick] = useState(null), [cc, setCc] = useState(fixed ? h3CadChords(fixed.k, fixed.id)[fixed.i] : ch);
  const ask = () => { const kk = H3_CAD_KEYS[Math.floor(Math.random() * H3_CAD_KEYS.length)], id = Math.random() < 0.5 ? 'perfect' : 'plagal', i = Math.floor(Math.random() * 2), vv = 'SATB'[Math.floor(Math.random() * 4)];
    setCc(h3CadChords(kk, id)[i]); setV(vv); setQuiz(true); setPick(null); };
  const say = (id) => { if (pick != null) return; setPick(id); if (onResult) onResult({ ok: id === v }); };
  const r = H3_RANGE[v];
  return (
    <div className="try-box" style={actBox} data-h3="satb">
      <div style={actTitle}>{t('Soprano, alto, tenor, bass', '소프라노, 알토, 테너, 베이스')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>네 성부로 쓸 때: <b>소프라노와 알토</b>는 높은음자리표(소프라노 기둥은 위, 알토는 아래), <b>테너와 베이스</b>는 낮은음자리표(테너 기둥은 위, 베이스는 아래). 성부마다 부르기 좋은 음역이 있어요.</>
        : <>Written in four parts: <b>soprano and alto</b> share the treble staff (soprano's stems up, alto's down); <b>tenor and bass</b> share the bass staff (tenor's stems up, bass's down). Each voice has its own comfortable range.</>}</div>
      {!quiz && spChips('SATB'.split('').map(x => [x, h3Voice(x)]), v, (x) => setV(x))}
      <SatbStaff chords={[cc]} hi={{ i: 0, v }} bands={quiz ? null : [v]} width={220}/>
      {quiz && h3Choice('SATB'.split('').map(x => [x, h3Voice(x)]), v, pick, say, 2)}
      {h3Msg(quiz ? (pick == null ? t('Which voice sings the coral note? Look at the staff and the stem.', '빨간 음은 어느 성부일까요? 오선과 기둥을 봐요.') : pick === v ? t('Yes: the ' + H3_VOICE[v][0] + '.', '맞아요: ' + H3_VOICE[v][1] + '.') : t('The ' + H3_VOICE[v][0] + ': ' + (v === 'S' || v === 'A' ? 'treble' : 'bass') + ' staff, stem ' + (v === 'S' || v === 'T' ? 'up' : 'down') + '.', H3_VOICE[v][1] + '예요: ' + (v === 'S' || v === 'A' ? '높은음자리표' : '낮은음자리표') + ', 기둥 ' + (v === 'S' || v === 'T' ? '위' : '아래') + '.'))
        : t(h3Voice(v) + ': about ' + r[0] + ' to ' + r[1] + '.', h3Voice(v) + ': 대략 ' + r[0] + '부터 ' + r[1] + '까지.'), quiz && pick != null ? (pick === v ? BK.green : BK.coral) : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={h3Btn} onClick={() => h3Play([[cc.S, cc.A, cc.T, cc.B]])}>{t('▶ Hear it', '▶ 들어 보기')}</button>
        {!fixed && <button className="ghost-btn" style={h3Btn} onClick={ask}>{quiz && pick != null ? t('▶ Another', '▶ 다른 것') : t('▶ Your turn', '▶ 내가 해보기')}</button>}
      </div>
    </div>
  );
}

// ── step 5: the perfect and plagal cadences ──
function H3CadPad({ fixed, onResult }) {
  const [k, setK] = useState(fixed ? fixed.k : 'C'), [id, setId] = useState(fixed ? fixed.id : 'perfect'), [quiz, setQuiz] = useState(!!fixed), [pick, setPick] = useState(null);
  const cs = h3CadChords(k, id), rom = h3CadRom(k, id);
  const play = () => h3Play(cs.map(c => [c.S, c.A, c.T, c.B]), 60, 2);
  const ask = () => { const kk = H3_CAD_KEYS[Math.floor(Math.random() * H3_CAD_KEYS.length)], ii = Math.random() < 0.5 ? 'perfect' : 'plagal'; setK(kk); setId(ii); setQuiz(true); setPick(null); h3Play(h3CadChords(kk, ii).map(c => [c.S, c.A, c.T, c.B]), 60, 2); };
  const say = (x) => { if (pick != null) return; setPick(x); if (onResult) onResult({ ok: x === id }); };
  return (
    <div className="try-box" style={actBox} data-h3="cad">
      <div style={actTitle}>{t('Perfect and plagal cadences', '정격종지와 변격종지')}</div>
      <div style={actNote}>{LANG === 'ko' ? <><b>정격종지</b>는 V에서 I: 마침표처럼 끝나요. <b>변격종지</b>는 IV에서 I: "아멘". 네 성부로 쓸 때: 베이스는 근음, 이끎음은 으뜸음으로 올라가고, 두 화음에 같은 음은 같은 성부에 그대로 둬요.</>
        : <><b>Perfect</b>: V to I, a full stop. <b>Plagal</b>: IV to I, the "Amen". In four parts: the bass takes the roots, the leading note rises to the tonic, and a note the two chords share stays in the same voice.</>}</div>
      {!fixed && spChips(H3_CAD_KEYS.map(x => [x, h3KeyOfCad(x)]), k, (x) => { setK(x); setQuiz(false); setPick(null); })}
      {!fixed && spChips([['perfect', t('Perfect', '정격')], ['plagal', t('Plagal', '변격')]], id, (x) => { setId(x); setQuiz(false); setPick(null); })}
      <SatbStaff chords={cs} ks={H3_CAD[k].ks} labels={quiz && pick == null ? ['?', '?'] : rom} width={250}/>
      {quiz && h3Choice([['perfect', h3CadName('perfect')], ['plagal', h3CadName('plagal')]], id, pick, say, 2)}
      {h3Msg(quiz ? (pick == null ? t('Listen and look at the bass: from the dominant or the subdominant?', '듣고 베이스를 봐요: 딸림음에서? 버금딸림음에서?') : pick === id ? t('Yes: ' + rom.join('–') + ', a ' + (id === 'perfect' ? 'perfect' : 'plagal') + ' cadence.', '맞아요: ' + rom.join('–') + ', ' + h3CadName(id) + '.') : t('It was ' + rom.join('–') + ': a ' + (id === 'perfect' ? 'perfect' : 'plagal') + ' cadence.', rom.join('–') + '였어요: ' + h3CadName(id) + '.'))
        : t(h3KeyOfCad(k) + ': ' + rom.join('–') + ', a ' + (id === 'perfect' ? 'perfect' : 'plagal') + ' cadence.', h3KeyOfCad(k) + ': ' + rom.join('–') + ', ' + h3CadName(id) + '.'), quiz && pick != null ? (pick === id ? BK.green : BK.coral) : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={h3Btn} onClick={play}>{t('▶ Hear it', '▶ 들어 보기')}</button>
        {!fixed && <button className="ghost-btn" style={h3Btn} onClick={ask}>{quiz && pick != null ? t('▶ Another', '▶ 다른 것') : t('▶ Your turn', '▶ 내가 해보기')}</button>}
      </div>
    </div>
  );
}

// ── the pictures on paper ──
const h3PicIv = () => lsRawPic('<ellipse cx="22" cy="32" rx="6" ry="4.4" transform="rotate(-20 22 32)" fill="#26296b"/><ellipse cx="40" cy="22" rx="6" ry="4.4" transform="rotate(-20 40 22)" fill="#e4572e"/><text x="58" y="27" font-family="Inter, sans-serif" font-size="12" font-weight="900" fill="#e4572e">m3</text>', [0, 0, 80, 44]);
const h3PicDeg = () => lsRawPic([1, 2, 3, 4, 5].map((n, i) => lsCircleSvg(8 + i * 15, 36 - i * 6, 6, n === 1 || n === 5 ? 'play' : 'beat', String(n))).join(''), [0, 0, 80, 44]);
const h3PicInv = () => lsRawPic('<ellipse cx="30" cy="34" rx="6" ry="4.4" transform="rotate(-20 30 34)" fill="#e4572e"/><ellipse cx="30" cy="24" rx="6" ry="4.4" transform="rotate(-20 30 24)" fill="#26296b"/><ellipse cx="30" cy="14" rx="6" ry="4.4" transform="rotate(-20 30 14)" fill="#26296b"/><text x="46" y="38" font-family="Inter, sans-serif" font-size="11" font-weight="900" fill="#e4572e">3rd</text>', [0, 0, 80, 44]);
const h3PicSatb = () => lsRawPic('<line x1="10" x2="70" y1="10" y2="10" stroke="#26296b" stroke-width="1.4"/><line x1="10" x2="70" y1="18" y2="18" stroke="#26296b" stroke-width="1.4"/><line x1="10" x2="70" y1="28" y2="28" stroke="#26296b" stroke-width="1.4"/><line x1="10" x2="70" y1="36" y2="36" stroke="#26296b" stroke-width="1.4"/>' + ['S', 'A', 'T', 'B'].map((x, i) => '<text x="' + (16 + i * 15) + '" y="' + (i < 2 ? 16 : 34) + '" font-family="Inter, sans-serif" font-size="10" font-weight="900" fill="' + (i === 0 ? '#e4572e' : '#26296b') + '">' + x + '</text>').join(''), [0, 0, 80, 44]);
const h3PicCad = () => lsRawPic('<text x="6" y="30" font-family="Inter, sans-serif" font-size="16" font-weight="900" fill="#26296b">V</text><path d="M24 25 L44 25 M39 20 L44 25 L39 30" fill="none" stroke="#e4572e" stroke-width="2"/><text x="50" y="30" font-family="Inter, sans-serif" font-size="16" font-weight="900" fill="#26296b">I</text>', [0, 0, 70, 44]);

function h3LbPages(scr = false) {
  const ch = 'harmony-23', iv = bkChapterNo('intervals'), cd = bkChapterNo('chords');
  const pen = (x) => <PenArt shapes={x.shapes} vb={x.vb} style={{width:90}}/>;
  const checks5 = [[h3PicIv(), t('I name the intervals above the tonic in a minor key, number and quality', '단조에서 으뜸음 위의 음정을 숫자와 성질로 말해요')], [h3PicDeg(), t('I name the degrees: tonic, supertonic, mediant, subdominant, dominant, submediant, leading note', '음계 음의 이름을 말해요: 으뜸음, 윗으뜸음, 가온음, 버금딸림음, 딸림음, 버금가온음, 이끎음')],
    [h3PicInv(), t('I write I, IV and V in root position and first inversion', 'I, IV, V를 기본 위치와 제1전위로 써요')], [h3PicSatb(), t('I know where soprano, alto, tenor and bass sit, and their stems', '소프라노, 알토, 테너, 베이스의 자리와 기둥 방향을 알아요')], [h3PicCad(), t('I write and recognise the perfect and plagal cadences in four parts', '정격종지와 변격종지를 네 성부로 쓰고 알아봐요')]];
  const toc = [[t('Above the tonic, in a minor key', '단조에서 으뜸음 위의 음정'), 2], [t('The degree names', '음계 음의 이름'), 3], [t('Root position and first inversion', '기본 위치와 제1전위'), 4], [t('Soprano, alto, tenor, bass', '소프라노, 알토, 테너, 베이스'), 5], [t('Perfect and plagal cadences', '정격종지와 변격종지'), 6], [t('My five checks', '나의 다섯 가지 확인'), 7]];
  const W = scr ? 230 : 320;
  const ivStill = (k, clef) => <div><div style={{textAlign:'center',fontSize:13,fontWeight:900,color:BK.ink,marginBottom:2}}>{t(H3_MIN[k].en, H3_MIN[k].ko)}</div><div style={{display:'flex',gap:6,justifyContent:'center',flexWrap:'wrap'}}>{[3, 6, 7].map(n => { const [a, b] = h3Above(k, clef, n); return <div key={n} style={{width:scr ? 96 : 130}}><IntervalStaff clef={clef} notes={[a, b]} colors={[BK.ink, BK.coral]} labels={[null, h3IvName(H3_QMIN[n], n)]} width={150}/></div>; })}</div></div>;
  return [
    <LbPage key="1" no={1} chId={ch} teacher={<>{t('Theory of Music, Grades 2 and 3: intervals above the tonic, number and quality, in the grade\'s keys (Grade 2 treble clef; Grade 3 treble or bass); the technical names of the degrees (Grade 3); the three primary triads in close position, root position and first inversion, treble or bass (Grade 3); the approximate compass of soprano, alto, tenor and bass (Grade 3); the perfect and plagal cadences in four-part vocal style (Grade 3). Chapters ' + iv + ' and ' + cd + ' have the groundwork.', 'Theory of Music 2·3급: 급의 조에서 으뜸음 위의 음정을 숫자와 성질로(2급 높은음자리표, 3급 높은음·낮은음자리표); 음계 음의 이름(3급); 주요 3화음을 밀집 위치로, 기본 위치와 제1전위, 높은음·낮은음자리표(3급); 소프라노, 알토, 테너, 베이스의 대략적인 음역(3급); 정격종지와 변격종지를 네 성부 성악 양식으로(3급). 기초는 ' + iv + '장과 ' + cd + '장에 있어요.')}</>}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:46,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{t('Intervals and Chords Further', '음정과 화음 한 걸음 더')}</div>
      </div></LbOnly>
      <LbPic h={170}><div style={{width:'100%',maxWidth:scr ? 300 : 420,margin:'0 auto'}}><SatbStaff chords={h3CadChords('C', 'perfect')} labels={['V', 'I']} width={W}/></div></LbPic>
      <LbSay size={18}>{t('Theory for Grades 2 and 3: intervals in minor keys, the names of the degrees, chords turned over, four voices, and the two cadences that end a piece.', '2·3급 이론: 단조의 음정, 음계 음의 이름, 자리를 바꾼 화음, 네 성부, 그리고 곡을 끝내는 두 종지.')}</LbSay>
      <div className="lb-toc" style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>
        <LbOnly print><div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('In this chapter', '이 챕터에서는')}</div>
          {toc.map(([n, p]) => <div key={p} className="lb-toc-row" style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:14.5,padding:'5px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkGoal(15)}{n}</span><span style={{color:BK.muted,fontWeight:700}}>{p}</span></div>)}
        </div></LbOnly>
        <div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 챕터를 마치면')}</div>
          {[t('name any interval above the tonic, major or minor key', '장조든 단조든 으뜸음 위의 음정을 말할 수 있어요'), t('name every degree of the scale', '음계의 모든 음의 이름을 말할 수 있어요'), t('write I, IV and V in root position and first inversion', 'I, IV, V를 기본 위치와 제1전위로 쓸 수 있어요'), t('write a perfect and a plagal cadence in four parts', '정격종지와 변격종지를 네 성부로 쓸 수 있어요')].map((x, i) => <div key={i} style={{display:'flex',alignItems:'flex-start',gap:9,fontSize:14.5,padding:'5px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}>{bkGoal(15)}<span>{x}</span></div>)}
        </div>
      </div>
      <LbOnly print><LbDrillStrip id={ch}/></LbOnly>
    </LbPage>,
    <LbPage key="2" no={2} chId={ch} kicker={t('Step 1', '1단계')} title={t('Above the tonic, in a minor key', '단조에서 으뜸음 위의 음정')}
      teacher={<>{t('Grade 2: all the diatonic intervals above the tonic in the grade\'s keys (C, G, F, D, A major; A, E, D minor, harmonic form), treble clef, number and quality. Grade 3 adds E, B♭, E♭, A♭ major and G, C minor, in the treble or bass clef. In the harmonic minor the 3rd and 6th are minor and the 7th, the raised leading note, is major. Chapter ' + iv + ' has the major keys.', '2급: 급의 조(C, G, F, D, A장조; A, E, D단조 화성형)에서 으뜸음 위의 모든 온음계 음정을 높은음자리표로, 숫자와 성질까지. 3급은 E, B♭, E♭, A♭장조와 G, C단조를 더하고, 높은음자리표나 낮은음자리표로. 화성 단음계에서는 3도와 6도가 단음정, 올린 이끎음인 7도는 장음정. 장조는 ' + iv + '장에 있어요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=1')}>
      <LbLive still={<LbPic h={170}><div style={{display:'flex',flexDirection:'column',gap:10,width:'100%',maxWidth:560,margin:'0 auto'}}>{ivStill('Am', 'treble')}{ivStill('Dm', 'bass')}</div></LbPic>} live={<H3IvPad/>}/>
      <LbSay>{LANG === 'ko' ? <>단조에서는 <b>3도와 6도가 단음정</b>이 돼요. 7도는 올린 이끎음이라 <b>장7도</b> 그대로. 4도, 5도, 8도는 언제나 <b>완전음정</b>.</> : <>In a minor key <b>the 3rd and the 6th are minor</b>. The 7th is the raised leading note, so it stays <b>a major 7th</b>. The 4th, 5th and octave are always <b>perfect</b>.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>A와 C를 함께 쳐요: 단3도. 그다음 A와 C♯: 장3도. 소리를 비교해요.</>, <>A단조 음계의 음을 하나씩 A와 함께 치고 이름을 말해요.</>, <>낮은음자리표로 쓴 음정도 똑같이 세어요: 선과 칸.</>]
        : [<>Play A and C together: a minor 3rd. Then A and C♯: a major 3rd. Compare the sound.</>, <>Play each note of A minor with A and name it.</>, <>Intervals in the bass clef count the same way: lines and spaces.</>]}/>
      <LbRemember>{t('Minor key: the 3rd and 6th go minor.', '단조: 3도와 6도가 단음정.')}</LbRemember>
    </LbPage>,
    <LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={t('The degree names', '음계 음의 이름')}
      teacher={<>{t('Grade 3: the technical names of the degrees of the scale. The dominant is a 5th above the tonic and the subdominant a 5th below it; the mediant is halfway from tonic up to dominant, the submediant halfway from tonic down to subdominant; the supertonic is just above the tonic, the leading note a semitone below it.', '3급: 음계 음의 이름. 딸림음은 으뜸음의 5도 위, 버금딸림음은 5도 아래; 가온음은 으뜸음에서 딸림음까지의 가운데, 버금가온음은 으뜸음에서 버금딸림음까지의 가운데; 윗으뜸음은 으뜸음 바로 위, 이끎음은 반음 아래.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=3')}>
      <LbLive still={<LbPic h={160}><div style={{display:'grid',gridTemplateColumns:scr ? '1fr 1fr' : 'repeat(4,minmax(0,1fr))',gap:8,width:'100%',maxWidth:620,margin:'0 auto'}}>{H3_DEGN.map((nm, j) => <div key={j} style={{border:'1.5px solid ' + (j === 0 || j === 4 ? BK.coral : BK.ink),borderRadius:10,padding:'6px 4px',textAlign:'center'}}><div style={{fontSize:20,fontWeight:900,color:j === 0 || j === 4 ? BK.coral : BK.ink}}>{j + 1}</div><div style={{fontSize:13,fontWeight:800,color:BK.ink}}>{t(nm[0], nm[1])}</div></div>)}</div></LbPic>} live={<H3DegPad/>}/>
      <LbSay>{LANG === 'ko' ? <>1 <b>으뜸음</b>, 2 <b>윗으뜸음</b>, 3 <b>가온음</b>, 4 <b>버금딸림음</b>, 5 <b>딸림음</b>, 6 <b>버금가온음</b>, 7 <b>이끎음</b>.</> : <>1 <b>tonic</b>, 2 <b>supertonic</b>, 3 <b>mediant</b>, 4 <b>subdominant</b>, 5 <b>dominant</b>, 6 <b>submediant</b>, 7 <b>leading note</b>.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>C장조 음계를 치며 이름을 말해요.</>, <>딸림음(G)은 C의 5도 위, 버금딸림음(F)은 5도 아래: 아래의 F에서 C까지 세어 봐요.</>, <>이끎음 B에서 멈춰요: C로 가고 싶어져요.</>]
        : [<>Play C major, naming each note.</>, <>The dominant (G) is a 5th above C, the subdominant (F) a 5th below: count from the F below up to C.</>, <>Stop on the leading note, B: it wants to go on to C.</>]}/>
      <LbRemember>{t('Dominant: 5 up. Subdominant: 5 down.', '딸림음: 5도 위. 버금딸림음: 5도 아래.')}</LbRemember>
    </LbPage>,
    <LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title={t('Root position and first inversion', '기본 위치와 제1전위')}
      teacher={<>{t('Grade 3: the three primary triads (I, IV, V) in close position, root position and first inversion, in the keys of Grades 1 to 3, on the treble or bass staff. First inversion puts the 3rd in the bass (written Ib, IVb, Vb). In a minor key V is major: its 3rd is the raised leading note.', '3급: 주요 3화음(I, IV, V)을 밀집 위치로, 기본 위치와 제1전위, 1~3급의 조에서, 높은음자리표나 낮은음자리표로. 제1전위는 3음이 베이스(Ib, IVb, Vb로 써요). 단조의 V는 장3화음: 3음이 올린 이끎음이에요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=4')}>
      <LbLive still={<LbPic h={160}><div style={{width:'100%',maxWidth:scr ? 320 : 480,margin:'0 auto'}}><ChordStaff clef="treble" chords={[{ notes: h3Triad('C', 1, 'treble', 0), label: 'I' }, { notes: h3Triad('C', 1, 'treble', 1), label: 'Ib', color: BK.coral }, { notes: h3Triad('C', 5, 'treble', 0), label: 'V' }, { notes: h3Triad('C', 5, 'treble', 1), label: 'Vb', color: BK.coral }]} width={scr ? 320 : 420}/></div></LbPic>} live={<H3InvPad/>}/>
      <LbSay>{LANG === 'ko' ? <><b>기본 위치</b>: 근음이 맨 아래. 근음을 한 옥타브 올리면 <b>3음이 맨 아래</b>: <b>제1전위</b>(Ib).</> : <><b>Root position</b>: the root at the bottom. Move the root up an octave and <b>the 3rd is at the bottom</b>: <b>first inversion</b> (Ib).</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>C장조 I: C E G. 그다음 E G C.</>, <>IV와 V도: F A C → A C F, G B D → B D G.</>, <>G장조와 F장조에서도. 단조의 V는 이끎음을 올려요.</>]
        : [<>C major, I: C E G. Then E G C.</>, <>IV and V too: F A C → A C F, G B D → B D G.</>, <>In G and F major as well. In a minor key, V raises the leading note.</>]}/>
      <LbRemember>{t('First inversion: the 3rd at the bottom.', '제1전위: 3음이 맨 아래.')}</LbRemember>
    </LbPage>,
    <LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title={t('Soprano, alto, tenor, bass', '소프라노, 알토, 테너, 베이스')}
      teacher={<>{t('Grade 3 general knowledge: the approximate compass of soprano, alto, tenor and bass in normal choral writing, on the treble and bass staves. The ranges shown are the usual textbook ones (soprano C4–G5, alto G3–C5, tenor C3–G4, bass E2–C4); some books stretch each a step. In four-part vocal style the soprano and alto share the treble staff (stems up, down), the tenor and bass the bass staff.', '3급 일반 지식: 보통 합창곡에서 소프라노, 알토, 테너, 베이스의 대략적인 음역을 높은음·낮은음자리표에. 여기 음역은 흔한 교과서 음역이에요(소프라노 C4–G5, 알토 G3–C5, 테너 C3–G4, 베이스 E2–C4). 책에 따라 한 음씩 넓기도 해요. 네 성부 성악 양식에서 소프라노와 알토는 높은음자리표(기둥 위, 아래), 테너와 베이스는 낮은음자리표.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=5')}>
      <LbLive still={<LbPic h={160}><div style={{display:'grid',gridTemplateColumns:scr ? '1fr 1fr' : 'repeat(4,minmax(0,1fr))',gap:8,width:'100%',maxWidth:680,margin:'0 auto'}}>{'SATB'.split('').map(v => <div key={v}><div style={{textAlign:'center',fontSize:13,fontWeight:900,color:BK.ink}}>{h3Voice(v)}</div><SatbStaff chords={[h3CadChords('C', 'perfect')[1]]} hi={{ i: 0, v }} bands={[v]} width={150}/></div>)}</div></LbPic>} live={<H3SatbPad/>}/>
      <LbSay>{LANG === 'ko' ? <>높은음자리표에 <b>소프라노</b>(기둥 위)와 <b>알토</b>(기둥 아래), 낮은음자리표에 <b>테너</b>(기둥 위)와 <b>베이스</b>(기둥 아래).</> : <>On the treble staff, <b>soprano</b> (stems up) and <b>alto</b> (stems down); on the bass staff, <b>tenor</b> (stems up) and <b>bass</b> (stems down).</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>C장조 I을 네 성부로: 베이스 C, 테너 E, 알토 G, 소프라노 C.</>, <>한 성부씩 불러 봐요. 테너는 가운데 도 근처.</>, <>각 성부의 음역 안에 있는지 확인해요.</>]
        : [<>C major I in four parts: bass C, tenor E, alto G, soprano C.</>, <>Sing each part on its own. The tenor sits around middle C.</>, <>Check each part stays inside its range.</>]}/>
      <LbRemember>{t('Treble: soprano up, alto down. Bass: tenor up, bass down.', '높은음: 소프라노 위, 알토 아래. 낮은음: 테너 위, 베이스 아래.')}</LbRemember>
    </LbPage>,
    <LbPage key="6" no={6} chId={ch} kicker={t('Step 5', '5단계')} title={t('Perfect and plagal cadences', '정격종지와 변격종지')}
      teacher={<>{t('Grade 3: writing and recognising the perfect (V–I) and plagal (IV–I) cadences in four-part vocal style, in the grade\'s keys. A safe recipe: roots in the bass, the root doubled, the leading note rising to the tonic, a shared note kept in the same voice, the other voices moving to the nearest note; no parallel 5ths or octaves. Every example here was checked that way.', '3급: 정격종지(V–I)와 변격종지(IV–I)를 네 성부 성악 양식으로 쓰고 알아보기, 급의 조에서. 안전한 방법: 베이스는 근음, 근음을 겹치고, 이끎음은 으뜸음으로 올라가고, 두 화음에 같은 음은 같은 성부에 두고, 나머지 성부는 가장 가까운 음으로; 연속 5도와 8도는 없게. 여기 예시는 모두 그렇게 확인했어요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=6')}>
      <LbLive still={<LbPic h={170}><div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:14,width:'100%',maxWidth:scr ? 360 : 720,margin:'0 auto'}}><div><div style={{textAlign:'center',fontSize:13,fontWeight:900,color:BK.ink}}>{h3CadName('perfect')}</div><SatbStaff chords={h3CadChords('C', 'perfect')} labels={['V', 'I']} width={W}/></div><div><div style={{textAlign:'center',fontSize:13,fontWeight:900,color:BK.ink}}>{h3CadName('plagal')}</div><SatbStaff chords={h3CadChords('C', 'plagal')} labels={['IV', 'I']} width={W}/></div></div></LbPic>} live={<H3CadPad/>}/>
      <LbSay>{LANG === 'ko' ? <><b>정격종지</b>: V에서 I. <b>변격종지</b>: IV에서 I. 베이스는 근음, 이끎음은 위로, 같은 음은 그대로.</> : <><b>Perfect</b>: V to I. <b>Plagal</b>: IV to I. Roots in the bass, the leading note up, a shared note stays.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>C장조 정격종지를 쳐요: 왼손 G→C, 오른손 B D G → C E G.</>, <>변격종지: 왼손 F→C, 오른손 F A C → E G C.</>, <>어느 쪽이 "아멘"처럼 들려요?</>]
        : [<>Play the perfect cadence in C: left hand G→C, right hand B D G → C E G.</>, <>The plagal: left hand F→C, right hand F A C → E G C.</>, <>Which one sounds like "Amen"?</>]}/>
      <LbRemember>{t('V–I perfect, IV–I plagal.', 'V–I 정격, IV–I 변격.')}</LbRemember>
    </LbPage>,
    <LbPage key="7" no={7} chId={ch} kicker={t('Check-up', '점검')} title={t('My five checks', '나의 다섯 가지 확인')}
      teacher={<>{t('On paper and at the piano: write each one, then play it. The Workbook has the paper version.', '종이와 피아노로: 하나씩 쓰고, 그다음 쳐요. 종이 점검은 워크북에.')}</>}>
      <LbSay>{t('Tick each one: not yet, nearly, or got it!', '하나씩 표시해요: 아직, 거의, 됐어요!')}</LbSay>
      <LbLive still={<LbStageRows big rows={checks5.map(([a, txt]) => [pen(a), txt])}/>} live={<FiveChecks376 rows={checks5} storeKey="pb_h3_five"/>}/>
    </LbPage>,
  ];
}
function Harmony23LessonBook() { return <>{h3LbPages(false)}</>; }
function H3Learn({ onStart }) {
  const pages = h3LbPages(true), opener = pages[0];
  return (
    <Lesson id="harmony-23" title={t('Intervals and Chords Further', '음정과 화음 한 걸음 더')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="harmony-23"><div className="lb-screen lb-open" style={{display:'flex',flexDirection:'column',gap:12,margin:'0 0 8px'}}>{lbWordsFirst(opener.props.children)}</div></BkChapterCtx.Provider></LbScreenCtx.Provider>}>
      {pages.slice(1).map((pg, i) => <Step key={i} title={pg.props.title}><LbScreenPage page={pg}/></Step>)}
    </Lesson>
  );
}
// ── the drill ──
const H3_LEVELS = [
  { n: 1, label: 'Above the tonic in a minor key (treble)', kind: 'iv', clef: 'treble', time: 15 },
  { n: 2, label: 'Above the tonic in a minor key (bass)', kind: 'iv', clef: 'bass', time: 15 },
  { n: 3, label: 'The degree names', kind: 'deg', time: 12 },
  { n: 4, label: 'Root position or first inversion?', kind: 'inv', time: 12 },
  { n: 5, label: 'Which voice: soprano, alto, tenor or bass?', kind: 'voice', time: 12 },
  { n: 6, label: 'Perfect or plagal cadence?', kind: 'cad', time: 15 },
];
Object.assign(LEVEL_KO, { 'Above the tonic in a minor key (treble)': '단조에서 으뜸음 위의 음정 (높은음자리표)', 'Above the tonic in a minor key (bass)': '단조에서 으뜸음 위의 음정 (낮은음자리표)', 'The degree names': '음계 음의 이름', 'Root position or first inversion?': '기본 위치일까, 제1전위일까?', 'Which voice: soprano, alto, tenor or bass?': '어느 성부: 소프라노, 알토, 테너, 베이스?', 'Perfect or plagal cadence?': '정격종지일까, 변격종지일까?' });
function genH3Question(lv, prev) {
  const uid = Math.random(), kind = lv.kind, R = (a) => a[Math.floor(Math.random() * a.length)];
  if (kind === 'iv') { let k, n, g = 0; do { k = R(lv.clef === 'bass' ? ['Gm', 'Cm', 'Am', 'Dm'] : H3_MIN_KEYS); n = 2 + Math.floor(Math.random() * 7); } while (prev && prev.key === k + n && g++ < 10);
    return { kind, clef: lv.clef, k, n, answer: H3_QMIN[n] + n, choices: shuffle(H3_DIST[n].map(([q, m]) => q + m)), key: k + n, uid }; }
  if (kind === 'deg') { let i, g = 0; do { i = Math.floor(Math.random() * 7); } while (prev && prev.key === 'd' + i && g++ < 10); return { kind, i, answer: i, choices: h3DegOpts(i), key: 'd' + i, uid }; }
  if (kind === 'inv') { let k, dg, inv, clef, g = 0; do { k = R(H3_TRI_KEYS); dg = R([1, 4, 5]); inv = Math.random() < 0.5 ? 0 : 1; clef = Math.random() < 0.5 ? 'treble' : 'bass'; } while (prev && prev.key === k + dg + inv + clef && g++ < 10);
    return { kind, k, dg, inv, clef, answer: inv, choices: [0, 1], key: k + dg + inv + clef, uid }; }
  if (kind === 'voice') { let k, id, i, v, g = 0; do { k = R(H3_CAD_KEYS); id = R(['perfect', 'plagal']); i = R([0, 1]); v = R(['S', 'A', 'T', 'B']); } while (prev && prev.key === k + id + i + v && g++ < 10);
    return { kind, k, id, i, v, answer: v, choices: ['S', 'A', 'T', 'B'], key: k + id + i + v, uid }; }
  let k, id, g = 0; do { k = R(H3_CAD_KEYS); id = R(['perfect', 'plagal']); } while (prev && prev.key === 'c' + k + id && g++ < 10);
  return { kind: 'cad', k, id, answer: id, choices: ['perfect', 'plagal'], key: 'c' + k + id, uid };
}
function h3AnswerLabel(q) {
  if (q.kind === 'iv') return h3IvName(q.answer[0], Number(q.answer.slice(1)));
  if (q.kind === 'deg') return h3DegName(q.answer);
  if (q.kind === 'inv') return q.answer ? t('first inversion', '제1전위') : t('root position', '기본 위치');
  if (q.kind === 'voice') return h3Voice(q.answer);
  return h3CadName(q.answer);
}
function H3Question({ q, given, locked, onAnswer, pixel }) {
  const done = !!given;
  const btnCls = pixel ? 'pixel-choice' : 'choice-btn', cls = (c) => btnCls + (!done ? '' : c === q.answer ? ' good' : given.ans === c ? ' bad' : '');
  const pickIt = (c) => { if (locked || done) return; onAnswer(c); };
  const grid = (cols, items) => <div style={{display:'grid',gridTemplateColumns:'repeat(' + cols + ',minmax(0,1fr))',gap:8,marginTop:10}}>{items.map(([c, lab]) => <button key={String(c)} disabled={locked} className={cls(c)} style={{padding:'12px 4px',fontSize:15,fontWeight:900}} onClick={() => pickIt(c)}>{lab}</button>)}</div>;
  let title, body, sound = null;
  if (q.kind === 'iv') { const [a, b] = h3Above(q.k, q.clef, q.n); sound = () => h3Play([[a, b]]);
    title = t(H3_MIN[q.k].en + ', above the tonic: name the interval.', H3_MIN[q.k].ko + ', 으뜸음 위: 음정의 이름은?');
    body = <><div style={{maxWidth:260,margin:'0 auto'}}><IntervalStaff clef={q.clef} notes={[a, b]} colors={[BK.ink, done ? BK.coral : BK.ink]} labels={[h3Let(a), done ? h3Let(b) : '']} width={200}/></div>{grid(1, q.choices.map(c => [c, h3IvName(c[0], Number(c.slice(1)))]))}</>; }
  else if (q.kind === 'deg') { const K = [0, 2, 4, 5, 7, 9, 11, 12], lit = {}; K.forEach((x, j) => { lit[x] = j === q.i ? 'cor' : 'pale'; }); sound = () => playKey(K[q.i], 0.8);
    title = t('C major: what is the name of note ' + (q.i + 1) + '?', 'C장조: ' + (q.i + 1) + '번째 음의 이름은?');
    body = <><SpKb lo={0} hi={12} W={28} H={76} lit={lit} names={{ [K[q.i]]: String(q.i + 1) }}/>{grid(2, q.choices.map(c => [c, h3DegName(c)]))}</>; }
  else if (q.kind === 'inv') { const ns = h3Triad(q.k, q.dg, q.clef, q.inv); sound = () => h3Play([ns]);
    title = t(H3_TRI[q.k].en + ', ' + h3Rom(q.k, q.dg) + ': root position or first inversion?', H3_TRI[q.k].ko + ', ' + h3Rom(q.k, q.dg) + ': 기본 위치일까, 제1전위일까?');
    body = <><div style={{maxWidth:240,margin:'0 auto'}}><ChordStaff clef={q.clef} chords={[{ notes: ns, color: done ? BK.coral : BK.ink, label: done ? h3Rom(q.k, q.dg) + (q.inv ? 'b' : '') : null }]} width={180}/></div>{grid(2, [[0, t('Root position', '기본 위치')], [1, t('First inversion', '제1전위')]])}</>; }
  else if (q.kind === 'voice') { const c = h3CadChords(q.k, q.id)[q.i];
    title = t('Which voice sings the coral note?', '빨간 음은 어느 성부일까요?');
    body = <><div style={{maxWidth:280,margin:'0 auto'}}><SatbStaff chords={[c]} ks={H3_CAD[q.k].ks} hi={{ i: 0, v: q.v }} width={200}/></div>{grid(2, 'SATB'.split('').map(x => [x, h3Voice(x)]))}</>; }
  else { const cs = h3CadChords(q.k, q.id); sound = () => h3Play(cs.map(c => [c.S, c.A, c.T, c.B]), 60, 2);
    title = t(H3_CAD[q.k].en + ': perfect or plagal?', H3_CAD[q.k].ko + ': 정격종지일까, 변격종지일까?');
    body = <><div style={{maxWidth:300,margin:'0 auto'}}><SatbStaff chords={cs} ks={H3_CAD[q.k].ks} labels={done ? h3CadRom(q.k, q.id) : null} width={240}/></div>{grid(2, [['perfect', h3CadName('perfect')], ['plagal', h3CadName('plagal')]])}</>; }
  const why = !done || pixel ? null : q.kind === 'iv' ? t('In a minor key the 3rd and 6th are minor; the raised 7th is major.', '단조에서는 3도와 6도가 단음정, 올린 7도는 장음정.')
    : q.kind === 'inv' ? t(q.inv ? 'The 3rd is at the bottom.' : 'The root is at the bottom.', q.inv ? '3음이 맨 아래.' : '근음이 맨 아래.')
    : q.kind === 'voice' ? t('Treble: soprano up, alto down. Bass: tenor up, bass down.', '높은음: 소프라노 위, 알토 아래. 낮은음: 테너 위, 베이스 아래.')
    : q.kind === 'cad' ? t('Look at the bass: from the dominant (V) or the subdominant (IV) to the tonic.', '베이스를 봐요: 딸림음(V)에서, 아니면 버금딸림음(IV)에서 으뜸음으로.') : null;
  return (<div>
    <p style={pixel ? {fontSize:11.5,textAlign:'center'} : {fontSize:15,fontWeight:700,textAlign:'center',margin:'0 0 8px',color:'var(--muted)',textWrap:'balance'}}>{title}</p>
    {sound && <div style={{textAlign:'center',marginBottom:8}}><button className={pixel ? 'pixel-btn' : 'ghost-btn'} style={{minHeight:40}} onClick={sound}>{t('▶ Hear it', '▶ 들어 보기')}</button></div>}
    {body}
    {why && <div style={{marginTop:10,fontSize:13.5,color:'#4a4d86',background:'#fff',borderRadius:8,padding:'7px 10px',lineHeight:1.45}}>{why}</div>}
  </div>);
}
Object.assign(HARMONY_23_DRILL, { levels: H3_LEVELS, generate: genH3Question, check: (q, ans) => ans !== null && ans !== undefined && ans === q.answer, answerLabel: h3AnswerLabel, Question: H3Question, Learn: H3Learn });
// the teacher's copy: the answers for each step, in every key the chapter uses
function H3Teacher() {
  const pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="harmony-23" teacher>{content}</WbPage>);
  const ivRow = (k) => H3_MIN[k].en + ': ' + [2, 3, 4, 5, 6, 7, 8].map(n => { const [, b] = h3Above(k, 'treble', n); return h3Let(b) + ' ' + { M: 'M', m: 'm', P: 'P' }[H3_QMIN[n]] + (n === 8 ? '8' : n); }).join(', ');
  const triRow = (k) => H3_TRI[k].en + ': ' + [1, 4, 5].map(d => h3Rom(k, d) + ' ' + h3Triad(k, d, 'treble', 0).map(h3Let).join(' ') + ' / ' + h3Triad(k, d, 'treble', 1).map(h3Let).join(' ')).join(' · ');
  P(<>
    <div style={{fontFamily:LB_SERIF,fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('harmony-23')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 12px',lineHeight:1.5}}>Theory of Music, Grades 2 and 3. Every answer below is computed from the chapter's own data. The vocal ranges are the usual textbook ones: check them against the course book you use.</div>
    <TcBlock page={2} title="Above the tonic, in a minor key" answers={<>{tcAns('HARMONIC MINOR, ABOVE THE TONIC (M = MAJOR, m = MINOR, P = PERFECT)', H3_MIN_KEYS.map(ivRow))}</>}
      watch="Calling the 7th minor: in the harmonic minor it is the raised leading note, a major 7th. The 3rd and 6th are the ones that go minor."
      say="“Minor key: the 3rd and 6th go minor.”"/>
    <TcBlock page={3} title="The degree names" answers={<>{tcAns('1 TO 7', H3_DEGN.map(([en]) => en))}</>}
      watch="Subdominant taken as 'the note under the dominant' (it is, by position, but the name means a 5th below the tonic)."
      say="“Dominant: 5 up. Subdominant: 5 down.”"/>
  </>);
  P(<>
    <TcBlock page={4} title="Root position and first inversion" answers={<>{tcAns('ROOT / FIRST INVERSION', H3_TRI_KEYS.map(triRow))}</>}
      watch="A first inversion with the root still at the bottom and only the order of the upper notes changed. Check the lowest note: it must be the 3rd."
      say="“First inversion: the 3rd at the bottom.”"/>
    <TcBlock page={5} title="Soprano, alto, tenor, bass" answers={<>{tcAns('USUAL RANGES', ['soprano C4–G5', 'alto G3–C5', 'tenor C3–G4', 'bass E2–C4'])}</>}
      watch="Stems the wrong way, or the tenor written on the treble staff. Soprano and tenor stems up, alto and bass down."
      say="“Treble: soprano up, alto down. Bass: tenor up, bass down.”"/>
    <TcBlock page={6} title="Perfect and plagal cadences" answers={<>{tcAns('S, A, T, B', H3_CAD_KEYS.flatMap(k => ['perfect', 'plagal'].map(id => H3_CAD[k].en + ' ' + id + ': ' + H3_CAD[k][id].map((c, i) => h3CadRom(k, id)[i] + ' ' + c.map(x => x.replace('#', '♯').replace(/^([A-G])b/, '$1♭')).join(' ')).join(' → '))))}</>}
      watch="The leading note falling, or a shared note moved for no reason. Then check every pair of voices for parallel 5ths and octaves."
      say="“V–I perfect, IV–I plagal.”"/>
    <TcBlock page={7} title="My five checks" answers={<div style={{fontSize:12,color:BK.ink,lineHeight:1.5}}>Each one written on paper, then played at the piano. Use keys the child has not practised this week.</div>}/>
  </>);
  return <>{pages}</>;
}
TEACHER_COPIES['harmony-23'] = H3Teacher;
'''
rep("""TEACHER_COPIES['scales-23'] = ScfTeacher;""", """TEACHER_COPIES['scales-23'] = ScfTeacher;""" + CH)

HOME = r'''
// ══ Build AL: Intervals and Chords Further on the Home (Pitch, Chords) ══
LBH_FN['harmony-23'] = (s) => h3LbPages(s);
const h3HomeAdd = (id, i, en, ko, benEn, bko, make) => lbhAdd(id, 'p-chords', 'pitch', en, ko, benEn, bko, lbhSpec('harmony-23', i, { make }));
const h3AnsEK = (q) => q.kind === 'iv' ? [H3_QW[q.answer[0]][0] + ' ' + H3_ORD[Number(q.answer.slice(1))], H3_QW[q.answer[0]][1] + H3_ORDK[Number(q.answer.slice(1))]] : q.kind === 'deg' ? H3_DEGN[q.answer]
  : q.kind === 'inv' ? [['root position', '기본 위치'], ['first inversion', '제1전위']][q.answer] : q.kind === 'voice' ? H3_VOICE[q.answer] : [{ perfect: 'perfect cadence', plagal: 'plagal cadence' }[q.answer], { perfect: '정격종지', plagal: '변격종지' }[q.answer]];
const h3Q = (lv) => (n, prev) => { const q = genH3Question(H3_LEVELS[lv], prev), a = h3AnsEK(q);
  return { kind: 'choice', cols: q.kind === 'iv' ? 1 : 2, key: q.key, prompt: [h3Prompt(q, 'en'), h3Prompt(q, 'ko')], opts: q.choices.map(c => ({ id: c, label: () => h3AnswerLabel({ ...q, answer: c }) })), ans: q.answer, ok: (v) => v === q.answer,
    play: q.kind === 'cad' ? () => h3Play(h3CadChords(q.k, q.id).map(c => [c.S, c.A, c.T, c.B]), 60, 2) : null, fig: (c) => ({ mid: h3Fig(q, !!c.res) }),
    yes: ['Yes: ' + a[0] + '.', '맞아요: ' + a[1] + '.'], no: ['It is the ' + a[0] + '.', '답은 ' + a[1] + '.'] }; };
const h3Prompt = (q, lang) => { const ko = lang === 'ko';
  if (q.kind === 'iv') return ko ? H3_MIN[q.k].ko + ', 으뜸음 위: 음정의 이름은?' : H3_MIN[q.k].en + ', above the tonic: name the interval.';
  if (q.kind === 'deg') return ko ? 'C장조: ' + (q.i + 1) + '번째 음의 이름은?' : 'C major: the name of note ' + (q.i + 1) + '?';
  if (q.kind === 'inv') return ko ? H3_TRI[q.k].ko + ', ' + h3Rom(q.k, q.dg) + ': 기본 위치일까, 제1전위일까?' : H3_TRI[q.k].en + ', ' + h3Rom(q.k, q.dg) + ': root position or first inversion?';
  if (q.kind === 'voice') return ko ? '빨간 음은 어느 성부일까요?' : 'Which voice sings the coral note?';
  return ko ? H3_CAD[q.k].ko + ': 정격종지일까, 변격종지일까?' : H3_CAD[q.k].en + ': perfect or plagal?'; };
const h3Fig = (q, shown) => {
  if (q.kind === 'iv') { const [a, b] = h3Above(q.k, q.clef, q.n); return <div style={{maxWidth:260,margin:'0 auto'}}><IntervalStaff clef={q.clef} notes={[a, b]} colors={[BK.ink, shown ? BK.coral : BK.ink]} labels={[h3Let(a), shown ? h3Let(b) : '']} width={200}/></div>; }
  if (q.kind === 'deg') { const K = [0, 2, 4, 5, 7, 9, 11, 12], lit = {}; K.forEach((x, j) => { lit[x] = j === q.i ? 'cor' : 'pale'; }); return <SpKb lo={0} hi={12} W={28} H={76} lit={lit} names={{ [K[q.i]]: String(q.i + 1) }}/>; }
  if (q.kind === 'inv') { const ns = h3Triad(q.k, q.dg, q.clef, q.inv); return <div style={{maxWidth:240,margin:'0 auto'}}><ChordStaff clef={q.clef} chords={[{ notes: ns, color: shown ? BK.coral : BK.ink, label: shown ? h3Rom(q.k, q.dg) + (q.inv ? 'b' : '') : null }]} width={180}/></div>; }
  if (q.kind === 'voice') return <div style={{maxWidth:280,margin:'0 auto'}}><SatbStaff chords={[h3CadChords(q.k, q.id)[q.i]]} ks={H3_CAD[q.k].ks} hi={{ i: 0, v: q.v }} width={200}/></div>;
  return <div style={{maxWidth:300,margin:'0 auto'}}><SatbStaff chords={h3CadChords(q.k, q.id)} ks={H3_CAD[q.k].ks} labels={shown ? h3CadRom(q.k, q.id) : null} width={240}/></div>; };
h3HomeAdd('h3-iv', 1, 'Above the tonic, in a minor key', '단조에서 으뜸음 위의 음정', 'The 3rd and 6th go minor; the raised 7th is major.', '3도와 6도는 단음정, 올린 7도는 장음정.', h3Q(0));
h3HomeAdd('h3-deg', 2, 'The degree names', '음계 음의 이름', 'Tonic, supertonic, mediant… leading note.', '으뜸음, 윗으뜸음, 가온음… 이끎음.', h3Q(2));
h3HomeAdd('h3-inv', 3, 'Root position and first inversion', '기본 위치와 제1전위', 'First inversion: the 3rd at the bottom.', '제1전위: 3음이 맨 아래.', h3Q(3));
h3HomeAdd('h3-satb', 4, 'Soprano, alto, tenor, bass', '소프라노, 알토, 테너, 베이스', 'Four voices on two staves.', '두 오선 위의 네 성부.', h3Q(4));
h3HomeAdd('h3-cad', 5, 'Perfect and plagal cadences', '정격종지와 변격종지', 'V–I and IV–I in four parts.', '네 성부로 V–I와 IV–I.', h3Q(5));
'''
rep("""
lbhAdd('rb-finger', 'r-beat', 'rhythm', 'The beat in your fingers'""", HOME + """
lbhAdd('rb-finger', 'r-beat', 'rhythm', 'The beat in your fingers'""")
rep("""const LESSON_BOOKS = { 'scales-23': Scales23LessonBook,""", """const LESSON_BOOKS = { 'harmony-23': Harmony23LessonBook, 'scales-23': Scales23LessonBook,""")
rep("""const LB_PAGE_FNS = { 'scales-23': scfLbPages,""", """const LB_PAGE_FNS = { 'harmony-23': h3LbPages, 'scales-23': scfLbPages,""")
rep("""const HOUSE_ICONS = {"scales-23": """, """const HOUSE_ICONS = {"harmony-23": "<path d=\\"M6 12 H42 M6 18 H42 M6 30 H42 M6 36 H42\\"/><ellipse cx=\\"18\\" cy=\\"15\\" rx=\\"4\\" ry=\\"3\\" fill=\\"#26296b\\"/><ellipse cx=\\"18\\" cy=\\"33\\" rx=\\"4\\" ry=\\"3\\" fill=\\"#26296b\\"/><ellipse cx=\\"32\\" cy=\\"12\\" rx=\\"4\\" ry=\\"3\\" fill=\\"#e4572e\\" stroke=\\"#e4572e\\"/><ellipse cx=\\"32\\" cy=\\"36\\" rx=\\"4\\" ry=\\"3\\" fill=\\"#e4572e\\" stroke=\\"#e4572e\\"/>", "scales-23": """)
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
