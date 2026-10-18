const { start } = require('/home/claude/pbtest/kit/contentharness');
(async () => {
  const H = await start('drills.t485.html');
  for (const w of [320, 340, 360, 375, 390]) {
    const p = await H.open({ path: '?teacher=1&tool=cb-p-scales', w, h: 860, dsf: 2 });
    const t = await p.$('[role=table]'); await t.scrollIntoViewIfNeeded(); await t.screenshot({ path: '/home/claude/pbtest/cb/review/r1/shots/table-' + w + '.png' });
    // overlapping cells: any two text spans in one row closer than their widths
    const ov = await p.evaluate(() => { const rows = [...document.querySelectorAll('[role=table] > div')]; let n = 0; rows.forEach(r => { const c = [...r.children].map(x => { const rg = document.createRange(); rg.selectNodeContents(x); const b = rg.getBoundingClientRect(); return b; }); for (let i = 1; i < c.length; i++) if (c[i].left < c[i - 1].right - 0.5) n++; }); return n; });
    const wide = await p.evaluate(() => { const W = document.documentElement.clientWidth, out = []; document.querySelectorAll('#root *').forEach(e => { const r = e.getBoundingClientRect(); if (r.width && r.right > W + 0.5) out.push(e.tagName + ' "' + (e.textContent || '').slice(0, 30) + '" ' + Math.round(r.left) + '-' + Math.round(r.right)); }); return out.slice(0, 6); });
    console.log(w + ': overlapping cell texts=' + ov + ' wide=' + JSON.stringify(wide));
    await p.context().close();
  }
  await H.close();
})();
