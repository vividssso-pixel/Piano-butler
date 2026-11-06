// Phase 431: the guide-page worksheet and printables pictures (Workbook page 1) for chapters 4 and 6 -- the numbers moved into the boxes
const { start } = require('./contentharness');
(async () => {
  const H = await start(process.env.BUILD || 'drills.t431.html');
  for (const ch of ['staff', 'ledger-lines']) {
    const p = await H.open({ path: '?book=work&ch=' + ch + '&lang=en&pages=1', w: 1800, h: 2600 });
    await p.waitForTimeout(1500); await p.evaluate(() => { document.documentElement.style.zoom = 2; }); await p.waitForTimeout(800);
    for (const pg of await p.$$('section.bk-page')) if (await pg.isVisible()) { await pg.screenshot({ path: '/tmp/ws431-' + ch + '.png' }); break; }
    console.log(ch, p._errs.join('|')); await p.context().close();
  }
  await H.close(); process.exit(0);
})();
