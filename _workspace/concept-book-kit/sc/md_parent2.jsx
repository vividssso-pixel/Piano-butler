// 6: find the parent major. First the one she knows (the relative minor), then count back for any mode.
const MD_STEPS = [
  { st: 5, par: 'C', show: 'mode' }, { st: 5, par: 'C', show: 'parent' }, { st: 1, par: 'D', show: 'mode' }, { st: 1, par: 'D', show: 'parent' }, { st: 1, par: 'D', show: 'all' },
];
const MD_Q = [[5, 'C'], [5, 'G'], [1, 'C'], [1, 'D'], [4, 'C'], [3, 'D'], [2, 'F'], [6, 'G'], [4, 'E'], [1, 'A']];
function MdParent() {
  const [view, setView] = useState('one'), [s, setS] = useState(0), [q, setQ] = useState(0), [bad, setBad] = useState(null), [ok, setOk] = useState(false), P = useScPlay([view, s, q]);
  let body;
  if (view === 'one') {
    const S = MD_STEPS[s], m = MODES[S.st], K = scModeK(S.par, S.st), N = scModeNames(S.par, S.st), PK = scModeK(S.par, 0), PN = scModeNames(S.par, 0), R = prettyAny(N[0]), pr = prettyNote(S.par);
    const back = PN.slice(0, S.st + 1).map((n, j) => prettyAny(n) + ' (' + (j + 1) + ')').reverse().join(', ');
    const lines = [
      t('You already know this one. A minor has the very same notes as C major. A minor is the Aeolian mode.', '이건 이미 알아요. A단조는 C장조와 음이 똑같아요. A단조가 에올리안 선법이에요.'),
      t('Aeolian is the 6th mode, so A is the 6th note of its parent. Count back: ' + back + '. The parent is C major.', '에올리안은 6번째 선법이라 A가 부모의 6번째 음이에요. 거꾸로 세요: ' + back + '. 부모는 C장조예요.'),
      t('Now the same trick with Dorian, the 2nd mode: E Dorian. E must be the 2nd note of its parent.', '이제 2번째 선법 도리안으로 같은 방법을 써요: E 도리안. E는 부모의 2번째 음이어야 해요.'),
      t('Count back: ' + back + '. The parent is D major.', '거꾸로 세요: ' + back + '. 부모는 D장조예요.'),
      t('So E Dorian has the notes of D major, started on E. The rule for every mode: its number is which note of the parent the home is.', '그래서 E 도리안은 D장조의 음을 E에서 시작한 거예요. 모든 선법의 규칙: 선법의 번호는 집이 부모의 몇 번째 음인지예요.'),
    ];
    let ks, marks = {}, names = {};
    if (S.show === 'mode') { const X = mdPic(K, N, -1); ks = K; marks = X.marks; names = X.names; }
    else { ks = PK; PK.forEach((k, j) => { marks[k] = j === 0 || j === 7 ? 'target' : j === S.st ? 'pick' : 'pass'; names[k] = prettyAny(PN[j]); }); }
    body = <>
      <div style={scS.title}>{t('Find the parent major', '부모 장조 찾기')}</div>
      <div style={scS.line}>{lines[s]}</div>
      <div style={{ textAlign: 'center', fontFamily: "'Playfair Display', Georgia, serif", fontSize: 20, fontWeight: 900, color: '#26296b', marginBottom: 4 }}>{S.show === 'mode' ? R + ' ' + mdNm(m) : pr + ' ' + t('major', '장조')}</div>
      <ScKeys ks={ks} marks={marks} names={names} arcs={[]} nonce={'p' + s}/>
      {scRow(<>
        <button className="ghost-btn" style={scS.back} onClick={() => setS(Math.max(0, s - 1))}>{t('← Back', '← 이전')}</button>
        <button className="ghost-btn" style={scS.prim} onClick={() => { if (s === MD_STEPS.length - 1) { setView('try'); setQ(0); setBad(null); setOk(false); } else setS(s + 1); }}>{s === MD_STEPS.length - 1 ? t('Your turn →', '내가 해보기 →') : t('Next →', '다음 →')}</button>
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
        <button className="ghost-btn" style={scS.back} onClick={() => { setView('one'); setS(MD_STEPS.length - 1); }}>{t('← Back', '← 이전')}</button>
        {ok && <button className="ghost-btn" style={scS.prim} onClick={() => { setQ((q + 1) % MD_Q.length); setBad(null); setOk(false); }}>{t('Another →', '다른 것 →')}</button>}
      </>)}
    </>;
  }
  return scBox('modes', body);
}

