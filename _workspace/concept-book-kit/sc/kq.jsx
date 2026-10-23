// ─── Keys and staff, built again from the start in the Scales style (her call 2026-10-22: "make it new, not fitted into the old ones; use the final colours of the key signatures and scales; don't say the same thing twice").
// Look: the Scales keyboard (ScKeys: the names above the keys, the two-name black keys), coral and blue for the two groups (coral = the small house, 3 white keys; blue = the big house, 4 white keys),
// the key you tapped solid. Every lesson: the whole picture, one at a time, her turn. Title, line and feedback each say something new. The staff is shown on request in the keyboard lessons.
const KQ = { CO: '#e4572e', COD: '#c0431f', BL: '#3b4fa8', NV: '#26296b' };
const kqT = (a) => t(a[0], a[1]);
const kqYe = (w) => { const x = String(w), ch = x.slice(-1), c = ch.charCodeAt(0); const closed = /[♯♭]/.test(ch) || (c >= 0xAC00 && c <= 0xD7A3 && (c - 0xAC00) % 28 > 0); return x + (closed ? '이에요' : '예요'); };
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
const KQW = 560;
const kqW = (vx) => Math.min(KQW, Math.max(380, (vx[1] - vx[0]) * 1.5));
const KQ_BLK = [1, 3, 6, 8, 10];
const kqKb = (f0, onTap) => { let f = f0.keepBlack ? f0 : { ...f0, marks: Object.fromEntries(Object.entries(f0.marks || {}).filter(([k, v]) => !(KQ_BLK.includes(((+k % 12) + 12) % 12) && (v === 'seg3' || v === 'seg4')))) }; if (f0.mcOn && !f.bare) { const mc = -(f.base || 0), rg = f.ks || [0, f.oct * 12]; if (mc >= rg[0] && mc <= rg[1] && !(f.names && f.names[mc])) { const mk = { ...(f.marks || {}) }; if (!mk[mc]) mk[mc] = 'pass'; f = { ...f, marks: mk, names: { ...(f.names || {}), [mc]: 'C' }, ncol: { ...(f.ncol || {}), [mc]: KQ.COD }, cap: !!f0.mcCap }; } }
  const el = f.bare
  ? <div style={{ maxWidth: f.mw || kqW(f.vx || kqVx(0, f.oct * 12)), margin: '0 auto' }}><TapKeyboard octaves={f.oct} extraC marks={f.marks || {}} onTap={onTap} top={0} names={f.names || null} nameCol={f.ncol || null} vx={f.vx || kqVx(0, f.oct * 12)}/></div>
  : <ScKeys ks={f.ks || [0, f.oct * 12]} oct={f.oct} marks={f.marks || {}} names={f.names || {}} ncol={f.ncol || {}} arcs={f.arcs || []} spans={f.spans || []} nonce={f.nonce || 0} onTap={onTap} mw={f.mw || kqW([kqX(f.ks ? f.ks[0] : 0) - 24, kqX(f.ks ? f.ks[1] : f.oct * 12) + 24])} plain={f.plain !== false}/>;
  return f.cap ? <>{el}<div style={{ textAlign: 'center', fontSize: 13.5, fontWeight: 800, color: KQ.COD, margin: '2px 0 0' }}>{t('C = middle C, the C near the middle of the keyboard', 'C = 가운데 도, 건반 한가운데 가까이의 C')}</div></> : el; };
// words or numbers above the keyboard, at the keys' own x (same crop as the keyboard under it, so they line up)
const kqNumRow = (vx, items, fs = 22, drop = 0) => { const sc = (vx[1] - vx[0]) / 430, h0 = (fs + 14) * sc, h = h0 + drop, w = kqW(vx), pxu = w / (vx[1] - vx[0]);
  return <div style={{ maxWidth: w, margin: '0 auto', marginBottom: drop ? -drop * pxu : 0, position: 'relative', zIndex: 1, pointerEvents: 'none' }}><svg viewBox={`${vx[0]} 0 ${vx[1] - vx[0]} ${h}`} style={{ width: '100%', display: 'block' }}>
  {items.map((it) => { const half = it.t.length * 0.3 * fs * sc + 2 * sc; const cx = Math.min(Math.max(it.x, vx[0] + half), vx[1] - half);
    return <g key={it.t + ':' + it.x} style={{ animation: 'fadeUp 0.3s both' }}>
      {drop > 0 && it.ln && <line x1={it.x} x2={it.x} y1={h0 - 4 * sc} y2={h} stroke={it.col} strokeWidth={(it.lw || 1.6) * sc} strokeLinecap="round" opacity={it.lo == null ? 0.9 : it.lo}/>}
      <text x={cx} y={h0 - 8 * sc} textAnchor="middle" fontSize={fs * sc} fontWeight="900" fill={it.col}>{it.t}</text></g>; })}</svg></div>; };
// roofs, drawn in the keyboard's own coordinates (so they sit exactly over the black keys)
function KqRoofs({ oct = 2, show = 'both', vx, k = 0, only = null }) {   // the bracket and count over a black-key group (kept the old name)
  const hs = []; for (let o = 0; o < oct; o++) { hs.push({ small: true, x1: o * 252 + 25, x2: o * 252 + 83, id: o * 2 }); hs.push({ small: false, x1: o * 252 + 133, x2: o * 252 + 227, id: o * 2 + 1 }); }
  const v = vx || [-6, oct * 252 + 42], sc = (v[1] - v[0]) / 430, H = 44 * sc;
  return <div style={{ maxWidth: kqW(v), margin: '0 auto' }}><svg viewBox={`${v[0]} 0 ${v[1] - v[0]} ${H}`} style={{ width: '100%', display: 'block' }}>
    {hs.filter(h => (show === 'both' || (show === 'small') === h.small) && (!only || only.includes(h.id))).map(h => { const col = h.small ? KQ.CO : KQ.BL, mid = (h.x1 + h.x2) / 2;
      return <g key={h.id + ':' + k} style={{ animation: 'fadeUp 0.4s both' }}>
        <path d={`M${h.x1},${H - 2 * sc} V${H - 12 * sc} H${h.x2} V${H - 2 * sc}`} fill="none" stroke={col} strokeWidth={3 * sc} strokeLinejoin="round"/>
        <text x={mid} y={H - 17 * sc} textAnchor="middle" fontSize={20 * sc} fontWeight="900" fill={col}>{h.small ? 2 : 3}</text></g>; })}
  </svg></div>;
}
const kqFeed = (ok, txt) => <div style={{ textAlign: 'center', fontSize: 14.5, fontWeight: 900, minHeight: 40, margin: '8px 0 0', color: ok === true ? '#2e8a6e' : ok === false ? '#c8361b' : KQ.NV, textWrap: 'balance' }}>{txt}</div>;
// the black-key groups: a bracket and its count (coral 2, blue 3), in the keyboard's coordinates
function KqGroupsTop({ oct = 2, show = 'both', lit = null, onTap, upto = 99 }) {
  const items = []; for (let o = 0; o < oct; o++) [[1, 3], [6, 8, 10]].forEach((g, gi) => { const c = (k) => o * 252 + (k === 1 ? 36 : k === 3 ? 72 : k === 6 ? 144 : k === 8 ? 180 : 216); items.push({ n: g.length, x1: c(g[0]) - 11, x2: c(g[g.length - 1]) + 11, keys: g.map(k => o * 12 + k), id: o * 2 + gi }); });
  return <div style={{ maxWidth: kqW([-6, oct * 252 + 42]), margin: '0 auto' }}><svg viewBox={`-6 0 ${oct * 252 + 48} 40`} style={{ width: '100%', display: 'block' }}>
    {items.map(it => { const col = it.n === 2 ? KQ.CO : KQ.BL, on = !!lit && lit.g === it.id, dim = show !== 'both' && show !== it.n, mid = (it.x1 + it.x2) / 2, hid = it.id >= upto;
      return <g key={it.id} onClick={() => onTap && onTap(it)} style={{ cursor: onTap ? 'pointer' : 'default', opacity: hid ? 0 : dim ? 0.18 : 1, transition: 'opacity 0.35s' }}>
        <path d={`M${it.x1},36 V26 H${it.x2} V36`} fill="none" stroke={col} strokeWidth={on ? 4.5 : 3} strokeLinejoin="round"/>
        <text x={mid} y="18" textAnchor="middle" fontSize="19" fontWeight="900" fill={col}>{it.n}</text></g>; })}
  </svg></div>;
}
const kqArrow = (pos, n) => <div style={{ maxWidth: 560, margin: '0 auto' }}><svg viewBox="0 0 500 34" style={{ width: '100%', display: 'block' }}>
  <text x="20" y="12" fontSize="13" fontWeight="900" fill={KQ.COD}>{t('← low', '← 낮은 소리')}</text><text x="480" y="12" textAnchor="end" fontSize="13" fontWeight="900" fill={KQ.BL}>{t('high →', '높은 소리 →')}</text>
  <line x1="20" y1="24" x2="470" y2="24" stroke={KQ.NV} strokeWidth="3"/><path d="M468 16 L486 24 L468 32 Z" fill={KQ.NV}/>
  {pos != null && <circle cx={20 + 450 * (pos + 0.5) / n} cy="24" r="8" fill={KQ.CO} style={{ transition: 'cx 0.25s' }}/>}
</svg></div>;
// the staff, as in the Scales lessons (SkgStaff)
const kqStaff = (ds, clef, o = {}) => {
  const items = ds.map(d => ['q', 1, d]).concat([['||']]);
  const oo = { boxS: 26, D: 30, ring: o.ring || [], ...(o.under ? skgUnder(items, 'C', o.under === true ? null : o.under, o.coral || []) : {}) };
  if (o.bracket) { items.splice(ds.length, 0, ['|']); oo.bracket = o.bracket; }
  return <div style={{ maxWidth: 480, margin: '0 auto' }}><SkgStaff items={items} k="C" clef={clef} width={330} o={oo}/></div>;
};
// five lines and four spaces, counted from the bottom
function KqLines({ hl, labels, onTap, pickd, ok }) {
  const yl = (n) => 116 - (n - 1) * 26, col = (type, n) => hl && hl.type === type && hl.n === n ? KQ.CO : KQ.NV, pk = (type, n) => pickd && pickd.type === type && pickd.n === n;
  return <svg viewBox="0 0 320 130" style={{ width: '100%', display: 'block', maxWidth: KQW, margin: '0 auto' }}>
    {[1, 2, 3, 4].map(n => <rect key={'s' + n} x="40" y={yl(n + 1) + 7} width="240" height="12" rx="4" fill={pk('space', n) ? (ok ? '#cfe8dd' : '#f6c9bf') : hl && hl.type === 'space' && hl.n === n ? '#fbe3da' : 'transparent'} onClick={() => onTap && onTap({ type: 'space', n })} style={{ cursor: onTap ? 'pointer' : 'default' }}/>)}
    {[1, 2, 3, 4, 5].map(n => <g key={'l' + n} onClick={() => onTap && onTap({ type: 'line', n })} style={{ cursor: onTap ? 'pointer' : 'default' }}>
      <rect x="40" y={yl(n) - 7} width="240" height="14" fill="transparent"/>
      <line x1="40" x2="280" y1={yl(n)} y2={yl(n)} stroke={pk('line', n) ? (ok ? '#2e8a6e' : '#c8361b') : col('line', n)} strokeWidth={hl && hl.type === 'line' && hl.n === n || pk('line', n) ? 4 : 2}/></g>)}
    {labels && [1, 2, 3, 4, 5].map(n => <text key={'tl' + n} x="22" y={yl(n) + 5} textAnchor="middle" fontSize="15" fontWeight="900" fill={col('line', n)}>{n}</text>)}
    {labels && [1, 2, 3, 4].map(n => <text key={'ts' + n} x="300" y={yl(n) - 8} textAnchor="middle" fontSize="15" fontWeight="900" fill={col('space', n)}>{n}</text>)}
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
      {kb && kqKb({ ...kb, marks, keepBlack: !!kb.keepBlack || spec === KQ_SPEC['kq-black'], mcOn: !!kb.mcOn || ['kq-climb', 'kq-clefs', 'kq-read', 'kq-middlec'].some(id => spec === KQ_SPEC[id]), mcCap: spec === KQ_SPEC['kq-climb'] }, (k) => { playKey(k + (kb.base || 0), 0.6); setLast(k); if (view === 'try' && q && (q.kind === 'key' || q.kind === 'multi')) pick(k); else if (kb.onTap) kb.onTap(k); })}
      {allowStaff && f.staffAlt && <>
        <div style={{ textAlign: 'center', margin: '8px 0 0' }}><button className="ghost-btn" style={{ ...scS.back, minWidth: 0, fontSize: 14 }} onClick={() => setStf(!stf)}>{stf ? t('Hide the staff', '오선 숨기기') : t('Show on the staff', '오선으로 보여주기')}</button></div>
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
      <button className="ghost-btn" style={scS.prim} onClick={() => si < steps.length - 1 ? go('step', si + 1) : spec.onLast ? spec.onLast() : startTry()}>{si < steps.length - 1 ? t('Next →', '다음 →') : spec.lastLabel ? kqT(spec.lastLabel) : t('Your turn →', '내가 해보기 →')}</button>
    </>)}
  </>; }
  else if (q) { const f = q.fig(ctx);
    const txt = res === 'ok' ? [kqT(q.yes), true] : res === 'no' ? [kqT(typeof q.no === 'function' ? q.no(pickd) : q.no), false] : q.kind === 'multi' && found.length ? [kqT(q.prog(found.length, q.targets.length)), true] : ['', null];
    body = <>
      {tit(spec.tryTitle || ['Your turn', '내가 해보기'])}{lin(q.prompt)}{kqFeed(txt[1], txt[0])}{show(f, false)}
      {q.opts && <div style={{ display: 'grid', gridTemplateColumns: 'repeat(' + (q.cols || 2) + ',1fr)', gap: 8, margin: '10px 0 0' }}>
        {q.opts.map(o => <button key={o.id} className={'choice-btn' + (res == null ? '' : o.id === q.ans ? ' good' : o.id === pickd ? ' bad' : '')} disabled={res != null} onClick={() => pick(o.id)} style={{ gridColumn: o.span ? '1 / -1' : undefined, padding: '13px 4px', fontSize: q.cols > 3 ? 18 : 16, fontWeight: 900 }}>{typeof o.label === 'function' ? o.label() : o.label}</button>)}
      </div>}
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
// where each white key sits next to the black-key groups: [title, line, phrase for feedback, short label]
const KQ_DOOR = {
  C: [['C: left of the 2', 'C: 2개 묶음의 왼쪽'], ['It sits just left of the group of 2.', '2개 묶음 바로 왼쪽에 있어요.'], ['just left of the group of 2', '2개 묶음 바로 왼쪽'], ['left', '왼쪽']],
  D: [['D: between the 2', 'D: 2개 사이'], ['It sits between the two black keys.', '두 검은건반 사이에 있어요.'], ['between the two black keys', '두 검은건반 사이'], ['between', '사이']],
  E: [['E: right of the 2', 'E: 2개 묶음의 오른쪽'], ['It sits just right of the group of 2.', '2개 묶음 바로 오른쪽에 있어요.'], ['just right of the group of 2', '2개 묶음 바로 오른쪽'], ['right', '오른쪽']],
  F: [['F: left of the 3', 'F: 3개 묶음의 왼쪽'], ['It sits just left of the group of 3.', '3개 묶음 바로 왼쪽에 있어요.'], ['just left of the group of 3', '3개 묶음 바로 왼쪽'], ['left', '왼쪽']],
  G: [['G: first gap in the 3', 'G: 3개 묶음의 첫째 틈'], ['It sits between the 1st and 2nd black keys of the group of 3.', '3개 묶음의 첫째와 둘째 검은건반 사이에 있어요.'], ['between the 1st and 2nd black keys of the group of 3', '3개 묶음의 첫째와 둘째 검은건반 사이'], ['first gap', '첫째 틈']],
  A: [['A: second gap in the 3', 'A: 3개 묶음의 둘째 틈'], ['It sits between the 2nd and 3rd black keys of the group of 3.', '3개 묶음의 둘째와 셋째 검은건반 사이에 있어요.'], ['between the 2nd and 3rd black keys of the group of 3', '3개 묶음의 둘째와 셋째 검은건반 사이'], ['second gap', '둘째 틈']],
  B: [['B: right of the 3', 'B: 3개 묶음의 오른쪽'], ['It sits just right of the group of 3.', '3개 묶음 바로 오른쪽에 있어요.'], ['just right of the group of 3', '3개 묶음 바로 오른쪽'], ['right', '오른쪽']],
};
const KQ_MC = [
  { k: 12, p: ['Tap middle C.', '가운데 도를 눌러 보세요.'], y: ['Yes, the C in the middle of the keyboard.', '맞아요. 건반 한가운데의 C예요.'] },
  { k: 24, p: ['Tap the next C to the right of middle C.', '가운데 도의 오른쪽 다음 C를 눌러 보세요.'], y: ['One pattern to the right of middle C.', '가운데 도에서 오른쪽으로 무늬 하나예요.'] },
  { k: 0, p: ['Tap the next C to the left of middle C.', '가운데 도의 왼쪽 다음 C를 눌러 보세요.'], y: ['One pattern to the left of middle C.', '가운데 도에서 왼쪽으로 무늬 하나예요.'] },
];
const kqLetterKeyNo = (k, L) => [(KQ_L[((k % 12) + 12) % 12] ? 'That is ' + KQ_L[((k % 12) + 12) % 12] + '. ' : 'That is a black key. ') + L + ' is ' + KQ_DOOR[L][2][0] + '.', (KQ_L[((k % 12) + 12) % 12] ? '그건 ' + KQ_L[((k % 12) + 12) % 12] + ' 건반이에요. ' : '그건 검은건반이에요. ') + L + ' 건반: ' + KQ_DOOR[L][2][1] + '.'];

// ── lesson 1: the black keys, then low and high. No letters on the keys yet; a tap anywhere in a group's column counts as that group.
const KQ_REG = (k) => [0, 1, 2, 3, 4].includes(((k % 12) + 12) % 12) ? 2 : 3;
{ const GR = { 2: { keys: [1, 3], style: 'seg3', col: KQ.CO, vx: kqVx(0, 4) }, 3: { keys: [6, 8, 10], style: 'seg4', col: KQ.BL, vx: kqVx(5, 11) } };
  const blacks = (n, o = 2) => { const m = {}; for (let i = 0; i < o; i++) (n === 2 ? [1, 3] : n === 3 ? [6, 8, 10] : [1, 3, 6, 8, 10]).forEach(k => { m[i * 12 + k] = n === 2 ? 'seg3' : n === 3 ? 'seg4' : (KQ_BK2.includes(k) ? 'seg3' : 'seg4'); }); return m; };
  const zoom = (n, c) => { const g = GR[n], lit = Math.min(c.tk, n), m = {}; g.keys.slice(0, lit).forEach(k => { m[k] = g.style; });
    return { top: kqNumRow(g.vx, g.keys.slice(0, lit).map((k, i) => ({ x: kqX(k), t: String(i + 1), col: g.col }))), kb: { bare: true, oct: 1, vx: g.vx, mw: 300, marks: m } }; };
  const reg = (want) => ({ kind: 'key', retry: true, prompt: ['Tap any key in a group of ' + want + ' black keys.', '검은건반이 ' + want + '개 모인 곳의 건반을 아무거나 눌러 보세요.'],
    fig: (c) => ({ kb: { bare: true, oct: 2, base: 0, marks: c.res === 'ok' ? blacks(want) : {} } }), ok: (k) => KQ_REG(k) === want,
    yes: want === 2 ? ['Two, side by side.', '두 개가 나란히 있네요.'] : ['Three, in a row.', '세 개가 줄지어 있네요.'],
    no: (k) => ['That key is in a group of ' + (5 - want) + '. Look for a group of ' + want + '.', '그 건반은 ' + (5 - want) + '개 묶음에 있어요. ' + want + '개 묶음을 찾아 보세요.'] });
  const hearQ = (n) => { const gap = [30, 20, 12, 7, 4, 2][Math.min(n, 5)], lo = kqRnd(48 - gap), hi = lo + gap, firstHigh = Math.random() < 0.5, a = firstHigh ? hi : lo, b = firstHigh ? lo : hi;
    return { kind: 'choice', prompt: ['Listen to two sounds. Which one is higher?', '소리 두 개를 들어 보세요. 어느 쪽이 더 높을까요?'], opts: [{ id: '1', label: () => t('The first', '처음 소리') }, { id: '2', label: () => t('The second', '나중 소리') }], ans: firstHigh ? '1' : '2', ok: (v) => v === (firstHigh ? '1' : '2'),
      play: () => { playKey(a - 24, 0.8); setTimeout(() => playKey(b - 24, 0.8), 900); },
      fig: (c) => ({ top: kqArrow(c.res ? hi : null, 48), kb: { bare: true, oct: 4, base: -24, marks: c.res ? { [lo]: 'seg3', [hi]: 'pick' } : {} } }),
      yes: ['The higher sound came from the key further right.', '높은 소리는 더 오른쪽 건반에서 났어요.'], no: ['The other one was higher. Its key is further right.', '다른 쪽이 더 높았어요. 그 건반이 더 오른쪽에 있어요.'] }; };
  const multiB = (n) => { const ks = (n === 2 ? [1, 3] : [6, 8, 10]), targets = [0, 1].flatMap(o => ks.map(k => o * 12 + k));
    return { kind: 'multi', retry: true, targets, prompt: ['Tap every black key that sits in a group of ' + n + '.', '검은건반이 ' + n + '개씩 모인 곳의 건반을 모두 눌러 보세요.'], prog: (a, b) => ['Found ' + a + ' of ' + b + '. Keep going.', b + '개 중 ' + a + '개를 찾았어요. 계속해요.'],
      fig: () => ({ kb: { bare: true, oct: 2, base: 0 } }), yes: ['All ' + targets.length + ' found: ' + (n === 2 ? 'two' : 'three') + ' in every group.', '모두 ' + targets.length + '개 찾았어요. 묶음마다 ' + n + '개씩이에요.'],
      no: (k) => [[1, 3, 6, 8, 10].includes(((k % 12) + 12) % 12) ? 'That key is in a group of ' + (5 - n) + '. Look for the groups of ' + n + '.' : 'Only the black keys count here. Look for the groups of ' + n + '.', [1, 3, 6, 8, 10].includes(((k % 12) + 12) % 12) ? '그 건반은 ' + (5 - n) + '개 묶음에 있어요. ' + n + '개 묶음을 찾아 보세요.' : '여기서는 검은건반만 골라요. ' + n + '개 묶음을 찾아 보세요.'] }; };
  KQ_SPEC['kq-black'] = {
    title: ['Black keys', '검은건반'], allLine: ['They come in groups of 2 and 3, always in the same order. Tap to listen.', '2개와 3개씩 모여 있고, 순서는 늘 같아요. 눌러 들어 보세요.'],
    fig: (c) => ({ top: <KqGroupsTop lit={c.last && typeof c.last === 'object' ? c.last : null} onTap={(it) => { it.keys.forEach((k, j) => setTimeout(() => playKey(k, 0.3), j * 220)); c.setLast({ g: it.id }); }}/>, kb: { bare: true, oct: 2, base: 0, marks: blacks(0) } }),
    steps: [
      { title: ['Two', '둘'], line: ['Two black keys stand side by side. Count them.', '검은건반 두 개가 나란히 서 있어요. 세어 보세요.'], fig: (c) => zoom(2, c) },
      { title: ['Three', '셋'], line: ['Then comes a row of three.', '그다음에는 세 개가 줄지어 있어요.'], fig: (c) => zoom(3, c) },
      { title: ['Two, three, two, three', '둘, 셋, 둘, 셋'], line: ['The groups take turns from left to right, and the order never changes.', '묶음은 왼쪽에서 오른쪽으로 번갈아 나오고, 순서는 바뀌지 않아요.'], fig: (c) => { const u = Math.min(c.tk, 4), m = {}; for (let i = 0; i < u; i++) Object.assign(m, kqPaint({}, (i % 2 === 0 ? [1, 3] : [6, 8, 10]).map(k => Math.floor(i / 2) * 12 + k), i % 2 === 0 ? 'seg3' : 'seg4')); return { top: <KqGroupsTop upto={u}/>, kb: { bare: true, oct: 2, base: 0, marks: m } }; } },
      { title: ['Low and high', '낮은 소리, 높은 소리'], line: ['Tap along the keys. Left sounds low and right sounds high.', '건반을 눌러 보세요. 왼쪽은 낮은 소리, 오른쪽은 높은 소리예요.'], fig: (c) => ({ top: kqArrow(typeof c.last === 'number' ? c.last : null, 36), kb: { bare: true, oct: 3, base: -12, marks: typeof c.last === 'number' ? { [c.last]: 'pick' } : {} } }) },
    ],
    make: (n) => { const cntQ = () => { const g = kqPick([2, 3]), ks = g === 2 ? [1, 3] : [6, 8, 10], m = {}; ks.forEach(k => { m[k] = g === 2 ? 'seg3' : 'seg4'; }); return { kind: 'choice', cols: 2, prompt: ['How many black keys are in the marked group?', '표시된 묶음에 검은건반이 몇 개 있을까요?'], opts: [{ id: '2', label: '2' }, { id: '3', label: '3' }], ans: String(g), ok: (v) => v === String(g), fig: () => ({ kb: { bare: true, oct: 1, base: 0, marks: m, mw: 380 } }), yes: ['Yes, ' + g + '.', '맞아요. ' + g + '개예요.'], no: ['Count the marked black keys: ' + g + '.', '표시된 검은건반을 세어 보세요. ' + g + '개예요.'] }; };
      const hl = (hi) => { const m0 = 8 + kqRnd(20); return { kind: 'key', retry: true, prompt: hi ? ['Tap any key that sounds higher than the marked key.', '표시된 건반보다 높게 들리는 건반을 아무거나 눌러 보세요.'] : ['Tap any key that sounds lower than the marked key.', '표시된 건반보다 낮게 들리는 건반을 아무거나 눌러 보세요.'], play: () => playKey(m0, 0.7), fig: () => ({ kb: { bare: true, oct: 3, base: 0, marks: { [m0]: 'pick' } } }), ok: (k) => hi ? k > m0 : k < m0,
        yes: hi ? ['Further right: higher.', '더 오른쪽이니 더 높아요.'] : ['Further left: lower.', '더 왼쪽이니 더 낮아요.'], no: (k) => k === m0 ? ['That is the marked key itself. Pick another.', '그건 표시된 건반이에요. 다른 건반을 눌러 보세요.'] : hi ? ['That key is to the left, so it sounds lower. Higher is to the right.', '그 건반은 왼쪽이라 더 낮아요. 높은 건 오른쪽이에요.'] : ['That key is to the right, so it sounds higher. Lower is to the left.', '그 건반은 오른쪽이라 더 높아요. 낮은 건 왼쪽이에요.'] }; };
      return [() => reg(2), () => reg(3), () => multiB(3), () => hearQ(n), cntQ, () => reg(3), () => multiB(2), () => hl(true), () => hearQ(n), cntQ, () => hl(false)][n % 11](); },
  }; }

// ── lesson 2: naming the white keys, one at a time, by where each sits next to the black-key groups; then four ways to try
const KQ_HZ = { small: { Ls: KQ_SMALL, ks: [0, 4], style: 'seg3', pk: 'pick', col: KQ.COD, name: ['The group of 2', '2개 묶음'] }, big: { Ls: KQ_BIG, ks: [5, 11], style: 'seg4', pk: 'pickB', col: KQ.BL, name: ['The group of 3', '3개 묶음'] } };
{ const hz = (kind, shown, cur, paint = true, word = false) => { const h = KQ_HZ[kind], small = kind === 'small', vx = kqVx(h.ks[0], h.ks[1]), m = paint ? kqPaint({}, kqHouseKeys(1, small).filter(k => KQ_L[k % 12]), h.style) : {}, nm = kqNames(1, shown);
    if (cur) { m[KQ_PC[cur]] = h.pk; nm.ncol[KQ_PC[cur]] = '#fff'; }
    return { top: <>{<KqRoofs oct={1} show={kind} vx={vx} k={kind}/>}{word && cur ? kqNumRow(vx, [{ x: kqX(KQ_PC[cur]), t: kqT(KQ_DOOR[cur][3]), col: h.col }], 17) : null}</>, kb: { bare: true, oct: 1, vx, mw: 290, marks: m, names: nm.names, ncol: nm.ncol } }; };
  const both = (cur, upto = 4) => { const ids = [0, 1, 2, 3].filter(x => x < upto), m = {}, names = {}, ncol = {};
    ids.forEach(id => { const o = Math.floor(id / 2), small = id % 2 === 0; kqPaint(m, kqHouseKeys(o + 1, small, o), small ? 'seg3' : 'seg4'); (small ? KQ_SMALL : KQ_BIG).forEach(L => { names[o * 12 + KQ_PC[L]] = L; ncol[o * 12 + KQ_PC[L]] = kqHouseCol(L); }); });
    if (cur != null && m[cur]) m[cur] = KQ_SMALL.includes(KQ_L[cur % 12] || (KQ_BK2.includes(cur % 12) ? 'C' : 'F')) ? 'pick' : 'pickB';
    return { top: <KqRoofs oct={2} only={ids}/>, kb: { oct: 2, base: 0, marks: m, names, ncol, plain: true } }; };
  const one = (L, i) => { const kind = KQ_SMALL.includes(L) ? 'small' : 'big', Ls = KQ_HZ[kind].Ls; return { title: KQ_DOOR[L][0], line: KQ_DOOR[L][1], fig: () => hz(kind, Ls.slice(0, i + 1), L, true, false) }; };
  const tryKb = (marks) => ({ top: <KqRoofs oct={2}/>, kb: { bare: true, oct: 2, base: 0, marks } });
  const houseM = (() => { const m = {}; kqHouseKeys(2, true).forEach(k => { m[k] = 'seg3'; }); kqHouseKeys(2, false).forEach(k => { m[k] = 'seg4'; }); return m; })();
  const pcOf = (L) => KQ_PC[L];
  KQ_SPEC['kq-houses'] = {
    title: ['Naming the white keys', '흰건반 이름 붙이기'], allLine: ['Each white key is named by where it sits next to the black-key groups.', '흰건반은 검은건반 묶음 옆 어디에 있는지로 이름을 붙여요.'],
    fig: (c) => both(typeof c.last === 'number' ? c.last : null, c.tk),
    steps: [
      { title: KQ_HZ.small.name, line: ['Three white keys go with it: one on the left, one between, one on the right.', '흰건반 세 개가 딸려 있어요. 왼쪽, 사이, 오른쪽에 하나씩이에요.'], fig: (c) => hz('small', [], null, c.tk >= 1) },
      one('C', 0), one('D', 1), one('E', 2),
      { title: KQ_HZ.big.name, line: ['Four white keys go with it: one on the left, two between, one on the right.', '흰건반 네 개가 딸려 있어요. 왼쪽에 하나, 사이에 둘, 오른쪽에 하나예요.'], fig: (c) => hz('big', [], null, c.tk >= 1) },
      one('F', 0), one('G', 1), one('A', 2), one('B', 3),
      { title: ['The pattern repeats', '무늬는 되풀이돼요'], line: ['Group of 2, group of 3, again and again, with the same seven letters. Tap the keys to hear them.', '2개 묶음, 3개 묶음이 되풀이되고 같은 일곱 글자가 돌아와요. 건반을 눌러 들어 보세요.'], fig: (c) => both(typeof c.last === 'number' ? c.last : null, c.tk) },
    ],
    make: (n, prev) => { let L; do { L = kqPick(KQ_ABC); } while (prev && prev.L === L);
      const kind = n % 8, D = KQ_DOOR[L];
      if (kind === 4) { const small = KQ_SMALL.includes(L), mk = { ...houseM }; mk[pcOf(L)] = small ? 'pick' : 'pickB';
        return { L, kind: 'choice', cols: 2, prompt: ['This white key sits by which group of black keys?', '이 흰건반은 어느 검은건반 묶음 옆에 있을까요?'], opts: [{ id: '2', label: () => t('The group of 2', '2개 묶음') }, { id: '3', label: () => t('The group of 3', '3개 묶음') }], ans: small ? '2' : '3', ok: (v) => v === (small ? '2' : '3'), fig: () => tryKb(mk),
          yes: ['Yes: ' + L + ' belongs to the group of ' + (small ? '2' : '3') + '.', '맞아요. ' + L + '은(는) ' + (small ? '2' : '3') + '개 묶음에 속해요.'], no: ['It is ' + L + ', which belongs to the group of ' + (small ? '2' : '3') + '.', kqYe(L) + '. ' + (small ? '2' : '3') + '개 묶음에 속해요.'] }; }
      if (kind === 5) return { L, kind: 'choice', cols: 4, prompt: ['Which letter is the white key ' + D[2][0] + '?', D[2][1] + '인 흰건반은 어떤 글자일까요?'], opts: kqLet7(), ans: L, ok: (v) => v === L, fig: () => tryKb(houseM),
        yes: ['Yes: ' + L + '.', '맞아요. ' + kqYe(L) + '.'], no: ['That is ' + L + '. Look at where it sits among the black keys.', L + '이에요. 검은건반 사이에서 어디에 있는지 보세요.'] };
      if (kind === 6) return { L, kind: 'key', retry: true, prompt: ['Tap ' + L + ' in the higher pattern, the one on the right.', '오른쪽의 더 높은 무늬에서 ' + L + ' 건반을 눌러 보세요.'], fig: () => tryKb(houseM), ok: (k) => k === pcOf(L) + 12,
        yes: ['Yes: the same letter, one pattern higher.', '맞아요. 같은 글자, 한 무늬 위예요.'], no: (k) => k % 12 === pcOf(L) ? ['Right letter, but the lower pattern. Take the one on the right.', '글자는 맞지만 낮은 무늬예요. 오른쪽 것을 눌러 보세요.'] : kqLetterKeyNo(k, L) };
      if (kind === 7) { let L2; do { L2 = kqPick(KQ_ABC); } while (L2 === L); const targets = [pcOf(L), pcOf(L) + 12, pcOf(L2), pcOf(L2) + 12];
        return { L, kind: 'multi', retry: true, targets, prompt: ['Tap every ' + L + ' and every ' + L2 + '.', L + ' 건반과 ' + L2 + ' 건반을 모두 눌러 보세요.'], prog: (a, b) => ['Found ' + a + ' of ' + b + '. Keep going.', b + '개 중 ' + a + '개를 찾았어요. 계속해요.'], fig: () => tryKb(houseM),
          yes: ['All four found: each letter once in each pattern.', '네 개 모두 찾았어요. 글자마다 무늬마다 하나씩이에요.'], no: (k) => [(KQ_L[((k % 12) + 12) % 12] ? 'That is ' + KQ_L[((k % 12) + 12) % 12] + '. ' : 'That is a black key. ') + 'Look for ' + L + ' and ' + L2 + '.', (KQ_L[((k % 12) + 12) % 12] ? '그건 ' + KQ_L[((k % 12) + 12) % 12] + ' 건반이에요. ' : '그건 검은건반이에요. ') + L + '과(와) ' + L2 + ' 건반을 찾아 보세요.'] }; }
      if (kind === 3) { const targets = [pcOf(L), pcOf(L) + 12]; return { L, kind: 'multi', retry: true, targets, prompt: ['Tap every white key that is ' + D[2][0] + '.', D[2][1] + '인 흰건반을 모두 눌러 보세요.'], prog: (a, b) => ['Found ' + a + ' of ' + b + '. One more.', b + '개 중 ' + a + '개를 찾았어요. 하나 더요.'], fig: () => tryKb(houseM), yes: ['Both found: that is the letter ' + L + ', once in each pattern.', '두 개 모두 찾았어요. 글자 ' + kqYe(L) + '. 무늬마다 하나씩 있어요.'], no: (k) => kqLetterKeyNo(k, L) }; }
      if (kind === 0) return { L, kind: 'key', retry: true, prompt: ['Tap ' + L + '.', L + ' 건반을 눌러 보세요.'], fig: () => tryKb(houseM), ok: (k) => k % 12 === pcOf(L),
        yes: ['Yes, ' + L + ' is ' + D[2][0] + '.', '맞아요. ' + L + ' 건반: ' + D[2][1] + '.'], no: (k) => kqLetterKeyNo(k, L) };
      if (kind === 1) { const small = KQ_SMALL.includes(L), Ls = small ? KQ_SMALL : KQ_BIG, mk = { ...houseM }; mk[pcOf(L) + 12] = small ? 'pick' : 'pickB';
        return { L, kind: 'choice', cols: Ls.length > 3 ? 4 : 3, prompt: ['Which letter is the marked key?', '표시된 건반은 어떤 글자일까요?'], opts: Ls.map(x => ({ id: x, label: x })), ans: L, ok: (v) => v === L, fig: () => tryKb(mk),
          yes: ['Yes: ' + L + ', ' + D[2][0] + '.', '맞아요. ' + L + ' 건반: ' + D[2][1] + '.'], no: ['That key is ' + L + ': ' + D[2][0] + '.', '이 건반은 ' + L + ' 건반이에요: ' + D[2][1] + '.'] }; }
      return { L, kind: 'key', retry: true, prompt: ['Tap the white key that is ' + D[2][0] + '.', D[2][1] + '인 흰건반을 눌러 보세요.'], fig: () => tryKb(houseM), ok: (k) => k % 12 === pcOf(L),
        yes: ['Yes, that is ' + L + '.', '맞아요. ' + L + ' 건반이에요.'], no: (k) => kqLetterKeyNo(k, L) }; },
  }; }

// ── lesson 3: the same name in every pattern, middle C, twelve keys and seven names, and round again
{ const O = 2, N = O * 12, base = -12;
  const same = (Ls, cur) => { const m = {}; const nm = kqNames(O, Ls); Ls.forEach(L => { for (let o = 0; o <= O; o++) { const k = o * 12 + KQ_PC[L]; if (k <= N) { m[k] = KQ_SMALL.includes(L) ? 'seg3' : 'seg4'; if (k % 12 === 0 && o === O) { nm.names[k] = L; nm.ncol[k] = kqHouseCol(L); } } } }); if (cur != null) m[cur] = KQ_SMALL.includes(KQ_L[cur % 12]) ? 'pick' : 'pickB'; return { oct: O, base, marks: m, names: nm.names, ncol: nm.ncol, plain: true }; };
  const allNames = (cur) => same(['C', 'D', 'E', 'F', 'G', 'A', 'B'], cur);
  const twelve = (c) => { const n = Math.min(c.tk, 12), m = {}; for (let k = 0; k < n; k++) m[k] = 'seg3'; const nm = c.tk >= 14 ? kqNames(1, ['C', 'D', 'E', 'F', 'G', 'A', 'B']) : { names: {}, ncol: {} }; if (c.tk >= 14) m[12] = 'pick';
    const cnt = c.tk < 14; if (cnt && n > 0) m[n - 1] = 'pick';
    return { top: kqNumRow(kqVx(0, 12), Array.from({ length: Math.min(n, 12) }, (_, k) => ({ x: kqX(k), t: String(k + 1), col: cnt && k === n - 1 ? KQ.COD : KQ.NV, ln: cnt, lw: cnt && k === n - 1 ? 2.6 : 1.2, lo: cnt && k === n - 1 ? 1 : 0.45 })), 15, c.tk >= 14 ? 0 : 46), kb: { oct: 1, base: 0, marks: m, names: nm.names, ncol: nm.ncol, plain: true } }; };
  const multi = (L) => { const pc = KQ_PC[L], targets = []; for (let o = 0; o <= O; o++) if (o * 12 + pc <= N) targets.push(o * 12 + pc);
    return { L, kind: 'multi', retry: true, targets, prompt: ['Tap every ' + L + ' on the keyboard.', L + ' 건반을 모두 눌러 보세요.'], prog: (a, b) => ['Found ' + a + ' of ' + b + '. Keep going.', b + '개 중 ' + a + '개를 찾았어요. 계속해요.'],
      fig: () => ({ kb: { bare: true, oct: O, base } }), yes: ['All ' + targets.length + ' found: every pattern has one.', '모두 ' + targets.length + '개 찾았어요. 무늬마다 하나씩 있어요.'], no: (k) => kqLetterKeyNo(k, L) }; };
  const nextL = (prev, first) => { if (first) return 'C'; let L; do { L = kqPick(KQ_ABC); } while (prev && prev.L === L); return L; };
  KQ_SPEC['kq-names'] = {
    title: ['Every key has its place', '모든 건반에는 제 자리가 있어요'], allLine: ['The seven names go round and round, so every pattern has the same letters. Tap a key to hear it.', '이름 일곱 개가 돌고 돌아서, 무늬마다 같은 글자가 있어요. 건반을 눌러 들어 보세요.'],
    fig: (c) => ({ kb: c.tk >= 1 || typeof c.last === 'number' ? allNames(typeof c.last === 'number' ? c.last : null) : { oct: O, base } }),
    steps: [
      { title: ['Every C', '모든 C'], line: ['Each C sits just left of a group of 2, so every C has the same spot.', 'C는 2개 묶음 바로 왼쪽마다 있어서, 모든 C가 같은 자리에 있어요.'], fig: () => ({ kb: same(['C']) }) },
      { title: ['One letter at a time', '글자 하나씩'], line: ['Watch: each letter lights up in every pattern, always in its own spot.', '보세요. 글자마다 모든 무늬에서 늘 제 자리에 켜져요.'], fig: (c) => ({ kb: c.tk < 1 ? { oct: O, base } : same(['DEFGAB'[Math.min(Math.floor((c.tk - 1) / 2), 5)]]) }) },
      { title: ['Middle C', '가운데 도'], line: ['One C has a name of its own: the C in the middle of the keyboard.', 'C 하나는 이름이 따로 있어요. 건반 한가운데 있는 C예요.'], fig: () => ({ kb: { ...same(['C'], 12) } }) },
      { title: ['Twelve keys, seven names', '건반 열두 개, 이름 일곱 개'], line: ['A group of 2 and a group of 3 make one pattern. Count its 12 keys, black ones too: only the white keys have letters.', '2개 묶음과 3개 묶음이 무늬 하나예요. 건반 12개를 검은건반까지 세어 보세요. 글자가 있는 건 흰건반뿐이에요.'], fig: (c) => twelve(c) },
      { title: ['Round again', '다시 처음으로'], line: ['After B the next group of 2 begins, and C comes round again. From one C to the next C is called an octave.', 'B 다음에는 다음 2개 묶음이 시작되고, C가 다시 나와요. 한 C에서 다음 C까지를 한 옥타브라고 불러요.'], fig: () => ({ kb: { oct: 2, base: 0, marks: { 11: 'seg4', 12: 'pick' }, names: { 11: 'B', 12: 'C' }, ncol: { 11: KQ.BL, 12: KQ.COD }, plain: true, ks: [5, 16] } }) },
    ],
    make: (n, prev) => { const WH = [0, 2, 4, 5, 7, 9, 11, 12], mcI = Math.floor(n / 8) % 3,
      mid = () => ({ L: null, kind: 'key', retry: true, prompt: KQ_MC[mcI].p, fig: () => ({ kb: { bare: true, oct: O, base } }), ok: (k) => k === KQ_MC[mcI].k, yes: KQ_MC[mcI].y,
        no: (k) => k % 12 === 0 ? ['That is a C, but not the one asked for. Middle C is the C in the middle of this keyboard.', '그건 C지만 찾는 C가 아니에요. 가운데 도는 이 건반 한가운데의 C예요.'] : ['That is not a C. A C sits just left of a group of 2 black keys.', '그건 C가 아니에요. C는 검은건반 2개 묶음 바로 왼쪽에 있어요.'] }),
      nbr = (dir) => { const Ls = dir > 0 ? KQ_ABC.filter(x => x !== 'A' || true) : 'DEFGAB'.split(''); const L = kqPick(dir > 0 ? 'CDEFGAB'.split('') : Ls), i0 = 'CDEFGAB'.indexOf(L), A = 'CDEFGAB'[(i0 + dir + 7) % 7], k0 = WH[i0], k1 = dir > 0 ? WH[i0 + 1] : WH[i0 - 1];
        return { L: null, kind: 'choice', cols: 4, prompt: dir > 0 ? ['Which name comes after ' + L + '?', L + ' 다음에 오는 이름은?'] : ['Which name comes before ' + L + '?', L + ' 앞에 오는 이름은?'], opts: kqLet7(), ans: A, ok: (v) => v === A,
          fig: (c) => ({ kb: { bare: true, oct: 1, base: 0, marks: c.res ? { [k0]: 'seg3', [k1]: 'pass' } : { [k0]: 'pick' } } }),
          yes: dir > 0 ? [A + ': the next white key to the right' + (L === 'B' ? ', where the next pattern begins.' : '.'), A + '예요. 바로 오른쪽 흰건반' + (L === 'B' ? '이고 다음 무늬가 시작돼요.' : '이에요.')] : [A + ': the next white key to the left.', A + '예요. 바로 왼쪽 흰건반이에요.'],
          no: dir > 0 ? ['After ' + L + ' comes ' + A + ', the next white key to the right.', L + ' 다음은 ' + A + ', 바로 오른쪽 흰건반이에요.'] : ['Before ' + L + ' comes ' + A + ', the next white key to the left.', L + ' 앞은 ' + A + ', 바로 왼쪽 흰건반이에요.'] }; },
      cnt = (w) => w === 0 ? { L: null, kind: 'choice', cols: 4, prompt: ['How many keys make one pattern, black ones too?', '무늬 하나는 검은건반까지 건반 몇 개일까요?'], opts: ['5', '7', '12', '24'].map(x => ({ id: x, label: x })), ans: '12', ok: (v) => v === '12', fig: () => ({ kb: { bare: true, oct: 1, base: 0 } }), yes: ['12 keys: 7 white and 5 black.', '12개예요. 흰건반 7개, 검은건반 5개예요.'], no: ['One pattern has 12 keys: 7 white and 5 black.', '무늬 하나는 12개예요. 흰건반 7개, 검은건반 5개예요.'] }
        : { L: null, kind: 'choice', cols: 4, prompt: ['How many different letter names are there?', '글자 이름은 모두 몇 가지일까요?'], opts: ['5', '7', '8', '12'].map(x => ({ id: x, label: x })), ans: '7', ok: (v) => v === '7', fig: () => ({ kb: { bare: true, oct: 1, base: 0 } }), yes: ['Seven: A B C D E F G.', '일곱 가지예요: A B C D E F G.'], no: ['Seven: A B C D E F G, then they start over.', '일곱 가지예요: A B C D E F G, 그다음엔 처음부터 다시예요.'] };
      return [() => multi(nextL(prev, n === 0)), mid, () => nbr(1), () => multi(nextL(prev)), () => cnt(0), mid, () => nbr(-1), () => cnt(1)][n % 8](); },
  }; }

// ══ 2. The staff and clefs ══
const kqLinePos = (p) => p % 2 === 0 ? ['line', p / 2 + 1] : ['space', (p - 1) / 2 + 1];
const kqLS = (ty) => ty === 'line' ? ['line', '줄'] : ['space', '칸'];
KQ_SPEC['kq-lines'] = {
  title: ['Lines and spaces', '줄과 칸'], allLine: ['Notes sit on the five lines and in the four spaces between them.', '음표는 다섯 줄 위에도, 그 사이 네 칸에도 앉아요.'],
  fig: () => ({ staff: <KqLines labels/> }),
  steps: [
    { title: ['Five lines', '줄 다섯'], line: ['Count from the bottom: the lowest line is line 1.', '아래에서부터 세요. 가장 아래 줄이 1번이에요.'], fig: (c) => ({ staff: <KqLines labels hl={{ type: 'line', n: Math.min(c.tk + 1, 5) }}/> }) },
    { title: ['Four spaces', '칸 넷'], line: ['Spaces are counted from the bottom too: the lowest space is space 1.', '칸도 아래에서부터 세요. 가장 아래 칸이 1번이에요.'], fig: (c) => ({ staff: <KqLines labels hl={{ type: 'space', n: Math.min(c.tk + 1, 4) }}/> }) },
    { title: ['Taking turns', '번갈아'], line: ['Lines and spaces alternate, so the staff has nine places for notes.', '줄과 칸이 번갈아 나와서, 오선에는 음표가 앉을 자리가 아홉 군데예요.'], fig: (c) => { const [ty, n] = kqLinePos(Math.min(c.tk, 8)); return { staff: <KqLines labels hl={{ type: ty, n }}/> }; } },
  ],
  make: (n) => { const k = n % 4;
    if (k % 2 === 0) { const type = k === 0 ? 'line' : 'space', max = type === 'line' ? 5 : 4, num = 1 + kqRnd(max), w = kqLS(type);
      return { kind: 'tap', retry: true, prompt: ['Tap the ' + kqOrd(num) + ' ' + w[0] + ', counting from the bottom.', '아래에서부터 세어 ' + kqOrd(num) + ' ' + w[1] + '을 눌러 보세요.'], fig: (c) => ({ staff: <KqLines onTap={c.pick} pickd={c.pickd} ok={c.res === 'ok'}/> }), ok: (v) => v.type === type && v.n === num,
        yes: ['Yes, ' + w[0] + ' ' + num + '.', '맞아요. ' + num + '번 ' + w[1] + '이에요.'], no: (v) => ['That is ' + kqLS(v.type)[0] + ' ' + v.n + '. Start again from the bottom.', '그건 ' + v.n + '번 ' + kqLS(v.type)[1] + '이에요. 다시 아래에서부터 세어 보세요.'] }; }
    const p = kqRnd(9), [ty, num] = kqLinePos(p), d = 30 + p, w = kqLS(ty);
    return { kind: 'choice', cols: 2, prompt: ['Does this note sit on a line or in a space?', '이 음표는 줄 위에 있을까요, 칸 안에 있을까요?'], opts: [{ id: 'line', label: () => t('On a line', '줄 위') }, { id: 'space', label: () => t('In a space', '칸 안') }], ans: ty, ok: (v) => v === ty,
      fig: () => ({ staff: kqStaff([d], 'treble') }), yes: ['Yes: ' + w[0] + ' ' + num + '.', '맞아요. ' + num + '번 ' + w[1] + '이에요.'], no: ['It is ' + w[0] + ' ' + num + '. A line runs through a note on a line, and a note in a space has lines above and below it.', num + '번 ' + w[1] + '이에요. 줄 위의 음표는 줄이 가운데를 지나고, 칸 안의 음표는 위아래에 줄이 있어요.'] }; },
};
// staff and keyboard side by side: one step on the staff is the next white key
const kqClimb = (ds, marks) => ({ staff: kqStaff(ds, 'treble'), kb: { oct: 2, ks: [0, 12], base: 0, plain: true, marks } });
const kqWhiteMarks = (ds, last) => { const m = {}; ds.forEach((d, i) => { m[dMidiKey(d)] = i === ds.length - 1 && last ? 'pick' : 'seg3'; }); return m; };
KQ_SPEC['kq-climb'] = {
  title: ['Higher and lower', '높은 음, 낮은 음'], allLine: ['A note higher on the staff is a key further right on the keyboard, and it sounds higher.', '오선에서 더 위에 있는 음표는 건반에서 더 오른쪽이고, 더 높게 들려요.'],
  fig: () => kqClimb([28, 29, 30, 31, 32, 33, 34, 35], kqWhiteMarks([28, 29, 30, 31, 32, 33, 34, 35])),
  steps: [
    { title: ['One step up', '한 걸음 위로'], line: ['Each step up the staff, from a line to a space or a space to a line, is the next white key to the right.', '오선에서 줄에서 칸으로, 칸에서 줄로 한 걸음 오르면 흰건반은 바로 오른쪽이에요.'], fig: (c) => { const ds = [28, 29, 30, 31, 32, 33, 34, 35].slice(0, Math.min(c.tk + 1, 8)); return kqClimb(ds, kqWhiteMarks(ds, true)); } },
    { title: ['One step down', '한 걸음 아래로'], line: ['Going down is the next white key to the left.', '내려가면 흰건반은 바로 왼쪽이에요.'], fig: (c) => { const ds = [35, 34, 33, 32, 31, 30, 29, 28].slice(0, Math.min(c.tk + 1, 8)); return kqClimb(ds, kqWhiteMarks(ds, true)); } },
    { title: ['Line to line', '줄에서 줄로'], line: ['From one line to the next line is two steps. One white key is skipped in between.', '줄에서 다음 줄까지는 두 걸음이에요. 그 사이 흰건반 하나를 건너뛰어요.'], fig: () => kqClimb([30, 32, 34], { ...kqWhiteMarks([30, 32, 34]), 5: 'pass', 9: 'pass' }) },
  ],
  make: (n) => { const k = n % 4;
    if (k % 2 === 0) { const hi = k === 0; let a = 29 + kqRnd(10), b; do { b = 29 + kqRnd(10); } while (b === a); const ans = (a > b) === hi ? '1' : '2';
      return { kind: 'choice', prompt: hi ? ['Which note is higher?', '어느 음표가 더 높을까요?'] : ['Which note is lower?', '어느 음표가 더 낮을까요?'], opts: [{ id: '1', label: () => t('The first', '처음 음표') }, { id: '2', label: () => t('The second', '나중 음표') }], ans, ok: (v) => v === ans, play: () => kqPlayDs([a, b]),
        fig: (c) => ({ staff: kqStaff([a, b], 'treble'), kb: c.res ? { oct: 3, ks: [0, 36], base: 0, plain: true, marks: { [dMidiKey(a)]: a > b ? 'pick' : 'seg3', [dMidiKey(b)]: b > a ? 'pick' : 'seg3' } } : null }),
        yes: ['Higher on the staff, further right on the keys.', '오선에서 더 위, 건반에서 더 오른쪽이에요.'], no: ['The ' + ((a > b) === hi ? 'first' : 'second') + ' note is ' + (hi ? 'higher: it sits higher on the staff.' : 'lower: it sits lower on the staff.'), (((a > b) === hi) ? '처음' : '나중') + ' 음표가 ' + (hi ? '더 높아요. 오선에서 더 위에 있어요.' : '더 낮아요. 오선에서 더 아래에 있어요.')] }; }
    const up = k === 1, d = up ? 28 + kqRnd(7) : 29 + kqRnd(7), tk = dMidiKey(d + (up ? 1 : -1));
    return { kind: 'key', retry: true, prompt: up ? ['The marked key is this note. Tap the key one step up.', '표시된 건반이 이 음표예요. 한 걸음 위의 건반을 눌러 보세요.'] : ['The marked key is this note. Tap the key one step down.', '표시된 건반이 이 음표예요. 한 걸음 아래의 건반을 눌러 보세요.'], play: () => playKey(dMidiKey(d), 0.6),
      fig: () => kqClimb([d], { [dMidiKey(d)]: 'pick' }), ok: (x) => x === tk,
      yes: up ? ['One step up is the next white key to the right.', '한 걸음 위는 바로 오른쪽 흰건반이에요.'] : ['One step down is the next white key to the left.', '한 걸음 아래는 바로 왼쪽 흰건반이에요.'],
      no: (x) => [x === dMidiKey(d) ? 'That is the note’s own key. Take the white key right next to it, on the ' + (up ? 'right.' : 'left.') : KQ_L[((x % 12) + 12) % 12] ? 'Take the white key right next to the marked key, on the ' + (up ? 'right.' : 'left.') : 'Staff steps land on white keys. Take the white key right next to the marked key, on the ' + (up ? 'right.' : 'left.'), x === dMidiKey(d) ? '그건 음표 자신의 건반이에요. 그 ' + (up ? '오른쪽' : '왼쪽') + ' 바로 옆 흰건반을 눌러 보세요.' : '표시된 건반의 ' + (up ? '오른쪽' : '왼쪽') + ' 바로 옆 흰건반을 눌러 보세요.'] }; },
};
const KQ_GRAND = () => ({ ...kqPaint(kqPaint({}, Array.from({ length: 12 }, (_, i) => i), 'seg4'), Array.from({ length: 12 }, (_, i) => 13 + i), 'seg3'), 12: 'pass' });
const KQ_GR = () => ({ ...KQ_GRAND(), 12: 'pick' });
const KQ_GRNM = { 5: 'F', 12: 'C', 19: 'G' }, KQ_GRCOL = { 5: KQ.BL, 12: KQ.COD, 19: KQ.COD };
const kqGrand = () => ({ staff: <>{kqStaff([28, 32], 'treble', { under: true })}{kqStaff([28, 24], 'bass', { under: true })}</>, kb: { oct: 2, ks: [0, 24], base: -12, plain: true, marks: KQ_GR(), names: KQ_GRNM, ncol: KQ_GRCOL } });
KQ_SPEC['kq-clefs'] = {
  title: ['Treble and bass clefs', '높은음자리표와 낮은음자리표'], allLine: ['A clef sign at the start of a staff says which notes that staff is for. The treble clef is the Queen, high; the bass clef is the King, low. Both are read from middle C.', '오선 맨 앞의 음자리표가 그 오선이 어느 음을 위한 것인지 알려 줘요. 높은음자리표는 여왕, 높은 음이고 낮은음자리표는 왕, 낮은 음이에요. 둘 다 가운데 도를 기준으로 읽어요.'],
  fig: () => kqGrand(),
  steps: [
    { title: ['The treble clef: the Queen', '높은음자리표: 여왕'], line: ['The Queen sings the high notes, usually with the right hand. Her curl circles line 2, G, to the right of middle C: that line is her house.', '여왕은 높은 음을 노래해요. 보통 오른손이 쳐요. 말린 부분이 2번 줄 G를 감싸요. 가운데 도의 오른쪽이고, 그 줄이 여왕의 집이에요.'],
      fig: () => ({ staff: kqStaff([32], 'treble', { ring: [0], under: true }), kb: { oct: 2, ks: [0, 24], base: -12, plain: true, marks: { 12: 'pass', 19: 'pick' }, names: { 12: 'C', 19: 'G' }, ncol: { 12: KQ.COD, 19: KQ.COD } } }) },
    { title: ['The bass clef: the King', '낮은음자리표: 왕'], line: ['The King sings the low notes, usually with the left hand. His two dots sit either side of line 4, F, to the left of middle C: that line is his house.', '왕은 낮은 음을 노래해요. 보통 왼손이 쳐요. 두 점이 4번 줄 F의 양쪽에 있어요. 가운데 도의 왼쪽이고, 그 줄이 왕의 집이에요.'],
      fig: () => ({ staff: kqStaff([24], 'bass', { ring: [0], under: true }), kb: { oct: 2, ks: [0, 24], base: -12, plain: true, marks: { 12: 'pass', 5: 'pickB' }, names: { 12: 'C', 5: 'F' }, ncol: { 12: KQ.COD, 5: KQ.BL } } }) },
    { title: ['Both together', '함께 쓰기'], line: ['Piano music stacks them. Middle C sits between the two staves: the treble staff reads to the right of it, the bass staff to the left.', '피아노 악보는 둘을 겹쳐 써요. 가운데 도는 두 오선 사이에 있어요. 높은음자리 오선은 그 오른쪽, 낮은음자리 오선은 그 왼쪽을 읽어요.'], fig: () => kqGrand() },
    { title: ['The G clef and the F clef', 'G 음자리표와 F 음자리표'], line: ['Long ago the treble clef was a written letter G and the bass clef a letter F. So they are also called the G clef and the F clef: they name the Queen’s and the King’s lines.', '아주 옛날 높은음자리표는 손으로 쓴 글자 G였고, 낮은음자리표는 글자 F였어요. 그래서 G 음자리표, F 음자리표라고도 불러요. 여왕의 줄과 왕의 줄 이름이에요.'], fig: () => kqGrand() },
  ],
  make: (n) => { const tr = Math.floor(n / 4) % 2 === 0, k = n % 4;
    if (k === 0) { const high = Math.random() < 0.5, key = high ? 13 + kqRnd(11) : 1 + kqRnd(10), ans = high ? 'T' : 'B';
      return { kind: 'choice', prompt: ['Listen. Which clef would usually show this key?', '들어 보세요. 이 건반은 보통 어느 음자리표로 쓸까요?'], opts: [{ id: 'T', label: () => t('Treble clef', '높은음자리표') }, { id: 'B', label: () => t('Bass clef', '낮은음자리표') }], ans, ok: (v) => v === ans, play: () => playKey(key - 12, 0.9),
        fig: (c) => ({ kb: { oct: 2, ks: [0, 24], base: -12, plain: true, marks: { [key]: c.res ? 'good' : 'pick' } } }), yes: high ? ['A key on the high side: the treble clef.', '높은 쪽의 건반이에요. 높은음자리표예요.'] : ['A key on the low side: the bass clef.', '낮은 쪽의 건반이에요. 낮은음자리표예요.'],
        no: high ? ['That key is further right, so it is high: the treble clef.', '그 건반은 오른쪽에 있어서 높아요. 높은음자리표예요.'] : ['That key is further left, so it is low: the bass clef.', '그 건반은 왼쪽에 있어서 낮아요. 낮은음자리표예요.'] }; }
    if (k === 1) return { kind: 'choice', cols: 3, prompt: tr ? ['Which line does the treble clef’s curl circle?', '높은음자리표의 말린 부분은 어느 줄을 감쌀까요?'] : ['Which line do the two dots of the bass clef surround?', '낮은음자리표의 두 점은 어느 줄 양쪽에 있을까요?'],
      opts: (tr ? [1, 2, 3] : [3, 4, 5]).map(x => ({ id: String(x), label: () => t('Line ' + x, x + '번 줄') })), ans: tr ? '2' : '4', ok: (v) => v === (tr ? '2' : '4'), fig: (c) => ({ staff: kqStaff(tr ? [32] : [24], tr ? 'treble' : 'bass', { ring: c.res ? [0] : [], under: !!c.res }) }),
      yes: tr ? ['Line 2 is G.', '2번 줄이 G예요.'] : ['Line 4 is F.', '4번 줄이 F예요.'], no: tr ? ['The curl circles line 2, which is G.', '말린 부분은 2번 줄을 감싸요. 그 줄이 G예요.'] : ['The dots sit either side of line 4, which is F.', '두 점은 4번 줄 양쪽에 있어요. 그 줄이 F예요.'] };
    if (k === 2) return { kind: 'choice', prompt: tr ? ['Which hand usually plays the treble staff?', '높은음자리 오선은 보통 어느 손이 칠까요?'] : ['Which hand usually plays the bass staff?', '낮은음자리 오선은 보통 어느 손이 칠까요?'], opts: [{ id: 'L', label: () => t('The left hand', '왼손') }, { id: 'R', label: () => t('The right hand', '오른손') }], ans: tr ? 'R' : 'L', ok: (v) => v === (tr ? 'R' : 'L'),
      fig: () => ({ staff: kqStaff(tr ? [32, 33, 34] : [23, 22, 21], tr ? 'treble' : 'bass') }), yes: tr ? ['Higher notes: usually the right hand.', '높은 음은 보통 오른손이에요.'] : ['Lower notes: usually the left hand.', '낮은 음은 보통 왼손이에요.'], no: tr ? ['The treble staff holds the higher notes, usually the right hand.', '높은음자리 오선은 높은 음이라 보통 오른손이에요.'] : ['The bass staff holds the lower notes, usually the left hand.', '낮은음자리 오선은 낮은 음이라 보통 왼손이에요.'] };
    return { kind: 'choice', cols: 4, prompt: tr ? ['The treble clef circles line 2. Which letter is that line?', '높은음자리표가 감싸는 2번 줄은 어느 글자일까요?'] : ['The bass clef surrounds line 4. Which letter is that line?', '낮은음자리표가 둘러싸는 4번 줄은 어느 글자일까요?'], opts: kqLet7(), ans: tr ? 'G' : 'F', ok: (v) => v === (tr ? 'G' : 'F'), fig: () => ({ staff: kqStaff(tr ? [32] : [24], tr ? 'treble' : 'bass', { ring: [0] }) }),
      yes: tr ? ['Line 2 of the treble staff is G.', '높은음자리 오선의 2번 줄은 G예요.'] : ['Line 4 of the bass staff is F.', '낮은음자리 오선의 4번 줄은 F예요.'], no: tr ? ['It is G: the treble clef curls round line 2.', 'G예요. 높은음자리표는 2번 줄을 감싸요.'] : ['It is F: the bass clef’s dots sit either side of line 4.', 'F예요. 낮은음자리표의 두 점은 4번 줄 양쪽에 있어요.'] }; },
};

// ══ 3. Notes on the staff ══
const KQ_ST = { treble: { lines: [30, 32, 34, 36, 38], spaces: [31, 33, 35, 37], hint: ['Count up from line 1 = E, one letter per place.', '1번 줄 E에서 한 자리에 한 글자씩 올라가며 세어 보세요.'] },
  bass: { lines: [18, 20, 22, 24, 26], spaces: [19, 21, 23, 25], hint: ['Count up from line 1 = G, one letter per place.', '1번 줄 G에서 한 자리에 한 글자씩 올라가며 세어 보세요.'] } };
const kqNameQ = (clef) => { const S = KQ_ST[clef], d = kqPick(S.lines.concat(S.spaces)), L = kqLetter(d), isLine = S.lines.includes(d), num = (isLine ? S.lines : S.spaces).indexOf(d) + 1, w = kqLS(isLine ? 'line' : 'space');
  return { kind: 'choice', cols: 4, prompt: ['Name this note.', '이 음표의 이름을 말해요.'], opts: kqLet7(), ans: L, ok: (v) => v === L, fig: (c) => ({ staff: kqStaff([d], clef, { ring: [0], under: c.res ? true : null }) }),
    yes: [L + ', on ' + w[0] + ' ' + num + '.', L + '예요. ' + num + '번 ' + w[1] + '에 있어요.'], no: [L + ', on ' + w[0] + ' ' + num + '. ' + S.hint[0], L + '예요. ' + num + '번 ' + w[1] + '이에요. ' + S.hint[1]] }; };
KQ_SPEC['kq-letters'] = {
  title: ['Letters up the staff', '오선을 따라 오르는 글자'], allLine: ['Every line and every space has a letter. One place up is the next letter.', '줄과 칸마다 글자가 있어요. 한 자리 오를 때마다 다음 글자예요.'],
  fig: () => ({ staff: kqStaff([30, 31, 32, 33, 34, 35, 36, 37], 'treble', { under: true }) }),
  steps: [
    { title: ['Treble lines', '높은음자리 줄'], line: ['The five lines, from the bottom: E G B D F. Every Good Boy Deserves Fun.', '다섯 줄을 아래에서부터 읽으면 E G B D F예요.'], fig: () => ({ staff: kqStaff(KQ_ST.treble.lines, 'treble', { under: true }) }) },
    { title: ['Treble spaces', '높은음자리 칸'], line: ['The four spaces, from the bottom: F A C E. They spell FACE.', '네 칸을 아래에서부터: F A C E. FACE라는 단어가 돼요.'], fig: () => ({ staff: kqStaff(KQ_ST.treble.spaces, 'treble', { under: true }) }) },
    { title: ['Bass lines', '낮은음자리 줄'], line: ['The bass staff starts two letters lower: G B D F A. Great Big Dragon Flies Away.', '낮은음자리 오선은 두 글자 아래에서 시작해요. 줄은 G B D F A예요.'], fig: () => ({ staff: kqStaff(KQ_ST.bass.lines, 'bass', { under: true }) }) },
    { title: ['Bass spaces', '낮은음자리 칸'], line: ['The spaces: A C E G. All Cows Eat Grass.', '칸은 A C E G예요.'], fig: () => ({ staff: kqStaff(KQ_ST.bass.spaces, 'bass', { under: true }) }) },
  ],
  make: (n) => kqNameQ(n % 2 === 0 ? 'treble' : 'bass'),
};
const KQ_LM = [
  { d: 24, c: 'bass', n: ['bass F', '낮은음자리표의 F'], w: ['line 4 of the bass staff', '낮은음자리 오선의 4번 줄'] }, { d: 21, c: 'bass', n: ['bass C', '낮은음자리표의 C'], w: ['space 2 of the bass staff', '낮은음자리 오선의 2번 칸'] },
  { d: 28, c: 'treble', n: ['middle C', '가운데 도'], w: ['the short line below the treble staff', '높은음자리 오선 아래의 짧은 줄'] }, { d: 32, c: 'treble', n: ['treble G', '높은음자리표의 G'], w: ['line 2 of the treble staff', '높은음자리 오선의 2번 줄'] }, { d: 35, c: 'treble', n: ['treble C', '높은음자리표의 C'], w: ['space 3 of the treble staff', '높은음자리 오선의 3번 칸'] }];
const kqCountQ = () => { const H = kqPick(KQ_LM.filter(x => x.d !== 28)), off = kqPick([-2, -1, 1, 2]), d = H.d + off, L = kqLetter(d), a = Math.abs(off), stp = a === 1 ? ' place ' : ' places ';
  return { kind: 'choice', cols: 4, prompt: ['Start from ' + H.n[0] + ' (ringed). Name the other note.', '동그라미 친 ' + H.n[1] + '에서 시작해요. 다른 음표의 이름을 말해요.'], opts: kqLet7(), ans: L, ok: (v) => v === L,
    fig: (c) => ({ staff: kqStaff([H.d, d], H.c, { ring: [0], under: c.res ? true : [0] }) }), yes: [L + ': ' + a + stp + (off > 0 ? 'up.' : 'down.'), L + '예요. ' + a + '자리 ' + (off > 0 ? '위예요.' : '아래예요.')],
    no: ['From ' + kqLetter(H.d) + ', go ' + a + stp + (off > 0 ? 'up' : 'down') + ' the alphabet: ' + L + '.', kqLetter(H.d) + '에서 알파벳으로 ' + a + '자리 ' + (off > 0 ? '위' : '아래') + '로 가면 ' + kqYe(L) + '.'] }; };
// the grand staff folded at middle C: each landmark above has its mirror below (G and F, the two Cs)
function KqFold({ stage = 2 }) {
  const yc = 150, h = 11, Y = (d) => yc - (d - 28) * h, T = KQ.COD, B = KQ.BL;
  const note = (x, d, col, lab, k) => <g key={k} style={{ animation: 'fadeUp 0.4s both' }}><ellipse cx={x} cy={Y(d)} rx="9" ry="6.5" fill={col} transform={`rotate(-18 ${x} ${Y(d)})`}/><text x={x - 16} y={Y(d) + 5} textAnchor="end" fontSize="15" fontWeight="900" fill={col}>{lab}</text></g>;
  const arc = (x, d1, d2, k) => <g key={k} style={{ animation: 'fadeUp 0.5s both' }} fill="none" stroke={KQ.NV} strokeWidth="2" strokeLinecap="round"><path d={`M${x + 12},${Y(d1)} C${x + 62},${Y(d1)} ${x + 62},${Y(d2)} ${x + 12},${Y(d2)}`}/><path d={`M${x + 20},${Y(d2) - 5} L${x + 12},${Y(d2)} L${x + 21},${Y(d2) + 4}`}/></g>;
  return <div style={{ maxWidth: 430, margin: '0 auto' }}><svg viewBox="0 0 340 300" style={{ width: '100%', display: 'block' }}>
    {[30, 32, 34, 36, 38, 18, 20, 22, 24, 26].map(d => <line key={d} x1="70" x2="300" y1={Y(d)} y2={Y(d)} stroke="#5a5c93" strokeWidth="1.6"/>)}
    <text x="8" y={Y(34) + 5} fontSize="14" fontWeight="900" fill={KQ.NV}>{t('treble', '높은음자리')}</text><text x="8" y={Y(22) + 5} fontSize="14" fontWeight="900" fill={KQ.NV}>{t('bass', '낮은음자리')}</text>
    <line x1="52" x2="320" y1={yc} y2={yc} stroke={KQ.CO} strokeWidth="2" strokeDasharray={stage >= 1 ? '7 5' : '0'} opacity={stage >= 1 ? 0.9 : 0.5}/>
    <line x1="150" x2="190" y1={yc} y2={yc} stroke={KQ.NV} strokeWidth="2"/>
    <ellipse cx="170" cy={yc} rx="9" ry="6.5" fill={KQ.CO} transform={`rotate(-18 170 ${yc})`}/><text x="192" y={yc - 8} fontSize="14" fontWeight="900" fill={KQ.COD}>{t('middle C', '가운데 도')}</text>
    {stage >= 1 && <>{note(110, 32, T, 'G', 'g')}{note(110, 24, B, 'F', 'f')}{arc(110, 32, 24, 'a1')}</>}
    {stage >= 2 && <>{note(230, 35, T, 'C', 'c1')}{note(230, 21, B, 'C', 'c2')}{arc(230, 35, 21, 'a2')}</>}
  </svg></div>;
}
const kqFoldKb = (stage) => ({ oct: 2, ks: [0, 24], base: -12, plain: true, mc: false, marks: { 12: 'pick', ...(stage >= 1 ? { 19: 'pick', 5: 'pickB' } : {}), ...(stage >= 2 ? { 0: 'seg4', 24: 'seg3' } : {}) }, names: { 12: 'C', ...(stage >= 1 ? { 19: 'G', 5: 'F' } : {}), ...(stage >= 2 ? { 0: 'C', 24: 'C' } : {}) }, ncol: { 12: KQ.COD, 19: KQ.COD, 5: KQ.BL, 0: KQ.BL, 24: KQ.COD } });
KQ_SPEC['kq-landmarks'] = {
  title: ['Five landmarks', '기준 음 다섯 개'], allLine: ['Fold the two staves at middle C and the landmarks mirror each other: G and F, and the two Cs.', '두 오선을 가운데 도에서 접으면 기준 음이 서로 마주 봐요. G와 F, 그리고 두 C예요.'],
  fig: () => ({ staff: <KqFold stage={2}/>, kb: kqFoldKb(2) }),
  steps: [
    { title: ['Middle C in the centre', '한가운데의 가운데 도'], line: ['The two staves meet at middle C, on a short line of its own. It is the centre of the keyboard too.', '두 오선은 가운데 도에서 만나요. 자기만의 짧은 줄 위에 있고, 건반에서도 한가운데예요.'], fig: () => ({ staff: <KqFold stage={0}/>, kb: kqFoldKb(0) }) },
    { title: ['Fold: G and F', '접기: G와 F'], line: ['Fold at middle C. Treble G, 4 steps above, meets bass F, 4 steps below. On the keyboard they are 7 keys either side.', '가운데 도에서 접어요. 4걸음 위의 높은음자리 G와 4걸음 아래의 낮은음자리 F가 마주 봐요. 건반에서는 양쪽으로 7칸이에요.'], fig: () => ({ staff: <KqFold stage={1}/>, kb: kqFoldKb(1) }) },
    { title: ['Fold again: the two Cs', '다시 접기: 두 C'], line: ['Seven steps above and seven steps below are the two other landmarks: treble C and bass C, an octave either side of middle C.', '7걸음 위와 7걸음 아래가 나머지 기준 음이에요. 높은음자리 C와 낮은음자리 C로, 가운데 도에서 한 옥타브씩 떨어져 있어요.'], fig: () => ({ staff: <KqFold stage={2}/>, kb: kqFoldKb(2) }) },
    { title: ['A place up', '한 자리 위'], line: ['Count letters from a landmark: one place up from G is A.', '기준 음에서 글자를 세어요. G에서 한 자리 위는 A예요.'], fig: () => ({ staff: kqStaff([32, 33], 'treble', { under: true, ring: [0] }) }) },
    { title: ['A place down', '한 자리 아래'], line: ['One place down from G is F.', 'G에서 한 자리 아래는 F예요.'], fig: () => ({ staff: kqStaff([32, 31], 'treble', { under: true, ring: [0] }) }) },
  ],
  make: (n, prev) => { if (n % 2 === 1) return kqCountQ(); let H; do { H = kqPick(KQ_LM); } while (prev && prev.H === H);
    return { H, kind: 'choice', cols: 1, prompt: ['Which landmark is this?', '어느 기준 음일까요?'], opts: KQ_LM.map(x => ({ id: String(x.d), label: () => t(x.n[0], x.n[1]) })), ans: String(H.d), ok: (v) => v === String(H.d),
      fig: () => ({ staff: kqStaff([H.d], H.c, { ring: [0] }) }), yes: [H.n[0].charAt(0).toUpperCase() + H.n[0].slice(1) + ': ' + H.w[0] + '.', kqYe(H.n[1]) + '. ' + H.w[1] + '이에요.'], no: ['This is ' + H.n[0] + ': ' + H.w[0] + '.', kqYe(H.n[1]) + '. ' + H.w[1] + '이에요.'] }; },
};
KQ_SPEC['kq-read'] = {
  title: ['From staff to keys', '오선에서 건반으로'], allLine: ['Read the note, then find its key. Tap a key to hear it.', '음표를 읽고, 그 건반을 찾아요. 건반을 누르면 소리가 나요.'],
  fig: () => ({ staff: kqStaff([32], 'treble', { under: true }), kb: { oct: 2, ks: [0, 12], base: 0, plain: true, marks: { 7: 'pick' }, names: { 7: 'G' }, ncol: { 7: KQ.COD } } }),
  steps: [
    { title: ['Treble: from middle C up', '높은음자리: 가운데 도에서 위로'], line: ['Treble G is the G just above middle C.', '높은음자리표의 G는 가운데 도 바로 위의 G예요.'], fig: () => ({ staff: kqStaff([32], 'treble', { under: true }), kb: { oct: 2, ks: [0, 12], base: 0, plain: true, marks: { 7: 'pick' }, names: { 7: 'G' }, ncol: { 7: KQ.COD } } }) },
    { title: ['Bass: from middle C down', '낮은음자리: 가운데 도에서 아래로'], line: ['Bass F is the F just below middle C.', '낮은음자리표의 F는 가운데 도 바로 아래의 F예요.'], fig: () => ({ staff: kqStaff([24], 'bass', { under: true }), kb: { oct: 2, ks: [0, 12], base: -12, plain: true, marks: { 5: 'pickB' }, names: { 5: 'F' }, ncol: { 5: KQ.BL } } }) },
  ],
  make: (n) => { const treble = n % 2 === 0, d = treble ? kqPick(KQ_ST.treble.lines.concat(KQ_ST.treble.spaces, [28, 39])) : kqPick(KQ_ST.bass.lines.concat(KQ_ST.bass.spaces, [27])), base = -24, tk = dMidiKey(d) - base, clef = treble ? 'treble' : 'bass', L = kqLetter(d);
    return { kind: 'key', retry: true, prompt: ['Which key is this note?', '이 음표는 어느 건반일까요?'], fig: () => ({ staff: kqStaff([d], clef), kb: { oct: 4, ks: treble ? [24, 48] : [0, 24], base, plain: true } }), ok: (k) => k === tk, onPick: (k, ok) => { if (ok) playKey(dMidiKey(d), 0.6); },
      yes: ['That is ' + L + '.', L + '예요.'], no: (k) => KQ_L[((k % 12) + 12) % 12] === L ? ['Right letter, but another ' + L + '. Check which octave the note is in.', '글자는 맞지만 다른 ' + L + '예요. 음표가 어느 옥타브인지 확인해 보세요.'] : ['That key is not ' + L + '. Count from ' + (treble ? 'treble G or middle C.' : 'bass F or middle C.'), '그 건반은 ' + L + '이(가) 아니에요. ' + (treble ? '높은음자리표의 G나 가운데 도' : '낮은음자리표의 F나 가운데 도') + '에서 세어 보세요.'] }; },
};

// ══ 4. Ledger lines and 8va ══
const KQ_LED = { 39: 0, 40: 1, 41: 1, 42: 2, 17: 0, 16: 1, 15: 1, 14: 2 };
KQ_SPEC['kq-ledger'] = {
  title: ['Ledger lines', '덧줄'], allLine: ['When a note is too high or too low for the five lines, short extra lines are added: ledger lines.', '다섯 줄에 담기지 않는 높은 음이나 낮은 음에는 짧은 덧줄을 더해요.'],
  fig: () => ({ staff: <>{kqStaff([38, 39, 40, 41, 42], 'treble', { under: true })}{kqStaff([18, 17, 16, 15, 14], 'bass', { under: true })}</> }),
  steps: [
    { title: ['Above the treble staff', '높은음자리 오선 위'], line: ['The top line is F. The letters carry on: G in the space above, A on the first ledger line.', '맨 윗줄은 F예요. 글자는 이어져요. 위의 칸은 G, 첫 덧줄은 A예요.'], fig: () => ({ staff: kqStaff([38, 39, 40], 'treble', { under: true, ring: [2] }) }) },
    { title: ['Higher still', '더 위로'], line: ['B in the next space, then C on the second ledger line.', '다음 칸은 B, 둘째 덧줄은 C예요.'], fig: () => ({ staff: kqStaff([40, 41, 42], 'treble', { under: true, ring: [2] }) }) },
    { title: ['Below the bass staff', '낮은음자리 오선 아래'], line: ['The bottom line is G. Going down: F in the space below, E on the first ledger line.', '맨 아랫줄은 G예요. 내려가면 아래 칸은 F, 첫 덧줄은 E예요.'], fig: () => ({ staff: kqStaff([18, 17, 16], 'bass', { under: true, ring: [2] }) }) },
    { title: ['Lower still', '더 아래로'], line: ['D in the next space, then C on the second ledger line.', '다음 칸은 D, 둘째 덧줄은 C예요.'], fig: () => ({ staff: kqStaff([16, 15, 14], 'bass', { under: true, ring: [2] }) }) },
  ],
  make: (n) => { const above = Math.floor(n / 2) % 2 === 0, clef = above ? 'treble' : 'bass', d = kqPick(above ? [39, 40, 41, 42, 43] : [17, 16, 15, 14]);
    if (n % 2 === 1 && KQ_LED[d] != null) { const a = KQ_LED[d], w = [['No ledger line', '덧줄 없음'], ['One ledger line', '덧줄 하나'], ['Two ledger lines', '덧줄 둘']];
      return { kind: 'choice', cols: 3, prompt: ['How many ledger lines does this note need?', '이 음표에는 덧줄이 몇 개 필요할까요?'], opts: w.map((x, i) => ({ id: String(i), label: () => t(x[0], x[1]) })), ans: String(a), ok: (v) => v === String(a), fig: () => ({ staff: kqStaff([d], clef, { ring: [0] }) }),
        yes: [a === 0 ? 'It sits in the space just beyond the staff, so none.' : 'It needs ' + a + ' ledger line' + (a > 1 ? 's' : '') + ' to reach it.', a === 0 ? '오선 바로 바깥 칸에 있어서 덧줄이 필요 없어요.' : '닿으려면 덧줄이 ' + a + '개 필요해요.'], no: ['Count the ledger lines from the staff to the note: ' + a + '.', '오선에서 음표까지 덧줄을 세어 보세요. ' + a + '개예요.'] }; }
    const L = kqLetter(d);
    return { kind: 'choice', cols: 4, prompt: ['Name this note.', '이 음표의 이름을 말해요.'], opts: kqLet7(), ans: L, ok: (v) => v === L, fig: (c) => ({ staff: kqStaff([d], clef, { ring: [0], under: c.res ? true : null }) }), yes: [L + '.', L + '예요.'],
      no: [L + '. ' + (above ? 'From the top line F, the letters carry on upward.' : 'From the bottom line G, the letters carry on downward.'), L + '예요. ' + (above ? '맨 윗줄 F에서 글자가 위로 이어져요.' : '맨 아랫줄 G에서 글자가 아래로 이어져요.')] }; },
};
KQ_SPEC['kq-middlec'] = {
  title: ['Middle C on the page', '악보 위의 가운데 도'], allLine: ['One key, two places on the page: under the treble staff, or above the bass staff.', '건반은 하나인데 악보에서는 두 자리예요: 높은음자리 오선 아래, 또는 낮은음자리 오선 위.'],
  fig: () => ({ staff: <>{kqStaff([28], 'treble')}{kqStaff([28], 'bass')}</>, kb: { oct: 2, ks: [0, 24], base: -12, names: { 12: 'C' }, ncol: { 12: KQ.COD }, marks: { 12: 'pick' } } }),
  steps: [
    { title: ['Under the treble staff', '높은음자리 오선 아래'], line: ['A short line below the lowest line.', '가장 아래 줄 밑의 짧은 줄이에요.'], fig: () => ({ staff: kqStaff([28], 'treble'), kb: { oct: 2, ks: [0, 24], base: -12, names: { 12: 'C' }, ncol: { 12: KQ.COD }, marks: { 12: 'pick' } } }) },
    { title: ['Above the bass staff', '낮은음자리 오선 위'], line: ['A short line above the top line. It is the same key.', '가장 위 줄 위의 짧은 줄이에요. 같은 건반이에요.'], fig: () => ({ staff: kqStaff([28], 'bass'), kb: { oct: 2, ks: [0, 24], base: -12, names: { 12: 'C' }, ncol: { 12: KQ.COD }, marks: { 12: 'pick' } } }) },
  ],
  make: () => { const treble = Math.random() < 0.5, d = kqPick([26, 27, 28, 29]), clef = treble ? 'treble' : 'bass', tk = dMidiKey(d) + 12;
    return { kind: 'key', retry: true, prompt: ['Find this note near middle C.', '가운데 도 근처의 이 음표를 찾아요.'], fig: () => ({ staff: kqStaff([d], clef), kb: { oct: 2, ks: [0, 24], base: -12, names: { 12: 'C' }, ncol: { 12: KQ.COD } } }), ok: (k) => k === tk, onPick: (k, ok) => { if (ok) playKey(dMidiKey(d), 0.6); },
      yes: ['That is ' + kqLetter(d) + '.', kqLetter(d) + '예요.'], no: (k) => KQ_L[((k % 12) + 12) % 12] === kqLetter(d) ? ['The right letter, but another one. Look for the one nearest middle C.', '글자는 맞지만 다른 것이에요. 가운데 도에서 가장 가까운 것을 찾아요.'] : ['That key is ' + (KQ_L[((k % 12) + 12) % 12] || 'a black key') + '. The note is ' + kqLetter(d) + ': count from middle C.', '그 건반은 ' + (KQ_L[((k % 12) + 12) % 12] || '검은건반') + '이에요. 이 음은 ' + kqLetter(d) + '예요: 가운데 도에서 세어 보세요.'] }; },
};
KQ_SPEC['kq-8va'] = {
  title: ['8va and 8vb', '8va와 8vb'], allLine: ['Very high or very low notes need many ledger lines. 8va above the notes: play one octave higher. 8vb below the notes: one octave lower.', '아주 높거나 아주 낮은 음은 덧줄이 많아져요. 음표 위에 8va가 있으면 한 옥타브 높게, 음표 아래에 8vb가 있으면 한 옥타브 낮게 쳐요.'],
  fig: () => ({ staff: kqStaff([38, 39, 40, 41], 'treble', { bracket: { from: 0, bar: 0, label: '8va' } }), kb: { oct: 3, base: 0, ks: [12, 36], marks: kqPaint(kqPaint({}, [17, 19, 21, 23], 'seg3'), [29, 31, 33, 35], 'seg4') } }),
  steps: [
    { title: ['As written', '쓴 그대로'], line: ['Without a sign, you play the keys the notes sit on.', '기호가 없으면 음표가 앉은 그대로의 건반을 쳐요.'], fig: () => ({ staff: kqStaff([38, 39, 40, 41], 'treble'), kb: { oct: 3, base: 0, marks: kqPaint({}, [17, 19, 21, 23], 'seg3') } }) },
    { title: ['With 8va', '8va가 있으면'], line: ['The same letters, one octave up: coral is written, blue is what you play.', '같은 글자를 한 옥타브 위에서: 코랄은 쓴 음, 파랑은 실제로 치는 음이에요.'], fig: () => ({ staff: kqStaff([38, 39, 40, 41], 'treble', { bracket: { from: 0, bar: 0, label: '8va' } }), kb: { oct: 3, base: 0, ks: [12, 36], marks: kqPaint(kqPaint({}, [17, 19, 21, 23], 'seg3'), [29, 31, 33, 35], 'seg4') } }) },
    { title: ['With 8vb', '8vb가 있으면'], line: ['8vb sits below the notes, mostly in the bass clef: the same letters, one octave lower. Coral is written, blue is what you play.', '8vb는 음표 아래에 있어요. 주로 낮은음자리표에서 써요. 같은 글자를 한 옥타브 아래에서 쳐요. 코랄은 쓴 음, 파랑은 실제로 치는 음이에요.'], fig: () => kq8vbFig() },
  ],
  make: (n) => { if (n % 2 === 1) { const d = kqPick(KQ_8VB), tk = dMidiKey(d) + 24, L = kqLetter(d);
    return { kind: 'key', retry: true, prompt: ['This note is under an 8vb. Which key do you play?', '이 음표 아래에 8vb가 있어요. 어느 건반을 칠까요?'], fig: () => ({ staff: <KqStaffSvg clef="bass" notes={[{ d }]} ott="8vb"/>, kb: kq8vbKb({ ks: [0, 24] }) }), ok: (k) => k === tk, onPick: (k, ok) => { if (ok) playKey(tk - 36, 0.6); },
      yes: ['One octave below the written ' + L + '.', '쓴 ' + L + '보다 한 옥타브 아래예요.'], no: (k) => [(KQ_L[((k % 12) + 12) % 12] ? 'That is ' + KQ_L[((k % 12) + 12) % 12] + '. ' : '') + 'Find the written ' + L + ', then take the next ' + L + ' to its left.', (KQ_L[((k % 12) + 12) % 12] ? '그건 ' + KQ_L[((k % 12) + 12) % 12] + ' 건반이에요. ' : '') + '쓴 ' + L + '를 찾고, 그 왼쪽의 다음 ' + L + '를 누르세요.'] }; }
    const d = kqPick([38, 39, 40, 41]), tk = dMidiKey(d) + 12; return { kind: 'key', retry: true, prompt: ['This note is under an 8va. Which key do you play?', '이 음표는 8va 아래에 있어요. 어느 건반을 칠까요?'], fig: () => ({ staff: kqStaff([d, d], 'treble', { bracket: { from: 0, bar: 0, label: '8va' } }), kb: { oct: 3, base: 0, ks: [12, 36], plain: true, names: { 12: 'C', 24: 'C', 36: 'C' }, ncol: { 12: KQ.NV, 24: KQ.NV, 36: KQ.NV } } }), ok: (k) => k === tk, onPick: (k, ok) => { if (ok) playKey(tk, 0.6); },
    yes: ['One octave above the written ' + kqLetter(d) + '.', '쓴 ' + kqLetter(d) + ' 한 옥타브 위예요.'], no: (k) => [(KQ_L[((k % 12) + 12) % 12] ? 'That is ' + KQ_L[((k % 12) + 12) % 12] + '. ' : '') + 'Find the written ' + kqLetter(d) + ', then take the next ' + kqLetter(d) + ' to its right.', (KQ_L[((k % 12) + 12) % 12] ? '그건 ' + KQ_L[((k % 12) + 12) % 12] + ' 건반이에요. ' : '') + '쓴 ' + kqLetter(d) + '를 찾고, 그 오른쪽의 다음 ' + kqLetter(d) + '를 누르세요.'] }; },
};

KQ_SPEC['kq-octave'] = {
  title: ['Octaves', '옥타브'], allLine: ['From any key to the next key with the same name is an octave.', '어떤 건반에서 같은 이름의 다음 건반까지가 한 옥타브예요.'],
  fig: () => ({ kb: { oct: 2, ks: [0, 24], base: 0, plain: true, marks: { 0: 'seg3', 12: 'seg3', 24: 'seg3' }, names: { 0: 'C', 12: 'C', 24: 'C' }, ncol: { 0: KQ.COD, 12: KQ.COD, 24: KQ.COD } } }),
  steps: [
    { title: ['Eight white keys', '흰건반 여덟 개'], line: ['Count the white keys from one C to the next, both ends included: eight. That is where the word octave comes from.', '한 C에서 다음 C까지 흰건반을 양 끝까지 세면 여덟 개예요. 그래서 옥타브라고 불러요.'],
      fig: (c) => { const W = [0, 2, 4, 5, 7, 9, 11, 12], m = {}, nm = {}, nc = {}; W.slice(0, Math.min(c.tk + 1, 8)).forEach((k, i) => { m[k] = i === 0 || i === 7 ? 'pick' : 'seg3'; nm[k] = String(i + 1); nc[k] = i === 0 || i === 7 ? KQ.COD : KQ.NV; }); return { kb: { oct: 1, ks: [0, 12], base: 0, plain: true, marks: m, names: nm, ncol: nc } }; } },
    { title: ['Twelve keys', '건반 열두 개'], line: ['Count every key, black ones too: the next C is 12 keys up.', '검은건반까지 모든 건반을 세면 다음 C는 12번째예요.'],
      fig: (c) => { const m = {}, nm = {}, nc = {}; for (let k = 1; k <= Math.min(c.tk, 12); k++) { m[k] = k === 12 ? 'pick' : 'seg3'; nm[k] = String(k); nc[k] = k === 12 ? KQ.COD : KQ.NV; } m[0] = 'pick'; nm[0] = 'C'; nc[0] = KQ.COD; return { kb: { oct: 1, ks: [0, 12], base: 0, plain: true, marks: m, names: nm, ncol: nc } }; } },
    { title: ['Same name, higher sound', '같은 이름, 더 높은 소리'], line: ['Tap the three Cs. It is the same note, each one higher.', '세 C를 눌러 보세요. 같은 음이고, 하나씩 더 높아져요.'], fig: () => ({ kb: { oct: 2, ks: [0, 24], base: 0, plain: true, marks: { 0: 'seg3', 12: 'seg3', 24: 'seg3' }, names: { 0: 'C', 12: 'C', 24: 'C' }, ncol: { 0: KQ.COD, 12: KQ.COD, 24: KQ.COD } } }) },
  ],
  make: (n) => { const W = [0, 2, 4, 5, 7, 9, 11], k = n % 3, s = kqPick(W);
    if (k === 2) { const targets = [s, s + 12, s + 24].concat(s === 0 ? [36] : []); return { kind: 'multi', targets, prompt: ['Tap every key with the same name as the marked key.', '표시된 건반과 이름이 같은 건반을 모두 눌러 보세요.'], prog: (a, b) => ['Found ' + a + ' of ' + b + '. Keep going.', b + '개 중 ' + a + '개를 찾았어요. 계속해요.'],
      fig: () => ({ kb: { oct: 3, ks: [0, 36], base: 0, plain: true, marks: { [s]: 'pick' } } }), yes: ['All ' + targets.length + ' found: one in each octave.', '모두 ' + targets.length + '개 찾았어요. 옥타브마다 하나씩이에요.'],
      no: (x) => [KQ_L[((x % 12) + 12) % 12] ? 'That key has a different name. Look one octave, 12 keys, from the marked key.' : 'That is a black key. Look one octave, 12 keys, from the marked key.', '그 건반은 이름이 달라요. 표시된 건반에서 한 옥타브, 건반 12개 떨어진 곳을 찾아 보세요.'] }; }
    const up = k === 0, from = up ? s : s + 12, tk = up ? s + 12 : s;
    return { kind: 'key', retry: true, prompt: up ? ['Tap the key one octave above the marked key.', '표시된 건반의 한 옥타브 위 건반을 눌러 보세요.'] : ['Tap the key one octave below the marked key.', '표시된 건반의 한 옥타브 아래 건반을 눌러 보세요.'], play: () => playKey(from, 0.7),
      fig: () => ({ kb: { oct: 3, ks: [0, 36], base: 0, plain: true, marks: { [from]: 'pick' } } }), ok: (x) => x === tk, yes: ['Same name, 12 keys ' + (up ? 'higher.' : 'lower.'), '이름이 같고, 건반 12개 ' + (up ? '위예요.' : '아래예요.')],
      no: (x) => x === from ? ['That is the marked key itself. One octave ' + (up ? 'up' : 'down') + ' is the next key with the same name.', '그건 표시된 건반 자신이에요. 한 옥타브 ' + (up ? '위' : '아래') + '는 같은 이름의 바로 다음 건반이에요.'] : [x % 12 === from % 12 ? 'Right name, but ' + (Math.abs(x - from) / 12) + ' octaves away. One octave is the next key with the same name.' : 'One octave ' + (up ? 'up' : 'down') + ' is 12 keys away: the next key with the same name.', x % 12 === from % 12 ? '이름은 맞지만 ' + (Math.abs(x - from) / 12) + '옥타브 떨어졌어요. 한 옥타브는 같은 이름의 바로 다음 건반이에요.' : '한 옥타브 ' + (up ? '위' : '아래') + '는 건반 12개 떨어진 곳, 같은 이름의 다음 건반이에요.'] }; },
};

// ══ Build D (her calls 2026-10-24: the old Keys-and-staff topics move onto the Home): writing notes, the alto clef, 8vb ══
// a staff drawn for the new lessons: whole-note heads left to right (with ledger lines), an 8va / 8vb bracket,
// and, with onPick, big tap rows for every line and space from lo to hi (one step = 5 units; the svg is drawn about twice size)
function KqStaffSvg({ clef, lo, hi, notes = [], onPick, ott }) {
  const c = CLEFS[clef], nN = notes.length, W = nN <= 1 ? 150 : 66 + (nN - 1) * 40 + 36, yOf = (d) => dY(d), ink = clefInkYs(clef, yOf, clef), ds = notes.map(n => n.d);
  const top = Math.max(hi != null ? hi : c.high, c.high, ...ds), bot = Math.min(lo != null ? lo : c.low, c.low, ...ds);
  const n = nN, xs = notes.map((_, i) => n === 1 ? 100 : 66 + i * 40);
  const by = ott === '8va' ? yOf(top) - 14 : ott === '8vb' ? yOf(bot) + 16 : null;
  const y0 = Math.min(yOf(top) - 9, ink[0] - 2, by != null ? by - 12 : 1e9), y1 = Math.max(yOf(bot) + 10, ink[1] + 2, by != null ? by + 8 : -1e9);
  const rows = []; if (onPick) for (let d = lo; d <= hi; d++) rows.push(d);
  return <svg viewBox={`0 ${y0} ${W} ${y1 - y0}`} style={{ width: '100%', maxWidth: 330, display: 'block', margin: '0 auto', touchAction: 'manipulation', userSelect: 'none' }}>
    {c.lines.map(l => <line key={l} x1="4" x2={W - 4} y1={yOf(l)} y2={yOf(l)} stroke={KQ.NV} strokeOpacity="0.6" strokeWidth="1.1"/>)}
    <ClefGlyph clef={clef} st={clef} yOf={yOf} ink={KQ.NV}/>
    {rows.map(d => <circle key={'g' + d} cx={100} cy={yOf(d)} r="1.2" fill={KQ.CO} opacity="0.55" style={{ pointerEvents: 'none' }}/>)}
    {notes.map((nt, i) => <g key={'n' + i} opacity={nt.op || 1} style={{ pointerEvents: 'none', animation: 'fadeUp 0.25s both' }}>
      <Ledgers clef={clef} d={nt.d} x={xs[i]} yOf={yOf} ink={KQ.NV}/>
      <ellipse cx={xs[i]} cy={yOf(nt.d)} rx="7" ry="5" transform={`rotate(-20 ${xs[i]} ${yOf(nt.d)})`} fill={nt.col || KQ.NV}/>
      {nt.lab && <text x={xs[i] + 11} y={yOf(nt.d) + 4} fontSize="11" fontWeight="900" fill={nt.col || KQ.NV} style={{ paintOrder: 'stroke', stroke: '#fffefa', strokeWidth: 3 }}>{nt.lab}</text>}
    </g>)}
    {ott && <g style={{ animation: 'fadeUp 0.3s both' }}><text x={xs[0] - 22} y={by + 4} fontSize="11" fontWeight="900" fontStyle="italic" fill={ott === '8va' ? KQ.COD : KQ.BL}>{ott}</text>
      <path d={`M${xs[0] - 2},${by} L${xs[n - 1] + 10},${by} L${xs[n - 1] + 10},${by + (ott === '8va' ? 6 : -6)}`} fill="none" stroke={ott === '8va' ? KQ.COD : KQ.BL} strokeWidth="1.3" strokeDasharray="4 3"/></g>}
    {rows.map(d => <rect key={'r' + d} x="40" y={yOf(d) - 2.5} width={W - 44} height="5" fill="transparent" style={{ cursor: 'pointer' }} onClick={() => onPick(d)}/>)}
  </svg>;
}
const kqCap = (a, col = KQ.NV) => <div style={{ textAlign: 'center', fontSize: 15, fontWeight: 900, color: col, margin: '6px 0 2px', textWrap: 'balance', wordBreak: 'keep-all' }}>{kqT(a)}</div>;
const kqClefW = (clef) => clef === 'treble' ? ['treble', '높은음자리'] : clef === 'bass' ? ['bass', '낮은음자리'] : ['alto', '알토음자리'];

// ── Write it on the staff: tap the place; any octave counts. Count from the Queen's G (treble) or the King's F (bass).
const KQ_WR = { treble: [28, 39], bass: [17, 28] };
const KQ_WR_FROM = { treble: [32, ['Count from G on line 2, the Queen’s line.', '2번 줄, 여왕의 줄 G에서 세어 보세요.']], bass: [24, ['Count from F on line 4, the King’s line.', '4번 줄, 왕의 줄 F에서 세어 보세요.']] };
const kqWrNotes = (clef, list) => list.map(([d, hl]) => ({ d, col: hl ? KQ.CO : KQ.NV, lab: kqLetter(d) }));
KQ_SPEC['kq-write'] = {
  title: ['Write it on the staff', '오선에 쓰기'], allLine: ['Tap a line or a space to write a note there. Its name appears beside it.', '줄이나 칸을 눌러 음표를 써 보세요. 옆에 음 이름이 나와요.'],
  fig: (c) => ({ staff: <KqStaffSvg clef="treble" lo={28} hi={39} notes={typeof c.last === 'number' ? [{ d: c.last, col: KQ.CO, lab: kqLetter(c.last) }] : []} onPick={(d) => { c.setLast(d); playKey(dMidiKey(d), 0.5); }}/> }),
  steps: [
    { title: ['G on line 2', '2번 줄의 G'], line: ['In the treble clef, G sits on line 2, the line the Queen’s curl circles.', '높은음자리표에서 G는 2번 줄에 있어요. 여왕의 말린 부분이 감싸는 줄이에요.'], fig: () => ({ staff: <KqStaffSvg clef="treble" notes={kqWrNotes('treble', [[32, 1]])}/> }) },
    { title: ['Count from G', 'G에서 세기'], line: ['To write B, count up from G, one letter per place: G on line 2, A in space 2, B on line 3.', 'B를 쓰려면 G에서 한 자리에 한 글자씩 올라가요. 2번 줄 G, 2번 칸 A, 3번 줄 B.'], fig: (c) => ({ staff: <KqStaffSvg clef="treble" notes={kqWrNotes('treble', [[32, 0], [33, 0], [34, 1]].slice(0, Math.min(c.tk + 1, 3)))}/> }) },
    { title: ['In the bass clef', '낮은음자리표에서'], line: ['In the bass clef start from F on line 4, the King’s line. To write D, count down: F, E, D.', '낮은음자리표에서는 4번 줄, 왕의 줄 F에서 시작해요. D를 쓰려면 F, E, D로 내려가요.'], fig: (c) => ({ staff: <KqStaffSvg clef="bass" notes={kqWrNotes('bass', [[24, 0], [23, 0], [22, 1]].slice(0, Math.min(c.tk + 1, 3)))}/> }) },
  ],
  make: (n, prev) => { const clef = n % 2 === 0 ? 'treble' : 'bass', [lo, hi] = KQ_WR[clef]; let L, g = 0; do { L = kqPick('CDEFGAB'.split('')); } while (prev && prev.L === L && g++ < 8);
    const all = []; for (let d = lo; d <= hi; d++) if (kqLetter(d) === L) all.push(d); const [fromD, hint] = KQ_WR_FROM[clef], w = kqClefW(clef);
    return { L, kind: 'tap', retry: true, prompt: ['Write ' + L + ' on the ' + w[0] + ' staff. Any ' + L + ' counts.', w[1] + ' 오선에 ' + L + '를 써 보세요. 어느 ' + L + '든 괜찮아요.'], ok: (v) => kqLetter(v) === L, onPick: (v) => playKey(dMidiKey(v), 0.5),
      fig: (c) => ({ staff: <KqStaffSvg clef={clef} lo={lo} hi={hi} onPick={c.res === 'ok' ? null : c.pick} notes={c.pickd == null ? [] : c.res === 'ok' ? all.map(d => ({ d, col: '#2e8a6e', op: d === c.pickd ? 1 : 0.4, lab: d === c.pickd ? L : null })) : [{ d: c.pickd, col: '#c8361b', lab: kqLetter(c.pickd) }]}/> }),
      yes: all.length > 1 ? [L + '. The faint one is ' + L + ' too, an octave away.', L + '예요. 흐린 음표도 한 옥타브 떨어진 ' + L + '예요.'] : [L + '.', L + '예요.'],
      no: (v) => ['That is ' + kqLetter(v) + '. ' + hint[0], '그건 ' + kqLetter(v) + '예요. ' + hint[1]] }; },
};

// ── The alto clef: the C clef, centred on line 3, middle C
const KQ_ALTO = [24, 25, 26, 27, 28, 29, 30, 31, 32];
const kqAltoKb = (d, o = {}) => ({ oct: 2, ks: [0, 24], base: -12, plain: true, names: { 12: 'C' }, ncol: { 12: KQ.COD }, marks: d == null ? { 12: 'pass' } : { 12: 'pass', [dMidiKey(d) + 12]: o.mk || 'pick' } });
KQ_SPEC['kq-alto'] = {
  title: ['The alto clef', '알토음자리표'], allLine: ['A third clef: the alto clef, a C clef. Its middle points at line 3, and line 3 is middle C.', '세 번째 음자리표, 알토음자리표는 C 음자리표예요. 가운데가 3번 줄을 가리키고, 그 줄이 가운데 도예요.'],
  fig: () => ({ staff: <KqStaffSvg clef="alto" notes={[{ d: 28, col: KQ.CO, lab: 'C' }]}/>, kb: kqAltoKb(28) }),
  steps: [
    { title: ['Middle C on line 3', '3번 줄은 가운데 도'], line: ['The clef sits right on the middle line. That line is middle C, the same key as always.', '음자리표가 가운데 줄에 딱 걸쳐 있어요. 그 줄이 가운데 도예요. 늘 치던 그 건반이에요.'], fig: () => ({ staff: <KqStaffSvg clef="alto" notes={[{ d: 28, col: KQ.CO, lab: 'C' }]}/>, kb: kqAltoKb(28) }) },
    { title: ['Count from C', 'C에서 세기'], line: ['Count up and down from middle C, one letter per place: D in the space above, B in the space below.', '가운데 도에서 한 자리에 한 글자씩 세어요. 위의 칸은 D, 아래 칸은 B예요.'], fig: () => ({ staff: <KqStaffSvg clef="alto" notes={[{ d: 27, lab: 'B' }, { d: 28, col: KQ.CO, lab: 'C' }, { d: 29, lab: 'D' }]}/>, kb: { ...kqAltoKb(28), marks: { 11: 'seg3', 12: 'pick', 14: 'seg3' } } }) },
    { title: ['Who reads it', '누가 읽을까요'], line: ['The viola reads the alto clef. Its notes sit in the middle: too high for the bass clef, too low for the treble.', '비올라가 알토음자리표를 읽어요. 비올라의 음은 가운데에 있어서, 낮은음자리표에는 너무 높고 높은음자리표에는 너무 낮아요.'], fig: () => ({ staff: <KqStaffSvg clef="alto" notes={[24, 26, 28, 30, 32].map(d => ({ d, col: d === 28 ? KQ.CO : KQ.NV, lab: kqLetter(d) }))}/> }) },
  ],
  make: (n, prev) => { const k = n % 3; let d, g = 0; do { d = kqPick(KQ_ALTO); } while (prev && prev.d === d && g++ < 8); const L = kqLetter(d), up = d - 28;
    const why = up === 0 ? ['Line 3 is middle C.', '3번 줄이 가운데 도예요.'] : ['Count ' + (up > 0 ? 'up' : 'down') + ' from middle C on line 3: ' + Math.abs(up) + ' place' + (Math.abs(up) > 1 ? 's' : '') + ', ' + L + '.', '3번 줄 가운데 도에서 ' + (up > 0 ? '위로' : '아래로') + ' ' + Math.abs(up) + '자리, ' + L + '예요.'];
    if (k === 1) return { d, kind: 'choice', cols: 3, prompt: ['In the alto clef, which line is middle C?', '알토음자리표에서 가운데 도는 몇 번 줄일까요?'], opts: [2, 3, 4].map(x => ({ id: String(x), label: () => t('Line ' + x, x + '번 줄') })), ans: '3', ok: (v) => v === '3',
      fig: (c) => ({ staff: <KqStaffSvg clef="alto" notes={c.res ? [{ d: 28, col: KQ.CO, lab: 'C' }] : []}/> }), yes: ['Line 3, the middle line.', '3번 줄, 가운데 줄이에요.'], no: ['The alto clef is centred on the middle line, line 3: middle C.', '알토음자리표는 가운데 줄, 3번 줄에 걸쳐 있어요. 그 줄이 가운데 도예요.'] };
    if (k === 0) return { d, kind: 'choice', cols: 4, prompt: ['Alto clef: name this note.', '알토음자리표: 이 음표의 이름은?'], opts: kqLet7(), ans: L, ok: (v) => v === L, fig: (c) => ({ staff: <KqStaffSvg clef="alto" notes={c.res ? [{ d: 28, col: KQ.CO, lab: 'C', op: d === 28 ? 0 : 0.5 }, { d, lab: L }] : [{ d }]}/> }),
      yes: [L + '.', L + '예요.'], no: why };
    const tk = dMidiKey(d) + 12;
    return { d, kind: 'key', retry: true, prompt: ['Alto clef: find this note on the keys.', '알토음자리표: 이 음을 건반에서 찾아요.'], fig: () => ({ staff: <KqStaffSvg clef="alto" notes={[{ d }]}/>, kb: kqAltoKb(null) }), ok: (x) => x === tk, onPick: (x, ok) => { if (ok) playKey(dMidiKey(d), 0.6); },
      yes: [L + ', ' + (up === 0 ? 'middle C itself.' : Math.abs(up) + ' white key' + (Math.abs(up) > 1 ? 's' : '') + ' ' + (up > 0 ? 'above' : 'below') + ' middle C.'), up === 0 ? '가운데 도 그 자체예요.' : L + ', 가운데 도에서 흰건반 ' + Math.abs(up) + '개 ' + (up > 0 ? '위예요.' : '아래예요.')], no: why };
  },
};

// ── 8vb, beside 8va: the same letters one octave lower (written below the notes, mostly in the bass clef)
const KQ_8VB = [17, 16, 15, 14];   // F E D C below the bass staff
const kq8vbKb = (o = {}) => ({ oct: 3, base: -36, ks: o.ks || [0, 17], plain: true, names: { 0: 'C', 12: 'C', 24: 'C' }, ncol: { 0: KQ.NV, 12: KQ.NV, 24: KQ.NV }, marks: o.marks || {} });
const kq8vbFig = () => ({ staff: <KqStaffSvg clef="bass" notes={KQ_8VB.map(d => ({ d, col: KQ.CO }))} ott="8vb"/>, kb: kq8vbKb({ marks: kqPaint(kqPaint({}, KQ_8VB.map(d => dMidiKey(d) + 36), 'seg3'), KQ_8VB.map(d => dMidiKey(d) + 24), 'seg4') }) });

// ══ 5. Pitch and range ══
const kqBars = ({ lens, hl, onTap, pickd }) => <svg viewBox="0 0 320 120" style={{ width: '100%', maxWidth: 340, display: 'block', margin: '0 auto' }}>
  {lens.map((h, i) => { const x = 20 + i * (280 / lens.length) + 4, w = 280 / lens.length - 8, on = hl === i, pk = pickd === i; return <g key={i} onClick={() => onTap && onTap(i)} style={{ cursor: onTap ? 'pointer' : 'default' }}><rect x={x} y={14} width={w} height={h} rx="6" fill={pk ? '#fad0c2' : on ? '#fbe3da' : '#fffefa'} stroke={on || pk ? KQ.CO : KQ.NV} strokeWidth="3"/>{onTap && <text x={x + w / 2} y={14 + h / 2 + 8} textAnchor="middle" fontSize="24" fontWeight="900" fill={on || pk ? KQ.COD : '#9a9cc2'} style={{ pointerEvents: 'none' }}>♪</text>}</g>; })}
</svg>;
const KQ_XY = [0, 2, 4, 5, 7, 9, 11, 12], KQ_LENS = [100, 92, 84, 78, 70, 62, 54, 46];
KQ_SPEC['kq-size'] = {
  title: ['Long and short', '긴 것과 짧은 것'], allLine: ['Tap the bars. Long ones sound low, short ones sound high.', '막대를 눌러 보세요. 긴 막대는 낮게, 짧은 막대는 높게 울려요.'],
  fig: (c) => ({ top: kqBars({ lens: KQ_LENS, hl: c.last, onTap: (i) => { playKey(KQ_XY[i], 0.7); c.setLast(i); } }) }),
  steps: [
    { title: ['The longest bar', '가장 긴 막대'], line: ['It makes the lowest sound.', '가장 낮은 소리가 나요.'], fig: () => ({ top: kqBars({ lens: KQ_LENS, hl: 0, onTap: (i) => playKey(KQ_XY[i], 0.7) }) }) },
    { title: ['The shortest bar', '가장 짧은 막대'], line: ['It makes the highest sound.', '가장 높은 소리가 나요.'], fig: () => ({ top: kqBars({ lens: KQ_LENS, hl: 7, onTap: (i) => playKey(KQ_XY[i], 0.7) }) }) },
  ],
  make: () => { const a = 30 + kqRnd(60), b = a + kqPick([-1, 1]) * (15 + kqRnd(30)), lens = [a, b], low = a > b ? 0 : 1, ans = low === 0 ? 'L' : 'R';
    return { kind: 'choice', cols: 2, prompt: ['Tap each bar to hear it. Which one sounds lower?', '막대를 하나씩 눌러 소리를 들어 보세요. 어느 쪽이 더 낮게 들리나요?'], opts: [{ id: 'L', label: () => t('The left bar', '왼쪽 막대') }, { id: 'R', label: () => t('The right bar', '오른쪽 막대') }], ans, ok: (v) => v === ans,
      fig: (c) => ({ top: kqBars({ lens, hl: c.res ? low : c.last, onTap: (i) => { playKey(i === low ? 0 : 12, 0.7); c.setLast(i); } }) }),
      yes: ['The longer bar sounds lower.', '더 긴 막대가 더 낮게 들려요.'], no: ['The longer bar sounds lower. The shorter one rings higher.', '더 긴 막대가 더 낮게 들려요. 짧은 막대는 더 높게 울려요.'] }; },
};
const KQ_PIANO = 'Piano (today, 88 keys)', KQ_RNG = [KQ_PIANO, 'Violin', 'Cello', 'Flute', 'Tuba', 'Soprano', 'Bass'];
// instrument sounds for the range lesson (a plain synth: bowed, flute, reed, brass, voice; keyboards use the piano)
const kqTimbre = (name) => { const r = SPR_RANGE(name); if (!r) return 'piano'; if (r.g === 'Strings') return /Guitar|Harp/.test(name) ? 'piano' : 'bow'; if (r.g === 'Woodwind') return /Flute|Piccolo/.test(name) ? 'flute' : 'reed'; if (r.g === 'Brass') return 'brass'; if (r.g === 'Voices') return 'voice'; return 'piano'; };
function kqSound(name, m, at = 0, len = 1.1) {
  const ctx = getAudio(); if (!ctx) return; const kind = kqTimbre(name), t0 = ctx.currentTime + 0.04 + at;
  if (kind === 'piano') return instNote('piano', ctx, t0, m, len, 0.48);
  const f = mFreq(m), out = ctx.createGain(), end = t0 + len, peak = 0.2, atk = kind === 'brass' ? 0.07 : kind === 'bow' ? 0.12 : kind === 'voice' ? 0.1 : 0.08;
  out.gain.setValueAtTime(0.0001, t0); out.gain.exponentialRampToValueAtTime(peak, t0 + atk); out.gain.setValueAtTime(peak, end - 0.18); out.gain.exponentialRampToValueAtTime(0.0001, end); out.connect(ctx.destination);
  const osc = (type, freq, g, dest) => { const o = ctx.createOscillator(), gg = ctx.createGain(); o.type = type; o.frequency.value = freq; gg.gain.value = g; o.connect(gg); gg.connect(dest); o.start(t0); o.stop(end + 0.05); return o; };
  const vib = (o, rate, depth, delay) => { const l = ctx.createOscillator(), lg = ctx.createGain(); l.frequency.value = rate; lg.gain.value = depth; l.connect(lg); lg.connect(o.frequency); l.start(t0 + delay); l.stop(end + 0.05); };
  const lp = (hz, q = 0.7) => { const b = ctx.createBiquadFilter(); b.type = 'lowpass'; b.frequency.value = hz; b.Q.value = q; b.connect(out); return b; };
  if (kind === 'bow') { const d = lp(Math.min(f * 5 + 600, 5000)); const a = osc('sawtooth', f, 0.6, d), b = osc('sawtooth', f * 1.004, 0.4, d); vib(a, 5.6, f * 0.007, 0.25); vib(b, 5.6, f * 0.007, 0.25); }
  else if (kind === 'flute') { const d = lp(Math.min(f * 4, 6000)); const a = osc('sine', f, 0.8, d); osc('sine', f * 2, 0.18, d); osc('triangle', f * 3, 0.05, d); vib(a, 5, f * 0.005, 0.3); }
  else if (kind === 'reed') { const d = lp(Math.min(f * 6, 4500), 1.5); const a = osc('square', f, 0.35, d); osc('sawtooth', f, 0.25, d); vib(a, 5, f * 0.004, 0.35); }
  else if (kind === 'brass') { const d = lp(f * 1.5, 1); d.frequency.setValueAtTime(f * 1.5, t0); d.frequency.linearRampToValueAtTime(Math.min(f * 7, 5000), t0 + 0.22); osc('sawtooth', f, 0.55, d); osc('sawtooth', f * 1.003, 0.35, d); }
  else { const mix = ctx.createGain(); mix.gain.value = 0.9; [[800, 6], [1150, 5], [2800, 3]].forEach(([hz, q]) => { const b = ctx.createBiquadFilter(); b.type = 'bandpass'; b.frequency.value = hz; b.Q.value = q; mix.connect(b); b.connect(out); }); const a = osc('sawtooth', f, 1, mix); vib(a, 5.5, f * 0.012, 0.25); }
}
const kqRangeFig = (name, c) => { const R = SPR_RANGE(name); return { top: <div style={{ maxWidth: 520, margin: '0 auto' }}><SprStrip range={[R.lo, R.hi]}/></div>,
  mid: <div style={{ display: 'flex', flexWrap: 'wrap', gap: 6, justifyContent: 'center', margin: '8px 0 0' }}>{KQ_RNG.map(n => <button key={n} className={'chip' + (n === name ? ' active' : '')} style={{ padding: '6px 12px', minHeight: 40 }} onClick={() => { const r = SPR_RANGE(n); kqSound(n, r.lo, 0, 0.9); kqSound(n, r.hi, 0.95, 0.9); c.setLast(n); }}>{kqRangeName(n)}</button>)}</div> }; };
KQ_SPEC['kq-range'] = {
  title: ['How far a piano reaches', '피아노가 닿는 범위'], allLine: ['A piano covers a huge range. Tap a name to see how much of it another instrument covers.', '피아노는 아주 넓은 범위를 맡아요. 이름을 눌러 다른 악기가 그중 얼마를 맡는지 보세요.'],
  fig: (c) => kqRangeFig(c.last || KQ_PIANO, c),
  steps: [
    { title: ['The piano', '피아노'], line: ['88 keys, from A0 at the far left to C8 at the far right.', '건반 88개, 맨 왼쪽 A0에서 맨 오른쪽 C8까지예요.'], fig: (c) => kqRangeFig(KQ_PIANO, c) },
    { title: ['The others', '다른 악기들'], line: ['A violin, a cello or a voice each covers only a part.', '바이올린, 첼로, 목소리는 각각 일부만 맡아요.'], fig: (c) => kqRangeFig(c.last && c.last !== KQ_PIANO ? c.last : 'Violin', c) },
  ],
  make: () => { let a, b; do { a = kqPick(KQ_RNG.slice(1)); b = kqPick(KQ_RNG.slice(1)); } while (a === b || SPR_RANGE(a).lo === SPR_RANGE(b).lo); const low = SPR_RANGE(a).lo < SPR_RANGE(b).lo ? a : b; return { kind: 'choice', prompt: ['Which one reaches lower?', '어느 쪽이 더 낮은 음까지 내려갈까요?'], opts: [a, b].map(n => ({ id: n, label: () => kqRangeName(n) })), ans: low, ok: (v) => v === low,
    fig: (c) => ({ top: <div style={{ maxWidth: 520, margin: '0 auto' }}><SprStrip range={c.res ? [SPR_RANGE(low).lo, SPR_RANGE(low).hi] : null}/></div> }), play: () => { kqSound(a, SPR_RANGE(a).lo, 0, 0.9); kqSound(b, SPR_RANGE(b).lo, 1, 0.9); },
    yes: [kqRangeName(low) + ' starts lower down.', kqRangeName(low) + '은(는) 더 낮은 곳에서 시작해요.'], no: ['It is the ' + kqRangeName(low) + ': its lowest note is lower.', kqRangeName(low) + '이(가) 정답이에요. 가장 낮은 음이 더 낮아요.'] }; },
};

// the registry: five sections, each lesson one idea
const kqRow = (id, en, ko, bEn, bKo) => [id, en, ko, bEn, bKo, () => <KqEngine spec={KQ_SPEC[id]}/>];
const KS_ROWS = [
  ['p-keys', [
    kqRow('kq-black', 'Black keys', '검은건반', 'Groups of 2 and 3, and low and high.', '2개와 3개씩 모인 검은건반, 낮은 소리와 높은 소리.'),
    kqRow('kq-houses', 'Naming the white keys', '흰건반 이름 붙이기', 'C D E around the group of 2, F G A B around the group of 3.', '2개 묶음 둘레의 C D E, 3개 묶음 둘레의 F G A B.'),
    kqRow('kq-names', 'Every key has its place', '모든 건반에는 제 자리가 있어요', 'The same name everywhere, middle C, 12 keys and 7 names.', '어디서나 같은 이름, 가운데 도, 건반 12개와 이름 7개.'),
    kqRow('kq-octave', 'Octaves', '옥타브', 'The next key with the same name: 8 white keys, 12 keys.', '같은 이름의 다음 건반: 흰건반 8개, 건반 12개.'),
  ]],
  ['p-stf', [
    kqRow('kq-lines', 'Lines and spaces', '줄과 칸', 'Five lines, four spaces, counted from the bottom.', '줄 다섯, 칸 넷, 아래에서부터 세기.'),
    kqRow('kq-climb', 'Higher and lower', '높은 음, 낮은 음', 'Up the staff is right on the keys.', '오선에서 위는 건반에서 오른쪽.'),
    kqRow('kq-clefs', 'Treble and bass clefs', '높은음자리표와 낮은음자리표', 'The Queen and the King: which notes each staff is for.', '여왕과 왕: 각 오선이 맡는 음.'),
    kqRow('kq-alto', 'The alto clef', '알토음자리표', 'A C clef: line 3 is middle C.', 'C 음자리표: 3번 줄이 가운데 도.'),
  ]],
  ['p-lines', [
    kqRow('kq-letters', 'Letters up the staff', '오선을 따라 오르는 글자', 'One place up is the next letter.', '한 자리 위는 다음 글자.'),
    kqRow('kq-landmarks', 'Five landmarks', '기준 음 다섯 개', 'Five notes to know, and counting from them.', '알아 둘 음 다섯 개와 거기서 세기.'),
    kqRow('kq-read', 'From staff to keys', '오선에서 건반으로', 'Read the note, find its key.', '음표를 읽고 건반 찾기.'),
    kqRow('kq-write', 'Write it on the staff', '오선에 쓰기', 'Tap the line or space; count from G or F.', '줄이나 칸을 눌러 쓰기, G나 F에서 세기.'),
  ]],
  ['p-ledger', [
    kqRow('kq-ledger', 'Ledger lines', '덧줄', 'Notes above and below the staff.', '오선 위아래의 음.'),
    kqRow('kq-middlec', 'Middle C on the page', '악보 위의 가운데 도', 'One key, two places on the page.', '건반 하나, 악보 위 두 자리.'),
    kqRow('kq-8va', '8va and 8vb', '8va와 8vb', 'One octave higher, or one octave lower, than written.', '쓴 것보다 한 옥타브 높게, 또는 낮게.'),
  ]],
  ['p-range', [
    kqRow('kq-size', 'Long and short', '긴 것과 짧은 것', 'Long bars sound low, short bars sound high.', '긴 막대는 낮게, 짧은 막대는 높게.'),
    kqRow('kq-range', 'How far a piano reaches', '피아노가 닿는 범위', 'The piano’s range next to other instruments.', '다른 악기와 비교한 피아노의 범위.'),
  ]],
];
