const { start } = require('./contentharness');
(async () => {
  const H = await start(process.env.BUILD);
  for (const ch of ['posture-hands', 'first-steps', 'note-names', 'staff']) for (const lang of ['en', 'ko']) {
    const p = await H.open({ path: '?book=lesson&ch=' + ch + '&lang=' + lang, w: 900, h: 1200 });
    await p.waitForTimeout(2400);
    const r = await p.evaluate(() => [...document.querySelectorAll('.bk-page')].map(e => { const b = e.querySelector('.bk-body'); const kids = [...b.children]; const last = kids[kids.length - 1].getBoundingClientRect(); return (b.scrollHeight - b.clientHeight) + '/' + Math.round(b.getBoundingClientRect().bottom - last.bottom); }));
    console.log(ch, lang, 'over/free', r.join(' '), p._errs.length ? 'ERR ' + p._errs[0] : '');
    await p.context().close();
  }
  await H.close();
})();
