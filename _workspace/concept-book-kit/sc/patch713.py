import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build AT (board call 18, the third Grade 4 room): Keys and Intervals, Grade 4. Theory of Music Grade 4 (Manual of Syllabuses
# 2026, read 26 Oct): the scales and key signatures of B, F sharp, D flat and G flat major and B, F sharp, C sharp, F and B flat
# minor (harmonic form); double sharps and flats; tones and semitones; all diatonic intervals above or below the tonic in these keys,
# treble or bass, and their inversion; modulation in melodies to the dominant or the relative major or minor; general knowledge:
# diatonic and chromatic, as applied to semitones and scales. Double sharps and flats already have their own lesson (Accidentals:
# 'Double sharp, double flat'): it moves to the Grade 4 floor, as board call 19 recommended, with the tritone and the diminished and
# augmented triads going to Grade 5 (Theory of Music: chromatic intervals at Grade 5). The modulation clues are the usual textbook
# ones (the new key's leading note; for a minor key's relative major, the raised 7th cancelled): flagged on the board.
# Transposition (Theory of Music Grade 4: a short melody into another of the grade's keys, accidentals involved) is step 6.

rep("""const SCALES_4_DRILL = { id: 'scales-4', label: 'Scales and Arpeggios, Grade 4' };   // Build AS""",
    """const SCALES_4_DRILL = { id: 'scales-4', label: 'Scales and Arpeggios, Grade 4' };   // Build AS
const KEYS_4_DRILL = { id: 'keys-4', label: 'Keys and Intervals, Grade 4' };   // Build AT""")
rep("""  { id: 'scales-4', label: 'Scales and Arpeggios, Grade 4', concept: SCALES_4_DRILL, track: 'start' },   // Build AS""",
    """  { id: 'scales-4', label: 'Scales and Arpeggios, Grade 4', concept: SCALES_4_DRILL, track: 'start' },   // Build AS
  { id: 'keys-4', label: 'Keys and Intervals, Grade 4', concept: KEYS_4_DRILL, track: 'start' },   // Build AT""")
rep("""'scales-4': '스케일과 아르페지오, Grade 4'""", """'scales-4': '스케일과 아르페지오, Grade 4', 'keys-4': '조와 음정, Grade 4'""")
rep("""'scales-4': ['scales-23'],""", """'scales-4': ['scales-23'], 'keys-4': ['key-signatures', 'harmony-23'],""")
rep("""'scales-4': ['Scales, Grade 4', '스케일 4'],""", """'scales-4': ['Scales, Grade 4', '스케일 4'], 'keys-4': ['Keys, Grade 4', '조 4'],""")
rep("""  'scales-4': 'scales arpeggios grade 4""", """  'keys-4': 'keys intervals grade 4 theory key signature five six sharps flats harmonic minor raised seventh e sharp b sharp diatonic chromatic semitone below the tonic inversion modulation dominant relative',
  'scales-4': 'scales arpeggios grade 4""")
rep("""'scales-4': 'k-play', 'harmony-23'""", """'scales-4': 'k-play', 'keys-4': 'p-scales', 'harmony-23'""")
rep("""    { id: 'psc-minor', en: 'Minor scales', ko: '단음계', lessons: ['ms-third', 'ms-rel', 'ms-har', 'ms-gaps', 'ms-ear', 'sc-min'], check: 'minor-scales' },""",
    """    { id: 'psc-minor', en: 'Minor scales', ko: '단음계', lessons: ['ms-third', 'ms-rel', 'ms-har', 'ms-gaps', 'ms-ear', 'sc-min'], check: 'minor-scales' },
    { id: 'psc-4', en: 'Keys and intervals, Grade 4', ko: '조와 음정, Grade 4', lessons: ['k4-sig', 'k4-lead', 'k4-semi', 'k4-below', 'k4-mod', 'k4-tr'], check: 'keys-4' },   // Build AT""")
rep("""  set('4', 's4-four s4-touch s4-mirror s4-chrom s4-arp');   // Build AS: Scales and Arpeggios, Grade 4""",
    """  set('4', 's4-four s4-touch s4-mirror s4-chrom s4-arp');   // Build AS: Scales and Arpeggios, Grade 4
  set('4', 'k4-sig k4-lead k4-semi k4-below k4-mod k4-tr');   // Build AT: Keys and Intervals, Grade 4""")
# board call 19: double sharps and flats at Grade 4; the tritone and the diminished and augmented triads at Grade 5
rep("""  set('4', 'iv-invert iv-tritone ch-da ch-seven md-family md-ladder');""", """  set('4', 'iv-invert ch-seven md-family md-ladder ac-double');   // Build AT (call 19): double sharps and flats are Grade 4 theory""")
rep("""  set('5', 'ac-double sc-all kf-piece ch-7th md-parent md-keys');""", """  set('5', 'iv-tritone ch-da sc-all kf-piece ch-7th md-parent md-keys');   // Build AT (call 19): chromatic intervals are Grade 5""")

CH = r'''
// ─── Chapter: Keys and Intervals, Grade 4 (Build AT, 2026-10-26; board call 18, the third Grade 4 room) ───
// The Grade 4 keys by their signatures; the raised 7th of the Grade 4 minor keys (A♯, E♯, B♯, E♮, A♮); diatonic and chromatic
// semitones; intervals above or below the tonic, and inversion; modulation in a melody, to the dominant or the relative.
const K4 = {   // the Grade 4 keys: tr / bs = the lower tonic on the treble / bass staff; ks = the key signature
  B: { en: 'B major', ko: 'B장조', ks: ['sharp', 5], tr: 'B3', bs: 'B2' },
  Fs: { en: 'F♯ major', ko: 'F♯장조', ks: ['sharp', 6], tr: 'F#4', bs: 'F#2' },
  Db: { en: 'D♭ major', ko: 'D♭장조', ks: ['flat', 5], tr: 'Db4', bs: 'Db3' },
  Gb: { en: 'G♭ major', ko: 'G♭장조', ks: ['flat', 6], tr: 'Gb4', bs: 'Gb2' },
  Bm: { en: 'B minor', ko: 'B단조', ks: ['sharp', 2], tr: 'B3', bs: 'B2', minor: true },
  Fsm: { en: 'F♯ minor', ko: 'F♯단조', ks: ['sharp', 3], tr: 'F#4', bs: 'F#2', minor: true },
  Csm: { en: 'C♯ minor', ko: 'C♯단조', ks: ['sharp', 4], tr: 'C#4', bs: 'C#3', minor: true },
  Fm: { en: 'F minor', ko: 'F단조', ks: ['flat', 4], tr: 'F4', bs: 'F2', minor: true },
  Bbm: { en: 'B♭ minor', ko: 'B♭단조', ks: ['flat', 5], tr: 'Bb3', bs: 'Bb2', minor: true },
};
const K4_IDS = ['B', 'Fs', 'Db', 'Gb', 'Bm', 'Fsm', 'Csm', 'Fm', 'Bbm'], K4_MIN = ['Bm', 'Fsm', 'Csm', 'Fm', 'Bbm'];
const k4Name = (k) => t(K4[k].en, K4[k].ko);
const k4Sig = (k) => { const [ty, n] = K4[k].ks, out = {}; (ty === 'sharp' ? SHARP_ORDER : FLAT_ORDER).slice(0, n).forEach(a => { out[a[0]] = ty === 'sharp' ? 1 : -1; }); return out; };
// the note x scale steps above the lower tonic (harmonic minor: the 7th raised a semitone)
const k4Note = (k, clef, x) => { const c = K4[k], t0 = h3N(clef === 'bass' ? c.bs : c.tr), d = t0.d + x, L = H3_L[((d % 7) + 7) % 7]; let a = k4Sig(k)[L] || 0; if (c.minor && ((x % 7) + 7) % 7 === 6) a += 1; return { d, acc: a }; };
const K4_QT = { 2: { 1: 'm', 2: 'M' }, 3: { 3: 'm', 4: 'M' }, 4: { 5: 'P' }, 5: { 7: 'P' }, 6: { 8: 'm', 9: 'M' }, 7: { 10: 'm', 11: 'M' }, 8: { 12: 'P' } };
const k4Iv = (lo, hi) => { const n = hi.d - lo.d + 1, s = ivMidi(hi) - ivMidi(lo); return (K4_QT[n] && K4_QT[n][s]) + n; };   // 'm2' ... 'P8'
const k4IvName = (id) => h3IvName(id[0], Number(id.slice(1)));
const k4Inv = (id) => ({ M: 'm', m: 'M', P: 'P' })[id[0]] + (9 - Number(id.slice(1)));
// the key-signature names, by the number of sharps or flats
const K4_MAJ = { sharp: ['C', 'G', 'D', 'A', 'E', 'B', 'F♯', 'C♯'], flat: ['C', 'F', 'B♭', 'E♭', 'A♭', 'D♭', 'G♭', 'C♭'] }, K4_MINS = { sharp: ['A', 'E', 'B', 'F♯', 'C♯', 'G♯', 'D♯', 'A♯'], flat: ['A', 'D', 'G', 'C', 'F', 'B♭', 'E♭', 'A♭'] };
const k4KeyLab = (id) => (id.endsWith('m') ? t(id.slice(0, -1) + ' minor', id.slice(0, -1) + '단조') : t(id + ' major', id + '장조'));
// the raised 7th of the Grade 4 minor keys: the key (semitones from middle C for the keyboard), the written name, two near misses
const K4_LEAD = {
  Bm: { r: -1, lead: 'A♯', alts: ['B♭', 'A'], why: ['A♯: the key signature gives A; the raised 7th is A♯ (a black key, written as a kind of A).', 'A♯: 조표로는 A, 올린 7도는 A♯(검은건반이지만 A의 한 종류로 적어요).'] },
  Fsm: { r: 6, lead: 'E♯', alts: ['F', 'E'], why: ['E♯ is the white key F. It is written E♯, not F: a scale uses each letter once, and the 7th of F♯ minor is a kind of E.', 'E♯는 흰건반 F예요. F가 아니라 E♯로 적어요: 음계는 글자를 한 번씩 쓰고, F♯단조의 7도는 E의 한 종류니까요.'] },
  Csm: { r: 1, lead: 'B♯', alts: ['C', 'B'], why: ['B♯ is the white key C. It is written B♯, not C: the 7th of C♯ minor is a kind of B.', 'B♯는 흰건반 C예요. C가 아니라 B♯로 적어요: C♯단조의 7도는 B의 한 종류니까요.'] },
  Fm: { r: 5, lead: 'E♮', alts: ['E♭', 'F♭'], why: ['The key signature makes it E♭; the raised 7th needs a natural: E♮.', '조표로는 E♭, 올린 7도는 제자리표가 필요해요: E♮.'] },
  Bbm: { r: -2, lead: 'A♮', alts: ['A♭', 'G♯'], why: ['The key signature makes it A♭; the raised 7th needs a natural: A♮.', '조표로는 A♭, 올린 7도는 제자리표가 필요해요: A♮.'] },
};
// diatonic and chromatic semitones: next-door keys; different letters, or the same letter
const K4_SEMI = [['C4', 'C#4'], ['C4', 'Db4'], ['E4', 'F4'], ['F4', 'F#4'], ['B4', 'C5'], ['Gb4', 'G4'], ['E#4', 'F#4'], ['A4', 'A#4'], ['D#4', 'E4'], ['Bb4', 'B4'], ['G#4', 'A4'], ['Db5', 'D5']];
const k4SemiKind = (i) => (K4_SEMI[i][0][0] === K4_SEMI[i][1][0] ? 'chr' : 'dia');
// modulation: short melodies (each note one beat) that leave the home key for its dominant or its relative; clue = the note that
// tells (the new key's leading note; for a minor key's relative major, the raised 7th cancelled)
const K4_MOD = [
  { h: 'C', ks: [null, 0], dom: 'G', rel: 'Am', m: ['E4', 'G4', 'C5', 'B4', 'A4', 'F#4', 'A4', 'G4'], to: 'dom', clue: 5 },
  { h: 'C', ks: [null, 0], dom: 'G', rel: 'Am', m: ['G4', 'E4', 'C5', 'B4', 'A4', 'G#4', 'B4', 'A4'], to: 'rel', clue: 5 },
  { h: 'G', ks: ['sharp', 1], dom: 'D', rel: 'Em', m: ['B4', 'D5', 'G5', 'F#5', 'E5', 'C#5', 'E5', 'D5'], to: 'dom', clue: 5 },
  { h: 'G', ks: ['sharp', 1], dom: 'D', rel: 'Em', m: ['B4', 'D5', 'G5', 'F#5', 'E5', 'D#5', 'F#5', 'E5'], to: 'rel', clue: 5 },
  { h: 'F', ks: ['flat', 1], dom: 'C', rel: 'Dm', m: ['A4', 'C5', 'F5', 'E5', 'D5', 'B4', 'D5', 'C5'], to: 'dom', clue: 5 },
  { h: 'F', ks: ['flat', 1], dom: 'C', rel: 'Dm', m: ['A4', 'C5', 'F5', 'E5', 'D5', 'C#5', 'E5', 'D5'], to: 'rel', clue: 5 },
  { h: 'Am', ks: [null, 0], dom: 'Em', rel: 'C', m: ['A4', 'G#4', 'A4', 'C5', 'E5', 'D5', 'G4', 'C5'], to: 'rel', clue: 6 },
  { h: 'Am', ks: [null, 0], dom: 'Em', rel: 'C', m: ['A4', 'C5', 'E5', 'G#4', 'A4', 'B4', 'D#5', 'E5'], to: 'dom', clue: 6 },
  { h: 'Dm', ks: ['flat', 1], dom: 'Am', rel: 'F', m: ['D5', 'C#5', 'D5', 'F5', 'A5', 'G5', 'C5', 'F5'], to: 'rel', clue: 6 },
  { h: 'Dm', ks: ['flat', 1], dom: 'Am', rel: 'F', m: ['D5', 'F5', 'E5', 'C5', 'A4', 'G#4', 'C5', 'A4'], to: 'dom', clue: 5 },
];
const k4ModNotes = (i) => K4_MOD[i].m.map(h3N);
const k4ModWhy = (i) => { const c = K4_MOD[i], nt = k4ModNotes(i)[c.clue], nm = h3Let(nt) === h3Let({ d: nt.d, acc: 0 }) && nt.acc === 0 ? h3Let(nt) + '♮' : h3Let(nt), dest = c[c.to], last = h3Let(k4ModNotes(i)[c.m.length - 1]);
  if (c.h.endsWith('m') && c.to === 'rel') return t(nm + ': the raised 7th is cancelled, and the tune comes to rest on ' + last + ': ' + k4KeyLab(dest) + ', the relative major.', nm + ': 올린 7도가 제자리로 돌아오고, 선율은 ' + last + '에서 쉬어요: 나란한조 ' + k4KeyLab(dest) + '.');
  return t(nm + ' is the leading note of ' + k4KeyLab(dest) + ', and the tune comes to rest on ' + last + ': ' + (c.to === 'dom' ? 'the dominant.' : 'the relative ' + (c.h.endsWith('m') ? 'major.' : 'minor.')), nm + '은 ' + k4KeyLab(dest) + '의 이끎음이고, 선율은 ' + last + '에서 쉬어요: ' + (c.to === 'dom' ? '딸림조.' : '나란한조.')); };
// transposition: each note is [scale steps from the tonic, alteration against the key signature], so a melody moves to any key
const K4_TRK = { C: ['C4', [null, 0], 'C major', 'C장조'], D: ['D4', ['sharp', 2], 'D major', 'D장조'], G: ['G4', ['sharp', 1], 'G major', 'G장조'], F: ['F4', ['flat', 1], 'F major', 'F장조'], Db: ['Db4', ['flat', 5], 'D♭ major', 'D♭장조'],
  Am: ['A4', [null, 0], 'A minor', 'A단조'], Em: ['E4', ['sharp', 1], 'E minor', 'E단조'], D2: ['D4', ['sharp', 2], 'D major', 'D장조'], B: ['B4', ['sharp', 5], 'B major', 'B장조'] };
const K4_TR = [
  { from: 'C', to: 'D', m: [[4, 0], [5, 0], [3, 1], [4, 0], [2, 0], [0, 0]] },
  { from: 'G', to: 'F', m: [[0, 0], [4, 0], [3, 1], [4, 0], [2, 0], [1, 0], [0, 0]] },
  { from: 'F', to: 'Db', m: [[0, 0], [2, 0], [4, 0], [3, 1], [4, 0], [5, 0], [4, 0]] },
  { from: 'Am', to: 'Em', m: [[0, 0], [2, 0], [1, 0], [-1, 1], [0, 0], [4, 0], [2, 0], [0, 0]] },
  { from: 'D2', to: 'B', m: [[2, 0], [1, 0], [0, 0], [-1, 0], [0, 0], [3, 1], [4, 0]] },
];
const k4TrNotes = (key, m, o = {}) => { const [ts, ks] = K4_TRK[key], t0 = h3N(ts), sig = {}; if (ks[0]) (ks[0] === 'sharp' ? SHARP_ORDER : FLAT_ORDER).slice(0, ks[1]).forEach(a => { sig[a[0]] = ks[0] === 'sharp' ? 1 : -1; });
  return m.map(([st, alt]) => { const d = t0.d + st + (o.shift || 0), L = H3_L[((d % 7) + 7) % 7]; return { d, acc: (sig[L] || 0) + (o.miss ? 0 : alt) }; }); };
const k4TrName = (key) => t(K4_TRK[key][2], K4_TRK[key][3]);
const k4TrVer = (i, c) => k4TrNotes(K4_TR[i].to, K4_TR[i].m, c === 'miss' ? { miss: true } : c === 'shift' ? { shift: 1 } : {});
const k4TrMel = (i, c, w) => <K4Melody notes={c === 'from' ? k4TrNotes(K4_TR[i].from, K4_TR[i].m) : k4TrVer(i, c)} ks={K4_TRK[c === 'from' ? K4_TR[i].from : K4_TR[i].to][1]} width={w || 300}/>;
const k4ModPlay = (i) => { const ns = k4ModNotes(i); return spPlay(ns.map((n, j) => ({ at: j * 0.9, keys: [h3Semi(n)], len: j === ns.length - 1 ? 2 : 0.85, vol: 0.15 })), 84); };

// one treble staff with a key signature: accidentals drawn the way a bar shows them (against the key, and against an earlier note)
function K4Melody({ notes, ks = [null, 0], hi = [], width = 320, labels = null }) {
  const n = notes.length, ksN = ks[0] ? ks[1] : 0, x0 = 46 + ksN * 10, xOf = (i) => x0 + 20 + i * ((width - x0 - 40) / Math.max(1, n - 1));
  const sig = ks[0] ? (ks[0] === 'sharp' ? SHARP_ORDER : FLAT_ORDER).slice(0, ksN) : [], cur = {}; sig.forEach(a => { cur[a[0]] = ks[0] === 'sharp' ? 1 : -1; });
  const ys = [dY(38) - 10, dY(30) + 10, ...clefInkYs('treble', dY, 'treble')]; notes.forEach(nt => ys.push(dY(nt.d) - 36, dY(nt.d) + 36)); const yTop = Math.min(...ys), yBot = Math.max(...ys) + (labels ? 16 : 0);
  const marks = notes.map(nt => { const L = H3_L[((nt.d % 7) + 7) % 7], show = (cur[L] || 0) !== nt.acc; cur[L] = nt.acc; return show; });
  return <svg viewBox={`0 ${yTop} ${width} ${yBot - yTop}`} style={{width:'100%',maxWidth:width * 1.5,display:'block',margin:'0 auto'}} role="img" aria-label={t('A melody', '선율')}>
    {CLEFS.treble.lines.map(l => <line key={l} x1="4" x2={width - 4} y1={dY(l)} y2={dY(l)} stroke={BK.ink} strokeOpacity="0.55" strokeWidth="1.2"/>)}
    <ClefGlyph clef="treble" st="treble" yOf={(d) => dY(d)} ink={BK.ink}/>
    {sig.map((a, j) => { const y = dY(30 + (ks[0] === 'sharp' ? SHARP_POS : FLAT_POS)[a]), x = 46 + j * 10; return ks[0] === 'sharp' ? <SharpShape key={a} x={x} y={y} color={BK.ink}/> : <FlatShape key={a} x={x} y={y} color={BK.ink}/>; })}
    {notes.map((nt, i) => { const x = xOf(i), y = dY(nt.d), col = hi.includes(i) ? BK.coral : BK.ink, up = nt.d < 34;
      return <g key={i}>{ledgersFor(nt.d, 30, 38).map(p => <line key={p} x1={x - 11} x2={x + 11} y1={dY(p)} y2={dY(p)} stroke={BK.ink} strokeWidth="1.3"/>)}
        {marks[i] && (nt.acc > 0 ? <SharpShape x={x - 16} y={y} color={col}/> : nt.acc < 0 ? <FlatShape x={x - 15} y={y} color={col}/> : <NaturalShape x={x - 15} y={y} color={col}/>)}
        <ellipse cx={x} cy={y} rx="6.6" ry="4.8" transform={`rotate(-20 ${x} ${y})`} fill={col}/>
        <line x1={up ? x + 6 : x - 6} x2={up ? x + 6 : x - 6} y1={y} y2={y + (up ? -30 : 30)} stroke={col} strokeWidth="1.6"/>
        {labels && labels[i] && <text x={x} y={yBot - 3} textAnchor="middle" fontSize="11" fontWeight="900" fill={col} fontFamily="Inter, sans-serif">{labels[i]}</text>}</g>; })}
    <line x1={width - 10} x2={width - 10} y1={dY(38)} y2={dY(30)} stroke={BK.ink} strokeWidth="1.3"/><line x1={width - 5} x2={width - 5} y1={dY(38)} y2={dY(30)} stroke={BK.ink} strokeWidth="3.2"/>
  </svg>;
}

// ── the questions (the steps, the drill and the Home share them) ──
const K4_SIGQ = [['sharp', 5, false], ['sharp', 6, false], ['flat', 5, false], ['flat', 6, false], ['sharp', 2, true], ['sharp', 3, true], ['sharp', 4, true], ['flat', 4, true], ['flat', 5, true]];
const k4SigId = (ty, n, minor) => (minor ? K4_MINS[ty][n] + 'm' : K4_MAJ[ty][n]);
function genK4(kind, prev, fixed) {
  const uid = Math.random(), again = (key) => prev && prev.key === key;
  if (kind === 'sig') { let i, clef, g = 0; do { i = fixed != null ? fixed : Math.floor(Math.random() * K4_SIGQ.length); clef = Math.random() < 0.7 ? 'treble' : 'bass'; } while (fixed == null && again('s' + i) && g++ < 10);
    const [ty, n, minor] = K4_SIGQ[i], ans = k4SigId(ty, n, minor), ch = [ans, k4SigId(ty, n - 1, minor), k4SigId(ty, Math.min(7, n + 1), minor), k4SigId(ty, n, !minor)];
    return { kind, i, ty, n, minor, clef, answer: ans, choices: shuffle([...new Set(ch)]), key: 's' + i, uid }; }
  if (kind === 'lead') { let k, g = 0; do { k = fixed || pick(K4_MIN); } while (!fixed && again('l' + k) && g++ < 10); const c = K4_LEAD[k]; return { kind, k, answer: c.lead, choices: shuffle([c.lead, ...c.alts]), key: 'l' + k, uid }; }
  if (kind === 'semi') { let i, g = 0; do { i = fixed != null ? fixed : Math.floor(Math.random() * K4_SEMI.length); } while (fixed == null && again('e' + i) && g++ < 10); return { kind, i, answer: k4SemiKind(i), choices: ['dia', 'chr'], key: 'e' + i, uid }; }
  if (kind === 'iv') { let k, clef, dir, x, g = 0; do { k = fixed ? fixed.k : pick(K4_IDS); clef = fixed ? fixed.clef : Math.random() < 0.6 ? 'treble' : 'bass'; dir = fixed ? fixed.dir : Math.random() < 0.5 ? 'up' : 'down'; x = fixed ? fixed.x : 1 + Math.floor(Math.random() * 7); } while (!fixed && again(k + clef + dir + x) && g++ < 10);
    const ns = dir === 'up' ? [k4Note(k, clef, 0), k4Note(k, clef, x)] : [k4Note(k, clef, x - 1), k4Note(k, clef, 7)], ans = k4Iv(ns[0], ns[1]);
    const ch = ans[0] === 'P' ? { P4: ['P4', 'P5', 'M3'], P5: ['P5', 'P4', 'M6'], P8: ['P8', 'M7', 'P5'] }[ans] : [ans, ({ M: 'm', m: 'M' })[ans[0]] + ans.slice(1), k4Inv(ans)];   // the near misses: the other quality, and the inversion
    return { kind, k, clef, dir, x, ns, answer: ans, choices: shuffle(ch), key: k + clef + dir + x, uid }; }
  if (kind === 'tr') { let i, g = 0; do { i = fixed != null ? fixed : Math.floor(Math.random() * K4_TR.length); } while (fixed == null && again('t' + i) && g++ < 10); return { kind, i, answer: 'ok', choices: shuffle(['ok', 'miss', 'shift']), key: 't' + i, uid }; }
  let i, g = 0; do { i = fixed != null ? fixed : Math.floor(Math.random() * K4_MOD.length); } while (fixed == null && again('m' + i) && g++ < 10); return { kind: 'mod', i, answer: K4_MOD[i].to, choices: ['dom', 'rel'], key: 'm' + i, uid };
}
function k4Lab(q, c) {
  if (q.kind === 'sig') return k4KeyLab(c);
  if (q.kind === 'lead') return c;
  if (q.kind === 'semi') return c === 'dia' ? t('Diatonic semitone', '온음계적 반음') : t('Chromatic semitone', '반음계적 반음');
  if (q.kind === 'iv') return k4IvName(c);
  if (q.kind === 'tr') return <div style={{width:'100%',minWidth:0}}>{k4TrMel(q.i, c)}</div>;
  const m = K4_MOD[q.i]; return c === 'dom' ? t(k4KeyLab(m.dom) + ' (the dominant)', k4KeyLab(m.dom) + ' (딸림조)') : t(k4KeyLab(m.rel) + ' (the relative ' + (m.h.endsWith('m') ? 'major' : 'minor') + ')', k4KeyLab(m.rel) + ' (나란한조)');
}
function k4Prompt(q) {
  if (q.kind === 'sig') return q.minor ? t('This key signature, a minor key: which one?', '이 조표의 단조는?') : t('This key signature, a major key: which one?', '이 조표의 장조는?');
  if (q.kind === 'lead') return t(k4Name(q.k) + ', harmonic: the coral key is the raised 7th. How is it written?', k4Name(q.k) + ', 화성 단음계: 빨간 건반이 올린 7도. 어떻게 적을까요?');
  if (q.kind === 'semi') return t('A semitone: diatonic or chromatic?', '반음: 온음계적일까, 반음계적일까?');
  if (q.kind === 'iv') return q.dir === 'up' ? t(k4Name(q.k) + ': the tonic and a note above it. Name the interval.', k4Name(q.k) + ': 으뜸음과 그 위의 음. 음정 이름은?') : t(k4Name(q.k) + ': the tonic and a note below it. Name the interval.', k4Name(q.k) + ': 으뜸음과 그 아래의 음. 음정 이름은?');
  if (q.kind === 'tr') return t('Transpose this melody from ' + K4_TRK[K4_TR[q.i].from][2] + ' to ' + K4_TRK[K4_TR[q.i].to][2] + ': which version is right?', '이 선율을 ' + K4_TRK[K4_TR[q.i].from][3] + '에서 ' + K4_TRK[K4_TR[q.i].to][3] + '로 옮기면: 어느 것이 맞을까요?');
  return t('This melody starts in ' + k4KeyLab(K4_MOD[q.i].h) + '. Where does it go?', '이 선율은 ' + k4KeyLab(K4_MOD[q.i].h) + '에서 시작해요. 어디로 갈까요?');
}
function k4Why(q) {
  if (q.kind === 'sig') { const nm = k4KeyLab(q.answer);
    if (q.minor) { const rel = K4_MAJ[q.ty][q.n]; return t('The signature belongs to ' + rel + ' major; its relative minor is three semitones below: ' + nm + '.', '이 조표의 장조는 ' + rel + '장조, 나란한 단조는 반음 세 개 아래: ' + nm + '.'); }
    return q.ty === 'sharp' ? t('The last sharp is the 7th note: go up a semitone to the key note: ' + nm + '.', '마지막 샵은 7번째 음: 반음 올라가면 으뜸음: ' + nm + '.') : t('The second-last flat names the key: ' + nm + '.', '뒤에서 두 번째 플랫이 조 이름: ' + nm + '.'); }
  if (q.kind === 'lead') return t(K4_LEAD[q.k].why[0], K4_LEAD[q.k].why[1]);
  if (q.kind === 'semi') { const [a, b] = K4_SEMI[q.i].map(h3N), A = h3Let(a), B = h3Let(b); return q.answer === 'dia' ? t('Different letters (' + A + ', ' + B + '): a diatonic semitone, the kind a major or minor scale uses.', '다른 글자(' + A + ', ' + B + '): 온음계적 반음, 장음계와 단음계가 쓰는 반음.') : t('The same letter (' + A + ', ' + B + '): a chromatic semitone, only the accidental changes.', '같은 글자(' + A + ', ' + B + '): 반음계적 반음, 임시표만 바뀌어요.'); }
  if (q.kind === 'iv') { const up = q.dir === 'up', inv = k4Inv(q.answer), L = h3Let(q.ns[up ? 1 : 0]), T = h3Let(q.ns[up ? 0 : 1]);
    return up ? t(T + ' up to ' + L + ': a ' + k4IvName(q.answer) + '. Below the tonic, ' + L + ' up to ' + T + ' is its inversion: a ' + k4IvName(inv) + '.', T + '에서 ' + L + '까지: ' + k4IvName(q.answer) + '. 으뜸음 아래로 뒤집으면(' + L + '에서 ' + T + '까지) ' + k4IvName(inv) + '.')
      : t(L + ' up to ' + T + ': a ' + k4IvName(q.answer) + '. It is the inversion of ' + T + ' up to ' + L + ' (a ' + k4IvName(inv) + '): the numbers add to 9, major and minor swap, perfect stays perfect.', L + '에서 ' + T + '까지: ' + k4IvName(q.answer) + '. ' + T + '에서 ' + L + '까지(' + k4IvName(inv) + ')를 뒤집은 것: 숫자의 합은 9, 장과 단은 바뀌고, 완전은 그대로.'); }
  if (q.kind === 'tr') { const T = K4_TR[q.i], j = T.m.findIndex(([, a]) => a), A = h3Let(k4TrNotes(T.from, T.m)[j]), B = h3Let(k4TrNotes(T.to, T.m)[j]), Bn = B.length === 1 ? B + '♮' : B;
    return t('Every note moves the same distance, and the accidental moves with it: ' + A + ' in ' + K4_TRK[T.from][2] + ' becomes ' + Bn + ' in ' + K4_TRK[T.to][2] + '. Check the first note, then the accidental.', '모든 음이 같은 거리만큼 움직이고, 임시표도 함께 옮겨요: ' + K4_TRK[T.from][3] + '의 ' + A + '는 ' + K4_TRK[T.to][3] + '에서 ' + Bn + '. 첫 음, 그다음 임시표를 확인해요.'); }
  return k4ModWhy(q.i);
}
const k4Play = (q) => (q.kind === 'tr' ? () => { const a = k4TrNotes(K4_TR[q.i].from, K4_TR[q.i].m), b = k4TrVer(q.i, 'ok'); spPlay(a.concat(b).map((n, j) => ({ at: j * 0.8 + (j >= a.length ? 1.2 : 0), keys: [h3Semi(n)], len: 0.75, vol: 0.15 })), 96); } : q.kind === 'iv' ? () => h3Play([[q.ns[0], q.ns[1]]]) : q.kind === 'semi' ? () => { const [a, b] = K4_SEMI[q.i].map(h3N); spPlay([{ at: 0, keys: [h3Semi(a)], len: 1 }, { at: 1.2, keys: [h3Semi(b)], len: 1.4 }], 72); } : q.kind === 'mod' ? () => k4ModPlay(q.i) : q.kind === 'lead' ? () => { const r = K4_LEAD[q.k].r; spPlay(SP_HAR.concat([12]).map((x, j) => ({ at: j * 0.5, keys: [r + x], len: j === 7 ? 1.5 : 0.5 })), 84); } : null);
function k4Fig(q, shown, scr = true) {
  if (q.kind === 'sig') { const ty = q.ty, n = q.n; return <div style={{maxWidth:280,margin:'0 auto'}}><KSStaff count={n} type={ty} width={170} clef={q.clef} accent={BK.coral} ink={BK.ink}/>
    {shown && <div style={{textAlign:'center',fontSize:13,fontWeight:900,color:BK.muted,marginTop:4}}>{n + ' ' + (ty === 'sharp' ? t(n > 1 ? 'sharps' : 'sharp', '샵') : t(n > 1 ? 'flats' : 'flat', '플랫')) + ' · ' + k4KeyLab(K4_MAJ[ty][n]) + ' / ' + k4KeyLab(K4_MINS[ty][n] + 'm')}</div>}</div>; }
  if (q.kind === 'lead') { const c = K4_LEAD[q.k], K = SP_HAR.map(x => c.r + x).concat([c.r + 12]), lit = {}; K.forEach(x => { lit[x] = 'pale'; }); lit[c.r + 11] = shown ? 'good' : 'cor';
    return <><div style={{maxWidth:240,margin:'0 auto 4px'}}><KSStaff count={K4[q.k].ks[1]} type={K4[q.k].ks[0]} width={150} accent={BK.ink} ink={BK.ink}/></div>
      <SpKb lo={c.r} hi={c.r + 12} W={scr ? 28 : 36} H={scr ? 78 : 96} lit={lit} names={{ [c.r]: K4[q.k].en.split(' ')[0], [c.r + 11]: shown ? c.lead : '?' }} label={k4Name(q.k)}/></>; }
  if (q.kind === 'semi') { const [a, b] = K4_SEMI[q.i].map(h3N), sa = h3Semi(a), sb = h3Semi(b), lo = Math.min(sa, sb) - 2, lit = { [sa]: 'cor', [sb]: 'cor' };
    return <><div style={{maxWidth:260,margin:'0 auto'}}><IntervalStaff clef="treble" notes={[a, b]} colors={[shown ? BK.coral : BK.ink, shown ? BK.coral : BK.ink]} labels={[h3Let(a), h3Let(b)]} width={200}/></div>
      <SpKb lo={lo - (spIsW(lo) ? 0 : 1)} hi={lo + 6} W={scr ? 30 : 38} H={scr ? 74 : 92} lit={lit} label={t('Next-door keys', '이웃 건반')}/></>; }
  if (q.kind === 'iv') { const up = q.dir === 'up'; return <div style={{maxWidth:280,margin:'0 auto'}}><IntervalStaff clef={q.clef} notes={q.ns} colors={up ? [BK.ink, shown ? BK.coral : BK.ink] : [shown ? BK.coral : BK.ink, BK.ink]} labels={up ? [h3Let(q.ns[0]) + ' ' + t('(tonic)', '(으뜸음)'), shown ? h3Let(q.ns[1]) : ''] : [shown ? h3Let(q.ns[0]) : '', h3Let(q.ns[1]) + ' ' + t('(tonic)', '(으뜸음)')]} width={220}/></div>; }
  if (q.kind === 'tr') return <><div style={{fontSize:12.5,fontWeight:900,color:BK.muted,textAlign:'center'}}>{k4TrName(K4_TR[q.i].from)}</div>{k4TrMel(q.i, 'from', scr ? 300 : 360)}</>;
  const m = K4_MOD[q.i]; return <K4Melody notes={k4ModNotes(q.i)} ks={m.ks} hi={shown ? [m.clue] : []} width={scr ? 300 : 360}/>;
}
// a step's pad: a figure, a question, the reason; then another
function K4Pad({ kind, title, note, first, fixed, onResult, tag }) {
  const [q, setQ] = useState(() => genK4(kind, null, fixed != null ? fixed : first)), [pickd, setPick] = useState(null), [run, setRun] = useState(0);
  const say = (c) => { if (pickd != null) return; setPick(c); const ok = c === q.answer; setRun(r => (ok ? r + 1 : 0)); if (onResult) onResult({ ok }); };
  const next = () => { setQ(genK4(kind, q)); setPick(null); };
  const play = k4Play(q), shown = pickd != null;
  return (
    <div className="try-box" style={actBox} data-k4={tag || kind}>
      <div style={actTitle}>{title}</div>
      <div style={actNote}>{note}</div>
      <div style={{textAlign:'center',fontSize:14.5,fontWeight:800,color:BK.ink,margin:'2px 0 6px',textWrap:'balance'}}>{k4Prompt(q)}</div>
      {k4Fig(q, shown)}
      {h3Choice(q.choices.map(c => [c, k4Lab(q, c)]), q.answer, pickd, say, q.kind === 'iv' || q.kind === 'mod' || q.kind === 'tr' ? 1 : q.choices.length > 3 ? 2 : q.choices.length)}
      {shown && <div style={{marginTop:10,fontSize:13.5,color:'#4a4d86',background:'#fff',borderRadius:8,padding:'7px 10px',lineHeight:1.45}}>{(pickd === q.answer ? t('Yes. ', '맞아요. ') + (run > 1 ? t(run + ' in a row. ', run + '번 연속. ') : '') : '') + k4Why(q)}</div>}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        {play && <button className="ghost-btn" style={spBtn} onClick={play}>{t('▶ Hear it', '▶ 들어 보기')}</button>}
        {shown && fixed == null && <button className="ghost-btn" style={spBtn} onClick={next}>{t('▶ Another', '▶ 다른 것')}</button>}
      </div>
    </div>
  );
}
const K4_NOTES = {
  sig: [<>The Grade 4 keys: <b>B, F♯, D♭ and G♭ major</b>; <b>B, F♯, C♯, F and B♭ minor</b>. Sharps: the last sharp is the 7th note, so go up a semitone. Flats: the second-last flat names the key. A minor key sits three semitones below its relative major.</>,
    <>4급의 조: <b>B, F♯, D♭, G♭장조</b>; <b>B, F♯, C♯, F, B♭단조</b>. 샵: 마지막 샵이 7번째 음이니 반음 올라가요. 플랫: 뒤에서 두 번째 플랫이 조 이름. 단조는 나란한 장조보다 반음 세 개 아래.</>],
  lead: [<>The harmonic minor raises the 7th, <b>with an accidental, never in the key signature</b>. In F♯ and C♯ minor that makes <b>E♯ and B♯</b>: white keys with a sharp, because each letter comes once in a scale.</>,
    <>화성 단음계는 7도를 올려요, <b>조표가 아니라 임시표로</b>. F♯단조와 C♯단조에서는 <b>E♯와 B♯</b>: 샵이 붙은 흰건반이에요. 음계는 글자를 한 번씩 쓰니까요.</>],
  semi: [<>A semitone is always next-door keys, but it can be written two ways. <b>Different letters</b> (E–F, C♯–D): a <b>diatonic</b> semitone, as in a major or minor scale. <b>The same letter</b> (C–C♯): a <b>chromatic</b> semitone. The chromatic scale uses both.</>,
    <>반음은 언제나 이웃 건반이지만 두 가지로 적어요. <b>다른 글자</b>(E–F, C♯–D): <b>온음계적</b> 반음, 장음계와 단음계 속의 반음. <b>같은 글자</b>(C–C♯): <b>반음계적</b> 반음. 반음계는 둘 다 써요.</>],
  iv: [<>Above the tonic, or <b>below</b> it. Below is the <b>inversion</b> of above: the numbers add to 9, <b>major and minor swap</b>, <b>perfect stays perfect</b>. Count from the lower note, always.</>,
    <>으뜸음 위로, 또는 <b>아래로</b>. 아래는 위를 <b>뒤집은 것</b>: 숫자의 합은 9, <b>장과 단은 바뀌고</b>, <b>완전은 그대로</b>. 언제나 아래 음부터 세요.</>],
  mod: [<>A melody can travel to a nearby key. Look for <b>the new accidental</b>: it is the new key's <b>leading note</b> (in a minor key, a natural that cancels the raised 7th points to the relative major). Then see where the tune <b>comes to rest</b>.</>,
    <>선율은 가까운 조로 옮겨 가기도 해요. <b>새 임시표</b>를 찾아요: 새 조의 <b>이끎음</b>이에요(단조에서 올린 7도를 지우는 제자리표는 나란한 장조를 가리켜요). 그다음 선율이 <b>어디서 쉬는지</b> 봐요.</>],
};
K4_NOTES.tr = [<>To <b>transpose</b> is to write the same tune in another key. Every note moves <b>the same distance</b>; the key signature changes, and <b>an accidental moves with its note</b>: a sharp may become a natural, a natural a flat.</>,
  <>선율을 <b>옮긴다</b>는 건 같은 선율을 다른 조로 적는 거예요. 모든 음이 <b>같은 거리</b>만큼 움직이고, 조표가 바뀌고, <b>임시표도 그 음과 함께</b> 옮겨요: 샵이 제자리표가 되거나, 제자리표가 플랫이 되기도 해요.</>];
const k4Note2 = (kind) => (LANG === 'ko' ? K4_NOTES[kind][1] : K4_NOTES[kind][0]);
const K4_STEP = { sig: ['The Grade 4 keys', '4급의 조'], lead: ['The raised 7th', '올린 7도'], semi: ['Diatonic or chromatic?', '온음계적? 반음계적?'], iv: ['Above or below the tonic', '으뜸음 위로, 아래로'], mod: ['Where does the tune go?', '선율은 어디로 갈까?'], tr: ['Transposing a melody', '선율 옮기기'] };
const k4StepT = (kind) => t(K4_STEP[kind][0], K4_STEP[kind][1]);
const K4_FIRST = { sig: 0, lead: 'Fsm', semi: 0, iv: { k: 'Db', clef: 'treble', dir: 'down', x: 7 }, mod: 0, tr: 0 };
const K4Step = ({ kind, fixed, onResult }) => <K4Pad kind={kind} title={k4StepT(kind)} note={k4Note2(kind)} first={K4_FIRST[kind]} fixed={fixed} onResult={onResult}/>;

// ── the pictures on paper ──
const k4PicSig = () => ({ shapes: [{ k: 'raw', svg: [0, 1, 2, 3, 4].map(i => '<line x1="4" x2="76" y1="' + (12 + i * 5) + '" y2="' + (12 + i * 5) + '" stroke="#26296b" stroke-width="1"/>').join('') + [[18, 12], [28, 27], [38, 7]].map(([x, y]) => '<text x="' + x + '" y="' + (y + 5) + '" font-size="14" font-weight="900" fill="#e4572e">♯</text>').join('') }], vb: [0, 0, 80, 44] });
const k4PicLead = () => { const m = spMiniKeys(6, 18, { 6: 'pale', 17: 'cor', 18: 'pale' }); return { shapes: [{ k: 'raw', svg: m.svg }], vb: [0, 0, m.w, 44] }; };
const k4PicSemi = () => { const m = spMiniKeys(0, 6, { 0: 'cor', 1: 'cor', 4: 'cor', 5: 'cor' }); return { shapes: [{ k: 'raw', svg: m.svg }], vb: [0, 0, m.w, 44] }; };
const k4PicIv = () => ({ shapes: [{ k: 'raw', svg: lsCircleSvg(18, 30, 7, 'play', '') + lsCircleSvg(18, 12, 7, 'beat', '') + lsCircleSvg(58, 12, 7, 'play', '') + lsCircleSvg(58, 30, 7, 'beat', '') + '<path d="M30 21 L46 21 M42 17 L46 21 L42 25" fill="none" stroke="#e4572e" stroke-width="2"/>' }], vb: [0, 0, 80, 44] });
const k4PicTr = () => ({ shapes: [{ k: 'raw', svg: [[6, 30], [16, 24], [26, 28]].map(([x, y]) => lsCircleSvg(x, y, 4.5, 'beat', '')).join('') + '<path d="M34 24 L44 24 M40 20 L44 24 L40 28" fill="none" stroke="#e4572e" stroke-width="2"/>' + [[52, 22], [62, 16], [72, 20]].map(([x, y]) => lsCircleSvg(x, y, 4.5, 'play', '')).join('') }], vb: [0, 0, 80, 44] });
const k4PicMod = () => ({ shapes: [{ k: 'raw', svg: [[8, 30], [20, 24], [32, 18], [44, 24], [56, 12], [68, 16]].map(([x, y], i) => lsCircleSvg(x, y, 5, i === 4 ? 'play' : 'beat', '')).join('') + '<text x="47" y="16" font-size="11" font-weight="900" fill="#e4572e">♯</text>' }], vb: [0, 0, 80, 44] });

function k4LbPages(scr = false) {
  const ch = 'keys-4';
  const pen = (x) => <PenArt shapes={x.shapes} vb={x.vb} style={{width:90}}/>;
  const checks5 = [[k4PicSig(), t('I name the Grade 4 keys from their key signatures', '조표를 보고 4급의 조 이름을 말해요')], [k4PicLead(), t('I write the raised 7th of the Grade 4 minor keys, E♯ and B♯ too', '4급 단조의 올린 7도를 적어요, E♯와 B♯도')],
    [k4PicSemi(), t('I tell a diatonic semitone from a chromatic one', '온음계적 반음과 반음계적 반음을 구별해요')], [k4PicIv(), t('I name intervals above or below the tonic, and turn them upside down', '으뜸음 위와 아래의 음정 이름을 말하고, 뒤집을 수 있어요')],
    [k4PicMod(), t('I see where a melody goes: to the dominant or the relative', '선율이 딸림조로 가는지 나란한조로 가는지 알아봐요')], [k4PicTr(), t('I transpose a short melody into another key, accidentals too', '짧은 선율을 다른 조로 옮겨요, 임시표도')]];
  const kinds = ['sig', 'lead', 'semi', 'iv', 'mod', 'tr'];
  const toc = kinds.map((k, i) => [k4StepT(k), i + 2]).concat([[t('My six checks', '나의 여섯 가지 확인'), 8]]);
  const still = (kind, fx) => kind === 'tr' ? <LbPic h={170}><div style={{display:'grid',gridTemplateColumns:'1fr',gap:6,width:'100%',maxWidth:600,margin:'0 auto'}}>{['from', 'ok'].map(c => <div key={c}><div style={{fontSize:12.5,fontWeight:900,color:BK.muted,textAlign:'center'}}>{k4TrName(c === 'from' ? K4_TR[0].from : K4_TR[0].to)}</div>{k4TrMel(0, c, scr ? 300 : 380)}</div>)}</div></LbPic> : <LbPic h={kind === 'mod' ? 150 : 170}><div style={{width:'100%',maxWidth:kind === 'mod' ? 600 : 480,margin:'0 auto'}}>{k4Fig(genK4(kind, null, fx), true, scr)}</div></LbPic>;
  const TEACH = {
    sig: t('Theory of Music Grade 4 adds the scales and key signatures of B, F♯, D♭ and G♭ major and B, F♯, C♯, F and B♭ minor (harmonic form), one or two octaves, treble or bass. The rules the earlier chapter taught still work: the last sharp is the leading note; the second-last flat names the key; the relative minor is a minor 3rd below its major.', '이론 4급은 B, F♯, D♭, G♭장조와 B, F♯, C♯, F, B♭단조(화성 단음계)의 음계와 조표를 더해요. 한 옥타브나 두 옥타브, 높은음자리표나 낮은음자리표. 앞 챕터의 규칙이 그대로 통해요: 마지막 샵이 이끎음, 뒤에서 두 번째 플랫이 조 이름, 나란한 단조는 장조보다 단3도 아래.'),
    lead: t('The raised 7th of the harmonic minor is written as an accidental: A♯ in B minor, E♯ in F♯ minor, B♯ in C♯ minor, E♮ in F minor, A♮ in B♭ minor. E♯ and B♯ are where children write F or C instead: the letter must follow on from the 6th. Double sharps and flats (also Grade 4) have their own lesson in Accidentals.', '화성 단음계의 올린 7도는 임시표로 적어요: B단조 A♯, F♯단조 E♯, C♯단조 B♯, F단조 E♮, B♭단조 A♮. E♯와 B♯ 자리에 아이들이 F나 C를 적기 쉬워요: 글자는 6도 다음 글자여야 해요. 겹샵과 겹플랫(역시 4급)은 임시표의 자기 레슨에 있어요.'),
    semi: t('General knowledge, Grade 4: diatonic and chromatic, as applied to semitones and to scales. A diatonic semitone has two letter names (E–F, C♯–D); a chromatic semitone keeps the letter (C–C♯). Major and minor scales are diatonic; the chromatic scale moves by semitones throughout.', '일반 지식 4급: 반음과 음계에 쓰이는 온음계적·반음계적. 온음계적 반음은 글자가 둘(E–F, C♯–D), 반음계적 반음은 글자가 같아요(C–C♯). 장음계와 단음계는 온음계적, 반음계는 내내 반음으로 움직여요.'),
    iv: t('All diatonic intervals above or below the tonic, in the Grade 4 keys, treble or bass; inversion of intervals. Below the tonic, the interval is still counted from the lower note, and it is the inversion of the one above: the numbers add to 9, major and minor swap, perfect stays perfect.', '4급의 조에서 으뜸음 위나 아래의 모든 온음계 음정, 높은음자리표나 낮은음자리표; 음정 자리바꿈. 으뜸음 아래도 아래 음부터 세고, 위 음정을 뒤집은 것이에요: 숫자의 합은 9, 장과 단이 바뀌고, 완전은 그대로.'),
    tr: t('Transposition: a short melody (up to eight bars, the grade\'s note values) into another of the grade\'s keys, accidentals involved. Every interval stays; the accidentals move with their notes and may change sign (F♯ in G major becomes B♮ in F major). The app asks which of three versions is right: one has lost an accidental, one starts on the wrong note.', '옮기기: 짧은 선율(8마디까지, 그 급의 음표)을 그 급의 다른 조로, 임시표도 함께. 모든 음정은 그대로, 임시표는 음과 함께 옮기며 기호가 바뀔 수 있어요(G장조의 C♯은 F장조에서 B♮). 앱은 세 가지 중 맞는 것을 고르게 해요: 하나는 임시표를 잃었고, 하나는 첫 음이 틀렸어요.'),
    mod: t('Recognition in melodies of modulation to the dominant or the relative major or minor. The clue is usually the new key\'s leading note (C major → G: F♯; C major → A minor: G♯; A minor → E minor: D♯); a minor key going to its relative major cancels its raised 7th (A minor → C: G♮). Then the cadence: where the tune comes to rest. The clues are the usual textbook ones: check them against the papers you use.', '선율의 전조 알아보기: 딸림조, 또는 나란한 장조·단조로. 단서는 대개 새 조의 이끎음(C장조 → G: F♯; C장조 → A단조: G♯; A단조 → E단조: D♯); 단조가 나란한 장조로 갈 때는 올린 7도를 제자리로(A단조 → C: G♮). 그다음 종지: 선율이 어디서 쉬는지. 단서는 흔히 쓰는 교과서 규칙이에요: 쓰시는 시험지와 맞춰 보세요.'),
  };
  const SAY = {
    sig: t('Sharps: up a semitone from the last sharp. Flats: the second-last flat. Minor: three semitones below its major.', '샵: 마지막 샵에서 반음 위. 플랫: 뒤에서 두 번째. 단조: 장조보다 반음 세 개 아래.'),
    lead: t('The raised 7th: an accidental, and the right letter.', '올린 7도: 임시표로, 맞는 글자로.'),
    semi: t('Different letters: diatonic. The same letter: chromatic.', '다른 글자: 온음계적. 같은 글자: 반음계적.'),
    iv: t('Below is above, turned upside down: add to 9; major and minor swap.', '아래는 위를 뒤집은 것: 합은 9, 장과 단이 바뀌어요.'),
    mod: t('Find the new accidental, then where the tune comes to rest.', '새 임시표를 찾고, 선율이 쉬는 곳을 봐요.'),
    tr: t('The same distance for every note; the accidentals travel too.', '모든 음이 같은 거리, 임시표도 함께.'),
  };
  const PIANO = {
    sig: [t('Play B major, one octave: count its five sharps.', 'B장조를 한 옥타브: 샵 다섯 개를 세요.'), t('Play D♭ major: five flats, the second-last is D♭.', 'D♭장조: 플랫 다섯, 뒤에서 두 번째가 D♭.'), t('Play their relative minors: G♯ and B♭ minor.', '나란한 단조도: G♯단조와 B♭단조.')],
    lead: [t('Play F♯ harmonic minor, one octave. Which key is E♯?', 'F♯ 화성 단음계를 한 옥타브. E♯는 어느 건반?'), t('Play C♯ harmonic minor: B♯ is the key C.', 'C♯ 화성 단음계: B♯는 건반 C.'), t('Write both scales, with the accidental on the 7th.', '두 음계를 적어요, 7도에 임시표를 붙여서.')],
    semi: [t('Play C then C♯: the same letter, chromatic.', 'C 다음 C♯: 같은 글자, 반음계적.'), t('Play C♯ then D: different letters, diatonic.', 'C♯ 다음 D: 다른 글자, 온음계적.'), t('Play the chromatic scale from C: both kinds, one after another.', 'C에서 반음계: 두 가지가 번갈아.')],
    iv: [t('D♭ major: play the tonic, then the 6th above it: a major 6th.', 'D♭장조: 으뜸음, 그다음 위의 6도: 장6도.'), t('Now that note an octave lower, below the tonic: a minor 3rd.', '그 음을 한 옥타브 아래로, 으뜸음 아래: 단3도.'), t('Check: 6 + 3 = 9, major became minor.', '확인: 6 + 3 = 9, 장이 단이 됐어요.')],
    tr: [t('Play the C major tune, then the same tune starting on D.', 'C장조 선율, 그다음 D에서 시작하는 같은 선율을 쳐요.'), t('Find where the F♯ went: it is now G♯.', 'F♯은 어디로 갔을까요: 이제 G♯.'), t('Write it in D major, with the key signature and the accidental.', 'D장조로, 조표와 임시표를 붙여 적어요.')],
    mod: [t('Play the C major melody that turns to G: hear the F♯.', 'G로 가는 C장조 선율을 쳐요: F♯를 들어 봐요.'), t('Now the one that turns to A minor: hear the G♯.', '이번엔 A단조로 가는 선율: G♯를 들어 봐요.'), t('Point to the new accidental, then the last note.', '새 임시표를 가리키고, 마지막 음도.')],
  };
  const FX = { sig: 0, lead: 'Fsm', semi: 0, iv: { k: 'Db', clef: 'treble', dir: 'down', x: 3 }, mod: 0, tr: 0 };
  return [
    <LbPage key="1" no={1} chId={ch} teacher={<>{t('Theory of Music Grade 4, one step each: the new keys and their signatures; the raised 7th of the new minor keys; diatonic and chromatic semitones; intervals above or below the tonic, and inversion; modulation to the dominant or the relative; transposition. Double sharps and flats, also Grade 4, are taught in Accidentals.', '이론 4급을 한 단계씩: 새 조와 조표; 새 단조의 올린 7도; 온음계적·반음계적 반음; 으뜸음 위·아래의 음정과 자리바꿈; 딸림조나 나란한조로의 전조; 선율 옮기기. 겹샵과 겹플랫(역시 4급)은 임시표에서 배워요.')}</>}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:48,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{bkChapterName(ch)}</div>
      </div></LbOnly>
      {still('lead', 'Fsm')}
      <LbSay size={18}>{t('Grade 4 theory: five and six sharps and flats, E♯ and B♯, two kinds of semitone, intervals below the tonic, and a tune that travels to a new key.', '4급 이론: 샵과 플랫 다섯, 여섯 개, E♯와 B♯, 두 가지 반음, 으뜸음 아래의 음정, 그리고 새 조로 옮겨 가는 선율.')}</LbSay>
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
    ...kinds.map((kind, i) => <LbPage key={kind} no={i + 2} chId={ch} kicker={t('Step ' + (i + 1), (i + 1) + '단계')} title={k4StepT(kind)} teacher={<>{TEACH[kind]}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=' + (i + 1))}>
      <LbLive still={still(kind, FX[kind])} live={<K4Step kind={kind}/>}/>
      <LbSay>{k4Note2(kind)}</LbSay>
      <LbPiano steps={PIANO[kind].map((x, j) => <React.Fragment key={j}>{x}</React.Fragment>)}/>
      <LbRemember>{SAY[kind]}</LbRemember>
    </LbPage>),
    <LbPage key="8" no={8} chId={ch} kicker={t('Check-up', '점검')} title={t('My six checks', '나의 여섯 가지 확인')}
      teacher={<>{t('Each one on paper or at the piano, in the Grade 4 keys, treble and bass. Use keys the child has not just practised.', '하나씩 종이나 피아노에서, 4급의 조로, 높은음자리표와 낮은음자리표 둘 다. 방금 연습하지 않은 조로 해 보세요.')}</>}>
      <LbSay>{t('Tick each one: not yet, nearly, or got it!', '하나씩 표시해요: 아직, 거의, 됐어요!')}</LbSay>
      <LbLive still={<LbStageRows big rows={checks5.map(([a, txt]) => [pen(a), txt])}/>} live={<FiveChecks376 rows={checks5} storeKey="pb_k4_five"/>}/>
    </LbPage>,
  ];
}
function Keys4LessonBook() { return <>{k4LbPages(false)}</>; }
function K4Learn({ onStart }) {
  const pages = k4LbPages(true), opener = pages[0];
  return (
    <Lesson id="keys-4" title={bkChapterName('keys-4')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="keys-4"><div className="lb-screen lb-open" style={{display:'flex',flexDirection:'column',gap:12,margin:'0 0 8px'}}>{lbWordsFirst(opener.props.children)}</div></BkChapterCtx.Provider></LbScreenCtx.Provider>}>
      {pages.slice(1).map((pg, i) => <Step key={i} title={pg.props.title}><LbScreenPage page={pg}/></Step>)}
    </Lesson>
  );
}
// ── the drill ──
const K4_LEVELS = [
  { n: 1, label: 'The Grade 4 keys: which key?', kind: 'sig', time: 15 },
  { n: 2, label: 'The raised 7th: how is it written?', kind: 'lead', time: 15 },
  { n: 3, label: 'Diatonic or chromatic semitone?', kind: 'semi', time: 12 },
  { n: 4, label: 'Intervals above or below the tonic', kind: 'iv', time: 20 },
  { n: 5, label: 'Modulation: the dominant or the relative?', kind: 'mod', time: 25 },
  { n: 6, label: 'Transposition: which is right?', kind: 'tr', time: 30 },
];
Object.assign(LEVEL_KO, { 'The Grade 4 keys: which key?': '4급의 조: 어느 조?', 'The raised 7th: how is it written?': '올린 7도: 어떻게 적을까?', 'Diatonic or chromatic semitone?': '온음계적? 반음계적 반음?', 'Intervals above or below the tonic': '으뜸음 위와 아래의 음정', 'Modulation: the dominant or the relative?': '전조: 딸림조? 나란한조?', 'Transposition: which is right?': '옮기기: 어느 것이 맞을까?' });
const genK4Question = (lv, prev) => genK4(lv.kind, prev);
const k4AnswerLabel = (q) => (q.kind === 'tr' ? t('the version that keeps every interval and accidental', '음정과 임시표를 그대로 지킨 것') : k4Lab(q, q.answer));
function K4Question({ q, given, locked, onAnswer, pixel }) {
  const done = !!given, play = k4Play(q);
  useEffect(() => { if (q.kind !== 'mod') return; const id = setTimeout(() => play && play(), 350); return () => { clearTimeout(id); stopClicks(); }; }, [q.uid]);
  const btnCls = pixel ? 'pixel-choice' : 'choice-btn', cls = (c) => btnCls + (!done ? '' : c === q.answer ? ' good' : given.ans === c ? ' bad' : '');
  const cols = q.kind === 'iv' || q.kind === 'mod' || q.kind === 'tr' ? 1 : q.choices.length > 3 ? 2 : q.choices.length;
  return (<div>
    <p style={pixel ? {fontSize:11.5,textAlign:'center'} : {fontSize:15,fontWeight:700,textAlign:'center',margin:'0 0 8px',color:'var(--muted)',textWrap:'balance'}}>{k4Prompt(q)}</p>
    {k4Fig(q, done)}
    {play && <div style={{textAlign:'center',margin:'6px 0 0'}}><button className={pixel ? 'pixel-btn' : 'ghost-btn'} style={{minHeight:44}} onClick={() => { stopClicks(); play(); }}>{t('▶ Hear it', '▶ 들어 보기')}</button></div>}
    <div style={{display:'grid',gridTemplateColumns:'repeat(' + cols + ',minmax(0,1fr))',gap:8,marginTop:10}}>{q.choices.map(c => <button key={String(c)} disabled={locked} className={cls(c)} style={{padding:'12px 4px',fontSize:15,fontWeight:900}} onClick={() => { if (locked || done) return; stopClicks(); onAnswer(c); }}>{k4Lab(q, c)}</button>)}</div>
    {done && !pixel && <div style={{marginTop:10,fontSize:13.5,color:'#4a4d86',background:'#fff',borderRadius:8,padding:'7px 10px',lineHeight:1.45}}>{k4Why(q)}</div>}
  </div>);
}
Object.assign(KEYS_4_DRILL, { levels: K4_LEVELS, generate: genK4Question, check: (q, ans) => ans !== null && ans !== undefined && ans === q.answer, answerLabel: k4AnswerLabel, Question: K4Question, Learn: K4Learn });
// the teacher's copy (the Workbook comes with the floor's Workbooks)
function K4Teacher() {
  const pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="keys-4" teacher>{content}</WbPage>);
  const scale = (k) => { const ns = Array.from({ length: 8 }, (_, x) => k4Note(k, 'treble', x)); return K4[k].en + ': ' + ns.map(h3Let).join(' '); };
  const below = (k) => { const ns = Array.from({ length: 7 }, (_, x) => k4Iv(k4Note(k, 'treble', x), k4Note(k, 'treble', 7))); return K4[k].en + ' below: ' + ns.map((id, x) => h3Let(k4Note(k, 'treble', x)) + ' ' + id).join(', '); };
  P(<>
    <div style={{fontFamily:LB_SERIF,fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('keys-4')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 12px',lineHeight:1.5}}>Theory of Music Grade 4. Every answer below is computed from the room's own data, the same as the app uses.</div>
    <TcBlock page={2} title="The Grade 4 keys" answers={<>{tcAns('MAJOR', ['B (5♯)', 'F♯ (6♯)', 'D♭ (5♭)', 'G♭ (6♭)'])}{tcAns('MINOR, HARMONIC', ['B (2♯)', 'F♯ (3♯)', 'C♯ (4♯)', 'F (4♭)', 'B♭ (5♭)'])}{tcAns('SCALES', K4_IDS.map(scale), null)}</>}
      watch="The minor key named from the major rule. A minor key is a minor 3rd below the major that shares its signature."
      say="“Sharps: up a semitone from the last sharp. Flats: the second-last flat.”"/>
    <TcBlock page={3} title="The raised 7th" answers={<>{tcAns('HARMONIC MINOR 7TH', K4_MIN.map(k => K4[k].en + ': ' + K4_LEAD[k].lead))}</>}
      watch="F for E♯, C for B♯: the right key, the wrong letter. Each letter once in a scale."
      say="“The raised 7th: an accidental, and the right letter.”"/>
  </>);
  P(<>
    <TcBlock page={4} title="Diatonic or chromatic?" answers={<>{tcAns('PAIRS', K4_SEMI.map((p, i) => p.map(h3N).map(h3Let).join('–') + ' ' + (k4SemiKind(i) === 'dia' ? 'diatonic' : 'chromatic')))}</>}
      watch="Judging by the keys instead of the letters: every semitone is next-door keys; only the letters tell the kind."
      say="“Different letters: diatonic. The same letter: chromatic.”"/>
    <TcBlock page={5} title="Above or below the tonic" answers={<>{tcAns('BELOW THE TONIC (the lower note, then the interval)', ['Db', 'Bbm'].map(below), null)}</>}
      watch="Counting down from the tonic and naming the interval above. Count up from the lower note; or invert: add to 9, major and minor swap."
      say="“Below is above, turned upside down.”"/>
    <TcBlock page={6} title="Where does the tune go?" answers={<>{tcAns('MELODIES', K4_MOD.map((m, i) => k4KeyLab(m.h).replace(/<[^>]*>/g, '') + ' → ' + (m.to === 'dom' ? 'dominant, ' : 'relative, ') + (m.to === 'dom' ? m.dom : m.rel) + ' (clue ' + h3Let(k4ModNotes(i)[m.clue]) + ')'))}</>}
      watch="Naming the key from the first note only. The new accidental and the last note decide."
      say="“Find the new accidental, then where the tune comes to rest.”"/>
    <TcBlock page={7} title="Transposing a melody" answers={<>{tcAns('MELODIES', K4_TR.map(T => K4_TRK[T.from][2] + ' ' + k4TrNotes(T.from, T.m).map(h3Let).join(' ') + ' → ' + K4_TRK[T.to][2] + ' ' + k4TrNotes(T.to, T.m).map(h3Let).join(' ')))}</>}
      watch="An accidental copied as it was (F♯ kept as F♯) instead of moved (to G♯ in D major). Check the first note and every accidental."
      say="“The same distance for every note; the accidentals travel too.”"/>
    <TcBlock page={8} title="My six checks" answers={<div style={{fontSize:12,color:BK.ink,lineHeight:1.5}}>On paper or at the piano, in the Grade 4 keys, treble and bass.</div>}/>
  </>);
  return <>{pages}</>;
}
TEACHER_COPIES['keys-4'] = K4Teacher;
'''
rep("""TEACHER_COPIES['harmony-23'] = H3Teacher;""", """TEACHER_COPIES['harmony-23'] = H3Teacher;""" + CH)

HOME = r'''
// ══ Build AT: Keys and Intervals, Grade 4 on the Home (Scales and keys, after Minor scales) ══
LBH_FN['keys-4'] = (s) => k4LbPages(s);
const k4HomeQ = (kind) => (n, prev) => { const q = genK4(kind, prev), a = q.answer, p = k4Prompt(q), w = k4Why(q);   // in the language of the moment, as the question is made
  return { kind: 'choice', cols: kind === 'iv' || kind === 'mod' || kind === 'tr' ? 1 : q.choices.length > 3 ? 2 : q.choices.length, key: q.key, prompt: [p, p], opts: q.choices.map(c => ({ id: c, label: () => k4Lab(q, c) })), ans: a, ok: (v) => v === a,
    play: k4Play(q), fig: (c) => ({ mid: k4Fig(q, !!c.res) }), yes: ['Yes. ' + w, '맞아요. ' + w], no: [w, w] }; };
const k4HomeAdd = (id, i, en, ko, benEn, bko, make) => lbhAdd(id, 'p-scales', 'pitch', en, ko, benEn, bko, lbhSpec('keys-4', i, { make }));
k4HomeAdd('k4-sig', 1, 'The Grade 4 keys', '4급의 조', 'Five and six sharps and flats, and their minors.', '샵과 플랫 다섯, 여섯 개, 그리고 단조.', k4HomeQ('sig'));
k4HomeAdd('k4-lead', 2, 'The raised 7th', '올린 7도', 'E♯ and B♯: the right key, the right letter.', 'E♯와 B♯: 맞는 건반, 맞는 글자.', k4HomeQ('lead'));
k4HomeAdd('k4-semi', 3, 'Diatonic or chromatic?', '온음계적? 반음계적?', 'Two kinds of semitone: the letters tell.', '두 가지 반음: 글자가 알려 줘요.', k4HomeQ('semi'));
k4HomeAdd('k4-below', 4, 'Above or below the tonic', '으뜸음 위로, 아래로', 'Below is above, turned upside down.', '아래는 위를 뒤집은 것.', k4HomeQ('iv'));
k4HomeAdd('k4-tr', 6, 'Transposing a melody', '선율 옮기기', 'The same tune in another key, accidentals too.', '같은 선율을 다른 조로, 임시표도.', k4HomeQ('tr'));
k4HomeAdd('k4-mod', 5, 'Where does the tune go?', '선율은 어디로 갈까?', 'The new accidental, then where it comes to rest.', '새 임시표, 그다음 쉬는 곳.', k4HomeQ('mod'));
'''
rep("""
lbhAdd('rb-finger', 'r-beat', 'rhythm', 'The beat in your fingers'""", HOME + """
lbhAdd('rb-finger', 'r-beat', 'rhythm', 'The beat in your fingers'""")
rep("""const LESSON_BOOKS = { 'scales-4': Scales4LessonBook,""", """const LESSON_BOOKS = { 'keys-4': Keys4LessonBook, 'scales-4': Scales4LessonBook,""")
rep("""const LB_PAGE_FNS = { 'scales-4': s4LbPages,""", """const LB_PAGE_FNS = { 'keys-4': k4LbPages, 'scales-4': s4LbPages,""")
rep("""const HOUSE_ICONS = {"scales-4": """, """const HOUSE_ICONS = {"keys-4": "<path d=\\"M4 13 H44 M4 19 H44 M4 25 H44 M4 31 H44 M4 37 H44\\" stroke-width=\\"1.2\\"/><text x=\\"10\\" y=\\"30\\" font-size=\\"15\\" font-weight=\\"900\\" fill=\\"#e4572e\\" stroke=\\"none\\">♯♯</text><text x=\\"32\\" y=\\"38\\" font-size=\\"12\\" font-weight=\\"900\\" fill=\\"#26296b\\" stroke=\\"none\\" font-family=\\"Inter, sans-serif\\">4</text>", "scales-4": """)
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
