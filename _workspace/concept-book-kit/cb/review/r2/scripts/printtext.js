// Smallest text per printed page (CSS px at A4 size; 1 px = 0.75 pt), SVG and HTML.
const { start } = require('/home/claude/pbtest/kit/contentharness');
(async () => {
  const H = await start('drills.t485.html');
  for (const lang of ['en', 'ko']) {
    const p = await H.open({ path: '?book=concept&ch=p-scales&lang=' + lang, w: 900, h: 1300, dsf: 1 }); await p.waitForTimeout(2500);
    const r = await p.evaluate(() => [...document.querySelectorAll('[data-lb-page]')].map(pg => {
      const items = [];
      pg.querySelectorAll('svg text, svg tspan').forEach(t => { if (!t.textContent.trim() || t.querySelector('tspan')) return; const m = t.getScreenCTM(); if (!m) return; items.push([+(parseFloat(getComputedStyle(t).fontSize) * Math.hypot(m.a, m.b)).toFixed(1), t.textContent.trim().slice(0, 12), 'svg']); });
      const tw = document.createTreeWalker(pg, NodeFilter.SHOW_TEXT); let n; while ((n = tw.nextNode())) { if (!n.nodeValue.trim()) continue; const el = n.parentElement; if (el.closest('svg')) continue; const rr = el.getBoundingClientRect(); if (!rr.width) continue; items.push([parseFloat(getComputedStyle(el).fontSize), n.nodeValue.trim().slice(0, 12), 'html']); }
      items.sort((a, b) => a[0] - b[0]);
      return pg.getAttribute('data-lb-page') + ': ' + items.filter(x => x[0] < 11).slice(0, 8).map(x => x[0] + '"' + x[1] + '"' + x[2]).join('  ') + ' | under11=' + items.filter(x => x[0] < 11).length + '/' + items.length;
    }));
    console.log('== ' + lang + '\n' + r.join('\n'));
    await p.context().close();
  }
  await H.close();
})();
