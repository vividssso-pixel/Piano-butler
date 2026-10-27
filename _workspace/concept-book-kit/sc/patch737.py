import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build BR (board call 26, the fourth Grade 6 room): Chords and Cadences, Grade 6, Theory of Music Grade 6, the last graded theory
# exam (Manual of Syllabuses 2026, Theory of Music Grade 6, read 28 Oct): the vocabulary I II III IV V VI with their first
# inversions, cadential Ic, passing Ic, IVc and Vc, V7 V7b V7c V7d, accented and unaccented passing notes and auxiliary notes,
# single suspensions, the tierce de Picardie (minor keys only); modulation within the six related keys; harmonising a melody or
# an unfigured bass in four parts; a part above or below a given part in two-part keyboard style. Five steps, the last one a
# thing to make (call 25): a tune written above a bass, checked as it is written. What the room says about figures, passing
# six-fours and the decorations is textbook harmony from my own knowledge: on the board's list of things for Sohyun to check.

rep("""const HARMONY_5_DRILL = { id: 'harmony-5', label: 'Chords and Cadences, Grade 5' };   // Build BC""",
    """const HARMONY_5_DRILL = { id: 'harmony-5', label: 'Chords and Cadences, Grade 5' };   // Build BC
const HARMONY_6_DRILL = { id: 'harmony-6', label: 'Chords and Cadences, Grade 6' };   // Build BR""")
rep("""  { id: 'harmony-5', label: 'Chords and Cadences, Grade 5', concept: HARMONY_5_DRILL, track: 'start' },   // Build BC""",
    """  { id: 'harmony-5', label: 'Chords and Cadences, Grade 5', concept: HARMONY_5_DRILL, track: 'start' },   // Build BC
  { id: 'harmony-6', label: 'Chords and Cadences, Grade 6', concept: HARMONY_6_DRILL, track: 'start' },   // Build BR""")
rep("""'harmony-5': '화음과 종지, Grade 5'""", """'harmony-5': '화음과 종지, Grade 5', 'harmony-6': '화음과 종지, Grade 6'""")
rep("""'harmony-5': 'p-chords'""", """'harmony-5': 'p-chords', 'harmony-6': 'p-chords'""")
rep("""'harmony-5': ['harmony-4', 'keys-5']""", """'harmony-5': ['harmony-4', 'keys-5'], 'harmony-6': ['harmony-5']""")
rep("""'harmony-5': ['Chords 5', '화음 5']""", """'harmony-5': ['Chords 5', '화음 5'], 'harmony-6': ['Chords 6', '화음 6']""")
rep("""  'harmony-5': 'chords cadences grade 5""", """  'harmony-6': 'chords cadences grade 6 theory dominant seventh V7 inversions figured bass six five four three four two passing six four suspension accented passing note auxiliary tierce de picardie picardy third modulation six related keys two part counterpoint',
  'harmony-5': 'chords cadences grade 5""")

CH = r'''
// ─── Chapter: Chords and Cadences, Grade 6 (Build BR, 2026-10-28; board call 26, the fourth Grade 6 room; Theory of Music Grade 6) ───
// Four-part chords are [bass, tenor, alto, soprano] in semitones from middle C, in C major (A minor for the Picardy third);
// h6T moves them to another key. Each chord lasts two beats unless it says otherwise.
const h6T = (ch, k) => ch.map(x => x + k);
// c.hold: the top note goes on sounding into the next chord (tied); c.split: the top part of this chord as [[note or null, beats], …],
// null meaning the note tied over from before
const h6Play = (chords, bpm = 66, k = 0) => { const ev = []; let at = 0; chords.forEach(c => { const len = c.len || 2;
  if (c.split || c.hold) ev.push({ at, keys: h6T(c.v.slice(0, 3), k), len, vol: 0.11 }); else ev.push({ at, keys: h6T(c.v, k), len, vol: 0.11 });
  if (c.hold) ev.push({ at, keys: [c.v[3] + k], len: len + c.hold, vol: 0.13 });
  if (c.split) { let a = at; c.split.forEach(([x, d]) => { if (x != null) ev.push({ at: a, keys: [x + k], len: d, vol: 0.13 }); a += d; }); }
  at += len; }); return spPlay(ev, bpm); };
const H6_KEYS = { C: [0, 'C'], G: [-5, 'G'], F: [5, 'F'], D: [2, 'D'], Bb: [-2, 'B♭'] };   // G and B♭ sit below C so every chord fits the keyboard
// ── step 1: V7 and its three inversions, each resolving: the 7th falls, the leading note rises ──
const H6_V7 = {
  a: { nm: 'V7', fig: '7', ko: 'V7', bassDeg: 5, v: [-17, -1, 5, 14], to: [-12, 0, 4, 12], toNm: 'I' },
  b: { nm: 'V7b', fig: '6 5', ko: 'V7b', bassDeg: 7, v: [-13, -5, 2, 5], to: [-12, -5, 0, 4], toNm: 'I' },
  c: { nm: 'V7c', fig: '4 3', ko: 'V7c', bassDeg: 2, v: [-10, -5, -1, 5], to: [-12, -5, 0, 4], toNm: 'I' },
  d: { nm: 'V7d', fig: '4 2', ko: 'V7d', bassDeg: 4, v: [-7, -5, -1, 2], to: [-8, -5, 0, 4], toNm: 'Ib' },
};
const H6_INV = ['a', 'b', 'c', 'd'];
const h6Let = (k, x) => { const s = spPc(x - H6_KEYS[k][0]); return l6Spell(H6_KEYS[k][1], s, { 0: 1, 2: 2, 4: 3, 5: 4, 7: 5, 9: 6, 11: 7 }[s] || 1); };
const h6Fig = (f) => f === '7' ? null : <span style={{display:'inline-grid',lineHeight:0.95,fontSize:12,fontWeight:900,verticalAlign:'middle',marginLeft:3}}>{f.split(' ').map((x, i) => <span key={i}>{x}</span>)}</span>;
function H6V7Pad({ onResult, fixed }) {
  const [k, setK] = useState(fixed ? fixed.k : 'C'), [inv, setInv] = useState(fixed ? fixed.inv : 'a'), [quiz, setQuiz] = useState(!!fixed), [ans, setAns] = useState(null);
  const c = H6_V7[inv], kk = H6_KEYS[k][0], V = h6T(c.v, kk), lit = {}; V.forEach((x, j) => { lit[x] = j === 0 ? 'cor' : 'pale'; });
  const play = () => h6Play([{ v: c.v }, { v: c.to, len: 3 }], 66, kk);
  const ask = () => { let x, g = 0; do { x = pick(H6_INV); } while (x === inv && g++ < 10); setInv(x); setK(pick(Object.keys(H6_KEYS))); setQuiz(true); setAns(null); };
  const say = (x) => { if (!quiz || ans) return; setAns(x); if (onResult) onResult({ ok: x === inv }); };
  const show = !quiz || ans;
  return (
    <div className="try-box" style={actBox} data-h6="v7">
      <div style={actTitle}>{t('V7 and its inversions', 'V7과 그 자리바꿈')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>딸림7화음은 네 음이라 자리가 넷: 베이스가 <b>근음</b>이면 V7(숫자 7), <b>3음</b>(이끔음)이면 V7b(6 5), <b>5음</b>이면 V7c(4 3), <b>7음</b>이면 V7d(4 2). 풀릴 때 <b>7음은 한 걸음 내려가고</b>, <b>이끔음은 한 걸음 올라가요</b>. 빨간 건반이 베이스.</>
        : <>The dominant 7th has four notes, so four positions: the bass on <b>the root</b> is V7 (figured 7), on <b>the 3rd</b> (the leading note) V7b (6 5), on <b>the 5th</b> V7c (4 3), on <b>the 7th</b> V7d (4 2). When it resolves, <b>the 7th falls a step</b> and <b>the leading note rises a step</b>. The coral key is the bass.</>}</div>
      {!quiz && spChips(Object.keys(H6_KEYS).map(x => [x, H6_KEYS[x][1] + t(' major', '장조')]), k, (x) => { setK(x); setAns(null); })}
      {!quiz && spChips(H6_INV.map(x => [x, H6_V7[x].nm]), inv, (x) => { setInv(x); setAns(null); })}
      <div style={{textAlign:'center',fontSize:15,fontWeight:900,color:BK.ink,margin:'2px 0 4px'}}>{H6_KEYS[k][1] + t(' major', '장조')} · {show ? <>{c.nm}{h6Fig(c.fig)} · {t('bass: ', '베이스: ') + h6Let(k, V[0]) + t(' (degree ' + c.bassDeg + ')', '(' + c.bassDeg + '번 음)')}</> : t('Which one? Look at the bass.', '어느 것? 베이스를 봐요.')}</div>
      <SpKb lo={-24} hi={20} W={11} H={66} lit={lit} names={Object.fromEntries(V.map(x => [x, h6Let(k, x)]))} label={t('The chord', '화음')}/>
      {quiz && !ans && <div style={{display:'grid',gridTemplateColumns:'repeat(4,minmax(0,1fr))',gap:6,marginTop:8}}>{H6_INV.map(x => <button key={x} className="choice-btn" onClick={() => say(x)} style={{padding:'10px 2px',fontSize:15,fontWeight:900}}>{H6_V7[x].nm}</button>)}</div>}
      {spMsg(quiz && !ans ? t('The bass is ' + h6Let(k, V[0]) + ': which degree of ' + H6_KEYS[k][1] + ' major is it?', '베이스는 ' + h6Let(k, V[0]) + ': ' + H6_KEYS[k][1] + '장조의 몇 번 음?') : ans ? (ans === inv ? t('Yes: ' + c.nm + ', the bass on degree ' + c.bassDeg + '.', '맞아요: ' + c.nm + ', 베이스가 ' + c.bassDeg + '번 음.') : t('It was ' + c.nm + ': the bass on degree ' + c.bassDeg + '.', '정답은 ' + c.nm + ': 베이스가 ' + c.bassDeg + '번 음.'))
        : t(c.nm + ' goes to ' + c.toNm + ': ' + h6Let(k, V[3]) + (c.v[3] > c.to[3] ? ' falls' : ' rises') + ', the 7th (' + h6Let(k, kk + 5) + ') falls.', c.nm + ' → ' + c.toNm + ': 7음(' + h6Let(k, kk + 5) + ')은 내려가요.'), ans ? (ans === inv ? BK.green : BK.coral) : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={spBtn} onClick={play}>{t('▶ ' + c.nm + ' then ' + c.toNm, '▶ ' + c.nm + ', 그다음 ' + c.toNm)}</button>
        {!fixed && <button className="ghost-btn" style={spBtn} onClick={ask}>{t('▶ Which one?', '▶ 어느 것일까?')}</button>}
        {quiz && !fixed && <button className="ghost-btn" style={spBtn} onClick={() => { setQuiz(false); setAns(null); }}>{t('Back to all four', '네 가지 다시 보기')}</button>}
      </div>
    </div>
  );
}
// ── step 2: passing six-fours (the bass walks by step) or the cadential six-four (the bass stays for V) ──
const H6_64 = {
  passV: { en: 'I – Vc – Ib', ko: 'I – Vc – Ib', kind: 'pass', bass: ['C', 'D', 'E'], seq: [{ v: [-12, 0, 7, 16] }, { v: [-10, -1, 7, 14], len: 1 }, { v: [-8, 0, 7, 12], len: 3 }], mid: 1 },
  passI: { en: 'IV – Ic – IVb', ko: 'IV – Ic – IVb', kind: 'pass', bass: ['F', 'G', 'A'], seq: [{ v: [-7, 5, 9, 12] }, { v: [-5, 4, 7, 12], len: 1 }, { v: [-3, 0, 5, 12], len: 3 }], mid: 1 },
  cad: { en: 'Ic – V – I', ko: 'Ic – V – I', kind: 'cad', bass: ['G', 'G', 'C'], seq: [{ v: [-5, 0, 4, 12] }, { v: [-5, -1, 2, 11] }, { v: [-12, 0, 4, 12], len: 3 }], mid: 0 },
};
function H6SixFourPad({ onResult, fixed }) {
  const [id, setId] = useState(fixed ? fixed.id : 'passV'), [quiz, setQuiz] = useState(!!fixed), [ans, setAns] = useState(null);
  const x = H6_64[id], show = !quiz || ans;
  const ask = () => { const y = pick(Object.keys(H6_64)); setId(y); setQuiz(true); setAns(null); h6Play(H6_64[y].seq); };
  const say = (v) => { if (!quiz || ans) return; setAns(v); if (onResult) onResult({ ok: v === x.kind }); };
  return (
    <div className="try-box" style={actBox} data-h6="64">
      <div style={actTitle}>{t('Passing six-fours', '경과 6-4화음')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>6-4화음(둘째 자리바꿈)은 두 가지로 와요. <b>경과 6-4</b>: 베이스가 <b>한 걸음씩 걸어가는</b> 가운데에 잠깐(I–Vc–Ib, IV–Ic–IVb). <b>종지 6-4</b>: 강박의 Ic, 베이스는 <b>그대로 V로</b>(5급).</>
        : <>A six-four (a second inversion) comes two ways. <b>Passing</b>: briefly, in the middle of a bass that <b>walks by step</b> (I–Vc–Ib, IV–Ic–IVb). <b>Cadential</b>: Ic on a strong beat, the bass <b>staying put</b> for V (Grade 5).</>}</div>
      {!quiz && spChips(Object.keys(H6_64).map(y => [y, t(H6_64[y].en, H6_64[y].ko)]), id, (y) => { setId(y); setAns(null); h6Play(H6_64[y].seq); })}
      <div style={{display:'flex',justifyContent:'center',gap:10,margin:'6px 0'}}>{x.bass.map((b, j) => <div key={j} style={{textAlign:'center'}}><div style={{fontFamily:LB_SERIF,fontSize:17,fontWeight:900,color:show && j === x.mid ? BK.coral : BK.ink}}>{show ? x.en.split(' – ')[j] : '?'}</div><div style={{marginTop:2,width:40,height:40,borderRadius:20,border:'2px solid ' + BK.ink,display:'flex',alignItems:'center',justifyContent:'center',fontWeight:900,color:BK.ink}}>{b}</div></div>)}</div>
      <div style={{textAlign:'center',fontSize:12.5,fontWeight:800,color:BK.muted}}>{t('the bass, in C major', '베이스, C장조')}</div>
      {quiz && !ans && <div style={{display:'grid',gridTemplateColumns:'repeat(2,minmax(0,1fr))',gap:8,marginTop:8}}>{[['pass', t('Passing: the bass walks', '경과: 베이스가 걸어요')], ['cad', t('Cadential: the bass stays', '종지: 베이스가 머물러요')]].map(([v, lab]) => <button key={v} className="choice-btn" onClick={() => say(v)} style={{padding:'12px 4px',fontSize:14,fontWeight:900}}>{lab}</button>)}</div>}
      {spMsg(ans ? (ans === x.kind ? t('Yes: ' + x.en + '.', '맞아요: ' + x.ko + '.') : t('It was ' + x.en + ': ' + (x.kind === 'pass' ? 'the bass walked ' + x.bass.join(' ') + '.' : 'the bass stayed on G for V.'), '정답은 ' + x.ko + ': ' + (x.kind === 'pass' ? '베이스가 ' + x.bass.join(' ') + '로 걸었어요.' : '베이스가 V를 위해 G에 머물렀어요.'))) : quiz ? t('Listen to the bass: walking or staying?', '베이스를 들어요: 걸어가요, 머물러요?') : x.kind === 'pass' ? t('The six-four sits between two positions of one chord, on a bass that walks.', '6-4는 한 화음의 두 자리 사이, 걸어가는 베이스 위에.') : t('Ic, then V on the same bass, then I.', 'Ic, 같은 베이스 위의 V, 그다음 I.'), ans ? (ans === x.kind ? BK.green : BK.coral) : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={spBtn} onClick={() => h6Play(x.seq)}>{t('▶ Hear it', '▶ 들어 보기')}</button>
        {!fixed && <button className="ghost-btn" style={spBtn} onClick={ask}>{t('▶ Passing or cadential?', '▶ 경과? 종지?')}</button>}
        {quiz && !fixed && <button className="ghost-btn" style={spBtn} onClick={() => { setQuiz(false); setAns(null); }}>{t('Back', '돌아가기')}</button>}
      </div>
    </div>
  );
}
// ── step 3: decorations: a suspension, an accented passing note, the Picardy third ──
const H6_DEC = {
  sus: { en: 'A suspension', chip: 'Suspension', ko: '계류음', what: ['The top note is held over from the chord before, clashes on the beat, then falls a step to a note of the new chord: prepare, suspend, resolve.', '윗음이 앞 화음에서 이어져 박 위에서 부딪히고, 한 걸음 내려가 새 화음의 음으로: 준비, 계류, 해결.'],
    plain: [{ v: [-7, -3, 5, 12] }, { v: [-17, -5, 2, 11] }, { v: [-12, -5, 4, 12], len: 3 }], dec: [{ v: [-7, -3, 5, 12], hold: 1 }, { v: [-17, -5, 2, 11], split: [[null, 1], [11, 1]] }, { v: [-12, -5, 4, 12], len: 3 }], top: [12, [12, 11], 12] },
  apn: { en: 'An accented passing note', chip: 'Accented passing note', ko: '강박 경과음', what: ['A note between two notes a 3rd apart, ON the beat, not part of the chord; it moves on by step the same way.', '3도 떨어진 두 음 사이의 음이 박 위에 와요. 화음 음이 아니고, 같은 방향으로 한 걸음 더 가요.'],
    plain: [{ v: [-7, -3, 0, 5] }, { v: [-17, -5, -1, 2] }, { v: [-12, -8, -5, 0], len: 3 }], dec: [{ v: [-7, -3, 0, 5] }, { v: [-17, -5, -1, 2], split: [[4, 1], [2, 1]] }, { v: [-12, -8, -5, 0], len: 3 }], top: [5, [4, 2], 0] },
  pic: { en: 'The Picardy third', chip: 'Picardy third', ko: '피카르디 3도', what: ['A piece in a minor key ending on a MAJOR tonic chord: its 3rd raised a semitone (in A minor, C♯ for C).', '단조 곡이 장3화음 으뜸화음으로 끝나요: 3음을 반음 올려요(A단조에서 C 대신 C♯).'],
    plain: [{ v: [-10, -3, 2, 5] }, { v: [-8, -4, -1, 4] }, { v: [-15, -3, 0, 4], len: 3 }], dec: [{ v: [-10, -3, 2, 5] }, { v: [-8, -4, -1, 4] }, { v: [-15, -3, 1, 4], len: 3 }], top: [5, 4, 4] },
};
const H6_DECS = ['sus', 'apn', 'pic'];
function H6DecorPad({ onResult, fixed }) {
  const [id, setId] = useState(fixed ? fixed.id : 'sus'), [quiz, setQuiz] = useState(!!fixed), [ans, setAns] = useState(null);
  const x = H6_DEC[id], show = !quiz || ans;
  const ask = () => { let y, g = 0; do { y = pick(H6_DECS); } while (y === id && g++ < 10); setId(y); setQuiz(true); setAns(null); h6Play(H6_DEC[y].dec); };
  const say = (v) => { if (!quiz || ans) return; setAns(v); if (onResult) onResult({ ok: v === id }); };
  return (
    <div className="try-box" style={actBox} data-h6="dec">
      <div style={actTitle}>{t('Suspensions, passing notes and the Picardy third', '계류음, 경과음, 피카르디 3도')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>화음은 그대로, 장식이 하나. 먼저 <b>장식 없이</b>, 그다음 <b>장식과 함께</b> 들어요. 무엇이 달라졌나요?</> : <>The same chords, with one decoration. Hear them <b>plain</b>, then <b>decorated</b>. What changed?</>}</div>
      {!quiz && spChips(H6_DECS.map(y => [y, t(H6_DEC[y].chip, H6_DEC[y].ko)]), id, (y) => { setId(y); setAns(null); })}
      {show && <div style={{fontSize:14,color:BK.ink,lineHeight:1.45,margin:'4px 0 6px',textWrap:'pretty'}}><b>{t(x.en, x.ko)}</b>: {t(x.what[0], x.what[1])}</div>}
      {quiz && !ans && <div style={{display:'grid',gridTemplateColumns:'1fr',gap:6,marginTop:6}}>{H6_DECS.map(v => <button key={v} className="choice-btn" onClick={() => say(v)} style={{padding:'11px 4px',fontSize:14.5,fontWeight:900}}>{t(H6_DEC[v].en, H6_DEC[v].ko)}</button>)}</div>}
      {spMsg(ans ? (ans === id ? t('Yes: ' + x.en.toLowerCase() + '.', '맞아요: ' + x.ko + '.') : t('It was ' + x.en.toLowerCase() + '.', '정답은 ' + x.ko + '.')) : quiz ? t('Listen: which decoration?', '들어요: 어떤 장식?') : '', ans ? (ans === id ? BK.green : BK.coral) : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={spBtn} onClick={() => h6Play(x.plain)}>{t('▶ Plain', '▶ 장식 없이')}</button>
        <button className="ghost-btn" style={spBtn} onClick={() => h6Play(x.dec)}>{t('▶ Decorated', '▶ 장식과 함께')}</button>
        {!fixed && <button className="ghost-btn" style={spBtn} onClick={ask}>{t('▶ Which one?', '▶ 어느 것일까?')}</button>}
        {quiz && !fixed && <button className="ghost-btn" style={spBtn} onClick={() => { setQuiz(false); setAns(null); }}>{t('Back', '돌아가기')}</button>}
      </div>
    </div>
  );
}
// ── step 4: the six related keys: the home key, its dominant and subdominant, and the relatives of all three ──
const H6_MAJ = ['C', 'D♭', 'D', 'E♭', 'E', 'F', 'F♯', 'G', 'A♭', 'A', 'B♭', 'B'], H6_MIN = ['C', 'C♯', 'D', 'E♭', 'E', 'F', 'F♯', 'G', 'G♯', 'A', 'B♭', 'B'];
const h6KeyName = ([pc, m]) => (m === 'M' ? H6_MAJ[spPc(pc)] + t(' major', '장조') : H6_MIN[spPc(pc)] + t(' minor', '단조'));
const h6Family = ([h, m]) => (m === 'M' ? { top: [[h + 5, 'M'], [h, 'M'], [h + 7, 'M']], bot: [[h + 2, 'm'], [h + 9, 'm'], [h + 4, 'm']] } : { top: [[h + 8, 'M'], [h + 3, 'M'], [h + 10, 'M']], bot: [[h + 5, 'm'], [h, 'm'], [h + 7, 'm']] });
const h6Same = (a, b) => spPc(a[0]) === spPc(b[0]) && a[1] === b[1];
const H6_HOMES = [[0, 'M'], [7, 'M'], [5, 'M'], [2, 'M'], [10, 'M'], [3, 'M'], [9, 'm'], [4, 'm'], [2, 'm'], [7, 'm']];
const h6Decoys = (home) => { const F = h6Family(home), all = F.top.concat(F.bot), out = []; [[1, 'M'], [2, 'M'], [6, 'M'], [8, 'm'], [11, 'm'], [0, 'm'], [3, 'm'], [4, 'M'], [9, 'M'], [10, 'm']].forEach(([d, m]) => { const x = [home[0] + d, m]; if (!all.some(y => h6Same(y, x)) && !out.some(y => h6Same(y, x))) out.push(x); }); return shuffle(out).slice(0, 3); };
const h6Travel = (home, to) => { const tri = (pc, m) => [pc, pc + (m === 'M' ? 4 : 3), pc + 7].map(x => spPc(x) + (spPc(x) < 5 ? 0 : -12)), dom7 = (pc) => [pc + 7, pc + 11, pc + 14, pc + 17].map(x => spPc(x) - 12);
  return spPlay([{ at: 0, keys: tri(home[0], home[1]).concat([spPc(home[0]) - 24]), len: 1.8, vol: 0.11 }, { at: 2, keys: dom7(to[0]).concat([spPc(to[0] + 7) - 24]), len: 1.8, vol: 0.11 }, { at: 4, keys: tri(to[0], to[1]).concat([spPc(to[0]) - 24]), len: 2.5, vol: 0.11 }], 70); };
function H6KeysPad({ onResult, fixed }) {
  const [hi, setHi] = useState(fixed != null ? fixed : 0), own = fixed == null, [found, setFound] = useState([]), [bad, setBad] = useState(null), [miss, setMiss] = useState(0), [deck, setDeck] = useState(null);
  const home = H6_HOMES[hi], F = h6Family(home), rel = F.top.concat(F.bot).filter(x => !h6Same(x, home)), done = found.length >= 5;
  const cards = React.useMemo(() => shuffle(rel.concat(h6Decoys(home))), [hi]);
  const reset = (i) => { setHi(i); setFound([]); setBad(null); setMiss(0); };
  const tap = (x) => { if (done) return; if (rel.some(y => h6Same(y, x))) { if (found.some(y => h6Same(y, x))) return; const nf = found.concat([x]); setFound(nf); setBad(null); h6Travel(home, x); if (nf.length >= 5 && onResult) onResult({ ok: miss === 0 }); } else { setBad(x); setMiss(m => m + 1); } };
  const cell = (x) => { const isHome = h6Same(x, home), got = found.some(y => h6Same(y, x)); return <div key={x.join()} style={{padding:'8px 4px',borderRadius:8,textAlign:'center',fontSize:13.5,fontWeight:900,border:'1.5px solid ' + (isHome ? BK.coral : 'rgba(38,41,107,0.25)'),background:isHome ? '#fbe3da' : got || done ? '#fff' : 'transparent',color:isHome ? BK.ink : got || done ? BK.green : BK.muted}}>{isHome || got || done ? h6KeyName(x) : '?'}</div>; };
  return (
    <div className="try-box" style={actBox} data-h6="keys">
      <div style={actTitle}>{t('The six related keys', '여섯 근친조')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>집 조와 가장 가까운 조 다섯: <b>딸림조</b>(5도 위), <b>버금딸림조</b>(5도 아래), 그리고 <b>이 셋의 나란한조</b>. 위 줄은 버금딸림·집·딸림, 아래 줄은 그 나란한조. 조표가 같거나 하나만 달라요. 다섯 조를 찾아요: 찾을 때마다 그 조로 여행해요.</>
        : <>The five keys closest to home: <b>the dominant</b> (a 5th up), <b>the subdominant</b> (a 5th down), and <b>the relatives of all three</b>. The top row is subdominant, home, dominant; the bottom row their relatives. Their key signatures are the same or one sharp or flat apart. Find the five: each one you find, you travel there.</>}</div>
      <div style={{display:'grid',gridTemplateColumns:'repeat(3,minmax(0,1fr))',gap:6,margin:'6px 0'}}>{F.top.map(cell)}{F.bot.map(cell)}</div>
      <div style={{display:'grid',gridTemplateColumns:'repeat(4,minmax(0,1fr))',gap:6,marginTop:6}}>{cards.map(x => { const got = found.some(y => h6Same(y, x)); return <button key={x.join()} disabled={got || done} className={'choice-btn' + (got ? ' good' : bad && h6Same(bad, x) ? ' bad' : '')} onClick={() => tap(x)} style={{padding:'9px 2px',fontSize:12.5,fontWeight:900,lineHeight:1.2}}>{h6KeyName(x)}</button>; })}</div>
      {own && <div style={{display:'flex',justifyContent:'center',marginTop:8}}><button className="ghost-btn" style={spBtn} onClick={() => { let i, g = 0; do { i = Math.floor(Math.random() * H6_HOMES.length); } while (i === hi && g++ < 10); reset(i); }}>{t('Another home key', '다른 집 조')}</button></div>}
      {spMsg(done ? t('All five: the family of ' + h6KeyName(home) + '.', '다섯 모두: ' + h6KeyName(home) + '의 가족.') : bad ? t('Not that one: count the sharps or flats. A related key has the same, or one more or one fewer.', '그 조가 아니에요: 샵이나 플랫을 세어 봐요. 근친조는 같거나 하나 많거나 하나 적어요.') : t('Find the related keys: ' + found.length + ' of 5', '근친조를 찾아요: 5개 중 ' + found.length), done ? BK.green : bad ? BK.coral : undefined)}
    </div>
  );
}
// ── step 5 (and the thing to make): a tune above a bass, checked as it is written ──
const H6_BASS = [
  { en: 'C major, walking up', ko: 'C장조, 걸어 올라가요', b: [-12, -10, -8, -7, -5, -12] },
  { en: 'C major, up and back', ko: 'C장조, 올라갔다 내려와요', b: [-12, -8, -7, -5, -7, -8, -10, -12] },
  { en: 'G major', ko: 'G장조', b: [-5, -1, -3, -5, -8, -12, -10, -17] },
  { en: 'F major', ko: 'F장조', b: [-7, -10, -12, -14, -15, -17, -12, -19] },
];
const h6Iv = (lo, hi) => { const d = hi - lo, m = spPc(d); return { d, m, cons: d > 0 && [0, 3, 4, 7, 8, 9].includes(m), perf: m === 0 || m === 7 }; };
const H6_IVN = [['an octave', '8도'], ['a 2nd', '2도'], ['a 2nd', '2도'], ['a 3rd', '3도'], ['a 3rd', '3도'], ['a 4th', '4도'], ['a tritone', '증4도'], ['a 5th', '5도'], ['a 6th', '6도'], ['a 6th', '6도'], ['a 7th', '7도'], ['a 7th', '7도']];
const h6IvName = (lo, hi) => { const n = H6_IVN[spPc(hi - lo)], far = hi - lo > 12 && spPc(hi - lo) !== 0; return t(n[0] + (far ? ' (plus an octave)' : ''), (far ? '한 옥타브 넘은 ' : '') + n[1]); };
const h6IvNum = (lo, hi) => { const d = hi - lo, m = spPc(d); return m === 0 ? (d === 0 ? '1' : '8') : String([1, 2, 2, 3, 3, 4, 4, 5, 6, 6, 7, 7][m]); };
const h6Check = (B, S) => S.map((x, j) => { const v = h6Iv(B[j], x), out = { cons: v.cons, par: false, perf: v.perf };
  if (j > 0 && v.perf) { const p = h6Iv(B[j - 1], S[j - 1]); if (p.perf && p.m === v.m && (B[j] - B[j - 1]) * (x - S[j - 1]) > 0) out.par = true; } return out; });
// the two parts drawn as two lines of dots: the bass in navy, the tune in coral, a dashed ring where the next note goes
function H6Lines({ B, S, at = -1, w = 420 }) {
  const n = B.length, ks = B.concat(S, [0, 12]), lo = Math.min(...ks), hi = Math.max(...ks), X = (j) => 24 + j * (352 / Math.max(1, n - 1)), Y = (k) => 100 - (k - lo) / Math.max(1, hi - lo) * 86;
  const path = (P, c) => P.length > 1 ? '<path d="' + P.map((k, j) => (j ? 'L' : 'M') + X(j).toFixed(1) + ' ' + Y(k).toFixed(1)).join(' ') + '" fill="none" stroke="' + c + '" stroke-width="2.2"/>' : '';
  const dots = (P, c) => P.map((k, j) => '<ellipse cx="' + X(j).toFixed(1) + '" cy="' + Y(k).toFixed(1) + '" rx="' + (j === at ? 7.5 : 6) + '" ry="' + (j === at ? 5.6 : 4.5) + '" transform="rotate(-20 ' + X(j).toFixed(1) + ' ' + Y(k).toFixed(1) + ')" fill="' + c + '"/>').join('');
  const next = S.length < n ? '<circle cx="' + X(S.length).toFixed(1) + '" cy="' + Y(Math.max(...S.concat([B[S.length] + 9]))).toFixed(1) + '" r="8" fill="none" stroke="#e4572e" stroke-width="1.6" stroke-dasharray="3 3"/>' : '';
  return <svg viewBox="0 0 400 112" style={{width:'100%',maxWidth:w,display:'block',margin:'0 auto'}} role="img" aria-label={t('Two parts', '두 성부')} dangerouslySetInnerHTML={{ __html: path(B, '#26296b') + path(S, '#e4572e') + dots(B, '#26296b') + dots(S, '#e4572e') + next }}/>;
}
function TwoPartPad({ onResult, toy = false }) {
  const [bi, setBi] = useState(0), [S, setS] = useState([]), [at, setAt] = useState(-1);
  const T = useSpTimers(), B = H6_BASS[bi].b, n = B.length, chk = h6Check(B, S), done = S.length >= n;
  const lastOk = done && chk.every(c => c.cons && !c.par) && ['1', '8', '3'].includes(h6IvNum(B[n - 1], S[n - 1]));
  const reset = (i) => { T.clear(); setBi(i); setS([]); setAt(-1); };
  const tap = (k) => { playKey(k, 0.4); if (done) return; const ns = S.concat([k]); setS(ns); spPlay([{ at: 0, keys: [B[ns.length - 1], k], len: 1.2, vol: 0.13 }], 72);
    if (ns.length >= n && onResult && !toy) { const c = h6Check(B, ns), ok = c.every(x => x.cons && !x.par) && ['1', '8', '3'].includes(h6IvNum(B[n - 1], ns[n - 1])); onResult({ ok }); } };
  const play = () => { T.clear(); const r = spPlay(B.map((b, j) => ({ at: j, keys: j < S.length ? [b, S[j]] : [b], len: 0.95, vol: 0.13 })), 72); if (!r) return; B.forEach((_, j) => T.at(r.ms(j), () => setAt(j))); T.at(r.ms(n + 0.5), () => setAt(-1)); };
  const lit = {}; if (S.length) lit[S[S.length - 1]] = chk[S.length - 1].cons && !chk[S.length - 1].par ? 'good' : 'bad';
  return (
    <div className="try-box" style={actBox} data-h6="two">
      <div style={actTitle}>{toy ? t('My tune above a bass', '베이스 위의 내 선율') : t('Two parts: a tune above a bass', '두 성부: 베이스 위의 선율')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>베이스가 주어져요. 베이스 음마다 위에 한 음씩, 건반을 눌러 써요. 규칙 셋: 두 음 사이가 <b>3도, 5도, 6도, 8도</b>(잘 어울리는 음정); <b>5도나 8도가 연달아</b> 같은 쪽으로 가지 않기; 마지막은 <b>8도나 3도</b>. 베이스와 <b>반대로</b> 움직이면 더 좋아요. 목록에 없는 음정(2도, 4도, 7도)은 빨갛게 보여요.</>
        : <>The bass is given. Above each bass note write one note, by tapping a key. Three rules: between the parts, <b>a 3rd, 5th, 6th or octave</b> (the intervals that blend); no <b>two 5ths or two octaves in a row</b> moving the same way; end on <b>an octave or a 3rd</b>. Moving <b>against</b> the bass sounds best. An interval not on the list (a 2nd, 4th or 7th) turns coral.</>}</div>
      {spChips(H6_BASS.map((x, i) => [i, t(x.en, x.ko)]), bi, reset)}
      <H6Lines B={B} S={S} at={at}/>
      <div style={{display:'flex',justifyContent:'center',gap:4,flexWrap:'wrap',margin:'2px 0 6px'}}>{B.map((b, j) => { const c = chk[j]; return <span key={j} style={{minWidth:30,padding:'3px 4px',borderRadius:6,textAlign:'center',fontSize:13,fontWeight:900,border:'1.5px solid ' + (at === j ? BK.coral : 'rgba(38,41,107,0.2)'),color:!c ? BK.muted : c.cons && !c.par ? BK.green : BK.coral,background:'#fff'}}>{c ? h6IvNum(b, S[j]) + (c.par ? '!' : '') : j === S.length ? '?' : '·'}</span>; })}</div>
      <SpKb lo={0} hi={19} W={20} H={70} lit={lit} names={{ 0: 'C', 12: 'C' }} onTap={tap} label={t('Write the tune', '선율 쓰기')}/>
      <div style={{textAlign:'center',fontSize:12,fontWeight:800,color:BK.muted,marginTop:2}}>{t('the tune, from middle C up (the bass is below)', '선율: 가운데 도부터 위(베이스는 아래)')}</div>
      {spMsg(done ? (lastOk ? t('Every interval blends, no parallel 5ths or octaves, and it ends well ✓', '모든 음정이 어울리고, 5도·8도 나란히 없이, 끝도 좋아요 ✓') : t(chk.some(c => c.par) ? 'A ! marks two 5ths or two octaves in a row: change one note.' : chk.some(c => !c.cons) ? 'A coral number clashes: try a 3rd or a 6th there.' : 'End on an octave or a 3rd above the last bass note.', chk.some(c => c.par) ? '!는 5도나 8도가 연달아: 한 음을 바꿔요.' : chk.some(c => !c.cons) ? '빨간 숫자는 부딪혀요: 거기에 3도나 6도를.' : '마지막 베이스 음 위 8도나 3도로 끝나요.'))
        : chk.length && (!chk[chk.length - 1].cons || chk[chk.length - 1].par) ? t('That one clashes: undo and try a 3rd or a 6th.', '그 음은 부딪혀요: 되돌리고 3도나 6도를.') : t('Note ' + (S.length + 1) + ' of ' + n + ': where the dashed ring is.', n + '개 중 ' + (S.length + 1) + '번째: 점선 동그라미 자리에.'), done ? (lastOk ? BK.green : BK.coral) : chk.length && (!chk[chk.length - 1].cons || chk[chk.length - 1].par) ? BK.coral : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={spBtn} onClick={play}>{t('▶ Play both parts', '▶ 두 성부 듣기')}</button>
        <button className="ghost-btn" style={spBtn} disabled={!S.length} onClick={() => setS(S.slice(0, -1))}>{t('Undo', '되돌리기')}</button>
        <button className="ghost-btn" style={spBtn} disabled={!S.length} onClick={() => setS([])}>{t('Clear', '지우기')}</button>
      </div>
    </div>
  );
}

// ── the pictures on paper ──
const h6PicV7 = () => lsRawPic([0, 1, 2, 3].map(i => '<ellipse cx="22" cy="' + (38 - i * 8) + '" rx="6" ry="4.4" transform="rotate(-20 22 ' + (38 - i * 8) + ')" fill="' + (i === 0 ? '#e4572e' : '#26296b') + '"/>').join('') + '<text x="40" y="20" font-family="Inter, sans-serif" font-size="11" font-weight="900" fill="#26296b">6</text><text x="40" y="33" font-family="Inter, sans-serif" font-size="11" font-weight="900" fill="#26296b">5</text>', [0, 0, 60, 44]);
const h6Pic64 = () => lsRawPic('<path d="M6 38 H20 V28 H34 V18 H48" fill="none" stroke="#26296b" stroke-width="2.6"/><circle cx="27" cy="28" r="5" fill="#e4572e"/>', [0, 0, 56, 44]);
const h6PicDec = () => lsRawPic('<path d="M8 12 Q20 4 32 12" fill="none" stroke="#e4572e" stroke-width="2"/><ellipse cx="8" cy="16" rx="5.5" ry="4" fill="#26296b"/><ellipse cx="32" cy="16" rx="5.5" ry="4" fill="#e4572e"/><ellipse cx="48" cy="24" rx="5.5" ry="4" fill="#26296b"/>', [0, 0, 60, 44]);
const h6PicKeys = () => lsRawPic([0, 1, 2].map(i => '<rect x="' + (4 + i * 20) + '" y="6" width="17" height="14" rx="3" fill="' + (i === 1 ? '#e4572e' : '#26296b') + '"/><rect x="' + (4 + i * 20) + '" y="24" width="17" height="14" rx="3" fill="none" stroke="#26296b" stroke-width="2"/>').join(''), [0, 0, 66, 44]);
const h6PicTwo = () => l6PicTwo();

function h6LbPages(scr = false) {
  const ch = 'harmony-6', h5n = bkChapterNo('harmony-5');
  const pen = (x) => <PenArt shapes={x.shapes} vb={x.vb} style={{width:90}}/>;
  const checks = [[h6PicV7(), t('I name V7, V7b, V7c and V7d from the bass, and resolve them', '베이스로 V7, V7b, V7c, V7d를 알고 풀어요')], [h6Pic64(), t('I tell a passing six-four from a cadential one', '경과 6-4와 종지 6-4를 구별해요')],
    [h6PicDec(), t('I hear a suspension, an accented passing note and a Picardy third', '계류음, 강박 경과음, 피카르디 3도를 들어요')], [h6PicKeys(), t('I name the five keys related to any key', '어느 조든 근친조 다섯을 말해요')], [h6PicTwo(), t('I write a tune above a bass with 3rds, 5ths, 6ths and octaves', '3도, 5도, 6도, 8도로 베이스 위에 선율을 써요')]];
  const toc = [[t('V7 and its inversions', 'V7과 그 자리바꿈'), 2], [t('Passing six-fours', '경과 6-4화음'), 3], [t('Suspensions, passing notes and the Picardy third', '계류음, 경과음, 피카르디 3도'), 4], [t('The six related keys', '여섯 근친조'), 5], [t('Two parts: a tune above a bass', '두 성부: 베이스 위의 선율'), 6], [t('My five checks', '나의 다섯 가지 확인'), 7]];
  const v7Still = <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:scr ? 10 : '18px 28px',width:'100%',maxWidth:scr ? 720 : 640,margin:'0 auto'}}>{H6_INV.map(x => { const V = H6_V7[x].v; return <div key={x}><div style={{textAlign:'center',fontSize:scr ? 13.5 : 18,fontWeight:900,color:BK.ink,marginBottom:4}}>{H6_V7[x].nm}{h6Fig(H6_V7[x].fig)}</div><SpKb lo={-19} hi={16} W={scr ? 7 : 13} H={scr ? 44 : 70} lit={Object.fromEntries(V.map((y, j) => [y, j === 0 ? 'cor' : 'pale']))} names={{ [V[0]]: h6Let('C', V[0]) }} k={1}/></div>; })}</div>;
  const famStill = (home) => { const F = h6Family(home); return <div style={{display:'grid',gridTemplateColumns:'repeat(3,1fr)',gap:scr ? 6 : 12,width:'100%',maxWidth:scr ? 420 : 600,margin:'0 auto'}}>{F.top.concat(F.bot).map(x => <div key={x.join()} style={{padding:scr ? '8px 4px' : '16px 6px',borderRadius:8,textAlign:'center',fontSize:scr ? 14 : 20,fontWeight:900,border:'1.5px solid ' + (h6Same(x, home) ? BK.coral : 'rgba(38,41,107,0.3)'),background:h6Same(x, home) ? '#fbe3da' : '#fff',color:BK.ink}}>{h6KeyName(x)}</div>)}</div>; };
  return [
    <LbPage key="1" no={1} chId={ch} teacher={<>{t('Theory of Music Grade 6, the last graded theory exam (chapter ' + h5n + ' has Grade 5). Its harmony vocabulary, major and minor keys: I II III IV V VI and their first inversions; cadential Ic; passing Ic, IVc and Vc; V7 V7b V7c V7d; accented and unaccented passing notes and auxiliary notes; single suspensions; the tierce de Picardie (minor keys only); modulation within the six related keys. Tasks: harmonise a melody or an unfigured bass in four vocal parts; write a part above or below a given part in two-part keyboard style. This chapter takes the new items one step each and ends with a two-part tune to write. The figures, the passing six-four examples and the definitions of the decorations are textbook harmony (please check: the board lists them).', '이론 6급, 마지막 급 이론 시험(' + h5n + '장은 5급). 화성 어휘, 장조와 단조: I II III IV V VI과 첫째 자리바꿈; 종지 Ic; 경과 Ic, IVc, Vc; V7 V7b V7c V7d; 강박·약박 경과음과 보조음; 단일 계류음; 피카르디 3도(단조만); 여섯 근친조 안의 전조. 과제: 선율이나 숫자 없는 베이스에 네 성부로 화음 붙이기; 주어진 성부 위나 아래에 두 성부 건반 양식으로 쓰기. 이 챕터는 새 항목을 한 단계씩, 마지막에 두 성부 선율 쓰기. 숫자, 경과 6-4 예, 장식의 정의는 교과서 화성이에요(확인 부탁드려요: 보드에 목록이 있어요).')}</>}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:46,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{bkChapterName(ch)}</div>
      </div></LbOnly>
      <LbPic h={130}>{v7Still}</LbPic>
      <LbSay size={18}>{t('Theory Grade 6, the last theory grade: the dominant 7th in all four positions, passing six-fours, decorations, the six related keys, and two parts of your own.', '이론 6급, 마지막 이론 급수: 네 자리의 딸림7화음, 경과 6-4, 장식, 여섯 근친조, 그리고 나만의 두 성부.')}</LbSay>
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
    <LbPage key="2" no={2} chId={ch} kicker={t('Step 1', '1단계')} title={t('V7 and its inversions', 'V7과 그 자리바꿈')}
      teacher={<>{t('V7 (bass the root, figured 7), V7b (the 3rd, 6 5), V7c (the 5th, 4 3), V7d (the 7th, 4 2). Resolutions: the 7th falls a step, the leading note rises; V7, V7b and V7c usually go to I, V7d to Ib (its bass, the 7th, falls). The app\'s chords are in four parts in C, G, F, D and B♭ major.', 'V7(베이스가 근음, 숫자 7), V7b(3음, 6 5), V7c(5음, 4 3), V7d(7음, 4 2). 해결: 7음은 한 걸음 내려가고 이끔음은 올라가요; V7, V7b, V7c는 대개 I로, V7d는 Ib로(베이스인 7음이 내려가요). 앱의 화음은 C, G, F, D, B♭장조의 네 성부.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=1')}>
      <LbLive still={<LbPic h={140}>{v7Still}</LbPic>} live={<H6V7Pad/>}/>
      <LbSay>{LANG === 'ko' ? <>네 음 화음, 네 자리. <b>베이스를 보면</b> 이름이 나와요: 근음 V7, 3음 V7b, 5음 V7c, 7음 V7d. 풀릴 때 7음은 내려가고 이끔음은 올라가요.</> : <>A four-note chord, four positions. <b>Look at the bass</b> and you have its name: root V7, 3rd V7b, 5th V7c, 7th V7d. As it resolves, the 7th falls and the leading note rises.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>C장조 G7: G B D F. 그다음 C로.</>, <>B를 베이스에(V7b), D를 베이스에(V7c), F를 베이스에(V7d). 매번 풀어 봐요.</>, <>V7d는 Ib로: 베이스 F가 E로 내려가요.</>]
        : [<>In C major, G7: G B D F. Then to C.</>, <>B in the bass (V7b), D in the bass (V7c), F in the bass (V7d). Resolve each one.</>, <>V7d goes to Ib: the bass F falls to E.</>]}/>
      <LbRemember>{t('The bass names it; the 7th falls, the leading note rises.', '베이스가 이름을; 7음은 내려가고 이끔음은 올라가요.')}</LbRemember>
    </LbPage>,
    <LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={t('Passing six-fours', '경과 6-4화음')}
      teacher={<>{t('Passing six-fours: the bass moves by step through the six-four, between two positions of one chord, on a weak beat: I – Vc – Ib (bass ^1 ^2 ^3), IV – Ic – IVb (bass ^4 ^5 ^6). The syllabus also lists a passing IVc. Compare the cadential six-four (Grade 5): Ic on a strong beat, the bass staying for V.', '경과 6-4: 베이스가 6-4를 지나 한 걸음씩, 한 화음의 두 자리 사이, 약박에서: I – Vc – Ib(베이스 1 2 3), IV – Ic – IVb(베이스 4 5 6). 실라버스에는 경과 IVc도 있어요. 종지 6-4(5급)와 견줘 보세요: 강박의 Ic, 베이스는 V를 위해 머물러요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=2')}>
      <LbLive still={<LbPic h={120}><div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:16,width:'100%',maxWidth:560,margin:'0 auto',fontWeight:900,color:BK.ink,textAlign:'center'}}>{['passV', 'cad'].map(y => <div key={y}><div style={{fontFamily:LB_SERIF,fontSize:scr ? 20 : 30}}>{H6_64[y].en}</div><div style={{fontSize:scr ? 14 : 18,color:BK.muted,marginTop:6}}>{t('bass ', '베이스 ') + H6_64[y].bass.join(' ')}</div><div style={{fontSize:scr ? 13 : 17,color:H6_64[y].kind === 'pass' ? BK.coral : BK.ink,marginTop:6}}>{H6_64[y].kind === 'pass' ? t('passing: the bass walks', '경과: 베이스가 걸어요') : t('cadential: the bass stays', '종지: 베이스가 머물러요')}</div></div>)}</div></LbPic>} live={<H6SixFourPad/>}/>
      <LbSay>{LANG === 'ko' ? <>베이스가 <b>걸어가는</b> 가운데의 6-4는 <b>경과</b>, 베이스가 <b>머물러</b> V로 가는 강박의 Ic는 <b>종지</b>.</> : <>A six-four in the middle of a <b>walking</b> bass is <b>passing</b>; Ic on a strong beat with the bass <b>staying</b> for V is <b>cadential</b>.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>C장조: I – Vc – Ib, 베이스 C D E.</>, <>IV – Ic – IVb, 베이스 F G A.</>, <>Ic – V – I과 견줘요: 베이스 G G C.</>]
        : [<>C major: I – Vc – Ib, the bass C D E.</>, <>IV – Ic – IVb, the bass F G A.</>, <>Compare Ic – V – I: the bass G G C.</>]}/>
      <LbRemember>{t('Walking bass: passing. Staying bass: cadential.', '걷는 베이스: 경과. 머무는 베이스: 종지.')}</LbRemember>
    </LbPage>,
    <LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title={t('Suspensions, passing notes and the Picardy third', '계류음, 경과음, 피카르디 3도')}
      teacher={<>{t('Single suspensions (prepared in the chord before, held over onto the strong beat as a discord, resolved down a step; here a 4–3 over V), accented passing notes (a passing note on the beat, here E between F and D over V; Grade 5 had the unaccented ones), and the tierce de Picardie (a minor-key piece ending on a major tonic chord: in A minor, A C♯ E). The app plays each plain, then decorated.', '단일 계류음(앞 화음에서 준비, 강박 위로 이어져 불협화, 한 걸음 내려가 해결; 여기서는 V 위의 4–3), 강박 경과음(박 위의 경과음, 여기서는 V 위에서 F와 D 사이의 E; 5급은 약박 경과음), 피카르디 3도(단조 곡이 장3화음 으뜸화음으로 끝나요: A단조에서 A C♯ E). 앱은 먼저 장식 없이, 그다음 장식과 함께 들려줘요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=3')}>
      <LbLive still={<LbPic h={140}><div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr 1fr',gap:12,width:'100%',maxWidth:720,margin:'0 auto'}}>{H6_DECS.map(y => <div key={y} style={{fontSize:scr ? 13 : 16,color:BK.ink,lineHeight:1.45}}><div style={{fontWeight:900,fontSize:scr ? 14 : 18,marginBottom:4}}>{t(H6_DEC[y].en, H6_DEC[y].ko)}</div>{t(H6_DEC[y].what[0], H6_DEC[y].what[1])}</div>)}</div></LbPic>} live={<H6DecorPad/>}/>
      <LbSay>{LANG === 'ko' ? <>화음은 그대로, 윗성부에 장식 하나. <b>계류음</b>은 붙잡았다 내려가고, <b>강박 경과음</b>은 박 위에서 지나가고, <b>피카르디 3도</b>는 단조 곡을 장조로 끝내요.</> : <>The chords stay; the top part has one decoration. <b>A suspension</b> holds on, then falls; <b>an accented passing note</b> passes on the beat; <b>the Picardy third</b> ends a minor piece in major.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>C장조 IV–V–I, 윗음 C를 V로 이어 붙잡았다 B로.</>, <>F–E–D를 V 위에, E가 박 위에.</>, <>A단조 iv–V–I, 마지막 화음에 C♯.</>]
        : [<>C major IV–V–I: hold the top C over into V, then fall to B.</>, <>F–E–D over V, the E on the beat.</>, <>A minor iv–V–I, with C♯ in the last chord.</>]}/>
      <LbRemember>{t('Hold and fall; pass on the beat; end in major.', '붙잡고 내려가기; 박 위에서 지나가기; 장조로 끝내기.')}</LbRemember>
    </LbPage>,
    <LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title={t('The six related keys', '여섯 근친조')}
      teacher={<>{t('Modulation within the six related keys: the tonic, the dominant and the subdominant, and the relative major or minor of each. From C major: G, F, A minor, E minor (relative of G), D minor (relative of F). From A minor: E minor, D minor, C major, G major, F major. Their key signatures are the same or one sharp or flat apart.', '여섯 근친조 안의 전조: 으뜸조, 딸림조, 버금딸림조, 그리고 각각의 나란한 장조나 단조. C장조에서: G, F, A단조, E단조(G의 나란한조), D단조(F의 나란한조). A단조에서: E단조, D단조, C장조, G장조, F장조. 조표가 같거나 샵·플랫 하나 차이.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=4')}>
      <LbLive still={<LbPic h={130}>{famStill([0, 'M'])}</LbPic>} live={<H6KeysPad/>}/>
      <LbSay>{LANG === 'ko' ? <>집 조의 가족: <b>위 줄</b>은 버금딸림·집·딸림, <b>아래 줄</b>은 그 나란한조. 조표가 같거나 하나만 달라서, 이 조들로 쉽게 여행해요.</> : <>Home's family: <b>the top row</b> is subdominant, home, dominant; <b>the bottom row</b> their relatives. Their key signatures differ by one sharp or flat at most, so it is easy to travel between them.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>C장조의 가족: F, C, G, 그리고 D단조, A단조, E단조.</>, <>A단조의 가족: D단조, A단조, E단조, 그리고 F, C, G.</>, <>G장조와 D단조의 가족도 말해 봐요.</>]
        : [<>C major's family: F, C, G, and D minor, A minor, E minor.</>, <>A minor's family: D minor, A minor, E minor, and F, C, G.</>, <>Say the families of G major and D minor too.</>]}/>
      <LbRemember>{t('Dominant, subdominant, and their relatives.', '딸림조, 버금딸림조, 그리고 그 나란한조.')}</LbRemember>
    </LbPage>,
    <LbPage key="6" no={6} chId={ch} kicker={t('Step 5', '5단계')} title={t('Two parts: a tune above a bass', '두 성부: 베이스 위의 선율')}
      teacher={<>{t('Writing a part above a given part in two-part keyboard style, the simplest way in: note against note, every interval consonant (3rds, 6ths, perfect 5ths and octaves), no consecutive 5ths or octaves, contrary motion preferred, an octave or a 3rd at the end. The syllabus asks for more (rhythm, passing notes); this is the first rung. The app checks each note as it is written; it is also the thing to make in this room.', '주어진 성부 위에 두 성부 건반 양식으로 쓰기, 가장 쉬운 시작: 음 대 음, 모든 음정이 협화(3도, 6도, 완전5도, 8도), 5도·8도 연속 없이, 반진행을 더 좋게, 끝은 8도나 3도. 실라버스는 더 많이(리듬, 경과음) 요구해요; 이것은 첫 걸음. 앱은 쓰는 대로 음마다 확인해요; 이 방의 만들어 보기이기도 해요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=5')}>
      <LbLive still={<LbPic h={140}><div style={{width:'100%',maxWidth:scr ? 440 : 620,margin:'0 auto'}}><H6Lines B={H6_BASS[0].b} S={[4, 2, 0, 2, 4, 12]} w={scr ? 420 : 620}/><div style={{textAlign:'center',fontSize:scr ? 13 : 17,fontWeight:900,color:BK.green}}>{t('3 8 6 6 6 8: it blends, moves against the bass and ends on the octave', '3 8 6 6 6 8: 어울리고, 베이스와 반대로 가고, 8도로 끝나요')}</div></div></LbPic>} live={<TwoPartPad/>}/>
      <LbSay>{LANG === 'ko' ? <>베이스 음마다 위에 한 음: <b>3도, 5도, 6도, 8도</b>. 5도와 8도는 연달아 같은 쪽으로 가지 않기. 끝은 8도나 3도.</> : <>One note above each bass note: <b>a 3rd, 5th, 6th or octave</b>. Never two 5ths or two octaves in a row moving the same way. End on an octave or a 3rd.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>왼손으로 베이스 C D E F G C. 오른손으로 3도 위를 나란히.</>, <>이번엔 6도로. 그다음 섞어서.</>, <>반대로 움직여 봐요: 베이스가 올라가면 선율은 내려가게.</>]
        : [<>The left hand plays the bass C D E F G C. The right hand a 3rd above, in parallel.</>, <>Now in 6ths. Then mix them.</>, <>Try contrary motion: as the bass climbs, let the tune come down.</>]}/>
      <LbRemember>{t('3rds and 6ths blend; no two 5ths or octaves in a row.', '3도와 6도는 어울려요; 5도·8도 연달아는 안 돼요.')}</LbRemember>
    </LbPage>,
    <LbPage key="7" no={7} chId={ch} kicker={t('Check-up', '점검')} title={t('My five checks', '나의 다섯 가지 확인')}
      teacher={<>{t('On paper and at the piano: V7 in each position named and resolved; a passing and a cadential six-four told apart by ear; the three decorations heard; the related keys of any key up to four sharps or flats; a tune above a given bass. The Workbook\'s last page is the paper check.', '종이와 피아노로: 네 자리의 V7 이름과 해결; 경과 6-4와 종지 6-4를 귀로 구별; 장식 셋 듣기; 샵·플랫 넷까지 어느 조든 근친조; 주어진 베이스 위에 선율. 워크북의 마지막 쪽이 종이 점검.')}</>}>
      <LbSay>{t('Tick each one: not yet, nearly, or got it!', '하나씩 표시해요: 아직, 거의, 됐어요!')}</LbSay>
      <LbLive still={<LbStageRows big rows={checks.map(([a, txt]) => [pen(a), txt])}/>} live={<FiveChecks376 rows={checks} storeKey="pb_h6_five"/>}/>
    </LbPage>,
  ];
}
function Harmony6LessonBook() { return <>{h6LbPages(false)}</>; }
function H6Learn({ onStart }) {
  const pages = h6LbPages(true), opener = pages[0];
  return (
    <Lesson id="harmony-6" title={bkChapterName('harmony-6')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="harmony-6"><div className="lb-screen lb-open" style={{display:'flex',flexDirection:'column',gap:12,margin:'0 0 8px'}}>{lbWordsFirst(opener.props.children)}</div></BkChapterCtx.Provider></LbScreenCtx.Provider>}>
      {pages.slice(1).map((pg, i) => <Step key={i} title={pg.props.title}><LbScreenPage page={pg}/></Step>)}
    </Lesson>
  );
}
// ── the drill ──
const H6_LEVELS = [
  { n: 1, label: 'V7, V7b, V7c or V7d?', kind: 'v7', time: 15 },
  { n: 2, label: 'Passing or cadential six-four?', kind: '64', time: 20 },
  { n: 3, label: 'Which decoration?', kind: 'dec', time: 25 },
  { n: 4, label: 'Is it a related key?', kind: 'key', time: 15 },
  { n: 5, label: 'Do the two parts blend?', kind: 'iv', time: 12 },
];
Object.assign(LEVEL_KO, { 'V7, V7b, V7c or V7d?': 'V7, V7b, V7c, V7d?', 'Passing or cadential six-four?': '경과 6-4? 종지 6-4?', 'Which decoration?': '어떤 장식?', 'Is it a related key?': '근친조일까?', 'Do the two parts blend?': '두 성부가 어울릴까?' });
function genH6Question(lv, prev) {
  const uid = Math.random(), kind = lv.kind;
  if (kind === 'v7') { let k, inv, g = 0; do { k = pick(Object.keys(H6_KEYS)); inv = pick(H6_INV); } while (prev && prev.key === k + inv && g++ < 10); return { kind, k, inv, answer: inv, choices: H6_INV.slice(), key: k + inv, uid }; }
  if (kind === '64') { let id, g = 0; do { id = pick(Object.keys(H6_64)); } while (prev && prev.key === id && g++ < 10); return { kind, id, answer: H6_64[id].kind, choices: ['pass', 'cad'], key: id + uid, uid }; }
  if (kind === 'dec') { let id, g = 0; do { id = pick(H6_DECS); } while (prev && prev.key === id && g++ < 10); return { kind, id, answer: id, choices: H6_DECS.slice(), key: id, uid }; }
  if (kind === 'key') { let h, x, g = 0; do { h = pick(H6_HOMES); const F = h6Family(h), rel = F.top.concat(F.bot).filter(y => !h6Same(y, h)); x = Math.random() < 0.5 ? pick(rel) : pick(h6Decoys(h)); } while (prev && prev.key === h.join() + x.join() && g++ < 10);
    const F = h6Family(h), yes = F.top.concat(F.bot).some(y => h6Same(y, x)); return { kind, h, x, answer: yes ? 'yes' : 'no', choices: ['yes', 'no'], key: h.join() + x.join(), uid }; }
  let b, d, g = 0; do { b = pick([-12, -10, -8, -7, -5]); d = pick([3, 4, 7, 8, 9, 12, 15, 16, 2, 10, 11, 13, 14]); } while (prev && prev.key === b + '-' + d && g++ < 10); const c = h6Iv(b, b + d).cons;
  return { kind: 'iv', b, s: b + d, answer: c ? 'yes' : 'no', choices: ['yes', 'no'], key: b + '-' + d, uid };
}
function H6Question({ q, given, locked, onAnswer, pixel }) {
  const done = !!given;
  const btnCls = pixel ? 'pixel-choice' : 'choice-btn', cls = (c) => btnCls + (!done ? '' : c === q.answer ? ' good' : given.ans === c ? ' bad' : '');
  const pickIt = (c) => { if (locked || done) return; stopClicks(); onAnswer(c); };
  const play = () => { stopClicks(); if (q.kind === '64') h6Play(H6_64[q.id].seq); else if (q.kind === 'dec') h6Play(H6_DEC[q.id].dec); else if (q.kind === 'iv') spPlay([{ at: 0, keys: [q.b, q.s], len: 1.6, vol: 0.14 }], 72); };
  useEffect(() => { if (!['64', 'dec', 'iv'].includes(q.kind)) return; const id = setTimeout(play, 350); return () => { clearTimeout(id); stopClicks(); }; }, [q.uid]);
  const grid = (cols, items) => <div style={{display:'grid',gridTemplateColumns:'repeat(' + cols + ',minmax(0,1fr))',gap:8,marginTop:10}}>{items.map(([c, lab]) => <button key={String(c)} disabled={locked} className={cls(c)} style={{padding:'12px 4px',fontSize:14.5,fontWeight:900}} onClick={() => pickIt(c)}>{lab}</button>)}</div>;
  const again = ['64', 'dec', 'iv'].includes(q.kind) ? <div style={{textAlign:'center'}}><button className={pixel ? 'pixel-btn' : 'ghost-btn'} style={{minHeight:44}} onClick={play}>{t('▶ Play it again', '▶ 다시 듣기')}</button></div> : null;
  let title, body;
  if (q.kind === 'v7') { const V = h6T(H6_V7[q.inv].v, H6_KEYS[q.k][0]); title = t(H6_KEYS[q.k][1] + ' major: which dominant 7th is this? Look at the bass.', H6_KEYS[q.k][1] + '장조: 어떤 딸림7화음일까요? 베이스를 봐요.');
    body = <><SpKb lo={-24} hi={20} W={11} H={60} lit={Object.fromEntries(V.map((x, j) => [x, j === 0 ? 'cor' : 'pale']))} names={Object.fromEntries(V.map(x => [x, h6Let(q.k, x)]))}/>{grid(4, H6_INV.map(x => [x, H6_V7[x].nm]))}</>; }
  else if (q.kind === '64') { title = t('Listen to the bass: a passing or a cadential six-four?', '베이스를 들어요: 경과 6-4? 종지 6-4?'); body = grid(2, [['pass', t('Passing', '경과')], ['cad', t('Cadential', '종지')]]); }
  else if (q.kind === 'dec') { title = t('Which decoration did you hear?', '어떤 장식을 들었나요?'); body = grid(1, H6_DECS.map(x => [x, t(H6_DEC[x].en, H6_DEC[x].ko)])); }
  else if (q.kind === 'key') { title = t('Is ' + h6KeyName(q.x) + ' related to ' + h6KeyName(q.h) + '?', h6KeyName(q.x) + '는 ' + h6KeyName(q.h) + '의 근친조일까요?'); body = grid(2, [['yes', t('Related', '근친조')], ['no', t('Not related', '근친조 아님')]]); }
  else { title = t('Two parts: does this interval blend (3rd, 5th, 6th, octave)?', '두 성부: 이 음정은 어울릴까요(3도, 5도, 6도, 8도)?'); body = <><SpKb lo={-12} hi={19} W={11} H={58} lit={{ [q.b]: 'pale', [q.s]: 'cor' }} names={{ [q.b]: lwLet(q.b), [q.s]: lwLet(q.s) }}/>{grid(2, [['yes', t('Blends', '어울려요')], ['no', t('Clashes', '부딪혀요')]])}</>; }
  const why = !done || pixel ? null : q.kind === 'v7' ? t('The bass on degree ' + H6_V7[q.inv].bassDeg + ': ' + H6_V7[q.inv].nm + ' (' + H6_V7[q.inv].fig + ').', '베이스가 ' + H6_V7[q.inv].bassDeg + '번 음: ' + H6_V7[q.inv].nm + '(' + H6_V7[q.inv].fig + ').') : q.kind === '64' ? t(H6_64[q.id].en + ', the bass ' + H6_64[q.id].bass.join(' ') + '.', H6_64[q.id].ko + ', 베이스 ' + H6_64[q.id].bass.join(' ') + '.') : q.kind === 'dec' ? t(H6_DEC[q.id].what[0], H6_DEC[q.id].what[1])
    : q.kind === 'key' ? t('The family of ' + h6KeyName(q.h) + ': ' + h6Family(q.h).top.concat(h6Family(q.h).bot).map(h6KeyName).join(', ') + '.', h6KeyName(q.h) + '의 가족: ' + h6Family(q.h).top.concat(h6Family(q.h).bot).map(h6KeyName).join(', ') + '.') : (h6Iv(q.b, q.s).cons ? t('It is ', '') + h6IvName(q.b, q.s) + t(': on the list.', ': 목록에 있어요.') : t('It is ', '') + h6IvName(q.b, q.s) + t(': not a 3rd, 5th, 6th or octave.', ': 3도, 5도, 6도, 8도가 아니에요.'));
  return (<div>
    <p style={pixel ? {fontSize:11.5,textAlign:'center'} : {fontSize:15,fontWeight:700,textAlign:'center',margin:'0 0 8px',color:'var(--muted)',textWrap:'balance'}}>{title}</p>
    {again}{body}
    {why && <div style={{marginTop:10,fontSize:13.5,color:'#4a4d86',background:'#fff',borderRadius:8,padding:'7px 10px',lineHeight:1.45}}>{why}</div>}
  </div>);
}
const h6AnswerLabel = (q) => (q.kind === 'v7' ? H6_V7[q.answer].nm : q.kind === '64' ? (q.answer === 'pass' ? t('Passing', '경과') : t('Cadential', '종지')) : q.kind === 'dec' ? t(H6_DEC[q.answer].en, H6_DEC[q.answer].ko) : q.answer === 'yes' ? t('Yes', '네') : t('No', '아니요'));
Object.assign(HARMONY_6_DRILL, { levels: H6_LEVELS, generate: genH6Question, check: (q, ans) => ans !== null && ans !== undefined && ans === q.answer, answerLabel: h6AnswerLabel, Question: H6Question, Learn: H6Learn });
// the teacher's copy and the Workbook
const H6_WB = {
  v7: [['C', 'b'], ['G', 'd'], ['F', 'c'], ['D', 'a']],
  fam: [[7, 'M'], [2, 'm'], [10, 'M'], [4, 'm']],
  two: [[-12, 4], [-10, 5], [-8, 0], [-7, 2], [-5, 4], [-12, 12]],
  chk: { v7: [['Bb', 'c'], ['C', 'd'], ['G', 'b'], ['F', 'a']], dec: ['A top note held over into the next chord, then falling a step', 'A piece in A minor ending on A C♯ E', 'Over V the top line goes F E D, the E on the beat', 'The bass walks C D E under I, ?, Ib'], fam: [[5, 'M'], [9, 'm'], [3, 'M'], [7, 'm']], two: [[-12, 4], [-10, 7], [-8, 1], [-7, 9]] },
};
const H6_DEC_ANS = ['a suspension', 'the Picardy third', 'an accented passing note', 'Vc (a passing six-four)'];
function H6Teacher() {
  const pages = [], W = H6_WB;
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="harmony-6" teacher>{content}</WbPage>);
  const fam = (h) => h6KeyName(h) + ': ' + h6Family(h).top.concat(h6Family(h).bot).filter(x => !h6Same(x, h)).map(h6KeyName).join(', ');
  P(<>
    <div style={{fontFamily:LB_SERIF,fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('harmony-6')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 12px',lineHeight:1.5}}>Theory of Music Grade 6 (Manual of Syllabuses 2026). The figures, the passing six-four examples and the definitions of the decorations are textbook harmony written from our own knowledge: please check them against the books you teach from.</div>
    <TcBlock page={2} title="V7 and its inversions" answers={<>{tcAns('TRY IT', W.v7.map(([k, inv]) => H6_KEYS[k][1] + ' major, bass ' + h6Let(k, h6T(H6_V7[inv].v, H6_KEYS[k][0])[0]) + ': ' + H6_V7[inv].nm))}{tcAns('FIGURES', ['V7: 7', 'V7b: 6 5', 'V7c: 4 3', 'V7d: 4 2'], null)}</>}
      watch="Naming the chord by its top note. The bass decides; and V7d's bass (the 7th) must fall, so it goes to Ib."
      say="“The bass names it; the 7th falls, the leading note rises.”"/>
    <TcBlock page={3} title="Passing six-fours" answers={<>{tcAns('EXAMPLES', ['I – Vc – Ib (bass 1 2 3)', 'IV – Ic – IVb (bass 4 5 6)', 'cadential: Ic – V – I (bass 5 5 1)'], null)}</>}
      watch="Every second inversion called cadential. Ask where the bass goes next."
      say="“Walking bass: passing. Staying bass: cadential.”"/>
    <TcBlock page={4} title="Suspensions, passing notes and the Picardy third" answers={<>{tcAns('IN THE APP', ['suspension: C over G, falling to B (4–3)', 'accented passing note: E over V, between F and D', 'Picardy third: A minor ending on A C♯ E'], null)}</>}
      watch="A suspension without its preparation (the note must be heard in the chord before)."
      say="“Hold and fall; pass on the beat; end in major.”"/>
  </>);
  P(<>
    <TcBlock page={5} title="The six related keys" answers={<>{tcAns('TRY IT', W.fam.map(fam))}</>}
      watch="The relative of the home key found, but not the relatives of the dominant and subdominant."
      say="“Dominant, subdominant, and their relatives.”"/>
    <TcBlock page={6} title="Two parts: a tune above a bass" answers={<>{tcAns('TRY IT (EXAMPLE ANSWER)', ['E D C D E C over C D E F G C: 3 8 6 6 6 8 (the last C an octave higher)'], null)}{tcAns('RULES', ['3rds, 6ths, perfect 5ths, octaves', 'no consecutive 5ths or octaves', 'end on the octave or a 3rd'], null)}</>}
      watch="Parallel octaves at the end (G over G, then C over C). Approach the last octave by contrary motion."
      say="“3rds and 6ths blend; no two 5ths or octaves in a row.”"/>
    <TcBlock page={7} title="The check-up on paper (the Workbook's last page)" answers={<>{tcAns('A', W.chk.v7.map(([k, inv]) => H6_V7[inv].nm))}{tcAns('B', H6_DEC_ANS, 5)}{tcAns('C', W.chk.fam.map(h => h6Family(h).top.concat(h6Family(h).bot).filter(x => !h6Same(x, h)).map(h6KeyName).join(', ')), 9)}{tcAns('D', W.chk.two.map(([b, d]) => (h6Iv(b, b + d).cons ? 'Y ' : 'N ') + '(' + h6IvNum(b, b + d) + ')'), 13)}
      <div style={{fontSize:12,color:BK.ink,marginTop:6,lineHeight:1.5}}>One mark for each answer (C: one mark per complete family). Score each part on its own (4 marks each, pass 3+). Not passed? Go back to that step's page: A p.2 · B pp.3–4 · C p.5 · D p.6.</div></>}/>
  </>);
  return <>{pages}</>;
}
TEACHER_COPIES['harmony-6'] = H6Teacher;
function H6Workbook({ startNo = 1 }) {
  const W = H6_WB, pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + 1 + pages.length} chId="harmony-6">{content}</WbPage>);
  P(<>
    <WbTop step={1}/>
    <Part kind="together" title="Name it from the bass" how="Each chord is a dominant 7th; the coral key is the bass. Write V7, V7b, V7c or V7d.">
      <BkGrid cols={2} gap="6px 10px">{W.v7.map(([k, inv], i) => { const V = h6T(H6_V7[inv].v, H6_KEYS[k][0]); return <ExCell key={i} n={i + 1} ex={i === 0}><div style={{display:'grid',gap:4,padding:'16px 4px 4px'}}>{s4wLabel(H6_KEYS[k][1] + ' major')}
        <SpKb lo={-24} hi={20} W={9} H={38} lit={Object.fromEntries(V.map((x, j) => [x, j === 0 ? 'cor' : 'pale']))} names={{ [V[0]]: h6Let(k, V[0]) }} k={1}/>
        <div style={{display:'flex',justifyContent:'center'}}>{nvBox(i === 0, H6_V7[inv].nm, 60, 26)}</div></div></ExCell>; })}</BkGrid>
    </Part>
    <Part kind="home" title="This week" how="Tick a box each day.">
      <PhLog rows={['C major: G7 in all four positions, each resolved', 'Say the figure as you play: 7, 6 5, 4 3, 4 2', 'G and F major the same']} label={300}/>
    </Part>
    <Faces/>
  </>);
  P(<>
    <WbTop step={2}/>
    <Part kind="together" title="Fill the gap" how="A passing six-four sits between two positions of one chord, the bass walking by step. Write the middle chord.">
      <div style={{display:'grid',gap:10,padding:'4px 0'}}>{[['I', 'Ib', 'C D E', 'Vc'], ['IV', 'IVb', 'F G A', 'Ic']].map(([a, b, bs, ans], i) => <ExCell key={i} n={i + 1} ex={i === 0}><div style={{display:'flex',alignItems:'center',justifyContent:'center',gap:10,padding:'16px 4px 6px',fontFamily:LB_SERIF,fontSize:18,fontWeight:900,color:BK.ink}}>{a} – {nvBox(i === 0, ans, 54, 28)} – {b}<span style={{fontFamily:'Inter, sans-serif',fontSize:12,color:BK.muted}}>bass {bs}</span></div></ExCell>)}</div>
    </Part>
    <Part kind="home" title="Decorations this week" how="Tick a box each day.">
      <PhLog rows={['Play IV–V–I in C, then with a 4–3 suspension over V', 'Add an accented passing note: F–E–D over V', 'A minor iv–V–I, then end with C♯: the Picardy third']} label={300}/>
    </Part>
    <Faces/>
  </>);
  P(<>
    <WbTop step={4}/>
    <Part kind="together" title="The family" how="Write the five keys related to each home key.">
      <div style={{display:'grid',gap:8}}>{W.fam.map((h, i) => <ExCell key={i} n={i + 1} ex={i === 0}><div style={{display:'flex',alignItems:'center',gap:10,padding:'16px 4px 6px',fontSize:13,fontWeight:800,color:BK.ink}}><span style={{minWidth:90}}>{h6KeyName(h)}:</span>{nvBox(i === 0, h6Family(h).top.concat(h6Family(h).bot).filter(x => !h6Same(x, h)).map(h6KeyName).join(', '), 360, 26)}</div></ExCell>)}</div>
    </Part>
    <Faces/>
  </>);
  P(<>
    <WbTop step={5}/>
    <Part kind="together" title="A tune above the bass" how="Above each bass note write a note a 3rd, 5th, 6th or octave higher. No two 5ths or octaves in a row; end on the octave or a 3rd. Write the interval number under each pair.">
      <div style={{display:'grid',gap:6,padding:'4px 0'}}>
        {s4wRow('tune', <div style={{display:'flex',gap:3}}>{W.two.map(([b, d], j) => <span key={j}>{nvBox(false, '', 44, 30)}</span>)}</div>)}
        {s4wRow('bass', scfwLetters(W.two.map(([b]) => lwLet(b)), 44))}
        {s4wRow('interval', <div style={{display:'flex',gap:3}}>{W.two.map((_, j) => <span key={j}>{bkBox(44, 26)}</span>)}</div>)}
      </div>
    </Part>
    <Part kind="home" title="Two parts this week" how="Tick a box each day.">
      <PhLog rows={['Play your tune with the bass: the left hand the bass, the right hand the tune', 'Write a second tune in 6ths, moving against the bass', 'Try the G major bass in the app']} label={300}/>
    </Part>
    <Faces/>
  </>);
  P(<H6PaperCheck/>);
  return <>{pages}</>;
}
function H6PaperCheck() {
  const C = H6_WB.chk;
  return <div className="lb-paper" style={{display:'flex',flexDirection:'column',gap:4}}>
    <LbPaperHead/>
    {bkSec('A', 'Which dominant 7th? (the coral key is the bass)')}
    <BkGrid cols={4} gap="6px 8px">{C.v7.map(([k, inv], i) => { const V = h6T(H6_V7[inv].v, H6_KEYS[k][0]); return <BkCell key={i} n={i + 1}><div style={{display:'grid',gap:3,padding:'14px 0 0'}}>{s4wLabel(H6_KEYS[k][1] + ' major')}<SpKb lo={-24} hi={20} W={5.4} H={28} lit={Object.fromEntries(V.map((x, j) => [x, j === 0 ? 'cor' : 'pale']))} names={{}} k={1}/><div style={{display:'flex',justifyContent:'center'}}>{bkBox(54, 24)}</div></div></BkCell>; })}</BkGrid>
    {bkSec('B', 'Name it')}
    <BkGrid cols={2} gap="6px 8px">{C.dec.map((x, i) => <BkCell key={i} n={i + 5}><div style={{display:'grid',gap:4,padding:'14px 2px 2px',fontSize:11.5,fontWeight:800,color:BK.ink}}>{x}{bkBox(150, 22)}</div></BkCell>)}</BkGrid>
    {bkSec('C', 'The five related keys of …')}
    <BkGrid cols={2} gap="6px 8px">{C.fam.map((h, i) => <BkCell key={i} n={i + 9}><div style={{display:'grid',gap:4,padding:'14px 2px 2px',fontSize:11.5,fontWeight:800,color:BK.ink}}>{h6KeyName(h)}{bkBox(240, 22)}</div></BkCell>)}</BkGrid>
    {bkSec('D', 'Bass and tune: does the interval blend? Y or N')}
    <BkGrid cols={4} gap="6px 8px">{C.two.map(([b, d], i) => <BkCell key={i} n={i + 13}><div style={{display:'grid',gap:4,padding:'14px 0 0',justifyItems:'center',fontSize:11.5,fontWeight:800,color:BK.ink}}>{lwLet(b) + ' and ' + lwLet(b + d) + ' above'}{bkBox(40, 22)}</div></BkCell>)}</BkGrid>
  </div>;
}
WORKBOOKS['harmony-6'] = H6Workbook;
'''
rep("""TEACHER_COPIES['harmony-5'] = H5Teacher;""", """TEACHER_COPIES['harmony-5'] = H5Teacher;""" + CH)

HOME = r'''
// ══ Build BR: Chords and Cadences, Grade 6 on the Home (Pitch, Chords) ══
LBH_FN['harmony-6'] = (s) => h6LbPages(s);
const h6HomeAdd = (id, i, en, ko, benEn, bko, make) => lbhAdd(id, 'p-chords', 'pitch', en, ko, benEn, bko, lbhSpec('harmony-6', i, { make }));
const h6V7Q = (n, prev) => { let k, inv, g = 0; do { k = pick(Object.keys(H6_KEYS)); inv = H6_INV[n % 4]; } while (prev && prev.key === k + inv && g++ < 10); const V = h6T(H6_V7[inv].v, H6_KEYS[k][0]);
  return { kind: 'choice', cols: 4, key: k + inv, prompt: [H6_KEYS[k][1] + ' major: which dominant 7th? Look at the bass.', H6_KEYS[k][1] + '장조: 어떤 딸림7? 베이스를 봐요.'], opts: H6_INV.map(x => ({ id: x, label: () => H6_V7[x].nm })), ans: inv, ok: (v) => v === inv,
    play: () => h6Play([{ v: H6_V7[inv].v }, { v: H6_V7[inv].to, len: 3 }], 66, H6_KEYS[k][0]), fig: () => ({ mid: <SpKb lo={-24} hi={20} W={11} H={60} lit={Object.fromEntries(V.map((x, j) => [x, j === 0 ? 'cor' : 'pale']))} names={Object.fromEntries(V.map(x => [x, h6Let(k, x)]))}/> }),
    yes: ['Yes: the bass on degree ' + H6_V7[inv].bassDeg + '.', '맞아요: 베이스가 ' + H6_V7[inv].bassDeg + '번 음.'], no: ['It was ' + H6_V7[inv].nm + ': the bass on degree ' + H6_V7[inv].bassDeg + '.', '정답은 ' + H6_V7[inv].nm + ': 베이스가 ' + H6_V7[inv].bassDeg + '번 음.'] }; };
const h6EarQ = (kind) => (n, prev) => { const ids = kind === '64' ? Object.keys(H6_64) : H6_DECS; let id, g = 0; do { id = pick(ids); } while (prev && prev.key === id && g++ < 10); const ans = kind === '64' ? H6_64[id].kind : id;
  const opts = kind === '64' ? [{ id: 'pass', label: () => t('Passing', '경과') }, { id: 'cad', label: () => t('Cadential', '종지') }] : H6_DECS.map(x => ({ id: x, label: () => t(H6_DEC[x].en, H6_DEC[x].ko) }));
  return { kind: 'choice', cols: kind === '64' ? 2 : 1, key: id, prompt: kind === '64' ? ['Listen to the bass: passing or cadential?', '베이스를 들어요: 경과? 종지?'] : ['Which decoration?', '어떤 장식?'], opts, ans, ok: (v) => v === ans,
    play: () => h6Play(kind === '64' ? H6_64[id].seq : H6_DEC[id].dec), fig: () => ({ mid: null }),
    yes: ['Yes.', '맞아요.'], no: kind === '64' ? ['It was ' + H6_64[id].en + ', the bass ' + H6_64[id].bass.join(' ') + '.', '정답은 ' + H6_64[id].ko + ', 베이스 ' + H6_64[id].bass.join(' ') + '.'] : [H6_DEC[id].what[0], H6_DEC[id].what[1]] }; };
h6HomeAdd('h6-v7', 1, 'V7 and its inversions', 'V7과 그 자리바꿈', 'The bass names it: root, 3rd, 5th or 7th.', '베이스가 이름을: 근음, 3음, 5음, 7음.', h6V7Q);
h6HomeAdd('h6-64', 2, 'Passing six-fours', '경과 6-4화음', 'A walking bass, or a bass that stays for V?', '걷는 베이스, 아니면 V로 머무는 베이스?', h6EarQ('64'));
h6HomeAdd('h6-dec', 3, 'Suspensions, passing notes and the Picardy third', '계류음, 경과음, 피카르디 3도', 'Hear the decoration.', '장식을 들어요.', h6EarQ('dec'));
h6HomeAdd('h6-keys', 4, 'The six related keys', '여섯 근친조', 'Find the five keys closest to home, and travel there.', '집에 가장 가까운 다섯 조를 찾아 여행해요.', lwTapQ(H6KeysPad, (n) => ({ fixed: n % H6_HOMES.length }), ['Tap the five related keys.', '근친조 다섯을 눌러요.'], ['All five ✓', '다섯 모두 ✓']));
h6HomeAdd('h6-two', 5, 'Two parts: a tune above a bass', '두 성부: 베이스 위의 선율', '3rds, 5ths, 6ths and octaves; no two 5ths in a row.', '3도, 5도, 6도, 8도; 5도 연달아는 안 돼요.', lwTapQ(TwoPartPad, () => ({}), ['Write a note above each bass note.', '베이스 음마다 위에 한 음씩.'], ['It blends ✓', '어울려요 ✓']));
'''
rep("""
lbhAdd('rb-finger', 'r-beat', 'rhythm', 'The beat in your fingers'""", HOME + """
lbhAdd('rb-finger', 'r-beat', 'rhythm', 'The beat in your fingers'""")
rep("""    { id: 'ch-5', en: 'Chords and cadences, Grade 5', ko: '화음과 종지, Grade 5', lessons: ['h5-inv', 'h5-c64', 'h5-pass', 'h5-pre', 'h5-harm'], check: 'harmony-5' },   // Build BC""",
    """    { id: 'ch-5', en: 'Chords and cadences, Grade 5', ko: '화음과 종지, Grade 5', lessons: ['h5-inv', 'h5-c64', 'h5-pass', 'h5-pre', 'h5-harm'], check: 'harmony-5' },   // Build BC
    { id: 'ch-6', en: 'Chords and cadences, Grade 6', ko: '화음과 종지, Grade 6', lessons: ['h6-v7', 'h6-64', 'h6-dec', 'h6-keys', 'h6-two', 'mk-two'], check: 'harmony-6' },   // Build BR""")
rep("""  set('5', 'h5-inv h5-c64 h5-pass h5-pre h5-harm');   // Build BC: Chords and Cadences, Grade 5""", """  set('5', 'h5-inv h5-c64 h5-pass h5-pre h5-harm');   // Build BC: Chords and Cadences, Grade 5
  set('6', 'h6-v7 h6-64 h6-dec h6-keys h6-two mk-two');   // Build BR: Chords and Cadences, Grade 6 (Theory of Music Grade 6)""")
rep("""  { id: 'mk-wave', ch: 'arps-6',""", """  { id: 'mk-two', ch: 'harmony-6', title: 'My tune above a bass', blurb: 'Write a tune note by note above a bass; every interval is checked as you go.', C: () => <TwoPartPad toy/> },   // Build BR
  { id: 'mk-wave', ch: 'arps-6',""")
rep("""  'mk-wave': ['나의 아르페지오 하프',""", """  'mk-two': ['베이스 위의 내 선율', '베이스 위에 한 음씩 선율을 써요; 쓰는 대로 음정을 확인해요.'],
  'mk-wave': ['나의 아르페지오 하프',""")
rep("""'mk-wave': ['chords', 3, 3, 'game ear'],""", """'mk-wave': ['chords', 3, 3, 'game ear'], 'mk-two': ['chords', 3, 3, 'write ear'],""")
rep("""  'mk-wave': () => (\n""", """  'mk-two': () => (
    <svg width="34" height="34" viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#3b4fa8"/><path d="M3 8 L9 6 L15 9 L21 5" fill="none" stroke="#e9a83a" strokeWidth="2"/><path d="M3 18 L9 15 L15 17 L21 14" fill="none" stroke="#fefbf3" strokeWidth="2"/></svg>
  ),
  'mk-wave': () => (\n""")
rep("""const LESSON_BOOKS = { 'arps-6': Arps6LessonBook,""", """const LESSON_BOOKS = { 'harmony-6': Harmony6LessonBook, 'arps-6': Arps6LessonBook,""")
rep("""const LB_PAGE_FNS = { 'arps-6': a6LbPages,""", """const LB_PAGE_FNS = { 'harmony-6': h6LbPages, 'arps-6': a6LbPages,""")
rep("""const HOUSE_ICONS = {""", """const HOUSE_ICONS = {"harmony-6": "<ellipse cx=\\"14\\" cy=\\"36\\" rx=\\"5.2\\" ry=\\"3.8\\" transform=\\"rotate(-20 14 36)\\" fill=\\"#e4572e\\" stroke=\\"#e4572e\\"/><ellipse cx=\\"14\\" cy=\\"28\\" rx=\\"5.2\\" ry=\\"3.8\\" transform=\\"rotate(-20 14 28)\\" fill=\\"#26296b\\"/><ellipse cx=\\"14\\" cy=\\"20\\" rx=\\"5.2\\" ry=\\"3.8\\" transform=\\"rotate(-20 14 20)\\" fill=\\"#26296b\\"/><ellipse cx=\\"14\\" cy=\\"12\\" rx=\\"5.2\\" ry=\\"3.8\\" transform=\\"rotate(-20 14 12)\\" fill=\\"#26296b\\"/><text x=\\"26\\" y=\\"30\\" font-size=\\"14\\" font-weight=\\"900\\" fill=\\"#26296b\\" stroke=\\"none\\" font-family=\\"Inter, sans-serif\\">7</text>", """)
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
