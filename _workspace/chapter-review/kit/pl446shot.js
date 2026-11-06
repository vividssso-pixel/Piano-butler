const { start } = require('/home/claude/pbtest/kit/contentharness');
(async () => { const H = await start('drills.t446.html');
  for (const lang of ['en', 'ko']) {
    const b = await H.open({ path: '?book=lesson&ch=pulse&lang=' + lang + '&draft=1', w: 900, h: 1200, lang }); await b.waitForTimeout(2500);
    const pg = await b.$$('.bk-page'); console.log(lang, 'pages', pg.length, 'errs', b._errs.join('|').slice(0, 300));
    for (let i = 0; i < pg.length; i++) await pg[i].screenshot({ path: '/tmp/claude-0/pl-' + lang + '-' + (i + 1) + '.png' });
    await b.context().close(); }
  await H.close(); })();
