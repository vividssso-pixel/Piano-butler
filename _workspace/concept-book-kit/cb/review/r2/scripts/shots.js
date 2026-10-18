// Render every printed page (EN, KO) and every screen step (390 EN/KO; 320 and 1024 spot) to PNG.
const { start } = require('/home/claude/pbtest/kit/contentharness');
const OUT = '/home/claude/pbtest/cb/review/r2/shots/';
const what = (process.env.WHAT || 'book,screen').split(',');
(async () => {
  const H = await start('drills.t485.html');
  if (what.includes('book')) for (const lang of ['en', 'ko']) {
    const p = await H.open({ path: '?book=concept&ch=p-scales&lang=' + lang, w: 900, h: 1300, dsf: +(process.env.DSF || 1.5) });
    await p.waitForTimeout(2500);
    const pages = await p.$$('[data-lb-page]');
    for (const pg of pages) { const n = await pg.getAttribute('data-lb-page'); await pg.screenshot({ path: OUT + 'p-' + lang + '-' + n + '.png' }); }
    console.log('book', lang, pages.length, 'errs', p._errs.join('|').slice(0, 300), 'reqs-db', p._reqs.filter(u => /supabase/.test(u)).length);
    await p.context().close();
  }
  if (what.includes('screen')) for (const [lang, w] of (process.env.SCR || 'en:390,ko:390').split(',').map(x => x.split(':'))) {
    const p = await H.open({ path: '?teacher=1&tool=cb-p-scales', w: +w, h: 860, lang, dsf: 1.5 });
    await p.waitForTimeout(1500);
    const steps = await p.$$('[data-lb-screen]');
    for (const s of steps) { const n = await s.getAttribute('data-lb-screen'); await s.screenshot({ path: OUT + 's-' + lang + w + '-' + n + '.png' }); }
    // the head (opener) too
    await p.screenshot({ path: OUT + 's-' + lang + w + '-top.png' });
    const hs = await p.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
    console.log('screen', lang, w, 'steps', steps.length, 'hscroll', hs, 'errs', p._errs.join('|').slice(0, 300));
    await p.context().close();
  }
  await H.close();
})();
