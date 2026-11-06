// the guide pages' sample worksheet = each chapter's first Workbook page (pages=1), at 2x
const { start } = require('./contentharness');
(async () => {
  const H = await start(process.env.BUILD);
  for (const [ch, pg] of [['posture-hands', 1], ['first-steps', 2], ['note-names', 4], ['staff', 1]]) {
    const p = await H.open({ path: '?book=work&ch=' + ch + '&lang=en&pages=' + pg, w: 1800, h: 2600 });
    await p.waitForTimeout(1500);
    await p.evaluate(() => { document.documentElement.style.zoom = 2; });
    await p.waitForTimeout(800);
    const pages = await p.$$('section.bk-page');
    let n = 0;
    for (const pg of pages) { if (await pg.isVisible()) { await pg.screenshot({ path: 'g418/' + ch + '.png' }); n++; break; } }
    console.log(ch, 'visible pages shot', n, 'of', pages.length, p._errs.join('|'));
    await p.context().close();
  }
  await H.close(); process.exit(0);
})();
