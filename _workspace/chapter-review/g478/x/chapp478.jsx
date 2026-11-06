// ─── Phase 478: chapter 22's pads (pages 1 to 6), the screen lesson and the drill ───
const CHX_W = 300;   // a pad's staff width on a phone
// the sound: a triad broken (root up), then together; held notes are let go when another starts
let _chxRel = [];
const chxStop = () => { stopClicks(); _chxRel.forEach(r => { try { if (typeof r === 'function') r(); } catch (e) {} }); _chxRel = []; };
function chxPlay(notes, mode = 'both') {
  chxStop(); const ctx = getAudio(); if (!ctx) return;
  const t0 = ctx.currentTime + 0.05, go = (t, n, len, vol) => _chxRel.push(blip(ctx, t, ivFreq(n), len, vol, 'triangle'));
  if (mode !== 'block') notes.forEach((n, i) => go(t0 + i * 0.32, n, 0.55, 0.15));
  if (mode !== 'arp') { const b = mode === 'block' ? t0 : t0 + notes.length * 0.32 + 0.12; notes.forEach(n => go(b, n, 1.3, 0.11)); }
}
// chords one after the other (I IV V I), each together
function chxPlayRow(rows, gap = 0.9) {
  chxStop(); const ctx = getAudio(); if (!ctx) return;
  const t0 = ctx.currentTime + 0.05;
  rows.forEach((notes, i) => notes.forEach(n => _chxRel.push(blip(ctx, t0 + i * gap, ivFreq(n), gap * 0.95, 0.11, 'triangle'))));
}
const chxMsg = (msg, bad) => <div style={{textAlign:'center',fontSize:15,fontWeight:900,color:bad ? BK.coral : BK.ink,minHeight:22,margin:'6px 0',textWrap:'balance',wordBreak:'keep-all'}}>{sscSx(chxKoT(msg))}</div>;
const chxChips = (list, on, set, lab = (x) => sscSx(prettyNote(x))) => <div style={{display:'flex',gap:6,justifyContent:'center',flexWrap:'wrap',margin:'0 auto 6px',maxWidth:list.length === 7 ? 242 : list.length === 5 ? 180 : undefined}}>{list.map(x => <button key={x} className={'chip' + (x === on ? ' active' : '')} style={{minHeight:44,minWidth:44,justifyContent:'center',fontWeight:900}} onClick={() => set(x)}>{lab(x)}</button>)}</div>;
const chxRow = (kids) => <div style={{display:'flex',gap:6,justifyContent:'center',flexWrap:'wrap'}}>{kids}</div>;
const chxBtn = (key, w, on, act) => <button key={key} className={'ghost-btn' + (act ? ' active' : '')} style={{minHeight:44}} onClick={on}>{w}</button>;
// o.third: the 3rd coral (page 3: what moves), else the root
const chxKeysFor = (notes, o = {}) => { const [d0, nk] = chxKeyRange(notes), c = o.third ? 1 : 0; return <div style={{maxWidth:nk * 46,margin:'6px auto 0'}}><ChxKeys d0={d0} n={nk} o={{ H: o.H || 100, lit: [ivMidi(notes[c])], pale: notes.filter((_, j) => j !== c).map(ivMidi), nums: o.nums }} onTap={(m) => sacKey(m)}/></div>; };
const chxSum = (q) => q === 'minor' ? '3 + 4' : '4 + 3';
const chxWhiteQ = (r) => 'CFG'.includes(r) ? 'major' : 'DEA'.includes(r) ? 'minor' : 'diminished';

// page 1: the chord clock: tap a key, the triangle turns to it; major or minor; the triad on the staff under it
function ChxClockPad() {
  const [at, setAt] = useState(0), [q, setQ] = useState('major');
  useEffect(() => () => chxStop(), []);
  const root = chxRoot12(at, q), names = chxSpell(root, q), nt = chxNotes(root, q);
  const go = (i, qq = q) => { setAt(i); const r = chxRoot12(i, qq); chxPlay(chxNotes(r, qq)); };
  return (
    <div className="try-box" style={actBox} data-chx="pad-clock">
      <div style={actTitle}>{t('The chord clock', '화음 시계')}</div>
      <div style={{...actNote,textWrap:'pretty'}}>{chxKoT(t('Tap any key: the triangle moves there and the triad sounds. The same shape on every key.', '아무 건반이나 누르면 삼각형이 그리로 옮겨 가고 3화음이 울려요. 어느 건반에서나 같은 모양이에요.'))}</div>
      {chxChips(['major', 'minor'], q, (x) => { setQ(x); go(at, x); }, (x) => chxQ(x))}
      <div style={{maxWidth:300,margin:'0 auto'}}><ChxRing at={at} q={q} onPick={(i) => go(i)} label={t('The chord clock: ' + chxName(root, q) + ', ' + chxTxt(names) + '.', '화음 시계: ' + chxName(root, q) + ', ' + chxTxt(names) + '.')}/></div>
      <div style={{maxWidth:250,margin:'4px auto 0'}}><ChxStaff places={[{ notes: nt, side: chxSide() }]} width={170} o={{ x0: 54, padTop: 18, sideSize: 13 }}/></div>
      {chxMsg(t(chxName(root, q) + ': ' + chxTxt(names) + '. ' + (q === 'minor' ? '3 half steps, then 4.' : '4 half steps, then 3.'), chxName(root, q) + ': ' + chxTxt(names) + '. ' + (q === 'minor' ? '반 걸음 3개, 그다음 4개.' : '반 걸음 4개, 그다음 3개.')))}
      <div style={{display:'flex',justifyContent:'center'}}>{chxBtn('p', t('▶ Listen', '▶ 듣기'), () => chxPlay(nt))}</div>
    </div>
  );
}
// page 2: stack a triad on any white key: root, 3rd, 5th on the staff and the keys
function ChxStackPad() {
  const [r, setR] = useState('D');
  useEffect(() => () => chxStop(), []);
  const white = (x) => [0, 2, 4].map(st => IVX_N(CHX_D[x] + st)), nt = white(r), onL = chxOnLines(nt);
  const pickR = (x) => { setR(x); chxPlay(white(x)); };
  return (
    <div className="try-box" style={actBox} data-chx="pad-stack">
      <div style={actTitle}>{t('Stack a triad', '3화음 쌓기')}</div>
      <div style={actNote}>{chxKoT(t('Pick a root. The 3rd and the 5th stack above it on the white keys.', '근음을 골라요. 흰건반에서 3음과 5음이 그 위에 쌓여요.'))}</div>
      {chxChips(CHX_L.split(''), r, pickR)}
      <div style={{maxWidth:250,margin:'0 auto'}}><ChxStaff places={[{ notes: nt, side: chxSide() }]} width={170} o={{ x0: 54, sideSize: 13 }} label={t('The triad on ' + r + ': ' + chxNotesTxt(nt) + '.', r + ' 위의 3화음: ' + chxNotesTxt(nt) + '.')}/></div>
      {chxKeysFor(nt)}
      {chxMsg(t(chxNotesTxt(nt) + ': skip a letter, skip a letter. All ' + (onL ? 'on lines' : 'in spaces') + '.', chxNotesTxt(nt) + ': 하나 건너, 하나 건너. 모두 ' + (onL ? '줄' : '칸') + '에 있어요.'))}
      <div style={{display:'flex',justifyContent:'center'}}>{chxBtn('p', t('▶ Listen', '▶ 듣기'), () => chxPlay(nt))}</div>
    </div>
  );
}
// page 3: major or minor: a root, then flip the 3rd; the half steps counted on the keys
function ChxMinorPad() {
  const [r, setR] = useState('C'), [q, setQ] = useState('major');
  useEffect(() => () => chxStop(), []);
  const nt = chxNotes(r, q), wq = chxWhiteQ(r), names = chxSpell(r, q);
  const go = (rr, qq) => { setR(rr); setQ(qq); chxPlay(chxNotes(rr, qq)); };
  const msg = t(chxName(r, q) + ': ' + chxTxt(names) + ', ' + chxSum(q) + '.' + (q === wq ? ' On the white keys, ' + r + '’s triad is ' + wq + '.' : ' The 3rd moved ' + (q === 'minor' ? 'down' : 'up') + ' a half step.'),
    chxName(r, q) + ': ' + chxTxt(names) + ', ' + chxSum(q) + '.' + (q === wq ? ' 흰건반에서 ' + r + ' 3화음은 ' + chxQ(wq) + '이에요.' : ' 3음이 반 걸음 ' + (q === 'minor' ? '내려갔어요.' : '올라갔어요.')));
  return (
    <div className="try-box" style={actBox} data-chx="pad-mm">
      <div style={actTitle}>{t('Major or minor?', '장3화음? 단3화음?')}</div>
      <div style={actNote}>{chxKoT(t('Pick a root, then major or minor. Count the half steps on the keys.', '근음을 고른 다음 장3화음이나 단3화음을 골라요. 건반에서 반 걸음을 세어요.'))}</div>
      {chxChips(['C', 'D', 'E', 'F', 'G', 'A'], r, (x) => go(x, chxWhiteQ(x)))}
      {chxChips(['major', 'minor'], q, (x) => go(r, x), (x) => chxQ(x))}
      <div style={{maxWidth:250,margin:'0 auto'}}><ChxStaff places={[{ notes: nt, hl: [1], side: chxSide() }]} width={170} o={{ x0: 54, sideSize: 13 }}/></div>
      {chxKeysFor(nt, { nums: chxCount(nt), H: 110, third: true })}
      {chxMsg(msg)}
      <div style={{display:'flex',justifyContent:'center'}}>{chxBtn('p', t('▶ Listen', '▶ 듣기'), () => chxPlay(nt))}</div>
    </div>
  );
}
// page 4: the tonic triad of a key, with its key signature
const CHX_TONIC5 = ['C', 'G', 'D', 'F', 'Bb'];
function ChxTonicPad() {
  const [k, setK] = useState('G');
  useEffect(() => () => chxStop(), []);
  const nt = chxDeg(k, 1);
  return (
    <div className="try-box" style={actBox} data-chx="pad-tonic">
      <div style={actTitle}>{t('The tonic triad', '으뜸화음')}</div>
      <div style={actNote}>{chxKoT(t('Pick a key: its tonic triad, the scale’s 1st, 3rd and 5th notes.', '조를 골라요. 그 조의 으뜸화음, 음계의 1번, 3번, 5번 음이 나와요.'))}</div>
      {chxChips(CHX_TONIC5, k, (x) => { setK(x); chxPlay(chxDeg(x, 1)); })}
      <div style={{maxWidth:CHX_W,margin:'0 auto'}}><ChxStaff places={[{ notes: nt, lab: 'I', lab2: chxNotesTxt(nt) }]} width={240} o={{ x0: 60, key: k, labSize: 15 }} label={t(skgKeyName(k) + ': the tonic triad, ' + chxNotesTxt(nt) + '.', skgKeyName(k) + '의 으뜸화음: ' + chxNotesTxt(nt) + '.')}/></div>
      {chxKeysFor(nt)}
      {chxMsg(t(skgKeyName(k) + ': the tonic triad is ' + chxNotesTxt(nt) + '.', skgKeyName(k) + '의 으뜸화음은 ' + chxNotesTxt(nt) + '.'))}
      <div style={{display:'flex',justifyContent:'center'}}>{chxBtn('p', t('▶ Listen', '▶ 듣기'), () => chxPlay(nt))}</div>
    </div>
  );
}
// page 5 and the end: I, IV and V in a key; tap one to hear it, ▶ I IV V I. end: the student's keys, else C G D F
function ChxPrimaryPad({ end }) {
  const { keys, fromTeacher } = pbKeysFor('scales'), list = end && fromTeacher ? keys : CHX_TONIC_KEYS;
  const [k, setK] = useState(end ? list[0] : 'C'), [dg, setDg] = useState(1);
  useEffect(() => () => chxStop(), []);
  const kk = pbKeyId(k) || k, nt = chxDeg(kk, dg), rootOf = (d) => prettyNote(spellScale(kk)[d - 1]);
  const pl = [1, 4, 5].map(d => ({ notes: chxDeg(kk, d), lab: CHX_ROM[d], lab2: rootOf(d), hl: d === dg ? [0, 1, 2] : [] }));
  const pick = (d) => { setDg(d); chxPlay(chxDeg(kk, d), 'block'); };
  const nAcc = skgKs(kk, 'treble').length;
  return (
    <div className="try-box" style={actBox} data-chx={end ? 'pad-mine' : 'pad-145'}>
      {!end && <div style={actTitle}>{t('I, IV and V', 'I, IV, V')}</div>}
      <div style={{...actNote,textWrap:'pretty'}}>{chxKoT(end ? (fromTeacher ? t('I, IV and V in your keys: the triads on the 1st, 4th and 5th notes. Tap one to hear it.', '나의 조의 I, IV, V: 1번, 4번, 5번 음 위의 3화음이에요. 누르면 들려요.')
          : t('I, IV and V in this chapter’s keys: the triads on the 1st, 4th and 5th notes. Tap one to hear it.', '이 챕터의 조의 I, IV, V: 1번, 4번, 5번 음 위의 3화음이에요. 누르면 들려요.'))
        : t('Pick a key, then one of I, IV and V. ▶ I IV V I plays them all in turn.', '조를 고른 다음 I, IV, V 중 하나를 골라요. ▶ I IV V I을 누르면 차례로 모두 들려요.'))}</div>
      {chxChips(list, k, (x) => { setK(x); setDg(1); chxPlay(chxDeg(pbKeyId(x) || x, 1), 'block'); }, (x) => sscSx(pbKeyName(x)))}
      <div style={{maxWidth:CHX_W + 20,margin:'0 auto'}}><ChxStaff places={pl} width={260 + 12 * Math.max(0, nAcc - 2)} o={{ x0: 58, key: kk, labSize: 18, bars: true }} label={t(skgKeyName(kk) + ': I ' + chxNotesTxt(chxDeg(kk, 1)) + ', IV ' + chxNotesTxt(chxDeg(kk, 4)) + ', V ' + chxNotesTxt(chxDeg(kk, 5)) + '.', skgKeyName(kk) + ': I ' + chxNotesTxt(chxDeg(kk, 1)) + ', IV ' + chxNotesTxt(chxDeg(kk, 4)) + ', V ' + chxNotesTxt(chxDeg(kk, 5)) + '.')}/></div>
      {chxKeysFor(nt)}
      <div style={{display:'grid',gridTemplateColumns:'repeat(3,minmax(0,1fr))',gap:6,maxWidth:300,margin:'8px auto 4px'}}>{[1, 4, 5].map(d => <button key={d} className={'chip' + (d === dg ? ' active' : '')} style={{minHeight:44,justifyContent:'center',fontWeight:900,fontFamily:LB_SERIF,fontSize:17}} onClick={() => pick(d)}>{CHX_ROM[d]}</button>)}</div>
      {chxMsg(t(CHX_ROM[dg] + ' in ' + skgKeyName(kk) + ': ' + chxNotesTxt(nt) + ', the triad on ' + rootOf(dg) + ', the ' + ['1st', '', '', '4th', '5th'][dg - 1] + ' note.', skgKeyName(kk) + '의 ' + CHX_ROM[dg] + '(' + chxRomKo(dg) + '): ' + chxNotesTxt(nt) + ', ' + dg + '번 음 ' + rootOf(dg) + ' 위의 3화음이에요.'))}
      {end && pbKeysRow(PB_DOT, fromTeacher, list)}
      <div style={{display:'flex',justifyContent:'center'}}>{chxBtn('a', '▶ I IV V I', () => chxPlayRow([1, 4, 5, 1].map(d => chxDeg(kk, d))))}</div>
    </div>
  );
}
// page 6: blocked or broken? the right hand on the treble staff, the left on the bass
const CHX_HANDS = [['C', 'treble', 0], ['F', 'bass', 1], ['G', 'treble', 1], ['C', 'bass', 0], ['F', 'treble', 0], ['G', 'bass', 1]];
function ChxHandsPad() {
  const [i, setI] = useState(0), [ans, setAns] = useState(null);
  useEffect(() => () => chxStop(), []);
  const [r, clef, br] = CHX_HANDS[i], nt = chxNotes(r, 'major', clef), right = br ? 'broken' : 'blocked', done = ans === right;
  const play = () => chxPlay(nt, br ? 'arp' : 'block');
  const pick = (c) => { setAns(c); play(); };
  const fing = clef === 'treble' ? t('right hand, fingers 1 3 5', '오른손 1 3 5번 손가락') : t('left hand, fingers 5 3 1', '왼손 5 3 1번 손가락');
  const word = (c) => c === 'broken' ? t('broken', '펼쳐서') : t('blocked', '함께');
  return (
    <div className="try-box" style={actBox} data-chx="pad-hands">
      <div style={actTitle}>{t('Blocked or broken?', '함께? 펼쳐서?')}</div>
      <div style={actNote}>{chxKoT(t('Look, pick, then listen. Which hand plays it?', '보고 고른 다음 들어요. 어느 손으로 칠까요?'))}</div>
      <div style={{maxWidth:CHX_W,margin:'0 auto'}}><ChxStaff clef={clef} places={[{ notes: nt, broken: !!br }]} width={240} o={{ x0: 66 }} label={t(chxName(r) + ' on the ' + (clef === 'bass' ? 'bass' : 'treble') + ' staff.', (clef === 'bass' ? '낮은음자리표' : '높은음자리표') + ' 오선의 ' + chxName(r) + '.')}/></div>
      {chxMsg(ans == null ? t('Together, or one after the other?', '함께? 한 음씩 차례로?') : done ? t(chxName(r) + ', ' + (br ? 'broken' : 'blocked') + ': the ' + fing + '.', chxName(r) + '을 ' + word(right) + ' 쳐요: ' + fing + '.') + ' ✓' : t('Look again: one above the other, or in a row?', '다시 봐요: 위아래로 쌓였나요, 옆으로 나란히 있나요?'), ans != null && !done)}
      <div style={{display:'grid',gridTemplateColumns:'repeat(2,minmax(0,1fr))',gap:6,maxWidth:300,margin:'0 auto 8px'}}>{['blocked', 'broken'].map(c => <button key={c} className={'chip' + (ans === c ? ' active' : '')} style={{minHeight:44,justifyContent:'center',fontWeight:900}} onClick={() => pick(c)}>{word(c)}</button>)}</div>
      {chxRow([chxBtn('l', t('▶ Listen', '▶ 듣기'), play), chxBtn('n', t('Next →', '다음 →'), () => { chxStop(); setI((i + 1) % CHX_HANDS.length); setAns(null); })])}
    </div>
  );
}

// ── the book on screen: the opener is the lesson's head, every other page a step; I IV V in my keys at the end ──
function ChxLearn({ onStart }) {
  const pages = chxLbPages(true);
  const opener = pages[0];
  return (
    <Lesson id="chords" title={bkChapterName('chords')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="chords"><div className="lb-screen lb-open" style={{display:'flex',flexDirection:'column',gap:12,margin:'0 0 8px'}}>{lbWordsFirst(opener.props.children)}</div></BkChapterCtx.Provider></LbScreenCtx.Provider>}>
      {pages.slice(1).map((pg, i) => (
        <Step key={i} title={<span>{pg.props.title}</span>} storeAs={'k' + (i + 1)}>
          <LbScreenPage page={pg}/>
        </Step>
      ))}
      <Step key="map" extra title={t('My chords', '나의 화음')} storeAs="k7"><ChxPrimaryPad end/></Step>
    </Lesson>
  );
}

// ── the drill, after page 6, in the book's order: stack it (1), the root (2), major or minor (3), write it (4),
// listening (5), the bass staff (6), tonic triads (7), I IV V in the student's keys (8); 9 extra: spell I, IV and V ──
const CHX_LEVELS = [
  { n: 1, label: 'Stack a triad: its letters', kind: 'spell', time: 9 },
  { n: 2, label: 'Name the root', kind: 'root', time: 7 },
  { n: 3, label: 'Major or minor?', kind: 'mm', time: 9 },
  { n: 4, label: 'Write it: the triad on a note', kind: 'write', time: 16 },
  { n: 5, label: 'Listen: major or minor?', kind: 'ear', time: 10, noPrint: true },
  { n: 6, label: 'The bass staff', kind: 'bass', time: 8 },
  { n: 7, label: 'Tonic triads: which key?', kind: 'tonic', time: 9 },
  { n: 8, label: 'I, IV or V, in my keys', kind: 'roman', time: 9 },
  { n: 9, label: 'Extra: spell I, IV and V', kind: 'spellR', time: 12 },
];
// ('The bass staff' keeps chapter 19's Korean, 낮은음자리표 오선)
Object.assign(LEVEL_KO, { 'Stack a triad: its letters': '3화음 쌓기: 음이름', 'Name the root': '근음 찾기', 'Major or minor?': '장3화음? 단3화음?', 'Write it: the triad on a note': '써 보기: 3화음',
  'Listen: major or minor?': '듣기: 장3화음? 단3화음?', 'Tonic triads: which key?': '으뜸화음: 어느 조?', 'I, IV or V, in my keys': '나의 조: I, IV, V?', 'Extra: spell I, IV and V': '더 해 보기: I, IV, V의 음이름' });
const CHX_MM_ROOTS = [['C', 'major'], ['D', 'major'], ['E', 'major'], ['F', 'major'], ['G', 'major'], ['A', 'major'], ['Bb', 'major'], ['Eb', 'major'],
  ['C', 'minor'], ['D', 'minor'], ['E', 'minor'], ['F', 'minor'], ['G', 'minor'], ['A', 'minor'], ['B', 'minor']];
const chxLetterRow = (L0, steps) => steps.map(s => CHX_L[(L0 + s) % 7]).join(' ');
// roots drawn from a shuffled bag, so a worksheet does not repeat one before all seven have come
const _chxBag = {};
const chxFromBag = (kind) => { let b = _chxBag[kind]; if (!b || !b.length) b = _chxBag[kind] = shuffle(CHX_L.split('')); return b.pop(); };
const chxPool = () => pbMyKeys() ? pbKeysFor('scales').keys.map(k => pbKeyId(k) || k) : CHX_TONIC_KEYS;
function genChxQuestion(lv, prev) {
  const uid = Math.random(), same = (key) => prev && prev.key === key;
  for (let g = 0; g < 40; g++) {
    if (lv.kind === 'spell') {
      const r = chxFromBag('spell'), L0 = CHX_L.indexOf(r), key = 'sp' + r;
      if (same(key)) continue;
      const answer = chxLetterRow(L0, [0, 2, 4]), wrong = shuffle([[0, 1, 2], [0, 2, 3], [0, 3, 5], [0, 2, 5], [0, 1, 4]].map(st => chxLetterRow(L0, st))).slice(0, 3);
      return { kind: 'spell', key, r, d: CHX_D[r], answer, choices: shuffle([answer, ...wrong]), uid };
    }
    if (lv.kind === 'root' || lv.kind === 'bass') {
      const clef = lv.kind === 'bass' ? 'bass' : 'treble', r = chxFromBag(lv.kind), key = lv.kind + r;
      if (same(key)) continue;
      const L0 = CHX_L.indexOf(r), nt = chxNotes(r, 'major', clef).map(n => IVX_N(n.d)), others = [2, 4, pick([1, 3, 5, 6])].map(s => CHX_L[(L0 + s) % 7]);
      return { kind: 'root', key, r, clef, notes: nt, answer: r, choices: shuffle([r, ...others]), uid };
    }
    if (lv.kind === 'mm' || lv.kind === 'ear') {
      const [r, q] = pick(CHX_MM_ROOTS), key = lv.kind + r + q;
      if (same(key)) continue;
      return { kind: lv.kind, key, r, q, notes: chxNotes(r, q), answer: q, choices: ['major', 'minor'], uid };
    }
    if (lv.kind === 'write') {
      const r = chxFromBag('write'), d = CHX_D[r], key = 'w' + r;
      if (same(key)) continue;
      return { kind: 'write', key, r, d, answer: (d + 2) + ',' + (d + 4), uid };
    }
    if (lv.kind === 'tonic') {
      const k = pick(CHX_TONIC_KEYS), key = 't' + k;   // the book's four (B♭ is a screen extra on the pad)
      if (same(key)) continue;
      const others = CHX_TONIC_KEYS.filter(x => x !== k);
      return { kind: 'tonic', key, k, notes: chxDeg(k, 1), answer: k, choices: shuffle([k, ...others]), uid };
    }
    if (lv.kind === 'roman' || lv.kind === 'spellR') {
      const k = pick(chxPool()), dg = pick([1, 4, 5]), key = lv.kind + k + dg;
      if (same(key) || !spellScale(k)) continue;
      const nt = chxDeg(k, dg);
      if (lv.kind === 'roman') return { kind: 'roman', key, k, dg, notes: nt, answer: CHX_ROM[dg], choices: ['I', 'IV', 'V'], uid };
      const right = chxNotesTxt(nt), plain = nt.map(n => dName(n.d)).join(' '), other = (x) => chxNotesTxt(chxDeg(k, x));
      const m3 = { d: nt[1].d, acc: nt[1].acc - 1 }, minor = m3.acc > -2 ? chxNotesTxt([nt[0], m3, nt[2]]) : null;   // the same triad minor (none when it would need a double flat)
      const cands = [plain, minor, other(dg === 5 ? 6 : dg + 1), other(dg > 1 ? dg - 1 : 6), ...[1, 4, 5].filter(x => x !== dg).map(other)].filter(Boolean);
      const wrong = shuffle([...new Set(cands)].filter(x => x !== right)).slice(0, 3);
      if (wrong.length < 3) continue;
      return { kind: 'spellR', key, k, dg, notes: nt, answer: right, choices: shuffle([right, ...wrong]), uid };
    }
  }
  return { kind: 'spell', key: 'f', r: 'C', d: 28, answer: 'C E G', choices: ['C E G', 'C D E', 'C F A', 'C E A'], uid };
}
const chxCheck = (q, ans) => ans != null && String(ans) === String(q.answer);
const chxChoiceTxt = (q, c) => q.kind === 'mm' || q.kind === 'ear' ? chxQ(c) : q.kind === 'tonic' ? skgKeyName(c) : c;
// a string: the game shows it in capitals
function chxAnswerLabel(q) {
  if (q.kind === 'write') { const nt = [q.d, q.d + 2, q.d + 4].map(d => dName(d)).join(' '); return t(nt + ' (the triad on ' + q.r + ')', nt + ' (' + q.r + ' 위의 3화음)'); }
  if (q.kind === 'spell') return q.answer;
  if (q.kind === 'root') return t(q.r + ' (the bottom note of ' + chxNotesTxt(q.notes) + ')', q.r + ' (' + chxNotesTxt(q.notes) + '의 맨 아래 음)');
  if (q.kind === 'mm' || q.kind === 'ear') return t(chxName(q.r, q.q) + ': ' + chxNotesTxt(q.notes) + ' (' + chxSum(q.q) + ')', chxName(q.r, q.q) + ' (' + chxNotesTxt(q.notes) + ', ' + chxSum(q.q) + ')');
  if (q.kind === 'tonic') return skgKeyName(q.k) + ': ' + chxNotesTxt(q.notes);
  return t(CHX_ROM[q.dg] + ' in ' + skgKeyName(q.k), skgKeyName(q.k) + '의 ' + CHX_ROM[q.dg]) + ': ' + chxNotesTxt(q.notes);
}
// level 4: write the triad on a note: tap a line or space above the root to add a note (tap it again to take it off), or
// ▲ ▼ to move the chosen note and + to add the second one above it; two notes, then Check. After: a wrong triad keeps its
// notes (wrong ones red) and the right triad stands beside it in green. On a worksheet: the root alone, room above.
function ChxWrite({ q, given, locked, onAnswer, pixel, paper }) {
  const [g, setG] = useState([]), [sel, setSel] = useState(null), isDone = !!given, lo = q.d, hiD = lo + 7, clef = 'treble';
  useEffect(() => { setG([]); setSel(null); }, [q.uid]);
  const W = 200, xa = 92, top = Math.max(CLEFS[clef].high, hiD);
  const head = (x, d, col, k) => <g key={k}>{ledgersFor(d, CLEFS[clef].low, CLEFS[clef].high).map(pp => <line key={pp} x1={x - 12} x2={x + 12} y1={dY(pp)} y2={dY(pp)} stroke={col} strokeWidth="1.4"/>)}
    <ellipse cx={x} cy={dY(d)} rx="7.4" ry="5.2" fill={col}/><ellipse cx={x} cy={dY(d)} rx="3.4" ry="2.7" transform={`rotate(-38 ${x} ${dY(d)})`} fill="#fff"/></g>;
  const toggle = (d) => { if (g.includes(d)) { setG(g.filter(v => v !== d)); setSel(null); } else { setG(g.length >= 2 ? [g[1], d] : [...g, d]); setSel(d); } };
  const tapAt = (e) => { if (locked || isDone) return; const svg = e.currentTarget.ownerSVGElement; if (!svg || !svg.getScreenCTM) return; const pt = svg.createSVGPoint(); pt.x = e.clientX; pt.y = e.clientY;
    const raw = Math.round(30 + (100 - pt.matrixTransform(svg.getScreenCTM().inverse()).y) / 5); if (raw <= lo) return; toggle(Math.min(hiD, raw)); };
  const cur = sel != null && g.includes(sel) ? sel : g.length ? g[g.length - 1] : null;
  const nudge = (k) => { if (cur == null) { setG([lo + 1]); setSel(lo + 1); return; } let nd = cur + k; while (g.includes(nd)) nd += k; if (nd <= lo || nd > hiD) return; setG(g.map(v => v === cur ? nd : v)); setSel(nd); };
  const add = () => { if (g.length !== 1) return; let nd = g[0] + 1; if (nd > hiD) return; setG([g[0], nd]); setSel(nd); };
  const right = String(q.answer).split(',').map(Number), mine = isDone && given.ans ? String(given.ans).split(',').map(Number) : [];
  const ok = isDone && String(given.ans) === String(q.answer);
  const side = (d, list) => { let k = 0; for (let x = d - 1; x === lo || list.includes(x); x--) k++; return (k % 2) * 15; };   // a 2nd sits beside, as in print
  const extra = (yOf, layer) => layer !== 'over' ? null : <g>
    {!paper && !isDone && g.map(d => head(xa + side(d, g), d, d === cur ? 'rgba(38,41,107,0.8)' : 'rgba(38,41,107,0.45)', 'g' + d))}
    {isDone && mine.map(d => head(xa + side(d, mine), d, right.includes(d) ? PEN_N : '#c8361b', 'm' + d))}
    {isDone && !ok && [lo, ...right].map(d => head(xa + 62, d, '#2e8a6e', 'r' + d))}
    {isDone && ok && right.map(d => head(xa, d, '#2e8a6e', 'r' + d))}
    {!paper && !isDone && !locked && <rect x={xa - 36} y={dY(hiD) - 6} width={W - xa + 28} height={dY(lo) - dY(hiD) + 12} fill="transparent" style={{cursor:'pointer'}} onClick={tapAt}/>}
  </g>;
  const staff = <SfStaff clef={clef} width={W} notes={[{ d: lo, x: xa }]} pad={[Math.max(14, dY(CLEFS[clef].high) - dY(top) + 14), 16]} extra={extra}/>;
  if (paper) return <div style={{maxWidth:W * 1.6,margin:'0 auto'}}>{staff}</div>;
  const bs = { minWidth:52, minHeight:48, fontSize:20 };
  return <div>
    <div style={{maxWidth:W * 1.6,margin:'0 auto',background:pixel ? '#fff' : 'transparent',borderRadius:pixel ? 0 : 8,touchAction:'manipulation'}}>{staff}</div>
    {!isDone && !locked && <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',margin:'8px 0 0'}}>
      <button className={pixel ? 'pixel-choice' : 'choice-btn'} style={bs} aria-label={t('Up', '위로')} onClick={() => nudge(1)}>▲</button>
      <button className={pixel ? 'pixel-choice' : 'choice-btn'} style={bs} aria-label={t('Down', '아래로')} onClick={() => nudge(-1)}>▼</button>
      <button className={pixel ? 'pixel-choice' : 'choice-btn'} style={bs} aria-label={t('Add a note', '음 하나 더')} disabled={g.length !== 1} onClick={add}>+</button>
      <button className={pixel ? 'pixel-choice' : 'choice-btn'} style={{minWidth:96,minHeight:48,fontWeight:900}} disabled={g.length !== 2} onClick={() => g.length === 2 && onAnswer([...g].sort((a, b) => a - b).join(','))}>{t('Check', '확인')}</button>
    </div>}
    {!isDone && !locked && <div style={{textAlign:'center',fontSize:13,fontWeight:700,margin:'6px 0 0',minHeight:18,color:pixel ? '#faf6ec' : 'rgba(38,41,107,0.72)'}}>{g.length < 2 ? t('Tap the staff, or use ▲ ▼ and +. Tap a note again to take it off.', '오선을 누르거나 ▲ ▼와 +로 음을 놓아요. 음을 다시 누르면 지워져요.') : ''}</div>}
  </div>;
}
function ChxQuestion({ q, given, locked, onAnswer, pixel }) {
  const paper = locked && !given;   // the printed worksheet
  const board = useBoard(q, given), isDone = !!given, btnCls = pixel ? 'pixel-choice' : 'choice-btn';
  const ink = pixel ? '#faf6ec' : 'var(--text)', box = { background: pixel ? '#fff' : 'transparent', borderRadius: pixel ? 0 : 8 };
  const st = (c) => !isDone ? '' : (String(c) === String(q.answer) ? ' good' : (String(given.ans) === String(c) ? ' bad' : ''));
  useEffect(() => { if (q.kind === 'ear' && !locked) { const tm = setTimeout(() => chxPlay(q.notes, 'block'), 350); return () => { clearTimeout(tm); chxStop(); }; } }, [q.uid]);
  const prompt = { spell: t('The triad on ' + (q.r || '') + ': which letters?', (q.r || '') + ' 위의 3화음: 어떤 음이름일까요?'), root: t('Which note is the root?', '근음은 어느 음일까요?'),
    mm: t('Major or minor?', '장3화음일까요, 단3화음일까요?'), ear: t('Listen: major or minor?', '듣고 골라요: 장3화음? 단3화음?'),
    write: t((paper ? 'Draw' : 'Write') + ' the triad on ' + (q.r || '') + '.', (q.r || '') + ' 위에 3화음을 ' + (paper ? '그려요.' : '써요.')),
    tonic: t('Whose tonic triad is it?', '어느 조의 으뜸화음일까요?'), roman: t('I, IV or V?', 'I, IV, V 가운데 무엇일까요?'),
    spellR: t((CHX_ROM[q.dg] || '') + ': which notes?', (CHX_ROM[q.dg] || '') + ': 어떤 음일까요?') }[q.kind];
  const head = (q.kind === 'roman' || q.kind === 'spellR') && <div style={{textAlign:'center',fontFamily:LB_SERIF,fontSize:pixel ? 14 : 22,fontWeight:900,color:pixel ? '#faf6ec' : 'var(--navy)',margin:'0 0 2px'}}>{sscSx(skgKeyName(q.k))}</div>;
  let pic = null;
  if (q.kind === 'write') {
    pic = <ChxWrite q={q} given={given} locked={locked} onAnswer={onAnswer} pixel={pixel} paper={paper}/>;
  } else if (q.kind === 'spell') {
    pic = <div style={{maxWidth:240,margin:'0 auto',...box}}><ChxStaff places={[{ notes: isDone ? [IVX_N(q.d), IVX_N(q.d + 2), IVX_N(q.d + 4)] : [IVX_N(q.d)] }]} width={220} o={{ x0: 64 }}/></div>;
  } else if (q.kind === 'ear') {
    pic = <div style={{textAlign:'center',margin:'4px 0 6px'}}><button className="ghost-btn" style={{minHeight:44}} onClick={() => chxPlay(q.notes, 'block')}>{t('▶ Listen again', '▶ 다시 듣기')}</button>
      {isDone && <div style={{maxWidth:240,margin:'8px auto 0',...box}}><ChxStaff places={[{ notes: q.notes, hl: [1] }]} width={220} o={{ x0: 64 }}/></div>}</div>;
  } else if (q.kind === 'spellR') {
    pic = isDone ? <div style={{maxWidth:260,margin:'0 auto',...box}}><ChxStaff places={[{ notes: q.notes }]} width={240} o={{ x0: 64, key: q.k }}/></div> : null;
  } else {
    const kk = q.kind === 'tonic' || q.kind === 'roman' ? q.k : null;
    pic = <div style={{maxWidth:260,margin:'0 auto',...box}}><ChxStaff clef={q.clef || 'treble'} places={[{ notes: q.notes, hl: isDone && q.kind === 'root' ? [0] : isDone && q.kind === 'mm' ? [1] : [] }]} width={240} o={{ x0: 64, key: kk }}/></div>;
    if (isDone && q.kind === 'mm' && !pixel) pic = <>{pic}{chxKeysFor(q.notes, { nums: chxCount(q.notes), H: 96, third: true })}</>;
  }
  const cols = q.kind === 'write' ? 0 : q.choices.length === 2 ? 2 : q.choices.length === 3 ? 3 : q.kind === 'spell' || q.kind === 'spellR' || q.kind === 'tonic' ? 2 : 4;
  return <div>{!paper && <BoardTrack b={board} pixel={pixel}/>}
    {head}
    <p style={{fontSize:pixel ? 11.5 : 17,fontWeight:900,textAlign:'center',margin:'0 0 8px',color:ink,textWrap:'balance',wordBreak:'keep-all'}}>{sscSx(prompt)}</p>
    {pic && <div style={{margin:'0 auto 10px'}}>{pic}</div>}
    {cols > 0 && <div style={{display:'grid',gridTemplateColumns:'repeat(' + cols + ',minmax(0,1fr))',gap:8}}>{q.choices.map(c => <button key={c} disabled={locked} onClick={() => { if (q.kind === 'ear') chxStop(); onAnswer(c); }} className={btnCls + st(c)} style={{padding:'12px 4px',minHeight:44}}><span style={{fontSize:pixel ? 11 : 18,fontWeight:900,fontFamily:q.kind === 'roman' ? LB_SERIF : undefined}}>{sscSx(chxChoiceTxt(q, c))}</span></button>)}</div>}
  </div>;
}
