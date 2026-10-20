import sys
a, b = sys.argv[1], sys.argv[2]
s = open(a, encoding='utf-8').read()
def rep(x, y, n=1):
    global s
    assert s.count(x) == n, (s.count(x), x[:80])
    s = s.replace(x, y)

NEW = r'''
// ── Scales, lesson 12: the modes. A mode is the major scale started on another of its own notes. Facts: the MODES table (her material). ──
const SC_MP = [0, 2, 4, 5, 7, 9, 11];
function scModeK(parent, st) {
  const root = SCALES[parent].rootPc; let K = [];
  for (let j = st; j <= st + 7; j++) K.push(root + SC_MP[j % 7] + 12 * Math.floor(j / 7));
  while (K[0] >= 12) K = K.map(x => x - 12);
  return K;
}
const scModeNames = (parent, st) => { const sp = spellScale(parent), r = Array.from({ length: 7 }, (_, i) => sp[(st + i) % 7]); return r.concat([r[0]]); };
function ScModes() {
  const [view, setView] = useState('all'), [stf, setStf] = useState(false);   // 'all' -> 'one' -> 'try'
  const [i, setI] = useState(0), [parent, setParent] = useState('C'), [nonce, setNonce] = useState(0);
  const [tm, setTm] = useState(1), [at, setAt] = useState(0), [bad, setBad] = useState(null);
  const P = useScPlay([view, i, parent]);
  const timers = useRef([]);
  const clear = () => { timers.current.forEach(clearTimeout); timers.current = []; };
  useEffect(() => clear, []);
  const title = t('The seven modes', '일곱 가지 선법');
  const staffOf = (par, st, K) => {
    const nm = scModeNames(par, st), d0 = nm[0][0] === 'B' ? 27 : 28 + STAFF_LETTERS.indexOf(nm[0][0]), items = Array.from({ length: 8 }, (_, j) => ['q', 1, d0 + j]).concat([['||']]), hl = skgOf(items, par, n => n.byKey);
    return <SkgStaff key={par + st} items={items} k={par} width={330} o={{ boxS: 26, D: 30, hl2: hl, underAlt: hl, ksCol: '#2e8a6e', ...skgUnder(items, par, null, []) }}/>;
  };
  const picture = (par, st, an) => { const K = scModeK(par, st), N = scModeNames(par, st).map(prettyAny), marks = {}, names = {}; K.forEach((k, j) => { marks[k] = j === 0 || j === 7 ? 'target' : 'pass'; names[k] = N[j]; }); if (an >= 0) marks[K[an]] = 'pick'; return { K, marks, names }; };
  let body;
  if (view === 'all') {
    const M = picture('C', 0, -1);
    body = <>
      <div style={scS.title}>{title}</div>
      <div style={scS.line}>{t('A mode is the major scale started on another of its own notes: the same notes, the same key signature, a new home.', '선법은 장음계를 자기 안의 다른 음에서 시작한 거예요: 음도 조표도 같고, “집”만 달라요.')}</div>
      <ScKeys ks={M.K} marks={M.marks} names={M.names} arcs={[]} nonce="all"/>
      <div style={{display:'flex',flexWrap:'wrap',gap:5,justifyContent:'center',maxWidth:330,margin:'8px auto 0'}}>
        {MODES.map((m, j) => <span key={m.name} style={{padding:'4px 9px',borderRadius:999,border:'1.5px solid #d8cfb6',background:'#efeadc',fontSize:12.5,fontWeight:800,color:'#26296b'}}>{j + 1} {LANG === 'ko' ? m.nameKo : m.name}</span>)}
      </div>
      {scRow(<button className="ghost-btn" style={scS.prim} onClick={() => { setView('one'); setI(0); setNonce(n => n + 1); }}>{t('One by one →', '하나씩 →')}</button>)}
    </>;
  } else if (view === 'one') {
    const m = MODES[i], an = P.an, M = picture(parent, m.start, an), nm = scModeNames(parent, m.start);
    body = <>
      <div style={scS.title}>{LANG === 'ko' ? m.nameKo + ' (' + m.name + ')' : m.name} {t('on', '')} {prettyAny(nm[0])}{LANG === 'ko' ? '에서' : ''}</div>
      <div style={scS.line}>{t(m.formula, m.formulaKo)}. {t(m.mood, m.moodKo)}</div>
      <ScKeys ks={M.K} marks={M.marks} names={M.names} arcs={[]} nonce={nonce + ':' + i + parent}/>
      <div style={{textAlign:'center',fontSize:13,fontWeight:700,color:'#4a4d86',fontStyle:'italic',margin:'6px 0'}}>{t(m.exEn, m.exKo)}</div>
      <div style={{display:'grid',gridTemplateColumns:'repeat(5,minmax(0,1fr))',gap:5,maxWidth:330,margin:'6px auto'}}>
        {MODE_PARENTS.map(k => <button key={k} className={'chip' + (parent === k ? ' active' : '')} aria-pressed={parent === k} style={{...KF_BTN,minHeight:38,padding:'0 2px'}} onClick={() => { setParent(k); setNonce(n => n + 1); }}>{scKeyBtn(k)}</button>)}
      </div>
      <div style={{textAlign:'center',fontSize:12.5,fontWeight:700,color:'var(--muted)'}}>{t('Notes of ' + prettyNote(parent) + ' major, started on ' + prettyAny(nm[0]) + '.', prettyNote(parent) + ' 장음계의 음을 ' + prettyAny(nm[0]) + '에서 시작해요.')}</div>
      <ScStaffBtn on={stf} set={setStf}/>
      {stf && <>{staffOf(parent, m.start)}<div style={{textAlign:'center',fontSize:12.5,fontWeight:700,color:'#6d6f9c',marginTop:4}}>{t('Green: from the key signature of ' + prettyNote(parent) + ' major.', '초록: ' + prettyNote(parent) + ' 장조의 조표에 있는 음.')}</div></>}
      {scRow(<>
        <button className="ghost-btn" style={scS.back} onClick={() => { if (i === 0) setView('all'); else setI(i - 1); setNonce(n => n + 1); }}>{t('← Back', '← 이전')}</button>
        <button className="ghost-btn" style={scS.back} onClick={() => P.play(M.K)}>{t('▶ Hear it', '▶ 듣기')}</button>
        <button className="ghost-btn" style={scS.prim} onClick={() => { if (i === 6) { setView('try'); setTm(1); setAt(0); setBad(null); } else setI(i + 1); setNonce(n => n + 1); }}>{i === 6 ? t('Your turn →', '내가 해보기 →') : t('Next →', '다음 →')}</button>
      </>)}
    </>;
  } else {
    const m = MODES[tm], K = scModeK('C', m.start), N = scModeNames('C', m.start).map(prettyAny), done = at >= 7, marks = {}, names = {}, arcs = [];
    for (let j = 0; j <= at; j++) { marks[K[j]] = j === at && !done ? 'pick' : j === 0 ? 'target' : 'pass'; names[K[j]] = N[j]; }
    if (bad != null) marks[bad] = 'bad';
    const line = done ? t('That is ' + m.name + ' on ' + N[0] + '. Same notes as C major.', LANG === 'ko' ? m.nameKo + ' (' + m.name + ') ' + N[0] + '에서예요. C장조와 같은 음이에요.' : '')
      : bad != null ? t('Not that key. These are the notes of C major, started on ' + N[0] + ': after ' + N[at] + ' comes ' + N[at + 1] + '.', '그 건반이 아니에요. C장조의 음을 ' + N[0] + '에서 시작해요: ' + N[at] + ' 다음은 ' + N[at + 1] + '이에요.')
      : at === 0 ? t('Play ' + m.name + ' on ' + N[0] + ': the white keys of C major, started on ' + N[0] + '. Start on ' + N[0] + ', then tap ' + N[1] + '.', m.nameKo + ' (' + m.name + ') ' + N[0] + '에서: C장조의 흰건반을 ' + N[0] + '에서 시작해요. ' + N[0] + '에서 시작해서 ' + N[1] + '을 눌러요.')
      : t('From ' + N[at] + ', tap the next white key: ' + N[at + 1] + '.', N[at] + ' 다음 흰건반 ' + N[at + 1] + '을 눌러요.');
    const tap = (k) => { if (done) return; clear(); if (k === K[at + 1]) { setBad(null); setAt(at + 1); setNonce(n => n + 1); playKey(k, 0.5); } else if (at === 0 && k === K[0]) { setAt(0); playKey(k, 0.5); } else { setBad(k); playKey(k, 0.4); timers.current.push(setTimeout(() => setBad(null), 1100)); } };
    body = <>
      <div style={scS.title}>{t('Your turn', '내가 해보기')}</div>
      <div style={scS.line}>{line}</div>
      <ScKeys ks={K} marks={at === 0 ? { ...marks, [K[0]]: 'pick' } : marks} names={names} arcs={arcs} nonce={nonce + ':' + tm} onTap={tap}/>
      {scRow(<>
        <button className="ghost-btn" style={scS.back} onClick={() => { clear(); setView('one'); setI(6); setNonce(n => n + 1); }}>{t('← Back', '← 이전')}</button>
        {done && <button className="ghost-btn" style={scS.prim} onClick={() => { setTm(1 + (tm % 6)); setAt(0); setBad(null); setNonce(n => n + 1); }}>{t('Another →', '다른 것 →')}</button>}
      </>)}
    </>;
  }
  return scBox('modes', body);
}
'''
rep("\nconst scDirTag = (dn) =>", NEW + "\nconst scDirTag = (dn) =>")
rep("'sc-chrom', 'sc-min'], check: 'scales'", "'sc-chrom', 'sc-min', 'sc-modes'], check: 'scales'")
rep("tryLine: ['Eleven short lessons: the shape, fingering, all twelve keys, the minor scales', '열한 개의 짧은 레슨: 모양, 손가락, 열두 조, 단음계'],",
    "tryLine: ['Twelve short lessons: the shape, fingering, all twelve keys, the minor scales, the modes', '열두 개의 짧은 레슨: 모양, 손가락, 열두 조, 단음계, 선법'],")
rep("'Natural, harmonic and melodic, shown on A.', 'A에서 보는 자연, 화성, 가락.', ScMinor]].forEach",
    "'Natural, harmonic and melodic, shown on A.', 'A에서 보는 자연, 화성, 가락.', ScMinor],\n ['sc-modes', 'The seven modes', '일곱 가지 선법', 'The major scale started on another of its notes.', '장음계를 다른 음에서 시작해요.', ScModes]].forEach")
open(b, 'w', encoding='utf-8').write(s); print('ok')
