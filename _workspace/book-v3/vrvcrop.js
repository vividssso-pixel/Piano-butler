// Crop Verovio snippets: tight horizontally, a fixed band of 3 staff spaces above and below the staff (more if labels hang lower)
const { chromium } = require('playwright'); const fs = require('fs');
(async () => {
  const S = JSON.parse(fs.readFileSync(process.argv[2])); const out = {};
  const b = await chromium.launch(); const p = await b.newPage();
  for (const [k, svg] of Object.entries(S)) {
    await p.setContent('<body style="margin:0">' + svg + '</body>');
    out[k] = await p.evaluate(() => {
      const o = document.querySelector('svg'); const [, , W, H] = o.getAttribute('viewBox').split(' ').map(Number);
      o.setAttribute('width', W); o.setAttribute('height', H);
      const inner = o.querySelector('svg.definition-scale'); inner.setAttribute('width', W); inner.setAttribute('height', H);
      const O = o.getBoundingClientRect(); let x0 = 1e9, x1 = -1e9, y1 = -1e9, st = [1e9, -1e9];
      o.querySelectorAll('g.staff').forEach(g => { const r = g.querySelector(':scope > path') ? null : null; });
      o.querySelectorAll('g.staff > path').forEach(pth => { const r = pth.getBoundingClientRect(); st[0] = Math.min(st[0], r.top); st[1] = Math.max(st[1], r.bottom); });
      const hasNote = !!inner.querySelector('g.note, g.chord, g.rest'); inner.querySelectorAll('path, use, text, rect, ellipse, polygon').forEach(e => { if (hasNote && e.parentNode.matches('g.staff') && e.tagName === 'path') return; const r = e.getBoundingClientRect(); if (!r.width && !r.height) return; x0 = Math.min(x0, r.left); x1 = Math.max(x1, r.right); y1 = Math.max(y1, r.bottom); });
      const sp = (st[1] - st[0]) / 4, pad = sp * 0.8; if (!hasNote) x1 = Math.min(x1, x0 + 14 * sp); if (hasNote && inner.querySelector('g.space')) x1 = Math.max(x1, x0 + 11 * sp);
      const top = st[0] - 3 * sp - O.top, bot = Math.max(st[1] + 3 * sp, y1 + pad) - O.top;
      o.setAttribute('viewBox', `${(x0 - O.left - pad).toFixed(1)} ${top.toFixed(1)} ${(x1 - x0 + 2 * pad).toFixed(1)} ${(bot - top).toFixed(1)}`);
      o.removeAttribute('width'); o.removeAttribute('height');
      return o.outerHTML;
    });
  }
  fs.writeFileSync(process.argv[3], JSON.stringify(out)); await b.close(); console.log(Object.keys(out).length);
})();
