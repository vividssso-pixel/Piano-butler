// pictures that spill out of their picture box (.lb-pic): any drawn element outside the box, per page
const { start } = require('./contentharness');
(async () => {
  const H = await start(process.env.BUILD);
  for (const kind of ['lesson', 'work']) for (const ch of ['posture-hands', 'first-steps', 'note-names', 'staff', 'whole-staff']) {
    const p = await H.open({ path: '?book=' + kind + '&ch=' + ch + '&lang=' + (process.env.LANG2 || 'en'), w: 900, h: 1200 }); await p.waitForTimeout(2400);
    await p.evaluate((v) => { document.body.dataset.inset = v; }, process.env.INSET || '0');
    const r = await p.evaluate(() => [...document.querySelectorAll('.bk-page')].map((pg, i) => {
      const out = [];
      pg.querySelectorAll('.lb-pic').forEach((box, j) => { const b = box.getBoundingClientRect(); let worst = 0; const IN = +(document.body.dataset.inset || 0);
        box.querySelectorAll('svg *, img, text').forEach(e => { if (!e.getBoundingClientRect) return; const r = e.getBoundingClientRect(); if (!r.width && !r.height) return;
          worst = Math.max(worst, b.top + IN - r.top, r.bottom - b.bottom + IN, b.left + IN - r.left, r.right - b.right + IN); });
        if (worst > 1) out.push('pic' + (j + 1) + ':' + Math.round(worst)); });
      return out.length ? 'p' + (i + 1) + ' ' + out.join(',') : null; }).filter(Boolean));
    console.log(kind, ch, r.join(' | ') || 'ok');
    await p.context().close();
  }
  await H.close();
})();
