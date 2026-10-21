// ─── Keys and staff, built again from the start in the Scales style (her call 2026-10-22: "make it new, not fitted into the old ones; use the final colours of the key signatures and scales; don't say the same thing twice").
// Look: the Scales keyboard (ScKeys: the names above the keys, the two-name black keys), coral and blue for the two groups (coral = the small house, 3 white keys; blue = the big house, 4 white keys),
// the key you tapped solid. Every lesson: the whole picture, one at a time, her turn. Title, line and feedback each say something new. The staff is shown on request in the keyboard lessons.
const KQ = { CO: '#e4572e', COD: '#c0431f', BL: '#3b4fa8', NV: '#26296b' };
const kqT = (a) => t(a[0], a[1]);
const kqRnd = (n) => Math.floor(Math.random() * n), kqPick = (a) => a[kqRnd(a.length)];
const KQ_PC = { C: 0, D: 2, E: 4, F: 5, G: 7, A: 9, B: 11 }, KQ_L = { 0: 'C', 2: 'D', 4: 'E', 5: 'F', 7: 'G', 9: 'A', 11: 'B' }, KQ_ABC = ['A', 'B', 'C', 'D', 'E', 'F', 'G'];
const KQ_SMALL = ['C', 'D', 'E'], KQ_BIG = ['F', 'G', 'A', 'B'], KQ_BK2 = [1, 3], KQ_BK3 = [6, 8, 10];
const kqLetter = (d) => 'CDEFGAB'[((d % 7) + 7) % 7];
const kqHouseCol = (L) => KQ_SMALL.includes(L) ? KQ.COD : KQ.BL;
// keys of one house in every octave: white letters and the black keys under its roof
const kqHouseKeys = (oct, small, from = 0) => { const k = []; for (let o = from; o < oct; o++) (small ? [0, 1, 2, 3, 4] : [5, 6, 7, 8, 9, 10, 11]).forEach(p => k.push(o * 12 + p)); return k; };
const kqPaint = (marks, keys, style) => { keys.forEach(k => { marks[k] = style; }); return marks; };
const kqNames = (oct, letters, ncol) => { const n = {}, c = {}; for (let o = 0; o < oct; o++) letters.forEach(L => { n[o * 12 + KQ_PC[L]] = L; c[o * 12 + KQ_PC[L]] = kqHouseCol(L); }); return { names: n, ncol: c }; };
// the keyboard, the Scales one
const KQX = [18, 36, 54, 72, 90, 126, 144, 162, 180, 198, 216, 234];
const kqX = (k) => Math.floor(k / 12) * 252 + KQX[((k % 12) + 12) % 12];
const kqVx = (a, b) => [kqX(a) - 24, kqX(b) + 24];
// f.bare: a keyboard with no letters at all (the first lessons, before the names are taught); f.ks: crop to the keys a..b (a close-up)
const kqKb = (f, onTap) => f.bare
  ? <div style={{ maxWidth: f.mw || 340, margin: '0 auto' }}><TapKeyboard octaves={f.oct} extraC marks={f.marks || {}} onTap={onTap} top={0} names={f.names || null} nameCol={f.ncol || null} vx={f.vx || kqVx(0, f.oct * 12)}/></div>
  : <ScKeys ks={f.ks || [0, f.oct * 12]} oct={f.oct} marks={f.marks || {}} names={f.names || {}} ncol={f.ncol || {}} arcs={[]} nonce={0} onTap={onTap} mw={f.mw || 340} plain={f.plain}/>;
// words or numbers above the keyboard, at the keys' own x (same crop as the keyboard under it, so they line up)
const kqNumRow = (vx, items, fs = 22) => { const sc = (vx[1] - vx[0]) / 340, h = (fs + 14) * sc; return <div style={{ maxWidth: 340, margin: '0 auto' }}><svg viewBox={`${vx[0]} 0 ${vx[1] - vx[0]} ${h}`} style={{ width: '100%', display: 'block' }}>
  {items.map((it) => <text key={it.t + ':' + it.x} x={it.x} y={h - 8 * sc} textAnchor="middle" fontSize={fs * sc} fontWeight="900" fill={it.col} style={{ animation: 'fadeUp 0.3s both' }}>{it.t}</text>)}</svg></div>; };
// roofs, drawn in the keyboard's own coordinates (so they sit exactly over the black keys)
function KqRoofs({ oct = 2, show = 'both', vx, k = 0, only = null }) {
  const hs = []; for (let o = 0; o < oct; o++) { hs.push({ small: true, x1: o * 252 + 23, x2: o * 252 + 85, id: o * 2 }); hs.push({ small: false, x1: o * 252 + 131, x2: o * 252 + 229, id: o * 2 + 1 }); }
  const v = vx || [-6, oct * 252 + 42], sc = (v[1] - v[0]) / 340, H = 46 * sc;
  return <div style={{ maxWidth: 340, margin: '0 auto' }}><svg viewBox={`${v[0]} 0 ${v[1] - v[0]} ${H}`} style={{ width: '100%', display: 'block' }}>
    <style>{'@keyframes kqDrop{from{transform:translateY(-' + 26 * sc + 'px);opacity:0}to{transform:none;opacity:1}}'}</style>
    {hs.filter(h => (show === 'both' || (show === 'small') === h.small) && (!only || only.includes(h.id))).map(h => { const col = h.small ? KQ.CO : KQ.BL, mid = (h.x1 + h.x2) / 2, y0 = H - 2 * sc, ph = (h.small ? 26 : 34) * sc;
      return <g key={h.id + ':' + k} style={{ animation: 'kqDrop 0.55s ease-out both' }}>
        <polygon points={`${h.x1},${y0} ${mid},${y0 - ph} ${h.x2},${y0}`} fill={col + '33'} stroke={col} strokeWidth={2.4 * sc} strokeLinejoin="round"/>
        {h.small ? <rect x={mid - 3 * sc} y={y0 - 14 * sc} width={6 * sc} height={8 * sc} fill={col}/> : <><rect x={mid - 10 * sc} y={y0 - 16 * sc} width={6 * sc} height={8 * sc} fill={col}/><rect x={mid + 4 * sc} y={y0 - 16 * sc} width={6 * sc} height={8 * sc} fill={col}/></>}</g>; })}
  </svg></div>;
}
const kqFeed = (ok, txt) => <div style={{ textAlign: 'center', fontSize: 14.5, fontWeight: 900, minHeight: 40, margin: '8px 0 0', color: ok === true ? '#2e8a6e' : ok === false ? '#c8361b' : KQ.NV, textWrap: 'balance' }}>{txt}</div>;
// the black-key groups: a bracket and its count (coral 2, blue 3), in the keyboard's coordinates
function KqGroupsTop({ oct = 2, show = 'both', lit = null, onTap, upto = 99 }) {
  const items = []; for (let o = 0; o < oct; o++) [[1, 3], [6, 8, 10]].forEach((g, gi) => { const c = (k) => o * 252 + (k === 1 ? 36 : k === 3 ? 72 : k === 6 ? 144 : k === 8 ? 180 : 216); items.push({ n: g.length, x1: c(g[0]) - 11, x2: c(g[g.length - 1]) + 11, keys: g.map(k => o * 12 + k), id: o * 2 + gi }); });
  return <div style={{ maxWidth: 340, margin: '0 auto' }}><svg viewBox={`-6 0 ${oct * 252 + 48} 40`} style={{ width: '100%', display: 'block' }}>
    {items.map(it => { const col = it.n === 2 ? KQ.CO : KQ.BL, on = !!lit && lit.g === it.id, dim = show !== 'both' && show !== it.n, mid = (it.x1 + it.x2) / 2, hid = it.id >= upto;
      return <g key={it.id} onClick={() => onTap && onTap(it)} style={{ cursor: onTap ? 'pointer' : 'default', opacity: hid ? 0 : dim ? 0.18 : 1, transition: 'opacity 0.35s' }}>
        <path d={`M${it.x1},36 V26 H${it.x2} V36`} fill="none" stroke={col} strokeWidth={on ? 4.5 : 3} strokeLinejoin="round"/>
        <text x={mid} y="18" textAnchor="middle" fontSize="19" fontWeight="900" fill={col}>{it.n}</text></g>; })}
  </svg></div>;
}
const kqArrow = (pos, n) => <div style={{ maxWidth: 340, margin: '0 auto' }}><svg viewBox="0 0 500 34" style={{ width: '100%', display: 'block' }}>
  <text x="20" y="12" fontSize="13" fontWeight="900" fill={KQ.COD}>{t('← low', '← 낮은 음')}</text><text x="480" y="12" textAnchor="end" fontSize="13" fontWeight="900" fill={KQ.BL}>{t('high →', '높은 음 →')}</text>
  <line x1="20" y1="24" x2="470" y2="24" stroke={KQ.NV} strokeWidth="3"/><path d="M468 16 L486 24 L468 32 Z" fill={KQ.NV}/>
  {pos != null && <circle cx={20 + 450 * (pos + 0.5) / n} cy="24" r="8" fill={KQ.CO} style={{ transition: 'cx 0.25s' }}/>}
</svg></div>;
// the staff, as in the Scales lessons (SkgStaff)
const kqStaff = (ds, clef, o = {}) => {
  const items = ds.map(d => ['q', 1, d]).concat([['||']]);
  const oo = { boxS: 26, D: 30, ring: o.ring || [], ...(o.under ? skgUnder(items, 'C', o.under === true ? null : o.under, o.coral || []) : {}) };
  if (o.bracket) { items.splice(ds.length, 0, ['|']); oo.bracket = o.bracket; }
  return <div style={{ maxWidth: 330, margin: '0 auto' }}><SkgStaff items={items} k="C" clef={clef} width={330} o={oo}/></div>;
};
// five lines and four spaces, counted from the bottom
function KqLines({ hl, labels, onTap, pickd, ok }) {
  const yl = (n) => 116 - (n - 1) * 26, col = (type, n) => hl && hl.type === type && hl.n === n ? KQ.CO : KQ.NV, pk = (type, n) => pickd && pickd.type === type && pickd.n === n;
  return <svg viewBox="0 0 320 130" style={{ width: '100%', display: 'block', maxWidth: 340, margin: '0 auto' }}>
    {[1, 2, 3, 4].map(n => <rect key={'s' + n} x="40" y={yl(n + 1) + 7} width="240" height="12" rx="4" fill={pk('space', n) ? (ok ? '#cfe8dd' : '#f6c9bf') : hl && hl.type === 'space' && hl.n === n ? '#fbe3da' : 'transparent'} onClick={() => onTap && onTap({ type: 'space', n })} style={{ cursor: onTap ? 'pointer' : 'default' }}/>)}
    {[1, 2, 3, 4, 5].map(n => <g key={'l' + n} onClick={() => onTap && onTap({ type: 'line', n })} style={{ cursor: onTap ? 'pointer' : 'default' }}>
      <rect x="40" y={yl(n) - 7} width="240" height="14" fill="transparent"/>
      <line x1="40" x2="280" y1={yl(n)} y2={yl(n)} stroke={pk('line', n) ? (ok ? '#2e8a6e' : '#c8361b') : col('line', n)} strokeWidth={hl && hl.type === 'line' && hl.n === n || pk('line', n) ? 4 : 2}/></g>)}
    {labels && [1, 2, 3, 4, 5].map(n => <text key={'tl' + n} x="22" y={yl(n) + 5} textAnchor="middle" fontSize="15" fontWeight="900" fill={col('line', n)}>{n}</text>)}
    {labels && [1, 2, 3, 4].map(n => <text key={'ts' + n} x="300" y={yl(n) - 8} textAnchor="middle" fontSize="15" fontWeight="900" fill={col('space', n)}>{n}</text>)}
    <text x="40" y="127" fontSize="11" fontWeight="800" fill={KQ.COD}>{t('count up from the bottom', '아래에서부터 세어요')}</text>
  </svg>;
}
const kqOrd = (n) => ['', t('1st', '첫째'), t('2nd', '둘째'), t('3rd', '셋째'), t('4th', '넷째'), t('5th', '다섯째')][n];
const kqPlayDs = (ds) => ds.forEach((d, j) => setTimeout(() => playKey(dMidiKey(d), 0.45), j * 380));

// ── the engine: every lesson has the same three views ──
function KqEngine({ spec }) {
  const [view, setView] = useState('all'), [si, setSi] = useState(0), [qn, setQn] = useState(0), [q, setQ] = useState(null), [res, setRes] = useState(null), [pickd, setPickd] = useState(null), [last, setLast] = useState(null), [stf, setStf] = useState(false), [tk, setTk] = useState(0), [found, setFound] = useState([]);
  useEffect(() => { setTk(0); const id = setInterval(() => setTk(x => x >= 40 ? x : x + 1), 650); return () => clearInterval(id); }, [view, si, qn]);
  const pick = (v) => { if (!q) return;
    if (q.kind === 'multi') { if (res === 'ok') return; if (q.targets.includes(v)) { if (found.includes(v)) return; const nf = found.concat([v]); setFound(nf); setPickd(null); setRes(nf.length === q.targets.length ? 'ok' : null); } else { setPickd(v); setRes('no'); } return; }
    if (res === 'ok' || (res === 'no' && !q.retry)) return; const ok = q.ok(v); setPickd(v); setRes(ok ? 'ok' : 'no'); if (q.onPick) q.onPick(v, ok); };
  const ctx = { last, setLast, res, pickd, si, q, pick, qn, tk, view, found };
  const go = (v, i) => { setView(v); if (i != null) setSi(i); setRes(null); setPickd(null); setFound([]); };
  const newQ = (n) => { const nq = spec.make(n, q); setQ(nq); setQn(n); setRes(null); setPickd(null); setLast(null); setFound([]); if (nq.play) setTimeout(nq.play, 300); };
  const startTry = () => { setView('try'); newQ(0); };
  const show = (f, allowStaff) => {
    if (!f) return null;
    const kb = f.kb, marks = kb ? { ...(kb.marks || {}) } : {};
    if (kb && view === 'try' && q && q.kind === 'key' && pickd != null) marks[pickd] = res === 'ok' ? 'good' : 'bad';
    if (kb && view === 'try' && q && q.kind === 'multi') { found.forEach(k => { marks[k] = 'good'; }); if (pickd != null && res === 'no') marks[pickd] = 'bad'; }
    return <>
      {f.top}{f.staff}{f.mid}
      {kb && kqKb({ ...kb, marks }, (k) => { playKey(k + (kb.base || 0), 0.6); setLast(k); if (view === 'try' && q && (q.kind === 'key' || q.kind === 'multi')) pick(k); else if (kb.onTap) kb.onTap(k); })}
      {allowStaff && f.staffAlt && <>
        <div style={{ textAlign: 'center', margin: '8px 0 0' }}><button className="ghost-btn" style={{ ...scS.back, minWidth: 0, fontSize: 14 }} onClick={() => setStf(!stf)}>{stf ? t('Hide the staff', '스태프 숨기기') : t('Show on the staff', '스태프로 보여주기')}</button></div>
        {stf && f.staffAlt}</>}
      {f.below}
    </>;
  };
  const steps = spec.steps, tit = (a) => <div style={scS.title}>{kqT(a)}</div>, lin = (a) => <div style={scS.line}>{kqT(a)}</div>;
  let body;
  if (view === 'all') body = <>
    {tit(spec.title)}{lin(spec.allLine)}{show(spec.fig(ctx), true)}
    {scRow(<button className="ghost-btn" style={scS.prim} onClick={() => go('step', 0)}>{t('One by one →', '하나씩 →')}</button>)}
  </>;
  else if (view === 'step') { const s = steps[si]; body = <>
    {tit(s.title)}{lin(s.line)}{show(s.fig(ctx), true)}
    {scRow(<>
      <button className="ghost-btn" style={scS.back} onClick={() => si === 0 ? go('all') : go('step', si - 1)}>{t('← Back', '← 이전')}</button>
      <button className="ghost-btn" style={scS.prim} onClick={() => si < steps.length - 1 ? go('step', si + 1) : startTry()}>{si < steps.length - 1 ? t('Next →', '다음 →') : t('Your turn →', '내가 해보기 →')}</button>
    </>)}
  </>; }
  else if (q) { const f = q.fig(ctx);
    const txt = res === 'ok' ? [kqT(q.yes), true] : res === 'no' ? [kqT(typeof q.no === 'function' ? q.no(pickd) : q.no), false] : q.kind === 'multi' && found.length ? [kqT(q.prog(found.length, q.targets.length)), true] : ['', null];
    body = <>
      {tit(spec.tryTitle || ['Your turn', '내가 해보기'])}{lin(q.prompt)}{show(f, false)}
      {q.opts && <div style={{ display: 'grid', gridTemplateColumns: 'repeat(' + (q.cols || 2) + ',1fr)', gap: 8, margin: '10px 0 0' }}>
        {q.opts.map(o => <button key={o.id} className={'choice-btn' + (res == null ? '' : o.id === q.ans ? ' good' : o.id === pickd ? ' bad' : '')} disabled={res != null} onClick={() => pick(o.id)} style={{ padding: '13px 4px', fontSize: q.cols > 3 ? 18 : 16, fontWeight: 900 }}>{typeof o.label === 'function' ? o.label() : o.label}</button>)}
      </div>}
      {kqFeed(txt[1], txt[0])}
      {scRow(<>
        <button className="ghost-btn" style={scS.back} onClick={() => go('step', steps.length - 1)}>{t('← Back', '← 이전')}</button>
        {q.play && <button className="ghost-btn" style={scS.back} onClick={q.play}>{t('♪ Again', '♪ 다시')}</button>}
        {(res === 'ok' || (res === 'no' && !q.retry)) && <button className="ghost-btn" style={scS.prim} onClick={() => newQ(qn + 1)}>{t('Another →', '다른 것 →')}</button>}
        {res === 'no' && q.retry && q.kind !== 'multi' && <button className="ghost-btn" style={scS.back} onClick={() => { setRes(null); setPickd(null); }}>{t('Try again', '다시 해 보기')}</button>}
      </>)}
    </>; }
  return scBox('kq', body);
}
const kqLet7 = () => KQ_ABC.map(L => ({ id: L, label: L }));
const KQ_SPEC = {};

// ══ 1. Keyboard patterns and note names (three lessons, her call 2026-10-22: 1+2, 3+4 and 5+6+7 each into one) ══
const KQ_DOOR = {
  C: [['C: the left door', 'C: 왼쪽 문'], ['Just before the two black keys.', '검은건반 두 개 바로 앞에 있어요.'], ['the left door of the small house', '작은 집의 왼쪽 문']],
  D: [['D: inside', 'D: 집 안'], ['Between the two black keys.', '두 검은건반 사이에 있어요.'], ['inside the small house, between its two black keys', '작은 집 안, 두 검은건반 사이']],
  E: [['E: the right door', 'E: 오른쪽 문'], ['Just after the two black keys.', '검은건반 두 개 바로 뒤에 있어요.'], ['the right door of the small house', '작은 집의 오른쪽 문']],
  F: [['F: the left door', 'F: 왼쪽 문'], ['Just before the three black keys.', '검은건반 세 개 바로 앞에 있어요.'], ['the left door of the big house', '큰 집의 왼쪽 문']],
  G: [['G: inside, first', 'G: 집 안, 첫째'], ['Between the first and second black keys.', '첫째와 둘째 검은건반 사이에 있어요.'], ['inside the big house, after its first black key', '큰 집 안, 첫째 검은건반 다음']],
  A: [['A: inside, second', 'A: 집 안, 둘째'], ['Between the second and third black keys.', '둘째와 셋째 검은건반 사이에 있어요.'], ['inside the big house, after its second black key', '큰 집 안, 둘째 검은건반 다음']],
  B: [['B: the right door', 'B: 오른쪽 문'], ['Just after the three black keys.', '검은건반 세 개 바로 뒤에 있어요.'], ['the right door of the big house', '큰 집의 오른쪽 문']],
};
const KQ_MC = [
  { k: 24, p: ['Tap middle C.', '가운데 도를 눌러 보세요.'], y: ['Yes, the C in the middle of the keyboard.', '맞아요. 건반 한가운데의 C예요.'] },
  { k: 36, p: ['Tap the next C to the right of middle C.', '가운데 도의 오른쪽 다음 C를 눌러 보세요.'], y: ['One pattern up from middle C.', '가운데 도에서 무늬 하나 위예요.'] },
  { k: 12, p: ['Tap the next C to the left of middle C.', '가운데 도의 왼쪽 다음 C를 눌러 보세요.'], y: ['One pattern down from middle C.', '가운데 도에서 무늬 하나 아래예요.'] },
];
// ── lesson 1: the black keys, then low and high. No letters on the keys yet; a tap anywhere in a group's column counts as that group.
const KQ_REG = (k) => [0, 1, 2, 3, 4].includes(((k % 12) + 12) % 12) ? 2 : 3;
{ const GR = { 2: { keys: [1, 3], style: 'seg3', col: KQ.CO, vx: kqVx(0, 4) }, 3: { keys: [6, 8, 10], style: 'seg4', col: KQ.BL, vx: kqVx(5, 11) } };
  const blacks = (n, o = 2) => { const m = {}; for (let i = 0; i < o; i++) (n === 2 ? [1, 3] : n === 3 ? [6, 8, 10] : [1, 3, 6, 8, 10]).forEach(k => { m[i * 12 + k] = n === 2 ? 'seg3' : n === 3 ? 'seg4' : (KQ_BK2.includes(k) ? 'seg3' : 'seg4'); }); return m; };
  const zoom = (n, c) => { const g = GR[n], lit = Math.min(c.tk, n), m = {}; g.keys.slice(0, lit).forEach(k => { m[k] = g.style; });
    return { top: kqNumRow(g.vx, g.keys.slice(0, lit).map((k, i) => ({ x: kqX(k), t: String(i + 1), col: g.col }))), kb: { bare: true, oct: 1, vx: g.vx, mw: 300, marks: m } }; };
  const reg = (want) => ({ kind: 'key', retry: true, prompt: ['Tap the side with ' + want + ' black keys.', '검은건반이 ' + want + '개인 쪽을 눌러 보세요.'],
    fig: (c) => ({ kb: { bare: true, oct: 2, base: 0, marks: c.res === 'ok' ? blacks(want) : {} } }), ok: (k) => KQ_REG(k) === want,
    yes: want === 2 ? ['Two, side by side.', '두 개가 나란히 있네요.'] : ['Three, in a row.', '세 개가 줄지어 있네요.'],
    no: (k) => ['That side has ' + (5 - want) + ' black keys. Look for the side with ' + want + '.', '그쪽은 검은건반이 ' + (5 - want) + '개예요. ' + want + '개인 쪽을 찾아 보세요.'] });
  const hearQ = (n) => { const gap = [30, 20, 12, 7, 4, 2][Math.min(n, 5)], lo = kqRnd(48 - gap), hi = lo + gap, firstHigh = Math.random() < 0.5, a = firstHigh ? hi : lo, b = firstHigh ? lo : hi;
    return { kind: 'choice', prompt: ['Listen to two sounds. Which one is higher?', '소리 두 개를 들어 보세요. 어느 쪽이 더 높을까요?'], opts: [{ id: '1', label: () => t('The first', '처음 소리') }, { id: '2', label: () => t('The second', '나중 소리') }], ans: firstHigh ? '1' : '2', ok: (v) => v === (firstHigh ? '1' : '2'),
      play: () => { playKey(a - 24, 0.8); setTimeout(() => playKey(b - 24, 0.8), 900); },
      fig: (c) => ({ top: kqArrow(c.res ? hi : null, 48), kb: { bare: true, oct: 4, base: -24, marks: c.res ? { [lo]: 'seg3', [hi]: 'pick' } : {} } }),
      yes: ['The higher sound came from the key further right.', '높은 소리는 더 오른쪽 건반에서 났어요.'], no: ['The other one was higher. Its key is further to the right.', '다른 쪽이 더 높았어요. 그 건반이 더 오른쪽에 있어요.'] }; };
  KQ_SPEC['kq-black'] = {
    title: ['Black keys', '검은건반'], allLine: ['They come in groups of 2 and 3, always in the same order. Tap to listen.', '2개와 3개씩 모여 있고, 순서는 늘 같아요. 눌러 들어 보세요.'],
    fig: (c) => ({ top: <KqGroupsTop lit={c.last && typeof c.last === 'object' ? c.last : null} onTap={(it) => { it.keys.forEach((k, j) => setTimeout(() => playKey(k, 0.3), j * 220)); c.setLast({ g: it.id }); }}/>, kb: { bare: true, oct: 2, base: 0, marks: blacks(0) } }),
    steps: [
      { title: ['Two', '둘'], line: ['Two black keys stand side by side. Count them.', '검은건반 두 개가 나란히 서 있어요. 세어 보세요.'], fig: (c) => zoom(2, c) },
      { title: ['Three', '셋'], line: ['Then comes a row of three.', '그다음에는 세 개가 줄지어 있어요.'], fig: (c) => zoom(3, c) },
      { title: ['Two, three, two, three', '둘, 셋, 둘, 셋'], line: ['The groups take turns from left to right, and the order never changes.', '무리는 왼쪽에서 오른쪽으로 번갈아 나오고, 순서는 바뀌지 않아요.'], fig: (c) => { const u = Math.min(c.tk, 4), m = {}; for (let i = 0; i < u; i++) Object.assign(m, kqPaint({}, (i % 2 === 0 ? [1, 3] : [6, 8, 10]).map(k => Math.floor(i / 2) * 12 + k), i % 2 === 0 ? 'seg3' : 'seg4')); return { top: <KqGroupsTop upto={u}/>, kb: { bare: true, oct: 2, base: 0, marks: m } }; } },
      { title: ['Low and high', '낮은 소리, 높은 소리'], line: ['Tap along the keys. Left sounds low and right sounds high.', '건반을 눌러 보세요. 왼쪽은 낮은 소리, 오른쪽은 높은 소리예요.'], fig: (c) => ({ top: kqArrow(typeof c.last === 'number' ? c.last : null, 48), kb: { bare: true, oct: 4, base: -24, marks: typeof c.last === 'number' ? { [c.last]: 'pick' } : {} } }) },
    ],
    make: (n) => [reg(3), reg(2), hearQ(n), reg(2), reg(3), hearQ(n)][n % 6],
  }; }

// ── lesson 2: the two houses, shown big, then the letters one at a time
const KQ_HZ = { small: { Ls: KQ_SMALL, ks: [0, 4], style: 'seg3', pk: 'pick', col: KQ.COD, name: ['The small house', '작은 집'] }, big: { Ls: KQ_BIG, ks: [5, 11], style: 'seg4', pk: 'pickB', col: KQ.BL, name: ['The big house', '큰 집'] } };
{ const ds = (arr) => arr.map(L => 28 + 'CDEFGAB'.indexOf(L));
  const hz = (kind, shown, cur, tkey, paint = true) => { const h = KQ_HZ[kind], small = kind === 'small', m = paint ? kqPaint({}, kqHouseKeys(1, small), h.style) : {}, nm = kqNames(1, shown);
    if (cur) m[KQ_PC[cur]] = h.pk;
    return { top: <KqRoofs oct={1} show={kind} vx={kqVx(h.ks[0], h.ks[1])} k={tkey}/>, kb: { bare: true, oct: 1, vx: kqVx(h.ks[0], h.ks[1]), mw: 290, marks: m, names: nm.names, ncol: nm.ncol } }; };
  const letters = (kind, c) => { const Ls = KQ_HZ[kind].Ls, n = Math.min(c.tk, Ls.length); return hz(kind, Ls.slice(0, n), c.tk >= 1 && c.tk <= Ls.length ? Ls[c.tk - 1] : null, 'l'); };
  const both = (cur, upto = 4) => { const ids = [0, 1, 2, 3].filter(x => x < upto), m = {}, names = {}, ncol = {};
    ids.forEach(id => { const o = Math.floor(id / 2), small = id % 2 === 0; kqPaint(m, kqHouseKeys(o + 1, small, o), small ? 'seg3' : 'seg4'); (small ? KQ_SMALL : KQ_BIG).forEach(L => { names[o * 12 + KQ_PC[L]] = L; ncol[o * 12 + KQ_PC[L]] = kqHouseCol(L); }); });
    if (cur != null && m[cur]) m[cur] = KQ_SMALL.includes(KQ_L[cur % 12] || (KQ_BK2.includes(cur % 12) ? 'C' : 'F')) ? 'pick' : 'pickB';
    return { top: <KqRoofs oct={2} only={ids}/>, kb: { oct: 2, base: 0, marks: m, names, ncol, plain: true } }; };
  KQ_SPEC['kq-houses'] = {
    title: ['Two houses', '두 채의 집'], allLine: ['The black keys build two kinds of house, and the white keys live inside them.', '검은건반이 집 두 채를 짓고, 흰건반이 그 안에 살아요.'],
    fig: (c) => both(typeof c.last === 'number' ? c.last : null, c.tk),
    steps: [
      { title: KQ_HZ.small.name, line: ['Two black keys make the roof, and three white keys live underneath.', '검은건반 두 개가 지붕이 되고, 그 아래 흰건반 세 개가 살아요.'], fig: (c) => hz('small', [], null, 's', c.tk >= 1) },
      { title: ['Meet C, D and E', 'C, D, E를 만나 봐요'], line: ['C waits at the left door, D lives inside, and E waits at the right door.', 'C는 왼쪽 문, D는 집 안, E는 오른쪽 문에 있어요.'], fig: (c) => letters('small', c) },
      { title: KQ_HZ.big.name, line: ['Three black keys make the roof, and four white keys live underneath.', '검은건반 세 개가 지붕이 되고, 그 아래 흰건반 네 개가 살아요.'], fig: (c) => hz('big', [], null, 'b', c.tk >= 1) },
      { title: ['Meet F, G, A and B', 'F, G, A, B를 만나 봐요'], line: ['F waits at the left door, G and A live inside, and B waits at the right door.', 'F는 왼쪽 문, G와 A는 집 안, B는 오른쪽 문에 있어요.'], fig: (c) => letters('big', c) },
      { title: ['Round and round', '돌고 돌아요'], line: ['Small house, big house, small house, big house: tap the keys to hear each name’s place.', '작은 집, 큰 집, 작은 집, 큰 집: 건반을 눌러 각 이름의 자리를 들어 보세요.'], fig: (c) => both(typeof c.last === 'number' ? c.last : null, c.tk) },
    ],
    make: (n, prev) => { let L; do { L = kqPick(KQ_ABC.filter(x => x !== 'A' || true)); } while (prev && prev.L === L); const small = KQ_SMALL.includes(L), hk = kqHouseKeys(2, true).concat(kqHouseKeys(2, false)), m = {}; hk.forEach(k => { m[k] = KQ_SMALL.includes(KQ_L[k % 12] || (KQ_BK2.includes(k % 12) ? 'C' : 'F')) ? 'seg3' : 'seg4'; });
      return { L, kind: 'key', retry: true, prompt: ['Tap ' + L + '.', L + ' 건반을 눌러 보세요.'], fig: () => ({ top: <KqRoofs oct={2}/>, kb: { bare: true, oct: 2, base: 0, marks: m } }), ok: (k) => k % 12 === KQ_PC[L],
        yes: ['Yes, ' + L + ' is ' + KQ_DOOR[L][2][0] + '.', '맞아요. ' + L + '는 ' + KQ_DOOR[L][2][1] + '에 있어요.'],
        no: (k) => [(KQ_L[k % 12] ? 'That is ' + KQ_L[k % 12] + '. ' : 'That is a black key. ') + L + ' is ' + KQ_DOOR[L][2][0] + '.', (KQ_L[k % 12] ? '그건 ' + KQ_L[k % 12] + '예요. ' : '그건 검은건반이에요. ') + L + '는 ' + KQ_DOOR[L][2][1] + '에 있어요.'] }; },
  }; }

// ── lesson 3: the same name all along the keyboard, middle C, and 12 keys with 7 names
{ const O = 3, N = O * 12, base = -12;
  const same = (Ls, cur) => { const m = {}; const nm = kqNames(O, Ls); Ls.forEach(L => { for (let o = 0; o <= O; o++) { const k = o * 12 + KQ_PC[L]; if (k <= N) { m[k] = KQ_SMALL.includes(L) ? 'seg3' : 'seg4'; if (k <= N && k % 12 === 0 && o === O) { nm.names[k] = L; nm.ncol[k] = kqHouseCol(L); } } } }); if (cur != null) m[cur] = KQ_SMALL.includes(KQ_L[cur % 12]) ? 'pick' : 'pickB'; return { oct: O, base, marks: m, names: nm.names, ncol: nm.ncol, plain: true }; };
  const allNames = (cur) => same(['C', 'D', 'E', 'F', 'G', 'A', 'B'], cur);
  const twelve = (c) => { const n = Math.min(c.tk, 12), m = {}; for (let k = 0; k < n; k++) m[k] = 'seg3'; const nm = c.tk >= 14 ? kqNames(1, ['C', 'D', 'E', 'F', 'G', 'A', 'B']) : { names: {}, ncol: {} }; if (c.tk >= 14) m[12] = 'pick';
    return { top: kqNumRow(kqVx(0, 12), Array.from({ length: n }, (_, k) => ({ x: kqX(k), t: String(k + 1), col: KQ.NV })), 15), kb: { oct: 1, base: 0, marks: m, names: nm.names, ncol: nm.ncol, mw: 340, plain: true } }; };
  const multi = (L, prev) => { const pc = KQ_PC[L], targets = []; for (let o = 0; o <= O; o++) if (o * 12 + pc <= N) targets.push(o * 12 + pc);
    return { L, kind: 'multi', retry: true, targets, prompt: ['Tap every ' + L + ' on the keyboard.', L + ' 건반을 모두 눌러 보세요.'], prog: (a, b) => ['Found ' + a + ' of ' + b + '. Keep going.', b + '개 중 ' + a + '개를 찾았어요. 계속해요.'],
      fig: () => ({ kb: { bare: true, oct: O, base } }), yes: ['All ' + targets.length + ' found: every pattern has one.', '모두 ' + targets.length + '개 찾았어요. 무늬마다 하나씩 있어요.'],
      no: (k) => [(KQ_L[((k % 12) + 12) % 12] ? 'That is ' + KQ_L[((k % 12) + 12) % 12] + '. ' : 'That is a black key. ') + L + ' is ' + KQ_DOOR[L][2][0] + '.', (KQ_L[((k % 12) + 12) % 12] ? '그건 ' + KQ_L[((k % 12) + 12) % 12] + '예요. ' : '그건 검은건반이에요. ') + L + '는 ' + KQ_DOOR[L][2][1] + '에 있어요.'] }; };
  const nextL = (prev) => { let L; do { L = kqPick(KQ_ABC); } while (prev && prev.L === L); return L; };
  KQ_SPEC['kq-names'] = {
    title: ['Every key has its place', '모든 건반에는 제 자리가 있어요'], allLine: ['The seven names go round and round, so every letter appears again in each pattern. Tap a key to hear it.', '이름 일곱 개가 돌고 돌아서, 무늬마다 같은 글자가 다시 나와요. 건반을 눌러 들어 보세요.'],
    fig: (c) => ({ kb: c.tk >= 1 || typeof c.last === 'number' ? allNames(typeof c.last === 'number' ? c.last : null) : { oct: O, base } }),
    steps: [
      { title: ['Every C', '모든 C'], line: ['Each C waits at the left door of a small house.', 'C는 모두 작은 집의 왼쪽 문에 서 있어요.'], fig: () => ({ kb: same(['C']) }) },
      { title: ['One letter at a time', '글자 하나씩'], line: ['Watch: the same letter lights up in every pattern.', '보세요. 같은 글자가 무늬마다 켜져요.'], fig: (c) => ({ kb: c.tk < 1 ? { oct: O, base } : same(['DEFGAB'[Math.min(Math.floor((c.tk - 1) / 2), 5)]]) }) },
      { title: ['Middle C', '가운데 도'], line: ['One C has a name of its own: the C in the middle of the keyboard.', 'C 하나는 이름이 따로 있어요. 건반 한가운데 있는 C예요.'], fig: () => ({ kb: { ...same(['C'], 12) } }) },
      { title: ['Twelve keys, seven names', '건반 열두 개, 이름 일곱 개'], line: ['Count every key in one pattern, black ones too. Only the white keys have letters.', '무늬 하나의 건반을 검은건반까지 모두 세어 보세요. 글자가 있는 건 흰건반뿐이에요.'], fig: (c) => twelve(c) },
    ],
    make: (n, prev) => [() => multi(nextL(prev), prev), () => ({ L: null, kind: 'key', retry: true, prompt: KQ_MC[n % 3].p, fig: () => ({ kb: { bare: true, oct: O, base } }), ok: (k) => k === [12, 24, 0][n % 3], yes: KQ_MC[n % 3].y,
        no: (k) => k % 12 === 0 ? ['That is a C, but not the right one. Count patterns from the middle.', '그건 C지만 찾는 C가 아니에요. 한가운데에서 무늬를 세어 보세요.'] : ['That is not a C. A C waits at the left door of a small house, just before two black keys.', '그건 C가 아니에요. C는 작은 집의 왼쪽 문, 검은건반 두 개 바로 앞에 있어요.'] }),
      () => multi(nextL(prev), prev), () => ({ L: null, kind: 'choice', cols: 4, prompt: ['Which name comes after B?', 'B 다음에 오는 이름은?'], opts: kqLet7(), ans: 'C', ok: (v) => v === 'C', fig: () => ({ kb: { bare: true, oct: 1, base: 0, marks: { 11: 'seg4', 12: 'pass' } } }),
        yes: ['C again: the next pattern has begun.', '다시 C예요. 다음 무늬가 시작됐어요.'], no: ['After B the names start over at C.', 'B 다음에는 이름이 처음부터 다시 시작해서 C가 와요.'] })][n % 4](),
  }; }

// ══ 2. The staff and clefs ══
KQ_SPEC['kq-lines'] = {
  title: ['Five lines, four spaces', '줄 다섯, 칸 넷'], allLine: ['Notes sit on the lines and in the spaces between them.', '음표는 줄 위에도, 줄 사이 칸에도 앉아요.'],
  fig: () => ({ staff: <KqLines labels/> }),
  steps: [
    { title: ['The lines', '줄'], line: ['There are five. Count from the bottom: the lowest is line 1.', '다섯 개예요. 아래에서부터 세요: 가장 아래가 1번 줄이에요.'], fig: () => ({ staff: <KqLines labels hl={{ type: 'line', n: 1 }}/> }) },
    { title: ['The spaces', '칸'], line: ['There are four, between the lines. The lowest is space 1.', '줄 사이에 네 개 있어요. 가장 아래가 1번 칸이에요.'], fig: () => ({ staff: <KqLines labels hl={{ type: 'space', n: 1 }}/> }) },
  ],
  make: (n) => { const type = n % 2 === 0 ? 'line' : 'space', max = type === 'line' ? 5 : 4, num = 1 + kqRnd(max), what = type === 'line' ? ['line', '줄'] : ['space', '칸'];
    return { kind: 'tap', retry: true, prompt: ['Tap the ' + kqOrd(num) + ' ' + what[0] + '.', kqOrd(num) + ' ' + what[1] + '을 눌러 보세요.'], fig: (c) => ({ staff: <KqLines onTap={c.pick} pickd={c.pickd} ok={c.res === 'ok'}/> }), ok: (v) => v.type === type && v.n === num,
      yes: ['You counted from the bottom.', '아래에서부터 잘 세었어요.'], no: (v) => ['That is ' + (v.type === 'line' ? 'line ' : 'space ') + v.n + '. Start again from the bottom.', '그건 ' + v.n + '번 ' + (v.type === 'line' ? '줄' : '칸') + '이에요. 다시 아래에서부터 세어 보세요.'] }; },
};
const kqClef = (c) => { const tr = c === 'treble'; return {
  title: tr ? ['The treble clef', '높은음자리표'] : ['The bass clef', '낮은음자리표'],
  allLine: tr ? ['This sign belongs to the Queen. She sings high.', '이 기호는 여왕의 것이에요. 여왕은 높은 목소리로 노래해요.'] : ['This sign belongs to the King. He sings low.', '이 기호는 왕의 것이에요. 왕은 낮은 목소리로 노래해요.'],
  fig: () => ({ staff: kqStaff(tr ? [32, 33, 34, 35] : [22, 23, 24, 25], c), kb: { oct: 3, base: tr ? 0 : -12, marks: tr ? kqPaint({}, Array.from({ length: 24 }, (_, i) => 12 + i), 'seg3') : kqPaint({}, Array.from({ length: 12 }, (_, i) => i), 'seg4') } }),
  steps: [
    { title: tr ? ['Her notes', '여왕의 음'] : ['His notes', '왕의 음'], line: tr ? ['They are on the right of the piano, the high side.', '피아노 오른쪽, 높은 쪽에 있어요.'] : ['They are on the left of the piano, the low side.', '피아노 왼쪽, 낮은 쪽에 있어요.'],
      fig: () => ({ staff: kqStaff(tr ? [32, 33, 34, 35] : [22, 23, 24, 25], c), kb: { oct: 3, base: tr ? 0 : -12, marks: tr ? kqPaint({}, Array.from({ length: 24 }, (_, i) => 12 + i), 'seg3') : kqPaint({}, Array.from({ length: 12 }, (_, i) => i), 'seg4') } }) },
    { title: tr ? ['Her hand', '여왕의 손'] : ['His hand', '왕의 손'], line: tr ? ['The right hand usually plays them.', '보통 오른손이 쳐요.'] : ['The left hand usually plays them.', '보통 왼손이 쳐요.'],
      fig: () => ({ staff: kqStaff(tr ? [32, 33, 34, 35] : [22, 23, 24, 25], c), kb: { oct: 3, base: tr ? 0 : -12, marks: tr ? kqPaint({}, Array.from({ length: 24 }, (_, i) => 12 + i), 'seg3') : kqPaint({}, Array.from({ length: 12 }, (_, i) => i), 'seg4') } }) },
    { title: tr ? ['The curl'] .concat(['말린 부분']) : ['The two dots', '두 점'], line: tr ? ['It winds round the second line. That line is G.', '둘째 줄을 감싸요. 그 줄이 G예요.'] : ['They sit either side of the fourth line. That line is F.', '넷째 줄 양쪽에 있어요. 그 줄이 F예요.'],
      fig: () => ({ staff: kqStaff(tr ? [32] : [24], c, { ring: [0], under: true }), kb: { oct: 3, base: tr ? 0 : -12, marks: { [tr ? 7 : 5]: tr ? 'pick' : 'pickB' } } }) },
  ],
  make: (n) => n % 2 === 0 ? { kind: 'choice', cols: 3, prompt: tr ? ['Which line does the treble clef wind round?', '높은음자리표는 어느 줄을 감쌀까요?'] : ['Which line do the two dots of the bass clef surround?', '낮은음자리표의 두 점은 어느 줄 양쪽에 있을까요?'],
    opts: (tr ? [1, 2, 3] : [3, 4, 5]).map(x => ({ id: String(x), label: () => t('Line ' + x, x + '번 줄') })), ans: tr ? '2' : '4', ok: (v) => v === (tr ? '2' : '4'),
    fig: (cx) => ({ staff: kqStaff(tr ? [32] : [24], c, { ring: cx.res ? [0] : [], under: !!cx.res }) }), yes: tr ? ['Line 2 is G.', '2번 줄이 G예요.'] : ['Line 4 is F.', '4번 줄이 F예요.'], no: tr ? ['G lives on line 2, where the curl winds.', 'G는 2번 줄에 있어요. 말린 부분이 감싸는 곳이에요.'] : ['F lives on line 4, between the dots.', 'F는 4번 줄에 있어요. 두 점 사이예요.'] }
    : { kind: 'choice', prompt: tr ? ['Which hand usually plays the treble clef?', '높은음자리표는 보통 어느 손이 칠까요?'] : ['Which hand usually plays the bass clef?', '낮은음자리표는 보통 어느 손이 칠까요?'], opts: [{ id: 'L', label: () => t('The left hand', '왼손') }, { id: 'R', label: () => t('The right hand', '오른손') }], ans: tr ? 'R' : 'L', ok: (v) => v === (tr ? 'R' : 'L'),
      fig: () => ({ staff: kqStaff(tr ? [32, 33, 34] : [23, 22, 21], c) }), yes: tr ? ['High notes go to the right hand.', '높은 음은 오른손 몫이에요.'] : ['Low notes go to the left hand.', '낮은 음은 왼손 몫이에요.'], no: tr ? ['Treble is the high clef, so the right hand.', '높은음자리표는 높은 쪽이라 오른손이에요.'] : ['Bass is the low clef, so the left hand.', '낮은음자리표는 낮은 쪽이라 왼손이에요.'] },
}; };
KQ_SPEC['kq-treble'] = kqClef('treble');
KQ_SPEC['kq-bass'] = kqClef('bass');
KQ_SPEC['kq-grand'] = {
  title: ['Two staves', '오선 둘'], allLine: ['Piano music uses both clefs at once, one staff above the other.', '피아노 악보는 두 음자리표를 한꺼번에 써요. 오선 하나가 다른 오선 위에 놓여요.'],
  fig: () => ({ staff: <>{kqStaff([33, 35], 'treble')}{kqStaff([23, 21], 'bass')}</>, kb: { oct: 3, base: -12, marks: kqPaint(kqPaint({}, Array.from({ length: 12 }, (_, i) => i), 'seg4'), Array.from({ length: 24 }, (_, i) => 12 + i), 'seg3') } }),
  steps: [
    { title: ['On top', '위'], line: ['The treble staff is for the right hand.', '높은음자리 오선은 오른손이 읽어요.'], fig: () => ({ staff: kqStaff([33, 35], 'treble'), kb: { oct: 3, base: -12, marks: kqPaint({}, Array.from({ length: 24 }, (_, i) => 12 + i), 'seg3') } }) },
    { title: ['Underneath', '아래'], line: ['The bass staff is for the left hand.', '낮은음자리 오선은 왼손이 읽어요.'], fig: () => ({ staff: kqStaff([23, 21], 'bass'), kb: { oct: 3, base: -12, marks: kqPaint({}, Array.from({ length: 12 }, (_, i) => i), 'seg4') } }) },
  ],
  make: () => { const high = Math.random() < 0.5, k = high ? 15 + kqRnd(18) : 1 + kqRnd(9), ans = high ? 'T' : 'B'; return { kind: 'choice', prompt: ['Listen. Which staff would show this note?', '들어 보세요. 이 음은 어느 오선에 쓸까요?'], opts: [{ id: 'T', label: () => t('The top staff', '위 오선') }, { id: 'B', label: () => t('The bottom staff', '아래 오선') }], ans, ok: (v) => v === ans, play: () => playKey(k - 12, 0.9),
    fig: (c) => ({ kb: { oct: 3, base: -12, marks: { [k]: c.res ? 'good' : 'pick' } } }), yes: high ? ['High sound, right hand: the top staff.', '높은 소리, 오른손: 위 오선이에요.'] : ['Low sound, left hand: the bottom staff.', '낮은 소리, 왼손: 아래 오선이에요.'], no: high ? ['That key is on the right, so it is high: the top staff.', '그 건반은 오른쪽에 있어서 높아요: 위 오선이에요.'] : ['That key is on the left, so it is low: the bottom staff.', '그 건반은 왼쪽에 있어서 낮아요: 아래 오선이에요.'] }; },
};
KQ_SPEC['kq-climb'] = {
  title: ['Going up', '위로 올라가기'], allLine: ['A note that sits higher on the staff sounds higher.', '오선에서 더 위에 앉은 음표는 더 높은 소리가 나요.'],
  fig: () => ({ staff: kqStaff([30, 31, 32, 33, 34, 35], 'treble'), kb: { oct: 3, base: 0, marks: kqPaint({}, [4, 5, 7, 9, 11, 12], 'seg3') } }),
  steps: [
    { title: ['Step up', '한 칸 위로'], line: ['One step up the staff is the next white key to the right.', '오선에서 한 칸 오르면 흰건반은 한 칸 오른쪽이에요.'], fig: () => ({ staff: kqStaff([32, 33, 34], 'treble'), kb: { oct: 3, base: 0, marks: kqPaint({}, [7, 9, 11], 'seg3') } }) },
    { title: ['Step down', '한 칸 아래로'], line: ['One step down is the next white key to the left.', '한 칸 내려가면 흰건반은 한 칸 왼쪽이에요.'], fig: () => ({ staff: kqStaff([34, 33, 32], 'treble'), kb: { oct: 3, base: 0, marks: kqPaint({}, [7, 9, 11], 'seg3') } }) },
  ],
  make: () => { let a = 29 + kqRnd(10), b; do { b = 29 + kqRnd(10); } while (b === a); const ans = a > b ? '1' : '2'; return { kind: 'choice', prompt: ['Which note is higher?', '어느 음표가 더 높을까요?'], opts: [{ id: '1', label: () => t('The first', '처음 음표') }, { id: '2', label: () => t('The second', '나중 음표') }], ans, ok: (v) => v === ans, play: () => kqPlayDs([a, b]),
    fig: (c) => ({ staff: kqStaff([a, b], 'treble'), kb: c.res ? { oct: 3, base: 0, marks: { [dMidiKey(a)]: a > b ? 'pick' : 'seg3', [dMidiKey(b)]: b > a ? 'pick' : 'seg3' } } : null }),
    yes: ['Higher on the staff, further right on the keys.', '오선에서 더 위, 건반에서 더 오른쪽이에요.'], no: ['The ' + (a > b ? 'first' : 'second') + ' note sits higher, so it sounds higher.', (a > b ? '처음' : '나중') + ' 음표가 더 위에 있어서 더 높게 들려요.'] }; },
};

// ══ 3. Line and space names ══
const KQ_ST = { treble: { lines: [30, 32, 34, 36, 38], spaces: [31, 33, 35, 37], rhyme: ['E G B D F: Every Good Boy Deserves Fun', 'E G B D F: Every Good Boy Deserves Fun'], sp: ['F A C E: they spell FACE', 'F A C E: FACE라는 단어가 돼요'] },
  bass: { lines: [18, 20, 22, 24, 26], spaces: [19, 21, 23, 25], rhyme: ['G B D F A: Great Big Dragon Flies Away', 'G B D F A: Great Big Dragon Flies Away'], sp: ['A C E G: All Cows Eat Grass', 'A C E G: All Cows Eat Grass'] } };
const kqNameLesson = (clef) => { const S = KQ_ST[clef], tr = clef === 'treble';
  return {
    title: tr ? ['The treble staff', '높은음자리 오선'] : ['The bass staff', '낮은음자리 오선'], allLine: ['Every line and space has a letter. Lines first, then spaces.', '줄과 칸마다 글자가 있어요. 줄을 먼저, 그다음 칸을 배워요.'],
    fig: () => ({ staff: kqStaff([...S.lines, ...S.spaces].sort((a, b) => a - b), clef, { under: true }) }),
    steps: [
      { title: ['The lines', '줄'], line: S.rhyme, fig: () => ({ staff: kqStaff(S.lines, clef, { under: true }) }) },
      { title: ['The spaces', '칸'], line: S.sp, fig: () => ({ staff: kqStaff(S.spaces, clef, { under: true }) }) },
    ],
    make: () => { const d = kqPick([...S.lines, ...S.spaces]), L = kqLetter(d), isLine = S.lines.includes(d), n = isLine ? S.lines.indexOf(d) + 1 : S.spaces.indexOf(d) + 1;
      return { kind: 'choice', cols: 4, prompt: ['Name this note.', '이 음표의 이름을 말해요.'], opts: kqLet7(), ans: L, ok: (v) => v === L, fig: (c) => ({ staff: kqStaff([d], clef, { ring: [0], under: c.res ? true : null }) }),
        yes: [L + ', on ' + (isLine ? 'line ' : 'space ') + n + '.', L + '예요, ' + n + '번 ' + (isLine ? '줄' : '칸') + '에 있어요.'],
        no: [L + ', on ' + (isLine ? 'line ' : 'space ') + n + '. Remember: ' + (isLine ? S.rhyme[0] : S.sp[0]), L + '예요, ' + n + '번 ' + (isLine ? '줄' : '칸') + '이에요. 기억해요: ' + (isLine ? S.rhyme[1] : S.sp[1])] }; },
  }; };
KQ_SPEC['kq-ntreble'] = kqNameLesson('treble');
KQ_SPEC['kq-nbass'] = kqNameLesson('bass');
const KQ_HOP = [{ d: 21, n: ['bass C', '낮은음자리표 도'], c: 'bass' }, { d: 24, n: ['the King’s F', '왕의 F'], c: 'bass' }, { d: 28, n: ['middle C', '가운데 도'], c: 'treble' }, { d: 32, n: ['the Queen’s G', '여왕의 G'], c: 'treble' }, { d: 35, n: ['treble C', '높은음자리표 도'], c: 'treble' }];
KQ_SPEC['kq-landmarks'] = {
  title: ['Five landmarks', '기준 음 다섯 개'], allLine: ['Five notes are easy to remember. Use them to find your way around.', '기억하기 쉬운 음 다섯 개가 있어요. 길을 찾는 이정표예요.'],
  fig: () => ({ staff: <>{kqStaff([28, 32, 35], 'treble', { under: true })}{kqStaff([21, 24], 'bass', { under: true })}</> }),
  steps: [
    { title: ['The Queen’s G', '여왕의 G'], line: ['On line 2, where her curl winds round.', '2번 줄에 있어요. 말린 부분이 감싸는 곳이에요.'], fig: () => ({ staff: kqStaff([32], 'treble', { under: true, ring: [0] }) }) },
    { title: ['Treble C', '높은음자리표 도'], line: ['In space 3, a few steps above the Queen’s G.', '3번 칸에 있어요. 여왕의 G에서 몇 걸음 위예요.'], fig: () => ({ staff: kqStaff([32, 35], 'treble', { under: true, ring: [1] }) }) },
    { title: ['The King’s F', '왕의 F'], line: ['On line 4, between his two dots.', '4번 줄에 있어요. 두 점 사이예요.'], fig: () => ({ staff: kqStaff([24], 'bass', { under: true, ring: [0] }) }) },
    { title: ['Bass C', '낮은음자리표 도'], line: ['In space 2, a few steps below the King’s F.', '2번 칸에 있어요. 왕의 F에서 몇 걸음 아래예요.'], fig: () => ({ staff: kqStaff([24, 21], 'bass', { under: true, ring: [1] }) }) },
    { title: ['Middle C', '가운데 도'], line: ['Between the two staves, on a short line of its own.', '두 오선 사이, 자기만의 짧은 줄 위에 있어요.'], fig: () => ({ staff: kqStaff([28], 'treble', { under: true, ring: [0] }) }) },
  ],
  make: (n, prev) => { let H; do { H = kqPick(KQ_HOP); } while (prev && prev.H === H); return { H, kind: 'choice', cols: 1, prompt: ['Which landmark is this?', '어느 기준 음일까요?'], opts: KQ_HOP.map(x => ({ id: String(x.d), label: () => t(x.n[0], x.n[1]) })), ans: String(H.d), ok: (v) => v === String(H.d),
    fig: () => ({ staff: kqStaff([H.d], H.c, { ring: [0] }) }), yes: ['You know that one.', '잘 아는 음이네요.'], no: ['It is ' + H.n[0] + '.', H.n[1] + '이에요.'] }; },
};
KQ_SPEC['kq-count'] = {
  title: ['Count from a landmark', '기준 음에서 세기'], allLine: ['To name any note, start at the nearest landmark and count the steps. A line or a space is one step.', '어떤 음이든 가장 가까운 기준 음에서 걸음을 세요. 줄 하나, 칸 하나가 한 걸음이에요.'],
  fig: () => ({ staff: kqStaff([32, 33, 34], 'treble', { under: true, ring: [0] }) }),
  steps: [
    { title: ['A step up', '한 걸음 위'], line: ['From the Queen’s G, the next line or space up is A.', '여왕의 G에서 위의 다음 칸이 A예요.'], fig: () => ({ staff: kqStaff([32, 33], 'treble', { under: true, ring: [1] }) }) },
    { title: ['A step down', '한 걸음 아래'], line: ['The next one down is F.', '아래의 다음 칸은 F예요.'], fig: () => ({ staff: kqStaff([32, 31], 'treble', { under: true, ring: [1] }) }) },
  ],
  make: () => { const H = kqPick(KQ_HOP.filter(x => x.d !== 28)), off = kqPick([-2, -1, 1, 2]), d = H.d + off, L = kqLetter(d), a = Math.abs(off); return { kind: 'choice', cols: 4, prompt: ['Start from ' + H.n[0] + ' (ringed). Name the other note.', '동그라미 친 ' + H.n[1] + '에서 시작해요. 다른 음표의 이름을 말해요.'], opts: kqLet7(), ans: L, ok: (v) => v === L,
    fig: (c) => ({ staff: kqStaff([H.d, d], H.c, { ring: [0], under: c.res ? true : [0] }) }), yes: [L + ': ' + a + (a === 1 ? ' step ' : ' steps ') + (off > 0 ? 'up.' : 'down.'), L + '예요: ' + a + '걸음 ' + (off > 0 ? '위예요.' : '아래예요.')], no: ['Count ' + a + (a === 1 ? ' step ' : ' steps ') + (off > 0 ? 'up' : 'down') + ' from ' + kqLetter(H.d) + ': that is ' + L + '.', kqLetter(H.d) + '에서 ' + a + '걸음 ' + (off > 0 ? '위' : '아래') + '로 세면 ' + L + '이에요.'] }; },
};
KQ_SPEC['kq-read'] = {
  title: ['Read it, play it', '읽고 치기'], allLine: ['Read the note, then find its key. Tap a key to hear it.', '음표를 읽고, 그 건반을 찾아요. 건반을 누르면 소리가 나요.'],
  fig: () => ({ staff: kqStaff([32], 'treble', { under: true }), kb: { oct: 3, base: 0, marks: { 7: 'pick' }, names: { 7: 'G' }, ncol: { 7: KQ.COD } } }),
  steps: [
    { title: ['Treble: above middle C', '높은음자리: 가운데 도 위'], line: ['The Queen’s G is the G just above middle C.', '여왕의 G는 가운데 도 바로 위의 G예요.'], fig: () => ({ staff: kqStaff([32], 'treble', { under: true }), kb: { oct: 3, base: 0, marks: { 7: 'pick' }, names: { 7: 'G' }, ncol: { 7: KQ.COD } } }) },
    { title: ['Bass: below middle C', '낮은음자리: 가운데 도 아래'], line: ['The King’s F is the F just below middle C.', '왕의 F는 가운데 도 바로 아래의 F예요.'], fig: () => ({ staff: kqStaff([24], 'bass', { under: true }), kb: { oct: 3, base: -12, marks: { 5: 'pickB' }, names: { 5: 'F' }, ncol: { 5: KQ.BL } } }) },
  ],
  make: () => { const treble = Math.random() < 0.5, d = treble ? kqPick(KQ_ST.treble.lines.concat(KQ_ST.treble.spaces, [28, 39])) : kqPick(KQ_ST.bass.lines.concat(KQ_ST.bass.spaces, [27])), base = treble ? 0 : -12, tk = dMidiKey(d) - base, clef = treble ? 'treble' : 'bass';
    return { kind: 'key', retry: true, prompt: ['Which key is this note?', '이 음표는 어느 건반일까요?'], fig: () => ({ staff: kqStaff([d], clef), kb: { oct: 3, base } }), ok: (k) => k === tk, onPick: (k, ok) => { if (ok) playKey(dMidiKey(d), 0.6); },
      yes: ['That is ' + kqLetter(d) + '.', kqLetter(d) + '예요.'], no: (k) => KQ_L[((k % 12) + 12) % 12] === kqLetter(d) ? ['The right letter, but another ' + kqLetter(d) + '. Check which octave the note is in.', '글자는 맞지만 다른 ' + kqLetter(d) + '예요. 음표가 어느 옥타브인지 확인해 보세요.'] : ['That key is ' + (KQ_L[((k % 12) + 12) % 12] || 'a black key') + '. The note is ' + kqLetter(d) + ': count from ' + (treble ? 'the Queen’s G.' : 'the King’s F.'), '그 건반은 ' + (KQ_L[((k % 12) + 12) % 12] || '검은건반') + '이에요. 이 음은 ' + kqLetter(d) + '예요: ' + (treble ? '여왕의 G' : '왕의 F') + '에서 세어 보세요.'] }; },
};

// ══ 4. Ledger lines and 8va ══
const kqLedger = (o) => ({
  title: o.title, allLine: o.all, fig: () => ({ staff: kqStaff(o.show, o.clef, { under: true }) }),
  steps: o.steps.map(s => ({ title: s[0], line: s[1], fig: () => ({ staff: kqStaff(s[2], o.clef, { under: true, ring: s[3] || [] }) }) })),
  make: () => { const d = kqPick(o.ask), L = kqLetter(d); return { kind: 'choice', cols: 4, prompt: ['Name this note.', '이 음표의 이름을 말해요.'], opts: kqLet7(), ans: L, ok: (v) => v === L, fig: (c) => ({ staff: kqStaff([d], o.clef, { ring: [0], under: c.res ? true : null }) }), yes: [L + '.', L + '예요.'], no: [L + '. ' + o.hint[0], L + '예요. ' + o.hint[1]] }; },
});
KQ_SPEC['kq-above'] = kqLedger({ clef: 'treble', title: ['Above the staff', '오선 위'], all: ['A note too high for the five lines sits on a short extra line: a ledger line.', '다섯 줄보다 높은 음은 짧은 덧줄 위에 앉아요.'], show: [38, 39, 40, 41, 42], ask: [39, 40, 41, 42, 43], hint: ['From the top line F, G is the space above and A is the first ledger line.', '맨 윗줄 F에서, 위 칸이 G이고 첫 덧줄이 A예요.'],
  steps: [[['The first ledger line', '첫 번째 덧줄'], ['Above the top line F is the space G, then the first ledger line: A.', '맨 윗줄 F 위는 G 칸, 그 위 첫 덧줄은 A예요.'], [38, 39, 40], [2]], [['Higher still', '더 위로'], ['B sits in the next space, and C on the second ledger line.', '다음 칸이 B, 두 번째 덧줄이 C예요.'], [40, 41, 42], [2]]] });
KQ_SPEC['kq-below'] = kqLedger({ clef: 'bass', title: ['Below the staff', '오선 아래'], all: ['Notes too low for the five lines use ledger lines under the staff.', '다섯 줄보다 낮은 음은 오선 아래의 덧줄을 써요.'], show: [18, 17, 16, 15, 14], ask: [17, 16, 15, 14], hint: ['From the bottom line G, F is the space below and E is the first ledger line.', '맨 아랫줄 G에서, 아래 칸이 F이고 첫 덧줄이 E예요.'],
  steps: [[['The first ledger line', '첫 번째 덧줄'], ['Below the bottom line G is the space F, then the first ledger line: E.', '맨 아랫줄 G 아래는 F 칸, 그 아래 첫 덧줄은 E예요.'], [18, 17, 16], [2]], [['Lower still', '더 아래로'], ['D sits in the next space, and C on the second ledger line.', '다음 칸이 D, 두 번째 덧줄이 C예요.'], [16, 15, 14], [2]]] });
KQ_SPEC['kq-middlec'] = {
  title: ['Middle C on the page', '악보 위의 가운데 도'], allLine: ['One key, two places on the page: under the treble staff, or above the bass staff.', '건반은 하나인데 악보에서는 두 자리예요: 높은음자리 오선 아래, 또는 낮은음자리 오선 위.'],
  fig: () => ({ staff: <>{kqStaff([28], 'treble')}{kqStaff([28], 'bass')}</>, kb: { oct: 3, base: -12, names: { 12: 'C' }, ncol: { 12: KQ.COD }, marks: { 12: 'pick' } } }),
  steps: [
    { title: ['Under the treble staff', '높은음자리 오선 아래'], line: ['A short line below the lowest line.', '가장 아래 줄 밑의 짧은 줄이에요.'], fig: () => ({ staff: kqStaff([28], 'treble'), kb: { oct: 3, base: -12, names: { 12: 'C' }, ncol: { 12: KQ.COD }, marks: { 12: 'pick' } } }) },
    { title: ['Above the bass staff', '낮은음자리 오선 위'], line: ['A short line above the top line. It is the same key.', '가장 위 줄 위의 짧은 줄이에요. 같은 건반이에요.'], fig: () => ({ staff: kqStaff([28], 'bass'), kb: { oct: 3, base: -12, names: { 12: 'C' }, ncol: { 12: KQ.COD }, marks: { 12: 'pick' } } }) },
  ],
  make: () => { const treble = Math.random() < 0.5, d = kqPick([26, 27, 28, 29]), clef = treble ? 'treble' : 'bass', tk = dMidiKey(d) + 12;
    return { kind: 'key', retry: true, prompt: ['Find this note near middle C.', '가운데 도 근처의 이 음표를 찾아요.'], fig: () => ({ staff: kqStaff([d], clef), kb: { oct: 3, base: -12, names: { 12: 'C' }, ncol: { 12: KQ.COD } } }), ok: (k) => k === tk, onPick: (k, ok) => { if (ok) playKey(dMidiKey(d), 0.6); },
      yes: ['That is ' + kqLetter(d) + '.', kqLetter(d) + '예요.'], no: (k) => KQ_L[((k % 12) + 12) % 12] === kqLetter(d) ? ['The right letter, but another one. Look for the one nearest middle C.', '글자는 맞지만 다른 것이에요. 가운데 도에서 가장 가까운 것을 찾아요.'] : ['That key is ' + (KQ_L[((k % 12) + 12) % 12] || 'a black key') + '. The note is ' + kqLetter(d) + ': count from middle C.', '그 건반은 ' + (KQ_L[((k % 12) + 12) % 12] || '검은건반') + '이에요. 이 음은 ' + kqLetter(d) + '예요: 가운데 도에서 세어 보세요.'] }; },
};
KQ_SPEC['kq-8va'] = {
  title: ['8va', '8va'], allLine: ['Very high notes need many ledger lines, so 8va stands in: play it one octave higher than written.', '아주 높은 음은 덧줄이 너무 많아져서 8va를 써요: 쓴 것보다 한 옥타브 높게 쳐요.'],
  fig: () => ({ staff: kqStaff([38, 39, 40, 41], 'treble', { bracket: { from: 0, bar: 0, label: '8va' } }), kb: { oct: 3, base: 0, marks: kqPaint(kqPaint({}, [17, 19, 21, 23], 'seg3'), [29, 31, 33, 35], 'seg4') } }),
  steps: [
    { title: ['As written', '쓴 그대로'], line: ['Without a sign, you play the keys the notes sit on.', '기호가 없으면 음표가 앉은 그대로의 건반을 쳐요.'], fig: () => ({ staff: kqStaff([38, 39, 40, 41], 'treble'), kb: { oct: 3, base: 0, marks: kqPaint({}, [17, 19, 21, 23], 'seg3') } }) },
    { title: ['With 8va', '8va가 있으면'], line: ['The same letters, one octave up: coral is written, blue is what you play.', '같은 글자를 한 옥타브 위에서: 코랄은 쓴 음, 파랑은 실제로 치는 음이에요.'], fig: () => ({ staff: kqStaff([38, 39, 40, 41], 'treble', { bracket: { from: 0, bar: 0, label: '8va' } }), kb: { oct: 3, base: 0, marks: kqPaint(kqPaint({}, [17, 19, 21, 23], 'seg3'), [29, 31, 33, 35], 'seg4') } }) },
  ],
  make: () => { const d = kqPick([38, 39, 40, 41]), tk = dMidiKey(d) + 12; return { kind: 'key', retry: true, prompt: ['This note is under an 8va. Which key do you play?', '이 음표는 8va 아래에 있어요. 어느 건반을 칠까요?'], fig: () => ({ staff: kqStaff([d, d], 'treble', { bracket: { from: 0, bar: 0, label: '8va' } }), kb: { oct: 3, base: 0 } }), ok: (k) => k === tk, onPick: (k, ok) => { if (ok) playKey(tk, 0.6); },
    yes: ['One octave above the written ' + kqLetter(d) + '.', '쓴 ' + kqLetter(d) + ' 한 옥타브 위예요.'], no: ['Find the written ' + kqLetter(d) + ', then take the next ' + kqLetter(d) + ' to its right.', '쓴 ' + kqLetter(d) + '를 찾고, 그 오른쪽의 다음 ' + kqLetter(d) + '를 치세요.'] }; },
};

// ══ 5. Pitch and range ══
const kqBars = ({ lens, hl, onTap, pickd }) => <svg viewBox="0 0 320 120" style={{ width: '100%', maxWidth: 340, display: 'block', margin: '0 auto' }}>
  {lens.map((h, i) => { const x = 20 + i * (280 / lens.length) + 4, w = 280 / lens.length - 8, on = hl === i, pk = pickd === i; return <g key={i} onClick={() => onTap && onTap(i)} style={{ cursor: onTap ? 'pointer' : 'default' }}><rect x={x} y={14} width={w} height={h} rx="6" fill={pk ? '#fad0c2' : on ? '#fbe3da' : '#fffefa'} stroke={on || pk ? KQ.CO : KQ.NV} strokeWidth="3"/></g>; })}
</svg>;
const KQ_XY = [0, 2, 4, 5, 7, 9, 11, 12], KQ_LENS = [100, 92, 84, 78, 70, 62, 54, 46];
KQ_SPEC['kq-size'] = {
  title: ['Long and short', '긴 것과 짧은 것'], allLine: ['Tap the bars. Long ones sound low, short ones sound high.', '막대를 눌러 보세요. 긴 막대는 낮게, 짧은 막대는 높게 울려요.'],
  fig: (c) => ({ top: kqBars({ lens: KQ_LENS, hl: c.last, onTap: (i) => { playKey(KQ_XY[i], 0.7); c.setLast(i); } }) }),
  steps: [
    { title: ['The longest bar', '가장 긴 막대'], line: ['It makes the lowest sound.', '가장 낮은 소리가 나요.'], fig: () => ({ top: kqBars({ lens: KQ_LENS, hl: 0, onTap: (i) => playKey(KQ_XY[i], 0.7) }) }) },
    { title: ['The shortest bar', '가장 짧은 막대'], line: ['It makes the highest sound.', '가장 높은 소리가 나요.'], fig: () => ({ top: kqBars({ lens: KQ_LENS, hl: 7, onTap: (i) => playKey(KQ_XY[i], 0.7) }) }) },
  ],
  make: () => { const a = 30 + kqRnd(60), b = a + kqPick([-1, 1]) * (15 + kqRnd(30)), lens = [a, b], low = a > b ? 0 : 1; return { kind: 'tap', retry: true, prompt: ['Tap the bar that sounds lower.', '더 낮게 울리는 막대를 눌러 보세요.'], fig: (c) => ({ top: kqBars({ lens, onTap: (i) => { playKey(i === low ? 0 : 12, 0.7); c.pick(i); }, pickd: c.pickd }) }), ok: (i) => i === low,
    yes: ['The longer bar always sounds lower.', '더 긴 막대가 늘 더 낮게 울려요.'], no: ['That bar is shorter, so it rings higher.', '그 막대는 더 짧아서 더 높게 울려요.'] }; },
};
const KQ_PIANO = 'Piano (today, 88 keys)', KQ_RNG = [KQ_PIANO, 'Violin', 'Cello', 'Flute', 'Tuba', 'Soprano', 'Bass'];
const kqRangeFig = (name, c) => { const R = SPR_RANGE(name); return { top: <div style={{ maxWidth: 520, margin: '0 auto' }}><SprStrip range={[R.lo, R.hi]}/></div>,
  mid: <div style={{ display: 'flex', flexWrap: 'wrap', gap: 6, justifyContent: 'center', margin: '8px 0 0' }}>{KQ_RNG.map(n => <button key={n} className={'chip' + (n === name ? ' active' : '')} style={{ padding: '6px 12px', minHeight: 40 }} onClick={() => { const r = SPR_RANGE(n); sprPiano(r.lo); sprPiano(r.hi, 0.95); c.setLast(n); }}>{rangeName(n)}</button>)}</div> }; };
KQ_SPEC['kq-range'] = {
  title: ['How far a piano reaches', '피아노가 닿는 범위'], allLine: ['A piano covers a huge range. Tap a name to see how much of it another instrument covers.', '피아노는 아주 넓은 범위를 맡아요. 이름을 눌러 다른 악기가 그중 얼마를 맡는지 보세요.'],
  fig: (c) => kqRangeFig(c.last || KQ_PIANO, c),
  steps: [
    { title: ['The piano', '피아노'], line: ['88 keys, from A0 at the far left to C8 at the far right.', '건반 88개, 맨 왼쪽 A0에서 맨 오른쪽 C8까지예요.'], fig: (c) => kqRangeFig(KQ_PIANO, c) },
    { title: ['The others', '다른 악기들'], line: ['A violin, a cello or a voice each covers only a part.', '바이올린, 첼로, 목소리는 각각 일부만 맡아요.'], fig: (c) => kqRangeFig(c.last && c.last !== KQ_PIANO ? c.last : 'Violin', c) },
  ],
  make: () => { let a, b; do { a = kqPick(KQ_RNG.slice(1)); b = kqPick(KQ_RNG.slice(1)); } while (a === b || SPR_RANGE(a).lo === SPR_RANGE(b).lo); const low = SPR_RANGE(a).lo < SPR_RANGE(b).lo ? a : b; return { kind: 'choice', prompt: ['Which one reaches lower?', '어느 쪽이 더 낮은 음까지 내려갈까요?'], opts: [a, b].map(n => ({ id: n, label: () => rangeName(n) })), ans: low, ok: (v) => v === low,
    fig: (c) => ({ top: <div style={{ maxWidth: 520, margin: '0 auto' }}><SprStrip range={c.res ? [SPR_RANGE(low).lo, SPR_RANGE(low).hi] : null}/></div> }), play: () => { sprPiano(SPR_RANGE(a).lo); sprPiano(SPR_RANGE(b).lo, 0.95); },
    yes: [rangeName(low) + ' starts lower down.', rangeName(low) + '은(는) 더 낮은 곳에서 시작해요.'], no: ['It is the ' + rangeName(low) + ': its lowest note is lower.', rangeName(low) + '이(가) 정답이에요. 가장 낮은 음이 더 낮아요.'] }; },
};

// the registry: five sections, each lesson one idea
const kqRow = (id, en, ko, bEn, bKo) => [id, en, ko, bEn, bKo, () => <KqEngine spec={KQ_SPEC[id]}/>];
const KS_ROWS = [
  ['p-keys', [
    kqRow('kq-black', 'Black keys', '검은건반', 'Groups of 2 and 3, and low and high.', '2개와 3개씩 모인 검은건반, 낮은 소리와 높은 소리.'),
    kqRow('kq-houses', 'Two houses', '두 채의 집', 'C D E under two black keys, F G A B under three.', '검은건반 두 개 아래의 C D E, 세 개 아래의 F G A B.'),
    kqRow('kq-names', 'Every key has its place', '모든 건반에는 제 자리가 있어요', 'The same name everywhere, middle C, 12 keys and 7 names.', '어디서나 같은 이름, 가운데 도, 건반 12개와 이름 7개.'),
  ]],
  ['p-stf', [
    kqRow('kq-lines', 'Five lines, four spaces', '줄 다섯, 칸 넷', 'Counting lines and spaces from the bottom.', '아래에서부터 줄과 칸 세기.'),
    kqRow('kq-treble', 'The treble clef', '높은음자리표', 'The Queen: high, right hand, G.', '여왕: 높은 음, 오른손, G.'),
    kqRow('kq-bass', 'The bass clef', '낮은음자리표', 'The King: low, left hand, F.', '왕: 낮은 음, 왼손, F.'),
    kqRow('kq-grand', 'Two staves', '오선 둘', 'The treble staff above, the bass staff below.', '위의 높은음자리 오선, 아래의 낮은음자리 오선.'),
    kqRow('kq-climb', 'Going up', '위로 올라가기', 'Higher on the staff, higher on the piano.', '오선에서 위쪽은 건반에서 오른쪽.'),
  ]],
  ['p-lines', [
    kqRow('kq-ntreble', 'The treble staff', '높은음자리 오선', 'E G B D F on the lines, F A C E in the spaces.', '줄은 E G B D F, 칸은 F A C E.'),
    kqRow('kq-nbass', 'The bass staff', '낮은음자리 오선', 'G B D F A on the lines, A C E G in the spaces.', '줄은 G B D F A, 칸은 A C E G.'),
    kqRow('kq-landmarks', 'Five landmarks', '기준 음 다섯 개', 'Five notes that are easy to remember.', '기억하기 쉬운 음 다섯 개.'),
    kqRow('kq-count', 'Count from a landmark', '기준 음에서 세기', 'Name any note by counting steps.', '걸음을 세어 어떤 음이든 이름 붙이기.'),
    kqRow('kq-read', 'Read it, play it', '읽고 치기', 'From the note on the staff to its key.', '오선의 음표에서 그 건반까지.'),
  ]],
  ['p-ledger', [
    kqRow('kq-above', 'Above the staff', '오선 위', 'Ledger lines above the staff.', '오선 위의 덧줄.'),
    kqRow('kq-below', 'Below the staff', '오선 아래', 'Ledger lines below the staff.', '오선 아래의 덧줄.'),
    kqRow('kq-middlec', 'Middle C on the page', '악보 위의 가운데 도', 'One key, two places on the page.', '건반 하나, 악보 위 두 자리.'),
    kqRow('kq-8va', '8va', '8va', 'Play one octave higher than written.', '쓴 것보다 한 옥타브 높게 치기.'),
  ]],
  ['p-range', [
    kqRow('kq-size', 'Long and short', '긴 것과 짧은 것', 'Long bars sound low, short bars sound high.', '긴 막대는 낮게, 짧은 막대는 높게.'),
    kqRow('kq-range', 'How far a piano reaches', '피아노가 닿는 범위', 'The piano’s range next to other instruments.', '다른 악기와 비교한 피아노의 범위.'),
  ]],
];
