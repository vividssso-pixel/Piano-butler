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
def after_line(prefix, text):   # insert text after the one line that starts with prefix
    global s
    lines = s.split('\n'); hits = [i for i, x in enumerate(lines) if x.startswith(prefix)]
    assert len(hits) == 1, (len(hits), prefix[:80])
    lines.insert(hits[0] + 1, text.strip('\n')); s = '\n'.join(lines)

# Build BB (board call 23, the third Grade 5 room): Keys and Intervals, Grade 5. Theory of Music Grade 5 (Manual of Syllabuses
# 2026, read 27 Oct): the recognition and writing of all the major and minor scales (both forms) and their key signatures; all
# diatonic and chromatic intervals and their inversions, in treble and bass clefs, with or without key signatures; recognition in
# melodies of modulation to the dominant, subdominant, or relative major or minor.

# ── registrations ──
rep("""const KEYS_4_DRILL = { id: 'keys-4', label: 'Keys and Intervals, Grade 4' };   // Build AT""",
    """const KEYS_4_DRILL = { id: 'keys-4', label: 'Keys and Intervals, Grade 4' };   // Build AT
const KEYS_5_DRILL = { id: 'keys-5', label: 'Keys and Intervals, Grade 5' };   // Build BB""")
rep("""  { id: 'keys-4', label: 'Keys and Intervals, Grade 4', concept: KEYS_4_DRILL, track: 'start' },   // Build AT""",
    """  { id: 'keys-4', label: 'Keys and Intervals, Grade 4', concept: KEYS_4_DRILL, track: 'start' },   // Build AT
  { id: 'keys-5', label: 'Keys and Intervals, Grade 5', concept: KEYS_5_DRILL, track: 'start' },   // Build BB""")
rep("""'keys-4': '조와 음정, Grade 4'""", """'keys-4': '조와 음정, Grade 4', 'keys-5': '조와 음정, Grade 5'""")
rep("""'keys-4': 'p-scales'""", """'keys-4': 'p-scales', 'keys-5': 'p-scales'""")
rep("""'keys-4': ['key-signatures', 'harmony-23']""", """'keys-4': ['key-signatures', 'harmony-23'], 'keys-5': ['keys-4']""")
rep("""'keys-4': ['Keys 4', '조 4']""", """'keys-4': ['Keys 4', '조 4'], 'keys-5': ['Keys 5', '조 5']""")
rep("""  'keys-4': 'keys intervals grade 4""", """  'keys-5': 'keys intervals grade 5 theory every key signature seven sharps flats c sharp c flat enharmonic melodic minor harmonic both forms double sharp augmented diminished chromatic intervals inversion modulation dominant subdominant relative',
  'keys-4': 'keys intervals grade 4""")

# ── shared pieces opened up: the double sharp on a melody staff; the augmented and diminished qualities ──
rep_in("function K4Melody({ notes, ks = [null, 0], hi = [], width = 320, labels = null }) {", [
    ("{marks[i] && (nt.acc > 0 ? <SharpShape x={x - 16} y={y} color={col}/>", "{marks[i] && (nt.acc > 1 ? <DoubleSharpShape x={x - 14} y={y} color={col}/> : nt.acc > 0 ? <SharpShape x={x - 16} y={y} color={col}/>"),
])

CH = r'''
// ─── Chapter: Keys and Intervals, Grade 5 (Build BB, 2026-10-27; board call 23, the third Grade 5 room) ───
// Every key up to seven sharps or flats (C♯ and C♭ major; G♯, D♯, A♯, E♭ and A♭ minor are new); both forms of the minor, the
// melodic written up and down (raising a sharp makes a double sharp, raising a flat a natural); augmented and diminished intervals;
// inverting every interval; modulation to the dominant, the subdominant, or the relative major or minor.
Object.assign(H3_QW, { A: ['augmented', '증'], d: ['diminished', '감'] });
const K5M = {   // minor keys for the two forms: tr = the lower tonic on the treble staff; r = that key, semitones from middle C
  Gsm: { en: 'G♯ minor', ko: 'G♯단조', ks: ['sharp', 5], tr: 'G#4', r: 8 },
  Dsm: { en: 'D♯ minor', ko: 'D♯단조', ks: ['sharp', 6], tr: 'D#4', r: 3 },
  Asm: { en: 'A♯ minor', ko: 'A♯단조', ks: ['sharp', 7], tr: 'A#3', r: -2 },
  Ebm: { en: 'E♭ minor', ko: 'E♭단조', ks: ['flat', 6], tr: 'Eb4', r: 3 },
  Abm: { en: 'A♭ minor', ko: 'A♭단조', ks: ['flat', 7], tr: 'Ab3', r: -4 },
  Csm: { en: 'C♯ minor', ko: 'C♯단조', ks: ['sharp', 4], tr: 'C#4', r: 1 },
  Bbm: { en: 'B♭ minor', ko: 'B♭단조', ks: ['flat', 5], tr: 'Bb3', r: -2 },
};
const K5M_IDS = ['Gsm', 'Dsm', 'Asm', 'Ebm', 'Abm', 'Csm', 'Bbm'], K5M_NEW = ['Gsm', 'Dsm', 'Asm', 'Ebm', 'Abm'];
const k5Name = (k) => t(K5M[k].en, K5M[k].ko);
const k5Sig = (ks) => { const out = {}; if (ks[0]) (ks[0] === 'sharp' ? SHARP_ORDER : FLAT_ORDER).slice(0, ks[1]).forEach(a => { out[a[0]] = ks[0] === 'sharp' ? 1 : -1; }); return out; };
// the note x steps above the lower tonic: 'nat' (the key signature), 'har' (the 7th raised), 'mel' (going up: the 6th and 7th raised)
const k5MNote = (k, x, form) => { const c = K5M[k], t0 = h3N(c.tr), d = t0.d + x, L = H3_L[((d % 7) + 7) % 7], j = ((x % 7) + 7) % 7; let a = k5Sig(c.ks)[L] || 0;
  if ((form === 'har' && j === 6) || (form === 'mel' && (j === 5 || j === 6))) a += 1; return { d, acc: a }; };
const K5_ACC = { 2: '𝄪', 1: '♯', 0: '', '-1': '♭', '-2': '𝄫' };
const k5Let = (n, sig) => { const L = H3_L[((n.d % 7) + 7) % 7]; return L + (n.acc === 0 && sig && sig[L] ? '♮' : K5_ACC[n.acc]); };   // a natural shown where it cancels the key signature
const k5Up = (n) => { const d = n.d + 1, w = { d, acc: 0 }; return { d, acc: ivMidi(n) - ivMidi(w) }; };   // the same key, the next letter up
// intervals: the number from the letters, the quality from the semitones
const K5_BASE = { 1: 0, 2: 2, 3: 4, 4: 5, 5: 7, 6: 9, 7: 11, 8: 12 };
const k5Iv = (lo, hi) => { const n = hi.d - lo.d + 1, s = ivMidi(hi) - ivMidi(lo), df = s - K5_BASE[n];
  return ([1, 4, 5, 8].includes(n) ? { '-1': 'd', 0: 'P', 1: 'A' } : { '-2': 'd', '-1': 'm', 0: 'M', 1: 'A' })[df] + n; };
const k5IvName = (id) => h3IvName(id[0], Number(id.slice(1)));
const k5Inv = (id) => ({ M: 'm', m: 'M', P: 'P', A: 'd', d: 'A' })[id[0]] + (9 - Number(id.slice(1)));
const k5AnA = (s) => (/^[aeiou]/i.test(s) ? 'an ' : 'a ') + s;
const K5_AD = [['C4', 'F#4'], ['F4', 'B4'], ['B3', 'F4'], ['C#4', 'G4'], ['Eb4', 'B4'], ['C4', 'G#4'], ['F4', 'G#4'], ['Bb4', 'C#5'], ['G#4', 'F5'], ['C#4', 'Bb4'], ['B3', 'Eb4'], ['F#4', 'Bb4'], ['Ab4', 'F#5'], ['D4', 'B4'], ['E4', 'C5']];
const K5_IVC = { A4: ['d5', 'P4'], d5: ['A4', 'P5'], A5: ['m6', 'P5'], A2: ['m3', 'M2'], d7: ['M6', 'm7'], d4: ['M3', 'P4'], A6: ['m7', 'M6'], M6: ['d7', 'm6'], m6: ['A5', 'M6'] };   // the same keys under another number; the plain interval of that number
const k5Pair = (i, clef) => K5_AD[i].map(h3N).map(n => (clef === 'bass' ? { d: n.d - 7, acc: n.acc } : n));
// the key signatures asked: the new keys, and the five- and six-sharp and -flat ones beside them
const K5_SIGQ = [['sharp', 7, false], ['flat', 7, false], ['sharp', 6, false], ['flat', 6, false], ['sharp', 5, true], ['sharp', 6, true], ['sharp', 7, true], ['flat', 6, true], ['flat', 7, true]];
const k5Enh = (ty, n, minor) => (n >= 5 ? k4SigId(ty === 'sharp' ? 'flat' : 'sharp', 12 - n, minor) : null);   // from five on, the same keys under the other name
// modulation: short melodies (each note one beat) from a home key to its dominant, subdominant or relative; clue = the note that tells
const K5_MOD = [
  { h: 'C', ks: [null, 0], dom: 'G', sub: 'F', rel: 'Am', m: ['E4', 'G4', 'C5', 'B4', 'A4', 'F#4', 'A4', 'G4'], to: 'dom', clue: 5 },
  { h: 'C', ks: [null, 0], dom: 'G', sub: 'F', rel: 'Am', m: ['C5', 'G4', 'E4', 'C5', 'Bb4', 'A4', 'G4', 'F4'], to: 'sub', clue: 4 },
  { h: 'C', ks: [null, 0], dom: 'G', sub: 'F', rel: 'Am', m: ['G4', 'E4', 'C5', 'B4', 'A4', 'G#4', 'B4', 'A4'], to: 'rel', clue: 5 },
  { h: 'G', ks: ['sharp', 1], dom: 'D', sub: 'C', rel: 'Em', m: ['B4', 'D5', 'G5', 'F#5', 'E5', 'C#5', 'E5', 'D5'], to: 'dom', clue: 5 },
  { h: 'G', ks: ['sharp', 1], dom: 'D', sub: 'C', rel: 'Em', m: ['G4', 'B4', 'D5', 'G5', 'F5', 'E5', 'D5', 'C5'], to: 'sub', clue: 4 },
  { h: 'F', ks: ['flat', 1], dom: 'C', sub: 'B♭', rel: 'Dm', m: ['A4', 'C5', 'F5', 'E5', 'D5', 'B4', 'D5', 'C5'], to: 'dom', clue: 5 },
  { h: 'F', ks: ['flat', 1], dom: 'C', sub: 'B♭', rel: 'Dm', m: ['F4', 'A4', 'C5', 'F5', 'Eb5', 'D5', 'C5', 'Bb4'], to: 'sub', clue: 4 },
  { h: 'D', ks: ['sharp', 2], dom: 'A', sub: 'G', rel: 'Bm', m: ['A4', 'D5', 'F#5', 'D5', 'C5', 'B4', 'A4', 'G4'], to: 'sub', clue: 4 },
  { h: 'Am', ks: [null, 0], dom: 'Em', sub: 'Dm', rel: 'C', m: ['A4', 'G#4', 'A4', 'C5', 'E5', 'D5', 'G4', 'C5'], to: 'rel', clue: 6 },
  { h: 'Am', ks: [null, 0], dom: 'Em', sub: 'Dm', rel: 'C', m: ['A4', 'C5', 'E5', 'G#4', 'A4', 'B4', 'D#5', 'E5'], to: 'dom', clue: 6 },
  { h: 'Am', ks: [null, 0], dom: 'Em', sub: 'Dm', rel: 'C', m: ['A4', 'C5', 'E5', 'G#4', 'A4', 'Bb4', 'C#5', 'D5'], to: 'sub', clue: 6 },
  { h: 'Em', ks: ['sharp', 1], dom: 'Bm', sub: 'Am', rel: 'G', m: ['E4', 'G4', 'B4', 'D#5', 'E5', 'C5', 'G#4', 'A4'], to: 'sub', clue: 6 },
  { h: 'Dm', ks: ['flat', 1], dom: 'Am', sub: 'Gm', rel: 'F', m: ['D5', 'C#5', 'D5', 'F5', 'A5', 'G5', 'C5', 'F5'], to: 'rel', clue: 6 },
  { h: 'Dm', ks: ['flat', 1], dom: 'Am', sub: 'Gm', rel: 'F', m: ['D5', 'F5', 'A5', 'C#5', 'D5', 'Eb5', 'F#5', 'G5'], to: 'sub', clue: 6 },
];
const k5ModNotes = (i) => K5_MOD[i].m.map(h3N);
const K5_WHERE = { dom: ['the dominant', '딸림조'], sub: ['the subdominant', '버금딸림조'] };
const k5ModWhy = (i) => { const c = K5_MOD[i], ns = k5ModNotes(i), nt = ns[c.clue], nm = h3Let(nt) + (nt.acc === 0 ? '♮' : ''), dest = c[c.to], last = ns[ns.length - 1], L = h3Let(last), minor = c.h.endsWith('m');
  const lead = ((h3Semi(nt) + 1 - h3Semi(last)) % 12 + 12) % 12 === 0, wh = c.to === 'rel' ? [minor ? 'the relative major' : 'the relative minor', '나란한조'] : K5_WHERE[c.to];
  if (minor && c.to === 'rel') return t(nm + ': the raised 7th is cancelled, and the tune comes to rest on ' + L + ': ' + k4KeyLab(dest) + ', the relative major.', nm + ': 올린 7도가 제자리로 돌아오고, 선율은 ' + L + '에서 쉬어요: 나란한조 ' + k4KeyLab(dest) + '.');
  if (lead) return t(nm + ' is the leading note of ' + k4KeyLab(dest) + ', and the tune comes to rest on ' + L + ': ' + wh[0] + '.', nm + '은 ' + k4KeyLab(dest) + '의 이끎음이고, 선율은 ' + L + '에서 쉬어요: ' + wh[1] + '.');
  return t(nm + ' takes the place of ' + k4KeyLab(c.h) + '\'s leading note: it is the 4th of ' + k4KeyLab(dest) + '. The tune comes to rest on ' + L + ': ' + wh[0] + '.', nm + '이 ' + k4KeyLab(c.h) + '의 이끎음 자리에 와요: ' + k4KeyLab(dest) + '의 4도. 선율은 ' + L + '에서 쉬어요: ' + wh[1] + '.'); };
// the two forms written out: up or down, the notes that differ
const k5FormNotes = (q) => (q.dir === 'up' ? [0, 1, 2, 3, 4, 5, 6, 7] : [7, 6, 5, 4, 3, 2, 1, 0]).map(x => k5MNote(q.k, x, q.form));
const k5FormHi = (q) => (q.dir === 'up' ? (q.form === 'mel' ? [5, 6] : q.form === 'har' ? [6] : []) : (q.form === 'har' ? [1] : [1, 2]));

// ── the questions (the steps, the drill and the Home share them) ──
function genK5(kind, prev, fixed) {
  const uid = Math.random(), again = (key) => prev && prev.key === key;
  if (kind === 'sig') { let i, clef, g = 0; do { i = fixed != null ? fixed : Math.floor(Math.random() * K5_SIGQ.length); clef = Math.random() < 0.7 ? 'treble' : 'bass'; } while (fixed == null && again('s' + i) && g++ < 10);
    const [ty, n, minor] = K5_SIGQ[i], ans = k4SigId(ty, n, minor), ch = [ans, k4SigId(ty, n - 1, minor), n < 7 ? k4SigId(ty, n + 1, minor) : k5Enh(ty, n, minor), k4SigId(ty, n, !minor)];
    return { kind, i, ty, n, minor, clef, answer: ans, choices: shuffle([...new Set(ch)]), key: 's' + i, uid }; }
  if (kind === 'mel') { let k, sub, form, g = 0; do { k = fixed ? fixed.k : (Math.random() < 0.75 ? pick(K5M_NEW) : pick(K5M_IDS)); sub = fixed ? fixed.sub : Math.random() < 0.5 ? 'pair' : 'form'; form = fixed && fixed.form ? fixed.form : pick(['har', 'mel', 'nat']); } while (!fixed && again(sub + k + form) && g++ < 10);
    if (sub === 'pair') { const sig = k5Sig(K5M[k].ks), L = (x, f) => k5Let(k5MNote(k, x, f), sig), ans = L(5, 'mel') + ' ' + L(6, 'mel'), ch = [ans, L(5, 'nat') + ' ' + L(6, 'har'), L(5, 'nat') + ' ' + L(6, 'nat')];
      if (K5M[k].ks[0] === 'sharp') ch.push([5, 6].map(x => k5Let(k5Up(k5MNote(k, x, 'mel')))).join(' '));   // the right keys under the wrong letters
      return { kind, sub, k, answer: ans, choices: shuffle(ch), key: sub + k + 'p', uid }; }
    const dir = form === 'mel' ? 'up' : form === 'nat' ? 'down' : (fixed && fixed.dir) || (Math.random() < 0.5 ? 'up' : 'down');
    return { kind, sub, k, form, dir, answer: form, choices: ['har', 'mel', 'nat'], key: sub + k + form, uid }; }
  if (kind === 'iv') { let i, clef, g = 0; do { i = fixed != null ? fixed : Math.floor(Math.random() * K5_AD.length); clef = fixed != null ? 'treble' : Math.random() < 0.6 ? 'treble' : 'bass'; } while (fixed == null && again('i' + i) && g++ < 10);
    const ns = k5Pair(i, clef), ans = k5Iv(ns[0], ns[1]); return { kind, i, clef, ns, answer: ans, choices: shuffle([ans].concat(K5_IVC[ans])), key: 'i' + i, uid }; }
  if (kind === 'inv') { let i, g = 0; do { i = fixed != null ? fixed : Math.floor(Math.random() * K5_AD.length); } while (fixed == null && again('v' + i) && g++ < 10);
    const ns = K5_AD[i].map(h3N), iv = k5Iv(ns[0], ns[1]), up = [ns[1], { d: ns[0].d + 7, acc: ns[0].acc }], ans = k5Inv(iv), n = Number(iv.slice(1));
    return { kind, i, ns, up, iv, answer: ans, choices: shuffle([...new Set([ans, iv[0] + (9 - n), ans[0] + n])]), key: 'v' + i, uid }; }
  let i, g = 0; do { i = fixed != null ? fixed : Math.floor(Math.random() * K5_MOD.length); } while (fixed == null && again('m' + i) && g++ < 10); return { kind: 'mod', i, answer: K5_MOD[i].to, choices: ['dom', 'sub', 'rel'], key: 'm' + i, uid };
}
const K5_FORM = { har: ['Harmonic', '화성 단음계'], mel: ['Melodic, going up', '가락 단음계, 올라갈 때'], nat: ['Melodic, coming down', '가락 단음계, 내려올 때'] };
function k5Lab(q, c) {
  if (q.kind === 'sig') return k4KeyLab(c);
  if (q.kind === 'mel') return q.sub === 'pair' ? c : t(K5_FORM[c][0], K5_FORM[c][1]);
  if (q.kind === 'iv' || q.kind === 'inv') return k5IvName(c);
  const m = K5_MOD[q.i]; return c === 'dom' ? t(k4KeyLab(m.dom) + ' (the dominant)', k4KeyLab(m.dom) + ' (딸림조)') : c === 'sub' ? t(k4KeyLab(m.sub) + ' (the subdominant)', k4KeyLab(m.sub) + ' (버금딸림조)')
    : t(k4KeyLab(m.rel) + ' (the relative ' + (m.h.endsWith('m') ? 'major' : 'minor') + ')', k4KeyLab(m.rel) + ' (나란한조)');
}
function k5Prompt(q) {
  if (q.kind === 'sig') return q.minor ? t('This key signature, a minor key: which one?', '이 조표의 단조는?') : t('This key signature, a major key: which one?', '이 조표의 장조는?');
  if (q.kind === 'mel') return q.sub === 'pair' ? t(K5M[q.k].en + ', melodic, going up: the 6th and the 7th?', K5M[q.k].ko + ' 가락 단음계, 올라갈 때: 6도와 7도는?') : t(K5M[q.k].en + ': which form is written here?', K5M[q.k].ko + ': 여기 적힌 건 어떤 꼴일까요?');
  if (q.kind === 'iv') return t('Name the interval: the letters first, then the semitones.', '음정 이름은? 먼저 글자, 그다음 반음.');
  if (q.kind === 'inv') { const [a, b] = q.ns.map(h3Let), nm = k5IvName(q.iv); return t(a + ' up to ' + b + ' is ' + k5AnA(nm) + '. Turned upside down, ' + b + ' up to ' + a + ' is?', a + '에서 ' + b + '까지는 ' + nm + '. 뒤집으면(' + b + '에서 위의 ' + a + '까지)?'); }
  return t('This melody starts in ' + k4KeyLab(K5_MOD[q.i].h) + '. Where does it go?', '이 선율은 ' + k4KeyLab(K5_MOD[q.i].h) + '에서 시작해요. 어디로 갈까요?');
}
function k5Why(q) {
  if (q.kind === 'sig') { const nm = k4KeyLab(q.answer), enh = k5Enh(q.ty, q.n, q.minor), ow = q.ty === 'sharp' ? t('flats', '플랫') : t('sharps', '샵');
    const same = enh ? t(' It sounds the same as ' + k4KeyLab(enh) + ' (' + (12 - q.n) + ' ' + ow + '): the same keys, another name.', ' ' + k4KeyLab(enh) + '(' + ow + ' ' + (12 - q.n) + '개)와 소리가 같아요: 같은 건반, 다른 이름.') : '';
    if (q.minor) { const rel = K4_MAJ[q.ty][q.n]; return t('The signature belongs to ' + rel + ' major; its relative minor is three semitones below: ' + nm + '.', '이 조표의 장조는 ' + rel + '장조, 나란한 단조는 반음 세 개 아래: ' + nm + '.') + same; }
    return (q.ty === 'sharp' ? t('The last sharp is the 7th note: go up a semitone to the key note: ' + nm + '.', '마지막 샵은 7번째 음: 반음 올라가면 으뜸음: ' + nm + '.') : t('The second-last flat names the key: ' + nm + '.', '뒤에서 두 번째 플랫이 조 이름: ' + nm + '.')) + same; }
  if (q.kind === 'mel' && q.sub === 'pair') { const sig = k5Sig(K5M[q.k].ks), L = (x, f) => k5Let(k5MNote(q.k, x, f), sig), up = L(5, 'mel') + ' and ' + L(6, 'mel'), dn = L(6, 'nat') + ' and ' + L(5, 'nat');
    return t('Going up, the 6th and 7th rise a semitone from the key signature: ' + up + '. Coming down they fall back: ' + dn + '. The harmonic form raises only the 7th.', '올라갈 때 6도와 7도는 조표에서 반음 올라가요: ' + up.replace(' and ', ', ') + '. 내려올 때는 제자리로: ' + dn.replace(' and ', ', ') + '. 화성 단음계는 7도만 올려요.'); }
  if (q.kind === 'mel') { const sig = k5Sig(K5M[q.k].ks), ns = k5FormNotes(q), hi = k5FormHi(q).map(j => k5Let(ns[j], sig)).join(', ');
    return q.form === 'har' ? t('Only the 7th is raised (' + hi + '), the same up and down: harmonic. Between the 6th and 7th, a step and a half: an augmented 2nd.', '7도만 올렸어요(' + hi + '), 올라갈 때도 내려올 때도: 화성 단음계. 6도와 7도 사이는 한 음 반: 증2도.')
      : q.form === 'mel' ? t('Going up, the 6th and 7th are both raised (' + hi + '): melodic.', '올라가면서 6도와 7도를 둘 다 올렸어요(' + hi + '): 가락 단음계.')
      : t('Coming down, nothing is raised (' + hi + ': the key signature): the melodic minor falls back.', '내려오면서 아무것도 올리지 않았어요(' + hi + ': 조표대로): 가락 단음계가 제자리로 돌아와요.'); }
  if (q.kind === 'iv') { const [a, b] = q.ns, n = b.d - a.d + 1, s = ivMidi(b) - ivMidi(a), A = h3Let(a), B = h3Let(b), lets = Array.from({ length: n }, (_, j) => H3_L[((a.d + j) % 7 + 7) % 7]).join(' '), nm = k5IvName(q.answer);
    return t(A + ' up to ' + B + ': ' + n + ' letters (' + lets + '), and ' + s + ' semitones: ' + k5AnA(nm) + '.', A + '에서 ' + B + '까지: 글자 ' + n + '개(' + lets + '), 반음 ' + s + '개: ' + nm + '.'); }
  if (q.kind === 'inv') return t('Upside down, ' + k5AnA(k5IvName(q.iv)) + ' becomes ' + k5AnA(k5IvName(q.answer)) + ': ' + q.iv.slice(1) + ' + ' + q.answer.slice(1) + ' = 9, and ' + ({ A: 'augmented becomes diminished', d: 'diminished becomes augmented', M: 'major becomes minor', m: 'minor becomes major', P: 'perfect stays perfect' })[q.iv[0]] + '.',
    k5IvName(q.iv) + '를 뒤집으면 ' + k5IvName(q.answer) + ': ' + q.iv.slice(1) + ' + ' + q.answer.slice(1) + ' = 9, ' + ({ A: '증은 감으로', d: '감은 증으로', M: '장은 단으로', m: '단은 장으로', P: '완전은 그대로' })[q.iv[0]] + '.');
  return k5ModWhy(q.i);
}
const k5Play = (q) => (q.kind === 'sig' ? null
  : q.kind === 'mel' ? (q.sub === 'pair' ? () => { const r = K5M[q.k].r; spPlay([0, 2, 3, 5, 7, 9, 11, 12, 10, 8, 7, 5, 3, 2, 0].map((x, j) => ({ at: j * 0.5, keys: [r + x], len: j === 14 ? 1.5 : 0.5 })), 84); }
    : () => { const ns = k5FormNotes(q); spPlay(ns.map((n, j) => ({ at: j * 0.5, keys: [h3Semi(n)], len: j === 7 ? 1.5 : 0.5 })), 84); })
  : q.kind === 'iv' || q.kind === 'inv' ? () => { const ev = []; (q.kind === 'iv' ? [q.ns] : [q.ns, q.up]).forEach((p, k) => { const a = k * 4.4; ev.push({ at: a, keys: [h3Semi(p[0])], len: 0.9 }, { at: a + 1, keys: [h3Semi(p[1])], len: 0.9 }, { at: a + 2.2, keys: p.map(h3Semi), len: 1.6 }); }); spPlay(ev, 72); }
  : () => { const ns = k5ModNotes(q.i); spPlay(ns.map((n, j) => ({ at: j * 0.9, keys: [h3Semi(n)], len: j === ns.length - 1 ? 2 : 0.85, vol: 0.15 })), 84); });
const k5Cap = (x) => <div style={{textAlign:'center',fontSize:12.5,fontWeight:900,color:BK.muted,marginTop:2}}>{x}</div>;
function k5Fig(q, shown, scr = true) {
  if (q.kind === 'sig') { const ty = q.ty, n = q.n, enh = k5Enh(ty, n, q.minor); return <div style={{maxWidth:300,margin:'0 auto'}}><KSStaff count={n} type={ty} width={180} clef={q.clef} accent={BK.coral} ink={BK.ink}/>
    {shown && k5Cap(n + ' ' + (ty === 'sharp' ? t('sharps', '샵') : t('flats', '플랫')) + ' · ' + k4KeyLab(K4_MAJ[ty][n]) + ' / ' + k4KeyLab(K4_MINS[ty][n] + 'm') + (enh ? ' · ' + t('the same keys as ', '같은 건반: ') + k4KeyLab(enh) : ''))}</div>; }
  if (q.kind === 'mel' && q.sub === 'pair') { const c = K5M[q.k], sig = k5Sig(c.ks), K = [0, 2, 3, 5, 7, 9, 11, 12].map(x => c.r + x), lit = {}, nm = { [c.r]: c.en.split(' ')[0] };
    K.forEach(x => { lit[x] = 'pale'; }); [5, 6].forEach(j => { lit[K[j]] = shown ? 'good' : 'cor'; nm[K[j]] = shown ? k5Let(k5MNote(q.k, j, 'mel'), sig) : '?'; });
    return <><div style={{maxWidth:240,margin:'0 auto 4px'}}><KSStaff count={c.ks[1]} type={c.ks[0]} width={180} accent={BK.ink} ink={BK.ink}/></div>
      <SpKb lo={c.r} hi={c.r + 12} W={scr ? 28 : 36} H={scr ? 78 : 96} lit={lit} names={nm} label={k5Name(q.k)}/></>; }
  if (q.kind === 'mel') return <><K4Melody notes={k5FormNotes(q)} ks={K5M[q.k].ks} hi={shown ? k5FormHi(q) : []} width={380}/>{k5Cap(q.dir === 'up' ? t('going up', '올라갈 때') : t('coming down', '내려올 때'))}</>;
  if (q.kind === 'iv') return <div style={{maxWidth:280,margin:'0 auto'}}><IntervalStaff clef={q.clef} notes={q.ns} labels={shown ? q.ns.map(h3Let) : ['', '']} width={220}/></div>;
  if (q.kind === 'inv') return <div style={{display:'grid',gridTemplateColumns:shown ? '1fr 1fr' : '1fr',gap:10,maxWidth:shown ? 460 : 240,margin:'0 auto'}}>
    <div><IntervalStaff clef="treble" notes={q.ns} labels={q.ns.map(h3Let)} width={200}/>{k5Cap(k5IvName(q.iv))}</div>
    {shown && <div><IntervalStaff clef="treble" notes={q.up} colors={[BK.ink, BK.coral]} labels={q.up.map(h3Let)} width={200}/>{k5Cap(k5IvName(q.answer))}</div>}</div>;
  const m = K5_MOD[q.i]; return <K4Melody notes={k5ModNotes(q.i)} ks={m.ks} hi={shown ? [m.clue] : []} width={scr ? 300 : 360}/>;
}
const k5Cols = (q) => (q.kind === 'iv' || q.kind === 'inv' || q.kind === 'mod' || (q.kind === 'mel' && q.sub === 'form') ? 1 : 2);
function K5Pad({ kind, title, note, first, fixed, onResult }) {
  const [q, setQ] = useState(() => genK5(kind, null, fixed != null ? fixed : first)), [pickd, setPick] = useState(null), [run, setRun] = useState(0);
  const say = (c) => { if (pickd != null) return; setPick(c); const ok = c === q.answer; setRun(r => (ok ? r + 1 : 0)); if (onResult) onResult({ ok }); };
  const next = () => { setQ(genK5(kind, q)); setPick(null); };
  const play = k5Play(q), shown = pickd != null;
  return (
    <div className="try-box" style={actBox} data-k5={kind}>
      <div style={actTitle}>{title}</div>
      <div style={actNote}>{note}</div>
      <div style={{textAlign:'center',fontSize:14.5,fontWeight:800,color:BK.ink,margin:'2px 0 6px',textWrap:'balance'}}>{k5Prompt(q)}</div>
      {k5Fig(q, shown)}
      {h3Choice(q.choices.map(c => [c, k5Lab(q, c)]), q.answer, pickd, say, k5Cols(q))}
      {shown && <div style={{marginTop:10,fontSize:13.5,color:'#4a4d86',background:'#fff',borderRadius:8,padding:'7px 10px',lineHeight:1.45}}>{(pickd === q.answer ? t('Yes. ', '맞아요. ') + (run > 1 ? t(run + ' in a row. ', run + '번 연속. ') : '') : '') + k5Why(q)}</div>}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        {play && <button className="ghost-btn" style={spBtn} onClick={play}>{t('▶ Hear it', '▶ 들어 보기')}</button>}
        {shown && fixed == null && <button className="ghost-btn" style={spBtn} onClick={next}>{t('▶ Another', '▶ 다른 것')}</button>}
      </div>
    </div>
  );
}
const K5_NOTES = {
  sig: [<>Grade 5 completes the circle: <b>every key up to seven sharps or seven flats</b>. New: <b>C♯ and C♭ major</b>; <b>G♯, D♯, A♯, E♭ and A♭ minor</b>. The rules still work: the last sharp is the 7th note; the second-last flat names the key; a minor key sits three semitones below its relative major. From five on, two names share the same keys: <b>B = C♭, F♯ = G♭, C♯ = D♭</b>.</>,
    <>5급은 원을 완성해요: <b>샵이나 플랫 일곱 개까지 모든 조</b>. 새로: <b>C♯장조와 C♭장조</b>; <b>G♯, D♯, A♯, E♭, A♭단조</b>. 규칙은 그대로: 마지막 샵은 7번째 음, 뒤에서 두 번째 플랫이 조 이름, 단조는 나란한 장조보다 반음 세 개 아래. 다섯 개부터는 두 이름이 같은 건반을 나눠요: <b>B = C♭, F♯ = G♭, C♯ = D♭</b>.</>],
  mel: [<>A minor key has <b>two forms</b>. <b>Harmonic</b>: the 7th raised, up and down. <b>Melodic</b>: going up, the <b>6th and 7th raised</b>; coming down, both fall back to the key signature. To raise is one step up from the key signature: a flat becomes a natural, a sharp a <b>double sharp</b> (𝄪).</>,
    <>단조에는 <b>두 가지 꼴</b>이 있어요. <b>화성 단음계</b>: 7도를 올려요, 올라갈 때도 내려올 때도. <b>가락 단음계</b>: 올라갈 때 <b>6도와 7도를 올리고</b>, 내려올 때는 둘 다 조표대로. 올린다는 건 조표에서 반음 위로: 플랫은 제자리표가, 샵은 <b>겹샵</b>(𝄪)이 돼요.</>],
  iv: [<>Count the <b>letters</b> first: that gives the number. Then count the <b>semitones</b>. One more than a perfect or major interval: <b>augmented</b>. One less than a perfect or minor interval: <b>diminished</b>. C–F♯ and C–G♭ are the same keys, but C–F♯ is a 4th (augmented) and C–G♭ a 5th (diminished).</>,
    <>먼저 <b>글자</b>를 세요: 그게 숫자. 그다음 <b>반음</b>을 세요. 완전음정이나 장음정보다 반음 하나 많으면 <b>증</b>, 완전음정이나 단음정보다 하나 적으면 <b>감</b>. C–F♯와 C–G♭는 같은 건반이지만, C–F♯는 4도(증4도), C–G♭는 5도(감5도).</>],
  inv: [<>Turn an interval upside down: the lower note goes up an octave. The numbers <b>add to 9</b>; <b>major and minor swap</b>; <b>augmented and diminished swap</b>; <b>perfect stays perfect</b>.</>,
    <>음정을 뒤집어요: 아래 음이 한 옥타브 위로. 숫자의 <b>합은 9</b>, <b>장과 단이 바뀌고</b>, <b>증과 감이 바뀌고</b>, <b>완전은 그대로</b>.</>],
  mod: [<>Grade 5 adds the <b>subdominant</b>, the key a 5th below (C → F, A minor → D minor). The clues: to the <b>dominant</b>, a note <b>raised</b>, its leading note (F♯ for G); to the <b>subdominant</b> from a major key, a note <b>lowered</b> (B♭ for F); from a minor key, the new leading note (C♯ for D minor); to the <b>relative</b>, its leading note (G♯ for A minor), or from a minor key the raised 7th <b>cancelled</b>. Then: where does the tune come to rest?</>,
    <>5급은 <b>버금딸림조</b>를 더해요: 5도 아래의 조(C → F, A단조 → D단조). 단서는: <b>딸림조</b>로 가면 <b>올린</b> 음, 그 조의 이끎음(G로 가면 F♯); 장조에서 <b>버금딸림조</b>로 가면 <b>내린</b> 음(F로 가면 B♭); 단조에서는 새 이끎음(D단조로 가면 C♯); <b>나란한조</b>로 가면 그 이끎음(A단조로 가면 G♯), 단조에서는 올린 7도를 <b>제자리로</b>. 그다음: 선율은 어디서 쉬나요?</>],
};
const k5Note2 = (kind) => (LANG === 'ko' ? K5_NOTES[kind][1] : K5_NOTES[kind][0]);
const K5_STEP = { sig: ['Every key, up to seven', '일곱 개까지, 모든 조'], mel: ['The melodic minor', '가락 단음계'], iv: ['Augmented and diminished', '증음정과 감음정'], inv: ['Every interval upside down', '모든 음정 뒤집기'], mod: ['Dominant, subdominant or relative?', '딸림조? 버금딸림조? 나란한조?'] };
const k5StepT = (kind) => t(K5_STEP[kind][0], K5_STEP[kind][1]);
const K5_FIRST = { sig: 0, mel: { k: 'Gsm', sub: 'pair' }, iv: 0, inv: 0, mod: 1 };
const K5Step = ({ kind, fixed, onResult }) => <K5Pad kind={kind} title={k5StepT(kind)} note={k5Note2(kind)} first={K5_FIRST[kind]} fixed={fixed} onResult={onResult}/>;

// ── the pictures on paper ──
const k5PicMel = () => { const m = spMiniKeys(8, 20, { 8: 'pale', 17: 'cor', 19: 'cor', 20: 'pale' }); return { shapes: [{ k: 'raw', svg: m.svg }], vb: [0, 0, m.w, 44] }; };
const k5PicAD = () => { const m = spMiniKeys(0, 7, { 0: 'cor', 6: 'cor' }); return { shapes: [{ k: 'raw', svg: m.svg }], vb: [0, 0, m.w, 44] }; };

function k5LbPages(scr = false) {
  const ch = 'keys-5', k4n = bkChapterNo('keys-4');
  const pen = (x) => <PenArt shapes={x.shapes} vb={x.vb} style={{width:90}}/>;
  const checks5 = [[k4PicSig(), t('I name every key up to seven sharps or flats', '샵이나 플랫 일곱 개까지 모든 조의 이름을 말해요')], [k5PicMel(), t('I write the melodic minor up and down, double sharps too', '가락 단음계를 올라가고 내려오며 적어요, 겹샵도')],
    [k5PicAD(), t('I name augmented and diminished intervals', '증음정과 감음정의 이름을 말해요')], [k4PicIv(), t('I turn any interval upside down', '어떤 음정이든 뒤집을 수 있어요')],
    [k4PicMod(), t('I see where a melody goes: the dominant, the subdominant or the relative', '선율이 딸림조, 버금딸림조, 나란한조 중 어디로 가는지 알아봐요')]];
  const kinds = ['sig', 'mel', 'iv', 'inv', 'mod'];
  const toc = kinds.map((k, i) => [k5StepT(k), i + 2]).concat([[t('My five checks', '나의 다섯 가지 확인'), 7]]);
  const FX = { sig: 0, mel: { k: 'Gsm', sub: 'pair' }, iv: 0, inv: 0, mod: 1 };
  const still = (kind, fx) => <LbPic h={kind === 'mod' || kind === 'inv' ? 150 : 170}><div style={{width:'100%',maxWidth:kind === 'mod' || kind === 'inv' ? 600 : 480,margin:'0 auto'}}>{k5Fig(genK5(kind, null, fx), true, scr)}</div></LbPic>;
  const TEACH = {
    sig: t('Theory of Music Grade 5: the recognition and writing of all the major and minor scales (both forms) and their key signatures. New since Grade 4: C♯ and C♭ major (7♯, 7♭); G♯, D♯, A♯, E♭ and A♭ minor. From five sharps or flats, keys pair up as the same keys under two names: B = C♭, F♯ = G♭, C♯ = D♭; G♯ = A♭ minor, D♯ = E♭ minor, A♯ = B♭ minor. The rules still work, and the sharps and flats always come in the same order.', '이론 5급: 모든 장음계와 단음계(두 가지 꼴)와 조표를 알아보고 적기. 4급에 더해 새로: C♯장조와 C♭장조(샵 7, 플랫 7); G♯, D♯, A♯, E♭, A♭단조. 샵이나 플랫 다섯 개부터는 같은 건반이 두 이름을 가져요: B = C♭, F♯ = G♭, C♯ = D♭; G♯단조 = A♭단조, D♯단조 = E♭단조, A♯단조 = B♭단조. 규칙은 그대로, 샵과 플랫은 언제나 같은 순서로 붙어요.'),
    mel: t('Both forms of every minor scale. Harmonic: the 7th raised a semitone, the same up and down. Melodic: going up the 6th and 7th raised; coming down, the key signature. Raising a sharp makes a double sharp: G♯ minor E♯ F𝄪, D♯ minor B♯ C𝄪, A♯ minor F𝄪 G𝄪; raising a flat makes a natural: E♭ minor C♮ D♮, A♭ minor F♮ G♮. Always accidentals, never in the key signature. The app asks for the raised pair, or which form is written.', '모든 단음계의 두 가지 꼴. 화성 단음계: 7도를 반음 올려요, 올라갈 때도 내려올 때도. 가락 단음계: 올라갈 때 6도와 7도를 올리고, 내려올 때는 조표대로. 샵을 올리면 겹샵: G♯단조 E♯ F𝄪, D♯단조 B♯ C𝄪, A♯단조 F𝄪 G𝄪; 플랫을 올리면 제자리표: E♭단조 C♮ D♮, A♭단조 F♮ G♮. 언제나 임시표로, 조표에는 넣지 않아요. 앱은 올린 두 음, 또는 적힌 꼴을 물어요.'),
    iv: t('All diatonic and chromatic intervals, treble and bass, with or without key signatures. The number comes from the letters, the quality from the semitones: one more than perfect or major is augmented; one less than perfect or minor is diminished. The ones that come up most: the augmented 2nd (6 to 7 in the harmonic minor), the diminished 7th (7 up to 6), the augmented 4th and diminished 5th, the augmented 5th (3 up to 7 in the harmonic minor) and the diminished 4th.', '온음계 음정과 반음계 음정 모두, 높은음자리표와 낮은음자리표, 조표가 있든 없든. 숫자는 글자로, 성질은 반음으로: 완전이나 장음정보다 하나 많으면 증, 완전이나 단음정보다 하나 적으면 감. 자주 나오는 것: 증2도(화성 단음계의 6도에서 7도), 감7도(7도에서 위의 6도), 증4도와 감5도, 증5도(화성 단음계의 3도에서 7도), 감4도.'),
    inv: t('Inversion of all intervals: the numbers add to 9; major and minor swap; augmented and diminished swap; perfect stays perfect. Augmented 4th and diminished 5th; augmented 2nd and diminished 7th; augmented 5th and diminished 4th: each pair inverts into the other.', '모든 음정의 자리바꿈: 숫자의 합은 9, 장과 단이 바뀌고, 증과 감이 바뀌고, 완전은 그대로. 증4도와 감5도, 증2도와 감7도, 증5도와 감4도: 짝끼리 서로 뒤집혀요.'),
    mod: t('Recognition in melodies of modulation to the dominant, subdominant, or relative major or minor. The clue is usually one accidental: to the dominant, its leading note (C → G: F♯); to the subdominant from a major key, the old leading note lowered (C → F: B♭; G → C: F♮); from a minor key, the new key\'s leading note (A minor → D minor: C♯); to the relative minor, its leading note (C → A minor: G♯); to the relative major, the raised 7th cancelled (A minor → C: G♮). Then the cadence: where the tune comes to rest. These are the usual textbook clues: check them against the papers you use.', '선율의 전조 알아보기: 딸림조, 버금딸림조, 나란한 장조나 단조로. 단서는 대개 임시표 하나: 딸림조는 그 이끎음(C → G: F♯); 장조에서 버금딸림조는 원래 이끎음을 내려요(C → F: B♭; G → C: F♮); 단조에서는 새 조의 이끎음(A단조 → D단조: C♯); 나란한 단조는 그 이끎음(C → A단조: G♯); 나란한 장조는 올린 7도를 제자리로(A단조 → C: G♮). 그다음 종지: 선율이 어디서 쉬는지. 흔히 쓰는 교과서 단서예요: 쓰시는 시험지와 맞춰 보세요.'),
  };
  const SAY = {
    sig: t('Seven is the most: C♯ and C♭. From five on, two names for the same keys.', '일곱이 끝: C♯와 C♭. 다섯 개부터는 같은 건반에 두 이름.'),
    mel: t('Melodic: up, raise 6 and 7; down, the key signature.', '가락 단음계: 올라갈 때 6과 7을 올리고, 내려올 때는 조표대로.'),
    iv: t('Letters for the number, semitones for the quality.', '숫자는 글자로, 성질은 반음으로.'),
    inv: t('Add to 9; major and minor swap, augmented and diminished swap, perfect stays.', '합은 9, 장과 단, 증과 감이 바뀌고, 완전은 그대로.'),
    mod: t('Which note changed, and where does the tune come to rest?', '어떤 음이 바뀌었고, 선율은 어디서 쉬나요?'),
  };
  const PIANO = {
    sig: [t('Play C♯ major: seven sharps, every key black except E♯ and B♯.', 'C♯장조를 쳐요: 샵 일곱, E♯와 B♯ 말고는 모두 검은건반.'), t('Play C♭ major: the same keys as B major, written with seven flats.', 'C♭장조: B장조와 같은 건반, 플랫 일곱으로 적어요.'), t('Play their relative minors: A♯ minor and A♭ minor.', '나란한 단조도: A♯단조와 A♭단조.')],
    mel: [t('G♯ melodic minor going up: E♯ and F𝄪 are the white keys F and G.', 'G♯ 가락 단음계, 올라갈 때: E♯와 F𝄪는 흰건반 F와 G.'), t('Coming down: F♯ and E, the key signature.', '내려올 때: F♯와 E, 조표대로.'), t('E♭ melodic minor: up with C♮ and D♮, down with D♭ and C♭.', 'E♭ 가락 단음계: 올라갈 때 C♮와 D♮, 내려올 때 D♭와 C♭.')],
    iv: [t('Play C–F♯, then C–G♭: the same keys.', 'C–F♯, 그다음 C–G♭: 같은 건반.'), t('Write them: C–F♯ is a 4th (augmented), C–G♭ a 5th (diminished).', '적어 봐요: C–F♯는 4도(증), C–G♭는 5도(감).'), t('In A harmonic minor, play F–G♯: an augmented 2nd.', 'A 화성 단음계에서 F–G♯: 증2도.')],
    inv: [t('Play C up to F♯: an augmented 4th.', 'C에서 F♯까지: 증4도.'), t('Move the C up an octave: F♯ up to C, a diminished 5th.', 'C를 한 옥타브 위로: F♯에서 C까지, 감5도.'), t('Check: 4 + 5 = 9, and augmented became diminished.', '확인: 4 + 5 = 9, 증이 감이 됐어요.')],
    mod: [t('Play the C major melody that turns to F: hear the B♭.', 'F로 가는 C장조 선율을 쳐요: B♭를 들어 봐요.'), t('Now the one that turns to G: hear the F♯.', '이번엔 G로 가는 선율: F♯를 들어 봐요.'), t('Point to the new accidental, then the last note.', '새 임시표를 가리키고, 마지막 음도.')],
  };
  return [
    <LbPage key="1" no={1} chId={ch} teacher={<>{t('Theory of Music Grade 5, one step each: every key up to seven sharps or flats; both forms of the minor, the melodic written; augmented and diminished intervals; the inversion of every interval; modulation to the dominant, subdominant or relative. Grade 4\'s keys, semitones and transposition are in chapter ' + k4n + '.', '이론 5급을 한 단계씩: 샵이나 플랫 일곱 개까지 모든 조; 단음계의 두 가지 꼴, 가락 단음계 적기; 증음정과 감음정; 모든 음정의 자리바꿈; 딸림조, 버금딸림조, 나란한조로의 전조. 4급의 조, 반음, 선율 옮기기는 ' + k4n + '장에 있어요.')}</>}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:48,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{bkChapterName(ch)}</div>
      </div></LbOnly>
      {still('sig', 0)}
      <LbSay size={18}>{t('Grade 5 theory: every key up to seven sharps or flats, the melodic minor with its double sharps, augmented and diminished intervals turned upside down, and a tune that travels to the subdominant.', '5급 이론: 샵이나 플랫 일곱 개까지 모든 조, 겹샵이 나오는 가락 단음계, 뒤집히는 증음정과 감음정, 그리고 버금딸림조로 옮겨 가는 선율.')}</LbSay>
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
    ...kinds.map((kind, i) => <LbPage key={kind} no={i + 2} chId={ch} kicker={t('Step ' + (i + 1), (i + 1) + '단계')} title={k5StepT(kind)} teacher={<>{TEACH[kind]}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=' + (i + 1))}>
      <LbLive still={still(kind, FX[kind])} live={<K5Step kind={kind}/>}/>
      <LbSay>{k5Note2(kind)}</LbSay>
      <LbPiano steps={PIANO[kind].map((x, j) => <React.Fragment key={j}>{x}</React.Fragment>)}/>
      <LbRemember>{SAY[kind]}</LbRemember>
    </LbPage>),
    <LbPage key="7" no={7} chId={ch} kicker={t('Check-up', '점검')} title={t('My five checks', '나의 다섯 가지 확인')}
      teacher={<>{t('Each one on paper or at the piano, treble and bass, with and without key signatures. Use keys the child has not just practised.', '하나씩 종이나 피아노에서, 높은음자리표와 낮은음자리표, 조표가 있을 때와 없을 때. 방금 연습하지 않은 조로 해 보세요.')}</>}>
      <LbSay>{t('Tick each one: not yet, nearly, or got it!', '하나씩 표시해요: 아직, 거의, 됐어요!')}</LbSay>
      <LbLive still={<LbStageRows big rows={checks5.map(([a, txt]) => [pen(a), txt])}/>} live={<FiveChecks376 rows={checks5} storeKey="pb_k5_five"/>}/>
    </LbPage>,
  ];
}
function Keys5LessonBook() { return <>{k5LbPages(false)}</>; }
function K5Learn({ onStart }) {
  const pages = k5LbPages(true), opener = pages[0];
  return (
    <Lesson id="keys-5" title={bkChapterName('keys-5')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="keys-5"><div className="lb-screen lb-open" style={{display:'flex',flexDirection:'column',gap:12,margin:'0 0 8px'}}>{lbWordsFirst(opener.props.children)}</div></BkChapterCtx.Provider></LbScreenCtx.Provider>}>
      {pages.slice(1).map((pg, i) => <Step key={i} title={pg.props.title}><LbScreenPage page={pg}/></Step>)}
    </Lesson>
  );
}
// ── the drill ──
const K5_LEVELS = [
  { n: 1, label: 'Every key: which one?', kind: 'sig', time: 15 },
  { n: 2, label: 'The melodic minor', kind: 'mel', time: 20 },
  { n: 3, label: 'Augmented or diminished?', kind: 'iv', time: 20 },
  { n: 4, label: 'Turn the interval upside down', kind: 'inv', time: 15 },
  { n: 5, label: 'Dominant, subdominant or relative?', kind: 'mod', time: 25 },
];
Object.assign(LEVEL_KO, { 'Every key: which one?': '모든 조: 어느 조?', 'The melodic minor': '가락 단음계', 'Augmented or diminished?': '증음정? 감음정?', 'Turn the interval upside down': '음정 뒤집기', 'Dominant, subdominant or relative?': '딸림조? 버금딸림조? 나란한조?' });
const genK5Question = (lv, prev) => genK5(lv.kind, prev);
const k5AnswerLabel = (q) => k5Lab(q, q.answer);
function K5Question({ q, given, locked, onAnswer, pixel }) {
  const done = !!given, play = k5Play(q);
  useEffect(() => { if (q.kind !== 'mod') return; const id = setTimeout(() => play && play(), 350); return () => { clearTimeout(id); stopClicks(); }; }, [q.uid]);
  const btnCls = pixel ? 'pixel-choice' : 'choice-btn', cls = (c) => btnCls + (!done ? '' : c === q.answer ? ' good' : given.ans === c ? ' bad' : '');
  return (<div>
    <p style={pixel ? {fontSize:11.5,textAlign:'center'} : {fontSize:15,fontWeight:700,textAlign:'center',margin:'0 0 8px',color:'var(--muted)',textWrap:'balance'}}>{k5Prompt(q)}</p>
    {k5Fig(q, done)}
    {play && <div style={{textAlign:'center',margin:'6px 0 0'}}><button className={pixel ? 'pixel-btn' : 'ghost-btn'} style={{minHeight:44}} onClick={() => { stopClicks(); play(); }}>{t('▶ Hear it', '▶ 들어 보기')}</button></div>}
    <div style={{display:'grid',gridTemplateColumns:'repeat(' + k5Cols(q) + ',minmax(0,1fr))',gap:8,marginTop:10}}>{q.choices.map(c => <button key={String(c)} disabled={locked} className={cls(c)} style={{padding:'12px 4px',fontSize:15,fontWeight:900}} onClick={() => { if (locked || done) return; stopClicks(); onAnswer(c); }}>{k5Lab(q, c)}</button>)}</div>
    {done && !pixel && <div style={{marginTop:10,fontSize:13.5,color:'#4a4d86',background:'#fff',borderRadius:8,padding:'7px 10px',lineHeight:1.45}}>{k5Why(q)}</div>}
  </div>);
}
Object.assign(KEYS_5_DRILL, { levels: K5_LEVELS, generate: genK5Question, check: (q, ans) => ans !== null && ans !== undefined && ans === q.answer, answerLabel: k5AnswerLabel, Question: K5Question, Learn: K5Learn });
// the teacher's copy: every answer computed from the room's own data
function K5Teacher() {
  const pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="keys-5" teacher>{content}</WbPage>);
  const mel = (k) => { const sig = k5Sig(K5M[k].ks), up = Array.from({ length: 8 }, (_, x) => k5Let(k5MNote(k, x, 'mel'), sig)), dn = [7, 6, 5, 4, 3, 2, 1, 0].map(x => k5Let(k5MNote(k, x, 'nat'), sig)); return K5M[k].en + ': ' + up.join(' ') + ' · ' + dn.join(' '); };
  const pair = (p) => { const ns = p.map(h3N); return ns.map(h3Let).join('–') + ' ' + k5Iv(ns[0], ns[1]); };
  P(<>
    <div style={{fontFamily:LB_SERIF,fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('keys-5')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 12px',lineHeight:1.5}}>Theory of Music Grade 5. Every answer below is computed from the room's own data, the same as the app uses.</div>
    <TcBlock page={2} title="Every key, up to seven" answers={<>{tcAns('NEW MAJOR', ['C♯ (7♯)', 'C♭ (7♭)'])}{tcAns('NEW MINOR', ['G♯ (5♯)', 'D♯ (6♯)', 'A♯ (7♯)', 'E♭ (6♭)', 'A♭ (7♭)'])}{tcAns('THE SAME KEYS', ['B = C♭', 'F♯ = G♭', 'C♯ = D♭', 'G♯ minor = A♭ minor', 'D♯ minor = E♭ minor', 'A♯ minor = B♭ minor'], null)}</>}
      watch="The seven-sharp and seven-flat keys named from the six: count every sign. A minor key named by the major rule: a minor key is three semitones below its major."
      say="“Seven is the most: C♯ and C♭.”"/>
    <TcBlock page={3} title="The melodic minor" answers={<>{tcAns('MELODIC, UP · DOWN', K5M_IDS.map(mel), null)}{tcAns('HARMONIC 7TH', K5M_IDS.map(k => K5M[k].en + ': ' + k5Let(k5MNote(k, 6, 'har'), k5Sig(K5M[k].ks))))}</>}
      watch="G for F𝄪, F for E♯: the right key, the wrong letter. And the raised notes left in on the way down."
      say="“Up: raise 6 and 7. Down: the key signature.”"/>
  </>);
  P(<>
    <TcBlock page={4} title="Augmented and diminished" answers={<>{tcAns('THE PAIRS (treble; in the bass an octave lower)', K5_AD.map(pair), null)}</>}
      watch="Naming by the keys instead of the letters: C–F♯ and C–G♭ sound the same, but one is a 4th and the other a 5th."
      say="“Letters for the number, semitones for the quality.”"/>
    <TcBlock page={5} title="Every interval upside down" answers={<>{tcAns('INVERSIONS', K5_AD.map(p => { const ns = p.map(h3N), iv = k5Iv(ns[0], ns[1]); return iv + ' → ' + k5Inv(iv); }), null)}</>}
      watch="Keeping the quality: augmented 4th → augmented 5th. Augmented and diminished swap, like major and minor."
      say="“Add to 9; augmented and diminished swap.”"/>
    <TcBlock page={6} title="Dominant, subdominant or relative?" answers={<>{tcAns('MELODIES', K5_MOD.map((m, i) => k4KeyLab(m.h) + ' → ' + ({ dom: 'dominant', sub: 'subdominant', rel: 'relative' })[m.to] + ', ' + m[m.to] + ' (clue ' + h3Let(k5ModNotes(i)[m.clue]) + (k5ModNotes(i)[m.clue].acc === 0 ? '♮' : '') + ')'))}</>}
      watch="Taking a lowered note for a sign of the relative minor. Lowered in a major key: the subdominant. Then the last note decides."
      say="“Which note changed, and where does the tune come to rest?”"/>
    <TcBlock page={7} title="The check-up" answers={<div style={{fontSize:12,color:BK.ink,lineHeight:1.5}}>Each one on paper or at the piano, treble and bass, with and without key signatures, in keys the child has not just practised. The drill's levels 1 to 5 match the steps.</div>}/>
  </>);
  return <>{pages}</>;
}
TEACHER_COPIES['keys-5'] = K5Teacher;
'''
rep("""TEACHER_COPIES['keys-4'] = K4Teacher;""", """TEACHER_COPIES['keys-4'] = K4Teacher;""" + CH)

HOME = r'''
// ══ Build BB: Keys and Intervals, Grade 5 on the Home (Scales and keys, after Grade 4) ══
LBH_FN['keys-5'] = (s) => k5LbPages(s);
const k5HomeQ = (kind) => (n, prev) => { const q = genK5(kind, prev), a = q.answer, p = k5Prompt(q), w = k5Why(q);
  return { kind: 'choice', cols: k5Cols(q), key: q.key, prompt: [p, p], opts: q.choices.map(c => ({ id: c, label: () => k5Lab(q, c) })), ans: a, ok: (v) => v === a,
    play: k5Play(q), fig: (c) => ({ mid: k5Fig(q, !!c.res) }), yes: ['Yes. ' + w, '맞아요. ' + w], no: [w, w] }; };
const k5HomeAdd = (id, i, en, ko, benEn, bko, make) => lbhAdd(id, 'p-scales', 'pitch', en, ko, benEn, bko, lbhSpec('keys-5', i, { make }));
k5HomeAdd('k5-sig', 1, 'Every key, up to seven', '일곱 개까지, 모든 조', 'C♯ and C♭ major, and the new minor keys.', 'C♯장조와 C♭장조, 그리고 새 단조.', k5HomeQ('sig'));
k5HomeAdd('k5-mel', 2, 'The melodic minor', '가락 단음계', 'Up: raise 6 and 7. Down: the key signature.', '올라갈 때 6과 7을 올리고, 내려올 때는 조표대로.', k5HomeQ('mel'));
k5HomeAdd('k5-ad', 3, 'Augmented and diminished', '증음정과 감음정', 'Letters for the number, semitones for the quality.', '숫자는 글자로, 성질은 반음으로.', k5HomeQ('iv'));
k5HomeAdd('k5-inv', 4, 'Every interval upside down', '모든 음정 뒤집기', 'Add to 9; augmented and diminished swap.', '합은 9, 증과 감이 바뀌어요.', k5HomeQ('inv'));
k5HomeAdd('k5-mod', 5, 'Dominant, subdominant or relative?', '딸림조? 버금딸림조? 나란한조?', 'Which note changed, and where it comes to rest.', '바뀐 음, 그리고 쉬는 곳.', k5HomeQ('mod'));
'''
after_line("k4HomeAdd('k4-mod', 5,", HOME)
rep("""    { id: 'psc-4', en: 'Keys and intervals, Grade 4', ko: '조와 음정, Grade 4', lessons: ['k4-sig', 'k4-lead', 'k4-semi', 'k4-below', 'k4-mod', 'k4-tr'], check: 'keys-4' },   // Build AT""",
    """    { id: 'psc-4', en: 'Keys and intervals, Grade 4', ko: '조와 음정, Grade 4', lessons: ['k4-sig', 'k4-lead', 'k4-semi', 'k4-below', 'k4-mod', 'k4-tr'], check: 'keys-4' },   // Build AT
    { id: 'psc-5', en: 'Keys and intervals, Grade 5', ko: '조와 음정, Grade 5', lessons: ['k5-sig', 'k5-mel', 'k5-ad', 'k5-inv', 'k5-mod'], check: 'keys-5' },   // Build BB""")
rep("""  set('4', 'k4-sig k4-lead k4-semi k4-below k4-mod k4-tr');   // Build AT: Keys and Intervals, Grade 4""",
    """  set('4', 'k4-sig k4-lead k4-semi k4-below k4-mod k4-tr');   // Build AT: Keys and Intervals, Grade 4
  set('5', 'k5-sig k5-mel k5-ad k5-inv k5-mod');   // Build BB: Keys and Intervals, Grade 5""")
rep("""const LESSON_BOOKS = { 'scales-5': Scales5LessonBook,""", """const LESSON_BOOKS = { 'keys-5': Keys5LessonBook, 'scales-5': Scales5LessonBook,""")
rep("""const LB_PAGE_FNS = { 'scales-5': s5LbPages,""", """const LB_PAGE_FNS = { 'keys-5': k5LbPages, 'scales-5': s5LbPages,""")
rep("""const HOUSE_ICONS = {""", """const HOUSE_ICONS = {"keys-5": "<path d=\\"M4 13 H44 M4 19 H44 M4 25 H44 M4 31 H44 M4 37 H44\\" stroke-width=\\"1.2\\"/><text x=\\"10\\" y=\\"30\\" font-size=\\"15\\" font-weight=\\"900\\" fill=\\"#e4572e\\" stroke=\\"none\\">♯♯</text><text x=\\"32\\" y=\\"38\\" font-size=\\"12\\" font-weight=\\"900\\" fill=\\"#26296b\\" stroke=\\"none\\" font-family=\\"Inter, sans-serif\\">5</text>", """)
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
