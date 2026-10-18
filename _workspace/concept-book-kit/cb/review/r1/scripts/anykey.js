const { start } = require('/home/claude/pbtest/kit/contentharness');
(async () => {
  const H = await start('drills.t485.html');
  for (const ch of ['scales', 'key-signatures']) {
    const p = await H.open({ path: '?book=work&ch=' + ch + '&pages=6', w: 900, h: 1300 });
    await p.waitForTimeout(1200);
    const vis = await p.$$eval('section.bk-page', a => a.filter(s => getComputedStyle(s).display !== 'none').map(s => s.innerText.replace(/\s+/g, ' ').slice(0, 140)));
    console.log(ch, JSON.stringify(vis));
    await p.context().close();
  }
  const p = await H.open({ path: '?teacher=1&tool=cb-p-scales', w: 390, h: 860, lang: 'ko' });
  console.log(await p.$$eval('[data-five-checks] button', a => [...new Set(a.map(b => b.textContent))]));
  await p.context().close();
  await H.close();
})();
