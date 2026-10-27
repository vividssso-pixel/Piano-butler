import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build BQ (board call 26, the third Grade 6 room): Arpeggios and Progressions, Grade 6. From the technical work book, Grade 6
# (pp36-41, read 28 Oct): I-V-I chord progressions in G, F and A major, from memory, mf, legato, crotchet about 72, the right hand's
# chord in three positions (first chord B D G, then D G B, then G B D in G major), the left hand the bass (2 5 2); arpeggios, root
# position and inversions, F-sharp and E-flat major and minor, four octaves, hands separately and together, mf, crotchet 60 four notes a
# beat (the fingerings below are the book's); dominant 7th arpeggios "of F-sharp" (C-sharp E-sharp G-sharp B) and "of E-flat" (B-flat D F
# A-flat): the dominant 7th IN that key, starting on its 5th note; diminished 7th arpeggios "of F-sharp" (E-sharp G-sharp B D) and "of
# E-flat" (D F A-flat C-flat): starting on the leading note; four octaves, mf, crotchet 60 four notes a beat. The walk, the
# 7th-chord pads and the arpeggio pad take the grade as a prop, for Grades 7 and 8.

rep("""const SCALES_6_DRILL = { id: 'scales-6', label: 'Scales, Grade 6' };   // Build BP""",
    """const SCALES_6_DRILL = { id: 'scales-6', label: 'Scales, Grade 6' };   // Build BP
const ARPS_6_DRILL = { id: 'arps-6', label: 'Arpeggios and Progressions, Grade 6' };   // Build BQ""")
rep("""  { id: 'scales-6', label: 'Scales, Grade 6', concept: SCALES_6_DRILL, track: 'start' },   // Build BP""",
    """  { id: 'scales-6', label: 'Scales, Grade 6', concept: SCALES_6_DRILL, track: 'start' },   // Build BP
  { id: 'arps-6', label: 'Arpeggios and Progressions, Grade 6', concept: ARPS_6_DRILL, track: 'start' },   // Build BQ""")
rep("""'scales-6': '스케일, Grade 6'""", """'scales-6': '스케일, Grade 6', 'arps-6': '아르페지오와 화음 진행, Grade 6'""")
rep("""'scales-6': 'k-play'""", """'scales-6': 'k-play', 'arps-6': 'k-play'""")
rep("""'scales-6': ['scales-5']""", """'scales-6': ['scales-5'], 'arps-6': ['scales-5', 'chords']""")
rep("""  'scales-6': 'scales grade 6""", """  'arps-6': 'arpeggios grade 6 inversions root position first second chord progression I V I three positions dominant seventh diminished seventh f sharp e flat thumb white key',
  'scales-6': 'scales grade 6""")
rep("""'scales-6': ['Scales 6', '스케일 6']""", """'scales-6': ['Scales 6', '스케일 6'], 'arps-6': ['Arpeggios 6', '아르페지오 6']""")

CH = r'''
// ─── Chapter: Arpeggios and Progressions, Grade 6 (Build BQ, 2026-10-28; board call 26, the third Grade 6 room) ───
// Four skills, each from the technical work book (Grade 6 pp36-41): the chord walk I–V–I from three positions (the note that
// stays, the others a step); arpeggios from every note of the chord (the thumb lives on the one white key; all black keys: the
// C-major shape, the thumb on the first note); the dominant 7th "of" a key (its 5th note, a major triad and a minor 7th);
// the diminished 7th "of" a key (its leading note, every gap three semitones). Then a harp of arpeggios to make.
// ── step 1: the chord walk. The right hand's chords, by position (the top note: the root, the 3rd or the 5th), from the tonic t ──
const CW_RH = {
  1: { I: [-8, -5, 0], IV: [-7, -3, 0], V: [-10, -5, -1] },
  2: { I: [-5, 0, 4], IV: [-3, 0, 5], V: [-5, -1, 2] },
  3: { I: [0, 4, 7], IV: [0, 5, 9], V: [-1, 2, 7] },
};
const CW_GR = {   // the progressions, the left hand's bass from the first chord's, and the keys (the book's)
  6: { prog: ['I', 'V', 'I'], bass: [0, -5, 0], keys: ['G', 'F', 'A'], bpm: 72, lh: '2 5 2' },
  7: { prog: ['I', 'IV', 'V', 'I'], bass: [0, -7, -5, 0], keys: ['G', 'F', 'E'], bpm: 72, lh: '1 5 4 1' },
  8: { prog: ['I', 'IV', 'I64', 'V', 'I'], bass: [0, 5, 7, -5, 0], keys: ['C', 'D', 'Eb'], bpm: 72, lh: '5 2 1 5 2' },
};
const CW_KEY = { C: [12, 'C'], D: [14, 'D'], Eb: [15, 'E♭'], E: [4, 'E'], F: [5, 'F'], G: [7, 'G'], A: [9, 'A'] };   // the tonic t, where the first chord sits, and its name
const cwChord = (k, pos, rn) => CW_RH[pos][rn === 'I64' ? 'I' : rn].map(x => CW_KEY[k][0] + x);
const cwBass0 = (k) => spPc(CW_KEY[k][0]) - 12;   // the tonic below middle C
const cwRn = (rn) => (rn === 'I64' ? 'I⁶₄' : rn);
const cwName = (k, i) => { const sm = spPc(i - CW_KEY[k][0]); return l6Spell(CW_KEY[k][1], sm, { 0: 1, 2: 2, 4: 3, 5: 4, 7: 5, 9: 6, 11: 7 }[sm] || 1); };
const cwRange = (k) => { const all = [1, 2, 3].flatMap(p => ['I', 'IV', 'V'].flatMap(rn => cwChord(k, p, rn))); return [Math.min(...all) - 1, Math.max(...all) + 1]; };
const cwPlay = (k, pos, g, upto = null) => { const G = CW_GR[g], b0 = cwBass0(k), ev = [], P = G.prog.slice(0, upto == null ? G.prog.length : upto);
  P.forEach((rn, j) => { const last = j === P.length - 1; ev.push({ at: j, keys: cwChord(k, pos, rn).concat([b0 + G.bass[j]]), len: last ? 2 : 0.95, vol: 0.12 }); });
  return spPlay(ev, G.bpm); };
function ChordWalkPad({ g = 6, onResult, fixed }) {
  const G = CW_GR[g], N = G.prog.length;
  const [k, setK] = useState(fixed ? fixed.k : G.keys[0]), [pos, setPos] = useState(fixed ? fixed.pos : 1), [at, setAt] = useState(1), [tap, setTap] = useState([]), [bad, setBad] = useState(false), [miss, setMiss] = useState(0);
  const done = at >= N, want = done ? null : cwChord(k, pos, G.prog[at]), prev = cwChord(k, pos, G.prog[done ? N - 1 : at - 1]);
  const reset = (fn) => { setAt(1); setTap([]); setBad(false); setMiss(0); if (fn) fn(); };
  const press = (i) => { playKey(i, 0.4); if (done) return; if (tap.includes(i)) { setTap(tp => tp.filter(x => x !== i)); return; } const nt = tap.concat([i]); setBad(false);
    if (nt.length < 3) { setTap(nt); return; }
    if (want.every(x => nt.includes(x))) { const na = at + 1; setAt(na); setTap([]); spPlay([{ at: 0, keys: want.concat([cwBass0(k) + G.bass[at]]), len: 1.2, vol: 0.12 }], 72); if (na >= N) { if (onResult) onResult({ ok: miss === 0 }); setTimeout(() => cwPlay(k, pos, g), 1300); } }
    else { setTap([]); setBad(true); setMiss(m => m + 1); } };
  const lit = {}; prev.forEach(x => { lit[x] = done ? 'good' : 'pale'; }); tap.forEach(x => { lit[x] = 'cor'; });
  const stays = done ? [] : prev.filter(x => want.includes(x));
  const nameOf = (rn) => cwChord(k, pos, rn).map(i => cwName(k, i)).join(' ');
  return (
    <div className="try-box" style={actBox} data-cw={g}>
      <div style={actTitle}>{t(G.prog.map(cwRn).join('–') + ' from three positions', '세 자리에서 ' + G.prog.map(cwRn).join('–'))}</div>
      <div style={actNote}>{LANG === 'ko' ? <>오른손은 화음, 왼손은 베이스. 다음 화음으로 갈 때 <b>같은 음은 그대로 두고</b>, 나머지는 <b>바로 옆 건반으로</b>만 움직여요. 오른손의 다음 화음 세 음을 눌러요. 자리 1은 맨 위가 으뜸음, 2는 3음, 3은 5음.</>
        : <>The right hand plays the chords, the left hand the bass. To move to the next chord, <b>keep the note that stays</b> and move the others <b>just a step</b>. Tap the right hand's three notes for the next chord. Position 1 has the key note on top, 2 the 3rd, 3 the 5th.</>}</div>
      {!fixed && spChips(G.keys.map(x => [x, CW_KEY[x][1] + t(' major', '장조')]), k, (x) => reset(() => setK(x)))}
      {!fixed && spChips([[1, t('Position 1', '자리 1')], [2, t('Position 2', '자리 2')], [3, t('Position 3', '자리 3')]], pos, (x) => reset(() => setPos(x)))}
      <div style={{display:'flex',justifyContent:'center',gap:6,flexWrap:'wrap',margin:'2px 0 6px'}}>{G.prog.map((rn, j) => <span key={j} style={{minWidth:46,padding:'5px 8px',borderRadius:8,border:'1.5px solid ' + (j === at ? BK.coral : 'rgba(38,41,107,0.25)'),background:j < at ? '#fff' : j === at ? '#fbe3da' : 'transparent',textAlign:'center',fontFamily:LB_SERIF,fontSize:17,fontWeight:900,color:j < at ? BK.green : BK.ink}}>{cwRn(rn)}<div style={{fontFamily:'Inter, sans-serif',fontSize:10.5,fontWeight:800,color:BK.muted}}>{j < at || done ? nameOf(rn) : '?'}</div></span>)}</div>
      <SpKb lo={cwRange(k)[0]} hi={cwRange(k)[1]} W={22} H={76} lit={lit} names={Object.fromEntries(prev.concat(tap).map(i => [i, cwName(k, i)]))} onTap={press} label={t('The right hand', '오른손')}/>
      {spMsg(done ? t('The walk: ' + G.prog.map(cwRn).join(' – ') + (miss ? '.' : '. First time!'), '진행: ' + G.prog.map(cwRn).join(' – ') + (miss ? '.' : '. 한 번에!'))
        : bad ? t('Not quite: keep ' + stays.map(x => cwName(k, x)).join(' and ') + ', and move the others one step.', '아니에요: 그대로 둘 음 ' + stays.map(x => cwName(k, x)).join(', ') + '. 나머지는 한 걸음.') : t('Now ' + cwRn(G.prog[at]) + ': tap its three notes (' + tap.length + ' of 3).', '이제 ' + cwRn(G.prog[at]) + ': 세 음을 눌러요(3개 중 ' + tap.length + ').'), done ? BK.green : bad ? BK.coral : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={spBtn} onClick={() => cwPlay(k, pos, g, done ? null : at)}>{done ? t('▶ The whole walk', '▶ 진행 전체') : t('▶ So far', '▶ 지금까지')}</button>
        {done && !fixed && <button className="ghost-btn" style={spBtn} onClick={() => reset(() => setPos(pos % 3 + 1))}>{t('▶ Next position', '▶ 다음 자리')}</button>}
      </div>
    </div>
  );
}

// ── step 2: arpeggios from every note of the chord: where does the thumb go? ──
const AP_DATA = {   // the book's fingerings, two octaves up, by position (0 root, 1 first inversion, 2 second inversion)
  Fs: { en: 'F♯ major', ko: 'F♯장조', r: 6, q: [0, 4, 7], nm: ['F♯', 'A♯', 'C♯'], R: [[1, 2, 3, 1, 2, 3, 5], [1, 2, 4, 1, 2, 4, 5], [1, 2, 4, 1, 2, 4, 5]], L: [[5, 3, 2, 1, 3, 2, 1], [5, 4, 2, 1, 4, 2, 1], [5, 3, 2, 1, 3, 2, 1]] },
  Fsm: { en: 'F♯ minor', ko: 'F♯단조', r: 6, q: [0, 3, 7], nm: ['F♯', 'A', 'C♯'], R: [[2, 1, 2, 4, 1, 2, 4], [1, 2, 4, 1, 2, 4, 5], [2, 4, 1, 2, 4, 1, 2]], L: [[2, 1, 4, 2, 1, 4, 2], [5, 4, 2, 1, 4, 2, 1], [4, 2, 1, 4, 2, 1, 2]] },
  Eb: { en: 'E♭ major', ko: 'E♭장조', r: 3, q: [0, 4, 7], nm: ['E♭', 'G', 'B♭'], R: [[2, 1, 2, 4, 1, 2, 4], [1, 2, 4, 1, 2, 4, 5], [2, 4, 1, 2, 4, 1, 2]], L: [[2, 1, 4, 2, 1, 4, 2], [5, 4, 2, 1, 4, 2, 1], [4, 2, 1, 4, 2, 1, 2]] },
  Ebm: { en: 'E♭ minor', ko: 'E♭단조', r: 3, q: [0, 3, 7], nm: ['E♭', 'G♭', 'B♭'], R: [[1, 2, 3, 1, 2, 3, 5], [1, 2, 4, 1, 2, 4, 5], [1, 2, 3, 1, 2, 3, 5]], L: [[5, 4, 2, 1, 4, 2, 1], [5, 4, 2, 1, 4, 2, 1], [5, 3, 2, 1, 3, 2, 1]] },
};
const AP_POS = [['Root position', '기본형'], ['First inversion', '첫째 자리바꿈'], ['Second inversion', '둘째 자리바꿈']];
const apKeys = (k, pos) => { const c = AP_DATA[k], out = []; for (let j = 0; j < 7; j++) { const d = pos + j; out.push(c.r + 12 * Math.floor(d / 3) + c.q[d % 3]); } return out; };
const apNames = (k, pos) => Array.from({ length: 7 }, (_, j) => AP_DATA[k].nm[(pos + j) % 3]);
const apWhite = (k) => AP_DATA[k].q.map((x, j) => (spIsW(AP_DATA[k].r + x) ? AP_DATA[k].nm[j] : null)).filter(Boolean);
const apChip = (k) => AP_DATA[k].nm[0] + (AP_DATA[k].q[1] === 3 ? 'm' : '');
const apPlay = (k, pos, bpm = 60) => { const K = apKeys(k, pos), sq = K.concat(K.slice(0, -1).reverse()); return spPlay(sq.map((x, n) => ({ at: n / 4, keys: [x, x - 12], len: n === sq.length - 1 ? 1.5 : 0.25, vol: 0.12 })), bpm, 2); };
function ArpPosPad({ keys = ['Eb', 'Fsm', 'Fs', 'Ebm'], onResult, fixed }) {
  const [k, setK] = useState(fixed ? fixed.k : keys[0]), [pos, setPos] = useState(fixed ? fixed.pos : 1), [h, setH] = useState(fixed ? fixed.h : 'R'), [found, setFound] = useState([]), [bad, setBad] = useState(null), [miss, setMiss] = useState(0);
  const c = AP_DATA[k], K = apKeys(k, pos), F = c[h][pos], thumbs = K.filter((_, j) => F[j] === 1), done = thumbs.every(x => found.includes(x));
  const reset = (fn) => { setFound([]); setBad(null); setMiss(0); if (fn) fn(); };
  const tap = (i) => { playKey(i, 0.4); if (done) return; if (thumbs.includes(i)) { if (found.includes(i)) return; const nf = found.concat([i]); setFound(nf); setBad(null); if (thumbs.every(x => nf.includes(x))) { if (onResult) onResult({ ok: miss === 0 }); setTimeout(() => apPlay(k, pos), 400); } } else { setBad(i); setMiss(m => m + 1); } };
  const lit = {}, nums = {}; K.forEach((x, j) => { lit[x] = 'pale'; if (done) nums[x] = F[j]; }); found.forEach(x => { lit[x] = 'good'; nums[x] = 1; }); if (bad != null) lit[bad] = 'bad'; lit[K[0]] = lit[K[0]] === 'good' ? 'good' : 'cor';
  const W = apWhite(k);
  return (
    <div className="try-box" style={actBox} data-ap="pos">
      <div style={actTitle}>{t('Arpeggios from every note', '모든 음에서 아르페지오')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>같은 세 음, 시작만 달라요: <b>기본형</b>은 으뜸음에서, <b>첫째 자리바꿈</b>은 3음에서, <b>둘째 자리바꿈</b>은 5음에서. 엄지는 <b>하나뿐인 흰건반</b>에 살아요(E♭장조는 G, F♯단조는 A). 모두 검은건반이면 C장조 모양으로: 엄지가 첫 음에. 엄지가 치는 건반을 모두 눌러요.</>
        : <>The same three notes, a different start: <b>root position</b> starts on the key note, <b>first inversion</b> on the 3rd, <b>second inversion</b> on the 5th. The thumb lives on <b>the one white key</b> (G in E♭ major, A in F♯ minor). All black keys? Use the C-major shape: the thumb on the first note. Tap every key the thumb plays.</>}</div>
      {!fixed && spChips(keys.map(x => [x, apChip(x)]), k, (x) => reset(() => setK(x)))}
      {!fixed && spChips([0, 1, 2].map(p => [p, t(AP_POS[p][0], AP_POS[p][1])]), pos, (x) => reset(() => setPos(x)))}
      {!fixed && spChips([['R', spHand('R')], ['L', spHand('L')]], h, (x) => reset(() => setH(x)))}
      <div style={{textAlign:'center',fontSize:15,fontWeight:900,color:BK.ink,margin:'2px 0 4px'}}>{t(c.en, c.ko)} · {t(AP_POS[pos][0], AP_POS[pos][1])} · {spHand(h)}</div>
      <SpKb lo={K[0] - 1} hi={K[6] + 1} W={17} H={74} lit={lit} names={Object.fromEntries(K.map((x, j) => [x, apNames(k, pos)[j]]))} up={h === 'R' ? nums : {}} dn={h === 'L' ? nums : {}} onTap={tap} label={t(c.en, c.ko)}/>
      {spMsg(done ? t(spHand(h) + ': ' + F.join(' ') + '. ' + (W.length ? 'The thumb on ' + W[0] + ', the white key.' : 'All black: the C-major shape.'), spHand(h) + ': ' + F.join(' ') + '. ' + (W.length ? '엄지는 흰건반 ' + W[0] + '에.' : '모두 검은건반: C장조 모양.'))
        : bad != null ? t(W.length ? 'Not there: find the white key, ' + W[0] + '.' : 'Not there: all black, so the thumb starts each group.', W.length ? '거기가 아니에요: 흰건반 ' + W[0] + '을 찾아요.' : '거기가 아니에요: 모두 검은건반이라 엄지가 묶음마다 시작해요.') : t('Where does the thumb go? ' + found.length + ' of ' + thumbs.length, '엄지는 어디에? ' + thumbs.length + '개 중 ' + found.length), done ? BK.green : bad != null ? BK.coral : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={spBtn} onClick={() => apPlay(k, pos)}>{t('▶ Hear it, hands together', '▶ 양손으로 듣기')}</button>
      </div>
    </div>
  );
}

// ── steps 3 and 4: the dominant 7th and the diminished 7th "of" a key ──
const S7_KEYS = { Fs: 'F♯', Eb: 'E♭', C: 'C', G: 'G', F: 'F', D: 'D', A: 'A', B: 'B', Ab: 'A♭', E: 'E', Bb: 'B♭' };
const s7Pc = (k) => ({ C: 0, D: 2, E: 4, F: 5, G: 7, A: 9, B: 11 })[S7_KEYS[k][0]] + (S7_KEYS[k].includes('♯') ? 1 : S7_KEYS[k].includes('♭') ? -1 : 0);
// the four notes from the bottom, in semitones from middle C, and their names: dominant 7th = degrees 5 7 2 4; diminished 7th = 7 2 4 ♭6
const s7Notes = (k, kind) => { const t0 = ((s7Pc(k) % 12) + 12) % 12, base = kind === 'dom' ? spPc(t0 + 7) - 12 : spPc(t0 - 1) - 12, steps = kind === 'dom' ? [0, 4, 7, 10] : [0, 3, 6, 9];
  const b = base < -7 ? base + 12 : base; return steps.map(x => b + x); };
const s7Names = (k, kind) => (kind === 'dom' ? [[7, 5], [11, 7], [2, 2], [5, 4]] : [[11, 7], [2, 2], [5, 4], [8, 6]]).map(([sm, n]) => l6Spell(S7_KEYS[k], sm, n));
const s7Play = (k, kind, inv = 0, bpm = 60, resolve = true) => { const N = s7Notes(k, kind), up = []; for (let j = 0; j <= 8; j++) { const d = inv + j; up.push(N[d % 4] + 12 * Math.floor(d / 4)); }
  const sq = up.concat(up.slice(0, -1).reverse()), ev = sq.map((x, n) => ({ at: n / 4, keys: [x, x - 12], len: 0.25, vol: 0.12 }));
  if (resolve) { const t0 = ((s7Pc(k) % 12) + 12) % 12, tri = kind === 'dom' ? [0, 4, 7] : [0, 3, 7], end = sq.length / 4 + 0.25; ev.push({ at: end, keys: tri.map(x => t0 + x - 12).concat([t0 - 24]), len: 2, vol: 0.12 }); }
  return spPlay(ev, bpm, 2); };
const S7_FING = {   // the book's fingerings, two octaves up (root position)
  dom: { Fs: { R: [2, 1, 2, 3, 4, 1, 2, 3, 4], L: [2, 1, 4, 3, 2, 1, 4, 3, 2] }, Eb: { R: [2, 1, 2, 3, 4, 1, 2, 3, 4], L: [3, 2, 1, 4, 3, 2, 1, 3, 2] } },
  dim: { Fs: { R: [1, 2, 3, 4, 1, 2, 3, 4, 5], L: [5, 4, 3, 2, 1, 4, 3, 2, 1] }, Eb: { R: [1, 2, 3, 4, 1, 2, 3, 4, 5], L: [5, 4, 3, 2, 1, 4, 3, 2, 1] } },
};
function Sev7Pad({ kind = 'dom', keys = ['Fs', 'Eb', 'C', 'G', 'F'], onResult, fixed, g = 6 }) {
  const [k, setK] = useState(fixed ? fixed.k : keys[0]), [got, setGot] = useState(0), [bad, setBad] = useState(null), [miss, setMiss] = useState(0);
  const N = s7Notes(k, kind), nm = s7Names(k, kind), done = got >= 4, t0 = ((s7Pc(k) % 12) + 12) % 12;
  const reset = (fn) => { setGot(0); setBad(null); setMiss(0); if (fn) fn(); };
  const tap = (i) => { playKey(i, 0.4); if (done) return; if (i === N[got]) { const n = got + 1; setGot(n); setBad(null); if (n >= 4) { if (onResult) onResult({ ok: miss === 0 }); setTimeout(() => s7Play(k, kind), 400); } } else { setBad(i); setMiss(m => m + 1); } };
  const lit = {}; N.slice(0, got).forEach(x => { lit[x] = done ? 'good' : 'cor'; }); if (bad != null) lit[bad] = 'bad';
  const ton = [t0 - 12, t0]; ton.forEach(x => { if (!lit[x] && x >= -12 && x <= 19) lit[x] = 'pale'; });
  const KN = S7_KEYS[k], F = S7_FING[kind][k];
  const ask = got === 0 ? (kind === 'dom' ? t('First the 5th note of ' + KN + ' (the dominant).', '먼저 ' + KN + '의 5번 음(딸림음).') : t('First the leading note: a semitone below ' + KN + '.', '먼저 이끔음: ' + KN + '보다 반음 아래.'))
    : kind === 'dom' ? [null, t('Now a major 3rd up (4 semitones).', '이제 장3도 위(반음 4개).'), t('Now a minor 3rd up (3 semitones).', '이제 단3도 위(반음 3개).'), t('Now the 7th: another minor 3rd up.', '이제 7음: 단3도 하나 더 위.')][got] : t('Now three semitones up (' + got + ' of 3 more).', '이제 반음 셋 위(3개 중 ' + got + ').');
  return (
    <div className="try-box" style={actBox} data-s7={kind}>
      <div style={actTitle}>{kind === 'dom' ? t('The dominant 7th of a key', '어느 조의 딸림7화음') : t('The diminished 7th of a key', '어느 조의 감7화음')}</div>
      <div style={actNote}>{kind === 'dom' ? (LANG === 'ko' ? <>책의 '<b>F♯의 딸림7</b>'은 F♯조 안의 딸림7화음: F♯의 <b>5번 음 C♯</b>에서 시작해요. 장3화음(C♯ E♯ G♯) 위에 단7도(B)를 얹어 <b>네 음</b>. 반음으로 4, 3, 3. 끝에서 으뜸화음으로 풀리고 싶어 해요.</> : <>The book's "<b>dominant 7th of F♯</b>" is the dominant 7th in F♯: it starts on F♯'s <b>5th note, C♯</b>. A major triad (C♯ E♯ G♯) with a minor 7th on top (B): <b>four notes</b>. In semitones: 4, 3, 3. It wants to resolve to the key's tonic chord.</>)
        : (LANG === 'ko' ? <>'<b>F♯의 감7</b>'은 F♯의 <b>이끔음 E♯</b>(반음 아래)에서 시작해요. 네 음이 모두 <b>반음 셋씩</b> 떨어진 고른 계단: E♯ G♯ B D. 어디서 시작해도 모양이 같아요.</> : <>The "<b>diminished 7th of F♯</b>" starts on F♯'s <b>leading note, E♯</b> (a semitone below). Four notes, every gap <b>three semitones</b>: an even staircase, E♯ G♯ B D. It looks the same from any of its notes.</>)}</div>
      {!fixed && spChips(keys.map(x => [x, t('of ' + S7_KEYS[x], S7_KEYS[x] + '의')]), k, (x) => reset(() => setK(x)))}
      <div style={{display:'flex',justifyContent:'center',gap:6,margin:'2px 0 6px'}}>{nm.map((x, j) => <span key={j} style={{minWidth:40,padding:'5px 6px',borderRadius:8,border:'1.5px solid ' + (j === got && !done ? BK.coral : 'rgba(38,41,107,0.25)'),textAlign:'center',fontWeight:900,fontSize:15,color:j < got ? (done ? BK.green : BK.coral) : BK.muted}}>{j < got ? x : '?'}</span>)}</div>
      <SpKb lo={-12} hi={19} W={14} H={70} lit={lit} names={Object.fromEntries(N.slice(0, got).map((x, j) => [x, nm[j]]).concat(ton.filter(x => x >= -12 && x <= 19).map(x => [x, KN])))} onTap={tap} up={done && F && F.R ? Object.fromEntries(N.map((x, j) => [x, F.R[j]])) : {}} label={t('Build the chord', '화음 쌓기')}/>
      {spMsg(done ? t((kind === 'dom' ? 'The dominant 7th of ' : 'The diminished 7th of ') + KN + ': ' + nm.join(' ') + (F ? '. Right hand ' + F.R.join(' ') + '.' : '.'), KN + (kind === 'dom' ? '의 딸림7: ' : '의 감7: ') + nm.join(' ') + (F ? '. 오른손 ' + F.R.join(' ') + '.' : '.'))
        : bad != null ? t('Not that one. ', '그 건반이 아니에요. ') + ask : ask, done ? BK.green : bad != null ? BK.coral : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={spBtn} onClick={() => s7Play(k, kind)}>{t('▶ Hear it, then home', '▶ 듣고, 집으로')}</button>
        {done && !fixed && <button className="ghost-btn" style={spBtn} onClick={() => reset(() => setK(keys[(keys.indexOf(k) + 1) % keys.length]))}>{t('▶ Another key', '▶ 다른 조')}</button>}
      </div>
    </div>
  );
}

// ── make: a harp of arpeggios. Four chords, each swept up (or up and down) over two octaves ──
const AW_KEYS = { C: 0, G: 7, F: 5, Eb: 3 };
const AW_CH = { I: [0, 4, 7], IV: [5, 9, 0], V7: [7, 11, 2, 5], vi: [9, 0, 4], 'vii°7': [11, 2, 5, 8] };
const awNotes = (key, rn) => { const pcs = AW_CH[rn].map(x => (x + key) % 12), root = pcs[0], out = []; let b = root - 24; while (b < -20) b += 12; for (let o = 0; o < 2; o++) pcs.map(p => { let x = p; while (x < root) x += 12; return x - root; }).sort((a, z) => a - z).forEach(d => out.push(b + 12 * o + d)); out.push(b + 24); return out; };
function ArpWave() {
  const T = useSpTimers();
  const [key, setKey] = useState('C'), [seq, setSeq] = useState(['I', 'vi', 'IV', 'V7']), [sel, setSel] = useState(0), [shape, setShape] = useState('updown'), [at, setAt] = useState(-1);
  const play = () => { T.clear(); const ev = []; let b = 0; const marks = [];
    seq.forEach((rn, j) => { const up = awNotes(AW_KEYS[key], rn), run = shape === 'up' ? up : up.concat(up.slice(0, -1).reverse()); marks.push([b, j]); run.forEach((x, n) => ev.push({ at: b + n / 4, keys: [x], len: 0.3, vol: 0.13 })); b += run.length / 4; });
    const lastUp = awNotes(AW_KEYS[key], 'I'); ev.push({ at: b, keys: lastUp.slice(0, 3), len: 2, vol: 0.1 });
    const r = spPlay(ev, 84); if (!r) return; marks.forEach(([bb, j]) => T.at(r.ms(bb), () => setAt(j))); T.at(r.ms(b + 2), () => setAt(-1)); };
  const put = (rn) => { setSeq(q => q.map((x, j) => (j === sel ? rn : x))); setSel((sel + 1) % 4); const up = awNotes(AW_KEYS[key], rn); spPlay(up.map((x, n) => ({ at: n / 6, keys: [x], len: 0.3, vol: 0.12 })), 84); };
  return (
    <div className="try-box" style={actBox} data-mk="wave">
      <div style={actTitle}>{t('My harp of arpeggios', '나의 아르페지오 하프')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>네 화음을 골라요. 화음마다 아르페지오로 두 옥타브를 쓸어 올라가요. 딸림7(V7)과 감7(vii°7)을 넣으면 끝의 I이 얼마나 반가운지 들어 봐요.</> : <>Choose four chords. Each one is swept as an arpeggio over two octaves, like a harp. Put in a V7 or a vii°7 and hear how welcome the final I sounds.</>}</div>
      {spChips(Object.keys(AW_KEYS).map(x => [x, (x === 'Eb' ? 'E♭' : x) + t(' major', '장조')]), key, setKey)}
      <div style={{display:'grid',gridTemplateColumns:'repeat(4,minmax(0,1fr))',gap:6,margin:'4px 0 8px'}}>{seq.map((rn, j) => <button key={j} onClick={() => setSel(j)} aria-pressed={sel === j} style={{minHeight:52,borderRadius:10,border:sel === j ? '2.5px solid ' + BK.coral : '1.5px solid rgba(38,41,107,0.3)',background:at === j ? BK.coral : '#fff',color:at === j ? '#fff' : BK.ink,fontFamily:LB_SERIF,fontSize:18,fontWeight:900,cursor:'pointer'}}>{rn}</button>)}</div>
      <div style={{display:'flex',gap:6,justifyContent:'center',flexWrap:'wrap'}}>{Object.keys(AW_CH).map(rn => <button key={rn} className="chip" onClick={() => put(rn)} style={{minWidth:52,minHeight:44,fontFamily:LB_SERIF,fontSize:16,fontWeight:900}}>{rn}</button>)}</div>
      <div style={{marginTop:8}}>{spChips([['up', t('Up only', '위로만')], ['updown', t('Up and down', '위로, 아래로')]], shape, setShape)}</div>
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap'}}>
        <button className="ghost-btn" style={spBtn} onClick={play}>{t('▶ Play my harp', '▶ 내 하프 듣기')}</button>
      </div>
    </div>
  );
}

// ── the pictures on paper ──
const a6PicWalk = () => lsRawPic('<rect x="4" y="24" width="16" height="16" rx="3" fill="#26296b"/><rect x="4" y="8" width="16" height="14" rx="3" fill="#26296b"/><path d="M24 30 H36" stroke="#e4572e" stroke-width="2.4"/><path d="M32 26 L36 30 L32 34" stroke="#e4572e" stroke-width="2.4" fill="none"/><rect x="40" y="24" width="16" height="16" rx="3" fill="#e4572e"/><rect x="40" y="8" width="16" height="14" rx="3" fill="#26296b"/>', [0, 0, 64, 44]);
const a6PicArp = () => { const m = spMiniKeys(3, 27, { 3: 'pale', 7: 'cor', 10: 'pale', 15: 'pale', 19: 'cor', 22: 'pale', 27: 'pale' }, 6); return { shapes: [{ k: 'raw', svg: m.svg }], vb: [0, 0, m.w, 44] }; };
const a6PicDom = () => lsRawPic([0, 1, 2, 3].map(i => '<ellipse cx="' + (14 + i * 14) + '" cy="' + (36 - i * 9) + '" rx="6" ry="4.4" transform="rotate(-20 ' + (14 + i * 14) + ' ' + (36 - i * 9) + ')" fill="' + (i === 3 ? '#e4572e' : '#26296b') + '"/>').join(''), [0, 0, 72, 44]);
const a6PicDim = () => lsRawPic('<path d="M6 40 H20 V30 H34 V20 H48 V10 H62" fill="none" stroke="#e4572e" stroke-width="2.6"/>' + [0, 1, 2, 3].map(i => '<text x="' + (13 + i * 14) + '" y="' + (37 - i * 10) + '" text-anchor="middle" font-family="Inter, sans-serif" font-size="8" font-weight="900" fill="#26296b">3</text>').join(''), [0, 0, 70, 44]);

function a6LbPages(scr = false) {
  const ch = 'arps-6', s6n = bkChapterNo('scales-6');
  const pen = (x) => <PenArt shapes={x.shapes} vb={x.vb} style={{width:90}}/>;
  const checks = [[a6PicWalk(), t('I play I–V–I from three positions, the note that stays held', '세 자리에서 I–V–I을, 같은 음은 그대로 두고 쳐요')], [a6PicArp(), t('I play the Grade 6 arpeggios from every note of the chord', '6급 아르페지오를 화음의 모든 음에서 쳐요')],
    [a6PicDom(), t('I find and play the dominant 7th of F♯ and of E♭', 'F♯과 E♭의 딸림7화음을 찾아서 쳐요')], [a6PicDim(), t('I find and play the diminished 7th of F♯ and of E♭', 'F♯과 E♭의 감7화음을 찾아서 쳐요')]];
  const toc = [[t('I–V–I from three positions', '세 자리에서 I–V–I'), 2], [t('Arpeggios from every note', '모든 음에서 아르페지오'), 3], [t('The dominant 7th of a key', '어느 조의 딸림7화음'), 4], [t('The diminished 7th of a key', '어느 조의 감7화음'), 5], [t('My four checks', '나의 네 가지 확인'), 6]];
  const walkStill = (k) => <div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr 1fr',gap:10,width:'100%',maxWidth:720,margin:'0 auto'}}>{[1, 2, 3].map(p => <div key={p}><div style={{textAlign:'center',fontSize:13,fontWeight:900,color:BK.ink}}>{t('Position ' + p, '자리 ' + p)}: {CW_GR[6].prog.map(rn => cwChord(k, p, rn).map(i => cwName(k, i)).join(' ')).join(' · ')}</div>
    <SpKb lo={-12} hi={19} W={scr ? 9 : 11} H={scr ? 44 : 54} lit={Object.fromEntries(cwChord(k, p, 'I').map(x => [x, 'cor']).concat(cwChord(k, p, 'V').filter(x => !cwChord(k, p, 'I').includes(x)).map(x => [x, 'pale'])))} names={{}} k={1}/></div>)}</div>;
  const s7Still = (kind) => <div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:14,width:'100%',maxWidth:680,margin:'0 auto'}}>{['Fs', 'Eb'].map(k => { const N = s7Notes(k, kind), nm = s7Names(k, kind);
    return <div key={k}><div style={{textAlign:'center',fontSize:13.5,fontWeight:900,color:BK.ink}}>{kind === 'dom' ? t('Dominant 7th of ' + S7_KEYS[k], S7_KEYS[k] + '의 딸림7') : t('Diminished 7th of ' + S7_KEYS[k], S7_KEYS[k] + '의 감7')}: {nm.join(' ')}</div><SpKb lo={-12} hi={19} W={scr ? 9 : 12} H={scr ? 48 : 60} lit={Object.fromEntries(N.map(x => [x, 'cor']))} names={Object.fromEntries(N.map((x, j) => [x, nm[j]]))} k={1}/></div>; })}</div>;
  return [
    <LbPage key="1" no={1} chId={ch} teacher={<>{spTx(t('The rest of the Grade 6 technical work (chapter ' + s6n + ' has the scales). From the technical work book, Grade 6: I–V–I chord progressions in G, F and A major, from memory, mf, clear even legato, ♩ = ca 72 (alternative fingerings are acceptable); arpeggios root position and inversions, F♯ and E♭ major and minor, four octaves, hands separately and together, mf, ♩ = 60 four notes a beat; dominant 7th arpeggios of F♯ and of E♭ and diminished 7th arpeggios of F♯ and of E♭, four octaves, hands separately and together, mf, ♩ = 60 four notes a beat. "Of F♯" means in F♯: the dominant 7th starts on C♯, the diminished 7th on E♯ (as the book prints them).', '6급 테크닉의 나머지(' + s6n + '장은 스케일). 테크니컬 워크 책 6급: G, F, A장조의 I–V–I 화음 진행, 외워서, mf, 고르고 또렷한 레가토, ♩ = 약 72(다른 운지도 괜찮아요); 아르페지오 기본형과 자리바꿈, F♯·E♭ 장조와 단조, 네 옥타브, 한 손씩 그리고 양손 함께, mf, ♩ = 60 한 박에 네 음; F♯과 E♭의 딸림7 아르페지오와 감7 아르페지오, 네 옥타브, 한 손씩 그리고 양손 함께, mf, ♩ = 60 한 박에 네 음. \'F♯의\'는 F♯조 안에서라는 뜻: 딸림7은 C♯에서, 감7은 E♯에서 시작해요(책에 인쇄된 대로).'))}</>}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:44,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{bkChapterName(ch)}</div>
      </div></LbOnly>
      <LbPic h={140}><div style={{width:'100%'}}>{walkStill('G').props.children[0]}</div></LbPic>
      <LbSay size={18}>{t('Grade 6 chords and arpeggios: a chord walk from three positions, arpeggios from every note, and two new four-note chords, the dominant 7th and the diminished 7th.', '6급 화음과 아르페지오: 세 자리에서 화음 진행, 모든 음에서 아르페지오, 그리고 새로운 네 음 화음 둘, 딸림7과 감7.')}</LbSay>
      <div className="lb-toc" style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>
        <LbOnly print><div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('In this chapter', '이 챕터에서는')}</div>
          {toc.map(([n, p]) => <div key={p} className="lb-toc-row" style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:14.5,padding:'5px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkGoal(15)}{n}</span><span style={{color:BK.muted,fontWeight:700}}>{p}</span></div>)}
        </div></LbOnly>
        <div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 챕터를 마치면')}</div>
          {checks.map(([, x], i) => <div key={i} style={{display:'flex',alignItems:'flex-start',gap:9,fontSize:14.5,padding:'5px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}>{bkGoal(15)}<span>{x.replace(/^I /, '')}</span></div>)}
        </div>
      </div>
      <LbOnly print><LbDrillStrip id={ch}/></LbOnly>
    </LbPage>,
    <LbPage key="2" no={2} chId={ch} kicker={t('Step 1', '1단계')} title={t('I–V–I from three positions', '세 자리에서 I–V–I')}
      teacher={<>{spTx(t('I–V–I in G, F and A major, from memory, mf, legato, ♩ = ca 72, as the book prints it: the right hand\'s chords in three positions, one bar each (G major: B D G – A D F♯ – B D G; D G B – D F♯ A – D G B; G B D – F♯ A D – G B D; fingers 1 2 5 – 1 2 4 – 1 2 5, then 1 3 5 – 1 2 4 – 1 3 5, then 1 3 5 – 1 2 5 – 1 3 5); the left hand the bass, G D G (2 5 2). Alternative fingerings are acceptable. The rule the game teaches: the note common to both chords stays; the others move by a step.', 'G, F, A장조의 I–V–I, 외워서, mf, 레가토, ♩ = 약 72, 책에 인쇄된 대로: 오른손 화음은 세 자리, 한 마디씩(G장조: B D G – A D F♯ – B D G; D G B – D F♯ A – D G B; G B D – F♯ A D – G B D; 손가락 1 2 5 – 1 2 4 – 1 2 5, 그다음 1 3 5 – 1 2 4 – 1 3 5, 그다음 1 3 5 – 1 2 5 – 1 3 5); 왼손은 베이스 G D G(2 5 2). 다른 운지도 괜찮아요. 게임이 가르치는 규칙: 두 화음에 같은 음은 그대로, 나머지는 한 걸음.'))}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=1')}>
      <LbLive still={<LbPic h={150}>{walkStill('G')}</LbPic>} live={<ChordWalkPad g={6}/>}/>
      <LbSay>{LANG === 'ko' ? <>I에서 V로: <b>두 화음에 같은 음은 그대로</b>, 나머지 두 음은 <b>한 걸음씩</b>. 그래서 손이 거의 움직이지 않아요. 자리 1, 2, 3은 맨 위 음이 으뜸음, 3음, 5음.</> : <>From I to V: <b>the note both chords share stays</b>, and the other two move <b>one step each</b>. So the hand hardly moves. Positions 1, 2 and 3 have the key note, the 3rd and the 5th on top.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>G장조, 오른손 B D G. D는 그대로, B는 A로, G는 F♯으로: V.</>, <>다시 B D G로. 왼손은 G, D, G.</>, <>자리 2와 3도, 그다음 F장조와 A장조. 약 {spMM(72)}.</>]
        : [<>G major, the right hand on B D G. Keep D; B to A, G to F♯: that is V.</>, <>Back to B D G. The left hand plays G, D, G.</>, <>Positions 2 and 3, then F and A major. About {spMM(72)}.</>]}/>
      <LbRemember>{t('Keep the note that stays; move the others a step.', '같은 음은 그대로, 나머지는 한 걸음.')}</LbRemember>
    </LbPage>,
    <LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={t('Arpeggios from every note', '모든 음에서 아르페지오')}
      teacher={<>{spTx(t('Arpeggios root position, first and second inversion: F♯ major and minor, E♭ major and minor, four octaves, hands separately and together, mf, ♩ = 60 four notes a beat. The book\'s fingerings, RH (root / 1st / 2nd): F♯ major 1 2 3 1 2 3 5 / 1 2 4 1 2 4 5 / 1 2 4 1 2 4 5; F♯ minor 2 1 2 4 1 2 4 / 1 2 4 1 2 4 5 / 2 4 1 2 4 1 2; E♭ major as F♯ minor; E♭ minor 1 2 3 1 2 3 5 / 1 2 4 1 2 4 5 / 1 2 3 1 2 3 5. LH: F♯ major 5 3 2 1 3 2 1 / 5 4 2 1 4 2 1 / 5 3 2 1 3 2 1; F♯ minor and E♭ major 2 1 4 2 1 4 2 / 5 4 2 1 4 2 1 / 4 2 1 4 2 1 2; E♭ minor 5 4 2 1 4 2 1 / 5 4 2 1 4 2 1 / 5 3 2 1 3 2 1. The pattern behind them (our reading): with one white key the thumb takes it in every position; with all black keys the thumb takes the first note, the C-major shape. The book also allows the root position\'s pattern carried through every inversion.', '아르페지오 기본형, 첫째·둘째 자리바꿈: F♯ 장조·단조, E♭ 장조·단조, 네 옥타브, 한 손씩 그리고 양손 함께, mf, ♩ = 60 한 박에 네 음. 책의 운지, 오른손(기본형 / 첫째 / 둘째): F♯장조 1 2 3 1 2 3 5 / 1 2 4 1 2 4 5 / 1 2 4 1 2 4 5; F♯단조 2 1 2 4 1 2 4 / 1 2 4 1 2 4 5 / 2 4 1 2 4 1 2; E♭장조는 F♯단조와 같음; E♭단조 1 2 3 1 2 3 5 / 1 2 4 1 2 4 5 / 1 2 3 1 2 3 5. 왼손: F♯장조 5 3 2 1 3 2 1 / 5 4 2 1 4 2 1 / 5 3 2 1 3 2 1; F♯단조와 E♭장조 2 1 4 2 1 4 2 / 5 4 2 1 4 2 1 / 4 2 1 4 2 1 2; E♭단조 5 4 2 1 4 2 1 / 5 4 2 1 4 2 1 / 5 3 2 1 3 2 1. 그 뒤의 무늬(우리 해석): 흰건반이 하나면 엄지는 모든 자리에서 그 건반; 모두 검은건반이면 엄지가 첫 음, C장조 모양. 책은 기본형의 무늬를 모든 자리바꿈에 그대로 쓰는 방법도 허용해요.'))}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=2')}>
      <LbLive still={<LbPic h={160}><div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr 1fr',gap:10,width:'100%',maxWidth:720,margin:'0 auto'}}>{[0, 1, 2].map(p => { const K = apKeys('Eb', p), F = AP_DATA.Eb.R[p]; return <div key={p}><div style={{textAlign:'center',fontSize:13,fontWeight:900,color:BK.ink}}>{t('E♭ major, ' + AP_POS[p][0].toLowerCase(), 'E♭장조, ' + AP_POS[p][1])}</div><SpKb lo={K[0] - 1} hi={K[6] + 1} W={scr ? 12 : 14} H={scr ? 50 : 60} lit={Object.fromEntries(K.map((x, j) => [x, F[j] === 1 ? 'cor' : 'pale']))} names={Object.fromEntries(K.map((x, j) => [x, apNames('Eb', p)[j]]))} up={Object.fromEntries(K.map((x, j) => [x, F[j]]))} k={1}/></div>; })}</div></LbPic>} live={<ArpPosPad/>}/>
      <LbSay>{LANG === 'ko' ? <>같은 세 음, 다른 시작. 흰건반이 하나뿐이면 <b>엄지는 언제나 그 흰건반</b>: E♭장조는 G, F♯단조는 A. 모두 검은건반(F♯장조, E♭단조)이면 C장조처럼, 엄지가 첫 음에.</> : <>The same three notes, a different start. With one white key, <b>the thumb always takes it</b>: G in E♭ major, A in F♯ minor. All black keys (F♯ major, E♭ minor)? Like C major, the thumb on the first note.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>E♭장조, 오른손: 기본형 2 1 2 4, 첫째 자리바꿈 1 2 4, 둘째 자리바꿈 2 4 1. 엄지는 언제나 G.</>, <>F♯장조: 1 2 3, 1 2 4, 1 2 4. 엄지가 첫 음.</>, <>네 옥타브, 양손 함께, 한 박에 네 음. {spMM(60)}까지.</>]
        : [<>E♭ major, right hand: root position 2 1 2 4, first inversion 1 2 4, second inversion 2 4 1. The thumb is always on G.</>, <>F♯ major: 1 2 3, 1 2 4, 1 2 4. The thumb on the first note.</>, <>Four octaves, hands together, four notes a beat. Up to {spMM(60)}.</>]}/>
      <LbRemember>{t('One white key: the thumb lives there.', '흰건반이 하나면: 엄지는 거기에.')}</LbRemember>
    </LbPage>,
    <LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title={t('The dominant 7th of a key', '어느 조의 딸림7화음')}
      teacher={<>{spTx(t('Dominant 7th arpeggios of F♯ (C♯ E♯ G♯ B) and of E♭ (B♭ D F A♭), root position, four octaves, hands separately and together, mf, ♩ = 60 four notes a beat. Fingering: RH 2 1 2 3 4 1 2 3 4 for both; LH of F♯ 2 1 4 3 2 1 4 3 2, of E♭ 3 2 1 4 3 2 1 3 2. The chord: the key\'s 5th note, a major 3rd, a perfect 5th and a minor 7th above it (degrees 5, 7, 2 and 4 of the key). Grade 7 adds its inversions.', 'F♯의 딸림7(C♯ E♯ G♯ B)과 E♭의 딸림7(B♭ D F A♭) 아르페지오, 기본형, 네 옥타브, 한 손씩 그리고 양손 함께, mf, ♩ = 60 한 박에 네 음. 운지: 오른손 둘 다 2 1 2 3 4 1 2 3 4; 왼손 F♯의 2 1 4 3 2 1 4 3 2, E♭의 3 2 1 4 3 2 1 3 2. 화음: 그 조의 5번 음, 그 위 장3도, 완전5도, 단7도(그 조의 5, 7, 2, 4번 음). 7급에 자리바꿈이 더해져요.'))}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=3')}>
      <LbLive still={<LbPic h={150}>{s7Still('dom')}</LbPic>} live={<Sev7Pad kind="dom"/>}/>
      <LbSay>{LANG === 'ko' ? <>조의 <b>5번 음</b>에서 장3화음, 그 위에 <b>단7도</b> 하나: 네 음. 반음으로 4, 3, 3. 듣고 나면 집(으뜸화음)으로 가고 싶어져요.</> : <>From the key's <b>5th note</b>: a major triad, with <b>a minor 7th</b> on top: four notes. In semitones, 4, 3, 3. Hear it, and you want to go home to the tonic chord.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>F♯조의 5번 음 C♯을 찾아요. C♯ E♯ G♯, 그 위에 B.</>, <>오른손 2 1 2 3, 그다음 4 1 2 3 4.</>, <>E♭의 딸림7: B♭ D F A♭. 네 옥타브, {spMM(60)}까지.</>]
        : [<>Find F♯'s 5th note, C♯. Then C♯ E♯ G♯, with B on top.</>, <>Right hand 2 1 2 3, then 4 1 2 3 4.</>, <>The dominant 7th of E♭: B♭ D F A♭. Four octaves, up to {spMM(60)}.</>]}/>
      <LbRemember>{t('Of F♯: start on its 5th, C♯.', 'F♯의 딸림7: 5번 음 C♯에서.')}</LbRemember>
    </LbPage>,
    <LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title={t('The diminished 7th of a key', '어느 조의 감7화음')}
      teacher={<>{spTx(t('Diminished 7th arpeggios of F♯ (E♯ G♯ B D) and of E♭ (D F A♭ C♭), four octaves, hands separately and together, mf, ♩ = 60 four notes a beat. Fingering: RH 1 2 3 4 1 2 3 4 5, LH 5 4 3 2 1 4 3 2 1, for both. The chord: the key\'s leading note and three minor 3rds above it (degrees 7, 2, 4 and the minor 6th of the harmonic minor), every gap three semitones; its spelling follows the key (C♭, not B).', 'F♯의 감7(E♯ G♯ B D)과 E♭의 감7(D F A♭ C♭) 아르페지오, 네 옥타브, 한 손씩 그리고 양손 함께, mf, ♩ = 60 한 박에 네 음. 운지: 둘 다 오른손 1 2 3 4 1 2 3 4 5, 왼손 5 4 3 2 1 4 3 2 1. 화음: 그 조의 이끔음과 그 위 단3도 셋(화성 단음계의 7, 2, 4번 음과 단6도), 모든 간격이 반음 셋; 이름은 그 조를 따라요(B가 아니라 C♭).'))}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=4')}>
      <LbLive still={<LbPic h={150}>{s7Still('dim')}</LbPic>} live={<><Sev7Pad kind="dim"/><div style={{height:12}}/><ArpWave/></>}/>
      <LbSay>{LANG === 'ko' ? <>조의 <b>이끔음</b>(으뜸음보다 반음 아래)에서 시작해서 <b>반음 셋씩</b> 네 번: 고른 계단. 아래에 '아르페지오 하프': 감7과 딸림7을 넣고 끝의 I을 들어 봐요.</> : <>Start on the key's <b>leading note</b> (a semitone below the key note) and climb <b>three semitones</b> at a time: an even staircase. Below, the harp of arpeggios: put in a diminished 7th and a dominant 7th, and hear the final I.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>F♯보다 반음 아래, E♯(F 건반)를 찾아요. E♯ G♯ B D.</>, <>오른손 1 2 3 4, 그다음 1 2 3 4 5. 왼손 5 4 3 2 1.</>, <>E♭의 감7: D F A♭ C♭. 네 옥타브, {spMM(60)}까지.</>]
        : [<>A semitone below F♯: E♯ (the F key). E♯ G♯ B D.</>, <>Right hand 1 2 3 4, then 1 2 3 4 5. Left hand 5 4 3 2 1.</>, <>The diminished 7th of E♭: D F A♭ C♭. Four octaves, up to {spMM(60)}.</>]}/>
      <LbRemember>{t('Three semitones, four times: an even staircase.', '반음 셋씩 네 번: 고른 계단.')}</LbRemember>
    </LbPage>,
    <LbPage key="6" no={6} chId={ch} kicker={t('Check-up', '점검')} title={t('My four checks', '나의 네 가지 확인')}
      teacher={<>{t('Each one played to you from memory, as the book asks: the progressions in G, F and A from three positions; the arpeggios in every position, hands together; the two dominant and two diminished 7ths. Listen for a held common note, an even thumb, and the 7ths named before they are played.', '하나씩 외워서, 책이 요구하는 대로: G, F, A장조 진행을 세 자리에서; 아르페지오를 모든 자리에서 양손으로; 딸림7과 감7 둘씩. 같은 음을 붙잡고 있는지, 엄지가 고른지, 치기 전에 7화음의 이름을 말하는지 들어 주세요.')}</>}>
      <LbSay>{t('At the piano, tick each one: not yet, nearly, or got it!', '피아노 앞에서 하나씩 표시해요: 아직, 거의, 됐어요!')}</LbSay>
      <LbLive still={<LbStageRows big rows={checks.map(([a, txt]) => [pen(a), txt])}/>} live={<FiveChecks376 rows={checks} storeKey="pb_a6_four"/>}/>
    </LbPage>,
  ];
}
function Arps6LessonBook() { return <>{a6LbPages(false)}</>; }
function A6Learn({ onStart }) {
  const pages = a6LbPages(true), opener = pages[0];
  return (
    <Lesson id="arps-6" title={bkChapterName('arps-6')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="arps-6"><div className="lb-screen lb-open" style={{display:'flex',flexDirection:'column',gap:12,margin:'0 0 8px'}}>{lbWordsFirst(opener.props.children)}</div></BkChapterCtx.Provider></LbScreenCtx.Provider>}>
      {pages.slice(1).map((pg, i) => <Step key={i} title={pg.props.title}><LbScreenPage page={pg}/></Step>)}
    </Lesson>
  );
}
// ── the drill ──
const A6_LEVELS = [
  { n: 1, label: 'I–V–I: which note stays?', kind: 'walk', time: 15 },
  { n: 2, label: 'Arpeggios: which note does the thumb play?', kind: 'thumb', time: 15 },
  { n: 3, label: 'The dominant 7th of a key: its notes', kind: 'dom', time: 20 },
  { n: 4, label: 'The diminished 7th of a key: its notes', kind: 'dim', time: 20 },
];
Object.assign(LEVEL_KO, { 'I–V–I: which note stays?': 'I–V–I: 그대로인 음은?', 'Arpeggios: which note does the thumb play?': '아르페지오: 엄지가 치는 음은?', 'The dominant 7th of a key: its notes': '어느 조의 딸림7: 그 음들', 'The diminished 7th of a key: its notes': '어느 조의 감7: 그 음들' });
const s7Wrong = (k, kind) => { const right = s7Names(k, kind).join(' '), other = Object.keys(S7_KEYS).filter(x => x !== k), outs = [];
  outs.push(s7Names(k, kind === 'dom' ? 'dim' : 'dom').join(' ')); outs.push(s7Names(pick(other), kind).join(' '));
  const tw = s7Names(k, kind).slice(); tw[3] = l6Spell(S7_KEYS[k], kind === 'dom' ? 4 : 9, kind === 'dom' ? 3 : 6); outs.push(tw.join(' '));
  return [...new Set(outs.filter(x => x !== right))].slice(0, 3); };
function genA6Question(lv, prev) {
  const uid = Math.random(), kind = lv.kind;
  if (kind === 'walk') { let k, pos, g = 0; do { k = pick(CW_GR[6].keys); pos = pick([1, 2, 3]); } while (prev && prev.key === k + pos && g++ < 10); const I = cwChord(k, pos, 'I'), V = cwChord(k, pos, 'V'), st = I.filter(x => V.includes(x))[0];
    return { kind, k, pos, answer: cwName(k, st), choices: I.map(x => cwName(k, x)), key: k + pos, uid }; }
  if (kind === 'thumb') { let k, pos, g = 0; do { k = pick(['Eb', 'Fsm', 'Fs', 'Ebm']); pos = pick([0, 1, 2]); } while (prev && prev.key === k + pos && g++ < 10); const K = apKeys(k, pos), F = AP_DATA[k].R[pos], j = F.indexOf(1);
    return { kind, k, pos, answer: apNames(k, pos)[j], choices: AP_DATA[k].nm.slice(), key: k + pos, uid }; }
  let k, g = 0; do { k = pick(['Fs', 'Eb', 'C', 'G', 'F', 'D']); } while (prev && prev.key === kind + k && g++ < 10); const right = s7Names(k, kind).join(' ');
  return { kind, k, answer: right, choices: shuffle([right].concat(s7Wrong(k, kind))), key: kind + k, uid };
}
function A6Question({ q, given, locked, onAnswer, pixel }) {
  const done = !!given;
  const btnCls = pixel ? 'pixel-choice' : 'choice-btn', cls = (c) => btnCls + (!done ? '' : c === q.answer ? ' good' : given.ans === c ? ' bad' : '');
  const pickIt = (c) => { if (locked || done) return; stopClicks(); onAnswer(c); };
  const grid = (cols, items) => <div style={{display:'grid',gridTemplateColumns:'repeat(' + cols + ',minmax(0,1fr))',gap:8,marginTop:10}}>{items.map(([c, lab]) => <button key={String(c)} disabled={locked} className={cls(c)} style={{padding:'12px 4px',fontSize:15,fontWeight:900}} onClick={() => pickIt(c)}>{lab}</button>)}</div>;
  let title, body;
  if (q.kind === 'walk') { const I = cwChord(q.k, q.pos, 'I'), V = cwChord(q.k, q.pos, 'V'), lit = Object.fromEntries(I.map(x => [x, 'cor'])); if (done) V.forEach(x => { lit[x] = I.includes(x) ? 'good' : 'pale'; });
    title = t(CW_KEY[q.k][1] + ' major, I in position ' + q.pos + ': moving to V, which note stays?', CW_KEY[q.k][1] + '장조, 자리 ' + q.pos + '의 I: V로 갈 때 그대로인 음은?'); body = <><SpKb lo={-12} hi={19} W={12} H={60} lit={lit} names={Object.fromEntries(I.concat(done ? V : []).map(x => [x, cwName(q.k, x)]))}/>{grid(3, q.choices.map(c => [c, c]))}</>; }
  else if (q.kind === 'thumb') { const K = apKeys(q.k, q.pos), nm = apNames(q.k, q.pos), F = AP_DATA[q.k].R[q.pos];
    title = t(AP_DATA[q.k].en + ', ' + AP_POS[q.pos][0].toLowerCase() + ', right hand: which note does the thumb play?', AP_DATA[q.k].ko + ', ' + AP_POS[q.pos][1] + ', 오른손: 엄지가 치는 음은?');
    body = <><SpKb lo={K[0] - 1} hi={K[6] + 1} W={15} H={62} lit={Object.fromEntries(K.map((x, j) => [x, done && F[j] === 1 ? 'good' : 'pale']))} names={Object.fromEntries(K.map((x, j) => [x, nm[j]]))} up={done ? Object.fromEntries(K.map((x, j) => [x, F[j]])) : {}}/>{grid(3, q.choices.map(c => [c, c]))}</>; }
  else { title = q.kind === 'dom' ? t('The dominant 7th of ' + S7_KEYS[q.k] + ': which notes?', S7_KEYS[q.k] + '의 딸림7화음: 어떤 음들?') : t('The diminished 7th of ' + S7_KEYS[q.k] + ': which notes?', S7_KEYS[q.k] + '의 감7화음: 어떤 음들?'); body = grid(1, q.choices.map(c => [c, c])); }
  const why = !done || pixel ? null : q.kind === 'walk' ? t('The note both chords share stays; the others move a step.', '두 화음에 같은 음은 그대로, 나머지는 한 걸음.') : q.kind === 'thumb' ? t(apWhite(q.k).length ? 'The one white key, ' + apWhite(q.k)[0] + ', takes the thumb.' : 'All black keys: the thumb starts each group of three.', apWhite(q.k).length ? '하나뿐인 흰건반 ' + apWhite(q.k)[0] + '에 엄지.' : '모두 검은건반: 엄지가 세 음 묶음마다 시작.')
    : q.kind === 'dom' ? t('From ' + S7_KEYS[q.k] + '\'s 5th note: 4, 3, 3 semitones.', S7_KEYS[q.k] + '의 5번 음에서: 반음 4, 3, 3.') : t('From ' + S7_KEYS[q.k] + '\'s leading note: 3, 3, 3 semitones.', S7_KEYS[q.k] + '의 이끔음에서: 반음 3, 3, 3.');
  return (<div>
    <p style={pixel ? {fontSize:11.5,textAlign:'center'} : {fontSize:15,fontWeight:700,textAlign:'center',margin:'0 0 8px',color:'var(--muted)',textWrap:'balance'}}>{title}</p>
    {body}
    {why && <div style={{marginTop:10,fontSize:13.5,color:'#4a4d86',background:'#fff',borderRadius:8,padding:'7px 10px',lineHeight:1.45}}>{why}</div>}
  </div>);
}
Object.assign(ARPS_6_DRILL, { levels: A6_LEVELS, generate: genA6Question, check: (q, ans) => ans !== null && ans !== undefined && ans === q.answer, answerLabel: (q) => String(q.answer), Question: A6Question, Learn: A6Learn });
// the teacher's copy
const A6_WB = {
  walk: [['G', 1], ['G', 2], ['F', 3], ['A', 1]],
  thumb: [['Eb', 0], ['Fsm', 2], ['Fs', 1], ['Ebm', 0]],
  dom: ['Fs', 'Eb', 'G', 'F'],
  dim: ['Fs', 'Eb', 'C', 'A'],
  chk: { walk: [['F', 1], ['A', 2], ['G', 3], ['F', 2]], thumb: [['Fsm', 0], ['Eb', 1], ['Eb', 2], ['Fs', 0]], dom: ['C', 'D', 'Fs', 'Eb'], dim: ['G', 'D', 'Fs', 'Eb'] },
};
function A6Teacher() {
  const pages = [], W = A6_WB;
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="arps-6" teacher>{content}</WbPage>);
  const walkAns = ([k, p]) => CW_KEY[k][1] + ' pos. ' + p + ': V = ' + cwChord(k, p, 'V').map(x => cwName(k, x)).join(' ');
  const thumbAns = ([k, p]) => AP_DATA[k].en + ', ' + AP_POS[p][0].toLowerCase() + ': RH ' + AP_DATA[k].R[p].join(' ') + ' (thumb ' + apNames(k, p)[AP_DATA[k].R[p].indexOf(1)] + ')';
  P(<>
    <div style={{fontFamily:LB_SERIF,fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('arps-6')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 12px',lineHeight:1.5}}>{spTx('The keys, speeds and fingerings are the technical work book\'s (Grade 6 pp36–41). Progressions and arpeggios from memory; arpeggios four octaves (the book prints two). Another fingering is fine if it is logical and systematic.')}</div>
    <TcBlock page={2} title="I–V–I from three positions" answers={<>{tcAns('TRY IT', W.walk.map(walkAns))}{tcAns(spTx('G, F AND A MAJOR, mf, ♩ = ca 72, RH IN THREE POSITIONS, LH 2 5 2'), CW_GR[6].keys.map(k => CW_KEY[k][1] + ': ' + [1, 2, 3].map(p => CW_GR[6].prog.map(rn => cwChord(k, p, rn).map(x => cwName(k, x)).join(' ')).join(' – ')).join(' | ')), null)}</>}
      watch="Lifting the whole hand to the next chord instead of holding the common note. Say the note that stays before playing."
      say="“Keep the note that stays; move the others a step.”"/>
    <TcBlock page={3} title="Arpeggios from every note" answers={<>{tcAns('TRY IT', W.thumb.map(thumbAns))}{tcAns(spTx('FOUR OCTAVES, HANDS SEPARATELY AND TOGETHER, mf, ♩ = 60 FOUR NOTES A BEAT'), Object.keys(AP_DATA).map(k => AP_DATA[k].en + ': RH ' + AP_DATA[k].R.map(f => f.join(' ')).join(' / ') + ' · LH ' + AP_DATA[k].L.map(f => f.join(' ')).join(' / ')), null)}</>}
      watch="A thumb that lands on a black key where a white key waits (E♭ major, F♯ minor). In F♯ major and E♭ minor the thumb starts each group, as in C."
      say="“One white key: the thumb lives there.”"/>
  </>);
  P(<>
    <TcBlock page={4} title="The dominant 7th of a key" answers={<>{tcAns('TRY IT', W.dom.map(k => 'of ' + S7_KEYS[k] + ': ' + s7Names(k, 'dom').join(' ')))}{tcAns(spTx('OF F♯ AND OF E♭, FOUR OCTAVES, mf, ♩ = 60'), ['of F♯: C♯ E♯ G♯ B, RH 2 1 2 3 4 1 2 3 4, LH 2 1 4 3 2 1 4 3 2', 'of E♭: B♭ D F A♭, RH 2 1 2 3 4 1 2 3 4, LH 3 2 1 4 3 2 1 3 2'], null)}</>}
      watch="Starting on the key note (F♯) instead of its 5th (C♯); E♯ called F."
      say="“Of F♯: start on its 5th, C♯.”"/>
    <TcBlock page={5} title="The diminished 7th of a key" answers={<>{tcAns('TRY IT', W.dim.map(k => 'of ' + S7_KEYS[k] + ': ' + s7Names(k, 'dim').join(' ')))}{tcAns(spTx('OF F♯ AND OF E♭, FOUR OCTAVES, mf, ♩ = 60'), ['of F♯: E♯ G♯ B D', 'of E♭: D F A♭ C♭', 'RH 1 2 3 4 1 2 3 4 5, LH 5 4 3 2 1 4 3 2 1'], null)}</>}
      watch="A gap of four semitones somewhere (a C♭ played as C). Every gap is three."
      say="“Three semitones, four times: an even staircase.”"/>
    <TcBlock page={6} title="The check-up on paper (the Workbook's last page)" answers={<>{tcAns('A', W.chk.walk.map(([k, p]) => cwChord(k, p, 'V').map(x => cwName(k, x)).join(' ')))}{tcAns('B', W.chk.thumb.map(([k, p]) => apNames(k, p)[AP_DATA[k].R[p].indexOf(1)]), 5)}{tcAns('C', W.chk.dom.map(k => s7Names(k, 'dom').join(' ')), 9)}{tcAns('D', W.chk.dim.map(k => s7Names(k, 'dim').join(' ')), 13)}
      <div style={{fontSize:12,color:BK.ink,marginTop:6,lineHeight:1.5}}>One mark for each answer. Score each part on its own (4 marks each, pass 3+). Not passed? Go back to that step's page: A p.2 · B p.3 · C p.4 · D p.5. Then hear each one at the piano, from memory, at the book's speeds.</div></>}/>
  </>);
  return <>{pages}</>;
}
TEACHER_COPIES['arps-6'] = A6Teacher;
// ─── Arpeggios and Progressions, Grade 6: the Workbook ───
function A6Workbook({ startNo = 1 }) {
  const W = A6_WB, pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + 1 + pages.length} chId="arps-6">{content}</WbPage>);
  const kbCell = (lit, names, lo = -12, hi = 19) => <SpKb lo={lo} hi={hi} W={8} H={30} lit={lit} names={names} k={1}/>;
  P(<>
    <WbTop step={1}/>
    <Part kind="together" title="From I to V" how="The coral keys are I. Write the three notes of V: keep the note that stays, move the others one step.">
      <BkGrid cols={2} gap="6px 10px">{W.walk.map(([k, p], i) => { const I = cwChord(k, p, 'I'), V = cwChord(k, p, 'V'); return <ExCell key={i} n={i + 1} ex={i === 0}><div style={{display:'grid',gap:4,padding:'16px 4px 4px'}}>
        {s4wLabel(CW_KEY[k][1] + ' major, position ' + p + ': I = ' + I.map(x => cwName(k, x)).join(' '))}{kbCell(Object.fromEntries(I.map(x => [x, 'cor'])), Object.fromEntries(I.map(x => [x, cwName(k, x)])))}
        <div style={{display:'flex',alignItems:'center',justifyContent:'center',gap:6,fontSize:11.5,fontWeight:800,color:BK.ink}}>V: {nvBox(i === 0, V.map(x => cwName(k, x)).join(' '), 90, 26)}</div></div></ExCell>; })}</BkGrid>
    </Part>
    <Part kind="home" title="The walk this week" how="Tick a box each day.">
      <PhLog rows={s4wRows(['G major, position 1: B D G – A D F♯ – B D G, the left hand G D G', 'Positions 2 and 3; then F major', 'A major too, from memory, at about ♩ = 72'])} label={300}/>
    </Part>
    <Faces/>
  </>);
  P(<>
    <WbTop step={2}/>
    <Part kind="together" title="Where is the thumb?" how="Two octaves of each arpeggio, right hand. Write the note the thumb plays.">
      <BkGrid cols={2} gap="6px 10px">{W.thumb.map(([k, p], i) => { const K = apKeys(k, p), nm = apNames(k, p); return <ExCell key={i} n={i + 1} ex={i === 0}><div style={{display:'grid',gap:4,padding:'16px 4px 4px'}}>
        {s4wLabel(AP_DATA[k].en + ', ' + AP_POS[p][0].toLowerCase())}{kbCell(Object.fromEntries(K.map(x => [x, 'pale'])), Object.fromEntries(K.map((x, j) => [x, nm[j]])), K[0] - 1, K[6] + 1)}
        <div style={{display:'flex',alignItems:'center',justifyContent:'center',gap:6,fontSize:11.5,fontWeight:800,color:BK.ink}}>thumb: {nvBox(i === 0, nm[AP_DATA[k].R[p].indexOf(1)], 40, 26)}</div></div></ExCell>; })}</BkGrid>
    </Part>
    <Part kind="home" title="Arpeggios this week" how="Tick a box each day.">
      <PhLog rows={s4wRows(['E♭ major, every position, each hand: the thumb on G', 'F♯ minor (the thumb on A), then F♯ major and E♭ minor (the C-major shape)', 'Hands together, four octaves, up to ♩ = 60'])} label={300}/>
    </Part>
    <Faces/>
  </>);
  P(<>
    <WbTop step={3}/>
    <Part kind="together" title="Build the dominant 7th" how="Start on the key's 5th note; add a major 3rd, then a minor 3rd, then another minor 3rd. Write the four notes.">
      <BkGrid cols={2} gap="6px 10px">{W.dom.map((k, i) => <ExCell key={k} n={i + 1} ex={i === 0}><div style={{display:'grid',gap:4,padding:'16px 4px 4px',justifyItems:'center'}}>
        {s4wLabel('The dominant 7th of ' + S7_KEYS[k])}{nvBox(i === 0, s7Names(k, 'dom').join(' '), 130, 28)}</div></ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Dominant 7ths this week" how="Tick a box each day.">
      <PhLog rows={s4wRows(['Of F♯: C♯ E♯ G♯ B, then home to F♯', 'Of E♭: B♭ D F A♭, then home to E♭', 'Four octaves, hands together, up to ♩ = 60'])} label={300}/>
    </Part>
    <Faces/>
  </>);
  P(<>
    <WbTop step={4}/>
    <Part kind="together" title="Build the diminished 7th" how="Start on the key's leading note (a semitone below the key note) and add three minor 3rds. Write the four notes, spelt for the key.">
      <BkGrid cols={2} gap="6px 10px">{W.dim.map((k, i) => <ExCell key={k} n={i + 1} ex={i === 0}><div style={{display:'grid',gap:4,padding:'16px 4px 4px',justifyItems:'center'}}>
        {s4wLabel('The diminished 7th of ' + S7_KEYS[k])}{nvBox(i === 0, s7Names(k, 'dim').join(' '), 130, 28)}</div></ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Diminished 7ths this week" how="Tick a box each day.">
      <PhLog rows={s4wRows(['Of F♯: E♯ G♯ B D, RH 1 2 3 4', 'Of E♭: D F A♭ C♭, LH 5 4 3 2 1', 'Four octaves, hands together, up to ♩ = 60'])} label={300}/>
    </Part>
    <Faces/>
  </>);
  P(<A6PaperCheck/>);
  return <>{pages}</>;
}
function A6PaperCheck() {
  const C = A6_WB.chk;
  return <div className="lb-paper" style={{display:'flex',flexDirection:'column',gap:4}}>
    <LbPaperHead/>
    {bkSec('A', 'I is given: write V, the note that stays held')}
    <BkGrid cols={4} gap="6px 8px">{C.walk.map(([k, p], i) => <BkCell key={i} n={i + 1}><div style={{display:'grid',gap:4,padding:'14px 0 0',justifyItems:'center',fontSize:11,fontWeight:800,color:BK.ink,textAlign:'center'}}>{CW_KEY[k][1] + ' major: I = ' + cwChord(k, p, 'I').map(x => cwName(k, x)).join(' ')}{bkBox(80, 24)}</div></BkCell>)}</BkGrid>
    {bkSec('B', 'Arpeggio, right hand: which note does the thumb play?')}
    <BkGrid cols={4} gap="6px 8px">{C.thumb.map(([k, p], i) => <BkCell key={i} n={i + 5}><div style={{display:'grid',gap:4,padding:'14px 0 0',justifyItems:'center',fontSize:11,fontWeight:800,color:BK.ink,textAlign:'center'}}>{AP_DATA[k].en + ', ' + AP_POS[p][0].toLowerCase()}{bkBox(44, 24)}</div></BkCell>)}</BkGrid>
    {bkSec('C', 'The dominant 7th of …: its four notes')}
    <BkGrid cols={4} gap="6px 8px">{C.dom.map((k, i) => <BkCell key={i} n={i + 9}><div style={{display:'grid',gap:4,padding:'14px 0 0',justifyItems:'center',fontSize:11,fontWeight:800,color:BK.ink}}>{'of ' + S7_KEYS[k]}{bkBox(100, 24)}</div></BkCell>)}</BkGrid>
    {bkSec('D', 'The diminished 7th of …: its four notes')}
    <BkGrid cols={4} gap="6px 8px">{C.dim.map((k, i) => <BkCell key={i} n={i + 13}><div style={{display:'grid',gap:4,padding:'14px 0 0',justifyItems:'center',fontSize:11,fontWeight:800,color:BK.ink}}>{'of ' + S7_KEYS[k]}{bkBox(100, 24)}</div></BkCell>)}</BkGrid>
  </div>;
}
WORKBOOKS['arps-6'] = A6Workbook;
'''
rep("""TEACHER_COPIES['scales-6'] = S6Teacher;""", """TEACHER_COPIES['scales-6'] = S6Teacher;""" + CH)

HOME = r'''
// ══ Build BQ: Arpeggios and Progressions, Grade 6 on the Home (Technique, Playing scales) ══
LBH_FN['arps-6'] = (s) => a6LbPages(s);
const a6HomeAdd = (id, i, en, ko, benEn, bko, make) => lbhAdd(id, 'k-play', 'tech', en, ko, benEn, bko, lbhSpec('arps-6', i, { make }));
const a6S7Q = (kind) => (n, prev) => { let k, g = 0; do { k = pick(['Fs', 'Eb', 'C', 'G', 'F', 'D']); } while (prev && prev.key === k && g++ < 10); const right = s7Names(k, kind).join(' '), opts = shuffle([right].concat(s7Wrong(k, kind)));
  return { kind: 'choice', cols: 1, key: k, prompt: [(kind === 'dom' ? 'The dominant 7th of ' : 'The diminished 7th of ') + S7_KEYS[k] + ': which notes?', S7_KEYS[k] + (kind === 'dom' ? '의 딸림7화음' : '의 감7화음') + ': 어떤 음들?'], opts: opts.map(x => ({ id: x, label: () => x })), ans: right, ok: (v) => v === right,
    play: () => s7Play(k, kind), fig: (c) => ({ mid: c.res ? <SpKb lo={-12} hi={19} W={12} H={60} lit={Object.fromEntries(s7Notes(k, kind).map(x => [x, 'cor']))} names={Object.fromEntries(s7Notes(k, kind).map((x, j) => [x, s7Names(k, kind)[j]]))}/> : null }),
    yes: ['Yes: ' + right + '.', '맞아요: ' + right + '.'], no: ['It was ' + right + (kind === 'dom' ? ': from the 5th note, 4, 3, 3 semitones.' : ': from the leading note, three semitones each time.'), right + (kind === 'dom' ? '였어요: 5번 음에서 반음 4, 3, 3.' : '였어요: 이끔음에서 반음 셋씩.')] }; };
a6HomeAdd('a6-walk', 1, 'I–V–I from three positions', '세 자리에서 I–V–I', 'Keep the note that stays; move the others a step.', '같은 음은 그대로, 나머지는 한 걸음.', lwTapQ(ChordWalkPad, (n) => ({ fixed: { k: CW_GR[6].keys[n % 3], pos: 1 + (n % 3) } }), ['Tap the three notes of the next chord.', '다음 화음의 세 음을 눌러요.'], ['Walked ✓', '진행했어요 ✓']));
a6HomeAdd('a6-arp', 2, 'Arpeggios from every note', '모든 음에서 아르페지오', 'The thumb lives on the one white key.', '엄지는 하나뿐인 흰건반에.', lwTapQ(ArpPosPad, (n) => ({ fixed: { k: ['Eb', 'Fsm', 'Fs', 'Ebm'][n % 4], pos: n % 3, h: n % 2 ? 'L' : 'R' } }), ['Tap every key the thumb plays.', '엄지가 치는 건반을 모두 눌러요.'], ['Found them ✓', '찾았어요 ✓']));
a6HomeAdd('a6-dom', 3, 'The dominant 7th of a key', '어느 조의 딸림7화음', 'Start on the key\'s 5th note: 4, 3, 3 semitones.', '조의 5번 음에서: 반음 4, 3, 3.', a6S7Q('dom'));
a6HomeAdd('a6-dim', 4, 'The diminished 7th of a key', '어느 조의 감7화음', 'Start on the leading note: three semitones, four times.', '이끔음에서: 반음 셋씩 네 번.', a6S7Q('dim'));
'''
rep("""
lbhAdd('rb-finger', 'r-beat', 'rhythm', 'The beat in your fingers'""", HOME + """
lbhAdd('rb-finger', 'r-beat', 'rhythm', 'The beat in your fingers'""")
rep("""check: 'scales-6' },   // Build BP""", """check: 'scales-6' },   // Build BP
    { id: 'kpl-a6', en: 'Arpeggios and progressions, Grade 6', ko: '아르페지오와 화음 진행, Grade 6', lessons: ['a6-walk', 'a6-arp', 'a6-dom', 'a6-dim', 'mk-wave'], check: 'arps-6' },   // Build BQ""")
rep("""  set('6', 's6-four s6-dyn s6-grand s6-ls s6-mirror s6-poly mk-poly');   // Build BP: Scales, Grade 6""", """  set('6', 's6-four s6-dyn s6-grand s6-ls s6-mirror s6-poly mk-poly');   // Build BP: Scales, Grade 6
  set('6', 'a6-walk a6-arp a6-dom a6-dim mk-wave');   // Build BQ: Arpeggios and Progressions, Grade 6""")
rep("""  { id: 'mk-poly', ch: 'scales-6',""", """  { id: 'mk-wave', ch: 'arps-6', title: 'My harp of arpeggios', blurb: 'Four chords swept as arpeggios over two octaves; a V7 or a diminished 7th before the last I.', C: () => <ArpWave/> },   // Build BQ
  { id: 'mk-poly', ch: 'scales-6',""")
rep("""  'mk-poly': ['나의 폴리리듬 밴드',""", """  'mk-wave': ['나의 아르페지오 하프', '네 화음을 두 옥타브 아르페지오로 쓸어 올려요; 마지막 I 앞에 V7이나 감7.'],
  'mk-poly': ['나의 폴리리듬 밴드',""")
rep("""'mk-poly': ['rrhythm', 3, 3, 'game ear'],""", """'mk-poly': ['rrhythm', 3, 3, 'game ear'], 'mk-wave': ['chords', 3, 3, 'game ear'],""")
rep("""  'mk-poly': () => (\n""", """  'mk-wave': () => (
    <svg width="34" height="34" viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#3f9a7e"/><path d="M3 17 L7 11 L11 7 L15 11 L19 17 L21 14" fill="none" stroke="#fefbf3" strokeWidth="2" strokeLinejoin="round"/>{[3, 7, 11, 15, 19].map((x, i) => <circle key={i} cx={x} cy={[17, 11, 7, 11, 17][i]} r="1.8" fill="#e9a83a"/>)}</svg>
  ),
  'mk-poly': () => (\n""")
rep("""const LESSON_BOOKS = { 'scales-6': Scales6LessonBook,""", """const LESSON_BOOKS = { 'arps-6': Arps6LessonBook, 'scales-6': Scales6LessonBook,""")
rep("""const LB_PAGE_FNS = { 'scales-6': s6LbPages,""", """const LB_PAGE_FNS = { 'arps-6': a6LbPages, 'scales-6': s6LbPages,""")
rep("""const HOUSE_ICONS = {""", """const HOUSE_ICONS = {"arps-6": "<ellipse cx=\\"10\\" cy=\\"36\\" rx=\\"4.4\\" ry=\\"3.3\\" transform=\\"rotate(-20 10 36)\\" fill=\\"#26296b\\"/><ellipse cx=\\"19\\" cy=\\"28\\" rx=\\"4.4\\" ry=\\"3.3\\" transform=\\"rotate(-20 19 28)\\" fill=\\"#26296b\\"/><ellipse cx=\\"28\\" cy=\\"20\\" rx=\\"4.4\\" ry=\\"3.3\\" transform=\\"rotate(-20 28 20)\\" fill=\\"#26296b\\"/><ellipse cx=\\"37\\" cy=\\"12\\" rx=\\"4.4\\" ry=\\"3.3\\" transform=\\"rotate(-20 37 12)\\" fill=\\"#e4572e\\" stroke=\\"#e4572e\\"/><path d=\\"M6 40 L42 8\\" stroke-dasharray=\\"2 3\\" stroke-width=\\"1.2\\"/>", """)
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
