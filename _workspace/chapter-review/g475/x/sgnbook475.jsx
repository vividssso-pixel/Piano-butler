// ─── Phase 475: chapter 20, Signs: the second room of Level 4 (the level plan of Phase 435: 'Tie or slur? D.C., D.S. and
// Fine. (8va and ornaments: later.)'; the tie came in chapter 8 and the slur beside it in chapter 10, so this room reads
// the road signs: the repeat signs at both ends, 1st and 2nd time bars, D.C. al Fine, D.S. al Fine and the pause).
// It builds on chapter 8 (bars, the double bar line, the repeat sign: back to the start) and chapter 9 (C position).
// Built in full under Book rules 14 and 15 (her 2026-10-14 09:17 '계속 가줘 최종검토는 한꺼번에하게').
// Words: repeat sign (start and end), 1st and 2nd time bars, D.C. (da capo), D.S. (dal segno), segno, Fine, pause (its
// other name fermata); Korean 도돌이표 (chapter 8's), 시작 도돌이표 / 끝 도돌이표, 1번 괄호 / 2번 괄호, 다 카포, 달 세뇨,
// 세뇨, 피네, 늘임표 (its other name 페르마타), 끝세로줄 (chapter 8's double bar line), 마디.
// A road is a list of bars: { n: notes ([kind, beats, d]), start, end (repeat signs), v (1 or 2: a 1st or 2nd time bar),
// fine, segno, dc / ds (the words at its end), pause: [note indexes], curve: [[note, note]] (a tie or a slur in the bar) }.

// the order the bars are played in (1-based): a repeat once (not again after a D.C. or D.S.), the 1st time bar skipped the
// second time (and after a D.C. or D.S.), D.C. back to bar 1, D.S. back to the segno, Fine the end after a D.C. or D.S.,
// To Coda (after a D.C. or D.S.) on to the coda bar. mis: a mistake to make (the drill's wrong answers and the wrong roads
// it plays): noRep (no repeat), fromStart (back to the beginning, not to the start-repeat sign), v1Again (the 1st time
// bar played again), noFine (on past Fine), fineFirst (stop at Fine the first time), dsStart (D.S. back to the
// beginning), repAgain (the repeat taken again after the jump), noCoda (on past To Coda)
function sgnOrder(bars, mis = {}) {
  const out = [], done = new Set(), segno = bars.findIndex(x => x.segno), coda = bars.findIndex(x => x.coda);
  let i = 0, rs = 0, jumped = false, pass2 = false, guard = 0;
  while (i < bars.length && guard++ < 200) {
    const b = bars[i];
    if (b.start && !mis.fromStart) rs = i;
    if (b.v === 1 && pass2 && !mis.v1Again) { i++; continue; }
    out.push(i + 1);
    if (b.fine && (jumped || mis.fineFirst) && !mis.noFine) break;
    if (b.tocoda && jumped && coda > i && !mis.noCoda) { i = coda; continue; }
    if (b.end && !done.has(i) && (!jumped || mis.repAgain) && !mis.noRep) { done.add(i); pass2 = true; i = rs; continue; }
    if (b.end && done.has(i)) pass2 = false;   // past a repeat already taken: a later 1st time bar is played the first time
    if (b.v === 2) pass2 = false;
    if ((b.dc || b.ds) && !jumped) { jumped = true; pass2 = !mis.repAgain; rs = 0; if (mis.repAgain) done.clear(); i = b.dc || mis.dsStart ? 0 : Math.max(0, segno); continue; }
    if (coda > 0 && i === coda - 1 && !jumped) break;   // the coda is only reached by To Coda
    i++;
  }
  return out;
}
const sgnWords = (b) => (b.dc ? 'D.C.' : 'D.S.') + ' al ' + (b.al === 'coda' ? 'Coda' : 'Fine');
// a thin double bar line under Fine (not at the end) and before the coda; never on a task that asks for Fine
const sgnDbl = (bars, i, skip) => i < bars.length - 1 && ((bars[i].fine && !skip.has('fine')) || (bars[i + 1] && bars[i + 1].coda));
// the items of bars a..b (for sskRaw), with room for the signs; and where each bar's closing line is (its item index)
function sgnItems(bars, a, b, o = {}) {
  const items = [], ends = [], starts = [], skip = new Set(o.noSigns || []);
  if (o.ts) items.push(['ts', o.ts]);
  for (let i = a; i <= b; i++) {
    const bar = bars[i], last = i === bars.length - 1, next = bars[i + 1];
    if (i === a && (bar.start || o.room)) items.push(['sp', o.room ? 20 : 16]);
    if (i === a && bar.coda) items.push(['sp', 6]);
    starts.push(items.length); bar.n.forEach(nt => items.push(nt));
    if (bar.end) items.push(['sp', o.room ? 13 : 9], skip.has('end') && !last ? ['|'] : ['||']);
    else { const lt = bar.n[bar.n.length - 1], nD = lt[1] * (o.D || 30), tail = lt[0] === 'w' ? Math.max(0, 30 - nD) : Math.max(0, 24 - nD);   // the last note clear of the bar line
      if (o.room) items.push(['sp', 13]); else if (sgnDbl(bars, i, skip)) items.push(['sp', 5 + tail]); else if (tail) items.push(['sp', tail]); items.push(last ? ['||'] : ['|']); }
    ends.push(items.length - 1);
    if (i < b && next && (next.start || next.coda || o.room)) items.push(['sp', next.coda ? 26 : o.room ? 18 : 14]);
    else if (i < b && bar.end && !skip.has('end')) items.push(['sp', 10]);   // the next note clear of the thick line
  }
  return { items, ends, starts };
}
// the segno and the coda drawn (no music font needed): s = scale, (x, y) the foot of the sign, its middle
const sgnSegnoSvg = (x, y, s, c) => <g transform={`translate(${x} ${y}) scale(${s})`}><path d="M5 -21.5 C5 -26.5 -5.5 -26 -5 -20.5 C-4.6 -15 5 -15.5 5 -8.5 C5 -2 -5 -2.5 -5 -7" fill="none" stroke={c} strokeWidth="2.5" strokeLinecap="round"/>
  <line x1="-8" y1="-2" x2="8" y2="-26.5" stroke={c} strokeWidth="1.5"/><circle cx="-7.2" cy="-15.5" r="1.9" fill={c}/><circle cx="7.2" cy="-11.5" r="1.9" fill={c}/></g>;
const sgnCodaSvg = (x, y, s, c) => <g transform={`translate(${x} ${y}) scale(${s})`}><circle cx="0" cy="-13" r="7.5" fill="none" stroke={c} strokeWidth="2"/><line x1="0" x2="0" y1="-26" y2="0" stroke={c} strokeWidth="1.6"/><line x1="-11.5" x2="11.5" y1="-13" y2="-13" stroke={c} strokeWidth="1.6"/></g>;
const sgnPauseSvg = (x, y, s, c) => <g transform={`translate(${x} ${y}) scale(${s})`}><path d="M-10 0 Q0 -18 10 0" fill="none" stroke={c} strokeWidth="2.4" strokeLinecap="round"/><circle cx="0" cy="-2.5" r="2.3" fill={c}/></g>;
// the same signs in running text, about a capital's height
const SGN_INLINE = { '𝄋': ['-10 -28 20 30', (c) => sgnSegnoSvg(0, 0, 1, c)], '𝄌': ['-13 -28 26 30', (c) => sgnCodaSvg(0, 0, 1, c)], '𝄐': ['-12 -14 24 14', (c) => sgnPauseSvg(0, -1, 1, c)] };
const sgnGlyph = (g, key) => { const [vb, f] = SGN_INLINE[g]; return <svg key={key} viewBox={vb} aria-label={{ '𝄋': 'segno', '𝄌': 'coda', '𝄐': t('pause', '늘임표') }[g]} role="img" style={{height:g === '𝄐' ? '0.6em' : '1.05em',width:'auto',verticalAlign:g === '𝄐' ? '0.15em' : '-0.12em',margin:'0 0.08em',overflow:'visible'}}>{f('currentColor')}</svg>; };
const sgnSx = (x) => typeof x !== 'string' || !/[𝄋𝄐𝄌]/u.test(x) ? x : x.split(/([𝄋𝄐𝄌])/u).map((p, i) => /[𝄋𝄐𝄌]/u.test(p) ? sgnGlyph(p, i) : p);
const SGN_IT = "'Playfair Display', Georgia, serif";
// a road (bars a to b) on one staff with its signs. o.nums: bar numbers under the bars; o.lit: the bar sounding (pale coral
// behind it); o.hl: notes in coral ([bar, note]); o.coral: the signs in coral (start, end, v (or v1, v2), segno, fine, dc,
// pause, coda); o.noSigns: signs left out, with their room kept (for drawing them in)
function SgnStaff({ bars, a = 0, b, width = 400, o = {}, label, full, left }) {
  const bb = b == null ? bars.length - 1 : b, { items, ends, starts } = sgnItems(bars, a, bb, o), clef = 'treble';
  const hlIdx = []; let k = 0;
  for (let i = a; i <= bb; i++) bars[i].n.forEach((nt, j) => { if (sskIsRest(nt[0])) return; if ((o.hl || []).some(([x, y]) => x === i && y === j)) hlIdx.push(k); k++; });
  const oo = { D: o.D || 30, clef, hl: hlIdx, x0: o.x0 }, m = sskRaw((d) => dY(d), items, oo), vbw = Math.ceil(m.last + 8);
  const hi = dY(CLEFS[clef].high), lo = dY(CLEFS[clef].low), skip = new Set(o.noSigns || []), cor = new Set(o.coral || []);
  const col = (type) => cor.has(type) ? PEN_C : PEN_N, shown = (type, x) => x && !skip.has(type);
  const tier = (i) => i > a && ((bars[i - 1].fine && !skip.has('fine')) || (bars[i - 1].tocoda && !skip.has('coda')));
  let up = 0;
  for (let i = a; i <= bb; i++) { const x = bars[i];
    if (shown('segno', x.segno) || shown('coda', x.coda)) up = Math.max(up, 30); if (shown('v', x.v)) up = Math.max(up, 26);
    if (shown('fine', x.fine) || shown('dc', x.dc || x.ds) || shown('coda', x.tocoda)) up = Math.max(up, (x.dc || x.ds) && tier(i) ? 38 : 22);
    if (shown('pause', (x.pause || []).length)) up = Math.max(up, 22); }
  const pad = [Math.max(12, hi - m.top + 8, up + 6 + (o.band || 0)), Math.max(14, m.bottom - lo + (o.nums ? 19 : 8))];
  // each bar's closing line: '|' at last - 0.8; '||' thin at last - 7, thick last - 4 to last
  const closeX = ends.map(e => { const it = items[e], L = sskRaw((d) => dY(d), items.slice(0, e + 1), oo).last; return it[0] === '||' ? L - 7 : L - 0.8; });
  return <div style={{width:full ? '100%' : Math.min(100, vbw / width * 100) + '%',margin:full || left ? undefined : '0 auto'}}><SfStaff clef={clef} width={vbw} span={[4, m.last]} pad={pad} label={label}
    extra={(yOf, layer) => {
      const mm = sskRaw((d) => yOf(d, clef), items, oo), yT = yOf(CLEFS[clef].high, clef), yB = yOf(CLEFS[clef].low, clef);
      let ni = 0; const geo = [];
      for (let i = a; i <= bb; i++) { const cnt = bars[i].n.filter(nt => !sskIsRest(nt[0])).length, ns = mm.notes.slice(ni, ni + cnt); ni += cnt;
        const prev = geo[geo.length - 1], endX = closeX[i - a], startX = prev ? prev.endX + (bars[i].coda ? 26 : o.room ? 18 : bars[i].start ? 14 : bars[i - 1].end && !skip.has('end') ? 10 : 0) : (ns[0] ? ns[0].x - 18 : 60);
        geo.push({ i, ns, startX, endX }); }
      const topOf = (nt) => Math.min(nt.y - 7, nt.up ? nt.end : nt.y - 7), botOf = (nt) => Math.max(nt.y + 7, nt.up ? nt.y + 7 : nt.end);
      if (layer === 'under') return o.lit == null ? null : <g>{geo.filter(g => g.i === o.lit).map(g => { const y1 = Math.min(yT - 6, ...g.ns.map(topOf)) - 2, y2 = Math.max(yB + 6, ...g.ns.map(botOf)) + 3;
        return <rect key="lit" x={g.startX + 2} y={y1} width={g.endX - g.startX - 4} height={y2 - y1} rx="4" fill="#fbe3da"/>; })}</g>;
      const dots = (x, c) => [CLEFS[clef].low + 3, CLEFS[clef].low + 5].map((d, j) => <circle key={j} cx={x} cy={yOf(d, clef)} r="2.6" fill={c}/>);
      const numY = Math.max(yB, ...mm.notes.map(botOf)) + 14;
      const word = (x, y, s, c, sz = 14, anchor = 'end') => <text x={x} y={y} textAnchor={anchor} fontSize={sz} fontWeight="800" fontStyle="italic" fill={c} style={{fontFamily:SGN_IT}} paintOrder="stroke" stroke="#fff" strokeWidth="3" strokeLinejoin="round">{s}</text>;
      const els = [];
      geo.forEach(({ i, ns, startX, endX }, gi) => { const bar = bars[i], first = gi === 0;
        if (sgnDbl(bars, i, skip) && !bar.end) els.push(<line key={'b' + i} x1={endX - 4.5} x2={endX - 4.5} y1={yT} y2={yB} stroke={PEN_N} strokeWidth="1.5"/>);
        if (bar.start && !skip.has('start')) { const x = first ? (ns[0] ? ns[0].x - 30 : startX) : geo[gi - 1].endX, c = col('start');
          els.push(<g key={'s' + i}><rect x={x - 2} y={yT} width="4" height={yB - yT} fill={c}/><line x1={x + 5} x2={x + 5} y1={yT} y2={yB} stroke={c} strokeWidth="1.5"/>{dots(x + 10, c)}</g>); }
        if (bar.end && !skip.has('end')) { const c = col('end');
          els.push(<g key={'e' + i}>{dots(endX - 7, c)}{c !== PEN_N && <g><line x1={endX} x2={endX} y1={yT} y2={yB} stroke={c} strokeWidth="1.5"/><rect x={endX + 3} y={yT} width="4" height={yB - yT} fill={c}/></g>}</g>); }
        if (bar.v && !skip.has('v')) { const y = yT - 24, c = cor.has('v') || cor.has('v' + bar.v) ? PEN_C : PEN_N, w = c === PEN_C ? 2.2 : 1.6;
          const x1 = gi > 0 && bars[i - 1].end ? geo[gi - 1].endX + 9 : startX + 3, x2 = bar.end ? endX + 6 : endX - 3;
          els.push(<g key={'v' + i}><path d={`M${x1} ${y + 13} L${x1} ${y} L${x2} ${y}` + (bar.v === 1 ? ` L${x2} ${y + 13}` : '')} fill="none" stroke={c} strokeWidth={w}/>
            <text x={x1 + 5} y={y + 13} fontSize="13" fontWeight="900" fill={c} fontFamily="Inter, sans-serif">{bar.v}.</text></g>); }
        if (bar.segno && !skip.has('segno')) els.push(<g key={'g' + i}>{sgnSegnoSvg(first && ns[0] ? ns[0].x : startX + 12, yT - 6, 0.95, col('segno'))}</g>);
        if (bar.coda && !skip.has('coda')) els.push(<g key={'c' + i}>{sgnCodaSvg(startX + 12, yT - 6, 0.9, col('coda'))}{word(startX + 26, yT - 12, 'Coda', col('coda'), 13, 'start')}</g>);
        if (bar.fine && !skip.has('fine')) els.push(<g key={'f' + i}>{word(endX - 2, yT - 10, 'Fine', col('fine'), 12.5)}</g>);
        if (bar.tocoda && !skip.has('coda')) els.push(<g key={'t' + i}>{word(endX - 20, yT - 10, 'To Coda', col('coda'), 12.5)}{sgnCodaSvg(endX - 8, yT - 7, 0.7, col('coda'))}</g>);
        if ((bar.dc || bar.ds) && !skip.has('dc')) { const hit = tier(i) && endX - startX < sgnWords(bar).length * 6.4 + 8;
          els.push(<g key={'d' + i}>{word(endX - 2, yT - (hit ? 26 : 10), sgnWords(bar), col('dc'), 12)}</g>); }
        (bar.curve || []).forEach(([j1, j2]) => { const n1 = ns[j1], n2 = ns[j2]; if (!n1 || !n2) return; const y = Math.max(n1.y, n2.y) + 8, x1 = n1.x + 2, x2 = n2.x - 2;   // a tie or a slur (under the heads)
          els.push(<path key={'u' + i + '-' + j1} d={`M${x1} ${y} Q${(x1 + x2) / 2} ${y + 11} ${x2} ${y} Q${(x1 + x2) / 2} ${y + 8} ${x1} ${y}`} fill={PEN_N} stroke={PEN_N} strokeWidth="0.8"/>); });
        (bar.pause || []).forEach(j => { const it = bar.n[j]; if (!it || skip.has('pause')) return; let x, y;
          if (sskIsRest(it[0])) { x = sskRaw((d) => yOf(d, clef), items.slice(0, starts[gi] + j), oo).end + 14; y = yT - 4; }
          else { const nt = ns[bar.n.slice(0, j).filter(z => !sskIsRest(z[0])).length]; if (!nt) return; x = nt.x; y = Math.min(yT - 4, nt.up ? nt.end - 4 : nt.y - 10); }
          els.push(<g key={'p' + i + '-' + j}>{sgnPauseSvg(x, y, 1, col('pause'))}</g>); });
        if (o.nums) els.push(<text key={'n' + i} x={(startX + endX) / 2} y={numY} textAnchor="middle" fontSize="11.5" fontWeight="900" fill={o.lit === i ? PEN_C : BK.muted} fontFamily="Inter, sans-serif">{i + 1}</text>);
      });
      return <g><g dangerouslySetInnerHTML={{ __html: mm.raw }}/>{els}</g>;
    }}/></div>;
}
const sgnBox = (bars, rows, o = {}) => Math.max(...rows.map(([a, b], r) => sgnVbw(bars, a, b, r === 0 ? o : { ...o, ts: undefined })));
const sgnVbw = (bars, a, b, o = {}) => { const { items } = sgnItems(bars, a, b, o); return Math.ceil(sskRaw((d) => dY(d), items, { D: o.D || 30, clef: 'treble', x0: o.x0 }).last + 8); };
// a road in rows of bars (rows: [[a, b], ...]), one size, the clefs in line; the time signature on the first row only.
// rw: the width the staff is drawn for (the scale: a road narrower than rw keeps it); a wider road first spaces its notes
// closer (D down to 20), and only then is drawn smaller; every row then as wide as the widest (at most 1.7 times)
function SgnRoad({ bars, rows, rw = 330, o = {}, label, box: boxIn }) {
  const oOf = (r, oo = o) => r === 0 ? oo : { ...oo, ts: undefined };
  let oF = o;
  if (!boxIn && o.fit !== false) { let D = o.D || 30; while (D > 20 && sgnBox(bars, rows, { ...o, D }) > rw) D -= 0.5; oF = { ...o, D }; }
  const box = boxIn || sgnBox(bars, rows, oF), R = Math.max(rw, box);
  const just = (a, b, oo) => { if (o.just === false) return oo; const D0 = oo.D || 30, v1 = sgnVbw(bars, a, b, oo), v2 = sgnVbw(bars, a, b, { ...oo, D: D0 + 10 }), k = (v2 - v1) / 10;
    return k <= 0 || v1 >= box - 1 ? oo : { ...oo, D: Math.min(D0 * 1.7, D0 + (box - v1) / k) }; };
  return <div role="img" aria-label={label} style={{display:'flex',flexDirection:'column',gap:2,width:'100%'}}>{rows.map(([a, b], r) => <div key={r} aria-hidden="true" style={{width:box / R * 100 + '%',margin:'0 auto'}}><SgnStaff bars={bars} a={a} b={b} width={box} left o={just(a, b, oOf(r, oF))}/></div>)}</div>;
}
// the playing order as a row of numbers (coral outline: a bar played again); cur: the step sounding now
const sgnOrderRow = (ord, sz = 17, cur = -1) => { const seen = new Set();
  return <div style={{display:'flex',justifyContent:'center',flexWrap:'wrap',gap:6,fontSize:sz,fontWeight:900}}>{ord.map((n, j) => { const again = seen.has(n); seen.add(n);
    return <span key={j} style={{minWidth:sz * 1.6,textAlign:'center',padding:'2px 4px',borderRadius:6,border:'1.5px solid ' + (again ? PEN_C : 'rgba(38,41,107,0.35)'),color:j === cur ? '#fff' : BK.ink,background:j === cur ? PEN_N : 'transparent'}}>{n}</span>; })}</div>; };

const sgnQ = (d, k = 'q', n) => [k, n || ({ q: 1, h: 2, w: 4 })[k], d];
// the roads of the book's pictures (the pads on pages 2 to 6 play them); C position, right hand
const SGN_ROADS = {
  2: [{ n: [sgnQ(28), sgnQ(29), sgnQ(30), sgnQ(28)] }, { start: true, n: [sgnQ(30), sgnQ(31), sgnQ(32, 'h')] }, { end: true, n: [sgnQ(32), sgnQ(31), sgnQ(30), sgnQ(29)] }, { n: [sgnQ(28, 'w')] }],
  3: [{ n: [sgnQ(32), sgnQ(30), sgnQ(31), sgnQ(29)] }, { n: [sgnQ(30), sgnQ(28), sgnQ(29, 'h')] }, { v: 1, end: true, n: [sgnQ(29), sgnQ(30), sgnQ(31, 'h')] }, { v: 2, n: [sgnQ(28, 'w')] }],
  4: [{ n: [sgnQ(28), sgnQ(30), sgnQ(32), sgnQ(30)] }, { fine: true, n: [sgnQ(31), sgnQ(29), sgnQ(28, 'h')] }, { n: [sgnQ(32), sgnQ(32), sgnQ(31), sgnQ(31)] }, { dc: true, n: [sgnQ(30), sgnQ(30), sgnQ(29, 'h')] }],
  5: [{ n: [sgnQ(28, 'h'), sgnQ(30, 'h')] }, { segno: true, n: [sgnQ(32), sgnQ(31), sgnQ(30), sgnQ(31)] }, { fine: true, n: [sgnQ(32), sgnQ(30), sgnQ(28, 'h')] }, { n: [sgnQ(29), sgnQ(29), sgnQ(30), sgnQ(31)] }, { ds: true, n: [sgnQ(32), sgnQ(31), sgnQ(29, 'h')] }],
  6: [{ n: [sgnQ(30), sgnQ(31), sgnQ(32, 'h')], pause: [2] }, { n: [sgnQ(31), sgnQ(29), sgnQ(28, 'h')], pause: [2] }],
};
const SGN_ROAD6B = [{ n: [sgnQ(32), sgnQ(31), sgnQ(30), ['r', 1]], pause: [3] }, { n: [sgnQ(29), sgnQ(30), sgnQ(28, 'h')] }];
const SGN_LABEL6B = () => t('Two bars: G F E and a crotchet rest with a pause over it; D E C.', '두 마디: G F E와 늘임표가 붙은 4분쉼표; D E C.');
const SGN_CORAL = { 2: ['start', 'end'], 3: ['v'], 4: ['fine', 'dc'], 5: ['segno', 'dc'], 6: ['pause'] };
const SGN_ROWS = { 2: [[0, 1], [2, 3]], 3: [[0, 1], [2, 3]], 4: [[0, 1], [2, 3]], 5: [[0, 1], [2, 4]], 6: [[0, 1]] };
// what each road shows (the pictures' spoken names; the pads in the toolbox too)
const SGN_LABEL = {
  2: () => t('Four bars in 4/4. A start-repeat sign before bar 2, an end-repeat sign after bar 3. The bars are played 1 2 3 2 3 4.', '4/4의 네 마디. 2마디 앞에 시작 도돌이표, 3마디 뒤에 끝 도돌이표. 치는 차례는 1 2 3 2 3 4.'),
  3: () => t('Four bars. Bar 3 is under a bracket 1. and ends with an end-repeat sign; bar 4 is under a bracket 2. The bars are played 1 2 3 1 2 4.', '네 마디. 3마디는 1번 괄호 아래, 끝에 끝 도돌이표. 4마디는 2번 괄호 아래. 치는 차례는 1 2 3 1 2 4.'),
  4: () => t('Four bars. Fine over the end of bar 2, D.C. al Fine over the end of bar 4. The bars are played 1 2 3 4 1 2.', '네 마디. 2마디 끝 위에 Fine, 4마디 끝 위에 D.C. al Fine. 치는 차례는 1 2 3 4 1 2.'),
  5: () => t('Five bars. The segno over the start of bar 2, Fine over the end of bar 3, D.S. al Fine over the end of bar 5. The bars are played 1 2 3 4 5 2 3.', '다섯 마디. 2마디 시작 위에 세뇨, 3마디 끝 위에 Fine, 5마디 끝 위에 D.S. al Fine. 치는 차례는 1 2 3 4 5 2 3.'),
  6: () => t('Two bars: E F G, F D C. A pause over the G and over the last C.', '두 마디: E F G, F D C. G 위와 마지막 C 위에 늘임표.'),
};

// page 6: how long each note sounds, in time and with the pauses: a box a beat, the pause's extra time in coral; both rows
// on one time scale (the longer row sets it), so the held row is visibly longer. stack: the labels above the rows (phones)
function SgnBeats({ bars, stack, h = 34 }) {
  const beats = (held) => bars.reduce((a, b) => a + b.n.reduce((s, nt, j) => s + nt[1] * (held && (b.pause || []).includes(j) ? 2 : 1), 0), 0), max = beats(true);
  const row = (held, label) => { let x = 0; const els = [];
    bars.forEach((b, i) => { if (i > 0) els.push(<span key={'s' + i} style={{position:'absolute',left:'calc(' + x / max * 100 + '% - 1px)',top:-3,bottom:-3,width:2,background:BK.ink}}/>);
      b.n.forEach((nt, j) => { const w = nt[1], p = held && (b.pause || []).includes(j), r = sskIsRest(nt[0]);
        els.push(<span key={i + '-' + j} style={{position:'absolute',left:'calc(' + x / max * 100 + '% + 2px)',width:'calc(' + w / max * 100 + '% - 4px)',top:0,bottom:0,border:'1.5px ' + (r ? 'dotted' : 'solid') + ' ' + BK.ink,borderRadius:4,display:'flex',alignItems:'center',justifyContent:'center',fontSize:r ? 11 : 14,fontWeight:900,color:r ? BK.muted : BK.ink,background:'#fff',boxSizing:'border-box',overflow:'hidden',whiteSpace:'nowrap'}}>{r ? t('rest', '쉼') : dName(nt[2])}</span>); x += w;
        if (p) { els.push(<span key={i + '-' + j + 'p'} style={{position:'absolute',left:'calc(' + x / max * 100 + '% + 2px)',width:'calc(' + w / max * 100 + '% - 4px)',top:0,bottom:0,border:'1.5px dashed ' + PEN_C,borderRadius:4,background:'#fbe3da',boxSizing:'border-box'}}/>); x += w; } }); });
    return <div style={{display:'grid',gridTemplateColumns:stack ? '1fr' : '128px 1fr',alignItems:'center',gap:stack ? 3 : 12}}>
      <div style={{fontSize:13,fontWeight:800,color:BK.muted,textAlign:stack ? 'left' : 'right',lineHeight:1.2}}>{label}</div>
      <div style={{position:'relative',height:h,minWidth:0}}>{els}</div></div>; };
  return <div aria-hidden="true" style={{display:'flex',flexDirection:'column',gap:10,width:'100%'}}>{row(false, t('in time', '박자대로'))}{row(true, t('with the pauses', '늘임표대로'))}</div>;
}

function sgnLbPages(scr = false) {
  const ch = 'signs';
  const live = (still, comp) => <LbLive still={still} live={comp}/>;
  const stack = (nodes, h, gap = 12, mw = 680) => <LbPic h={h}><div style={{display:'flex',flexDirection:'column',gap,width:'100%',maxWidth:mw,margin:'0 auto',alignItems:'stretch'}}>{nodes}</div></LbPic>;
  const nbKo = (x) => x.replace(/(\d번) 괄호/g, '$1 괄호').replace(/D\.([CS])\. al Fine/g, 'D.$1. al Fine');
  const X = (en, ko) => sgnSx(sscT(en, nbKo(skgKo(ko)))), REF = scr ? 270 : 330, LN = (x) => <span style={{fontFamily:'inherit',fontVariantNumeric:'lining-nums'}}>{x}</span>;
  const road = (pg, extra, rw = REF) => [<SgnRoad key="r" bars={SGN_ROADS[pg]} rows={SGN_ROWS[pg]} rw={rw} o={{ ts: 4, nums: pg !== 6, D: 28, coral: SGN_CORAL[pg], ...extra }} label={SGN_LABEL[pg]()}/>,
    pg !== 6 && <div key="o" style={{display:'flex',flexDirection:'column',alignItems:'center',gap:4}}><div style={{fontSize:13,fontWeight:800,color:BK.muted,letterSpacing:'0.06em'}}>{t('PLAY THE BARS IN THIS ORDER', '이 차례로 쳐요')}</div>{sgnOrderRow(sgnOrder(SGN_ROADS[pg]))}</div>].filter(Boolean);
  // the opener: the signs of the chapter, each named, its sign in coral; one whole note a bar, every staff at one size
  const W1 = (d, x = {}) => ({ n: [sgnQ(d, 'w')], ...x });
  const minis = [
    ['r', t('Repeat signs', '도돌이표'), [W1(30, { start: true }), W1(32, { end: true }), W1(28)], ['start', 'end']],
    ['v', t('1st and 2nd time bars', '1번 괄호와 2번 괄호'), [W1(30), W1(32, { v: 1, end: true }), W1(28, { v: 2 })], ['v']],
    ['dc', 'D.C. al Fine', [W1(30), W1(28, { fine: true }), W1(31, { dc: true })], ['dc']],
    ['ds', t('Segno and D.S. al Fine', '세뇨와 D.S. al Fine'), [W1(30), W1(28, { segno: true, fine: true }), W1(31, { ds: true })], ['segno', 'dc']],
    ['f', t('Fine (said fee-nay)', 'Fine(피네)'), [W1(30), W1(28, { fine: true }), W1(31, { dc: true })], ['fine']],
    ['p', t('The pause', '늘임표'), [W1(30), W1(28, { pause: [0] })], ['pause']],
  ], MO = { D: 14 }, mBox = Math.max(...minis.map(([, , bars]) => sgnVbw(bars, 0, bars.length - 1, MO)));
  const p1 = <LbPic h={scr ? undefined : 260}><div role="img" aria-label={t('The signs of this chapter: the repeat signs, 1st and 2nd time bars, D.C. al Fine, the segno with D.S. al Fine, Fine, and the pause.', '이 챕터의 기호: 도돌이표, 1번 괄호와 2번 괄호, D.C. al Fine, 세뇨와 D.S. al Fine, Fine, 늘임표.')} style={{display:'grid',gridTemplateColumns:scr ? '1fr' : 'repeat(2,1fr)',gap:scr ? '10px' : '18px 40px',width:'100%',maxWidth:scr ? 300 : 640,margin:'0 auto'}}>
    {minis.map(([key, name, bars, coral]) => <div key={key} style={{display:'flex',flexDirection:'column',alignItems:'center',justifyContent:'flex-end',gap:2,minWidth:0}}><div aria-hidden="true" style={{width:'100%',maxWidth:scr ? 260 : 290}}><SgnStaff bars={bars} width={mBox} o={{ ...MO, coral }}/></div>
      <div style={{fontSize:scr ? 13 : 14,fontWeight:800,color:BK.ink,textAlign:'center',lineHeight:1.3,fontVariantNumeric:'lining-nums'}}>{name}</div></div>)}
  </div></LbPic>;
  const p2 = stack(road(2), 300, 14);
  const p3 = stack(road(3), 300, 14);
  const p4 = stack(road(4), 300, 14);
  const p5 = stack(road(5), 300, 14);
  const PW = scr ? REF : 370, pauseEx = (bars, label, k) => { const o = { ts: 4, D: 28, coral: ['pause'] }; let D = 28; while (D > 20 && sgnBox(bars, [[0, 1]], { ...o, D }) > PW) D -= 0.5;
    const box = sgnBox(bars, [[0, 1]], { ...o, D }), R = Math.max(PW, box);
    return <div key={k} style={{display:'flex',flexDirection:'column',gap:4}}><SgnRoad bars={bars} rows={[[0, 1]]} rw={PW} o={o} label={label}/>
      <div style={{width:box / R * 100 + '%',margin:'0 auto',boxSizing:'border-box',padding:'0 ' + 8 / box * 100 + '% 0 ' + 74 / box * 100 + '%'}}><SgnBeats bars={bars} stack h={28}/></div></div>; };
  const p6 = stack([pauseEx(SGN_ROADS[6], SGN_LABEL[6](), 'a'), pauseEx(SGN_ROAD6B, SGN_LABEL6B(), 'b')], 260, 16);

  // the check icons
  const tx = (x, c, col, s = 18, y = 28, it) => '<text x="' + x + '" y="' + y + '" text-anchor="middle" font-family="' + (it ? "'Playfair Display', Georgia, serif" : 'Inter, sans-serif') + '"' + (it ? ' style="font-family:\'Playfair Display\', Georgia, serif;font-style:italic"' : '') + ' font-size="' + s + '" font-weight="900" fill="' + col + '">' + c + '</text>';
  const rep = (x, start) => start ? '<rect x="' + x + '" y="6" width="4" height="28" fill="' + PEN_N + '"/><line x1="' + (x + 8) + '" x2="' + (x + 8) + '" y1="6" y2="34" stroke="' + PEN_N + '" stroke-width="1.5"/><circle cx="' + (x + 14) + '" cy="16" r="2.4" fill="' + PEN_C + '"/><circle cx="' + (x + 14) + '" cy="24" r="2.4" fill="' + PEN_C + '"/>'
    : '<circle cx="' + x + '" cy="16" r="2.4" fill="' + PEN_C + '"/><circle cx="' + x + '" cy="24" r="2.4" fill="' + PEN_C + '"/><line x1="' + (x + 6) + '" x2="' + (x + 6) + '" y1="6" y2="34" stroke="' + PEN_N + '" stroke-width="1.5"/><rect x="' + (x + 10) + '" y="6" width="4" height="28" fill="' + PEN_N + '"/>';
  const segno = (x, y, c) => '<g transform="translate(' + x + ' ' + y + ') scale(1.05)"><path d="M5 -21.5 C5 -26.5 -5.5 -26 -5 -20.5 C-4.6 -15 5 -15.5 5 -8.5 C5 -2 -5 -2.5 -5 -7" fill="none" stroke="' + c + '" stroke-width="2.5" stroke-linecap="round"/><line x1="-8" y1="-2" x2="8" y2="-26.5" stroke="' + c + '" stroke-width="1.5"/><circle cx="-7.2" cy="-15.5" r="1.9" fill="' + c + '"/><circle cx="7.2" cy="-11.5" r="1.9" fill="' + c + '"/></g>';
  const ic = {
    rep: [{ k: 'raw', svg: rep(14, true) + tx(46, '…', PEN_N, 16, 26) + rep(64, false) }],
    v: [{ k: 'raw', svg: '<path d="M8 30 L8 10 L42 10 L42 30" fill="none" stroke="' + PEN_N + '" stroke-width="2"/>' + tx(20, '1.', PEN_C, 13, 24) + '<path d="M50 30 L50 10 L86 10" fill="none" stroke="' + PEN_N + '" stroke-width="2"/>' + tx(62, '2.', PEN_C, 13, 24) }],
    dc: [{ k: 'raw', svg: tx(46, 'D.C.', PEN_C, 18, 27, true) }],
    ds: [{ k: 'raw', svg: segno(22, 34, PEN_N) + tx(60, 'D.S.', PEN_C, 18, 27, true) }],
    pause: [{ k: 'raw', svg: '<path d="M32 22 Q46 4 60 22" fill="none" stroke="' + PEN_C + '" stroke-width="2.4"/><circle cx="46" cy="18" r="2.6" fill="' + PEN_C + '"/><ellipse cx="46" cy="32" rx="6.5" ry="4.8" fill="' + PEN_N + '"/>' }],
  };
  const checksRows = [
    ['rep', t('I can play a part twice between the repeat signs', '도돌이표 사이의 마디를 두 번 칠 수 있어요')],
    ['v', t('I can play the 1st time bar, then the 2nd', '1번 괄호 마디를 치고, 다음에는 2번 괄호 마디를 칠 수 있어요')],
    ['dc', t('I can follow D.C. al Fine', 'D.C. al Fine를 따라 칠 수 있어요')],
    ['ds', t('I can follow D.S. al Fine', 'D.S. al Fine를 따라 칠 수 있어요')],
    ['pause', t('I can hold a pause', '늘임표가 붙은 음을 길게 누를 수 있어요')],
  ].map(([a, x]) => [a, LANG === 'ko' ? nbKo(skgKo(sscNbKo(x))) : sscNbEn(x)]);
  const ch8 = bkChapterNo('time-signatures');

  return [
    <LbPage key="1" no={1} chId={ch}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:44,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{bkChapterName(ch)}</div>
      </div></LbOnly>
      {p1}
      <LbSay size={17.5}>{LANG === 'ko' ? <>악보의 <b>기호</b>는 길을 알려 줘요: 어느 마디를 다시 칠지, 어디로 돌아갈지, 어디서 멈출지, 어느 음을 길게 누를지.</> : <>The <b>signs</b> in the music show the road: which bars to play again, where to go back to, where to stop, and which note to hold.</>}</LbSay>
      <div className="lb-toc" style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>
        <LbOnly print><div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('In this chapter', '이 챕터에서는')}</div>
          {[[t('Repeat signs', '도돌이표'), 2], [t('1st and 2nd time bars', '1번 괄호와 2번 괄호'), 3], ['D.C. al Fine', 4], ['D.S. al Fine', 5], [t('The pause', '늘임표'), 6], [t('My five checks', '나의 다섯 가지 확인'), 7]].map(([n, p]) => <div key={p} className="lb-toc-row" style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:14.5,padding:'4px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkGoal(15)}<span>{n}</span></span><span style={{color:BK.muted,fontWeight:800}}>{p}</span></div>)}
        </div></LbOnly>
        <div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 챕터를 마치면')}</div>
          {checksRows.map(([, x], i) => <div key={i} style={{display:'flex',gap:9,fontSize:14.5,padding:'4px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}>{bkGoal(15)}<span>{sscSx(x.replace(/^I can /, ''))}</span></div>)}
        </div>
      </div>
      <LbOnly print><LbDrillStrip id={ch}/></LbOnly>
    </LbPage>,

    <LbPage key="2" no={2} chId={ch} kicker={t('Step 1', '1단계')} title={t('Repeat signs', '도돌이표')}>
      {live(p2, <SgnPad page={2}/>)}
      <LbDefs items={[
        [t('end-repeat sign', '끝 도돌이표'), X('Two dots before a thin and a thick line: go back to the start-repeat sign, or to the beginning, and play again (chapter ' + ch8 + ').', '끝세로줄 앞의 점 두 개: 시작 도돌이표로, 없으면 처음으로 돌아가 한 번 더 쳐요(' + ch8 + '챕터).')],
        [t('start-repeat sign', '시작 도돌이표'), X('A thick and a thin line with two dots after them: the place to go back to.', '굵은 줄과 가는 줄 뒤의 점 두 개: 돌아갈 자리.')],
      ]}/>
      <LbPiano steps={[
        X('Right hand in C position: counting 1 2 3 4, play the bars in the order under the picture.', '오른손 C 자리: 1 2 3 4를 세면서, 그림 아래의 차례로 마디를 쳐요.'),
        X('Point to the two repeat signs, then play it again, saying the bar numbers.', '도돌이표 두 개를 가리키고, 마디 번호를 말하며 다시 쳐요.'),
      ]}/>
      <LbRemember>{X('Go back to the start-repeat sign, or to the beginning.', '시작 도돌이표로, 없으면 처음으로 돌아가요.')}</LbRemember>
    </LbPage>,

    <LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={LN(t('1st and 2nd time bars', '1번 괄호와 2번 괄호'))}>
      {live(p3, <SgnPad page={3}/>)}
      <LbDefs items={[
        [LN(t('1st time bar', '1번 괄호')), X('The bar under the bracket marked 1.: play it the first time, then go back.', '숫자 1이 적힌 괄호: 그 아래 마디는 처음에만 치고, 돌아가요.')],
        [LN(t('2nd time bar', '2번 괄호')), X('The bar under the bracket marked 2.: the second time, skip the 1st time bar and play this one. The brackets’ other name is volta brackets.', '숫자 2가 적힌 괄호: 두 번째에는 1번 괄호를 건너뛰고 그 아래 마디를 쳐요.')],
      ]}/>
      <LbPiano steps={[
        X('Counting 1 2 3 4, play the bars in the order under the picture.', '1 2 3 4를 세면서, 그림 아래의 차례로 마디를 쳐요.'),
        X('Play it again, saying “first time” at bar 3 and “second time” at bar 4.', '3마디에서 “처음”, 4마디에서 “두 번째”라고 말하며 다시 쳐요.'),
      ]}/>
      <LbRemember>{X('First time the 1. bar, second time the 2. bar.', '처음에는 1번 괄호, 두 번째에는 2번 괄호.')}</LbRemember>
    </LbPage>,

    <LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title="D.C. al Fine">
      {live(p4, <SgnPad page={4}/>)}
      <LbDefs items={[
        ['D.C.', X('Da capo, Italian for “from the head”: go back to the beginning.', '다 카포, 이탈리아어로 “첫머리부터”: 처음으로 돌아가요.')],
        ['Fine', X('Said fee-nay, Italian for “end”: stop here when you come to it after a D.C. or D.S. It sits over two thin bar lines.', '피네, 이탈리아어로 “끝”: D.C.나 D.S.로 돌아온 뒤에는 여기서 멈춰요. 겹세로줄 위에 적어요.')],
        ['D.C. al Fine', X('“From the head to the end”: go back to the beginning and play up to Fine.', '“처음부터 끝까지”: 처음으로 돌아가 Fine까지 쳐요.')],
      ]}/>
      <LbPiano steps={[
        X('Play the bars in the order under the picture.', '그림 아래의 차례로 마디를 쳐요.'),
        X('Point to Fine and to D.C. al Fine, then play it again with no gap at the D.C.', 'Fine와 D.C. al Fine를 가리키고, D.C.에서 쉬지 않고 이어서 다시 쳐요.'),
      ]}/>
      <LbRemember>{X('D.C. al Fine: from the beginning to Fine.', 'D.C. al Fine: 처음부터 Fine까지.')}</LbRemember>
    </LbPage>,

    <LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title="D.S. al Fine">
      {live(p5, <SgnPad page={5}/>)}
      <LbDefs items={[
        [sgnSx(t('segno 𝄋', '세뇨 𝄋')), X('Italian for “sign”: a place to go back to.', '이탈리아어로 “표시”: 돌아갈 자리.')],
        ['D.S.', X('Dal segno, “from the sign”: go back to 𝄋.', '달 세뇨, “표시부터”: 𝄋로 돌아가요.')],
        ['D.S. al Fine', X('“From the sign to the end”: go back to the sign and play up to Fine.', '“세뇨부터 끝까지”: 세뇨로 돌아가 Fine까지 쳐요.')],
      ]}/>
      <LbPiano steps={[
        X('Play the bars in the order under the picture.', '그림 아래의 차례로 마디를 쳐요.'),
        X('Point to the segno, to Fine and to D.S. al Fine, then play it again with no gap at the D.S.', '세뇨, Fine, D.S. al Fine를 가리키고, D.S.에서 쉬지 않고 이어서 다시 쳐요.'),
      ]}/>
      <LbRemember>{X('D.C.: back to the beginning. D.S.: back to the sign.', 'D.C.는 처음으로, D.S.는 세뇨로.')}</LbRemember>
    </LbPage>,

    <LbPage key="6" no={6} chId={ch} kicker={t('Step 5', '5단계')} title={t('The pause', '늘임표')}>
      {live(p6, <SgnPad page={6}/>)}
      <LbDefs items={[
        [sgnSx(t('pause 𝄐', '늘임표 𝄐')), X('A curve with a dot, over a note or rest: hold it longer than its value (about twice as long, or as the music needs), then go on. Its other name is fermata.', '음표나 쉼표 위에 붙는, 점이 있는 곡선: 제 길이보다 더 길게(두 배쯤, 또는 음악에 맞게) 늘인 다음, 이어서 쳐요. 다른 이름은 페르마타예요.')],
      ]}/>
      <LbPiano steps={[
        X('Play the two bars of the picture. Hold the G and the last C about twice as long.', '그림의 두 마디를 쳐요. G와 마지막 C를 두 배쯤 길게 눌러요.'),
        X('Play it once without the pauses, then with them. Hear the difference.', '늘임표 없이 한 번, 늘임표대로 한 번 쳐요. 차이를 들어 봐요.'),
      ]}/>
      <LbRemember>{X('A pause: hold it longer, then go on.', '늘임표: 더 길게 누르고, 이어서 쳐요.')}</LbRemember>
    </LbPage>,

    <LbPage key="7" no={7} chId={ch} kicker={t('Check-up', '점검')} title={t('My five checks', '나의 다섯 가지 확인')}>
      <LbSay>{t('Show each one at the piano, on its page (2 to 6). The check-up on paper is in the Workbook.', '2~6쪽을 하나씩 펴고 피아노 앞에서 보여 줘요. 종이 점검은 워크북에 있어요.')}</LbSay>
      <LbLive still={<LbStageRows big rows={checksRows.map(([a, x]) => [<PenArt shapes={ic[a]} vb={[0, 0, 92, 40]} style={{width:80}}/>, sscSx(x)])}/>} live={<FiveChecks376 storeKey="pb_five_sgn_v1" rows={checksRows.map(([a, x]) => [{ shapes: ic[a], vb: [0, 0, 92, 40] }, sscSx(x)])}/>}/>
    </LbPage>,
  ];
}
function SignsLessonBook() { return <>{sgnLbPages(false)}</>; }
