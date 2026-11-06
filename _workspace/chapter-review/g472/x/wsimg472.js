// Phase 472: the chapter 17 worksheet and printables picture (Workbook page 4: until the bar line)
const { start } = require('./contentharness');
(async () => {
  const H = await start(process.env.BUILD || 'drills.t472.html');
  for (const ch of ['accidentals']) {
    const p = await H.open({ path: '?book=work&ch=' + ch + '&lang=en&pages=3', w: 1800, h: 2600 });
    await p.waitForTimeout(1500); await p.evaluate(() => { document.documentElement.style.zoom = 2; }); await p.waitForTimeout(800);
    for (const pg of await p.$$('section.bk-page')) if (await pg.isVisible()) { await pg.screenshot({ path: '/tmp/claude-0/ws472-' + ch + '.png' }); break; }
    console.log(ch, p._errs.join('|')); await p.context().close();
  }
  await H.close(); process.exit(0);
})();
