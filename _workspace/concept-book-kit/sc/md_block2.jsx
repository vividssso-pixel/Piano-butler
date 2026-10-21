
// ─── Modes, finer steps (her answer 2026-10-21: all four were unclear). Order on Home:
// 1 md-home (which note feels like home), 2 md-start (a new home, heard with the home held), 3 sc-modes (the seven names),
// 4 md-family (the 3rd: major- or minor-sounding), 5 md-ladder (bright to dark, one note at a time), 6 md-parent (count back, starting from the relative minor she knows),
// 7 md-keys (the shape travels to any home note). Theory in 4, 5 and 7 is mine, derived from the MODES table and spellScale: flagged for her review.
const mdHold = (P, K) => { P.play(K); playKey(K[0] - 12, 7); };

function MdHome() {
  const [stop, setStop] = useState(-1), [nonce, setNonce] = useState(0), P = useScPlay([stop, nonce]);
  const K = scModeK('C', 0), N = scModeNames('C', 0), names = {}, marks = {};
  K.forEach((k, j) => { names[k] = N[j]; marks[k] = 'pass'; });
  if (stop >= 0) marks[K[stop]] = 'target';
  const tap = (k) => { const j = K.indexOf(k); if (j < 0) return; setStop(j); setNonce(n => n + 1); setTimeout(() => P.play(K.slice(0, j + 1), 420), 30); };
  const line = stop < 0 ? t('Tap a white key. The C major scale plays up and stops on it.', '흰건반을 눌러 보세요. C장조 음계가 올라가다가 그 음에서 멈춰요.')
    : stop === 7 || stop === 0 ? t('Stopped on C. It feels finished: the tune can rest here. This is home.', 'C에서 멈췄어요. 끝난 느낌이 들죠: 여기서 쉴 수 있어요. 이게 “집”이에요.')
    : t('Stopped on ' + N[stop] + '. Does it feel finished, or does it want to go on? Now tap the top C and listen again.', N[stop] + '에서 멈췄어요. 끝난 느낌이에요, 아니면 더 가고 싶나요? 이제 맨 위 C를 눌러서 다시 들어 보세요.');
  return scBox('modes', <>
    <div style={scS.title}>{t('Which note feels like home?', '어느 음이 “집”처럼 느껴져요?')}</div>
    <div style={scS.line}>{line}</div>
    <ScKeys ks={K} marks={marks} names={names} arcs={[]} nonce={'h' + nonce} onTap={tap}/>
    <div style={{ textAlign: 'center', fontSize: 13, fontWeight: 700, color: '#4a4d86', margin: '8px 0 0' }}>{t('The note a tune feels finished on is its home note. In a major scale it is the first note.', '곡이 끝난 느낌으로 쉬는 음이 그 곡의 “집”이에요. 장음계에서는 첫 번째 음이에요.')}</div>
  </>);
}

// 4: the 3rd decides the family
function MdFamily() {
  const [view, setView] = useState('one'), [st, setSt] = useState(0), [q, setQ] = useState(1), [bad, setBad] = useState(false), [ok, setOk] = useState(false), P = useScPlay([view, st, q]);
  const fam = (s) => scModeK('C', s)[2] - scModeK('C', s)[0] === 4 ? 'maj' : 'min';
  let body;
  if (view === 'one') {
    const K = scModeK('C', st), N = scModeNames('C', st), m = MODES[st], M = mdPic(K, N, P.an), gap = K[2] - K[0], f = fam(st);
    M.marks[K[2]] = 'pick';
    body = <>
      <div style={scS.title}>{t('The 3rd decides the family', '3번째 음이 계열을 정해요')}</div>
      <div style={scS.line}>{t('From the home note ' + N[0] + ' to the 3rd note ' + N[2] + ' is ' + gap + ' half steps: ' + (f === 'maj' ? 'the major sound.' : 'the minor sound.'), '집 ' + N[0] + '에서 3번째 음 ' + N[2] + '까지는 반음 ' + gap + '개: ' + (f === 'maj' ? '장조 소리예요.' : '단조 소리예요.'))}</div>
      <div style={{ textAlign: 'center', fontFamily: "'Playfair Display', Georgia, serif", fontSize: 20, fontWeight: 900, color: '#26296b', marginBottom: 4 }}>{N[0]} {mdNm(m)}</div>
      <ScKeys ks={K} marks={M.marks} names={M.names} arcs={[[K[0], K[2], false, '#c0431f']]} nonce={'f' + st}/>
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(2,minmax(0,1fr))', gap: 8, maxWidth: 340, margin: '10px auto 0' }}>
        {[['maj', t('Major family: 4 half steps', '장조 계열: 반음 4개'), [0, 3, 4]], ['min', t('Minor family: 3 half steps', '단조 계열: 반음 3개'), [1, 2, 5, 6]]].map(([id, lab, list]) => <div key={id} style={{ border: '1.5px solid ' + (f === id ? '#e4572e' : 'rgba(38,41,107,0.14)'), background: f === id ? '#fbe3da' : '#fff', borderRadius: 12, padding: '6px 6px 8px', textAlign: 'center' }}>
          <div style={{ fontSize: 11.5, fontWeight: 900, color: '#c0431f', marginBottom: 4 }}>{lab}</div>
          <div style={{ display: 'flex', flexWrap: 'wrap', gap: 4, justifyContent: 'center' }}>{list.map(s => <button key={s} className={'chip' + (st === s ? ' active' : '')} aria-pressed={st === s} style={{ ...KF_BTN, minHeight: 32, padding: '0 7px', fontSize: 12 }} onClick={() => setSt(s)}>{mdNm(MODES[s])}</button>)}</div>
        </div>)}
      </div>
      {scRow(<>
        <button className="ghost-btn" style={scS.back} onClick={() => mdHold(P, K)}>{t('▶ Hear it', '▶ 듣기')}</button>
        <button className="ghost-btn" style={scS.prim} onClick={() => { setView('try'); setQ(1); setBad(false); setOk(false); }}>{t('Your turn →', '내가 해보기 →')}</button>
      </>)}
    </>;
  } else {
    const ORD = [1, 3, 5, 2, 4, 6, 0], s = ORD[(q - 1) % 7], K = scModeK('C', s), N = scModeNames('C', s), m = MODES[s], gap = K[2] - K[0], f = fam(s), M = mdPic(K, N, -1);
    const line = ok ? t(N[0] + ' ' + m.name + ': ' + gap + ' half steps to the 3rd, so the ' + (f === 'maj' ? 'major' : 'minor') + ' family.', N[0] + ' ' + m.nameKo + ': 3번째 음까지 반음 ' + gap + '개라서 ' + (f === 'maj' ? '장조' : '단조') + ' 계열이에요.')
      : bad ? t('Not that one. Count the half steps from ' + N[0] + ' to ' + N[2] + ': ' + gap + '. 4 is major, 3 is minor, so this is the ' + (f === 'maj' ? 'major' : 'minor') + ' family.', '그쪽이 아니에요. ' + N[0] + '에서 ' + N[2] + '까지 반음을 세 보세요: ' + gap + '개. 4개는 장조, 3개는 단조라서 ' + (f === 'maj' ? '장조' : '단조') + ' 계열이에요.')
      : t(N[0] + ' ' + m.name + ': is it in the major family or the minor family?', N[0] + ' ' + m.nameKo + ': 장조 계열일까요, 단조 계열일까요?');
    M.marks[K[2]] = 'pick';
    body = <>
      <div style={scS.title}>{t('Your turn', '내가 해보기')}</div>
      <div style={scS.line}>{line}</div>
      <ScKeys ks={K} marks={M.marks} names={M.names} arcs={[[K[0], K[2], false, '#c0431f']]} nonce={'g' + q}/>
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(2,minmax(0,1fr))', gap: 8, maxWidth: 340, margin: '10px auto 0' }}>
        {[['maj', t('Major family', '장조 계열')], ['min', t('Minor family', '단조 계열')]].map(([id, lab]) => <button key={id} className={'chip' + (ok && f === id ? ' active' : '')} style={{ ...KF_BTN, minHeight: 44 }} onClick={() => { if (ok) return; if (id === f) { setOk(true); setBad(false); } else setBad(true); }}>{lab}</button>)}
      </div>
      {scRow(<>
        <button className="ghost-btn" style={scS.back} onClick={() => { setView('one'); }}>{t('← Back', '← 이전')}</button>
        {ok && <button className="ghost-btn" style={scS.prim} onClick={() => { setQ(q + 1); setBad(false); setOk(false); }}>{t('Another →', '다른 것 →')}</button>}
      </>)}
    </>;
  }
  return scBox('modes', body);
}

// 5: the ladder from bright to dark: on C, each step down lowers one note by a half step
const MD_LAD = [3, 0, 4, 1, 5, 2, 6];
function MdLadder() {
  const [pos, setPos] = useState(1), P = useScPlay([pos]);
  const st = MD_LAD[pos], K = scModeK(mdParent(0, st), st), N = scModeNames(mdParent(0, st), st), m = MODES[st], M = mdPic(K, N, P.an);
  let line;
  if (pos === 0) line = t('The brightest: C major with its 4th note raised (' + prettyAny(N[3]) + ').', '가장 밝아요: C장조에서 4번째 음을 올렸어요(' + prettyAny(N[3]) + ').');
  else {
    const ps = MD_LAD[pos - 1], PK = scModeK(mdParent(0, ps), ps), PN = scModeNames(mdParent(0, ps), ps), j = K.findIndex((k, i) => i < 7 && k !== PK[i]);
    line = t('From ' + mdNm(MODES[ps]) + ' to ' + m.name + ': the ' + mdOrd(j) + ' note moves down one half step, ' + prettyAny(PN[j]) + ' → ' + prettyAny(N[j]) + '.', mdNm(MODES[ps]) + '에서 ' + m.nameKo + '으로: ' + mdOrd(j) + ' 음이 반음 내려가요, ' + prettyAny(PN[j]) + ' → ' + prettyAny(N[j]) + '.');
    M.marks = {}; K.forEach((k, i) => { M.marks[k] = i === j ? 'target' : 'pass'; }); if (P.an >= 0) M.marks[K[P.an]] = 'pick';
  }
  if (pos === 0) { M.marks = {}; K.forEach((k, i) => { M.marks[k] = i === 3 ? 'target' : 'pass'; }); if (P.an >= 0) M.marks[K[P.an]] = 'pick'; }
  return scBox('modes', <>
    <div style={scS.title}>{t('From bright to dark', '밝은 것에서 어두운 것까지')}</div>
    <div style={scS.line}>{line}</div>
    <div style={{ textAlign: 'center', fontFamily: "'Playfair Display', Georgia, serif", fontSize: 20, fontWeight: 900, color: '#26296b', marginBottom: 4 }}>C {mdNm(m)}</div>
    <ScKeys ks={K} marks={M.marks} names={M.names} arcs={[]} nonce={'l' + pos}/>
    <div style={{ maxWidth: 340, margin: '10px auto 0', display: 'grid', gap: 4 }}>
      <div style={{ fontSize: 11, fontWeight: 900, color: '#c0431f', textAlign: 'center' }}>{t('▲ brightest', '▲ 가장 밝음')}</div>
      {MD_LAD.map((s2, i) => { const on = pos === i; let mv = ''; if (i > 0) { const ps = MD_LAD[i - 1], pk = scModeK(mdParent(0, ps), ps), ck = scModeK(mdParent(0, s2), s2), pn = scModeNames(mdParent(0, ps), ps), cn = scModeNames(mdParent(0, s2), s2), j = ck.findIndex((k, x) => x < 7 && k !== pk[x]); mv = prettyAny(pn[j]) + ' → ' + prettyAny(cn[j]); } else mv = '♯4';
        return <button key={s2} aria-pressed={on} onClick={() => setPos(i)} style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', gap: 8, minHeight: 36, padding: '0 14px', borderRadius: 10, cursor: 'pointer', fontFamily: 'inherit', fontSize: 14, fontWeight: 900, color: on ? '#fffefa' : '#26296b', background: on ? '#26296b' : '#fff', border: '1.5px solid ' + (on ? '#26296b' : 'rgba(38,41,107,0.2)') }}><span>{mdNm(MODES[s2])}</span><span style={{ fontSize: 12.5, fontWeight: 800, color: on ? '#ffd9cc' : '#c0431f' }}>{mv}</span></button>; })}
      <div style={{ fontSize: 11, fontWeight: 900, color: '#c0431f', textAlign: 'center' }}>{t('▼ darkest', '▼ 가장 어두움')}</div>
    </div>
    <div style={{ textAlign: 'center', fontSize: 13, fontWeight: 700, color: '#4a4d86', marginTop: 8 }}>{t(m.mood, m.moodKo)}</div>
    {scRow(<>
      <button className="ghost-btn" style={scS.back} disabled={pos === 0} onClick={() => setPos(Math.max(0, pos - 1))}>{t('← Brighter', '← 더 밝게')}</button>
      <button className="ghost-btn" style={scS.back} onClick={() => mdHold(P, K)}>{t('▶ Hear it', '▶ 듣기')}</button>
      <button className="ghost-btn" style={scS.prim} disabled={pos === 6} onClick={() => setPos(Math.min(6, pos + 1))}>{t('Darker →', '더 어둡게 →')}</button>
    </>)}
  </>);
}
