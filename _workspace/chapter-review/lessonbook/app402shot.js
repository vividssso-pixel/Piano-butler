const { start } = require('./contentharness');
(async () => {
  const H = await start(process.env.BUILD || 'drills.t402.html');
  let p = await H.open({ path: '', w: 1024, h: 1100 }); await p.waitForTimeout(1200);
  const hb = await p.$('[data-house]'); await hb.screenshot({ path: 'p402app/house-wide.png' }); await p.context().close();
  p = await H.open({ path: '', w: 390, h: 1100 }); await p.waitForTimeout(1200);
  await (await p.$('[data-house]')).screenshot({ path: 'p402app/house-tall.png' }); await p.context().close();
  for (const id of ['staff', 'whole-staff']) {
    p = await H.open({ path: '?drill=' + id, w: 390, h: 1400 }); await p.waitForTimeout(1200);
    await p.screenshot({ path: 'p402app/' + id + '-lesson.png' });
    const tab = await p.$('button:has-text("Drill")'); await tab.click(); await p.waitForTimeout(700);
    for (const n of [1, 2, 3, 4]) { const b = await p.$('button:has-text("Level ' + n + '")'); if (!b) { console.log('no level', n); continue; } await b.click(); await p.waitForTimeout(800); await p.screenshot({ path: 'p402app/' + id + '-l' + n + '.png', clip: { x: 0, y: 100, width: 390, height: 560 } }); }
    console.log(id, 'errs', p._errs.join('|'));
    await p.context().close();
  }
  await H.close(); process.exit(0);
})().catch(e => { console.error('CRASH', e); process.exit(1); });
