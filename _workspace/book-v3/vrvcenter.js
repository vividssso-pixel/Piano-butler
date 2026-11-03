// Centre every lyric label under its notehead (Verovio places it left-aligned for its own font; we print in another font).
// Usage: node center.js in.json out.json
const { chromium } = require('playwright'); const fs = require('fs');
(async () => {
  const S = JSON.parse(fs.readFileSync(process.argv[2])); const out = {};
  const b = await chromium.launch(); const p = await b.newPage();
  for (const [k, svg] of Object.entries(S)) {
    await p.setContent('<body style="margin:0">' + svg + '</body>');
    out[k] = await p.evaluate(() => {
      document.querySelectorAll('g.verse text').forEach(tx => {
        const owner = tx.closest('g.chord') || tx.closest('g.note'); if (!owner) return;
        const heads = [...owner.querySelectorAll('g.notehead')]; if (!heads.length) return;
        let x0 = 1e9, x1 = -1e9; heads.forEach(h => { const bb = h.getBBox(); x0 = Math.min(x0, bb.x); x1 = Math.max(x1, bb.x + bb.width); });
        tx.setAttribute('x', ((x0 + x1) / 2).toFixed(1)); tx.setAttribute('text-anchor', 'middle');
      });
      return document.querySelector('svg').outerHTML;
    });
  }
  fs.writeFileSync(process.argv[3], JSON.stringify(out)); await b.close(); console.log(Object.keys(out).length);
})();
