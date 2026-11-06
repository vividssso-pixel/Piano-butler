const { start } = require('./contentharness');
(async () => {
  const H = await start(process.env.BUILD);
  for (const [kind, lang] of [['lesson', 'en'], ['lesson', 'ko'], ['work', 'en'], ['teacher', 'en']]) {
    const p = await H.open({ path: '?book=' + kind + '&ch=ledger-lines&lang=' + lang, w: 900, h: 1200 });
    await p.waitForTimeout(2600);
    const pages = await p.$$('.bk-page');
    for (let i = 0; i < pages.length; i++) await pages[i].screenshot({ path: 'rev428/' + kind + '-' + lang + '-' + (i + 1) + '.png' });
    console.log(kind, lang, pages.length, p._errs.join('|'));
    await p.context().close();
  }
  await H.close();
})();
