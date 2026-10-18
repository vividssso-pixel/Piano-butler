const { start } = require('/home/claude/pbtest/kit/contentharness');
(async () => {
  const H = await start('drills.t489.html');
  for (const lang of ['en', 'ko']) {
    const p = await H.open({ path: '?teacher=1&tool=scale-finder&ret=home&area=pitch&concept=p-scales&room=try', w: 390, h: 900, lang });
    const labels = await p.evaluate(() => [...document.querySelectorAll('button')].map(b => b.innerText.trim()).filter(x => x.startsWith('←')));
    console.log(lang, 'reload tool, back labels:', JSON.stringify(labels));
    await p.locator('button', { hasText: /^←/ }).first().click(); await p.waitForTimeout(400);
    console.log('  -> ', await p.evaluate(() => location.search), 'errs', JSON.stringify(p._errs));
    const q = await H.open({ path: '?teacher=1&view=home&area=pitch&concept=p-scales&room=try', w: 390, h: 900, lang });
    await q.screenshot({ path: '/home/claude/pbtest/sc/shots/h2-' + lang + '-try.png', fullPage: true });
  }
  await H.close();
})();
