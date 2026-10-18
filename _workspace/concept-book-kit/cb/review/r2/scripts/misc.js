const { start } = require('/home/claude/pbtest/kit/contentharness');
const OUT = '/home/claude/pbtest/cb/review/r2/shots/';
(async () => {
  const H = await start('drills.t485.html');
  for (const lang of ['en', 'ko']) {
    const p = await H.open({ path: '?book=concept&ch=zzz&lang=' + lang, w: 900, h: 900, dsf: 1 }); await p.waitForTimeout(1200);
    const txt = await p.evaluate(() => document.body.innerText.trim().slice(0, 300));
    console.log('zzz', lang, JSON.stringify(txt), 'errs', p._errs.join('|'));
    await p.screenshot({ path: OUT + 'zzz-' + lang + '.png' });
    await p.context().close();
  }
  for (const lang of ['en', 'ko']) {
    const p = await H.open({ path: '?teacher=1&tool=cb-p-scales', w: 1024, h: 900, lang, dsf: 1 }); await p.waitForTimeout(1500);
    const r = await p.evaluate(() => ({ hs: document.documentElement.scrollWidth - document.documentElement.clientWidth, h: document.documentElement.scrollHeight }));
    console.log('1024', lang, JSON.stringify(r));
    await p.screenshot({ path: OUT + 'w1024-' + lang + '-top.png' });
    const st = await p.$('[data-lb-screen="3"]'); if (st) { await st.scrollIntoViewIfNeeded(); await p.waitForTimeout(300); await st.screenshot({ path: OUT + 'w1024-' + lang + '-step2.png' }); }
    const s5 = await p.$('[data-lb-screen="5"]'); if (s5) { await s5.scrollIntoViewIfNeeded(); await p.waitForTimeout(300); await s5.screenshot({ path: OUT + 'w1024-' + lang + '-step4.png' }); }
    await p.context().close();
  }
  await H.close();
})();
