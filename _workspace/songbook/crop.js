// Crop each snippet to its music, top to bottom (the full width stays, so lines of one song keep one scale).
const { chromium } = require('playwright'); const fs = require('fs');
(async () => {
  const S = JSON.parse(fs.readFileSync(process.argv[2])); const out = {};
  const b = await chromium.launch(require('fs').existsSync('/opt/pw-browsers/chromium') ? { executablePath: '/opt/pw-browsers/chromium' } : {}); const p = await b.newPage();
  for (const [k, svg] of Object.entries(S)) {
    await p.setContent('<body style="margin:0;width:900px">' + svg + '</body>');
    out[k] = await p.evaluate(() => {
      const o = document.querySelector('svg'), inner = o.querySelector('svg.definition-scale'), g = inner.querySelector('g.page-margin');
      const bb = g.getBBox(), t = g.transform.baseVal.consolidate(), ty = t ? t.matrix.f : 0, tx = t ? t.matrix.e : 0;
      const iv = inner.getAttribute('viewBox').split(' ').map(Number), ov = o.getAttribute('viewBox').split(' ').map(Number), r = ov[2] / iv[2], pad = 56;
      const y0 = bb.y + ty - pad, h = bb.height + 2 * pad;
      inner.setAttribute('viewBox', [iv[0], y0, iv[2], h].map(v => +v.toFixed(1)).join(' '));
      o.setAttribute('viewBox', [0, 0, ov[2], +(h * r).toFixed(1)].join(' '));
      o.setAttribute('height', ''); o.removeAttribute('height'); o.removeAttribute('width');
      return o.outerHTML;
    });
  }
  fs.writeFileSync(process.argv[3], JSON.stringify(out)); await b.close(); console.log(Object.keys(out).length, 'cropped');
})();
