
// ─── Chapter: Minor Scales (Build AC, 2026-10-26; the board's call 6 as the syllabus settles it: Grade 1 theory) ───
// Playing Scales plays A and E minor; this room is the minor key on paper and by ear, as the Grade 1 theory asks: a major or a
// minor third; the minor that shares a key signature (three half steps down: A, E, D and G minor); the harmonic minor (the 7th
// raised by an accidental beside the note, not in the key signature); tones, semitones and the tone and a half; a major or a
// harmonic minor scale by ear. Spelling from spellMinor and the key signatures from KEY_SIGS; the staff is SkgStaff.
const MS_KEYS = ['A', 'E', 'D', 'G'];
const MS_REL = { A: 'C', E: 'G', D: 'F', G: 'Bb' };
const MS_LO = { A: -3, E: 4, D: 2, G: -5 };   // where each scale starts on the keys (semitones from middle C)
const MS_MAJ_LO = { C: 0, G: -5, F: 5, Bb: -2, D: 2 };
const MS_HAR = [0, 2, 3, 5, 7, 8, 11, 12], MS_NAT = [0, 2, 3, 5, 7, 8, 10, 12], MS_MAJ = [0, 2, 4, 5, 7, 9, 11, 12];
const msName = (m) => t(m + ' minor', m + '단조');
const msMajName = (M) => t(prettyNote(M) + ' major', prettyNote(M) + '장조');
const msNames = (m, form) => spellMinor(m, form).map(prettyAny).concat([m]);
const msKeys = (m, form) => (form === 'harmonic' ? MS_HAR : MS_NAT).map(x => MS_LO[m] + x);
const msSigWords = (M) => { const k = KEY_SIGS.find(x => x.major === M); if (!k || !k.type) return t('no sharps or flats', '샵도 플랫도 없음');
  const signs = (k.type === 'sharp' ? SHARP_ORDER : FLAT_ORDER).slice(0, k.count).map(prettyNote).join(' ');
  return t(['', 'one', 'two'][k.count] + ' ' + (k.type === 'sharp' ? 'sharp' : 'flat') + (k.count > 1 ? 's' : '') + ': ' + signs, (k.type === 'sharp' ? '샵 ' : '플랫 ') + ['', '하나', '둘'][k.count] + ': ' + signs); };
const msGapWord = (n) => (n === 1 ? t('S', 'S') : n === 2 ? t('T', 'T') : t('T½', 'T½'));
const msGapLong = (n) => (n === 1 ? t('a semitone', '반음') : n === 2 ? t('a tone', '온음') : t('a tone and a half', '온음 반'));
// the scale on the staff: the key signature of its major, the raised 7th written beside its note (scMinItems)
function MsStaff({ m, form = 'harmonic', clef = 'treble', width = 330, hl = [], dir = 'up' }) {
  const dn = m === 'D' ? 7 : 14, items = scMinItems(form, dir, m).map(it => (it[0] === 'q' && clef === 'bass' ? [it[0], it[1], it[2] - dn].concat(it.slice(3)) : it));   // on the bass staff an octave or two down, within one ledger line
  return <SkgStaff items={items} k={MS_REL[m]} clef={clef} width={width} o={{ boxS: 26, D: 30, hl, ksCol: PEN_C }} label={msName(m)}/>;
}
const msBtn = { padding:'10px 14px', fontSize:14, minHeight:44 };
const msMsg = (txt, col) => <div style={{textAlign:'center',fontSize:15,fontWeight:900,color:col || 'var(--navy)',minHeight:22,lineHeight:1.35,textWrap:'balance'}}>{txt}</div>;
const msChoice = (opts, ans, picked, onPick, cols) => <div style={{display:'grid',gridTemplateColumns:'repeat(' + (cols || opts.length) + ',minmax(0,1fr))',gap:8,marginTop:10}}>{opts.map(([id, lab]) => <button key={id} className={'choice-btn' + (picked == null ? '' : id === ans ? ' good' : id === picked ? ' bad' : '')} onClick={() => onPick(id)} style={{padding:'12px 4px',fontSize:15,fontWeight:900}}>{lab}</button>)}</div>;
function msPlayScale(K, bpm, T, setAt) {
  const ix = spUpDown(8), run = spPlay(ix.map((j, s) => ({ at: s, keys: [K[j]], len: s === ix.length - 1 ? 2 : 1 })), bpm); if (!run) return;
  if (setAt) { ix.forEach((j, s) => T.at(run.ms(s), () => setAt(j))); T.at(run.ms(ix.length + 1.2), () => setAt(-1)); }
}

// ── step 1: a major or a minor third: count the half steps, then listen ──
const MS_ROOTS = [0, 2, 4, 5, 7, 9];   // C D E F G A, from middle C
const msThirdKeys = (r, q) => ({ lit: { [r]: 'cor', [r + (q === 'maj' ? 4 : 3)]: 'cor' }, up: Object.fromEntries(Array.from({ length: q === 'maj' ? 4 : 3 }, (_, i) => [r + i + 1, i + 1])) });
function msPlayThird(r, q) { const b = r + (q === 'maj' ? 4 : 3); spPlay([{ at: 0, keys: [r] }, { at: 1, keys: [b] }, { at: 2.2, keys: [r, b], len: 1.8 }], 96); }
function MsThirdPad({ onResult }) {
  const [x, setX] = useState({ r: 0, q: 'maj' }), [mys, setMys] = useState(false), [ans, setAns] = useState(null), [run, setRun] = useState(0);
  const L = (i) => ['C', 'C♯', 'D', 'E♭', 'E', 'F', 'F♯', 'G', 'G♯', 'A', 'B♭', 'B'][spPc(i)];
  const show = (q) => { setMys(false); setAns(null); setX({ r: x.r, q }); msPlayThird(x.r, q); };
  const fresh = () => { let r, q, g = 0; do { r = pick(MS_ROOTS); q = Math.random() < 0.5 ? 'maj' : 'min'; } while (r === x.r && q === x.q && g++ < 10); setX({ r, q }); setMys(true); setAns(null); msPlayThird(r, q); };
  const say = (c) => { if (!mys || ans) return; setAns(c); const ok = c === x.q; setRun(n => (ok ? n + 1 : 0)); if (onResult) onResult({ ok }); };
  const hide = mys && !ans, K = msThirdKeys(x.r, x.q), top = x.r + (x.q === 'maj' ? 4 : 3);
  return (
    <div className="try-box" style={actBox} data-ms="third">
      <div style={actTitle}>{t('Major or minor third?', '장3도? 단3도?')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>첫 음에서 셋째 음까지 반음을 세어요. <b>반음 4개는 장3도</b>, <b>반음 3개는 단3도</b>. 장음계는 장3도로, 단음계는 단3도로 시작해요.</> : <>Count the half steps from the first note up to the third. <b>Four half steps: a major third.</b> <b>Three: a minor third.</b> A major scale starts with a major third, a minor scale with a minor one.</>}</div>
      {!hide && <div style={{display:'flex',gap:6,justifyContent:'center',flexWrap:'wrap',marginBottom:8}}>{MS_ROOTS.map(r => <button key={r} className={'chip' + (r === x.r ? ' active' : '')} style={{minHeight:40,padding:'6px 12px'}} onClick={() => { setMys(false); setAns(null); setX({ r, q: x.q }); msPlayThird(r, x.q); }}>{L(r)}</button>)}</div>}
      <SpKb lo={-1} hi={17} W={24} H={70} lit={hide ? {} : K.lit} up={hide ? {} : K.up} names={hide ? null : { [x.r]: L(x.r), [top]: L(top) }} label={t('A third', '3도')}/>
      {msMsg(hide ? t('Major or minor?', '장3도일까요, 단3도일까요?') : t(L(x.r) + ' to ' + L(top) + ': ' + (x.q === 'maj' ? 'four half steps, a major third.' : 'three half steps, a minor third.'), L(x.r) + '에서 ' + L(top) + ': ' + (x.q === 'maj' ? '반음 4개, 장3도.' : '반음 3개, 단3도.')), hide ? undefined : x.q === 'min' ? BK.coral : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={msBtn} onClick={() => show('maj')}>{t('▶ Major third', '▶ 장3도')}</button>
        <button className="ghost-btn" style={msBtn} onClick={() => show('min')}>{t('▶ Minor third', '▶ 단3도')}</button>
        <button className="ghost-btn" style={msBtn} onClick={fresh}>{t('▶ Which one?', '▶ 어느 쪽?')}</button>
        {mys && <button className="ghost-btn" style={msBtn} onClick={() => msPlayThird(x.r, x.q)}>{t('♪ Again', '♪ 다시')}</button>}
      </div>
      {mys && msChoice([['maj', t('Major', '장3도')], ['min', t('Minor', '단3도')]], x.q, ans, say)}
      {ans && msMsg(ans === x.q ? t('Yes! ' + (run > 1 ? run + ' in a row.' : ''), '맞아요! ' + (run > 1 ? run + '번 연속.' : '')) : t('Count the half steps on the keys and listen again.', '건반에서 반음을 세고 다시 들어 봐요.'), ans === x.q ? BK.green : BK.coral)}
    </div>
  );
}

// ── step 2: the minor that shares a key signature: three half steps down from the major ──
function MsRelKeys({ m, k = 1.3, W = 26 }) {
  const M = MS_REL[m], top = MS_LO[m] + 3, up = { [top - 1]: 1, [top - 2]: 2, [top - 3]: 3 };
  return <SpKb lo={MS_LO[m] - 2} hi={top + 9} W={W} H={70} lit={{ [MS_LO[m]]: 'cor', [top]: 'pale' }} up={up} names={{ [MS_LO[m]]: m, [top]: prettyNote(M) }} label={msMajName(M) + ' · ' + msName(m)} k={k}/>;
}
function MsRelPad({ onResult }) {
  const [m, setM] = useState('A'), [q, setQ] = useState(null), [ans, setAns] = useState(null);
  const ask = () => { let x, g = 0; do { x = pick(MS_KEYS); } while (q && q.m === x && g++ < 10); setQ({ m: x }); setAns(null); setM(x); };
  const say = (c) => { if (!q || ans) return; setAns(c); if (onResult) onResult({ ok: c === q.m }); };
  const hide = q && !ans, M = MS_REL[m];
  return (
    <div className="try-box" style={actBox} data-ms="rel">
      <div style={actTitle}>{t('The minor key’s key signature', '단조의 조표')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>단조마다 조표가 같은 장조가 있어요: <b>나란한조</b>. 장조의 으뜸음에서 <b>반음 세 칸 아래</b>가 단조의 으뜸음이에요.</> : <>Every minor key shares its key signature with a major key: its <b>relative</b>. From the major's first note, go <b>three half steps down</b>: that is the minor's first note.</>}</div>
      {!q && spChips(MS_KEYS.map(x => [x, msName(x)]), m, setM)}
      <div style={{maxWidth:240,margin:'0 auto 6px'}}><SkgStaff items={[['sp', 6]]} k={M} width={200} full pad={[22, 16]} o={{ ...SKG_AL, ksCol: PEN_C }} label={msSigWords(M)}/></div>
      {msMsg(msSigWords(M))}
      {!hide && <MsRelKeys m={m}/>}
      {!hide && msMsg(t(msMajName(M) + ' → three half steps down → ' + m + ' minor', msMajName(M) + ' → 반음 세 칸 아래 → ' + m + '단조'), BK.coral)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={msBtn} onClick={ask}>{q && ans ? t('▶ Another', '▶ 다른 것') : t('▶ Your turn: name the minor', '▶ 내가 해보기: 단조 이름')}</button>
        {q && <button className="ghost-btn" style={msBtn} onClick={() => { setQ(null); setAns(null); }}>{t('Show all', '모두 보기')}</button>}
      </div>
      {q && msChoice(MS_KEYS.map(x => [x, msName(x)]), q.m, ans, say, 4)}
      {ans && msMsg(ans === q.m ? t('Yes: ' + msName(q.m) + ', the relative of ' + msMajName(MS_REL[q.m]) + '.', '맞아요: ' + msName(q.m) + ', ' + msMajName(MS_REL[q.m]) + '의 나란한조.') : t('This is ' + msMajName(MS_REL[q.m]) + '’s key signature: three half steps down is ' + q.m + '.', msMajName(MS_REL[q.m]) + '의 조표예요: 반음 세 칸 아래는 ' + q.m + '.'), ans === q.m ? BK.green : BK.coral)}
    </div>
  );
}

// ── step 3: the harmonic minor: the 7th goes up a half step, written beside the note ──
function MsHarPad({ onResult }) {
  const T = useSpTimers();
  const [m, setM] = useState('A'), [form, setForm] = useState('harmonic'), [clef, setClef] = useState('treble'), [at, setAt] = useState(-1), [q, setQ] = useState(false), [ans, setAns] = useState(null);
  const K = msKeys(m, form), N = msNames(m, form), Nn = msNames(m, 'natural');
  const reset = (fn) => { T.clear(); setAt(-1); setQ(false); setAns(null); fn(); };
  const say = (j) => { if (!q || ans != null) return; setAns(j); if (j === 6) setForm('harmonic'); if (onResult) onResult({ ok: j === 6 }); };
  const lit = Object.fromEntries(K.map((x, j) => [x, j === 6 && form === 'harmonic' && !q ? 'cor' : 'pale'])); if (at >= 0) lit[K[at]] = 'cor';
  return (
    <div className="try-box" style={actBox} data-ms="har">
      <div style={actTitle}>{t('The harmonic minor', '화성 단음계')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>자연 단음계는 조표 그대로. <b>화성 단음계는 7번째 음을 반음 올려요</b>. 그 샵이나 내추럴은 조표에 넣지 않고 <b>음표 옆에</b> 적어요.</> : <>The natural minor keeps to the key signature. <b>The harmonic minor raises the 7th note a half step.</b> That sharp or natural is not in the key signature: it is written <b>beside the note</b>.</>}</div>
      {spChips(MS_KEYS.map(x => [x, msName(x)]), m, (x) => reset(() => setM(x)))}
      {spChips([['natural', t('Natural', '자연')], ['harmonic', t('Harmonic', '화성')]], form, (x) => reset(() => setForm(x)))}
      {spChips([['treble', t('Treble clef', '높은음자리표')], ['bass', t('Bass clef', '낮은음자리표')]], clef, (x) => reset(() => setClef(x)))}
      <MsStaff m={m} form={q && ans == null ? 'natural' : form} clef={clef} hl={form === 'harmonic' && !(q && ans == null) ? [6] : []}/>
      <div style={{marginTop:6}}><SpKb lo={K[0]} hi={K[7]} W={30} H={70} lit={q && ans == null ? Object.fromEntries(msKeys(m, 'natural').map(x => [x, 'pale'])) : lit} names={spNameMap(q && ans == null ? msKeys(m, 'natural') : K, q && ans == null ? Nn : N)} label={msName(m)}/></div>
      {msMsg(q && ans == null ? t('In the harmonic minor, which note goes up?', '화성 단음계에서 어느 음이 올라갈까요?') : form === 'harmonic' ? t('The 7th, ' + Nn[6] + ', goes up to ' + N[6] + ', written beside the note.', '7번째 음 ' + Nn[6] + ' → ' + N[6] + ', 음표 옆에 적어요.') : t('Natural minor: just the key signature, ' + msSigWords(MS_REL[m]) + '.', '자연 단음계: 조표 그대로, ' + msSigWords(MS_REL[m]) + '.'), form === 'harmonic' && !q ? BK.coral : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={msBtn} onClick={() => { T.clear(); setQ(false); setAns(null); msPlayScale(K, 92, T, setAt); }}>{t('▶ Play it', '▶ 들어 보기')}</button>
        <button className="ghost-btn" style={msBtn} onClick={() => reset(() => { setQ(true); setForm('natural'); setM(pick(MS_KEYS.filter(x => x !== m))); })}>{t('▶ Your turn', '▶ 내가 해보기')}</button>
      </div>
      {q && msChoice(Nn.slice(0, 7).map((x, j) => [j, x]), 6, ans, say, 7)}
      {q && ans != null && msMsg(ans === 6 ? t('Yes: the 7th, ' + Nn[6] + ' → ' + msNames(m, 'harmonic')[6] + '.', '맞아요: 7번째 음, ' + Nn[6] + ' → ' + msNames(m, 'harmonic')[6] + '.') : t('Always the 7th: ' + Nn[6] + ' → ' + msNames(m, 'harmonic')[6] + '.', '언제나 7번째 음: ' + Nn[6] + ' → ' + msNames(m, 'harmonic')[6] + '.'), ans === 6 ? BK.green : BK.coral)}
    </div>
  );
}

// ── step 4: tones, semitones and the tone and a half, marked between the notes ──
const MS_GAPS = MS_HAR.slice(1).map((x, j) => x - MS_HAR[j]);   // 2 1 2 2 1 3 1
function MsGapRow({ names, gaps, got, cur }) {
  return <div style={{display:'flex',alignItems:'center',justifyContent:'center',flexWrap:'wrap',gap:2,margin:'8px 0'}}>{names.map((nm, j) => <React.Fragment key={j}>
    <span style={{minWidth:30,height:30,padding:'0 3px',boxSizing:'border-box',borderRadius:6,border:'1.5px solid ' + PEN_N,display:'inline-flex',alignItems:'center',justifyContent:'center',fontWeight:900,fontSize:nm.length > 1 ? 11.5 : 13,color:PEN_N,background:'#fff'}}>{nm}</span>
    {j < names.length - 1 && <span style={{minWidth:26,textAlign:'center',fontWeight:900,fontSize:13,color:j < got ? (gaps[j] === 3 ? PEN_C : PEN_N) : PEN_C,borderBottom:'2px solid ' + (j === cur ? PEN_C : 'transparent')}}>{j < got ? msGapWord(gaps[j]) : j === cur ? '?' : ''}</span>}
  </React.Fragment>)}</div>;
}
function MsGapPad({ onResult }) {
  const [m, setM] = useState('A'), [got, setGot] = useState(0), [bad, setBad] = useState(null), [miss, setMiss] = useState(0);
  const K = msKeys(m, 'harmonic'), N = msNames(m, 'harmonic'), done = got >= 7;
  const reset = (x) => { setM(x); setGot(0); setBad(null); setMiss(0); };
  const say = (n) => { if (done) return; if (n === MS_GAPS[got]) { const g = got + 1; setGot(g); setBad(null); playKey(K[got], 0.35); setTimeout(() => playKey(K[got + 1], 0.5), 280); if (g >= 7 && onResult) onResult({ ok: miss === 0 }); } else { setBad(n); setMiss(x => x + 1); } };
  const j = Math.min(got, 6), up = done ? {} : Object.fromEntries(Array.from({ length: MS_GAPS[j] }, (_, i) => [K[j] + i + 1, i + 1]));
  const lit = Object.fromEntries(K.map(x => [x, 'pale'])); if (!done) { lit[K[j]] = 'cor'; lit[K[j + 1]] = 'cor'; }
  return (
    <div className="try-box" style={actBox} data-ms="gaps">
      <div style={actTitle}>{t('Tone, semitone, tone and a half', '온음, 반음, 온음 반')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>이웃한 두 음 사이의 반음을 세어요: <b>1개는 반음(S)</b>, <b>2개는 온음(T)</b>, <b>3개는 온음 반(T½)</b>. 화성 단음계에는 6번째와 올라간 7번째 음 사이에 온음 반이 있어요.</> : <>Count the half steps between two neighbours: <b>one is a semitone (S)</b>, <b>two a tone (T)</b>, <b>three a tone and a half (T½)</b>. The harmonic minor has a tone and a half between the 6th and the raised 7th.</>}</div>
      {spChips(MS_KEYS.map(x => [x, msName(x)]), m, reset)}
      <MsGapRow names={N} gaps={MS_GAPS} got={got} cur={done ? -1 : got}/>
      <SpKb lo={K[0]} hi={K[7]} W={30} H={70} lit={lit} up={up} names={spNameMap(K, N)} label={msName(m) + ', ' + t('harmonic', '화성')}/>
      {msMsg(done ? t('T S T T S T½ S: the harmonic minor. ' + (miss ? '' : 'All first time!'), 'T S T T S T½ S: 화성 단음계. ' + (miss ? '' : '모두 한 번에!')) : bad != null ? t('Count the numbers on the keys: ' + MS_GAPS[got] + '.', '건반 위 숫자를 세어 봐요: ' + MS_GAPS[got] + '.') : t(N[j] + ' to ' + N[j + 1] + ': tone, semitone, or tone and a half?', N[j] + '에서 ' + N[j + 1] + ': 온음, 반음, 온음 반?'), done ? BK.green : bad != null ? BK.coral : undefined)}
      {!done && msChoice([[2, t('Tone (T)', '온음 (T)')], [1, t('Semitone (S)', '반음 (S)')], [3, t('T and a half', '온음 반')]], -9, null, say, 3)}
      {done && <div style={{textAlign:'center',marginTop:8}}><button className="ghost-btn" style={msBtn} onClick={() => reset(pick(MS_KEYS.filter(x => x !== m)))}>{t('▶ Another minor', '▶ 다른 단조')}</button></div>}
    </div>
  );
}

// ── step 5: a major or a harmonic minor scale, by ear ──
const MS_EAR = [['C', 'maj'], ['G', 'maj'], ['F', 'maj'], ['D', 'maj'], ['Bb', 'maj'], ['A', 'min'], ['E', 'min'], ['D', 'min'], ['G', 'min']];
const msEarKeys = (x) => (x[1] === 'maj' ? MS_MAJ.map(s => MS_MAJ_LO[x[0]] + s) : msKeys(x[0], 'harmonic'));
const msEarName = (x) => (x[1] === 'maj' ? msMajName(x[0]) : t(x[0] + ' harmonic minor', x[0] + ' 화성 단음계'));
function MsEarPad({ onResult }) {
  const T = useSpTimers();
  const [x, setX] = useState(null), [ans, setAns] = useState(null), [at, setAt] = useState(-1), [run, setRun] = useState(0);
  const fresh = () => { T.clear(); let y, g = 0; do { y = pick(MS_EAR); } while (x && y[0] === x[0] && y[1] === x[1] && g++ < 10); setX(y); setAns(null); msPlayScale(msEarKeys(y), 100, T, setAt); };
  const say = (c) => { if (!x || ans) return; T.clear(); setAt(-1); setAns(c); const ok = c === x[1]; setRun(n => (ok ? n + 1 : 0)); if (onResult) onResult({ ok }); };
  const K = x ? msEarKeys(x) : null;
  return (
    <div className="try-box" style={actBox} data-ms="ear">
      <div style={actTitle}>{t('Major or harmonic minor?', '장음계? 화성 단음계?')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>음계 하나가 올라갔다 내려와요. 셋째 음이 어두운가요? 꼭대기 바로 밑에 <b>넓은 걸음(온음 반)</b>이 들리나요? 그러면 화성 단음계예요.</> : <>A scale goes up and down. Is the third darker? Can you hear a <b>wide step (the tone and a half)</b> just under the top? Then it is a harmonic minor.</>}</div>
      {K && <SpKb lo={K[0]} hi={K[7]} W={30} H={70} lit={Object.fromEntries(K.map((y, j) => [y, at === j ? 'cor' : ans ? 'pale' : at >= 0 && j === at ? 'cor' : undefined]).filter(e => e[1]))} names={ans ? spNameMap(K, x[1] === 'maj' ? spellScale(x[0]).concat([x[0]]).map(prettyNote) : msNames(x[0], 'harmonic')) : null} label={t('A scale', '음계')}/>}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={msBtn} onClick={fresh}>{x && !ans ? t('▶ Another scale', '▶ 다른 음계') : t('▶ Play a scale', '▶ 음계 듣기')}</button>
        {x && <button className="ghost-btn" style={msBtn} onClick={() => { T.clear(); msPlayScale(K, 100, T, setAt); }}>{t('♪ Again', '♪ 다시')}</button>}
      </div>
      {x && msChoice([['maj', t('Major', '장음계')], ['min', t('Harmonic minor', '화성 단음계')]], x[1], ans, say, 2)}
      {ans && msMsg((ans === x[1] ? t('Yes: ', '맞아요: ') : t('It was ', '정답: ')) + msEarName(x) + (ans === x[1] && run > 1 ? t(' · ' + run + ' in a row', ' · ' + run + '번 연속') : ''), ans === x[1] ? BK.green : BK.coral)}
    </div>
  );
}

// ── the pictures on paper ──
const msPicThird = () => { const m = spMiniKeys(0, 7, { 0: 'cor', 3: 'cor' }); return { shapes: [{ k: 'raw', svg: m.svg + '<text x="' + ((m.kx(0) + m.kx(3)) / 2) + '" y="10" text-anchor="middle" font-family="Inter, sans-serif" font-size="9" font-weight="900" fill="#e4572e">1 2 3</text>' }], vb: [0, 0, m.w, 44] }; };
const msPicRel = () => ({ shapes: [{ k: 'raw', svg: '<text x="40" y="18" text-anchor="middle" font-family="Inter, sans-serif" font-size="13" font-weight="900" fill="#26296b">C ↔ A</text><text x="40" y="36" text-anchor="middle" font-family="Inter, sans-serif" font-size="11" font-weight="900" fill="#e4572e">−3</text>' }], vb: [0, 0, 80, 44] });
const msPicHar = () => { const m = spMiniKeys(-3, 9, { [-3]: 'pale', [-1]: 'pale', 0: 'pale', 2: 'pale', 4: 'pale', 5: 'pale', 8: 'cor', 9: 'pale' }); return { shapes: [{ k: 'raw', svg: m.svg }], vb: [0, 0, m.w, 44] }; };
const msPicGaps = () => ({ shapes: [{ k: 'raw', svg: '<text x="40" y="27" text-anchor="middle" font-family="Inter, sans-serif" font-size="11" font-weight="900" fill="#26296b">T S T T S <tspan fill="#e4572e">T½</tspan> S</text>' }], vb: [0, 0, 80, 44] });
const msPicEar = () => ({ shapes: [{ k: 'raw', svg: '<path d="M10 34 L22 28 L34 22 L46 16 L58 10" fill="none" stroke="#26296b" stroke-width="2"/><path d="M58 10 L68 24" fill="none" stroke="#e4572e" stroke-width="2"/>' + [10, 22, 34, 46, 58, 68].map((x, i) => '<circle cx="' + x + '" cy="' + [34, 28, 22, 16, 10, 24][i] + '" r="3.4" fill="' + (i === 5 ? '#e4572e' : '#26296b') + '"/>').join('') }], vb: [0, 0, 80, 44] });

function msLbPages(scr = false) {
  const ch = 'minor-scales';
  const checks5 = [[msPicThird(), t('I hear and see a major or a minor third', '장3도와 단3도를 듣고 알아봐요')], [msPicRel(), t('I name the minor key of a key signature: A, E, D or G minor', '조표를 보고 단조 이름을 말해요: A, E, D, G단조')],
    [msPicHar(), t('I write the harmonic minor: the 7th raised beside the note', '화성 단음계를 적어요: 7번째 음을 음표 옆에서 올려요')], [msPicGaps(), t('I mark the tones, semitones and the tone and a half', '온음, 반음, 온음 반을 표시해요')], [msPicEar(), t('I hear a major or a harmonic minor scale', '장음계와 화성 단음계를 들어서 구별해요')]];
  const pen = (x) => <PenArt shapes={x.shapes} vb={x.vb} style={{width:90}}/>;
  const toc = [[t('Major or minor third?', '장3도? 단3도?'), 2], [t('The minor key’s key signature', '단조의 조표'), 3], [t('The harmonic minor', '화성 단음계'), 4], [t('Tone, semitone, tone and a half', '온음, 반음, 온음 반'), 5], [t('Major or harmonic minor?', '장음계? 화성 단음계?'), 6], [t('My five checks', '나의 다섯 가지 확인'), 7]];
  const KC = MS_MAJ.map(x => x), KA = msKeys('A', 'natural');
  const relStill = <LbPic h={200}><div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:12,width:'100%'}}>{MS_KEYS.map(m => <div key={m}>
    <div style={{textAlign:'center',fontSize:13,fontWeight:900,color:BK.ink,marginBottom:2}}>{msMajName(MS_REL[m])} · <span style={{color:BK.coral}}>{msName(m)}</span></div>
    <div style={{maxWidth:150,margin:'0 auto'}}><SkgStaff items={[['sp', 6]]} k={MS_REL[m]} width={150} full pad={[22, 16]} o={{ ...SKG_AL, ksCol: PEN_C }}/></div></div>)}</div></LbPic>;
  return [
    <LbPage key="1" no={1} chId={ch} teacher={<>{t('The minor key on paper and by ear, as the Grade 1 theory asks: the harmonic minor scales of A, E, D and G with their key signatures, written up or down on either staff, with tones, semitones and the tone and a half marked; a major or a minor third and a major or a harmonic minor scale by ear. Chapter ' + bkChapterNo('scale-play') + ' plays A and E minor; chapter ' + bkChapterNo('key-signatures') + ' has the key signatures.', '2단계 이론이 요구하는 대로 단조를 종이와 귀로 배워요: A, E, D, G 화성 단음계를 조표와 함께 두 음자리표에 올라가거나 내려가게 적고, 온음·반음·온음 반을 표시해요. 귀로는 장3도·단3도, 장음계·화성 단음계를 구별해요. A단조와 E단조를 치는 건 ' + bkChapterNo('scale-play') + '장, 조표는 ' + bkChapterNo('key-signatures') + '장에 있어요.')}</>} qr={bkLink('drill=' + ch + '&lock=1')}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:50,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{t('Minor Scales', '단음계')}</div>
      </div></LbOnly>
      <LbPic h={200}><div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:16,width:'100%',maxWidth:640,margin:'0 auto'}}>
        <div><div style={{textAlign:'center',fontSize:13,fontWeight:900,color:BK.ink,marginBottom:2}}>{msMajName('C')}</div><SpKb lo={0} hi={12} W={26} H={66} lit={Object.fromEntries(KC.map(x => [x, 'pale']))} names={spNameMap(KC, ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C'])}/></div>
        <div><div style={{textAlign:'center',fontSize:13,fontWeight:900,color:BK.coral,marginBottom:2}}>{msName('A')}</div><SpKb lo={-3} hi={9} W={26} H={66} lit={Object.fromEntries(KA.map((x, j) => [x, j === 0 || j === 7 ? 'cor' : 'pale']))} names={spNameMap(KA, msNames('A', 'natural'))}/></div>
      </div></LbPic>
      <LbSay size={18}>{t('The same white keys, a different home: C major and A minor share a key signature. Then the minor raises its 7th.', '같은 흰건반, 다른 집: C장조와 A단조는 조표가 같아요. 그다음 단조는 7번째 음을 올려요.')}</LbSay>
      <div className="lb-toc" style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>
        <LbOnly print><div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('In this chapter', '이 챕터에서는')}</div>
          {toc.map(([n, p]) => <div key={p} className="lb-toc-row" style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:14.5,padding:'5px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkGoal(15)}{n}</span><span style={{color:BK.muted,fontWeight:800}}>{p}</span></div>)}
        </div></LbOnly>
        <div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 챕터를 마치면')}</div>
          {[t('tell a major third from a minor third', '장3도와 단3도를 구별할 수 있어요'), t('name the minor key of a key signature', '조표를 보고 단조 이름을 말할 수 있어요'), t('write a harmonic minor scale', '화성 단음계를 적을 수 있어요'), t('mark tones, semitones and the tone and a half', '온음, 반음, 온음 반을 표시할 수 있어요'), t('hear a major or a harmonic minor scale', '장음계와 화성 단음계를 들어서 구별할 수 있어요')].map(x => <div key={x} style={{display:'flex',gap:9,alignItems:'flex-start',fontSize:14.5,padding:'5px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}><span style={{flex:'0 0 auto',marginTop:3}}>{bkGoal(15)}</span><span>{x}</span></div>)}
        </div>
      </div>
      <LbOnly print><LbDrillStrip id={ch}/></LbOnly>
    </LbPage>,
    <LbPage key="2" no={2} chId={ch} kicker={t('Step 1', '1단계')} title={t('Major or minor third?', '장3도? 단3도?')}
      teacher={<>{t('Count on the keys first, then hear it: play the two notes one after the other, then together. Sing the scale\'s first three notes (do re mi, then la ti do) so the child hears where the third sits.', '먼저 건반에서 세고, 그다음 들어요: 두 음을 하나씩, 그다음 함께 쳐 주세요. 음계의 첫 세 음을 불러 보면(도 레 미, 그다음 라 시 도) 셋째 음이 어디인지 들려요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=1')}>
      <LbLive still={<LbPic h={170}><div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:16,width:'100%',maxWidth:640,margin:'0 auto'}}>{[['maj', t('C to E: a major third', 'C에서 E: 장3도')], ['min', t('A to C: a minor third', 'A에서 C: 단3도')]].map(([q, cap]) => { const r = q === 'maj' ? 0 : 9, K = msThirdKeys(r, q);
        return <div key={q}><div style={{textAlign:'center',fontSize:13,fontWeight:900,color:q === 'min' ? BK.coral : BK.ink,marginBottom:2}}>{cap}</div><SpKb lo={r - 2} hi={r + 7} W={26} H={66} lit={K.lit} up={K.up} names={{ [r]: q === 'maj' ? 'C' : 'A', [r + (q === 'maj' ? 4 : 3)]: q === 'maj' ? 'E' : 'C' }}/></div>; })}</div></LbPic>} live={<MsThirdPad/>}/>
      <LbSay>{LANG === 'ko' ? <>첫 음에서 셋째 음까지 반음을 세어요. <b>4개면 장3도</b>(C에서 E), <b>3개면 단3도</b>(A에서 C). 장음계는 장3도로, 단음계는 단3도로 시작해요. 단3도가 더 어둡게 들려요.</> : <>Count the half steps from the first note to the third. <b>Four: a major third</b> (C to E). <b>Three: a minor third</b> (A to C). A major scale starts with a major third, a minor scale with a minor third, which sounds darker.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>C와 E를 하나씩, 그다음 함께 쳐요. 사이의 반음을 세어요: 4개.</>,
        <>A와 C를 쳐요: 반음 3개. 둘을 번갈아 치며 들어 봐요.</>,
        <>선생님이 3도를 치면, 장3도인지 단3도인지 말해요.</>,
      ] : [
        <>Play C and E, one then the other, then together. Count the half steps between: four.</>,
        <>Play A and C: three half steps. Play the two thirds in turn and listen.</>,
        <>Your teacher plays a third: say major or minor.</>,
      ]}/>
      <LbRemember>{t('Four half steps: major third. Three: minor third.', '반음 4개는 장3도, 3개는 단3도.')}</LbRemember>
    </LbPage>,
    <LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={t('The minor key’s key signature', '단조의 조표')}
      teacher={<>{t('Grade 1 needs four minor keys: A (no sharps or flats), E (F♯), D (B♭) and G (B♭ and E♭). The relative minor is three half steps (and three letters) below the major\'s first note, or the 6th note of the major scale. A key signature alone does not say major or minor: the first and last notes of the piece do.', '2단계에는 단조 네 개가 나와요: A(샵·플랫 없음), E(F♯), D(B♭), G(B♭, E♭). 나란한 단조는 장조의 으뜸음에서 반음 세 칸(글자로는 세 글자) 아래, 또는 장음계의 6번째 음이에요. 조표만으로는 장조인지 단조인지 알 수 없어요: 곡의 첫 음과 끝 음이 알려 줘요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=3')}>
      <LbLive still={relStill} live={<MsRelPad/>}/>
      <LbSay>{LANG === 'ko' ? <>단조마다 <b>조표가 같은 장조</b>가 있어요: 나란한조. 장조의 으뜸음에서 <b>반음 세 칸 아래</b>로 가면 단조의 으뜸음이에요. C장조와 A단조, G장조와 E단조, F장조와 D단조, B♭장조와 G단조.</> : <>Every minor key <b>shares its key signature with a major key</b>: its relative. From the major's first note, <b>three half steps down</b> is the minor's first note. C major and A minor, G major and E minor, F major and D minor, B♭ major and G minor.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>C에서 반음 세 칸 아래로 쳐요: B, B♭, A. A단조의 으뜸음이에요.</>,
        <>G에서 세 칸 아래: E. F에서: D. B♭에서: G.</>,
        <>조표 카드를 보고 장조와 단조 이름을 둘 다 말해요.</>,
      ] : [
        <>From C, play three half steps down: B, B♭, A. That is A minor's first note.</>,
        <>From G, three down: E. From F: D. From B♭: G.</>,
        <>Look at a key signature and say both names, the major and the minor.</>,
      ]}/>
      <LbRemember>{t('Same key signature: the minor is three half steps down.', '조표가 같아요: 단조는 반음 세 칸 아래.')}</LbRemember>
    </LbPage>,
    <LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title={t('The harmonic minor', '화성 단음계')}
      teacher={<>{t('Write it with the key signature, or without it (every sharp and flat beside its note). The raised 7th is always an accidental: G♯ in A minor, D♯ in E minor, C♯ in D minor, F♯ in G minor. In G minor the F♯ appears with a key signature of two flats; in D minor the C♯ with one flat. Check that the child writes the accidental before the note, on the same line or space.', '조표를 써서 적거나, 조표 없이 적어요(샵과 플랫을 모두 음표 옆에). 올라간 7번째 음은 언제나 임시표예요: A단조 G♯, E단조 D♯, D단조 C♯, G단조 F♯. G단조에서는 플랫 두 개 조표에 F♯이, D단조에서는 플랫 하나에 C♯이 나와요. 임시표를 음표 앞, 같은 줄이나 칸에 적는지 봐 주세요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=4')}>
      <LbLive still={<LbPic h={200}><div style={{display:'flex',flexDirection:'column',gap:10,width:'100%',maxWidth:560,margin:'0 auto'}}><MsStaff m="A" form="harmonic" width={420} hl={[6]}/><MsStaff m="D" form="harmonic" clef="bass" width={420} hl={[6]}/></div></LbPic>} live={<MsHarPad/>}/>
      <LbSay>{LANG === 'ko' ? <><b>자연 단음계</b>는 조표 그대로예요. <b>화성 단음계</b>는 7번째 음을 반음 올려요. A단조는 G♯, E단조는 D♯, D단조는 C♯, G단조는 F♯. 그 기호는 조표가 아니라 <b>음표 옆</b>에 적어요.</> : <>The <b>natural minor</b> keeps to the key signature. The <b>harmonic minor</b> raises the 7th a half step: A minor G♯, E minor D♯, D minor C♯, G minor F♯. That sign goes <b>beside the note</b>, not in the key signature.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>A 화성 단음계를 쳐요: 7번째 음 G♯. 올라가고 내려와요.</>,
        <>D 화성 단음계: 조표의 B♭, 그리고 7번째 음 C♯.</>,
        <>공책에 G 화성 단음계를 적어요: 조표 B♭ E♭, F 앞에 샵.</>,
      ] : [
        <>Play A harmonic minor: the 7th is G♯. Up and back down.</>,
        <>D harmonic minor: the key signature's B♭, and the 7th, C♯.</>,
        <>Write G harmonic minor in your book: the key signature B♭ E♭, and a sharp before the F.</>,
      ]}/>
      <LbRemember>{t('Harmonic minor: raise the 7th, beside the note.', '화성 단음계: 7번째 음을 올려요, 음표 옆에.')}</LbRemember>
    </LbPage>,
    <LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title={t('Tone, semitone, tone and a half', '온음, 반음, 온음 반')}
      teacher={<>{t('Mark each step between neighbours, as the written theory asks: a curve or a bracket with T, S or T½ (any marking the child uses the same way each time). Every harmonic minor has the same pattern: T S T T S T½ S. The tone and a half is between the 6th and the raised 7th.', '이웃한 두 음 사이마다 표시해요(이론 시험처럼): 곡선이나 괄호에 T, S, T½(아이가 매번 같은 방법으로 쓰면 돼요). 화성 단음계는 모두 같은 패턴이에요: T S T T S T½ S. 온음 반은 6번째와 올라간 7번째 음 사이에 있어요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=5')}>
      <LbLive still={<LbPic h={190}><div style={{display:'flex',flexDirection:'column',gap:8,width:'100%',maxWidth:560,margin:'0 auto'}}><MsGapRow names={msNames('A', 'harmonic')} gaps={MS_GAPS} got={7} cur={-1}/><SpKb maxW={520} lo={-3} hi={9} W={36} H={74} lit={Object.fromEntries(msKeys('A', 'harmonic').map((x, j) => [x, j === 5 || j === 6 ? 'cor' : 'pale']))} up={{ 6: 1, 7: 2, 8: 3 }} names={spNameMap(msKeys('A', 'harmonic'), msNames('A', 'harmonic'))}/></div></LbPic>} live={<MsGapPad/>}/>
      <LbSay>{LANG === 'ko' ? <>이웃한 두 음 사이의 반음을 세어요. 1개는 <b>반음(S)</b>, 2개는 <b>온음(T)</b>, 3개는 <b>온음 반(T½)</b>. 화성 단음계는 언제나 <b>T S T T S T½ S</b>. 온음 반은 6번째와 올라간 7번째 음 사이에 있어요: A단조에서는 F와 G♯.</> : <>Count the half steps between neighbours. One is a <b>semitone (S)</b>, two a <b>tone (T)</b>, three a <b>tone and a half (T½)</b>. A harmonic minor is always <b>T S T T S T½ S</b>. The tone and a half sits between the 6th and the raised 7th: in A minor, F to G♯.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>A 화성 단음계를 아주 천천히 치며 걸음마다 말해요: 온, 반, 온, 온, 반, 온 반, 반.</>,
        <>F에서 G♯까지 반음 세 개를 하나씩 쳐요: F♯, G, G♯.</>,
        <>공책에 적은 G 화성 단음계에 T, S, T½를 표시해요.</>,
      ] : [
        <>Play A harmonic minor very slowly, naming each step: tone, semitone, tone, tone, semitone, tone and a half, semitone.</>,
        <>From F to G♯, play the three half steps one by one: F♯, G, G♯.</>,
        <>Mark T, S and T½ on the G harmonic minor in your book.</>,
      ]}/>
      <LbRemember>{t('Harmonic minor: T S T T S T½ S.', '화성 단음계: T S T T S T½ S.')}</LbRemember>
    </LbPage>,
    <LbPage key="6" no={6} chId={ch} kicker={t('Step 5', '5단계')} title={t('Major or harmonic minor?', '장음계? 화성 단음계?')}
      teacher={<>{t('The scale is played up and down, one octave. Two clues: the darker third near the bottom, and the wide step (the tone and a half) just under the top. Play the same tonic both ways (C major, then C harmonic minor) before mixing keys.', '음계를 한 옥타브 올라갔다 내려와요. 단서는 둘: 아래쪽의 더 어두운 셋째 음, 그리고 꼭대기 바로 밑의 넓은 걸음(온음 반). 조를 섞기 전에 같은 으뜸음으로 두 가지를 쳐 주세요(C장조, 그다음 C 화성 단음계).')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=6')}>
      <LbLive still={<LbPic h={180}><div style={{display:'flex',flexDirection:'column',gap:12,width:'100%',maxWidth:560,margin:'0 auto'}}>{[['C', 'maj'], ['A', 'min']].map(x => <div key={x[0]}><div style={{fontSize:13,fontWeight:900,color:x[1] === 'min' ? BK.coral : BK.ink,textAlign:'center'}}>{msEarName(x)}</div><MsGapRow names={x[1] === 'maj' ? ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C'] : msNames('A', 'harmonic')} gaps={x[1] === 'maj' ? [2, 2, 1, 2, 2, 2, 1] : MS_GAPS} got={7} cur={-1}/></div>)}</div></LbPic>} live={<MsEarPad/>}/>
      <LbSay>{LANG === 'ko' ? <>음계를 들어요. <b>셋째 음이 어둡고</b>, 꼭대기 바로 밑에 <b>넓은 걸음</b>이 있으면 화성 단음계예요. 밝은 셋째 음에 고른 걸음이면 장음계.</> : <>Listen to a scale. A <b>darker third</b> and a <b>wide step</b> just under the top: a harmonic minor. A bright third and even steps: a major scale.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>C장조, 그다음 C 화성 단음계(E♭, A♭, B)를 쳐요. 어디가 다른지 들어 봐요.</>,
        <>선생님이 음계를 치면, 장음계인지 화성 단음계인지 말해요.</>,
        <>이번엔 내가 치고, 선생님이 맞혀요.</>,
      ] : [
        <>Play C major, then C harmonic minor (E♭, A♭, B). Listen for what changes.</>,
        <>Your teacher plays a scale: say major or harmonic minor.</>,
        <>Now you play, and your teacher guesses.</>,
      ]}/>
      <LbRemember>{t('A darker third and a wide step near the top: harmonic minor.', '어두운 셋째 음과 꼭대기 밑의 넓은 걸음: 화성 단음계.')}</LbRemember>
    </LbPage>,
    <LbPage key="7" no={7} chId={ch} kicker={t('Check-up', '점검')} title={t('My five checks', '나의 다섯 가지 확인')}
      teacher={<>{t('The written checks on paper (key signatures, the scale with its raised 7th, the T S marks); the two by ear at the piano.', '쓰는 점검은 종이에(조표, 7번째 음을 올린 음계, T·S 표시), 듣는 점검 두 개는 피아노 앞에서.')}</>}>
      <LbSay>{t('Tick each one: not yet, nearly, or got it!', '하나씩 표시해요: 아직, 거의, 됐어요!')}</LbSay>
      <LbLive still={<LbStageRows big rows={checks5.map(([a, txt]) => [pen(a), txt])}/>} live={<FiveChecks376 rows={checks5} storeKey="pb_ms_five"/>}/>
    </LbPage>,
  ];
}
function MinorScalesLessonBook() { return <>{msLbPages(false)}</>; }
function MsLearn({ onStart }) {
  const pages = msLbPages(true), opener = pages[0];
  return (
    <Lesson id="minor-scales" title={t('Minor scales', '단음계')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="minor-scales"><div className="lb-screen lb-open" style={{display:'flex',flexDirection:'column',gap:12,margin:'0 0 8px'}}>{lbWordsFirst(opener.props.children)}</div></BkChapterCtx.Provider></LbScreenCtx.Provider>}>
      {pages.slice(1).map((pg, i) => <Step key={i} title={pg.props.title}><LbScreenPage page={pg}/></Step>)}
    </Lesson>
  );
}

// ── the drill ──
const MS_LEVELS = [
  { n: 1, label: 'Major or minor third?', kind: 'third', time: 10 },
  { n: 2, label: 'Listen: major or minor third?', kind: 'earThird', time: 12, noPrint: true },
  { n: 3, label: 'Name the minor key', kind: 'rel', time: 10 },
  { n: 4, label: 'Harmonic minor: the raised 7th', kind: 'raise', time: 12 },
  { n: 5, label: 'Tone, semitone or tone and a half?', kind: 'gap', time: 12 },
  { n: 6, label: 'Listen: major or harmonic minor?', kind: 'earScale', time: 16, noPrint: true },
];
Object.assign(LEVEL_KO, { 'Major or minor third?': '장3도? 단3도?', 'Listen: major or minor third?': '듣기: 장3도? 단3도?', 'Name the minor key': '단조 이름', 'Harmonic minor: the raised 7th': '화성 단음계: 올라간 7번째 음', 'Tone, semitone or tone and a half?': '온음? 반음? 온음 반?', 'Listen: major or harmonic minor?': '듣기: 장음계? 화성 단음계?' });
function genMsQuestion(lv, prev) {
  const uid = Math.random(), kind = lv.kind;
  if (kind === 'third' || kind === 'earThird') { let r, q, g = 0; do { r = pick(MS_ROOTS); q = Math.random() < 0.5 ? 'maj' : 'min'; } while (prev && prev.r === r && prev.answer === q && g++ < 10); return { kind, r, answer: q, choices: ['maj', 'min'], key: r + q, uid }; }
  if (kind === 'rel') { let m, g = 0; do { m = pick(MS_KEYS); } while (prev && prev.answer === m && g++ < 10); return { kind, answer: m, choices: MS_KEYS.slice(), key: m, uid }; }
  if (kind === 'raise') { let m, g = 0; do { m = pick(MS_KEYS); } while (prev && prev.m === m && g++ < 10); const H = msNames(m, 'harmonic'), ans = H[6], pool = shuffle(['G♯', 'D♯', 'C♯', 'F♯', 'B♭', 'E♭'].filter(x => x !== ans)).slice(0, 3);
    return { kind, m, answer: ans, choices: shuffle([ans].concat(pool)), key: m, uid }; }
  if (kind === 'gap') { let m, j, g = 0; do { m = pick(MS_KEYS); j = Math.floor(Math.random() * 7); } while (prev && prev.m === m && prev.j === j && g++ < 10); return { kind, m, j, answer: MS_GAPS[j], choices: [2, 1, 3], key: m + j, uid }; }
  let x, g = 0; do { x = pick(MS_EAR); } while (prev && prev.x && prev.x[0] === x[0] && prev.x[1] === x[1] && g++ < 10);
  return { kind: 'earScale', x, answer: x[1], choices: ['maj', 'min'], key: x.join(''), uid };
}
const MS_WORD = { maj: () => t('Major', '장'), min: () => t('Minor', '단') };
function msAnswerLabel(q) {
  if (q.kind === 'third' || q.kind === 'earThird') return q.answer === 'maj' ? t('major third', '장3도') : t('minor third', '단3도');
  if (q.kind === 'rel') return msName(q.answer);
  if (q.kind === 'raise') return q.answer;
  if (q.kind === 'gap') return msGapLong(q.answer);
  return q.answer === 'maj' ? t('major', '장음계') : t('harmonic minor', '화성 단음계');
}
function MsQuestion({ q, given, locked, onAnswer, pixel }) {
  const T = useSpTimers(), [at, setAt] = useState(-1), done = !!given, heard = q.kind === 'earThird' || q.kind === 'earScale';
  const play = () => { T.clear(); setAt(-1); if (q.kind === 'earThird') msPlayThird(q.r, q.answer); else if (q.kind === 'earScale') msPlayScale(msEarKeys(q.x), 100, T, setAt); };
  useEffect(() => { if (!heard) return; const id = setTimeout(play, 350); return () => { clearTimeout(id); T.clear(); }; }, [q.uid]);
  const btnCls = pixel ? 'pixel-choice' : 'choice-btn', cls = (c) => btnCls + (!done ? '' : c === q.answer ? ' good' : given.ans === c ? ' bad' : '');
  let title, fig = null, label = (c) => c;
  if (q.kind === 'third' || q.kind === 'earThird') { const K = msThirdKeys(q.r, q.answer), show = q.kind === 'third' || done;
    title = q.kind === 'third' ? t('Count the half steps: a major or a minor third?', '반음을 세어요: 장3도일까요, 단3도일까요?') : t('Listen: a major or a minor third?', '들어 봐요: 장3도일까요, 단3도일까요?');
    fig = <SpKb lo={-1} hi={17} W={22} H={64} lit={show ? K.lit : {}} up={done ? K.up : {}}/>; label = (c) => (c === 'maj' ? t('Major third', '장3도') : t('Minor third', '단3도')); }
  else if (q.kind === 'rel') { const M = MS_REL[q.answer];
    title = t('This key signature belongs to a major key and a minor key. Which minor?', '이 조표는 장조 하나와 단조 하나의 것이에요. 어느 단조일까요?');
    fig = <div style={{maxWidth:220,margin:'0 auto'}}><SkgStaff items={[['sp', 6]]} k={M} width={200} full pad={[22, 16]} o={{ ...SKG_AL, ksCol: PEN_C }} label={msSigWords(M)}/></div>; label = (c) => msName(c); }
  else if (q.kind === 'raise') { title = t(q.m + ' harmonic minor: which note is the raised 7th?', q.m + ' 화성 단음계: 올라간 7번째 음은 무엇일까요?');
    fig = <MsStaff m={q.m} form={done ? 'harmonic' : 'natural'} hl={done ? [6] : []}/>; }
  else if (q.kind === 'gap') { const N = msNames(q.m, 'harmonic'), K = msKeys(q.m, 'harmonic');
    title = t(q.m + ' harmonic minor: from ' + N[q.j] + ' to ' + N[q.j + 1] + ', a tone, a semitone, or a tone and a half?', q.m + ' 화성 단음계: ' + N[q.j] + '에서 ' + N[q.j + 1] + '까지, 온음, 반음, 온음 반?');
    fig = <SpKb lo={K[0]} hi={K[7]} W={28} H={66} lit={{ [K[q.j]]: 'cor', [K[q.j + 1]]: 'cor' }} names={spNameMap(K, N)} up={done ? Object.fromEntries(Array.from({ length: q.answer }, (_, i) => [K[q.j] + i + 1, i + 1])) : {}}/>; label = (c) => msGapLong(c); }
  else { const K = msEarKeys(q.x); title = t('Listen: a major scale, or a harmonic minor?', '들어 봐요: 장음계일까요, 화성 단음계일까요?');
    fig = <SpKb lo={K[0]} hi={K[7]} W={28} H={66} lit={at >= 0 ? { [K[at]]: 'cor' } : {}} names={done ? spNameMap(K, q.x[1] === 'maj' ? spellScale(q.x[0]).concat([q.x[0]]).map(prettyNote) : msNames(q.x[0], 'harmonic')) : null}/>; label = (c) => (c === 'maj' ? t('Major', '장음계') : t('Harmonic minor', '화성 단음계')); }
  const why = !done ? null : q.kind === 'third' || q.kind === 'earThird' ? t(q.answer === 'maj' ? 'Four half steps: a major third.' : 'Three half steps: a minor third.', q.answer === 'maj' ? '반음 4개: 장3도.' : '반음 3개: 단3도.')
    : q.kind === 'rel' ? t(msMajName(MS_REL[q.answer]) + '’s key signature; three half steps down: ' + q.answer + ' minor.', msMajName(MS_REL[q.answer]) + '의 조표, 반음 세 칸 아래: ' + q.answer + '단조.')
    : q.kind === 'raise' ? t('The 7th, ' + msNames(q.m, 'natural')[6] + ', goes up a half step: ' + q.answer + '.', '7번째 음 ' + msNames(q.m, 'natural')[6] + '이 반음 올라가요: ' + q.answer + '.')
    : q.kind === 'gap' ? t('T S T T S T½ S: this step is ' + msGapLong(q.answer) + '.', 'T S T T S T½ S: 이 걸음은 ' + msGapLong(q.answer) + '.')
    : t('It was ' + msEarName(q.x) + '.', '정답: ' + msEarName(q.x) + '.');
  const cols = q.choices.length;
  return (<div>
    <p style={pixel ? {fontSize:11.5,textAlign:'center'} : {fontSize:15,fontWeight:700,textAlign:'center',margin:'0 0 8px',color:'var(--muted)',textWrap:'balance'}}>{title}</p>
    {heard && <div style={{textAlign:'center',marginBottom:10}}><button className={pixel ? 'pixel-btn' : 'ghost-btn'} style={{minHeight:44}} onClick={play}>{t('▶ Play it again', '▶ 다시 듣기')}</button></div>}
    <div style={{marginBottom:12}}>{fig}</div>
    <div style={{display:'grid',gridTemplateColumns:'repeat(' + cols + ',minmax(0,1fr))',gap:8}}>{q.choices.map(c => <button key={c} disabled={locked} className={cls(c)} style={{padding:pixel ? '14px 4px' : '12px 4px',fontSize:pixel ? 9.5 : 15,fontWeight:900}} onClick={() => { if (locked || done) return; T.clear(); setAt(-1); onAnswer(c); }}>{label(c)}</button>)}</div>
    {why && !pixel && <div style={{marginTop:10,fontSize:13.5,color:'#4a4d86',background:'#fff',borderRadius:8,padding:'7px 10px',lineHeight:1.45}}>{why}</div>}
  </div>);
}
Object.assign(MINOR_SCALES_DRILL, { levels: MS_LEVELS, generate: genMsQuestion, check: (q, ans) => ans !== null && ans !== undefined && ans === q.answer, answerLabel: msAnswerLabel, Question: MsQuestion, Learn: MsLearn });
