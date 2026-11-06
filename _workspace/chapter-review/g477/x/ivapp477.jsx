// ─── Phase 477: chapter 21's pads (pages 1 to 6), the screen lesson and the drill ───
const IVX_W = 300;   // a pad's staff width on a phone
// play an interval: melodic low then high (a falling one high then low), or harmonic
const ivxPlay = (p) => { stopClicks(); if (p.down && !p.harm) playIv(p.b, p.a, 'melodic'); else playIv(p.a, p.b, p.harm ? 'harmonic' : 'melodic'); };
const ivxMidis = (p) => [ivMidi(p.a), ivMidi(p.b)];
// the keys under a pair: from the lower note's white key (a flat's white key below it), wide enough for both
const ivxKeyRange = (p) => { const d0 = p.a.d - (p.a.acc < 0 ? 1 : 0), d1 = p.b.d + (p.b.acc > 0 ? 1 : 0); return [d0, Math.max(5, d1 - d0 + 1)]; };
const ivxMsg = (msg, bad) => <div style={{textAlign:'center',fontSize:15,fontWeight:900,color:bad ? BK.coral : BK.ink,minHeight:22,margin:'6px 0',textWrap:'balance',wordBreak:'keep-all'}}>{sscSx(ivxKoT(msg))}</div>;
const ivxCountWords = (p) => { const n = p.b.d - p.a.d + 1, L = Array.from({ length: n }, (_, k) => dName(p.a.d + k)).join(' ');
  return t(L + ', ' + (n === 8 ? 'an octave' : 'a ' + ivxEn(n)), L + ', ' + (n === 8 ? '옥타브' : n + '도')); };
const ivxNums = (n) => <div style={{display:'grid',gridTemplateColumns:'repeat(4,minmax(0,1fr))',gap:6,maxWidth:340,margin:'8px auto 4px'}}>{n}</div>;
const IVX_SCALE_N = (d) => Object.fromEntries([0, 1, 2, 3, 4].map(i => [d + i, String(i + 1)]));

// pages 2, 4 and 5: an interval to count (page 5: melodic or harmonic?); ▶ Listen, ▶ Count it (the ladder), the next one
const IVX_SETS = {
  p2: [[28, 30], [32, 35], [29, 33], [30, 32, 'down'], [31, 36], [33, 34]].map(([a, b, w]) => ({ a: IVX_N(a), b: IVX_N(b), down: w === 'down' })),
  p4: [[28, 33], [28, 34], [28, 35], [29, 34], [30, 36], [32, 39]].map(([a, b]) => ({ a: IVX_N(a), b: IVX_N(b), harm: true })),
  p5: [[28, 30, 0], [28, 30, 1], [32, 33, 1], [29, 33, 0], [31, 35, 1], [30, 31, 0]].map(([a, b, h]) => ({ a: IVX_N(a), b: IVX_N(b), harm: !!h })),
};
const IVX_PAD_T = { p2: () => t('Count it', '몇 도일까요?'), p4: () => t('6th, 7th or octave?', '6도, 7도, 옥타브?'), p5: () => t('Melodic or harmonic?', '선율적? 화성적?') };
function IvxCountPad({ set }) {
  const list = IVX_SETS[set], [i, setI] = useState(0), [ans, setAns] = useState(null), [lad, setLad] = useState(false);
  useEffect(() => () => stopClicks(), []);
  const p = list[i], n = p.b.d - p.a.d + 1, mh = set === 'p5', right = mh ? (p.harm ? 'harm' : 'mel') : n;
  const choices = mh ? ['mel', 'harm'] : set === 'p4' ? [5, 6, 7, 8] : [2, 3, 4, 5, 6, 7, 8];
  const name = (c) => mh ? ivxP5Lab(c === 'harm' ? 'harm' : 'mel') : ivxShort(c);
  const done = ans != null && String(ans) === String(right);
  const pick = (c) => { setAns(c); ivxPlay(p); if (String(c) === String(right)) setLad(true); };
  const next = () => { stopClicks(); setI((i + 1) % list.length); setAns(null); setLad(false); };
  const d0 = p.a.d - (p.a.acc < 0 ? 1 : 0);   // eight keys from the lower note's letter: the keyboard never gives the answer away
  const msg = ans == null ? (mh ? t('One after the other, or together?', '차례로? 함께?') : t('How many letters, both notes included?', '몇 도일까요? 두 음 모두 세요.'))
    : done ? (mh ? (p.harm ? t('Harmonic: together. ', '화성적: 함께. ') : t('Melodic: one after the other. ', '선율적: 차례로. ')) : '') + ivxCountWords(p) + ' ✓'
    : mh ? t('Look again: together (one above the other, or touching), or one after the other?', '다시 봐요: 함께(위아래로, 또는 붙어서)? 차례로?') : t('Count again: the lower note is 1.', '다시 세어요: 아래 음이 1이에요.');
  return (
    <div className="try-box" style={actBox} data-ivx={'pad-' + set}>
      <div style={actTitle}>{IVX_PAD_T[set]()}</div>
      <div style={actNote}>{ivxKoT(t('▶ Listen, then pick the answer. ▶ Count it shows the count on the staff.', '▶ 듣기를 누르고 답을 골라요. ▶ 세어 보기를 누르면 오선에 숫자가 나와요.'))}</div>
      <div style={{maxWidth:IVX_W,margin:'0 auto'}}><IvxStaff pairs={[{ ...p, ladder: lad }]} width={IVX_W} o={{ x0: 70 }}
        label={t((p.harm ? 'Together: ' : 'One after the other: ') + ivxNoteTxt(p.down ? p.b : p.a) + ' and ' + ivxNoteTxt(p.down ? p.a : p.b) + '.', (p.harm ? '함께: ' : '차례로: ') + ivxNoteTxt(p.down ? p.b : p.a) + '와 ' + ivxNoteTxt(p.down ? p.a : p.b) + '.')}/></div>
      <div style={{maxWidth:8 * 40,margin:'6px auto 0'}}><SacKeys d0={d0} n={8} o={{ lit: done ? [ivMidi(p.a)] : [], pale: done ? [ivMidi(p.b)] : [], H: 100 }} onTap={(m) => sacKey(m)}/></div>
      {ivxMsg(msg, ans != null && !done)}
      <div style={{display:'grid',gridTemplateColumns:'repeat(' + Math.min(choices.length, 4) + ',minmax(0,1fr))',gap:6,maxWidth:340,margin:'0 auto 8px'}}>
        {choices.map(c => <button key={c} className={'chip' + (ans != null && String(c) === String(ans) ? ' active' : '')} style={{minHeight:44,justifyContent:'center',fontWeight:900}} onClick={() => pick(c)}>{name(c)}</button>)}</div>
      <div style={{display:'flex',gap:6,justifyContent:'center',flexWrap:'wrap'}}>
        <button className="ghost-btn" style={{minHeight:44}} onClick={() => ivxPlay(p)}>{t('▶ Listen', '▶ 듣기')}</button>
        <button className="ghost-btn" style={{minHeight:44}} onClick={() => setLad(true)}>{t('▶ Count it', '▶ 세어 보기')}</button>
        <button className="ghost-btn" style={{minHeight:44}} onClick={next}>{t('Next →', '다음 →')}</button>
      </div>
    </div>
  );
}
// page 3: C or G position, a finger number over each key: tap a key, the thumb sounds with it
function IvxHandPad() {
  const [pos, setPos] = useState(28), [b, setB] = useState(null);
  useEffect(() => () => stopClicks(), []);
  const thumb = IVX_N(pos), p = b == null ? null : { a: thumb, b: IVX_N(b), harm: true }, n = b == null ? null : b - pos + 1;
  const tap = (m) => { const k = Array.from({ length: 5 }, (_, i) => pos + i).find(d => ivMidi({ d }) === m); if (k == null) { sacKey(m); return; } setB(k); stopClicks(); playIv(thumb, IVX_N(k), 'harmonic'); };
  return (
    <div className="try-box" style={actBox} data-ivx="pad-hand">
      <div style={actTitle}>{t('In the hand', '손 안의 음정')}</div>
      <div style={actNote}>{ivxKoT(t('Tap a key: the thumb’s note sounds with it. Finger 3: a 3rd.', '건반을 누르면 엄지 음과 함께 울려요. 3번 손가락이면 3도.'))}</div>
      <div style={{display:'flex',gap:6,justifyContent:'center',margin:'0 0 8px'}}>{[[28, t('C position', 'C 자리')], [32, t('G position', 'G 자리')]].map(([d, w]) => <button key={d} className={'chip' + (pos === d ? ' active' : '')} style={{minHeight:44}} onClick={() => { stopClicks(); setPos(d); setB(null); }}>{w}</button>)}</div>
      <div style={{maxWidth:IVX_W,margin:'0 auto'}}><IvxStaff pairs={p ? [{ ...p, lab: t('1 and ' + n, n === 1 ? '1번만' : '1번과 ' + n + '번'), lab2: n === 1 ? t('unison', '1도') : ivxShort(n) }] : [{ a: thumb, b: thumb, harm: true }]} width={IVX_W} o={{ x0: 70, labSize: 14 }}/></div>
      <div style={{maxWidth:260,margin:'6px auto 0'}}><IvxKeys d0={pos} n={5} nums={IVX_SCALE_N(pos)} numCol={PEN_N} o={{ H: 120, lit: [ivMidi(thumb)], pale: b != null && b !== pos ? [ivMidi({ d: b })] : [] }} onTap={tap}/></div>
      {ivxMsg(p ? (n === 1 ? t('The same note: a unison.', '같은 음: 1도.') : t('Thumb and finger ' + n + ': ' + ivxCountWords(p) + '.', '엄지와 ' + n + '번 손가락: ' + ivxCountWords(p) + '.')) : t('Tap finger 2, 3, 4 or 5.', '2, 3, 4, 5번 손가락 건반을 눌러요.'))}
    </div>
  );
}
// page 6: pick a key and a number: the tonic and the note above it (with the key signature), major or perfect
const IVX_TONIC_KEYS = ['C', 'G', 'D', 'F'];
function IvxTonicPad() {
  const [k, setK] = useState('G'), [n, setN] = useState(3);
  useEffect(() => () => stopClicks(), []);
  const sc = ivxScale(k), p = { a: sc[0], b: sc[n - 1], harm: true }, q = IVX_MP[n];
  const [d0, nk] = ivxKeyRange({ a: sc[0], b: sc[7] });
  const pickN = (x) => { setN(x); const s = ivxScale(k); stopClicks(); playIv(s[0], s[x - 1], 'harmonic'); };
  return (
    <div className="try-box" style={actBox} data-ivx="pad-tonic">
      <div style={actTitle}>{t('Above the tonic', '으뜸음 위의 음정')}</div>
      <div style={actNote}>{ivxKoT(t('Pick a key, then a number: the tonic sounds with that note of the scale.', '조를 고르고 몇 도인지 골라요. 으뜸음과 그 음이 함께 울려요.'))}</div>
      <div style={{display:'flex',gap:6,justifyContent:'center',margin:'0 0 6px'}}>{IVX_TONIC_KEYS.map(x => <button key={x} className={'chip' + (x === k ? ' active' : '')} style={{minHeight:44,minWidth:48,justifyContent:'center',fontWeight:900}} onClick={() => { stopClicks(); setK(x); }}>{sscSx(prettyNote(x))}</button>)}</div>
      <div style={{maxWidth:IVX_W,margin:'0 auto'}}><IvxStaff pairs={[{ ...p, lab: ivxQ(q), lab2: ivxShort(n) }]} width={IVX_W} o={{ x0: 64, labSize: 15, key: k }} label={t(skgKeyName(k) + ': ' + ivxNoteTxt(p.a) + ' and ' + ivxNoteTxt(p.b) + ', a ' + ivxQName(q, n) + '.', skgKeyName(k) + ': ' + ivxNoteTxt(p.a) + '와 ' + ivxNoteTxt(p.b) + ', ' + ivxQName(q, n) + '.')}/></div>
      <div style={{maxWidth:nk * 36,margin:'6px auto 0'}}><SacKeys d0={d0} n={nk} o={{ lit: [ivMidi(p.a)], pale: [ivMidi(p.b)], H: 100 }} onTap={(m) => sacKey(m)}/></div>
      {ivxNums([2, 3, 4, 5, 6, 7, 8].map(x => <button key={x} className={'chip' + (x === n ? ' active' : '')} style={{minHeight:44,justifyContent:'center',padding:'4px 2px',fontWeight:900}} onClick={() => pickN(x)}>{ivxShort(x)}</button>))}
      {ivxMsg(t(skgKeyName(k) + ': ' + ivxNoteTxt(p.a) + ' to ' + ivxNoteTxt(p.b) + ', a ' + ivxQName(q, n) + '.', skgKeyName(k) + ': ' + ivxNoteTxt(p.a) + '에서 ' + ivxNoteTxt(p.b) + ', ' + ivxQName(q, n) + '.'))}
    </div>
  );
}

// the ladder: page 1 (from C, G, D or F) and again at the end (the teacher's keys, else the exam's four; with the key
// signature, major and perfect); tap a number; two staves (2nd to 5th, 6th to octave) so the words stay readable
function IvxMapPad({ end }) {
  const { keys, fromTeacher } = pbKeysFor('scales'), list = end && fromTeacher ? keys : IVX_TONIC_KEYS;   // the exam's four keys unless the teacher set some
  const [k, setK] = useState(list[0]), [n, setN] = useState(null);
  useEffect(() => () => stopClicks(), []);
  const sc = ivxScale(k), [d0, nk] = ivxKeyRange({ a: sc[0], b: sc[7] }), lad = ivxLadder(k, !!end, n);
  const pickN = (x) => { stopClicks(); setN(x); playIv(sc[0], sc[x - 1], 'harmonic'); };
  const all = () => { const s = ivxScale(k), ctx = getAudio(); if (!ctx) return; stopClicks(); const t0 = ctx.currentTime + 0.05;
    s.slice(1).forEach((b, i) => { blip(ctx, t0 + i * 0.75, ivFreq(s[0]), 0.65, 0.13, 'triangle'); blip(ctx, t0 + i * 0.75, ivFreq(b), 0.65, 0.13, 'triangle'); }); };
  return (
    <div className="try-box" style={actBox} data-pb="iv-map">
      {!end && <div style={actTitle}>{t('The interval ladder', '음정 사다리')}</div>}
      <div style={{...actNote,textWrap:'pretty'}}>{ivxKoT(end ? t('Every interval above the tonic: the 2nd, 3rd, 6th and 7th major; the 4th, 5th and octave perfect. Tap one to hear it.', '고른 조에서 으뜸음 위의 모든 음정: 2·3·6·7도는 장음정, 4·5·8도는 완전음정. 음정을 누르면 들려요.')
        : t('Every interval from one note, a 2nd to an octave. Tap one to hear it; ▶ All plays them in order.', '한 음에서 2도부터 옥타브까지 모든 음정. 음정을 누르면 들려요. ▶ 모두 듣기는 차례로 들려줘요.'))}</div>
      <div style={{display:'flex',gap:6,justifyContent:'center',flexWrap:'wrap',margin:'0 0 6px'}}>{list.map(x => <button key={x} className={'chip' + (x === k ? ' active' : '')} style={{minHeight:44,minWidth:44,justifyContent:'center',fontWeight:900}} onClick={() => { stopClicks(); setK(x); setN(null); }}>{sscSx(pbKeyName(x))}</button>)}</div>
      <div role="img" aria-label={ivxLadderLabel(k, !!end)} style={{maxWidth:340,margin:'0 auto'}}>
        {[lad.slice(0, 4), lad.slice(4).concat([{ blank: true }])].map((row, r) => <IvxStaff key={r} pairs={row} width={300 + 12 * Math.max(0, (end ? skgKs(k, 'treble').length : 0) - 3)} o={{ x0: 60, labSize: 14, key: end ? k : null, padTop: 12 }}/>)}</div>
      <div style={{maxWidth:nk * 36,margin:'6px auto 0'}}><SacKeys d0={d0} n={nk} o={{ lit: [ivMidi(sc[0])], pale: n ? [ivMidi(sc[n - 1])] : [], H: 96 }} onTap={(m) => sacKey(m)}/></div>
      {ivxNums([2, 3, 4, 5, 6, 7, 8].map(x => <button key={x} className={'chip' + (x === n ? ' active' : '')} style={{minHeight:44,justifyContent:'center',padding:'4px 2px',fontWeight:900}} onClick={() => pickN(x)}>{ivxShort(x)}</button>))}
      {n ? ivxMsg(t(ivxNoteTxt(sc[0]) + ' to ' + ivxNoteTxt(sc[n - 1]) + ': ' + (end ? 'a ' + ivxQName(IVX_MP[n], n) : (n === 8 ? 'an octave' : 'a ' + ivxEn(n))) + '.', ivxNoteTxt(sc[0]) + '에서 ' + ivxNoteTxt(sc[n - 1]) + ': ' + (end ? ivxQName(IVX_MP[n], n) : n === 8 ? '옥타브' : ivxShort(n)) + '.')) : null}
      {end && pbKeysRow(PB_DOT, fromTeacher, list)}
      <div style={{display:'flex',justifyContent:'center'}}><button className="ghost-btn" style={{minHeight:44}} onClick={all}>{t('▶ All', '▶ 모두 듣기')}</button></div>
    </div>
  );
}

// ── the book on screen: the opener is the lesson's head, every other page a step; the ladder again at the end ──
function IvxLearn({ onStart }) {
  const pages = ivxLbPages(true);
  const opener = pages[0];
  return (
    <Lesson id="intervals" title={bkChapterName('intervals')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="intervals"><div className="lb-screen lb-open" style={{display:'flex',flexDirection:'column',gap:12,margin:'0 0 8px'}}>{lbWordsFirst(opener.props.children)}</div></BkChapterCtx.Provider></LbScreenCtx.Provider>}>
      {pages.slice(1).map((pg, i) => (
        <Step key={i} title={<span>{pg.props.title}</span>} storeAs={'k' + (i + 1)}>
          <LbScreenPage page={pg}/>
        </Step>
      ))}
      <Step key="map" extra title={t('My intervals', '나의 음정')} storeAs="k7"><IvxMapPad end/></Step>
    </Lesson>
  );
}

// ── the drill, after page 6, in the book's order: count it (1, 2), in the hand (3), write it (4), melodic or harmonic (5),
// the bass staff (6), listening (7), above the tonic in the student's keys (8); 9 extra: major or perfect ──
const IVX_LEVELS = [
  { n: 1, label: 'Count it', kind: 'count', time: 8 },
  { n: 2, label: 'Count it: together too', kind: 'count2', time: 8 },
  { n: 3, label: 'In C or G position', kind: 'hand', time: 8 },
  { n: 4, label: 'Write it: the note above', kind: 'write', time: 14 },
  { n: 5, label: 'Melodic or harmonic?', kind: 'mh', time: 6 },
  { n: 6, label: 'The bass staff', kind: 'bass', time: 8 },
  { n: 7, label: 'Listen: 2nd, 3rd, 5th or octave?', kind: 'ear', time: 12, noPrint: true },
  { n: 8, label: 'Above the tonic, in my keys', kind: 'tonic', time: 9 },
  { n: 9, label: 'Extra: major or perfect?', kind: 'mp', time: 8 },
];
// ('The bass staff' keeps chapter 19's Korean, 낮은음자리표 오선)
Object.assign(LEVEL_KO, { 'Count it': '세어 보기', 'Count it: together too': '세어 보기: 함께 치는 음정도', 'In C or G position': 'C 자리나 G 자리에서', 'Write it: the note above': '써 보기: 위의 음',
  'Melodic or harmonic?': '선율적? 화성적?', 'Listen: 2nd, 3rd, 5th or octave?': '듣기: 2도, 3도, 5도, 8도?', 'Above the tonic, in my keys': '나의 조: 으뜸음 위의 음정', 'Extra: major or perfect?': '더 해 보기: 장음정? 완전음정?' });
const ivxNear = (n, lo = 2, hi = 8) => shuffle([n, ...shuffle([n - 1, n + 1, n - 2, n + 2, n + 3, n - 3].filter(x => x >= lo && x <= hi && x !== n)).slice(0, 3)]);
function genIvxQuestion(lv, prev) {
  const uid = Math.random(), same = (key) => prev && prev.key === key;
  for (let g = 0; g < 40; g++) {
    if (lv.kind === 'count' || lv.kind === 'count2' || lv.kind === 'bass' || lv.kind === 'mh') {
      const clef = lv.kind === 'bass' ? 'bass' : 'treble', lo = clef === 'bass' ? 16 : 28, hi = clef === 'bass' ? 28 : 40;
      const n = 2 + Math.floor(Math.random() * 7), a = lo + Math.floor(Math.random() * (hi - lo - n + 2)), b = a + n - 1;
      const harm = lv.kind === 'count' ? false : Math.random() < 0.5, down = !harm && Math.random() < 0.4, key = lv.kind + a + '-' + b + (harm ? 'h' : down ? 'd' : 'm');
      if (b > hi || same(key)) continue;
      const p = { a: IVX_N(a), b: IVX_N(b), harm, down };
      if (lv.kind === 'mh') return { kind: 'mh', key, p, clef, answer: harm ? 'harm' : 'mel', choices: ['mel', 'harm'], uid };
      return { kind: 'count', key, p, clef, answer: n, choices: ivxNear(n), uid };
    }
    if (lv.kind === 'hand') {
      const pos = Math.random() < 0.6 ? 28 : 32, n = 2 + Math.floor(Math.random() * 4), key = 'h' + pos + n;
      if (same(key)) continue;
      return { kind: 'hand', key, pos, p: { a: IVX_N(pos), b: IVX_N(pos + n - 1), harm: true }, answer: n, choices: [2, 3, 4, 5], uid };
    }
    if (lv.kind === 'write') {
      const n = 2 + Math.floor(Math.random() * 7), a = 28 + Math.floor(Math.random() * (40 - 28 - n + 2)), key = 'w' + a + n;
      if (a + n - 1 > 40 || same(key)) continue;
      return { kind: 'write', key, a: IVX_N(a), n, answer: a + n - 1, uid };
    }
    if (lv.kind === 'ear') {
      const n = pick([2, 3, 5, 8]), a = 28 + Math.floor(Math.random() * 5), harm = Math.random() < 0.4, key = 'e' + a + n;
      if (same(key)) continue;
      return { kind: 'ear', key, p: { a: IVX_N(a), b: IVX_N(a + n - 1), harm }, answer: n, choices: [2, 3, 5, 8], uid };
    }
    if (lv.kind === 'tonic' || lv.kind === 'mp') {
      const { keys } = pbKeysFor('scales'), pool = pbMyKeys() ? keys : IVX_TONIC_KEYS, k = pick(pool), sc = ivxScale(k), n = 2 + Math.floor(Math.random() * 7);
      const harm = Math.random() < 0.5, key = lv.kind + k + n;
      if (same(key)) continue;
      const p = { a: sc[0], b: sc[n - 1], harm };
      if (lv.kind === 'tonic') return { kind: 'tonic', key, k, p, answer: n, choices: ivxNear(n), uid };
      return { kind: 'mp', key, k, p, n, answer: IVX_MP[n], choices: ['M', 'P'], uid };   // the number is given: major or perfect is the question
    }
  }
  return { kind: 'count', key: 'f', p: { a: IVX_N(28), b: IVX_N(30), harm: false }, clef: 'treble', answer: 3, choices: [2, 3, 4, 5], uid };
}
const ivxCheck = (q, ans) => ans != null && String(ans) === String(q.answer);
const ivxChoiceTxt = (q, c) => q.kind === 'mh' ? ivxP5Lab(c === 'harm' ? 'harm' : 'mel') : q.kind === 'mp' ? ivxQ(c) + (LANG === 'ko' ? '음정' : '') : ivxShort(+c);
// a string: the game shows it in capitals
function ivxAnswerLabel(q) {
  const ar = ' → ';
  if (q.kind === 'write') return dName(q.answer) + t(': ' + ivxShortEn(q.n) + ' above ' + dName(q.a.d), ' (' + dName(q.a.d) + '에서 ' + ivxShort(q.n) + ' 위)');
  const p = q.p, lo = p.down && !p.harm ? p.b : p.a, hi = p.down && !p.harm ? p.a : p.b, pr = ' (' + ivxNoteTxt(lo) + (p.harm ? '–' : ar) + ivxNoteTxt(hi) + ')';
  if (q.kind === 'mh') return (q.answer === 'harm' ? t('harmonic', '화성적') : t('melodic', '선율적')) + ' ' + ivxShort(p.b.d - p.a.d + 1) + pr;
  if (q.kind === 'mp') return ivxQName(q.answer, q.n) + pr;
  return ivxShort(q.answer) + pr;
}
// level 4: write the note above. Tap the staff to place a note (it snaps to a line or space), ▲ ▼ to move it, Check. After
// the answer: a wrong note in red, the right one in green. On a worksheet (no answer, locked): the lower note and room above.
function IvxWrite({ q, given, locked, onAnswer, pixel, paper }) {
  const [g, setG] = useState(null), isDone = !!given, lo = q.a.d, hiD = Math.min(41, lo + 8), clef = 'treble';
  useEffect(() => { setG(null); }, [q.uid]);
  const W = 240, xa = 96, xb = 150, top = Math.max(CLEFS[clef].high, hiD);
  const head = (x, d, col, k) => <g key={k}>{ledgersFor(d, CLEFS[clef].low, CLEFS[clef].high).map(pp => <line key={pp} x1={x - 12} x2={x + 12} y1={dY(pp)} y2={dY(pp)} stroke={col} strokeWidth="1.4"/>)}
    <ellipse cx={x} cy={dY(d)} rx="7.4" ry="5.2" fill={col}/><ellipse cx={x} cy={dY(d)} rx="3.4" ry="2.7" transform={`rotate(-38 ${x} ${dY(d)})`} fill="#fff"/></g>;
  const tapAt = (e) => { if (locked || isDone) return; const svg = e.currentTarget.ownerSVGElement; if (!svg || !svg.getScreenCTM) return; const pt = svg.createSVGPoint(); pt.x = e.clientX; pt.y = e.clientY;
    const y = pt.matrixTransform(svg.getScreenCTM().inverse()).y, d = Math.round(30 + (100 - y) / 5); setG(Math.max(lo, Math.min(hiD, d))); };
  const miss = isDone && given.ans != null && String(given.ans) !== String(q.answer);
  const extra = (yOf, layer) => layer !== 'over' ? null : <g>
    {!paper && !isDone && g != null && head(xb, g, 'rgba(38,41,107,0.45)', 'g')}
    {isDone && miss && head(xb, +given.ans, '#c8361b', 'w')}
    {isDone && head(xb + (miss ? 30 : 0), q.answer, '#2e8a6e', 'r')}
    {!paper && !isDone && !locked && <rect x={xa + 16} y={dY(41) - 6} width={W - xa - 20} height={dY(Math.min(lo, 30)) - dY(41) + 12} fill="transparent" style={{cursor:'pointer'}} onClick={tapAt}/>}
  </g>;
  const staff = <SfStaff clef={clef} width={W} notes={[{ d: lo, x: xa }]} pad={[Math.max(14, dY(CLEFS[clef].high) - dY(top) + 14), 16]} extra={extra}/>;
  if (paper) return <div style={{maxWidth:W * 1.4,margin:'0 auto'}}>{staff}</div>;
  const nudge = (k) => setG(x => Math.max(lo, Math.min(hiD, (x == null ? lo : x) + k)));
  return <div>
    <div style={{maxWidth:W * 1.25,margin:'0 auto',background:pixel ? '#fff' : 'transparent',borderRadius:pixel ? 0 : 8}}>{staff}</div>
    {!isDone && !locked && <div style={{display:'flex',gap:8,justifyContent:'center',margin:'8px 0 0'}}>
      <button className={pixel ? 'pixel-choice' : 'choice-btn'} style={{minWidth:52,minHeight:48,fontSize:20}} aria-label={t('Up', '위로')} onClick={() => nudge(1)}>▲</button>
      <button className={pixel ? 'pixel-choice' : 'choice-btn'} style={{minWidth:52,minHeight:48,fontSize:20}} aria-label={t('Down', '아래로')} onClick={() => nudge(-1)}>▼</button>
      <button className={pixel ? 'pixel-choice' : 'choice-btn'} style={{minWidth:96,minHeight:48,fontWeight:900}} disabled={g == null} onClick={() => g != null && onAnswer(g)}>{t('Check', '확인')}</button>
    </div>}
    {!isDone && !locked && <div style={{textAlign:'center',fontSize:13,fontWeight:700,margin:'6px 0 0',minHeight:18,color:pixel ? '#faf6ec' : 'rgba(38,41,107,0.72)'}}>{g == null ? t('Tap the staff, or use ▲ ▼.', '오선을 누르거나 ▲ ▼로 옮겨요.') : ''}</div>}
  </div>;
}
function IvxQuestion({ q, given, locked, onAnswer, pixel }) {
  const paper = locked && !given;   // the printed worksheet
  const board = useBoard(q, given), isDone = !!given, btnCls = pixel ? 'pixel-choice' : 'choice-btn';
  const ink = pixel ? '#faf6ec' : 'var(--text)', box = { background: pixel ? '#fff' : 'transparent', borderRadius: pixel ? 0 : 8 };
  const st = (c) => !isDone ? '' : (String(c) === String(q.answer) ? ' good' : (String(given.ans) === String(c) ? ' bad' : ''));
  useEffect(() => { if (q.kind === 'ear' && !locked) { const tm = setTimeout(() => ivxPlay(q.p), 350); return () => { clearTimeout(tm); stopClicks(); }; } }, [q.uid]);
  const above = (q.n === 8 ? t('an octave', '옥타브') : t('a ' + ivxEn(q.n || 2), ivxShort(q.n || 2)));
  const prompt = { count: t('How many? Count both notes.', '몇 도일까요? 두 음 모두 세요.'), hand: t('Thumb and which finger? Name the interval.', '엄지와 몇 번 손가락? 몇 도일까요?'),
    write: t((paper ? 'Draw' : 'Write') + ' the note ' + above + ' above ' + (q.a ? dName(q.a.d) : '') + '.', (q.a ? dName(q.a.d) : '') + '에서 ' + above + ' 위의 음을 ' + (paper ? '그려요.' : '써요.')),
    mh: t('Melodic or harmonic?', '선율적일까요, 화성적일까요?'), ear: t('Listen: which interval?', '듣고 골라요: 몇 도?'),
    tonic: t('The interval above the tonic?', '으뜸음 위의 음정은?'), mp: t((q.n === 8 ? 'An octave' : 'A ' + ivxEn(q.n || 2)) + ' above the tonic: major or perfect?', '으뜸음 위 ' + ivxShort(q.n || 2) + ': 장음정? 완전음정?') }[q.kind];
  const head = (q.kind === 'tonic' || q.kind === 'mp') && <div style={{textAlign:'center',fontFamily:LB_SERIF,fontSize:pixel ? 14 : 22,fontWeight:900,color:pixel ? '#faf6ec' : 'var(--navy)',margin:'0 0 2px'}}>{sscSx(skgKeyName(q.k))}</div>;
  let pic = null;
  if (q.kind === 'write') {
    pic = <IvxWrite q={q} given={given} locked={locked} onAnswer={onAnswer} pixel={pixel} paper={paper}/>;
  } else if (q.kind === 'hand') {
    pic = <div style={{maxWidth:240,margin:'0 auto',...box}}><IvxKeys d0={q.pos} n={5} nums={IVX_SCALE_N(q.pos)} numCol={PEN_N} o={{ H: 110, lit: [ivMidi(q.p.a)], pale: [ivMidi(q.p.b)] }}/></div>;
  } else if (q.kind === 'ear') {
    pic = <div style={{textAlign:'center',margin:'4px 0 6px'}}><button className="ghost-btn" style={{minHeight:44}} onClick={() => ivxPlay(q.p)}>{t('▶ Listen again', '▶ 다시 듣기')}</button>
      {isDone && <div style={{maxWidth:240,margin:'8px auto 0',background:pixel ? '#fff' : 'transparent',borderRadius:pixel ? 0 : 8}}><IvxStaff pairs={[q.p]} width={240} o={{ x0: 64 }}/></div>}</div>;
  } else {
    const kk = q.kind === 'tonic' || q.kind === 'mp' ? q.k : null;
    pic = <div style={{maxWidth:260,margin:'0 auto',...box}}><IvxStaff clef={q.clef || 'treble'} pairs={[{ ...q.p, ladder: isDone && q.kind !== 'mh' && q.kind !== 'mp' }]} width={260} o={{ x0: 66, key: kk }}/></div>;
  }
  const cols = q.kind === 'write' ? 0 : q.choices.length === 2 ? 2 : 4;
  return <div>{!paper && <BoardTrack b={board} pixel={pixel}/>}
    {head}
    <p style={{fontSize:pixel ? 11.5 : 17,fontWeight:900,textAlign:'center',margin:'0 0 8px',color:ink,textWrap:'balance',wordBreak:'keep-all'}}>{prompt}</p>
    <div style={{margin:'0 auto 10px'}}>{pic}</div>
    {cols > 0 && <div style={{display:'grid',gridTemplateColumns:'repeat(' + cols + ',minmax(0,1fr))',gap:8}}>{q.choices.map(c => <button key={c} disabled={locked} onClick={() => { if (q.kind === 'ear') stopClicks(); onAnswer(c); }} className={btnCls + st(c)} style={{padding:'12px 4px',minHeight:44}}><span style={{fontSize:pixel ? 11 : 18,fontWeight:900}}>{sscSx(ivxChoiceTxt(q, c))}</span></button>)}</div>}
  </div>;
}
