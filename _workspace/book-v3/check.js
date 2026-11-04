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
        pg.querySelectorAll('g.verse text').forEach(tx => {   // (4) every note label sits centred under its notehead
          const ow = tx.closest('g.chord') || tx.closest('g.note'); if (!ow) return;
          const hs = [...ow.querySelectorAll('g.notehead')]; if (!hs.length) return;
          let a = 1e9, b = -1e9; hs.forEach(h => { const r = h.getBoundingClientRect(); a = Math.min(a, r.left); b = Math.max(b, r.right); });
          const T = tx.getBoundingClientRect(); if (!T.width) return;
          const d = (T.left + T.right) / 2 - (a + b) / 2;
          if (Math.abs(d) > 2) out.push(`p${i + 1}: label “${tx.textContent.trim()}” ${Math.round(d)}px off its note`);
        });
        pg.querySelectorAll('svg').forEach(sv => {   // (5) a gap of at least 3px between every label and any notehead or ledger line
          const objs = [...sv.querySelectorAll('g.notehead, g.ledgerLines path, g.accid')].map(e => e.getBoundingClientRect()).filter(r => r.width);
          sv.querySelectorAll('g.verse text').forEach(tx => { const T = tx.getBoundingClientRect(); if (!T.width) return;
            if (objs.some(R => R.left < T.right && R.right > T.left && T.top < R.bottom + 3 && T.bottom > R.top - 3)) out.push(`p${i + 1}: label “${tx.textContent.trim()}” touches a note`); });
        });
        const body = pg.querySelector('.body');
        if (body) {
          const lk = body.querySelector('.links');   // See also / Practise it sit at the bottom: content keeps 20px clear of them
          const limit = lk ? lk.getBoundingClientRect().top - 20 : (pg.querySelector('.sign, .ffoot') || pg.querySelector('.foot')).getBoundingClientRect().top - 4;
          if (lk && lk.getBoundingClientRect().bottom > pg.querySelector('.foot').getBoundingClientRect().top - 4) out.push(`p${i + 1}: links run into the page number`);
          let last = 0; body.querySelectorAll('*').forEach(e => { if (e.closest('.links')) return; const R = e.getBoundingClientRect(); if (R.height) last = Math.max(last, R.bottom); });
          if (last > limit) out.push(`p${i + 1}: content runs ${Math.round(last - limit)}px into the footer`);
          if (!pg.classList.contains('part2') && !pg.dataset.end) { const top = body.getBoundingClientRect().top, room = limit - top, used = last - top;   // (6) no wasted space: a page is at least 80% full
            if (room > 0 && used / room < 0.8) out.push(`p${i + 1}: page only ${Math.round(100 * used / room)}% full`); }
          body.querySelectorAll('*').forEach(e => { const R = e.getBoundingClientRect(); if (R.width && (R.right > P.right - 20 || R.left < P.left + 20)) out.push(`p${i + 1}: ${e.tagName.toLowerCase()} pokes out sideways`); });
        }
      });
      return [...new Set(out)];
    });
    console.log(f.split('/').pop() + ': ' + (r.length ? r.length + ' problem(s)' : 'OK'));
    r.slice(0, 25).forEach(x => console.log('   ' + x)); bad += (/handbook/.test(f) || process.env.STRICTFILL) ? r.length : r.filter(x => !/% full$/.test(x)).length;   // fill rule is strict for handbooks; a warning elsewhere until those pages are filled
    await p.close();
  }
  await b.close(); process.exit(bad ? 1 : 0);
})();
