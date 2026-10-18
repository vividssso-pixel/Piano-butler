const { start } = require('/home/claude/pbtest/kit/contentharness');
(async () => {
  const H = await start('drills.t485.html');
  const p = await H.open({ path: '?teacher=1&tool=cb-p-scales', w: 390, h: 860, lang: 'ko' });
  const pad = await p.$('[data-cb="key-pad"]'); const k = await pad.$('g[data-key="Eb"]'); await k.click(); await p.waitForTimeout(200);
  const a = await p.$('a[href*="scale-finder"]'); console.log('href', await a.getAttribute('href')); await a.click(); await p.waitForTimeout(1500);
  console.log(await p.evaluate(() => ({ url: location.search, ko: /[가-힣]/.test(document.body.innerText.slice(0, 400)), head: document.body.innerText.slice(0, 160).replace(/\s+/g, ' '), finder: (document.body.innerText.match(/E♭[^\n]{0,30}/) || [])[0] })));
  await p.context().close(); await H.close();
})();
