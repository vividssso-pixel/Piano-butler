const { start } = require('./contentharness');
(async () => {
  const H = await start(process.env.BUILD);
  for (const [lang, draft] of [['en', '&draft=1'], ['ko', '']]) {
    const p = await H.open({ path: '?book=lesson&ch=' + (process.env.CH || 'ledger-lines') + '&lang=' + lang + draft, w: 900, h: 1200 });
    await p.waitForTimeout(2600);
    const r = await p.evaluate(() => [...document.querySelectorAll('.bk-page')].map(e => { const b = e.querySelector('.bk-body'); const kids = [...b.children]; const last = kids[kids.length - 1].getBoundingClientRect(); const R = b.getBoundingClientRect().right; return (b.scrollHeight - b.clientHeight) + '/' + Math.round(b.getBoundingClientRect().bottom - last.bottom) + '/' + Math.max(0, ...[...b.querySelectorAll('*')].map(x => Math.round(x.getBoundingClientRect().right - R))); }));
    console.log(lang, 'over/free/clip', r.join(' '), p._errs.length ? 'ERR ' + p._errs.join('|').slice(0, 300) : '');
    if (lang === 'en') { const pages = await p.$$('.bk-page'); for (let i = 0; i < pages.length; i++) await pages[i].screenshot({ path: (process.env.PFX || 'll427-') + (i + 1) + '.png' }); }
    await p.context().close();
  }
  await H.close();
})();
