// QA E: every drill level opened as a student would (?drill=&level=), phone width: page errors, sideways scroll,
// text cut off in buttons and boxes, elements running past the right edge.
const { start } = require('./contentharness');
(async () => {
  const H = await start(process.env.BUILD || 'drills.t448.html'); const lang = process.env.LANGX || 'en', W = +(process.env.W || 390);
  const p0 = await H.open({ path: '', w: 800, h: 600 }); await p0.waitForTimeout(1000);
  const lv = await p0.evaluate(() => DRILLS.map(d => [d.id, ((d.concept || d).levels || []).map(l => l.n)])); await p0.context().close();
  const res = [];
  for (const [id, ns] of lv) for (const n of ns) {
    const p = await H.open({ path: '?drill=' + id + '&level=' + n + '&lang=' + lang, w: W, h: 844, lang }); await p.waitForTimeout(1800);
    const r = await p.evaluate((W) => {
      const out = [], de = document.documentElement;
      if (de.scrollWidth > de.clientWidth + 1) out.push('page scrolls sideways ' + de.scrollWidth);
      document.querySelectorAll('button, .choice-btn, [class*="chip"]').forEach(b => { const cs = getComputedStyle(b); if (b.offsetParent && b.scrollWidth > b.clientWidth + 2 && cs.overflow !== 'visible') out.push('button text cut: ' + b.textContent.trim().slice(0, 30)); });
      document.querySelectorAll('body *').forEach(e => { const r = e.getBoundingClientRect(); if (r.width > 0 && r.right > W + 2 && e.offsetParent && getComputedStyle(e).position !== 'fixed') { const sc = e.closest('[style*="overflow"]'); if (!sc || getComputedStyle(sc).overflowX === 'visible') out.push('past the edge: ' + e.tagName + ' ' + (e.textContent || '').trim().slice(0, 25) + ' ' + Math.round(r.right)); } });
      return [...new Set(out)].slice(0, 5);
    }, W);
    if (r.length || p._errs.length) res.push([id, n, r, p._errs.slice(0, 2)]);
    await p.context().close();
  }
  res.forEach(x => console.log(JSON.stringify(x))); console.log('levels with layout findings: ' + res.length);
  await H.close();
})();
