p='drills.src.html'; s=open(p).read()
if 'XTRA_SCALES' in s: print('already'); raise SystemExit
def rep(old, new, cnt=1):
    global s
    assert s.count(old)==cnt, (s.count(old), old[:90])
    s=s.replace(old,new)
rep("splitDrill(SCALES_1_DRILL, SCALE_PLAY_DRILL, [4, 7, 8], (p) => <SpLearn part=\"1\" {...p}/>);   // m40",
    "splitDrill(SCALES_1_DRILL, SCALE_PLAY_DRILL, [4, 7, 8, 9], (p) => <SpLearn part=\"1\" {...p}/>);   // m40; m48: 9 = the extra step")
rep("splitDrill(SCALES_3_DRILL, SCALES_23_DRILL, [3, 4, 5], S3Learn);   // Build DJ",
    "splitDrill(SCALES_3_DRILL, SCALES_23_DRILL, [3, 4, 5, 7], S3Learn);   // Build DJ; m48: 7 = the extra step")
i = s.index("Object.assign(SCALES_7_DRILL, {"); j = s.index("\n", i) + 1
MOD = r'''
// ══ m48 (her 1-2 Nov: 'scales must teach everything worth learning, even what is not on the exam'): an Extra step in six scale rooms.
// Each is marked 'not on the exam'. A question shows a scale on the keys (with its sound) and asks which scale it is, or, for the
// enharmonic pairs, which other name the same keys have. The why line teaches the pattern. Patterns are semitones from the tonic.
const XP = { mel: [0, 2, 3, 5, 7, 9, 11, 12], maj: [0, 2, 4, 5, 7, 9, 11, 12], nat: [0, 2, 3, 5, 7, 8, 10, 12], mp: [0, 2, 4, 7, 9, 12], np: [0, 3, 5, 7, 10, 12], blues: [0, 3, 5, 6, 7, 10, 12], wt: [0, 2, 4, 6, 8, 10, 12],
  dor: [0, 2, 3, 5, 7, 9, 10, 12], mix: [0, 2, 4, 5, 7, 9, 10, 12], phr: [0, 1, 3, 5, 7, 8, 10, 12], loc: [0, 1, 3, 5, 6, 8, 10, 12] };
const XW = {
  mel: ['Melodic minor: going up, the 6th and 7th are raised by a semitone; coming down, it is the natural minor.', '가락 단음계: 올라갈 때 6도와 7도를 반음 올리고, 내려올 때는 자연 단음계.'],
  mp: ['Major pentatonic: the major scale without its 4th and 7th. Five notes and no semitones, so nothing clashes.', '장조 5음 음계: 장음계에서 4도와 7도를 뺀 다섯 음. 반음이 없어 부딪히는 음이 없어요.'],
  np: ['Minor pentatonic: the natural minor without its 2nd and 6th. Five notes, found in folk songs and the blues.', '단조 5음 음계: 자연 단음계에서 2도와 6도를 뺀 다섯 음. 민요와 블루스에 많아요.'],
  blues: ['Blues scale: the minor pentatonic with one extra blue note, the flattened 5th.', '블루스 음계: 단조 5음 음계에 블루 노트(낮춘 5도) 하나를 더해요.'],
  wt: ['Whole-tone scale: every step is a tone, so it has only six notes. With no semitones it floats, with no home note.', '온음 음계: 모든 간격이 온음이라 여섯 음뿐. 반음이 없어 중심음 없이 떠다니는 느낌이에요.'],
  dor: ['Dorian: a natural minor with a raised 6th. On the white keys it runs from D to D.', '도리아: 6도를 올린 자연 단음계. 흰건반으로 D에서 D까지.'],
  mix: ['Mixolydian: a major scale with a lowered 7th. On the white keys it runs from G to G.', '믹솔리디아: 7도를 내린 장음계. 흰건반으로 G에서 G까지.'],
  phr: ['Phrygian: a natural minor with a lowered 2nd. On the white keys it runs from E to E.', '프리지아: 2도를 내린 자연 단음계. 흰건반으로 E에서 E까지.'],
  loc: ['Locrian: on the white keys from B to B. Its 5th is diminished, so it never quite settles.', '로크리아: 흰건반으로 B에서 B까지. 5도가 감5도라 좀처럼 안정되지 않아요.'],
};
// [id, scale name (en, ko), lowest note (midi), pattern, why, the note names, wrong answers]
const XS = (id, en, ko, r, pat, why, nm, wrong) => ({ id, en, ko, r, pat, why, nm: nm.split(' '), wrong });
const XTRA_ITEMS = {
  amel: XS('amel', 'A melodic minor', 'A 가락 단음계', 57, 'mel', 'mel', 'A B C D E F♯ G♯ A', ['A harmonic minor', 'A major']),
  emel: XS('emel', 'E melodic minor', 'E 가락 단음계', 52, 'mel', 'mel', 'E F♯ G A B C♯ D♯ E', ['E harmonic minor', 'E major']),
  dmel: XS('dmel', 'D melodic minor', 'D 가락 단음계', 62, 'mel', 'mel', 'D E F G A B C♯ D', ['D harmonic minor', 'D major']),
  bmel: XS('bmel', 'B melodic minor', 'B 가락 단음계', 59, 'mel', 'mel', 'B C♯ D E F♯ G♯ A♯ B', ['B harmonic minor', 'B major']),
  cmp: XS('cmp', 'C major pentatonic', 'C 장조 5음 음계', 60, 'mp', 'mp', 'C D E G A C', ['C major', 'A minor pentatonic']),
  gmp: XS('gmp', 'G major pentatonic', 'G 장조 5음 음계', 55, 'mp', 'mp', 'G A B D E G', ['G major', 'E minor pentatonic']),
  fmp: XS('fmp', 'F major pentatonic', 'F 장조 5음 음계', 53, 'mp', 'mp', 'F G A C D F', ['F major', 'D minor pentatonic']),
  anp: XS('anp', 'A minor pentatonic', 'A 단조 5음 음계', 57, 'np', 'np', 'A C D E G A', ['A natural minor', 'C major pentatonic']),
  enp: XS('enp', 'E minor pentatonic', 'E 단조 5음 음계', 52, 'np', 'np', 'E G A B D E', ['E natural minor', 'G major pentatonic']),
  fsmel: XS('fsmel', 'F♯ melodic minor', 'F♯ 가락 단음계', 54, 'mel', 'mel', 'F♯ G♯ A B C♯ D♯ E♯ F♯', ['F♯ harmonic minor', 'F♯ major']),
  cbl: XS('cbl', 'C blues scale', 'C 블루스 음계', 60, 'blues', 'blues', 'C E♭ F F♯ G B♭ C', ['C minor pentatonic', 'C natural minor']),
  abl: XS('abl', 'A blues scale', 'A 블루스 음계', 57, 'blues', 'blues', 'A C D D♯ E G A', ['A minor pentatonic', 'A natural minor']),
  cwt: XS('cwt', 'C whole-tone scale', 'C 온음 음계', 60, 'wt', 'wt', 'C D E F♯ G♯ A♯ C', ['C major', 'C chromatic']),
  ebmel: XS('ebmel', 'E♭ melodic minor', 'E♭ 가락 단음계', 51, 'mel', 'mel', 'E♭ F G♭ A♭ B♭ C D E♭', ['E♭ harmonic minor', 'E♭ major']),
  ddor: XS('ddor', 'D Dorian', 'D 도리아', 62, 'dor', 'dor', 'D E F G A B C D', ['D natural minor', 'G Mixolydian']),
  gmix: XS('gmix', 'G Mixolydian', 'G 믹솔리디아', 55, 'mix', 'mix', 'G A B C D E F G', ['G major', 'D Dorian']),
  ephr: XS('ephr', 'E Phrygian', 'E 프리지아', 52, 'phr', 'phr', 'E F G A B C D E', ['E natural minor', 'B Locrian']),
  bloc: XS('bloc', 'B Locrian', 'B 로크리아', 59, 'loc', 'loc', 'B C D E F G A B', ['B natural minor', 'E Phrygian']),
  dphr: XS('dphr', 'A Phrygian', 'A 프리지아', 57, 'phr', 'phr', 'A B♭ C D E F G A', ['A natural minor', 'A Locrian']),
};
// the enharmonic pairs (Level 5): same keys, two names
const XTRA_ENH = [
  { id: 'csdb', a: 'C♯ major', b: 'D♭ major', r: 61, pat: 'maj', nm: 'C♯ D♯ E♯ F♯ G♯ A♯ B♯ C♯', wrong: ['D major', 'C major'], why: ['C♯ major has 7 sharps; D♭ major, on the same keys, has 5 flats. Most players read D♭.', 'C♯ 장조는 샵 7개, 같은 건반의 D♭ 장조는 플랫 5개. 대부분 D♭로 읽어요.'] },
  { id: 'cbb', a: 'C♭ major', b: 'B major', r: 59, pat: 'maj', nm: 'C♭ D♭ E♭ F♭ G♭ A♭ B♭ C♭', wrong: ['C major', 'B♭ major'], why: ['C♭ major has 7 flats; B major, on the same keys, has 5 sharps.', 'C♭ 장조는 플랫 7개, 같은 건반의 B 장조는 샵 5개.'] },
  { id: 'asbb', a: 'A♯ minor', b: 'B♭ minor', r: 58, pat: 'nat', nm: 'A♯ B♯ C♯ D♯ E♯ F♯ G♯ A♯', wrong: ['A minor', 'B minor'], why: ['A♯ minor has 7 sharps; B♭ minor, on the same keys, has 5 flats.', 'A♯ 단조는 샵 7개, 같은 건반의 B♭ 단조는 플랫 5개.'] },
  { id: 'abgs', a: 'A♭ minor', b: 'G♯ minor', r: 56, pat: 'nat', nm: 'A♭ B♭ C♭ D♭ E♭ F♭ G♭ A♭', wrong: ['A minor', 'G minor'], why: ['A♭ minor has 7 flats; G♯ minor, on the same keys, has 5 sharps.', 'A♭ 단조는 플랫 7개, 같은 건반의 G♯ 단조는 샵 5개.'] },
];
const xtraLevel = (n, en, ko, xs, enh) => { LEVEL_KO[en] = ko; return { n, label: en, kind: 'xtra', xs, enh: !!enh, extra: true, time: 20 }; };
const XTRA_SCALES = {
  'scales-1': xtraLevel(9, 'Extra: melodic minor in A, E and D', '보너스: A·E·D 가락 단음계', ['amel', 'emel', 'dmel']),
  'scales-23': xtraLevel(6, 'Extra: pentatonic scales and B melodic minor', '보너스: 5음 음계와 B 가락 단음계', ['bmel', 'cmp', 'gmp', 'fmp', 'anp', 'enp']),
  'scales-3': xtraLevel(7, 'Extra: blues, whole-tone and F♯ melodic minor', '보너스: 블루스, 온음 음계, F♯ 가락 단음계', ['fsmel', 'cbl', 'abl', 'cwt']),
  'scales-5': xtraLevel(0, 'Extra: same keys, two names', '보너스: 같은 건반, 두 이름', null, true),
  'scales-6': xtraLevel(0, 'Extra: Dorian, Mixolydian and E♭ melodic minor', '보너스: 도리아, 믹솔리디아, E♭ 가락 단음계', ['ebmel', 'ddor', 'gmix']),
  'scales-7': xtraLevel(0, 'Extra: Phrygian and Locrian', '보너스: 프리지아와 로크리아', ['ephr', 'dphr', 'bloc', 'ddor', 'gmix']),
};
function genXtra(lv, prev) {
  const uid = Math.random();
  if (lv.enh) { let e, g = 0; do { e = pick(XTRA_ENH); } while (prev && prev.key === e.id && g++ < 10); const keys = e.pat ? XP[e.pat].map(o => e.r + o) : [];
    return { kind: 'xtra', enh: true, e, keys, nm: e.nm.split(' '), answer: e.b, choices: shuffle([e.b, ...e.wrong]), key: e.id, uid }; }
  let x, g = 0; do { x = XTRA_ITEMS[pick(lv.xs)]; } while (prev && prev.key === x.id && g++ < 10);
  return { kind: 'xtra', x, keys: XP[x.pat].map(o => x.r + o), nm: x.nm, answer: x.en, choices: shuffle([x.en, ...x.wrong]), key: x.id, uid };
}
function xtraPlay(keys) { const ctx = getAudio(); if (!ctx) return; stopClicks(); const seq = [...keys, ...keys.slice(0, -1).reverse()]; seq.forEach((m, i) => blip(ctx, ctx.currentTime + 0.08 + i * 0.28, 440 * Math.pow(2, (m - 69) / 12), 0.26, 0.2, 'triangle')); }
function XtraQuestion({ q, given, locked, onAnswer, pixel }) {
  const done = !!given, btnCls = pixel ? 'pixel-choice' : 'choice-btn';
  const cls = (c) => btnCls + (!done ? '' : c === q.answer ? ' good' : given.ans === c ? ' bad' : '');
  useEffect(() => { xtraPlay(q.keys); }, [q.uid]);
  const lit = {}, names = {}; q.keys.forEach((m, j) => { lit[m] = done ? 'good' : 'pale'; if (done) names[m] = q.nm[j]; });
  const lo = q.keys[0] - (spIsW(q.keys[0]) ? 0 : 1), hi = q.keys[q.keys.length - 1] + (spIsW(q.keys[q.keys.length - 1]) ? 0 : 1);
  const title = q.enh ? t(q.e.a + ' is played on these keys. What is its other name?', q.e.a + '는 이 건반으로 쳐요. 다른 이름은?') : t('Listen and look: which scale is this?', '듣고 보세요: 어떤 음계일까요?');
  const why = !done || pixel ? null : q.enh ? t(q.e.why[0], q.e.why[1]) : t(XW[q.x.why][0], XW[q.x.why][1]);
  return (<div data-testid="xtra-q">
    {!pixel && <div style={{textAlign:'center',fontSize:10.5,fontWeight:900,letterSpacing:'0.1em',textTransform:'uppercase',color:'var(--coral)',marginBottom:4}}>{t('Extra · not on the exam', '보너스 · 시험에는 안 나와요')}</div>}
    <p style={pixel ? {fontSize:11.5,textAlign:'center'} : {fontSize:15,fontWeight:700,textAlign:'center',margin:'0 0 8px',color:'var(--muted)',textWrap:'balance'}}>{title}</p>
    <SpKb lo={lo} hi={hi} W={26} H={76} lit={lit} names={names}/>
    <div style={{textAlign:'center',margin:'6px 0 2px'}}><button type="button" className="chip" onClick={() => xtraPlay(q.keys)} style={{padding:'4px 12px',fontSize:13}}>{t('♪ Hear it again', '♪ 다시 듣기')}</button></div>
    <div style={{display:'grid',gridTemplateColumns:'minmax(0,1fr)',gap:8,marginTop:8}}>{q.choices.map(c => <button key={c} disabled={locked} className={cls(c)} style={{padding:'12px 6px',fontSize:pixel ? 13 : 15.5,fontWeight:800}} onClick={() => { if (!locked && !done) onAnswer(c); }}>{q.enh || LANG !== 'ko' ? c : ((Object.values(XTRA_ITEMS).find(x => x.en === c) || {}).ko || c)}</button>)}</div>
    {why && <p style={{fontSize:13.5,lineHeight:1.45,color:'var(--navy)',margin:'10px 0 0',textAlign:'center'}}>{why}</p>}
  </div>);
}
function xtraWrap(D) {
  const g = D.generate, c = D.check, a = D.answerLabel, Q = D.Question;
  D.generate = (lv, prev) => (lv && lv.kind === 'xtra' ? genXtra(lv, prev) : g(lv, prev));
  D.check = (q, ans) => (q && q.kind === 'xtra' ? ans === q.answer : c(q, ans));
  D.answerLabel = (q) => (q && q.kind === 'xtra' ? q.answer : a(q));
  D.Question = (p) => (p.q && p.q.kind === 'xtra' ? <XtraQuestion {...p}/> : <Q {...p}/>);
}
// the steps join their rooms: Scales, Level 1 and Grade 3 are sub-rooms (their base gets the step, the split names it)
SP_LEVELS.push(XTRA_SCALES['scales-1']); xtraWrap(SCALE_PLAY_DRILL);
SCF_LEVELS.push(XTRA_SCALES['scales-23'], XTRA_SCALES['scales-3']); SCALES_23_DRILL.allLevels = SCF_LEVELS; SCALES_23_DRILL.levels = SCF_LEVELS.filter(l => l.n !== 7); xtraWrap(SCALES_23_DRILL);
[[SCALES_5_DRILL, 'scales-5'], [SCALES_6_DRILL, 'scales-6'], [SCALES_7_DRILL, 'scales-7']].forEach(([D, id]) => { const lv = XTRA_SCALES[id]; lv.n = Math.max(...D.levels.map(l => l.n)) + 1; D.levels = [...D.levels, lv]; xtraWrap(D); });
'''
s = s[:j] + MOD + s[j:]
open(p,'w').write(s); print('ok')
