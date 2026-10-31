// Build DS (her 09:38): stems that hang off their noteheads. For every page (each chapter's Lesson Book, Workbook and Teacher
// copy, the checkpoints, every online step, the Scale finder's staff) this reads the DOM: a vertical line 18 to 60 px long is a
// stem; the notehead (an ellipse) at one of its ends is its head. A stem is attached when its centre line runs into the head
// (fill or outline) and its outer edge is flush with the head's outer edge (within half a pixel out, a pixel and a half in).
// Usage: node stems795.js drills.t795.html [books|online|all] > report ; ONLY=path1,path2 limits the pages
const { start } = require('/home/claude/pbtest/kit/contentharness');
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
const WHAT = process.argv[3] || 'all';
const AUDIT = () => {
  const out = [];
  for (const svg of document.querySelectorAll('svg')) {
    const heads = [...svg.querySelectorAll('ellipse')].filter(e => { const rx = +e.getAttribute('rx'), ry = +e.getAttribute('ry'); return rx >= 2.5 && rx <= 12 && ry >= 1.5 && ry <= 9 && rx / ry < 2.6 && e.getBoundingClientRect().width > 0; });
    if (!heads.length) continue;
    const hb = heads.map(e => { const st = getComputedStyle(e), m = e.getScreenCTM(), sc = m ? Math.hypot(m.a, m.b) : 1, sw = st.stroke !== 'none' ? (parseFloat(st.strokeWidth) || 0) : 0;
      // the true outer half-width of a tilted ellipse (a bounding box of a rotated shape is too wide)
      const th = (+((e.getAttribute('transform') || '').match(/rotate\(\s*([-\d.]+)/) || [0, 0])[1]) * Math.PI / 180, ax = +e.getAttribute('rx') + sw / 2, ay = +e.getAttribute('ry') + sw / 2;
      const X = sc * Math.sqrt(ax * ax * Math.cos(th) ** 2 + ay * ay * Math.sin(th) ** 2), c0 = svg.createSVGPoint(); c0.x = +e.getAttribute('cx'); c0.y = +e.getAttribute('cy'); const c = c0.matrixTransform(m);
      return { e, l: c.x - X, r: c.x + X, cy: c.y, cx: c.x, sc, sig: [e.getAttribute('rx'), e.getAttribute('ry'), (e.getAttribute('transform') || '').replace(/[\d.-]+ [\d.-]+\)$/, ')'), st.stroke === 'none' ? 'f' : 'o'].join('|') }; });
    for (const ln of svg.querySelectorAll('line')) {
      const x1 = +ln.getAttribute('x1'), x2 = +ln.getAttribute('x2'); if (Math.abs(x1 - x2) > 0.01) continue;
      const b = ln.getBoundingClientRect(), len = b.height; if (len < 18 || len > 70) continue;
      const st = getComputedStyle(ln), m = ln.getScreenCTM(); if (!m) continue; const sc = Math.hypot(m.a, m.b), w = (parseFloat(st.strokeWidth) || 1) * sc; if (w < 0.9 || w > 3.5 * sc) continue;
      const sx = b.left + b.width / 2, yA = b.top, yB = b.bottom;
      // the head at one end of the stem: its centre within 9 px across and 8 px up or down of that end
      let best = null;
      for (const h of hb) { const dy = Math.min(Math.abs(h.cy - yA), Math.abs(h.cy - yB)), dx = Math.abs(h.cx - sx); if (dx < (+h.e.getAttribute('rx') + 2.2) * h.sc && dy < 8 * h.sc && (!best || dx + dy < best.d)) best = { h, d: dx + dy, up: Math.abs(h.cy - yB) < Math.abs(h.cy - yA) }; }
      if (!best) continue;
      const h = best.h, right = sx > h.cx;   // a stem right of the head goes up, left goes down (or the head is below it)
      // does the centre line run into the head? test points along the stem, near its head end, in the head's own coordinates
      const inv = h.e.getScreenCTM().inverse(), pt = svg.createSVGPoint(); let hit = false;
      const yEnd = best.up ? yB : yA, dir = best.up ? -1 : 1;
      for (let k = -6; k <= 14 && !hit; k += 0.5) { pt.x = sx; pt.y = yEnd + dir * k; const p = pt.matrixTransform(inv); if (h.e.isPointInFill(p) || h.e.isPointInStroke(p)) hit = true; }
      const edge = right ? (sx + w / 2) - h.r : h.l - (sx - w / 2);   // >0: the stem's outer edge sticks out past the head
      const gap = edge / h.sc;
      const bad = !hit ? 'hangs' : gap > 0.5 ? 'out' : gap < -1.5 ? 'in' : '';
      out.push({ sig: h.sig + '|w' + (w / sc).toFixed(2), gap: +gap.toFixed(2), bad, hit });
    }
  }
  return out;
};
(async () => {
  const H = await start(process.argv[2]);
  const q0 = await H.open({ path: '?drill=staff', w: 900, h: 900 }); await sleep(800);
  const ids = await q0.evaluate(() => pathIds()); await q0.close();
  const pages = process.env.ONLY ? process.env.ONLY.split(',') : [];
  if (!process.env.ONLY && WHAT !== 'online') { for (const id of ids) for (const b of ['lesson', 'work', 'teacher']) pages.push('?book=' + b + '&ch=' + id); for (const f of ['0a', '0b', '1', '2', '3', '4']) pages.push('?book=check&floor=' + f); }
  if (!process.env.ONLY && WHAT !== 'books') { for (const id of ids) pages.push('?drill=' + id); pages.push('?tool=scale-finder&key=D', '?tool=scale-finder&key=Bb'); }
  const tally = {}; let n = 0, nb = 0;
  for (const path of pages) {
    const p = await H.open({ path, w: 900, h: 1300, dsf: 1 }); await sleep(1100);
    let r = [];
    if (/tool=scale-finder/.test(path)) { const b = p.locator('button', { hasText: 'Show on the staff' }); if (await b.count()) { await b.first().click(); await sleep(500); } r = await p.evaluate(AUDIT); }
    else if (/drill=/.test(path)) { r = await p.evaluate(AUDIT); const ns = await p.locator('section > button').count(); for (let k = 0; k < ns; k++) { try { await p.locator('section > button').nth(k).click({ timeout: 1500 }); await sleep(300); r = r.concat(await p.evaluate(AUDIT)); } catch (e) {} } }
    else r = await p.evaluate(AUDIT);
    for (const s of r) { n++; const t = tally[s.sig] = tally[s.sig] || { n: 0, bad: 0, kinds: {}, gaps: [], where: [] }; t.n++; t.gaps.push(s.gap); if (s.bad) { nb++; t.bad++; t.kinds[s.bad] = (t.kinds[s.bad] || 0) + 1; if (t.where.length < 3 && !t.where.includes(path)) t.where.push(path); } }
    await p.close();
  }
  console.log('pages', pages.length, 'stems', n, 'bad', nb);
  Object.entries(tally).sort((a, b) => b[1].bad - a[1].bad).forEach(([sig, t]) => { const g = t.gaps.sort((a, b) => a - b); console.log((t.bad ? 'FIX ' : 'ok  ') + sig.padEnd(44), 'n', t.n, 'bad', t.bad, JSON.stringify(t.kinds), 'gap', g[0], '..', g[g.length - 1], t.where.join(' ')); });
  await H.close();
})();
