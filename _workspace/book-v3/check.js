// Layout check for every book page: (1) each sign, glyph or drawing stays inside its table cell / box,
// (2) nothing runs past the page footer, (3) nothing pokes out of the page sideways. Usage: node check.js file.html [...]
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); let bad = 0;
  for (const f of process.argv.slice(2)) {
    const p = await b.newPage({ viewport: { width: 900, height: 1200 } });
    await p.goto('file://' + f, { waitUntil: 'networkidle' }).catch(() => {}); await p.waitForTimeout(900);
    const r = await p.evaluate(() => {
      const out = [];
      const boxes = 'td, th, .mc, .bc, .bsq, .call, .mem, .tt3, .sdc, .mzc, .hb, .tile, .mcell, .opc, .fc, .lock, .dom, .wsc, .mm4 > div';
      document.querySelectorAll('.pg').forEach((pg, i) => {
        const P = pg.getBoundingClientRect();
        pg.querySelectorAll(boxes).forEach(cell => {
          const C = cell.getBoundingClientRect();
          cell.querySelectorAll('svg, img, .gl2, .ts, .pat, .ab').forEach(el => {
            if (el.closest('figure.vx') && !cell.matches('.fc, .opc')) return;
            const E = el.getBoundingClientRect(); if (!E.width || !E.height) return;
            const t = 1.5;
            if (E.top < C.top - t || E.bottom > C.bottom + t || E.left < C.left - t || E.right > C.right + t)
              out.push(`p${i + 1}: ${el.tagName.toLowerCase()}${el.className && el.className.baseVal === undefined ? '.' + el.className : ''} outside ${cell.tagName.toLowerCase()} (${Math.round(Math.max(C.top - E.top, E.bottom - C.bottom, C.left - E.left, E.right - C.right))}px) in “${(cell.innerText || '').trim().slice(0, 30)}”`);
          });
        });
        const body = pg.querySelector('.body');
        if (body) {
          const limit = (pg.querySelector('.sign, .ffoot') || pg.querySelector('.foot')).getBoundingClientRect().top - 4;
          let last = 0; body.querySelectorAll('*').forEach(e => { const R = e.getBoundingClientRect(); if (R.height) last = Math.max(last, R.bottom); });
          if (last > limit) out.push(`p${i + 1}: content runs ${Math.round(last - limit)}px into the footer`);
          body.querySelectorAll('*').forEach(e => { const R = e.getBoundingClientRect(); if (R.width && (R.right > P.right - 20 || R.left < P.left + 20)) out.push(`p${i + 1}: ${e.tagName.toLowerCase()} pokes out sideways`); });
        }
      });
      return [...new Set(out)];
    });
    console.log(f.split('/').pop() + ': ' + (r.length ? r.length + ' problem(s)' : 'OK'));
    r.slice(0, 25).forEach(x => console.log('   ' + x)); bad += r.length;
    await p.close();
  }
  await b.close(); process.exit(bad ? 1 : 0);
})();
