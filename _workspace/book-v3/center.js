// Labels under notes: centre each on its notehead(s), then keep one straight row at least `GAP` below every notehead,
// ledger line and accidental it sits under (Sohyun: labels never touch the notes). Grows the viewBox to fit.
// Usage: node center.js in.json out.json
const { chromium } = require('playwright'); const fs = require('fs');
(async () => {
  const S = JSON.parse(fs.readFileSync(process.argv[2])); const out = {};
  const b = await chromium.launch(); const p = await b.newPage();
  for (const [k, svg] of Object.entries(S)) {
    await p.setContent('<body style="margin:0">' + svg + '</body>');
    out[k] = await p.evaluate(() => {
      const GAP = 230;   // a little under one staff space (180 units)
      const texts = [...document.querySelectorAll('g.verse text')];
      texts.forEach(tx => {
        const owner = tx.closest('g.chord') || tx.closest('g.note'); if (!owner) return;
        const heads = [...owner.querySelectorAll('g.notehead')]; if (!heads.length) return;
        let x0 = 1e9, x1 = -1e9; heads.forEach(h => { const bb = h.getBBox(); x0 = Math.min(x0, bb.x); x1 = Math.max(x1, bb.x + bb.width); });
        tx.setAttribute('x', ((x0 + x1) / 2).toFixed(1)); tx.setAttribute('text-anchor', 'middle');
      });
      if (!texts.length) return document.querySelector('svg').outerHTML;
      // labels of one staff share a row: group by their current y
      const rows = {}; texts.forEach(t => { const y = t.getAttribute('y'); (rows[y] = rows[y] || []).push(t); });
      const objs = [...document.querySelectorAll('g.notehead, g.ledgerLines path, g.accid')].map(e => e.getBBox());
      let grow = 0;
      Object.values(rows).forEach(row => {
        let dy = 0;
        row.forEach(t => { const T = t.getBBox(); objs.forEach(R => { if (R.x < T.x + T.width && R.x + R.width > T.x && R.y + R.height + GAP > T.y) dy = Math.max(dy, R.y + R.height + GAP - T.y); }); });
        if (dy > 0) { row.forEach(t => t.setAttribute('y', (parseFloat(t.getAttribute('y')) + dy).toFixed(1))); grow = Math.max(grow, dy); }
      });
      if (grow > 0) {
        const o = document.querySelector('svg'), inner = o.querySelector('svg.definition-scale');
        const ov = o.getAttribute('viewBox').split(' ').map(Number), iv = inner.getAttribute('viewBox').split(' ').map(Number);
        const add = grow + 40; iv[3] += add; ov[3] += add * ov[2] / iv[2];
        inner.setAttribute('viewBox', iv.join(' ')); o.setAttribute('viewBox', ov.map(v => +v.toFixed(2)).join(' '));
      }
      return document.querySelector('svg').outerHTML;
    });
  }
  fs.writeFileSync(process.argv[3], JSON.stringify(out)); await b.close(); console.log(Object.keys(out).length);
})();
