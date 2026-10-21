
// ─── Keyboard patterns, rebuilt in the Scales way (her call 2026-10-21: "start with 1"): one idea per lesson; the whole picture, then one at a time, then her turn;
// the keyboard first; a wrong answer is said plainly and the right one is shown. Her words: small house = 2 black keys, big house = 3; C at the left door, D inside, E at the right door.
function KpRoofs({ oct = 2, show = 'both', lit = -1, onTap }) {
  const W = oct * 252, houses = [];
  for (let o = 0; o < oct; o++) { houses.push({ kind: 'small', x1: o * 252 + 36 - 13, x2: o * 252 + 72 + 13, base: o * 12 }); houses.push({ kind: 'big', x1: o * 252 + 144 - 13, x2: o * 252 + 216 + 13, base: o * 12 }); }
  return <svg viewBox={`-1 0 ${W + 2} 44`} style={{ width: '100%', display: 'block' }}>
    {houses.map((h, i) => {
      const mid = (h.x1 + h.x2) / 2, on = lit === i, col = h.kind === 'small' ? '#e4572e' : '#26296b', dim = show !== 'both' && show !== h.kind;
      return <g key={i} onClick={() => onTap && onTap(h, i)} style={{ cursor: onTap ? 'pointer' : 'default', opacity: dim ? 0.22 : 1, transition: 'opacity 0.25s' }}>
        <polygon points={`${h.x1},42 ${mid},${h.kind === 'small' ? 14 : 6} ${h.x2},42`} fill={on ? col : col + '33'} stroke={col} strokeWidth="2" strokeLinejoin="round" style={{ transition: 'fill 0.2s' }}/>
        {h.kind === 'small' ? <rect x={mid - 3} y={26} width="6" height="8" fill={on ? '#fff' : col}/> : <><rect x={mid - 9} y={24} width="6" height="7" fill={on ? '#fff' : col}/><rect x={mid + 3} y={24} width="6" height="7" fill={on ? '#fff' : col}/></>}
      </g>;
    })}
  </svg>;
}
const kpHousePlay = (h) => (h.kind === 'small' ? [1, 3] : [6, 8, 10]).forEach((k, j) => setTimeout(() => playKey(h.base + k, 0.3), j * 200));
const kpFeed = (ok, txt) => <div style={{ textAlign: 'center', fontSize: 14.5, fontWeight: 900, minHeight: 40, margin: '8px 0 0', color: ok === true ? '#2e8a6e' : ok === false ? '#c8361b' : '#26296b' }}>{txt}</div>;

// 1: high and low
function KpHear() {
  const [view, setView] = useState('all'), [q, setQ] = useState(null), [ans, setAns] = useState(null), [nonce, setNonce] = useState(0);
  const ask = () => { const hi = Math.random() < 0.5, k = hi ? 38 + Math.floor(Math.random() * 8) : 2 + Math.floor(Math.random() * 8); setQ({ hi, k }); setAns(null); playKey(k - 24, 0.9); setNonce(n => n + 1); };
  const marks = q && ans != null ? { [q.k]: ans === q.hi ? 'good' : 'bad' } : {};
  let body;
  if (view === 'all') body = <>
    <div style={scS.title}>{t('High and low', '높은 소리, 낮은 소리')}</div>
    <div style={scS.line}>{t('On the piano, left is low and right is high. Tap some keys and listen.', '피아노에서는 왼쪽이 낮은 소리, 오른쪽이 높은 소리예요. 건반을 눌러 들어 보세요.')}</div>
    <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: 13, fontWeight: 900, color: '#c0431f', margin: '0 4px 2px' }}><span>{t('← low', '← 낮은 음')}</span><span>{t('high →', '높은 음 →')}</span></div>
    <TapKeyboard octaves={4} onTap={(k) => playKey(k - 24)}/>
    {scRow(<button className="ghost-btn" style={scS.prim} onClick={() => { setView('try'); setQ(null); setAns(null); }}>{t('Your turn →', '내가 해보기 →')}</button>)}
  </>;
  else body = <>
    <div style={scS.title}>{t('Your turn', '내가 해보기')}</div>
    <div style={scS.line}>{q == null ? t('Press Listen. Is the sound high or low?', '듣기를 누르세요. 높은 소리일까요, 낮은 소리일까요?') : ans == null ? t('Which was it?', '어느 쪽이었을까요?') : ''}</div>
    <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: 13, fontWeight: 900, color: '#c0431f', margin: '0 4px 2px' }}><span>{t('← low', '← 낮은 음')}</span><span>{t('high →', '높은 음 →')}</span></div>
    <TapKeyboard octaves={4} marks={marks} onTap={(k) => playKey(k - 24)}/>
    <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 8, margin: '10px 0 0' }}>
      {[['Low', t('Low', '낮아요'), false], ['High', t('High', '높아요'), true]].map(([id, lab, hi]) => <button key={id} className="ghost-btn" disabled={q == null || ans != null} onClick={() => setAns(hi)} style={{ padding: '14px 0', fontSize: 18, fontWeight: 900 }}>{lab}</button>)}
    </div>
    {ans == null ? kpFeed(null, '') : ans === q.hi ? kpFeed(true, t('Yes! That one was ' + (q.hi ? 'high: it came from the right.' : 'low: it came from the left.'), '맞아요! ' + (q.hi ? '높은 소리였어요: 오른쪽에서 났어요.' : '낮은 소리였어요: 왼쪽에서 났어요.')))
      : kpFeed(false, t('Not that one. It was ' + (q.hi ? 'high: look, the key is on the right.' : 'low: look, the key is on the left.'), '아니에요. ' + (q.hi ? '높은 소리였어요: 보세요, 건반이 오른쪽에 있어요.' : '낮은 소리였어요: 보세요, 건반이 왼쪽에 있어요.')))}
    {scRow(<>
      <button className="ghost-btn" style={scS.back} onClick={() => setView('all')}>{t('← Back', '← 이전')}</button>
      <button className="ghost-btn" style={scS.back} disabled={q == null} onClick={() => playKey(q.k - 24, 0.9)}>{t('♪ Again', '♪ 다시')}</button>
      <button className="ghost-btn" style={scS.prim} onClick={ask}>{q == null ? t('▶ Listen', '▶ 듣기') : t('Next sound ▶', '다음 소리 ▶')}</button>
    </>)}
  </>;
  return scBox('kp', body);
}

// 2: black keys come in twos and threes
const KP_SMALL = [1, 3], KP_BIG = [6, 8, 10];
const KP_HQ = ['small', 'big', 'big', 'small', 'big', 'small'];
function KpHouses() {
  const [view, setView] = useState('all'), [lit, setLit] = useState(-1), [qi, setQi] = useState(0), [res, setRes] = useState(null);
  const show = view === 'small' ? 'small' : view === 'big' ? 'big' : 'both';
  const hit = (h, i) => { setLit(i); kpHousePlay(h); if (view === 'try' && res == null) { const want = KP_HQ[qi]; setRes(h.kind === want ? 'ok' : 'no'); setLit(i); } };
  const tapKey = (k) => { const pc = k % 12; playKey(k); if (view !== 'try' || res != null) return; if (KP_SMALL.includes(pc) || KP_BIG.includes(pc)) { const kind = KP_SMALL.includes(pc) ? 'small' : 'big'; setRes(kind === KP_HQ[qi] ? 'ok' : 'no'); } else setRes('white'); };
  const marks = {};
  if (show !== 'both') for (let o = 0; o < 2; o++) (show === 'small' ? KP_SMALL : KP_BIG).forEach(k => { marks[o * 12 + k] = 'target'; });
  let body;
  const want = KP_HQ[qi];
  if (view === 'all') body = <>
    <div style={scS.title}>{t('Black keys come in twos and threes', '검은건반은 두 개, 세 개씩 모여 있어요')}</div>
    <div style={scS.line}>{t('Look at the black keys. They are in groups, and the groups repeat all the way up the piano. Tap a house.', '검은건반을 보세요. 무리지어 있고, 그 무리가 피아노 끝까지 되풀이돼요. 집을 눌러 보세요.')}</div>
    <KpRoofs onTap={hit} lit={lit}/>
    <TapKeyboard octaves={2} tint onTap={(k) => playKey(k)}/>
    {scRow(<button className="ghost-btn" style={scS.prim} onClick={() => { setView('small'); setLit(-1); }}>{t('One by one →', '하나씩 →')}</button>)}
  </>;
  else if (view === 'small' || view === 'big') body = <>
    <div style={scS.title}>{view === 'small' ? t('The small house: 2', '작은 집: 2') : t('The big house: 3', '큰 집: 3')}</div>
    <div style={scS.line}>{view === 'small' ? t('Two black keys side by side make a small house.', '검은건반 두 개가 나란히 있으면 작은 집이에요.') : t('Three black keys side by side make a big house.', '검은건반 세 개가 나란히 있으면 큰 집이에요.')}</div>
    <KpRoofs show={show} onTap={hit} lit={lit}/>
    <TapKeyboard octaves={2} marks={marks} tint onTap={(k) => playKey(k)}/>
    {scRow(<>
      <button className="ghost-btn" style={scS.back} onClick={() => { setView(view === 'small' ? 'all' : 'small'); setLit(-1); }}>{t('← Back', '← 이전')}</button>
      <button className="ghost-btn" style={scS.prim} onClick={() => { if (view === 'small') setView('big'); else { setView('try'); setQi(0); setRes(null); } setLit(-1); }}>{view === 'small' ? t('Next →', '다음 →') : t('Your turn →', '내가 해보기 →')}</button>
    </>)}
  </>;
  else body = <>
    <div style={scS.title}>{t('Your turn', '내가 해보기')}</div>
    <div style={scS.line}>{t('Tap a ' + (want === 'small' ? 'small house (2 black keys).' : 'big house (3 black keys).'), (want === 'small' ? '작은 집(검은건반 2개)' : '큰 집(검은건반 3개)') + '을 눌러 보세요.')}</div>
    <KpRoofs onTap={hit} lit={res ? lit : -1}/>
    <TapKeyboard octaves={2} tint onTap={tapKey}/>
    {res === 'ok' ? kpFeed(true, t('Yes! ' + (want === 'small' ? 'Two black keys: a small house.' : 'Three black keys: a big house.'), '맞아요! ' + (want === 'small' ? '검은건반 두 개: 작은 집이에요.' : '검은건반 세 개: 큰 집이에요.')))
      : res === 'no' ? kpFeed(false, t('Not that one. That is a ' + (want === 'small' ? 'big' : 'small') + ' house, with ' + (want === 'small' ? '3' : '2') + ' black keys. Look for ' + (want === 'small' ? '2' : '3') + '.', '아니에요. 그건 ' + (want === 'small' ? '큰' : '작은') + ' 집이에요, 검은건반이 ' + (want === 'small' ? '3' : '2') + '개예요. ' + (want === 'small' ? '2' : '3') + '개를 찾아보세요.'))
      : res === 'white' ? kpFeed(false, t('That is a white key. Look for the black keys in a group.', '그건 흰건반이에요. 무리지어 있는 검은건반을 찾아보세요.')) : kpFeed(null, '')}
    {scRow(<>
      <button className="ghost-btn" style={scS.back} onClick={() => { setView('big'); setLit(-1); }}>{t('← Back', '← 이전')}</button>
      {res === 'ok' && <button className="ghost-btn" style={scS.prim} onClick={() => { setQi((qi + 1) % KP_HQ.length); setRes(null); setLit(-1); }}>{t('Another →', '다른 것 →')}</button>}
      {res !== 'ok' && res != null && <button className="ghost-btn" style={scS.back} onClick={() => { setRes(null); setLit(-1); }}>{t('Try again', '다시 해 보기')}</button>}
    </>)}
  </>;
  return scBox('kp', body);
}

// 3: the white keys of each house
const KP_WQ = ['D', 'F', 'B', 'C', 'G', 'E', 'A'];
const KP_PC = { C: 0, D: 2, E: 4, F: 5, G: 7, A: 9, B: 11 };
const KP_GUIDE = { C: ['C is at the left door of the small house.', 'C는 작은 집의 왼쪽 문에 있어요.'], D: ['D lives inside the small house, between its two black keys.', 'D는 작은 집 안, 두 검은건반 사이에 살아요.'], E: ['E is at the right door of the small house.', 'E는 작은 집의 오른쪽 문에 있어요.'],
  F: ['F is at the left door of the big house.', 'F는 큰 집의 왼쪽 문에 있어요.'], G: ['G lives inside the big house, between its first and second black keys.', 'G는 큰 집 안, 첫째와 둘째 검은건반 사이에 살아요.'], A: ['A lives inside the big house, between its second and third black keys.', 'A는 큰 집 안, 둘째와 셋째 검은건반 사이에 살아요.'], B: ['B is at the right door of the big house.', 'B는 큰 집의 오른쪽 문에 있어요.'] };
function KpWhite() {
  const [view, setView] = useState('all'), [qi, setQi] = useState(0), [res, setRes] = useState(null), [bad, setBad] = useState(null);
  const names = {}, marks = {}, set = (L, kind) => { for (let o = 0; o < 2; o++) L.forEach(n => { names[o * 12 + KP_PC[n]] = n; if (kind) marks[o * 12 + KP_PC[n]] = 'target'; }); };
  if (view === 'all') set(['C', 'D', 'E', 'F', 'G', 'A', 'B'], false);
  if (view === 'small') set(['C', 'D', 'E'], true);
  if (view === 'big') set(['F', 'G', 'A', 'B'], true);
  const L = KP_WQ[qi];
  const tap = (k) => { playKey(k); if (view !== 'try' || res === 'ok') return; const pc = k % 12; if (pc === KP_PC[L]) { setRes('ok'); setBad(null); } else { setRes('no'); setBad(k); } };
  if (view === 'try') { if (res === 'ok') for (let o = 0; o < 2; o++) { marks[o * 12 + KP_PC[L]] = 'good'; names[o * 12 + KP_PC[L]] = L; } if (bad != null && res === 'no') marks[bad] = 'bad'; }
  const show = view === 'small' ? 'small' : view === 'big' ? 'big' : 'both';
  let body;
  if (view === 'all') body = <>
    <div style={scS.title}>{t('The white keys of each house', '집마다 있는 흰건반')}</div>
    <div style={scS.line}>{t('Every white key lives at a house. C D E live at the small house. F G A B live at the big house.', '흰건반은 모두 어느 집에 살아요. 작은 집에는 C D E, 큰 집에는 F G A B가 살아요.')}</div>
    <KpRoofs/>
    <TapKeyboard octaves={2} names={names} tint onTap={tap}/>
    {scRow(<button className="ghost-btn" style={scS.prim} onClick={() => setView('small')}>{t('One by one →', '하나씩 →')}</button>)}
  </>;
  else if (view === 'small' || view === 'big') body = <>
    <div style={scS.title}>{view === 'small' ? t('C D E: the small house', 'C D E: 작은 집') : t('F G A B: the big house', 'F G A B: 큰 집')}</div>
    <div style={scS.line}>{view === 'small' ? t('C is at the left door, D is inside, E is at the right door.', 'C는 왼쪽 문, D는 집 안, E는 오른쪽 문에 있어요.') : t('F is at the left door, G and A are inside, B is at the right door.', 'F는 왼쪽 문, G와 A는 집 안, B는 오른쪽 문에 있어요.')}</div>
    <KpRoofs show={show}/>
    <TapKeyboard octaves={2} marks={marks} names={names} tint onTap={tap}/>
    {scRow(<>
      <button className="ghost-btn" style={scS.back} onClick={() => setView(view === 'small' ? 'all' : 'small')}>{t('← Back', '← 이전')}</button>
      <button className="ghost-btn" style={scS.prim} onClick={() => { if (view === 'small') setView('big'); else { setView('try'); setQi(0); setRes(null); setBad(null); } }}>{view === 'small' ? t('Next →', '다음 →') : t('Your turn →', '내가 해보기 →')}</button>
    </>)}
  </>;
  else body = <>
    <div style={scS.title}>{t('Your turn', '내가 해보기')}</div>
    <div style={scS.line}>{res === 'ok' ? t('Yes! ' + KP_GUIDE[L][0], '맞아요! ' + KP_GUIDE[L][1]) : t('Tap ' + L + '. Think of the house first.', L + '을 눌러 보세요. 먼저 어느 집인지 생각해 봐요.')}</div>
    <KpRoofs/>
    <TapKeyboard octaves={2} marks={marks} names={names} tint onTap={tap}/>
    {res === 'no' ? kpFeed(false, t('Not that one. ' + KP_GUIDE[L][0], '아니에요. ' + KP_GUIDE[L][1])) : kpFeed(null, '')}
    {scRow(<>
      <button className="ghost-btn" style={scS.back} onClick={() => { setView('big'); }}>{t('← Back', '← 이전')}</button>
      {res === 'ok' && <button className="ghost-btn" style={scS.prim} onClick={() => { setQi((qi + 1) % KP_WQ.length); setRes(null); setBad(null); }}>{t('Another →', '다른 것 →')}</button>}
    </>)}
  </>;
  return scBox('kp', body);
}
