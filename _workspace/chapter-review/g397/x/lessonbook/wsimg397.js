const { start } = require('./contentharness');
(async () => {
  const H = await start(process.env.BUILD || 'drills.t397.html');
  const p = await H.open({ path: '?book=work&ch=note-names&lang=en&pages=5', w: 1800, h: 2600 });
  await p.waitForTimeout(1500);
  await p.evaluate(() => { document.documentElement.style.zoom = 2; });
  await p.waitForTimeout(800);
  const pages = await p.$$('section.bk-page');
  let shot = null;
  for (const pg of pages) { const v = await pg.isVisible(); if (v) { await pg.screenshot({ path: 'p397/ws5.png' }); shot = 1; break; } }
  console.log('shot', shot, p._errs.join('|'));
  await H.close(); process.exit(0);
})();
