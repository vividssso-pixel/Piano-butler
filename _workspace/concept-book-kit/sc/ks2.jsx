
// Keyboard patterns, lesson 1, designed from the learning goal (her call 2026-10-21: design first, keep old things only if they fit).
// One idea: black keys come in groups of 2 and 3. Whole picture, then the twos, then the threes, then her turn.
const KG_GROUPS = [[1, 3], [6, 8, 10]];
function KgBrackets({ lit, show = 'both', onTap }) {
  const items = [];
  for (let o = 0; o < 2; o++) KG_GROUPS.forEach((g, gi) => { const c = (k) => o * 252 + (k === 1 ? 36 : k === 3 ? 72 : k === 6 ? 144 : k === 8 ? 180 : 216); items.push({ n: g.length, x1: c(g[0]) - 11, x2: c(g[g.length - 1]) + 11, keys: g.map(k => o * 12 + k), id: o * 2 + gi }); });
  return <svg viewBox="-1 0 506 46" style={{ width: '100%', display: 'block' }}>
    {items.map(it => { const on = lit === it.id, dim = show !== 'both' && show !== it.n, mid = (it.x1 + it.x2) / 2;
      return <g key={it.id} onClick={() => onTap && onTap(it)} style={{ cursor: onTap ? 'pointer' : 'default', opacity: dim ? 0.2 : 1, transition: 'opacity 0.25s' }}>
        <path d={`M${it.x1},40 V28 H${it.x2} V40`} fill="none" stroke={on ? '#e4572e' : '#26296b'} strokeWidth="3" strokeLinejoin="round" style={{ transition: 'stroke 0.2s' }}/>
        <text x={mid} y="18" textAnchor="middle" fontSize="22" fontWeight="900" fill={on ? '#e4572e' : '#26296b'} style={{ fontFamily: 'Playfair Display, serif' }}>{it.n}</text>
      </g>; })}
  </svg>;
}
const kgPlay = (it) => it.keys.forEach((k, j) => setTimeout(() => playKey(k, 0.3), j * 220));
const KG_Q = [3, 2, 2, 3, 3, 2];
function KpGroups() {
  const [view, setView] = useState('all'), [lit, setLit] = useState(-1), [qi, setQi] = useState(0), [res, setRes] = useState(null);
  const want = KG_Q[qi], show = view === 'two' ? 2 : view === 'three' ? 3 : 'both';
  const keyOf = (k) => { const pc = k % 12, o = Math.floor(k / 12); const gi = pc === 1 || pc === 3 ? 0 : pc === 6 || pc === 8 || pc === 10 ? 1 : -1; return gi < 0 ? null : { n: KG_GROUPS[gi].length, id: o * 2 + gi, keys: KG_GROUPS[gi].map(x => o * 12 + x) }; };
  const marks = {};
  const litKeys = (id) => { const o = Math.floor(id / 2), gi = id % 2; return KG_GROUPS[gi].map(x => o * 12 + x); };
  if (lit >= 0) litKeys(lit).forEach(k => { marks[k] = res === 'no' ? 'bad' : res === 'ok' ? 'good' : 'target'; });
  if (show !== 'both' && view !== 'try') for (let o = 0; o < 2; o++) KG_GROUPS.forEach(g => { if (g.length === show) g.forEach(x => { marks[o * 12 + x] = 'target'; }); });
  const tapKB = (k) => { playKey(k); const g = keyOf(k); if (view === 'try') { if (res === 'ok') return; if (!g) { setRes('white'); setLit(-1); return; } setLit(g.id); setRes(g.n === want ? 'ok' : 'no'); } else if (g) { setLit(g.id); } };
  const tapBr = (it) => { kgPlay(it); setLit(it.id); if (view === 'try' && res !== 'ok') setRes(it.n === want ? 'ok' : 'no'); };
  const go = (v) => { setView(v); setLit(-1); setRes(null); };
  let body;
  if (view === 'all') body = <>
    <div style={scS.title}>{t('Black keys come in twos and threes', '검은건반은 두 개, 세 개씩 모여 있어요')}</div>
    <div style={scS.line}>{t('Look at the black keys. They sit in groups: 2, then 3, then 2, then 3. Tap a group to hear it.', '검은건반을 보세요. 2개, 3개, 2개, 3개씩 무리지어 있어요. 무리를 눌러 들어 보세요.')}</div>
    <KgBrackets lit={lit} onTap={tapBr}/>
    <TapKeyboard octaves={2} marks={marks} onTap={tapKB}/>
    {scRow(<button className="ghost-btn" style={scS.prim} onClick={() => go('two')}>{t('One at a time →', '하나씩 →')}</button>)}
  </>;
  else if (view === 'two' || view === 'three') body = <>
    <div style={scS.title}>{view === 'two' ? t('A group of 2', '두 개짜리 무리') : t('A group of 3', '세 개짜리 무리')}</div>
    <div style={scS.line}>{view === 'two' ? t('Two black keys side by side. Find them all the way up the piano.', '검은건반 두 개가 나란히 있어요. 피아노 위쪽까지 어디에나 있어요.') : t('Three black keys side by side. Find them all the way up the piano.', '검은건반 세 개가 나란히 있어요. 피아노 위쪽까지 어디에나 있어요.')}</div>
    <KgBrackets show={show} lit={lit} onTap={tapBr}/>
    <TapKeyboard octaves={2} marks={marks} onTap={tapKB}/>
    {scRow(<>
      <button className="ghost-btn" style={scS.back} onClick={() => go(view === 'two' ? 'all' : 'two')}>{t('← Back', '← 이전')}</button>
      <button className="ghost-btn" style={scS.prim} onClick={() => go(view === 'two' ? 'three' : 'try')}>{view === 'two' ? t('Next →', '다음 →') : t('Your turn →', '내가 해보기 →')}</button>
    </>)}
  </>;
  else body = <>
    <div style={scS.title}>{t('Your turn', '내가 해보기')}</div>
    <div style={scS.line}>{t('Tap a group of ' + want + '.', '검은건반이 ' + want + '개인 무리를 눌러 보세요.')}</div>
    <KgBrackets lit={lit} onTap={tapBr}/>
    <TapKeyboard octaves={2} marks={marks} onTap={tapKB}/>
    {res === 'ok' ? kpFeed(true, t('Yes! A group of ' + want + '.', '맞아요! ' + want + '개짜리 무리예요.'))
      : res === 'no' ? kpFeed(false, t('Not that one. That group has ' + (5 - want) + '. Look for the group of ' + want + '.', '아니에요. 그 무리는 ' + (5 - want) + '개예요. ' + want + '개짜리를 찾아보세요.'))
      : res === 'white' ? kpFeed(false, t('That is a white key. Look for the black keys in a group.', '그건 흰건반이에요. 무리지어 있는 검은건반을 찾아보세요.')) : kpFeed(null, '')}
    {scRow(<>
      <button className="ghost-btn" style={scS.back} onClick={() => go('three')}>{t('← Back', '← 이전')}</button>
      {res === 'ok' && <button className="ghost-btn" style={scS.prim} onClick={() => { setQi((qi + 1) % KG_Q.length); setRes(null); setLit(-1); }}>{t('Another →', '다른 것 →')}</button>}
      {(res === 'no' || res === 'white') && <button className="ghost-btn" style={scS.back} onClick={() => { setRes(null); setLit(-1); }}>{t('Try again', '다시 해 보기')}</button>}
    </>)}
  </>;
  return scBox('kp', body);
}
