
// ─── Phase 437: chapter 7 on screen -- what moves on each page of the book (navy and coral; a half step coral, a whole
// step navy, as on paper) ───
Object.assign(MARK_STYLE, {
  tnHalf: { white: '#fde6dd', black: '#f08a6c', stroke: '#e4572e' },
  tnWhole: { white: '#e4e5f3', black: '#6d6f9c', stroke: '#26296b' },
});
const tnName = (i) => pcLabel(((i % 12) + 12) % 12);   // 'C', 'C♯ / D♭'
const tnBtn = { padding: '4px 12px', fontSize: 13.5 };
const tnWord = (i) => PC_INFO[((i % 12) + 12) % 12].white ? tnName(i) : t('a black key', '검은건반');   // pages 2-4 come before the black keys' names
// p2: tap a key -- its half steps light up, up and down; the half-step walk from C to C
function TnHalf() {
  const N = 24;
  const [me, setMe] = useState(14);   // the Dog's D, the second octave
  const [walk, setWalk] = useState(-1);
  const timer = useRef(null);
  useEffect(() => () => clearTimeout(timer.current), []);
  const tap = (i) => { clearTimeout(timer.current); setWalk(-1); setMe(i); playKey(i); };
  const go = () => {
    clearTimeout(timer.current); setMe(null);
    const step = (k) => { setWalk(k); playKey(k, 0.3); if (k < 12) timer.current = setTimeout(() => step(k + 1), 430); };
    step(0);
  };
  const marks = {}, names = {};
  if (walk >= 0) { for (let k = 0; k < walk; k++) marks[k] = 'tnHalf'; marks[walk] = 'target'; }
  else if (me != null) { marks[me] = 'target'; [me - 1, me + 1].forEach(k => { if (k >= 0 && k < N) { marks[k] = 'tnHalf'; } }); }
  const up = me != null && me + 1 < N ? me + 1 : null, dn = me != null && me - 1 >= 0 ? me - 1 : null;
  const word = (k, side) => k == null ? '--' : PC_INFO[k % 12].white ? tnName(k) : side > 0 ? t('the black key on the right', '오른쪽 검은건반') : t('the black key on the left', '왼쪽 검은건반');
  const meWord = me == null ? '' : PC_INFO[me % 12].white ? tnName(me) : t('the black key', '검은건반');
  return (
    <div className="try-box" style={actBox}>
      <div style={actTitle}>{t('A half step: the very next key', '반 걸음: 바로 옆 건반')}</div>
      <div style={actNote}>{t('Tap a key to stand on it. Its half steps light up: the very next key up (right) and down (left), black or white.', '건반을 눌러 그 위에 서 봐요. 반 걸음이 켜져요: 바로 오른쪽(위)과 바로 왼쪽(아래) 건반, 검은건반이든 흰건반이든.')}</div>
      <TapKeyboard octaves={2} labels="white" marks={marks} names={names} onTap={tap}/>
      <div style={{textAlign:'center',fontSize:14.5,fontWeight:800,color:BK.ink,minHeight:44,margin:'8px 0 0',lineHeight:1.5}}>
        {walk >= 0 ? <>{t('The half-step walk: ', '반 걸음 걷기: 반 걸음 ')}{LANG === 'ko' ? null : <b style={{color:BK.coral}}>{walk}</b>}{LANG === 'ko' ? <><b style={{color:BK.coral}}>{walk}</b>{'개'}</> : t(walk === 1 ? ' half step' : ' half steps', '')}{walk === 12 && t(' -- C to the next C.', ', C에서 다음 C까지.')}</>
          : me != null && (LANG === 'ko' ? <><b style={{color:BK.coral}}>{meWord}</b>{'에서 반 걸음 위: '}<b style={{color:BK.coral}}>{word(up, 1)}</b>{' · 반 걸음 아래: '}<b style={{color:BK.coral}}>{word(dn, -1)}</b></>
            : <>{'From '}<b style={{color:BK.coral}}>{meWord}</b>{': a half step up is '}<b style={{color:BK.coral}}>{word(up, 1)}</b>{', a half step down is '}<b style={{color:BK.coral}}>{word(dn, -1)}</b>{'.'}</>)}
      </div>
      {llBtnRow([<button key="w" className="chip active" style={tnBtn} onClick={go}>{t('▶ The half-step walk, C to C', '▶ 반 걸음 걷기, C에서 C까지')}</button>])}
    </div>
  );
}
// p3: tap two keys -- how many half steps; two make a whole step
function TnSteps() {
  const [a, setA] = useState(0), [b, setB] = useState(2), [next, setNext] = useState('a');
  const lo = Math.min(a, b), hi = Math.max(a, b), n = hi - lo;
  const marks = { [a]: 'target', [b]: 'target' }; for (let k = lo + 1; k < hi; k++) marks[k] = n === 2 ? 'tnWhole' : 'tnHalf';
  const tap = (i) => { playKey(i); if (next === 'a') { setA(i); setNext('b'); } else { setB(i); setNext('a'); } };
  const say = n === 0 ? t('the same key', '같은 건반') : n === 1 ? t('1 half step = a semitone', '반 걸음 1개 = 반음') : n === 2 ? t('2 half steps = a whole step = a tone', '반 걸음 2개 = 온 걸음 = 온음') : t(n + ' half steps', '반 걸음 ' + n + '개');
  return (
    <div className="try-box" style={actBox}>
      <div style={actTitle}>{t('Count the half steps', '반 걸음 세기')}</div>
      <div style={actNote}>{t('Tap two keys. Count the steps, not the keys: two half steps -- one key in between -- make a whole step.', '건반 두 개를 눌러요. 건반 말고 걸음을 세요: 반 걸음 두 개 -- 사이에 건반 하나 -- 가 온 걸음이에요.')}</div>
      <TapKeyboard octaves={1} labels="white" marks={marks} onTap={tap}/>
      <div style={{textAlign:'center',fontSize:15,fontWeight:900,margin:'8px 0 0',color:BK.ink}}>{tnWord(lo)} → {tnWord(hi)}: <span style={{color:n === 2 ? BK.ink : BK.coral}}>{say}</span></div>
    </div>
  );
}
// p4: tap a white key -- the step to the next white key: whole, or half at E F and B C
function TnWhites() {
  const [a, setA] = useState(4);   // E
  const b = PC_INFO[(a + 1) % 12].white ? a + 1 : a + 2, half = b - a === 1;
  const marks = { [a]: 'target', [b]: 'target' }; if (!half) marks[a + 1] = 'tnWhole';
  const tap = (i) => { if (!PC_INFO[i % 12].white) return; const j = PC_INFO[(i + 1) % 12].white ? i + 1 : i + 2; if (j > 23) return; setA(i); playKey(i); setTimeout(() => playKey(j), 330); };
  return (
    <div className="try-box" style={actBox}>
      <div style={actTitle}>{t('White neighbours', '흰건반 이웃')}</div>
      <div style={actNote}>{t('Tap a white key: is the next white key up a whole step or a half step?', '흰건반을 눌러요: 바로 위 흰건반까지 온 걸음일까요, 반 걸음일까요?')}</div>
      <TapKeyboard octaves={2} labels="white" marks={marks} onTap={tap}/>
      <div style={{textAlign:'center',fontSize:15,fontWeight:900,margin:'8px 0 0',color:half ? BK.coral : BK.ink}}>
        {tnName(a)} → {tnName(b)}: {half ? t('a half step -- no black key between.', '반 걸음 -- 사이에 검은건반이 없어요.') : t('a whole step -- one black key between.', '온 걸음 -- 사이에 검은건반 하나.')}
      </div>
    </div>
  );
}
// p5: tap a white key and push it: the sharp up a half step, the flat down; the black key it lands on, both names.
// E and B have no black key on their right, C and F none on their left: those names wait for later (B7)
function TnSharpFlat() {
  const [from, setFrom] = useState(0);
  const [dir, setDir] = useState(1);
  const L = PC_INFO[from].names[0], to = from + dir;
  const ok = to >= 0 && to < 12 && !PC_INFO[to].white;
  const marks = { [from]: 'target' }; if (ok) marks[to] = 'tnHalf';
  const push = (d) => { setDir(d); const k = from + d; if (k >= 0 && k < 12 && !PC_INFO[k].white) { playKey(from); setTimeout(() => playKey(k), 330); } };
  const tap = (i) => { if (!PC_INFO[i].white) return; setFrom(i); playKey(i); };
  const name = L + (dir > 0 ? '#' : 'b');
  return (
    <div className="try-box" style={actBox}>
      <div style={actTitle}>{t('Sharp up, flat down', '샤프는 위로, 플랫은 아래로')}</div>
      <div style={actNote}>{t('Tap a white key, then tap ♯ up or ♭ down: the sharp moves it a half step up, the flat a half step down.', '흰건반을 누르고 ♯ 위로 또는 ♭ 아래로를 눌러요: 샤프는 반 걸음 위로, 플랫은 반 걸음 아래로 옮겨요.')}</div>
      <TapKeyboard octaves={1} labels="white" marks={marks} onTap={tap}/>
      {llBtnRow([<button key="s" className={'chip' + (dir > 0 ? ' active' : '')} style={tnBtn} onClick={() => push(1)}>{tnSign('#')} {t('up', '위로')}</button>, <button key="f" className={'chip' + (dir < 0 ? ' active' : '')} style={tnBtn} onClick={() => push(-1)}>{tnSign('b')} {t('down', '아래로')}</button>])}
      <div style={{textAlign:'center',fontSize:15,fontWeight:800,minHeight:44,margin:'8px 0 0',lineHeight:1.5,color:BK.ink}}>
        {ok ? <><b style={{color:BK.coral}}>{L}{tnSign(dir > 0 ? '#' : 'b')}</b>{t(' -- a half step ' + (dir > 0 ? 'up' : 'down') + ' from ' + L + ', the black key on its ' + (dir > 0 ? 'right' : 'left') + '. Its other name: ', ' -- ' + L + '에서 반 걸음 ' + (dir > 0 ? '위' : '아래') + ', ' + (dir > 0 ? '오른쪽' : '왼쪽') + ' 검은건반이에요. 다른 이름: ')}<b>{prettyNote(PC_INFO[to].names.find(x => x !== name))}</b>.</>
          : t(L + ' has no black key on its ' + (dir > 0 ? 'right' : 'left') + ' -- try ' + (dir > 0 ? 'the other way, or another key.' : 'the other way, or another key.'), L + '의 ' + (dir > 0 ? '오른쪽' : '왼쪽') + '에는 검은건반이 없어요 -- 반대로 밀거나 다른 건반을 골라 봐요.')}
      </div>
    </div>
  );
}
// p6: the book's eight notes -- tap one: hear it, see its key
const TN_STAFF8 = [['treble', 38, '#'], ['treble', 35, '#'], ['treble', 34, 'b'], ['treble', 30, 'b'], ['bass', 24, '#'], ['bass', 23, 'b'], ['bass', 20, 'b'], ['bass', 18, '#']];
const tnDpc = (d, acc) => (([0, 2, 4, 5, 7, 9, 11][d % 7] + (acc === '#' ? 1 : acc === 'b' ? -1 : 0)) + 12) % 12;
const tnDName = (d, acc) => 'CDEFGAB'[d % 7] + (acc || '');
const tnDMidi = (d, acc) => 12 * (Math.floor(d / 7) + 1) + [0, 2, 4, 5, 7, 9, 11][d % 7] + (acc === '#' ? 1 : acc === 'b' ? -1 : 0);
function TnStaffPlay() {
  const [k, setK] = useState(0);
  const [clef, d, acc] = TN_STAFF8[k], list = TN_STAFF8.map((x, i) => [...x, i]).filter(x => x[0] === clef);
  const xs = [96, 168, 240, 312];
  const pick = (i) => { setK(i); const [, dd, aa] = TN_STAFF8[i]; playKey(tnDMidi(dd, aa) - 60, 0.4); };
  return (
    <div className="try-box" style={actBox}>
      <div style={actTitle}>{t('Read the sign, play the key', '기호를 읽고, 건반을 쳐요')}</div>
      <div style={actNote}>{t('Tap a note: hear it and see its key. The sign sits just before the note, on its own line or space.', '음표를 눌러요: 소리를 듣고 건반을 봐요. 기호는 음표 바로 앞, 그 음의 줄이나 칸에 있어요.')}</div>
      <div style={{display:'flex',gap:5,justifyContent:'center',margin:'0 0 6px'}}>{[['treble', t('Queensland', '퀸즈랜드')], ['bass', t('Kingsland', '킹스랜드')]].map(([c, nm]) => <button key={c} className={'chip' + (c === clef ? ' active' : '')} style={tnBtn} onClick={() => pick(TN_STAFF8.findIndex(x => x[0] === c))}>{nm}</button>)}</div>
      <div style={{maxWidth:420,margin:'0 auto'}}>
        <SfStaff clef={clef} width={360} span={[4, 356]} pad={[26, 22]} label={t('Four notes with sharps and flats', '샤프와 플랫이 붙은 네 음')}
          notes={list.map(([, dd, , i], j) => ({ d: dd, x: xs[j], color: i === k ? BK.coral : BK.ink }))}
          extra={(yOf, layer) => layer === 'over' && <g>
            {list.map(([, dd, aa, i], j) => <g key={i}>{tnAcc(aa, xs[j] - 19, yOf(dd), i === k ? BK.coral : BK.ink)}<rect x={xs[j] - 30} y={yOf(dd) - 24} width="46" height="48" fill="transparent" style={{cursor:'pointer'}} onClick={() => pick(i)}/></g>)}
          </g>}/>
      </div>
      <div style={{textAlign:'center',fontSize:15,fontWeight:900,margin:'4px 0 6px',color:BK.coral}}>{prettyNote(tnDName(d, acc))}</div>
      <TapKeyboard octaves={2} labels="white" marks={{ [tnDpc(d, acc) + 12]: 'target' }} onTap={(i) => playKey(i)}/>
    </div>
  );
}

// the book on screen: the opener is the lesson's head, every other page a step (the old three steps' ticks kept:
// half steps under 'semitones and tones', sharp and flat under 'accidentals')
const TN_STORE = [0, 3, 4, 1, 5, 6];
function TnLearn({ onStart }) {
  const pages = tnLbPages(true);
  const opener = pages[0];
  return (
    <Lesson id="tones" title={t('Tones & Semitones', '온음과 반음')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="tones"><div className="lb-screen lb-open" style={{display:'flex',flexDirection:'column',gap:12,margin:'0 0 8px'}}>{lbWordsFirst(opener.props.children)}</div></BkChapterCtx.Provider></LbScreenCtx.Provider>}>
      {pages.slice(1).map((pg, i) => (
        <Step key={i} storeAs={TN_STORE[i]} title={pg.props.title}>
          <LbScreenPage page={pg}/>
        </Step>
      ))}
    </Lesson>
  );
}

// ─── the drill (B9): one idea a level; either name of a step is right ───
const TN_BLACK = [1, 3, 6, 8, 10];
const TN_LEVELS = [
  { n: 1, label: 'Half step or whole step?', kind: 'hw', time: 7 },
  { n: 2, label: 'Play a half step, up or down', kind: 'find', size: 1, time: 9 },
  { n: 3, label: 'Play a whole step, up or down', kind: 'find', size: 2, time: 9 },
  { n: 4, label: 'White neighbours: E F and B C', kind: 'wn', time: 7 },
  { n: 5, label: 'Name the black keys', kind: 'bname', time: 7 },
  { n: 6, label: 'One key, two names', kind: 'enh', time: 8 },
  { n: 7, label: 'Sharps and flats on the staff', kind: 'staff', time: 10 },
];
Object.assign(LEVEL_KO, {
  'Half step or whole step?': '반 걸음일까, 온 걸음일까?', 'Play a half step, up or down': '반 걸음 치기, 위나 아래로', 'Play a whole step, up or down': '온 걸음 치기, 위나 아래로',
  'White neighbours: E F and B C': '흰건반 이웃: E F와 B C', 'Name the black keys': '검은건반 이름', 'One key, two names': '건반 하나, 이름 둘', 'Sharps and flats on the staff': '오선 위의 샤프와 플랫',
});
function genTnQuestion(lv, prev) {
  const uid = Math.random(), again = (q) => prev && prev.key === q.key;
  for (let g = 0; g < 20; g++) {
    let q;
    if (lv.kind === 'hw') { const size = Math.random() < 0.5 ? 1 : 2, a = 2 + Math.floor(Math.random() * 18); q = { kind: 'hw', a, b: a + size, answer: size === 1 ? 'half' : 'whole', key: 'hw' + a + ':' + size }; }
    else if (lv.kind === 'find') { const a = 7 + Math.floor(Math.random() * 11), up = Math.random() < 0.5; q = { kind: 'find', a, size: lv.size, up, target: a + (up ? lv.size : -lv.size), key: 'f' + a + up }; }
    else if (lv.kind === 'wn') { const WH = [0, 2, 4, 5, 7, 9, 11, 12], j = Math.random() < 0.5 ? pick([2, 6]) : pick([0, 1, 3, 4, 5]); q = { kind: 'wn', a: WH[j], b: WH[j + 1], answer: WH[j + 1] - WH[j] === 1 ? 'half' : 'whole', key: 'wn' + j }; }
    else if (lv.kind === 'bname') {
      const pc = pick(TN_BLACK), si = Math.random() < 0.5 ? 0 : 1, answer = PC_INFO[pc].names[si];
      const others = sampleN(TN_BLACK.filter(p => p !== pc).map(p => PC_INFO[p].names[si]), 3);   // the same sign: the sign alone gives nothing away
      q = { kind: 'bname', pc, a: pc, answer, choices: shuffle([answer, ...others]), key: 'b' + pc + answer };
    } else if (lv.kind === 'enh') {
      const pc = pick(TN_BLACK), [s, f] = PC_INFO[pc].names, flip = Math.random() < 0.5, shown = flip ? f : s, answer = flip ? s : f;
      const others = sampleN(TN_BLACK.filter(p => p !== pc).map(p => PC_INFO[p].names[flip ? 0 : 1]), 3);
      q = { kind: 'enh', shown, answer, choices: shuffle([answer, ...others]), key: 'e' + shown };
    } else {
      const clef = Math.random() < 0.5 ? 'treble' : 'bass', lo = clef === 'treble' ? 30 : 18;
      let d, acc;
      for (let h = 0; h < 30; h++) { d = lo + Math.floor(Math.random() * 9); acc = Math.random() < 0.5 ? '#' : 'b'; if ((acc === '#' ? 'CDFGA' : 'DEGAB').includes('CDEFGAB'[d % 7])) break; }
      q = { kind: 'staff', clef, d, acc, pc: tnDpc(d, acc), key: 's' + clef + d + acc };
    }
    if (!again(q) || g === 19) return { ...q, uid };
  }
}
const tnStepName = (a) => a === 'half' ? t('a half step (a semitone)', '반 걸음 (반음)') : t('a whole step (a tone)', '온 걸음 (온음)');
const tnPlace = (clef, d) => { const c = CLEFS[clef], k = d - c.low; return k % 2 === 0 ? [t('bottom line', '맨 아랫줄'), t('second line', '둘째 줄'), t('middle line', '가운데 줄'), t('fourth line', '넷째 줄'), t('top line', '맨 윗줄')][k / 2] : [t('first space', '첫째 칸'), t('second space', '둘째 칸'), t('third space', '셋째 칸'), t('fourth space', '넷째 칸')][(k - 1) / 2]; };
function TnQuestion({ q, level, given, locked, onAnswer, pixel }) {
  const done = !!given;
  const btnCls = pixel ? 'pixel-choice' : 'choice-btn';
  const prompt = (txt) => <p style={{fontSize:15,fontWeight:700,textAlign:'center',margin:'0 0 10px',color:'var(--muted)'}}>{txt}</p>;
  const choose = (opts, cols = 2) => <div style={{display:'grid',gridTemplateColumns:'repeat(' + cols + ',1fr)',gap:8,marginTop:14}}>
    {opts.map(([v, label]) => <button key={v} disabled={locked} onClick={() => onAnswer(v)} className={btnCls + (!done ? '' : v === q.answer ? ' good' : given.ans === v ? ' bad' : '')} style={{padding:'14px 0',fontSize:16}}>{label}</button>)}</div>;
  const hw = [['half', t('Half step · semitone', '반 걸음 · 반음')], ['whole', t('Whole step · tone', '온 걸음 · 온음')]];
  if (q.kind === 'hw' || q.kind === 'wn') return (<div>
    {prompt(q.kind === 'wn' ? t('White neighbours: a half step or a whole step?', '흰건반 이웃: 반 걸음일까요, 온 걸음일까요?') : t('A half step or a whole step?', '반 걸음일까요, 온 걸음일까요?'))}
    <TapKeyboard octaves={2} labels="white" marks={{ [q.a]: 'target', [q.b]: 'target' }} pixel={pixel}/>
    {choose(hw)}
  </div>);
  if (q.kind === 'bname') return (<div>
    {prompt(t('Name the black key -- a sharp or a flat name.', '검은건반의 이름은? -- 샤프 이름이든 플랫 이름이든.'))}
    <TapKeyboard octaves={1} labels="white" marks={{ [q.a]: 'target' }} pixel={pixel}/>
    {choose(q.choices.map(c => [c, prettyNote(c)]), 4)}
  </div>);
  if (q.kind === 'enh') return (<div>
    {prompt(t('One key, two names. What is its other name?', '건반 하나, 이름 둘. 다른 이름은?'))}
    <div style={{textAlign:'center',fontSize:60,fontWeight:900,margin:'0 0 6px',color:BK.ink}}>{q.shown[0]}{tnSign(q.shown[1])}</div>
    {choose(q.choices.map(c => [c, <>{c[0]}{tnSign(c[1])}</>]))}
  </div>);
  const marks = {};
  if (q.kind === 'staff') {
    if (done) { const good = q.pc + 12; marks[good] = 'good'; if (!given.ok && given.ans != null) marks[given.ans] = 'bad'; }
    return (<div>
      {prompt(t('Read the note with its sign. Tap its key.', '기호가 붙은 음을 읽어요. 그 건반을 눌러요.'))}
      <div style={{maxWidth:300,margin:'0 auto 8px'}}>
        <SfStaff clef={q.clef} width={240} span={[4, 236]} pad={[24, 22]} label={t(prettyNote(tnDName(q.d, q.acc)), prettyNote(tnDName(q.d, q.acc)))}
          notes={[{ d: q.d, x: 150, color: done ? (given.ok ? BK.green : BK.coral) : BK.ink }]}
          extra={(yOf, layer) => layer === 'over' && tnAcc(q.acc, 131, yOf(q.d), BK.ink)}/>
      </div>
      <TapKeyboard octaves={2} labels="white" marks={marks} pixel={pixel} onTap={locked ? null : (i) => onAnswer(i)}/>
    </div>);
  }
  marks[q.a] = 'target';
  if (done) { marks[q.target] = 'good'; if (!given.ok && given.ans != null && given.ans !== q.target) marks[given.ans] = 'bad'; }
  const what = q.size === 1 ? (q.up ? t('a half step up', '반 걸음 위') : t('a half step down', '반 걸음 아래')) : (q.up ? t('a whole step up', '온 걸음 위') : t('a whole step down', '온 걸음 아래'));
  return (<div>
    {prompt(t('Tap the key ' + what + ' from ' + tnName(q.a) + '.', tnName(q.a) + '에서 ' + what + '인 건반을 눌러요.'))}
    <TapKeyboard octaves={2} labels="white" marks={marks} pixel={pixel} onTap={locked ? null : (i) => onAnswer(i)}/>
  </div>);
}
Object.assign(TONES_DRILL, {
  levels: TN_LEVELS, generate: genTnQuestion,
  check: (q, ans) => ans !== null && ans !== undefined && (q.kind === 'find' ? ans === q.target : q.kind === 'staff' ? ((ans % 12) + 12) % 12 === q.pc : ans === q.answer),
  answerLabel: (q) => q.kind === 'hw' || q.kind === 'wn' ? tnStepName(q.answer) : q.kind === 'find' ? tnName(q.target) : q.kind === 'bname' ? prettyNote(q.answer) + ' (' + tnName(q.pc) + ')'
    : q.kind === 'enh' ? prettyNote(q.shown) + ' = ' + prettyNote(q.answer) : prettyNote(tnDName(q.d, q.acc)) + ' (' + (q.clef === 'treble' ? t('Queensland, ', '퀸즈랜드, ') : t('Kingsland, ', '킹스랜드, ')) + tnPlace(q.clef, q.d) + ')',
  Question: TnQuestion, Learn: TnLearn,
});

// ─── the Workbook (B10): a set task on every page a child can do alone; English, like every Workbook ───
// A paper keyboard for this chapter. Keys: 'w3' = the white key 3 from `start`, 'b3' = the black key just right of it.
// you: the key you stand on (coral, as in the book); dots: coral dots (a worked answer); arrow: [key, +1 up / -1 down]
const TN_WL = ['C', 'D', 'E', 'F', 'G', 'A', 'B'];
function TnPKeys({ start = 'C', whites = 7, w = 34, h = 104, you = [], dots = [], labels = {}, arrow = null, rings = [], gaps = [], slots = false }) {
  const s0 = TN_WL.indexOf(start), L = (i) => TN_WL[(s0 + i) % 7];
  const hasB = (i) => 'CDFGA'.includes(L(i)) && i < whites - 1;
  const bw = w * 0.6, bh = h * 0.6, T = arrow ? 26 : 3, W = whites * w + 4;
  const cx = (k) => k[0] === 'w' ? 2 + (+k.slice(1) + 0.5) * w : 2 + (+k.slice(1) + 1) * w;
  const youW = you.filter(k => k[0] === 'w'), youB = you.filter(k => k[0] === 'b');
  return (
    <svg viewBox={`0 0 ${W} ${T + h + 4}`} style={{width:'100%',display:'block'}}>
      {arrow && (() => { const x1 = cx(arrow[0]), x2 = x1 + arrow[1] * w * (arrow[2] || 1.15), y = 19; return <g>
        <line x1={x1} y1={y} x2={x2} y2={y} stroke={BK.coral} strokeWidth="2"/><path d={`M${x2 - arrow[1] * 7} ${y - 5} L${x2} ${y} L${x2 - arrow[1] * 7} ${y + 5}`} fill="none" stroke={BK.coral} strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
        <text x={(x1 + x2) / 2} y={y - 6} textAnchor="middle" fontSize="11" fontWeight="900" fill={BK.coral}>{arrow[1] > 0 ? 'up' : 'down'}</text></g>; })()}
      {Array.from({ length: whites }, (_, i) => <g key={i}>
        <rect x={2 + i * w} y={T} width={w} height={h} rx="3" fill={youW.includes('w' + i) ? '#fbd9cc' : '#fff'} stroke={BK.ink} strokeWidth="1.3"/>
        {labels['w' + i] && <text x={2 + (i + 0.5) * w} y={T + h - 10} textAnchor="middle" fontSize={w * 0.42} fontWeight="900" fill={youW.includes('w' + i) ? BK.coral : BK.ink}>{labels['w' + i]}</text>}
      </g>)}
      {Array.from({ length: whites }, (_, i) => hasB(i) && <rect key={'b' + i} x={2 + (i + 1) * w - bw / 2} y={T} width={bw} height={bh} rx="2" fill={youB.includes('b' + i) ? BK.coral : BK.ink}/>)}
      {slots && Array.from({ length: whites }, (_, i) => hasB(i) && !youB.includes('b' + i) && !dots.includes('b' + i) && <circle key={'s' + i} cx={2 + (i + 1) * w} cy={T + bh - 11} r={w * 0.15} fill="#fff"/>)}
      {Object.entries(labels).filter(([k]) => k[0] === 'b').map(([k, v]) => <text key={k} x={cx(k)} y={T - 4} textAnchor="middle" fontSize="11" fontWeight="900" fill={BK.ink}>{v}</text>)}
      {dots.map(k => k[0] === 'w' ? <circle key={k} cx={cx(k)} cy={T + h - (labels[k] ? 34 : 18)} r={w * 0.17} fill={BK.coral}/> : <circle key={k} cx={cx(k)} cy={T + bh - 11} r={w * 0.15} fill={BK.coral} stroke="#fff" strokeWidth="1.5"/>)}
      {rings.map(([a, b], j) => { const x1 = cx(a) - w * 0.5, x2 = cx(b) + w * 0.5; return <ellipse key={j} cx={(x1 + x2) / 2} cy={T + h * 0.78} rx={(x2 - x1) / 2 + 2} ry={h * 0.2} fill="none" stroke={BK.coral} strokeWidth="2"/>; })}
      {gaps.map(([i, txt]) => <text key={'g' + i} x={2 + (i + 1) * w} y={T + h + 1} textAnchor="middle" fontSize="11" fontWeight="900" fill={BK.coral}>{txt}</text>)}
    </svg>
  );
}
// a staff for this chapter's Workbook: notes at set places, a sign drawn before each (or not yet), boxes or labels under
function TnPStaff({ clef, notes, width = 300, items = [], minSpan, boxW = 46, boxH = 34 }) {
  const pct = (x) => (x / width * 100) + '%';
  const ds = notes.map(n => n.d), lo = Math.min(...ds, CLEFS[clef].low) - 2, hi = Math.max(...ds, CLEFS[clef].high) + 2;
  return <div style={{width:'100%'}}>
    <SfStaff clef={clef} width={width} span={[4, width - 4]} pad={[16, 14]} notes={notes.map(n => ({ d: n.d, x: n.x, color: n.color }))}
      extra={(yOf, layer) => layer === 'over' && <g>{notes.filter(n => n.acc).map((n, i) => <g key={i}>{tnAcc(n.acc, n.x - 19, yOf(n.d), n.accC || BK.ink)}</g>)}</g>}/>
    {items.length > 0 && <div style={{position:'relative',height:boxH + 6,marginTop:4}}>{items.map((it, i) => it.label != null
      ? <span key={i} style={{position:'absolute',left:pct(it.x),transform:'translateX(-50%)',top:4,fontSize:13,fontWeight:900,color:it.ex ? BK.coral : BK.ink,whiteSpace:'nowrap',background:BK.soft,borderRadius:12,padding:'3px 10px'}}>{it.label}</span>
      : <span key={i} style={{position:'absolute',left:pct(it.x),transform:'translateX(-50%)',top:0,width:boxW,height:boxH,border:'1.5px solid ' + (it.ex ? BK.coral : BK.ink),borderRadius:3,background:it.ex ? '#fdf3ef' : '#fff',display:'flex',alignItems:'center',justifyContent:'center',fontSize:18,fontWeight:900,fontStyle:'italic',color:BK.coral}}>
          {!it.ex && it.n != null && <span style={{...SF_NUM,position:'absolute',left:3,top:2}}>{it.n}</span>}{it.ex ? it.ans : null}</span>)}</div>}
  </div>;
}
function TnBoxRow({ whites, w, idx, ex = {}, nos = {}, bw = 40, bh = 36 }) {
  const W = whites * w + 4;
  return <div style={{position:'relative',height:bh + 4,marginTop:4}}>{idx.map(i => <span key={i} style={{position:'absolute',left:((i + 0.5) * w + 2) / W * 100 + '%',transform:'translateX(-50%)',top:0,width:bw,height:bh,border:'1.5px solid ' + (ex[i] ? BK.coral : BK.ink),borderRadius:3,background:ex[i] ? '#fdf3ef' : '#fff',display:'flex',alignItems:'center',justifyContent:'center',fontSize:19,fontWeight:900,fontStyle:'italic',color:BK.coral}}>
    {ex[i] || null}{!ex[i] && nos[i] != null && <span style={{...SF_NUM,position:'absolute',left:3,top:2}}>{nos[i]}</span>}</span>)}</div>;
}
const tnSignTxt = (nm) => <>{nm[0]}{nm[1] ? tnSign(nm[1]) : null}</>;
// a write-in: letter boxes with the sign printed after, e.g. [ ]♯ = [ ]♭ (ex: the letters written in coral)
const tnWrite = (sign, ex) => <span style={{display:'inline-flex',alignItems:'center',gap:2}}><span style={{width:34,height:34,border:'1.5px solid ' + (ex ? BK.coral : BK.ink),borderRadius:3,background:ex ? '#fdf3ef' : '#fff',display:'inline-flex',alignItems:'center',justifyContent:'center',fontSize:18,fontWeight:900,fontStyle:'italic',color:BK.coral}}>{ex || ''}</span><span style={{fontSize:16,color:BK.ink}}>{tnSign(sign)}</span></span>;

// the Workbook's tasks, fixed so the Teacher copy always matches. A key is [white index from C, +1 for the black key after it]
// on the C-to-B keyboard: 'w0' C ... 'w6' B; 'b0' C♯/D♭, 'b1' D♯/E♭, 'b3' F♯/G♭, 'b4' G♯/A♭, 'b5' A♯/B♭
const TN_PC = { w0: 0, b0: 1, w1: 2, b1: 3, w2: 4, w3: 5, b3: 6, w4: 7, b4: 8, w5: 9, b5: 10, w6: 11, w7: 12 };
const TN_KEY = Object.fromEntries(Object.entries(TN_PC).map(([k, v]) => [v, k]));
const tnKeyName = (k) => tnName(TN_PC[k]);
const tnStep = (k, n) => TN_KEY[TN_PC[k] + n];
const TN_WB = {
  halfUp: ['w0', 'w2', 'b3', 'w5'], halfDown: ['w1', 'w3', 'b5', 'w4'],
  count: [['w0', 'w2'], ['w2', 'w4'], ['w3', 'w5'], ['w1', 'w3']],
  wholeUp: ['w0', 'w3', 'w2', 'b4'], upDown: [['w1', -1], ['w4', 1], ['w6', -1], ['w3', -1]],
  pairs: [['w0', 'w1'], ['w2', 'w3'], ['b3', 'b4'], ['b1', 'w2']],
  names: ['b0', 'b1', 'b3', 'b4', 'b5'], push: [['F', '#'], ['B', 'b'], ['D', '#'], ['A', 'b']],
  same: [['C#', 'Db'], ['F#', 'Ab'], ['Eb', 'D#'], ['G#', 'Bb'], ['Gb', 'F#'], ['A#', 'Bb'], ['D#', 'Db'], ['Ab', 'G#']],
  draw: [[38, '#'], [34, 'b'], [35, '#'], [30, 'b']],
  read: { tre: [[36, 'b'], [31, '#'], [37, 'b'], [33, '#']], bas: [[24, '#'], [22, 'b'], [19, 'b'], [25, '#']] },
  colour: [['treble', 31, '#'], ['treble', 37, 'b'], ['bass', 21, '#'], ['bass', 22, '#']],
};
const tnPcOf = (nm) => PC_INFO.findIndex(p => p.names.includes(nm));
const tnSamePc = (x, y) => tnPcOf(x) === tnPcOf(y);
const tnPairStep = ([a, b]) => TN_PC[b] - TN_PC[a] === 1 ? 'half' : 'whole';
function TnWorkbook({ startNo = 1 }) {
  const W = TN_WB, pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + 1 + pages.length} chId="tones">{content}</WbPage>);
  const keyCell = (n, ex, props, under, big) => <ExCell key={n} n={n} ex={ex}><div style={{padding:big ? '14px 10px 4px' : '14px 2px 3px'}}><TnPKeys whites={7} w={big ? 36 : 30} h={big ? 64 : 72} slots={big} {...props}/>{under}</div></ExCell>;
  const xs4 = (w) => sfXs(4, w, true);

  // 2 (faces "A half step: a semitone")
  P(<>
    <WbTop step={1}/>
    <Part kind="together" title="A half step up" how="Your key is in coral. Mark the key a half step up -- the very next key on the right: a dot on a white key, or fill in the circle on a black key.">
      <BkGrid cols={2} gap="8px 10px">{W.halfUp.map((k, i) => keyCell(i + 1, i === 0, { you: [k], arrow: [k, 1], dots: i === 0 ? [tnStep(k, 1)] : [] }, null, true))}</BkGrid>
    </Part>
    <Part kind="home" title="A half step down" how="Mark the key a half step down: the very next key on the left.">
      <BkGrid cols={2} gap="8px 10px">{W.halfDown.map((k, i) => keyCell(i + 5, false, { you: [k], arrow: [k, -1] }, null, true))}</BkGrid>
    </Part>
    <Part kind="play" title="Count the half steps" how="How many half steps from one coral key to the other? Count the steps, not the keys, and write the number.">
      <BkGrid cols={4} gap="8px 8px">{W.count.map(([a, b], i) => keyCell(i + 9, i === 0, { you: [a, b] }, <div style={{display:'flex',justifyContent:'center',marginTop:4}}>{nvBox(i === 0, String(TN_PC[b] - TN_PC[a]), 40, 34)}</div>))}</BkGrid>
    </Part>
    <Faces/>
  </>);

  // 3 (faces "A whole step: a tone")
  P(<>
    <WbTop step={2}/>
    <Part kind="together" title="A whole step up" how="Mark the key a whole step up -- two half steps, one key in between: a dot on a white key, or fill in the circle on a black key.">
      <BkGrid cols={2} gap="8px 10px">{W.wholeUp.map((k, i) => keyCell(i + 1, i === 0, { you: [k], arrow: [k, 1, 2.1], dots: i === 0 ? [tnStep(k, 2)] : [] }, null, true))}</BkGrid>
    </Part>
    <Part kind="home" title="Up or down?" how="Go a whole step the way the arrow says, and mark that key.">
      <BkGrid cols={2} gap="8px 10px">{W.upDown.map(([k, dir], i) => keyCell(i + 5, false, { you: [k], arrow: [k, dir, 2.1] }, null, true))}</BkGrid>
    </Part>
    <Part kind="play" title="Half or whole?" how="The two coral keys: a half step or a whole step apart? Circle one.">
      <BkGrid cols={4} gap="8px 8px">{W.pairs.map((pr, i) => <ExCell key={i} n={i + 9} ex={i === 0}><div style={{padding:'14px 2px 3px'}}>
        <TnPKeys whites={8} w={26} h={72} you={pr}/>
        <div style={{display:'flex',justifyContent:'center',marginTop:4}}>{wsChoose(['half', 'whole'], i === 0 ? tnPairStep(pr) : null)}</div></div></ExCell>)}</BkGrid>
    </Part>
    <Faces/>
  </>);

  // 4 (faces "White half steps: E F and B C")
  const hwRow = (start, ex) => { const S0 = TN_WL.indexOf(start), steps = Array.from({ length: 7 }, (_, i) => ['E', 'B'].includes(TN_WL[(S0 + i) % 7]) ? 'H' : 'W');
    return <div><TnPKeys start={start} whites={8} w={44} h={74} labels={Object.fromEntries(Array.from({ length: 8 }, (_, i) => ['w' + i, TN_WL[(S0 + i) % 7]]))}/>
      <TnBoxRow whites={8} w={44} idx={[0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5]} ex={ex ? { 0.5: steps[0] } : {}} nos={Object.fromEntries([0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5].map((x, j) => [x, (ex ? 1 : 8) + j]))}/>
    </div>; };
  P(<>
    <WbTop step={3}/>
    <Part kind="together" title="H or W, from C to C" how="Under each pair of white neighbours, write H for a half step or W for a whole step. Look for the black key between them.">
      {hwRow('C', true)}
    </Part>
    <Part kind="home" title="H or W, from A to A" how="The same from A up to A: H or W under each pair.">
      {hwRow('A', false)}
    </Part>
    <Part kind="play" title="Find every E F and B C" how="Circle every E F and every B C on this long piano -- the half steps with no black key between. The first one is done for you.">
      <TnPKeys whites={22} w={23} h={118} rings={[['w2', 'w3']]} labels={Object.fromEntries(Array.from({ length: 22 }, (_, i) => ['w' + i, TN_WL[i % 7]]))}/>
      <div style={{display:'flex',alignItems:'center',gap:10,justifyContent:'flex-end',marginTop:8,fontSize:13.5,fontWeight:800,color:BK.ink}}>Count all the circles, the first one too: {bkBox(46, 34)}</div>
    </Part>
    <Faces/>
  </>);

  // 5 (faces "Sharp and flat: one key, two names")
  const nameCell = (k, i) => { const j = +k.slice(1), [sh, fl] = PC_INFO[TN_PC[k]].names;
    return <ExCell key={k} n={i + 1} ex={i === 0}><div style={{padding:'14px 2px 4px'}}>
      <TnPKeys whites={7} w={22} h={70} you={[k]} labels={{ w0: 'C', w1: 'D', w2: 'E', w3: 'F', w4: 'G', w5: 'A', w6: 'B' }}/>
      <div style={{display:'flex',justifyContent:'center',alignItems:'center',gap:6,marginTop:6,fontSize:16,fontWeight:900,color:BK.ink}}>{tnWrite('#', i === 0 ? sh[0] : null)}={tnWrite('b', i === 0 ? fl[0] : null)}</div>
    </div></ExCell>; };
  P(<>
    <WbTop step={4}/>
    <Part kind="together" title="Two names for each black key" how="The coral black key: write its sharp name (the letter on its left) and its flat name (the letter on its right).">
      <BkGrid cols={5} gap="8px 6px">{W.names.map(nameCell)}</BkGrid>
    </Part>
    <Part kind="home" title="Sharp up, flat down" how="Start on the letter. Draw an arrow a half step up for a sharp, or down for a flat, and fill in the circle on the black key you land on.">
      <BkGrid cols={2} gap="8px 10px">{W.push.map(([L, s], i) => { const w0 = 'w' + 'CDEFGAB'.indexOf(L), to = tnStep(w0, s === '#' ? 1 : -1);
        return <ExCell key={i} n={i + 6} ex={i === 0}><div style={{display:'grid',gridTemplateColumns:'64px 1fr',alignItems:'center',gap:6,padding:'12px 8px 4px'}}>
          <div style={{textAlign:'center',fontSize:28,fontWeight:900,color:BK.coral,lineHeight:1}}>{L}{tnSign(s)}</div>
          <TnPKeys whites={7} w={34} h={72} slots labels={{ w0: 'C', w1: 'D', w2: 'E', w3: 'F', w4: 'G', w5: 'A', w6: 'B' }} arrow={i === 0 ? [w0, s === '#' ? 1 : -1] : null} dots={i === 0 ? [to] : []}/>
        </div></ExCell>; })}</BkGrid>
    </Part>
    <Part kind="play" title="Same key or not?" how="Are the two names the same black key on the piano? Circle yes or no.">
      <BkGrid cols={4} gap="10px 10px">{W.same.map(([x, y], i) => <ExCell key={i} n={i + 10} ex={i === 0}><div style={{padding:'16px 4px 8px',display:'grid',justifyItems:'center',gap:10}}>
        <div style={{fontSize:30,fontWeight:900,color:BK.ink,lineHeight:1}}>{tnSignTxt(x)} <span style={{color:BK.muted,fontSize:22}}>·</span> {tnSignTxt(y)}</div>
        {wsChoose(['yes', 'no'], i === 0 ? (tnSamePc(x, y) ? 'yes' : 'no') : null)}</div></ExCell>)}</BkGrid>
    </Part>
    <Faces/>
  </>);

  // 6 (faces "Sharps and flats on the staff")
  const x4 = xs4(520);
  P(<>
    <WbTop step={5}/>
    <Part kind="together" title="Draw the sign" how="Draw the sign just before each note, on the note's own line or space. Then say its name.">
      <TnPStaff clef="treble" width={520} notes={W.draw.map(([d, a], i) => ({ d, x: x4[i], acc: i === 0 ? a : null, accC: BK.coral }))} items={W.draw.map(([d, a], i) => ({ x: x4[i], label: <>{'CDEFGAB'[d % 7]}{tnSign(a)}</>, ex: i === 0 }))}/>
    </Part>
    <Part kind="home" title="Name the sharps and flats" how="Write each note's name: the letter, then its sign.">
      <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:16}}>
        {[['treble', W.read.tre, 1], ['bass', W.read.bas, 5]].map(([cl, list, n0]) => { const x = sfXs(4, 270, true); return <TnPStaff key={cl} clef={cl} width={270} notes={list.map(([d, a], i) => ({ d, x: x[i], acc: a }))} items={list.map((_, i) => ({ x: x[i], n: n0 + i }))}/>; })}
      </div>
    </Part>
    <Part kind="play" title="Mark the key" how="Read the note with its sign, then fill in the circle on its black key.">
      <BkGrid cols={2} gap="8px 10px">{W.colour.map(([cl, d, a], i) => <ExCell key={i} n={i + 9} ex={i === 0}><div style={{display:'grid',gap:4,padding:'12px 18px 4px'}}>
        <TnPStaff clef={cl} width={240} notes={[{ d, x: 150, acc: a }]}/>
        <TnPKeys whites={7} w={34} h={72} slots labels={{ w0: 'C', w1: 'D', w2: 'E', w3: 'F', w4: 'G', w5: 'A', w6: 'B' }} dots={i === 0 ? [TN_KEY[tnDpc(d, a)]] : []}/>
      </div></ExCell>)}</BkGrid>
    </Part>
    <Faces/>
  </>);

  // 7. the check-up on paper (the Workbook's last page)
  P(<TnPaperCheck/>);
  return <>{pages}</>;
}
const TN_CHK = {
  half: [['w4', 1], ['b1', -1], ['w2', 1], ['w3', -1]], whole: [['w1', 1], ['w5', -1], ['b0', 1], ['w2', -1]],
  names: ['b1', 'b4', 'b3'], read: [['treble', 36, '#'], ['treble', 32, 'b'], ['bass', 22, '#'], ['bass', 25, 'b']],
};
function TnPaperCheck() {
  const C = TN_CHK, cell = (n, props, under) => <BkCell key={n} n={n}><div style={{padding:'12px 2px 3px'}}><TnPKeys whites={7} w={26} h={90} slots {...props}/>{under}</div></BkCell>;
  const x4 = sfXs(4, 510, true);
  return <div className="lb-paper" style={{display:'flex',flexDirection:'column',gap:4}}>
    <LbPaperHead/>
    {bkSec('A', 'A half step, the way the arrow says: mark the key (fill in the circle on a black key).')}
    <BkGrid cols={4} gap="6px 8px">{C.half.map(([k, dir], i) => cell(i + 1, { you: [k], arrow: [k, dir] }))}</BkGrid>
    {bkSec('B', 'A whole step, the way the arrow says: mark the key.')}
    <BkGrid cols={4} gap="6px 8px">{C.whole.map(([k, dir], i) => cell(i + 5, { you: [k], arrow: [k, dir, 2.1] }))}</BkGrid>
    {bkSec('C', 'From E up to E: write H or W under each pair of white neighbours.')}
    <TnPKeys start="E" whites={8} w={44} h={72} labels={Object.fromEntries(Array.from({ length: 8 }, (_, i) => ['w' + i, TN_WL[(2 + i) % 7]]))}/>
    <TnBoxRow whites={8} w={44} idx={[0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5]} nos={Object.fromEntries([0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5].map((x, j) => [x, 9 + j]))} bw={36} bh={32}/>
    {bkSec('D', 'Write both names of each coral black key.')}
    <BkGrid cols={3} gap="6px 8px">{C.names.map((k, i) => <BkCell key={k} n={i + 16}><div style={{padding:'12px 2px 4px'}}><TnPKeys whites={7} w={22} h={70} you={[k]} labels={{ w0: 'C', w1: 'D', w2: 'E', w3: 'F', w4: 'G', w5: 'A', w6: 'B' }}/>
      <div style={{display:'flex',justifyContent:'center',alignItems:'center',gap:6,marginTop:5,fontSize:16,fontWeight:900,color:BK.ink}}>{tnWrite('#')}={tnWrite('b')}</div></div></BkCell>)}</BkGrid>
    {bkSec('E', 'Write each note\'s name: the letter, then its sign.')}
    <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:16}}>
      {[['treble', C.read.filter(x => x[0] === 'treble'), 19], ['bass', C.read.filter(x => x[0] === 'bass'), 21]].map(([cl, list, n0]) => { const x = sfXs(2, 250, true); return <TnPStaff key={cl} clef={cl} width={250} notes={list.map(([, d, a], i) => ({ d, x: x[i], acc: a }))} items={list.map((_, i) => ({ x: x[i], n: n0 + i }))}/>; })}
    </div>
  </div>;
}

function TnTeacher() {
  const W = TN_WB, C = TN_CHK, pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="tones" teacher>{content}</WbPage>);
  const nm = (k) => tnKeyName(k), hw = (start) => { const S0 = TN_WL.indexOf(start); return Array.from({ length: 7 }, (_, i) => ['E', 'B'].includes(TN_WL[(S0 + i) % 7]) ? 'H' : 'W').join(' '); };
  const both = (k) => PC_INFO[TN_PC[k]].names.map(prettyNote).join(' = ');
  P(<>
    <div style={{fontFamily:"'Playfair Display', Georgia, serif",fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('tones')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 12px',lineHeight:1.5}}>Answers for every workbook page, the mistakes students make most, and a line to say when they get stuck. The book teaches both pairs of names: semitone and tone (Australian and British books, AMEB), half step and whole step (American books); either is right. One black key with two names is <b>enharmonic</b> (C♯ = D♭) -- a Music Craft Grade 1 word, said here, not in the student's book. The half-step walk from C to C is the <b>chromatic scale</b> -- named in the book; Piano for Leisure Grade 1 plays it hands separately, writing it out waits for later. The white keys' W W H W W W H from C is the major scale's recipe: the book only names it; the Scales room builds on it. Left for later: the natural sign and "a sign lasts until the bar line" (the Accidentals room), E♯ = F and C♭ = B (the scales chapters), double sharps and flats (Grade 4).</div>
    <TcBlock page={2} title="A half step: a semitone" answers={<>{tcAns('TRY IT', W.halfUp.map(k => nm(k) + ' → ' + nm(tnStep(k, 1))))}{tcAns('YOUR TURN', W.halfDown.map(k => nm(k) + ' → ' + nm(tnStep(k, -1))), 5)}{tcAns('PLAY', W.count.map(([a, b]) => nm(a) + ' to ' + nm(b) + ': ' + (TN_PC[b] - TN_PC[a])), 9)}</>}
      watch="Counting the key they stand on as the first step (“C, C♯, D -- three!”). Skipping the black key and landing on the next white key. From E and B a half step up is a white key: there is no black key on their right."
      say="“Count the steps, not the keys: the first step lands on the very next key.”"/>
    <TcBlock page={3} title="A whole step: a tone" answers={<>{tcAns('TRY IT', W.wholeUp.map(k => nm(k) + ' → ' + nm(tnStep(k, 2))))}{tcAns('YOUR TURN', W.upDown.map(([k, d]) => nm(k) + (d > 0 ? ' up → ' : ' down → ') + nm(tnStep(k, 2 * d))), 5)}{tcAns('PLAY', W.pairs.map(p => nm(p[0]) + ' ' + nm(p[1]) + ': ' + tnPairStep(p)), 9)}</>}
      watch="Thinking a whole step is always from a white key to the next white key: E to F is not. From E a whole step up is the black key F♯; from F a whole step down is E♭. A whole step can be black to black (F♯ to G♯)."
      say="“Two half steps: one key in between.”"/>
    <TcBlock page={4} title="White half steps: E F and B C" answers={<>{tcAns('TRY IT', ['1-7: ' + hw('C')], null)}{tcAns('YOUR TURN', ['8-14: ' + hw('A')], null)}{tcAns('PLAY', ['6 circles: E F and B C in each of the three octaves'], null)}</>}
      watch="Calling every pair of white neighbours a tone. Missing the B C that crosses from one octave into the next. The pattern from C -- W W H W W W H -- is the major scale's; AMEB and the scales chapter write it T T S T T T S (tone, semitone): accept either."
      say="“Is there a black key between them?”"/>
  </>);
  P(<>
    <TcBlock page={5} title="Sharp and flat: one key, two names" answers={<>{tcAns('TRY IT', W.names.map(both))}{tcAns('YOUR TURN', W.push.map(([L, s]) => prettyNote(L + s) + ': ' + L + (s === '#' ? ' up → ' : ' down → ') + nm(tnStep('w' + 'CDEFGAB'.indexOf(L), s === '#' ? 1 : -1))), 6)}{tcAns('PLAY', W.same.map(([x, y]) => prettyNote(x) + ' ' + prettyNote(y) + ': ' + (tnSamePc(x, y) ? 'yes' : 'no')), 10)}</>}
      watch="Thinking a black key has one name, or that a sharp is always the black key on the right of any key: the sharp is named from the white key on its left, the flat from the white key on its right. Writing the sign before the letter (“♯F”)."
      say="“A half step up from C is C sharp; a half step down from D is D flat -- the same key.”"/>
    <TcBlock page={6} title="Sharps and flats on the staff" answers={<>{tcAns('TRY IT', W.draw.map(([d, a]) => prettyNote(tnDName(d, a)) + ((d - CLEFS.treble.low) % 2 ? ' in the ' : ' on the ') + tnPlace('treble', d)), null)}{tcAns('YOUR TURN', [...W.read.tre, ...W.read.bas].map(([d, a]) => prettyNote(tnDName(d, a))))}{tcAns('PLAY', W.colour.map(([, d, a]) => prettyNote(tnDName(d, a)) + ': ' + tnName(tnDpc(d, a))), 9)}</>}
      watch="Writing the sign after the note, or a line or space too high or too low: the sharp's box and the flat's round belly sit on the note's own line or space. Reading the letter without the sign."
      say="“The letter first, then the sign: F sharp. Write the sign first, then the note.”"/>
    <TcBlock page={7} title="The check-up on paper (the Workbook's last page)" answers={<>
      {tcAns('A', C.half.map(([k, d]) => nm(k) + (d > 0 ? ' up → ' : ' down → ') + nm(tnStep(k, d))))}
      {tcAns('B', C.whole.map(([k, d]) => nm(k) + (d > 0 ? ' up → ' : ' down → ') + nm(tnStep(k, 2 * d))), 5)}
      {tcAns('C', ['9-15: ' + hw('E')], null)}
      {tcAns('D', C.names.map(both), 16)}
      {tcAns('E', C.read.map(([, d, a]) => prettyNote(tnDName(d, a))), 19)}
    </>}
      goBack={[{ id: 'a', step: 1, page: 2 }, { id: 'b', step: 2, page: 3 }, { id: 'c', step: 3, page: 4 }, { id: 'd', step: 4, page: 5 }, { id: 'e', step: 5, page: 6 }]}/>
  </>);
  return <>{pages}</>;
}
WORKBOOKS.tones = TnWorkbook;
TEACHER_COPIES.tones = TnTeacher;
