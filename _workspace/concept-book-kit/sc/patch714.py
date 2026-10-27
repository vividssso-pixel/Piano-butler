import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build AU (board call 18, the fourth Grade 4 room): Chords and Cadences, Grade 4. Theory of Music Grade 4 (Manual of Syllabuses
# 2026, read 26 Oct): the recognition of chords on I, II, IV, V, VI and their first inversions in major keys, and I, IV, V, VI and
# their first inversions in minor keys, in keys up to four sharps or four flats, in four-part vocal style; the writing and
# recognition of the four principal cadences in the same keys; the harmonisation of a simple melody of not more than six bars.
# Every four-part chord and cadence here was realised from scale-degree templates and checked by a script before it went in
# (sc/au/satb.py: each voice in its range, no voices crossing, upper voices within an octave, no parallel 5ths or octaves,
# the leading note never doubled, the third doubled in VI after V). The chord names follow the app's earlier chapters (small
# letters for minor chords: ii, vi, i, iv); the syllabus prints them all as capitals: flagged on the board.

rep("""const KEYS_4_DRILL = { id: 'keys-4', label: 'Keys and Intervals, Grade 4' };   // Build AT""",
    """const KEYS_4_DRILL = { id: 'keys-4', label: 'Keys and Intervals, Grade 4' };   // Build AT
const HARMONY_4_DRILL = { id: 'harmony-4', label: 'Chords and Cadences, Grade 4' };   // Build AU""")
rep("""  { id: 'keys-4', label: 'Keys and Intervals, Grade 4', concept: KEYS_4_DRILL, track: 'start' },   // Build AT""",
    """  { id: 'keys-4', label: 'Keys and Intervals, Grade 4', concept: KEYS_4_DRILL, track: 'start' },   // Build AT
  { id: 'harmony-4', label: 'Chords and Cadences, Grade 4', concept: HARMONY_4_DRILL, track: 'start' },   // Build AU""")
rep("""'keys-4': '조와 음정, Grade 4'""", """'keys-4': '조와 음정, Grade 4', 'harmony-4': '화음과 종지, Grade 4'""")
rep("""'keys-4': ['key-signatures', 'harmony-23'],""", """'keys-4': ['key-signatures', 'harmony-23'], 'harmony-4': ['harmony-23', 'keys-4'],""")
rep("""'keys-4': ['Keys, Grade 4', '조 4'],""", """'keys-4': ['Keys, Grade 4', '조 4'], 'harmony-4': ['Chords, Grade 4', '화음 4'],""")
rep("""  'keys-4': 'keys intervals grade 4""", """  'harmony-4': 'chords cadences grade 4 theory supertonic submediant first inversion four part vocal perfect plagal imperfect interrupted harmonise melody',
  'keys-4': 'keys intervals grade 4""")
rep("""'keys-4': 'p-scales', 'harmony-23'""", """'keys-4': 'p-scales', 'harmony-4': 'p-chords', 'harmony-23'""")
rep("""    { id: 'ch-23', en: 'Intervals and chords further', ko: '음정과 화음 한 걸음 더',""", """    { id: 'ch-4', en: 'Chords and cadences, Grade 4', ko: '화음과 종지, Grade 4', lessons: ['h4-deg', 'h4-inv', 'h4-cad', 'h4-fit'], check: 'harmony-4' },   // Build AU
    { id: 'ch-23', en: 'Intervals and chords further', ko: '음정과 화음 한 걸음 더',""")
rep("""  set('4', 'k4-sig k4-lead k4-semi k4-below k4-mod k4-tr');   // Build AT: Keys and Intervals, Grade 4""",
    """  set('4', 'k4-sig k4-lead k4-semi k4-below k4-mod k4-tr');   // Build AT: Keys and Intervals, Grade 4
  set('4', 'h4-deg h4-inv h4-cad h4-fit');   // Build AU: Chords and Cadences, Grade 4""")

CH = r'''
// ─── Chapter: Chords and Cadences, Grade 4 (Build AU, 2026-10-26; board call 18, the fourth Grade 4 room) ───
// Chords on I, II, IV, V and VI (major) and I, IV, V and VI (minor), root position and first inversion, in four parts, in keys up
// to four sharps or flats; the four principal cadences; choosing chords for a melody. Four-part chords are voiced by rule (root
// position: the root doubled, close position above; first inversion: the 3rd in the bass, the root and 5th above, so the leading
// note is never doubled); the cadences are the checked realisations.
const H4_KEYS = {   // tonic letter, accidental, key signature, minor
  C: ['C', 0, [null, 0]], G: ['G', 0, ['sharp', 1]], D: ['D', 0, ['sharp', 2]], A: ['A', 0, ['sharp', 3]], E: ['E', 0, ['sharp', 4]],
  F: ['F', 0, ['flat', 1]], Bb: ['B', -1, ['flat', 2]], Eb: ['E', -1, ['flat', 3]], Ab: ['A', -1, ['flat', 4]],
  Am: ['A', 0, [null, 0], 1], Em: ['E', 0, ['sharp', 1], 1], Bm: ['B', 0, ['sharp', 2], 1], Fsm: ['F', 1, ['sharp', 3], 1], Csm: ['C', 1, ['sharp', 4], 1],
  Dm: ['D', 0, ['flat', 1], 1], Gm: ['G', 0, ['flat', 2], 1], Cm: ['C', 0, ['flat', 3], 1], Fm: ['F', 0, ['flat', 4], 1],
};
const H4_IDS = Object.keys(H4_KEYS);
const h4Min = (k) => !!H4_KEYS[k][3];
const h4Name = (k) => { const L = H4_KEYS[k][0] + (H4_KEYS[k][1] > 0 ? '♯' : H4_KEYS[k][1] < 0 ? '♭' : ''); return h4Min(k) ? t(L + ' minor', L + '단조') : t(L + ' major', L + '장조'); };
const h4Sig = (k) => { const [ty, n] = H4_KEYS[k][2], out = {}; if (ty) (ty === 'sharp' ? SHARP_ORDER : FLAT_ORDER).slice(0, n).forEach(a => { out[a[0]] = ty === 'sharp' ? 1 : -1; }); return out; };
const h4Td = (k, oct = 3) => oct * 7 + H3_L.indexOf(H4_KEYS[k][0]);
const h4Note = (k, td, step) => { const d = td + step, L = H3_L[((d % 7) + 7) % 7]; let a = h4Sig(k)[L] || 0; if (h4Min(k) && ((step % 7) + 7) % 7 === 6) a += 1; return { d, acc: a }; };
const h4M = (n) => ivMidi(n);
const H4_RANGE = { S: [60, 79], A: [55, 72], T: [48, 67], B: [40, 60] };   // C4-G5, G3-C5, C3-G4, E2-C4
const H4_DEGS = (k) => (h4Min(k) ? [1, 4, 5, 6] : [1, 2, 4, 5, 6]);
const H4_ROM = { maj: { 1: 'I', 2: 'ii', 4: 'IV', 5: 'V', 6: 'vi' }, min: { 1: 'i', 4: 'iv', 5: 'V', 6: 'VI' } };
const h4Rom = (k, deg, inv) => H4_ROM[h4Min(k) ? 'min' : 'maj'][deg] + (inv ? 'b' : '');
// one chord in four parts: { S, A, T, B }
function h4Chord(k, deg, inv) {
  const td = h4Td(k), r = deg - 1, note = (x) => h4Note(k, td, x);
  let b = (inv ? r + 2 : r) - 7; while (h4M(note(b)) > 52) b -= 7; while (h4M(note(b)) < 40) b += 7;
  const allow = inv ? [0, 4] : [0, 2, 4], ok = (x) => allow.includes((((x - r) % 7) + 7) % 7), B = note(b), cands = [];
  for (let t0 = b + 1; t0 < b + 15; t0++) { if (!ok(t0)) continue; const ups = [t0]; let x = t0 + 1; while (ups.length < 3) { if (ok(x)) ups.push(x); x++; }
    const [T, A, S] = ups.map(note), inR = (v, n) => h4M(n) >= H4_RANGE[v][0] && h4M(n) <= H4_RANGE[v][1];
    if (inR('T', T) && inR('A', A) && inR('S', S) && h4M(T) - h4M(B) >= 3) cands.push({ S, A, T, B }); }
  cands.sort((p, q) => Math.abs(h4M(p.S) - 69) - Math.abs(h4M(q.S) - 69)); return cands[0];
}
// the four cadences, realised and checked (soprano, alto, tenor, bass for each of the two chords)
const H4_CAD = {
  C: { perfect: ['B4 G4 D4 G3', 'C5 G4 E4 C3'], plagal: ['C5 A4 F4 F3', 'C5 G4 E4 C3'], imperfect: ['E5 C5 G4 C3', 'D5 B4 G4 G2'], interrupted: ['B4 G4 D4 G3', 'C5 E4 C4 A3'] },
  G: { perfect: ['F#4 D4 A3 D3', 'G4 D4 B3 G2'], plagal: ['G4 E4 C4 C3', 'G4 D4 B3 G2'], imperfect: ['D5 B4 G4 G3', 'D5 A4 F#4 D3'], interrupted: ['F#4 D4 A3 D3', 'G4 B3 G3 E3'] },
  D: { perfect: ['C#5 A4 E4 A3', 'D5 A4 F#4 D3'], plagal: ['D5 B4 G4 G3', 'D5 A4 F#4 D3'], imperfect: ['A4 F#4 D4 D3', 'A4 E4 C#4 A2'], interrupted: ['C#5 A4 E4 A3', 'D5 F#4 D4 B3'] },
  A: { perfect: ['G#4 E4 B3 E3', 'A4 E4 C#4 A2'], plagal: ['A4 F#4 D4 D3', 'A4 E4 C#4 A2'], imperfect: ['C#5 A4 E4 A2', 'B4 G#4 E4 E2'], interrupted: ['G#4 E4 B3 E3', 'A4 C#4 A3 F#3'] },
  E: { perfect: ['D#4 B3 F#3 B2', 'E4 B3 G#3 E2'], plagal: ['E4 C#4 A3 A2', 'E4 B3 G#3 E2'], imperfect: ['B4 G#4 E4 E3', 'B4 F#4 D#4 B2'], interrupted: ['D#4 B3 F#3 B2', 'E4 G#3 E3 C#3'] },
  F: { perfect: ['E4 C4 G3 C3', 'F4 C4 A3 F2'], plagal: ['F4 D4 Bb3 Bb2', 'F4 C4 A3 F2'], imperfect: ['C5 A4 F4 F3', 'C5 G4 E4 C3'], interrupted: ['E4 C4 G3 C3', 'F4 A3 F3 D3'] },
  Bb: { perfect: ['A4 F4 C4 F3', 'Bb4 F4 D4 Bb2'], plagal: ['Bb4 G4 Eb4 Eb3', 'Bb4 F4 D4 Bb2'], imperfect: ['D5 Bb4 F4 Bb2', 'C5 A4 F4 F2'], interrupted: ['A4 F4 C4 F3', 'Bb4 D4 Bb3 G3'] },
  Eb: { perfect: ['D5 Bb4 F4 Bb3', 'Eb5 Bb4 G4 Eb3'], plagal: ['C5 Ab4 Eb4 Ab3', 'Bb4 G4 Eb4 Eb3'], imperfect: ['Bb4 G4 Eb4 Eb3', 'Bb4 F4 D4 Bb2'], interrupted: ['D5 Bb4 F4 Bb3', 'Eb5 G4 Eb4 C4'] },
  Ab: { perfect: ['G4 Eb4 Bb3 Eb3', 'Ab4 Eb4 C4 Ab2'], plagal: ['Ab4 F4 Db4 Db3', 'Ab4 Eb4 C4 Ab2'], imperfect: ['Ab4 Eb4 C4 Ab2', 'G4 Eb4 Bb3 Eb3'], interrupted: ['G4 Eb4 Bb3 Eb3', 'Ab4 C4 Ab3 F3'] },
  Am: { perfect: ['G#4 E4 B3 E3', 'A4 E4 C4 A2'], plagal: ['A4 F4 D4 D3', 'A4 E4 C4 A2'], imperfect: ['C5 A4 E4 A2', 'B4 G#4 E4 E2'], interrupted: ['G#4 E4 B3 E3', 'A4 C4 A3 F3'] },
  Em: { perfect: ['D#5 B4 F#4 B3', 'E5 B4 G4 E3'], plagal: ['E4 C4 A3 A2', 'E4 B3 G3 E2'], imperfect: ['B4 G4 E4 E3', 'B4 F#4 D#4 B2'], interrupted: ['D#5 B4 F#4 B3', 'E5 G4 E4 C4'] },
  Bm: { perfect: ['A#4 F#4 C#4 F#3', 'B4 F#4 D4 B2'], plagal: ['B4 G4 E4 E3', 'B4 F#4 D4 B2'], imperfect: ['D5 B4 F#4 B2', 'C#5 A#4 F#4 F#2'], interrupted: ['A#4 F#4 C#4 F#3', 'B4 D4 B3 G3'] },
  Fsm: { perfect: ['E#4 C#4 G#3 C#3', 'F#4 C#4 A3 F#2'], plagal: ['F#4 D4 B3 B2', 'F#4 C#4 A3 F#2'], imperfect: ['C#5 A4 F#4 F#3', 'C#5 G#4 E#4 C#3'], interrupted: ['E#4 C#4 G#3 C#3', 'F#4 A3 F#3 D3'] },
  Csm: { perfect: ['B#4 G#4 D#4 G#3', 'C#5 G#4 E4 C#3'], plagal: ['C#5 A4 F#4 F#3', 'C#5 G#4 E4 C#3'], imperfect: ['G#4 E4 C#4 C#3', 'G#4 D#4 B#3 G#2'], interrupted: ['B#4 G#4 D#4 G#3', 'C#5 E4 C#4 A3'] },
  Dm: { perfect: ['C#5 A4 E4 A3', 'D5 A4 F4 D3'], plagal: ['D5 Bb4 G4 G3', 'D5 A4 F4 D3'], imperfect: ['A4 F4 D4 D3', 'A4 E4 C#4 A2'], interrupted: ['C#5 A4 E4 A3', 'D5 F4 D4 Bb3'] },
  Gm: { perfect: ['F#4 D4 A3 D3', 'G4 D4 Bb3 G2'], plagal: ['G4 Eb4 C4 C3', 'G4 D4 Bb3 G2'], imperfect: ['D5 Bb4 G4 G3', 'D5 A4 F#4 D3'], interrupted: ['F#4 D4 A3 D3', 'G4 Bb3 G3 Eb3'] },
  Cm: { perfect: ['B4 G4 D4 G3', 'C5 G4 Eb4 C3'], plagal: ['C5 Ab4 F4 F3', 'C5 G4 Eb4 C3'], imperfect: ['Eb5 C5 G4 C3', 'D5 B4 G4 G2'], interrupted: ['B4 G4 D4 G3', 'C5 Eb4 C4 Ab3'] },
  Fm: { perfect: ['E4 C4 G3 C3', 'F4 C4 Ab3 F2'], plagal: ['F4 Db4 Bb3 Bb2', 'F4 C4 Ab3 F2'], imperfect: ['C5 Ab4 F4 F3', 'C5 G4 E4 C3'], interrupted: ['E4 C4 G3 C3', 'F4 Ab3 F3 Db3'] },
};
const H4_CADS = ['perfect', 'plagal', 'imperfect', 'interrupted'];
const H4_CADN = { perfect: ['perfect', '정격종지'], plagal: ['plagal', '변격종지'], imperfect: ['imperfect', '반종지'], interrupted: ['interrupted', '거짓종지'] };
const h4CadName = (c) => t(H4_CADN[c][0] + ' cadence', H4_CADN[c][1]);
const h4CadChords = (k, c) => H4_CAD[k][c].map(str => { const [S, A, T, B] = str.split(' ').map(h3N); return { S, A, T, B }; });
const h4CadRom = (k, c) => { const m = h4Min(k); return c === 'perfect' ? ['V', m ? 'i' : 'I'] : c === 'plagal' ? [m ? 'iv' : 'IV', m ? 'i' : 'I'] : c === 'imperfect' ? (H4_CAD[k].imperfect[0] === H4_CAD[k].plagal[0] ? [m ? 'iv' : 'IV', 'V'] : [m ? 'i' : 'I', 'V']) : ['V', m ? 'VI' : 'vi']; };
const h4Play = (chs, gap = 1.6) => spPlay(chs.map((c, i) => ({ at: i * gap, keys: ['S', 'A', 'T', 'B'].map(v => h3Semi(c[v])), len: gap * 0.92, vol: 0.1 })), 60);
// melodies to harmonise (each note one chord); every one ends with a cadence on the tonic
const H4_MEL = [
  { k: 'C', m: ['G4', 'A4', 'F4', 'E4', 'D4', 'C4'] },
  { k: 'G', m: ['B4', 'C5', 'A4', 'G4', 'F#4', 'G4'] },
  { k: 'F', m: ['A4', 'Bb4', 'C5', 'A4', 'G4', 'F4'] },
  { k: 'C', m: ['E4', 'G4', 'F4', 'A4', 'C5', 'C5'] },
  { k: 'Am', m: ['A4', 'B4', 'C5', 'D5', 'B4', 'A4'] },
  { k: 'D', m: ['F#4', 'G4', 'A4', 'B4', 'E4', 'D4'] },
];
const h4Has = (k, deg, n) => [0, 2, 4].includes((((n.d - h4Td(k, 0)) - (deg - 1)) % 7 + 7) % 7);   // does the chord on deg hold this note?

// ── the questions (shared by the steps, the drill and the Home) ──
function genH4(kind, prev, fixed) {
  const uid = Math.random(), again = (key) => prev && prev.key === key;
  if (kind === 'deg' || kind === 'inv') { let k, deg, g = 0; do { k = fixed ? fixed.k : pick(H4_IDS); deg = fixed ? fixed.deg : pick(H4_DEGS(k)); } while (!fixed && again(kind + k + deg) && g++ < 12);
    const inv = kind === 'inv' ? 1 : 0, ans = h4Rom(k, deg, inv);
    let ch = H4_DEGS(k).map(d => h4Rom(k, d, inv));
    if (inv) { const bassDeg = ((deg + 1) % 7) + 1, trap = H4_DEGS(k).includes(bassDeg) ? h4Rom(k, bassDeg, 0) : null; ch = shuffle([...new Set([ans, h4Rom(k, deg, 0), trap || h4Rom(k, H4_DEGS(k).find(d => d !== deg), 1), h4Rom(k, H4_DEGS(k).filter(d => d !== deg).slice(-1)[0], 1)])]).slice(0, 4); if (!ch.includes(ans)) ch[0] = ans; }
    return { kind, k, deg, inv, chord: h4Chord(k, deg, inv), answer: ans, choices: ch, key: kind + k + deg, uid }; }
  if (kind === 'cad') { let k, c, g = 0; do { k = fixed ? fixed.k : pick(H4_IDS); c = fixed ? fixed.c : pick(H4_CADS); } while (!fixed && again('c' + k + c) && g++ < 12); return { kind, k, c, answer: c, choices: H4_CADS.slice(), key: 'c' + k + c, uid }; }
  let i, j, g = 0; do { i = fixed ? fixed.i : Math.floor(Math.random() * H4_MEL.length); j = fixed ? fixed.j : Math.floor(Math.random() * 5); } while (!fixed && again('f' + i + j) && g++ < 12);
  const M = H4_MEL[i], n = h3N(M.m[j]), fits = H4_DEGS(M.k).filter(d => h4Has(M.k, d, n)), nots = H4_DEGS(M.k).filter(d => !h4Has(M.k, d, n));
  const ans = h4Rom(M.k, pick(fits), 0), ch = shuffle([ans, ...shuffle(nots).slice(0, 2).map(d => h4Rom(M.k, d, 0))]);
  return { kind: 'fit', i, j, k: M.k, n, fits: fits.map(d => h4Rom(M.k, d, 0)), answer: ans, choices: ch, key: 'f' + i + j, uid };
}
const h4Ok = (q, c) => (q.kind === 'fit' ? q.fits.includes(c) : c === q.answer);
function h4Lab(q, c) { return q.kind === 'cad' ? h4CadName(c) : c; }
function h4Prompt(q) {
  if (q.kind === 'deg') return t(h4Name(q.k) + ': which chord is this?', h4Name(q.k) + ': 어떤 화음일까요?');
  if (q.kind === 'inv') return t(h4Name(q.k) + ': which chord, and which position?', h4Name(q.k) + ': 어떤 화음, 어떤 자리일까요?');
  if (q.kind === 'cad') return t(h4Name(q.k) + ': which cadence?', h4Name(q.k) + ': 어떤 종지일까요?');
  return t(h4Name(q.k) + ': which chord holds the coral melody note?', h4Name(q.k) + ': 빨간 선율 음이 들어 있는 화음은?');
}
const h4Letters = (k, deg) => [0, 2, 4].map(x => h3Let(h4Note(k, h4Td(k), deg - 1 + x))).join(' ');
function h4Why(q) {
  if (q.kind === 'deg') return t(h4Rom(q.k, q.deg, 0) + ': the bass is the root, ' + h3Let(q.chord.B) + '. The chord is ' + h4Letters(q.k, q.deg) + '.', h4Rom(q.k, q.deg, 0) + ': 베이스가 근음 ' + h3Let(q.chord.B) + '. 화음은 ' + h4Letters(q.k, q.deg) + '.');
  if (q.kind === 'inv') return t(q.answer + ': the chord is ' + h4Letters(q.k, q.deg) + ' and its 3rd, ' + h3Let(q.chord.B) + ', is in the bass. Name a chord by its root, not by its bass note.', q.answer + ': 화음은 ' + h4Letters(q.k, q.deg) + ', 베이스에는 3음 ' + h3Let(q.chord.B) + '. 화음 이름은 베이스가 아니라 근음으로 지어요.');
  if (q.kind === 'cad') { const r = h4CadRom(q.k, q.c); return t({ perfect: 'V to I: the full stop.', plagal: 'IV to I: the "Amen".', imperfect: 'Ending on V: the comma, the music waits.', interrupted: 'V to vi (VI in a minor key): the surprise, it should have gone home to I.' }[q.c] + ' Here ' + r.join(' – ') + '.', { perfect: 'V에서 I: 마침표.', plagal: 'IV에서 I: "아멘".', imperfect: 'V에서 멈춤: 쉼표, 음악이 기다려요.', interrupted: 'V에서 vi(단조에서는 VI): 깜짝, 집(I)으로 가야 했는데.' }[q.c] + ' 여기서는 ' + r.join(' – ') + '.'); }
  return t(h3Let(q.n) + ' is in ' + q.fits.map(r => r + ' (' + h4Letters(q.k, H4_DEGS(q.k).find(d => h4Rom(q.k, d, 0) === r)) + ')').join(', ') + '.', '선율 음 ' + h3Let(q.n) + ': ' + q.fits.map(r => r + '(' + h4Letters(q.k, H4_DEGS(q.k).find(d => h4Rom(q.k, d, 0) === r)) + ')').join(', ') + '에 들어 있어요.');
}
const h4PlayQ = (q) => (q.kind === 'cad' ? () => h4Play(h4CadChords(q.k, q.c)) : q.kind === 'fit' ? null : () => h4Play([q.chord]));
function h4Fig(q, shown, scr = true) {
  const ks = H4_KEYS[q.k][2];
  if (q.kind === 'deg' || q.kind === 'inv') return <div style={{maxWidth:280,margin:'0 auto'}}><SatbStaff chords={[q.chord]} ks={ks} labels={shown ? [q.answer] : null} width={200}/></div>;
  if (q.kind === 'cad') return <div style={{maxWidth:320,margin:'0 auto'}}><SatbStaff chords={h4CadChords(q.k, q.c)} ks={ks} labels={shown ? h4CadRom(q.k, q.c) : null} width={240}/></div>;
  const M = H4_MEL[q.i]; return <K4Melody notes={M.m.map(h3N)} ks={ks} hi={[q.j]} width={scr ? 300 : 360}/>;
}
function H4Pad({ kind, title, note, first, fixed, onResult }) {
  const [q, setQ] = useState(() => genH4(kind, null, fixed || first)), [pickd, setPick] = useState(null), [run, setRun] = useState(0);
  const say = (c) => { if (pickd != null) return; setPick(c); const ok = h4Ok(q, c); setRun(r => (ok ? r + 1 : 0)); if (onResult) onResult({ ok }); };
  const next = () => { setQ(genH4(kind, q)); setPick(null); };
  const play = h4PlayQ(q), shown = pickd != null, good = shown && h4Ok(q, pickd);
  return (
    <div className="try-box" style={actBox} data-h4={kind}>
      <div style={actTitle}>{title}</div>
      <div style={actNote}>{note}</div>
      <div style={{textAlign:'center',fontSize:14.5,fontWeight:800,color:BK.ink,margin:'2px 0 6px',textWrap:'balance'}}>{h4Prompt(q)}</div>
      {h4Fig(q, shown)}
      <div style={{display:'grid',gridTemplateColumns:'repeat(' + (q.kind === 'cad' ? 2 : Math.min(q.choices.length, 5)) + ',minmax(0,1fr))',gap:8,marginTop:10}}>{q.choices.map(c => <button key={c} className={'choice-btn' + (!shown ? '' : h4Ok(q, c) && (c === pickd || q.kind !== 'fit') ? ' good' : c === pickd ? ' bad' : '')} onClick={() => say(c)} style={{padding:'11px 4px',fontSize:q.kind === 'cad' ? 14.5 : 17,fontWeight:900}}>{h4Lab(q, c)}</button>)}</div>
      {shown && <div style={{marginTop:10,fontSize:13.5,color:'#4a4d86',background:'#fff',borderRadius:8,padding:'7px 10px',lineHeight:1.45}}>{(good ? t('Yes. ', '맞아요. ') + (run > 1 ? t(run + ' in a row. ', run + '번 연속. ') : '') : '') + h4Why(q)}</div>}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        {play && <button className="ghost-btn" style={spBtn} onClick={play}>{t('▶ Hear it', '▶ 들어 보기')}</button>}
        {shown && !fixed && <button className="ghost-btn" style={spBtn} onClick={next}>{t('▶ Another', '▶ 다른 것')}</button>}
      </div>
    </div>
  );
}
// ── step 4: choose a chord for every note of a melody, ending with a cadence ──
function H4HarmPad({ fixed, onResult }) {
  const [i, setI] = useState(fixed != null ? fixed : 0), [sel, setSel] = useState([]), [at, setAt] = useState(0), [res, setRes] = useState(null);
  const M = H4_MEL[i], ns = M.m.map(h3N), degs = H4_DEGS(M.k), n = ns.length, ks = H4_KEYS[M.k][2], I1 = h4Rom(M.k, 1, 0);
  const reset = (j) => { setI(j); setSel([]); setAt(0); setRes(null); };
  const choose = (deg) => { if (res) return; const s2 = sel.slice(); s2[at] = deg; setSel(s2); if (at < n - 1) setAt(at + 1); };
  const check = () => { const fit = ns.map((nt, j) => sel[j] != null && h4Has(M.k, sel[j], nt)), last = sel[n - 1], pen = sel[n - 2], cad = last === 1 && (pen === 5 || pen === 4), start = sel[0] === 1;
    const r = { fit, cad, start, ok: fit.every(Boolean) && cad && start }; setRes(r); if (onResult) onResult({ ok: r.ok }); };
  const play = () => { const td = h4Td(M.k); spPlay(ns.flatMap((nt, j) => { const d = sel[j]; if (d == null) return [{ at: j * 1.2, keys: [h3Semi(nt)], len: 1.1 }];
    const root = h4Note(M.k, td - 7, d - 1), mid = [2, 4].map(x => h4Note(M.k, td, d - 1 + x)); return [{ at: j * 1.2, keys: [h3Semi(nt), h3Semi(root), ...mid.map(h3Semi)], len: 1.1, vol: 0.1 }]; }), 72); };
  const full = sel.filter(x => x != null).length === n;
  return (
    <div className="try-box" style={actBox} data-h4="harm">
      <div style={actTitle}>{t('Chords for a melody', '선율에 화음 붙이기')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>음마다 그 음이 <b>들어 있는 화음</b>을 골라요. <b>으뜸화음으로 시작</b>하고, 끝은 <b>종지</b>: V–I(정격) 또는 IV–I(변격). 네 성부로 적는 건 선생님과 종이에서.</>
        : <>For each note, choose a chord that <b>holds it</b>. <b>Start on the tonic chord</b>, and end with a <b>cadence</b>: V–I (perfect) or IV–I (plagal). Writing the four parts comes next, on paper with your teacher.</>}</div>
      {!fixed && spChips(H4_MEL.map((x, j) => [j, h4Name(x.k) + ' ' + (j + 1)]), i, reset)}
      <K4Melody notes={ns} ks={ks} hi={res ? (res.fit.indexOf(false) >= 0 ? [res.fit.indexOf(false)] : []) : [at]} labels={ns.map((_, j) => sel[j] != null ? h4Rom(M.k, sel[j], 0) : '·')} width={320}/>
      {!res && <div style={{display:'grid',gridTemplateColumns:'repeat(' + degs.length + ',minmax(0,1fr))',gap:6,marginTop:8}}>{degs.map(d => <button key={d} className="choice-btn" onClick={() => choose(d)} style={{padding:'10px 2px',fontSize:17,fontWeight:900}}>{h4Rom(M.k, d, 0)}</button>)}</div>}
      {!res && <div style={{display:'flex',gap:4,justifyContent:'center',marginTop:6}}>{ns.map((_, j) => <button key={j} onClick={() => setAt(j)} className={'chip' + (j === at ? ' active' : '')} style={{minHeight:36,minWidth:36,padding:'2px 6px'}}>{j + 1}</button>)}</div>}
      {spMsg(res ? (res.ok ? t('It works: every chord holds its note, and it ends ' + (sel[n - 2] === 5 ? 'V–I, a perfect cadence.' : 'IV–I, a plagal cadence.'), '좋아요: 화음마다 그 음이 들어 있고, 끝은 ' + (sel[n - 2] === 5 ? 'V–I, 정격종지.' : 'IV–I, 변격종지.'))
        : !res.fit.every(Boolean) ? t('Note ' + (res.fit.indexOf(false) + 1) + ' is not in its chord.', (res.fit.indexOf(false) + 1) + '번째 음이 그 화음에 없어요.') : !res.start ? t('Start on the tonic chord, ' + I1 + '.', '으뜸화음 ' + I1 + '으로 시작해요.') : t('End with V–' + I1 + ' or IV–' + I1 + ': a cadence.', 'V–' + I1 + ' 또는 IV–' + I1 + '로 끝내요: 종지.'))
        : t('Note ' + (at + 1) + ' of ' + n + ': ' + h3Let(ns[at]) + '. Which chord?', n + '개 중 ' + (at + 1) + '번째 음: ' + h3Let(ns[at]) + '. 어떤 화음?'), res ? (res.ok ? BK.green : BK.coral) : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        {full && !res && <button className="ghost-btn" style={spBtn} onClick={check}>{t('✓ Check', '✓ 확인')}</button>}
        <button className="ghost-btn" style={spBtn} onClick={play}>{t('▶ Hear it', '▶ 들어 보기')}</button>
        {res && <button className="ghost-btn" style={spBtn} onClick={() => { setRes(null); setAt(res.fit.indexOf(false) >= 0 ? res.fit.indexOf(false) : n - 2); }}>{t('✎ Change', '✎ 고치기')}</button>}
      </div>
    </div>
  );
}
const H4_NOTE = {
  deg: [<>Grade 4 names five chords in a major key, <b>I ii IV V vi</b>, and four in a minor key, <b>i iv V VI</b>. In root position <b>the bass is the root</b>: find the bass, count up from the tonic.</>,
    <>4급은 장조의 다섯 화음 <b>I ii IV V vi</b>, 단조의 네 화음 <b>i iv V VI</b>를 알아봐요. 기본 위치에서는 <b>베이스가 근음</b>: 베이스를 찾아 으뜸음부터 세요.</>],
  inv: [<>First inversion, <b>b</b>: <b>the 3rd is in the bass</b>. Stack the notes in 3rds to find the root, and name the chord by its root: Ib, iib, IVb, Vb, vib.</>,
    <>첫째 자리바꿈 <b>b</b>: <b>3음이 베이스</b>에 있어요. 음을 3도로 쌓아 근음을 찾고, 근음으로 이름 지어요: Ib, iib, IVb, Vb, vib.</>],
  cad: [<>The four cadences: <b>perfect</b> V–I (a full stop), <b>plagal</b> IV–I (the "Amen"), <b>imperfect</b> ending on V (a comma), <b>interrupted</b> V–vi (the surprise).</>,
    <>네 가지 종지: <b>정격</b> V–I(마침표), <b>변격</b> IV–I("아멘"), <b>반종지</b> V에서 멈춤(쉼표), <b>거짓종지</b> V–vi(깜짝).</>],
  fit: [<>To harmonise a melody, give each note a chord <b>that holds it</b>. Most notes fit two or three chords: choose, and save V–I or IV–I for the end.</>,
    <>선율에 화음을 붙이려면 음마다 <b>그 음이 들어 있는</b> 화음을 줘요. 대부분의 음은 두세 화음에 들어 있어요: 골라 쓰고, 끝은 V–I나 IV–I로.</>],
};
const h4NoteT = (k) => (LANG === 'ko' ? H4_NOTE[k][1] : H4_NOTE[k][0]);
const H4_STEP = { deg: ['Chords on every degree', '음계 위의 화음'], inv: ['First inversions', '첫째 자리바꿈'], cad: ['The four cadences', '네 가지 종지'], fit: ['Chords for a melody', '선율에 화음 붙이기'] };
const h4StepT = (k) => t(H4_STEP[k][0], H4_STEP[k][1]);
const H4_FIRST = { deg: { k: 'G', deg: 2 }, inv: { k: 'C', deg: 4 }, cad: { k: 'C', c: 'interrupted' }, fit: { i: 0, j: 2 } };
const H4Step = ({ kind, fixed, onResult }) => kind === 'harm' ? <H4HarmPad fixed={fixed} onResult={onResult}/> : <H4Pad kind={kind} title={h4StepT(kind)} note={h4NoteT(kind)} first={H4_FIRST[kind]} fixed={fixed} onResult={onResult}/>;

// ── the pictures on paper ──
const h4PicDeg = () => ({ shapes: [{ k: 'raw', svg: ['I', 'ii', 'IV', 'V', 'vi'].map((r, i) => '<text x="' + (6 + i * 15) + '" y="27" font-size="11" font-weight="900" fill="' + (i === 1 ? '#e4572e' : '#26296b') + '" font-family="Inter, sans-serif">' + r + '</text>').join('') }], vb: [0, 0, 80, 44] });
const h4PicInv = () => ({ shapes: [{ k: 'raw', svg: lsCircleSvg(30, 34, 6, 'play', '3') + lsCircleSvg(30, 20, 6, 'beat', '5') + lsCircleSvg(30, 8, 6, 'beat', '1') + '<text x="44" y="38" font-size="12" font-weight="900" fill="#e4572e" font-family="Inter, sans-serif">b</text>' }], vb: [0, 0, 70, 44] });
const h4PicCad = () => ({ shapes: [{ k: 'raw', svg: '<text x="4" y="28" font-size="14" font-weight="900" fill="#26296b" font-family="Inter, sans-serif">V</text><path d="M20 23 L34 23 M30 19 L34 23 L30 27" fill="none" stroke="#e4572e" stroke-width="2"/><text x="40" y="28" font-size="14" font-weight="900" fill="#26296b" font-family="Inter, sans-serif">I</text><circle cx="58" cy="24" r="3.2" fill="#26296b"/>' }], vb: [0, 0, 70, 44] });
const h4PicFit = () => ({ shapes: [{ k: 'raw', svg: [[10, 18], [26, 14], [42, 22], [58, 26]].map(([x, y], i) => lsCircleSvg(x, y, 5, i === 1 ? 'play' : 'beat', '')).join('') + ['I', 'IV', 'V', 'I'].map((r, i) => '<text x="' + (5 + i * 16) + '" y="42" font-size="9" font-weight="900" fill="#e4572e" font-family="Inter, sans-serif">' + r + '</text>').join('') }], vb: [0, 0, 70, 44] });

function h4LbPages(scr = false) {
  const ch = 'harmony-4', kinds = ['deg', 'inv', 'cad', 'harm'];
  const pen = (x) => <PenArt shapes={x.shapes} vb={x.vb} style={{width:90}}/>;
  const checks4 = [[h4PicDeg(), t('I name the chords on I, II, IV, V and VI in four parts', '네 성부의 I, II, IV, V, VI 화음 이름을 말해요')], [h4PicInv(), t('I tell a first inversion by its bass, and name it by its root', '베이스로 첫째 자리바꿈을 알아보고, 근음으로 이름을 지어요')],
    [h4PicCad(), t('I name and write the four cadences', '네 가지 종지의 이름을 말하고 적어요')], [h4PicFit(), t('I choose chords for a melody and end with a cadence', '선율에 화음을 고르고, 종지로 끝내요')]];
  const stepT = (k) => (k === 'harm' ? h4StepT('fit') : h4StepT(k));
  const toc = kinds.map((k, i) => [stepT(k), i + 2]).concat([[t('My four checks', '나의 네 가지 확인'), 6]]);
  const still = (kind) => { if (kind === 'harm') { const M = H4_MEL[0], sel = [1, 4, 2, 1, 5, 1]; return <LbPic h={150}><div style={{width:'100%',maxWidth:560,margin:'0 auto'}}><K4Melody notes={M.m.map(h3N)} ks={H4_KEYS[M.k][2]} labels={sel.map(d => h4Rom(M.k, d, 0))} width={scr ? 300 : 380}/></div></LbPic>; }
    if (kind === 'cad') return <LbPic h={170}><div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:10,width:'100%',maxWidth:680,margin:'0 auto'}}>{H4_CADS.map(c => <div key={c}><div style={{textAlign:'center',fontSize:12.5,fontWeight:900,color:BK.ink}}>{h4CadName(c)}</div><SatbStaff chords={h4CadChords('C', c)} ks={[null, 0]} labels={h4CadRom('C', c)} width={200}/></div>)}</div></LbPic>;
    const inv = kind === 'inv' ? 1 : 0; return <LbPic h={160}><div style={{display:'grid',gridTemplateColumns:scr ? 'repeat(3,1fr)' : 'repeat(5,1fr)',gap:4,width:'100%',maxWidth:680,margin:'0 auto'}}>{H4_DEGS('C').map(d => <div key={d}><SatbStaff chords={[h4Chord('C', d, inv)]} ks={[null, 0]} labels={[h4Rom('C', d, inv)]} width={120}/></div>)}</div></LbPic>; };
  const TEACH = {
    deg: t('Theory of Music Grade 4: the recognition of chords on I, II, IV, V and VI in major keys and I, IV, V and VI in minor keys, root position and first inversion, in keys up to four sharps or four flats, in four-part vocal style. Here each chord is voiced by rule: the root doubled, close position above. The chord names follow the earlier chapters (small letters for minor chords); the syllabus prints them all as capitals: use whichever your papers use.', '이론 4급: 장조의 I, II, IV, V, VI와 단조의 I, IV, V, VI 화음을 기본 위치와 첫째 자리바꿈으로, 조표 샵·플랫 네 개까지, 네 성부 성악 양식으로 알아봐요. 여기서 화음은 규칙대로: 근음을 겹치고 위는 밀집 배치. 화음 이름은 앞 챕터처럼(단3화음은 소문자); 실라버스는 모두 대문자로 적어요: 쓰시는 시험지를 따르세요.'),
    inv: t('First inversions (Ib, IIb, IVb, Vb, VIb): the 3rd in the bass. The usual slip is to name the chord from its bass note (Ib called iii). Here the upper voices hold the root and the 5th, so the leading note is never doubled in Vb.', '첫째 자리바꿈(Ib, IIb, IVb, Vb, VIb): 3음이 베이스. 흔한 실수는 베이스 음으로 화음 이름을 짓는 것(Ib를 iii로). 여기서 위 성부는 근음과 5음을 가져서 Vb의 이끎음이 겹치지 않아요.'),
    cad: t('The writing and recognition of the four principal cadences in the same keys, four-part vocal style: perfect V–I, plagal IV–I, imperfect ending on V (here I–V or IV–V), interrupted V–VI (the 3rd of VI doubled). Every cadence here was checked for range, spacing and parallel 5ths and octaves.', '같은 조에서 네 가지 주요 종지를 네 성부로 적고 알아봐요: 정격 V–I, 변격 IV–I, 반종지 V에서 멈춤(여기서는 I–V나 IV–V), 거짓종지 V–VI(VI의 3음을 겹쳐요). 여기 모든 종지는 음역, 간격, 연속 5도와 8도를 확인했어요.'),
    harm: t('The harmonisation of a simple melody of not more than six bars, major or minor, up to four sharps or flats, four-part vocal style. The app does the first decision, choosing a chord that holds each note and ending with a cadence; writing the four parts is on paper with you.', '6마디 이하의 간단한 선율에 화음 붙이기, 장조나 단조, 샵·플랫 네 개까지, 네 성부 성악 양식. 앱은 첫 결정, 음마다 그 음이 든 화음을 고르고 종지로 끝내기를 해요. 네 성부로 적는 건 선생님과 종이에서.'),
  };
  const SAY = { deg: t('Root position: the bass is the root.', '기본 위치: 베이스가 근음.'), inv: t('First inversion: the 3rd in the bass; name it by its root.', '첫째 자리바꿈: 3음이 베이스, 이름은 근음으로.'), cad: t('Full stop, Amen, comma, surprise.', '마침표, 아멘, 쉼표, 깜짝.'), harm: t('A chord that holds the note; a cadence at the end.', '그 음이 든 화음, 끝에는 종지.') };
  const PIANO = {
    deg: [t('In G major play I, ii, IV, V, vi with the left hand: root at the bottom.', 'G장조에서 왼손으로 I, ii, IV, V, vi: 근음을 맨 아래.'), t('Sing each root, then name the chord.', '근음을 부르고, 화음 이름을 말해요.'), t('Now in A minor: i, iv, V, VI.', '이번엔 A단조: i, iv, V, VI.')],
    inv: [t('Play C major I, then Ib: the E goes to the bottom.', 'C장조 I, 그다음 Ib: E가 맨 아래로.'), t('Play IVb and Vb: which note is in the bass?', 'IVb와 Vb: 베이스는 어떤 음?'), t('Hear how the first inversion feels lighter.', '첫째 자리바꿈이 더 가볍게 들리는지 들어 봐요.')],
    cad: [t('Play V–I in C: the full stop.', 'C에서 V–I: 마침표.'), t('Play IV–I, then I–V, then V–vi.', 'IV–I, 그다음 I–V, 그다음 V–vi.'), t('Close your eyes: your teacher plays one; which?', '눈을 감아요: 선생님이 하나를 치면, 어느 것?')],
    harm: [t('Sing the melody, then play it.', '선율을 부르고, 쳐요.'), t('Play the bass roots of your chords under it.', '고른 화음의 근음을 그 아래에 쳐요.'), t('Write the four parts on paper with your teacher.', '선생님과 종이에 네 성부로 적어요.')],
  };
  return [
    <LbPage key="1" no={1} chId={ch} teacher={<>{t('Theory of Music Grade 4 harmony, one step each: the chords on I, II, IV, V and VI, root position and first inversion, in four parts; the four principal cadences; choosing chords for a melody. Keys up to four sharps or four flats.', '이론 4급 화성을 한 단계씩: I, II, IV, V, VI 화음, 기본 위치와 첫째 자리바꿈, 네 성부; 네 가지 주요 종지; 선율에 화음 고르기. 조표 샵·플랫 네 개까지.')}</>}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:48,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{bkChapterName(ch)}</div>
      </div></LbOnly>
      {still('cad')}
      <LbSay size={18}>{t('Grade 4 harmony: five chords in a major key, four in a minor, their first inversions, four ways to end a phrase, and chords for a melody.', '4급 화성: 장조의 화음 다섯, 단조의 넷, 첫째 자리바꿈, 프레이즈를 끝내는 네 가지, 그리고 선율의 화음.')}</LbSay>
      <div className="lb-toc" style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>
        <LbOnly print><div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('In this chapter', '이 챕터에서는')}</div>
          {toc.map(([n, p]) => <div key={p} className="lb-toc-row" style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:14.5,padding:'5px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkGoal(15)}{n}</span><span style={{color:BK.muted,fontWeight:700}}>{p}</span></div>)}
        </div></LbOnly>
        <div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 챕터를 마치면')}</div>
          {checks4.map(([, x], i) => <div key={i} style={{display:'flex',alignItems:'flex-start',gap:9,fontSize:14.5,padding:'5px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}>{bkGoal(15)}<span>{x.replace(/^I /, '')}</span></div>)}
        </div>
      </div>
      <LbOnly print><LbDrillStrip id={ch}/></LbOnly>
    </LbPage>,
    ...kinds.map((kind, i) => <LbPage key={kind} no={i + 2} chId={ch} kicker={t('Step ' + (i + 1), (i + 1) + '단계')} title={stepT(kind)} teacher={<>{TEACH[kind]}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=' + (i + 1))}>
      <LbLive still={still(kind)} live={<H4Step kind={kind}/>}/>
      <LbSay>{h4NoteT(kind === 'harm' ? 'fit' : kind)}</LbSay>
      <LbPiano steps={PIANO[kind].map((x, j) => <React.Fragment key={j}>{x}</React.Fragment>)}/>
      <LbRemember>{SAY[kind]}</LbRemember>
    </LbPage>),
    <LbPage key="6" no={6} chId={ch} kicker={t('Check-up', '점검')} title={t('My four checks', '나의 네 가지 확인')}
      teacher={<>{t('On paper and at the piano, in keys up to four sharps or flats. For the cadences, have the child write one of each in four parts.', '종이와 피아노에서, 샵·플랫 네 개까지의 조로. 종지는 네 가지를 하나씩 네 성부로 적게 해 주세요.')}</>}>
      <LbSay>{t('Tick each one: not yet, nearly, or got it!', '하나씩 표시해요: 아직, 거의, 됐어요!')}</LbSay>
      <LbLive still={<LbStageRows big rows={checks4.map(([a, txt]) => [pen(a), txt])}/>} live={<FiveChecks376 rows={checks4} storeKey="pb_h4_four"/>}/>
    </LbPage>,
  ];
}
function Harmony4LessonBook() { return <>{h4LbPages(false)}</>; }
function H4Learn({ onStart }) {
  const pages = h4LbPages(true), opener = pages[0];
  return (
    <Lesson id="harmony-4" title={bkChapterName('harmony-4')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="harmony-4"><div className="lb-screen lb-open" style={{display:'flex',flexDirection:'column',gap:12,margin:'0 0 8px'}}>{lbWordsFirst(opener.props.children)}</div></BkChapterCtx.Provider></LbScreenCtx.Provider>}>
      {pages.slice(1).map((pg, i) => <Step key={i} title={pg.props.title}><LbScreenPage page={pg}/></Step>)}
    </Lesson>
  );
}
// ── the drill ──
const H4_LEVELS = [
  { n: 1, label: 'Which chord? Root position', kind: 'deg', time: 15 },
  { n: 2, label: 'First inversions: which chord?', kind: 'inv', time: 18 },
  { n: 3, label: 'Which cadence?', kind: 'cad', time: 18 },
  { n: 4, label: 'Which chord holds the melody note?', kind: 'fit', time: 15 },
];
Object.assign(LEVEL_KO, { 'Which chord? Root position': '어떤 화음? 기본 위치', 'First inversions: which chord?': '첫째 자리바꿈: 어떤 화음?', 'Which cadence?': '어떤 종지?', 'Which chord holds the melody note?': '선율 음이 든 화음은?' });
const genH4Question = (lv, prev) => genH4(lv.kind, prev);
const h4AnswerLabel = (q) => (q.kind === 'fit' ? q.fits.join(' / ') : h4Lab(q, q.answer));
function H4Question({ q, given, locked, onAnswer, pixel }) {
  const done = !!given, play = h4PlayQ(q);
  const btnCls = pixel ? 'pixel-choice' : 'choice-btn', cls = (c) => btnCls + (!done ? '' : h4Ok(q, c) && (c === given.ans || q.kind !== 'fit') ? ' good' : given.ans === c ? ' bad' : '');
  return (<div>
    <p style={pixel ? {fontSize:11.5,textAlign:'center'} : {fontSize:15,fontWeight:700,textAlign:'center',margin:'0 0 8px',color:'var(--muted)',textWrap:'balance'}}>{h4Prompt(q)}</p>
    {h4Fig(q, done)}
    {play && <div style={{textAlign:'center',margin:'6px 0 0'}}><button className={pixel ? 'pixel-btn' : 'ghost-btn'} style={{minHeight:44}} onClick={() => { stopClicks(); play(); }}>{t('▶ Hear it', '▶ 들어 보기')}</button></div>}
    <div style={{display:'grid',gridTemplateColumns:'repeat(' + (q.kind === 'cad' ? 2 : Math.min(q.choices.length, 5)) + ',minmax(0,1fr))',gap:8,marginTop:10}}>{q.choices.map(c => <button key={c} disabled={locked} className={cls(c)} style={{padding:'12px 4px',fontSize:q.kind === 'cad' ? 14.5 : 17,fontWeight:900}} onClick={() => { if (locked || done) return; stopClicks(); onAnswer(c); }}>{h4Lab(q, c)}</button>)}</div>
    {done && !pixel && <div style={{marginTop:10,fontSize:13.5,color:'#4a4d86',background:'#fff',borderRadius:8,padding:'7px 10px',lineHeight:1.45}}>{h4Why(q)}</div>}
  </div>);
}
Object.assign(HARMONY_4_DRILL, { levels: H4_LEVELS, generate: genH4Question, check: (q, ans) => ans !== null && ans !== undefined && h4Ok(q, ans), answerLabel: h4AnswerLabel, Question: H4Question, Learn: H4Learn });
// the teacher's copy
function H4Teacher() {
  const pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="harmony-4" teacher>{content}</WbPage>);
  const cad = (k) => h4Name(k) + ': ' + H4_CADS.map(c => H4_CADN[c][0] + ' ' + h4CadRom(k, c).join('–') + ' (' + H4_CAD[k][c].join(' / ') + ')').join('; ');
  P(<>
    <div style={{fontFamily:LB_SERIF,fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('harmony-4')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 12px',lineHeight:1.5}}>Theory of Music Grade 4, harmony. Keys up to four sharps or flats. Chords are listed soprano, alto, tenor, bass. Every cadence was checked for range, spacing, and parallel 5ths and octaves.</div>
    <TcBlock page={2} title="Chords on every degree" answers={<>{tcAns('C MAJOR, ROOT POSITION', H4_DEGS('C').map(d => h4Rom('C', d, 0) + ' ' + h4Letters('C', d)))}{tcAns('A MINOR', H4_DEGS('Am').map(d => h4Rom('Am', d, 0) + ' ' + h4Letters('Am', d)))}</>}
      watch="Counting from C in every key. Count from the key's tonic: in G major, A–C–E is ii."
      say="“Root position: the bass is the root.”"/>
    <TcBlock page={3} title="First inversions" answers={<>{tcAns('C MAJOR, FIRST INVERSION: THE BASS', H4_DEGS('C').map(d => h4Rom('C', d, 1) + ': ' + h3Let(h4Chord('C', d, 1).B)))}</>}
      watch="Naming from the bass note (Ib called iii, IVb called vi). Stack in 3rds to find the root."
      say="“First inversion: the 3rd in the bass; name it by its root.”"/>
  </>);
  P(<>
    <TcBlock page={4} title="The four cadences" answers={<div style={{fontSize:11,color:BK.ink,lineHeight:1.55}}>{['C', 'G', 'F', 'D', 'Bb', 'Am', 'Em', 'Dm'].map(k => <div key={k} style={{marginBottom:2}}>{cad(k)}</div>)}</div>}
      watch="Interrupted heard as perfect: listen for the bass going up a step to vi instead of down to I."
      say="“Full stop, Amen, comma, surprise.”"/>
    <TcBlock page={5} title="Chords for a melody" answers={<>{tcAns('ONE WAY TO HARMONISE EACH (others work)', H4_MEL.map(M => h4Name(M.k) + ': ' + M.m.map(x => h3Let(h3N(x))).join(' ')))}</>}
      watch="A chord that does not hold its note, or a melody that ends without a cadence."
      say="“A chord that holds the note; a cadence at the end.”"/>
    <TcBlock page={6} title="My four checks" answers={<div style={{fontSize:12,color:BK.ink,lineHeight:1.5}}>On paper and at the piano. One cadence of each kind written in four parts.</div>}/>
  </>);
  return <>{pages}</>;
}
TEACHER_COPIES['harmony-4'] = H4Teacher;
'''
rep("""TEACHER_COPIES['keys-4'] = K4Teacher;""", """TEACHER_COPIES['keys-4'] = K4Teacher;""" + CH)

HOME = r'''
// ══ Build AU: Chords and Cadences, Grade 4 on the Home (Chords, before Intervals and chords further) ══
LBH_FN['harmony-4'] = (s) => h4LbPages(s);
const h4HomeQ = (kind) => (n, prev) => { const q = genH4(kind, prev), p = h4Prompt(q), w = h4Why(q);
  return { kind: 'choice', cols: kind === 'cad' ? 2 : Math.min(q.choices.length, 5), key: q.key, prompt: [p, p], opts: q.choices.map(c => ({ id: c, label: () => h4Lab(q, c) })), ans: q.answer, ok: (v) => h4Ok(q, v),
    play: h4PlayQ(q), fig: (c) => ({ mid: h4Fig(q, !!c.res) }), yes: ['Yes. ' + w, '맞아요. ' + w], no: [w, w] }; };
const h4HomeAdd = (id, i, en, ko, benEn, bko, make) => lbhAdd(id, 'p-chords', 'pitch', en, ko, benEn, bko, lbhSpec('harmony-4', i, { make }));
h4HomeAdd('h4-deg', 1, 'Chords on every degree', '음계 위의 화음', 'I ii IV V vi, and i iv V VI, in four parts.', '네 성부로 I ii IV V vi, 그리고 i iv V VI.', h4HomeQ('deg'));
h4HomeAdd('h4-inv', 2, 'First inversions', '첫째 자리바꿈', 'The 3rd in the bass; name it by its root.', '3음이 베이스, 이름은 근음으로.', h4HomeQ('inv'));
h4HomeAdd('h4-cad', 3, 'The four cadences', '네 가지 종지', 'Perfect, plagal, imperfect, interrupted.', '정격, 변격, 반종지, 거짓종지.', h4HomeQ('cad'));
h4HomeAdd('h4-fit', 4, 'Chords for a melody', '선율에 화음 붙이기', 'A chord that holds each note.', '음마다 그 음이 든 화음.', h4HomeQ('fit'));
'''
rep("""
lbhAdd('rb-finger', 'r-beat', 'rhythm', 'The beat in your fingers'""", HOME + """
lbhAdd('rb-finger', 'r-beat', 'rhythm', 'The beat in your fingers'""")
rep("""const LESSON_BOOKS = { 'keys-4': Keys4LessonBook,""", """const LESSON_BOOKS = { 'harmony-4': Harmony4LessonBook, 'keys-4': Keys4LessonBook,""")
rep("""const LB_PAGE_FNS = { 'keys-4': k4LbPages,""", """const LB_PAGE_FNS = { 'harmony-4': h4LbPages, 'keys-4': k4LbPages,""")
rep("""const HOUSE_ICONS = {"keys-4": """, """const HOUSE_ICONS = {"harmony-4": "<ellipse cx=\\"16\\" cy=\\"35\\" rx=\\"5.5\\" ry=\\"4\\" transform=\\"rotate(-20 16 35)\\" fill=\\"#26296b\\"/><ellipse cx=\\"16\\" cy=\\"27\\" rx=\\"5.5\\" ry=\\"4\\" transform=\\"rotate(-20 16 27)\\" fill=\\"#26296b\\"/><ellipse cx=\\"16\\" cy=\\"19\\" rx=\\"5.5\\" ry=\\"4\\" transform=\\"rotate(-20 16 19)\\" fill=\\"#26296b\\"/><ellipse cx=\\"32\\" cy=\\"31\\" rx=\\"5.5\\" ry=\\"4\\" transform=\\"rotate(-20 32 31)\\" fill=\\"#e4572e\\" stroke=\\"#e4572e\\"/><ellipse cx=\\"32\\" cy=\\"23\\" rx=\\"5.5\\" ry=\\"4\\" transform=\\"rotate(-20 32 23)\\" fill=\\"#e4572e\\" stroke=\\"#e4572e\\"/><ellipse cx=\\"32\\" cy=\\"15\\" rx=\\"5.5\\" ry=\\"4\\" transform=\\"rotate(-20 32 15)\\" fill=\\"#e4572e\\" stroke=\\"#e4572e\\"/>", "keys-4": """)
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
