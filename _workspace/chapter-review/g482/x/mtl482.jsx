// ─── Phase 482: the timeline of music (chapters 26 and 27 share it). One x axis, 1600 to today; its rows: the periods,
// the keyboards of each time, the composers' lives, the sound of each period, and the styles beside them. Each chapter
// draws its own rows strongly (26: the composers; 27: the sound and the styles) and the other rows lightly. Coral is the
// one thing being looked at: a selected period or composer, or the line down from one year.
// Facts: the periods and the composers' years are Phases 304-305's (CMP_PERIODS, CMP; checked then). The keyboards:
// chapter 18's (Cristofori's piano about 1700; the fortepiano of Mozart's time, the 1770s; the piano from about 1830, as
// the iron frame came in, 1825-1859). The styles: ragtime 1890s-1910s (Maple Leaf Rag 1899); blues from the late 1800s;
// jazz from the 1910s (its first record 1917); rock and roll from the late 1940s and early 1950s (Library of Congress;
// Wikipedia, checked 2026-10-17).
const MTL_NOW = 2026;
const MTL_ERAS = ['baroque', 'classical', 'romantic', 'modern', 'contemporary'];
const mtlYears = (id) => CMP_PERIODS[id].years;
const MTL_KEYS = [[1600, 1770, 'harpsichord', '하프시코드'], [1770, 1830, 'fortepiano', '포르테피아노'], [1830, MTL_NOW, 'piano', '피아노']];
const MTL_SOUND = { baroque: ['counterpoint', '대위법'], classical: ['a clear tune', '또렷한 선율'], romantic: ['big feelings', '풍부한 감정'], modern: ['new sounds', '새로운 소리'], contemporary: ['anything goes', '무엇이든 가능'] };
const MTL_STYLES = [[1890, MTL_NOW, 'blues', '블루스', 0], [1895, 1920, 'ragtime', '래그타임', 1], [1950, MTL_NOW, 'rock and pop', '록과 팝', 1], [1915, MTL_NOW, 'jazz', '재즈', 2]];
const MTL_ROW_W = { era: ['periods', '시대'], keys: ['keyboards', '건반 악기'], cmp: ['composers', '작곡가'], sound: ['sound', '소리'], style: ['styles', '스타일'], draw: ['my composers', '나의 작곡가'] };
const mtlEraOf = (y) => MTL_ERAS.find(id => y >= mtlYears(id)[0] && y < mtlYears(id)[1]) || (y < 1600 ? null : 'contemporary');
const mtlEnd = (c) => c.died || MTL_NOW;
const mtlSur = (c) => t(c.sur[0], c.sur[1]);
// Korean writes a range with ~ (kept to the number after it)
const mtlLife = (c) => c.died ? (c.bornApprox ? t('c. ', '약 ') : '') + c.born + t('–⁠', '~⁠') + c.died : t('born ' + c.born, c.born + '년 출생');
// alive in a year: born before it and died after it (the years of birth and death themselves are left out of every question)
const mtlAlive = (c, y) => c.born < y && mtlEnd(c) > y;
// the width of a bold label: Hangul about a square each, the rest about 0.61 of the size
const mtlTw = (s, f) => [...String(s)].reduce((w, ch) => w + (/[가-힣]/.test(ch) ? 0.98 : 0.61), 0) * f;

// lanes: each composer in the first lane whose last bar (and its name) ends before this one begins.
// one: a lane each (in order of birth); big: the years inside the bar too. A name goes inside the bar, after it, or
// (at the right edge) before it, never outside [xMin, xMax]; where none fits, the surname alone.
function mtlLanes(cs, X, f, one, sur = mtlSur, life = mtlLife, xMax = 9999, big = one, xMin = -9999) {
  const lanes = [], out = [];
  [...cs].sort((a, b) => a.born - b.born).forEach(c => {
    const x0 = X(c.born), x1 = X(mtlEnd(c)), tip = c.died ? 0 : 7;
    let name = big ? sur(c) + ' ' + life(c) : sur(c), tw = mtlTw(name, f), inside = big && x1 - x0 >= tw + 12;
    const fitsR = (w) => x1 + tip + 4 + w <= xMax + 2, fitsL = (w) => x0 - 4 - w >= xMin;
    if (big && !inside && !fitsR(tw) && !fitsL(tw)) { name = sur(c); tw = mtlTw(name, f); inside = x1 - x0 >= tw + 12; }
    const left = !inside && !fitsR(tw) && fitsL(tw), s0 = left ? x0 - 4 - tw : x0, end = inside || left ? x1 + tip : x1 + tip + 4 + tw;
    let k = one ? lanes.length : lanes.findIndex(e => e < s0 - 14);
    if (k < 0) k = lanes.length;
    lanes[k] = end; out.push({ c, k, x0, x1, name, inside, left, tip });
  });
  return { n: lanes.length, bars: out };
}

// MusTimeline: from/to the years shown; rows in order; focus the rows drawn strongly; ids the composers; sel {kind, id};
// year a line down from one year; lit composers drawn coral; onTap(kind, id) makes the periods and composers (tapKinds)
// buttons. stack: a lane per composer; big: their years inside the bars; fs, laneH, barH: the sizes; guides: the period
// boundaries drawn faintly through the composers; en: English whatever the language (the Workbook).
function MusTimeline({ from = 1600, to = MTL_NOW, rows = ['era', 'keys', 'cmp', 'sound', 'style'], focus = ['cmp'], ids = CPX_IDS, sel, year, lit = [], onTap, tapKinds = ['era', 'cmp'], big, W = 680, label, rowLabels = true, step, firstPiano, en, stack, fs, laneH, barH, guides, hiEra }) {
  const T = en ? (a) => a : t, ko = LANG === 'ko' && !en, sur = (c) => en ? c.sur[0] : mtlSur(c), life = (c) => en ? (c.died ? (c.bornApprox ? 'c. ' : '') + c.born + '–' + c.died : 'born ' + c.born) : mtlLife(c);
  const eraNm = (id) => en ? CMP_PERIODS[id].name[0].replace(/ \(.*\)$/, '') : cmpEraTag(id), ital = ko ? 'normal' : 'italic';
  const f = fs || (big ? 11.5 : 9.5), LW = rowLabels ? (ko ? 62 : 74) * f / 9.5 + (rows.includes('draw') ? 14 : 0) : 0, x0 = LW + 8, x1 = W - 10;
  const X = (y) => x0 + (Math.max(from, Math.min(to, y)) - from) / (to - from) * (x1 - x0);
  const cs = ids.map(cmpById).filter(Boolean);
  const L = mtlLanes(cs, X, f, !!(big || stack), sur, life, x1, !!big, x0 - 2), on = (r) => focus.includes(r);
  const sw = (r) => on(r) ? PEN_N : 'rgba(38,41,107,0.45)', fillOf = (r) => on(r) ? 'rgba(38,41,107,0.10)' : 'rgba(38,41,107,0.04)';
  const parts = [], labs = [];
  let y = 0;
  // the axis: ticks at least 34 units apart; a label that would touch the one before it, the edge or the year's flag is left out
  const yx = year != null ? Math.max(20, Math.min(W - 20, X(year))) : null;
  const pxy = (x1 - x0) / (to - from), st = step || [10, 20, 50, 100].find(v => v * pxy >= 34) || 100;
  const ticks = []; for (let v = Math.ceil(from / st) * st; v <= to; v += st) ticks.push(v);
  let lastR = -99; const tl = ticks.map(v => { const w = mtlTw(v, f), a = X(v) + w / 2 > W - 1 ? 'end' : X(v) - w / 2 < 1 ? 'start' : 'middle', l = a === 'end' ? X(v) - w : a === 'start' ? X(v) : X(v) - w / 2,
    show = l > lastR + 4 && (yx == null || l > yx + 22 || l + w < yx - 22); if (show) lastR = l + w; return [v, a, show]; });
  parts.push(<g key="ax">{tl.map(([v, a, show]) => <g key={v}><line x1={X(v)} x2={X(v)} y1={13} y2={17} stroke={BK.muted} strokeWidth="1"/>{show && <text x={X(v)} y={10} textAnchor={a} fontSize={f} fontWeight="700" fill={BK.muted}>{v}</text>}</g>)}<line x1={x0} x2={x1} y1={17} y2={17} stroke={BK.muted} strokeWidth="1"/></g>);
  y = 22;
  const tap = (kind, id, lab, pressed) => onTap && tapKinds.includes(kind) ? { role: 'button', tabIndex: 0, 'aria-label': lab, 'aria-pressed': !!pressed, className: 'mtl-part', style: { cursor: 'pointer' },
    onClick: () => onTap(kind, id), onKeyDown: (e) => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); onTap(kind, id); } } } : {};
  const rowLab = (r, yc) => rowLabels && labs.push(<text key={'l' + r} x={0} y={yc + 3.5} fontSize={Math.max(9, f - 0.5)} fontWeight="900" letterSpacing="0.06em" fill={on(r) ? BK.ink : BK.muted}>{T(MTL_ROW_W[r][0], MTL_ROW_W[r][1]).toUpperCase()}</text>);
  rows.forEach(r => {
    if (r === 'era' || r === 'keys') {
      // a name inside its band where it fits; otherwise under the row, centred on its band, on as few lines as needed
      const isEra = r === 'era', h = isEra ? Math.max(big ? 26 : 22, f * 2.2) : Math.max(big ? 16 : 13, f * 1.4), under = [];
      const items = isEra ? MTL_ERAS.map(id => [...mtlYears(id), eraNm(id), id]) : MTL_KEYS.map(([a, b, e1, k1]) => [a, b, T(e1, k1), e1]);
      items.forEach(([a, b, nm, id]) => { if (b <= from || a >= to) return;
        const xa = X(a), xb = X(b), isSel = isEra && ((sel && sel.kind === 'era' && sel.id === id) || hiEra === id);
        const fz = isEra ? f + 0.5 : f - 0.5, inside = xb - xa >= mtlTw(nm, fz) * 1.06 + (isEra ? 6 : 10);
        const col = isSel ? BK.coral : on(r) || (isEra && on('cmp')) ? BK.ink : BK.muted, halo = year != null ? { stroke: '#fff', strokeWidth: 3, paintOrder: 'stroke', strokeLinejoin: 'round' } : {};
        // (a band cut off at the edge of a close-up is only context: its name, if it does not fit, is left out)
        if (!inside && xb - xa > 2 && ((a >= from && b <= to) || isSel)) under.push({ id, nm, cx: (xa + xb) / 2, col });
        parts.push(<g key={r + id} {...(isEra ? tap('era', id, nm + ' ' + a + T('–', '~') + (b > 2025 ? T('today', '오늘날') : b), isSel) : {})}>
          {isEra ? <rect x={xa + 0.5} y={y} width={Math.max(0, xb - xa - 1)} height={h} fill={isSel ? 'rgba(228,87,46,0.12)' : fillOf('era')} stroke={isSel ? BK.coral : sw('era')} strokeWidth={isSel ? 2 : on('era') ? 1.2 : 0.8}/>
            : <rect x={xa + 0.5} y={y} width={Math.max(0, xb - xa - 1)} height={h} rx={h / 2} fill={fillOf('keys')} stroke={sw('keys')} strokeWidth={on('keys') ? 1.1 : 0.7}/>}
          {inside && <text x={isEra ? (xa + xb) / 2 : xa + 6} y={y + h / 2 + fz * 0.36} textAnchor={isEra ? 'middle' : 'start'} fontSize={fz} fontWeight={isEra ? 900 : 800} fontStyle={isEra ? 'normal' : ital} fill={col} {...halo}>{nm}</text>}</g>); });
      if (!isEra && firstPiano && from < 1700 && to > 1700) parts.push(<g key="fp"><line x1={X(1700)} x2={X(1700)} y1={y - 2} y2={y + h + 2} stroke={BK.ink} strokeWidth="1.4"/><text x={X(1700) + 4} y={y + h / 2 + (f - 1) * 0.36} fontSize={f - 1} fontWeight="800" fill={BK.ink}>{T('first piano', '첫 피아노')}</text></g>);
      rowLab(r, y + h / 2); y += h + 2;
      const uz = Math.max(9, f - 0.5), ends = [];
      under.forEach(u => { const w = mtlTw(u.nm, uz) * 1.06, cx = Math.max(x0 + w / 2, Math.min(x1 - w / 2, u.cx));
        let k = ends.findIndex(e => cx - w / 2 > e + 6); if (k < 0) k = ends.length; ends[k] = cx + w / 2;
        parts.push(<text key={'u' + r + u.id} x={cx} y={y + (k + 1) * (uz + 2) - 1} textAnchor="middle" fontSize={uz} fontWeight={isEra ? 900 : 800} fontStyle={isEra ? 'normal' : ital} fill={u.col}>{u.nm}</text>); });
      y += ends.length * (uz + 2) + (isEra ? 4 : 5);
    }
    if (r === 'cmp') {
      const lh = laneH || (big ? 19 : 13), bh = barH || (big ? 14.5 : 8.5), y0 = y, nL = Math.max(1, L.n);
      if (guides) MTL_ERAS.slice(1).map(id => mtlYears(id)[0]).filter(b => b > from && b < to).forEach(b =>
        parts.push(<line key={'gd' + b} x1={X(b)} x2={X(b)} y1={y0 - 2} y2={y0 + nL * lh} stroke="rgba(38,41,107,0.18)" strokeWidth="0.8" strokeDasharray="2 3"/>));
      L.bars.forEach(({ c, k, x0: xa, x1: xb, name, inside, left, tip }) => {
        const yy = y0 + k * lh, picked = !!(sel && sel.kind === 'cmp' && sel.id === c.id), isSel = picked || lit.includes(c.id) || (year != null && mtlAlive(c, year));
        const col = isSel ? BK.coral : on('cmp') ? PEN_N : 'rgba(38,41,107,0.4)';
        const tx = inside ? xa + 6 : left ? xa - 4 : xb + tip + 4, anchor = left ? 'end' : 'start', tw = mtlTw(name, f);
        parts.push(<g key={'c' + c.id} {...tap('cmp', c.id, cmpT(c.name) + ', ' + life(c), picked)}>
          {onTap && tapKinds.includes('cmp') && <rect x={(left ? tx - tw : xa) - 2} y={yy} width={(left ? xb - tx + tw : inside ? xb - xa : xb - xa + tip + 4 + tw) + 4} height={lh} fill="transparent"/>}
          <rect x={xa} y={yy + (lh - bh) / 2} width={Math.max(2, xb - xa)} height={bh} rx={bh / 2} fill={col}/>
          {!c.died && <polygon points={`${xb},${yy + (lh - bh) / 2 - 2} ${xb + 6},${yy + lh / 2} ${xb},${yy + (lh + bh) / 2 + 2}`} fill={col}/>}
          <text x={tx} y={yy + lh / 2 + f * 0.35} textAnchor={anchor} fontSize={f} fontWeight={big ? 900 : 800} fill={inside ? '#fff' : isSel ? BK.coral : on('cmp') ? BK.ink : BK.muted}
            stroke={year != null && !inside ? '#fff' : 'none'} strokeWidth="3" paintOrder="stroke" strokeLinejoin="round">{name}</text></g>);
      });
      rowLab('cmp', y0 + nL * lh / 2); y += nL * lh + 6;
    }
    if (r === 'sound') {
      const h = 14;
      MTL_ERAS.forEach(id => { const [a, b] = mtlYears(id); if (b <= from || a >= to) return; const xa = X(a), xb = X(b), nm = T(MTL_SOUND[id][0], MTL_SOUND[id][1]);
        if (xb - xa >= mtlTw(nm, f) + 4) parts.push(<text key={'s' + id} x={(xa + xb) / 2} y={y + h / 2 + f * 0.36} textAnchor="middle" fontSize={f} fontWeight="800" fontStyle={ital} fill={on('sound') ? BK.ink : BK.muted}>{nm}</text>); });
      rowLab('sound', y + h / 2); y += h + 6;
    }
    if (r === 'style') {
      const lh = Math.max(12, f + 4.5), nl = 3;
      MTL_STYLES.forEach(([a, b, e1, k1, k]) => { if (b <= from || a >= to) return; const xa = X(a), xb = X(b), nm = T(e1, k1), yy = y + k * lh, inside = xb - xa >= mtlTw(nm, f - 0.5) + 10;
        parts.push(<g key={'g' + e1}><rect x={xa} y={yy + 1.5} width={Math.max(2, xb - xa)} height={lh - 3} rx={(lh - 3) / 2} fill={on('style') ? 'rgba(38,41,107,0.16)' : 'rgba(38,41,107,0.07)'} stroke={sw('style')} strokeWidth={0.6}/>
          <text x={inside ? xa + 5 : xa - 4} y={yy + lh / 2 + (f - 0.5) * 0.36} textAnchor={inside ? 'start' : 'end'} fontSize={f - 0.5} fontWeight="800" fill={on('style') ? BK.ink : BK.muted}>{nm}</text></g>); });
      rowLab('style', y + nl * lh / 2); y += nl * lh + 4;
    }
    if (r === 'draw') {   // empty lanes to draw lives on (the Workbook), the ticks carried up
      const n = 6, dh = 24;
      ticks.forEach(v => parts.push(<line key={'dv' + v} x1={X(v)} x2={X(v)} y1={y} y2={y + n * dh} stroke="rgba(38,41,107,0.2)" strokeWidth="0.7" strokeDasharray="2 3"/>));
      for (let i = 1; i <= n; i++) parts.push(<line key={'dl' + i} x1={x0} x2={x1} y1={y + i * dh} y2={y + i * dh} stroke="rgba(38,41,107,0.3)" strokeWidth="0.8"/>);
      rowLab('draw', y + n * dh / 2); y += n * dh + 6;
    }
  });
  if (year != null) {   // the line behind everything, its flag on top
    parts.unshift(<line key="yrl" x1={X(year)} x2={X(year)} y1={14} y2={y} stroke={BK.coral} strokeWidth="2"/>);
    parts.push(<g key="yr"><rect x={yx - 19} y={0} width={38} height={14} rx={3} fill={BK.coral}/><text x={yx} y={10.5} textAnchor="middle" fontSize="10.5" fontWeight="900" fill="#fff">{year}</text></g>);
  }
  const H = y + 2;
  return <svg viewBox={`0 0 ${W} ${H}`} role={onTap ? 'group' : 'img'} aria-label={label} style={{width:'100%',height:'auto',display:'block',fontFamily:'Inter, system-ui, sans-serif'}}>
    {onTap && <style>{'.mtl-part:focus{outline:none}.mtl-part:focus-visible>rect:first-of-type{stroke:#e4572e;stroke-width:2.5;stroke-dasharray:5 3}'}</style>}
    {labs}{parts}</svg>;
}
