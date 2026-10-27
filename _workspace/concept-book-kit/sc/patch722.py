import sys, json
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
PROG = json.load(open('/tmp/claude-0/-home-claude/c245f740-5546-5c71-9064-9bfc4952b3ac/scratchpad/h5/prog.json'))
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)
def after_line(prefix, text):
    global s
    lines = s.split('\n'); hits = [i for i, x in enumerate(lines) if x.startswith(prefix)]
    assert len(hits) == 1, (len(hits), prefix[:80])
    lines.insert(hits[0] + 1, text.strip('\n')); s = '\n'.join(lines)

# Build BC (board call 23, the fourth Grade 5 room): Chords and Cadences, Grade 5. Theory of Music Grade 5, Harmony (Manual of
# Syllabuses 2026, read 27 Oct): harmonise a melody of up to eight bars in four-part vocal style with I II(major only) IV V VI,
# Ib IIb IVb Vb VIb VIIb, Ic (cadential), unaccented passing and auxiliary notes; harmonise cadences in a melody or unfigured
# bass, preceding each cadence by a suitable chord. The three-chord progressions below come from a small voice-leading solver
# (scratchpad h5/solve.py): complete chords, the leading note never doubled and rising to the tonic in the soprano, no parallel
# or contrary 5ths and octaves, no hidden 5ths or octaves in the outer voices with a leaping soprano, no augmented or tritone
# leaps, no overlap, voices in range; the 6-4's 6th and 4th fall a step over a held bass; VIIb doubles its bass.

rep("""const HARMONY_4_DRILL = { id: 'harmony-4', label: 'Chords and Cadences, Grade 4' };   // Build AU""",
    """const HARMONY_4_DRILL = { id: 'harmony-4', label: 'Chords and Cadences, Grade 4' };   // Build AU
const HARMONY_5_DRILL = { id: 'harmony-5', label: 'Chords and Cadences, Grade 5' };   // Build BC""")
rep("""  { id: 'harmony-4', label: 'Chords and Cadences, Grade 4', concept: HARMONY_4_DRILL, track: 'start' },   // Build AU""",
    """  { id: 'harmony-4', label: 'Chords and Cadences, Grade 4', concept: HARMONY_4_DRILL, track: 'start' },   // Build AU
  { id: 'harmony-5', label: 'Chords and Cadences, Grade 5', concept: HARMONY_5_DRILL, track: 'start' },   // Build BC""")
def reg(pattern, add):
    global s
    import re
    m = re.findall(pattern, s); assert len(m) == 1, (len(m), pattern)
    s = s.replace(m[0], m[0] + add)
reg(r"'harmony-4': '화음과 종지, Grade 4'", ", 'harmony-5': '화음과 종지, Grade 5'")
reg(r"'harmony-4': 'p-chords'", ", 'harmony-5': 'p-chords'")
reg(r"'harmony-4': \['harmony-23', 'keys-4'\]", ", 'harmony-5': ['harmony-4', 'keys-5']")
reg(r"'harmony-4': \['Chords 4', '[^']*'\]", ", 'harmony-5': ['Chords 5', '화음 5']")
rep("""  'harmony-4': 'chords cadences grade 4""", """  'harmony-5': 'chords cadences grade 5 theory leading note chord seventh first inversion viib cadential six four 6-4 passing auxiliary notes approach chord before the cadence harmonise eight bar melody four part vocal',
  'harmony-4': 'chords cadences grade 4""")

CH = r'''
// ─── Chapter: Chords and Cadences, Grade 5 (Build BC, 2026-10-27; board call 23, the fourth Grade 5 room) ───
// Every first inversion and the new leading-note chord, vii°b; the cadential 6-4, Ic–V–I; unaccented passing and auxiliary notes;
// the chord before a cadence (IIb, IV, IVb or Ic; in a minor key iv, ivb, VI or ic); harmonising an eight-note melody with the
// whole vocabulary. Single chords are voiced by rule as in Grade 4 (vii°b: the bass doubled, the leading note once); the
// three-chord progressions are the solver's checked realisations (see the build note in patch722).
const h5Rom = (k, deg, inv) => (deg === 7 ? 'vii°' : H4_ROM[h4Min(k) ? 'min' : 'maj'][deg]) + ['', 'b', 'c'][inv];
const H5_DEGS = (k) => H4_DEGS(k).concat([7]);
function h5Chord(k, deg, inv) {
  if (deg !== 7) return h4Chord(k, deg, inv);
  const td = h4Td(k), r = 6, note = (x) => h4Note(k, td, x), isT = (x) => [0, 2, 4].includes((((x - r) % 7) + 7) % 7);
  let b = r + 2 - 7; while (h4M(note(b)) > 52) b -= 7; while (h4M(note(b)) < 40) b += 7;
  const B = note(b), cands = [];   // close position above: three different notes, so the bass is the one doubled
  for (let t0 = b + 1; t0 < b + 15; t0++) { if (!isT(t0)) continue; const ups = [t0]; let x = t0 + 1; while (ups.length < 3) { if (isT(x)) ups.push(x); x++; }
    const [T, A, S] = ups.map(note), inR = (v, n) => h4M(n) >= H4_RANGE[v][0] && h4M(n) <= H4_RANGE[v][1];
    if (inR('T', T) && inR('A', A) && inR('S', S) && h4M(T) - h4M(B) >= 3) cands.push({ S, A, T, B }); }
  cands.sort((p, q) => Math.abs(h4M(p.S) - 69) - Math.abs(h4M(q.S) - 69)); return cands[0];
}
const H5_PROG = __PROG__;
const H5_PKEYS = Object.keys(H5_PROG);
const h5Prog = (k, nm) => H5_PROG[k][nm].map(str => { const [S, A, T, B] = str.split(' ').map(h3N); return { S, A, T, B }; });
const H5_PRE = { iib: [2, 1], iv: [4, 0], ivb: [4, 1], c64: [1, 2], vi: [6, 0] };   // the chord before V, as [degree, position]
const h5PreOpts = (k) => (h4Min(k) ? ['iv', 'ivb', 'vi', 'c64'] : ['iib', 'iv', 'ivb', 'c64']);
const h5PreRom = (k, nm) => h5Rom(k, H5_PRE[nm][0], H5_PRE[nm][1]);
// passing and auxiliary notes: strong, weak, strong ... (the chords change on the strong notes, c)
const H5_PASS = [
  { k: 'C', m: ['E4', 'F4', 'G4', 'A4', 'G4', 'E4', 'C4'], c: [1, 5, 1, 1] },
  { k: 'G', m: ['B4', 'C5', 'D5', 'E5', 'D5', 'A4', 'B4'], c: [1, 5, 5, 1] },
  { k: 'F', m: ['A4', 'Bb4', 'C5', 'G4', 'F4', 'G4', 'A4'], c: [1, 5, 1, 1] },
  { k: 'D', m: ['F#4', 'E4', 'D4', 'E4', 'F#4', 'B4', 'D5'], c: [1, 4, 6, 1] },
  { k: 'Am', m: ['C5', 'B4', 'A4', 'G#4', 'A4', 'B4', 'C5'], c: [1, 4, 1, 6] },
  { k: 'Dm', m: ['D5', 'E5', 'F5', 'E5', 'D5', 'Bb4', 'D5'], c: [1, 6, 4, 1] },
  { k: 'C', m: ['G4', 'A4', 'G4', 'F4', 'E4', 'D4', 'C4'], c: [1, 5, 1, 1] },
  { k: 'Bb', m: ['F4', 'G4', 'F4', 'Eb4', 'D4', 'F4', 'Bb4'], c: [1, 5, 1, 1] },
];
const h5PassKind = (i, j) => { const M = H5_PASS[i], ns = M.m.map(h3N), n = ns[j], a = ns[j - 1], b = ns[j + 1], deg = M.c[(j - 1) / 2];
  if (h4Has(M.k, deg, n)) return 'chord'; if (a.d === b.d && a.acc === b.acc && Math.abs(n.d - a.d) === 1) return 'aux'; if (n.d - a.d === b.d - n.d && Math.abs(n.d - a.d) === 1) return 'pass'; return null; };
const h5PassLabels = (i) => H5_PASS[i].m.map((_, x) => (x % 2 === 0 ? h5Rom(H5_PASS[i].k, H5_PASS[i].c[x / 2], 0) : ''));
const H5_PK = { chord: ['A chord note', '화음 음'], pass: ['A passing note', '경과음'], aux: ['An auxiliary note', '보조음'] };
// eight-note melodies to harmonise, one chord a note (start on the tonic chord; a cadence at the end)
const H5_MEL = [
  { k: 'C', m: ['C5', 'B4', 'A4', 'G4', 'F4', 'E4', 'D4', 'C4'] },
  { k: 'G', m: ['D5', 'C5', 'B4', 'E5', 'D5', 'B4', 'A4', 'G4'] },
  { k: 'F', m: ['A4', 'C5', 'Bb4', 'G4', 'A4', 'F4', 'E4', 'F4'] },
  { k: 'D', m: ['F#4', 'G4', 'A4', 'B4', 'A4', 'G4', 'E4', 'D4'] },
  { k: 'Am', m: ['C5', 'B4', 'A4', 'D5', 'C5', 'B4', 'G#4', 'A4'] },
  { k: 'Bb', m: ['D5', 'C5', 'Bb4', 'Eb5', 'D5', 'C5', 'A4', 'Bb4'] },
];

// ── the questions (shared by the steps, the drill and the Home) ──
function genH5(kind, prev, fixed) {
  const uid = Math.random(), again = (key) => prev && prev.key === key;
  if (kind === 'inv') { let k, deg, g = 0; do { k = fixed ? fixed.k : pick(H5_PKEYS); deg = fixed ? fixed.deg : (Math.random() < 0.3 ? 7 : pick(H4_DEGS(k))); } while (!fixed && again('i' + k + deg) && g++ < 12);
    const ans = h5Rom(k, deg, 1), bassDeg = ((deg + 1) % 7) + 1, trap = H4_DEGS(k).includes(bassDeg) ? h5Rom(k, bassDeg, 0) : null;
    let ch = [...new Set([ans, deg === 7 ? h5Rom(k, 5, 1) : h5Rom(k, deg, 0), trap || h5Rom(k, H4_DEGS(k).find(d => d !== deg), 1), deg === 7 ? h5Rom(k, 2 in H4_ROM[h4Min(k) ? 'min' : 'maj'] ? 2 : 4, 1) : h5Rom(k, 7, 1)])];
    return { kind, k, deg, chord: h5Chord(k, deg, 1), answer: ans, choices: shuffle(ch).slice(0, 4), key: 'i' + k + deg, uid }; }
  if (kind === 'c64') { let k, p, g = 0; do { k = fixed ? fixed.k : pick(H5_PKEYS); p = fixed ? fixed.p : Math.floor(Math.random() * 3); } while (!fixed && again('c' + k + p) && g++ < 12);
    return { kind, k, p, chords: h5Prog(k, ['r64', 'b64', 'c64'][p]), answer: h5Rom(k, 1, p), choices: [0, 1, 2].map(x => h5Rom(k, 1, x)), key: 'c' + k + p, uid }; }
  if (kind === 'pre') { let k, o, g = 0; do { k = fixed ? fixed.k : pick(H5_PKEYS); o = fixed ? fixed.o : pick(h5PreOpts(k)); } while (!fixed && again('p' + k + o) && g++ < 12);
    return { kind, k, o, chords: h5Prog(k, o), answer: h5PreRom(k, o), choices: h5PreOpts(k).map(x => h5PreRom(k, x)), key: 'p' + k + o, uid }; }
  if (kind === 'pass') { let i, j, g = 0; do { i = fixed ? fixed.i : Math.floor(Math.random() * H5_PASS.length); j = fixed ? fixed.j : pick([1, 3, 5]); } while (!fixed && again('s' + i + j) && g++ < 12);
    return { kind, i, j, k: H5_PASS[i].k, answer: h5PassKind(i, j), choices: ['chord', 'pass', 'aux'], key: 's' + i + j, uid }; }
  let i, j, g = 0; do { i = fixed ? fixed.i : Math.floor(Math.random() * H5_MEL.length); j = fixed ? fixed.j : Math.floor(Math.random() * 8); } while (!fixed && again('f' + i + j) && g++ < 12);
  const M = H5_MEL[i], n = h3N(M.m[j]), fits = H4_DEGS(M.k).filter(d => h4Has(M.k, d, n)), nots = H4_DEGS(M.k).filter(d => !h4Has(M.k, d, n));
  const ans = h5Rom(M.k, pick(fits), 0), ch = shuffle([ans, ...shuffle(nots).slice(0, 2).map(d => h5Rom(M.k, d, 0))]);
  return { kind: 'fit', i, j, k: M.k, n, fits: fits.map(d => h5Rom(M.k, d, 0)), answer: ans, choices: ch, key: 'f' + i + j, uid };
}
const h5Ok = (q, c) => (q.kind === 'fit' ? q.fits.includes(c) : c === q.answer);
const h5Lab = (q, c) => (q.kind === 'pass' ? t(H5_PK[c][0], H5_PK[c][1]) : c);
function h5Prompt(q) {
  if (q.kind === 'inv') return t(h4Name(q.k) + ': which first inversion is this?', h4Name(q.k) + ': 어떤 첫째 자리바꿈일까요?');
  if (q.kind === 'c64') return t(h4Name(q.k) + ': the first chord is the tonic chord. Which position?', h4Name(q.k) + ': 첫 화음은 으뜸화음. 어떤 자리일까요?');
  if (q.kind === 'pre') return t(h4Name(q.k) + ', a perfect cadence: which chord comes before V?', h4Name(q.k) + ', 정격종지: V 앞의 화음은?');
  if (q.kind === 'pass') return t(h4Name(q.k) + ': the coral note, on a weak beat, is?', h4Name(q.k) + ': 약박의 빨간 음은?');
  return t(h4Name(q.k) + ': which chord holds the coral melody note?', h4Name(q.k) + ': 빨간 선율 음이 들어 있는 화음은?');
}
const h5Letters = (k, deg) => [0, 2, 4].map(x => h3Let(h4Note(k, h4Td(k), deg - 1 + x))).join(' ');
function h5Why(q) {
  if (q.kind === 'inv') return q.deg === 7 ? t(q.answer + ': ' + h5Letters(q.k, 7) + ', the chord on the leading note, with its 3rd, ' + h3Let(q.chord.B) + ', in the bass. The bass is doubled; the leading note never is.', q.answer + ': ' + h5Letters(q.k, 7) + ', 이끎음 위의 화음, 베이스에는 3음 ' + h3Let(q.chord.B) + '. 베이스를 겹치고, 이끎음은 절대 겹치지 않아요.')
    : t(q.answer + ': the chord is ' + h5Letters(q.k, q.deg) + ' and its 3rd, ' + h3Let(q.chord.B) + ', is in the bass. Name a chord by its root, not by its bass note.', q.answer + ': 화음은 ' + h5Letters(q.k, q.deg) + ', 베이스에는 3음 ' + h3Let(q.chord.B) + '. 화음 이름은 베이스가 아니라 근음으로 지어요.');
  if (q.kind === 'c64') { const B = h3Let(q.chords[0].B), I = h5Rom(q.k, 1, 0); return [t(I + ': the root, ' + B + ', in the bass.', I + ': 베이스에 근음 ' + B + '.'), t(I + 'b: the 3rd, ' + B + ', in the bass.', I + 'b: 베이스에 3음 ' + B + '.'), t(I + 'c: the 5th, ' + B + ', in the bass, the same bass as V. Above it a 6th and a 4th fall a step into V: the cadential 6-4.', I + 'c: 베이스에 5음 ' + B + ', V와 같은 베이스. 그 위의 6도와 4도가 한 음씩 내려가 V로: 종지의 6-4.')][q.p]; }
  if (q.kind === 'pre') { const B = h3Let(q.chords[0].B); return t(q.answer + ' (bass ' + B + ') leads into V–' + h5Rom(q.k, 1, 0) + '.' + (q.o === 'c64' ? ' ' + h5Rom(q.k, 1, 2) + ' shares V\'s bass: its 6th and 4th fall onto V.' : q.o === 'ivb' || q.o === 'iib' ? ' A first inversion: the bass steps up to V.' : ''), q.answer + '(베이스 ' + B + ')가 V–' + h5Rom(q.k, 1, 0) + '로 이어져요.' + (q.o === 'c64' ? ' ' + h5Rom(q.k, 1, 2) + '는 V와 베이스가 같고, 6도와 4도가 V로 내려가요.' : q.o === 'ivb' || q.o === 'iib' ? ' 첫째 자리바꿈: 베이스가 V로 한 음 올라가요.' : '')); }
  if (q.kind === 'pass') { const M = H5_PASS[q.i], ns = M.m.map(h3N), [a, n, b] = [ns[q.j - 1], ns[q.j], ns[q.j + 1]].map(h3Let), deg = M.c[(q.j - 1) / 2], R = h5Rom(M.k, deg, 0);
    return q.answer === 'chord' ? t(n + ' is in ' + R + ' (' + h5Letters(M.k, deg) + '): a chord note, reached by a leap.', '선율 음 ' + n + ': ' + R + '(' + h5Letters(M.k, deg) + ')의 화음 음, 도약으로 왔어요.')
      : q.answer === 'pass' ? t(n + ' is not in ' + R + '; it fills the step from ' + a + ' to ' + b + ': a passing note.', '선율 음 ' + n + ': ' + R + '에 없는 음; ' + a + '에서 ' + b + '까지 한 음씩 채워요: 경과음.')
      : t(n + ' is not in ' + R + '; it steps away from ' + a + ' and back: an auxiliary note.', '선율 음 ' + n + ': ' + R + '에 없는 음; ' + a + '에서 한 음 떠났다 돌아와요: 보조음.'); }
  return t(h3Let(q.n) + ' is in ' + q.fits.map(r => r + ' (' + h5Letters(q.k, H4_DEGS(q.k).find(d => h5Rom(q.k, d, 0) === r)) + ')').join(', ') + '.', '선율 음 ' + h3Let(q.n) + ': ' + q.fits.map(r => r + '(' + h5Letters(q.k, H4_DEGS(q.k).find(d => h5Rom(q.k, d, 0) === r)) + ')').join(', ') + '에 들어 있어요.');
}
const h5PlayQ = (q) => (q.kind === 'inv' ? () => h4Play([q.chord]) : q.kind === 'c64' || q.kind === 'pre' ? () => h4Play(q.chords) : q.kind === 'pass' ? () => { const M = H5_PASS[q.i]; spPlay(M.m.map((x, j) => ({ at: j * 0.5, keys: [h3Semi(h3N(x))].concat(j % 2 === 0 ? [h3Semi(h4Note(M.k, h4Td(M.k) - 7, M.c[j / 2] - 1))] : []), len: j % 2 === 0 ? 0.95 : 0.45, vol: 0.13 })), 66); } : null);
function h5Fig(q, shown, scr = true) {
  const ks = H4_KEYS[q.k][2];
  if (q.kind === 'inv') return <div style={{maxWidth:280,margin:'0 auto'}}><SatbStaff chords={[q.chord]} ks={ks} labels={shown ? [q.answer] : null} width={200}/></div>;
  if (q.kind === 'c64' || q.kind === 'pre') return <div style={{maxWidth:340,margin:'0 auto'}}><SatbStaff chords={q.chords} ks={ks} labels={[shown ? q.answer : '?', 'V', h5Rom(q.k, 1, 0)]} width={250}/></div>;
  if (q.kind === 'pass') { const M = H5_PASS[q.i]; return <K4Melody notes={M.m.map(h3N)} ks={ks} hi={[q.j]} labels={h5PassLabels(q.i)} width={scr ? 300 : 360}/>; }
  const M = H5_MEL[q.i]; return <K4Melody notes={M.m.map(h3N)} ks={ks} hi={[q.j]} width={scr ? 320 : 380}/>;
}
function H5Pad({ kind, title, note, first, fixed, onResult }) {
  const [q, setQ] = useState(() => genH5(kind, null, fixed || first)), [pickd, setPick] = useState(null), [run, setRun] = useState(0);
  const say = (c) => { if (pickd != null) return; setPick(c); const ok = h5Ok(q, c); setRun(r => (ok ? r + 1 : 0)); if (onResult) onResult({ ok }); };
  const next = () => { setQ(genH5(kind, q)); setPick(null); };
  const play = h5PlayQ(q), shown = pickd != null, good = shown && h5Ok(q, pickd), cols = q.kind === 'pass' ? 1 : q.choices.length > 3 ? 2 : q.choices.length;
  return (
    <div className="try-box" style={actBox} data-h5={kind}>
      <div style={actTitle}>{title}</div>
      <div style={actNote}>{note}</div>
      <div style={{textAlign:'center',fontSize:14.5,fontWeight:800,color:BK.ink,margin:'2px 0 6px',textWrap:'balance'}}>{h5Prompt(q)}</div>
      {h5Fig(q, shown)}
      <div style={{display:'grid',gridTemplateColumns:'repeat(' + cols + ',minmax(0,1fr))',gap:8,marginTop:10}}>{q.choices.map(c => <button key={c} className={'choice-btn' + (!shown ? '' : h5Ok(q, c) && (c === pickd || q.kind !== 'fit') ? ' good' : c === pickd ? ' bad' : '')} onClick={() => say(c)} style={{padding:'11px 4px',fontSize:q.kind === 'pass' ? 15 : 17,fontWeight:900}}>{h5Lab(q, c)}</button>)}</div>
      {shown && <div style={{marginTop:10,fontSize:13.5,color:'#4a4d86',background:'#fff',borderRadius:8,padding:'7px 10px',lineHeight:1.45}}>{(good ? t('Yes. ', '맞아요. ') + (run > 1 ? t(run + ' in a row. ', run + '번 연속. ') : '') : '') + h5Why(q)}</div>}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        {play && <button className="ghost-btn" style={spBtn} onClick={play}>{t('▶ Hear it', '▶ 들어 보기')}</button>}
        {shown && !fixed && <button className="ghost-btn" style={spBtn} onClick={next}>{t('▶ Another', '▶ 다른 것')}</button>}
      </div>
    </div>
  );
}
// ── step 5: an eight-note melody, a chord for every note, the whole Grade 5 vocabulary ──
function H5HarmPad({ fixed, onResult }) {
  const [i, setI] = useState(fixed != null ? fixed : 0), [sel, setSel] = useState([]), [at, setAt] = useState(0), [pos, setPos] = useState(0), [res, setRes] = useState(null);
  const M = H5_MEL[i], ns = M.m.map(h3N), degs = H5_DEGS(M.k), n = ns.length, ks = H4_KEYS[M.k][2], I1 = h5Rom(M.k, 1, 0);
  const reset = (j) => { setI(j); setSel([]); setAt(0); setPos(0); setRes(null); };
  const choose = (deg) => { if (res) return; const s2 = sel.slice(); s2[at] = [deg, deg === 7 ? 1 : pos]; setSel(s2); setPos(0); if (at < n - 1) setAt(at + 1); };
  const check = () => { const fit = ns.map((nt, j) => sel[j] != null && h4Has(M.k, sel[j][0], nt)), is = (j, d, p) => sel[j] && sel[j][0] === d && sel[j][1] === p;
    const start = sel[0] && sel[0][0] === 1 && sel[0][1] < 2, cad = is(n - 1, 1, 0) && (is(n - 2, 5, 0) || is(n - 2, 4, 0));
    const c64 = sel.every((x, j) => !(x && x[0] === 1 && x[1] === 2) || is(j + 1, 5, 0)), vii = sel.every((x, j) => !(x && x[0] === 7) || (sel[j + 1] && sel[j + 1][0] === 1 && sel[j + 1][1] < 2));
    const r = { fit, start, cad, c64, vii, ok: fit.every(Boolean) && start && cad && c64 && vii }; setRes(r); if (onResult) onResult({ ok: r.ok }); };
  const play = () => { spPlay(ns.flatMap((nt, j) => { const x = sel[j]; if (!x) return [{ at: j * 1.1, keys: [h3Semi(nt)], len: 1 }];
    const c = h5Chord(M.k, x[0], x[1] === 2 ? 0 : x[1]), bass = x[1] === 2 ? h4Note(M.k, h4Td(M.k) - 7, 4) : c.B; return [{ at: j * 1.1, keys: [h3Semi(nt), h3Semi(bass), h3Semi(c.T), h3Semi(c.A)], len: 1, vol: 0.09 }]; }), 72); };
  const full = sel.filter(x => x != null).length === n, lab = (x) => h5Rom(M.k, x[0], x[1]);
  const msg = res ? (res.ok ? t('It works: every chord holds its note, and it ends ' + (sel[n - 2][0] === 5 ? 'V–I, a perfect cadence' : 'IV–I, a plagal cadence') + (sel.some(x => x[1] === 2) ? ', with the cadential 6-4.' : '.'), '좋아요: 화음마다 그 음이 들어 있고, 끝은 ' + (sel[n - 2][0] === 5 ? 'V–I, 정격종지' : 'IV–I, 변격종지') + (sel.some(x => x[1] === 2) ? ', 종지의 6-4와 함께.' : '.'))
    : !res.fit.every(Boolean) ? t('Note ' + (res.fit.indexOf(false) + 1) + ' is not in its chord.', (res.fit.indexOf(false) + 1) + '번째 음이 그 화음에 없어요.')
    : !res.start ? t('Start on the tonic chord, ' + I1 + ' or ' + I1 + 'b.', '으뜸화음 ' + I1 + '이나 ' + I1 + 'b로 시작해요.') : !res.cad ? t('End with V–' + I1 + ' or IV–' + I1 + ', both in root position: a cadence.', 'V–' + I1 + ' 또는 IV–' + I1 + ', 둘 다 기본 위치로 끝내요: 종지.')
    : !res.c64 ? t(I1 + 'c goes straight to V: Ic–V–I.', I1 + 'c 다음은 바로 V: Ic–V–I.') : t('vii°b goes to ' + I1 + ' or ' + I1 + 'b.', 'vii°b 다음은 ' + I1 + '이나 ' + I1 + 'b.'))
    : t('Note ' + (at + 1) + ' of ' + n + ': ' + h3Let(ns[at]) + '. Which chord?', n + '개 중 ' + (at + 1) + '번째 음: ' + h3Let(ns[at]) + '. 어떤 화음?');
  return (
    <div className="try-box" style={actBox} data-h5="harm">
      <div style={actTitle}>{t('Harmonise eight notes', '여덟 음에 화음 붙이기')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>음마다 그 음이 <b>들어 있는 화음</b>을 골라요. 자리(<b>b</b>: 3음이 베이스, <b>c</b>: 5음이 베이스)를 먼저 고를 수 있어요. 으뜸화음으로 시작하고, 끝은 <b>V–I</b>나 <b>IV–I</b>. 선율이 허락하면 <b>Ic–V–I</b>. 네 성부로 적는 건 선생님과 종이에서.</>
        : <>For each note, choose a chord that <b>holds it</b>. Pick a position first if you want one (<b>b</b>: the 3rd in the bass; <b>c</b>: the 5th). Start on the tonic chord and end with <b>V–I</b> or <b>IV–I</b>; where the melody allows, <b>Ic–V–I</b>. Writing the four parts comes next, on paper with your teacher.</>}</div>
      {fixed == null && spChips(H5_MEL.map((x, j) => [j, h4Name(x.k) + ' ' + (j + 1)]), i, reset)}
      <K4Melody notes={ns} ks={ks} hi={res ? (res.fit.indexOf(false) >= 0 ? [res.fit.indexOf(false)] : []) : [at]} labels={ns.map((_, j) => (sel[j] ? lab(sel[j]) : '·'))} width={360}/>
      {!res && <>{spChips([[0, t('Root', '기본')], [1, 'b'], [2, 'c']], pos, setPos)}
        <div style={{display:'grid',gridTemplateColumns:'repeat(' + degs.length + ',minmax(0,1fr))',gap:5,marginTop:4}}>{degs.map(d => { const off = pos === 2 && d !== 1; return <button key={d} className="choice-btn" disabled={off} onClick={() => choose(d)} style={{padding:'10px 1px',fontSize:15,fontWeight:900,opacity:off ? 0.35 : 1}}>{h5Rom(M.k, d, d === 7 ? 1 : pos)}</button>; })}</div>
        <div style={{display:'flex',gap:3,justifyContent:'center',flexWrap:'wrap',marginTop:6}}>{ns.map((_, j) => <button key={j} onClick={() => setAt(j)} className={'chip' + (j === at ? ' active' : '')} style={{minHeight:32,minWidth:30,padding:'2px 4px'}}>{j + 1}</button>)}</div></>}
      {spMsg(msg, res ? (res.ok ? BK.green : BK.coral) : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        {full && !res && <button className="ghost-btn" style={spBtn} onClick={check}>{t('✓ Check', '✓ 확인')}</button>}
        <button className="ghost-btn" style={spBtn} onClick={play}>{t('▶ Hear it', '▶ 들어 보기')}</button>
        {res && <button className="ghost-btn" style={spBtn} onClick={() => { setRes(null); setAt(res.fit.indexOf(false) >= 0 ? res.fit.indexOf(false) : n - 2); }}>{t('✎ Change', '✎ 고치기')}</button>}
      </div>
    </div>
  );
}
const H5_NOTE = {
  inv: [<>Grade 5 uses <b>every first inversion</b>: Ib, iib, IVb, Vb, vib, and one new chord, <b>vii°b</b>, the chord on the leading note, used in first inversion. Stack the notes in 3rds to find the root; the bass is the 3rd. In vii°b the bass is doubled, never the leading note.</>,
    <>5급은 <b>모든 첫째 자리바꿈</b>을 써요: Ib, iib, IVb, Vb, vib, 그리고 새 화음 <b>vii°b</b>, 이끎음 위의 화음을 첫째 자리바꿈으로. 음을 3도로 쌓아 근음을 찾아요; 베이스는 3음. vii°b는 베이스를 겹치고, 이끎음은 절대 겹치지 않아요.</>],
  c64: [<>The <b>cadential 6-4</b>, <b>Ic</b>: the tonic chord with its <b>5th in the bass</b>, the same bass as the V that follows. Above the bass a 6th and a 4th, and both <b>fall a step</b> into V: <b>Ic–V–I</b>. Ib has the 3rd in the bass; I the root.</>,
    <><b>종지의 6-4</b>, <b>Ic</b>: 으뜸화음의 <b>5음이 베이스</b>, 뒤따르는 V와 같은 베이스. 베이스 위의 6도와 4도가 둘 다 <b>한 음씩 내려가</b> V로: <b>Ic–V–I</b>. Ib는 3음이, I은 근음이 베이스.</>],
  pass: [<>Not every melody note needs its own chord. On a weak beat a <b>passing note</b> fills the step between two chord notes (C–<b>D</b>–E), and an <b>auxiliary note</b> steps away and comes back (C–<b>D</b>–C). Here the chords change on the strong notes, the ones with a chord name.</>,
    <>선율 음마다 화음이 필요하진 않아요. 약박에서 <b>경과음</b>은 두 화음 음 사이를 한 음씩 채우고(C–<b>D</b>–E), <b>보조음</b>은 한 음 떠났다 돌아와요(C–<b>D</b>–C). 여기서는 화음 이름이 붙은 강박 음에서 화음이 바뀌어요.</>],
  pre: [<>A cadence sounds stronger with <b>a good chord before it</b>. Before V: <b>iib, IV, IVb or Ic</b> (in a minor key iv, ivb, VI or ic). Each leads smoothly into V: hear it, then name it.</>,
    <>종지는 <b>앞에 좋은 화음</b>이 오면 더 단단하게 들려요. V 앞에: <b>iib, IV, IVb, Ic</b>(단조에서는 iv, ivb, VI, ic). 모두 V로 매끄럽게 이어져요: 듣고, 이름을 말해요.</>],
  harm: [<>Eight notes, eight chords. Start on the tonic chord, choose a chord that <b>holds each note</b>, try a <b>first inversion</b> where the bass would rather move by step, and end with a cadence: <b>Ic–V–I</b> where the melody allows.</>,
    <>여덟 음, 여덟 화음. 으뜸화음으로 시작해서 음마다 <b>그 음이 든 화음</b>을 고르고, 베이스가 한 음씩 움직이면 좋을 곳에는 <b>첫째 자리바꿈</b>, 끝은 종지: 선율이 허락하면 <b>Ic–V–I</b>.</>],
};
const h5NoteT = (k) => (LANG === 'ko' ? H5_NOTE[k][1] : H5_NOTE[k][0]);
const H5_STEP = { inv: ['vii°b and the first inversions', 'vii°b와 첫째 자리바꿈'], c64: ['The cadential 6-4', '종지의 6-4'], pass: ['Passing and auxiliary notes', '경과음과 보조음'], pre: ['The chord before the cadence', '종지 앞의 화음'], harm: ['Harmonise eight notes', '여덟 음에 화음 붙이기'] };
const h5StepT = (k) => t(H5_STEP[k][0], H5_STEP[k][1]);
const H5_FIRST = { inv: { k: 'C', deg: 7 }, c64: { k: 'C', p: 2 }, pass: { i: 0, j: 1 }, pre: { k: 'G', o: 'iib' } };
const H5Step = ({ kind, fixed, onResult }) => kind === 'harm' ? <H5HarmPad fixed={fixed} onResult={onResult}/> : <H5Pad kind={kind} title={h5StepT(kind)} note={h5NoteT(kind)} first={H5_FIRST[kind]} fixed={fixed} onResult={onResult}/>;

// ── the pictures on paper ──
const h5PicVii = () => ({ shapes: [{ k: 'raw', svg: '<text x="4" y="28" font-size="15" font-weight="900" fill="#e4572e" font-family="Inter, sans-serif">vii°b</text>' }], vb: [0, 0, 70, 44] });
const h5PicC64 = () => ({ shapes: [{ k: 'raw', svg: '<text x="2" y="28" font-size="13" font-weight="900" fill="#e4572e" font-family="Inter, sans-serif">Ic</text><text x="22" y="28" font-size="13" font-weight="900" fill="#26296b" font-family="Inter, sans-serif">V</text><text x="40" y="28" font-size="13" font-weight="900" fill="#26296b" font-family="Inter, sans-serif">I</text><circle cx="56" cy="24" r="3" fill="#26296b"/>' }], vb: [0, 0, 70, 44] });
const h5PicPass = () => ({ shapes: [{ k: 'raw', svg: [[10, 30], [26, 24], [42, 18]].map(([x, y], i) => lsCircleSvg(x, y, 5, i === 1 ? 'play' : 'beat', '')).join('') + [[58, 30]].map(([x, y]) => lsCircleSvg(x, y, 5, 'beat', '')).join('') }], vb: [0, 0, 70, 44] });
const h5PicPre = () => ({ shapes: [{ k: 'raw', svg: '<text x="2" y="28" font-size="12" font-weight="900" fill="#e4572e" font-family="Inter, sans-serif">iib</text><text x="26" y="28" font-size="12" font-weight="900" fill="#26296b" font-family="Inter, sans-serif">V</text><text x="42" y="28" font-size="12" font-weight="900" fill="#26296b" font-family="Inter, sans-serif">I</text>' }], vb: [0, 0, 70, 44] });

function h5LbPages(scr = false) {
  const ch = 'harmony-5', kinds = ['inv', 'c64', 'pass', 'pre', 'harm'], h4n = bkChapterNo('harmony-4');
  const pen = (x) => <PenArt shapes={x.shapes} vb={x.vb} style={{width:90}}/>;
  const checks5 = [[h5PicVii(), t('I name every first inversion, vii°b too', 'vii°b까지, 모든 첫째 자리바꿈의 이름을 말해요')], [h5PicC64(), t('I write the cadential 6-4: Ic–V–I', '종지의 6-4를 적어요: Ic–V–I')],
    [h5PicPass(), t('I tell passing and auxiliary notes from chord notes', '경과음과 보조음을 화음 음과 구별해요')], [h5PicPre(), t('I choose a good chord before a cadence', '종지 앞에 좋은 화음을 골라요')],
    [h4PicFit(), t('I harmonise an eight-note melody, ending with a cadence', '여덟 음 선율에 화음을 붙이고, 종지로 끝내요')]];
  const toc = kinds.map((k, i) => [h5StepT(k), i + 2]).concat([[t('My five checks', '나의 다섯 가지 확인'), 7]]);
  const satb = (k, nm, labs, w) => <SatbStaff chords={h5Prog(k, nm)} ks={H4_KEYS[k][2]} labels={labs} width={w || 220}/>;
  const still = (kind) => {
    if (kind === 'inv') return <LbPic h={160}><div style={{display:'grid',gridTemplateColumns:scr ? 'repeat(3,1fr)' : 'repeat(6,1fr)',gap:4,width:'100%',maxWidth:700,margin:'0 auto'}}>{H5_DEGS('C').map(d => <div key={d}><SatbStaff chords={[h5Chord('C', d, 1)]} ks={[null, 0]} labels={[h5Rom('C', d, 1)]} width={120}/></div>)}</div></LbPic>;
    if (kind === 'c64') return <LbPic h={160}><div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:12,width:'100%',maxWidth:620,margin:'0 auto'}}><div>{satb('C', 'c64', ['Ic', 'V', 'I'])}</div><div>{satb('Am', 'c64', ['ic', 'V', 'i'])}</div></div></LbPic>;
    if (kind === 'pass') return <LbPic h={150}><div style={{width:'100%',maxWidth:560,margin:'0 auto'}}><K4Melody notes={H5_PASS[0].m.map(h3N)} ks={[null, 0]} hi={[1, 3]} labels={h5PassLabels(0)} width={scr ? 300 : 380}/></div></LbPic>;
    if (kind === 'pre') return <LbPic h={160}><div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:12,width:'100%',maxWidth:620,margin:'0 auto'}}>{['iib', 'ivb'].map(o => <div key={o}>{satb('C', o, [h5PreRom('C', o), 'V', 'I'])}</div>)}</div></LbPic>;
    const M = H5_MEL[0], sel = [[1, 0], [5, 0], [4, 0], [1, 0], [4, 0], [1, 2], [5, 0], [1, 0]]; return <LbPic h={150}><div style={{width:'100%',maxWidth:560,margin:'0 auto'}}><K4Melody notes={M.m.map(h3N)} ks={[null, 0]} labels={sel.map(x => h5Rom('C', x[0], x[1]))} width={scr ? 320 : 400}/></div></LbPic>; };
  const TEACH = {
    inv: t('Theory of Music Grade 5 harmony vocabulary: I II IV V VI (II in major keys only), Ib IIb IVb Vb VIb VIIb, and Ic as a cadential 6-4. VIIb is new: the leading-note chord in first inversion, usually between I and Ib (I–VIIb–Ib, the bass rising by step). It doubles its bass (or 5th), never the leading note. The names follow the earlier chapters (small letters for minor chords, ° for the diminished VII); the syllabus prints them all as capitals: use whichever your papers use.', '이론 5급 화성의 어휘: I II IV V VI(II는 장조만), Ib IIb IVb Vb VIb VIIb, 그리고 종지의 6-4인 Ic. VIIb가 새로워요: 이끎음 위 화음의 첫째 자리바꿈, 흔히 I과 Ib 사이(I–VIIb–Ib, 베이스가 한 음씩 올라가요). 베이스(또는 5음)를 겹치고, 이끎음은 겹치지 않아요. 화음 이름은 앞 챕터처럼(단3화음은 소문자, 감3화음 VII는 °); 실라버스는 모두 대문자로 적어요: 쓰시는 시험지를 따르세요.'),
    c64: t('Ic (cadential): the tonic chord with its 5th in the bass, on the strong beat before V, the bass held (or repeated an octave apart). The 6th and 4th above the bass fall to the 5th and 3rd of V; the doubled bass note stays. The progressions here were checked by rule (see the teacher\'s copy).', 'Ic(종지): 으뜸화음의 5음이 베이스, V 앞의 강박에, 베이스는 그대로(또는 옥타브로 반복). 베이스 위의 6도와 4도가 V의 5음과 3음으로 내려가고, 겹친 베이스 음은 그대로. 여기 진행은 규칙으로 확인했어요(선생님용 참고).'),
    pass: t('Unaccented passing and auxiliary notes: a passing note moves by step between two different chord notes; an auxiliary note steps away from a chord note and back to the same note. Both fall on the weak part of the beat. In the app the chords change on the named (strong) notes and the notes between are weak.', '강세 없는 경과음과 보조음: 경과음은 서로 다른 두 화음 음 사이를 한 음씩 움직이고, 보조음은 화음 음에서 한 음 떠났다 같은 음으로 돌아와요. 둘 다 박의 약한 부분에 와요. 앱에서는 이름이 붙은(강박) 음에서 화음이 바뀌고, 그 사이 음은 약박이에요.'),
    pre: t('Cadences preceded by a suitable chord (Grade 5 (b)). Before V: IIb, IV, IVb or Ic in a major key; IV, IVb, VI or Ic in a minor key (II is major keys only). First inversions may be included in cadential progressions. The melodies on the exam may modulate to closely related keys: the same approach chords work in the new key.', '알맞은 화음을 앞에 둔 종지(5급 (b)). V 앞에: 장조에서는 IIb, IV, IVb, Ic; 단조에서는 IV, IVb, VI, Ic(II는 장조만). 종지 진행에 첫째 자리바꿈을 넣어도 돼요. 시험의 선율은 가까운 조로 전조할 수 있어요: 새 조에서도 같은 화음이 통해요.'),
    harm: t('Harmonise a melody of not more than eight bars in four-part vocal style with the Grade 5 vocabulary. The app does the first decision: a chord for each note (any that holds it), the tonic at the start, a cadence at the end, Ic only straight before V, VIIb only before I or Ib. Writing the four parts, and adding passing notes, is on paper with you.', '8마디 이하의 선율에 5급 어휘로 네 성부 화음 붙이기. 앱은 첫 결정을 해요: 음마다 그 음이 든 화음, 시작은 으뜸화음, 끝은 종지, Ic는 바로 V 앞에만, VIIb는 I이나 Ib 앞에만. 네 성부로 적고 경과음을 더하는 건 선생님과 종이에서.'),
  };
  const SAY = { inv: t('Stack in 3rds, name it by its root; vii°b doubles its bass.', '3도로 쌓아 근음으로 이름; vii°b는 베이스를 겹쳐요.'), c64: t('Ic: the same bass as V; the 6th and the 4th fall.', 'Ic: V와 같은 베이스, 6도와 4도가 내려가요.'), pass: t('A step through: passing. A step away and back: auxiliary.', '지나가는 한 음: 경과음. 떠났다 돌아오는 한 음: 보조음.'), pre: t('iib, IV, IVb or Ic, then V–I.', 'iib, IV, IVb, Ic, 그다음 V–I.'), harm: t('A chord that holds each note; Ic–V–I at the end.', '음마다 그 음이 든 화음, 끝은 Ic–V–I.') };
  const PIANO = {
    inv: [t('In C: play I, then vii°b with D in the bass, then Ib: the bass climbs C D E.', 'C에서: I, 그다음 D가 베이스인 vii°b, 그다음 Ib: 베이스가 C D E로 올라가요.'), t('Play every first inversion in G major.', 'G장조의 모든 첫째 자리바꿈을 쳐요.'), t('Name each one by its root.', '하나씩 근음으로 이름을 말해요.')],
    c64: [t('In C: hold G in the bass; play C and E above it, then B and D: Ic–V.', 'C에서: 베이스 G를 누른 채, 위에 C와 E, 그다음 B와 D: Ic–V.'), t('Then resolve to C major: Ic–V–I.', '그다음 C장조로: Ic–V–I.'), t('Try it in G and F.', 'G와 F에서도.')],
    pass: [t('Sing the melody, then play only its strong notes with their chords.', '선율을 부르고, 강박 음만 화음과 함께 쳐요.'), t('Add the weak notes: hear them pass through or step away.', '약박 음을 더해요: 지나가는지 떠났다 오는지 들어 봐요.'), t('Point to each passing and auxiliary note.', '경과음과 보조음을 하나씩 가리켜요.')],
    pre: [t('In C: play iib–V–I, then IV–V–I.', 'C에서: iib–V–I, 그다음 IV–V–I.'), t('Then IVb–V–I and Ic–V–I.', '그다음 IVb–V–I와 Ic–V–I.'), t('Your teacher plays one: which chord came before V?', '선생님이 하나를 치면: V 앞의 화음은?')],
    harm: [t('Sing the melody; mark the notes that could take Ic–V–I.', '선율을 부르고, Ic–V–I가 올 수 있는 음을 표시해요.'), t('Choose a chord for each note.', '음마다 화음을 골라요.'), t('Write the four parts on paper with your teacher.', '선생님과 종이에 네 성부로 적어요.')],
  };
  return [
    <LbPage key="1" no={1} chId={ch} teacher={<>{t('Theory of Music Grade 5 harmony, one step each: vii°b and every first inversion; the cadential 6-4; passing and auxiliary notes; the chord before a cadence; harmonising an eight-note melody. Grade 4\'s chords and cadences are in chapter ' + h4n + '.', '이론 5급 화성을 한 단계씩: vii°b와 모든 첫째 자리바꿈; 종지의 6-4; 경과음과 보조음; 종지 앞의 화음; 여덟 음 선율에 화음 붙이기. 4급의 화음과 종지는 ' + h4n + '장에 있어요.')}</>}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:42,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{bkChapterName(ch)}</div>
      </div></LbOnly>
      {still('c64')}
      <LbSay size={18}>{t('Grade 5 harmony: a new chord on the leading note, the cadential 6-4, notes that pass between the chords, a good chord before the cadence, and eight notes to harmonise.', '5급 화성: 이끎음 위의 새 화음, 종지의 6-4, 화음 사이를 지나가는 음, 종지 앞의 좋은 화음, 그리고 화음을 붙일 여덟 음.')}</LbSay>
      <div className="lb-toc" style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>
        <LbOnly print><div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('In this chapter', '이 챕터에서는')}</div>
          {toc.map(([n, p]) => <div key={p} className="lb-toc-row" style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:14.5,padding:'5px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkGoal(15)}{n}</span><span style={{color:BK.muted,fontWeight:700}}>{p}</span></div>)}
        </div></LbOnly>
        <div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 챕터를 마치면')}</div>
          {checks5.slice(0, 4).map(([, x], i) => <div key={i} style={{display:'flex',alignItems:'flex-start',gap:9,fontSize:14.5,padding:'5px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}>{bkGoal(15)}<span>{x.replace(/^I /, '')}</span></div>)}
        </div>
      </div>
      <LbOnly print><LbDrillStrip id={ch}/></LbOnly>
    </LbPage>,
    ...kinds.map((kind, i) => <LbPage key={kind} no={i + 2} chId={ch} kicker={t('Step ' + (i + 1), (i + 1) + '단계')} title={h5StepT(kind)} teacher={<>{TEACH[kind]}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=' + (i + 1))}>
      <LbLive still={still(kind)} live={<H5Step kind={kind}/>}/>
      <LbSay>{h5NoteT(kind)}</LbSay>
      <LbPiano steps={PIANO[kind].map((x, j) => <React.Fragment key={j}>{x}</React.Fragment>)}/>
      <LbRemember>{SAY[kind]}</LbRemember>
    </LbPage>),
    <LbPage key="7" no={7} chId={ch} kicker={t('Check-up', '점검')} title={t('My five checks', '나의 다섯 가지 확인')}
      teacher={<>{t('On paper and at the piano. For the cadential 6-4 and the chord before the cadence, have the child write one in four parts in a key not practised here.', '종이와 피아노에서. 종지의 6-4와 종지 앞의 화음은 여기서 연습하지 않은 조로 네 성부를 하나씩 적게 해 주세요.')}</>}>
      <LbSay>{t('Tick each one: not yet, nearly, or got it!', '하나씩 표시해요: 아직, 거의, 됐어요!')}</LbSay>
      <LbLive still={<LbStageRows big rows={checks5.map(([a, txt]) => [pen(a), txt])}/>} live={<FiveChecks376 rows={checks5} storeKey="pb_h5_five"/>}/>
    </LbPage>,
  ];
}
function Harmony5LessonBook() { return <>{h5LbPages(false)}</>; }
function H5Learn({ onStart }) {
  const pages = h5LbPages(true), opener = pages[0];
  return (
    <Lesson id="harmony-5" title={bkChapterName('harmony-5')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="harmony-5"><div className="lb-screen lb-open" style={{display:'flex',flexDirection:'column',gap:12,margin:'0 0 8px'}}>{lbWordsFirst(opener.props.children)}</div></BkChapterCtx.Provider></LbScreenCtx.Provider>}>
      {pages.slice(1).map((pg, i) => <Step key={i} title={pg.props.title}><LbScreenPage page={pg}/></Step>)}
    </Lesson>
  );
}
// ── the drill ──
const H5_LEVELS = [
  { n: 1, label: 'vii°b and the first inversions', kind: 'inv', time: 18 },
  { n: 2, label: 'I, Ib or Ic?', kind: 'c64', time: 18 },
  { n: 3, label: 'Passing, auxiliary or chord note?', kind: 'pass', time: 15 },
  { n: 4, label: 'Which chord comes before V?', kind: 'pre', time: 20 },
  { n: 5, label: 'Eight notes: which chord holds it?', kind: 'fit', time: 15 },
];
Object.assign(LEVEL_KO, { 'vii°b and the first inversions': 'vii°b와 첫째 자리바꿈', 'I, Ib or Ic?': 'I? Ib? Ic?', 'Passing, auxiliary or chord note?': '경과음? 보조음? 화음 음?', 'Which chord comes before V?': 'V 앞의 화음은?', 'Eight notes: which chord holds it?': '여덟 음: 그 음이 든 화음은?' });
const genH5Question = (lv, prev) => genH5(lv.kind, prev);
const h5AnswerLabel = (q) => (q.kind === 'fit' ? q.fits.join(' / ') : h5Lab(q, q.answer));
function H5Question({ q, given, locked, onAnswer, pixel }) {
  const done = !!given, play = h5PlayQ(q), cols = q.kind === 'pass' ? 1 : q.choices.length > 3 ? 2 : q.choices.length;
  const btnCls = pixel ? 'pixel-choice' : 'choice-btn', cls = (c) => btnCls + (!done ? '' : h5Ok(q, c) && (c === given.ans || q.kind !== 'fit') ? ' good' : given.ans === c ? ' bad' : '');
  return (<div>
    <p style={pixel ? {fontSize:11.5,textAlign:'center'} : {fontSize:15,fontWeight:700,textAlign:'center',margin:'0 0 8px',color:'var(--muted)',textWrap:'balance'}}>{h5Prompt(q)}</p>
    {h5Fig(q, done)}
    {play && <div style={{textAlign:'center',margin:'6px 0 0'}}><button className={pixel ? 'pixel-btn' : 'ghost-btn'} style={{minHeight:44}} onClick={() => { stopClicks(); play(); }}>{t('▶ Hear it', '▶ 들어 보기')}</button></div>}
    <div style={{display:'grid',gridTemplateColumns:'repeat(' + cols + ',minmax(0,1fr))',gap:8,marginTop:10}}>{q.choices.map(c => <button key={c} disabled={locked} className={cls(c)} style={{padding:'12px 4px',fontSize:q.kind === 'pass' ? 15 : 17,fontWeight:900}} onClick={() => { if (locked || done) return; stopClicks(); onAnswer(c); }}>{h5Lab(q, c)}</button>)}</div>
    {done && !pixel && <div style={{marginTop:10,fontSize:13.5,color:'#4a4d86',background:'#fff',borderRadius:8,padding:'7px 10px',lineHeight:1.45}}>{h5Why(q)}</div>}
  </div>);
}
Object.assign(HARMONY_5_DRILL, { levels: H5_LEVELS, generate: genH5Question, check: (q, ans) => ans !== null && ans !== undefined && h5Ok(q, ans), answerLabel: h5AnswerLabel, Question: H5Question, Learn: H5Learn });
// the teacher's copy: the checked progressions, and every answer from the room's own data
function H5Teacher() {
  const pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="harmony-5" teacher>{content}</WbPage>);
  const row = (k, nm, labs) => h4Name(k) + ' ' + labs.join('–') + ': ' + H5_PROG[k][nm].join(' / ');
  P(<>
    <div style={{fontFamily:LB_SERIF,fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('harmony-5')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 12px',lineHeight:1.5}}>Theory of Music Grade 5, harmony. Chords are listed soprano, alto, tenor, bass. Every progression below was found and checked by rule: complete chords, the leading note never doubled and rising in the soprano, no parallel 5ths or octaves, no augmented or tritone leaps, the 6-4's 6th and 4th falling over a held bass.</div>
    <TcBlock page={2} title="vii°b and the first inversions" answers={<div style={{fontSize:11,color:BK.ink,lineHeight:1.55}}>{tcAns('C MAJOR, FIRST INVERSION: THE BASS', H5_DEGS('C').map(d => h5Rom('C', d, 1) + ': ' + h3Let(h5Chord('C', d, 1).B)))}{['C', 'G', 'F', 'Am', 'Dm'].map(k => <div key={k}>{row(k, 'vii', [h5Rom(k, 1, 0), h5Rom(k, 7, 1), h5Rom(k, 1, 1)])}</div>)}</div>}
      watch="vii°b named ii (its bass is the 2nd degree), or the leading note doubled. Stack in 3rds: B D F, root B."
      say="“Stack in 3rds, name it by its root.”"/>
    <TcBlock page={3} title="The cadential 6-4" answers={<div style={{fontSize:11,color:BK.ink,lineHeight:1.55}}>{H5_PKEYS.map(k => <div key={k}>{row(k, 'c64', [h5Rom(k, 1, 2), 'V', h5Rom(k, 1, 0)])}</div>)}</div>}
      watch="Ic on a weak beat, or its 6th and 4th moving anywhere but down a step. The bass stays."
      say="“Ic: the same bass as V; the 6th and the 4th fall.”"/>
  </>);
  P(<>
    <TcBlock page={4} title="Passing and auxiliary notes" answers={<>{tcAns('THE MELODIES (strong notes with their chords; the weak notes classed)', H5_PASS.map((M, i) => h4Name(M.k) + ': ' + M.m.map((x, j) => h3Let(h3N(x)) + (j % 2 === 0 ? '(' + h5Rom(M.k, M.c[j / 2], 0) + ')' : '[' + ({ chord: 'chord', pass: 'p', aux: 'a' })[h5PassKind(i, j)] + ']')).join(' ')), null)}</>}
      watch="Every non-chord note called a passing note: an auxiliary comes back to the same note."
      say="“A step through: passing. A step away and back: auxiliary.”"/>
    <TcBlock page={5} title="The chord before the cadence" answers={<div style={{fontSize:11,color:BK.ink,lineHeight:1.55}}>{['C', 'G', 'F', 'Am', 'Dm'].flatMap(k => h5PreOpts(k).filter(o => o !== 'c64').map(o => <div key={k + o}>{row(k, o, [h5PreRom(k, o), 'V', h5Rom(k, 1, 0)])}</div>))}</div>}
      watch="Parallel 5ths from IV to V: the upper voices move against the bass. Before V in a minor key, VI doubles its 3rd."
      say="“iib, IV, IVb or Ic, then V–I.”"/>
    <TcBlock page={6} title="Harmonise eight notes" answers={<>{tcAns('EVERY ROOT-POSITION CHORD THAT HOLDS EACH NOTE', H5_MEL.map(M => h4Name(M.k) + ': ' + M.m.map(x => { const n = h3N(x); return h3Let(n) + ' (' + H4_DEGS(M.k).filter(d => h4Has(M.k, d, n)).map(d => h5Rom(M.k, d, 0)).join(', ') + ')'; }).join(' ')), null)}{tcAns('ONE WAY, C MAJOR', ['I V IV I IV Ic V I'], null)}</>}
      watch="A cadence without a good chord before it, or Ic that does not go to V."
      say="“A chord that holds each note; Ic–V–I at the end.”"/>
    <TcBlock page={7} title="The check-up" answers={<div style={{fontSize:12,color:BK.ink,lineHeight:1.5}}>Each one on paper and at the piano, in keys the child has not just practised: one vii°b between I and Ib, one Ic–V–I, one cadence with a chord before it, and a short melody harmonised in four parts with a passing note.</div>}/>
  </>);
  return <>{pages}</>;
}
TEACHER_COPIES['harmony-5'] = H5Teacher;
'''
prog = {k: {nm: v for nm, v in PROG[k].items()} for k in PROG}
CH = CH.replace('__PROG__', json.dumps(prog, ensure_ascii=False, separators=(',', ':')))
rep("""TEACHER_COPIES['harmony-4'] = H4Teacher;""", """TEACHER_COPIES['harmony-4'] = H4Teacher;""" + CH)

HOME = r'''
// ══ Build BC: Chords and Cadences, Grade 5 on the Home (Chords, after Grade 4) ══
LBH_FN['harmony-5'] = (s) => h5LbPages(s);
const h5HomeQ = (kind) => (n, prev) => { const q = genH5(kind, prev), p = h5Prompt(q), w = h5Why(q);
  return { kind: 'choice', cols: q.kind === 'pass' ? 1 : q.choices.length > 3 ? 2 : q.choices.length, key: q.key, prompt: [p, p], opts: q.choices.map(c => ({ id: c, label: () => h5Lab(q, c) })), ans: q.answer, ok: (v) => h5Ok(q, v),
    play: h5PlayQ(q), fig: (c) => ({ mid: h5Fig(q, !!c.res) }), yes: ['Yes. ' + w, '맞아요. ' + w], no: [w, w] }; };
const h5HomeAdd = (id, i, en, ko, benEn, bko, make) => lbhAdd(id, 'p-chords', 'pitch', en, ko, benEn, bko, lbhSpec('harmony-5', i, { make }));
h5HomeAdd('h5-inv', 1, 'vii°b and the first inversions', 'vii°b와 첫째 자리바꿈', 'Every first inversion, and the chord on the leading note.', '모든 첫째 자리바꿈, 그리고 이끎음 위의 화음.', h5HomeQ('inv'));
h5HomeAdd('h5-c64', 2, 'The cadential 6-4', '종지의 6-4', 'Ic: the same bass as V; the 6th and 4th fall.', 'Ic: V와 같은 베이스, 6도와 4도가 내려가요.', h5HomeQ('c64'));
h5HomeAdd('h5-pass', 3, 'Passing and auxiliary notes', '경과음과 보조음', 'A step through, or a step away and back.', '지나가는 한 음, 떠났다 돌아오는 한 음.', h5HomeQ('pass'));
h5HomeAdd('h5-pre', 4, 'The chord before the cadence', '종지 앞의 화음', 'iib, IV, IVb or Ic, then V–I.', 'iib, IV, IVb, Ic, 그다음 V–I.', h5HomeQ('pre'));
h5HomeAdd('h5-harm', 5, 'Harmonise eight notes', '여덟 음에 화음 붙이기', 'A chord for each note, Ic–V–I at the end.', '음마다 화음, 끝은 Ic–V–I.', lwTapQ(H5HarmPad, (n) => ({ fixed: n % H5_MEL.length }), ['Choose a chord for every note, then check.', '음마다 화음을 고르고, 확인해요.'], ['It works ✓', '좋아요 ✓']));
'''
after_line("h4HomeAdd('h4-fit', 4,", HOME)
rep("""    { id: 'ch-4', en: 'Chords and cadences, Grade 4', ko: '화음과 종지, Grade 4', lessons: ['h4-deg', 'h4-inv', 'h4-cad', 'h4-fit'], check: 'harmony-4' },   // Build AU""",
    """    { id: 'ch-4', en: 'Chords and cadences, Grade 4', ko: '화음과 종지, Grade 4', lessons: ['h4-deg', 'h4-inv', 'h4-cad', 'h4-fit'], check: 'harmony-4' },   // Build AU
    { id: 'ch-5', en: 'Chords and cadences, Grade 5', ko: '화음과 종지, Grade 5', lessons: ['h5-inv', 'h5-c64', 'h5-pass', 'h5-pre', 'h5-harm'], check: 'harmony-5' },   // Build BC""")
import re
m = re.findall(r"  set\('4', 'h4-[^']*'\);[^\n]*", s); assert len(m) == 1, m
s = s.replace(m[0], m[0] + "\n  set('5', 'h5-inv h5-c64 h5-pass h5-pre h5-harm');   // Build BC: Chords and Cadences, Grade 5")
rep("""const LESSON_BOOKS = { 'keys-5': Keys5LessonBook,""", """const LESSON_BOOKS = { 'harmony-5': Harmony5LessonBook, 'keys-5': Keys5LessonBook,""")
rep("""const LB_PAGE_FNS = { 'keys-5': k5LbPages,""", """const LB_PAGE_FNS = { 'harmony-5': h5LbPages, 'keys-5': k5LbPages,""")
rep("""const HOUSE_ICONS = {""", """const HOUSE_ICONS = {"harmony-5": "<ellipse cx=\\"14\\" cy=\\"35\\" rx=\\"5.5\\" ry=\\"4\\" transform=\\"rotate(-20 14 35)\\" fill=\\"#26296b\\"/><ellipse cx=\\"14\\" cy=\\"27\\" rx=\\"5.5\\" ry=\\"4\\" transform=\\"rotate(-20 14 27)\\" fill=\\"#26296b\\"/><ellipse cx=\\"14\\" cy=\\"19\\" rx=\\"5.5\\" ry=\\"4\\" transform=\\"rotate(-20 14 19)\\" fill=\\"#26296b\\"/><text x=\\"24\\" y=\\"24\\" font-size=\\"12\\" font-weight=\\"900\\" fill=\\"#e4572e\\" stroke=\\"none\\" font-family=\\"Inter, sans-serif\\">6</text><text x=\\"24\\" y=\\"37\\" font-size=\\"12\\" font-weight=\\"900\\" fill=\\"#e4572e\\" stroke=\\"none\\" font-family=\\"Inter, sans-serif\\">4</text>", """)

# Grade 4 harmony, found while checking: the four cadences overflowed their picture on the printed pages 1 and 4 (two rows of two
# staves); in print they now stand in one row of four. And the chapter title no longer breaks before its grade number.
rep("""    if (kind === 'cad') return <LbPic h={170}><div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:10,width:'100%',maxWidth:680,margin:'0 auto'}}>{H4_CADS.map(c =>""",
    """    if (kind === 'cad') return <LbPic h={170}><div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : 'repeat(4,minmax(0,1fr))',gap:8,width:'100%',maxWidth:720,margin:'0 auto'}}>{H4_CADS.map(c =>""")
rep("""        <div style={{fontFamily:LB_SERIF,fontSize:48,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{bkChapterName(ch)}</div>
      </div></LbOnly>
      {still('cad')}""", """        <div style={{fontFamily:LB_SERIF,fontSize:42,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{bkChapterName(ch)}</div>
      </div></LbOnly>
      {still('cad')}""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
