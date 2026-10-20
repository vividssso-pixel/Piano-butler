
// ─── Modes lessons (her call, 2026-10-21): Home, Pitch, Modes is its own concept, taught as a lecture to her.
// 1 white keys, a new home (md-start); 2 the seven names (sc-modes); 3 same home, new colour (md-colour); 4 find the parent major (md-parent); 5 any key (md-keys).
// Facts: the MODES table (her material); the parent-major rule below is derived from the same table and spellScale, flagged for her review.
const MD_PK = { 0: 'C', 7: 'G', 2: 'D', 9: 'A', 4: 'E', 11: 'B', 6: 'Gb', 1: 'Db', 8: 'Ab', 3: 'Eb', 10: 'Bb', 5: 'F' };
const mdParent = (pc, st) => MD_PK[(((pc - SC_MP[st]) % 12) + 12) % 12];
const MD_WN = ['C', 'D', 'E', 'F', 'G', 'A', 'B'];
const mdNm = (m) => LANG === 'ko' ? m.nameKo : m.name;
const mdOrd = (n) => t(['1st', '2nd', '3rd', '4th', '5th', '6th', '7th'][n], (n + 1) + '번째');
const mdSign = (par) => { const k = KEY_SIGS.find(x => x.major === par); return !k || !k.count ? t('no ♯ or ♭', '♯도 ♭도 없음') : k.count + (k.type === 'sharp' ? '♯' : '♭'); };
const mdStaff = (par, st) => {
  const nm = scModeNames(par, st), d0 = nm[0][0] === 'B' ? 27 : 28 + STAFF_LETTERS.indexOf(nm[0][0]), items = Array.from({ length: 8 }, (_, j) => ['q', 1, d0 + j]).concat([['||']]), hl = skgOf(items, par, n => n.byKey);
  return <SkgStaff key={par + st} items={items} k={par} width={330} o={{ boxS: 26, D: 30, hl2: hl, underAlt: hl, ksCol: '#2e8a6e', ...skgUnder(items, par, null, []) }}/>;
};
const mdPic = (K, N, an, hot) => { const marks = {}, names = {}; K.forEach((k, j) => { marks[k] = hot && hot[j] ? 'target' : j === 0 || j === 7 ? 'target' : 'pass'; names[k] = prettyAny(N[j]); }); if (an >= 0) marks[K[an]] = 'pick'; return { marks, names }; };
// tap the eight notes one by one; a wrong key is said plainly and the next note is named
function MdSeq({ K, N, first, next, done, again, onBack, nk }) {
  const [at, setAt] = useState(0), [bad, setBad] = useState(null), [nonce, setNonce] = useState(0), timers = useRef([]);
  const clear = () => { timers.current.forEach(clearTimeout); timers.current = []; };
  useEffect(() => clear, []);
  useEffect(() => { clear(); setAt(0); setBad(null); setNonce(n => n + 1); }, [nk]);
  const fin = at >= 7, marks = {}, names = {}, NN = N.map(prettyAny);
  for (let j = 0; j <= at; j++) { marks[K[j]] = j === at && !fin ? 'pick' : j === 0 || j === 7 ? 'target' : 'pass'; names[K[j]] = NN[j]; }
  if (bad != null) marks[bad] = 'bad';
  const line = fin ? done : bad != null ? t('Not that key. After ' + NN[at] + ' comes ' + NN[at + 1] + '.', '그 건반이 아니에요. ' + NN[at] + ' 다음은 ' + NN[at + 1] + '이에요.') : at === 0 ? first : next(at, NN);
  const tap = (k) => { if (fin) return; clear(); if (k === K[at + 1]) { setBad(null); setAt(at + 1); setNonce(n => n + 1); playKey(k, 0.5); } else if (at === 0 && k === K[0]) { setAt(0); playKey(k, 0.5); } else { setBad(k); playKey(k, 0.4); timers.current.push(setTimeout(() => setBad(null), 1100)); } };
  return <>
    <div style={scS.title}>{t('Your turn', '내가 해보기')}</div>
    <div style={scS.line}>{line}</div>
    <ScKeys ks={K} marks={at === 0 ? { ...marks, [K[0]]: 'pick' } : marks} names={names} arcs={[]} nonce={nonce + ':' + nk} onTap={tap}/>
    {scRow(<>
      <button className="ghost-btn" style={scS.back} onClick={() => { clear(); onBack(); }}>{t('← Back', '← 이전')}</button>
      {fin && again && <button className="ghost-btn" style={scS.prim} onClick={again}>{t('Another →', '다른 것 →')}</button>}
    </>)}
  </>;
}

// 1: the same seven white keys, a new home
function MdStart() {
  const [view, setView] = useState('all'), [st, setSt] = useState(1), [q, setQ] = useState(1), P = useScPlay([view, st]);
  let body;
  if (view === 'all') {
    const K = scModeK('C', 0), N = scModeNames('C', 0), M = mdPic(K, N, -1);
    body = <>
      <div style={scS.title}>{t('The same white keys, a new home', '같은 흰건반, 새로운 집')}</div>
      <div style={scS.line}>{t('Play only the white keys from C up to the next C. That is C major, and C is its home.', 'C에서 다음 C까지 흰건반만 쳐요. 그게 C장조이고, C가 “집”이에요.')}</div>
      <ScKeys ks={K} marks={M.marks} names={M.names} arcs={[]} nonce="all"/>
      {scRow(<button className="ghost-btn" style={scS.prim} onClick={() => setView('one')}>{t('Move the home →', '집을 옮겨 보기 →')}</button>)}
    </>;
  } else if (view === 'one') {
    const K = scModeK('C', st), N = scModeNames('C', st), M = mdPic(K, N, P.an);
    body = <>
      <div style={scS.title}>{t('Start on ' + N[0], N[0] + '에서 시작')}</div>
      <div style={scS.line}>{t('Still only the white keys, the same seven notes. Only the home changed: now ' + N[0] + ' is home.', '여전히 흰건반 일곱 개, 같은 음이에요. “집”만 바뀌었어요: 이제 ' + N[0] + '이 집이에요.')}</div>
      <ScKeys ks={K} marks={M.marks} names={M.names} arcs={[]} nonce={'o' + st}/>
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(7,minmax(0,1fr))', gap: 4, maxWidth: 330, margin: '8px auto 0' }}>
        {MD_WN.map((w, j) => <button key={w} className={'chip' + (st === j ? ' active' : '')} aria-pressed={st === j} style={{ ...KF_BTN, minHeight: 38, padding: '0 2px' }} onClick={() => setSt(j)}>{w}</button>)}
      </div>
      {scRow(<>
        <button className="ghost-btn" style={scS.back} onClick={() => setView('all')}>{t('← Back', '← 이전')}</button>
        <button className="ghost-btn" style={scS.back} onClick={() => P.play(K)}>{t('▶ Hear it', '▶ 듣기')}</button>
        <button className="ghost-btn" style={scS.prim} onClick={() => { setView('try'); setQ(1); }}>{t('Your turn →', '내가 해보기 →')}</button>
      </>)}
    </>;
  } else {
    const K = scModeK('C', q), N = scModeNames('C', q);
    body = <MdSeq K={K} N={N} nk={'s' + q} onBack={() => setView('one')} again={() => setQ(1 + (q % 6))}
      first={t('Play the white keys from ' + N[0] + ' up to the next ' + N[0] + '. Start on ' + N[0] + ', then tap ' + N[1] + '.', N[0] + '에서 다음 ' + N[0] + '까지 흰건반을 쳐요. ' + N[0] + '에서 시작해서 ' + N[1] + '을 눌러요.')}
      next={(at, NN) => t('From ' + NN[at] + ', tap the next white key: ' + NN[at + 1] + '.', NN[at] + ' 다음 흰건반 ' + NN[at + 1] + '을 눌러요.')}
      done={t('Seven white keys again, with a new home: ' + N[0] + '.', '흰건반 일곱 개 그대로, 집만 ' + N[0] + '(으)로 바뀌었어요.')}/>;
  }
  return scBox('modes', body);
}

// 2: the seven names (the white keys of C, each home has a name)
function MdNames() {
  const [view, setView] = useState('all'), [i, setI] = useState(0), [stf, setStf] = useState(false), [q, setQ] = useState(1), [at, setAt] = useState(-1), [bad, setBad] = useState(null), [nonce, setNonce] = useState(0), P = useScPlay([view, i]);
  const timers = useRef([]); useEffect(() => () => timers.current.forEach(clearTimeout), []);
  let body;
  if (view === 'all') {
    const K = scModeK('C', 0), N = scModeNames('C', 0), M = mdPic(K, N, -1);
    body = <>
      <div style={scS.title}>{t('The seven modes', '일곱 가지 선법')}</div>
      <div style={scS.line}>{t('Every white key can be a home, and every home has its own name. These are the modes.', '흰건반마다 “집”이 될 수 있고, 집마다 이름이 있어요. 이게 선법이에요.')}</div>
      <ScKeys ks={K} marks={M.marks} names={M.names} arcs={[]} nonce="all"/>
      <div style={{ display: 'flex', flexWrap: 'wrap', gap: 5, justifyContent: 'center', maxWidth: 330, margin: '8px auto 0' }}>
        {MODES.map((m, j) => <span key={m.name} style={{ padding: '4px 9px', borderRadius: 999, border: '1.5px solid #d8cfb6', background: '#efeadc', fontSize: 12.5, fontWeight: 800, color: '#26296b' }}>{MD_WN[j]} {mdNm(m)}</span>)}
      </div>
      {scRow(<button className="ghost-btn" style={scS.prim} onClick={() => { setView('one'); setI(0); }}>{t('One by one →', '하나씩 →')}</button>)}
    </>;
  } else if (view === 'one') {
    const m = MODES[i], K = scModeK('C', i), N = scModeNames('C', i), M = mdPic(K, N, P.an);
    body = <>
      <div style={scS.title}>{LANG === 'ko' ? m.nameKo + ' (' + m.name + ')' : m.name} {t('on', '')} {N[0]}{LANG === 'ko' ? '에서' : ''}</div>
      <div style={scS.line}>{t(m.formula, m.formulaKo)}. {t(m.mood, m.moodKo)}</div>
      <ScKeys ks={K} marks={M.marks} names={M.names} arcs={[]} nonce={'n' + i}/>
      <div style={{ textAlign: 'center', fontSize: 13, fontWeight: 700, color: '#4a4d86', fontStyle: 'italic', margin: '6px 0' }}>{t(m.exEn, m.exKo)}</div>
      <ScStaffBtn on={stf} set={setStf}/>
      {stf && <>{mdStaff('C', i)}<div style={{ textAlign: 'center', fontSize: 12.5, fontWeight: 700, color: '#6d6f9c', marginTop: 4 }}>{t('Only white keys: no sharps or flats.', '흰건반만: ♯도 ♭도 없어요.')}</div></>}
      {scRow(<>
        <button className="ghost-btn" style={scS.back} onClick={() => { if (i === 0) setView('all'); else setI(i - 1); }}>{t('← Back', '← 이전')}</button>
        <button className="ghost-btn" style={scS.back} onClick={() => P.play(K)}>{t('▶ Hear it', '▶ 듣기')}</button>
        <button className="ghost-btn" style={scS.prim} onClick={() => { if (i === 6) { setView('try'); setQ(1); setAt(-1); setBad(null); } else setI(i + 1); }}>{i === 6 ? t('Your turn →', '내가 해보기 →') : t('Next →', '다음 →')}</button>
      </>)}
    </>;
  } else {
    const m = MODES[q], K = scModeK('C', 0), done = at >= 0, marks = {}, names = {};
    K.slice(0, 7).forEach((k, j) => { names[k] = MD_WN[j]; });
    if (done) { marks[K[q]] = 'target'; } if (bad != null) marks[bad] = 'bad';
    const count = MD_WN.slice(0, q + 1).map((w, j) => w + ' (' + (j + 1) + ')').join(', ');
    const line = done ? t(mdNm(m) + ' starts on ' + MD_WN[q] + '.', mdNm(m) + '은(는) ' + MD_WN[q] + '에서 시작해요.')
      : bad != null ? t('Not that key. ' + m.name + ' is the ' + mdOrd(q) + ' mode: from C count ' + count + '. Its home is ' + MD_WN[q] + '.', '그 건반이 아니에요. ' + m.nameKo + '은(는) ' + mdOrd(q) + ' 선법이에요: C부터 세면 ' + count + '. 집은 ' + MD_WN[q] + '이에요.')
      : t('Where is the home of ' + m.name + '? Tap the white key.', m.nameKo + '(' + m.name + ')의 집은 어디일까요? 흰건반을 눌러요.');
    const tap = (k) => { if (done) return; timers.current.forEach(clearTimeout); if (k === K[q]) { setBad(null); setAt(q); setNonce(n => n + 1); playKey(k, 0.5); } else { setBad(k); playKey(k, 0.4); timers.current = [setTimeout(() => setBad(null), 1400)]; } };
    body = <>
      <div style={scS.title}>{t('Your turn', '내가 해보기')}</div>
      <div style={scS.line}>{line}</div>
      <ScKeys ks={K} marks={marks} names={names} arcs={[]} nonce={'t' + q + nonce} onTap={tap}/>
      {scRow(<>
        <button className="ghost-btn" style={scS.back} onClick={() => { setView('one'); setI(6); }}>{t('← Back', '← 이전')}</button>
        {done && <button className="ghost-btn" style={scS.prim} onClick={() => { setQ(1 + (q % 6)); setAt(-1); setBad(null); }}>{t('Another →', '다른 것 →')}</button>}
      </>)}
    </>;
  }
  return scBox('modes', body);
}

// 3: the same home, a different colour. The seven modes on C, against C major.
function MdColour() {
  const [st, setSt] = useState(1), P = useScPlay([st]);
  const par = mdParent(0, st), K = scModeK(par, st), N = scModeNames(par, st), M = MODES[st], BK = scModeK('C', 0), BN = scModeNames('C', 0);
  const diff = K.map((k, j) => k - SC_OFF[j]), lw = [1, 2, 3, 4, 5, 6].filter(j => diff[j] < 0), rs = [1, 2, 3, 4, 5, 6].filter(j => diff[j] > 0);
  const joinAnd = (a) => LANG === 'ko' ? a.join(' · ') : a.length < 2 ? a.join('') : a.slice(0, -1).join(', ') + ' and ' + a[a.length - 1];
  const fmt = (arr) => joinAnd(arr.map(j => mdOrd(j))) + ' (' + arr.map(j => prettyAny(N[j])).join(' ') + ')';
  const line = !lw.length && !rs.length ? t('Nothing changes: this is C major itself.', '바뀌는 음이 없어요: C장조 그 자체예요.')
    : t('Compared with C major: ' + (lw.length ? 'the ' + fmt(lw) + ' lowered' : '') + (lw.length && rs.length ? '; ' : '') + (rs.length ? 'the ' + fmt(rs) + ' raised' : '') + '.',
      'C장조와 달라진 음: ' + (lw.length ? fmt(lw) + ' 내림' : '') + (lw.length && rs.length ? ', ' : '') + (rs.length ? fmt(rs) + ' 올림' : '') + '.');
  const hot = diff.map(d => d !== 0), B = mdPic(BK, BN, -1), X = mdPic(K, N, P.an, hot);
  X.marks = {}; K.forEach((k, j) => { X.marks[k] = diff[j] !== 0 ? 'target' : 'pass'; }); if (P.an >= 0) X.marks[K[P.an]] = 'pick';
  B.marks = {}; BK.forEach((k) => { B.marks[k] = 'pass'; });
  const lab = { fontSize: 12, fontWeight: 900, color: 'var(--muted)', letterSpacing: '0.05em', margin: '8px 0 2px' };
  return scBox('modes', <>
    <div style={scS.title}>{t('The same home, a new colour', '같은 집, 다른 색깔')}</div>
    <div style={scS.line}>{line}</div>
    <div style={lab}>{t('C MAJOR', 'C 장조')}</div>
    <ScKeys inKey clean ks={BK} marks={B.marks} names={B.names} ncol={{}} arcs={[]} nonce="b" mw={520}/>
    <div style={lab}>{'C ' + mdNm(M).toUpperCase()}</div>
    <ScKeys inKey clean ks={K} marks={X.marks} names={X.names} ncol={{}} arcs={[]} nonce={'x' + st} mw={520}/>
    <div style={{ display: 'flex', gap: 14, justifyContent: 'center', marginTop: 8, fontSize: 12.5, fontWeight: 800, color: '#26296b' }}>
      <span style={{ display: 'inline-flex', alignItems: 'center', gap: 5 }}><span style={{ width: 14, height: 14, borderRadius: 3, background: '#e4572e', border: '1.5px solid #c0431f' }}/>{t('different from C major', 'C장조와 다른 음')}</span>
    </div>
    <div style={{ display: 'grid', gridTemplateColumns: 'repeat(4,minmax(0,1fr))', gap: 5, maxWidth: 340, margin: '10px auto 0' }}>
      {MODES.map((m, j) => <button key={m.name} className={'chip' + (st === j ? ' active' : '')} aria-pressed={st === j} style={{ ...KF_BTN, minHeight: 38, padding: '0 2px', fontSize: 12.5 }} onClick={() => setSt(j)}>{mdNm(m)}</button>)}
    </div>
    <div style={{ textAlign: 'center', fontSize: 13, fontWeight: 700, color: '#4a4d86', marginTop: 8 }}>{t(M.mood, M.moodKo)}</div>
    {scRow(<button className="ghost-btn" style={scS.back} onClick={() => P.an >= 0 ? P.stop() : P.play(K)}>{P.an >= 0 ? t('■ Stop', '■ 멈추기') : t('▶ Hear it', '▶ 듣기')}</button>)}
  </>);
}

// 4: find the parent major: the home note is the nth note of its parent, so count back
const MD_Q = [[1, 'D'], [4, 'C'], [5, 'G'], [3, 'D'], [2, 'F'], [1, 'A'], [4, 'E'], [6, 'G']];
function MdParent() {
  const [view, setView] = useState('one'), [s, setS] = useState(0), [q, setQ] = useState(0), [bad, setBad] = useState(null), [ok, setOk] = useState(false), P = useScPlay([view, s, q]);
  let body;
  if (view === 'one') {
    const st = MD_Q[0][0], par = MD_Q[0][1], m = MODES[st], K = scModeK(par, st), N = scModeNames(par, st), PK = scModeK(par, 0), PN = scModeNames(par, 0);
    const R = prettyAny(N[0]), pr = prettyNote(par);
    const hot = {}; PK.forEach((k) => { hot[k] = false; });
    const mk = {}, nm = {};
    if (s < 1) { const X = mdPic(K, N, -1); body = { marks: X.marks, names: X.names, ks: K }; }
    else { PK.forEach((k, j) => { mk[k] = j === 0 || j === 7 ? 'target' : j === st ? 'pick' : 'pass'; nm[k] = prettyAny(PN[j]); }); body = { marks: mk, names: nm, ks: PK }; }
    const lines = [
      t(mdNm(m) + ' is the ' + mdOrd(st) + ' mode: its home is the ' + mdOrd(st) + ' note of its parent major scale.', mdNm(m) + '은(는) ' + mdOrd(st) + ' 선법이에요: 집이 부모 장음계의 ' + mdOrd(st) + ' 음이에요.'),
      t('So ' + R + ' is the ' + mdOrd(st) + ' note. Count back: ' + R + ' (' + (st + 1) + '), ' + prettyAny(PN[0]) + ' (1). The first note is ' + prettyAny(PN[0]) + '.', R + '이 ' + mdOrd(st) + ' 음이에요. 거꾸로 세요: ' + R + ' (' + (st + 1) + '), ' + prettyAny(PN[0]) + ' (1). 첫 음은 ' + prettyAny(PN[0]) + '이에요.'),
      t('The parent is ' + pr + ' major. ' + R + ' ' + m.name + ' is the notes of ' + pr + ' major, started on ' + R + '.', '부모는 ' + pr + ' 장조예요. ' + R + ' ' + m.nameKo + '은(는) ' + pr + ' 장음계의 음을 ' + R + '에서 시작한 거예요.'),
    ];
    const ln = s === 0 ? lines[0] : s === 1 ? lines[1] : lines[2];
    body = <>
      <div style={scS.title}>{t('Find the parent major', '부모 장조 찾기')}</div>
      <div style={scS.line}>{ln}</div>
      <div style={{ textAlign: 'center', fontFamily: "'Playfair Display', Georgia, serif", fontSize: 20, fontWeight: 900, color: '#26296b', marginBottom: 4 }}>{R} {mdNm(m)}</div>
      <ScKeys ks={body.ks} marks={body.marks} names={body.names} arcs={[]} nonce={'p' + s}/>
      {scRow(<>
        <button className="ghost-btn" style={scS.back} onClick={() => setS(Math.max(0, s - 1))}>{t('← Back', '← 이전')}</button>
        <button className="ghost-btn" style={scS.prim} onClick={() => { if (s === 2) { setView('try'); setQ(0); setBad(null); setOk(false); } else setS(s + 1); }}>{s === 2 ? t('Your turn →', '내가 해보기 →') : t('Next →', '다음 →')}</button>
      </>)}
    </>;
  } else {
    const [st, par] = MD_Q[q], m = MODES[st], K = scModeK(par, st), N = scModeNames(par, st), PN = scModeNames(par, 0), R = prettyAny(N[0]), X = mdPic(K, N, -1);
    const others = ['C', 'G', 'D', 'A', 'E', 'F', 'Bb', 'Eb'].filter(k => k !== par), ch = [par, others[q % 7], others[(q + 2) % 7], others[(q + 4) % 7]].filter((k, j, a) => a.indexOf(k) === j);
    while (ch.length < 4) { const k = others.find(o => !ch.includes(o)); ch.push(k); }
    const order = ch.slice().sort((a, b) => ((SF12.indexOf(a) * 7 + q * 3) % 11) - ((SF12.indexOf(b) * 7 + q * 3) % 11));
    const back = PN.slice(0, st + 1).map((n, j) => prettyAny(n) + ' (' + (j + 1) + ')').reverse().join(', ');
    const line = ok ? t('Yes: ' + R + ' ' + m.name + ' is ' + prettyNote(par) + ' major started on ' + R + '.', '맞아요: ' + R + ' ' + m.nameKo + '은(는) ' + prettyNote(par) + ' 장음계를 ' + R + '에서 시작한 거예요.')
      : bad ? t('Not ' + prettyNote(bad) + ' major. ' + m.name + ' is the ' + mdOrd(st) + ' mode, so ' + R + ' is the ' + mdOrd(st) + ' note. Count back: ' + back + '. The parent is ' + prettyNote(par) + ' major.', prettyNote(bad) + ' 장조가 아니에요. ' + m.nameKo + '은(는) ' + mdOrd(st) + ' 선법이라 ' + R + '이 ' + mdOrd(st) + ' 음이에요. 거꾸로 세면 ' + back + '. 부모는 ' + prettyNote(par) + ' 장조예요.')
      : t(R + ' ' + m.name + ': which major scale has the same notes?', R + ' ' + m.nameKo + ': 같은 음을 가진 장음계는 무엇일까요?');
    body = <>
      <div style={scS.title}>{t('Your turn', '내가 해보기')}</div>
      <div style={scS.line}>{line}</div>
      <ScKeys ks={K} marks={X.marks} names={X.names} arcs={[]} nonce={'q' + q}/>
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(4,minmax(0,1fr))', gap: 6, maxWidth: 330, margin: '10px auto 0' }}>
        {order.map(k => <button key={k} className={'chip' + (ok && k === par ? ' active' : '')} style={{ ...KF_BTN, minHeight: 42, padding: '0 2px', ...(bad === k ? { borderColor: '#c8361b', color: '#c8361b' } : {}) }} onClick={() => { if (ok) return; if (k === par) { setOk(true); setBad(null); } else setBad(k); }}>{prettyNote(k)}</button>)}
      </div>
      {scRow(<>
        <button className="ghost-btn" style={scS.back} onClick={() => { setView('one'); setS(2); }}>{t('← Back', '← 이전')}</button>
        {ok && <button className="ghost-btn" style={scS.prim} onClick={() => { setQ((q + 1) % MD_Q.length); setBad(null); setOk(false); }}>{t('Another →', '다른 것 →')}</button>}
      </>)}
    </>;
  }
  return scBox('modes', body);
}

// 5: any key. Choose the mode and the home note; the parent major is worked out for you. Then play it.
const MD_BLACK = { 1: ['C♯', 'D♭'], 3: ['D♯', 'E♭'], 6: ['F♯', 'G♭'], 8: ['G♯', 'A♭'], 10: ['A♯', 'B♭'] };
function MdKeys() {
  const [view, setView] = useState('pick'), [st, setSt] = useState(1), [pc, setPc] = useState(2), [stf, setStf] = useState(false), P = useScPlay([view, st, pc]);
  const par = mdParent(pc, st), K = scModeK(par, st), N = scModeNames(par, st), M = MODES[st], R = prettyAny(N[0]), X = mdPic(K, N, P.an);
  let body;
  if (view === 'pick') {
    body = <>
      <div style={scS.title}>{R} {mdNm(M)}</div>
      <div style={scS.line}>{t('The notes of ' + prettyNote(par) + ' major (' + mdSign(par) + '), started on ' + R + '.', prettyNote(par) + ' 장음계(' + mdSign(par) + ')의 음을 ' + R + '에서 시작해요.')}</div>
      <ScKeys ks={K} marks={X.marks} names={X.names} arcs={[]} nonce={'k' + st + ':' + pc}/>
      <div style={{ fontSize: 12, fontWeight: 900, color: 'var(--muted)', letterSpacing: '0.05em', margin: '10px 0 4px', textAlign: 'center' }}>{t('MODE', '선법')}</div>
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(4,minmax(0,1fr))', gap: 5, maxWidth: 340, margin: '0 auto' }}>
        {MODES.map((m, j) => <button key={m.name} className={'chip' + (st === j ? ' active' : '')} aria-pressed={st === j} style={{ ...KF_BTN, minHeight: 38, padding: '0 2px', fontSize: 12.5 }} onClick={() => setSt(j)}>{mdNm(m)}</button>)}
      </div>
      <div style={{ fontSize: 12, fontWeight: 900, color: 'var(--muted)', letterSpacing: '0.05em', margin: '10px 0 4px', textAlign: 'center' }}>{t('HOME NOTE', '집이 되는 음')}</div>
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(6,minmax(0,1fr))', gap: 5, maxWidth: 340, margin: '0 auto' }}>
        {[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11].map(p => <button key={p} className={'chip' + (pc === p ? ' active' : '')} aria-pressed={pc === p} style={{ ...KF_BTN, minHeight: 40, padding: '0 2px' }} onClick={() => setPc(p)}>{MD_BLACK[p] ? <span style={{ display: 'inline-grid', lineHeight: 1.05, fontSize: 12, gap: 1 }}><span>{MD_BLACK[p][0]}</span><span>{MD_BLACK[p][1]}</span></span> : MD_WN[[0, 0, 1, 0, 2, 3, 0, 4, 0, 5, 0, 6][p]]}</button>)}
      </div>
      <ScStaffBtn on={stf} set={setStf}/>
      {stf && <>{mdStaff(par, st)}<div style={{ textAlign: 'center', fontSize: 12.5, fontWeight: 700, color: '#6d6f9c', marginTop: 4 }}>{t('Green: from the key signature of ' + prettyNote(par) + ' major.', '초록: ' + prettyNote(par) + ' 장조의 조표에 있는 음.')}</div></>}
      {scRow(<>
        <button className="ghost-btn" style={scS.back} onClick={() => P.an >= 0 ? P.stop() : P.play(K)}>{P.an >= 0 ? t('■ Stop', '■ 멈추기') : t('▶ Hear it', '▶ 듣기')}</button>
        <button className="ghost-btn" style={scS.prim} onClick={() => setView('try')}>{t('Play it myself →', '직접 쳐 보기 →')}</button>
      </>)}
    </>;
  } else {
    body = <MdSeq K={K} N={N} nk={'k' + st + ':' + pc} onBack={() => setView('pick')}
      first={t('Play ' + R + ' ' + M.name + ': the notes of ' + prettyNote(par) + ' major, started on ' + R + '. Start on ' + R + ', then tap ' + prettyAny(N[1]) + '.', R + ' ' + M.nameKo + ': ' + prettyNote(par) + ' 장음계의 음을 ' + R + '에서 시작해요. ' + R + '에서 시작해서 ' + prettyAny(N[1]) + '을 눌러요.')}
      next={(at, NN) => t('From ' + NN[at] + ', tap the next note of ' + prettyNote(par) + ' major: ' + NN[at + 1] + '.', NN[at] + ' 다음, ' + prettyNote(par) + ' 장음계의 음 ' + NN[at + 1] + '을 눌러요.')}
      done={t(R + ' ' + M.name + ' is ' + prettyNote(par) + ' major started on ' + R + '.', R + ' ' + M.nameKo + '은(는) ' + prettyNote(par) + ' 장음계를 ' + R + '에서 시작한 거예요.')}/>;
  }
  return scBox('modes', body);
}
