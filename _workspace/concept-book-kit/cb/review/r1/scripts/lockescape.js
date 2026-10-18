const { start } = require('/home/claude/pbtest/kit/contentharness');
(async () => {
  const H = await start('drills.t485.html');
  for (const mode of [null, 'student']) {
    const p = await H.open({ path: '?tool=cb-p-scales&lock=1', w: 390, h: 860 });
    await p.evaluate((m) => { if (m) localStorage.setItem('pb_mode_v1', m); else localStorage.removeItem('pb_mode_v1'); }, mode);
    await p.reload(); await p.waitForSelector('#root *'); await p.waitForTimeout(900);
    const a = await p.$('a[href*="scale-finder"]'); await a.click(); await p.waitForTimeout(1500);
    const r = await p.evaluate(() => ({ url: location.search, words: ['Chapters', 'Toolbox', 'Practice', 'TEACHER VIEW', 'Copy student link', '← Toolbox', 'Learn the whole chapter'].filter(w => document.body.innerText.includes(w)), h: (document.querySelector('h2,h1') || {}).textContent }));
    console.log('lock=1, saved mode ' + mode + ' -> tap "Fingering →": ' + JSON.stringify(r) + ' errs=' + JSON.stringify(p._errs));
    await p.goBack(); await p.waitForTimeout(1200);
    console.log('   browser back -> ' + await p.evaluate(() => location.search));
    await p.context().close();
  }
  // teacher: the same link, what does the back button do
  const p = await H.open({ path: '?teacher=1&tool=cb-p-scales', w: 390, h: 860 });
  const a = await p.$('a[href*="scale-finder"]'); await a.click(); await p.waitForTimeout(1500);
  const b = await p.$('button:has-text("←")'); const bt = await b.innerText(); await b.click(); await p.waitForTimeout(600);
  console.log('teacher: after Fingering, back button "' + bt + '" -> ' + await p.evaluate(() => location.search));
  await p.context().close();
  await H.close();
})();
