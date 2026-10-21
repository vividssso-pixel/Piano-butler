
// ─── Keys and staff, all six sections designed from the learning goal (her call 2026-10-21: "make them all, no overlap, don't cling to the old ones").
// One engine, three views for every lesson: the whole picture, one at a time, her turn. A wrong answer says plainly it is wrong and shows the right one.
// Facts come from her own material (the rhymes, the landmarks, the piano's range) or from the keyboard itself; nothing is added from memory.
const ksTT = (a) => t(a[0], a[1]);
const ksRnd = (n) => Math.floor(Math.random() * n), ksPick = (a) => a[ksRnd(a.length)];
const KS_W = [0, 2, 4, 5, 7, 9, 11], KS_L = { 0: 'C', 2: 'D', 4: 'E', 5: 'F', 7: 'G', 9: 'A', 11: 'B' }, KS_ABC = ['A', 'B', 'C', 'D', 'E', 'F', 'G'];
const ksNames = (oct, only) => { const n = {}; for (let o = 0; o < oct; o++) KS_W.forEach(p => { if (!only || only.includes(KS_L[p])) n[o * 12 + p] = KS_L[p]; }); return n; };
const ksMarks = (oct, pcs, style, base) => { const m = { ...(base || {}) }; for (let o = 0; o < oct; o++) pcs.forEach(p => { m[o * 12 + p] = style; }); return m; };
const ksSpan = (a, b, style, base) => { const m = { ...(base || {}) }; for (let k = a; k <= b; k++) m[k] = style; return m; };
const ksLetter = (d) => 'CDEFGAB'[((d % 7) + 7) % 7];
const ksStaff = (ds, clef, o = {}) => {
  const items = ds.map(d => ['q', 1, d]).concat([['||']]);
  const oo = { boxS: 26, D: 30, ring: o.ring || [], ...(o.under ? skgUnder(items, 'C', o.under === true ? null : o.under, o.coral || []) : {}) };
  if (o.bracket) { items.splice(ds.length, 0, ['|']); oo.bracket = o.bracket; }
  return <div style={{ maxWidth: 330, margin: '0 auto' }}><SkgStaff items={items} k="C" clef={clef} width={330} o={oo}/></div>;
};
const ksArrow = (pos, n) => <svg viewBox="0 0 500 34" style={{ width: '100%', display: 'block' }}>
  <text x="20" y="12" fontSize="13" fontWeight="900" fill="#c0431f">{t('← low', '← 낮은 음')}</text><text x="480" y="12" textAnchor="end" fontSize="13" fontWeight="900" fill="#c0431f">{t('high →', '높은 음 →')}</text>
  <line x1="20" y1="24" x2="470" y2="24" stroke="#26296b" strokeWidth="3"/><path d="M468 16 L486 24 L468 32 Z" fill="#26296b"/>
  {pos != null && <circle cx={20 + 450 * (pos + 0.5) / n} cy="24" r="8" fill="#e4572e" style={{ transition: 'cx 0.25s' }}/>}
</svg>;
const ksChain = (hl) => <div style={{ display: 'flex', justifyContent: 'center', gap: 5, margin: '2px 0 8px' }}>
  {['A', 'B', 'C', 'D', 'E', 'F', 'G', 'A'].map((L, i) => { const on = hl.includes(i); return <span key={i} style={{ width: 34, height: 40, borderRadius: 9, border: '2px solid ' + (on ? '#e4572e' : '#26296b'), background: on ? '#fbe3da' : '#fffefa', color: '#26296b', opacity: i === 7 && !on ? 0.35 : 1, display: 'flex', alignItems: 'center', justifyContent: 'center', fontWeight: 900, fontSize: 18, transition: 'all 0.2s' }}>{L}</span>; })}
</div>;
// five lines, four spaces, counted from the bottom
function KsLinesFig({ hl, labels, onTap, pickd, ok }) {
  const yl = (n) => 116 - (n - 1) * 26, col = (type, n) => hl && hl.type === type && hl.n === n ? '#e4572e' : '#26296b';
  const pk = (type, n) => pickd && pickd.type === type && pickd.n === n;
  return <svg viewBox="0 0 320 130" style={{ width: '100%', display: 'block', maxWidth: 340, margin: '0 auto' }}>
    {[1, 2, 3, 4].map(n => <rect key={'s' + n} x="40" y={yl(n + 1) + 7} width="240" height="12" rx="4" fill={pk('space', n) ? (ok ? '#cfe8dd' : '#f6c9bf') : hl && hl.type === 'space' && hl.n === n ? '#fbe3da' : 'transparent'} onClick={() => onTap && onTap({ type: 'space', n })} style={{ cursor: onTap ? 'pointer' : 'default' }}/>)}
    {[1, 2, 3, 4, 5].map(n => <g key={'l' + n} onClick={() => onTap && onTap({ type: 'line', n })} style={{ cursor: onTap ? 'pointer' : 'default' }}>
      <rect x="40" y={yl(n) - 7} width="240" height="14" fill="transparent"/>
      <line x1="40" x2="280" y1={yl(n)} y2={yl(n)} stroke={pk('line', n) ? (ok ? '#2e8a6e' : '#c8361b') : col('line', n)} strokeWidth={hl && hl.type === 'line' && hl.n === n || pk('line', n) ? 4 : 2}/>
    </g>)}
    {labels && [1, 2, 3, 4, 5].map(n => <text key={'tl' + n} x="22" y={yl(n) + 5} textAnchor="middle" fontSize="15" fontWeight="900" fill={col('line', n)}>{n}</text>)}
    {labels && [1, 2, 3, 4].map(n => <text key={'ts' + n} x="300" y={yl(n) - 8} textAnchor="middle" fontSize="15" fontWeight="900" fill={col('space', n)}>{n}</text>)}
    <text x="40" y="127" fontSize="11" fontWeight="800" fill="#c0431f">{t('count up from the bottom', '아래에서부터 세어요')}</text>
  </svg>;
}
const ksOrd = (n) => ['', t('1st', '첫째'), t('2nd', '둘째'), t('3rd', '셋째'), t('4th', '넷째'), t('5th', '다섯째')][n];

function KsEngine({ spec }) {
  const [view, setView] = useState('all'), [si, setSi] = useState(0), [qn, setQn] = useState(0), [q, setQ] = useState(null), [res, setRes] = useState(null), [pickd, setPickd] = useState(null), [last, setLast] = useState(null);
  const pick = (v) => { if (!q || res === 'ok' || (res === 'no' && !q.retry)) return; const ok = q.ok(v); setPickd(v); setRes(ok ? 'ok' : 'no'); if (q.onPick) q.onPick(v, ok); };
  const ctx = { last, setLast, res, pickd, si, q, pick, qn };
  const go = (v, i) => { setView(v); if (i != null) setSi(i); setRes(null); setPickd(null); };
  const newQ = (n) => { const nq = spec.make(n, q); setQ(nq); setQn(n); setRes(null); setPickd(null); setLast(null); if (nq.play) setTimeout(nq.play, 300); };
  const startTry = () => { setView('try'); newQ(0); };
  const show = (f) => {
    if (!f) return null;
    const kb = f.kb, marks = kb ? { ...(kb.marks || {}) } : {};
    if (kb && view === 'try' && q && q.kind === 'key' && pickd != null) marks[pickd] = res === 'ok' ? 'good' : 'bad';
    return <>
      {f.top}
      {f.staff}
      {f.mid}
      {kb && <TapKeyboard octaves={kb.oct} marks={marks} names={kb.names || null} tint={!!kb.tint} onTap={(k) => { playKey(k + (kb.base || 0), 0.6); setLast(k); if (view === 'try' && q && q.kind === 'key') pick(k); else if (kb.onTap) kb.onTap(k); }}/>}
      {f.below}
    </>;
  };
  const steps = spec.steps, tit = (a) => <div style={scS.title}>{ksTT(a)}</div>, lin = (a) => <div style={scS.line}>{ksTT(a)}</div>;
  let body;
  if (view === 'all') body = <>
    {tit(spec.title)}{lin(spec.allLine)}{show(spec.fig(ctx))}
    {scRow(<button className="ghost-btn" style={scS.prim} onClick={() => go('step', 0)}>{t('One at a time →', '하나씩 →')}</button>)}
  </>;
  else if (view === 'step') { const s = steps[si]; body = <>
    {tit(s.title)}{lin(s.line)}{show(s.fig(ctx))}
    {scRow(<>
      <button className="ghost-btn" style={scS.back} onClick={() => si === 0 ? go('all') : go('step', si - 1)}>{t('← Back', '← 이전')}</button>
      <button className="ghost-btn" style={scS.prim} onClick={() => si < steps.length - 1 ? go('step', si + 1) : startTry()}>{si < steps.length - 1 ? t('Next →', '다음 →') : t('Your turn →', '내가 해보기 →')}</button>
    </>)}
  </>; }
  else if (q) { const f = q.fig(ctx), asked = res == null;
    const txt = res === 'ok' ? [t('Yes! ', '맞아요! ') + ksTT(q.yes), true] : res === 'no' ? [(q.kind === 'choice' ? t('Not that one. ', '아니에요. ') : '') + ksTT(typeof q.no === 'function' ? q.no(pickd) : q.no), false] : ['', null];
    body = <>
      {tit(spec.tryTitle || ['Your turn', '내가 해보기'])}{lin(q.prompt)}{show(f)}
      {q.opts && <div style={{ display: 'grid', gridTemplateColumns: 'repeat(' + (q.cols || 2) + ',1fr)', gap: 8, margin: '10px 0 0' }}>
        {q.opts.map(o => <button key={o.id} className={'choice-btn' + (res == null ? '' : o.id === q.ans ? ' good' : o.id === pickd ? ' bad' : '')} disabled={res != null} onClick={() => pick(o.id)} style={{ padding: '13px 4px', fontSize: q.cols > 3 ? 18 : 16, fontWeight: 900 }}>{typeof o.label === 'function' ? o.label() : o.label}</button>)}
      </div>}
      {kpFeed(txt[1], txt[0])}
      {scRow(<>
        <button className="ghost-btn" style={scS.back} onClick={() => go('step', steps.length - 1)}>{t('← Back', '← 이전')}</button>
        {q.play && <button className="ghost-btn" style={scS.back} onClick={q.play}>{t('♪ Again', '♪ 다시')}</button>}
        {(res === 'ok' || (res === 'no' && !q.retry)) && <button className="ghost-btn" style={scS.prim} onClick={() => newQ(qn + 1)}>{t('Another →', '다른 것 →')}</button>}
        {res === 'no' && q.retry && <button className="ghost-btn" style={scS.back} onClick={() => { setRes(null); setPickd(null); }}>{t('Try again', '다시 해 보기')}</button>}
      </>)}
    </>; }
  return scBox('kp', body);
}
const ksLet7 = () => ['C', 'D', 'E', 'F', 'G', 'A', 'B'].map(L => ({ id: L, label: L }));
const KS_SPEC = {};

// ══ 1. Keyboard patterns ══
// high and low
KS_SPEC['kp-hear'] = {
  title: ['Low and high', '낮은 소리, 높은 소리'], allLine: ['On the piano, left is low and right is high. Tap keys and watch the dot.', '피아노에서는 왼쪽이 낮은 소리, 오른쪽이 높은 소리예요. 건반을 누르고 점을 보세요.'],
  fig: (c) => ({ top: ksArrow(c.last, 48), kb: { oct: 4, base: -24 } }),
  steps: [
    { title: ['Left: low', '왼쪽: 낮은 소리'], line: ['Tap the keys on the left. They sound low.', '왼쪽 건반을 눌러 보세요. 낮은 소리가 나요.'], fig: (c) => ({ top: ksArrow(c.last, 48), kb: { oct: 4, base: -24, marks: ksSpan(0, 11, 'target') } }) },
    { title: ['Right: high', '오른쪽: 높은 소리'], line: ['Tap the keys on the right. They sound high.', '오른쪽 건반을 눌러 보세요. 높은 소리가 나요.'], fig: (c) => ({ top: ksArrow(c.last, 48), kb: { oct: 4, base: -24, marks: ksSpan(36, 47, 'target') } }) },
  ],
  tryTitle: ['Which is higher?', '어느 쪽이 더 높을까요?'],
  make: (n) => {
    const gap = [30, 20, 12, 7, 4, 2][Math.min(n, 5)], lo = ksRnd(48 - gap), hi = lo + gap, firstHigh = Math.random() < 0.5, a = firstHigh ? hi : lo, b = firstHigh ? lo : hi;
    return { kind: 'choice', prompt: ['Listen to two sounds. Which one is higher?', '두 소리를 들어 보세요. 어느 쪽이 더 높을까요?'], opts: [{ id: '1', label: () => t('The first', '처음 소리') }, { id: '2', label: () => t('The second', '나중 소리') }], ans: firstHigh ? '1' : '2',
      play: () => { playKey(a - 24, 0.8); setTimeout(() => playKey(b - 24, 0.8), 900); },
      fig: (c) => ({ top: ksArrow(c.res ? hi : null, 48), kb: { oct: 4, base: -24, marks: c.res ? { [lo]: 'target', [hi]: 'good' } : {} } }), ok: (v) => v === (firstHigh ? '1' : '2'),
      yes: [(firstHigh ? 'The first' : 'The second') + ' sound was higher: its key is further right.', (firstHigh ? '처음' : '나중') + ' 소리가 더 높았어요. 그 건반이 더 오른쪽에 있어요.'],
      no: [(firstHigh ? 'The first' : 'The second') + ' sound was higher: its key is further right.', (firstHigh ? '처음' : '나중') + ' 소리가 더 높아요. 그 건반이 더 오른쪽에 있어요.'] };
  },
};
// the pattern repeats
const ksBr3 = (hl) => <svg viewBox="-1 0 758 34" style={{ width: '100%', display: 'block' }}>{[0, 1, 2].map(o => <g key={o} style={{ opacity: hl == null || hl === o ? 1 : 0.2, transition: 'opacity 0.25s' }}><path d={`M${o * 252 + 4},32 V20 H${o * 252 + 248} V32`} fill="none" stroke={hl === o ? '#e4572e' : '#26296b'} strokeWidth="3" strokeLinejoin="round"/><text x={o * 252 + 126} y="14" textAnchor="middle" fontSize="15" fontWeight="900" fill={hl === o ? '#e4572e' : '#26296b'}>{o + 1}</text></g>)}</svg>;
KS_SPEC['kp-repeat'] = {
  title: ['The pattern repeats', '같은 무늬가 되풀이돼요'], allLine: ['2 black keys, then 3. Then again: 2, then 3. The same pattern starts again and again.', '검은건반 2개, 3개. 그리고 또 2개, 3개. 같은 무늬가 계속 다시 시작돼요.'],
  fig: () => ({ top: ksBr3(null), kb: { oct: 3, base: 0, names: ksNames(3, ['C']), marks: ksMarks(3, [0], 'target') } }),
  steps: [
    { title: ['One pattern is 12 keys', '무늬 하나는 건반 12개'], line: ['7 white keys and 5 black keys: 2 black, then 3 black. That is one pattern.', '흰건반 7개와 검은건반 5개예요. 검은건반 2개, 3개가 무늬 하나예요.'], fig: () => ({ top: ksBr3(0), kb: { oct: 3, base: 0, marks: ksSpan(0, 11, 'pass') } }) },
    { title: ['Then it starts again', '그리고 다시 시작해요'], line: ['The next 12 keys are the same pattern, a little higher.', '다음 건반 12개도 같은 무늬예요. 조금 더 높은 소리예요.'], fig: () => ({ top: ksBr3(1), kb: { oct: 3, base: 0, marks: ksSpan(12, 23, 'pass') } }) },
    { title: ['Every pattern starts on C', '무늬는 모두 C에서 시작해요'], line: ['Each pattern starts at the white key just left of the group of 2. That key is called C.', '무늬는 검은건반 2개짜리 무리의 바로 왼쪽 흰건반에서 시작해요. 이 건반의 이름이 C예요.'], fig: () => ({ top: ksBr3(null), kb: { oct: 3, base: 0, names: ksNames(3, ['C']), marks: ksMarks(3, [0], 'target') } }) },
  ],
  make: () => ({ kind: 'key', retry: true, prompt: ['Tap a key where a new pattern starts: the white key just left of a group of 2.', '새 무늬가 시작되는 건반을 눌러 보세요: 검은건반 2개짜리 무리의 바로 왼쪽 흰건반이에요.'], fig: () => ({ top: ksBr3(null), kb: { oct: 3, base: 0 } }), ok: (k) => k % 12 === 0,
    yes: ['That key is C, where a pattern starts.', '그 건반은 C예요. 무늬가 시작되는 곳이에요.'], no: (k) => [([1, 3, 6, 8, 10].includes(k % 12) ? 'That is a black key. ' : 'That key does not start a pattern. ') + 'Look for the white key just left of a group of 2 black keys.', ([1, 3, 6, 8, 10].includes(k % 12) ? '그건 검은건반이에요. ' : '그 건반에서는 무늬가 시작되지 않아요. ') + '검은건반 2개짜리 무리의 바로 왼쪽 흰건반을 찾아보세요.'] }),
};
// middle C
const KS_MC = [
  { k: 24, p: ['Tap middle C: the C in the middle of the keyboard.', '가운데 도를 눌러 보세요: 건반 한가운데에 있는 C예요.'], y: ['That is middle C.', '그게 가운데 도예요.'] },
  { k: 36, p: ['Tap the next C to the right of middle C.', '가운데 도 바로 오른쪽의 다음 C를 눌러 보세요.'], y: ['That C is one pattern to the right of middle C.', '가운데 도에서 무늬 하나만큼 오른쪽에 있는 C예요.'] },
  { k: 12, p: ['Tap the next C to the left of middle C.', '가운데 도 바로 왼쪽의 다음 C를 눌러 보세요.'], y: ['That C is one pattern to the left of middle C.', '가운데 도에서 무늬 하나만큼 왼쪽에 있는 C예요.'] },
];
KS_SPEC['kp-middle'] = {
  title: ['Middle C', '가운데 도'], allLine: ['The C in the middle of the keyboard is called middle C. Tap it.', '건반 한가운데 있는 C를 가운데 도라고 불러요. 눌러 보세요.'],
  fig: () => ({ kb: { oct: 4, base: -24, names: ksNames(4, ['C']), marks: { 24: 'target' } } }),
  steps: [
    { title: ['Find the middle', '한가운데 찾기'], line: ['This keyboard has four patterns. Middle C starts the third one, in the middle.', '이 건반에는 무늬가 네 개 있어요. 가운데 도는 한가운데, 세 번째 무늬를 시작해요.'], fig: () => ({ kb: { oct: 4, base: -24, marks: { 24: 'target' }, names: { 24: 'C' } } }) },
    { title: ['The other C’s', '다른 C들'], line: ['The other C’s are not in the middle. Each one is a pattern away.', '다른 C들은 한가운데가 아니에요. 무늬 하나씩 떨어져 있어요.'], fig: () => ({ kb: { oct: 4, base: -24, names: ksNames(4, ['C']), marks: ksMarks(4, [0], 'pass', { 24: 'target' }) } }) },
  ],
  make: (n) => { const Q = KS_MC[n % KS_MC.length]; return { kind: 'key', retry: true, prompt: Q.p, fig: () => ({ kb: { oct: 4, base: -24 } }), ok: (k) => k === Q.k, yes: Q.y,
    no: (k) => k % 12 === 0 ? ['That is a C, but not the one we want. Count the patterns from middle C.', '그건 C지만 찾는 C가 아니에요. 가운데 도에서 무늬를 세어 보세요.'] : ['That is not a C. A C is the white key just left of a group of 2 black keys.', '그건 C가 아니에요. C는 검은건반 2개짜리 무리의 바로 왼쪽 흰건반이에요.'] }; },
};

// ══ 2. Note names ══
const ksNext = (L, dir) => KS_ABC[(KS_ABC.indexOf(L) + dir + 7) % 7];
KS_SPEC['nn-letters'] = {
  title: ['Seven letters', '글자는 일곱 개'], allLine: ['Music uses only seven letters: A B C D E F G. After G, it starts again at A.', '음악은 글자 일곱 개만 써요: A B C D E F G. G 다음에는 다시 A로 돌아가요.'],
  fig: () => ({ top: ksChain([]), kb: { oct: 2, base: 0, names: ksNames(2) } }),
  steps: [
    { title: ['A B C D E F G', 'A B C D E F G'], line: ['Seven letters, always in this order.', '일곱 글자는 늘 이 순서예요.'], fig: () => ({ top: ksChain([0, 1, 2, 3, 4, 5, 6]), kb: { oct: 2, base: 0, names: ksNames(2) } }) },
    { title: ['Then start again', '그리고 다시 시작'], line: ['After G comes A again. The letters go round and round.', 'G 다음에는 다시 A예요. 글자는 계속 돌고 돌아요.'], fig: () => ({ top: ksChain([6, 7]), kb: { oct: 2, base: 0, names: ksNames(2) } }) },
  ],
  make: () => { const L = ksPick(KS_ABC), dir = Math.random() < 0.5 ? 1 : -1, ans = ksNext(L, dir); return { kind: 'choice', cols: 4, prompt: dir > 0 ? ['Which letter comes after ' + L + '?', L + ' 다음에 오는 글자는?'] : ['Which letter comes before ' + L + '?', L + ' 바로 앞의 글자는?'],
    opts: KS_ABC.map(x => ({ id: x, label: x })), ans, ok: (v) => v === ans, fig: () => ({ top: ksChain(KS_ABC.indexOf(L) < 0 ? [] : [KS_ABC.indexOf(L) + (L === 'A' && dir < 0 ? 0 : 0)]) }),
    yes: [ans + ' comes ' + (dir > 0 ? 'after ' : 'before ') + L + '.', ans + '가 ' + L + (dir > 0 ? ' 다음이에요.' : ' 바로 앞이에요.')],
    no: [ans + ' comes ' + (dir > 0 ? 'after ' : 'before ') + L + (L === 'G' && dir > 0 ? ': after G it starts again at A.' : L === 'A' && dir < 0 ? ': before A, the letters wrap round to G.' : '.'), ans + '가 ' + L + (dir > 0 ? ' 다음이에요.' : ' 바로 앞이에요.') + (L === 'G' && dir > 0 ? ' G 다음에는 다시 A예요.' : L === 'A' && dir < 0 ? ' A 앞에는 G가 와요.' : '')] }; },
};
const KS_GUIDE = { C: ['C is at the left door of the small house.', 'C는 작은 집의 왼쪽 문에 있어요.'], D: ['D is inside the small house, between its two black keys.', 'D는 작은 집 안, 두 검은건반 사이에 있어요.'], E: ['E is at the right door of the small house.', 'E는 작은 집의 오른쪽 문에 있어요.'],
  F: ['F is at the left door of the big house.', 'F는 큰 집의 왼쪽 문에 있어요.'], G: ['G is inside the big house, between its first and second black keys.', 'G는 큰 집 안, 첫째와 둘째 검은건반 사이에 있어요.'], A: ['A is inside the big house, between its second and third black keys.', 'A는 큰 집 안, 둘째와 셋째 검은건반 사이에 있어요.'], B: ['B is at the right door of the big house.', 'B는 큰 집의 오른쪽 문에 있어요.'] };
const KS_PC = { C: 0, D: 2, E: 4, F: 5, G: 7, A: 9, B: 11 };
KS_SPEC['nn-houses'] = {
  title: ['The white keys by house', '집으로 흰건반 찾기'], allLine: ['The group of 2 black keys is a small house, the group of 3 is a big house. Every white key has a place in a house.', '검은건반 2개짜리 무리는 작은 집, 3개짜리 무리는 큰 집이에요. 흰건반은 모두 어느 집에 자리가 있어요.'],
  fig: () => ({ top: <KpRoofs/>, kb: { oct: 2, base: 0, names: ksNames(2), tint: true } }),
  steps: [
    { title: ['C D E: the small house', 'C D E: 작은 집'], line: ['C is at the left door, D is inside, E is at the right door.', 'C는 왼쪽 문, D는 집 안, E는 오른쪽 문에 있어요.'], fig: () => ({ top: <KpRoofs show="small"/>, kb: { oct: 2, base: 0, names: ksNames(2, ['C', 'D', 'E']), marks: ksMarks(2, [0, 2, 4], 'target'), tint: true } }) },
    { title: ['F G A B: the big house', 'F G A B: 큰 집'], line: ['F is at the left door, G and A are inside, B is at the right door.', 'F는 왼쪽 문, G와 A는 집 안, B는 오른쪽 문에 있어요.'], fig: () => ({ top: <KpRoofs show="big"/>, kb: { oct: 2, base: 0, names: ksNames(2, ['F', 'G', 'A', 'B']), marks: ksMarks(2, [5, 7, 9, 11], 'target'), tint: true } }) },
  ],
  make: () => { const L = ksPick(['D', 'F', 'B', 'C', 'G', 'E', 'A']); return { kind: 'key', retry: true, prompt: ['Tap ' + L + '. Think of the house first.', L + '을 눌러 보세요. 먼저 어느 집인지 생각해 봐요.'], fig: () => ({ top: <KpRoofs/>, kb: { oct: 2, base: 0, tint: true } }), ok: (k) => k % 12 === KS_PC[L],
    yes: KS_GUIDE[L], no: (k) => [(KS_L[k % 12] ? 'That is ' + KS_L[k % 12] + '. ' : 'That is a black key. ') + KS_GUIDE[L][0], (KS_L[k % 12] ? '그건 ' + KS_L[k % 12] + '예요. ' : '그건 검은건반이에요. ') + KS_GUIDE[L][1]] }; },
};
KS_SPEC['nn-updown'] = {
  title: ['Right is next, left is back', '오른쪽은 다음, 왼쪽은 앞'], allLine: ['Move one white key to the right: the next letter. Move one to the left: the letter before.', '흰건반 하나 오른쪽으로 가면 다음 글자, 왼쪽으로 가면 앞의 글자예요.'],
  fig: () => ({ kb: { oct: 2, base: 0, names: ksNames(2) } }),
  steps: [
    { title: ['One to the right', '오른쪽으로 하나'], line: ['From C, one white key right is D.', 'C에서 흰건반 하나 오른쪽은 D예요.'], fig: () => ({ kb: { oct: 2, base: 0, names: { 0: 'C', 2: 'D' }, marks: { 0: 'pick', 2: 'good' } } }) },
    { title: ['One to the left', '왼쪽으로 하나'], line: ['From E, one white key left is D.', 'E에서 흰건반 하나 왼쪽은 D예요.'], fig: () => ({ kb: { oct: 2, base: 0, names: { 2: 'D', 4: 'E' }, marks: { 4: 'pick', 2: 'good' } } }) },
  ],
  make: () => { const W = []; for (let o = 0; o < 2; o++) KS_W.forEach(p => W.push(o * 12 + p)); const n = ksPick([1, 1, 2]), dir = Math.random() < 0.5 ? 1 : -1, s = ksPick(W.map((_, i) => i).filter(i => i + dir * n >= 0 && i + dir * n < 14 && i >= 2 && i <= 11)), tgt = W[s + dir * n], sk = W[s];
    return { kind: 'key', retry: true, prompt: ['Start at ' + KS_L[sk % 12] + '. Tap the key ' + (n === 1 ? 'one' : 'two') + ' white ' + (n === 1 ? 'key' : 'keys') + ' to the ' + (dir > 0 ? 'right' : 'left') + '.', KS_L[sk % 12] + '에서 시작해요. ' + (dir > 0 ? '오른쪽' : '왼쪽') + '으로 흰건반 ' + (n === 1 ? '하나' : '둘') + ' 간 건반을 눌러 보세요.'],
      fig: () => ({ kb: { oct: 2, base: 0, names: { [sk]: KS_L[sk % 12] }, marks: { [sk]: 'pick' } } }), ok: (k) => k === tgt,
      yes: [KS_L[tgt % 12] + ' is ' + (n === 1 ? 'one' : 'two') + ' to the ' + (dir > 0 ? 'right' : 'left') + ' of ' + KS_L[sk % 12] + '.', KS_L[tgt % 12] + '가 ' + KS_L[sk % 12] + '에서 ' + (dir > 0 ? '오른쪽' : '왼쪽') + '으로 ' + (n === 1 ? '하나' : '둘') + ' 간 건반이에요.'],
      no: (k) => ['That is ' + (KS_L[k % 12] || 'a black key') + '. Count white keys ' + (dir > 0 ? 'to the right' : 'to the left') + ' of ' + KS_L[sk % 12] + ': ' + (n === 1 ? 'one' : 'two') + ' step' + (n === 1 ? '' : 's') + '.', '그건 ' + (KS_L[k % 12] || '검은건반') + '예요. ' + KS_L[sk % 12] + '에서 ' + (dir > 0 ? '오른쪽' : '왼쪽') + '으로 흰건반을 ' + (n === 1 ? '하나' : '둘') + ' 세어 보세요.'] }; },
};
KS_SPEC['nn-find'] = {
  title: ['Every key with the same name', '이름이 같은 건반 모두 찾기'], allLine: ['The same letter shows up in every pattern. Tap a white key to light them all.', '같은 글자는 무늬마다 하나씩 있어요. 흰건반을 누르면 같은 글자가 모두 켜져요.'],
  fig: (c) => { const p = c.last != null ? ((c.last % 12) + 12) % 12 : null; return { kb: { oct: 3, base: -12, names: p != null && KS_L[p] ? ksNames(3, [KS_L[p]]) : null, marks: p != null && KS_L[p] ? ksMarks(3, [p], 'target') : {} } }; },
  steps: [
    { title: ['All the D’s', '모든 D'], line: ['D is inside the small house, in every pattern.', 'D는 무늬마다 작은 집 안에 있어요.'], fig: () => ({ kb: { oct: 3, base: -12, names: ksNames(3, ['D']), marks: ksMarks(3, [2], 'target') } }) },
    { title: ['All the G’s', '모든 G'], line: ['G is inside the big house, in every pattern.', 'G는 무늬마다 큰 집 안에 있어요.'], fig: () => ({ kb: { oct: 3, base: -12, names: ksNames(3, ['G']), marks: ksMarks(3, [7], 'target') } }) },
  ],
  make: () => { const L = ksPick(['D', 'G', 'A', 'E', 'F', 'B', 'C']); return { kind: 'key', retry: true, prompt: ['Tap any ' + L + ' on the keyboard.', '건반에서 ' + L + ' 아무거나 눌러 보세요.'], fig: () => ({ kb: { oct: 3, base: -12 } }), ok: (k) => k % 12 === KS_PC[L],
    yes: ['That key is ' + L + '. Every ' + L + ' sits in the same place in its pattern.', '그 건반은 ' + L + '예요. ' + L + '는 무늬 안에서 항상 같은 자리에 있어요.'], no: (k) => ['That is ' + (KS_L[k % 12] || 'a black key') + '. ' + KS_GUIDE[L][0], '그건 ' + (KS_L[k % 12] || '검은건반') + '예요. ' + KS_GUIDE[L][1]] }; },
};

// ══ 3. The staff and clefs ══
const KS_LQ = [['line', 5], ['space', 4]];
KS_SPEC['sf-lines'] = {
  title: ['Five lines, four spaces', '줄 다섯 개, 칸 네 개'], allLine: ['Notes live on five lines and in the four spaces between them. We count from the bottom.', '음표는 다섯 줄 위와 그 사이 네 칸 안에 살아요. 아래에서부터 세어요.'],
  fig: () => ({ staff: <KsLinesFig labels/>, kb: null }),
  steps: [
    { title: ['The lines', '줄'], line: ['Five lines. Line 1 is the bottom one.', '줄은 다섯 개예요. 1번 줄이 맨 아래예요.'], fig: (c) => ({ staff: <KsLinesFig labels hl={{ type: 'line', n: (c.si === 0 ? 1 : 1) }}/> }) },
    { title: ['The spaces', '칸'], line: ['Four spaces. Space 1 is between line 1 and line 2.', '칸은 네 개예요. 1번 칸은 1번 줄과 2번 줄 사이예요.'], fig: () => ({ staff: <KsLinesFig labels hl={{ type: 'space', n: 1 }}/> }) },
  ],
  make: (n) => { const type = n % 2 === 0 ? 'line' : 'space', max = type === 'line' ? 5 : 4, num = 1 + ksRnd(max), what = type === 'line' ? ['line', '줄'] : ['space', '칸'];
    return { kind: 'tap', retry: true, prompt: ['Tap the ' + ksOrd(num) + ' ' + what[0] + ', counting from the bottom.', '아래에서부터 세어서 ' + ksOrd(num) + ' ' + what[1] + '을 눌러 보세요.'],
      fig: (c) => ({ staff: <KsLinesFig onTap={c.pick} pickd={c.pickd} ok={c.res === 'ok'}/> }), ok: (v) => v.type === type && v.n === num,
      yes: ['That is the ' + ksOrd(num) + ' ' + what[0] + '.', '그게 ' + ksOrd(num) + ' ' + what[1] + '이에요.'],
      no: (v) => ['That is ' + (v.type === 'line' ? 'line ' : 'space ') + v.n + '. Count up from the bottom to the ' + ksOrd(num) + ' ' + what[0] + '.', '그건 ' + v.n + '번 ' + (v.type === 'line' ? '줄' : '칸') + '이에요. 아래에서부터 세어서 ' + ksOrd(num) + ' ' + what[1] + '을 찾아보세요.'] }; },
};
const ksPlayDs = (ds, base = 0) => ds.forEach((d, j) => setTimeout(() => playKey(dMidiKey(d), 0.45), j * 380));
const ksHandQ = (clefName, hand, ko) => ({ kind: 'choice', prompt: ['Which hand usually plays the ' + clefName + ' clef’s notes?', clefName === 'treble' ? '높은음자리표의 음은 보통 어느 손으로 칠까요?' : '낮은음자리표의 음은 보통 어느 손으로 칠까요?'], opts: [{ id: 'L', label: () => t('The left hand', '왼손') }, { id: 'R', label: () => t('The right hand', '오른손') }], ans: hand, ok: (v) => v === hand, fig: () => ({}),
  yes: ['The ' + clefName + ' clef is usually the ' + (hand === 'R' ? 'right' : 'left') + ' hand.', ko], no: ['The ' + clefName + ' clef is usually the ' + (hand === 'R' ? 'right' : 'left') + ' hand.', ko] });
KS_SPEC['sf-treble'] = {
  title: ['The treble clef: the Queen', '높은음자리표: 여왕'], allLine: ['The treble clef is the Queen’s. She sings high, and her notes are usually played by the right hand.', '높은음자리표는 여왕의 것이에요. 높은 목소리로 노래하고, 보통 오른손으로 쳐요.'],
  fig: () => ({ staff: ksStaff([32, 33, 34, 35], 'treble'), kb: { oct: 3, base: 0, marks: { 7: 'target', 9: 'target', 11: 'target', 12: 'target' } } }),
  steps: [
    { title: ['High notes, right hand', '높은 음, 오른손'], line: ['The Queen’s notes are on the right side of the piano: the high side.', '여왕의 음은 피아노 오른쪽, 높은 쪽에 있어요.'], fig: () => ({ staff: ksStaff([32, 33, 34, 35], 'treble'), kb: { oct: 3, base: 0, marks: ksSpan(12, 35, 'seg3') } }) },
    { title: ['Her curl wraps round G', '말린 부분은 G를 감싸요'], line: ['The curl of the clef wraps round the second line. That line is G.', '음자리표의 말린 부분은 둘째 줄을 감싸요. 그 줄이 G예요.'], fig: () => ({ staff: ksStaff([32], 'treble', { ring: [0], under: true }), kb: { oct: 3, base: 0, names: { 7: 'G' }, marks: { 7: 'target' } } }) },
  ],
  make: (n) => n % 2 === 0 ? { kind: 'choice', cols: 3, prompt: ['Which line does the treble clef curl round?', '높은음자리표는 어느 줄을 감싸고 있을까요?'], opts: [{ id: '1', label: () => t('Line 1', '1번 줄') }, { id: '2', label: () => t('Line 2', '2번 줄') }, { id: '3', label: () => t('Line 3', '3번 줄') }], ans: '2', ok: (v) => v === '2',
    fig: (c) => ({ staff: ksStaff([32], 'treble', { ring: c.res ? [0] : [], under: !!c.res }) }), yes: ['Line 2: its note is G.', '2번 줄이에요: 그 줄의 음은 G예요.'], no: ['It is line 2: its note is G.', '2번 줄이에요: 그 줄의 음은 G예요.'] }
    : ksHandQ('treble', 'R', '높은음자리표는 보통 오른손이에요.'),
};
KS_SPEC['sf-bass'] = {
  title: ['The bass clef: the King', '낮은음자리표: 왕'], allLine: ['The bass clef is the King’s. He sings low, and his notes are usually played by the left hand.', '낮은음자리표는 왕의 것이에요. 낮은 목소리로 노래하고, 보통 왼손으로 쳐요.'],
  fig: () => ({ staff: ksStaff([22, 23, 24, 25], 'bass'), kb: { oct: 3, base: -12, marks: ksSpan(0, 11, 'seg4') } }),
  steps: [
    { title: ['Low notes, left hand', '낮은 음, 왼손'], line: ['The King’s notes are on the left side of the piano: the low side.', '왕의 음은 피아노 왼쪽, 낮은 쪽에 있어요.'], fig: () => ({ staff: ksStaff([22, 23, 24, 25], 'bass'), kb: { oct: 3, base: -12, marks: ksSpan(0, 11, 'seg4') } }) },
    { title: ['His two dots wrap round F', '두 점은 F를 감싸요'], line: ['The two dots of the clef wrap round the fourth line. That line is F.', '음자리표의 두 점은 넷째 줄을 감싸요. 그 줄이 F예요.'], fig: () => ({ staff: ksStaff([24], 'bass', { ring: [0], under: true }), kb: { oct: 3, base: -12, names: { 5: 'F' }, marks: { 5: 'target' } } }) },
  ],
  make: (n) => n % 2 === 0 ? { kind: 'choice', cols: 3, prompt: ['Which line do the two dots of the bass clef wrap round?', '낮은음자리표의 두 점은 어느 줄을 감싸고 있을까요?'], opts: [{ id: '3', label: () => t('Line 3', '3번 줄') }, { id: '4', label: () => t('Line 4', '4번 줄') }, { id: '5', label: () => t('Line 5', '5번 줄') }], ans: '4', ok: (v) => v === '4',
    fig: (c) => ({ staff: ksStaff([24], 'bass', { ring: c.res ? [0] : [], under: !!c.res }) }), yes: ['Line 4: its note is F.', '4번 줄이에요: 그 줄의 음은 F예요.'], no: ['It is line 4: its note is F.', '4번 줄이에요: 그 줄의 음은 F예요.'] }
    : ksHandQ('bass', 'L', '낮은음자리표는 보통 왼손이에요.'),
};
KS_SPEC['sf-grand'] = {
  title: ['Two staves, two hands', '오선 둘, 손 둘'], allLine: ['Piano music uses two staves together: the treble staff on top for the right hand, the bass staff below for the left hand.', '피아노 악보는 오선 둘을 함께 써요. 위의 높은음자리 오선은 오른손, 아래의 낮은음자리 오선은 왼손이에요.'],
  fig: () => ({ staff: <>{ksStaff([33, 35], 'treble')}{ksStaff([23, 21], 'bass')}</>, kb: { oct: 3, base: -12, marks: ksSpan(0, 11, 'seg4', ksSpan(12, 35, 'seg3')) } }),
  steps: [
    { title: ['Top: the right hand', '위: 오른손'], line: ['The treble staff is on top. The right hand plays the higher keys.', '높은음자리 오선이 위에 있어요. 오른손이 높은 건반을 쳐요.'], fig: () => ({ staff: ksStaff([33, 35], 'treble'), kb: { oct: 3, base: -12, marks: ksSpan(12, 35, 'seg3') } }) },
    { title: ['Bottom: the left hand', '아래: 왼손'], line: ['The bass staff is below. The left hand plays the lower keys.', '낮은음자리 오선이 아래에 있어요. 왼손이 낮은 건반을 쳐요.'], fig: () => ({ staff: ksStaff([23, 21], 'bass'), kb: { oct: 3, base: -12, marks: ksSpan(0, 11, 'seg4') } }) },
  ],
  make: () => { const high = Math.random() < 0.5, k = high ? 15 + ksRnd(18) : 1 + ksRnd(9), ans = high ? 'T' : 'B'; return { kind: 'choice', prompt: ['Listen. Which staff would write this note?', '소리를 들어 보세요. 이 음은 어느 오선에 쓸까요?'], opts: [{ id: 'T', label: () => t('The top staff', '위 오선') }, { id: 'B', label: () => t('The bottom staff', '아래 오선') }], ans, ok: (v) => v === ans,
    play: () => playKey(k - 12, 0.9), fig: (c) => ({ kb: { oct: 3, base: -12, marks: { [k]: c.res ? 'good' : 'pick' } } }),
    yes: [high ? 'It is a high note: the top staff, the right hand.' : 'It is a low note: the bottom staff, the left hand.', high ? '높은 음이라 위 오선, 오른손이에요.' : '낮은 음이라 아래 오선, 왼손이에요.'], no: [high ? 'It is on the right of the piano: high, so the top staff.' : 'It is on the left of the piano: low, so the bottom staff.', high ? '피아노 오른쪽의 높은 음이라 위 오선이에요.' : '피아노 왼쪽의 낮은 음이라 아래 오선이에요.'] }; },
};
KS_SPEC['sf-climb'] = {
  title: ['Higher on the staff, higher on the piano', '오선에서 위로, 피아노에서 오른쪽으로'], allLine: ['A note higher on the staff is a higher sound: its key is further right.', '오선에서 더 위에 있는 음표는 더 높은 소리예요. 그 건반은 더 오른쪽에 있어요.'],
  fig: () => ({ staff: ksStaff([30, 31, 32, 33, 34, 35], 'treble'), kb: { oct: 3, base: 0, marks: { 4: 'target', 5: 'target', 7: 'target', 9: 'target', 11: 'target', 12: 'target' } } }),
  steps: [
    { title: ['Up the staff', '오선 위로'], line: ['Each step up the staff is the next white key to the right.', '오선에서 한 칸씩 올라가면 흰건반은 한 칸씩 오른쪽으로 가요.'], fig: () => ({ staff: ksStaff([32, 33, 34], 'treble'), kb: { oct: 3, base: 0, marks: { 7: 'target', 9: 'target', 11: 'target' } } }) },
    { title: ['Down the staff', '오선 아래로'], line: ['Each step down is the next white key to the left.', '한 칸씩 내려가면 흰건반은 한 칸씩 왼쪽으로 가요.'], fig: () => ({ staff: ksStaff([34, 33, 32], 'treble'), kb: { oct: 3, base: 0, marks: { 7: 'target', 9: 'target', 11: 'target' } } }) },
  ],
  make: () => { let a = 29 + ksRnd(10), b; do { b = 29 + ksRnd(10); } while (b === a); const ans = a > b ? '1' : '2'; return { kind: 'choice', prompt: ['Which note is higher?', '어느 음표가 더 높을까요?'], opts: [{ id: '1', label: () => t('The first', '처음 음표') }, { id: '2', label: () => t('The second', '나중 음표') }], ans, ok: (v) => v === ans, play: () => ksPlayDs([a, b]),
    fig: (c) => ({ staff: ksStaff([a, b], 'treble'), kb: c.res ? { oct: 3, base: 0, marks: { [dMidiKey(a)]: a > b ? 'good' : 'target', [dMidiKey(b)]: b > a ? 'good' : 'target' } } : null }),
    yes: ['The ' + (a > b ? 'first' : 'second') + ' note is higher on the staff, and its key is further right.', (a > b ? '처음' : '나중') + ' 음표가 오선에서 더 위에 있고, 건반도 더 오른쪽이에요.'], no: ['The ' + (a > b ? 'first' : 'second') + ' note is higher on the staff, so it is the higher sound.', (a > b ? '처음' : '나중') + ' 음표가 오선에서 더 위에 있어서 더 높은 소리예요.'] }; },
};

// ══ 4. Line and space names ══
const KS_ST = { treble: { lines: [30, 32, 34, 36, 38], spaces: [31, 33, 35, 37], low: 30, high: 38, rhyme: ['E G B D F: Every Good Boy Deserves Fun', 'E G B D F: Every Good Boy Deserves Fun'], sp: ['F A C E: it spells FACE', 'F A C E: FACE라는 단어가 돼요'] },
  bass: { lines: [18, 20, 22, 24, 26], spaces: [19, 21, 23, 25], low: 18, high: 26, rhyme: ['G B D F A: Great Big Dragon Flies Away', 'G B D F A: Great Big Dragon Flies Away'], sp: ['A C E G: All Cows Eat Grass', 'A C E G: All Cows Eat Grass'] } };
const ksNameLesson = (clef) => { const S = KS_ST[clef], nm = clef === 'treble' ? ['treble', '높은음자리'] : ['bass', '낮은음자리'];
  return {
    title: ['Naming the ' + nm[0] + ' staff', nm[1] + ' 오선의 이름'], allLine: ['Every line and space has a letter. Learn the lines, then the spaces.', '줄과 칸에는 모두 글자가 있어요. 줄을 먼저, 그다음 칸을 배워요.'],
    fig: () => ({ staff: ksStaff([...S.lines, ...S.spaces].sort((a, b) => a - b), clef, { under: true }) }),
    steps: [
      { title: ['The lines', '줄'], line: [S.rhyme[0], S.rhyme[1]], fig: () => ({ staff: ksStaff(S.lines, clef, { under: true }) }) },
      { title: ['The spaces', '칸'], line: [S.sp[0], S.sp[1]], fig: () => ({ staff: ksStaff(S.spaces, clef, { under: true }) }) },
    ],
    make: () => { const d = ksPick([...S.lines, ...S.spaces]), L = ksLetter(d), isLine = S.lines.includes(d), n = isLine ? S.lines.indexOf(d) + 1 : S.spaces.indexOf(d) + 1;
      return { kind: 'choice', cols: 4, prompt: ['What is the name of this note?', '이 음표의 이름은?'], opts: ksLet7(), ans: L, ok: (v) => v === L, fig: (c) => ({ staff: ksStaff([d], clef, { ring: [0], under: c.res ? true : null }) }),
        yes: [L + ': ' + (isLine ? 'line ' : 'space ') + n + '. ' + (isLine ? S.rhyme[0] : S.sp[0]), L + ': ' + n + '번 ' + (isLine ? '줄' : '칸') + '. ' + (isLine ? S.rhyme[1] : S.sp[1])],
        no: [L + ': it is on ' + (isLine ? 'line ' : 'space ') + n + '. ' + (isLine ? S.rhyme[0] : S.sp[0]), L + '예요: ' + n + '번 ' + (isLine ? '줄' : '칸') + '에 있어요. ' + (isLine ? S.rhyme[1] : S.sp[1])] }; },
  }; };
KS_SPEC['ws-treble'] = ksNameLesson('treble');
KS_SPEC['ws-bass'] = ksNameLesson('bass');
const KS_HOP = [{ d: 21, n: ['bass C', '낮은음자리표 도'], c: 'bass' }, { d: 24, n: ['the King’s F', '왕의 F'], c: 'bass' }, { d: 28, n: ['middle C', '가운데 도'], c: 'treble' }, { d: 32, n: ['the Queen’s G', '여왕의 G'], c: 'treble' }, { d: 35, n: ['treble C', '높은음자리표 도'], c: 'treble' }];
KS_SPEC['ws-landmarks'] = {
  title: ['Five landmarks', '기준 음 다섯 개'], allLine: ['Five notes are easy to remember. They are your landmarks on the staves.', '기억하기 쉬운 음 다섯 개가 있어요. 오선 위의 기준점이에요.'],
  fig: () => ({ staff: <>{ksStaff([28, 32, 35], 'treble', { under: true })}{ksStaff([21, 24], 'bass', { under: true })}</> }),
  steps: [
    { title: ['The Queen’s G and treble C', '여왕의 G와 높은음자리표 도'], line: ['The Queen’s G is on line 2. Treble C is in space 3.', '여왕의 G는 2번 줄에 있어요. 높은음자리표 도는 3번 칸에 있어요.'], fig: () => ({ staff: ksStaff([32, 35], 'treble', { under: true }) }) },
    { title: ['The King’s F and bass C', '왕의 F와 낮은음자리표 도'], line: ['The King’s F is on line 4. Bass C is in space 2.', '왕의 F는 4번 줄에 있어요. 낮은음자리표 도는 2번 칸에 있어요.'], fig: () => ({ staff: ksStaff([24, 21], 'bass', { under: true }) }) },
    { title: ['Middle C', '가운데 도'], line: ['Middle C sits between the staves, on its own short line below the treble staff.', '가운데 도는 두 오선 사이에 있어요. 높은음자리 오선 아래의 짧은 줄 위에 앉아요.'], fig: () => ({ staff: ksStaff([28], 'treble', { under: true }) }) },
  ],
  make: (n, prev) => { let H; do { H = ksPick(KS_HOP); } while (prev && prev.H === H); return { H, kind: 'choice', cols: 1, prompt: ['Which landmark is this?', '어느 기준 음일까요?'], opts: KS_HOP.map(x => ({ id: String(x.d), label: () => t(x.n[0], x.n[1]) })), ans: String(H.d), ok: (v) => v === String(H.d),
    fig: () => ({ staff: ksStaff([H.d], H.c, { ring: [0] }) }), yes: [H.n[0] + '.', H.n[1] + '이에요.'], no: ['It is ' + H.n[0] + '.', H.n[1] + '이에요.'] }; },
};
KS_SPEC['ws-count'] = {
  title: ['Count from a landmark', '기준 음에서 세기'], allLine: ['To name any note, start at the nearest landmark and count steps. Each line or space is one step.', '어떤 음이든 가장 가까운 기준 음에서 한 칸씩 세어요. 줄이나 칸 하나가 한 걸음이에요.'],
  fig: () => ({ staff: ksStaff([32, 33, 34], 'treble', { under: true, ring: [0] }) }),
  steps: [
    { title: ['One step up', '한 걸음 위로'], line: ['From the Queen’s G, one step up is A.', '여왕의 G에서 한 걸음 위는 A예요.'], fig: () => ({ staff: ksStaff([32, 33], 'treble', { under: true, ring: [1] }) }) },
    { title: ['One step down', '한 걸음 아래로'], line: ['From the Queen’s G, one step down is F.', '여왕의 G에서 한 걸음 아래는 F예요.'], fig: () => ({ staff: ksStaff([32, 31], 'treble', { under: true, ring: [1] }) }) },
  ],
  make: () => { const H = ksPick(KS_HOP.filter(x => x.d !== 28)), off = ksPick([-2, -1, 1, 2]), d = H.d + off, L = ksLetter(d); return { kind: 'choice', cols: 4, prompt: ['Start at ' + H.n[0] + ' (the ringed note). What is the other note?', H.n[1] + '(동그라미 친 음)에서 시작해요. 다른 음표의 이름은?'], opts: ksLet7(), ans: L, ok: (v) => v === L,
    fig: (c) => ({ staff: ksStaff([H.d, d], H.c, { ring: [0], under: c.res ? true : [0] }) }),
    yes: [L + ': ' + Math.abs(off) + (Math.abs(off) === 1 ? ' step ' : ' steps ') + (off > 0 ? 'up' : 'down') + ' from ' + ksLetter(H.d) + '.', L + '예요: ' + ksLetter(H.d) + '에서 ' + Math.abs(off) + '걸음 ' + (off > 0 ? '위' : '아래') + '예요.'],
    no: ['Count ' + Math.abs(off) + (Math.abs(off) === 1 ? ' step ' : ' steps ') + (off > 0 ? 'up' : 'down') + ' from ' + ksLetter(H.d) + ': ' + L + '.', ksLetter(H.d) + '에서 ' + Math.abs(off) + '걸음 ' + (off > 0 ? '위' : '아래') + '로 세면 ' + L + '이에요.'] }; },
};
KS_SPEC['ws-read'] = {
  title: ['Read it, play it', '읽고 치기'], allLine: ['Read the note on the staff, then find its key. Tap the keys to hear them.', '오선의 음표를 읽고 그 건반을 찾아요. 건반을 눌러 소리를 들어 보세요.'],
  fig: () => ({ staff: ksStaff([32], 'treble', { under: true }), kb: { oct: 3, base: 0, names: ksNames(3), marks: { 7: 'target' } } }),
  steps: [
    { title: ['Treble: the right hand', '높은음자리: 오른손'], line: ['The Queen’s G is the G above middle C.', '여왕의 G는 가운데 도 위의 G예요.'], fig: () => ({ staff: ksStaff([32], 'treble', { under: true }), kb: { oct: 3, base: 0, names: ksNames(3), marks: { 7: 'target' } } }) },
    { title: ['Bass: the left hand', '낮은음자리: 왼손'], line: ['The King’s F is the F below middle C.', '왕의 F는 가운데 도 아래의 F예요.'], fig: () => ({ staff: ksStaff([24], 'bass', { under: true }), kb: { oct: 3, base: -12, names: ksNames(3), marks: { 5: 'target' } } }) },
  ],
  make: () => { const treble = Math.random() < 0.5, d = treble ? ksPick(KS_ST.treble.lines.concat(KS_ST.treble.spaces, [28, 39])) : ksPick(KS_ST.bass.lines.concat(KS_ST.bass.spaces, [27])), base = treble ? 0 : -12, tk = dMidiKey(d) - base, clef = treble ? 'treble' : 'bass';
    return { kind: 'key', retry: true, prompt: ['Tap the key for this note.', '이 음표의 건반을 눌러 보세요.'], fig: () => ({ staff: ksStaff([d], clef), kb: { oct: 3, base } }), ok: (k) => k === tk, onPick: (k, ok) => { if (ok) playKey(dMidiKey(d), 0.6); },
      yes: ['That is ' + ksLetter(d) + '.', '그 건반은 ' + ksLetter(d) + '예요.'], no: (k) => KS_L[((k % 12) + 12) % 12] === ksLetter(d) ? ['That is the right letter, but another ' + ksLetter(d) + '. Look at which octave the note is in.', '글자는 맞지만 다른 ' + ksLetter(d) + '예요. 음표가 어느 옥타브에 있는지 보세요.'] : ['That key is ' + (KS_L[((k % 12) + 12) % 12] || 'a black key') + '. This note is ' + ksLetter(d) + ': ' + (treble ? 'count from the Queen’s G.' : 'count from the King’s F.'), '그 건반은 ' + (KS_L[((k % 12) + 12) % 12] || '검은건반') + '이에요. 이 음은 ' + ksLetter(d) + '예요: ' + (treble ? '여왕의 G에서 세어 보세요.' : '왕의 F에서 세어 보세요.')] }; },
};

// ══ 5. Ledger lines and 8va ══
const ksLedgerLesson = (o) => ({
  title: o.title, allLine: o.all,
  fig: () => ({ staff: ksStaff(o.show, o.clef, { under: true }) }),
  steps: o.steps.map(s => ({ title: s[0], line: s[1], fig: () => ({ staff: ksStaff(s[2], o.clef, { under: true, ring: s[3] || [] }) }) })),
  make: () => { const d = ksPick(o.ask), L = ksLetter(d); return { kind: 'choice', cols: 4, prompt: ['What is the name of this note?', '이 음표의 이름은?'], opts: ksLet7(), ans: L, ok: (v) => v === L, fig: (c) => ({ staff: ksStaff([d], o.clef, { ring: [0], under: c.res ? true : null }) }),
    yes: [L + '. ' + o.hint[0], L + '예요. ' + o.hint[1]], no: [L + '. ' + o.hint[0], L + '예요. ' + o.hint[1]] }; },
});
KS_SPEC['ll-above'] = ksLedgerLesson({ clef: 'treble', title: ['Above the staff', '오선 위로'], all: ['When a note is higher than the five lines, it sits on a short extra line: a ledger line.', '음이 다섯 줄보다 높으면 짧은 덧줄 위에 앉아요.'], show: [38, 39, 40, 41, 42], ask: [39, 40, 41, 42, 43], hint: ['Count up from the top line, F: G is the space above, then A on the first ledger line.', '맨 윗줄 F에서 위로 세어요: 위의 칸이 G, 첫 덧줄이 A예요.'],
  steps: [[['The first ledger line', '첫 번째 덧줄'], ['Above the top line F comes the space G, then the first ledger line: A.', '맨 윗줄 F 위에는 G 칸이 있고, 그 위 첫 덧줄이 A예요.'], [38, 39, 40], [2]], [['More steps up', '더 위로'], ['Keep counting: B in the space, then C on the second ledger line.', '계속 세어요: 칸의 B, 두 번째 덧줄의 C.'], [40, 41, 42], [2]]] });
KS_SPEC['ll-below'] = ksLedgerLesson({ clef: 'bass', title: ['Below the staff', '오선 아래로'], all: ['Notes lower than the five lines use ledger lines too, below the staff.', '다섯 줄보다 낮은 음도 오선 아래의 덧줄을 써요.'], show: [18, 17, 16, 15, 14], ask: [17, 16, 15, 14], hint: ['Count down from the bottom line, G: F is the space below, then E on the first ledger line.', '맨 아랫줄 G에서 아래로 세어요: 아래 칸이 F, 첫 덧줄이 E예요.'],
  steps: [[['The first ledger line', '첫 번째 덧줄'], ['Below the bottom line G comes the space F, then the first ledger line: E.', '맨 아랫줄 G 아래에는 F 칸이 있고, 그 아래 첫 덧줄이 E예요.'], [18, 17, 16], [2]], [['More steps down', '더 아래로'], ['Keep counting down: D in the space, then C on the second ledger line.', '계속 내려가요: 칸의 D, 두 번째 덧줄의 C.'], [16, 15, 14], [2]]] });
KS_SPEC['ll-middle'] = {
  title: ['Middle C, written two ways', '가운데 도, 두 가지 표기'], allLine: ['Middle C is one key, but it can be written on a ledger line under the treble staff or above the bass staff.', '가운데 도는 건반 하나지만, 높은음자리 오선 아래 덧줄에도, 낮은음자리 오선 위 덧줄에도 쓸 수 있어요.'],
  fig: () => ({ staff: <>{ksStaff([28], 'treble')}{ksStaff([28], 'bass')}</>, kb: { oct: 3, base: -12, names: { 12: 'C' }, marks: { 12: 'target' } } }),
  steps: [
    { title: ['Under the treble staff', '높은음자리 오선 아래'], line: ['One short line below the treble staff: middle C.', '높은음자리 오선 아래 짧은 줄 하나: 가운데 도예요.'], fig: () => ({ staff: ksStaff([28], 'treble'), kb: { oct: 3, base: -12, names: { 12: 'C' }, marks: { 12: 'target' } } }) },
    { title: ['Above the bass staff', '낮은음자리 오선 위'], line: ['One short line above the bass staff: the same key, middle C.', '낮은음자리 오선 위 짧은 줄 하나: 같은 건반, 가운데 도예요.'], fig: () => ({ staff: ksStaff([28], 'bass'), kb: { oct: 3, base: -12, names: { 12: 'C' }, marks: { 12: 'target' } } }) },
  ],
  make: () => { const treble = Math.random() < 0.5, d = treble ? ksPick([26, 27, 28, 29]) : ksPick([26, 27, 28, 29]), clef = treble ? 'treble' : 'bass', tk = dMidiKey(d) + 12;
    return { kind: 'key', retry: true, prompt: ['Tap the key for this note near middle C.', '가운데 도 근처의 이 음표의 건반을 눌러 보세요.'], fig: () => ({ staff: ksStaff([d], clef), kb: { oct: 3, base: -12, names: { 12: 'C' } } }), ok: (k) => k === tk, onPick: (k, ok) => { if (ok) playKey(dMidiKey(d), 0.6); },
      yes: ['That is ' + ksLetter(d) + '.', '그 건반은 ' + ksLetter(d) + '예요.'], no: (k) => KS_L[((k % 12) + 12) % 12] === ksLetter(d) ? ['That is the right letter, but another ' + ksLetter(d) + '. Look for the one nearest middle C.', '글자는 맞지만 다른 ' + ksLetter(d) + '예요. 가운데 도에서 가장 가까운 것을 찾아보세요.'] : ['That key is ' + (KS_L[((k % 12) + 12) % 12] || 'a black key') + '. This note is ' + ksLetter(d) + ': count from middle C, which is on the ledger line.', '그 건반은 ' + (KS_L[((k % 12) + 12) % 12] || '검은건반') + '이에요. 이 음은 ' + ksLetter(d) + '예요: 덧줄 위의 가운데 도에서 세어 보세요.'] }; },
};
KS_SPEC['ll-8va'] = {
  title: ['8va: an octave higher', '8va: 한 옥타브 높게'], allLine: ['When notes are very high, 8va above them means: play one octave higher than written.', '음이 아주 높으면 위에 8va를 써요. 쓴 것보다 한 옥타브 높게 치라는 뜻이에요.'],
  fig: () => ({ staff: ksStaff([38, 39, 40, 41], 'treble', { bracket: { from: 0, bar: 0, label: '8va' } }), kb: { oct: 3, base: 0, marks: { 17: 'pass', 19: 'pass', 21: 'pass', 23: 'pass', 29: 'good', 31: 'good', 33: 'good', 35: 'good' } } }),
  steps: [
    { title: ['What is written', '쓴 그대로'], line: ['Without 8va, these notes are played where they are written.', '8va가 없으면 쓴 위치 그대로 쳐요.'], fig: () => ({ staff: ksStaff([38, 39, 40, 41], 'treble'), kb: { oct: 3, base: 0, marks: { 17: 'good', 19: 'good', 21: 'good', 23: 'good' } } }) },
    { title: ['With 8va', '8va가 있으면'], line: ['With 8va, play the same letters one octave higher.', '8va가 있으면 같은 글자를 한 옥타브 높은 곳에서 쳐요.'], fig: () => ({ staff: ksStaff([38, 39, 40, 41], 'treble', { bracket: { from: 0, bar: 0, label: '8va' } }), kb: { oct: 3, base: 0, marks: { 17: 'pass', 19: 'pass', 21: 'pass', 23: 'pass', 29: 'good', 31: 'good', 33: 'good', 35: 'good' } } }) },
  ],
  make: () => { const d = ksPick([38, 39, 40, 41]), tk = dMidiKey(d) + 12; return { kind: 'key', retry: true, prompt: ['This note has 8va above it. Tap the key you play.', '이 음표 위에 8va가 있어요. 실제로 치는 건반을 눌러 보세요.'], fig: () => ({ staff: ksStaff([d, d], 'treble', { bracket: { from: 0, bar: 0, label: '8va' } }), kb: { oct: 3, base: 0 } }), ok: (k) => k === tk, onPick: (k, ok) => { if (ok) playKey(tk, 0.6); },
    yes: ['That is ' + ksLetter(d) + ' one octave higher than written.', '쓴 것보다 한 옥타브 높은 ' + ksLetter(d) + '예요.'], no: (k) => ['Not that one. Find the written ' + ksLetter(d) + ', then play the next ' + ksLetter(d) + ' to the right.', '그 건반이 아니에요. 쓴 ' + ksLetter(d) + '를 찾고, 오른쪽의 다음 ' + ksLetter(d) + '를 치세요.'] }; },
};

// ══ 6. Pitch and range ══
const ksBars = ({ lens, hl, onTap, pickd }) => <svg viewBox="0 0 320 120" style={{ width: '100%', maxWidth: 340, display: 'block', margin: '0 auto' }}>
  {lens.map((h, i) => { const x = 20 + i * (280 / lens.length) + 4, w = 280 / lens.length - 8, on = hl === i, pk = pickd === i; return <g key={i} onClick={() => onTap && onTap(i)} style={{ cursor: onTap ? 'pointer' : 'default' }}>
    <rect x={x} y={14} width={w} height={h} rx="6" fill={pk ? '#fad0c2' : on ? '#fbe3da' : '#fffefa'} stroke={on || pk ? '#e4572e' : '#26296b'} strokeWidth="3"/></g>; })}
</svg>;
const KS_XY = [0, 2, 4, 5, 7, 9, 11, 12];
KS_SPEC['sr-size'] = {
  title: ['Long is low, short is high', '긴 것은 낮게, 짧은 것은 높게'], allLine: ['Tap the bars. The long bar sounds low and the short bar sounds high.', '막대를 눌러 보세요. 긴 막대는 낮은 소리, 짧은 막대는 높은 소리가 나요.'],
  fig: (c) => ({ top: ksBars({ lens: [100, 92, 84, 78, 70, 62, 54, 46], hl: c.last, onTap: (i) => { playKey(KS_XY[i], 0.7); c.setLast(i); } }) }),
  steps: [
    { title: ['The longest bar', '가장 긴 막대'], line: ['The longest bar has the lowest sound.', '가장 긴 막대가 가장 낮은 소리를 내요.'], fig: (c) => ({ top: ksBars({ lens: [100, 92, 84, 78, 70, 62, 54, 46], hl: 0, onTap: (i) => { playKey(KS_XY[i], 0.7); } }) }) },
    { title: ['The shortest bar', '가장 짧은 막대'], line: ['The shortest bar has the highest sound.', '가장 짧은 막대가 가장 높은 소리를 내요.'], fig: () => ({ top: ksBars({ lens: [100, 92, 84, 78, 70, 62, 54, 46], hl: 7, onTap: (i) => { playKey(KS_XY[i], 0.7); } }) }) },
  ],
  make: () => { const a = 30 + ksRnd(60), b = a + ksPick([-1, 1]) * (15 + ksRnd(30)), lens = [a, b], low = a > b ? 0 : 1; return { kind: 'tap', retry: true, prompt: ['Tap the bar that sounds lower.', '더 낮은 소리가 나는 막대를 눌러 보세요.'], fig: (c) => ({ top: ksBars({ lens, onTap: (i) => { playKey(i === low ? 0 : 12, 0.7); c.pick(i); }, pickd: c.pickd }) }), ok: (i) => i === low,
    yes: ['The longer bar sounds lower.', '더 긴 막대가 더 낮은 소리를 내요.'], no: ['That bar is shorter, so it sounds higher. The longer bar sounds lower.', '그 막대는 더 짧아서 더 높은 소리가 나요. 더 긴 막대가 더 낮은 소리를 내요.'] }; },
};
const KS_PIANO = 'Piano (today, 88 keys)', KS_RNG = [KS_PIANO, 'Violin', 'Cello', 'Flute', 'Tuba', 'Soprano', 'Bass'];
const ksRangeFig = (name, c) => { const R = SPR_RANGE(name); return { top: <div style={{ maxWidth: 520, margin: '0 auto' }}><SprStrip range={[R.lo, R.hi]}/></div>,
  mid: <div style={{ display: 'flex', flexWrap: 'wrap', gap: 6, justifyContent: 'center', margin: '8px 0 0' }}>{KS_RNG.map(n => <button key={n} className={'chip' + (n === name ? ' active' : '')} style={{ padding: '6px 12px', minHeight: 40 }} onClick={() => { const r = SPR_RANGE(n); sprPiano(r.lo); sprPiano(r.hi, 0.95); c.setLast(n); }}>{rangeName(n)}</button>)}</div> }; };
KS_SPEC['sr-range'] = {
  title: ['How far a piano reaches', '피아노가 닿는 범위'], allLine: ['A piano covers a very wide range of sounds. Other instruments and voices cover part of it. Tap a name to see and hear its range.', '피아노는 아주 넓은 범위의 소리를 내요. 다른 악기와 목소리는 그중 일부를 맡아요. 이름을 눌러 범위를 보고 들어 보세요.'],
  fig: (c) => ksRangeFig(c.last || KS_PIANO, c),
  steps: [
    { title: ['The piano: 88 keys', '피아노: 건반 88개'], line: ['The piano goes from A0 at the far left to C8 at the far right.', '피아노는 맨 왼쪽 A0에서 맨 오른쪽 C8까지 닿아요.'], fig: (c) => ksRangeFig(KS_PIANO, c) },
    { title: ['Other ranges', '다른 음역'], line: ['A violin, a cello and a voice each cover only part of the piano’s range.', '바이올린, 첼로, 목소리는 각각 피아노 범위의 일부만 맡아요.'], fig: (c) => ksRangeFig(c.last && c.last !== KS_PIANO ? c.last : 'Violin', c) },
  ],
  make: () => { let a, b; do { a = ksPick(KS_RNG.slice(1)); b = ksPick(KS_RNG.slice(1)); } while (a === b || SPR_RANGE(a).lo === SPR_RANGE(b).lo); const low = SPR_RANGE(a).lo < SPR_RANGE(b).lo ? a : b; return { kind: 'choice', prompt: ['Which one reaches lower?', '어느 쪽이 더 낮은 음까지 내려갈까요?'], opts: [a, b].map(n => ({ id: n, label: () => rangeName(n) })), ans: low, ok: (v) => v === low,
    fig: (c) => ({ top: <div style={{ maxWidth: 520, margin: '0 auto' }}><SprStrip range={c.res ? [SPR_RANGE(low).lo, SPR_RANGE(low).hi] : null}/></div> }), play: () => { sprPiano(SPR_RANGE(a).lo); sprPiano(SPR_RANGE(b).lo, 0.95); },
    yes: ['The ' + rangeName(low) + ' starts lower.', rangeName(low) + '이(가) 더 낮은 데서 시작해요.'], no: ['The ' + rangeName(low) + ' starts lower.', rangeName(low) + '이(가) 더 낮은 데서 시작해요.'] }; },
};

// registry: her six sections, each lesson one idea
const KS_ROWS = [
  ['p-keys', [
    ['kp-groups', 'Black keys in twos and threes', '검은건반은 두 개, 세 개씩', 'The black keys sit in groups of 2 and 3.', '검은건반은 두 개, 세 개씩 모여 있어요.', () => <KpGroups/>],
    ['kp-repeat', 'The pattern repeats', '같은 무늬가 되풀이돼요', 'Every 12 keys the same pattern starts again, on C.', '건반 12개마다 같은 무늬가 C에서 다시 시작해요.', () => <KsEngine spec={KS_SPEC['kp-repeat']}/>],
    ['kp-middle', 'Middle C', '가운데 도', 'The C in the middle of the keyboard.', '건반 한가운데 있는 C.', () => <KsEngine spec={KS_SPEC['kp-middle']}/>],
    ['kp-hear', 'Low and high', '낮은 소리, 높은 소리', 'Left is low, right is high.', '왼쪽은 낮은 소리, 오른쪽은 높은 소리.', () => <KsEngine spec={KS_SPEC['kp-hear']}/>],
  ]],
  ['p-names', [
    ['nn-letters', 'Seven letters', '글자는 일곱 개', 'A B C D E F G, and then again.', 'A B C D E F G, 그리고 다시.', () => <KsEngine spec={KS_SPEC['nn-letters']}/>],
    ['nn-houses', 'The white keys by house', '집으로 흰건반 찾기', 'Where each white key lives in its house.', '흰건반이 집 안 어디에 사는지.', () => <KsEngine spec={KS_SPEC['nn-houses']}/>],
    ['nn-updown', 'Right is next, left is back', '오른쪽은 다음, 왼쪽은 앞', 'One white key right is the next letter.', '흰건반 하나 오른쪽은 다음 글자.', () => <KsEngine spec={KS_SPEC['nn-updown']}/>],
    ['nn-find', 'Every key with the same name', '이름이 같은 건반 모두 찾기', 'The same letter in every pattern.', '무늬마다 있는 같은 글자.', () => <KsEngine spec={KS_SPEC['nn-find']}/>],
  ]],
  ['p-stf', [
    ['sf-lines', 'Five lines, four spaces', '줄 다섯 개, 칸 네 개', 'Counting the lines and spaces from the bottom.', '아래에서부터 줄과 칸 세기.', () => <KsEngine spec={KS_SPEC['sf-lines']}/>],
    ['sf-treble', 'The treble clef: the Queen', '높은음자리표: 여왕', 'High notes, the right hand, and the curl round G.', '높은 음, 오른손, G를 감싸는 말림.', () => <KsEngine spec={KS_SPEC['sf-treble']}/>],
    ['sf-bass', 'The bass clef: the King', '낮은음자리표: 왕', 'Low notes, the left hand, and the dots round F.', '낮은 음, 왼손, F를 감싸는 두 점.', () => <KsEngine spec={KS_SPEC['sf-bass']}/>],
    ['sf-grand', 'Two staves, two hands', '오선 둘, 손 둘', 'The treble staff above, the bass staff below.', '위의 높은음자리 오선, 아래의 낮은음자리 오선.', () => <KsEngine spec={KS_SPEC['sf-grand']}/>],
    ['sf-climb', 'Higher on the staff, higher on the piano', '오선에서 위로, 피아노에서 오른쪽으로', 'Up the staff is up the keys.', '오선 위쪽은 건반 오른쪽.', () => <KsEngine spec={KS_SPEC['sf-climb']}/>],
  ]],
  ['p-lines', [
    ['ws-treble', 'Naming the treble staff', '높은음자리 오선의 이름', 'E G B D F on the lines, F A C E in the spaces.', '줄은 E G B D F, 칸은 F A C E.', () => <KsEngine spec={KS_SPEC['ws-treble']}/>],
    ['ws-bass', 'Naming the bass staff', '낮은음자리 오선의 이름', 'G B D F A on the lines, A C E G in the spaces.', '줄은 G B D F A, 칸은 A C E G.', () => <KsEngine spec={KS_SPEC['ws-bass']}/>],
    ['ws-landmarks', 'Five landmarks', '기준 음 다섯 개', 'Five notes that are easy to remember.', '기억하기 쉬운 음 다섯 개.', () => <KsEngine spec={KS_SPEC['ws-landmarks']}/>],
    ['ws-count', 'Count from a landmark', '기준 음에서 세기', 'Name any note by counting steps.', '걸음을 세어 어떤 음이든 이름 붙이기.', () => <KsEngine spec={KS_SPEC['ws-count']}/>],
    ['ws-read', 'Read it, play it', '읽고 치기', 'From the note on the staff to its key.', '오선의 음표에서 그 건반까지.', () => <KsEngine spec={KS_SPEC['ws-read']}/>],
  ]],
  ['p-ledger', [
    ['ll-above', 'Above the staff', '오선 위로', 'Ledger lines above the staff.', '오선 위의 덧줄.', () => <KsEngine spec={KS_SPEC['ll-above']}/>],
    ['ll-below', 'Below the staff', '오선 아래로', 'Ledger lines below the staff.', '오선 아래의 덧줄.', () => <KsEngine spec={KS_SPEC['ll-below']}/>],
    ['ll-middle', 'Middle C, written two ways', '가운데 도, 두 가지 표기', 'One key, two places on the page.', '건반 하나, 악보 위 두 자리.', () => <KsEngine spec={KS_SPEC['ll-middle']}/>],
    ['ll-8va', '8va: an octave higher', '8va: 한 옥타브 높게', 'Play one octave higher than written.', '쓴 것보다 한 옥타브 높게 치기.', () => <KsEngine spec={KS_SPEC['ll-8va']}/>],
  ]],
  ['p-range', [
    ['sr-size', 'Long is low, short is high', '긴 것은 낮게, 짧은 것은 높게', 'Long bars sound low, short bars sound high.', '긴 막대는 낮은 소리, 짧은 막대는 높은 소리.', () => <KsEngine spec={KS_SPEC['sr-size']}/>],
    ['sr-range', 'How far a piano reaches', '피아노가 닿는 범위', 'The piano’s range next to other instruments.', '다른 악기와 비교한 피아노의 범위.', () => <KsEngine spec={KS_SPEC['sr-range']}/>],
  ]],
];
