// Build DK: the noteheads on every staff. Her 15:03: a notehead must not cross the lines around it, and a line note's line
// must show through its middle. For each page (the Lesson Book, Workbook and Teacher copy of every chapter, the checkpoints
// on paper, and the online lesson of every chapter) this reads the DOM: five equally spaced horizontal lines are a staff; a
// filled ellipse over a staff is a notehead; its box height against the gap and its centre against the nearest line or
// space say whether it fits and sits true. Usage: node heads786.js drills.t785.html [books|online|all] > report
const { start } = require('/home/claude/pbtest/kit/contentharness');
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
const WHAT = process.argv[3] || 'all';
const AUDIT = () => {
  const out = [];
  const svgs = [...document.querySelectorAll('svg')];
  svgs.forEach((svg, si) => {
    const sb = svg.getBoundingClientRect(); if (sb.width < 30 || sb.height < 20) return;
    const lines = [];
    svg.querySelectorAll('line, path, rect').forEach(el => {
      const r = el.getBoundingClientRect(); if (r.height > 2.6 || r.width < 36) return;
      if (el.tagName === 'rect' && r.height > 2) return;
      const st = getComputedStyle(el); if (el.tagName !== 'rect' && (st.stroke === 'none' || st.strokeOpacity === '0')) return;
      lines.push({ y: r.top + r.height / 2, x1: r.left, x2: r.right });
    });
    lines.sort((a, b) => a.y - b.y);
    const staves = [];
    for (let i = 0; i + 4 < lines.length; i++) {
      const L = lines.slice(i, i + 5), g = L[1].y - L[0].y; if (g < 4 || g > 40) continue;
      if (!L.every((l, j) => j === 0 || Math.abs(l.y - L[j - 1].y - g) < 0.7)) continue;
      const x1 = Math.max(...L.map(l => l.x1)), x2 = Math.min(...L.map(l => l.x2)); if (x2 - x1 < 30) continue;
      staves.push({ top: L[0].y, g, x1, x2 }); i += 4;
    }
    if (!staves.length) return;
    const heads = [];
    svg.querySelectorAll('ellipse, circle').forEach(el => {
      const st = getComputedStyle(el), f = st.fill; if (!f || f === 'none' || /^rgb\(255, 255, 255\)|rgb\(25[0-5], 2[45][0-9], 2[0-4][0-9]\)/.test(f)) return;
      const r = el.getBoundingClientRect(); if (r.width < 5 || r.height < 3 || r.width > 40) return;
      const vb = (svg.getAttribute('viewBox') || '').split(/[ ,]+/).map(Number), sc = vb.length === 4 && vb[2] > 0 ? sb.width / vb[2] : 1;
      const m = el.getScreenCTM(), cxu = +el.getAttribute('cx') || 0, cyu = +el.getAttribute('cy') || 0;   // the centre, through the element's own transform
      const pt = svg.createSVGPoint(); pt.x = cxu; pt.y = cyu; const q = pt.matrixTransform(m); const cx = q.x, cy = q.y;
      const rxu = +(el.getAttribute('rx') || el.getAttribute('r')), ryu = +(el.getAttribute('ry') || el.getAttribute('r'));
      const rot = (/rotate\((-?[\d.]+)/.exec(el.getAttribute('transform') || '') || [0, 0])[1] * Math.PI / 180;
      const sw = st.stroke && st.stroke !== 'none' ? parseFloat(st.strokeWidth) || 0 : 0;
      const hu = Math.sqrt(Math.pow(rxu * Math.sin(rot), 2) + Math.pow(ryu * Math.cos(rot), 2)) + sw / 2;
      const s = staves.find(s => cx >= s.x1 - 4 && cx <= s.x2 + 4 && cy >= s.top - 3.5 * s.g && cy <= s.top + 4 * s.g + 3.5 * s.g);
      if (!s) return;
      const p = (cy - s.top) / (s.g / 2), k = Math.round(p), err = Math.abs(p - k) * s.g / 2, onLine = ((k % 2) + 2) % 2 === 0;
      const h = hu * sc, over = h - s.g / 2;
      heads.push({ rx: el.getAttribute('rx') || el.getAttribute('r'), ry: el.getAttribute('ry') || el.getAttribute('r'), tr: el.getAttribute('transform') || '', g: +(s.g / sc).toFixed(1), h: +h.toFixed(2), over: +(over / sc).toFixed(2), err: +(err / sc).toFixed(2), onLine, fill: f, sw });
    });
    if (heads.length) out.push({ si, w: Math.round(sb.width), heads });
  });
  return out;
};
(async () => {
  const H = await start(process.argv[2] || 'drills.t785.html');
  const q0 = await H.open({ path: '?drill=staff', w: 900, h: 900 }); await sleep(800);
  const ids = await q0.evaluate(() => pathIds()); await q0.close();
  const pages = process.env.ONLY ? process.env.ONLY.split(',') : [];
  if (!process.env.ONLY && WHAT !== 'online') { for (const id of ids) for (const b of ['lesson', 'work', 'teacher']) pages.push('?book=' + b + '&ch=' + id); for (const f of ['0a', '0b', '1', '2', '3', '4']) pages.push('?book=check&floor=' + f, '?book=checkkey&floor=' + f); }
  if (!process.env.ONLY && WHAT !== 'books') for (const id of ids) pages.push('?drill=' + id + '&lock=1');
  const tally = {};   // by (rx, ry, transform, gap): counts, worst overflow, worst err
  let nHeads = 0, nOver = 0, nOff = 0;
  for (const path of pages) {
    const p = await H.open({ path, w: 900, h: 1300, dsf: 1 }); await sleep(1200);
    if (/drill=/.test(path)) { try { for (let i = 0; i < 6; i++) { const b = p.locator('button:has-text("Next")').first(); if (await b.count()) { await b.click(); await sleep(250); } } } catch (e) {} }
    const r = await p.evaluate(AUDIT);
    for (const s of r) for (const h of s.heads) {
      nHeads++; const bad = h.over > 0.05, off = h.err > 0.4; if (bad) nOver++; if (off) nOff++;
      const key = [h.rx, h.ry, h.tr.replace(/[-\d.]+ [-\d.]+\)$/, 'x y)'), 'sw' + h.sw, 'g' + h.g].join('|');
      const t = tally[key] || (tally[key] = { n: 0, over: 0, off: 0, worstOver: -99, worstErr: 0, where: [] });
      t.n++; if (bad) t.over++; if (off) t.off++; t.worstOver = Math.max(t.worstOver, h.over); t.worstErr = Math.max(t.worstErr, h.err);
      if ((bad || off) && t.where.length < 3 && !t.where.includes(path)) t.where.push(path);
    }
    await p.close();
  }
  console.log('pages', pages.length, 'heads', nHeads, 'overflow', nOver, 'off-centre', nOff);
  Object.entries(tally).sort((a, b) => (b[1].over + b[1].off) - (a[1].over + a[1].off)).forEach(([k, t]) => console.log((t.over || t.off ? 'FIX ' : 'ok  ') + k.padEnd(48), 'n', t.n, 'over', t.over, 'off', t.off, 'worstOver', t.worstOver.toFixed(1), 'worstErr', t.worstErr.toFixed(1), t.where.join(' ')));
  await H.close();
})();
