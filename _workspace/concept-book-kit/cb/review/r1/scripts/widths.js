const { start } = require('/home/claude/pbtest/kit/contentharness');
(async () => {
  const H = await start('drills.t485.html');
  for (const lang of ['en', 'ko']) for (const w of [390, 360, 320]) {
    const p = await H.open({ path: '?teacher=1&tool=cb-p-scales', w, h: 860, lang });
    await p.waitForTimeout(800);
    const sw = await p.evaluate(() => [document.documentElement.scrollWidth, document.documentElement.clientWidth]);
    const wide = await p.evaluate(() => { const W = document.documentElement.clientWidth, out = []; document.querySelectorAll('#root *').forEach(e => { const r = e.getBoundingClientRect(); if (r.width && r.right > W + 0.5 && !e.closest('[style*="overflow"]')) out.push((e.getAttribute('data-cb') || e.getAttribute('data-cb-tool') || e.tagName) + ' ' + Math.round(r.right)); }); return [...new Set(out)].slice(0, 6); });
    // rings: rendered size
    const rings = await p.$$eval('[data-cb="key-pad"] svg[viewBox="0 0 360 360"]', a => a.map(s => Math.round(s.getBoundingClientRect().width) + '@' + Math.round(s.getBoundingClientRect().top)));
    const tbl = await p.evaluate(() => { const t = document.querySelector('[role=table]'); if (!t) return null; const r = t.getBoundingClientRect(); return [Math.round(r.width), t.scrollWidth > t.clientWidth + 1]; });
    console.log(lang + ' ' + w + ': scrollW ' + sw.join('/') + ' wide=' + JSON.stringify(wide) + ' keypad rings ' + JSON.stringify(rings) + ' table ' + JSON.stringify(tbl) + ' errs=' + JSON.stringify(p._errs));
    await p.context().close();
  }
  await H.close();
})();
